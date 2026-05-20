# 三命题 actual-load 闭合合同

## 0. 结论边界

本文把最新的 formal-to-actual 临界负载原则落成三个可执行闭合合同：

```text
PM-ALC: Prime Matrix actual packet critical-load contract
TP-ALC: Two-point actual ratio denominator-floor contract
RH-ALC: RH final-load controlled-exit contract
```

这些合同不是三命题无条件证明。它们的作用是把下一步硬攻变成可验证的输入/输出格式：哪些量是 actual load，哪些只是 formal envelope，失败时进入哪个命名出口。

## 1. PM-ALC：Prime Matrix actual packet 合同

### 1.1 当前机器证书

本轮新增脚本：

```text
experiments/prime_matrix_affine_twin_actual_packet_contract.py
```

输出：

```text
data/prime-matrix-affine-twin-actual-packet-contract-ledger.json
docs/monograph/prime-matrix-affine-twin-actual-packet-contract.json
docs/monograph/prime-matrix-affine-twin-actual-packet-contract.md
```

当前 sweep 结论：

```text
candidate_q_values=[31, 43, 103]
actual_q_values_current=[31]
total_formal_product_upper=40
total_actual_packet_count_current=1
total_formal_to_actual_gap=39
all_actual_packets_pass_sqrt_gate_current=true
projection_collision_pdec_count_current=0
row_column_unconditional_closed=false
```

这说明当前数据中，形式上界 `M_q^{form}` 远大于 actual packet 数 `N_q`。临界负载必须按 `N_q^2` 计，而不能按 `(A_gA_f)^2` 计。

### 1.2 合同陈述

**PM-ALC.** 对每个持久 AffineTwin `q>=13`，构造实际包集合 `Pi_q`，并证明分解

\[
\Pi_q=\Pi_q^{prim}\sqcup \Pi_q^{esc}\sqcup \Pi_q^{pdec}.
\]

要求：

1. `Pi_q^{prim}` 注入 primitive support，宽度为

   \[
   W_q=(q+9)/2\le\sqrt{q(q-2)}.
   \]

2. `Pi_q^{pdec}` 是 projection collision、repeated residue、reset 或 ColumnCRT/PDEC。
3. `Pi_q^{esc}` 是 primitive support escape，必须 SAE 可求和或另成 PDEC。
4. Rankin/SAE 质量只按 actual load 计：

   \[
   A_q=|\Pi_q^{prim}|^2+|\Pi_q^{esc}|^2,
   \]

   不按形式包络 `(A_gA_f)^2` 计。

### 1.3 闭合条件

若

\[
|\Pi_q^{prim}|\le W_q,\qquad
\sum_q {|\Pi_q^{esc}|\over q(q-2)}<\infty,
\]

且 `Pi_q^{pdec}` 全部被排斥，则 AffineTwin 超平方根分支被吸收。

当前最窄剩余：

```text
ProductAccountingTightening
PrimitiveTwinSlotSupportExhaustion
PrimitiveTwinSlotSupportEscape-PDEC/SAE
```

### 1.4 formal-pair pruning 更新

后续审计

```text
experiments/prime_matrix_affine_twin_formal_pair_pruning_audit.py
data/prime-matrix-affine-twin-formal-pair-pruning-ledger.json
docs/monograph/prime-matrix-affine-twin-formal-pair-pruning-audit.md
```

把当前 sweep 的 `ProductAccountingTightening` 进一步展开为可逐项检查的删除账本：

```text
formal_pair_total=40
actual_packet_total_current=1
formal_to_actual_gap=39
crt_window_empty_pair_total_current=11
source_unmaterialized_pair_total_current=28
unresolved_formal_pair_total_current=0
current_formal_gap_fully_pruned=true
```

其中 `q=31` 的 `12=3 x 4` 个 formal residue 配对已逐个 CRT 枚举，只有 `(generator residue, fill residue)=(19,8)` 在 pair support `[2669,2688]` 中给出代表 `2687`；其余 `11` 个是 `CRTWindowEmpty`。`q=43,103` 在当前方向没有 matching gap-fill source materialization，分别删除 `16` 与 `12` 个未物化配对。

这关闭的是当前 sweep 的形式账本收紧缺口，不是全局证明。全局最窄剩余相应改写为：

```text
GlobalProductAccountingTightening
SourceMaterializationFailure-PDEC/SAE
CRTWindowEmptyGlobalSupportBound
PrimitiveTwinSlotSupportEscape-PDEC/SAE
```

### 1.5 source materialization gate 更新

后续审计

```text
experiments/prime_matrix_affine_twin_source_materialization_gate_audit.py
data/prime-matrix-affine-twin-source-materialization-gate-ledger.json
docs/monograph/prime-matrix-affine-twin-source-materialization-gate-audit.md
```

把 `SourceMaterializationFailure` 继续拆成源门控不变量：

```text
source_gate_pass_q_values=[31]
source_gate_fail_q_values=[43, 103]
formal_pairs_blocked_by_source_gate=28
same_gap_wrong_source_formal_pair_count=16
no_gap_source_formal_pair_count=12
all_source_failures_classified_current=true
```

源门控要求：

```text
gap=q,
generator=q-2,
fill=q,
sides match AffineTwin orientation,
p_delay=(11q-21)/4,
slot-lock source key agrees when present.
```

当前 `q=43` 有同 gap source，但实际为 `generator=47, fill=43, sides=plus->minus, p_delay=74`，而 AffineTwin 期望 `generator=41, fill=43, sides=minus->plus, p_delay=113`，故阻断 `16` 个 formal products。`q=103` 当前无任何 gap-fill source，阻断 `12` 个 formal products。

全局最窄剩余进一步压成：

```text
GlobalSourceMaterializationGate
SameGapWrongSource-PDEC/SAE
NoGapSource-PDEC/SAE
CRTWindowEmptyGlobalSupportBound
```

### 1.6 CRT window gap 更新

后续审计

```text
experiments/prime_matrix_affine_twin_crt_window_gap_audit.py
data/prime-matrix-affine-twin-crt-window-gap-ledger.json
docs/monograph/prime-matrix-affine-twin-crt-window-gap-audit.md
```

把 `CRTWindowEmpty` 从布尔空窗推进为带距离的相位间隙证书：

```text
source_gate_pass_q_values=[31]
formal_pair_total_with_exact_source=12
supported_actual_packet_total_current=1
crt_window_gap_pair_total_current=11
min_empty_window_distance=40
max_empty_window_distance=434
modulus_minus_support_width_current=879
crt_window_gap_closed_current_sweep=true
```

当前 `q=31` 的 exact-source formal pairs 全部由模数 `29*31=899` 的 CRT 类控制，共同 pair support 为 `[2669,2688]`，宽度 `20`。唯一 actual packet 是 `(generator residue, fill residue)=(19,8)`，代表 `2687`；其余 `11` 对的最近 CRT 代表距窗口至少 `40`，因此不是边界贴合或数值误差，而是严格正间隙。

全局最窄剩余继续压成：

```text
GlobalCRTWindowGapBound
WindowEdgeCollision-PDEC
SupportMotionEscape-PDEC/SAE
```

### 1.7 window edge-collision 更新

后续审计

```text
experiments/prime_matrix_affine_twin_window_edge_collision_audit.py
data/prime-matrix-affine-twin-window-edge-collision-ledger.json
docs/monograph/prime-matrix-affine-twin-window-edge-collision-audit.md
```

把 `CRTWindowGap` 的下一失败形态写成 residue 网格位移：

```text
target_window_pair_count=20
edge_collision_candidate_count_current=11
min_empty_l1_residue_displacement=1
max_empty_l1_residue_displacement=11
empty_pairs_target_existing_actual_count=2
empty_pairs_target_unused_residue_arrival_count=9
window_edge_collision_displacement_closed_current_sweep=true
```

共同窗口 `[2669,2688]` 诱导 `20` 个可命中的 target residue pairs。当前 `11` 个空窗 formal pairs 要变成 actual packet，必须移动到这些 target 之一；最近的单点为 `(19,9)->(19,8)`，只需 fill residue 位移 `-1`，因此成为下一轮最窄 atom。其余 `9` 个最近目标不在当前 actual pair 上，需要新的 target residue arrival。

全局最窄剩余继续压成：

```text
GlobalWindowEdgeCollisionDisplacementBound
ExistingActualResidueCollision-PDEC
UnusedTargetResidueArrival-PDEC/SAE
SupportMotionEscape-PDEC/SAE
```

## 2. TP-ALC：二点筛 actual ratio 合同

### 2.1 actual ratio

二点筛终局需要：

\[
R_Y=
{1\over |U_Y(I)|}
\sum_{x\in U_Y(I)}D_Y^P(x)<1.
\]

这里：

\[
D_Y^P(x)=\#\{Y<p\le P:p\mid x(x-2)\}.
\]

BMD/KLS 只提供分子分布输入。要推出 TLI，必须同时给出 denominator floor。

### 2.2 合同陈述

**TP-ALC.** 取固定 `alpha in (2/3,1)`，`Y=P^alpha`。在同一 Buchstab/奇异级数 convention 下证明：

\[
\sum_{x\in U_Y(I)}D_Y^P(x)
\le (K(\alpha)+\varepsilon(\alpha))\mathcal M_Y(I),
\]

\[
|U_Y(I)|\ge (1-\delta(\alpha))\mathcal M_Y(I),
\]

并且

\[
K(\alpha)+\varepsilon(\alpha)<1-\delta(\alpha).
\]

其中

\[
K(\alpha)=
{2\log((2-\alpha)/\alpha)\over
1+\log((2-\alpha)/\alpha)}.
\]

### 2.3 失败出口

若分母地板失败，则不得把 BMD 写成 TLI 终局，而必须登记为：

```text
DenominatorFloor-PDEC
CharacterDefect
EndpointSmoothingDefect
ParityTransferGap
```

当前最窄剩余：

```text
BMDToTLI-CriticalDenominatorFloor
```

## 3. RH-ALC：RH final-load controlled-exit 合同

### 3.1 actual final load

RH 线已有定义：

\[
\operatorname{Load}(E;X)
=\sum_{a\mapsto E}\theta_{a,E}\operatorname{Excess}(a),
\]

且

\[
\operatorname{Excess}(a)
=\max(0,\sigma\sum_{n\in a}(w_X(n)-w_X^0(n))).
\]

这已经扣除零频 baseline，并要求 source-deleted transfer 不重复计数。

### 3.2 合同陈述

**RH-ALC.** 对每个出口

```text
E in {A, PI, FCT, SC, LV, LSMP, CE, DSO, NRC}
```

建立四列表：

| 项 | 必须证明 |
|---|---|
| input actual load | 进入 `E` 的 atoms 已扣除 baseline |
| closure mechanism | capacity、absorption、descent、transfer 或外部定理 |
| no double counting | source-deleting，internal descent 不计 final load |
| terminal inequality | `Load(E;X)=o(X^{beta-o(1)})` 或 strict descent |

同时保持入口下界：

\[
\sum_E\operatorname{Load}(E;X)\ge X^{\beta-o(1)}.
\]

若所有出口上界都完成，则 off-critical zero anomaly 无处承载，RH 矛盾场才可能升级。

当前最窄剩余：

```text
ControlledExitCriticalLoadNormalization
```

## 4. 三合同统一矩阵

| 合同 | actual load | critical capacity | 当前可证状态 | 剩余硬点 |
|---|---:|---:|---|---|
| PM-ALC | `N_q^2` | `q(q-2)` | 当前 sweep actual packet、source gate、CRT gap、edge-collision 位移、existing-actual CRT 跳跃、unused-target arrival、support-motion depth、fixed-primitive defect 与同向 moving-key 深度公式闭合 | 全局 moving primitive key nonpersistence |
| TP-ALC | actual `sum D / |U_Y|` | `1` with Buchstab `K(alpha)` | 分子 BMD 外部版可用 | denominator floor / parity gap |
| RH-ALC | source-deleted final load | exit capacity | verification ledger 已有 | controlled exits 逐项归一化 |

## 5. 当前下一步

最直接的继续硬攻顺序是：

1. **PM：** 当前固定 key 与同向 moving-key 深度公式都已不能吸收 support motion；下一步主攻方向改变/source 重物化的 primitive key 迁移，或登记为 `OrientationChangingPrimitiveKey-PDEC/SAE`、`SourceRematerialization-PDEC/SAE`。
2. **TP：** 写出 denominator floor 的 beta/Buchstab 下筛合同，明确 `delta(alpha)` 的可接受上限。
3. **RH：** 生成 controlled-exit 四列表，先不证明 RH，只把每个 exit 的 actual-load 输入、闭合机制和未闭合项固定。

这三个动作都直接服务于目标命题无条件化，但都不会越界声称终局已经完成。

## 6. PM existing-actual CRT jump 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-existing-actual-collision-jump-audit.md
data/prime-matrix-affine-twin-existing-actual-collision-jump-ledger.json
```

继续把上一节的 `(19,9)->(19,8)` 单 fill-residue atom 从 residue 网格位移提升到 CRT 相位跳跃。当前结果为：

```text
existing_actual_collision_candidate_count=2
existing_actual_target_pair_count=1
min_existing_actual_residue_l1=1
min_abs_crt_jump_to_existing_actual=120
max_abs_crt_jump_to_existing_actual=435
support_width_current=20
existing_actual_collision_jump_closed_current_sweep=true
```

双模 CRT 单位步长为 `generator_unit=465`、`fill_unit=435`。因此最窄 atom `19:9 -> 19:8` 虽然只有 `L1=1`，但相位上必须跳 `435`，远大于共同支撑宽度 `20`；另一个 existing-actual 候选 `15:12 -> 19:8` 也要跳 `120`。

这一步把 existing-actual 分支的当前 sweep 关闭为：它不是窗口边缘微小滑入，而是完整 CRT 相位跳跃。全局剩余仍是证明这种跳跃不能随支撑移动持久复现，或把复现登记为 `RepeatedResidue-ColumnCRT-PDEC` / `SupportMotionEscape-PDEC/SAE`。

## 7. PM unused-target arrival 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-unused-target-arrival-audit.md
data/prime-matrix-affine-twin-unused-target-arrival-ledger.json
```

继续把 `WindowEdgeCollision` 中另一个分支压成新侧残基到达账本。当前结果为：

```text
unused_target_arrival_candidate_count=9
unique_unused_target_pair_count=5
required_unique_side_residue_arrival_count=9
occurrence_new_side_residue_requirement_total=17
min_abs_crt_jump_to_unused_target=59
max_abs_crt_jump_to_unused_target=375
support_width_current=20
unused_target_arrival_closed_current_sweep=true
```

`9` 个候选只落到 `5` 个唯一 target pairs：`10:30`、`16:5`、`17:6`、`18:7`、`20:9`。它们全部不在当前形式积中；要让这些 target 变成 actual，必须新增 generator residues `[10,16,17,18,20]` 和 fill residues `[5,6,7,30]`，合计 `9` 个新侧残基。

最窄 unused-target atom 是 `19:12 -> 20:9`，只需一个新 generator residue，但 CRT 跳跃仍为 `59`，大于共同窗口宽度 `20`。因此当前 unused-target 分支也不是 hidden actual load，而是明确的新残基到达/支撑移动义务。

## 8. PM support-motion depth 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-support-motion-depth-audit.md
data/prime-matrix-affine-twin-support-motion-depth-ledger.json
```

继续把剩余的 `SupportMotionEscape` 分支压成端点释放与深度膨胀账本。当前结果为：

```text
support_motion_candidate_count=11
support_motion_side_histogram={'above': 3, 'below': 8}
support_width_current=20
min_required_common_side_depth=58
max_required_common_side_depth=435
min_endpoint_release_total_required=70
max_endpoint_release_total_required=863
support_motion_depth_closed_current_sweep=true
```

当前 generator phase 为 `[2669,2693]`，shifted-fill phase 为 `[2659,2688]`，共同支撑为 `[2669,2688]`。因此要靠移动支撑吞掉空窗 CRT 代表，不能只移动一个端点；同侧的 generator 端点和 shifted-fill 端点都必须释放，并且两侧深度必须同步膨胀到同一个代表距离。

最窄 support-motion atom 是 `19:12`，nearest representative 为 `2629`：它需要共同侧深度 `58`，即 generator 深度额外 `40`、fill 深度额外 `30`，总端点释放 `70`。这把 support-motion 从泛称逃逸压成可审计的同步深度膨胀义务。

## 9. PM support-motion primitive-depth defect 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-support-motion-primitive-defect-audit.md
data/prime-matrix-affine-twin-support-motion-primitive-defect-ledger.json
```

继续把 support-motion 的同步深度膨胀接回固定 AffineTwin primitive 身份。当前结果为：

```text
support_motion_primitive_defect_candidate_count=11
min_total_affine_depth_defect=70
max_total_affine_depth_defect=863
all_support_motion_breaks_both_depth_identities=true
fixed_primitive_key_support_motion_absorption_closed_current_sweep=true
```

最小缺陷 atom 仍是 `19:12`。它要求共同侧深度 `58`，但当前 `q=31` 的 AffineTwin 深度恒等式给出 generator 左深度 `18`、fill 左深度 `28`，因此产生 generator 缺陷 `40`、fill 缺陷 `30`，总缺陷 `70`。

于是当前固定 primitive key 分支已经关闭：support motion 若要继续，就不能保持当前 `q=31` primitive key，必须移动 primitive key 或进入 `MovingPrimitiveKey-PDEC/SAE`、`MovingSupportDepthInflation-PDEC/SAE`、`EndpointReleaseCoupling-PDEC`。

## 10. PM moving-key depth formula 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-moving-key-depth-formula-audit.md
data/prime-matrix-affine-twin-moving-key-depth-formula-ledger.json
```

继续检查“移动 primitive key”是否可用同向 AffineTwin 深度公式吸收当前 support-motion 深度。当前结果为：

```text
moving_key_depth_formula_candidate_count=11
min_lower_q_candidate_gap=50
max_lower_q_candidate_gap=375
min_above_fill_right_depth_residual=341
max_above_fill_right_depth_residual=434
same_orientation_moving_key_depth_absorption_closed_current_sweep=true
```

lower-side 同向吸收要求 `(q+5)/2=D` 且 `q-3=D`，即 `q=2D-5` 与 `q=D+3` 必须相等；这只在 `D=8` 时可能。当前最窄 lower atom `19:12` 的 `D=58`，generator 公式给 `q=111`，fill 公式给 `q=61`，差距 `50`。

above-side 同向吸收要求 `(q-7)/4=D` 且 `fill_right_depth=1=D`，而当前 above depths 最小也为 `342`。因此当前支撑运动不能被同向 moving AffineTwin key 吸收；剩余只剩方向改变、source 重物化或 key 迁移的全局非持久性证明。

## 11. PM moving-key source-rematerialization 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-moving-key-source-rematerialization-audit.md
data/prime-matrix-affine-twin-moving-key-source-rematerialization-ledger.json
```

继续检查 moving key 是否能在别的 `q` 上重新物化为同向 AffineTwin source。审计把上一节深度公式给出的所有单侧候选 `q` 全部过 prime gate 与 source gate：

```text
moving_q_formula_occurrence_count=19
unique_moving_q_candidate_count=19
prime_candidate_q_values=[61,181,293,761,1499,1747]
affine_twin_prime_gate_q_values=[]
exact_rematerialized_q_values=[]
route_histogram={CompositeQ:13,PrimeButNotTwinAffine:6}
moving_key_source_rematerialization_closed_current_sweep=true
```

最窄 depth atom `19:12` 给出候选 `q=111` 与 `q=61`。其中 `111` 为合数；`61` 虽与 `59` 同为素数，但 `61≡1 mod 4`，使 AffineTwin 期望延迟 `(11q-21)/4` 非整数，且当前没有 gap `q=61` 的 matching source。最接近的已物化 source 是 gap `59`，角色为 `generator=61, fill=59, sides=minus->minus, p_delay=70`，不是 `q=61` 期望的 `generator=59, fill=61, sides=minus->plus`。

因此当前同向 moving-key source-rematerialization 通道也关闭。全局剩余继续压成方向改变、source 重物化的非持久性证明，或进入 `OrientationChangingPrimitiveKey-PDEC/SAE`、`SourceRematerialization-PDEC/SAE`、`EndpointReleaseCoupling-PDEC`。

## 12. PM endpoint-release critical-error 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-critical-error-audit.md
data/prime-matrix-affine-twin-endpoint-release-critical-error-ledger.json
```

把剩余 support-motion 逃逸接入“临界误差必须结构化”的统一原则。定义当前局部端点释放临界误差为：

```text
endpoint critical error = actual endpoint-release load / support width - 1
```

其中 support width 是 primitive 双槽共同支撑窗口宽度 `20`，actual endpoint-release load 是把空窗 CRT 代表拉入窗口所需的 generator 与 shifted-fill 双端点同步释放总量。当前证书给出：

```text
support_motion_candidate_count=11
critical_capacity_support_width=20
total_endpoint_release_load=4929
total_window_capacity_budget=220
total_endpoint_release_critical_error=21.4045454545
min_endpoint_release_critical_error=2.5
max_endpoint_release_critical_error=42.15
all_endpoint_release_loads_supercritical=true
all_same_orientation_rematerialization_absent=true
endpoint_release_critical_error_structured_current_sweep=true
```

最窄显式超界点仍是 `19:12`：端点释放负载为 `70`，窗口容量为 `20`，临界误差为 `50/20=2.5`。它的 moving q 候选 `[61,111]` 已在上一节证明不能同向重物化为 AffineTwin source。因此这个正临界误差不能保留为匿名波动，只能显化为 `EndpointReleaseCoupling-PDEC`。

本步关闭的是当前 sweep 的“匿名端点释放超界”解释，而不是全局行/列命题。全局剩余继续是排斥 `EndpointReleaseCoupling-PDEC` 持久复现，或处理方向改变/source 重物化出口。

## 13. PM endpoint-release feedback-loss 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-feedback-loss-audit.md
data/prime-matrix-affine-twin-endpoint-release-feedback-loss-ledger.json
```

继续把端点释放临界误差拆成“几何支撑回补”和“第二端点反馈损耗”。即使把较大端点移动量全部记作支撑扩张信用，仍剩：

```text
feedback loss = endpoint release load - geometric support gain credit
              = min(generator release, fill release)
post-credit feedback error = feedback loss / support width - 1
```

当前证书给出：

```text
support_motion_candidate_count=11
support_width=20
total_endpoint_release_load=4929
total_geometric_support_gain_credit=2512
total_coupled_second_endpoint_feedback_loss=2417
total_post_credit_feedback_error=9.98636363636
min_feedback_loss=30
max_feedback_loss=429
min_post_credit_feedback_error=0.5
all_feedback_losses_exceed_support_width=true
endpoint_release_feedback_loss_structured_current_sweep=true
```

最窄 atom 仍是 `19:12`：负载 `70` 中最多 `40` 可解释为几何支撑扩张，剩余反馈损耗 `30` 仍超过原支撑宽度 `20`，post-credit feedback error 为 `0.5`。因此即便允许局部超界通过支撑移动做自反馈回补，当前 sweep 仍留下不可匿名化的 `EndpointReleaseFeedbackLoss-PDEC`。

本步不证明全局不可能出现持久端点反馈；它把剩余硬点从 `EndpointReleaseCoupling-PDEC` 压窄为 `EndpointReleaseFeedbackLoss-PDEC` 的全局排斥或路由。

## 14. PM endpoint-release feedback-horizon 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-feedback-horizon-audit.md
data/prime-matrix-affine-twin-endpoint-release-feedback-horizon-ledger.json
```

继续把 feedback loss 改写成纯相位地平线判据：

```text
feedback horizon = support width + |generator side depth - fill side depth|
phase horizon surplus = window distance - feedback horizon
```

当前证书给出：

```text
support_motion_candidate_count=11
support_motion_side_histogram={above:3,below:8}
support_width=20
total_window_distance=2512
total_feedback_horizon_width=315
total_phase_horizon_surplus=2197
min_phase_horizon_surplus=10
max_phase_horizon_surplus=409
all_feedback_loss_formulas_hold=true
all_representatives_outside_feedback_horizon=true
endpoint_release_feedback_horizon_structured_current_sweep=true
```

最窄 atom `19:12` 的 CRT 代表距窗口 `40`，当前 support width 为 `20`，两端点侧深度差为 `10`，所以 feedback horizon 为 `30`，相位地平线缺口为 `10`。这把局部超界自反馈的显式矛盾点压成：

```text
反例链要求支撑移动吸收距离 40 的代表；
真实链最大自反馈吸收地平线只有 30。
```

本步关闭当前 sweep 的端点自反馈吸收通道，并把剩余硬点压成 `EndpointReleaseFeedbackHorizon-PDEC` 的全局排斥或路由。

## 15. PM endpoint-release feedback-horizon slack 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-feedback-horizon-slack-audit.md
data/prime-matrix-affine-twin-endpoint-release-feedback-horizon-slack-ledger.json
```

把上一层 `phase horizon surplus` 再压成“必须新增的 side-depth skew”：

```text
required total skew = max(0, window distance - support width)
required extra skew = required total skew - current side-depth skew
required extra skew = phase horizon surplus
```

当前证书给出：

```text
support_motion_candidate_count=11
support_width=20
total_required_absorption_skew=2292
total_current_side_depth_skew=95
total_required_extra_skew=2197
current_skew_coverage_ratio=0.0414485165794
extra_skew_deficit_ratio=0.958551483421
min_required_extra_skew=10
all_required_extra_skews_equal_phase_surpluses=true
all_pure_orientation_flips_fail_absorption=true
same_orientation_source_rematerialization_absent=true
feedback_horizon_slack_structured_current_sweep=true
```

最窄 atom 仍是 `19:12`：CRT 代表距离 `40`，support width `20`，吸收所需总 skew 为 `20`；当前 skew 为 `10`，必须额外增长 `10`。纯方向翻转保持绝对 skew，因此不能缩短该缺口；同向 moving-key 候选 `[61,111]` 继承 source-rematerialization 账本后仍无精确重物化。

本步把当前最窄剩余从“地平线缺口”进一步压成 `EndpointSkewGrowth-PDEC/OrientationChangingPrimitiveKey-SAE`：若反例链要继续吸收该缺口，就必须提供新的 skew-growth 机制、方向改变 primitive key，或进入 source 重物化/SAE 出口。全局行/列命题仍未无条件闭合。

## 16. PM endpoint-release bidirectional skew-hull 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-bidirectional-skew-hull-audit.md
data/prime-matrix-affine-twin-endpoint-release-bidirectional-skew-hull-ledger.json
```

把上一层逐行 slack 放回局部逆元对齐框架：每个 formal pair 给出一个关于 `P` 的 CRT 类

```text
P = generator_residue (mod q-2)
P = shifted_fill_residue (mod q)
```

然后求当前周期中同时包含全部 formal pair 最近代表的最小相位壳层。当前证书给出：

```text
formal_alignment_row_count=12
empty_alignment_row_count=11
combined_crt_modulus=899
support_interval=[2669,2688]
support_width=20
alignment_hull_interval=[2304,3122]
alignment_hull_width=819
left_extension_required=365
right_extension_required=434
left_extra_skew_after_feedback_horizon=335
right_extra_skew_after_feedback_horizon=409
bidirectional_extra_skew_after_shared_hull=744
modulus_minus_hull_width=80
affine_p_delay=80
hull_complement_equals_affine_p_delay=true
one_sided_skew_growth_absorption_closed_current_sweep=true
```

这给出比逐行缺口更全局的局部刚性：反例链若要把 `q=31` 的 `12` 个 formal pair 同时塞回一个支撑壳层，壳层宽度必须达到 `819`，已经占 `899` 周期的约 `91.10%`，只留下 affine `p_delay=80` 大小的互补缝。真实链当前 primitive 支撑宽度只有 `20`，扣除 feedback horizon 后仍要双向额外增长 `335+409=744`。

本步关闭当前 sweep 的单侧 skew-growth 吸收解释，并把剩余压成 `BidirectionalSkewHull-PDEC/ColumnCRT` 或 moving-family multiplicity 出口。全局行/列命题仍需排斥该壳层持久复现或把它吸收到 `SAE/ColumnCRT/PDEC`。

## 17. PM endpoint-release circular-aperture 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-circular-aperture-audit.md
data/prime-matrix-affine-twin-endpoint-release-circular-aperture-ledger.json
```

修正上一张线性壳层证书的口径：`[2304,3122]` 是当前周期切口下的线性 hull，不是模 `q(q-2)` 圆周上的最小弧。圆周口径应先在 `899` 周期上删除最大空弧，再取覆盖全部 formal alignment 代表的最小 circular arc。

当前证书给出：

```text
formal_alignment_row_count=12
combined_crt_modulus=899
support_width=20
linear_hull_width_from_previous_audit=819
largest_circular_open_gap_width=341
largest_gap_from_pair=19:8
largest_gap_to_pair=13:9
minimal_circular_alignment_arc=[3029,3586]
minimal_circular_alignment_arc_width=558
minimal_circular_arc_width_to_modulus_ratio=0.620689655172
optimal_shifted_support_interval=[3568,3587]
optimal_total_extension_required=539
conservative_extra_after_best_single_side_feedback=509
p_delay_open_gap_present=true
p_delay_open_gap_is_largest_gap=false
p_delay_gap_rank_by_width=3
one_sided_circular_absorption_closed_current_sweep=true
```

因此最新容量/相位矛盾点更精确：不是“圆周最小壳层近全周期”，而是“即使删去最大空弧后，最小圆弧仍宽 `558`，是 primitive support width `20` 的 `27.9` 倍”。把 support 最优平移到 `[3568,3587]` 后仍需总扩张 `539`；即使给最有利单侧 feedback horizon 信用，仍缺 `509`。

`p_delay=80` 空缝确实存在，但它只排第 `3` 大，不是最大圆周切口。上一层 `modulus_minus_hull_width=80` 的线性读数仍有结构意义，但不能再被表述为圆周最小弧的互补长度。

本步关闭当前 sweep 的单侧 circular-aperture/skew-growth 吸收解释。全局行/列命题仍未闭合；最新剩余是排斥 `CircularAperture-PDEC`，或证明持久圆弧复现进入 `ColumnCRT/PDEC`、`SAE` 或 moving-family multiplicity 出口。

## 18. PM endpoint-release anchored circular-depth 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-anchored-circular-depth-audit.md
data/prime-matrix-affine-twin-endpoint-release-anchored-circular-depth-ledger.json
```

把 circular-aperture 继续压到 actual 锚点：圆周最小弧 `[3029,3586]` 的右端点正是唯一 actual packet `19:8` 平移一周期后的代表 `3586`。因此反例链若既要保留当前 actual packet，又要用同一支撑吸收全部 formal pair，就不能只支付交支撑的左扩 `539`；generator phase 与 shifted-fill phase 两个左端点都必须到达圆弧起点。

当前读数为：

```text
actual_anchor_pair=19:8
actual_anchor_is_circular_arc_end=true
support_width=20
required_common_left_depth_to_cover_arc=557
current_generator_left_depth=18
current_fill_left_depth=28
generator_left_increment_required=539
fill_left_increment_required=529
anchored_endpoint_release_total_required=1068
one_sided_circular_support_extension=539
hidden_second_endpoint_release=529
endpoint_release_to_support_width_ratio=53.4
q_from_generator_depth_formula=1109
q_from_fill_depth_formula=560
q_candidate_gap=549
same_orientation_common_q_absent=true
same_orientation_anchored_depth_absorption_closed_current_sweep=true
```

这把上一层单侧 circular aperture 缺口进一步变成双端点释放缺口：真实链当前 generator 左深度为 `18`、fill 左深度为 `28`，而锚定圆弧要求共同左深度 `557`；总释放 `1068` 是支撑宽度 `20` 的 `53.4` 倍。同向 AffineTwin moving key 也无法吸收该深度，因为 lower-side 深度公式给出 `q=2D-5=1109` 与 `q=D+3=560`，不可能是同一个奇素数 key。

本步关闭当前 sweep 的 same-orientation anchored circular-depth absorption。全局行/列命题仍未闭合；最新剩余是排斥 `AnchoredCircularDepth-PDEC`，或证明持久 actual-anchored 圆弧复现进入 `ColumnCRT/PDEC`、`SAE`、方向改变 key 或 moving-family multiplicity 出口。

## 19. PM endpoint-release anchored parity no-go 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-anchored-parity-nogo-audit.md
data/prime-matrix-affine-twin-endpoint-release-anchored-parity-nogo-ledger.json
```

把 anchored circular-depth 的同向 moving-key 失败从数值不等式提升为方程/奇偶 no-go。若 lower-side 的同向 AffineTwin key 要用同一共同深度 `D` 同时解释 generator 与 fill 两端，则必须满足：

```text
generator left depth D = (q+5)/2  =>  q_g=2D-5
fill left depth D = q-3           =>  q_f=D+3
```

同一个 `q` 要求 `2D-5=D+3`，唯一解为 `D=8,q=11`。当前 actual-anchored 圆弧强制：

```text
actual_anchor_pair=19:8
required_common_left_depth=557
required_depth_parity=odd
q_from_generator_depth_formula=1109
q_from_fill_depth_formula=560
q_from_fill_is_even=true
q_from_fill_is_prime=false
common_depth_solution=8
required_depth_gap_from_common_solution=549
anchored_parity_nogo_closed_current_sweep=true
```

因此这里的失败不是“另一个大素数可能补上”的问题：`D=557` 为奇数，fill 侧候选 `D+3=560` 是大于 `2` 的偶数，根本不能成为奇素数 AffineTwin key；同时它与唯一共同深度解 `8` 相差 `549`。

本步关闭当前 sweep 的 same-orientation anchored parity absorption。全局行/列命题仍未闭合；剩余是把这个 parity no-go 升格为全局族定理，或处理方向改变 key、`ColumnCRT/PDEC`、`SAE`、moving-family multiplicity 出口。

## 20. PM endpoint-release cut-anchor sweep 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-cut-anchor-sweep-audit.md
data/prime-matrix-affine-twin-endpoint-release-cut-anchor-sweep-ledger.json
```

把 anchored parity no-go 从单个最优圆弧扩展到全部圆周切口。对每个相邻 CRT 类之间的 cut，保留唯一 actual packet `19:8`，把它平移进 lifted arc，然后同时计算 left/right 共同深度与 generator、shifted-fill 双端点释放量。

当前读数为：

```text
cut_count=12
actual_anchor_position_histogram={'arc_end': 1, 'arc_interior': 10, 'arc_start': 1}
minimal_circular_arc_matches_previous_audit=true
min_arc_cut=19:8->13:9
min_arc_width=558
min_total_endpoint_release_required=1068
min_release_to_support_width_ratio=53.4
max_total_endpoint_release_required=1737
left_common_depth_solution=8
right_common_depth_solution=1
min_positive_left_depth=58
min_left_gap_from_common_depth_solution=50
min_positive_right_depth=342
min_right_gap_from_common_depth_solution=341
all_endpoint_releases_exceed_support_width=true
all_actual_retained_cuts_same_orientation_closed=true
cut_anchor_sweep_closed_current_sweep=true
```

因此换切口不能释放当前矛盾：最优 cut 是之前的 `[3029,3586]` 圆弧，actual 位于右端并落入 left `D=557` 的 parity no-go；另一个 endpoint cut 让 actual 位于左端，但要求 right `D=841`，被 above-side `D=1` fixed-fill 条件排斥。其余十个 interior cut 更强，因为 actual 在圆弧内部，必须同时支付左右两侧端点释放；所有同向 moving-key 公式均无共同解。

本步关闭当前 sweep 的 actual-retained same-orientation cut-anchor absorption。全局行/列命题仍未闭合；剩余是把 `CutAnchorSweepGlobalFamilyNoGo` 升格为全局族定理，或处理方向改变 key、`ColumnCRT/PDEC`、`SAE`、moving-family multiplicity 出口。

## 21. PM endpoint-release cut-anchor ColumnCRT compression 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-cut-anchor-columncrt-compression-audit.md
data/prime-matrix-affine-twin-endpoint-release-cut-anchor-columncrt-compression-ledger.json
```

继续下钻 cut-anchor sweep 的容量出口：圆周 cut 是分析切口，不是新的 actual residue 自由度。若保留同一个 actual packet，全部 cut 都压回同一个 `P mod q(q-2)` 的 ColumnCRT 原子。

当前读数为：

```text
cut_count=12
combined_crt_modulus=899
actual_anchor_pair=19:8
actual_representatives_used_by_cuts=[2687, 3586]
actual_crt_residue=889
unique_actual_crt_residue_count=1
cut_to_actual_residue_compression_factor=12.0
fixed_actual_columncrt_mass=1/899
naive_cut_counting_mass=12/899
mass_saved_by_cut_compression=11/899
same_orientation_cut_anchor_closed_current_sweep=true
fixed_q_fixed_residue_columncrt_registered=true
moving_family_candidate_q_values=[31, 43, 103]
cut_anchor_columncrt_compression_closed_current_sweep=true
```

因此，换 cut 不能把容量从一个固定相位原子放大成十二个原子。所有 cut 中 actual representative 只是在 `2687` 与 `3586=2687+899` 两个 lift 之间切换，同余类始终是 `889 mod 899`。同向 cut-anchor 已关闭后，固定 `q=31` 固定残基的方向改变逃逸只能作为 `CutAnchorColumnCRT-PDEC` 输入对象登记；若 `q` 或残基移动，则回到既有 AffineTwin moving-family SAE/ColumnCRT 账本。

本步关闭当前 sweep 中“切口多重性作为容量来源”的解释。全局行/列命题仍未闭合；剩余是排斥 `CutAnchorColumnCRT-PDEC`、方向改变 key、或 closing moving-family multiplicity。

## 22. PM endpoint-release actual-anchor replacement 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-actual-anchor-replacement-audit.md
data/prime-matrix-affine-twin-endpoint-release-actual-anchor-replacement-ledger.json
```

继续下钻 cut-anchor ColumnCRT compression 后的逃逸：如果不保留当前 actual anchor `19:8`，则反例链必须让另一个现有 formal pair 变成 actual，或跳到未使用 target residue。两条路线都不再是自由换锚。

当前读数为：

```text
actual_crt_residue=889
support_width=20
formal_replacement_candidate_count=11
min_formal_replacement_pair=19:12
min_formal_replacement_abs_crt_jump=58
min_formal_replacement_endpoint_release=70
min_formal_release_to_support_width_ratio=3.5
unused_target_replacement_candidate_count=9
unique_unused_target_pair_count=5
min_unused_target_pair=20:9
min_unused_target_abs_crt_jump=59
min_unused_target_new_side_residue_count=1
all_formal_replacement_jumps_exceed_support_width=true
all_formal_replacement_releases_exceed_support_width=true
all_unused_target_jumps_exceed_support_width=true
all_unused_targets_need_new_side_residue=true
actual_anchor_replacement_closed_current_sweep=true
```

因此 actual anchor 替换不能绕开容量/相位压力：现有 formal pair 替换的最窄跳跃 `58` 已超过 support width `20`，且最小双端点释放 `70` 是支撑宽度的 `3.5` 倍；未使用 target 替换的最窄跳跃 `59` 也超过支撑，并且至少新增一个侧残基。

本步关闭当前 sweep 的 actual-anchor replacement 吸收解释。全局行/列命题仍未闭合；剩余是把 replacement no-go 升格为全局族定理，或排斥 support-motion、unused-target arrival、ColumnCRT/PDEC 与 moving-family 出口。

## 23. PM endpoint-release 61/59 near-miss phase-fracture 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-near-miss-61-59-phase-fracture-audit.md
data/prime-matrix-affine-twin-endpoint-release-near-miss-61-59-phase-fracture-ledger.json
```

继续下钻 actual-anchor replacement 后的最窄近失配。最窄 formal 替换 atom 仍是 `19:12`，它给出 CRT 跳跃 `58`、共同侧深度 `58` 和端点释放 `70`；同一 atom 的 moving-key 深度公式给出候选 `q=61` 与 `q=111`。同时 unused-target 最窄路线 `19:12 -> 20:9` 的 CRT 跳跃为 `59`，最近可用 gap source 也为 `59`。表面上这形成一个 `61/59` 近邻桥。

审计读数为：

```text
support_width=20
formal_min_pair=19:12
formal_min_abs_crt_jump=58
formal_min_required_common_side_depth=58
formal_min_endpoint_release=70
moving_narrowest_candidate_q_values=[61, 111]
q61_route=PrimeButNotTwinAffine
q61_failed_invariants=['expected_p_delay_integral', 'gap_source_absent', 'q_mod4_eq3']
q111_route=CompositeQ
q111_failed_invariants=['gap_source_absent', 'q_composite']
q59_is_moving_candidate=false
gap59_source_signature=gap=59, generator=61, fill=59, sides=minus->minus, p_delay=70
unused_min_target_pair=20:9
unused_min_abs_crt_jump=59
unused_min_new_side_residue_count=1
near_miss_61_59_phase_fracture_closed_current_sweep=true
```

关键相位裂缝是：`q=61` 的同向 AffineTwin 源期望 `gap=61, generator=59, fill=61, sides=minus->plus`，且 `p_delay=(11q-21)/4` 必须为整数；但 `61≡1 mod 4`，delay 非整数，并且当前没有 gap `61` source。最近的 gap `59` source 实际为 `generator=61, fill=59, sides=minus->minus`，不是 `q=61` 的重物化源。

因此整数 `59` 的两次出现不能桥接反例链：它一边只是 `q=61` 的邻近源，另一边只是 unused-target 的新侧残基到达尺度。二者都没有给出 current primitive support 内的合法 actual anchor 替换。

本步关闭当前 sweep 中 `61/59` 近失配作为隐藏吸收通道的解释。全局行/列命题仍未闭合；剩余是把 `NearMiss6159GlobalFamilyNoGo` 升格为族定理，或继续排斥 source-rematerialization、unused-target arrival、ColumnCRT/PDEC 与 moving-family 出口。

## 24. PM endpoint-release phase-scale bridge exhaustion 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-phase-scale-bridge-exhaustion-audit.md
data/prime-matrix-affine-twin-endpoint-release-phase-scale-bridge-exhaustion-ledger.json
```

把上一节的 `61/59` 近失配扩展到所有 moving-q 候选、当前 gap source 与 unused-target CRT 跳跃。当前三组尺度为：

```text
moving_q_values=[61, 65, 96, 111, 119, 123, 154, 181, 235, 293, 297, 355, 386, 575, 699, 761, 1375, 1499, 1747]
available_gap_source_values=[31, 43, 59]
unused_target_jump_values=[59, 60, 90, 150, 281, 343, 345, 374, 375]
```

审计给出：

```text
exact_q_gap_bridge_q_values=[]
exact_q_unused_jump_bridge_q_values=[]
exact_qminus2_gap_and_unused_bridge_q_values=[61]
viable_exact_scale_bridge_q_values=[]
all_exact_or_offset_scale_bridges_fractured_current_sweep=true
```

因此更强的结论是：没有任何 moving-q 本身精确命中可用 source 或 unused jump；唯一精确 offset 桥仍是 `q=61` 的 `q-2=59`，而该桥已经被 `61/59 phase-fracture` 证明断裂。也就是说，反例链不能把 moving-key、已有 source 和 unused-target arrival 三者接成同一条 actual 相位桥。

本步关闭当前 sweep 的 exact/offset phase-scale bridge 吸收解释。全局行/列命题仍未闭合；剩余是把 `PhaseScaleBridgeGlobalNoGo` 升格为族定理，或继续处理 source-rematerialization、unused-target arrival、ColumnCRT/PDEC 与 moving-family 出口。

## 25. PM endpoint-release support-width near-scale fracture 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-support-width-nearscale-fracture-audit.md
data/prime-matrix-affine-twin-endpoint-release-support-width-nearscale-fracture-ledger.json
```

继续检查 exact/offset 桥关闭后，是否还能利用 support width `20` 的邻域容忍度形成近似相位桥。审计把每个 moving-q 的 `q` 和 `q-2` 同时与 gap source、unused-target jump 做 `<=20` 的近邻枚举。

当前读数为：

```text
support_width=20
support_width_near_source_q_values=[61, 65]
support_width_near_unused_jump_q_values=[61, 65, 96, 111, 154, 293, 297, 355, 386]
support_width_near_source_and_jump_q_values=[61, 65]
viable_support_width_nearscale_bridge_q_values=[]
near_source_and_jump_moving_route_histogram={'CompositeQ': 1, 'PrimeButNotTwinAffine': 1}
all_support_width_nearscale_bridges_fractured_current_sweep=true
```

因此即使把 exact equality 放宽到支撑宽度邻域，同时靠近 source 与 unused jump 的也只有两个 q：`61` 和 `65`。`61` 仍失败于 AffineTwin 同向 prime/source gate；`65` 是合数。其余近 unused jump 的 q 没有近 source，不能组成 actual 相位桥。

本步关闭当前 sweep 的 support-width near-scale 偷渡解释。全局仍需把 `SupportWidthNearScaleGlobalNoGo` 升格为族定理，或继续处理 source-rematerialization、unused-target arrival、ColumnCRT/PDEC 与 moving-family 出口。

## 26. PM endpoint-release orphan near-jump source-deficit 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-orphan-nearjump-source-deficit-audit.md
data/prime-matrix-affine-twin-endpoint-release-orphan-nearjump-source-deficit-ledger.json
```

继续处理 support-width near-scale 中只靠近 unused-target jump、但不靠近 source 的 orphan 候选。它们是：

```text
orphan_nearjump_q_values=[96, 111, 154, 293, 297, 355, 386]
orphan_nearjump_moving_route_histogram={'CompositeQ': 6, 'PrimeButNotTwinAffine': 1}
min_source_gap_abs_delta=35
min_source_gap_abs_delta_minus_support_width=15
min_source_gap_deficit_q=96
all_orphan_nearjump_source_gaps_exceed_support_width=true
all_orphan_nearjump_events_need_new_side_residue=true
orphan_nearjump_source_deficit_closed_current_sweep=true
```

因此这些 orphan 候选虽然靠近 unused-target jump，但最近 source scale 也至少距离 `35`，已经超过 support width `20`。同时所有 unused-target 事件都需要新增侧残基，moving source 均未物化，候选本身也全部失败于合数或 AffineTwin prime/source gate。

本步给出的显式矛盾点是：近 target 不等于近 source；反例链若想把 orphan near-jump 变成真实链桥，必须额外移动 source 超过支撑宽度，并且还要支付新侧残基 arrival。当前 sweep 中这条吸收解释关闭；全局仍需证明 `OrphanNearJumpSourceDeficitGlobalNoGo` 或转入命名 PDEC/SAE 出口。

## 27. PM endpoint-release near-jump carrier exhaustion 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-nearjump-carrier-exhaustion-audit.md
data/prime-matrix-affine-twin-endpoint-release-nearjump-carrier-exhaustion-ledger.json
```

把 support-width 内所有 near-jump 候选统一分解，检查 target 侧近邻是否还有匿名承载通道。当前读数为：

```text
nearjump_carrier_q_values=[61, 65, 96, 111, 154, 293, 297, 355, 386]
near_source_gate_fractured_q_values=[61, 65]
orphan_source_deficit_q_values=[96, 111, 154, 293, 297, 355, 386]
source_status_histogram={'near_source_gate_fractured': 2, 'orphan_source_deficit': 7}
moving_route_histogram={'CompositeQ': 7, 'PrimeButNotTwinAffine': 2}
min_orphan_source_gap_abs_delta=35
min_orphan_source_gap_abs_delta_minus_support_width=15
all_carrier_jump_events_need_new_side_residue=true
nearjump_carrier_exhausted_current_sweep=true
```

因此 near-jump carrier 全部耗尽：`61,65` 近 source 但 source gate 断裂；其余七个 q 缺 source，最近 source 也超出 support width。并且所有 target 侧 near-jump 都需要新增侧残基。

本步把当前 sweep 的 target-side near-jump 分支整体关闭。全局仍需证明 `NearJumpCarrierGlobalNoGo`，或将失败路由到 source-rematerialization、unused-target arrival、ColumnCRT/PDEC 或 moving-family 出口。

## 28. PM endpoint-release carrier-arrival routing 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-carrier-arrival-routing-audit.md
data/prime-matrix-affine-twin-endpoint-release-carrier-arrival-routing-ledger.json
```

继续检查 near-jump carrier target 侧是否还有未登记的匿名承载通道。审计把 9 个 carrier 产生的 27 个 target 近邻事件逐个匹配到 unused-target arrival 账本。

当前读数为：

```text
carrier_event_count=27
unique_arrival_atom_count_used_by_carriers=9
missing_unused_target_arrival_match_count=0
carrier_event_new_side_residue_requirement_total=50
required_new_generator_residues=[10, 16, 17, 18, 20]
required_new_fill_residues=[5, 6, 7, 30]
exact_zero_phase_event_count=1
all_carrier_events_match_closed_unused_target_arrival=true
carrier_arrival_routed_current_sweep=true
```

因此 target 侧近邻没有匿名吸收：所有 carrier 事件都已经落到 closed unused-target arrival 原子。唯一 exact zero phase 事件 `q=61,q-2=59,jump=59` 也仍然需要新增 generator residue `20`，并且 source gate 已在 `61/59` phase-fracture 中失败。

本步把当前 sweep 的 near-jump target 侧全部回收到“新侧残基到达”账本。全局剩余进一步压成 `GlobalUnusedTargetResidueArrivalBound`，或命名 `NewGeneratorResidueArrival-PDEC/SAE`、`NewFillResidueArrival-PDEC/SAE`、`ColumnCRT/PDEC` 与 moving-family 出口。

## 29. PM endpoint-release carrier-arrival pressure-product 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-carrier-arrival-pressure-product-audit.md
data/prime-matrix-affine-twin-endpoint-release-carrier-arrival-pressure-product-ledger.json
```

继续把 carrier-arrival 从“新残基到达”推进到压力乘积门。当前 AffineTwin slot 为 `g=29,f=31`，所以平方根门为：

```text
sqrt_floor=floor(sqrt(29*31))=29
base_counts=(3,4)
base_side_product=12
```

若物化 carrier-arrival 使用的全部新残基：

```text
carrier_required_new_generator_residues=[10, 16, 17, 18, 20]
carrier_required_new_fill_residues=[5, 6, 7, 30]
full_counts_after_carrier_arrival=(8,8)
full_side_product_after_carrier_arrival=64
full_square_excess_over_modulus_product=3197
```

更窄的断点是：任意两个双侧 target atoms 已经把侧计数推到 `(5,6)`，乘积 `30`，并且

```text
30^2-29*31=1.
```

所以当前 carrier-arrival packet 若真实物化，不再是普通 arrival 义务，而是立即触发 `SuperSqrt/PressureProduct-PDEC`。若该 PDEC 被排斥，则当前 carrier-arrival packet 不能复现；若不排斥，它就是显式命名出口。

## 30. PM endpoint-release carrier-arrival projection-deficit 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-carrier-arrival-projection-deficit-audit.md
data/prime-matrix-affine-twin-endpoint-release-carrier-arrival-projection-deficit-ledger.json
```

继续检查上一步的 `SuperSqrt` crossing 是否真是 actual overload。审计把形式侧乘积投影回共同支撑窗口，得到：

```text
sqrt_floor=29
target_window_pair_count=20
minimal_crossing_formal_product_count=30
minimal_crossing_projection_hit_count=3
minimal_crossing_projection_deficit_count=27
minimal_crossing_actual_sqrt_slack=26
full_formal_product_count=64
full_projection_hit_count=6
full_projection_deficit_count=58
full_actual_sqrt_slack=23
```

因此最小 crossing 的 `30` 个形式 pair 只有 `3` 个投影为 actual hits：实际锚点 `19:8` 加两个 selected target atoms。完整 carrier packet 的 `64` 个形式 pair 也只有 `6` 个 actual hits。

本步把当前 sweep 的 `SuperSqrt` actual-overload 解释关闭：这里的超界来自形式侧笛卡尔积过粗，而非真实链 actual 负载超平方根。全局剩余转成 `ProductAccountingTightening`、`ProjectionCollision-PDEC` 或 `PrimitiveTwinSlotSupportEscape-PDEC/SAE` 的族级证明。

## 31. PM endpoint-release support-graph cap 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-support-graph-cap-audit.md
data/prime-matrix-affine-twin-endpoint-release-support-graph-cap-ledger.json
```

继续把 actual projection 的计数原则内化。当前共同支撑窗口不是二维区域，而是 20 个 target pairs 的函数图像：

```text
q=31
support_width=20
sqrt_floor=29
generator_functional_graph=true
fill_functional_graph=true
affine_offsets_mod_fill=[20]
support_graph_cap=20
support_graph_cap_slack_to_sqrt_floor=9
```

因此任意侧残基集合的 actual projection hits 都由图像容量 `20` 控制，而不是由侧残基笛卡尔积控制。当前最小 crossing hits 为 `3`，完整 packet hits 为 `6`，均低于 `20<=29`。

固定 AffineTwin 槽的一般公式也在本步登记：`W=(q+9)/2`，对 `q>=13` 有 `W^2<=q(q-2)`，等价于 `3q^2-26q-81>=0`。所以在不移动槽的前提下，ProductAccounting 已收紧到 actual graph projection；全局剩余只剩 moving-slot support escape 或 projection-collision 的命名出口。

## 32. PM endpoint-release moving-slot graph-cap route 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-moving-slot-graph-cap-route-audit.md
data/prime-matrix-affine-twin-endpoint-release-moving-slot-graph-cap-route-ledger.json
```

本节把上一节留下的 moving-slot support escape 拆成分层路由。当前证书给出：

```text
current_q=31
current_support_graph_cap=20
current_sqrt_floor=29
fixed_candidate_q_values=[31,43,103]
all_fixed_candidate_graph_caps_passed=true
support_motion_candidate_count=11
all_support_motion_requires_both_endpoint_release=true
exact_rematerialized_q_values=[]
anonymous_moving_slot_actual_overload_closed_current_sweep=true
```

因此，若槽只是换到同向 AffineTwin 固定候选族，图容量门仍成立；候选 `q=31,43,103` 的支撑宽度都满足 `W^2<=q(q-2)`。若真正移动当前 `q=31` 支撑，11 个 support-motion 候选全部需要双端点释放；最窄 atom `19:12` 也要释放 `70`，是支撑宽度 `20` 的 `3.5` 倍。

进一步，保持固定 primitive key 会同时打破 generator/fill 两侧深度恒等式；允许同向 moving key 时，最窄 atom `19:12` 给出 `q_g=111` 与 `q_f=61`，差 `50`，不能形成同一 key。深度公式吐出的 19 个候选 `q` 没有任何精确 source 重物化，直方图为 `CompositeQ:13, PrimeButNotTwinAffine:6`。

所以当前 sweep 内没有匿名 moving-slot actual overload。剩余被压成明确命名出口：`MovingSlotFamilyPersistenceNoGo`、方向改变 primitive key、`SourceRematerialization-PDEC/SAE`、`ColumnCRT/PDEC` 或 unused-target arrival 的族级控制；行/列命题仍未无条件闭合。

## 33. PM endpoint-release moving-family persistence pressure 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-moving-family-persistence-pressure-audit.md
data/prime-matrix-affine-twin-endpoint-release-moving-family-persistence-pressure-ledger.json
```

继续攻击上一节剩下的 moving family 持久复现口。当前候选族为 `q=[31,43,103]`，联合 source gate、epoch 稀疏、paired pressure、threshold route 与 fill catchup 后得到：

```text
source_gate_pass_q_values=[31]
source_gate_fail_q_values=[43,103]
source_gate_blocked_formal_pairs=28
candidate_product_mass_upper_sum=0.023577117628562343
one_sided_pressure_q_values=[43,103]
all_minimal_routes_require_fill_increment=true
total_min_extra_fill_required_if_all_candidates_cross=11
anonymous_moving_family_persistence_closed_current_sweep=true
```

`q=31` 是唯一 exact source materialized 候选，但它已被 fixed graph cap 管住；若要越过当前安全阈值，仍需新增 fill residue 或触发 reset/ColumnCRT。`q=43` 有同 gap source，但实际签名为 `plus->minus, p_delay=74`，而 AffineTwin 期望 `minus->plus, p_delay=113`，相位差 `-39`，阻断 16 个 formal pairs。`q=103` 没有 gap source，阻断 12 个 formal pairs。

`q=43,103` 虽有 generator 单侧压力，但 paired pressure product 仍低于 1，瓶颈在 fill 侧。若三个候选都尝试阈值穿越，至少要新增 11 个 fill residue，对应 Rankin 质量 `23339/137299≈0.169986671425`；若不是新 residue，则直接进入 reset/ColumnCRT-PDEC。

所以当前 sweep 的 moving family 持久复现不能作为匿名容量来源。全局剩余进一步压成 `FillResidueArrivalBound`、`HighDensityEpochPair-PDEC/ColumnCRT`、`PressureProduct-PDEC` 或 `SourceRematerialization-PDEC/SAE`。

## 34. PM endpoint-release fill-arrival projection gate 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-fill-arrival-projection-gate-audit.md
data/prime-matrix-affine-twin-endpoint-release-fill-arrival-projection-gate-ledger.json
```

继续压缩 `FillResidueArrivalBound`。fill 到达若要变成 actual overload，必须先通过两个门：已物化 source 和 actual projection。当前证书给出：

```text
candidate_q_values=[31,43,103]
realized_q_values=[31]
source_blocked_q_values=[43,103]
source_blocked_formal_pairs=28
all_realized_fill_arrivals_require_generator_coarrival=true
minimal_crossing_formal_product_count=30
minimal_crossing_projection_hit_count=3
minimal_crossing_actual_sqrt_slack=26
anonymous_fill_arrival_actual_overload_closed_current_sweep=true
```

`q=31` 是唯一已物化候选，但不能走 fill-only 路线：`minimal_route_can_be_fill_only=false`，任何阈值穿越至少还要新增 2 个 generator residue。unused-target 账本给出的新 fill residues 为 `[5,6,7,30]`，但所有 target 都同时需要新 generator residue，且 CRT jump 都超过 support width。

若把这种 generator/fill 共到达按形式乘积计到最小 crossing `30`，actual projection 也只有 `3` 个 hits，仍有 `26` 个平方根余量。另一方面，`q=43,103` 的 fill-only 形式路线先被 source gate 阻断，不能进入真实链。

所以当前 sweep 内没有匿名 fill-arrival actual overload。最新剩余进一步压成 `GeneratorCoarrivalBound`、`ProductAccountingTighteningGlobal`、`SourceRematerialization-PDEC/SAE` 与 `ColumnCRT/PDEC`。

## 35. PM endpoint-release generator-coarrival projection accounting 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-generator-coarrival-projection-accounting-audit.md
data/prime-matrix-affine-twin-endpoint-release-generator-coarrival-projection-accounting-ledger.json
```

继续下钻上一节留下的 `GeneratorCoarrivalBound`。当 realized `q=31` 的 fill 到达被迫携带 generator 共到达时，必须区分形式侧乘积和 actual 支撑投影。当前全枚举 5 个 unused-target 原子的所有非空子集得到：

```text
subset_count=31
fill_arrival_subset_count=30
fill_only_subset_count=0
formal_super_sqrt_subset_count=22
actual_overload_subset_count=0
minimal_coarrival_formal_product_count=30
minimal_coarrival_projection_hit_count=3
minimal_coarrival_actual_sqrt_slack=26
full_formal_product_count=64
full_projection_hit_count=6
full_actual_sqrt_slack=23
generator_coarrival_projection_accounting_closed_current_sweep=true
```

因此，本轮最窄显式矛盾点已经从“fill 侧追赶”压到“generator/fill 共到达后的投影账本”：反例链可把侧残基笛卡尔积推过平方根门，但真实链只把共同支撑图像上的点计入 actual load。所有 22 个形式超界子集投影后仍低于平方根门，且投影 hits 精确等于 actual anchor `19:8` 加所选 target atoms。

本步关闭当前 sweep 中 generator coarrival 作为匿名 actual overload 的解释。全局行/列命题仍未闭合；最新剩余是把该投影账本升格为族级 `GeneratorCoarrivalFamilyBound`，或把失败形态登记为 `ProductAccountingTighteningGlobal`、`SourceRematerialization-PDEC/SAE`、`ColumnCRT/PDEC` 与 moving-family persistence 出口。

## 36. PM endpoint-release generator-coarrival family schema 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-generator-coarrival-family-schema-audit.md
data/prime-matrix-affine-twin-endpoint-release-generator-coarrival-family-schema-ledger.json
```

本节把上一轮 `q=31` 的 coarrival 子集枚举提升成族级门控格式。固定 AffineTwin 槽的 actual load 由共同支撑函数图像控制，而不是由 generator/fill 侧残基笛卡尔积控制。图像宽度为

```text
W=(q+9)/2.
```

对所有 `q>=13`，

```text
W^2<=q(q-2)  <=>  3q^2-26q-81>=0.
```

由于 `q=13` 时右端为 `88>0`，且导数 `6q-26` 在 `q>=13` 为正，固定图像族级不等式闭合。当前候选 `q=[31,43,103]` 的读数为：

```text
q=31: W=20, sqrt_floor=29, q(q-2)-W^2=499
q=43: W=26, sqrt_floor=41, q(q-2)-W^2=1087
q=103: W=56, sqrt_floor=101, q(q-2)-W^2=7267
```

因此当前最窄矛盾进一步写成：

```text
反例链需要 coarrival 后的形式笛卡尔积作为容量；
真实链固定支撑图像只允许 W 个 actual hits；
W 始终低于 sqrt(q(q-2))；
所以 actual overload 必须破坏固定图像假设。
```

当前 sweep 中，破坏固定图像的出口也都被路由：support motion 最窄释放 `70>20`，source gate 阻断 `28` 个 formal pairs，固定 actual anchor 压成 `P≡889 mod 899` 的单个 ColumnCRT 原子，moving-family persistence 仍只剩命名出口。

本步关闭当前 sweep 的匿名 generator-coarrival family schema。全局仍需把该 schema 推广到所有持久 AffineTwin family，并排斥 `MovingSlotFamilyPersistenceNoGo`、`SourceRematerialization-PDEC/SAE`、`ColumnCRT/PDEC` 与 `ProductAccountingTighteningGlobal`。

## 37. PM endpoint-release persistent-family promotion 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-persistent-family-promotion-audit.md
data/prime-matrix-affine-twin-endpoint-release-persistent-family-promotion-ledger.json
```

本节继续把“推广到所有持久 AffineTwin family”的义务拆成独立账本。当前 promotion 路由给出：

```text
candidate_q_values=[31,43,103]
realized_q_values=[31]
candidate_product_mass_upper_sum=0.023577117628562343
eta=0.025
candidate_total_eta_slack=0.0014228823714376587
high_density_epoch_pair_count=0
fixed_slot_recurrence_count=0
fixed_residue_slot_drift_pair_count=12
source_gate_blocked_formal_pairs=28
persistent_family_promotion_closed_current_sweep=true
```

其结构含义是：

```text
固定图像: 由 W<=sqrt(q(q-2)) 阻断 actual overload；
固定 q/残基复现: 进入固定模 ColumnCRT/PDEC，当前 fixed-slot 复现为 0；
moving q/残基: 进入 epoch-pair SAE，当前 occupancy 上界低于 eta；
source/pressure/fill: 当前 source 阻断 28 个 formal pairs，paired pressure 未超界，fill 到达进入 new-fill/reset 二分。
```

因此当前 sweep 中，persistent family 不能作为匿名容量来源。全局最窄剩余进一步压成 `GlobalEpochPairMultiplicityBound` 与 `FixedResidueSlotDriftColumnCRT`，并保留 `MovingResidueShapeSAE/Rankin`、`HighDensityEpochPair-PDEC/ColumnCRT` 与 source-rematerialization 出口。

## 38. PM endpoint-release transport-frontier integration 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-transport-frontier-integration-audit.md
data/prime-matrix-affine-twin-endpoint-release-transport-frontier-integration-ledger.json
```

本节把上一节留下的 `FixedResidueSlotDriftColumnCRT` 接入既有 transport-cell 深层账本。当前集成审计给出：

```text
fixed_residue_slot_drift_pair_count=12
transport_cell_count=12
unique_transport_cell_count=12
transport_cell_recurrence_count=0
exact_phase_translate_count=0
max_forward_transition_count=8
reset_pdec_atom_count=0
physical_record_count=324
transport_cell_physical_record_count=24
singleton_residue_physical_record_count=300
unclassified_physical_record_count=0
transport_frontier_integration_closed_current_sweep=true
```

新的显式冲突读数是：

```text
反例链若把固定残基槽漂移当作持续容量来源；
真实链要求这些漂移成为可复现的 transport cell；
但当前 12 个 transport cell 全部互异且无 exact phase translate；
链式复现会有限步终止，非连续复现又必须重复完整 reset key；
当前 reset-PDEC atom 数为 0。
```

因此 `FixedResidueSlotDriftColumnCRT` 在当前 sweep 内不再是匿名容量出口，而被压成 `TransportResetPDECExclusion` 与 `SingletonResidueSAE/Rankin` 两个更底层义务。全局最窄剩余现在是 `TransportResetPDECExclusion`、`SingletonResidueSAE/Rankin` 与 `GlobalEpochPairMultiplicityBound`，并保留 `MovingResidueShapeSAE/Rankin` 作为移动残基形状出口；行/列命题仍未无条件闭合。

## 39. PM endpoint-release remaining-frontier bridge 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-remaining-frontier-bridge-audit.md
data/prime-matrix-affine-twin-endpoint-release-remaining-frontier-bridge-ledger.json
```

本节把 transport-frontier 集成后的三条剩余接入既有 singleton/active-ell/epoch-pair 账本，形成当前最新前沿读数：

```text
transport_reset_pdec_atom_count=0
singleton_residue_packet_count=300
one_slot_mass=4.291749690880195
two_slot_mass_share=0.008484456873983595
active_band=23..109
minus_only_ell_values=[23,109]
candidate_product_mass_upper_sum=0.023577117628562343
eta=0.025
high_density_epoch_pair_count=0
remaining_frontier_bridge_closed_current_sweep=true
```

桥接后的精确主攻面是：

```text
transport reset: 当前 atom 为 0，但全局 reset-PDEC 仍未排斥；
singleton SAE: 300 个 singleton packet 已定位到 one-slot/active-ell 带端点增长；
epoch-pair: 当前候选 q=[31,43,103] 低于 eta 门，但 global multiplicity 仍未证明；
moving residue shape: 仍保留 SAE/Rankin 出口。
```

因此最新可攻接口不再是泛化的 `SingletonResidueSAE/Rankin`，而是更窄的 `ActiveEllBandEndpointGrowthBoundOrEndpointResetPDEC`，并与 `TransportResetPDECExclusion`、`GlobalEpochPairMultiplicityBound`、`MovingResidueShapeSAE/Rankin` 并列为全局剩余。当前 bridge 只关闭 current sweep 的路由连接，不关闭行/列命题。

## 40. H-lower endpoint-motion stencil 更新

后续文件

```text
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-stencil-audit.md
data/square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-stencil-ledger.json
```

本节继续下钻 `ActiveEllBandEndpointGrowthBoundOrEndpointResetPDEC`。端点运动被拆成外向邻素数、端点自身、内向核心边缘三类模板：

```text
outward_neighbor_primes=[19,113]
active_band_endpoints=[23,109]
inward_core_edge_primes=[29,107]
outward_neighbors_empty_current_sweep=true
endpoints_are_minus_singletons_current_sweep=true
inward_edges_are_core_absorption_current_sweep=true
endpoint_motion_stencil_closed_current_sweep=true
```

具体形态为：

```text
ell=19: empty
ell=23: minus-only singleton
ell=29: both-side core, 4 records
ell=107: both-side core, 6 records
ell=109: minus-only singleton
ell=113: empty
```

所以当前 sweep 中端点运动不能再作为未分类容量来源：外向一步没有物化，端点自身只有两个 minus-only 单原子，内向一步已经进入核心吸收带。最新全局硬点压成 `EndpointOutwardArrivalBoundOrEndpointAtomPDECExclusion`，并保留 `CoreEdgeAbsorptionMultiplicityBound` 作为内侧核心吸收的 multiplicity 义务。

## 41. H-lower endpoint-motion gap 更新

后续文件

```text
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-gap-router.md
data/square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-gap-ledger.json
```

本节把端点运动从相邻模板继续压成“内部缺口填充”义务。按一槽 `ell` 的首次激活顺序，当前证书给出：

```text
activation_count=21
gap_snapshot_count=3
gap_ells=[31,43,59]
max_known_gap_fill_delay=80
all_activation_gaps_filled_in_current_sweep=true
all_1000_prefix_snapshots_exact_intervals=true
final_active_band=[23,109]
```

三次缺口具体为：

```text
p=2063 activates ell=47, missing [43], filled after 74
p=2687 activates ell=29, missing [31], filled after 80
p=3187 activates ell=61, missing [59], filled after 70
```

因此当前 sweep 中，端点扩张只产生短暂内部素数缺口，且所有千级 `P` 前缀快照已经恢复为连续素数带。最新全局硬点为 `EndpointMotionGapFillBoundOrGapPDECExclusion`：要么证明端点扩张造成的缺口有统一填充界，要么把持久缺口登记并排斥为 Gap-PDEC/SAE。

## 42. H-lower gap-fill pair / repair corridor 更新

后续文件

```text
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-router.md
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-repair-corridor-router.md
data/square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json
data/square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-repair-corridor-ledger.json
```

本节把三次内部缺口继续压成生成-填充二元组和短 `P` 走廊：

```text
gap_pair_count=3
unique_gap_fill_pair_key_count=3
repeated_gap_fill_pair_key_count=0
all_gaps_are_next_activation_repairs=true
all_repairs_restore_exact_interval=true
max_activation_rank_delay=1
max_p_delay=80
all_repairs_within_3_gap_ell_current_sweep=true
all_repairs_within_2_gap_ell_current_sweep=false
max_p_delay_over_gap_ell=2.580645161290
min_corridor_defect_against_3_gap_ell=13
```

三条二元组为：

```text
gap=43: 47 -> 43, dp=74, key sides=plus->minus
gap=31: 29 -> 31, dp=80, key sides=minus->plus
gap=59: 61 -> 59, dp=70, key sides=minus->minus
```

因此当前缺口填充不是任意等待，而是 rank-delay `1` 的 immediate repair，并且全部处在 `3*gap_ell` 短走廊内。最新全局硬点进一步压成 `ShortGapRepairCorridorBoundOrCorridorPDECExclusion`：要么证明端点缺口修复始终有短走廊包络，要么把走廊失效登记并排斥为 Corridor-PDEC/SAE。

## 43. H-lower corridor phase budget 更新

后续文件

```text
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-corridor-phase-budget-router.md
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-corridor-phase-budget-router.json
data/square-phase-offband-prefix-gap-shadow-selector-h-lower-corridor-phase-budget-ledger.json
```

本节把短走廊延迟进一步分解为精确三分量预算身份：

```text
p_delay = generator_right_depth + phase_bridge_gap + fill_left_depth
phase_budget_row_count=3
all_phase_budget_identities_closed=true
all_corridor_3gap_slack_positive=true
min_corridor_3gap_slack=13
max_phase_bridge_gap_over_gap=1.483870967742
all_phase_bridges_within_2gap=true
component_excess_row_count=1
min_other_component_spare_after_excess=13
```

三条预算行为：

```text
gap=43: gen_right=12, bridge=40, fill_left=22, total=74, 3gap slack=55
gap=31: gen_right=6, bridge=46, fill_left=28, total=80, 3gap slack=13, excess=15
gap=59: gen_right=31, bridge=31, fill_left=8, total=70, 3gap slack=107
```

因此当前短走廊最紧张处不是总预算失效，而是 `gap_ell=31` 的单分量 phase bridge 超过一个 `gap_ell`；该超标量 `15` 被左右深度余量吸收后仍保留 `13` 的总余量。最新全局硬点压成 `CorridorPhaseBudgetBoundOrPhaseBridgePDECExclusion`：要么证明相位桥三分量预算在全局持久成立，要么把不可吸收的 phase-bridge 超标登记并排斥为 PhaseBridge-PDEC/SAE。

## 44. H-lower phase-bridge excess 回流到 AffineTwin/ColumnCRT 主线

后续文件

```text
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-atom-router.md
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-source-router.md
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-absorption-normal-form-router.md
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-primitive-identity-router.md
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-primitive-affine-collapse-router.md
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-prime-gate-router.md
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-router.md
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-moving-family-sae-columncrt-router.md
```

这一串账本说明上一节唯一 phase-bridge 超标并不是新型匿名容量，而是回流到既有 AffineTwin/ColumnCRT 主线：

```text
phase_bridge_excess_atom_count=1
excess=15
absorbing_spare=28
spare_after_excess=13
excess = generator_margin = 3*rho_jump
slack_after_absorption = |delta_b| = 13
absorbing_depth_spare = generator_margin + |delta_b|
phase_bridge_gap = gap_ell + generator_margin
```

primitive 身份组进一步塌缩为单个仿射整数型：

```text
fill_ell=gap_ell=31
generator_ell=gap_ell-2=29
generator_margin=(gap_ell-1)/2=15
|delta_b|=(gap_ell-5)/2=13
|delta_u|=(gap_ell-3)/4=7
rho_jump=2*(fill_ell-generator_ell)+1=5
```

因此当前唯一原子满足 AffineTwin 必要门：`q=31`、`q-2=29` 同为素数，且 `q≡3 mod 4`。双槽相位锁给出：

```text
P≡19 mod 29
P≡21 mod 31
combined_modulus=29*31=899
pair_support_width=20
unique_representative=P=2687
```

这把 corridor phase budget 线接回既有主线：固定 `q=31` 双槽原子被 `899>20` 的 CRT 相位支撑差孤立；若固定 `q` 与固定残基复现，则进入固定模 ColumnCRT/PDEC；若 `q` 或残基移动，则进入 AffineTwin epoch-pair SAE/Rankin 和 moving-family 出口。当前回流桥关闭的是 current sweep 的新匿名 hardpoint，不关闭全局行/列命题；全局仍需沿已登记的 `AffineTwinEpochPairMultiplicityBoundOrColumnCRTPDECExclusion`、`ActiveEllBandEndpointGrowthBoundOrEndpointResetPDEC`、`TransportResetPDECExclusion` 与 `MovingResidueShapeSAE/Rankin` 继续排斥或吸收。

## 45. H-lower AffineTwin epoch-pair sparse SAE 更新

后续文件

```text
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-epoch-pair-multiplicity-router.md
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sparse-sae-global-envelope-router.md
data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-epoch-pair-multiplicity-ledger.json
data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sparse-sae-global-envelope-ledger.json
```

回流到 AffineTwin moving-family 后，已有账本先给出 `eta=1/40` 稀疏门：

```text
candidate_q_values=[31,43,103]
realized_q_values=[31]
candidate_product_mass_upper_sum=0.023577117629
candidate_total_eta_slack=0.001422882371
max_occupancy_upper_ratio=0.013348164627
high_density_epoch_pair_count=0
```

因此当前 sweep 没有 HighDensityEpochPair，失败若出现则已经命名为 HighDensityEpochPair-PDEC/ColumnCRT。更深一层，SparseSAE 的真正可求和部分是单固定双槽原子质量：

```text
1/(q(q-2)) = (1/2)*(1/(q-2)-1/q)
sum_{odd q>=Q} 1/(q(q-2)) <= 1/(2(Q-2))
Q=31 gives tail <= 1/58 = 0.017241379310
current_realized_sae_mass = 1/899 = 0.001112347052
```

这关闭了“单原子 SAE 尾和”这一全局恒等式，不依赖孪生素数猜想或有限扫描。但账本也给出必要诊断：`eta` 稀疏门本身不能推出全局可求和，因为每个 `q` 若允许 `O(eta*q(q-2))` 个原子，则每个 `q` 都可贡献约 `eta`，无穷求和会发散。

因此反例链与真实链的最新显式交叉点不再是单原子质量，而是每个 `q` 的 AffineTwin 原子 multiplicity：要么证明每 `q` 只有 `O(1)` 个或有额外衰减的可实现原子，要么 multiplicity 超额必须回流为 HighDensityEpochPair-PDEC/ColumnCRT。最新最窄硬点为 `AffineTwinPerQMultiplicityBoundOrHighDensityEpochPairPDECExclusion`。

## 46. H-lower AffineTwin sqrt-product / Brun 条件出口更新

后续文件

```text
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sqrt-product-brun-router.md
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sqrt-product-brun-router.json
data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sqrt-product-brun-ledger.json
```

本节把上一节的 per-`q` multiplicity 目标继续收窄。令 `M_q` 为同一 AffineTwin `q` 的候选双残基乘积上界；当前候选全部满足平方根乘积门：

```text
candidate_q_values=[31,43,103]
all_current_rows_pass_sqrt_product_gate=true
max_product_over_sqrt_capacity=0.400222407579
min_sqrt_product_gate_slack_squared=755
current_product_sae_mass_upper_sum=0.023577117629
current_sqrt_gate_envelope_sum=0.066972535473
```

平方根乘积门的含义是：

```text
M_q^2 <= q(q-2)
=> M_q/(q(q-2)) <= 1/sqrt(q(q-2)) <= 1/(q-2)
```

由于 AffineTwin `q` 满足 `q` 与 `q-2` 同为素数，若接受经典 Brun 孪生素数倒数收敛，则满足平方根门的 moving packets 进入可求和 SAE 尾和。账本明确标注：

```text
external_brun_input=ClassicalBrunTwinPrimeReciprocalConvergence
external_brun_input_accepted_in_author_side=false
internal_sqrt_product_bound_proved=false
super_sqrt_epoch_pair_pdec_excluded_globally=false
```

因此本步只关闭“外部 Brun 输入 + 全局平方根门”条件下的 SAE 出口，并证明当前有限候选没有 SuperSqrtEpochPair。作者侧自足线的最新硬点更精确地变成：证明所有持久 AffineTwin epoch-pair 满足 `M_q^2<=q(q-2)`，或把违反者登记并排斥为 `SuperSqrtEpochPair-PDEC/ColumnCRT`。最新最窄硬点为 `AffineTwinSqrtProductBoundOrSuperSqrtEpochPairPDECExclusion`。

## 47. H-lower sqrt-product 回流到 actual-packet 支撑耗尽

后续文件

```text
docs/monograph/prime-matrix-pressure-packet-carrying-ceiling-brun-selberg-router.md
docs/monograph/prime-matrix-nonpdec-sqrt-phase-support-reduction.md
```

这两份已归档文件把上一节的平方根乘积门再压低一层。关键修正是区分形式侧乘积与真实包数：

```text
M_q^form = A_g*A_f          # generator/fill 侧残基笛卡尔积上界
N_q      = |Pi_q|           # 真正通过双槽、CRT、相位支撑和非复用门的 actual packets
N_q <= M_q^form
```

非 PDEC actual packet 若都落入 primitive AffineTwin 双槽支撑，则共同相位支撑宽度为：

```text
W_q=(q+9)/2
```

并且对所有 `q>=13` 有：

```text
W_q <= sqrt(q(q-2))
<=> 3q^2-26q-81 >= 0
```

同一 primitive 投影若复现，则不再是两个自由 packets，而是 repeated-residue/reset 或 fixed projection ColumnCRT/PDEC。因此排除 PDEC/ColumnCRT 后有注入：

```text
Pi_q -> Omega_q
N_q <= |Omega_q| <= W_q <= sqrt(q(q-2))
```

于是 `SuperSqrt` 失败只剩三分：

```text
1. ProductAccountingTightening: M_q^form 超界但 N_q 未超界；
2. ProjectionCollision-PDEC/ColumnCRT: N_q 超界且仍声称在 primitive 支撑内；
3. PrimitiveTwinSlotSupportEscape-PDEC/SAE: actual packet 逃出 primitive 双槽支撑。
```

这把最新硬点从抽象 `SuperSqrtPressureProductPDECExclusion` 进一步压成 actual load 口径：证明所有未触发 PDEC/ColumnCRT 的 actual packets 都满足 primitive depth identities 并落入宽度 `(q+9)/2` 的共同相位支撑；否则把逃逸对象登记为 `PrimitiveTwinSlotSupportEscape-PDEC/SAE`。最新最窄主攻点为 `PrimitiveTwinSlotSupportExhaustion`，并行需要把现有 SAE/Rankin 账本从 `M_q^form` 口径收紧到 `N_q` 口径。

## 48. H-lower actual-packet critical-load 合同回接

后续文件

```text
docs/monograph/prime-matrix-affine-twin-actual-packet-contract.md
docs/monograph/prime-matrix-affine-twin-actual-packet-contract.json
data/prime-matrix-affine-twin-actual-packet-contract-ledger.json
```

actual-packet 合同给出当前 sweep 的精确账本口径：

```text
candidate_q_values=[31,43,103]
actual_q_values_current=[31]
total_formal_product_upper=40
total_actual_packet_count_current=1
total_formal_to_actual_gap=39
all_actual_packets_in_primitive_support_current=true
all_actual_packets_pass_sqrt_gate_current=true
projection_collision_pdec_count_current=0
```

逐 `q` 的实际负载为：

```text
q=31:  M_form=12, N_q=1, W=20, capacity=899, route=ActualPrimitiveSupportAbsorbed+ProductAccountingTightening
q=43:  M_form=16, N_q=0, W=26, capacity=1763, route=NoActualPacketCurrentSweep+ProductAccountingTightening
q=103: M_form=12, N_q=0, W=56, capacity=10403, route=NoActualPacketCurrentSweep+ProductAccountingTightening
```

因此当前反例链的形式压力并没有变成真实负载：最大形式负载比为 `0.160177975528`，最大 actual 负载比仅为 `0.001112347052`。这把 current sweep 中的 `SuperSqrt/PressureProduct` 全部转成 `ProductAccountingTightening`；全局仍需证明这个 `M_q^form -> N_q` 收紧在所有持久 AffineTwin 家族中成立，并排斥 `PrimitiveTwinSlotSupportEscape-PDEC/SAE`。

## 49. H-lower formal-pair pruning 合同回接

后续文件

```text
docs/monograph/prime-matrix-affine-twin-formal-pair-pruning-audit.md
docs/monograph/prime-matrix-affine-twin-formal-pair-pruning-audit.json
data/prime-matrix-affine-twin-formal-pair-pruning-ledger.json
```

`formal-pair-pruning` 把上一节的 `formal_to_actual_gap=39` 完全拆开：

```text
formal_pair_total=40
actual_packet_total_current=1
formal_to_actual_gap=39
crt_window_empty_pair_total_current=11
source_unmaterialized_pair_total_current=28
unresolved_formal_pair_total_current=0
product_accounting_tightening_closed_current_sweep=true
```

逐 `q` 的删除机制为：

```text
q=31:  M_form=12, actual=1, CRTWindowEmpty=11, source_unmaterialized=0
q=43:  M_form=16, actual=0, CRTWindowEmpty=0,  source_unmaterialized=16
q=103: M_form=12, actual=0, CRTWindowEmpty=0,  source_unmaterialized=12
```

其中 `q=31` 的唯一 actual packet 为 `(generator residue, fill residue)=(19,8)`，shifted fill residue 为 `21`，合成 CRT residue 为 `889 mod 899`，在 pair support `[2669,2688]` 中的代表为 `2687`；其余 11 个形式配对都没有短窗代表。`q=43` 有同 gap 但错源：期望 `generator=41, fill=43, sides=minus->plus, p_delay=113`，实际源为 `generator=47, fill=43, sides=plus->minus, p_delay=74`。`q=103` 当前无 gap-fill source。

因此当前 sweep 的容量/相位矛盾已经不是“40 个形式 packet 与平方根门冲突”，而是“39 个形式 packet 无法物化”：11 个被 CRT 短窗排空，28 个被 source materialization gate 删除。最新剩余接口随之收窄为 `GlobalProductAccountingTightening` 的统一化证明：任意持久 AffineTwin 形式配对若不能成为 actual packet，必须进入 `CRTWindowEmptyGlobalSupportBound` 或 `SourceMaterializationFailure-PDEC/SAE`；若它能绕过二者，则只能作为 `PrimitiveTwinSlotSupportEscape-PDEC/SAE` 登记。

## 50. PM formal-to-actual global cutset 回接

后续文件

```text
experiments/prime_matrix_formal_to_actual_global_cutset_router.py
docs/monograph/prime-matrix-formal-to-actual-global-cutset-router.md
docs/monograph/prime-matrix-formal-to-actual-global-cutset-router.json
data/prime-matrix-formal-to-actual-global-cutset-ledger.json
```

本证书把 actual-packet、formal pruning、source gate、CRT window、moving-slot graph cap、remaining-frontier bridge 与 endpoint atom 账本合成同一个 cutset。当前读数为：

```text
formal_pair_total=40
actual_packet_total_current=1
formal_to_actual_gap=39
crt_window_empty_pair_total_current=11
source_unmaterialized_pair_total_current=28
unresolved_formal_pair_total_current=0
combined_modulus_current=899
support_width_current=20
min_empty_window_distance=40
endpoint_atom_count=2
current_sweep_cutset_closed=true
row_column_unconditional_closed=false
```

这给出当前反例链/真实链的显式冲突切面：

```text
ProductAccounting: 40 个形式配对只有 1 个 actual packet；
SourceGate: q=43 的 16 个配对错源，q=103 的 12 个配对无源；
CRTWindow: 899 模数远大于 20 窗宽，空窗最小距离为 40；
PrimitiveSupport: 固定支撑宽度 20 低于 sqrt floor 29，支撑逃逸已回流到 moving-slot/source/ColumnCRT 出口；
RemainingBridge: transport reset atom=0，singleton packets=300，epoch-pair mass=0.023577117628562343<eta=0.025；
EndpointAtom: 活跃带端点 [23,109] 只有 2 个 minus-only 单原子。
```

因此 current sweep 已无匿名 actual-load 缺口。全局主攻点被压成 `GlobalFormalToActualCutsetPromotionOrNamedExitExclusion`：把上述 cutset 推广到所有持久反例族，并逐一排斥或求和吸收 `GlobalProductAccountingTightening`、`SourceMaterializationFailure-PDEC/SAE`、`CRTWindowEmptyGlobalSupportBound`、`PrimitiveTwinSlotSupportEscape-PDEC/SAE`、端点增长/reset、transport reset、epoch-pair multiplicity 与 moving-residue SAE/Rankin。

## 51. formal-to-actual cutset completeness lemma

后续文件

```text
docs/monograph/prime-matrix-formal-to-actual-cutset-completeness-lemma.md
```

本引理把上一节 `GlobalFormalToActualCutsetPromotion` 中的确定性部分从有限扫描中剥离出来。固定 `q>=13`，令 `F_q=G_q x H_q` 为形式 residue product。对任意 `a in F_q` 按三道门检查：

```text
Source_q(a): matching gap-fill source 是否物化；
CRT_q(a): 合成 CRT class 是否命中 primitive pair support；
Primitive_q(a): 是否保持 primitive depth identities、非复用投影、非 ColumnCRT/PDEC。
```

于是得到互斥完备分割：

```text
F_q = S_q disjoint_union C_q disjoint_union P_q disjoint_union E_q
S_q: SourceMaterializationFailure-PDEC/SAE
C_q: CRTWindowEmpty / WindowEdgeCollision / SupportMotion exits
P_q: actual primitive-supported packet
E_q: ProjectionCollision/ColumnCRT/PDEC or PrimitiveTwinSlotSupportEscape-PDEC/SAE
```

因此

```text
M_q^form=|F_q|=|S_q|+|C_q|+|P_q|+|E_q|
N_q=|P_q|
```

这证明“形式负载差额必须进入命名出口”不是 current sweep 的偶然性，而是 actual-load 管道的确定性分类律。当前 `40=28+11+1+0` 只是该分割的一个实例。最新硬点随之从 `GlobalFormalToActualCutsetPromotion` 进一步收缩为 `NamedExitExclusionOrSummabilityAfterCutsetCompleteness`。

## 52. after-cutset named-exit frontier 回接

后续文件

```text
experiments/prime_matrix_after_cutset_named_exit_frontier_router.py
docs/monograph/prime-matrix-after-cutset-named-exit-frontier-router.md
docs/monograph/prime-matrix-after-cutset-named-exit-frontier-router.json
data/prime-matrix-after-cutset-named-exit-frontier-ledger.json
```

本证书接在 cutset completeness 之后，把 `S_q/C_q/E_q` 后续出口统一成一张命名出口前沿表。当前读数为：

```text
formal_pair_total=40
actual_packet_total_current=1
formal_to_actual_gap=39
source_unmaterialized_pair_total_current=28
crt_window_empty_pair_total_current=11
unresolved_formal_pair_total_current=0
edge_collision_candidate_count_current=11
support_motion_candidate_count=11
min_endpoint_release_total_required=70
min_endpoint_release_over_support_width=3.500000
min_total_affine_depth_defect=70
fixed_highfactor_slot_pattern_isolation_failure_count_at_p0=0
transport_reset_pdec_atom_count=0
candidate_product_mass_upper_sum=0.023577117628562343<eta=0.025
high_density_epoch_pair_count=0
moving_residue_shape_count=37
singleton_residue_packet_count=300
current_sweep_frontier_closed=true
row_column_unconditional_closed=false
```

解释如下：

```text
SourceMaterializationFailure: 28 个 formal pairs；
CRTWindowEmpty: 11 个 formal pairs，主模数 899，支撑宽度 20，最小空窗距离 40；
WindowEdge/UnusedTarget: 11 个空窗边缘候选拆成 2 个 existing-actual collision 需要和 9 个 unused-target arrival 需要；
SupportMotion: 11 个支撑移动候选都需要双端点释放，最小释放 70=3.5*20；
PrimitiveIdentityShift: 固定 primitive key 不能吸收支撑移动，最小 affine depth defect 为 70；
MovingSlotFamily: 固定高因子槽图样当前隔离失败数为 0，剩余只能是 moving-slot family；
TransportReset: 12 个 transport cells 全为唯一 key，reset atom=0；
EpochPairMultiplicity: 当前候选总质量 0.023577117628562343<1/40，高密度行 0；
MovingResidue/SingletonSAE: 37 个 moving residue shapes 和 300 个 singleton packets 进入 SAE/Rankin 接口。
```

因此 cutset 后不再存在匿名容量或相位逃逸。新的精确硬点是

```text
GlobalNamedExitExclusionOrSummability
```

即证明这些命名出口在全局持久反例族中全被排斥，或总质量可求和吸收。本节仍不是行/列命题无条件证明；它把剩余从“分类是否完备”推进到“命名出口是否可全局吸收”。

## 53. global named-exit terminal choke 回接

后续文件

```text
experiments/prime_matrix_global_named_exit_terminal_choke_router.py
docs/monograph/prime-matrix-global-named-exit-terminal-choke-router.md
docs/monograph/prime-matrix-global-named-exit-terminal-choke-router.json
data/prime-matrix-global-named-exit-terminal-choke-ledger.json
```

本证书把上一节 after-cutset 的十个命名出口继续压缩为五个终端 choke：

```text
SourceAndCRTMaterialization
SupportMotionPrimitiveIdentity
TransportSingletonActiveEll
EpochPairPairedPressure
MovingResidueShapeSAE
```

当前显式容量/相位读数为：

```text
terminal_choke_count=5
all_terminal_chokes_closed_current_sweep=true
row_column_unconditional_closed=false
formal_pair_total=40
formal_to_actual_gap=39
unresolved_formal_pair_total_current=0
crt_phase_margin=879
min_endpoint_release_total_required=70
endpoint_release_extra_over_support_width=50
transport_reset_pdec_atom_count=0
one_slot_epoch_spare_ratio=0.9038893044128646
one_slot_epoch_min_spare_ratio=0.6901408450704225
active_ell_band=23..109
endpoint_gap_count=3
max_known_gap_fill_delay=80
candidate_single_pair_sae_mass_sum=0.0017756881442217531
max_paired_side_pressure_product=0.16017797552836485
paired_pressure_slack=0.8398220244716351
moving_residue_shape_count=37
```

所以当前反例链与真实链的最新显式冲突不是单个局部容量过载：固定 CRT 窗有大相位余量，支撑移动要付出双端点释放和 primitive depth defect，transport reset 原子为空，singleton 一槽 epoch 有大量剩余容量，AffineTwin epoch-pair 的两侧压力乘积也远低于 1。若全局反例链仍要复现，只能让这些余量沿持久族同步复现；这会进入对应的 PDEC/SAE/ColumnCRT 终端。最新主攻点因此改写为：

```text
TerminalChokeSetGlobalExclusionOrSummability
```

即排斥这五个终端 choke 的持久复现，或证明它们的总质量可求和吸收。

## 54. terminal choke amplification barrier 回接

后续文件

```text
experiments/prime_matrix_terminal_choke_amplification_barrier_router.py
docs/monograph/prime-matrix-terminal-choke-amplification-barrier-router.md
docs/monograph/prime-matrix-terminal-choke-amplification-barrier-router.json
data/prime-matrix-terminal-choke-amplification-barrier-ledger.json
```

本证书把五个终端 choke 的“复现需要多大放大”量化为放大屏障。当前排序为：

```text
CRTWindowPhaseJump
 -> OneSlotTransportOverflow
 -> SupportEndpointRelease
 -> EpochPairPairedPressure
 -> FixedMovingSlotCRT
```

核心读数为：

```text
narrowest_barrier=CRTWindowPhaseJump
narrowest_barrier_factor=2.000000000000
narrowest_terminal_barrier=OneSlotTransportOverflow
narrowest_terminal_factor=3.227272727273
tight_epoch_key=minus:71
tight_epoch_used=22
tight_epoch_capacity=71
tight_epoch_unused=49
tight_epoch_overflow_new_units=50
support_endpoint_release_extra_units=50
fifty_unit_cross_lock=true
support_release_factor=3.500000000000
moving_slot_crt_factor=7.028846153846
pressure_amplification_to_failure=6.243055555556
fill_total_min_rankin_mass_if_all_cross=0.169986671425
transport_reset_pdec_atom_count=0
```

解释如下。CRT 空窗到最近支撑窗只需 `40=2*20` 的相位跳，但它不是独立终端；该跳动会立即进入 `UnusedTargetArrival` 或 `WindowEdgeCollision-PDEC/SAE`。真正终端侧的最窄门槛是 singleton/transport 一槽溢出：最拥挤 epoch 为 `minus:71`，当前只用 `22/71`，还要新增 `50` 个 residue 才会越界；另一方面 support motion 若要移动支撑，最小端点释放为 `70`，相对支撑宽度 `20` 的额外释放也正好是 `50`。

因此最新显式交叉点变成：

```text
FiftyUnitCrossLockOrTerminalPDECExclusion
```

即全局反例链若继续沿真实链复现，必须支付同一个 `50-unit` release/residue 包；若不能支付，则容量不足；若通过重复 residue 或移动槽图样支付，则进入 reset/PDEC/SAE/ColumnCRT 终端。

## 55. fifty-unit cross-lock carrier separation 回接

后续文件

```text
experiments/prime_matrix_fifty_unit_cross_lock_carrier_separation_router.py
docs/monograph/prime-matrix-fifty-unit-cross-lock-carrier-separation-router.md
docs/monograph/prime-matrix-fifty-unit-cross-lock-carrier-separation-router.json
data/prime-matrix-fifty-unit-cross-lock-carrier-separation-ledger.json
```

本证书继续下钻上一节的 `50-unit cross-lock`。关键结论是：这个 `50` 不是同一载体上的即时矛盾，而是两个互素载体之间的同步门。

```text
support_atom_key=19:12
support_q=31
support_generator_residue=19
support_fill_residue=12
support_generator_p=2687
support_endpoint_release_extra_units=50
tight_epoch_key=minus:71
tight_epoch_used=22
tight_epoch_capacity=71
tight_epoch_overflow_new_units=50
same_q_or_ell=false
same_side_taxonomy=false
same_p_band=false
direct_same_carrier_contradiction=false
cross_carrier_sync_required=true
combined_carrier_modulus=2201
combined_modulus_over_fifty_units=44.02
p_delay_mod_tight_epoch=9
p_delay_gcd_tight_epoch=1
fifty_distinct_residue_count=50
fifty_step_ramp_is_reset_free=true
first_enter_epoch_p=4207
last_fifty_block_p=8127
fifty_step_block_can_fit_current_epoch_p_range=true
if_fifty_new_residues_sync_then_one_slot_overflow=true
newness_against_existing_epoch_residues_proved=false
```

解释如下。支撑移动最窄原子在 `q=31/source_pair=19:12`，当前 `P` 带约为 `2629..2687`；最拥挤 singleton epoch 是 `minus:71`，当前 `P` 区间为 `4177..9257`。因此二者不构成同载体直接矛盾，必须通过互素模数 `31*71=2201` 的跨载体 CRT 门同步。

固定 `p_delay=80` 在模 `71` 上等于 `9`，且 `gcd(80,71)=1`，所以前 `50` 步给出 `50` 个互异 residue；从 `P=4207` 到 `8127` 的 50 步块可以放入当前 `minus:71` 的 P 区间。这说明“重复 residue 立刻触发 PDEC”的短路路线不能免费使用。反过来，若这 50 个跨载体到达都作为新 residue 同步进入 `minus:71`，则 `22+50>71`，立即越过 one-slot 容量。

因此最新最窄剩余接口被精确改写为：

```text
CrossCarrierFiftyUnitSynchronizationPDECOrSAE
```

也就是证明 50 个跨载体到达若持久同步则必须为新 residue 并越界，或把非新/不同步形态登记为 `TransportReset-PDEC`、`SingletonResidue-SAE`、`SupportMotion/UnusedTarget` 或 `MovingCarrier-ColumnCRT`。本节仍不是全局行/列命题证明；它关闭的是同载体直接矛盾路线，并把剩余压成跨载体同步的新硬点。

## 56. cross-carrier fifty-unit residue saturation 回接

后续文件

```text
experiments/prime_matrix_cross_carrier_fifty_unit_residue_saturation_router.py
docs/monograph/prime-matrix-cross-carrier-fifty-unit-residue-saturation-router.md
docs/monograph/prime-matrix-cross-carrier-fifty-unit-residue-saturation-router.json
data/prime-matrix-cross-carrier-fifty-unit-residue-saturation-ledger.json
```

本证书重建 `minus:71` 的完整 singleton 物理记录，而不是继续使用 sample。核心读数为：

```text
shape_key=size=1|side=minus|ells=71
used_residue_count_reconstructed=22
exact_used_matches_capacity_ledger=true
used_residues=[3,9,10,12,18,21,22,26,27,28,34,35,36,37,39,40,44,46,53,59,65,66]
admitted_step_range=[19,82]
admitted_p_range_on_support_lattice=[4207,9247]
admitted_distinct_residue_count=64
admitted_intersection_existing_count=17
admitted_new_residue_count=47
union_size_after_admitted_band=69
spare_after_admitted_band=2
missing_residues_after_admitted_band=[0,62]
direct_fifty_overflow_current_blocks=false
min_block_new_residue_count=34
max_block_new_residue_count=40
max_block_union_size=62
min_block_spare_after=9
p_extension_to_first_missing_residue=390
p_extension_to_full_capacity=470
p_extension_to_post_full_repeat=550
```

这一步修正了上一接口中的潜在捷径：50 步同步块不是 50 个全新 residue。当前可进入 `minus:71` 的 15 个连续 50 步块，最多只新增 40 个 residue，并集最大为 `62/71`，不能直接溢出。若把整个当前可进入的 support lattice 带都算上，它有 64 个互异 residue，其中 17 个已在既有 singleton 集中，新增 47 个；合并后为 `69/71`，只剩 `0` 与 `62` 两个空位。

当前最窄剩余因此从“50 新 residue 溢出”改写为“两空位端点外延/重置”：

```text
TwoResidueSpareEndpointExtensionOrTransportResetPDEC
```

具体地，若端点外延到 `P=9647` 和 `P=9727`，两个空位会依次被填满；再到 `P=9807`，同步 residue 已是旧 residue，必须触发 transport reset-PDEC，或提前回到 SAE、unused-target、moving-carrier 出口。本节仍未关闭全局行/列命题；它排除了当前带内的直接溢出捷径，并把剩余压成显式的两空位端点外延问题。

## 57. two-residue spare prime-anchor filter 回接

后续文件

```text
experiments/prime_matrix_two_residue_spare_prime_anchor_filter_router.py
docs/monograph/prime-matrix-two-residue-spare-prime-anchor-filter-router.md
docs/monograph/prime-matrix-two-residue-spare-prime-anchor-filter-router.json
data/prime-matrix-two-residue-spare-prime-anchor-filter-ledger.json
```

本证书把上一节的两空位端点外延再加上一条真实链必要条件：外延锚 `P` 必须为奇素数。核心读数为：

```text
previous_hardpoint=TwoResidueSpareEndpointExtensionOrTransportResetPDEC
admitted_step_range=[19,82]
admitted_lattice_step_count=64
admitted_prime_anchor_count=17
admitted_composite_anchor_count=47
admitted_prime_anchor_new_residue_count=13
prime_filtered_union_size=35
prime_filtered_nonzero_spare=35
residue_zero_prime_anchor_impossible=true
residue_zero_p_class_mod_5680=4047
residue_zero_gcd_class_modulus=71
predicted_two_spare_rows_are_prime=false
first_prime_hit_for_residue_62={step:300,p:26687,residue:62}
first_full_nonzero_capacity_row={residue:67,step:1192,p:98047}
first_repeat_after_full_nonzero_capacity={step:1194,p:98207,residue:14}
```

解释如下。上一节的近端外延给出 `P=9647 -> residue 62`、`P=9727 -> residue 0`、`P=9807 -> residue 9`，但这三个 `P` 都不是素数锚；尤其 `residue 0` 的整条 AP 类满足 `P≡4047 (mod 5680)`，与模数的 gcd 为 `71`，因此在 `P>71` 时结构性不可能为素数锚。`residue 62` 虽结构上可行，但首个素数锚推迟到 `P=26687`。

所以 near-fill 并不是一条真实链。把当前 admitted lattice 的 64 个步号按素数锚过滤后，只剩 17 个素数锚，新增 residue 仅 13 个；与既有 22 个 residue 合并后只有 `35/70` 个非零 residue 被覆盖，仍有 35 个非零空位。若反例链仍要通过 `minus:71` 的长 AP 素数锚到达填满所有非零 residue，当前扫描中最后一个缺失非零 residue 到 `P=98047` 才出现，随后首个素数锚重复在 `P=98207`，才会进入 transport reset-PDEC。

因此最新最窄剩余接口被改写为：

```text
PrimeAnchorFilteredNonzeroResidueCoverageOrTransportResetPDEC
```

这一步关闭了“两空位近端端点外延即可填满”的真实链解释，并把剩余压成长 AP 素数锚覆盖全部非零 residue 或 transport reset-PDEC。全局行/列命题仍未无条件闭合。

## 58. prime-anchor post-band immediate repeat 回接

后续文件

```text
experiments/prime_matrix_prime_anchor_postband_immediate_repeat_router.py
docs/monograph/prime-matrix-prime-anchor-postband-immediate-repeat-router.md
docs/monograph/prime-matrix-prime-anchor-postband-immediate-repeat-router.json
data/prime-matrix-prime-anchor-postband-immediate-repeat-ledger.json
```

本证书继续攻击上一节留下的长 AP 非零 residue 覆盖分支。关键发现是：覆盖并不是只被推迟，而是在 admitted 带后第一个素数锚处就被旧 residue 抢先截断。

```text
previous_hardpoint=PrimeAnchorFilteredNonzeroResidueCoverageOrTransportResetPDEC
current_prime_filtered_union_size=35
current_prime_filtered_nonzero_spare=35
first_postband_prime_anchor={step:90,p:9887,residue:18}
first_postband_prime_is_repeat=true
first_postband_prime_is_original_used_repeat=true
new_prime_anchor_count_before_first_repeat=0
missing_nonzero_remaining_at_first_repeat=35
repeat_p_extension_beyond_epoch_p_max=630
coverage_before_reset_possible_in_same_epoch=false
```

具体地，admitted 带结束于步号 `82`；之后步号 `83..89` 的候选都不是素数锚，其中 `9647`、`9727`、`9807` 正是上一节的近端候选。步号 `90` 给出第一个素数锚 `P=9887`，其 `minus:71` residue 为 `18`。而 `18` 已在原始已用 residue 集

```text
[3,9,10,12,18,21,22,26,27,28,34,35,36,37,39,40,44,46,53,59,65,66]
```

中，不只是 prime-filtered 合并后才出现的 residue。因此如果同一无 reset epoch 延伸到 `P=9887`，它在补入任何新缺失非零 residue 之前已经触发旧 residue repeat，必须进入 transport reset-PDEC；如果该 epoch 不能延伸到此点，则出口是 endpoint motion/SAE。

最新最窄剩余接口因此改写为：

```text
ImmediatePrimeAnchorRepeatTransportResetPDECOrEndpointMotionSAE
```

这一步关闭了 `PrimeAnchorFilteredNonzeroResidueCoverage` 分支在当前 primitive epoch 内的 reset-free 实现。全局行/列命题仍需排斥 transport reset-PDEC 或 endpoint motion/SAE 的持久复现。

## 59. prime-anchor repeat reset atom 回接

后续文件

```text
experiments/prime_matrix_prime_anchor_repeat_reset_atom_router.py
docs/monograph/prime-matrix-prime-anchor-repeat-reset-atom-router.md
docs/monograph/prime-matrix-prime-anchor-repeat-reset-atom-router.json
data/prime-matrix-prime-anchor-repeat-reset-atom-ledger.json
```

本证书把上一节的 immediate repeat 从“旧 residue”提升为一个明确的一槽 reset 原子。原始 singleton 记录中，`minus:71` 的 `residue=18` 来自：

```text
original_record_p=7757
slot_keys=['644:128:71']
```

而 admitted 带后首个素数锚为：

```text
repeat_prime_anchor_p=9887
repeat_residue=18
p_delta=2130=30*71
original_lift=109
repeat_lift=139
lift_delta=30
exact_same_residue_ell_translate=true
reset_atom_instantiated=true
new_prime_anchor_count_before_first_repeat=0
missing_nonzero_remaining_at_reset_atom=35
```

因此 `P=9887` 不是新的覆盖相位，而是 `P=7757` 同一个 residue packet 的 30 个 `ell` 周期平移。若保持同一无 reset epoch，`one-slot-repeat-reset|side=minus|ell=71|residue=18|lift_delta=30|p=7757->9887` 已经实例化；若反例链拒绝 reset，则必须在首个 post-band 素数锚之前切断端点：

```text
must_cut_before_step=90
must_cut_before_p=9887
step_gap_after_admitted_band=8
p_extension_beyond_epoch_p_max=630
composite_buffer_steps=[83,84,85,86,87,88,89]
```

最新最窄剩余接口为：

```text
OneSlotPrimeAnchorRepeatResetPDECExclusionOrEndpointMotionSAE
```

本步把“是否会 repeat”转成“已实例化的 repeat-reset 原子是否可全局排斥，或端点运动是否可 SAE/Rankin 吸收”。全局行/列命题仍未无条件闭合。

## 60. endpoint cut zero-gain 回接

后续文件

```text
experiments/prime_matrix_endpoint_cut_zero_gain_router.py
docs/monograph/prime-matrix-endpoint-cut-zero-gain-router.md
docs/monograph/prime-matrix-endpoint-cut-zero-gain-router.json
data/prime-matrix-endpoint-cut-zero-gain-ledger.json
```

本证书攻击上一节剩余的 endpoint-motion 逃逸：若为了避免 `P=9887` 的 repeat-reset 而切断端点，那么从当前 epoch 上界到首个 post-band 素数锚之前是否有任何实际素数锚收益。结果为零：

```text
previous_hardpoint=OneSlotPrimeAnchorRepeatResetPDECExclusionOrEndpointMotionSAE
cut_buffer_step_count=7
cut_buffer_steps=[83,84,85,86,87,88,89]
cut_buffer_p_values=[9327,9407,9487,9567,9647,9727,9807]
formal_gap_composite_row_count=2
formal_gap_composite_residues=[62,0]
actual_prime_anchor_count_before_reset=0
actual_new_prime_anchor_count_before_reset=0
endpoint_cut_actual_gain_zero=true
reset_atom_instantiated_at_first_prime_anchor=true
reset_or_zero_gain_endpoint_dichotomy_closed_current_epoch=true
```

这里 `residue 62` 与 `residue 0` 是形式缺口，但对应的 `P=9647` 与 `P=9727` 分别为合数和 `71` 的倍数；其余缓冲步号也都是旧 residue 的合数锚。因此端点切断在当前 primitive epoch 内不能获得任何实际素数锚容量，只是一个 zero-gain endpoint SAE 形态。若不切断，`step=90,P=9887` 立即进入上一节已实例化的一槽 repeat-reset PDEC。

最新最窄剩余接口为：

```text
ZeroGainEndpointCutSAEOrOneSlotResetPDECExclusion
```

本步关闭的是当前 epoch 的“端点切断可获得真实覆盖收益”解释。全局行/列命题仍需排斥 one-slot reset-PDEC 的持久复现，或证明 zero-gain endpoint cut 的 SAE/Rankin 可吸收。

## 61. endpoint cut no-payload SAE 回接

后续文件

```text
experiments/prime_matrix_endpoint_cut_no_payload_sae_router.py
docs/monograph/prime-matrix-endpoint-cut-no-payload-sae-router.md
docs/monograph/prime-matrix-endpoint-cut-no-payload-sae-router.json
data/prime-matrix-endpoint-cut-no-payload-sae-ledger.json
```

本证书把上一节的 zero-gain endpoint cut 进一步提升为“空 actual payload”。端点切断缓冲 `step=83..89` 中：

```text
actual_prime_anchor_count_before_reset=0
actual_new_prime_anchor_count_before_reset=0
filtered_repeat_prime_anchor_count_before_reset=0
actual_payload_empty=true
actual_payload_mass=0
formal_gap_composite_residues=[0,62]
missing_nonzero_before_cut=35
missing_nonzero_after_cut=35
missing_nonzero_set_preserved_by_cut=true
endpoint_cut_routes_to_no_payload_sae=true
reset_atom_at_first_prime_anchor=true
```

也就是说，端点切断不只是没有新增 coverage；它完全没有 actual prime-anchor payload，且缺失非零 residue 集不变。形式缺口 `62,0` 被素数锚过滤掉后不留下任何实际支撑。因此 endpoint 分支不能提供反例链所需容量，只能登记为 no-payload endpoint SAE；若不走该 SAE，首个素数锚已经是一槽 reset-PDEC。

最新最窄剩余接口为：

```text
OneSlotResetPDECExclusionOrNoPayloadEndpointSAESummability
```

本步关闭的是当前 primitive epoch 的 endpoint cut actual-load 出口；全局仍需排斥 one-slot reset-PDEC 持久复现，或证明 no-payload endpoint SAE 的全局可求和/可吸收。

## 62. one-slot reset prefix no-relief 回接

后续文件

```text
experiments/prime_matrix_one_slot_reset_prefix_no_relief_router.py
docs/monograph/prime-matrix-one-slot-reset-prefix-no-relief-router.md
docs/monograph/prime-matrix-one-slot-reset-prefix-no-relief-router.json
data/prime-matrix-one-slot-reset-prefix-no-relief-ledger.json
```

本证书继续攻击上一节剩余的 reset 端：若不走 no-payload endpoint SAE，而接受 `step=90,P=9887,residue=18` 的一槽 reset，则该 reset 之后不会立刻产生新缺失非零 residue relief。精确读数为：

```text
previous_hardpoint=OneSlotResetPDECExclusionOrNoPayloadEndpointSAESummability
reset_step=90
reset_p=9887
reset_residue=18
endpoint_cut_actual_payload_empty=true
prefix_step_count_before_first_relief=25
prefix_prime_anchor_count_before_first_relief=7
prefix_new_missing_nonzero_count_before_first_relief=0
prefix_repeat_prime_anchor_count_before_first_relief=7
first_missing_nonzero_relief=(step=115,P=11887,residue=30)
first_relief_requires_accepted_reset_pdec=true
```

因此当前反例链若要从这条同步线上取得新的实际容量，必须先越过已经材料化的一槽 reset-PDEC；在 reset 到首个 relief 之间，所有实际素数锚都是已见 residue，不能减少 `35` 个缺失非零 residue。若拒绝 reset，则剩余端点分支已经是 no-payload endpoint SAE。

最新最窄剩余接口为：

```text
AcceptedResetPDECExclusionOrDelayedReliefSupportMotionSAE
```

本步关闭的是“接受 reset 后立即获得新容量”的解释；全局仍需排斥 accepted reset-PDEC 的持久复现，或证明延迟 relief 所要求的 support motion/SAE 可全局吸收。

## 63. accepted reset full relief horizon 回接

后续文件

```text
experiments/prime_matrix_accepted_reset_full_relief_horizon_router.py
docs/monograph/prime-matrix-accepted-reset-full-relief-horizon-router.md
docs/monograph/prime-matrix-accepted-reset-full-relief-horizon-router.json
data/prime-matrix-accepted-reset-full-relief-horizon-ledger.json
```

本证书继续推进上一节的 delayed relief：若接受一槽 reset 后沿同一同步线等待所有 `35` 个缺失非零 residue 都被真实素数锚补到，则完整 relief horizon 远离当前 primitive epoch：

```text
previous_hardpoint=AcceptedResetPDECExclusionOrDelayedReliefSupportMotionSAE
missing_nonzero_count_at_reset=35
reset_step=90
reset_p=9887
first_relief=(step=115,P=11887,residue=30)
full_relief=(step=1192,P=98047,residue=67)
full_relief_step_gap_after_reset=1102
full_relief_p_gap_after_reset=88160
full_relief_extension_over_epoch_width=17.474906514466
prime_anchor_count_until_full_relief=260
new_relief_prime_anchor_count_until_full_relief=35
repeat_prime_anchor_count_until_full_relief=225
composite_missing_candidate_count_until_full_relief=101
```

因此，完整 relief 不是当前局部结构内的即时容量修补；它需要在 reset 之后进行长程 support motion。中间 `225` 个 repeat prime-anchor 不减少缺失非零 residue，`101` 个形式缺失命中又被合数过滤掉。

最新最窄剩余接口为：

```text
AcceptedResetPDECExclusionOrLongReliefHorizonSupportMotionSAE
```

本步关闭的是“accepted reset 后局部补完全部 actual relief”的解释；全局仍需排斥 accepted reset-PDEC，或证明这种长程 relief horizon 的 support-motion/SAE 可吸收。

## 64. long relief cycle-debt 回接

后续文件

```text
experiments/prime_matrix_long_relief_cycle_debt_router.py
docs/monograph/prime-matrix-long-relief-cycle-debt-router.md
docs/monograph/prime-matrix-long-relief-cycle-debt-router.json
data/prime-matrix-long-relief-cycle-debt-ledger.json
```

本证书把 long-relief horizon 进一步分解为固定 `ell=71` 周期上的相位等待债务。由于同步线的 residue 周期为 `71` 步、P 周期为 `5680`，每个缺失 residue 在 reset 后都有一个首次形式命中；若该命中为合数，就必须等待下一个完整 `71` 周期。

核心读数为：

```text
previous_hardpoint=AcceptedResetPDECExclusionOrLongReliefHorizonSupportMotionSAE
ell=71
period_p=5680
missing_nonzero_count=35
zero_cycle_relief_count=8
positive_cycle_debt_residue_count=27
total_cycle_debt=101
total_composite_wait_count=101
matches_full_horizon_composite_missing_count=true
max_cycle_debt=15
max_cycle_debt_residue=67
max_cycle_debt_p_delay=85200
periods_touched_until_full_relief=16
```

这说明上一节的 `101` 个合数形式命中并非噪声，而是精确等于所有缺失 residue 的周期相位债务总和。最大硬点是 `residue=67`：首次形式命中在 `P=12847`，但真实素数锚要等到 `P=98047`，中间跨 `15` 个完整 `71` 周期。

最新最窄剩余接口为：

```text
LongReliefCycleDebtPDECExclusionOrSupportMotionSAESummability
```

本步关闭的是“long relief 只是远端但无结构代价”的解释；全局仍需排斥这种周期债务族的 PDEC 复现，或证明其 support-motion/SAE 可全局求和吸收。

## 65. one-period relief deficit 回接

后续文件

```text
experiments/prime_matrix_one_period_relief_deficit_router.py
docs/monograph/prime-matrix-one-period-relief-deficit-router.md
docs/monograph/prime-matrix-one-period-relief-deficit-router.json
data/prime-matrix-one-period-relief-deficit-ledger.json
```

本证书把上一节的周期债务压成一个更局部的容量-相位交叉点：reset 后第一个完整 `ell=71` 周期为 `step=90..160`，对应 `P=9887..15487`。这个周期已经遍历全部 `71` 个 residue，因此 35 个缺失非零 residue 都各自形式命中一次。

精确读数为：

```text
previous_hardpoint=LongReliefCycleDebtPDECExclusionOrSupportMotionSAESummability
period_is_complete_residue_cycle=true
missing_nonzero_required=35
formal_missing_hit_count=35
actual_relief_count_in_one_period=8
composite_missing_count_in_one_period=27
repeat_prime_anchor_count_in_one_period=10
relief_deficit_after_one_period=27
composite_missing_matches_positive_cycle_debt_residues=true
```

也就是说，一个 reset-local 完整周期已经给了所有缺失 residue 一次机会，但真实链只得到 `8` 个 actual relief；另外 `27` 个机会全是合数形式命中，正好就是 cycle-debt 证书中的正周期债务 residue。与此同时，同周期还产生 `10` 个 repeat prime-anchor，继续施加 reset/旧容量压力。

最新最窄剩余接口为：

```text
OnePeriodReliefDeficitForcesCycleDebtPDECOrSupportMotionSAE
```

本步关闭的是“一个 reset-local 周期即可提供足够 actual relief”的解释；全局仍需排斥由该缺口强制出的周期债务 PDEC，或证明后续 support-motion/SAE 可吸收。

## 66. cycle-debt CRT cover pressure 回接

后续文件

```text
experiments/prime_matrix_cycle_debt_crt_cover_pressure_router.py
docs/monograph/prime-matrix-cycle-debt-crt-cover-pressure-router.md
docs/monograph/prime-matrix-cycle-debt-crt-cover-pressure-router.json
data/prime-matrix-cycle-debt-crt-cover-pressure-ledger.json
```

本证书把 `27` 个正周期债务 residue 的合数等待写成周期坐标 `k` 上的 CRT 阻断覆盖。对每个同 residue 周期列

```text
P(k)=P0+5680*k
```

若第 `k` 个形式命中为合数，最小素因子 `q` 给出一个周期坐标同余类 `k mod q`。合并所有正债务 residue 后得到：

```text
previous_hardpoint=OnePeriodReliefDeficitForcesCycleDebtPDECOrSupportMotionSAE
positive_cycle_debt_residue_count=27
total_composite_waits=101
global_unique_blocker_factor_count=24
global_blocker_lcm=337212073559813724487421695331234639247
global_blocker_product_log10=38.527903115735
max_row_residue=67
max_row_cycle_debt=15
max_row_unique_blocker_factor_count=11
max_row_blocker_lcm=55140500775337593
crt_cover_modulus_exceeds_local_period=true
```

这说明周期债务不是单一小模数反复造成的局部偶然。若反例链要把这种 debt pattern 作为全局族复现，它必须携带 `24` 个不同阻断素因子组成的 CRT 相位包；其 lcm 已远大于本地 P 周期 `5680`。最大压力行 `residue=67` 单独就需要 `11` 个不同阻断素因子，单行 lcm 达 `55140500775337593`。

最新最窄剩余接口为：

```text
CycleDebtCRTCoverPressurePDECOrGlobalSupportMotionSAE
```

本步关闭的是“周期债务可作为无结构局部漂移复现”的解释；全局仍需排斥这种大 CRT cover family 的 PDEC，或证明相应 global support-motion SAE 可求和吸收。

## 67. cycle-debt transverse CRT independence 回接

后续文件

```text
experiments/prime_matrix_cycle_debt_transverse_crt_independence_router.py
docs/monograph/prime-matrix-cycle-debt-transverse-crt-independence-router.md
docs/monograph/prime-matrix-cycle-debt-transverse-crt-independence-router.json
data/prime-matrix-cycle-debt-transverse-crt-independence-ledger.json
```

本证书把上一节的 CRT cover pressure 继续压到本地周期与横向 CRT 相位的交叉点。当前本地周期为

```text
period_p=5680=2^4*5*71
```

而上一节出现的 `24` 个阻断素因子全部与 `5680` 互素：

```text
global_unique_blocker_factor_count=24
transverse_blocker_factor_count=24
all_blocker_factors_coprime_to_period_p=true
gcd_global_blocker_lcm_with_period_p=1
combined_period_equals_product=true
global_blocker_lcm=337212073559813724487421695331234639247
global_lcm_over_period_p_floor=59368322809826359944968608332963844
global_lcm_over_period_p_remainder=5327
all_row_shift_replay_crt_consistent=true
all_row_shift_replay_classes_zero=true
all_row_lcm_exceeds_phase_support_width=true
local_period_absorption_closed_current_certificate=true
```

解释如下：固定一个缺失 residue 的同 residue 列

```text
P(k)=P0+5680*k
```

若第 `c` 个等待被阻断素因子 `q` 覆盖，则 `q` 与 `5680` 互素，因而复现同一阻断等待的平移量 `K` 必须满足 `K=0 mod q`。一行合并为 `K=0 mod row_lcm`，27 行合并为

```text
K=0 mod 337212073559813724487421695331234639247.
```

这个模数与本地周期 `5680` 互素，所以它不是周期自身的因子、不是同一槽内的局部漂移，也不能由本地周期平移吸收。最大压力行仍是 `residue=67`，`cycle_debt=15`，但单行复现模数已为 `55140500775337593`。

最新最窄剩余接口为：

```text
TransverseCRTCoverPDECExclusionOrGlobalSupportMotionSAE
```

本步关闭的是“cycle-debt CRT cover 可由本地周期/局部槽移动自然复现”的解释；全局仍需排斥 transverse CRT cover PDEC，或证明真正 global support-motion SAE 可求和吸收。

## 68. cycle-debt sparse replay barrier 回接

后续文件

```text
experiments/prime_matrix_cycle_debt_sparse_replay_barrier_router.py
docs/monograph/prime-matrix-cycle-debt-sparse-replay-barrier-router.md
docs/monograph/prime-matrix-cycle-debt-sparse-replay-barrier-router.json
data/prime-matrix-cycle-debt-sparse-replay-barrier-ledger.json
```

本证书把横向 CRT cover 的 exact replay 复现间距显式化。若保持同一阻断图和同一阻断相位类，则完整 debt word 的平移量必须是全局横向 lcm 的倍数：

```text
global_exact_replay_cycle_modulus=337212073559813724487421695331234639247
global_exact_replay_p_gap=1915364577819741955088555229481412750922960
global_exact_replay_density_log10=-38.527903115735
max_cycle_debt_support_width=15
total_composite_wait_width=101
full_relief_cycle_span=1102/71
full_relief_cycle_span_ceiling=16
global_modulus_over_full_cycle_span_ceiling_floor=21075754597488357780463855958202164952
single_full_debt_copy_per_full_relief_horizon=true
rows_with_replay_modulus_exceeding_own_debt=27
exact_replay_branch_is_sae_sparse_current_certificate=true
non_sparse_persistence_forces_moving_blocker_map=true
```

因此，在任意短于 `global_lcm` 的局部/中程 support-motion 窗口中，完整 transverse CRT debt word 至多出现一份 exact 复本。当前 full-relief 可见跨度只有 `ceil(1102/71)=16` 个 residue 周期，远小于完整复现间距；若坚持 exact replay，该分支只能作为孤立低密度原子进入 SAE 账本。若反例链要求正密度或短窗口内持续复现，就必须改变阻断素因子、相位类或行组合，这正是 moving transverse cover PDEC。

最新最窄剩余接口为：

```text
SparseReplaySAEOrMovingTransverseCoverPDEC
```

本步关闭的是“保持同一 transverse CRT cover 即可高频补偿容量”的解释；全局仍需排斥 moving transverse cover PDEC，或把 exact sparse replay 的 SAE 求和完全接入。

## 69. cycle-debt near-shift exit-boundary 回接

后续文件

```text
experiments/prime_matrix_cycle_debt_near_shift_exit_boundary_router.py
docs/monograph/prime-matrix-cycle-debt-near-shift-exit-boundary-router.md
docs/monograph/prime-matrix-cycle-debt-near-shift-exit-boundary-router.json
data/prime-matrix-cycle-debt-near-shift-exit-boundary-ledger.json
```

本证书继续攻击 moving transverse cover 分支：若不是 exact 稀疏复现，而是试图做近程移动，那么旧 debt 前缀会被每行的首个 relief prime 边界撕裂。当前审计取 near-shift 窗口为上一节 full-relief 周期跨度上取整：

```text
near_shift_limit_cycles=16
near_shift_limit_p=90880
positive_cycle_debt_residue_count=27
total_cycle_debt_mass=101
max_cycle_debt=15
tested_nonzero_near_shift_count=16
all_near_shifts_close_old_prefix_reuse=true
shift_1_exit_prime_collision_row_count=27
shift_1_exit_prime_collision_debt_mass=101
shift_max_cycle_debt_exit_prime_collision_row_count=1
shift_max_cycle_debt_exit_prime_collision_debt_mass=15
shift_near_limit_fresh_cover_required_row_count=27
shift_near_limit_fresh_cover_required_debt_mass=101
moving_branch_must_replace_some_or_all_support_rows=true
```

对任一正债务行，原始 composite prefix 的第 `debt` 个周期正是该行首个素数 relief。因此平移量 `1<=K<=debt` 会把这个 exit prime 拉入平移后的 debt word；而 `K>debt` 时，旧 composite prefix 已完全不能为该行提供复用支撑。结果是：`K=1` 时 27 行全部撞上 exit prime；`1<=K<=15` 时所有 `debt>=K` 的行被撕裂；`K=16` 时 27 行全都必须 fresh cover。

最新最窄剩余接口为：

```text
FreshMovingCoverPDECOrGlobalSupportMotionSAE
```

本步关闭的是“moving 分支只是旧 CRT cover 的近程滑动复用”的解释；全局仍需排斥 fresh moving cover PDEC，或证明它只能形成 global support-motion SAE。

## 70. cycle-debt fresh-cover prime-obstacle 回接

后续文件

```text
experiments/prime_matrix_cycle_debt_fresh_cover_prime_obstacle_router.py
docs/monograph/prime-matrix-cycle-debt-fresh-cover-prime-obstacle-router.md
docs/monograph/prime-matrix-cycle-debt-fresh-cover-prime-obstacle-router.json
data/prime-matrix-cycle-debt-fresh-cover-prime-obstacle-ledger.json
```

本证书把 fresh moving cover 在同一 27 个正债务 residue 支撑行上的真实障碍直接数出。对每个 `K=1..16`，取与原 debt 长度相同的 shifted window；若 fresh cover 仍想在同一支撑行上重建全合数词，这些窗口必须全部为 composite。但真实审计为：

```text
positive_cycle_debt_residue_count=27
total_cycle_debt_mass_per_shift=101
tested_shift_count=16
total_tested_same_support_slots=1616
total_prime_obstacles_all_near_shifts=364
total_new_prime_obstacles_all_near_shifts=263
all_near_shift_same_support_windows_have_prime_obstacles=true
min_prime_obstacle_count_per_shift=17
min_prime_obstacle_shift=5
min_prime_obstacle_rows_per_shift=12
max_prime_obstacle_count_per_shift=28
max_prime_obstacle_shift=14
shift_1_prime_obstacle_count=27
shift_near_limit_prime_obstacle_count=27
shift_near_limit_new_prime_obstacle_count=27
same_support_fresh_cover_closed_current_certificate=true
support_row_replacement_or_prime_obstacle_pdec_required=true
```

也就是说，同一支撑行的任意近程 fresh window 都含 actual prime obstacles。最轻的 `K=5` 仍有 `17` 个素数障碍；完全越过旧前缀的 `K=16` 仍有 `27` 个素数障碍，且全部是新素数障碍。因此 same-support fresh cover 已被真实链阻断。

最新最窄剩余接口为：

```text
FreshCoverPrimeObstaclePDECOrSupportRowReplacementSAE
```

本步关闭的是“fresh moving cover 可在同一支撑行上重建全合数词”的解释；全局仍需排斥删除实际素数障碍的 PDEC，或证明支撑行替换只能形成可求和的 support-row replacement SAE/PDEC。

## 71. cycle-debt support-row replacement Hall 回接

后续文件

```text
experiments/prime_matrix_cycle_debt_support_row_replacement_hall_router.py
docs/monograph/prime-matrix-cycle-debt-support-row-replacement-hall-router.md
docs/monograph/prime-matrix-cycle-debt-support-row-replacement-hall-router.json
data/prime-matrix-cycle-debt-support-row-replacement-hall-ledger.json
```

本证书把 support-row replacement 写成全局容量匹配问题：35 个缺失 residue 候选行，对 27 个正债务需求行。对每个近程相位 `K`，候选行容量定义为从 `K` 开始最长连续 composite 段；需求是原正债务行的 debt 长度。Hall 阈值条件为：

```text
candidate rows with capacity>=t >= demand rows with debt>=t
```

审计结果：

```text
candidate_missing_residue_count=35
needed_positive_debt_row_count=27
total_demand_width=101
max_required_width=15
hall_fail_shift_count=14
hall_fail_shifts=[1,2,3,4,5,6,7,8,9,10,11,12,15,16]
hall_survivor_shift_count=2
hall_survivor_shifts=[13,14]
all_but_k13_k14_fail_hall_capacity=true
k13_assigned_immediate_relief_rows=6
k14_assigned_immediate_relief_rows=8
support_row_replacement_closed_except_k13_k14_current_certificate=true
```

因此，16 个近程相位中有 14 个不只是含素数障碍，而是即便允许换到任意缺失 residue 行，也在阈值 Hall 容量上不足。仅 `K=13,14` 通过容量测试；但二者都必须调用原本 immediate-relief 的行，并且需要大规模替换：`K=13` 替换 26 行，`K=14` 替换 27 行。

最新最窄剩余接口为：

```text
K13K14SupportReplacementSurvivorPDECOrGlobalSAE
```

本步关闭的是“support-row replacement 可在大多数近程相位自由实现”的解释；全局仍需排斥 `K=13,14` 两个幸存相位，或证明它们只能形成 global SAE/PDEC。

## 72. cycle-debt K13/K14 survivor rigidity 回接

后续文件

```text
experiments/prime_matrix_cycle_debt_k13_k14_survivor_rigidity_router.py
docs/monograph/prime-matrix-cycle-debt-k13-k14-survivor-rigidity-router.md
docs/monograph/prime-matrix-cycle-debt-k13-k14-survivor-rigidity-router.json
data/prime-matrix-cycle-debt-k13-k14-survivor-rigidity-ledger.json
```

本证书继续下钻 `K=13,14` 两个 survivor。此前 Hall router 给出一份贪心 assignment；本步改用 exact min-cost matching，抽取所有 zero-slack Hall cut，并把 tight cut 的强制合数槽转成横向 CRT 阻断模数。

```text
survivor_shifts=[13,14]
k13_zero_slack_thresholds=[1,4,7,8]
k14_zero_slack_thresholds=[7,8,13,15]
k13_minimum_replacement_count=20
k14_minimum_replacement_count=19
k13_minimum_immediate_relief_rows=6
k14_minimum_immediate_relief_rows=6
k13_minimum_overstretch_units=61
k14_minimum_overstretch_units=65
all_tight_layers_have_transverse_lcm_exceeding_period=true
k13_same_support_prime_obstacles=27
k14_same_support_prime_obstacles=28
survivor_island_has_adjacent_hall_failures=true
```

核心结构不是局部个例，而是一个两点 survivor island：

- `K=13` 的零 slack 阈值为 `1,4,7,8`。特别是 `t=1` 层使全部 27 个正容量候选行都不可丢失；`t=8` 层强制 4 个高层候选支撑 4 个高需求行。
- `K=14` 的零 slack 阈值为 `7,8,13,15`。`t=15` 与 `t=13` 层把最高两层需求压成强制 shell，`t=7` 层还强制引入 immediate-relief residue `70`。
- 相邻 `K=12` 与 `K=15` 均 Hall 失败，因此 `K=13,14` 不是可连续滑动的 replacement family。
- 即便优化匹配，`K=13/14` 仍至少需要 `20/19` 个行替换、至少 `6/6` 个 immediate-relief 行，并分别产生至少 `61/65` 个超出原 debt 的支撑单元。
- 每个 tight Hall 层的强制合数槽都有横向 CRT lcm 超过本地周期 `5680`，所以短周期内不能作为自由容量被吸收。

最新最窄剩余接口为：

```text
K13K14TightHallCRTIslandPDECOrMovingSupportSAE
```

本步关闭的是“`K=13,14` survivor 只是普通支撑替换自由度”的解释。全局行/列命题仍未无条件闭合；下一步必须排斥该 tight-Hall CRT island 的 PDEC，或证明它进入可求和的 moving-support SAE。

## 73. cycle-debt shell phase graph 回接

后续文件

```text
experiments/prime_matrix_cycle_debt_shell_phase_graph_router.py
docs/monograph/prime-matrix-cycle-debt-shell-phase-graph-router.md
docs/monograph/prime-matrix-cycle-debt-shell-phase-graph-router.json
data/prime-matrix-cycle-debt-shell-phase-graph-ledger.json
```

本证书继续把 `K=13,14` 的 tight-Hall 岛拆成 forced shell 内的 bipartite phase graph。每个 shell 的供给 residue 到需求 residue 的边，必须同时满足容量阈值与 shell 平衡；若剩余支撑运动只是一个普通 residue 平移，则所有 forced shell 应存在公共单一相位差。

```text
k13_forced_shell_matching_product=252829237248000
k14_forced_shell_matching_product=2
k13_forced_edge_count=1
k14_forced_edge_count=3
k13_single_translation_support_possible=false
k14_single_translation_support_possible=false
all_survivors_close_single_translation_support=true
k13_core_min_distinct_delta_lower_bound=7
k14_core_min_distinct_delta_lower_bound=4
```

具体结构：

- `K=14` 的高层 forced shell 乘积只有 `2` 个匹配，且三条边强制出现：`13 -> 67 (delta 54)`、`19 -> 23 (delta 4)`、`70 -> 15 (delta 16)`。这些强制相位已互不相同，所以单一平移支撑运动不可能。
- `K=14` 剩余的 `8..12` shell 只有两种匹配；最少也要形成 `4` 个不同相位差。
- `K=13` 的 forced edge 为 `31 -> 15 (delta 55)`；仅枚举 `>=8`、`7..7`、`4..6` 三个刚性核心 shell，就至少需要 `7` 个不同相位差。低层 `1..3` shell 匹配数巨大，但加入它只会保持或增加相位差数，不会降低该下界。
- 因此，两个 survivor 都不能解释为同一 CRT 周期中的普通单平移支撑运动；若反例链继续保留这些 shell，必须进入非仿射、多相位的支撑重物化。

最新最窄剩余接口为：

```text
NonAffineShellPhaseFragmentPDECOrMultiDeltaSupportSAE
```

本步关闭的是“tight-Hall 岛可由单一平移 support motion 吸收”的解释。全局行/列命题仍未无条件闭合；下一步要攻击的是多相位碎裂本身是否可求和，或是否强制产生新的 PDEC/ColumnCRT。

## 74. cycle-debt multi-delta core CRT load 回接

后续文件

```text
experiments/prime_matrix_cycle_debt_multi_delta_core_crt_load_router.py
docs/monograph/prime-matrix-cycle-debt-multi-delta-core-crt-load-router.md
docs/monograph/prime-matrix-cycle-debt-multi-delta-core-crt-load-router.json
data/prime-matrix-cycle-debt-multi-delta-core-crt-load-ledger.json
```

本证书继续把 multi-delta support SAE 的核心匹配展开成实际合数槽和阻断素因子。每条 `source -> target` 边按目标 demand width 展开 source 行从对应 `K` 开始的实际 composite slots，再按 delta lane 汇总 CRT lcm。

```text
period_p=5680
k13_enumerated_core_matching_count=96
k13_minimum_delta_count=7
k13_minimum_delta_matching_count=2
k13_best_min_delta_global_lcm_log10=36.165
k13_excluded_large_shell_labels=['1..3']
k14_enumerated_core_matching_count=2
k14_minimum_delta_count=4
k14_minimum_delta_matching_count=1
k14_best_min_delta_global_lcm_log10=31.716
all_min_delta_lcms_exceed_period=true
```

核心读数：

- `K=14` 的最小多相位核心唯一，4 个 delta lane 分别为 `4,16,28,54`，总需求宽度 `52`，全局 CRT lcm 约为 `10^31.716`。
- `K=13` 的可枚举刚性核心有 `96` 个匹配，其中只有 `2` 个达到最少 `7` 个 delta；最优全局 CRT lcm 约为 `10^36.165`，核心需求宽度为 `71`。
- `K=13` 的低层 `1..3` shell 尚未作为闭合证明使用；它匹配数巨大、可产生全 residue delta，因此被保留为独立的 full-residue SAE/PDEC 出口。

最新最窄剩余接口为：

```text
MultiDeltaCoreCRTLoadPDECOrLowShellFullResidueSAE
```

本步关闭的是“多相位碎裂只是轻量局部相位噪声”的解释。剩余要么排斥这个重 CRT 核心载荷形成的 PDEC，要么把 `K=13` 低层 full-residue shell 作为可求和 SAE 处理。

## 75. cycle-debt low-shell delta skeleton 回接

后续文件

```text
experiments/prime_matrix_cycle_debt_low_shell_delta_skeleton_router.py
docs/monograph/prime-matrix-cycle-debt-low-shell-delta-skeleton-router.md
docs/monograph/prime-matrix-cycle-debt-low-shell-delta-skeleton-router.json
data/prime-matrix-cycle-debt-low-shell-delta-skeleton-ledger.json
```

本证书继续攻击 `K=13` 的低层 `1..3` shell。上一层保留了 low-shell full-residue SAE，因为该 shell 的 possible delta 覆盖 `0..70` 全部 residue；本步用整数规划精确求最小 delta 骨架，并把低层补齐后的 `K=13` 全需求载荷重新汇总。

```text
low_shell_possible_delta_count=71
low_shell_minimum_delta_count=6
low_shell_minimum_delta_witness=[23,35,38,58,68,70]
core_delta_count_before_low_shell=7
low_shell_new_delta_count_over_core=2
low_shell_new_deltas_over_core=[0,66]
full_k13_delta_count_after_low_shell=9
full_k13_total_required_width=101
full_k13_global_lcm_log10=42.095
full_k13_lcm_exceeds_period=true
```

因此，低层并不需要真的扩散成 `71` 个 delta；但它也不是自由出口。相对已有 `K=13` 刚性核心的 `7` 个 delta，低层只新增 `0` 与 `66` 两条 lane，最终形成：

- `9` 个 delta lane；
- 全部 `101` 个 demand width；
- `25` 个不同阻断素因子；
- 全局 CRT lcm 约 `10^42.095`，远超本地周期 `5680`。

最新最窄剩余接口为：

```text
K13FullDebtNineLaneCRTLoadPDECOrResidualSlackTailSAE
```

本步关闭的是“`K=13` 低层必须作为 full-residue SAE 逃逸”的解释。剩余变为九 lane 全债务 CRT-load PDEC，或尚未完全命名的 residual slack-tail SAE。

## 76. cycle-debt K13 full-debt nine-lane tail 回接

后续文件

```text
experiments/prime_matrix_cycle_debt_k13_full_debt_nine_lane_tail_router.py
docs/monograph/prime-matrix-cycle-debt-k13-full-debt-nine-lane-tail-router.md
docs/monograph/prime-matrix-cycle-debt-k13-full-debt-nine-lane-tail-router.json
data/prime-matrix-cycle-debt-k13-full-debt-nine-lane-tail-ledger.json
```

本证书继续攻击 `K13FullDebtNineLaneCRTLoadPDECOrResidualSlackTailSAE`。关键转折是把 residual slack-tail 从“可能是匹配选择造成的剩余尾巴”改写成 K=13 层 Hall 账本不变量。

```text
capacity_row_count=27
demand_row_count=27
all_capacity_rows_mandatory=true
total_capacity=119
total_demand_width=101
unavoidable_tail_slot_count=18
zero_slack_layers=[1,4,7,8]
allowed_deltas=[0,8,22,39,54,55,58,59,66]
allowed_edge_count=71
min_tail_factor_count=8
min_tail_lcm_log10=11.488
min_tail_lcm_exceeds_period=true
```

结构读数：

- 第 1 层 Hall slack 为 `0`，因此所有 27 个正容量行都必须被任意 full-debt 匹配使用。
- `119-101=18`，且 `sum layer_slack=18`，所以 residual tail 的 18 个槽不是当前匹配见证的伪影。
- 零 slack 层 `1,4,7,8` 是移动槽的刚性门；这些层若损失一行容量，Hall 条件立即失败，除非同时产生新的 arrival/PDEC。
- 在固定九 lane 的所有可行匹配中，MILP 优化后 tail 仍至少激活 8 个阻断素因子，最小 tail lcm 约 `10^11.488`，已经超过本地周期 `5680`。

最新最窄剩余接口为：

```text
K13LayerSlackTailCRTInvariantPDECOrMovingFamilySAE
```

本步关闭的是“residual slack-tail 只是匹配 artifact”的解释。剩余变成层不变量 tail-CRT PDEC，或真正随 P 漂移的 moving-family SAE。

## 77. cycle-debt K13 tail gate drift 回接

后续文件

```text
experiments/prime_matrix_cycle_debt_k13_tail_gate_drift_router.py
docs/monograph/prime-matrix-cycle-debt-k13-tail-gate-drift-router.md
docs/monograph/prime-matrix-cycle-debt-k13-tail-gate-drift-router.json
data/prime-matrix-cycle-debt-k13-tail-gate-drift-ledger.json
```

本证书继续攻击 `K13LayerSlackTailCRTInvariantPDECOrMovingFamilySAE`。它不再问 K=13 tail 本身有多重，而是问这个层门形状能否在 near-shift 窗口中无漂移复现。

```text
hall_pass_shifts=[13,14]
same_slack_vector_shifts=[13]
same_zero_gate_set_shifts=[13]
passing_same_slack_vector_shifts=[13]
k13_tail_balance=18
k13_zero_slack_layers=[1,4,7,8]
k14_tail_balance=31
k14_tail_increase_over_k13=13
k14_zero_slack_layers=[7,8,13,15]
k14_slack_l1_distance_from_k13=19
k14_zero_gate_lost_from_k13=[1,4]
k14_zero_gate_gained_over_k13=[13,15]
```

结构读数：

- 在 `K=1..16` 的 near-shift 窗口内，K=13 的完整 slack 向量只在 `K=13` 自身复现。
- 通过 Hall 的相位只有 `K=13,14`；因此若要在 near-shift 中移动，唯一去向是 `K=14`。
- `K=14` 不是 K=13 tail 的同形复本：低门 `1,4` 消失，高门 `13,15` 出现，tail balance 增加 `13`。
- 所以 K=13 layer-tail 无法近程无漂移重播；移动分支必须改名为 K14 high-gate drift SAE/PDEC。

最新最窄剩余接口为：

```text
K13GateProfileNoNearReplayPDECOrK14HighGateDriftSAE
```

本步关闭的是“K=13 层不变量 tail 可以在 near-shift 内保持同形移动”的解释。剩余变成固定 K13 gate-profile PDEC，或 K14 高门漂移族的 SAE/PDEC。

## 78. cycle-debt K14 high-gate low-shell skeleton 回接

后续文件

```text
experiments/prime_matrix_cycle_debt_k14_high_gate_low_shell_skeleton_router.py
docs/monograph/prime-matrix-cycle-debt-k14-high-gate-low-shell-skeleton-router.md
docs/monograph/prime-matrix-cycle-debt-k14-high-gate-low-shell-skeleton-router.json
data/prime-matrix-cycle-debt-k14-high-gate-low-shell-skeleton-ledger.json
```

本证书继续攻击 `K13GateProfileNoNearReplayPDECOrK14HighGateDriftSAE` 中的 K14 moving 分支。K14 的高门漂移不是一个未登记自由 SAE；高门 tight shell 只产生两个 core 匹配，低层剩余可以继续用 delta skeleton 精确压缩。

```text
k14_zero_slack_layers=[7,8,13,15]
k14_high_gate_core_alternative_count=2
k14_best_core_deltas=[4,16,28,54]
k14_low_shell_minimum_delta_count=6
k14_low_shell_new_delta_count_over_core=4
k14_low_shell_new_deltas_over_core=[2,48,58,70]
k14_full_delta_count_after_low_shell=8
k14_full_deltas_after_low_shell=[2,4,16,28,48,54,58,70]
k14_full_total_required_width=101
k14_full_global_lcm_log10=48.508
k14_full_used_tail_slots=28
k14_tail_lcm_log10=17.956
```

结构读数：

- K14 high-core 的两个候选分别来自 `8..12` shell 的两个二分匹配。
- 选择 lane 数最小的 core 后，低层补齐单独最少 `6` 个 delta；相对 core 只需新增 `2,48,58,70`。
- 补齐后 K14 全部 `101` demand width 落在 `8` 条 lane 上，整体 CRT lcm 约 `10^48.508`，远超本地周期 `5680`。
- 因此 K14 high-gate drift 分支返回 full-debt CRT-load PDEC，而不是保留未命名 moving SAE。

最新最窄剩余接口为：

```text
K13FixedGateProfilePDECOrK14FullDebtEightLaneCRTLoadPDEC
```

本步关闭的是“K14 高门漂移可以作为未登记自由族继续逃逸”的解释。剩余变成固定 K13 gate-profile PDEC，或 K14 全债务八 lane CRT-load PDEC。

## 79. cycle-debt two-survivor terminal CRT bifurcation 回接

后续文件

```text
experiments/prime_matrix_cycle_debt_two_survivor_terminal_crt_bifurcation_router.py
docs/monograph/prime-matrix-cycle-debt-two-survivor-terminal-crt-bifurcation-router.md
docs/monograph/prime-matrix-cycle-debt-two-survivor-terminal-crt-bifurcation-router.json
data/prime-matrix-cycle-debt-two-survivor-terminal-crt-bifurcation-ledger.json
```

本证书把 K13 与 K14 两个 survivor 终端分支放到同一 CRT 账本中比较。两者都覆盖同一 `27` 个 target 需求，但实际支撑运动并不是同一个图样的小扰动。

```text
k13_delta_count=9
k14_delta_count=8
common_deltas=[54,58]
delta_union_count=15
delta_symmetric_difference_count=13
source_intersection_count=19
source_symmetric_difference_count=16
target_intersection_count=27
pair_intersection_count=1
pair_intersection=[13->67]
k13_lcm_log10=42.095
k14_lcm_log10=48.508
union_factor_count=32
union_lcm_log10=57.156
tail_union_lcm_log10=24.632
```

结构读数：

- target 需求完全相同，但 source 支撑只重合 `19` 行，source 对称差为 `16`。
- 实际匹配边只重合 `13->67` 一条，说明 K13/K14 不是同一支撑图样的局部相位移动。
- lane 交集只有 `54,58`，其余 `13` 条 lane 位于对称差。
- 两分支联合 CRT lcm 约 `10^57.156`，tail 因子联合 lcm 约 `10^24.632`，均远超本地周期 `5680`。

最新最窄剩余接口为：

```text
TwoSurvivorTerminalCRTBifurcationPDECExclusion
```

本步关闭的是“K13/K14 两个终端 survivor 可以互相吸收为同一未命名 SAE”的解释。剩余变成明确的 two-survivor terminal CRT bifurcation PDEC 排斥问题。

## 80. cycle-debt two-survivor PDEC exclusion 回接

后续文件

```text
experiments/prime_matrix_cycle_debt_two_survivor_pdec_exclusion_router.py
docs/monograph/prime-matrix-cycle-debt-two-survivor-pdec-exclusion-router.md
docs/monograph/prime-matrix-cycle-debt-two-survivor-pdec-exclusion-router.json
data/prime-matrix-cycle-debt-two-survivor-pdec-exclusion-ledger.json
```

本证书继续攻击 `TwoSurvivorTerminalCRTBifurcationPDECExclusion`。它不再只登记 K13/K14 终端分支不同，而是把终端切换必须支付的容量和相位代价逐项量化。

```text
common_pair_count=1
common_pair_width=15
forced_rematched_target_count=26
forced_rematched_target_width=86
minimum_branch_exclusive_delta_width=70
minimum_branch_exclusive_delta_lcm_log10=32.582
k14_only_assigned_width=29
k14_only_capacity_at_k13=0
k14_only_capacity_at_k14=39
k14_arrival_lcm_log10=20.205
k13_same_support_capacity_deficit_at_k14=8
common_source_changed_count=18
```

结构读数：

- 唯一共同实际边 `13->67` 只承载 target `67` 的宽度 `15`，其余 `26` 个 target 合计宽度 `86` 必须重路由。
- 共同 delta `54,58` 不能吸收全部重路由；每个分支仍至少有 `70` 宽度落在 branch-exclusive delta 上。
- 若从 K13 切到 K14，K14 必须调用 `8` 个在 K13 时容量为 `0` 的新 source；这些 fresh-arrival source 到 K14 才出现 `39` 容量并实际承载 `29` 宽度。
- K13 原支撑若直接拖到 K14，只剩 `93` 容量，距离 `101` 需求有 `8` 宽度缺口，正好对应 K13-only source 的容量流失。

最新最窄剩余接口为：

```text
TerminalSwitchArrivalColumnCRTPDECOrBranchExclusiveCRTLoadExclusion
```

本步关闭的是“two-survivor PDEC 可以由共同 anchor/共同 delta 局部吸收”的解释。全局行/列命题仍未无条件闭合；下一步必须排斥 terminal switch-arrival ColumnCRT/PDEC，或排斥 branch-exclusive CRT-load 的持久复现。

## 81. cycle-debt terminal switch arrival wall 回接

后续文件

```text
experiments/prime_matrix_cycle_debt_terminal_switch_arrival_wall_router.py
docs/monograph/prime-matrix-cycle-debt-terminal-switch-arrival-wall-router.md
docs/monograph/prime-matrix-cycle-debt-terminal-switch-arrival-wall-router.json
data/prime-matrix-cycle-debt-terminal-switch-arrival-wall-ledger.json
```

本证书继续攻击 `TerminalSwitchArrivalColumnCRTPDECOrBranchExclusiveCRTLoadExclusion` 中的 terminal switch-arrival 分支。核心结论是：K14 的 fresh-arrival 容量不是平滑打开，而是越过一个同步入口素数墙后才出现。

```text
arrival_source_count=8
all_arrival_sources_zero_capacity_at_k13=true
all_entry_wall_cycles_equal_13=true
all_entry_wall_positions_zero_at_k13=true
entry_wall_lcm_log10=39.482
postwall_capacity_total=39
postwall_assigned_width_total=29
postwall_tail_slot_total=10
postwall_assigned_lcm_log10=20.205
entry_plus_assigned_lcm_log10=59.687
entry_plus_postwall_lcm_log10=68.361
entry_plus_postwall_coprime_to_period=true
arrival_width_by_delta={2:5,16:7,28:7,48:2,54:3,58:5}
```

结构读数：

- `8` 个 K14-only source 在 K13 时容量全部为 `0`，并且全部在 `window_position=0` 撞到真实素数入口墙。
- 入口素数墙由 `8` 个互素素数构成，lcm 约 `10^39.482`，且与本地周期 `5680` 互素。
- 越过入口墙后 K14 才得到 `39` 个 post-wall 容量槽，其中 `29` 槽实际分配，tail 为 `10`。
- `entry+assigned` 联合 lcm 约 `10^59.687`；`entry+全部 post-wall` 联合 lcm 约 `10^68.361`，说明持久复现不是本地周期微调。

最新最窄剩余接口为：

```text
EightPrimeEntryWallPostWallCRTExclusionOrBranchExclusiveCRTLoadExclusion
```

本步关闭的是“fresh-arrival 是匿名平滑容量”的解释。全局行/列命题仍未无条件闭合；下一步必须排斥八素数入口墙加 post-wall CRT-load 的持久复现，或排斥 branch-exclusive CRT-load。

## 82. cycle-debt coupled branch entry-wall 回接

后续文件

```text
experiments/prime_matrix_cycle_debt_coupled_branch_entry_wall_router.py
docs/monograph/prime-matrix-cycle-debt-coupled-branch-entry-wall-router.md
docs/monograph/prime-matrix-cycle-debt-coupled-branch-entry-wall-router.json
data/prime-matrix-cycle-debt-coupled-branch-entry-wall-ledger.json
```

本证书继续攻击 `EightPrimeEntryWallPostWallCRTExclusionOrBranchExclusiveCRTLoadExclusion`。它把 K14 的 entry-wall/post-wall 与 branch-exclusive 载荷放回同一个终端分支中，而不是保留成两个松散并列出口。

```text
k13_branch_exclusive_width=73
k13_branch_exclusive_lcm_log10=36.678
k14_branch_exclusive_width=70
k14_arrival_assigned_width=29
k14_arrival_branch_overlap_width=21
k14_branch_arrival_union_width=78
k14_branch_plus_entry_lcm_log10=72.064
k14_branch_plus_entry_plus_assigned_lcm_log10=76.351
k14_branch_plus_entry_plus_postwall_lcm_log10=85.024
both_branches_plus_k14_entry_postwall_lcm_log10=99.349
entry_wall_disjoint_from_branch_and_postwall=true
all_coupled_lcms_coprime_to_period=true
```

结构读数：

- 若终端走 K14，`70` 宽度 branch-exclusive 载荷与 `29` 宽度 arrival 载荷有 `21` 宽度重叠，但联合仍强制 `78` 宽度 actual load。
- K14 的 entry-wall 因子与 branch/post-wall 因子不相交；耦合后 `branch+entry+全部 post-wall` 的 lcm 约 `10^85.024`。
- 若终端走 K13，则剩余是 `73` 宽度 K13 branch-exclusive CRT-load，lcm 约 `10^36.678`。
- 若把 K13/K14 branch-exclusive 与 K14 entry/post-wall 全部合并，联合 lcm 约 `10^99.349`，仍与本地周期 `5680` 互素。

最新最窄剩余接口为：

```text
K13BranchExclusiveCRTLoadExclusionOrK14CoupledEntryBranchCRTWallExclusion
```

本步关闭的是“entry-wall 与 branch-exclusive 是两个无关松散出口”的解释。全局行/列命题仍未无条件闭合；下一步必须分别排斥 K13 branch-exclusive 持久载荷，或 K14 coupled entry-branch CRT wall。

## 83. cycle-debt branch replay support-gap 回接

后续文件

```text
experiments/prime_matrix_cycle_debt_branch_replay_support_gap_router.py
docs/monograph/prime-matrix-cycle-debt-branch-replay-support-gap-router.md
docs/monograph/prime-matrix-cycle-debt-branch-replay-support-gap-router.json
data/prime-matrix-cycle-debt-branch-replay-support-gap-ledger.json
```

本证书继续攻击 `K13BranchExclusiveCRTLoadExclusionOrK14CoupledEntryBranchCRTWallExclusion`。它把“高因子吸收槽能否随本地 support motion 平滑移动并复现”写成周期坐标中的 replay lemma：若同一阻断素因子包在平移 `T` 个本地周期后复现，则每个阻断因子 `q` 都给出 `T=0 mod q`，所以非零复现周期至少是该包的 CRT lcm。

```text
period_p=5680
near_shift_limit_cycles=16
k13_branch_exclusive_width=73
k14_branch_arrival_union_width=78
k14_coupled_audit_slot_count_all_postwall=117
smallest_log10_margin_over_support_width=30.737
smallest_log10_margin_over_audit_slots=30.737
all_blocks_coprime_to_period=true
all_nonzero_replay_moduli_exceed_support_width=true
all_nonzero_replay_moduli_exceed_audit_slots=true
local_moving_slot_replay_excluded_for_registered_blocks=true
far_replay_still_requires_columncrt_pdec=true
```

结构读数：

- K13 branch-exclusive 的复现模数约 `10^36.678`，比 `73` 宽度支撑大约 `10^34.814` 倍。
- K14 `branch+entry+postwall` 的复现模数约 `10^85.024`，比 `78` 宽度 actual 支撑大约 `10^83.132` 倍，也远超 `117` 个审计槽。
- 因此当前登记的高因子吸收槽不能通过本地 moving-slot 运动复现；一旦移动，必须换成新的阻断包并回流 `ColumnCRT/PDEC/SAE`。

最新最窄剩余接口为：

```text
BranchReplayColumnCRTPDECExclusionOrIsolatedTerminalAtomAbsorption
```

本步关闭的是“终端载荷可由本地 moving-slot 平滑复现”的解释。全局行/列命题仍未无条件闭合；下一步必须排斥远程 branch replay ColumnCRT/PDEC，或证明所有剩余只是可吸收的孤立有限原子。

## 84. cycle-debt branch replay global dichotomy 回接

后续文件

```text
experiments/prime_matrix_cycle_debt_branch_replay_global_dichotomy_router.py
docs/monograph/prime-matrix-cycle-debt-branch-replay-global-dichotomy-router.md
docs/monograph/prime-matrix-cycle-debt-branch-replay-global-dichotomy-router.json
data/prime-matrix-cycle-debt-branch-replay-global-dichotomy-ledger.json
```

本证书继续攻击 `BranchReplayColumnCRTPDECExclusionOrIsolatedTerminalAtomAbsorption`。它把上一证书中的“孤立有限原子”从全局结构出口中剥离：登记的终端 replay block 只有有限个；若某个登记 block 在全局反例链中无限复现，则周期坐标 replay 立即提升为 `P` 坐标中的固定 ColumnCRT 类。

```text
registered_replay_block_count=6
minimum_cycle_replay_modulus_log10=32.582
minimum_p_space_columncrt_modulus_log10=36.337
maximum_p_space_columncrt_modulus_log10=103.103
persistent_registered_replay_routes_to_columncrt_pdec=true
isolated_atoms_cannot_form_infinite_registered_family=true
finite_atom_base_check_required=true
```

结构读数：

- 无限复现的登记终端包必须落入 `period_p*lcm(B)` 的 P-space ColumnCRT 类；最小 P-space 模数已约 `10^36.337`。
- 若没有任何登记包无限复现，则登记原子只剩有限项，不能作为全局反例链的结构逃逸。
- 若阻断包改变，则不属于同一 replay block，回流 `PDEC/SAE` 或新的命名 router。

最新最窄剩余接口为：

```text
BranchReplayColumnCRTPDECExclusionOrFiniteAtomBaseCheck
```

本步不排斥远程 ColumnCRT/PDEC，也不替代有限基例检查；它关闭的是“孤立原子可支撑全局反例链”的解释。

## 85. cycle-debt finite atom boundary bridge 回接

后续文件

```text
experiments/prime_matrix_cycle_debt_finite_atom_boundary_bridge_router.py
docs/monograph/prime-matrix-cycle-debt-finite-atom-boundary-bridge-router.md
docs/monograph/prime-matrix-cycle-debt-finite-atom-boundary-bridge-router.json
data/prime-matrix-cycle-debt-finite-atom-boundary-bridge-ledger.json
```

本证书继续攻击 `BranchReplayColumnCRTPDECExclusionOrFiniteAtomBaseCheck`。它把有限原子基例检查与仓库中已有的有限桥分段对齐，避免把 `P<=5000` 的直接方阵验证误用到当前 cycle-debt 终端原子上。

```text
direct_grid_verified_max_p=5000
dynamic_finite_bridge_range=[3001,99991]
dynamic_finite_bridge_closed=true
cover_pressure_atom_count=155
cover_pressure_all_atoms_in_dynamic_finite_bridge=true
arrival_wall_atom_count=55
arrival_wall_tail_atom_count=31
total_post100000_tail_atom_count=31
tail_atom_p_range=[101087,134047]
finite_atom_base_check_fully_closed=false
```

结构读数：

- cycle-debt cover pressure 的 `155` 个 P 坐标全落在已关闭的 `3001<=P<100000` 动态有限桥内。
- terminal arrival/post-wall 的 `55` 个坐标中，`24` 个在动态有限桥内，`31` 个进入 `P>=100000` 尾段。
- 尾段原子由 `15` 个 assigned slot、`8` 个 postwall first prime、`8` 个 tail slot 构成，范围为 `101087..134047`。

最新最窄剩余接口为：

```text
BranchReplayColumnCRTPDECExclusionOrPost100000TailAtomRunner
```

本步关闭的是“当前有限原子可被旧 P<=5000 直接验证整体吸收”的误解，并吸收了 `P<100000` 前缀原子；全局行/列命题仍未无条件闭合。

## 86. cycle-debt post-100000 tail atom exact runner 回接

后续文件

```text
experiments/prime_matrix_cycle_debt_post100000_tail_atom_exact_runner.py
docs/monograph/prime-matrix-cycle-debt-post100000-tail-atom-exact-runner.md
docs/monograph/prime-matrix-cycle-debt-post100000-tail-atom-exact-runner.json
data/prime-matrix-cycle-debt-post100000-tail-atom-exact-ledger.json
```

本证书继续攻击 `BranchReplayColumnCRTPDECExclusionOrPost100000TailAtomRunner`。它对上一层剩余的 `31` 个 post-100000 tail atoms 做逐点精确审计：合数槽验证记录小因子，first-prime 槽验证素性，并检查每个 arrival row 的 first prime 之前槽位全为合数。

```text
tail_atom_count=31
tail_atom_p_range=[101087,134047]
kind_counts={'assigned_slot': 15, 'postwall_first_prime': 8, 'tail_slot': 8}
composite_atom_count=23
postwall_first_prime_count=8
all_composite_atoms_divisible_by_recorded_factor=true
all_composite_recorded_factors_are_smallest=true
all_postwall_first_primes_verified=true
all_preprime_slots_composite_in_arrival_rows=true
finite_atom_branch_closed_for_registered_atoms=true
```

结构读数：

- `23` 个 post-100000 合数槽全部由记录因子整除，且记录因子均为最小因子。
- `8` 个 post-wall first prime 全部经独立素性检查确认。
- 八个 arrival row 的 first-prime 边界均精确闭合，有限尾段原子不再作为并列出口。

最新最窄剩余接口为：

```text
BranchReplayColumnCRTPDECExclusion
```

本步只关闭当前登记有限原子分支，不排斥全局持久 ColumnCRT/PDEC；全局行/列命题仍未无条件闭合。

## 87. cycle-debt branch replay fresh-modulus escalation 回接

后续文件

```text
experiments/prime_matrix_cycle_debt_branch_replay_fresh_modulus_escalation_router.py
docs/monograph/prime-matrix-cycle-debt-branch-replay-fresh-modulus-escalation-router.md
docs/monograph/prime-matrix-cycle-debt-branch-replay-fresh-modulus-escalation-router.json
data/prime-matrix-cycle-debt-branch-replay-fresh-modulus-escalation-ledger.json
```

本证书继续攻击 `BranchReplayColumnCRTPDECExclusion`。在有限原子分支关闭后，它把“固定有限 ColumnCRT replay 类是否可以作为终端稳定结构”形式化为 fresh-modulus escalation：任意登记 replay block 的模数都是有限的；当未登记新素数层进入后续筛层时，该新素数与旧模数互素，给出新的 CRT 坐标。

```text
finite_atom_branch_closed_for_registered_atoms=true
registered_replay_block_count=6
fresh_prime_sample_count_per_block=8
all_registered_blocks_have_coprime_fresh_layers=true
minimum_first_fresh_log10_gain=2.400
minimum_sample_log10_gain=19.435
finite_crt_terminal_description_excluded=true
persistent_family_requires_unbounded_modulus_or_pdec=true
```

结构读数：

- 任一登记 replay block 仍只是有限 CRT 类；它不能控制后续无限素数层。
- 对每个 block 加入首个 fresh prime，模数至少增加 `10^2.400`；加入 8 个 fresh prime 样本，至少增加 `10^19.435`。
- 因此无限反例链不能在固定有限模数上稳定；它必须不断扩模、触发 PDEC/ColumnCRT 缺陷，或进入尾段筛稳定矛盾。

最新最窄剩余接口为：

```text
UnboundedFreshModulusEscalationPDECOrTailSieveStabilityContradiction
```

本步不宣称行/列命题闭合；它把最后固定 ColumnCRT 类排斥推进到无界 fresh-modulus escalation 与尾段筛稳定矛盾。

## 88. cycle-debt fresh-modulus 到 tail-sieve 桥接回接

后续文件

```text
experiments/prime_matrix_cycle_debt_fresh_modulus_tail_sieve_bridge_router.py
docs/monograph/prime-matrix-cycle-debt-fresh-modulus-tail-sieve-bridge-router.md
docs/monograph/prime-matrix-cycle-debt-fresh-modulus-tail-sieve-bridge-router.json
data/prime-matrix-cycle-debt-fresh-modulus-tail-sieve-bridge-ledger.json
```

本证书直接承接最新接口：

```text
UnboundedFreshModulusEscalationPDECOrTailSieveStabilityContradiction
```

固定有限 ColumnCRT 终端已经被排除后，持久 branch replay 若不在 fresh layer 触发 PDEC/ColumnCRT，则每个新素数层都只能作为一个禁相位进入 CRT 周期。对无界多个 fresh primes 重复该过程，得到的正是尾段对象：

```text
S(P)=#{1<=k<P: k avoids one prescribed residue class modulo every prime q<=P^0.43}.
```

当前读数：

```text
fresh_modulus_escalation_registered=true
finite_columncrt_terminal_excluded=true
non_pdec_unbounded_fresh_layers_force_tail_rough_object=true
tail_object_interface_closed=true
conditional_external_tail_sieve_closed=true
strict_self_contained_tail_sieve_closed=false
fresh_layer_pdec_excluded=false
row_column_unconditional_closed=false
```

结构判定：

- 无界扩模不能再停留为抽象出口；若无 fresh-layer PDEC，它必须进入避单余类尾段粗筛对象。
- 该对象已与 B3 lower-sieve 账本同口径，`P=100000` 处模型主项约 `4896.256004`，10% 主项仍比 `401` 多 `88.625600`。
- 接受外部显式 Mertens/Dusart 或标准 beta-sieve 输入时，tail-sieve stability 分支条件关闭。
- 严格自足路线仍剩 `SelfContainedDusartReciprocalPrimeProofAppendixXGe10372`，且 fresh-layer PDEC/ColumnCRT 仍需排斥。

最新最窄剩余接口为：

```text
FreshLayerPDECColumnCRTExclusionOrSelfContainedTailSieveStabilityClosure
```

本步仍不宣称行/列命题闭合；它把无界新素数层扩模出口压成 tail-sieve/PDEC 双出口。

## 89. cycle-debt fresh-modulus tail-sieve strict 自足同步回接

后续文件

```text
experiments/prime_matrix_cycle_debt_fresh_modulus_tail_self_contained_sync_router.py
docs/monograph/prime-matrix-cycle-debt-fresh-modulus-tail-self-contained-sync-router.md
docs/monograph/prime-matrix-cycle-debt-fresh-modulus-tail-self-contained-sync-router.json
data/prime-matrix-cycle-debt-fresh-modulus-tail-self-contained-sync-ledger.json
```

上一节把无界 fresh-modulus 分支压成：

```text
FreshLayerPDECColumnCRTExclusionOrSelfContainedTailSieveStabilityClosure
```

其中 strict tail-sieve 出口仍登记为旧粗原子 `SelfContainedDusartReciprocalPrimeProofAppendixXGe10372`。后续 strict 速率尾段同步证书已经将该粗原子展开并关闭；终端预算同步也确认 B3-TV 自足同步完成。因此在 branch-replay 子分支内，tail-sieve stability 出口可从剩余基移除。

当前读数：

```text
previous_tail_object_interface_closed=true
previous_non_pdec_unbounded_fresh_layers_force_tail_rough_object=true
previous_conditional_external_tail_sieve_closed=true
previous_strict_tail_sieve_closed=false
strict_self_contained_mertens_tail_proved_latest=true
b3_tv_strict_self_contained_synchronized_latest=true
strict_self_contained_tail_sieve_closed_for_branch_replay=true
fresh_layer_pdec_excluded=false
row_column_unconditional_closed=false
```

branch-replay strict 剩余基由

```text
FreshLayerPDECColumnCRTExclusion AND SelfContainedDusartReciprocalPrimeProofAppendixXGe10372
```

收缩为

```text
FreshLayerPDECColumnCRTExclusion
```

这一步仍不宣称行/列命题闭合；它只把 tail-sieve stability 出口从 branch-replay 子分支中移除，下一步必须直接排斥 fresh-layer PDEC/ColumnCRT。

## 90. cycle-debt fresh-layer 本地投影碰撞回接

后续文件

```text
experiments/prime_matrix_cycle_debt_fresh_layer_local_collision_router.py
docs/monograph/prime-matrix-cycle-debt-fresh-layer-local-collision-router.md
docs/monograph/prime-matrix-cycle-debt-fresh-layer-local-collision-router.json
data/prime-matrix-cycle-debt-fresh-layer-local-collision-ledger.json
```

本证书继续攻击

```text
FreshLayerPDECColumnCRTExclusion
```

并排除其中的本地投影碰撞子类。设本地周期步长为 `M=5680`，fresh prime 为 `ell`。若 `gcd(M,ell)=1` 且局部窗口长度 `W<ell`，则 `j -> a+jM mod ell` 在该窗口内单射，因此同一 registered support 内不能产生 fresh-layer 投影碰撞。

当前读数：

```text
registered_block_count=6
all_sample_fresh_primes_coprime_to_period_p=true
all_first_fresh_primes_exceed_support_width=true
all_first_fresh_primes_exceed_audit_slots=true
all_registered_samples_injective_on_local_windows=true
minimum_first_fresh_minus_support_width=178
minimum_first_fresh_minus_audit_slots=178
local_fresh_layer_projection_collision_excluded=true
fresh_layer_pdec_fully_excluded=false
row_column_unconditional_closed=false
```

因此 branch-replay 最新剩余接口收缩为：

```text
FreshLayerSupportMotionEscapeOrRemoteColumnCRTPDECExclusion
```

这一步仍不宣称行/列命题闭合；它只说明 fresh-layer PDEC 若持续，不能是 registered primitive support 内的本地相位碰撞，必须是支撑运动逃逸、远程 P-space ColumnCRT/PDEC 或未登记 moving family。

## 91. cycle-debt fresh support-motion 全局路由回接

后续文件

```text
experiments/prime_matrix_cycle_debt_fresh_support_motion_global_router.py
docs/monograph/prime-matrix-cycle-debt-fresh-support-motion-global-router.md
docs/monograph/prime-matrix-cycle-debt-fresh-support-motion-global-router.json
data/prime-matrix-cycle-debt-fresh-support-motion-global-ledger.json
```

上一节剩余为

```text
FreshLayerSupportMotionEscapeOrRemoteColumnCRTPDECExclusion
```

本证书同步两条已有刚性：

1. fresh-layer 本地投影碰撞已由单射引理排除；
2. 同一 registered 阻断包的本地支撑漂移已由 support-gap `lcm(B)` 屏障排除。

因此 registered support-motion escape 不再是活动出口。若 registered block 仍在全局反例链中无限复现，只能提升为固定 P-space ColumnCRT 类；若阻断包改变，则它已不是 registered support motion，而是未登记 moving family。

当前读数：

```text
registered_block_count=6
local_fresh_layer_projection_collision_excluded=true
registered_local_support_motion_excluded=true
persistent_registered_replay_routes_to_columncrt_pdec=true
isolated_registered_atoms_cannot_form_global_escape=true
registered_support_motion_escape_closed=true
minimum_cycle_log10_margin_over_support_width=30.737
minimum_p_space_columncrt_modulus_log10=36.337
remote_pspace_columncrt_excluded=false
unregistered_moving_family_excluded=false
row_column_unconditional_closed=false
```

branch-replay 最新剩余接口为：

```text
RemotePspaceColumnCRTExclusionOrUnregisteredMovingFamilyRouter
```

本步仍不宣称行/列命题闭合；它只删除 registered support-motion escape 这个本地出口。

## 92. cycle-debt remote ColumnCRT feedback 回接

后续文件

```text
experiments/prime_matrix_cycle_debt_remote_columncrt_feedback_router.py
docs/monograph/prime-matrix-cycle-debt-remote-columncrt-feedback-router.md
docs/monograph/prime-matrix-cycle-debt-remote-columncrt-feedback-router.json
data/prime-matrix-cycle-debt-remote-columncrt-feedback-ledger.json
```

上一节剩余为

```text
RemotePspaceColumnCRTExclusionOrUnregisteredMovingFamilyRouter
```

本证书把 `RemotePspaceColumnCRT` 拆成两层：裸固定远程周期类、以及在新素数层已经材料化的 PDEC/ColumnCRT。裸固定远程周期类已经回落到旧闭合链：

1. 当前登记有限原子已由 post-100000 exact runner 吸收；
2. 固定有限 CRT replay 类已由 fresh-modulus escalation 证明为非终端；
3. 若无 fresh-layer PDEC/ColumnCRT，则 non-PDEC 无界 fresh layers 已接入 B3 tail-sieve 对象并由 strict 同步关闭。

当前读数：

```text
registered_remote_block_count=6
minimum_remote_pspace_columncrt_modulus_log10=36.337
maximum_remote_pspace_columncrt_modulus_log10=103.103
minimum_first_fresh_log10_gain=2.400
minimum_sample_fresh_log10_gain=19.435
registered_finite_atoms_absorbed=true
fixed_finite_remote_crt_not_terminal=true
non_pdec_fresh_tail_sieve_closed=true
bare_remote_pspace_columncrt_terminal_closed=true
materialized_fresh_layer_pdec_columncrt_excluded=false
unregistered_moving_family_excluded=false
row_column_unconditional_closed=false
```

branch-replay 最新剩余接口因此收缩为：

```text
MaterializedFreshLayerPDECColumnCRTExclusionOrUnregisteredMovingFamilyRouter
```

本步仍不宣称行/列命题闭合；它只删除裸 remote P-space ColumnCRT 终端解释，尚未排斥材料化 fresh-layer PDEC/ColumnCRT 或未登记 moving family。

## 93. cycle-debt fresh-layer PDEC 准入防火墙回接

后续文件

```text
experiments/prime_matrix_cycle_debt_fresh_layer_pdec_admission_firewall_router.py
docs/monograph/prime-matrix-cycle-debt-fresh-layer-pdec-admission-firewall-router.md
docs/monograph/prime-matrix-cycle-debt-fresh-layer-pdec-admission-firewall-router.json
data/prime-matrix-cycle-debt-fresh-layer-pdec-admission-firewall-ledger.json
```

上一节剩余为

```text
MaterializedFreshLayerPDECColumnCRTExclusionOrUnregisteredMovingFamilyRouter
```

本证书删除“无名材料化 fresh-layer PDEC/ColumnCRT”这个口径。registered support 内 fresh prime 投影单射，不能形成本地相位复用；跨窗口或远程材料化若要成为 PDEC，必须通过已经登记的 PDEC family 准入边界：同一 formal unit、固定 phase map、三物理原子以上、非二点 tautology、二秩以上且 cap-stable。否则事件回流 ColumnCRT/SAE/refined PDEC/sparse extractor/multiplicity，而不是成为新的终端。

当前读数：

```text
registered_block_count=6
minimum_first_fresh_minus_max_window=178
minimum_remote_plus_first_fresh_log10=38.803
local_registered_materialized_pdec_closed=true
current_materialized_pdec_frontier_closed=true
pdec_family_explicit_input_boundary_closed=true
newlayer_schema_admission_closed=true
newlayer_ranktwo_budget_independent_gate_removed=true
current_corpus_materialized_fresh_layer_pdec_closed=true
future_explicit_primitive_fresh_layer_pdec_schema_submitted=false
unregistered_moving_family_excluded=false
row_column_unconditional_closed=false
```

branch-replay 最新剩余接口因此收缩为：

```text
FutureExplicitPrimitiveFreshLayerPDECSchemaIfNewOrUnregisteredMovingFamilyRouter
```

本步仍不宣称行/列命题闭合；它只关闭当前语料中的无名材料化 PDEC/ColumnCRT 口径，不证明未来 primitive fresh-layer PDEC schema 不存在，也不排斥未登记 moving family。

## 94. cycle-debt branch-replay 当前物化前沿清零回接

后续文件

```text
experiments/prime_matrix_cycle_debt_branch_replay_current_frontier_zero_router.py
docs/monograph/prime-matrix-cycle-debt-branch-replay-current-frontier-zero-router.md
docs/monograph/prime-matrix-cycle-debt-branch-replay-current-frontier-zero-router.json
data/prime-matrix-cycle-debt-branch-replay-current-frontier-zero-ledger.json
```

上一节剩余为

```text
FutureExplicitPrimitiveFreshLayerPDECSchemaIfNewOrUnregisteredMovingFamilyRouter
```

本证书把“当前实例”与“未来准入”分开：`FutureExplicitPrimitiveFreshLayerPDECSchemaIfNew` 不是当前已出现的反例对象，而是未来新增 PDEC family 的准入纪律；未登记 moving family 若没有提交 source、shape、phase 与 persistence schema，也不能作为当前终端保留。

当前读数：

```text
current_fresh_layer_pdec_frontier_closed=true
future_explicit_primitive_fresh_layer_pdec_schema_submitted=false
unregistered_moving_family_schema_submitted=false
future_pdec_schema_admission_discipline_closed=true
future_sparse_schema_admission_discipline_closed=true
final_input_firewall_boundary_closed=true
no_hidden_terminal_remaining=true
cycle_debt_branch_replay_current_materialized_frontier_zero=true
future_explicit_schema_global_nonexistence_proved=false
row_column_unconditional_closed=false
```

因此 cycle-debt branch-replay 的当前物化前沿已经清零：

```text
CycleDebtBranchReplayCurrentMaterializedFrontierZeroWithFutureSchemaFirewall
```

但全局行/列命题仍未闭合；剩余转回最终输入防火墙后的全局门：

```text
GlobalFinalInputsStillOpen
```

本步不证明未来 primitive fresh-layer PDEC schema 或 moving-family schema 永不存在；若未来提交显式 schema，需要按防火墙重新审查。

## 95. early-zero gap CRT asymmetry 回接

后续文件

```text
experiments/prime_matrix_early_zero_gap_crt_asymmetry_router.py
docs/monograph/prime-matrix-early-zero-gap-crt-asymmetry-router.md
docs/monograph/prime-matrix-early-zero-gap-crt-asymmetry-router.json
data/prime-matrix-early-zero-gap-crt-asymmetry-ledger.json
```

本证书吸收用户提出的早期零行相邻素数载体提示。若第 `k` 行
`[(k-1)P+1,kP]` 无素数，则左右最近素数构成跨越该行的相邻素数对，间隙严格大于 `P`。
这给出真实链与反例链的强接口；但 CRT 周期只复制小素因子覆盖图案，不复制素数端点。

当前读数：

```text
early_zero_gap_lemma_proved=true
crt_gap_asymmetry_standalone_contradiction_proved=false
persistent_phase_routes_to_pdec_columncrt=true
sparse_phase_routes_to_sae=true
nonperiodic_endpoint_routes_to_h3_dsb_kls=true
nc_blk_or_external_dibfi_closed=false
row_column_unconditional_closed=false
```

因此该提示不再作为孤立启发保留，而是路由为三分支：

```text
persistent carrier phase => PDEC/ColumnCRT
sparse carrier phase => SAE
nonperiodic prime endpoint => H3-DSB/KLS -> NC-BLK or external DI/BFI
```

有限核查 `P<=5000` 的 `1547466` 条早期非第一行未发现零行；这只是证书核查，不替代全局证明。
最新剩余为：

```text
EarlyZeroGapCarrierAsymmetryRoutedToH3DSBNCBLKOrExternalDIBFI;GlobalFinalInputsStillOpen
```

本步仍不宣称行/列命题闭合；它只把相邻素数大间隙/CRT 非对称提示严格接入当前最终硬核，并排除
“单个 gap carrier 自动形成全局 CRT 矛盾”的跳步。

## 96. early-zero period-lift carrier drift 回接

后续文件

```text
experiments/prime_matrix_early_zero_period_lift_carrier_drift_router.py
docs/monograph/prime-matrix-early-zero-period-lift-carrier-drift-router.md
docs/monograph/prime-matrix-early-zero-period-lift-carrier-drift-router.json
data/prime-matrix-early-zero-period-lift-carrier-drift-ledger.json
```

本证书进一步处理 `P,k` 行 CRT 周期问题。令

```text
L_P=prod_{q<P} q.
```

若 `x` 是 `P` 的零行乘数，则 `x+tL_P` 仍为零行乘数，因为每个覆盖同余
`q | Px+c` 在 `q | P(x+tL_P)+c` 下保持不变。这说明反例覆盖链会在 CRT 行周期中精确复现。
但跨越该零行的左右相邻素数端点不由该周期控制；`a_t,b_t` 不必等于 `a_0+tPL_P,b_0+tPL_P`。

当前读数：

```text
zero_row_period_lift_exact=true
carrier_endpoint_periodic_translation_forced=false
all_sample_lifts_zero=true
sample_endpoint_translate_match_total_after_t0=1
persistent_drift_routes_to_pdec_columncrt=true
sparse_drift_routes_to_sae=true
nonperiodic_drift_routes_to_h3_dsb=true
row_column_unconditional_closed=false
```

已登记零行样本在 `12` 次周期提升中全部保持零行覆盖；端点 slack/gap 大量漂移，整体端点平移只
偶然出现 `1` 次，不能作为 CRT 推论使用。

最新三分流为：

```text
persistent carrier drift => PDEC/ColumnCRT
sparse carrier drift => SAE
nonperiodic carrier drift with persistent cover pressure => H3-DSB/KLS -> NC-BLK or external DI/BFI
```

最新剩余为：

```text
PeriodLiftCarrierDriftRoutedToPersistentPDECOrSparseSAEOrH3DSBNCBLK;GlobalFinalInputsStillOpen
```

本步不证明行/列命题全局闭合；它把“CRT 周期复现会在后续周期制造不对称矛盾”的说法精确化为
端点漂移三分流。

## 97. Q2 carrier-stage endpoint inversion 回接

后续文件

```text
experiments/prime_matrix_q2_carrier_stage_crt_asymmetry_router.py
docs/monograph/prime-matrix-q2-carrier-stage-crt-asymmetry-router.md
docs/monograph/prime-matrix-q2-carrier-stage-crt-asymmetry-router.json
data/prime-matrix-q2-carrier-stage-crt-asymmetry-ledger.json
```

本证书把相邻素数载体推进到 `Q2` 阶轮。设早期零行由相邻素数 `Q1<Q2` 跨越。
若 `Q2<P^2`，开间隙中每个合数都有小于 `P` 的素因子；若 `Q2>=P^2`，则进入平方锚/对角端点分支。
在完整 `Q2` 阶轮 `M_{<=Q2}` 下，两个端点复制后分别被 `Q1,Q2` 整除，因而不可能同时复现素端点。

当前读数：

```text
q2_full_wheel_endpoint_inversion_proved=true
q2_less_wheel_one_sided_endpoint_break_proved=true
all_sample_full_q2_endpoint_prime_replay_impossible=true
all_sample_q2_stage_modulus_exceeds_support_width=true
persistent_q2_carrier_block_routes_to_columncrt_pdec=true
sparse_q2_carrier_block_routes_to_sae=true
moving_endpoint_or_fresh_support_routes_to_h3_dsb=true
row_column_unconditional_closed=false
```

最新三分流为：

```text
full Q2 endpoint-prime replay => impossible
persistent closed carrier block => ColumnCRT/PDEC
sparse closed carrier block => SAE
moving endpoint/support => moving-family/H3-DSB/KLS
```

最新剩余为：

```text
Q2StageEndpointInversionRoutedToColumnCRTPDECOrSparseSAEOrMovingEndpointH3DSB;GlobalFinalInputsStillOpen
```

本步只关闭 `Q2` 阶端点稳定复现的跳步；全局行/列命题仍需排斥持久 `ColumnCRT/PDEC`、`SAE`
与 moving-family 出口。

## 98. Q2 endpoint replacement aperture-growth 回接

后续文件

```text
experiments/prime_matrix_q2_endpoint_replacement_aperture_growth_router.py
docs/monograph/prime-matrix-q2-endpoint-replacement-aperture-growth-router.md
docs/monograph/prime-matrix-q2-endpoint-replacement-aperture-growth-router.json
data/prime-matrix-q2-endpoint-replacement-aperture-growth-ledger.json
```

本证书把 `Q2` 阶端点反转转成孔径增长账本。完整 `Q2` 阶轮复制后，闭区间
`[Q1+tM_{<=Q2}, Q2+tM_{<=Q2}]` 全部为复合点，因此真实相邻素数端点必须替换到闭块外：

```text
new_gap >= old_gap + 2
```

当前读数：

```text
corrected_endpoint_bound=Q1<=kP-P, with equality possible at k=2; Q2>kP
full_q2_replay_makes_closed_carrier_composite=true
endpoint_replacement_gap_growth_per_replay_at_least=2
same_aperture_replay_impossible=true
bounded_aperture_replay_finite=true
persistent_moving_aperture_routes_to_pdec_columncrt=true
sparse_replacement_routes_to_sae=true
unbounded_replacement_routes_to_h3_dsb=true
row_column_unconditional_closed=false
```

最新三分流为：

```text
same bounded aperture replay => impossible
persistent moving aperture => ColumnCRT/PDEC
sparse replacement => SAE
unbounded moving support => H3-DSB/KLS or moving-family global input
```

最新剩余为：

```text
EndpointReplacementApertureGrowthNoBoundedReplayOrMovingSupportPDECSAEH3DSB;GlobalFinalInputsStillOpen
```

本步排除固定有界孔径复现；它仍不排斥全部 moving aperture、PDEC/ColumnCRT、SAE 与 H3-DSB/KLS 出口。

## 99. Q2 endpoint fresh-layer cascade 回接

后续文件

```text
experiments/prime_matrix_q2_endpoint_fresh_layer_cascade_router.py
docs/monograph/prime-matrix-q2-endpoint-fresh-layer-cascade-router.md
docs/monograph/prime-matrix-q2-endpoint-fresh-layer-cascade-router.json
data/prime-matrix-q2-endpoint-fresh-layer-cascade-ledger.json
```

本证书把扩孔/移动分支继续转成新素层扩模级联。端点替换后的新右端素数 `B_new` 位于闭复合块外，
且大于旧全轮平移边界；它进入下一阶全轮后，下一次复现又被自身零类杀掉。于是每一阶都必须引入
旧有限端点层之外的新素数。

当前读数：

```text
fresh_endpoint_after_each_replacement=true
next_full_wheel_kills_fresh_endpoint=true
log_modulus_at_least_doubles_per_endpoint_cascade=true
aperture_lower_bound_growth_linear_plus_two=true
finite_crt_period_terminal_possible=false
persistent_fresh_endpoint_pattern_routes_to_pdec_columncrt=true
sparse_fresh_endpoint_cascade_routes_to_sae=true
non_pdec_fresh_layer_cascade_routes_to_tail_sieve_h3=true
row_column_unconditional_closed=false
```

最新三分流为：

```text
fixed finite CRT period terminal => impossible
persistent fresh endpoint phase => ColumnCRT/PDEC
sparse fresh endpoint cascade => SAE
non-PDEC unbounded fresh layers => tail-sieve/H3-DSB/KLS
```

最新剩余为：

```text
FreshEndpointLayerCascadeNoFiniteCRTPeriodOrPDECSAEH3TailSieve;GlobalFinalInputsStillOpen
```

本步排除固定有限 CRT 周期终端；全局行/列命题仍需排斥 fresh-layer PDEC/ColumnCRT、SAE 与
tail-sieve/H3 出口。

## 100. Q2 fresh-layer tail-mass 二分回接

后续文件

```text
experiments/prime_matrix_q2_fresh_layer_tail_mass_dichotomy_router.py
docs/monograph/prime-matrix-q2-fresh-layer-tail-mass-dichotomy-router.md
docs/monograph/prime-matrix-q2-fresh-layer-tail-mass-dichotomy-router.json
data/prime-matrix-q2-fresh-layer-tail-mass-dichotomy-ledger.json
```

本证书把上一节留下的 non-PDEC 无界 fresh-layer 级联压成“受控孔径 SAE / 孔径爆炸支撑运动”二分。
若 fresh-layer 没有形成持久相关集中，则每个新素层只贡献一个禁相位；在孔径 `W_j` 内的形式质量至多为
`W_j/B_j`。由上一节的 fresh modulus `M_j` 对数至少倍增、且 `B_{j+1}>M_j`，以及端点替换给出的线性孔径模型 `W_j=W0+2j`，得到

```text
sum_j W_j/B_j < infinity
```

所以受控孔径、无 PDEC 的 fresh-tail 只能进入可求和 `SAE`。若孔径增长到反复追赶 fresh modulus，
则该分支已经变成全局支撑运动或孔径爆炸，回到 `H3-DSB`、moving-support `PDEC` 或显式支撑运动账本。

当前读数：

```text
one_residue_fresh_layer_mass_model=true
linear_aperture_fresh_mass_summable=true
subexponential_controlled_aperture_summable=true
aperture_explosion_dichotomy=true
persistent_fresh_layer_correlation_routes_to_pdec=true
controlled_non_pdec_fresh_tail_routes_to_sae=true
row_column_unconditional_closed=false
```

最新三分流为：

```text
controlled non-PDEC fresh-tail => SAE
persistent fresh-layer correlation => ColumnCRT/PDEC
aperture explosion/support motion => H3-DSB or moving-support PDEC
```

最新剩余为：

```text
ControlledFreshLayerTailMassSAEOrApertureExplosionH3PDEC;GlobalFinalInputsStillOpen
```

本步只关闭受控孔径尾质量；它仍不排斥孔径爆炸、moving-support H3/DSB 或 fresh-layer PDEC，
因此不是行/列命题的全局无条件证明。

## 101. Q2 aperture-explosion schema-firewall 回接

后续文件

```text
experiments/prime_matrix_q2_aperture_explosion_schema_firewall_router.py
docs/monograph/prime-matrix-q2-aperture-explosion-schema-firewall-router.md
docs/monograph/prime-matrix-q2-aperture-explosion-schema-firewall-router.json
data/prime-matrix-q2-aperture-explosion-schema-firewall-ledger.json
```

本证书把孔径爆炸剩余口径同步到已有支撑运动与 PDEC 防火墙。受控孔径 fresh-tail 已由上一证书压入 `SAE`；
若剩余反例链要求 `log W_j` 反复追赶 `log M_j`，则必须提交支撑运动、阻断包变化、fresh-layer PDEC
或 moving-family 的显式 schema。当前 registered support-motion、本轮材料化 fresh-layer PDEC 与 branch-replay
current frontier 已有防火墙同步，故无名 aperture-explosion 终端不能作为活动剩余保留。

当前读数：

```text
controlled_fresh_tail_imported=true
registered_support_motion_imported_closed=true
current_materialized_fresh_pdec_imported_closed=true
current_branch_replay_frontier_zero_imported=true
future_explicit_aperture_explosion_schema_submitted=false
unnamed_aperture_explosion_terminal_allowed=false
row_column_unconditional_closed=false
```

最新三分流为：

```text
controlled fresh-tail => SAE
current unnamed aperture explosion => forbidden by schema firewall
future explicit moving-family/PDEC schema => reopen under firewall
```

最新剩余为：

```text
Q2ApertureExplosionCurrentSchemaFirewall;GlobalFinalInputsStillOpen
```

本步仍不是行/列命题全局闭合；它只把当前无名孔径爆炸口径删除，未来显式 schema 与全局最终输入仍开。

## 102. Q2 CRT ladder 到最终 exact-source 原子对齐回接

后续文件

```text
experiments/prime_matrix_q2_to_final_exact_source_alignment_router.py
docs/monograph/prime-matrix-q2-to-final-exact-source-alignment-router.md
docs/monograph/prime-matrix-q2-to-final-exact-source-alignment-router.json
data/prime-matrix-q2-to-final-exact-source-alignment-ledger.json
```

本证书把 Q2 阶 CRT 梯对齐到最终开放输入。受控尾量已入 `SAE`，无名孔径爆炸已被 schema 防火墙删除；
因此当前 Q2 局部不再含活动终端。Q2/CRT 的位置刚性不能替代 actual pre-Cauchy source 的 exact `(u,v)`
fiber 质量非集中估计；若要把反例链与真实链的容量/相位矛盾推成最终矛盾，必须证明 source 侧的
nonterminal exact-UV fiber 非集中，或接受/证明外部 DI/BFI/Kuznetsov 谱输入，并通过 DStructure/Rankin
独立晋级验收。

当前读数：

```text
q2_current_local_terminal_removed=true
q2_position_rigidity_controls_source_mass=false
preterminal_exact_uv_fiber_aperiodicity_imported=true
source_domain_rank_atom_package_imported=true
dstructure_independently_accepted=false
row_column_unconditional_closed=false
```

最新三分流为：

```text
Q2 local CRT ladder => current unnamed terminal removed
strict self-contained lane => NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource
external/promotion lane => ExternalDIBFIKuznetsovDispersionTheoremMatch plus DStructureRankinPromotion
```

最新剩余为：

```text
NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource OR ExternalDIBFIKuznetsovDispersionTheoremMatch; DStructureRankinPromotionIndependentAcceptanceOpen
```

本步关闭的是 Q2 局部残余与最终输入之间的对齐缺口；它没有证明 fiber 非集中、外部谱定理或独立晋级验收。

## 103. Global CRT homogeneity 前沿同步回接

后续文件

```text
experiments/prime_matrix_global_crt_homogeneity_frontier_router.py
docs/monograph/prime-matrix-global-crt-homogeneity-frontier-router.md
docs/monograph/prime-matrix-global-crt-homogeneity-frontier-router.json
data/prime-matrix-global-crt-homogeneity-frontier-ledger.json
```

本证书把用户提出的 Q1/Q2 相邻素数不对称与全局 CRT 周期路线放在同一防火墙中。结论是：
全 `Q2` 轮确实不能同时复现覆盖块和两个素端点；端点稳定 replay 已闭合。但纯有限 CRT 前缀具有同质提升结构：
若 `r` 是新素数且 `r` 不整除旧轮模 `M_Y`，则每个旧余类 `a` 的 `r` 个提升 `a+tM_Y`
在模 `r` 下遍历全部余类，恰删一个相位。因此无穷轮筛解释临界密度，却不自动给出长度 `P`
移动区间的 actual occupancy 下界；除非相位方程形成已登记的 `PDEC/ColumnCRT`，否则不能从 CRT
位置刚性直接推出全局矛盾。

当前读数：

```text
full_q2_wheel_endpoint_stable_replay_impossible=true
finite_crt_period_terminal_removed=true
controlled_fresh_layer_tail_sae_imported=true
unnamed_aperture_explosion_forbidden=true
pure_finite_crt_global_phase_contradiction_found=false
global_crt_homogeneity_blocks_pure_phase_contradiction=true
q2_crt_position_rigidity_routed_to_exact_source=true
source_rank_package_synced_to_pointwise_kernel=true
alpha_row_anchor_phase_emission_formula_proved=false
row_column_unconditional_closed=false
```

最新剩余被同步为：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger
AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

这一步关闭的是“纯 CRT 全局相位矛盾”作为最终证明的误出口；它把剩余推进到 actual-source exact-UV
与逐 primitive alpha/delta 核表前沿，但没有证明行/列命题无条件闭合。

## 104. Global CRT 到 strict 终端饱和前沿同步

后续文件

```text
experiments/prime_matrix_global_crt_terminal_saturation_sync_router.py
docs/monograph/prime-matrix-global-crt-terminal-saturation-sync-router.md
docs/monograph/prime-matrix-global-crt-terminal-saturation-sync-router.json
data/prime-matrix-global-crt-terminal-saturation-sync-ledger.json
```

本证书继续利用既有 alpha-row 与终端家族下钻结果，把上一节的 `AlphaRowAnchorPhaseEmissionFormulaLedger`
继续同步到当前 strict 饱和前沿。结论是：global CRT/Q1-Q2 路线不应停在 alpha row 粗硬点；
alpha row 局部前沿已回到 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve` 与模型账本，PDEC/CleanKLS
终端门又被当前内部语料攻成饱和循环。CleanKLS/Kuznetsov/DLS 手臂回到终端家族，nonrecursive
破环包回到 signed 坐标-来源闭环，seed-cycle-cut 分支也已饱和。

当前读数：

```text
pure_crt_homogeneity_firewall_imported=true
alpha_row_local_frontier_terminal_synced=true
pdec_cap_clean_kls_terminal_split_imported=true
kuznetsov_dls_route_returns_to_terminal_family=true
pdec_scope_branch_saturated=true
nonrecursive_breaker_cycle_detected=true
seed_cycle_cut_branch_saturated=true
acyclic_same_set_scope_match_proved=false
new_explicit_joint_constructor_formula_artifact_present=false
row_column_unconditional_closed=false
```

最新 strict 活动基压成：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact)
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

这一步继续推进了全局 CRT 路线的对齐深度：纯 CRT 相位矛盾、alpha row 局部公式、CleanKLS/DLS
和 seed-cycle-cut 都不是当前已证闭合出口。剩余真正非循环候选是 PDEC same-set 作用域匹配或新的显式
joint alpha/delta 构造公式。

## 105. Global CRT branch trace 前沿回接

后续文件

```text
experiments/prime_matrix_global_crt_branch_trace_frontier_router.py
docs/monograph/prime-matrix-global-crt-branch-trace-frontier-router.md
docs/monograph/prime-matrix-global-crt-branch-trace-frontier-router.json
data/prime-matrix-global-crt-branch-trace-frontier-ledger.json
```

本证书把上一节的 `NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact` 继续沿已有 strict
反分裂/原子 joint row/内置 pairing 链下钻。旧分裂路线会回到 row-level/signed-source 固定点，
所以真正需要的是 atomic branch trace：对每条 atomic joint row，在同一 formal unit 和
Cauchy/Phi/payment 前完整列出 branch trace，同时同步给出 basis word、signed coefficient、
alpha/delta pairing、orientation/local factor、exact UV 和命名回流。

当前读数：

```text
global_crt_terminal_saturation_imported=true
pdec_scope_branch_still_open=true
new_joint_formula_terminal_obligation_imported=true
new_joint_reduced_to_antisplit_formula=true
antisplit_reduced_to_atomic_declaration=true
atomic_declaration_reduced_to_builtin_pairing=true
builtin_pairing_reduced_to_exact_branch_trace=true
acyclic_same_set_scope_match_proved=false
exact_atomic_joint_branch_trace_signed_coefficient_formula_proved=false
row_column_unconditional_closed=false
```

最新 strict 活动基压成：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn)
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

这一步把“新 joint 公式”继续精确到 signed coefficient 的奇取向数据来源。PDEC scope 与 atomic
branch trace 二者均未证明，因此行/列命题仍未无条件闭合。

## 106. Global CRT signed payload 同步回接

后续文件

```text
experiments/prime_matrix_global_crt_signed_payload_sync_router.py
docs/monograph/prime-matrix-global-crt-signed-payload-sync-router.md
docs/monograph/prime-matrix-global-crt-signed-payload-sync-router.json
data/prime-matrix-global-crt-signed-payload-sync-ledger.json
```

本证书把上一节的 exact atomic branch trace 一侧继续与 strict payload 前沿同步：
`ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn` 已压成
`AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn`。同时，PDEC same-set 手臂在当前内部自足语料中
已饱和到新 joint 公式线，而新 joint 公式线又经 branch-trace 链回到 signed payload。

当前读数：

```text
global_crt_branch_trace_basis_imported=true
exact_atomic_trace_reduced_to_signed_payload=true
finite_crt_cannot_generate_signed_payload=true
pdec_internal_arm_saturated_to_new_joint=true
external_or_new_pdec_scope_still_open=true
strict_internal_self_contained_basis_sharpened=true
atomic_signed_payload_constructor_proved=false
acyclic_same_set_scope_match_proved=false
row_column_unconditional_closed=false
```

内部自足线的最新硬点为：

```text
AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

若保留新 scope/PDEC 输入，总活动基为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn)
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

这一步识别的全局结构断点是：CRT 周期扩张只复制零同余类和可见坐标 trace，不能生成 orientation、
local factor 与 signed coefficient 的 payload。它仍不是最终证明；signed payload constructor、
新 PDEC scope、ExactUV、模型余量、RatePreservation 与 DStructure/Rankin 仍未合取闭合。

## 107. 前素数间隙 P-CRT 均匀性路由回接

后续文件

```text
experiments/prime_matrix_predecessor_gap_pcrt_uniformity_router.py
docs/monograph/prime-matrix-predecessor-gap-pcrt-uniformity-router.md
docs/monograph/prime-matrix-predecessor-gap-pcrt-uniformity-router.json
data/prime-matrix-predecessor-gap-pcrt-uniformity-ledger.json
```

本证书专门审计“若 `P` 与前一素数 `p^-` 的间隙较大，是否在 `P` 阶 CRT 周期中产生非 P 列均匀性
或 `c <-> P-c` 对称性矛盾”这一接口。结论是：完整 `M_{\le P}=P M_{<P}` 周期内，CRT 交集在每个
非 P 列精确等量，反射 `n -> -n` 也精确配对 `c` 与 `P-c`；这些是全周期恒等式，且与前素数间隙无关。

前素数间隙真正给出的只是第一行局部缺口：列 `p^-+1,...,P-1` 在第一行没有实际素数。若要把完整
P-wheel 的列均匀性转化为初始 `P x P` 方阵内的补偿或相位矛盾，必须新增局部化转移定理。

当前读数：

```text
complete_wheel_non_p_uniformity_proved=true
complete_wheel_reflection_symmetry_proved=true
localized_transfer_to_initial_square_proved=false
large_predecessor_gap_symmetry_contradiction_found=false
non_p_column_uniformity_contradiction_found=false
row_column_unconditional_closed=false
```

`P<=5000` 最大前素数间隙样本中，非 P 零列总数为 `0`，最大样本 `P=1361,p^-=1327,gap=34` 的
33 个第一行缺口列都在后续行被实际素数补上；但这只是风险形态定位，不是证明。

最新活动基保持为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn)
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

这一步关闭的是“完整 P-wheel 均匀性自动给出局部非 P 列矛盾”的跳步。真正新接口是
`LocalizedPCRTColumnUniformityTransferToInitialPxPSquare`，它若无法自足证明，就回流到 PDEC scope 或
signed payload/ExactUV 前沿。

## 108. Localized P-CRT / Linnik=2 屏障回接

后续文件

```text
experiments/prime_matrix_localized_pcrt_transfer_linnik2_barrier_router.py
docs/monograph/prime-matrix-localized-pcrt-transfer-linnik2-barrier-router.md
docs/monograph/prime-matrix-localized-pcrt-transfer-linnik2-barrier-router.json
data/prime-matrix-localized-pcrt-transfer-linnik2-barrier-ledger.json
```

本证书继续攻击上一节的 `LocalizedPCRTColumnUniformityTransferToInitialPxPSquare`。列侧内容可完全精确化：
非 P 列 `c` 在初始 `P x P` 方阵中有素数，当且仅当存在素数
`ell<=P^2` 且 `ell≡c mod P`。因此对所有非零 `c mod P` 完成该局部化转移，等价于 prime-modulus
点态最小 AP 素数指数 `2`。

当前读数：

```text
localized_pcrt_transfer_active=true
column_occupancy_equivalent_to_least_prime_ap=true
linnik2_barrier_identified=true
localized_transfer_current_corpus_proved=false
pointwise_linnik2_ap_theorem_proved=false
row_column_unconditional_closed=false
```

有限样本 `P<=3000` 检查了 `429` 个素数模数，缺失剩余类总数为 `0`，最大首素数行号为 `108`
（`P=2861`）。这继续说明有限现象稳定，但不作为证明。

最新活动基扩展为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
 OR PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2)
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

这一步把“局部化 P-CRT 列均匀转移”压成一个清晰的 AP 点态屏障。完整 CRT 均匀性、BV/平均 AP
均匀性和有限样本均不能替代这个点态断言；若不引入新的 AP 定理，路线必须回到 PDEC scope 或
signed payload/ExactUV 前沿。

## 109. Linnik=2 非主角色障碍回接

后续文件

```text
experiments/prime_matrix_linnik2_nonprincipal_character_obstruction_router.py
docs/monograph/prime-matrix-linnik2-nonprincipal-character-obstruction-router.md
docs/monograph/prime-matrix-linnik2-nonprincipal-character-obstruction-router.json
data/prime-matrix-linnik2-nonprincipal-character-obstruction-ledger.json
```

本证书继续攻击 `PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2`。对每个非零剩余类定义

```text
theta_a(P)=sum_{ell<=P^2, ell prime, ell=a mod P} log ell
T_chi(P)=sum_{a in F_P^*} chi(a) theta_a(P)
N_a(P)=sum_{chi!=chi0} conjugate(chi(a)) T_chi(P)
```

有限群角色正交给出精确恒等式：

```text
theta_a(P)=(T_0(P)+N_a(P))/(P-1)
```

因此若某个非 P 列在 `P^2` 前没有素数，则 `theta_a(P)=0`，从而

```text
N_a(P)=-T_0(P)
sum_{chi!=chi0}|T_chi(P)|^2 >= T_0(P)^2/(P-2)
```

这一步把零列缺陷压成显式的非主角色负相位投影/能量尖峰。下一步只需排斥所有 `a` 上
`N_a(P)` 到达 `-T_0(P)` 的极端负相位对齐。

当前读数：

```text
theta_character_expansion_exact=true
zero_column_forces_negative_projection=true
zero_column_forces_energy_spike=true
pointwise_projection_bound_proved=false
row_column_unconditional_closed=false
```

有限样本 `P<=3000` 检查 `429` 个素数模数，theta 零剩余类总数为 `0`，最大负缺口比例为
`0.686688`（`P=73`）。这只作为风险定位，不作为证明。

最新活动基收缩为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
 OR PointwiseNonprincipalProjectionBoundBelowPrincipalMassAtXEqualsP2)
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本步仍不是无条件闭合；当前语料尚未证明点态非主投影界，也未排除 Siegel/大偏差型负相位集中。

## 110. Linnik=2 rank-one 相位容量回接

后续文件

```text
experiments/prime_matrix_linnik2_rankone_phase_capacity_router.py
docs/monograph/prime-matrix-linnik2-rankone-phase-capacity-router.md
docs/monograph/prime-matrix-linnik2-rankone-phase-capacity-router.json
data/prime-matrix-linnik2-rankone-phase-capacity-ledger.json
```

本证书继续攻击 `PointwiseNonprincipalProjectionBoundBelowPrincipalMassAtXEqualsP2`。关键分解为：

```text
rho_a(P)=-N_a(P)/T_0(P)=1-theta_a(P)/average_theta(P)
theta_a(P)=0  iff  rho_a(P)=1
```

零列确实推出容量必要条件：

```text
||T_nonprincipal||_2^2 >= T_0(P)^2/(P-2)
```

但这个条件不是矛盾。有限样本 `P<=3000` 中，`429` 个素数模数没有 theta 零列；其中 `423` 个已经满足
非主总能量超过零列必要地板，说明容量-only 线路不能作为最终闭合。最大总能量/零列地板比例为
`5.751979`（`P=2953`），但对应最大负投影比例只有 `0.139565`。真正危险的是某个 residue evaluation
simplex 方向上的 rank-one 负投影，而不是总能量大小。

当前读数：

```text
energy_floor_necessary_condition_closed=true
energy_capacity_only_route_not_enough=true
evaluation_vector_simplex_geometry_closed=true
rankone_phase_coherence_exclusion_proved=false
row_column_unconditional_closed=false
```

最新活动基进一步收缩为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
 OR RankOneNegativeEvaluationProjectionPhaseCoherenceExclusionAtP2)
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本步关闭的是“用总能量容量直接制造矛盾”的误出口；剩余是逐 residue 的 rank-one 相位极化排斥。

## 111. 三命题前沿与 rank-one 显式公式屏障回接

后续文件

```text
experiments/three_claims_frontier_rankone_explicit_formula_router.py
docs/monograph/three-claims-frontier-rankone-explicit-formula-router.md
docs/monograph/three-claims-frontier-rankone-explicit-formula-router.json
data/three-claims-frontier-rankone-explicit-formula-ledger.json
```

本证书重新梳理三个命题的最前沿：

```text
row/column latest open:
  RankOneNegativeEvaluationProjectionPhaseCoherenceExclusionAtP2

two-point / quadratic secondary sieve latest open:
  I3CoreTrueResidualTotalLargeIncidenceOrExternalDIBFIKLSWindow

RH latest open:
  IndependentRefereeAcceptanceOfAllRHControlledExits
```

对行/列最新硬点继续下钻：

```text
rho_a(P)=1-theta(P^2;P,a)/(T_0(P)/(P-1))
rho_a(P)<1  iff  theta(P^2;P,a)>0
```

因此 rank-one 相位排斥不是一个新的弱命题，而是 sharp pointwise AP positivity：

```text
SharpPointwiseThetaAPPositivityAtXEqualsP2ForPrimeModuli
```

显式公式口径为：主项约为 `P`，必须逐个 residue 证明带符号非主零点包和 trivial 项严格小于主项。
当前 GRH 形状误差 `O(P log^2 P)`、BV 平均、完整 CRT 均匀性、标准 Linnik 均不能推出阈值正性。

当前读数：

```text
rankone_equivalent_to_theta_ap_positivity=true
explicit_formula_barrier_identified=true
current_classical_inputs_sufficient=false
row_column_unconditional_closed=false
two_point_unconditional_closed=false
rh_unconditional_closed=false
```

最新活动基更新为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
 OR ExplicitAPZeroPacketBoundBeatingMainTermAtXEqualsP2)
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本步仍不是无条件闭合；它关闭的是将三个命题状态混用、将 GRH/BV/CRT 平均误用为 `P^2` 点态 AP 正性的路线。

## 112. 显式 AP 零点包的 Siegel/非实相位二分回接

后续文件

```text
experiments/prime_matrix_explicit_ap_zero_packet_siegel_split_router.py
docs/monograph/prime-matrix-explicit-ap-zero-packet-siegel-split-router.md
docs/monograph/prime-matrix-explicit-ap-zero-packet-siegel-split-router.json
data/prime-matrix-explicit-ap-zero-packet-siegel-split-ledger.json
```

本证书继续攻击上一节的

```text
ExplicitAPZeroPacketBoundBeatingMainTermAtXEqualsP2
```

并把它拆成两个真正硬分支：

```text
SiegelExceptionalBiasExclusionAtSquareScale
NonrealZeroPacketResiduePhaseCancellationAtXEqualsP2
```

实零分支的尺度读数为：若 `beta=1-lambda/log P`，则 square-scale 贡献约为

```text
P^(2*beta-1)/beta = P*exp(-2*lambda)/beta
```

仍可与 `P` 级主项同阶；因此不能靠平均、容量或完整 CRT 均匀性自动排除。剥离实零后，非实零点包还需要逐
`residue` 的相位抵消，排除单个 evaluation simplex 方向上的同向集中。

当前读数：

```text
siegel_branch_closed=false
nonreal_branch_closed=false
trivial_terms_isolated=true
classical_inputs_sufficient=false
row_column_unconditional_closed=false
```

最新活动基更新为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
 OR (SiegelExceptionalBiasExclusionAtSquareScale
     AND NonrealZeroPacketResiduePhaseCancellationAtXEqualsP2))
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本步仍不是行/列命题无条件闭合；它关闭的是“无名零点包”出口，把解析 AP 分支压成 Siegel 偏置排斥与非实零包相位抵消两个可审计目标。

## 113. Siegel 分支的二次半类余量门回接

后续文件

```text
experiments/prime_matrix_siegel_quadratic_halfclass_margin_router.py
docs/monograph/prime-matrix-siegel-quadratic-halfclass-margin-router.md
docs/monograph/prime-matrix-siegel-quadratic-halfclass-margin-router.json
data/prime-matrix-siegel-quadratic-halfclass-margin-ledger.json
```

本证书继续下钻上一节的

```text
SiegelExceptionalBiasExclusionAtSquareScale
```

对素模 `P` 的二次角色 `chi_P`，定义

```text
T_chi(P)=sum_{ell<=P^2, ell prime, ell!=P} chi_P(ell) log ell
T0(P)=sum_{ell<=P^2, ell prime, ell!=P} log ell
r_quad(P)=|T_chi(P)|/T0(P)
```

实零偏置分支被压成二次半类余量门：危险半类平均主项余量正比于 `1-r_quad(P)`。若
`beta=1-lambda/log P`，则 square-scale 下该比例的危险尺度约为 `exp(-2*lambda)/beta`，所以没有有效
`beta` 间隙时不能自动排除。

当前读数：

```text
quadratic_projection_identity_closed=true
halfclass_margin_theorem_proved=false
effective_no_siegel_input_accepted=false
siegel_branch_closed=false
row_column_unconditional_closed=false
```

有限诊断口径 `7<=P<=1000` 中最大 `r_quad(P)=0.13027036286351173` 出现在 `P=7`；该扫描只用于定位风险，
不是无限证明输入。

最新活动基更新为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
 OR ((QuadraticHalfClassSquareScaleBiasMarginTheorem
      OR EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale)
     AND NonrealZeroPacketResiduePhaseCancellationAtXEqualsP2))
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本步仍不是闭合；它把 Siegel 实零偏置从口头风险变为可审计的二次角色投影余量定理，或等价地需要足够强的外部无 Siegel 零点/`beta` 间隙输入。

## 114. 非实零包的二次半类 simplex 相位门回接

后续文件

```text
experiments/prime_matrix_nonreal_halfclass_simplex_phase_router.py
docs/monograph/prime-matrix-nonreal-halfclass-simplex-phase-router.md
docs/monograph/prime-matrix-nonreal-halfclass-simplex-phase-router.json
data/prime-matrix-nonreal-halfclass-simplex-phase-ledger.json
```

本证书继续下钻

```text
NonrealZeroPacketResiduePhaseCancellationAtXEqualsP2
```

删除主角色和二次角色后，非实残差为

```text
R_a=(P-1)theta_a(P)-T0(P)-chi_2(a)T_2(P)
```

相应 evaluation 向量 `w_a` 满足精确内积：

```text
<w_a,w_b>=P-3  if a=b
<w_a,w_b>=-2   if a!=b and chi_2(a)=chi_2(b)
<w_a,w_b>=0    if chi_2(a)!=chi_2(b)
```

也就是说，非实零包不是无结构残差，而是两个正交二次半类 simplex 上的 rank-one 投影问题。零列若存在，则

```text
R_a=-T0(P)-chi_2(a)T_2(P)
```

所以非实包必须在对应半类的单方向提供至少 `(1-|T_2|/T0)T0` 的负投影。

当前读数：

```text
halfclass_simplex_geometry_closed=true
zero_requirement_after_quadratic_removal_closed=true
nonreal_energy_floor_closed=true
nonreal_rankone_projection_exclusion_proved=false
row_column_unconditional_closed=false
```

有限诊断 `7<=P<=1000` 中，删除二次角色后仍有 `161` 个样本的非实能量超过零列必要地板但无零列；最大非实能量/地板比为 `4.868669254524807`。这继续说明容量地板不能替代相位排斥。

最新活动基更新为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
 OR ((QuadraticHalfClassSquareScaleBiasMarginTheorem
      OR EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale)
     AND NonrealHalfClassSimplexRankOneProjectionExclusionAtP2))
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本步仍不是闭合；它把非实残差的全局相位硬点从“零包抵消”压成两个半类 simplex 中的 rank-one 负投影排斥。

## 111. Nonreal half-class compensation variance router

新增文件

```text
experiments/prime_matrix_nonreal_halfclass_compensation_variance_router.py
docs/monograph/prime-matrix-nonreal-halfclass-compensation-variance-router.md
docs/monograph/prime-matrix-nonreal-halfclass-compensation-variance-router.json
data/prime-matrix-nonreal-halfclass-compensation-variance-ledger.json
```

本步继续下钻

```text
NonrealHalfClassSimplexRankOneProjectionExclusionAtP2
```

对每个二次半类 `H_s={a:chi_2(a)=s}`，令

```text
mu_s=(T0+sT2)/(P-1).
```

则非实残差不是任意 simplex 坐标，而是严格中心化：

```text
R_a=(P-1)(theta_a-mu_s),    sum_{a in H_s} R_a=0.
```

若零列发生在 `a0 in H_s`，则同半类其它 residue 必须承担等量正补偿：

```text
R_a0=-(P-1)mu_s
sum_{a!=a0, a in H_s} R_a=(P-1)mu_s.
```

尖孔方差地板为

```text
sum_{a in H_s} R_a^2 >= ((P-1)mu_s)^2 * h/(h-1),  h=(P-1)/2,
```

且等号态是非孔 residue 全部取 `theta=mu_s*h/(h-1)` 的平铺补偿。因此容量/方差地板是锐的必要条件，不是排斥零列的充分条件。

当前读数：

```text
halfclass_centering_identity_closed=true
zero_column_compensation_mass_closed=true
sharp_one_hole_variance_floor_closed=true
capacity_only_sufficiency_rejected=true
actual_prime_compensation_nonconcentration_proved=false
row_column_unconditional_closed=false
```

有限诊断 `7<=P<=1000` 中，半类方差超过零列尖孔地板的样本半类数为 `297`，但这并不产生零列；最大实际缺孔/零列所需缺孔比为 `0.6876234883389729`，发生在 `P=73` 的二次剩余半类。

最新活动基更新为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
 OR ((QuadraticHalfClassSquareScaleBiasMarginTheorem
      OR EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale)
     AND HalfClassCompensationMassNonconcentrationOrColumnCRTPDEC))
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本步关闭的是“半类容量足够即可矛盾”的误出口。剩余硬点更窄：证明真实素数诱导的补偿质量不能在同半类近似平铺，或者把持久平铺相位登记并排斥为 ColumnCRT/PDEC/moving-family 出口。

## 112. Half-class ratio Fourier lock router

新增文件

```text
experiments/prime_matrix_halfclass_ratio_fourier_lock_router.py
docs/monograph/prime-matrix-halfclass-ratio-fourier-lock-router.md
docs/monograph/prime-matrix-halfclass-ratio-fourier-lock-router.json
data/prime-matrix-halfclass-ratio-fourier-lock-ledger.json
```

本步继续下钻

```text
HalfClassCompensationMassNonconcentrationOrColumnCRTPDEC
```

固定假想缺孔 `a0` 后，用 ratio 坐标

```text
u=a0^{-1}a
```

把同一二次半类归一化为二次剩余子群 `Q`。令

```text
f_a0(u)=theta(P^2;P,a0*u)
c_a0=sum_{u!=1} f_a0(u)/(h-1).
```

则半类方差超过单点地板的部分精确等于 punctured flatness：

```text
sum R_a^2 - (P-1)^2(theta_a0-mu)^2*h/(h-1)
= (P-1)^2 * sum_{u!=1}(f_a0(u)-c_a0)^2.
```

并且平铺补偿等价于二次剩余子群上的所有非平凡 Fourier 系数同时锁定：

```text
F_psi = theta_a0 - c_a0    for every nontrivial psi on Q.
```

Parseval 形式为

```text
sum_{psi!=1}|F_psi-(theta_a0-c_a0)|^2
= h * sum_{u!=1}(f_a0(u)-c_a0)^2.
```

当前读数：

```text
ratio_normalization_closed=true
one_point_variance_excess_identity_closed=true
flat_compensator_fourier_lock_equivalence_closed=true
capacity_or_variance_only_sufficiency_rejected=true
persistent_ratio_fourier_lock_excluded=false
row_column_unconditional_closed=false
```

有限诊断 `7<=P<=1000` 中，最小 residue puncture 的最佳平铺误差相对能量最小值为 `0.00045571844422404815`；大量大素数样本接近平铺，说明“接近平铺”本身不是矛盾。真正剩余是排斥零列条件下的持久全频率锁，或将其登记并排斥为 ColumnCRT/PDEC/moving-family。

最新活动基更新为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
 OR ((QuadraticHalfClassSquareScaleBiasMarginTheorem
      OR EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale)
     AND HalfClassRatioFourierLockExclusionOrColumnCRTPDEC))
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本步关闭的是“补偿平铺只是局部容量现象”的误出口：若零列平铺补偿持久存在，它必须表现为二次剩余 ratio 子群上的全非平凡频率同步锁相。行/列命题仍未无条件闭合。

## 113. Half-class twist-pair character lock router

新增文件

```text
experiments/prime_matrix_halfclass_twist_pair_character_lock_router.py
docs/monograph/prime-matrix-halfclass-twist-pair-character-lock-router.md
docs/monograph/prime-matrix-halfclass-twist-pair-character-lock-router.json
data/prime-matrix-halfclass-twist-pair-character-lock-ledger.json
```

本步继续下钻

```text
HalfClassRatioFourierLockExclusionOrColumnCRTPDEC
```

令 `Q` 为模 `P` 的二次剩余子群。`Q` 上每个非平凡频率 `psi` 都有模 `P` 的两条 Dirichlet 扩张 `chi` 与 `chi*chi_2`。对假想缺孔 `a0 in H_s`，上一节的 ratio-Fourier 系数满足精确配对公式：

```text
F_psi(a0)=chi(a0)*(T_chi+s*T_{chi chi_2})/2.
```

因此零列平铺补偿不是单个角色异常，也不是单纯容量问题；它要求所有二次扭曲角色对同步落到同一个 `a0` 相位轨道：

```text
chi(a0)*(T_chi+s*T_{chi chi_2})/2 = theta(P^2;P,a0)-c_a0
```

当前读数：

```text
subgroup_character_extension_closed=true
twist_pair_projection_identity_closed=true
orbit_lock_reformulation_closed=true
single_character_or_capacity_sufficiency_rejected=true
persistent_twist_pair_orbit_lock_excluded=false
row_column_unconditional_closed=false
```

最新活动基更新为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
 OR ((QuadraticHalfClassSquareScaleBiasMarginTheorem
      OR EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale)
     AND QuadraticTwistPairCharacterOrbitLockExclusionOrColumnCRTPDEC))
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本步关闭的是“ratio-Fourier 全频率锁仍停留在抽象子群语言”的误出口。剩余最窄接口是排斥持久二次扭曲配对角色轨道锁，或将其登记并排斥为 ColumnCRT/PDEC/moving-family 出口。行/列命题仍未无条件闭合。

## 114. Half-class log independence degeneracy router

新增文件

```text
experiments/prime_matrix_halfclass_log_independence_degeneracy_router.py
docs/monograph/prime-matrix-halfclass-log-independence-degeneracy-router.md
docs/monograph/prime-matrix-halfclass-log-independence-degeneracy-router.json
data/prime-matrix-halfclass-log-independence-degeneracy-ledger.json
```

本步继续下钻

```text
QuadraticTwistPairCharacterOrbitLockExclusionOrColumnCRTPDEC
```

对非零 residue `a` 记

```text
S_a(P)={ell prime: ell<=P^2, ell!=P, ell=a mod P},
theta_a=sum_{ell in S_a(P)} log ell.
```

若 `a!=b` 且 `theta_a=theta_b`，则

```text
prod_{ell in S_a(P)} ell = prod_{ell in S_b(P)} ell.
```

唯一分解强迫两个素数支撑完全相同；但不同 residue 支撑互不相交，所以只能同时为空。于是 `P>=7` 时，punctured 半类精确平铺

```text
theta(P^2;P,a0*u)=c  for all u in Q, u!=1
```

只能退化为

```text
c=0
S_{a0*u}(P)=empty  for all u in Q, u!=1.
```

当前读数：

```text
log_prime_product_independence_closed=true
positive_exact_punctured_flatness_excluded=true
orbit_lock_routed_to_zero_support_degeneracy=true
punctured_halfclass_zero_support_degeneracy_excluded=false
row_column_unconditional_closed=false
```

最新活动基更新为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
 OR ((QuadraticHalfClassSquareScaleBiasMarginTheorem
      OR EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale)
     AND PuncturedHalfClassZeroSupportDegeneracyExclusionOrColumnCRTPDEC))
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本步关闭的是“精确全配对轨道锁还能保持正平铺”的误出口。剩余最窄接口是排斥 punctured 半类全零支撑退化，或将它登记并排斥为 ColumnCRT/PDEC/moving-family 出口。行/列命题仍未无条件闭合。

## 115. Half-class single-residue capacity router

新增文件

```text
experiments/prime_matrix_halfclass_single_residue_capacity_router.py
docs/monograph/prime-matrix-halfclass-single-residue-capacity-router.md
docs/monograph/prime-matrix-halfclass-single-residue-capacity-router.json
data/prime-matrix-halfclass-single-residue-capacity-ledger.json
```

本步继续下钻

```text
PuncturedHalfClassZeroSupportDegeneracyExclusionOrColumnCRTPDEC
```

若同一二次半类 `H_s` 除缺孔外全无 `P^2` 内素数到达，则该半类全部 Chebyshev 质量只能落在一个 residue。固定 residue 在 `P^2` 前至多有 `P` 个候选位置，故

```text
theta(P^2;P,a) <= 2P log P.
```

因此该退化只能发生在

```text
Theta_s(P) <= 2P log P
```

的容量失败情形。用二次角色投影写为：

```text
min_s Theta_s(P)=(T0(P)-|T_chi(P)|)/2,
T0(P)*(1-|T_chi(P)|/T0(P)) > 4P log P
```

即可排除该退化。

当前读数：

```text
single_residue_deterministic_capacity_closed=true
zero_support_degeneracy_implies_capacity_failure_closed=true
quadratic_halfclass_mass_beats_single_residue_capacity_proved=false
row_column_unconditional_closed=false
```

有限诊断 `7<=P<=1000` 中，粗容量门只在 `P=7,11,13` 不通过；从 `P>=17` 开始最小半类质量/单 residue 容量比为 `1.284236511887034`。实际支撑退化数为 `0`。该有限读数只用于定位，不作为无限证明输入。

最新活动基更新为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
 OR ((QuadraticHalfClassSquareScaleBiasMarginTheorem
      OR EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale)
     AND QuadraticHalfClassMassBeatsSingleResidueCapacityAtP2))
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本步关闭的是“punctured 半类全零支撑仍是纯支撑语言”的误出口。剩余最窄接口是证明二次半类总 Chebyshev 质量击穿单 residue 容量，或将容量失败登记并排斥为 ColumnCRT/PDEC/moving-family 出口。行/列命题仍未无条件闭合。

## 116. Half-class capacity margin factorization router

新增文件

```text
experiments/prime_matrix_halfclass_capacity_margin_factorization_router.py
docs/monograph/prime-matrix-halfclass-capacity-margin-factorization-router.md
docs/monograph/prime-matrix-halfclass-capacity-margin-factorization-router.json
data/prime-matrix-halfclass-capacity-margin-factorization-ledger.json
```

本步继续下钻

```text
QuadraticHalfClassMassBeatsSingleResidueCapacityAtP2
```

半类容量门

```text
min_s Theta_s(P)>2P log P
```

等价于二次投影缺口门：

```text
1-|T_chi(P)|/T0(P) > 4P log P / T0(P).
```

若同时有主质量下界

```text
T0(P)>=c0(P)P^2,
```

则足以证明

```text
1-|T_chi(P)|/T0(P) > 4 log P/(c0(P)P).
```

所以持久失败不再是普通半类偏置，而是二次投影接近主质量到 `logP/P` 级的极端异常。

当前读数：

```text
projection_gap_equivalence_closed=true
log_over_p_threshold_reduction_closed=true
quadratic_projection_gap_beats_threshold_proved=false
row_column_unconditional_closed=false
```

有限诊断 `7<=P<=1000` 中，容量门失败模数仍为 `P=7,11,13`；从 `P>=17` 开始，实际缺口/所需缺口最小比值为 `1.2842365118870342`。该有限读数只用于定位，不作为无限证明输入。

最新活动基更新为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
 OR ((ChebyshevPrincipalMassLowerBoundAtP2
      AND (QuadraticHalfClassSquareScaleBiasMarginTheorem
           OR EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale
           OR QuadraticProjectionGapBeatsLogOverPThresholdAtSquareScale))))
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本步关闭的是“容量门仍是总质量语言”的误出口。剩余最窄接口是证明二次投影缺口击穿 `4P log P/T0`，或将 ultra-near-one 二次投影缺陷登记并排斥为 ColumnCRT/PDEC/moving-family 出口。行/列命题仍未无条件闭合。

## 117. Quadratic projection large splitting router

新增文件

```text
experiments/prime_matrix_quadratic_projection_large_splitting_router.py
docs/monograph/prime-matrix-quadratic-projection-large-splitting-router.md
docs/monograph/prime-matrix-quadratic-projection-large-splitting-router.json
data/prime-matrix-quadratic-projection-large-splitting-ledger.json
```

本步继续下钻

```text
QuadraticProjectionGapBeatsLogOverPThresholdAtSquareScale
```

把二次投影缺口阈值改写为少数半类质量门：

```text
1-|T_chi(P)|/T0(P) > 4P log P/T0(P)
<=> min_s Theta_s(P)>2P log P.
```

再精确拆分

```text
Theta_s(P)=L_s(P)+G_s(P),
L_s(P)=sum_{ell<P, chi_P(ell)=s} log ell,
G_s(P)=sum_{P<ell<=P^2, chi_P(ell)=s} log ell.
```

低 CRT 层满足平凡上界

```text
L_+(P)+L_-(P)=theta(P-1)<=P log P<2P log P.
```

所以低轮/有限 CRT 相位层可以被反例允许的 `2P log P` 少数质量预算完全吸收，不能单独推出全局矛盾。若容量门失败，则某个半类在大素数层已经满足 `G_s(P)<=2P log P`；反过来，若证明 `min_s G_s(P)>2P log P`，容量门立即闭合。

当前读数：

```text
minority_mass_equivalence_closed=true
low_crt_capacity_insufficiency_closed=true
large_prime_quadratic_splitting_mass_proved=false
row_column_unconditional_closed=false
```

有限诊断 `7<=P<=1000` 中，容量门和大分裂门失败模数均为 `P=7,11,13`；从 `P>=17` 开始，大素数层少数质量/所需质量最小比值为 `1.2504140082035853`。该有限读数只用于定位，不作为无限证明输入。

最新活动基更新为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
 OR ((ChebyshevPrincipalMassLowerBoundAtP2
      AND (QuadraticHalfClassSquareScaleBiasMarginTheorem
           OR EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale
           OR LargePrimeQuadraticSplittingMinorityMassBeatsTwoPLogPAtSquareScale
           OR UltraNearOneQuadraticProjectionDefectToLargeSplittingPDECOrSiegelPacket))))
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本步关闭的是“低 CRT 周期结构本身足以排斥 ultra-near-one 投影”的误出口。剩余最窄接口是证明大素数二次分裂少数半类质量超过 `2P log P`，或把长期失败登记为大分裂荒漠/Siegel/ColumnCRT-PDEC 出口。行/列命题仍未无条件闭合。

## 118. Large splitting beta-gap router

新增文件

```text
experiments/prime_matrix_large_splitting_beta_gap_router.py
docs/monograph/prime-matrix-large-splitting-beta-gap-router.md
docs/monograph/prime-matrix-large-splitting-beta-gap-router.json
data/prime-matrix-large-splitting-beta-gap-ledger.json
```

本步继续下钻

```text
LargePrimeQuadraticSplittingMinorityMassBeatsTwoPLogPAtSquareScale
```

定义高区间半类质量与投影：

```text
G_s(P)=sum_{P<ell<=P^2, chi_P(ell)=s} log ell,
H0=G_+(P)+G_-(P),
Hchi=G_+(P)-G_-(P).
```

大分裂门等价于

```text
min_s G_s(P)>2P log P
<=> 1-|Hchi|/H0 > 4P log P/H0.
```

若显式公式给出预算

```text
|Hchi|/H0 <= R_beta(P)+E_zero(P),
R_beta(P)=(P^(2 beta)-P^beta)/(beta H0),
```

则足以证明

```text
R_beta(P)+E_zero(P)<1-4P log P/H0.
```

无剩余零包的实零模型中，临界 `delta=1-beta` 满足

```text
R_(1-delta)(P)=1-4P log P/H0,
```

且在 `H0~P^2` 下为 `delta_crit~2/P`。因此持久失败不再是普通二次半类偏置，而是实零贴近到 `1/P` 级，或非实零/端点/素数幂残差同向相干吃掉同一 slack。

当前读数：

```text
high_projection_equivalence_closed=true
beta_gap_critical_scale_identified=true
beta_gap_and_zero_packet_budget_proved=false
row_column_unconditional_closed=false
```

有限诊断 `7<=P<=1000` 中，大分裂门失败模数仍为 `P=7,11,13`；从 `P>=17` 开始，高区间少数质量/所需质量最小比值为 `1.2504140082035853`；从 `P>=101` 开始，临界 `P(1-beta)` 约在 `2.2492763319844737` 到 `2.7065999766476923` 之间。该读数只用于定位，不作为无限证明输入。

最新活动基更新为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
 OR ((ChebyshevPrincipalMassLowerBoundAtP2
      AND (QuadraticHalfClassSquareScaleBiasMarginTheorem
           OR EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale
           OR (SelfContainedEffectivePrimeModulusQuadraticBetaGapAtScaleOneOverP
               AND NonrealZeroPacketResidualBelowLargeSplittingSlackAtP2)
           OR UltraCloseRealZeroOrCoherentZeroPacketLargeSplittingPDEC))))
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本步关闭的是“普通低轮或常数级二次偏置分析仍能继续压缩”的误出口。剩余最窄接口是有效 `1/P` 级 beta-gap 与非实零包残差预算，或把长期失败登记为超近实零/相干零包 PDEC/Siegel 出口。行/列命题仍未无条件闭合。

## 119. Beta-gap Page sparsity router

新增文件

```text
experiments/prime_matrix_beta_gap_page_sparsity_router.py
docs/monograph/prime-matrix-beta-gap-page-sparsity-router.md
docs/monograph/prime-matrix-beta-gap-page-sparsity-router.json
data/prime-matrix-beta-gap-page-sparsity-ledger.json
```

本步继续下钻

```text
SquareScaleQuadraticBetaGapAndZeroPacketResidualBudgetAtP2
```

上一层把实零失败压到

```text
beta_P > 1 - C(P)/P
```

的超近区域。若接受 Page/Landau 例外零唯一性输入

```text
LandauPageExceptionalZeroUniquenessWithAdaptedConstants:
  q<=Q 中至多一个 primitive 实角色零点满足 beta>1-c_Page/logQ,
```

并且在某个范围内 `C(P)<=C_*`，则当

```text
P > C_* logQ / c_Page,  P<=Q
```

时有

```text
1-C(P)/P > 1-c_Page/logQ.
```

因此这些 `1/P` 级超近实零载体全部落入同一个 Page 唯一性区域，任意 `q<=Q`
范围中至多出现一个。结论是：

```text
|E(Q) cap ((C_*/c_Page)logQ,Q]| <= 1
|E(Q)|/pi(Q) <= (1+pi((C_*/c_Page)logQ))/pi(Q)=o(1)
```

这排除了固定周期或正密度 CRT 反例族靠“多实零载体复现”维持大分裂失败的形态。

当前读数：

```text
page_region_inclusion_algebra_closed=true
page_uniqueness_constants_internalized=false
moving_singleton_carrier_excluded=false
nonreal_zero_packet_residual_proved=false
row_column_unconditional_closed=false
```

最新活动基更新为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
 OR ((ChebyshevPrincipalMassLowerBoundAtP2
      AND (QuadraticHalfClassSquareScaleBiasMarginTheorem
           OR EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale
           OR ((LandauPageExceptionalZeroUniquenessWithAdaptedConstants
                AND PageExceptionalSingletonCarrierExclusionOrMovingFamilyPDEC)
               AND NonrealZeroPacketResidualBelowLargeSplittingSlackAtP2)
           OR (SelfContainedEffectivePrimeModulusQuadraticBetaGapAtScaleOneOverP
               AND NonrealZeroPacketResidualBelowLargeSplittingSlackAtP2)
           OR MovingPageSingletonCarrierPDECOrCoherentZeroPacket))))
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本步关闭的是“多载体 Page 例外零可以按固定 CRT 周期稳定复现”的误出口。它没有内化 Page 常数，也没有排斥每个尺度一个的 moving singleton 例外载体，更没有证明非实零包/端点残差低于大分裂 slack。行/列命题仍未无条件闭合。

## 120. Terminal-row CRT atom router

新增文件

```text
experiments/prime_matrix_terminal_row_crt_atom_router.py
docs/monograph/prime-matrix-terminal-row-crt-atom-router.md
docs/monograph/prime-matrix-terminal-row-crt-atom-router.json
data/prime-matrix-terminal-row-crt-atom-ledger.json
```

本步吸收用户给出的 `P=5,7` 终端例子。对 `P=5`：

```text
M_{<=5}=30
last_row_units=[23]
next_row_units=[29]
23 mod (2,3,5) = (1,2,3)
29 mod (2,3,5) = (1,2,4)
```

对 `P=7`：

```text
M_{<=7}=210
last_row_units=[43,47]
next_row_units=[53]
```

`43,47,53` 在 `(2,3,5,7)` 下也全为非零坐标。因此“它们是假合数并被 `<=P`
小素数整除”的假设直接与 CRT 坐标矛盾。

可推广的原子级引理为：

```text
若 1<n<p_next^2 且 gcd(n,M_{<=P})=1，则 n 为素数。
```

因为若 `n` 合成而无 `<=P` 素因子，其最小素因子至少是下一素数 `p_next`，从而
`n>=p_next^2`，矛盾。

当前读数：

```text
specified_terminal_atoms_small_factor_absorption_impossible=true
terminal_sqrt_gate=true
complete_wheel_symmetry_identity=true
full_wheel_symmetry_localizes_to_terminal_rows=false
global_terminal_row_no_missing_prime_proved=false
row_column_unconditional_closed=false
```

这一步关闭的是“指定终端原子可被小素数吸收”的误出口。真正全局化仍需证明目标短行中必有
`gcd(n,M_{<=P})=1` 的 reduced atom；完整 CRT 周期均匀和反射不自动给这个局部存在性。
最新剩余回到：

```text
TerminalRowReducedResidueExistenceOrLocalizedPCRTTransfer
PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2OrAPZeroPacketFrontier
PageExceptionalSingletonCarrierOrNonrealZeroPacketResidualBudget
```

行/列命题仍未无条件闭合。

### 1.171 Phi-LPF pointwise signed value table frontier 更新

新增机器证书：

```text
experiments/prime_matrix_phi_lpf_pointwise_signed_value_table_frontier_router.py
data/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-ledger.json
docs/monograph/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.md
docs/monograph/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json
```

同步读数为：

```text
phi_lpf_support_and_capacity_imported=true
bucket_signed_law_downstream_imported=true
unit_seed_square_base_boundary_imported=true
common_packet_self_proof_blocked=true
pointwise_phi_lpf_bucket_signed_value_table_proved=false
seed_cycle_cut_input_proved=false
acyclic_same_set_scope_match_proved=false
new_explicit_joint_constructor_formula_artifact_present=false
row_column_unconditional_closed=false
```

actual-load 含义是：Phi/LPF 已经支付 support、capacity、candidate-row 与 square-base/root
字段。若要走 direct 旁路，必须把
`PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward` 作为真正新的
prepushforward signed value 工件提交，逐 `(p,m)` 给 signed coefficient、local factor、
alpha/delta side、ExactUV 输出和求和恒等式。若沿现有 signed-source/source-origin 链展开，
会回到已登记的非证明固定点。

因此最新可攻输入保持为：

```text
PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
```

非循环破环替代为：

```text
AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
```

同时仍需独立关闭：

```text
ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward AND
PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward
ExplicitModelGapAndFiniteDPRCLedger
RatePreservationLedger_FOR_moving_atom_packet
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

行/列命题仍未无条件闭合。

### 1.172 Phi-LPF rough cofactor ordered factorization coherence 更新

新增机器证书：

```text
experiments/prime_matrix_phi_lpf_rough_cofactor_ordered_factorization_coherence_router.py
data/prime-matrix-phi-lpf-rough-cofactor-ordered-factorization-coherence-ledger.json
docs/monograph/prime-matrix-phi-lpf-rough-cofactor-ordered-factorization-coherence-router.md
docs/monograph/prime-matrix-phi-lpf-rough-cofactor-ordered-factorization-coherence-router.json
```

同步读数为：

```text
phi_lpf_support_and_capacity_imported=true
unsigned_cofactor_split_imported=true
rough_cofactor_ordered_factorization_coherence_proved=true
rough_cofactor_step_local_factor_update_law_proved=false
pointwise_phi_lpf_bucket_signed_value_table_proved=false
row_column_unconditional_closed=false
```

actual-load 含义是：固定 LPF owner prime `p` 后，每个 p-rough cofactor `m` 由最小素因子
剥离得到唯一非降素因子词。每个前缀仍是 p-rough，且 `p*prefix<=p*m<=N`，所以路径不会
离开同一 owner bucket；非降 LPF 词也排除了同一 cofactor 的排列重复路径。`N=10000`
审计给出 `8770` 个 support keys、`21986` 个 ordered factor steps、最大深度 `12`，
全部前缀一致性通过。

因此 `PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward` 可从最新剩余基中
移除。但这仍只是无符号路径事实，不产生 signed coefficient、orientation parity 或 local
factor 乘子。最新直接主攻变为：

```text
PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward
```

并行仍需：

```text
PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
ExplicitModelGapAndFiniteDPRCLedger
RatePreservationLedger_FOR_moving_atom_packet
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

行/列命题仍未无条件闭合。

### 1.173 Phi-LPF step local factor update frontier 更新

新增机器证书：

```text
experiments/prime_matrix_phi_lpf_step_local_factor_update_frontier_router.py
data/prime-matrix-phi-lpf-step-local-factor-update-frontier-ledger.json
docs/monograph/prime-matrix-phi-lpf-step-local-factor-update-frontier-router.md
docs/monograph/prime-matrix-phi-lpf-step-local-factor-update-frontier-router.json
```

同步读数为：

```text
ordered_lpf_edge_path_imported=true
step_update_reduced_to_edge_multiplier_table=true
edge_signed_multiplier_table_proved=false
rough_cofactor_step_local_factor_update_law_proved=false
pointwise_phi_lpf_bucket_signed_value_table_proved=false
row_column_unconditional_closed=false
```

actual-load 含义是：ordered LPF path 已经固定后，剩余不再是 cofactor 路径选择问题。
对每个 owner bucket 内的边 `(p,prefix,q,prefix*q)`，必须在推前前正向给出 signed
multiplier、orientation parity 增量、local factor 非零或命名回流、alpha/delta branch
与 ExactUV 转移，并证明沿路径乘积就是该 Phi-LPF support key 的 signed coefficient。

样本审计中 `N=10000` 给出 `8770` 个 support keys、`21986` 个 ordered edge occurrences、
最大 LPF 深度 `12`。这些数字只验证支撑路径和字段容量；它们同时显示 distinct-edge 与
edge-occurrence 两种 sign-shadow 自由度，不能从 LPF/Phi 无符号计数推出 signed 表。

因此最新直接主攻收窄为：

```text
PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward
```

条件生成器为：

```text
ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn
ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn
PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward
```

并行替代仍是直接提交
`PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward`。行/列命题仍未
无条件闭合。

### 1.174 Phi-LPF first-edge slab frontier 更新

新增机器证书：

```text
experiments/prime_matrix_phi_lpf_first_edge_slab_frontier_router.py
data/prime-matrix-phi-lpf-first-edge-slab-frontier-ledger.json
docs/monograph/prime-matrix-phi-lpf-first-edge-slab-frontier-router.md
docs/monograph/prime-matrix-phi-lpf-first-edge-slab-frontier-router.json
```

同步读数为：

```text
edge_signed_multiplier_table_imported=true
edge_table_split_into_first_seed_and_internal_transition=true
first_edge_phi_fiber_formula_proved=true
semiprime_first_edge_signed_seed_table_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
edge_signed_multiplier_table_proved=false
row_column_unconditional_closed=false
```

actual-load 含义是：逐 edge signed multiplier 表有一个强制 first/internal 分解。每条
ordered LPF path 的第一边是 `(p,1,q,q)`，对应 semiprime composite `p*q` 和一个
q-rough continuation fiber；后续边才是 `prefix>1` 的内部 prime-adjoin transition。
第一边 occurrence mass 有精确 Phi 公式：

```text
mass_N(p,q)=Phi(floor(N/(p*q)),q)
```

样本 `N=10000` 中 first-edge 类型数为 `2625`，first-edge occurrence 数为 `8770`，
internal transition occurrence 数为 `13216`，且 first-edge Phi 纤维公式总和正好等于
support keys。这个公式只支付支撑/纤维质量，不给 semiprime first seed signed value，也
不给内部 transition 的非零 local factor。

因此最新直接主攻拆成：

```text
PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward
PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
```

并行替代仍是逐点 signed value table、完整 branch trace 或 atomic trace。行/列命题仍未
无条件闭合。

### 1.175 Phi-LPF semiprime seed diagonal frontier 更新

新增机器证书：

```text
experiments/prime_matrix_phi_lpf_semiprime_seed_diagonal_frontier_router.py
data/prime-matrix-phi-lpf-semiprime-seed-diagonal-frontier-ledger.json
docs/monograph/prime-matrix-phi-lpf-semiprime-seed-diagonal-frontier-router.md
docs/monograph/prime-matrix-phi-lpf-semiprime-seed-diagonal-frontier-router.json
```

同步读数为：

```text
semiprime_first_edge_signed_seed_target_imported=true
diagonal_offdiagonal_support_split_proved=true
diagonal_square_base_private_signed_escape_removed=true
diagonal_common_packet_signed_source_proved=false
offdiagonal_ordered_semiprime_signed_seed_table_proved=false
semiprime_first_edge_signed_seed_table_proved=false
row_column_unconditional_closed=false
```

actual-load 含义是：semiprime first-edge seed 仍不是单一黑箱。diagonal `p=q` 正是
square-base root `(p,p)`；既有 square-base source packet reduction 已经排除其私有 signed
出口，但它回到 `PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket` 后仍未闭合。
offdiagonal `p<q` 则是真正新的 ordered semiprime first-seed 表口。

样本 `N=10000` 中 diagonal 类型 `25` 个、offdiagonal 类型 `2600` 个；occurrence 分解为
`3302 + 5468 = 8770`。因此 diagonal 不是主要类型复杂度来源，最新最窄主攻为：

```text
PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward
```

配套仍需：

```text
PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket
PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
```

并行替代仍是逐点 signed table、branch trace、atomic trace、seed cycle-cut、same-set PDEC
或 new joint formula。行/列命题仍未无条件闭合。

### 1.176 Phi-LPF offdiagonal semiprime seed tuple-fields 更新

新增机器证书：

```text
experiments/prime_matrix_phi_lpf_offdiagonal_semiprime_seed_tuple_fields_router.py
data/prime-matrix-phi-lpf-offdiagonal-semiprime-seed-tuple-fields-ledger.json
docs/monograph/prime-matrix-phi-lpf-offdiagonal-semiprime-seed-tuple-fields-router.md
docs/monograph/prime-matrix-phi-lpf-offdiagonal-semiprime-seed-tuple-fields-router.json
```

同步读数为：

```text
offdiagonal_seed_target_imported=true
offdiagonal_source_tuple_bijection_proved=true
offdiagonal_phi_tail_fiber_mass_proved=true
offdiagonal_unsigned_tuple_fields_closed=true
offdiagonal_signed_seed_formula_proved=false
offdiagonal_orientation_parity_law_proved=false
offdiagonal_exactuv_fixed_pair_return_ledger_proved=false
offdiagonal_ordered_semiprime_signed_seed_table_proved=false
row_column_unconditional_closed=false
```

actual-load 含义是：offdiagonal `p<q` first seed 的 LPF/Phi 部分已经不能再作为黑箱。
每个 occurrence 唯一写成

```text
(owner_p, first_rough_prime_q, q_rough_tail_t),  p<q,
```

且总质量精确为

```text
sum_{p<q} Phi(floor(N/(p*q)), q).
```

样本 `N=10000` 中 offdiagonal 类型为 `2600` 个，tuple occurrences 为 `5468` 个，
其中 `tail=1` 的纯 semiprime occurrence 为 `2600` 个，`tail>1` 的 continuation
occurrence 为 `2868` 个。这个账本关闭的是 owner、first prime、tail、type key 与
Phi fiber mass；它不产生 signed seed value、orientation parity、branch side、local factor
或 ExactUV return tag。

因此最新直接主攻变为：

```text
PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward
```

配套仍需：

```text
PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket
```

并行替代仍是逐点 signed table、完整 branch trace、atomic trace、seed cycle-cut、
same-set PDEC 或 new joint formula。行/列命题仍未无条件闭合。

### 1.177 Phi-LPF offdiagonal pure semiprime seed atom 更新

新增机器证书：

```text
experiments/prime_matrix_phi_lpf_offdiagonal_pure_semiprime_seed_atom_router.py
data/prime-matrix-phi-lpf-offdiagonal-pure-semiprime-seed-atom-ledger.json
docs/monograph/prime-matrix-phi-lpf-offdiagonal-pure-semiprime-seed-atom-router.md
docs/monograph/prime-matrix-phi-lpf-offdiagonal-pure-semiprime-seed-atom-router.json
```

同步读数为：

```text
offdiagonal_source_tuple_signed_seed_target_imported=true
pure_semiprime_pair_seed_atom_bijection_proved=true
tail_nonunit_reduced_to_internal_transition_lift=true
tail_lift_phi_minus_one_mass_formula_proved=true
pure_semiprime_pair_signed_seed_atom_proved=false
offdiagonal_source_tuple_signed_seed_formula_proved=false
row_column_unconditional_closed=false
```

actual-load 含义是：offdiagonal source tuple signed formula 仍可再拆一层。每个
ordered type `(p,q), p<q` 恰有一个 `tail=1` 的 pure semiprime pair seed atom，即
composite `p*q` 本身；所有 `tail>1` 的 q-rough continuation occurrence 不构成新的
first seed，只能由同一 pure atom 加 internal prime-adjoin transition lift 支付。每个
`(p,q)` 的 tail-lift mass 为：

```text
Phi(floor(N/(p*q)), q)-1.
```

样本 `N=10000` 中 pure atoms 为 `2600` 个，tail-lift occurrences 为 `2868` 个，
合计仍为上一层 offdiagonal occurrences `5468`。因此最新直接主攻进一步收窄为：

```text
PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward
```

配套仍需：

```text
PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket
```

本步没有给出 pure pair signed seed value；它只关闭 pure atom/tail lift 的无符号分解与
`Phi-1` 质量公式。行/列命题仍未无条件闭合。

### 1.178 Phi-LPF pure pair Ferrers support 更新

新增机器证书：

```text
experiments/prime_matrix_phi_lpf_pure_pair_ferrers_support_router.py
data/prime-matrix-phi-lpf-pure-pair-ferrers-support-ledger.json
docs/monograph/prime-matrix-phi-lpf-pure-pair-ferrers-support-router.md
docs/monograph/prime-matrix-phi-lpf-pure-pair-ferrers-support-router.json
```

同步读数为：

```text
pure_pair_signed_atom_target_imported=true
pure_pair_ferrers_support_rule_proved=true
pure_pair_degree_ledger_proved=true
support_graph_signed_kernel_emission_proved=false
two_prime_signed_interaction_kernel_proved=false
pure_semiprime_pair_signed_seed_atom_proved=false
row_column_unconditional_closed=false
```

actual-load 含义是：offdiagonal pure pair atom 的支撑已经完全显式化为二素数 Ferrers 图。
左侧是 owner primes `p<=sqrt(N)`，右侧是 first primes `q`，边条件为：

```text
p<q<=N/p.
```

随着 `p` 增大，邻域 `N(p)={q prime: p<q<=N/p}` 嵌套下降；left/right degree 和总边数
都由 prime table 与 `floor(N/p)` 机械决定。样本 `N=10000` 中 left owner layers 为
`25`，right prime vertices 为 `668`，pure pair edges 为 `2600`，Ferrers 嵌套和度数
恒等式均通过。

因此 pure atom 剩余不再是支撑/度数/容量问题，而是每条 `(p,q)` 边上的 signed 交互：

```text
PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward
```

配套仍需 orientation parity、ExactUV return、internal transition 与 common packet。本步不从
Ferrers 支撑图推出 sign 或 local factor。行/列命题仍未无条件闭合。

### 1.179 Phi-LPF two-prime ordered no-swap 更新

新增机器证书：

```text
experiments/prime_matrix_phi_lpf_two_prime_ordered_no_swap_router.py
data/prime-matrix-phi-lpf-two-prime-ordered-no-swap-ledger.json
docs/monograph/prime-matrix-phi-lpf-two-prime-ordered-no-swap-router.md
docs/monograph/prime-matrix-phi-lpf-two-prime-ordered-no-swap-router.json
```

同步读数为：

```text
two_prime_signed_kernel_target_imported=true
lpf_owner_ordered_no_swap_identity_proved=true
product_symmetry_signed_emission_proved=false
edge_local_two_prime_signed_formula_proved=false
two_prime_signed_interaction_kernel_proved=false
row_column_unconditional_closed=false
```

actual-load 含义是：two-prime signed kernel 不能从 `p*q=q*p` 的交换对称里取 sign。
LPF owner source domain 只接纳 canonical ordered edge `(p,q)`，其中 `p<q`；
reverse edge `(q,p)` 不属于同一 source domain，也不能作为 cancellation partner。
样本 `N=10000` 中 ordered edges 为 `2600`，distinct unordered semiprime products 也是
`2600`，reverse edges 为 `0`，duplicates 为 `0`。

因此 product symmetry 在 signed kernel 之前已经被 LPF owner 顺序擦除。最新直接主攻为：

```text
PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward
```

配套仍需 orientation parity、ExactUV return、internal transition 与 common packet。本步只删除
swap-symmetry 伪出口，不给出 edge-local signed formula。行/列命题仍未无条件闭合。

### 1.180 Phi-LPF edge-local two-prime field-cut 更新

新增机器证书：

```text
experiments/prime_matrix_phi_lpf_edge_local_two_prime_field_cut_router.py
data/prime-matrix-phi-lpf-edge-local-two-prime-field-cut-ledger.json
docs/monograph/prime-matrix-phi-lpf-edge-local-two-prime-field-cut-router.md
docs/monograph/prime-matrix-phi-lpf-edge-local-two-prime-field-cut-router.json
```

同步读数为：

```text
edge_local_formula_target_imported=true
edge_local_closed_unsigned_label_ledger_proved=true
edge_label_bijection_proved=true
lpf_bucket_product_fields_proved=true
ferrers_rank_degree_fields_proved=true
edge_atom_multiplicity_one_proved=true
signed_atom_field_table_proved=false
orientation_parity_branch_side_proved=false
exactuv_fixed_pair_return_tag_proved=false
edge_local_signed_interaction_formula_proved=false
row_column_unconditional_closed=false
```

actual-load 含义是：edge-local formula-or-return 中由 LPF/Phi/Ferrers 可支付的部分已经
全部固定为无符号 edge label。每条 canonical `(p,q)` edge 的 owner、product、LPF bucket、
Ferrers row/column rank-degree 与 atom multiplicity 均闭合。样本 `N=10000` 中 canonical
edges、unique labels 与 unique products 都是 `2600`，LPF/row degree/column degree/atom
multiplicity 审计全部为 true。

因此剩余不再是支撑或容量问题，而是逐 edge signed atom fields 或命名 return tag：

```text
PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward
```

配套仍需 orientation parity、ExactUV return、internal transition 与 common packet。本步
不从 LPF/Phi/Ferrers label 推出 sign/local factor。行/列命题仍未无条件闭合。

### 1.181 Phi-LPF edge-local signed atom trace-sync 更新

新增机器证书：

```text
experiments/prime_matrix_phi_lpf_edge_local_signed_atom_trace_sync_router.py
data/prime-matrix-phi-lpf-edge-local-signed-atom-trace-sync-ledger.json
docs/monograph/prime-matrix-phi-lpf-edge-local-signed-atom-trace-sync-router.md
docs/monograph/prime-matrix-phi-lpf-edge-local-signed-atom-trace-sync-router.json
```

同步读数为：

```text
signed_atom_fields_target_imported=true
closed_unsigned_edge_labels_imported=true
same_trace_key_requirement_closed=true
named_return_matrix_closed=true
atomic_trace_reduced_to_signed_payload=true
signed_lane_cycle_imported=true
signed_lane_self_proof_eliminated=true
branch_trace_self_proof_eliminated=true
new_primitive_payload_or_trace_artifact_present=false
edge_local_signed_atom_fields_proved=false
row_column_unconditional_closed=false
```

actual-load 含义是：edge-local signed atom fields 必须在同一 pre-Cauchy trace key 上
一次性给出 signed value、local factor、orientation/branch side、alpha/delta payload、
ExactUV fixed pair 与 source row。若这些字段缺失、冲突、零因子、超预算或后验读取，
则进入 named return/PDEC，而不是保留匿名 signed 缺口。样本 `N=10000` 中需要 `2600`
个 edge trace packets，对应 `15600` 个开放 signed slots。

现有 branch-trace/atomic-trace 线已经由 signed-lane cycle closure 证明不能自证。最新
直接主攻为：

```text
NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact
```

并行出口为 terminal descent、PDEC scope、逐点 signed table 与 ExactUV。该步只关闭
same-trace-key 与 named return 路由，不给 signed value/local factor 公式。行/列命题仍未
无条件闭合。

### 1.182 Phi-LPF new-payload source-atom alignment sync 更新

新增机器证书：

```text
experiments/prime_matrix_phi_lpf_new_payload_source_atom_alignment_sync_router.py
data/prime-matrix-phi-lpf-new-payload-source-atom-alignment-sync-ledger.json
docs/monograph/prime-matrix-phi-lpf-new-payload-source-atom-alignment-sync-router.md
docs/monograph/prime-matrix-phi-lpf-new-payload-source-atom-alignment-sync-router.json
```

同步读数为：

```text
phi_lpf_trace_sync_imported=true
unsigned_lpf_data_cannot_pay_signed_payload=true
strict_new_payload_alignment_imported=true
phi_lpf_new_payload_independent_terminal_present=false
phi_lpf_new_payload_reduced_to_source_rank_atom=true
actual_source_domain_entropy_proved=false
complete_primitive_emitter_key_partition_proved=false
fixed_key_exact_uv_local_multiplicity_proved=false
pointwise_phi_lpf_bucket_signed_value_table_proved=false
row_column_unconditional_closed=false
```

actual-load 含义是：上一层的 `NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact`
不能作为新的独立终点。LPF/Phi/Ferrers 已支付的是无符号 support/capacity/tuple/fiber
标签；signed value、local factor、orientation 与 alpha/delta payload 仍必须来自同一
pre-Cauchy actual source。若 new-payload 不是 signed-lane 环内改名，就必须提交：

```text
ActualPreCauchySourceDomainAbsoluteEntropyLedger
CompletePrimitiveEmitterKeyPartitionLedger
FixedKeyExactUVLocalMultiplicityO1Ledger
```

或转入 terminal descent、PDEC scope、逐点 signed table。当前第一直接主攻为
`ActualPreCauchySourceDomainAbsoluteEntropyLedger`；ExactUV、模型、Rate 与 DStructure/Rankin
仍独立开放。行/列命题仍未无条件闭合。

## 132. Strict post-alpha terminal leaf latest noncycle sync router

新增文件

```text
experiments/prime_matrix_strict_post_alpha_terminal_leaf_latest_noncycle_sync_router.py
docs/monograph/prime-matrix-strict-post-alpha-terminal-leaf-latest-noncycle-sync-router.md
docs/monograph/prime-matrix-strict-post-alpha-terminal-leaf-latest-noncycle-sync-router.json
data/prime-matrix-strict-post-alpha-terminal-leaf-latest-noncycle-sync-ledger.json
```

本步把 post-alpha terminal leaf 的二选一继续同步到仓库已有更深前沿：

```text
AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NoncanonicalFullSComplementLegalClosureMode
-> AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
   OR (AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn
       AND IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed)
-> pair-energy/rate-packet/source-entropy fixed point
-> ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple
-> NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
   OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
-> TERMINAL-SOURCE-PAIR-JOINT macrocycle
```

因此 `NoncanonicalFullSComplementLegalClosureMode` 不再作为最深活动标签；普通 pair-energy、joint constructor 与 terminal descent 路线均不能作为非循环证明。当前严格内部非循环基为：

```text
(NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
OR ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab
OR FullSNonAPStrengthenedSourceAntiAtomForActualSource
OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate)
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻为 `NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact`；并行保留 actual-source 外环桥、PDEC same-set 作用域、ExactUV、模型余量、RatePreservation 与 DStructure/Rankin。行/列命题仍未无条件闭合。

## 133. Strict post-alpha noncycle to terminal three atoms sync router

新增文件

```text
experiments/prime_matrix_strict_post_alpha_noncycle_to_terminal_three_atoms_sync_router.py
docs/monograph/prime-matrix-strict-post-alpha-noncycle-to-terminal-three-atoms-sync-router.md
docs/monograph/prime-matrix-strict-post-alpha-noncycle-to-terminal-three-atoms-sync-router.json
data/prime-matrix-strict-post-alpha-noncycle-to-terminal-three-atoms-sync-ledger.json
```

本步把 c75 的 `NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact` 继续同步到更深前沿：branch trace、signed payload、common source declaration packet 与 signed-lane cycle 已共同说明该线不是非循环闭合点。当前 strict 自足全局前沿被压成三原子：

```text
AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
A1CleanBranchCanonicalSourceAdmission
ActualNoncanonicalCleanCoreMovingAtomExclusion
```

其中最窄直接主攻是：

```text
IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore
```

这一步只删除旧的 `NewExplicit...` 自回流主攻标签；没有证明 moving atom 排斥、canonical-lock、A1 admission 或 DStructure/Rankin 晋级门。

## 132. Strict post-antisplit alpha terminal leaf sync router

新增文件

```text
experiments/prime_matrix_strict_post_antisplit_alpha_terminal_leaf_sync_router.py
docs/monograph/prime-matrix-strict-post-antisplit-alpha-terminal-leaf-sync-router.md
docs/monograph/prime-matrix-strict-post-antisplit-alpha-terminal-leaf-sync-router.json
data/prime-matrix-strict-post-antisplit-alpha-terminal-leaf-sync-ledger.json
```

本步把上一节暴露的 `AlphaRowAnchorPhaseEmissionFormulaLedger` 继续同步到既有三腿回流和终端叶子前沿：

```text
PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate
-> AlphaRowAnchorPhaseEmissionFormulaLedger
   AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
   AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows

alpha/weight 两腿 -> PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve
rank/multiplicity 腿 -> 同一 primitive table
三腿合取 -> NonrecursivePointwisePrimitiveKernelTableConstructionWithoutTerminalReturn
-> ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple
-> signed-source fixed point
-> terminal leaf firewall
```

因此当前严格自足活动基更新为：

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
OR NoncanonicalFullSComplementLegalClosureMode)
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

这一步删除了“继续单攻 alpha/weight/rank 任一腿即可闭合”的误出口；行/列命题仍未无条件闭合。

## 121. Terminal-row square-phase bridge router

新增文件

```text
experiments/prime_matrix_terminal_row_square_phase_bridge_router.py
docs/monograph/prime-matrix-terminal-row-square-phase-bridge-router.md
docs/monograph/prime-matrix-terminal-row-square-phase-bridge-router.json
data/prime-matrix-terminal-row-square-phase-bridge-ledger.json
```

本步把上一节的终端行 reduced atom 存在性并入既有平方锚特殊相位线。对 `1<=r<P`：

```text
plus survivor  <=> gcd(P^2+r, M_<P)=1
minus survivor <=> gcd(P^2-r, M_<P)=1
plus full cover  <=> r=-P^2 mod q 的禁类覆盖 r=1..P-1
minus full cover <=> r= P^2 mod q 的禁类覆盖 r=1..P-1
```

因此末行或下一行的全缺失不是普通 CRT 全周期不均匀，而是 `P^2` 特殊相位启动长度 `P-1`
低筛覆盖块。既有 `square-phase Jacobsthal` 证书已经显示：全周期最大覆盖块 `<P-1`
的强路线失效，真正硬点是特殊相位避让，或把特殊相位命中登记为 `PDEC/SAE/ColumnCRT`。

当前读数：

```text
terminal_reduced_atom_equivalent_to_square_phase_survivor=true
terminal_full_cover_implies_special_long_block=true
uniform_jacobsthal_bound_suffices_but_rejected=true
global_special_phase_avoidance_proved=false
row_column_unconditional_closed=false
```

最新剩余：

```text
SquarePhaseSpecialPhaseLongBlockPDECExclusion
```

备选仍为：

```text
TwoSidedSquarePhaseLayeredWheelSurvivorLowerBound
PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2OrAPZeroPacketFrontier
```

本步关闭的是“从完整 CRT 周期对称性直接推出终端行局部矛盾”的跳步；行/列命题仍未无条件闭合。

## 122. Terminal-square downstream frontier sync router

新增文件

```text
experiments/prime_matrix_terminal_square_phase_downstream_frontier_sync_router.py
docs/monograph/prime-matrix-terminal-square-phase-downstream-frontier-sync-router.md
docs/monograph/prime-matrix-terminal-square-phase-downstream-frontier-sync-router.json
data/prime-matrix-terminal-square-phase-downstream-frontier-sync-ledger.json
```

本步不是新闭合证明，而是把上一节的终端行平方相位桥接同步到仓库中已经存在的更深前沿。
同步表确认：

```text
frontier_file_count=10
square_phase_longblock_synced_downstream=true
row_column_unconditional_closed=false
```

因此 `SquarePhaseSpecialPhaseLongBlockPDECExclusion` 应作为上游接口别名保留；它已经被
half-grid/boundary-word、no-slot phase-band、localized P-CRT/AP 零点包、global CRT signed-payload
等路线进一步细化。当前 consolidated 剩余基为：

```text
PageExceptionalSingletonCarrierOrNonrealZeroPacketResidualBudget
AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
ExplicitModelGapAndFiniteDPRCLedger
RatePreservationLedger_FOR_moving_atom_packet
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

这一步关闭的是前沿口径错位，不关闭行/列命题。下一步应直接攻击 consolidated 剩余基中的
AP 零点包、signed payload 或 same-set PDEC 输入。

## 123. Strict source declaration / payload / ExactUV unification router

新增文件

```text
experiments/prime_matrix_strict_source_declaration_payload_exactuv_unification_router.py
docs/monograph/prime-matrix-strict-source-declaration-payload-exactuv-unification-router.md
docs/monograph/prime-matrix-strict-source-declaration-payload-exactuv-unification-router.json
data/prime-matrix-strict-source-declaration-payload-exactuv-unification-ledger.json
```

本步把 strict 内部 source lane 的两个活动硬点合流：

```text
NoncircularAtomicBasisWordSignedCoefficientOriginIdentityBeforePushforward
ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
```

共同压到：

```text
PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket
```

该 packet 必须在 Cauchy/Phi/payment 前正向给出 actual noncanonical source declaration、primitive
summand rows、basis word/signed coefficient 来源恒等式、alpha/delta 推前前等式、source-domain
entropy、fixed exact `(u,v)` polylog fiber bound，以及缺声明、fiber collapse、entropy deficit、
符号冲突、local factor 为零、超预算、canonical 泄漏等命名回流。

当前读数：

```text
common_packet_proved=false
atomic_signed_payload_constructor_proved=false
actual_emitter_exact_uv_bounded_multiplicity_incidence_proved=false
row_column_unconditional_closed=false
```

这一步关闭的是 payload 线与 ExactUV 线之间的口径分裂；它没有提交共同 source declaration
packet，也不关闭 AP 零点包、same-set PDEC、模型余量、RatePreservation 或 DStructure/Rankin 门。
下一直接主攻对象为：

```text
PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket
```

## 124. Strict source declaration downstream sync router

新增文件

```text
experiments/prime_matrix_strict_source_declaration_downstream_sync_router.py
docs/monograph/prime-matrix-strict-source-declaration-downstream-sync-router.md
docs/monograph/prime-matrix-strict-source-declaration-downstream-sync-router.json
data/prime-matrix-strict-source-declaration-downstream-sync-ledger.json
```

本步把上一节的 common packet 继续同步到已有下游前沿。`PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket`
分成两条子线：

```text
signed/payload lane -> BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
ExactUV lane -> ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
```

关键判定是：普通 `ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRule` 继续展开会回到
signed-source 固定点；若要避免固定点，必须使用反分裂原子声明，把 rows formula、basis word/signed
coefficient pairing、alpha/delta payload 与 prepushforward identity 内置到同一 pre-Cauchy row 中。
已有 `atomic-joint-rows` 证书进一步把这个原子声明压到 built-in signed coefficient/pairing 闭式。

当前读数：

```text
downstream_sync_closed=true
built_in_signed_pairing_proved=false
actual_emitter_exact_uv_bounded_multiplicity_incidence_proved=false
common_packet_proved=false
row_column_unconditional_closed=false
```

因此 common packet 不再是一个未拆分黑箱。下一直接主攻是：

```text
BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
```

并行 ExactUV 子线仍需：

```text
ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
```

本步不关闭 AP 零点包、same-set PDEC、RatePreservation 或 DStructure/Rankin 门。

## 125. Strict signed lane cycle closure router

新增文件

```text
experiments/prime_matrix_strict_signed_lane_cycle_closure_router.py
docs/monograph/prime-matrix-strict-signed-lane-cycle-closure-router.md
docs/monograph/prime-matrix-strict-signed-lane-cycle-closure-router.json
data/prime-matrix-strict-signed-lane-cycle-closure-ledger.json
```

本步把 signed/payload 子线的下游链闭合成一个可审查环：

```text
PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket
-> BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
-> ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn
-> AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
-> NoncircularAtomicBasisWordSignedCoefficientOriginIdentityBeforePushforward
-> PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket
```

这说明 common packet、built-in pairing、branch trace、signed payload 与 origin identity 不能互相
自证。branch trace 的可见坐标链只给 row/word 坐标，不产生 orientation、local factor 或 signed
coefficient；origin identity 又通过 common packet 回到 signed 子线起点。

当前读数：

```text
signed_lane_cycle_closed=true
signed_lane_self_proof_eliminated=true
new_primitive_payload_or_trace_artifact_present=false
row_column_unconditional_closed=false
```

因此下一步不能继续在环内换名。非循环出口只剩：

```text
NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact
AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
```

并行仍需：

```text
ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
RatePreservationLedger_FOR_moving_atom_packet
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本步是自证路线删除，不是行/列命题无条件闭合。

## 126. Strict new primitive payload source-atom alignment router

新增文件

```text
experiments/prime_matrix_strict_new_primitive_payload_source_atom_alignment_router.py
docs/monograph/prime-matrix-strict-new-primitive-payload-source-atom-alignment-router.md
docs/monograph/prime-matrix-strict-new-primitive-payload-source-atom-alignment-router.json
data/prime-matrix-strict-new-primitive-payload-source-atom-alignment-ledger.json
```

本步直接审计 `NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact`。结论是：它若只是
signed-lane 环内的 trace、payload、origin 或 common packet 改名，不能破环；若要成为真正
new primitive 工件，则必须在 Cauchy/Phi/payment 前声明同一 actual source object，并给出：

```text
ActualPreCauchySourceDomainAbsoluteEntropyLedger
CompletePrimitiveEmitterKeyPartitionLedger
FixedKeyExactUVLocalMultiplicityO1Ledger
```

因此该出口已对齐到：

```text
ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger
```

或转入 terminal descent、PDEC、外部谱输入。当前没有独立 new primitive 工件，下一直接主攻为
`ActualPreCauchySourceDomainAbsoluteEntropyLedger`；行/列命题仍未无条件闭合。

## 127. Strict source entropy downstream cycle sync router

新增文件

```text
experiments/prime_matrix_strict_source_entropy_downstream_cycle_sync_router.py
docs/monograph/prime-matrix-strict-source-entropy-downstream-cycle-sync-router.md
docs/monograph/prime-matrix-strict-source-entropy-downstream-cycle-sync-router.json
data/prime-matrix-strict-source-entropy-downstream-cycle-sync-ledger.json
```

本步把 `ActualPreCauchySourceDomainAbsoluteEntropyLedger` 沿既有下游证书同步到底：

```text
ActualPreCauchySourceDomainAbsoluteEntropyLedger
-> AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward
-> AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows
-> AcyclicSeedInternalArithmeticBasisExpansionBeforeCauchy
-> AcyclicSeedNoncanonicalPreCauchyBasisAlphabetLedger
-> signed coordinate-source cycle
```

该环不能作为 source entropy 的证明。若不提交无环的
`AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput`，source entropy 首原子只能回流
`AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate` 或其他独立出口。complete-key、
fixed-key、PDEC/外部谱与 DStructure/Rankin 仍开放。

## 128. Strict cycle-cut / terminal descent unified frontier router

新增文件

```text
experiments/prime_matrix_strict_cyclecut_terminal_descent_unified_frontier_router.py
docs/monograph/prime-matrix-strict-cyclecut-terminal-descent-unified-frontier-router.md
docs/monograph/prime-matrix-strict-cyclecut-terminal-descent-unified-frontier-router.json
data/prime-matrix-strict-cyclecut-terminal-descent-unified-frontier-ledger.json
```

本步把 source entropy 出口、seed-cycle-cut 饱和证书、terminal descent 宏循环证书、PDEC same-set 饱和证书和 joint-emitter 字段原子证书统一到同一张前沿账本。当前读数：

```text
source_entropy_exit_imported=true
seed_cycle_cut_branch_saturated=true
terminal_descent_macrocycle_detected=true
pdec_internal_branch_saturated=true
new_joint_formula_reduced_to_declaration_line=true
pre_cauchy_joint_declaration_line_proved=false
row_column_unconditional_closed=false
```

因此最新 strict 内部第一生产性单点是：

```text
PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple
```

但它不是孤立输入；仍需同一 pre-Cauchy actual source tuple 的 rows formula、word/coefficient identity 与 no-downstream-return ledger。canonical-lock、independent source bridge、PDEC/外部谱、complete/fixed-key、ExactUV、模型余量、RatePreservation 和 DStructure/Rankin 仍是独立开放门。

## 129. Strict cycle-cut unified antisplit downstream sync router

新增文件

```text
experiments/prime_matrix_strict_cyclecut_unified_antisplit_downstream_sync_router.py
docs/monograph/prime-matrix-strict-cyclecut-unified-antisplit-downstream-sync-router.md
docs/monograph/prime-matrix-strict-cyclecut-unified-antisplit-downstream-sync-router.json
data/prime-matrix-strict-cyclecut-unified-antisplit-downstream-sync-ledger.json
```

本步把普通 joint declaration 继续同步到既有下游前沿。关键结论是：普通 declaration 会降到
`ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple`，
而普通 constructor 路线已经登记为 signed-source 固定点，不能作为非循环证明。真正内部自足路线必须走反分裂 atomic rows。

当前读数：

```text
ordinary_joint_declaration_route_rejected_as_nonproof=true
antisplit_atomic_route_imported=true
atomic_rows_reduced_to_builtin_pairing=true
exactuv_entropy_fiber_split_imported=true
built_in_signed_pairing_proved=false
row_column_unconditional_closed=false
```

下一直接主攻更新为：

```text
BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
```

并行硬点为：

```text
ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
```

## 130. Strict antisplit trace-cycle / ExactUV atomized frontier router

新增文件

```text
experiments/prime_matrix_strict_antisplit_trace_exactuv_atomized_frontier_router.py
docs/monograph/prime-matrix-strict-antisplit-trace-exactuv-atomized-frontier-router.md
docs/monograph/prime-matrix-strict-antisplit-trace-exactuv-atomized-frontier-router.json
data/prime-matrix-strict-antisplit-trace-exactuv-atomized-frontier-ledger.json
```

本步继续同步 built-in pairing 与 ExactUV 两侧。signed 侧：

```text
BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
-> ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn
-> signed-lane dependency cycle
```

所以 trace 本身不能自证，非循环出口回到：

```text
NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact
```

并行 ExactUV 侧进一步拆成：

```text
AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward
RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger
FixedKeyExactUVLocalMultiplicityO1Ledger
```

当前三项均未证明，行/列命题仍保持开放。

## 131. Strict post-antisplit source-rank convergence router

新增文件

```text
experiments/prime_matrix_strict_post_antisplit_source_rank_convergence_router.py
docs/monograph/prime-matrix-strict-post-antisplit-source-rank-convergence-router.md
docs/monograph/prime-matrix-strict-post-antisplit-source-rank-convergence-router.json
data/prime-matrix-strict-post-antisplit-source-rank-convergence-ledger.json
```

本步把刚完成的 antisplit trace/ExactUV 前沿与既有 new primitive、terminal descent、source-rank/no-collapse、source entropy、complete key 和 source table 证书合并。关键收敛链为：

```text
NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact
-> ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger

AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
-> ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger

ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger
-> PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate
```

因此 `NewPrimitive...` 与 terminal descent 不再是独立闭合点；二者共同回到同 formal-unit 的逐 primitive alpha/delta 核表。当前第一硬点更新为：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger
```

并行硬点为：

```text
IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
```

行/列命题仍未无条件闭合。

## 146. Strict terminal atoms to alpha-return bridge sync router

新增文件

```text
experiments/prime_matrix_strict_terminal_atoms_to_alpha_return_bridge_sync_router.py
docs/monograph/prime-matrix-strict-terminal-atoms-to-alpha-return-bridge-sync-router.md
docs/monograph/prime-matrix-strict-terminal-atoms-to-alpha-return-bridge-sync-router.json
data/prime-matrix-strict-terminal-atoms-to-alpha-return-bridge-sync-ledger.json
```

本步把上一轮三原子同步到当前更深 strict 前沿。读数确认：

```text
terminal_three_atoms_imported=true
moving_atom_reduced_to_exact_entropy=true
post_mertens_reduced_to_kernel_identity=true
kernel_identity_reduced_to_pointwise_table=true
alpha_return_route_reclassified_as_backedge=true
row_column_unconditional_closed=false
```

实际负载链条上的意义是：moving atom 不再作为孤立出口；它先进入 exact entropy，再进入同 formal-unit kernel identity 与逐点 primitive 核表。核表若沿旧 alpha/weight/rank 三腿拆开，会回到 PDEC/CleanKLS 与终端家族；因此旧 pointwise/alpha 展开只能记为回边，不能提供严格下降量。

最新 strict 自足主攻为：

```text
AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
OR IndependentActualSourceBridgeNotFactoredThroughAlphaReturn
```

前者要提交 canonical-lock 的同集推前、有限因子图、无 noncanonical payload 残留等证书；后者要在进入 exact-UV/rank/alpha 回边前，独立证明 actual-source 恒等或强化反原子。当前仍没有全局无条件闭合。

## 147. Strict alpha-return bridge to concrete terminal split sync router

新增文件

```text
experiments/prime_matrix_strict_alpha_return_bridge_to_concrete_terminal_split_sync_router.py
docs/monograph/prime-matrix-strict-alpha-return-bridge-to-concrete-terminal-split-sync-router.md
docs/monograph/prime-matrix-strict-alpha-return-bridge-to-concrete-terminal-split-sync-router.json
data/prime-matrix-strict-alpha-return-bridge-to-concrete-terminal-split-sync-ledger.json
```

本步把 alpha-return 二选一压成三类具体硬点：

```text
((AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn
AND IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed)
OR SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks
OR (PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve
AND ExplicitModelGapAndFiniteDPRCLedger))
```

读数确认：

```text
alpha_return_bridge_imported=true
independent_bridge_concrete_atoms_imported=true
a1_admission_absorbed_as_scoped_only=true
exact_entropy_reduced_to_seed_and_pair_energy=true
canonical_lock_direct_attack_imported=true
concrete_terminal_split_pinned=true
row_column_unconditional_closed=false
```

负载链条上的实质含义是：A1 admission 已不能作为全局矛盾；exact entropy 不能绕过无环 seed 与独立 pair-energy；canonical-lock 也不能作为单标签闭合，只能进入 Kuznetsov/DLS 或 PDEC/CleanKLS+模型余量。

下一直接主攻：

```text
IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed
```

并行保留无环 seed、自足 Kuznetsov/DLS、PDEC/CleanKLS+模型余量、RatePreservation 与 DStructure/Rankin。

## 148. Strict pair-energy to seed-coordinate cycle sync router

新增文件

```text
experiments/prime_matrix_strict_pair_energy_to_seed_coordinate_cycle_sync_router.py
docs/monograph/prime-matrix-strict-pair-energy-to-seed-coordinate-cycle-sync-router.md
docs/monograph/prime-matrix-strict-pair-energy-to-seed-coordinate-cycle-sync-router.json
data/prime-matrix-strict-pair-energy-to-seed-coordinate-cycle-sync-ledger.json
```

本步直接攻击上一节钉住的
`IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed`。同步结果是：seed-only
和定性投影已经不能给 log-power 速率；旧 ExactUV/source-entropy 脊柱会回到 signed
坐标-来源环与终端家族；seed 存在/不存在两支也已回流 acyclic terminal family。
因此抽象 pair-energy 不能再靠内部来源字段继续下降。

最新剩余被压成三路：

```text
SelfContainedExactPairEnergyLargeSieveInequalityForAcyclicSeed
OR SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks
OR (PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve
AND ExplicitModelGapAndFiniteDPRCLedger)
```

严格活动基仍需保留：

```text
RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本步不是行/列命题的无条件闭合；三路中的直接 pair-energy 大筛、Kuznetsov/DLS 与
PDEC/CleanKLS+模型余量均仍未证明。

## 149. Strict pair-energy diagonal peeling terminal reduction router

新增文件

```text
experiments/prime_matrix_strict_pair_energy_diagonal_peeling_terminal_reduction_router.py
docs/monograph/prime-matrix-strict-pair-energy-diagonal-peeling-terminal-reduction-router.md
docs/monograph/prime-matrix-strict-pair-energy-diagonal-peeling-terminal-reduction-router.json
data/prime-matrix-strict-pair-energy-diagonal-peeling-terminal-reduction-ledger.json
```

本步继续直接拆解上一节留下的
`SelfContainedExactPairEnergyLargeSieveInequalityForAcyclicSeed`。关键剥离是对角项：
没有同 formal unit 的 exact-pair no-heavy 输入时，单个 exact pair 的 delta 模型已经破坏
任意 log-power L2/max-atom 目标；因此 direct pair-energy 大筛不能作为黑箱第三分支。

对角失败正是既有 `RateBearingLargePairAtomPacketExclusion`，会回到 PDEC/clean 终端；
对角剥离后的 off-diagonal 双线性型就是 clean Kuznetsov/DLS。结合 KZ 原子同步、
PDEC/CleanKLS 终端二分与模型余量有限段闭合后，最新严格剩余压成：

```text
AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom
OR (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
AND HighSegmentModelGapAlpha043C3AnalyticLedger)
```

严格活动基仍需保留：

```text
RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本步仍不是无条件闭合；NCBLK/source anti-atom、PDEC 同集作用域、高段模型余量、
RatePreservation 与 DStructure/Rankin 都仍未证明。

## 150. Strict NCBLK/source anti-atom frontier sync router

新增文件

```text
experiments/prime_matrix_strict_ncblk_source_antiatom_frontier_sync_router.py
docs/monograph/prime-matrix-strict-ncblk-source-antiatom-frontier-sync-router.md
docs/monograph/prime-matrix-strict-ncblk-source-antiatom-frontier-sync-router.json
data/prime-matrix-strict-ncblk-source-antiatom-frontier-sync-ledger.json
```

本步继续攻击上一节留下的
`AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom`。同步已有
strict NCBLK 去重、actual-source seed 支撑、假设零行 seed no-go、pre-Cauchy
来源分类、moving-block 回流与 source-declaration 下游证书后，结论是：
NCBLK/source anti-atom 仍未证明，但它也不再是最清晰的主攻名。generic WFD
反原子路线已被 moving-delta 阻断；actual 路线必须先给出不从 downstream 反推的
forward pre-Cauchy source-root packet。若该 source-root 无法正向给出，既有分类
把失败推回 moving-block/global PDEC-sparse 终端。

最新剩余压成：

```text
(ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn)
OR (GlobalPDECorSparseTerminalExclusion
    AND HighSegmentModelGapAlpha043C3AnalyticLedger)
OR (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
    AND HighSegmentModelGapAlpha043C3AnalyticLedger)
```

严格活动基仍需保留：

```text
RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻改为：

```text
ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn
```

该 packet 必须正向给出 declaration line、primitive rows、built-in signed
word/coefficient pairing、actual source-domain entropy、fixed exact `(u,v)` fiber
bound、same formal-unit exact-pair no-heavy/L2 能量账本，以及 no-downstream-recovery
的命名回流分割。本步不是行/列命题无条件闭合；source-root、全局终端、direct PDEC
作用域、高段模型、Rate 与 DStructure 仍未证明。

## 151. Strict forward source-root terminal cycle sync router

新增文件

```text
experiments/prime_matrix_strict_forward_source_root_terminal_cycle_sync_router.py
docs/monograph/prime-matrix-strict-forward-source-root-terminal-cycle-sync-router.md
docs/monograph/prime-matrix-strict-forward-source-root-terminal-cycle-sync-router.json
data/prime-matrix-strict-forward-source-root-terminal-cycle-sync-ledger.json
```

本步继续直接攻击上一节留下的
`ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn`。同步 common packet 下游、
signed-lane 自证环、new primitive/source-rank 汇合、cycle-cut/terminal descent、
antisplit ExactUV 原子化、逐点 primitive alpha/delta 核表、alpha row unsigned
skeleton、signed-lift 回流与 anchor-collar overload 回流后，结论是：当前语料中的
source-root 内部路线没有留下独立非循环闭合；它回到终端容量环。

关键读数：

```text
forward_source_root_packet_proved=false
forward_source_root_independent_after_router=false
signed_lane_self_proof_eliminated=true
source_rank_paths_converged_to_pointwise_kernel=true
alpha_unsigned_skeleton_closed=true
signed_lift_branch_recycles_to_terminal_gap=true
anchor_collar_overload_return_schema_closed=true
row_column_unconditional_closed=false
```

因此上一节的 source-root 名称被同步为终端循环，而不是全局证明。最新严格剩余改写为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse)
AND HighSegmentModelGapAlpha043C3AnalyticLedger
```

严格活动基仍需保留：

```text
RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻相应变为：

```text
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
```

并行保留非循环 KZ/DLS、高段模型、RatePreservation 与 DStructure/Rankin。这里的
`NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse` 是硬边界：
如果 CleanKLS/KZ-DLS 再经 NCBLK/source-root 线闭合，就回到本节识别出的同一终端环。
本步只封住 source-root 的自足回环；行/列命题仍未无条件闭合。

## 152. Strict post-source-root PDEC scope saturation sync router

新增文件

```text
experiments/prime_matrix_strict_post_source_root_pdec_scope_saturation_sync_router.py
docs/monograph/prime-matrix-strict-post-source-root-pdec-scope-saturation-sync-router.md
docs/monograph/prime-matrix-strict-post-source-root-pdec-scope-saturation-sync-router.json
data/prime-matrix-strict-post-source-root-pdec-scope-saturation-sync-ledger.json
```

本步继续攻击上一节留下的直接主攻
`AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate`。同步既有 direct PDEC
作用域审计、PDEC scope 分支饱和、canonical-lock 直攻、KZ/DLS 终端回流和终端家族
饱和证书后，关键读数为：

```text
post_source_root_pdec_scope_active=true
direct_pdec_scope_audit_imported=true
pdec_scope_branch_saturated_in_current_internal_corpus=true
pdec_scope_proved=false
noncircular_kuznetsov_dls_without_source_root_reuse_proved=false
new_explicit_joint_constructor_formula_artifact_present=false
row_column_unconditional_closed=false
```

结论是：same-set PDEC 协议和 canonical-source 容量边界可用作工具，但不能自动导入
strict acyclic noncanonical 分支。direct PDEC 若要成为闭合输入，仍需新证书证明
acyclic 终端证书与 canonical same-set 证书在 formal unit、坏窗集合、`U_CRT/L_PDEC`
和质量推前上完全同口径；否则它在当前内部语料中已经回到饱和边界。

最新内部非循环基同步为：

```text
(NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
 OR NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse)
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

条件保留线为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY
 OR NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse)
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻改为：

```text
NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
```

本步不是行/列命题无条件闭合；它只说明 post-source-root 的 direct PDEC 内部路线已经
不能继续作为已证非循环出口。新 PDEC scope 证书、外部 DIBFI、非循环 KZ/DLS、高段模型、
RatePreservation 与 DStructure/Rankin 仍均未给出。

## 153. Strict post-PDEC new-joint noncycle sync router

新增文件

```text
experiments/prime_matrix_strict_post_pdec_new_joint_noncycle_sync_router.py
docs/monograph/prime-matrix-strict-post-pdec-new-joint-noncycle-sync-router.md
docs/monograph/prime-matrix-strict-post-pdec-new-joint-noncycle-sync-router.json
data/prime-matrix-strict-post-pdec-new-joint-noncycle-sync-ledger.json
```

本步继续攻击上一节留下的
`NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact`。同步 global CRT
branch-trace、signed payload、atomic trace payload、signed-lane cycle、new primitive
和 post-antisplit source-rank convergence 证书后，关键读数为：

```text
new_joint_current_internal_route_saturated=true
new_explicit_joint_constructor_formula_artifact_present=false
exact_atomic_branch_trace_formula_proved=false
atomic_signed_payload_constructor_proved=false
signed_lane_self_proof_eliminated=true
new_primitive_artifact_independent_present=false
noncircular_kuznetsov_dls_without_source_root_reuse_proved=false
row_column_unconditional_closed=false
```

结论是：当前内部 new-joint 旧路线不能作为非循环出口。旧 joint/antisplit
链只把生产性内容压到 exact atomic branch trace；branch trace 只给可见坐标；
signed coefficient/local factor 仍需要 atomic signed payload constructor；而 signed
payload 又回到 origin/common-packet 闭环。new primitive 若要破环，必须提交闭环外的
pre-Cauchy actual source-rank/no-collapse 工件；当前语料没有该工件。

最新内部非循环基同步为：

```text
NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

条件保留线为：

```text
(NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
 OR NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact
 OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY
 OR NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse)
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻改为：

```text
NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse
```

本步不是行/列命题无条件闭合；它只删除 new-joint 的旧内部自证路线。剩余核心是一个不
复用 NCBLK/source-root 的 Kuznetsov/DLS 大筛证明，并且高段模型、RatePreservation 与
DStructure/Rankin 仍未闭合。

## 154. Strict post-new-joint KZ no-cycle gate sync router

新增文件

```text
experiments/prime_matrix_strict_post_new_joint_kz_nocycle_gate_sync_router.py
docs/monograph/prime-matrix-strict-post-new-joint-kz-nocycle-gate-sync-router.md
docs/monograph/prime-matrix-strict-post-new-joint-kz-nocycle-gate-sync-router.json
data/prime-matrix-strict-post-new-joint-kz-nocycle-gate-sync-ledger.json
```

本步继续攻击上一节留下的
`NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse`。
同步 windowed DLS、KZ 原子、KZ 终端同步、NC-BLK/source anti-atom 去重、forward
source-root 终端环和 alpha terminal cycle guard 后，关键读数为：

```text
latest_kz_nocycle_gate_active=true
windowed_dls_formal_layer_imported=true
kz_abcd_spine_imported=true
existing_kz_e_route_factors_through_ncblk=true
ncblk_projection_forbidden_for_nocycle_gate=true
noncircular_kuznetsov_dls_without_source_root_reuse_proved=false
kz_e_direct_log_saving_without_ncblk_projection_proved=false
row_column_unconditional_closed=false
```

结论是：KZ-A--KZ-D 的谱脊柱和 windowed DLS 形式层已经可以导入，但当前语料里的
KZ-E log-saving 路线通过 NC-BLK/source anti-atom 投影闭合；该投影随后回到
source-root/terminal cycle。由于本门明确要求 `without NCBLK/source-root reuse`，
这条旧路线不能计入非循环 KZ/DLS 证明。

最新内部非循环基同步为：

```text
AcyclicKZEWellFactorableDispersionLogSavingWithoutNCBLKProjection
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

条件外部线为：

```text
(AcyclicKZEWellFactorableDispersionLogSavingWithoutNCBLKProjection
 OR ExactExternalDIBFIKuznetsovNoProjectionCertificate_FOR_NONCIRCULAR_KZ_ONLY)
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻改为：

```text
AcyclicKZEWellFactorableDispersionLogSavingWithoutNCBLKProjection
```

本步不是行/列命题无条件闭合；它只把“非循环 KZ/DLS”门进一步原子化为不得经
NC-BLK 投影的 KZ-E well-factorable dispersion log-saving。高段模型、
RatePreservation 与 DStructure/Rankin 仍未闭合。

## 155. Strict post-KZ-E direct source-bridge sync router

新增文件

```text
experiments/prime_matrix_strict_post_kze_direct_source_bridge_sync_router.py
docs/monograph/prime-matrix-strict-post-kze-direct-source-bridge-sync-router.md
docs/monograph/prime-matrix-strict-post-kze-direct-source-bridge-sync-router.json
data/prime-matrix-strict-post-kze-direct-source-bridge-sync-ledger.json
```

本步继续攻击上一节留下的
`AcyclicKZEWellFactorableDispersionLogSavingWithoutNCBLKProjection`。同步 KZ-E
spine、DIBFI 自足闭合分类、actual-source provenance、source-lock 合同、branch coverage、
strict actual-source bridge 障碍和 terminal recurrence firewall 后，关键读数为：

```text
kze_direct_no_projection_gate_active=true
self_contained_taxonomy_imported=true
canonical_provenance_closed_only_for_canonical_branch=true
source_lock_scoped_not_global=true
actual_source_bridge_obstruction_imported=true
noncanonical_moving_atom_not_kz_nocycle_proof=true
kze_direct_current_internal_route_reduced_to_source_admission=true
a1_clean_branch_canonical_source_admission_proved=false
row_column_unconditional_closed=false
```

结论是：KZ-E direct no-projection 若不接受外部 DI/BFI/Kuznetsov 证书，不能继续走
generic WFD 自足线，也不能走 noncanonical moving-atom/anti-atom 回流线，因为后者不是当前
KZ no-cycle 门的直接谱证明。canonical-restricted 自足分支可用，但只在当前 clean A1
反例分支已经于 Cauchy/dispersion 前准入 canonical RIW/Buchstab source 时可用。

最新内部非循环基同步为：

```text
A1CleanBranchCanonicalSourceAdmission
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

条件外部线为：

```text
(A1CleanBranchCanonicalSourceAdmission
 OR ExactExternalDIBFIKuznetsovNoProjectionCertificate_FOR_NONCIRCULAR_KZ_ONLY)
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻改为：

```text
A1CleanBranchCanonicalSourceAdmission
```

本步不是行/列命题无条件闭合；它只把 KZ-E direct 门压到 actual source admission。不能把
canonical 分支闭合偷渡为 generic/noncanonical 分支闭合；高段模型、RatePreservation 与
DStructure/Rankin 仍未闭合。

## 156. Strict post-source-admission macrocycle sync router

新增文件

```text
experiments/prime_matrix_strict_post_source_admission_macrocycle_sync_router.py
docs/monograph/prime-matrix-strict-post-source-admission-macrocycle-sync-router.md
docs/monograph/prime-matrix-strict-post-source-admission-macrocycle-sync-router.json
data/prime-matrix-strict-post-source-admission-macrocycle-sync-ledger.json
```

本步继续攻击上一节留下的 `A1CleanBranchCanonicalSourceAdmission`，并把它接入
仓库已有的 A1/T1/signed-lift/PDEC/KZ 深层链。关键读数为：

```text
post_kze_source_admission_active=true
a1_source_admission_scoped_not_global=true
t1_mismatch_no_silent_exit_imported=true
signed_lift_failure_return_only_registers=true
alpha_weight_downstream_returns_to_terminal=true
internal_pdec_clean_kls_cycle_imported=true
nonrecursive_breaker_hits_seed_cycle=true
new_joint_and_kz_return_to_a1_gate=true
a1_pdec_kz_macrocycle_detected=true
row_column_unconditional_closed=false
```

结论是：A1 source-admission 不是尚未展开的孤立证明点。canonical 等式 case 只被
scoped 吸收；mismatch case 经 signed lift 登记、alpha weight law、PDEC/CleanKLS、
new-joint 与 KZ no-cycle 后回到 KZ-E/A1 门。因此当前内部路线形成非证明宏循环：

```text
A1CleanBranchCanonicalSourceAdmission
  -> T1 canonical equality classifier
  -> mismatch forcing / signed lift failure registration
  -> alpha signed weight downstream
  -> PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve
  -> self-contained terminal cycle / nonrecursive breaker
  -> new-joint saturation
  -> non-circular KZ/DLS gate
  -> KZ-E direct source bridge
  -> A1CleanBranchCanonicalSourceAdmission
```

最新非循环破环基为：

```text
(AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput
 OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR NewPrimitiveJointPayloadArtifactOutsideSignedLaneCycle
 OR ExactExternalDIBFIKuznetsovNoProjectionCertificate_FOR_NONCIRCULAR_KZ_ONLY)
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput
```

本步不证明 A1 source-admission 的全局排斥，也不证明 PDEC/CleanKLS、外部 KZ/DI/BFI、
高段模型、RatePreservation 或 DStructure/Rankin；它只关闭一条当前内部路线的非循环性审查：
该路线回到自身，不能作为无条件证明。

## 157. Row-gap supply/phase cycle-cut router

新增文件

```text
experiments/prime_matrix_row_gap_supply_phase_cycle_cut_router.py
docs/monograph/prime-matrix-row-gap-supply-phase-cycle-cut-router.md
docs/monograph/prime-matrix-row-gap-supply-phase-cycle-cut-router.json
data/prime-matrix-row-gap-supply-phase-cycle-cut-ledger.json
```

本步把具体反例模型 `I_k={kP+a:1<=a<P}` 无素数拆成低根供给、近根半素数槽与
`Q1/Q2` 相邻素数 CRT 传输三块。关键读数为：

```text
row_gap_model_pinned=true
correct_divisor_supply_law=true
low_root_only_claim_rejected=true
capacity_only_contradiction_rejected=true
crt_period_mirror_not_contradiction=true
low_root_deficit_after_near_root_slots_proved=false
q1q2_transport_defect_or_stable_short_return_proved=false
row_column_unconditional_closed=false
```

校正后的供给律是：若 `kP+a` 合数且 `1<=a<P`，则 `kP+a<P^2`，所以存在素因子
`q<P`；但不能统一写成 `q<=sqrt(kP)`，因为

```text
sqrt(kP) < q <= sqrt(kP+P-1)
```

的近根素数仍可能覆盖边缘半素数槽。零行的精确义务是：

```text
low-root slots union near-root slots covers every a=1..P-1.
```

raw capacity 带重数通常大于 `P`，所以单纯“供给总量”不产生矛盾；真正可攻点是：

```text
UniformLowRootSiftedResidueDeficitAfterNearRootSlots
```

即低根筛余槽在扣除近根 only 槽后仍有统一正缺口。另一路是：

```text
AdjacentPrimeQ1Q2CRTTransportDefectOrStableShortReturn
```

若 `Q1<kP` 与 `Q2>(k+1)P` 是夹住零行的相邻素数，CRT 镜像只给镜像覆盖块，本身不是矛盾；
必须额外证明 `Q1/Q2` 传输强制同 formal unit 短同标签复现，或所有不稳定都登记为
PDEC/SAE/ColumnCRT 缺陷。

最新非循环基为：

```text
(UniformLowRootSiftedResidueDeficitAfterNearRootSlots
 OR AdjacentPrimeQ1Q2CRTTransportDefectOrStableShortReturn
 OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput
 OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR ExactExternalPrimeGapSqrtBarrierCertificate_FOR_ROW_GAP_ONLY)
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
UniformLowRootSiftedResidueDeficitAfterNearRootSlots
```

本步没有证明所有 row-gap 不可能；它把具体反例的供需/相位矛盾压成统一低根筛余缺口或
`Q1/Q2` CRT 传输矛盾。

## 158. Low-root sifted deficit frontier router

新增文件

```text
experiments/prime_matrix_lowroot_sifted_deficit_frontier_router.py
docs/monograph/prime-matrix-lowroot-sifted-deficit-frontier-router.md
docs/monograph/prime-matrix-lowroot-sifted-deficit-frontier-router.json
data/prime-matrix-lowroot-sifted-deficit-frontier-ledger.json
```

本步继续攻击上一节留下的 `UniformLowRootSiftedResidueDeficitAfterNearRootSlots`。同步读数为：

```text
exact_deficit_identity_closed=true
near_root_slot_upper_bound_elementary=true
mertens_heuristic_not_proof=true
jacobsthal_barrier_identified=true
noncircular_short_interval_rough_residue_lower_bound_proved=false
row_column_unconditional_closed=false
```

精确等价已经闭合：在 `I_k={kP+a:1<=a<P}` 中，`kP+a<P^2`。因此

```text
full_uncovered_slots > 0  <=>  row contains a prime.
```

近根槽只来自

```text
sqrt(kP) < q <= sqrt(kP+P-1)
```

每个这样的 `q` 在 row 内只给一个 residue class，容量有初等上界；它不是主要未知。真正硬点是：

```text
NonCircularShortIntervalRoughResidueLowerBoundLengthPLevelSqrtkP
```

即在长度 `P` 的指定相位短区间中，筛到 `sqrt(kP)` 后仍保留足够 rough residue，使近根槽不能全部吞掉。
Mertens 密度只能给启发，不能替代逐行下界；否则会把行命题循环写回自身。

最新非循环基为：

```text
(NonCircularShortIntervalRoughResidueLowerBoundLengthPLevelSqrtkP
 OR AdjacentPrimeQ1Q2CRTTransportDefectOrStableShortReturn
 OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput
 OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate)
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
NonCircularShortIntervalRoughResidueLowerBoundLengthPLevelSqrtkP
```

## 159. Short-interval rough-residue barrier router

新增文件

```text
experiments/prime_matrix_short_interval_rough_residue_barrier_router.py
docs/monograph/prime-matrix-short-interval-rough-residue-barrier-router.md
docs/monograph/prime-matrix-short-interval-rough-residue-barrier-router.json
data/prime-matrix-short-interval-rough-residue-barrier-ledger.json
```

本步继续审查上一节的直接首攻点。同步读数为：

```text
full_root_rough_equals_prime_in_row=true
near_root_subtraction_keeps_equivalence=true
mertens_average_insufficient=true
periodwide_jacobsthal_shortcut_rejected=true
noncircular_internal_use_rejected=true
noncircular_short_interval_rough_residue_lower_bound_proved=false
row_column_unconditional_closed=false
```

关键压缩是：在 `I_k={kP+a:1<=a<P}`、`1<=k<P` 中，若某槽未被任何
`q<=sqrt(kP+P-1)` 覆盖，则该槽只能是素数。因此

```text
full_root_uncovered > 0  <=>  row contains a prime.
```

low-root 未覆盖数扣除近根 only 槽后的正性仍等价于 full-root 未覆盖正性。于是
`NonCircularShortIntervalRoughResidueLowerBoundLengthPLevelSqrtkP` 不能再作为自足证明内部黑箱；
直接证明它已经是平方根长度 row-gap 素数存在性本身。

最新内部非循环基改为：

```text
(AdjacentPrimeQ1Q2CRTTransportDefectOrStableShortReturn
 OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput
 OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate)
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

若接受外部强输入，可登记：

```text
ExactExternalSqrtLengthPrimeGapInput_FOR_ROW_GAP_ONLY
```

但它未在当前文稿内证明，不能冒充自足闭合。下一直接主攻转为：

```text
AdjacentPrimeQ1Q2CRTTransportDefectOrStableShortReturn
```

## 160. Q1/Q2 transport latest noncycle sync router

新增文件

```text
experiments/prime_matrix_q1q2_transport_latest_noncycle_sync_router.py
docs/monograph/prime-matrix-q1q2-transport-latest-noncycle-sync-router.md
docs/monograph/prime-matrix-q1q2-transport-latest-noncycle-sync-router.json
data/prime-matrix-q1q2-transport-latest-noncycle-sync-ledger.json
```

本步继续攻击上一节留下的 Q1/Q2 传输首攻点。同步读数为：

```text
q2_endpoint_stable_replay_impossible=true
persistent_closed_carrier_routes_to_columncrt_pdec=true
controlled_fresh_endpoint_tail_routes_to_sae=true
unnamed_aperture_explosion_forbidden=true
pure_crt_global_phase_contradiction_blocked=true
q1q2_branch_reduced_to_exact_source_or_external=true
q1q2_transport_defect_or_stable_short_return_proved_as_global_contradiction=false
row_column_unconditional_closed=false
```

核心结论是：Q1/Q2 相邻素数传输确实排除了 endpoint-stable replay。全 `Q2` 阶轮会把
两个素端点复本分别变成被 `Q1,Q2` 自身整除的复合点。但这只排除“同端点复现”跳步；
其余分支已有旧 Q2 梯路由：

```text
persistent closed carrier => ColumnCRT/PDEC
controlled fresh endpoint tail => SAE
aperture explosion/support motion => explicit schema firewall
pure finite CRT phase contradiction => exact-source dispersion required
```

因此 `AdjacentPrimeQ1Q2CRTTransportDefectOrStableShortReturn` 不能作为独立终端硬点保留。
立即内部基改写为：

```text
((NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource
 OR ExternalDIBFIKuznetsovDispersionTheoremMatch)
 OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput
 OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate)
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

若同时导入既有 seed/PDEC 分支饱和同步，strict 内部剩余进一步压到：

```text
NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource
```

## 161. Exact-UV fiber latest noncycle sync router

新增文件

```text
experiments/prime_matrix_exactuv_fiber_latest_noncycle_sync_router.py
docs/monograph/prime-matrix-exactuv-fiber-latest-noncycle-sync-router.md
docs/monograph/prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json
data/prime-matrix-exactuv-fiber-latest-noncycle-sync-ledger.json
```

本步继续攻击上一节留下的 exact-source 首攻点。同步读数为：

```text
preterminal_fiber_atomization_imported=true
deterministic_source_atom_implication_closed=true
source_entropy_reduced_to_signed_rows=true
complete_key_reduced_to_actual_source_table=true
fixed_pair_fiber_formal_inequality_closed=true
map_rank_equivalent_to_bounded_incidence=true
nonterminal_exactuv_fiber_aperiodicity_proved=false
row_column_unconditional_closed=false
```

核心结论是：`NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource`
不是 CRT 位置/相位刚性问题，而是同一 actual formal unit 内 pre-Cauchy source 的源域熵、
complete emitter key 分区与 fixed-key exact-UV 局部重数问题。当前已闭合的是形式蕴含：

```text
ActualPreCauchySourceDomainAbsoluteEntropyLedger
AND RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger
AND FixedKeyExactUVLocalMultiplicityO1Ledger
=> NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource
```

未闭合的是这三个 actual 源侧输入本身。完全原子化后的内部基为：

```text
((AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward
  AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
  AND PrimitiveRowSupportLowerBoundBeforeExactUVProjectionLedger)
 AND (ActualNoncanonicalPrimitiveEmitterSourceTableLedger
  AND CompleteEmitterTraceKeyBudgetLedger
  AND SignLocalFactorRefinementNoCancellationLedger
  AND OverBudgetOrUnregisteredReturnLedger)
 AND FixedKeyExactUVLocalMultiplicityO1Ledger)
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

若导入既有 strict 下游同步，内部剩余可继续压到：

```text
NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward
```

并行保留 `ActualNoncanonicalPrimitiveEmitterSourceTableLedger`、
`FixedKeyExactUVLocalMultiplicityO1Ledger`、`NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact`
与 `ExternalDIBFIKuznetsovDispersionTheoremMatch`。本步删除 exact-UV 作为纯 CRT/位置问题的误出口；
行/列命题仍未全局无条件闭合。

## 162. Inverse-alignment 第 P+1 行归约检查

新增文件

```text
experiments/prime_matrix_inverse_alignment_pplus1_row_reduction_check_router.py
docs/monograph/prime-matrix-inverse-alignment-pplus1-row-reduction-check-router.md
docs/monograph/prime-matrix-inverse-alignment-pplus1-row-reduction-check-router.json
data/prime-matrix-inverse-alignment-pplus1-row-reduction-check-ledger.json
```

本步检查旧仓库中“同余方程组最小对齐解 `x` 必大于 `P`”路线与 `P^2` 后第 `P+1` 行的关系。同步读数为：

```text
old_minrep_equivalence_closed=true
pplus1_row_is_x_equals_p=true
x_equals_p_no_cover_equivalent_to_first_half_prime_square=true
pplus1_nonzero_suffices_for_all_early_rows_proved=false
row_column_unconditional_closed=false
```

按仓库记号，行乘数 `x` 的窗口是 `xP+r, 1<=r<P`；所以 `x=P` 是一编号第 `P+1` 行，
即平方锚后首行 `(P^2,P^2+P)`。旧稿已经闭合：

```text
x=P 无全覆盖
<=> (P^2,P^2+P) 内存在素数
```

但旧稿没有证明：

```text
x=P 非零行  =>  所有 1<=x<P 非零行
```

原因是不同 `x` 给出不同覆盖相位 `rho_q(x)=-xP mod q`；`x=P` 的负平方相位只是一条特殊相位线，
不能自动控制全部早期相位线。可安全使用的条件归约必须写成：

```text
EarlyZero(x<P)
=> ZeroAtXEqualsP OR NamedReturn(PDEC/SAE/ColumnCRT/source-rank)
```

因此本分支新增的缺失接口为：

```text
AcyclicEarlyZeroToSquareAnchorPhaseTransferOrNamedReturn
```

它不替代上一节的 signed-row 主攻，而是作为 inverse-alignment 旧路线回流接口并行保留。合并后的活动基为：

```text
((AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward
  OR AcyclicEarlyZeroToSquareAnchorPhaseTransferOrNamedReturn)
 OR ActualNoncanonicalPrimitiveEmitterSourceTableLedger
 OR FixedKeyExactUVLocalMultiplicityO1Ledger
 OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
 OR ExternalDIBFIKuznetsovDispersionTheoremMatch)
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本步回答旧稿检查：已有的是 `x=P`/第 `P+1` 行等价链；尚未有第 `P+1` 行非零推出 `x<P` 零行不存在的充分性证明。

## 163. Early-to-square phase-transfer 首破裂分裂

新增文件

```text
experiments/prime_matrix_early_to_square_phase_transfer_split_router.py
docs/monograph/prime-matrix-early-to-square-phase-transfer-split-router.md
docs/monograph/prime-matrix-early-to-square-phase-transfer-split-router.json
data/prime-matrix-early-to-square-phase-transfer-split-ledger.json
```

本步继续攻击上一节新增的 `AcyclicEarlyZeroToSquareAnchorPhaseTransferOrNamedReturn`。同步读数为：

```text
contiguous_zero_block_dichotomy_closed=true
persist_to_square_implies_square_zero=true
first_break_release_set_nonempty=true
unit_phase_slip_formula_closed=true
phase_slip_schema_admission_imported=true
transfer_proved_as_contradiction=false
row_column_unconditional_closed=false
```

设存在早期零行 `x0<P`。从 `x0` 向平方锚 `x=P` 推进，只有两种情形：

```text
1. 零行块一直延续到 x=P，则得到 square-zero 分支；
2. 否则存在首个破裂行 y<=P，且 y-1 是零行、y 有非空释放列集。
```

对首破裂释放列 `c`，上一行由某个 `q<P` 覆盖，而当前行不再被任何 `q<P` 覆盖。覆盖相位满足：

```text
rho_q(t)=-tP mod q,
rho_q(t+1)=rho_q(t)-P mod q.
```

因此首破裂是一个单位相位滑移缺陷；它不再是无名 transfer 缺口，而按旧的
early-zero phase-defect schema 登记到 `PDEC/SAE/ColumnCRT/LocalSurvivor` 命名回流。

抽象 transfer 分支被压成：

```text
NoZeroRowAtXEqualsP_PlusOneRowAfterSquare
AND FirstBreakPhaseSlipNamedReturnExclusion
```

合并 exact-UV/source-rank 前沿后的活动基为：

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare
  AND FirstBreakPhaseSlipNamedReturnExclusion)
 OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward
  AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger
  AND FixedKeyExactUVLocalMultiplicityO1Ledger)
 OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
 OR ExternalDIBFIKuznetsovDispersionTheoremMatch)
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
FirstBreakPhaseSlipNamedReturnExclusion
```

本步关闭的是抽象 transfer 的无名性；尚未排斥首破裂 phase-slip 的 PDEC/SAE/LocalSurvivor 终端。

## 164. First-break phase-slip LCM-支撑宽度屏障

新增文件

```text
experiments/prime_matrix_firstbreak_phase_slip_lcm_barrier_router.py
docs/monograph/prime-matrix-firstbreak-phase-slip-lcm-barrier-router.md
docs/monograph/prime-matrix-firstbreak-phase-slip-lcm-barrier-router.json
data/prime-matrix-firstbreak-phase-slip-lcm-barrier-ledger.json
```

本步继续攻击 `FirstBreakPhaseSlipNamedReturnExclusion`。同步读数为：

```text
fixed_carrier_lcm_replay_period_closed=true
square_support_width_sharpened_to_p_minus_y=true
lcm_exceeds_width_no_fixed_replay=true
firstbreak_phase_slip_named_return_exclusion_proved=false
row_column_unconditional_closed=false
```

设首破裂发生在行 `y<=P`，释放 formal unit 的活动 carrier 标签集为 `Lambda`。若同一释放相位模式在
`y+d` 复现且 carrier 标签不移动，则对每个活动素数 `q` 都有：

```text
rho_q(y+d)=rho_q(y),
rho_q(t)=-tP mod q,
dP == 0 mod q.
```

因为 `(P,q)=1`，所以 `q|d`，即：

```text
lcm(Lambda) | d.
```

从首破裂行到平方锚前的复现支撑宽度只有：

```text
H=P-y.
```

因此若 `lcm(Lambda)>H`，在 `1<=d<=H` 内没有固定 carrier 同标签复现；若 `lcm(Lambda)<=H`，则活动
carrier 的合成模数已经被 `H<=P` 控制，只能作为小 LCM/固定 residue 的 ColumnCRT/PDEC 分支处理。
若反例链通过更换 carrier 逃避该屏障，则不再是 fixed replay，而是 moving-carrier phase slip。

于是首破裂终端被压成：

```text
FirstBreakPhaseSlipNamedReturnExclusion
  -> SmallLCMColumnCRTPDECExclusion
  AND NonreplaySparseFirstBreakSAESummability
  AND MovingCarrierPhaseSlipPDECExclusion
```

inverse-alignment 回流分支更新为：

```text
NoZeroRowAtXEqualsP_PlusOneRowAfterSquare
AND SmallLCMColumnCRTPDECExclusion
AND NonreplaySparseFirstBreakSAESummability
AND MovingCarrierPhaseSlipPDECExclusion
```

本步关闭的是固定 carrier 复现的合成模数屏障；小 LCM PDEC、非复现 sparse SAE 与 moving-carrier PDEC
仍未排斥，行/列命题仍未无条件闭合。

## 165. First-break small-LCM rank-pressure 压缩

新增文件

```text
experiments/prime_matrix_firstbreak_small_lcm_rank_pressure_router.py
docs/monograph/prime-matrix-firstbreak-small-lcm-rank-pressure-router.md
docs/monograph/prime-matrix-firstbreak-small-lcm-rank-pressure-router.json
data/prime-matrix-firstbreak-small-lcm-rank-pressure-ledger.json
```

本步继续攻击 `SmallLCMColumnCRTPDECExclusion`。同步读数为：

```text
distinct_prime_product_law_closed=true
small_lcm_rank_pressure_closed=true
two_large_carrier_sqrt_barrier_closed=true
small_lcm_branch_excluded=false
row_column_unconditional_closed=false
```

在 fixed small-LCM 分支中，必须有 `H=P-y>=1`；若 `y=P`，则没有后续非零复现步长，回到
square-anchor/SAE 边界。活动 carrier 标签集 `Lambda` 由互异素数构成，并满足：

```text
L = lcm(Lambda) = product_{q in Lambda} q <= H = P-y.
```

对任意阈值 `B>1`：

```text
|{q in Lambda:q>B}| <= floor(log H / log B).
```

特别地，两个 `q>sqrt(H)` 的 carrier 不可能同处一个 fixed small-LCM formal unit。因此小 LCM
若要承担反例压力，只能进入三类更低层出口：

```text
SmallLCMColumnCRTPDECExclusion
  -> LowCarrierFixedResidueColumnCRTPDECExclusion
  AND LowCarrierNonpersistentSparseSAESummability
  AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE
```

当前 inverse-alignment 回流分支更新为：

```text
NoZeroRowAtXEqualsP_PlusOneRowAfterSquare
AND LowCarrierFixedResidueColumnCRTPDECExclusion
AND LowCarrierNonpersistentSparseSAESummability
AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE
AND NonreplaySparseFirstBreakSAESummability
AND MovingCarrierPhaseSlipPDECExclusion
```

本步没有排斥 small-LCM 分支，而是把它从宽口径 ColumnCRT/PDEC 压成低 carrier 固定 residue、低 carrier
非持久 sparse SAE、高 carrier 低秩容量缺口三项。

## 166. First-break low-carrier fixed-residue AP 骨架

新增文件

```text
experiments/prime_matrix_firstbreak_low_carrier_residue_ap_router.py
docs/monograph/prime-matrix-firstbreak-low-carrier-residue-ap-router.md
docs/monograph/prime-matrix-firstbreak-low-carrier-residue-ap-router.json
data/prime-matrix-firstbreak-low-carrier-residue-ap-ledger.json
```

本步继续攻击 `LowCarrierFixedResidueColumnCRTPDECExclusion`。同步读数为：

```text
residue_to_row_ap_formula_closed=true
single_residue_ap_envelope_closed=true
low_carrier_residue_table_finite_closed=true
ap_envelope_capacity_comparison_proved=false
low_carrier_fixed_residue_excluded=false
row_column_unconditional_closed=false
```

首破裂后行区间记为：

```text
I_y={y,...,P-1},  H=P-y.
```

对固定低 carrier 素数 `q<P` 和固定列 residue `a mod q`，覆盖条件

```text
tP+c == 0 mod q,  c == a mod q
```

等价于：

```text
t == -a P^{-1} mod q.
```

因此同一 `(q,a)` residue cell 在 `I_y` 中最多命中：

```text
ceil(H/q)
```

个行位置。固定阈值 `B` 后，所有 `q<=B` 的低 carrier cell 数至多 `sum_{q<=B} q`，所以低
carrier fixed-residue 压力被写成低维 AP table，而不是无结构的 ColumnCRT 标签。

该出口更新为：

```text
LowCarrierFixedResidueColumnCRTPDECExclusion
  -> LowCarrierResidueAPEnvelopeCapacityComparison
  AND DenseLowCarrierResidueTablePDECExclusion
  AND SparseLowCarrierResidueCellSAESummability
```

本步关闭的是 AP 骨架和命名分流；尚未证明 AP envelope 容量比较，也未排斥稠密 residue table PDEC
或稀疏 cell SAE。

## 167. First-break low-carrier AP exact-envelope 证书

新增文件

```text
experiments/prime_matrix_firstbreak_low_carrier_ap_envelope_router.py
docs/monograph/prime-matrix-firstbreak-low-carrier-ap-envelope-router.md
docs/monograph/prime-matrix-firstbreak-low-carrier-ap-envelope-router.json
data/prime-matrix-firstbreak-low-carrier-ap-envelope-ledger.json
```

本步继续攻击 `LowCarrierResidueAPEnvelopeCapacityComparison`。同步读数为：

```text
cell_count_formula_closed=true
single_cell_sharp_bound_closed=true
all_residues_exact_mass_closed=true
selected_table_envelope_closed=true
ap_capacity_comparison_proved=false
row_column_unconditional_closed=false
```

对任意低 carrier residue table

```text
T subset {(q,a): q<=B, a mod q},
```

在首破裂后行区间 `I_y` 上定义

```text
U_T(I_y)=sum_{(q,a) in T} #{t in I_y: t == -a P^{-1} mod q}.
```

单个 cell 的发生量满足

```text
#{t in I_y: t == -a P^{-1} mod q} <= ceil(H/q),  H=P-y.
```

更关键的是，固定 `q` 后所有 residue cell 精确分割行区间：

```text
sum_{a mod q} #{t in I_y: t == -a P^{-1} mod q} = H.
```

因此任意 table 的形式包络为

```text
U_T(I_y) <= sum_{(q,a) in T} ceil(H/q),
U_T(I_y) <= H * |{q: exists a with (q,a) in T}|.
```

该容量比较出口更新为：

```text
LowCarrierResidueAPEnvelopeCapacityComparison
  -> ActualLowCarrierRowIncidenceDemandLowerBound
  AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC
```

本步关闭的是 AP table 的 exact envelope 公式。尚未证明反例链强制的 actual row-incidence demand
超过该 envelope，也未排斥接近 envelope 的稠密低维 table PDEC；行/列命题仍未无条件闭合。

## 168. First-break actual demand 源侧切口

新增文件

```text
experiments/prime_matrix_firstbreak_actual_demand_source_cut_router.py
docs/monograph/prime-matrix-firstbreak-actual-demand-source-cut-router.md
docs/monograph/prime-matrix-firstbreak-actual-demand-source-cut-router.json
data/prime-matrix-firstbreak-actual-demand-source-cut-ledger.json
```

本步继续攻击 `ActualLowCarrierRowIncidenceDemandLowerBound`。同步读数为：

```text
firstbreak_release_set_imported=true
unit_release_demand_lower_bound_closed=true
unit_demand_not_gap_sufficient=true
no_envelope_recycling_guard=true
release_mass_amplification_proved=false
low_carrier_payment_injection_proved=false
actual_low_carrier_row_incidence_demand_proved=false
row_column_unconditional_closed=false
```

首破裂分裂只给出源侧单位下界：

```text
R_y != empty  =>  D_y >= 1.
```

但 AP exact-envelope 至少可以容纳单个 residue cell 的单位发生，因此 `D_y>=1` 不能推出容量矛盾。
为了避免循环论证，actual demand 必须从零行/首破裂源侧推出，而不能从 AP table 接近饱和反推。

该硬点更新为：

```text
ActualLowCarrierRowIncidenceDemandLowerBound
  -> FirstBreakReleaseMassAmplificationOrSingletonSAE
  AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse
```

也就是说，下一步必须证明首破裂释放沿反例链放大到可与 `H=P-y` 比较；若不放大，则只能作为
singleton/sparse SAE 计费。同时还要证明放大的压力确实非循环地注入同一低 carrier AP table；若不能注入，
则回流到高秩、moving-carrier、PDEC 或 SAE 出口。

## 169. First-break release mass 零行块阶梯

新增文件

```text
experiments/prime_matrix_firstbreak_release_mass_zero_block_ladder_router.py
docs/monograph/prime-matrix-firstbreak-release-mass-zero-block-ladder-router.md
docs/monograph/prime-matrix-firstbreak-release-mass-zero-block-ladder-router.json
data/prime-matrix-firstbreak-release-mass-zero-block-ladder-ledger.json
```

本步继续攻击 `FirstBreakReleaseMassAmplificationOrSingletonSAE`。同步读数为：

```text
contiguous_zero_block_imported=true
boundary_only_amplification_blocked=true
zero_block_cover_obligation_mass_closed=true
block_length_dichotomy_closed=true
short_zero_block_singleton_sae_proved=false
long_zero_block_mass_transfer_proved=false
release_mass_amplification_proved=false
row_column_unconditional_closed=false
```

首破裂边界释放本身只给单位事件；若要得到可与 `H=P-y` 比较的源侧质量，唯一来源是首破裂前的连续零行块。
设 `[x0,y-1]` 为零行块，长度

```text
L = y - x0.
```

则对每个 `t in [x0,y-1]` 和每个 `1<=c<P`，都有某个 `q<P` 覆盖 `tP+c`。因此源侧覆盖义务总量精确为：

```text
L(P-1).
```

对任意阈值 `A>=1`，出现长短二分：

```text
L < A   -> ShortZeroBlockSingletonSAESummability
L >= A  -> LongZeroBlockCoverMassTransferToAPDemandOrPDEC
```

该硬点更新为：

```text
FirstBreakReleaseMassAmplificationOrSingletonSAE
  -> ShortZeroBlockSingletonSAESummability
  AND LongZeroBlockCoverMassTransferToAPDemandOrPDEC
```

本步关闭的是“放大源头定位”：放大不能来自首破裂单位释放，只能来自前置零行块覆盖账本。尚未证明短块
singleton/sparse SAE 可求和，也未证明长块覆盖义务必能非循环转移为 post-break AP demand；若转移失败，
应进入持续覆盖历史 PDEC/ColumnCRT/SAE。

## 170. Long zero-block cover mass 稳定 history 注入路由

新增文件

```text
experiments/prime_matrix_firstbreak_long_zero_block_mass_transfer_router.py
docs/monograph/prime-matrix-firstbreak-long-zero-block-mass-transfer-router.md
docs/monograph/prime-matrix-firstbreak-long-zero-block-mass-transfer-router.json
data/prime-matrix-firstbreak-long-zero-block-mass-transfer-ledger.json
```

本步继续攻击 `LongZeroBlockCoverMassTransferToAPDemandOrPDEC`。同步读数为：

```text
zero_block_cover_obligation_mass_imported=true
history_projection_key_defined=true
no_loss_return_accounting_imported=true
stable_table_or_named_switch_route_registered=true
history_switch_pdec_excluded=false
postbreak_ap_demand_injection_proved=false
long_zero_block_mass_transfer_proved=false
row_column_unconditional_closed=false
```

设长零块为 `B=[x0,y-1]`，其覆盖义务域为：

```text
O_B={(t,c): x0<=t<y, 1<=c<P},   |O_B|=L(P-1).
```

每个覆盖义务 `q | tP+c` 都给出同一 formal unit 内的 history key：

```text
kappa=(q,a),   a == c mod q,   t == -a P^{-1} mod q.
```

这把长零块源质量接到低 carrier AP table 的相位字段上，但仍不能自动推出 post-break demand。利用
no-loss return accounting，义务只有两种合法去向：

```text
stable low-carrier/residue table  ->  PostBreakAPDemandInjectionFromStableHistory
history key/carrier/phase switch  ->  HistorySwitch-PDEC/ColumnCRT/MovingCarrier/SAE
```

于是硬点进一步更新为：

```text
LongZeroBlockCoverMassTransferToAPDemandOrPDEC
  -> ZeroBlockHistoryProjectionNoLossLedger
  AND StableLowCarrierPaymentTableOrHistorySwitchPDEC
  AND PostBreakAPDemandInjectionFromStableHistory
```

本步关闭的是无名逃逸口：长零块质量若稳定，必须进入稳定 history 注入硬点；若不稳定，切换本身必须作为
PDEC/ColumnCRT/MovingCarrier/SAE 命名终端登记。尚未证明稳定 history 必给出 post-break actual demand
下界，也未排斥 history switch 终端；行/列命题仍未无条件闭合。

## 171. Stable history AP 到达/越界二分

新增文件

```text
experiments/prime_matrix_firstbreak_stable_history_ap_arrival_router.py
docs/monograph/prime-matrix-firstbreak-stable-history-ap-arrival-router.md
docs/monograph/prime-matrix-firstbreak-stable-history-ap-arrival-router.json
data/prime-matrix-firstbreak-stable-history-ap-arrival-ledger.json
```

本步继续攻击 `PostBreakAPDemandInjectionFromStableHistory`。同步读数为：

```text
stable_history_route_imported=true
ap_row_class_formula_closed=true
last_prebreak_hit_successor_closed=true
arrival_nonarrival_dichotomy_closed=true
terminal_nonarrival_large_step_registered=true
arrival_candidate_registered=true
arrival_candidate_actual_demand_proved=false
terminal_nonarrival_excluded=false
postbreak_ap_demand_injection_proved=false
row_column_unconditional_closed=false
```

对稳定 history key `kappa=(q,a)`，低 carrier AP 行类为：

```text
t == -a P^{-1} mod q.
```

令 `t_*` 是该 key 在零块 `B=[x0,y-1]` 中的最后一次命中，则下一次同 key 行精确为：

```text
t_next = t_* + q.
```

由 `t_*` 的最后性，`t_next>=y`。因此在 post-break 支撑 `I_y=[y,P-1]` 中有精确二分：

```text
arrival candidate      <=> t_*+q <= P-1 <=> q <= P-1-t_*
terminal nonarrival   <=> t_*+q >= P   <=> q >= P-t_*
```

硬点更新为：

```text
PostBreakAPDemandInjectionFromStableHistory
  -> StableHistoryAPSuccessorDichotomyLedger
  AND ArrivalCandidateActualDemandInjectionWithoutEnvelopeReuse
  AND TerminalNonarrivalLargeStepEscapePDECOrSAE
```

本步关闭的是稳定 history key 的 AP 后继相位门：到达给出 post-break AP cell 候选；未到达说明 AP 周期超过
平方锚前支撑宽度，必须登记为 large-step escape/PDEC/SAE。尚未证明到达候选必然成为 actual demand，
也未排斥 terminal nonarrival 出口；行/列命题仍未无条件闭合。

## 172. Arrival candidate actual demand 单位注入与商化

新增文件

```text
experiments/prime_matrix_firstbreak_arrival_candidate_actual_demand_router.py
docs/monograph/prime-matrix-firstbreak-arrival-candidate-actual-demand-router.md
docs/monograph/prime-matrix-firstbreak-arrival-candidate-actual-demand-router.json
data/prime-matrix-firstbreak-arrival-candidate-actual-demand-ledger.json
```

本步继续攻击 `ArrivalCandidateActualDemandInjectionWithoutEnvelopeReuse`。同步读数为：

```text
arrival_candidate_imported=true
no_envelope_recycling_guard_imported=true
source_tagged_unit_incidence_closed=true
arrival_quotient_map_defined=true
no_loss_collision_return_imported=true
arrival_collision_return_registered=true
distinct_arrival_quotient_lower_bound_proved=false
arrival_collision_return_excluded=false
arrival_candidate_actual_demand_injection_proved=false
row_column_unconditional_closed=false
```

arrival candidate 带有零块源侧 history tag，并满足：

```text
t_next == -a P^{-1} mod q,   y <= t_next <= P-1.
```

因此它非循环地产生一个低 carrier AP row-incidence 单位：

```text
(source tag, t_next, q, a) -> incidence(t_next,q,a).
```

但 raw source-tagged arrivals 不能直接当作聚合 demand。必须先商化：

```text
pi: source-tagged arrivals -> (t_next,q,a).
```

真正可与 AP envelope 比较的是 `|image(pi)|`。若许多源义务塌缩到少数 `(t_next,q,a)`，则塌缩不能被删除，
也不能当作多个独立 demand；它必须进入 quotient、weighted return、duplicate/collision PDEC、ColumnCRT 或 SAE。

硬点更新为：

```text
ArrivalCandidateActualDemandInjectionWithoutEnvelopeReuse
  -> SourceTaggedArrivalUnitIncidenceLedger
  AND DistinctArrivalQuotientDemandLowerBoundOrCollisionPDEC
  AND ArrivalCollisionOrDuplicatePaymentReturnLedger
```

本步关闭的是单位注入与去重口径；尚未证明去重后的 arrival image 足够大，也未排斥碰撞/重复支付终端。
行/列命题仍未无条件闭合。

## 173. Arrival quotient 纤维 envelope

新增文件

```text
experiments/prime_matrix_firstbreak_arrival_quotient_fiber_router.py
docs/monograph/prime-matrix-firstbreak-arrival-quotient-fiber-router.md
docs/monograph/prime-matrix-firstbreak-arrival-quotient-fiber-router.json
data/prime-matrix-firstbreak-arrival-quotient-fiber-ledger.json
```

本步继续攻击 `DistinctArrivalQuotientDemandLowerBoundOrCollisionPDEC`。同步读数为：

```text
source_tagged_unit_incidence_imported=true
arrival_quotient_map_imported=true
fiber_row_factor_closed=true
fiber_column_factor_closed=true
arrival_fiber_envelope_closed=true
weighted_image_lower_bound_formula_closed=true
raw_arrival_mass_after_nonarrival_removal_proved=false
high_fiber_concentration_registered=true
high_fiber_collision_pdec_excluded=false
distinct_arrival_quotient_lower_bound_proved=false
row_column_unconditional_closed=false
```

令 `A` 为 source-tagged arrivals，商化映射为：

```text
pi: A -> (t_next,q,a).
```

固定 image 点 `(t,q,a)`。其源行 `s` 必须满足 `s in [x0,y-1]` 且 `s == t mod q`，所以：

```text
R_B(t,q) <= ceil(L/q).
```

源列 `c` 必须满足 `1<=c<P` 且 `c == a mod q`，所以：

```text
C_P(a,q) <= ceil((P-1)/q).
```

因此 arrival quotient 的原像纤维满足：

```text
|pi^{-1}(t,q,a)| <= ceil(L/q) ceil((P-1)/q).
```

于是得到加权 image 下界：

```text
|image(pi)| >= sum_{u in A} 1/F(pi(u)),
F(t,q,a)=ceil(L/q)ceil((P-1)/q).
```

硬点更新为：

```text
DistinctArrivalQuotientDemandLowerBoundOrCollisionPDEC
  -> ArrivalQuotientFiberMultiplicityEnvelopeLedger
  AND ArrivalRawSourceMassAfterNonarrivalRemoval
  AND WeightedArrivalImageLowerBoundFromFiberEnvelope
  AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn
```

本步关闭的是 arrival quotient 的乘数纪律。尚未证明 terminal nonarrival 去除后的 raw arrival mass 足够大；
若 weighted image 仍太小，则说明压力集中在小 `q`/高纤维或重复碰撞上，必须回流到 dense low-carrier/PDEC/SAE。
行/列命题仍未无条件闭合。

## 174. Arrival raw mass 层平衡与低步长阈值

新增文件

```text
experiments/prime_matrix_firstbreak_arrival_raw_mass_layer_router.py
docs/monograph/prime-matrix-firstbreak-arrival-raw-mass-layer-router.md
docs/monograph/prime-matrix-firstbreak-arrival-raw-mass-layer-router.json
data/prime-matrix-firstbreak-arrival-raw-mass-layer-ledger.json
```

本步继续攻击 `ArrivalRawSourceMassAfterNonarrivalRemoval`。同步读数为：

```text
raw_arrival_mass_imported=true
ap_successor_dichotomy_imported=true
source_layer_universe_defined=true
arrival_nonarrival_source_layer_balance_closed=true
low_step_always_arrives_closed=true
terminal_escape_tail_cutoff_closed=true
raw_arrival_lower_bound_formula_closed=true
low_step_stable_history_mass_lower_bound_proved=false
large_step_tail_escape_registered=true
large_step_tail_escape_excluded=false
raw_arrival_mass_after_nonarrival_removal_proved=false
row_column_unconditional_closed=false
```

令 `S` 为稳定 source-tagged history 层，`A` 为到达层，`E` 为 terminal nonarrival 层。
AP 后继二分给出

```text
S = A disjoint_union E.
```

设 `H=P-y`。对任意 `u in S`，最后零块命中 `t_*(u)<=y-1`。若 `q(u)<=H`，则：

```text
t_*(u)+q(u)<=P-1,
```

故 `u in A`。若 `u in E`，则：

```text
q(u)>=P-t_*(u)>=H+1.
```

于是得到非循环 raw mass 下界：

```text
|A| >= |S_{q<=H}|.
```

硬点更新为：

```text
ArrivalRawSourceMassAfterNonarrivalRemoval
  -> ArrivalNonarrivalSourceLayerBalanceLedger
  AND LowStepStableHistoryAlwaysArrivesLedger
  AND RawArrivalMassLowerBoundFromLowStepHistory
  AND LowStepStableHistoryMassLowerBoundOrLargeStepTailEscapePDEC
```

本步关闭的是 terminal nonarrival 去除的阈值纪律。尚未证明 `S_{q<=H}` 足够厚；
若该层不足，则反例链必须集中到 `q>H` 的大步长尾逃逸，并登记为 PDEC/SAE。
行/列命题仍未无条件闭合。

## 175. Low-step/tail 显式容量 envelope

新增文件

```text
experiments/prime_matrix_firstbreak_lowstep_tail_capacity_router.py
docs/monograph/prime-matrix-firstbreak-lowstep-tail-capacity-router.md
docs/monograph/prime-matrix-firstbreak-lowstep-tail-capacity-router.json
data/prime-matrix-firstbreak-lowstep-tail-capacity-ledger.json
```

本步继续攻击 `LowStepStableHistoryMassLowerBoundOrLargeStepTailEscapePDEC`。同步读数为：

```text
lowstep_mass_imported=true
raw_layer_balance_imported=true
stable_low_tail_partition_closed=true
terminal_tail_row_window_closed=true
tail_column_multiplicity_closed=true
large_step_tail_envelope_closed=true
lowstep_mass_from_total_minus_tail_closed=true
large_step_tail_no_small_lcm_replay_imported=true
stable_total_minus_tail_envelope_gap_proved=false
large_step_tail_saturation_pdec_excluded=false
lowstep_stable_history_mass_lower_bound_proved=false
row_column_unconditional_closed=false
```

令 `S` 为稳定 source-tagged history 层。上一层给出：

```text
S = S_{q<=H} disjoint_union S_{q>H},  H=P-y.
```

其中 `S_{q<=H}` 必到达。现在控制 `S_{q>H}`。若 `u in S_{q>H}` 是 terminal nonarrival，
最后零块命中 `t_*` 必满足：

```text
t_*+q>=P,  t_* in B=[x0,y-1].
```

故

```text
t_* in B ∩ [P-q,y-1],
|B ∩ [P-q,y-1]| <= min(L,q-H).
```

固定 `q,t_*` 后，源列必须满足 `c == -t_*P mod q`，所以列重数至多 `ceil((P-1)/q)`。
于是 tail 容量 envelope 为：

```text
C_tail = sum_{H<q<P} |B ∩ [P-q,y-1]| ceil((P-1)/q),
|S_{q>H}| <= C_tail.
```

从而：

```text
|S_{q<=H}| >= |S| - C_tail.
```

硬点更新为：

```text
LowStepStableHistoryMassLowerBoundOrLargeStepTailEscapePDEC
  -> StableHistoryLowTailMassPartitionLedger
  AND LargeStepTailTerminalWindowEnvelopeLedger
  AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope
  AND StableTotalMinusTailEnvelopeGapOrLargeStepTailSaturationPDEC
```

本步关闭的是 `q>H` terminal tail 的 row-window/column-multiplicity envelope。
尚未证明 `|S|-C_tail` 已超过需求阈值；若不超过，必须把 tail 近饱和、重复支付或逃逸登记为 PDEC/SAE。
行/列命题仍未无条件闭合。

## 176. Stable tail gap functional

新增文件

```text
experiments/prime_matrix_firstbreak_stable_tail_gap_router.py
docs/monograph/prime-matrix-firstbreak-stable-tail-gap-router.md
docs/monograph/prime-matrix-firstbreak-stable-tail-gap-router.json
data/prime-matrix-firstbreak-stable-tail-gap-ledger.json
```

本步继续攻击 `StableTotalMinusTailEnvelopeGapOrLargeStepTailSaturationPDEC`。同步读数为：

```text
tail_gap_imported=true
zero_block_obligation_mass_imported=true
no_loss_accounting_imported=true
stable_total_after_named_returns_closed=true
tail_envelope_imported=true
explicit_tail_gap_functional_closed=true
positive_stable_tail_gap_proved=false
named_return_mass_pdec_excluded=false
stable_total_minus_tail_envelope_gap_proved=false
row_column_unconditional_closed=false
```

零块覆盖义务域为：

```text
O_B={(t,c): x0<=t<y, 1<=c<P},
|O_B|=L(P-1).
```

no-loss 账本给出：

```text
O_B = StableSourceRecords disjoint_union NamedReturnRecords.
```

记命名 return 质量为 `R_named`。上一层已给出：

```text
C_tail = sum_{H<q<P} |B ∩ [P-q,y-1]| ceil((P-1)/q).
```

因此：

```text
|S_{q<=H}| >= L(P-1)-R_named-C_tail.
```

硬点更新为：

```text
StableTotalMinusTailEnvelopeGapOrLargeStepTailSaturationPDEC
  -> ZeroBlockCoverObligationMassLedger
  AND StableSourceTotalAfterNamedReturnsLedger
  AND ExplicitStableTailGapFunctionalLedger
  AND PositiveStableTailGapOrNamedReturnMassPDEC
```

本步关闭的是低步长稳定质量的显式 gap functional。尚未证明该 gap 足够大；
若不够大，必须由 `R_named`、tail saturation、history switch、duplicate/collision 或 PDEC/SAE 账本承载。
行/列命题仍未无条件闭合。

## 177. Tail gap 归一化回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_normalization_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-normalization-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-normalization-router.json
data/prime-matrix-firstbreak-tail-gap-normalization-ledger.json
```

本步继续攻击 `PositiveStableTailGapOrNamedReturnMassPDEC`。同步读数为：

```text
positive_gap_imported=true
explicit_gap_functional_imported=true
tail_index_change_of_variables_closed=true
exact_prime_tail_envelope_closed=true
all_integer_dominating_envelope_closed=true
named_return_separation_closed=true
normalized_positive_gap_proved=false
dense_tail_return_pdec_excluded=false
positive_stable_tail_gap_proved=false
row_column_unconditional_closed=false
```

令 `H=P-y`，对 tail carrier 写 `q=H+r`。因为 `P-q=y-r`，所以 terminal row window 变为：

```text
B ∩ [P-q,y-1] = B ∩ [y-r,y-1],
|B ∩ [P-q,y-1]| = min(L,r).
```

因此上一层 tail envelope 精确归一化为：

```text
C_tail = sum_{prime q=H+r<P} min(L,r) ceil((P-1)/(H+r)).
```

去掉素数限制还给出安全整数上界：

```text
C_tail <= C_all = sum_{1<=r<P-H} min(L,r) ceil((P-1)/(H+r)).
```

gap 分离为：

```text
G_prime = L(P-1)-C_tail,
G = G_prime-R_named.
```

硬点更新为：

```text
PositiveStableTailGapOrNamedReturnMassPDEC
  -> TailIndexChangeOfVariablesLedger
  AND ExactPrimeTailEnvelopeOneDimensionalLedger
  AND StableTailGapNamedReturnSeparationLedger
  AND NormalizedTailGapPositiveOrDenseTailReturnPDEC
```

本步关闭的是 tail window 的变量替换和一维 functional；真正剩余是证明归一化 prime-tail functional 留出正 gap，
或证明 dense tail、tail saturation、`R_named` 过大已经进入 PDEC/SAE。
行/列命题仍未无条件闭合。

## 178. Tail gap 全整数 margin 分裂回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_integer_margin_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-integer-margin-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-integer-margin-router.json
data/prime-matrix-firstbreak-tail-gap-integer-margin-ledger.json
```

本步继续攻击 `NormalizedTailGapPositiveOrDenseTailReturnPDEC`。同步读数为：

```text
normalized_tail_gap_imported=true
one_dimensional_tail_imported=true
integer_margin_functional_closed=true
prime_tail_dominated_by_integer_tail_closed=true
positive_branch_criterion_closed=true
early_half_support_tail_cannot_saturate_closed=true
integer_margin_positive_globally_proved=false
late_support_dense_tail_named_return_pdec_excluded=false
normalized_positive_gap_proved=false
row_column_unconditional_closed=false
```

由上一层 `H=P-y` 与一维 tail 和式，定义全整数上界：

```text
C_all = sum_{1<=r<y} min(L,r) ceil((P-1)/(P-y+r)),
G_int = L(P-1)-C_all.
```

因为 prime tail 是 integer tail 的子和：

```text
C_tail <= C_all,
G_prime=L(P-1)-C_tail >= G_int.
```

于是若 `G_int>R_named`，则：

```text
G=G_prime-R_named>0.
```

前半支撑分支还给出无条件的 pure-tail 不饱和引理。若 `P` 为奇素数且 `y<=floor(P/2)`，则：

```text
ceil((P-1)/(P-y+r)) <= 2,
C_all <= L(2y-L-1),
G_int >= L(P-2y+L)>0.
```

硬点更新为：

```text
NormalizedTailGapPositiveOrDenseTailReturnPDEC
  -> NormalizedIntegerTailMarginFunctionalLedger
  AND PrimeTailDominatedByIntegerTailEnvelopeLedger
  AND EarlyHalfSupportTailCannotSaturateLemma
  AND IntegerMarginPositiveBranchCriterionLedger
  AND IntegerTailMarginPositiveOrLateSupportDenseTailNamedReturnPDEC
```

本步关闭的是前半支撑的 pure-tail 饱和解释。剩余集中为：
late-support dense-tail，或 `R_named` 吃掉整数 margin 的命名 return 质量。
行/列命题仍未无条件闭合。

## 179. Tail gap late-support collar 回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_late_collar_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-late-collar-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-late-collar-router.json
data/prime-matrix-firstbreak-tail-gap-late-collar-ledger.json
```

本步继续攻击 `IntegerTailMarginPositiveOrLateSupportDenseTailNamedReturnPDEC`。同步读数为：

```text
late_dense_imported=true
late_coordinate_closed=true
regular_tail_endpoint_defect_closed=true
late_core_excess_functional_closed=true
late_margin_exact_formula_closed=true
positive_late_margin_criterion_closed=true
deep_late_collar_excluded=false
core_excess_named_return_pdec_excluded=false
late_dense_tail_named_return_proved=false
row_column_unconditional_closed=false
```

在 late branch 写：

```text
P=2m+1, H=P-y, y>m,
D=2y-P, E=y-m-1=(D-1)/2.
```

超过二重的 tail 只来自短 core `1<=r<=E`。当 `r>E` 且 `r<y-1` 时，
`ceil((P-1)/(H+r))=2`；端点 `r=y-1` 对应 `q=P-1`，故 `ceil=1`。

定义：

```text
X_core = sum_{1<=r<=E} min(L,r)(ceil((P-1)/(P-y+r))-2).
```

则全整数 tail 精确分解为：

```text
C_all = L(2y-L-1)+X_core-min(L,y-1).
```

因此：

```text
G_int = L(P-1)-C_all
      = L(L-D)+min(L,y-1)-X_core.
```

若

```text
L(L-D)+min(L,y-1) > X_core+R_named,
```

则正 gap 已成立。硬点更新为：

```text
IntegerTailMarginPositiveOrLateSupportDenseTailNamedReturnPDEC
  -> LateSupportExcessCoordinateLedger
  AND RegularTailTwoUnitEndpointDefectLedger
  AND LateCoreExcessFunctionalLedger
  AND LateCollarMarginExactFormulaLedger
  AND DeepLateShortCollarOrCoreExcessNamedReturnPDEC
```

本步关闭的是 late-support tail 的精确 collar 公式。剩余集中为：
deep-late short collar，或 `X_core/R_named` 吃掉 late margin。
行/列命题仍未无条件闭合。

## 180. Deep-late collar quotient-layer 回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_deep_collar_layer_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-deep-collar-layer-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-deep-collar-layer-router.json
data/prime-matrix-firstbreak-tail-gap-deep-collar-layer-ledger.json
```

本步继续攻击 `DeepLateShortCollarOrCoreExcessNamedReturnPDEC`。同步读数为：

```text
deep_collar_imported=true
mirror_collar_equivalence_closed=true
cross_collar_positive_margin_closed=true
core_layer_decomposition_closed=true
core_or_named_consumption_closed=true
self_mirror_collar_excluded=false
core_layer_concentration_excluded=false
deep_late_closed=false
row_column_unconditional_closed=false
```

令：

```text
x0=y-L, H=P-y, D=2y-P.
```

则 deep-late short collar 有等价式：

```text
L<=D
<=> x0>=H
<=> B=[x0,y-1] subset [H,y-1].
```

所以几何剩余不再是一般 late 支撑，而是自镜像 collar 内部相位问题。

若 `L>D`，则零块跨出 collar。记：

```text
M=L(L-D)+min(L,y-1).
```

上一层给出 `G_int=M-X_core`，因此：

```text
X_core+R_named < M  =>  G>0.
```

若反例仍存在，则必须有：

```text
X_core+R_named >= M.
```

同时 core excess 精确分解到 quotient 层。令：

```text
h=H+r, H+1<=h<=m,
k(h)=ceil((P-1)/h)-2,
I_k={h: ceil((P-1)/h)=k+2}.
```

则：

```text
X_core=sum_{k>=1} k sum_{h in I_k} min(L,h-H).
```

硬点更新为：

```text
DeepLateShortCollarOrCoreExcessNamedReturnPDEC
  -> DeepLateCollarMirrorContainmentLedger
  AND CrossCollarPositiveMarginCriterionLedger
  AND CoreExcessQuotientLayerDecompositionLedger
  AND CoreExcessLayerConcentrationOrNamedReturnPDEC
  AND SelfMirrorDeepLateCollarOrCoreLayerExcessNamedReturnPDEC
```

本步关闭的是 deep-late 的几何等价和 core quotient 层分解。剩余集中为：
自镜像 collar 内部相位，或 quotient core 层/命名 return 对 margin 的显式消耗。
行/列命题仍未无条件闭合。

## 181. Self-mirror tail-gap 筛缺陷回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_sieved_defect_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-sieved-defect-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-sieved-defect-router.json
data/prime-matrix-firstbreak-tail-gap-sieved-defect-ledger.json
```

本步继续攻击 `SelfMirrorDeepLateCollarOrCoreLayerExcessNamedReturnPDEC`。同步读数为：

```text
self_mirror_imported=true
nonprime_defect_exact_closed=true
sqrt_rough_prime_tail_identity_closed=true
endpoint_parity_defect_lower_bound_closed=true
sieved_margin_functional_closed=true
sieved_positive_gap_criterion_closed=true
weighted_rough_crt_defect_excluded=false
self_mirror_sieved_gap_proved=false
row_column_unconditional_closed=false
```

令：

```text
w(q)=min(L,q-H)ceil((P-1)/q), H<q<P.
```

则真实 prime tail 与整数 tail 的差额为精确非素数缺陷：

```text
C_tail=C_all-D_np,
D_np=sum_{H<q<P, q not prime}w(q).
```

取：

```text
z=floor(sqrt(P-1)), W_z=prod_{ell prime, ell<=z} ell.
```

则对 `z<q<P` 有：

```text
q prime <=> gcd(q,W_z)=1.
```

所以 prime tail 精确拆成小素数部分与 sqrt-rough CRT 支撑：

```text
C_tail=sum_{H<q<=z, q prime}w(q)
      +sum_{z<q<P, gcd(q,W_z)=1}w(q).
```

上一层 late collar 公式给出：

```text
G_int=L(L-D)+min(L,y-1)-X_core.
```

加入非素数缺陷后：

```text
G=G_int+D_np-R_named
 =L(L-D)+min(L,y-1)-X_core+D_np-R_named.
```

在 self-mirror 分支 `L<=D` 中：

```text
G=L(L-D)+L-X_core+D_np-R_named.
```

因此若

```text
L(L-D)+min(L,y-1)-X_core+D_np>R_named,
```

则正 gap 已成立。若失败仍存在，则必须是 weighted sqrt-rough CRT 支撑过密，
或 `R_named` 吃掉筛缺陷。硬点更新为：

```text
SelfMirrorDeepLateCollarOrCoreLayerExcessNamedReturnPDEC
  -> PrimeTailNonprimeDefectExactLedger
  AND SqrtRoughPrimeTailIdentityLedger
  AND EndpointParityNonprimeDefectLowerBoundLedger
  AND SievedTailGapMarginFunctionalLedger
  AND SievedPositiveGapCriterionLedger
  AND WeightedRoughTailCRTDefectOrNamedReturnPDEC
  AND SelfMirrorSievedTailGapOrWeightedRoughCRTDefectPDEC
```

本步关闭的是素/非素数缺陷恒等式、sqrt-rough 精确身份和筛后 margin。
剩余集中为：weighted rough tail 的 CRT 过密或命名 return 质量过大。
行/列命题仍未无条件闭合。

## 182. Weighted rough tail LPF 删除债务回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_lpf_deletion_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-deletion-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-deletion-router.json
data/prime-matrix-firstbreak-tail-gap-lpf-deletion-ledger.json
```

本步继续攻击 `SelfMirrorSievedTailGapOrWeightedRoughCRTDefectPDEC`。同步读数为：

```text
weighted_rough_target_imported=true
small_tail_finite_nonprime_defect_closed=true
large_tail_lpf_partition_closed=true
rough_prefix_deletion_telescoping_closed=true
lpf_crt_deletion_cell_closed=true
lpf_sieved_gap_functional_closed=true
dyadic_lpf_deletion_debt_excluded=false
lpf_deletion_debt_proved_impossible=false
row_column_unconditional_closed=false
```

沿用：

```text
w(q)=min(L,q-H)ceil((P-1)/q),
z=floor(sqrt(P-1)).
```

先扣出小端非素数质量：

```text
D_small=sum_{H<q<=z, q not prime}w(q).
```

对大端 `z<q<P`，每个非素数都有唯一最小素因子 `ell<=z`，故：

```text
B_ell=sum_{z<q<P, ell=lpf(q)}w(q),
D_large=sum_{ell<=z}B_ell,
D_np=D_small+D_large.
```

每个删除层有 CRT 形式：

```text
B_ell=sum_{z/ell<n<P/ell, gcd(n,W_<ell)=1}w(ell*n),
W_<ell=prod_{p<ell}p.
```

令 `W_u=prod_{p<=u}p` 与：

```text
S_u=sum_{z<q<P, gcd(q,W_u)=1}w(q).
```

按素数 `ell` 递增筛时：

```text
S_{ell^-}-S_ell=B_ell,
S_0-S_z=sum_{ell<=z}B_ell.
```

设：

```text
Phi=L(L-D)+min(L,y-1)-X_core.
```

则真实 gap 为：

```text
G=Phi+D_small+sum_{ell<=z}B_ell-R_named.
```

若反例仍存在，则必须满足：

```text
sum B_ell<=R_named-Phi-D_small.
```

硬点更新为：

```text
SelfMirrorSievedTailGapOrWeightedRoughCRTDefectPDEC
  -> SmallTailFiniteNonprimeDefectLedger
  AND LargeTailLeastPrimeFactorPartitionLedger
  AND RoughPrefixDeletionTelescopingLedger
  AND LeastPrimeFactorCRTDeletionCellLedger
  AND SievedGapLPFDeletionFunctionalLedger
  AND DyadicLPFDeletionDebtOrNamedReturnPDEC
  AND LPFDeletionDebtOrRoughPrefixOverdensityPDEC
```

本步关闭的是 LPF 唯一分区、前缀删除 telescoping 与 CRT 删除单元。
剩余集中为：dyadic 最小素因子层删除质量不足，或命名 return 吃掉这些删除。
行/列命题仍未无条件闭合。

## 183. LPF 删除债务 dyadic cofactor 回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_lpf_dyadic_cofactor_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-dyadic-cofactor-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-dyadic-cofactor-router.json
data/prime-matrix-firstbreak-tail-gap-lpf-dyadic-cofactor-ledger.json
```

本步继续攻击 `LPFDeletionDebtOrRoughPrefixOverdensityPDEC`。同步读数为：

```text
lpf_debt_imported=true
dyadic_layer_partition_closed=true
debt_localization_closed=true
ramp_saturated_weight_split_closed=true
quotient_layer_cofactor_interval_closed=true
cofactor_interval_endpoint_formula_closed=true
rough_cofactor_interval_crt_support_closed=true
dyadic_rough_cofactor_interval_debt_excluded=false
row_column_unconditional_closed=false
```

把 LPF 删除层

```text
B_ell=sum_{z<q<P, ell=lpf(q)}w(q)
```

按 dyadic 最小素因子层重组为

```text
B_Y=sum_{Y<ell<=2Y, ell prime}B_ell,
B_tot=sum_Y B_Y.
```

若 `B_tot<=T<sum_Y A_Y`，则至少有一层 `B_Y<A_Y`。这不是额外平均假设，
而是纯粹的有限分层定位：总删除债务不能支付候选预算时，债务必落在某个
dyadic 局部层。

层内再写

```text
w(q)=u(q)v(q),
u(q)=min(L,q-H),
v(q)=ceil((P-1)/q).
```

于是支撑分成 ramp 层 `H<q<H+L` 与 saturated 层 `q>=H+L`。再按

```text
Q_j={q: ceil((P-1)/q)=j}
```

分块。令 `A=P-1`，则

```text
q_j_min=floor(A/j)+1,
q_j_max=A              if j=1,
q_j_max=floor(A/(j-1)) if j>=2.
```

与 tail、ramp/saturated 边界相交后，固定 `ell` 的 cofactor 区间端点为：

```text
ramp:      q_min=max(z+1,H+1,q_j_min),   q_max=min(P-1,H+L-1,q_j_max),
saturated: q_min=max(z+1,H+L,q_j_min),   q_max=min(P-1,q_j_max),
n_min=ceil(q_min/ell),                   n_max=floor(q_max/ell).
```

因此每个局部单元具有显式 CRT 支撑：

```text
B_{Y,sigma,j}=
sum_{Y<ell<=2Y} sum_{n_min<=n<=n_max, gcd(n,W_<ell)=1} u(ell*n)j.
```

硬点更新为：

```text
LPFDeletionDebtOrRoughPrefixOverdensityPDEC
  -> DyadicLPFDeletionLayerPartitionLedger
  AND DyadicDebtLocalizationForAnyBudgetVectorLedger
  AND RampSaturatedTailWeightSplitLedger
  AND QuotientLayerCofactorIntervalLedger
  AND CofactorIntervalEndpointFormulaLedger
  AND RoughCofactorIntervalCRTSupportLedger
  AND DyadicRoughCofactorIntervalDebtOrNamedReturnPDEC
  AND DyadicRoughCofactorIntervalDebtOrColumnCRTPDEC
```

本步关闭的是 dyadic 分层、预算定位、权重分裂、quotient 分块与 cofactor 区间端点公式。
剩余集中为：某个 dyadic/quotient/cofactor interval 的 rough CRT 支撑仍可能删除质量不足，
或其失败必须进一步登记为 ColumnCRT/PDEC/SAE。行/列命题仍未无条件闭合。

## 184. cofactor-LPF 覆盖债务回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_cofactor_lpf_cover_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-cover-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-cover-router.json
data/prime-matrix-firstbreak-tail-gap-cofactor-lpf-cover-ledger.json
```

本步继续攻击 `DyadicRoughCofactorIntervalDebtOrColumnCRTPDEC`。同步读数为：

```text
dyadic_cofactor_debt_imported=true
weighted_envelope_closed=true
support_quota_criterion_closed=true
cofactor_lpf_partition_closed=true
cofactor_lpf_crt_cell_closed=true
product_width_dichotomy_closed=true
local_cofactor_lpf_cover_debt_excluded=false
row_column_unconditional_closed=false
```

固定上一层 cell `C=(Y,sigma,j)`，写

```text
alpha_{ell,n}=j*u(ell*n).
```

全整数权重包络、rough 支撑质量与被 cofactor 小因子删除质量为：

```text
F_C=sum_{ell in Y} sum_{n in I_{ell,j,sigma}} alpha_{ell,n},
B_C=sum_{ell in Y} sum_{n in I_{ell,j,sigma}, gcd(n,W_<ell)=1} alpha_{ell,n},
E_C=F_C-B_C.
```

若该 cell 的目标预算为 `A_C`，则局部 rough 支撑债务等价于：

```text
B_C<A_C  <=>  E_C>F_C-A_C.
```

也就是说，支撑不足不再是黑箱，而是 cofactor 小素因子覆盖过量。对每个被删除的
cofactor 按最小素因子分区：

```text
r=lpf(n)<ell,
E_C=sum_{ell in Y} sum_{r<ell} E_{r<-ell}.
```

每个分区又有短区间 CRT 形式：

```text
n=r*m,
gcd(m,W_<r)=1,
ceil(n_min/r)<=m<=floor(n_max/r).
```

若局部覆盖债务使用 distinct cofactor primes `R_C`，其完整相位字周期为：

```text
M_R=prod_{r in R_C}r.
```

当 `M_R` 超过 cell 支撑宽度时，同一覆盖字不能由局部短周期漂移稳定复现，只能登记为
有限原子、ColumnCRT/PDEC，或转入更深的 moving-support 出口。

硬点更新为：

```text
DyadicRoughCofactorIntervalDebtOrColumnCRTPDEC
  -> CofactorCellWeightedEnvelopeLedger
  AND RoughSupportQuotaCriterionLedger
  AND CofactorLeastPrimeFactorPartitionLedger
  AND CofactorLPFCRTCellLedger
  AND CofactorCoverPrimeProductWidthLedger
  AND LocalCofactorLPFCoverDebtOrFiniteAtomPDEC
  AND CofactorLPFCoverDebtOrProductWidthColumnCRTPDEC
```

本步关闭的是 cell 权重包络、quota 等价、cofactor 最小素因子分区、CRT cell 与
product-width 登记。剩余集中为：cofactor-LPF 过覆盖债务本身，或 product-width
ColumnCRT/PDEC 出口。行/列命题仍未无条件闭合。

## 185. cofactor-LPF dyadic pressure 回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_cofactor_lpf_dyadic_pressure_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-dyadic-pressure-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-dyadic-pressure-router.json
data/prime-matrix-firstbreak-tail-gap-cofactor-lpf-dyadic-pressure-ledger.json
```

本步继续攻击 `CofactorLPFCoverDebtOrProductWidthColumnCRTPDEC`。同步读数为：

```text
cofactor_lpf_cover_debt_imported=true
excess_threshold_closed=true
active_prime_product_dichotomy_closed=true
dyadic_r_partition_closed=true
overfull_localization_closed=true
fixed_r_m_endpoint_closed=true
r_layer_crt_closed=true
small_product_concentration_excluded=false
dyadic_pressure_excluded=false
row_column_unconditional_closed=false
```

上一层给出 `B_C<A_C <=> E_C>F_C-A_C`。本步记

```text
H_C=F_C-A_C.
```

因此局部反例要求：

```text
E_C>H_C.
```

令活动 cofactor primes 为：

```text
R_C={r prime: E_r(C)>0},
M_C=prod_{r in R_C}r.
```

若 `M_C>width(C)`，完整覆盖相位字的周期超过 cell 支撑宽度，必须进入 product-width
ColumnCRT/PDEC 或有限原子出口。若 `M_C<=width(C)`，反例只能集中在 small-product
active cover 上。

再按 dyadic `r` 层分解：

```text
E_C=sum_Z E_Z(C),
M_C=prod_Z M_Z.
```

若候选允许预算满足

```text
sum_Z U_Z<=H_C
```

而反例要求 `E_C>H_C`，则存在至少一个 dyadic 层：

```text
E_Z(C)>U_Z.
```

固定 `r` 后，cofactor 区间给出更低阶 rough-m CRT 单元：

```text
n=r*m,
m_min=ceil(n_min/r),
m_max=floor(n_max/r),
gcd(m,W_<r)=1.
```

硬点更新为：

```text
CofactorLPFCoverDebtOrProductWidthColumnCRTPDEC
  -> CofactorCoverExcessThresholdLedger
  AND ActiveCofactorPrimeProductDichotomyLedger
  AND DyadicCofactorPrimePressurePartitionLedger
  AND OverfullDyadicRLayerLocalizationLedger
  AND FixedRToMIntervalEndpointLedger
  AND RLayerRoughMCRTSupportLedger
  AND SmallProductActiveCoverConcentrationPDEC
  AND DyadicCofactorLPFPressureOrSmallProductColumnCRTPDEC
```

本步关闭的是 excess 阈值、active product-width 二分、dyadic `r` 压力定位和 fixed-r
rough-m CRT 端点。剩余集中为：dyadic `r` 层过载，或 small-product active cover
的 ColumnCRT/PDEC。行/列命题仍未无条件闭合。

## 186. cofactor-LPF single-r pressure 回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_cofactor_lpf_single_r_pressure_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-single-r-pressure-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-single-r-pressure-router.json
data/prime-matrix-firstbreak-tail-gap-cofactor-lpf-single-r-pressure-ledger.json
```

本步继续攻击 `DyadicCofactorLPFPressureOrSmallProductColumnCRTPDEC`。同步读数为：

```text
dyadic_pressure_imported=true
active_prime_cardinality_closed=true
small_z_finite_atom_boundary_closed=true
single_r_pressure_localization_closed=true
fixed_r_source_ell_partition_closed=true
fixed_r_ell_rough_m_crt_cell_closed=true
fixed_pair_product_width_closed=true
single_r_pressure_excluded=false
row_column_unconditional_closed=false
```

在 dyadic 层 `Z<r<=2Z` 中，活动集合为：

```text
R_Z(C)={r: Z<r<=2Z, E_r(C)>0}.
```

`Z<2` 的最低层作为有限小素因子原子边界单独登记。对 `Z>=2`，若仍处于 small-product 分支：

```text
M_Z=prod_{r in R_Z(C)}r <= W_C=width(C),
```

则每个活动 `r>Z` 给出活动个数界：

```text
|R_Z(C)| <= K_Z=floor(log W_C/log Z).
```

若 dyadic 层仍超预算：

```text
E_Z(C)>U_Z,
```

则必存在单个活动素因子：

```text
E_r(C)>U_Z/K_Z.
```

固定 `r` 后按源 `ell` 分区：

```text
E_r(C)=sum_{ell in Y, ell>r}E_{r<-ell}(C).
```

于是超预算继续落到固定 `(r,ell)`，其单元为：

```text
q=ell*r*m,
m_min=ceil(n_min/r),
m_max=floor(n_max/r),
gcd(m,W_<r)=1,
alpha_{ell,r*m}=j*u(ell*r*m).
```

硬点更新为：

```text
DyadicCofactorLPFPressureOrSmallProductColumnCRTPDEC
  -> ActivePrimeCardinalityFromProductLedger
  AND SmallZFiniteAtomBoundaryLedger
  AND SingleCofactorPrimePressureLocalizationLedger
  AND FixedRSourceEllPartitionLedger
  AND FixedREllRoughMCRTCellLedger
  AND FixedPairProductWidthColumnCRTExitLedger
  AND SingleRSmallProductPressurePDEC
  AND SingleCofactorPrimePressureOrFixedPairMCRTColumnCRTPDEC
```

本步关闭的是 small-product 活动个数界、低层有限原子边界、single-r 压力定位与
fixed-pair rough-m CRT 形式。剩余集中为：single-r/fixed-pair pressure，或 fixed-pair
ColumnCRT/PDEC。行/列命题仍未无条件闭合。

## 187. fixed-pair second-LPF descent 回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_fixed_pair_second_lpf_descent_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-fixed-pair-second-lpf-descent-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-fixed-pair-second-lpf-descent-router.json
data/prime-matrix-firstbreak-tail-gap-fixed-pair-second-lpf-descent-ledger.json
```

本步继续攻击 `SingleCofactorPrimePressureOrFixedPairMCRTColumnCRTPDEC`。同步读数为：

```text
fixed_pair_pressure_imported=true
m_support_strict_descent_closed=true
m_equals_one_finite_atom_closed=true
second_lpf_partition_closed=true
second_lpf_crt_cell_closed=true
second_product_width_closed=true
strict_no_cycle_closed=true
second_lpf_pressure_excluded=false
row_column_unconditional_closed=false
```

固定 `(r,ell)` 后：

```text
q=ell*r*m,
m_min<=m<=m_max,
gcd(m,W_<r)=1,
beta_m=j*u(ell*r*m).
```

`m=1` 只给出单点 `q=ell*r`，登记为有限原子。对 `m>1`，由
`gcd(m,W_<r)=1` 得：

```text
s=lpf(m)>=r.
```

于是：

```text
m=s*t,
gcd(t,W_<s)=1,
t_min=ceil(m_min/s),
t_max=floor(m_max/s).
```

并有互不重叠分区：

```text
E_{r<-ell}=E_{m=1}+sum_{s>=r}E_{s<-r,ell}.
```

记 `width_m=m_max-m_min+1`，则固定 `s` 后：

```text
width_t<=ceil(width_m/s)<=ceil(width_m/r).
```

非有限分支 `r>=2`，因此若 `width_m>1`，二级递降后的支撑严格变小；若
`width_m<=1`，直接进入有限原子。这给出 non-cycle 证书：fixed-pair pressure
不能在同一支撑尺度上循环。

硬点更新为：

```text
SingleCofactorPrimePressureOrFixedPairMCRTColumnCRTPDEC
  -> FixedPairPressureImportedLedger
  AND FixedPairMSupportStrictDescentLedger
  AND MEqualsOneFiniteAtomLedger
  AND SecondCofactorLeastPrimeFactorPartitionLedger
  AND SecondLPFRoughTCRTCellLedger
  AND SecondLPFProductWidthColumnCRTExitLedger
  AND ResidualSupportWidthStrictDecreaseNoCycleLedger
  AND SecondLPFDescentPressureOrTripleMCRTColumnCRTPDEC
```

本步关闭的是 fixed-pair 下的 m=1 有限原子、二级 LPF 分区、rough-t CRT 形式、
product-width 登记与支撑宽度严格下降。剩余集中为：二级 LPF/triple pressure，
或二级 product-width ColumnCRT/PDEC。行/列命题仍未无条件闭合。

## 188. iterated LPF rank-budget 回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_iterated_lpf_rank_budget_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-iterated-lpf-rank-budget-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-iterated-lpf-rank-budget-router.json
data/prime-matrix-firstbreak-tail-gap-iterated-lpf-rank-budget-ledger.json
```

本步继续攻击 `SecondLPFDescentPressureOrTripleMCRTColumnCRTPDEC`。同步读数为：

```text
second_lpf_triple_pressure_imported=true
ordered_residual_chain_closed=true
support_product_reciprocity_closed=true
depth_rank_budget_closed=true
iterated_crt_word_cell_closed=true
product_width_exit_closed=true
terminal_residual_finite_atom_closed=true
well_founded_no_cycle_closed=true
rank_budgeted_moving_family_excluded=false
row_column_unconditional_closed=false
```

固定 `(r,ell,s)` 后：

```text
q=ell*r*m,
m=s*t,
s=lpf(m)>=r,
gcd(t,W_<s)=1.
```

若 residual `n_i>1`，递归取：

```text
a_i=lpf(n_i),
n_i=a_i*n_{i+1},
gcd(n_{i+1},W_<a_i)=1.
```

于是 LPF 因子词非降：

```text
r<=s<=a_1<=a_2<=...
```

令：

```text
A_h=s*prod_{i<=h}a_i.
```

原 m 支撑宽度为 `width_m`。支撑-周期互反不变量为：

```text
width(n_h-support)<=ceil(width_m/A_h).
```

若仍未进入 product-width 出口，则 `A_h<=width_m`。非有限分支中所有因子至少为
`r>=2`，所以含初始二级因子 `s` 的总深度 `d` 满足：

```text
d<=floor(log_r(width_m)).
```

硬点更新为：

```text
SecondLPFDescentPressureOrTripleMCRTColumnCRTPDEC
  -> SecondLPFTriplePressureImportedLedger
  AND IteratedLPFOrderedRoughResidualChainLedger
  AND LPFSupportProductReciprocityInvariantLedger
  AND LPFDepthRankBudgetLedger
  AND IteratedLPFCRTWordCellLedger
  AND IteratedLPFProductWidthColumnCRTExitLedger
  AND TerminalResidualFiniteAtomLedger
  AND IteratedLPFWellFoundedNoCycleLedger
  AND RankBudgetedIteratedLPFMovingFamilyOrColumnCRTPDEC
```

本步关闭的是迭代 LPF 的有序分解、支撑-周期互反不变量、有限秩预算、终端有限原子
与 product-width ColumnCRT/PDEC 出口。剩余集中为：随 `P` 移动的低秩因子词族。
行/列命题仍未无条件闭合。

## 189. LPF word-entropy / first-moving-coordinate 回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_lpf_word_entropy_motion_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-word-entropy-motion-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-word-entropy-motion-router.json
data/prime-matrix-firstbreak-tail-gap-lpf-word-entropy-motion-ledger.json
```

本步继续攻击 `RankBudgetedIteratedLPFMovingFamilyOrColumnCRTPDEC`。同步读数为：

```text
rank_budgeted_moving_family_imported=true
word_signature_partition_closed=true
word_entropy_finite_cap_closed=true
aggregate_to_single_word_closed=true
fixed_word_columncrt_exit_closed=true
first_moving_coordinate_closed=true
moving_coordinate_support_reciprocity_closed=true
anonymous_moving_family_removed=true
first_moving_coordinate_pressure_excluded=false
row_column_unconditional_closed=false
```

由 LPF 唯一性，每个 residual 落入唯一有序 word：

```text
omega=(s,a_1,...,a_d),
r<=s<=a_1<=...<=a_d,
A(omega)=s*prod_{i<=d}a_i.
```

若 `A(omega)>W`，其中 `W` 是原 m 支撑宽度，则回到 product-width
ColumnCRT/PDEC 或有限原子。否则：

```text
A(omega)<=W,
d+1<=floor(log_r W).
```

所以活动 word 集 `Omega(P,C)` 有有限熵预算 `H(W,r)`。聚合压力满足：

```text
E(Omega)=sum_{omega in Omega}E_omega.
```

若 `E(Omega)>U`，则存在单个 word：

```text
E_omega>U/|Omega|.
```

承压 word 若在族中素坐标和相位残基稳定，则它不是 moving-family，而是固定 MCRT word，
进入 `FixedLPFWordColumnCRTExit`。若不稳定，则存在首个移动坐标 `mu`，其前缀乘积
`A_prefix` 稳定，并有：

```text
width_after_mu<=ceil(W/(A_prefix*mu)).
```

若 `A_prefix*mu>W`，直接进入 ColumnCRT/PDEC 或有限原子；否则剩余只可能是首移动
LPF 坐标压力。

硬点更新为：

```text
RankBudgetedIteratedLPFMovingFamilyOrColumnCRTPDEC
  -> RankBudgetedMovingFamilyImportedLedger
  AND IteratedLPFWordSignaturePartitionLedger
  AND LPFWordEntropyFiniteCapLedger
  AND AggregatePressureToSingleLPFWordLedger
  AND FixedLPFWordColumnCRTExitLedger
  AND FirstMovingLPFCoordinateLedger
  AND MovingCoordinateSupportReciprocityLedger
  AND NoAnonymousRankBudgetedMovingFamilyLedger
  AND FirstMovingLPFCoordinatePressureOrWordMotionColumnCRTPDEC
```

本步关闭的是匿名 rank-budgeted moving-family 口径；剩余集中为首移动 LPF 坐标的
相位/容量压力，或 word-motion ColumnCRT/PDEC。行/列命题仍未无条件闭合。

## 190. first-moving LPF coordinate 回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_first_moving_lpf_coordinate_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-first-moving-lpf-coordinate-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-first-moving-lpf-coordinate-router.json
data/prime-matrix-firstbreak-tail-gap-first-moving-lpf-coordinate-ledger.json
```

本步继续攻击 `FirstMovingLPFCoordinatePressureOrWordMotionColumnCRTPDEC`。同步读数为：

```text
first_moving_coordinate_pressure_imported=true
stable_prefix_product_support_closed=true
effective_width_closed=true
low_coordinate_finite_atom_closed=true
dyadic_coordinate_partition_closed=true
active_product_width_exit_closed=true
active_count_bound_closed=true
single_coordinate_pressure_localized=true
fixed_coordinate_columncrt_exit_closed=true
anonymous_coordinate_pool_removed=true
single_coordinate_drift_excluded=false
row_column_unconditional_closed=false
```

首移动坐标 `mu` 前的 LPF word 前缀稳定，记：

```text
A_prefix=stable prefix product,
W_prefix=floor(W/A_prefix).
```

若 `mu>W_prefix`，则 `A_prefix*mu>W`，直接进入 product-width ColumnCRT/PDEC 或有限原子。
低坐标 `mu<=2` 也只给出有限原子。其余活动坐标落入有限 dyadic 层：

```text
B<mu<=2B,
B=2^b,
B>=2,
B<=W_prefix.
```

固定一层，令活动坐标集合为 `M_B`：

```text
P_B=prod_{mu in M_B}mu.
```

若 `P_B>W_prefix`，进入 ColumnCRT/PDEC 或有限原子；若 `P_B<=W_prefix`，则：

```text
|M_B|<=floor(log W_prefix/log B).
```

因此 dyadic 层聚合压力若超界，必须定位到单个坐标：

```text
E_mu>U_B/|M_B|.
```

若该 `mu` 稳定，则回到固定 word 坐标的 Prefix/ColumnCRT/PDEC；若它随 `P` 漂移，
进入新的单坐标漂移硬点。

硬点更新为：

```text
FirstMovingLPFCoordinatePressureOrWordMotionColumnCRTPDEC
  -> FirstMovingLPFCoordinatePressureImportedLedger
  AND StablePrefixProductSupportLedger
  AND FirstMovingCoordinateEffectiveWidthLedger
  AND LowMovingCoordinateFiniteAtomLedger
  AND FirstMovingCoordinateDyadicPartitionLedger
  AND MovingCoordinateActiveProductWidthExitLedger
  AND MovingCoordinateActiveCountBoundLedger
  AND SingleMovingCoordinatePressureLocalizationLedger
  AND FixedMovingCoordinateDegeneratesToColumnCRTLedger
  AND NoAnonymousFirstMovingCoordinatePoolLedger
  AND SingleMovingLPFCoordinateDriftOrPrefixColumnCRTPDEC
```

本步关闭的是匿名首移动坐标池；剩余集中为单个 moving LPF coordinate drift，
或 prefix ColumnCRT/PDEC。行/列命题仍未无条件闭合。

## 191. single-moving LPF coordinate scale-escape 回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_single_moving_lpf_coordinate_scale_escape_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-single-moving-lpf-coordinate-scale-escape-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-single-moving-lpf-coordinate-scale-escape-router.json
data/prime-matrix-firstbreak-tail-gap-single-moving-lpf-coordinate-scale-escape-ledger.json
```

本步继续攻击 `SingleMovingLPFCoordinateDriftOrPrefixColumnCRTPDEC`。同步读数为：

```text
single_coordinate_drift_imported=true
stable_prefix_closed=true
dyadic_scale_closed=true
bounded_scale_degenerates_closed=true
unbounded_scale_escape_closed=true
post_coordinate_support_descent_closed=true
same_scale_cycle_excluded=true
sparse_drift_registered=true
anonymous_single_coordinate_drift_removed=true
scale_escaping_coordinate_excluded=false
sparse_drift_sae_summability_proved=false
row_column_unconditional_closed=false
```

单坐标漂移保留上一层稳定前缀，记：

```text
W_prefix=floor(W/A_prefix).
```

对移动坐标 `mu` 定义 dyadic 尺度：

```text
B(mu)=2^floor(log_2 mu),
B(mu)<=mu<=2B(mu).
```

若 `B(mu)` 在无限子族中有界，则 `mu` 只可能取有限多个素值；由无限鸽巢，
存在固定 `mu` 的无限子族，故回到固定坐标 ColumnCRT/PDEC 或有限原子。因而真正
的 moving drift 必须满足 `B(mu)->infty`。

加入 `mu` 后，后继 residual 支撑宽度满足：

```text
W_after<=ceil(W_prefix/mu)<=ceil(W_prefix/B(mu)).
```

在非有限分支中 `B(mu)>=2`，所以后继支撑严格下降，排除同尺度循环。若漂移事件不
形成持久同尺度压力，则只登记为 sparse drift/SAE 质量；本步不证明该 SAE 全局可求和。

硬点更新为：

```text
SingleMovingLPFCoordinateDriftOrPrefixColumnCRTPDEC
  -> SingleMovingLPFCoordinateDriftImportedLedger
  AND SingleMovingCoordinateStablePrefixLedger
  AND SingleMovingCoordinateDyadicScaleLedger
  AND BoundedScaleDriftDegeneratesToFixedCoordinateLedger
  AND UnboundedCoordinateScaleEscapeLedger
  AND PostMovingCoordinateSupportDescentLedger
  AND SameScaleCoordinateCycleExcludedLedger
  AND SparseCoordinateDriftSAERegistrationLedger
  AND NoAnonymousSingleCoordinateDriftLedger
  AND ScaleEscapingSingleCoordinateDescentOrSparseDriftSAEColumnCRTPDEC
```

本步关闭的是有界尺度匿名漂移和同尺度循环；剩余集中为尺度逃逸单坐标递降族，
或 sparse drift/SAE/ColumnCRT/PDEC。行/列命题仍未无条件闭合。

## 192. scale-escape support-clock 回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_scale_escape_support_clock_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-scale-escape-support-clock-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-scale-escape-support-clock-router.json
data/prime-matrix-firstbreak-tail-gap-scale-escape-support-clock-ledger.json
```

本步继续攻击 `ScaleEscapingSingleCoordinateDescentOrSparseDriftSAEColumnCRTPDEC`。同步读数为：

```text
scale_escape_descent_imported=true
integer_support_clock_closed=true
halving_clock_descent_closed=true
finite_depth_per_fiber_closed=true
terminal_width_one_finite_atom_closed=true
scale_ladder_product_width_exit_closed=true
persistent_scale_ladder_signature_registered=true
sparse_scale_ladder_sae_registered=true
cyclic_scale_escape_descent_excluded=true
anonymous_scale_escape_descent_removed=true
persistent_scale_ladder_excluded=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

对有效支撑宽度 `W` 定义整数时钟：

```text
K(W)=ceil(log_2 max(W,1)).
```

真实尺度逃逸层满足 `B_i>=2` 且：

```text
W_{i+1}<=ceil(W_i/B_i)<=ceil(W_i/2).
```

所以当 `W_i>=2` 时：

```text
K(W_{i+1})<=K(W_i)-1.
```

这给出非循环单调量：同一反例纤维上的尺度逃逸步数至多 `K(W_0)`，不能回到同一
支撑时钟层。若递降到 `W<=1`，进入有限原子或命名边界；若尺度阶梯乘积越过初始
支撑：

```text
prod_i B_i>W_0,
```

则合成周期超过支撑，进入 ColumnCRT/PDEC 或有限原子。剩余无限族不能再作为匿名
scale-escape descent 存在，必须登记为持久有序尺度阶梯签名；非持久事件进入 sparse
scale-ladder SAE。

硬点更新为：

```text
ScaleEscapingSingleCoordinateDescentOrSparseDriftSAEColumnCRTPDEC
  -> ScaleEscapingSingleCoordinateDescentImportedLedger
  AND ScaleEscapeIntegerSupportClockLedger
  AND ScaleEscapeHalvingClockDescentLedger
  AND FiniteDepthScaleEscapePerFiberLedger
  AND TerminalWidthOneFiniteAtomLedger
  AND ScaleLadderProductWidthColumnCRTExitLedger
  AND PersistentScaleLadderSignatureRegistrationLedger
  AND SparseScaleLadderSAERegistrationLedger
  AND NoCyclicScaleEscapeDescentLedger
  AND NoAnonymousScaleEscapeDescentLedger
  AND PersistentScaleLadderSignatureOrSparseScaleLadderSAEColumnCRTPDEC
```

本步关闭的是抽象 scale-escape 内循环和匿名递降口径；剩余集中为持久尺度阶梯签名，
或 sparse scale-ladder SAE/ColumnCRT/PDEC。行/列命题仍未无条件闭合。

## 193. scale-ladder word-entropy 回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_scale_ladder_word_entropy_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-scale-ladder-word-entropy-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-scale-ladder-word-entropy-router.json
data/prime-matrix-firstbreak-tail-gap-scale-ladder-word-entropy-ledger.json
```

本步继续攻击 `PersistentScaleLadderSignatureOrSparseScaleLadderSAEColumnCRTPDEC`。同步读数为：

```text
persistent_scale_ladder_imported=true
dyadic_word_partition_closed=true
product_budget_closed=true
word_entropy_finite_cap_closed=true
aggregate_to_single_scale_word_closed=true
fixed_scale_ladder_columncrt_exit_closed=true
first_moving_scale_ladder_phase_localized=true
sparse_scale_ladder_sae_carried_forward=true
anonymous_persistent_scale_ladder_removed=true
first_moving_scale_ladder_phase_excluded=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

持久尺度阶梯由 dyadic 指数词表示：

```text
B_i=2^{b_i}, b_i>=1,
sigma=(b_1,...,b_d),
A_sigma=prod_i B_i=2^{sum_i b_i}.
```

若 `A_sigma>W_0`，已经进入 product-width ColumnCRT/PDEC 或有限原子；否则：

```text
sum_i b_i<=K_0=ceil(log_2 max(W_0,1)).
```

正整数有序组成给出有限尺度词数：

```text
N_ladder(K_0)=1+sum_{n=1}^{K_0}2^{n-1}<=2^{K_0}.
```

因此持久尺度阶梯不能作为匿名无限容量池。若聚合压力：

```text
E_total=sum_sigma E_sigma
```

超出预算 `U`，则某个尺度词满足：

```text
E_sigma>U/N_ladder(K_0).
```

对该承压尺度词，若实际素坐标和相位残基在无限子族中稳定，则回到固定
MCRT/ColumnCRT/PDEC 或有限原子；若不稳定，则存在首个移动素坐标或相位残基。

硬点更新为：

```text
PersistentScaleLadderSignatureOrSparseScaleLadderSAEColumnCRTPDEC
  -> PersistentScaleLadderSignatureImportedLedger
  AND ScaleLadderDyadicWordPartitionLedger
  AND ScaleLadderProductBudgetLedger
  AND ScaleLadderWordEntropyFiniteCapLedger
  AND AggregatePersistentPressureToSingleScaleWordLedger
  AND FixedScaleLadderMCRTColumnCRTExitLedger
  AND FirstMovingScaleLadderPhaseCoordinateLedger
  AND SparseScaleLadderSAECarriedForwardLedger
  AND NoAnonymousPersistentScaleLadderSignatureLedger
  AND FirstMovingScaleLadderPhaseDriftOrSparseScaleLadderSAEColumnCRTPDEC
```

本步关闭的是匿名持久尺度阶梯签名池和尺度词聚合压力口径；剩余集中为固定尺度词内
首个移动素坐标/相位漂移，或 sparse scale-ladder SAE/ColumnCRT/PDEC。行/列命题仍未无条件闭合。

## 194. scale-ladder finite-slot lock 回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_scale_ladder_finite_slot_lock_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-scale-ladder-finite-slot-lock-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-scale-ladder-finite-slot-lock-router.json
data/prime-matrix-firstbreak-tail-gap-scale-ladder-finite-slot-lock-ledger.json
```

本步继续攻击 `FirstMovingScaleLadderPhaseDriftOrSparseScaleLadderSAEColumnCRTPDEC`。同步读数为：

```text
first_moving_scale_ladder_phase_imported=true
fixed_scale_word_slot_closed=true
finite_prime_choices_per_slot_closed=true
finite_residue_choices_per_slot_closed=true
finite_actual_scale_ladder_atom_set_closed=true
infinite_pigeonhole_stable_actual_ladder_closed=true
persistent_first_moving_scale_ladder_phase_excluded=true
stable_actual_ladder_columncrt_exit_closed=true
sparse_scale_ladder_sae_carried_forward=true
anonymous_first_moving_scale_ladder_phase_removed=true
sparse_scale_ladder_sae_summability_proved=false
stable_actual_ladder_columncrt_pdec_excluded=false
row_column_unconditional_closed=false
```

固定尺度词：

```text
sigma=(b_1,...,b_d), b_i fixed
```

后，每个槽的实际素数只能来自有限集合：

```text
Q_i={q prime: 2^{b_i}<=q<2^{b_i+1}}.
```

固定 `q in Q_i` 后，相位残基 `a_i in Z/qZ` 也有限。于是固定尺度词下实际
素数-相位词数量满足粗上界：

```text
N_actual(sigma)<=prod_i sum_{q in Q_i} q < infinity.
```

若该尺度词在无限子族中持久承压，则由无限鸽巢存在稳定实际素数-相位词子族；
该子族是固定 MCRT cell，回到 ColumnCRT/PDEC 或有限原子。不能在任一实际词上
持久复现的事件只登记为 sparse scale-ladder SAE。

硬点更新为：

```text
FirstMovingScaleLadderPhaseDriftOrSparseScaleLadderSAEColumnCRTPDEC
  -> FirstMovingScaleLadderPhaseDriftImportedLedger
  AND FixedScaleWordSlotLedger
  AND FinitePrimeChoicesPerScaleSlotLedger
  AND FiniteResidueChoicesPerPrimeSlotLedger
  AND FiniteActualScaleLadderAtomSetLedger
  AND InfinitePigeonholeStableActualScaleLadderLedger
  AND NoPersistentFirstMovingScaleLadderPhaseDriftLedger
  AND StableActualScaleLadderMCRTColumnCRTExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterFiniteSlotLockLedger
  AND NoAnonymousFirstMovingScaleLadderPhaseDriftLedger
  AND SparseScaleLadderSAESummabilityOrStableActualLadderColumnCRTPDEC
```

本步关闭的是固定尺度词内持久首移动素坐标/相位漂移；剩余集中为稳定实际 ladder
的 ColumnCRT/PDEC 出口，或 sparse scale-ladder SAE 全局求和问题。行/列命题仍未无条件闭合。

## 195. stable-ladder Fourier/PDEC 回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_fourier_pdec_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-fourier-pdec-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-fourier-pdec-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-fourier-pdec-ledger.json
```

本步继续攻击 `SparseScaleLadderSAESummabilityOrStableActualLadderColumnCRTPDEC`。
同步读数为：

```text
stable_ladder_or_sparse_sae_imported=true
finite_group_closed=true
zero_mean_cell_function_closed=true
exact_excess_identity_closed=true
fourier_pdec_bridge_closed=true
nontrivial_character_lower_bound_closed=true
anonymous_stable_ladder_columncrt_removed=true
sparse_scale_ladder_sae_carried_forward=true
stable_ladder_fourier_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

稳定实际 ladder 被写成有限乘积群上的固定点位：

```text
G=prod_i Z/q_iZ,
N=|G|=prod_i q_i,
tau(n)=(n mod q_i)_i,
a=(a_i)_i.
```

令零均值点位函数

```text
F_a(g)=1_{g=a}-1/N.
```

则对任意支撑 `S` 有精确超额恒等式：

```text
E_a(S)=sum_{n in S}F_a(tau(n))
      =#{n in S:tau(n)=a}-|S|/N.
```

在有限群 `G` 上作 Fourier 展开，平凡角色系数为零，并得到：

```text
E_a(S)=sum_{chi!=1} hat F_a(chi) * S_chi,
S_chi=sum_{n in S}chi(tau(n)).
```

若 `E_a(S)>0`，则存在非平凡角色满足：

```text
max_{chi!=1}|S_chi| >= N*E_a(S)/(N-1).
```

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderColumnCRTPDEC
  -> StableActualLadderOrSparseSAEImportedLedger
  AND StableActualLadderFiniteGroupLedger
  AND StableActualLadderZeroMeanCellFunctionLedger
  AND StableActualLadderExactExcessIdentityLedger
  AND StableActualLadderFourierPDECBridgeLedger
  AND StableActualLadderNontrivialCharacterLowerBoundLedger
  AND NoAnonymousStableActualLadderColumnCRTExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterFourierBridgeLedger
  AND SparseScaleLadderSAESummabilityOrStableActualLadderFourierPDECCap
```

本步关闭的是匿名 stable actual ladder ColumnCRT 出口：它已被改写为显式
Fourier/PDEC 角色和下界。剩余没有消失，而是集中为 stable ladder Fourier/PDEC
cap，或 sparse scale-ladder SAE 全局求和问题。行/列命题仍未无条件闭合。

## 196. stable-ladder pivot-fiber PDEC 回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_pivot_fiber_pdec_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-pivot-fiber-pdec-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-pivot-fiber-pdec-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-pivot-fiber-pdec-ledger.json
```

本步继续攻击 `SparseScaleLadderSAESummabilityOrStableActualLadderFourierPDECCap`。
同步读数为：

```text
stable_ladder_fourier_cap_imported=true
character_factorization_closed=true
nontrivial_pivot_coordinate_closed=true
complement_fiber_partition_closed=true
global_character_to_pivot_fiber_localization_closed=true
primitive_pivot_character_correlation_closed=true
anonymous_fourier_cap_removed=true
sparse_scale_ladder_sae_carried_forward=true
primitive_fiber_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

任一非平凡角色都可写成坐标角色乘积：

```text
chi(g)=prod_i chi_i(g_i).
```

取 `chi_j` 非平凡的 pivot 坐标 `j`。令：

```text
G_{-j}=prod_{i!=j} Z/q_iZ,
|G_{-j}|=N/q_j,
S_h={n in S: tau_{-j}(n)=h}.
```

定义纤维角色和：

```text
A_h=sum_{n in S_h} chi_j(n mod q_j).
```

则：

```text
S_chi=sum_h chi_{-j}(h) * A_h
```

并由三角不等式得到：

```text
|S_chi|<=sum_h |A_h|<=|G_{-j}| max_h |A_h|.
```

所以若 `|S_chi|>=Lambda`，则存在补坐标纤维 `h` 使：

```text
|A_h|>=Lambda/|G_{-j}|.
```

代入上一层 `Lambda=N*E_a(S)/(N-1)` 与 `|G_{-j}|=N/q_j`，得到原子阈值：

```text
|A_h|>=q_j*E_a(S)/(N-1).
```

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderFourierPDECCap
  -> StableActualLadderFourierCapImportedLedger
  AND StableLadderCharacterFactorizationLedger
  AND StableLadderNontrivialPivotCoordinateLedger
  AND StableLadderComplementFiberPartitionLedger
  AND StableLadderGlobalCharacterToPivotFiberLocalizationLedger
  AND StableLadderPrimitivePivotCharacterCorrelationLedger
  AND NoAnonymousStableLadderFourierCapLedger
  AND SparseScaleLadderSAECarriedForwardAfterPivotFiberLedger
  AND SparseScaleLadderSAESummabilityOrStableActualLadderPrimitiveFiberPDECCap
```

本步关闭的是匿名 stable ladder Fourier cap：它必落到某个单素数模数 `q_j`
与固定补坐标纤维上的原子相位相关。剩余集中为 primitive pivot-fiber PDEC cap，
或 sparse scale-ladder SAE 全局求和问题。行/列命题仍未无条件闭合。

## 197. stable-ladder residue-count PDEC 回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_residue_count_pdec_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-residue-count-pdec-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-residue-count-pdec-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-residue-count-pdec-ledger.json
```

本步继续攻击 `SparseScaleLadderSAESummabilityOrStableActualLadderPrimitiveFiberPDECCap`。
同步读数为：

```text
primitive_fiber_pdec_imported=true
residue_count_vector_closed=true
zero_mean_deviation_closed=true
character_to_residue_deviation_closed=true
residue_imbalance_localization_closed=true
residue_imbalance_threshold_closed=true
anonymous_primitive_character_exit_removed=true
sparse_scale_ladder_sae_carried_forward=true
residue_count_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

在上一层固定的 pivot 坐标 `j` 与补坐标纤维 `S_h` 内，定义：

```text
L=|S_h|,
M_r=#{n in S_h: n mod q_j=r},
D_r=M_r-L/q_j.
```

则：

```text
sum_r D_r=0.
```

上一层的 primitive fiber 角色和满足：

```text
A_h=sum_{n in S_h} chi_j(n mod q_j)=sum_r M_r chi_j(r).
```

由于 `chi_j` 非平凡，`sum_r chi_j(r)=0`，所以：

```text
A_h=sum_r D_r chi_j(r).
```

三角不等式给出：

```text
|A_h|<=sum_r |D_r|<=q_j max_r |D_r|.
```

代入上一层阈值 `|A_h|>=q_j*E_a(S)/(N-1)`，得到存在余数 `r` 使：

```text
|M_r-L/q_j|>=E_a(S)/(N-1).
```

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderPrimitiveFiberPDECCap
  -> StableActualLadderPrimitiveFiberPDECImportedLedger
  AND StableLadderPivotFiberResidueCountVectorLedger
  AND StableLadderPivotFiberZeroMeanDeviationLedger
  AND StableLadderPivotFiberCharacterToResidueDeviationLedger
  AND StableLadderPivotFiberResidueImbalanceLocalizationLedger
  AND StableLadderPivotFiberResidueImbalanceThresholdLedger
  AND NoAnonymousPrimitiveFiberCharacterPDECExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterResidueCountLedger
  AND SparseScaleLadderSAESummabilityOrStableActualLadderResidueCountPDECCap
```

本步关闭的是匿名 primitive fiber 角色相关出口：它被改写为固定补坐标纤维中的
单余数类计数偏差。剩余集中为 residue-count PDEC cap，或 sparse scale-ladder
SAE 全局求和问题。行/列命题仍未无条件闭合。

## 198. stable-ladder positive-surplus PDEC 回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_positive_surplus_pdec_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-positive-surplus-pdec-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-positive-surplus-pdec-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-positive-surplus-pdec-ledger.json
```

本步继续攻击 `SparseScaleLadderSAESummabilityOrStableActualLadderResidueCountPDECCap`。
同步读数为：

```text
residue_count_pdec_imported=true
sign_dichotomy_closed=true
zero_sum_transfer_closed=true
positive_surplus_localization_closed=true
positive_surplus_threshold_closed=true
anonymous_signed_imbalance_removed=true
sparse_scale_ladder_sae_carried_forward=true
positive_surplus_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

沿用上一层固定纤维内的偏差向量：

```text
D_r=M_r-L/q_j,
sum_r D_r=0.
```

上一层给出 `|D_r|>=delta`，其中：

```text
delta=E_a(S)/(N-1).
```

若 `D_r>=delta`，则直接得到正余数过载。若 `D_r<=-delta`，则零和给出：

```text
sum_{s!=r}D_s=-D_r>=delta.
```

因此某个 `s!=r` 满足：

```text
D_s>=delta/(q_j-1).
```

统一写成：

```text
M_s-L/q_j>=E_a(S)/((N-1)(q_j-1)).
```

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderResidueCountPDECCap
  -> StableActualLadderResidueCountPDECImportedLedger
  AND StableLadderResidueDeviationSignDichotomyLedger
  AND StableLadderResidueDeviationZeroSumTransferLedger
  AND StableLadderPositiveResidueSurplusLocalizationLedger
  AND StableLadderPositiveResidueSurplusThresholdLedger
  AND NoAnonymousSignedResidueImbalanceExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterPositiveSurplusLedger
  AND SparseScaleLadderSAESummabilityOrStableActualLadderPositiveResidueSurplusPDECCap
```

本步关闭的是有符号 residue-count 绝对偏差出口：亏损分支由零和关系转移为
某个余数类正过载。剩余集中为 positive residue-surplus PDEC cap，或 sparse
scale-ladder SAE 全局求和问题。行/列命题仍未无条件闭合。

## 199. stable-ladder occupancy-dichotomy 回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_occupancy_dichotomy_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-occupancy-dichotomy-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-occupancy-dichotomy-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-occupancy-dichotomy-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableActualLadderPositiveResidueSurplusPDECCap`。
同步读数为：

```text
positive_surplus_imported=true
integer_occupancy_closed=true
singleton_or_pair_dichotomy_closed=true
singleton_surplus_atom_registered=true
same_cell_pair_congruence_closed=true
same_cell_pair_period_multiple_closed=true
anonymous_positive_surplus_removed=true
sparse_scale_ladder_sae_carried_forward=true
singleton_surplus_sae_summability_proved=false
same_cell_pair_period_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层给出固定补坐标纤维与 pivot 余数类中的正过载：

```text
M_s-L/q_j>=eta,
eta=E_a(S)/((N-1)(q_j-1))>0.
```

由于 `M_s` 是非负整数，故 `M_s>=1`。于是只剩下两个互斥出口：

```text
M_s=1  OR  M_s>=2.
```

`M_s=1` 分支登记为 singleton surplus atom；本步不证明其全局求和。
若 `M_s>=2`，则同一完整 stable-ladder cell 中存在两点 `n1<n2`。
令：

```text
W=lcm_i(q_i).
```

同一完整 cell 强制两点在所有 ladder 坐标上同余，因此：

```text
n2-n1 is a nonzero multiple of W.
```

若上游另有支撑宽度界 `H<W`，则 same-cell pair 分支可立即排斥；否则它成为
显式 same-cell period-pair PDEC/cap 输入。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderPositiveResidueSurplusPDECCap
  -> StableActualLadderPositiveResidueSurplusImportedLedger
  AND StableLadderOverloadedCellIntegerOccupancyLedger
  AND StableLadderPositiveSurplusSingletonOrPairDichotomyLedger
  AND StableLadderSingletonSurplusAtomRegistrationLedger
  AND StableLadderSameCellPairCongruenceLedger
  AND StableLadderSameCellPairPeriodMultipleLedger
  AND NoAnonymousPositiveResidueSurplusExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterOccupancyDichotomyLedger
  AND SparseScaleLadderSAESummabilityOrStableActualLadderSingletonSurplusOrCellPairPeriodPDECCap
```

本步关闭的是匿名 positive residue-surplus 出口：它被改写为 singleton atom
或同 cell period-pair 的显式二分。剩余集中为 singleton surplus atom 的全局
可求和、same-cell period-pair PDEC/cap，或 sparse scale-ladder SAE 全局求和。
行/列命题仍未无条件闭合。

## 200. stable-ladder singleton/pair width 回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_singleton_pair_width_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-singleton-pair-width-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-singleton-pair-width-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-singleton-pair-width-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableActualLadderSingletonSurplusOrCellPairPeriodPDECCap`。
同步读数为：

```text
singleton_pair_imported=true
singleton_low_fiber_quota_closed=true
pair_support_width_dichotomy_closed=true
short_support_pair_excluded=true
long_width_pair_registered=true
anonymous_singleton_or_pair_removed=true
sparse_scale_ladder_sae_carried_forward=true
low_fiber_singleton_summability_proved=false
long_width_pair_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

singleton 分支满足：

```text
M_s=1,
M_s-L/q_j>=eta>0.
```

因此：

```text
1-L/q_j>0,
L<q_j.
```

所以 singleton surplus atom 不能留在高 pivot 纤维中；它只能作为低纤维事件
继续求和/排斥。

pair 分支满足：

```text
n2-n1=tW, t>=1, W=lcm_i(q_i).
```

若承载支撑直径为 `H`，则必有：

```text
H>=n2-n1>=W.
```

因此 `H<W` 的短支撑分支排斥同 cell period-pair；只有 `H>=W` 的长宽度
分支保留为显式 PDEC/cap。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderSingletonSurplusOrCellPairPeriodPDECCap
  -> StableActualLadderSingletonOrPairPeriodImportedLedger
  AND StableLadderSingletonSurplusLowFiberQuotaLedger
  AND StableLadderSameCellPairSupportWidthDichotomyLedger
  AND StableLadderShortSupportPairExclusionLedger
  AND StableLadderLongWidthSameCellPeriodPairRegistrationLedger
  AND NoAnonymousSingletonOrPairPeriodExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterSingletonPairWidthLedger
  AND SparseScaleLadderSAESummabilityOrStableActualLadderLowFiberSingletonSurplusOrLongWidthCellPairPDECCap
```

本步关闭的是匿名 singleton/pair 出口：singleton 被限制到低纤维 `L<q_j`，
pair 被限制到长宽度 `H>=W`。剩余集中为低纤维 singleton 全局求和、长宽度
same-cell period-pair PDEC/cap，或 sparse scale-ladder SAE 全局求和。行/列
命题仍未无条件闭合。

## 201. stable-ladder low-fiber phase 回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_low_fiber_phase_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-low-fiber-phase-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-low-fiber-phase-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-low-fiber-phase-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableActualLadderLowFiberSingletonSurplusOrLongWidthCellPairPDECCap`。
同步读数为：

```text
low_fiber_or_long_pair_imported=true
low_fiber_occupancy_dichotomy_closed=true
isolated_singleton_atom_registered=true
repeated_pivot_modulus_forces_isolation=true
anti_pivot_complement_pair_closed=true
complement_period_and_antipivot_phase_closed=true
complement_pair_width_dichotomy_closed=true
long_full_cell_pair_carried_forward=true
anonymous_low_fiber_singleton_removed=true
sparse_scale_ladder_sae_carried_forward=true
isolated_singleton_summability_proved=false
anti_pivot_complement_pair_pdec_cap_proved=false
long_full_cell_pair_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

低纤维 singleton 分支满足：

```text
M_s=1,
1<=L<q_j.
```

因此只有：

```text
L=1 OR 2<=L<q_j.
```

`L=1` 分支登记为补坐标纤维孤立 singleton atom。若 `2<=L<q_j`，取
singleton 点和同补纤维内另一点；二者补坐标相同但 pivot 残基不同。令：

```text
W_-j=lcm_{i!=j}(q_i), empty lcm=1.
```

则：

```text
W_-j | (n2-n1),
q_j does not divide (n2-n1).
```

若 `q_j|W_-j`，固定补坐标已决定 pivot 残基，因此 `M_s=1` 强制 `L=1`；
非孤立分支必须是真正的 anti-pivot 相位不对齐。

若承载支撑直径为 `H`，补纤维双点还给出：

```text
H>=W_-j.
```

因此 `H<W_-j` 的短支撑分支排斥补纤维双点；`H>=W_-j` 保留为
anti-pivot complement-pair PDEC/cap。上一层 `H>=W=lcm_i(q_i)` 的
full-cell long pair 继续前传。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderLowFiberSingletonSurplusOrLongWidthCellPairPDECCap
  -> StableActualLadderLowFiberSingletonOrLongPairImportedLedger
  AND StableLadderLowFiberOccupancyOneOrMultiDichotomyLedger
  AND StableLadderFiberIsolatedSingletonAtomLedger
  AND StableLadderRepeatedPivotModulusForcesIsolationLedger
  AND StableLadderComplementFiberAntiPivotPairLedger
  AND StableLadderComplementFiberPeriodAndAntiPivotPhaseLedger
  AND StableLadderComplementFiberPairWidthDichotomyLedger
  AND StableLadderLongFullCellPairCarriedForwardLedger
  AND NoAnonymousLowFiberSingletonExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterLowFiberPhaseLedger
  AND SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrAntiPivotComplementPairOrLongFullCellPairPDECCap
```

本步关闭的是匿名低纤维 singleton 出口：它被改写为孤立 singleton atom
或补周期对齐但 pivot 反对齐的 complement-pair。剩余集中为孤立 singleton
全局求和、anti-pivot complement-pair PDEC/cap、long full-cell pair PDEC/cap，
或 sparse scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

## 202. stable-ladder pair quotient-phase 回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_pair_quotient_phase_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-pair-quotient-phase-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-pair-quotient-phase-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-pair-quotient-phase-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrAntiPivotComplementPairOrLongFullCellPairPDECCap`。
同步读数为：

```text
isolated_or_pair_imported=true
isolated_singleton_carried_forward=true
complement_base_period_closed=true
pair_difference_quotient_normalized=true
pivot_phase_quotient_period_closed=true
anti_pivot_nonzero_quotient_phase_closed=true
full_cell_zero_quotient_phase_closed=true
pair_quotient_width_envelope_closed=true
quotient_nowrap_or_period_dichotomy_closed=true
anonymous_pair_branches_removed=true
sparse_scale_ladder_sae_carried_forward=true
isolated_singleton_summability_proved=false
pair_quotient_phase_cycle_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

对 anti-pivot complement pair 与 long full-cell pair 统一取补坐标基周期：

```text
B=W_-j=lcm_{i!=j}(q_i), empty lcm=1.
```

pair 差值写为：

```text
d=n2-n1=tB, t>=1.
```

设：

```text
g=gcd(q_j,B),
R=q_j/g.
```

则 pivot 相位 `d mod q_j` 只由 `t mod R` 决定。于是：

```text
anti-pivot complement pair <=> t not congruent 0 mod R,
full-cell pair <=> t congruent 0 mod R, equivalently t=R*u.
```

承载支撑直径 `H` 给出：

```text
1<=t<=floor(H/B).
```

因此若 `floor(H/B)<R`，quotient 相位尚未完成一个 pivot 周期；若
`floor(H/B)>=R`，则 quotient 区间已包含完整相位周期块。该周期块是新的
显式 PDEC/cap 输入。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrAntiPivotComplementPairOrLongFullCellPairPDECCap
  -> StableActualLadderIsolatedSingletonOrPairImportedLedger
  AND StableLadderIsolatedSingletonCarriedForwardLedger
  AND StableLadderComplementBasePeriodLedger
  AND StableLadderPairDifferenceQuotientNormalizationLedger
  AND StableLadderPivotPhaseQuotientPeriodLedger
  AND StableLadderAntiPivotPairNonzeroQuotientPhaseLedger
  AND StableLadderFullCellPairZeroQuotientPhaseLedger
  AND StableLadderPairQuotientWidthEnvelopeLedger
  AND StableLadderQuotientNoWrapOrFullPeriodDichotomyLedger
  AND NoAnonymousAntiPivotOrFullPairExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterPairQuotientPhaseLedger
  AND SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrPairQuotientPhaseCyclePDECCap
```

本步关闭的是分散的 pair 出口：anti-pivot 与 full-cell pair 被统一成
补周期商变量 `t` 的非零/零 pivot 相位。剩余集中为孤立 singleton 全局求和、
quotient phase cycle PDEC/cap，或 sparse scale-ladder SAE 全局求和。行/列
命题仍未无条件闭合。

## 203. stable-ladder quotient short-arc/mean 回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_quotient_phase_arc_mean_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-phase-arc-mean-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-phase-arc-mean-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-phase-arc-mean-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrPairQuotientPhaseCyclePDECCap`。
同步读数为：

```text
quotient_phase_cycle_imported=true
isolated_singleton_carried_forward=true
quotient_span_parameter_closed=true
nowrap_zero_phase_exclusion_closed=true
short_arc_cluster_registered=true
full_cycle_euclidean_decomposition_closed=true
full_cycle_formal_phase_mean_closed=true
full_cycle_residual_tail_arc_closed=true
anonymous_quotient_cycle_removed=true
sparse_scale_ladder_sae_carried_forward=true
isolated_singleton_summability_proved=false
quotient_short_arc_cluster_cap_proved=false
phase_cycle_actual_mean_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

沿用上一层记号：

```text
B=W_-j,
g=gcd(q_j,B),
R=q_j/g,
d=n2-n1=tB.
```

支撑直径给出：

```text
T=floor(H/B), 1<=t<=T.
```

若 `T<R`，则 `t=1,...,T` 在 `Z/RZ` 中是真短弧，且不含零相位。
因此 no-wrap 分支中 full-cell pair 不可能，实际 pair 只能登记为
`QuotientShortArcCluster`。

若 `T>=R`，写：

```text
T=aR+s, a=floor(T/R)>=1, 0<=s<R.
```

完整周期给出 formal phase mean：每个 pivot 相位在每个完整周期中出现一次，
`a` 个完整周期给出同样次数 `a`；尾段 `s<R` 回到 no-wrap 短弧。这里不把
formal mean 当成 actual load 证明，只把剩余压成 actual-mean cap 或短弧 cap。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrPairQuotientPhaseCyclePDECCap
  -> StableActualLadderQuotientPhaseCycleImportedLedger
  AND StableLadderIsolatedSingletonCarriedForwardAfterArcMeanLedger
  AND StableLadderQuotientSpanParameterLedger
  AND StableLadderQuotientNoWrapZeroPhaseExclusionLedger
  AND StableLadderQuotientShortArcClusterLedger
  AND StableLadderFullCycleEuclideanDecompositionLedger
  AND StableLadderFullCycleFormalPhaseMeanLedger
  AND StableLadderFullCycleResidualTailArcLedger
  AND NoAnonymousQuotientPhaseCycleExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterArcMeanLedger
  AND SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrQuotientShortArcClusterOrPhaseCycleMeanPDECCap
```

本步关闭的是匿名 quotient cycle 口径：它被拆成 no-wrap 真短弧聚集、完整
周期 formal mean 与尾弧。剩余集中为孤立 singleton 全局求和、
quotient short-arc cluster cap、phase-cycle actual-mean cap，或 sparse
scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

## 204. stable-ladder quotient arc Fourier 回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_quotient_arc_fourier_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-arc-fourier-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-arc-fourier-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-arc-fourier-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrQuotientShortArcClusterOrPhaseCycleMeanPDECCap`。
同步读数为：

```text
short_arc_or_mean_imported=true
isolated_singleton_carried_forward=true
quotient_circle_group_closed=true
actual_phase_load_measure_closed=true
arc_discrepancy_functional_closed=true
dirichlet_kernel_identity_closed=true
nontrivial_frequency_lower_bound_closed=true
phase_mean_as_point_arc_closed=true
anonymous_short_arc_or_mean_removed=true
sparse_scale_ladder_sae_carried_forward=true
isolated_singleton_summability_proved=false
quotient_arc_fourier_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

沿用 quotient 相位记号：

```text
C_R=Z/RZ,
R=q_j/gcd(q_j,B),
d=n2-n1=tB.
```

把 actual quotient witnesses 按相位计数：

```text
mu(r)=#{actual witnesses: t congruent r mod R}.
```

按完整周期均值或同一 actual-load 口径期望中心化：

```text
nu(r)=mu(r)-model(r),
sum_{r mod R}nu(r)=0.
```

对任意弧 `A subset C_R`，定义短弧/点弧偏差：

```text
Delta(A)=sum_{r in A}nu(r).
```

short-arc cluster 是真短弧的 `Delta(A)>0`；phase-cycle actual-mean cap 是
点弧 `A={r0}` 的同一情形。Fourier 变换给出：

```text
Delta(A)=(1/R) sum_{h=1}^{R-1} hat nu(h) hat 1_A(-h).
```

令：

```text
Lambda_R(A)=sum_{h=1}^{R-1}|hat 1_A(h)|.
```

若 `Delta(A)>0`，则存在非平凡频率满足：

```text
|hat nu(h)| >= R*Delta(A)/Lambda_R(A).
```

这把 short-arc cluster 与 phase-cycle actual-mean cap 统一为 quotient arc
Fourier/PDEC cap。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrQuotientShortArcClusterOrPhaseCycleMeanPDECCap
  -> StableLadderQuotientShortArcOrMeanImportedLedger
  AND StableLadderIsolatedSingletonCarriedForwardAfterQuotientFourierLedger
  AND StableLadderQuotientCircleGroupLedger
  AND StableLadderQuotientActualPhaseLoadMeasureLedger
  AND StableLadderQuotientArcDiscrepancyFunctionalLedger
  AND StableLadderQuotientDirichletKernelIdentityLedger
  AND StableLadderQuotientNontrivialFrequencyLowerBoundLedger
  AND StableLadderPhaseMeanCapAsPointArcLedger
  AND NoAnonymousShortArcOrPhaseMeanExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterQuotientFourierLedger
  AND SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrQuotientArcFourierPDECCap
```

本步关闭的是匿名 short-arc/phase-mean 口径。剩余集中为孤立 singleton 全局
求和、quotient arc Fourier/PDEC cap，或 sparse scale-ladder SAE 全局求和。
行/列命题仍未无条件闭合。

## 205. stable-ladder quotient Fourier lift 回接

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_quotient_fourier_lift_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-fourier-lift-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-fourier-lift-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-fourier-lift-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrQuotientArcFourierPDECCap`。
同步读数为：

```text
quotient_arc_fourier_imported=true
isolated_singleton_carried_forward=true
nontrivial_frequency_forces_r_gt_one=true
quotient_coprime_factorization_closed=true
quotient_inverse_lift_closed=true
quotient_character_to_pivot_difference_closed=true
lifted_character_nontriviality_closed=true
endpoint_bilinear_phase_factorization_closed=true
centered_model_kernel_separated=true
anonymous_quotient_arc_fourier_removed=true
sparse_scale_ladder_sae_carried_forward=true
isolated_singleton_summability_proved=false
endpoint_bilinear_fourier_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

沿用 `d=n2-n1=tB`。令：

```text
g=gcd(q_j,B),
B=gB0,
q_j=gR.
```

则：

```text
gcd(B0,R)=1.
```

取 `uB0 == 1 mod R`。因为：

```text
d/g == tB0 mod R,
```

所以：

```text
t == u*(d/g) mod R.
```

对任意非平凡 quotient 频率 `h`，设 `beta == h*u mod R`，则在 actual
pair witnesses 上有：

```text
e_R(h*t)=e_{q_j}(beta*d).
```

且 `beta` 非零于 `mod R`，所以提升后的 pivot-difference 角色非平凡。
再用 `d=n2-n1`：

```text
e_{q_j}(beta*(n2-n1))
  = e_{q_j}(beta*n2) * conjugate(e_{q_j}(beta*n1)).
```

因此 quotient arc Fourier 异常不是抽象相位异常，而是原始 pair 两端点的
显式双线性相位相关。中心化项仍按 actual-load 纪律分离：

```text
hat nu(h)=actual endpoint bilinear phase sum - explicit model kernel.
```

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrQuotientArcFourierPDECCap
  -> StableLadderQuotientArcFourierImportedLedger
  AND StableLadderIsolatedSingletonCarriedForwardAfterFourierLiftLedger
  AND StableLadderNontrivialQuotientFrequencyForcesRGreaterOneLedger
  AND StableLadderQuotientCoprimeFactorizationLedger
  AND StableLadderQuotientInverseLiftLedger
  AND StableLadderQuotientCharacterToPivotDifferenceLedger
  AND StableLadderLiftedCharacterNontrivialityLedger
  AND StableLadderEndpointBilinearPhaseFactorizationLedger
  AND StableLadderCenteredModelKernelSeparatedLedger
  AND NoAnonymousQuotientArcFourierExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterFourierLiftLedger
  AND SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrQuotientEndpointBilinearFourierPDECCap
```

本步关闭的是匿名 quotient arc Fourier 口径。剩余集中为孤立 singleton 全局
求和、endpoint bilinear Fourier/PDEC cap，或 sparse scale-ladder SAE 全局求和。
行/列命题仍未无条件闭合。

## 206. stable-ladder endpoint bilinear balance 三分

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_bilinear_balance_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-bilinear-balance-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-bilinear-balance-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-bilinear-balance-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrQuotientEndpointBilinearFourierPDECCap`。
同步读数为：

```text
endpoint_bilinear_fourier_imported=true
isolated_singleton_carried_forward=true
endpoint_pair_matrix_registered=true
endpoint_centered_kernel_total_zero=true
endpoint_marginal_balanced_decomposition_closed=true
endpoint_bilinear_phase_pairing_closed=true
endpoint_bilinear_triangle_trichotomy_closed=true
endpoint_row_marginal_fourier_exit_registered=true
endpoint_column_marginal_fourier_exit_registered=true
endpoint_balanced_core_energy_lower_bound_registered=true
anonymous_endpoint_bilinear_removed=true
sparse_scale_ladder_sae_carried_forward=true
isolated_singleton_summability_proved=false
endpoint_marginal_fourier_pdec_cap_proved=false
balanced_bilinear_energy_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

把 actual pair witnesses 按端点余数登记为二部矩阵：

```text
x=n1 mod q_j,
y=n2 mod q_j,
M(x,y)=# actual pair witnesses with endpoints (x,y).
```

减去上一层显式 model/Dirichlet kernel 得中心化核：

```text
K(x,y)=M(x,y)-Model(x,y),
sum_{x,y}K(x,y)=0.
```

写行列边际：

```text
rho(x)=sum_y K(x,y),
sigma(y)=sum_x K(x,y).
```

则在活动端点域 `X,Y` 上有精确分解：

```text
K(x,y)=rho(x)/|Y| + sigma(y)/|X| + K0(x,y),
sum_y K0(x,y)=0,
sum_x K0(x,y)=0.
```

上一层端点双线性相位为：

```text
S_beta=sum_{x,y}K(x,y)*conjugate(phi_beta(x))*phi_beta(y).
```

代入分解：

```text
S_beta=S_row(beta)+S_col(beta)+S_bal(beta).
```

若 `|S_beta|>=eta`，则至少一个出口发生：

```text
|S_row(beta)|>=eta/3,
or |S_col(beta)|>=eta/3,
or |S_bal(beta)|>=eta/3.
```

前两项是端点行/列边际 Fourier cap。第三项由 Cauchy-Schwarz 给出平衡核能量下界：

```text
||K0||_HS^2 >= eta^2/(9|X||Y|).
```

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrQuotientEndpointBilinearFourierPDECCap
  -> StableLadderEndpointBilinearFourierImportedLedger
  AND StableLadderIsolatedSingletonCarriedForwardAfterBilinearBalanceLedger
  AND StableLadderEndpointPairMatrixRegisteredLedger
  AND StableLadderEndpointCenteredKernelTotalZeroLedger
  AND StableLadderEndpointMarginalBalancedDecompositionLedger
  AND StableLadderEndpointBilinearPhasePairingLedger
  AND StableLadderEndpointBilinearTriangleTrichotomyLedger
  AND StableLadderEndpointRowMarginalFourierExitLedger
  AND StableLadderEndpointColumnMarginalFourierExitLedger
  AND StableLadderEndpointBalancedCoreEnergyLowerBoundLedger
  AND NoAnonymousEndpointBilinearFourierExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterBilinearBalanceLedger
  AND SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrEndpointMarginalFourierOrBalancedBilinearEnergyPDECCap
```

本步关闭的是匿名 endpoint bilinear Fourier 口径。剩余集中为孤立 singleton
全局求和、端点边际 Fourier/PDEC cap、balanced bilinear energy/PDEC cap，
或 sparse scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

## 207. stable-ladder endpoint energy packet 归约

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_energy_packet_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-energy-packet-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-energy-packet-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-energy-packet-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrEndpointMarginalFourierOrBalancedBilinearEnergyPDECCap`。
同步读数为：

```text
endpoint_marginal_or_balanced_energy_imported=true
isolated_singleton_carried_forward=true
endpoint_marginal_fourier_parseval_variance_closed=true
endpoint_marginal_variance_dyadic_packet_closed=true
balanced_core_energy_imported=true
balanced_core_energy_dyadic_cell_packet_closed=true
endpoint_energy_packet_signed_half_closed=true
endpoint_dyadic_energy_packet_registered=true
anonymous_endpoint_marginal_or_balanced_energy_removed=true
sparse_scale_ladder_sae_carried_forward=true
isolated_singleton_summability_proved=false
endpoint_dyadic_energy_packet_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

端点边际 Fourier 出口先由 Parseval 转成边际二范数。若：

```text
|hat rho(beta)| >= eta,
```

则：

```text
sum_x |rho(x)|^2 >= eta^2/q_j.
```

列边际 `sigma` 同理。balanced 分支沿用上一层：

```text
||K0||_HS^2 >= E.
```

对任意有限支持实值偏差函数 `F`，dyadic 分层给出某个尺度 `lambda`：

```text
lambda^2 * #{z: lambda < |F(z)| <= 2lambda} >= E_F/L,
E_F=sum_z |F(z)|^2.
```

其中 `L` 是有限非空 dyadic 层数。对 `rho` 或 `sigma` 得到一维端点边际包；
对 `K0` 得到二维端点 cell 包。再按正负偏差分裂，至少一侧贡献一半能量：

```text
energy(positive packet) >= packet_energy/2
or energy(negative packet) >= packet_energy/2.
```

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrEndpointMarginalFourierOrBalancedBilinearEnergyPDECCap
  -> StableLadderEndpointMarginalOrBalancedEnergyImportedLedger
  AND StableLadderIsolatedSingletonCarriedForwardAfterEnergyPacketLedger
  AND StableLadderEndpointMarginalFourierParsevalVarianceLedger
  AND StableLadderEndpointMarginalVarianceDyadicPacketLedger
  AND StableLadderBalancedCoreEnergyImportedLedger
  AND StableLadderBalancedCoreEnergyDyadicCellPacketLedger
  AND StableLadderEndpointEnergyPacketSignedHalfLedger
  AND StableLadderEndpointDyadicEnergyPacketRegisteredLedger
  AND NoAnonymousEndpointMarginalOrBalancedEnergyExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterEndpointEnergyPacketLedger
  AND SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrEndpointDyadicEnergyPacketPDECCap
```

本步关闭的是匿名端点边际 Fourier / balanced energy 口径。剩余集中为孤立
singleton 全局求和、endpoint dyadic energy packet/PDEC cap，或 sparse
scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

## 208. stable-ladder endpoint packet autocorrelation 归约

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_packet_autocorrelation_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-packet-autocorrelation-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-packet-autocorrelation-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-packet-autocorrelation-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrEndpointDyadicEnergyPacketPDECCap`。
同步读数为：

```text
endpoint_dyadic_energy_packet_imported=true
isolated_singleton_carried_forward=true
endpoint_packet_finite_group_closed=true
endpoint_packet_signed_support_closed=true
endpoint_packet_singleton_atom_registered=true
endpoint_packet_nonzero_pair_count_closed=true
endpoint_packet_displacement_pigeonhole_closed=true
endpoint_packet_weighted_autocorrelation_closed=true
endpoint_packet_dimension_preserved=true
anonymous_endpoint_dyadic_energy_packet_removed=true
sparse_scale_ladder_sae_carried_forward=true
isolated_singleton_summability_proved=false
endpoint_packet_singleton_atom_sae_proved=false
endpoint_displacement_autocorrelation_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

endpoint dyadic packet 位于有限群：

```text
dimension=1: H=Z/q_j Z,
dimension=2: H=(Z/q_j Z)^2.
```

上一层已经给出尺度 `lambda`、符号 `epsilon` 和同号支持：

```text
S={z in H: lambda < epsilon*F(z) <= 2lambda}.
```

若 `|S|=1`，则 packet 成为 endpoint packet singleton atom。若
`|S|=m>=2`，定义：

```text
C_S(delta)=#{z in S: z+delta in S}.
```

所有有序不同点对给出：

```text
sum_{delta != 0} C_S(delta)=m(m-1).
```

有限群鸽巢给出某个非零位移：

```text
C_S(delta) >= m(m-1)/(|H|-1).
```

同号 dyadic 幅度进一步给出：

```text
A_F(delta)=sum_{z,z+delta in S} F(z)F(z+delta)
          >= lambda^2*C_S(delta).
```

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrEndpointDyadicEnergyPacketPDECCap
  -> StableLadderEndpointDyadicEnergyPacketImportedLedger
  AND StableLadderIsolatedSingletonCarriedForwardAfterPacketAutocorrelationLedger
  AND StableLadderEndpointPacketFiniteGroupLedger
  AND StableLadderEndpointPacketSignedSupportLedger
  AND StableLadderEndpointPacketSingletonAtomLedger
  AND StableLadderEndpointPacketNonzeroPairCountLedger
  AND StableLadderEndpointPacketDisplacementPigeonholeLedger
  AND StableLadderEndpointPacketWeightedAutocorrelationLedger
  AND StableLadderEndpointPacketDimensionPreservedLedger
  AND NoAnonymousEndpointDyadicEnergyPacketExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterPacketAutocorrelationLedger
  AND SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrEndpointPacketSingletonAtomSAEOrEndpointDisplacementAutocorrelationPDECCap
```

本步关闭的是匿名 endpoint dyadic energy packet 口径。剩余集中为原有孤立
singleton 全局求和、endpoint packet singleton atom/SAE、endpoint
displacement autocorrelation/PDEC cap，或 sparse scale-ladder SAE 全局求和。
行/列命题仍未无条件闭合。

## 209. stable-ladder endpoint displacement orbit 归约

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_displacement_orbit_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-displacement-orbit-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-displacement-orbit-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-displacement-orbit-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrEndpointPacketSingletonAtomSAEOrEndpointDisplacementAutocorrelationPDECCap`。
同步读数为：

```text
endpoint_singleton_or_displacement_autocorrelation_imported=true
endpoint_singleton_atom_sae_unified=true
endpoint_displacement_autocorrelation_imported=true
endpoint_nonzero_displacement_order_closed=true
endpoint_displacement_orbit_partition_closed=true
endpoint_autocorrelation_orbit_decomposition_closed=true
endpoint_weighted_orbit_pigeonhole_closed=true
endpoint_orbit_cyclic_adjacency_packet_registered=true
endpoint_orbit_dimension_preserved=true
anonymous_endpoint_displacement_autocorrelation_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_translation_orbit_adjacency_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

原有 isolated singleton 与 packet singleton 合并为：

```text
EndpointSingletonAtomSAE.
```

对非零位移自相关分支，令：

```text
r=ord_H(delta)>1.
```

有限群 `H` 被平移 `T_delta:z -> z+delta` 分解为周期轨道：

```text
Omega=H/<delta>,
O=a+<delta>={a+t*delta: t in Z/rZ},
|Omega|=|H|/r.
```

加权自相关按轨道精确分解：

```text
A_F(delta)=sum_{O in Omega} A_O(delta),
A_O(delta)=sum_{t in Z/rZ} F(a+t*delta)F(a+(t+1)*delta) 1_{both in S}.
```

若全局分支达到下界，则存在单个轨道：

```text
A_O(delta) >= A_F(delta)/|Omega|.
```

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrEndpointPacketSingletonAtomSAEOrEndpointDisplacementAutocorrelationPDECCap
  -> StableLadderEndpointSingletonOrDisplacementAutocorrelationImportedLedger
  AND StableLadderEndpointSingletonAtomSAEUnifiedLedger
  AND StableLadderEndpointDisplacementAutocorrelationImportedLedger
  AND StableLadderEndpointNonzeroDisplacementOrderLedger
  AND StableLadderEndpointDisplacementOrbitPartitionLedger
  AND StableLadderEndpointAutocorrelationOrbitDecompositionLedger
  AND StableLadderEndpointWeightedOrbitPigeonholeLedger
  AND StableLadderEndpointOrbitCyclicAdjacencyPacketLedger
  AND StableLadderEndpointOrbitDimensionPreservedLedger
  AND NoAnonymousEndpointDisplacementAutocorrelationExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterDisplacementOrbitLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointTranslationOrbitAdjacencyPDECCap
```

本步关闭的是匿名 displacement autocorrelation 口径。剩余集中为 endpoint
singleton atom/SAE、endpoint translation orbit adjacency/PDEC cap，或 sparse
scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

## 210. stable-ladder endpoint orbit run/boundary 归约

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_run_boundary_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-run-boundary-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-run-boundary-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-run-boundary-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointTranslationOrbitAdjacencyPDECCap`。
同步读数为：

```text
endpoint_translation_orbit_adjacency_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_signed_cycle_model_closed=true
endpoint_orbit_dyadic_edge_count_closed=true
endpoint_orbit_run_partition_closed=true
endpoint_orbit_adjacency_run_boundary_identity_closed=true
endpoint_orbit_run_boundary_budget_dichotomy_closed=true
endpoint_orbit_long_same_sign_arc_registered=true
endpoint_orbit_boundary_flux_registered=true
anonymous_endpoint_translation_orbit_adjacency_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_long_same_sign_arc_sae_proved=false
endpoint_orbit_boundary_flux_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

固定上一层给出的平移轨道：

```text
C_r=Z/rZ,
z_t=a+t*delta.
```

令 `u_t=1_{z_t in S}`，`sigma_t=sign F(z_t)`。同号邻接边为：

```text
e_t=1 iff u_t=u_{t+1}=1 and sigma_t=sigma_{t+1}.
```

在 dyadic packet 中存在尺度 `lambda` 使：

```text
lambda^2 E <= W <= 4 lambda^2 E.
```

把 active 同号相邻点分解为极大循环 runs。若不是全周期同号特例，则有：

```text
E=n-b.
```

其中 `n` 是 active 点数，`b` 是 run/cut 数。全周期同号特例直接进入长度
`r` 的 long same-sign arc 出口。对任意边界预算 `B>=1`，若 `b>B` 则进入
boundary flux 出口；否则：

```text
L_max >= n/b >= E/B.
```

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointTranslationOrbitAdjacencyPDECCap
  -> StableLadderEndpointTranslationOrbitAdjacencyImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterOrbitRunLedger
  AND StableLadderEndpointOrbitSignedCycleModelLedger
  AND StableLadderEndpointOrbitDyadicEdgeCountLedger
  AND StableLadderEndpointOrbitRunPartitionLedger
  AND StableLadderEndpointOrbitAdjacencyRunBoundaryIdentityLedger
  AND StableLadderEndpointOrbitRunBoundaryBudgetDichotomyLedger
  AND StableLadderEndpointOrbitLongSameSignArcRegistrationLedger
  AND StableLadderEndpointOrbitBoundaryFluxRegistrationLedger
  AND NoAnonymousEndpointTranslationOrbitAdjacencyExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterOrbitRunBoundaryLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitLongSameSignArcSAEOrEndpointOrbitBoundaryFluxPDECCap
```

本步关闭的是匿名 endpoint translation orbit adjacency 口径。剩余集中为
endpoint singleton atom/SAE、endpoint orbit long same-sign arc SAE、endpoint
orbit boundary flux/PDEC cap，或 sparse scale-ladder SAE 全局求和。行/列命题
仍未无条件闭合。

## 211. stable-ladder endpoint orbit signed Fourier 归约

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_signed_fourier_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-signed-fourier-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-signed-fourier-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-signed-fourier-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitLongSameSignArcSAEOrEndpointOrbitBoundaryFluxPDECCap`。
同步读数为：

```text
endpoint_orbit_run_boundary_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_signed_indicator_sequence_closed=true
endpoint_orbit_full_cycle_mean_atom_registered=true
endpoint_orbit_long_arc_centered_discrepancy_closed=true
endpoint_orbit_arc_dirichlet_kernel_closed=true
endpoint_orbit_boundary_derivative_support_closed=true
endpoint_orbit_boundary_derivative_fourier_closed=true
endpoint_orbit_signed_fourier_cap_registered=true
anonymous_endpoint_orbit_long_arc_boundary_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_signed_fourier_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

固定单轨道 `C_r=Z/rZ`，定义有符号 active 函数：

```text
g_t=sigma_t*u_t in {-1,0,1},
bar_g=(1/r) sum_t g_t,
nu_t=g_t-bar_g.
```

若极大长同号 run `I` 不是全周期，且 `g_t=epsilon` 于 `I` 上，则：

```text
Delta_epsilon(I)=epsilon*sum_{t in I} nu_t >= |I|/r > 0.
```

Fourier 展开给出：

```text
Delta_epsilon(I)=(epsilon/r) sum_{h!=0} hat g(h) hat 1_I(-h),
|hat g(h)| >= r*Delta_epsilon(I)/Lambda_r(I)
```

对 boundary flux 分支，令 `Dg_t=g_{t+1}-g_t`。若切口数为 `b`，则：

```text
sum_t |Dg_t|^2 >= b,
sum_{h!=0}|(exp(2*pi*i*h/r)-1)hat g(h)|^2 = r*sum_t |Dg_t|^2.
```

因此存在非零频率：

```text
|(exp(2*pi*i*h/r)-1)hat g(h)| >= sqrt(r*b/(r-1)).
```

全周期同号特例登记为：

```text
EndpointOrbitFullCycleMeanAtomSAE.
```

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitLongSameSignArcSAEOrEndpointOrbitBoundaryFluxPDECCap
  -> StableLadderEndpointOrbitRunBoundaryImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterSignedFourierLedger
  AND StableLadderEndpointOrbitSignedIndicatorSequenceLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomRegistrationLedger
  AND StableLadderEndpointOrbitLongArcCenteredDiscrepancyLedger
  AND StableLadderEndpointOrbitArcDirichletKernelLedger
  AND StableLadderEndpointOrbitBoundaryDerivativeSupportLedger
  AND StableLadderEndpointOrbitBoundaryDerivativeFourierLedger
  AND StableLadderEndpointOrbitSignedFourierCapRegistrationLedger
  AND NoAnonymousEndpointOrbitLongArcBoundaryExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterOrbitSignedFourierLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitSignedFourierPDECCap
```

本步关闭的是匿名 long-arc/boundary 口径。剩余集中为 endpoint singleton
atom/SAE、endpoint orbit full-cycle mean atom/SAE、endpoint orbit signed
Fourier/PDEC cap，或 sparse scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

## 212. stable-ladder endpoint orbit conductor-character 归约

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_conductor_character_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-conductor-character-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-conductor-character-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-conductor-character-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitSignedFourierPDECCap`。
同步读数为：

```text
endpoint_orbit_signed_fourier_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_nonzero_frequency_conductor_closed=true
endpoint_orbit_frequency_kernel_quotient_closed=true
endpoint_orbit_kernel_fiber_collapse_closed=true
endpoint_orbit_primitive_conductor_character_packet_registered=true
endpoint_orbit_derivative_multiplier_absorbed=true
anonymous_endpoint_orbit_signed_fourier_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_primitive_conductor_character_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

对 signed Fourier 分支的非零频率 `h`，令：

```text
1 <= h <= r-1,
d=gcd(h,r),
m=r/d>1,
h0=h/d,
gcd(h0,m)=1.
```

则：

```text
exp(-2*pi*i*h*t/r)=exp(-2*pi*i*h0*(t mod m)/m).
```

该角色的 kernel 为 `{0,m,2m,...,(d-1)m}`，并且 `C_r/kernel ~= C_m`。
把有符号负载沿 kernel 纤维折叠：

```text
G_s=sum_{u=0}^{d-1} g_{s+u*m}.
```

得到精确恒等式：

```text
hat g(h)=sum_{s mod m} G_s exp(-2*pi*i*h0*s/m).
```

由于 `gcd(h0,m)=1`，这是 `C_m` 上的 primitive additive character packet。
若上一层来自 derivative Fourier 下界，则由 `|omega_r^h-1|<=2` 吸收常数：

```text
|(omega_r^h-1)hat g(h)| >= M  =>  |hat g(h)| >= M/2.
```

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitSignedFourierPDECCap
  -> StableLadderEndpointOrbitSignedFourierImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterConductorLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardLedger
  AND StableLadderEndpointOrbitNonzeroFrequencyConductorLedger
  AND StableLadderEndpointOrbitFrequencyKernelQuotientLedger
  AND StableLadderEndpointOrbitKernelFiberCollapseLedger
  AND StableLadderEndpointOrbitPrimitiveConductorCharacterPacketLedger
  AND StableLadderEndpointOrbitDerivativeMultiplierAbsorbedLedger
  AND NoAnonymousEndpointOrbitSignedFourierExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterOrbitConductorLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitPrimitiveConductorCharacterPDECCap
```

本步关闭的是匿名 signed Fourier 频率口径。剩余集中为 endpoint singleton
atom/SAE、endpoint orbit full-cycle mean atom/SAE、endpoint orbit primitive
conductor character/PDEC cap，或 sparse scale-ladder SAE 全局求和。行/列命题
仍未无条件闭合。

## 213. stable-ladder endpoint orbit standard-character 归约

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_standard_character_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-standard-character-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-standard-character-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-standard-character-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitPrimitiveConductorCharacterPDECCap`。
同步读数为：

```text
endpoint_orbit_primitive_conductor_character_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_conductor_unit_automorphism_closed=true
endpoint_orbit_standard_phase_coordinate_closed=true
endpoint_orbit_automorphic_load_permutation_closed=true
endpoint_orbit_first_harmonic_identity_closed=true
endpoint_orbit_load_norms_and_support_preserved=true
anonymous_primitive_conductor_frequency_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_standard_conductor_first_harmonic_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

上一层 conductor packet 形如：

```text
m>1, gcd(h0,m)=1,
sum_{s mod m} G_s exp(-2*pi*i*h0*s/m).
```

因为 `h0` 是 `Z/mZ` 的单位，取逆元 `u*h0==1 mod m`。令：

```text
a=h0*s mod m,
S_a=G_{u*a mod m}.
```

这是 `C_m` 上的精确置换，并给出恒等式：

```text
sum_{s mod m} G_s exp(-2*pi*i*h0*s/m)
  = sum_{a mod m} S_a exp(-2*pi*i*a/m).
```

置换保持支撑、`L1/L2` 质量、均值和 Fourier 下界常数。硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitPrimitiveConductorCharacterPDECCap
  -> StableLadderEndpointOrbitPrimitiveConductorCharacterImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterStandardCharacterLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterStandardCharacterLedger
  AND StableLadderEndpointOrbitConductorUnitAutomorphismLedger
  AND StableLadderEndpointOrbitStandardPhaseCoordinateLedger
  AND StableLadderEndpointOrbitAutomorphicLoadPermutationLedger
  AND StableLadderEndpointOrbitFirstHarmonicIdentityLedger
  AND StableLadderEndpointOrbitLoadNormsAndSupportPreservedLedger
  AND NoAnonymousPrimitiveConductorFrequencyExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterStandardCharacterLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStandardConductorFirstHarmonicPDECCap
```

本步关闭的是匿名 primitive 频率口径。剩余集中为 endpoint singleton
atom/SAE、endpoint orbit full-cycle mean atom/SAE、standard conductor
first-harmonic PDEC/cap，或 sparse scale-ladder SAE 全局求和。行/列命题仍未
无条件闭合。

## 214. stable-ladder endpoint orbit axis-lobe 归约

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_axis_lobe_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-axis-lobe-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-axis-lobe-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-axis-lobe-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStandardConductorFirstHarmonicPDECCap`。
同步读数为：

```text
endpoint_orbit_standard_first_harmonic_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_complex_first_harmonic_amplitude_closed=true
endpoint_orbit_axis_projection_dichotomy_closed=true
endpoint_orbit_axis_sign_choice_closed=true
endpoint_orbit_trigonometric_lobe_weight_closed=true
endpoint_orbit_axis_lobe_weighted_surplus_packet_registered=true
anonymous_standard_first_harmonic_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_axis_lobe_weighted_surplus_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

上一层标准 first harmonic 写成：

```text
F=sum_{a mod m} S_a exp(-2*pi*i*a/m), |F|>=M.
```

其实部、虚部分别为：

```text
Re F=sum_a S_a cos(2*pi*a/m),
Im F=-sum_a S_a sin(2*pi*a/m).
```

因此至少一个轴向投影满足：

```text
max(|Re F|, |Im F|) >= M/sqrt(2).
```

取 `phi_0(a)=cos(2*pi*a/m)`、`phi_1(a)=-sin(2*pi*a/m)`，存在
`j in {0,1}` 和 `eps in {+1,-1}` 使：

```text
sum_a S_a eps*phi_j(a) >= M/sqrt(2).
```

再令：

```text
w_a=max(eps*phi_j(a),0),
v_a=max(-eps*phi_j(a),0),
```

得到显式半圆叶片加权盈余：

```text
sum_a S_a*(w_a-v_a) >= M/sqrt(2).
```

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStandardConductorFirstHarmonicPDECCap
  -> StableLadderEndpointOrbitStandardFirstHarmonicImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterAxisLobeLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterAxisLobeLedger
  AND StableLadderEndpointOrbitComplexFirstHarmonicAmplitudeLedger
  AND StableLadderEndpointOrbitAxisProjectionDichotomyLedger
  AND StableLadderEndpointOrbitAxisSignChoiceLedger
  AND StableLadderEndpointOrbitTrigonometricLobeWeightLedger
  AND StableLadderEndpointOrbitAxisLobeWeightedSurplusPacketLedger
  AND NoAnonymousStandardFirstHarmonicExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterAxisLobeLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitAxisLobeWeightedSurplusPDECCap
```

本步关闭的是匿名复数 first-harmonic 口径。剩余集中为 endpoint singleton
atom/SAE、endpoint orbit full-cycle mean atom/SAE、axis-lobe weighted
surplus PDEC/cap，或 sparse scale-ladder SAE 全局求和。行/列命题仍未
无条件闭合。

## 215. stable-ladder endpoint orbit single-lobe 归约

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_single_lobe_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-single-lobe-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-single-lobe-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-single-lobe-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitAxisLobeWeightedSurplusPDECCap`。
同步读数为：

```text
endpoint_orbit_axis_lobe_weighted_surplus_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_two_lobe_surplus_decomposition_closed=true
endpoint_orbit_half_threshold_loss_closed=true
endpoint_orbit_single_lobe_sign_choice_closed=true
endpoint_orbit_single_lobe_half_circle_support_closed=true
endpoint_orbit_single_lobe_signed_surplus_packet_registered=true
anonymous_axis_lobe_difference_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_single_lobe_signed_surplus_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

上一层给出：

```text
sum_a S_a*(w_a-v_a) >= L,  w_a>=0, v_a>=0.
```

记：

```text
A=sum_a S_a*w_a,
B=sum_a S_a*v_a.
```

则 `A-B>=L`。若 `A>=L/2`，取 `W=w, eta=+1`；否则 `A<L/2`，必有
`-B>L/2`，取 `W=v, eta=-1`。于是：

```text
sum_a eta*S_a*W_a >= L/2,
0 <= W_a <= 1,
supp(W) is one axis half-circle.
```

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitAxisLobeWeightedSurplusPDECCap
  -> StableLadderEndpointOrbitAxisLobeWeightedSurplusImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterSingleLobeLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterSingleLobeLedger
  AND StableLadderEndpointOrbitTwoLobeSurplusDecompositionLedger
  AND StableLadderEndpointOrbitHalfThresholdLossLedger
  AND StableLadderEndpointOrbitSingleLobeSignChoiceLedger
  AND StableLadderEndpointOrbitSingleLobeHalfCircleSupportLedger
  AND StableLadderEndpointOrbitSingleLobeSignedSurplusPacketLedger
  AND NoAnonymousAxisLobeDifferenceExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterSingleLobeLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitSingleLobeSignedSurplusPDECCap
```

本步关闭的是匿名双叶片差异口径。剩余集中为 endpoint singleton atom/SAE、
endpoint orbit full-cycle mean atom/SAE、single-lobe signed surplus PDEC/cap，
或 sparse scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

## 216. stable-ladder endpoint orbit single-arc 归约

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_single_arc_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-single-arc-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-single-arc-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-single-arc-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitSingleLobeSignedSurplusPDECCap`。
同步读数为：

```text
endpoint_orbit_single_lobe_signed_surplus_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_single_lobe_layer_cake_identity_closed=true
endpoint_orbit_lobe_superlevel_arc_support_closed=true
endpoint_orbit_layer_cake_arc_pigeonhole_closed=true
endpoint_orbit_single_arc_signed_surplus_packet_registered=true
anonymous_single_lobe_weight_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_single_arc_signed_surplus_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

上一层给出：

```text
sum_a eta*S_a*W_a >= L, 0 <= W_a <= 1.
```

用 layer-cake 恒等式：

```text
W_a=int_0^1 1_{W_a>=t} dt,
H(t)=sum_{a: W_a>=t} eta*S_a.
```

于是：

```text
sum_a eta*S_a*W_a = int_0^1 H(t) dt.
```

若左侧至少为 `L`，则存在阈值 `t` 使 `H(t)>=L`。对单个三角半圆叶片，
超水平集：

```text
A_t={a mod m: W_a>=t}
```

是同一轴向半圆内的循环弧，因此：

```text
sum_{a in A_t} eta*S_a >= L.
```

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitSingleLobeSignedSurplusPDECCap
  -> StableLadderEndpointOrbitSingleLobeSignedSurplusImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterSingleArcLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterSingleArcLedger
  AND StableLadderEndpointOrbitSingleLobeLayerCakeIdentityLedger
  AND StableLadderEndpointOrbitLobeSuperlevelArcSupportLedger
  AND StableLadderEndpointOrbitLayerCakeArcPigeonholeLedger
  AND StableLadderEndpointOrbitSingleArcSignedSurplusPacketLedger
  AND NoAnonymousSingleLobeWeightExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterSingleArcLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitSingleArcSignedSurplusPDECCap
```

本步关闭的是匿名连续叶片权重口径。剩余集中为 endpoint singleton atom/SAE、
endpoint orbit full-cycle mean atom/SAE、single-arc signed surplus PDEC/cap，
或 sparse scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

## 217. stable-ladder endpoint orbit arc endpoint-potential 归约

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_arc_endpoint_potential_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-arc-endpoint-potential-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-arc-endpoint-potential-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-arc-endpoint-potential-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitSingleArcSignedSurplusPDECCap`。
同步读数为：

```text
endpoint_orbit_single_arc_signed_surplus_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_arc_signed_load_sequence_closed=true
endpoint_orbit_arc_mean_contribution_dichotomy_closed=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_centered_arc_surplus_closed=true
endpoint_orbit_centered_prefix_potential_closed=true
endpoint_orbit_arc_endpoint_potential_gap_closed=true
endpoint_orbit_arc_endpoint_potential_packet_registered=true
anonymous_single_arc_interior_surplus_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_arc_endpoint_potential_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

上一层给出单弧包：

```text
sum_{a in A} X_a >= L,
X_a=eta*S_a, A=[u,v) subset C_m.
```

令

```text
mu=(1/m) sum_{a in C_m} X_a,
Y_a=X_a-mu.
```

则

```text
sum_{a in A} X_a = |A|*mu + sum_{a in A}Y_a.
```

若 `|A|*mu>=L/2`，因 `|A|<=m`，全周期均值满足 `m*mu>=L/2`，
进入 full-cycle mean atom 出口。否则中心化弧差满足：

```text
sum_{a in A}Y_a >= L/2.
```

定义中心化前缀势能：

```text
F(0)=0, F(j+1)=F(j)+Y_j, F(m)=0.
```

对 `A=[u,v)` 有：

```text
sum_{a in A}Y_a = F(v)-F(u).
```

因此非均值支路强制两个弧端点之间存在至少 `L/2` 的势能差。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitSingleArcSignedSurplusPDECCap
  -> StableLadderEndpointOrbitSingleArcSignedSurplusImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterArcEndpointPotentialLedger
  AND StableLadderEndpointOrbitArcSignedLoadSequenceLedger
  AND StableLadderEndpointOrbitArcMeanContributionDichotomyLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterArcEndpointPotentialLedger
  AND StableLadderEndpointOrbitCenteredArcSurplusLedger
  AND StableLadderEndpointOrbitCenteredPrefixPotentialLedger
  AND StableLadderEndpointOrbitArcEndpointPotentialGapLedger
  AND StableLadderEndpointOrbitArcEndpointPotentialPacketLedger
  AND NoAnonymousSingleArcInteriorSurplusExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterArcEndpointPotentialLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitArcEndpointPotentialPDECCap
```

本步关闭的是匿名弧内部盈余口径。剩余集中为 endpoint singleton atom/SAE、
endpoint orbit full-cycle mean atom/SAE、arc endpoint-potential PDEC/cap，
或 sparse scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

## 218. stable-ladder endpoint orbit potential-variation 归约

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_potential_variation_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-potential-variation-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-potential-variation-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-potential-variation-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitArcEndpointPotentialPDECCap`。
同步读数为：

```text
endpoint_orbit_arc_endpoint_potential_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_centered_potential_increment_closed=true
endpoint_orbit_endpoint_gap_directed_arc_closed=true
endpoint_orbit_positive_variation_lower_bound_closed=true
endpoint_orbit_negative_variation_lower_bound_closed=true
endpoint_orbit_signed_variation_packet_registered=true
anonymous_endpoint_potential_gap_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_signed_variation_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

上一层给出端点势能差：

```text
F(v)-F(u) >= G,
G=L/2.
```

中心化边增量满足：

```text
Y_j=F(j+1)-F(j),
sum_{j in C_m}Y_j=0.
```

令 `I=[u,v)`、`J=[v,u)`，则：

```text
sum_{j in I}Y_j = F(v)-F(u) >= G,
sum_{j in J}Y_j = F(u)-F(v) <= -G.
```

因此有实际边增量的双向 variation 义务：

```text
sum_{j in I}(Y_j)_+ >= G,
sum_{j in J}(Y_j)_- >= G.
```

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitArcEndpointPotentialPDECCap
  -> StableLadderEndpointOrbitArcEndpointPotentialImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterPotentialVariationLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterPotentialVariationLedger
  AND StableLadderEndpointOrbitCenteredPotentialIncrementLedger
  AND StableLadderEndpointOrbitEndpointGapDirectedArcLedger
  AND StableLadderEndpointOrbitPositiveVariationLowerBoundLedger
  AND StableLadderEndpointOrbitNegativeVariationLowerBoundLedger
  AND StableLadderEndpointOrbitSignedVariationPacketLedger
  AND NoAnonymousEndpointPotentialGapExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterPotentialVariationLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitSignedVariationPDECCap
```

本步关闭的是匿名两端点势能差口径。剩余集中为 endpoint singleton atom/SAE、
endpoint orbit full-cycle mean atom/SAE、endpoint orbit signed variation PDEC/cap，
或 sparse scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

## 219. stable-ladder endpoint orbit variation run/boundary 归约

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_variation_run_boundary_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-variation-run-boundary-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-variation-run-boundary-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-variation-run-boundary-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitSignedVariationPDECCap`。
同步读数为：

```text
endpoint_orbit_signed_variation_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_variation_signed_side_choice_closed=true
endpoint_orbit_positive_increment_edge_set_closed=true
endpoint_orbit_variation_run_partition_closed=true
endpoint_orbit_variation_run_boundary_budget_dichotomy_closed=true
endpoint_orbit_increment_run_surplus_packet_registered=true
endpoint_orbit_variation_boundary_flux_packet_registered=true
anonymous_signed_variation_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_increment_run_surplus_sae_proved=false
endpoint_orbit_variation_boundary_flux_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

上一层给出某个有向支撑 `K` 与符号 `sigma`：

```text
sum_{j in K}(sigma*Y_j)_+ >= G.
```

令正增量边集合：

```text
E_+={j in K: sigma*Y_j>0}.
```

把 `E_+` 分解为极大连续同符号增量 runs。给定边界预算 `B`，
若 run 数 `b>B`，则登记为 variation boundary flux PDEC/cap。若 `b<=B`，
则 pigeonhole 给出：

```text
exists h: sum_{j in R_h} sigma*Y_j >= G/B.
```

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitSignedVariationPDECCap
  -> StableLadderEndpointOrbitSignedVariationImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterVariationRunBoundaryLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterVariationRunBoundaryLedger
  AND StableLadderEndpointOrbitVariationSignedSideChoiceLedger
  AND StableLadderEndpointOrbitPositiveIncrementEdgeSetLedger
  AND StableLadderEndpointOrbitVariationRunPartitionLedger
  AND StableLadderEndpointOrbitVariationRunBoundaryBudgetDichotomyLedger
  AND StableLadderEndpointOrbitIncrementRunSurplusPacketLedger
  AND StableLadderEndpointOrbitVariationBoundaryFluxPacketLedger
  AND NoAnonymousSignedVariationExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterVariationRunBoundaryLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitIncrementRunSurplusSAEOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步关闭的是匿名 signed variation 口径。剩余集中为 endpoint singleton atom/SAE、
endpoint orbit full-cycle mean atom/SAE、increment-run surplus SAE、
variation-boundary flux PDEC/cap，或 sparse scale-ladder SAE 全局求和。
行/列命题仍未无条件闭合。

## 220. stable-ladder endpoint orbit increment-run amplitude/drift 归约

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_increment_run_amplitude_drift_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-increment-run-amplitude-drift-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-increment-run-amplitude-drift-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-increment-run-amplitude-drift-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitIncrementRunSurplusSAEOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步读数为：

```text
endpoint_orbit_increment_run_surplus_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_variation_boundary_flux_carried_forward=true
endpoint_orbit_increment_run_same_sign_coordinate_closed=true
endpoint_orbit_increment_run_mass_lower_bound_closed=true
endpoint_orbit_increment_run_amplitude_threshold_dichotomy_closed=true
endpoint_orbit_increment_edge_spike_packet_registered=true
endpoint_orbit_long_bounded_increment_drift_packet_registered=true
anonymous_increment_run_surplus_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_increment_edge_spike_sae_proved=false
endpoint_orbit_long_bounded_increment_drift_pdec_cap_proved=false
endpoint_orbit_variation_boundary_flux_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

上一层低边界支路给出一个连续同符号增量 run `R`。令：

```text
Z_j=sigma*Y_j>0 for j in R,
sum_{j in R}Z_j >= H,  H=G/B.
```

固定任意幅度阈值 `Lambda>0`。若：

```text
max_{j in R}Z_j >= Lambda,
```

则登记为单边大增量 edge-spike atom。否则所有 run 内增量都满足
`0<Z_j<Lambda`，于是：

```text
|R| >= H/Lambda.
```

当阈值选择使 `H/Lambda` 很大时，这一支路就是长的有界增量单调漂移。
上一层高切换 run 支路的 variation-boundary flux 继续前传。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitIncrementRunSurplusSAEOrEndpointOrbitVariationBoundaryFluxPDECCap
  -> StableLadderEndpointOrbitIncrementRunSurplusImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterIncrementRunAmplitudeDriftLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterIncrementRunAmplitudeDriftLedger
  AND StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterIncrementRunAmplitudeDriftLedger
  AND StableLadderEndpointOrbitIncrementRunSameSignCoordinateLedger
  AND StableLadderEndpointOrbitIncrementRunMassLowerBoundLedger
  AND StableLadderEndpointOrbitIncrementRunAmplitudeThresholdDichotomyLedger
  AND StableLadderEndpointOrbitIncrementEdgeSpikePacketLedger
  AND StableLadderEndpointOrbitLongBoundedIncrementDriftPacketLedger
  AND NoAnonymousIncrementRunSurplusExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterIncrementRunAmplitudeDriftLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitIncrementEdgeSpikeSAEOrEndpointOrbitLongBoundedIncrementDriftPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步关闭的是匿名 increment-run surplus 口径。剩余集中为 endpoint singleton atom/SAE、
endpoint orbit full-cycle mean atom/SAE、increment edge-spike SAE、
long bounded-increment drift PDEC/cap、variation-boundary flux PDEC/cap，
或 sparse scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

## 221. stable-ladder endpoint orbit edge-spike mean/singleton 归约

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_edge_spike_mean_singleton_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-edge-spike-mean-singleton-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-edge-spike-mean-singleton-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-edge-spike-mean-singleton-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitIncrementEdgeSpikeSAEOrEndpointOrbitLongBoundedIncrementDriftPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步读数为：

```text
endpoint_orbit_increment_edge_spike_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_long_bounded_increment_drift_carried_forward=true
endpoint_orbit_variation_boundary_flux_carried_forward=true
endpoint_orbit_edge_spike_centered_load_expansion_closed=true
endpoint_orbit_edge_spike_half_threshold_dichotomy_closed=true
endpoint_orbit_edge_spike_singleton_atom_absorption_closed=true
endpoint_orbit_edge_spike_full_cycle_mean_atom_absorption_closed=true
anonymous_increment_edge_spike_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_long_bounded_increment_drift_pdec_cap_proved=false
endpoint_orbit_variation_boundary_flux_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

edge-spike 支路给出某个边位 `j` 与符号 `sigma`：

```text
sigma*Y_j >= Lambda.
```

而上一层的增量是中心化点负载：

```text
Y_j=X_j-mu.
```

所以：

```text
sigma*X_j - sigma*mu >= Lambda.
```

于是半阈值二分给出：

```text
sigma*X_j >= Lambda/2
or
-sigma*mu >= Lambda/2.
```

第一支是 endpoint singleton atom；第二支是 full-cycle mean atom。因此
increment edge-spike 不再作为独立出口保留，而并入已有的 singleton/full-cycle mean
出口。long bounded-increment drift 与 variation-boundary flux 继续前传。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitIncrementEdgeSpikeSAEOrEndpointOrbitLongBoundedIncrementDriftPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
  -> StableLadderEndpointOrbitIncrementEdgeSpikeImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterEdgeSpikeMeanSingletonLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterEdgeSpikeMeanSingletonLedger
  AND StableLadderEndpointOrbitLongBoundedIncrementDriftCarriedForwardAfterEdgeSpikeMeanSingletonLedger
  AND StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterEdgeSpikeMeanSingletonLedger
  AND StableLadderEndpointOrbitEdgeSpikeCenteredLoadExpansionLedger
  AND StableLadderEndpointOrbitEdgeSpikeHalfThresholdDichotomyLedger
  AND StableLadderEndpointOrbitEdgeSpikeSingletonAtomAbsorptionLedger
  AND StableLadderEndpointOrbitEdgeSpikeFullCycleMeanAtomAbsorptionLedger
  AND NoAnonymousIncrementEdgeSpikeExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterEdgeSpikeMeanSingletonLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLongBoundedIncrementDriftPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步关闭的是独立 increment edge-spike 口径。剩余集中为 endpoint singleton atom/SAE、
endpoint orbit full-cycle mean atom/SAE、long bounded-increment drift PDEC/cap、
variation-boundary flux PDEC/cap，或 sparse scale-ladder SAE 全局求和。
行/列命题仍未无条件闭合。

## 222. stable-ladder endpoint orbit long-drift dyadic plateau 归约

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_long_drift_dyadic_plateau_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-long-drift-dyadic-plateau-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-long-drift-dyadic-plateau-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-long-drift-dyadic-plateau-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLongBoundedIncrementDriftPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步读数为：

```text
endpoint_orbit_long_bounded_increment_drift_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_variation_boundary_flux_carried_forward=true
endpoint_orbit_long_drift_positive_bounded_run_closed=true
endpoint_orbit_long_drift_dyadic_amplitude_partition_closed=true
endpoint_orbit_long_drift_amplitude_depth_budget_dichotomy_closed=true
endpoint_orbit_long_drift_heavy_dyadic_band_closed=true
endpoint_orbit_dyadic_band_plateau_run_partition_closed=true
endpoint_orbit_dyadic_plateau_run_boundary_dichotomy_closed=true
endpoint_orbit_comparable_amplitude_plateau_drift_packet_registered=true
endpoint_orbit_amplitude_depth_packet_registered=true
anonymous_long_bounded_increment_drift_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_comparable_amplitude_plateau_drift_pdec_cap_proved=false
endpoint_orbit_amplitude_depth_pdec_cap_proved=false
endpoint_orbit_variation_boundary_flux_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

long bounded drift 支路给出连续 run `R`：

```text
0<Z_j<Lambda,  sum_{j in R}Z_j>=H.
```

按 dyadic 幅度层分解：

```text
A_l={j in R: 2^{-(l+1)}Lambda <= Z_j < 2^{-l}Lambda}.
```

由于 `R` 有限，非空层数有限。给定深度预算 `D`，若非空层数 `d>D`，
则登记为 amplitude-depth PDEC/cap；若 `d<=D`，则某个 dyadic band 满足：

```text
sum_{j in A_l}Z_j >= H/D.
```

再把该重层在 `R` 中分解为极大连续 plateau runs。给定 plateau 边界预算 `B`，
若 plateau run 数超过 `B`，则进入 variation-boundary flux；否则某个 `P_s` 满足：

```text
sum_{j in P_s}Z_j >= H/(D*B),
```

且 `P_s` 内所有增量处于同一 dyadic band，幅度相差小于 2 倍。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLongBoundedIncrementDriftPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
  -> StableLadderEndpointOrbitLongBoundedIncrementDriftImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterLongDriftDyadicPlateauLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterLongDriftDyadicPlateauLedger
  AND StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterLongDriftDyadicPlateauLedger
  AND StableLadderEndpointOrbitLongDriftPositiveBoundedRunLedger
  AND StableLadderEndpointOrbitLongDriftDyadicAmplitudePartitionLedger
  AND StableLadderEndpointOrbitLongDriftAmplitudeDepthBudgetDichotomyLedger
  AND StableLadderEndpointOrbitLongDriftHeavyDyadicBandLedger
  AND StableLadderEndpointOrbitDyadicBandPlateauRunPartitionLedger
  AND StableLadderEndpointOrbitDyadicPlateauRunBoundaryDichotomyLedger
  AND StableLadderEndpointOrbitComparableAmplitudePlateauDriftPacketLedger
  AND StableLadderEndpointOrbitAmplitudeDepthPacketLedger
  AND NoAnonymousLongBoundedIncrementDriftExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterLongDriftDyadicPlateauLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitComparableAmplitudePlateauDriftPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步关闭的是匿名 long bounded drift 口径。剩余集中为 endpoint singleton atom/SAE、
endpoint orbit full-cycle mean atom/SAE、comparable-amplitude plateau drift PDEC/cap、
amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap，或 sparse scale-ladder
SAE 全局求和。行/列命题仍未无条件闭合。

### 1.64 stable-ladder endpoint orbit plateau-ramp 更新

新增机器证书：

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_plateau_ramp_router.py
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-ramp-ledger.json
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-ramp-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-ramp-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitComparableAmplitudePlateauDriftPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
endpoint_orbit_comparable_amplitude_plateau_drift_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_amplitude_depth_carried_forward=true
endpoint_orbit_variation_boundary_flux_carried_forward=true
endpoint_orbit_comparable_plateau_same_sign_load_closed=true
endpoint_orbit_plateau_length_budget_dichotomy_closed=true
endpoint_orbit_short_plateau_edge_spike_absorption_closed=true
endpoint_orbit_long_plateau_monotone_ramp_packet_registered=true
anonymous_comparable_amplitude_plateau_drift_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_plateau_ramp_potential_pdec_cap_proved=false
endpoint_orbit_amplitude_depth_pdec_cap_proved=false
endpoint_orbit_variation_boundary_flux_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

plateau 支路被写成连续弧 `P_s` 上的真实同号负载：

```text
Z_j=sigma*Y_j>0,  a<=Z_j<2a,  sum_{j in P_s}Z_j>=H0.
```

给定长度预算 `L0`。若 `|P_s|<=L0`，则 `max Z_j>=H0/L0`，这是已归档
edge-spike 机制的短原子，吸收到 endpoint singleton 或 full-cycle mean 出口。若
`|P_s|>L0`，则 prefix potential

```text
S(t)=sum_{i<=t} sigma*Y_i
```

在 `P_s` 上单调爬升至少 `H0`，形成长 plateau-ramp potential 包。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitComparableAmplitudePlateauDriftPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
  -> StableLadderEndpointOrbitComparableAmplitudePlateauDriftImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterPlateauRampLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterPlateauRampLedger
  AND StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterPlateauRampLedger
  AND StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterPlateauRampLedger
  AND StableLadderEndpointOrbitComparablePlateauSameSignLoadLedger
  AND StableLadderEndpointOrbitPlateauLengthBudgetDichotomyLedger
  AND StableLadderEndpointOrbitShortPlateauEdgeSpikeAbsorptionLedger
  AND StableLadderEndpointOrbitLongPlateauMonotoneRampPacketLedger
  AND NoAnonymousComparableAmplitudePlateauDriftExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterPlateauRampLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitPlateauRampPotentialPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步关闭的是匿名 comparable-amplitude plateau drift 口径。剩余集中为 endpoint
singleton atom/SAE、endpoint orbit full-cycle mean atom/SAE、plateau-ramp
potential PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap，
或 sparse scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

### 1.65 stable-ladder endpoint orbit plateau-return mirror 更新

新增机器证书：

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_plateau_return_mirror_router.py
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-return-mirror-ledger.json
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-return-mirror-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-return-mirror-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitPlateauRampPotentialPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
endpoint_orbit_plateau_ramp_potential_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_amplitude_depth_carried_forward=true
endpoint_orbit_variation_boundary_flux_carried_forward=true
endpoint_orbit_positive_plateau_ramp_imported_model_closed=true
endpoint_orbit_full_cycle_zero_sum_return_obligation_closed=true
endpoint_orbit_negative_return_mass_lower_bound_closed=true
endpoint_orbit_return_mass_dyadic_amplitude_partition_closed=true
endpoint_orbit_return_amplitude_depth_dichotomy_closed=true
endpoint_orbit_heavy_return_dyadic_band_closed=true
endpoint_orbit_return_plateau_run_partition_closed=true
endpoint_orbit_return_run_boundary_dichotomy_closed=true
endpoint_orbit_opposite_sign_plateau_ramp_pair_packet_registered=true
anonymous_plateau_ramp_potential_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_opposite_sign_plateau_ramp_pair_pdec_cap_proved=false
endpoint_orbit_amplitude_depth_pdec_cap_proved=false
endpoint_orbit_variation_boundary_flux_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

正向 plateau-ramp 给出：

```text
P consecutive,  Z_j=sigma*Y_j>0,  sum_{j in P}Z_j>=H0.
```

由于 `Y` 是中心化轨道负载：

```text
sum_cycle sigma*Y_j=0.
```

补弧上的负向 return mass

```text
W_j=(-sigma*Y_j)_+
```

必须满足 `sum W_j>=H0`。将 `W_j` 作 dyadic 幅度层与连续 run 分解：若非空层数
超过 `D`，进入 amplitude-depth；若重层的 return run 数超过 `B`，进入
variation-boundary flux；否则存在负向 return plateau `Q`：

```text
sum_{j in Q} W_j >= H0/(D*B).
```

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitPlateauRampPotentialPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
  -> StableLadderEndpointOrbitPlateauRampPotentialImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterPlateauReturnMirrorLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterPlateauReturnMirrorLedger
  AND StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterPlateauReturnMirrorLedger
  AND StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterPlateauReturnMirrorLedger
  AND StableLadderEndpointOrbitPositivePlateauRampImportedModelLedger
  AND StableLadderEndpointOrbitFullCycleZeroSumReturnObligationLedger
  AND StableLadderEndpointOrbitNegativeReturnMassLowerBoundLedger
  AND StableLadderEndpointOrbitReturnMassDyadicAmplitudePartitionLedger
  AND StableLadderEndpointOrbitReturnAmplitudeDepthDichotomyLedger
  AND StableLadderEndpointOrbitHeavyReturnDyadicBandLedger
  AND StableLadderEndpointOrbitReturnPlateauRunPartitionLedger
  AND StableLadderEndpointOrbitReturnRunBoundaryDichotomyLedger
  AND StableLadderEndpointOrbitOppositeSignPlateauRampPairPacketLedger
  AND NoAnonymousPlateauRampPotentialExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterPlateauReturnMirrorLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitOppositeSignPlateauRampPairPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步关闭的是匿名 plateau-ramp potential 口径。剩余集中为 endpoint singleton
atom/SAE、endpoint orbit full-cycle mean atom/SAE、opposite-sign plateau-ramp
pair PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap，
或 sparse scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

### 1.66 stable-ladder endpoint orbit plateau-pair phase 更新

新增机器证书：

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_plateau_pair_phase_router.py
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-pair-phase-ledger.json
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-pair-phase-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-pair-phase-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitOppositeSignPlateauRampPairPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
endpoint_orbit_opposite_sign_plateau_ramp_pair_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_amplitude_depth_carried_forward=true
endpoint_orbit_variation_boundary_flux_carried_forward=true
endpoint_orbit_opposite_sign_plateau_pair_model_closed=true
endpoint_orbit_plateau_pair_cyclic_gap_decomposition_closed=true
endpoint_orbit_plateau_pair_gap_budget_dichotomy_closed=true
endpoint_orbit_near_contact_opposite_sign_boundary_packet_registered=true
endpoint_orbit_phase_separated_bipolar_plateau_pair_packet_registered=true
anonymous_opposite_sign_plateau_ramp_pair_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_phase_separated_bipolar_plateau_pair_pdec_cap_proved=false
endpoint_orbit_amplitude_depth_pdec_cap_proved=false
endpoint_orbit_variation_boundary_flux_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

镜像对被写成同一周期轨道上的两个不交连续弧：

```text
P: sigma*Y_j>0,
Q: -sigma*Y_j>0.
```

两个弧决定两个 cyclic gaps `g1,g2`。给定 gap 预算 `E`：

```text
if min(g1,g2)<=E: near-contact opposite-sign boundary packet;
if min(g1,g2)>E: phase-separated bipolar plateau pair.
```

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitOppositeSignPlateauRampPairPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
  -> StableLadderEndpointOrbitOppositeSignPlateauRampPairImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterPlateauPairPhaseLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterPlateauPairPhaseLedger
  AND StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterPlateauPairPhaseLedger
  AND StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterPlateauPairPhaseLedger
  AND StableLadderEndpointOrbitOppositeSignPlateauPairModelLedger
  AND StableLadderEndpointOrbitPlateauPairCyclicGapDecompositionLedger
  AND StableLadderEndpointOrbitPlateauPairGapBudgetDichotomyLedger
  AND StableLadderEndpointOrbitNearContactOppositeSignBoundaryPacketLedger
  AND StableLadderEndpointOrbitPhaseSeparatedBipolarPlateauPairPacketLedger
  AND NoAnonymousOppositeSignPlateauRampPairExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterPlateauPairPhaseLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitPhaseSeparatedBipolarPlateauPairPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步关闭的是匿名 opposite-sign plateau pair 口径。剩余集中为 endpoint
singleton atom/SAE、endpoint orbit full-cycle mean atom/SAE、phase-separated
bipolar plateau pair PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux
PDEC/cap，或 sparse scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

### 1.67 stable-ladder endpoint orbit bipolar-shelf 更新

新增机器证书：

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_bipolar_shelf_router.py
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-bipolar-shelf-ledger.json
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-bipolar-shelf-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-bipolar-shelf-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitPhaseSeparatedBipolarPlateauPairPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
endpoint_orbit_phase_separated_bipolar_plateau_pair_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_amplitude_depth_carried_forward=true
endpoint_orbit_variation_boundary_flux_carried_forward=true
endpoint_orbit_phase_separated_bipolar_pair_model_closed=true
endpoint_orbit_bipolar_prefix_potential_coordinate_closed=true
endpoint_orbit_bipolar_bridge_decomposition_closed=true
endpoint_orbit_bridge_cancellation_or_shelf_dichotomy_closed=true
endpoint_orbit_bridge_cancellation_packet_registered=true
endpoint_orbit_long_potential_shelf_packet_registered=true
anonymous_phase_separated_bipolar_plateau_pair_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_long_potential_shelf_pdec_cap_proved=false
endpoint_orbit_bridge_cancellation_pdec_cap_proved=false
endpoint_orbit_amplitude_depth_pdec_cap_proved=false
endpoint_orbit_variation_boundary_flux_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

相位分离双极包给出正 plateau `P` 与负 plateau `Q`，且两个 cyclic gaps 均大于
`E`。定义有向前缀势能：

```text
S(t)=sum_{i<=t} sigma*Y_i.
```

`P` 使 `S` 上升，`Q` 使 `S` 回落。若桥段在遇到相反 plateau 前已经抵消至少半个
高度，则登记为 bridge-cancellation；否则势能在长桥段上保持至少半高度，形成
long potential shelf。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitPhaseSeparatedBipolarPlateauPairPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
  -> StableLadderEndpointOrbitPhaseSeparatedBipolarPlateauPairImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterBipolarShelfLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterBipolarShelfLedger
  AND StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterBipolarShelfLedger
  AND StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterBipolarShelfLedger
  AND StableLadderEndpointOrbitPhaseSeparatedBipolarPairModelLedger
  AND StableLadderEndpointOrbitBipolarPrefixPotentialCoordinateLedger
  AND StableLadderEndpointOrbitBipolarBridgeDecompositionLedger
  AND StableLadderEndpointOrbitBridgeCancellationOrShelfDichotomyLedger
  AND StableLadderEndpointOrbitBridgeCancellationPacketLedger
  AND StableLadderEndpointOrbitLongPotentialShelfPacketLedger
  AND NoAnonymousPhaseSeparatedBipolarPlateauPairExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterBipolarShelfLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLongPotentialShelfPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步关闭的是匿名 phase-separated bipolar pair 口径。剩余集中为 endpoint
singleton atom/SAE、endpoint orbit full-cycle mean atom/SAE、long potential
shelf PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap，或 sparse scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

### 1.68 stable-ladder endpoint orbit long-potential-shelf static-bias 更新

新增机器证书：

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_long_potential_shelf_static_bias_router.py
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-long-potential-shelf-static-bias-ledger.json
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-long-potential-shelf-static-bias-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-long-potential-shelf-static-bias-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLongPotentialShelfPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
endpoint_orbit_long_potential_shelf_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_bridge_cancellation_carried_forward=true
endpoint_orbit_amplitude_depth_carried_forward=true
endpoint_orbit_variation_boundary_flux_carried_forward=true
endpoint_orbit_long_potential_shelf_model_closed=true
endpoint_orbit_shelf_potential_floor_closed=true
endpoint_orbit_shelf_increment_balance_closed=true
endpoint_orbit_shelf_oscillation_boundary_flux_dichotomy_closed=true
endpoint_orbit_shelf_positive_drift_amplitude_depth_dichotomy_closed=true
endpoint_orbit_shelf_negative_cancellation_dichotomy_closed=true
endpoint_orbit_static_potential_shelf_bias_packet_registered=true
anonymous_long_potential_shelf_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_static_potential_shelf_bias_pdec_cap_proved=false
endpoint_orbit_bridge_cancellation_pdec_cap_proved=false
endpoint_orbit_amplitude_depth_pdec_cap_proved=false
endpoint_orbit_variation_boundary_flux_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

long potential shelf 给出长度 `L>E` 的桥段 `I`，且选定符号 `sigma` 后有

```text
sigma*S(t) >= H/2 for all t in I.
```

把 shelf 内增量 `d_t=S(t+1)-S(t)` 分成正漂移、负抵消与边界振荡。高振荡回流
variation-boundary flux；正漂移继续堆高回流 amplitude-depth；足量反向抵消回流
bridge-cancellation。三者都不发生时，剩余被命名为 static potential shelf bias。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLongPotentialShelfPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
  -> StableLadderEndpointOrbitLongPotentialShelfImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterShelfStaticBiasLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterShelfStaticBiasLedger
  AND StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterShelfStaticBiasLedger
  AND StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterShelfStaticBiasLedger
  AND StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterShelfStaticBiasLedger
  AND StableLadderEndpointOrbitLongPotentialShelfModelLedger
  AND StableLadderEndpointOrbitShelfPotentialFloorLedger
  AND StableLadderEndpointOrbitShelfIncrementBalanceLedger
  AND StableLadderEndpointOrbitShelfOscillationBoundaryFluxDichotomyLedger
  AND StableLadderEndpointOrbitShelfPositiveDriftAmplitudeDepthDichotomyLedger
  AND StableLadderEndpointOrbitShelfNegativeCancellationDichotomyLedger
  AND StableLadderEndpointOrbitStaticPotentialShelfBiasPacketLedger
  AND NoAnonymousLongPotentialShelfExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterShelfStaticBiasLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStaticPotentialShelfBiasPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步关闭的是匿名 long potential shelf 口径。剩余集中为 endpoint singleton
atom/SAE、endpoint orbit full-cycle mean atom/SAE、static potential shelf bias
PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap，或 sparse scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

### 1.69 stable-ladder endpoint orbit static-shelf area-moment 更新

新增机器证书：

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_static_shelf_area_moment_router.py
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-area-moment-ledger.json
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-area-moment-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-area-moment-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStaticPotentialShelfBiasPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
endpoint_orbit_static_potential_shelf_bias_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_bridge_cancellation_carried_forward=true
endpoint_orbit_amplitude_depth_carried_forward=true
endpoint_orbit_variation_boundary_flux_carried_forward=true
endpoint_orbit_static_shelf_bias_model_closed=true
endpoint_orbit_static_shelf_area_lower_bound_closed=true
endpoint_orbit_shelf_summation_by_parts_closed=true
endpoint_orbit_shelf_endpoint_charge_return_closed=true
endpoint_orbit_static_shelf_area_moment_packet_registered=true
anonymous_static_potential_shelf_bias_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_static_shelf_area_moment_pdec_cap_proved=false
endpoint_orbit_bridge_cancellation_pdec_cap_proved=false
endpoint_orbit_amplitude_depth_pdec_cap_proved=false
endpoint_orbit_variation_boundary_flux_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

static potential shelf bias 给出低振荡、无深漂移、无早抵消的一侧势能地板：

```text
sigma*S(t) >= H/2 for t in I,  |I|=L>E.
```

因此强制矩形面积

```text
A(I)=sum_{t in I} sigma*S(t) >= H*L/2.
```

离散分部求和把 `A(I)` 写成端点收费与 triangular/sawtooth 权重下的增量矩。若端点收费
已经解释该面积，则回流 bridge-cancellation、amplitude-depth 或 variation-boundary flux；
否则剩余就是 static shelf area moment。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStaticPotentialShelfBiasPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
  -> StableLadderEndpointOrbitStaticPotentialShelfBiasImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterStaticShelfAreaLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterStaticShelfAreaLedger
  AND StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterStaticShelfAreaLedger
  AND StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterStaticShelfAreaLedger
  AND StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterStaticShelfAreaLedger
  AND StableLadderEndpointOrbitStaticShelfBiasModelLedger
  AND StableLadderEndpointOrbitStaticShelfAreaLowerBoundLedger
  AND StableLadderEndpointOrbitShelfSummationByPartsLedger
  AND StableLadderEndpointOrbitShelfEndpointChargeReturnLedger
  AND StableLadderEndpointOrbitStaticShelfAreaMomentPacketLedger
  AND NoAnonymousStaticPotentialShelfBiasExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterStaticShelfAreaLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStaticShelfAreaMomentPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步关闭的是匿名 static potential shelf bias 口径。剩余集中为 endpoint singleton
atom/SAE、endpoint orbit full-cycle mean atom/SAE、static shelf area moment
PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap，或 sparse scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

### 1.70 stable-ladder endpoint orbit static-shelf centroid-moment 更新

新增机器证书：

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_static_shelf_centroid_moment_router.py
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-centroid-moment-ledger.json
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-centroid-moment-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-centroid-moment-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStaticShelfAreaMomentPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
endpoint_orbit_static_shelf_area_moment_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_bridge_cancellation_carried_forward=true
endpoint_orbit_amplitude_depth_carried_forward=true
endpoint_orbit_variation_boundary_flux_carried_forward=true
endpoint_orbit_static_shelf_area_moment_model_closed=true
endpoint_orbit_static_shelf_boundary_collar_split_closed=true
endpoint_orbit_static_shelf_collar_charge_return_closed=true
endpoint_orbit_static_shelf_interior_core_mass_closed=true
endpoint_orbit_static_shelf_interior_centroid_moment_packet_registered=true
anonymous_static_shelf_area_moment_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_static_shelf_interior_centroid_moment_pdec_cap_proved=false
endpoint_orbit_bridge_cancellation_pdec_cap_proved=false
endpoint_orbit_amplitude_depth_pdec_cap_proved=false
endpoint_orbit_variation_boundary_flux_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

static shelf area moment 若存在，先按 `eta` 把 shelf 区间拆成左右边界 collar 与 interior core：

```text
I = C_left(eta L) union K_eta union C_right(eta L).
```

若 weighted increment moment 主要落在 collar，则仍是端点收费，回流 bridge-cancellation、
amplitude-depth 或 variation-boundary flux。若 collar 不能支付，至少固定比例的 moment
必须落在远离端点的 `K_eta`，并给出内部有向质心：

```text
c_K = sum_{t in K_eta} t*w(t)*sigma*d_t / sum_{t in K_eta} w(t)*sigma*d_t.
```

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStaticShelfAreaMomentPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
  -> StableLadderEndpointOrbitStaticShelfAreaMomentImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterStaticShelfCentroidLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterStaticShelfCentroidLedger
  AND StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterStaticShelfCentroidLedger
  AND StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterStaticShelfCentroidLedger
  AND StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterStaticShelfCentroidLedger
  AND StableLadderEndpointOrbitStaticShelfAreaMomentModelLedger
  AND StableLadderEndpointOrbitStaticShelfBoundaryCollarSplitLedger
  AND StableLadderEndpointOrbitStaticShelfCollarChargeReturnLedger
  AND StableLadderEndpointOrbitStaticShelfInteriorCoreMassLedger
  AND StableLadderEndpointOrbitStaticShelfInteriorCentroidMomentPacketLedger
  AND NoAnonymousStaticShelfAreaMomentExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterStaticShelfCentroidLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStaticShelfInteriorCentroidMomentPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步关闭的是匿名 static shelf area moment 口径。剩余集中为 endpoint singleton
atom/SAE、endpoint orbit full-cycle mean atom/SAE、static shelf interior centroid
moment PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap，或 sparse scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

### 1.71 stable-ladder endpoint orbit static-shelf centroid phase-lock 更新

新增机器证书：

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_static_shelf_centroid_phase_lock_router.py
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-centroid-phase-lock-ledger.json
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-centroid-phase-lock-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-centroid-phase-lock-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStaticShelfInteriorCentroidMomentPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
endpoint_orbit_static_shelf_interior_centroid_moment_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_bridge_cancellation_carried_forward=true
endpoint_orbit_amplitude_depth_carried_forward=true
endpoint_orbit_variation_boundary_flux_carried_forward=true
endpoint_orbit_interior_centroid_coordinate_model_closed=true
endpoint_orbit_interior_centroid_scale_window_closed=true
endpoint_orbit_interior_centroid_drift_return_closed=true
endpoint_orbit_interior_centroid_opposite_sign_bridge_return_closed=true
endpoint_orbit_interior_centroid_same_sign_stack_return_closed=true
endpoint_orbit_interior_centroid_phase_lock_packet_registered=true
anonymous_static_shelf_interior_centroid_moment_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_static_shelf_interior_centroid_phase_lock_pdec_cap_proved=false
endpoint_orbit_bridge_cancellation_pdec_cap_proved=false
endpoint_orbit_amplitude_depth_pdec_cap_proved=false
endpoint_orbit_variation_boundary_flux_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

static shelf interior centroid moment 若真实存在，先把每个窗口的内部质心归一化为：

```text
m_j = sum_{t in K_j} w_j(t)*sigma_j*d_t
c_j = sum_{t in K_j} t*w_j(t)*sigma_j*d_t / m_j
theta_j = (c_j-a_j)/L_j in [eta,1-eta].
```

若 `theta_j` 在 stable ladder 窗口中持续显著漂移，则内部质量必须跨过相位切线，回流
variation-boundary flux。若同相或邻近相位单元出现足量反号质量，则回流 bridge-cancellation。
若同相同号质量持续堆高并超过势能预算，则回流 amplitude-depth。三类支付都不足时，剩余只能
是持久内部质心相位锁定包。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStaticShelfInteriorCentroidMomentPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
  -> StableLadderEndpointOrbitStaticShelfInteriorCentroidMomentImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterCentroidPhaseLockLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterCentroidPhaseLockLedger
  AND StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterCentroidPhaseLockLedger
  AND StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterCentroidPhaseLockLedger
  AND StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterCentroidPhaseLockLedger
  AND StableLadderEndpointOrbitInteriorCentroidCoordinateModelLedger
  AND StableLadderEndpointOrbitInteriorCentroidScaleWindowLedger
  AND StableLadderEndpointOrbitInteriorCentroidDriftReturnLedger
  AND StableLadderEndpointOrbitInteriorCentroidOppositeSignBridgeReturnLedger
  AND StableLadderEndpointOrbitInteriorCentroidSameSignStackReturnLedger
  AND StableLadderEndpointOrbitInteriorCentroidPhaseLockPacketLedger
  AND NoAnonymousStaticShelfInteriorCentroidMomentExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterCentroidPhaseLockLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStaticShelfInteriorCentroidPhaseLockPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步关闭的是匿名 static shelf interior centroid moment 口径。剩余集中为 endpoint singleton
atom/SAE、endpoint orbit full-cycle mean atom/SAE、static shelf interior centroid
phase-lock PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap，或 sparse scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

### 1.72 stable-ladder endpoint orbit locked phase-cell pressure 更新

新增机器证书：

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_locked_phase_cell_pressure_router.py
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-phase-cell-pressure-ledger.json
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-phase-cell-pressure-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-phase-cell-pressure-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStaticShelfInteriorCentroidPhaseLockPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
endpoint_orbit_interior_centroid_phase_lock_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_bridge_cancellation_carried_forward=true
endpoint_orbit_amplitude_depth_carried_forward=true
endpoint_orbit_variation_boundary_flux_carried_forward=true
endpoint_orbit_locked_interior_phase_cell_model_closed=true
endpoint_orbit_locked_phase_cell_finite_slot_closed=true
endpoint_orbit_locked_phase_cell_actual_residue_word_closed=true
endpoint_orbit_locked_phase_cell_sparse_or_stable_subsequence_closed=true
endpoint_orbit_locked_phase_cell_column_pressure_packet_registered=true
anonymous_interior_centroid_phase_lock_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_locked_interior_phase_cell_column_pressure_pdec_cap_proved=false
endpoint_orbit_bridge_cancellation_pdec_cap_proved=false
endpoint_orbit_amplitude_depth_pdec_cap_proved=false
endpoint_orbit_variation_boundary_flux_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

interior centroid phase-lock 若真实存在，说明 surviving mass 长期停在有限内部相位单元中。
把相位单元、符号、dyadic mass 档和 actual CRT residue word 组成有限槽位：

```text
B_r = [eta+r*rho, eta+(r+1)*rho]
omega = (phase_cell r, sign, dyadic_mass_band, actual_residue_word).
```

若没有任何槽位在无穷尺度上持续承载质量，则该分支进入 sparse scale-ladder SAE。若 sparse
出口不支付，则无穷鸽巢给出持久 `omega`，特别是持久 actual residue word；它在 CRT cylinder
中投影成固定列或窄列族，并形成 locked phase-cell column pressure。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStaticShelfInteriorCentroidPhaseLockPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
  -> StableLadderEndpointOrbitInteriorCentroidPhaseLockImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterLockedPhaseCellLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterLockedPhaseCellLedger
  AND StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterLockedPhaseCellLedger
  AND StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterLockedPhaseCellLedger
  AND StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterLockedPhaseCellLedger
  AND StableLadderEndpointOrbitLockedInteriorPhaseCellModelLedger
  AND StableLadderEndpointOrbitLockedPhaseCellFiniteSlotLedger
  AND StableLadderEndpointOrbitLockedPhaseCellActualResidueWordLedger
  AND StableLadderEndpointOrbitLockedPhaseCellSparseOrStableSubsequenceLedger
  AND StableLadderEndpointOrbitLockedPhaseCellColumnPressurePacketLedger
  AND NoAnonymousInteriorCentroidPhaseLockExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterLockedPhaseCellLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLockedInteriorPhaseCellColumnPressurePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步关闭的是匿名 interior centroid phase-lock 口径。剩余集中为 endpoint singleton atom/SAE、
endpoint orbit full-cycle mean atom/SAE、locked interior phase-cell column pressure PDEC/cap、
bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap，
或 sparse scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

### 1.73 stable-ladder endpoint orbit locked-column capacity 更新

新增机器证书：

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_locked_column_capacity_router.py
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-column-capacity-ledger.json
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-column-capacity-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-column-capacity-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLockedInteriorPhaseCellColumnPressurePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
endpoint_orbit_locked_phase_cell_column_pressure_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_bridge_cancellation_carried_forward=true
endpoint_orbit_amplitude_depth_carried_forward=true
endpoint_orbit_variation_boundary_flux_carried_forward=true
endpoint_orbit_locked_column_family_model_closed=true
endpoint_orbit_locked_column_fiber_quota_closed=true
endpoint_orbit_locked_column_load_quota_dichotomy_closed=true
endpoint_orbit_locked_column_under_quota_return_closed=true
endpoint_orbit_locked_column_capacity_defect_packet_registered=true
anonymous_locked_phase_cell_column_pressure_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_locked_column_capacity_defect_pdec_cap_proved=false
endpoint_orbit_bridge_cancellation_pdec_cap_proved=false
endpoint_orbit_amplitude_depth_pdec_cap_proved=false
endpoint_orbit_variation_boundary_flux_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

locked phase-cell column pressure 给出固定列或窄列族 `C` 上的 signed load。登记：

```text
L(C)=sum_{omega projects to C} signed_mass(omega)
Q(C)=local_CRT_allowed_fiber_count(C)*scale_weight.
```

若 `|L(C)| <= Q(C)`，列压力未超额，不能支付上一层强制锁定质量，必须回流
full-cycle mean、singleton、sparse 或 bridge/amplitude/boundary。若 `|L(C)| > Q(C)`，
固定列族超过 CRT 允许纤维容量，得到 locked column capacity defect。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLockedInteriorPhaseCellColumnPressurePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
  -> StableLadderEndpointOrbitLockedPhaseCellColumnPressureImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterLockedColumnCapacityLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterLockedColumnCapacityLedger
  AND StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterLockedColumnCapacityLedger
  AND StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterLockedColumnCapacityLedger
  AND StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterLockedColumnCapacityLedger
  AND StableLadderEndpointOrbitLockedColumnFamilyModelLedger
  AND StableLadderEndpointOrbitLockedColumnFiberQuotaLedger
  AND StableLadderEndpointOrbitLockedColumnLoadQuotaDichotomyLedger
  AND StableLadderEndpointOrbitLockedColumnUnderQuotaReturnLedger
  AND StableLadderEndpointOrbitLockedColumnCapacityDefectPacketLedger
  AND NoAnonymousLockedPhaseCellColumnPressureExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterLockedColumnCapacityLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLockedColumnCapacityDefectPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步关闭的是匿名 locked phase-cell column pressure 口径。剩余集中为 endpoint singleton
atom/SAE、endpoint orbit full-cycle mean atom/SAE、locked column capacity defect PDEC/cap、
bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap，
或 sparse scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

### 1.74 stable-ladder endpoint orbit locked-column residue-shadow 更新

新增机器证书：

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_locked_column_residue_shadow_router.py
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-column-residue-shadow-ledger.json
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-column-residue-shadow-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-column-residue-shadow-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLockedColumnCapacityDefectPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
endpoint_orbit_locked_column_capacity_defect_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_bridge_cancellation_carried_forward=true
endpoint_orbit_amplitude_depth_carried_forward=true
endpoint_orbit_variation_boundary_flux_carried_forward=true
endpoint_orbit_locked_column_residue_shadow_model_closed=true
endpoint_orbit_locked_column_residue_shadow_quota_closed=true
endpoint_orbit_locked_column_overfull_shadow_pigeonhole_closed=true
endpoint_orbit_locked_column_residue_shadow_named_return_split_closed=true
endpoint_orbit_locked_column_residue_shadow_imbalance_packet_registered=true
anonymous_locked_column_capacity_defect_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_locked_column_residue_shadow_imbalance_pdec_cap_proved=false
endpoint_orbit_bridge_cancellation_pdec_cap_proved=false
endpoint_orbit_amplitude_depth_pdec_cap_proved=false
endpoint_orbit_variation_boundary_flux_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

locked column capacity defect 给出固定列族 `C` 的容量超额。按 CRT residue shadow 分解：

```text
L(C)=sum_s L_s
Q(C)=sum_s Q_s.
```

若所有 shadow 都满足 `|L_s|<=Q_s`，则总列族也不会超额；所以容量缺陷必给出至少一个
overfull residue shadow。该 shadow 若退化为孤立点、整周期均值、反号互付、同号堆高或边界迁移，
分别回流 singleton、full-cycle mean、bridge、amplitude 或 boundary；否则剩余就是真实
locked column residue-shadow imbalance。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLockedColumnCapacityDefectPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
  -> StableLadderEndpointOrbitLockedColumnCapacityDefectImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterLockedColumnResidueShadowLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterLockedColumnResidueShadowLedger
  AND StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterLockedColumnResidueShadowLedger
  AND StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterLockedColumnResidueShadowLedger
  AND StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterLockedColumnResidueShadowLedger
  AND StableLadderEndpointOrbitLockedColumnResidueShadowModelLedger
  AND StableLadderEndpointOrbitLockedColumnResidueShadowQuotaLedger
  AND StableLadderEndpointOrbitLockedColumnOverfullShadowPigeonholeLedger
  AND StableLadderEndpointOrbitLockedColumnResidueShadowNamedReturnSplitLedger
  AND StableLadderEndpointOrbitLockedColumnResidueShadowImbalancePacketLedger
  AND NoAnonymousLockedColumnCapacityDefectExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterLockedColumnResidueShadowLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLockedColumnResidueShadowImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步关闭的是匿名 locked column capacity defect 口径。剩余集中为 endpoint singleton
atom/SAE、endpoint orbit full-cycle mean atom/SAE、locked column residue-shadow imbalance
PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux
PDEC/cap，或 sparse scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

### 1.75 stable-ladder endpoint orbit residue-shadow dual-row 更新

新增机器证书：

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_router.py
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-ledger.json
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLockedColumnResidueShadowImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
endpoint_orbit_locked_column_residue_shadow_imbalance_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_bridge_cancellation_carried_forward=true
endpoint_orbit_amplitude_depth_carried_forward=true
endpoint_orbit_variation_boundary_flux_carried_forward=true
endpoint_orbit_residue_shadow_dual_row_map_closed=true
endpoint_orbit_residue_shadow_dual_row_fiber_closed=true
endpoint_orbit_residue_shadow_dual_row_average_return_closed=true
endpoint_orbit_residue_shadow_dual_row_pressure_packet_registered=true
anonymous_locked_column_residue_shadow_imbalance_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_residue_shadow_dual_row_pressure_pdec_cap_proved=false
endpoint_orbit_bridge_cancellation_pdec_cap_proved=false
endpoint_orbit_amplitude_depth_pdec_cap_proved=false
endpoint_orbit_variation_boundary_flux_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

locked column residue-shadow imbalance 是列方向的局部超额。CRT 对偶把该 shadow 投影为
dual-row shadow，并保留 signed excess：

```text
s -> R_s
E(R_s)=E(C_s).
```

若 `R_s` 没有真实行压力，列 shadow excess 会在行纤维平均中被吸收，回流
full-cycle mean、singleton、sparse 或 bridge/amplitude/boundary。若不能吸收，则剩余就是
residue-shadow dual-row pressure。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLockedColumnResidueShadowImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
  -> StableLadderEndpointOrbitLockedColumnResidueShadowImbalanceImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterResidueShadowDualRowLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterResidueShadowDualRowLedger
  AND StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterResidueShadowDualRowLedger
  AND StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterResidueShadowDualRowLedger
  AND StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterResidueShadowDualRowLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowMapLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowFiberLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowAverageReturnLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPressurePacketLedger
  AND NoAnonymousLockedColumnResidueShadowImbalanceExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterResidueShadowDualRowLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPressurePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步关闭的是匿名 locked column residue-shadow imbalance 口径。剩余集中为 endpoint singleton
atom/SAE、endpoint orbit full-cycle mean atom/SAE、residue-shadow dual-row pressure
PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux
PDEC/cap，或 sparse scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

### 1.76 stable-ladder endpoint orbit residue-shadow dual-row capacity 更新

新增机器证书：

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_capacity_router.py
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-capacity-ledger.json
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-capacity-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-capacity-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPressurePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
endpoint_orbit_residue_shadow_dual_row_pressure_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_bridge_cancellation_carried_forward=true
endpoint_orbit_amplitude_depth_carried_forward=true
endpoint_orbit_variation_boundary_flux_carried_forward=true
endpoint_orbit_residue_shadow_dual_row_pressure_model_closed=true
endpoint_orbit_residue_shadow_dual_row_window_closed=true
endpoint_orbit_residue_shadow_dual_row_capacity_quota_closed=true
endpoint_orbit_residue_shadow_dual_row_load_quota_dichotomy_closed=true
endpoint_orbit_residue_shadow_dual_row_under_quota_return_closed=true
endpoint_orbit_residue_shadow_dual_row_capacity_defect_packet_registered=true
anonymous_residue_shadow_dual_row_pressure_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_residue_shadow_dual_row_capacity_defect_pdec_cap_proved=false
endpoint_orbit_bridge_cancellation_pdec_cap_proved=false
endpoint_orbit_amplitude_depth_pdec_cap_proved=false
endpoint_orbit_variation_boundary_flux_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

residue-shadow dual-row pressure 必须落在具体对偶行窗口 `R` 上。该窗口的 signed load 与
局部 CRT 行纤维容量分别为：

```text
H(R)=sum_{omega projects to R} signed_mass(omega)
B(R)=local_CRT_allowed_row_fiber_count(R)*scale_weight.
```

若 `|H(R)|<=B(R)`，对偶行窗口没有真实容量压力，无法支付上一层强制压力，必须回流
full-cycle mean、singleton、sparse 或 bridge/amplitude/boundary。若 `|H(R)|>B(R)`，
剩余就是 residue-shadow dual-row capacity defect。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPressurePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
  -> StableLadderEndpointOrbitResidueShadowDualRowPressureImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterResidueShadowDualRowCapacityLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterResidueShadowDualRowCapacityLedger
  AND StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterResidueShadowDualRowCapacityLedger
  AND StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterResidueShadowDualRowCapacityLedger
  AND StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterResidueShadowDualRowCapacityLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPressureModelLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowWindowLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowCapacityQuotaLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowLoadQuotaDichotomyLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowUnderQuotaReturnLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowCapacityDefectPacketLedger
  AND NoAnonymousResidueShadowDualRowPressureExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterResidueShadowDualRowCapacityLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowCapacityDefectPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步关闭的是匿名 residue-shadow dual-row pressure 口径。剩余集中为 endpoint singleton
atom/SAE、endpoint orbit full-cycle mean atom/SAE、residue-shadow dual-row capacity defect
PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux
PDEC/cap，或 sparse scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

### 1.77 stable-ladder endpoint orbit residue-shadow dual-row phase-cell 更新

新增机器证书：

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_phase_cell_router.py
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-ledger.json
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowCapacityDefectPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
endpoint_orbit_residue_shadow_dual_row_capacity_defect_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_bridge_cancellation_carried_forward=true
endpoint_orbit_amplitude_depth_carried_forward=true
endpoint_orbit_variation_boundary_flux_carried_forward=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_model_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_quota_closed=true
endpoint_orbit_residue_shadow_dual_row_overfull_phase_cell_pigeonhole_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_named_return_split_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_imbalance_packet_registered=true
anonymous_residue_shadow_dual_row_capacity_defect_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_residue_shadow_dual_row_phase_cell_imbalance_pdec_cap_proved=false
endpoint_orbit_bridge_cancellation_pdec_cap_proved=false
endpoint_orbit_amplitude_depth_pdec_cap_proved=false
endpoint_orbit_variation_boundary_flux_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

residue-shadow dual-row capacity defect 已经落在某个对偶行窗口 `R` 上。把该窗口按 CRT
phase-cell `theta` 分解：

```text
H(R)=sum_theta H_theta
B(R)=sum_theta B_theta
```

若 `|H(R)|>B(R)`，固定符号后不可能每个 phase-cell 都满足 `|H_theta|<=B_theta`；
否则加总后整个 `R` 也不超额。因此至少存在一个 overfull phase-cell。若该 cell
退化为孤立点、整周期均值、反号互付、同号堆高或边界迁移，则分别回流 singleton、
full-cycle mean、bridge、amplitude 或 boundary；否则剩余就是 residue-shadow
dual-row phase-cell imbalance。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowCapacityDefectPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
  -> StableLadderEndpointOrbitResidueShadowDualRowCapacityDefectImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterResidueShadowDualRowPhaseCellLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterResidueShadowDualRowPhaseCellLedger
  AND StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterResidueShadowDualRowPhaseCellLedger
  AND StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterResidueShadowDualRowPhaseCellLedger
  AND StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterResidueShadowDualRowPhaseCellLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellModelLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellQuotaLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowOverfullPhaseCellPigeonholeLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellNamedReturnSplitLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellImbalancePacketLedger
  AND NoAnonymousResidueShadowDualRowCapacityDefectExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterResidueShadowDualRowPhaseCellLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步关闭的是匿名 residue-shadow dual-row capacity defect 口径。剩余集中为 endpoint
singleton atom/SAE、endpoint orbit full-cycle mean atom/SAE、residue-shadow dual-row
phase-cell imbalance PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap，或 sparse scale-ladder SAE 全局求和。行/列命题仍未
无条件闭合。

### 1.78 stable-ladder endpoint orbit residue-shadow dual-row phase-cell atom 更新

新增机器证书：

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_router.py
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-ledger.json
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
endpoint_orbit_residue_shadow_dual_row_phase_cell_imbalance_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_bridge_cancellation_carried_forward=true
endpoint_orbit_amplitude_depth_carried_forward=true
endpoint_orbit_variation_boundary_flux_carried_forward=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_model_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_quota_closed=true
endpoint_orbit_residue_shadow_dual_row_overfull_phase_cell_atom_pigeonhole_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_named_return_split_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_imbalance_packet_registered=true
anonymous_residue_shadow_dual_row_phase_cell_imbalance_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_imbalance_pdec_cap_proved=false
endpoint_orbit_bridge_cancellation_pdec_cap_proved=false
endpoint_orbit_amplitude_depth_pdec_cap_proved=false
endpoint_orbit_variation_boundary_flux_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

residue-shadow dual-row phase-cell imbalance 已经落在固定 CRT phase-cell `theta` 上。把该
cell 内部按实际 residue/source atom `a` 分解：

```text
H_theta=sum_a h_{theta,a}
B_theta=sum_a b_{theta,a}
```

若 `|H_theta|>B_theta`，取 `sigma=sign(H_theta)`。如果所有 atom 都满足
`sigma*h_{theta,a}<=b_{theta,a}`，则加总得到 `|H_theta|<=B_theta`，矛盾。因此至少有一个
同号 atom 满足 `sigma*h_{theta,a}>b_{theta,a}`。若该 atom 退化为孤立点、整周期均值、
反号互付、同号堆高或边界迁移，则分别回流 singleton、full-cycle mean、bridge、amplitude
或 boundary；否则剩余就是 residue-shadow dual-row phase-cell atom imbalance。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
  -> StableLadderEndpointOrbitResidueShadowDualRowPhaseCellImbalanceImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterResidueShadowDualRowPhaseCellAtomLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterResidueShadowDualRowPhaseCellAtomLedger
  AND StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterResidueShadowDualRowPhaseCellAtomLedger
  AND StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterResidueShadowDualRowPhaseCellAtomLedger
  AND StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterResidueShadowDualRowPhaseCellAtomLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomModelLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomQuotaLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowOverfullPhaseCellAtomPigeonholeLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomNamedReturnSplitLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomImbalancePacketLedger
  AND NoAnonymousResidueShadowDualRowPhaseCellImbalanceExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterResidueShadowDualRowPhaseCellAtomLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步关闭的是匿名 residue-shadow dual-row phase-cell imbalance 口径。剩余集中为 endpoint
singleton atom/SAE、endpoint orbit full-cycle mean atom/SAE、residue-shadow dual-row
phase-cell atom imbalance PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth
PDEC/cap、variation-boundary flux PDEC/cap，或 sparse scale-ladder SAE 全局求和。
行/列命题仍未无条件闭合。

### 1.79 stable-ladder endpoint orbit residue-shadow dual-row phase-cell atom signed-core 更新

新增机器证书：

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_router.py
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-ledger.json
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_imbalance_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_bridge_cancellation_carried_forward=true
endpoint_orbit_amplitude_depth_carried_forward=true
endpoint_orbit_variation_boundary_flux_carried_forward=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_model_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_decomposition_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_lower_bound_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_named_return_split_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_imbalance_packet_registered=true
anonymous_residue_shadow_dual_row_phase_cell_atom_imbalance_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_imbalance_pdec_cap_proved=false
endpoint_orbit_bridge_cancellation_pdec_cap_proved=false
endpoint_orbit_amplitude_depth_pdec_cap_proved=false
endpoint_orbit_variation_boundary_flux_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

residue-shadow dual-row phase-cell atom imbalance 已经给出某个 atom 的同号净超额。固定
`sigma=sign(h_a)`，把该 atom 内部实际贡献拆为同号核心与反号抵消：

```text
sigma*h_a=C_plus-C_minus
sigma*h_a>b_a
```

因此：

```text
C_plus>b_a+C_minus
```

若 `C_minus` 形成真实反号互付，则回流 bridge-cancellation；否则压力已经集中为同号核心
超过自身 quota 加抵消债。若同号核心退化为孤立点、整周期均值、跨尺度堆高或边界迁移，
分别回流 singleton、full-cycle mean、amplitude 或 boundary；否则剩余就是 residue-shadow
dual-row phase-cell atom signed-core imbalance。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
  -> StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomImbalanceImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreLedger
  AND StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreLedger
  AND StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreLedger
  AND StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreModelLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedDecompositionLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreLowerBoundLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreNamedReturnSplitLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreImbalancePacketLedger
  AND NoAnonymousResidueShadowDualRowPhaseCellAtomImbalanceExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步关闭的是匿名 residue-shadow dual-row phase-cell atom imbalance 口径。剩余集中为
endpoint singleton atom/SAE、endpoint orbit full-cycle mean atom/SAE、residue-shadow
dual-row phase-cell atom signed-core imbalance PDEC/cap、bridge-cancellation PDEC/cap、
amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap，或 sparse scale-ladder SAE
全局求和。行/列命题仍未无条件闭合。

### 1.80 stable-ladder endpoint orbit residue-shadow dual-row phase-cell atom signed-core support-slice 更新

新增机器证书：

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_router.py
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-ledger.json
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_imbalance_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_bridge_cancellation_carried_forward=true
endpoint_orbit_amplitude_depth_carried_forward=true
endpoint_orbit_variation_boundary_flux_carried_forward=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_model_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_quota_debt_allocation_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_overfull_support_slice_pigeonhole_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_named_return_split_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_imbalance_packet_registered=true
anonymous_residue_shadow_dual_row_phase_cell_atom_signed_core_imbalance_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_imbalance_pdec_cap_proved=false
endpoint_orbit_bridge_cancellation_pdec_cap_proved=false
endpoint_orbit_amplitude_depth_pdec_cap_proved=false
endpoint_orbit_variation_boundary_flux_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

signed-core imbalance 已给出：

```text
C_plus>b_a+C_minus
```

把同号核心与 quota 加抵消债同步分解到有限 CRT/source support slice `s`：

```text
C_plus=sum_s C_s
b_a+C_minus=sum_s d_s
```

如果每个 support slice 都满足 `C_s<=d_s`，则加总得到 `C_plus<=b_a+C_minus`，矛盾。
因此至少有一个具体支撑槽满足 `C_s>d_s`。若该槽退化为孤立点、整周期均值、由抵消债
互付、同号跨尺度堆高或边界迁移，则分别回流 singleton、full-cycle mean、bridge、
amplitude 或 boundary；否则剩余就是 residue-shadow dual-row phase-cell atom signed-core
support-slice imbalance。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
  -> StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreImbalanceImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceLedger
  AND StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceLedger
  AND StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceLedger
  AND StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceModelLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceQuotaDebtAllocationLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreOverfullSupportSlicePigeonholeLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceNamedReturnSplitLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceImbalancePacketLedger
  AND NoAnonymousResidueShadowDualRowPhaseCellAtomSignedCoreImbalanceExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步关闭的是匿名 residue-shadow dual-row phase-cell atom signed-core imbalance 口径。剩余
集中为 endpoint singleton atom/SAE、endpoint orbit full-cycle mean atom/SAE、support-slice
imbalance PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap，或 sparse scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

### 1.81 stable-ladder endpoint orbit residue-shadow dual-row phase-cell atom signed-core support-slice residue-fiber 更新

新增机器证书：

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_router.py
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-ledger.json
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_imbalance_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_bridge_cancellation_carried_forward=true
endpoint_orbit_amplitude_depth_carried_forward=true
endpoint_orbit_variation_boundary_flux_carried_forward=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_model_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_quota_debt_allocation_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_overfull_support_slice_residue_fiber_pigeonhole_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_named_return_split_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_imbalance_packet_registered=true
anonymous_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_imbalance_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_imbalance_pdec_cap_proved=false
endpoint_orbit_bridge_cancellation_pdec_cap_proved=false
endpoint_orbit_amplitude_depth_pdec_cap_proved=false
endpoint_orbit_variation_boundary_flux_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

support-slice imbalance 已给出：

```text
C_s>d_s
```

把该槽继续按实际 CRT residue fiber `rho` 分解：

```text
C_s=sum_rho C_{s,rho}
d_s=sum_rho d_{s,rho}
```

如果每个 residue fiber 都满足 `C_{s,rho}<=d_{s,rho}`，则加总得到 `C_s<=d_s`，矛盾。
因此至少有一个具体 residue fiber 满足 `C_{s,rho}>d_{s,rho}`。若该 fiber 退化为孤立点、
整周期均值、由抵消债互付、同号跨尺度堆高或边界迁移，则分别回流 singleton、
full-cycle mean、bridge、amplitude 或 boundary；否则剩余就是 residue-shadow dual-row
phase-cell atom signed-core support-slice residue-fiber imbalance。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
  -> StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceImbalanceImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberLedger
  AND StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberLedger
  AND StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberLedger
  AND StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberModelLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberQuotaDebtAllocationLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreOverfullSupportSliceResidueFiberPigeonholeLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberNamedReturnSplitLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberImbalancePacketLedger
  AND NoAnonymousResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceImbalanceExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步关闭的是匿名 support-slice imbalance 口径。剩余集中为 endpoint singleton atom/SAE、
endpoint orbit full-cycle mean atom/SAE、support-slice residue-fiber imbalance PDEC/cap、
bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap，
或 sparse scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

### 1.82 stable-ladder endpoint orbit residue-shadow dual-row phase-cell atom signed-core support-slice residue-fiber phase-word 更新

新增机器证书：

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_router.py
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-ledger.json
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_imbalance_imported=true
endpoint_singleton_atom_sae_carried_forward=true
endpoint_orbit_full_cycle_mean_atom_carried_forward=true
endpoint_orbit_bridge_cancellation_carried_forward=true
endpoint_orbit_amplitude_depth_carried_forward=true
endpoint_orbit_variation_boundary_flux_carried_forward=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_model_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_quota_debt_allocation_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_overfull_support_slice_residue_fiber_phase_word_pigeonhole_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_named_return_split_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_imbalance_packet_registered=true
anonymous_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_imbalance_removed=true
sparse_scale_ladder_sae_carried_forward=true
endpoint_singleton_atom_sae_proved=false
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_imbalance_pdec_cap_proved=false
endpoint_orbit_bridge_cancellation_pdec_cap_proved=false
endpoint_orbit_amplitude_depth_pdec_cap_proved=false
endpoint_orbit_variation_boundary_flux_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

residue-fiber imbalance 已给出：

```text
C_{s,rho}>d_{s,rho}
```

把该 fiber 继续按有限 CRT phase word `omega` 分解：

```text
C_{s,rho}=sum_omega C_{s,rho,omega}
d_{s,rho}=sum_omega d_{s,rho,omega}
```

如果每个 phase word 都满足 `C_{s,rho,omega}<=d_{s,rho,omega}`，则加总得到
`C_{s,rho}<=d_{s,rho}`，矛盾。因此至少有一个具体 phase word 满足
`C_{s,rho,omega}>d_{s,rho,omega}`。若该 phase word 退化为孤立点、整周期均值、由抵消债
互付、同号跨尺度堆高或边界迁移，则分别回流 singleton、full-cycle mean、bridge、
amplitude 或 boundary；否则剩余就是 residue-shadow dual-row phase-cell atom signed-core
support-slice residue-fiber phase-word imbalance。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
  -> StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberImbalanceImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordLedger
  AND StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordLedger
  AND StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordLedger
  AND StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordModelLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordQuotaDebtAllocationLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreOverfullSupportSliceResidueFiberPhaseWordPigeonholeLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordNamedReturnSplitLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordImbalancePacketLedger
  AND NoAnonymousResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberImbalanceExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步关闭的是匿名 residue-fiber imbalance 口径。剩余集中为 endpoint singleton atom/SAE、
endpoint orbit full-cycle mean atom/SAE、support-slice residue-fiber phase-word imbalance
PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux
PDEC/cap，或 sparse scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

### 1.83 stable-ladder endpoint orbit residue-shadow dual-row phase-cell atom signed-core support-slice residue-fiber phase-word-slot 更新

新增机器证书：

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_router.py
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-ledger.json
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_imbalance_imported=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_model_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_quota_debt_allocation_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_overfull_support_slice_residue_fiber_phase_word_slot_pigeonhole_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_named_return_split_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_imbalance_packet_registered=true
anonymous_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_imbalance_removed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_imbalance_pdec_cap_proved=false
row_column_unconditional_closed=false
```

phase-word imbalance 已给出：

```text
C_{s,rho,omega}>d_{s,rho,omega}
```

把该 phase word 继续按有限实际 CRT word slot `tau` 分解：

```text
C_{s,rho,omega}=sum_tau C_{s,rho,omega,tau}
d_{s,rho,omega}=sum_tau d_{s,rho,omega,tau}
```

如果每个 word slot 都满足 `C_{s,rho,omega,tau}<=d_{s,rho,omega,tau}`，则加总得到
`C_{s,rho,omega}<=d_{s,rho,omega}`，矛盾。因此至少有一个具体 word slot 满足
`C_{s,rho,omega,tau}>d_{s,rho,omega,tau}`。若该 word slot 退化为孤立点、整周期均值、
由抵消债互付、同号跨尺度堆高或边界迁移，则分别回流 singleton、full-cycle mean、
bridge、amplitude 或 boundary；否则剩余就是 residue-shadow dual-row phase-cell atom
signed-core support-slice residue-fiber phase-word-slot imbalance。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
  -> StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordImbalanceImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotLedger
  AND StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotLedger
  AND StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotLedger
  AND StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotModelLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotQuotaDebtAllocationLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreOverfullSupportSliceResidueFiberPhaseWordSlotPigeonholeLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotNamedReturnSplitLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotImbalancePacketLedger
  AND NoAnonymousResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordImbalanceExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步关闭的是匿名 phase-word imbalance 口径。剩余集中为 endpoint singleton atom/SAE、
endpoint orbit full-cycle mean atom/SAE、support-slice residue-fiber phase-word-slot
imbalance PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap，或 sparse scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

### 1.84 stable-ladder endpoint orbit residue-shadow dual-row phase-cell atom signed-core support-slice residue-fiber phase-word-slot source-atom 更新

新增机器证书：

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_router.py
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-ledger.json
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_imbalance_imported=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_model_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_quota_debt_allocation_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_overfull_support_slice_residue_fiber_phase_word_slot_source_atom_pigeonhole_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_named_return_split_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_imbalance_packet_registered=true
anonymous_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_imbalance_removed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_imbalance_pdec_cap_proved=false
row_column_unconditional_closed=false
```

phase-word-slot imbalance 已给出：

```text
C_{s,rho,omega,tau}>d_{s,rho,omega,tau}
```

把该 word slot 继续按有限实际 endpoint/source atom `alpha` 分解：

```text
C_{s,rho,omega,tau}=sum_alpha C_{s,rho,omega,tau,alpha}
d_{s,rho,omega,tau}=sum_alpha d_{s,rho,omega,tau,alpha}
```

如果每个 source atom 都满足 `C_{s,rho,omega,tau,alpha}<=d_{s,rho,omega,tau,alpha}`，
则加总得到 `C_{s,rho,omega,tau}<=d_{s,rho,omega,tau}`，矛盾。因此至少有一个实际
source atom 满足 `C_{s,rho,omega,tau,alpha}>d_{s,rho,omega,tau,alpha}`。若该 atom
退化为孤立点、整周期均值、由抵消债互付、同号跨尺度堆高或边界迁移，则分别回流
singleton、full-cycle mean、bridge、amplitude 或 boundary；否则剩余就是 phase-word-slot
source-atom imbalance。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
  -> StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotImbalanceImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomLedger
  AND StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomLedger
  AND StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomLedger
  AND StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomModelLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomQuotaDebtAllocationLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreOverfullSupportSliceResidueFiberPhaseWordSlotSourceAtomPigeonholeLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomNamedReturnSplitLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomImbalancePacketLedger
  AND NoAnonymousResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotImbalanceExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步关闭的是匿名 phase-word-slot imbalance 口径。剩余集中为 endpoint singleton atom/SAE、
endpoint orbit full-cycle mean atom/SAE、phase-word-slot source-atom imbalance PDEC/cap、
bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap，
或 sparse scale-ladder SAE 全局求和。行/列命题仍未无条件闭合。

### 1.85 stable-ladder endpoint orbit residue-shadow dual-row phase-cell atom signed-core support-slice residue-fiber phase-word-slot source-atom multiplicity-fiber 更新

新增机器证书：

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_router.py
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-ledger.json
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_imbalance_imported=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_model_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_quota_debt_allocation_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_overfull_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_pigeonhole_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_cap_packet_registered=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_imbalance_packet_registered=true
anonymous_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_imbalance_removed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_cap_pdec_cap_proved=false
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_imbalance_pdec_cap_proved=false
row_column_unconditional_closed=false
```

source-atom imbalance 已给出：

```text
C_{s,rho,omega,tau,alpha}>d_{s,rho,omega,tau,alpha}
```

把该 source atom 内部按有限实际 multiplicity fiber `mu` 分解：

```text
C_{s,rho,omega,tau,alpha}=sum_mu C_{s,rho,omega,tau,alpha,mu}
d_{s,rho,omega,tau,alpha}=sum_mu d_{s,rho,omega,tau,alpha,mu}
```

若同一 source atom 的实际出现重数已经超过局部 cap，则登记为
source-atom multiplicity-cap PDEC/cap。否则，如果每个 fiber 都满足
`C_{s,rho,omega,tau,alpha,mu}<=d_{s,rho,omega,tau,alpha,mu}`，则加总得到
`C_{s,rho,omega,tau,alpha}<=d_{s,rho,omega,tau,alpha}`，矛盾。因此至少有一个实际
multiplicity fiber 满足
`C_{s,rho,omega,tau,alpha,mu}>d_{s,rho,omega,tau,alpha,mu}`。若该 fiber 退化为孤立点、
整周期均值、由抵消债互付、同号跨尺度堆高或边界迁移，则分别回流 singleton、
full-cycle mean、bridge、amplitude 或 boundary；否则剩余就是 source-atom
multiplicity-fiber imbalance。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
  -> StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomImbalanceImportedLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberLedger
  AND StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberLedger
  AND StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberLedger
  AND StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberModelLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberQuotaDebtAllocationLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreOverfullSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberPigeonholeLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPacketLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberNamedReturnSplitLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberImbalancePacketLedger
  AND NoAnonymousResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomImbalanceExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步关闭的是匿名 source-atom imbalance 口径。剩余集中为 endpoint singleton atom/SAE、
endpoint orbit full-cycle mean atom/SAE、source-atom multiplicity-cap PDEC/cap、
source-atom multiplicity-fiber imbalance PDEC/cap、bridge-cancellation PDEC/cap、
amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap，或 sparse scale-ladder SAE
全局求和。行/列命题仍未无条件闭合。

### 1.86 stable-ladder endpoint orbit residue-shadow dual-row phase-cell atom signed-core support-slice residue-fiber phase-word-slot source-atom multiplicity-fiber signed-unit 更新

新增机器证书：

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_unit_router.py
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-signed-unit-ledger.json
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-signed-unit-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-signed-unit-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_imbalance_imported=true
source_atom_multiplicity_cap_carried_forward=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_occurrence_unit_model_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_occurrence_unit_quota_debt_allocation_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_overfull_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_occurrence_unit_pigeonhole_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_occurrence_unit_imbalance_packet_registered=true
anonymous_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_imbalance_removed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_cap_pdec_cap_proved=false
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_occurrence_unit_imbalance_pdec_cap_proved=false
row_column_unconditional_closed=false
```

multiplicity-fiber imbalance 已给出：

```text
C_{s,rho,omega,tau,alpha,mu}>d_{s,rho,omega,tau,alpha,mu}
```

把该 fiber 内部按有限实际 signed occurrence/load unit `eta` 分解：

```text
C_{s,rho,omega,tau,alpha,mu}=sum_eta C_{s,rho,omega,tau,alpha,mu,eta}
d_{s,rho,omega,tau,alpha,mu}=sum_eta d_{s,rho,omega,tau,alpha,mu,eta}
```

如果每个 signed unit 都满足
`C_{s,rho,omega,tau,alpha,mu,eta}<=d_{s,rho,omega,tau,alpha,mu,eta}`，则加总得到
`C_{s,rho,omega,tau,alpha,mu}<=d_{s,rho,omega,tau,alpha,mu}`，矛盾。因此至少有一个实际
signed occurrence unit 满足
`C_{s,rho,omega,tau,alpha,mu,eta}>d_{s,rho,omega,tau,alpha,mu,eta}`。source-atom
multiplicity-cap 异常不被本步吸收，继续作为独立出口。若该 signed unit 退化为孤立点、
整周期均值、由抵消债互付、同号跨尺度堆高或边界迁移，则分别回流 singleton、
full-cycle mean、bridge、amplitude 或 boundary；否则剩余就是 signed occurrence unit
imbalance。

硬点更新为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
  -> StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberImbalanceImportedLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapCarriedForwardAfterSignedUnitLedger
  AND StableLadderEndpointSingletonAtomSAECarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedUnitLedger
  AND StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedUnitLedger
  AND StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedUnitLedger
  AND StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedUnitLedger
  AND StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedUnitLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitModelLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitQuotaDebtAllocationLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreOverfullSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitPigeonholeLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitNamedReturnSplitLedger
  AND StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitImbalancePacketLedger
  AND NoAnonymousResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberImbalanceExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedUnitLedger
  AND SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步关闭的是匿名 multiplicity-fiber imbalance 口径。剩余集中为 endpoint singleton atom/SAE、
endpoint orbit full-cycle mean atom/SAE、source-atom multiplicity-cap PDEC/cap、
signed occurrence unit imbalance PDEC/cap、bridge-cancellation PDEC/cap、
amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap，或 sparse scale-ladder SAE
全局求和。行/列命题仍未无条件闭合。

### 1.87 stable-ladder endpoint orbit residue-shadow dual-row phase-cell atom signed-core support-slice residue-fiber phase-word-slot source-atom multiplicity-fiber signed-unit incidence-cell 更新

新增机器证书：

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_unit_incidence_cell_router.py
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-signed-unit-incidence-cell-ledger.json
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-signed-unit-incidence-cell-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-signed-unit-incidence-cell-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_occurrence_unit_imbalance_imported=true
source_atom_multiplicity_cap_carried_forward=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_occurrence_unit_incidence_cell_model_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_occurrence_unit_incidence_cell_quota_debt_allocation_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_overfull_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_occurrence_unit_incidence_cell_pigeonhole_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_occurrence_unit_incidence_cell_imbalance_packet_registered=true
anonymous_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_occurrence_unit_imbalance_removed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_cap_pdec_cap_proved=false
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_occurrence_unit_incidence_cell_imbalance_pdec_cap_proved=false
row_column_unconditional_closed=false
```

signed occurrence unit imbalance 已给出：

```text
C_{s,rho,omega,tau,alpha,mu,eta}>d_{s,rho,omega,tau,alpha,mu,eta}
```

把该 unit 内部按有限实际 incidence cell `iota` 分解：

```text
C_{s,rho,omega,tau,alpha,mu,eta}=sum_iota C_{s,rho,omega,tau,alpha,mu,eta,iota}
d_{s,rho,omega,tau,alpha,mu,eta}=sum_iota d_{s,rho,omega,tau,alpha,mu,eta,iota}
```

如果每个 incidence cell 都满足
`C_{s,rho,omega,tau,alpha,mu,eta,iota}<=d_{s,rho,omega,tau,alpha,mu,eta,iota}`，
则该 signed unit 不可能超额；所以必有某个 `iota` 满足
`C_{s,rho,omega,tau,alpha,mu,eta,iota}>d_{s,rho,omega,tau,alpha,mu,eta,iota}`。
source-atom multiplicity-cap PDEC/cap 不在本步证明，继续作为并行出口。该
incidence cell 若由 singleton、full-cycle mean、bridge、amplitude-depth、boundary flux
或 sparse SAE 支付，则回流已有出口；否则留下实际 incidence-cell imbalance
PDEC/cap。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、incidence-cell imbalance PDEC/cap、bridge-cancellation
PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap 或 sparse SAE 求和；
它只把匿名 signed occurrence unit imbalance 压成 incidence-cell imbalance 包或
mean/singleton/sparse/三出口。

### 1.88 stable-ladder endpoint orbit residue-shadow dual-row phase-cell atom signed-core support-slice residue-fiber phase-word-slot source-atom multiplicity-fiber signed-unit incidence-cell primitive-witness 更新

新增机器证书：

```text
experiments/prime_matrix_signed_unit_incidence_cell_primitive_witness_router.py
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-signed-unit-incidence-cell-primitive-witness-ledger.json
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-signed-unit-incidence-cell-primitive-witness-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-signed-unit-incidence-cell-primitive-witness-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_occurrence_unit_incidence_cell_imbalance_imported=true
source_atom_multiplicity_cap_carried_forward=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_occurrence_unit_incidence_cell_primitive_witness_model_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_occurrence_unit_incidence_cell_primitive_witness_quota_debt_allocation_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_overfull_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_occurrence_unit_incidence_cell_primitive_witness_pigeonhole_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_occurrence_unit_incidence_cell_primitive_witness_imbalance_packet_registered=true
anonymous_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_occurrence_unit_incidence_cell_imbalance_removed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_cap_pdec_cap_proved=false
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_occurrence_unit_incidence_cell_primitive_witness_imbalance_pdec_cap_proved=false
row_column_unconditional_closed=false
```

incidence-cell imbalance 已给出：

```text
C_{s,rho,omega,tau,alpha,mu,eta,iota}>d_{s,rho,omega,tau,alpha,mu,eta,iota}
```

把该 cell 内部按有限实际 primitive witness `kappa` 分解；`kappa` 记录实际行、列、载体素数、同余代表、端点侧和方向：

```text
C_{s,rho,omega,tau,alpha,mu,eta,iota}=sum_kappa C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa}
d_{s,rho,omega,tau,alpha,mu,eta,iota}=sum_kappa d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa}
```

如果每个 primitive witness 都满足
`C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa}<=d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa}`，
则该 incidence cell 不可能超额；所以必有某个 `kappa` 满足
`C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa}>d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa}`。
source-atom multiplicity-cap PDEC/cap 不在本步证明，继续作为并行出口。该 primitive
witness 若由 singleton、full-cycle mean、bridge、amplitude-depth、boundary flux 或
sparse SAE 支付，则回流已有出口；否则留下实际 primitive-witness imbalance PDEC/cap。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、primitive-witness imbalance PDEC/cap、bridge-cancellation
PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap 或 sparse SAE 求和；
它只把匿名 incidence-cell imbalance 压成 primitive-witness imbalance 包或
mean/singleton/sparse/三出口。

### 1.89 stable-ladder primitive-witness CRT-coordinate-atom 更新

新增机器证书：

```text
experiments/prime_matrix_primitive_witness_crt_coordinate_atom_router.py
data/prime-matrix-primitive-witness-crt-coordinate-atom-ledger.json
docs/monograph/prime-matrix-primitive-witness-crt-coordinate-atom-router.md
docs/monograph/prime-matrix-primitive-witness-crt-coordinate-atom-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_occurrence_unit_incidence_cell_primitive_witness_imbalance_imported=true
source_atom_multiplicity_cap_carried_forward=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_occurrence_unit_incidence_cell_primitive_witness_crt_coordinate_atom_model_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_occurrence_unit_incidence_cell_primitive_witness_crt_coordinate_atom_quota_debt_allocation_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_overfull_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_occurrence_unit_incidence_cell_primitive_witness_crt_coordinate_atom_pigeonhole_closed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_occurrence_unit_incidence_cell_primitive_witness_crt_coordinate_atom_imbalance_packet_registered=true
anonymous_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_occurrence_unit_incidence_cell_primitive_witness_imbalance_removed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_cap_pdec_cap_proved=false
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_occurrence_unit_incidence_cell_primitive_witness_crt_coordinate_atom_imbalance_pdec_cap_proved=false
row_column_unconditional_closed=false
```

primitive-witness imbalance 已给出：

```text
C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa}>d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa}
```

把该 witness 内部按有限规范 CRT coordinate atom `chi` 分解；`chi` 记录实际行、列、载体素数
`q`、同余残基 `a`、端点侧、方向，以及同余方程
`N_{row,column,side} == a mod q`：

```text
C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa}=sum_chi C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi}
d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa}=sum_chi d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi}
```

如果每个 CRT coordinate atom 都满足
`C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi}<=d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi}`，
则该 primitive witness 不可能超额；所以必有某个 `chi` 满足
`C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi}>d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi}`。
source-atom multiplicity-cap PDEC/cap 不在本步证明，继续作为并行出口。该 coordinate atom
若由 singleton、full-cycle mean、bridge、amplitude-depth、boundary flux 或 sparse SAE
支付，则回流已有出口；否则留下实际 CRT-coordinate-atom imbalance PDEC/cap。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、CRT-coordinate-atom imbalance PDEC/cap、bridge-cancellation
PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap 或 sparse SAE 求和；
它只把匿名 primitive-witness imbalance 压成 CRT-coordinate-atom imbalance 包或
mean/singleton/sparse/三出口。

### 1.90 stable-ladder CRT-coordinate canonical-equation 更新

新增机器证书：

```text
experiments/prime_matrix_crt_coordinate_canonical_equation_router.py
data/prime-matrix-crt-coordinate-canonical-equation-ledger.json
docs/monograph/prime-matrix-crt-coordinate-canonical-equation-router.md
docs/monograph/prime-matrix-crt-coordinate-canonical-equation-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
crt_coordinate_atom_imbalance_imported=true
source_atom_multiplicity_cap_carried_forward=true
crt_coordinate_canonical_congruence_equation_atom_model_closed=true
crt_coordinate_canonical_congruence_equation_normal_form_closed=true
crt_coordinate_canonical_congruence_equation_id_stability_closed=true
crt_coordinate_canonical_congruence_equation_quota_debt_allocation_closed=true
crt_coordinate_canonical_congruence_equation_atom_pigeonhole_closed=true
crt_coordinate_canonical_congruence_equation_atom_imbalance_packet_registered=true
anonymous_crt_coordinate_atom_imbalance_removed=true
endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_cap_pdec_cap_proved=false
crt_coordinate_canonical_congruence_equation_atom_imbalance_pdec_cap_proved=false
row_column_unconditional_closed=false
```

CRT-coordinate-atom imbalance 已给出：

```text
C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi}>d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi}
```

把该 coordinate atom 内部可能的同一同余方程多表示归一到有限 canonical congruence equation
atom `epsilon`：

```text
epsilon=(equation_id,normal_form,row,column,carrier_prime q,residue a,endpoint_side,orientation,phase_boundary_key)
C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi}=sum_epsilon C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon}
d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi}=sum_epsilon d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon}
```

如果每个 canonical equation atom 都满足
`C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon}<=d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon}`，
则该 CRT coordinate atom 不可能超额；所以必有某个 `epsilon` 满足
`C_{...,chi,epsilon}>d_{...,chi,epsilon}`。source-atom multiplicity-cap PDEC/cap
不在本步证明，继续作为并行出口。该 equation atom 若由 singleton、full-cycle mean、bridge、
amplitude-depth、boundary flux 或 sparse SAE 支付，则回流已有出口；否则留下实际
canonical-congruence-equation atom imbalance PDEC/cap。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、canonical-congruence-equation atom imbalance PDEC/cap、
bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux
PDEC/cap 或 sparse SAE 求和；它只把匿名 CRT-coordinate-atom imbalance 压成
canonical equation imbalance 包或 mean/singleton/sparse/三出口。

### 1.91 stable-ladder canonical-equation phase-residue-evaluation 更新

新增机器证书：

```text
experiments/prime_matrix_canonical_equation_phase_residue_evaluation_router.py
data/prime-matrix-canonical-equation-phase-residue-evaluation-ledger.json
docs/monograph/prime-matrix-canonical-equation-phase-residue-evaluation-router.md
docs/monograph/prime-matrix-canonical-equation-phase-residue-evaluation-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
canonical_congruence_equation_atom_imbalance_imported=true
source_atom_multiplicity_cap_carried_forward=true
canonical_equation_phase_residue_evaluation_atom_model_closed=true
canonical_equation_row_phase_closed=true
canonical_equation_column_phase_closed=true
canonical_equation_carrier_residue_evaluation_closed=true
canonical_equation_phase_residue_evaluation_id_stability_closed=true
canonical_equation_phase_residue_evaluation_quota_debt_allocation_closed=true
canonical_equation_phase_residue_evaluation_atom_pigeonhole_closed=true
canonical_equation_phase_residue_evaluation_atom_imbalance_packet_registered=true
anonymous_canonical_congruence_equation_atom_imbalance_removed=true
phase_residue_evaluation_atom_imbalance_pdec_cap_proved=false
row_column_unconditional_closed=false
```

canonical-congruence-equation atom imbalance 已给出：

```text
C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon}>d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon}
```

把该 equation atom 内部的实际 CRT 相位评价固定为有限 phase-residue evaluation atom `zeta`：

```text
zeta=(evaluation_id,equation_id,q,a,row mod q,column mod q,N_{row,column,side} mod q,endpoint_side,orientation,phase_boundary_key)
C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon}=sum_zeta C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon,zeta}
d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon}=sum_zeta d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon,zeta}
```

如果每个 phase-residue evaluation atom 都满足
`C_{...,epsilon,zeta}<=d_{...,epsilon,zeta}`，则该 canonical equation atom 不可能超额；
所以必有某个 `zeta` 满足 `C_{...,epsilon,zeta}>d_{...,epsilon,zeta}`。source-atom
multiplicity-cap PDEC/cap 不在本步证明，继续作为并行出口。该 phase-residue atom 若由
singleton、full-cycle mean、bridge、amplitude-depth、boundary flux 或 sparse SAE 支付，
则回流已有出口；否则留下实际 phase-residue-evaluation atom imbalance PDEC/cap。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue-evaluation atom imbalance PDEC/cap、
bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux
PDEC/cap 或 sparse SAE 求和；它只把匿名 canonical equation atom imbalance 压成
phase-residue-evaluation imbalance 包或 mean/singleton/sparse/三出口。

### 1.92 stable-ladder phase-residue Hall-defect 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_hall_defect_router.py
data/prime-matrix-phase-residue-hall-defect-ledger.json
docs/monograph/prime-matrix-phase-residue-hall-defect-router.md
docs/monograph/prime-matrix-phase-residue-hall-defect-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_evaluation_atom_imbalance_imported=true
phase_residue_load_token_ledger_closed=true
phase_residue_quota_debt_slot_ledger_closed=true
phase_residue_payment_graph_closed=true
phase_residue_hall_defect_normal_form_closed=true
phase_residue_hall_defect_pigeonhole_closed=true
phase_residue_hall_defect_packet_registered=true
phase_residue_hall_defect_pdec_cap_proved=false
row_column_unconditional_closed=false
```

phase-residue-evaluation atom imbalance 已给出：

```text
C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon,zeta}>d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon,zeta}
```

把该 atom 内部负载展开为 load tokens `L_zeta`，把 quota/cancellation debt 展开为 slots
`D_zeta`，并只在同一 `evaluation_id`、同 side/orientation 纪律且不跨 boundary 的
token-slot 之间连边：

```text
G_zeta=(L_zeta,D_zeta,E_zeta)
C_{...,zeta}=|L_zeta|, d_{...,zeta}=|D_zeta|
C_{...,zeta}>d_{...,zeta} => exists S subset L_zeta with |S|>|N_G(S)|
Delta_H(S)=|S|-|N_G(S)|>0
```

如果不存在 Hall 缺陷子集，则 Hall 定理给出从全部负载 token 到支付 slot 的注入匹配，
从而 `C_{...,zeta}<=d_{...,zeta}`，与输入超额矛盾。因此 phase-residue 超额必须显形为
供需匹配缺陷，或回流 singleton、full-cycle mean、bridge、amplitude-depth、boundary flux
或 sparse SAE 出口；否则留下实际 phase-residue Hall-defect PDEC/cap。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomHallDefectPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue Hall-defect PDEC/cap、bridge-cancellation
PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap 或 sparse SAE
求和；它只把匿名 phase-residue C>d 压成 Hall 供需缺陷包或 mean/singleton/sparse/三出口。

### 1.93 stable-ladder phase-residue critical-Hall-cut 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_critical_hall_cut_router.py
data/prime-matrix-phase-residue-critical-hall-cut-ledger.json
docs/monograph/prime-matrix-phase-residue-critical-hall-cut-router.md
docs/monograph/prime-matrix-phase-residue-critical-hall-cut-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomHallDefectPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_hall_defect_imported=true
phase_residue_hall_defect_finite_family_closed=true
phase_residue_hall_defect_minimal_choice_closed=true
phase_residue_hall_defect_connected_core_closed=true
phase_residue_hall_defect_proper_subset_hall_ok_closed=true
phase_residue_critical_hall_cut_boundary_closed=true
phase_residue_critical_hall_cut_margin_closed=true
phase_residue_critical_hall_cut_pdec_cap_proved=false
row_column_unconditional_closed=false
```

phase-residue Hall defect 给出非空有限缺陷族：

```text
F={S subset L_zeta: |S|>|N_G(S)|}
```

在 `F` 中按 `(|S|,-Delta_H(S),stable_hash(S))` 选取规范临界子集：

```text
S_*=argmin_{S in F} (|S|,-Delta_H(S),stable_hash(S))
B_*=N_G(S_*)
Delta_*=|S_*|-|B_*|>0
for every proper T subset S_*: |T|<=|N_G(T)|
```

若 `S_*` 可分解为互不相连分量，则至少一个分量仍有正缺陷，违背最小性；所以可取连通
critical core。于是剩余缺口不再是任意 Hall 失败，而是边界 `B_*` 明确、真子集 Hall 正常、
缺陷量 `Delta_*` 不可再分的 phase-residue critical-Hall-cut PDEC/cap。已有出口若支付则回流；
否则留下该 critical cut。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomCriticalHallCutPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue critical-Hall-cut PDEC/cap、bridge-cancellation
PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap 或 sparse SAE
求和；它只把任意 Hall defect 压成 critical cut 包或 mean/singleton/sparse/三出口。

### 1.94 stable-ladder phase-residue unit-defect critical-cut 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_unit_defect_critical_cut_router.py
data/prime-matrix-phase-residue-unit-defect-critical-cut-ledger.json
docs/monograph/prime-matrix-phase-residue-unit-defect-critical-cut-router.md
docs/monograph/prime-matrix-phase-residue-unit-defect-critical-cut-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomCriticalHallCutPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_critical_hall_cut_imported=true
phase_residue_critical_hall_cut_proper_subset_hall_ok_imported=true
phase_residue_critical_hall_cut_unit_margin_closed=true
phase_residue_critical_hall_cut_single_deletion_boundary_saturation_closed=true
multi_unit_phase_residue_critical_hall_cut_defect_excluded=true
phase_residue_unit_defect_critical_hall_cut_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层给出 critical cut：

```text
B_*=N_G(S_*)
Delta_*=|S_*|-|B_*|>0
for every proper T subset S_*: |T|<=|N_G(T)|
```

若 `|S_*|=1`，正缺陷强制 `B_*=empty` 且 `Delta_*=1`。若 `|S_*|>=2`，任取
`s in S_*`，由真子集 Hall 正常与邻域单调性得到：

```text
|S_*|-1 <= |N_G(S_*\{s})| <= |B_*| = |S_*|-Delta_*
```

因此 `Delta_*<=1`；又 `Delta_*>0` 为整数，所以 `Delta_*=1`。同时
`N_G(S_*\{s}) subset B_*` 且基数相等，故：

```text
for every s in S_*: N_G(S_*\{s})=B_*
```

这关闭了 critical cut 内部的多单位容量缺口口径：反例若还存在，不能靠一个大 Hall 缺陷隐藏，
只能表现为单位缺口 critical-Hall-cut，且其边界在删除任一源点后仍完整保留。已有出口若支付则回流；
否则留下实际 unit-defect critical-Hall-cut PDEC/cap。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomUnitDefectCriticalHallCutPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue unit-defect critical-Hall-cut PDEC/cap、
bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap
或 sparse SAE 求和；它只把 critical cut 的容量缺口压成单位缺口或 mean/singleton/sparse/三出口。

### 1.95 stable-ladder phase-residue near-perfect matching circuit 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_near_perfect_matching_circuit_router.py
data/prime-matrix-phase-residue-near-perfect-matching-circuit-ledger.json
docs/monograph/prime-matrix-phase-residue-near-perfect-matching-circuit-router.md
docs/monograph/prime-matrix-phase-residue-near-perfect-matching-circuit-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomUnitDefectCriticalHallCutPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_unit_defect_critical_hall_cut_imported=true
phase_residue_every_single_deletion_hall_ok_closed=true
phase_residue_every_single_deletion_perfect_matching_closed=true
phase_residue_critical_cut_maximum_matching_size_closed=true
phase_residue_boundary_double_cover_closed=true
phase_residue_near_perfect_matching_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层给出：

```text
|S_*|=|B_*|+1
N_G(S_*\{s})=B_* for every s in S_*
for every proper T subset S_*: |T|<=|N_G(T)|
```

任取 `s in S_*`。对任意 `U subset S_*\{s}`，`U` 仍是 `S_*` 的真子集，所以满足 Hall。
又 `|S_*\{s}|=|B_*|`，因此由 Hall 定理得到：

```text
for every s in S_*: exists perfect matching M_s:S_*\{s}->B_*
```

于是整体最大匹配大小正好是 `|B_*|=|S_*|-1`，且每个源点都可作为唯一未匹配源点。
此外若某个 `b in B_*` 只邻接唯一源点 `s`，删除 `s` 后无法覆盖 `b`，矛盾；所以每个边界槽
至少由两个源点支撑。反例链剩余不再是任意单位缺口 cut，而是 near-perfect matching circuit。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomNearPerfectMatchingCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue near-perfect matching circuit PDEC/cap、
bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap
或 sparse SAE 求和；它只把单位缺口 cut 压成近完美匹配 circuit 或 mean/singleton/sparse/三出口。

### 1.96 stable-ladder phase-residue alternating exchange circuit 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_alternating_exchange_circuit_router.py
data/prime-matrix-phase-residue-alternating-exchange-circuit-ledger.json
docs/monograph/prime-matrix-phase-residue-alternating-exchange-circuit-router.md
docs/monograph/prime-matrix-phase-residue-alternating-exchange-circuit-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomNearPerfectMatchingCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_near_perfect_matching_circuit_imported=true
phase_residue_matching_symmetric_difference_graph_closed=true
phase_residue_unique_source_defect_alternating_path_closed=true
phase_residue_every_source_exchange_reachable_closed=true
phase_residue_alternating_exchange_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层给出对每个 `s in S_*` 的完美删除匹配：

```text
M_s:S_*\{s}->B_*
```

任选基准缺失源点 `s0`，令 `M0=M_{s0}`。对任意 `s!=s0`，考察对称差
`H_s=M0 Δ M_s`。由于 `M0` 与 `M_s` 都覆盖全部 `B_*`，每个边界槽在 `H_s` 中度数为
`0` 或 `2`；源点侧除 `s` 与 `s0` 外度数为 `0` 或 `2`，而 `s` 与 `s0` 度数为 `1`。
因此 `H_s` 分解为若干交替偶圈加一条端点为 `s` 与 `s0` 的交替开路径。

这把剩余反例从“近完美匹配缺口”压成“所有源点都能交换到同一基准缺失源点”的
alternating exchange circuit。新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomAlternatingExchangeCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue alternating exchange circuit PDEC/cap、
bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap
或 sparse SAE 求和；它只把近完美匹配 circuit 压成交替交换 circuit 或 mean/singleton/sparse/三出口。

### 1.97 stable-ladder phase-residue rooted directed exchange path 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_rooted_directed_exchange_path_router.py
data/prime-matrix-phase-residue-rooted-directed-exchange-path-ledger.json
docs/monograph/prime-matrix-phase-residue-rooted-directed-exchange-path-router.md
docs/monograph/prime-matrix-phase-residue-rooted-directed-exchange-path-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomAlternatingExchangeCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_alternating_exchange_circuit_imported=true
phase_residue_exchange_path_m0_ms_edge_coloring_closed=true
phase_residue_exchange_path_root_orientation_closed=true
phase_residue_every_source_root_reachable_by_directed_exchange_closed=true
phase_residue_rooted_directed_exchange_path_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层给出基准缺失源点 `s0`、基准匹配 `M0=M_{s0}`，以及每个 `s!=s0` 的交替路径 `P_s`。
本步给 `P_s` 上的边加上来源色：

```text
M0-only, M_s-only
```

并按规则定向：

```text
M0-only: source -> boundary
M_s-only: boundary -> source
```

于是每条路径都成为从 `s` 到 `s0` 的根向有向交替路径。沿 `P_s` 做对称差切换会把
`M0` 在路径分量上的边替换为 `M_s` 的边，从而给出缺失源点状态之间的显式转移规则。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomRootedDirectedExchangePathCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue rooted directed exchange path circuit PDEC/cap、
bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap
或 sparse SAE 求和；它只把交替交换 circuit 压成根向有向交换路径 circuit 或 mean/singleton/sparse/三出口。

### 1.98 stable-ladder phase-residue exchange toggle word 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_toggle_word_router.py
data/prime-matrix-phase-residue-exchange-toggle-word-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-toggle-word-router.md
docs/monograph/prime-matrix-phase-residue-exchange-toggle-word-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomRootedDirectedExchangePathCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_rooted_directed_exchange_path_imported=true
phase_residue_alternating_vertex_word_normal_form_closed=true
phase_residue_exchange_word_boundary_distinctness_closed=true
phase_residue_no_internal_boundary_reuse_in_toggle_word_closed=true
phase_residue_exchange_toggle_word_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层给出每个 `s` 到基准缺失源点 `s0` 的简单根向有向交替路径。本步把路径写成有限词

```text
P_s=(u_0=s,b_1,u_1,...,b_r,u_r=s0)
```

简单性给出词内源点 `u_i` 两两不同，边界槽 `b_i` 两两不同。每个二步片段
`u_{i-1}->b_i->u_i` 是一个局部 pivot，把 `M0` 边 `(u_{i-1},b_i)` 替换为 `M_s`
边 `(u_i,b_i)`；整条路径切换就是这些局部 pivot 的有序有限乘积。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeToggleWordCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange toggle word circuit PDEC/cap、
bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap
或 sparse SAE 求和；它只把根向有向交换路径 circuit 压成 exchange toggle word circuit
或 mean/singleton/sparse/三出口。

### 1.99 stable-ladder phase-residue exchange prefix defect ladder 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_prefix_defect_ladder_router.py
data/prime-matrix-phase-residue-exchange-prefix-defect-ladder-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-prefix-defect-ladder-router.md
docs/monograph/prime-matrix-phase-residue-exchange-prefix-defect-ladder-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeToggleWordCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_toggle_word_imported=true
phase_residue_exchange_prefix_unit_defect_identity_closed=true
phase_residue_exchange_prefix_nested_ladder_closed=true
phase_residue_exchange_prefix_toggle_state_transport_closed=true
phase_residue_exchange_prefix_defect_ladder_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层给出交替切换词

```text
P_s=(u_0=s,b_1,u_1,...,b_r,u_r=s0)
```

本步对每个 `1<=t<=r` 定义：

```text
U_t={u_0,...,u_t},  B_t={b_1,...,b_t}.
```

由于词内源点与边界槽分别互异，`|U_t|=t+1`、`|B_t|=t`，所以每个非空前缀都有精确单位缺口
`|U_t|-|B_t|=1`。这些前缀随 `t` 嵌套增长，每步只新增一个源点和一个边界槽；前缀 pivot 的有序乘积把缺失源状态从 `u_0` 输运到 `u_t`。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangePrefixDefectLadderCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange prefix defect ladder circuit PDEC/cap、
bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap
或 sparse SAE 求和；它只把 exchange toggle word circuit 压成前缀单位缺口 ladder circuit
或 mean/singleton/sparse/三出口。

### 1.100 stable-ladder phase-residue exchange endpoint telescoping charge 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_endpoint_telescoping_charge_router.py
data/prime-matrix-phase-residue-exchange-endpoint-telescoping-charge-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-endpoint-telescoping-charge-router.md
docs/monograph/prime-matrix-phase-residue-exchange-endpoint-telescoping-charge-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangePrefixDefectLadderCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_prefix_defect_ladder_imported=true
phase_residue_exchange_pivot_boundary_operator_closed=true
phase_residue_exchange_internal_source_cancellation_closed=true
phase_residue_exchange_endpoint_charge_identity_closed=true
phase_residue_exchange_endpoint_telescoping_charge_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层给出前缀单位缺口 ladder：

```text
P_s=(u_0=s,b_1,u_1,...,b_r,u_r=s0).
```

本步把每个局部 pivot 的源侧边界写成：

```text
d_i=[u_i]-[u_{i-1}].
```

于是内部源点 `u_i` 在 `d_i` 中以正号出现，又在 `d_{i+1}` 中以负号出现，求和后相消：

```text
sum_{i=1}^r d_i=[u_r]-[u_0]=[s0]-[s].
```

任意前缀也满足 `sum_{i=1}^t d_i=[u_t]-[u_0]`，与前缀切换输运一致。未命名净债不能留在内部源点，只能回流已有出口或压到端点望远镜电荷。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeEndpointTelescopingChargeCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange endpoint telescoping charge circuit PDEC/cap、
bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap
或 sparse SAE 求和；它只把 exchange prefix defect ladder circuit 压成端点望远镜电荷 circuit
或 mean/singleton/sparse/三出口。

### 1.101 stable-ladder phase-residue exchange root-star charge 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_root_star_charge_router.py
data/prime-matrix-phase-residue-exchange-root-star-charge-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-root-star-charge-router.md
docs/monograph/prime-matrix-phase-residue-exchange-root-star-charge-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeEndpointTelescopingChargeCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_endpoint_telescoping_charge_imported=true
phase_residue_exchange_common_root_endpoint_closed=true
phase_residue_exchange_root_charge_multiplicity_closed=true
phase_residue_exchange_root_star_total_charge_zero_closed=true
phase_residue_exchange_root_star_charge_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层把每条交换路径压成端点电荷：

```text
c_s=[s0]-[s].
```

由于所有路径共用同一根点 `s0`，聚合所有 `s!=s0` 得到根星电荷场：

```text
C=sum_{s!=s0} c_s=(|S|-1)[s0]-sum_{s!=s0}[s].
```

根点承受 `|S|-1` 个正电荷，每个非根源点只贡献一次负电荷；总系数为
`(|S|-1)-(|S|-1)=0`。本步不创造净量，只把匿名端点压力固定成唯一根星入射场。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeRootStarChargeCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange root-star charge circuit PDEC/cap、
bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap
或 sparse SAE 求和；它只把 endpoint telescoping charge circuit 压成根星电荷 circuit
或 mean/singleton/sparse/三出口。

### 1.102 stable-ladder phase-residue exchange normalized root-mean dipole 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_normalized_root_mean_dipole_router.py
data/prime-matrix-phase-residue-exchange-normalized-root-mean-dipole-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-normalized-root-mean-dipole-router.md
docs/monograph/prime-matrix-phase-residue-exchange-normalized-root-mean-dipole-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeRootStarChargeCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_root_star_charge_imported=true
phase_residue_exchange_root_mean_normalization_closed=true
phase_residue_exchange_nonroot_mean_measure_closed=true
phase_residue_exchange_normalized_root_mean_dipole_zero_mean_closed=true
phase_residue_exchange_normalized_root_mean_dipole_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层把所有端点压力固定成根星电荷：

```text
C=(|S|-1)[s0]-sum_{s!=s0}[s].
```

当 `|S|>1` 时除以 `|S|-1`，得到非根均值
`mu=(1/(|S|-1))sum_{s!=s0}[s]` 以及归一化偶极：

```text
D=[s0]-mu=[s0]-(1/(|S|-1))sum_{s!=s0}[s].
```

于是 `C=(|S|-1)D`，且 `D` 的总系数为 `1-(|S|-1)/(|S|-1)=0`。
`|S|=1` 的退化情形归入 singleton atom/SAE 出口。本步去掉根点重数放大口径，
把剩余压力压成“根点相对非根均值”的零均值偏差。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeNormalizedRootMeanDipoleCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange normalized root-mean dipole circuit
PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux
PDEC/cap 或 sparse SAE 求和；它只把 root-star charge circuit 压成 normalized
root-mean dipole circuit 或 mean/singleton/sparse/三出口。

### 1.103 stable-ladder phase-residue exchange root-source pair-average contrast 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_root_source_pair_average_contrast_router.py
data/prime-matrix-phase-residue-exchange-root-source-pair-average-contrast-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-root-source-pair-average-contrast-router.md
docs/monograph/prime-matrix-phase-residue-exchange-root-source-pair-average-contrast-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeNormalizedRootMeanDipoleCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_normalized_root_mean_dipole_imported=true
phase_residue_exchange_root_source_pair_fan_closed=true
phase_residue_exchange_uniform_pair_weight_closed=true
phase_residue_exchange_pair_average_contrast_identity_closed=true
phase_residue_exchange_root_source_pair_average_contrast_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层把剩余压力固定为归一化偶极：

```text
D=[s0]-(1/(|S|-1))sum_{s!=s0}[s].
```

当 `|S|>1` 时，对每个非根源点定义成对对比 `e_s=[s0]-[s]`。于是有精确恒等式：

```text
D=(1/(|S|-1))sum_{s!=s0} e_s
 =(1/(|S|-1))sum_{s!=s0}([s0]-[s]).
```

每个 `e_s` 都是一个根点正单位和一个源点负单位的零均值单位对比，权重固定为
`1/(|S|-1)`。因此非根均值云不再匿名，剩余压力被压成 root-source pair fan 的均匀平均。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeRootSourcePairAverageContrastCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange root-source pair-average contrast
circuit PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；它只把 normalized root-mean
dipole circuit 压成 root-source pair-average contrast circuit 或 mean/singleton/sparse/三出口。

### 1.104 stable-ladder phase-residue exchange root-source pair witness localization 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_root_source_pair_witness_localization_router.py
data/prime-matrix-phase-residue-exchange-root-source-pair-witness-localization-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-root-source-pair-witness-localization-router.md
docs/monograph/prime-matrix-phase-residue-exchange-root-source-pair-witness-localization-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeRootSourcePairAverageContrastCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_root_source_pair_average_contrast_imported=true
phase_residue_exchange_pair_witness_mean_identity_closed=true
phase_residue_exchange_average_to_single_pair_max_localization_closed=true
phase_residue_exchange_named_single_pair_witness_closed=true
phase_residue_exchange_root_source_pair_witness_localization_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层把剩余压力固定为成对均匀平均：

```text
D=(1/(|S|-1))sum_{s!=s0} e_s,  e_s=[s0]-[s].
```

对任意导入的线性相位/容量见证 `Lambda`，定义 `a_s=Lambda(e_s)`。线性性给出：

```text
Lambda(D)=(1/(|S|-1))sum_{s!=s0} a_s.
```

令 `sigma=sign(Lambda(D))`。若平均见证非零，则有限平均不可能大于所有单项：

```text
max_{s!=s0} sigma*a_s >= sigma*Lambda(D)=|Lambda(D)|.
```

因此平均见证不能只由匿名整体承载；它可以定位到一个命名 root-source pair。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeRootSourcePairWitnessLocalizationCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange root-source pair witness localization
circuit PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；也没有证明线性见证本身存在。
它只把 root-source pair-average contrast circuit 压成单对见证定位 circuit
或 mean/singleton/sparse/三出口。

### 1.105 stable-ladder phase-residue exchange oriented root-source witness gap 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_oriented_root_source_witness_gap_router.py
data/prime-matrix-phase-residue-exchange-oriented-root-source-witness-gap-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-oriented-root-source-witness-gap-router.md
docs/monograph/prime-matrix-phase-residue-exchange-oriented-root-source-witness-gap-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeRootSourcePairWitnessLocalizationCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_root_source_pair_witness_localization_imported=true
phase_residue_exchange_named_root_source_pair_closed=true
phase_residue_exchange_oriented_witness_gap_coordinate_closed=true
phase_residue_exchange_witness_gap_lower_bound_closed=true
linear_witness_existence_proved=false
phase_residue_exchange_oriented_root_source_witness_gap_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层给出命名单对 `s*` 与定向符号 `sigma`，满足：

```text
sigma*Lambda([s0]-[s*]) >= |Lambda(D)|.
```

本步登记两个端点分数：

```text
R=sigma*Lambda([s0])
T=sigma*Lambda([s*])
```

由线性性得到：

```text
G=R-T=sigma*Lambda([s0]-[s*]) >= |Lambda(D)|.
```

因此单对见证不再以匿名 pair-localization 形式保留；剩余压力被压成根端分数超过源端分数的
oriented root-source witness gap 坐标。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeOrientedRootSourceWitnessGapCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange oriented root-source witness gap
circuit PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；也没有证明线性见证本身存在。
它只把 root-source pair witness localization circuit 压成有向两端点差值坐标
或 mean/singleton/sparse/三出口。

### 1.106 stable-ladder phase-residue exchange centered root-source score dipole 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_centered_root_source_score_dipole_router.py
data/prime-matrix-phase-residue-exchange-centered-root-source-score-dipole-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-centered-root-source-score-dipole-router.md
docs/monograph/prime-matrix-phase-residue-exchange-centered-root-source-score-dipole-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeOrientedRootSourceWitnessGapCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_oriented_root_source_witness_gap_imported=true
phase_residue_exchange_witness_score_midpoint_closed=true
phase_residue_exchange_root_source_score_centering_closed=true
phase_residue_exchange_centered_two_point_score_zero_mean_closed=true
phase_residue_exchange_centered_half_gap_lower_bound_closed=true
linear_witness_existence_proved=false
phase_residue_exchange_centered_root_source_score_dipole_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层给出：

```text
R=sigma*Lambda([s0])
T=sigma*Lambda([s*])
G=R-T>=|Lambda(D)|.
```

本步取共同中点：

```text
M=(R+T)/2.
```

于是：

```text
R=M+G/2
T=M-G/2
U=R-M=G/2
V=T-M=-G/2
U+V=0
U>=|Lambda(D)|/2.
```

因此 oriented gap 中的公共分数偏移不再匿名保留；剩余压力被压成零均值的
centered root-source score dipole。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeCenteredRootSourceScoreDipoleCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange centered root-source score dipole
circuit PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；也没有证明线性见证本身存在。
它只把 oriented root-source witness gap circuit 压成中心化两点 score dipole
或 mean/singleton/sparse/三出口。

### 1.107 stable-ladder phase-residue exchange signed root-source half-gap atom 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_signed_root_source_half_gap_atom_router.py
data/prime-matrix-phase-residue-exchange-signed-root-source-half-gap-atom-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-signed-root-source-half-gap-atom-router.md
docs/monograph/prime-matrix-phase-residue-exchange-signed-root-source-half-gap-atom-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeCenteredRootSourceScoreDipoleCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_centered_root_source_score_dipole_imported=true
phase_residue_exchange_half_gap_amplitude_closed=true
phase_residue_exchange_half_gap_amplitude_lower_bound_closed=true
phase_residue_exchange_root_positive_source_negative_support_closed=true
phase_residue_exchange_signed_half_gap_atom_factorization_closed=true
phase_residue_exchange_signed_half_gap_atom_zero_mass_closed=true
phase_residue_exchange_signed_half_gap_atom_total_variation_closed=true
linear_witness_existence_proved=false
phase_residue_exchange_signed_root_source_half_gap_atom_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层给出：

```text
U=G/2
V=-G/2
U+V=0
G>=|Lambda(D)|.
```

本步定义半 gap 正幅度：

```text
A=G/2=U=-V.
```

于是中心化两点分数无损因式分解为：

```text
W=A([s0]-[s*])
mass(W)=0
TV(W)=2A=G
A>=|Lambda(D)|/2.
```

因此 centered score dipole 中的不等幅端点表述不再匿名保留；剩余压力被压成一个正幅度乘固定
root-positive/source-negative 符号原子。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeSignedRootSourceHalfGapAtomCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange signed root-source half-gap atom
circuit PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；也没有证明线性见证本身存在。
它只把 centered root-source score dipole circuit 压成 signed half-gap atom
或 mean/singleton/sparse/三出口。

### 1.108 stable-ladder phase-residue exchange oriented root-source transport edge 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_oriented_root_source_transport_edge_router.py
data/prime-matrix-phase-residue-exchange-oriented-root-source-transport-edge-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-oriented-root-source-transport-edge-router.md
docs/monograph/prime-matrix-phase-residue-exchange-oriented-root-source-transport-edge-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeSignedRootSourceHalfGapAtomCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_signed_root_source_half_gap_atom_imported=true
phase_residue_exchange_transport_edge_orientation_closed=true
phase_residue_exchange_transport_edge_flux_closed=true
phase_residue_exchange_transport_edge_boundary_identity_closed=true
phase_residue_exchange_transport_edge_divergence_closed=true
phase_residue_exchange_transport_edge_mass_conservation_closed=true
phase_residue_exchange_transport_edge_flux_lower_bound_closed=true
linear_witness_existence_proved=false
phase_residue_exchange_oriented_root_source_transport_edge_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层给出：

```text
W=A([s0]-[s*])
A>=|Lambda(D)|/2
mass(W)=0.
```

本步把它改写成一条 source-to-root 输运边：

```text
e=s* -> s0
F=A
partial(F e)=A([s0]-[s*])=W
div(s0)=+A
div(s*)=-A
div(s0)+div(s*)=0.
```

因此 signed half-gap atom 不再只是符号测度口径；剩余压力被压成一条命名的有向守恒输运边。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeOrientedRootSourceTransportEdgeCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange oriented root-source transport edge
circuit PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；也没有证明线性见证本身存在。
它只把 signed root-source half-gap atom circuit 压成有向输运边
或 mean/singleton/sparse/三出口。

### 1.109 stable-ladder phase-residue exchange transport-edge incidence column 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_transport_edge_incidence_column_router.py
data/prime-matrix-phase-residue-exchange-transport-edge-incidence-column-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-transport-edge-incidence-column-router.md
docs/monograph/prime-matrix-phase-residue-exchange-transport-edge-incidence-column-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeOrientedRootSourceTransportEdgeCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_oriented_root_source_transport_edge_imported=true
phase_residue_exchange_transport_edge_tail_head_coordinate_closed=true
phase_residue_exchange_transport_edge_incidence_vector_closed=true
phase_residue_exchange_transport_edge_boundary_matrix_column_closed=true
phase_residue_exchange_transport_edge_flux_coordinate_closed=true
phase_residue_exchange_transport_edge_matrix_boundary_identity_closed=true
phase_residue_exchange_transport_edge_incidence_column_zero_sum_closed=true
phase_residue_no_hidden_cycle_inside_single_incidence_column_closed=true
linear_witness_existence_proved=false
phase_residue_exchange_transport_edge_incidence_column_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层给出：

```text
e=s* -> s0
F=A
partial(F e)=A([s0]-[s*])=W.
```

本步把它坐标化为单列边界矩阵：

```text
tail(e)=s*
head(e)=s0
b_e=[s0]-[s*]
B[:,e]=b_e
f_e=A
Bf=A b_e=A([s0]-[s*])=W.
```

因此有向输运边不再只是边对象口径；剩余压力被压成一列命名 incidence column，
列和为零，非退化时只在 root/source 两端有非零坐标。单列对象没有内部路径可藏，
循环性只能进入命名 transport-edge incidence-column PDEC/cap 出口。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeTransportEdgeIncidenceColumnCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange transport-edge incidence-column
circuit PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；也没有证明线性见证本身存在。
它只把有向输运边 circuit 压成单列 incidence 坐标
或 mean/singleton/sparse/三出口。

### 1.110 stable-ladder phase-residue exchange incidence-column Kronecker stencil 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_incidence_column_kronecker_stencil_router.py
data/prime-matrix-phase-residue-exchange-incidence-column-kronecker-stencil-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-incidence-column-kronecker-stencil-router.md
docs/monograph/prime-matrix-phase-residue-exchange-incidence-column-kronecker-stencil-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeTransportEdgeIncidenceColumnCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_transport_edge_incidence_column_imported=true
phase_residue_exchange_root_kronecker_delta_coordinate_closed=true
phase_residue_exchange_source_kronecker_delta_coordinate_closed=true
phase_residue_exchange_kronecker_delta_difference_stencil_closed=true
phase_residue_exchange_kronecker_stencil_signed_coefficient_closed=true
phase_residue_exchange_kronecker_stencil_endpoint_crt_coordinate_closed=true
phase_residue_exchange_incidence_column_equals_kronecker_stencil_closed=true
phase_residue_exchange_kronecker_stencil_flux_scaling_closed=true
linear_witness_existence_proved=false
phase_residue_exchange_incidence_column_kronecker_stencil_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层给出：

```text
b_e=[s0]-[s*]
B[:,e]=b_e
f_e=A
Bf=A b_e=W.
```

本步删除矩阵列抽象，改写为端点单位坐标模板：

```text
delta_{s0}(v)=1 if v=s0, else 0
delta_{s*}(v)=1 if v=s*, else 0
k=delta_{s0}-delta_{s*}
b_e=k
A k=A(delta_{s0}-delta_{s*})=W.
```

两个端点继承上游 primitive witness CRT coordinate atom 的 residue word：

```text
root_crt_word=crt(s0)
source_crt_word=crt(s*)
stencil=(+1 at root_crt_word)+(-1 at source_crt_word).
```

因此 incidence column 不再是匿名 boundary-matrix column；剩余压力被压成两个命名 CRT
端点单位坐标的符号差。若 `s0=s*`，模板为零并回流 singleton/degenerate 出口；否则
保留两点 Kronecker signed stencil。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeIncidenceColumnKroneckerStencilCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange incidence-column Kronecker-stencil
circuit PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；也没有证明线性见证本身存在。
它只把 incidence column circuit 压成 Kronecker endpoint stencil
或 mean/singleton/sparse/三出口。

### 1.111 stable-ladder phase-residue exchange Kronecker-stencil signed CRT pair 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_kronecker_stencil_signed_crt_pair_router.py
data/prime-matrix-phase-residue-exchange-kronecker-stencil-signed-crt-pair-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-kronecker-stencil-signed-crt-pair-router.md
docs/monograph/prime-matrix-phase-residue-exchange-kronecker-stencil-signed-crt-pair-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeIncidenceColumnKroneckerStencilCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_incidence_column_kronecker_stencil_imported=true
phase_residue_exchange_root_crt_word_coordinate_closed=true
phase_residue_exchange_source_crt_word_coordinate_closed=true
phase_residue_exchange_root_canonical_congruence_equation_closed=true
phase_residue_exchange_source_canonical_congruence_equation_closed=true
phase_residue_exchange_ordered_root_source_crt_word_pair_closed=true
phase_residue_exchange_signed_crt_word_pair_support_dictionary_closed=true
phase_residue_exchange_signed_crt_pair_equals_kronecker_stencil_closed=true
phase_residue_exchange_signed_crt_pair_flux_scaling_closed=true
linear_witness_existence_proved=false
phase_residue_exchange_kronecker_stencil_signed_crt_pair_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层给出：

```text
k=delta_{s0}-delta_{s*}
A k=W
root_crt_word=crt(s0)
source_crt_word=crt(s*).
```

本步删除 delta 函数模板，改写为显式 CRT word 有序对：

```text
r0=crt(s0)
r*=crt(s*)
Pi=(r0,r*)
s0 == r0_i mod p_i  for every active prime coordinate p_i
s* == r*_i mod p_i  for every active prime coordinate p_i.
```

并把 stencil 写成有限 signed support dictionary：

```text
C_Pi(r0)=+1
C_Pi(r*)=-1
C_Pi(r)=0 for all other CRT words
A C_Pi=W.
```

因此 Kronecker stencil 不再是匿名 delta 函数模板；剩余压力被压成两个命名 CRT words 的
有序 signed dictionary。若 `r0=r*`，字典消去并回流 singleton/degenerate 出口；否则
保留两词 signed CRT pair。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeKroneckerStencilSignedCRTPairCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange Kronecker-stencil signed CRT pair
circuit PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；也没有证明线性见证本身存在。
它只把 Kronecker stencil circuit 压成 signed CRT word pair
或 mean/singleton/sparse/三出口。

### 1.112 stable-ladder phase-residue exchange signed CRT pair primitive atom 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_signed_crt_pair_primitive_atom_router.py
data/prime-matrix-phase-residue-exchange-signed-crt-pair-primitive-atom-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-signed-crt-pair-primitive-atom-router.md
docs/monograph/prime-matrix-phase-residue-exchange-signed-crt-pair-primitive-atom-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeKroneckerStencilSignedCRTPairCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_kronecker_stencil_signed_crt_pair_imported=true
phase_residue_exchange_signed_pair_support_size_closed=true
phase_residue_exchange_signed_pair_positive_negative_atom_closed=true
phase_residue_exchange_signed_pair_coefficient_balance_closed=true
phase_residue_exchange_signed_pair_total_variation_closed=true
phase_residue_exchange_signed_pair_flux_weight_packet_closed=true
phase_residue_exchange_signed_pair_collision_or_singleton_exit_closed=true
linear_witness_existence_proved=false
phase_residue_exchange_signed_crt_pair_primitive_atom_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层给出：

```text
Pi=(r0,r*)
C_Pi(r0)=+1
C_Pi(r*)=-1
A C_Pi=W.
```

本步删除一般字典口径，把非退化对象登记为二词 signed support primitive atom：

```text
support={r0,r*}
coefficient(r0)=+1
coefficient(r*)=-1
support_size=2
coefficient_sum=0
total_variation=2
flux_weights=(+A,-A)
A C_Pi=W.
```

若 `r0=r*`，则 `+1-1=0` 并回流 singleton/degenerate 出口；否则方向保留为
source -> root。剩余压力不再是匿名 signed CRT dictionary，而是带支撑数、零质量、
总变差和通量权重的 primitive atom。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeSignedCRTPairPrimitiveAtomCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange signed CRT pair primitive atom
circuit PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；也没有证明线性见证本身存在。
它只把 signed CRT pair dictionary 压成 primitive atom
或 mean/singleton/sparse/三出口。

### 1.113 stable-ladder phase-residue exchange primitive atom endpoint charge 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_primitive_atom_endpoint_charge_router.py
data/prime-matrix-phase-residue-exchange-primitive-atom-endpoint-charge-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-primitive-atom-endpoint-charge-router.md
docs/monograph/prime-matrix-phase-residue-exchange-primitive-atom-endpoint-charge-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeSignedCRTPairPrimitiveAtomCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_signed_crt_pair_primitive_atom_imported=true
phase_residue_exchange_root_positive_endpoint_charge_closed=true
phase_residue_exchange_source_negative_endpoint_charge_closed=true
phase_residue_exchange_ordered_endpoint_charge_pair_closed=true
phase_residue_exchange_endpoint_charge_balance_closed=true
phase_residue_exchange_endpoint_positive_negative_mass_equality_closed=true
phase_residue_exchange_endpoint_absolute_flux_closed=true
phase_residue_exchange_endpoint_charge_collision_or_singleton_exit_closed=true
linear_witness_existence_proved=false
phase_residue_exchange_primitive_atom_endpoint_charge_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层给出：

```text
support={r0,r*}
coefficient(r0)=+1
coefficient(r*)=-1
flux_weights=(+A,-A)
A C_Pi=W.
```

本步删除 primitive atom 黑箱口径，把非退化对象登记为 root/source 两个端点电荷：

```text
root_charge=(r0,+A)
source_charge=(r*,-A)
ordered_charge_pair=((r0,+A),(r*,-A))
net_charge=+A-A=0
positive_mass=A
negative_mass=A
absolute_flux=2A
A C_Pi=W.
```

若 `r0=r*`，则同点 `+A-A=0` 并回流 singleton/degenerate 出口；否则方向保留为
source -> root。剩余压力不再是匿名二点 primitive atom，而是 root/source 已命名、
净电荷守恒、正负质量相等、绝对通量固定的 endpoint charge packet。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangePrimitiveAtomEndpointChargeCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange primitive atom endpoint charge
circuit PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；也没有证明线性见证本身存在。
它只把 primitive atom 压成 endpoint charge packet
或 mean/singleton/sparse/三出口。

### 1.114 stable-ladder phase-residue exchange endpoint charge Kirchhoff cell 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_endpoint_charge_kirchhoff_cell_router.py
data/prime-matrix-phase-residue-exchange-endpoint-charge-kirchhoff-cell-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-endpoint-charge-kirchhoff-cell-router.md
docs/monograph/prime-matrix-phase-residue-exchange-endpoint-charge-kirchhoff-cell-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangePrimitiveAtomEndpointChargeCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_primitive_atom_endpoint_charge_imported=true
phase_residue_exchange_endpoint_charge_local_kirchhoff_cell_closed=true
phase_residue_exchange_endpoint_charge_root_positive_divergence_closed=true
phase_residue_exchange_endpoint_charge_source_negative_divergence_closed=true
phase_residue_exchange_endpoint_charge_kirchhoff_balance_closed=true
phase_residue_exchange_endpoint_charge_positive_negative_divergence_equality_closed=true
phase_residue_exchange_endpoint_charge_boundary_variation_closed=true
phase_residue_exchange_kirchhoff_cell_collision_or_singleton_exit_closed=true
linear_witness_existence_proved=false
phase_residue_exchange_endpoint_charge_kirchhoff_cell_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层给出：

```text
root_charge=(r0,+A)
source_charge=(r*,-A)
ordered_charge_pair=((r0,+A),(r*,-A))
net_charge=+A-A=0
positive_mass=A
negative_mass=A
absolute_flux=2A
A C_Pi=W.
```

本步删除 endpoint charge 黑箱口径，把非退化对象登记为二点局部 Kirchhoff cell：

```text
K={r0,r*}
div(r0)=+A
div(r*)=-A
sum_K div=0
positive_divergence=A
negative_divergence=A
total_boundary_variation=2A
A C_Pi=W.
```

若 `r0=r*`，则同点 `+A-A=0` 并回流 singleton/degenerate 出口；否则方向保留为
source -> root。剩余压力不再是匿名 endpoint charge packet，而是 root/source 已命名、
局部散度守恒、正负散度质量相等、边界总变差固定的 Kirchhoff cell。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeEndpointChargeKirchhoffCellCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange endpoint charge Kirchhoff cell
circuit PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；也没有证明线性见证本身存在。
它只把 endpoint charge packet 压成局部 Kirchhoff cell
或 mean/singleton/sparse/三出口。

### 1.115 stable-ladder phase-residue exchange Kirchhoff cell cut-potential 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_kirchhoff_cell_cut_potential_router.py
data/prime-matrix-phase-residue-exchange-kirchhoff-cell-cut-potential-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-kirchhoff-cell-cut-potential-router.md
docs/monograph/prime-matrix-phase-residue-exchange-kirchhoff-cell-cut-potential-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeEndpointChargeKirchhoffCellCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_endpoint_charge_kirchhoff_cell_imported=true
phase_residue_exchange_kirchhoff_cell_cut_potential_support_closed=true
phase_residue_exchange_kirchhoff_cell_cut_potential_values_closed=true
phase_residue_exchange_kirchhoff_cell_cut_potential_zero_mean_closed=true
phase_residue_exchange_kirchhoff_cell_cut_potential_unit_oscillation_closed=true
phase_residue_exchange_kirchhoff_cell_cut_potential_divergence_pairing_closed=true
phase_residue_exchange_cut_potential_collision_or_singleton_exit_closed=true
linear_witness_existence_proved=false
phase_residue_exchange_endpoint_charge_kirchhoff_cell_cut_potential_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层给出：

```text
K={r0,r*}
div(r0)=+A
div(r*)=-A
sum_K div=0
positive_divergence=A
negative_divergence=A
total_boundary_variation=2A
A C_Pi=W.
```

本步删除 Kirchhoff cell 黑箱口径，把非退化对象登记为规范化 cut-potential：

```text
phi(r0)=+1/2
phi(r*)=-1/2
phi(r0)+phi(r*)=0
phi(r0)-phi(r*)=1
<div,phi>=(+A)(+1/2)+(-A)(-1/2)=A
A C_Pi=W.
```

若 `r0=r*`，则势差退化为 `0` 并回流 singleton/degenerate 出口；否则方向保留为
source -> root。剩余压力不再是匿名二点 Kirchhoff cell，而是带零均值、单位振荡和正散度配对的
cut-potential 证书。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeEndpointChargeKirchhoffCellCutPotentialCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange endpoint charge Kirchhoff cell
cut-potential circuit PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；也没有证明线性见证本身存在。
它只把局部 Kirchhoff cell 压成 cut-potential 配对证书
或 mean/singleton/sparse/三出口。

### 1.116 stable-ladder phase-residue exchange cut-potential dual-norm 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_cut_potential_dual_norm_router.py
data/prime-matrix-phase-residue-exchange-cut-potential-dual-norm-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-cut-potential-dual-norm-router.md
docs/monograph/prime-matrix-phase-residue-exchange-cut-potential-dual-norm-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeEndpointChargeKirchhoffCellCutPotentialCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_kirchhoff_cell_cut_potential_imported=true
phase_residue_exchange_cut_potential_divergence_l1_norm_closed=true
phase_residue_exchange_cut_potential_l_infinity_norm_closed=true
phase_residue_exchange_cut_potential_holder_dual_bound_closed=true
phase_residue_exchange_cut_potential_pairing_value_closed=true
phase_residue_exchange_cut_potential_dual_norm_saturation_closed=true
phase_residue_exchange_cut_potential_polar_sign_alignment_closed=true
phase_residue_exchange_dual_norm_collision_or_singleton_exit_closed=true
linear_witness_existence_proved=false
phase_residue_exchange_cut_potential_dual_norm_saturation_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层给出：

```text
phi(r0)=+1/2
phi(r*)=-1/2
phi(r0)+phi(r*)=0
phi(r0)-phi(r*)=1
<div,phi>=A
A C_Pi=W.
```

本步删除 cut-potential 黑箱口径，把非退化对象登记为 L1-Linfty 对偶范数等号饱和：

```text
||div||_1=|+A|+|-A|=2A
||phi||_infty=1/2
||div||_1 ||phi||_infty=A
<div,phi>=(+A)(+1/2)+(-A)(-1/2)=A
<div,phi>=||div||_1 ||phi||_infty
sign(div(r0))=sign(phi(r0))=+
sign(div(r*))=sign(phi(r*))=-
A C_Pi=W.
```

若 `r0=r*`，则势差与对偶质量退化并回流 singleton/degenerate 出口；否则方向由
正散度/正势端与负散度/负势端的极化关系保留。剩余压力不再是匿名 cut-potential，
而是带 Hölder 等号饱和和极化符号对齐的 dual-norm 证书。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeCutPotentialDualNormSaturationCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange cut-potential dual-norm saturation
circuit PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；也没有证明线性见证本身存在。
它只把 cut-potential 配对压成 dual-norm saturation 证书
或 mean/singleton/sparse/三出口。

### 1.117 stable-ladder phase-residue exchange complementary slackness 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_dual_norm_complementary_slackness_router.py
data/prime-matrix-phase-residue-exchange-dual-norm-complementary-slackness-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-dual-norm-complementary-slackness-router.md
docs/monograph/prime-matrix-phase-residue-exchange-dual-norm-complementary-slackness-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeCutPotentialDualNormSaturationCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_cut_potential_dual_norm_imported=true
phase_residue_exchange_calibrated_edge_orientation_closed=true
phase_residue_exchange_complementary_slackness_unit_potential_drop_closed=true
phase_residue_exchange_complementary_slackness_primal_flux_closed=true
phase_residue_exchange_complementary_slackness_primal_cost_closed=true
phase_residue_exchange_complementary_slackness_dual_value_closed=true
phase_residue_exchange_complementary_slackness_zero_duality_gap_closed=true
phase_residue_exchange_complementary_slackness_saturated_edge_support_closed=true
linear_witness_existence_proved=false
phase_residue_exchange_dual_norm_complementary_slackness_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层给出：

```text
div(r0)=+A
div(r*)=-A
phi(r0)=+1/2
phi(r*)=-1/2
||div||_1=2A
||phi||_infty=1/2
<div,phi>=||div||_1 ||phi||_infty=A
A C_Pi=W.
```

本步删除 dual-norm saturation 黑箱口径，把非退化对象登记为 primal/dual 互补松弛零间隙：

```text
e=(r* -> r0)
partial(A e)=A([r0]-[r*])=div
cost(e)=1
phi(r0)-phi(r*)=1=cost(e)
primal_cost=A cost(e)=A
dual_value=<div,phi>=A
duality_gap=primal_cost-dual_value=0
support(F) subset {edges with phi(head)-phi(tail)=cost(edge)}
A C_Pi=W.
```

若 `r0=r*`，则边、势差和对偶间隙证书退化并回流 singleton/degenerate 出口；否则方向由
负势/负散度端指向正势/正散度端，即 source -> root。剩余压力不再是匿名 dual-norm saturation，
而是带单位势差饱和、通量成本等值和零对偶间隙的 complementary-slackness 证书。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeDualNormComplementarySlacknessCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange dual-norm complementary-slackness
circuit PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；也没有证明线性见证本身存在。
它只把 dual-norm saturation 压成 complementary-slackness 零间隙证书
或 mean/singleton/sparse/三出口。

### 1.118 stable-ladder phase-residue exchange active-facet normal-cone 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_complementary_slackness_active_facet_router.py
data/prime-matrix-phase-residue-exchange-complementary-slackness-active-facet-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-complementary-slackness-active-facet-router.md
docs/monograph/prime-matrix-phase-residue-exchange-complementary-slackness-active-facet-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeDualNormComplementarySlacknessCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_complementary_slackness_imported=true
phase_residue_exchange_active_facet_dual_feasibility_closed=true
phase_residue_exchange_active_facet_equality_closed=true
phase_residue_exchange_active_facet_normal_vector_closed=true
phase_residue_exchange_active_facet_normal_cone_closed=true
phase_residue_exchange_active_facet_flow_normal_cone_membership_closed=true
phase_residue_no_inactive_constraint_carries_flux_after_active_facet_closed=true
linear_witness_existence_proved=false
phase_residue_exchange_complementary_slackness_active_facet_normal_cone_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层给出：

```text
e=(r* -> r0)
partial(A e)=A([r0]-[r*])=div
cost(e)=1
phi(r0)-phi(r*)=1=cost(e)
primal_cost=A
dual_value=<div,phi>=A
duality_gap=0
A C_Pi=W.
```

本步删除 complementary slackness 黑箱口径，把非退化对象登记为单个活跃 Lipschitz 约束面及其正法锥：

```text
dual_feasible_constraint: phi(r0)-phi(r*) <= 1
active_constraint: phi(r0)-phi(r*) = 1
n_e=[r0]-[r*]
normal_cone(e)={lambda n_e: lambda>=0}
div=A n_e
div in normal_cone(e)
gap=A(1-(phi(r0)-phi(r*)))=0
inactive_constraint_with_A_positive => gap>0
A C_Pi=W.
```

若 `r0=r*` 或 `A=0`，则法向量/法锥证书退化并回流 singleton/degenerate 出口；否则方向由
正法向量 `[r0]-[r*]` 固定为 source -> root。剩余压力不再是匿名 complementary slackness，
而是带单活跃约束面、正法锥隶属和非活跃约束排除的 active-facet 证书。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeComplementarySlacknessActiveFacetNormalConeCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange complementary-slackness active-facet
normal-cone circuit PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；也没有证明线性见证本身存在。
它只把 complementary-slackness 零间隙压成 active-facet normal-cone 证书
或 mean/singleton/sparse/三出口。

### 1.119 stable-ladder phase-residue exchange normal-cone ray-coordinate 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeComplementarySlacknessActiveFacetNormalConeCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_active_facet_normal_cone_imported=true
phase_residue_exchange_normal_cone_ray_generator_closed=true
phase_residue_exchange_normal_cone_ray_coordinate_closed=true
phase_residue_exchange_normal_cone_positive_coordinate_closed=true
phase_residue_exchange_normal_cone_unique_coordinate_closed=true
phase_residue_exchange_normal_cone_no_transverse_component_closed=true
phase_residue_exchange_normal_cone_coordinate_boundary_pairing_closed=true
phase_residue_exchange_normal_cone_coordinate_total_variation_closed=true
linear_witness_existence_proved=false
phase_residue_exchange_active_facet_normal_cone_ray_coordinate_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层给出：

```text
phi(r0)-phi(r*)=1
n_e=[r0]-[r*]
normal_cone(e)={lambda n_e: lambda>=0}
div=A n_e
div in normal_cone(e)
A C_Pi=W.
```

本步删除 active-facet normal-cone 黑箱口径，把非退化对象登记为唯一正射线坐标：

```text
ray_generator=n_e=[r0]-[r*]
div=lambda n_e
lambda=A>0
transverse_component=0
<div,phi>=lambda(phi(r0)-phi(r*))=A
||div||_1=2lambda=2A
A C_Pi=W.
```

若 `r0=r*` 或 `A=0`，则生成元/坐标证书退化并回流 singleton/degenerate 出口；否则
`n_e` 的二点支撑和一维正法锥强制唯一坐标 `lambda=A`，不存在匿名横向法锥分量。
剩余压力不再是匿名 active-facet normal-cone，而是 normal-cone ray-coordinate circuit PDEC/cap
或已有出口。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange active-facet normal-cone ray-coordinate
circuit PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；也没有证明线性见证本身存在。
它只把 active-facet normal-cone 压成唯一正射线坐标证书
或 mean/singleton/sparse/三出口。

### 1.120 stable-ladder phase-residue exchange ray-coordinate scalar-load 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_normal_cone_ray_coordinate_imported=true
phase_residue_exchange_ray_coordinate_positive_scalar_load_closed=true
phase_residue_exchange_ray_coordinate_rank_one_support_closed=true
phase_residue_exchange_ray_coordinate_scalar_pairing_equals_load_closed=true
phase_residue_exchange_ray_coordinate_half_total_variation_equals_load_closed=true
phase_residue_exchange_ray_coordinate_unit_saturation_ratio_closed=true
phase_residue_exchange_ray_coordinate_no_residual_vector_geometry_closed=true
linear_witness_existence_proved=false
phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层给出：

```text
n_e=[r0]-[r*]
div=lambda n_e
lambda=A>0
transverse_component=0
<div,phi>=A
||div||_1=2A
A C_Pi=W.
```

本步删除 ray-coordinate 黑箱口径，把非退化对象登记为单一正标量负载：

```text
scalar_load=A=lambda>0
rank_one_generator=n_e=[r0]-[r*]
pairing_load=<div,phi>=A
variation_load=||div||_1/2=A
unit_saturation_ratio=1
residual_vector_geometry=0
A C_Pi=W.
```

若 `r0=r*` 或 `A=0`，则 scalar load 退化并回流 singleton/degenerate 出口；否则
所有几何自由度已冻结在同一生成元 `n_e` 上，待支付对象只剩一维正标量 `A`。
剩余压力不再是匿名 ray-coordinate，而是 scalar-load circuit PDEC/cap 或已有出口。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange active-facet normal-cone ray-coordinate
scalar-load circuit PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；也没有证明线性见证本身存在。
它只把 ray-coordinate 压成唯一 scalar-load 支付证书
或 mean/singleton/sparse/三出口。

### 1.121 stable-ladder phase-residue exchange scalar-load unit-normalization 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_scalar_load_imported=true
phase_residue_exchange_scalar_load_unit_generator_closed=true
phase_residue_exchange_scalar_load_unit_pairing_load_closed=true
phase_residue_exchange_scalar_load_unit_variation_load_closed=true
phase_residue_exchange_scalar_load_unit_saturation_ratio_closed=true
phase_residue_exchange_scalar_load_scale_factor_closed=true
phase_residue_exchange_scalar_load_div_factorization_closed=true
phase_residue_exchange_scalar_load_no_residual_scale_freedom_closed=true
linear_witness_existence_proved=false
phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层给出：

```text
scalar_load=A=lambda>0
rank_one_generator=n_e=[r0]-[r*]
pairing_load=<div,phi>=A
variation_load=||div||_1/2=A
unit_saturation_ratio=1
residual_vector_geometry=0
A C_Pi=W.
```

本步把 scalar-load 的尺度和单位形状分离：

```text
unit_div=n_e=[r0]-[r*]
<unit_div,phi>=1
||unit_div||_1/2=1
unit_saturation_ratio=1
scale_factor=A>0
div=A*unit_div=A*n_e
total_weight=A
A C_Pi=W
residual_scale_freedom=0.
```

若 `r0=r*` 或 `A=0`，则单位形状或正尺度退化并回流 singleton/degenerate 出口；否则
待支付对象就是同一单位二点形状上的总权重 `A`。剩余压力不再是匿名 scalar-load 尺度规范，
而是 scalar-load unit-normalization circuit PDEC/cap 或已有出口。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange active-facet normal-cone ray-coordinate
scalar-load unit-normalization circuit PDEC/cap、bridge-cancellation PDEC/cap、
amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap 或 sparse SAE 求和；
也没有证明线性见证本身存在。它只把 scalar-load 压成单位形状加总权重证书
或 mean/singleton/sparse/三出口。

### 1.122 stable-ladder phase-residue exchange unit-face-value 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_scalar_load_unit_normalization_imported=true
phase_residue_exchange_unit_face_value_unit_shape_closed=true
phase_residue_exchange_unit_face_value_pairing_closed=true
phase_residue_exchange_unit_face_value_variation_closed=true
phase_residue_exchange_unit_face_value_one_closed=true
phase_residue_exchange_unit_face_value_total_amount_closed=true
phase_residue_exchange_unit_face_value_payment_value_closed=true
phase_residue_exchange_unit_face_value_no_capacity_multiplier_closed=true
phase_residue_exchange_unit_face_value_no_denomination_split_closed=true
linear_witness_existence_proved=false
phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层给出：

```text
unit_div=n_e=[r0]-[r*]
<unit_div,phi>=1
||unit_div||_1/2=1
unit_saturation_ratio=1
scale_factor=A>0
div=A*unit_div=A*n_e
total_weight=A
A C_Pi=W
residual_scale_freedom=0.
```

本步把单位证书的容量面额固定为 1：

```text
u_e=n_e=[r0]-[r*]
<u_e,phi>=1
||u_e||_1/2=1
face_value=1
C_Pi(r0)=+1
C_Pi(r*)=-1
C_Pi(other)=0
amount=A>0
payment_value=amount*face_value=A
W=A C_Pi
capacity_multiplier=1
denomination_split=0.
```

若 `r0=r*` 或 `A=0`，则单位面额证书退化并回流 singleton/degenerate 出口；否则
待支付对象就是同一 price-one 单位证书上的数量 `A`。剩余压力不再是匿名容量面额、
容量乘子或多面额拆分，而是 unit-face-value circuit PDEC/cap 或已有出口。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange active-facet normal-cone ray-coordinate
scalar-load unit-normalization unit-face-value circuit PDEC/cap、bridge-cancellation PDEC/cap、
amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap 或 sparse SAE 求和；
也没有证明线性见证本身存在。它只把 unit-normalization 压成 price-one 支付证书
或 mean/singleton/sparse/三出口。

### 1.123 stable-ladder phase-residue exchange signed-amount-coordinate 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_unit_face_value_imported=true
phase_residue_exchange_signed_amount_coordinate_price_one_closed=true
phase_residue_exchange_signed_amount_coordinate_positive_endpoint_atom_closed=true
phase_residue_exchange_signed_amount_coordinate_negative_endpoint_atom_closed=true
phase_residue_exchange_signed_amount_coordinate_signed_mass_closed=true
phase_residue_exchange_signed_amount_coordinate_endpoint_mass_balance_closed=true
phase_residue_exchange_signed_amount_coordinate_half_l1_equals_amount_closed=true
phase_residue_exchange_signed_amount_coordinate_no_amount_slot_split_closed=true
phase_residue_exchange_signed_amount_coordinate_no_orientation_flip_closed=true
linear_witness_existence_proved=false
phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层给出：

```text
u_e=n_e=[r0]-[r*]
<u_e,phi>=1
||u_e||_1/2=1
face_value=1
C_Pi(r0)=+1
C_Pi(r*)=-1
C_Pi(other)=0
amount=A>0
payment_value=A
W=A C_Pi
capacity_multiplier=1
denomination_split=0.
```

本步把 price-one 支付数量写成唯一二端点有符号质量坐标：

```text
positive_endpoint_atom=A delta_{r0}
negative_endpoint_atom=A delta_{r*}
signed_mass=W=A(delta_{r0}-delta_{r*})=A C_Pi
positive_mass=A
negative_mass=A
net_mass=0
||W||_1=2A
||W||_1/2=A
support={r0,r*}
amount_slot_split=0
orientation_flip=0
anonymous_amount_pool=0.
```

若 `r0=r*` 或 `A=0`，则二端点有符号质量退化并回流 singleton/degenerate 出口；否则
待支付对象就是同一 signed dictionary 上的唯一 amount 坐标。剩余压力不再是匿名 amount 池、
多槽拆分或方向翻转，而是 signed-amount-coordinate circuit PDEC/cap 或已有出口。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinateCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange active-facet normal-cone ray-coordinate
scalar-load unit-normalization unit-face-value signed-amount-coordinate circuit PDEC/cap、
bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap
或 sparse SAE 求和；也没有证明线性见证本身存在。它只把 unit-face-value 压成
二端点 signed-amount-coordinate 证书或 mean/singleton/sparse/三出口。

### 1.124 stable-ladder phase-residue exchange phase-pairing 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinateCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_signed_amount_coordinate_imported=true
phase_residue_exchange_phase_pairing_unit_gap_closed=true
phase_residue_exchange_phase_pairing_signed_mass_value_closed=true
phase_residue_exchange_phase_pairing_equals_amount_closed=true
phase_residue_exchange_phase_pairing_equals_half_l1_closed=true
phase_residue_exchange_phase_pairing_equals_payment_value_closed=true
phase_residue_exchange_phase_pairing_no_phase_rescale_closed=true
phase_residue_exchange_phase_pairing_no_sign_mismatch_closed=true
linear_witness_existence_proved=false
phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

上一层给出：

```text
positive_endpoint_atom=A delta_{r0}
negative_endpoint_atom=A delta_{r*}
signed_mass=W=A(delta_{r0}-delta_{r*})=A C_Pi
positive_mass=A
negative_mass=A
net_mass=0
||W||_1=2A
||W||_1/2=A
support={r0,r*}
amount_slot_split=0
orientation_flip=0
anonymous_amount_pool=0.
```

本步把相位读数也锁成同一个校准值：

```text
phi(r0)-phi(r*)=1
positive_phase_contribution=A phi(r0)
negative_phase_contribution=A phi(r*)
<W,phi>=A(phi(r0)-phi(r*))=A
phase_pairing_value=A
amount=A
payment_value=A
||W||_1/2=A
constant_offset_cancelled=true
phase_rescale=0
sign_mismatch=0
phase_pairing_support={r0,r*}.
```

若 `r0=r*` 或 `A=0`，则相位配对退化并回流 singleton/degenerate 出口；否则
待支付对象就是同一二端点 signed dictionary 上的校准相位配对。剩余压力不再是
相位偏移、相位重标定或正负端点符号错配，而是 phase-pairing circuit PDEC/cap 或已有出口。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange active-facet normal-cone ray-coordinate
scalar-load unit-normalization unit-face-value signed-amount-coordinate phase-pairing
circuit PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；也没有证明线性见证本身存在。
它只把 signed-amount-coordinate 压成校准 phase-pairing 证书或 mean/singleton/sparse/三出口。

### 1.125 stable-ladder phase-residue exchange circuit-materialization 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_circuit_materialization_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-circuit-materialization-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-circuit-materialization-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-circuit-materialization-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_phase_pairing_circuit_imported=true
phase_residue_exchange_circuit_same_formal_unit_key_schema_closed=true
phase_residue_exchange_circuit_source_atom_slot_closed=true
phase_residue_exchange_circuit_occurrence_unit_slot_closed=true
phase_residue_exchange_circuit_crt_coordinate_slot_closed=true
phase_residue_exchange_circuit_phase_evaluation_slot_closed=true
phase_residue_exchange_circuit_signed_mass_slot_closed=true
phase_residue_exchange_circuit_calibrated_pairing_slot_closed=true
phase_residue_exchange_no_object_switch_after_phase_pairing_closed=true
phase_residue_exchange_actual_circuit_materialization_proved=false
phase_residue_exchange_materialized_circuit_capacity_pdec_cap_proved=false
phase_residue_exchange_phase_pairing_circuit_pdec_cap_proved=false
linear_witness_existence_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：phase-pairing circuit 不能再作为可换对象的黑箱。source atom、
occurrence unit、CRT coordinate、canonical congruence、phase evaluation、signed mass 与
calibrated pairing 必须共享同一个 formal-unit key，并且要在同一个 actual CRT/fiber 对象上物化。

同一对象门为：

```text
same_formal_unit_key=true
source_atom_slot=same key
occurrence_unit_slot=same key
crt_coordinate_slot=same key
canonical_congruence_slot=same key
phase_evaluation_slot=same key
signed_mass_slot=W=A(delta_{r0}-delta_{r*})
calibrated_pairing_slot=<W,phi>=A
object_switch=0
```

若任一槽不能同物化，则进入 actual-circuit materialization PDEC/cap；若同物化成立，
剩余就是同一个实际 circuit 上以 `A` 为负载的 materialized-circuit capacity PDEC/cap。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingActualCircuitMaterializationPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitCapacityPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 actual-circuit materialization PDEC/cap、materialized-circuit capacity
PDEC/cap、endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom multiplicity-cap、
bridge-cancellation、amplitude-depth、variation-boundary flux 或 sparse SAE 求和；也没有证明
线性见证本身存在。它只把 phase-pairing circuit 压成同一对象物化门和物化后容量门。

### 1.126 stable-ladder phase-residue exchange actual-object-predicate 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_actual_object_predicate_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-actual-object-predicate-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-actual-object-predicate-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-actual-object-predicate-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingActualCircuitMaterializationPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitCapacityPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_actual_circuit_materialization_imported=true
phase_residue_exchange_actual_object_tuple_schema_closed=true
phase_residue_exchange_actual_object_canonical_hash_closed=true
phase_residue_exchange_actual_object_source_incidence_predicate_closed=true
phase_residue_exchange_actual_object_occurrence_incidence_predicate_closed=true
phase_residue_exchange_actual_object_crt_representative_predicate_closed=true
phase_residue_exchange_actual_object_phase_endpoint_predicate_closed=true
phase_residue_exchange_actual_object_signed_mass_predicate_closed=true
phase_residue_exchange_actual_object_calibrated_pairing_predicate_closed=true
phase_residue_exchange_actual_object_incidence_predicate_proved=false
phase_residue_exchange_materialized_circuit_capacity_pdec_cap_proved=false
linear_witness_existence_proved=false
row_column_unconditional_closed=false
```

actual materialization 被写成七槽 actual object：

```text
O=(source_atom, occurrence_unit, crt_coordinate, canonical_congruence, phase_evaluation, signed_mass, calibrated_pairing)
actual_object_hash=H(formal_unit_key,O)
source_incidence=true
occurrence_incidence=true
crt_representative=true
canonical_congruence_eval=true
phase_endpoint_eval=true
signed_mass_match=true
calibrated_pairing_match=true
```

若缺少 actual object、有两个不同 actual object，或任一槽位不匹配，则进入
actual-object incidence predicate PDEC/cap；若全部谓词成立，才进入 materialized-circuit
capacity 门。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingActualObjectIncidencePredicatePDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitCapacityPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 actual-object incidence predicate PDEC/cap、materialized-circuit capacity
PDEC/cap、endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom multiplicity-cap、
bridge-cancellation、amplitude-depth、variation-boundary flux 或 sparse SAE 求和；也没有证明
线性见证本身存在。它只把 actual materialization 压成显式七槽同对象谓词。

### 1.127 stable-ladder phase-residue exchange materialized-capacity-slack 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_materialized_capacity_slack_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingActualObjectIncidencePredicatePDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitCapacityPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_materialized_circuit_capacity_imported=true
phase_residue_exchange_capacity_slack_same_actual_object_closed=true
phase_residue_exchange_capacity_slack_actual_load_closed=true
phase_residue_exchange_capacity_slack_formula_closed=true
phase_residue_exchange_no_formal_envelope_after_capacity_slack_closed=true
phase_residue_exchange_no_load_switch_after_capacity_slack_closed=true
phase_residue_exchange_capacity_value_bound_proved=false
phase_residue_exchange_materialized_capacity_slack_pdec_cap_proved=false
phase_residue_exchange_actual_object_incidence_predicate_proved=false
linear_witness_existence_proved=false
row_column_unconditional_closed=false
```

materialized capacity 被写成同一 actual object 的 slack：

```text
O=(source_atom, occurrence_unit, crt_coordinate, canonical_congruence, phase_evaluation, signed_mass, calibrated_pairing)
L(O)=A=<W,phi>
A=amount=payment_value=||W||_1/2
C(O)=capacity of the same materialized circuit
Sigma(O)=C(O)-A
```

分支为：

```text
Sigma(O)>0 -> absorbed by capacity
Sigma(O)<0 -> materialized capacity slack PDEC/cap
Sigma(O)=0 -> boundary equality atom
formal_envelope_load=forbidden
load_switch=0
```

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingActualObjectIncidencePredicatePDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitCapacitySlackPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 materialized capacity slack PDEC/cap、actual-object incidence predicate PDEC/cap、
endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom multiplicity-cap、
bridge-cancellation、amplitude-depth、variation-boundary flux 或 sparse SAE 求和；也没有证明
线性见证本身存在。它只把 materialized capacity 压成同对象 slack 不等式。

### 1.128 stable-ladder phase-residue exchange materialized-capacity-slack-sign 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_materialized_capacity_slack_sign_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-sign-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-sign-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-sign-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingActualObjectIncidencePredicatePDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitCapacitySlackPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_materialized_capacity_slack_imported=true
phase_residue_exchange_capacity_slack_sign_trichotomy_closed=true
phase_residue_exchange_positive_slack_absorption_closed=true
phase_residue_exchange_no_strict_contradiction_from_equality_closed=true
phase_residue_exchange_no_slack_sign_merge_closed=true
phase_residue_exchange_negative_slack_pdec_cap_proved=false
phase_residue_exchange_boundary_equality_atom_exclusion_proved=false
phase_residue_exchange_actual_object_incidence_predicate_proved=false
linear_witness_existence_proved=false
row_column_unconditional_closed=false
```

同对象 slack 的符号三分为：

```text
Sigma(O)>0 -> PositiveSlackAbsorption
Sigma(O)<0 -> MaterializedCircuitNegativeSlackPDECCap
Sigma(O)=0 -> MaterializedCircuitBoundaryEqualityAtomPDEC
equality_is_not_strict_contradiction=true
anonymous_slack_sign_merge=0
```

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingActualObjectIncidencePredicatePDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitNegativeSlackPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitBoundaryEqualityAtomPDECOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 materialized negative-slack PDEC/cap、没有排斥 boundary equality atom、
没有证明 actual-object incidence predicate PDEC/cap，也没有证明 endpoint singleton、
full-cycle mean、source-atom multiplicity-cap、bridge、amplitude、boundary 或 sparse SAE 求和；
也没有证明线性见证本身存在。它只把 materialized capacity slack 压成严格的符号三分。

### 1.129 stable-ladder phase-residue exchange negative-unit-defect 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_materialized_capacity_slack_sign_negative_unit_defect_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-sign-negative-unit-defect-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-sign-negative-unit-defect-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-sign-negative-unit-defect-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingActualObjectIncidencePredicatePDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitNegativeSlackPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitBoundaryEqualityAtomPDECOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_negative_slack_imported=true
phase_residue_exchange_negative_slack_same_actual_object_closed=true
phase_residue_exchange_negative_slack_deficit_formula_closed=true
phase_residue_exchange_negative_slack_no_infinitesimal_escape_closed=true
phase_residue_exchange_capacity_value_unit_integrality_proved=false
phase_residue_exchange_unit_negative_defect_pdec_cap_proved=false
phase_residue_exchange_boundary_equality_atom_exclusion_proved=false
phase_residue_exchange_actual_object_incidence_predicate_proved=false
linear_witness_existence_proved=false
row_column_unconditional_closed=false
```

负 slack 的单位缺口规整为：

```text
Sigma(O)=C(O)-A<0
D(O)=A-C(O)=-Sigma(O)>0

if C(O) is not a same-object unit integer capacity:
  MaterializedCircuitCapacityValueUnitIntegralityPDECCap
otherwise:
  D(O) in Z_{>=1}
  MaterializedCircuitUnitNegativeDefectPDECCap
```

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingActualObjectIncidencePredicatePDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitCapacityValueUnitIntegralityPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitUnitNegativeDefectPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitBoundaryEqualityAtomPDECOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 capacity-value unit-integrality PDEC/cap、没有排斥 unit negative defect、
没有排斥 boundary equality atom，也没有证明 actual-object incidence predicate PDEC/cap；
也没有证明 endpoint singleton、full-cycle mean、source-atom multiplicity-cap、bridge、
amplitude、boundary 或 sparse SAE 求和；也没有证明线性见证本身存在。
它只切掉“负 slack 作为匿名实数微小误差”的出口。

### 1.130 stable-ladder phase-residue exchange unit-defect-witness 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_unit_defect_witness_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-unit-defect-witness-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-unit-defect-witness-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-unit-defect-witness-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingActualObjectIncidencePredicatePDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitCapacityValueUnitIntegralityPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitUnitNegativeDefectPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitBoundaryEqualityAtomPDECOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_unit_negative_defect_imported=true
phase_residue_exchange_demand_unit_set_locked=true
phase_residue_exchange_unit_defect_cardinality_gap_closed=true
phase_residue_exchange_unit_defect_nonempty_complement_closed=true
phase_residue_exchange_no_aggregate_unit_defect_escape_closed=true
phase_residue_exchange_unit_capacity_assignment_incidence_proved=false
phase_residue_exchange_missing_capacity_unit_witness_pdec_cap_proved=false
phase_residue_exchange_capacity_value_unit_integrality_proved=false
phase_residue_exchange_boundary_equality_atom_exclusion_proved=false
phase_residue_exchange_actual_object_incidence_predicate_proved=false
linear_witness_existence_proved=false
row_column_unconditional_closed=false
```

单位缺口的见证化为：

```text
D(O)=A-C(O)>=1
|U_A|=A
|U_C|=C(O)

if U_C is not materialized as a same-object assigned subset of U_A:
  MaterializedCircuitUnitCapacityAssignmentIncidencePDECCap
otherwise:
  choose u* in U_A \ U_C
  MaterializedCircuitMissingCapacityUnitWitnessPDECCap
```

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingActualObjectIncidencePredicatePDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitCapacityValueUnitIntegralityPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitUnitCapacityAssignmentIncidencePDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitMissingCapacityUnitWitnessPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitBoundaryEqualityAtomPDECOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 unit-capacity assignment incidence PDEC/cap、没有排斥 missing capacity unit witness、
没有证明 capacity-value unit-integrality、没有排斥 boundary equality atom，也没有证明
actual-object incidence predicate PDEC/cap；也没有证明 endpoint singleton、full-cycle mean、
source-atom multiplicity-cap、bridge、amplitude、boundary 或 sparse SAE 求和；也没有证明
线性见证本身存在。它只把单位负缺口从匿名总量赤字压成分配缺陷或具体缺失单位见证。

### 1.131 stable-ladder phase-residue exchange missing-unit-coordinate-lock 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_missing_unit_coordinate_lock_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-missing-unit-coordinate-lock-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-missing-unit-coordinate-lock-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-missing-unit-coordinate-lock-router.json
```

本步继续攻击：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingActualObjectIncidencePredicatePDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitCapacityValueUnitIntegralityPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitUnitCapacityAssignmentIncidencePDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitMissingCapacityUnitWitnessPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitBoundaryEqualityAtomPDECOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

同步读数为：

```text
phase_residue_exchange_missing_capacity_unit_witness_imported=true
phase_residue_exchange_missing_unit_demand_membership_closed=true
phase_residue_exchange_missing_unit_capacity_exclusion_closed=true
phase_residue_exchange_missing_unit_coordinate_lock_schema_closed=true
phase_residue_exchange_no_moving_missing_unit_witness_closed=true
phase_residue_exchange_missing_unit_coordinate_slot_mismatch_pdec_cap_proved=false
phase_residue_exchange_canonical_missing_capacity_unit_witness_pdec_cap_proved=false
phase_residue_exchange_unit_capacity_assignment_incidence_proved=false
phase_residue_exchange_capacity_value_unit_integrality_proved=false
phase_residue_exchange_boundary_equality_atom_exclusion_proved=false
phase_residue_exchange_actual_object_incidence_predicate_proved=false
linear_witness_existence_proved=false
row_column_unconditional_closed=false
```

缺失单位的 canonical 坐标锁为：

```text
u* in U_A
u* notin U_C

required slots:
  source_atom
  occurrence_unit
  CRT_coordinate
  canonical_congruence
  phase_endpoint
  signed_amount

if any slot is missing or switched:
  MaterializedCircuitMissingUnitCoordinateSlotMismatchPDECCap
otherwise:
  MaterializedCircuitCanonicalMissingCapacityUnitWitnessPDECCap
```

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingActualObjectIncidencePredicatePDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitCapacityValueUnitIntegralityPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitUnitCapacityAssignmentIncidencePDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitMissingUnitCoordinateSlotMismatchPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitCanonicalMissingCapacityUnitWitnessPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitBoundaryEqualityAtomPDECOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 coordinate slot mismatch PDEC/cap、没有排斥 canonical missing capacity unit witness、
没有证明 unit-capacity assignment incidence、没有证明 capacity-value unit-integrality、
没有排斥 boundary equality atom，也没有证明 actual-object incidence predicate PDEC/cap；
也没有证明 endpoint singleton、full-cycle mean、source-atom multiplicity-cap、bridge、
amplitude、boundary 或 sparse SAE 求和；也没有证明线性见证本身存在。
它只把缺失单位见证从可移动对象压成 canonical 坐标见证或换槽缺陷。

### 1.132 stable-ladder phase-residue exchange canonical-missing-unit-balance 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_missing_unit_balance_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-missing-unit-balance-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-missing-unit-balance-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-missing-unit-balance-router.json
```

同步读数为：

```text
phase_residue_exchange_canonical_missing_capacity_unit_witness_imported=true
phase_residue_exchange_canonical_missing_unit_key_closed=true
phase_residue_exchange_canonical_missing_unit_demand_indicator_closed=true
phase_residue_exchange_canonical_missing_unit_capacity_indicator_closed=true
phase_residue_exchange_canonical_missing_unit_face_value_closed=true
phase_residue_exchange_canonical_missing_unit_cell_deficit_closed=true
phase_residue_exchange_no_anonymous_canonical_missing_unit_compensation_closed=true
phase_residue_exchange_canonical_missing_unit_unpaid_demand_cell_pdec_cap_proved=false
phase_residue_exchange_canonical_missing_unit_compensation_mismatch_pdec_cap_proved=false
phase_residue_exchange_missing_unit_coordinate_slot_mismatch_pdec_cap_proved=false
phase_residue_exchange_unit_capacity_assignment_incidence_proved=false
phase_residue_exchange_capacity_value_unit_integrality_proved=false
phase_residue_exchange_boundary_equality_atom_exclusion_proved=false
phase_residue_exchange_actual_object_incidence_predicate_proved=false
linear_witness_existence_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：canonical 缺失单位已经不能换对象或换槽。
令它的 canonical key 为 `k`，则 `u* in U_A` 给出 `I_A(k)=1`，
`u* notin U_C` 给出 `I_C(k)=0`，且 signed amount 已单位化，所以同一
canonical cell 上出现单位赤字 `I_A(k)-I_C(k)=1`。

余额路由为：

```text
canonical key k
I_A(k)=1
I_C(k)=0
unit_face_value=1

if no legal same-object same-key compensator exists:
  MaterializedCircuitCanonicalMissingUnitUnpaidDemandCellPDECCap
otherwise if the compensator switches object/key/slot or lacks a named outlet:
  MaterializedCircuitCanonicalMissingUnitCompensationMismatchPDECCap
```

本步没有证明 canonical unpaid demand cell PDEC/cap、没有证明 canonical
compensation mismatch PDEC/cap、没有证明 missing-unit coordinate slot mismatch、
没有证明 unit-capacity assignment incidence、capacity-value unit-integrality、
actual-object incidence predicate，也没有排斥 boundary equality atom 或 endpoint
并行出口；它只把 canonical 缺失单位压成同 key 的单位余额赤字。

### 1.133 stable-ladder phase-residue exchange canonical-unit-payment-conservation 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_unit_payment_conservation_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-unit-payment-conservation-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-unit-payment-conservation-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-unit-payment-conservation-router.json
```

同步读数为：

```text
phase_residue_exchange_canonical_unpaid_or_mismatch_imported=true
phase_residue_exchange_canonical_unit_demand_key_closed=true
phase_residue_exchange_canonical_unit_capacity_key_closed=true
phase_residue_exchange_no_hidden_cross_key_payment_closed=true
phase_residue_exchange_canonical_unit_payment_graph_closed=false
phase_residue_exchange_same_key_payment_edge_obligation_proved=false
phase_residue_exchange_canonical_payment_return_whitelist_proved=false
phase_residue_exchange_canonical_unit_payment_conservation_defect_pdec_cap_proved=false
phase_residue_exchange_canonical_unit_compensator_key_collision_pdec_cap_proved=false
phase_residue_exchange_boundary_equality_atom_exclusion_proved=false
phase_residue_exchange_actual_object_incidence_predicate_proved=false
linear_witness_existence_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：`unpaid demand cell` 与 `compensation mismatch`
现在统一进入 canonical 单位支付图。直接支付必须来自同一 actual object、同一 key
的容量边；非同 key 的补偿必须进入 boundary、bridge、assignment 或 slot-mismatch
等已命名出口。未登记的跨 key 支付不能支付同一 canonical cell。

支付守恒路由为：

```text
canonical key k
I_A(k)=1
I_C(k)=0

if no same-object same-key capacity edge and no named return exists:
  MaterializedCircuitCanonicalUnitPaymentConservationDefectPDECCap
otherwise if a compensator uses another key:
  MaterializedCircuitCanonicalUnitCompensatorKeyCollisionPDECCap
```

本步没有证明 canonical payment conservation defect、没有证明 canonical
compensator key collision、没有证明 canonical payment graph 完全闭合，
也没有证明 same-key payment edge obligation 或 return whitelist；行/列命题仍未无条件闭合。

### 1.134 stable-ladder phase-residue exchange canonical-unit-payment-singleton-cut 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_unit_payment_singleton_cut_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-unit-payment-singleton-cut-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-unit-payment-singleton-cut-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-unit-payment-singleton-cut-router.json
```

同步读数为：

```text
phase_residue_exchange_canonical_payment_defect_or_collision_imported=true
phase_residue_exchange_singleton_key_cut_closed=true
phase_residue_exchange_singleton_cut_demand_one_closed=true
phase_residue_exchange_singleton_cut_capacity_zero_closed=true
phase_residue_exchange_singleton_cut_balance_closed=true
phase_residue_exchange_same_key_capacity_edge_empty_on_cut_closed=true
phase_residue_exchange_cross_key_collision_trichotomy_closed=true
phase_residue_exchange_no_anonymous_payment_conservation_defect_closed=true
phase_residue_exchange_named_return_boundary_proved=false
phase_residue_exchange_canonical_singleton_hall_cut_defect_pdec_cap_proved=false
phase_residue_exchange_canonical_payment_key_injectivity_defect_pdec_cap_proved=false
phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved=false
phase_residue_exchange_canonical_unit_payment_graph_closed=false
phase_residue_exchange_canonical_payment_return_whitelist_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：当前 payment defect/key collision 不再只是
支付图中的匿名故障。取缺失 key `k` 的单点 Hall cut，有 `I_A(k)=1`
且 `I_C(k)=0`，所以同 key 直接容量为空；若没有命名 return 离开该 cut，
则保留显式 1 单位 Hall cut 缺口。若跨 key 补偿声称仍支付同一 canonical
cell，则变成 key injectivity defect；若它不是同一 cell 又未进入白名单，
则变成 cross-key return whitelist leak。

单点 cut 路由为：

```text
singleton cut S={k}
cut_demand = I_A(k)=1
cut_capacity = I_C(k)=0

if no named return leaves S:
  MaterializedCircuitCanonicalUnitSingletonHallCutDefectPDECCap
otherwise if a cross-key compensator claims the same canonical cell:
  MaterializedCircuitCanonicalPaymentKeyInjectivityDefectPDECCap
otherwise if a cross-key compensator is not whitelisted:
  MaterializedCircuitCanonicalCrossKeyReturnWhitelistLeakPDECCap
```

本步没有证明 singleton Hall cut defect、没有证明 payment key injectivity
defect、没有证明 cross-key return whitelist leak，也没有证明 payment graph
全局闭合或 return whitelist；行/列命题仍未无条件闭合。

### 1.135 stable-ladder phase-residue exchange canonical-payment-key-tuple-lock 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_key_tuple_lock_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-tuple-lock-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-tuple-lock-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-tuple-lock-router.json
```

同步读数为：

```text
phase_residue_exchange_payment_key_injectivity_defect_imported=true
phase_residue_exchange_actual_object_canonical_hash_imported=true
phase_residue_exchange_missing_unit_canonical_hash_imported=true
phase_residue_exchange_payment_cell_tuple_schema_closed=true
phase_residue_exchange_payment_key_defined_as_tuple_closed=true
phase_residue_exchange_same_cell_projection_equality_closed=true
phase_residue_exchange_cross_key_same_cell_trichotomy_closed=true
phase_residue_exchange_no_anonymous_key_injectivity_defect_closed=true
phase_residue_exchange_canonical_payment_key_tuple_alias_defect_pdec_cap_proved=false
phase_residue_exchange_missing_unit_coordinate_slot_mismatch_pdec_cap_proved=false
phase_residue_exchange_canonical_singleton_hall_cut_defect_pdec_cap_proved=false
phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：payment key 不再作为可碰撞的外部标签使用，而是
actual-object 七槽 hash 与 missing-unit canonical hash 的规范 tuple。若跨 key
补偿声称仍支付同一 canonical cell，则所有 tuple 投影必须逐槽相等。投影相等
但 key 不同，剩余为 canonical payment key tuple alias defect；若投影不等，
则回流 missing-unit coordinate slot mismatch。

key-tuple 路由为：

```text
payment_key = canonical_tuple(actual_object_hash, missing_unit_hash, phase/payment slots)

if cross-key compensator claims the same canonical cell:
  if tuple projections are equal and keys differ:
    MaterializedCircuitCanonicalPaymentKeyTupleAliasDefectPDECCap
  else:
    MaterializedCircuitMissingUnitCoordinateSlotMismatchPDECCap
```

本步没有证明 key tuple alias defect、没有证明 missing-unit coordinate slot
mismatch，也没有证明 singleton Hall cut defect、cross-key return whitelist leak、
payment graph 全局闭合或 return whitelist；行/列命题仍未无条件闭合。

### 1.136 stable-ladder phase-residue exchange canonical-payment-key-alias-normalization 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_key_alias_normalization_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-alias-normalization-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-alias-normalization-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-alias-normalization-router.json
```

同步读数为：

```text
phase_residue_exchange_payment_key_tuple_alias_imported=true
canonical_formal_unit_hash_stability_imported=true
phase_residue_exchange_payment_key_domain_separator_closed=true
phase_residue_exchange_payment_key_serialization_schema_closed=true
phase_residue_exchange_equal_tuple_equal_serialization_closed=true
phase_residue_exchange_payment_key_hash_formula_closed=true
phase_residue_exchange_alias_normalization_trichotomy_closed=true
phase_residue_exchange_no_anonymous_key_tuple_alias_closed=true
phase_residue_exchange_canonical_payment_key_serialization_drift_pdec_cap_proved=false
phase_residue_exchange_canonical_payment_noncanonical_key_label_residue_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：key tuple alias 不再是独立数学出口。payment key
被规范化为固定 domain separator 与 canonical tuple bytes 的 hash：

```text
payment_key = H('canonical_payment_key', canonical_bytes(payment_tuple))

if same tuple has two keys:
  if canonical_bytes differ:
    MaterializedCircuitCanonicalPaymentKeySerializationDriftPDECCap
  else:
    MaterializedCircuitCanonicalPaymentNoncanonicalKeyLabelResiduePDECCap
```

若同一 tuple 产生不同规范字节串，剩余为 canonical payment key serialization
drift；若规范字节串相同但记录仍携带另一个 key，则剩余为 noncanonical key
label residue。

本步没有证明 serialization drift、没有证明 noncanonical key label residue、
没有证明 missing-unit coordinate slot mismatch，也没有证明 singleton Hall cut、
cross-key return whitelist leak、payment graph 全局闭合或 return whitelist；
行/列命题仍未无条件闭合。

### 1.137 stable-ladder phase-residue exchange canonical-payment-serialization-codec-lock 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_serialization_codec_lock_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-serialization-codec-lock-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-serialization-codec-lock-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-serialization-codec-lock-router.json
```

同步读数为：

```text
phase_residue_exchange_canonical_payment_serialization_drift_imported=true
phase_residue_exchange_alias_normalization_imported=true
canonical_formal_unit_hash_stability_imported=true
phase_residue_exchange_payment_tuple_field_vector_closed=true
phase_residue_exchange_payment_field_tag_total_order_closed=true
phase_residue_exchange_payment_scalar_encoding_closed=true
phase_residue_exchange_payment_length_prefix_injective_codec_closed=true
phase_residue_exchange_payment_null_sentinel_closed=true
phase_residue_exchange_payment_codec_determinism_closed=true
phase_residue_exchange_equal_field_vector_equal_bytes_closed=true
phase_residue_exchange_serialization_drift_field_or_codec_dichotomy_closed=true
phase_residue_exchange_no_independent_serialization_drift_closed=true
phase_residue_exchange_canonical_payment_key_serialization_drift_pdec_cap_proved=true
phase_residue_exchange_canonical_payment_noncanonical_key_label_residue_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：canonical bytes 不再是可浮动的实现文本，而是
payment tuple 字段向量上的确定编码：

```text
canonical_bytes = codec(field_vector(payment_tuple))

if same tuple has two canonical byte strings:
  if field vectors differ:
    named slot/object/assignment exit
  else:
    impossible by deterministic canonical codec
```

因此 serialization drift 不能作为独立活动出口保留。若字段向量不同，它回流
missing-unit coordinate slot mismatch、actual-object incidence、unit assignment
等已有命名出口；若字段向量相同，则字段顺序、类型标签、长度前缀、唯一标量
编码与空值哨兵强制同一字节串。

本步没有证明 noncanonical key label residue、没有证明 missing-unit coordinate
slot mismatch，也没有证明 singleton Hall cut、cross-key return whitelist leak、
payment graph 全局闭合或 return whitelist；行/列命题仍未无条件闭合。

### 1.138 stable-ladder phase-residue exchange canonical-payment-key-label-admission-lock 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_key_label_admission_lock_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-label-admission-lock-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-label-admission-lock-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-label-admission-lock-router.json
```

同步读数为：

```text
phase_residue_exchange_canonical_payment_noncanonical_key_label_residue_imported=true
phase_residue_exchange_serialization_codec_lock_imported=true
phase_residue_exchange_payment_admitted_key_formula_closed=true
phase_residue_exchange_payment_external_label_erasure_closed=true
phase_residue_exchange_payment_edge_admission_predicate_closed=true
phase_residue_exchange_payment_return_whitelist_binding_closed=true
phase_residue_exchange_payment_noncanonical_label_not_admitted_edge_closed=true
phase_residue_exchange_noncanonical_label_to_whitelist_leak_closed=true
phase_residue_exchange_no_independent_noncanonical_label_residue_closed=true
phase_residue_exchange_canonical_payment_noncanonical_key_label_residue_pdec_cap_proved=true
phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：payment edge 的身份只来自 admitted key：

```text
admitted_key = H('canonical_payment_key', canonical_bytes(payment_tuple))
admitted_edge = canonical_key_ok AND object_gate_ok AND unit_capacity_gate_ok

if external key label differs from admitted_key:
  edge is not admitted to the canonical graph
  if it is still used as a return:
    MaterializedCircuitCanonicalCrossKeyReturnWhitelistLeakPDECCap
```

因此 noncanonical key label residue 不能作为独立活动出口保留。外部标签被
擦除；若它仍然产生跨 key return 作用，则它不是新的 key 自由度，而是
canonical cross-key return whitelist leak。

本步没有证明 missing-unit coordinate slot mismatch，也没有证明 singleton Hall cut、
cross-key return whitelist leak、payment graph 全局闭合或 return whitelist；
行/列命题仍未无条件闭合。

### 1.139 stable-ladder phase-residue exchange canonical-payment-same-cell-slot-admission 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_same_cell_slot_admission_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-same-cell-slot-admission-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-same-cell-slot-admission-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-same-cell-slot-admission-router.json
```

同步读数为：

```text
phase_residue_exchange_missing_unit_coordinate_slot_mismatch_imported=true
phase_residue_exchange_missing_unit_coordinate_slot_mismatch_occurrences_removed=2
phase_residue_exchange_key_label_admission_lock_imported=true
phase_residue_exchange_same_cell_claim_requires_slot_vector_closed=true
phase_residue_exchange_slot_vector_equality_gate_closed=true
phase_residue_exchange_slot_mismatch_not_same_cell_edge_closed=true
phase_residue_exchange_counted_slot_mismatch_assignment_incidence_closed=true
phase_residue_exchange_uncounted_slot_mismatch_singleton_cut_closed=true
phase_residue_exchange_no_independent_slot_mismatch_closed=true
phase_residue_exchange_missing_unit_coordinate_slot_mismatch_pdec_cap_proved=true
phase_residue_exchange_unit_capacity_assignment_incidence_proved=false
phase_residue_exchange_canonical_singleton_hall_cut_defect_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：补偿边若声称支付同一 canonical missing unit cell，
就必须逐槽相等：

```text
if compensator claims the same canonical missing unit cell:
  require equal slot_vector(source, occurrence, CRT, congruence, endpoint, signed_amount)

if slot_vector differs:
  edge is not an admitted same-cell payment
  if it is counted as capacity:
    MaterializedCircuitUnitCapacityAssignmentIncidencePDECCap
  else:
    MaterializedCircuitCanonicalUnitSingletonHallCutDefectPDECCap
```

因此 missing-unit coordinate slot mismatch 不再是独立活动出口。错槽边要么
不能补该 cell，单点 Hall cut 继续暴露；要么被错误计入容量，回流
unit-capacity assignment incidence。

本步没有证明 assignment incidence，也没有证明 singleton Hall cut、cross-key
return whitelist leak、payment graph 全局闭合或 return whitelist；行/列命题仍未
无条件闭合。

### 1.140 stable-ladder phase-residue exchange canonical-payment-assignment-incidence-lock 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_assignment_incidence_lock_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-assignment-incidence-lock-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-assignment-incidence-lock-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-assignment-incidence-lock-router.json
```

同步读数为：

```text
phase_residue_exchange_unit_capacity_assignment_incidence_imported=true
phase_residue_exchange_same_cell_slot_admission_imported=true
phase_residue_exchange_counted_capacity_unit_closed=true
phase_residue_exchange_admitted_capacity_unit_predicate_closed=true
phase_residue_exchange_capacity_unit_value_one_gate_closed=true
phase_residue_exchange_assignment_actual_object_gate_closed=true
phase_residue_exchange_assignment_same_cell_gate_closed=true
phase_residue_exchange_assignment_whitelist_gate_closed=true
phase_residue_exchange_assignment_partial_injection_closed=true
phase_residue_exchange_bad_counted_unit_trichotomy_closed=true
phase_residue_exchange_no_independent_assignment_incidence_closed=true
phase_residue_exchange_unit_capacity_assignment_incidence_proved=true
phase_residue_exchange_actual_object_incidence_predicate_proved=false
phase_residue_exchange_capacity_value_unit_integrality_proved=false
phase_residue_exchange_canonical_singleton_hall_cut_defect_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：任何 counted capacity unit 必须先通过 admitted-unit
谓词：

```text
admitted_capacity_unit = actual_object_gate AND unit_value_one_gate
                         AND same_cell_gate AND whitelist_gate

if a counted capacity unit fails a gate:
  actual_object_gate failure -> ActualObjectIncidencePredicatePDECCap
  unit_value_one failure     -> CapacityValueUnitIntegralityPDECCap
  whitelist_gate failure     -> CanonicalCrossKeyReturnWhitelistLeakPDECCap
  otherwise remove the bad count -> CanonicalUnitSingletonHallCutDefectPDECCap
```

因此 unit-capacity assignment incidence 不再是独立活动出口。通过所有 gate 的
容量单位形成到需求单位集合的部分单射；坏计数只会回流到对象、单位值、
白名单或单点 Hall cut 出口。

本步没有证明 actual-object incidence、capacity integrality、singleton Hall cut、
cross-key return whitelist leak、payment graph 全局闭合或 return whitelist；
行/列命题仍未无条件闭合。

### 1.141 stable-ladder phase-residue exchange canonical-payment-capacity-unit-value-lock 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_capacity_unit_value_lock_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-capacity-unit-value-lock-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-capacity-unit-value-lock-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-capacity-unit-value-lock-router.json
```

同步读数为：

```text
phase_residue_exchange_capacity_value_unit_integrality_imported=true
phase_residue_exchange_assignment_incidence_lock_imported=true
phase_residue_exchange_signed_amount_unit_atom_closed=true
phase_residue_exchange_unit_value_one_normalization_closed=true
phase_residue_exchange_capacity_as_unit_indicator_sum_closed=true
phase_residue_exchange_capacity_integer_sum_closed=true
phase_residue_exchange_nonunit_value_actual_object_return_closed=true
phase_residue_exchange_bad_unit_value_singleton_cut_closed=true
phase_residue_exchange_no_independent_capacity_integrality_closed=true
phase_residue_exchange_capacity_value_unit_integrality_proved=true
phase_residue_exchange_actual_object_incidence_predicate_proved=false
phase_residue_exchange_canonical_singleton_hall_cut_defect_pdec_cap_proved=false
phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：admitted capacity value 不再是独立实数或未命名容量，
而是 admitted unit indicators 的有限和：

```text
capacity_value = sum_{admitted units u} 1_u

if a capacity unit has non-unit signed amount:
  ActualObjectIncidencePredicatePDECCap
else if the bad unit is removed from capacity:
  CanonicalUnitSingletonHallCutDefectPDECCap
```

因此 capacity-value unit-integrality 不再是独立活动出口。通过 assignment
incidence lock 的 admitted unit 已经带有 unit-value-one gate；每一项都是
0/1 指示，有限和自动是非负整数。非一单位 signed amount 不能伪装成半个容量
或多重容量，它只能回流 actual-object gate；剔除后同一 canonical cell 的
singleton Hall cut 赤字仍然暴露。

本步没有证明 actual-object incidence、singleton Hall cut、cross-key return
whitelist leak、payment graph 全局闭合或 return whitelist；也没有排斥 boundary
equality atom 或 endpoint 并行出口。行/列命题仍未无条件闭合。

### 1.142 stable-ladder phase-residue exchange canonical-payment-actual-object-field-packet-lock 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_actual_object_field_packet_lock_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-field-packet-lock-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-field-packet-lock-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-field-packet-lock-router.json
```

同步读数为：

```text
phase_residue_exchange_actual_object_incidence_predicate_imported=true
phase_residue_exchange_capacity_unit_value_lock_imported=true
phase_residue_exchange_actual_object_predicate_router_imported=true
phase_residue_exchange_actual_object_tuple_schema_imported=true
phase_residue_exchange_actual_object_canonical_hash_imported=true
phase_residue_exchange_actual_object_field_packet_partition_closed=true
phase_residue_exchange_no_independent_actual_object_predicate_closed=true
phase_residue_exchange_actual_object_incidence_predicate_proved=true
phase_residue_exchange_actual_object_field_packet_exits_proved=false
phase_residue_exchange_canonical_singleton_hall_cut_defect_pdec_cap_proved=false
phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：actual object 不再是一个可匿名失败的黑箱谓词，而是
canonical tuple/hash 上的字段包：

```text
actual_object = canonical_tuple(source, occurrence, CRT, congruence,
                                phase, signed_mass, pairing)

if actual object is missing or duplicated:
  ActualObjectMissingFieldPDECCap or ActualObjectDuplicateFieldPDECCap
else if any tuple field fails:
  the matching ActualObject<Field>FieldPDECCap
else:
  actual-object incidence predicate is satisfied
```

因此 `ActualObjectIncidencePredicatePDECCap` 不再作为单一匿名出口保留。它被
拆成 missing、duplicate、source、occurrence、CRT、congruence、phase、
signed-mass 与 pairing 九个字段级出口。

本步没有排斥这些字段级出口，也没有证明 singleton Hall cut、cross-key return
whitelist leak、payment graph 全局闭合、return whitelist、boundary equality atom
或 endpoint 并行出口。行/列命题仍未无条件闭合。

### 1.143 stable-ladder phase-residue exchange canonical-payment-actual-object-slot-mismatch-unification 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_actual_object_slot_mismatch_unification_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-slot-mismatch-unification-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-slot-mismatch-unification-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-slot-mismatch-unification-router.json
```

同步读数为：

```text
phase_residue_exchange_actual_object_named_field_exits_imported=true
phase_residue_exchange_actual_object_field_packet_lock_imported=true
phase_residue_exchange_actual_object_slot_mismatch_return_imported=true
phase_residue_exchange_actual_object_slot_vector_closed=true
phase_residue_exchange_actual_object_slot_mismatch_union_closed=true
phase_residue_exchange_actual_object_field_failure_to_slot_mismatch_closed=true
phase_residue_exchange_no_independent_actual_object_named_field_exits_closed=true
phase_residue_exchange_actual_object_missing_field_pdec_cap_proved=false
phase_residue_exchange_actual_object_duplicate_field_pdec_cap_proved=false
phase_residue_exchange_actual_object_slot_mismatch_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：actual object 的七个谓词槽位失败不再各自作为独立出口；
它们统一等价为同一个 canonical slot vector 的某槽不匹配：

```text
actual_object_slot_vector = (source, occurrence, CRT, congruence,
                             phase, signed_mass, pairing)

missing object   -> ActualObjectMissingFieldPDECCap
duplicate object -> ActualObjectDuplicateFieldPDECCap
any slot failure -> ActualObjectSlotMismatchPDECCap
```

因此 actual-object 字段硬点被压缩为三分支：缺对象、重对象、换槽。

本步没有排斥 missing、duplicate 或 slot mismatch，也没有证明 singleton Hall cut、
cross-key return whitelist leak、boundary equality atom 或 endpoint 并行出口。行/列命题
仍未无条件闭合。

### 1.144 stable-ladder phase-residue exchange canonical-payment-actual-object-admission-trichotomy 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_actual_object_admission_trichotomy_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-admission-trichotomy-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-admission-trichotomy-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-admission-trichotomy-router.json
```

同步读数为：

```text
phase_residue_exchange_actual_object_admission_defects_imported=true
phase_residue_exchange_actual_object_slot_mismatch_unification_imported=true
phase_residue_exchange_assignment_incidence_lock_imported=true
phase_residue_exchange_missing_object_not_admitted_capacity_closed=true
phase_residue_exchange_slot_mismatch_not_same_cell_capacity_closed=true
phase_residue_exchange_duplicate_object_collision_or_whitelist_closed=true
phase_residue_exchange_bad_object_edge_removal_singleton_cut_closed=true
phase_residue_exchange_no_independent_actual_object_admission_defect_closed=true
phase_residue_exchange_actual_object_missing_field_pdec_cap_proved=true
phase_residue_exchange_actual_object_duplicate_field_pdec_cap_proved=true
phase_residue_exchange_actual_object_slot_mismatch_pdec_cap_proved=true
phase_residue_exchange_canonical_singleton_hall_cut_defect_pdec_cap_proved=false
phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：对象侧三分支不再是独立 capacity 出口：

```text
missing object   -> not admitted capacity -> singleton Hall cut
slot mismatch    -> not same-cell admitted capacity -> singleton Hall cut
duplicate object -> same-key duplicate adds no capacity, or cross-key whitelist leak
```

因此 actual-object admission 缺陷只会回到 singleton Hall cut 或 cross-key whitelist
leak；它们不再作为独立活动出口保留。

本步没有证明 singleton Hall cut 或 cross-key return whitelist leak，也没有排斥
boundary equality atom 或 endpoint 并行出口。行/列命题仍未无条件闭合。

### 1.145 stable-ladder phase-residue exchange canonical-payment-singleton-cut-return-admission-lock 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_singleton_cut_return_admission_lock_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-singleton-cut-return-admission-lock-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-singleton-cut-return-admission-lock-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-singleton-cut-return-admission-lock-router.json
```

同步读数为：

```text
phase_residue_exchange_singleton_hall_cut_defect_imported=true
phase_residue_exchange_actual_object_admission_trichotomy_imported=true
phase_residue_exchange_singleton_cut_router_imported=true
phase_residue_exchange_singleton_cut_balance_imported=true
phase_residue_exchange_same_key_capacity_empty_imported=true
phase_residue_exchange_singleton_return_admission_partition_closed=true
phase_residue_exchange_same_key_return_no_new_capacity_closed=true
phase_residue_exchange_cross_key_return_whitelist_gate_closed=true
phase_residue_exchange_legal_return_named_boundary_registered=true
phase_residue_exchange_singleton_no_return_hall_atom_registered=true
phase_residue_exchange_no_independent_broad_singleton_hall_cut_defect_closed=true
phase_residue_exchange_canonical_singleton_no_return_hall_atom_pdec_cap_proved=false
phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：旧 singleton-cut 证书给出单点 cut 的需求为 1、同 key
容量为 0；actual-object admission 证书排除了坏对象边作为独立容量。于是任何补偿尝试只
能落入四类：

```text
same-key duplicate -> no new capacity
bad actual-object edge -> already routed by actual-object admission
cross-key return not whitelisted -> cross-key whitelist leak
no legal named return -> CanonicalUnitSingletonNoReturnHallAtomPDECCap
```

因此 broad singleton Hall cut 不再作为独立出口保留；它被压成 no-return Hall atom，
或回到 cross-key whitelist leak、boundary equality/endpoint return 出口。

本步没有证明 no-return Hall atom，也没有排斥 cross-key return whitelist leak、
boundary equality atom 或 endpoint 并行出口。行/列命题仍未无条件闭合。

### 1.146 stable-ladder phase-residue exchange canonical-payment-singleton-no-return-endpoint-projection 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_singleton_no_return_endpoint_projection_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-singleton-no-return-endpoint-projection-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-singleton-no-return-endpoint-projection-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-singleton-no-return-endpoint-projection-router.json
```

同步读数为：

```text
phase_residue_exchange_singleton_no_return_hall_atom_imported=true
phase_residue_exchange_actual_object_field_packet_imported_for_no_return_projection=true
phase_residue_exchange_no_return_singleton_unit_key_closed=true
phase_residue_exchange_no_return_phase_endpoint_projection_closed=true
phase_residue_exchange_no_return_signed_mass_unit_projection_closed=true
phase_residue_exchange_no_return_source_multiplicity_gate_closed=true
phase_residue_exchange_no_independent_singleton_no_return_hall_atom_closed=true
endpoint_singleton_atom_sae_proved=false
source_atom_multiplicity_cap_pdec_cap_proved=false
phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：no-return Hall atom 已不再是 payment 图黑箱。actual-object
字段包锁定 source、occurrence、phase endpoint 与 signed mass；投影到 endpoint 后，
若无多 source/occurrence 补偿，就是 endpoint singleton atom SAE；若有多重补偿，
则是 source-atom multiplicity cap。

因此 payment 侧 no-return atom 不再作为独立活动出口保留。

本步没有证明 endpoint singleton atom SAE 或 source-atom multiplicity cap，也没有排斥
cross-key return whitelist leak、boundary equality atom 或 endpoint 并行出口。行/列命题
仍未无条件闭合。

### 1.147 stable-ladder phase-residue exchange canonical-payment-cross-key-return-whitelist-slot-projection 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_cross_key_return_whitelist_slot_projection_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-cross-key-return-whitelist-slot-projection-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-cross-key-return-whitelist-slot-projection-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-cross-key-return-whitelist-slot-projection-router.json
```

同步读数为：

```text
phase_residue_exchange_cross_key_return_whitelist_leak_imported=true
phase_residue_exchange_actual_object_slot_vector_imported_for_cross_key_return=true
phase_residue_exchange_cross_key_return_unit_pair_closed=true
phase_residue_exchange_cross_key_return_slot_change_partition_closed=true
phase_residue_exchange_no_independent_cross_key_return_whitelist_leak_closed=true
source_atom_multiplicity_cap_pdec_cap_proved=false
phase_residue_exchange_boundary_equality_atom_exclusion_proved=false
endpoint_orbit_bridge_cancellation_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：跨 key 非白名单 return 不能作为 payment 图匿名逃逸。
actual-object slot vector 已固定；若它不是同一对象，则至少一个槽位变化：

```text
source/occurrence change -> source-atom multiplicity cap
CRT/congruence change    -> boundary equality/CRT boundary
phase endpoint change    -> bridge, amplitude-depth, or variation-boundary flux
signed/pairing change    -> full-cycle mean or amplitude-depth
```

因此 cross-key return whitelist leak 不再作为独立活动出口保留。

本步没有证明 source multiplicity、boundary equality、endpoint orbit 或 sparse SAE 出口。
行/列命题仍未无条件闭合。

### 1.148 stable-ladder phase-residue exchange boundary-equality-critical-endpoint-projection 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_boundary_equality_critical_endpoint_projection_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-boundary-equality-critical-endpoint-projection-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-boundary-equality-critical-endpoint-projection-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-boundary-equality-critical-endpoint-projection-router.json
```

同步读数为：

```text
phase_residue_exchange_boundary_equality_atom_imported=true
phase_residue_exchange_slack_sign_imported_for_boundary_equality=true
phase_residue_exchange_boundary_equality_zero_slack_actual_object_closed=true
phase_residue_exchange_boundary_equality_critical_facet_closed=true
phase_residue_exchange_boundary_equality_first_variation_partition_closed=true
phase_residue_exchange_no_independent_boundary_equality_atom_closed=true
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
endpoint_orbit_amplitude_depth_pdec_cap_proved=false
endpoint_orbit_variation_boundary_flux_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：`Sigma(O)=0` 只说明同一 actual object 落在 active facet 的临界面，
不能当作严格矛盾，也不能作为匿名出口保留。它必须投影为：

```text
constant endpoint phase -> full-cycle mean atom
nonzero amplitude depth -> amplitude-depth exit
boundary sustaining flux -> variation-boundary flux exit
```

因此 boundary equality atom 不再作为独立活动出口保留。

本步没有证明 full-cycle mean、amplitude-depth、variation-boundary flux、endpoint singleton、
source multiplicity 或 sparse SAE。行/列命题仍未无条件闭合。

### 1.149 stable-ladder phase-residue exchange endpoint-dynamic-signed-depth-flux-packet 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_endpoint_dynamic_signed_depth_flux_packet_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-dynamic-signed-depth-flux-packet-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-dynamic-signed-depth-flux-packet-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-dynamic-signed-depth-flux-packet-router.json
```

同步读数为：

```text
endpoint_dynamic_bridge_amplitude_variation_imported=true
phase_residue_exchange_boundary_equality_projection_imported_for_dynamic_packet=true
endpoint_orbit_dynamic_signed_endpoint_measure_closed=true
endpoint_orbit_dynamic_packet_zero_mean_reduction_closed=true
endpoint_orbit_signed_depth_flux_decomposition_closed=true
endpoint_orbit_signed_depth_flux_packet_registered=true
endpoint_orbit_no_independent_bridge_amplitude_variation_closed=true
endpoint_orbit_signed_depth_flux_packet_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：boundary/payment 独立出口移除后，bridge cancellation、
amplitude-depth 与 variation-boundary flux 都是同一个 endpoint signed-depth/flux 测度
的三种投影：

```text
opposite-sign cancellation -> bridge component
same-sign positive depth   -> amplitude-depth component
boundary transport flux    -> variation-boundary component
```

因此三个 endpoint 动态出口不再作为三条并行独立出口保留，而是统一为
`EndpointOrbitSignedDepthFluxPacketPDECCap`。

本步没有证明 signed-depth/flux packet、endpoint singleton、full-cycle mean、
source multiplicity 或 sparse SAE。行/列命题仍未无条件闭合。

### 1.150 stable-ladder phase-residue exchange endpoint-signed-depth-flux-cycle-skeleton 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_endpoint_signed_depth_flux_cycle_skeleton_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-signed-depth-flux-cycle-skeleton-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-signed-depth-flux-cycle-skeleton-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-signed-depth-flux-cycle-skeleton-router.json
```

同步读数为：

```text
endpoint_orbit_signed_depth_flux_packet_imported=true
endpoint_signed_depth_flux_finite_support_skeleton_closed=true
endpoint_signed_depth_flux_unit_atom_expansion_closed=true
endpoint_signed_depth_flux_zero_mean_balance_closed=true
endpoint_signed_depth_flux_pairing_graph_closed=true
endpoint_signed_depth_flux_acyclic_leaf_return_closed=true
endpoint_signed_depth_flux_packet_reduced_to_alternating_cycle=true
endpoint_signed_depth_flux_alternating_transport_cycle_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：`EndpointOrbitSignedDepthFluxPacketPDECCap` 不能继续作为
匿名整包出口。finite CRT endpoint support 上的零均值 signed unit atoms 形成有限
pairing graph；若该图无交替环，则叶剥离必回到 endpoint singleton、full-cycle mean
或 source multiplicity。因此剩余非匿名硬点只能登记为
`EndpointOrbitSignedDepthFluxAlternatingTransportCyclePDECCap`。

本步没有证明 alternating transport cycle、endpoint singleton、full-cycle mean、
source multiplicity 或 sparse SAE。行/列命题仍未无条件闭合。

### 1.151 stable-ladder phase-residue exchange endpoint-alternating-cycle-monodromy-lock 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_endpoint_alternating_cycle_monodromy_lock_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-monodromy-lock-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-monodromy-lock-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-monodromy-lock-router.json
```

同步读数为：

```text
endpoint_alternating_transport_cycle_imported=true
endpoint_alternating_cycle_ordered_support_closed=true
endpoint_alternating_cycle_signed_edge_incidence_closed=true
endpoint_alternating_cycle_boundary_zero_closed=true
endpoint_alternating_cycle_crt_phase_increment_word_closed=true
endpoint_alternating_cycle_monodromy_dichotomy_closed=true
endpoint_alternating_cycle_zero_monodromy_circulation_return_closed=true
endpoint_alternating_cycle_reduced_to_nonzero_monodromy=true
endpoint_alternating_cycle_monodromy_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：alternating transport cycle 已经不是匿名环出口。它被写成
有序 CRT endpoint cycle、signed edge incidence 与相位增量词；零 monodromy 是边界为零
的纯环流，不能形成 endpoint load defect。剩余只能是
`EndpointOrbitSignedDepthFluxAlternatingCycleMonodromyPDECCap`。

本步没有证明 nonzero monodromy、endpoint singleton、full-cycle mean、source
multiplicity 或 sparse SAE。行/列命题仍未无条件闭合。

### 1.152 stable-ladder phase-residue exchange endpoint-alternating-cycle-pivot-phase-slip 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_endpoint_alternating_cycle_pivot_phase_slip_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-router.json
```

同步读数为：

```text
endpoint_alternating_cycle_monodromy_imported=true
endpoint_alternating_cycle_monodromy_crt_vector_closed=true
endpoint_alternating_cycle_nonzero_crt_coordinate_localized=true
endpoint_alternating_cycle_pivot_prime_selected=true
endpoint_alternating_cycle_monodromy_reduced_to_pivot_phase_slip=true
endpoint_alternating_cycle_pivot_prime_phase_slip_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：nonzero monodromy 不再作为匿名整体出口。它在有限 CRT
prime-coordinate 向量中至少有一个非零坐标；取最小非零素模坐标作为规范 pivot，
最新硬点就是该 pivot prime 上的非零 phase-slip。

本步没有证明 pivot phase-slip、endpoint singleton、full-cycle mean、source
multiplicity 或 sparse SAE。行/列命题仍未无条件闭合。

### 1.153 stable-ladder phase-residue exchange endpoint-pivot-phase-slip-LCM-support-barrier 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_endpoint_alternating_cycle_pivot_phase_slip_lcm_support_barrier_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-lcm-support-barrier-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-lcm-support-barrier-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-lcm-support-barrier-router.json
```

同步读数为：

```text
endpoint_pivot_phase_slip_imported=true
endpoint_pivot_prime_phase_motion_formula_closed=true
endpoint_pivot_fixed_set_lcm_replay_period_closed=true
endpoint_pivot_support_width_registered=true
endpoint_pivot_lcm_exceeds_support_no_fixed_replay=true
endpoint_pivot_phase_slip_reduced_to_lcm_support_barrier=true
endpoint_pivot_small_lcm_branch_excluded=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：pivot-prime phase-slip 不再作为匿名单出口保留。固定非零
素模滑移若以同一 pivot 标签复现，replay 位移 `d` 必须满足 `q|d`；固定 pivot
标签集则要求 `lcm(Lambda)|d`。若该 LCM 超过 endpoint cycle 的有限支撑宽度 `W`，
则没有非零固定复现；若 `L<=W`，只剩小 LCM/ColumnCRT/PDEC 分支；逃避固定标签
的情形登记为 moving-pivot PDEC/SAE。

本步没有证明小 LCM pivot 分支、nonreplay sparse SAE、moving-pivot PDEC、
endpoint singleton、full-cycle mean、source multiplicity 或 sparse SAE。
行/列命题仍未无条件闭合。

### 1.154 stable-ladder phase-residue exchange endpoint-pivot-small-LCM-rank-pressure 更新

新增机器证书：

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_endpoint_alternating_cycle_pivot_phase_slip_small_lcm_rank_pressure_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-small-lcm-rank-pressure-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-small-lcm-rank-pressure-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-small-lcm-rank-pressure-router.json
```

同步读数为：

```text
endpoint_pivot_small_lcm_imported=true
endpoint_pivot_distinct_prime_product_law_closed=true
endpoint_pivot_small_lcm_rank_pressure_closed=true
endpoint_pivot_two_large_carrier_sqrt_barrier_closed=true
endpoint_pivot_small_lcm_reduced_to_rank_pressure=true
endpoint_pivot_low_carrier_fixed_residue_pdec_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：endpoint pivot small-LCM 分支不再是宽口径
ColumnCRT/PDEC 出口。固定 pivot 标签集满足 `L=lcm(Lambda)<=W`；对任意阈值
`B>1`，高 carrier 数 `r_B` 满足 `r_B<=floor(log W/log B)`。特别地，两个
`q>sqrt(W)` 的 pivot carrier 不能同处一个 fixed small-LCM unit。剩余压力必须
进入低 carrier fixed-residue、低 carrier 非持久 sparse，或高 carrier 低秩容量缺口。

本步没有证明低 carrier fixed-residue、低 carrier sparse、高 carrier rank-deficit、
nonreplay sparse、moving-pivot、endpoint singleton、full-cycle mean、source
multiplicity 或 sparse SAE。行/列命题仍未无条件闭合。

### 1.155 stable-ladder phase-residue exchange endpoint-pivot-low-carrier-fixed-residue-AP-envelope 更新

新增机器证书：

```text
experiments/prime_matrix_endpoint_pivot_low_carrier_fixed_residue_ap_table_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-low-carrier-fixed-residue-ap-table-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-low-carrier-fixed-residue-ap-table-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-low-carrier-fixed-residue-ap-table-router.json
```

同步读数为：

```text
endpoint_pivot_low_carrier_fixed_residue_imported=true
endpoint_pivot_boundary_carrier_degeneracy_closed=true
endpoint_pivot_residue_to_row_ap_formula_closed=true
endpoint_pivot_selected_table_exact_envelope_closed=true
endpoint_pivot_low_carrier_fixed_residue_reduced_to_ap_envelope=true
endpoint_pivot_actual_demand_lower_bound_proved=false
endpoint_pivot_low_carrier_fixed_residue_excluded=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：endpoint pivot low-carrier fixed-residue 不再作为匿名
ColumnCRT/PDEC 出口保留。对 `q<P`，固定 residue `a` 强制 endpoint 行坐标
`t==-aP^{-1} mod q`，长度 `H` 的窗口内单 cell 至多给出 `ceil(H/q)` 个命中；
固定 `q` 的全部 residue cell 总量精确为 `H`。`q=P` 的边界 carrier 不进入
AP 公式，而退化到既有 ColumnCRT 或 endpoint singleton/source-multiplicity 出口。

本步没有证明 endpoint actual demand 下界、AP strict gap、dense-table PDEC、
sparse-cell SAE、低 carrier nonpersistent sparse、高 carrier rank-deficit、nonreplay、
moving-pivot、endpoint singleton、full-cycle mean、source multiplicity 或 sparse SAE。
行/列命题仍未无条件闭合。

### 1.156 stable-ladder phase-residue exchange endpoint-pivot-actual-demand-source-cut 更新

新增机器证书：

```text
experiments/prime_matrix_endpoint_pivot_actual_demand_source_cut_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-actual-demand-source-cut-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-actual-demand-source-cut-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-actual-demand-source-cut-router.json
```

同步读数为：

```text
endpoint_actual_demand_imported=true
endpoint_unit_incidence_demand_closed=true
endpoint_unit_demand_not_gap_sufficient=true
endpoint_no_ap_envelope_recycling_guard=true
endpoint_actual_demand_reduced_to_source_cut=true
endpoint_release_mass_amplification_proved=false
endpoint_low_carrier_payment_injection_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：endpoint actual demand 不能继续作为匿名下界口。活跃
fixed-residue demand 至少给出一个 source-tagged endpoint incidence，但单位需求
不足以超过 AP exact-envelope；actual demand 必须来自源侧释放质量沿 endpoint orbit
的放大，并且非循环地注入同一低 carrier AP table。

本步没有证明 release-mass amplification、low-carrier payment injection、AP strict
gap、dense-table PDEC、sparse-cell SAE、低 carrier sparse、高 carrier rank-deficit、
nonreplay、moving-pivot、endpoint singleton、full-cycle mean、source multiplicity
或 sparse SAE。行/列命题仍未无条件闭合。

### 1.157 stable-ladder phase-residue exchange endpoint-pivot-release-mass-support-ladder 更新

新增机器证书：

```text
experiments/prime_matrix_endpoint_pivot_release_mass_support_ladder_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-release-mass-support-ladder-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-release-mass-support-ladder-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-release-mass-support-ladder-router.json
```

同步读数为：

```text
endpoint_release_mass_amplification_imported=true
endpoint_unit_release_not_amplification_closed=true
endpoint_release_source_finite_support_closed=true
endpoint_source_support_mass_ledger_closed=true
endpoint_source_support_threshold_dichotomy_closed=true
endpoint_release_mass_reduced_to_support_ladder=true
endpoint_long_source_support_mass_transfer_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：release-mass amplification 不再是匿名出口。单位源点不能
产生 AP envelope gap；释放质量只能来自 signed-depth/flux skeleton 的有限
source-tagged unit support。短支撑进入 endpoint singleton/full-cycle/source-multiplicity
或 sparse SAE；长支撑才可能转移为 low-carrier AP demand，转移失败则是 PDEC/SAE。

本步没有证明 bounded support SAE、long support mass-transfer、payment injection、
AP strict gap、dense-table PDEC、sparse-cell SAE、高秩、nonreplay、moving-pivot
或 endpoint 并行出口。行/列命题仍未无条件闭合。

### 1.158 stable-ladder phase-residue exchange endpoint-pivot-low-carrier-payment-injection-lock 更新

新增机器证书：

```text
experiments/prime_matrix_endpoint_pivot_low_carrier_payment_injection_lock_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-low-carrier-payment-injection-lock-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-low-carrier-payment-injection-lock-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-low-carrier-payment-injection-lock-router.json
```

同步读数为：

```text
endpoint_low_carrier_payment_injection_imported=true
endpoint_no_envelope_reuse_guard_imported=true
endpoint_same_ap_table_key_tuple_closed=true
endpoint_canonical_assignment_incidence_imported=true
endpoint_no_hidden_cross_key_payment_imported=true
endpoint_no_loss_return_accounting_imported=true
endpoint_same_ap_table_payment_injection_lock_registered=true
endpoint_payment_injection_reduced_to_lock=true
endpoint_same_ap_table_payment_injection_lock_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：low-carrier payment injection 不再是匿名注入口。有效支付
不能复用 AP envelope，必须落到同一 endpoint packet、pivot prime、residue、row AP
class、窗口和 source atom 形成的 canonical same-AP-table key。跨 key 或跨表支付进入
cross-table switch/PDEC 或 moving-pivot；同槽重复支付进入 duplicate-payment collision
或 sparse SAE。

本步没有证明同表 payment injection 存在或足量，也没有排斥 cross-table switch、
duplicate collision、bounded support、long support mass-transfer、AP strict gap、
dense-table、sparse-cell、高秩、nonreplay、moving-pivot 或 endpoint 并行出口。
行/列命题仍未无条件闭合。

### 1.159 stable-ladder phase-residue exchange endpoint-pivot-duplicate-payment-slot-accounting 更新

新增机器证书：

```text
experiments/prime_matrix_endpoint_pivot_duplicate_payment_slot_accounting_router.py
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-duplicate-payment-slot-accounting-ledger.json
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-duplicate-payment-slot-accounting-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-duplicate-payment-slot-accounting-router.json
```

同步读数为：

```text
endpoint_duplicate_payment_imported=true
endpoint_duplicate_same_canonical_slot_key_closed=true
endpoint_duplicate_capacity_unit_value_imported=true
endpoint_duplicate_assignment_partial_injection_imported=true
endpoint_actual_object_duplicate_collision_imported=true
endpoint_duplicate_count_not_new_capacity_closed=true
endpoint_duplicate_payment_reduced_to_slot_accounting=true
endpoint_duplicate_same_slot_multiplicity_cap_pdec_proved=false
endpoint_duplicate_payment_sparse_sae_summability_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：duplicate payment 不能作为新增 AP-table capacity。合法支付
已经锁到 same-AP-table canonical slot，且 admitted slot 的容量值为一单位；同槽重复
只会变成同槽 source multiplicity cap/PDEC，或非持久 duplicate sparse SAE。

本步没有证明同槽 source multiplicity cap/PDEC，也没有证明 duplicate sparse SAE 求和。
same AP table injection、cross-table switch、bounded/long support、strict gap、
dense/sparse table、高秩、nonreplay、moving-pivot 与 endpoint 并行出口仍未排斥。
行/列命题仍未无条件闭合。

### 1.160 stable-ladder phase-residue exchange endpoint-pivot-duplicate-same-slot-multiplicity-cap-import 更新

新增机器证书：

```text
experiments/prime_matrix_endpoint_pivot_duplicate_same_slot_multiplicity_cap_import_router.py
data/prime-matrix-endpoint-pivot-duplicate-same-slot-multiplicity-cap-import-ledger.json
docs/monograph/prime-matrix-endpoint-pivot-duplicate-same-slot-multiplicity-cap-import-router.md
docs/monograph/prime-matrix-endpoint-pivot-duplicate-same-slot-multiplicity-cap-import-router.json
```

同步读数为：

```text
endpoint_duplicate_same_slot_multiplicity_imported=true
endpoint_duplicate_same_slot_key_carries_source_atom=true
endpoint_duplicate_extra_unit_same_source_atom_closed=true
endpoint_duplicate_multiplicity_no_new_payment_capacity=true
existing_source_atom_multiplicity_cap_imported=true
endpoint_duplicate_same_slot_multiplicity_reduced_to_existing_cap=true
source_atom_multiplicity_cap_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：duplicate same-slot source multiplicity 不再作为 endpoint
专属独立出口。上一层 same canonical slot key 已固定 source-support atom；同槽额外
source unit 不能增加 AP-table payment capacity，只能解释为该 source atom 的持久重数
异常。因此该分支并入既有
`EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCap`。

本步没有证明 source-atom multiplicity cap/PDEC，也没有证明 duplicate sparse SAE、
same AP table injection、cross-table switch、bounded/long support、AP strict gap/dense
table、sparse cell、高秩、nonreplay、moving-pivot 或 endpoint 并行出口。行/列命题
仍未无条件闭合。

### 1.161 source-atom multiplicity-cap ExactUV fixed-key bridge 更新

新增机器证书：

```text
experiments/prime_matrix_source_atom_multiplicity_cap_exactuv_fixed_key_bridge_router.py
data/prime-matrix-source-atom-multiplicity-cap-exactuv-fixed-key-bridge-ledger.json
docs/monograph/prime-matrix-source-atom-multiplicity-cap-exactuv-fixed-key-bridge-router.md
docs/monograph/prime-matrix-source-atom-multiplicity-cap-exactuv-fixed-key-bridge-router.json
```

同步读数为：

```text
source_atom_multiplicity_cap_imported=true
source_atom_multiplicity_cap_packet_registered=true
source_atom_multiplicity_same_source_key_field_closed=true
exactuv_source_atom_implication_imported=true
strict_source_atomization_imported=true
actual_noncanonical_primitive_emitter_source_table_proved=false
complete_primitive_emitter_key_partition_ledger_proved=false
fixed_key_exact_uv_local_multiplicity_o1_ledger_proved=false
source_atom_multiplicity_cap_reduced_to_exactuv_fixed_key_atoms=true
source_atom_multiplicity_cap_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：source-atom multiplicity cap 不再作为 endpoint 局部独立口径。
同一 source atom 的大重数若要成为真实反例，必须先有 actual noncanonical primitive
emitter source table，再有 complete key partition，最后由 fixed-key exact-UV local
multiplicity O(1) 排斥固定 key 下的大原像坍缩。因此该 cap 被桥接到 ExactUV
source-rank/no-collapse 三原子。

本步没有证明 actual emitter source table、complete key partition、fixed-key local
multiplicity O(1)、duplicate sparse SAE、payment injection、cross-table switch 或其他
endpoint 并行出口。行/列命题仍未无条件闭合。

### 1.162 LPF ownership sieve source declaration 更新

新增机器证书：

```text
experiments/prime_matrix_lpf_ownership_sieve_source_declaration_router.py
data/prime-matrix-lpf-ownership-sieve-source-declaration-ledger.json
docs/monograph/prime-matrix-lpf-ownership-sieve-source-declaration-router.md
docs/monograph/prime-matrix-lpf-ownership-sieve-source-declaration-router.json
```

同步读数为：

```text
ascending_lpf_ownership_partition_proved=true
prime_count_identity_from_lpf_ownership_proved=true
quotient_condition_matches_user_sieve_proved=true
lpf_ownership_unsigned_declaration_line_closed=true
lpf_ownership_to_signed_alpha_delta_lift_proved=false
explicit_alpha_delta_primitive_constructor_rule_proved=false
row_column_unconditional_closed=false
```

actual-load 含义是：升序最小素因子筛给出严格非重叠 ownership。对任意 `N`，
每个合数 `n<=N` 唯一落入 `p=LPF(n)` 的筛层；等价地，`p` 层新筛掉的数正是
`p*m<=N`、`m>=p` 且 `m` 没有小于 `p` 的素因子的数。因此
`pi(N)=N-1-sum_p LPF_p(N)` 是精确恒等式，并关闭 pre-Cauchy declaration line
中的 unsigned ownership 字段。

本步没有证明 signed `alpha/delta` primitive constructor rule、local factor、exact-UV
fixed-key multiplicity、actual emitter source table、complete key partition 或
DStructure/Rankin 验收。最新直接主攻转为
`ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter`。行/列命题仍未
无条件闭合。

### 1.163 LPF candidate-row map alpha-rule 更新

新增机器证书：

```text
experiments/prime_matrix_lpf_candidate_row_map_alpha_rule_router.py
data/prime-matrix-lpf-candidate-row-map-alpha-rule-ledger.json
docs/monograph/prime-matrix-lpf-candidate-row-map-alpha-rule-router.md
docs/monograph/prime-matrix-lpf-candidate-row-map-alpha-rule-router.json
```

同步读数为：

```text
alpha_side_primitive_rule_imported=true
deterministic_alpha_map_gap_imported=true
lpf_ownership_declaration_imported=true
lpf_candidate_row_emission_map_closed=true
pointwise_signed_alpha_value_table_proved=false
primitive_summand_signed_weight_expression_proved=false
row_column_unconditional_closed=false
```

actual-load 含义是：LPF ownership 不只给素数计数恒等式，也给 alpha-side primitive
rule 的非后验候选行索引。每个候选合数 row 由唯一最小素因子层 `p` 与 cofactor
`m` 确定，并与已有 carry-shell、P 列锚、phase rule、layered-wheel unsigned skeleton
兼容。

本步没有证明这些 candidate rows 已是 actual signed alpha primitive rows。真正缺口仍是
前推前逐行 signed summand 表达式、local factor、权重公式和失败回流。最新直接主攻为
`ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward`。行/列命题仍未
无条件闭合。

### 1.164 Phi-recursive LPF ownership 更新

新增机器证书：

```text
experiments/prime_matrix_phi_recursive_lpf_ownership_router.py
data/prime-matrix-phi-recursive-lpf-ownership-ledger.json
docs/monograph/prime-matrix-phi-recursive-lpf-ownership-router.md
docs/monograph/prime-matrix-phi-recursive-lpf-ownership-router.json
```

同步读数为：

```text
phi_rough_count_definition_proved=true
phi_recursion_identity_proved=true
phi_recursive_lpf_bucket_formula_proved=true
prime_count_identity_from_phi_lpf_proved=true
large_prime_layer_zero_mass_proved=true
sample_audit_all_passed=true
phi_recursive_ownership_to_signed_alpha_delta_lift_proved=false
primitive_summand_signed_weight_expression_proved=false
row_column_unconditional_closed=false
```

actual-load 含义是：LPF ownership 现在有了用户给出的 rough-count 递推读数。定义
`Phi(x,p)` 为 `1<=m<=x` 且所有素因子都不小于 `p` 的整数个数，包含 `m=1`。按是否
被 `p_k` 整除分拆，得到
`Phi(x,p_k)=Phi(x,p_{k+1})+Phi(floor(x/p_k),p_k)`；当 `p_k>x` 时只剩 `m=1`。
因此 `p` 层新筛合数数为 `c_N(p)=Phi(floor(N/p),p)-1`，且 `p>sqrt(N)` 时自动为零。

本层闭合的是无符号 ownership 容量递推。`N=10000` 审计给出 `pi(N)=1229`、合数桶和
`8770`，与精确恒等式一致。它仍不产生 signed coefficient、orientation、local factor
或 actual primitive summand 表达式；最新直接主攻保持为
`ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward`。行/列命题仍未
无条件闭合。

### 1.165 Phi-LPF support-stripped signed kernel 更新

新增机器证书：

```text
experiments/prime_matrix_phi_lpf_support_stripped_signed_kernel_router.py
data/prime-matrix-phi-lpf-support-stripped-signed-kernel-ledger.json
docs/monograph/prime-matrix-phi-lpf-support-stripped-signed-kernel-router.md
docs/monograph/prime-matrix-phi-lpf-support-stripped-signed-kernel-router.json
```

同步读数为：

```text
phi_recursive_lpf_ownership_imported=true
lpf_candidate_row_map_imported=true
phi_lpf_support_bijection_proved=true
support_and_capacity_components_closed=true
phi_lpf_bucket_signed_coefficient_law_proved=false
noncircular_signed_coefficient_emission_kernel_proved=false
row_column_unconditional_closed=false
```

actual-load 含义是：noncircular signed coefficient kernel 中的无符号支撑、容量和候选行
索引已被 Phi-LPF 层剥离。每个候选合数支撑键唯一为 `(p,m)`，其中 `p=LPF(pm)`，
`m` 为 p-rough，且容量由 `Phi(floor(N/p),p)-1` 给出。`N=10000` 审计中支撑键数
`8770` 与合数数 `8770` 一一对应。

本层没有证明 signed coefficient。最新缺口不再是找行、数行或证明 rough 容量，而是
对每个 Phi-LPF support key 正向赋 signed coefficient、sign/local factor、alpha/delta
侧、branch key、`(u,v)` 输出与推前前求和恒等式。最新直接主攻变为
`PhiLPFBucketSignedCoefficientLawBeforePushforward`。行/列命题仍未无条件闭合。

### 1.166 Phi-LPF bucket signed transport 更新

新增机器证书：

```text
experiments/prime_matrix_phi_lpf_bucket_signed_transport_router.py
data/prime-matrix-phi-lpf-bucket-signed-transport-ledger.json
docs/monograph/prime-matrix-phi-lpf-bucket-signed-transport-router.md
docs/monograph/prime-matrix-phi-lpf-bucket-signed-transport-router.json
```

同步读数为：

```text
phi_lpf_support_and_capacity_imported=true
unsigned_cofactor_split_identity_proved=true
signed_bucket_sum_partition_identity_proved=true
phi_lpf_rough_cofactor_signed_transport_law_proved=false
pointwise_phi_lpf_bucket_signed_value_table_proved=false
phi_lpf_bucket_signed_coefficient_law_proved=false
row_column_unconditional_closed=false
```

actual-load 含义是：Phi 递推在 signed 场景中继续给出精确支撑分裂。对 owner prime
`p` 和待证明系数 `a_p(m)`，

```text
sum_{m p-rough, 1<m<=x} a_p(m)
  = sum_{m p_next-rough, 1<m<=x} a_p(m)
    + sum_{m' p-rough, m'<=floor(x/p)} a_p(p*m')
```

这是有限求和恒等式，但它不生成 `a_p(p*m')` 的符号、local factor、branch 传输或
alpha/delta 侧。`N=10000` 审计中 `8770` 个 Phi-LPF support keys 分裂为 `5468` 个
next-rough 非整除项和 `3302` 个整除预像项。

因此最新硬点从泛化 bucket signed law 收窄为
`PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward`，等价并行入口为
`PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward`。行/列命题仍未
无条件闭合。

### 1.167 Phi-LPF signed transport unit-seed 更新

新增机器证书：

```text
experiments/prime_matrix_phi_lpf_signed_transport_unit_seed_router.py
data/prime-matrix-phi-lpf-signed-transport-unit-seed-ledger.json
docs/monograph/prime-matrix-phi-lpf-signed-transport-unit-seed-router.md
docs/monograph/prime-matrix-phi-lpf-signed-transport-unit-seed-router.json
```

同步读数为：

```text
phi_minus_one_prime_row_guard_imported=true
unit_preimage_square_seed_identity_proved=true
unit_seed_or_square_base_signed_coefficient_proved=false
rough_cofactor_step_local_factor_update_law_proved=false
rough_cofactor_ordered_factorization_coherence_proved=false
phi_lpf_rough_cofactor_signed_transport_law_proved=false
row_column_unconditional_closed=false
```

actual-load 含义是：Phi 公式中的 `-1` 不只是计数修正，也是 signed transport 的边界。
`m=1` 在 `Phi(floor(N/p),p)` 中对应 prime row `p`，所以必须从 composite support 中排除；
但 rough cofactor 乘法分支的 `m'=1` 又映到真实 composite key `(p,p)`，即 `p^2`。

因此递推 signed transport 不能从 Phi 计数自动启动；它必须显式给出 virtual-unit seed 或
square-base signed coefficient，并防止把 prime row `p` 后验偷换为 composite signed seed。
`N=10000` 审计中有 `25` 个 square-base seeds 和 `8745` 个 non-square support keys。

最新直接主攻为
`PhiLPFUnitCofactorVirtualSeedOrSquareBaseSignedCoefficientBeforePushforward`；即使该 seed
闭合，仍需 `PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward` 和
`PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward`。行/列命题仍未无条件闭合。

### 1.168 Phi-LPF square-base diagonal source 更新

新增机器证书：

```text
experiments/prime_matrix_phi_lpf_square_base_diagonal_source_router.py
data/prime-matrix-phi-lpf-square-base-diagonal-source-ledger.json
docs/monograph/prime-matrix-phi-lpf-square-base-diagonal-source-router.md
docs/monograph/prime-matrix-phi-lpf-square-base-diagonal-source-router.json
```

同步读数为：

```text
virtual_unit_not_composite_support_proved=true
square_base_minimal_support_root_proved=true
no_support_predecessor_below_square_base_proved=true
virtual_seed_collapses_to_square_base_declaration=true
square_base_diagonal_root_signed_source_declaration_proved=false
phi_lpf_rough_cofactor_signed_transport_law_proved=false
row_column_unconditional_closed=false
```

actual-load 含义是：`(p,1)` 是 Phi-LPF 公式减掉的 prime row，不是 composite support。
对 owner bucket `p`，不存在 `1<m<p` 且 `m` 为 `p`-rough 的真实 support cofactor；
所以最小真实 support key 是 `(p,p)`。transport 中的 virtual-unit 只能作为这个
square-base diagonal root 的声明前像出现，不能独立携带 composite signed coefficient。

因此最新直接主攻从
`PhiLPFUnitCofactorVirtualSeedOrSquareBaseSignedCoefficientBeforePushforward`
收窄为
`PhiLPFSquareBaseDiagonalRootSignedSourceDeclarationBeforePushforward`。仍需对 `(p,p)`
在推前前提交 source tuple、basis word、signed coefficient、orientation/local factor、
alpha/delta branch、ExactUV、prime-row leak guard 和 return tag。行/列命题仍未无条件闭合。

### 1.169 Phi-LPF square-base source packet reduction 更新

新增机器证书：

```text
experiments/prime_matrix_phi_lpf_square_base_source_packet_reduction_router.py
data/prime-matrix-phi-lpf-square-base-source-packet-reduction-ledger.json
docs/monograph/prime-matrix-phi-lpf-square-base-source-packet-reduction-router.md
docs/monograph/prime-matrix-phi-lpf-square-base-source-packet-reduction-router.json
```

同步读数为：

```text
lpf_root_and_prime_leak_fields_fixed=true
declaration_field_map_complete=true
no_square_base_private_signed_escape_proved=true
pre_cauchy_actual_noncanonical_emitter_source_declaration_packet_proved=false
built_in_signed_coefficient_pairing_closed_form_proved=false
exactuv_entropy_fiber_pair_proved=false
row_column_unconditional_closed=false
```

actual-load 含义是：`(p,p)` 的 diagonal-root key 与 prime-row leak guard 已由 Phi-LPF
层固定；剩余的 source tuple、basis word、signed coefficient、orientation/local factor、
ExactUV、推前前恒等式和 return tag 都不是 square-base 私有字段。它们必须由同一个
`PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket` 及其 built-in pairing / ExactUV
entropy-fiber 下游字段正向给出。

因此 square-base 专属硬点被剥离，最新直接主攻回到
`PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket`；下游 signed 子线为
`BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows`，ExactUV 子线为
`ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger`。
`PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward` 和
`PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward` 仍开放。行/列命题仍未
无条件闭合。

### 1.170 Phi-LPF source packet cycle guard sync 更新

新增机器证书：

```text
experiments/prime_matrix_phi_lpf_source_packet_cycle_guard_sync_router.py
data/prime-matrix-phi-lpf-source-packet-cycle-guard-sync-ledger.json
docs/monograph/prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.md
docs/monograph/prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.json
```

同步读数为：

```text
square_base_reduction_to_common_packet_imported=true
signed_lane_cycle_imported=true
common_packet_self_proof_rejected_after_lpf=true
new_primitive_exit_downstream_already_imported=true
pointwise_kernel_table_imported=true
alpha_row_anchor_phase_emission_formula_proved=false
new_primitive_payload_or_trace_artifact_present=false
pointwise_phi_lpf_bucket_signed_value_table_proved=false
row_column_unconditional_closed=false
```

actual-load 含义是：LPF/Phi route 回到 common packet 后，不能再把该 packet 当作非循环
证明入口。既有 signed-lane cycle 已给出闭环：
`PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket -> BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows -> branch trace -> payload -> origin identity -> PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket`。
Phi/LPF 当前只固定 support/capacity/root 与 prime-row guard，不产生 primitive signed
payload/trace 公式。既有 post-antisplit 收敛证书又已把 `NewPrimitive...` 与 terminal descent
吸收到 source-rank/no-collapse 和逐点 primitive 核表。

因此最新非循环主攻同步为 `AlphaRowAnchorPhaseEmissionFormulaLedger`。并行出口为
`IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger`、
`SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows`、
`AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate`、
`PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward`、
`ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger`，
以及：

```text
PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward AND
PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward
```

行/列命题仍未无条件闭合。
