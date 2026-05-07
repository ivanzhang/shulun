# Triad-A1 Maynard-W4 参数账本记录

**状态：** `maynard_w4_parameter_template_extracted_current_wfd_match_open`

本记录固定 Maynard 对 DI Theorem 12 调用后的 W4 参数账本。它不是当前 WFD 块的闭合证明；
它只把需要核验的 W4 参数条件从源码证明中抽成可审稿表。

## 1. W4 参数

Maynard W4 阶段使用：

```text
B << N R；
C << N R S；
F << N / Q；
Z ≍ S^2；
Y << x^o N R^2 S^3 / M。
```

这里的 `N,R,S,M,Q` 是 Maynard 源码中的上游参数；为避免和本项目共同变量表冲突，后续账本
应记作：

```text
N_May, R_May, S_May, M_May, Q_May。
```

## 2. J-bound 简化

在 W4 代入后：

```text
J^2 <= C(Z+Y)(C+B Z)
       + C^2 B sqrt((Z+Y)Z)
       + B^2 Y Z。
```

若 Maynard 的 factor 条件给出

```text
M_May > R_May^2 S_May N_May,
```

则 `Z>Y`，且主要界简化为：

```text
J^2 << x^eps (
  N_May^2 R_May^2 S_May^5
  + N_May^3 R_May^3 S_May^4
)。
```

## 3. W4 目标与充分条件

W4 目标是：

```text
W4 << N_May^2 R_May^2 S_May^3 / x^(6 eps)。
```

源码推导把非对角项压到以下两个充分条件：

```text
N_May R_May^2 S_May^5 Q_May < x^(2-14 eps)；
N_May^2 R_May^3 S_May^4 Q_May < x^(2-14 eps)。
```

对角项还需要：

```text
N_May^2 R_May^2 S_May << x^(1-7 eps)。
```

## 4. 当前剩余

因此当前项目的尺度侧终端应改写为：

```text
CurrentWFDSatisfiesMaynardW4Conditions:
  1. 当前未中心化 WFD 块逐项生成 W4 off-diagonal 变量 z,y,b,c；
  2. 当前 X,Q,N,M,C,S,H 非冲突地翻译为 N_May,R_May,S_May,M_May,Q_May；
  3. 证明三条 Maynard 条件均由当前窗口范围推出。
```

这一步只抽取模板，不能替代第 1--3 项的当前对象证明。
