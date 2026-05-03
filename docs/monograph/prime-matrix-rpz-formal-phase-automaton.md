# RPZ Formal-Family 下降相位自动机证书

**状态：** `rpz_formal_phase_automaton_certificate`

## 总结

- 最大起始素数层：`13`。
- 转移行数：`5`。
- 接受集行数：`6`。
- 当前起始行数：`6`。
- 当前起始行被自动机接受数：`6`。
- 全局 formal-family 是否闭合：`False`。

## 接受相位表

| p | modulus P(p) | accepted | rejected | accepted density |
|---:|---:|---:|---:|---:|
| 2 | 2 | 2 | 0 | 1.000000 |
| 3 | 6 | 6 | 0 | 1.000000 |
| 5 | 30 | 30 | 0 | 1.000000 |
| 7 | 210 | 126 | 84 | 0.600000 |
| 11 | 2310 | 990 | 1320 | 0.428571 |
| 13 | 30030 | 3510 | 26520 | 0.116883 |

## 当前起始行追踪

| start p | start row | start phase | accepted | trace deltas |
|---:|---:|---:|---|---|
| 5 | 439 | 19 | `True` | `['5->3:d=0,g=2', '3->2:d=0,g=1']` |
| 7 | 2940 | 0 | `True` | `['7->5:d=2,g=2', '5->3:d=2,g=2', '3->2:d=1,g=1']` |
| 7 | 9930 | 60 | `True` | `['7->5:d=2,g=2', '5->3:d=2,g=2', '3->2:d=1,g=1']` |
| 7 | 9931 | 61 | `True` | `['7->5:d=0,g=2', '5->3:d=0,g=2', '3->2:d=0,g=1']` |
| 11 | 123 | 123 | `True` | `['11->7:d=2,g=4', '7->5:d=1,g=2', '5->3:d=2,g=2', '3->2:d=1,g=1']` |
| 13 | 11622 | 11622 | `True` | `['13->11:d=1,g=2', '11->7:d=0,g=4', '7->5:d=1,g=2', '5->3:d=2,g=2', '3->2:d=1,g=1']` |

## 证书定理

定义 `A_p` 为模 `P(p)` 的接受相位集合：`a mod P(p)` 属于 `A_p` 当且仅当 canonical 相邻素数下降每一步满足 `delta<=p-r` 并最终到达 `p=2`。则：

```text
formal start phase in A_p  =>  formal descent to p=2 contradiction；
formal start phase not in A_p => first-grid-fail seam => SAE/PDEC/ColumnCRT。
```

当前 BCB-Core 账本的所有起始行都属于 `A_p`，因此路线 A 在当前账本中闭合。

## 剩余缺口

本证书仍未证明任意正式反例族的起始相位必属于 `A_p`。下一步真正目标是证明 formal-family 的起始相位避开 rejected set，或把 rejected set 的命中送入已经物化的 seam/PDEC/ColumnCRT 证书链。
