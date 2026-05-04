# AlphaTail `C13` 高 P 的 `D2` 支配余量账本

**状态：** `c13_highp_d2_margin_input_ready`

本文接续低 `P` 有限证书。目标是把 `P>P_fin` 的剩余预算义务从

```text
|M| eta D_even <= 0.781 D2
```

进一步拆成可逐项审计的 `D2=M2-B2` 余量不等式。

## 1. 预算等价式

固定一个高 `P` 目标窗口，记：

```text
Cap_even = |M| eta D_even；
D2       = M2-B2；
M2       = 实际二阶尾交集矩；
B2       = 乘法模型二阶基线。
```

需要证明

\[
\mathrm{Cap}_{\rm even}\le D_2.
\tag{HDM-1}
\]

由于 `D2=M2-B2`，`(HDM-1)` 等价于

\[
{B_2\over M_2}
\le
1-{\mathrm{Cap}_{\rm even}\over M_2}.
\tag{HDM-2}
\]

右端是当前窗口允许的乘法基线占比上限。因此高 `P` 的真正剩余不是重新估计
`D_even`，而是证明二阶正偏差足够大：

```text
实际二阶尾交集矩 M2 必须比乘法基线 B2 多出至少 Cap_even。
```

**引理 HDM-1（高 P `D2` 支配等价）。**  
对任意高 `P` 目标窗口，`Cap_even<=D2` 当且仅当 `(HDM-2)` 成立。

**证明。**  
把 `D2=M2-B2` 代入 `Cap_even<=D2`，得到
`Cap_even<=M2-B2`，即 `B2<=M2-Cap_even`。两边除以正数 `M2`，
得到 `(HDM-2)`。反向完全相同。□

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_highp_d2_margin.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_highp_d2_margin.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --format table
```

输出摘要：

```text
highP-total:
  Cap_even = 7476.160000；
  D2       = 9964.123717；
  margin   = 2487.963717；
  Cap/D2   = 0.750308；
  B2/M2    = 0.440532；
  allowed  = 0.580227；
  B2_margin= 0.139695。
```

窗口级：

```text
p=5003:
  Cap_even=2408.880000, D2=3086.607367, margin=677.727367；
  Cap/D2=0.780430, B2/M2=0.511613, allowed=0.618848。

p=10007:
  Cap_even=5067.280000, D2=6877.516350, margin=1810.236350；
  Cap/D2=0.736789, B2/M2=0.401435, allowed=0.558983。
```

当前压力样本的最紧窗口仍为 `p=5003`，但它有正余量：

\[
D_2-\mathrm{Cap}_{\rm even}=677.727367.
\tag{HDM-3}
\]

## 3. 对主链的影响

高 `P` 接口现在可写成二层判据：

```text
几何层：
  SparseSAE atoms <= |M| eta D_even；

偏差层：
  |M| eta D_even <= D2
  等价于 B2/M2 <= 1-Cap_even/M2。
```

这比单纯记录 `Cap_even/D2<=0.781` 更适合审稿，因为它明确指出最终要证明的对象是
`B2` 相对 `M2` 的上界，而不是混合预算中的经验比例。

## 4. 剩余义务

已完成：

```text
高 P 预算等价式；
当前压力样本的高 P 总量与逐窗口正余量；
最紧窗口 p=5003 的具体余量定位。
```

仍未完成：

```text
证明所有 P>P_fin 目标窗口满足 B2/M2 <= 1-Cap_even/M2；
把该不等式与 H/RRD/OSPC 主链预算常数合并；
证明 P<=P_fin 的目标窗口清单已由有限证书全覆盖。
```

进一步的固定 gap 素对下界化见
`prime-matrix-eda-alpha-tail-tailpair-c13-highp-pair-lower-target.md`。该文件把
`HighP-D2-Lower` 细化为

```text
sum G_m^L >= sum(B2_m+Cap_even_m)，
```

其中 `G_m^L` 是低筛后等乘数固定 gap 尾素对数。

所以本文完成的是 `HighP-D2-Lower` 的代数化和样本证书，不是行命题最终闭合。
