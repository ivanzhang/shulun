# Seam 多层下降路线

**状态：** `conditional_seam_descent_supported_not_global_proof`

本文回答新的问题：

```text
缝合零窗如果存在，继续降阶方阵时，是否总有一阶会成为完整零行？
```

结论分两层：

1. 在条件模型中，答案得到强实验支持：全量 `p<=500` 的 `21339` 条 seam 窗口全部在某个下层素数
   `h` 处出现强制完整零行；`p<=2000,row_stride=25` 的确定性抽样 `11488` 条也全部成功。
2. 这还不是全局无条件证明。原因是“出现下层零行”必须继续接入下层零行延迟、方阵内位置或
   `SAE/PDEC/ColumnCRT` 出口；不能把它直接等同于原命题闭合。

## 1. 条件 seam 模型

设 `p<q` 为相邻素数，`q` 行

\[
I=[(s-1)q+1,sq]
\]

在降到旧 `p`-筛后不是完整 `p` 行，而是 seam zero window。也就是说，`I` 在 `p`-筛下为空，
但只覆盖一条 `p` 行后缀与下一条 `p` 行前缀。

继续降到更小素数 `h<p`。若 `I` 在 `p`-筛下为空，则在 `h`-筛下可能复活的点只能是

\[
\operatorname{Rev}_{h,p}(I)
=\{n\in I:\ P^-(n)>h,\ P^-(n)\le p\},
\tag{SMD-1}
\]

并在最后一条 `q` 行中额外保留端点穿孔 `q^2`。

这是严格恒等式：`P^-(n)>h` 表示 `n` 避开所有 `<=h` 的素数；若同时 `P^-(n)>p`，则 `n`
本来就是 `p`-筛幸存者，与 `I` 为 `p`-零窗矛盾。因此唯一能在剥层后出现的点，是最小素因子落在
`(h,p]` 的点。

## 2. 强制零行判据

令 `J` 是完整包含在 `I` 内的一条 `h` 对齐行。若

\[
J\cap \operatorname{Rev}_{h,p}(I)=\varnothing
\tag{SMD-2}
\]

且 `J` 不含终端穿孔 `q^2`，则在 `I` 为 `p`-零窗的假设下，`J` 必为 `h`-筛零行。

**证明。**  
若 `n∈J` 在 `h`-筛下幸存，则 `P^-(n)>h`。若 `P^-(n)>p`，则 `n` 也是 `p`-筛幸存者，违背
`I` 为 `p`-零窗。否则 `h<P^-(n)<=p`，于是 `n∈Rev_{h,p}(I)`，违背 `(SMD-2)`。证毕。

所以 seam 多层下降的真正硬点不是几何包含，而是复活点是否能打断所有完整下层行。

## 3. 有限审计

新增：

```text
experiments/prime_matrix_seam_multilevel_descent_audit.py
docs/monograph/prime-matrix-seam-multilevel-descent-audit.md/json
docs/monograph/prime-matrix-seam-multilevel-descent-audit-p2000-sample.md/json
```

全量 `p<=500`：

```text
seam windows checked = 21339
descend to forced zero row = 21339
blocked through checked levels = 0
first success inside lower h×h square = 15267
max first success level index = 87
```

确定性抽样 `p<=2000,row_stride=25`：

```text
seam windows checked = 11488
descend to forced zero row = 11488
blocked through checked levels = 0
first success inside lower h×h square = 9250
max first success level index = 292
```

审计含义：

```text
seam zero window
=> 降到更小 h 层时，几何上包含完整 h 行
=> 若某条完整 h 行避开 Rev_{h,p} 与 q^2 穿孔
=> 强制 h-zero-row
```

样本中没有发现“复活点永远打断所有完整下层行”的 seam。

## 4. 不能直接宣称闭合的原因

仍需区分三件事：

1. **完整下层零行**：`SMD-2` 给出的是某个 `h`-筛零行；
2. **下层方阵内零行**：该零行行号是否 `<=h`，才决定它是否直接落入 `h×h` 方阵；
3. **全局矛盾出口**：若零行在方阵外，还需接入下层首零行延迟、继续 RPZ 下降或
   `SAE/PDEC/ColumnCRT`。

本次账本显示多数首次成功已经落入对应 `h×h` 方阵，但仍有相当部分首次成功在方阵外。因此严证版本应写成：

```text
SeamDescent-ZeroRow:
  每个真实 seam 反例要么在某层产生受保护的下层零行，
  要么复活点对所有候选下层行形成持久阻断。

Persistent-Revival-Blocking:
  持久阻断必须触发 SAE/PDEC/ColumnCRT。
```

## 5. 下一步最小硬点

当前可攻目标已从泛泛的 `SeamGuard-Elimination` 进一步细化为：

```text
SMD-Global Inequality
```

即对任意相邻 `p<q` 与 seam 相位，证明存在某个 `h<p` 和完整 `h` 对齐行 `J⊂I`，满足

\[
J\cap \operatorname{Rev}_{h,p}(I)=\varnothing
\]

或证明若所有候选 `J` 都被复活点击中，则复活点集合在低模列残基、端点相位或尾锚方向出现
`SAE/PDEC/ColumnCRT` 缺陷。

这一步是目前最接近用户“缝合零窗继续降阶必变零行”直觉的可审稿形式。
