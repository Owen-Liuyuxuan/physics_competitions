"""Content-checked PLANCKS page boundaries (physical PDF pages, one-based).

Each tuple is (number, English title, Chinese title, first page, last page).
The 2026 solution booklet uses a different order: map by content, not numbering.
"""

PAPERS = {
 'plancks-2019-final-problem': [
  (1,'Mono- and Multilayer Adsorption','单层与多层吸附',2,3),
  (2,'Quantum Optics','量子光学',4,6),
  (3,'Radical Pair Spin Chemistry','自由基对自旋化学',7,7),
  (4,'Relativistic Orbit','相对论轨道',8,8),
  (5,'Polymers and Rubber','高分子与橡胶',9,10),
  (6,'Topological Phase Transition in the 2D XY Model','二维 XY 模型中的拓扑相变',11,13),
  (7,'Higgs Mechanism','希格斯机制',14,15),
  (8,'Black Hole Picture','黑洞图像',16,17),
  (9,'Solid State Physics','固体物理',18,18),
  (10,'Freezing Front','冻结前沿',19,19)],
 'plancks-2020-final-problem': [
  (1,'A Snow Plough Problem','扫雪车问题',2,2),(2,'Dotty Dinosaur','斑点恐龙',3,3),
  (3,"Einstein’s Story",'爱因斯坦的故事',4,6),(4,'Time of Flight','飞行时间',7,8),
  (5,'Phonon-assisted Charge Transport in 2D','二维声子辅助电荷输运',9,9),
  (6,"Newcomen’s Beam Engine",'纽科门梁式蒸汽机',10,11),(7,'1888','1888 年的试题',12,12),
  (8,'Dominoes and Pendulums','多米诺骨牌与单摆',13,14),(9,'Buried Room','地心房间',15,15)],
 'plancks-2020-final-solution': [
  (1,'A Snow Plough Problem','扫雪车问题',2,4),(2,'Dotty Dinosaur','斑点恐龙',5,7),
  (3,"Einstein’s Story",'爱因斯坦的故事',8,11),(4,'Time of Flight','飞行时间',12,13),
  (5,'Phonon-assisted Charge Transport in 2D','二维声子辅助电荷输运',14,14),
  (6,"Newcomen’s Beam Engine",'纽科门梁式蒸汽机',15,19),(7,'1888','1888 年的试题',20,27),
  (8,'Dominoes and Pendulums','多米诺骨牌与单摆',28,31),(9,'Buried Room','地心房间',32,37)],
 'plancks-2021-preliminary-problem': [
  (1,'Prologue – Where Our Host Discovers Gravity','序幕：主人发现引力',3,3),
  (2,'The First Guests Arrive','首批客人到来',4,4),(3,'Coming or Going?','迎面而来还是远离而去？',5,5),
  (4,'Electrostatics by Conformal Mapping','用保角映射研究静电场',6,6),
  (5,'Parastatistics','仲统计',7,7),(6,'Condensed Matter','凝聚态物理',8,8),
  (7,'A Rotating Glass of Mead','旋转的蜂蜜酒杯',9,9),(8,'A Harmonious Synthesiser','和谐的合成器',10,10),
  (9,"Bernoulli’s Airship",'伯努利的飞艇',11,11),
  (10,'Epilogue – Where Our Host Tries to Go to Bed','尾声：主人试图入睡',12,12)],
 'plancks-2021-final-combined': [
  (1,'Quantum Mechanics','量子力学',4,4,5,8),
  (2,'Tight-Binding Models in a Magnetic Field','磁场中的紧束缚模型',10,13,14,19),
  (3,'The Evolution of Accretion Disks','吸积盘的演化',21,22,23,24),
  (4,'Fluids and Fourier Transform Applied to Solid State Physics','流体及傅里叶变换在固体物理中的应用',26,27,28,31),
  (5,'Exoplanets','系外行星',33,34,35,37),
  (6,'Cosmology','宇宙学',39,40,41,42),
  (7,'Nanotechnology','纳米技术',44,45,46,51),
  (8,'Cosmological Consequences of Scalar Fields','标量场的宇宙学效应',53,54,55,57),
  (9,'Electromagnetism','电磁学',59,59,60,61),
  (10,'Statistical Mechanics of Pressure, Buoyancy and Soap Bubbles','压强、浮力与肥皂泡的统计力学',63,67,68,76),
  (11,'Medical Physics','医学物理：磁共振',78,78,79,80),
  (12,'Optics','光学',82,84,85,88)],
 'plancks-2022-preliminary-problem': [
  (1,'The Stellar Engine Solution','恒星发动机方案',3,4),
  (2,'An Alternative Space Craft','另一种航天器',5,5),
  (3,'What If... All Energy Was Electrical?','假如所有能量都是电能？',6,6),
  (4,'Refuelling with Hemisphere Hydrodynamics','半球流体动力学与加注燃料',7,7),
  (5,'Simple Harmonic Mattresses','简谐床垫',8,11),(6,'The Firefly Dance','萤火虫之舞',12,13),
  (7,'Bending Light in a Plane','平面内的光线弯曲',14,14),(8,'A Magnetic Spa Day','磁性水疗日',15,15),
  (9,'Droplets in SPACE','太空中的液滴',16,16),(10,'Oscillators on a Train','列车上的振子',17,17)],
 'plancks-2023-final-combined': [
  (1,'Quantum Mechanics','量子力学',2,3,4,7),
  (2,'Thermodynamics','热力学',8,8,9,10),
  (3,'Quantum Optics','量子光学',11,12,13,16),
  (4,'Structure of Matter','物质结构',17,17,18,22),
  (5,'Classical Mechanics','经典力学',23,23,24,26),
  (6,'Electromagnetism','电磁学',27,28,29,33),
  (7,'Medical Physics','医学物理',34,35,36,39),
  (8,'Astrophysics of Protoplanetary Discs','原行星盘的天体物理',40,41,42,44),
  (9,'Particle Physics','粒子物理',45,45,46,49),
  (10,'General Relativity','广义相对论',50,50,51,52)],
 'plancks-2024-final-combined': [
  (1,'Moment of Inertia','转动惯量',3,3,4,5),(2,'Quaternions','四元数',6,7,8,10),
  (3,'Möbius Strip · Time Travel?','莫比乌斯带：时间旅行？',11,11,12,13),
  (4,'Icy Roof','结冰的屋顶',14,14,15,16),(5,'Floating Ring','悬浮的圆环',17,17,18,19),
  (6,'Nuclear Medicine Scan','核医学扫描',20,22,23,24),
  (7,'Dark Matter in the Galaxy','星系中的暗物质',25,25,26,26),
  (8,'Icosahedron of Resistors','电阻正二十面体',27,27,28,30),
  (9,'Molecular Zipper','分子拉链',31,31,32,34),(10,'4D Sun','四维太阳',35,35,36,37)],
 'plancks-2025-final-combined': [
  (1,'Levitation in an Anti-Helmholtz Coil','反亥姆霍兹线圈中的悬浮',3,3,4,6),
  (2,'Surface Adsorption','表面吸附',7,7,8,9),(3,'Second Sound','第二声',10,10,11,13),
  (4,'Some Questions About Our Universe','关于宇宙的几个问题',14,15,16,16),
  (5,'Black Hole Shadow','黑洞阴影',17,18,19,20),
  (6,'Pulling a Chain Upwards with Constant Force','用恒力向上提起链条',21,21,22,23),
  (7,'Stellar Observation: From Diffraction to Interferometry','恒星观测：从衍射到干涉测量',24,25,25,27),
  (8,'Graphene Nanoribbons','石墨烯纳米带',28,29,30,33),
  (9,'Quantum Grover Algorithm and Classical Collisions','量子 Grover 算法与经典碰撞',34,35,36,38)],
 'plancks-2026-final-problem': [
  (1,'Cheerios Effect – Breakfast Physics','麦圈效应：早餐物理',4,5),
  (2,'Partial Coherence and 3D Imaging','部分相干性与三维成像',6,7),
  (3,'Woodwind Instruments','木管乐器',8,10),(4,'Death Race Pilot','死亡赛车手',11,11),
  (5,'Gravitational Waves of a Binary System','双星系统的引力波',12,12),
  (6,'The Penrose Process','彭罗斯过程',13,14),(7,'Rotating Elastic Cord','旋转的弹性绳',15,15),
  (8,'Wave Function Collapse','波函数坍缩',16,17),(9,'Optical Waveguiding Principles','光波导原理',18,18)],
 'plancks-2026-final-solution': [
  (1,'Cheerios Effect – Breakfast Physics','麦圈效应：早餐物理',3,4),
  (2,'Partial Coherence and 3D Imaging','部分相干性与三维成像',5,6),
  (3,'Woodwind Instruments','木管乐器',7,8),(4,'Death Race Pilot','死亡赛车手',16,21),
  (5,'Gravitational Waves of a Binary System','双星系统的引力波',9,10),
  (6,'The Penrose Process','彭罗斯过程',11,11),(7,'Rotating Elastic Cord','旋转的弹性绳',22,25),
  (8,'Wave Function Collapse','波函数坍缩',13,15),(9,'Optical Waveguiding Principles','光波导原理',12,12)]
}


def split_paper(resource, doc, make_question):
    """Preserve historic IDs and split mixed problem/solution pages precisely."""
    rows=[]
    def bounds(first,last):
        return (first-1,35),(last-1,doc[last-1].rect.height-24)
    for entry in PAPERS[resource['id']]:
        q,title,zh,a,b,*answer=entry
        start,end=bounds(a,b)
        split_y=None
        if resource['id']=='plancks-2025-final-combined' and q==7:
            hits=doc[24].search_for('Solution')
            assert len(hits)==1, 'Ambiguous mixed-page solution boundary'
            split_y=hits[0].y0
            end=(24,split_y)
        role='problem' if answer else resource['role']
        row=make_question(resource,q,title,start,end,doc,role=role)
        row['title_zh']=zh
        row['boundary_status']='page_ranges_checked'
        row['boundary_note']='按原卷大题标题和解答起点核对页码；原图始终可对照。'
        rows.append(row)
        if answer:
            c,d=answer
            start,end=bounds(c,d)
            if split_y is not None:start=(24,split_y)
            sol=make_question(dict(resource,id=resource['id']+'-answer'),q,title+' · 参考解答',start,end,doc,role='solution')
            sol['title_zh']=zh+' · 参考解答'
            sol['boundary_status']='page_ranges_checked'
            row['solution_ids']=[sol['id']]
            rows.append(sol)
    return rows
