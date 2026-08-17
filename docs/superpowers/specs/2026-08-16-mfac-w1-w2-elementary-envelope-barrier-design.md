# MFAC W1→W2 初等绝对值包络障碍审计设计

**日期：**2026-08-16
**状态：**已确认，待实施计划

## 目标

为 W1→W2 的 Möbius 尾和缺口增加一个完全非循环的“初等绝对值包络”审计器。
它精确核验有限 Möbius 尾和、三角不等式包络与 Euler--φ 聚合之间的关系，并登记
该包络是否仍随截断尺度增长。产物的目的在于排除“仅靠绝对值估计即可得到统一 L²
上界”的错误路线，而不是证明所需的消去估计。

本工作不证明 W1→W2、互素限制尾和的统一 L²--Upper、Euler--φ 的统一聚合、
Chebyshev 能量桥、Mellin 收缩、零自由区域或 RH。

## 非目标

- 不接受 Mertens、PNT、RH、零点、零自由区域、显式公式、Mellin 或 Chebyshev 误差。
- 不将有限截断增长、有限样本单调性或数值拟合提升为全局发散定理。
- 不替代或修改既有非循环 Möbius 尾和审计器、W1→W2 解析桥合同或 Chebyshev 桥合同。
- 不改动隔离工作树以外的主工作区未提交文件。

## 数学对象

给定整数截断 `D >= 3`，对每个 `2 <= r < D` 定义精确有限尾和

\[
T_D(r)=\sum_{\substack{r\mid d\\2\le d<D}}\frac{\mu(d)}{d}.
\]

其互素展开为

\[
T_D(r)=\frac{\mu(r)}{r}
\sum_{\substack{rm<D\\(m,r)=1}}\frac{\mu(m)}{m}.
\]

丢弃 Möbius 符号后，定义初等绝对值包络

\[
B_D(r)=\frac{|\mu(r)|}{r}
\sum_{\substack{rm<D\\(m,r)=1}}\frac{1}{m}.
\]

有限模型以精确 `Fraction` 验证

\[
|T_D(r)|\le B_D(r),
\qquad
E_D=\sum_{r=2}^{D-1}\varphi(r)T_D(r)^2
\le
A_D=\sum_{r=2}^{D-1}\varphi(r)B_D(r)^2.
\]

这里 `E_D` 是精确有限代数能量，`A_D` 只是无消去上包络。两者都不是渐近定理。

## 增长见证

审计器在给定有限 `D` 上记录 `r=2` 的包络分量和可选 dyadic 截断序列。它可以验证：

- `B_D(2)^2` 是 `A_D` 的非负有限组成部分；
- 指定有限 dyadic 尺度上的读数与预先声明的块下界比较；
- 若有限序列出现增长，只能写为 `finite_growth_witnessed`。

审计器不得宣称该有限序列证明了 `D→∞` 的发散。任何将初等包络升级为“无法存在统一
常数”的全局解析结论，必须保留为 `nonuniformity_obligation_open`，直到提供逐步可审查的
全称证明。

## 架构

新增 `experiments/prime_matrix_mfac_w1_w2_elementary_envelope_barrier_audit.py`，包含：

1. 严格合同验证器与禁止依赖防火墙；
2. 模块内精确 Möbius、Euler--φ、尾和与绝对值包络算术；
3. 有限逐模数不等式、聚合不等式及 `r=2` 增长见证；
4. JSON/Markdown 证书写入器和脚本路径 CLI。

新增配套单元测试，覆盖合法合同、禁止来源、目标结论提升、精确有限不等式、非法截断、
dyadic 见证与 CLI 证书边界。

## 合同边界

合同仅允许 `finite_arithmetic`、`mobius_definition`、`coprimality_relation`、
`triangle_inequality`、`finite_sum_identity` 作为来源。

禁止来源至少包括 `Mertens`、`PNT`、`RH`、`zeta_zero`、`zero_free_region`、
`explicit_formula`、`Mellin`、`Chebyshev_error`、`target_energy_bridge`、
`chebyshev_energy_bridge`、`finite_profile`、`numerical_experiment`。

禁止结论字段至少包括 `uniform_l2_upper_proved`、`w1_to_w2_proved`、`w2_closed`、
`chebyshev_energy_bridge_proved`、`rh_proved`、`rh_consequence`。

默认产物必须保持：

```text
finite_inequality_status=verified_finite
finite_growth_status=finite_growth_witnessed
nonuniformity_obligation_status=open
w1_to_w2_status=unproved
rh_proved=false
```

## 使用示例

```bash
python3 -m unittest \
  experiments.prime_matrix_mfac_w1_w2_elementary_envelope_barrier_audit_test -v

python3 experiments/prime_matrix_mfac_w1_w2_elementary_envelope_barrier_audit.py \
  --limit 512 --dyadic-levels 5
```

## 验收条件

- 每个 `2 <= r < D` 的精确三角不等式均被核验，且聚合不等式残差非负。
- `r=2` 与 dyadic 见证只报告有限读数，不升级为全局发散或解析上界结论。
- 禁止输入、未声明的逐义务来源和目标结论循环均有负向测试。
- JSON/Markdown/CLI 明确区分 `verified_finite`、`finite_growth_witnessed` 与 `open`。
- 新模块与已提交的 W1→W2 合同测试共同通过，主工作区既有未提交文件不受影响。
