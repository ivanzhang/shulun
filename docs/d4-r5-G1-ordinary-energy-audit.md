# D4/R5 G1 ordinary 层能量接口审计

**状态：** `ordinary_energy_candidate_exceptional_l2_verified_on_scans_not_yet_theorem`

ordinary 层并非无能量层；现有扫描中 ordinary_weight 在所有出现处都可由 exceptional_l2_sqrt 支配，观测最坏 ordinary/e_exceptional 约为 7.3343。若把 light_l2_sqrt 也加入同一局部能量池，最坏比值约为 3.9345，但这会与 light 层能量重复，不能直接用于 Cauchy 分层总和。

## 首选接口
- 定义候选：`e_ordinary := exceptional_l2_sqrt`
- ordinary 正质量行数：`291`
- 扫描最坏常数：{'source': 'd4-r5-offset-layered-scan-1e6-1p1e6-step100-T60-full.json', 'x': 1048300, 'ordinary_weight': 0.25494228505186817, 'energy': 0.03476049050565637, 'keys': ['exceptional_l2_sqrt'], 'ratio': 7.33425453275416}

## 候选能量比较
- `exceptional_only`：available=291, missing=0, worst={'source': 'd4-r5-offset-layered-scan-1e6-1p1e6-step100-T60-full.json', 'x': 1048300, 'ordinary_weight': 0.25494228505186817, 'energy': 0.03476049050565637, 'keys': ['exceptional_l2_sqrt'], 'ratio': 7.33425453275416}
- `exceptional_plus_light`：available=291, missing=0, worst={'source': 'd4-r5-offset-layered-scan-1e6-1p1e6-step100-T60-full.json', 'x': 1048300, 'ordinary_weight': 0.25494228505186817, 'energy': 0.06479674171273066, 'keys': ['exceptional_l2_sqrt', 'light_l2_sqrt'], 'ratio': 3.9344923573800545}
- `ordinary_local_available`：available=291, missing=0, worst={'source': 'd4-r5-offset-layered-scan-1e6-1p1e6-step100-T60-full.json', 'x': 1048300, 'ordinary_weight': 0.25494228505186817, 'energy': 0.03476049050565637, 'keys': ['exceptional_l2_sqrt'], 'ratio': 7.33425453275416}

## 定理化义务
- 在正文定义 e_ordinary 为 ordinary 子图诱导的 exceptional L2 半范数，而不是借用 light 能量
- 证明 ordinary_weight <= A_ordinary * e_ordinary，建议先以 A_ordinary=8 作为可审查常数目标
- 证明 e_ordinary 与 light/short/transition 的能量池正交或按平方和可合并，避免重复使用同一能量
- 若无法证明正交，则改为 ordinary 正质量触发 jump/base 证书路线
