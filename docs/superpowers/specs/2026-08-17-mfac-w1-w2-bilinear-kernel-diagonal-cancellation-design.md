# MFAC W1→W2 双线性核对角—非对角抵消审计设计

**日期：**2026-08-17
**状态：**已确认，待实施计划

## 目标

为 W1→W2 的互素限制 Möbius 尾和统一 L² 缺口新增一个完全非循环的有限双线性核
审计器。它固定有限能量的精确核展开、对角项与非对角项账本，并审计任何候选
“对角—非对角抵消”引理的量词、常数依赖和有限后果。

本工作不预设、也不宣称能证明互素限制尾和的统一界。其目的在于将真正需要的新输入
定位为：对带符号 Möbius 系数的非对角项必须提供何种可审查抵消，避免把核的正半定性、
有限数值或逐点绝对值界误写成统一 L² 上界。

## 精确有限对象

给定整数截断 `D >= 3`，令

\[
a_d=\frac{\mu(d)}{d}\quad(2\le d<D),
\qquad
T_D(r)=\sum_{\substack{2\le d<D\\r\mid d}}a_d.
\]

定义 Euler--φ 加权有限能量

\[
E_D=\sum_{r=2}^{D-1}\varphi(r)T_D(r)^2.
\]

交换有限求和并使用
\(\sum_{r\mid n}\varphi(r)=n\)，得到精确核恒等式

\[
E_D=\sum_{2\le d,e<D}a_da_eK(d,e),
\qquad
K(d,e)=\gcd(d,e)-1.
\]

记

\[
\operatorname{Diag}_D=\sum_{2\le d<D}a_d^2(d-1),
\qquad
\operatorname{Off}_D=
\sum_{\substack{2\le d,e<D\\d\ne e}}a_da_e(\gcd(d,e)-1),
\]

则 `E_D = Diag_D + Off_D` 精确成立。`K` 也是有限 Gram 核：

\[
K(d,e)=\sum_{\substack{2\le r<D\\r\mid d,\ r\mid e}}\varphi(r).
\]

此正半定性只说明 `E_D >= 0`；它不控制 `E_D` 对 `D` 的统一有界性。由于对角账本
本身可能增长，任何成功路线都必须给出带符号的非对角抵消，而不能诉诸“对角支配”。

## 候选新引理的最小合同

审计器接受一个 `Mapping`，其中必须登记：

- `kernel_identity`：`True`，仅指上述有限求和恒等式已核验；
- `gram_positivity`：`True`，仅指有限 Gram 表示与非负性；
- `offdiagonal_cancellation_lemma`：`False` 或带有明确量词的外部证明包；
- `uniformity_variable`：固定为 `"truncation"`；
- `constant_dependency`：仅允许预注册有限依赖，例如 `"fixed_test_function"`；
- `uses` 与 `claimed_uses`：每项只允许有限算术、Möbius 定义、最大公约数、
  Euler--φ 除数和恒等式、有限 Gram 分解与有限求和重排。

当未提供逐步可审查的、对所有截断统一的抵消证明时，审计器必须固定输出：

```text
finite_kernel_identity_status=verified_finite
finite_gram_positivity_status=verified_finite
diagonal_cancellation_obligation_status=open
coprime_restricted_tail_bound_status=open
w1_to_w2_status=unproved
rh_proved=false
```

`offdiagonal_cancellation_lemma=True` 不能由调用者单独填入；除非同时提交可机器定位的
证明记录、全称量词、常数依赖及来源，否则必须拒绝。有限尺度上观察到
`Off_D < 0` 或 `E_D <= C`，只能登记为 `finite_cancellation_witnessed`。

## 禁止循环与错误升级

禁止来源至少包括：`Mertens`、`PNT`、`RH`、`zeta_zero`、`zero_free_region`、
`explicit_formula`、`Mellin`、`Chebyshev_error`、`target_energy_bridge`、
`chebyshev_energy_bridge`、`finite_profile`、`numerical_experiment`。

禁止结论字段至少包括：`uniform_l2_upper_proved`、
`coprime_restricted_tail_bound_proved`、`w1_to_w2_proved`、`w2_closed`、
`chebyshev_energy_bridge_proved`、`rh_proved`、`rh_consequence`。

尤其禁止以下错误推理：

1. 从 `K` 正半定推出 `E_D` 对所有 `D` 有界；
2. 从有限 `Off_D < 0` 或有限能量读数推出全局抵消；
3. 以逐模数绝对值界替代平均的带符号非对角抵消；
4. 以目标的统一 L²--Upper、Chebyshev 桥或 RH 反向证明抵消引理。

## 架构

新增 `experiments/prime_matrix_mfac_w1_w2_bilinear_kernel_cancellation_audit.py`，包含：

1. 严格合同验证器与禁止依赖防火墙；
2. 模块内精确 Möbius、Euler--φ、`gcd` 核和 Gram 分解；
3. `Fraction` 有限模型，逐项核验三种能量写法、对角—非对角分解和 Gram 残差；
4. 有限抵消见证记录器，仅输出有限状态；
5. JSON/Markdown 证书写入器和脚本路径 CLI。

新增配套单元测试，覆盖：合法最小合同、未知/禁止来源、额外未核验义务、伪造抵消引理、
非法截断、精确核恒等式、Gram 非负性、对角—非对角残差、有限见证和 CLI 证书边界。

## 非目标

- 不证明 `Off_D` 存在统一负抵消界。
- 不证明互素限制尾和的统一 L²--Upper、Euler--φ 统一聚合、Chebyshev 传递、
  Mellin 收缩、零自由区域或 RH。
- 不接入已有 W1→W2 解析桥或 Chebyshev 桥并改变其状态。
- 不把有限正半定、有限反例搜索或有限负交叉项升级为任意全局解析结论。

## 使用示例

```bash
python3 -m unittest \
  experiments.prime_matrix_mfac_w1_w2_bilinear_kernel_cancellation_audit_test -v

python3 experiments/prime_matrix_mfac_w1_w2_bilinear_kernel_cancellation_audit.py \
  --limit 512
```

## 验收条件

- 对每个有限 `D`，divisor-sum、双线性 `gcd-1` 核和 Gram 表示三种能量精确相等。
- `Diag_D + Off_D - E_D` 与全部 Gram 残差使用 `Fraction` 精确为零。
- 任何有限抵消读数均只报告 `finite_cancellation_witnessed`，全部统一性与主链状态保持 `open` 或 `unproved`。
- 核正半定、伪造全局抵消、禁止来源和目标结论循环均有负向测试。
- JSON/Markdown/CLI 明确说明该模块不证明统一 L² 界、W1→W2 或 RH。
