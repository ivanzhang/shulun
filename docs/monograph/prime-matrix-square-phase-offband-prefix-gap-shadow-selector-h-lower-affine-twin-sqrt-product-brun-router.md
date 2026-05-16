# Prime Matrix square-phase off-band prefix gap shadow selector H lower affine twin sqrt-product Brun router

**状态：** `affine_twin_sqrt_product_gate_passes_current_sweep_brun_conditional_global_open`

本步把 per-q multiplicity 的目标从过强的 O(1) 压窄为平方根乘积门：设 `M_q` 为同一 AffineTwin `q` 的候选双残基乘积上界。若 `M_q^2<=q(q-2)`，则该 q 的 SAE 贡献至多 `1/sqrt(q(q-2))<=1/(q-2)`；在接受经典 Brun 孪生素数倒数收敛作为外部输入时，这条 twin-q 尾和可求和。当前候选 `q=[31, 43, 103]` 全部通过该门，最大 `M_q/sqrt(q(q-2))=0.400222407579`。但作者侧自足闭合仍需全局证明平方根乘积门，或排斥 `SuperSqrtEpochPair-PDEC/ColumnCRT`。

```text
candidate_q_values=[31, 43, 103]
realized_q_values=[31]
all_current_rows_pass_sqrt_product_gate=true
max_product_over_sqrt_capacity=0.400222407579
min_sqrt_product_gate_slack_squared=755
current_product_sae_mass_upper_sum=0.023577117629
current_sqrt_gate_envelope_sum=0.066972535473
external_brun_input=ClassicalBrunTwinPrimeReciprocalConvergence
external_brun_input_accepted_in_author_side=false
row_column_unconditional_closed=false
```

## 1. 平方根乘积门

| q | used product M_q | q(q-2) | M_q/sqrt(q(q-2)) | squared slack | pass | realized |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 31 | 12 | 899 | 0.400222408 | 755 | `true` | `true` |
| 43 | 16 | 1763 | 0.381060407 | 1507 | `true` | `false` |
| 103 | 12 | 10403 | 0.117652713 | 10259 | `true` | `false` |

## 2. Brun 条件包络

```text
If M_q^2 <= q(q-2), then
M_q/(q(q-2)) <= 1/sqrt(q(q-2)) <= 1/(q-2).
For affine-twin q, q and q-2 are twin primes.
Classical Brun convergence makes sum_{twin q} 1/(q-2) finite.
```

这关闭的是“接受外部 Brun 输入后的 SAE 可求和出口”。作者侧自足线仍不能把 Brun 输入或当前有限扫描当作最终证明。

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `sqrt_product_gate_implies_brun_sae_summability` | `closed_conditional_on_external_brun` | For affine-twin q, if M_q<=sqrt(q(q-2)), then M_q/(q(q-2))<=1/sqrt(q(q-2))<=1/(q-2); Brun convergence for twin-prime reciprocals makes the SAE tail summable. |
| `current_affine_twin_rows_pass_sqrt_product_gate` | `closed_current_sweep` | Every current candidate q has epoch-pair product upper M_q with M_q^2<=q(q-2). |
| `super_sqrt_epoch_pair_pdec_routing` | `closed_routing` | Any q with M_q>sqrt(q(q-2)) is no longer a sparse SAE row; it is a named SuperSqrtEpochPair-PDEC/ColumnCRT side-residue concentration object. |
| `internal_sqrt_product_bound` | `open` | The self-contained route still must prove the sqrt-product gate globally, or exclude the super-sqrt PDEC family without appealing to finite scans. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `CurrentSqrtProductGateClosed` | `true` | `false` | 当前候选 q 全部满足 M_q^2<=q(q-2)，且最大 M_q/sqrt(q(q-2)) 低于 1。 | finite evidence only |
| `BrunConditionalSAESummability` | `true` | `false` | 若接受外部 Brun twin-prime reciprocal convergence，并全局证明平方根乘积门，则 AffineTwin SAE 尾和可求和。 | external input + global sqrt gate |
| `SuperSqrtEpochPairPDECRouted` | `true` | `true` | 平方根乘积门失败时，失败 q 被明确登记为 side-residue product 超平方根集中，而不是普通 sparse 行。 | exclusion still separate |
| `InternalGlobalSqrtProductBoundProved` | `false` | `false` | 作者侧自足路线仍需证明 M_q<=sqrt(q(q-2))，或排斥持久 SuperSqrtEpochPair-PDEC。 | AffineTwinSqrtProductBoundOrSuperSqrtEpochPairPDECExclusion |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只压窄 per-q multiplicity 门，不关闭全局行/列命题。 | AffineTwinSqrtProductBoundOrSuperSqrtEpochPairPDECExclusion |

## 5. 下一步

- 主攻：`AffineTwinSqrtProductBoundOrSuperSqrtEpochPairPDECExclusion`。
- 自足线：证明所有持久 AffineTwin epoch-pair 都满足 `M_q^2<=q(q-2)`。
- 失败线：若 `M_q^2>q(q-2)`，把该 q 的 side-residue product 超平方根集中登记为 `SuperSqrtEpochPair-PDEC/ColumnCRT` 并排斥。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_sqrt_product_brun_router.py` | `4b21ac7a44ef0e62ac863d43dcb62cc9b6e02b650935adf2f2cfc446d71d9fd1` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-moving-family-sae-columncrt-ledger.json` | `2e401269ab68cb196babfb74e6f7b63c946ee9de37bc6ab5d502f49deaa7bf28` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sparse-sae-global-envelope-ledger.json` | `18a67505beef2a1ba7ec53a6088bb26da6a3955e2f63c02f5e215cfe171a8063` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-persistence-frontier-partition-ledger.json` | `1f61cb91bbabc3fdccfee381045187a294f0483a73834491189b8d636e585745` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sqrt-product-brun-ledger.json` | `44e048bbb9be8b3e2fa427090bf3bfa613575035385807986c0b7a3c664ff50a` |
