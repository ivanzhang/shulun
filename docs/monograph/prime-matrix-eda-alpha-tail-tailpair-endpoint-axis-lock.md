# AlphaTail 单侧端点频率的列残基锁相

**状态：** `endpoint_axis_phase_lock_columncrt_input_open`

本文接续责任频率路由。对进入 `OneSidedEndpointCRTDefect/ColumnCRT` 的轴向频率，本文检查其
是否不仅是“一侧端点偏置”，而且精确锁到单一列残基。样本结果显示：全部轴向键均为精确锁相。

## 1. 轴向频率与列残基

对端点相位

\[
\tau_Q(D)=(D^-\bmod Q,\ D^+\bmod Q)
\]

若责任频率为右轴向

\[
h=(0,h_+),\quad h_+\ne0,
\]

则 Fourier 相位只依赖

\[
h_+D^+\pmod Q.
\tag{EAL-1}
\]

左轴向同理只依赖 `h_-D^- mod Q`。

定义轴向锁相值

\[
\lambda_e=
\begin{cases}
h_+D^+_e\bmod Q, & h=(0,h_+),\\
h_-D^-_e\bmod Q, & h=(h_-,0).
\end{cases}
\tag{EAL-2}
\]

若同一持久键 `K` 的全部观测端点原子满足同一个 `lambda`，称其为
`ExactAxisPhaseLock(K,Q,h)`。

## 2. 引理：精确锁相到 ColumnCRT 输入

**引理 EAL-1（轴向锁相）。**  
若 `K` 是 mirror-admissible 的轴向责任频率键，且满足 `ExactAxisPhaseLock(K,Q,h)`，
则 `K` 给出一条 `ColumnCRT` 输入行：

```text
endpoint side      : left/right；
frequency          : h；
locked residue     : lambda；
mass               : M_K；
bad window support : S_K。
```

**证明。**  
轴向频率只依赖单侧端点坐标。若所有正超额质量集中在同一个 `lambda`，则这些坏窗在
低模 `Q` 的单侧端点投影上落入同一非零角色的同一相位类。这不是双端几何效应，而是列方向
端点残基过密；按 `H4-PDEC` 模板，它必须作为 `ColumnCRT` 或单侧端点 CRT 缺陷处理。□

## 3. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_endpoint_axis_lock_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_endpoint_axis_lock_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --num-primes 8 --local-c 1.2 --endpoint-theta 0.1 \
  --phase-modulus 210 --format table
```

样本结果：

```text
8 个 OneSidedEndpoint/ColumnCRT 键全部：
lock_classes=1,
locked=True,
max_lock_fraction=1.000000,
route=EXACT_AXIS_PHASE_LOCK_COLUMNCRT_INPUT。
```

最大锁相行：

```text
g900:j1-0:u1:B,
endpoint=right,
best_freq=(0,3),
locked residue=24,
total_excess=28.759861。
```

## 4. 对主硬点的压缩

上一层有

```text
OneSidedEndpointCRTDefect/ColumnCRT:
count=8, total_excess=120.8777794864998。
```

本文把它进一步压缩为：

```text
8 条精确右端锁相 ColumnCRT 输入行。
```

因此下一步不再需要处理一般轴向频率，而是处理具体列残基锁相：

```text
证明同一右端锁相残基不能持久承载 M_K；
或把该锁相残基作为 ColumnCRT/PDEC 证书提交并排斥；
或证明其只能有限出现，进入 SAE。
```

## 5. 审稿边界

已完成：

```text
轴向锁相值 lambda 的定义；
ExactAxisPhaseLock => ColumnCRT 输入；
样本中全部轴向键精确锁相。
```

未完成：

```text
ColumnCRT 锁相残基的全局排斥；
列残基容量上界；
ColumnCRT 失败回流到 SAE/PDEC 的定量余量。
```
