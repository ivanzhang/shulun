# D4/R5 G1 统一 exceptional 能量接口审计

**状态：** `unified_exceptional_Aeff_candidate_has_scan_margin_not_yet_theorem`

若将 G1 能量口径改为单一 exceptional_l2_sqrt，则 ordinary、transition、short_chain、light 的总正质量 L 在扫描中统一受控，最坏 A_eff 约 12.6822，距离 18.113 仍有约 5.43 余量。这避免了对同一 exceptional 能量的分层重复使用问题。

## 核心比值
- 行数：`2000`
- 阈值参考：For L_cap=0.48 and eta=0.015, sufficient A_eff <= 18.113...
- 最坏 `L/exceptional_l2_sqrt`：{'source': 'd4-r5-offset-layered-scan-1e6-1p1e6-step100-T60-full.json', 'x': 1048300, 'L': 0.44083675266307654, 'ordinary_weight': 0.25494228505186817, 'nonordinary_exceptional_mass': 0.18589446761120842, 'exceptional_l2_sqrt': 0.03476049050565637, 'L_over_exceptional_l2_sqrt': 12.682121174076695, 'nonordinary_over_exceptional_l2_sqrt': 5.347866641322536, 'ordinary_over_exceptional_l2_sqrt': 7.33425453275416}
- 最坏非 ordinary 质量比：{'source': 'd4-r5-offset-layered-scan-1e6-1p1e6-step100-T60-full.json', 'x': 1023400, 'L': 0.12864024379619862, 'ordinary_weight': 0.0, 'nonordinary_exceptional_mass': 0.12864024379619862, 'exceptional_l2_sqrt': 0.019258766518065816, 'L_over_exceptional_l2_sqrt': 6.6795681683729216, 'nonordinary_over_exceptional_l2_sqrt': 6.6795681683729216, 'ordinary_over_exceptional_l2_sqrt': 0.0}
- 最坏 ordinary 质量比：{'source': 'd4-r5-offset-layered-scan-1e6-1p1e6-step100-T60-full.json', 'x': 1048300, 'L': 0.44083675266307654, 'ordinary_weight': 0.25494228505186817, 'nonordinary_exceptional_mass': 0.18589446761120842, 'exceptional_l2_sqrt': 0.03476049050565637, 'L_over_exceptional_l2_sqrt': 12.682121174076695, 'nonordinary_over_exceptional_l2_sqrt': 5.347866641322536, 'ordinary_over_exceptional_l2_sqrt': 7.33425453275416}
- 对 18.113 的扫描余量：`5.430878825923305`

## 定理化义务
- 证明 exceptional_l2_sqrt 的定义覆盖 transition/short_chain/light 三层，且 ordinary 层也可被同一 exceptional 场的 L2 半范数控制
- 将 Lyapunov 能量 E_* 从分层 sqrt 和改写为统一 exceptional 能量或证明两者的安全替代关系
- 以 A_eff=13 或 A_eff=14 作为显式定理常数，重新检查 D_* >= 0.015 的参数余量
- 确认统一 exceptional 能量在递归尺度 j 下可传递，并不破坏 stable payment telescope
