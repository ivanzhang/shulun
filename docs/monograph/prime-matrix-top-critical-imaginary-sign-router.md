# Prime Matrix 顶边临界半段虚部负号路由器

**状态：** `top_critical_center_values_reduced_to_imaginary_negative_replay_open`

中心值 replay 的目标从复模下界进一步压缩为单边虚部负号表：只需证明 1024 个中心点 Im zeta(c_j+14i)<=-1/40。已闭合导数界保证整段虚部仍严格为负，因此顶边临界半段非零。当前仍缺这 1024 个有理区间中心虚部证书。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
top_critical_center_value_reduced_to_imaginary_sign=true
top_critical_segment_self_contained_closed=false
lowheight_rectangle_count_self_contained_closed=false
row_column_self_contained_closed=false
```

## 1. 虚部侦察

| item | value |
| --- | ---: |
| height | `14.0` |
| mesh denominator | `2048` |
| cell count | `1024` |
| imag floor contract | `-0.025000000000` |
| audit max center imag | `-0.030701862705` |
| audit max center sigma | `0.999755859375` |
| audit min center imag | `-0.103208220630` |
| audit margin below floor | `0.005701862705` |
| derivative half-cell loss | `0.005360689033` |

## 2. 证明合同

1. 对每个中心 c_j=1/2+(j+1/2)/2048，用 EM replay 证明 Im zeta(c_j+14i)<=-1/40。
2. 已闭合导数界给每个半小段的虚部漂移至多 0.005360689033。
3. 若中心虚部 <=-1/40，则整段虚部 <= -0.019639310967<0。
4. 因此 zeta 在顶边临界半段无零；xi 的显式因子非零，所以 xi 也无零。
5. 这比 |zeta|>=0.1 的复模证书更窄，只需证明一个实区间上界。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ImaginarySignGateActive` | `true` | `true` | 中心值复模表可被更窄的中心虚部负号表替代。 | TopCriticalSegmentCenterValueEMReplayLedgerN32P8Mesh2048Floor0p1 |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只处理低高度解析证书，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `DerivativeAndRoundingInputsImported` | `true` | `true` | 导数传播和 EM replay 舍入纪律均已闭合。 | ready for real one-sided center table. |
| `FloatAuditShowsImaginaryGap` | `true` | `false` | 侦察最大中心虚部≈-0.030701862705，低于 -1/40=-0.025000000000。 | 只能确定参数，不作为自足证明。 |
| `ImaginaryPropagationLemmaClosed` | `true` | `true` | 中心虚部 <=-1/40 且半段漂移 <=0.005360689033 推出整段虚部仍 <0。 | TopCriticalSegmentXiNonzeroClosedByImagNegativeT14HalfToOne |
| `ExactCenterImaginaryReplayStillMissing` | `false` | `false` | 还需 1024 个中心点的有理区间 EM replay，逐点证明 Im zeta<=-1/40。 | TopCriticalSegmentCenterImagNegativeEMReplayLedgerN32P8Mesh2048FloorMinus1Over40 |
| `TopCriticalSegmentCenterValueEMReplayLedgerN32P8Mesh2048Floor0p1` | `false` | `false` | 复模中心值表已压缩成单边虚部负号表，但严格自足尚未闭合。 | TopCriticalSegmentCenterImagNegativeEMReplayLedgerN32P8Mesh2048FloorMinus1Over40 |

## 4. 下一步

严格自足唯一顶边剩余：`TopCriticalSegmentCenterImagNegativeEMReplayLedgerN32P8Mesh2048FloorMinus1Over40`。
顶边完成后仍需：`XiBoundaryWindingNumberZeroIntervalCertificate0To14`。

判定：顶边非零已变成 1024 个一维实不等式。
