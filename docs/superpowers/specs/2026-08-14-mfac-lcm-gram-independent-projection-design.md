# MFAC LCM Gram 独立投影恒等式合同设计

**日期：** 2026-08-14

**状态：** 已确认设计，待用户审阅书面规格

## 1. 目的

本阶段为 W1→W2 桥接建立一个严格独立的 Hilbert 空间接口：对任意 dyadic 区间
上的 \(L^2\) 函数，预注册的正交投影能量是否可精确表示为一个 LCM Gram 二次型。
该接口只涉及投影、特征、内积、Gram 核和去常数方向；它不以 \(\psi-t\)、
\(\Lambda-1\) 或任何 Chebyshev 误差数据定义子空间、基底或系数。

本阶段不证明 Chebyshev 能量桥。即使投影—Gram 恒等式未来闭合，还必须独立证明
\(f=\psi-t\) 被该独立投影控制，并独立控制正交残差 \((I-P_X)(\psi-t)\)。

## 2. 空间、量词与恒等式

对每个充分大的实数 \(X\)，定义

\[
H_X=L^2([X,2X]),
\]

内积为 \(\langle f,g\rangle_X=\int_X^{2X}f(t)\overline{g(t)}\,dt\)。预注册一个
由独立整除特征生成的闭子空间 \(\mathcal V_X\subseteq H_X\)，及其正交投影
\(P_X:H_X\to\mathcal V_X\)。

待证明的接口具有全称量词：存在 \(X_0\ge1\)，使对所有实数 \(X\ge X_0\) 和所有
\(f\in H_X\)，有

\[
\|P_Xf\|_{H_X}^2=\mathcal G_{\mathrm{LCM}}(X;f).
\]

其中右端必须是显式注册的 LCM Gram 二次型。有限整数 \(X\)、有限维矩阵或数值样本
只能核对归一化，不能替代“所有充分大实数 \(X\)、所有 \(f\)”的恒等式。

## 3. 独立投影注册合同

`projection_contract` 必须为 Mapping，包含：

```text
space: "L2([X,2X])"
quantifier: "exists_X0_for_all_real_X_ge_X0_and_all_f_in_HX"
feature_family: 非空字符串
feature_independence: "registered_independent_of_chebyshev_target"
closed_subspace: true
orthogonal_projection: true
constant_projection: 非空字符串
uses: 非裸字符串的字符串序列
```

`feature_family`、`constant_projection` 只描述独立整除特征和去常数方向；它们不是
证明。`closed_subspace` 与 `orthogonal_projection` 必须为内建 `True`，否则拒绝。

`gram_contract` 必须为 Mapping，包含：

```text
kernel: 非空字符串
coefficient_coordinates: 非空字符串
normalization: 非空字符串
lcm_overlap: "registered_lcm_divisibility_overlap"
constant_projection: 与 projection_contract 一致的非空字符串
uses: 非裸字符串的字符串序列
```

两个 `constant_projection` 必须字符串完全一致；不允许用相似名称推断一致性。

## 4. 禁止输入与循环防护

`projection_contract.uses`、`gram_contract.uses` 和顶层 `uses` 合并后，必须拒绝：

```text
Chebyshev_error
psi(X)-X
Lambda(n)-1
target_energy
Mellin
zero_free_region
zeta_zero
explicit_formula
RH
PNT
Mertens_cancellation
```

任何目标误差、后继解析结论或外部素数分布输入都会破坏 W1→W2 的独立性。出现时
审计器必须拒绝，不降级为条件合同。

若提供 `claimed_identity_uses`，其每一项必须属于已声明 `uses` 并且不得是禁止项。
顶层不得含 `actual_chebyshev_projection`、`residual_control`、`w2_closed`、
`rh_proved` 或 `projection_identity_proved` 等目标结论循环字段。

## 5. 状态与证书

一个有效合同只能输出：

```text
projection_space_status=registered_unproved
lcm_gram_identity_status=registered_unproved
finite_normalization_status=not_used_as_proof
actual_chebyshev_projection_status=not_started
residual_control_status=not_started
w2_actual_chebyshev_energy_bridge_status=unproved
rh_proved=false
```

默认 CLI 生成 JSON 和 Markdown。证书必须记录空间、全称量词、独立特征声明、
LCM overlap、去常数一致性、禁止输入检查和来源子集检查；并写明它不证明正交投影
存在、Gram 恒等式、\(f=\psi-t\) 的控制、残差吸收、W2、Mellin、零自由区或 RH。

## 6. 测试与验收

测试至少覆盖：

1. 合法合同只能登记未证明投影—Gram 恒等式，且 RH 始终为假；
2. 量词、空间、独立特征字段、闭子空间/正交投影布尔值、LCM overlap、归一化和
   去常数方向字段缺失或错误时被拒绝；
3. 两个去常数方向名称不一致时被拒绝；
4. 裸字符串、非字符串 `uses`、未声明 `claimed_identity_uses` 被拒绝；
5. 禁止输入和目标结论循环字段在任一层出现都被拒绝；
6. JSON/Markdown 与脚本路径 CLI 始终保留 W2/RH 未证明边界；
7. 全量 MFAC 回归测试通过。

完成实现后只提交本规格、本计划、新投影审计器、新测试和两种证书；必须先运行
`git diff --check` 与全量 MFAC 测试，且不得混入既有未提交文件。

## 7. 非目标

- 不构造、逼近或计算任何具体 \(P_X\)、\(\mathcal V_X\)、\(\mathcal G_{\mathrm{LCM}}\)；
- 不证明对所有充分大实数 \(X\) 的恒等式；
- 不以有限 LCM 矩阵检查替代抽象恒等式；
- 不把 `actual_lcm_gram_energy` 或其他现有审计器自动提升为本合同实例；
- 不处理 \(f=\psi-t\) 的投影可控性或残差；
- 不输出 W2、Chebyshev 能量桥、Mellin、零自由区或 RH 已证明。

## 使用示例

```bash
python3 experiments/prime_matrix_mfac_lcm_gram_independent_projection_audit.py \
  --json-out /tmp/mfac-lcm-projection.json \
  --markdown-out /tmp/mfac-lcm-projection.md
```

该命令只登记独立投影—Gram 接口，不运行具体投影、不读取 Chebyshev 数据，也不证明 RH。
