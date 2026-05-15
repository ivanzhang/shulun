# Prime Matrix square-phase no-slot moving prime cluster router

**状态：** `noslot_layer_prime_load_reduced_to_moving_short_prime_cluster_open`

本步把 moving layer prime-load 精确接成普通短区间素数簇对象。固定 `P,side,k` 的层原子由显式二次不等式给出；对应 `q=P-2b` 区间为 `[P-2b_hi, P-2b_lo]`，其负载等于 `pi(q_hi)-pi(q_lo-1)`。若无槽分支大到威胁 `PrimeWindow`，则必须出现某个 moving q-interval 的高素数簇。确定性长度上界只能给出 `prime_load<=length`，不足以闭合全局；剩余是证明这些 moving 短区间素数簇上界，或把持久高簇登记并排斥为 PDEC/SAE。

```text
max_p=5000
finite_prime_count=668
formula_match_failure_count=0
prefix_load_failure_count=0
length_failure_count=0
finite_large_branch_count=0
row_column_unconditional_closed=false
```

## 1. 短区间素数簇对象

固定 `P,side,k` 后，原子由下列二次不等式给出：

```text
s_k(b)=2b^2+2kb-kP.
plus atom:  0 <= s_k(b) < (P+1)/2-2b
minus atom: (P-1)/2 < s_k(b) < P-2b
```

若原子为 `b_lo<=b<=b_hi`，则对应普通 q 区间

```text
q_lo=P-2b_hi,  q_hi=P-2b_lo,
prime_load = pi(q_hi)-pi(q_lo-1).
```

这把 moving layer 负载从二次相位问题转成短区间素数簇问题。

## 2. 有限审计摘要

| metric | value |
| --- | ---: |
| plus PrimeWindow | 97145 |
| minus PrimeWindow | 97396 |
| plus no-slot load | 18299 |
| minus no-slot load | 15895 |
| plus atom count | 35777 |
| minus atom count | 35476 |
| max plus atom load | 11 |
| max minus atom load | 7 |

## 3. 最大素数簇原子

| side | P | k | b interval | q interval | length | q span | load | density | sample q |
| --- | ---: | ---: | --- | --- | ---: | ---: | ---: | ---: | --- |
| plus | 4273 | 0 | [1,32] | [4209,4271] | 32 | 63 | 11 | 0.343750 | `[4271, 4261, 4259, 4253, 4243, 4241, 4231, 4229]` |
| minus | 4733 | 0 | [35,48] | [4637,4663] | 14 | 27 | 7 | 0.500000 | `[4663, 4657, 4651, 4649, 4643, 4639, 4637]` |

## 4. 样本表

| P | plus atoms | plus load | plus max cluster | minus atoms | minus load | minus max cluster |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 13 | 1 | 1 | 1 | 0 | 0 | 0 |
| 17 | 1 | 0 | 0 | 0 | 0 | 0 |
| 19 | 1 | 1 | 1 | 0 | 0 | 0 |
| 23 | 1 | 0 | 0 | 0 | 0 | 0 |
| 29 | 1 | 0 | 0 | 0 | 0 | 0 |
| 31 | 1 | 1 | 1 | 1 | 0 | 0 |
| 101 | 2 | 1 | 1 | 2 | 2 | 1 |
| 499 | 9 | 9 | 3 | 12 | 6 | 2 |
| 1009 | 25 | 17 | 3 | 20 | 9 | 3 |
| 2003 | 42 | 28 | 6 | 46 | 18 | 2 |
| 4999 | 117 | 58 | 11 | 117 | 46 | 3 |

## 5. 命题行

| name | status | statement |
| --- | --- | --- |
| `quadratic_inequality_endpoint_formula` | `closed` | Layer atoms are exactly the integer solutions of explicit quadratic inequalities in b. |
| `moving_q_interval_prime_load_identity` | `closed` | Each atom load equals pi(q_hi)-pi(q_lo-1) for q=P-2b on its moving interval. |
| `trivial_length_envelope` | `closed` | Every atom has prime_load<=length, giving a deterministic but insufficient envelope. |
| `large_branch_forces_short_prime_cluster` | `closed` | A threatening no-slot branch forces a moving q-interval with prime cluster load above the pigeonhole threshold. |
| `short_prime_cluster_bound_or_pdec` | `open` | A global proof needs an upper bound for these moving short prime clusters, or a PDEC/SAE exclusion of persistent clusters. |

## 6. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `QuadraticFormulaMatchesDirectAtoms` | `true` | `true` | 二次不等式端点公式与 residue 定义生成的原子完全一致。 | closed |
| `PiDeltaLoadIdentityClosed` | `true` | `true` | 每个原子的 prime-load 等于普通素数计数函数在 q 区间的差。 | closed |
| `TrivialLengthEnvelopeClosed` | `true` | `true` | 确定性长度上界成立，但不足以排除全局反例。 | closed but insufficient |
| `FiniteNoLargeNoSlotBranch` | `true` | `false` | 有限扫描 P<=5000 没有威胁性无槽分支。 | finite evidence only |
| `GlobalMovingShortPrimeClusterBound` | `false` | `false` | 仍需全局证明 moving q-interval 内素数簇不可能承担反例所需负载。 | MovingLayerShortPrimeClusterBoundOrPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把 prime-load 接成短区间素数簇对象，不关闭全局行/列命题。 | MovingLayerShortPrimeClusterBoundOrPDEC |

## 7. 下一步

- 主攻：`MovingLayerShortPrimeClusterBoundOrPDEC`。
- 当前可合法使用的确定性上界只有 `prime_load<=length`；要闭合必须证明更强的 moving 短区间素数簇上界，或把持续高簇作为 PDEC/SAE 排斥。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/square-phase-noslot-moving-prime-cluster-ledger.json` | `f02bbd1e35629b21b0f2e16a91e3269466bd7e14b0c4fbb0bedab5d1e20437e8` |
| `experiments/prime_matrix_square_phase_noslot_moving_prime_cluster_router.py` | `7a9b7d4fe4b9bbe79c5c04ea688162247efe8900477de06d35ce44e911b24381` |
