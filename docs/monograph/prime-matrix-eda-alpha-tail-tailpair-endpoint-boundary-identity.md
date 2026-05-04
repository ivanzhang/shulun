# AlphaTail 端点右边界钉扎的单位乘数恒等式

**状态：** `endpoint_unit_multiplier_boundary_identity_open`

本文接续精确列目标审计。新的结论是：主列核的右边界钉扎不是普通列残基偏置，而是由
`u=1` 的几何截断恒等式强制产生。

```text
D^+=R_w
```

因此该分支应从 `ColumnCRT` 再路由到更窄的
`UnitMultiplierRightEndpointTruncation`。

## 1. 几何恒等式

端点尖峰责任区间由

\[
d=qu-j_1r
\tag{EBI-1}
\]

给出。窗口可行起点区间为

\[
I_m=[L_w,R_w].
\]

局部素对变量 `q` 的右端为

\[
q^+
=
\left\lfloor {R_w+j_1r\over u}\right\rfloor.
\tag{EBI-2}
\]

于是

\[
D^+=uq^+-j_1r\le R_w.
\tag{EBI-3}
\]

若

\[
u\mid R_w+j_1r,
\tag{EBI-4}
\]

则

\[
D^+=R_w.
\tag{EBI-5}
\]

特别地，当 `u=1` 时 `(EBI-4)` 自动成立，所以任何右端截断责任区间都满足

\[
D^+=R_w.
\tag{EBI-6}
\]

## 2. 样本审计

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_endpoint_boundary_identity.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_boundary_identity.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 \
  --target-residue 4 --target-modulus 210 --format table
```

输出摘要：

```text
route=UNIT_MULTIPLIER_RIGHT_ENDPOINT_TRUNCATION；
records=10；
keys=5；
windows=2；
excess=69.927274；
all_right_boundary=True；
all_forced_by_u1=True；
all_forced_by_divisibility=True。
```

全部记录满足：

```text
u=1,
D^+=R_w=16384,
right_slack=0。
```

## 3. 引理：列缺陷到端点截断

**引理 EBI-1（单位乘数右端截断）。**  
若某个右端轴向锁相列目标的全部记录满足 `u=1` 且 `D^+=R_w`，则该目标不是普通内部
列残基容量异常，而是 `UnitMultiplierRightEndpointTruncation` 输入。

**证明。**  
由 `(EBI-1)`--`(EBI-3)`，右端点由 `q` 区间的上取整边界决定。`u=1` 时
`q^+=R_w+j_1r`，代回得到 `D^+=R_w`。因此端点相位固定来自窗口右边界截断，而不是内部列
残基自由选择后的异常集中。若该截断超额跨尺度持久出现，则进入有向端点 PDEC；若只在有限
窗口中出现，则进入 SAE。□

## 4. 对当前硬点的压缩

前一层目标：

```text
排斥 D^+==4 mod 210 的精确 ColumnCRT 子目标。
```

本文压缩为：

```text
排斥 u=1 且 D^+=R_w 的右端单位乘数截断尖峰。
```

这比列容量上界更具体，因为它只涉及：

```text
gap=36 或 72；
u=1；
q 区间右端由 R_w 强制；
所有超额来自局部 Brun/Selberg 常数超过 C_local 的端点短区间。
```

## 5. 下一步最小硬点

当前最小硬点变为：

```text
UnitMultiplierRightEndpointTruncation
=> finite SAE
or persistent Endpoint/PDEC。
```

要继续闭合，需要证明以下二选一：

1. `u=1` 右端截断尖峰在全局窗口族中可求和，因此是 SAE；
2. 若不可求和，则固定右端截断相位持久出现，触发可排斥的 Endpoint/PDEC。

## 6. 审稿边界

已完成：

```text
D^+=R_w 的单位乘数恒等式；
样本主列核全部由 u=1 强制；
ColumnCRT 分支到右端截断分支的路由。
```

未完成：

```text
u=1 右端截断尖峰的全局可求和上界；
或持久 Endpoint/PDEC 的最终排斥。
```
