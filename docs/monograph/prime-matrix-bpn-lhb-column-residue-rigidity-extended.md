# BPN low-hole bucket 列残基刚性扩展审计

**状态：** `extended_q2310_turning_range_checked`

扩展检查显示 P=53 与 P=61 已无 zero bucket；P=59 仅有 8 个 zero bucket，且全部由整洞集 Delta(H)>0 直接 Hall 亏损覆盖。

| P | Q | high primes | zero | Delta(H)>0 | Delta(H)=0 | bridged critical | Delta(H)<0 | affine failures | bridge supports |
| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 53 | 2310 | `[13, 17, 19, 23, 29, 31, 37, 41, 43, 47]` | 0 | 0 | 0 | 0 | 0 | 0 | `{}` |
| 59 | 2310 | `[13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]` | 8 | 8 | 0 | 0 | 0 | 0 | `{}` |
| 61 | 2310 | `[13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]` | 0 | 0 | 0 | 0 | 0 | 0 | `{}` |

## 结论

`Q=2310` 的 low-hole zero bucket 在 `P=53` 后基本消失；唯一例外 `P=59` 的 8 个相位不需要桥洞，整洞集 Hall 亏损已直接闭合。这说明桥洞交叉是窄范围临界现象，而扩展段的主要任务转为证明 zero bucket 消失或整洞集直接亏损。
