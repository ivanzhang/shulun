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
