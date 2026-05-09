# Prime Matrix 低高度 xi 矩形零点计数压缩路由器

**状态：** `lowheight_two_zero_atoms_compressed_to_rectangle_count_open`

低高度零点包可再压缩：不必分别证明临界线无零和离线 Turing 计数。一个自足的 xi 矩形零点计数为 0 证书即可同时关闭二者。这一步只完成逻辑压缩；真正证明仍需 xi 区间求值引擎、边界非零证书和 winding=0 证书。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
compression_closed=true
strict_rectangle_count_closed=false
row_column_self_contained_closed=false
```

## 1. 压缩替换

```text
(CriticalLineNoZeroOn0To14FiniteLedger AND CriticalStripNoOffLineZeroBelow14TuringLedger) => LowHeightXiRectangleZeroCountZero0To14Ledger
```

新的单原子：

```text
LowHeightXiRectangleZeroCountZero0To14Ledger
```

必要证书包：

```text
SelfContainedXiIntervalEvaluationEngine0To14 AND XiBoundaryIntervalNonzeroCertificate0To14 AND XiBoundaryWindingNumberZeroIntervalCertificate0To14
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `LowHeightSplitActive` | `true` | `true` | 当前低高度包确实把自足剩余拆成临界线有限账本与离线 Turing 账本。 | CriticalLineNoZeroOn0To14FiniteLedger AND CriticalStripNoOffLineZeroBelow14TuringLedger |
| `RectangleCountDominatesBothAtoms` | `true` | `true` | 若 xi 在覆盖 0<Im s<=14 的低高度矩形中零点计数为 0，则临界线和离线区域都没有零点，两个旧原子同时关闭。 | LowHeightXiRectangleZeroCountZero0To14Ledger |
| `BoundaryNonzeroCertificateRequired` | `false` | `false` | argument principle 需要证明矩形边界上 xi 不为 0，避免 winding 数未定义。 | XiBoundaryIntervalNonzeroCertificate0To14 |
| `WindingNumberZeroCertificateRequired` | `false` | `false` | 需要用区间算术证明 xi(boundary) 曲线绕原点次数为 0，而不是只做浮点采样。 | XiBoundaryWindingNumberZeroIntervalCertificate0To14 |
| `SelfContainedIntervalEngineRequired` | `false` | `false` | 必须内联 xi、Gamma、zeta 的区间求值与余项界，不能依赖外部零点表。 | SelfContainedXiIntervalEvaluationEngine0To14 |

## 3. 下一步

下一主攻单原子：`LowHeightXiRectangleZeroCountZero0To14Ledger`。
先补 `{SelfContainedXiIntervalEvaluationEngine0To14}`，再补 `{XiBoundaryIntervalNonzeroCertificate0To14}` 与 `{XiBoundaryWindingNumberZeroIntervalCertificate0To14}`。

判定：这是严格自足路线的进一步压缩，不是外部零点表接受，也不是最终闭合。
