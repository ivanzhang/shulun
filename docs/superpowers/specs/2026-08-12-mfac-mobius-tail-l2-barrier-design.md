# MFAC Möbius 尾和整体 L² 门槛设计

**日期：** 2026-08-12

**状态：** 已确认方向，待用户审阅书面规格

## 1. 目的

本规格不再试图为固定线性截断 Möbius--log 系数族证明统一正强制性，而是审计下列相反命题：该族在极限中心化整除核上的归一化能量是否至多为 \(O(1/\log D)\)。

若该上界被严格证明，则它只否定这个**固定系数族**存在尺度无关的正强制常数；它不否定所有受限系数族、任何尚未定义的 MFAC 构造、Chebyshev 能量桥、Mellin 收缩或 RH。

## 2. 固定系数与极限比率

对整数 \(D\ge3\)，定义

\[
a_D(d)=-\mu(d)\log d\left(1-\frac{\log d}{\log D}\right),
\qquad 2\le d<D.
\]

定义极限核能量和质量

\[
E_D=
\sum_{2\le d,e<D}a_D(d)a_D(e)
\left(\frac{(d,e)}{de}-\frac1{de}\right),
\qquad
W_D=\sum_{2\le d<D}\frac{a_D(d)^2}{d},
\]

并设 \(R_D=E_D/W_D\)。

有限 \(X\) 审计仅用于检查 \(D=\lfloor X^\vartheta\rfloor\) 时有限核趋近极限核；本规格中的定理量词全部关于 \(D\)，不把有限采样当作证明。

## 3. 精确 Euler--\(\varphi\) 分解

利用恒等式

\[
\frac{(d,e)}{de}=\sum_{r\mid(d,e)}\frac{\varphi(r)}{de},
\]

有严格有限重排

\[
E_D=
\sum_{2\le r<D}\varphi(r)\,|T_D(r)|^2,
\]

其中

\[
T_D(r)=
\sum_{\substack{r\mid d\\2\le d<D}}\frac{a_D(d)}d.
\]

若 \(r\) 非平方自由则 \(T_D(r)=0\)。当 \(r\) 平方自由且 \(d=rm\) 时，

\[
T_D(r)=
-\frac{\mu(r)}r
\sum_{\substack{m<D/r\\(m,r)=1}}
\frac{\mu(m)\log(rm)}m
\left(1-\frac{\log(rm)}{\log D}\right).
\]

该分解为有限代数恒等式，只使用 Möbius 乘法性、Euler \(\varphi\) 的因子和恒等式和有限求和交换；不得调用 `psi(X)-X`、Mellin、零点、显式公式或 RH。

## 4. 待证/待证伪命题

### L2--Upper（主负面命题）

存在绝对常数 \(C>0\) 与 \(D_0\)，使对所有 \(D\ge D_0\)，

\[
E_D\le C(\log D)^2.
\]

### Mass--Lower（分母义务）

存在绝对常数 \(c>0\) 与 \(D_1\)，使对所有 \(D\ge D_1\)，

\[
W_D\ge c(\log D)^3.
\]

二者同时成立时，严格推出

\[
R_D\le\frac{C}{c\log D},
\]

从而固定系数族的尺度无关正强制性被 `refuted_for_fixed_linear_mobius_log_family`。

## 5. 证明分层与允许输入

### A. 纯有限/初等层

必须独立完成：

1. `EulerPhiSquareSumIdentity`：第 3 节精确分解；
2. `FiniteToLimitKernelError`：从 floor 恒等式导出的有限核误差；
3. `MassLower`：给出 \(W_D\) 的明确下界，记录是否只使用非负性、平方自由计数或外部结果；
4. 有限尺度反例/一致性证书。

### B. Möbius 消去层

`L2--Upper` 的唯一未闭合数学门是整体和

\[
\sum_{r<D}\varphi(r)|T_D(r)|^2\ll(\log D)^2.
\]

不得把逐个 \(T_D(r)\) 的强上界当作必要目标；优先寻找整体平方和、双线性重排、卷积正性或大筛型估计。

若任何推导使用下列输入，必须逐条在 `uses` 中声明并将结论标为 `conditional_on_named_mobius_estimate`：

```text
PNT
Mertens_cancellation
zero_free_region
zeta_zero
explicit_formula
Mellin
RH
```

调用外部无条件定理本身并不自动违规，但它不能被伪装为“由 MFAC 结构自足推出”，且必须列出完整定理、常数、适用范围与引用。

## 6. 反证与停止条件

下列证据分别对应不同结论：

- 若构造 \(D_j\to\infty\) 并严格证明 \(R_{D_j}\ge c_0>0\)，则 `L2--Upper` 被否定；
- 若只能有限扫描得到 \((\log D)R_D\) 稳定，状态只能是 `numerical_only`; 
- 若 `Mass--Lower` 成立而 `L2--Upper` 依赖未声明的 Mertens/PNT 型消去，则停止，状态为 `mobius_cancellation_dependency_unresolved`；
- 若两条不等式都仅在有限 \(D\) 被检查，则不得宣称固定系数族已被反证；
- 即使固定族被严格反证，`rh_proved=false` 保持不变。

## 7. 当前数值线索（非定理）

截至 2026-08-12，极限核扫描给出：

| \(D\) | \(R_D\) | \((\log D)R_D\) |
| ---: | ---: | ---: |
| 32 | 0.220789580080 | 0.765198374649 |
| 256 | 0.162641755931 | 0.901877396517 |
| 1024 | 0.134991231739 | 0.935687916801 |
| 4096 | 0.111654013027 | 0.928711971936 |

这些读数支持但不证明 \(R_D\asymp1/\log D\)。它们只能用于选择后续引理和反例搜索范围。

## 8. 验收标准

- 所有有限恒等式以精确有理核或可验证代数重排单独测试；
- `Mass--Lower` 与 `L2--Upper` 分开记录，不允许用分母经验增长替代证明；
- 每个外部输入都有 `uses`、来源、适用区间和条件标签；
- 数值剖面、外推猜想、条件命题与已证明命题具有不同状态；
- 任何结果均明确写出：不构成 Chebyshev 能量桥、Mellin 收缩、零自由区域或 RH 证明。

## 使用示例

计划中的有限诊断命令形式：

```bash
python3 experiments/prime_matrix_mfac_mobius_tail_l2_audit.py \
  --cutoff 4096 --json-out /tmp/mfac-mobius-tail-l2.json
```

该命令只检查 Euler--\(\varphi\) 分解、有限层贡献和数值归一化；不会输出 `L2--Upper proved` 或任何 RH 结论。
