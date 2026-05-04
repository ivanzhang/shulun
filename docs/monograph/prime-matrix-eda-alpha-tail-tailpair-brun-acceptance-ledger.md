# AlphaTail 尾素对 Brun/Selberg 验收账本

**状态：** `alpha_tail_tailpair_brun_acceptance_ledger_open`

本文把 `TailPair Brun/Selberg envelope` 变成可执行验收规则。目标是避免“常数包足够小”
停留在口头层面：每个样本或正式窗口都必须输出通过、全局常数不足、或局部 `SAE/Endpoint`
责任区间。

## 1. 两级验收

对一个窗口记

\[
G_{\rm geom}=M_2^{=,\rm geom},
\qquad
B_{\rm BS}=\sum_{g,j_1,j_2}\mathfrak S_g {|J(g,j_1,j_2)|\over\log^2 J_-}.
\tag{BAL-1}
\]

给定候选统一常数 `C_global`，全局验收为

\[
G_{\rm geom}\le C_{\rm global}B_{\rm BS}.
\tag{BAL-2}
\]

同时对每个局部区间 `J` 定义

\[
C_{\rm loc}(g,J)=
{N_g(J)\over \mathfrak S_g |J|/\log^2J_-}.
\tag{BAL-3}
\]

给定局部阈值 `C_local`，若某个 `C_loc>C_local`，则该窗口不能被普通平滑上界吸收，
必须输出具体 `(g,j_1,j_2,J)`，进入

```text
TailPairResonance-SAE / Endpoint concentration.
```

## 2. 三分结论

每个窗口只有三种合法状态：

1. **EnvelopePass.**  
   `(BAL-2)` 成立且所有局部 `C_loc<=C_local`。
2. **GlobalConstantGap.**  
   局部无尖峰，但 `(BAL-2)` 失败；说明统一 Selberg 常数包太弱。
3. **SAEEndpointCandidate.**  
   存在局部 `C_loc>C_local`；输出最坏短区间，回流 `SAE/Endpoint`。

该三分把后续工作固定为具体常数，而不是新的命题转换。

## 3. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_brun_acceptance_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_brun_acceptance_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --global-c 1.5 --local-c 1.5 --format table
```

样本中 `C_global=C_local=1.5` 可通过；这不是证明 `1.5` 全局成立，而是给出下一步
Selberg 常数包的明确目标。

## 4. 审稿边界

已证明：

```text
给定 C_global/C_local 后，每个窗口可严格分类为通过、全局常数不足或 SAE/Endpoint；
失败输出是具体短区间素对过密，不再是模糊出口。
```

尚未证明：

```text
存在全局有效的 C_global=C_local=1.5；
或所有 C_loc>1.5 的窗口可由 SAE/Endpoint 排斥。
```

下一步最小硬点是把二维 Selberg 上筛常数外向化，争取证明足够小的 `C_global`，
否则转攻局部尖峰的 `SAE/Endpoint` 排斥。
