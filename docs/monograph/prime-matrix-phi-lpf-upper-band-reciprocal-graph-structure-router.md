# Prime Matrix Phi-LPF upper-band reciprocal graph structure 证书

**状态：** `upper_band_reciprocal_shadow_graph_reduced_to_ordered_degree_two_forest`

本层继续压缩 upper-band reciprocal prime-pair shadow。把每个 shadow 对 `(q,m)` 看成
二部图的一条边，其中 `q in (P/2,P)`，`m in [q,2P)` 且 `qm` 落入同一行。

## 1. 结构证明读法

固定 `q` 时，`m` 的窗口长度小于 `P/q<2`，所以 `q` 侧度数至多二。
固定 `m` 时同理，`q` 的窗口长度小于 `P/m<=P/q<2`，所以 `m` 侧度数也至多二。

若存在交叉边 `q1<mapped to m1` 与 `q2<mapped to m2`，其中 `q1<q2` 且 `m1<m2`，则

```text
q2*m2-q1*m1 >= (q2-q1)*m2 + q1*(m2-m1) > P,
```

这与二者同时落在长度 `P` 的同一行矛盾。因此 shadow 图有序无交叉；结合两侧度数至多二，
它不能形成循环反馈。更直接地，若存在环，取环中最小的 `q0`，它在环上连接两个
不同的 `m`，设为 `m_a<m_b`。任意其他 `q>q0` 若连接到 `m>m_a`，就与边
`(q0,m_a)` 交叉；于是 `m_b` 不可能再连接到第二个 `q`，矛盾。故 shadow 图只能是森林型边集。

## 2. 有限审计

```text
max_prime=1009
prime_base_count=165
all_upper_rows_have_forest_shadow_graph=true
graph_structure_failure_count=0
finite_evidence_not_used_as_global_proof=true
```

最大 edge 行读数：

```text
P=953, k=943, edges=24, vertices=48, components=24, direct_primes=56
```

## 3. 有限样本表

| P | k | edges | vertices | components | max deg q | max deg m | forest | direct primes |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| 11 | 2 | 0 | 0 | 0 | 0 | 0 | `true` | 3 |
| 11 | 5 | 0 | 0 | 0 | 0 | 0 | `true` | 2 |
| 11 | 8 | 1 | 2 | 1 | 1 | 1 | `true` | 2 |
| 11 | 9 | 0 | 0 | 0 | 0 | 0 | `true` | 4 |
| 11 | 10 | 1 | 2 | 1 | 1 | 1 | `true` | 1 |
| 101 | 25 | 0 | 0 | 0 | 0 | 0 | `true` | 12 |
| 101 | 50 | 2 | 4 | 2 | 1 | 1 | `true` | 11 |
| 101 | 66 | 2 | 4 | 2 | 1 | 1 | `true` | 12 |
| 101 | 75 | 2 | 4 | 2 | 1 | 1 | `true` | 12 |
| 101 | 100 | 4 | 8 | 4 | 1 | 1 | `true` | 12 |
| 257 | 64 | 0 | 0 | 0 | 0 | 0 | `true` | 27 |
| 257 | 128 | 4 | 8 | 4 | 1 | 1 | `true` | 28 |
| 257 | 152 | 4 | 8 | 4 | 1 | 1 | `true` | 27 |
| 257 | 192 | 2 | 4 | 2 | 1 | 1 | `true` | 24 |
| 257 | 256 | 6 | 12 | 6 | 1 | 1 | `true` | 23 |
| 1009 | 252 | 0 | 0 | 0 | 0 | 0 | `true` | 85 |
| 1009 | 504 | 9 | 18 | 9 | 1 | 1 | `true` | 70 |
| 1009 | 523 | 9 | 18 | 9 | 1 | 1 | `true` | 71 |
| 1009 | 756 | 9 | 18 | 9 | 1 | 1 | `true` | 79 |
| 1009 | 1008 | 19 | 38 | 19 | 1 | 1 | `true` | 70 |

## 4. 大尺度抽样

```text
sample_seeds=[100000, 300000]
sample_count=10
all_sampled_graphs_are_forests=true
all_sampled_degrees_at_most_two=true
large_samples_are_evidence_not_global_proof=true
```

| P | k | edges | vertices | components | max deg q | max deg m | forest | direct primes |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| 100003 | 25000 | 0 | 0 | 0 | 0 | 0 | `true` |  |
| 100003 | 33406 | 119 | 238 | 119 | 1 | 1 | `true` |  |
| 100003 | 50001 | 284 | 568 | 284 | 1 | 1 | `true` |  |
| 100003 | 75002 | 445 | 890 | 445 | 1 | 1 | `true` |  |
| 100003 | 100002 | 515 | 1030 | 515 | 1 | 1 | `true` |  |
| 300007 | 75001 | 0 | 0 | 0 | 0 | 0 | `true` |  |
| 300007 | 90261 | 200 | 400 | 200 | 1 | 1 | `true` |  |
| 300007 | 150003 | 716 | 1432 | 716 | 1 | 1 | `true` |  |
| 300007 | 225005 | 1061 | 2122 | 1061 | 1 | 1 | `true` |  |
| 300007 | 300006 | 1272 | 2544 | 1272 | 1 | 1 | `true` |  |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ReciprocalShadowGraphDegreeTwoClosed | `true` | `true` | 固定 q 和固定 m 的 reciprocal 窗口长度都小于 2，因此二部图两侧度数均不超过 2。 | exact graph structure |
| OrderedNoncrossingShadowEdgesClosed | `true` | `true` | 若 q1<q2 且 m1<m2，则 q2m2-q1m1>P，不能同时落入同一长度 P 行。 | monotone reciprocal ordering |
| UpperBandShadowGraphForestClosed | `true` | `true` | 有序无交叉加度数二排除 reciprocal shadow 的循环反馈；有限审计与结构证明均给出森林图。 | forest shadow graph |
| FiniteSweepSupportsForestStructure | `true` | `true` | 有限审计确认所有 upper rows 的 graph 读数正常，但不作为全局正性证明。 | finite audit only |
| ForestSaturationExcluded | `false` | `false` | 尚未证明这个森林边集不能刚好覆盖全部 half-rough survivors。 | UpperBandForestShadowSaturationExclusionOrPDEC |
| UnifiedPositiveCoreProved | `false` | `false` | 本层只排除 upper-band shadow 的循环反馈，不证明三目标命题。 | HalfPrimorialSpecialPhaseAvoidsLongCoveredBlockOrPDEC AND UpperBandForestShadowSaturationExclusionOrPDEC |

## 6. 结论

upper-band two-prime shadow 的 reciprocal prime-pair 图是有序、无交叉、两侧度数至多二的森林。因此反例不能依靠循环反馈放大 shadow；若仍失败，只能是这片森林边集真实饱和全部 half-rough survivor，或触发显式 PDEC。

当前 upper-band 的下一窄口为：

```text
UpperBandForestShadowSaturationExclusionOrPDEC
```

本层仍不证明 `UnifiedPositiveCore`、行/列命题或三目标命题；它只排除了 upper-band
shadow 的循环反馈形态。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-upper-band-two-prime-shadow-excess-router.json` | `55556f72402db91637fa98a903e4ee80c3fcb0ddabc81e334898523313d06d3f` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-half-rough-shadow-band-split-router.json` | `9db4d90a17cdd1c8e1730e6b8d5d86caa454ea43951ddc4c3ce713a09acf373f` |
| `docs/monograph/prime-matrix-phi-lpf-shadow-free-half-primorial-phase-router.json` | `6f2af1f27399871c3838a8a760f625bd16d18ac1e02e3740bdb2f903d3c27011` |
