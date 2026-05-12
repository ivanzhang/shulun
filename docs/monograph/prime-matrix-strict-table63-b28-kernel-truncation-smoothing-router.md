# Prime Matrix strict Table 6.3 b=28 核/截断/平滑口径审计证书

**状态：** `table63_b28_kernel_original_open_fk_smoothed_kernel_identified_b28_packet_next`

当前最窄点被推进了一层：旧 Dusart Table 6.3 b=28 源只给表行，不给生成核；仓库内部非平滑 Perron 核虽已自足闭合，但因预算差约 2.78e12 倍，不能作为 b=28 表生成器。可严格对接同一 psi 高尾目标的外部核已定位为 Faber-Kadiri 光滑显式公式；它给出 S^-<=psi<=S^+、显式光滑核 g 和校正版 epsilon 公式。剩余真正单点不再是找核，而是直接计算并验收 b0=28 的校正版参数包、预算、外向舍入和 hash。

```text
faber_kadiri_smoothed_kernel_convention_identified=true
internal_unsmoothed_kernel_rejected_for_b28=true
table63_b28_kernel_truncation_smoothing_convention_closed=false
replacement_external_kernel_lane_opened=true
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 数值边界

| field | value |
| --- | ---: |
| `coarse_template_gap_factor_high_tail_b28` | `2779902555195.0005` |
| `faber_kadiri_platt_b25_epsilon` | `4.8208e-5` |
| `faber_kadiri_platt_b30_epsilon` | `5.6685e-6` |
| `faber_kadiri_gourdon_b25_epsilon` | `4.8208e-5` |
| `faber_kadiri_gourdon_b30_epsilon` | `5.6646e-6` |
| `target_1_over_36260` | `0.000027578599007170435741864313292884721456150027578599` |

## 2. 外部核事实

| source | fact | meaning | effect |
| --- | --- | --- | --- |
| Dusart 2016 Math. Comp. paper | `moderate_range_points_to_faber_kadiri` | 正式版说明在较低 b 区间，Faber-Kadiri 的方法和值优于该文全局上界。 | 旧 Table 6.3 b=28 的自足替代路线应优先接 Faber-Kadiri 型平滑显式公式。 |
| Faber-Kadiri 2015 / arXiv:1310.6374 | `smooth_weight_bounds_psi` | 引入光滑权 f，并以 S^-(x)<=psi(x)<=S^+(x) 把普通 psi 误差转成光滑显式公式误差。 | 这给出与 Table 6.3 相同目标函数 psi 的核/平滑 convention。 |
| Faber-Kadiri 2015 / arXiv:1310.6374 | `kernel_g_declared` | 第 3.1 节给出优化核 g(x)=1-((2m+1)!/(m!)^2) int_0^x t^m(1-t)^m dt。 | 外部平滑核本身已声明；它不是仓库内部的非平滑 Perron 核。 |
| Faber-Kadiri 2015 / corrigendum 2017 | `corrected_budget_formula_required` | corrigendum 修正 B5 定义并重列计算表；必须使用校正版 epsilon 公式和表。 | 仅识别核不够，b0=28 还需校正版参数包、预算和外向舍入。 |
| Faber-Kadiri table rows | `bracketing_rows_not_enough` | 公开表有 b0=25 与 b0=30 行；b0=25 的 epsilon 太弱，b0=30 不能覆盖 x>=e^28。 | 不能靠表行单调性偷换，必须直接计算 b0=28 参数包。 |

## 3. 核口径矩阵

| field | internal unsmoothed | external FK | status |
| --- | --- | --- | --- |
| `base_function` | psi_0 半权端点，已由上一证书转为普通 psi 并登记端点税 | 普通 psi 由 S^- 与 S^+ 光滑上下包络夹住 | function target compatible after endpoint tax |
| `kernel` | 非平滑 Perron 竖线核，finite-T 常数 C=12128 | beta 型光滑核 g 及 Mellin transform F | kernel convention differs |
| `truncation` | 固定 T 与 contour shift 预算，后接粗 zero-sum 包 | 按 H, T0, T1, sigma0 分割零点块，使用 B_i 预算函数 | truncation variables differ |
| `budget_pressure` | 现有粗 contour 距 2.224E-5 表值约 2.78e12 倍 | 有校正版 epsilon 公式，但 b0=28 未直接列成表行 | internal rejected, external needs b28 packet |
| `output` | 已自洽但不能生成 Table 6.3 b=28 | 需给出 b0=28 的 m, delta, sigma0, T1, H/R0, corrected B_i 与 hash | next exact hardpoint |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只处理假设反例链可调用的 psi 高尾输入，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `KernelConventionGateActive` | `true` | `true` | 上一证书已关闭 psi/psi0 端点税，并把下一最窄点压到 b=28 的核/截断/平滑口径。 | Table63B28KernelTruncationAndSmoothingConventionLedger |
| `Table63B28PsiVsPsi0EndpointConventionLedger` | `true` | `true` | 函数目标已经对齐到普通 psi；端点半权税可显式扣除。 | endpoint tax registered |
| `OriginalDusartB28AlgorithmArtifactMissing` | `true` | `true` | 旧 arXiv/Dusart Table 6.3 只给出表行与使用点，没有给出 b=28 表生成核、截断高度、平滑规则或 hash。 | DusartEpsSubmittedTableAlgorithmArtifactLedger |
| `InternalUnsmoothedPerronKernelAvailable` | `true` | `true` | 仓库内部非平滑 Perron 核和 finite-T 常数 C=12128 已自足闭合。 | UnsmoothedChebyshevPerronExplicitFormulaConstantSelfContainedClosedC12128 |
| `InternalUnsmoothedKernelRejectedForB28` | `true` | `true` | 现有内部粗核自洽但不能生成 b=28 表值，压力差约 2779902555195.0005 倍，且不是 Dusart/FK 表算法口径。 | cannot be used as Table63 b=28 generator |
| `FaberKadiriSmoothedExplicitFormulaKernelConventionLedger` | `true` | `true` | 外部可对接的核/平滑 convention 已定位为 Faber-Kadiri 光滑显式公式：S^-<=psi<=S^+，核 g 显式给出。 | external smoothed convention identified |
| `PublishedB25B30RowsDoNotCloseB28` | `true` | `true` | Faber-Kadiri 表中 b0=25 的界太弱，b0=30 又只覆盖 x>=e^30；不能直接替代 x>=e^28。 | FaberKadiriCorrectedB28ParameterPacketAndBudgetLedger |
| `Table63B28KernelTruncationAndSmoothingConventionLedger` | `false` | `false` | 原始 Table 6.3 b=28 的核口径仍未自足生成；但可替代的外部平滑核已定位，剩余精确压成 b0=28 校正版参数包与预算。 | (DusartEpsSubmittedTableAlgorithmArtifactLedger) OR (FaberKadiriSmoothedExplicitFormulaKernelConventionLedger AND FaberKadiriCorrectedB28ParameterPacketAndBudgetLedger AND FaberKadiriB28DirectedRoundingAndComputationHashLedger) |
| `IndependentRegenerationStillOpen` | `false` | `false` | 核/平滑 convention 的外部定位不等于表值重建；仍需有限零点块、尾项、预算、舍入和 hash 同步。 | Table63B28FiniteRHHeightEndpointAndZeroBlockLedger AND Table63B28ZeroFreeTailConstantsAndStartHeightLedger AND Table63B28PsiEpsilonBudgetPartitionLedger AND Table63B28DirectedUpperRoundingAndIntervalPropagationLedger AND Table63B28ReproducibleComputationHashLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步仍只推进 psi 高尾输入，尚未产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 5. 下一最窄点

```text
FaberKadiriCorrectedB28ParameterPacketAndBudgetLedger
```

