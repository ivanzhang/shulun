# Triad-A1 alternate W4 reroute audit 记录

**状态：** `alternate_w4_reroute_rejected_maynard_s_compression_open`

本记录审计 `AlternateW4ObjectRerouting` 是否已有可用闭合出口。结论是：在当前已登记合同中，
没有一个可直接替代 Maynard-S 压缩的闭合对象路由。

## 1. AP-source 直接 BFI 不是非 AP 出口

直接 BFI 原子确实存在，但它的闭合范围已经被 AP-source 分支限定：

```text
APSourceDirectBFI:
  closed on AP-source branch；

NonAPSourceGenericWFD:
  cannot silently upgrade to prime-AP discrepancy；
  must use KE-13 no-projection / original-dispersion fallback。
```

因此非 AP generic WFD 不能用“回到 BFI prime-AP 原子”绕开当前 Maynard-S 障碍。

## 2. HLCWindowedKLSAtom 也不是 generic WFD 出口

`HLCWindowedKLSAtom` 已登记为 clean HLC 分支可用，但直接 BFI 原子路由器明确说明：

```text
HLCWindowedKLSAtom:
  closed_for_clean_hlc_branch_only；
  not a direct replacement for generic WFD common table。
```

所以它也不能替代当前非 AP generic WFD 的 W4/DI 路由。

## 3. non-AP fallback 回到同一路线

非 AP-source 原始 dispersion 路由器给出的 fallback 是：

```text
DIBFIQuantifiedNoProjectionWindowCertificateForNonAPSource
  = NoProjectionUncenteredDispersionIdentity
    + QuantifiedDIBFIWindowSubstitution。
```

其中尺度侧已经被压到 Maynard-W4/DI 指数锥链条。因此这不是另一个闭合出口，而是当前
`MaynardSCompressionMap` 所在的同一路线。

## 4. 当前剩余

`AlternateW4ObjectRerouting` 在当前资料下没有闭合出口。除非新增并证明一个新的外部原始
dispersion 原子，否则当前硬点只能保留为：

```text
MaynardSCompressionMap:
  从 s1,s2,h,completion 结构中抽出真实 S_May，
  且 S_May <= X^(3/10-o(1))。
```

这一步不证明 `MaynardSCompressionMap`，但排除了把它旁路掉的已登记路线。
