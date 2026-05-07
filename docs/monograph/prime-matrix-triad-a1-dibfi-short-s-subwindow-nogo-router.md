# Triad-A1 DI/BFI short-S subwindow no-go 路由器

**状态：** `short_s_subwindow_decomposition_rejected_full_s_atom_open`

短 S 子窗口分解被排除：小区间宽度不能替代 Maynard-S 的实际量级；当前尺度侧剩余单点化为 `NewFullSDispersionAtom`。

## 1. 结构律

Short interval width does not reduce the Maynard S parameter. In W4, S_May is tied to the magnitude of z=s1*s2 via Z≈S_May^2. A subinterval inside s≈X^(1/2) still has s magnitude X^(1/2), so it still forces S_May≈X^(1/2). A true S_May<=X^(3/10) selection leaves the current full-S dyadic block. Thus the remaining scale route requires a new full-S dispersion atom.

```text
previous terminal:
  ShortSSubwindowOrNewFullSDispersionAtom;

new terminal:
  NewFullSDispersionAtom;
```

## 2. 汇总

- `short_s_subwindow_closed=false`。
- `closed_subwindow_gates=['PriorShortSOrFullSAtomFrontierAvailable', 'MaynardSIsMagnitudeNotIntervalWidth', 'CurrentBlockIsFullCommonS', 'ShortSWidthDoesNotReduceMaynardMagnitude', 'SmallMagnitudeSSelectionLosesFullSBlock', 'ShortSSubwindowDecompositionRejected']`。
- `open_subwindow_gates=['NewFullSDispersionAtom']`。
- `terminal_gap_after_router=NewFullSDispersionAtom`。

## 3. 子窗口账本表

| gate | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- |
| `PriorShortSOrFullSAtomFrontierAvailable` | `true` | 上游已排除完整 S 窗口下的 Maynard-S 压缩，并留下短 S 子窗口/full-S 原子二选一。 | none at prior-frontier level | `ShortSWidthDoesNotReduceMaynardMagnitude` |
| `MaynardSIsMagnitudeNotIntervalWidth` | `true` | W4 使用 z=s1*s2 且 Z≈S_May^2；S_May 控制乘积变量的量级，不是局部区间宽度。 | none at notation level | `ShortSWidthDoesNotReduceMaynardMagnitude` |
| `CurrentBlockIsFullCommonS` | `true` | 当前 KE-13/common table 的逆元变量仍在 full-S dyadic 块 S_common≈X^(1/2)。 | none unless the target object is changed to a genuinely smaller dyadic S block | `ShortSWidthDoesNotReduceMaynardMagnitude` |
| `ShortSWidthDoesNotReduceMaynardMagnitude` | `true` | 把 s≈X^(1/2) 的窗口切成短宽度区间后，s 的量级仍是 X^(1/2)，故 z=s1*s2≈X。 | 不能用区间宽度 L<=X^(3/10) 替代 S_May。 | `ShortSSubwindowDecompositionRejected` |
| `SmallMagnitudeSSelectionLosesFullSBlock` | `true` | 若真实要求 s1,s2<=X^(3/10)，则已经离开当前 S_common≈X^(1/2) dyadic 块。 | 必须另证目标质量不在 full-S 块；当前合同没有该事实。 | `ShortSSubwindowDecompositionRejected` |
| `ShortSSubwindowDecompositionRejected` | `true` | 短宽度分解不能降低 Maynard-S 量级；真实短量级选择又会丢失当前 full-S dyadic 目标块。 | 当前资料下短 S 子窗口出口不可用。 | `NewFullSDispersionAtom` |
| `NewFullSDispersionAtom` | `false` | 仍需新增并证明适配 S_common≈X^(1/2)、z≈X 的 full-S 原始 dispersion 原子。 | 当前最新终端硬点。 | `NewFullSDispersionAtom` |

## 4. 当前结论

当前尺度侧剩余为：

```text
NewFullSDispersionAtom:
  prove a full-S original dispersion atom for S_common≈X^(1/2), z≈X.
```

这一步排除的是短 S 子窗口退路，不是 full-S 原子本身。
