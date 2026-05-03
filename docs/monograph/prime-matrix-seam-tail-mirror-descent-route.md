# Seam 尾镜像递归下降路线

**状态：** `conditional_tail_mirror_descent_supported_not_global_proof`

本文分析用户提出的加强路径：

```text
高阶零行
=> 相邻壳层剥离成 seam 零窗
=> seam 多层下降得到某阶 h 的强制零行
=> 该 h 零行未必以绝对行号落入 h×h 方阵
=> 但它可能落在 h-筛 CRT 周期的头部相位或尾镜像相位
=> 由周期性和镜像刚性反推 h×h 方阵内零行
=> 与下阶 Row(h) 冲突。
```

该路线是合理的，但必须用“CRT 行相位”表述，而不是只看绝对行号。

## 1. 严格镜像公式

固定小阶素数 `h`，令

\[
M_h=\prod_{\ell\le h}\ell,\qquad N_h={M_h\over h}.
\]

第 `R` 条 `h` 对齐行的非平凡列为

\[
n_{R,c}=(R-1)h+c,\qquad 1\le c<h.
\]

行相位为

\[
\rho(R)=((R-1)\bmod N_h)+1.
\]

若第 `R` 行是 `h`-筛零行，则周期性给出第 `\rho(R)` 行也是零行。取负映射给出

\[
M_h-n_{R,c}\equiv -n_{R,c}\pmod {M_h},
\]

并在非平凡列上把 `c` 送到 `h-c`。所以零行相位的 CRT 镜像为

\[
\rho^\ast=N_h-\rho+1.
\]

因此：

```text
若 rho<=h，则零行周期相位直接落入 h×h 方阵；
若 rho*<=h，则尾边界零行镜像落入 h×h 方阵。
```

第二种就是用户指出的“尾边界区通过镜像强制头部方阵零行”。

## 2. 与 seam 多层下降的连接

由 `prime-matrix-seam-multilevel-descent-route.md`，若 seam 区间 `I` 已经是旧 `p`-筛零窗，
降到 `h<p` 后复活点为

\[
\operatorname{Rev}_{h,p}(I)=\{n\in I:P^-(n)>h,\ P^-(n)\le p\},
\]

最后 `q` 行另加 `q^2` 端点穿孔。若存在完整 `h` 行 `J_R⊂I` 且

\[
J_R\cap \operatorname{Rev}_{h,p}(I)=\varnothing,
\]

则在该 seam 反例假设下，第 `R` 条 `h` 行被强制为零行。

如果进一步满足

\[
\rho(R)\le h\quad\text{or}\quad N_h-\rho(R)+1\le h,
\tag{TM}
\]

则该条件零行经周期性或尾镜像落入 `h×h` 方阵头部。这时只要下阶 `Row(h)` 已作为归纳输入成立，
seam 反例立即矛盾。

## 3. 有限审计

新增：

```text
experiments/prime_matrix_seam_tail_mirror_descent_audit.py
docs/monograph/prime-matrix-seam-tail-mirror-descent-audit.md/json
docs/monograph/prime-matrix-seam-tail-mirror-descent-audit-p2000-sample.md/json
```

全量 `p<=500`：

```text
seam windows checked = 21339
forced zero found = 21339
head or tail mirror hits = 21339
blocked without hit = 0
hit mode counts = {'direct_head_phase': 28279, 'tail_mirror_phase': 12984}
```

确定性抽样 `p<=2000,row_stride=25`：

```text
seam windows checked = 11488
forced zero found = 11488
head or tail mirror hits = 11488
blocked without hit = 0
hit mode counts = {'direct_head_phase': 15603, 'tail_mirror_phase': 6397}
```

这比上一层 `SMD` 更强：不仅 seam 多层下降会产生条件强制零行，而且在这些样本中总能找到
周期头部或尾镜像命中，从而落回小阶方阵头部。

## 4. 对递归证明的意义

这给出一条更清晰的归纳路线：

```text
假设 Row(h) 对所有 h<q 已成立。
若 q 方阵出现零行：
  1. 相邻壳层单点性把它降为旧 p-筛 q 零窗；
  2. 完整 p 行分支直接与 Row(p) 矛盾；
  3. seam 分支进入多层下降；
  4. 若满足 (TM)，则在某个 h<q 的 h×h 方阵内强制零行；
  5. 与归纳假设 Row(h) 矛盾。
```

因此新的核心硬点可以压缩为：

```text
TailMirror-SMD:
任意真实 seam 反例在多层下降中必存在满足 (TM) 的强制 h-零行；
若不存在，则持久非命中阻断必触发 SAE/PDEC/ColumnCRT。
```

有限账本显示 `TailMirror-SMD` 在测试域内没有反例。

## 5. 审稿边界

必须避免两个跳步：

1. `R<=h` 不是必要条件。真正条件是 `rho(R)<=h` 或 `rho*(R)<=h`。
2. `TailMirror-SMD` 目前仍是有限审计支持的条件接口；全局论文中必须证明 `(TM)` 总能发生，
   或把不发生的相位集合转入 `SAE/PDEC/ColumnCRT`。

所以该路线不是“有限实验已经闭合”，而是把 seam guard 的剩余义务变成更窄的相位命中不等式。
