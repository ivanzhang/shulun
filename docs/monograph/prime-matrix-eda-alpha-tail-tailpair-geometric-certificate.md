# AlphaTail 尾素对共振几何截断证书

**状态：** `alpha_tail_tailpair_geometric_certificate_open`

前一节把 `M2_equal` 上界从 `m^2` 粗系数收紧到精确有向点位系数 `C_{g,m}`。
但该上界仍把所有尾素对 `q,q+g` 都计入；事实上，对固定点位和乘数，候选起点 `d`
是唯一的，必须落在当前窗口 `I_m` 内。这给出更强的几何截断。

## 1. 候选点唯一性

固定 `q<q+g` 与有向点位 `(j_1,j_2)`。若等乘数共振发生，则

\[
d+j_1r=qu,\qquad d+j_2r=(q+g)u,
\tag{TGC-1}
\]

其中

\[
u={-(j_1-j_2)r\over g}.
\tag{TGC-2}
\]

因此候选点唯一：

\[
d(q,g,j_1,j_2)=qu-j_1r.
\tag{TGC-3}
\]

若 `d` 不在起点窗口 `I_m` 中，该尾素对不可能贡献 `M2_equal`。

## 2. 几何截断容量

定义

\[
N^{\rm geom}_{g,j_1,j_2}
=
\#\{q\in P_T:q+g\in P_T,\ d(q,g,j_1,j_2)\in I_m\}.
\tag{TGC-4}
\]

则

\[
M_2^=
\le
\sum_{g\in G_r(m)}
\sum_{(j_1,j_2)\in C_g}
N^{\rm geom}_{g,j_1,j_2}.
\tag{TGC-5}
\]

若进一步要求候选 `d` 已在低大素幸存集 `L` 中，得到有限窗口精确计数

\[
M_2^=
\sum_{g,j_1,j_2}
N^{L}_{g,j_1,j_2},
\tag{TGC-6}
\]

其中 `N^L` 只计 `d in L`。`(TGC-6)` 是有限审计等式；全局证明可使用 `(TGC-5)`，
再用固定差值素对上界控制其中的短区间素对数。

## 3. 审计意义

该截断把全尾区间的短差值素对计数，压成若干由

\[
q\in \left[{I_m^-+j_1r\over u},{I_m^++j_1r\over u}\right]
\tag{TGC-7}
\]

给出的短 `q` 区间。乘数 `u` 越大，区间越短；因此高 `u` 的共振容量自然衰减。
这正是尾素对补洞能力的几何刚性。

## 4. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_geometric_certificate_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_geometric_certificate_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --format table
```

输出 `geometric_upper/low_survivor_exact/equal_actual`。`low_survivor_exact` 应与实际
`M2_equal` 一致；`geometric_upper` 是不使用低幸存筛的纯几何上界。

## 5. 审稿边界

已证明：

```text
固定 q,g,j1,j2 的等乘数共振候选 d 唯一；
d 必须落入 I_m；
因此 M2_equal 受几何截断短区间素对数控制。
```

尚未证明：

```text
全局几何截断 Brun/Selberg 常数足以吸收 TailPairResonance；
或几何截断仍过大时必触发 SAE/Endpoint。
```

下一步最小硬点是把 `(TGC-7)` 的短区间固定差值素对上界写成统一常数包。
