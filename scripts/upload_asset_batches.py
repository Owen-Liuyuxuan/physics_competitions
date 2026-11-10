#!/usr/bin/env python3
"""Seed an unpublished private source repository in bounded pushes.

Credential arrives only via hidden stdin. Partial trees are never deployed;
the normal Sites helper still pushes/packages the complete final main branch.
The original unpublished HEAD is retained under a backup ref before assembly.
"""
import json
import os
import subprocess
import sys
import tempfile
import termios

def main():
    attrs=termios.tcgetattr(sys.stdin)
    hidden=termios.tcgetattr(sys.stdin);hidden[3]&=~termios.ECHO
    termios.tcsetattr(sys.stdin,termios.TCSANOW,hidden)
    print('Ready for source credential JSON on hidden stdin.',flush=True)
    try:credential=json.loads(sys.stdin.readline())
    finally:termios.tcsetattr(sys.stdin,termios.TCSANOW,attrs)
    env=dict(os.environ,GIT_TERMINAL_PROMPT='0')
    for key in list(env):
        if key.startswith('GIT_TRACE') or key=='GIT_CURL_VERBOSE':env.pop(key)
    env['SITES_GIT_AUTHORIZATION']='Authorization: Bearer '+credential['token']
    remote=credential['remote_url']
    auth=['-c','credential.helper=','-c','http.extraHeader=','-c','http.followRedirects=false',f'--config-env=http.{remote}.extraHeader=SITES_GIT_AUTHORIZATION']
    def git(args,content=None,network=False):
        result=subprocess.run(['git',*(auth if network else []),*args],input=content,text=True,env=env,capture_output=True)
        if result.returncode:
            raise RuntimeError(result.stderr.replace(credential['token'],'[redacted]'))
        return result.stdout.strip()
    if '--status' in sys.argv:
        print(git(['ls-remote','--heads',remote],network=True),flush=True)
        return
    main_ref='refs/heads/'+credential['branch']
    if git(['ls-remote','--heads',remote,main_ref],network=True):
        raise RuntimeError('Main is already published; do not rebuild its history.')
    initial=git(['rev-parse','HEAD'])
    if git(['symbolic-ref','HEAD'])!=main_ref:raise RuntimeError('Unexpected local branch')
    rows=[]
    for line in git(['ls-tree','-rl','HEAD']).splitlines():
        meta,path=line.split('\t',1);mode,kind,sha,size=meta.split()
        if kind=='blob':rows.append((mode,sha,int(size),path))
    # Each raw group stays well below 64 MiB even before compression.
    groups=[];current=[];total=0
    for row in rows:
        if total+row[2]>32*1024*1024 and current:groups.append(current);current=[];total=0
        current.append(row);total+=row[2]
    if current:groups.append(current)
    with tempfile.TemporaryDirectory(prefix='physics-sites-index-') as temp:
        env['GIT_INDEX_FILE']=temp+'/index'
        commits=[]
        for i,group in enumerate(groups,1):
            git(['read-tree','--empty'])
            git(['update-index','--index-info'],''.join(f'{m} {s}\t{p}\n' for m,s,_,p in group))
            tree=git(['write-tree'])
            commit=git(['-c','user.name=Sites','-c','user.email=sites@users.noreply.openai.com','commit-tree',tree],f'Private archive asset batch {i}\n')
            ref=f'refs/heads/archive-assets-{i}'
            existing=git(['ls-remote','--heads',remote,ref],network=True)
            if existing:raise RuntimeError('Staging ref already exists; inspect before retry: '+ref)
            git(['update-ref',ref,commit])
            print(f'Uploading asset batch {i}/{len(groups)}: {sum(r[2] for r in group)/1048576:.1f} MiB',flush=True)
            git(['push',remote,f'{commit}:{ref}'],network=True)
            commits.append(commit)
            print(f'Uploaded asset batch {i}/{len(groups)}',flush=True)
    tree=git(['rev-parse',initial+'^{tree}'])
    parents=[v for sha in commits for v in ['-p',sha]]
    assembled=git(['-c','user.name=Sites','-c','user.email=sites@users.noreply.openai.com','commit-tree',tree,*parents],'Assemble private archive batches\n')
    git(['update-ref','refs/heads/archive-before-batching-'+initial[:12],initial])
    git(['update-ref',main_ref,assembled,initial])
    print('Asset batches assembled; original unpublished history retained. Run the Sites helper to push/package main.',flush=True)

if __name__=='__main__':main()
