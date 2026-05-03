# BPN Rankin smooth-core 走廊证书审计

**状态：** `finite_rankin_ledger_computable_with_lowmod_residue_report`

有限走廊证书可精确计算 smooth-core 计数，并给出 Rankin 账本和低模相位尖峰。若 Rankin 账本无法进入允许预算，下一步应调参或把最大相位尖峰登记为 low-mod core CRTDefect。

## 1. 输入摘要

- `P=1009`，`K=9`。
- 走廊总宽度 `256`，精确 smooth-core 数 `39`。
- core 密度 `0.152344`。
- omega 分布 `{2: 6, 3: 13, 4: 14, 5: 4, 6: 2}`。
- allowed budget `40.0`，Rankin pass `True`，exact pass `True`。

## 2. Rankin 网格最优

| best s | Rankin ledger | ledger/exact |
| ---: | ---: | ---: |
| 0.05 | 39.000257 | 1.000007 |

## 3. 低模相位尖峰

| modulus | max residue | max count | uniform expected | ratio |
| ---: | ---: | ---: | ---: | ---: |
| 30 | 3 | 4 | 1.300000 | 3.076923 |
| 210 | 33 | 3 | 0.185714 | 16.153846 |

## 4. 审稿含义

该证书格式把 `finite Rankin smooth-core ledger` 从口头常数义务变成可复核数据：

```text
走廊列表 -> exact core count + Rankin ledger + low-mod residue spike
```

若某个正式走廊证书的 Rankin 账本超预算，而低模相位报告显示尖峰，则该尖峰应接入 `low-mod core CRTDefect`。
