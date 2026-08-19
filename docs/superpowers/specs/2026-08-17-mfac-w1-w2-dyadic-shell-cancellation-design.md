# MFAC W1→W2 相邻 Dyadic 壳抵消与可和残余审计设计

**日期：**2026-08-17
**状态：**已确认，待实施计划

## 目标

为 W1→W2 的 Möbius 双线性核增加一个“相邻 dyadic 壳抵消”审计器。它把有限核能量
按系数尺度分为对角壳质量、同壳/相邻壳交叉项和远壳交叉项，并把得到统一 L² 上界所需的
解析新输入拆成三个明确义务：近邻支付、残余可和、远壳聚合。

本工作不证明这三个义务，也不证明互素限制尾和统一 L²--Upper、W1→W2、Chebyshev 能量桥或 RH。
它的作用是排除“有限负交叉项已构成统一抵消”的错误升级，并给未来直接解析证明提供唯一、可证伪的量词接口。

## 精确有限分解

令 `D >= 3`，`a_d=μ(d)/d`，并定义

\[
K(d,e)=\gcd(d,e)-1,
\qquad
E_D=\sum_{2\le d,e<D}a_da_eK(d,e).
\]

对 `j >= 1` 定义截断 dyadic 壳

\[
I_j(D)=\{d:2\le d<D,\ 2^j\le d<\min(2^{j+1},D)\},
\]

以及精确块核账本

\[
Q_{j,k}(D)=\sum_{d\in I_j(D)}\sum_{e\in I_k(D)}a_da_eK(d,e).
\]

令

\[
\Delta_j(D)=\sum_{d\in I_j(D)}a_d^2(d-1),
\]

\[
N_j(D)=\sum_{\substack{d,e\in I_j(D)\\d\ne e}}a_da_eK(d,e)
+2Q_{j,j+1}(D),
\]

\[
F_D=\sum_{|j-k|\ge2}Q_{j,k}(D).
\]

有限恒等式必须精确核验：

\[
E_D=\sum_j\bigl(\Delta_j(D)+N_j(D)\bigr)+F_D.
\]

`N_j` 的定义故意将同壳非对角项与相邻壳全部有序交叉项合并；它不等同于单个壳的正性或负性。

## 候选解析证明包

以下三项是得到统一能量控制的**充分候选义务**，不是本规格声称已成立的定理：

1. **相邻壳支付。** 存在 `j0`、`η>0`、`C_near>0`，使对所有 `j>=j0` 和所有足够大截断 `D`，
   \[
   \Delta_j(D)+N_j(D)\le C_{near}2^{-\eta j}.
   \]
2. **残余可和。** 上式的常数和阈值独立于 `D`，故
   \[
   \sum_{j\ge j0}C_{near}2^{-\eta j}<\infty.
   \]
3. **远壳聚合。** 存在与 `D` 无关的 `C_far`，使
   \[
   F_D\le C_{far}
   \]
   对所有足够大 `D` 成立。

若三项均有独立、非循环、逐步可审查的证明包，则有限初始壳可被固定常数吸收，从而给出候选的
`coprime_restricted_tail_bound`。该蕴含仅记录为待证明的逻辑模板；审计器不得因为有限壳读数自动设为成立。

## 合同与状态

合同必须登记：

- `kernel_block_identity=True`：仅指有限壳分解恒等式；
- `adjacent_shell_cancellation_lemma=False`；
- `summable_residual_lemma=False`；
- `far_shell_aggregation_lemma=False`；
- `uniformity_variable="truncation"`；
- `constant_dependency="fixed_test_function"`；
- `uses` 与每项 `claimed_uses`：只允许有限算术、Möbius 定义、最大公约数、dyadic 分解、
  Euler--φ 除数和恒等式、有限求和重排。

默认产物必须保持：

```text
finite_shell_ledger_status=verified_finite
finite_near_cancellation_status=finite_cancellation_witnessed_or_not_witnessed
adjacent_shell_cancellation_obligation_status=open
summable_residual_obligation_status=open
far_shell_aggregation_obligation_status=open
coprime_restricted_tail_bound_status=open
w1_to_w2_status=unproved
rh_proved=false
```

任一候选解析义务的 `True` 值都必须被拒绝，除非未来另有包含完整证明记录、全称量词、独立常数账本及来源追踪的新版本合同。

## 禁止循环与错误升级

禁止来源至少包括：`Mertens`、`PNT`、`RH`、`zeta_zero`、`zero_free_region`、
`explicit_formula`、`Mellin`、`Chebyshev_error`、`target_energy_bridge`、
`chebyshev_energy_bridge`、`tail_l2_upper`、`coprime_restricted_tail_bound`、
`finite_profile`、`numerical_experiment`。

禁止结论字段至少包括：`uniform_l2_upper_proved`、
`coprime_restricted_tail_bound_proved`、`w1_to_w2_proved`、`w2_closed`、
`chebyshev_energy_bridge_proved`、`rh_proved`、`rh_consequence`。

特别拒绝：

1. 从某个有限 `N_j(D)<0` 推出所有壳的近邻支付；
2. 从有限 `F_D` 有界或样本拟合推出统一远壳聚合；
3. 让 `C_near`、`η`、`C_far`、`j0` 依赖截断或样本范围；
4. 以当前目标统一界、Chebyshev 桥、RH 或 Mertens/PNT 类结论反向证明三个义务。

## 架构

新增 `experiments/prime_matrix_mfac_w1_w2_dyadic_shell_cancellation_audit.py`，提供：

1. 严格合同验证器、来源白名单和结论升级防火墙；
2. 模块内 `Fraction` Möbius、Euler--φ、`gcd` 核和 dyadic 壳构造；
3. 精确 `Q_{j,k}` 块账本、近邻/远壳/总能量重组残差；
4. 有限近邻抵消见证，仅记录有限符号；
5. JSON/Markdown 证书写入器和 CLI。

新增配套测试，覆盖合法合同、非法截断、未知/禁止来源、额外未核验义务、伪造三项解析引理、
精确壳账本、截断边界壳、有限见证和 CLI 状态边界。

## 非目标

- 不证明相邻壳支付、残余可和或远壳聚合。
- 不构造借用 Mertens、PNT、Mellin、零点或显式公式的替代证明。
- 不把有限壳的负交叉项、有限残差或测试通过升级为统一 L² 上界。
- 不修改已提交的双线性核、非循环尾和或解析桥审计接口。

## 使用示例

```bash
python3 -m unittest \
  experiments.prime_matrix_mfac_w1_w2_dyadic_shell_cancellation_audit_test -v

python3 experiments/prime_matrix_mfac_w1_w2_dyadic_shell_cancellation_audit.py \
  --limit 512
```

## 验收条件

- 对每个有限截断，块核、近邻/远壳账本和总能量重组全部以 `Fraction` 精确为零。
- 截断边界壳被单独列出，不被伪装成完整 dyadic 壳。
- 任何有限负 `N_j(D)` 只登记有限见证，三项候选解析义务全部保持 `open`。
- 禁止来源、截断依赖常数、伪造引理和目标结论循环均有负向测试。
- JSON、Markdown 和 CLI 清楚说明：相邻壳账本不是统一 L² 或 RH 的证明。
