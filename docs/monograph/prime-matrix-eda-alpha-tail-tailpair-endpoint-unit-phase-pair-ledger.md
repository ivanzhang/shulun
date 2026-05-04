# AlphaTail 单位乘数截断的双端相位账本

**状态：** `endpoint_unit_phase_pair_sae_pdec_ledger_open`

本文修正并加强 `UnitEndpointTruncation` 的审稿口径：单位乘数全窗口截断的精确端点相位必须是

```text
(L_w mod Q, R_w mod Q)
```

而不是单独左端或右端相位。该修正防止把同右端、不同左端的窗口误合并。

## 1. 双端相位键

当 `u=1` 时，前文已证明

\[
D=I_m=[L_w,R_w].
\]

因此自然的端点相位键为

\[
\Phi_Q(w)=(L_w\bmod Q,\ R_w\bmod Q).
\tag{EUP-1}
\]

对一个单位截断原子，定义完整键：

```text
(side, gap, j1, j2, Phi_Q(w)).
```

若该键有限出现，则进入 SAE；若该键持久正超额，则进入
`UnitPhasePair/PDEC`。

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_endpoint_unit_phase_pair_ledger.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_unit_phase_pair_ledger.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 \
  --phase-modulus 210 --format table
```

样本摘要：

```text
records=26,
keys=26,
total_excess=177.008191,
UnitPhasePair/SAE: count=26。
```

即使使用双端相位，样本中每个单位截断相位键仍只出现一次。

## 3. 对上一层账本的修正

上一层 `endpoint_unit_truncation_ledger` 使用的是单端 `phase_value`。该口径可以作为粗诊断，
但正式 SAE/PDEC 二分必须使用 `(L mod Q,R mod Q)`。

本文给出正式口径，并保留同一结论：

```text
当前样本的 u=1 全窗口截断项全部进入 SAE。
```

## 4. 引理：双端相位 SAE/PDEC 二分

**引理 EUP-1（双端相位二分）。**  
对 `u=1` 且 `D=I_m` 的端点尖峰，若完整键

\[
(g,j_1,j_2,L_w\bmod Q,R_w\bmod Q)
\]

有限出现，则该键贡献进入 SAE；若该键在无限窗口族中持久出现且正超额不可求和，则触发
`UnitPhasePair/PDEC`。

**证明。**  
`u=1` 时责任区间完全等于窗口 `I_m`，所以全部端点相位信息由 `(L_w,R_w)` 决定。若完整键
不复现，就不存在同一端点 CRT 相位上的累积偏差；若完整键持久复现并产生不可求和正超额，
则正是端点相位持久缺陷，按 PDEC 定义登记。□

## 5. 下一步硬点

当前样本层面，OneSided 主分支已经被降为精确双端相位 SAE。全局仍需：

```text
证明 UnitPhasePair 键全局可求和；
或排斥持久 UnitPhasePair/PDEC。
```

## 6. 审稿边界

已完成：

```text
单位截断的正式双端相位键；
样本 26 个单位截断项全部 SAE；
修正单端相位口径的潜在混合风险。
```

未完成：

```text
无限窗口族 UnitPhasePair 键的可求和证明；
持久 UnitPhasePair/PDEC 的排斥证书。
```
