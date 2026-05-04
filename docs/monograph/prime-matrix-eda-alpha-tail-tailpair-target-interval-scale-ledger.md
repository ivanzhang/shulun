# AlphaTail 固定 gap 目标区间尺度下界账本

**状态：** `target_interval_scale_floor_sample_closed_global_open`

本文接续 `C_local=1.3` 可采纳性审查，处理第一子硬点：目标窗口族中是否存在极短固定
gap 区间，使 `C_local=1.3` 被单个素对命中自动击穿。

## 1. 尺度地板

记

\[
B_g(J)=\mathfrak S_g{|J|\over \log^2 J_-}.
\tag{TIS-1}
\]

若 `N_g(J)=1`，则局部需求常数为 `1/B_g(J)`。因此对阈值 `C_local`，任何满足

\[
B_g(J)<{1\over C_{\rm local}}
\tag{TIS-2}
\]

且含有一个固定 gap 素对的区间，都会自动成为局部尖峰。

对 `C_local=1.3`，尺度地板为

\[
1/C_{\rm local}=0.769230\ldots.
\tag{TIS-3}
\]

因此 `(TIS-2)` 是必须先排除的最小伪反例入口。

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_target_interval_scale_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_target_interval_scale_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.3 --format table
```

输出摘要：

```text
rows 6 intervals 870 local_C 1.300000 scale_floor 0.769231
low_scale 0 low_scale_positive 0
global_min_scale 1.056366
global_min_positive_scale 25.371688
global_max_local_C 1.292474
```

逐行最小正命中尺度：

```text
p=997,m=4      min_positive_scale=31.058234；
p=997,m=5      min_positive_scale=25.371688；
p=5003,m=4     min_positive_scale=85.903290；
p=5003,m=5     min_positive_scale=85.427018；
p=10007,m=4    min_positive_scale=160.329313；
p=10007,m=5    min_positive_scale=148.136015。
```

## 3. 结论

样本中：

```text
低于 1/1.3 的目标区间数 = 0；
低于 1/1.3 且含素对的目标区间数 = 0；
所有有素对命中的区间尺度至少为 25.371688。
```

所以当前样本的 `C_local` 压力不是单个素对落入极短区间造成的，而是中尺度固定 gap 素对
密度偏高造成的真实局部常数问题。最紧样本为：

```text
actual=65, scale=50.291, required_C=1.292474。
```

这进一步确认下一步不能只做“小区间有限例外”处理，还必须处理目标窗口族的中尺度局部
Brun/Selberg 常数或 SAE/PDEC 出口。

## 4. 可引用引理

**引理 TIS-1（单命中尺度地板）。**  
若目标窗口族对所有固定 gap 区间满足 `B_g(J)>=1/C_local`，则单个素对命中不会导致
`C_loc>C_local`。

**证明。**  
当 `N_g(J)=1` 时，`C_loc=1/B_g(J)<=C_local`。□

该引理只排除单命中伪尖峰；对 `N_g(J)>=2` 的中尺度过密仍需独立上界。

## 5. 审稿边界

已完成：

```text
样本目标区间尺度地板审计；
确认样本无单命中极短区间尖峰；
把剩余压力定位为中尺度局部素对密度问题。
```

仍未完成：

```text
全局目标窗口族的尺度地板证明；
中尺度固定 gap 素对局部常数 <=1.3；
或全部中尺度超标窗口的 SAE/PDEC 证书。
```

