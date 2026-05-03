# 前窗口残洞集偏序扫描

**状态：** `hole_sets_have_many_descents_but_minimal_cores_remain_nonempty`

前窗口洞集并非整体反链：存在 H(y) 严格包含 H(x) 的局部净消洞。但所有极小洞集仍非空；因此 RCC 不能表述为任意两相位的偏序反链，必须表述为‘沿可实现的全覆盖补洞链，极小残洞核不可跨窗消失’。

## 摘要
- P=13 hist={1: 1, 2: 1, 3: 10} min=1 min_rows=[{'x': 9, 'holes': [10]}] descents=3
- P=17 hist={1: 1, 2: 1, 3: 5, 4: 9} min=1 min_rows=[{'x': 12, 'holes': [7]}] descents=4
- P=19 hist={1: 1, 2: 2, 3: 5, 4: 7, 5: 2, 6: 1} min=1 min_rows=[{'x': 15, 'holes': [8]}] descents=8
- P=23 hist={2: 1, 3: 3, 4: 12, 5: 5, 6: 1} min=2 min_rows=[{'x': 14, 'holes': [9, 15]}] descents=4
- P=29 hist={3: 3, 4: 8, 5: 9, 6: 6, 7: 2} min=3 min_rows=[{'x': 11, 'holes': [12, 18, 28]}, {'x': 18, 'holes': [1, 19, 25]}, {'x': 24, 'holes': [5, 13, 23]}] descents=4
- P=31 hist={2: 1, 3: 1, 4: 7, 5: 10, 6: 9, 7: 2} min=2 min_rows=[{'x': 25, 'holes': [12, 22]}] descents=4
- P=37 hist={2: 1, 3: 2, 4: 2, 5: 11, 6: 10, 7: 5, 8: 4, 9: 1} min=2 min_rows=[{'x': 36, 'holes': [29, 35]}] descents=6
- P=41 hist={3: 1, 4: 5, 5: 5, 6: 11, 7: 10, 8: 6, 9: 2} min=3 min_rows=[{'x': 32, 'holes': [7, 9, 15]}] descents=2
- P=43 hist={3: 2, 4: 5, 5: 5, 6: 8, 7: 9, 8: 10, 9: 3} min=3 min_rows=[{'x': 31, 'holes': [28, 34, 40]}, {'x': 32, 'holes': [5, 23, 33]}] descents=3
- P=47 hist={3: 1, 4: 3, 5: 6, 6: 9, 7: 8, 8: 13, 9: 5, 10: 1} min=3 min_rows=[{'x': 46, 'holes': [17, 41, 45]}] descents=1
- P=53 hist={4: 2, 5: 5, 6: 8, 7: 11, 8: 8, 9: 11, 10: 5, 11: 2} min=4 min_rows=[{'x': 25, 'holes': [2, 36, 42, 48]}, {'x': 34, 'holes': [9, 21, 29, 45]}] descents=0
- P=59 hist={3: 1, 5: 2, 6: 8, 7: 10, 8: 16, 9: 9, 10: 6, 11: 4, 13: 2} min=3 min_rows=[{'x': 42, 'holes': [25, 43, 53]}] descents=1

## 下一证明义务
- 识别前窗口洞集偏序中的极小元，研究其残洞核类型。
- 证明极小元不能为空；这比任意相位净消洞不等式更准确。
- 把极小残洞核与 CRT 列均衡、镜像相位和相邻商互质约束连接。
