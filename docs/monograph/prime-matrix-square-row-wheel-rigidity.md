# 平方前后两行的轮筛刚性

**状态：** `structural_reduction_not_a_proof`

本文把用户提出的 `6/30/210` 轮结构写成可审稿的平方端点接口。核心结论是：
`P^2-k` 与 `P^2+k` 的低模覆盖不是概率现象，而是同一个轮单位集合的平移和镜像。

## 1. 轮骨架恒等式

令

\[
W=\prod_{\ell\in\mathcal L}\ell,\qquad
U_W=\{u\bmod W:(u,W)=1\},
\]

且 `P` 是不整除 `W` 的奇素数。对 `1<=k<P`：

\[
P^2+k\text{ 避开所有 }\ell|W
\iff
k\bmod W\in U_W-P^2.
\tag{WR-1}
\]

同理

\[
P^2-k\text{ 避开所有 }\ell|W
\iff
k\bmod W\in P^2-U_W.
\tag{WR-2}
\]

由于 `-U_W=U_W`，平方前后两行满足镜像关系

\[
P^2-U_W=-(U_W-P^2).
\tag{WR-3}
\]

因此前后两行的低模骨架完全由 `P^2 mod W` 决定。

## 2. 平方残基压缩

`P mod W` 可能有 `phi(W)` 个单位类，但 `P^2 mod W` 只落在单位平方类中。
对方阵最常用的轮：

```text
W=6:    square residues = 1；
W=30:   square residues = 1,19；
W=210:  square residues = 1,79,109,121,151,169；
W=2310: square residues = 30 classes。
```

这就是 `P=6k±1`、`P=30k±...`、`P=210k±...` 对平方端点真正产生刚性的地方：
不是只知道 `P` 的类，而是把 `P^2±k` 的覆盖偏移集合压成少数平方残基平移。

## 3. 双侧幸存偏移

同一个偏移 `k` 若同时让 `P^2-k` 和 `P^2+k` 避开 `W` 的素因子，则对每个奇素数
`\ell|W` 必须避开两个类：

\[
k\not\equiv P^2,\ -P^2\pmod \ell.
\tag{WR-4}
\]

因为 `P` 是单位且 `ell` 为奇素数，这两个类不同。因此每个奇 `ell` 留下 `ell-2`
个类；模 `2` 留下一个类。于是若 `W` 为含 `2` 的平方自由轮，

\[
\#\{k\bmod W:\ P^2-k,\ P^2+k\text{ 同时避开 }W\}
=
\prod_{\ell|W,\ \ell>2}(\ell-2).
\tag{WR-5}
\]

所以：

```text
W=6:    both=1；
W=30:   both=3；
W=210:  both=15；
W=2310: both=135。
```

这与 `P^2 mod W` 无关，是强刚性。

## 4. 尾段计数账本

审计脚本：

```text
experiments/prime_matrix_square_row_wheel_rigidity_audit.py
```

报告：

```text
docs/square_row_wheel_rigidity_audit_p100000_20260506.md
```

在 `P>=10007` 的尾段：

```text
W=210:
  plus >= 2286；
  minus >= 2287；
  both >= 714；
  plus/P >= 0.228440；
  both/P >= 0.071336。

W=2310:
  plus >= 2078；
  minus >= 2079；
  both >= 584；
  plus/P >= 0.207655；
  both/P >= 0.058173。
```

这些数不是概率估计。它们来自整轮块精确计数：

\[
\#\{1\le k\le H:k\bmod W\in A\}
=
\left\lfloor {H\over W}\right\rfloor |A|+\text{prefix}_A(H\bmod W).
\tag{WR-6}
\]

轮骨架给出一个确定的大候选集。要形成零行，`W` 以上的斜线必须覆盖这个确定集合。

## 4A. 轮提升不变性

进一步的结构恒等式见：

```text
docs/monograph/prime-matrix-wheel-promotion-invariance.md
docs/monograph/prime-matrix-promoted-wheel-setcover-capacity.md
docs/square_row_wheel_setcover_capacity_audit_w6_2310_20260506.md
```

若 `s<P` 是素数且 `s∤W`，把 `s` 提升进轮底座 `W'=Ws`，最终幸存偏移集合不变：

\[
R_W^\pm(P)=R_{Ws}^\pm(P).
\tag{WR-7a}
\]

因为

\[
S_{Ws}^\pm(P)=S_W^\pm(P)\setminus C_s^\pm(P),
\]

而高素覆盖层同步去掉了 `q=s` 这条斜线。审计中 `W=6,30,210,2310` 的最终未覆盖偏移完全一致。

这说明小模连乘不是概率近似，而是严格的覆盖层重分配工具。扩大轮模数不能自动证明行命题，
但能把剩余覆盖问题放到更刚性的 CRT 坐标系中。

## 5. 高素斜线的集合覆盖形式

固定平方后行。对任意素数 `q`，`q` 覆盖 `P^2+k` 当且仅当

\[
k\equiv -P^2\pmod q.
\tag{WR-7}
\]

平方前行则为

\[
k\equiv P^2\pmod q.
\tag{WR-8}
\]

因此，去掉轮素因子后，高素补洞不是任意覆盖，而是在刚性集合

\[
S_W^+(P)=\{1\le k<P:k\bmod W\in U_W-P^2\}
\]

或

\[
S_W^-(P)=\{1\le k<P:k\bmod W\in P^2-U_W\}
\]

上，用每个 `q>max(L)` 的单个同余类做集合覆盖。

当前结构化目标可写为：

```text
Wheel-Rigid Set Cover:
  union_{q in (max L, P)} {k in S_W^±(P): k≡∓P^2 mod q}
  不能覆盖全部 S_W^±(P)，
  或覆盖失败必须产生 PDEC/SAE/ColumnCRT 证书。
```

这比“轮筛后剩余密度约为 phi(W)/W”强得多，因为每个高素斜线与低模轮骨架的交点完全由 CRT 决定。

## 6. 与当前 ERO-Low 的连接

`ERO-Low` 的 B-process 包络中，最大贡献来自小平方自由核：

```text
2,3,5,6,7,10,14,15,21,30,42。
```

这些正是 `2,3,5,7` 轮结构及其低阶组合。`CoreKernel-Lock` 可以解释为：
`P` 不能同时把多个低阶平方自由方向 `2P sqrt(d)` 锁入同向短弧。

轮刚性给出相同事实的离散版本：`P^2 mod 210` 只有 6 个平方残基，核心低模结构只有少数平移骨架。
若核心小核与尾核正贡献同步，就意味着许多不同平方自由方向同时相锁，应进入 endpoint `PDEC`。

## 7. 当前最小硬点

这条结构路线的最小硬点不是再扩大实验，而是证明以下二分：

```text
Wheel-Core Lock Exclusion:
  对 W=210 或 2310，核心轮骨架的高峰不能与尾核正堆积同步。

Failure -> PDEC:
  若同步发生，则从 P^2 mod W、若干 q-residue 覆盖类、
  以及 B-process 非平方根相位中抽取同一个 endpoint CRT/Fourier 缺陷。
```

完成该二分后，平方前后端点的低模结构将从“筛余概率”升级为“轮骨架刚性 + 缺陷排斥”。
