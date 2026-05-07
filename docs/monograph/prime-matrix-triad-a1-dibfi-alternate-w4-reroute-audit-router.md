# Triad-A1 DI/BFI alternate W4 reroute audit 路由器

**状态：** `alternate_w4_reroute_rejected_maynard_s_compression_open`

替代 W4 对象路由在当前合同下被排除；非 AP generic WFD 的尺度侧剩余单点化为 `MaynardSCompressionMap`。

## 1. 结构律

No registered closed alternate W4 object route is available for the non-AP generic WFD branch. Direct BFI is AP-source only, HLCWindowedKLS is clean-HLC only, and the non-AP fallback returns to the same KE-13/DI-Maynard chain. The remaining scale hard point is MaynardSCompressionMap.

```text
previous terminal:
  MaynardSCompressionMapOrAlternateW4Rerouting;

new terminal:
  MaynardSCompressionMap;
```

## 2. 汇总

- `alternate_w4_reroute_closed=false`。
- `closed_reroute_gates=['PriorSCompressionBarrierAvailable', 'DirectBFIAtomScopeAPOnly', 'HLCWindowedKLSAtomScopeCleanOnly', 'NonAPFallbackReturnsToSameKE13Route', 'NoRegisteredClosedAlternateW4Route']`。
- `open_reroute_gates=['MaynardSCompressionMap']`。
- `terminal_gap_after_router=MaynardSCompressionMap`。

## 3. 替代路由账本表

| gate | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- |
| `PriorSCompressionBarrierAvailable` | `true` | 上游已把朴素 S_common=S_May 同一化排除，并留下压缩/替代二选一。 | none at prior-barrier level | `NoRegisteredClosedAlternateW4Route` |
| `DirectBFIAtomScopeAPOnly` | `true` | 直接 BFI 原子只在 AP-source 分支闭合；非 AP generic WFD 不能静默升级。 | 若要用直接 BFI，必须重新证明源头 AP residual identity。 | `NoRegisteredClosedAlternateW4Route` |
| `HLCWindowedKLSAtomScopeCleanOnly` | `true` | HLCWindowedKLSAtom 只覆盖 clean HLC 分支，不替代 generic WFD 共同变量表。 | none for current non-AP generic WFD route | `NoRegisteredClosedAlternateW4Route` |
| `NonAPFallbackReturnsToSameKE13Route` | `true` | 非 AP fallback 回到无投影 KE-13/量化窗口代入；这正是当前 Maynard-W4 链条。 | 不是独立闭合出口。 | `NoRegisteredClosedAlternateW4Route` |
| `NoRegisteredClosedAlternateW4Route` | `true` | 当前已登记原子中没有可绕开 Maynard-S 压缩并闭合非 AP generic WFD 的替代路由。 | 只有新增外部原始 dispersion 原子才会重开该出口。 | `MaynardSCompressionMap` |
| `MaynardSCompressionMap` | `false` | 仍需从 s1,s2,h,completion 结构中构造 S_May<=X^(3/10-o(1))。 | 当前最终尺度硬点。 | `MaynardSCompressionMap` |

## 4. 当前结论

当前尺度侧最终硬点为：

```text
MaynardSCompressionMap:
  construct S_May from s1,s2,h,completion;
  prove S_May <= X^(3/10-o(1)).
```

这一步排除的是已登记替代出口；它没有证明 S 压缩映射本身。
