# Prime Matrix strict 兄弟冷核心数值 envelope 攻坚路由器

**状态：** `sibling_numeric_envelope_reduced_to_support_overlap_and_collar_open`

`SiblingColdCoreThresholdNumericEnvelopeTable` 已被进一步下钻。同一父前缀 `U` 的兄弟冷收费不能靠独立常数 `C_sib(U)` 猜测闭合；它有精确投影恒等式：所有子收费对象 `(g,k)` 经 `d=gk` 投到父频率除数支撑，于是兄弟总收费等于父投影支撑大小加同一父除数的重复收费债。因此可留在冷供给里的 sibling envelope 只能是父级 scaled-child union support，重复收费必须登记为固定历史或 ColumnCRT 回流，外向缩放产生的边界 collar 也必须进入同参数数值界。本步关闭的是结构恒等式和 `C_sib` 的合法定义，尚未证明父支撑数值上界、overlap 排斥或 collar 上界；行/列命题仍未无条件闭合。

```text
sibling_charging_ledger_imported=true
sibling_multiset_projection_identity_proved=true
free_constant_c_sib_rejected=true
exact_c_sib_support_definition_closed=true
parent_scaled_child_union_support_numeric_envelope_proved=false
sibling_overlap_multiplicity_return_excluded=false
sibling_scaled_window_collar_numeric_envelope_proved=false
sibling_cold_core_threshold_numeric_envelope_proved=false
row_column_unconditional_closed=false
```

## 精确拆分

| piece | formula | meaning |
|---|---|---|
| `child multiset` | `F_U={(g,k): g in G_U, k\|H_U/g, k in I_{U,g}}` | 所有兄弟冷窗口原始收费对象。 |
| `parent projection` | `pi(g,k)=gk, so pi(F_U) subset {d:d\|H_U}` | 把子核心推回父频率除数支撑。 |
| `exact identity` | `\|F_U\|=\|pi(F_U)\|+sum_d(max(mu_U(d)-1,0))` | 兄弟总收费等于父支撑数加重复收费债。 |
| `support budget` | `C_sib,supp(U)=\|pi(F_U)\|` | 可留在冷供给中的整族支撑项。 |
| `overlap return` | `E_overlap(U)=sum_d(max(mu_U(d)-1,0))` | 同一父除数被多个孩子重复收费时必须回流固定历史或 ColumnCRT。 |
| `collar discipline` | `pi(F_U) uses union_g g I_{U,g}, not a naive single parent interval` | 外向取整产生的边界 collar 必须被数值 envelope 覆盖或命名回流。 |

## 有限模型核验

| H_U | parent window | children | child charge | projected support | overlap excess | collar support | identity |
|---:|---|---|---:|---:|---:|---:|---:|
| 360 | `[20, 180]` | `[2, 3, 5, 6]` | 37 | 12 | 25 | 1 | `true` |
| 840 | `[30, 240]` | `[2, 3, 4, 5, 7]` | 46 | 14 | 32 | 1 | `true` |
| 1260 | `[50, 420]` | `[3, 4, 5, 6, 7, 9]` | 51 | 14 | 37 | 1 | `true` |
| 2520 | `[60, 720]` | `[4, 5, 6, 7, 8, 9, 10]` | 82 | 21 | 61 | 1 | `true` |

## 判定表

| gate | closed | proved | meaning | remaining |
|---|---:|---:|---|---|
| `SiblingChargingLedgerImported` | `true` | `true` | 上一层已关闭兄弟收费/热回流账本规则。 | `SiblingColdCoreThresholdNumericEnvelopeTable` |
| `MultisetProjectionIdentityProved` | `true` | `true` | 同父前缀兄弟收费可精确分解为父支撑计数和重叠债。 | `ParentScaledChildUnionSupportNumericEnvelope` |
| `FreeConstantCsibRejected` | `true` | `true` | C_sib(U) 不能作为固定常数猜测；必须由同参数父支撑表生成。 | `ParentScaledChildUnionSupportNumericEnvelope` |
| `ExactCsibSupportDefinitionClosed` | `true` | `true` | 可留在冷供给的 C_sib,supp(U) 定义为 projected support 的实际大小。 | `ParentScaledChildUnionSupportNumericEnvelope` |
| `OverlapDebtRegisteredButNotExcluded` | `true` | `false` | 重复收费已可命名为固定历史/ColumnCRT 债，但尚未全局排斥。 | `SiblingOverlapMultiplicityFixedReturnOrColumnCRTExclusion` |
| `BoundaryCollarNumericEnvelopeProved` | `false` | `false` | 外向缩放后的 union_g gI_{U,g} 需要同参数 collar 数值界。 | `SiblingScaledWindowCollarNumericEnvelope` |
| `ParentSupportNumericEnvelopeProved` | `false` | `false` | 尚未证明 projected support 在父级 union/collar 中满足可求和数值上界。 | `ParentScaledChildUnionSupportNumericEnvelope AND ColdCoreThresholdFunctionNumericTable` |
| `SiblingColdCoreThresholdNumericEnvelopeProved` | `false` | `false` | 结构恒等式已闭合，但父支撑、collar 和 overlap 三项尚未全部关闭。 | `ParentScaledChildUnionSupportNumericEnvelope AND SiblingOverlapMultiplicityFixedReturnOrColumnCRTExclusion AND SiblingScaledWindowCollarNumericEnvelope` |
| `TerminalColdWindowAntiCascadeProved` | `false` | `false` | 兄弟数值 envelope 仍未完成，反级联不能升级为定理。 | `SiblingColdCoreThresholdNumericEnvelopeTable AND TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到早期零行反例链的终端矛盾。 | `ParentScaledChildUnionSupportNumericEnvelope AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 下一步

- 主攻：`ParentScaledChildUnionSupportNumericEnvelope`。
- 并行保留：
  - `SiblingOverlapMultiplicityFixedReturnOrColumnCRTExclusion`
  - `SiblingScaledWindowCollarNumericEnvelope`
  - `ColdCoreThresholdFunctionNumericTable`
  - `SameParameterPDECThresholdNumericTable`
  - `TerminalCoreHotDivisorWindowPDECorSAE`
  - `FixedTypeHistoryPDECExclusion`
  - `TerminalColdWindowCompatibilityAntiCascadeLemma`
  - `IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore`
  - `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`

## 证据哈希

| file | sha256 |
|---|---|
| `experiments/prime_matrix_strict_sibling_numeric_envelope_attack_router.py` | `84b9b8b64f345ef2c616d067002d0c9a58de67fe24401e434b5627da49738c2d` |
| `docs/monograph/prime-matrix-strict-cold-window-sibling-charging-router.json` | `be05fb4b2dee03515ca4eea8e086eff6341c0e04d69da9501072cccf74414591` |
| `docs/monograph/prime-matrix-strict-terminal-cold-window-anticascade-attack-router.json` | `c2ef211342a04f992f35f62a595d3c1647663d1a9fde5d1e78ff57c735bf63d6` |
| `docs/monograph/prime-matrix-strict-cold-core-threshold-dyadic-invariance-router.json` | `c93a11c1f9f9a11728fb454eb16ead7a4cc308bdfcf2647af6dcb20d6f405602` |
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.json` | `a689365ed710e4e9239a844479f62f45f1cbd1c2f6a1410a349153ddee1b06c0` |
| `docs/monograph/prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json` | `7c34a1965c8ddc44a43cafb902ae668fb7ed21db3fc6f73cb42716be37c213be` |
