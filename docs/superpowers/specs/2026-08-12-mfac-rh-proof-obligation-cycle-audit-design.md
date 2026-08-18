# MFAC→RH 证明义务与循环依赖审计设计

**日期：** 2026-08-12

**状态：** 已确认结构，待用户审阅书面规格

## 1. 目的与范围

本规格只覆盖 MFAC 主线：从不读取目标误差的实际整数系数/见证构造，经过统一去常数强制性、实际 Chebyshev 误差的无循环能量桥、dyadic 到 Mellin 的可和性、再到一个明确的零点结论，最后才讨论是否能推出 RH。

它的任务不是证明 RH，也不把有限数值、经验随机性、自由模型、形式恒等式或条件估计升级为定理。它把每一步所需的全称命题、允许输入、禁止输入、当前证据、逻辑角色与循环风险固定下来，使任何后续“突破”都能被逐边审查。

不纳入 B3/Perron/轮廓积分链，也不纳入 MFAC 的全部 payload/router 支线；仅在它们为实际非循环见证的前置缺口时，作为 `origin_orientation_gate` 记录。

## 2. 主证明义务链

主链节点按顺序编号为 `W0` 到 `W5`：

```text
W0  独立实际算术见证与来源/取向合同
 │
 ▼
W1  统一去常数强制性
 │
 ▼
W2  实际 Chebyshev 误差的无循环能量桥
 │
 ▼
W3  dyadic 能量到 Mellin 范数的无条件可和性
 │
 ▼
W4  Mellin 半平面收缩到明确零点排除命题
 │
 ▼
W5  由已声明零点排除命题推出 RH
```

每一条箭头都表示逻辑上必要的独立引理包；任一节点为 `finite_only`、`conditional`、`unproved` 或 `cycle_detected` 时，后续节点不得升级为 `proved`。

### W0：独立实际算术见证与来源/取向合同

**输入：** 整数索引、预注册的算术规则、有限因子分解和不读取目标误差的固定参数。

**输出义务：** 给出对全部允许尺度和全部相关实际行/列的明确见证族；逐项指定 `origin`、`registration`、`orientation`、`local_factor` 与精确索引恒等式，并证明它不是既有目标误差、零点信息或下游 pushforward 的重编码。

**禁止输入：** `psi(X)-X`、`Chebyshev_error`、`Mellin`、`zeta_zero`、`explicit_formula`、`RH`，以及由这些对象后验拟合或校准的参数。

**当前状态：** `unproved`。现有 LCM 直接秩一投影中，唯一正交系数为

\[
\alpha_X=\frac{\psi(X)-X}{X},
\]

因此该模板已被拒绝为循环；现有 origin/orientation 审计也未给出独立 actual primitive emitter。

**对 RH 的作用：** 必要前置，不充分。

### W1：统一去常数强制性

**输入：** W0 的独立实际见证、实际 LCM/中心化整除核及预注册范数。

**输出义务：** 存在与候选维度、截断范围和 dyadic 尺度无关的常数 \(c>0\)，使全部允许去常数向量满足明确能量下界。必须写出量词、范数、余项和可吸收范围。

**禁止替代：** 有限最小特征值、正主子式、Gershgorin 读数、有限尺度扫描、固定 Möbius--log 系数族的经验比率。

**当前状态：** `unproved`。截断 Möbius--log 族只有有限证书；其 Euler--\(\varphi\) 尾和审计还留下 `Mass--Lower` 与整体 `L2--Upper` 两个未证明义务。

**对 RH 的作用：** 必要前置，不充分。

### W2：实际 Chebyshev 误差的无循环能量桥

**输入：** W0、W1，以及独立定义的实际 Chebyshev 误差对象。

**输出义务：** 对所有充分大尺度，以不读取该尺度 \(\psi(X)-X\) 的系数、投影或调参方式，证明实际误差产生的负载进入 W1 的能量，并得到明示的非循环不等式。

**禁止输入：** 以 \(\psi(X)-X\) 选择正交投影、系数或中心化常数；以待证误差界反推能量参数；以 `Mellin`、零点或显式公式倒灌该桥。

**当前状态：** `not_started`。直接 \(e_1\) 投影因唯一正交系数读取目标误差而被标为 `cycle_detected`；这只否决该秩一模板，不否决所有可能的实际见证。

**对 RH 的作用：** 必要前置，不充分。

### W3：dyadic 能量到 Mellin 范数的无条件可和性

**输入：** W2 给出的实际 dyadic 能量控制、固定权重和明确 Mellin 定义域。

**输出义务：** 独立证明跨尺度求和/积分引理，说明权重、收敛半平面、边界项和常数来源；结论不能依赖 RH、零自由区域或被控制的 Mellin 范数本身。

**禁止替代：** 仅有限 dyadic 样本、经验收缩、Möbius 层内洗牌、自由乘法模型、未经证明的交换求和/极限步骤。

**当前状态：** `not_started`。自由 Mellin 增长反模型表明交替、守恒与形式 divisor identity 本身不足以强迫平方根型收缩。

**对 RH 的作用：** 必要前置，不充分。

### W4：Mellin 半平面收缩到明确零点排除

**输入：** W3 的无条件 Mellin 范数控制，以及一个完全写明的解析延拓/变换恒等式。

**输出义务：** 指定零点对象、半平面、边界线、极点处理和从 Mellin 控制到“该区域无非平凡零点”的完整蕴含。若使用外部复分析定理，必须记录定理原文、假设、常数和使用位置。

**禁止输入：** 直接假设零自由区域、显式公式的 RH 型余项、零点位置或等价于待证结论的解析延拓界。

**当前状态：** `not_started`。当前 MFAC 语料没有实际 Mellin 收缩，更没有零点排除引理。

**对 RH 的作用：** 若零点排除区域为 \(\Re s>1/2\)，则该节点是走向 RH 的充分前置；否则仅为部分零自由结论。

### W5：从零点排除到 RH

**输入：** W4 的明确零点排除命题，以及函数方程/对称性等已单独声明的标准事实。

**输出义务：** 精确说明如何将 `Re(s)>1/2` 的零点排除与临界带、函数方程对称性合并，推出所有非平凡零点实部为 \(1/2\)。

**禁止替代：** “Mellin 收缩看起来像 RH”、有限零点验证、未经声明的零点对称性或已假定的 RH 等价命题。

**当前状态：** `not_started`，并固定 `rh_proved=false`。

**对 RH 的作用：** 只有 W0--W4 均由独立无循环定理闭合时，W5 才可执行。

## 3. 循环边清单

审计器必须把下列反向边视为阻断边，而不是辅助证据：

| 编号 | 反向边 | 判定 | 原因 |
| --- | --- | --- | --- |
| C1 | `Chebyshev_error → W0/W2` | `cycle_detected` | 用 \(\psi(X)-X\) 选择实际见证、正交系数或投影，会把待控制量写入构造。 |
| C2 | `Mellin_norm → W2` | `cycle_detected` | 用待建立的 Mellin 收缩反推 Chebyshev 能量桥，不能提供独立控制。 |
| C3 | `zero_free_region / zeta_zero → W3/W4` | `cycle_detected` | 用零点信息证明所需可和性或收缩，再由收缩推出零点排除，是闭环。 |
| C4 | `RH → W1--W5` | `cycle_detected` | 任何 RH、RH 等价界或隐含平方根消去输入都不能参与本路线的正向证明。 |
| C5 | `finite_profile → W1/W3/W4` | `insufficient_not_cycle` | 有限样本不构成全称定理；它可用于反例搜索或选择引理。 |
| C6 | `free_multiplicative_model → W3` | `insufficient_not_cycle` | 自由模型可否定“形式交替足够”的论证，但不能提供实际整数收缩。 |
| C7 | `Mertens/PNT cancellation → W1 tail L2` | `conditional_dependency` | 可作为明示外部条件使用，但不能被标为 MFAC 自足推导，且不能自动推进 W2--W5。 |

任何未列出的边若读取了后继节点的结论、目标对象或等价信息，默认分类为 `cycle_suspected`，直至给出独立来源证明。

## 4. 机器可读状态合同

后续审计产物应保存以下字段：

```text
scope=mfac_only_rh_proof_obligation_cycle_audit
w0_independent_actual_witness_status
w1_uniform_offconstant_coercivity_status
w1_fixed_mobius_tail_l2_status
w2_actual_chebyshev_energy_bridge_status
w3_dyadic_to_mellin_summability_status
w4_mellin_to_zero_free_region_status
w5_zero_free_region_to_rh_status
cycle_edges
conditional_dependencies
finite_evidence_only
rh_proved=false
```

允许状态仅为：`proved`、`unproved`、`not_started`、`finite_only`、`conditional`、`cycle_detected`、`insufficient_not_cycle`。`proved` 必须附带独立定理引用或本仓库中可检查的完整证明；没有该证据时不得使用。

## 5. 验收标准与停止条件

审计交付必须同时满足：

1. 每个 W 节点都有输入、全称输出、禁止输入、当前状态和 RH 逻辑角色；
2. 每条循环边都写明源、目标、判定和理由；
3. 固定 Möbius--log 尾和审计只影响 W1 的特定候选族，不得外推到全部 MFAC 见证；
4. 直接 \(e_1\) 投影的循环只否决该模板，不得伪装为全体非秩一构造不可能；
5. 任何外部 PNT/Mertens/零点输入都标记为条件依赖；
6. 成果明确保持 `rh_proved=false`，除非 W0--W5 各自都有独立、无循环、全称证明。

本规格的下一次实现只允许生成依赖图、状态证书和一致性测试；不得新增“RH 已证明”或“实际 Mellin 收缩已建立”的字段。

## 6. 使用示例

计划中的审计命令形式：

```bash
python3 experiments/prime_matrix_mfac_rh_proof_obligation_cycle_audit.py \
  --json-out /tmp/mfac-rh-cycle.json \
  --markdown-out /tmp/mfac-rh-cycle.md
```

该命令只能读取预注册的节点/边合同与既有状态，输出缺失引理清单和循环边；不会计算或宣称 RH 结论。
