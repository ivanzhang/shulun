# Prime Matrix strict acyclic seed 与终端家族门融合路由器

**状态：** `strict_acyclic_seed_independent_input_removed_terminal_family_open`

本步把 `AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn` 从最终并列输入基中删除，但不是证明 seed 存在。理由是严格二分：若假设早期零行反例链能给出合法 seed，则后续 ExactUV、pair-mass、moving-atom 与 NC-BLK 路由已经把失败态接回 acyclic terminal family；若给不出 seed，来源环切断、早期零行 seed no-go 和独立来源恒等式分类又强制它回流同一 PDEC/SAE/ColumnCRT/CleanKLS 终端家族。因此 seed 不再是独立闭合输入，真正剩余收缩为 acyclic terminal family，另加高段 Mertens/PNT 自足尾项与 DStructure/Rankin 替代包。行/列命题仍未无条件闭合。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
seed_exists_branch_covered_by_terminal_family=true
seed_absent_branch_returned_to_terminal_family=true
acyclic_pre_cauchy_seed_independent_input_removed=true
acyclic_pre_cauchy_seed_proved=false
strict_acyclic_terminal_family_proved=false
self_contained_mertens_tail_proved=false
self_contained_dstructure_rankin_replacement_proved=false
row_column_unconditional_closed=false
terminal_gap_after_router=PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily
```

## 1. 融合二分

```text
Assume EarlyZeroRowWithinP
  -> valid acyclic pre-Cauchy source seed exists
       -> ExactUV / pair-mass / moving-atom / NC-BLK returns
       -> PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily
  -> no valid seed exists
       -> source-loop cut + zero-row seed no-go + identity taxonomy
       -> PDEC / SAE / ColumnCRT / CleanKLS return
       -> PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily
```

所以本步只删除 seed 的独立输入地位；不声明 seed 定理成立。

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `SeedAndTerminalBothActive` | `true` | `false` | 上一层 strict 基同时含 acyclic pre-Cauchy seed 与 acyclic terminal family。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只在假设早期零行反例链内做分支覆盖，不使用真实零行缺席。 | 所有 seed 缺失或 seed 下游失败必须进入命名终端家族。 |
| `SeedExistsBranchCovered` | `true` | `true` | 若反例链确有合法 acyclic pre-Cauchy seed，则 ExactUV/pair-mass/NC-BLK 路由已把失败对象接回终端家族。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily |
| `SeedAbsentBranchReturned` | `true` | `true` | 若反例链不能给出 seed，来源环切断与早期零行 seed no-go 已禁止 clean-core 偷渡，强制回流 PDEC/SAE/ColumnCRT/CleanKLS。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily |
| `IndependentIdentityNotFourthExit` | `true` | `true` | 独立 pre-Cauchy 来源恒等式已被分类：canonical scoped、generic rejected、external not-self-contained，actual 分支回到 moving-block/NC-BLK。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily |
| `MovingBlockReturnImported` | `true` | `true` | actual moving-block/NC-BLK 若出现大原子，已由 moving-block 与 strict NC-BLK 路由接回早期零行/全局终端门。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily |
| `SeedNoLongerIndependentConjunct` | `true` | `true` | seed 不是被证明存在，而是通过存在/不存在两支都落入同一终端家族，故可从最终并列输入基中删除。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily |
| `AcyclicPreCauchySeedCurrentCorpusProved` | `true` | `false` | 当前仍没有构造 acyclic pre-Cauchy seed；本步不声称 seed 定理成立。 | seed 已变成分支准入门，不再是独立闭合输入。 |
| `StrictAcyclicTerminalFamilyCurrentCorpusProved` | `true` | `false` | 终端家族本身仍未排斥；这是 seed 融合后的真正数学主攻点。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn |
| `HighTailCurrentCorpusProved` | `true` | `false` | 若不接受外部 Mertens/theta 定理，高段 PNT/Mertens 自足尾项仍开放。 | SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000 |
| `DStructureRankinCurrentCorpusProved` | `true` | `false` | DStructure/Tail-log4/finite Rankin 替代包仍未自足证明。 | SelfContainedDStructureTailLog4FiniteRankinReplacementPackage。 |
| `RowColumnUnconditionalClosureCurrentCorpusProved` | `true` | `false` | seed 融合后仍缺终端家族、高段自足尾项或外部接受、DStructure/Rankin 替代包。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage |

## 3. 最新严格基

融合前：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

融合后：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

若明确接受外部 Mertens/theta 显式输入，高段尾项可暂时移出活动缺口，剩：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

## 4. 下一主攻合同

下一数学主攻点：`AcyclicTerminalFamilyThreeAtomDirectAttack`。

三原子终端门：

```text
AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn
```

建议优先顺序：
- `DirectAcyclicSameSetPDECCapDualCertificate`。
- `DirectAcyclicCleanKLSDLSEstimateWithNamedReturn`。
- `AcyclicTerminalCanonicalLockToCanonicalSourceBoundary`。

必须证明：
- 在同一坏窗集合和同一 formal unit 下证明 direct acyclic PDEC 对偶容量证书。
- 或证明 diffuse clean residual 的 direct acyclic KLS/DLS 吸收并把失败命名回流。
- 若改用 canonical-lock，必须证明同集推前、无 payload 残留和有限因子图。
- 继续保持 seed 存在/不存在两支都覆盖。
- 保留高段尾项与 DStructure/Rankin 替代包的独立状态。

不能作为证明使用：
- 把 seed 融合误写成 seed 已证明存在。
- 从 unsigned 早期零行覆盖图反推出 signed source seed。
- 把 canonical-source 终端闭合直接导入 acyclic noncanonical 分支。
- 把当前已物化样本清零当作全局终端家族排斥。
- 把外部谱定理或外部 Mertens/theta 当作 strict 自足证明。
