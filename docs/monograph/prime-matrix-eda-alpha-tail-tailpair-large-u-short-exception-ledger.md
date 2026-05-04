# AlphaTail large-`u` 短 `q` 例外账本

**状态：** `large_u_short_exception_sample_empty_global_certificate_open`

本文接续格点端点几何引理。由 `LEG-3`，不被小 `u` 强制端点化的责任区间必为短 `q`
窗口。本文审计这些 large-`u` 例外是否仍可能触发 `C_local=1.3`。

## 1. large-`u` 例外

固定端点阈值 `theta=0.1`。large-`u` 分支定义为

\[
u>0.1|I|.
\tag{LUS-1}
\]

由 `LEG-3` 立刻得到

\[
|J|\le 10.
\tag{LUS-2}
\]

因此该分支不再是中尺度素对常数问题，而是一个至多 `10` 点的短窗口例外：

```text
Large-u short-q exception
=> finite SAE candidate or short-window PDEC row.
```

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_large_u_short_exception_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_large_u_short_exception_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.3 --endpoint-theta 0.1 --format table
```

输出摘要：

```text
large_u 12 positive 0 failures 0 parity_void 9
theta 0.100000 max_q_length 10 max_actual 0
```

结构拆分：

```text
large-u 总例外 = 12；
奇 gap ParityVoid = 9；
偶 gap 例外 = 3；
偶 gap 正素对命中 = 0；
C13 failure = 0。
```

因此当前样本中 large-`u` 短 `q` 分支完全清空。

## 3. 可引用引理

**引理 LUS-1（large-`u` 例外短窗口化）。**  
在 `theta=0.1` 下，任何非端点责任区间都满足 `|J|<=10`。若其 `gap` 为奇数，则
`N_g(J)=0`；若 `gap` 为偶数，则该区间可作为至多 `10` 个候选 `q` 的有限证书对象。

**证明。**  
`|J|<=10` 来自 `LEG-3`。奇 gap 情形由 `ISL-2`。偶 gap 情形没有额外估计，直接列举
`J` 中至多 `10` 个整数即可形成有限 SAE 证书候选。□

## 4. 对 C13 链条的影响

结合格点端点引理，`OnePairMargin-C13` 现在拆为：

```text
u<=0.1|I|:
  自动 EndpointGate，回流 Endpoint/PDEC/SAE/ColumnCRT；

u>0.1|I|:
  |J|<=10，进入 finite short-q SAE/PDEC；
  样本中该分支 actual=0。
```

因此固定 gap `C13` 分支的全局剩余已不再是普通中尺度 Brun/Selberg 常数，而是两个窄接口：

```text
Endpoint branch:
  排斥端点 PDEC/SAE/ColumnCRT；

Large-u finite branch:
  提交所有 large-u 短 q 例外的有限/可求和证书，
  或证明偶 gap 短窗口不触发整数门槛。
```

## 5. 审稿边界

已完成：

```text
large-u 分支短窗口化；
样本 large-u 例外清空；
奇 gap 例外由奇偶刚性排除。
```

仍未完成：

```text
全局 large-u 短 q 例外证书；
端点分支的最终 PDEC/SAE/ColumnCRT 排斥。
```

