# Terminal-SAE 分层骨架/尾命中不等式

**状态：** `terminal_sae_reduced_to_split_margin_inequality`

本文接续 `prime-matrix-gje-sae-terminal-band-decomposition.md`，把终端镜像 CRT 覆盖硬点压缩为一个确定不等式：

```text
low-sieved skeleton count > tail-prime incidence count.
```

该不等式一旦逐行证明，就直接排除 `Terminal-SAE` 反例。

## 1. 终端镜像块

设 `p<q` 为相邻奇素数。对终端行写

\[
s=q-h+1,\qquad 1\le h\le q,
\]

并令

\[
B_h=[(h-1)q,hq-1]\cap\mathbb Z
\]

为镜像变量 `m=q^2-n` 的长度 `q` 块。`m=0` 对应例外点 `n=q^2`，必须排除。

对每个旧素数 `\ell<=p`，坏类为

\[
m\equiv q^2\pmod\ell.
\]

因此终端空行等价于

\[
B_h\setminus\{0\}\subseteq
\bigcup_{\ell\le p}\{m:m\equiv q^2\pmod\ell\}.
\tag{1}
\]

## 2. 分层骨架

取

\[
y=\max(2,\lfloor p/e\rfloor).
\]

定义低筛骨架

\[
G_y(h)=
\#\{m\in B_h\setminus\{0\}:
m\not\equiv q^2\pmod\ell\ \text{for all}\ \ell\le y\}.
\]

再定义尾命中重数

\[
T_y(h)=
\sum_{y<\ell\le p}
\#\{m\in B_h\setminus\{0\}:
m\not\equiv q^2\pmod r\ (r\le y),
\ m\equiv q^2\pmod\ell\}.
\]

注意 `T_y(h)` 是带重数计数。实际被尾素数覆盖的骨架点数不超过 `T_y(h)`。

## 3. 核心不等式

**Lemma TSI-1（分层不等式排除终端覆盖）。**
若对某个 `h` 有

\[
G_y(h)>T_y(h),
\tag{TSI}
\]

则终端块 `B_h` 不可能满足 `(1)`。换言之，对应 `q` 行含有旧 `p`-筛幸存者，并由平方壳层引理给出素数。

**证明。**
反设 `(1)` 成立。所有低筛骨架点已经避开 `\ell<=y` 的坏类，因此它们必须被某个尾素数 `y<\ell<=p` 的坏类覆盖。若用 `U_y(h)` 表示被尾素数覆盖的骨架点集合，则

\[
G_y(h)=|U_y(h)|.
\]

而 `T_y(h)` 对同一集合按尾素数命中重数计数，所以

\[
|U_y(h)|\le T_y(h).
\]

于是 `G_y(h)<=T_y(h)`，与 `(TSI)` 矛盾。证毕。

因此 `Terminal-SAE` 的最小证明义务变为：

```text
For every adjacent p<q and every 1<=h<=q:
G_y(h) > T_y(h),  y=max(2,floor(p/e)).
```

## 4. 实验支持

审计见 `docs/monograph/prime-matrix-terminal-sae-split-audit.md`。当前参数：

```text
max_p = 1000
y = max(2, floor(p/e))
```

结果：

```text
prime_count = 167
split_certified_records = 167
unresolved_records_p_ge_7 = 0
min_margin_p_ge_7 = 1
min_margin_p_ge_19 = 1
```

也就是说，样本中每个终端镜像块都满足 `G_y(h)-T_y(h)>0`。最小余量为 `1`，说明该不等式非常锋利，但方向正确。

## 5. 为什么这是实质突破

原先的终端覆盖问题是：

```text
所有 ell<=p 的坏类是否能覆盖整个 q 块？
```

直接一阶容量太大，无法矛盾。分层后变成：

```text
先保留 ell<=p/e 后的骨架；
再证明 p/e<ell<=p 的尾素数连带重数也不够覆盖骨架。
```

模型上，

\[
G_y(h)\approx q\prod_{\ell\le y}(1-1/\ell)
\asymp {q\over \log p},
\]

而

\[
T_y(h)\approx
G_y(h)\sum_{p/e<\ell\le p}{1\over\ell}
\asymp {G_y(h)\over\log p}.
\]

所以期望余量约为

\[
G_y(h)\left(1-O({1\over\log p})\right),
\]

随 `p` 增长应越来越强。实验中的大 `p` 余量增厚与该模型一致。

## 6. 剩余证明义务

要把 `(TSI)` 升级为定理，需要两个显式估计：

1. **骨架下界：**
   \[
   G_y(h)\ge c_1{q\over\log p}-E_1(p,h).
   \]
2. **尾命中上界：**
   \[
   T_y(h)\le c_2{q\over(\log p)^2}+E_2(p,h).
   \]

并证明

\[
c_1{q\over\log p}-E_1(p,h)
>
c_2{q\over(\log p)^2}+E_2(p,h)
\]

对所有相邻 `p<q` 和 `1<=h<=q` 成立。

难点在于 `G_y(h)` 是长度约 `y e` 的短区间筛余下界，普通线性筛在这个尺度有明显的短区间/Jacobsthal障碍。必须利用这里的特殊结构：

- 每个坏类都是同一个相位 `q^2 mod ell`；
- 这些类全是非零类；
- 终端块随 `h` 平移形成端点旋转；
- 若某些 `h` 上骨架异常偏小，就应触发 `PDEC`。

## 7. 当前最小硬点

最终硬点现在可以精确写成：

```text
TSI-or-PDEC:
Either G_y(h)>T_y(h) for every terminal block,
or the failure of this split inequality creates persistent endpoint CRT defect.
```

这比 `Terminal-SAE` 更窄：只需证明一个低筛骨架与尾命中之间的显式余量不等式，或者证明该余量失败必然持续化。

尾命中项的进一步结构化见 `docs/monograph/prime-matrix-terminal-tail-cofactor-identity.md` 与审计 `docs/monograph/prime-matrix-terminal-tail-cofactor-audit.md`。尾命中精确等于 `q^2-m=ell*t` 中互补因子 `t` 的极短 `y`-rough 区间计数；样本 `p<=1000` 中最大互补区间长度为 `4`，复合 `y`-rough 互补因子最后只出现在 `p=19`。因此右侧 `T_y(h)` 可进一步压成极短互补素数窗口总和，异常则进入 Tail-anchor/PDEC。

新增 `docs/monograph/prime-matrix-terminal-sae-cancellation-identity.md` 后，`G_y(h)-T_y(h)` 又有精确单尾抵消恒等式：

```text
G_y(h)-T_y(h)=sum_{P^-(n)>y}(1-omega_tail(n)).
```

恰有一个尾素因子的骨架点贡献为 `0`；真正剩余硬核是证明“无尾储备数严格大于多尾碰撞超额”。在 `y^3>q^2` 后，这进一步化为“无尾储备数大于双尾碰撞数”。因此当前最小接口更新为 `RCI/PDEC`。
