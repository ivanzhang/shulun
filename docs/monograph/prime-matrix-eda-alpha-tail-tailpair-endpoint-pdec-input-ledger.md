# AlphaTail 端点持久键的 PDEC 输入包

**状态：** `alpha_tail_endpoint_pdec_input_ready_threshold_open`

本文接续端点相位持久性账本。目标是把每个 `persistent endpoint phase key`
转成可交给 `H4-PDEC` 模板的输入行，并明确仍缺什么上界证书。

## 1. 输入行

端点持久账本给出

\[
K=(g,j_1,j_2,u,\operatorname{side}),
\]

窗口支撑集合

\[
S_K=\{w:\exists e\in Ept(w),\ \mathcal K(e)=K\},
\tag{EPI-1}
\]

和超额质量

\[
M_K=
\sum_{\mathcal K(e)=K}
\bigl(A_g(J_e)-C_{\rm local}B_g(J_e)\bigr)_+.
\tag{EPI-2}
\]

每条 PDEC 输入行记录：

```text
key                  : K=(g,j1,j2,u,side);
bad_window_set       : S_K;
phase_map            : endpoint_phase_key;
lower_mass_source    : local Brun/Selberg positive excess;
pdec_lower_input     : M_K;
missing_upper_bound  : prove U_CRT(K)<L_PDEC(K).
```

这不是 `PDEC-Cert` 的完成版，因为尚未给出同一坏窗集合上的 `Q,F,kappa,||F||_2`
和对偶上界 `U_CRT`。

## 2. 输入充分性引理

**引理 EPI-1（持久端点键给出 PDEC 输入）。**  
若端点键 `K` 满足持久阈值，则 `K` 与 `S_K,M_K` 是合法的
`Directed Endpoint CRTDefect/PDEC` 输入对象。

**证明。**  
持久阈值保证同一线性端点映射

\[
d=qu-j_1r
\]

在同一短差值形状 `(g,j1,j2,u)` 和同一端点方向 `side` 上重复产生正超额。
因此 `S_K` 是同一相位机制生成的坏窗集合，不是混合口径集合；`M_K` 是该集合上的
非负质量下界。由 `Directed Endpoint CRTDefect` 桥，持续端点偏差必须登记为
端点 CRT 缺陷输入。□

## 3. 尚需的 PDEC 阈值比较

要把输入行升级为排斥证书，必须补齐：

1. 周期 `Q_K` 与相位映射
   \[
   \tau_K:S_K\to\mathbb Z/Q_K\mathbb Z;
   \]
2. 零均值测试函数 `F_K` 和阈值 `kappa_K`，满足
   \[
   \Re F_K(\tau_K(w))\ge\kappa_K
   \quad(w\in S_K);
   \]
3. 由同一 `S_K` 的结构约束推出的上界
   \[
   U_{\rm CRT}(K)<L_{\rm PDEC}(K).
   \]

其中

\[
L_{\rm PDEC}(K)
=
\frac{\kappa_K |S_K|}
{\sqrt{Q_K-1}\|F_K\|_2}.
\tag{EPI-3}
\]

没有 `U_CRT<L_PDEC`，只能说进入命名出口，不能说矛盾已经排出。

## 4. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_endpoint_pdec_input_ledger.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_pdec_input_ledger.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 --format table
```

样本摘要：

```text
endpoint_spikes=41, key_count=27,
persistent_key_count=14, sae_key_count=13,
persistent_total_excess=169.647458,
sae_total_excess=64.280293.
```

这些数说明：当前样本中主要端点超额已经集中到少数持久键，下一步不是继续粗分尖峰，
而是为这些 `K` 构造同一相位集合上的 `PDEC` 上界证书。

## 5. 审稿边界

已完成：

```text
persistent endpoint key -> PDEC input row；
SAE key -> finite SAE/summable SAE obligation；
每行保留 bad_window_set、lower_mass_source 与缺失上界字段。
```

未完成：

```text
Q_K,tau_K,F_K,kappa_K 的显式构造；
同一 S_K 上的 U_CRT(K) 上界；
严格余量 U_CRT(K)<L_PDEC(K)。
```

因此本文把端点持久分支压缩为阈值比较硬点，但没有排斥该分支。
