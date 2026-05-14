# Prime Matrix x=P 特化轮序 gcd 方程组路由器

**状态：** `x_equals_p_wheel_equivalence_closed_global_no_cover_open`

`x=P` 特化后，用户给出的轮序 gcd 系统有一个无冗余 canonical 子系统：`gcd((P-q)P+r,q)=q`。它与 `q|P^2+r` 完全等价；若使用复合模 `P-k`，安全条件应写成 `gcd(kP+r,P-k)>1`，而精确等号 `=q` 要落在 canonical 模数 `P-k=q` 上。若某个 `r` 未被所有 `q<P` 覆盖，则 `P^2+r` 必为素数。因此“`x=P` 时方程组无全覆盖解”不是额外弱命题，而正是平方后前半窗素数命题。本步把等价链和有限样本固定下来；全局突破仍需 square-phase 粗幸存下界或 PDEC/SAE 矛盾。

```text
max_p=5000
finite_prime_count=668
finite_failure_count=0
canonical_equivalence_checked=true
full_wheel_checked_count=11
x_equals_p_no_solution_global_proved=false
row_column_unconditional_closed=false
```

## 1. 等价链

| name | status | statement |
| --- | --- | --- |
| `canonical_wheel_equivalence` | `closed` | 对 q<P，q \| P^2+r 当且仅当 gcd((P-q)P+r,q)=q。 |
| `full_wheel_redundancy` | `closed` | 用户轮序 gcd(kP+r,P-k)>1 与小素因子覆盖等价；canonical k=P-q 是最小无冗余子系统。 |
| `exact_gcd_q_scope` | `closed` | 若在复合模 P-k 上写 gcd(...)=q 会漏掉 gcd 为复合数的覆盖；精确等号 q 应锚定在 canonical 模数 P-k=q。 |
| `uncovered_is_prime` | `closed` | 若 1<=r<P 未被任何 q<P 覆盖，则 P^2+r 不能合成；否则其最小素因子必须小于 P。 |
| `x_equals_P_no_solution_equivalence` | `target_equivalent_open` | 证明 x=P 时轮序系统不能覆盖所有 r，正等价于证明 (P^2,P^2+P) 内有素数。 |

## 2. 样本记录

| P | survivors | least r | P^2+r | prime | canonical mismatch | full wheel mismatch |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 13 | 3 | 4 | 173 | `true` | 0 | 0 |
| 17 | 1 | 4 | 293 | `true` | 0 | 0 |
| 19 | 3 | 6 | 367 | `true` | 0 | 0 |
| 23 | 2 | 12 | 541 | `true` | 0 | 0 |
| 29 | 4 | 12 | 853 | `true` | 0 | 0 |
| 31 | 5 | 6 | 967 | `true` | 0 | 0 |
| 101 | 11 | 10 | 10211 | `true` | 0 | 0 |
| 499 | 40 | 16 | 249017 | `true` | 0 | 0 |
| 1009 | 72 | 10 | 1018091 | `true` | 0 | 0 |
| 2003 | 125 | 4 | 4012013 | `true` | 0 | 0 |
| 4999 | 300 | 36 | 24990037 | `true` | 0 | 0 |

## 3. 最小幸存样本

- `P=3`，未覆盖列数 `1`，最小未覆盖 `r=2`，对应素数 `11`。

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `XEqualsPCanonicalWheelEquivalenceChecked` | `true` | `true` | canonical 方程 gcd((P-q)P+r,q)=q 与 q\|P^2+r 完全一致。 | closed |
| `FiniteXEqualsPWheelNoFullCoverChecked` | `true` | `false` | 有限扫描 P<=5000 未出现 x=P 全覆盖。 | finite evidence only |
| `XEqualsPNoSolutionGlobalProved` | `false` | `false` | x=P 无解就是平方后前半窗素数命题本身；当前未给出全局证明。 | PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP |
| `SquarePhaseAttackPointIsolated` | `true` | `false` | 真正新信息不是任意 x，而是 P^2 在所有小模上的负平方相位刚性。 | SquarePhaseRoughSurvivorUniformLowerBound |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步完成等价链和有限证据，不闭合最终命题。 | SquarePhaseRoughSurvivorUniformLowerBound OR NonFinalTailPDECSAEBudgetAmplificationOrAlternativeContradiction |

## 5. 下一步

- 主攻 `SquarePhaseRoughSurvivorUniformLowerBound`：利用 `r=-P^2 mod q` 的负平方相位，证明长度 `P` 内存在未覆盖列。
- 若 square-phase 全覆盖被假设成立，则必须把覆盖相位异常登记到 `NonFinalTailPDECSAEBudgetAmplificationOrAlternativeContradiction`，寻找 PDEC/SAE/预算矛盾。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-square-x-equals-p-wheel-sample-ledger.json` | `a6ef3925ea7cd227f94cdec0c7baf427a50e913ab6f67170472344e1f7e77885` |
| `experiments/prime_matrix_prime_square_x_equals_p_wheel_router.py` | `d22f1f3455f229d969948610b0b998877cb334cc727f66d32db38e17c8d35956` |
