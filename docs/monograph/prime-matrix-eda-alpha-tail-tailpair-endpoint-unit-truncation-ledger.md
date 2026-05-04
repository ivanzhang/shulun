# AlphaTail 单位乘数全窗口截断 SAE/PDEC 账本

**状态：** `endpoint_unit_truncation_sae_pdec_ledger_open`

本文接续单位乘数右边界恒等式。进一步审计发现：当 `u=1` 时，不只是右端点满足
`D^+=R_w`，左端点也满足 `D^-=L_w`。因此责任区间实际为整个窗口

```text
D=I_m。
```

这把该分支从“右边界钉扎”进一步压缩为“单位乘数全窗口截断”。

## 1. 全窗口恒等式

责任区间由

\[
d=qu-j_1r
\]

生成。`q` 区间为

\[
q^-
=
\left\lceil {L_w+j_1r\over u}\right\rceil,
\qquad
q^+
=
\left\lfloor {R_w+j_1r\over u}\right\rfloor.
\]

当 `u=1` 时，

\[
q^-=L_w+j_1r,\qquad q^+=R_w+j_1r.
\]

代回得

\[
D^- = q^- - j_1r=L_w,\qquad
D^+ = q^+ - j_1r=R_w.
\tag{EUT-1}
\]

所以

\[
D=I_m.
\tag{EUT-2}
\]

这说明 `u=1` 端点尖峰不是内部短区间局部尖峰，而是全窗口截断项。

## 2. 精确端点相位账本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_endpoint_unit_truncation_ledger.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_unit_truncation_ledger.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 \
  --phase-modulus 210 --format table
```

样本摘要：

```text
records=26,
keys=26,
total_excess=177.008191,
UnitEndpointTruncation/SAE: count=26。
```

解释：

```text
若端点相位键包含精确边界相位，
样本中的 u=1 全窗口截断项全部只出现一次；
因此在当前有限样本族中应记为 SAE，而不是 persistent PDEC。
```

## 3. 与上一层主列核的关系

上一层主列核

```text
D^+==4 mod210,
excess=69.927274
```

在本文口径下属于 `u=1` 全窗口截断的一个子族。其“列残基锁相”来自窗口端点相位，而不是
内部列残基自由度。因此继续用普通 `ColumnCRT` 容量估计会误判结构来源。

正确路由是：

```text
u=1 and D=I_m
=> UnitEndpointTruncation
=> exact-phase SAE
   or persistent exact-boundary Endpoint/PDEC。
```

## 4. 引理：精确端点相位二分

**引理 EUT-1（单位截断二分）。**  
对 `u=1` 且 `D=I_m` 的端点尖峰，若精确端点相位键

\[
(L_w\bmod Q,\ R_w\bmod Q,g,j_1,j_2)
\]

只出现有限次，则其贡献进入 SAE；若该键在无限窗口族中持久出现并保持正超额，则触发
`UnitEndpointTruncation/PDEC`。

**证明。**  
由 `(EUT-2)`，该尖峰完全由窗口两端点决定。若精确端点相位不复现，则没有可累积的同一
CRT 相位缺陷，只能作为有限异常项登记。若同一精确端点相位反复复现且正超额不可求和，则它
正是端点 CRT 相位持久偏差，按定义进入 PDEC。□

## 5. 下一步最小硬点

当前分支的最小硬点已经变成：

```text
证明 u=1 全窗口截断的精确端点相位键不会持久正超额；
或若持久，则排斥 UnitEndpointTruncation/PDEC。
```

这比前面的列容量不等式更具体，也更适合有限 SAE 账本或端点相位周期证书。

## 6. 审稿边界

已完成：

```text
u=1 => D=I_m 的逐行恒等式；
样本单位截断项全部按精确端点相位键进入 SAE；
主列核从普通 ColumnCRT 改路由到 UnitEndpointTruncation。
```

未完成：

```text
无限窗口族中的精确端点相位可求和证明；
UnitEndpointTruncation/PDEC 的全局排斥。
```
