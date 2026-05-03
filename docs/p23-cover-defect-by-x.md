# P=23 覆盖缺口随 x 变化

对 P=23，前窗口 x<P 中没有完整覆盖；若排除 x=0 的第一行特殊洞 1，则 1<=x<P 最少仍有 2 个洞。第一个完整覆盖在 x=58，说明零行出现需要禁余类相位经过足够长的 CRT 漂移后使大素数逐点补齐小筛洞。

前窗口最少洞数：`1`

前窗口正行 `1<=x<P` 最少洞数：`2`
前窗口最佳：`{'x': 0, 'r': 1, 'covered': 21, 'holes': [1], 'is_zero': False}`

零行样本：`[{'x': 58, 'r': 59, 'covered': 22, 'holes': [], 'is_zero': True}]`

## x=0..22
- x=0 r=1 covered=21 holes=[1]
- x=1 r=2 covered=17 holes=[6, 8, 14, 18, 20]
- x=2 r=3 covered=17 holes=[1, 7, 13, 15, 21]
- x=3 r=4 covered=17 holes=[2, 4, 10, 14, 20]
- x=4 r=5 covered=16 holes=[5, 9, 11, 15, 17, 21]
- x=5 r=6 covered=19 holes=[12, 16, 22]
- x=6 r=7 covered=18 holes=[1, 11, 13, 19]
- x=7 r=8 covered=17 holes=[2, 6, 12, 18, 20]
- x=8 r=9 covered=18 holes=[7, 9, 13, 15]
- x=9 r=10 covered=18 holes=[4, 16, 20, 22]
- x=10 r=11 covered=18 holes=[3, 9, 11, 21]
- x=11 r=12 covered=18 holes=[4, 10, 16, 18]
- x=12 r=13 covered=18 holes=[1, 5, 7, 17]
- x=13 r=14 covered=18 holes=[8, 12, 14, 18]
- x=14 r=15 covered=20 holes=[9, 15]
- x=15 r=16 covered=17 holes=[2, 4, 8, 14, 22]
- x=16 r=17 covered=18 holes=[5, 11, 15, 21]
- x=17 r=18 covered=19 holes=[6, 10, 18]
- x=18 r=19 covered=18 holes=[5, 7, 17, 19]
- x=19 r=20 covered=18 holes=[2, 6, 12, 20]
- x=20 r=21 covered=18 holes=[1, 3, 7, 19]
- x=21 r=22 covered=18 holes=[4, 8, 16, 20]
- x=22 r=23 covered=19 holes=[3, 15, 17]

## 下一证明义务
- 对一般 P 证明 x<P 时禁余类族至少留一个洞。
- 分析前窗口最小洞数与 P 的增长。
- 研究大素数逐点补洞所需的相位延迟下界。
