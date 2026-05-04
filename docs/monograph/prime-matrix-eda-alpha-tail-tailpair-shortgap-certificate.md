# AlphaTail 短差值尾素对容量证书

**状态：** `alpha_tail_tailpair_shortgap_certificate_open`

本文给 `TailPairResonance budget` 补上第一版可验收容量证书。核心点是：等乘数共振只依赖有限
gap 集 `G_r(m)`，所以在固定窗口内可以精确计数；在全局证明中，该精确计数可替换为
Brun/Selberg 固定差值素对上界。

## 1. 允许 gap 集

由等乘数方程

\[
u(q_1-q_2)=(j_1-j_2)r
\tag{TSC-1}
\]

可得允许正 gap：

\[
G_r(m)=
\left\{{|j r|\over u}:\ 1\le j<m,\ u\mid jr\right\}.
\tag{TSC-2}
\]

这是完全显式的有限集合。对 `m<=5`，它通常只含少量短差值，如 `|r|,2|r|,|r|/2,...`。

## 2. 固定窗口精确证书

令 `P_T` 是当前条件尾素集合。定义

\[
N_g=\#\{q\in P_T:\ q+g\in P_T\}.
\tag{TSC-3}
\]

旧版使用粗系数 `m^2`。现在可精确到有向点位差。对每个 gap 定义

\[
C_{g,m}(r)=
\#\{(j_1,j_2):0\le j_1,j_2<m,\ j_1\ne j_2,
-(j_1-j_2)r>0,\ g\mid -(j_1-j_2)r\}.
\tag{TSC-4}
\]

这里 `q<q+g`，所以只有满足 `-(j_1-j_2)r>0` 的有向点位对能产生正乘数

\[
u={-(j_1-j_2)r\over g}.
\tag{TSC-5}
\]

对固定 `q,q+g` 与固定有向点位对，候选 `d` 至多一个：

\[
d=qu-j_1r.
\tag{TSC-6}
\]

因此得到精确系数容量

\[
M_2^=
\le
\sum_{g\in G_r(m)}C_{g,m}(r)N_g.
\tag{TSC-7}
\]

这是对旧粗界

\[
M_2^=
\le
m^2\sum_{g\in G_r(m)}N_g.
\tag{TSC-8}
\]

的严格改进，且不使用任何概率模型。若 `M_2^=` 接近该上界，说明尾重叠几乎完全由短差值
素对共振解释；若上界远小于 tail-overlap 缺口，则剩余必须进入非共振 `correlation-PDEC`。

## 3. 全局 Brun/Selberg 接口

全局化时，对每个固定 `g` 使用二维上界筛：

\[
N_g(X;Y,Z)
\le
C_2(g)\,{X\over \log^2 X}
 + {\rm endpoint}(g,Y,Z),
\tag{TSC-9}
\]

其中 `C_2(g)` 是显式奇异级数上界，端点误差必须按同一尾素区间 `[Y,Z]` 外向控制。
这只是上界筛方向，不涉及素数对存在性，因此不触碰 parity barrier。

代入 `(TSC-7)` 得到

\[
M_2^=
\le
\sum_{g\in G_r(m)}
C_{g,m}(r)
\left(C_2(g){X\over\log^2X}+{\rm endpoint}_g\right).
\tag{TSC-10}
\]

若 `(TSC-6)` 小于必须支付的 overlap 缺口，等乘数共振分支关闭；否则它成为明确的
`TailPairResonance` 出口，而不是未定义的 PDEC。

## 4. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_shortgap_certificate_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_shortgap_certificate_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --format table
```

输出 `gap_count/pair_count/exact_upper/coarse_upper/equal_actual/upper_pass`。
`top_gap_counts` 的格式为 `gap:pairs/coefficient/capacity`。

## 5. 审稿边界

已证明：

```text
固定窗口内 M2_equal <= sum_g C_{g,m}(r) N_g；
N_g 可由脚本精确计数；
全局版本只需要固定差值素对的 Brun/Selberg 上界。
```

尚未证明：

```text
全局 Brun/Selberg 常数足以吸收所有 TailPairResonance；
或 TailPairResonance 出口可由 SAE/Endpoint 排斥。
```

下一步最小硬点是把 `(TSC-5)` 的常数包显式化，并与 `Xi_T` 缺口同口径比较。
