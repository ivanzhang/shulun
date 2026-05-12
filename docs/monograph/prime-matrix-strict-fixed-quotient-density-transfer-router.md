# Prime Matrix strict 固定商型密度传递路由器

**状态：** `fixed_quotient_density_transfer_closed_iterated_threshold_and_pdec_open`

固定商型密度传递已经闭合到显式乘子账本。对固定互素商型 (b,c)，核心 k 与 pair (kb,kc) 一一对应，因此该商型内部没有计数损失。跨商型选择至多损失有限字母表因子 A_Lambda<=8Lambda^2；有向/无向口径的常数损失也并入这个因子。于是 pair-lock 密度进入缩频 core-density 时没有未登记损耗。新的剩余是多层缩频后阈值是否仍足以触发 LCM/PDEC/SAE，或固定商型 PDEC 是否可排斥。

```text
core_pair_bijection_closed=true
finite_type_pigeonhole_loss_closed=true
core_window_distortion_bound_closed=true
density_transfer_without_loss_closed=true
no_untracked_weight_loss_closed=true
iterated_threshold_survival_proved=false
fixed_pdec_excluded=false
fixed_quotient_type_excluded=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 无隐性损失

固定 `(b,c)` 后，映射

```text
k -> (kb,kc)
```

是一一对应。因此固定商型内部没有 pair 到 core 的计数损失。

若还没有固定商型，只知道总共有 `T` 个大核 pair-lock，则上一层给出商型数

```text
A_Lambda <= 8 Lambda^2.
```

鸽巢后存在某个商型至少贡献

```text
T/A_Lambda
```

个核心 `k`。这就是全部损耗；后续证明必须把它写入阈值账本，不能再额外引入未登记常数。

## 2. 剩余不是循环，而是阈值账本

固定商型递归每步已有 `|h| -> |h|/(bc) <= |h|/2` 的高度下降。现在真正剩余是：经过有限多层后，`prod A_Lambda` 的损耗是否仍允许触发 LCM 高度矛盾或 PDEC/SAE 出口。

## 3. 引理表

| name | formula | status | meaning |
| --- | --- | --- | --- |
| `fixed_type_core_pair_bijection` | For fixed coprime (b,c), k <-> (kb,kc) is one-to-one. | `closed` | 固定商型内部从 pair 到 core 不丢计数。 |
| `finite_type_pigeonhole_loss` | With at most A_Lambda<=8Lambda^2 types, T pair locks give some type with >=T/A_Lambda cores. | `closed` | 跨商型选择只有登记的有限字母表损失。 |
| `core_window_distortion_bound` | Y/max(b,c)<k<=2Y/min(b,c), with 1<=b,c<2Lambda. | `closed` | 核心窗口长度和乘法比被 Lambda 显式控制。 |
| `registered_density_threshold_transfer` | A pair-lock density rho transfers to core density at least rho/(8Lambda^2) after type selection. | `closed` | 密度阈值没有隐性丢失；所有损耗进入显式乘子账本。 |
| `no_untracked_weight_loss` | Any orientation or duplicate convention costs at most a factor 2 and is absorbed into A_Lambda. | `closed` | 有向/无向 pair 口径不会形成额外未登记误差。 |
| `iterated_threshold_survival` | After depth r, threshold loss is controlled by product_r A_{Lambda_r}; it must still beat the PDEC/SAE trigger. | `open_input` | 多层缩频递归的阈值账本仍需独立闭合。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 仍在早期零行反例链的固定商型缩频分支内。 | 保持 row_column_unconditional_closed=false。 |
| `CorePairBijectionClosed` | `true` | `true` | 固定商型内部 `k` 与 `(kb,kc)` 一一对应。 | 无。 |
| `FiniteTypePigeonholeLossClosed` | `true` | `true` | 跨商型只损失 `<=8Lambda^2` 的显式因子。 | BoundedQuotientTypeSAEAbsorption |
| `DensityTransferWithoutLossClosed` | `true` | `true` | pair-lock 密度到 core-density 的全部损耗已登记。 | IteratedScaledCoreDensitySurvivalOrPDECEscape |
| `IteratedThresholdSurvivalProved` | `false` | `false` | 尚未证明多层递归后的阈值仍足以触发 PDEC/SAE 或 LCM 高度矛盾。 | IteratedScaledCoreDensitySurvivalOrPDECEscape |
| `FixedPDECExcluded` | `false` | `false` | 尚未排斥跨 formal unit 的固定商型 PDEC/ColumnCRT 证书。 | FixedQuotientTypePDECColumnCertificateExclusion |

## 5. 下一步最窄点

```text
IteratedScaledCoreDensitySurvivalOrPDECEscape
```

并列需要补齐：

```text
FixedQuotientTypePDECColumnCertificateExclusion
```

并行保留：

```text
StrictHeightDescentFiniteDepthLedger AND BoundedQuotientTypeSAEAbsorption
```

审稿边界：本步闭合密度传递的显式损耗账本；未闭合多层阈值生存，也未排斥固定商型 PDEC。
