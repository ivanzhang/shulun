# 行列双向闭锁扫描

**状态：** `natural_shared_factor_locks_not_yet_strong_enough`

扫描同一大因子在方阵内自然产生的短差 `uP+v`。结果显示：自然共享因子的短差簇很多，但目前没有出现模数乘积超过差值的簇。因此 RCL 不能只靠“同一 q 的自然短差重复”，必须改攻“全覆盖选择迫使多个不同 q 共同约束同一短差”的更强闭锁机制。

## 摘要
- P=101 labels=1103 shifts=52 exceed=0 top={'u': 5, 'v': 1, 'abs_uP_v': 506, 'mod_count': 2, 'pair_count': 84, 'log_product': 5.53338948872752, 'log_bound': 6.226536669287466, 'product_exceeds_diff': False, 'mods_sample': [11, 23]}
- P=211 labels=3957 shifts=114 exceed=0 top={'u': 14, 'v': 4, 'abs_uP_v': 2958, 'mod_count': 2, 'pair_count': 335, 'log_product': 6.20050917404269, 'log_bound': 7.992268643270745, 'product_exceeds_diff': False, 'mods_sample': [17, 29]}
- P=401 labels=12827 shifts=226 exceed=0 top={'u': 10, 'v': -8, 'abs_uP_v': 4002, 'mod_count': 2, 'pair_count': 911, 'log_product': 6.502790045915624, 'log_bound': 8.294549515143679, 'product_exceeds_diff': False, 'mods_sample': [23, 29]}

## 下一证明义务
- 区分“自然共享同一 q 的短差”和“全覆盖选择迫使的闭锁短差”。
- 证明全覆盖标签链不仅产生同因子短差，还会迫使多个不同因子共同绑定同一短差。
- 将短差簇转化为 RCL 引理的 Q_*。
