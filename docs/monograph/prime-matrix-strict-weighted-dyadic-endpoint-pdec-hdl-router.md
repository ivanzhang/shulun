# Prime Matrix strict 加权 dyadic endpoint PDEC 到 HDL/CoreLoad 路由器

**状态：** `weighted_dyadic_endpoint_pdec_reduced_to_hdl_coreload_cofactor_exclusion_open`

当前 alpha-prefix 链的 dyadic 端点缺陷带有 Rosser-Iwaniec lower-weight 权重，不能直接套用旧的 Möbius HDL。本文把 HDL-9/HDL-10 升级为加权形式：若某个 dyadic 块有 E_I<=-tau，则要么正权端点命中亏损，要么负权端点命中过剩。若该块在 d>P-1 的高区间，端点命中是单命中 CRT 事件，并精确等价于逐列低素核的加权 coreload 异常；过剩分支还可反演到 m<P+2 的低互补因子带。本步关闭权重口径和结构接桥，但尚未排斥这些加权异常。

```text
weighted_hdl_bridge_closed=true
high_block_single_hit_coreload_closed=true
weighted_cofactor_band_projection_closed=true
dyadic_endpoint_pdec_excluded=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 加权 HDL 口径

对 dyadic 块 `I`，当前端点误差是

```text
E_I(x)=sum_{d in I} lambda_d^- epsilon_d(x),
epsilon_d(x)=A_d(x)-(P-1)/d.
```

把权重拆成正负部分后，若 `E_I<=-tau`，则必有

```text
A_I^+ <= H R_I^+ - tau/2
或
A_I^- >= H R_I^- + tau/2.
```

这就是 HDL 端点亏损/过剩的 lower-weight 加权版本。

## 2. 闭合接桥

| name | formula | status | meaning |
| --- | --- | --- | --- |
| `weighted_endpoint_block` | E_I(x)=sum_{d in I} lambda_d^- epsilon_d(x), epsilon_d=A_d-(P-1)/d. | `closed_definition` | 当前链使用 lower-weight，而不是 Möbius 裸权重。 |
| `positive_negative_weight_split` | lambda_d^{low}=w_d^+ - w_d^-, with w_d^+,w_d^- >=0; E_I=(A_I^+-H R_I^+) - (A_I^--H R_I^-). | `closed_identity` | 任何负缺陷都可拆成正权端点亏损或负权端点过剩。 |
| `weighted_hdl_dichotomy` | If E_I<=-tau, then A_I^+<=H R_I^+-tau/2 or A_I^->=H R_I^-+tau/2. | `closed_implication` | 这是 HDL-9/HDL-10 的 lower-weight 加权版本。 |
| `high_block_single_hit` | If d>H=P-1, then A_d(x)=1_{rho_d(x)<=H}. | `closed_imported` | 高 dyadic 块中每个模数最多命中一次，端点缺陷变成单命中偏斜。 |
| `weighted_coreload_identity` | A_I^sigma=sum_{k<=H} sum_{d in I,d\|G_z(k)} w_d^sigma. | `closed_identity` | 加权端点命中偏斜等价于逐列低素 squarefree 核的加权负载异常。 |
| `weighted_cofactor_inversion` | For d>H, d\|xP+c and m=(xP+c)/d imply m<P+2; weighted load projects to low cofactor band. | `closed_implication` | 奇/负权过剩若不集中为列锚，就必须在低互补因子带分布。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 仍在早期零行反例链中处理 dyadic 负端点缺陷。 | 保持 row_column_unconditional_closed=false。 |
| `WeightedHDLBridgeClosed` | `true` | `true` | Möbius HDL 已升级为 lower-weight 加权 HDL，避免权重口径偷换。 | WeightedDyadicEndpointHDLCoreLoadExclusion |
| `HighBlockSingleHitCoreLoadClosed` | `true` | `true` | 高块缺陷可精确改写为加权逐列 coreload 异常。 | WeightedPositiveEndpointHitDeficitPDEC OR WeightedNegativeEndpointHitSurplusCoreLoad |
| `WeightedCofactorBandProjectionClosed` | `true` | `true` | 过剩分支投影到 m<P+2 的互补因子带；单 m 容量仍受一个剩余类限制。 | WeightedCofactorLoadCapacityOrColumnCRT |
| `DyadicEndpointPDECExcludedCurrentCorpus` | `false` | `false` | 加权 HDL/CoreLoad 接桥闭合，但正权亏损、负权过剩和低/中块 PDEC 尚未排斥。 | LowOrMiddleDyadicEndpointPDECExclusion AND WeightedPositiveEndpointHitDeficitPDEC AND WeightedNegativeEndpointHitSurplusCoreLoad |
| `RowColumnClosed` | `false` | `false` | 当前只把 dyadic PDEC 压到加权 HDL/CoreLoad/互补因子出口。 | AlphaLowerWeightMainGapPositiveAgainstHighLabelCapacity AND LowOrMiddleDyadicEndpointPDECExclusion AND WeightedDyadicEndpointHDLCoreLoadExclusion AND LowerWeightFarTailCoreOrSAEExclusion |

## 4. 最新最窄输入

```text
WeightedPositiveEndpointHitDeficitPDEC
```

并行保留：

```text
WeightedNegativeEndpointHitSurplusCoreLoad AND WeightedCofactorLoadCapacityOrColumnCRT AND LowOrMiddleDyadicEndpointPDECExclusion AND LowerWeightFarTailCoreOrSAEExclusion AND AlphaLowerWeightMainGapPositiveAgainstHighLabelCapacity
```

审稿边界：本步闭合的是 weighted endpoint PDEC 到 HDL/CoreLoad/cofactor 的结构接桥；没有证明这些加权异常不可能。
