# D4/R5 G1 直接 Neff 二阶能量审计

**状态：** `direct_Neff64_route_replaces_fixed_topr_tail_route`

直接 Neff 审计合并 step100 全局扫描与 Case A 密邻域后，最大 Neff≈47.78，仍远低于 64。最坏点不是固定 top-r 头部失败本身，而是 tau 桶较均衡混合；各桶均贡献平方能量，因此二阶能量界比 top-r 半质量更稳定。

## 最坏记录
- {'source': 'docs/d4-r5-O2-caseA-neighborhood-1023000-1023800-step1.json', 'x': 1023427, 'count': 95, 'S': 0.13741097199809407, 'sqrtQ': 0.019878973066740763, 'Neff': 47.780966769787746, 'ratio': 6.912377794202784, 'bucket_mass_share': {'tau_le_4': 0.16716398357489698, 'tau_5_8': 0.15754501747611543, 'tau_9_16': 0.297760852373164, 'tau_17_32': 0.2905983585947855, 'tau_33_59': 0.08693178798103805, 'heavy_short': 0.0}, 'bucket_square_share': {'tau_le_4': 0.046614871305962875, 'tau_5_8': 0.09056095681351997, 'tau_9_16': 0.26770028760508063, 'tau_17_32': 0.41455475629089406, 'tau_33_59': 0.18056912798454242, 'heavy_short': 0.0}, 'top10': [{'weight': 0.006043675149438258, 'tau_sum': 33, 'count': 7, 'offset': 8}, {'weight': 0.005901706334568413, 'tau_sum': 48, 'count': 4, 'offset': 29}, {'weight': 0.005543719143673169, 'tau_sum': 32, 'count': 4, 'offset': 13}, {'weight': 0.005171733928497282, 'tau_sum': 18, 'count': 1, 'offset': 125}, {'weight': 0.004657784038283013, 'tau_sum': 14, 'count': 2, 'offset': 69}, {'weight': 0.004638579363296409, 'tau_sum': 24, 'count': 3, 'offset': 61}, {'weight': 0.004607585531560955, 'tau_sum': 24, 'count': 1, 'offset': 53}, {'weight': 0.0042032073362360915, 'tau_sum': 28, 'count': 4, 'offset': 143}, {'weight': 0.003996148726461814, 'tau_sum': 20, 'count': 2, 'offset': 317}, {'weight': 0.0036300336487965694, 'tau_sum': 27, 'count': 2, 'offset': 173}]}
- Neff64 violations：`0`

## 证明归约
- 正式 O2 接口应为直接 S^2 <= 64 Q
- 证明策略应建立 tau 桶二阶能量账本：每个 tau 桶有质量份额与平方份额的联合下界
- 固定 top-r/tail44 证书只能作为启发，不进入最终闭合链条
- 下一步提取 tau 桶质量-平方联合不等式，目标给出 Q/S^2 >= 1/64
