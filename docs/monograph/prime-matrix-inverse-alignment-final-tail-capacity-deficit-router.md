# Prime Matrix inverse alignment final-tail 容量缺口路由器

**状态：** `final_tail_decomposition_closed_uniform_rough_survivor_bound_open`

final-tail 下钻给出一个严格结构分解：设 ell 为 P 以下最大素数、z 为其前一素数。在 `1<=x<=P` 中，过了 `q<=z` 的残洞若不是 ell 相位倍数，就只能是真正的素数；不可能是其它合数，因为其它允许素因子只能是 `>P`，两因子乘积已超过 `P^2+P`，而 P 本身不整除 `xP+r`。因此 final-tail 缺口不再是抽象容量账本，而是精确的“ell 倍数或素数幸存”二分。有限探针到 `P<=251` 全部有素数幸存，且 `P>=29` 全部满足更强的 `|R_z(x)|>mu_ell(x)`。但全局仍需证明 primorial cutoff 的粗幸存下界，或把等号态登记为相位缺陷；行/列命题尚未无条件闭合。

```text
final_tail_residual_decomposition_closed=true
finite_probe_prime_survivor_for_all_rows=true
finite_probe_strict_capacity_deficit_for_all_P_ge_29=true
uniform_final_tail_capacity_deficit_or_phase_defect_lower_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 结构分解

令 `ell` 为小于 `P` 的最大素数，`z` 为 `ell` 前一个素数。对 `1<=x<=P`，定义

```text
R_z(x)={1<=r<P: xP+r 不被任何 q<=z 整除}.
A_ell(x)={1<=r<P: ell | xP+r}.
```

若 `r in R_z(x) \ A_ell(x)` 且 `xP+r` 合数，则其最小素因子不能小于 `ell`，不能等于 `ell`，也不能等于 `P`。因此最小素因子必须大于 `P`，两个因子乘积超过 `P^2+P`，与 `xP+r<=P^2+P-1` 矛盾。所以这类列必为素数。

## 2. 有限探针

扫描范围：素数 `13<=P<=251`，每个 `1<=x<=P`。

| P | z | ell | min R_minus_mu_ell | min R_minus_effective | strict capacity all x | prime survivor all x | nonpositive witnesses |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| `13` | `7` | `11` | `1` | `1` | `true` | `true` | `[]` |
| `17` | `11` | `13` | `0` | `1` | `false` | `true` | `[{'x': 12, 'residual_size': 1, 'tail_capacity_mu': 1, 'tail_effective_hits_inside_residual': 0, 'prime_survivor_columns': [7]}]` |
| `19` | `13` | `17` | `1` | `1` | `true` | `true` | `[]` |
| `23` | `17` | `19` | `0` | `2` | `false` | `true` | `[{'x': 14, 'residual_size': 2, 'tail_capacity_mu': 2, 'tail_effective_hits_inside_residual': 0, 'prime_survivor_columns': [9, 15]}]` |
| `29` | `19` | `23` | `1` | `3` | `true` | `true` | `[]` |
| `31` | `23` | `29` | `1` | `2` | `true` | `true` | `[]` |
| `37` | `29` | `31` | `1` | `2` | `true` | `true` | `[]` |
| `41` | `31` | `37` | `2` | `3` | `true` | `true` | `[]` |
| `43` | `37` | `41` | `2` | `3` | `true` | `true` | `[]` |
| `47` | `41` | `43` | `2` | `3` | `true` | `true` | `[]` |
| `53` | `43` | `47` | `3` | `4` | `true` | `true` | `[]` |
| `59` | `47` | `53` | `2` | `3` | `true` | `true` | `[]` |
| `61` | `53` | `59` | `4` | `5` | `true` | `true` | `[]` |
| `67` | `59` | `61` | `3` | `5` | `true` | `true` | `[]` |
| `71` | `61` | `67` | `5` | `5` | `true` | `true` | `[]` |
| `73` | `67` | `71` | `4` | `5` | `true` | `true` | `[]` |
| `79` | `71` | `73` | `4` | `5` | `true` | `true` | `[]` |
| `83` | `73` | `79` | `5` | `6` | `true` | `true` | `[]` |
| `89` | `79` | `83` | `6` | `7` | `true` | `true` | `[]` |
| `97` | `83` | `89` | `5` | `6` | `true` | `true` | `[]` |
| `101` | `89` | `97` | `6` | `7` | `true` | `true` | `[]` |
| `103` | `97` | `101` | `7` | `8` | `true` | `true` | `[]` |
| `107` | `101` | `103` | `5` | `6` | `true` | `true` | `[]` |
| `109` | `103` | `107` | `7` | `8` | `true` | `true` | `[]` |
| `113` | `107` | `109` | `6` | `7` | `true` | `true` | `[]` |
| `127` | `109` | `113` | `9` | `10` | `true` | `true` | `[]` |
| `131` | `113` | `127` | `9` | `10` | `true` | `true` | `[]` |
| `137` | `127` | `131` | `8` | `9` | `true` | `true` | `[]` |
| `139` | `131` | `137` | `8` | `9` | `true` | `true` | `[]` |
| `149` | `137` | `139` | `10` | `11` | `true` | `true` | `[]` |
| `151` | `139` | `149` | `11` | `12` | `true` | `true` | `[]` |
| `157` | `149` | `151` | `10` | `11` | `true` | `true` | `[]` |
| `163` | `151` | `157` | `10` | `11` | `true` | `true` | `[]` |
| `167` | `157` | `163` | `10` | `11` | `true` | `true` | `[]` |
| `173` | `163` | `167` | `10` | `11` | `true` | `true` | `[]` |
| `179` | `167` | `173` | `12` | `13` | `true` | `true` | `[]` |
| `181` | `173` | `179` | `10` | `11` | `true` | `true` | `[]` |
| `191` | `179` | `181` | `13` | `14` | `true` | `true` | `[]` |
| `193` | `181` | `191` | `13` | `14` | `true` | `true` | `[]` |
| `197` | `191` | `193` | `14` | `15` | `true` | `true` | `[]` |
| `199` | `193` | `197` | `11` | `12` | `true` | `true` | `[]` |
| `211` | `197` | `199` | `14` | `15` | `true` | `true` | `[]` |
| `223` | `199` | `211` | `13` | `14` | `true` | `true` | `[]` |
| `227` | `211` | `223` | `14` | `15` | `true` | `true` | `[]` |
| `229` | `223` | `227` | `14` | `15` | `true` | `true` | `[]` |
| `233` | `227` | `229` | `14` | `15` | `true` | `true` | `[]` |
| `239` | `229` | `233` | `15` | `16` | `true` | `true` | `[]` |
| `241` | `233` | `239` | `15` | `16` | `true` | `true` | `[]` |
| `251` | `239` | `241` | `17` | `18` | `true` | `true` | `[]` |

## 3. 请求 P 的最弱行

| P | z | ell | weakest x | R_size | mu_ell | effective hits | prime survivor columns |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `13` | `7` | `11` | `5` | `3` | `2` | `0` | `[2, 6, 8]` |
| `17` | `11` | `13` | `12` | `1` | `1` | `0` | `[7]` |
| `19` | `13` | `17` | `6` | `2` | `1` | `0` | `[13, 17]` |
| `23` | `17` | `19` | `14` | `2` | `2` | `0` | `[9, 15]` |
| `29` | `19` | `23` | `11` | `3` | `2` | `0` | `[12, 18, 28]` |
| `31` | `23` | `29` | `25` | `2` | `1` | `0` | `[12, 22]` |

## 4. 判定边界

| name | status | statement |
| --- | --- | --- |
| `final_tail_decomposition` | `closed` | After sieving by all primes below ell, where ell is the largest prime <P, every residual column is either an ell-multiple or a genuine prime >P in the early range 1<=x<=P. |
| `tail_capacity_at_most_two` | `closed` | Because ell>P/2, the largest tail prime phase hits at most two columns in 1<=r<P. |
| `capacity_or_phase_defect_implication` | `closed` | If \|R\|>mu_ell then a prime survivor exists; if \|R\|<=mu_ell but R is not contained in the ell phase, the missing alignment is a registered phase defect and also leaves a prime survivor. |
| `finite_probe` | `diagnostic_closed` | For tested primes 13<=P<=251 every early row has a final-tail prime survivor; for all tested P>=29 the stronger strict capacity deficit \|R\|>mu_ell holds. |
| `uniform_lower_bound` | `open` | The remaining global task is to prove a non-tautological rough survivor lower bound for the primorial cutoff, or route equality cases to a registered phase defect. |

## 5. 下一步

- 主攻：`UniformFinalTailRoughSurvivorLowerBoundOrRegisteredPhaseDefect`。
- 具体化为：证明 `P>=29` 时 `|R_z(x)|>mu_ell(x)` 对所有 `1<=x<=P` 成立；或证明所有等号态必须进入 `RegisteredFinalTailPhaseDefectPDECSAERoute`。
- 这等价需要一个 `PrimorialCutoffJacobsthalRoughSurvivorLowerBoundForPBlocks` 型粗幸存下界，不能把有限探针当作全局证明。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/inverse-alignment-final-tail-capacity-probe-ledger.json` | `9f38c983499bff7fa3bc553c67afcf50ad2b28645116471235d3d10be68a1874` |
| `data/inverse-alignment-min-x-phase-scan-ledger.json` | `ece15abdb5fd5bf50a50e66217cd6472bd1f627b57feea2b19e92ab162fe6f98` |
| `docs/monograph/prime-matrix-inverse-alignment-min-x-phase-scan-router.json` | `81175f0cc0257e65e6183e6f9ea05f717c205f0a6dce6fc89afb3672df24d387` |
| `docs/monograph/prime-matrix-zero-row-minrep-route-review.md` | `cff5609900bcfaa796b6b586c44458727b9807f2f1afd2210e52360dbe5bef26` |
| `experiments/prime_matrix_inverse_alignment_final_tail_capacity_deficit_router.py` | `b39561518818ca76be14aa238b5f04d4d00a95edbf3486bc9ef072383efccce8` |
