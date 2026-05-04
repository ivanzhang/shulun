# AlphaTail 单位截断到固定差值短区间常数的归约

**状态：** `endpoint_unit_truncation_fixed_gap_constant_open`

本文把 `UnitPhasePair` 分支继续压缩：`u=1` 全窗口截断项不再是 CRT 几何问题，而是固定差值
素对短区间 Brun/Selberg 局部常数问题。

## 1. 归约

当 `u=1` 时，责任区间 `D=I_m`。对应的尾素对变量区间为

\[
J=[q^-,q^+],
\]

并且局部超额就是固定差值 `g` 的短区间素对计数

\[
A_g(J)-C_{\rm local}B_g(J).
\]

因此：

```text
UnitEndpointTruncation
=> FixedGapShortIntervalConstant
=> SAE or fixed-gap Brun/Selberg input。
```

若能证明对全部相关固定差值和短区间有

\[
A_g(J)\le C_{\rm FG} B_g(J),
\qquad C_{\rm FG}\le C_{\rm local},
\tag{USG-1}
\]

则单位截断分支消失。若 `(USG-1)` 失败且持久，则失败不是方阵列残基异常，而是固定差值短区间
素对常数包缺口。

## 2. 样本审计

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_endpoint_unit_shortgap_reduction.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_unit_shortgap_reduction.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 --format table
```

样本摘要：

```text
records=26,
gaps=8,
total_excess=177.008191,
max_required_C=1.253939。
```

按 gap 聚合的最大需求：

```text
g=900  : max_C=1.253939；
g=144  : max_C=1.251074；
g=36   : max_C=1.247242；
g=72   : max_C=1.230896；
g=3600 : max_C=1.226478。
```

这说明当前 `u=1` 分支只需要一个约 `1.254` 的固定差值短区间常数包来吸收样本。

## 3. 引理：单位截断出口

**引理 USG-1（单位截断到固定 gap 常数）。**  
任何 `u=1` 全窗口截断尖峰，要么由固定差值短区间常数包吸收，要么给出
`FixedGapShortIntervalDefect(g,J)`。若该缺陷持久，则进入固定 gap 的外部/内部常数输入；若有限，
则进入 SAE。

**证明。**  
`u=1` 时 `D=I_m`，没有内部端点自由度。尖峰定义正是 `A_g(J)>C_local B_g(J)`。
因此唯一可能的解释是固定 gap 短区间素对计数超过所用常数包。有限失败列入 SAE；持久失败则是
固定 gap 常数包缺口。□

## 4. 对行命题链条的影响

前一层硬点：

```text
UnitPhasePair 键可求和或持久 PDEC 排斥。
```

本文压缩为：

```text
证明固定差值短区间素对常数 C_FG <= 1.2；
或把 C_local 提高到可验收常数；
或提交有限 SAE 账本。
```

注意：提高 `C_local` 会影响上游 TailPairLocalSpike 的尖峰数量，必须同步重跑端点/内区账本。

## 5. 审稿边界

已完成：

```text
u=1 单位截断到固定 gap 短区间计数的归约；
样本所需固定 gap 常数表；
明确该分支不是普通 ColumnCRT 几何异常。
```

未完成：

```text
全局固定 gap 短区间 Brun/Selberg 常数包；
或有限 SAE 账本；
或调整 C_local 后的全链重审计。
```
