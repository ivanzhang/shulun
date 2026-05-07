# Triad-A1 short-S subwindow no-go 记录

**状态：** `short_s_subwindow_decomposition_rejected_full_s_atom_open`

本记录继续审计 `ShortSSubwindowDecomposition`。关键区别是：Maynard-W4 的 `S_May` 由

```text
Z_window≈S_May^2
```

和对象变量

```text
z=s1*s2
```

共同确定，它控制的是 `s1,s2` 的实际量级，不是把一个大 dyadic 窗口切成小区间后的区间宽度。

## 1. 小宽度不等于小 Maynard-S

若当前 dyadic 块为：

```text
s1,s2 ~ S_common≈X^(1/2)，
```

即使把该窗口切成许多短区间：

```text
s_i in [u,u+L],  L<=X^(3/10)，  u≈X^(1/2)，
```

仍有：

```text
s_i≈X^(1/2)，
z=s1*s2≈X。
```

因此 W4 的

```text
Z_window≈S_May^2
```

仍强制：

```text
S_May≈X^(1/2)，
```

不会因为区间宽度 `L` 较短而变成 `X^(3/10)`。

## 2. 真实短 S 会丢失当前 dyadic 块

若要求真实满足：

```text
S_May<=X^(3/10-o(1))，
```

则必须有：

```text
s1,s2<=X^(3/10-o(1))。
```

这不是 `S_common≈X^(1/2)` dyadic 块的子分解，而是离开了当前 dyadic 块。因此它不能在不丢失
当前目标对象/质量的前提下关闭 full-S non-AP generic WFD 路线。

## 3. 当前剩余

于是第 111 节留下的二选一继续收缩：

```text
ShortSSubwindowDecomposition:
  rejected for the current full-S dyadic block；

NewFullSDispersionAtom:
  still open。
```

当前尺度侧只能要求一个真正适配 `S_common≈X^(1/2)`、`z=s1*s2≈X` 的 full-S 原始 dispersion 原子。
