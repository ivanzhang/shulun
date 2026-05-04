# AlphaTail 固定 gap `C_local=1.3` 整数余量账本

**状态：** `c13_integer_slack_sample_closed_one_pair_margin_global_open`

本文继续推进 `FGC-13-admissible`。尺度账本已经排除样本中的单命中极短区间伪尖峰；本文件进一步把
中尺度局部常数压力离散化为整数素对余量。

## 1. 整数门槛

固定 gap 区间的局部常数条件为

\[
N_g(J)\le C_{\rm local}B_g(J),
\qquad
B_g(J)=\mathfrak S_g{|J|\over\log^2J_-}.
\tag{ISL-1}
\]

由于 `N_g(J)` 是整数，`C_local=1.3` 失败等价于

\[
N_g(J)\ge \lfloor 1.3B_g(J)\rfloor+1.
\tag{ISL-2}
\]

定义整数余量

\[
\Delta_{13}(g,J)
=
\lfloor1.3B_g(J)\rfloor+1-N_g(J).
\tag{ISL-3}
\]

则 `\Delta_{13}<=0` 当且仅当该区间触发 `TailPairLocalSpike`。

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_integer_slack_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_integer_slack_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.3 --format table
```

输出摘要：

```text
rows 6 intervals 870 local_C 1.300000 positive_even 167
failures 0 global_min_slack 1 global_max_required_C 1.292474
```

逐行最紧余量：

```text
p=997,m=4      min_slack=2；
p=997,m=5      min_slack=1；
p=5003,m=4     min_slack=12；
p=5003,m=5     min_slack=10；
p=10007,m=4    min_slack=29；
p=10007,m=5    min_slack=8。
```

最紧记录为：

```text
p=997, block=4096, shift=-36, m=5, gap=24, u=3,
actual=65, threshold=66, integer_slack=1,
required_C=1.292474, q_length=1317。
```

## 3. 奇偶刚性

所有奇数 `gap` 区间自动为 `ParityVoid`：若 `q>2` 且 `q+g` 同为素数，则 `g` 必为偶数。
样本中：

```text
ParityVoid intervals = 19+32+19+32+57+96 = 255。
```

因此真正参与 `C13` 压力的只有偶 gap 中尺度区间。这个排除是完全确定的，不依赖素数分布估计。

## 4. 当前最小硬点

样本中无 `C13Failure`，但最紧处只差一个素对。因此下一步不能用粗粒度平均不等式，应直接攻：

```text
OnePairMargin-C13:
  对目标窗口族中所有偶 gap 中尺度区间，
  排除 N_g(J) 达到 floor(1.3B_g(J))+1 的单个额外素对；
  若不能排除，则该额外素对必须物化为 SAE/PDEC/ColumnCRT 证书。
```

该目标比“证明一个宽松 Brun 常数”更窄：它只关心跨过整数门槛的最后一个素对。

## 5. 可引用引理

**引理 ISL-1（整数门槛等价）。**  
对任意固定 gap 目标区间，`C_loc<=1.3` 当且仅当 `\Delta_{13}(g,J)>=1`。

**证明。**  
`N_g(J)<=1.3B_g(J)` 与整数不等式
`N_g(J)<=floor(1.3B_g(J))` 等价。移项即 `(ISL-3)`。□

**引理 ISL-2（奇 gap 排除）。**  
若 `g` 为奇数且 `J` 中的素数均大于 `2`，则 `N_g(J)=0`。

**证明。**  
奇数 gap 使 `q` 与 `q+g` 一奇一偶。二者若都为素数，则偶数者只能是 `2`；在本文尾素区间中
`q>2` 且 `q+g>2`，矛盾。□

## 6. 审稿边界

已完成：

```text
C=1.3 条件的整数门槛化；
样本中全部 C13 失败为 0；
最小余量定位为 1 个素对；
奇 gap 压力确定排除。
```

仍未完成：

```text
全局 OnePairMargin-C13；
或所有触及整数门槛的窗口进入 SAE/PDEC/ColumnCRT 并被排斥。
```

因此当前硬点已从“连续常数包”收窄为“偶 gap 中尺度区间的最后一个额外素对”。

