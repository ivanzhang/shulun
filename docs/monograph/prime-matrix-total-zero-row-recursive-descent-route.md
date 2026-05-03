# 任意高阶零行的总递归下降路线

**状态：** `conditional_total_descent_supported_not_global_proof`

本文把当前所有可用机制合并为一个统一路线，回应用户的总判断：

```text
无论高阶 q×q 方阵的零行在哪一行，
沿相邻壳层、缝合下降、CRT 周期和尾镜像，
都应在某个小阶 h×h 方阵内强制产生零行，
从而与下阶 Row(h) 或有限基底事实矛盾。
```

结论：该路线在有限账本中得到全分支支持；但要达到论文级无条件证明，还需把有限相位命中升级为
全局 `TotalDescent-TM` 定理，或证明所有非命中相位进入 `SAE/PDEC/ColumnCRT`。

## 1. 统一下降对象

设 `p<q` 为相邻素数。假设 `q×q` 方阵第 `s` 行，`2<=s<=q`，为 `q`-筛零行：

\[
I_s^{(q)}=[(s-1)q+1,sq].
\]

由相邻壳层单点性，在 `q^2` 内旧 `p`-筛唯一合数幸存者是 `q^2`。因此：

```text
s<q:  I_s^(q) 是旧 p-筛零窗；
s=q:  I_q^(q) 是旧 p-筛零窗，至多带端点穿孔 q^2。
```

这一步已经同时覆盖 aligned、seam 和末行端点三类情形。

## 2. 任意下层 h 的复活点公式

对任意素数 `h<=p`，从旧 `p`-筛零窗降到 `h`-筛后，唯一可能复活的点为

\[
\operatorname{Rev}_{h,p}(I)=
\{n\in I:\ P^-(n)>h,\ P^-(n)\le p\},
\]

并在末行额外加入 `q^2` 穿孔。若完整 `h` 对齐行 `J_R` 满足

\[
J_R\subset I,\qquad J_R\cap \operatorname{Rev}_{h,p}(I)=\varnothing,
\]

且不含端点穿孔，则第 `R` 条 `h` 行被条件强制为零行。

这一步把“不同路径”统一成同一个判据：aligned 分支只是 `h=p` 时已经找到完整行；seam 分支则继续
下降到更小 `h`，直到出现避开复活点的完整行。

## 3. CRT 周期头部与尾镜像

令

\[
M_h=\prod_{\ell\le h}\ell,\qquad N_h={M_h\over h},\qquad
\rho(R)=((R-1)\bmod N_h)+1.
\]

若第 `R` 条 `h` 行为零行，则第 `\rho(R)` 条行也为零行；取负映射给出镜像相位

\[
\rho^\ast=N_h-\rho(R)+1.
\]

因此只要

\[
\rho(R)\le h
\quad\text{or}\quad
\rho^\ast\le h,
\tag{TM}
\]

该条件零行就经周期性或尾镜像落入 `h×h` 方阵头部。若归纳假设 `Row(h)` 已成立，则矛盾。

## 4. 总审计账本

新增：

```text
experiments/prime_matrix_total_zero_row_descent_audit.py
docs/monograph/prime-matrix-total-zero-row-descent-audit.md/json
docs/monograph/prime-matrix-total-zero-row-descent-audit-p2000-sample.md/json
```

全量 `p<=500`：

```text
q rows checked = 21936
initial type counts = {'aligned_p_row_contained': 597, 'seam_window': 21339}
forced zero found = 21936
matrix head or tail hits = 21936
unclosed rows = 0
terminal puncture rows = 93
hit mode counts = {'direct_head_phase': 29065, 'tail_mirror_phase': 13357}
```

确定性抽样 `p<=2000,row_stride=25`：

```text
q rows checked = 11583
initial type counts = {'aligned_p_row_contained': 95, 'seam_window': 11488}
forced zero found = 11583
matrix head or tail hits = 11583
unclosed rows = 0
terminal puncture rows = 301
hit mode counts = {'direct_head_phase': 15739, 'tail_mirror_phase': 6501}
```

也就是说，在测试域中：

```text
任意非第一 q 行假设为零
=> 旧 p 零窗或端点穿孔零窗
=> 某层 h 出现强制 h 零行
=> h 行相位或尾镜像相位落入 h×h
=> 与下阶 Row(h) 归纳输入冲突。
```

## 5. 证明链条的最窄剩余

当前总路线已经不再需要在多个分支之间来回转换。所有分支统一为一个命题：

```text
TotalDescent-TM(q):
对任意相邻 p<q 和任意 2<=s<=q，
若 I_s^(q) 是旧 p-筛零窗（末行允许 q^2 穿孔），
则存在 h<=p 和完整 h 行 J_R⊂I_s^(q)，使
  J_R 避开 Rev_{h,p}(I_s^(q)) 与端点穿孔，
  且 rho(R)<=h 或 N_h-rho(R)+1<=h。
```

若 `TotalDescent-TM(q)` 对所有 `q` 成立，则可用强归纳证明 `Row(q)`：

1. 基底小素数直接验证；
2. 假设所有 `h<q` 的 `Row(h)` 成立；
3. 若 `q` 方阵有非第一零行，由相邻壳层单点性进入 `TotalDescent-TM(q)`；
4. 得到某个 `h<q` 的 `h×h` 方阵条件零行；
5. 与归纳假设矛盾。

## 6. 审稿边界

需要明确三点：

1. 这不是“实验证明”。实验说明总下降机制没有发现反例；论文仍需证明 `TotalDescent-TM`。
2. “与实证矛盾”应在正式稿中改写为“与有限基底验证和强归纳输入 `Row(h)` 矛盾”。
3. 若 `TotalDescent-TM` 全局证明暂缺，则唯一剩余出口是证明非命中相位集合必触发
   `SAE/PDEC/ColumnCRT`。这比早期的 `SeamGuard-Elimination` 更窄、更可审查。

所以当前最优攻坚目标不是再换命题，而是直接证明：

```text
TotalDescent-TM
or
NonHit-Phase => SAE/PDEC/ColumnCRT。
```
