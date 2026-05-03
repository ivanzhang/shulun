# 中模数对骨架洞集的命中顺序

**状态：** `necessary_columns_are_not_early_hole_hits_for_crossing_prime`

对跨越素数 q，其在骨架洞集中的早期命中通常落在其他洞；真正必要列的命中序号足够靠后，使得 x0+m*s>=P。这提示必要列不是任意洞，而是完整方案中与后续模数兼容的延迟洞。

## 摘要
- P=13 q=5 necessary=1 rank=3 threshold=3 order=[{'hole': 5, 's': 0, 'x': 0, 'crosses_P': False}, {'hole': 7, 's': 1, 'x': 6, 'crosses_P': False}, {'hole': 1, 's': 3, 'x': 18, 'crosses_P': True}, {'hole': 11, 's': 3, 'x': 18, 'crosses_P': True}]
- P=17 q=7 necessary=3 rank=2 threshold=1 order=[{'hole': 9, 's': 4, 'x': 130, 'crosses_P': True}, {'hole': 3, 's': 5, 'x': 160, 'crosses_P': True}, {'hole': 11, 's': 6, 'x': 190, 'crosses_P': True}]
- P=19 q=5 necessary=3 rank=5 threshold=3 order=[{'hole': 9, 's': 0, 'x': 4, 'crosses_P': False}, {'hole': 15, 's': 1, 'x': 10, 'crosses_P': False}, {'hole': 1, 's': 2, 'x': 16, 'crosses_P': False}, {'hole': 7, 's': 3, 'x': 22, 'crosses_P': True}, {'hole': 3, 's': 4, 'x': 28, 'crosses_P': True}, {'hole': 13, 's': 4, 'x': 28, 'crosses_P': True}]
- P=23 q=5 necessary=11 rank=6 threshold=4 order=[{'hole': 3, 's': 0, 'x': 4, 'crosses_P': False}, {'hole': 5, 's': 1, 'x': 10, 'crosses_P': False}, {'hole': 15, 's': 1, 'x': 10, 'crosses_P': False}, {'hole': 17, 's': 2, 'x': 16, 'crosses_P': False}, {'hole': 9, 's': 3, 'x': 22, 'crosses_P': False}, {'hole': 11, 's': 4, 'x': 28, 'crosses_P': True}, {'hole': 21, 's': 4, 'x': 28, 'crosses_P': True}]
- P=29 q=7 necessary=6 rank=5 threshold=1 order=[{'hole': 2, 's': 0, 'x': 19, 'crosses_P': False}, {'hole': 12, 's': 2, 'x': 79, 'crosses_P': True}, {'hole': 26, 's': 2, 'x': 79, 'crosses_P': True}, {'hole': 8, 's': 4, 'x': 139, 'crosses_P': True}, {'hole': 6, 's': 5, 'x': 169, 'crosses_P': True}, {'hole': 20, 's': 5, 'x': 169, 'crosses_P': True}, {'hole': 18, 's': 6, 'x': 199, 'crosses_P': True}]
- P=31 q=7 necessary=3 rank=5 threshold=1 order=[{'hole': 15, 's': 1, 'x': 44, 'crosses_P': True}, {'hole': 29, 's': 1, 'x': 44, 'crosses_P': True}, {'hole': 9, 's': 2, 'x': 74, 'crosses_P': True}, {'hole': 23, 's': 2, 'x': 74, 'crosses_P': True}, {'hole': 3, 's': 3, 'x': 104, 'crosses_P': True}, {'hole': 17, 's': 3, 'x': 104, 'crosses_P': True}, {'hole': 5, 's': 5, 'x': 164, 'crosses_P': True}, {'hole': 27, 's': 6, 'x': 194, 'crosses_P': True}]

## 下一证明义务
- 解释为什么早期命中的洞不能作为完整方案必要列：它们会破坏后续唯一覆盖结构。
- 研究后续模数兼容性如何选择延迟洞。
- 将必要列定义改为全方案兼容必要列，而非当前骨架的任意洞。
