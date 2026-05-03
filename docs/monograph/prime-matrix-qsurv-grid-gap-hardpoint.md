# QSurv 的 q 网格素数荒漠等价硬点

**状态：** `q_grid_prime_desert_equivalence_and_sae_target`

本文接续：

- `prime-matrix-zero-row-delay-recursive-lemma.md`；
- `prime-matrix-dec-ospc-exclusion-hardpoint.md`；
- `prime-matrix-qsurv-gap-structure-audit.md`。

当前唯一剩余硬点应从模糊的“排除坏行”改写为精确的 `q` 网格素数荒漠排斥。

## 1. QSurv 的等价形式

设 `p<q` 为相邻奇素数。定义

\[
I_s^{(q)}=[(s-1)q+1,sq]\qquad(1\le s\le q).
\]

由平方壳层引理，对 `n<=q^2`：

\[
(n,P(p))=1,\quad n>1
\quad\Longrightarrow\quad
n\in\mathbb P\ \text{or}\ n=q^2.
\]

因此

\[
\mathcal R_p(I_s^{(q)})\setminus\{q^2\}\ne\varnothing
\]

等价于

\[
I_s^{(q)}\cap\mathbb P\ne\varnothing.
\tag{QGrid}
\]

所以 `QSurv(p,q)` 不是一般粗数命题，而是：

```text
每个 q 网格行在 q^2 以前含至少一个素数。
```

## 2. 失败的素数间隙表达

若某个 `q` 行为空，则存在相邻素数 `a<b` 使

\[
a<(s-1)q+1,\qquad b>sq.
\]

于是

\[
b-a>q-1.
\]

更精确地，失败不是任意大素数间隙，而是一个素数间隙覆盖完整 `q` 网格单元：

```text
prime gap covers [(s-1)q+1, sq].
```

这比 `max prime gap <= q` 弱，也更有结构。实验 `prime-matrix-qsurv-gap-structure-audit.md` 中出现 `p=11,q=13` 的最大素数间隙 `14>q`，但没有空 `q` 行，因为该间隙没有覆盖完整 `q` 网格单元。这说明下一步不能简单攻普通最大素数间隙，而必须攻 `q` 网格对齐荒漠。

## 3. 为什么旧约束还不够

### 3.1 p 对齐零行延迟不够

`p` 对齐零行控制的是

\[
[(r-1)p+1,rp].
\]

但 `q` 行控制的是

\[
[(s-1)q+1,sq].
\]

当 `q=p+g` 且 `g` 小时，多数 `q` 行跨越两个 `p` 行端点，只包含旧行尾段和下一旧行首段。故

```text
p-aligned zero-row delay
not imply QGrid.
```

### 3.2 完整 CRT 周期均衡不够

旧筛在完整 `P(p)` 周期内各非零类严格均衡。但 `I_s^{(q)}` 长度只有 `q`，而 `P(p)` 指数级大。完整周期均衡不能直接控制单个长度 `q` 的短窗。

### 3.3 裸覆盖容量不够

若 `I_s^{(q)}` 为空，则每个 `n∈I_s^{(q)}` 至少有一个小素因子 `\ell<=p`。对每个 `\ell`，它在长度 `q` 窗口内可覆盖约 `q/\ell` 个点，因此

\[
\sum_{\ell\le p}{q\over \ell}
\]

远大于 `q`。所以一阶容量不能推出矛盾。必须使用相邻互质、同标签间距、端点漂移、复用能量和 Fourier/CRT 缺陷。

### 3.4 Sylvester 型定理不够

Sylvester--Schur 型结论可保证一段连续整数乘积含有大于段长的素因子。但空 `q` 行只要求每个整数有某个小因子 `<=p`；它仍可同时含大素因子。因此 Sylvester 型输入不能直接给出旧筛幸存者。

## 4. SAE 的精确目标

若 `QGrid` 失败，对每个 `n∈I_s^{(q)}` 选一个小素因子标签

\[
\lambda(n)\le p,\qquad \lambda(n)\mid n.
\]

这些标签满足四类刚性：

1. **相邻互质：** 相邻整数标签不同，且相邻商也受互质约束；
2. **同标签间距：** 若 `\lambda(n)=\ell`，同标签位置相距至少 `\ell`；
3. **端点漂移：** `I_s^{(q)}` 的端点随 `s` 以步长 `q` 对所有 `d|P_T` 作单位旋转；
4. **早期壳层限制：** 全部 `n<=q^2`，因此任何避开小素因子的点自动是素数或 `q^2`。

`SAE` 应证明：

```text
在上述四类刚性下，一个孤立 q 网格荒漠不可能存在；
若存在，则相邻漂移窗口中同一低模端点缺陷必持续出现，进入 PDEC。
```

这把最终硬点压成两条可攻分支：

```text
QGrid failure
=> PDEC
   or SAE label-cover contradiction.
```

## 5. 实验支撑

`prime-matrix-qsurv-gap-structure-audit.md` 到 `p<=5000` 显示：

```text
zero_q_row_records = 0
global_min_q_row_prime_count = 1
singleton_min_records = 6
max_gap_over_q = 1.0769230769230769
```

解释：

- 没有空 `q` 行；
- 最薄余量确实可以只有一个素数，所以不能用粗平均；
- 普通素数间隙可以超过 `q`，但不一定造成网格荒漠；
- 需要证明的是网格对齐荒漠排斥，而不是普通间隙上界。

## 6. 下一步最小命题

当前最小可攻命题应命名为 `GJE-SAE`：

**GJE-SAE（q 网格早期 Jacobsthal--SAE 引理）。**
对相邻奇素数 `p<q`，不存在 `1<=s<=q` 使

\[
I_s^{(q)}\cap\mathbb P=\varnothing.
\]

更结构化地，若存在，则其小素标签覆盖必在同一低模字典块上造成 `PDEC`，或违反单窗标签覆盖刚性。

该命题一旦证明，就与 `ZRL-1` 合成：

```text
GJE-SAE
=> QSurv(p,q)
=> Row(q).
```

## 7. 审稿边界

本文完成的是硬点定位，不是最终证明。它排除了三个误攻方向：

1. 只证明 `p` 对齐零行延迟；
2. 只引用完整 CRT 周期均衡；
3. 只证明普通 `prime gap <= q` 或用 Sylvester 型大素因子结论。

真正必须证明的是：

```text
q-grid prime desert impossible by PDEC-or-SAE.
```

进一步的终端带分解见 `docs/monograph/prime-matrix-gje-sae-terminal-band-decomposition.md`。该文档说明：任何指数 `theta>1/2` 的普通短区间素数输入只能覆盖低行段，不能闭合靠近 `q^2` 的终端带；终端带在变量 `m=q^2-n` 下等价为一个“每个小素数只允许一个非零指定类 `q^2 mod ell`”的 CRT 覆盖问题。当前最小硬核因此收缩为 `Terminal-SAE/PDEC`。
