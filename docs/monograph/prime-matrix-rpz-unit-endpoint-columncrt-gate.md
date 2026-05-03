# RPZ Unit Endpoint ColumnCRT 门控证书

**状态：** `rpz_unit_endpoint_columncrt_gate_certificate`

## 关键恒等式

设相邻下降 `p->r`、`g=p-r`、`delta=-(a-1)g mod r`，并处在 first-grid-fail seam：`g<delta<r`。若 `a≡rho mod r`，则 unit endpoint `ap` 在下层 `r` 网格中的列为

```text
c ≡ p*rho mod r = r+g-delta。
```

因此 `c` 是固定的非平凡列 `1<=c<r`。若同列素数见证为 `pi=h*r+c`，则端点下层行号满足

```text
H*r+c = a*p,  so  H ≡ -c*r^{-1} mod p。
```

于是位移 `d=h-H mod p` 与 `a` 无关；且若 `pi` 是素数并且 `pi!=p`，则 `d` 不能为 `0 mod p`。这正是 `ColumnCRT` 的固定非零位移余类入口。

## 总结

- 门控行数：`12`。
- unit endpoint 相位总数：`404`。
- 列恒等式通过行数：`12`。
- 有显式同列素数见证行数：`12`。
- 非零位移通过行数：`12`。
- unit residues 固定列通过行数：`12`。
- unit residues 固定 `H mod p` 通过行数：`12`。

## 门控表

| p | r | delta | rho | c | unit | witness pi | witness row | H mod p | d mod p | verdict |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 7 | 5 | 3 | 2 | 4 | 2 | 19 | 3 | 2 | 1 | `routes_to_fixed_nonzero_columncrt_residue` |
| 7 | 5 | 4 | 4 | 3 | 2 | 3 | 0 | 5 | 2 | `routes_to_fixed_nonzero_columncrt_residue` |
| 11 | 7 | 5 | 5 | 6 | 8 | 13 | 1 | 7 | 5 | `routes_to_fixed_nonzero_columncrt_residue` |
| 11 | 7 | 6 | 3 | 5 | 8 | 5 | 0 | 4 | 7 | `routes_to_fixed_nonzero_columncrt_residue` |
| 13 | 11 | 3 | 5 | 10 | 48 | 43 | 3 | 5 | 11 | `routes_to_fixed_nonzero_columncrt_residue` |
| 13 | 11 | 4 | 10 | 9 | 48 | 31 | 2 | 11 | 4 | `routes_to_fixed_nonzero_columncrt_residue` |
| 13 | 11 | 5 | 4 | 8 | 48 | 19 | 1 | 4 | 10 | `routes_to_fixed_nonzero_columncrt_residue` |
| 13 | 11 | 6 | 9 | 7 | 48 | 7 | 0 | 10 | 3 | `routes_to_fixed_nonzero_columncrt_residue` |
| 13 | 11 | 7 | 3 | 6 | 48 | 17 | 1 | 3 | 11 | `routes_to_fixed_nonzero_columncrt_residue` |
| 13 | 11 | 8 | 8 | 5 | 48 | 5 | 0 | 9 | 4 | `routes_to_fixed_nonzero_columncrt_residue` |
| 13 | 11 | 9 | 2 | 4 | 48 | 37 | 3 | 2 | 1 | `routes_to_fixed_nonzero_columncrt_residue` |
| 13 | 11 | 10 | 7 | 3 | 48 | 3 | 0 | 8 | 5 | `routes_to_fixed_nonzero_columncrt_residue` |

## 审稿意义

本证书把 `404` 个 unit endpoint seam 相位进一步压缩：一旦同一 unit seam 相位持久出现，端点标签固定为 `p`，下层列固定为 `c=r+g-delta`，同列见证位移固定为一个非零 `mod p` 余类。因此它不是任意 PDEC 坏窗，而是标准 `ColumnCRTDefect(p,d)` 候选。

这一步仍不是全局命题闭合。剩余硬义务是证明正式反例族确实映入这些门控行，并排除对应 `ColumnCRTDefect` 阈值 `L_D`，或证明正式反例族避开 unit endpoint seam。
