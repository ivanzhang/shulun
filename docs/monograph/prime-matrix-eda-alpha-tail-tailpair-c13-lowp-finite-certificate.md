# AlphaTail `C13` 低 P 有限 group 证书与高 P 预算接口

**状态：** `c13_lowp_finite_certificate_input_ready`

本文接续混合预算证书。目标是把 `P<=P_fin` 的有限外壳从一句话落实为可复现 group 清单，
并把 `P>P_fin` 的预算义务写成单个明确不等式。

## 1. 低 P 有限证书

取当前工作阈值

\[
P_{\rm fin}=1000.
\tag{LFC-1}
\]

对 `P<=P_fin` 的窗口，使用纯几何 group 外壳：

\[
\Delta |r|=g u,\qquad g\equiv0\pmod2,
\tag{LFC-2}
\]

并逐个 group 记录：

```text
(p,B,r,g,j1,j2,u,side,epsilon,slots,q_interval,support_m)。
```

该证书不依赖实际 failure 原子，也不依赖尾素对分布；它只依赖有限窗口清单、点位差和端点带
公式。

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_lowp_finite_certificate.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_lowp_finite_certificate.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --format table
```

输出摘要：

```text
finite_cut=1000；
windows=1；
groups=81；
slots=9387；
capacity=750.960000；
D2=1058.946880；
capacity/D2=0.709157；
capacity/Equal=0.149982。
```

这给出低 `P` 窗口的有限几何证书：

```text
p=997, B=4096, r=-36；
records=123；
groups=81；
slots=9387；
capacity=750.96。
```

## 3. 高 P 预算接口

对 `P>P_fin`，继续使用闭式 `D_even` 外壳。逐窗口充分条件为

\[
|M|\eta D_{\rm even}(B,r)
\le
c_* D_2(B,r).
\tag{LFC-3}
\]

在当前压力样本中，高 `P` 两个窗口读数为：

```text
p=5003  : D_even-capacity/D2=0.780430；
p=10007 : D_even-capacity/D2=0.736789。
```

更细的 `D2=M2-B2` 余量账本见
`prime-matrix-eda-alpha-tail-tailpair-c13-highp-d2-margin.md`。该账本把 `(LFC-3)` 等价改写为

\[
{B_2\over M_2}
\le
1-{|M|\eta D_{\rm even}\over M_2}.
\tag{LFC-4}
\]

当前高 `P` 样本总量为：

```text
Cap_even=7476.160000；
D2=9964.123717；
margin=2487.963717；
Cap_even/D2=0.750308。
```

逐窗口最紧者仍是 `p=5003`：

```text
Cap_even=2408.880000；
D2=3086.607367；
margin=677.727367；
Cap_even/D2=0.780430。
```

因此当前样本的高 `P` 接口可定为

\[
c_*=0.781.
\tag{LFC-5}
\]

正式全局证明必须证明所有 `P>P_fin` 目标窗口满足 `(LFC-3)`，或把超出者送入
`ColumnCRT/PDEC/finite certificate`。

## 4. 对主链的影响

混合链条现在是：

```text
P<=1000:
  finite geometric group certificate, cap/D2=0.709157 in sample；

P>1000:
  D_even divisor envelope；
  required high-P inequality: |M| eta D_even <= 0.781 D2；
  equivalent margin inequality:
    B2/M2 <= 1-|M| eta D_even/M2。
```

这一步把上一层剩余拆成两个可审稿对象：

```text
LowP-FiniteComplete:
  P<=P_fin 的目标窗口清单必须完整，且证书可复现；

HighP-D2-Lower:
  P>P_fin 时 D2 必须统一支配 D_even 外壳；
  等价于乘法基线 B2 在 M2 中留出足够正偏差余量。
```

## 5. 审稿边界

已完成：

```text
P_fin=1000 的样本有限 group 证书；
低 P 证书不依赖实际 failure 分布；
高 P 预算接口压成 |M| eta D_even <= 0.781 D2；
HighP-D2-Lower 已代数化为 B2/M2 余量不等式。
```

仍未完成：

```text
证明 P<=1000 的目标窗口清单已经全覆盖；
全局证明 HighP-D2-Lower；
把 0.781 与最终主链预算常数合并。
```

所以本文完成的是低 `P` 有限证书与高 `P` 预算接口，不是行命题最终闭合。
