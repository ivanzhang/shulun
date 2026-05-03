# RPZ Rejected Phase 吸收证书

**状态：** `rpz_rejected_phase_absorption_certificate`

## 总结

- 起始素数层数：`6`。
- rejected phase 总数：`27924`。
- 不同首失败 seam 数：`12`。
- 已物化 seam 行数：`12`。
- 未覆盖 rejected 样例数：`0`。
- rejected 是否全部被已物化 seam 覆盖：`True`。

## 按起始素数分解

| start p | modulus | rejected | first-fail rows | covered |
|---:|---:|---:|---:|---|
| 2 | 2 | 0 | 0 | `True` |
| 3 | 6 | 0 | 0 | `True` |
| 5 | 30 | 0 | 0 | `True` |
| 7 | 210 | 84 | 2 | `True` |
| 11 | 2310 | 1320 | 4 | `True` |
| 13 | 30030 | 26520 | 12 | `True` |

## 全局首失败 seam 表

| first fail key [p,r,delta,rho] | count | materialized |
|---|---:|---|
| `[7, 5, 3, 2]` | 1542 | `True` |
| `[7, 5, 4, 4]` | 1542 | `True` |
| `[11, 7, 5, 5]` | 1500 | `True` |
| `[11, 7, 6, 3]` | 1500 | `True` |
| `[13, 11, 3, 5]` | 2730 | `True` |
| `[13, 11, 4, 10]` | 2730 | `True` |
| `[13, 11, 5, 4]` | 2730 | `True` |
| `[13, 11, 6, 9]` | 2730 | `True` |
| `[13, 11, 7, 3]` | 2730 | `True` |
| `[13, 11, 8, 8]` | 2730 | `True` |
| `[13, 11, 9, 2]` | 2730 | `True` |
| `[13, 11, 10, 7]` | 2730 | `True` |

## 证书定理

对当前自动机范围内的任意起始相位：

```text
phase in A_p     => canonical descent reaches p=2；
phase not in A_p => first failure is one of the materialized first-grid-fail seam rows。
```

因此路线 A 的 rejected set 不再是未定义逃逸；它已经完全回流到 seam/PDEC/ColumnCRT 证书链。

## 剩余缺口

本证书仍不排除 seam 出口。全局闭合还需要二选一：证明 formal-family 起始相位从不进入 rejected set；或排除已物化 seam/PDEC/ColumnCRT 出口。
