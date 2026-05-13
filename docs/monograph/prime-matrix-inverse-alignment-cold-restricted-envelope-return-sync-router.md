# Prime Matrix 冷限制逆元 envelope 回流同步路由器

**状态：** `cold_restricted_inverse_alignment_envelope_synced_to_cold_numeric_tables_open`

`ColdRestrictedInverseAlignmentSiblingChargeEnvelope` 不再是独立硬点。逆元 tau 桶的 raw 容量上界过宽；加入冷限制后，它正好落入已有兄弟收费链：tau/cold 兄弟收费投影到父支撑，重复收费登记为 overlap 回流，collar 宽度爆发进入 LCM/共同核，共同核回流不能免费循环，最终回到回流后冷供给数值包。因此对非持久预算而言，逆元方程组已经被充分并入前沿；真正剩余不是新的逆元结构，而是同参数 `C_core` 与 `T_PDEC` 数值表，以及并行的热/固定/持久终端排斥。

```text
cold_restricted_inverse_alignment_envelope_synced_to_return_frontier=true
effective_pruning_closed_for_inverse_alignment_nonpersistent_budget=true
cold_core_threshold_numeric_table_proved=false
same_parameter_pdec_threshold_numeric_table_proved=false
cold_supply_same_parameter_numeric_envelope_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 路由链

| stage | fact | route |
| --- | --- | --- |
| `raw inverse tau` | all tau capacity is bounded by sum_{z<q<P} mu_q but this is Theta(P) | raw envelope rejected as sufficient |
| `cold restriction` | only tau buckets passing terminal cold tests may remain in nonpersistent cold supply | sibling charging ledger |
| `sibling projection` | child charges project to parent divisor support plus overlap debt | parent support / overlap return / collar |
| `collar and LCM` | collar width overflow routes to LCM height or low-multiplier common kernel | width LCM compression |
| `return cycle` | common-kernel return cannot loop for free; it descends or becomes PDEC/fixed history | no-free return cycle |
| `after-return cold budget` | nonpersistent cold supply now only needs same-parameter C_core and T_PDEC numeric tables | ColdCoreThresholdFunctionNumericTable + SameParameterPDECThresholdNumericTable |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ColdRestrictedEnvelopeTargetImported` | `true` | `false` | 上一层把 raw 逆元 tau envelope 的不足压成冷限制 envelope。 | ColdRestrictedInverseAlignmentSiblingChargeEnvelope |
| `ColdRestrictedEnvelopeIndependentHardpointRemoved` | `true` | `true` | 冷限制逆元 tau 桶已接入兄弟收费、父支撑、collar、共同核回流和回流后预算链。 | none as independent hardpoint |
| `EffectivePruningClosedForNonpersistentBudget` | `true` | `true` | 对非持久冷供给，终端反级联失败、兄弟超收费和共同核回流都不能继续算作免费冷容量。 | ColdCoreThresholdFunctionNumericTable AND SameParameterPDECThresholdNumericTable |
| `ColdCoreNumericTableProved` | `false` | `false` | 同参数 C_core 可求和数值表仍未证明。 | ColdCoreThresholdFunctionNumericTable |
| `PDECThresholdNumericTableProved` | `false` | `false` | 同参数 T_PDEC 阈值表仍未证明。 | SameParameterPDECThresholdNumericTable |
| `ColdSupplySameParameterNumericEnvelopeProved` | `false` | `false` | 冷供给数值 envelope 尚未闭合；当前只关闭了逆元冷限制 envelope 的独立性。 | ColdCoreThresholdFunctionNumericTable AND SameParameterPDECThresholdNumericTable |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未同时完成冷数值表、持久 moving atom 排斥和 DStructure/Rankin 验收。 | ColdCoreThresholdFunctionNumericTable AND SameParameterPDECThresholdNumericTable AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 下一步

- 主攻：`ColdCoreThresholdFunctionNumericTable`。
- 并行保留：
  - `SameParameterPDECThresholdNumericTable`
  - `TerminalCoreHotDivisorWindowPDECorSAE`
  - `FixedTypeHistoryPDECExclusion`
  - `IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore`
  - `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`

审稿边界：本步只删除冷限制逆元 envelope 的独立性，不证明冷数值表，不声明行/列命题无条件闭合。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-inverse-alignment-sibling-charge-uniform-envelope-router.json` | `83c35aa6bc0fa34003c64e89e141054faee5ea873bc7f2270ed670846499104c` |
| `docs/monograph/prime-matrix-strict-cold-supply-numeric-after-return-cycle-router.json` | `5be154f20bb3ff27a7c356dc2fc1d9b2a963be039e3c4f94ec2d941a7e47f721` |
| `docs/monograph/prime-matrix-strict-common-kernel-return-cycle-descent-router.json` | `133a5b59827c92d7e6e3b2cefcadf6f8c67b5b999fa6a1b5e7cbda57b8d4e671` |
| `docs/monograph/prime-matrix-strict-parent-support-numeric-envelope-router.json` | `c6fe6dcdc47b377c9a55915560031ec8b37d528f6d9980eedbce671a2ee8d653` |
| `docs/monograph/prime-matrix-strict-sibling-collar-cap-table-router.json` | `04affb2be59db89256bbc83cb022d0808a473268dff3de85d9f2230214a06b42` |
| `docs/monograph/prime-matrix-strict-sibling-collar-width-lcm-kernel-router.json` | `973a1c986598cb27dd132354715b336eae7938103c89d09da451123f2ade08de` |
| `docs/monograph/prime-matrix-strict-sibling-numeric-envelope-attack-router.json` | `52bd322127d85f72df347da33b5ccc71b6ef2c023539db38244793e6d8d3448c` |
| `docs/monograph/prime-matrix-strict-unified-budget-after-return-cycle-sync-router.json` | `0b1f76cce75b61929c79f82036782b10d6c1755b84840de0e666224ad5ae7922` |
| `experiments/prime_matrix_inverse_alignment_cold_restricted_envelope_return_sync_router.py` | `1596729e178ee9c3004dad9659ebdefa4c2711817567c7ab4e99c81d6ec07763` |
