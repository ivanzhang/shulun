# 前窗口缺口与首个零行相位延迟

**状态：** `front_window_keeps_holes_before_first_zero_phase_delay`

多个 P 显示前窗口 x<P 均保留洞，而首个零行需要相位延迟到 r>P。前窗口最佳洞数通常很小但非零，说明证明可聚焦于“最后一个洞为何不能被大素数相位提前补齐”。

## 摘要
- P=5 front_min={'x': 0, 'holes': [1], 'hole_count': 1} positive_min={'x': 1, 'holes': [2], 'hole_count': 1} first_zero_r=None first/P=None
- P=7 front_min={'x': 0, 'holes': [1], 'hole_count': 1} positive_min={'x': 3, 'holes': [2], 'hole_count': 1} first_zero_r=None first/P=None
- P=11 front_min={'x': 0, 'holes': [1], 'hole_count': 1} positive_min={'x': 10, 'holes': [3], 'hole_count': 1} first_zero_r=None first/P=None
- P=13 front_min={'x': 0, 'holes': [1], 'hole_count': 1} positive_min={'x': 9, 'holes': [10], 'hole_count': 1} first_zero_r=169 first/P=13.0
- P=17 front_min={'x': 0, 'holes': [1], 'hole_count': 1} positive_min={'x': 12, 'holes': [7], 'hole_count': 1} first_zero_r=1211 first/P=71.23529411764706
- P=19 front_min={'x': 0, 'holes': [1], 'hole_count': 1} positive_min={'x': 15, 'holes': [8], 'hole_count': 1} first_zero_r=3659 first/P=192.57894736842104
- P=23 front_min={'x': 0, 'holes': [1], 'hole_count': 1} positive_min={'x': 14, 'holes': [9, 15], 'hole_count': 2} first_zero_r=59 first/P=2.5652173913043477
- P=29 front_min={'x': 0, 'holes': [1], 'hole_count': 1} positive_min={'x': 11, 'holes': [12, 18, 28], 'hole_count': 3} first_zero_r=5210 first/P=179.6551724137931
- P=31 front_min={'x': 0, 'holes': [1], 'hole_count': 1} positive_min={'x': 25, 'holes': [12, 22], 'hole_count': 2} first_zero_r=60795 first/P=1961.1290322580646

## 下一证明义务
- 分析 front_positive_min 的最后洞位置与缺失大素数相位条件。
- 证明补齐最后洞需要 x 满足某个模数系统，其最小正解超过 P。
- 将首零行问题转化为覆盖同余系统的最小正解下界。
