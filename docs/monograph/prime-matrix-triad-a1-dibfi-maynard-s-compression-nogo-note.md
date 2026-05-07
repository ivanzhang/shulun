# Triad-A1 Maynard S-compression no-go 记录

**状态：** `maynard_s_compression_map_rejected_full_s_window_open`

本记录继续硬攻 `MaynardSCompressionMap`。结论是：在当前非 AP generic WFD 路线中，如果同时保持
现有 W4 对象等式

```text
z=s1*s2
```

并把 `s1,s2` 视为共同变量表的完整逆元窗口变量，则 Maynard-S 压缩映射不可能存在。

## 1. 两个强制事实

共同变量表/KE-13 已固定：

```text
s1,s2 ~ S_common；
S_common≈P=X^(1/2+o(1))。
```

Maynard-W4 对象等式要求：

```text
Z_window ≍ S_May^2；
z=s1*s2。
```

因此若当前 WFD 的 `s1,s2` 不被进一步拆短，则：

```text
Z_window ≍ S_common^2 ≍ X；
S_May ≍ X^(1/2)。
```

## 2. 与指数锥冲突

第 109 节已经由指数锥推出：

```text
q=1/2+o(1)  =>  S_May <= X^(3/10-o(1))。
```

但完整 `s1*s2` 对象等式强制：

```text
S_May ≍ X^(1/2)。
```

所以当前三个条件不能同时成立：

```text
CurrentWFDMatchesW4OffDiagonalForm；
FullCommonSWindowUsed；
MaynardSCompressionMap。
```

## 3. 剩余出口

这不是行命题闭合，而是排除一条错误闭合路径。剩余必须变成：

```text
ShortSSubwindowDecomposition:
  证明当前 KE-13/WFD 的 s1,s2 窗口可被合法分解成
  S_short<=X^(3/10-o(1)) 的子窗口，并且不丢失目标对象与质量；

或

NewFullSDispersionAtom:
  引入并证明一个真正适配 S_common≈X^(1/2) 的 full-S 原始 dispersion 原子。
```

如果二者都没有，则当前 Maynard-W4 匹配路线对非 AP generic WFD 不是闭合路径。
