# AlphaTail short-`q` 有限证书合同

**状态：** `short_q_finite_certificate_sample_closed_global_open`

本文接续 `C13` 二分路由定理，处理 `u>0.1|I|` 的 finite short-`q` 分支。该分支已知
`q_length<=10`，因此可以不用 Brun/Selberg 常数包，改用逐候选证书。

## 1. 证书对象

对 large-`u` 责任区间

\[
J=[q_-,q_+],\qquad |J|\le 10,
\tag{SQC-1}
\]

证书逐项列出所有整数

\[
q\in J
\tag{SQC-2}
\]

并标记：

```text
left_tail(q)  : q 是否为当前 tail prime；
right_tail(q) : q+g 是否为当前 tail prime；
pair(q)       : left_tail(q) and right_tail(q)。
```

于是

\[
N_g(J)=\sum_{q\in J}1_{\rm pair(q)}.
\tag{SQC-3}
\]

只要

\[
N_g(J)<\lfloor1.3B_g(J)\rfloor+1,
\tag{SQC-4}
\]

该 short-`q` 行就通过 `C13` 验收。

## 2. TailCutoffVoid

tail primes 的构造是：

```text
tail prime q > floor(alpha*p)。
```

因此有确定剪枝：

**引理 SQC-1（TailCutoffVoid）。**  
若

\[
q_+\le \lfloor\alpha p\rfloor,
\tag{SQC-5}
\]

则 `J` 中没有 tail prime，故 `N_g(J)=0`。

**证明。**  
`J` 中每个候选 `q<=q_+<=floor(alpha p)`，而 tail prime 必须严格大于
`floor(alpha p)`，所以 `left_tail(q)` 全为假。由 `(SQC-3)` 得 `N_g(J)=0`。□

一个可用于全局证明的充分条件是：

\[
{B+j_1r\over u}\le \alpha p.
\tag{SQC-6}
\]

若只使用 large-`u` 条件 `u>\theta |I|`，则更粗的充分条件为

\[
{B+j_1r\over \theta |I|}\le \alpha p.
\tag{SQC-7}
\]

这给出下一步可直接攻击的显式不等式：证明目标窗口族的 large-`u` 分支都满足 `(SQC-7)`，
则 finite short-`q` 分支全局清空。

## 3. 生成脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_short_q_certificate_builder.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_short_q_certificate_builder.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.3 --endpoint-theta 0.1 --format table
```

输出摘要：

```text
rows 12 positive_rows 0 failure_rows 0 all_certified True
tail_cutoff_void 12 max_candidate_count 10 max_pair_count 0
max_q_upper 22 min_tail_cutoff 9006
```

逐行证书显示：

```text
所有 large-u 行均满足 q_upper<=floor(alpha*p)；
因此全部为 TailCutoffVoid；
没有任何候选 q 是 tail prime pair；
全部 C13 certificate_pass=True。
```

## 4. 对主链的影响

`C13` 的 short-`q` 分支现在可写成：

```text
Short-q branch
=> TailCutoffVoid
   or explicit finite q-candidate certificate
   or persistent short-q PDEC/ColumnCRT.
```

样本中直接落入 `TailCutoffVoid`，因此 short-`q` 分支清空。

## 5. 审稿边界

已完成：

```text
short-q 逐候选证书格式；
TailCutoffVoid 引理；
样本 large-u 分支全部 TailCutoffVoid；
样本 short-q 分支全部 certificate_pass。
```

仍未完成：

```text
全局证明 large-u 分支满足 TailCutoffVoid 条件；
或生成全局 finite q-candidate 证书全集；
或排斥 persistent short-q PDEC/ColumnCRT。
```

