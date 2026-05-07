# 第P列远尾模型付款常数接口

**状态：** `conditional_payment_audit_not_a_proof`

本文接续 `FarTail-Cofactor Bound`。远尾反演已经把 `q>10Y` 的高素命中写成 `Y`-rough 互补因子 `m` 上的短素数区间计数。本层进一步建立模型付款常数：

\[
\operatorname{Model}_{tail}(P,y)
=\sum_m {|I_m|\over \log q_m^-},
\tag{FTP-1}
\]

其中

\[
I_m=\left[
\max(10Y,\lceil (Py-P+1)/m\rceil),
\min(P-1,\lfloor (Py-1)/m\rfloor)
\right].
\]

目标是证明一个统一上界

\[
T_{>10Y}(P,y)\le C_{tail}\operatorname{Model}_{tail}(P,y),
\tag{FTP-2}
\]

并使

\[
T_{\le 10Y}(P,y)+C_{tail}\operatorname{Model}_{tail}(P,y)<|S_Y(P,y)|.
\tag{FTP-3}
\]

## 1. 模型付款审计

脚本：

```text
experiments/prime_matrix_pcolumn_far_tail_model_bound.py
experiments/prime_matrix_pcolumn_tail_payment_constant_scan.py
```

报告：

```text
docs/pcolumn_far_tail_model_bound_20260506.md
docs/pcolumn_tail_payment_constant_scan_20260506.md
```

对最强近截止行，实际远尾命中几乎等于模型量：

| P | y | tail actual | model | actual/model | allow/model | slack |
|---:|---:|---:|---:|---:|---:|---:|
| 5003 | 41 | 356 | 352.234 | 1.010693 | 1.141288 | 0.130595 |
| 10007 | 46 | 684 | 674.138 | 1.014629 | 1.160000 | 0.145371 |
| 20011 | 71 | 1402 | 1367.240 | 1.025423 | 1.107340 | 0.081917 |
| 50021 | 104 | 3252 | 3272.428 | 0.993758 | 1.141660 | 0.147902 |
| 100003 | 147 | 6468 | 6441.275 | 1.004149 | 1.124777 | 0.120628 |
| 200003 | 185 | 12580 | 12566.596 | 1.001067 | 1.111598 | 0.110531 |

这里

```text
allow/model = (S - non_tail) / model_tail
```

表示只要 `C_tail` 小于该值，远尾就可付款并推出 `T<S`。

## 2. C_tail=1.05 风险簇扫描

进一步对每个 `P` 的 `y<=4Y` 区域取 `T/S` 最高的 `top_n=16` 行，检验

\[
T_{\le 10Y}+1.05\,\operatorname{Model}_{tail}<S.
\tag{FTP-4}
\]

结果：

| P | cutoff | min pay margin | min C allow | max actual/model | fails |
|---:|---:|---:|---:|---:|---:|
| 5003 | 38 | 32.155 | 1.141288 | 1.020616 | 0 |
| 10007 | 52 | 73.566 | 1.157071 | 1.033097 | 0 |
| 20011 | 70 | 78.398 | 1.107340 | 1.027271 | 0 |
| 50021 | 104 | 299.951 | 1.141423 | 1.010889 | 0 |
| 100003 | 141 | 478.903 | 1.124231 | 1.013767 | 0 |
| 200003 | 190 | 760.506 | 1.110310 | 1.006172 | 0 |

最紧点仍是 `P=20011,y=71`：

```text
S=2596, T=2484,
tail=1402, non_tail=1082,
model_tail=1367.240,
C_allow=1.107340,
actual/model=1.025423,
payment_margin(C=1.05)=78.398。
```

因此样本支持一个清晰的条件接口：

```text
FarTail Payment:
  若 tail <= 1.05 * model_tail，
  则 top 近截止风险行已经不能全覆盖。
```

## 3. 分桶结构

在最强行上，`actual/model` 在各 `m/y` 桶中也贴近 `1`。例如 `P=200003,y=185`：

| band | actual | model | actual/model |
|---|---:|---:|---:|
| `(2,5]y` | 2555 | 2547.619 | 1.002897 |
| `(10,25]y` | 2399 | 2409.839 | 0.995502 |
| `(1,2]y` | 1975 | 1977.190 | 0.998892 |
| `>50y` | 1931 | 1951.485 | 0.989503 |
| `(5,10]y` | 1878 | 1860.956 | 1.009159 |
| `(25,50]y` | 1842 | 1819.506 | 1.012363 |

这说明远尾不是由单个 `m/y` 层爆炸，而是多层短素数区间共同按 `1/log` 密度付款。若某一层未来长期超过 `1.05`，它将成为比当前模型更尖锐的 `cofactor-anchor/SAE` 入口。

## 4. 当前最小硬点

当前最小硬点可写成：

```text
FarTail-Model Bound:
  对 y≈Y 的近截止风险行，
  证明
    T_{>10Y}(P,y) <= 1.05 * sum_m |I_m|/log(q_m^-)，
  或证明任何超标层必触发 cofactor-anchor / SAE / PDEC / ColumnCRT。
```

这还不是最终行命题证明，因为仍需：

```text
1. 把 top-16 风险行推广到所有近截止风险行；
2. 给出严格短素数区间上界，不能只用模型；
3. 处理 non-tail(q<=10Y) 的统一容量上界；
4. 把超标层接入已有 PDEC/SAE/ColumnCRT 证书框架。
```

但硬点已经从“远尾高素偏差”压成一个审稿员可检查的短区间素数上界常数问题。
