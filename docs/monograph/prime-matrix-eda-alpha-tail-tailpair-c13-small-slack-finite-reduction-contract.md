# AlphaTail `C13` 小余量窗口有限化归约合同

**状态：** `small_slack_finite_reduction_sample_closed_generator_open`

本文把前向源槽付款分成两个互斥出口：

```text
LargeSlackExit:
  Allow(W) >= K * sum_m 2*C(m,3)；

SmallSlackFiniteExit:
  Allow(W) < K * sum_m 2*C(m,3)，且 W 被列入有限源槽证书表。
```

这样 `SkeletonCountBound` 不再需要逐窗口混合处理。大余量窗口由纯组合上界自动付款；
小余量窗口必须进入显式有限表，并由 `SmallSlackSourceCertificate` 逐项证明。

## 1. 合同命题

令

\[
S_{\rm slot}(M)=\sum_{m\in M}2\binom m3.
\tag{SSFR-1}
\]

在当前 `M={4,5}`、`K=8` 下，

\[
K S_{\rm slot}=8(2\binom43+2\binom53)=224.
\tag{SSFR-2}
\]

若窗口满足

\[
Allow(W)\ge224,
\tag{SSFR-3}
\]

则 `SourceSlotStructural` 的粗前向槽上界直接给出 `ActiveClassBound`。
若 `(SSFR-3)` 失败，则该窗口必须进入有限表 `F_small`，并由源槽枚举证明

\[
T_{\rm active}(W)\le Allow(W)/K.
\tag{SSFR-4}
\]

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_small_slack_finite_reduction_contract.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_small_slack_finite_reduction_contract.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --format table
```

## 3. 当前样本结果

```text
windows=2；
large_slack_windows=1；
small_slack_windows=1；
finite_exit_windows=2；
all_pass=True；
enumeration_matches_ap=True；
lowp_excluded={(997,4096,-36)}；
min_source_margin=8.340921。
```

有限小余量表为：

```text
F_small = {(p,B,r)=(5003,8192,-36)}。
```

其中 `p=997` 不进入高 `P` 小余量链；它由当前默认 `finite-p-cut=1000`
路由到低 `P` 有限证书系统。

逐窗口：

```text
p=5003:
  Allow=106.727367<224；
  active_sources=5；
  source_budget=13.340921；
  source_margin=8.340921；
  SmallSlackFiniteExit=True。

p=10007:
  Allow=1279.236350>=224；
  LargeSlackExit=True。
```

## 4. 全局剩余

该归约没有证明完整目标族已经闭合；它把全局剩余改写为一个更具体的生成器义务：

```text
SSFR-G1: 证明完整高 P 目标族中所有 Allow(W)<224 的窗口都落入有限集合 F_small；
SSFR-G2: 对 F_small 中每个窗口提交 SmallSlackSourceCertificate；
SSFR-G3: 对 Allow(W)>=224 的窗口使用 LargeSlackExit 自动付款。
SSFR-G4: 对 p<=P_fin 的窗口使用低 P 有限证书系统，不混入高 P 小余量链。
```

当前样本已满足 `SSFR-G2/G3`。未完成的是 `SSFR-G1`，即目标族生成器必须证明
不会产生新的小余量窗口，或把它们全部列入有限证书表。
