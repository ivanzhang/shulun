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
