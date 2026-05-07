# Triad-A1 DI/BFI Maynard S-compression no-go 路由器

**状态：** `maynard_s_compression_map_rejected_full_s_window_open`

Maynard-S 压缩映射在完整共同 S 窗口和 W4 对象等式同时保留时被排除；剩余转为短 S 子窗口分解，或新增 full-S 原始 dispersion 原子。

## 1. 结构律

If the current WFD keeps the full common inverse window S_common≈X^(1/2) and also matches the Maynard W4 object z=s1*s2, then Z≈X and S_May≈X^(1/2). The Maynard cone with q=1/2 permits only S_May<=X^(3/10-o(1)). Therefore MaynardSCompressionMap is impossible without a genuine short-S subwindow decomposition, or else a new full-S dispersion atom.

```text
previous terminal:
  MaynardSCompressionMap;

forced scales:
  full_common_s=1/2+o(1);
  full_z=1+o(1);
  maynard_s_bound=3/10-o(1);
  maynard_z_bound=3/5-o(1);

new terminal:
  ShortSSubwindowOrNewFullSDispersionAtom;
```

## 2. 汇总

- `maynard_s_compression_map_closed=false`。
- `closed_nogo_gates=['PriorSingleMaynardSCompressionTerminalAvailable', 'FullCommonSWindowPinned', 'W4ZEqualsS1S2ObjectRequirement', 'MaynardConeForcesSmallSAndZ', 'FullCommonSProductForcesLargeZ', 'FullCommonSProductContradictsMaynardZBound']`。
- `open_nogo_gates=['ShortSSubwindowDecomposition', 'NewFullSDispersionAtom']`。
- `terminal_gap_after_router=ShortSSubwindowOrNewFullSDispersionAtom`。

## 3. No-go 账本表

| gate | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- |
| `PriorSingleMaynardSCompressionTerminalAvailable` | `true` | 上游已排除已登记替代 W4 路由，尺度侧单点化为 MaynardSCompressionMap。 | none at prior-frontier level | `FullCommonSProductForcesLargeZ` |
| `FullCommonSWindowPinned` | `true` | 共同变量表固定 KE-13 逆元窗口 s,S；当前 non-AP 账本记录 S_common≈P=X^(1/2+o(1))。 | 若要压缩，必须证明合法短子窗口分解，而非直接使用完整 S_common。 | `ShortSSubwindowDecomposition` |
| `W4ZEqualsS1S2ObjectRequirement` | `true` | DI RDN/W4 账本要求当前 WFD 对象逐项生成 z=s1*s2。 | 该对象等式尚未证明，但一旦坚持它，就固定 Z 的尺度。 | `FullCommonSProductForcesLargeZ` |
| `MaynardConeForcesSmallSAndZ` | `true` | q=1/2 时 S_May<=3/10，故 Z≈S_May^2<=3/5。 | none at cone consequence level | `FullCommonSProductContradictsMaynardZBound` |
| `FullCommonSProductForcesLargeZ` | `true` | s1,s2~X^1/2 and z=s1*s2 force Z~X^1/1 and S_May~X^1/2。 | none if full S window is preserved | `FullCommonSProductContradictsMaynardZBound` |
| `FullCommonSProductContradictsMaynardZBound` | `true` | full-S object gives Z exponent 1/1；Maynard cone allows at most 3/5。 | MaynardSCompressionMap cannot preserve the full common S window and the W4 z=s1*s2 object simultaneously. | `ShortSSubwindowOrNewFullSDispersionAtom` |
| `ShortSSubwindowDecomposition` | `false` | 需要证明 KE-13/WFD 的 s1,s2 窗口可合法切成 S_short<=X^(3/10-o(1)) 并不丢目标质量。 | 尚未建立；这是新的具体硬点。 | `ShortSSubwindowOrNewFullSDispersionAtom` |
| `NewFullSDispersionAtom` | `false` | 若不能短窗分解，必须新增适配 S_common≈X^(1/2) 的 full-S 原始 dispersion 原子。 | 当前仓库没有该已登记闭合原子。 | `ShortSSubwindowOrNewFullSDispersionAtom` |

## 4. 当前结论

当前尺度侧剩余为：

```text
ShortSSubwindowOrNewFullSDispersionAtom:
  ShortSSubwindowDecomposition;
  NewFullSDispersionAtom.
```

这一步排除的是完整 S 窗口下的 Maynard-S 压缩映射，不是行命题闭合。
