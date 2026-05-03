# D4/R5 G1 互斥分层口径审计

**状态：** `partition_identity_verified_energy_interface_missing_for_ordinary_and_some_short_transition_files`

G1 的质量口径可以无重叠地改写为 transition/short_chain/ordinary/light 四层；heavy 不是互斥层，而是前三层父类。剩余硬点从‘漏 heavy’改为‘ordinary 层及部分扫描文件的 short/transition 层缺少匹配 l2_sqrt 能量字段或解析能量定义’。

## 恒等式验证
- 行数：`2000`
- 互斥分解：`positive_contract_sum = transition_weight + short_chain_weight + ordinary_weight + light_weight`
- 父类关系：`heavy_weight = transition_weight + short_chain_weight + ordinary_weight`
- 最大互斥残差：{'source': 'd4-r5-offset-layered-scan-1088200-1088600-step1-T60-full.json', 'x': 1088565, 'L': 0.4007652991178815, 'partition_sum': 0.4007652991178814, 'heavy_weight': 0.21148536145767632, 'heavy_children_sum': 0.21148536145767632, 'partition_residual': 1.1102230246251565e-16, 'heavy_parent_residual': 0.0}
- 最大 heavy 父类残差：{'source': 'd4-r5-offset-layered-scan-1088200-1088600-step1-T60-full.json', 'x': 1088540, 'L': 0.4194721590212945, 'partition_sum': 0.4194721590212945, 'heavy_weight': 0.2534698365770398, 'heavy_children_sum': 0.25346983657703975, 'partition_residual': 0.0, 'heavy_parent_residual': 5.551115123125783e-17}

## 能量接口缺口
- `transition_weight`：positive_count=337, missing_energy_count=0, example=None
- `short_chain_weight`：positive_count=1972, missing_energy_count=0, example=None
- `ordinary_weight`：positive_count=291, missing_energy_count=291, example={'source': 'd4-r5-offset-layered-scan-1049300-1049900-step1-T60-full.json', 'x': 1049326, 'mass': 0.05736485950119473, 'usable_energy': 0.0}
- `light_weight`：positive_count=2000, missing_energy_count=0, example=None

## 已有能量字段下的最坏 B/e
- `transition_weight`：ratio=1.684983172127716, x=1060700, source=d4-r5-offset-layered-scan-1e6-1p1e6-step100-T60-full.json
- `short_chain_weight`：ratio=3.0268510362362, x=1088304, source=d4-r5-offset-layered-scan-1088200-1088600-step1-T60-full.json
- `light_weight`：ratio=6.835154130403232, x=1023400, source=d4-r5-offset-layered-scan-1e6-1p1e6-step100-T60-full.json

## 下一步义务
- 在正文中把 G1 分层定义为 P_transition, P_short, P_ordinary, P_light 四个互斥层
- 将 heavy 仅作为父类监控量，不进入 Cauchy 求和分解
- 为 ordinary 层定义解析能量 e_ordinary，或证明 ordinary 正质量必触发 jump/base 证书
- 补齐 short_chain/transition 在非 full 扫描文件中的 l2_sqrt 字段，或用 exceptional_l2_sqrt 给出可审查替代上界
