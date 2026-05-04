# AlphaTail `C13` 端点失败见证障碍

**状态：** `c13_witness_barrier_no_loss_exits_open`

本文继续压缩 `C13` 端点分支。上一层定义整数失败质量
`mu_13=max(0,1-slack)`；本文把该质量进一步物化为具体尾素对见证。这样，任何
`C13` 端点失败都不能停留在“局部常数超标”的抽象表述，必须交出明确的
`(q,q+g)` 尾素对。

## 1. 尾素对见证集

固定 gap 责任区间 `J=[q_-,q_+]`，定义

\[
\mathcal P_g(J)
=
\{q\in J:q,\ q+g\text{ 均为 tail prime}\}.
\tag{CWB-1}
\]

于是

\[
N_g(J)=|\mathcal P_g(J)|.
\tag{CWB-2}
\]

令

\[
T_{13}(J)=\lfloor1.3B_g(J)\rfloor+1.
\tag{CWB-3}
\]

若 `J` 失败，则 `N_g(J)>=T_13(J)`，并定义超额见证数

\[
e_{13}(J)=N_g(J)-T_{13}(J)+1=\mu_{13}(J).
\tag{CWB-4}
\]

从 `P_g(J)` 中按端点方向取最靠近端点的 `e_13(J)` 个元素，得到规范见证集

\[
\mathcal W_{13}(J)\subset \mathcal P_g(J),
\qquad
|\mathcal W_{13}(J)|=e_{13}(J).
\tag{CWB-5}
\]

## 2. 无损见证定理

**定理 CWB-1（C13 失败的尾素对见证障碍）。**  
若端点责任区间 `J` 触发 `C13` 失败，则存在规范见证集 `W_13(J)`，且删除这些见证后
整数余量恢复为正：

\[
N_g(J)-|\mathcal W_{13}(J)|
=T_{13}(J)-1.
\tag{CWB-6}
\]

因此任何 `C13` 失败都等价地给出至少一个明确尾素对见证

\[
(q,q+g),\qquad q,q+g\text{ 均为 tail prime}.
\tag{CWB-7}
\]

**证明。**  
由 `(CWB-2)`，`N_g(J)` 就是见证集 `P_g(J)` 的基数。失败条件给出
`N_g(J)>=T_13(J)`，故 `e_13=N_g-T_13+1>=1`。从有限集合 `P_g(J)` 中取任意
`e_13` 个元素，特别是按端点方向取规范子集，得到 `(CWB-5)`。删除后剩余
`N_g-e_13=T_13-1`，正好低于失败门槛一票，故整数余量为 `1`。□

## 3. 出口强化

本文把上一层出口改写为：

```text
C13 endpoint failure
=> concrete witness pairs (q,q+g)
=> if same key/witness phase persists: PairPhase-PDEC/ColumnCRT
=> if isolated: SAE witness row.
```

这比只登记端点键更强，因为 `PDEC/SAE` 输入现在必须保留：

```text
gap g；
point indices j1,j2；
multiplier u；
endpoint side；
witness pair q,q+g；
d=qu-j1*r 的端点相位。
```

因此 persistent 分支不再是一个松散的“端点过密”事件，而是同一端点相位下固定差值尾素对
反复出现。

具体相位输入格式与同商数锁定恒等式已在
`prime-matrix-eda-alpha-tail-tailpair-c13-witness-phase-ledger.md` 中物化：每个见证原子
携带 `Q_pair=q(q+g)`、`tau_pair=d mod Q_pair` 和端点深度 `depth`。

## 4. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_witness_barrier.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_witness_barrier.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.3 --slack-cut 40 --format table
```

输出摘要：

```text
records 123 failures 0 failure_mass 0 identity_failures 0
min_extra_to_failure 1 max_required_C 1.292474
```

其中 `identity_failures=0` 核验了 `actual=|P_g(J)|` 的见证计数恒等式。样本中
`C13` 端点失败见证集为空；最紧记录距离失败只差一个额外尾素对。

压力测试口径下，若把局部常数临时降为 `1.2`，同一脚本输出
`failures=57, failure_mass=281, identity_failures=0`，说明见证抽取会在真实失败时
输出具体 `(q,q+g)` 原子，而不是只对空失败样本成立。

## 5. 当前最窄剩余

已完成：

```text
C13 失败质量被物化为具体尾素对见证；
删除见证后整数余量严格恢复为 1；
样本 C13 见证失败集合为空；
最紧样本的 extra_to_failure=1；
见证原子已可接入相位/PDEC 输入账本。
```

仍未完成：

```text
全局证明端点责任区间中不存在 W_13；
或证明 persistent witness phase 被 PairPhase-PDEC/ColumnCRT 排斥；
或把 isolated witness 全部提交为 SAE witness row。
```

所以本文继续收窄了行命题链条中的 `C13` 出口，但仍不是行命题的最终无条件闭合。
