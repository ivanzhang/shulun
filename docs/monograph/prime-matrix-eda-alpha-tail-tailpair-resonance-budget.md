# AlphaTail 二阶尾素对共振预算

**状态：** `alpha_tail_tailpair_resonance_budget_open`

本文把二阶交集矩 `M_2` 拆成结构共振预算与非共振预算。目标是进一步缩小
tail-overlap 的真正 PDEC 输入：只有非共振剩余需要低模 Fourier 排斥，等乘数共振应由
短差值尾素对容量或 `SAE` 处理。

## 1. 二阶交集的乘数分解

每个二阶尾命中由数据

\[
(d;q_1,q_2;j_1,j_2;u_1,u_2)
\tag{TRB-1}
\]

给出，其中

\[
d+j_1r=q_1u_1,\qquad d+j_2r=q_2u_2.
\tag{TRB-2}
\]

定义

\[
M_2^{=}:=\#\{(TRB\text{-}1):u_1=u_2\},
\qquad
M_2^{\ne}:=M_2-M_2^{=}.
\tag{TRB-3}
\]

`M_2^=` 是等乘数共振预算；`M_2^ne` 是非共振尾交集。

## 2. 等乘数支的短差值锁定

若 `u_1=u_2=u`，则 `(TRB-2)` 相减给出

\[
u(q_1-q_2)=(j_1-j_2)r.
\tag{TRB-4}
\]

因此等乘数支只可能出现在有限短差值尾素对上：

\[
q_2-q_1={-(j_1-j_2)r\over u}.
\tag{TRB-5}
\]

特别地，单位乘数 `u=1` 给出上一节的 `q_2-q_1=|r|` 主峰。更一般地，
`u` 必须整除 `(j_1-j_2)r`，而 `|j_1-j_2|<m`，所以每个点位差只产生有限个
可列举 gap。

## 3. 预算不等式

令 `G_r(m)` 为由 `(TRB-5)` 允许的正 gap 集合：

\[
G_r(m)=
\left\{ {|(j_1-j_2)r|\over u}:
0\le j_1,j_2<m,\ j_1\ne j_2,\ u\mid (j_1-j_2)r
\right\}.
\tag{TRB-6}
\]

则

\[
M_2^=
\le
\sum_{g\in G_r(m)}
\sum_{\substack{q,q+g\in\mathcal P_T}}
C_{g,m}(q),
\tag{TRB-7}
\]

其中 `C_{g,m}(q)` 是由点位差和可行乘数决定的有限边界系数，满足粗上界

\[
C_{g,m}(q)\le m^2.
\tag{TRB-8}
\]

所以保守容量为

\[
M_2^=
\le
m^2\sum_{g\in G_r(m)}
\#\{q\in\mathcal P_T:q+g\in\mathcal P_T\}.
\tag{TRB-9}
\]

该不等式把共振预算转成固定短差值的尾素对计数。若 `(TRB-9)` 足以覆盖观测到的
`M_2`，则 tail-overlap 主因是 `TailPairResonance`；若不足，剩余

\[
M_2^{\ne}
\tag{TRB-10}
\]

必须进入 `correlation-PDEC` 或 `SAE`。

## 4. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_resonance_budget_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_resonance_budget_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --format table
```

输出 `M2/equal_multiplier/non_equal/unit`，并给出二阶模型 `B2` 与偏差 `D2`。

## 5. 审稿边界

已证明：

```text
M2 = M2_equal + M2_non_equal；
M2_equal 只来自有限短差值尾素对 gap 集；
M2_equal <= m^2 * sum_g #{q,q+g in P_T}。
```

尚未证明：

```text
该短差值尾素对容量全局不足以支付 Xi_T；
或容量过大时必进入 TailPairResonance/SAE 并可排斥。
```

下一步最小硬点是给 `(TRB-9)` 配显式 Brun/Selberg 上界或窗口内有限证书。
