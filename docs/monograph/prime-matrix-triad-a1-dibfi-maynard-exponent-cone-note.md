# Triad-A1 Maynard-W4 指数锥记录

**状态：** `maynard_w4_conditions_reduced_to_exponent_cone_open`

本记录把 Maynard-W4 的三条乘法条件改写为指数锥。它不证明当前 WFD 块满足这些条件，只把最后
尺度硬点改写成一个统一、可线性审查的 admission 条件。

## 1. 指数变量

令

```text
N_May = x^n；
R_May = x^r；
S_May = x^s；
M_May = x^m；
Q_May = x^q；
N_May M_May ≍ x，即 n+m=1。
```

## 2. Maynard-W4 三条件的指数形式

对角条件：

```text
N_May^2 R_May^2 S_May << x^(1-7eps)
```

等价为：

```text
2n + 2r + s <= 1 - eta。
```

第一条非对角条件：

```text
N_May R_May^2 S_May^5 Q_May < x^(2-14eps)
```

等价为：

```text
n + 2r + 5s + q <= 2 - eta。
```

第二条非对角条件：

```text
N_May^2 R_May^3 S_May^4 Q_May < x^(2-14eps)
```

等价为：

```text
2n + 3r + 4s + q <= 2 - eta。
```

## 3. 对角条件的结构解释

Maynard 证明中还使用：

```text
M_May > R_May^2 S_May N_May。
```

结合 `n+m=1`，这正是：

```text
1 - n > 2r + s + n
<=> 2n + 2r + s < 1。
```

所以 `MaynardDiagonalCondition` 不是独立新型不等式；它就是 factor condition 的指数形式。

## 4. 当前剩余

三条条件可统一写为：

```text
CurrentWFDFitsMaynardExponentCone:
  n+m=1；
  2n+2r+s <= 1-eta；
  n+2r+5s+q <= 2-eta；
  2n+3r+4s+q <= 2-eta。
```

因此当前尺度侧最窄剩余应变为：

```text
CurrentWFDMaynardVariableTranslation
  + CurrentWFDMatchesW4OffDiagonalForm
  + CurrentWFDFitsMaynardExponentCone。
```

后续若给出当前 WFD 的 `n,r,s,m,q` 翻译表，就可以直接线性检查是否闭合；若不满足，则失败项
会精确暴露为 factor-condition 失败、第一非对角失败或第二非对角失败。
