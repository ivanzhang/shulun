# 对角平方后端点一尾互补因子恒等式

**状态：** `postsquare_tail_perfect_cover_reduced_to_short_prime_cofactor_cover`

本文继续压缩 `x=P` 对角端点的 `Tail-Perfect-Cover Exclusion`。核心结论是：当 `P>=23` 时，平方后窗口的一尾项不是一般粗互补因子，而是唯一的短窗素互补因子。

## 1. 设置

令

\[
y=\max(2,\lfloor P/e\rfloor),\qquad 1\le k<P,\qquad n=P^2+k.
\]

低筛骨架条件为 `P^-(n)>y`。若骨架点被尾素数 `y<ell<P` 命中，则

\[
n=\ell m.
\tag{PCF-1}
\]

由于 `n` 已避开所有 `<=y` 的素因子，互补因子也满足

\[
P^-(m)>y.
\tag{PCF-2}
\]

并且 `m` 被锁入极短区间

\[
\left\lfloor {P^2\over \ell}\right\rfloor+1
\le m\le
\left\lfloor {P^2+P-1\over \ell}\right\rfloor .
\tag{PCF-3}
\]

因为 `ell>y>=floor(P/e)`，该区间的整数长度满足

\[
L_\ell<1+{P\over \ell}<1+e<4,
\]

所以每条尾斜线最多只贡献 `3` 个互补因子候选。

## 2. 素互补因子阈值

当 `P>=23` 时，由 `y+1>P/e` 与 `e^3<21` 得

\[
(y+1)^3>{P^3\over e^3}>{P^3\over 21}>P^2+P-1.
\tag{PCF-4}
\]

结合 `(PCF-3)`，

\[
m\le {P^2+P-1\over y+1} < (y+1)^2.
\tag{PCF-5}
\]

若 `m` 是复合数且满足 `P^-(m)>y`，则 `m` 至少含两个 `>y` 的因子，故

\[
m\ge (y+1)^2,
\]

与 `(PCF-5)` 矛盾。因此：

```text
P>=23 时，平方后端点的一尾互补因子 m 必为素数。
```

同时由于 `ell<P` 且 `n>P^2`，有 `m>P`。所以一尾项精确形如

\[
P^2+k=\ell m,\qquad y<\ell<P<m,\qquad m\in\mathbb P.
\tag{PCF-6}
\]

## 3. 与尾碰撞消失的合并

已有文档

```text
docs/monograph/prime-matrix-diagonal-postsquare-tail-collision-vanishing.md
```

证明 `P>=23` 时平方后窗口没有多尾碰撞。因此 `(PCF-6)` 的表示唯一，低筛骨架被分解为：

```text
低筛骨架 = 无尾点 disjoint_union 短窗素互补一尾点。
```

无尾点位于 `(P^2,(P+1)^2)` 内且没有 `<P` 素因子，所以必为素数。

## 4. 新的最小硬点

`Tail-Perfect-Cover Exclusion` 现在可写成更窄的集合排斥：

\[
\{1\le k<P:P^-(P^2+k)>y\}
\not\subseteq
\bigcup_{y<\ell<P}
\{\ell m-P^2:m\in\mathbb P\cap I_\ell\},
\tag{PCF-7}
\]

其中

\[
I_\ell=
\left[
\left\lfloor {P^2\over \ell}\right\rfloor+1,
\left\lfloor {P^2+P-1\over \ell}\right\rfloor
\right],
\qquad |I_\ell|\le 3.
\]

也就是说，端点剩余硬点不再是“任意尾素数覆盖低筛骨架”，而是：

```text
Short Prime-Cofactor Perfect-Cover Exclusion:
长度至多 3 的互补素数窗口，不能完美吃掉平方后端点的低筛骨架。
```

若 `(PCF-7)` 失败，则每个低筛骨架列都被唯一的二素数锚 `ell*m` 吃掉。这种失败必须表现为互补素数短窗异常集中，或固定端点相位的 `PDEC/Tail-anchor` 缺陷。

## 5. 三条倒数地板曲线

把

\[
P^2=\ell a_\ell+r_\ell,\qquad 0\le r_\ell<\ell
\]

写入 `(PCF-3)`。由于 `|I_ell|<=3`，任意一尾命中都可唯一写成

\[
m=a_\ell+s,\qquad s\in\{1,2,3\},
\tag{PCF-8}
\]

并且对应列为

\[
k=\ell s-r_\ell.
\tag{PCF-9}
\]

所以完美覆盖若存在，就不是任意 set-cover，而是三条倒数地板素数曲线的完美覆盖：

```text
ell prime, y<ell<P；
floor(P^2/ell)+s prime, s=1,2,3；
k=ell*s-(P^2 mod ell) 落入低筛骨架。
```

这给出下一层可攻接口：

```text
Reciprocal-Floor Prime-Pair Excess:
三条曲线上的素-素命中数若达到低筛骨架大小，
则必须产生短窗素数异常集中或端点相位 PDEC/Tail-anchor 缺陷。
```

进一步的维数差合同见：

```text
docs/monograph/prime-matrix-diagonal-postsquare-primepair-dimension-gap.md
```

该文把剩余目标拆为两个显式常数输入：低筛骨架下界 `G(P)>=0.48 P/log P` 与倒数地板素对上界
`B(P)<=1.50 P/log^2 P`。这组常数一旦证明，从 `P>=23` 起即可直接给出正余量。

## 6. 审计证据

脚本：

```text
experiments/prime_matrix_diagonal_postsquare_tail_cofactor_audit.py
```

最新输出：

```text
docs/diagonal_postsquare_tail_cofactor_audit_p100000_20260505.md
docs/diagonal_postsquare_tail_cofactor_audit_p100000_20260505.json
```

读数：

```text
max_p=100000；
odd primes checked=9591；
total y-rough cofactors=3770121；
composite y-rough cofactors=4；
last composite y-rough p=13；
max cofactor interval length=3；
last cofactor-prime-threshold failure p=19；
offset counts={1:2382774, 2:1224068, 3:163279}；
max single-row cofactor record:
  P=98327, y=36172, yrough cofactors=817,
  offset counts={1:508, 2:267, 3:42}。
```

这些读数支持上面的阈值剥离，但正式证明只依赖 `(PCF-4)` 到 `(PCF-5)`；数值审计用于核查有限小例外与实现口径。
