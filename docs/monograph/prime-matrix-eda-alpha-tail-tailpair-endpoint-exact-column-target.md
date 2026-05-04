# AlphaTail 端点精确列目标与右边界钉扎

**状态：** `endpoint_exact_column_target_boundary_pinned_open`

本文接续列核嵌套压力账本。新的审计发现比锁相同余反解更强：样本主列核
`D^+==4 mod35` 的全部端点记录实际满足

```text
D^+ = 16384,
D^+ == 4 mod 210。
```

也就是说，质量不是只集中在低模列核，而是钉在同一个窗口右边界。

## 1. 精确目标定义

对给定精确列目标

\[
D^+\equiv a\pmod q,
\]

收集所有右端轴向锁相记录 `e`，若

\[
D^+_e\equiv a\pmod q
\tag{ECT-1}
\]

则登记为 `ExactColumnTarget(a,q)`。

若进一步所有记录有相同端点值

\[
D^+_e=R_0,
\tag{ECT-2}
\]

则称为 `RightBoundaryPinnedTarget`。

## 2. 样本审计

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_endpoint_exact_column_target.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_exact_column_target.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 \
  --target-residue 4 --target-modulus 210 --format table
```

输出：

```text
target 4 mod 210,
route EXACT_COLUMNCRT_PDEC_INPUT,
records=10,
keys=5,
windows=2,
p_support=1,
excess=69.927274。
```

五个键全部来自同一几何窗口族：

```text
5003:8192:-36:m4,
5003:8192:-36:m5。
```

全部记录满足：

```text
D^+=16384,
D^+ mod 210=4。
```

这说明主列核的真实结构是右边界钉扎，而不是普通列残基稀疏偏置。

## 3. 与上一层嵌套账本的关系

上一层 `column_nested_pressure` 使用锁相方程

\[
hD^+\equiv\lambda\pmod Q
\]

反解出若干“由频率可见”的精确子类。那些子类是频率方程给出的约束，不是不交列分割。

本文直接回到原始端点 `D^+`，发现所有主列核事件实际落在同一个更强目标

\[
D^+\equiv4\pmod{210}
\]

且端点值完全相同。因此后续上界应优先使用边界钉扎刚性，而不是只使用频率反解的子类。

## 4. 引理：右边界钉扎到端点 PDEC

**引理 ECT-1（边界钉扎出口）。**  
若持久端点质量在同一窗口族中满足同一右边界值 `D^+=R_0`，则它给出
`RightBoundaryPinnedEndpointDefect`。该缺陷若持久出现，进入 `Endpoint/PDEC` 或
`ColumnCRT`；若只有限出现，进入 `SAE`。

**证明。**  
`D^+=R_0` 固定意味着端点尖峰的责任区间右端没有内部自由度，所有正超额都由窗口右边界截断
造成。这比单纯残基偏置更强：端点 sawtooth 的相位不仅在模 `q` 上固定，而且在整数端点上固定。
若这种现象跨尺度持久，则是有向端点 CRT 缺陷；若只出现在有限样本窗口，则只能作为 SAE 登记。
□

## 5. 下一步最小硬点

当前最优目标从

```text
D^+ == 4 mod 35 的列核容量上界
```

进一步压缩为

```text
D^+=R_w 的右边界钉扎端点质量上界。
```

要闭合该分支，需要证明：

```text
右边界钉扎不能持久承载 69.927274 级别的端点超额；
若持久，则触发 Endpoint/PDEC 或 ColumnCRT；
若有限，则进入 SAE。
```

## 6. 审稿边界

已完成：

```text
主列核全部记录的精确端点值审计；
D^+=16384 的右边界钉扎识别；
边界钉扎出口定义。
```

未完成：

```text
RightBoundaryPinnedEndpointDefect 的全局排斥；
Endpoint/PDEC 或 ColumnCRT 的最终证书；
SAE 可求和证明。
```
