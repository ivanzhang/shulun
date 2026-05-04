# AlphaTail 条件尾重叠 Rankin/ColumnCRT 账本

**状态：** `alpha_tail_tail_overlap_rankin_reduction_open`

本文继续压缩 `RoughSurplus` 的条件高大素尾出口。前文已经证明

\[
\Xi_T=|R|-|L|V_T
=|L|(1-V_T)-\left|\bigcup_{q\in\mathcal P_T}\mathcal A_q\right|.
\tag{TOR-1}
\]

因此 `Xi_T>0` 等价于：在低大素幸存集 `L` 上，尾大素删除并集低于乘法模型。
本文件处理其中的“尾删除重叠过强”分支。

## 1. 尾命中重数

对

\[
\mathcal A_q=\{d\in L:\exists 0\le j<m,\ d+jr\equiv0\pmod q\}
\tag{TOR-2}
\]

定义尾命中重数

\[
h_T(d)=\sum_{q\in\mathcal P_T}1_{\mathcal A_q}(d).
\tag{TOR-3}
\]

记

\[
T_1=\sum_{d\in L}h_T(d),\qquad
U_T=\left|\bigcup_{q\in\mathcal P_T}\mathcal A_q\right|,\qquad
\Omega_T=T_1-U_T.
\tag{TOR-4}
\]

这里 `Omega_T` 是真实重叠预算：每个被一个尾素删除的点贡献 `0`，每多命中一个尾素贡献 `1`。
由 `(TOR-1)`，

\[
\Xi_T=|L|(1-V_T)-U_T.
\tag{TOR-5}
\]

所以若一阶质量没有亏损，即

\[
T_1\ge |L|(1-V_T)-\eta,
\tag{TOR-6}
\]

则

\[
\Omega_T=T_1-U_T\ge \Xi_T-\eta.
\tag{TOR-7}
\]

这一步把条件尾盈余精确转成重叠盈余：若尾质量正常而删除仍不足，缺口只能由大量多重命中支付。

## 2. 点态乘积上界

令

\[
N_m(d)=\prod_{j=0}^{m-1}(d+jr),\qquad
z=\max_{d\in I_m,0\le j<m}|d+jr|.
\tag{TOR-8}
\]

若 `h_T(d)>=\ell`，则有 `ell` 个不同尾素同时整除 `N_m(d)`。设
`q_{T,1}<q_{T,2}<...` 为 `P_T` 中尾素的递增排列，则

\[
\prod_{i=1}^{\ell}q_{T,i}\le |N_m(d)|\le z^m.
\tag{TOR-9}
\]

因此

\[
h_T(d)\le L_T(z,m):=\max\left\{\ell:\prod_{i=1}^{\ell}q_{T,i}\le z^m\right\}.
\tag{TOR-10}
\]

这是无条件点态约束。它不排除所有重叠，但把任一点的补洞复用次数锁死为有限 Rankin 账本。

## 3. Rankin 矩账本

对任意 `rho>1` 与整数 `ell>=1`，

\[
|\{d\in L:h_T(d)\ge \ell\}|
\le \rho^{-\ell}\sum_{d\in L}\rho^{h_T(d)}.
\tag{TOR-11}
\]

并且

\[
\sum_{d\in L}\rho^{h_T(d)}
=\sum_{\mathcal J\subseteq\mathcal P_T}(\rho-1)^{|\mathcal J|}
\left|\bigcap_{q\in\mathcal J}\mathcal A_q\right|.
\tag{TOR-12}
\]

对固定 `J`，交集条件是有限 CRT 方程组：

\[
d\equiv -j_qr\pmod q,\qquad q\in\mathcal J,\quad 0\le j_q<m.
\tag{TOR-13}
\]

若这些交集按乘法模型分布，则 `(TOR-11)` 控制高重数尾点，从而 `(TOR-7)` 无法由重叠支付。
若某一阶交集系统显著高于模型，则存在固定尾素集合、固定点位向量或固定低模相位块的 CRT 聚集，
进入 `ColumnCRT/PDEC`。若该现象只在单个窗口出现，则进入 `SAE`。

## 4. 尾重叠三出口

结合 `(TOR-7)` 至 `(TOR-13)`，`Xi_T>0` 且 tail-mass 分支不承担缺口时，只能进入三类证书：

1. **Rankin 点态账本失败。**  
   某些点的 `h_T(d)` 超过 `(TOR-10)`。这与乘积整除直接矛盾，或由脚本证书排除。
2. **ColumnCRT 聚集。**  
   高重叠来自许多尾素在固定线性点位 `d+jr` 上同步命中；等价于 `(TOR-13)` 的交集数超过乘法模型。
3. **PDEC/SAE。**  
   若低大素幸存集 `L` 对尾 CRT 模数发生系统偏置，则进入 `PDEC`；若只在单窗出现，则进入 `SAE`。

因此 tail-overlap 不是独立黑箱；它已被压成可计算 Rankin 账本与有限 CRT 缺陷出口。

## 5. 审计脚本

对应脚本：

```text
experiments/prime_matrix_alpha_tail_tail_overlap_rankin_audit.py
```

推荐命令：

```text
python3 experiments/prime_matrix_alpha_tail_tail_overlap_rankin_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --format table
```

脚本输出 `low_count/full_count/tail_hit_sum/tail_deleted/max_tail_hits/L_bound/overlap_excess`。
其中：

```text
overlap_excess = tail_hit_sum - tail_deleted = Omega_T.
```

若 `max_tail_hits<=L_bound`，则点态乘积约束通过；若 `Xi_tail>0` 且 `overlap_excess` 很大，
则下一步必须审查 `(TOR-13)` 的交集是否形成 `ColumnCRT/PDEC`。

## 6. 审稿边界

已证明：

```text
Xi_T>0 + tail-mass 不足以解释
=> tail overlap Omega_T 必须为正；
h_T(d) 受 product Rankin 上界 L_T(z,m) 控制；
持续高重叠必表现为 finite CRT intersection excess，即 ColumnCRT/PDEC；
孤立高重叠进入 SAE。
```

尚未证明：

```text
所有 ColumnCRT/PDEC/SAE 出口均不可能；
或 Rankin 交集矩在全局参数下给出足以吸收 Xi_T 的显式常数。
```

下一步最小硬点是把 `(TOR-12)` 的交集矩展开成有限阶可验收证书，并与 `Xi_T` 缺口逐项比较。
