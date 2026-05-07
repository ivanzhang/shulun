# Triad-A1 FullS-KLS-ext 专门化定理合同

本文把 `FullSKLSExternalTheoremSpecialization` 写成一个可审稿的外部深定理输入。它不是
DI/BFI 的自足重证，而是精确定义本文需要引用的 full-S 版本。

## 1. Theorem FullS-KLS-ext

设 `X≈P^2`，并令

```text
C≈P/log^{O(1)}P,
S≈P=X^(1/2+o(1)),
0<|h|<=H<=P/log^{O(1)}P.
```

令 `lambda_c` 为 level `Q<=P log^{O(1)}P=X^(1/2+o(1))` 的 well-factorable 模权，
`beta_s` 为 divisor-bounded 系数，`omega_h` 为 sawtooth/Fourier 平滑截断权。考虑当前
non-AP generic WFD 分支的未中心化、无投影窗口

```text
W_full(C,S,H)
  = sum_{c~C} lambda_c
    sum_{0<|h|<=H} omega_h
    sum_{s~S,(s,c)=1} beta_s e_c(a_h s + b_h bar{s}),
```

以及其 gcd strata、dyadic endpoints、partial summation 和 Type-I/II 分块带来的有限
多对数损失。

**Theorem FullS-KLS-ext.** 接受 DI 谱 Kloosterman 大筛与 BFI well-factorable
dispersion 定理时，对任意 `A>0`，可选择损失预算 `B(A)`，使

```text
|W_full(C,S,H)| <= NaturalWFDScale(C,S,H) / log^A P.
```

这里 `NaturalWFDScale(C,S,H)` 是 KZ-E/KE-13 中同一未中心化 WFD 窗口的自然二范数尺度。
该定理估计的是当前 non-AP WFD 对象本身，不插入块中心化，不删同块对角，不投影到
canonical/AP-source 对象。

## 2. 适配条件

该外部输入允许使用的条件正是：

```text
phase:
  CRT 相位归一化为 e_c(a_h s + b_h bar{s}).

modulus:
  C≈P/log^{O(1)}P, Q<=P log^{O(1)}P.

inverse variable:
  S≈P, full-S dyadic block retained.

frequency:
  0<|h|<=H<=P/log^{O(1)}P.

weights:
  lambda well-factorable, beta divisor-bounded, omega smooth.

loss:
  dyadic/gcd/smoothing/endpoint losses absorbed by B(A).
```

## 3. 外部版与自足版的边界

外部深定理版：

```text
FullS-KLS-ext accepted
=> ExternalFullSDIBFIAtomMatch closed
=> non-AP full-S scale side closed.
```

完全自足版：

```text
仍需 DIBFIPrimarySourceSpecializationProof:
  从 DI/BFI 原文定理逐项推出 Theorem FullS-KLS-ext，
  包括未中心化、无投影对象兼容性。
```

因此本文当前可以把“外部定理合同”写清，但不能把 DI/BFI 原文重证也标为已完成。
