# Prime Matrix strict 边界残洞质量下界路由器

**状态：** `boundary_residual_mass_reduced_to_adaptive_prefix_potential_transfer_capacity_defect_open`

`BoundaryResidualMassLowerBoundForTypeCompression` 的自然 cutoff 版本不能作为免费内部输入：在 x 接近 P 时，它已经与短区间素数/底部平方根窗口同强。继续非循环推进的更紧源头是 adaptive prefix：把 cutoff 从 x 降到 z<x，先制造更厚的 prefix 残洞势，再证明早期零行迫使这些残洞无损转入同一 formal-unit 义务场。这一步产生三个真正剩余：prefix 势下界、prefix 到边界义务转移、以及容量乘子纪律；若 prefix 势异常偏低，则必须另证其登记为 PDEC/SAE/ColumnCRT 缺陷。当前仍未发现无条件直接矛盾，行/列命题不能升级为闭合。

```text
same_theorem_target_preserved=true
natural_cutoff_mass_not_free_diagnosed=true
adaptive_prefix_residual_definition_closed=true
adaptive_prefix_residual_potential_lower_bound_proved=false
prefix_residual_to_boundary_formal_unit_transfer_proved=false
registered_prefix_capacity_multiplier_discipline_proved=false
low_prefix_residual_mass_to_registered_phase_defect_proved=false
boundary_residual_mass_lower_bound_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 硬点压缩

拆分前：

```text
BoundaryResidualMassLowerBoundForTypeCompression
```

拆分后：

```text
AdaptivePrefixResidualPotentialLowerBound AND PrefixResidualToBoundaryFormalUnitObligationTransfer AND RegisteredPrefixCapacityMultiplierDiscipline AND LowPrefixResidualMassToRegisteredPhaseDefect
```

## 2. 残洞质量律

| law | formula | status |
| --- | --- | --- |
| `natural_cutoff_obstruction` | R_x at cutoff q<=x is the exact completed-line residual; proving it large near x~P meets the prime-window barrier. | `diagnosed_nonfree` |
| `bottom_band_exact_split` | R_{P-h}=PrimeColumns disjoint_union {a(h-a): P-a and P-h+a prime}. | `closed_as_reduction` |
| `adaptive_prefix_amplification` | For z<x, R_{x,z}={c: no q<=z divides xP+c}; EarlyZero forces R_{x,z} to be covered by labels q>z. | `definition_closed_transfer_open` |
| `low_mass_defect_route` | If a chosen prefix z has too few residuals, the deficit is a low-mod endpoint/sieve defect rather than silent failure. | `open_registered_exit` |
| `capacity_multiplier_discipline` | Prefix obligations must carry a multiplier ledger so q in (z,x] does not inflate reusable capacity for free. | `open` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ResidualMassInputActive` | `true` | `false` | 上一层已把 forced obligation 下界的首要缺口压到边界残洞质量。 | BoundaryResidualMassLowerBoundForTypeCompression |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只在假设早期零行反例链内推导，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| `NaturalCutoffResidualEquationImported` | `true` | `true` | CLB 已给出自然 cutoff q<=x 的恒等分解 U_x=R_x\F_x；早期零行等价于 R_x 被高标签补完。 | 这只是等价式，不给 \|R_x\| 的可用下界。 |
| `NaturalCutoffMassNotFreeDiagnosed` | `true` | `true` | 在 x 接近 P 的底部带，R_x 已精确分解为素数列与高素对曲线；证其足够大等价撞上短区间素数/平方根窗口输入。 | 不能把自然 cutoff 残洞下界当成免费内部引理。 |
| `SylvesterLargeFactorOnlyWeak` | `true` | `true` | Sylvester 只保证某列含 >P 的大因子，不保证该列没有 <=x 小因子，因此不给 R_x 质量。 | 需要筛余质量或登记缺陷，而不是单个大因子。 |
| `AdaptivePrefixResidualDefinitionClosed` | `true` | `true` | 对任意 z<x 可定义 R_{x,z}；若存在早期零行，则每个 prefix 残洞都必须由 q>z 的标签支付。 | 要证明这些 prefix 义务能进入同一 formal-unit 类型压缩账本。 |
| `WitnessAtomInterfaceImported` | `true` | `true` | 已有 witness obligation 域可记录 physical filler atoms、return 与 quotient；这给 prefix 义务转移的接口。 | PrefixResidualToBoundaryFormalUnitObligationTransfer |
| `AdaptivePrefixPotentialLowerBoundCurrentCorpusProved` | `false` | `false` | 当前语料尚未给出某个统一 z=z(P,x) 的全局筛余下界；可走经典低界筛外部输入，或内部化该筛余势。 | AdaptivePrefixResidualPotentialLowerBound |
| `PrefixTransferToFormalUnitCurrentCorpusProved` | `false` | `false` | 尚未证明从 R_{x,z} 产生的覆盖义务在升回边界 formal unit 后不丢失、不换题、不破坏 row-free type key。 | PrefixResidualToBoundaryFormalUnitObligationTransfer |
| `PrefixCapacityMultiplierDisciplineCurrentCorpusProved` | `false` | `false` | 降低 cutoff 会引入 q in (z,x] 的额外标签；必须登记容量乘子，防止同一标签复用被误算为大量不同实例。 | RegisteredPrefixCapacityMultiplierDiscipline |
| `LowPrefixMassDefectCurrentCorpusProved` | `false` | `false` | 若 prefix 筛余质量异常偏低，应推出低模端点/PDEC/SAE 缺陷；该回流尚未逐行证明。 | LowPrefixResidualMassToRegisteredPhaseDefect |
| `BoundaryResidualMassLowerBoundCurrentCorpusProved` | `false` | `false` | 自然 cutoff 质量下界不能直接闭合；最窄非循环路线转为 prefix 势、prefix 转移和容量乘子纪律三项。 | AdaptivePrefixResidualPotentialLowerBound AND PrefixResidualToBoundaryFormalUnitObligationTransfer AND RegisteredPrefixCapacityMultiplierDiscipline AND LowPrefixResidualMassToRegisteredPhaseDefect |

## 4. 最窄继续点

直接攻：

```text
PrefixResidualToBoundaryFormalUnitObligationTransfer
```

并行保留：

```text
AdaptivePrefixResidualPotentialLowerBound AND RegisteredPrefixCapacityMultiplierDiscipline AND LowPrefixResidualMassToRegisteredPhaseDefect
```

审稿边界：本步证明的是自然残洞质量硬点的非循环改写；它没有证明 prefix 势下界、没有证明容量乘子纪律，也没有关闭行/列无条件命题。
