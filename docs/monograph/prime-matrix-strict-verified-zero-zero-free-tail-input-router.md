# Prime Matrix strict verified-zero/zero-free tail 输入路由器

**状态：** `verified_zero_zero_free_tail_input_sources_extracted_large_height_and_tail_bridge_open`

epsilon 表的零点输入被拆清：它不是仓库已有 `T<=14` 低高度核验，而是大高度有限 RH 验证、显式零点自由区尾项和二者的桥接算法共同支撑。当前只完成外部来源边界抽取；缺少可复现的大高度零点证书、尾段零点自由常数和表生成桥接 hash。

```text
zero_input_source_extraction_closed=true
verified_zero_and_zero_free_tail_input_closed=false
large_finite_rh_verification_table_input_closed=false
explicit_zero_free_region_table_tail_closed=false
finite_verified_zero_to_tail_transition_closed=false
low_height_t14_external_ready_but_insufficient=true
symbolic_zero_free_ready_but_numeric_table_tail_open=true
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 来源边界

| source | input | role | url |
| --- | --- | --- | --- |
| `Rosser-Schoenfeld 1975` | first 3,502,500 zeros on the critical line/strip in the classical table lineage | historical finite RH verification input | https://www.ams.org/mcom/1975-29-129/S0025-5718-1975-0457373-8/ |
| `van de Lune-te Riele-Winter 1986` | first 1,500,000,000 zeros | larger finite RH verification input cited by Dusart | https://www.ams.org/mcom/1986-46-174/S0025-5718-1986-0829637-3/ |
| `Gourdon 2004` | first 10^13 nontrivial zeros | largest finite RH verification cited by Dusart for improved tables | http://numbers.computation.free.fr/Constants/Miscellaneous/zetazeros1e13-1e24.pdf |
| `Kadiri 2004` | explicit zero-free region | zero-free tail input cited by Dusart | https://arxiv.org/abs/math/0401238 |
| `Dusart arXiv:1002.0442` | source text tying finite RH verification and zero-free regions to psi/theta tables | boundary statement, not a reproducible table computation artifact | https://arxiv.org/abs/1002.0442 |

## 2. 自足替换

```text
VerifiedZeroAndZeroFreeTailInputForSchoenfeldDusartTableLedger
  =>
LargeFiniteRHVerificationForPsiEpsilonTableLedger AND ExplicitZeroFreeRegionForTableTailLedger AND FiniteVerifiedZerosToZeroFreeTailTransitionLedger

FiniteVerifiedZerosToZeroFreeTailTransitionLedger
  =>
LargeFiniteRHVerificationForPsiEpsilonTableLedger AND ExplicitZeroFreeRegionForTableTailLedger AND SchoenfeldDusartEpsilonTableGeneratorFormalizationLedger

```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只审计 epsilon 表所需解析输入，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `VerifiedZeroZeroFreeTailGateActive` | `true` | `true` | 上一证书把下一最窄点设为表生成器所需的有限零点验证与零点自由尾项输入。 | VerifiedZeroAndZeroFreeTailInputForSchoenfeldDusartTableLedger |
| `DusartSchoenfeldZeroInputSourceExtractionLedger` | `true` | `true` | 已从 Dusart/Schoenfeld 线索中抽出表值依赖的外部零点验证与零点自由区来源。 | Rosser-Schoenfeld, van de Lune, Gourdon, Kadiri, Dusart |
| `LowHeightT14IsNotEnoughForPsiTable` | `true` | `true` | 仓库已外部匹配 T<=14 低高度核验，但 psi epsilon 表需要大高度有限 RH 验证和尾项桥接，不能由 T<=14 替代。 | LargeFiniteRHVerificationForPsiEpsilonTableLedger |
| `SymbolicZeroFreeRegionNotEnoughForTableTail` | `true` | `true` | 仓库已有符号零点自由区链和部分常数化路线，但表尾项需要明确的可复算数值常数与阈值。 | ExplicitZeroFreeRegionForTableTailLedger |
| `LargeFiniteRHVerificationForPsiEpsilonTableLedger` | `false` | `false` | 需要指定表生成实际使用的有限 RH 验证高度/零点数、来源证书、覆盖范围和 hash。 | Gourdon10^13 OR equivalent verified-zero certificate with reproducible audit |
| `ExplicitZeroFreeRegionForTableTailLedger` | `false` | `false` | 需要指定尾段使用的显式零点自由区常数、适用高度和同一表算法中的误差预算。 | Kadiri/Rosser-Schoenfeld zero-free constants or internal proof |
| `FiniteVerifiedZerosToZeroFreeTailTransitionLedger` | `false` | `false` | 需要证明有限零点验证窗口和零点自由尾项如何拼接成 eps_psi(b) 的整段表值，含阈值选择和余项分配。 | LargeFiniteRHVerificationForPsiEpsilonTableLedger AND ExplicitZeroFreeRegionForTableTailLedger AND SchoenfeldDusartEpsilonTableGeneratorFormalizationLedger |
| `VerifiedZeroAndZeroFreeTailInputForSchoenfeldDusartTableLedger` | `false` | `false` | 当前只完成来源边界和缺口分类；没有可复现大高度零点证书、零点自由尾项常数和桥接算法。 | LargeFiniteRHVerificationForPsiEpsilonTableLedger AND ExplicitZeroFreeRegionForTableTailLedger AND FiniteVerifiedZerosToZeroFreeTailTransitionLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | verified-zero/zero-free 输入审计不产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一最窄点

```text
LargeFiniteRHVerificationForPsiEpsilonTableLedger
```
