# Prime Matrix 顶边临界半段 Euler-Maclaurin replay 路由器

**状态：** `top_critical_segment_reduced_to_em_replay_ledger_open`

顶边临界半段已压成一个具体有限 replay 账本：1024 个 dyadic 小段、Euler-Maclaurin N=32,p=8 中心值证书与 |zeta'|<=64 导数证书。浮点侦察显示最小 |zeta| 约 0.10547，导数约 0.77566，合同余量很宽；但严格自足仍需把这些值写成有理区间 replay。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
top_critical_segment_compressed_to_em_replay=true
top_critical_segment_self_contained_closed=false
lowheight_rectangle_count_self_contained_closed=false
row_column_self_contained_closed=false
```

## 1. 侦察参数

| item | value |
| --- | ---: |
| height | `14.0` |
| sigma range | `['1/2', '1']` |
| mesh denominator | `2048` |
| cell count | `1024` |
| EM N | `32` |
| EM p | `8` |
| center floor contract | `0.1` |
| derivative bound contract | `64.0` |
| propagation loss | `0.015625000000` |
| certified margin if replay passes | `0.084375000000` |
| audit min center abs | `0.105472687242` |
| audit min center sigma | `0.507080078125` |
| audit max derivative abs | `0.775507226486` |
| audit derivative slack factor | `82.526633` |
| audit max EM remainder bound | `3.063668e-19` |
| audit max eta/EM cross error | `2.549937e-15` |

## 2. 有限证明合同

1. 把 [1/2,1] 分成 1024 个 dyadic 小段，中心 c_j=1/2+(j+1/2)/2048。
2. 对每个中心 s_j=c_j+14i，用 Euler-Maclaurin 公式 N=32, p=8 给 zeta(s_j) 的复区间盒。
3. 每个中心盒必须证明 |zeta(s_j)|>=1/10；xi 的其他因子在顶边上非零，所以 zeta 非零等价于 xi 非零。
4. 同时用同一 Euler-Maclaurin replay 或 Cauchy 盒证明整段水平导数 |d zeta/d sigma|<=64。
5. 任意点离中心距离至多 1/4096，因此 |zeta(s)|>=1/10-64/4096=0.084375>0。
6. 所有中心值、导数界、余项界与父 trace hash 进入 dyadic complex interval replay 账本。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `TopCriticalSegmentGateActive` | `true` | `true` | 上一层已把顶边自足剩余压缩到 Im(s)=14, 1/2<=Re(s)<=1。 | TopCriticalSegmentXiBoxCoverLedgerT14SigmaHalfToOne |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只处理低高度解析证书，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `SymmetryAndEulerProductCompressionImported` | `true` | `true` | 顶边左半和右外段已关闭，只需临界半段。 | critical half segment only. |
| `FloatReconnaissanceSupportsWideMargin` | `true` | `false` | 侦察最小 \|zeta\|≈0.105472687242，最大水平导数≈0.775507226486，远优于 0.1/64 合同。 | 不能作为自足证明，只用于确定可行证书参数。 |
| `CenterDerivativePropagationLemmaClosed` | `true` | `true` | 若中心值 >=1/10 且导数 <=64，则每段内 \|zeta\|>=0.084375，因而 xi 非零。 | finite replay remains. |
| `ExactDyadicEulerMaclaurinReplayStillMissing` | `false` | `false` | 还需把 1024 个中心值和导数界用有理区间 Euler-Maclaurin replay 实际登记。 | TopCriticalSegmentEulerMaclaurinDyadicReplayLedgerN32P8Mesh2048 AND DyadicComplexIntervalEulerMaclaurinReplayRoundingLedger |
| `TopCriticalSegmentXiBoxCoverLedgerT14SigmaHalfToOne` | `false` | `false` | 旧顶边临界半段盒账本已压缩为有限 Euler-Maclaurin replay，但严格自足尚未闭合。 | TopCriticalSegmentEulerMaclaurinDyadicReplayLedgerN32P8Mesh2048 |

## 4. 下一步

严格自足最窄点：`TopCriticalSegmentEulerMaclaurinDyadicReplayLedgerN32P8Mesh2048`。
并行实现门：`DyadicComplexIntervalEulerMaclaurinReplayRoundingLedger`。
之后仍需：`XiBoundaryWindingNumberZeroIntervalCertificate0To14`。

判定：已经不是开放解析问题，而是一个具体有限有理区间 replay 账本。
