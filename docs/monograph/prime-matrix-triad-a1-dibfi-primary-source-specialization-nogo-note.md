# Triad-A1 DI/BFI primary-source specialization no-go

本文审计最后单点：

```text
DIBFIPrimarySourceSpecializationProof:
  derive Theorem FullS-KLS-ext from DI/BFI primary sources line by line.
```

结论：不能把它标为已闭合。主来源可支持 AP-level well-factorable 定理与 DI Kloosterman
估计，但它们不自动推出本文自定义的 full-S KLS-ext 对象。

## 1. 主来源修正

Maynard `arXiv:2006.07088` 中引用的 BFI Theorem 10 是：

```text
BFI1986-Theorem10:
  Bombieri--Friedlander--Iwaniec,
  Primes in Arithmetic Progressions to Large Moduli,
  Acta Math. 156(3--4), 203--251, 1986.
```

不是当前历史索引里曾写成主来源的 Math. Ann. 1987 续篇。1987 条目只能保留为兼容别名，
不能继续作为 well-factorable AP Theorem 10 的主定位。

## 2. BFI Theorem 10 能关闭什么

BFI Theorem 10 给出的是 prime-AP discrepancy 的 well-factorable 加权估计：

```text
Q <= X^(4/7-eps),
lambda_q well-factorable,
sum_q lambda_q (pi(X;q,a)-pi(X)/phi(q)) << X/log^A X.
```

在本文参数 `Q<=P log^O P=X^(1/2+o(1))` 下，level 有正余量。因此 AP-source 分支可以
直接由 BFI Theorem 10 闭合。

但 non-AP generic WFD 分支不是 AP-source 残差对象；它是抽出的 KE-13/WFD Kloosterman
窗口。因此 BFI Theorem 10 本身不能直接替代 `FullS-KLS-ext`。

## 3. DI Theorem 12 能关闭什么

DI Theorem 12 提供 Kloosterman 平均估计。Maynard 的公开 TeX 将其重述为
`Deshouillers-Iwaniec estimate`，其核心是一个带 `J^2` 的 Kloosterman 二范数界。

该估计是 BFI/Maynard dispersion proof 的深核，但把它代入 W4/DI J-scale 后会产生尺度条件。
此前指数锥已经给出：

```text
n + 2r + 5s + q <= 2 - eta.
```

当前 full-S non-AP 块有：

```text
q = 1/2 + o(1),
s = 1/2 + o(1).
```

于是左侧至少为：

```text
0 + 0 + 5/2 + 1/2 = 3,
```

大于 `2`。因此 DI/Maynard 的现有 J-scale 不能在 full-S `S≈X^(1/2)` 块上给出所需
任意 log-saving。

## 4. 当前最窄结论

所以 `DIBFIPrimarySourceSpecializationProof` 被当前主来源尺度条件阻断：

```text
DIBFIPrimarySourceSpecializationProof rejected for full-S KLS-ext.
```

剩余不再是“补一页引用”，而是二选一：

```text
NewFullSTheoremInput:
  接受一个严格强于当前 DI/BFI 专门化的 full-S KLS 外部定理；

APSourceLift:
  证明当前 non-AP generic WFD 残差其实可无损提升回 BFI prime-AP discrepancy。
```

否则不能诚实宣称行命题完全闭合。
