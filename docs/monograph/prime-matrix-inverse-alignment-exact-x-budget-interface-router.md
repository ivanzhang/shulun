# Prime Matrix inverse alignment 精确 x 预算接口路由器

**状态：** `exact_x_budget_interface_closed_strict_margin_open`

逆元最小对齐解路线已接入同参数预算判定：给定 P，零行行号 `X(P)` 是一个有限 CRT 覆盖最小解；一旦 x 被确定，同一 x 直接生成 `rho_q(x)`、`mu_q`、`R_{x,z}`、`tau_z(c)` 和 `M#_{x,z}`。因此在需要精细判定时，可以用 exact-x runner 逐项比较注册的非持久冷供给 `U_np`。但该接口不自动证明全局 `X(P)>P`，也不自动证明 `M#_{x,z}>U_np`；前者会落入短区间素数路线，后者仍需冷供给数值 envelope 或解析支配。

```text
same_parameter_margin_target_imported=true
exact_zero_row_x_budget_fields_closed=true
exact_x_sample_min_gt_p_verified=true
exact_x_runner_interface_closed=true
same_parameter_sparse_demand_cold_supply_strict_margin_proved=false
row_column_unconditional_closed=false
```

## 1. 接口定理

| name | statement | status |
| --- | --- | --- |
| `exact_x_crt_decision_function` | X(P)=min{x>0: for every 1<=c<P, some q<P has c=-xP mod q}. | `closed_as_finite_crt_algorithm` |
| `same_x_budget_fields` | rho_q(x), mu_q, R_{x,z}, tau_z(c), M#_{x,z} are all generated from the same exact x. | `closed` |
| `early_window_no_go` | proving X(P)>P directly for every P is the prime-in-each-P-block short-interval route. | `identified_not_used_as_global_closure` |
| `exact_x_budget_runner` | finite or analytic certificates may compare exact M#_{x,z} against the registered U_np envelope. | `new_interface_open` |
| `strict_margin` | M#_{x,z} > U_np for every hypothetical early zero row under the same parameter ledger. | `open` |

## 2. exact x 预算样本

| P | X(P) | X/P | z | R_xz | M# | suffix cap | overlap debt | max mult |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `168` | `12.923076923` | `3` | `4` | `2.666666666667` | `5` | `3` | `3` |
| `17` | `1210` | `71.176470588` | `3` | `5` | `3.166666666667` | `7` | `5` | `4` |
| `19` | `3658` | `192.526315789` | `3` | `6` | `2.666666666667` | `11` | `8` | `4` |
| `23` | `58` | `2.52173913` | `3` | `7` | `3.566666666667` | `14` | `11` | `3` |
| `29` | `5209` | `179.620689655` | `4` | `9` | `3.233333333333` | `20` | `16` | `4` |
| `31` | `60794` | `1961.096774194` | `4` | `10` | `4.0` | `21` | `16` | `4` |
| `37` | `73916` | `1997.72972973` | `4` | `12` | `4.595238095238` | `26` | `20` | `4` |
| `41` | `170880` | `4167.804878049` | `4` | `13` | `5.041666666667` | `30` | `23` | `5` |
| `43` | `162932` | `3789.11627907` | `5` | `11` | `4.916666666667` | `24` | `25` | `5` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `SameParameterMarginTargetImported` | `true` | `true` | 回流后统一预算已经把非持久主攻点压到同参数稀疏余量。 | SameParameterSparseDemandColdSupplyStrictMarginCertificate |
| `ExactZeroRowXBudgetFieldsClosed` | `true` | `true` | 精确最小零行 x 可生成同一参数下的全部需求字段。 | ExactZeroRowXDrivenSameParameterBudgetRunnerOrAnalyticEnvelope |
| `ExactXSampleMinGreaterThanP` | `true` | `false` | 样本精确 X(P) 均大于 P，但这不是全局证明。 | PrimeGapBelowP2ForAllPBlocks |
| `ExactXRunnerInterfaceClosed` | `true` | `true` | 后续有限 runner 或解析包可直接读取 exact x/M#/tau 字段比较 U_np。 | ExactZeroRowXDrivenSameParameterBudgetRunnerOrAnalyticEnvelope AND ColdSupplySameParameterNumericEnvelope |
| `SameParameterStrictMarginProved` | `false` | `false` | 还没有证明 exact M# 统一反超注册冷供给 U_np。 | ExactZeroRowXDrivenSameParameterBudgetRunnerOrAnalyticEnvelope AND ColdSupplySameParameterNumericEnvelope |
| `DirectUnconditionalContradictionFound` | `false` | `false` | 本步没有推出早期零行反例不存在；只是把精确 x 接入终端预算。 | ExactZeroRowXDrivenSameParameterBudgetRunnerOrAnalyticEnvelope AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 非持久 exact-x 预算、持久 moving atom 与 DStructure/Rankin 仍未全部闭合。 | ExactZeroRowXDrivenSameParameterBudgetRunnerOrAnalyticEnvelope AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一步

- 主攻：`ExactZeroRowXDrivenSameParameterBudgetRunnerOrAnalyticEnvelope`。
- 任务：把 exact `M#_{x,z}` 与同参数 `U_np` 冷供给 envelope 做可复核有限 runner 或解析支配。
- 边界：不能把样本 `X(P)>P` 当作全局证明。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/inverse-alignment-exact-x-budget-interface-ledger.json` | `1cdc1a5cabb6ff9043184f7e567b14622b5667f708564ef9daae04c44beb6a52` |
| `data/inverse-alignment-exact-zero-row-charge-profile-ledger.json` | `c7cabc90437430aee6614b0428662fe0ce67a1eac9a3ee263b5560ef06481db3` |
| `docs/monograph/prime-matrix-inverse-alignment-cold-core-chain-reconciliation-router.json` | `61ef7bdeadde280e4c1e4944c477654cf55da19bad4bfbe57dff6ae80a5a4bc4` |
| `docs/monograph/prime-matrix-inverse-alignment-covering-system-router.json` | `09be6a101dd2775a057577a1ef960270dbd88b03dd5e5cec4d1bddec67eb1acf` |
| `docs/monograph/prime-matrix-inverse-alignment-exact-zero-row-charge-profile-router.json` | `f6f2c2c1d5bbd95e83d085f48ac5c6bb6a6250c72fc450112b6815b8313429ba` |
| `docs/monograph/prime-matrix-inverse-alignment-prefix-demand-bridge-router.json` | `369bf801b153a8cb792ef4a0971d5156020eb6604c2cdd31808d81cd4770c70a` |
| `docs/monograph/prime-matrix-strict-cold-supply-numeric-after-return-cycle-router.json` | `5be154f20bb3ff27a7c356dc2fc1d9b2a963be039e3c4f94ec2d941a7e47f721` |
| `docs/monograph/prime-matrix-strict-same-parameter-sparse-margin-after-return-cycle-router.json` | `c7265153d74715fc941d430ceb1307996ffff0955769b5d84660464dc7f90faa` |
| `docs/monograph/prime-matrix-strict-unified-budget-after-return-cycle-sync-router.json` | `0b1f76cce75b61929c79f82036782b10d6c1755b84840de0e666224ad5ae7922` |
| `experiments/prime_matrix_inverse_alignment_exact_x_budget_interface_router.py` | `2937e5c71182b01d4a41eb185a31a891a15632416d5d514c90c009430d570817` |
