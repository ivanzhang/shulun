# Triad-A1 全 PhaseResidue 终端审计

**状态：** `all_materialized_phase_residue_atoms_expanded_to_full_crt`

当前已物化 Q=30030 与 Q=510510 的全部非零相位都可局部展开为完整 CRT 终端相位，且所有终端相位均大于 P；因此当前有限升层的全 phase-residue 原子都不能产生 P 行以内零行。

## 1. 结构律

对每个非零 M_Q(u)，枚举剩余高素 CRT fiber u+yQ。完整终端行数量必须等于 M_Q(u)。若所有终端行都大于 P，则这一整层已物化 phase-residue 原子都不能在前 P 行内产生零行。

```text
M_Q(u)>0；
R={ell<P: ell does not divide Q}；
terminal row w=u+yQ, y mod prod(R)；
M_Q(u)=#{y: w 完整覆盖}。
```

这一步审计全部非零相位，不只 `NoDeletion-KL` 见证器抽出的 top 原子。

## 2. 汇总

- `prime_row_count=6`。
- `route_counts={'AllTerminalBeyondP': 6}`。
- `total_nonzero_phase_count=5030`。
- `total_terminal_count=14348`。
- `all_total_mass_identities_hold=True`。
- `all_phase_mass_identities_hold=True`。
- `all_terminal_gt_p=True`。
- `all_terminal_gt_p2=False`。
- `total_terminal_le_p_count=0`。
- `total_terminal_le_p2_count=2`。
- `global_min_terminal_phase=59`。

## 3. P 级明细

| Q | P | nonzero phases | terminal count | high primes | min terminal | <=P | <=P^2 | mass ok | >P | >P^2 | earliest terminals |
| ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | --- | --- | --- | --- |
| 30030 | 17 | 28 | 28 | `[]` | 1211 | 0 | 0 | `True` | `True` | `True` | `[1211, 1638, 2323, 4744, 5171, 6530, 8277, 9618]` |
| 30030 | 19 | 368 | 496 | `[17]` | 3659 | 0 | 0 | `True` | `True` | `True` | `[3659, 4101, 4731, 6705, 6820, 7671, 9004, 9981]` |
| 30030 | 23 | 936 | 3456 | `[17, 19]` | 59 | 0 | 1 | `True` | `True` | `False` | `[59, 2612, 5539, 5840, 6569, 10747, 13709, 14759]` |
| 30030 | 29 | 610 | 6416 | `[17, 19, 23]` | 5210 | 0 | 0 | `True` | `True` | `True` | `[5210, 74840, 100844, 161928, 165030, 213078, 216674, 239444]` |
| 510510 | 19 | 496 | 496 | `[]` | 3659 | 0 | 0 | `True` | `True` | `True` | `[3659, 4101, 4731, 6705, 6820, 7671, 9004, 9981]` |
| 510510 | 23 | 2592 | 3456 | `[19]` | 59 | 0 | 1 | `True` | `True` | `False` | `[59, 2612, 5539, 5840, 6569, 10747, 13709, 14759]` |

## 4. 读法

`all_terminal_gt_p=True` 是行命题相关读数：当前已物化升层的全部非零相位都不会在第 `P` 行以内形成零行。
`all_terminal_gt_p2=False` 是预期现象，例如 `P=23` 的完整 CRT 周期中存在第 59 行零行；它不违反行命题，因为 59>P。
因此本报告关闭的是当前有限升层全原子的 `P×P` 早期出口，不是所有无限终端证书全集。
