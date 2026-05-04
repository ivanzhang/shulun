# AlphaTail 尾素对端点相位持久性账本

**状态：** `alpha_tail_tailpair_endpoint_persistence_ledger_open`

本文补足 `EndpointSpike -> Directed Endpoint CRTDefect` 桥中的审稿账本层。它不排斥
端点缺陷；它把每个端点尖峰无损分成两类：

```text
persistent endpoint phase key  -> Directed Endpoint CRTDefect/PDEC；
finite or nonpersistent key    -> SAE ledger。
```

因此本文闭合的是“端点尖峰如何登记、如何二分、如何进入下一出口”，不是行命题终局。

## 1. 原子端点记录

对一个窗口

\[
w=(p,B,r,m)
\]

和局部常数 `C_local`，`TailPairLocalSpike` 脚本给出端点尖峰原子

\[
e=(g,j_1,j_2,u,J,D,A_g(J),B_g(J)).
\tag{TPL-1}
\]

其中几何责任区间满足

\[
d=qu-j_1r,\qquad
D=[uJ^- - j_1r,\ uJ^+ - j_1r]\subset I_m.
\tag{TPL-2}
\]

若 `D` 距离 `I_m` 左端、右端或双端不超过 `theta |I_m|`，记

\[
\operatorname{side}(e)\in\{L,R,B\}.
\tag{TPL-3}
\]

定义端点相位键

\[
\mathcal K(e)=(g,j_1,j_2,u,\operatorname{side}(e)).
\tag{TPL-4}
\]

`K` 不含 `p,B,r,m`，因为这些量是窗口尺度；`K` 只记录造成端点尖峰的局部短差值
形状和端点方向。

## 2. 持久性账本

令 `W` 是待审计窗口族，令 `Ept(W)` 是其中全部端点尖峰。对每个相位键 `K` 定义

\[
N_K(W)=|\{e\in Ept(W):\mathcal K(e)=K\}|,
\tag{TPL-5}
\]

\[
S_K(W)=|\{w:e\in Ept(w),\ \mathcal K(e)=K\}|,
\tag{TPL-6}
\]

以及正超额

\[
\mathcal E_K(W)=
\sum_{\mathcal K(e)=K}
\bigl(A_g(J_e)-C_{\rm local}B_g(J_e)\bigr)_+.
\tag{TPL-7}
\]

给定审稿阈值

\[
\nu_0\ge 2,\qquad \Lambda_0>0,
\tag{TPL-8}
\]

若

\[
S_K(W)\ge \nu_0
\quad\text{or}\quad
\mathcal E_K(W)\ge\Lambda_0,
\tag{TPL-9}
\]

则把 `K` 登记为 `persistent`；否则登记为 `SAE`。

## 3. 无损二分引理

**引理 TPL-1（端点账本无损分解）。**  
对任意有限窗口族 `W`，所有端点尖峰按 `K` 唯一分组，并且

\[
\sum_{e\in Ept(W)}
\bigl(A_g(J_e)-C_{\rm local}B_g(J_e)\bigr)_+
=
\sum_K \mathcal E_K(W).
\tag{TPL-10}
\]

每个 `K` 恰好落入 `persistent` 或 `SAE` 一类。

**证明。**  
`K(e)` 由 `(g,j1,j2,u,side)` 确定，故每个原子端点记录只有一个键。按键分组只是对
有限集合 `Ept(W)` 做不交并分解，所以正超额求和保持等式。最后由阈值判定
`TPL-9` 及其否定给出二分。□

**引理 TPL-2（持久键出口）。**  
若某键 `K` 被登记为 `persistent`，则该键给出 `Directed Endpoint CRTDefect/PDEC`
输入；若登记为 `SAE`，则其贡献进入有限异常账本。

**证明。**  
`persistent` 意味着同一 `(g,j1,j2,u,side)` 在多个证书窗口或以大超额反复出现。由
`TPL-2`，每次超额都来自同一线性端点映射 `d=qu-j1 r` 贴住同一端点方向；这正是
`prime-matrix-directed-endpoint-crtdefect-bridge.md` 中有向端点缺陷的相位块输入。
若不满足持久阈值，则该键在当前有限审计族中只留下有限个孤立记录，按 SAE 账本列项吸收。
□

## 4. 全局使用边界

对增长窗口族 `W_T`，本文只给出如下条件化出口：

```text
若端点超额不能由 SAE 总量吸收，
并且相位键宇宙在所选归一化下不能无限稀释，
则鸽巢推出某个 persistent K，
从而进入 Directed Endpoint CRTDefect/PDEC。
```

因此全局闭合还需要二选一：

1. 证明所有 `persistent K` 被 `Directed Endpoint CRTDefect/PDEC` 排斥；
2. 或证明所有非持久键的 SAE 总量满足全局可求和上界。

这正是下一层最窄硬点。

## 5. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 --format table
```

样本账本给出：

```text
endpoint_spikes=41, key_count=27,
persistent_key_count=14, sae_key_count=13,
max_key_count=2, max_key_excess=28.759861,
side_counts=B:41.
```

解释：

```text
当前样本的端点尖峰全部为双端 B；
超过持久阈值的键进入 DirectedEndpointCRTDefect/PDEC；
只出现一次且超额未超过阈值的键进入 SAE。
```

## 6. 审稿边界

已完成：

```text
EndpointSpike 的跨窗口相位键账本；
持久键与 SAE 键的无损二分；
persistent => Directed Endpoint CRTDefect/PDEC 的接口；
nonpersistent => SAE 的有限账本接口。
```

未完成：

```text
Directed Endpoint CRTDefect/PDEC 的全局排斥；
非持久键在无限窗口族中的全局可求和 SAE 上界；
Brun/Selberg 固定差值素对常数包的无条件 C_BS<=1.5 证明。
```

所以本文是行命题闭合链条中的端点账本补强，不是行命题的最终无条件证明。
