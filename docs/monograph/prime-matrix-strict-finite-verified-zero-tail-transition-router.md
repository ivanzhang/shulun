# Prime Matrix strict 有限 verified-zero 到零点自由尾项桥接路由器

**状态：** `finite_verified_zero_tail_transition_interface_taxonomy_closed_bridge_budgets_open`

有限 verified-zero 到零点自由尾项的真正硬点不是再登记一个外部常数，而是共同变量接口。Gourdon 和 Kadiri 两块即使都可外部引用，也必须经由同一显式公式、同一高度端点、同一尾项阈值、同一预算分摊和同一可复现 hash，才能推出 Dusart/Schoenfeld 的 epsilon 表值。本步关闭接口分类，但不关闭自足桥接；最新最窄点压到 psi epsilon 预算分摊账本。

```text
external_pieces_identified_but_not_composed=true
common_variable_interface_taxonomy_closed=true
finite_verified_zero_to_tail_transition_closed=false
finite_rh_height_endpoint_closed=false
zero_free_tail_start_height_closed=false
finite_to_tail_no_gap_no_overlap_closed=false
same_explicit_formula_convention_closed=false
psi_epsilon_budget_partition_closed=false
table_generator_hash_interface_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 共同变量表

| variable | required_by | must_cover | current_status |
| --- | --- | --- | --- |
| `x_range` | `epsilon table / Dusart P5.1` | x>=e^28 high tail and 8e11<=x<=e^28 middle band | statement extracted, computation proof open |
| `finite_zero_height_H` | `FiniteRHHeightEndpointLedger` | verified nontrivial zeros up to the exact height used by the table generator | external Gourdon source identified, endpoint-to-table mapping open |
| `zero_free_region_R_and_t0` | `ZeroFreeTailStartHeightLedger` | tail zero-free estimates from the first height where the table tail uses them | external Kadiri source identified, table constants and thresholds open |
| `explicit_formula_kernel` | `SameExplicitFormulaConventionLedger` | same psi/theta formula, truncation, smoothing and prime-power convention | not yet matched to the table generator hash |
| `remainder_budget` | `PsiEpsilonBudgetPartitionLedger` | eps_psi(28)<=0.00002224 and psi(x)<1.00002841x for 8e11<=x<=e^28 | budget partition open; rough C=1280,C_Z=65536 template is far too weak |
| `rounding_and_hash` | `TableGeneratorHashInterfaceLedger` | directed rounding, interval propagation and reproducible table output | table value extraction closed, reproducible computation hash open |

## 2. 自足替换

```text
FiniteVerifiedZerosToZeroFreeTailTransitionLedger
  =>
FiniteRHHeightEndpointLedger AND ZeroFreeTailStartHeightLedger AND FiniteToTailNoGapNoOverlapLedger AND SameExplicitFormulaConventionLedger AND PsiEpsilonBudgetPartitionLedger AND TableGeneratorHashInterfaceLedger

DusartSchoenfeldPsiEpsilonTableExternalComputationAccepted
  =>
external contract only; does not close repository self-contained route

```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只处理早期零行反例链可调用的解析输入，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `FiniteVerifiedZeroTailTransitionGateActive` | `true` | `true` | 上一证书把下一最窄点设为有限 verified-zero 窗口与零点自由尾项的桥接。 | FiniteVerifiedZerosToZeroFreeTailTransitionLedger |
| `ExternalPiecesIdentifiedButNotAutomaticallyComposed` | `true` | `true` | Gourdon 有限零点与 Kadiri 零点自由区可登记为外部块，但二者不会自动生成 Dusart epsilon 表。 | FiniteVerifiedZerosToZeroFreeTailTransitionLedger or DusartSchoenfeldPsiEpsilonTableExternalComputationAccepted |
| `CommonVariableInterfaceTaxonomyClosed` | `true` | `true` | 桥接必须共用 x 区间、高度端点、零点自由阈值、显式公式核、余项预算和舍入 hash 六类变量。 | FiniteRHHeightEndpointLedger AND ZeroFreeTailStartHeightLedger AND FiniteToTailNoGapNoOverlapLedger AND PsiEpsilonBudgetPartitionLedger AND SameExplicitFormulaConventionLedger AND TableGeneratorHashInterfaceLedger |
| `FiniteRHHeightEndpointLedger` | `false` | `false` | 需要把外部零点数量或验证高度转成表生成器实际调用的精确高度端点。 | Gourdon10^13FiniteRHVerificationExternalAcceptedForTableInput |
| `ZeroFreeTailStartHeightLedger` | `false` | `false` | 需要登记零点自由区公式、常数 R、适用 t0，并说明表尾项从哪里开始使用。 | Kadiri2004ExplicitZeroFreeRegionExternalAcceptedForTableTail |
| `FiniteToTailNoGapNoOverlapLedger` | `false` | `false` | 需要证明有限 RH 覆盖段、零点自由尾段和显式公式截断段没有高度缺口、重叠重复扣费或变量换口径。 | FiniteRHHeightEndpointLedger AND ZeroFreeTailStartHeightLedger AND SameExplicitFormulaConventionLedger |
| `SameExplicitFormulaConventionLedger` | `false` | `false` | 需要证明 zero sum、zero-free tail、prime-power correction 与 psi/theta 表使用同一显式公式规范。 | SchoenfeldDusartEpsilonTableGeneratorFormalizationLedger |
| `PsiEpsilonBudgetPartitionLedger` | `false` | `false` | 需要把 finite-zero 主块、zero-free tail、平凡零点、素数幂和舍入误差分配到表值余量内。 | eps_psi(28)<=0.00002224 AND psi(x)<1.00002841x for 8e11<=x<=e^28 |
| `TableGeneratorHashInterfaceLedger` | `false` | `false` | 需要给出可复现表生成 hash，证明上述预算确实输出 0.00002224 和 1.00002841。 | ReproduciblePsiEpsilonTableComputationHashLedger |
| `FiniteVerifiedZerosToZeroFreeTailTransitionLedger` | `false` | `false` | 当前完成的是桥接接口压缩和变量表，不是自足闭合；缺任一变量账本都不能推出 epsilon 表。 | FiniteRHHeightEndpointLedger AND ZeroFreeTailStartHeightLedger AND FiniteToTailNoGapNoOverlapLedger AND SameExplicitFormulaConventionLedger AND PsiEpsilonBudgetPartitionLedger AND TableGeneratorHashInterfaceLedger |
| `ExternalConditionalBridgeAvailable` | `true` | `false` | 若显式接受 Dusart/Schoenfeld 表计算为外部合同，可条件跳过内部桥接账本。 | DusartSchoenfeldPsiEpsilonTableExternalComputationAccepted |
| `RowColumnUnconditionalClosed` | `false` | `false` | 有限零点到尾项桥接仍是解析输入审计；尚未产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一最窄点

```text
PsiEpsilonBudgetPartitionLedger
```
