# Prime Matrix square-phase RFP-Upper 直接下钻路由器

**状态：** `rfp_upper_reduced_to_area_carry_selberg_reciprocal_phase_or_pdec_open`

`RFP-Upper` 已下钻为三块具体任务：双曲窄带面积/进位计数、端点倒数相位 CarryDiscrepancy、二维 Selberg 上筛常数。三条倒数地板素-素曲线的几何表示已闭合；若 `B(P)` 超过 `1.50P/log^2P`，失败不能是无名现象，只能表现为面积进位过密、端点倒数相位低频集中，或尾锚素对异常峰值，并进入 PDEC/SAE。

```text
three_curve_prime_pair_reduction_closed=true
hyperbolic_strip_embedding_closed=true
rfp_area_carry_bound_proved=false
carry_discrepancy_endpoint_reciprocal_phase_proved=false
rfp_selberg_constant_proved=false
row_column_unconditional_closed=false
```

## 1. 公式

| name | formula | status |
| --- | --- | --- |
| `prime_pair_cover` | `B(P)=#{(ell,m): y<ell<P<m, ell,m prime, P^2<ell*m<P^2+P}` | `closed_definition` |
| `three_curves` | `m=floor(P^2/ell)+s, s in {1,2,3}` | `closed_reduction` |
| `hyperbolic_strip` | `R_P={(a,b): y<a<P, P<b, P^2<ab<P^2+P}` | `closed_embedding` |
| `rfp_target` | `B(P)<=1.50 P/log^2 P` | `open_upper_bound` |
| `area_target` | `X(P)=\|R_P\|<=1.02P for P>=2003` | `open_tail_or_pdec` |
| `carry_discrepancy_target` | `D(P)<=1.98 sqrt(P) for P>=10007` | `open_endpoint_reciprocal_phase` |

## 2. 阻塞与路由

| obstruction | detail | route |
| --- | --- | --- |
| `two-dimensional sieve constant` | 需要二维 Selberg/Brun 权常数加边界误差压到 1.50。 | `RFP-SelbergConstantLedger` |
| `hyperbolic floor area` | 窄带面积 X(P) 的 1.02P 尾段界等价于进位计数控制。 | `RFP-AreaCarryBound` |
| `carry discrepancy` | 进位偏差 D(P) 是端点倒数相位低频和；过大即 HyperbolicDisc/PDEC。 | `CarryDiscrepancyEndpointReciprocalPhaseBound` |
| `tail prime-pair spike` | 若三曲线素-素点超过二维筛预算，必须表现为短窗素数或尾锚异常集中。 | `ReciprocalFloorPrimePairExcessTailAnchorPDECOrSAE` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `RFPTargetImportedFromDimensionGap` | `true` | `true` | 维数差闭合需要 RFP-Upper 控制一尾素-素覆盖数。 | RFP-Upper |
| `ThreeCurvePrimePairReductionClosed` | `true` | `true` | 一尾覆盖已压成三条倒数地板素-素曲线。 | RFP-SelbergConstantLedger |
| `HyperbolicStripEmbeddingClosed` | `true` | `true` | B(P) 是双曲窄带 R_P 中两个坐标同为素数的点数。 | RFP-SelbergConstantLedger |
| `RFPAreaCarryBoundProved` | `false` | `false` | P>=2003 的 X(P)<=1.02P 尚未作者侧证明；过密需路由到 HyperbolicDisc/PDEC。 | RFP-AreaCarryBound OR HyperbolicDiscFailurePDEC |
| `CarryDiscrepancyEndpointReciprocalPhaseProved` | `false` | `false` | D(P)<=1.98sqrt(P) 尚未证明；过大即端点倒数相位低频集中。 | CarryDiscrepancyEndpointReciprocalPhaseBound OR HyperbolicDiscFailurePDEC |
| `RFPSelbergConstantProved` | `false` | `false` | 二维上筛主常数、边界误差和离散误差尚未压入 1.50。 | RFP-SelbergConstantLedger OR ReciprocalFloorPrimePairExcessTailAnchorPDECOrSAE |
| `RFPUpperCurrentCorpusProved` | `false` | `false` | RFP 已精确拆分，但面积、倒数相位和 Selberg 常数未同时闭合。 | RFP-AreaCarryBound AND CarryDiscrepancyEndpointReciprocalPhaseBound AND RFP-SelbergConstantLedger |
| `SquarePhaseDimensionGapClosed` | `false` | `false` | 即便 RFP 闭合，仍需并行 LDG-Lower。 | LDG-Lower AND RFP-Upper |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 没有得到全局无条件终端矛盾。 | (LDG-Lower AND RFP-Upper) OR NonFinalTailPDECSAEBudgetAmplificationOrAlternativeContradiction |

## 4. 下一步

- 主攻 `CarryDiscrepancyEndpointReciprocalPhaseBound`：证明端点倒数相位偏差 `D(P)<=1.98sqrt(P)`，或产出 `HyperbolicDiscFailurePDEC`。
- 并行攻 `RFP-SelbergConstantLedger`：给出二维上筛常数账本，压入 `1.50`。
- 保留 `RFP-AreaCarryBound` 的面积进位边界和 `ReciprocalFloorPrimePairExcessTailAnchorPDECOrSAE` 的尾锚异常路由。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-diagonal-postsquare-carry-discrepancy-pdec-route.md` | `387ce4c609d73b447c374db4b53986a72b2655427cbc6d64c449eaee9d19f1e5` |
| `docs/monograph/prime-matrix-diagonal-postsquare-carry-reciprocal-frequency.md` | `4d6f95b7c545e525d9ae34bc3065d11c807ef752ddefdc3186b344979c7caf78` |
| `docs/monograph/prime-matrix-diagonal-postsquare-endpoint-reciprocal-osc-hard-attack.md` | `7273db44f356102efe52596633741bce672c0fd9317425fee8bf69503db3dd38` |
| `docs/monograph/prime-matrix-diagonal-postsquare-rfp-selberg-route.md` | `e94ee4bb9b45dd441f151c88b99c23ebcf60b7c618d1c293c739a9fa20eba147` |
| `docs/monograph/prime-matrix-square-phase-dimension-gap-attack-router.json` | `447849c4b4f88cb1b930e20183d7060acc4fc85ed3d46759930093af03d1b467` |
| `experiments/prime_matrix_square_phase_rfp_upper_direct_attack_router.py` | `952f25e2df74a4a47195208aba87b7855ed9a937e087d47ff8cccdfdfc14e3f8` |
