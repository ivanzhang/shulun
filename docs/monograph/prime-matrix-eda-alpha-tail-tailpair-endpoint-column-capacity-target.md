# AlphaTail 端点列残基核的容量目标

**状态：** `endpoint_column_capacity_target_open`

本文把两个低模右端列核转换为显式容量不等式目标。它仍不是排斥证明；它给出：

```text
若没有 ColumnCRT/PDEC，
则列残基容量上界至少必须允许多少倍均衡超载。
```

样本显示主列核需要约 `20.25` 倍均衡容量才能被吸收，因此它是强 ColumnCRT 输入。

## 1. 容量模型

设单侧端点锁相总质量为

\[
M_{\rm axis}.
\]

一个列核

\[
D^+\equiv a\pmod q
\]

承载质量 `M(a,q)`。若无列残基缺陷，最基础的均衡期望是

\[
M(a,q)\approx {M_{\rm axis}\over q}.
\tag{ECC-1}
\]

定义吸收该列核所需的容量常数

\[
C_{\rm req}(a,q)
=
{M(a,q)\over M_{\rm axis}/q}
=
q\,{M(a,q)\over M_{\rm axis}}.
\tag{ECC-2}
\]

若可证明无 ColumnCRT 时存在统一上界

\[
C_{\rm col}<C_{\rm req}(a,q),
\tag{ECC-3}
\]

则该列核必须触发 `ColumnCRT/PDEC`。

## 2. 样本容量目标

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_endpoint_column_capacity_target.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_column_capacity_target.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 \
  --phase-modulus 210 --format table
```

总单侧端点质量：

```text
M_axis=120.877779。
```

两个兼容列核：

```text
D^+ == 4 mod 35:
  key_count=5,
  excess=69.927274,
  density=0.578496,
  uniform_density=0.028571,
  C_req=20.247349。

D^+ == 3 mod 5:
  key_count=3,
  excess=50.950505,
  density=0.421504,
  uniform_density=0.200000,
  C_req=2.107522。
```

精确列类中最强的目标为：

```text
D^+ == 4 mod 210:
  C_req=47.418683。
```

但精确类只承载两条键；兼容列核 `4 mod 35` 承载五条键，通常是更稳健的全局硬攻对象。

## 3. 引理：容量目标到 ColumnCRT 出口

**引理 ECC-1（列容量目标）。**  
若存在无缺陷容量定理：

\[
M(a,q)\le C_{\rm col}{M_{\rm axis}\over q}
\tag{ECC-4}
\]

且某列核满足 `C_req(a,q)>C_col`，则该列核不能在无 ColumnCRT 状态下出现，必须进入
`ColumnCRT/PDEC` 或有限 `SAE`。

**证明。**  
由 `(ECC-2)`，`C_req>C_col` 等价于

\[
M(a,q)>C_{\rm col}{M_{\rm axis}\over q},
\]

与 `(ECC-4)` 矛盾。因此若该质量持久存在，只能触发列残基缺陷；若不持久，则进入 SAE。□

## 4. 下一步最小硬点

当前最优攻坚目标已经定量化为：

```text
证明无 ColumnCRT 时，
D^+ == 4 mod 35 的右端端点质量不能超过
C_col * M_axis/35，
并将 C_col 压到 20.247349 以下。
```

这比直接证明 `U_CRT<L_PDEC` 更窄：只需针对右端列核 `4 mod 35` 建立容量上界或证明其
持久出现本身就是 ColumnCRT/PDEC。

## 5. 审稿边界

已完成：

```text
列核容量常数 C_req 的定义；
两个低模列核的显式 C_req；
ColumnCRT 出口的阈值比较接口。
```

未完成：

```text
无 ColumnCRT 状态下的 C_col 上界；
ColumnCRT/PDEC 的最终排斥；
SAE 可求和或有限证书。
```
