# 中模数跨越步骤几何分析

**状态：** `crossing_t_exceeds_threshold_because_early_phases_miss_required_holes`

跨越步骤中，t 必须至少达到 threshold=ceil((P-x0)/m)。逐例看，所有 s<threshold 的早期相位下，新增 q 的禁余类没有以正确方式补齐骨架洞集；必要列命中发生在跨越之后。

## 摘要
- P=13 q=5 c=1 x0=0 m=6 t=3 threshold=3 x1=18 holes_before=[1, 5, 7, 11] early=[{'s': 0, 'x': 0, 'residue': 0, 'hits': [5, 10], 'hits_holes': [5]}, {'s': 1, 'x': 6, 'residue': 2, 'hits': [2, 7, 12], 'hits_holes': [7]}, {'s': 2, 'x': 12, 'residue': 4, 'hits': [4, 9], 'hits_holes': []}]
- P=17 q=7 c=3 x0=10 m=30 t=5 threshold=1 x1=160 holes_before=[3, 9, 11] early=[{'s': 0, 'x': 10, 'residue': 5, 'hits': [5, 12], 'hits_holes': []}]
- P=19 q=5 c=3 x0=4 m=6 t=4 threshold=3 x1=28 holes_before=[1, 3, 7, 9, 13, 15] early=[{'s': 0, 'x': 4, 'residue': 4, 'hits': [4, 9, 14], 'hits_holes': [9]}, {'s': 1, 'x': 10, 'residue': 0, 'hits': [5, 10, 15], 'hits_holes': [15]}, {'s': 2, 'x': 16, 'residue': 1, 'hits': [1, 6, 11, 16], 'hits_holes': [1]}]
- P=23 q=5 c=11 x0=4 m=6 t=4 threshold=4 x1=28 holes_before=[3, 5, 9, 11, 15, 17, 21] early=[{'s': 0, 'x': 4, 'residue': 3, 'hits': [3, 8, 13, 18], 'hits_holes': [3]}, {'s': 1, 'x': 10, 'residue': 0, 'hits': [5, 10, 15, 20], 'hits_holes': [5, 15]}, {'s': 2, 'x': 16, 'residue': 2, 'hits': [2, 7, 12, 17, 22], 'hits_holes': [17]}, {'s': 3, 'x': 22, 'residue': 4, 'hits': [4, 9, 14, 19], 'hits_holes': [9]}]
- P=29 q=7 c=6 x0=19 m=30 t=5 threshold=1 x1=169 holes_before=[2, 6, 8, 12, 18, 20, 26] early=[{'s': 0, 'x': 19, 'residue': 2, 'hits': [2, 9, 16, 23], 'hits_holes': [2]}]
- P=31 q=7 c=3 x0=14 m=30 t=3 threshold=1 x1=104 holes_before=[3, 5, 9, 15, 17, 23, 27, 29] early=[{'s': 0, 'x': 14, 'residue': 0, 'hits': [7, 14, 21, 28], 'hits_holes': []}]

## 下一证明义务
- 证明早期 s<threshold 时 q 的命中列不能覆盖必要洞 c。
- 将 holes_before 的位置与 q 的等差命中类比较。
- 推导 t>=threshold 的一般不等式。
