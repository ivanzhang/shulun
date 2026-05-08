# Prime Matrix Rosser-Iwaniec 权重与 floor 余项账本路由器

**状态：** `rosser_weighted_floor_remainder_split_to_weight_definition_and_sawtooth_bound_open`

本步把 Rosser-Iwaniec 加权余项命题改写成可审稿的两个原子。第一，必须固定 lower weights lambda_d^- 与 level D；第二，在这些权重固定后，证明精确 CRT 残基 floor 余项的加权负损失不超过 90% 主项。没有权重账本时，旧余项命题还不是一个良定义定理。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
rosser_weight_floor_remainder_split=true
explicit_rosser_iwaniec_lower_weight_ledger_proved=false
exact_residue_weighted_floor_sawtooth_bound_proved=false
external_short_interval_rough_lower_bound_accepted=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 拆分律

```text
RosserIwaniecWeightedFloorRemainderTenPercentBound
  =>
(ExplicitRosserIwaniecLowerWeightLedgerAlpha043PGe100000 AND ExactResidueWeightedFloorSawtoothTenPercentBound)
```

精确 floor 对象：

```text
A_d^±(P)=# {1<=k<P: k ≡ rho_d^±(P) mod d}, rho_d^+(P) ≡ -P^2 mod d, rho_d^-(P) ≡ P^2 mod d.
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| RosserFloorRemainderGateActive | `true` | `false` | 最新内部最窄点是 Rosser-Iwaniec 下界权重与 floor 余项的 10% 主项控制。 | RosserIwaniecWeightedFloorRemainderTenPercentBound |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只在假设早期零行反例链条内整理尾段筛账本，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| ExactFloorFormulaAvailable | `true` | `true` | 一旦权重固定，余项对象有精确公式：A_d 是一个指定 CRT 残基在 1<=k<P 中的 floor 计数。 | 需要固定 lambda_d^- 与 level D。 |
| RemainderAtomSplitToWeightAndSawtooth | `true` | `false` | 旧余项原子先拆成权重定义账本与精确加权 sawtooth 余项界。 | ExplicitRosserIwaniecLowerWeightLedgerAlpha043PGe100000 AND ExactResidueWeightedFloorSawtoothTenPercentBound |
| ExplicitRosserIwaniecLowerWeightLedgerAlpha043PGe100000 | `false` | `false` | 需要明确 Rosser-Iwaniec lower weights lambda_d^-、支撑 level D、s=log D/log z 以及主项常数。 | ExplicitRosserIwaniecLowerWeightLedgerAlpha043PGe100000 |
| ExactResidueWeightedFloorSawtoothTenPercentBound | `false` | `false` | 权重固定后，证明 sum lambda_d^-(A_d-P/d) 的负向损失不超过 90% 主项。 | ExactResidueWeightedFloorSawtoothTenPercentBound |
| ExternalShortIntervalRoughNumberLowerBoundForAlpha043 | `false` | `false` | 外部路线仍可直接引用短区间 rough-number 下界，绕开内部权重余项账本。 | ExternalShortIntervalRoughNumberLowerBoundForAlpha043 |
| DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY | `false` | `false` | generic/external DI/BFI 宽口径仍在 canonical 自足边界外。 | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。 | DStructureRankinPromotionPackage。 |

## 3. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND (((ExplicitRosserIwaniecLowerWeightLedgerAlpha043PGe100000 AND ExactResidueWeightedFloorSawtoothTenPercentBound) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional 输入基：

```text
((NoFurtherCanonicalSourceTerminalPromotionGap AND (((ExplicitRosserIwaniecLowerWeightLedgerAlpha043PGe100000 AND ExactResidueWeightedFloorSawtoothTenPercentBound) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043))) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

global/external 宽口径输入基：

```text
DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY AND (((ExplicitRosserIwaniecLowerWeightLedgerAlpha043PGe100000 AND ExactResidueWeightedFloorSawtoothTenPercentBound) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 下一步

先攻 `ExplicitRosserIwaniecLowerWeightLedgerAlpha043PGe100000`：固定可计算的 lower weights、level 与主项常数。随后才能攻 `ExactResidueWeightedFloorSawtoothTenPercentBound`。若外部路线更优，则直接登记 `ExternalShortIntervalRoughNumberLowerBoundForAlpha043`。
