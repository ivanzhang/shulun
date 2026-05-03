# BPN LHB 尾段显式常数审计

在候选显式常数包下，连续乘积尾段从 stable_from_in_scan 起闭合；低于该阈值仍应使用有限精确证书。

## 1. 常数包

- `Q`: `2310`
- `phi(Q)/Q`: `0.2077922077922078`
- `Hmax` 安全加性常数: `5`
- `max_excess`: `{'length': 227, 'hmax': 52, 'excess': 4.8311688311688314}`
- `mertens_eps`: `0.03`
- `pi_upper_constant`: `1.25506`
- 外部来源：Rosser--Schoenfeld, *Approximate formulas for some functions of prime numbers*, Illinois J. Math. 6(1), 64--94, 1962。
- 公式定位：Corollary 1 `(3.5),(3.6)`, p. 69 给出 `pi` 上下界；Theorem 7 `(3.26)`,
  p. 70 给出 Mertens 乘积上界。
- 使用范围：`P>=13208` 时 `floor(P/5)>=2641`，足以把 Rosser--Schoenfeld 的
  `1+1/(2log^2 x)` 型 Mertens 因子放宽为 `1.03`；素数计数上下界输入点也满足
  对应阈值。

## 2. 解析余量

- `last_bad`: `13207`
- `stable_from_in_scan`: `13208`
- `min_margin`: `{'p': 2948, 'margin': -16.421548538620527}`

| P | analytic margin |
| ---: | ---: |
| 233 | -11.176921 |
| 1009 | -14.424539 |
| 13208 | 0.000436 |
| 25077 | 33.080810 |
| 100000 | 310.491681 |
| 300000 | 1173.083903 |

## 3. 审稿结论

该报告不替代外部显式 Mertens/素数计数定理；它只核算这些标准输入一旦接受后，
需要保留到哪个有限阈值。当前默认常数包下，`P>=stable_from_in_scan` 由解析余量闭合，
`233<=P<stable_from_in_scan` 应使用精确乘积有限证书。

引用接口已登记在 `external-theorem-index.md`。若常数包改变，必须重新生成本审计。
