# AlphaTail `C13` 除数外壳与二阶共振预算归一化账本

**状态：** `c13_budget_normalization_input_ready`

本文接续 `C13` 除数和闭式外壳。目标是把闭式容量
`|M| eta D_tau_sigma`、`|M| eta D_even` 与现有二阶尾素对共振账本中的 `D2`、
`equal_multiplier` 对齐，抽取正式闭合所需的预算比例。

## 1. 归一化对象

记：

```text
Cap_tau   = |M| eta sum D_tau_sigma(B,r)；
Cap_even  = |M| eta sum D_even(B,r)；
Cap_fail  = 当前真实 failure group 的确定性容量；
D2        = M2-B2，即二阶尾重叠超过乘法模型的超额；
Equal     = equal-multiplier 共振计数。
```

若主链允许把 `C13` 的 SparseSAE/endpoint 付款记入 `D2` 总预算，则充分条件可写成

\[
\mathrm{Cap}_{\rm even}\le c_{13}D_2
\quad\text{或}\quad
\mathrm{Cap}_{\tau}\le c_{13}D_2.
\tag{BNL-1}
\]

其中 `c13` 是主链愿意分配给 C13 分支的比例常数。若使用 `Equal` 作为更粗预算池，则对应为
`Cap/Equal`。

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_budget_normalization.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_budget_normalization.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --eta 0.04 --format table
```

输出总量：

```text
Cap_tau   = 9783.533520；
Cap_even  = 8667.360000；
Cap_fail  = 1971.280000；
D2        = 11023.070597；
Equal     = 22817；
M2        = 24545。
```

归一化比例：

```text
Cap_tau/D2   = 0.887551；
Cap_even/D2  = 0.786293；
Cap_fail/D2  = 0.178832；
Cap_tau/Equal  = 0.428783；
Cap_even/Equal = 0.379864。
```

窗口级结果：

```text
p=997   : Cap_tau/D2=1.272874, Cap_even/D2=1.124891；
p=5003  : Cap_tau/D2=0.880584, Cap_even/D2=0.780430；
p=10007 : Cap_tau/D2=0.831348, Cap_even/D2=0.736789。
```

这说明：

```text
1. 若按全局 D2 池付款，D_even 外壳需要约 78.63% 的 D2，D_tau_sigma 外壳需要约 88.76%。
2. 若要求逐窗口 D2 付款，p=997 窗口不够，必须使用全局池化、局部细分或更窄外壳。
3. 真实 failure 容量只需 17.88% 的 D2，但这依赖实际失败 group，不是全局无黑箱外壳。
```

## 3. 对主链的影响

当前 `C13-DivisorBudget` 不应写成“已经闭合”，而应精确写成二选一：

```text
Global-D2-Pool route:
  主链允许 C13 使用全局 D2 的至少 0.786293 份；
  则 D_even 外壳足以支付当前压力样本。

Refined-local route:
  若只能逐窗口付款，则必须继续压低 p=997 的局部外壳，
  或将 p=997 的低层异常接入有限证书/ColumnCRT。
```

因此下一最小硬点变为：

```text
C13-Budget-Allocation:
  证明 C13 分支可使用全局 D2 池；
  或证明 exact-even 外壳可进一步降到逐窗口 D2 以下；
  或把低 p 局部外壳改为有限证书。
```

低 `P` 有限证书与高 `P` 除数外壳的混合修正见
`prime-matrix-eda-alpha-tail-tailpair-c13-hybrid-budget-certificate.md`。当前样本取
`P_fin=1000`、低 `P` 使用 finite geometric envelope 后，逐窗口最大 `Cap/D2` 降为
`0.780430`，修复了 `p=997` 的逐窗口不足。

## 4. 审稿边界

已完成：

```text
Cap_tau、Cap_even、Cap_fail 与 D2/Equal 的逐窗口和全局比例；
指出全局池化可行但逐窗口 p=997 不足；
把预算缺口从模糊常数压缩为 C13-Budget-Allocation。
```

仍未完成：

```text
主链正式允许 C13 使用全局 D2 池的证明；
逐窗口外壳压低或低 p 有限证书；
与 H/RRD/OSPC 总预算的最终常数合并。
```

所以本文完成的是预算归一化，不是行命题最终闭合。
