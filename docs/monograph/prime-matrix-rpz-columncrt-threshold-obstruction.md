# RPZ ColumnCRT 阈值硬障碍审计

**状态：** `rpz_columncrt_threshold_obstruction_certificate`

## 结论

固定非零 ColumnCRT 位移门控本身不是排斥定理。对每条 unit endpoint gate，全部 unit residues 已经落在同一个 `(label=p, displacement=d mod p)` 类中，所以该类的内禀负载等于 unit support size。

因此：若阈值 `L_D` 小于这个 support size，得到的是 `ColumnCRTDefect` 被触发，而不是矛盾；若阈值 `L_D` 至少等于这个 support size，又不能排除该 gate。单靠阈值调参无法闭合全局命题。

## 总结

- 测试阈值 `L_D`：`2`。
- 门控行数：`12`。
- unit endpoint 相位总数：`404`。
- 最大单个位移类内禀负载：`48`。
- 超过测试阈值的行数：`10`。
- 超过测试阈值的相位数：`400`。
- `prod_(ell<r)(ell-1)` 公式逐行匹配：`True`。

## 阈值表

| p | r | delta | label | d mod label | unit load | min L_D | tested verdict |
|---:|---:|---:|---:|---:|---:|---:|---|
| 7 | 5 | 3 | 7 | 1 | 2 | 2 | `threshold_large_enough_but_no_exclusion` |
| 7 | 5 | 4 | 7 | 2 | 2 | 2 | `threshold_large_enough_but_no_exclusion` |
| 11 | 7 | 5 | 11 | 5 | 8 | 8 | `tested_threshold_forces_ColumnCRTDefect_not_exclusion` |
| 11 | 7 | 6 | 11 | 7 | 8 | 8 | `tested_threshold_forces_ColumnCRTDefect_not_exclusion` |
| 13 | 11 | 3 | 13 | 11 | 48 | 48 | `tested_threshold_forces_ColumnCRTDefect_not_exclusion` |
| 13 | 11 | 4 | 13 | 4 | 48 | 48 | `tested_threshold_forces_ColumnCRTDefect_not_exclusion` |
| 13 | 11 | 5 | 13 | 10 | 48 | 48 | `tested_threshold_forces_ColumnCRTDefect_not_exclusion` |
| 13 | 11 | 6 | 13 | 3 | 48 | 48 | `tested_threshold_forces_ColumnCRTDefect_not_exclusion` |
| 13 | 11 | 7 | 13 | 11 | 48 | 48 | `tested_threshold_forces_ColumnCRTDefect_not_exclusion` |
| 13 | 11 | 8 | 13 | 4 | 48 | 48 | `tested_threshold_forces_ColumnCRTDefect_not_exclusion` |
| 13 | 11 | 9 | 13 | 1 | 48 | 48 | `tested_threshold_forces_ColumnCRTDefect_not_exclusion` |
| 13 | 11 | 10 | 13 | 5 | 48 | 48 | `tested_threshold_forces_ColumnCRTDefect_not_exclusion` |

## 审稿定理

**Theorem RPZ-CCRT-OB（ColumnCRT 阈值障碍）。** 固定相邻下降 `p->r` 的 unit endpoint gate。若 `a` 遍历该 gate 的 `Q`-unit 支持，则端点标签恒为 `p`，同列见证位移余类恒为同一个非零 `d mod p`。于是

```text
R_{p,d} >= # {a mod Q: a≡rho mod r, gcd(a,Q)=1}
        = prod_{ell<r}(ell-1).
```

所以任何 `L_D < prod_{ell<r}(ell-1)` 的阈值只会把该 gate 登记为 `ColumnCRTDefect`，不能排除它；而取更大的 `L_D` 又失去排斥力。

## 剩余合法路线

1. 证明正式反例族避开 unit endpoint gate rows；
2. 提交 endpoint-PDEC 的 `U_CRT<L_PDEC` 上界；
3. 给出独立的 `ColumnCRTDefect` 排斥定理。仅调小 `L_D` 不是有效闭合方案。
