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
