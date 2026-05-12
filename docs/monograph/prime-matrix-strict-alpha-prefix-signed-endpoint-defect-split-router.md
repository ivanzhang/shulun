# Prime Matrix strict alpha-prefix 有符号端点缺陷分裂路由器

**状态：** `signed_endpoint_defect_forced_and_split_low_dyadic_far_tail_exclusion_open`

上一层的 TV 缺陷可以加强为有符号端点缺陷：lower-weight 和 L_alpha=(P-1)W^-_alpha+E_alpha 精确成立；若早期零行又要求 R_alpha 不超过高标签容量 C_alpha，而主项间隙 G_alpha=(P-1)W^-_alpha-C_alpha 为正，则必须有 E_alpha<=-G_alpha。随后按低模、中间 dyadic、远尾 core 分裂，若低模和远尾不能承担固定比例负缺陷，就得到某个 dyadic 块上的 PDEC 证书。这仍是缺陷显化，不是缺陷排斥。

```text
signed_endpoint_defect_forced=true
low_middle_far_split_closed=true
dyadic_pigeonhole_closed=true
high_dyadic_endpoint_lock_imported=true
signed_endpoint_defect_excluded=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 有符号缺陷公式

令

```text
L_alpha(x)=sum_d lambda_d^- A_d(x),
A_d(x)=(P-1)/d + epsilon_d(x).
```

则

```text
L_alpha(x)=(P-1)W_alpha^- + E_alpha(x),
E_alpha(x)=sum_d lambda_d^- epsilon_d(x).
```

若早期零行成立，则 `L_alpha(x)<=R_alpha(x)<=C_alpha(P)`。因此一旦

```text
G_alpha=(P-1)W_alpha^- - C_alpha(P)>0,
```

就强制

```text
E_alpha(x)<=-G_alpha.
```

这不是普通误差上界问题，而是有方向的端点 CRT 缺陷。

## 2. 闭合蕴含

| name | formula | status | meaning |
| --- | --- | --- | --- |
| `lower_weight_exact_endpoint_sum` | L_alpha(x)=sum_d lambda_d^- A_d(x)=(P-1)W_alpha^-+E_alpha(x), E_alpha=sum_d lambda_d^- epsilon_d(x). | `closed` | 把粗筛 lower sum 精确拆成主项和有符号端点误差。 |
| `capacity_forces_negative_endpoint` | If EarlyZeroRow and G_alpha=(P-1)W_alpha^- - C_alpha(P)>0, then E_alpha(x)<=-G_alpha. | `closed_implication` | 这是比 TV 大更强的同向负端点缺陷。 |
| `low_middle_far_split` | E_alpha=E_low(D0)+sum_j E_{I_j}+E_far(D1). | `closed_identity` | 缺陷可以按低模、中间 dyadic 块、远尾 core 精确分裂。 |
| `dyadic_pigeonhole` | If E_alpha<=-G, E_low>-eta0 G, E_far>-eta1 G, then some middle block E_I<=-(1-eta0-eta1)G/J. | `closed_implication` | 强缺陷不能无形分散；不是低模/远尾承担，就必有 dyadic PDEC 证书。 |
| `high_dyadic_lock_import` | When the defect block has d>P-1, each modulus has at most one endpoint hit. | `imported_closed` | 高块缺陷进一步变成 HDL-9/HDL-10 型端点命中偏斜。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 仍在早期零行假设下推出有符号缺陷。 | 保持 row_column_unconditional_closed=false。 |
| `SignedEndpointDefectForced` | `true` | `true` | 若 lower-weight 主项超过高标签容量，早期零行强制 E_alpha<=-G_alpha。 | AlphaLowerWeightMainGapPositiveAgainstHighLabelCapacity |
| `DyadicSplitClosed` | `true` | `true` | 强负缺陷若不由低模或远尾承担，必落入某个中间 dyadic 块。 | LowModSignedEndpointDefectExclusion OR DyadicLowerWeightEndpointPDECExclusion OR LowerWeightFarTailCoreOrSAEExclusion |
| `HighDyadicEndpointLockImported` | `true` | `true` | 高块 `d>P-1` 时端点误差是单命中 CRT 偏斜，可接 HDL/CoreLoad。 | HDL-9/HDL-10 energy exclusion |
| `SignedEndpointDefectExcludedCurrentCorpus` | `false` | `false` | 低模、dyadic PDEC、远尾 core 三出口尚未全部排斥。 | LowModSignedEndpointDefectExclusion AND DyadicLowerWeightEndpointPDECExclusion AND LowerWeightFarTailCoreOrSAEExclusion |
| `RowColumnClosed` | `false` | `false` | 当前只得到精确缺陷显化，不得到无条件闭合。 | AlphaLowerWeightMainGapPositiveAgainstHighLabelCapacity plus exclusion of LowModSignedEndpointDefectExclusion/DyadicLowerWeightEndpointPDECExclusion/LowerWeightFarTailCoreOrSAEExclusion |

## 4. 最新最窄输入

```text
DyadicLowerWeightEndpointPDECExclusion
```

并行保留：

```text
LowModSignedEndpointDefectExclusion AND LowerWeightFarTailCoreOrSAEExclusion AND AlphaLowerWeightMainGapPositiveAgainstHighLabelCapacity
```

审稿边界：本步只把强缺陷从抽象 TV 压成有符号端点 PDEC/远尾 core 出口；尚未排斥这些出口。
