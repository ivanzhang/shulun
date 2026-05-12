# Prime Matrix strict 迭代缩频核心密度账本路由器

**状态：** `iterated_scaled_core_density_ledger_closed_threshold_collapse_and_pdec_open`

迭代缩频核心密度账本已经闭合。若固定商型链为 (b_i,c_i)，则 h_r=h_0/prod b_i c_i，且因 b_i c_i>=2 有 |h_r|<=|h_0|/2^r。密度损耗也完全登记为 rho_r>=rho_0/prod A_{Lambda_i}，其中 A_{Lambda_i}<=8Lambda_i^2。于是递归层不再有循环或无名出口：每一层必须是 LCM 高度矛盾、固定商型 PDEC 逃逸，或阈值坍缩。当前唯一新的数学缺口是排斥阈值过早坍缩，另保留固定商型 PDEC 排斥。

```text
scaled_frequency_product_law_closed=true
strict_height_decay_closed=true
density_loss_product_ledger_closed=true
window_scale_product_law_closed=true
three_exit_ledger_closed=true
iterated_threshold_collapse_excluded=false
depthwise_lcm_explosion_proved=false
fixed_type_pdec_excluded=false
iterated_scaled_core_density_survival_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 统一账本

一条固定商型缩频链满足

```text
h_r = h_0 / prod_{i<=r} b_i c_i,
|h_r| <= |h_0| / 2^r.
```

对应密度阈值满足

```text
rho_r >= rho_0 / prod_{i<=r} A_{Lambda_i},
A_{Lambda_i} <= 8 Lambda_i^2.
```

所以固定商型路线已从“可能无限缠绕”变成有限深度的显式阈值账本。

## 2. 三出口

每一层只剩三种情况：

```text
1. LCM explosion against |h_r|;
2. fixed quotient-type ColumnCRT/PDEC escape;
3. threshold collapse before either trigger fires.
```

前两类是命名矛盾/证书出口；第三类是当前最新最窄硬点。

## 3. 引理表

| name | formula | status | meaning |
| --- | --- | --- | --- |
| `scaled_frequency_product_law` | h_r=h_0/prod_{i<=r} b_i c_i. | `closed` | 每层固定商型都精确剥离一个商型乘积。 |
| `strict_height_decay_law` | \|h_r\|<=\|h_0\|/2^r. | `closed` | 因每层 b_i c_i>=2，递归深度有限。 |
| `density_loss_product_law` | rho_r>=rho_0/prod_{i<=r} A_{Lambda_i}, with A_{Lambda_i}<=8Lambda_i^2. | `closed` | 密度损耗完全由有限字母表乘子登记。 |
| `window_scale_product_law` | Y_r is bounded by Y_0/prod_i max(b_i,c_i) and Y_0/prod_i min(b_i,c_i). | `closed` | 核心窗口尺度随商型链显式变化。 |
| `three_exit_ledger` | At each depth: LCM explosion, fixed-type PDEC escape, or threshold collapse. | `closed_dichotomy` | 迭代不再有第四种无名出口。 |
| `threshold_collapse_exclusion` | Show rho_r \|I_r\| stays above the trigger before height descent makes LCM impossible. | `open_input` | 剩余硬点是排斥阈值过早坍缩。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 仍在早期零行反例链的固定商型缩频迭代分支内。 | 保持 row_column_unconditional_closed=false。 |
| `ScaledFrequencyProductLawClosed` | `true` | `true` | 缩频频率等于初始频率除以全部商型乘积。 | 无。 |
| `StrictHeightDecayClosed` | `true` | `true` | 每层至少折半，递归不能无限循环。 | 无。 |
| `DensityLossProductLedgerClosed` | `true` | `true` | 全部密度损耗由 `prod A_Lambda` 显式登记。 | IteratedThresholdCollapseExclusionLedger |
| `ThreeExitLedgerClosed` | `true` | `true` | 每层只剩 LCM 高度矛盾、固定商型 PDEC、阈值坍缩三出口。 | DepthwiseLCMExplosionAgainstScaledFrequencyHeight OR FixedQuotientTypePDECColumnCertificateExclusion OR IteratedThresholdCollapseExclusionLedger |
| `IteratedThresholdCollapseExcluded` | `false` | `false` | 尚未证明阈值不会在触发 LCM/PDEC/SAE 前过早低于 1 个有效核心。 | IteratedThresholdCollapseExclusionLedger |
| `IteratedScaledCoreDensitySurvivalProved` | `false` | `false` | 账本已闭合，但尚未排斥阈值坍缩，也未排斥固定商型 PDEC。 | IteratedThresholdCollapseExclusionLedger AND FixedQuotientTypePDECColumnCertificateExclusion |

## 5. 下一步最窄点

```text
IteratedThresholdCollapseExclusionLedger
```

并列需要补齐：

```text
FixedQuotientTypePDECColumnCertificateExclusion
```

并行保留：

```text
DepthwiseLCMExplosionAgainstScaledFrequencyHeight AND BoundedQuotientTypeSAEAbsorption
```

审稿边界：本步闭合迭代账本和三出口分解；未证明阈值坍缩不发生，也未排斥固定商型 PDEC。
