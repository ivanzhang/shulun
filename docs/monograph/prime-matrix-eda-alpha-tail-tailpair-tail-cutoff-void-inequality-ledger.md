# AlphaTail TailCutoffVoid 显式不等式账本

**状态：** `tail_cutoff_void_inequality_sample_closed_global_open`

本文接续 short-`q` 有限证书合同。目标是把 finite short-`q` 分支进一步压成一个显式
尺度不等式。

## 1. 充分不等式

large-`u` 分支满足

\[
u>\theta |I|,\qquad \theta=0.1.
\tag{TCV-1}
\]

固定责任区间上端为

\[
q_+=
\left\lfloor {B+j_1r\over u}\right\rfloor.
\tag{TCV-2}
\]

若

\[
{B+j_1r\over \theta |I|}\le \alpha p,
\tag{TCV-3}
\]

则由 `u>\theta|I|` 得

\[
q_+\le \left\lfloor {B+j_1r\over u}\right\rfloor
\le \lfloor \alpha p\rfloor.
\tag{TCV-4}
\]

于是由 `TailCutoffVoid` 引理，`N_g(J)=0`。

## 2. 可引用引理

**引理 TCV-1（large-`u` TailCutoffVoid 充分条件）。**  
对任意 large-`u` 责任区间，若 `(TCV-3)` 成立，则该区间不含 tail prime pair，因而不能触发
`C13` 失败。

**证明。**  
由 `(TCV-1)` 和 `(TCV-2)` 得 `(TCV-4)`。tail primes 均严格大于 `floor(alpha p)`，
所以 `J` 内没有 tail prime，进而没有 tail prime pair。□

## 3. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_tail_cutoff_void_inequality_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_tail_cutoff_void_inequality_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --endpoint-theta 0.1 --format table
```

输出摘要：

```text
large_u 12 sufficient_failures 0 tail_cutoff_failures 0
max_sufficient_ratio 0.002690
max_actual_q_ratio 0.002443
max_q_upper 22 min_tail_cutoff 9006
```

其中

\[
{\rm sufficient\_ratio}
=
{(B+j_1r)/(\theta |I|)\over \lfloor\alpha p\rfloor}.
\tag{TCV-5}
\]

样本最大值仅 `0.002690`，远小于 `1`。因此当前样本的 large-`u` 分支不需要逐候选素性证书；
它已被 `(TCV-3)` 直接排除。

## 4. 对 C13 链条的影响

`C13` 的 short-`q` 分支现在可进一步写成：

```text
Short-q branch
=> TailCutoffVoid inequality (TCV-3)
   or finite q-candidate certificate
   or persistent short-q PDEC/ColumnCRT.
```

在当前样本中第一项已全部通过。

## 5. 审稿边界

已完成：

```text
TailCutoffVoid 的显式充分不等式；
样本中 large-u 全部满足该充分不等式；
最大安全比值约 0.002690。
```

仍未完成：

```text
目标无限窗口族上 (TCV-3) 的全局证明；
或未满足 (TCV-3) 的 finite q-candidate 证书全集；
或 persistent short-q PDEC/ColumnCRT 排斥。
```

