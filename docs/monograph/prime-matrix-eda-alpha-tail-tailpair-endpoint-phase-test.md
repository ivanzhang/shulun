# AlphaTail 端点持久键的显式相位测试函数

**状态：** `alpha_tail_endpoint_phase_test_explicit_U_CRT_open`

本文补齐端点 PDEC 输入包中的 `F_K,kappa_K,L_PDEC(K)` 构造。剩余缺口被进一步压缩为同一
相位集合上的上界

```text
U_CRT(K) < L_PDEC(K).
```

## 1. 端点相位群

固定低模周期 `Q>=2`。对端点尖峰原子 `e` 的责任区间

\[
D_e=[D^-_e,D^+_e]\subset I_m
\]

定义端点相位

\[
\tau_Q(e)=
(D^-_e\bmod Q,\ D^+_e\bmod Q)
\in
G_Q:=(\mathbb Z/Q\mathbb Z)^2.
\tag{EPT-1}
\]

这里用的是原始 `d` 端点，而不是尾素对变量 `q` 端点；这与
`Directed Endpoint CRTDefect` 的端点 sawtooth 输入一致。

## 2. 观测相位指示测试函数

对持久键 `K`，令

\[
T_K(Q)=\{\tau_Q(e):\mathcal K(e)=K\}
\subset G_Q,
\tag{EPT-2}
\]

\[
\delta_K={|T_K(Q)|\over |G_Q|}={|T_K(Q)|\over Q^2}.
\tag{EPT-3}
\]

定义零均值测试函数

\[
F_{K,Q}(t)=1_{T_K(Q)}(t)-\delta_K.
\tag{EPT-4}
\]

则

\[
\sum_{t\in G_Q}F_{K,Q}(t)=0.
\tag{EPT-5}
\]

对所有观测端点原子 `e`，有

\[
F_{K,Q}(\tau_Q(e))=1-\delta_K=:\kappa_{K,Q}>0,
\tag{EPT-6}
\]

只要 `T_K(Q)` 不是整个相位群。

## 3. 显式范数与下界

`F_{K,Q}` 的未归一化 `L2` 范数为

\[
\|F_{K,Q}\|_2^2
=
|T_K|(1-\delta_K)^2+(Q^2-|T_K|)\delta_K^2.
\tag{EPT-7}
\]

记持久键的端点超额质量为

\[
M_K=\sum_{\mathcal K(e)=K}
\bigl(A_g(J_e)-C_{\rm local}B_g(J_e)\bigr)_+.
\tag{EPT-8}
\]

用带权版本的 PDEC 下界得到

\[
L_{\rm PDEC}(K,Q)=
{ \kappa_{K,Q}M_K
\over
\sqrt{Q^2-1}\,\|F_{K,Q}\|_2 }.
\tag{EPT-9}
\]

因此 `F_K,kappa_K,L_PDEC` 已显式化；排斥该键只剩证明同一坏窗集合上的
`U_CRT(K,Q)` 严格小于 `(EPT-9)`。

## 4. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_endpoint_phase_test_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_phase_test_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 \
  --phase-modulus 210 --format table
```

样本结论：

```text
全部 14 个持久键均得到 EXPLICIT_F_K_READY_U_CRT_OPEN；
每键 phase_count=2, phase_density=2/210^2；
最大 weighted_L_PDEC=0.09683839。
```

这说明当前端点硬点已经从“找不到测试函数”压缩为“证明端点 CRT 上界小于显式下界”。

## 5. 审稿边界

已完成：

```text
相位群 G_Q=(Z/QZ)^2；
端点相位 tau_Q=(D^- mod Q,D^+ mod Q)；
零均值测试函数 F_{K,Q}=1_T-|T|/Q^2；
kappa、L2 范数与 weighted L_PDEC 显式公式。
```

未完成：

```text
选择全局有效的 Q；
证明同一 S_K 上的 U_CRT(K,Q) 上界；
核验 U_CRT(K,Q)<L_PDEC(K,Q)；
将失败情形回流到 SAE、Rankin low-mod spike 或 tail-anchor。
```

所以本文完成的是 PDEC 下界侧与测试函数侧，不是 PDEC 排斥。
