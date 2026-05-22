# 三命题 formal envelope 到 actual load 的临界负载前沿

## 0. 本步边界

本文继续整理并推进合著稿三条主线：

1. Prime Matrix 行/列命题；
2. 二点筛/素数对命题；
3. RH 矛盾场。

本步不宣称三命题已经无条件闭合。新增的实质进展是把“临界密度/临界误差”原则进一步精炼为：

```text
临界矛盾必须由 actual load 触发；
formal envelope 超界只能说明账本还需收紧，或必须证明 envelope=actual。
```

这条纪律非常关键。素数分布中的无穷叠加筛与自反馈矛盾场不会被粗上界本身打破；只有真实幸存者、真实覆盖、真实异常负载超过临界容量，才产生数学矛盾。

## 1. 统一原则：formal envelope 不等于 actual load

在三条线中，反例链通常先给出一个形式包络 `F`，真实结构链真正需要控制的是实际负载 `A`。总有

\[
0\le A\le F.
\]

临界容量记为 `C`。可能出现三种情况：

| 情形 | 含义 | 允许结论 |
|---|---|---|
| `F<=C` | 粗包络已经在临界容量内 | 该通道被吸收 |
| `F>C` 但 `A<=C` | 只是包络过粗 | 必须做 accounting tightening |
| `A>C` | 真实负载超临界 | 必须显化为 PDEC/SAE/KLS/controlled exit |

因此真正的闭合格式不是

```text
formal envelope exceeds capacity => contradiction
```

而是

```text
formal envelope exceeds capacity
=> either actual load still <= capacity after tightening,
   or actual load > capacity and produces a named structured defect.
```

这就是本轮新的全局刚性：**formal-to-actual critical-load rigidity**。

## 2. Prime Matrix：从 `M_q^{form}` 到 actual packet `N_q`

### 2.1 当前实际进展

最新文件

```text
docs/monograph/prime-matrix-nonpdec-sqrt-phase-support-reduction.md
```

已经把 AffineTwin 的平方根门改写成 actual packet 版本。

旧形式包络是：

\[
F_q=(M_q^{\rm form})^2=(A_gA_f)^2.
\]

真实负载应为：

\[
A_q=N_q^2,
\]

其中 `N_q` 是实际非 PDEC generator-fill packet 数。

primitive AffineTwin 双槽支撑宽度为

\[
W_q={q+9\over2}.
\]

对 `q>=13`，

\[
W_q\le\sqrt{q(q-2)}.
\]

若 every actual non-PDEC packet 都落入该 primitive 支撑，并且同一相位投影复现已经路由为 `PDEC/ColumnCRT`，则

\[
N_q\le W_q\le\sqrt{q(q-2)}.
\]

于是 actual load 满足临界容量：

\[
A_q=N_q^2\le q(q-2)=C_q.
\]

### 2.2 新硬点的精确形态

现在的行/列主攻不应再表述为“证明 `A_gA_f<=sqrt(q(q-2))`”。更精确的三分是：

```text
M_q^{form}>sqrt(q(q-2))
```

时：

1. **ProductAccountingTightening.**
   形式配对中有虚配对或无共同相位支撑，实际 `N_q` 未超界。

2. **ProjectionCollision-PDEC.**
   actual packets 全在 primitive 支撑内但超过支撑容量，必有同相位碰撞。

3. **PrimitiveTwinSlotSupportEscape.**
   存在实际 packet 逃出 primitive 双槽支撑，必须作为新的 PDEC/SAE 出口。

所以当前最窄行/列命题变为：

```text
PrimitiveTwinSlotSupportExhaustion
+ ProductAccountingTightening
+ PrimitiveTwinSlotSupportEscape-PDEC/SAE.
```

### 2.3 可继续硬攻的定理接口

**PM-ActualLoad Theorem Interface.**
对每个持久 AffineTwin 反例族和 `q>=13`，存在 disjoint decomposition

\[
\Pi_q=\Pi_q^{\rm prim}\sqcup\Pi_q^{\rm esc}\sqcup\Pi_q^{\rm pdec}
\]

满足：

1. `Pi_q^{prim}` 注入宽度 `(q+9)/2` 的 primitive support；
2. `Pi_q^{pdec}` 已触发 projection/repeated-residue/ColumnCRT；
3. `Pi_q^{esc}` 要么 SAE 可求和，要么触发新的 primitive-support escape PDEC；
4. SAE/Rankin 质量只按 `|Pi_q^{prim}|+|Pi_q^{esc}|` 计，不按 `A_gA_f` 计。

若该接口闭合，则 AffineTwin 超平方根分支不再是自由出口。

## 3. 二点筛：从分子包络到 actual TLI ratio

二点筛中同样存在 formal/actual 分离。

### 3.1 当前链条

已归约链为：

```text
DI/BFI
=> KLS-window
=> BE2-3K
=> BE2-3
=> WBE2
=> BMD
=> BST-2
=> BST
=> TLI.
```

当前外部深定理版可关闭的是 BMD 分布输入；真正终局仍卡在：

```text
BMD=>TLI without hidden denominator/parity gap.
```

### 3.2 actual TLI ratio

TLI 需要控制的是 actual ratio：

\[
R_Y={1\over |U_Y(I)|}
\sum_{x\in U_Y(I)}D_Y^P(x).
\]

其中

\[
D_Y^P(x)=\#\{Y<p\le P:p\mid x(x-2)\}.
\]

BMD/KLS 主要控制分子中的双素乘法曲线分布。它不能单独给出终局，除非同时有同一 convention 下的 actual denominator floor：

\[
|U_Y(I)|\ge (1-\delta)\mathcal M_Y(I).
\]

并且分子上界为

\[
\sum_{x\in U_Y(I)}D_Y^P(x)
\le (K(\alpha)+\varepsilon)\mathcal M_Y(I),
\]

满足

\[
K(\alpha)+\varepsilon<1-\delta.
\]

这才推出：

\[
R_Y<1.
\]

### 3.3 临界点选择

对 `alpha>2/3`，半素数转移主常数为

\[
K(\alpha)=
{2\log((2-\alpha)/\alpha)\over
1+\log((2-\alpha)/\alpha)}.
\]

仓库实验和推导已显示：

```text
alpha=0.75: K=0.67622..., margin=0.32377...
alpha=0.80: K=0.57698..., margin=0.42301...
alpha=0.85: K=0.46423..., margin=0.53576...
```

新的结构刚性点是：提高 `alpha` 会降低大素数命中层的 actual numerator load，但同时使 `U_Y` 的 denominator floor 更难。临界优化应围绕不等式

\[
\delta(\alpha)+\varepsilon(\alpha)<1-K(\alpha)
\]

而不是只看分子或只看经验扫描。

### 3.4 可继续硬攻的定理接口

**TP-ActualRatio Transfer Interface.**
对某个固定 `alpha in (2/3,1)`，证明：

1. BMD/KLS 给出 actual numerator bound；
2. beta/Buchstab lower sieve 给出同一奇异级数 convention 下的 actual denominator floor；
3. 两者误差满足 `delta+epsilon<1-K(alpha)`；
4. 若 denominator floor 失败，则失败转为低模二次型/character defect/endpoint smoothing defect，而不是 hidden parity gap。

若该接口闭合，则 `BMD=>TLI` 无隐藏下界审查完成。

## 4. RH：从 routed envelope 到 final load

RH 线已有 GEE 定义：

\[
\operatorname{Load}(E;X)=
\sum_{a\mapsto E}\theta_{a,E}\operatorname{Excess}(a),
\]

其中

\[
\operatorname{Excess}(a)=
\max\left(0,\sigma\sum_{n\in a}(w_X(n)-w_X^0(n))\right).
\]

这已经体现了 formal-to-actual discipline：零频 baseline、内部下降、source-deleted transfers 不能重复算作 final load。

当前风险不是没有框架，而是每个 controlled exit 是否都已经在同一 convention 下给出：

```text
actual final load lower/upper comparison
```

具体地，off-critical zero 给出入口 anomaly：

\[
\Delta=X^{\beta-o(1)}.
\]

经过路由后必须证明：

\[
\sum_E \operatorname{Load}(E;X)\ge X^{\beta-o(1)}
\]

且每个 exit 都满足：

\[
\operatorname{Load}(E;X)=o(X^{\beta-o(1)})
\]

或严格势下降/source deletion。只有这两端都用 actual final load，RH 矛盾场才可能升级。

### 4.1 可继续硬攻的定理接口

**RH-ActualLoad Controlled-Exit Interface.**
对每个出口 `E in {A,PI,FCT,SC,LV,LSMP,CE,DSO,NRC}` 建立四列表：

| 项 | 必须写清 |
|---|---|
| input actual load | 从哪些 atoms 进入，是否已扣除 baseline |
| closure mechanism | capacity、absorption、descent、transfer 或 external theorem |
| no double counting | source-deleting 与 internal descent 不计 final load |
| terminal inequality | `Load(E;X)` 相对 `X^{beta-o(1)}` 的上界 |

该接口闭合前，RH 仍只能标为 verification package。

## 5. 新的统一刚性矩阵

| 方向 | formal envelope | actual load | critical capacity | 新最窄硬点 |
|---|---:|---:|---:|---|
| PM AffineTwin | `(A_gA_f)^2` | `N_q^2` | `q(q-2)` | primitive support exhaustion / accounting tightening |
| TP TLI | model numerator and denominator | actual `sum D` / actual `|U_Y|` | threshold `1`, Buchstab `K(alpha)` | actual denominator floor |
| RH GEE | routed atom envelope | source-deleted final load | exit capacity/no-cycle | controlled-exit actual load normalization |

这张矩阵说明：三个命题的共同终端矛盾不是“有一个很大的形式误差”，而是“真实负载超过真实临界容量且无合法出口”。

## 6. 进一步的分布结构洞察

### 6.1 临界密度的局部反馈形式

`1/log x` 是全局自筛固定点；但在反例链中，固定点必须局部化为：

```text
actual survivor / actual capacity / actual load
```

三者都不能用粗模型替代。否则会出现两种假象：

1. 粗覆盖上界超临界，但实际覆盖没有超；
2. 粗幸存下界足够，但实际分母可能坍缩。

因此真正需要寻找的不是新的平均密度公式，而是每个局部反例通道的 actual-load identity。

### 6.2 无穷叠加筛的刚性

随着筛层增加，允许反例逃逸的空间不是单调变大，而是被分成更窄的实际通道：

```text
fixed phase      -> PDEC/ColumnCRT
moving phase     -> SAE/Rankin/KLS
denominator drop -> dual lower-sieve defect
analytic anomaly -> controlled exit
```

这就是自反馈矛盾场的真实结构刚性：无穷叠加条件不会直接给出一个简单闭式公式，但会不断压缩 actual load 的合法承载通道。

### 6.3 临界点的可攻形式

下一步最值得同时推进的三个临界点是：

```text
PM:
  actual packet support width <= sqrt capacity

TP:
  delta(alpha)+epsilon(alpha) < 1-K(alpha)

RH:
  sum final actual loads >= anomaly, while each exit load is absorbable
```

这三个不等式都是同一个原则的投影：真实负载不能超过临界容量而不显化为结构缺陷。

## 7. 当前可交付结论

本轮完成的是新的统一证明纪律和主攻接口：

```text
formal-to-actual critical-load rigidity
```

它把三条线的下一步从“继续寻找大而泛的矛盾”压成：

```text
PM: actual packet enumeration and primitive support exhaustion
TP: actual denominator floor and BMD-to-TLI transfer
RH: actual final-load controlled-exit table
```

这些仍是未闭合的数学义务，但它们已经比之前的表述更窄、更可审稿，并且直接围绕临界密度与临界误差的终端矛盾。下一步应优先对 PM 的 actual packet 账本生成机器可审计枚举，再同步推进 TP 的 denominator floor 和 RH 的 controlled-exit actual-load 表格化。

## 8. actual-load 闭合合同更新

后续文件

```text
docs/monograph/three-claims-actual-load-closure-contracts.md
```

把本文的 formal-to-actual 原则落成三个闭合合同：

```text
PM-ALC: Prime Matrix actual packet critical-load contract
TP-ALC: Two-point actual ratio denominator-floor contract
RH-ALC: RH final-load controlled-exit contract
```

其中 PM 合同已生成当前 sweep 机器证书：

```text
experiments/prime_matrix_affine_twin_actual_packet_contract.py
data/prime-matrix-affine-twin-actual-packet-contract-ledger.json
docs/monograph/prime-matrix-affine-twin-actual-packet-contract.md
```

当前结果为：

```text
candidate_q_values=[31, 43, 103]
total_formal_product_upper=40
total_actual_packet_count_current=1
total_formal_to_actual_gap=39
all_actual_packets_pass_sqrt_gate_current=true
```

这把 PM 前沿进一步具体化：当前 sweep 的真实负载非常小，形式包络与 actual load 的差额必须进入 `ProductAccountingTightening`，不能被用作真实临界矛盾。TP 与 RH 的合同则分别固定了 denominator floor 与 source-deleted final load 的下一步审稿格式。

## 9. PM formal-pair pruning 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-formal-pair-pruning-audit.md
data/prime-matrix-affine-twin-formal-pair-pruning-ledger.json
```

把 PM 的 `ProductAccountingTightening` 从抽象缺口压成当前 sweep 的逐项删除证书：

```text
formal_pair_total=40
actual_packet_total_current=1
formal_to_actual_gap=39
crt_window_empty_pair_total_current=11
source_unmaterialized_pair_total_current=28
unresolved_formal_pair_total_current=0
current_formal_gap_fully_pruned=true
```

因此当前 `F-A=39` 并不是隐藏临界负载，而是已经分解为两类非 actual packet：

```text
CRTWindowEmpty:
  source 已物化，但 CRT 代表不落入双槽共同相位支撑。

SourceMaterializationFailure:
  formal residue product 有计数，但没有匹配方向的 gap-fill source。
```

这一步把 PM 的全局硬点进一步收窄为：证明所有形式配对若不能成为 actual packet，必进入 `CRTWindowEmpty`、`SourceMaterializationFailure-PDEC/SAE` 或 `PrimitiveTwinSlotSupportEscape-PDEC/SAE`。若该分类失败，失败形态本身就是新的反例链/真实链交叉点。

## 10. PM source materialization gate 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-source-materialization-gate-audit.md
data/prime-matrix-affine-twin-source-materialization-gate-ledger.json
```

继续把 `SourceMaterializationFailure` 从泛称失败压成源门控不变量。当前结果为：

```text
source_gate_pass_q_values=[31]
source_gate_fail_q_values=[43, 103]
formal_pairs_blocked_by_source_gate=28
same_gap_wrong_source_formal_pair_count=16
no_gap_source_formal_pair_count=12
unresolved_source_failure_count_current=0
```

源门控是 actual packet 的必要输入：

```text
gap=q,
generator=q-2,
fill=q,
sides match,
p_delay=(11q-21)/4.
```

`q=43` 的同 gap source 失败在四个不变量上：`generator_ell`、两侧方向、`p_delay`。`q=103` 则完全没有 gap-fill source。于是前一步的 `28` 个 source 未物化 formal products 已全部解释。

全局硬点相应压缩为：

```text
GlobalSourceMaterializationGate
SameGapWrongSource-PDEC/SAE
NoGapSource-PDEC/SAE
```

也就是说，未来若某个 formal product 试图绕过 source gate，它必须显式破坏端点运动/生成填充二元组的结构，而不是作为 hidden actual load 留在账本中。

## 11. PM CRT window gap 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-crt-window-gap-audit.md
data/prime-matrix-affine-twin-crt-window-gap-ledger.json
```

继续把 `CRTWindowEmpty` 从布尔判断压成相位距离证书。当前结果为：

```text
formal_pair_total_with_exact_source=12
supported_actual_packet_total_current=1
crt_window_gap_pair_total_current=11
min_empty_window_distance=40
max_empty_window_distance=434
support_width_current=20
combined_modulus_current=899
```

这说明当前唯一通过 source gate 的 `q=31` 分支中，formal product 的每个 residue pair 都有明确 CRT 类。只有 `(19,8)` 的 CRT 代表 `2687` 落入共同窗口 `[2669,2688]`；其余 `11` 对的最近代表都与窗口保持正距离。

这一步把 PM 的 actual-load 管道进一步细化为：

```text
formal residue product
  -> source gate
  -> CRT window representative
  -> actual packet
```

全局硬点相应压成 `GlobalCRTWindowGapBound`：若未来有 source 已物化但空窗不成立，则它必须表现为 `WindowEdgeCollision-PDEC` 或 `SupportMotionEscape-PDEC/SAE`，不能作为未登记 actual load 混入临界负载。

## 12. PM window edge-collision 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-window-edge-collision-audit.md
data/prime-matrix-affine-twin-window-edge-collision-ledger.json
```

继续把 `WindowEdgeCollision` 从命名出口压成 residue 网格位移。当前结果为：

```text
target_window_pair_count=20
edge_collision_candidate_count_current=11
min_empty_l1_residue_displacement=1
max_empty_l1_residue_displacement=11
empty_pairs_target_existing_actual_count=2
empty_pairs_target_unused_residue_arrival_count=9
```

窗口 `[2669,2688]` 对应 `20` 个 target residue pairs。空窗 formal pair 若要变成 actual packet，必须移动到这些目标点之一。当前最近 atom 是

```text
(generator residue, fill residue) = (19,9) -> (19,8),
delta_g=0, delta_f=-1.
```

这不是全局矛盾，但它把下一步主攻点从“窗口边界可能碰撞”压成一个明确单点：若这种单 fill-residue edge collision 可持续复现，它必须与已有 actual pair `(19,8)` 发生 residue collision，或暴露 repeated residue / ColumnCRT / target-arrival 结构缺陷。

## 13. PM existing-actual collision CRT jump 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-existing-actual-collision-jump-audit.md
data/prime-matrix-affine-twin-existing-actual-collision-jump-ledger.json
```

继续下钻 existing-actual 分支。当前 `WindowEdgeCollision` 中有 `2` 个空窗 pair 的最近目标是已有 actual pair `19:8`：

```text
15:12 -> 19:8
19:9 -> 19:8
```

审计把 residue 位移提升为双模 CRT 相位跳跃：

```text
generator_unit_step_current=465
fill_unit_step_current=435
support_width_current=20
min_abs_crt_jump_to_existing_actual=120
max_abs_crt_jump_to_existing_actual=435
```

因此最窄 atom `19:9 -> 19:8` 不是微小边界误差。它固定 generator residue，只把 fill residue 改一格，但 CRT 代表从 `3122` 跳到 actual 点 `2687`，相位差为 `435`。另一个 `15:12 -> 19:8` 的相位差为 `120`，仍然超过支撑宽度 `20`。

本步关闭当前 sweep 的 existing-actual collision jump 账本；全局仍需证明这种 CRT 跳跃不能被 moving support 持久重置，或把失败形态登记为 `RepeatedResidue-ColumnCRT-PDEC` / `SupportMotionEscape-PDEC/SAE`。

## 14. PM unused-target arrival 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-unused-target-arrival-audit.md
data/prime-matrix-affine-twin-unused-target-arrival-ledger.json
```

继续下钻 `WindowEdgeCollision` 的 unused-target 分支。当前有 `9` 个空窗 formal pairs 的最近目标不是已有 actual pair，而是当前未使用的 target pair；它们压缩到 `5` 个唯一目标：

```text
10:30  multiplicity 3
16:5   multiplicity 2
17:6   multiplicity 2
18:7   multiplicity 1
20:9   multiplicity 1
```

这些 target 全部不在当前形式积中。当前形式 generator residues 为 `[13,15,19]`，fill residues 为 `[8,9,12,28]`；要让这些 unused target 进入形式积，至少需要新增 generator residues `[10,16,17,18,20]` 和 fill residues `[5,6,7,30]`，合计 `9` 个新侧残基。

审计同时记录 CRT 跳跃：

```text
min_abs_crt_jump_to_unused_target=59
max_abs_crt_jump_to_unused_target=375
support_width_current=20
```

最窄 unused-target atom 是 `19:12 -> 20:9`。它复用 fill residue `9`，但仍需新增 generator residue `20`，并且 CRT 相位跳跃为 `59`。这把 unused-target 分支从“可能补入目标点”压成明确的新 generator/fill residue arrival 或 support-motion 义务；全局仍需证明这些到达不能持久供给，或把失败登记为 `NewGeneratorResidueArrival-PDEC/SAE`、`NewFillResidueArrival-PDEC/SAE`、`SupportMotionEscape-PDEC/SAE`。

## 15. PM support-motion depth 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-support-motion-depth-audit.md
data/prime-matrix-affine-twin-support-motion-depth-ledger.json
```

继续下钻 `SupportMotionEscape` 本身。当前共同支撑来自两个相位区间：

```text
generator_phase=[2669,2693]
shifted_fill_phase=[2659,2688]
pair_phase_support=[2669,2688]
```

左端要同时受 generator lower 与 shifted-fill lower 约束，右端要同时受 generator upper 与 shifted-fill upper 约束。因此若一个空窗 CRT representative 要通过“移动支撑”进入窗口，必须释放同侧两个端点，而不是只释放当前钉住窗口边界的一个端点。

审计对 `11` 个空窗行逐项计算：

```text
min_required_common_side_depth=58
max_required_common_side_depth=435
min_generator_depth_increment_required=40
min_fill_depth_increment_required=30
min_endpoint_release_total_required=70
max_endpoint_release_total_required=863
```

最窄 atom 仍来自 `19:12`，nearest representative 为 `2629`。为了让它进入支撑，generator 左深度需从 `18` 增至 `58`，fill 左深度需从 `28` 增至 `58`；总端点释放为 `70`，比原 window gap `40` 还多 `30`。

本步关闭当前 sweep 的 support-motion depth 账本；全局剩余被压成同步深度膨胀的非持久性证明，或路由到 `MovingSupportDepthInflation-PDEC/SAE`、`EndpointReleaseCoupling-PDEC`、`PrimitiveTwinSlotSupportEscape-PDEC/SAE`。

## 16. PM support-motion primitive-depth defect 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-support-motion-primitive-defect-audit.md
data/prime-matrix-affine-twin-support-motion-primitive-defect-ledger.json
```

继续把同步深度膨胀接回固定 AffineTwin primitive key。当前 `q=31` slot-lock 已证明四个深度恒等式：

```text
generator_left_depth=(q+5)/2=18
generator_right_depth=(q-7)/4=6
fill_left_depth=q-3=28
fill_right_depth=1
```

如果 support motion 仍保持当前 `q=31` primitive key，那么每个空窗行要求的共同侧深度都必须等于对应 generator/fill 深度 RHS。但审计显示：

```text
support_motion_primitive_defect_candidate_count=11
min_total_affine_depth_defect=70
max_total_affine_depth_defect=863
all_support_motion_breaks_both_depth_identities=true
```

最窄 atom `19:12` 要把左侧共同深度提升到 `58`。这同时打破 `generator_left_depth=18` 与 `fill_left_depth=28`，缺陷分别为 `40` 与 `30`，总缺陷 `70`。

因此当前固定 primitive key 下的 support motion 已关闭；全局剩余进一步压成 primitive key 迁移的非持久性证明，或路由到 `MovingPrimitiveKey-PDEC/SAE`、`MovingSupportDepthInflation-PDEC/SAE`、`EndpointReleaseCoupling-PDEC`。

## 17. PM moving-key depth formula 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-moving-key-depth-formula-audit.md
data/prime-matrix-affine-twin-moving-key-depth-formula-ledger.json
```

继续检查 primitive key 迁移的最直接吸收方式：允许 `q` 移动，但保持同一 AffineTwin 深度公式和同侧吸收。此时 lower-side support motion 需要同一个深度 `D` 同时满足：

```text
(q+5)/2 = D
q-3 = D
```

也就是 `q=2D-5` 与 `q=D+3` 必须相等，只在 `D=8` 可能。当前最窄 lower atom `19:12` 有 `D=58`，所以 generator 公式给 `q=111`，fill 公式给 `q=61`，两者差 `50`。

above-side 则需要：

```text
(q-7)/4 = D
fill_right_depth = 1 = D
```

但当前 above depths 为 `342,373,435`，全部远离 `1`。审计结果：

```text
moving_key_depth_formula_candidate_count=11
min_lower_q_candidate_gap=50
min_above_fill_right_depth_residual=341
same_orientation_moving_key_depth_absorption_closed_current_sweep=true
```

因此当前 support motion 不仅不能由固定 key 吸收，也不能由同向 moving AffineTwin key 的深度公式吸收。全局剩余进一步压成方向改变、source 重物化或 key 迁移的非持久性证明，或路由到 `OrientationChangingPrimitiveKey-PDEC/SAE`、`SourceRematerialization-PDEC/SAE`、`EndpointReleaseCoupling-PDEC`。

## 18. PM moving-key source-rematerialization 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-moving-key-source-rematerialization-audit.md
data/prime-matrix-affine-twin-moving-key-source-rematerialization-ledger.json
```

上一节排除了“同一个移动 `q` 同时满足两侧深度公式”。本节继续审计更弱逃逸：只取深度公式吐出的单侧候选 `q`，看它是否能在别处重新通过 AffineTwin prime gate 与 source gate。当前证书给出：

```text
moving_q_formula_occurrence_count=19
unique_moving_q_candidate_count=19
composite_q_count=13
prime_but_not_twin_affine_count=6
affine_twin_prime_gate_q_values=[]
exact_rematerialized_q_values=[]
moving_key_source_rematerialization_closed_current_sweep=true
```

也就是说，`19` 个候选 `q` 中 `13` 个合数，`6` 个为素数但全部不满足同向 AffineTwin key 的必要门；没有任何候选同时满足 `q,q-2` 同素、`q≡3 mod 4`、整型 `p_delay=(11q-21)/4` 与 matching gap-fill source。

最窄 atom 仍是 `19:12`：它给出 `q=111` 与 `q=61`。`q=61` 是最接近通过的候选，因为 `61` 与 `59` 都是素数，但 `61≡1 mod 4`，且没有 gap `61` 的 source；已有 gap `59` source 的方向和角色也不匹配。因此当前 support motion 若继续，不能靠同向 moving-key source rematerialization 成为 hidden actual load，只能转入方向改变、全局 source 重物化非持久性，或已命名 PDEC/SAE 出口。

## 19. PM endpoint-release critical-error 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-critical-error-audit.md
data/prime-matrix-affine-twin-endpoint-release-critical-error-ledger.json
```

本节把临界误差原则落到当前最窄支撑逃逸口。若空窗 CRT 代表要被 support motion 吸收，则 actual load 不再是 formal pair 数，而是双端点同步释放总量；critical capacity 是当前 primitive 双槽共同支撑宽度 `20`。于是：

```text
endpoint critical error = actual endpoint-release load / 20 - 1
```

审计结果：

```text
support_motion_candidate_count=11
total_endpoint_release_load=4929
total_window_capacity_budget=220
total_endpoint_release_critical_error=21.4045454545
min_endpoint_release_critical_error=2.5
max_endpoint_release_critical_error=42.15
all_positive_endpoint_release_errors_structured_current=true
```

最窄 atom `19:12` 的端点释放负载为 `70`，临界容量为 `20`，已给出显式正临界误差 `2.5`。固定 primitive key 缺陷总量也正好是 `70`，并且同向 moving-key source-rematerialization 已缺席。这说明当前局部超界不是形式账本误差，也不是普通密度波动；它被迫显化为 `EndpointReleaseCoupling-PDEC`。

因此当前 actual-load 前沿进一步压窄：若反例链还要推进，就必须给出 `EndpointReleaseCoupling-PDEC` 的持久复现机制，或者转入方向改变/source 重物化的已命名出口。否则当前支撑逃逸在真实链中没有匿名承载通道。

## 20. PM endpoint-release feedback-loss 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-feedback-loss-audit.md
data/prime-matrix-affine-twin-endpoint-release-feedback-loss-ledger.json
```

上一节仍按总端点释放负载计量临界误差。本节给 support motion 最有利的自反馈解释：把较大端点移动量全部当作几何支撑扩张信用，只追踪剩余的第二端点同步损耗：

```text
feedback loss = endpoint release load - max(generator release, fill release)
              = min(generator release, fill release)
post-credit feedback error = feedback loss / support width - 1
```

即使这样，当前 sweep 仍全部超界：

```text
total_endpoint_release_load=4929
total_geometric_support_gain_credit=2512
total_coupled_second_endpoint_feedback_loss=2417
total_support_width_budget=220
total_post_credit_feedback_error=9.98636363636
min_post_credit_feedback_error=0.5
all_feedback_losses_exceed_support_width=true
```

最窄 `19:12` 的 `70` 负载中，`40` 可记作支撑扩张信用，剩余反馈损耗 `30` 仍大于 support width `20`。这正是局部超界自反馈的显式残差：反例链试图移动支撑来吸收误差，但真实链要求两个端点同步释放；几何扩张最多回收一个端点，第二端点损耗仍形成正临界误差。

因此当前最窄硬点进一步变成：排斥 `EndpointReleaseFeedbackLoss-PDEC` 持久复现，或证明这种损耗必回流到方向改变/source 重物化/SAE 出口。

## 21. PM endpoint-release feedback-horizon 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-feedback-horizon-audit.md
data/prime-matrix-affine-twin-endpoint-release-feedback-horizon-ledger.json
```

把上一节的 feedback loss 再写成相位地平线：

```text
feedback horizon = support width + side depth skew
side depth skew = |current generator side depth - current fill side depth|
phase horizon surplus = window distance - feedback horizon
```

这一步直接把“局部超界的自反馈波动”转成 CRT 代表距离与自反馈吸收半径的比较。当前读数为：

```text
total_window_distance=2512
total_feedback_horizon_width=315
total_phase_horizon_surplus=2197
min_phase_horizon_surplus=10
all_feedback_loss_formulas_hold=true
all_phase_surpluses_match_post_credit_units=true
all_representatives_outside_feedback_horizon=true
```

最窄 `19:12` 的相位数据是：

```text
window distance = 40
support width = 20
side depth skew = 10
feedback horizon = 30
phase horizon surplus = 10
```

这就是目前最精确的显式矛盾交叉点：反例链需要通过端点自反馈吞掉距离 `40` 的 CRT 代表；真实链在当前 primitive 双槽结构下最多给出 `30` 的反馈地平线。差额 `10` 不能再解释为 formal envelope、几何支撑回补或同向 source 重物化，只能登记为 `EndpointReleaseFeedbackHorizon-PDEC`，或进入方向改变/source 重物化/SAE 出口。

## 22. PM endpoint-release feedback-horizon slack 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-feedback-horizon-slack-audit.md
data/prime-matrix-affine-twin-endpoint-release-feedback-horizon-slack-ledger.json
```

把 `EndpointReleaseFeedbackHorizon-PDEC` 的最小剩余再写成 skew 缺口：

```text
required total skew = max(0, window distance - support width)
required extra skew = required total skew - current side-depth skew
required extra skew = phase horizon surplus
```

当前读数为：

```text
total_required_absorption_skew=2292
total_current_side_depth_skew=95
total_required_extra_skew=2197
current_skew_coverage_ratio=0.0414485165794
extra_skew_deficit_ratio=0.958551483421
min_required_extra_skew=10
max_required_extra_skew=409
all_pure_orientation_flips_fail_absorption=true
same_orientation_source_rematerialization_absent=true
```

这说明当前真实链中的侧深度差只支付了所需 skew 的约 `4.14%`，剩余约 `95.86%` 必须由新的 skew-growth 或方向改变 primitive key 供给。最窄 `19:12` 需要新增 skew `10`；纯方向翻转不改变绝对 skew，同向 source 重物化也为空，所以该缺口不能再由上一层自反馈解释吸收。

因此最新可攻接口变成：排斥 `EndpointSkewGrowth-PDEC`，或证明任何方向改变/source 重物化都必须进入可求和 `SAE` 或 `ColumnCRT/PDEC`。这仍是行/列命题内部同一条 actual-load 主线，不是命题转换。

## 23. PM endpoint-release bidirectional skew-hull 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-bidirectional-skew-hull-audit.md
data/prime-matrix-affine-twin-endpoint-release-bidirectional-skew-hull-ledger.json
```

将逆元最小对齐解的思想局部化到当前 AffineTwin 原子：旧路线中每个 `r,q` 给出 `x` 的同余类；这里每个 generator/fill residue pair 给出 `P` 的同余类。于是 formal pair 全集的“最小对齐”就是包含全部最近 CRT 代表的最短相位壳层。

当前读数为：

```text
combined_crt_modulus=899
support_width=20
alignment_hull_width=819
hull_width_to_modulus_ratio=0.911012235818
left_extension_required=365
right_extension_required=434
left_extra_skew_after_feedback_horizon=335
right_extra_skew_after_feedback_horizon=409
modulus_minus_hull_width=80
affine_p_delay=80
hull_complement_equals_affine_p_delay=true
```

这把局部超界自反馈波动改写成一个更尖锐的相位矛盾：反例链要求 near-full-period 的双向壳层；真实链只有宽度 `20` 的 primitive 支撑，且单侧 skew-growth 已无法解释 below/above 两侧同时超界。壳层互补宽度正好等于 `p_delay`，说明这不是随机距离误差，而是 AffineTwin 双槽 CRT 与延迟相位共同锁出的结构缺口。

最新剩余接口相应压成：排斥 `BidirectionalSkewHull-PDEC`，或证明持久 near-full-period 壳层必进入 `ColumnCRT/PDEC`、`SAE` 或 `AffineTwinEpochPairMultiplicityBoundOrColumnCRTPDECExclusion`。

## 24. PM endpoint-release circular-aperture 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-circular-aperture-audit.md
data/prime-matrix-affine-twin-endpoint-release-circular-aperture-ledger.json
```

把上一层的线性壳层读数放回模 `q(q-2)=899` 的圆周相位空间。线性 hull `[2304,3122]` 宽 `819`，依赖当前切口；圆周最小弧要删除最大 open gap 后再计。

当前读数为：

```text
support_width=20
linear_hull_width_from_previous_audit=819
largest_circular_open_gap_width=341
largest_gap_from_pair=19:8
largest_gap_to_pair=13:9
minimal_circular_alignment_arc=[3029,3586]
minimal_circular_alignment_arc_width=558
optimal_shifted_support_interval=[3568,3587]
optimal_total_extension_required=539
conservative_extra_after_best_single_side_feedback=509
p_delay_open_gap_present=true
p_delay_open_gap_is_largest_gap=false
p_delay_gap_rank_by_width=3
```

这给出更严格的审计边界：`p_delay=80` 子缝存在，但不是最大圆周空弧；真正最优切口删除的是 `19:8 -> 13:9` 的 `341` 宽 open gap。删除后剩余圆弧仍宽 `558`，远超真实链当前宽 `20` 的 primitive 支撑。反例链若试图通过支撑平移和单侧 feedback 吸收全部 formal pair，仍至少缺 `509` 的圆周 aperture 扩张。

因此当前接口从 `BidirectionalSkewHull-PDEC` 精炼为 `CircularAperture-PDEC/ColumnCRT`：若该圆弧形态持久复现，必须证明它进入 ColumnCRT/PDEC、SAE 或 moving-family multiplicity 出口；若不能证明持久复现排斥，则不能宣称行/列命题无条件闭合。

## 25. PM endpoint-release anchored circular-depth 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-anchored-circular-depth-audit.md
data/prime-matrix-affine-twin-endpoint-release-anchored-circular-depth-ledger.json
```

将圆周最小弧与真实 actual packet 绑定后，得到更尖锐的容量/相位缺口。最优圆弧 `[3029,3586]` 的右端点是唯一 actual pair `19:8` 的平移代表；若这个 actual 锚不消失，吸收整段圆弧要求双端点同时扩张。

当前读数为：

```text
actual_anchor_pair=19:8
shifted_actual_anchor_representative=3586
required_common_left_depth_to_cover_arc=557
generator_left_increment_required=539
fill_left_increment_required=529
anchored_endpoint_release_total_required=1068
hidden_second_endpoint_release=529
anchored_release_after_single_side_feedback=1038
endpoint_release_to_support_width_ratio=53.4
q_from_generator_depth_formula=1109
q_from_fill_depth_formula=560
q_candidate_gap=549
same_orientation_common_q_absent=true
```

因此 circular-aperture 失败若要继续作为真实链，必须支付两层约束：第一层是交支撑从宽 `20` 扩到覆盖 `558` 圆弧；第二层是 actual 锚固定时，generator 与 shifted-fill 两个相位端点都必须左移，额外暴露 `529` 的第二端点释放。把这个释放解释成同向 moving AffineTwin key 也失败，因为同一深度 `D=557` 同时要求两个不同的 `q`，且 fill 侧候选 `560` 不是奇素数。

最新接口相应压成 `AnchoredCircularDepth-PDEC/ColumnCRT`：持久 actual-anchored 圆弧若不能被排斥，就必须作为固定锚相位缺陷、方向改变 key、SAE 或 moving-family multiplicity 出口登记；当前仍不是行/列命题的无条件闭合。

## 26. PM endpoint-release anchored parity no-go 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-anchored-parity-nogo-audit.md
data/prime-matrix-affine-twin-endpoint-release-anchored-parity-nogo-ledger.json
```

将 actual-anchored 圆弧的深度压力进一步化为同向 key 的方程刚性。lower-side 同向 AffineTwin 吸收要求同一 `D` 同时满足：

\[
q=2D-5,\qquad q=D+3.
\]

所以共同 key 唯一可能发生在 `D=8,q=11`。但当前最小圆弧右端固定在 actual pair `19:8` 后，强制 `D=557`，并给出：

```text
q_from_generator_depth_formula=1109
q_from_fill_depth_formula=560
q_from_fill_is_even=true
same_orientation_common_q_absent_by_equality=true
same_orientation_common_q_absent_by_parity=true
```

这就是当前最窄显式矛盾点：反例链若保留 actual 锚并坚持同向 AffineTwin key，就同时要求 fill 侧 key 是大于 `2` 的偶数；真实链的奇素数 key 条件直接否定它。因此同向 anchored key 不再是开放吸收通道。

最新接口压成 `AnchoredParityNoGoGlobalFamily` 或方向改变/ColumnCRT/PDEC/SAE/moving-family 出口：要闭合全局命题，还需证明所有持久 actual-anchored 圆弧都落入同类 parity no-go，或把非同向逃逸登记为可排斥的命名证书。

## 27. PM endpoint-release cut-anchor sweep 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-cut-anchor-sweep-audit.md
data/prime-matrix-affine-twin-endpoint-release-cut-anchor-sweep-ledger.json
```

将上一节的 actual-anchored no-go 推广到当前 `q=31` 原子的所有圆周切口。每个 cut 都删除一个相邻 CRT 类之间的 open gap，并取覆盖全部 formal alignment 类的 lifted arc；唯一 actual pair `19:8` 在每个 lifted arc 中被保留，可能位于左端、右端或内部。

审计给出：

```text
cut_count=12
endpoint_cut_count=2
interior_cut_count=10
min_arc_cut=19:8->13:9
min_arc_width=558
min_total_endpoint_release_required=1068
max_total_endpoint_release_required=1737
all_endpoint_releases_exceed_support_width=true
all_actual_retained_cuts_same_orientation_closed=true
```

相位公式也全切口关闭。left lower-side 同向吸收要求 `D=8,q=11`；当前所有正 left depth 中最近的是 `D=58`，仍相差 `50`。right above-side 同向吸收要求 fill right depth 固定为 `D=1`；当前所有正 right depth 中最近的是 `D=342`，仍相差 `341`。

这说明“换圆周 cut 或换 actual 端点”不是逃逸通道。若 actual 在端点，则落入 left parity no-go 或 right fixed-fill no-go；若 actual 在内部，则同时要求两侧释放，容量缺口更大。最新接口压成 `CutAnchorSweepGlobalFamilyNoGo`，或进入方向改变 key、`ColumnCRT/PDEC`、`SAE`、moving-family multiplicity 出口。

## 28. PM endpoint-release cut-anchor ColumnCRT compression 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-cut-anchor-columncrt-compression-audit.md
data/prime-matrix-affine-twin-endpoint-release-cut-anchor-columncrt-compression-ledger.json
```

将 cut-anchor sweep 的剩余容量出口继续压缩：12 个 cut 不是 12 个独立相位，因为它们全部保留同一个 actual pair `19:8`。审计显示 actual representative 在两个 lift `2687` 与 `3586` 中切换，但同余类始终是：

```text
P == 889 mod 899
```

所以固定 `q=31`、固定 actual 槽的 ColumnCRT 质量是 `1/899`。若按 cut 数误计会得到 `12/899`，其中 `11/899` 是纯切口重数假象，不是真实链可使用的容量。

这给出新的显式矛盾点：反例链在 same-orientation 已关闭后若试图通过换 cut 维持固定 actual 锚，并不能获得新的相位容量；真实链只允许一个固定模 ColumnCRT 原子。于是固定 `q` 固定残基的方向改变逃逸必须登记为 `CutAnchorColumnCRT-PDEC`；移动 `q` 或移动残基则回到既有 AffineTwin moving-family SAE/ColumnCRT 账本。

## 29. PM endpoint-release actual-anchor replacement 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-actual-anchor-replacement-audit.md
data/prime-matrix-affine-twin-endpoint-release-actual-anchor-replacement-ledger.json
```

将“放弃 actual 锚点”这条逃逸路线显式量化。保留 `19:8` 时已经压成 `P≡889 mod 899` 的单个 ColumnCRT 原子；若不保留，则只有两种替换方式：

1. 让当前 11 个 unsupported formal pair 中某个变成 actual。
2. 跳到未使用 target residue，并新增侧残基。

审计给出：

```text
support_width=20
min_formal_replacement_abs_crt_jump=58
min_formal_replacement_endpoint_release=70
min_unused_target_abs_crt_jump=59
min_unused_target_new_side_residue_count=1
```

现有 formal 替换最窄为 `19:12`，相位跳跃 `58` 已超过 support width，且需要双端点释放 `70`。未使用 target 替换最窄为 `20:9`，相位跳跃 `59`，仍超过 support width，并新增侧残基。故 actual-anchor replacement 在当前 sweep 内也不是有效逃逸；它回流到 support-motion、unused-target arrival、ColumnCRT/PDEC 或 moving-family 出口。

## 30. PM endpoint-release 61/59 near-miss phase-fracture 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-near-miss-61-59-phase-fracture-audit.md
data/prime-matrix-affine-twin-endpoint-release-near-miss-61-59-phase-fracture-ledger.json
```

本节把上一节的最窄 replacement 接口与 moving-key source-rematerialization 接口合并审计。表面最接近闭合的桥是：

```text
formal minimum: 19:12, jump=58, depth=58, release=70
moving q candidates: 61 and 111
nearest available gap source to q=61: 59
unused-target minimum: 19:12 -> 20:9, jump=59, new side residue=1
```

审计结论是这个桥断裂在三个不同相位角色之间：

1. `q=61` 是 fill-depth formula 给出的 moving-key 候选；它虽然满足 `q` 与 `q-2=59` 都为素数，但 `61≡1 mod 4`，所以 AffineTwin delay 非整数，并且没有 gap `61` matching source。
2. `q=111` 是 generator-depth formula 给出的候选；它满足 delay 整数形式，但自身合数。
3. gap `59` source 的实际签名是 `gap=59, generator=61, fill=59, sides=minus->minus, p_delay=70`；而 `q=61` 期望的是 `gap=61, generator=59, fill=61, sides=minus->plus`。同一个整数邻近不能改变源角色、方向和 delay。

因此 unused-target 跳跃 `59` 与 gap source `59` 只是数值相邻，不是同一个合法相位通道。`20:9` 还需要新增 generator residue `20`，并且 `59>20`，仍在 primitive support 外。

最新接口压成 `NearMiss6159GlobalFamilyNoGo`：若全局族中反复出现同类 `q/(q-2)` 近邻，必须证明其源签名、方向与 delay 仍不能同时匹配；若失败，则登记为明确的 `SourceRematerialization-PDEC/SAE`、`UnusedTargetResidueArrival-PDEC`、`ColumnCRT/PDEC` 或 moving-family 出口。当前 sweep 的 `61/59` 近失配已经关闭，但这仍不是行/列命题的无条件闭合。

## 31. PM endpoint-release phase-scale bridge exhaustion 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-phase-scale-bridge-exhaustion-audit.md
data/prime-matrix-affine-twin-endpoint-release-phase-scale-bridge-exhaustion-ledger.json
```

继续把 near-miss 从单点推广为全候选相位尺度账本。对每个 moving-q 候选同时检查四类可能桥：

```text
q == available gap source
q-2 == available gap source
q == unused-target CRT jump
q-2 == unused-target CRT jump
```

当前结果为：

```text
exact_q_gap_bridge_q_values=[]
exact_q_unused_jump_bridge_q_values=[]
exact_qminus2_gap_bridge_q_values=[61]
exact_qminus2_unused_jump_bridge_q_values=[61]
exact_qminus2_gap_and_unused_bridge_q_values=[61]
viable_exact_scale_bridge_q_values=[]
```

这说明所有 exact-q 桥全部为空；唯一 exact-offset 桥就是 `q=61` 的 `q-2=59`，而它已经在上一节失败于源签名、方向、delay 与新侧残基条件。最近 unused jump 到 `q=61` 的差只有 `1`，但该 jump 是 `60` 而不是 AffineTwin key 或 gap source；真正同时落在 gap/source 与 unused-target 的整数仍是 `59=q-2`，不是 `q`。

因此当前可攻接口从“是否还有另一个近失配桥”压成：证明任意持久族的 exact/offset phase-scale bridge 都必须满足相同源签名门控；若不能满足，则进入 `PhaseScaleBridgeGlobalNoGo` 或命名 `PDEC/SAE` 出口。当前 sweep 内没有剩余匿名相位桥，但全局行/列命题仍未无条件闭合。

## 32. PM endpoint-release support-width near-scale fracture 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-support-width-nearscale-fracture-audit.md
data/prime-matrix-affine-twin-endpoint-release-support-width-nearscale-fracture-ledger.json
```

本节继续测试一个更弱逃逸：即使 exact/offset 桥不成立，反例链是否能利用 primitive support width `20` 把“近似相等”的尺度当作同一相位桥。审计枚举所有满足

```text
|gap_source - q| <= 20, |gap_source - (q-2)| <= 20,
|unused_jump - q| <= 20, |unused_jump - (q-2)| <= 20
```

的事件。结果显示：

```text
support_width_near_source_q_values=[61, 65]
support_width_near_unused_jump_q_values=[61, 65, 96, 111, 154, 293, 297, 355, 386]
support_width_near_source_and_jump_q_values=[61, 65]
viable_support_width_nearscale_bridge_q_values=[]
```

同时靠近 source 与 unused jump 的 `q=61` 已是上一层 phase-fracture，`q=65` 则为合数。`q=96,111,154,293,297,355,386` 只靠近 unused jump，不靠近 source；这些不能形成 moving-key、source、unused-target 三方同相位闭环。

这把当前最窄接口进一步压成：support-width 邻域本身不能替代 CRT/source 精确签名。非零尺度差若要被修正，必然移动 key、source 或 target，从而回到 `SourceRematerialization-PDEC/SAE`、`UnusedTargetResidueArrival-PDEC`、`ColumnCRT/PDEC` 或 moving-family 出口。当前 sweep 仍未给出全局无条件证明，但匿名 near-scale 吸收通道已关闭。

## 33. PM endpoint-release orphan near-jump source-deficit 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-orphan-nearjump-source-deficit-audit.md
data/prime-matrix-affine-twin-endpoint-release-orphan-nearjump-source-deficit-ledger.json
```

support-width near-scale 剩下的非同步候选是“near jump only”：它们靠近 unused-target CRT jump，但没有 near source。审计对这些 q 计算到最近 source scale 的距离：

```text
orphan_nearjump_q_values=[96, 111, 154, 293, 297, 355, 386]
min_source_gap_abs_delta=35
min_source_gap_abs_delta_minus_support_width=15
min_source_gap_deficit_q=96
```

最窄 orphan 为 `q=96`，即使取 `q-2=94`，离最近 gap source `59` 仍有距离 `35`，超过 support width `20`。其他 orphan 的 source 缺口更大。并且所有 orphan 的 unused-target 近邻事件都需要新增侧残基；moving source 没有物化；候选 q 全部失败于合数或 AffineTwin prime/source gate。

这说明 orphan near-jump 没有真实链相位承载：它只在 target 侧接近，source 侧仍越过支撑宽度。要把它补成桥，必须移动 source 或新增 source family；这正是 `SourceRematerialization-PDEC/SAE` 或 moving-family 出口，而不是当前 primitive support 内的匿名吸收。

## 34. PM endpoint-release near-jump carrier exhaustion 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-nearjump-carrier-exhaustion-audit.md
data/prime-matrix-affine-twin-endpoint-release-nearjump-carrier-exhaustion-ledger.json
```

本节合并 support-width near-scale 与 orphan source-deficit 两个分支，给出所有 near unused-target jump carrier 的总分解：

```text
nearjump_carrier_q_values=[61, 65, 96, 111, 154, 293, 297, 355, 386]
near_source_gate_fractured_q_values=[61, 65]
orphan_source_deficit_q_values=[96, 111, 154, 293, 297, 355, 386]
nearjump_carrier_exhausted_current_sweep=true
```

分解是无剩余的：`61,65` 是 near source and jump，但一个是 `PrimeButNotTwinAffine`，一个是合数；七个 orphan 只近 target，不近 source。所有 carrier 的 unused-target jump 事件还都需要新增侧残基。因此 target 侧相位近邻无法单独承载 actual load。

这把当前局部反例链的 near-target 尝试压成明确选择：要么补 source，进入 `SourceRematerialization-PDEC/SAE` 或 moving-family；要么补 target 侧残基，进入 `UnusedTargetResidueArrival-PDEC`；要么固定相位复现，进入 `ColumnCRT/PDEC`。当前 primitive support 内没有匿名 near-jump carrier。

## 35. PM endpoint-release carrier-arrival routing 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-carrier-arrival-routing-audit.md
data/prime-matrix-affine-twin-endpoint-release-carrier-arrival-routing-ledger.json
```

本节把 near-jump carrier 的 target 侧近邻全部接回 unused-target arrival 账本，测试是否存在“靠近 jump 但不用新增残基”的隐藏 actual load。

结果显示：

```text
carrier_event_count=27
unique_arrival_atom_count_used_by_carriers=9
target_pair_histogram={'10:30': 9, '16:5': 5, '17:6': 7, '18:7': 2, '20:9': 4}
carrier_event_new_side_residue_requirement_total=50
carrier_event_new_side_residue_histogram={1: 4, 2: 23}
missing_unused_target_arrival_match_count=0
all_carrier_targets_outside_current_formal_product=true
all_carrier_targets_not_supported_actual_current_sweep=true
```

这说明 target 近邻只是 unused-target arrival 的重复投影，不是新的 actual packet。特别是唯一 exact zero phase `q=61,q-2=59,jump=59` 仍落在 `19:12 -> 20:9`，需要新增 generator residue `20`；相位精确贴合并没有消除 target 侧新残基成本。

所以当前局部矛盾场又压窄一层：若反例链继续要求这些 target 近邻真实出现，就必须给出新侧残基的全局到达机制；若该机制持久复现，则登记为 `NewGeneratorResidueArrival-PDEC/SAE`、`NewFillResidueArrival-PDEC/SAE` 或 `ColumnCRT/PDEC`，不能留作未命名吸收。

## 36. PM endpoint-release carrier-arrival pressure-product 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-carrier-arrival-pressure-product-audit.md
data/prime-matrix-affine-twin-endpoint-release-carrier-arrival-pressure-product-ledger.json
```

本节把上一步的 arrival 义务翻译成 actual-load 压力乘积。基础 formal side sets 为：

```text
generator residues=[13,15,19], count=3
fill residues=[8,9,12,28], count=4
side_product=12
```

carrier-arrival packet 需要的新侧残基为：

```text
new generator=[10,16,17,18,20]
new fill=[5,6,7,30]
```

如果这些 target atoms 被真实物化，则侧计数变成 `(8,8)`，于是：

```text
64^2 > 29*31, with excess 3197.
```

最精确的本地 crossing 更强：任意两个双侧 target atoms 就产生 `(5,6)`，乘积 `30`，而

```text
30^2-29*31=1.
```

这个 `+1` 是当前反例链和真实链之间最窄的压力断点：反例链为了把 target arrival 变成 actual load，必须越过平方根临界面；真实链的账本纪律则要求这一步被登记为 `SuperSqrt/PressureProduct-PDEC`。因此最新剩余不再是匿名 arrival，而是 `SuperSqrtPressureProductPDECExclusion` 的全局排斥，或把该族作为命名 PDEC 出口保留。

## 37. PM endpoint-release carrier-arrival projection-deficit 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-carrier-arrival-projection-deficit-audit.md
data/prime-matrix-affine-twin-endpoint-release-carrier-arrival-projection-deficit-ledger.json
```

本节把 pressure product 的形式乘积与 actual projection 分开。最小 crossing 的形式账本是：

```text
formal_product=30
sqrt_floor=29
formal_excess=1
```

但投影到当前共同窗口后，每个最小 crossing 只剩：

```text
projection_hits=3
hits=actual anchor 19:8 + two selected target atoms
projection_deficit=27
actual_sqrt_slack=26
```

完整 packet 同样显示：

```text
formal_product=64
projection_hits=6
projection_deficit=58
actual_sqrt_slack=23
```

这给出更精确的反例链/真实链矛盾点：反例链的 `SuperSqrt` 来自把侧残基笛卡尔积当作 actual load；真实链只允许落入共同支撑窗口的 residue pairs 计入 actual load。当前 packet 的真实投影远低于平方根门。因此当前 `SuperSqrt` 分支不是 actual overload，而是 `ProductAccountingTightening` 问题；若未来投影 hits 也超界，则已经是命名 `ProjectionCollision/SupportEscape-PDEC`。

## 38. PM endpoint-release support-graph cap 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-support-graph-cap-audit.md
data/prime-matrix-affine-twin-endpoint-release-support-graph-cap-ledger.json
```

本节把 ProductAccounting 的正确 actual 计数对象固定为共同支撑图像。当前 target window 为连续整数段 `[2669,2688]`，对应 20 个 residue pairs：

```text
(1,21),(2,22),...,(10,30),(11,0),...,(20,9).
```

它是双向函数图像：

```text
generator_functional_graph=true
fill_functional_graph=true
affine_offsets_mod_fill=[20]
```

所以任意 `G x F` 的 actual projection 至多命中该图像的 `20` 个点。由于

```text
support_graph_cap=20
sqrt_floor=floor(sqrt(29*31))=29
```

当前固定槽不可能产生 actual SuperSqrt overload。一般固定 AffineTwin 槽的支撑宽度为 `W=(q+9)/2`；对 `q>=13`，

```text
W^2 <= q(q-2) <=> 3q^2-26q-81>=0.
```

当前 `q=31` 的符号余量为 `1996`。因此最新剩余已经不在固定槽 ProductAccounting，而是 moving-slot support escape：若反例链要绕过图像容量，必须移动或改变共同支撑图像，进入 `PrimitiveTwinSlotSupportEscape-PDEC/SAE`。

## 39. PM endpoint-release moving-slot graph-cap route 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-moving-slot-graph-cap-route-audit.md
data/prime-matrix-affine-twin-endpoint-release-moving-slot-graph-cap-route-ledger.json
```

本节直接攻击上一节的 moving-slot 剩余口。证书把逃逸拆成六个门：

```text
FixedOrMovedAffineTwinGraphCap
SamePrimitiveSupportMotion
FixedPrimitiveDepthIdentity
SameOrientationMovingKeyDepthFormula
MovingKeySourceRematerialization
MovingFamilyColumnCRTOrSAE
```

当前 fixed/moved AffineTwin 候选 `q=[31,43,103]` 全部满足固定图容量不等式；已实现的仍只有 `q=31`。如果反例链不保持固定图像而移动支撑，最窄 `19:12` 也要求共同深度 `58` 与双端点释放 `70`，超过支撑宽度 `20`。若试图把这解释为 key 迁移，同向深度公式给出 `q_g=111`、`q_f=61`，二者不相等；若只取单侧候选再 source 重物化，则 19 个候选没有一个精确物化。

由此得到当前最明确的容量/相位矛盾读数：

```text
真实链 fixed actual graph cap = 20 < sqrt(29*31)=29;
反例链 moving support 最小释放 = 70 > 20;
同向 moving key 最小公式差 = 50;
source rematerialized exact q = [].
```

这关闭当前 sweep 的匿名 moving-slot actual overload。若全局族继续复现，必须落入方向改变 primitive key、source-rematerialization、ColumnCRT/PDEC、SAE 或 unused-target arrival 的命名出口；因此本步是行/列命题内部主线的进一步收窄，而不是全局无条件终稿。

## 40. PM endpoint-release moving-family persistence pressure 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-moving-family-persistence-pressure-audit.md
data/prime-matrix-affine-twin-endpoint-release-moving-family-persistence-pressure-ledger.json
```

本节把 `MovingSlotFamilyPersistenceNoGo` 的当前可攻部分落到 source/pressure/fill 三重门。moving family 若要成为反例链的持久容量来源，必须满足：

```text
source materialized
paired side pressure product crosses sqrt gate
threshold crossing has enough fill-side residue arrival
duplicate fill arrival enters reset/ColumnCRT-PDEC
```

当前联合证书显示：3 个候选 `q=[31,43,103]` 中只有 `q=31` 通过 source gate；`q=43` 是 same-gap wrong-source，`p_delay` 相差 `-39`；`q=103` 没有 gap source。source gate 共阻断 28 个 formal pairs，占三候选 formal pairs 的 `70%`。

另一方面，`q=43,103` 的 generator 侧已经出现单侧压力，但 paired pressure product 仍低于 1，说明真实链没有形成双侧同步超载。所有最小阈值穿越路线都要求 fill 增量；三个候选全穿越至少要新增 11 个 fill residue，Rankin 质量为 `23339/137299`。

因此当前族级显式矛盾是：

```text
反例链需要 moving family 持久提供新容量；
真实链中未物化候选先被 source 相位门阻断；
已物化候选被 graph cap/fill-arrival 二分管住；
单侧 generator 压力没有与 fill 侧同步越过 paired pressure gate。
```

本步关闭当前 sweep 的匿名 moving-family persistence 解释；全局仍需证明 fill-side residue arrival 不会持久补齐阈值缺口，或排斥 `HighDensityEpochPair-PDEC/ColumnCRT`、`PressureProduct-PDEC`、`SourceRematerialization-PDEC/SAE`。

## 41. PM endpoint-release fill-arrival projection gate 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-fill-arrival-projection-gate-audit.md
data/prime-matrix-affine-twin-endpoint-release-fill-arrival-projection-gate-ledger.json
```

本节把 `FillResidueArrivalBound` 当前可攻部分继续拆开：fill-side residue arrival 只有在同时满足 source 物化和 actual projection 超界时，才可能成为真实链容量。

当前证书给出：

```text
realized_q_values=[31]
source_blocked_q_values=[43,103]
source_blocked_formal_pairs=28
realized_fill_only_route_count=0
realized_min_extra_generator_required=2
minimal_crossing_formal_product_count=30
minimal_crossing_projection_hit_count=3
minimal_crossing_actual_sqrt_slack=26
```

因此分支被精确拆成：

```text
q=31: exact source, but no fill-only route;
      any fill arrival needs generator coarrival, then projects to 3 actual hits.
q=43: formal fill-only possible, but same-gap wrong-source blocks actualization.
q=103: formal fill-only possible, but no gap source blocks actualization.
```

这给出更窄的容量/相位矛盾：反例链希望用 fill 侧追赶补齐 moving-family 阈值；真实链中唯一已物化候选不能单靠 fill 侧补齐，未物化候选没有 source 相位，而实际共到达投影仍低于平方根门。

本步关闭当前 sweep 的匿名 fill-arrival actual overload。全局剩余相应变成 `GeneratorCoarrivalBound`、`ProductAccountingTighteningGlobal`、`SourceRematerialization-PDEC/SAE` 与 `ColumnCRT/PDEC` 的族级排斥或控制。

## 42. PM endpoint-release generator-coarrival projection accounting 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-generator-coarrival-projection-accounting-audit.md
data/prime-matrix-affine-twin-endpoint-release-generator-coarrival-projection-accounting-ledger.json
```

本节把 `GeneratorCoarrivalBound` 当前可攻部分压成全枚举投影账本。realized `q=31` 的 base packet 有 `(3,4)` 个侧残基，形式乘积 `12`，actual 支撑 hits 只有 anchor `19:8`。unused-target 层有 5 个候选 target atoms，其中 4 个同时新增 generator/fill，1 个只新增 generator；所有带 fill arrival 的子集都不是 fill-only。

当前证书给出：

```text
actual_anchor_pair=19:8
base_formal_product_count=12
base_projection_hit_count=1
subset_count=31
fill_arrival_subset_count=30
fill_only_subset_count=0
formal_super_sqrt_subset_count=22
actual_overload_subset_count=0
minimal_coarrival_formal_product_count=30
minimal_coarrival_projection_hit_count=3
minimal_coarrival_projection_deficit_count=27
full_formal_product_count=64
full_projection_hit_count=6
full_projection_deficit_count=58
```

因此当前最精确的容量/相位矛盾读数是：

```text
反例链：coarrival 后形式侧乘积可从 12 提升到 30 或 64；
真实链：actual projection 只从 1 提升到 3 或 6；
平方根门：sqrt_floor=29；
结论：形式 SuperSqrt 子集 22 个，actual overload 子集 0 个。
```

这说明 generator coarrival 不是新的真实容量来源，而是 ProductAccounting 必须投影化的对象。若未来族级失败，失败形态不能再匿名称为 fill/generator 到达；它必须给出 support graph 逃逸、projection collision、source rematerialization、ColumnCRT/PDEC 或 moving-family persistence 证书。

## 43. PM endpoint-release generator-coarrival family schema 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-generator-coarrival-family-schema-audit.md
data/prime-matrix-affine-twin-endpoint-release-generator-coarrival-family-schema-ledger.json
```

本节把 `GeneratorCoarrivalFamilyBound` 的当前可攻部分写成一个明确的族级 schema。固定 AffineTwin 支撑图像的容量公式为：

```text
W=(q+9)/2,
W^2<=q(q-2) <=> 3q^2-26q-81>=0.
```

`q=13` 时 margin 为 `88`，且 margin 在 `q>=13` 单调递增，所以任意固定 AffineTwin 图像内的 actual projection 都不能越过平方根门。当前候选 `q=[31,43,103]` 全部通过该门控；当前 realized packet 的形式读数仍是 `formal_super_sqrt_subset_count=22`、`actual_overload_subset_count=0`、完整 packet `64 -> 6 hits`。

于是本轮前沿的显式容量/相位矛盾变为：

```text
若反例链停留在固定函数图像内，则 actual load <= W <= sqrt(q(q-2))；
若 actual load 真超界，则必须移动/破坏支撑图像；
而当前 sweep 的移动支撑、source 重物化、固定残基 ColumnCRT、moving family persistence 均已路由为命名出口。
```

这把“generator coarrival 是否补齐容量”的问题推进为“所有持久 AffineTwin family 是否都遵守固定图像投影 schema，或其失败是否必定进入命名 PDEC/SAE/ColumnCRT 出口”。当前 sweep 已闭合该 schema；全局行/列命题仍需族级推广和出口排斥。

## 44. PM endpoint-release persistent-family promotion 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-persistent-family-promotion-audit.md
data/prime-matrix-affine-twin-endpoint-release-persistent-family-promotion-ledger.json
```

本节把族级推广义务继续压成 promotion 路由。固定图像分支已经由 `W<=sqrt(q(q-2))` 关闭；剩下的持久 family 只能通过固定 q/残基复现或 moving q/残基复现进入真实链。当前证书给出：

```text
candidate_q_values=[31,43,103]
realized_q_values=[31]
candidate_product_mass_upper_sum=0.023577117628562343 < eta=0.025
high_density_epoch_pair_count=0
fixed_slot_recurrence_count=0
fixed_residue_slot_drift_pair_count=12
source_gate_blocked_formal_pairs=28
```

由此得到更窄的反例链/真实链冲突：

```text
反例链需要 persistent family 反复提供新容量；
真实链若固定 q/残基，则变成固定模 ColumnCRT/PDEC；
真实链若移动 q/残基，则进入 epoch-pair SAE/Rankin；
当前 sweep 中 moving epoch-pair 稀疏、无 high-density，fixed-slot 复现为 0。
```

最新未闭合硬点不再是匿名 `GeneratorCoarrivalFamilyBound`，而是 `GlobalEpochPairMultiplicityBound` 与 `FixedResidueSlotDriftColumnCRT`：要么证明 moving epoch-pair 总 multiplicity 可求和，要么把固定残基槽漂移族升级为明确 ColumnCRT/PDEC 并排斥。

## 45. PM endpoint-release transport-frontier integration 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-transport-frontier-integration-audit.md
data/prime-matrix-affine-twin-endpoint-release-transport-frontier-integration-ledger.json
```

本节继续下钻上一节的固定残基槽漂移出口。promotion 账本中有 `12` 个 fixed-residue slot-drift pairs；transport-cell 集成账本逐个匹配到 `12` 个 transport cells，且：

```text
unique_transport_cell_count=12
transport_cell_recurrence_count=0
exact_phase_translate_count=0
forward_finite_lifetime_count=12
max_forward_transition_count=8
immediate_terminal_after_observed_count=8
reset_pdec_atom_count=0
partition_total=24 transport physical + 300 singleton physical
unclassified_physical_record_count=0
```

这把容量/相位冲突继续收窄：

```text
反例链需要 slot-drift 在后续层继续复现以补足容量；
真实链若复现同一 transport cell，则深度漂移给出有限寿命；
真实链若跳过链式复现而非连续重置，则必须重复完整 cell key；
当前完整 key 重复数和 reset atom 都为 0；
剩余 singleton residue 被单独送入 SAE/Rankin 质量账本。
```

所以 current sweep 中的 `FixedResidueSlotDriftColumnCRT` 已被拆成可检查的 transport-frontier 路由，不再是未分类 ColumnCRT 容量来源。最新全局剩余是 `TransportResetPDECExclusion`、`SingletonResidueSAE/Rankin`、`GlobalEpochPairMultiplicityBound` 与 `MovingResidueShapeSAE/Rankin`；它们仍是全局义务，不能据此宣称行/列命题已经无条件闭合。

## 46. PM endpoint-release remaining-frontier bridge 更新

后续文件

```text
docs/monograph/prime-matrix-affine-twin-endpoint-release-remaining-frontier-bridge-audit.md
data/prime-matrix-affine-twin-endpoint-release-remaining-frontier-bridge-ledger.json
```

本节把上一节四个全局剩余中的三个可计算分支接到已有深层账本：transport reset、singleton residue SAE、AffineTwin epoch-pair multiplicity。当前 bridge 证书给出：

```text
TransportFrontierCurrentBridge=true
SingletonResidueToActiveEllBand=true
AffineTwinEpochPairSparseGate=true
remaining_frontier_bridge_closed_current_sweep=true
```

其显式含义是：

```text
1. transport reset 分支当前没有 reset atom；
2. singleton residue 分支中 300 个 packet 的 Rankin 质量主要来自 one-slot mass；
3. one-slot 分支有 40 个 active epochs，max occupancy 约 0.30986，spare ratio 至少约 0.69014；
4. active ell 来源精确为素数带 23..109，双侧核心为 29..107，端点不对称只在 [23,109]；
5. epoch-pair 候选 q=[31,43,103] 的总占用上界为 0.023577117628562343<eta=0.025。
```

这把反例链与真实链的最新交叉点继续压窄：若反例链要求 singleton SAE 质量持续失控，真实链必须让活跃素数带端点无限外推，或触发 endpoint reset-PDEC/SAE；若反例链改走 moving AffineTwin epoch-pair，真实链当前只允许低于 eta 的稀疏门，全球仍需 multiplicity bound。最新主攻硬点为 `ActiveEllBandEndpointGrowthBoundOrEndpointResetPDEC`、`TransportResetPDECExclusion`、`GlobalEpochPairMultiplicityBound` 与 `MovingResidueShapeSAE/Rankin`。

## 47. H-lower endpoint-motion stencil 更新

后续文件

```text
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-stencil-audit.md
data/square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-stencil-ledger.json
```

本节把活跃素数带端点增长再细分为一个六点模板：

```text
19 -> 23 -> 29   and   107 -> 109 -> 113
```

当前读数为：

```text
19,113: outward neighbors empty
23,109: minus-only endpoint singleton atoms
29,107: both-side core absorption edges
```

这给出新的显式相位/容量分叉：反例链若要求端点继续外推，真实链必须生成新的外向端点到达；但当前外邻为零。反例链若让端点向内合并，真实链立即进入双侧核心支撑，不再是端点单原子。于是端点增长剩余被压成 `EndpointOutwardArrivalBoundOrEndpointAtomPDECExclusion`，内侧另留 `CoreEdgeAbsorptionMultiplicityBound`。

## 48. H-lower endpoint-motion gap 更新

后续文件

```text
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-gap-router.md
data/square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-gap-ledger.json
```

本节把端点外推造成的相位风险具体化为“内部素数缺口”。按首次激活顺序，活跃带不是任意散列，而是最多带短暂缺口的素数区间运动。当前只出现三次缺口：

```text
ell=43, delay=74
ell=31, delay=80
ell=59, delay=70
```

并且所有缺口均在当前 sweep 内填回；按 `P=3000,4000,...,10000` 的千级前缀看，每个前缀的活跃 `ell` 集合已经是完整素数带。反例链若要利用端点运动制造持续容量缺口，就必须让某个内部素数缺口长期不填；真实链则把这种失败登记为 `Gap-PDEC/SAE`。最新主攻硬点为 `EndpointMotionGapFillBoundOrGapPDECExclusion`。

## 49. H-lower gap-fill pair / repair corridor 更新

后续文件

```text
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-router.md
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-repair-corridor-router.md
data/square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json
data/square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-repair-corridor-ledger.json
```

本节把“缺口会填回”进一步转成二元组和走廊不等式。三次缺口都由下一次 `ell` 首次激活修复，且修复后立即恢复连续素数带：

```text
43: generator ell=47, filler ell=43, P delay=74
31: generator ell=29, filler ell=31, P delay=80
59: generator ell=61, filler ell=59, P delay=70
```

三个完整 GapFillPair key 互异，没有当前复现。更窄地，三次修复均满足：

```text
fill_p - generator_p <= 3*gap_ell
```

其中最紧的是 `gap_ell=31`：`80 <= 93`，余量 `13`；`2*gap_ell` 已被这一行破坏，所以当前最小整数倍统一包络为 `3`。于是反例链若要保持持久缺口，必须破坏 immediate-repair 或短走廊包络；真实链把这两种失败分别登记为 `GapFillPair-PDEC/SAE` 或 `Corridor-PDEC/SAE`。最新主攻硬点为 `ShortGapRepairCorridorBoundOrCorridorPDECExclusion`。

## 50. H-lower corridor phase budget 更新

后续文件

```text
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-corridor-phase-budget-router.md
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-corridor-phase-budget-router.json
data/square-phase-offband-prefix-gap-shadow-selector-h-lower-corridor-phase-budget-ledger.json
```

本节把走廊约束改写成三段相位预算身份：

```text
p_delay = generator_right_depth + phase_bridge_gap + fill_left_depth
```

当前三条缺口修复全部满足该身份，且均仍在 `3*gap_ell` 包络内：

```text
43: 12 + 40 + 22 = 74, slack 55
31: 6 + 46 + 28 = 80, slack 13
59: 31 + 31 + 8 = 70, slack 107
```

唯一单分量超标为 `gap_ell=31` 的 phase bridge：`46-31=15`。但这一超标不是自由相位漂移，因为左右深度余量合计 `28`，吸收后仍余 `13`。所以反例链若想把短走廊破坏成持久缺口，必须制造不能被相邻深度余量吸收的相位桥超标；真实链的下一接口就是 `PhaseBridge-PDEC/SAE`。最新主攻硬点为 `CorridorPhaseBudgetBoundOrPhaseBridgePDECExclusion`。

## 51. H-lower phase-bridge excess 回流到 AffineTwin/ColumnCRT 主线

后续文件

```text
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-atom-router.md
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-source-router.md
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-absorption-normal-form-router.md
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-primitive-identity-router.md
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-primitive-affine-collapse-router.md
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-router.md
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-moving-family-sae-columncrt-router.md
```

本节把 phase bridge 超标的失败形态继续压缩。唯一超标原子满足：

```text
excess=15
absorbing_spare=28
spare_after_excess=13
excess=generator_margin=3*rho_jump
slack_after_absorption=|delta_b|=13
```

margin/slot 正规形与 primitive 身份组把它强制成：

```text
gap_ell=31
generator_ell=29
fill_ell=31
generator_margin=15
|delta_b|=13
|delta_u|=7
phase_bridge_gap=31+15=46
```

所以真实链中所谓“相位桥超标”不是任意可移动槽，而是 `q=31, q-2=29` 的 AffineTwin 原子。双槽 CRT 条件为：

```text
P=19 mod 29
P=21 mod 31
29*31=899 > support width 20
```

当前固定原子因此只有一个代表 `P=2687`，并已归入既有 `P≡889 mod 899` 的 ColumnCRT/actual-anchor 线。反例链若要继续复现，只能固定同一模类形成 ColumnCRT/PDEC，或让 `q`/残基移动并进入 AffineTwin epoch-pair SAE/Rankin。由此 corridor phase budget 的新剩余已经回流到既有主线，而不是新增第三条匿名容量出口；全局仍未闭合，最新剩余仍是移动族 multiplicity、endpoint-growth/reset、transport-reset 与 moving-residue SAE/Rankin 的全局排斥或吸收。

## 52. H-lower AffineTwin epoch-pair sparse SAE 更新

后续文件

```text
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-epoch-pair-multiplicity-router.md
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sparse-sae-global-envelope-router.md
data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-epoch-pair-multiplicity-ledger.json
data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sparse-sae-global-envelope-ledger.json
```

AffineTwin moving family 的当前候选 `q=[31,43,103]` 通过 `eta=1/40` 稀疏门：

```text
total occupancy upper = 0.023577117629 < 0.025
max single occupancy = 0.013348164627
high_density_epoch_pair_count=0
```

若这个稀疏门失败，失败行已经是 HighDensityEpochPair-PDEC/ColumnCRT；若稀疏门成立，则进入 SAE 求和。这里已闭合的全局恒等式是单原子望远镜尾和：

```text
1/(q(q-2)) = 1/2*(1/(q-2)-1/q)
sum_{odd q>=31} 1/(q(q-2)) <= 1/58
```

当前实际实现的 `q=31` 原子质量为 `1/899`，处在该尾和包络内。关键诊断是：`eta` 稀疏不等于全局求和；如果每个 `q` 都允许正比例多个 AffineTwin 原子，则总量仍可发散。因此真正剩余已经精确化为 per-q multiplicity 控制，而不是再寻找单原子质量估计。最新主攻硬点为 `AffineTwinPerQMultiplicityBoundOrHighDensityEpochPairPDECExclusion`。

## 53. H-lower AffineTwin sqrt-product / Brun 条件出口更新

后续文件

```text
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sqrt-product-brun-router.md
docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sqrt-product-brun-router.json
data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sqrt-product-brun-ledger.json
```

本节把 per-`q` multiplicity 控制改写为更弱也更结构化的平方根乘积门。若 `M_q` 是同一 AffineTwin `q` 的候选双残基乘积上界，则只需：

```text
M_q^2 <= q(q-2)
```

此时该 `q` 的 SAE 贡献满足：

```text
M_q/(q(q-2)) <= 1/sqrt(q(q-2)) <= 1/(q-2)
```

当前候选 `q=[31,43,103]` 全部通过该门，最大比值约 `0.400222407579`，最小平方余量为 `755`，当前没有 SuperSqrtEpochPair 行。若外部接受 Brun 孪生素数倒数收敛，则 AffineTwin `q` 的 `1/(q-2)` 尾和可求和；但作者侧自足线尚未接受该外部输入，也尚未证明全局平方根门。最新主攻硬点因此压成 `AffineTwinSqrtProductBoundOrSuperSqrtEpochPairPDECExclusion`：全局证明 `M_q^2<=q(q-2)`，或把失败 q 的超平方根侧残基积登记并排斥为 PDEC/ColumnCRT。

## 54. H-lower sqrt-product 回流到 actual-packet 支撑耗尽

后续文件

```text
docs/monograph/prime-matrix-pressure-packet-carrying-ceiling-brun-selberg-router.md
docs/monograph/prime-matrix-nonpdec-sqrt-phase-support-reduction.md
```

本节把平方根乘积门改写成 actual packet 投影问题。旧口径 `M_q=A_gA_f` 是形式笛卡尔积上界；真实链可消耗的对象是实际通过双槽、CRT、相位支撑、非复用和非 ColumnCRT/PDEC 门的 packet 集合 `Pi_q`，记 `N_q=|Pi_q|`。

若每个非 PDEC actual packet 都落在 primitive AffineTwin 双槽支撑内，则相位支撑宽度为：

```text
W_q=(q+9)/2 <= sqrt(q(q-2))    (q>=13)
```

同一 primitive 投影的复现必须回流为 repeated-residue/reset 或 fixed projection ColumnCRT/PDEC；所以非 PDEC 情况下 `Pi_q` 注入共同支撑 `Omega_q`，得到：

```text
N_q <= |Omega_q| <= W_q <= sqrt(q(q-2))
```

因此真正的超平方根分支不应再停留在形式 `M_q` 上，而只可能是三种明确对象：账本上界过粗，需要 `ProductAccountingTightening`；实际投影碰撞，进入 `ProjectionCollision-PDEC/ColumnCRT`；或 actual packet 逃出 primitive 双槽支撑，进入 `PrimitiveTwinSlotSupportEscape-PDEC/SAE`。最新主攻点由此变成 `PrimitiveTwinSlotSupportExhaustion`：证明所有能承担反例补洞负载且未触发 PDEC/ColumnCRT 的 generator-fill packet，都满足 primitive depth identities 并落入宽度 `(q+9)/2` 的共同相位支撑。

## 55. H-lower actual-packet critical-load 合同回接

后续文件

```text
docs/monograph/prime-matrix-affine-twin-actual-packet-contract.md
docs/monograph/prime-matrix-affine-twin-actual-packet-contract.json
data/prime-matrix-affine-twin-actual-packet-contract-ledger.json
```

当前合同把 `M_q^form` 和 `N_q` 的差距直接列出：

```text
total_formal_product_upper=40
total_actual_packet_count_current=1
total_formal_to_actual_gap=39
projection_collision_pdec_count_current=0
```

三条候选中，只有 `q=31` 有一个 actual packet；`q=43,103` 当前实际为 0。三条均通过 `N_q<=W_q<=sqrt(q(q-2))`。所以当前前沿的容量/相位显式矛盾是：反例链按侧残基笛卡尔积看到 40 个形式 packet，真实链按双槽 source、CRT 与共同支撑只承认 1 个 actual packet。最新主攻保持为 `PrimitiveTwinSlotSupportExhaustion + ProductAccountingTightening`；若未来 `N_q>W_q`，进入 `ProjectionCollision-PDEC/ColumnCRT`，若 packet 逃出 primitive 支撑，进入 `PrimitiveTwinSlotSupportEscape-PDEC/SAE`。

## 56. H-lower formal-pair pruning 收紧

后续文件

```text
docs/monograph/prime-matrix-affine-twin-formal-pair-pruning-audit.md
docs/monograph/prime-matrix-affine-twin-formal-pair-pruning-audit.json
data/prime-matrix-affine-twin-formal-pair-pruning-ledger.json
```

该审计把 `ProductAccountingTightening` 在当前 sweep 内完全实例化：

```text
formal_pair_total=40
actual_packet_total_current=1
formal_to_actual_gap=39
crt_window_empty_pair_total_current=11
source_unmaterialized_pair_total_current=28
unresolved_formal_pair_total_current=0
```

`q=31` 的 12 个形式 residue pair 中，只有 `(19,8)` 经过 fill shift 后合成 `889 mod 899`，并在共同支撑窗 `[2669,2688]` 中命中代表 `2687`；其余 11 个都是 `CRTWindowEmpty`。`q=43` 的 16 个形式配对有同 gap 但源身份错误，`q=103` 的 12 个形式配对没有 gap-fill source，因此二者全为 `SourceMaterializationFailure`。

所以当前前沿的真正单点已经变成：把这个有限账本分解提升为全局引理。形式上，需要证明任意持久 AffineTwin formal pair 都满足三分：

```text
actual packet in primitive support
or CRTWindowEmptyGlobalSupportBound
or SourceMaterializationFailure-PDEC/SAE
```

若出现第四种，即 source 与 CRT 都物化但不落入 primitive 支撑，则它正是 `PrimitiveTwinSlotSupportEscape-PDEC/SAE`。这一节关闭 current-sweep 的 `ProductAccountingTightening`，但仍不关闭全局行/列命题。

## 57. PM formal-to-actual global cutset 收束

后续文件

```text
experiments/prime_matrix_formal_to_actual_global_cutset_router.py
docs/monograph/prime-matrix-formal-to-actual-global-cutset-router.md
data/prime-matrix-formal-to-actual-global-cutset-ledger.json
```

本节把当前前沿从若干局部账本收束成一个 cutset。输入账本包括 actual-packet 合同、formal-pair pruning、source materialization gate、CRT window gap、moving-slot graph cap、remaining-frontier bridge 与 endpoint band atom。合成结论为：

```text
current_sweep_cutset_closed=true
row_column_unconditional_closed=false
```

具体容量/相位读数如下：

```text
formal=40, actual=1, gap=39=11 CRTWindowEmpty + 28 SourceMaterializationFailure
source pass=[31], fail=[43,103]
CRT modulus=899, support_width=20, min_empty_window_distance=40
primitive support_width=20, sqrt_floor=29, exact_rematerialized_q=[]
transport_reset_atoms=0, singleton_packets=300
active_band=23..109, endpoint_atom_count=2
epoch_pair_mass=0.023577117628562343<eta=0.025
```

所以当前最新的最窄接口不是再寻找一个隐藏的 actual packet，而是证明这个 cutset 可全局晋级：任意持久反例链若沿 formal-to-actual 管道推进，必然落入上述命名出口之一；若试图避开所有出口，就必须同时给出 source 物化、CRT 短窗命中、primitive 支撑命中、非复用投影与低于平方根门的 actual 负载，这与反例链所需的超容量相冲突。未闭合部分是出口的全局排斥/求和吸收，而不是 current sweep 的未分类容量。

## 58. cutset completeness 确定性晋级

后续文件

```text
docs/monograph/prime-matrix-formal-to-actual-cutset-completeness-lemma.md
```

上一节 cutset 的分类完备性可以不依赖有限扫描直接证明。对任意 AffineTwin formal pair `a in F_q=G_q x H_q`，按 `source -> CRT -> primitive` 三道门定义：

```text
S_q = source gate fails
C_q = source holds, CRT window fails
P_q = source holds, CRT holds, primitive actual holds
E_q = all remaining source+CRT hits whose primitive actual condition fails
```

这是由首个失败门给出的互斥完备分割：

```text
F_q=S_q disjoint_union C_q disjoint_union P_q disjoint_union E_q
M_q^form=|S_q|+|C_q|+|P_q|+|E_q|
N_q=|P_q|
```

所以 `M_q^form-N_q` 不能作为未登记 actual load：它要么是 `SourceMaterializationFailure-PDEC/SAE`，要么是 `CRTWindowEmpty/WindowEdgeCollision/SupportMotion`，要么是 `ProjectionCollision/ColumnCRT/PDEC` 或 `PrimitiveTwinSlotSupportEscape-PDEC/SAE`。确定性分类已经闭合；剩余最窄硬点变为 `NamedExitExclusionOrSummabilityAfterCutsetCompleteness`，即全局排斥或求和吸收这些命名出口。

## 59. after-cutset named-exit frontier 收束

后续文件

```text
experiments/prime_matrix_after_cutset_named_exit_frontier_router.py
docs/monograph/prime-matrix-after-cutset-named-exit-frontier-router.md
data/prime-matrix-after-cutset-named-exit-frontier-ledger.json
```

cutset 完备分割之后，当前前沿已经不需要再寻找隐藏 actual packet，而是把所有后续分支压成命名出口清单。合成读数为：

```text
40 formal pairs = 1 actual packet + 28 source failures + 11 CRT-window empty pairs
unresolved_formal_pair_total_current=0
edge_collision_candidate_count_current=11
support_motion_candidate_count=11
min_endpoint_release_total_required=70
min_total_affine_depth_defect=70
fixed_highfactor_slot_pattern_isolation_failure_count_at_p0=0
transport_reset_pdec_atom_count=0
candidate_product_mass_upper_sum=0.023577117628562343<eta=0.025
current_sweep_frontier_closed=true
row_column_unconditional_closed=false
```

这把 after-cutset 前沿压成以下十个全局接口：

```text
SourceMaterializationFailure-PDEC/SAE
CRTWindowEmptyGlobalSupportBound
WindowEdgeCollisionOrUnusedTargetArrivalBound
SupportMotionNonpersistenceOrEndpointReleaseBound
PrimitiveIdentityShiftExclusion
MovingSlotFamily-PDEC/ColumnCRT
TransportResetPDECExclusion
GlobalEpochPairMultiplicityBound
MovingResidueShapeSAE/Rankin
SingletonResidueSAE/Rankin
```

当前 sweep 已经关闭这些出口的匿名解释：空窗边缘有正位移，支撑移动要双端点释放，固定 primitive identity 无法吸收，固定 highfactor slot 图样被 CRT 模数/相位宽度隔离，transport reset atom 为空，epoch-pair 低于 eta 稀疏门。全局证明剩余随之精确改写为：

```text
GlobalNamedExitExclusionOrSummability
```

也就是证明上述出口在持久反例链中不能无限复现，或它们的总质量可被 SAE/Rankin/PDEC 账本吸收。

## 60. global named-exit terminal choke 收束

后续文件

```text
experiments/prime_matrix_global_named_exit_terminal_choke_router.py
docs/monograph/prime-matrix-global-named-exit-terminal-choke-router.md
data/prime-matrix-global-named-exit-terminal-choke-ledger.json
```

after-cutset 的十个全局接口现在可合并为五个终端 choke：

```text
SourceAndCRTMaterialization:
  source failure + CRT empty + window-edge/unused-target
SupportMotionPrimitiveIdentity:
  support motion + primitive identity shift + moving-slot family
TransportSingletonActiveEll:
  transport reset + singleton Rankin + active ell endpoint/gap
EpochPairPairedPressure:
  epoch-pair multiplicity + high-density/PressureProduct PDEC
MovingResidueShapeSAE:
  moving residue SAE + fixed residue ColumnCRT
```

当前所有终端 choke 都在 finite sweep 内闭合，关键余量如下：

```text
unresolved_formal_pair_total_current=0
crt_phase_margin=879
endpoint_release_extra_over_support_width=50
transport_reset_pdec_atom_count=0
one_slot_epoch_spare_ratio=0.9038893044128646
one_slot_epoch_min_spare_ratio=0.6901408450704225
paired_pressure_slack=0.8398220244716351
```

这说明最新前沿已经不是“找到另一个 actual packet”或“修补一个局部容量不等式”。若存在全局反例族，它必须在 source/CRT、support/primitive、transport/singleton/endpoint、epoch-pair pressure、moving-residue 五个终端 choke 中至少一个方向持久复现；而每个方向已经有对应的 PDEC/SAE/ColumnCRT 验收接口。下一硬点是：

```text
TerminalChokeSetGlobalExclusionOrSummability
```

也就是对五个终端 choke 建立全局排斥或可求和吸收。

## 61. terminal choke amplification barrier

后续文件

```text
experiments/prime_matrix_terminal_choke_amplification_barrier_router.py
docs/monograph/prime-matrix-terminal-choke-amplification-barrier-router.md
data/prime-matrix-terminal-choke-amplification-barrier-ledger.json
```

本步把五个终端 choke 改写为可比较的放大门槛：

```text
CRTWindowPhaseJump: factor=2, additive=40
OneSlotTransportOverflow: factor=71/22, additive=50
SupportEndpointRelease: factor=70/20, additive=50
EpochPairPairedPressure: factor=899/144, fill additive=1..8
FixedMovingSlotCRT: factor=731/104, additive=703
```

这里最窄 raw barrier 是 CRT 空窗的 `2*support_width` 相位跳，但它会立刻转入 edge/unused-target 出口，不是终端自由逃逸。真正终端最窄点是：

```text
tight_epoch=minus:71
used=22
capacity=71
unused=49
new residues to overflow=50
support extra endpoint release=50
```

这给出当前反例链与真实链的最新容量/相位交叉点：`50-unit cross-lock`。要让终端 choke 持久复现，真实链必须同时解释一个 50 单位级别的 endpoint release 或 residue arrival；若该到达是新 residue，则进入 SAE/Rankin 质量账本；若不是新 residue，则触发 reset/ColumnCRT-PDEC；若移动支撑试图吸收，则破坏 primitive depth identity 或进入 moving-slot ColumnCRT。

新的精确主攻点为：

```text
FiftyUnitCrossLockOrTerminalPDECExclusion
```

## 62. fifty-unit cross-lock carrier separation

后续文件

```text
experiments/prime_matrix_fifty_unit_cross_lock_carrier_separation_router.py
docs/monograph/prime-matrix-fifty-unit-cross-lock-carrier-separation-router.md
data/prime-matrix-fifty-unit-cross-lock-carrier-separation-ledger.json
```

本步把 `FiftyUnitCrossLock` 的直接矛盾尝试拆开。支撑端的最窄原子是

```text
q=31
source_pair_key=19:12
generator_residue=19
fill_residue=12
generator_p=2687
endpoint_release_total=70
endpoint_release_extra_over_width=50
p_delay=80
```

而一槽容量端的最紧 epoch 是

```text
side=minus
ell=71
used=22
capacity=71
unused=49
overflow_new_units=50
p_range=4177..9257
```

所以两端不是同一 carrier：

```text
same_q_or_ell=false
same_side_taxonomy=false
same_p_band=false
direct_same_carrier_contradiction=false
combined_carrier_modulus=31*71=2201
combined_modulus_over_fifty_units=44.02
```

进一步，固定 `p_delay=80` 在 `mod 71` 上给出增量 `9`，且 `gcd(80,71)=1`。因此前 `50` 步 residue 全互异；从进入 `minus:71` P 区间的第一步 `P=4207` 开始，50 步块到 `P=8127` 仍在 `4177..9257` 内。于是当前真正卡点不是短路的重复 residue，而是跨载体同步的新旧 residue 判定：

```text
fifty_step_ramp_is_reset_free=true
fifty_step_block_can_fit_current_epoch_p_range=true
if_fifty_new_residues_sync_then_one_slot_overflow=true
newness_against_existing_epoch_residues_proved=false
```

这给出新的前沿等价形态。若 50 个跨载体到达全为新 residue，则 `22+50>71`，一槽容量必爆；若其中有旧 residue 或不能保持同步，则对应形态必须进入 `TransportReset-PDEC`、`SingletonResidue-SAE`、`SupportMotion/UnusedTarget` 或 `MovingCarrier-ColumnCRT`。因此下一最窄接口为：

```text
CrossCarrierFiftyUnitSynchronizationPDECOrSAE
```

这一步关闭了 `50-unit cross-lock` 的同载体直接矛盾路线，但全局行/列命题仍未无条件闭合。

## 63. cross-carrier fifty-unit residue saturation

后续文件

```text
experiments/prime_matrix_cross_carrier_fifty_unit_residue_saturation_router.py
docs/monograph/prime-matrix-cross-carrier-fifty-unit-residue-saturation-router.md
data/prime-matrix-cross-carrier-fifty-unit-residue-saturation-ledger.json
```

本步攻击 `CrossCarrierFiftyUnitSynchronizationPDECOrSAE` 中最窄的新旧 residue 判定。重建完整 singleton 物理记录后，`minus:71` 的已用 residue 集为

```text
{3,9,10,12,18,21,22,26,27,28,34,35,36,37,39,40,44,46,53,59,65,66}
```

其大小为 `22`，与一槽容量账本完全一致。跨载体 support lattice 的当前可进入步号为 `19..82`，即 `P=4207..9247`，共 `64` 个互异 residue。与既有 `22` 个 residue 相交 `17` 个，新增 `47` 个，因此合并后为

```text
22 + 47 = 69 < 71.
```

所以当前带内没有直接溢出。逐个 50 步块扫描也确认：

```text
direct_fifty_overflow_current_blocks=false
min_block_new_residue_count=34
max_block_new_residue_count=40
max_block_union_size=62
min_block_spare_after=9
```

因此上一层“50 个到达全为新 residue 则溢出”的分支，在当前真实链上不能直接使用。真实链只留下两个空 residue：

```text
missing_residues_after_admitted_band=[0,62]
```

后续到达的精确相位为：

```text
P=9647 -> residue 62 -> union 70/71
P=9727 -> residue 0  -> union 71/71
P=9807 -> residue 9  -> old residue, reset/PDEC
```

于是新的最窄接口为：

```text
TwoResidueSpareEndpointExtensionOrTransportResetPDEC
```

要么证明当前端点无法合法外延到填满两个空位；要么一旦端点外延成功，再下一步持久同步必须进入 transport reset-PDEC；若同步在外延前失败，则回到 SAE、unused-target 或 moving-carrier ColumnCRT 出口。本步是对旧 residue 吸收能力的精确核算，不是全局无条件闭合。

## 64. two-residue spare prime-anchor filter

后续文件

```text
experiments/prime_matrix_two_residue_spare_prime_anchor_filter_router.py
docs/monograph/prime-matrix-two-residue-spare-prime-anchor-filter-router.md
data/prime-matrix-two-residue-spare-prime-anchor-filter-ledger.json
```

本步攻击 `TwoResidueSpareEndpointExtensionOrTransportResetPDEC` 中最窄的“两个空位近端外延”解释，并把 `P` 必须为素数锚的真实链条件加入。当前 admitted lattice 仍为步号 `19..82`，但 64 个步号中只有 17 个 `P=2687+80t` 是素数锚，新增 residue 只有 13 个：

```text
admitted_lattice_step_count=64
admitted_prime_anchor_count=17
admitted_prime_anchor_new_residue_count=13
prime_filtered_union_size=35
prime_filtered_nonzero_spare=35
```

上一节的两个近端空位外延不是合法真实链：

```text
P=9647 -> residue 62 -> composite P
P=9727 -> residue 0  -> divisible by 71
P=9807 -> residue 9  -> composite P
```

其中 `residue 0` 更强：其 AP 类为 `P≡4047 (mod 5680)`，`gcd(4047,5680)=71`，所以除 `P=71` 本身外不能出现素数锚。`residue 62` 的首个素数锚为

```text
step=300
P=26687
```

这说明当前 near-fill 被素数锚条件打断。若反例链仍要靠 `minus:71` 填满全部非零 residue 并触发 reset，必须沿长 AP 等待素数锚覆盖所有缺失非零 residue；当前扫描的最后一个缺失非零 residue 到

```text
residue=67
step=1192
P=98047
```

才出现，随后首个素数锚重复为

```text
step=1194
P=98207
residue=14
```

于是最新接口为：

```text
PrimeAnchorFilteredNonzeroResidueCoverageOrTransportResetPDEC
```

即要么证明这种长 AP 素数锚非零 residue 覆盖不能作为持久反例链复现，要么把覆盖后的重复素数锚登记为 transport reset-PDEC。本步关闭的是 two-residue near-fill 捷径，仍不是全局无条件证明。

## 65. prime-anchor post-band immediate repeat

后续文件

```text
experiments/prime_matrix_prime_anchor_postband_immediate_repeat_router.py
docs/monograph/prime-matrix-prime-anchor-postband-immediate-repeat-router.md
data/prime-matrix-prime-anchor-postband-immediate-repeat-ledger.json
```

本步继续攻击 `PrimeAnchorFilteredNonzeroResidueCoverageOrTransportResetPDEC`：检查 admitted 带后真正第一个素数锚是否会先补入新缺失 residue。结果更窄：

```text
first_postband_prime_anchor={step:90,p:9887,residue:18}
first_postband_prime_is_repeat=true
first_postband_prime_is_original_used_repeat=true
new_prime_anchor_count_before_first_repeat=0
missing_nonzero_remaining_at_first_repeat=35
coverage_before_reset_possible_in_same_epoch=false
```

步号 `83..89` 的候选均为合数：

```text
9327, 9407, 9487, 9567, 9647, 9727, 9807
```

随后步号 `90` 的 `P=9887` 是素数，但 residue 为 `18`，已经属于原始 `minus:71` 已用 residue 集。因此当前真实链不可能在同一无 reset epoch 中先完成任何新缺失非零 residue 的覆盖；第一次可用素数锚已经是 repeat。

于是上一接口的 coverage 分支在当前 primitive epoch 内关闭，剩余变为：

```text
ImmediatePrimeAnchorRepeatTransportResetPDECOrEndpointMotionSAE
```

含义是：若 epoch 延伸到 `P=9887`，则必须登记 transport reset-PDEC；若不延伸，则必须解释 endpoint motion/SAE。当前仍未完成全局无条件证明，但反例链的“长 AP 覆盖”出口已经被压成 immediate repeat/reset。

## 66. prime-anchor repeat reset atom

后续文件

```text
experiments/prime_matrix_prime_anchor_repeat_reset_atom_router.py
docs/monograph/prime-matrix-prime-anchor-repeat-reset-atom-router.md
data/prime-matrix-prime-anchor-repeat-reset-atom-ledger.json
```

本步把 immediate repeat 实例化为完整的一槽 repeat-reset 原子。原始 `minus:71` singleton 记录为

```text
P=7757
residue=18
slot_keys=['644:128:71']
```

post-band 首个素数锚为

```text
P=9887
residue=18
```

二者满足精确整周期平移：

```text
9887 - 7757 = 2130 = 30 * 71
original_lift=109
repeat_lift=139
lift_delta=30
reset_atom_instantiated=true
```

所以这不是一个新的 coverage packet，而是同一 residue packet 的 reset-PDEC 原子。避免该原子的唯一当前出口是端点在 `step=90, P=9887` 前切断；这个切断只剩 7 个合数步号缓冲：

```text
composite_buffer_steps=[83,84,85,86,87,88,89]
composite_buffer_p_values=[9327,9407,9487,9567,9647,9727,9807]
```

最新接口改写为：

```text
OneSlotPrimeAnchorRepeatResetPDECExclusionOrEndpointMotionSAE
```

即下一步只能继续排斥该已实例化的一槽 repeat-reset PDEC，或证明端点运动进入 SAE/Rankin 吸收。

## 67. endpoint cut zero-gain

后续文件

```text
experiments/prime_matrix_endpoint_cut_zero_gain_router.py
docs/monograph/prime-matrix-endpoint-cut-zero-gain-router.md
data/prime-matrix-endpoint-cut-zero-gain-ledger.json
```

本步检查 `OneSlotPrimeAnchorRepeatResetPDECExclusionOrEndpointMotionSAE` 中的 endpoint-motion 出口是否能在 reset 前带来实际素数锚收益。端点切断前唯一缓冲为：

```text
step=83..89
P=[9327,9407,9487,9567,9647,9727,9807]
```

其中没有任何素数锚：

```text
actual_prime_anchor_count_before_reset=0
actual_new_prime_anchor_count_before_reset=0
```

形式上看似补到两个缺口：

```text
residue 62 at P=9647
residue 0  at P=9727
```

但二者分别被最小因子 `11` 与 `71` 排除；所以它们不是真实覆盖。随后第一个素数锚 `P=9887` 已经是 `residue=18` 的 repeat-reset。

因此当前 primitive epoch 内的二分闭合为：

```text
reset-PDEC  OR  zero-gain endpoint cut SAE
```

最新接口为：

```text
ZeroGainEndpointCutSAEOrOneSlotResetPDECExclusion
```

这一步不关闭全局命题；它把 endpoint-motion 分支从“可能有新实际覆盖”压成零收益端点 SAE。

## 68. endpoint cut no-payload SAE

后续文件

```text
experiments/prime_matrix_endpoint_cut_no_payload_sae_router.py
docs/monograph/prime-matrix-endpoint-cut-no-payload-sae-router.md
data/prime-matrix-endpoint-cut-no-payload-sae-ledger.json
```

本步把 zero-gain endpoint cut 再压成空 actual payload。缓冲表中没有任何 actual prime-anchor 行：

```text
actual_prime_anchor_count_before_reset=0
actual_new_prime_anchor_count_before_reset=0
filtered_repeat_prime_anchor_count_before_reset=0
actual_payload_empty=true
actual_payload_mass=0
```

并且切断不改变当前缺失非零 residue 集：

```text
missing_nonzero_before_cut=35
missing_nonzero_after_cut=35
missing_nonzero_set_preserved_by_cut=true
```

因此 endpoint cut 分支不能作为容量来源；它只是一个 no-payload SAE。当前 epoch 的实际二分收窄为：

```text
one-slot reset-PDEC  OR  no-payload endpoint SAE
```

最新接口为：

```text
OneSlotResetPDECExclusionOrNoPayloadEndpointSAESummability
```

这一步关闭的是当前 endpoint cut 的 actual payload；全局仍需处理 reset-PDEC 排斥或 no-payload SAE 的全局吸收。

## 69. one-slot reset prefix no-relief

后续文件

```text
experiments/prime_matrix_one_slot_reset_prefix_no_relief_router.py
docs/monograph/prime-matrix-one-slot-reset-prefix-no-relief-router.md
data/prime-matrix-one-slot-reset-prefix-no-relief-ledger.json
```

本步检查另一边：若不采用 no-payload endpoint SAE，而让同步线经过 `P=9887`，则一槽 reset 先于任何新增缺失非零 residue relief 出现。reset 后首个 relief 前缀的读数是：

```text
reset_step=90
reset_p=9887
reset_residue=18
prefix_prime_anchor_count_before_first_relief=7
prefix_new_missing_nonzero_count_before_first_relief=0
prefix_repeat_prime_anchor_count_before_first_relief=7
first_relief_step_gap_after_reset=25
first_relief_p_gap_after_reset=2000
first_relief_requires_accepted_reset_pdec=true
```

首个真正新增缺失非零 residue 的素数锚为：

```text
step=115, P=11887, residue=30
```

所以当前 actual-load 前沿被压成：

```text
accepted reset-PDEC before relief  OR  no-payload endpoint SAE
```

最新接口为：

```text
AcceptedResetPDECExclusionOrDelayedReliefSupportMotionSAE
```

这一步不排斥全局 reset；它关闭的是 reset 后立即获得新容量的解释，并把剩余交给 accepted reset-PDEC 排斥或延迟 relief 所需的 support-motion/SAE 吸收。

## 70. accepted reset full relief horizon

后续文件

```text
experiments/prime_matrix_accepted_reset_full_relief_horizon_router.py
docs/monograph/prime-matrix-accepted-reset-full-relief-horizon-router.md
data/prime-matrix-accepted-reset-full-relief-horizon-ledger.json
```

本步把 delayed relief 从首个 relief 推到完整 relief。若从 `P=9887` 的 accepted reset 出发，要让当前 `35` 个缺失非零 residue 全部由真实素数锚补齐，最末一个 relief 是：

```text
step=1192, P=98047, residue=67
```

核心读数为：

```text
full_relief_step_gap_after_reset=1102
full_relief_p_gap_after_reset=88160
full_relief_extension_over_epoch_width=17.474906514466
prime_anchor_count_until_full_relief=260
new_relief_prime_anchor_count_until_full_relief=35
repeat_prime_anchor_count_until_full_relief=225
composite_missing_candidate_count_until_full_relief=101
```

因此 full relief 不能作为当前 primitive epoch 的局部补救；它已经是长程 support-motion 义务。当前 actual-load 前沿收窄为：

```text
accepted reset-PDEC  OR  long-relief-horizon support-motion SAE
```

最新接口为：

```text
AcceptedResetPDECExclusionOrLongReliefHorizonSupportMotionSAE
```

这一步仍不关闭全局行/列命题；它把 delayed relief 明确量化成长期 horizon，而不是局部容量收益。

## 71. long relief cycle-debt

后续文件

```text
experiments/prime_matrix_long_relief_cycle_debt_router.py
docs/monograph/prime-matrix-long-relief-cycle-debt-router.md
data/prime-matrix-long-relief-cycle-debt-ledger.json
```

本步把完整 relief horizon 的长距离解释为 `ell=71` 周期相位债务。每个缺失非零 residue 在 reset 后第一次相位命中时，若对应 P 为合数，则必须等待下一次同 residue 相位，也就是一个完整 `71` 步周期。

精确读数为：

```text
ell=71
period_p=5680
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

因此 full relief 的 `101` 个合数形式命中不是外部误差，而是每个缺失 residue 的周期等待债务之和。当前 actual-load 前沿进一步压成：

```text
long-relief cycle-debt PDEC  OR  support-motion SAE summability
```

最新接口为：

```text
LongReliefCycleDebtPDECExclusionOrSupportMotionSAESummability
```

这一步仍不关闭全局行/列命题；它把 long-relief 分支的相位代价材料化为周期债务账本。

## 72. one-period relief deficit

后续文件

```text
experiments/prime_matrix_one_period_relief_deficit_router.py
docs/monograph/prime-matrix-one-period-relief-deficit-router.md
data/prime-matrix-one-period-relief-deficit-ledger.json
```

本步回到 reset 后第一个完整 residue 周期，直接测量 actual relief 容量。`step=90..160` 覆盖全部 `71` 个 residue，因此每个缺失非零 residue 都形式出现一次；但素数锚过滤后只剩：

```text
actual_relief_count_in_one_period=8
composite_missing_count_in_one_period=27
repeat_prime_anchor_count_in_one_period=10
relief_deficit_after_one_period=27
```

其中：

```text
formal_missing_hit_count=35
composite_missing_matches_positive_cycle_debt_residues=true
```

所以当前 actual-load 前沿进一步压成：

```text
one-period relief deficit  =>  cycle-debt PDEC or support-motion SAE
```

最新接口为：

```text
OnePeriodReliefDeficitForcesCycleDebtPDECOrSupportMotionSAE
```

这一步仍不关闭全局命题；它把首个完整周期内的容量缺口固定为 `27` 个未获 actual relief 的缺失 residue。

## 73. cycle-debt CRT cover pressure

后续文件

```text
experiments/prime_matrix_cycle_debt_crt_cover_pressure_router.py
docs/monograph/prime-matrix-cycle-debt-crt-cover-pressure-router.md
data/prime-matrix-cycle-debt-crt-cover-pressure-ledger.json
```

本步把一周期 relief 缺口的后续等待写成周期坐标上的 CRT cover。每个合数等待都对应一个最小素因子阻断类，合并 `27` 个正债务 residue 后：

```text
positive_cycle_debt_residue_count=27
total_composite_waits=101
global_unique_blocker_factor_count=24
global_blocker_lcm=337212073559813724487421695331234639247
global_blocker_product_log10=38.527903115735
max_row_residue=67
max_row_cycle_debt=15
max_row_blocker_lcm=55140500775337593
crt_cover_modulus_exceeds_local_period=true
```

因此，反例链若要全局复现这种 cycle-debt，就不是在一个局部自由参数里滑动，而是要复现大 CRT cover 相位包。当前 actual-load 前沿收窄为：

```text
cycle-debt CRT cover PDEC  OR  global support-motion SAE
```

最新接口为：

```text
CycleDebtCRTCoverPressurePDECOrGlobalSupportMotionSAE
```

这一步仍不关闭全局行/列命题；它把局部缺口提升为全局族必须承担的 CRT cover pressure。

## 74. cycle-debt transverse CRT independence

后续文件

```text
experiments/prime_matrix_cycle_debt_transverse_crt_independence_router.py
docs/monograph/prime-matrix-cycle-debt-transverse-crt-independence-router.md
data/prime-matrix-cycle-debt-transverse-crt-independence-ledger.json
```

本步检查 CRT cover 是否可能只是 `5680` 周期自身的局部吸收。结论是否定的：

```text
period_p=5680=2^4*5*71
transverse_blocker_factor_count=24
all_blocker_factors_coprime_to_period_p=true
gcd_global_blocker_lcm_with_period_p=1
combined_period_equals_product=true
global_blocker_lcm=337212073559813724487421695331234639247
all_row_shift_replay_classes_zero=true
all_row_lcm_exceeds_phase_support_width=true
local_period_absorption_closed_current_certificate=true
```

对同 residue 列 `P(k)=P0+5680*k`，每个合数等待的阻断素因子 `q` 都是横向单位。若把同一等待前缀平移复现，平移量 `K` 必须满足 `K=0 mod q`；合并全部等待后必须满足 `K=0 mod global_lcm`。由于 `gcd(global_lcm,5680)=1`，该包不是局部周期因子，而是独立横向 CRT 相位包。

当前 actual-load 前沿收窄为：

```text
transverse CRT cover PDEC exclusion  OR  global support-motion SAE
```

最新接口为：

```text
TransverseCRTCoverPDECExclusionOrGlobalSupportMotionSAE
```

这一步仍不关闭全局行/列命题；它关闭的是“CRT cover 可以由本地周期平移吸收”的解释。

## 75. cycle-debt sparse replay barrier

后续文件

```text
experiments/prime_matrix_cycle_debt_sparse_replay_barrier_router.py
docs/monograph/prime-matrix-cycle-debt-sparse-replay-barrier-router.md
data/prime-matrix-cycle-debt-sparse-replay-barrier-ledger.json
```

本步把 transverse CRT cover 的复现间距转成 actual-load 容量判定。保持同一阻断图 exact replay 时：

```text
global_exact_replay_cycle_modulus=337212073559813724487421695331234639247
global_exact_replay_p_gap=1915364577819741955088555229481412750922960
max_cycle_debt_support_width=15
full_relief_cycle_span_ceiling=16
global_modulus_over_full_cycle_span_ceiling_floor=21075754597488357780463855958202164952
single_full_debt_copy_per_full_relief_horizon=true
exact_replay_branch_is_sae_sparse_current_certificate=true
non_sparse_persistence_forces_moving_blocker_map=true
```

也就是说，完整 debt word 的下一份 exact 复本在当前 full-relief 窗口外极远处；同一横向 CRT 包不能在短窗口内提供高频容量补偿。若需要高频复现，就必须改变阻断素因子、相位类或行组合，转为 moving transverse cover PDEC。

当前 actual-load 前沿收窄为：

```text
exact sparse replay SAE  OR  moving transverse cover PDEC
```

最新接口为：

```text
SparseReplaySAEOrMovingTransverseCoverPDEC
```

这一步仍不关闭全局行/列命题；它关闭的是“同一 transverse CRT cover 可在 CRT 周期中高频复现”的解释。

## 76. cycle-debt near-shift exit-boundary

后续文件

```text
experiments/prime_matrix_cycle_debt_near_shift_exit_boundary_router.py
docs/monograph/prime-matrix-cycle-debt-near-shift-exit-boundary-router.md
data/prime-matrix-cycle-debt-near-shift-exit-boundary-ledger.json
```

本步把 moving transverse cover 的近程滑动尝试转成 exit-prime 边界冲突：

```text
near_shift_limit_cycles=16
positive_cycle_debt_residue_count=27
total_cycle_debt_mass=101
max_cycle_debt=15
all_near_shifts_close_old_prefix_reuse=true
shift_1_exit_prime_collision_row_count=27
shift_1_exit_prime_collision_debt_mass=101
shift_max_cycle_debt_exit_prime_collision_row_count=1
shift_max_cycle_debt_exit_prime_collision_debt_mass=15
shift_near_limit_fresh_cover_required_row_count=27
shift_near_limit_fresh_cover_required_debt_mass=101
moving_branch_must_replace_some_or_all_support_rows=true
```

每个正债务行都满足：旧合数前缀结束处紧接该行首个 relief prime。于是 `K=1` 平移会把 27 行的 exit prime 全部拉入词内；`1<=K<=15` 时至少有一行发生 exit-prime 碰撞；`K=16` 时则没有任何旧前缀可复用，27 行都需要 fresh cover。

当前 actual-load 前沿收窄为：

```text
fresh moving cover PDEC  OR  global support-motion SAE
```

最新接口为：

```text
FreshMovingCoverPDECOrGlobalSupportMotionSAE
```

这一步仍不关闭全局行/列命题；它关闭的是“moving 分支可由旧 CRT cover 近程滑动复用”的解释。

## 77. cycle-debt fresh-cover prime-obstacle

后续文件

```text
experiments/prime_matrix_cycle_debt_fresh_cover_prime_obstacle_router.py
docs/monograph/prime-matrix-cycle-debt-fresh-cover-prime-obstacle-router.md
data/prime-matrix-cycle-debt-fresh-cover-prime-obstacle-ledger.json
```

本步检查 fresh moving cover 是否能在同一 27 行支撑上重建。对 `K=1..16` 的每个平移窗口，逐槽判定真实素数锚：

```text
total_cycle_debt_mass_per_shift=101
tested_shift_count=16
total_tested_same_support_slots=1616
total_prime_obstacles_all_near_shifts=364
total_new_prime_obstacles_all_near_shifts=263
all_near_shift_same_support_windows_have_prime_obstacles=true
min_prime_obstacle_count_per_shift=17
min_prime_obstacle_shift=5
shift_near_limit_prime_obstacle_count=27
shift_near_limit_new_prime_obstacle_count=27
same_support_fresh_cover_closed_current_certificate=true
support_row_replacement_or_prime_obstacle_pdec_required=true
```

所以同一支撑行的 fresh cover 不只是需要新 CRT 条件，而是直接撞上实际素数锚。若反例链继续坚持全合数词，必须删除这些 actual primes，形成 prime-obstacle PDEC；否则只能更换支撑行，进入 support-row replacement SAE/PDEC。

当前 actual-load 前沿收窄为：

```text
prime-obstacle PDEC  OR  support-row replacement SAE/PDEC
```

最新接口为：

```text
FreshCoverPrimeObstaclePDECOrSupportRowReplacementSAE
```

这一步仍不关闭全局行/列命题；它关闭的是“same-support fresh moving cover”的解释。

## 78. cycle-debt support-row replacement Hall

后续文件

```text
experiments/prime_matrix_cycle_debt_support_row_replacement_hall_router.py
docs/monograph/prime-matrix-cycle-debt-support-row-replacement-hall-router.md
data/prime-matrix-cycle-debt-support-row-replacement-hall-ledger.json
```

本步把支撑行替换变成 35 个缺失 residue 候选行与 27 个正债务需求行之间的 Hall 容量判定。对阈值 `t`，要求候选中 `capacity>=t` 的行数不少于需求中 `debt>=t` 的行数。

```text
candidate_missing_residue_count=35
needed_positive_debt_row_count=27
total_demand_width=101
hall_fail_shift_count=14
hall_fail_shifts=[1,2,3,4,5,6,7,8,9,10,11,12,15,16]
hall_survivor_shift_count=2
hall_survivor_shifts=[13,14]
all_but_k13_k14_fail_hall_capacity=true
k13_assigned_immediate_relief_rows=6
k14_assigned_immediate_relief_rows=8
```

所以 fresh replacement 分支被压缩到两个相位原子：`K=13` 与 `K=14`。它们不是轻微替换，分别需要调用 `6` 和 `8` 个 immediate-relief 行，并进行 `26/27` 行替换。

当前 actual-load 前沿收窄为：

```text
K=13/14 support replacement survivor PDEC  OR  global SAE
```

最新接口为：

```text
K13K14SupportReplacementSurvivorPDECOrGlobalSAE
```

这一步仍不关闭全局行/列命题；它关闭的是“多数相位可通过支撑行替换重建”的解释。

## 79. cycle-debt K13/K14 survivor rigidity

后续文件

```text
experiments/prime_matrix_cycle_debt_k13_k14_survivor_rigidity_router.py
docs/monograph/prime-matrix-cycle-debt-k13-k14-survivor-rigidity-router.md
data/prime-matrix-cycle-debt-k13-k14-survivor-rigidity-ledger.json
```

本步把 `K=13,14` 两个 survivor 从“存在 Hall assignment”继续压成 tight-Hall 刚性岛。每个 zero-slack 阈值都是一个精确 Hall cut：该层 supply set 必须整层进入匹配，任一 supply 行容量损失都会立刻造成阈值失败。

```text
k13_zero_slack_thresholds=[1,4,7,8]
k14_zero_slack_thresholds=[7,8,13,15]
k13_minimum_replacement_count=20
k14_minimum_replacement_count=19
k13_minimum_immediate_relief_rows=6
k14_minimum_immediate_relief_rows=6
k13_minimum_overstretch_units=61
k14_minimum_overstretch_units=65
all_tight_layers_have_transverse_lcm_exceeding_period=true
survivor_island_has_adjacent_hall_failures=true
```

forced-shell 读数显示：

- `K=13` 的 `>=8` shell 中 supply residues `[1,13,19,30]` 与 demand residues `[17,23,58,67]` 完全错位，立即给出 4 个强制替换；`7..7` shell 又强制 `31 -> 15`。
- `K=14` 的 `>=15` shell 强制 `13 -> 67`，`13..14` shell 强制 `19 -> 23`，`7..7` shell 强制 `70 -> 15`。
- `K=12` 左邻已在 `t=1` 缺 1 行，`K=15` 右邻在 `t=6,7` 缺行，所以幸存相位只能是孤立两点岛。

当前 actual-load 前沿收窄为：

```text
tight-Hall CRT island PDEC  OR  moving-support SAE
```

最新接口为：

```text
K13K14TightHallCRTIslandPDECOrMovingSupportSAE
```

这一步仍不关闭全局行/列命题；它关闭的是“两个 survivor 相位可自由推广成平滑替换族”的解释。

## 80. cycle-debt shell phase graph

后续文件

```text
experiments/prime_matrix_cycle_debt_shell_phase_graph_router.py
docs/monograph/prime-matrix-cycle-debt-shell-phase-graph-router.md
data/prime-matrix-cycle-debt-shell-phase-graph-ledger.json
```

本步把 tight-Hall survivor 岛的 forced shell 继续写成供给 residue 到需求 residue 的相位边图。若支撑运动只是一个普通 CRT 周期平移，则所有 forced shell 必须共享同一个 delta；实际审计结果否定这一点。

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

相位读数：

- `K=14` 的强制边为 `13->67`、`19->23`、`70->15`，对应 delta `54,4,16`，已经排斥公共单平移。
- `K=14` 整个 forced core 最少仍需 `4` 个不同 delta。
- `K=13` 的刚性核心 `>=8`、`7..7`、`4..6` 最少需要 `7` 个不同 delta；低层大 shell 未参与最小化，但它只能增加或保持这个下界。

当前 actual-load 前沿收窄为：

```text
non-affine shell phase fragmentation PDEC  OR  multi-delta support SAE
```

最新接口为：

```text
NonAffineShellPhaseFragmentPDECOrMultiDeltaSupportSAE
```

这一步仍不关闭全局行/列命题；它关闭的是“剩余可由单一 CRT 平移相位解释”的出口。

## 81. cycle-debt multi-delta core CRT load

后续文件

```text
experiments/prime_matrix_cycle_debt_multi_delta_core_crt_load_router.py
docs/monograph/prime-matrix-cycle-debt-multi-delta-core-crt-load-router.md
data/prime-matrix-cycle-debt-multi-delta-core-crt-load-ledger.json
```

本步把多相位核心的每条相位边展开成实际 composite slots 与阻断素因子。也就是说，multi-delta 不再只是“至少几个 delta”的抽象计数，而是每个 delta lane 上实际要承载多少需求宽度、多少小/中素因子 CRT 条件。

```text
k13_enumerated_core_matching_count=96
k13_minimum_delta_count=7
k13_minimum_delta_matching_count=2
k13_best_min_delta_global_lcm_log10=36.165
k14_enumerated_core_matching_count=2
k14_minimum_delta_count=4
k14_minimum_delta_matching_count=1
k14_best_min_delta_global_lcm_log10=31.716
all_min_delta_lcms_exceed_period=true
```

结果：

- `K=14` 的最小多相位核心唯一，需求宽度 `52`，全局 lcm 约 `10^31.716`。
- `K=13` 的可枚举刚性核心需求宽度 `71`，最小 delta 方案只有 `2` 个，全局 lcm 约 `10^36.165`。
- 两者的最小 delta 核心 lcm 都远超本地周期 `5680`。

当前 actual-load 前沿收窄为：

```text
multi-delta core CRT-load PDEC  OR  K=13 low-shell full-residue SAE
```

最新接口为：

```text
MultiDeltaCoreCRTLoadPDECOrLowShellFullResidueSAE
```

这一步仍不关闭全局行/列命题；它关闭的是“multi-delta support 只是轻量相位碎裂”的解释。

## 82. cycle-debt low-shell delta skeleton

后续文件

```text
experiments/prime_matrix_cycle_debt_low_shell_delta_skeleton_router.py
docs/monograph/prime-matrix-cycle-debt-low-shell-delta-skeleton-router.md
data/prime-matrix-cycle-debt-low-shell-delta-skeleton-ledger.json
```

本步专攻上一层留下的 `K=13` 低层 `1..3` shell。它的 possible delta 是全 `0..70`，但这只是“可出现相位”而不是“必须全相位扩散”。整数规划精确给出最小 delta 骨架：

```text
low_shell_possible_delta_count=71
low_shell_minimum_delta_count=6
low_shell_minimum_delta_witness=[23,35,38,58,68,70]
low_shell_new_delta_count_over_core=2
low_shell_new_deltas_over_core=[0,66]
full_k13_delta_count_after_low_shell=9
full_k13_total_required_width=101
full_k13_global_lcm_log10=42.095
```

结论：

- low shell 单独最少需要 `6` 个 delta；
- 若沿用 `K=13` 刚性核心的 `7` 个 delta，则 low shell 只需新增 `0,66`；
- 补齐后 `K=13` 覆盖全部 `101` 需求宽度，形成 `9` lane CRT 载荷。

当前 actual-load 前沿收窄为：

```text
K=13 full-debt nine-lane CRT-load PDEC  OR  residual slack-tail SAE
```

最新接口为：

```text
K13FullDebtNineLaneCRTLoadPDECOrResidualSlackTailSAE
```

这一步仍不关闭全局行/列命题；它关闭的是“low shell 必须作为 full-residue 自由逃逸”的解释。

## 83. cycle-debt K13 full-debt nine-lane tail

后续文件

```text
experiments/prime_matrix_cycle_debt_k13_full_debt_nine_lane_tail_router.py
docs/monograph/prime-matrix-cycle-debt-k13-full-debt-nine-lane-tail-router.md
data/prime-matrix-cycle-debt-k13-full-debt-nine-lane-tail-ledger.json
```

本步把上一接口中的 residual slack-tail 具体化。K=13 九 lane 全债务分支不是“已用需求 101 之外还有一些可忽略尾部”，而是被 Hall 层账本强制留下固定的 18 槽 tail。

```text
capacity_row_count=27
demand_row_count=27
all_capacity_rows_mandatory=true
total_capacity=119
total_demand_width=101
unavoidable_tail_slot_count=18
zero_slack_layers=[1,4,7,8]
min_tail_factor_count=8
min_tail_lcm_log10=11.488
```

结论：

- 第 1 层 Hall 贴边使 27 个正容量行全部强制入局；
- 总容量与总需求差为 `18`，等于层 slack 总和，因此 tail 槽数不依赖当前匹配；
- 零 slack 层 `1,4,7,8` 让槽移动无法无成本穿过临界层；
- 在固定九 lane 的可行匹配族内，tail 至少携带 8 个互素 blocker，其 lcm 已超过本地周期。

当前 actual-load 前沿收窄为：

```text
K=13 layer-slack tail-CRT invariant PDEC  OR  moving-family SAE
```

最新接口为：

```text
K13LayerSlackTailCRTInvariantPDECOrMovingFamilySAE
```

这一步仍不关闭全局行/列命题；它关闭的是“residual slack-tail 是匹配伪影或无 CRT 成本尾部”的解释。

## 84. cycle-debt K13 tail gate drift

后续文件

```text
experiments/prime_matrix_cycle_debt_k13_tail_gate_drift_router.py
docs/monograph/prime-matrix-cycle-debt-k13-tail-gate-drift-router.md
data/prime-matrix-cycle-debt-k13-tail-gate-drift-ledger.json
```

本步把 moving-family 出口进一步拆开：如果移动后仍保留 K=13 层门形状，则应在 near-shift 窗口中看到相同 slack 向量或相同 zero-gate 集合；实际没有。

```text
hall_pass_shifts=[13,14]
same_slack_vector_shifts=[13]
same_zero_gate_set_shifts=[13]
k13_zero_slack_layers=[1,4,7,8]
k14_zero_slack_layers=[7,8,13,15]
k14_tail_increase_over_k13=13
k14_slack_l1_distance_from_k13=19
```

结论：

- `K=13` 层形状在 `K=1..16` 中唯一；
- 仅有的可动 survivor `K=14` 已发生 gate drift；
- 该 drift 丢失低门 `1,4`，新增高门 `13,15`，并额外带来 13 个 tail 槽。

当前 actual-load 前沿收窄为：

```text
K=13 gate-profile no-near-replay PDEC  OR  K14 high-gate drift SAE
```

最新接口为：

```text
K13GateProfileNoNearReplayPDECOrK14HighGateDriftSAE
```

这一步仍不关闭全局行/列命题；它关闭的是“K=13 layer-tail 可以近程同形移动复现”的解释。

## 85. cycle-debt K14 high-gate low-shell skeleton

后续文件

```text
experiments/prime_matrix_cycle_debt_k14_high_gate_low_shell_skeleton_router.py
docs/monograph/prime-matrix-cycle-debt-k14-high-gate-low-shell-skeleton-router.md
data/prime-matrix-cycle-debt-k14-high-gate-low-shell-skeleton-ledger.json
```

本步处理上一接口中的 K14 high-gate drift 分支。K14 漂移不是无结构 SAE：高门 shell 已把 core 压成两个候选，低层再经整数规划补齐。

```text
k14_high_gate_core_alternative_count=2
k14_best_core_deltas=[4,16,28,54]
k14_low_shell_minimum_delta_count=6
k14_low_shell_new_deltas_over_core=[2,48,58,70]
k14_full_delta_count_after_low_shell=8
k14_full_total_required_width=101
k14_full_global_lcm_log10=48.508
```

结论：

- K14 high-core 不是连续 moving family，只剩两个二分匹配候选；
- 低层 possible motion 被压成有限 delta skeleton；
- 最佳补齐后 K14 全债务载荷占 `8` lane，CRT lcm 约 `10^48.508`。

当前 actual-load 前沿收窄为：

```text
fixed K13 gate-profile PDEC  OR  K14 full-debt eight-lane CRT-load PDEC
```

最新接口为：

```text
K13FixedGateProfilePDECOrK14FullDebtEightLaneCRTLoadPDEC
```

这一步仍不关闭全局行/列命题；它关闭的是“K14 high-gate drift 是未登记自由 SAE”的解释。

## 86. cycle-debt two-survivor terminal CRT bifurcation

后续文件

```text
experiments/prime_matrix_cycle_debt_two_survivor_terminal_crt_bifurcation_router.py
docs/monograph/prime-matrix-cycle-debt-two-survivor-terminal-crt-bifurcation-router.md
data/prime-matrix-cycle-debt-two-survivor-terminal-crt-bifurcation-ledger.json
```

本步把 K13 固定 gate-profile 分支与 K14 八 lane full-debt 分支合并审查。两条分支不是同一支撑运动的两个近邻相位，而是终端 CRT 分叉。

```text
common_deltas=[54,58]
delta_union_count=15
delta_symmetric_difference_count=13
source_intersection_count=19
source_symmetric_difference_count=16
target_intersection_count=27
pair_intersection_count=1
union_lcm_log10=57.156
tail_union_lcm_log10=24.632
```

结论：

- 两分支 target 需求完全相同，但 source 支撑与 edge matching 大幅分叉；
- 实际 source-target 边仅 `13->67` 重合；
- lane 对称差有 `13` 条，联合 CRT lcm 约 `10^57.156`。

当前 actual-load 前沿收窄为：

```text
two-survivor terminal CRT bifurcation PDEC exclusion
```

最新接口为：

```text
TwoSurvivorTerminalCRTBifurcationPDECExclusion
```

这一步仍不关闭全局行/列命题；它关闭的是“K13/K14 可以互相吸收为同一未命名 SAE”的解释。

## 87. cycle-debt two-survivor PDEC exclusion

后续文件

```text
experiments/prime_matrix_cycle_debt_two_survivor_pdec_exclusion_router.py
docs/monograph/prime-matrix-cycle-debt-two-survivor-pdec-exclusion-router.md
data/prime-matrix-cycle-debt-two-survivor-pdec-exclusion-ledger.json
```

本步继续压缩 `TwoSurvivorTerminalCRTBifurcationPDECExclusion`。two-survivor 的真正剩余不是“两个候选相位相差多少”，而是若反例链要在两个终端 survivor 之间切换，真实链必须重写多少 actual load。

```text
common_pair_width=15
forced_rematched_target_width=86
minimum_branch_exclusive_delta_width=70
minimum_branch_exclusive_delta_lcm_log10=32.582
k14_only_assigned_width=29
k14_only_capacity_at_k13=0
k14_only_capacity_at_k14=39
k14_arrival_lcm_log10=20.205
common_source_changed_count=18
```

结论：

- 共同实际边只有 `13->67`，因此共同 anchor 最多解释 `15` 宽度；
- 剩余 `86` 宽度必须重路由，且每个分支至少 `70` 宽度落在 branch-exclusive delta 上；
- K14 侧的 `29` 宽度来自 K13 时容量全为 `0` 的 fresh-arrival source，不能被解释为原支撑平滑拖动；
- branch-exclusive CRT lcm 与 arrival lcm 均远超本地周期 `5680`。

当前 actual-load 前沿收窄为：

```text
terminal switch-arrival ColumnCRT/PDEC  OR  branch-exclusive CRT-load exclusion
```

最新接口为：

```text
TerminalSwitchArrivalColumnCRTPDECOrBranchExclusiveCRTLoadExclusion
```

这一步仍不关闭全局行/列命题；它把 two-survivor 分叉的下一阻塞点压成 fresh-arrival ColumnCRT/PDEC 与 branch-exclusive CRT-load 的排斥。

## 88. cycle-debt terminal switch arrival wall

后续文件

```text
experiments/prime_matrix_cycle_debt_terminal_switch_arrival_wall_router.py
docs/monograph/prime-matrix-cycle-debt-terminal-switch-arrival-wall-router.md
data/prime-matrix-cycle-debt-terminal-switch-arrival-wall-ledger.json
```

本步把 `TerminalSwitchArrivalColumnCRTPDECOrBranchExclusiveCRTLoadExclusion` 的 fresh-arrival 侧继续下钻。K14 的新 source 不是从 K13 的支撑连续变形而来；它们在 K13 全部被入口素数墙切断，到 K14 才出现 post-wall 合数槽。

```text
arrival_source_count=8
all_arrival_sources_zero_capacity_at_k13=true
entry_wall_lcm_log10=39.482
postwall_capacity_total=39
postwall_assigned_width_total=29
postwall_assigned_lcm_log10=20.205
entry_plus_assigned_lcm_log10=59.687
entry_plus_postwall_lcm_log10=68.361
entry_plus_postwall_coprime_to_period=true
```

结论：

- `8` 个 arrival source 在 K13 全部 `capacity=0`，且全部由 `K=13` 的 `window_position=0` 素数入口墙解释；
- K14 的 `39` 个 post-wall 槽中 `29` 槽进入实际分配；
- 入口墙与 post-wall CRT 因子都与 `5680` 互素，联合模数远超本地周期。

当前 actual-load 前沿收窄为：

```text
eight-prime entry-wall post-wall CRT exclusion
OR branch-exclusive CRT-load exclusion
```

最新接口为：

```text
EightPrimeEntryWallPostWallCRTExclusionOrBranchExclusiveCRTLoadExclusion
```

这一步仍不关闭全局行/列命题；它把 switch-arrival 的匿名 ColumnCRT 侧物化为入口素数墙与 post-wall CRT-load 的持久排斥问题。

## 89. cycle-debt coupled branch entry-wall

后续文件

```text
experiments/prime_matrix_cycle_debt_coupled_branch_entry_wall_router.py
docs/monograph/prime-matrix-cycle-debt-coupled-branch-entry-wall-router.md
data/prime-matrix-cycle-debt-coupled-branch-entry-wall-ledger.json
```

本步把 `EightPrimeEntryWallPostWallCRTExclusionOrBranchExclusiveCRTLoadExclusion` 的两个出口重新按终端分支归类。K14 的 entry-wall/post-wall 载荷和 branch-exclusive 载荷不是相互独立的逃逸路线；它们同属 K14 终端分支。

```text
k13_branch_exclusive_width=73
k13_branch_exclusive_lcm_log10=36.678
k14_branch_exclusive_width=70
k14_arrival_assigned_width=29
k14_arrival_branch_overlap_width=21
k14_branch_arrival_union_width=78
k14_branch_plus_entry_plus_postwall_lcm_log10=85.024
both_branches_plus_k14_entry_postwall_lcm_log10=99.349
```

结论：

- K14 侧 arrival 与 branch-exclusive 有 `21` 宽度重叠，但联合仍强制 `78` 宽度 actual load；
- K14 侧 `branch+entry+全部 post-wall` 的 CRT lcm 约 `10^85.024`，与 `5680` 互素；
- K13 侧则剩下 `73` 宽度 branch-exclusive 载荷，lcm 约 `10^36.678`。

当前 actual-load 前沿收窄为：

```text
K13 branch-exclusive CRT-load exclusion
OR K14 coupled entry-branch CRT wall exclusion
```

最新接口为：

```text
K13BranchExclusiveCRTLoadExclusionOrK14CoupledEntryBranchCRTWallExclusion
```

这一步仍不关闭全局行/列命题；它把松散并列出口压成按 K13/K14 终端分支区分的两个明确 CRT-load 排斥问题。

## 90. cycle-debt branch replay support-gap

后续文件

```text
experiments/prime_matrix_cycle_debt_branch_replay_support_gap_router.py
docs/monograph/prime-matrix-cycle-debt-branch-replay-support-gap-router.md
data/prime-matrix-cycle-debt-branch-replay-support-gap-ledger.json
```

本步把 `K13BranchExclusiveCRTLoadExclusionOrK14CoupledEntryBranchCRTWallExclusion` 的 moving-slot 复现解释形式化。若一个已登记阻断包 `B` 在周期坐标中平移 `T` 个本地周期后仍由同一素因子包复现，则对每个 `q in B` 有 `T=0 mod q`；因此最小非零复现周期是 `lcm(B)`。

```text
k13_branch_exclusive_width=73
k14_branch_arrival_union_width=78
k14_coupled_audit_slot_count_all_postwall=117
smallest_log10_margin_over_support_width=30.737
all_nonzero_replay_moduli_exceed_support_width=true
all_nonzero_replay_moduli_exceed_audit_slots=true
local_moving_slot_replay_excluded_for_registered_blocks=true
far_replay_still_requires_columncrt_pdec=true
```

结论：

- K13 branch-exclusive 的最小复现模数约 `10^36.678`，远超 `73` 宽度支撑；
- K14 `branch+entry+postwall` 的最小复现模数约 `10^85.024`，远超 `78` 宽度 actual 支撑和 `117` 个审计槽；
- 本地 moving-slot 复现被关闭；若终端载荷在远处复现，它不再是自由支撑运动，而是明确的 ColumnCRT/PDEC 复现包。

当前 actual-load 前沿收窄为：

```text
BranchReplayColumnCRTPDECExclusionOrIsolatedTerminalAtomAbsorption
```

这一步仍不关闭全局行/列命题；它关闭本地复现解释，并把剩余压成远程 ColumnCRT/PDEC 排斥或孤立原子吸收。

## 91. cycle-debt branch replay global dichotomy

后续文件

```text
experiments/prime_matrix_cycle_debt_branch_replay_global_dichotomy_router.py
docs/monograph/prime-matrix-cycle-debt-branch-replay-global-dichotomy-router.md
data/prime-matrix-cycle-debt-branch-replay-global-dichotomy-ledger.json
```

本步把 `BranchReplayColumnCRTPDECExclusionOrIsolatedTerminalAtomAbsorption` 的孤立原子出口分解为全局二分。登记 replay block 是有限集合；若其中某一类无限复现，则它被上一 replay lemma 提升为 P-space ColumnCRT/PDEC；若没有任何登记类无限复现，则它们只是有限原子，不能作为全局结构逃逸。

```text
registered_replay_block_count=6
minimum_p_space_columncrt_modulus_log10=36.337
maximum_p_space_columncrt_modulus_log10=103.103
persistent_registered_replay_routes_to_columncrt_pdec=true
isolated_atoms_cannot_form_infinite_registered_family=true
finite_atom_base_check_required=true
```

结论：

- 持久登记 replay 只能走 ColumnCRT/PDEC；
- 非持久登记 replay 只剩有限基例检查；
- 变更阻断包则回流 PDEC/SAE 或新 router。

当前 actual-load 前沿收窄为：

```text
BranchReplayColumnCRTPDECExclusionOrFiniteAtomBaseCheck
```

这一步仍不关闭全局行/列命题；它把孤立原子从全局结构出口中剥离，保留远程 ColumnCRT/PDEC 排斥和有限基例检查。

## 92. cycle-debt finite atom boundary bridge

后续文件

```text
experiments/prime_matrix_cycle_debt_finite_atom_boundary_bridge_router.py
docs/monograph/prime-matrix-cycle-debt-finite-atom-boundary-bridge-router.md
data/prime-matrix-cycle-debt-finite-atom-boundary-bridge-ledger.json
```

本步把 `BranchReplayColumnCRTPDECExclusionOrFiniteAtomBaseCheck` 中的有限基例检查拆成已覆盖前缀和尾段原子。旧直接方阵验证只覆盖 `P<=5000`，不能直接吸收当前 cycle-debt 原子；可用的是已归档的 `3001<=P<100000` 动态有限桥。

```text
cover_pressure_atom_count=155
cover_pressure_all_atoms_in_dynamic_finite_bridge=true
arrival_wall_atom_count=55
arrival_wall_tail_atom_count=31
total_dynamic_bridge_atom_count=179
total_post100000_tail_atom_count=31
tail_atom_p_range=[101087,134047]
```

结论：

- 前缀 `P<100000` 的当前登记原子已由动态有限桥吸收；
- 仍有 `31` 个 post-100000 tail atoms，不能由有限前缀证明关闭；
- 这些尾段原子必须进入 post-100000 runner、tail lower-sieve 或 ColumnCRT/PDEC。

当前 actual-load 前沿收窄为：

```text
BranchReplayColumnCRTPDECExclusionOrPost100000TailAtomRunner
```

这一步仍不关闭全局行/列命题；它只完成 finite atom 出口的边界分段。

## 93. cycle-debt post-100000 tail atom exact runner

后续文件

```text
experiments/prime_matrix_cycle_debt_post100000_tail_atom_exact_runner.py
docs/monograph/prime-matrix-cycle-debt-post100000-tail-atom-exact-runner.md
data/prime-matrix-cycle-debt-post100000-tail-atom-exact-ledger.json
```

本步把 `BranchReplayColumnCRTPDECExclusionOrPost100000TailAtomRunner` 的 post-100000 tail runner 逐点关闭。对 `31` 个尾段原子，runner 验证 `23` 个合数槽的记录因子均为最小因子，并验证 `8` 个 post-wall first prime 为真素数；同时每个 arrival row 的 first-prime 之前槽位全为合数。

```text
tail_atom_count=31
tail_atom_p_range=[101087,134047]
all_composite_atoms_divisible_by_recorded_factor=true
all_composite_recorded_factors_are_smallest=true
all_postwall_first_primes_verified=true
all_preprime_slots_composite_in_arrival_rows=true
finite_atom_branch_closed_for_registered_atoms=true
```

结论：

- post-100000 有限原子分支对当前登记对象已闭合；
- 它不排斥无限反例链中的持久 replay；
- 最新实际前沿只剩 branch replay ColumnCRT/PDEC 排斥。

当前 actual-load 前沿收窄为：

```text
BranchReplayColumnCRTPDECExclusion
```

这一步仍不关闭全局行/列命题；它把 finite atom 出口移除，留下单一结构性 ColumnCRT/PDEC 接口。

## 94. cycle-debt branch replay fresh-modulus escalation

后续文件

```text
experiments/prime_matrix_cycle_debt_branch_replay_fresh_modulus_escalation_router.py
docs/monograph/prime-matrix-cycle-debt-branch-replay-fresh-modulus-escalation-router.md
data/prime-matrix-cycle-debt-branch-replay-fresh-modulus-escalation-ledger.json
```

本步把 `BranchReplayColumnCRTPDECExclusion` 的固定有限 CRT 类解释继续下钻。有限原子分支已关闭；剩余若是一条持久 replay family，则它不能停留在任何登记有限模数上，因为所有后续未登记素数层都与旧模数互素，并形成新的 CRT 坐标。

```text
registered_replay_block_count=6
all_registered_blocks_have_coprime_fresh_layers=true
minimum_first_fresh_log10_gain=2.400
minimum_sample_log10_gain=19.435
finite_crt_terminal_description_excluded=true
persistent_family_requires_unbounded_modulus_or_pdec=true
```

结论：

- 固定有限 ColumnCRT 类不再是终端稳定结构；
- 持久 replay 必须无界扩模，或在某个新素数层触发 PDEC/ColumnCRT 缺陷；
- 若扩模被尾段筛吸收，则剩余转为 tail-sieve stability contradiction。

当前 actual-load 前沿收窄为：

```text
UnboundedFreshModulusEscalationPDECOrTailSieveStabilityContradiction
```

这一步仍不关闭全局行/列命题；它把固定有限 CRT 接口推进为无穷新素数层的扩模/筛稳定接口。

## 95. cycle-debt fresh-modulus 到 tail-sieve 桥接

新增文件

```text
experiments/prime_matrix_cycle_debt_fresh_modulus_tail_sieve_bridge_router.py
docs/monograph/prime-matrix-cycle-debt-fresh-modulus-tail-sieve-bridge-router.md
data/prime-matrix-cycle-debt-fresh-modulus-tail-sieve-bridge-ledger.json
```

本步把上一节的无界 fresh-modulus 接口转成 actual-load 可审查对象。逻辑是：

```text
fixed finite ColumnCRT terminal excluded
and no fresh-layer PDEC/ColumnCRT
=> one forbidden residue class per fresh prime
=> B3 tail rough object
=> external/standard tail sieve conditional closure
```

关键读数：

```text
registered_replay_block_count=6
minimum_first_fresh_log10_gain=2.400
minimum_sample_log10_gain=19.435
tail_object_interface_closed=true
conditional_external_tail_sieve_closed=true
strict_self_contained_tail_sieve_closed=false
fresh_layer_pdec_excluded=false
```

actual-load 前沿因此改写为：

```text
FreshLayerPDECColumnCRTExclusionOrSelfContainedTailSieveStabilityClosure
```

严格自足 branch-replay 剩余基：

```text
FreshLayerPDECColumnCRTExclusion AND SelfContainedDusartReciprocalPrimeProofAppendixXGe10372
```

接受外部或标准筛输入时，tail-sieve 分支可从该 branch-replay 接口移除，只剩 fresh-layer PDEC/ColumnCRT 排斥。该结论仍不是行/列命题的全局无条件闭合，因为它尚未排斥 fresh-layer PDEC，也尚未给出 strict 自足 Mertens/PNT/Dusart 尾段证明。

## 96. cycle-debt fresh-modulus tail-sieve strict 自足同步

新增文件

```text
experiments/prime_matrix_cycle_debt_fresh_modulus_tail_self_contained_sync_router.py
docs/monograph/prime-matrix-cycle-debt-fresh-modulus-tail-self-contained-sync-router.md
data/prime-matrix-cycle-debt-fresh-modulus-tail-self-contained-sync-ledger.json
```

本步同步后续 strict 解析证书到 branch-replay fresh-modulus 分支。上一桥接中 strict tail-sieve 仍开放，是因为旧 B3 桥接证书尚未导入后续的 theta/PNT+B1 自足闭合。现在读取最新证书：

```text
strict_self_contained_mertens_tail_proved_latest=true
b3_tv_strict_self_contained_synchronized_latest=true
strict_self_contained_tail_sieve_closed_for_branch_replay=true
```

因此 actual-load 前沿从二选一

```text
FreshLayerPDECColumnCRTExclusionOrSelfContainedTailSieveStabilityClosure
```

继续收缩为单一 branch-replay 出口：

```text
FreshLayerPDECColumnCRTExclusion
```

这是一次同步型推进：它不新增全局定理，只删除已经由后续 strict 证书吸收的旧 tail-sieve 解析粗原子。真正下一步是证明 fresh layer 的相位复用、投影碰撞、moving support 逃逸或 ColumnCRT 缺陷不能在无限反例链中持续存在。

## 97. cycle-debt fresh-layer 本地投影碰撞排除

新增文件

```text
experiments/prime_matrix_cycle_debt_fresh_layer_local_collision_router.py
docs/monograph/prime-matrix-cycle-debt-fresh-layer-local-collision-router.md
data/prime-matrix-cycle-debt-fresh-layer-local-collision-ledger.json
```

本步对 `FreshLayerPDECColumnCRTExclusion` 继续下钻：registered branch replay 的本地支撑窗口已经太短，无法在 fresh prime 层产生投影碰撞。

```text
period_p=5680
registered_block_count=6
all_sample_fresh_primes_coprime_to_period_p=true
all_registered_samples_injective_on_local_windows=true
minimum_first_fresh_minus_support_width=178
minimum_first_fresh_minus_audit_slots=178
```

理由是若 `gcd(5680,ell)=1` 且窗口长度小于 `ell`，则 `a+j*5680 mod ell` 对窗口内槽位 `j` 单射。当前所有登记 block 的 fresh prime sample 都满足该条件。

actual-load 前沿继续收缩为：

```text
FreshLayerSupportMotionEscapeOrRemoteColumnCRTPDECExclusion
```

剩余已不是本地相位碰撞，而是支撑运动逃逸、远程 P-space ColumnCRT/PDEC 复现或未登记 moving family。

## 98. cycle-debt fresh support-motion 全局路由

新增文件

```text
experiments/prime_matrix_cycle_debt_fresh_support_motion_global_router.py
docs/monograph/prime-matrix-cycle-debt-fresh-support-motion-global-router.md
data/prime-matrix-cycle-debt-fresh-support-motion-global-ledger.json
```

本步把上一节剩余中的 `SupportMotionEscape` 再下钻。registered support motion 的两个本地机制均已关闭：

```text
local_fresh_layer_projection_collision_excluded=true
registered_local_support_motion_excluded=true
registered_support_motion_escape_closed=true
```

其中第二项来自同一阻断包的 `lcm(B)` 复现屏障；最小 cycle replay 对支撑宽度的十进对数余量为 `30.737`。若 registered block 无限复现，既然不能本地漂移，就只能进入全局二分中的固定 P-space ColumnCRT 类，最小 P-space 模数约 `10^36.337`。

actual-load 前沿继续收缩为：

```text
RemotePspaceColumnCRTExclusionOrUnregisteredMovingFamilyRouter
```

这一步不排斥远程 ColumnCRT，也不排斥未登记 moving family；它只把 registered support-motion escape 从剩余接口中删除。

## 99. cycle-debt remote ColumnCRT feedback

新增文件

```text
experiments/prime_matrix_cycle_debt_remote_columncrt_feedback_router.py
docs/monograph/prime-matrix-cycle-debt-remote-columncrt-feedback-router.md
data/prime-matrix-cycle-debt-remote-columncrt-feedback-ledger.json
```

本步继续压缩上一节的远程 ColumnCRT 出口。远程 P-space ColumnCRT 若只是裸固定周期类，则并不是新的终端结构：孤立有限原子已由 post-100000 exact runner 吸收；固定有限 CRT replay 类已由 fresh-modulus escalation 证明为非终端；若无 fresh-layer PDEC/ColumnCRT，则 non-PDEC 无界 fresh layers 已接入 B3 tail-sieve 对象并由 strict 同步关闭。

关键读数：

```text
registered_remote_block_count=6
minimum_remote_pspace_columncrt_modulus_log10=36.337
maximum_remote_pspace_columncrt_modulus_log10=103.103
minimum_first_fresh_log10_gain=2.400
minimum_sample_fresh_log10_gain=19.435
bare_remote_pspace_columncrt_terminal_closed=true
materialized_fresh_layer_pdec_columncrt_excluded=false
unregistered_moving_family_excluded=false
row_column_unconditional_closed=false
```

actual-load 前沿继续收缩为：

```text
MaterializedFreshLayerPDECColumnCRTExclusionOrUnregisteredMovingFamilyRouter
```

这一步不排斥材料化 fresh-layer PDEC/ColumnCRT，也不排斥未登记 moving family；它只把裸 remote P-space ColumnCRT 终端解释从剩余接口中删除。

## 100. cycle-debt fresh-layer PDEC admission firewall

新增文件

```text
experiments/prime_matrix_cycle_debt_fresh_layer_pdec_admission_firewall_router.py
docs/monograph/prime-matrix-cycle-debt-fresh-layer-pdec-admission-firewall-router.md
data/prime-matrix-cycle-debt-fresh-layer-pdec-admission-firewall-ledger.json
```

本步继续压缩上一节的材料化 fresh-layer PDEC/ColumnCRT 出口。registered support 内 fresh prime 投影在窗口内单射，不能形成本地材料化 PDEC；远程材料化若要成为 PDEC，必须通过 PDEC family 显式准入边界。该边界要求同一 formal unit、固定 phase map、去重后三物理 primitive atoms 以上、非二点 tautology、二秩以上且 cap-stable；否则回流 ColumnCRT/SAE/refined PDEC/sparse extractor/multiplicity。

关键读数：

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
row_column_unconditional_closed=false
```

actual-load 前沿继续收缩为：

```text
FutureExplicitPrimitiveFreshLayerPDECSchemaIfNewOrUnregisteredMovingFamilyRouter
```

这一步不证明未来 primitive fresh-layer PDEC schema 不存在，也不排斥未登记 moving family；它只关闭当前语料中的无名材料化 PDEC/ColumnCRT 口径。

## 101. cycle-debt branch-replay current frontier zero

新增文件

```text
experiments/prime_matrix_cycle_debt_branch_replay_current_frontier_zero_router.py
docs/monograph/prime-matrix-cycle-debt-branch-replay-current-frontier-zero-router.md
data/prime-matrix-cycle-debt-branch-replay-current-frontier-zero-ledger.json
```

本步把上一节的 `if new` 与 moving-family 口径做当前实例压缩。未来 fresh-layer PDEC schema 尚未提交，未来 moving-family schema 也尚未提交；二者在当前语料中是准入防火墙，不是活动数学障碍。最终输入防火墙同时确认当前语料没有隐藏终端。

关键读数：

```text
current_fresh_layer_pdec_frontier_closed=true
future_explicit_primitive_fresh_layer_pdec_schema_submitted=false
unregistered_moving_family_schema_submitted=false
future_pdec_schema_admission_discipline_closed=true
future_sparse_schema_admission_discipline_closed=true
final_input_firewall_boundary_closed=true
no_hidden_terminal_remaining=true
cycle_debt_branch_replay_current_materialized_frontier_zero=true
row_column_unconditional_closed=false
```

actual-load 的 cycle-debt branch-replay 子前沿在当前物化语料内清零：

```text
CycleDebtBranchReplayCurrentMaterializedFrontierZeroWithFutureSchemaFirewall
```

全局仍剩：

```text
GlobalFinalInputsStillOpen
```

这一步不证明未来 schema 永不存在，也不关闭完整行/列无条件命题。

## 102. early-zero gap CRT asymmetry router

新增文件

```text
experiments/prime_matrix_early_zero_gap_crt_asymmetry_router.py
docs/monograph/prime-matrix-early-zero-gap-crt-asymmetry-router.md
data/prime-matrix-early-zero-gap-crt-asymmetry-ledger.json
```

本步处理最新用户提示中的“早期零行必产生跨行相邻素数大间隙”接口。严格引理如下：若
第 `k` 行 `[(k-1)P+1,kP]` 没有素数，则左侧最近素数 `a` 与右侧最近素数 `b` 相邻，且
`b-a>P`。若 `1<k<P`，被跨越的行窗口完全位于 `P^2` 之前；若右端素数越过 `P^2`，则进入
更强的平方锚/对角分支。

关键读数：

```text
early_zero_gap_lemma_proved=true
crt_gap_asymmetry_standalone_contradiction_proved=false
persistent_phase_routes_to_pdec_columncrt=true
sparse_phase_routes_to_sae=true
nonperiodic_endpoint_routes_to_h3_dsb_kls=true
nc_blk_or_external_dibfi_closed=false
row_column_unconditional_closed=false
```

这说明 CRT 非对称的精确边界已经确定：`M_P` 周期复制小素因子覆盖，不复制相邻素数端点。
若端点相位持久复现，则进入 `PDEC/ColumnCRT`；若孤立出现，则进入 `SAE`；若覆盖持续但素端点
不能周期化，则回到 `H3-DSB/KLS` 的 `NC-BLK` 或外部 `DI/BFI` 分支。

actual-load 前沿更新为：

```text
EarlyZeroGapCarrierAsymmetryRoutedToH3DSBNCBLKOrExternalDIBFI;GlobalFinalInputsStillOpen
```

这一步是路由闭合，不是全局行/列无条件证明闭合。

## 103. early-zero period-lift carrier drift router

新增文件

```text
experiments/prime_matrix_early_zero_period_lift_carrier_drift_router.py
docs/monograph/prime-matrix-early-zero-period-lift-carrier-drift-router.md
data/prime-matrix-early-zero-period-lift-carrier-drift-ledger.json
```

本步把 `P,k` 行 CRT 周期复现后的不对称问题继续压实。若 `x` 是 `P` 零行乘数，则对
`L_P=prod_{q<P}q` 和任意 `t>=0`，`x+tL_P` 仍为零行乘数；整数区间平移量为 `P L_P`。
这是反例链在 CRT 行周期中的精确复现。

但相邻素数载体端点不是小素因子覆盖对象。令 `a_t,b_t` 为提升后零行区间的左右最近素数，
则 CRT 周期不推出

```text
a_t=a_0+tP L_P
b_t=b_0+tP L_P
```

关键读数：

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

因此后续 CRT 周期中的“不对称矛盾”不是一个裸矛盾，而是命名三分流：持久端点漂移进入
`PDEC/ColumnCRT`，孤立漂移进入 `SAE`，非周期漂移但覆盖压力持续则回到 `H3-DSB/KLS`
的 `NC-BLK` 或外部 `DI/BFI` 分支。

actual-load 前沿更新为：

```text
PeriodLiftCarrierDriftRoutedToPersistentPDECOrSparseSAEOrH3DSBNCBLK;GlobalFinalInputsStillOpen
```

这一步继续保持诚实边界：行/列全局无条件证明尚未闭合。

## 104. Q2 carrier-stage endpoint inversion router

新增文件

```text
experiments/prime_matrix_q2_carrier_stage_crt_asymmetry_router.py
docs/monograph/prime-matrix-q2-carrier-stage-crt-asymmetry-router.md
data/prime-matrix-q2-carrier-stage-crt-asymmetry-ledger.json
```

本步继续处理用户提示中的“早期零行相邻素数 `Q1<Q2` 在之后 `Q2` 阶 CRT 周期中产生什么不对称”接口。
若早期第 `k` 行 `[(k-1)P+1,kP]` 无素数并由相邻素数 `Q1<Q2` 跨越，则在 `Q2<P^2`
的主分支中，开间隙 `(Q1,Q2)` 内每个合数都有小于 `P` 的素因子；若 `Q2>=P^2`，则进入平方锚/对角端点分支。

关键新增观察是端点反转：令 `M_{<=Q2}=prod_{\ell<=Q2}\ell`，则对任意 `t>=1`

```text
Q1+t*M_{<=Q2} == 0 mod Q1
Q2+t*M_{<=Q2} == 0 mod Q2
```

所以完整 `Q2` 阶轮不会复制“两个端点仍为素数”的真实链，而会把两个素端点复制成被自身整除的复合端点。
若只用 `M_{<Q2}`，左端 `Q1` 已被自身零类杀掉，右端 `Q2` 的素性仍不由 CRT 强制。

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

因此 `Q2` 阶不对称确实给出一个显式矛盾点，但只排除了“全轮 CRT 同时复现覆盖块和素端点”的跳步。
若放弃素端点，只让闭覆盖块持久复现，则进入 `ColumnCRT/PDEC`；若孤立出现，则进入 `SAE`；
若通过移动端点、素层或支撑逃避反转，则回到 `moving-family/H3-DSB/KLS`。

actual-load 前沿更新为：

```text
Q2StageEndpointInversionRoutedToColumnCRTPDECOrSparseSAEOrMovingEndpointH3DSB;GlobalFinalInputsStillOpen
```

这一步仍不是行/列全局无条件证明；它关闭的是 `Q2` 阶端点稳定复现这一最窄跳步。

## 105. Q2 endpoint replacement aperture-growth router

新增文件

```text
experiments/prime_matrix_q2_endpoint_replacement_aperture_growth_router.py
docs/monograph/prime-matrix-q2-endpoint-replacement-aperture-growth-router.md
data/prime-matrix-q2-endpoint-replacement-aperture-growth-ledger.json
```

本步继续把 `Q2` 阶端点反转推进为真实链的孔径增长债务。早期零行端点边界精确为：

```text
Q1<=kP-P, with equality possible at k=2
Q2>kP
```

在 `Q2<P^2` 主分支中，开间隙 `(Q1,Q2)` 内每个合数有小于 `P` 的素因子；完整 `Q2` 阶轮又包含
`Q1,Q2`，所以 `[Q1,Q2]+t*M_{<=Q2}` 对 `t>=1` 是闭复合块。真实相邻素数端点必须落在块外，故新间隙满足

```text
new_gap >= old_gap + 2
```

当前读数：

```text
full_q2_replay_makes_closed_carrier_composite=true
endpoint_replacement_gap_growth_per_replay_at_least=2
same_aperture_replay_impossible=true
bounded_aperture_replay_finite=true
persistent_moving_aperture_routes_to_pdec_columncrt=true
sparse_replacement_routes_to_sae=true
unbounded_replacement_routes_to_h3_dsb=true
row_column_unconditional_closed=false
```

因此固定有界孔径的无限 CRT 复现被排除：若原闭载体宽度为 `W0`，固定孔径 `W` 最多容纳
`floor((W-W0)/2)` 次端点替换。无限反例链若继续，只能扩孔或移动支撑；固定有限规则的扩孔进入
`ColumnCRT/PDEC`，孤立替换进入 `SAE`，无界移动回到 `H3-DSB/KLS` 与 moving-family 出口。

actual-load 前沿更新为：

```text
EndpointReplacementApertureGrowthNoBoundedReplayOrMovingSupportPDECSAEH3DSB;GlobalFinalInputsStillOpen
```

这一步不是全局闭合；它把 `Q2` 阶之后的真实链压力从端点反转推进到有界孔径 no-go。

## 106. Q2 endpoint fresh-layer cascade router

新增文件

```text
experiments/prime_matrix_q2_endpoint_fresh_layer_cascade_router.py
docs/monograph/prime-matrix-q2-endpoint-fresh-layer-cascade-router.md
data/prime-matrix-q2-endpoint-fresh-layer-cascade-ledger.json
```

本步把上一节留下的“扩孔/移动”继续压成新素层级联。若第 `j` 阶全轮模数为 `M_j`，复现后的
闭复合块右侧真实相邻素数为 `B_{j+1}`，则

```text
B_{j+1} > copied block right edge >= M_j
```

所以 `B_{j+1}` 是旧有限端点层之外的新素数层。一旦下一阶全轮纳入 `B_{j+1}`，下一次复现又会把
`B_{j+1}` 的复制点变成被自身整除的复合点。令 `L_j=log M_j`，得到级联下界：

```text
L_{j+1} >= L_j + log(B_{j+1}) > 2 L_j
```

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

结论：有界孔径 no-go 之后，任何无限延续若仍沿全轮端点复现推进，就不能停在固定有限 CRT 周期；
它必须无界加入 fresh endpoint primes。若这些新素层以固定相位模板持久复现，则进入
`ColumnCRT/PDEC`；若孤立，则进入 `SAE`；若无 PDEC 地无界加入，则成为每个新素层禁一个相位的
`tail-sieve/H3-DSB/KLS` 对象。

actual-load 前沿更新为：

```text
FreshEndpointLayerCascadeNoFiniteCRTPeriodOrPDECSAEH3TailSieve;GlobalFinalInputsStillOpen
```

这一步排除了固定有限 CRT 周期终端，但仍不是行/列全局无条件证明。

## 107. Q2 fresh-layer tail-mass dichotomy router

新增文件

```text
experiments/prime_matrix_q2_fresh_layer_tail_mass_dichotomy_router.py
docs/monograph/prime-matrix-q2-fresh-layer-tail-mass-dichotomy-router.md
docs/monograph/prime-matrix-q2-fresh-layer-tail-mass-dichotomy-router.json
data/prime-matrix-q2-fresh-layer-tail-mass-dichotomy-ledger.json
```

本步把上一节的 non-PDEC fresh-layer 级联继续拆成尾质量二分。若 fresh layer 不触发
`ColumnCRT/PDEC`，则每个新素数层只能作为一个单余类禁相位进入局部孔径。设第 `j` 层新素数为
`B_j`、局部孔径为 `W_j`，该层形式质量不超过

```text
W_j / B_j
```

上一节已经给出 fresh modulus `M_j` 的对数至少倍增，且 `B_{j+1}>M_j`；端点替换的原生孔径债务只给出 `W_j=W0+2j` 的线性下界。
因此受控孔径分支满足

```text
sum_j W_j / B_j < infinity
```

并被压入 `SAE`。若 `log W_j` 反复追赶 `log M_j`，则这不再是局部端点替换，而是孔径爆炸或全局支撑运动，
必须回到 `H3-DSB`、moving-support `PDEC` 或新的显式支撑运动账本。

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

actual-load 前沿更新为：

```text
ControlledFreshLayerTailMassSAEOrApertureExplosionH3PDEC;GlobalFinalInputsStillOpen
```

这一步关闭受控 fresh-tail 尾质量出口；全局无条件证明仍需要排斥孔径爆炸、moving-support H3/DSB
与 fresh-layer PDEC。

## 108. Q2 aperture-explosion schema-firewall router

新增文件

```text
experiments/prime_matrix_q2_aperture_explosion_schema_firewall_router.py
docs/monograph/prime-matrix-q2-aperture-explosion-schema-firewall-router.md
docs/monograph/prime-matrix-q2-aperture-explosion-schema-firewall-router.json
data/prime-matrix-q2-aperture-explosion-schema-firewall-ledger.json
```

本步把上一节剩下的孔径爆炸/支撑运动口径同步到既有防火墙。受控 fresh-tail 已进入 `SAE`；
若孔径增长仍要追赶 fresh modulus，则它已经不是局部端点替换，而必须材料化为以下显式对象之一：

```text
support motion
blocker-package change
fresh-layer PDEC/ColumnCRT
explicit moving-family schema
```

已有链条提供三个同步输入：registered support-motion 本地漂移已关闭；当前材料化 fresh-layer PDEC/ColumnCRT
已被 admission firewall 关闭；当前 branch-replay 物化前沿已清零。因此当前无名 aperture-explosion 终端不可保留。

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

actual-load 前沿更新为：

```text
Q2ApertureExplosionCurrentSchemaFirewall;GlobalFinalInputsStillOpen
```

这一步只是当前语料的 schema 防火墙同步；它不证明未来显式 moving-family/PDEC schema 不存在，也不关闭全局最终输入。

## 109. Q2 CRT ladder to final exact-source alignment router

新增文件

```text
experiments/prime_matrix_q2_to_final_exact_source_alignment_router.py
docs/monograph/prime-matrix-q2-to-final-exact-source-alignment-router.md
docs/monograph/prime-matrix-q2-to-final-exact-source-alignment-router.json
data/prime-matrix-q2-to-final-exact-source-alignment-ledger.json
```

本步把 Q2 阶 CRT 梯的剩余与最终 exact-source 原子精确对齐。Q2 路线已证明：

```text
cover block replay != prime endpoint replay
controlled fresh tail => SAE
unnamed aperture explosion => schema firewall
```

因此当前 Q2 局部没有可保留的无名终端。关键边界是：CRT/轮筛刚性只控制位置和相位，不生成
Cauchy/dispersion 前 actual source 在 exact `(u,v)` fiber 上的质量分散。故 Q2 路线若要继续全局化，
必须回到最终 exact-source 原子或外部谱输入。

当前读数：

```text
q2_current_local_terminal_removed=true
q2_position_rigidity_controls_source_mass=false
active_final_inputs_imported=true
current_final_attack_imported=true
preterminal_exact_uv_fiber_aperiodicity_imported=true
source_domain_rank_atom_package_imported=true
dstructure_promotion_boundary_imported=true
dstructure_independently_accepted=false
row_column_unconditional_closed=false
```

actual-load 前沿更新为：

```text
NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource OR ExternalDIBFIKuznetsovDispersionTheoremMatch; DStructureRankinPromotionIndependentAcceptanceOpen
```

这一步不是最终证明；它把 Q2/CRT 方向的全局剩余精确回接到 actual-source fiber 非集中、
外部谱输入与 DStructure/Rankin 晋级验收。

## 110. Global CRT homogeneity frontier router

新增文件

```text
experiments/prime_matrix_global_crt_homogeneity_frontier_router.py
docs/monograph/prime-matrix-global-crt-homogeneity-frontier-router.md
docs/monograph/prime-matrix-global-crt-homogeneity-frontier-router.json
data/prime-matrix-global-crt-homogeneity-frontier-ledger.json
```

本步专门审计“全局 CRT 周期中是否存在本质相位矛盾”这一最新剩余接口。Q1/Q2 端点不对称的强结论仍然保留：
完整 `Q2` 阶轮会把相邻素数端点复制为被自身整除的复合点，所以同端点稳定 replay 不可能。
但若端点移动，进入的是 fresh endpoint/source 问题；受控 non-PDEC 尾量被 `SAE` 吸收，持久相关进入
`PDEC/ColumnCRT`，孔径失控必须提交 explicit moving-family schema。

关键同步是 CRT 同质性：

```text
M_Y squarefree, r∤M_Y prime
{a+tM_Y: 0<=t<r} mod r = all residue classes
=> exactly one lift is deleted by r
```

所以有限 CRT 前缀本身是均匀删相位，不是全局矛盾。Euler 乘积给出临界密度直觉，
但不是长度 `P` 短区间的 actual occupancy 证明。要把容量/相位矛盾升级为定理，必须提供
actual-source exact-UV 非集中，或外部谱输入；strict 内部链条已经把前者同步到逐 primitive
alpha/delta 核表。

当前读数：

```text
pure_finite_crt_global_phase_contradiction_found=false
global_crt_homogeneity_blocks_pure_phase_contradiction=true
q2_crt_position_rigidity_routed_to_exact_source=true
source_rank_package_synced_to_pointwise_kernel=true
alpha_row_anchor_phase_emission_formula_proved=false
row_column_unconditional_closed=false
```

actual-load 前沿更新为：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger
AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

这一步不是最终证明；它关闭纯 CRT 全局相位矛盾的误出口，并把主攻硬点压到 source/kernel 表的第一发射公式。

## 111. Global CRT terminal saturation sync router

新增文件

```text
experiments/prime_matrix_global_crt_terminal_saturation_sync_router.py
docs/monograph/prime-matrix-global-crt-terminal-saturation-sync-router.md
docs/monograph/prime-matrix-global-crt-terminal-saturation-sync-router.json
data/prime-matrix-global-crt-terminal-saturation-sync-ledger.json
```

本步把 `AlphaRowAnchorPhaseEmissionFormulaLedger` 之后的既有 strict 下钻全部导入 global CRT 路线：
alpha row 局部几何前沿已同步到 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve`；该终端门已拆成
PDEC same-set 作用域匹配或自足 Kuznetsov/DLS；KZ/DLS 形式层回到终端家族；非递归破环包回到
signed 坐标-来源闭环；seed-cycle-cut 分支也已经饱和。因此 global CRT/Q1-Q2 路线的最新非循环剩余
不再是 alpha row 粗硬点，而是：

```text
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
```

当前读数：

```text
pure_crt_homogeneity_firewall_imported=true
alpha_row_local_frontier_terminal_synced=true
pdec_cap_clean_kls_terminal_split_imported=true
kuznetsov_dls_route_returns_to_terminal_family=true
pdec_scope_branch_saturated=true
nonrecursive_breaker_cycle_detected=true
seed_cycle_cut_branch_saturated=true
row_column_unconditional_closed=false
```

actual-load 前沿更新为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact)
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 112. Global CRT branch trace frontier router

新增文件

```text
experiments/prime_matrix_global_crt_branch_trace_frontier_router.py
docs/monograph/prime-matrix-global-crt-branch-trace-frontier-router.md
docs/monograph/prime-matrix-global-crt-branch-trace-frontier-router.json
data/prime-matrix-global-crt-branch-trace-frontier-ledger.json
```

本步把 `NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact` 进一步压缩。若新公式沿旧路线分裂为
alpha-side、same-row、row-level、signed-source，则只形成已登记固定点；反分裂公式又要求原子 joint rows
声明；原子声明又压到内置 signed coefficient/pairing 闭式；该闭式最终需要
`ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn`。

这正是 Q1/Q2-CRT 全局路线与真实链之间的最新显式交叉点：CRT 和 unsigned skeleton 只给位置与相位，
不能决定 signed coefficient 的取向/local-factor 奇数据。若要形成真正容量/相位矛盾，必须在同一
formal unit 的 Cauchy 前 branch trace 中同时给出 word、coefficient、alpha/delta pairing、exact UV
和失败回流。

当前读数：

```text
pdec_scope_branch_still_open=true
builtin_pairing_reduced_to_exact_branch_trace=true
acyclic_same_set_scope_match_proved=false
exact_atomic_joint_branch_trace_signed_coefficient_formula_proved=false
row_column_unconditional_closed=false
```

actual-load 前沿更新为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn)
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

这一步不是最终证明；它把“新 joint 公式”硬点压到 exact atomic branch trace signed coefficient
公式，并保留 PDEC same-set 作用域匹配作为独立可攻证书。

## 113. Global CRT signed payload sync router

新增文件

```text
experiments/prime_matrix_global_crt_signed_payload_sync_router.py
docs/monograph/prime-matrix-global-crt-signed-payload-sync-router.md
docs/monograph/prime-matrix-global-crt-signed-payload-sync-router.json
data/prime-matrix-global-crt-signed-payload-sync-ledger.json
```

本步把 global CRT/Q1-Q2 最新前沿继续同步到 signed payload 层。
`ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn` 已由 strict payload 前沿压成
`AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn`。另一方面，PDEC same-set 手臂在当前内部自足语料中
已饱和到新 joint 公式线；而新 joint 公式线已通过 branch-trace 链回到 signed payload。

这给出一个更清楚的全局断点：有限 CRT 周期扩张能复制零同余类和可见坐标 trace，却不能生成
orientation、local factor、signed coefficient 这些 payload 字段。因此纯 CRT 全局相位矛盾仍不能作为
最终闭合；若不引入新的外部或 scope-PDEC 证书，内部自足路线的最窄硬点就是 signed payload constructor。

当前读数：

```text
exact_atomic_trace_reduced_to_signed_payload=true
finite_crt_cannot_generate_signed_payload=true
pdec_internal_arm_saturated_to_new_joint=true
external_or_new_pdec_scope_still_open=true
strict_internal_self_contained_basis_sharpened=true
atomic_signed_payload_constructor_proved=false
acyclic_same_set_scope_match_proved=false
row_column_unconditional_closed=false
```

内部自足 actual-load 前沿更新为：

```text
AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

保留新 scope/PDEC 输入的总活动基为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn)
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

这一步不是最终证明；它关闭的是“branch trace 作为未拆原子”这一粗口径，并把全局主攻点压到
pre-assignment signed payload 或新的 PDEC scope 证书。

## 114. Predecessor-gap P-CRT uniformity router

新增文件

```text
experiments/prime_matrix_predecessor_gap_pcrt_uniformity_router.py
docs/monograph/prime-matrix-predecessor-gap-pcrt-uniformity-router.md
docs/monograph/prime-matrix-predecessor-gap-pcrt-uniformity-router.json
data/prime-matrix-predecessor-gap-pcrt-uniformity-ledger.json
```

本步审计最新提出的前素数间隙路线：当 `P-p^-` 较大时，完整 `P` 阶 CRT 周期是否会在非 P 列产生
分布均匀性或反射对称性矛盾。审计结论是：完整周期中非 P 列均匀性本身是精确 CRT 恒等式。
在 `M_{\le P}=P M_{<P}` 的完整周期内，每个 `c in F_P^*` 都有 `phi(M_{<P})` 个非零交集元素；
映射 `n -> -n` 精确配对 `c` 与 `P-c`。前素数间隙不改变这个恒等式。

前素数间隙只产生初始方阵第一行的实际素数缺口：列 `p^-+1,...,P-1` 没有第一行素数。把完整周期
均匀性局部化到初始 `P x P` 方阵，需要额外证明：

```text
LocalizedPCRTColumnUniformityTransferToInitialPxPSquare
```

当前读数：

```text
complete_wheel_non_p_uniformity_proved=true
complete_wheel_reflection_symmetry_proved=true
localized_transfer_to_initial_square_proved=false
large_predecessor_gap_symmetry_contradiction_found=false
non_p_column_uniformity_contradiction_found=false
row_column_unconditional_closed=false
```

样本扫描 `P<=5000` 的最大前素数间隙显示：最大样本 `P=1361,p^-=1327,gap=34`，第一行缺口列 `33` 个，
在整个 `P x P` 方阵中均被后续行素数补上；所有记录样本的非 P 零列总数为 `0`。该扫描只定位风险
形态，不作为证明输入。

因此该路线不产生独立无条件闭合，最新活动基仍为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn)
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 115. Localized P-CRT transfer / Linnik=2 barrier router

新增文件

```text
experiments/prime_matrix_localized_pcrt_transfer_linnik2_barrier_router.py
docs/monograph/prime-matrix-localized-pcrt-transfer-linnik2-barrier-router.md
docs/monograph/prime-matrix-localized-pcrt-transfer-linnik2-barrier-router.json
data/prime-matrix-localized-pcrt-transfer-linnik2-barrier-ledger.json
```

本步把 `LocalizedPCRTColumnUniformityTransferToInitialPxPSquare` 的列侧内容压成精确的点态 AP 屏障：

```text
PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2
```

即对每个非零 `c mod P` 都要证明存在素数 `ell<=P^2` 且 `ell≡c mod P`。这正是 prime-modulus
least-prime-in-AP 的 Linnik 指数 `2` 型断言。完整 `P`-wheel 的非 P 列均匀性只是一条全周期平均恒等式；
BV/平均 AP 均匀性也只控制几乎所有列，不能给出每个初始短 AP 的点态首素数。

当前读数：

```text
localized_pcrt_transfer_active=true
column_occupancy_equivalent_to_least_prime_ap=true
linnik2_barrier_identified=true
localized_transfer_current_corpus_proved=false
pointwise_linnik2_ap_theorem_proved=false
row_column_unconditional_closed=false
```

样本扫描 `P<=3000` 中，`429` 个素数模数无缺失剩余类，最大首素数行号 `108`；这只是风险定位。

最新活动基为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
 OR PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2)
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

因此局部化 P-CRT 路线没有给出新的无条件闭合；它要么提交新的点态 AP 定理，要么回流到结构前沿。

## 116. Linnik=2 nonprincipal character obstruction router

新增文件

```text
experiments/prime_matrix_linnik2_nonprincipal_character_obstruction_router.py
docs/monograph/prime-matrix-linnik2-nonprincipal-character-obstruction-router.md
docs/monograph/prime-matrix-linnik2-nonprincipal-character-obstruction-router.json
data/prime-matrix-linnik2-nonprincipal-character-obstruction-ledger.json
```

本步把 `PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2` 的失败形态写成有限角色正交的精确障碍。
设

```text
theta_a(P)=sum_{ell<=P^2, ell prime, ell=a mod P} log ell
T_chi(P)=sum_{a in F_P^*} chi(a) theta_a(P)
N_a(P)=sum_{chi!=chi0} conjugate(chi(a)) T_chi(P)
```

则

```text
theta_a(P)=(T_0(P)+N_a(P))/(P-1)
```

所以零列缺陷 `theta_a(P)=0` 等价于非主投影精确命中 `N_a(P)=-T_0(P)`，并强制

```text
sum_{chi!=chi0}|T_chi(P)|^2 >= T_0(P)^2/(P-2)
```

当前读数：

```text
theta_character_expansion_exact=true
zero_column_forces_negative_projection=true
zero_column_forces_energy_spike=true
pointwise_projection_bound_proved=false
row_column_unconditional_closed=false
```

有限样本 `P<=3000` 中 theta 零剩余类总数为 `0`，最大负缺口比例为 `0.686688`，发生于 `P=73`；
该样本不作为证明输入。

最新活动基变为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
 OR PointwiseNonprincipalProjectionBoundBelowPrincipalMassAtXEqualsP2)
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

这一步关闭的是“只靠完整 CRT 平均或 AP 平均即可推出每个短列命中”的误出口；真正剩余是逐剩余类的
非主负相位投影界，或回流到 PDEC scope / signed payload / ExactUV 结构前沿。

## 117. Linnik=2 rank-one phase capacity router

新增文件

```text
experiments/prime_matrix_linnik2_rankone_phase_capacity_router.py
docs/monograph/prime-matrix-linnik2-rankone-phase-capacity-router.md
docs/monograph/prime-matrix-linnik2-rankone-phase-capacity-router.json
data/prime-matrix-linnik2-rankone-phase-capacity-ledger.json
```

本步将上一节的点态投影障碍拆成容量与相位两部分。零列给出 Cauchy 必要条件

```text
||T_nonprincipal||_2^2 >= T_0(P)^2/(P-2)
```

但总能量超过该地板并非矛盾；要排斥的是

```text
rho_a(P)=-N_a(P)/T_0(P)=1
```

也就是某个 residue evaluation 向量 `v_a` 方向上的 rank-one 负投影达到主项。各 `v_a` 满足 simplex
内积规则：

```text
<v_a,v_b>=P-2  (a=b)
<v_a,v_b>=-1   (a!=b)
```

有限样本 `P<=3000` 中，容量-only 不能排除的样本数为 `423/429`，最大总能量/零列地板比例为
`5.751979`（`P=2953`），但最大负投影比例只在 `P=73` 达到 `0.686688`，仍离 `1` 有 `0.313312`
余量。样本不作为证明，只用于定位容量路线的假阳性。

当前读数：

```text
energy_floor_necessary_condition_closed=true
energy_capacity_only_route_not_enough=true
evaluation_vector_simplex_geometry_closed=true
rankone_phase_coherence_exclusion_proved=false
row_column_unconditional_closed=false
```

最新活动基：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
 OR RankOneNegativeEvaluationProjectionPhaseCoherenceExclusionAtP2)
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

因此当前最窄接口已经不是 L2 容量，而是 evaluation simplex 的点态负相位极化。

## 118. Three-claims frontier / rank-one explicit formula router

新增文件

```text
experiments/three_claims_frontier_rankone_explicit_formula_router.py
docs/monograph/three-claims-frontier-rankone-explicit-formula-router.md
docs/monograph/three-claims-frontier-rankone-explicit-formula-router.json
data/three-claims-frontier-rankone-explicit-formula-ledger.json
```

本步先把合著稿三个命题的前沿拆开：

| 命题 | 最新剩余 |
| --- | --- |
| 行/列 | `RankOneNegativeEvaluationProjectionPhaseCoherenceExclusionAtP2` |
| 二次筛/two-point | `I3CoreTrueResidualTotalLargeIncidenceOrExternalDIBFIKLSWindow` |
| RH | `IndependentRefereeAcceptanceOfAllRHControlledExits` |

然后继续攻击行/列最新硬点。由上一层公式，

```text
rho_a(P)=1-theta(P^2;P,a)/(T_0(P)/(P-1))
```

所以 `rho_a(P)<1` 对所有 `a` 成立，等价于

```text
theta(P^2;P,a)>0    for every a in F_P^*
```

这正是 prime modulus 下每个非零 AP 类在 `P^2` 前有素数的 sharp positivity。显式公式把它压成：
每个 residue 的带符号非主零点包必须小于约 `P` 的主项。

当前读数：

```text
rankone_equivalent_to_theta_ap_positivity=true
explicit_formula_barrier_identified=true
current_classical_inputs_sufficient=false
row_column_unconditional_closed=false
two_point_unconditional_closed=false
rh_unconditional_closed=false
```

最新活动基：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
 OR ExplicitAPZeroPacketBoundBeatingMainTermAtXEqualsP2)
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

该证书说明：继续走解析 AP 路线时，目标已不是平均密度或总能量，而是 `x=P^2, q=P` 的逐类显式零点包强界。

## 119. Explicit AP zero-packet Siegel split router

新增文件

```text
experiments/prime_matrix_explicit_ap_zero_packet_siegel_split_router.py
docs/monograph/prime-matrix-explicit-ap-zero-packet-siegel-split-router.md
docs/monograph/prime-matrix-explicit-ap-zero-packet-siegel-split-router.json
data/prime-matrix-explicit-ap-zero-packet-siegel-split-ledger.json
```

本步把最新 AP 零包硬点

```text
ExplicitAPZeroPacketBoundBeatingMainTermAtXEqualsP2
```

拆成：

| 分支 | 当前状态 |
| --- | --- |
| `SiegelExceptionalBiasExclusionAtSquareScale` | 未证；无 Siegel 零点不是已认证无条件输入，且实零项在 `P^2` 尺度可与主项同阶 |
| `NonrealZeroPacketResiduePhaseCancellationAtXEqualsP2` | 未证；需要逐剩余类相位抵消，平均定理和总能量不能排除单方向集中 |
| `TrivialAndFiniteExplicitFormulaTermsBelowMainMarginAtP2` | 已从主硬点分离；待前两项给出余量后由显式常数账本吸收 |

当前读数：

```text
siegel_branch_closed=false
nonreal_branch_closed=false
trivial_terms_isolated=true
classical_inputs_sufficient=false
row_column_unconditional_closed=false
```

最新活动基：

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

该证书说明：若继续走解析 AP 路线，不能只说“零点包小”；必须分别证明实例外/Siegel 偏置不能制造危险半类，以及非实零点包不能在单个 `residue` 方向上相位同向集中。

## 120. Siegel quadratic half-class margin router

新增文件

```text
experiments/prime_matrix_siegel_quadratic_halfclass_margin_router.py
docs/monograph/prime-matrix-siegel-quadratic-halfclass-margin-router.md
docs/monograph/prime-matrix-siegel-quadratic-halfclass-margin-router.json
data/prime-matrix-siegel-quadratic-halfclass-margin-ledger.json
```

本步把 `SiegelExceptionalBiasExclusionAtSquareScale` 压成二次角色半类投影余量：

```text
r_quad(P)=|T_chi(P)|/T0(P)
T_chi(P)=sum_{ell<=P^2} chi_P(ell) log ell
```

危险半类的平均主项余量正比于 `1-r_quad(P)`。因此该分支的自足闭合目标不再是泛泛的“无 Siegel 偏置”，而是：

```text
QuadraticHalfClassSquareScaleBiasMarginTheorem
```

或外部接受足够强的

```text
EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale
```

当前读数：

```text
quadratic_projection_identity_closed=true
halfclass_margin_theorem_proved=false
effective_no_siegel_input_accepted=false
siegel_branch_closed=false
row_column_unconditional_closed=false
```

最新活动基：

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

该证书的实质进展是：Siegel 分支的容量/相位矛盾不再停留在“实零可能危险”，而是变成一个明确的二次半类余量命题；但该命题仍未在当前语料中证明。

## 121. Nonreal half-class simplex phase router

新增文件

```text
experiments/prime_matrix_nonreal_halfclass_simplex_phase_router.py
docs/monograph/prime-matrix-nonreal-halfclass-simplex-phase-router.md
docs/monograph/prime-matrix-nonreal-halfclass-simplex-phase-router.json
data/prime-matrix-nonreal-halfclass-simplex-phase-ledger.json
```

本步把非实零点包硬点压成半类 simplex 的 rank-one 投影问题。删除主角色与二次角色后：

```text
R_a=(P-1)theta_a(P)-T0(P)-chi_2(a)T_2(P)
```

且 evaluation 向量分裂为两个正交的二次半类 simplex：

```text
<w_a,w_b>=P-3, -2, 0
```

其中 `-2` 只发生在同一二次半类的不同 residue，`0` 发生在相反二次半类之间。零列要求非实残差在某个半类单方向提供至少

```text
(1-|T_2|/T0)T0
```

的负投影。

当前读数：

```text
halfclass_simplex_geometry_closed=true
zero_requirement_after_quadratic_removal_closed=true
nonreal_energy_floor_closed=true
nonreal_rankone_projection_exclusion_proved=false
row_column_unconditional_closed=false
```

最新活动基：

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

该证书关闭的是“非实零包无结构残差”的误出口；剩余仍是点态相位排斥，而不是总能量容量。

## 122. Nonreal half-class compensation variance router

新增文件

```text
experiments/prime_matrix_nonreal_halfclass_compensation_variance_router.py
docs/monograph/prime-matrix-nonreal-halfclass-compensation-variance-router.md
docs/monograph/prime-matrix-nonreal-halfclass-compensation-variance-router.json
data/prime-matrix-nonreal-halfclass-compensation-variance-ledger.json
```

本步把上一层的 rank-one 负投影继续拆成同半类补偿恒等式。对 `H_s={a:chi_2(a)=s}`，

```text
mu_s=(T0+sT2)/(P-1),
R_a=(P-1)(theta_a-mu_s),
sum_{a in H_s} R_a=0.
```

因此零列不是单独的负尖峰，而是

```text
one missing coordinate + same-halfclass positive compensation.
```

Cauchy 给出的尖孔地板

```text
sum R_a^2 >= ((P-1)mu_s)^2*h/(h-1)
```

是锐的：等号态由平铺补偿达到。这说明 formal energy envelope 超过地板不等于 actual contradiction；必须证明 actual prime-induced compensation 不能长期平铺，或把持久平铺相位送入 ColumnCRT/PDEC。

当前读数：

```text
halfclass_centering_identity_closed=true
zero_column_compensation_mass_closed=true
sharp_one_hole_variance_floor_closed=true
capacity_only_sufficiency_rejected=true
actual_prime_compensation_nonconcentration_proved=false
row_column_unconditional_closed=false
```

最新活动基：

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

该证书的实质进展是：非实分支的剩余不再是抽象相位集中，而是同半类补偿质量的非平铺/持久 ColumnCRT 二分。行/列命题仍未无条件闭合。

## 123. Half-class ratio Fourier lock router

新增文件

```text
experiments/prime_matrix_halfclass_ratio_fourier_lock_router.py
docs/monograph/prime-matrix-halfclass-ratio-fourier-lock-router.md
docs/monograph/prime-matrix-halfclass-ratio-fourier-lock-router.json
data/prime-matrix-halfclass-ratio-fourier-lock-ledger.json
```

本步把同半类补偿的“平铺/非平铺”接口进一步转成 multiplicative ratio 坐标。固定假想缺孔 `a0` 后，同半类通过 `u=a0^{-1}a` 变成二次剩余子群 `Q`。若

```text
f_a0(u)=theta(P^2;P,a0*u),
c_a0=sum_{u!=1}f_a0(u)/(h-1),
```

则有精确恒等式：

```text
one-point variance excess
= (P-1)^2 * punctured flatness.
```

更关键的是，平铺补偿等价于所有 `Q` 上非平凡 Fourier 系数同时满足

```text
F_psi=theta_a0-c_a0.
```

因此全局 CRT 结构硬点不再只是“容量是否够”，而是：

```text
HalfClassRatioFourierLockExclusionOrColumnCRTPDEC.
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

最新活动基：

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

该证书关闭的是“半类补偿平铺没有结构”的误出口。剩余是排斥持久全频率 ratio 锁，或把它作为 ColumnCRT/PDEC/moving-family 终端缺陷处理。

## 124. Half-class twist-pair character lock router

新增文件

```text
experiments/prime_matrix_halfclass_twist_pair_character_lock_router.py
docs/monograph/prime-matrix-halfclass-twist-pair-character-lock-router.md
docs/monograph/prime-matrix-halfclass-twist-pair-character-lock-router.json
data/prime-matrix-halfclass-twist-pair-character-lock-ledger.json
```

本步把上一节的二次剩余 ratio-Fourier 锁接回标准 Dirichlet 角色投影。若 `psi` 是 `Q` 上的非平凡角色，`chi` 是它到 `F_P^*` 的任一扩张，则另一扩张为 `chi*chi_2`。对 `a0 in H_s` 有精确恒等式：

```text
F_psi(a0)=chi(a0)*(T_chi+s*T_{chi chi_2})/2.
```

所以持久零列补偿必须使所有配对角色投影同时满足：

```text
chi(a0)*(T_chi+s*T_{chi chi_2})/2 = theta(P^2;P,a0)-c_a0.
```

这把剩余硬点压成：

```text
QuadraticTwistPairCharacterOrbitLockExclusionOrColumnCRTPDEC
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

最新活动基：

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

该证书关闭的是“全频率锁仍可能只是坐标表象”的误出口。剩余不是有限扫描可替代的命题，而是必须自足排斥全配对角色同步相位轨道锁，或把它纳入 ColumnCRT/PDEC/moving-family 终端缺陷链。

## 125. Half-class log independence degeneracy router

新增文件

```text
experiments/prime_matrix_halfclass_log_independence_degeneracy_router.py
docs/monograph/prime-matrix-halfclass-log-independence-degeneracy-router.md
docs/monograph/prime-matrix-halfclass-log-independence-degeneracy-router.json
data/prime-matrix-halfclass-log-independence-degeneracy-ledger.json
```

本步把精确轨道锁继续压到素数支撑层。对不同非零 residue `a,b`，

```text
theta_a=theta_b
```

等价于对应素数乘积相等。由唯一分解和 residue 支撑互斥，若 `a!=b` 则只能

```text
S_a(P)=S_b(P)=empty.
```

因此 `P>=7` 时，punctured 半类精确平铺不可能是正平铺；它只能退化为：

```text
c=0 and S_{a0*u}(P)=empty for every u in Q, u!=1.
```

这把剩余硬点压成：

```text
PuncturedHalfClassZeroSupportDegeneracyExclusionOrColumnCRTPDEC
```

当前读数：

```text
log_prime_product_independence_closed=true
positive_exact_punctured_flatness_excluded=true
orbit_lock_routed_to_zero_support_degeneracy=true
punctured_halfclass_zero_support_degeneracy_excluded=false
row_column_unconditional_closed=false
```

最新活动基：

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

该证书关闭的是“精确轨道锁仍可能以正质量平铺存在”的误出口。剩余不是对数独立问题，而是必须证明同半类除缺孔外不可能全部没有 `P^2` 内素数到达，或把这种极端支撑退化纳入 ColumnCRT/PDEC/moving-family 终端缺陷链。

## 126. Half-class single-residue capacity router

新增文件

```text
experiments/prime_matrix_halfclass_single_residue_capacity_router.py
docs/monograph/prime-matrix-halfclass-single-residue-capacity-router.md
docs/monograph/prime-matrix-halfclass-single-residue-capacity-router.json
data/prime-matrix-halfclass-single-residue-capacity-ledger.json
```

本步把 punctured 半类全零支撑继续压到容量不等式。若退化存在，则某个半类全部质量都集中在单个 residue；而单个 residue 在 `P^2` 前最多贡献

```text
2P log P.
```

因此只要证明

```text
min_s Theta_s(P)>2P log P
```

即可排除退化。等价二次投影形式为：

```text
T0(P)*(1-|T_chi(P)|/T0(P))>4P log P.
```

这把剩余硬点压成：

```text
QuadraticHalfClassMassBeatsSingleResidueCapacityAtP2
```

当前读数：

```text
single_residue_deterministic_capacity_closed=true
zero_support_degeneracy_implies_capacity_failure_closed=true
quadratic_halfclass_mass_beats_single_residue_capacity_proved=false
row_column_unconditional_closed=false
```

最新活动基：

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

该证书关闭的是“支撑退化不能与总质量账本对接”的误出口。剩余是自足证明二次半类质量在 square scale 下超过单 residue 容量，或把容量失败作为显式二次角色/ColumnCRT/PDEC 终端缺陷处理。

## 127. Half-class capacity margin factorization router

新增文件

```text
experiments/prime_matrix_halfclass_capacity_margin_factorization_router.py
docs/monograph/prime-matrix-halfclass-capacity-margin-factorization-router.md
docs/monograph/prime-matrix-halfclass-capacity-margin-factorization-router.json
data/prime-matrix-halfclass-capacity-margin-factorization-ledger.json
```

本步把半类容量门分解为主质量因子与二次投影缺口。精确等价式为：

```text
min_s Theta_s(P)>2P log P
<=> 1-|T_chi(P)|/T0(P) > 4P log P/T0(P).
```

若有 Chebyshev 级主质量下界

```text
T0(P)>=c0(P)P^2,
```

则所需二次投影缺口只有

```text
4 log P/(c0(P)P).
```

这把剩余硬点压成：

```text
QuadraticProjectionGapBeatsLogOverPThresholdAtSquareScale
```

当前读数：

```text
projection_gap_equivalence_closed=true
log_over_p_threshold_reduction_closed=true
quadratic_projection_gap_beats_threshold_proved=false
row_column_unconditional_closed=false
```

最新活动基：

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

该证书关闭的是“容量失败没有相位尺度”的误出口。剩余是自足排斥 `|T_chi|/T0 >= 1-O(logP/P)` 的 ultra-near-one 二次投影缺陷，或把它作为显式 ColumnCRT/PDEC/moving-family 终端缺陷处理。

## 128. Quadratic projection large splitting router

新增文件

```text
experiments/prime_matrix_quadratic_projection_large_splitting_router.py
docs/monograph/prime-matrix-quadratic-projection-large-splitting-router.md
docs/monograph/prime-matrix-quadratic-projection-large-splitting-router.json
data/prime-matrix-quadratic-projection-large-splitting-ledger.json
```

本步将 `QuadraticProjectionGapBeatsLogOverPThresholdAtSquareScale` 拆成少数半类质量阈值与低/高素数层。精确等价式为：

```text
1-|T_chi(P)|/T0(P) > 4P log P/T0(P)
<=> min_s Theta_s(P)>2P log P.
```

写

```text
Theta_s(P)=L_s(P)+G_s(P),
L_s(P)=sum_{ell<P, chi_P(ell)=s} log ell,
G_s(P)=sum_{P<ell<=P^2, chi_P(ell)=s} log ell.
```

则低 CRT 层整体只有

```text
L_+(P)+L_-(P)=theta(P-1)<=P log P,
```

不超过少数半类阈值 `2P log P` 的一半。因此低模 CRT 层不能单独闭合该接口；任何持久反例必须表现为某个大素数二次半类分裂层 `G_s(P)<=2P log P`。

这把剩余硬点压成：

```text
LargePrimeQuadraticSplittingMinorityMassBeatsTwoPLogPAtSquareScale
```

失败出口命名为：

```text
UltraNearOneQuadraticProjectionDefectToLargeSplittingPDECOrSiegelPacket
```

当前读数：

```text
minority_mass_equivalence_closed=true
low_crt_capacity_insufficiency_closed=true
large_prime_quadratic_splitting_mass_proved=false
row_column_unconditional_closed=false
```

最新活动基：

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

该证书关闭的是“继续在 `ell<P` 低 CRT 周期中寻找全局投影矛盾”的误出口。剩余必须攻击大素数二次分裂质量，或把极端分裂荒漠作为显式 PDEC/Siegel 包处理。

## 129. Large splitting beta-gap router

新增文件

```text
experiments/prime_matrix_large_splitting_beta_gap_router.py
docs/monograph/prime-matrix-large-splitting-beta-gap-router.md
docs/monograph/prime-matrix-large-splitting-beta-gap-router.json
data/prime-matrix-large-splitting-beta-gap-ledger.json
```

本步把 `LargePrimeQuadraticSplittingMinorityMassBeatsTwoPLogPAtSquareScale` 改写成高区间二次角色投影和显式公式预算。令：

```text
G_s(P)=sum_{P<ell<=P^2, chi_P(ell)=s} log ell,
H0=G_++G_-,
Hchi=G_+-G_-.
```

则

```text
min_s G_s(P)>2P log P
<=> 1-|Hchi|/H0 > 4P log P/H0.
```

若显式公式预算为

```text
|Hchi|/H0 <= R_beta(P)+E_zero(P),
R_beta(P)=(P^(2 beta)-P^beta)/(beta H0),
```

则闭合条件是

```text
R_beta(P)+E_zero(P)<1-4P log P/H0.
```

无剩余零包时，实零临界 gap `delta=1-beta` 由

```text
R_(1-delta)(P)=1-4P log P/H0
```

确定，渐近尺度为 `delta_crit~2/P`。所以持久失败必须是 `beta=1-O(1/P)` 的超近实零，或非实零/端点/素数幂残差同向相干。

这把剩余硬点压成：

```text
SquareScaleQuadraticBetaGapAndZeroPacketResidualBudgetAtP2
```

失败出口命名为：

```text
UltraCloseRealZeroOrCoherentZeroPacketLargeSplittingPDEC
```

当前读数：

```text
high_projection_equivalence_closed=true
beta_gap_critical_scale_identified=true
beta_gap_and_zero_packet_budget_proved=false
row_column_unconditional_closed=false
```

最新活动基：

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

该证书关闭的是“继续在普通 CRT 容量语言中寻找闭合”的误出口。剩余必须是有效 `1/P` 级 beta-gap、非实零包残差预算，或显式超近实零/相干零包 PDEC。

## 130. Beta-gap Page sparsity router

新增文件

```text
experiments/prime_matrix_beta_gap_page_sparsity_router.py
docs/monograph/prime-matrix-beta-gap-page-sparsity-router.md
docs/monograph/prime-matrix-beta-gap-page-sparsity-router.json
data/prime-matrix-beta-gap-page-sparsity-ledger.json
```

本步把

```text
SquareScaleQuadraticBetaGapAndZeroPacketResidualBudgetAtP2
```

中的实零失败分支继续压缩。上一层已说明无剩余零包时临界形态是

```text
beta_P > 1 - C(P)/P.
```

Page/Landau 唯一例外零区域是

```text
beta > 1 - c_Page/logQ.
```

只要

```text
P > C(P)logQ/c_Page,  P<=Q,
```

超近实零载体就落入 Page 区域。因此在接受 Page 唯一性与常数适配后，同一 `Q`
盒中至多有一个这样的实零载体。若存在固定周期或正密度的 CRT 载体复现，它会在同一
`Q` 范围内产生多个超近实零载体，从而与 Page 唯一性冲突。

这把剩余硬点压成：

```text
PageExceptionalSingletonCarrierOrNonrealZeroPacketResidualBudget
```

失败出口命名为：

```text
MovingPageSingletonCarrierPDECOrCoherentZeroPacket
```

当前读数：

```text
page_region_inclusion_algebra_closed=true
page_uniqueness_constants_internalized=false
moving_singleton_carrier_excluded=false
nonreal_zero_packet_residual_proved=false
row_column_unconditional_closed=false
```

最新活动基：

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

该证书关闭的是“超近实零多载体族可作为稳定 CRT 复现通道”的误出口。剩余必须排斥 Page moving singleton、给出自足 `1/P` 级 beta-gap，或证明非实零包/端点残差低于大分裂 slack。

## 131. Terminal-row CRT atom router

新增文件

```text
experiments/prime_matrix_terminal_row_crt_atom_router.py
docs/monograph/prime-matrix-terminal-row-crt-atom-router.md
docs/monograph/prime-matrix-terminal-row-crt-atom-router.json
data/prime-matrix-terminal-row-crt-atom-ledger.json
```

本步把 `P=5` 的 `23,29` 与 `P=7` 的 `43,47,53` 例子写成终端 CRT 原子证书：

```text
P=5:  last_row_units=[23], next_row_units=[29]
P=7:  last_row_units=[43,47], next_row_units=[53]
```

这些数在所有 `q<=P` 的小素数模下均非零，所以假设它们由 `<=P` 小素数整除会直接矛盾。
同时它们都位于下一素数平方之前，因此 reduced atom 一旦出现就由平方根门强制为素数。

一般引理：

```text
1<n<p_next^2 and gcd(n,M_{<=P})=1  =>  n prime.
```

这给出一个可复用的反例链/真实链交叉点：反例链若声称指定终端原子被小素覆盖，真实 CRT
向量立即反驳；但若要排除所有大 `P` 的零行类缺漏，还必须证明短行中存在 reduced atom。
完整 `M_{<=P}` 周期的对称性和周期性只给全周期单位残基均匀，不给这个短行局部化。

最新硬点改写为：

```text
TerminalRowReducedResidueExistenceOrLocalizedPCRTTransfer
```

并回流到：

```text
PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2OrAPZeroPacketFrontier
PageExceptionalSingletonCarrierOrNonrealZeroPacketResidualBudget
AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
```

该证书关闭的是指定终端原子的“小素吸收”误出口，不是全局行/列命题证明。

## 132. Terminal-row square-phase bridge router

新增文件

```text
experiments/prime_matrix_terminal_row_square_phase_bridge_router.py
docs/monograph/prime-matrix-terminal-row-square-phase-bridge-router.md
docs/monograph/prime-matrix-terminal-row-square-phase-bridge-router.json
data/prime-matrix-terminal-row-square-phase-bridge-ledger.json
```

本步把

```text
TerminalRowReducedResidueExistenceOrLocalizedPCRTTransfer
```

收窄到平方锚特殊相位 Jacobsthal/PDEC 接口。末行缺失等价于

```text
P^2-(1..P-1)
```

被 `q<P` 全覆盖；下一行缺失等价于

```text
P^2+(1..P-1)
```

被 `q<P` 全覆盖。任一侧全覆盖都会使 `P^2` 在 `M_<P` 周期中落入长度 `P-1`
覆盖块的起点深处。

由于既有审计已经发现全周期长覆盖块存在，不能再试图证明普通 Jacobsthal 最大块 `<P-1`。
下一步必须攻击特殊相位：

```text
SquarePhaseSpecialPhaseLongBlockPDECExclusion
```

即证明 `P^2` 这个具体相位不能持续对齐长覆盖块；若能对齐，则把它登记为固定相位
`PDEC/SAE/ColumnCRT` 并排斥或吸收。

该证书是接口合流，不是行/列命题无条件闭合。

## 133. Terminal-square downstream frontier sync router

新增文件

```text
experiments/prime_matrix_terminal_square_phase_downstream_frontier_sync_router.py
docs/monograph/prime-matrix-terminal-square-phase-downstream-frontier-sync-router.md
docs/monograph/prime-matrix-terminal-square-phase-downstream-frontier-sync-router.json
data/prime-matrix-terminal-square-phase-downstream-frontier-sync-ledger.json
```

本步把 terminal-row square-phase bridge 的旧硬点

```text
SquarePhaseSpecialPhaseLongBlockPDECExclusion
```

同步为仓库已有下游前沿的上游别名。已有链条已经把它分别压入：

```text
HalfGridSurvivorBeatsActivatedTailSupportOrBoundaryWordPDEC
NoSlotTailPrimePhaseBandDensityPDECExclusion
PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2
ExplicitAPZeroPacketBoundBeatingMainTermAtXEqualsP2
PageExceptionalSingletonCarrierOrNonrealZeroPacketResidualBudget
AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
```

因此最新 terminal-square 口径不再停在普通平方相位长块，而是同步到 AP 零点包、signed payload、
same-set PDEC 和若干全局输入的 consolidated 剩余基。该同步防止把较旧接口误当作最新硬点；
它不构成行/列命题无条件闭合。

## 134. Strict source declaration / payload / ExactUV unification router

新增文件

```text
experiments/prime_matrix_strict_source_declaration_payload_exactuv_unification_router.py
docs/monograph/prime-matrix-strict-source-declaration-payload-exactuv-unification-router.md
docs/monograph/prime-matrix-strict-source-declaration-payload-exactuv-unification-router.json
data/prime-matrix-strict-source-declaration-payload-exactuv-unification-ledger.json
```

本步把 signed payload 与 ActualEmitterExactUV 两个 strict 内部源线接口同步为同一个
pre-Cauchy actual source declaration packet。payload 侧需要它生成非循环 basis word/signed
coefficient 来源恒等式；ExactUV 侧需要它生成 source-domain entropy 与 fixed exact `(u,v)`
polylog fiber bound。

合流后的直接接口为：

```text
PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket
```

字段包括：

```text
declaration_line
source_tuple_domain_entropy
primitive_summand_rows
basis_word_signed_coefficient_identity
alpha_delta_prepushforward_identity
fixed_exact_uv_fiber_bound
no_downstream_recovery
named_return_partition
```

当前语料没有该 packet；因此本步是硬点压缩，不是行/列命题无条件闭合。并行开放项仍包括：

```text
PageExceptionalSingletonCarrierOrNonrealZeroPacketResidualBudget
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
ExplicitModelGapAndFiniteDPRCLedger
RatePreservationLedger_FOR_moving_atom_packet
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 135. Strict source declaration downstream sync router

新增文件

```text
experiments/prime_matrix_strict_source_declaration_downstream_sync_router.py
docs/monograph/prime-matrix-strict-source-declaration-downstream-sync-router.md
docs/monograph/prime-matrix-strict-source-declaration-downstream-sync-router.json
data/prime-matrix-strict-source-declaration-downstream-sync-ledger.json
```

本步将 common packet 的字段下游拆开，得到当前更精确的 strict source lane 基：

```text
BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
RatePreservationLedger_FOR_moving_atom_packet
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

普通 joint constructor 线被证实为固定点：它经 alpha-side、same-row、row-level origin table
回到 signed-source 来源环，不能作为 packet 的非循环证明。保持反分裂的路线必须进入原子 joint rows，
而该路线的 signed 首缺口正是每条 atomic row 的内置 signed coefficient/pairing 闭式值。

这一步只是下游同步，不是行/列命题无条件闭合。下一直接主攻：

```text
BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
```

## 136. Strict signed lane cycle closure router

新增文件

```text
experiments/prime_matrix_strict_signed_lane_cycle_closure_router.py
docs/monograph/prime-matrix-strict-signed-lane-cycle-closure-router.md
docs/monograph/prime-matrix-strict-signed-lane-cycle-closure-router.json
data/prime-matrix-strict-signed-lane-cycle-closure-ledger.json
```

本步确认 strict signed/payload 子线已经形成完整闭环：

```text
PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket
-> BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
-> ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn
-> AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
-> NoncircularAtomicBasisWordSignedCoefficientOriginIdentityBeforePushforward
-> PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket
```

闭环结论是：环内任何节点都不能再作为 strict 自足证明的终点。下一非循环输入必须是新的
primitive signed payload/trace 工件，或把回流转成 well-founded terminal descent，或走独立的
PDEC same-set scope 证书。

最新非循环出口：

```text
NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact
AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
```

ExactUV entropy/fiber、RatePreservation 与 DStructure/Rankin 仍独立开放。

## 137. Strict new primitive payload source-atom alignment router

新增文件

```text
experiments/prime_matrix_strict_new_primitive_payload_source_atom_alignment_router.py
docs/monograph/prime-matrix-strict-new-primitive-payload-source-atom-alignment-router.md
docs/monograph/prime-matrix-strict-new-primitive-payload-source-atom-alignment-router.json
data/prime-matrix-strict-new-primitive-payload-source-atom-alignment-ledger.json
```

本步把 signed-lane 闭环后的 `NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact` 拆成最低字段合同。
真正能破环的 primitive payload/trace 工件必须同时携带 same formal unit lock、pre-Cauchy actual
source object、signed payload formula、complete key partition、source-domain absolute entropy、
fixed-key exact-UV local multiplicity 与 no-cycle/no-terminal-recovery 条件。

对齐后，new primitive 出口不再是独立无名终端，而是回到：

```text
ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger
```

其三原子仍未证明：

```text
ActualPreCauchySourceDomainAbsoluteEntropyLedger
CompletePrimitiveEmitterKeyPartitionLedger
FixedKeyExactUVLocalMultiplicityO1Ledger
```

当前语料没有提交独立 new primitive 工件；外部谱输入、terminal descent、same-set PDEC 与
DStructure/Rankin 独立验收仍是未闭合边界。

## 138. Strict source entropy downstream cycle sync router

新增文件

```text
experiments/prime_matrix_strict_source_entropy_downstream_cycle_sync_router.py
docs/monograph/prime-matrix-strict-source-entropy-downstream-cycle-sync-router.md
docs/monograph/prime-matrix-strict-source-entropy-downstream-cycle-sync-router.json
data/prime-matrix-strict-source-entropy-downstream-cycle-sync-ledger.json
```

本步确认上一轮的 source-domain entropy 首原子不是新的终点。它沿已归档证书继续下钻为：

```text
source entropy
-> signed row coefficient law
-> basis weight source
-> internal arithmetic basis expansion
-> noncanonical basis alphabet
-> signed coordinate-source cycle
```

坐标-来源环已由 cycle guard 判定为互相定义而非证明。因此最新严格活动基同步为：

```text
((AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput
AND CompletePrimitiveEmitterKeyPartitionLedger
AND FixedKeyExactUVLocalMultiplicityO1Ledger)
OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
OR ExternalDIBFIKuznetsovDispersionTheoremMatch)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本步不关闭行/列命题；它只删除“source entropy 首原子可由 signed-source 环自证”的误出口。

## 139. Strict cycle-cut / terminal descent unified frontier router

新增文件

```text
experiments/prime_matrix_strict_cyclecut_terminal_descent_unified_frontier_router.py
docs/monograph/prime-matrix-strict-cyclecut-terminal-descent-unified-frontier-router.md
docs/monograph/prime-matrix-strict-cyclecut-terminal-descent-unified-frontier-router.json
data/prime-matrix-strict-cyclecut-terminal-descent-unified-frontier-ledger.json
```

本步把上一节 source-entropy 下游的两个出口继续合并审计：

```text
source entropy
-> cycle-cut OR terminal descent
cycle-cut -> PDEC same-set OR new joint formula
terminal descent -> canonical-lock OR new joint formula OR independent source bridge
PDEC same-set -> new joint formula, with conditional PDEC/external input retained
new joint formula -> pre-Cauchy joint declaration line
```

导入结果为：

```text
source_entropy_exit_imported=true
seed_cycle_cut_branch_saturated=true
terminal_descent_macrocycle_detected=true
pdec_internal_branch_saturated=true
new_joint_formula_reduced_to_declaration_line=true
pre_cauchy_joint_declaration_line_proved=false
row_column_unconditional_closed=false
```

因此 strict 内部自足线当前第一生产性单点压成：

```text
PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple
```

完整 joint 字段基仍为：

```text
PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple
AND JointEmitterPrimitiveSummandRowsFormulaBeforePushforward
AND JointEmitterPrepushforwardWordCoefficientIdentityLedger
AND JointEmitterNoDownstreamRecoveryAndNamedReturnLedger
```

统一保留剩余基为：

```text
((PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple
AND JointEmitterPrimitiveSummandRowsFormulaBeforePushforward
AND JointEmitterPrepushforwardWordCoefficientIdentityLedger
AND JointEmitterNoDownstreamRecoveryAndNamedReturnLedger)
OR AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
OR IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop
OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
OR ExternalDIBFIKuznetsovDispersionTheoremMatch)
AND CompletePrimitiveEmitterKeyPartitionLedger
AND FixedKeyExactUVLocalMultiplicityO1Ledger
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本步的实质推进是删除三个误出口：cycle-cut 不能靠顺序拆分破环，terminal descent 不能靠宏循环当下降，PDEC same-set 在当前内部语料中不能当独立无条件出口。行/列命题仍未无条件闭合，下一直接硬点是提交真正的 pre-Cauchy joint declaration line，或给出 canonical-lock、independent bridge、PDEC/外部谱等独立输入。

## 140. Strict cycle-cut unified antisplit downstream sync router

新增文件

```text
experiments/prime_matrix_strict_cyclecut_unified_antisplit_downstream_sync_router.py
docs/monograph/prime-matrix-strict-cyclecut-unified-antisplit-downstream-sync-router.md
docs/monograph/prime-matrix-strict-cyclecut-unified-antisplit-downstream-sync-router.json
data/prime-matrix-strict-cyclecut-unified-antisplit-downstream-sync-ledger.json
```

本步把上一节的 `PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple`
继续沿仓库已有下游证书同步。同步边为：

```text
ordinary joint declaration
-> explicit joint alpha/delta constructor rule
-> signed-source fixed point unless replaced
antisplit route
-> AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing
-> BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
ExactUV gate
-> ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
```

导入结果：

```text
ordinary_joint_declaration_route_rejected_as_nonproof=true
antisplit_atomic_route_imported=true
atomic_rows_reduced_to_builtin_pairing=true
exactuv_entropy_fiber_split_imported=true
built_in_signed_pairing_proved=false
actual_emitter_source_domain_entropy_proved=false
exact_uv_map_fixed_pair_polylog_fiber_bound_proved=false
row_column_unconditional_closed=false
```

因此最新内部下游基为：

```text
BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
AND ActualEmitterSourceDomainEntropyLedger
AND ExactUVMapFixedPairPolylogFiberBoundLedger
```

统一保留剩余基改写为：

```text
((BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
AND ActualEmitterSourceDomainEntropyLedger
AND ExactUVMapFixedPairPolylogFiberBoundLedger)
OR AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
OR IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop
OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
OR ExternalDIBFIKuznetsovDispersionTheoremMatch)
AND CompletePrimitiveEmitterKeyPartitionLedger
AND FixedKeyExactUVLocalMultiplicityO1Ledger
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本步删除的是“普通 joint declaration 可直接闭合”的误出口。若不提交内置 signed coefficient/pairing 闭式，ordinary constructor 只会回到 signed-source 固定点；若不证明 ExactUV entropy/fiber，则 source lane 也不能晋级。行/列命题仍未无条件闭合。

## 141. Strict antisplit trace-cycle / ExactUV atomized frontier router

新增文件

```text
experiments/prime_matrix_strict_antisplit_trace_exactuv_atomized_frontier_router.py
docs/monograph/prime-matrix-strict-antisplit-trace-exactuv-atomized-frontier-router.md
docs/monograph/prime-matrix-strict-antisplit-trace-exactuv-atomized-frontier-router.json
data/prime-matrix-strict-antisplit-trace-exactuv-atomized-frontier-ledger.json
```

本步把上一节的 built-in pairing 和 ExactUV 并行门继续原子化：

```text
BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
-> ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn
-> signed-lane dependency cycle
-> NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact OR terminal/PDEC

ActualEmitterSourceDomainEntropyLedger
-> ActualPreCauchySourceDomainEntropyFromSignedRowsAndRowMassLedger
-> AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward

ExactUVMapFixedPairPolylogFiberBoundLedger
-> RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger
   AND FixedKeyExactUVLocalMultiplicityO1Ledger
```

导入结果：

```text
built_in_pairing_reduced_to_branch_trace=true
signed_lane_trace_cycle_imported=true
new_primitive_payload_or_trace_artifact_present=false
emitter_entropy_atomized_to_signed_row_mass=true
fixed_pair_fiber_atomized=true
acyclic_seed_primitive_row_signed_coefficient_law_proved=false
registered_complete_primitive_emitter_key_partition_polylog_proved=false
fixed_key_exact_uv_local_multiplicity_o1_proved=false
row_column_unconditional_closed=false
```

细原子基为：

```text
(NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact
OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
OR ExternalDIBFIKuznetsovDispersionTheoremMatch)
AND AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward
AND RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger
AND FixedKeyExactUVLocalMultiplicityO1Ledger
```

统一保留剩余基为：

```text
((NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact
OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
OR ExternalDIBFIKuznetsovDispersionTheoremMatch)
AND AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward
AND RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger
AND FixedKeyExactUVLocalMultiplicityO1Ledger)
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本步的关键边界是：exact atomic branch trace 已经落入 signed-lane 闭环，不能作为 built-in pairing 的自足证明；ExactUV 也不能由 signed pairing 推出，而必须单独证明 signed row law、complete key 分区和 fixed-key 局部重数。行/列命题仍未无条件闭合。

## 142. Strict post-antisplit source-rank convergence router

新增文件

```text
experiments/prime_matrix_strict_post_antisplit_source_rank_convergence_router.py
docs/monograph/prime-matrix-strict-post-antisplit-source-rank-convergence-router.md
docs/monograph/prime-matrix-strict-post-antisplit-source-rank-convergence-router.json
data/prime-matrix-strict-post-antisplit-source-rank-convergence-ledger.json
```

本步吸收上一节留下的 `NewPrimitive...` 出口，并与 terminal descent、source-rank/no-collapse 的既有前沿合并：

```text
NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact
-> ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger

AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
-> ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger

ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger
-> ActualPreCauchySourceDomainAbsoluteEntropyLedger
   AND CompletePrimitiveEmitterKeyPartitionLedger
   AND FixedKeyExactUVLocalMultiplicityO1Ledger

ActualPreCauchySourceDomainAbsoluteEntropyLedger
-> AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward

CompletePrimitiveEmitterKeyPartitionLedger
/ RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger
-> ActualNoncanonicalPrimitiveEmitterSourceTableLedger

ActualPreCauchySourceDomainAbsoluteEntropyLedger
/ CompletePrimitiveEmitterKeyPartitionLedger
/ RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger
/ FixedKeyExactUVLocalMultiplicityO1Ledger
-> PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate
```

导入结果：

```text
new_primitive_exit_absorbed_to_source_rank=true
terminal_descent_converges_to_source_rank=true
source_rank_package_atomized=true
all_internal_source_rank_routes_meet_at_pointwise_kernel_table=true
alpha_row_anchor_phase_emission_formula_proved=false
row_column_unconditional_closed=false
```

统一保留剩余基更新为：

```text
((AlphaRowAnchorPhaseEmissionFormulaLedger
AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows)
OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
OR ExternalDIBFIKuznetsovDispersionTheoremMatch)
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本步的实际推进是删除一个重复主攻点：`NewPrimitive...` 已由旧证书吸收到 source-rank/no-collapse，terminal descent 也收敛到同一包。当前真正内部首攻点是 `AlphaRowAnchorPhaseEmissionFormulaLedger`，但该公式、pre-Cauchy 算术恒等式、同表 rank/multiplicity、PDEC/外部谱和最终晋级门均未证明，行/列命题仍未无条件闭合。

## 143. Strict post-antisplit alpha terminal leaf sync router

新增文件

```text
experiments/prime_matrix_strict_post_antisplit_alpha_terminal_leaf_sync_router.py
docs/monograph/prime-matrix-strict-post-antisplit-alpha-terminal-leaf-sync-router.md
docs/monograph/prime-matrix-strict-post-antisplit-alpha-terminal-leaf-sync-router.json
data/prime-matrix-strict-post-antisplit-alpha-terminal-leaf-sync-ledger.json
```

本步继续吸收历史更深前沿，确认 post-antisplit 后不应停在 alpha 单腿：

```text
post-antisplit source-rank convergence
-> PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate
-> AlphaRowAnchorPhaseEmissionFormulaLedger
   AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
   AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows

AlphaRowAnchorPhaseEmissionFormulaLedger
/ IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
-> PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve

SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
-> PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate

三腿合取
-> NonrecursivePointwisePrimitiveKernelTableConstructionWithoutTerminalReturn
-> ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple
-> signed-source fixed point
-> terminal leaf firewall
-> AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
   OR NoncanonicalFullSComplementLegalClosureMode
```

导入结果：

```text
post_antisplit_pointwise_frontier_imported=true
alpha_and_weight_legs_return_to_terminal=true
three_leg_separate_attack_fixed_point_imported=true
nonrecursive_pointwise_field_contract_imported=true
joint_constructor_old_route_returns_to_terminal_leaf=true
current_terminal_leaf_reduced=true
noncanonical_legal_mode_proved=false
acyclic_terminal_canonical_lock_proved=false
row_column_unconditional_closed=false
```

最新严格活动基为：

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
OR NoncanonicalFullSComplementLegalClosureMode)
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本步只完成前沿同步：alpha 单腿、weight 单腿、rank 单腿和旧 joint constructor 展开均不能作为非循环闭合。下一步必须攻 canonical-lock 或 noncanonical legal mode，并同时保留 ExactUV、RatePreservation 与 DStructure/Rankin。

## 144. Strict post-alpha terminal leaf latest noncycle sync router

新增文件

```text
experiments/prime_matrix_strict_post_alpha_terminal_leaf_latest_noncycle_sync_router.py
docs/monograph/prime-matrix-strict-post-alpha-terminal-leaf-latest-noncycle-sync-router.md
docs/monograph/prime-matrix-strict-post-alpha-terminal-leaf-latest-noncycle-sync-router.json
data/prime-matrix-strict-post-alpha-terminal-leaf-latest-noncycle-sync-ledger.json
```

本步继续把 post-alpha terminal leaf 与历史更深 strict 前沿合并。同步链确认：

```text
NoncanonicalFullSComplementLegalClosureMode
-> latest self-contained source-entropy / seed+pair-energy input
-> pair-energy old spine rejected as recursive
-> ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple
-> signed-source fixed point or terminal descent
-> TERMINAL-SOURCE-PAIR-JOINT macrocycle
```

因此当前最深 strict 内部非循环前沿不再停在 canonical/noncanonical 叶子，而是：

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

条件外部线可额外接受 `DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY`。本步只完成前沿同步和循环审查；新 joint 公式、actual-source 外环桥、PDEC same-set 作用域、ExactUV、模型余量、RatePreservation 与 DStructure/Rankin 均未证明，所以行/列命题仍未无条件闭合。

## 145. Strict post-alpha noncycle to terminal three atoms sync router

新增文件

```text
experiments/prime_matrix_strict_post_alpha_noncycle_to_terminal_three_atoms_sync_router.py
docs/monograph/prime-matrix-strict-post-alpha-noncycle-to-terminal-three-atoms-sync-router.md
docs/monograph/prime-matrix-strict-post-alpha-noncycle-to-terminal-three-atoms-sync-router.json
data/prime-matrix-strict-post-alpha-noncycle-to-terminal-three-atoms-sync-ledger.json
```

本步继续吸收 c75 后的 post-alpha 非循环基。既有 branch-trace 证书把
`NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact` 压到
`ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn`；signed-payload 证书再把它压到
`AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn`；source declaration / signed-lane 证书显示该线回到
`PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket` 并闭成依赖环。

因此 `NewExplicit...` 不再是当前最深活动硬点。删除 trace/source/terminal/pair-mass 自回流伪出口后，strict 当前全局前沿同步为：

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
OR A1CleanBranchCanonicalSourceAdmission
OR ActualNoncanonicalCleanCoreMovingAtomExclusion)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻更新为：

```text
IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore
```

本步仍只是前沿同步和自回流删除；三原子与 DStructure/Rankin 独立晋级门均未证明，行/列命题仍未无条件闭合。

## 146. Strict terminal atoms to alpha-return bridge sync router

新增文件

```text
experiments/prime_matrix_strict_terminal_atoms_to_alpha_return_bridge_sync_router.py
docs/monograph/prime-matrix-strict-terminal-atoms-to-alpha-return-bridge-sync-router.md
docs/monograph/prime-matrix-strict-terminal-atoms-to-alpha-return-bridge-sync-router.json
data/prime-matrix-strict-terminal-atoms-to-alpha-return-bridge-sync-ledger.json
```

本步把上一轮三原子继续接入已有更深前沿。同步链为：

```text
ActualNoncanonicalCleanCoreMovingAtomExclusion
-> ExactCleanCoreFullSNonAPWFDSourceEntropy
-> SameFormalUnitPreCauchyAlphaDeltaKernelIdentityWithSignedPhiAndFiberDispersion
-> PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate
-> NonrecursivePointwisePrimitiveKernelTableConstructionWithoutTerminalReturn
-> ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple
-> terminal leaf firewall
-> AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NoncanonicalFullSComplementLegalClosureMode
```

再经 noncanonical legal mode 过滤与 alpha-return 防火墙：

```text
NoncanonicalFullSComplementLegalClosureMode
-> IndependentActualSourceBridgeNotFactoredThroughAlphaReturn

old pointwise/alpha route
-> PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve
-> terminal-family backedge
```

因此 `IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore` 不是当前最深主攻点；旧 pointwise/alpha 展开也不能登记为 well-founded descent。最新 strict 自足活动基同步为：

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
OR IndependentActualSourceBridgeNotFactoredThroughAlphaReturn)
AND (SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000
AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000)
AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

若明确接受外部 Mertens/theta 显式输入，高段尾项可暂时移出活动缺口，剩：

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
OR IndependentActualSourceBridgeNotFactoredThroughAlphaReturn)
AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

本步仍不是无条件闭合；下一步必须证明 canonical-lock 五项同集证书，或在进入 exact-UV/rank/alpha 回边前独立证明 actual-source 恒等或强化反原子。

## 147. Strict alpha-return bridge to concrete terminal split sync router

新增文件

```text
experiments/prime_matrix_strict_alpha_return_bridge_to_concrete_terminal_split_sync_router.py
docs/monograph/prime-matrix-strict-alpha-return-bridge-to-concrete-terminal-split-sync-router.md
docs/monograph/prime-matrix-strict-alpha-return-bridge-to-concrete-terminal-split-sync-router.json
data/prime-matrix-strict-alpha-return-bridge-to-concrete-terminal-split-sync-ledger.json
```

本步把上一节的二选一继续拆到底层具体终端。independent actual-source 侧：

```text
IndependentActualSourceBridgeNotFactoredThroughAlphaReturn
-> A1CleanBranchCanonicalSourceAdmission OR ExactCleanCoreFullSNonAPWFDSourceEntropy

A1CleanBranchCanonicalSourceAdmission
-> scoped A1 branch statement, not global contradiction

ExactCleanCoreFullSNonAPWFDSourceEntropy
-> AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn
   AND IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed
```

canonical-lock 侧：

```text
AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
-> (PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve
    AND ExplicitModelGapAndFiniteDPRCLedger)
   OR SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks
```

因此最新具体终端分裂为：

```text
((AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn
AND IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed)
OR SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks
OR (PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve
AND ExplicitModelGapAndFiniteDPRCLedger))
```

rate-packet 口径下仍需：

```text
RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

严格自足高段尾项口径下仍需：

```text
SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000
AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000
AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

下一直接主攻钉为：

```text
IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed
```

并行仍需提交无环 pre-Cauchy source seed、自足 Kuznetsov/DLS 大筛，或 PDEC/CleanKLS+模型余量。行/列命题仍未无条件闭合。

## 148. Strict pair-energy to seed-coordinate cycle sync router

新增文件

```text
experiments/prime_matrix_strict_pair_energy_to_seed_coordinate_cycle_sync_router.py
docs/monograph/prime-matrix-strict-pair-energy-to-seed-coordinate-cycle-sync-router.md
docs/monograph/prime-matrix-strict-pair-energy-to-seed-coordinate-cycle-sync-router.json
data/prime-matrix-strict-pair-energy-to-seed-coordinate-cycle-sync-ledger.json
```

本步把上一节的抽象 pair-energy 主攻同步到已有 seed-only 阻断、rate-bearing packet、
signed 坐标-来源环、seed 融合和 canonical/direct-terminal 下游。关键读数：

```text
pair_energy_target_imported=true
seed_only_and_qualitative_projection_blocked=true
pair_energy_old_spine_recursive=true
rate_bearing_packet_terminal_trident_imported=true
seed_coordinate_source_cycle_detected=true
direct_pair_energy_large_sieve_proved=false
row_column_unconditional_closed=false
```

由此，pair-energy 分支若要无循环闭合，必须提交不经 signed source 环的直接能量大筛；
否则只能走终端三路的具体化版本：

```text
SelfContainedExactPairEnergyLargeSieveInequalityForAcyclicSeed
OR SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks
OR (PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve
AND ExplicitModelGapAndFiniteDPRCLedger)
```

这只是前沿压缩，不是无条件证明；RatePreservation 与 DStructure/Rankin 门仍需独立闭合。

## 149. Strict pair-energy diagonal peeling terminal reduction router

新增文件

```text
experiments/prime_matrix_strict_pair_energy_diagonal_peeling_terminal_reduction_router.py
docs/monograph/prime-matrix-strict-pair-energy-diagonal-peeling-terminal-reduction-router.md
docs/monograph/prime-matrix-strict-pair-energy-diagonal-peeling-terminal-reduction-router.json
data/prime-matrix-strict-pair-energy-diagonal-peeling-terminal-reduction-ledger.json
```

本步把 direct pair-energy 大筛拆成对角 no-heavy 账本与 off-diagonal clean 双线性大筛：

```text
SelfContainedExactPairEnergyLargeSieveInequalityForAcyclicSeed
=> SameFormalUnitExactPairDiagonalNoHeavyAtomLedger
AND CleanOffDiagonalExactPairDualLargeSieveLedger
```

对角 no-heavy 失败已经是 rate-bearing 大 pair packet；off-diagonal clean 部分则等于
Kuznetsov/DLS，而 KZ-A--KZ-E 既有同步又把它压到 NCBLK/source anti-atom。PDEC/CleanKLS
和模型余量分支同步后，direct pair-energy 不再是独立第三分支。

最新前沿：

```text
AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom
OR (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
AND HighSegmentModelGapAlpha043C3AnalyticLedger)
```

下一直接主攻：

```text
AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom
```

并行保留 `AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate`、
`HighSegmentModelGapAlpha043C3AnalyticLedger`、RatePreservation 与 DStructure/Rankin。

## 150. Strict NCBLK/source anti-atom frontier sync router

新增文件

```text
experiments/prime_matrix_strict_ncblk_source_antiatom_frontier_sync_router.py
docs/monograph/prime-matrix-strict-ncblk-source-antiatom-frontier-sync-router.md
docs/monograph/prime-matrix-strict-ncblk-source-antiatom-frontier-sync-router.json
data/prime-matrix-strict-ncblk-source-antiatom-frontier-sync-ledger.json
```

本步把 NCBLK/source anti-atom 与已有 source-root 链条同步。关键读数：

```text
ncblk_proved=false
forward_source_root_packet_proved=false
global_pdec_sparse_terminal_exclusion_proved=false
high_segment_model_gap_alpha043_c3_analytic_ledger_proved=false
row_column_unconditional_closed=false
```

因此最新前沿不再应写成单独攻击 NCBLK 名称，而应写成：

```text
(ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn)
OR (GlobalPDECorSparseTerminalExclusion
    AND HighSegmentModelGapAlpha043C3AnalyticLedger)
OR (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
    AND HighSegmentModelGapAlpha043C3AnalyticLedger)
```

这里的 formal-to-actual 含义是：`NCBLK` 若要成为 actual-load 矛盾，必须先有一个
pre-Cauchy actual source-root packet 承载真实 source 质量；不能由早期零行的
unsigned CRT 覆盖图、payment skeleton 或 generic WFD 模板反推出该 packet。若不能
正向给出 packet，失败必须进入 global PDEC/sparse、direct PDEC scope 或外部谱/模型
账本，而不能作为 hidden actual load 留在 `NCBLK` 名称下。

## 151. Strict forward source-root terminal cycle sync router

新增文件

```text
experiments/prime_matrix_strict_forward_source_root_terminal_cycle_sync_router.py
docs/monograph/prime-matrix-strict-forward-source-root-terminal-cycle-sync-router.md
docs/monograph/prime-matrix-strict-forward-source-root-terminal-cycle-sync-router.json
data/prime-matrix-strict-forward-source-root-terminal-cycle-sync-ledger.json
```

本步把 `ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn` 展开到底，检查它是否
仍是可独立攻击的 actual-load 入口。同步结果显示：

```text
forward_source_root_packet_proved=false
forward_source_root_independent_after_router=false
ForwardSourceRootSubsumedByTerminalCycle=true
RowColumnUnconditionalClosureReached=false
```

具体链条为：

```text
Forward source-root
-> common packet downstream
-> signed-lane cycle / ExactUV source-rank atoms
-> pointwise primitive alpha/delta kernel table
-> alpha row formula
-> unsigned skeleton closed
-> signed lift and anchor-collar overload return
-> PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve
```

所以 formal-to-actual 前沿再次收窄：source-root 不是新的 hidden actual load，而是
一个已经被下游证书证明会回到终端容量门的循环名称。要继续无条件化，不能再让
CleanKLS/KZ-DLS 使用 NCBLK/source-root 作为闭合输入；必须给出非循环 KZ/DLS，或直接
证明同一 formal unit、same-set 作用域下的 PDEC cap dual certificate。

最新剩余同步为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse)
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 152. Strict post-source-root PDEC scope saturation sync router

新增文件

```text
experiments/prime_matrix_strict_post_source_root_pdec_scope_saturation_sync_router.py
docs/monograph/prime-matrix-strict-post-source-root-pdec-scope-saturation-sync-router.md
docs/monograph/prime-matrix-strict-post-source-root-pdec-scope-saturation-sync-router.json
data/prime-matrix-strict-post-source-root-pdec-scope-saturation-sync-ledger.json
```

本步把上一节的 direct PDEC 主攻接入既有作用域审计和 PDEC scope 饱和前沿。结果是：

```text
post_source_root_pdec_scope_active=true
direct_pdec_scope_audit_imported=true
pdec_scope_branch_saturated_in_current_internal_corpus=true
pdec_scope_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：`PDEC` 名称只有在同一 actual formal unit、同一坏窗集合、
同一 `U_CRT/L_PDEC` 推前和同一质量口径下才是合法容量矛盾。canonical-source
same-set 证书已经 scoped 闭合，但 strict acyclic noncanonical 分支不能偷渡该结果。
如果不能提交新的同口径 scope 证书，也不能引用外部 DIBFI 无投影窗口定理，则该 PDEC
手臂在当前内部语料中只回到既有终端循环和 new-joint 破环口。

最新内部非循环剩余为：

```text
(NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
 OR NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse)
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

条件保留：

```text
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
OR DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY
OR NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse
```

下一直接主攻：

```text
NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
```

## 153. Strict post-PDEC new-joint noncycle sync router

新增文件

```text
experiments/prime_matrix_strict_post_pdec_new_joint_noncycle_sync_router.py
docs/monograph/prime-matrix-strict-post-pdec-new-joint-noncycle-sync-router.md
docs/monograph/prime-matrix-strict-post-pdec-new-joint-noncycle-sync-router.json
data/prime-matrix-strict-post-pdec-new-joint-noncycle-sync-ledger.json
```

本步把 post-PDEC 前沿中的 `NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact`
继续沿既有 branch trace、signed payload、signed-lane cycle、new primitive 和
source-rank convergence 链条展开。同步结果显示：

```text
new_joint_current_internal_route_saturated=true
new_explicit_joint_constructor_formula_artifact_present=false
exact_atomic_branch_trace_formula_proved=false
atomic_signed_payload_constructor_proved=false
new_primitive_artifact_independent_present=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：可见 CRT branch trace 不等于 actual signed payload；它没有
orientation、local factor 与 signed coefficient。若 new-joint 只经旧
joint/antisplit/branch-trace 路线，则它最终回到 signed-lane/source-rank/alpha 终端环；
若要成为真实 actual-load 输入，必须提交闭环外的新 signed payload 或 pre-Cauchy
source-rank/no-collapse 工件。

最新内部非循环剩余为：

```text
NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

条件保留：

```text
NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
OR NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact
OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
OR DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY
OR NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse
```

下一直接主攻：

```text
NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse
```

因此 new-joint 名称当前不是已证 actual contradiction carrier，而是一个已饱和回环名。
全局无条件化仍要在非循环 KZ/DLS、高段模型、RatePreservation 和 DStructure/Rankin
四个门上继续推进。

## 154. Strict post-new-joint KZ no-cycle gate sync router

新增文件

```text
experiments/prime_matrix_strict_post_new_joint_kz_nocycle_gate_sync_router.py
docs/monograph/prime-matrix-strict-post-new-joint-kz-nocycle-gate-sync-router.md
docs/monograph/prime-matrix-strict-post-new-joint-kz-nocycle-gate-sync-router.json
data/prime-matrix-strict-post-new-joint-kz-nocycle-gate-sync-ledger.json
```

本步把 `NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse`
继续沿 windowed DLS/KZ-A--KZ-E 链展开。同步结果显示：

```text
latest_kz_nocycle_gate_active=true
windowed_dls_formal_layer_imported=true
kz_abcd_spine_imported=true
existing_kz_e_route_factors_through_ncblk=true
ncblk_projection_forbidden_for_nocycle_gate=true
kz_e_direct_log_saving_without_ncblk_projection_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：KZ-A--KZ-D 只给出谱框架和大筛脊柱；真正的反例链质量节省
仍在 KZ-E well-factorable dispersion log-saving。若 KZ-E 只通过
NC-BLK/source anti-atom 投影获得节省，则它回到 source-root/terminal cycle，不满足当前
非循环门。因此 actual-load 闭合必须给出不经 NC-BLK 投影的 KZ-E 直接节省，或把外部
DI/BFI/Kuznetsov 作为明确条件输入。

最新内部非循环剩余为：

```text
AcyclicKZEWellFactorableDispersionLogSavingWithoutNCBLKProjection
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

条件保留：

```text
AcyclicKZEWellFactorableDispersionLogSavingWithoutNCBLKProjection
OR ExactExternalDIBFIKuznetsovNoProjectionCertificate_FOR_NONCIRCULAR_KZ_ONLY
```

下一直接主攻：

```text
AcyclicKZEWellFactorableDispersionLogSavingWithoutNCBLKProjection
```

所以当前前沿已从“证明一个非循环 KZ/DLS”压到更窄的“直接 KZ-E dispersion log-saving”，
且禁止经 NC-BLK/source-root 回流偷渡。

## 155. Strict post-KZ-E direct source-bridge sync router

新增文件

```text
experiments/prime_matrix_strict_post_kze_direct_source_bridge_sync_router.py
docs/monograph/prime-matrix-strict-post-kze-direct-source-bridge-sync-router.md
docs/monograph/prime-matrix-strict-post-kze-direct-source-bridge-sync-router.json
data/prime-matrix-strict-post-kze-direct-source-bridge-sync-ledger.json
```

本步把 `AcyclicKZEWellFactorableDispersionLogSavingWithoutNCBLKProjection` 继续接入
actual-source bridge 分类。同步结果显示：

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

formal-to-actual 含义是：KZ-E direct 节省不是泛 well-factorable 模板的免费结论。
canonical-restricted 分支可以闭合，但它要求 actual source 在 Cauchy/dispersion 前已锁定为
RIW/Buchstab 决策树源头；generic/noncanonical 分支若回到 moving atom 或 source anti-atom，
则是终端回流而非 KZ no-cycle 证明。

最新内部非循环剩余为：

```text
A1CleanBranchCanonicalSourceAdmission
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

条件保留：

```text
A1CleanBranchCanonicalSourceAdmission
OR ExactExternalDIBFIKuznetsovNoProjectionCertificate_FOR_NONCIRCULAR_KZ_ONLY
```

下一直接主攻：

```text
A1CleanBranchCanonicalSourceAdmission
```

因此当前前沿进一步从“直接 KZ-E dispersion log-saving”压到“actual clean A1 分支的
canonical source admission”，并显式保留外部 no-projection 条件线。

## 156. Strict post-source-admission macrocycle sync router

新增文件

```text
experiments/prime_matrix_strict_post_source_admission_macrocycle_sync_router.py
docs/monograph/prime-matrix-strict-post-source-admission-macrocycle-sync-router.md
docs/monograph/prime-matrix-strict-post-source-admission-macrocycle-sync-router.json
data/prime-matrix-strict-post-source-admission-macrocycle-sync-ledger.json
```

本步把 `A1CleanBranchCanonicalSourceAdmission` 接回已有的 A1/T1/signed-lift/PDEC/KZ
深层链。同步结果显示：

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

formal-to-actual 含义是：source-admission 的 canonical case 只能 scoped 吸收；非 canonical
mismatch 经 signed-lift 登记和 alpha weight law 下游同步后，会回到
`PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve`，再经 new-joint/KZ/KZ-E 回到 A1。
因此它不是新的单向下降链，而是一条已识别的宏循环。

最新非循环剩余为：

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

所以当前前沿已从“证明 A1 source-admission”转为“提供循环外 seed cycle-cut primitive
source 或同集 PDEC 作用域匹配/真正新 primitive/外部 no-projection KZ 证书”。宏循环同步本身
不是行/列命题无条件闭合。

## 157. Row-gap supply/phase cycle-cut router

新增文件

```text
experiments/prime_matrix_row_gap_supply_phase_cycle_cut_router.py
docs/monograph/prime-matrix-row-gap-supply-phase-cycle-cut-router.md
docs/monograph/prime-matrix-row-gap-supply-phase-cycle-cut-router.json
data/prime-matrix-row-gap-supply-phase-cycle-cut-ledger.json
```

本步把用户提出的具体零行反例模型形式化为 `I_k={kP+a:1<=a<P}`。同步结果显示：

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

formal-to-actual 含义是：零行确实要求所有列槽被 `<P` 的素因子覆盖；但将供给全部放在
`q<=sqrt(kP)` 是过强的，因为近根带
`sqrt(kP)<q<=sqrt(kP+P-1)` 会提供边缘半素数槽。另一方面，raw capacity 带重数通常不短缺，
所以不能靠总量矛盾闭合；必须证明低根筛余槽在扣除近根 only 槽后仍有正缺口，或者证明
`Q1/Q2` 相邻素数的 CRT 传输强制同 formal unit 的短同标签复现/登记缺陷。

最新非循环剩余为：

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

所以当前前沿从宏循环破环进一步落到一个具体 row-gap 筛余下界：低根覆盖后，近根槽不能吞掉全部剩余列。

## 158. Low-root sifted deficit frontier router

新增文件

```text
experiments/prime_matrix_lowroot_sifted_deficit_frontier_router.py
docs/monograph/prime-matrix-lowroot-sifted-deficit-frontier-router.md
docs/monograph/prime-matrix-lowroot-sifted-deficit-frontier-router.json
data/prime-matrix-lowroot-sifted-deficit-frontier-ledger.json
```

本步把 `UniformLowRootSiftedResidueDeficitAfterNearRootSlots` 继续拆解。同步结果显示：

```text
exact_deficit_identity_closed=true
near_root_slot_upper_bound_elementary=true
mertens_heuristic_not_proof=true
jacobsthal_barrier_identified=true
noncircular_short_interval_rough_residue_lower_bound_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：`full_uncovered_slots>0` 与 row 内存在素数等价；近根槽容量可初等控制，
但低根筛余的逐行正下界仍是核心。不能用 Mertens 平均密度替代该短区间下界，因为那会重新引入
待证行命题。

最新非循环剩余为：

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

所以当前前沿已压到一个标准但很硬的非循环筛论输入：指定相位短区间 rough residue 下界。

## 159. Short-interval rough-residue barrier router

新增文件

```text
experiments/prime_matrix_short_interval_rough_residue_barrier_router.py
docs/monograph/prime-matrix-short-interval-rough-residue-barrier-router.md
docs/monograph/prime-matrix-short-interval-rough-residue-barrier-router.json
data/prime-matrix-short-interval-rough-residue-barrier-ledger.json
```

本步把上一节的 rough-residue 首攻点做非循环性审查。同步结果显示：

```text
full_root_rough_equals_prime_in_row=true
near_root_subtraction_keeps_equivalence=true
mertens_average_insufficient=true
periodwide_jacobsthal_shortcut_rejected=true
noncircular_internal_use_rejected=true
noncircular_short_interval_rough_residue_lower_bound_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：`q<=sqrt(kP+P-1)` 的 full-root 未覆盖槽为正，当且仅当 row 内实际有素数。
因此 `NonCircularShortIntervalRoughResidueLowerBoundLengthPLevelSqrtkP` 不是新的独立 actual-load
不等式，而是目标 row-gap 的筛论重写。Mertens 平均密度、全周期 Jacobsthal 直觉、有限样本都不能把它变成逐行证明。

最新内部非循环剩余为：

```text
(AdjacentPrimeQ1Q2CRTTransportDefectOrStableShortReturn
 OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput
 OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate)
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
AdjacentPrimeQ1Q2CRTTransportDefectOrStableShortReturn
```

所以当前前沿不再把 direct rough-residue 下界当作内部目标；它被降格为外部平方根长度素数间隙输入，
内部路线转向 `Q1/Q2` 相邻素数 CRT 传输、seed cycle-cut 或 same-set PDEC 作用域匹配。

## 160. Q1/Q2 transport latest noncycle sync router

新增文件

```text
experiments/prime_matrix_q1q2_transport_latest_noncycle_sync_router.py
docs/monograph/prime-matrix-q1q2-transport-latest-noncycle-sync-router.md
docs/monograph/prime-matrix-q1q2-transport-latest-noncycle-sync-router.json
data/prime-matrix-q1q2-transport-latest-noncycle-sync-ledger.json
```

本步把 `Q1/Q2` 相邻素数传输分支同已有 Q2 阶 CRT 梯重新同步。同步结果显示：

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

formal-to-actual 含义是：Q1/Q2 的 CRT 刚性只控制位置和相位，不能给 actual source 质量分散。
全 `Q2` 阶轮已排除素端点稳定复现；固定闭覆盖块是 `ColumnCRT/PDEC`，受控 fresh endpoint tail 是 `SAE`，
无名孔径爆炸被 schema 防火墙阻断。纯 CRT 全局相位矛盾也被有限轮同质删相位机制排除。

立即内部剩余为：

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

所以当前前沿删除了 `Q1/Q2` 作为独立纯 CRT 终端的误出口；它没有完成行/列命题，只把剩余压回
actual-source exact-UV 非集中、外部谱输入或 strict new-joint 前沿。

## 161. Exact-UV fiber latest noncycle sync router

新增文件

```text
experiments/prime_matrix_exactuv_fiber_latest_noncycle_sync_router.py
docs/monograph/prime-matrix-exactuv-fiber-latest-noncycle-sync-router.md
docs/monograph/prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json
data/prime-matrix-exactuv-fiber-latest-noncycle-sync-ledger.json
```

本步把 `NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource`
从 Q1/Q2 后的首攻点同步到 actual source-rank/no-collapse 原子包。同步结果显示：

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

formal-to-actual 含义是：CRT、payment skeleton、DLS 可逆变量、signed-only 相消或 canonical cross-import
都不能直接给出 exact-UV fiber 非集中。可用的闭合蕴含只有：

```text
source-domain entropy
AND complete primitive emitter key partition
AND fixed-key exact-UV local O(1) multiplicity
=> exact-UV fiber aperiodicity / no-collapse
```

因此 immediate source-rank 基为：

```text
(ActualPreCauchySourceDomainAbsoluteEntropyLedger
 AND RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger
 AND FixedKeyExactUVLocalMultiplicityO1Ledger)
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全原子化后，内部剩余为：

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

下一直接主攻：

```text
AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward
```

所以当前前沿不再寻找纯 CRT 全周期结构矛盾来直接推出 exact-UV 非集中；它被压成 signed-row 源律、
actual emitter 源表/key 预算、fixed-key 局部重数、外部谱或 strict new-joint 前沿。该同步仍不是行/列命题的无条件闭合。

## 162. Inverse-alignment 第 P+1 行归约检查

新增文件

```text
experiments/prime_matrix_inverse_alignment_pplus1_row_reduction_check_router.py
docs/monograph/prime-matrix-inverse-alignment-pplus1-row-reduction-check-router.md
docs/monograph/prime-matrix-inverse-alignment-pplus1-row-reduction-check-router.json
data/prime-matrix-inverse-alignment-pplus1-row-reduction-check-ledger.json
```

本步回查旧仓库 inverse-alignment 路线，确认其与 `P^2` 后第 `P+1` 行的精确关系：

```text
old_minrep_equivalence_closed=true
pplus1_row_is_x_equals_p=true
x_equals_p_no_cover_equivalent_to_first_half_prime_square=true
pplus1_nonzero_suffices_for_all_early_rows_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：旧稿已经证明最小对齐解 `X_0(P)>P` 等价于所有 `1<=x<=P` 行非零；
也已经证明 `x=P` 特化等价于平方后前半窗素数输入：

```text
NoZeroRowAtXEqualsP_PlusOneRowAfterSquare
<=> PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP
```

但是这只是 `x=P` 这一条特殊相位线。它没有给出从任意早期相位 `1<=x<P`
转移到平方锚相位 `x=P` 的非循环定理。因此当前不能写成“只要证明第 `P+1` 行不可能是零行，就证明 `x<P` 零行不存在”。

正确的可攻接口是：

```text
AcyclicEarlyZeroToSquareAnchorPhaseTransferOrNamedReturn
```

即证明任一早期零行若存在，要么强制 `x=P` 也零行，要么进入命名 `PDEC/SAE/ColumnCRT/source-rank` 出口。
这一路线与 exact-UV 后的 signed-row 主前沿并行，而不是替代它。

## 163. Early-to-square phase-transfer 首破裂分裂

新增文件

```text
experiments/prime_matrix_early_to_square_phase_transfer_split_router.py
docs/monograph/prime-matrix-early-to-square-phase-transfer-split-router.md
docs/monograph/prime-matrix-early-to-square-phase-transfer-split-router.json
data/prime-matrix-early-to-square-phase-transfer-split-ledger.json
```

本步把上一节的抽象转移接口继续压缩。同步结果显示：

```text
contiguous_zero_block_dichotomy_closed=true
persist_to_square_implies_square_zero=true
first_break_release_set_nonempty=true
unit_phase_slip_formula_closed=true
phase_slip_schema_admission_imported=true
transfer_proved_as_contradiction=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：若早期零行 `x0<P` 不能一路延续到平方锚 `x=P`，则必有首个破裂行 `y`。
`y-1` 仍是零行，`y` 出现释放列；这些释放列是相位

```text
rho_q(y)=rho_q(y-1)-P mod q
```

滑移后的边界非覆盖。若 `y<P`，释放列给出真实早期素数幸存；若 `y=P`，给出平方锚幸存。
因此抽象 transfer 不再是独立硬点，而分裂为：

```text
ZeroAtXEqualsP
OR RegisteredFirstBreakUnitPhaseSlipPDECSAELocalSurvivorReturn
```

在第 `P+1` 行非零的条件下，剩余进一步压成：

```text
FirstBreakPhaseSlipNamedReturnExclusion
```

所以当前 inverse-alignment 回流路线的最新硬点不是“证明所有早期相位转移到平方锚”，而是排斥首破裂相位滑移的命名终端；全局 signed-row/source-rank 前沿仍并行开放。

## 164. First-break phase-slip LCM-支撑宽度屏障

新增文件

```text
experiments/prime_matrix_firstbreak_phase_slip_lcm_barrier_router.py
docs/monograph/prime-matrix-firstbreak-phase-slip-lcm-barrier-router.md
docs/monograph/prime-matrix-firstbreak-phase-slip-lcm-barrier-router.json
data/prime-matrix-firstbreak-phase-slip-lcm-barrier-ledger.json
```

本步把 `FirstBreakPhaseSlipNamedReturnExclusion` 继续压缩为固定 carrier 复现的 LCM 屏障。同步结果：

```text
fixed_carrier_lcm_replay_period_closed=true
square_support_width_sharpened_to_p_minus_y=true
lcm_exceeds_width_no_fixed_replay=true
firstbreak_phase_slip_named_return_exclusion_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：首破裂行 `y` 之后，如果释放相位要用同一 carrier 标签集 `Lambda` 再次复现，
则复现步长 `d` 必须满足：

```text
lcm(Lambda) | d.
```

但可复现的行宽只剩 `H=P-y`。因此 `lcm(Lambda)>H` 时，固定标签复现不可能；`lcm(Lambda)<=H`
时，活动 carrier 的合成模数被强制压在小范围内，进入小 LCM/ColumnCRT/PDEC。若标签移动，则进入
moving-carrier PDEC/SAE；若没有复现，则只能作为 sparse SAE/LocalSurvivor 处理。

当前硬点更新为：

```text
SmallLCMColumnCRTPDECExclusion
AND NonreplaySparseFirstBreakSAESummability
AND MovingCarrierPhaseSlipPDECExclusion
```

这一步没有排斥首破裂，只是把“相位滑移终端”拆成三个更低层的可审计出口。

## 165. First-break small-LCM rank-pressure 压缩

新增文件

```text
experiments/prime_matrix_firstbreak_small_lcm_rank_pressure_router.py
docs/monograph/prime-matrix-firstbreak-small-lcm-rank-pressure-router.md
docs/monograph/prime-matrix-firstbreak-small-lcm-rank-pressure-router.json
data/prime-matrix-firstbreak-small-lcm-rank-pressure-ledger.json
```

本步继续下钻 small-LCM 出口。同步结果：

```text
distinct_prime_product_law_closed=true
small_lcm_rank_pressure_closed=true
two_large_carrier_sqrt_barrier_closed=true
small_lcm_branch_excluded=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：fixed small-LCM 分支的 carrier 标签不能很多。若活动标签集为 `Lambda`，则

```text
lcm(Lambda)=product Lambda <= H=P-y.
```

所以任意阈值 `B` 以上的 carrier 数量满足：

```text
rank_{>B} <= floor(log H/log B).
```

特别地，两个 `>sqrt(H)` 的 carrier 不能同时存在。于是小 LCM 压力不可能仍被解释为“许多中高素 carrier
自由叠加”；它必须落入：

```text
LowCarrierFixedResidueColumnCRTPDECExclusion
AND LowCarrierNonpersistentSparseSAESummability
AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE
```

这一步提供的是非循环 rank-pressure 结构压缩，不是终端排斥。

## 166. First-break low-carrier fixed-residue AP 骨架

新增文件

```text
experiments/prime_matrix_firstbreak_low_carrier_residue_ap_router.py
docs/monograph/prime-matrix-firstbreak-low-carrier-residue-ap-router.md
docs/monograph/prime-matrix-firstbreak-low-carrier-residue-ap-router.json
data/prime-matrix-firstbreak-low-carrier-residue-ap-ledger.json
```

本步把 `LowCarrierFixedResidueColumnCRTPDECExclusion` 继续降维。同步结果：

```text
residue_to_row_ap_formula_closed=true
single_residue_ap_envelope_closed=true
low_carrier_residue_table_finite_closed=true
ap_envelope_capacity_comparison_proved=false
low_carrier_fixed_residue_excluded=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：固定低 carrier `q` 和固定列 residue `a` 不是自由相位。因为 `(P,q)=1`，
它强制行坐标落在唯一 AP：

```text
t == -a P^{-1} mod q.
```

在剩余宽度 `H=P-y` 内，单个 residue cell 的行向供给至多 `ceil(H/q)`。因此低 carrier
固定 residue 若持续承担压力，只能成为有限低维 AP table 的稠密偏斜：

```text
LowCarrierResidueAPEnvelopeCapacityComparison
AND DenseLowCarrierResidueTablePDECExclusion
AND SparseLowCarrierResidueCellSAESummability
```

这一步把“低 carrier 固定 residue”从宽泛相位标签变成可数的 AP table 容量接口；终端排斥仍未完成。

## 167. First-break low-carrier AP exact-envelope 证书

新增文件

```text
experiments/prime_matrix_firstbreak_low_carrier_ap_envelope_router.py
docs/monograph/prime-matrix-firstbreak-low-carrier-ap-envelope-router.md
docs/monograph/prime-matrix-firstbreak-low-carrier-ap-envelope-router.json
data/prime-matrix-firstbreak-low-carrier-ap-envelope-ledger.json
```

本步把 `LowCarrierResidueAPEnvelopeCapacityComparison` 中的形式供给端完全显式化。同步结果：

```text
cell_count_formula_closed=true
single_cell_sharp_bound_closed=true
all_residues_exact_mass_closed=true
selected_table_envelope_closed=true
ap_capacity_comparison_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：AP envelope 是真实反例压力必须穿过的硬容量边界，但它本身不是需求下界。
对任意 table `T`，

```text
U_T(I_y)=sum_{(q,a) in T} #{t in I_y: t == -a P^{-1} mod q}
```

且单 cell 有 `ceil(H/q)` 上界；固定 `q` 的所有 residue cell 精确合计为 `H`。所以形式容量端已经闭合：

```text
U_T(I_y) <= sum_{(q,a) in T} ceil(H/q),
U_T(I_y) <= H * |{q: exists a with (q,a) in T}|.
```

真正剩余接口变成：

```text
ActualLowCarrierRowIncidenceDemandLowerBound
AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC
```

也就是说，下一步必须证明首破裂反例链在低 carrier AP table 上产生足够 actual 行发生需求；若为了接近
envelope 而长期占满许多低维 residue cell，则必须登记并排斥为 dense-table PDEC。

## 168. First-break actual demand 源侧切口

新增文件

```text
experiments/prime_matrix_firstbreak_actual_demand_source_cut_router.py
docs/monograph/prime-matrix-firstbreak-actual-demand-source-cut-router.md
docs/monograph/prime-matrix-firstbreak-actual-demand-source-cut-router.json
data/prime-matrix-firstbreak-actual-demand-source-cut-ledger.json
```

本步把 `ActualLowCarrierRowIncidenceDemandLowerBound` 拆成源侧放大与支付注入。同步结果：

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

formal-to-actual 含义是：首破裂释放非空是严格源侧事实，但它只给出单位需求 `D_y>=1`。这不足以超过
AP exact-envelope，因此不能把“出现了释放列”直接升格为容量矛盾。非循环证明需要两步：

```text
FirstBreakReleaseMassAmplificationOrSingletonSAE
AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse
```

第一步从零行/首破裂源侧证明释放质量会沿反例链放大；若不放大，则事件是 singleton/sparse SAE。
第二步证明这些放大的压力确实注入低 carrier AP table，且证明过程不借用 AP envelope 饱和本身。

## 169. First-break release mass 零行块阶梯

新增文件

```text
experiments/prime_matrix_firstbreak_release_mass_zero_block_ladder_router.py
docs/monograph/prime-matrix-firstbreak-release-mass-zero-block-ladder-router.md
docs/monograph/prime-matrix-firstbreak-release-mass-zero-block-ladder-router.json
data/prime-matrix-firstbreak-release-mass-zero-block-ladder-ledger.json
```

本步把 `FirstBreakReleaseMassAmplificationOrSingletonSAE` 的可能来源定位到首破裂前零行块。同步结果：

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

formal-to-actual 含义是：首破裂释放列只是边界单位事件，不可能单独给出 `Ω(H)` 需求。若 `[x0,y-1]`
是首破裂前连续零行块，长度 `L=y-x0`，则块内覆盖义务总量为精确的 `L(P-1)`。所以真正的需求放大只能来自：

```text
ShortZeroBlockSingletonSAESummability
AND LongZeroBlockCoverMassTransferToAPDemandOrPDEC
```

短块必须由 singleton/sparse SAE 或局部短块证书吸收；长块必须证明覆盖义务能非循环地转移成 post-break
AP demand，或者证明转移失败形成持续覆盖历史 PDEC/ColumnCRT/SAE。

## 170. Long zero-block cover mass 稳定 history 注入路由

新增文件

```text
experiments/prime_matrix_firstbreak_long_zero_block_mass_transfer_router.py
docs/monograph/prime-matrix-firstbreak-long-zero-block-mass-transfer-router.md
docs/monograph/prime-matrix-firstbreak-long-zero-block-mass-transfer-router.json
data/prime-matrix-firstbreak-long-zero-block-mass-transfer-ledger.json
```

本步把 `LongZeroBlockCoverMassTransferToAPDemandOrPDEC` 拆成无损投影、稳定表/命名切换、稳定历史注入三段。
同步结果：

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

formal-to-actual 含义是：长零块覆盖义务 `O_B` 的每个支付事件都有
`kappa=(q,a)` 形式的低 carrier/residue history key；no-loss 账本保证这些义务不能无名消失。若同一
history key 在首破裂后稳定延续，下一步必须证明它给出 post-break AP demand；若 key、carrier 或相位移动，
则进入 `HistorySwitch-PDEC/ColumnCRT/MovingCarrier/SAE` 命名出口。

新的直接主攻为：

```text
PostBreakAPDemandInjectionFromStableHistory
```

并行保留：

```text
HistorySwitchPDECOrColumnCRTExclusion
AND ShortZeroBlockSingletonSAESummability
AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse
```

本步没有把长零块质量转移升级为矛盾；它只把转移失败的匿名缺口压成稳定注入缺口或命名 history-switch 终端。

## 171. Stable history AP 到达/越界二分

新增文件

```text
experiments/prime_matrix_firstbreak_stable_history_ap_arrival_router.py
docs/monograph/prime-matrix-firstbreak-stable-history-ap-arrival-router.md
docs/monograph/prime-matrix-firstbreak-stable-history-ap-arrival-router.json
data/prime-matrix-firstbreak-stable-history-ap-arrival-ledger.json
```

本步把 `PostBreakAPDemandInjectionFromStableHistory` 压成 AP 后继二分、到达候选 actual 注入和未到达越界出口。
同步结果：

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

formal-to-actual 含义是：稳定 history key 的下一次同余行由 `t_next=t_*+q` 精确给出。若
`t_next in [y,P-1]`，它只产生 AP arrival candidate；若 `t_next>=P`，则不是 demand，而是
`TerminalNonarrivalLargeStepEscapePDECOrSAE`。

新的直接主攻为：

```text
ArrivalCandidateActualDemandInjectionWithoutEnvelopeReuse
```

并行保留：

```text
TerminalNonarrivalLargeStepEscapePDECOrSAE
AND HistorySwitchPDECOrColumnCRTExclusion
AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse
```

本步没有把 arrival candidate 升级为 actual demand；它只把稳定 history 的相位去向从“抽象注入”压成
精确的到达/越界二分。

## 172. Arrival candidate actual demand 单位注入与商化

新增文件

```text
experiments/prime_matrix_firstbreak_arrival_candidate_actual_demand_router.py
docs/monograph/prime-matrix-firstbreak-arrival-candidate-actual-demand-router.md
docs/monograph/prime-matrix-firstbreak-arrival-candidate-actual-demand-router.json
data/prime-matrix-firstbreak-arrival-candidate-actual-demand-ledger.json
```

本步把 `ArrivalCandidateActualDemandInjectionWithoutEnvelopeReuse` 拆成单位 source-tagged incidence、
distinct quotient 下界和碰撞 return。同步结果：

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

formal-to-actual 含义是：每个带源侧 history tag 的到达候选都给出一个 actual AP incidence 单位，
但聚合需求只能数商化后的 distinct `(t_next,q,a)`。若大量源义务重合到同一 incidence，则这是
`ArrivalCollisionOrDuplicatePaymentReturnLedger`，不是免费多重需求。

新的直接主攻为：

```text
DistinctArrivalQuotientDemandLowerBoundOrCollisionPDEC
```

并行保留：

```text
ArrivalCollisionOrDuplicatePaymentReturnLedger
AND TerminalNonarrivalLargeStepEscapePDECOrSAE
AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse
```

本步没有证明聚合 actual demand 下界；它只关闭了单位 incidence 注入和去重纪律。

## 173. Arrival quotient 纤维 envelope

新增文件

```text
experiments/prime_matrix_firstbreak_arrival_quotient_fiber_router.py
docs/monograph/prime-matrix-firstbreak-arrival-quotient-fiber-router.md
docs/monograph/prime-matrix-firstbreak-arrival-quotient-fiber-router.json
data/prime-matrix-firstbreak-arrival-quotient-fiber-ledger.json
```

本步把 `DistinctArrivalQuotientDemandLowerBoundOrCollisionPDEC` 压成纤维 envelope、raw arrival mass、
加权 image 下界和高纤维回流。同步结果：

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

formal-to-actual 含义是：同一 arrival incidence `(t,q,a)` 的源侧原像不能任意大。它至多有
`ceil(L/q)` 个零块源行和 `ceil((P-1)/q)` 个同余源列，因此：

```text
|pi^{-1}(t,q,a)| <= ceil(L/q) ceil((P-1)/q).
```

这给出：

```text
|image(pi)| >= sum_{u in A} 1/F(pi(u)).
```

新的直接主攻为：

```text
ArrivalRawSourceMassAfterNonarrivalRemoval
```

并行保留：

```text
HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn
AND ArrivalCollisionOrDuplicatePaymentReturnLedger
AND TerminalNonarrivalLargeStepEscapePDECOrSAE
```

本步没有证明 distinct arrival demand 已足够大；它只关闭了 quotient 纤维乘数纪律。

## 174. Arrival raw mass 层平衡与低步长阈值

新增文件

```text
experiments/prime_matrix_firstbreak_arrival_raw_mass_layer_router.py
docs/monograph/prime-matrix-firstbreak-arrival-raw-mass-layer-router.md
docs/monograph/prime-matrix-firstbreak-arrival-raw-mass-layer-router.json
data/prime-matrix-firstbreak-arrival-raw-mass-layer-ledger.json
```

本步继续攻击 `ArrivalRawSourceMassAfterNonarrivalRemoval`。同步结果：

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

formal-to-actual 含义是：设 `H=P-y`，稳定 history 源标签的最后零块命中为 `t_*`。
若 `q<=H`，则

```text
t_*+q <= y-1+H = P-1,
```

所以低步长层必定成为 source-tagged arrival。若 terminal nonarrival 发生，则

```text
t_*+q>=P  =>  q>=P-t_*>=H+1.
```

因此

```text
|A| >= |S_{q<=H}|.
```

新的直接主攻为：

```text
LowStepStableHistoryMassLowerBoundOrLargeStepTailEscapePDEC
```

并行保留：

```text
LargeStepTailTerminalEscapePDECOrSAE
AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn
AND ArrivalCollisionOrDuplicatePaymentReturnLedger
AND TerminalNonarrivalLargeStepEscapePDECOrSAE
```

本步没有证明 raw arrival mass 已足够大；它只关闭了 nonarrival 去除的精确阈值：
低步长稳定源不会被 terminal nonarrival 吞掉，剩余硬点变成低步长稳定源质量下界，
或证明质量集中到 `q>H` 大步长尾部必为 PDEC/SAE。

## 175. Low-step/tail 显式容量 envelope

新增文件

```text
experiments/prime_matrix_firstbreak_lowstep_tail_capacity_router.py
docs/monograph/prime-matrix-firstbreak-lowstep-tail-capacity-router.md
docs/monograph/prime-matrix-firstbreak-lowstep-tail-capacity-router.json
data/prime-matrix-firstbreak-lowstep-tail-capacity-ledger.json
```

本步继续攻击 `LowStepStableHistoryMassLowerBoundOrLargeStepTailEscapePDEC`。同步结果：

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

formal-to-actual 含义是：设 `H=P-y`、`B=[x0,y-1]`、`L=y-x0`。稳定层满足

```text
S = S_{q<=H} disjoint_union S_{q>H}.
```

对 `q>H` 的 terminal tail，最后命中行必须满足

```text
t_* in T_q := B ∩ [P-q,y-1],
|T_q| <= min(L,q-H).
```

固定 `q,t_*` 后，源列满足 `c == -t_*P mod q`，因此列数至多 `ceil((P-1)/q)`。
所以 tail 有显式 envelope：

```text
C_tail = sum_{H<q<P} |B ∩ [P-q,y-1]| ceil((P-1)/q),
|S_{q>H}| <= C_tail.
```

于是

```text
|S_{q<=H}| >= |S| - C_tail.
```

新的直接主攻为：

```text
StableTotalMinusTailEnvelopeGapOrLargeStepTailSaturationPDEC
```

本步没有证明 `|S|-C_tail` 已足够大；它把剩余硬点压成显式差额问题：
证明稳定总源质量超过 tail envelope，或证明 tail 近饱和/重复就是 PDEC/SAE。

## 176. Stable tail gap functional

新增文件

```text
experiments/prime_matrix_firstbreak_stable_tail_gap_router.py
docs/monograph/prime-matrix-firstbreak-stable-tail-gap-router.md
docs/monograph/prime-matrix-firstbreak-stable-tail-gap-router.json
data/prime-matrix-firstbreak-stable-tail-gap-ledger.json
```

本步继续攻击 `StableTotalMinusTailEnvelopeGapOrLargeStepTailSaturationPDEC`。同步结果：

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

formal-to-actual 含义是：零块覆盖义务域满足

```text
|O_B|=L(P-1).
```

no-loss 账本给出

```text
O_B = StableSourceRecords disjoint_union NamedReturnRecords.
```

记命名 return 质量为 `R_named`，上一层 tail envelope 为

```text
C_tail = sum_{H<q<P} |B ∩ [P-q,y-1]| ceil((P-1)/q).
```

于是低步长稳定质量下界改写为：

```text
|S_{q<=H}| >= L(P-1)-R_named-C_tail.
```

新的直接主攻为：

```text
PositiveStableTailGapOrNamedReturnMassPDEC
```

本步没有证明该 gap 已经为正或足够大；它把剩余压成显式不等式：
证明 `L(P-1)-R_named-C_tail` 足够，或证明 `R_named`/tail saturation 已形成 PDEC/SAE。

## 177. Tail gap 归一化

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_normalization_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-normalization-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-normalization-router.json
data/prime-matrix-firstbreak-tail-gap-normalization-ledger.json
```

本步继续攻击 `PositiveStableTailGapOrNamedReturnMassPDEC`。同步结果：

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

formal-to-actual 含义是：tail carrier 用

```text
q=H+r,  H=P-y.
```

重写后满足

```text
P-q=y-r,
|B ∩ [P-q,y-1]|=min(L,r).
```

于是

```text
C_tail = sum_{prime q=H+r<P} min(L,r) ceil((P-1)/(H+r)),
C_tail <= sum_{1<=r<P-H} min(L,r) ceil((P-1)/(H+r)).
```

同时

```text
G_prime=L(P-1)-C_tail,
G=G_prime-R_named.
```

新的直接主攻为：

```text
NormalizedTailGapPositiveOrDenseTailReturnPDEC
```

本步没有证明归一化 gap 为正；它把剩余从二维窗口几何压成一维 tail-index 和式。
若一维 gap 仍不足，必须由 dense tail、tail saturation 或 named-return mass PDEC/SAE 承载。

## 178. Tail gap 全整数 margin 分裂

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_integer_margin_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-integer-margin-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-integer-margin-router.json
data/prime-matrix-firstbreak-tail-gap-integer-margin-ledger.json
```

本步继续攻击 `NormalizedTailGapPositiveOrDenseTailReturnPDEC`。同步结果：

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

formal-to-actual 含义是：把 prime-tail 上界放宽成全整数上界

```text
C_all = sum_{1<=r<y} min(L,r) ceil((P-1)/(P-y+r)),
G_int = L(P-1)-C_all.
```

则：

```text
C_tail <= C_all,
G_prime >= G_int.
```

所以 `G_int>R_named` 是正 gap 的充分条件。进一步，在 `y<=floor(P/2)` 的前半支撑中：

```text
C_all <= L(2y-L-1),
G_int >= L(P-2y+L)>0.
```

新的直接主攻为：

```text
IntegerTailMarginPositiveOrLateSupportDenseTailNamedReturnPDEC
```

本步没有证明全局正 gap；它删除了前半支撑 pure-tail 饱和解释。
剩余必须表现为 late-support dense-tail，或命名 return 质量 `R_named` 过大。

## 179. Tail gap late-support collar

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_late_collar_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-late-collar-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-late-collar-router.json
data/prime-matrix-firstbreak-tail-gap-late-collar-ledger.json
```

本步继续攻击 `IntegerTailMarginPositiveOrLateSupportDenseTailNamedReturnPDEC`。同步结果：

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

formal-to-actual 含义是：late branch 可写成

```text
P=2m+1, H=P-y, y>m,
D=2y-P, E=(D-1)/2.
```

其中超过二重的整数 tail 只在 `1<=r<=E` 的 short core 中出现。设

```text
X_core=sum_{1<=r<=E} min(L,r)(ceil((P-1)/(P-y+r))-2).
```

利用 regular tail 的二重上界和端点 `q=P-1` 的一重缺口，可得精确式：

```text
C_all=L(2y-L-1)+X_core-min(L,y-1),
G_int=L(L-D)+min(L,y-1)-X_core.
```

所以若

```text
L(L-D)+min(L,y-1)>X_core+R_named,
```

则 `G>0`。新的直接主攻为：

```text
DeepLateShortCollarOrCoreExcessNamedReturnPDEC
```

本步没有排斥 deep-late collar，也没有控制 `X_core` 或 `R_named`；
它把 late-support 剩余压成一个精确的 collar/core-excess 不等式。

## 180. Deep-late collar quotient-layer

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_deep_collar_layer_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-deep-collar-layer-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-deep-collar-layer-router.json
data/prime-matrix-firstbreak-tail-gap-deep-collar-layer-ledger.json
```

本步继续攻击 `DeepLateShortCollarOrCoreExcessNamedReturnPDEC`。同步结果：

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

formal-to-actual 含义是：若 `x0=y-L`、`H=P-y`、`D=2y-P`，则

```text
L<=D <=> x0>=H <=> B subset [H,y-1].
```

这把 deep-late short branch 改写成自镜像 collar containment。

若 `L>D`，则跨出 collar。设

```text
M=L(L-D)+min(L,y-1).
```

正 gap 失败必须满足：

```text
X_core+R_named >= M.
```

同时 core excess 有 quotient 层分解：

```text
h=H+r,
k(h)=ceil((P-1)/h)-2,
X_core=sum_{k>=1} k sum_{h in I_k} min(L,h-H).
```

新的直接主攻为：

```text
SelfMirrorDeepLateCollarOrCoreLayerExcessNamedReturnPDEC
```

本步没有排斥自镜像 collar，也没有排斥 quotient core 层集中或 `R_named` 吃掉 margin；
它把剩余压成几何 self-mirror 分支和显式 quotient-layer 消耗分支。

## 181. Self-mirror tail-gap sieved-defect frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_sieved_defect_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-sieved-defect-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-sieved-defect-router.json
data/prime-matrix-firstbreak-tail-gap-sieved-defect-ledger.json
```

本步继续攻击 `SelfMirrorDeepLateCollarOrCoreLayerExcessNamedReturnPDEC`。同步结果：

```text
nonprime_defect_exact_closed=true
sqrt_rough_prime_tail_identity_closed=true
endpoint_parity_defect_lower_bound_closed=true
sieved_margin_functional_closed=true
sieved_positive_gap_criterion_closed=true
weighted_rough_crt_defect_excluded=false
self_mirror_sieved_gap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：令

```text
w(q)=min(L,q-H)ceil((P-1)/q).
```

真实 prime tail 不再用整数包络粗替，而是满足：

```text
C_tail=C_all-D_np,
D_np=sum_{H<q<P, q not prime}w(q).
```

取 `z=floor(sqrt(P-1))`、`W_z=prod_{ell<=z}ell` 后，`z<q<P` 中的
`gcd(q,W_z)=1` 与 `q prime` 等价。因此 tail 失败必须表现为：

```text
C_tail=sum_{H<q<=z, q prime}w(q)
      +sum_{z<q<P, gcd(q,W_z)=1}w(q)
```

过大，即 weighted sqrt-rough CRT 支撑过密。筛后真实 gap 为：

```text
G=L(L-D)+min(L,y-1)-X_core+D_np-R_named.
```

self-mirror 分支中：

```text
G=L(L-D)+L-X_core+D_np-R_named.
```

新的直接主攻为：

```text
SelfMirrorSievedTailGapOrWeightedRoughCRTDefectPDEC
```

本步没有证明 weighted rough 支撑不能过密；它把“整数 tail 可饱和”替换为
真实素数筛后的 CRT 过密/PDEC 接口。

## 182. Weighted rough tail LPF deletion frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_lpf_deletion_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-deletion-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-deletion-router.json
data/prime-matrix-firstbreak-tail-gap-lpf-deletion-ledger.json
```

本步继续攻击 `SelfMirrorSievedTailGapOrWeightedRoughCRTDefectPDEC`。同步结果：

```text
small_tail_finite_nonprime_defect_closed=true
large_tail_lpf_partition_closed=true
rough_prefix_deletion_telescoping_closed=true
lpf_crt_deletion_cell_closed=true
lpf_sieved_gap_functional_closed=true
dyadic_lpf_deletion_debt_excluded=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：weighted rough tail 的失败不再写成重叠包含-排除。
令

```text
D_small=sum_{H<q<=z, q not prime}w(q).
```

对大端 `z<q<P`，每个非素数有唯一最小素因子 `ell<=z`，所以：

```text
D_np=D_small+sum_{ell<=z}B_ell,
B_ell=sum_{z<q<P, ell=lpf(q)}w(q).
```

并且

```text
B_ell=sum_{z/ell<n<P/ell, gcd(n,W_<ell)=1}w(ell*n).
```

这是 disjoint CRT 删除层。若

```text
S_u=sum_{z<q<P, gcd(q,W_u)=1}w(q),
```

则递增筛满足：

```text
S_{ell^-}-S_ell=B_ell.
```

真实 gap 改写为：

```text
G=Phi+D_small+sum_{ell<=z}B_ell-R_named.
```

新的直接主攻为：

```text
LPFDeletionDebtOrRoughPrefixOverdensityPDEC
```

本步没有证明 LPF 删除层总能支付 gap；它把 rough over-density 压成互不重叠的
dyadic 最小素因子 CRT 删除债务。

## 183. LPF dyadic cofactor interval frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_lpf_dyadic_cofactor_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-dyadic-cofactor-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-dyadic-cofactor-router.json
data/prime-matrix-firstbreak-tail-gap-lpf-dyadic-cofactor-ledger.json
```

本步继续攻击 `LPFDeletionDebtOrRoughPrefixOverdensityPDEC`。同步结果：

```text
dyadic_layer_partition_closed=true
debt_localization_closed=true
ramp_saturated_weight_split_closed=true
quotient_layer_cofactor_interval_closed=true
cofactor_interval_endpoint_formula_closed=true
rough_cofactor_interval_crt_support_closed=true
dyadic_rough_cofactor_interval_debt_excluded=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：LPF 删除债务不再只以总量

```text
sum_{ell<=z}B_ell
```

出现，而是被定位到可检查的短 cofactor CRT 单元。先按 dyadic 层：

```text
B_Y=sum_{Y<ell<=2Y, ell prime}B_ell,
B_tot=sum_Y B_Y.
```

若总债务小于某个全局预算阈值，而候选预算向量总和超过该阈值，则至少一个
dyadic 层短缺。层内再按

```text
w(q)=min(L,q-H)ceil((P-1)/q)
```

拆成 ramp/saturated 权重，并按 `j=ceil((P-1)/q)` 分块。固定 `ell` 与 `j`
后，`q=ell*n` 且 `gcd(n,W_<ell)=1`。令 `A=P-1`，quotient 层的整数端点为：

```text
q_j_min=floor(A/j)+1,
q_j_max=A if j=1, else floor(A/(j-1)).
```

再与 `z<q<P` 和 ramp/saturated 边界相交，得到：

```text
n_min=ceil(q_min/ell),  n_max=floor(q_max/ell).
```

新的直接主攻为：

```text
DyadicRoughCofactorIntervalDebtOrColumnCRTPDEC
```

本步没有证明每个局部 rough cofactor 区间必给出足够删除质量；它把剩余从
全局 LPF 债务压成 dyadic/quotient/cofactor interval 上的局部 CRT 支撑债务。

## 184. Cofactor-LPF cover frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_cofactor_lpf_cover_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-cover-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-cover-router.json
data/prime-matrix-firstbreak-tail-gap-cofactor-lpf-cover-ledger.json
```

本步继续攻击 `DyadicRoughCofactorIntervalDebtOrColumnCRTPDEC`。同步结果：

```text
weighted_envelope_closed=true
support_quota_criterion_closed=true
cofactor_lpf_partition_closed=true
cofactor_lpf_crt_cell_closed=true
product_width_dichotomy_closed=true
local_cofactor_lpf_cover_debt_excluded=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：局部 rough 支撑不足被改写为 cofactor 小素因子删除过量。
固定 cell `C=(Y,sigma,j)` 并令 `alpha_{ell,n}=j*u(ell*n)`，定义：

```text
F_C=sum all alpha_{ell,n},
B_C=sum_{gcd(n,W_<ell)=1} alpha_{ell,n},
E_C=F_C-B_C.
```

对预算 `A_C` 有精确等价：

```text
B_C<A_C  <=>  E_C>F_C-A_C.
```

再按 cofactor 的最小素因子分区：

```text
E_C=sum_{ell in Y} sum_{r<ell} E_{r<-ell},
E_{r<-ell}=sum_{n in I_{ell,j,sigma}, r=lpf(n)} alpha_{ell,n}.
```

每个分区写成

```text
n=r*m, gcd(m,W_<r)=1.
```

这一步只使用整数 LPF 唯一性，不把短区间素数存在性作为黑箱。若参与覆盖的
distinct cofactor primes 为 `R_C`，则局部覆盖字周期为：

```text
M_R=prod_{r in R_C}r.
```

新的直接主攻为：

```text
CofactorLPFCoverDebtOrProductWidthColumnCRTPDEC
```

本步没有证明 cofactor-LPF 过覆盖不可能；它把 rough 支撑债务推到更低素因子的
短区间 CRT 覆盖债务与 product-width ColumnCRT/PDEC 出口。

## 185. Cofactor-LPF dyadic pressure frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_cofactor_lpf_dyadic_pressure_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-dyadic-pressure-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-dyadic-pressure-router.json
data/prime-matrix-firstbreak-tail-gap-cofactor-lpf-dyadic-pressure-ledger.json
```

本步继续攻击 `CofactorLPFCoverDebtOrProductWidthColumnCRTPDEC`。同步结果：

```text
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

formal-to-actual 含义是：cofactor-LPF 过覆盖被写成一个明确 excess threshold：

```text
H_C=F_C-A_C,
E_C>H_C.
```

活动素因子集合与其相位周期为：

```text
R_C={r prime: E_r(C)>0},
M_C=prod_{r in R_C}r.
```

若 `M_C>width(C)`，同一覆盖相位字的精确复现周期已经超过 cell 支撑宽度，只能登记为
product-width ColumnCRT/PDEC 或有限原子。否则进入 small-product active cover concentration。

然后按 dyadic `r` 层：

```text
E_C=sum_Z E_Z(C).
```

若 `E_C>H_C` 且候选预算 `sum_Z U_Z<=H_C`，则存在层 `E_Z(C)>U_Z`。固定 `r` 后：

```text
n=r*m,
m_min=ceil(n_min/r),
m_max=floor(n_max/r),
gcd(m,W_<r)=1.
```

新的直接主攻为：

```text
DyadicCofactorLPFPressureOrSmallProductColumnCRTPDEC
```

本步没有证明 dyadic `r` 层过载不可能；它把最新剩余压到 product-width 二分和更低阶
rough-m CRT 支撑压力。

## 186. Cofactor-LPF single-r pressure frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_cofactor_lpf_single_r_pressure_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-single-r-pressure-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-single-r-pressure-router.json
data/prime-matrix-firstbreak-tail-gap-cofactor-lpf-single-r-pressure-ledger.json
```

本步继续攻击 `DyadicCofactorLPFPressureOrSmallProductColumnCRTPDEC`。同步结果：

```text
active_prime_cardinality_closed=true
small_z_finite_atom_boundary_closed=true
single_r_pressure_localization_closed=true
fixed_r_source_ell_partition_closed=true
fixed_r_ell_rough_m_crt_cell_closed=true
fixed_pair_product_width_closed=true
single_r_pressure_excluded=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：small-product active cover 不再作为整体保留。对 `Z<r<=2Z`
的活动集合 `R_Z(C)`，`Z<2` 作为有限原子边界。对 `Z>=2`，若：

```text
M_Z=prod_{r in R_Z(C)}r <= W_C=width(C),
```

则：

```text
|R_Z(C)| <= floor(log W_C/log Z).
```

若同时 `E_Z(C)>U_Z`，则存在单个 `r` 满足：

```text
E_r(C)>U_Z/K_Z.
```

固定 `r` 后按 `ell` 分区，继续落到固定 `(r,ell)`：

```text
q=ell*r*m,
m_min=ceil(n_min/r),
m_max=floor(n_max/r),
gcd(m,W_<r)=1.
```

新的直接主攻为：

```text
SingleCofactorPrimePressureOrFixedPairMCRTColumnCRTPDEC
```

本步没有证明 single-r/fixed-pair pressure 不可能；它把 small-product dyadic 压力压成
单个 cofactor prime 和固定 pair 的 rough-m CRT 单元。

## 187. Fixed-pair second-LPF descent frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_fixed_pair_second_lpf_descent_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-fixed-pair-second-lpf-descent-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-fixed-pair-second-lpf-descent-router.json
data/prime-matrix-firstbreak-tail-gap-fixed-pair-second-lpf-descent-ledger.json
```

本步继续攻击 `SingleCofactorPrimePressureOrFixedPairMCRTColumnCRTPDEC`。同步结果：

```text
m_support_strict_descent_closed=true
m_equals_one_finite_atom_closed=true
second_lpf_partition_closed=true
second_lpf_crt_cell_closed=true
second_product_width_closed=true
strict_no_cycle_closed=true
second_lpf_pressure_excluded=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：固定 `(r,ell)` 后，压力单元为：

```text
q=ell*r*m,
gcd(m,W_<r)=1.
```

`m=1` 是有限原子。若 `m>1`，则：

```text
s=lpf(m)>=r,
m=s*t,
gcd(t,W_<s)=1.
```

端点为：

```text
t_min=ceil(m_min/s),
t_max=floor(m_max/s).
```

支撑宽度满足：

```text
width_t<=ceil(width_m/s)<=ceil(width_m/r).
```

在非有限分支 `r>=2`，所以每次二级 LPF 递降都严格降低支撑尺度，直到有限原子或
ColumnCRT/PDEC 出口。

新的直接主攻为：

```text
SecondLPFDescentPressureOrTripleMCRTColumnCRTPDEC
```

本步没有证明二级 LPF/triple pressure 不可能；它把 fixed-pair pressure 变成严格下降的
rough-t CRT 单元，排除了同尺度循环解释。

## 188. Iterated LPF rank-budget frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_iterated_lpf_rank_budget_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-iterated-lpf-rank-budget-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-iterated-lpf-rank-budget-router.json
data/prime-matrix-firstbreak-tail-gap-iterated-lpf-rank-budget-ledger.json
```

本步继续攻击 `SecondLPFDescentPressureOrTripleMCRTColumnCRTPDEC`。同步结果：

```text
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

formal-to-actual 含义是：二级/triple pressure 不再作为自由失败形态保留。固定
`(r,ell,s)` 后，递归抽取 residual 的 least prime factors：

```text
a_i=lpf(n_i),
n_i=a_i*n_{i+1},
r<=s<=a_1<=a_2<=...
```

令：

```text
A_h=s*prod_{i<=h}a_i.
```

则 residual 支撑宽度与 CRT 周期乘积满足互反不变量：

```text
width(n_h-support)<=ceil(width_m/A_h).
```

若没有 product-width ColumnCRT/PDEC 出口，则 `A_h<=width_m`，并且总因子深度
`d` 满足：

```text
d<=floor(log_r(width_m)).
```

新的直接主攻为：

```text
RankBudgetedIteratedLPFMovingFamilyOrColumnCRTPDEC
```

本步没有证明秩预算化 moving-family 不可能；它把二级/triple pressure 压成有限秩、
有限深、支撑-周期互反约束下的迭代 LPF 因子词族。

## 189. LPF word-entropy / first-moving-coordinate frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_lpf_word_entropy_motion_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-word-entropy-motion-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-word-entropy-motion-router.json
data/prime-matrix-firstbreak-tail-gap-lpf-word-entropy-motion-ledger.json
```

本步继续攻击 `RankBudgetedIteratedLPFMovingFamilyOrColumnCRTPDEC`。同步结果：

```text
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

formal-to-actual 含义是：rank-budgeted moving-family 不能再作为匿名总量保留。每个
residual 有唯一 LPF word：

```text
omega=(s,a_1,...,a_d),
A(omega)=s*prod_{i<=d}a_i.
```

未进入 product-width 出口时：

```text
A(omega)<=W,
d+1<=floor(log_r W).
```

因此活动 word 集有限。若聚合压力超界，则至少一个 word 承压；该 word 若稳定，则回到
固定 MCRT/ColumnCRT；若不稳定，则有首个移动 LPF 坐标 `mu`，并满足：

```text
width_after_mu<=ceil(W/(A_prefix*mu)).
```

新的直接主攻为：

```text
FirstMovingLPFCoordinatePressureOrWordMotionColumnCRTPDEC
```

本步没有证明首移动 LPF 坐标压力不可能；它只把移动族压力从匿名 family 压到第一个
真正改变相位/容量的素坐标。

## 190. First-moving LPF coordinate frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_first_moving_lpf_coordinate_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-first-moving-lpf-coordinate-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-first-moving-lpf-coordinate-router.json
data/prime-matrix-firstbreak-tail-gap-first-moving-lpf-coordinate-ledger.json
```

本步继续攻击 `FirstMovingLPFCoordinatePressureOrWordMotionColumnCRTPDEC`。同步结果：

```text
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

formal-to-actual 含义是：首移动坐标池也不能匿名保留。稳定前缀给出：

```text
A_prefix,
W_prefix=floor(W/A_prefix).
```

若 `mu>W_prefix`，或活动坐标乘积超过 `W_prefix`，则相位周期超过有效支撑并回到
ColumnCRT/PDEC 或有限原子。除低坐标 `mu<=2` 的有限原子外，活动坐标落入
`B<mu<=2B, B>=2`，并有：

```text
|M_B|<=floor(log W_prefix/log B)
```

除非先触发 product-width 出口。因此超界压力必须落在单个 `mu`。若该 `mu` 稳定，
回到固定 word 坐标；若漂移，新的直接主攻为：

```text
SingleMovingLPFCoordinateDriftOrPrefixColumnCRTPDEC
```

本步没有证明单个 moving LPF coordinate drift 不可能；它把首移动坐标压力压到单坐标
漂移接口。

## 191. Single-moving LPF coordinate scale-escape frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_single_moving_lpf_coordinate_scale_escape_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-single-moving-lpf-coordinate-scale-escape-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-single-moving-lpf-coordinate-scale-escape-router.json
data/prime-matrix-firstbreak-tail-gap-single-moving-lpf-coordinate-scale-escape-ledger.json
```

本步继续攻击 `SingleMovingLPFCoordinateDriftOrPrefixColumnCRTPDEC`。同步结果：

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

formal-to-actual 含义是：单个移动 LPF 坐标也不能作为匿名漂移口径保留。稳定前缀给出：

```text
W_prefix=floor(W/A_prefix).
```

对 `mu` 取 dyadic 尺度：

```text
B(mu)=2^floor(log_2 mu),
B(mu)<=mu<=2B(mu).
```

若尺度有界，则 `mu` 在无限子族中退化为固定坐标，回到固定 ColumnCRT/PDEC 或有限原子。
若真漂移，则尺度必须无界；加入该坐标后：

```text
W_after<=ceil(W_prefix/mu)<=ceil(W_prefix/B(mu)).
```

因此非有限分支不能在同一尺度循环。新的直接主攻为：

```text
ScaleEscapingSingleCoordinateDescentOrSparseDriftSAEColumnCRTPDEC
```

本步没有证明尺度逃逸单坐标递降族不可能，也没有证明 sparse drift/SAE 全局可求和；
它只把单坐标漂移压到尺度逃逸递降和稀疏漂移出口。

## 192. Scale-escape support-clock frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_scale_escape_support_clock_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-scale-escape-support-clock-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-scale-escape-support-clock-router.json
data/prime-matrix-firstbreak-tail-gap-scale-escape-support-clock-ledger.json
```

本步继续攻击 `ScaleEscapingSingleCoordinateDescentOrSparseDriftSAEColumnCRTPDEC`。同步结果：

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

formal-to-actual 含义是：尺度逃逸递降也不能匿名循环保留。定义：

```text
K(W)=ceil(log_2 max(W,1)).
```

每个真实尺度逃逸坐标给出：

```text
W_{i+1}<=ceil(W_i/B_i), B_i>=2,
K(W_{i+1})<=K(W_i)-1 when W_i>=2.
```

因此同一反例纤维上的尺度逃逸链有有限深度；到 `W<=1` 则为有限原子，到
`prod_i B_i>W_0` 则为 product-width ColumnCRT/PDEC 或有限原子。新的直接主攻为：

```text
PersistentScaleLadderSignatureOrSparseScaleLadderSAEColumnCRTPDEC
```

本步没有证明持久尺度阶梯签名不可能，也没有证明 sparse scale-ladder SAE 全局可求和；
它只把抽象 scale-escape descent 压到有时钟的持久阶梯签名或稀疏出口。

## 193. Scale-ladder word-entropy frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_scale_ladder_word_entropy_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-scale-ladder-word-entropy-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-scale-ladder-word-entropy-router.json
data/prime-matrix-firstbreak-tail-gap-scale-ladder-word-entropy-ledger.json
```

本步继续攻击 `PersistentScaleLadderSignatureOrSparseScaleLadderSAEColumnCRTPDEC`。同步结果：

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

formal-to-actual 含义是：持久尺度阶梯签名也不能作为匿名容量池。写：

```text
B_i=2^{b_i}, b_i>=1,
sigma=(b_1,...,b_d),
A_sigma=2^{sum_i b_i}.
```

非 product-width 出口满足：

```text
sum_i b_i<=K_0=ceil(log_2 max(W_0,1)),
N_ladder(K_0)<=2^{K_0}.
```

所以聚合压力必须定位到单个尺度词。若该尺度词下实际素坐标与相位稳定，则为固定
MCRT/ColumnCRT/PDEC 或有限原子；若不稳定，新的直接主攻为：

```text
FirstMovingScaleLadderPhaseDriftOrSparseScaleLadderSAEColumnCRTPDEC
```

本步没有证明固定尺度词内首个移动素坐标/相位漂移不可能，也没有证明 sparse
scale-ladder SAE 全局可求和；它只把持久签名池压到单个尺度词的首移动层。

## 194. Scale-ladder finite-slot lock frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_scale_ladder_finite_slot_lock_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-scale-ladder-finite-slot-lock-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-scale-ladder-finite-slot-lock-router.json
data/prime-matrix-firstbreak-tail-gap-scale-ladder-finite-slot-lock-ledger.json
```

本步继续攻击 `FirstMovingScaleLadderPhaseDriftOrSparseScaleLadderSAEColumnCRTPDEC`。同步结果：

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

formal-to-actual 含义是：固定尺度词内不能存在持久首移动漂移。因为固定：

```text
sigma=(b_1,...,b_d)
```

后，每槽实际素数和相位只在有限集合内取值：

```text
Q_i={q prime: 2^{b_i}<=q<2^{b_i+1}},
N_actual(sigma)<=prod_i sum_{q in Q_i} q < infinity.
```

所以无限持久分支必有稳定实际素数-相位词子族，回到固定 MCRT/ColumnCRT/PDEC
或有限原子。新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderColumnCRTPDEC
```

本步没有排斥稳定实际 ladder 的 ColumnCRT/PDEC 出口，也没有证明 sparse
scale-ladder SAE 全局可求和；它只删除固定尺度词内持久首移动漂移。

## 195. Stable-ladder Fourier/PDEC frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_fourier_pdec_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-fourier-pdec-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-fourier-pdec-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-fourier-pdec-ledger.json
```

本步继续攻击 `SparseScaleLadderSAESummabilityOrStableActualLadderColumnCRTPDEC`。
同步结果：

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

formal-to-actual 含义是：上一层留下的稳定实际 ladder 不再以匿名 ColumnCRT
出口保存，而是被写成有限乘积群

```text
G=prod_i Z/q_iZ
```

上的固定点位 `a=(a_i)_i`。对映射 `tau(n)=(n mod q_i)_i` 定义
`F_a(g)=1_{g=a}-1/|G|`，则支撑超额满足精确恒等式

```text
E_a(S)=sum_{n in S}F_a(tau(n))
      =#{n in S:tau(n)=a}-|S|/|G|.
```

有限群 Fourier 展开给出：

```text
E_a(S)=sum_{chi!=1} hat F_a(chi) * sum_{n in S}chi(tau(n)).
```

因此若该稳定 ladder 真的产生正超额，则存在非平凡角色满足

```text
|sum_{n in S}chi(tau(n))| >= |G|*E_a(S)/(|G|-1).
```

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderFourierPDECCap
```

本步没有证明 stable actual ladder Fourier/PDEC cap，也没有证明 sparse
scale-ladder SAE 全局可求和；它只把稳定实际 ladder 的黑箱 CRT 出口回接到显式
Fourier/PDEC 输入。

## 196. Stable-ladder pivot-fiber PDEC frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_pivot_fiber_pdec_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-pivot-fiber-pdec-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-pivot-fiber-pdec-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-pivot-fiber-pdec-ledger.json
```

本步继续攻击 `SparseScaleLadderSAESummabilityOrStableActualLadderFourierPDECCap`。
同步结果：

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

formal-to-actual 含义是：稳定 ladder 的非平凡 Fourier 异常不能继续保留为全局
角色黑箱。任一非平凡角色分解为坐标角色乘积 `chi=prod_i chi_i`，选择一个
非平凡坐标 `j`，并按其余坐标分割支撑：

```text
S_h={n in S: tau_{-j}(n)=h}.
```

若全局角色和满足 `|S_chi|>=Lambda`，则

```text
|S_chi|<=sum_h |A_h|<=|G_{-j}| max_h |A_h|,
A_h=sum_{n in S_h} chi_j(n mod q_j).
```

因此存在一个补坐标纤维 `h` 使

```text
|A_h|>=Lambda/|G_{-j}|.
```

代入上一层 `Lambda=N*E_a(S)/(N-1)` 得到：

```text
|A_h|>=q_j*E_a(S)/(N-1).
```

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderPrimitiveFiberPDECCap
```

本步没有证明 primitive pivot-fiber PDEC cap，也没有证明 sparse scale-ladder
SAE 全局可求和；它只把全局 Fourier cap 局部化为单坐标纤维相位相关。

## 197. Stable-ladder residue-count PDEC frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_residue_count_pdec_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-residue-count-pdec-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-residue-count-pdec-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-residue-count-pdec-ledger.json
```

本步继续攻击 `SparseScaleLadderSAESummabilityOrStableActualLadderPrimitiveFiberPDECCap`。
同步结果：

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

formal-to-actual 含义是：primitive fiber 的角色相位异常不能继续保留为字符和
黑箱。固定补坐标纤维 `S_h` 后，定义余数计数

```text
M_r=#{n in S_h: n mod q_j=r}, L=|S_h|, D_r=M_r-L/q_j.
```

由于 `chi_j` 非平凡，`sum_r chi_j(r)=0`，所以

```text
A_h=sum_r M_r chi_j(r)=sum_r D_r chi_j(r).
```

于是：

```text
|A_h|<=sum_r |D_r|<=q_j max_r |D_r|.
```

结合上一层 `|A_h|>=q_j*E_a(S)/(N-1)`，得到某个余数 `r` 满足：

```text
|M_r-L/q_j|>=E_a(S)/(N-1).
```

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderResidueCountPDECCap
```

本步没有证明 residue-count PDEC cap，也没有证明 sparse scale-ladder SAE
全局可求和；它只把 primitive fiber 角色相关局部化为单余数类计数偏差。

## 198. Stable-ladder positive-surplus PDEC frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_positive_surplus_pdec_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-positive-surplus-pdec-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-positive-surplus-pdec-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-positive-surplus-pdec-ledger.json
```

本步继续攻击 `SparseScaleLadderSAESummabilityOrStableActualLadderResidueCountPDECCap`。
同步结果：

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

formal-to-actual 含义是：固定纤维内的有符号计数偏差可统一改写为正向过载。
设 `D_r=M_r-L/q_j` 且 `sum_r D_r=0`。若 `|D_r|>=delta`，则正分支直接给出
`D_r>=delta`；负分支给出

```text
sum_{s!=r}D_s>=delta.
```

所以某个余数类满足：

```text
D_s>=delta/(q_j-1).
```

代入 `delta=E_a(S)/(N-1)` 得到：

```text
M_s-L/q_j>=E_a(S)/((N-1)(q_j-1)).
```

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderPositiveResidueSurplusPDECCap
```

本步没有证明 positive residue-surplus PDEC cap，也没有证明 sparse scale-ladder
SAE 全局可求和；它只把有符号余数计数偏差改写为正余数过载输入。

## 199. Stable-ladder occupancy-dichotomy frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_occupancy_dichotomy_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-occupancy-dichotomy-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-occupancy-dichotomy-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-occupancy-dichotomy-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableActualLadderPositiveResidueSurplusPDECCap`。
同步结果：

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

formal-to-actual 含义是：正余数过载已经不再是匿名容量口径。设固定纤维内
某余数类占位数满足

```text
M_s-L/q_j>=eta>0.
```

由于 `M_s` 是整数，占位非空。若 `M_s=1`，则得到 singleton surplus atom；
若 `M_s>=2`，则得到同一完整 stable-ladder cell 中两点 `n1<n2`。在后一个
分支，令 `W=lcm_i(q_i)`，同 cell 同余给出：

```text
n2-n1 is a nonzero multiple of W.
```

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderSingletonSurplusOrCellPairPeriodPDECCap
```

本步没有证明 singleton surplus atom 全局可求和，也没有证明 same-cell
period-pair PDEC cap；它只把正过载口径改写为整数占位的 singleton/pair 二分。

## 200. Stable-ladder singleton/pair width frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_singleton_pair_width_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-singleton-pair-width-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-singleton-pair-width-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-singleton-pair-width-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableActualLadderSingletonSurplusOrCellPairPeriodPDECCap`。
同步结果：

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

formal-to-actual 含义是：上一层的 singleton/pair 出口可以再拆成两个更具体的
几何-容量接口。若 `M_s=1` 且仍有正过载 `M_s-L/q_j>=eta>0`，则：

```text
L<q_j.
```

若 same-cell pair 存在，则：

```text
n2-n1=tW>=W,
H>=W.
```

所以短支撑 `H<W` 分支不能承载 pair；剩余 pair 必是长宽度 period-pair。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderLowFiberSingletonSurplusOrLongWidthCellPairPDECCap
```

本步没有证明低纤维 singleton 全局可求和，也没有证明长宽度 same-cell
period-pair PDEC cap；它只把 singleton/pair 改写为低纤维/长宽度二分。

## 201. Stable-ladder low-fiber phase frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_low_fiber_phase_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-low-fiber-phase-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-low-fiber-phase-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-low-fiber-phase-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableActualLadderLowFiberSingletonSurplusOrLongWidthCellPairPDECCap`。
同步结果：

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

formal-to-actual 含义是：低纤维 singleton 的 `1<=L<q_j` 不是最终原子；
它要么是 `L=1` 的补纤维孤立 atom，要么在 `2<=L<q_j` 时强制出现一个
补坐标同纤维、pivot 残基不同的双点。令：

```text
W_-j=lcm_{i!=j}(q_i).
```

非孤立分支满足：

```text
W_-j | (n2-n1),
q_j does not divide (n2-n1),
H>=W_-j.
```

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrAntiPivotComplementPairOrLongFullCellPairPDECCap
```

本步没有证明孤立 singleton 全局可求和，也没有证明 anti-pivot complement-pair
或 long full-cell pair 的 PDEC cap；它只把低纤维 singleton 改写为孤立/相位反对齐二分。

## 202. Stable-ladder pair quotient-phase frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_pair_quotient_phase_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-pair-quotient-phase-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-pair-quotient-phase-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-pair-quotient-phase-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrAntiPivotComplementPairOrLongFullCellPairPDECCap`。
同步结果：

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

formal-to-actual 含义是：anti-pivot complement pair 与 long full-cell pair
不是两个独立黑箱；二者都是补周期商变量的 pivot 相位。令：

```text
B=W_-j,
d=n2-n1=tB,
g=gcd(q_j,B),
R=q_j/g.
```

则：

```text
anti-pivot branch <=> t not congruent 0 mod R,
full-cell branch <=> t congruent 0 mod R.
```

支撑直径给出 `1<=t<=floor(H/B)`，从而 pair 剩余被统一为 quotient phase
cycle PDEC/cap。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrPairQuotientPhaseCyclePDECCap
```

本步没有证明孤立 singleton 全局可求和，也没有证明 quotient phase cycle
PDEC/cap；它只把 anti-pivot/full-cell pair 统一到补周期商变量与 pivot 相位周期。

## 203. Stable-ladder quotient short-arc/mean frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_quotient_phase_arc_mean_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-phase-arc-mean-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-phase-arc-mean-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-phase-arc-mean-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrPairQuotientPhaseCyclePDECCap`。
同步结果：

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

formal-to-actual 含义是：quotient cycle 不能再作为未分解黑箱。令

```text
T=floor(H/B).
```

若 `T<R`，则 `1<=t<=T` 是 `Z/RZ` 的真短弧，零相位不存在；no-wrap 分支
只能是 short-arc cluster。若 `T>=R`，则 `T=aR+s`，完整周期只给 formal
phase mean，尾段仍是短弧；actual 偏差必须进入 phase-cycle actual-mean cap。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrQuotientShortArcClusterOrPhaseCycleMeanPDECCap
```

本步没有证明 short-arc cluster cap、phase-cycle actual-mean cap、孤立
singleton 求和或 sparse SAE 求和；它只把 quotient phase cycle 拆成短弧和
完整周期均值/尾弧。

## 204. Stable-ladder quotient arc Fourier frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_quotient_arc_fourier_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-arc-fourier-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-arc-fourier-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-arc-fourier-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrQuotientShortArcClusterOrPhaseCycleMeanPDECCap`。
同步结果：

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

formal-to-actual 含义是：short-arc cluster 与 phase-cycle mean 不是两个出口；
它们都是 `C_R=Z/RZ` 上中心化 actual phase load `nu` 与区间指标 `1_A`
的相关：

```text
Delta(A)=sum_{r in A}nu(r).
```

由于 `sum nu=0`，平凡频率消失，Dirichlet kernel 恒等式给出：

```text
Delta(A)=(1/R) sum_{h=1}^{R-1} hat nu(h) hat 1_A(-h).
```

因此 `Delta(A)>0` 强制存在非平凡频率：

```text
|hat nu(h)| >= R*Delta(A)/sum_{h=1}^{R-1}|hat 1_A(h)|.
```

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrQuotientArcFourierPDECCap
```

本步没有证明 quotient arc Fourier/PDEC cap、孤立 singleton 求和或 sparse
SAE 求和；它只把 short-arc/phase-mean 剩余桥接为显式非平凡频率证书。

## 205. Stable-ladder quotient Fourier lift frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_quotient_fourier_lift_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-fourier-lift-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-fourier-lift-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-fourier-lift-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrQuotientArcFourierPDECCap`。
同步结果：

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

formal-to-actual 含义是：quotient 非平凡频率可以反解为原始 pair 差值相位。
写

```text
g=gcd(q_j,B), B=gB0, q_j=gR, gcd(B0,R)=1.
```

取 `uB0 == 1 mod R`。若 `d=tB`，则：

```text
t == u*(d/g) mod R.
```

因此对任意 `h!=0 mod R`：

```text
e_R(h*t)=e_{q_j}(beta*d), beta == h*u mod R.
```

再展开 `d=n2-n1`，得到 endpoint bilinear phase：

```text
e_{q_j}(beta*(n2-n1))
  = e_{q_j}(beta*n2) * conjugate(e_{q_j}(beta*n1)).
```

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrQuotientEndpointBilinearFourierPDECCap
```

本步没有证明 endpoint bilinear Fourier/PDEC cap、孤立 singleton 求和或 sparse
SAE 求和；它只把 quotient arc Fourier 频率提升为原始 pair 端点双线性相位。

## 206. Stable-ladder endpoint bilinear balance frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_bilinear_balance_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-bilinear-balance-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-bilinear-balance-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-bilinear-balance-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrQuotientEndpointBilinearFourierPDECCap`。
同步结果：

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

formal-to-actual 含义是：上一层的端点双线性相位不再作为匿名整体处理。
把 actual pair witnesses 登记为端点二部矩阵：

```text
M(x,y), x=n1 mod q_j, y=n2 mod q_j.
```

减去显式 model 得中心化核 `K`。设：

```text
rho(x)=sum_y K(x,y), sigma(y)=sum_x K(x,y).
```

则：

```text
K(x,y)=rho(x)/|Y| + sigma(y)/|X| + K0(x,y),
sum_y K0(x,y)=0,
sum_x K0(x,y)=0.
```

对非平凡角色 `phi_beta(z)=e_{q_j}(beta z)`，

```text
S_beta=sum K(x,y)conjugate(phi_beta(x))phi_beta(y)
      =S_row(beta)+S_col(beta)+S_bal(beta).
```

若 `|S_beta|>=eta`，则 row marginal Fourier、column marginal Fourier
或 balanced core 至少一项达到 `eta/3`。在 balanced 分支：

```text
||K0||_HS^2 >= eta^2/(9|X||Y|).
```

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrEndpointMarginalFourierOrBalancedBilinearEnergyPDECCap
```

本步没有证明端点边际 Fourier/PDEC cap、balanced bilinear energy/PDEC cap、
孤立 singleton 求和或 sparse SAE 求和；它只把 endpoint bilinear Fourier
cap 拆成可审计的边际/平衡核出口。

## 207. Stable-ladder endpoint energy packet frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_energy_packet_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-energy-packet-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-energy-packet-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-energy-packet-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrEndpointMarginalFourierOrBalancedBilinearEnergyPDECCap`。
同步结果：

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

formal-to-actual 含义是：端点边际 Fourier 与 balanced core 能量不再作为
匿名异常保存。若边际 Fourier 满足：

```text
|hat rho(beta)| >= eta,
```

则 Parseval 给出：

```text
sum_x |rho(x)|^2 >= eta^2/q_j.
```

balanced 分支直接给出 `||K0||_HS^2 >= E`。两者都可在有限端点支持上做
dyadic pigeonhole，得到某个尺度 `lambda` 和一个一维或二维能量包：

```text
lambda^2 * |packet support| >= energy/L.
```

再按正负偏差取至少半能量一侧，得到带有 `dimension`、`lambda`、`sign`、
`support` 的 endpoint dyadic energy packet。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrEndpointDyadicEnergyPacketPDECCap
```

本步没有证明 endpoint dyadic energy packet/PDEC cap、孤立 singleton 求和或
sparse SAE 求和；它只把端点边际 Fourier 与 balanced energy 出口变成显式
可计数能量包。

## 208. Stable-ladder endpoint packet autocorrelation frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_packet_autocorrelation_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-packet-autocorrelation-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-packet-autocorrelation-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-packet-autocorrelation-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrEndpointDyadicEnergyPacketPDECCap`。
同步结果：

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

formal-to-actual 含义是：dyadic energy packet 不再停留在抽象能量。设其同号
支持为：

```text
S={z in H: lambda < epsilon*F(z) <= 2lambda}.
```

若 `|S|=1`，它是 endpoint packet singleton atom。若 `|S|=m>=2`，则非零
差分支持对满足：

```text
sum_{delta != 0} C_S(delta)=m(m-1).
```

所以存在非零位移：

```text
C_S(delta) >= m(m-1)/(|H|-1).
```

同号尺度给出 weighted autocorrelation：

```text
A_F(delta)>=lambda^2*C_S(delta).
```

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrEndpointPacketSingletonAtomSAEOrEndpointDisplacementAutocorrelationPDECCap
```

本步没有证明 endpoint packet singleton atom/SAE、endpoint displacement
autocorrelation/PDEC cap、孤立 singleton 求和或 sparse SAE 求和；它只把能量包
变成显式非零位移自相关或单点 atom。

## 209. Stable-ladder endpoint displacement orbit frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_displacement_orbit_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-displacement-orbit-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-displacement-orbit-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-displacement-orbit-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrEndpointPacketSingletonAtomSAEOrEndpointDisplacementAutocorrelationPDECCap`。
同步结果：

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

formal-to-actual 含义是：singleton 出口统一为 `EndpointSingletonAtomSAE`；
非零位移自相关不再留在全群，而进入单个平移周期轨道。令：

```text
r=ord_H(delta)>1,
Omega=H/<delta>.
```

则每个轨道为：

```text
O=a+<delta>={a+t*delta: t in Z/rZ}.
```

全局加权自相关分解为：

```text
A_F(delta)=sum_{O in Omega} A_O(delta).
```

因此存在单个轨道承载至少平均质量：

```text
A_O(delta) >= A_F(delta)/|Omega|.
```

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointTranslationOrbitAdjacencyPDECCap
```

本步没有证明 endpoint singleton atom/SAE、endpoint translation orbit
adjacency/PDEC cap 或 sparse SAE 求和；它只把非零位移自相关压成单个 CRT
平移周期上的循环邻接包。

## 210. Stable-ladder endpoint orbit run/boundary frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_run_boundary_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-run-boundary-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-run-boundary-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-run-boundary-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointTranslationOrbitAdjacencyPDECCap`。
同步结果：

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

formal-to-actual 含义是：单轨道邻接包不再保持为抽象相位对象，而被写成
`C_r=Z/rZ` 上的 signed active sequence。dyadic 尺度把加权邻接质量 `W`
与同号邻接边数 `E` 关联为：

```text
lambda^2 E <= W <= 4 lambda^2 E.
```

将 active 同号连续点分解为极大 cyclic runs。除 full-cycle 同号特例外：

```text
E=n-b.
```

因此对任意边界预算 `B>=1`，要么切口数 `b>B`，要么存在同号连续弧：

```text
L_max >= E/B.
```

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitLongSameSignArcSAEOrEndpointOrbitBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、long same-sign arc SAE、boundary
flux/PDEC cap 或 sparse SAE 求和；它只把单轨道邻接 cap 压成长弧或边界通量
二分。

## 211. Stable-ladder endpoint orbit signed Fourier frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_signed_fourier_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-signed-fourier-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-signed-fourier-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-signed-fourier-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitLongSameSignArcSAEOrEndpointOrbitBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：长同号弧和边界通量现在被统一写成同一个 signed
cycle function：

```text
g_t=sigma_t*u_t in {-1,0,1}.
```

非全周期极大长同号 run 给出正中心化区间差：

```text
Delta_epsilon(I)>=|I|/r.
```

再由 Dirichlet kernel 给出非零 signed Fourier 下界。边界通量则通过循环差分
`Dg_t=g_{t+1}-g_t` 与 Parseval 给出 derivative Fourier 下界。全周期同号退化
单独登记为 full-cycle mean atom。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitSignedFourierPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、signed
Fourier/PDEC cap 或 sparse SAE 求和；它只把 long-arc/boundary 二出口压成
full-cycle mean atom 或 signed Fourier cap。

## 212. Stable-ladder endpoint orbit conductor-character frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_conductor_character_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-conductor-character-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-conductor-character-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-conductor-character-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitSignedFourierPDECCap`。
同步结果：

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

formal-to-actual 含义是：signed Fourier 的非零频率不再作为匿名 `h` 保留。
令 `d=gcd(h,r)`，`m=r/d`，`h0=h/d`，则 `h0` 与 `m` 互素，且原 Fourier
和精确折叠为：

```text
hat g(h)=sum_{s mod m} G_s exp(-2*pi*i*h0*s/m),
G_s=sum_{u=0}^{d-1} g_{s+u*m}.
```

所以 signed Fourier cap 现在是导子 `m` 上的 primitive additive character
packet。derivative Fourier 分支通过 `|omega_r^h-1|<=2` 只损失常数进入同一
出口。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitPrimitiveConductorCharacterPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、
primitive conductor character/PDEC cap 或 sparse SAE 求和；它只把 signed
Fourier 频率规范化到 primitive conductor character packet。

## 213. Stable-ladder endpoint orbit standard-character frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_standard_character_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-standard-character-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-standard-character-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-standard-character-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitPrimitiveConductorCharacterPDECCap`。
同步结果：

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

formal-to-actual 含义是：primitive conductor character 中的频率 `h0` 不再保留
为真实硬点。由于 `gcd(h0,m)=1`，乘以 `h0` 是 `C_m` 的置换。取
`u*h0==1 mod m`，并令：

```text
a=h0*s mod m,
S_a=G_{u*a mod m}.
```

于是精确恒等式为：

```text
sum_{s mod m} G_s exp(-2*pi*i*h0*s/m)
  = sum_{a mod m} S_a exp(-2*pi*i*a/m).
```

该置换保持支撑、`L1/L2` 质量、均值和 Fourier 下界常数。因此 primitive
频率参数被删除，新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStandardConductorFirstHarmonicPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、
standard conductor first-harmonic PDEC/cap 或 sparse SAE 求和；它只把 primitive
conductor character packet 规范化为标准 first-harmonic packet。

## 214. Stable-ladder endpoint orbit axis-lobe frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_axis_lobe_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-axis-lobe-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-axis-lobe-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-axis-lobe-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStandardConductorFirstHarmonicPDECCap`。
同步结果：

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

formal-to-actual 含义是：standard first harmonic 的复数相位不再作为最后硬点
保留。令：

```text
F=sum_{a mod m} S_a exp(-2*pi*i*a/m).
```

则：

```text
Re F=sum_a S_a cos(2*pi*a/m),
Im F=-sum_a S_a sin(2*pi*a/m),
max(|Re F|, |Im F|) >= |F|/sqrt(2).
```

所以存在某个轴 `j` 和符号 `eps`，使：

```text
sum_a S_a eps*phi_j(a) >= M/sqrt(2).
```

把 `eps*phi_j` 分解为正负半圆叶片权重 `w-v` 后，得到：

```text
sum_a S_a*(w_a-v_a) >= M/sqrt(2).
```

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitAxisLobeWeightedSurplusPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、
axis-lobe weighted surplus PDEC/cap 或 sparse SAE 求和；它只把 standard
first-harmonic cap 压成轴向半圆叶片加权盈余包。

## 215. Stable-ladder endpoint orbit single-lobe frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_single_lobe_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-single-lobe-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-single-lobe-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-single-lobe-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitAxisLobeWeightedSurplusPDECCap`。
同步结果：

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

formal-to-actual 含义是：axis-lobe 的双叶片差异不再作为最后硬点保留。把

```text
sum_a S_a*(w_a-v_a) >= L
```

写成 `A-B>=L`，其中：

```text
A=sum_a S_a*w_a,
B=sum_a S_a*v_a.
```

于是 `A>=L/2` 或 `-B>=L/2`。因此存在单个半圆叶片 `W` 和符号 `eta`，使：

```text
sum_a eta*S_a*W_a >= L/2,
0 <= W_a <= 1.
```

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitSingleLobeSignedSurplusPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、
single-lobe signed surplus PDEC/cap 或 sparse SAE 求和；它只把 axis-lobe
weighted surplus cap 压成单叶片带符号盈余包。

## 216. Stable-ladder endpoint orbit single-arc frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_single_arc_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-single-arc-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-single-arc-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-single-arc-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitSingleLobeSignedSurplusPDECCap`。
同步结果：

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

formal-to-actual 含义是：单叶片连续权重 `W` 不再作为最后硬点保留。由

```text
W_a=int_0^1 1_{W_a>=t} dt
```

得到：

```text
sum_a eta*S_a*W_a = int_0^1 sum_{a:W_a>=t} eta*S_a dt.
```

若加权和至少为 `L`，则某个超水平集弧段 `A_t={a:W_a>=t}` 满足：

```text
sum_{a in A_t} eta*S_a >= L.
```

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitSingleArcSignedSurplusPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、
single-arc signed surplus PDEC/cap 或 sparse SAE 求和；它只把 single-lobe
signed surplus cap 压成单弧 signed surplus 包。

## 217. Stable-ladder endpoint orbit arc endpoint-potential frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_arc_endpoint_potential_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-arc-endpoint-potential-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-arc-endpoint-potential-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-arc-endpoint-potential-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitSingleArcSignedSurplusPDECCap`。
同步结果：

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

formal-to-actual 含义是：单弧内部盈余不再作为最后硬点保留。把

```text
sum_{a in A}X_a >= L
```

写成全周期均值与中心化弧差：

```text
sum_{a in A}X_a = |A|*mu + sum_{a in A}(X_a-mu).
```

若均值项承担半数负载，则进入 full-cycle mean atom 出口。否则令
`Y_a=X_a-mu`，中心化前缀势能 `F(j+1)=F(j)+Y_j` 满足：

```text
sum_{a in [u,v)}Y_a = F(v)-F(u) >= L/2.
```

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitArcEndpointPotentialPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、
arc endpoint-potential PDEC/cap 或 sparse SAE 求和；它只把 single-arc
signed surplus cap 压成 full-cycle mean atom 或端点势能差包。

## 218. Stable-ladder endpoint orbit potential-variation frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_potential_variation_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-potential-variation-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-potential-variation-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-potential-variation-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitArcEndpointPotentialPDECCap`。
同步结果：

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

formal-to-actual 含义是：端点势能差不再作为最后硬点保留。若

```text
F(v)-F(u)>=G
```

且 `Y_j=F(j+1)-F(j)`，则沿弧 `I=[u,v)` 与补弧 `J=[v,u)` 有：

```text
sum_{j in I}Y_j>=G,
sum_{j in J}Y_j<=-G.
```

所以实际边增量必须满足：

```text
sum_{j in I}(Y_j)_+>=G,
sum_{j in J}(Y_j)_->=G.
```

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitSignedVariationPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、
signed variation PDEC/cap 或 sparse SAE 求和；它只把 arc endpoint-potential
cap 压成轨道边增量 signed variation 包。

## 219. Stable-ladder endpoint orbit variation run/boundary frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_variation_run_boundary_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-variation-run-boundary-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-variation-run-boundary-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-variation-run-boundary-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitSignedVariationPDECCap`。
同步结果：

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

formal-to-actual 含义是：signed variation 不再作为最后硬点保留。把某一侧

```text
sum_{j in K}(sigma*Y_j)_+>=G
```

的正增量边分解为极大连续 runs。若 run 数超过预算 `B`，这是高切换边界通量；
若 run 数不超过 `B`，则存在一个同符号增量 run 满足：

```text
sum_{j in R_h}sigma*Y_j>=G/B.
```

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitIncrementRunSurplusSAEOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、
increment-run surplus SAE、variation-boundary flux PDEC/cap 或 sparse SAE 求和；
它只把 signed variation cap 压成同符号增量 run 或边界通量二分。

## 220. Stable-ladder endpoint orbit increment-run amplitude/drift frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_increment_run_amplitude_drift_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-increment-run-amplitude-drift-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-increment-run-amplitude-drift-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-increment-run-amplitude-drift-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitIncrementRunSurplusSAEOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：低切换 increment-run surplus 不再作为匿名出口保留。
上一层给出连续同符号增量 run：

```text
Z_j=sigma*Y_j>0,  sum_{j in R}Z_j>=H,  H=G/B.
```

对任意幅度阈值 `Lambda`，若某边 `Z_j>=Lambda`，则进入单边大增量
edge-spike atom；若所有边 `Z_j<Lambda`，则：

```text
|R|>=H/Lambda.
```

这把低切换大质量 run 改写为长的有界增量单调漂移支路。高切换
variation-boundary flux 从上一层继续前传。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitIncrementEdgeSpikeSAEOrEndpointOrbitLongBoundedIncrementDriftPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、
increment edge-spike SAE、long bounded-increment drift PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；它只把低切换
increment-run surplus 压成单边大增量或长有界单调漂移二分。

## 221. Stable-ladder endpoint orbit edge-spike mean/singleton frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_edge_spike_mean_singleton_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-edge-spike-mean-singleton-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-edge-spike-mean-singleton-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-edge-spike-mean-singleton-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitIncrementEdgeSpikeSAEOrEndpointOrbitLongBoundedIncrementDriftPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：edge-spike 并不是新的独立非循环终端。它给出

```text
sigma*Y_j>=Lambda,
Y_j=X_j-mu.
```

因此：

```text
sigma*X_j-sigma*mu>=Lambda.
```

于是必然出现：

```text
sigma*X_j>=Lambda/2
```

或：

```text
-sigma*mu>=Lambda/2.
```

第一支是单点实际负载原子，第二支是整周期均值原子。故 edge-spike 被吸收到
endpoint singleton atom/SAE 或 full-cycle mean atom/SAE；long bounded drift 与
variation-boundary flux 仍是未闭合出口。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLongBoundedIncrementDriftPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、
long bounded-increment drift PDEC/cap、variation-boundary flux PDEC/cap 或
sparse SAE 求和；它只把独立 edge-spike 出口吸收到已有的单点/均值出口。

## 222. Stable-ladder endpoint orbit long-drift dyadic plateau frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_long_drift_dyadic_plateau_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-long-drift-dyadic-plateau-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-long-drift-dyadic-plateau-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-long-drift-dyadic-plateau-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLongBoundedIncrementDriftPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：long bounded drift 不是最后的匿名接口。它给出：

```text
0<Z_j<Lambda,  sum_{j in R}Z_j>=H.
```

按 dyadic 幅度层：

```text
A_l={j in R: 2^{-(l+1)}Lambda <= Z_j < 2^{-l}Lambda}.
```

若非空幅度层数超过预算 `D`，这是 amplitude-depth PDEC/cap；否则存在重层
`A_l` 承载至少 `H/D`。再将该重层按连续 plateau runs 分解。若 plateau
run 数超过 `B`，进入 variation-boundary flux；否则存在一个可比较幅度 plateau
run 满足：

```text
sum_{j in P_s}Z_j>=H/(D*B).
```

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitComparableAmplitudePlateauDriftPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、
comparable-amplitude plateau drift PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；它只把匿名 long bounded
drift 压成 dyadic plateau、amplitude-depth 或 boundary-flux 三分。

## 223. Stable-ladder endpoint orbit plateau-ramp frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_plateau_ramp_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-ramp-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-ramp-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-ramp-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitComparableAmplitudePlateauDriftPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：plateau drift 不再作为匿名出口保留。真实负载必须呈现为
同一连续弧、同一符号、同一 dyadic 幅度层：

```text
Z_j=sigma*Y_j>0,  a<=Z_j<2a,  sum_{j in P_s}Z_j>=H0.
```

长度预算 `L0` 给出二分。短 plateau 满足 `max Z_j>=H0/L0`，由已归档的
edge-spike 半阈值机制吸收到 singleton 或 full-cycle mean；长 plateau 则强制
prefix potential 在连续弧上单调爬升至少 `H0`，成为 plateau-ramp potential 包。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitPlateauRampPotentialPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、
plateau-ramp potential PDEC/cap、amplitude-depth PDEC/cap、variation-boundary
flux PDEC/cap 或 sparse SAE 求和；它只把匿名 comparable-amplitude plateau
drift 压成短原子吸收或长单调 ramp potential。

## 224. Stable-ladder endpoint orbit plateau-return mirror frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_plateau_return_mirror_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-return-mirror-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-return-mirror-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-return-mirror-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitPlateauRampPotentialPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：真实正向 ramp 不能只作为局部增长存在。由于中心化负载整周期总和为零，
任一正向 plateau-ramp：

```text
P consecutive,  Z_j=sigma*Y_j>0,  sum_{j in P}Z_j>=H0
```

都强制补弧支付同等负向 return mass：

```text
sum_{complement}(-sigma*Y_j)_+ >= H0.
```

对 return mass 作 dyadic/连续 run 分解后，若不是 amplitude-depth 或 boundary-flux，
则存在一个负向 return plateau，与原正向 ramp 构成 opposite-sign mirror pair。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitOppositeSignPlateauRampPairPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、
opposite-sign plateau-ramp pair PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；它只把匿名 plateau-ramp
potential 压成负向 return mirror、amplitude-depth 或 boundary-flux 三分。

## 225. Stable-ladder endpoint orbit plateau-pair phase frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_plateau_pair_phase_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-pair-phase-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-pair-phase-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-plateau-pair-phase-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitOppositeSignPlateauRampPairPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：正负 return mirror 不能只作为无相位标签的两团质量存在。
两个连续 plateau 弧在周期上决定实际相位间隔。给定 gap 预算 `E`，若两个弧近接，
则正负号在短桥上切换，登记为 boundary-flux；若不近接，则保留为真正相位分离的
bipolar plateau pair。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitPhaseSeparatedBipolarPlateauPairPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、
phase-separated bipolar plateau pair PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；它只把匿名 opposite-sign
plateau pair 压成近接边界或相位分离双极包。

## 226. Stable-ladder endpoint orbit bipolar-shelf frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_bipolar_shelf_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-bipolar-shelf-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-bipolar-shelf-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-bipolar-shelf-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitPhaseSeparatedBipolarPlateauPairPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：相位分离的正负 plateau pair 仍然必须解释桥段上的势能过渡。
在有向前缀势能

```text
S(t)=sum_{i<=t} sigma*Y_i
```

下，正 plateau 造成势能上升，负 plateau 造成势能回落。若桥段提前抵消半个高度，
这是 bridge-cancellation；若不抵消，则长桥段上存在高位或低位 shelf。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLongPotentialShelfPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、long potential
shelf PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；它只把匿名 phase-separated
bipolar pair 压成 bridge cancellation 或 long potential shelf。

## 227. Stable-ladder endpoint orbit long-potential-shelf static-bias frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_long_potential_shelf_static_bias_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-long-potential-shelf-static-bias-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-long-potential-shelf-static-bias-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-long-potential-shelf-static-bias-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLongPotentialShelfPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：long potential shelf 若真实存在，不能只是“长桥段上势能偏离”
这个匿名描述。令 `d_t=S(t+1)-S(t)`，它必须在 shelf 内提交一种可审计机制：
高振荡进入 variation-boundary flux，同号继续堆高进入 amplitude-depth，反向足量抵消进入
bridge-cancellation。否则剩余就是低波动、低漂移、低抵消的一侧静态势能偏置。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStaticPotentialShelfBiasPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、static potential
shelf bias PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；它只把匿名 long potential shelf
压成静态偏置包或已命名三出口。

## 228. Stable-ladder endpoint orbit static-shelf area-moment frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_static_shelf_area_moment_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-area-moment-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-area-moment-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-area-moment-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStaticPotentialShelfBiasPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：静态 shelf 不是只保留“偏置存在”的语义，而必须支付其矩形面积。
从 `sigma*S(t)>=H/2` 得到 `A(I)>=H|I|/2`。分部求和把该面积拆成端点收费与加权增量矩。
端点收费若足够大，已经是已有命名出口；若不够，则真实剩余为 static shelf area moment。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStaticShelfAreaMomentPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、static shelf area
moment PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；它只把匿名 static potential shelf
bias 压成面积矩包或已命名三出口。

## 229. Stable-ladder endpoint orbit static-shelf centroid-moment frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_static_shelf_centroid_moment_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-centroid-moment-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-centroid-moment-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-centroid-moment-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStaticShelfAreaMomentPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：面积矩若只在端点 collar 中支付，就不是新内部硬点；它回到
bridge/amplitude/boundary。若 collar 支付不了，就必须在远离端点的 interior core 中留下
固定比例的 weighted increment moment，并定义内部有向质心 `c_K`。这把“面积异常”压成更
窄的内部质心相位异常。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStaticShelfInteriorCentroidMomentPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、static shelf
interior centroid moment PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth
PDEC/cap、variation-boundary flux PDEC/cap 或 sparse SAE 求和；它只把匿名 static shelf
area moment 压成内部质心矩包或已命名三出口。

## 230. Stable-ladder endpoint orbit static-shelf centroid phase-lock frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_static_shelf_centroid_phase_lock_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-centroid-phase-lock-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-centroid-phase-lock-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-static-shelf-centroid-phase-lock-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStaticShelfInteriorCentroidMomentPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：内部质心矩不是一个可停留的匿名口径。把每个窗口的质心转成
`theta_j=(c_j-a_j)/L_j` 后，显著漂移会产生内部切线通量，反号同相会产生桥接抵消，同号同相
持续堆高会产生幅深负债。若这些可支付出口全部不足，剩余就被迫成为“稳定内部相位单元中的
长期锁定质量”。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStaticShelfInteriorCentroidPhaseLockPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、static shelf
interior centroid phase-lock PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth
PDEC/cap、variation-boundary flux PDEC/cap 或 sparse SAE 求和；它只把匿名 interior centroid
moment 压成内部质心相位锁定包或已命名三出口。

## 231. Stable-ladder endpoint orbit locked phase-cell pressure frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_locked_phase_cell_pressure_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-phase-cell-pressure-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-phase-cell-pressure-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-phase-cell-pressure-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitStaticShelfInteriorCentroidPhaseLockPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：phase-lock 不能只停在“相位长期锁住”这一语义层。相位单元、符号、
dyadic mass 档和 actual CRT residue word 组成有限槽位；若槽位不持久，则该分支是 sparse
SAE。若槽位持久，则得到实际 residue word，在 CRT cylinder 中形成固定列或窄列族压力。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLockedInteriorPhaseCellColumnPressurePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、locked interior
phase-cell column pressure PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth
PDEC/cap、variation-boundary flux PDEC/cap 或 sparse SAE 求和；它只把匿名 interior centroid
phase-lock 压成 locked column pressure 包或 sparse/atom/mean/三出口。

## 232. Stable-ladder endpoint orbit locked-column capacity frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_locked_column_capacity_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-column-capacity-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-column-capacity-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-column-capacity-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLockedInteriorPhaseCellColumnPressurePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：固定列压力必须面对实际 CRT 纤维容量。令 `L(C)` 为固定列或窄列族
承载的 signed load，`Q(C)` 为局部 CRT 允许类数给出的容量。未超额时它不能支付强制质量，只能
回到均值、原子、稀疏或已命名三出口；超额时才是真正列容量缺陷。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLockedColumnCapacityDefectPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、locked column
capacity defect PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；它只把匿名 locked column pressure 压成
capacity defect 包或 mean/singleton/sparse/三出口。

## 233. Stable-ladder endpoint orbit locked-column residue-shadow frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_locked_column_residue_shadow_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-column-residue-shadow-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-column-residue-shadow-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-locked-column-residue-shadow-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLockedColumnCapacityDefectPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：列容量缺陷必须显现在某个 CRT residue shadow。若每个 shadow 都不
超额，则 shadow quota 的可加性会推出整列族不超额。于是剩余不再是整体列容量语义，而是一个
可定位的 overfull residue shadow；它的孤立、均值、反号、堆高、迁移部分仍回流已有出口。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLockedColumnResidueShadowImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、locked column
residue-shadow imbalance PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；它只把匿名 locked column capacity defect
压成 residue-shadow imbalance 包或 mean/singleton/sparse/三出口。

## 234. Stable-ladder endpoint orbit residue-shadow dual-row frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitLockedColumnResidueShadowImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：locked column residue-shadow imbalance 是列方向的局部超额，
但 CRT 对偶把每个 column residue shadow `s` 投影为 dual-row shadow `R_s`，并保留
signed excess：

```text
s -> R_s
E(R_s)=E(C_s).
```

若 `R_s` 没有真实行压力，则列 shadow excess 在行纤维平均中被吸收，回流
full-cycle mean、singleton、sparse 或 bridge/amplitude/boundary 出口。若平均不能吸收，
剩余不再是匿名列 shadow，而是显式 residue-shadow dual-row pressure PDEC/cap。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPressurePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、residue-shadow
dual-row pressure PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；它只把匿名 locked column
residue-shadow imbalance 压成 dual-row pressure 包或 mean/singleton/sparse/三出口。

## 235. Stable-ladder endpoint orbit residue-shadow dual-row capacity frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_capacity_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-capacity-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-capacity-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-capacity-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPressurePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：residue-shadow dual-row pressure 不能停在“对偶行有压力”的语义层。
固定对偶行窗口 `R` 后，实际 signed load 与 CRT 行纤维容量为：

```text
H(R)=sum_{omega projects to R} signed_mass(omega)
B(R)=local_CRT_allowed_row_fiber_count(R)*scale_weight.
```

若 `|H(R)|<=B(R)`，该窗口没有超出允许纤维容量，不能支付上一层强制压力，必须回到
mean、singleton、sparse 或 bridge/amplitude/boundary。若 `|H(R)|>B(R)`，才是实际
dual-row capacity defect。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowCapacityDefectPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、residue-shadow
dual-row capacity defect PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth
PDEC/cap、variation-boundary flux PDEC/cap 或 sparse SAE 求和；它只把匿名 residue-shadow
dual-row pressure 压成 capacity defect 包或 mean/singleton/sparse/三出口。

## 236. Stable-ladder endpoint orbit residue-shadow dual-row phase-cell frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_phase_cell_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowCapacityDefectPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：dual-row capacity defect 不能停在整块窗口超额的层面。对偶行
窗口 `R` 仍有 CRT phase-cell 坐标，且 signed load 与 quota 可逐 cell 分解：

```text
H(R)=sum_theta H_theta
B(R)=sum_theta B_theta
```

若整个窗口满足 `|H(R)|>B(R)`，则在固定符号选择下必有某个 phase-cell 满足
`|H_theta|>B_theta`；否则逐 cell 加总会推出窗口不超额。该 overfull cell 的孤立、
整周期均值、反号互付、同号堆高或边界迁移分别回到 singleton、full-cycle mean、
bridge、amplitude、boundary 或 sparse 出口。若这些命名出口都不能支付，剩余就是实际
residue-shadow dual-row phase-cell imbalance PDEC/cap。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、residue-shadow
dual-row phase-cell imbalance PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth
PDEC/cap、variation-boundary flux PDEC/cap 或 sparse SAE 求和；它只把匿名 residue-shadow
dual-row capacity defect 压成 phase-cell imbalance 包或 mean/singleton/sparse/三出口。

## 237. Stable-ladder endpoint orbit residue-shadow dual-row phase-cell atom frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：phase-cell imbalance 仍不是最小实际承载单位。固定 overfull
phase-cell `theta` 后，内部还可按 residue/source atom `a` 分解：

```text
H_theta=sum_a h_{theta,a}
B_theta=sum_a b_{theta,a}
```

若 `|H_theta|>B_theta`，令 `sigma=sign(H_theta)`。如果每个 atom 都满足
`sigma*h_{theta,a}<=b_{theta,a}`，则加总会推出 `|H_theta|<=B_theta`，与 overfull cell
矛盾。因此某个同号 atom 已超过自身 quota。这个 atom 若由 singleton、full-cycle mean、
opposite-sign bridge、same-sign amplitude stack、boundary flux 或 sparse SAE 支付，则回流
已有出口；若不能支付，剩余就是实际 residue-shadow dual-row phase-cell atom imbalance
PDEC/cap。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、residue-shadow
dual-row phase-cell atom imbalance PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth
PDEC/cap、variation-boundary flux PDEC/cap 或 sparse SAE 求和；它只把匿名 residue-shadow
dual-row phase-cell imbalance 压成 atom imbalance 包或 mean/singleton/sparse/三出口。

## 238. Stable-ladder endpoint orbit residue-shadow dual-row phase-cell atom signed-core frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：atom imbalance 仍可能把反号抵消和同号核心混在一起。固定
`sigma=sign(h_a)`，写：

```text
sigma*h_a=C_plus-C_minus
sigma*h_a>b_a
```

于是同号核心满足：

```text
C_plus>b_a+C_minus
```

若反号抵消 `C_minus` 是实质互付，则回到 bridge-cancellation；若不是，则 atom 的剩余压力
已经是同号核心超过 quota 加抵消债的 signed-core imbalance。该核心若由 singleton、
full-cycle mean、amplitude-depth、boundary flux 或 sparse SAE 支付，则回流已有出口；否则
留下实际 residue-shadow dual-row phase-cell atom signed-core imbalance PDEC/cap。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、residue-shadow
dual-row phase-cell atom signed-core imbalance PDEC/cap、bridge-cancellation PDEC/cap、
amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap 或 sparse SAE 求和；它只把匿名
residue-shadow dual-row phase-cell atom imbalance 压成 signed-core imbalance 包或
mean/singleton/sparse/三出口。

## 239. Stable-ladder endpoint orbit residue-shadow dual-row phase-cell atom signed-core support-slice frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：signed-core imbalance 仍需落到具体实际支撑槽，而不能停在核心总量。
从

```text
C_plus>b_a+C_minus
```

同步分解到有限 support slice：

```text
C_plus=sum_s C_s
b_a+C_minus=sum_s d_s
```

若所有槽都满足 `C_s<=d_s`，则总量不可能超额；所以必有某个 `s` 满足 `C_s>d_s`。
该槽若由 singleton、full-cycle mean、bridge、amplitude-depth、boundary flux 或 sparse SAE
支付，则回流已有出口；否则留下实际 support-slice imbalance PDEC/cap。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、support-slice
imbalance PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；它只把匿名 signed-core imbalance 压成
support-slice imbalance 包或 mean/singleton/sparse/三出口。

## 240. Stable-ladder endpoint orbit residue-shadow dual-row phase-cell atom signed-core support-slice residue-fiber frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：support-slice imbalance 仍可能把多个实际 CRT residue fiber 混在一个
槽内。已知

```text
C_s>d_s
```

同步分解到实际 residue fiber：

```text
C_s=sum_rho C_{s,rho}
d_s=sum_rho d_{s,rho}
```

若所有 fiber 都满足 `C_{s,rho}<=d_{s,rho}`，则总槽不可能超额；所以必有某个 `rho`
满足 `C_{s,rho}>d_{s,rho}`。该 fiber 若由 singleton、full-cycle mean、bridge、
amplitude-depth、boundary flux 或 sparse SAE 支付，则回流已有出口；否则留下实际
residue-fiber imbalance PDEC/cap。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、residue-fiber
imbalance PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；它只把匿名 support-slice imbalance
压成 residue-fiber imbalance 包或 mean/singleton/sparse/三出口。

## 241. Stable-ladder endpoint orbit residue-shadow dual-row phase-cell atom signed-core support-slice residue-fiber phase-word frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：residue-fiber imbalance 仍可能把多个实际 CRT phase word 混在一个
fiber 内。已知

```text
C_{s,rho}>d_{s,rho}
```

同步分解到有限 phase word：

```text
C_{s,rho}=sum_omega C_{s,rho,omega}
d_{s,rho}=sum_omega d_{s,rho,omega}
```

若所有 phase word 都满足 `C_{s,rho,omega}<=d_{s,rho,omega}`，则该 fiber 不可能超额；
所以必有某个 `omega` 满足 `C_{s,rho,omega}>d_{s,rho,omega}`。该 phase word 若由
singleton、full-cycle mean、bridge、amplitude-depth、boundary flux 或 sparse SAE 支付，
则回流已有出口；否则留下实际 phase-word imbalance PDEC/cap。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、phase-word
imbalance PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；它只把匿名 residue-fiber imbalance
压成 phase-word imbalance 包或 mean/singleton/sparse/三出口。

## 242. Stable-ladder endpoint orbit residue-shadow dual-row phase-cell atom signed-core support-slice residue-fiber phase-word-slot frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：phase-word imbalance 仍可能把多个实际 CRT word slot 混在一个
phase word 内。已知

```text
C_{s,rho,omega}>d_{s,rho,omega}
```

同步分解到有限 word slot：

```text
C_{s,rho,omega}=sum_tau C_{s,rho,omega,tau}
d_{s,rho,omega}=sum_tau d_{s,rho,omega,tau}
```

若所有 word slot 都满足 `C_{s,rho,omega,tau}<=d_{s,rho,omega,tau}`，则该 phase word
不可能超额；所以必有某个 `tau` 满足
`C_{s,rho,omega,tau}>d_{s,rho,omega,tau}`。该 word slot 若由 singleton、full-cycle
mean、bridge、amplitude-depth、boundary flux 或 sparse SAE 支付，则回流已有出口；
否则留下实际 phase-word-slot imbalance PDEC/cap。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、phase-word-slot
imbalance PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；它只把匿名 phase-word imbalance
压成 phase-word-slot imbalance 包或 mean/singleton/sparse/三出口。

## 243. Stable-ladder endpoint orbit residue-shadow dual-row phase-cell atom signed-core support-slice residue-fiber phase-word-slot source-atom frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：phase-word-slot imbalance 仍可能把多个实际 source atom 混在一个
word slot 内。已知

```text
C_{s,rho,omega,tau}>d_{s,rho,omega,tau}
```

同步分解到有限 endpoint/source atom：

```text
C_{s,rho,omega,tau}=sum_alpha C_{s,rho,omega,tau,alpha}
d_{s,rho,omega,tau}=sum_alpha d_{s,rho,omega,tau,alpha}
```

若所有 source atom 都满足 `C_{s,rho,omega,tau,alpha}<=d_{s,rho,omega,tau,alpha}`，
则该 word slot 不可能超额；所以必有某个 `alpha` 满足
`C_{s,rho,omega,tau,alpha}>d_{s,rho,omega,tau,alpha}`。该 source atom 若由 singleton、
full-cycle mean、bridge、amplitude-depth、boundary flux 或 sparse SAE 支付，则回流已有出口；
否则留下实际 phase-word-slot source-atom imbalance PDEC/cap。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、phase-word-slot
source-atom imbalance PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；它只把匿名 phase-word-slot imbalance
压成 source-atom imbalance 包或 mean/singleton/sparse/三出口。

## 244. Stable-ladder endpoint orbit residue-shadow dual-row phase-cell atom signed-core support-slice residue-fiber phase-word-slot source-atom multiplicity-fiber frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：source-atom imbalance 仍可能把同一 source atom 内多个实际出现
或同 key/fiber 的重数混在一起。已知

```text
C_{s,rho,omega,tau,alpha}>d_{s,rho,omega,tau,alpha}
```

若同一 `alpha` 的出现重数超过局部 cap，则它是 source-atom multiplicity-cap PDEC/cap。
否则同步分解到有限 multiplicity fiber：

```text
C_{s,rho,omega,tau,alpha}=sum_mu C_{s,rho,omega,tau,alpha,mu}
d_{s,rho,omega,tau,alpha}=sum_mu d_{s,rho,omega,tau,alpha,mu}
```

若所有 fiber 都满足 `C_{s,rho,omega,tau,alpha,mu}<=d_{s,rho,omega,tau,alpha,mu}`，
则该 source atom 不可能超额；所以必有某个 `mu` 满足
`C_{s,rho,omega,tau,alpha,mu}>d_{s,rho,omega,tau,alpha,mu}`。该 fiber 若由 singleton、
full-cycle mean、bridge、amplitude-depth、boundary flux 或 sparse SAE 支付，则回流已有出口；
否则留下实际 source-atom multiplicity-fiber imbalance PDEC/cap。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、source-atom multiplicity-fiber imbalance PDEC/cap、
bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap
或 sparse SAE 求和；它只把匿名 source-atom imbalance 压成 multiplicity-cap、
multiplicity-fiber imbalance 包或 mean/singleton/sparse/三出口。

## 245. Stable-ladder endpoint orbit residue-shadow dual-row phase-cell atom signed-core support-slice residue-fiber phase-word-slot source-atom multiplicity-fiber signed-unit frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_unit_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-signed-unit-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-signed-unit-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-signed-unit-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：multiplicity-fiber imbalance 仍可能把同一 fiber 内多个实际
signed occurrence/load unit 混在一起。已知

```text
C_{s,rho,omega,tau,alpha,mu}>d_{s,rho,omega,tau,alpha,mu}
```

同步分解到有限 signed occurrence unit：

```text
C_{s,rho,omega,tau,alpha,mu}=sum_eta C_{s,rho,omega,tau,alpha,mu,eta}
d_{s,rho,omega,tau,alpha,mu}=sum_eta d_{s,rho,omega,tau,alpha,mu,eta}
```

若所有 `eta` 都满足
`C_{s,rho,omega,tau,alpha,mu,eta}<=d_{s,rho,omega,tau,alpha,mu,eta}`，
则该 fiber 不可能超额；所以必有某个 `eta` 满足
`C_{s,rho,omega,tau,alpha,mu,eta}>d_{s,rho,omega,tau,alpha,mu,eta}`。source-atom
multiplicity-cap PDEC/cap 不在本步证明，继续作为并行出口。该 signed unit 若由
singleton、full-cycle mean、bridge、amplitude-depth、boundary flux 或 sparse SAE 支付，
则回流已有出口；否则留下实际 signed occurrence unit imbalance PDEC/cap。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、signed occurrence unit imbalance PDEC/cap、bridge-cancellation
PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap 或 sparse SAE 求和；
它只把匿名 multiplicity-fiber imbalance 压成 signed occurrence unit imbalance 包或
mean/singleton/sparse/三出口。

## 246. Stable-ladder endpoint orbit residue-shadow dual-row phase-cell atom signed-core support-slice residue-fiber phase-word-slot source-atom multiplicity-fiber signed-unit incidence-cell frontier

新增文件

```text
experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_fiber_signed_unit_incidence_cell_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-signed-unit-incidence-cell-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-signed-unit-incidence-cell-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-signed-unit-incidence-cell-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：signed occurrence unit imbalance 仍可能把同一带符号命中单位内多个
实际 incidence cells 混在一起。已知

```text
C_{s,rho,omega,tau,alpha,mu,eta}>d_{s,rho,omega,tau,alpha,mu,eta}
```

同步分解到有限 incidence cell：

```text
C_{s,rho,omega,tau,alpha,mu,eta}=sum_iota C_{s,rho,omega,tau,alpha,mu,eta,iota}
d_{s,rho,omega,tau,alpha,mu,eta}=sum_iota d_{s,rho,omega,tau,alpha,mu,eta,iota}
```

若所有 `iota` 都满足
`C_{s,rho,omega,tau,alpha,mu,eta,iota}<=d_{s,rho,omega,tau,alpha,mu,eta,iota}`，
则该 signed occurrence unit 不可能超额；所以必有某个 `iota` 满足
`C_{s,rho,omega,tau,alpha,mu,eta,iota}>d_{s,rho,omega,tau,alpha,mu,eta,iota}`。
source-atom multiplicity-cap PDEC/cap 不在本步证明，继续作为并行出口。该 incidence
cell 若由 singleton、full-cycle mean、bridge、amplitude-depth、boundary flux 或 sparse
SAE 支付，则回流已有出口；否则留下实际 incidence-cell imbalance PDEC/cap。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、incidence-cell imbalance PDEC/cap、bridge-cancellation
PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap 或 sparse SAE 求和；
它只把匿名 signed occurrence unit imbalance 压成 incidence-cell imbalance 包或
mean/singleton/sparse/三出口。

## 247. Stable-ladder endpoint orbit residue-shadow dual-row phase-cell atom signed-core support-slice residue-fiber phase-word-slot source-atom multiplicity-fiber signed-unit incidence-cell primitive-witness frontier

新增文件

```text
experiments/prime_matrix_signed_unit_incidence_cell_primitive_witness_router.py
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-signed-unit-incidence-cell-primitive-witness-router.md
docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-signed-unit-incidence-cell-primitive-witness-router.json
data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-residue-shadow-dual-row-phase-cell-atom-signed-core-support-slice-residue-fiber-phase-word-slot-source-atom-multiplicity-fiber-signed-unit-incidence-cell-primitive-witness-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：incidence-cell imbalance 仍可能把同一实际格点内多个行列/载体素数/同余代表见证混在一起。已知

```text
C_{s,rho,omega,tau,alpha,mu,eta,iota}>d_{s,rho,omega,tau,alpha,mu,eta,iota}
```

同步分解到有限 primitive witness：

```text
C_{s,rho,omega,tau,alpha,mu,eta,iota}=sum_kappa C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa}
d_{s,rho,omega,tau,alpha,mu,eta,iota}=sum_kappa d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa}
kappa=(row,column,carrier_prime,residue_representative,endpoint_side,orientation)
```

若所有 `kappa` 都满足
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

## 248. Stable-ladder primitive-witness CRT-coordinate-atom frontier

新增文件

```text
experiments/prime_matrix_primitive_witness_crt_coordinate_atom_router.py
docs/monograph/prime-matrix-primitive-witness-crt-coordinate-atom-router.md
docs/monograph/prime-matrix-primitive-witness-crt-coordinate-atom-router.json
data/prime-matrix-primitive-witness-crt-coordinate-atom-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：primitive-witness imbalance 仍可能把同一行列见证内多个等价的 CRT
坐标命中混在一起。已知

```text
C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa}>d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa}
```

同步分解到有限 CRT coordinate atom：

```text
C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa}=sum_chi C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi}
d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa}=sum_chi d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi}
chi=(row,column,carrier_prime q,residue a,endpoint_side,orientation,N_{row,column,side} == a mod q)
```

若所有 `chi` 都满足
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

## 249. Stable-ladder CRT-coordinate canonical-equation frontier

新增文件

```text
experiments/prime_matrix_crt_coordinate_canonical_equation_router.py
docs/monograph/prime-matrix-crt-coordinate-canonical-equation-router.md
docs/monograph/prime-matrix-crt-coordinate-canonical-equation-router.json
data/prime-matrix-crt-coordinate-canonical-equation-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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
crt_coordinate_canonical_congruence_equation_atom_imbalance_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：CRT coordinate atom 仍可能把同一同余方程的不同写法混在一起。已知

```text
C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi}>d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi}
```

同步分解到有限 canonical congruence equation atom：

```text
epsilon=(equation_id,normal_form,row,column,carrier_prime q,residue a,endpoint_side,orientation,phase_boundary_key)
C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi}=sum_epsilon C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon}
d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi}=sum_epsilon d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon}
```

若所有 `epsilon` 都满足
`C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon}<=d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon}`，
则该 coordinate atom 不可能超额；所以必有某个 `epsilon` 满足
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

## 250. Stable-ladder canonical-equation phase-residue-evaluation frontier

新增文件

```text
experiments/prime_matrix_canonical_equation_phase_residue_evaluation_router.py
docs/monograph/prime-matrix-canonical-equation-phase-residue-evaluation-router.md
docs/monograph/prime-matrix-canonical-equation-phase-residue-evaluation-router.json
data/prime-matrix-canonical-equation-phase-residue-evaluation-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

```text
canonical_congruence_equation_atom_imbalance_imported=true
canonical_equation_phase_residue_evaluation_atom_model_closed=true
canonical_equation_row_phase_closed=true
canonical_equation_column_phase_closed=true
canonical_equation_carrier_residue_evaluation_closed=true
canonical_equation_phase_residue_evaluation_id_stability_closed=true
canonical_equation_phase_residue_evaluation_atom_pigeonhole_closed=true
phase_residue_evaluation_atom_imbalance_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：canonical equation atom 仍可能没有显式固定实际 CRT 相位评价。已知

```text
C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon}>d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon}
```

同步分解到有限 phase-residue evaluation atom：

```text
zeta=(evaluation_id,equation_id,q,a,row mod q,column mod q,N_{row,column,side} mod q,endpoint_side,orientation,phase_boundary_key)
C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon}=sum_zeta C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon,zeta}
d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon}=sum_zeta d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon,zeta}
```

若所有 `zeta` 都满足 `C_{...,epsilon,zeta}<=d_{...,epsilon,zeta}`，则该 canonical
equation atom 不可能超额；所以必有某个 `zeta` 满足
`C_{...,epsilon,zeta}>d_{...,epsilon,zeta}`。source-atom multiplicity-cap PDEC/cap
不在本步证明，继续作为并行出口。该 phase-residue atom 若由 singleton、full-cycle mean、
bridge、amplitude-depth、boundary flux 或 sparse SAE 支付，则回流已有出口；否则留下实际
phase-residue-evaluation atom imbalance PDEC/cap。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue-evaluation atom imbalance PDEC/cap、
bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux
PDEC/cap 或 sparse SAE 求和；它只把匿名 canonical equation atom imbalance 压成
phase-residue-evaluation imbalance 包或 mean/singleton/sparse/三出口。

## 251. Stable-ladder phase-residue Hall-defect frontier

新增文件

```text
experiments/prime_matrix_phase_residue_hall_defect_router.py
docs/monograph/prime-matrix-phase-residue-hall-defect-router.md
docs/monograph/prime-matrix-phase-residue-hall-defect-router.json
data/prime-matrix-phase-residue-hall-defect-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomImbalancePDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

```text
phase_residue_evaluation_atom_imbalance_imported=true
phase_residue_load_token_ledger_closed=true
phase_residue_quota_debt_slot_ledger_closed=true
phase_residue_payment_graph_closed=true
phase_residue_hall_defect_normal_form_closed=true
phase_residue_hall_defect_pigeonhole_closed=true
phase_residue_hall_defect_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：phase-residue atom 的超额仍可能只以 `C>d` 形式出现，而没有显式
供需缺陷子集。已知

```text
C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon,zeta}>d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon,zeta}
```

同步展开为有限 Hall 图：

```text
G_zeta=(L_zeta,D_zeta,E_zeta)
C_{...,zeta}=|L_zeta|, d_{...,zeta}=|D_zeta|
edges preserve evaluation_id, side, orientation, and phase_boundary_key
```

若所有 `S subset L_zeta` 都满足 `|S|<=|N_G(S)|`，Hall 定理给出全匹配，从而
`C_{...,zeta}<=d_{...,zeta}`。因此必有某个 `S` 满足
`|S|>|N_G(S)|`，缺陷量为 `Delta_H(S)=|S|-|N_G(S)|>0`。source-atom
multiplicity-cap PDEC/cap 不在本步证明，继续作为并行出口。该 Hall defect 若由 singleton、
full-cycle mean、bridge、amplitude-depth、boundary flux 或 sparse SAE 支付，则回流已有出口；
否则留下实际 phase-residue Hall-defect PDEC/cap。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomHallDefectPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue Hall-defect PDEC/cap、bridge-cancellation
PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap 或 sparse SAE
求和；它只把匿名 phase-residue C>d 压成 Hall 供需缺陷包或 mean/singleton/sparse/三出口。

## 252. Stable-ladder phase-residue critical-Hall-cut frontier

新增文件

```text
experiments/prime_matrix_phase_residue_critical_hall_cut_router.py
docs/monograph/prime-matrix-phase-residue-critical-hall-cut-router.md
docs/monograph/prime-matrix-phase-residue-critical-hall-cut-router.json
data/prime-matrix-phase-residue-critical-hall-cut-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomHallDefectPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

```text
phase_residue_hall_defect_imported=true
phase_residue_hall_defect_finite_family_closed=true
phase_residue_hall_defect_minimal_choice_closed=true
phase_residue_hall_defect_connected_core_closed=true
phase_residue_hall_defect_proper_subset_hall_ok_closed=true
phase_residue_critical_hall_cut_boundary_closed=true
phase_residue_critical_hall_cut_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：Hall defect 仍可能只是任意失败子集。现在把它规范化为临界 cut：

```text
F={S subset L_zeta: |S|>|N_G(S)|}
S_*=argmin_{S in F} (|S|,-Delta_H(S),stable_hash(S))
B_*=N_G(S_*)
Delta_*=|S_*|-|B_*|>0
for every proper T subset S_*: |T|<=|N_G(T)|
```

若 `S_*` 不连通，则某个连通分量仍有正缺陷，违反 `|S_*|` 最小性。因此可以把剩余压成连通、
不可再分、边界明确的 phase-residue critical-Hall-cut。source-atom multiplicity-cap PDEC/cap
不在本步证明，继续作为并行出口。该 critical cut 若由 singleton、full-cycle mean、bridge、
amplitude-depth、boundary flux 或 sparse SAE 支付，则回流已有出口；否则留下实际
critical-Hall-cut PDEC/cap。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomCriticalHallCutPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue critical-Hall-cut PDEC/cap、bridge-cancellation
PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap 或 sparse SAE
求和；它只把任意 Hall defect 压成 critical cut 包或 mean/singleton/sparse/三出口。

## 253. Stable-ladder phase-residue unit-defect critical-cut frontier

新增文件

```text
experiments/prime_matrix_phase_residue_unit_defect_critical_cut_router.py
docs/monograph/prime-matrix-phase-residue-unit-defect-critical-cut-router.md
docs/monograph/prime-matrix-phase-residue-unit-defect-critical-cut-router.json
data/prime-matrix-phase-residue-unit-defect-critical-cut-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomCriticalHallCutPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

```text
phase_residue_critical_hall_cut_imported=true
phase_residue_critical_hall_cut_unit_margin_closed=true
phase_residue_critical_hall_cut_single_deletion_boundary_saturation_closed=true
multi_unit_phase_residue_critical_hall_cut_defect_excluded=true
phase_residue_unit_defect_critical_hall_cut_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：critical cut 的真子集 Hall 正常性不仅给出“不可再分”，还直接强制
容量缺口为单位。若 `|S_*|=1`，正缺陷只可能是 `B_*=empty`、`Delta_*=1`。若
`|S_*|>=2`，对任意 `s in S_*`：

```text
|S_*|-1 <= |N_G(S_*\{s})| <= |B_*| = |S_*|-Delta_*
```

所以 `Delta_*=1`，且

```text
N_G(S_*\{s})=B_*
```

即删除任一源点后，边界支付槽仍全部可见。由此，critical cut 不能再携带多单位总量型反例；
若反例链继续存在，必须是单位缺口 critical-Hall-cut 加上边界冗余相位刚性，或回流 singleton、
full-cycle mean、multiplicity cap、bridge、amplitude、boundary flux、sparse SAE 等已有出口。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomUnitDefectCriticalHallCutPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue unit-defect critical-Hall-cut PDEC/cap、
bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap
或 sparse SAE 求和；它只把 critical-Hall-cut 压成单位缺口包或 mean/singleton/sparse/三出口。

## 254. Stable-ladder phase-residue near-perfect matching circuit frontier

新增文件

```text
experiments/prime_matrix_phase_residue_near_perfect_matching_circuit_router.py
docs/monograph/prime-matrix-phase-residue-near-perfect-matching-circuit-router.md
docs/monograph/prime-matrix-phase-residue-near-perfect-matching-circuit-router.json
data/prime-matrix-phase-residue-near-perfect-matching-circuit-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomUnitDefectCriticalHallCutPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

```text
phase_residue_unit_defect_critical_hall_cut_imported=true
phase_residue_every_single_deletion_perfect_matching_closed=true
phase_residue_critical_cut_maximum_matching_size_closed=true
phase_residue_boundary_double_cover_closed=true
phase_residue_near_perfect_matching_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：单位缺口 cut 不是单纯的一个未支付容量槽，而是一个匹配 circuit。
对每个 `s in S_*`，所有 `U subset S_*\{s}` 都继承真子集 Hall 正常性，并且 `|S_*\{s}|=|B_*|`，
所以 Hall 定理给出完美匹配：

```text
M_s:S_*\{s}->B_*
```

这说明每个源点都可被选择为唯一未匹配源点，全部边界仍可支付；同时每个边界槽至少有两个源点支撑。
因此若反例链继续存在，它必须在“所有单点删除可支付、整体多一个源点”的 near-perfect matching
circuit 中产生真实相位矛盾，或回流 singleton、full-cycle mean、multiplicity cap、bridge、
amplitude、boundary flux、sparse SAE 等已有出口。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomNearPerfectMatchingCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue near-perfect matching circuit PDEC/cap、
bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap
或 sparse SAE 求和；它只把 unit-defect critical cut 压成近完美匹配 circuit 或 mean/singleton/sparse/三出口。

## 255. Stable-ladder phase-residue alternating exchange circuit frontier

新增文件

```text
experiments/prime_matrix_phase_residue_alternating_exchange_circuit_router.py
docs/monograph/prime-matrix-phase-residue-alternating-exchange-circuit-router.md
docs/monograph/prime-matrix-phase-residue-alternating-exchange-circuit-router.json
data/prime-matrix-phase-residue-alternating-exchange-circuit-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomNearPerfectMatchingCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

```text
phase_residue_near_perfect_matching_circuit_imported=true
phase_residue_matching_symmetric_difference_graph_closed=true
phase_residue_unique_source_defect_alternating_path_closed=true
phase_residue_every_source_exchange_reachable_closed=true
phase_residue_alternating_exchange_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：近完美匹配 circuit 不是一族互不相关的删除匹配。固定基准缺失源点
`s0` 与匹配 `M0=M_{s0}`。对任意 `s!=s0`，删除匹配 `M_s` 与 `M0` 的对称差
`H_s=M0 Δ M_s` 中，边界侧度数只能为 `0` 或 `2`，源点侧除 `s` 与 `s0` 外度数也只能为
`0` 或 `2`；唯一奇端点为 `s` 与 `s0`。所以 `H_s` 必含端点为二者的交替路径，并可能附加若干交替偶圈。

因此若反例链继续存在，它必须在“所有源点都沿交替路径交换可达到同一基准缺失源点”的
alternating exchange circuit 中产生真实相位矛盾，或回流 singleton、full-cycle mean、
multiplicity cap、bridge、amplitude、boundary flux、sparse SAE 等已有出口。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomAlternatingExchangeCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue alternating exchange circuit PDEC/cap、
bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap
或 sparse SAE 求和；它只把 near-perfect matching circuit 压成交替交换 circuit 或 mean/singleton/sparse/三出口。

## 256. Stable-ladder phase-residue rooted directed exchange path frontier

新增文件

```text
experiments/prime_matrix_phase_residue_rooted_directed_exchange_path_router.py
docs/monograph/prime-matrix-phase-residue-rooted-directed-exchange-path-router.md
docs/monograph/prime-matrix-phase-residue-rooted-directed-exchange-path-router.json
data/prime-matrix-phase-residue-rooted-directed-exchange-path-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomAlternatingExchangeCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

```text
phase_residue_alternating_exchange_circuit_imported=true
phase_residue_exchange_path_m0_ms_edge_coloring_closed=true
phase_residue_exchange_path_root_orientation_closed=true
phase_residue_every_source_root_reachable_by_directed_exchange_closed=true
phase_residue_rooted_directed_exchange_path_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：交替交换 circuit 不是无方向图。每条 `P_s` 都有由 `M0` 与 `M_s`
给出的边色，并可按 `M0-only: source->boundary`、`M_s-only: boundary->source` 定向。
这样，每个源点 `s` 都沿一条简单根向有向交替路径到达同一个基准缺失源点 `s0`。
沿该路径作对称差切换，正好给出 `M0` 与 `M_s` 在路径分量上的状态转换。

因此若反例链继续存在，它必须在带根、带边色、带方向和切换规则的 rooted directed exchange path
circuit 中产生真实相位矛盾，或回流 singleton、full-cycle mean、multiplicity cap、bridge、
amplitude、boundary flux、sparse SAE 等已有出口。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomRootedDirectedExchangePathCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue rooted directed exchange path circuit PDEC/cap、
bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap
或 sparse SAE 求和；它只把 alternating exchange circuit 压成根向有向交换路径 circuit 或 mean/singleton/sparse/三出口。

## 257. Stable-ladder phase-residue exchange toggle word frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_toggle_word_router.py
docs/monograph/prime-matrix-phase-residue-exchange-toggle-word-router.md
docs/monograph/prime-matrix-phase-residue-exchange-toggle-word-router.json
data/prime-matrix-phase-residue-exchange-toggle-word-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomRootedDirectedExchangePathCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

```text
phase_residue_rooted_directed_exchange_path_imported=true
phase_residue_alternating_vertex_word_normal_form_closed=true
phase_residue_exchange_word_boundary_distinctness_closed=true
phase_residue_no_internal_boundary_reuse_in_toggle_word_closed=true
phase_residue_exchange_toggle_word_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：根向有向交换路径不再作为匿名路径保留。任意简单路径都写成
`P_s=(u_0=s,b_1,u_1,...,b_r,u_r=s0)`。简单性强制词内源点与边界槽分别互异，特别是边界槽不能在同一条交换词中内部复用。每个二步片段 `u_{i-1}->b_i->u_i` 是局部 pivot，将 `M0` 边替换为 `M_s` 边；整条切换是这些 pivot 的有序有限乘积。

因此若反例链继续存在，它必须在“边界不复用的有限 exchange toggle word circuit”中产生真实相位矛盾，或回流 singleton、full-cycle mean、multiplicity cap、bridge、amplitude、boundary flux、sparse SAE 等已有出口。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeToggleWordCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange toggle word circuit PDEC/cap、
bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap
或 sparse SAE 求和；它只把 rooted directed exchange path circuit 压成 exchange toggle word
circuit 或 mean/singleton/sparse/三出口。

## 258. Stable-ladder phase-residue exchange prefix defect ladder frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_prefix_defect_ladder_router.py
docs/monograph/prime-matrix-phase-residue-exchange-prefix-defect-ladder-router.md
docs/monograph/prime-matrix-phase-residue-exchange-prefix-defect-ladder-router.json
data/prime-matrix-phase-residue-exchange-prefix-defect-ladder-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeToggleWordCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

```text
phase_residue_exchange_toggle_word_imported=true
phase_residue_exchange_prefix_unit_defect_identity_closed=true
phase_residue_exchange_prefix_nested_ladder_closed=true
phase_residue_exchange_prefix_toggle_state_transport_closed=true
phase_residue_exchange_prefix_defect_ladder_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：切换词不是无序 pivot 列表。对每个前缀
`U_t={u_0,...,u_t}`、`B_t={b_1,...,b_t}`，简单性强制 `|U_t|-|B_t|=1`。这些前缀按 `t` 嵌套，边界侧每一步只新增一个未复用槽，前缀切换把缺失源状态从 `u_0` 输运到 `u_t`。

因此若反例链继续存在，它必须在“嵌套前缀单位缺口 ladder”中产生真实容量/相位矛盾，或回流 singleton、full-cycle mean、multiplicity cap、bridge、amplitude、boundary flux、sparse SAE 等已有出口。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangePrefixDefectLadderCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange prefix defect ladder circuit PDEC/cap、
bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap
或 sparse SAE 求和；它只把 exchange toggle word circuit 压成 exchange prefix defect ladder
circuit 或 mean/singleton/sparse/三出口。

## 259. Stable-ladder phase-residue exchange endpoint telescoping charge frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_endpoint_telescoping_charge_router.py
docs/monograph/prime-matrix-phase-residue-exchange-endpoint-telescoping-charge-router.md
docs/monograph/prime-matrix-phase-residue-exchange-endpoint-telescoping-charge-router.json
data/prime-matrix-phase-residue-exchange-endpoint-telescoping-charge-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangePrefixDefectLadderCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

```text
phase_residue_exchange_prefix_defect_ladder_imported=true
phase_residue_exchange_pivot_boundary_operator_closed=true
phase_residue_exchange_internal_source_cancellation_closed=true
phase_residue_exchange_endpoint_charge_identity_closed=true
phase_residue_exchange_endpoint_telescoping_charge_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：前缀单位缺口 ladder 的内部源点不能匿名携带净债。把第 `i` 个 pivot 写成源侧边界
`d_i=[u_i]-[u_{i-1}]` 后，内部 `u_i` 在相邻两项中一正一负相消，整条链只剩
`[s0]-[s]`。每个前缀也满足 `sum_{i=1}^t d_i=[u_t]-[u_0]`，与缺失源状态输运一致。

因此若反例链继续存在，它必须在端点望远镜电荷中产生真实容量/相位矛盾，或回流 singleton、full-cycle mean、multiplicity cap、bridge、amplitude、boundary flux、sparse SAE 等已有出口。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeEndpointTelescopingChargeCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange endpoint telescoping charge circuit PDEC/cap、
bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap
或 sparse SAE 求和；它只把 exchange prefix defect ladder circuit 压成 endpoint telescoping
charge circuit 或 mean/singleton/sparse/三出口。

## 260. Stable-ladder phase-residue exchange root-star charge frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_root_star_charge_router.py
docs/monograph/prime-matrix-phase-residue-exchange-root-star-charge-router.md
docs/monograph/prime-matrix-phase-residue-exchange-root-star-charge-router.json
data/prime-matrix-phase-residue-exchange-root-star-charge-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeEndpointTelescopingChargeCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

```text
phase_residue_exchange_endpoint_telescoping_charge_imported=true
phase_residue_exchange_common_root_endpoint_closed=true
phase_residue_exchange_root_charge_multiplicity_closed=true
phase_residue_exchange_root_star_total_charge_zero_closed=true
phase_residue_exchange_root_star_charge_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：端点望远镜电荷族不是任意端点分布。每个非根源点有 `c_s=[s0]-[s]`，且所有电荷指向同一根点 `s0`。聚合后根点电荷为 `|S|-1`，每个非根源点为 `-1`，总电荷为零。

因此若反例链继续存在，它必须在“根点集中、非根单位输出、总量守恒”的 root-star charge circuit 中产生真实容量/相位矛盾，或回流 singleton、full-cycle mean、multiplicity cap、bridge、amplitude、boundary flux、sparse SAE 等已有出口。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeRootStarChargeCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange root-star charge circuit PDEC/cap、
bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux PDEC/cap
或 sparse SAE 求和；它只把 endpoint telescoping charge circuit 压成 exchange root-star
charge circuit 或 mean/singleton/sparse/三出口。

## 261. Stable-ladder phase-residue exchange normalized root-mean dipole frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_normalized_root_mean_dipole_router.py
docs/monograph/prime-matrix-phase-residue-exchange-normalized-root-mean-dipole-router.md
docs/monograph/prime-matrix-phase-residue-exchange-normalized-root-mean-dipole-router.json
data/prime-matrix-phase-residue-exchange-normalized-root-mean-dipole-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeRootStarChargeCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

```text
phase_residue_exchange_root_star_charge_imported=true
phase_residue_exchange_root_mean_normalization_closed=true
phase_residue_exchange_nonroot_mean_measure_closed=true
phase_residue_exchange_normalized_root_mean_dipole_zero_mean_closed=true
phase_residue_exchange_normalized_root_mean_dipole_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：根星电荷的主要容量形态不再是根点被 `|S|-1` 倍集中。
对非退化情形除以 `|S|-1` 后，根星电荷等价于
`D=[s0]-(1/(|S|-1))sum_{s!=s0}[s]`，也就是共同根点相对全部非根源点均值的零均值偶极。
退化情形仍由 singleton atom/SAE 出口承接。

因此若反例链继续存在，它必须在“根点相对非根均值偏差”的 normalized root-mean dipole
circuit 中产生真实容量/相位矛盾，或回流 singleton、full-cycle mean、multiplicity cap、
bridge、amplitude、boundary flux、sparse SAE 等已有出口。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeNormalizedRootMeanDipoleCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange normalized root-mean dipole circuit
PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、variation-boundary flux
PDEC/cap 或 sparse SAE 求和；它只把 exchange root-star charge circuit 压成 normalized
root-mean dipole circuit 或 mean/singleton/sparse/三出口。

## 262. Stable-ladder phase-residue exchange root-source pair-average contrast frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_root_source_pair_average_contrast_router.py
docs/monograph/prime-matrix-phase-residue-exchange-root-source-pair-average-contrast-router.md
docs/monograph/prime-matrix-phase-residue-exchange-root-source-pair-average-contrast-router.json
data/prime-matrix-phase-residue-exchange-root-source-pair-average-contrast-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeNormalizedRootMeanDipoleCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

```text
phase_residue_exchange_normalized_root_mean_dipole_imported=true
phase_residue_exchange_root_source_pair_fan_closed=true
phase_residue_exchange_uniform_pair_weight_closed=true
phase_residue_exchange_pair_average_contrast_identity_closed=true
phase_residue_exchange_root_source_pair_average_contrast_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：根点相对非根均值的偏差不是不可拆的均值云。对每个非根源点
定义 `e_s=[s0]-[s]` 后，
`D=(1/(|S|-1))sum_{s!=s0}e_s`。每个 `e_s` 是根点正单位与源点负单位的零均值单位对比，
且所有权重完全相同。

因此若反例链继续存在，它必须在“根点到单个非根源点的成对对比均匀扇”中产生真实
容量/相位矛盾，或回流 singleton、full-cycle mean、multiplicity cap、bridge、amplitude、
boundary flux、sparse SAE 等已有出口。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeRootSourcePairAverageContrastCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 endpoint singleton atom/SAE、full-cycle mean atom/SAE、source-atom
multiplicity-cap PDEC/cap、phase-residue exchange root-source pair-average contrast
circuit PDEC/cap、bridge-cancellation PDEC/cap、amplitude-depth PDEC/cap、
variation-boundary flux PDEC/cap 或 sparse SAE 求和；它只把 normalized root-mean
dipole circuit 压成 root-source pair-average contrast circuit 或 mean/singleton/sparse/三出口。

## 263. Stable-ladder phase-residue exchange root-source pair witness localization frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_root_source_pair_witness_localization_router.py
docs/monograph/prime-matrix-phase-residue-exchange-root-source-pair-witness-localization-router.md
docs/monograph/prime-matrix-phase-residue-exchange-root-source-pair-witness-localization-router.json
data/prime-matrix-phase-residue-exchange-root-source-pair-witness-localization-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeRootSourcePairAverageContrastCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

```text
phase_residue_exchange_root_source_pair_average_contrast_imported=true
phase_residue_exchange_pair_witness_mean_identity_closed=true
phase_residue_exchange_average_to_single_pair_max_localization_closed=true
phase_residue_exchange_named_single_pair_witness_closed=true
phase_residue_exchange_root_source_pair_witness_localization_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：若一个线性相位/容量见证能检测成对平均异常，那么它不能只存在于
平均整体上。设 `a_s=Lambda([s0]-[s])`，则 `Lambda(D)` 是这些 `a_s` 的均匀平均；
定向后至少有一个命名源点 `s*` 满足 `sigma*a_s* >= |Lambda(D)|`。

因此若反例链继续存在，它必须在一个命名 root-source pair 的见证定位 circuit 中产生真实
容量/相位矛盾，或回流 singleton、full-cycle mean、multiplicity cap、bridge、amplitude、
boundary flux、sparse SAE 等已有出口。

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

## 264. Stable-ladder phase-residue exchange oriented root-source witness gap frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_oriented_root_source_witness_gap_router.py
docs/monograph/prime-matrix-phase-residue-exchange-oriented-root-source-witness-gap-router.md
docs/monograph/prime-matrix-phase-residue-exchange-oriented-root-source-witness-gap-router.json
data/prime-matrix-phase-residue-exchange-oriented-root-source-witness-gap-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeRootSourcePairWitnessLocalizationCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

```text
phase_residue_exchange_root_source_pair_witness_localization_imported=true
phase_residue_exchange_named_root_source_pair_closed=true
phase_residue_exchange_oriented_witness_gap_coordinate_closed=true
phase_residue_exchange_witness_gap_lower_bound_closed=true
linear_witness_existence_proved=false
phase_residue_exchange_oriented_root_source_witness_gap_circuit_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：上一层的命名单对见证已经不再是平均扇对象。本步把它写成两个
端点分数 `R=sigma*Lambda([s0])` 与 `T=sigma*Lambda([s*])` 的有向差值：
`G=R-T=sigma*Lambda([s0]-[s*])`。上一层定位不等式直接变成
`G>=|Lambda(D)|`；若平均见证非零，则 `G>0`。

因此若反例链继续存在，它必须在一个命名 root-source pair 的有向端点差值中产生真实
容量/相位矛盾，或回流 singleton、full-cycle mean、multiplicity cap、bridge、amplitude、
boundary flux、sparse SAE 等已有出口。

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

## 265. Stable-ladder phase-residue exchange centered root-source score dipole frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_centered_root_source_score_dipole_router.py
docs/monograph/prime-matrix-phase-residue-exchange-centered-root-source-score-dipole-router.md
docs/monograph/prime-matrix-phase-residue-exchange-centered-root-source-score-dipole-router.json
data/prime-matrix-phase-residue-exchange-centered-root-source-score-dipole-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeOrientedRootSourceWitnessGapCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：有向差值 `G=R-T` 的共同偏移不是硬点。取
`M=(R+T)/2` 后，根端与源端分数无损写成 `R=M+G/2`、`T=M-G/2`。
中心化分数 `U=G/2`、`V=-G/2` 满足 `U+V=0`，并由上一层下界得到
`U>=|Lambda(D)|/2`。若平均见证非零，则这是一个根端正、源端负的两点偶极。

因此若反例链继续存在，它必须在零均值 centered root-source score dipole 中产生真实
容量/相位矛盾，或回流 singleton、full-cycle mean、multiplicity cap、bridge、amplitude、
boundary flux、sparse SAE 等已有出口。

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

## 266. Stable-ladder phase-residue exchange signed root-source half-gap atom frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_signed_root_source_half_gap_atom_router.py
docs/monograph/prime-matrix-phase-residue-exchange-signed-root-source-half-gap-atom-router.md
docs/monograph/prime-matrix-phase-residue-exchange-signed-root-source-half-gap-atom-router.json
data/prime-matrix-phase-residue-exchange-signed-root-source-half-gap-atom-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeCenteredRootSourceScoreDipoleCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：中心化两点偶极已经没有公共偏移，但还可以去掉端点分数表述。
设 `A=G/2`，则 `U=A`、`V=-A`，所以中心化分数向量等于
`W=A([s0]-[s*])`。这个符号原子净质量为 `0`，总变差为 `2A=G`，并继承
`A>=|Lambda(D)|/2`。若平均见证非零，则 `A>0`。

因此若反例链继续存在，它必须在一个正幅度的 root-positive/source-negative signed
half-gap atom 中产生真实容量/相位矛盾，或回流 singleton、full-cycle mean、multiplicity
cap、bridge、amplitude、boundary flux、sparse SAE 等已有出口。

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

## 267. Stable-ladder phase-residue exchange oriented root-source transport edge frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_oriented_root_source_transport_edge_router.py
docs/monograph/prime-matrix-phase-residue-exchange-oriented-root-source-transport-edge-router.md
docs/monograph/prime-matrix-phase-residue-exchange-oriented-root-source-transport-edge-router.json
data/prime-matrix-phase-residue-exchange-oriented-root-source-transport-edge-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeSignedRootSourceHalfGapAtomCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：`W=A([s0]-[s*])` 可以视为单条输运边的边界。
把边定向为 `s* -> s0` 并令通量 `F=A`，则
`partial(F e)=A([s0]-[s*])=W`。因此 root 端散度为 `+A`，source 端散度为 `-A`，
总散度为 `0`，且通量继承 `A>=|Lambda(D)|/2`。

因此若反例链继续存在，它必须在一条命名 source-to-root transport edge 中产生真实
容量/相位矛盾，或回流 singleton、full-cycle mean、multiplicity cap、bridge、amplitude、
boundary flux、sparse SAE 等已有出口。

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

## 268. Stable-ladder phase-residue exchange transport-edge incidence column frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_transport_edge_incidence_column_router.py
docs/monograph/prime-matrix-phase-residue-exchange-transport-edge-incidence-column-router.md
docs/monograph/prime-matrix-phase-residue-exchange-transport-edge-incidence-column-router.json
data/prime-matrix-phase-residue-exchange-transport-edge-incidence-column-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeOrientedRootSourceTransportEdgeCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：`e=s* -> s0`、`F=A` 不再只是边记号，而是单列边界矩阵坐标。
令 `b_e=[s0]-[s*]` 且 `B[:,e]=b_e`，单通量向量满足 `f_e=A`，于是
`Bf=A b_e=A([s0]-[s*])=W`。该 incidence column 的列和为 `0`；非退化情形下，
它只在 root/source 两端有非零坐标。单列对象没有内部路径或循环可藏。

因此若反例链继续存在，它必须在一列命名 boundary-matrix incidence column 中产生真实
容量/相位矛盾，或回流 singleton、full-cycle mean、multiplicity cap、bridge、amplitude、
boundary flux、sparse SAE 等已有出口。

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

## 269. Stable-ladder phase-residue exchange incidence-column Kronecker stencil frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_incidence_column_kronecker_stencil_router.py
docs/monograph/prime-matrix-phase-residue-exchange-incidence-column-kronecker-stencil-router.md
docs/monograph/prime-matrix-phase-residue-exchange-incidence-column-kronecker-stencil-router.json
data/prime-matrix-phase-residue-exchange-incidence-column-kronecker-stencil-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeTransportEdgeIncidenceColumnCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：`b_e=[s0]-[s*]` 不是匿名矩阵列，而是两个端点单位坐标的差。
定义 `delta_{s0}` 与 `delta_{s*}` 后，
`k=delta_{s0}-delta_{s*}`，所以 `b_e=k`，且
`A k=A(delta_{s0}-delta_{s*})=W`。root/source 两端继承上游 primitive witness CRT
coordinate atom 的 residue word，因此模板可以写成在 `crt(s0)` 处系数 `+1`、在
`crt(s*)` 处系数 `-1` 的显式 signed stencil。若 `s0=s*`，则模板为零并回流
singleton/degenerate 出口。

因此若反例链继续存在，它必须在一对命名 CRT 端点单位坐标的 signed stencil 中产生真实
容量/相位矛盾，或回流 singleton、full-cycle mean、multiplicity cap、bridge、amplitude、
boundary flux、sparse SAE 等已有出口。

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

## 270. Stable-ladder phase-residue exchange Kronecker-stencil signed CRT pair frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_kronecker_stencil_signed_crt_pair_router.py
docs/monograph/prime-matrix-phase-residue-exchange-kronecker-stencil-signed-crt-pair-router.md
docs/monograph/prime-matrix-phase-residue-exchange-kronecker-stencil-signed-crt-pair-router.json
data/prime-matrix-phase-residue-exchange-kronecker-stencil-signed-crt-pair-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeIncidenceColumnKroneckerStencilCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：`k=delta_{s0}-delta_{s*}` 不再只是 delta 函数模板。
把两个端点登记为显式 CRT words：
`r0=crt(s0)`、`r*=crt(s*)`、`Pi=(r0,r*)`，并保留 canonical congruence
equation 族：

```text
s0 == r0_i mod p_i  for every active prime coordinate p_i
s* == r*_i mod p_i  for every active prime coordinate p_i
```

于是 stencil 等价于有限 signed support dictionary：

```text
C_Pi(r0)=+1
C_Pi(r*)=-1
C_Pi(r)=0 for all other CRT words
A C_Pi=W.
```

若 `r0=r*`，字典消去并回流 singleton/degenerate 出口；否则剩余对象就是
两个命名 CRT words 的有序 signed dictionary。匿名 Kronecker stencil 口径被删除。

因此若反例链继续存在，它必须在这对 signed CRT words 上产生真实容量/相位矛盾，
或回流 singleton、full-cycle mean、multiplicity cap、bridge、amplitude、
boundary flux、sparse SAE 等已有出口。

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

## 271. Stable-ladder phase-residue exchange signed CRT pair primitive atom frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_signed_crt_pair_primitive_atom_router.py
docs/monograph/prime-matrix-phase-residue-exchange-signed-crt-pair-primitive-atom-router.md
docs/monograph/prime-matrix-phase-residue-exchange-signed-crt-pair-primitive-atom-router.json
data/prime-matrix-phase-residue-exchange-signed-crt-pair-primitive-atom-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeKroneckerStencilSignedCRTPairCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：`C_Pi(r0)=+1`、`C_Pi(r*)=-1`、`A C_Pi=W`
不再保留为一般有限字典。非退化情形下，它被登记为二词 signed support primitive atom：

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

若 `r0=r*`，则正负系数消去并回流 singleton/degenerate 出口；否则有序方向保留为
source -> root。匿名 signed CRT dictionary 口径被删除。

因此若反例链继续存在，它必须在这个二词 primitive atom 上产生真实容量/相位矛盾，
或回流 singleton、full-cycle mean、multiplicity cap、bridge、amplitude、
boundary flux、sparse SAE 等已有出口。

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

## 272. Stable-ladder phase-residue exchange primitive atom endpoint charge frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_primitive_atom_endpoint_charge_router.py
docs/monograph/prime-matrix-phase-residue-exchange-primitive-atom-endpoint-charge-router.md
docs/monograph/prime-matrix-phase-residue-exchange-primitive-atom-endpoint-charge-router.json
data/prime-matrix-phase-residue-exchange-primitive-atom-endpoint-charge-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeSignedCRTPairPrimitiveAtomCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：`support={r0,r*}`、`coefficient(r0)=+1`、
`coefficient(r*)=-1`、`flux_weights=(+A,-A)` 不再保留为匿名 primitive atom。
非退化情形下，它被登记为两个命名端点电荷：

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

若 `r0=r*`，则同点正负电荷消去并回流 singleton/degenerate 出口；否则有序方向保留为
source -> root。匿名 primitive atom 口径被删除。

因此若反例链继续存在，它必须在这个 root/source endpoint charge packet 上产生真实
容量/相位矛盾，或回流 singleton、full-cycle mean、multiplicity cap、bridge、
amplitude、boundary flux、sparse SAE 等已有出口。

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

## 273. Stable-ladder phase-residue exchange endpoint charge Kirchhoff cell frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_endpoint_charge_kirchhoff_cell_router.py
docs/monograph/prime-matrix-phase-residue-exchange-endpoint-charge-kirchhoff-cell-router.md
docs/monograph/prime-matrix-phase-residue-exchange-endpoint-charge-kirchhoff-cell-router.json
data/prime-matrix-phase-residue-exchange-endpoint-charge-kirchhoff-cell-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangePrimitiveAtomEndpointChargeCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：`root_charge=(r0,+A)`、`source_charge=(r*,-A)`、
`net_charge=0`、`absolute_flux=2A` 不再保留为匿名 endpoint charge packet。
非退化情形下，它被登记为二点局部散度守恒单元：

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

若 `r0=r*`，则同点正负散度消去并回流 singleton/degenerate 出口；否则有序方向保留为
source -> root。匿名 endpoint charge packet 口径被删除。

因此若反例链继续存在，它必须在这个局部 Kirchhoff cell 上产生真实容量/相位矛盾，
或回流 singleton、full-cycle mean、multiplicity cap、bridge、amplitude、
boundary flux、sparse SAE 等已有出口。

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

## 274. Stable-ladder phase-residue exchange Kirchhoff cell cut-potential frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_kirchhoff_cell_cut_potential_router.py
docs/monograph/prime-matrix-phase-residue-exchange-kirchhoff-cell-cut-potential-router.md
docs/monograph/prime-matrix-phase-residue-exchange-kirchhoff-cell-cut-potential-router.json
data/prime-matrix-phase-residue-exchange-kirchhoff-cell-cut-potential-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeEndpointChargeKirchhoffCellCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：`K={r0,r*}`、`div(r0)=+A`、`div(r*)=-A`、
`sum_K div=0` 不再保留为匿名 Kirchhoff cell。非退化情形下，它被登记为规范化势函数证书：

```text
phi(r0)=+1/2
phi(r*)=-1/2
phi(r0)+phi(r*)=0
phi(r0)-phi(r*)=1
<div,phi>=(+A)(+1/2)+(-A)(-1/2)=A
A C_Pi=W.
```

若 `r0=r*`，则势差退化并回流 singleton/degenerate 出口；否则有序方向由
`phi(root)-phi(source)>0` 保留。匿名 Kirchhoff cell 口径被删除。

因此若反例链继续存在，它必须在这个 cut-potential 正配对证书上产生真实容量/相位矛盾，
或回流 singleton、full-cycle mean、multiplicity cap、bridge、amplitude、
boundary flux、sparse SAE 等已有出口。

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

## 275. Stable-ladder phase-residue exchange cut-potential dual-norm frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_cut_potential_dual_norm_router.py
docs/monograph/prime-matrix-phase-residue-exchange-cut-potential-dual-norm-router.md
docs/monograph/prime-matrix-phase-residue-exchange-cut-potential-dual-norm-router.json
data/prime-matrix-phase-residue-exchange-cut-potential-dual-norm-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeEndpointChargeKirchhoffCellCutPotentialCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：`phi(r0)=+1/2`、`phi(r*)=-1/2` 与 `<div,phi>=A`
不再保留为匿名势函数配对。非退化情形下，它被登记为对偶范数等号饱和：

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

若 `r0=r*`，则势差与对偶质量退化并回流 singleton/degenerate 出口；否则有序方向由
Hölder 等号条件中的极化符号对齐保留。匿名 cut-potential 口径被删除。

因此若反例链继续存在，它必须在这个 dual-norm saturation 证书上产生真实容量/相位矛盾，
或回流 singleton、full-cycle mean、multiplicity cap、bridge、amplitude、
boundary flux、sparse SAE 等已有出口。

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

## 276. Stable-ladder phase-residue exchange complementary slackness frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_dual_norm_complementary_slackness_router.py
docs/monograph/prime-matrix-phase-residue-exchange-dual-norm-complementary-slackness-router.md
docs/monograph/prime-matrix-phase-residue-exchange-dual-norm-complementary-slackness-router.json
data/prime-matrix-phase-residue-exchange-dual-norm-complementary-slackness-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeCutPotentialDualNormSaturationCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：`||div||_1=2A`、`||phi||_infty=1/2`、`<div,phi>=A`
不再保留为匿名对偶范数等号。非退化情形下，它被登记为一条校准输运边：

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

若 `r0=r*`，则边、势差与对偶间隙证书退化并回流 singleton/degenerate 出口；否则有序方向由
负势/负散度端指向正势/正散度端。匿名 dual-norm saturation 口径被删除。

因此若反例链继续存在，它必须在这个 complementary-slackness 零间隙证书上产生真实容量/相位矛盾，
或回流 singleton、full-cycle mean、multiplicity cap、bridge、amplitude、
boundary flux、sparse SAE 等已有出口。

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

## 277. Stable-ladder phase-residue exchange active-facet normal-cone frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_complementary_slackness_active_facet_router.py
docs/monograph/prime-matrix-phase-residue-exchange-complementary-slackness-active-facet-router.md
docs/monograph/prime-matrix-phase-residue-exchange-complementary-slackness-active-facet-router.json
data/prime-matrix-phase-residue-exchange-complementary-slackness-active-facet-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeDualNormComplementarySlacknessCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：`e=(r* -> r0)`、`primal_cost=dual_value=A`、`duality_gap=0`
不再保留为匿名互补松弛口径。非退化情形下，它被登记为单个活跃约束面及其正法锥：

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

若 `r0=r*` 或 `A=0`，则法向量/法锥证书退化并回流 singleton/degenerate 出口；否则正法向量
`[r0]-[r*]` 保留 source -> root 的有序方向。匿名 complementary slackness 口径被删除。

因此若反例链继续存在，它必须在这个 active-facet normal-cone 证书上产生真实容量/相位矛盾，
或回流 singleton、full-cycle mean、multiplicity cap、bridge、amplitude、
boundary flux、sparse SAE 等已有出口。

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

## 278. Stable-ladder phase-residue exchange normal-cone ray-coordinate frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeComplementarySlacknessActiveFacetNormalConeCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：`n_e=[r0]-[r*]`、`N_e={lambda n_e: lambda>=0}`、
`div=A n_e` 不再保留为匿名正法锥口径。非退化情形下，它被登记为唯一正射线坐标：

```text
ray_generator=n_e=[r0]-[r*]
div=lambda n_e
lambda=A>0
transverse_component=0
<div,phi>=lambda(phi(r0)-phi(r*))=A
||div||_1=2lambda=2A
A C_Pi=W.
```

若 `r0=r*` 或 `A=0`，则生成元/坐标退化并回流 singleton/degenerate 出口；否则二点支撑
和一维正法锥排除任何横向分量，并固定唯一正坐标 `lambda=A`。匿名 active-facet normal-cone
口径被删除。

因此若反例链继续存在，它必须在这个 normal-cone ray-coordinate 证书上产生真实容量/相位矛盾，
或回流 singleton、full-cycle mean、multiplicity cap、bridge、amplitude、
boundary flux、sparse SAE 等已有出口。

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

## 279. Stable-ladder phase-residue exchange ray-coordinate scalar-load frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：`div=lambda n_e`、`lambda=A>0`、`<div,phi>=A`、
`||div||_1=2A` 不再保留为匿名 ray-coordinate 口径。非退化情形下，它被登记为单一正标量负载：

```text
scalar_load=A=lambda>0
rank_one_generator=n_e=[r0]-[r*]
pairing_load=<div,phi>=A
variation_load=||div||_1/2=A
unit_saturation_ratio=1
residual_vector_geometry=0
A C_Pi=W.
```

若 `r0=r*` 或 `A=0`，则 scalar load 退化并回流 singleton/degenerate 出口；否则待支付对象
只剩同一个正标量 `A`。匿名 ray-coordinate 口径被删除。

因此若反例链继续存在，它必须在这个 scalar-load 证书上产生真实容量/相位矛盾，
或回流 singleton、full-cycle mean、multiplicity cap、bridge、amplitude、
boundary flux、sparse SAE 等已有出口。

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

## 280. Stable-ladder phase-residue exchange scalar-load unit-normalization frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：`scalar_load=A` 不再保留为可任意缩放或拆分的黑箱。非退化情形下，
它被分解为单位二点形状和唯一总权重：

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

若 `r0=r*` 或 `A=0`，则单位形状或正尺度退化并回流 singleton/degenerate 出口；
否则反例链必须在同一个单位二点证书的总权重 `A` 上产生容量/相位矛盾。

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

## 281. Stable-ladder phase-residue exchange unit-face-value frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：unit-normalization 证书不再允许隐藏容量乘子或面额换算。非退化情形下，
支付对象被写成 price-one 单位证书上的数量：

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

若 `r0=r*` 或 `A=0`，则单位面额证书退化并回流 singleton/degenerate 出口；
否则反例链必须在这个 face-value 为 1 的二点证书上产生容量/相位矛盾。

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

## 282. Stable-ladder phase-residue exchange signed-amount-coordinate frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：unit-face-value 证书不再允许隐藏匿名 amount 池、同面额多槽拆分或方向翻转。
非退化情形下，支付对象被写成唯一二端点有符号质量坐标：

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

若 `r0=r*` 或 `A=0`，则二端点有符号质量退化并回流 singleton/degenerate 出口；
否则反例链必须在这个 signed dictionary 的唯一 amount 坐标上产生容量/相位矛盾。

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

## 283. Stable-ladder phase-residue exchange phase-pairing frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinateCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：signed-amount-coordinate 证书不再允许隐藏相位偏移、相位重标定或符号错配。
非退化情形下，相位、容量与变差读数被锁为同一数值：

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

若 `r0=r*` 或 `A=0`，则相位配对退化并回流 singleton/degenerate 出口；
否则反例链必须在这个二端点 signed dictionary 的校准相位配对上产生容量/相位矛盾。

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

## 284. Stable-ladder phase-residue exchange circuit-materialization frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_circuit_materialization_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-circuit-materialization-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-circuit-materialization-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-circuit-materialization-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingCircuitPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：校准 phase-pairing 值 `A` 不能被 formal envelope 或另一条对象链替代。
剩余 circuit 必须先通过同一 actual CRT/fiber 对象物化门：

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

若同物化失败，得到 actual-circuit materialization PDEC/cap；若同物化成功，才进入
materialized-circuit capacity PDEC/cap。于是 phase-pairing circuit 不再是匿名黑箱。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingActualCircuitMaterializationPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitCapacityPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 actual-circuit materialization、materialized-circuit capacity、endpoint singleton、
full-cycle mean、source-atom multiplicity cap、bridge、amplitude、boundary 或 sparse SAE；
也没有证明线性见证本身存在。它只把 phase-pairing circuit 压成同一对象物化门与物化后容量门。

## 285. Stable-ladder phase-residue exchange actual-object-predicate frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_actual_object_predicate_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-actual-object-predicate-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-actual-object-predicate-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-actual-object-predicate-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingActualCircuitMaterializationPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitCapacityPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：actual materialization 不是一个可后验解释的口号，而是同一
formal-unit key 下的七槽 actual object 谓词：

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

缺对象、重复对象或槽位不一致都被登记为 actual-object incidence predicate PDEC/cap；
全部通过后才可进入 materialized-circuit capacity 门。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingActualObjectIncidencePredicatePDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitCapacityPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 actual-object incidence predicate、materialized-circuit capacity、endpoint singleton、
full-cycle mean、source-atom multiplicity cap、bridge、amplitude、boundary 或 sparse SAE；
也没有证明线性见证本身存在。它只把 actual materialization 压成七槽同对象谓词。

## 286. Stable-ladder phase-residue exchange materialized-capacity-slack frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_materialized_capacity_slack_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingActualObjectIncidencePredicatePDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitCapacityPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：容量比较必须使用同一 actual object 的真实负载与真实容量：

```text
O=(source_atom, occurrence_unit, crt_coordinate, canonical_congruence, phase_evaluation, signed_mass, calibrated_pairing)
L(O)=A=<W,phi>
A=amount=payment_value=||W||_1/2
C(O)=capacity of the same materialized circuit
Sigma(O)=C(O)-A
```

若 `Sigma(O)>0`，容量吸收；若 `Sigma(O)<0`，是真实超容量 PDEC/cap；
若 `Sigma(O)=0`，则是临界等号原子，必须命名登记，不能当作严格矛盾。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingActualObjectIncidencePredicatePDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitCapacitySlackPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 materialized capacity slack、actual-object incidence predicate、endpoint singleton、
full-cycle mean、source-atom multiplicity cap、bridge、amplitude、boundary 或 sparse SAE；
也没有证明线性见证本身存在。它只把 materialized capacity 压成同对象 slack 不等式。

## 287. Stable-ladder phase-residue exchange materialized-capacity-slack-sign frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_materialized_capacity_slack_sign_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-sign-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-sign-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-sign-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingActualObjectIncidencePredicatePDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitCapacitySlackPDECCapOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。
同步结果：

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

formal-to-actual 含义是：`Sigma(O)=C(O)-A` 的正、负、零三支不能混用。
正 slack 已被容量吸收；负 slack 是真实超容量缺陷；零 slack 是临界等号原子，
不能当作严格矛盾。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingActualObjectIncidencePredicatePDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitNegativeSlackPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitBoundaryEqualityAtomPDECOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 negative-slack PDEC/cap、没有排斥 boundary equality atom，也没有证明
actual-object incidence predicate、endpoint singleton、full-cycle mean、source-atom multiplicity cap、
bridge、amplitude、boundary 或 sparse SAE；它只把 materialized capacity slack 压成符号三分。

## 288. Stable-ladder phase-residue exchange negative-unit-defect frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_materialized_capacity_slack_sign_negative_unit_defect_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-sign-negative-unit-defect-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-sign-negative-unit-defect-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-materialized-capacity-slack-sign-negative-unit-defect-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingActualObjectIncidencePredicatePDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitNegativeSlackPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitBoundaryEqualityAtomPDECOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。

同步结果：

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

formal-to-actual 含义是：负 slack 不能继续作为实数微小缺口存在。
在同对象单位面值框架下，负支要么暴露为 `C(O)` 的单位整数容量值缺陷，
要么成为 `D(O)=A-C(O)>=1` 的单位负缺口。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingActualObjectIncidencePredicatePDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitCapacityValueUnitIntegralityPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitUnitNegativeDefectPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitBoundaryEqualityAtomPDECOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 capacity-value unit-integrality、没有排斥 unit negative defect，
没有排斥 boundary equality atom，也没有证明 actual-object incidence predicate、
endpoint singleton、full-cycle mean、source-atom multiplicity cap、bridge、amplitude、
boundary 或 sparse SAE；它只把负 slack 规整为单位整数缺口或容量值整数性缺陷。

## 289. Stable-ladder phase-residue exchange unit-defect-witness frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_unit_defect_witness_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-unit-defect-witness-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-unit-defect-witness-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-unit-defect-witness-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingActualObjectIncidencePredicatePDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitCapacityValueUnitIntegralityPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitUnitNegativeDefectPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitBoundaryEqualityAtomPDECOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。

同步结果：

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

formal-to-actual 含义是：`D=A-C(O)>=1` 不能停留为匿名总量赤字。
若容量接纳单位集合 `U_C` 没有作为需求单位集合 `U_A` 的同对象分配子集合物化，
它就是 unit-capacity assignment incidence 缺陷；若分配门通过，则
`U_A \ U_C` 非空并给出缺失单位见证 `u*`。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingActualObjectIncidencePredicatePDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitCapacityValueUnitIntegralityPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitUnitCapacityAssignmentIncidencePDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitMissingCapacityUnitWitnessPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitBoundaryEqualityAtomPDECOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 unit-capacity assignment incidence，没有排斥 missing capacity unit witness，
没有证明 capacity-value unit-integrality、没有排斥 boundary equality atom，也没有证明
actual-object incidence predicate、endpoint singleton、full-cycle mean、source-atom multiplicity cap、
bridge、amplitude、boundary 或 sparse SAE；它只把单位负缺口物化为局部见证出口。

## 290. Stable-ladder phase-residue exchange missing-unit-coordinate-lock frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_missing_unit_coordinate_lock_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-missing-unit-coordinate-lock-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-missing-unit-coordinate-lock-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-missing-unit-coordinate-lock-ledger.json
```

本步继续攻击
`SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingActualObjectIncidencePredicatePDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitCapacityValueUnitIntegralityPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitUnitCapacityAssignmentIncidencePDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitMissingCapacityUnitWitnessPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitBoundaryEqualityAtomPDECOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap`。

同步结果：

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

formal-to-actual 含义是：缺失单位 `u*` 不能换对象、换槽或移动。
它必须同时携带需求成员、容量排除、source atom、occurrence unit、CRT coordinate、
canonical congruence、phase endpoint 与 signed amount 槽位。任一槽不一致时，
回流为 coordinate slot mismatch；全部一致时，剩余为 canonical missing capacity unit witness。

新的直接主攻为：

```text
SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingActualObjectIncidencePredicatePDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitCapacityValueUnitIntegralityPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitUnitCapacityAssignmentIncidencePDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitMissingUnitCoordinateSlotMismatchPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitCanonicalMissingCapacityUnitWitnessPDECCapOrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomPhaseResidueEvaluationAtomExchangeActiveFacetNormalConeRayCoordinateScalarLoadUnitNormalizationUnitFaceValueSignedAmountCoordinatePhasePairingMaterializedCircuitBoundaryEqualityAtomPDECOrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCapOrEndpointOrbitVariationBoundaryFluxPDECCap
```

本步没有证明 coordinate slot mismatch、没有排斥 canonical missing capacity unit witness，
没有证明 unit-capacity assignment incidence、capacity-value unit-integrality、actual-object incidence predicate，
也没有排斥 boundary equality atom 或 endpoint 并行出口；它只把缺失单位见证锁成 canonical 坐标对象。

## 291. Stable-ladder phase-residue exchange canonical-missing-unit-balance frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_missing_unit_balance_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-missing-unit-balance-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-missing-unit-balance-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-missing-unit-balance-ledger.json
```

同步结果：

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

formal-to-actual 含义是：上一层留下的 canonical missing capacity unit witness
不再是一个可滑移的局部物件，而是同一 key `k` 上的确定单位余额：
`I_A(k)=1`、`I_C(k)=0`、`unit_face_value=1`。因此它只能作为
canonical unpaid demand cell 保留，或要求一个同对象同 key 的合法补偿对象；
后者若换对象、换 key、换槽或没有进入已命名 boundary/bridge/assignment 出口，
则成为 canonical compensation mismatch。

本步没有闭合行/列命题；最新剩余为 canonical unpaid demand cell、canonical
compensation mismatch、missing-unit slot mismatch、assignment incidence、
capacity integrality、boundary equality、actual-object incidence predicate 与 endpoint 并行出口。

## 292. Stable-ladder phase-residue exchange canonical-unit-payment-conservation frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_unit_payment_conservation_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-unit-payment-conservation-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-unit-payment-conservation-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-unit-payment-conservation-ledger.json
```

同步结果：

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

formal-to-actual 含义是：同 key 赤字不能由隐藏跨 key 支付抹平。
若没有同对象同 key 的容量边，也没有 boundary/bridge/assignment/slot-mismatch
等已命名 return，则剩余就是 canonical unit payment conservation defect。
若声称有补偿但使用另一 key，则剩余就是 canonical unit compensator key collision。

本步没有闭合行/列命题；最新剩余为 canonical payment conservation defect、
canonical compensator key collision、payment graph/edge obligation/return whitelist、
boundary equality、actual-object incidence predicate 与 endpoint 并行出口。

## 293. Stable-ladder phase-residue exchange canonical-unit-payment-singleton-cut frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_unit_payment_singleton_cut_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-unit-payment-singleton-cut-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-unit-payment-singleton-cut-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-unit-payment-singleton-cut-ledger.json
```

同步结果：

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

formal-to-actual 含义是：取缺失 key `k` 的单点 cut 后，当前赤字具有
显式 Hall 形态：`cut_demand=1` 且 `cut_capacity=0`。如果没有 boundary、
bridge、assignment、slot-mismatch 等命名 return 离开该 cut，则剩余就是
canonical singleton Hall cut defect。若跨 key 补偿声称同一 canonical cell，
则剩余为 key injectivity defect；若跨 key 补偿不是同一 cell 且未进入白名单，
则剩余为 cross-key return whitelist leak。

本步没有闭合行/列命题；最新剩余为 singleton Hall cut defect、payment key
injectivity defect、cross-key return whitelist leak、payment graph/return whitelist、
boundary equality、actual-object incidence predicate 与 endpoint 并行出口。

## 294. Stable-ladder phase-residue exchange canonical-payment-key-tuple-lock frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_key_tuple_lock_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-tuple-lock-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-tuple-lock-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-tuple-lock-ledger.json
```

同步结果：

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

formal-to-actual 含义是：`payment_key` 由 actual-object 七槽 hash 与
missing-unit canonical hash 的 tuple 定义。跨 key 补偿若仍声称同一 canonical
cell，就必须满足所有 tuple 投影逐槽相等；否则它不是同一 cell，并回流坐标
槽位不一致。若投影相等但 key 仍不同，则剩余变成 key tuple alias defect。

本步没有闭合行/列命题；最新剩余为 singleton Hall cut defect、key tuple alias
defect、missing-unit slot mismatch、cross-key return whitelist leak、payment
graph/return whitelist、boundary equality、actual-object incidence predicate 与 endpoint 并行出口。

## 295. Stable-ladder phase-residue exchange canonical-payment-key-alias-normalization frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_key_alias_normalization_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-alias-normalization-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-alias-normalization-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-alias-normalization-ledger.json
```

同步结果：

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

formal-to-actual 含义是：同 tuple 不同 key 必须解释为规范化失败，而不是
新的支付自由度。若同一 payment tuple 有两个 key，则要么 canonical bytes
已经漂移，要么某条支付边仍携带非规范外部标签。

本步没有闭合行/列命题；最新剩余为 payment key serialization drift、
noncanonical key label residue、missing-unit slot mismatch、singleton Hall cut、
cross-key return whitelist leak、payment graph/return whitelist、boundary equality、
actual-object incidence predicate 与 endpoint 并行出口。

## 296. Stable-ladder phase-residue exchange canonical-payment-serialization-codec-lock frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_serialization_codec_lock_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-serialization-codec-lock-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-serialization-codec-lock-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-serialization-codec-lock-ledger.json
```

同步结果：

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

formal-to-actual 含义是：同一 payment tuple 先给出同一字段向量；canonical
serialization 是这个字段向量的确定函数。若两条记录声称同 tuple 但字节串
不同，则唯一可能是字段向量其实不同，并回流已有命名出口；否则确定 codec
直接给出相同字节串。

本步没有闭合行/列命题；最新剩余为 noncanonical key label residue、
missing-unit slot mismatch、singleton Hall cut、cross-key return whitelist leak、
payment graph/return whitelist、boundary equality、actual-object incidence predicate
与 endpoint 并行出口。

## 297. Stable-ladder phase-residue exchange canonical-payment-key-label-admission-lock frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_key_label_admission_lock_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-label-admission-lock-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-label-admission-lock-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-key-label-admission-lock-ledger.json
```

同步结果：

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

formal-to-actual 含义是：外部 key label 不决定 payment graph 的边。边只有在
canonical key 公式、对象 gate 与 unit-capacity gate 同时通过时才入图；非规范
标签若仍被当作 return 使用，就落入 cross-key return whitelist leak。

本步没有闭合行/列命题；最新剩余为 missing-unit slot mismatch、singleton Hall cut、
cross-key return whitelist leak、payment graph/return whitelist、boundary equality、
actual-object incidence predicate 与 endpoint 并行出口。

## 298. Stable-ladder phase-residue exchange canonical-payment-same-cell-slot-admission frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_same_cell_slot_admission_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-same-cell-slot-admission-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-same-cell-slot-admission-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-same-cell-slot-admission-ledger.json
```

同步结果：

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

formal-to-actual 含义是：槽位不一致的候选边不是同一 missing unit cell 的
admitted payment edge。若它仍被计入容量，则是 assignment-incidence 失败；
若不计入，单点 Hall cut 的 `demand=1, capacity=0` 赤字不变。

本步没有闭合行/列命题；最新剩余为 assignment incidence、singleton Hall cut、
cross-key return whitelist leak、payment graph/return whitelist、boundary equality、
actual-object incidence predicate 与 endpoint 并行出口。

## 299. Stable-ladder phase-residue exchange canonical-payment-assignment-incidence-lock frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_assignment_incidence_lock_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-assignment-incidence-lock-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-assignment-incidence-lock-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-assignment-incidence-lock-ledger.json
```

同步结果：

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

formal-to-actual 含义是：坏计数不能再作为独立容量来源。它要么违反对象谓词，
要么违反一单位容量值，要么违反跨 key return whitelist；若这些 gate 都不失败，
则该单位是 admitted assignment 的一部分，否则剔除后 singleton Hall cut 赤字继续存在。

本步没有闭合行/列命题；最新剩余为 actual-object incidence、capacity integrality、
singleton Hall cut、cross-key return whitelist leak、payment graph/return whitelist、
boundary equality 与 endpoint 并行出口。

## 300. Stable-ladder phase-residue exchange canonical-payment-capacity-unit-value-lock frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_capacity_unit_value_lock_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-capacity-unit-value-lock-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-capacity-unit-value-lock-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-capacity-unit-value-lock-ledger.json
```

同步结果：

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

formal-to-actual 含义是：capacity value 只能由 admitted 0/1 unit indicators
有限相加得到。非一单位 signed amount 不是新的容量自由度；它要么暴露
actual-object incidence predicate 失败，要么在剔除后保留 singleton Hall cut
的单位赤字。

本步没有闭合行/列命题；最新剩余为 actual-object incidence、singleton Hall cut、
cross-key return whitelist leak、payment graph/return whitelist、boundary equality
与 endpoint 并行出口。

## 301. Stable-ladder phase-residue exchange canonical-payment-actual-object-field-packet-lock frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_actual_object_field_packet_lock_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-field-packet-lock-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-field-packet-lock-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-field-packet-lock-ledger.json
```

同步结果：

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

formal-to-actual 含义是：actual-object incidence 失败不能再停留为匿名对象失败。
它必须落入缺失对象、重复对象，或 source/occurrence/CRT/congruence/phase/
signed-mass/pairing 某个字段包失败。

本步没有闭合行/列命题；最新剩余为 actual-object 字段包出口、singleton Hall cut、
cross-key return whitelist leak、payment graph/return whitelist、boundary equality
与 endpoint 并行出口。

## 302. Stable-ladder phase-residue exchange canonical-payment-actual-object-slot-mismatch-unification frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_actual_object_slot_mismatch_unification_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-slot-mismatch-unification-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-slot-mismatch-unification-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-slot-mismatch-unification-ledger.json
```

同步结果：

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

formal-to-actual 含义是：source、occurrence、CRT、congruence、phase、signed-mass、
pairing 任一字段失败都不是新自由度，只是 canonical actual-object slot vector 的换槽。

本步没有闭合行/列命题；最新剩余为 actual-object missing/duplicate/slot mismatch、
singleton Hall cut、cross-key return whitelist leak、payment graph/return whitelist、
boundary equality 与 endpoint 并行出口。

## 303. Stable-ladder phase-residue exchange canonical-payment-actual-object-admission-trichotomy frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_actual_object_admission_trichotomy_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-admission-trichotomy-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-admission-trichotomy-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-actual-object-admission-trichotomy-ledger.json
```

同步结果：

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

formal-to-actual 含义是：对象缺失或换槽意味着不存在同 cell admitted capacity；
重对象若跨 key 作为 return 使用则是 whitelist leak，否则同 key 重复不增加容量。

本步没有闭合行/列命题；最新剩余为 singleton Hall cut、cross-key return whitelist
leak、payment graph/return whitelist、boundary equality 与 endpoint 并行出口。

## 304. Stable-ladder phase-residue exchange canonical-payment-singleton-cut-return-admission-lock frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_singleton_cut_return_admission_lock_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-singleton-cut-return-admission-lock-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-singleton-cut-return-admission-lock-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-singleton-cut-return-admission-lock-ledger.json
```

同步结果：

```text
phase_residue_exchange_singleton_hall_cut_defect_imported=true
phase_residue_exchange_actual_object_admission_trichotomy_imported=true
phase_residue_exchange_singleton_cut_router_imported=true
phase_residue_exchange_singleton_return_admission_partition_closed=true
phase_residue_exchange_same_key_return_no_new_capacity_closed=true
phase_residue_exchange_cross_key_return_whitelist_gate_closed=true
phase_residue_exchange_singleton_no_return_hall_atom_registered=true
phase_residue_exchange_no_independent_broad_singleton_hall_cut_defect_closed=true
phase_residue_exchange_canonical_singleton_no_return_hall_atom_pdec_cap_proved=false
phase_residue_exchange_canonical_cross_key_return_whitelist_leak_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：broad singleton Hall cut 的合法补偿空间被完全分区；
同 key 不增容，坏对象边已在 admission 层回流，跨 key 非白名单就是 whitelist leak。
剩余真正新硬点是没有任何合法 return 的单点 Hall 原子。

本步没有闭合行/列命题；最新剩余为 no-return Hall atom、cross-key return whitelist
leak、boundary equality 与 endpoint 并行出口。

## 305. Stable-ladder phase-residue exchange canonical-payment-singleton-no-return-endpoint-projection frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_singleton_no_return_endpoint_projection_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-singleton-no-return-endpoint-projection-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-singleton-no-return-endpoint-projection-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-singleton-no-return-endpoint-projection-ledger.json
```

同步结果：

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
row_column_unconditional_closed=false
```

formal-to-actual 含义是：单点 no-return 缺口的 phase endpoint 与 signed mass 已锁定；
它只能作为 endpoint singleton atom 或 source-atom multiplicity cap 继续存在。

本步没有闭合行/列命题；最新剩余为 endpoint singleton、source multiplicity、
cross-key return whitelist leak、boundary equality 与 endpoint 并行出口。

## 306. Stable-ladder phase-residue exchange canonical-payment-cross-key-return-whitelist-slot-projection frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_canonical_payment_cross_key_return_whitelist_slot_projection_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-cross-key-return-whitelist-slot-projection-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-cross-key-return-whitelist-slot-projection-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-canonical-payment-cross-key-return-whitelist-slot-projection-ledger.json
```

同步结果：

```text
phase_residue_exchange_cross_key_return_whitelist_leak_imported=true
phase_residue_exchange_actual_object_slot_vector_imported_for_cross_key_return=true
phase_residue_exchange_cross_key_return_unit_pair_closed=true
phase_residue_exchange_cross_key_return_slot_change_partition_closed=true
phase_residue_exchange_no_independent_cross_key_return_whitelist_leak_closed=true
source_atom_multiplicity_cap_pdec_cap_proved=false
phase_residue_exchange_boundary_equality_atom_exclusion_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：跨 key 非白名单 return 必须表现为 actual-object slot vector
的某一槽变化；这些变化已分别命名为 source multiplicity、boundary equality 或 endpoint
orbit 出口。

本步没有闭合行/列命题；最新剩余为 endpoint singleton、source multiplicity、
boundary equality、bridge/amplitude/variation 与 sparse 出口。

## 307. Stable-ladder phase-residue exchange boundary-equality-critical-endpoint-projection frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_boundary_equality_critical_endpoint_projection_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-boundary-equality-critical-endpoint-projection-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-boundary-equality-critical-endpoint-projection-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-boundary-equality-critical-endpoint-projection-ledger.json
```

同步结果：

```text
phase_residue_exchange_boundary_equality_atom_imported=true
phase_residue_exchange_slack_sign_imported_for_boundary_equality=true
phase_residue_exchange_boundary_equality_zero_slack_actual_object_closed=true
phase_residue_exchange_boundary_equality_critical_facet_closed=true
phase_residue_exchange_boundary_equality_first_variation_partition_closed=true
phase_residue_exchange_no_independent_boundary_equality_atom_closed=true
endpoint_orbit_full_cycle_mean_atom_sae_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：零 slack 临界面必须转化为 endpoint critical exits，不能作为
独立 boundary equality 出口停留。

本步没有闭合行/列命题；最新剩余为 sparse SAE、endpoint singleton、full-cycle mean、
source multiplicity、bridge、amplitude-depth、variation-boundary flux。

## 308. Stable-ladder phase-residue exchange endpoint-dynamic-signed-depth-flux-packet frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_endpoint_dynamic_signed_depth_flux_packet_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-dynamic-signed-depth-flux-packet-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-dynamic-signed-depth-flux-packet-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-dynamic-signed-depth-flux-packet-ledger.json
```

同步结果：

```text
endpoint_dynamic_bridge_amplitude_variation_imported=true
phase_residue_exchange_boundary_equality_projection_imported_for_dynamic_packet=true
endpoint_orbit_signed_depth_flux_decomposition_closed=true
endpoint_orbit_no_independent_bridge_amplitude_variation_closed=true
endpoint_orbit_signed_depth_flux_packet_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：endpoint 动态三出口被统一为 signed-depth/flux packet。

本步没有闭合行/列命题；最新剩余为 sparse SAE、endpoint singleton、full-cycle mean、
source multiplicity 与 signed-depth/flux packet。

## 309. Stable-ladder phase-residue exchange endpoint-signed-depth-flux-cycle-skeleton frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_endpoint_signed_depth_flux_cycle_skeleton_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-signed-depth-flux-cycle-skeleton-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-signed-depth-flux-cycle-skeleton-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-signed-depth-flux-cycle-skeleton-ledger.json
```

同步结果：

```text
endpoint_orbit_signed_depth_flux_packet_imported=true
endpoint_signed_depth_flux_finite_support_skeleton_closed=true
endpoint_signed_depth_flux_zero_mean_balance_closed=true
endpoint_signed_depth_flux_acyclic_leaf_return_closed=true
endpoint_signed_depth_flux_packet_reduced_to_alternating_cycle=true
endpoint_signed_depth_flux_alternating_transport_cycle_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：signed-depth/flux 整包已经被压成有限支撑图的交替输运环。
无环情形被叶剥离送回 endpoint singleton、full-cycle mean 或 source multiplicity；
因此最新剩余为 sparse SAE、endpoint singleton、full-cycle mean、source multiplicity
与 alternating transport cycle。

## 310. Stable-ladder phase-residue exchange endpoint-alternating-cycle-monodromy-lock frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_endpoint_alternating_cycle_monodromy_lock_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-monodromy-lock-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-monodromy-lock-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-monodromy-lock-ledger.json
```

同步结果：

```text
endpoint_alternating_transport_cycle_imported=true
endpoint_alternating_cycle_ordered_support_closed=true
endpoint_alternating_cycle_boundary_zero_closed=true
endpoint_alternating_cycle_monodromy_dichotomy_closed=true
endpoint_alternating_cycle_reduced_to_nonzero_monodromy=true
endpoint_alternating_cycle_monodromy_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：交替输运环被锁成有序 CRT endpoint cycle 与相位增量词。
零 monodromy 只是纯环流；非零 monodromy 是最新显式硬点。最新剩余为 sparse SAE、
endpoint singleton、full-cycle mean、source multiplicity 与 nonzero monodromy。

## 311. Stable-ladder phase-residue exchange endpoint-alternating-cycle-pivot-phase-slip frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_endpoint_alternating_cycle_pivot_phase_slip_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-ledger.json
```

同步结果：

```text
endpoint_alternating_cycle_monodromy_imported=true
endpoint_alternating_cycle_monodromy_crt_vector_closed=true
endpoint_alternating_cycle_nonzero_crt_coordinate_localized=true
endpoint_alternating_cycle_monodromy_reduced_to_pivot_phase_slip=true
endpoint_alternating_cycle_pivot_prime_phase_slip_pdec_cap_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：非零 monodromy 已被定位到最小非零 CRT prime-coordinate
的 pivot phase-slip。最新剩余为 sparse SAE、endpoint singleton、full-cycle mean、
source multiplicity 与 pivot prime phase-slip。

## 312. Stable-ladder phase-residue exchange endpoint-pivot-phase-slip-LCM-support-barrier frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_endpoint_alternating_cycle_pivot_phase_slip_lcm_support_barrier_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-lcm-support-barrier-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-lcm-support-barrier-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-lcm-support-barrier-ledger.json
```

同步结果：

```text
endpoint_pivot_phase_slip_imported=true
endpoint_pivot_prime_phase_motion_formula_closed=true
endpoint_pivot_fixed_set_lcm_replay_period_closed=true
endpoint_pivot_lcm_exceeds_support_no_fixed_replay=true
endpoint_pivot_phase_slip_reduced_to_lcm_support_barrier=true
endpoint_pivot_small_lcm_branch_excluded=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：pivot-prime phase-slip 已被压成 LCM-support 屏障。
固定 pivot 标签复现强制 `q|d`，固定 pivot-set 复现强制 `lcm(Lambda)|d`。
若 LCM 超过有限支撑宽度，则没有固定复现；否则转入小 LCM/ColumnCRT/PDEC。
最新剩余为 sparse SAE、endpoint singleton、full-cycle mean、source multiplicity、
endpoint pivot 小 LCM、nonreplay sparse 与 moving-pivot。

## 313. Stable-ladder phase-residue exchange endpoint-pivot-small-LCM-rank-pressure frontier

新增文件

```text
experiments/prime_matrix_phase_residue_exchange_active_facet_normal_cone_ray_coordinate_scalar_load_unit_normalization_unit_face_value_signed_amount_coordinate_phase_pairing_endpoint_alternating_cycle_pivot_phase_slip_small_lcm_rank_pressure_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-small-lcm-rank-pressure-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-small-lcm-rank-pressure-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-small-lcm-rank-pressure-ledger.json
```

同步结果：

```text
endpoint_pivot_small_lcm_imported=true
endpoint_pivot_distinct_prime_product_law_closed=true
endpoint_pivot_small_lcm_rank_pressure_closed=true
endpoint_pivot_two_large_carrier_sqrt_barrier_closed=true
endpoint_pivot_small_lcm_reduced_to_rank_pressure=true
endpoint_pivot_low_carrier_fixed_residue_pdec_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：endpoint pivot small-LCM 已被压成 rank-pressure
三分。`L<=W` 强制高 carrier 数满足 `r_B<=floor(log W/log B)`；取 `B=sqrt(W)`
给出两个大 pivot carrier 不可同处一个 fixed small-LCM unit。最新剩余为 sparse SAE、
endpoint singleton、full-cycle mean、source multiplicity、低 carrier fixed-residue、
低 carrier sparse、高 carrier rank-deficit、nonreplay sparse 与 moving-pivot。

## 314. Stable-ladder phase-residue exchange endpoint-pivot-low-carrier-fixed-residue-AP-envelope frontier

新增文件

```text
experiments/prime_matrix_endpoint_pivot_low_carrier_fixed_residue_ap_table_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-low-carrier-fixed-residue-ap-table-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-low-carrier-fixed-residue-ap-table-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-low-carrier-fixed-residue-ap-table-ledger.json
```

同步结果：

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

formal-to-actual 含义是：低 carrier fixed-residue 分支被压成 endpoint AP-envelope
接口。`q<P` 时，fixed residue 给出唯一行 AP 类 `t==-aP^{-1} mod q`，单
cell 命中数受 `ceil(H/q)` 控制，固定 `q` 的全 residue 总量为 `H`。`q=P`
边界项退化到已命名 ColumnCRT/endpoint singleton/source-multiplicity 出口。
最新剩余为 endpoint actual demand、AP strict gap/dense table、sparse cell、
低 carrier sparse、高 carrier rank-deficit、nonreplay、moving-pivot、endpoint
singleton、full-cycle mean、source multiplicity 与 sparse SAE。

## 315. Stable-ladder phase-residue exchange endpoint-pivot-actual-demand-source-cut frontier

新增文件

```text
experiments/prime_matrix_endpoint_pivot_actual_demand_source_cut_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-actual-demand-source-cut-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-actual-demand-source-cut-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-actual-demand-source-cut-ledger.json
```

同步结果：

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

formal-to-actual 含义是：endpoint actual-demand 下界被切到源侧。活跃 fixed-residue
demand 至少给出一个 source-tagged endpoint incidence，但单位需求不足以超过 AP
exact-envelope；必须证明源侧释放质量沿 endpoint orbit 放大，并且非循环注入同一
低 carrier AP table。最新剩余为 release-mass amplification、low-carrier payment
injection、AP strict gap/dense table、sparse cell、低 carrier sparse、高 carrier
rank-deficit、nonreplay、moving-pivot、endpoint singleton、full-cycle mean、
source multiplicity 与 sparse SAE。

## 316. Stable-ladder phase-residue exchange endpoint-pivot-release-mass-support-ladder frontier

新增文件

```text
experiments/prime_matrix_endpoint_pivot_release_mass_support_ladder_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-release-mass-support-ladder-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-release-mass-support-ladder-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-release-mass-support-ladder-ledger.json
```

同步结果：

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

formal-to-actual 含义是：release-mass amplification 被压成有限 source-support
长短阶梯。单位 source incidence 不足以形成 AP envelope gap；短支撑必须进入
endpoint singleton/full-cycle/source-multiplicity/sparse SAE，长支撑才可能转移为
low-carrier AP demand。最新剩余为 bounded support SAE、long support mass-transfer、
payment injection、AP strict gap/dense table、sparse cell、高秩、nonreplay、
moving-pivot 与 endpoint 并行出口。

## 317. Stable-ladder phase-residue exchange endpoint-pivot-low-carrier-payment-injection-lock frontier

新增文件

```text
experiments/prime_matrix_endpoint_pivot_low_carrier_payment_injection_lock_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-low-carrier-payment-injection-lock-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-low-carrier-payment-injection-lock-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-low-carrier-payment-injection-lock-ledger.json
```

同步结果：

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

formal-to-actual 含义是：payment injection 被压成同表 canonical key 锁。合法注入必须
来自 source-support actual unit，并保持同一 endpoint packet、`q`、residue、row AP
class 与窗口；跨表改变进入 switch/PDEC 或 moving-pivot，同槽重复进入 collision 或
sparse SAE。最新剩余为 same-AP-table injection lock、cross-table switch、
duplicate collision、bounded support、long support mass-transfer、AP strict gap/dense
table、sparse cell、高秩、nonreplay、moving-pivot 与 endpoint 并行出口。

## 318. Stable-ladder phase-residue exchange endpoint-pivot-duplicate-payment-slot-accounting frontier

新增文件

```text
experiments/prime_matrix_endpoint_pivot_duplicate_payment_slot_accounting_router.py
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-duplicate-payment-slot-accounting-router.md
docs/monograph/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-duplicate-payment-slot-accounting-router.json
data/prime-matrix-phase-residue-exchange-active-facet-normal-cone-ray-coordinate-scalar-load-unit-normalization-unit-face-value-signed-amount-coordinate-phase-pairing-endpoint-alternating-cycle-pivot-phase-slip-duplicate-payment-slot-accounting-ledger.json
```

同步结果：

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

formal-to-actual 含义是：同一 canonical slot 的重复支付不再能增加实际容量；第二个
及以后的 source unit 必须转为同槽 source multiplicity cap/PDEC，或作为非持久重复
进入 duplicate sparse SAE。最新剩余为 same AP table injection lock、cross-table
switch、同槽 source multiplicity、duplicate sparse SAE、bounded/long support、
AP strict gap/dense table、sparse cell、高秩、nonreplay、moving-pivot 与 endpoint
并行出口。

## 319. Stable-ladder phase-residue exchange endpoint-pivot-duplicate-same-slot-multiplicity-cap-import frontier

新增文件

```text
experiments/prime_matrix_endpoint_pivot_duplicate_same_slot_multiplicity_cap_import_router.py
docs/monograph/prime-matrix-endpoint-pivot-duplicate-same-slot-multiplicity-cap-import-router.md
docs/monograph/prime-matrix-endpoint-pivot-duplicate-same-slot-multiplicity-cap-import-router.json
data/prime-matrix-endpoint-pivot-duplicate-same-slot-multiplicity-cap-import-ledger.json
```

同步结果：

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

formal-to-actual 含义是：duplicate same-slot multiplicity 被并入已有 source-atom
multiplicity cap。same canonical slot key 已带 source atom 字段；同槽第二个及以后
source unit 不能换成新 capacity，只能作为同一 source atom 的重数异常计费。因此旧出口
`EndpointOrbitAlternatingCyclePivotPrimeDuplicateSameSlotSourceMultiplicityCapPDEC`
被替换为
`EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCap`。
最新剩余为 source-atom multiplicity cap、duplicate sparse SAE、same AP table
injection、cross-table switch、bounded/long support、AP strict gap/dense table、
sparse cell、高秩、nonreplay、moving-pivot、endpoint singleton、full-cycle mean 与
sparse-scale SAE。

## 320. Source-atom multiplicity-cap ExactUV fixed-key bridge frontier

新增文件

```text
experiments/prime_matrix_source_atom_multiplicity_cap_exactuv_fixed_key_bridge_router.py
docs/monograph/prime-matrix-source-atom-multiplicity-cap-exactuv-fixed-key-bridge-router.md
docs/monograph/prime-matrix-source-atom-multiplicity-cap-exactuv-fixed-key-bridge-router.json
data/prime-matrix-source-atom-multiplicity-cap-exactuv-fixed-key-bridge-ledger.json
```

同步结果：

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
row_column_unconditional_closed=false
```

formal-to-actual 含义是：source-atom multiplicity cap 被桥接到 ExactUV
source-rank/no-collapse 三原子。固定 source atom 大重数不再作为 endpoint 局部
独立出口；它要求 actual emitter source table、complete key partition 与 fixed-key
exact-UV local multiplicity O(1) 同时成立。最新剩余为这三个源秩原子，以及
duplicate sparse SAE、same AP table injection、cross-table switch、bounded/long
support、AP strict gap/dense table、sparse cell、高秩、nonreplay、moving-pivot、
endpoint singleton、full-cycle mean 与 sparse-scale SAE。

## 321. LPF ownership sieve source declaration frontier

新增文件

```text
experiments/prime_matrix_lpf_ownership_sieve_source_declaration_router.py
docs/monograph/prime-matrix-lpf-ownership-sieve-source-declaration-router.md
docs/monograph/prime-matrix-lpf-ownership-sieve-source-declaration-router.json
data/prime-matrix-lpf-ownership-sieve-source-declaration-ledger.json
```

同步结果：

```text
ascending_lpf_ownership_partition_proved=true
prime_count_identity_from_lpf_ownership_proved=true
quotient_condition_matches_user_sieve_proved=true
lpf_ownership_unsigned_declaration_line_closed=true
lpf_ownership_to_signed_alpha_delta_lift_proved=false
explicit_alpha_delta_primitive_constructor_rule_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：用户提出的升序筛法公式已经被写成 LPF ownership 账本。
每个合数由唯一最小素因子 `p` 归属到一个筛层，`p` 层的新筛集合等于
`{p*m<=N: m>=p, m has no prime factor < p}`；这些集合不重叠且并为全部合数。
因此 `pi(N)=N-1-sum_p LPF_p(N)` 是严格恒等式，不是统计猜测。

该恒等式关闭的是 pre-Cauchy source declaration 的 unsigned ownership 字段。它不能
直接产生 signed `alpha/delta` coefficient、orientation、local factor 或 fixed-key
ExactUV 局部重数控制。最新直接主攻为
`ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter`，并行仍需
constructor domain、row emission、failure return、actual source table、complete key、
fixed-key ExactUV、模型/Rate 与 DStructure/Rankin 验收。

## 322. LPF candidate-row map alpha-rule frontier

新增文件

```text
experiments/prime_matrix_lpf_candidate_row_map_alpha_rule_router.py
docs/monograph/prime-matrix-lpf-candidate-row-map-alpha-rule-router.md
docs/monograph/prime-matrix-lpf-candidate-row-map-alpha-rule-router.json
data/prime-matrix-lpf-candidate-row-map-alpha-rule-ledger.json
```

同步结果：

```text
alpha_side_primitive_rule_imported=true
deterministic_alpha_map_gap_imported=true
lpf_ownership_declaration_imported=true
lpf_candidate_row_emission_map_closed=true
pointwise_signed_alpha_value_table_proved=false
primitive_summand_signed_weight_expression_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：`DeterministicAlphaPrimitiveRowEmissionMapLedger`
被拆成 LPF ownership candidate-row map 与前推前 signed summand 表达式。前者已经由
最小素因子唯一分桶支付：候选 row 不需要从 payment skeleton 或零行几何反推原像。
后者仍未证明，因为 LPF candidate map 不赋 signed coefficient、orientation、local factor
或 branch weight。

最新直接主攻为
`ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward`。并行仍需
alpha source tuple domain、coefficient formula、row `(u,v)`/key/sign/local-factor 输出、
failure return、delta-side primitive rule、alpha/delta pairing、ExactUV fixed-key、
模型/Rate 与 DStructure/Rankin 验收。

## 323. Phi-recursive LPF ownership frontier

新增文件

```text
experiments/prime_matrix_phi_recursive_lpf_ownership_router.py
docs/monograph/prime-matrix-phi-recursive-lpf-ownership-router.md
docs/monograph/prime-matrix-phi-recursive-lpf-ownership-router.json
data/prime-matrix-phi-recursive-lpf-ownership-ledger.json
```

同步结果：

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

formal-to-actual 含义是：`Phi(x,p)` 递推把 LPF ownership 从集合分桶提升为可机械计算的
rough-count 账本。`Phi(x,p)` 计数 `1<=m<=x` 且无小于 `p` 的素因子的整数，包含
`m=1`；相邻素数之间满足
`Phi(x,p_k)=Phi(x,p_{k+1})+Phi(floor(x/p_k),p_k)`。于是
`c_N(p)=Phi(floor(N/p),p)-1` 精确给出 `p` 层新筛合数数，求和后得到用户公式
`pi(N)=N-1-sum_{p<=sqrt(N)}(Phi(floor(N/p),p)-1)`。

这加强了 `LPFOwnershipAlphaCandidateRowEmissionMapLedger` 的源容量基础，但仍停留在
unsigned ownership 层。它不能输出 signed coefficient、orientation、local factor 或
branch weight。最新直接主攻保持为
`ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward`，并行仍需
alpha/delta primitive rule、pairing、ExactUV fixed-key、模型/Rate、DStructure/Rankin 与
endpoint 出口。

## 324. Phi-LPF support-stripped signed kernel frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_support_stripped_signed_kernel_router.py
docs/monograph/prime-matrix-phi-lpf-support-stripped-signed-kernel-router.md
docs/monograph/prime-matrix-phi-lpf-support-stripped-signed-kernel-router.json
data/prime-matrix-phi-lpf-support-stripped-signed-kernel-ledger.json
```

同步结果：

```text
phi_recursive_lpf_ownership_imported=true
lpf_candidate_row_map_imported=true
phi_lpf_support_bijection_proved=true
support_and_capacity_components_closed=true
phi_lpf_bucket_signed_coefficient_law_proved=false
noncircular_signed_coefficient_emission_kernel_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：`NoncircularPreCauchySignedCoefficientEmissionKernel`
里的 support/capacity 部分不再是匿名缺口。Phi-LPF 账本给出唯一 support key
`(p,m)`：`p` 是最小素因子，`m` 为 p-rough，且不同 key 对应不同合数 candidate。
因此 primitive row 的无符号支撑和数量已经由
`PhiLPFPrimitiveRowSupportAndCapacityLedger` 支付。

真正剩余被压成
`PhiLPFBucketSignedCoefficientLawBeforePushforward`：必须对每个 Phi-LPF key 正向给出
signed coefficient、sign/local factor、alpha/delta 侧、branch key、`(u,v)` 输出和推前前
求和恒等式。不能再用 payment skeleton、早期零行覆盖或来源表固定点反推这些符号值。
行/列命题仍未无条件闭合。

## 325. Phi-LPF bucket signed transport frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_bucket_signed_transport_router.py
docs/monograph/prime-matrix-phi-lpf-bucket-signed-transport-router.md
docs/monograph/prime-matrix-phi-lpf-bucket-signed-transport-router.json
data/prime-matrix-phi-lpf-bucket-signed-transport-ledger.json
```

同步结果：

```text
phi_lpf_support_and_capacity_imported=true
unsigned_cofactor_split_identity_proved=true
signed_bucket_sum_partition_identity_proved=true
phi_lpf_rough_cofactor_signed_transport_law_proved=false
pointwise_phi_lpf_bucket_signed_value_table_proved=false
phi_lpf_bucket_signed_coefficient_law_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：Phi 递推可以在 signed 层保持同一支撑分裂，但只能作为有限求和
的 domain identity。设 `a_p(m)` 是 LPF owner bucket `p` 上待证明的 Cauchy 前 signed
coefficient，则 first split 给出

```text
sum_{m p-rough, 1<m<=x} a_p(m)
  = sum_{m p_next-rough, 1<m<=x} a_p(m)
    + sum_{m' p-rough, m'<=floor(x/p)} a_p(p*m')
```

这里第二项仍需要解释 `a_p(p*m')` 如何由同 formal-unit source row 正向生成。也就是说，
Phi/LPF 已经支付 support/capacity 与 signed sum partition；真正未闭合的是 cofactor
乘法下的 signed coefficient transport：orientation parity、local factor、alpha/delta side、
branch key、ExactUV 输出、非零条件和回流标签。

最新直接主攻为
`PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward`；若不走递推传输，
则必须直接提交
`PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward`。行/列命题仍未
无条件闭合。

## 328. Phi-LPF pointwise signed value table frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_pointwise_signed_value_table_frontier_router.py
docs/monograph/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.md
docs/monograph/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json
data/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-ledger.json
```

同步结果：

```text
phi_lpf_support_and_capacity_imported=true
bucket_signed_law_downstream_imported=true
unit_seed_square_base_boundary_imported=true
common_packet_self_proof_blocked=true
pointwise_phi_lpf_bucket_signed_value_table_proved=false
primitive_summand_signed_weight_expression_proved=false
seed_cycle_cut_input_proved=false
acyclic_same_set_scope_match_proved=false
new_explicit_joint_constructor_formula_artifact_present=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：LPF/Phi 精确筛法恒等式已把支撑、容量和 square-base/root 结构
完全剥离，剩余不再是“有没有对应合数桶”的问题。真正缺口是逐 Phi-LPF key 的
prepushforward signed value 表；该表若沿既有 signed-source/source-origin 展开，会回到
固定点。因此它必须作为新工件直接提交，或转入 seed cycle-cut、same-set PDEC、
new joint formula 三个破环口。

最新保留基为：

```text
(PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
 OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput
 OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact)
AND ActualEmitterSourceDomainEntropyLedger
AND ExactUVMapFixedPairPolylogFiberBoundLedger
AND PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward
AND PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

行/列命题仍未无条件闭合。

## 330. Phi-LPF rough cofactor ordered factorization coherence frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_rough_cofactor_ordered_factorization_coherence_router.py
docs/monograph/prime-matrix-phi-lpf-rough-cofactor-ordered-factorization-coherence-router.md
docs/monograph/prime-matrix-phi-lpf-rough-cofactor-ordered-factorization-coherence-router.json
data/prime-matrix-phi-lpf-rough-cofactor-ordered-factorization-coherence-ledger.json
```

同步结果：

```text
phi_lpf_support_and_capacity_imported=true
unsigned_cofactor_split_imported=true
rough_cofactor_ordered_factorization_coherence_proved=true
rough_cofactor_step_local_factor_update_law_proved=false
pointwise_phi_lpf_bucket_signed_value_table_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：`PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward`
不是 signed 系数字段，而是 LPF 支撑路径字段。固定 owner prime `p` 和 p-rough cofactor
`m` 后，最小素因子剥离给出唯一非降素因子词 `q_1,...,q_t`；每个前缀仍为 p-rough，
且对应 composite `p*q_1...q_j` 仍在 `N` 内同一 owner bucket 中。因此递推路径没有
排列歧义，也没有跨 bucket 换对象。

本层闭合的是 ordered coherence；它不能给出 signed local factor 更新。最新保留基为：

```text
(PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
 OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput
 OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact)
AND ActualEmitterSourceDomainEntropyLedger
AND ExactUVMapFixedPairPolylogFiberBoundLedger
AND PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻为：

```text
PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward
```

行/列命题仍未无条件闭合。

## 326. Phi-LPF signed transport unit-seed frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_signed_transport_unit_seed_router.py
docs/monograph/prime-matrix-phi-lpf-signed-transport-unit-seed-router.md
docs/monograph/prime-matrix-phi-lpf-signed-transport-unit-seed-router.json
data/prime-matrix-phi-lpf-signed-transport-unit-seed-ledger.json
```

同步结果：

```text
phi_minus_one_prime_row_guard_imported=true
unit_preimage_square_seed_identity_proved=true
unit_seed_or_square_base_signed_coefficient_proved=false
rough_cofactor_step_local_factor_update_law_proved=false
rough_cofactor_ordered_factorization_coherence_proved=false
phi_lpf_rough_cofactor_signed_transport_law_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：signed transport 的第一字段不是一般 step update，而是启动种子。
Phi 桶中的 `m=1` 被减去，因为它对应 prime row `p`；但 transport 整除分支中的
`m'=1` 必须产生 `(p,p)` 这个 square-base composite key。因此没有 virtual-unit seed
或 square-base signed coefficient，就无法正向生成 `a_p(p)`，后续 `a_p(qm)` 也没有
递推起点。

本层关闭的是 seed 必要性和 prime-row leak guard。真正未闭合的是：

```text
PhiLPFUnitCofactorVirtualSeedOrSquareBaseSignedCoefficientBeforePushforward
AND PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward
AND PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward
```

并行替代仍是直接提交
`PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward`。行/列命题仍未
无条件闭合。

## 329. Full-S non-AP WFD theorem-match matrix frontier

新增文件

```text
experiments/prime_matrix_fulls_nonap_wfd_theorem_match_matrix_router.py
docs/monograph/prime-matrix-fulls-nonap-wfd-theorem-match-matrix-router.md
docs/monograph/prime-matrix-fulls-nonap-wfd-theorem-match-matrix-router.json
data/prime-matrix-fulls-nonap-wfd-theorem-match-matrix-ledger.json
```

同步结果：

```text
status=fulls_nonap_wfd_primary_sources_screened_exact_contract_or_new_theorem_remains
ready_made_primary_source_match_found=false
primary_source_derivation_closed=false
unconditional_hp_closure_reached=false
next_direct_attack_target=FullSNonAPWFDKLSTheoremInput OR APSourceLift OR NCBLKActualBlockNonConcentration
```

formal-to-actual 含义是：`H_P` 顶端 strict 带已经被确认处在
`x≈P^2, length≈P≈sqrt(x)` 的 Cramer-local 尺度；Phi-LPF/LPF/CRT 公式只提供精确
组合表达，不提供正性。新的外部解析方向必须逐项匹配当前 full-S non-AP WFD 对象：

```text
object, weights, window, moduli, smoothing_projection, saving_strength, conclusion
```

矩阵结论是：BHP/Li 普通短区间、Friedlander-Iwaniec 特殊 parity-breaking 模型、
BFI AP 定理、DI/Kuznetsov 谱模板、Maynard/GPY 小间隔工具均不能直接关闭当前
未中心化、无隐藏投影、无 AP-source lift 的 full-S non-AP WFD 目标。`FullS-KLS-ext`
与目标逐项匹配，但只能作为新外部黑箱合同；若要求从主来源推出，仍需
`DIBFIPrimarySourceSpecializationProof` 或新的自守/dispersion 证明。

当前直接主攻口被收缩为：

```text
FullSNonAPWFDKLSTheoremInput
OR APSourceLift
OR NCBLKActualBlockNonConcentration
```

本层关闭的是“只引用 FI/DI/BFI/Maynard/自守 L 函数名称即可闭合”的误路线。行/列命题、
`H_P` 和三目标命题仍未无条件闭合。

## 330. Full-S theorem-match true remainder cut frontier

新增文件

```text
experiments/prime_matrix_fulls_theorem_match_true_remainder_cut_router.py
docs/monograph/prime-matrix-fulls-theorem-match-true-remainder-cut-router.md
docs/monograph/prime-matrix-fulls-theorem-match-true-remainder-cut-router.json
data/prime-matrix-fulls-theorem-match-true-remainder-cut-ledger.json
```

同步结果：

```text
status=ap_lift_filtered_ncblk_expanded_true_remainder_external_or_actual_source_core_open
unconditional_closure_reached=false
current_true_remainder_basis=(ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

formal-to-actual 含义是：上一层 theorem-match 输出的

```text
FullSNonAPWFDKLSTheoremInput OR APSourceLift OR NCBLKActualBlockNonConcentration
```

不是三个同等真剩余。已有 no-go 证书已经排除 `APSourceLift` 作为当前 non-AP、
未中心化、无投影对象的活动捷径；若新增上游 AP source identity，那本身已经是新定理输入。
`NCBLKActualBlockNonConcentration` 也不能继续保留为黑箱名：沿 BWFD/BSC/KFLS、branch
alignment、exact entropy、support range 与 source anti-atom 账本，它被展开为 actual
noncanonical full-S 源的精确因子支撑与 Type/Fourier 容量兼容。generic full-S WFD
反原子已被 moving-delta 模型反证，所以必须是 actual-source theorem，而不是形式 WFD
模板定理。

因此最新真剩余基为：

```text
(ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch
 OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

若明确接受外部黑箱合同，则对应条件版为：

```text
AcceptedFullSKLSExt
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本层的突破是删除伪剩余并把 `NCBLK` 展开到 actual source 支撑/容量核心；它仍不证明
`H_P`、行/列命题或三目标命题无条件闭合。

## 398. Phi-LPF latest constructor source-entropy payload-loop cut sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_source_entropy_payload_loop_cut_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-source-entropy-payload-loop-cut-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-source-entropy-payload-loop-cut-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-source-entropy-payload-loop-cut-sync-ledger.json
```

同步结果：

```text
latest_constructor_source_entropy_imported=true
source_entropy_atom_boundary_carried=true
phi_lpf_candidate_capacity_still_unsigned=true
strict_source_entropy_downstream_to_cycle_or_terminal=true
cycle_or_terminal_unified_to_joint_declaration=true
constructor_upstream_joint_to_payload_chain_imported=true
constructor_payload_source_entropy_loop_detected=true
raw_constructor_payload_loop_counts_as_closure=false
fresh_joint_declaration_outside_loop_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=FreshIndependentPreCauchyJointDeclarationLineOutsideConstructorPayloadLoop
```

formal-to-actual 含义是：上一层 constructor new-payload 若要成为真正工件，必须支付
`ActualPreCauchySourceDomainAbsoluteEntropyLedger`。但该接口沿 strict source-entropy
downstream 展开到 cycle-cut/terminal，再由统一前沿回到
`PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple`。
这个 joint declaration 正是当前 constructor 上游已经用于推出 built-in pairing、new payload
和 source entropy 的入口。

因此当前 constructor 内部链形成：

```text
joint declaration
-> built-in pairing
-> new payload
-> source entropy
-> cycle/terminal
-> joint declaration
```

这不是矛盾闭合，而是一个必须切掉的自证环。新的非循环主攻是提交不经过该 payload
回环的新鲜独立 joint declaration line，或走 canonical-lock、independent source bridge、
same-set PDEC/外部谱、逐点 signed table、ExactUV、complete/fixed-key、signed survival
与 row-mass/no-heavy-row 等开放出口。行/列命题仍未无条件闭合。

## 399. Phi-LPF latest constructor fresh-joint identity taxonomy sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_fresh_joint_identity_taxonomy_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-fresh-joint-identity-taxonomy-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-fresh-joint-identity-taxonomy-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-fresh-joint-identity-taxonomy-sync-ledger.json
```

同步结果：

```text
fresh_joint_declaration_imported=true
strict_joint_field_atom_imported=true
freshness_deletes_constructor_antisplit_route=true
declaration_line_requires_independent_arithmetic_identity=true
identity_statement_taxonomy_imported=true
fresh_joint_declaration_reduced_to_moving_block=true
actual_noncanonical_moving_block_spread_ncb_lk_proved=false
joint_emitter_rows_formula_proved=false
joint_word_coefficient_identity_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn
```

formal-to-actual 含义是：fresh joint declaration 不是旧 declaration line 的重命名。fresh
条件禁止再次使用 constructor 内部的 joint declaration -> built-in pairing -> payload 路线。
因此该 declaration line 若要成立，必须作为独立 noncanonical pre-Cauchy 算术恒等式陈述
进入。

既有 strict 独立恒等式分类已经说明：canonical/generic/AP/external 都不能填 strict 自足来源；
剩余实际内容是：

```text
ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn
```

该 moving-block/NC-BLK 输入仍未证明；并且即使它成立，joint rows formula、word/coefficient
identity、prepushforward identity 与 no-downstream return ledger 仍需逐项闭合。行/列命题
仍未无条件闭合。

## 400. Phi-LPF latest constructor moving-block terminal sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_moving_block_terminal_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-moving-block-terminal-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-moving-block-terminal-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-moving-block-terminal-sync-ledger.json
```

同步结果：

```text
fresh_joint_moving_block_input_imported=true
strict_actual_moving_block_router_imported=true
global_pdec_sparse_split_imported=true
precauchy_alpha_terminal_sync_agrees=true
constructor_moving_block_unnamed_exit_removed=true
actual_noncanonical_moving_block_spread_ncb_lk_proved=false
pdec_cap_or_internal_clean_kls_large_sieve_proved=false
explicit_model_gap_and_finite_dprc_ledger_proved=false
row_column_unconditional_closed=false
next_direct_attack_target=PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger
```

formal-to-actual 含义是：上一层留下的 constructor moving-block/NC-BLK 不再能作为新的
无名 actual-load 黑箱。已有 strict moving-block 路由显示：有低维签名则进
PDEC/SAE/ColumnCRT/sparse 终端，无签名则进早期零行终端包；全局 terminal split
进一步把后者接到：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve
AND ExplicitModelGapAndFiniteDPRCLedger
```

因此 constructor fresh-joint 路线的最新硬点已经与 pre-Cauchy alpha-terminal 路线对齐：
它不再是 `ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn`
本身，而是 PDEC/CleanKLS 容量门与模型余量账本。

同时仍需并行闭合 joint rows formula、word/coefficient identity、no-downstream return、
ExactUV/source entropy、signed survival、row-mass/no-heavy-row、complete/fixed key、
Rate 与 DStructure。行/列命题仍未无条件闭合。

## 401. Phi-LPF latest constructor terminal hardpoint split sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_terminal_hardpoint_split_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-terminal-hardpoint-split-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-terminal-hardpoint-split-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-terminal-hardpoint-split-sync-ledger.json
```

同步结果：

```text
constructor_terminal_gate_imported=true
pdec_clean_kls_split_imported=true
explicit_model_gap_finite_ledger_split_imported=true
high_segment_model_gap_factorization_imported=true
terminal_hardpoint_split_sync_closed=true
self_contained_kuznetsov_dls_large_sieve_inequality_proved=false
tail_harmonic_upper_0850_proved=false
tail_skeleton_lower_401_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks
```

formal-to-actual 含义是：constructor 线刚得到的

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve
AND ExplicitModelGapAndFiniteDPRCLedger
```

已经可以同步到更具体的终端硬点：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks)
AND HarmonicWindowAlpha043PGe3001Upper0850Ledger
AND DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

其中 PDEC/CleanKLS 终端门被 strict hardpoint router 拆成同集 PDEC 作用域匹配与自足
Kuznetsov/DLS 大筛原子；模型余量账本删除了 `P<2003` 有限段，并把高段账本因子化为
`H<=0.850` 的调和窗口上界与 `S>=401` 的动态粗骨架下界。

这不是终端证明：Kuznetsov/DLS、同集 PDEC scope、harmonic window、rough skeleton、
Rate 与 DStructure 仍开放；constructor 兄弟字段也仍开放。行/列命题仍未无条件闭合。

## 402. Phi-LPF latest constructor Kuznetsov terminal-cycle sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_kuznetsov_terminal_cycle_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-kuznetsov-terminal-cycle-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-kuznetsov-terminal-cycle-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-kuznetsov-terminal-cycle-sync-ledger.json
```

同步结果：

```text
constructor_kuznetsov_arm_imported=true
strict_kuznetsov_terminal_sync_imported=true
ncblk_return_to_terminal_family_imported=true
model_gap_tail_factorization_carried=true
constructor_kuznetsov_independent_exit_removed=true
self_contained_kuznetsov_dls_large_sieve_inequality_proved=false
strict_acyclic_terminal_family_proved=false
tail_harmonic_upper_0850_proved=false
tail_skeleton_lower_401_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily
```

formal-to-actual 含义是：上一层把 constructor 首攻钉到
`SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks` 后，本层继续沿既有
strict KZ/DLS 终端同步往下查。结果是 KZ-A/B/C/D 形式谱脊柱可以同步，但 KZ-E 会转成
acyclic NC-BLK/source anti-atom；该对象又不能独立停留，会回到 moving atom/global terminal。

因此 KZ/DLS 不是新的独立终端出口。constructor 线的显式 KZ 手臂回流为：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn
AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily
AND HarmonicWindowAlpha043PGe3001Upper0850Ledger
AND DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

并行破环/替代仍为：

```text
NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage
OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
```

这仍不是终局证明；terminal family、nonrecursive breaker、new-joint、PDEC scope、harmonic、
skeleton、Rate、DStructure 与 constructor 兄弟字段都仍开放。行/列命题仍未无条件闭合。

## 403. Phi-LPF latest constructor terminal-family saturation sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_terminal_family_saturation_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-terminal-family-saturation-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-terminal-family-saturation-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-terminal-family-saturation-sync-ledger.json
```

同步结果：

```text
constructor_terminal_family_target_imported=true
strict_terminal_family_latest_saturation_imported=true
nonrecursive_breaker_cycle_imported=true
seed_cycle_cut_saturation_imported=true
pdec_scope_branch_internal_saturation_imported=true
global_crt_saturation_agrees=true
constructor_terminal_family_unnamed_exit_removed=true
strict_acyclic_terminal_family_proved=false
new_explicit_joint_constructor_formula_artifact_present=false
row_column_unconditional_closed=false
next_primary_attack_target=NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
```

formal-to-actual 含义是：上一层 KZ/DLS 回流留下的
`PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily`
不能继续作为 constructor 线的粗终端黑箱。strict 终端家族饱和证书已把三手臂全部展开：
canonical-lock 只给 scoped canonical case，direct PDEC 卡在同集作用域匹配，CleanKLS/DLS
回到终端循环。继续下钻 nonrecursive breaker 与 seed-cycle-cut，也回到 signed-source 固定点。

因此 constructor 线的最新显式保留基压成：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn
AND (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
     OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact)
AND HarmonicWindowAlpha043PGe3001Upper0850Ledger
AND DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

内部主攻现在是新的显式 joint alpha/delta 公式；PDEC same-set scope 仍可作为新的 scope
证书或外部输入保留。source seed、harmonic、skeleton、Rate、DStructure 与 constructor
兄弟字段仍开放。行/列命题仍未无条件闭合。

## 404. Phi-LPF latest constructor terminal new-joint macrocycle sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_terminal_new_joint_macrocycle_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-terminal-new-joint-macrocycle-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-terminal-new-joint-macrocycle-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-terminal-new-joint-macrocycle-sync-ledger.json
```

同步结果：

```text
terminal_family_new_joint_target_imported=true
new_joint_to_declaration_line_imported=true
declaration_antisplit_to_builtin_imported=true
builtin_macrocycle_cut_imported=true
source_payload_loop_carried=true
mandatory_signed_side_gate_imported=true
new_joint_coarse_artifact_removed=true
row_level_clean_core_origin_generation_table_proved=false
nonzero_signed_row_survival_proved=false
same_formal_unit_row_mass_normalization_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands
```

formal-to-actual 含义是：上一层留下的
`NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact` 不能作为换名后的自由出口。
已有 constructor new-joint 下游显示：new-joint 的第一生产性字段是 pre-Cauchy joint
declaration line；普通 declaration 回到 signed-source 固定点，anti-split 路线压到
built-in signed pairing。再沿 built-in 下钻会形成

```text
built-in pairing
-> new payload
-> alpha kernel
-> moving atom
-> pointwise signed table
-> origin identity
-> triad
-> joint declaration
-> built-in pairing
```

的 constructor signed 宏循环。source-entropy/payload 线也已登记为
`declaration -> payload -> source entropy -> declaration` 自证环。

因此本层删除 new-joint 粗原子，把内部主攻压到：

```text
RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands
AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
```

并在 constructor 线中保留：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn
AND (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
     OR row-level/signed-side gate)
AND HarmonicWindowAlpha043PGe3001Upper0850Ledger
AND DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

PDEC scope、canonical lock、independent bridge、ExactUV、key、Rate、DStructure 与 constructor
兄弟字段仍开放。行/列命题仍未无条件闭合。

## 405. Phi-LPF latest constructor row-level signed-source fixed-point sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_row_level_signed_source_fixed_point_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-row-level-signed-source-fixed-point-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-row-level-signed-source-fixed-point-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-row-level-signed-source-fixed-point-sync-ledger.json
```

同步结果：

```text
latest_constructor_row_level_target_imported=true
row_table_to_seed_emitter_imported=true
signed_source_fixed_point_cut_imported=true
seed_coordinate_source_cycle_guard_imported=true
reverse_payment_and_zero_row_recovery_blocked=true
row_level_coarse_target_removed=true
row_level_clean_core_origin_generation_table_proved=false
noncircular_signed_coefficient_emission_kernel_proved=false
nonzero_signed_row_survival_proved=false
same_formal_unit_row_mass_normalization_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows
```

formal-to-actual 含义是：latest constructor 已经不能停在
`RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands`
这个表名。strict row-level 证书说明，该表必须由无环 pre-Cauchy seed signed-row
emitter 正向产生；但 signed-source fixed-point 证书与 seed coordinate/source guard
显示，当前内部展开会沿 basis word、coordinate、assignment、value map 和 origin identity
回到同一 row-level 表。

因此 row-level 表名被删除为粗口，最新内部主攻同步为：

```text
NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows
```

constructor 线的 signed-side gate 相应改写为：

```text
NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows
AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
```

PDEC scope、canonical lock、independent bridge、terminal WFD、direct pointwise table、ExactUV、
key、harmonic/skeleton、Rate、DStructure 与 constructor 兄弟字段仍开放。行/列命题仍未
无条件闭合。

## 406. Phi-LPF latest constructor noncircular kernel bucket signed-law sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_noncircular_kernel_bucket_signed_law_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-noncircular-kernel-bucket-signed-law-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-noncircular-kernel-bucket-signed-law-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-noncircular-kernel-bucket-signed-law-sync-ledger.json
```

同步结果：

```text
latest_constructor_noncircular_kernel_target_imported=true
strict_kernel_first_field_imported=true
phi_lpf_support_stripping_imported=true
phi_lpf_support_and_capacity_closed=true
unsigned_phi_lpf_bucket_cannot_emit_signed_coefficient=true
noncircular_kernel_coarse_target_removed=true
noncircular_signed_coefficient_emission_kernel_proved=false
phi_lpf_bucket_signed_coefficient_law_proved=false
nonzero_signed_row_survival_proved=false
same_formal_unit_row_mass_normalization_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFBucketSignedCoefficientLawBeforePushforward
```

formal-to-actual 含义是：latest constructor 的非循环 signed emission kernel 不能继续作为
未拆粗口。strict kernel 纪律要求 Cauchy 前 actual noncanonical emitter declaration，且不得
读取 downstream payment/Phi、row table 或零行覆盖。Phi-LPF 支撑剥离证书已经把其中的
找行、数行、owner layer 和大素数零质量全部支付到最小素因子桶 `(p,m)`。

因此 constructor 线的 signed-side gate 进一步改写为：

```text
PhiLPFBucketSignedCoefficientLawBeforePushforward
AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
```

最新内部主攻为：

```text
PhiLPFBucketSignedCoefficientLawBeforePushforward
```

这一步只说明 LPF/Phi 精确桶已经完成无符号支撑职责；它不生成 signed coefficient、sign/local
factor、branch key 或 prepushforward alpha/delta 求和恒等式。PDEC scope、canonical lock、
independent bridge、terminal WFD、direct pointwise table、ExactUV/key、harmonic/skeleton、
Rate、DStructure 与 constructor 兄弟字段仍开放。行/列命题仍未无条件闭合。

## 407. Phi-LPF latest constructor bucket transport-stack rebase sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_bucket_transport_stack_rebase_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-bucket-transport-stack-rebase-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-bucket-transport-stack-rebase-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-bucket-transport-stack-rebase-sync-ledger.json
```

同步结果：

```text
latest_constructor_bucket_signed_law_imported=true
existing_transport_stack_imported=true
step_update_edge_multiplier_imported=true
source_packet_cycle_guard_imported=true
signed_side_gates_carried=true
bucket_transport_stack_rebased=true
edge_signed_multiplier_table_proved=false
alpha_row_anchor_phase_emission_formula_proved=false
independent_noncanonical_arithmetic_identity_proved=false
same_unit_exactuv_rank_multiplicity_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward
```

formal-to-actual 含义是：上一层最新 constructor kernel-bucket 证书得到的
`PhiLPFBucketSignedCoefficientLawBeforePushforward` 已重新接到既有 transport stack。
若不直接提交逐 Phi-LPF bucket signed value table，则 bucket signed law 必须经过
rough-cofactor transport；ordered path、unit/square-base 边界和 common packet 自证环
已经在旧证书中处理。

最新窄口压为：

```text
PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward
```

并行 source 三原子仍为：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger
AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
```

signed survival、row-mass/no-heavy-row、PDEC scope、ExactUV/key、harmonic/skeleton、Rate、
DStructure 与 constructor 兄弟字段仍开放。行/列命题仍未无条件闭合。

## 408. Phi-LPF latest constructor edge multiplier slab rebase sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_edge_multiplier_slab_rebase_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-edge-multiplier-slab-rebase-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-edge-multiplier-slab-rebase-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-edge-multiplier-slab-rebase-sync-ledger.json
```

同步结果：

```text
latest_rebased_edge_multiplier_imported=true
existing_constructor_edge_slab_reusable=true
first_edge_slab_router_imported=true
phi_fiber_unsigned_only_guard_imported=true
semiprime_diagonal_downstream_available=true
edge_multiplier_slab_rebased=true
semiprime_first_edge_signed_seed_table_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward
```

formal-to-actual 含义是：最新 rebase 后的
`PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward` 可接入既有 first-edge
slab 证书。逐 edge signed multiplier 表按 LPF ordered path 唯一拆成：

```text
PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward
AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
```

Phi fiber 只支付第一边 `(p,q)` 的 q-rough continuation occurrence mass，不能生成 signed seed、
local factor、orientation、branch key 或 ExactUV payload。最新主攻变成 semiprime first-edge
signed seed table；internal prime-adjoin transition law 是配套必需。source 三原子、signed
survival、row-mass/no-heavy-row、PDEC scope、ExactUV/key、harmonic/skeleton、Rate 与
DStructure 仍开放。行/列命题仍未无条件闭合。

## 409. Phi-LPF latest constructor semiprime seed diagonal rebase sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_semiprime_seed_diagonal_rebase_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-semiprime-seed-diagonal-rebase-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-semiprime-seed-diagonal-rebase-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-semiprime-seed-diagonal-rebase-sync-ledger.json
```

同步结果：

```text
latest_rebased_first_seed_imported=true
existing_constructor_semiprime_diagonal_reusable=true
semiprime_diagonal_router_imported=true
diagonal_private_escape_removed=true
common_packet_cycle_guard_carried_forward=true
semiprime_seed_diagonal_rebased=true
offdiagonal_ordered_semiprime_signed_seed_table_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward
```

formal-to-actual 含义是：最新 rebase 后的
`PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward` 已接回既有 semiprime
diagonal/offdiagonal 拆分。`p=q` diagonal square-base lane 无私有 signed 出口，只能由
source-packet 三原子承接：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger
AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
```

因此最新 seed-side 主攻推进到：

```text
PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward
```

`PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward` 仍是配套必需。signed
survival、row-mass/no-heavy-row、PDEC scope、ExactUV/key、harmonic/skeleton、Rate 与
DStructure 仍开放。行/列命题仍未无条件闭合。

## 410. Phi-LPF latest constructor offdiagonal seed tuple rebase sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_offdiagonal_seed_tuple_rebase_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-offdiagonal-seed-tuple-rebase-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-offdiagonal-seed-tuple-rebase-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-offdiagonal-seed-tuple-rebase-sync-ledger.json
```

同步结果：

```text
latest_rebased_offdiagonal_seed_imported=true
existing_constructor_offdiagonal_tuple_reusable=true
offdiagonal_tuple_fields_router_imported=true
offdiagonal_source_tuple_bijection_synced=true
offdiagonal_phi_tail_fiber_mass_synced=true
lpf_phi_unsigned_scope_exhausted_for_offdiag_seed=true
source_atoms_carried_forward=true
offdiagonal_seed_tuple_rebased=true
offdiagonal_signed_seed_formula_proved=false
offdiagonal_orientation_parity_law_proved=false
offdiagonal_exactuv_fixed_pair_return_ledger_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward
```

formal-to-actual 含义是：最新 rebase 后的
`PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward` 已接入既有
tuple-fields 证书。LPF/Phi 桶恒等式关闭了 owner prime、first rough prime、`q`-rough tail
与 Phi tail-fiber mass 的无符号账；它不能推出 signed seed、orientation parity、branch side
或 ExactUV return。

最新直接主攻推进到：

```text
PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward
```

配套仍需：

```text
PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
```

source 三原子、signed survival、row-mass/no-heavy-row、PDEC scope、ExactUV/key、
harmonic/skeleton、Rate 与 DStructure 仍开放。行/列命题仍未无条件闭合。

## 411. Phi-LPF latest constructor pure-pair atom rebase sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_pure_pair_atom_rebase_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-pure-pair-atom-rebase-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-pure-pair-atom-rebase-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-pure-pair-atom-rebase-sync-ledger.json
```

同步结果：

```text
latest_rebased_source_tuple_signed_formula_imported=true
existing_constructor_pure_pair_reusable=true
pure_pair_atom_router_imported=true
pure_pair_atom_bijection_synced=true
tail_lift_phi_minus_one_synced=true
tail_lift_no_new_first_seed_closed=true
source_atoms_carried_forward=true
pure_pair_atom_rebased=true
pure_semiprime_pair_signed_seed_atom_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward
```

formal-to-actual 含义是：最新 rebase 后的
`PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward` 已接入既有
pure-pair atom 证书。`tail=1` 是每个 ordered `(p,q)` 的唯一 pure semiprime first seed atom；
`tail>1` 的质量为 `Phi(floor(N/(p*q)),q)-1`，不是新 first seed，只能进入 internal transition
lift。

最新直接主攻推进到：

```text
PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward
```

orientation/branch-side、offdiagonal ExactUV return、internal prime-adjoin transition、source
三原子、signed survival、row-mass/no-heavy-row、PDEC scope、ExactUV/key、harmonic/skeleton、
Rate 与 DStructure 仍开放。行/列命题仍未无条件闭合。

## 412. Phi-LPF latest constructor pure-pair Ferrers support rebase sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_pure_pair_ferrers_support_rebase_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-pure-pair-ferrers-support-rebase-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-pure-pair-ferrers-support-rebase-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-pure-pair-ferrers-support-rebase-sync-ledger.json
```

同步结果：

```text
latest_rebased_pure_pair_atom_imported=true
existing_constructor_ferrers_reusable=true
ferrers_support_router_imported=true
ferrers_support_and_degree_ledger_closed=true
ferrers_support_does_not_emit_signed_kernel=true
source_atoms_carried_forward=true
pure_pair_ferrers_support_rebased=true
two_prime_signed_interaction_kernel_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward
```

formal-to-actual 含义是：最新 rebase 后的
`PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward` 已接入 Ferrers support
证书。pure pair 支撑由 `p<q<=N/p`、prime table 与 `floor(N/p)` 完全支付；left/right degree
和 edge 总数都不是剩余 signed 信息。

最新直接主攻推进到：

```text
PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward
```

orientation/branch-side、offdiagonal ExactUV return、internal prime-adjoin transition、source
三原子、signed survival、row-mass/no-heavy-row、PDEC scope、ExactUV/key、harmonic/skeleton、
Rate 与 DStructure 仍开放。行/列命题仍未无条件闭合。

## 413. Phi-LPF latest constructor two-prime no-swap rebase sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_two_prime_no_swap_rebase_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-two-prime-no-swap-rebase-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-two-prime-no-swap-rebase-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-two-prime-no-swap-rebase-sync-ledger.json
```

同步结果：

```text
latest_rebased_two_prime_kernel_imported=true
existing_constructor_no_swap_reusable=true
no_swap_router_imported=true
lpf_owner_ordered_no_swap_closed=true
product_symmetry_does_not_emit_signed_kernel=true
source_atoms_carried_forward=true
two_prime_no_swap_rebased=true
edge_local_two_prime_signed_formula_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward
```

formal-to-actual 含义是：最新 rebase 后的
`PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward` 已接入 ordered no-swap
证书。LPF owner source domain 只保留 canonical ordered edge `(p,q)` 且 `p<q`；交换对称
`pq=qp` 只识别同一个整数，不能供应反向 signed source row 或 cancellation partner。

最新直接主攻推进到：

```text
PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward
```

orientation/branch-side、offdiagonal ExactUV return、internal prime-adjoin transition、source
三原子、signed survival、row-mass/no-heavy-row、PDEC scope、ExactUV/key、harmonic/skeleton、
Rate 与 DStructure 仍开放。行/列命题仍未无条件闭合。

## 414. Phi-LPF latest constructor edge-local field-cut rebase sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_edge_local_field_cut_rebase_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-edge-local-field-cut-rebase-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-edge-local-field-cut-rebase-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-edge-local-field-cut-rebase-sync-ledger.json
```

同步结果：

```text
latest_rebased_edge_local_formula_imported=true
existing_constructor_field_cut_reusable=true
field_cut_router_imported=true
closed_unsigned_edge_fields_exhausted=true
unsigned_label_does_not_emit_signed_atom=true
source_atoms_carried_forward=true
edge_local_field_cut_rebased=true
signed_atom_field_table_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward
```

formal-to-actual 含义是：最新 rebase 后的
`PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward` 已接入
edge-local field-cut 证书。canonical edge 的 owner、product、LPF bucket、Ferrers
rank/degree 与 multiplicity-one label 都已由无符号账本支付；这些 closed unsigned
fields 不会生成 signed value、local factor、orientation、ExactUV return 或 source-row
coefficient。

最新直接主攻推进到：

```text
PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward
```

orientation/branch-side、offdiagonal ExactUV return、internal prime-adjoin transition、source
三原子、signed survival、row-mass/no-heavy-row、PDEC scope、ExactUV/key、harmonic/skeleton、
Rate 与 DStructure 仍开放。行/列命题仍未无条件闭合。

## 415. Phi-LPF latest constructor signed atom trace rebase sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_signed_atom_trace_rebase_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-signed-atom-trace-rebase-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-signed-atom-trace-rebase-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-signed-atom-trace-rebase-sync-ledger.json
```

同步结果：

```text
latest_rebased_signed_atom_fields_imported=true
existing_constructor_signed_atom_trace_reusable=true
trace_sync_router_imported=true
closed_unsigned_labels_carried=true
same_trace_key_and_named_return_matrix_synced=true
constructor_source_atoms_carried_forward=true
constructor_side_gates_not_paid_by_trace_sync=true
trace_self_proof_cycle_cut_synced=true
signed_atom_trace_rebased=true
new_primitive_payload_or_trace_artifact_present=false
edge_local_signed_atom_fields_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact
```

formal-to-actual 含义是：最新 rebase 后的
`PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward` 已接入
signed atom trace-sync。无符号 edge label 只给输入域；signed value、local factor、
orientation、alpha/delta side、ExactUV fixed pair 与 source row 必须同属一个
pre-Cauchy trace key。匿名失败已被命名 return 矩阵吸收。

最新直接主攻推进到：

```text
NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact
```

terminal descent、same-set PDEC、逐点 Phi-LPF signed table、source 三原子、signed survival、
row-mass/no-heavy-row、complete/fixed key、ExactUV、模型、Rate 与 DStructure 仍开放。
行/列命题仍未无条件闭合。

## 416. Phi-LPF latest constructor new-payload source-atom alignment rebase sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_new_payload_source_atom_alignment_rebase_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-new-payload-source-atom-alignment-rebase-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-new-payload-source-atom-alignment-rebase-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-new-payload-source-atom-alignment-rebase-sync-ledger.json
```

同步结果：

```text
latest_rebased_new_payload_imported=true
existing_constructor_new_payload_alignment_reusable=true
constructor_source_and_side_gates_carried=true
unsigned_labels_cannot_pay_payload=true
signed_lane_cycle_cut_carried=true
strict_new_payload_alignment_imported=true
new_payload_reduced_to_source_rank_atom=true
independent_new_payload_terminal_present=false
constructor_source_atoms_carried_forward=true
constructor_row_mass_and_survival_still_open=true
actual_source_domain_entropy_proved=false
complete_primitive_emitter_key_partition_proved=false
fixed_key_exact_uv_local_multiplicity_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=ActualPreCauchySourceDomainAbsoluteEntropyLedger
```

formal-to-actual 含义是：最新 rebase 后的
`NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact` 已接入 strict source-atom alignment。
无符号 label 与 signed-lane trace 不能生产新 payload；若 new-payload 要成为真正新工件，
必须携带 actual pre-Cauchy source-rank/no-collapse 三原子。

最新直接主攻推进到：

```text
ActualPreCauchySourceDomainAbsoluteEntropyLedger
```

source 三原子、row-mass/no-heavy-row、signed survival、complete key、fixed-key ExactUV local
multiplicity、terminal descent、same-set PDEC、逐点 Phi-LPF signed table、ExactUV、模型、
Rate 与 DStructure 仍开放。行/列命题仍未无条件闭合。

## 417. Phi-LPF latest constructor source-entropy payload-loop cut rebase sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_source_entropy_payload_loop_cut_rebase_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-source-entropy-payload-loop-cut-rebase-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-source-entropy-payload-loop-cut-rebase-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-source-entropy-payload-loop-cut-rebase-sync-ledger.json
```

同步结果：

```text
latest_rebased_source_entropy_imported=true
existing_constructor_payload_loop_cut_reusable=true
source_entropy_atom_boundary_carried=true
phi_lpf_candidate_capacity_still_unsigned=true
strict_source_entropy_downstream_to_cycle_or_terminal=true
cycle_or_terminal_unified_to_joint_declaration=true
constructor_upstream_joint_to_payload_chain_imported=true
constructor_payload_source_entropy_loop_detected=true
raw_constructor_payload_loop_counts_as_closure=false
fresh_joint_declaration_outside_loop_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=FreshIndependentPreCauchyJointDeclarationLineOutsideConstructorPayloadLoop
```

formal-to-actual 含义是：最新 rebase 后的
`ActualPreCauchySourceDomainAbsoluteEntropyLedger` 沿 strict source-entropy downstream 与
cycle-cut/terminal/PDEC 统一前沿展开后，会回到
`PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple`。
该 joint declaration 又是 constructor 上游推出 built-in pairing、new payload 与 source entropy
的入口，因此当前 constructor 内部路线形成 payload/source-entropy 自证环，不能作为非循环闭合。

最新直接主攻推进到：

```text
FreshIndependentPreCauchyJointDeclarationLineOutsideConstructorPayloadLoop
```

canonical-lock、independent source bridge、same-set PDEC、逐点 Phi-LPF signed table、complete/fixed
key、signed survival、row-mass/no-heavy-row、ExactUV、模型、Rate 与 DStructure 仍开放。
行/列命题仍未无条件闭合。

## 418. Phi-LPF latest constructor fresh-joint identity taxonomy rebase sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_fresh_joint_identity_taxonomy_rebase_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-fresh-joint-identity-taxonomy-rebase-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-fresh-joint-identity-taxonomy-rebase-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-fresh-joint-identity-taxonomy-rebase-sync-ledger.json
```

同步结果：

```text
latest_rebased_fresh_joint_declaration_imported=true
existing_fresh_joint_identity_taxonomy_reusable=true
strict_joint_field_atom_imported=true
freshness_deletes_constructor_antisplit_route=true
declaration_line_requires_independent_arithmetic_identity=true
identity_statement_taxonomy_imported=true
fresh_joint_declaration_reduced_to_moving_block=true
actual_noncanonical_moving_block_spread_ncb_lk_proved=false
joint_emitter_rows_formula_proved=false
joint_word_coefficient_identity_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn
```

formal-to-actual 含义是：fresh declaration 不能作为新的匿名黑箱停留。fresh 条件删除
constructor joint-declaration -> built-in -> payload 旧路线后，若 declaration line 要成立，
必须作为独立 noncanonical pre-Cauchy 算术恒等式陈述进入；既有 strict 分类把该剩余压到
actual noncanonical moving-block spread/NC-BLK。

最新直接主攻推进到：

```text
ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn
```

joint rows formula、word/coefficient identity、no-downstream return ledger、signed survival、row-mass、
complete/fixed key、ExactUV、模型、Rate 与 DStructure 仍开放。行/列命题仍未无条件闭合。

## 419. Phi-LPF latest constructor moving-block terminal rebase sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_moving_block_terminal_rebase_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-moving-block-terminal-rebase-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-moving-block-terminal-rebase-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-moving-block-terminal-rebase-sync-ledger.json
```

同步结果：

```text
latest_rebased_fresh_joint_moving_block_input_imported=true
existing_constructor_moving_block_terminal_reusable=true
strict_actual_moving_block_router_imported=true
global_pdec_sparse_split_imported=true
precauchy_alpha_terminal_sync_agrees=true
constructor_moving_block_unnamed_exit_removed=true
actual_noncanonical_moving_block_spread_ncb_lk_proved=false
pdec_cap_or_internal_clean_kls_large_sieve_proved=false
explicit_model_gap_and_finite_dprc_ledger_proved=false
row_column_unconditional_closed=false
next_direct_attack_target=PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger
```

formal-to-actual 含义是：上一层留下的
`ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn`
不能作为 constructor fresh-joint 路线的新无名终端。strict moving-block 路由、旧 constructor
moving-block terminal 证书、global PDEC/sparse terminal split 与 pre-Cauchy alpha-terminal
同步层给出同一结论：moving-block/NC-BLK 必须继续落到 PDEC/CleanKLS 容量门，并同时保留显式模型余量与有限
DPRC 账本。

最新直接主攻推进到：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger
```

joint rows、word/coefficient identity、no-downstream return、source entropy/ExactUV、
signed survival、row-mass/no-heavy-row、complete/fixed key、Rate 与 DStructure 仍开放。
行/列命题仍未无条件闭合。

## 420. Phi-LPF latest constructor terminal hardpoint/high-model rebase sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_terminal_hardpoint_high_model_rebase_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-terminal-hardpoint-high-model-rebase-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-terminal-hardpoint-high-model-rebase-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-terminal-hardpoint-high-model-rebase-sync-ledger.json
```

同步结果：

```text
latest_constructor_terminal_pair_imported=true
strict_pdec_clean_kls_terminal_split_imported=true
explicit_model_gap_finite_high_split_imported=true
finite_dprc_segment_closed=true
moving_block_dprc_compatibility_closed=true
wide_terminal_model_pair_removed=true
direct_pdec_scope_match_proved=false
self_contained_kuznetsov_dls_large_sieve_inequality_proved=false
high_segment_model_gap_alpha043_c3_analytic_ledger_proved=false
row_column_unconditional_closed=false
next_direct_attack_target=SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks AND HighSegmentModelGapAlpha043C3AnalyticLedger
```

formal-to-actual 含义是：宽口径
`PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger`
不再作为最新 constructor 前沿的无名硬点保留。strict PDEC/CleanKLS 终端硬点路由把前半拆成
`AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate` 或
`SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks`；strict global scope
把模型账本拆成已闭合的 `P<2003` 有限 DPRC 段与仍开放的
`HighSegmentModelGapAlpha043C3AnalyticLedger`。

最新直接主攻推进到：

```text
SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks AND HighSegmentModelGapAlpha043C3AnalyticLedger
```

PDEC 作用域匹配、joint rows、word/coefficient identity、no-downstream return、
source entropy/ExactUV、signed survival、row-mass/no-heavy-row、complete/fixed key、Rate
与 DStructure 仍开放。行/列命题仍未无条件闭合。

## 421. Phi-LPF latest constructor Kuznetsov/high-model rebase sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_kuznetsov_high_model_rebase_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-kuznetsov-high-model-rebase-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-kuznetsov-high-model-rebase-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-kuznetsov-high-model-rebase-sync-ledger.json
```

同步结果：

```text
latest_constructor_kuznetsov_high_model_pair_imported=true
strict_kuznetsov_abcd_spine_imported=true
kze_reduced_to_ncblk_antiatom=true
constructor_kuznetsov_cycle_import_agrees=true
strict_high_model_tail_update_imported=true
kuznetsov_high_model_wide_pair_removed=true
self_contained_kuznetsov_dls_large_sieve_inequality_proved=false
acyclic_ncblk_actual_block_nonconcentration_proved=false
self_contained_beta_sieve_appendix_proved=false
beta_sieve_main_coefficient_99_proved=false
exact_residue_weighted_floor_sawtooth_bound_proved=false
row_column_unconditional_closed=false
next_direct_attack_target=AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom AND SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix_THEN_ExactSawtooth
```

formal-to-actual 含义是：`SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks`
不能作为 constructor 路线的独立无名出口。KZ-A/B/C/D 形式谱脊柱已经同步，真正未证的
KZ-E 对数节省被 strict 原子路由压到
`AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom`。同时
`HighSegmentModelGapAlpha043C3AnalyticLedger` 被高段尾路由压到自足 beta-sieve 权重、
99% 主系数误差与 exact sawtooth 余项界。

最新直接主攻推进到：

```text
AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom AND SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix_THEN_ExactSawtooth
```

PDEC 作用域匹配、终端家族、nonrecursive breaker/new-joint、joint rows、source/ExactUV、
signed survival、row-mass、complete/fixed key、Rate 与 DStructure 仍开放。
行/列命题仍未无条件闭合。

## 422. Phi-LPF latest constructor post-KZ-E source-admission rebase sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_post_kze_source_admission_rebase_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-post-kze-source-admission-rebase-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-post-kze-source-admission-rebase-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-post-kze-source-admission-rebase-sync-ledger.json
```

同步结果：

```text
latest_constructor_ncblk_tail_imported=true
strict_ncblk_to_source_root_imported=true
forward_source_root_terminal_cycle_imported=true
post_source_root_pdec_saturation_imported=true
post_pdec_new_joint_noncycle_imported=true
post_new_joint_kz_nocycle_imported=true
post_kze_source_admission_imported=true
phi_lpf_unsigned_bucket_discipline_preserved=true
high_model_tail_beta_sawtooth_reapplied=true
latest_internal_route_reduced_to_a1_source_admission=true
a1_clean_branch_canonical_source_admission_proved=false
self_contained_beta_sieve_appendix_proved=false
beta_sieve_main_coefficient_99_proved=false
exact_residue_weighted_floor_sawtooth_bound_proved=false
row_column_unconditional_closed=false
next_direct_attack_target=A1CleanBranchCanonicalSourceAdmission AND SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix_THEN_ExactSawtooth
```

formal-to-actual 含义是：上一层留下的 `NCBLK/source anti-atom + 高段尾包`
不能作为 latest constructor 的最终无名硬点。strict source-root、PDEC、new-joint、
KZ no-cycle 与 post-KZ-E source-bridge 链显示，当前内部非循环 KZ-E 方向若不接受外部
no-projection DI/BFI/Kuznetsov 证书，就必须证明
`A1CleanBranchCanonicalSourceAdmission`。LPF/Phi 桶恒等式在本层只作为无符号
owner/support/capacity 纪律使用：它能排除从 bucket 容量反推 signed source 的捷径，
但不能生成 canonical source admission。

最新直接主攻推进到：

```text
A1CleanBranchCanonicalSourceAdmission AND SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix_THEN_ExactSawtooth
```

条件保留线包括外部 no-projection KZ、direct PDEC scope、新 joint、KZ-E direct、
Phi-LPF signed bucket table。beta-sieve 附录、99% 主系数、exact sawtooth、Rate 与
DStructure 仍开放。行/列命题仍未无条件闭合。

## 423. Phi-LPF latest constructor post-source-admission macrocycle rebase sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_post_source_admission_macrocycle_rebase_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-post-source-admission-macrocycle-rebase-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-post-source-admission-macrocycle-rebase-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-post-source-admission-macrocycle-rebase-sync-ledger.json
```

同步结果：

```text
latest_constructor_a1_source_admission_imported=true
a1_source_admission_absorbed_as_branch_boundary=true
canonical_branch_statement_coverage_imported=true
post_source_admission_macrocycle_imported=true
outside_cycle_break_basis_imported=true
threshold_finite_verification_boundary_preserved=true
ten_percent_tail_still_needs_beta_and_sawtooth=true
latest_internal_route_reduced_to_outside_cycle_break=true
acyclic_seed_cycle_cut_primitive_basis_and_coefficient_source_input_proved=false
self_contained_beta_sieve_appendix_proved=false
beta_sieve_main_coefficient_99_proved=false
exact_residue_weighted_floor_sawtooth_bound_proved=false
row_column_unconditional_closed=false
next_direct_attack_target=AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput AND SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix_THEN_ExactSawtooth
```

formal-to-actual 含义是：`A1CleanBranchCanonicalSourceAdmission` 已被吸收为 scoped
分支边界纪律。canonical RIW/Buchstab 分支内部链条已闭合，但 generic/noncanonical
宽口径不能被静默升级；沿 A1/T1/signed-lift/PDEC/new-joint/KZ/KZ-E 继续下钻只形成宏循环。
因此非循环推进必须提交循环外输入：

```text
AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput
OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
OR NewPrimitiveJointPayloadArtifactOutsideSignedLaneCycle
OR ExactExternalDIBFIKuznetsovNoProjectionCertificate_FOR_NONCIRCULAR_KZ_ONLY
```

关于“充分大阈值证明后再做有限验证”的两次路线：本层保留其正确边界。它们可用于关闭
已登记有限桥或把有限段从活动前沿移除，但不能替代 \(P\ge 100000\) 尾段所需的
自足 Rosser-Iwaniec beta-sieve 构造、99% 主系数误差与 exact sawtooth 余项界。

最新直接主攻推进到：

```text
AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput AND SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix_THEN_ExactSawtooth
```

PDEC scope、新 primitive/payload、外部 no-projection KZ、Rate、DStructure 与
source/ExactUV 相关账本仍开放。行/列命题仍未无条件闭合。

## 424. Phi-LPF latest constructor cycle-cut/antisplit downstream rebase sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_cyclecut_antisplit_downstream_rebase_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-cyclecut-antisplit-downstream-rebase-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-cyclecut-antisplit-downstream-rebase-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-cyclecut-antisplit-downstream-rebase-sync-ledger.json
```

同步结果：

```text
latest_constructor_seed_cyclecut_imported=true
seed_cycle_cut_branch_saturated=true
cyclecut_terminal_unified_to_joint_declaration=true
ordinary_joint_route_rejected_by_antisplit_downstream=true
atomic_rows_reduced_to_builtin_pairing=true
exactuv_entropy_fiber_split_imported=true
threshold_finite_verification_boundary_preserved=true
beta_sieve_sawtooth_tail_still_open=true
latest_internal_route_reduced_to_builtin_pairing_and_exactuv=true
built_in_signed_pairing_proved=false
actual_emitter_source_domain_entropy_proved=false
exact_uv_map_fixed_pair_polylog_fiber_bound_proved=false
self_contained_beta_sieve_appendix_proved=false
exact_residue_weighted_floor_sawtooth_bound_proved=false
row_column_unconditional_closed=false
next_direct_attack_target=BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows AND ActualEmitterSourceDomainEntropyLedger_AND_ExactUVMapFixedPairPolylogFiberBoundLedger AND SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix_THEN_ExactSawtooth
```

formal-to-actual 含义是：`AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput`
不能作为独立出口。seed-cycle-cut 已饱和到 PDEC/new-joint；cycle-cut、terminal descent
与 PDEC 内部分支统一到 pre-Cauchy joint declaration line；普通 joint declaration /
constructor 又回到 signed-source 固定点。因此真正下游首口是反分裂 atomic rows 的
内置 signed coefficient/pairing 闭式。ExactUV bounded incidence 并行拆成
actual source-domain entropy 与 fixed-pair polylog fiber bound。

最新直接主攻推进到：

```text
BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
AND ActualEmitterSourceDomainEntropyLedger
AND ExactUVMapFixedPairPolylogFiberBoundLedger
AND SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix_THEN_ExactSawtooth
```

高阈值加有限验证仍只关闭有限桥；\(P\ge100000\) 尾段仍需 beta-sieve 构造、99% 主系数和
exact sawtooth。PDEC scope、新 primitive/payload、外部 no-projection KZ、Rate、
DStructure、complete/fixed key、signed survival 与 row-mass 仍开放。行/列命题仍未
无条件闭合。

## 425. Phi-LPF latest constructor common signed-table rebase sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_common_signed_table_rebase_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-common-signed-table-rebase-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-common-signed-table-rebase-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-common-signed-table-rebase-sync-ledger.json
```

同步结果：

```text
latest_constructor_pairing_exactuv_triple_imported=true
built_in_pairing_trace_exit_imported=true
trace_exit_source_rank_convergence_imported=true
exactuv_fiber_atomization_imported=true
source_entropy_signed_rows_imported=true
fixed_pair_fiber_complete_key_atomized=true
complete_key_source_table_boundary_imported=true
phi_lpf_recursive_unsigned_ownership_closed=true
row_origin_reduced_to_bucket_signed_law=true
common_same_formal_unit_signed_table_aligned=true
threshold_finite_verification_boundary_preserved=true
beta_sieve_sawtooth_tail_still_open=true
phi_lpf_bucket_signed_coefficient_law_proved=false
alpha_row_anchor_phase_emission_formula_proved=false
same_formal_unit_row_mass_normalization_proved=false
fixed_key_exact_uv_local_multiplicity_o1_proved=false
self_contained_beta_sieve_appendix_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：latest constructor 的 built-in pairing、source entropy 与
fixed-pair ExactUV 三线不再应作为三个互不相干的黑箱处理。built-in pairing 的环外出口
必须携带 source-rank/no-collapse 并汇入逐 primitive 核表；source entropy 必须由
signed rows、row-mass/no-heavy-row 和发射前支撑下界支付；fixed-pair ExactUV 必须由
complete key polylog 分区和 fixed-key 局部 O(1) 重数支付。LPF/Phi 精准桶恒等式已经
严格关闭无符号 owner/support/capacity、素数计数恒等式和 \(p>\sqrt N\) 零质量，但它
不产生 signed coefficient、orientation/local factor、row mass 或 key multiplicity。

最新直接主攻推进到同 formal unit 的共同表字段包：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger
AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
AND PhiLPFBucketSignedCoefficientLawBeforePushforward
AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
AND PrimitiveRowSupportLowerBoundBeforeExactUVProjectionLedger
AND RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger
AND FixedKeyExactUVLocalMultiplicityO1Ledger
AND SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix_THEN_ExactSawtooth
```

充分大阈值加有限验证仍只关闭有限桥；beta-sieve、99% 主系数、exact sawtooth、Rate 与
DStructure 仍开放。行/列命题仍未无条件闭合。

## 426. Phi-LPF latest constructor common-table transport-stack rebase sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_common_table_transport_stack_rebase_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-common-table-transport-stack-rebase-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-common-table-transport-stack-rebase-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-common-table-transport-stack-rebase-sync-ledger.json
```

同步结果：

```text
common_signed_table_imported=true
bucket_transport_stack_imported=true
signed_transport_split_imported=true
step_update_reduced_to_edge_multiplier=true
source_packet_cycle_guard_carried=true
bucket_signed_law_removed_from_common_table=true
tail_package_still_open=true
edge_signed_multiplier_table_proved=false
pointwise_phi_lpf_bucket_signed_value_table_proved=false
alpha_row_anchor_phase_emission_formula_proved=false
same_formal_unit_row_mass_normalization_proved=false
fixed_key_exact_uv_local_multiplicity_o1_proved=false
self_contained_beta_sieve_appendix_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：`PhiLPFBucketSignedCoefficientLawBeforePushforward` 这个粗名已经
被拆开。Phi/LPF 递推只提供无符号 support split；如果不直接提交逐点 Phi-LPF signed
value table，就必须沿 rough-cofactor transport 给出逐 ordered edge 的 signed multiplier 表。
square-base/common-packet 私有出口已被 source-packet cycle guard 吸回 source 三原子。

最新直接主攻推进到：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger
AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
AND PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward
AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
AND PrimitiveRowSupportLowerBoundBeforeExactUVProjectionLedger
AND RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger
AND FixedKeyExactUVLocalMultiplicityO1Ledger
AND SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix_THEN_ExactSawtooth
```

逐点 signed value table 仍是直接旁路，但也必须同口径携带 source 三原子、row-mass/support
和 complete/fixed key。行/列命题仍未无条件闭合。

## 427. Phi-LPF latest constructor common-table edge multiplier slab rebase sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_common_table_edge_multiplier_slab_rebase_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-common-table-edge-multiplier-slab-rebase-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-common-table-edge-multiplier-slab-rebase-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-common-table-edge-multiplier-slab-rebase-sync-ledger.json
```

同步结果：

```text
common_table_transport_edge_multiplier_imported=true
latest_edge_multiplier_slab_reusable=true
first_edge_slab_router_imported=true
first_edge_phi_fiber_formula_imported=true
phi_fiber_unsigned_only_guard_imported=true
common_table_side_gates_carried=true
tail_package_still_open=true
edge_multiplier_slab_rebased=true
semiprime_first_edge_signed_seed_table_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：latest constructor common-table 里的逐 edge multiplier
也不是终端黑箱。LPF ordered path 强制把它拆成第一边 semiprime signed seed table 与
内部 prime-adjoin signed transition law。Phi/LPF 的精确 first-edge 纤维公式只支付
`Phi(floor(N/(p*q)),q)` 的 q-rough continuation 容量，不产生 signed seed、local factor、
row mass、key multiplicity 或 ExactUV payload。

最新直接主攻推进到：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger
AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
AND PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward
AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
AND PrimitiveRowSupportLowerBoundBeforeExactUVProjectionLedger
AND RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger
AND FixedKeyExactUVLocalMultiplicityO1Ledger
AND SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix_THEN_ExactSawtooth
```

下一最窄内部口是 `PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward`，但它必须与
`PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward` 同时保留；source 三原子、
row-mass/support、complete/fixed key、逐点 signed table 旁路、PDEC/terminal/external 旁路、
Rate 与 DStructure 仍开放。行/列命题仍未无条件闭合。

## 428. Phi-LPF latest constructor common-table semiprime seed diagonal rebase sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_common_table_semiprime_seed_diagonal_rebase_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-common-table-semiprime-seed-diagonal-rebase-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-common-table-semiprime-seed-diagonal-rebase-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-common-table-semiprime-seed-diagonal-rebase-sync-ledger.json
```

同步结果：

```text
common_table_first_seed_imported=true
existing_semiprime_diagonal_rebase_reusable=true
semiprime_diagonal_router_imported=true
diagonal_private_escape_removed=true
common_packet_cycle_guard_carried=true
common_table_side_gates_carried=true
tail_package_still_open=true
semiprime_seed_diagonal_rebased=true
offdiagonal_ordered_semiprime_signed_seed_table_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：semiprime first seed 已按 `p=q` 与 `p<q` 唯一拆开。
diagonal `(p,p)` 正是 square-base lane；既有证书已排除它作为私有 signed 出口，只能
回到 common source-packet 三原子。因而新 signed 缺口不再是全部 semiprime first seed，
而是 offdiagonal ordered semiprime first seed。

最新直接主攻推进到：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger
AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
AND PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward
AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
AND PrimitiveRowSupportLowerBoundBeforeExactUVProjectionLedger
AND RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger
AND FixedKeyExactUVLocalMultiplicityO1Ledger
AND SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix_THEN_ExactSawtooth
```

LPF/Phi 桶恒等式仍只支付 owner/support/capacity；offdiagonal signed seed、internal transition、
source 三原子、row-mass/support、complete/fixed key、尾段、Rate 与 DStructure 仍未闭合。
行/列命题仍未无条件闭合。

## 429. Phi-LPF endpoint interval difference frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_endpoint_interval_difference_router.py
docs/monograph/prime-matrix-phi-lpf-endpoint-interval-difference-router.md
docs/monograph/prime-matrix-phi-lpf-endpoint-interval-difference-router.json
data/prime-matrix-phi-lpf-endpoint-interval-difference-ledger.json
```

同步结果：

```text
endpoint_difference_identity_proved=true
kp_to_kp_plus_p_formula_proved=true
mechanical_exact_computation_available=true
interval_positivity_from_identity_alone_proved=false
universal_prime_in_every_aligned_interval_proved=false
crt_aligned_prime_free_block_exists=true
row_column_unconditional_closed=false
```

formal-to-actual 含义是：Phi-LPF 精准桶公式确实可以用于两个端点求差。对闭区间
`2<=A<=B`，

```text
pi(B)-pi(A-1)
=(B-A+1)-sum_{p<=sqrt(B)}[Phi(floor(B/p),p)-Phi(floor((A-1)/p),p)].
```

因此对闭区间 `[kP,kP+P]`，

```text
pi(kP+P)-pi(kP-1)
=P+1-sum_{p<=sqrt(kP+P)}
  [Phi(floor((kP+P)/p),p)-Phi(floor((kP-1)/p),p)].
```

这是精确值公式，不是误差估计；给定 `k,P` 后可以机械算出区间内素数个数。
但它不能单独推出区间正性，因为还需要证明所有 LPF 合数桶端点增量之和小于区间长度。
更强的是，任意固定 `P` 都可用 CRT 构造某个 `k`，使 `[kP,kP+P]` 全为合数。证书样本：
`P=5,k=8166` 时 `[40830,40835]` 全为合数，端点差分和直接筛都给出素数个数 `0`。

本层结论：端点差分公式是精确局部审计器和有限验证器；若要继续用于突破，必须额外加入
平均相位、容量压力、signed payload 或 `sum Delta_Phi_p` 的结构性上界。它本身不闭合
三命题。行/列命题仍未无条件闭合。

## 430. Phi-LPF 1<k<P row interval difference frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_k_less_p_row_interval_difference_router.py
docs/monograph/prime-matrix-phi-lpf-k-less-p-row-interval-difference-router.md
docs/monograph/prime-matrix-phi-lpf-k-less-p-row-interval-difference-router.json
data/prime-matrix-phi-lpf-k-less-p-row-interval-difference-ledger.json
```

同步结果：

```text
k_less_p_endpoint_difference_identity_proved=true
strict_k_closed_interval_equals_internal_row_proved=true
internal_row_formula_proved=true
phi_recurrence_computes_bucket_deltas=true
inside_p_square_prime_uncovered_equivalence_proved=true
previous_crt_prime_free_block_not_applicable=true
interval_positivity_from_identity_alone_proved=false
full_root_uncovered_slot_positive_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：用户强调的 `1<k<P` 需要与上一层一般 `[kP,kP+P]`
分开处理。闭区间端点差分仍然成立：

```text
pi(kP+P)-pi(kP-1)
=P+1-sum_{p<=sqrt(kP+P)}
  [Phi(floor((kP+P)/p),p)-Phi(floor((kP-1)/p),p)].
```

在严格 `1<k<P` 口径下，两个端点 `kP` 与 `kP+P=(k+1)P` 都是合数倍，因此

```text
pi(kP+P)-pi(kP-1)=pi(kP+P-1)-pi(kP).
```

所以闭区间端点差分给出的素数数目，恰好就是内部区间 `I_k={kP+a:1<=a<P}` 的素数数目：

```text
pi(kP+P-1)-pi(kP)
=(P-1)-sum_{p<=sqrt(kP+P-1)}
  [Phi(floor((kP+P-1)/p),p)-Phi(floor(kP/p),p)].
```

Phi 递推 `Phi(x,p_j)=Phi(x,p_{j+1})+Phi(floor(x/p_j),p_j)` 可机械计算这些桶端点。
证书样本的递推值与 LPF 直接计数一致。

本层的新精确信息是：当 `1<k<P` 且 `1<=a<P` 时，`kP+a<P^2`。因此内部行中未被任何
`q<=sqrt(kP+P-1)` 覆盖的槽与素数槽完全等价。上一层 CRT 零素数样本
`P=5,k=8166` 满足 `k>P`，不能用于否定本层 `1<k<P` 目标。

剩余硬点也因此更清楚：要证明该行有素数，必须证明

```text
sum_{p<=sqrt(kP+P-1)}
  [Phi(floor((kP+P-1)/p),p)-Phi(floor(kP/p),p)] < P-1.
```

但这正等价于 full-root 未覆盖槽存在，也就是 row-prime 正性本身。故本层关闭的是
精确计数与循环边界，不是无条件证明。下一步仍需 Q1/Q2 transport、seed/PDEC scope、
signed table、Rate/DStructure 或外部短区间输入。行/列命题仍未无条件闭合。

## 431. Phi-LPF strict-k endpoint bucket cancellation frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_strict_k_endpoint_bucket_cancellation_router.py
docs/monograph/prime-matrix-phi-lpf-strict-k-endpoint-bucket-cancellation-router.md
docs/monograph/prime-matrix-phi-lpf-strict-k-endpoint-bucket-cancellation-router.json
data/prime-matrix-phi-lpf-strict-k-endpoint-bucket-cancellation-ledger.json
```

同步结果：

```text
strict_k_endpoint_composite_mass_two_proved=true
endpoint_lpf_owner_buckets_pinned=true
closed_minus_internal_bucket_delta_equals_endpoint_owners_proved=true
no_endpoint_slack_for_row_positivity_proved=true
internal_row_composite_delta_inequality_proved=false
full_root_uncovered_slot_positive_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：上一层把 `1<k<P` 的闭区间端点差分化成内部行计数；本层进一步
逐 LPF 桶检查端点是否藏有额外余量。结论是否定的。若

```text
Delta_closed_p=[kP,kP+P] 的第 p 个 LPF 桶增量
Delta_internal_p=[kP+1,kP+P-1] 的第 p 个 LPF 桶增量,
```

则逐桶恒等式为

```text
Delta_closed_p-Delta_internal_p
=1_{p=LPF(k)}+1_{p=LPF(k+1)}.
```

因为 `1<k<P`，两个端点 `kP` 与 `(k+1)P` 都是合数。左端点归入 `LPF(k)` 桶，
右端点归入 `LPF(k+1)` 桶；当 `k+1=P` 时右端点是 `P^2`，归入 `P` 桶。于是闭区间
多出的长度 `2` 被两个端点合数的 owner 桶精确吃掉。

这排除了一个潜在捷径：不能把 `[kP,kP+P]` 的闭区间长度 `P+1` 当成比内部行 `P-1`
多出的正性余量。端点 LPF 付款完全抵消该余量。剩余硬点仍是内部行不等式

```text
sum Delta_internal_p < P-1,
```

也就是 full-root 未覆盖槽存在。行/列命题仍未无条件闭合。

## 432. Phi-LPF strict-k internal owner saturation frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_strict_k_internal_owner_saturation_router.py
docs/monograph/prime-matrix-phi-lpf-strict-k-internal-owner-saturation-router.md
docs/monograph/prime-matrix-phi-lpf-strict-k-internal-owner-saturation-router.json
data/prime-matrix-phi-lpf-strict-k-internal-owner-saturation-ledger.json
```

同步结果：

```text
internal_phi_bucket_equals_lpf_owner_partition_proved=true
owner_residue_equation_pinned=true
saturation_defect_equals_prime_count_proved=true
zero_row_iff_owner_saturation_proved=true
positive_saturation_defect_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：端点余量被抵消后，内部行的 Phi-LPF 桶端点增量不只是计算工具，
而是逐桶等于直接 LPF-owner 分桶：

```text
row_prime_count
=(P-1)-sum_p Delta_internal_p
=P-1-sum_p OwnerMass_p.
```

若内部槽 `a` 由 owner `p` 负责，则它满足

```text
a == -kP mod p,
(kP+a)/p is p-rough.
```

因此零行反例被精确改写为：

```text
sum_p OwnerMass_p=P-1,
```

也就是 LPF-owner 桶完全饱和内部行的每一个槽。样本正缺陷、Mertens 密度或 raw capacity
都不能替代证明。当前硬点进一步压成：

```text
PositiveSaturationDefectForStrictKInternalLPFOwnerPartition.
```

该正缺陷仍等价于 full-root 未覆盖槽存在，即 row-prime 内容本身。行/列命题仍未无条件闭合。

## 433. Phi-LPF strict-k raw rejection balance frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_strict_k_raw_rejection_balance_router.py
docs/monograph/prime-matrix-phi-lpf-strict-k-raw-rejection-balance-router.md
docs/monograph/prime-matrix-phi-lpf-strict-k-raw-rejection-balance-router.json
data/prime-matrix-phi-lpf-strict-k-raw-rejection-balance-ledger.json
```

同步结果：

```text
raw_incidence_owner_rejection_partition_proved=true
prime_count_equals_rejection_excess_proved=true
zero_row_iff_exact_raw_rejection_balance_proved=true
raw_capacity_only_contradiction_rejected=true
positive_rejection_excess_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：owner 饱和可继续拆成 raw incidence 与 LPF rejection 的严格账本。
在内部行 `I_k={kP+a:1<=a<P}` 中，先数所有根内素数 `p<=sqrt(kP+P-1)` 的原始命中：

```text
RawTotal = #{(a,p): 1<=a<P, p | kP+a, p<=sqrt(kP+P-1)}.
```

每个原始命中要么是该槽的 LPF-owner 命中，要么是已经被更小素因子负责的 rejected hit。因此

```text
RawTotal=OwnerMass+RejectionMass.
```

结合上一层

```text
row_prime_count=(P-1)-OwnerMass
```

得到新的精确等价式：

```text
row_prime_count=RejectionMass-(RawTotal-(P-1)).
```

于是零行反例不只是 owner 桶全饱和，而是

```text
RejectionMass = RawTotal-(P-1).
```

也就是 LPF rejection 精确吃掉 raw incidence 的全部超容量。真实有素数的行满足严格失衡：

```text
RejectionMass > RawTotal-(P-1).
```

本层排除了 raw capacity 直接矛盾：原始命中总量超过行长并不矛盾，因为超出的命中可以由
非 owner rejection 吸收。当前最窄硬点改写为：

```text
PositiveRejectionExcessForStrictKRawLPFIncidence.
```

这仍等价于 full-root 未覆盖槽存在，但它把下一步非循环入口定位为 signed/transport 型严格
失衡定理，而不是单纯容量比较。行/列命题仍未无条件闭合。

## 434. Phi-LPF strict-k short interval exponent barrier frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_strict_k_short_interval_exponent_barrier_router.py
docs/monograph/prime-matrix-phi-lpf-strict-k-short-interval-exponent-barrier-router.md
docs/monograph/prime-matrix-phi-lpf-strict-k-short-interval-exponent-barrier-router.json
data/prime-matrix-phi-lpf-strict-k-short-interval-exponent-barrier-ledger.json
```

同步结果：

```text
endpoint_difference_available=true
theta_greater_than_half_barrier_proved=true
finite_verification_plus_theta_gt_half_cannot_close_all_large_p=true
sqrt_scale_input_needed_for_pure_short_interval_lane=true
sqrt_scale_input_available_in_current_corpus=false
positive_rejection_excess_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：Phi-LPF 端点差分已能精确给出 strict `1<k<P` 的行内素数个数；
若把剩余正性转交给“充分大阈值以上短区间素数存在 + 有限验证”路线，则长度适配为：

```text
x=kP,  target length=P.
```

若外部输入只有

```text
[x, x + C x^theta] contains a prime
```

则要让该输入落入 `[kP,kP+P]`，必须有：

```text
P >= C*(kP)^theta
=> k <= C^(-1/theta)*P^((1-theta)/theta).
```

因此任意固定 `theta>1/2` 都只覆盖低 `k` 幂次段：

```text
k <= const * P^alpha,  alpha=(1-theta)/theta<1.
```

顶端带

```text
P^alpha < k < P
```

随 `P` 无界增长，不能用有限验证替代。即使 `theta` 极接近 `1/2`，只要仍大于 `1/2`，
该顶端带仍是无限族。纯短区间路线要覆盖全部 strict 行，至少需要：

```text
theta=1/2 with constant C<=1
```

或更强输入。当前语料没有这个无条件平方根尺度短区间定理。因此这层把“充分大阈值+有限验证”
尝试的失败原因严格定位：它不是 Phi-LPF 端点差分失败，而是正性输入尺度不够。最新非循环入口仍是：

```text
PositiveRejectionExcessForStrictKRawLPFIncidence
```

或提交外部/内部 Legendre-scale 平方根短区间定理。行/列命题仍未无条件闭合。

## 435. Phi-LPF strict-k sqrt gap equivalence frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_strict_k_sqrt_gap_equivalence_router.py
docs/monograph/prime-matrix-phi-lpf-strict-k-sqrt-gap-equivalence-router.md
docs/monograph/prime-matrix-phi-lpf-strict-k-sqrt-gap-equivalence-router.json
data/prime-matrix-phi-lpf-strict-k-sqrt-gap-equivalence-ledger.json
```

同步结果：

```text
endpoint_difference_exact_integer_value_proved=true
ge_one_equivalent_to_positive_rejection_excess_proved=true
ge_one_equivalent_to_aligned_sqrt_gap_exclusion_proved=true
sqrt_gap_input_would_close_all_large_strict_rows=true
finite_verification_template_after_sqrt_gap_input_proved=true
sqrt_gap_input_proved_in_current_corpus=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：Phi-LPF 不只给出实数近似，而给出 exact integer：

```text
N_P(k)=pi((k+1)P-1)-pi(kP).
```

由于 strict `1<k<P` 时两个端点 `kP` 和 `(k+1)P` 都是合数，所求 `>=1` 等价于：

```text
N_P(k)>=1
<=> next_prime(kP)<(k+1)P
<=> P 网格行 (kP,(k+1)P) 不被连续素数间隙完整覆盖。
```

结合 raw/rejection 层，也等价于：

```text
RejectionMass > RawTotal-(P-1).
```

这给出最清楚的阈值+有限验证模板。若存在输入：

```text
forall x>=X0, exists prime r with x<r<=x+sqrt(x),
```

则对所有 `kP>=X0` 的 strict 行，因为

```text
sqrt(kP)<P,
```

必有 `r<kP+P`，从而 `N_P(k)>=1`。剩余行满足 `kP<X0`，又因 `k>=2`，只需有限检查：

```text
P<X0/2.
```

所以“充分大阈值一般证明 + 有限验证”的正确闭合形式已经明确：关键不是 Phi-LPF 计数，
而是无条件平方根尺度 prime-gap 输入。当前语料尚未证明该输入，因此本层仍不构成无条件闭合。
最新并行硬点保持为：

```text
SqrtGapInputAfterXOrPositiveRejectionExcessForStrictKRawLPFIncidence.
```

行/列命题仍未无条件闭合。

## 436. Phi-LPF strict-k top row square collar frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_strict_k_top_row_square_collar_router.py
docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-square-collar-router.md
docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-square-collar-router.json
data/prime-matrix-phi-lpf-strict-k-top-row-square-collar-ledger.json
```

同步结果：

```text
top_row_necessary_hard_core_identified=true
top_row_minimal_sqrt_slack_proved=true
top_row_positive_proved_in_current_corpus=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：在 strict `1<k<P` 的全部行里，顶行 `k=P-1` 给出必要硬核。
此时

```text
I_{P-1}={P^2-P+a:1<=a<P}
       =(P^2-P,P^2)
```

而 Phi-LPF 端点差分专化为：

```text
N_top(P)=pi(P^2-1)-pi(P^2-P)
        =P-1-sum_{q<P}
          [Phi(floor((P^2-1)/q),q)-Phi(floor((P^2-P)/q),q)].
```

因此全 strict 行正性必须先证明：

```text
pi(P^2-1)-pi(P^2-P)>=1
```

对所有素数 `P` 成立。该顶行也是平方根尺度余量最小的行，因为 `P-sqrt(kP)` 随 `k`
增大而减小，且

```text
P-sqrt(P(P-1))=P/(P+sqrt(P(P-1))) in (1/2,1).
```

所以顶行正性是 prime-square 上边界 collar 输入：

```text
PrimeSquareUpperCollarPrimeInput.
```

有限审计到 `P<=5003` 没有发现顶行空段，但这不能替代全局证明。该层说明 Phi-LPF 递推若要推出
正性，至少必须在顶行解决这个 square-collar 硬核；当前语料尚未无条件闭合。并行出口仍是：

```text
SqrtGapInputAfterX
OR PositiveRejectionExcessForStrictKRawLPFIncidence
OR PrimeSquareUpperCollarPrimeInput plus remaining-row proof.
```

行/列命题仍未无条件闭合。

## 437. Phi-LPF strict-k top row perfect tiling frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_strict_k_top_row_perfect_tiling_router.py
docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-perfect-tiling-router.md
docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-perfect-tiling-router.json
data/prime-matrix-phi-lpf-strict-k-top-row-perfect-tiling-ledger.json
```

同步结果：

```text
perfect_tiling_excluded_globally=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：顶行 square-collar 正性已经可写成一个精确 LPF 铺满排除问题。令

```text
T_P={P^2-P+a:1<=a<P}
B_q(P)=Phi(floor((P^2-1)/q),q)-Phi(floor((P^2-P)/q),q).
```

则

```text
N_top(P)=P-1-sum_{q<P} B_q(P)
N_top(P)=0 iff sum_{q<P} B_q(P)=P-1
N_top(P)>=1 iff sum_{q<P} B_q(P)<=P-2.
```

所以 Phi-LPF 递推本身没有额外正项；它只是把同一批合数槽位继续拆成更深的有序粗因子树。
若要从端点差分推出正性，必须排除 LPF 合数桶对全部 `P-1` 个顶行槽位的 perfect tiling。

经典 Sylvester-Schur 连续乘积输入在这里的落点也被固定：`P-1` 个连续顶行槽位的乘积有素因子
`r>P-1`；又因顶行槽位都不被 `P` 整除，所以若出现该因子则 `r>P`。但在“顶行无素数”假设下，
`r` 只会被某个 `2<=m<P` 的小载体承载，并不直接给出矛盾。这把剩余硬点送回：

```text
LowCarrierHighPrimePaymentInjection
OR PositiveRejectionExcessForStrictKRawLPFIncidence
OR PrimeSquareUpperCollarPrimeInput.
```

有限审计到 `P<=5003` 没有发现 perfect LPF tiling，最大合数铺满比例样本为 `P=4253` 时约
`0.948495`。这只是实现口径审计，不替代全局证明。行/列命题仍未无条件闭合。

## 438. Phi-LPF strict-k top row high-prime payment split frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_strict_k_top_row_high_prime_payment_split_router.py
docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-high-prime-payment-split-router.md
docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-high-prime-payment-split-router.json
data/prime-matrix-phi-lpf-strict-k-top-row-high-prime-payment-split-ledger.json
```

同步结果：

```text
low_carrier_payment_capacity_exceeded=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：顶行 high-prime 泄出有一个精确分裂：

```text
P-1 = H_1(P)+sum_{2<=m<P}H_m(P)+S_P(P)
H_1(P)=pi(P^2-1)-pi(P^2-P)
H_m(P)=pi(floor((P^2-1)/m))-pi(floor((P^2-P)/m)), 2<=m<P
S_P(P)=# top-row composite slots with all prime factors <=P.
```

这里 `H_1(P)` 正是目标素数槽；`2<=m<P` 的 `H_m(P)` 是大素数因子被小载体支付，
而不是未铺满槽。Sylvester-Schur 连续乘积输入在反设 `H_1(P)=0` 下只推出：

```text
sum_{2<=m<P}H_m(P)>=1,
```

并不推出 `H_1(P)>=1`。因此它不能单独闭合顶行正性；还需要证明
低载体 payment 与 `P`-smooth 合数槽不能合计铺满全部顶行：

```text
sum_{2<=m<P}H_m(P)+S_P(P) <= P-2.
```

有限审计到 `P<=5003` 的分裂恒等式全部成立，最小 `H_1(P)` 为 `1`，但这不替代全局证明。
最新剩余接口为：

```text
LowCarrierPaymentCapacityDeficit
OR PositiveRejectionExcessForStrictKRawLPFIncidence
OR PrimeSquareUpperCollarPrimeInput.
```

行/列命题仍未无条件闭合。

## 439. Phi-LPF strict-k row high-prime payment support frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_strict_k_row_high_prime_payment_support_router.py
docs/monograph/prime-matrix-phi-lpf-strict-k-row-high-prime-payment-support-router.md
docs/monograph/prime-matrix-phi-lpf-strict-k-row-high-prime-payment-support-router.json
data/prime-matrix-phi-lpf-strict-k-row-high-prime-payment-support-ledger.json
```

同步结果：

```text
general_capacity_deficit_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：任意 strict 行

```text
I_{k,P}={kP+a:1<=a<P}, 1<k<P
```

中的 high-prime payment 支撑可以从顶行的 `2<=m<P` 精确缩成：

```text
If n=mr in I_{k,P} and r>P, then m<n/P<k+1, hence m<=k.
```

于是行级分裂为：

```text
P-1=H_1(k,P)+sum_{2<=m<=k}H_m(k,P)+S_k(P)
H_1(k,P)=pi((k+1)P-1)-pi(kP)
H_m(k,P)=pi(floor(((k+1)P-1)/m))-pi(floor(kP/m)), 2<=m<=k
S_k(P)=# row slots with all prime factors <=P.
```

目标正性是 `H_1(k,P)>=1`。因此需要证明容量缺口：

```text
sum_{2<=m<=k}H_m(k,P)+S_k(P)<=P-2.
```

有限审计到 `P<=1009` 的 `76797` 个 strict 行全部正、分裂恒等式全部通过。读数显示：
顶行 `k=P-1` 是最大 carrier 支撑硬核，但不总是最大 payment 比例；低 k 行可能由
`P`-smooth 合数槽主导。该有限现象不作为全局证明。最新剩余接口为：

```text
StrictKLowCarrierPaymentCapacityDeficit
OR StrictKPSmoothCapacityDeficit
OR PositiveRejectionExcessForStrictKRawLPFIncidence
OR SqrtGapInputAfterX.
```

行/列命题仍未无条件闭合。

## 440. Phi-LPF strict-k row load phase tradeoff frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_strict_k_row_load_phase_tradeoff_router.py
docs/monograph/prime-matrix-phi-lpf-strict-k-row-load-phase-tradeoff-router.md
docs/monograph/prime-matrix-phi-lpf-strict-k-row-load-phase-tradeoff-router.json
data/prime-matrix-phi-lpf-strict-k-row-load-phase-tradeoff-ledger.json
```

同步结果：

```text
anti_cosaturation_inequality_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：上一层容量缺口可归一化成两股负载的反同相问题。定义

```text
lambda(k,P)=sum_{2<=m<=k}H_m(k,P)/(P-1)
sigma(k,P)=S_k(P)/(P-1)
eta(k,P)=H_1(k,P)/(P-1).
```

则每个 strict 行满足精确恒等式：

```text
lambda(k,P)+sigma(k,P)+eta(k,P)=1.
```

目标正性等价于：

```text
H_1(k,P)>=1
iff lambda(k,P)+sigma(k,P)<=1-1/(P-1).
```

因此问题不再是 Phi-LPF 公式是否精确；公式已经精确。真正硬点是证明 low-carrier payment
负载 `lambda` 与 `P`-smooth 合数负载 `sigma` 不能同相饱和到 `1`。

有限审计 `P<=1009`、`76797` 个 strict 行显示：`lambda` 峰值出现在高相位
`P=37,k=36`，`sigma` 峰值出现在低相位 `P=863,k=2`，最大 `lambda+sigma`
样本为 `P=571,k=438`，约 `0.952632`。同时没有发现 `lambda>=0.70` 且
`sigma>=0.70` 的同行样本。该证据仅定位结构，不替代全局证明。

最新剩余接口为：

```text
GlobalPaymentSmoothAntiCoSaturationInequality
OR PositiveRejectionExcessForStrictKRawLPFIncidence
OR SqrtGapInputAfterX.
```

行/列命题仍未无条件闭合。

## 441. Phi-LPF strict-k Dusart interval bridge frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_strict_k_dusart_interval_bridge_router.py
docs/monograph/prime-matrix-phi-lpf-strict-k-dusart-interval-bridge-router.md
docs/monograph/prime-matrix-phi-lpf-strict-k-dusart-interval-bridge-router.json
data/prime-matrix-phi-lpf-strict-k-dusart-interval-bridge-ledger.json
```

同步结果：

```text
dusart_covers_all_strict_rows=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：外部 Dusart 2010 输入可作为显式低 k 桥。使用：

```text
for x>=396738, [x, x+x/(25 log^2 x)] contains at least one prime.
```

对 strict 行取 `x=kP`。若

```text
kP>=396738
AND k<=25 log^2(kP),
```

则 `x/(25 log^2 x)<=P`，而两个端点 `kP,(k+1)P` 都为合数，所以 Dusart 给出的素数落在
`(kP,(k+1)P)` 内。阈值以下 `kP<396738` 的行由有限桥验证：

```text
checked_rows=257198
finite_bridge_verified=true.
```

覆盖审计扩到 `P<=10007` 后显示：

```text
union_closed_ratio=0.968923
first_prime_with_uncovered_row=8101
last_prime_all_rows_closed_in_sample=8093.
```

第一个未被 Dusart+有限桥覆盖的样本是顶行：

```text
P=8101, k=8100.
```

这说明 Dusart 输入非常有用，但尺度是 `x/log^2 x`，在 `k~P` 时约为
`P^2/log^2(P^2)`，仍大于行长 `P`。因此它不能替代 `sqrt(x)` 尺度输入，也不能单独闭合全部
`1<k<P`。

最新剩余接口保持为：

```text
GlobalPaymentSmoothAntiCoSaturationInequality
OR PositiveRejectionExcessForStrictKRawLPFIncidence
OR SqrtGapInputAfterX.
```

行/列命题仍未无条件闭合。

## 442. Phi-LPF strict-k low-carrier lower-half source-cut frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_strict_k_low_carrier_lower_half_source_cut_router.py
docs/monograph/prime-matrix-phi-lpf-strict-k-low-carrier-lower-half-source-cut-router.md
docs/monograph/prime-matrix-phi-lpf-strict-k-low-carrier-lower-half-source-cut-router.json
data/prime-matrix-phi-lpf-strict-k-low-carrier-lower-half-source-cut-ledger.json
```

同步结果：

```text
all_payment_sources_in_lower_half=true
lower_half_payment_smooth_anti_tiling_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：strict 行 high-prime payment 的来源是无环的。若

```text
n=mr, 2<=m<=k, r>P prime, kP<n<(k+1)P,
```

则

```text
kP/m < r <= ((k+1)P-1)/m
m>=2 => r < ((k+1)P)/2 < kP
floor(r/P) <= floor(k/2).
```

所以 payment source 不可能来自目标行自身、近顶端行或未来行。固定目标行内，同一个源素数
`r>P` 也至多支付一个槽，因为两个 carrier 的乘积差至少为 `r>P`，超过行宽 `P-1`。

有限审计到 `P<=1009`：

```text
strict_row_count=76797
rows_with_low_carrier_payment=76795
all_payment_sources_in_lower_half=true
max_low_carrier_payment=685 at P=1009,k=968
max_source_ratio=0.5.
```

因此零行反例被压成下半源注入像与 `P`-smooth 槽的完美铺满：

```text
all slots = image(lower-half prime source injection) union P-smooth slots.
```

最新剩余接口相应变为：

```text
LowerHalfPaymentSmoothAntiTilingInequality
OR PositiveRejectionExcessForStrictKRawLPFIncidence
OR SqrtGapInputAfterX.
```

本层关闭的是 payment 来源环，不是 strict 行正性的无条件证明。行/列命题仍未无条件闭合。

## 443. Phi-LPF strict-k payment Beatty source-map frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_strict_k_payment_beatty_source_map_router.py
docs/monograph/prime-matrix-phi-lpf-strict-k-payment-beatty-source-map-router.md
docs/monograph/prime-matrix-phi-lpf-strict-k-payment-beatty-source-map-router.json
data/prime-matrix-phi-lpf-strict-k-payment-beatty-source-map-ledger.json
```

同步结果：

```text
all_hm_counts_match_beatty_source_map=true
beatty_smooth_anti_tiling_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：上一层的 lower-half payment source injection 不是任意注入，
而是一张由余数 `kP mod r` 唯一决定的 Beatty 近倍数源表。对 `1<k<P`，源素数 `r>P`
能支付目标行当且仅当

```text
P<r<=floor(((k+1)P-1)/2), r prime
m=floor(kP/r)+1
a=m*r-kP=r-(kP mod r)
1<=a<P.
```

于是有精确等式：

```text
sum_{2<=m<=k} H_m(k,P)
= #{prime r>P: r-(kP mod r) lies in [1,P-1]}.
```

有限审计：

```text
max_prime=257
strict_row_count=6227
all_hm_counts_match_beatty_source_map=true.
```

并额外确认 `P=571,k=438` 与 `P=1009,k=1008` 的 `H_m` payment 与 Beatty source
count 分别同为 `382` 与 `670`。因此零行反例进一步被压成

```text
all slots = image(Beatty near-multiple prime sources) union P-smooth slots.
```

最新剩余接口为：

```text
BeattySmoothAntiTilingInequality
OR PositiveRejectionExcessForStrictKRawLPFIncidence
OR SqrtGapInputAfterX.
```

本层关闭的是 payment 源表选择自由，不是 strict 行正性的无条件证明。行/列命题仍未
无条件闭合。

## 444. Phi-LPF strict-k endpoint Beatty-smooth exact value frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_strict_k_endpoint_beatty_smooth_value_router.py
docs/monograph/prime-matrix-phi-lpf-strict-k-endpoint-beatty-smooth-value-router.md
docs/monograph/prime-matrix-phi-lpf-strict-k-endpoint-beatty-smooth-value-router.json
data/prime-matrix-phi-lpf-strict-k-endpoint-beatty-smooth-value-ledger.json
```

同步结果：

```text
all_endpoint_beatty_smooth_value_identities_hold=true
all_rows_positive_in_finite_sweep=true
minimum_prime_count=1
finite_evidence_not_used_as_global_proof=true
```

formal-to-actual 含义是：`1<k<P` 的 `[kP,kP+P]` 端点差已经不只是可计算，
而是可同 Beatty 源像和 `P`-smooth 槽合并成同一个精确值坐标。由于
`kP` 与 `(k+1)P` 均为合数倍，

```text
N_P(k)=pi((k+1)P-1)-pi(kP)
      =(P-1)-sum_{p<=sqrt((k+1)P-1)}
        [Phi(floor(((k+1)P-1)/p),p)-Phi(floor(kP/p),p)]
      =(P-1)-B_P(k)-S_P(k).
```

这里 `B_P(k)` 是 Beatty 近倍数 high-prime payment 槽数，`S_P(k)` 是 `P`-smooth
槽数。有限审计到 `P<=257` 验证端点差、LPF owner 桶、Beatty payment 槽和 `P`-smooth
槽分解一致。最接近铺满样本：

```text
P=59, k=42, N_P(k)=3, B_P(k)=40, S_P(k)=15, B+S=55, P-1=58.
```

因此当前正性硬点被完全规范为：

```text
N_P(k)>=1 iff B_P(k)+S_P(k)<=P-2.
```

最新剩余接口为：

```text
BeattySmoothAntiTilingInequality
OR PositiveRejectionExcessForStrictKRawLPFIncidence
OR SqrtGapInputAfterX.
```

本层关闭的是 strict-k 端点差精确值坐标，不是 strict 行正性的无条件证明。

## 445. Phi-LPF strict-k Beatty Euclidean source-window frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_strict_k_beatty_euclidean_source_window_router.py
docs/monograph/prime-matrix-phi-lpf-strict-k-beatty-euclidean-source-window-router.md
docs/monograph/prime-matrix-phi-lpf-strict-k-beatty-euclidean-source-window-router.json
data/prime-matrix-phi-lpf-strict-k-beatty-euclidean-source-window-ledger.json
```

同步结果：

```text
all_hm_counts_match_quotient_source_windows=true
all_source_rows_in_lower_half=true
finite_evidence_not_used_as_global_proof=true
```

formal-to-actual 含义是：Beatty payment 不仅由 `kP mod r` 决定，还可按 carrier
`m` 写成早期源行的一个短有理窗口。设

```text
j=floor(k/m), k=mj+t, 0<=t<m, r=jP+b.
```

则

```text
kP < mr < (k+1)P
iff tP < m b < (t+1)P
iff floor(tP/m)+1 <= b <= floor(((t+1)P-1)/m).
```

因此

```text
B_P(k)=sum_{2<=m<=k} #{ prime r=jP+b in the corresponding source window }.
```

有限审计到 `P<=1009` 验证 `H_m` payment 与商源行窗口计数完全一致。最大 payment
样本为 `P=1009,k=968,payment=685`；最大非空源窗口数样本为
`P=1009,k=1008,nonempty_windows=368`。下半源切口现在成为 `j=floor(k/m)<=floor(k/2)`
的直接推论。

最新剩余接口仍为：

```text
BeattySmoothAntiTilingInequality
OR PositiveRejectionExcessForStrictKRawLPFIncidence
OR SqrtGapInputAfterX.
```

本层关闭的是 payment 源窗口选择自由，不是 strict 行正性的无条件证明。

## 446. Phi-LPF strict-k smooth owner quotient-window frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_strict_k_smooth_owner_quotient_window_router.py
docs/monograph/prime-matrix-phi-lpf-strict-k-smooth-owner-quotient-window-router.md
docs/monograph/prime-matrix-phi-lpf-strict-k-smooth-owner-quotient-window-router.json
data/prime-matrix-phi-lpf-strict-k-smooth-owner-quotient-window-ledger.json
```

同步结果：

```text
all_dual_quotient_window_identities_hold=true
strict_row_count=6227
minimum_prime_count=1
finite_evidence_not_used_as_global_proof=true
```

formal-to-actual 含义是：`P`-smooth 槽也被推回确定的 LPF-owner 商窗口。若 `p` 是
目标槽 `n=pq` 的最小素因子，则

```text
floor(kP/p)<q<=floor(((k+1)P-1)/p),
least_prime_factor(q)>=p,
greatest_prime_factor(q)<=P.
```

因此

```text
S_P(k)=sum_{p<=sqrt((k+1)P-1)} #{ admissible q in the p-owner window }.
```

与上一层

```text
B_P(k)=sum_{2<=m<=k} #{ prime r in the Euclidean Beatty source window }
```

合并后，strict 行正性完全等价于双窗口未铺满：

```text
N_P(k)=(P-1)-B_P(k)-S_P(k),
N_P(k)>=1 iff B_P(k)+S_P(k)<=P-2.
```

有限审计显示最大 smooth 样本为 `P=257,k=2,N=39,B=21,S=196`；最接近铺满样本为
`P=59,k=42,N=3,B=40,S=15,fill=0.948276`。

最新剩余接口改名并收窄为：

```text
DualWindowAntiTilingInequality
OR PositiveRejectionExcessForStrictKRawLPFIncidence
OR SqrtGapInputAfterX.
```

本层关闭的是 smooth source-domain 口径，不是 strict 行正性的无条件证明。

## 447. Phi-LPF strict-k external gap bridge frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_strict_k_external_gap_bridge_router.py
docs/monograph/prime-matrix-phi-lpf-strict-k-external-gap-bridge-router.md
docs/monograph/prime-matrix-phi-lpf-strict-k-external-gap-bridge-router.json
data/prime-matrix-phi-lpf-strict-k-external-gap-bridge-ledger.json
```

formal-to-actual 含义是：外部短区间引理可精确桥接到 strict 行，但桥接条件是

```text
H(kP)<=P=x/k.
```

当前筛查：

```text
Dusart 2010: [x,x+x/(25 log^2 x)] for x>396738
  => covers only k<=25 log^2(kP).
Baker-Harman-Pintz 2001: [x,x+x^0.525] for large x
  => covers only k<=x^0.475.
strict range: k<P, so k may approach x^0.5.
```

代表边界：

```text
P=1009, k=1008, Dusart direct coverage=true, BHP coverage=false.
P=10007, k=10006, Dusart direct coverage=false, BHP coverage=false.
P=1000003, k=1000002, Dusart direct coverage=false, BHP coverage=false.
```

因此 known external-gap route 目前不能关闭全部 strict 行；它只给出可合并的子带。
最新剩余接口保持为：

```text
DualWindowAntiTilingInequality
OR PositiveRejectionExcessForStrictKRawLPFIncidence
OR SqrtGapInputAfterX.
```

其中 `SqrtGapInputAfterX` 必须达到右侧 `H(x)<=sqrt(x)` 量级，或被内部
`B_P(k)+S_P(k)<=P-2` 双窗口反铺满替代。

## 448. Phi-LPF strict-k unified positive core frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_strict_k_unified_positive_core_router.py
docs/monograph/prime-matrix-phi-lpf-strict-k-unified-positive-core-router.md
docs/monograph/prime-matrix-phi-lpf-strict-k-unified-positive-core-router.json
data/prime-matrix-phi-lpf-strict-k-unified-positive-core-ledger.json
```

同步结果：

```text
all_four_coordinate_identities_hold=true
strict_row_count=6228
minimum_positive_core_value=1
finite_evidence_not_used_as_global_proof=true
```

formal-to-actual 含义是：strict 行正性的多个剩余名称已经归并为同一个整数：

```text
N_P(k)=pi((k+1)P-1)-pi(kP)
      =(P-1)-B_P(k)-S_P(k)
      =(P-1)-OwnerMass
      =RejectionMass-(RawTotal-(P-1)).
```

并且：

```text
N_P(k)>=1 iff next_prime(kP)<(k+1)P.
```

所以 `DualWindowAntiTilingInequality`、`PositiveRejectionExcessForStrictKRawLPFIncidence`
和 `SqrtGapInputAfterX` 不应继续被当成三个可分别绕开的硬点。它们是同一
`UnifiedPositiveCore` 的三种可证明入口：

```text
UnifiedPositiveCore:
  for every prime P and every 1<k<P, N_P(k)>=1.
```

最新剩余接口因此收缩为：

```text
UnifiedPositiveCore
  via internal dual-window anti-tiling
  OR via internal raw/rejection strict excess
  OR via external/internal sqrt-scale prime-gap input.
```

## 449. Phi-LPF strict-k top-row Oppermann alignment frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_strict_k_top_row_oppermann_alignment_router.py
docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-oppermann-alignment-router.md
docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-oppermann-alignment-router.json
data/prime-matrix-phi-lpf-strict-k-top-row-oppermann-alignment-ledger.json
```

同步结果：

```text
all_prime_bases_left_half_positive=true
all_prime_bases_right_half_positive=true
prime_base_count=669
minimum_left_oppermann_count=1
minimum_right_oppermann_count=1
finite_evidence_not_used_as_global_proof=true
```

formal-to-actual 含义是：最坏顶行 `k=P-1` 与 Oppermann 左半窗完全对齐：

```text
N_top(P)=pi(P^2-1)-pi(P^2-P).
```

这正是 `n=P` 的 `(n^2-n,n^2)`。完整 Oppermann 猜想会关闭该子核；Legendre
只保证 `((P-1)^2,P^2)` 某处有素数，不能强制落在上半窗；有限验证只给有限范围。

最新剩余接口进一步尖化为：

```text
PrimeIndexedOppermannLeftHalf(P)
  OR SquarePhaseSpecialPhaseLongBlockPDECExclusion
  OR SquarePhaseRoughSurvivorUniformLowerBound.
```

本层仍不证明 `UnifiedPositiveCore`，只禁止把 Legendre/有限验证误登记为顶行闭合。

## 450. Phi-LPF strict-k finite sqrt square-phase tail frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_strict_k_finite_sqrt_square_phase_tail_router.py
docs/monograph/prime-matrix-phi-lpf-strict-k-finite-sqrt-square-phase-tail-router.md
docs/monograph/prime-matrix-phi-lpf-strict-k-finite-sqrt-square-phase-tail-router.json
data/prime-matrix-phi-lpf-strict-k-finite-sqrt-square-phase-tail-ledger.json
```

同步结果：

```text
external_range=[117, 1000000000000000000]
small_checked_row_count=49
all_small_rows_positive=true
largest_prime_base_with_top_row_start_le_x_max=999999937
```

formal-to-actual 含义是：`UnifiedPositiveCore` 的有限初段可以借外部
sqrt-gap 计算输入真正关闭。对 `x=kP`、`1<k<P`，`sqrt(x)<P`，所以已发表的
有限输入 `117<=x<=10^18` 时 `[x,x+sqrt(x)]` 有素数，直接给出

```text
N_P(k)=pi((k+1)P-1)-pi(kP)>=1.
```

阈值以下由脚本直接核查。于是任何 formal-to-actual 反例链都必须满足：

```text
kP>10^18.
```

最坏顶行的尾段等价形式为：

```text
P>999999937
AND [1,P-1] fully covered by r == P^2 mod q for primes q<P.
```

因此当前真剩余接口不是有限验证，而是：

```text
SquarePhaseTailLongBlockPDECExclusion
OR SquarePhaseRoughSurvivorUniformLowerBound
OR genuine sqrt-scale theorem beyond 10^18.
```

本层仍不证明 `UnifiedPositiveCore`；它只把有限初段归档并把无限尾段压成平方相位
特殊长覆盖块。

## 451. Phi-LPF top-row half-rough semiprime shadow frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_top_row_half_rough_semiprime_shadow_router.py
docs/monograph/prime-matrix-phi-lpf-top-row-half-rough-semiprime-shadow-router.md
docs/monograph/prime-matrix-phi-lpf-top-row-half-rough-semiprime-shadow-router.json
data/prime-matrix-phi-lpf-top-row-half-rough-semiprime-shadow-ledger.json
```

同步结果：

```text
max_prime=5003
all_half_rough_identities_hold=true
minimum_half_rough_minus_shadow=1
P=5003: R_1/2=330, T_1/2=49, direct_top_primes=281
```

formal-to-actual 含义是：顶行 `PrimeIndexedOppermannLeftHalf` 的无限尾段可以改写成
half-rough excess。设

```text
R_1/2(P)=#{1<=r<P: gcd(P^2-r, product_{q<=P/2} q)=1}
T_1/2(P)=sum_{P/2<q<P, q prime}
  #{m prime: floor((P^2-P)/q)<m<=floor((P^2-1)/q)}.
```

则：

```text
N_top(P)=pi(P^2-1)-pi(P^2-P)=R_1/2(P)-T_1/2(P).
```

这不是新猜想，而是同一对象的更窄坐标：`R_1/2` 是平方相位在 `q<=P/2`
之后仍幸存的槽数，`T_1/2` 是所有可能把这些幸存槽解释为合数的 reciprocal
prime-semiprime shadow。因为剩余合数只能形如

```text
P^2-r=q*m,  P/2<q<P,  P<m<2P,  q,m both prime,
```

证明顶行正性等价于证明：

```text
R_1/2(P)>T_1/2(P).
```

最新真剩余接口更新为：

```text
HalfRoughSurvivorExcessOverReciprocalSemiprimeShadow
OR SquarePhaseTailLongBlockPDECExclusion
OR genuine sqrt-scale theorem beyond 10^18.
```

本层仍不证明 `UnifiedPositiveCore`；它把尾段反例从完整 LPF 铺满压缩成 reciprocal
semiprime shadow 铺满 half-rough survivor。

## 452. Phi-LPF strict-k external bulk square-band partition frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_strict_k_external_bulk_square_band_partition_router.py
docs/monograph/prime-matrix-phi-lpf-strict-k-external-bulk-square-band-partition-router.md
docs/monograph/prime-matrix-phi-lpf-strict-k-external-bulk-square-band-partition-router.json
data/prime-matrix-phi-lpf-strict-k-external-bulk-square-band-partition-ledger.json
```

同步结果：

```text
status=strict_k_external_bulk_covered_remaining_forced_to_high_k_square_band
bhp_strict_k_exponent=19/21
finite_sqrt_initial_segment=kP<=10^18
top_row_interface=HalfRoughSurvivorExcessOverReciprocalSemiprimeShadow
```

formal-to-actual 含义是：`[kP,kP+P]`、`1<k<P` 的 Phi-LPF 端点差分已经是精确
计数对象

```text
N_P(k)=pi((k+1)P-1)-pi(kP).
```

外部引理路线现在分成三层：有限 sqrt-gap 输入清掉 `kP<=10^18`；Dusart 2010
显式区间只覆盖 `k<=25 log^2(kP)` 的低 `k` 带；Baker--Harman--Pintz 的
`x^(21/40)` 输入若代入 `x=kP`，只给

```text
P >= (kP)^(21/40) iff k <= P^(19/21).
```

因此在这些外部 bulk 之后，任何尚未处理的反例必须落入

```text
x=kP>10^18
AND P^(19/21)<k<P.
```

顶行 `k=P-1` 已由上一层进一步压成 `R_1/2(P)>T_1/2(P)`。一般高 `k`
平方边界带仍需要对应的 Phi-LPF excess、semiprime-shadow PDEC 排斥，或真正
`sqrt(x)` 尺度且常数不超过 1 的外部短区间定理。本层仍不证明三目标命题无条件闭合。

## 453. Phi-LPF strict-k half-rough shadow band split frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_strict_k_half_rough_shadow_band_split_router.py
docs/monograph/prime-matrix-phi-lpf-strict-k-half-rough-shadow-band-split-router.md
docs/monograph/prime-matrix-phi-lpf-strict-k-half-rough-shadow-band-split-router.json
data/prime-matrix-phi-lpf-strict-k-half-rough-shadow-band-split-ledger.json
```

同步结果：

```text
max_prime=1009
all_half_rough_shadow_identities_hold=true
identity_failure_count=0
next_direct_attack_target=HalfRoughSurvivorExistenceInShadowFreeHighBand OR HighKHalfRoughSurvivorExcessOverTwoPrimeShadow
```

formal-to-actual 含义是：上一层留下的高 `k` 平方边界带不再需要完整 LPF 树。
对 `1<k<P`，定义

```text
R_half(P,k)=#{1<=t<P: gcd(kP+t, product_{q<=P/2} q)=1}
T_half(P,k)=#{q,m prime: P/2<q<=m<2P, kP<qm<(k+1)P}.
```

则有精确恒等式：

```text
pi((k+1)P-1)-pi(kP)=R_half(P,k)-T_half(P,k).
```

结构读法是：若 `kP+t` 避开所有 `q<=P/2` 但仍合成，则它的最小素因子
`q` 在 `(P/2,P)`，商 `m<2P` 且必须为素数；用 `q<=m` 避免双计数。
另外，当

```text
4*((k+1)P-1)<=P^2
```

时，整行低于 `P^2/4`，任何 `q,m>P/2` 的 shadow 都不可能出现，所以
`T_half(P,k)=0`。因此 BHP bulk 后的真剩余进一步拆成：

```text
HalfRoughSurvivorExistenceInShadowFreeHighBand
OR HighKHalfRoughSurvivorExcessOverTwoPrimeShadow.
```

本层仍不证明 `UnifiedPositiveCore`；它只把高 `k` 反例从完整 LPF 铺满压到
half-rough survivor 非空或 two-prime shadow excess。

## 454. Phi-LPF shadow-free half-primorial phase frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_shadow_free_half_primorial_phase_router.py
docs/monograph/prime-matrix-phi-lpf-shadow-free-half-primorial-phase-router.md
docs/monograph/prime-matrix-phi-lpf-shadow-free-half-primorial-phase-router.json
data/prime-matrix-phi-lpf-shadow-free-half-primorial-phase-ledger.json
```

同步结果：

```text
status=shadow_free_lane_reduced_to_half_primorial_special_phase_avoidance
large_sample_rows_have_survivor=true
small_period_max_run_less_than_P_minus_1=true
next_direct_attack_target=HalfPrimorialSpecialPhaseAvoidsLongCoveredBlockOrPDEC
```

formal-to-actual 含义是：对 shadow-free 子带，令

```text
M_half(P)=prod_{q<=P/2, q prime} q.
```

由于 `4*((k+1)P-1)<=P^2` 时 two-prime shadow 为空，行正性无损等价于

```text
exists 1<=t<P such that gcd(kP+t, M_half(P))=1.
```

并且该 survivor 自动为素数。于是 shadow-free 失败当且仅当特殊相位
`kP+1 mod M_half(P)` 在 half-primorial 周期中启动一个长度 `P-1` 的低筛覆盖块。
全周期上界 `max covered run < P-1` 会闭合该子带；若全周期 Jacobsthal 上界不可得，
剩余就是：

```text
HalfPrimorialSpecialPhaseAvoidsLongCoveredBlockOrPDEC.
```

本层仍不关闭 upper-band 的 two-prime shadow excess，也不证明三目标命题。

## 455. Phi-LPF upper-band two-prime shadow excess frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_upper_band_two_prime_shadow_excess_router.py
docs/monograph/prime-matrix-phi-lpf-upper-band-two-prime-shadow-excess-router.md
docs/monograph/prime-matrix-phi-lpf-upper-band-two-prime-shadow-excess-router.json
data/prime-matrix-phi-lpf-upper-band-two-prime-shadow-excess-ledger.json
```

同步结果：

```text
status=upper_band_two_prime_shadow_reduced_to_sparse_reciprocal_prime_pair_windows
max_prime=1009
all_reciprocal_window_identities_hold=true
large_sample_count=10
all_sampled_upper_rows_have_positive_margin=true
next_direct_attack_target=UpperBandReciprocalPrimePairShadowSaturationOrPDEC AND UpperBandHalfRoughFloorOrReciprocalPrimePairCeiling
```

formal-to-actual 含义是：对 upper square band

```text
4*((k+1)P-1)>P^2
```

上一层的 two-prime shadow 可精确写成高素数 `q in (P/2,P)` 上的倒数短窗：

```text
I_q(P,k)=[max(q, floor(kP/q)+1), floor(((k+1)P-1)/q)] intersect Z,
T_half(P,k)=sum_{P/2<q<P, q prime} #{m in I_q(P,k): m prime}.
```

因为 `|I_q(P,k)|<=2`，upper-band 的 actual shadow load 不是完整 LPF 树，而是
每个 `q` 至多两个候选 `m` 的 reciprocal prime-pair 图。若行失败，则必须是这些
稀疏短窗素数点真实饱和并吃掉全部 half-rough survivor，或进入 half-rough floor /
reciprocal prime-pair ceiling 的命名 PDEC。

当前 upper-band 直接口为：

```text
UpperBandReciprocalPrimePairShadowSaturationOrPDEC
AND UpperBandHalfRoughFloorOrReciprocalPrimePairCeiling.
```

本层只关闭短窗公式和有限审计；不证明 upper-band 正性，也不证明三目标命题。

## 456. Phi-LPF upper-band reciprocal graph structure frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_upper_band_reciprocal_graph_structure_router.py
docs/monograph/prime-matrix-phi-lpf-upper-band-reciprocal-graph-structure-router.md
docs/monograph/prime-matrix-phi-lpf-upper-band-reciprocal-graph-structure-router.json
data/prime-matrix-phi-lpf-upper-band-reciprocal-graph-structure-ledger.json
```

同步结果：

```text
status=upper_band_reciprocal_shadow_graph_reduced_to_ordered_degree_two_forest
max_prime=1009
all_upper_rows_have_forest_shadow_graph=true
graph_structure_failure_count=0
all_sampled_graphs_are_forests=true
next_direct_attack_target=UpperBandForestShadowSaturationExclusionOrPDEC
```

formal-to-actual 含义是：upper-band 的 reciprocal prime-pair shadow 可看成二部图，
边为同一行内的 `(q,m)`。固定 `q` 或固定 `m` 时，对侧窗口长度都小于 `2`，所以两侧
度数至多二。若 `q1<q2` 且 `m1<m2` 两条边同时存在，则

```text
q2*m2-q1*m1 >= (q2-q1)*m2 + q1*(m2-m1) > P,
```

与二者落在同一长度 `P` 行矛盾。因此 shadow 图有序无交叉；取任一假想环中最小的
`q0`，它的较大邻点不可能再接到第二个 `q`，故环不存在。反例不能依靠循环反馈放大
shadow，只能是森林边集真实饱和全部 half-rough survivor。

当前 upper-band 最新窄口为：

```text
UpperBandForestShadowSaturationExclusionOrPDEC.
```

本层不证明森林饱和不可能，也不证明三目标命题。

## 457. Phi-LPF punctured half-primorial forest phase frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_punctured_half_primorial_forest_phase_router.py
docs/monograph/prime-matrix-phi-lpf-punctured-half-primorial-forest-phase-router.md
docs/monograph/prime-matrix-phi-lpf-punctured-half-primorial-forest-phase-router.json
data/prime-matrix-phi-lpf-punctured-half-primorial-forest-phase-ledger.json
```

同步结果：

```text
status=shadow_free_and_upper_band_reduced_to_punctured_half_primorial_forest_phase
max_prime=1009
all_punctured_phase_identities_hold=true
saturation_row_count=0
minimum_sample_prime_slots=4385
next_direct_attack_target=PuncturedHalfPrimorialForestPhaseAvoidanceOrPDEC
```

formal-to-actual 含义是：设

```text
M_half(P)=prod_{q<=P/2, q prime} q,
F(P,k)={t: t=qm-kP, q,m prime, P/2<q<=m<2P, kP<qm<(k+1)P}.
```

则行内素数槽精确等于

```text
{1<=t<P: gcd(kP+t,M_half(P))=1 and t not in F(P,k)}.
```

因此 shadow-free 子带是 `F(P,k)=empty` 的零孔特例；upper-band 是有序森林孔特例。
若行失败，则所有半 primorial survivor 必须全部落入 forest holes：

```text
{t: gcd(kP+t,M_half(P))=1} subset F(P,k).
```

两个剩余口统一为：

```text
PuncturedHalfPrimorialForestPhaseAvoidanceOrPDEC.
```

本层只关闭等价转换和有限审计；不证明 punctured special phase 全局避让，也不证明三目标命题。

## 458. Phi-LPF punctured endpoint difference frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_punctured_endpoint_difference_router.py
docs/monograph/prime-matrix-phi-lpf-punctured-endpoint-difference-router.md
docs/monograph/prime-matrix-phi-lpf-punctured-endpoint-difference-router.json
data/prime-matrix-phi-lpf-punctured-endpoint-difference-ledger.json
```

同步结果：

```text
status=strict_k_prime_count_equals_phi_half_endpoint_difference_minus_forest_holes
max_prime=1009
all_endpoint_difference_identities_hold=true
minimum_sample_endpoint_margin=4385
next_direct_attack_target=PuncturedPhiEndpointDifferencePositiveOrPDEC
```

formal-to-actual 含义是：令 `p_half(P)` 为大于 `P/2` 的第一个素数，

```text
DeltaPhi_half(P,k)=Phi((k+1)P-1,p_half(P))-Phi(kP,p_half(P)).
```

则 strict 行的素数数目精确为：

```text
pi((k+1)P-1)-pi(kP)=DeltaPhi_half(P,k)-|F(P,k)|.
```

这里 `F(P,k)` 是 upper-band 的 reciprocal forest holes。shadow-free 是 `|F|=0`，
upper-band 是同一公式中 `|F|>0` 的情形。反例必须满足：

```text
DeltaPhi_half(P,k)<=|F(P,k)|.
```

当前统一最窄口改写为 Phi-LPF 两端点差正性：

```text
PuncturedPhiEndpointDifferencePositiveOrPDEC.
```

本层仍不证明端点差全局正性，也不证明三目标命题。

## 459. Phi-LPF punctured endpoint parity capacity frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_punctured_endpoint_parity_capacity_router.py
docs/monograph/prime-matrix-phi-lpf-punctured-endpoint-parity-capacity-router.md
docs/monograph/prime-matrix-phi-lpf-punctured-endpoint-parity-capacity-router.json
data/prime-matrix-phi-lpf-punctured-endpoint-parity-capacity-ledger.json
```

同步结果：

```text
status=forest_holes_bounded_by_reciprocal_integer_windows_minus_forced_even_candidates
max_prime=1009
row_count=76789
closed_by_integer_window_capacity_count=60813
closed_by_parity_ceiling_count=76788
parity_not_closed_count=1
parity_failure_count=0
parity_tie_count=1
minimum_sample_delta_minus_parity_ceiling=1769
next_direct_attack_target=PuncturedParityEndpointCapacityInequalityOrReciprocalPrimePairSaturationPDEC
```

formal-to-actual 含义是：在上一层

```text
prime_count(P,k)=DeltaPhi_half(P,k)-|F(P,k)|
```

之上，对每个 high prime `q in (P/2,P)` 的 reciprocal 短窗 `I_q(P,k)` 建立纯容量上界。
令

```text
W_int(P,k)=sum_q |I_q(P,k)|
E_even(P,k)=#{(q,m): m in I_q(P,k), m even, m>2}
C_par(P,k)=W_int(P,k)-E_even(P,k).
```

因为偶数 `m>2` 不可能成为 high-prime semiprime 的第二素因子，

```text
|F(P,k)| <= C_par(P,k).
```

所以新的非循环充分条件是：

```text
DeltaPhi_half(P,k)>C_par(P,k).
```

有限审计到 `P<=1009` 时，该 strict parity inequality 直接闭合 76788 行，只剩
`P=19,k=15` 的等号基例；该基例的真实读数为 `Delta=3, C_par=3, holes=2,
primes=1`，因此有限基例本身闭合。大尺度抽样只作证据，不作全局证明。

当前最窄口从“端点差正性”进一步压缩为：

```text
PuncturedParityEndpointCapacityInequalityOrReciprocalPrimePairSaturationPDEC.
```

若该奇偶容量不等式失败，反例必须让 odd reciprocal candidates 几乎全部成为 prime-pair
holes；也就是一个显式的 reciprocal prime-pair saturation/PDEC 出口。本层仍不证明全局
奇偶容量不等式，也不证明三目标命题。

## 460. Phi-LPF combinatorial exactness parity-barrier review frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_combinatorial_exactness_parity_barrier_review_router.py
docs/monograph/prime-matrix-phi-lpf-combinatorial-exactness-parity-barrier-review-router.md
docs/monograph/prime-matrix-phi-lpf-combinatorial-exactness-parity-barrier-review-router.json
data/prime-matrix-phi-lpf-combinatorial-exactness-parity-barrier-review-ledger.json
```

同步结果：

```text
status=review_absorbed_phi_lpf_exactness_is_not_positivity
accepted_review_core=true
numeric_update=BHP 0.525 has a newer 0.52 arXiv refinement, but both remain >1/2
current_frontier_after_review=PuncturedParityEndpointCapacityInequalityOrReciprocalPrimePairSaturationPDEC
unconditional_target_closure_reached=false
```

formal-to-actual 含义是：外部评审指出的核心问题成立，必须作为硬约束吸收。Phi-LPF/LPF
桶恒等式是组合精确：

```text
N_P(k)=DeltaPhi_half(P,k)-|F(P,k)|
```

但它本身不是素数正性下界。要推出 `N_P(k)>=1`，必须另行证明

```text
DeltaPhi_half(P,k)>|F(P,k)|
```

或更强的奇偶容量版本

```text
DeltaPhi_half(P,k)>C_par(P,k).
```

在最坏顶端带 `k≈P` 中，`x=kP≈P^2` 而目标长度是 `P≈sqrt(x)`。BHP `0.525`
或更新的 `0.52` 级普通短区间输入在 `X=P^2` 上仍给出 `P^1.05` 或 `P^1.04`
量级，不能推出长度 `P` 内的素数。线性筛下界在该尺度处也处在奇偶屏障区间，不能从无符号
LPF 容量账本直接产生正性。

因此后续非循环路线被收窄为三类：

```text
External sqrt-scale short interval input
OR Special square-phase/CRT structural lower bound
OR Signed transport / dispersion source route
```

被排除为闭合路线的是：

```text
Finite verification after theta>1/2
Capacity-only LPF/Phi rewriting
```

本层是路线校正和防错证书，不证明三目标命题。当前最窄口仍为：

```text
PuncturedParityEndpointCapacityInequalityOrReciprocalPrimePairSaturationPDEC.
```

## 461. H_P/Cramer-local route reset frontier

新增文件

```text
experiments/prime_matrix_hp_cramer_local_route_reset_router.py
docs/monograph/prime-matrix-hp-cramer-local-route-reset-router.md
docs/monograph/prime-matrix-hp-cramer-local-route-reset-router.json
data/prime-matrix-hp-cramer-local-route-reset-ledger.json
```

同步结果：

```text
status=hp_cramer_local_route_reset_after_parity_barrier_review
review_core_accepted=true
hp_direct_unconditional_closure_claim_allowed=false
current_frontier_after_reset=ExactExternalSqrtScaleOrFullSNonAPWFDKLSTheoremMatch OR NewAutomorphicDispersionProof OR SpecialSquarePhaseStructuralLowerBoundBeyondParity
```

formal-to-actual 含义是：更强评审已经吸收。`H_P` 的最坏 strict 顶端带满足

```text
k≈P, x=kP≈P^2, target interval length P≈sqrt(x).
```

这就是 Legendre/Cramer-local 短区间尺度。Phi-LPF、LPF bucket、CRT wheel、
Eratosthenes 筛等价公式仍然有价值，但它们只构成精确 reduction library 和反例结构定位。
在无新带符号取消、无 sqrt-scale 外部输入、无 special square-phase 下界的情况下，继续在
这些无符号等价公式内部重命名接口不能产生 `N_P(k)>=1`。

因此被降级或排除的路线为：

```text
Phi-LPF/Eratosthenes capacity rewriting -> demoted to reduction library
finite verification + theta>1/2 -> rejected as global closure
direct H_P unconditional closure claim -> not allowed
```

后续主攻路线重置为：

```text
Exact external theorem-match
OR DI/BFI/Kuznetsov self-contained appendix
OR automorphic L-functions / trace formula
OR genuinely new special square-phase structural lower bound
```

FI/DI/BFI/Maynard/自守工具被保留为高风险高回报技术族；现有仓库没有 ready-made theorem
直接覆盖 `H_P` 主命题。下一步必须写出精确 theorem-match checklist：变量、权重、模数范围、
窗口、平滑/投影、误差保存、常数和目标对象逐项验收。

## 331. Phi-LPF step local factor update frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_step_local_factor_update_frontier_router.py
docs/monograph/prime-matrix-phi-lpf-step-local-factor-update-frontier-router.md
docs/monograph/prime-matrix-phi-lpf-step-local-factor-update-frontier-router.json
data/prime-matrix-phi-lpf-step-local-factor-update-frontier-ledger.json
```

同步结果：

```text
ordered_lpf_edge_path_imported=true
step_update_reduced_to_edge_multiplier_table=true
edge_signed_multiplier_table_proved=false
rough_cofactor_step_local_factor_update_law_proved=false
pointwise_phi_lpf_bucket_signed_value_table_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：LPF ordered coherence 只固定每个 `p`-rough cofactor 的
非降素因子路径，不携带 actual signed coefficient。路径固定后，step local-factor
update 等价于一张逐 ordered edge 的 signed multiplier 表；第一边 `prefix=1` 也必须由
这张表正向给出，不能读取 Phi 中被减掉的 prime row，也不能从 downstream payment 原像
反推。

当前层关闭的是路径/递推接口的定位问题。真正未闭合的是：

```text
PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward
OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
OR ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn
OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn
```

并行仍需：

```text
ActualEmitterSourceDomainEntropyLedger
AND ExactUVMapFixedPairPolylogFiberBoundLedger
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

行/列命题仍未无条件闭合。

## 332. Phi-LPF first-edge slab frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_first_edge_slab_frontier_router.py
docs/monograph/prime-matrix-phi-lpf-first-edge-slab-frontier-router.md
docs/monograph/prime-matrix-phi-lpf-first-edge-slab-frontier-router.json
data/prime-matrix-phi-lpf-first-edge-slab-frontier-ledger.json
```

同步结果：

```text
edge_signed_multiplier_table_imported=true
edge_table_split_into_first_seed_and_internal_transition=true
first_edge_phi_fiber_formula_proved=true
semiprime_first_edge_signed_seed_table_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
edge_signed_multiplier_table_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：edge multiplier 表不能再作为一个匿名黑箱。LPF ordered path
固定后，每条路径先经过 semiprime first edge `(p,1,q,q)`，其 continuation fiber 精确由
`Phi(floor(N/(p*q)),q)` 给出；之后才进入 `prefix>1` 的内部 prime-adjoin transition。
这把无符号支撑质量和 signed 生成源分开：Phi 纤维公式只给每个 `(p,q)` 的 occurrence
mass，不给 first seed signed value，也不保证内部 transition 的非零前缀。

当前真正未闭合的是：

```text
PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward
AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
```

并行替代为：

```text
PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
OR ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn
OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn
OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput
OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
```

ExactUV、模型余量、RatePreservation 与 DStructure/Rankin 仍是并行门。行/列命题仍未
无条件闭合。

## 333. Phi-LPF semiprime seed diagonal frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_semiprime_seed_diagonal_frontier_router.py
docs/monograph/prime-matrix-phi-lpf-semiprime-seed-diagonal-frontier-router.md
docs/monograph/prime-matrix-phi-lpf-semiprime-seed-diagonal-frontier-router.json
data/prime-matrix-phi-lpf-semiprime-seed-diagonal-frontier-ledger.json
```

同步结果：

```text
semiprime_first_edge_signed_seed_target_imported=true
diagonal_offdiagonal_support_split_proved=true
diagonal_square_base_private_signed_escape_removed=true
diagonal_common_packet_signed_source_proved=false
offdiagonal_ordered_semiprime_signed_seed_table_proved=false
semiprime_first_edge_signed_seed_table_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：first-edge semiprime seed 的 diagonal 部分已经不是新 signed
逃逸口；`(p,p)` 被 square-base source packet reduction 送回 common pre-Cauchy source
packet。剩余 signed 新口集中在 offdiagonal ordered semiprime seeds `(p,q), p<q`。
Phi/LPF 给出这些 seed 类型和 occurrence 的精确分桶，但不提供它们的 sign、branch trace
或 ExactUV 输出。

当前真正未闭合的是：

```text
PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward
AND PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket
AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
```

并行替代仍为逐点 signed table、branch trace、atomic trace、seed cycle-cut、same-set PDEC
或 new joint formula；ExactUV、模型余量、RatePreservation 与 DStructure/Rankin 仍开放。
行/列命题仍未无条件闭合。

## 334. Phi-LPF offdiagonal semiprime seed tuple-fields frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_offdiagonal_semiprime_seed_tuple_fields_router.py
docs/monograph/prime-matrix-phi-lpf-offdiagonal-semiprime-seed-tuple-fields-router.md
docs/monograph/prime-matrix-phi-lpf-offdiagonal-semiprime-seed-tuple-fields-router.json
data/prime-matrix-phi-lpf-offdiagonal-semiprime-seed-tuple-fields-ledger.json
```

同步结果：

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

formal-to-actual 含义是：offdiagonal seed 的无符号来源字段已闭合为唯一 tuple

```text
(owner_p, first_rough_prime_q, q_rough_tail_t),  p<q,
```

并满足 fiber identity

```text
occ_N(p,q)=Phi(floor(N/(p*q)),q).
```

因此 `PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward`
不再是一个未解析黑箱；其 LPF/Phi 可贡献的字段已经用完。剩余 signed 缺口必须是
pushforward 前的 source tuple signed seed 公式、orientation parity/branch side、ExactUV
fixed pair/return tag，以及 tail 非单位时的 internal transition。样本 `N=10000` 中
offdiagonal 类型 `2600` 个、tuple occurrences `5468` 个，`tail=1/tail>1` 分解为
`2600/2868`。

当前真正未闭合的是：

```text
PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward
AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
AND PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket
```

并行替代仍为逐点 signed table、branch trace、atomic trace、seed cycle-cut、same-set PDEC
或 new joint formula；ExactUV、模型余量、RatePreservation 与 DStructure/Rankin 仍开放。
行/列命题仍未无条件闭合。

## 335. Phi-LPF offdiagonal pure semiprime seed atom frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_offdiagonal_pure_semiprime_seed_atom_router.py
docs/monograph/prime-matrix-phi-lpf-offdiagonal-pure-semiprime-seed-atom-router.md
docs/monograph/prime-matrix-phi-lpf-offdiagonal-pure-semiprime-seed-atom-router.json
data/prime-matrix-phi-lpf-offdiagonal-pure-semiprime-seed-atom-ledger.json
```

同步结果：

```text
offdiagonal_source_tuple_signed_seed_target_imported=true
pure_semiprime_pair_seed_atom_bijection_proved=true
tail_nonunit_reduced_to_internal_transition_lift=true
tail_lift_phi_minus_one_mass_formula_proved=true
pure_semiprime_pair_signed_seed_atom_proved=false
offdiagonal_source_tuple_signed_seed_formula_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：offdiagonal source tuple signed formula 的 first-seed 原子不能
放在全部 q-rough tail 上。真实 first seed 是唯一的 pure pair

```text
(p,q,tail=1),  p<q,
```

而 `tail>1` 只是在该 pure pair 之后继续走 internal transition。于是每个 `(p,q)` 的
continuation 质量是

```text
Phi(floor(N/(p*q)),q)-1.
```

样本 `N=10000` 中 `2600` 个 pure pair atoms 与 `2868` 个 tail-lift occurrences
合成上一层 `5468` 个 offdiagonal occurrences。这一步进一步移除了“tail continuation
也是新的 first seed”的误出口。

当前真正未闭合的是：

```text
PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward
AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
AND PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket
```

并行替代仍为逐点 signed table、branch trace、atomic trace、seed cycle-cut、same-set PDEC
或 new joint formula；ExactUV、模型余量、RatePreservation 与 DStructure/Rankin 仍开放。
行/列命题仍未无条件闭合。

## 336. Phi-LPF pure pair Ferrers support frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_pure_pair_ferrers_support_router.py
docs/monograph/prime-matrix-phi-lpf-pure-pair-ferrers-support-router.md
docs/monograph/prime-matrix-phi-lpf-pure-pair-ferrers-support-router.json
data/prime-matrix-phi-lpf-pure-pair-ferrers-support-ledger.json
```

同步结果：

```text
pure_pair_signed_atom_target_imported=true
pure_pair_ferrers_support_rule_proved=true
pure_pair_degree_ledger_proved=true
support_graph_signed_kernel_emission_proved=false
two_prime_signed_interaction_kernel_proved=false
pure_semiprime_pair_signed_seed_atom_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：pure pair atom 的所有无符号支撑自由度已压成一个 Ferrers 图：

```text
L={p prime: p<=sqrt(N)},   R={q prime},   edge(p,q) iff p<q<=N/p.
```

若 `p<r`，则 `N(r) subset N(p)`，所以左邻域嵌套下降。edge count、left degree、
right degree 都不是新的命题输入；它们由 prime table 和 `floor(N/p)` 逐项复算。
样本 `N=10000` 中 `25` 个左层、`668` 个右顶点、`2600` 条边，度数和嵌套均一致。

当前真正未闭合的是：

```text
PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward
AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
AND PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket
```

并行替代仍为逐点 signed table、branch trace、atomic trace、seed cycle-cut、same-set PDEC
或 new joint formula；ExactUV、模型余量、RatePreservation 与 DStructure/Rankin 仍开放。
行/列命题仍未无条件闭合。

## 337. Phi-LPF two-prime ordered no-swap frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_two_prime_ordered_no_swap_router.py
docs/monograph/prime-matrix-phi-lpf-two-prime-ordered-no-swap-router.md
docs/monograph/prime-matrix-phi-lpf-two-prime-ordered-no-swap-router.json
data/prime-matrix-phi-lpf-two-prime-ordered-no-swap-ledger.json
```

同步结果：

```text
two_prime_signed_kernel_target_imported=true
lpf_owner_ordered_no_swap_identity_proved=true
product_symmetry_signed_emission_proved=false
edge_local_two_prime_signed_formula_proved=false
two_prime_signed_interaction_kernel_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：`p*q=q*p` 的整数乘法对称不产生第二个 pre-Cauchy source row。
在 LPF owner domain 中，distinct semiprime product 只对应 canonical ordered edge
`(p,q)` with `p<q`。反向 `(q,p)` 会让 owner 不是最小素因子，因此不属于同一
source domain。样本 `N=10000` 中 ordered edges `2600`、unordered products `2600`、
reverse edges `0`、duplicates `0`。

当前真正未闭合的是：

```text
PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward
AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
AND PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket
```

并行替代仍为逐点 signed table、branch trace、atomic trace、seed cycle-cut、same-set PDEC
或 new joint formula；ExactUV、模型余量、RatePreservation 与 DStructure/Rankin 仍开放。
行/列命题仍未无条件闭合。

## 338. Phi-LPF edge-local two-prime field-cut frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_edge_local_two_prime_field_cut_router.py
docs/monograph/prime-matrix-phi-lpf-edge-local-two-prime-field-cut-router.md
docs/monograph/prime-matrix-phi-lpf-edge-local-two-prime-field-cut-router.json
data/prime-matrix-phi-lpf-edge-local-two-prime-field-cut-ledger.json
```

同步结果：

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

formal-to-actual 含义是：`PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward`
中所有 LPF/Ferrers 可读字段已经降为 closed unsigned edge label：

```text
owner_p, first_q, product_pq, lpf_bucket, ferrers_row_rank_and_degree,
ferrers_column_rank_and_degree, edge_atom_multiplicity
```

这些字段不含 sign、local factor、orientation parity、alpha/delta side、ExactUV fixed
pair 或 pre-Cauchy source row。样本 `N=10000` 中 canonical edges、unique labels 与
unique products 均为 `2600`，LPF/row degree/column degree/atom multiplicity 均闭合。

当前真正未闭合的是：

```text
PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward
AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
AND PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket
```

并行替代仍为逐点 signed table、branch trace、atomic trace、seed cycle-cut、same-set PDEC
或 new joint formula；ExactUV、模型余量、RatePreservation 与 DStructure/Rankin 仍开放。
行/列命题仍未无条件闭合。

## 339. Phi-LPF edge-local signed atom trace-sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_edge_local_signed_atom_trace_sync_router.py
docs/monograph/prime-matrix-phi-lpf-edge-local-signed-atom-trace-sync-router.md
docs/monograph/prime-matrix-phi-lpf-edge-local-signed-atom-trace-sync-router.json
data/prime-matrix-phi-lpf-edge-local-signed-atom-trace-sync-ledger.json
```

同步结果：

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

formal-to-actual 含义是：edge-local signed atom fields 已不再是 LPF/Phi 支撑问题。每条
closed unsigned edge label 要成为 signed edge-local formula，必须绑定同一 pre-Cauchy
trace key，并同时携带：

```text
signed value, local factor, orientation/branch side, alpha/delta payload,
ExactUV fixed pair, pre-Cauchy source row, return tag
```

任一字段缺失、冲突、零因子、超预算或后验读取，都必须进入 named return/PDEC。样本
`N=10000` 中 `2600` 个 edge trace packets 对应 `15600` 个开放 signed slots。

现有 branch-trace/atomic-trace 路线已被 signed-lane cycle closure 标记为不能自证。因此
当前真正未闭合的是：

```text
NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact
OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
```

并且仍需合取：

```text
ActualEmitterSourceDomainEntropyLedger
AND ExactUVMapFixedPairPolylogFiberBoundLedger
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

行/列命题仍未无条件闭合。

## 340. Phi-LPF new-payload source-atom alignment sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_new_payload_source_atom_alignment_sync_router.py
docs/monograph/prime-matrix-phi-lpf-new-payload-source-atom-alignment-sync-router.md
docs/monograph/prime-matrix-phi-lpf-new-payload-source-atom-alignment-sync-router.json
data/prime-matrix-phi-lpf-new-payload-source-atom-alignment-sync-ledger.json
```

同步结果：

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
next_primary_attack_target=ActualPreCauchySourceDomainAbsoluteEntropyLedger
```

formal-to-actual 含义是：`NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact` 不能在
Phi-LPF edge-local 线中保留为一个匿名新终点。它若只是 trace、payload、origin 或 common
packet 的改名，就落回 signed-lane 自证环；若要成为真正的新工件，就必须在 Cauchy/Phi/payment
前携带同一 actual source-rank/no-collapse 包。

因此最新非循环基变为：

```text
((ActualPreCauchySourceDomainAbsoluteEntropyLedger
  AND CompletePrimitiveEmitterKeyPartitionLedger
  AND FixedKeyExactUVLocalMultiplicityO1Ledger)
 OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
 OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward)
AND ActualEmitterSourceDomainEntropyLedger
AND ExactUVMapFixedPairPolylogFiberBoundLedger
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

LPF/Phi 的精准桶与 Phi 递推继续作为无符号支撑、容量和 fiber 账本使用；它们不能单独推出
signed coefficient 或 local factor。行/列命题仍未无条件闭合。

## 341. Phi-LPF source entropy signed-survival frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_source_entropy_signed_survival_router.py
docs/monograph/prime-matrix-phi-lpf-source-entropy-signed-survival-router.md
docs/monograph/prime-matrix-phi-lpf-source-entropy-signed-survival-router.json
data/prime-matrix-phi-lpf-source-entropy-signed-survival-ledger.json
```

同步结果：

```text
phi_lpf_candidate_capacity_ledger_closed=true
lpf_candidate_row_map_closed=true
candidate_capacity_audit_closed=true
candidate_rows_are_actual_signed_rows=false
nonzero_signed_row_survival_proved=false
actual_noncanonical_primitive_summand_signed_weight_expression_proved=false
same_formal_unit_row_mass_normalization_proved=false
source_domain_absolute_entropy_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward
```

formal-to-actual 含义是：LPF/Phi 桶公式已经给出完整的无符号候选容量，但 actual source
entropy 要求的是同一 formal unit 中的非零 signed row 质量。候选容量只说明“可发射位置”；
actual load 必须来自 signed coefficient 已经前推前给出的行。

因此本层把 source entropy 的支撑子原子切成：

```text
PrimitiveRowSupportLowerBoundBeforeExactUVProjectionLedger
->
PhiLPFCandidateRowCapacityLowerBoundLedger
AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
```

其中 `PhiLPFCandidateRowCapacityLowerBoundLedger` 由 LPF 唯一 ownership 与 Phi 递推关闭；
`NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward` 仍未证明，并依赖：

```text
ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward
SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
```

这一步删除了“Phi 计数本身就是 source entropy”的伪出口。行/列命题仍未无条件闭合。

## 342. Phi-LPF signed-survival origin-table sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_signed_survival_origin_table_sync_router.py
docs/monograph/prime-matrix-phi-lpf-signed-survival-origin-table-sync-router.md
docs/monograph/prime-matrix-phi-lpf-signed-survival-origin-table-sync-router.json
data/prime-matrix-phi-lpf-signed-survival-origin-table-sync-ledger.json
```

同步结果：

```text
phi_lpf_candidate_capacity_remains_closed=true
primitive_expression_reduced_to_origin_identity=true
origin_identity_reduced_to_row_level_generation=true
row_level_clean_core_origin_generation_table_proved=false
nonzero_signed_row_survival_proved=false
same_formal_unit_row_mass_normalization_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands
```

formal-to-actual 含义是：Phi-LPF 候选 row 的 signed survival 不能由一个未解释的 signed
expression 字段直接支付。表达式必须先给出 pre-Cauchy signed coefficient 来源恒等式；来源
恒等式再等价于逐行 clean-core 原始生成表：

```text
NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
->
ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward
->
PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward
->
RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands
```

LPF/Phi 桶恒等式仍只负责 closed unsigned candidate capacity。最新非循环硬点是逐行原始
生成表；若该表仍缺失，则 Phi-LPF 候选容量不能升级成 actual signed source entropy。
行/列命题仍未无条件闭合。

## 343. Row-origin table Phi-LPF bucket signed-law sync frontier

新增文件

```text
experiments/prime_matrix_row_origin_table_phi_lpf_bucket_law_sync_router.py
docs/monograph/prime-matrix-row-origin-table-phi-lpf-bucket-law-sync-router.md
docs/monograph/prime-matrix-row-origin-table-phi-lpf-bucket-law-sync-router.json
data/prime-matrix-row-origin-table-phi-lpf-bucket-law-sync-ledger.json
```

同步结果：

```text
row_level_origin_table_imported=true
row_table_requires_seed_emitter=true
signed_source_fixed_point_cut_imported=true
noncircular_kernel_imported=true
phi_lpf_support_stripping_imported=true
phi_lpf_support_and_capacity_closed=true
row_origin_table_reduced_to_phi_lpf_bucket_signed_law=true
phi_lpf_bucket_signed_coefficient_law_proved=false
same_formal_unit_row_mass_normalization_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFBucketSignedCoefficientLawBeforePushforward
```

formal-to-actual 含义是：`RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands`
不能继续被当作未拆开的黑箱。既有 row-level、signed-source fixed-point 与 support-stripped
证书给出非循环同步链：

```text
RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands
->
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity
->
NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows
->
PhiLPFPrimitiveRowSupportAndCapacityLedger
AND PhiLPFBucketSignedCoefficientLawBeforePushforward
```

其中 `PhiLPFPrimitiveRowSupportAndCapacityLedger` 已由 LPF ownership 和 Phi 递推关闭；最新
真正硬点只剩桶级 signed coefficient law。该 law 必须在 Cauchy/payment 前对每个 `(p,m)`
support key 正向给出 signed coefficient、sign/local factor、branch key 与推前前 alpha/delta
求和恒等式。行/列命题仍未无条件闭合。

## 344. Phi-LPF latest bucket transport-stack sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_bucket_transport_stack_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-bucket-transport-stack-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-bucket-transport-stack-sync-router.json
data/prime-matrix-phi-lpf-latest-bucket-transport-stack-sync-ledger.json
```

同步结果：

```text
latest_bucket_signed_law_imported=true
bucket_transport_router_imported=true
unit_seed_boundary_imported=true
ordered_coherence_closed=true
step_update_reduced_to_edge_multiplier=true
square_base_private_escape_removed=true
common_packet_cycle_guard_imported=true
edge_signed_multiplier_table_proved=false
pointwise_signed_table_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward
```

formal-to-actual 含义是：桶级 signed law 的“递推闭合”不是由 Phi 计数给出的。Phi/LPF 给
support 与 ordered path；若要让 signed law 沿 rough cofactor 递推，必须同时给出启动口径和
每步 signed multiplier。既有证书同步为：

```text
PhiLPFBucketSignedCoefficientLawBeforePushforward
->
PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward
->
PhiLPFUnitCofactorVirtualSeedOrSquareBaseSignedCoefficientBeforePushforward
AND PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward
AND PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward
```

其中 ordered coherence 已闭合；unit/square-base 私有 signed 出口已并回 common source-packet
cycle guard；step update 已压成逐 ordered edge signed multiplier 表。因此最新递推剩余基为：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger
AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
AND PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward
```

并行直接旁路仍是
`PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward`。行/列命题仍未
无条件闭合。

## 345. Phi-LPF latest edge multiplier slab sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_edge_multiplier_slab_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-edge-multiplier-slab-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-edge-multiplier-slab-sync-router.json
data/prime-matrix-phi-lpf-latest-edge-multiplier-slab-sync-ledger.json
```

同步结果：

```text
latest_transport_hardpoint_imported=true
first_edge_slab_router_imported=true
edge_multiplier_split_synced_to_latest_basis=true
first_edge_phi_fiber_formula_imported=true
phi_fiber_unsigned_only_guard=true
semiprime_first_edge_signed_seed_table_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
edge_signed_multiplier_table_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward
```

formal-to-actual 含义是：最新 transport-stack 中的逐 edge signed multiplier 表已经能接到
既有 first-edge slab 拆解。固定 owner prime `p` 与 LPF ordered cofactor path 后，第一边
必为 `(p,1,q,q)`，后续所有边才是 `prefix>1` 的 internal prime-adjoin transitions。因此：

```text
PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward
->
PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward
AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
```

第一边的无符号 continuation mass 已由
`Phi(floor(N/(p*q)),q)` 支付；样本 `N=10000` 给出 support `8770`、first occurrences
`8770`、internal occurrences `13216`、first-edge types `2625`。但 Phi fiber 仍只给支撑和
occurrence mass，不给 signed seed value、local factor、orientation、alpha/delta payload、
ExactUV fixed pair 或 named return。

当前真正未闭合的是：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger
AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
AND PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward
AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
```

并行替代仍为逐点 Phi-LPF signed table、完整 branch/atomic trace、seed cycle-cut、
terminal descent、same-set PDEC 或 new joint formula；ExactUV、模型余量、RatePreservation
与 DStructure/Rankin 仍开放。行/列命题仍未无条件闭合。

## 346. Phi-LPF latest semiprime seed diagonal sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_semiprime_seed_diagonal_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-semiprime-seed-diagonal-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-semiprime-seed-diagonal-sync-router.json
data/prime-matrix-phi-lpf-latest-semiprime-seed-diagonal-sync-ledger.json
```

同步结果：

```text
latest_first_seed_hardpoint_imported=true
semiprime_diagonal_router_imported=true
diagonal_offdiagonal_support_split_closed=true
diagonal_private_escape_removed=true
common_packet_cycle_guard_carried_forward=true
latest_basis_replaces_first_seed_with_offdiag_seed=true
offdiagonal_ordered_semiprime_signed_seed_table_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward
```

formal-to-actual 含义是：最新 first-edge signed seed 缺口已经不需要同时视为 diagonal 与
offdiagonal 未拆黑箱。LPF ordered seed 类型满足 `p<=q`，因此强制二分为：

```text
p=q   diagonal square-base seed
p<q   offdiagonal ordered semiprime seed
```

diagonal `(p,p)` 已由 square-base route 证明没有私有 signed 出口；它回到 common source
packet，而该 packet 在最新前沿中已经以 source 三原子形式被携带。于是最新 retained basis
中可以把 `PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward` 替换为
`PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward`，并保留
`PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward`。

样本 `N=10000` 给出 first-edge seed types `2625`，其中 diagonal/offdiagonal types 为
`25/2600`；occurrence mass 为 `3302/5468`。这些仍只是支撑与 occurrence 账本，不产生
offdiagonal signed seed value、orientation、ExactUV return 或 internal transition。

当前真正未闭合的是：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger
AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
AND PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward
AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
```

并行替代仍为逐点 Phi-LPF signed table、完整 branch/atomic trace、seed cycle-cut、
terminal descent、same-set PDEC 或 new joint formula；ExactUV、模型余量、RatePreservation
与 DStructure/Rankin 仍开放。行/列命题仍未无条件闭合。

## 347. Phi-LPF latest offdiagonal seed tuple sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_offdiagonal_seed_tuple_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-offdiagonal-seed-tuple-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-offdiagonal-seed-tuple-sync-router.json
data/prime-matrix-phi-lpf-latest-offdiagonal-seed-tuple-sync-ledger.json
```

同步结果：

```text
latest_offdiagonal_seed_hardpoint_imported=true
offdiagonal_tuple_fields_router_imported=true
offdiagonal_source_tuple_bijection_synced=true
offdiagonal_phi_tail_fiber_mass_synced=true
offdiagonal_unsigned_tuple_fields_closed=true
lpf_phi_unsigned_scope_exhausted_for_offdiag_seed=true
latest_basis_replaces_offdiag_seed_with_tuple_payload=true
offdiagonal_signed_seed_formula_proved=false
offdiagonal_orientation_parity_law_proved=false
offdiagonal_exactuv_fixed_pair_return_ledger_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward
```

formal-to-actual 含义是：最新 offdiagonal ordered semiprime seed 表已经接入
tuple-fields 拆解。对每个 `p<q` seed occurrence，LPF/Phi 只给出唯一 tuple

```text
(owner_p, first_rough_prime_q, q_rough_tail_t)
```

以及精确 tail 纤维：

```text
occ_N(p,q)=Phi(floor(N/(p*q)),q).
```

因此 `PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward`
不再保留匿名 LPF/Phi 黑箱。它的无符号来源字段已经用尽，剩余只能是 pushforward
前的 signed source tuple 公式、orientation parity/branch side、ExactUV fixed pair/return tag，
以及 tail continuation 所需的 internal prime-adjoin transition。样本 `N=10000` 给出
offdiagonal types `2600`、tuple occurrences `5468`、Phi sum `5468`，tail `1/>1`
分解为 `2600/2868`。

当前真正未闭合的是：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger
AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
AND PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward
AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
```

并行替代仍为逐点 Phi-LPF signed table、完整 branch/atomic trace、seed cycle-cut、
terminal descent、same-set PDEC 或 new joint formula；ExactUV、模型余量、RatePreservation
与 DStructure/Rankin 仍开放。行/列命题仍未无条件闭合。

## 348. Phi-LPF latest offdiagonal pure-pair atom sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_offdiagonal_pure_pair_atom_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-offdiagonal-pure-pair-atom-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-offdiagonal-pure-pair-atom-sync-router.json
data/prime-matrix-phi-lpf-latest-offdiagonal-pure-pair-atom-sync-ledger.json
```

同步结果：

```text
latest_source_tuple_signed_formula_imported=true
pure_pair_atom_router_imported=true
pure_pair_atom_bijection_synced=true
tail_lift_phi_minus_one_synced=true
tail_lift_no_new_first_seed_closed=true
latest_basis_replaces_tuple_formula_with_pure_atom=true
pure_semiprime_pair_signed_seed_atom_proved=false
offdiagonal_orientation_parity_law_proved=false
offdiagonal_exactuv_fixed_pair_return_ledger_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward
```

formal-to-actual 含义是：最新 source tuple signed seed formula 已经不再需要同时处理
所有 `q`-rough tail occurrence。first seed 原子强制是每个 ordered type `(p,q), p<q`
的唯一 tail=1 tuple：

```text
(p,q,1), value=p*q.
```

tail 非单位部分只有 continuation 意义，其质量为

```text
Phi(floor(N/(p*q)),q)-1.
```

因此它必须进入 internal prime-adjoin transition compatibility，而不能登记为新的 first seed
来源。样本 `N=10000` 给出 pure pair atoms `2600`、tail lift `2868`、total
offdiagonal occurrences `5468`。

当前真正未闭合的是：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger
AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
AND PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward
AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
```

并行替代仍为逐点 Phi-LPF signed table、完整 branch/atomic trace、seed cycle-cut、
terminal descent、same-set PDEC 或 new joint formula；ExactUV、模型余量、RatePreservation
与 DStructure/Rankin 仍开放。行/列命题仍未无条件闭合。

## 349. Phi-LPF latest pure-pair Ferrers support sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_pure_pair_ferrers_support_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-pure-pair-ferrers-support-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-pure-pair-ferrers-support-sync-router.json
data/prime-matrix-phi-lpf-latest-pure-pair-ferrers-support-sync-ledger.json
```

同步结果：

```text
latest_pure_pair_atom_imported=true
ferrers_support_router_imported=true
ferrers_support_rule_synced=true
ferrers_degree_ledger_synced=true
support_graph_signed_kernel_emission_proved=false
latest_basis_replaces_pure_atom_with_two_prime_kernel=true
two_prime_signed_interaction_kernel_proved=false
offdiagonal_orientation_parity_law_proved=false
offdiagonal_exactuv_fixed_pair_return_ledger_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward
```

formal-to-actual 含义是：最新 pure-pair atom 的支撑/度数层已经完全剥离。支撑图是
二素数 Ferrers 图：

```text
left p <= sqrt(N), right prime q, edge iff p<q<=N/p.
```

随着 `p` 增大，右邻域嵌套下降；总边数、left degree、right degree 均由素数表与
`floor(N/p)` 支付。样本 `N=10000` 给出 left layers `25`、right vertices `668`、
pure-pair edges `2600`。这一步关闭的是支撑和度数，不产生每条边的 signed value、
orientation、local factor 或 ExactUV return。

当前真正未闭合的是：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger
AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
AND PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward
AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
```

并行替代仍为逐点 Phi-LPF signed table、完整 branch/atomic trace、seed cycle-cut、
terminal descent、same-set PDEC 或 new joint formula；ExactUV、模型余量、RatePreservation
与 DStructure/Rankin 仍开放。行/列命题仍未无条件闭合。

## 350. Phi-LPF latest two-prime no-swap sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_two_prime_no_swap_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-two-prime-no-swap-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-two-prime-no-swap-sync-router.json
data/prime-matrix-phi-lpf-latest-two-prime-no-swap-sync-ledger.json
```

同步结果：

```text
latest_two_prime_kernel_imported=true
no_swap_router_imported=true
lpf_owner_ordered_no_swap_synced=true
product_symmetry_signed_emission_proved=false
latest_basis_replaces_two_prime_kernel_with_edge_local_formula=true
edge_local_two_prime_signed_formula_proved=false
two_prime_signed_interaction_kernel_proved=false
offdiagonal_orientation_parity_law_proved=false
offdiagonal_exactuv_fixed_pair_return_ledger_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward
```

formal-to-actual 含义是：最新 two-prime signed kernel 的交换对称伪出口已经被切掉。
LPF owner source domain 只保留 canonical ordered edge `(p,q)` with `p<q`。虽然整数
乘法满足

```text
p*q=q*p,
```

但 reverse edge `(q,p)` 不属于同一 pre-Cauchy source domain，不能被当作 signed
cancellation partner 或第二条 source row。样本 `N=10000` 中 ordered edges 与 unordered
products 均为 `2600`，reverse edges `0`，duplicates `0`。

当前真正未闭合的是：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger
AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
AND PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward
AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
```

并行替代仍为逐点 Phi-LPF signed table、完整 branch/atomic trace、seed cycle-cut、
terminal descent、same-set PDEC 或 new joint formula；ExactUV、模型余量、RatePreservation
与 DStructure/Rankin 仍开放。行/列命题仍未无条件闭合。

## 351. Phi-LPF latest edge-local field-cut sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_edge_local_field_cut_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-edge-local-field-cut-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-edge-local-field-cut-sync-router.json
data/prime-matrix-phi-lpf-latest-edge-local-field-cut-sync-ledger.json
```

同步结果：

```text
latest_edge_local_formula_imported=true
field_cut_router_imported=true
closed_unsigned_edge_label_ledger_synced=true
edge_atom_multiplicity_one_synced=true
lpf_phi_unsigned_scope_exhausted_for_edge_local=true
latest_basis_replaces_edge_local_formula_with_signed_atom_fields=true
signed_atom_field_table_proved=false
orientation_parity_branch_side_proved=false
exactuv_fixed_pair_return_tag_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward
```

formal-to-actual 含义是：最新 edge-local signed interaction formula-or-return 的无符号
部分已经全部落入 field-cut。对每条 canonical `(p,q)` edge，LPF/Phi/Ferrers 支付
owner、first prime、product、rank/degree 与 multiplicity-one label；这些字段不能产生
signed seed value、local factor、orientation、ExactUV return 或 pre-Cauchy source row。
样本 `N=10000` 中 canonical edges、labels、products 均为 `2600`，每条 edge 仍有 `6`
个开放 signed/return 字段。

当前真正未闭合的是：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger
AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
AND PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward
AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
```

并行替代仍为逐点 Phi-LPF signed table、完整 branch/atomic trace、seed cycle-cut、
terminal descent、same-set PDEC 或 new joint formula；ExactUV、模型余量、RatePreservation
与 DStructure/Rankin 仍开放。行/列命题仍未无条件闭合。

## 352. Phi-LPF latest signed atom trace-sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_signed_atom_trace_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-signed-atom-trace-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-signed-atom-trace-sync-router.json
data/prime-matrix-phi-lpf-latest-signed-atom-trace-sync-ledger.json
```

同步结果：

```text
latest_signed_atom_fields_imported=true
trace_sync_router_imported=true
closed_unsigned_labels_carried=true
same_trace_key_and_named_return_matrix_synced=true
trace_self_proof_cycle_cut_synced=true
latest_basis_replaces_signed_atom_fields_with_new_payload_or_exits=true
new_primitive_payload_or_trace_artifact_present=false
edge_local_signed_atom_fields_proved=false
pointwise_phi_lpf_bucket_signed_value_table_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact
```

formal-to-actual 含义是：最新 signed atom fields 已被接入同 trace key 与命名 return
矩阵。无符号 LPF/Phi/Ferrers label 不能产生 signed payload；真正可生产 signed value、
local factor、orientation、alpha/delta side、ExactUV fixed pair 与 source row 的只能是同一
pre-Cauchy trace key 上的新 payload/trace 工件。branch/atomic trace 自证环已被切掉，
样本 `N=10000` 中开放 signed slots 为 `15600`。

当前真正未闭合的是：

```text
NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact
OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
```

并仍需合取 ExactUV source/fiber、模型余量、RatePreservation 与 DStructure/Rankin。
行/列命题仍未无条件闭合。

## 353. Phi-LPF latest new-payload source-atom alignment sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_new_payload_source_atom_alignment_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-new-payload-source-atom-alignment-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-new-payload-source-atom-alignment-sync-router.json
data/prime-matrix-phi-lpf-latest-new-payload-source-atom-alignment-sync-ledger.json
```

同步结果：

```text
latest_new_payload_imported=true
latest_unsigned_labels_cannot_pay_payload=true
signed_lane_cycle_cut_carried=true
strict_new_payload_alignment_imported=true
latest_new_payload_reduced_to_source_rank_atom=true
independent_new_payload_terminal_present=false
actual_source_domain_entropy_proved=false
complete_primitive_emitter_key_partition_proved=false
fixed_key_exact_uv_local_multiplicity_proved=false
pointwise_phi_lpf_bucket_signed_value_table_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=ActualPreCauchySourceDomainAbsoluteEntropyLedger
```

formal-to-actual 含义是：latest new-payload 出口已经与 strict source-atom alignment 对齐。
LPF/Phi/Ferrers 的无符号字段与 trace-sync 的同 key 矩阵只给出输入域和命名 return；它们不能
产生真正破环的 signed payload。若 new payload 是独立新工件，它必须携带：

```text
ActualPreCauchySourceDomainAbsoluteEntropyLedger
AND CompletePrimitiveEmitterKeyPartitionLedger
AND FixedKeyExactUVLocalMultiplicityO1Ledger
```

当前真正未闭合的是上述三原子包，首攻项为
`ActualPreCauchySourceDomainAbsoluteEntropyLedger`；并行仍为 terminal descent、same-set PDEC、
逐点 signed table、ExactUV、模型、Rate 与 DStructure。行/列命题仍未无条件闭合。

## 354. Phi-LPF latest source-entropy downstream cycle sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_source_entropy_downstream_cycle_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-source-entropy-downstream-cycle-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-source-entropy-downstream-cycle-sync-router.json
data/prime-matrix-phi-lpf-latest-source-entropy-downstream-cycle-sync-ledger.json
```

同步结果：

```text
latest_source_entropy_imported=true
phi_lpf_candidate_capacity_boundary_carried=true
candidate_rows_are_actual_signed_rows=false
source_entropy_atom_sends_to_signed_law=true
source_entropy_downstream_edges_closed=true
seed_coordinate_source_cycle_detected=true
raw_cycle_counts_as_closure=false
primitive_basis_and_coefficient_source_input_proved=false
acyclic_terminal_descent_proved=false
complete_primitive_emitter_key_partition_proved=false
fixed_key_exact_uv_local_multiplicity_proved=false
pointwise_phi_lpf_bucket_signed_value_table_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput_OR_AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
```

formal-to-actual 含义是：latest new-payload/source-atom alignment 已把主攻点推到
`ActualPreCauchySourceDomainAbsoluteEntropyLedger`。本层将其接入 strict source entropy
downstream cycle guard，并同步携带 LPF/Phi 桶恒等式边界：候选容量已经由
`PhiLPFCandidateRowCapacityLowerBoundLedger` 关闭，但候选 row 不是 actual signed row，不能
自动支付 signed survival、row-mass 或推前前 signed coefficient。

沿下游展开，source entropy 先进入 signed coefficient law，再进入 basis weight source、
internal basis、basis alphabet，随后落入 signed 坐标-来源环。该环不能作为证明；若要继续
非循环闭合，必须提交

```text
AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput
```

或走 `AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate`。complete key、
fixed-key ExactUV local multiplicity、same-set PDEC、逐点 signed table、ExactUV、模型、Rate
与 DStructure/Rankin 仍开放。行/列命题仍未无条件闭合。

## 355. Phi-LPF latest cycle-cut terminal unified sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_cyclecut_terminal_unified_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-cyclecut-terminal-unified-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-cyclecut-terminal-unified-sync-router.json
data/prime-matrix-phi-lpf-latest-cyclecut-terminal-unified-sync-ledger.json
```

同步结果：

```text
latest_cycle_or_terminal_exit_imported=true
strict_unified_frontier_imported=true
seed_cycle_cut_branch_saturated=true
terminal_descent_macrocycle_detected=true
pdec_scope_internal_saturation_imported=true
new_joint_formula_reduced_to_declaration_line=true
pre_cauchy_joint_declaration_line_proved=false
joint_productive_field_basis_proved=false
canonical_lock_proved=false
independent_actual_source_bridge_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple
```

formal-to-actual 含义是：latest source-entropy 下游给出的
`AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput_OR_AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate`
不是终点。它与 strict cycle-cut/terminal/PDEC 统一前沿对齐后，cycle-cut 分支饱和到 PDEC
或 new joint，terminal descent 是宏循环，same-set PDEC 内部分支也不能给自足非循环出口。

因此当前内部第一生产性单点被压成：

```text
PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple
```

完整 joint 字段基仍为：

```text
PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple
AND JointEmitterPrimitiveSummandRowsFormulaBeforePushforward
AND JointEmitterPrepushforwardWordCoefficientIdentityLedger
AND JointEmitterNoDownstreamRecoveryAndNamedReturnLedger
```

canonical-lock、independent source bridge、same-set PDEC/外部谱、complete/fixed-key、ExactUV、
模型、Rate 与 DStructure 仍开放。行/列命题仍未无条件闭合。

## 356. Phi-LPF latest antisplit downstream sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_antisplit_downstream_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-antisplit-downstream-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-antisplit-downstream-sync-router.json
data/prime-matrix-phi-lpf-latest-antisplit-downstream-sync-ledger.json
```

同步结果：

```text
latest_joint_declaration_imported=true
strict_antisplit_downstream_imported=true
ordinary_joint_declaration_synced_to_constructor=true
ordinary_constructor_route_rejected_as_fixed_point=true
antisplit_atomic_route_imported=true
atomic_rows_reduced_to_builtin_pairing=true
exactuv_entropy_fiber_split_imported=true
built_in_signed_pairing_proved=false
actual_emitter_source_domain_entropy_proved=false
exact_uv_map_fixed_pair_polylog_fiber_bound_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
parallel_primary_attack_target=ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
```

formal-to-actual 含义是：latest joint declaration line 继续沿 strict 反分裂下游同步。普通 joint
declaration 会降到 explicit constructor；普通 constructor 已回到 signed-source 固定点，不能作为
非循环证明。因此真正自足路线必须走 atomic rows 反分裂，并把 signed 首缺口压到：

```text
BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
```

与此同时，ExactUV bounded incidence 并行门同步为：

```text
ActualEmitterSourceDomainEntropyLedger
AND ExactUVMapFixedPairPolylogFiberBoundLedger
```

当前最新内部下游基是 built-in pairing 与 ExactUV entropy/fiber 的合取。canonical-lock、
independent bridge、same-set PDEC/外部谱、complete/fixed-key、模型、Rate 与 DStructure 仍开放。
行/列命题仍未无条件闭合。

## 357. Phi-LPF latest built-in pairing trace sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_builtin_pairing_trace_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-builtin-pairing-trace-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-builtin-pairing-trace-sync-router.json
data/prime-matrix-phi-lpf-latest-builtin-pairing-trace-sync-ledger.json
```

同步结果：

```text
latest_builtin_pairing_imported=true
strict_builtin_pairing_frontier_imported=true
global_branch_trace_frontier_aligned=true
exact_atomic_joint_branch_trace_signed_coefficient_formula_proved=false
signed_lane_cycle_imported=true
branch_trace_self_proof_rejected=true
new_primitive_payload_or_trace_artifact_present=false
exactuv_entropy_fiber_pair_imported=true
actual_emitter_source_domain_entropy_proved=false
exact_uv_map_fixed_pair_polylog_fiber_bound_proved=false
row_column_unconditional_closed=false
intermediate_primary_attack_target=ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn
next_primary_attack_target=NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact
```

formal-to-actual 含义是：latest built-in pairing 必须先同步到 exact atomic branch trace；
但 exact branch trace 不能靠现有 signed/payload 子线自证，因为它会沿 payload、origin identity
和 common packet 回到 built-in pairing。该闭环只用于删除环内自证路线，不是全局矛盾。

因此当前最新非循环主攻为：

```text
NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact
```

并行出口为：

```text
AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger
FixedKeyExactUVLocalMultiplicityO1Ledger
```

这一步只替换最新活动前沿，不证明新 payload/trace、terminal descent、PDEC scope、source entropy、
fixed-pair fiber、模型、Rate 或 DStructure。行/列命题仍未无条件闭合。

## 358. Phi-LPF latest trace-exit source-rank convergence sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_trace_exit_source_rank_convergence_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-trace-exit-source-rank-convergence-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-trace-exit-source-rank-convergence-sync-router.json
data/prime-matrix-phi-lpf-latest-trace-exit-source-rank-convergence-sync-ledger.json
```

同步结果：

```text
latest_trace_exit_imported=true
latest_new_payload_source_atom_alignment_imported=true
source_rank_package_atoms_carried=true
post_antisplit_convergence_imported=true
source_packet_guard_downstream_imported=true
pointwise_kernel_frontier_imported=true
alpha_row_anchor_phase_emission_formula_proved=false
independent_noncircular_precauchy_arithmetic_identity_statement_proved=false
same_unit_exact_uv_rank_multiplicity_certificate_proved=false
exactuv_entropy_fiber_pair_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=AlphaRowAnchorPhaseEmissionFormulaLedger
```

formal-to-actual 含义是：latest trace-exit 得到的 `NewPrimitive...` 已被接到既有
source-rank/no-collapse 与 pointwise-kernel 收敛前沿。它若要破 signed-lane 环，必须携带
source entropy、complete key 与 fixed-key ExactUV local multiplicity；这些线又在同 formal-unit
的逐 primitive alpha/delta 核表汇合。

因此当前最新第一硬点为：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger
```

并行仍需：

```text
IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward AND
PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward
```

本层不证明这些并行门，也不关闭行/列命题。

## 359. Phi-LPF latest alpha terminal three-atoms sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_alpha_terminal_three_atoms_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-alpha-terminal-three-atoms-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-alpha-terminal-three-atoms-sync-router.json
data/prime-matrix-phi-lpf-latest-alpha-terminal-three-atoms-sync-ledger.json
```

同步结果：

```text
latest_alpha_frontier_imported=true
alpha_three_leg_terminal_leaf_imported=true
terminal_leaf_latest_noncycle_imported=true
new_joint_trace_cycle_absorbed=true
terminal_three_atoms_pinned=true
independent_moving_atom_chosen_as_narrowest=true
acyclic_terminal_canonical_lock_proved=false
a1_clean_branch_canonical_source_admission_proved=false
actual_noncanonical_clean_core_moving_atom_exclusion_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore
```

formal-to-actual 含义是：latest alpha 首攻点不再作为当前最深单点停留。已有 post-antisplit
alpha terminal leaf 证书说明 alpha/weight/rank 三腿分攻是固定点；post-alpha terminal leaf
和 three-atoms 证书又把旧 new-joint/trace/payload 路线吸收到 signed-lane cycle，并把当前
strict 前沿钉到：

```text
AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
A1CleanBranchCanonicalSourceAdmission
ActualNoncanonicalCleanCoreMovingAtomExclusion
```

最新直接主攻为：

```text
IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore
```

并行仍保留 canonical-lock、A1 admission、PDEC、ExactUV incidence、Rate、DStructure、逐点
Phi-LPF signed 表、ExactUV entropy/fiber 与 rough-cofactor transport/coherence。行/列命题仍未
无条件闭合。

## 360. Phi-LPF moving-atom source-bucket preimage sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_moving_atom_source_bucket_preimage_sync_router.py
docs/monograph/prime-matrix-phi-lpf-moving-atom-source-bucket-preimage-sync-router.md
docs/monograph/prime-matrix-phi-lpf-moving-atom-source-bucket-preimage-sync-router.json
data/prime-matrix-phi-lpf-moving-atom-source-bucket-preimage-sync-ledger.json
```

同步结果：

```text
latest_independent_moving_atom_frontier_imported=true
lpf_phi_composite_ownership_identity_imported=true
lpf_bucket_identity_sample_verified=true
moving_atom_unsigned_source_preimage_partition_closed=true
prime_row_leak_and_virtual_unit_preimage_blocked=true
signed_mass_injection_proved=false
rate_bearing_packet_exclusion_proved=false
independent_nonterminal_moving_atom_exclusion_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=LPFMovingAtomSignedPreimageMassInjectionLedger
```

formal-to-actual 含义是：LPF/Phi 精准桶恒等式已经足够关闭 moving atom 的无符号源前像问题。
任一来自 composite source 的 clean-core moving atom，其推前前源支撑必须按唯一 `(p,m)` 桶分解；
`p=LPF(pm)`，`m` 为 p-rough。Phi 公式中的 `m=1` 是 prime-row 修正，不是 composite source，
所以 virtual-unit/prime-row leak 不能作为 moving atom 前像。

本层没有证明 moving atom 排斥。真正剩余是从 final same-(u,v) 大原子向 LPF-owned 推前前源桶
注入 signed 质量，并同步给出 signed coefficient、local factor、alpha/delta branch、no-heavy-row
和速率保持。因此最新直接主攻变为：

```text
LPFMovingAtomSignedPreimageMassInjectionLedger
```

并行仍保留逐点 Phi-LPF signed 表、signed survival/row-mass、PDEC/CleanKLS 速率包、高段模型余量、
RatePreservation 和 DStructure/Rankin。行/列命题仍未无条件闭合。

## 361. Phi-LPF moving-atom signed-injection split frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_moving_atom_signed_injection_split_router.py
docs/monograph/prime-matrix-phi-lpf-moving-atom-signed-injection-split-router.md
docs/monograph/prime-matrix-phi-lpf-moving-atom-signed-injection-split-router.json
data/prime-matrix-phi-lpf-moving-atom-signed-injection-split-ledger.json
```

同步结果：

```text
lpf_preimage_partition_imported=true
signed_injection_has_no_unsigned_remainder=true
half_mass_sign_lane_extraction_finite_algebra_closed=true
prepushforward_same_uv_identity_proved=false
pointwise_phi_lpf_bucket_signed_value_table_proved=false
signed_survival_and_row_mass_proved=false
signed_injection_ledger_current_corpus_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
```

formal-to-actual 含义是：`LPFMovingAtomSignedPreimageMassInjectionLedger` 不再是独立计数硬点。
LPF-owned source buckets 已经给出无符号前像；一旦逐点 prepushforward same-`(u,v)` signed sum
identity 存在，大原子的 sign-lane 半质量抽取就是有限代数。缺失的不是桶数量，而是逐点 signed
coefficient/local factor/alpha-delta branch/推前前恒等式，以及同 formal unit 的 signed survival
和 row-mass/no-heavy-row。

因此最新直接主攻同步为：

```text
PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
```

并行保留完整 bucket signed law、primitive summand signed expression、signed survival、row-mass、
PDEC/CleanKLS 速率包、高段模型余量、RatePreservation 和 DStructure/Rankin。行/列命题仍未
无条件闭合。

## 362. Phi-LPF pointwise signed table orientation-law sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_pointwise_signed_table_orientation_law_sync_router.py
docs/monograph/prime-matrix-phi-lpf-pointwise-signed-table-orientation-law-sync-router.md
docs/monograph/prime-matrix-phi-lpf-pointwise-signed-table-orientation-law-sync-router.json
data/prime-matrix-phi-lpf-pointwise-signed-table-orientation-law-sync-ledger.json
```

同步结果：

```text
latest_pointwise_phi_lpf_signed_table_imported=true
pointwise_table_reduced_to_signed_alpha_weight=true
signed_alpha_weight_reduced_to_primitive_summand_expression=true
primitive_summand_expression_reduced_to_origin_identity=true
origin_identity_reduced_to_row_level_generation=true
signed_value_cycle_detected=true
noncircular_emission_kernel_imported=true
orientation_local_factor_law_imported_as_first_field=true
orientation_local_factor_law_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PrimitiveOrientationLocalFactorProductLawBeforePushforward
```

formal-to-actual 含义是：最新逐点 Phi-LPF signed 表可沿既有 signed-value 路由继续压缩。该表的
alpha 侧首要生成字段是 signed alpha weight；signed alpha weight 又必须来自 primitive summand
推前前 signed expression；expression 必须给 pre-Cauchy origin identity；origin identity 等价于
逐行 clean-core 原始生成表。继续用 signed slot/value-map/source identity 证明这张表会回到自身，
所以这是固定点，不是证明。

当前真正最窄字段为：

```text
PrimitiveOrientationLocalFactorProductLawBeforePushforward
```

它要求在 Cauchy/Phi/payment 推前之前，对每条 actual noncanonical primitive row 正向给出
orientation bit、local-factor product、truncation weight、非零条件和 prepushforward signed sum
identity。LPF/Phi 的桶恒等式仍只提供偶几何和容量，不能生成这个反变号取向。行/列命题仍未
无条件闭合。

## 363. Phi-LPF orientation trace payload source-rank sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_orientation_trace_payload_source_rank_sync_router.py
docs/monograph/prime-matrix-phi-lpf-orientation-trace-payload-source-rank-sync-router.md
docs/monograph/prime-matrix-phi-lpf-orientation-trace-payload-source-rank-sync-router.json
data/prime-matrix-phi-lpf-orientation-trace-payload-source-rank-sync-ledger.json
```

同步结果：

```text
orientation_reduced_to_actual_branch_trace=true
trace_payload_cycle_imported=true
visible_trace_cannot_generate_odd_payload=true
common_packet_need_imported=true
new_primitive_artifact_aligned_to_source_rank=true
source_rank_atom_package_imported=true
actual_source_domain_entropy_proved=false
complete_primitive_emitter_key_partition_proved=false
fixed_key_exact_uv_local_multiplicity_proved=false
orientation_local_factor_law_proved=false
row_column_unconditional_closed=false
next_direct_attack_target=ActualPreCauchySourceDomainAbsoluteEntropyLedger
```

formal-to-actual 含义是：当前 `PrimitiveOrientationLocalFactorProductLawBeforePushforward`
若要成为非循环 signed 输入，必须来自 Cauchy/Phi/payment 前的 actual branch trace。
但已有 trace cycle 审查显示，当前内部材料只给可见坐标 trace；signed payload 会回到
row-level/source packet 闭环。新增 primitive payload/trace artifact 也不能只命名单个 payload，
它必须证明 source rank/no-collapse 包。

因此最新直接主攻同步为：

```text
ActualPreCauchySourceDomainAbsoluteEntropyLedger
```

并行剩余为：

```text
CompletePrimitiveEmitterKeyPartitionLedger
FixedKeyExactUVLocalMultiplicityO1Ledger
AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
ExternalDIBFIKuznetsovDispersionTheoremMatch
RatePreservationLedger_FOR_moving_atom_packet
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

LPF/Phi 精准桶恒等式在这里只封闭无符号支撑归属，不生成 signed orientation。行/列命题仍未
无条件闭合。

## 364. Phi-LPF latest source-entropy to built-in pairing sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_source_entropy_to_builtin_pairing_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-source-entropy-to-builtin-pairing-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-source-entropy-to-builtin-pairing-sync-router.json
data/prime-matrix-phi-lpf-latest-source-entropy-to-builtin-pairing-sync-ledger.json
```

同步结果：

```text
latest_source_entropy_imported=true
source_entropy_downstream_cycle_imported=true
source_entropy_raw_cycle_rejected=true
cycle_cut_terminal_unified_imported=true
terminal_and_pdec_not_internal_closure=true
antisplit_downstream_imported=true
ordinary_joint_declaration_route_rejected_as_fixed_point=true
atomic_rows_reduced_to_builtin_pairing=true
exactuv_entropy_fiber_split_imported=true
builtin_pairing_trace_cycle_carried=true
trace_exit_source_rank_convergence_carried=true
built_in_signed_pairing_proved=false
actual_emitter_source_domain_entropy_proved=false
exact_uv_map_fixed_pair_polylog_fiber_bound_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
parallel_primary_attack_target=ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
```

formal-to-actual 含义是：latest orientation/trace/payload/source-rank 层留下的
`ActualPreCauchySourceDomainAbsoluteEntropyLedger` 已经接入既有 source-entropy downstream、
cycle-cut/terminal unified 与 antisplit downstream。source entropy 继续展开会进入 signed
law、basis source、internal basis 与 basis alphabet 的坐标-来源环；该环只删除自证路线，
不能作为证明。

cycle-cut/terminal/PDEC 统一后，普通 joint declaration 仍会降到 constructor fixed point。
因此非循环内部路线必须走 atomic antisplit rows，并把 signed 首缺口压到：

```text
BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
```

ExactUV 并行门仍为：

```text
ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
```

本层不证明 built-in pairing、ExactUV entropy/fiber、complete/fixed-key、terminal/PDEC/外部谱、
模型、Rate 或 DStructure。行/列命题仍未无条件闭合。

## 365. Phi-LPF latest signed macrocycle ExactUV source-table sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_signed_macrocycle_exactuv_source_table_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-signed-macrocycle-exactuv-source-table-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-signed-macrocycle-exactuv-source-table-sync-router.json
data/prime-matrix-phi-lpf-latest-signed-macrocycle-exactuv-source-table-sync-ledger.json
```

同步结果：

```text
source_entropy_to_builtin_imported=true
builtin_to_new_primitive_trace_cycle_imported=true
new_primitive_to_pointwise_kernel_imported=true
alpha_frontier_to_moving_atom_imported=true
moving_atom_unsigned_lpf_preimage_closed=true
moving_atom_signed_injection_to_pointwise_table_imported=true
pointwise_table_to_orientation_imported=true
orientation_returns_to_source_entropy_imported=true
full_signed_macrocycle_closed_as_nonproof=true
lpf_phi_unsigned_capacity_exhausted=true
exactuv_atomization_imported=true
fixed_pair_fiber_formal_inequality_closed=true
registered_complete_key_reduced_to_source_table=true
source_table_reduced_to_precauchy_declaration=true
pre_cauchy_constructor_declaration_line_proved=false
fixed_key_exact_uv_local_multiplicity_o1_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter
```

formal-to-actual 含义是：latest signed 路线已经闭成完整宏环：

```text
ActualPreCauchySourceDomainAbsoluteEntropyLedger
-> BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
-> NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact
-> AlphaRowAnchorPhaseEmissionFormulaLedger
-> IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore
-> LPFMovingAtomSignedPreimageMassInjectionLedger
-> PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
-> PrimitiveOrientationLocalFactorProductLawBeforePushforward
-> ActualPreCauchySourceDomainAbsoluteEntropyLedger
```

该宏环是自证删除证书，不是证明。LPF/Phi 精准桶恒等式只关闭无符号 ownership、support
与 capacity；它不能生成 signed source table 或 fixed-key local multiplicity。

ExactUV 侧继续原子化为 signed row law、registered complete key 与 fixed-key local
multiplicity。fixed-pair fiber 的形式不等式已闭合，registered complete key 又必须来自
actual noncanonical primitive emitter source table；该 source table 的首个生产性字段是：

```text
PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter
```

并行仍需 `FixedKeyExactUVLocalMultiplicityO1Ledger`、signed row law、same-set PDEC/外部谱、
模型、Rate 与 DStructure。行/列命题仍未无条件闭合。

## 366. Phi-LPF latest pre-Cauchy alpha-terminal sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_precauchy_alpha_terminal_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-precauchy-alpha-terminal-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-precauchy-alpha-terminal-sync-router.json
data/prime-matrix-phi-lpf-latest-precauchy-alpha-terminal-sync-ledger.json
```

同步结果：

```text
latest_source_table_imported=true
strict_precauchy_to_constructor_imported=true
constructor_to_explicit_alpha_delta_imported=true
explicit_alpha_delta_to_alpha_side_imported=true
alpha_side_to_deterministic_map_imported=true
deterministic_map_to_anchor_phase_imported=true
anchor_phase_to_signed_lift_imported=true
signed_lift_to_weight_law_imported=true
weight_law_to_independent_identity_imported=true
identity_taxonomy_to_moving_block_imported=true
moving_block_to_global_terminal_modelgap_imported=true
lpf_phi_unsigned_only_boundary_retained=true
pdec_cap_or_internal_clean_kls_large_sieve_proved=false
explicit_model_gap_and_finite_dprc_ledger_proved=false
fixed_key_exact_uv_local_multiplicity_o1_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve
```

formal-to-actual 含义是：latest source-table 层留下的 pre-Cauchy declaration 不是新的终点。
沿 strict productive alpha-side 分支展开：

```text
PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter
-> ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter
-> ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter
-> ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger
-> DeterministicAlphaPrimitiveRowEmissionMapLedger
-> AlphaRowAnchorPhaseEmissionFormulaLedger
-> AlphaFormulaSignedCoefficientLiftLedger
-> AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger
-> IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
-> ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn
-> PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger
```

因此下一条最接近显式全局矛盾的 productive 分支主攻是
`PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve`，模型余量、fixed-key ExactUV、signed row law、
delta/pairing/nonzero 兄弟字段、Rate 与 DStructure 仍并行开放。LPF/Phi 桶恒等式只提供
无符号桶容量边界，不生成 signed pre-Cauchy 权重。行/列命题仍未无条件闭合。

## 367. Phi-LPF latest terminal saturation to new-joint sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_terminal_saturation_to_new_joint_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-terminal-saturation-to-new-joint-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-terminal-saturation-to-new-joint-sync-router.json
data/prime-matrix-phi-lpf-latest-terminal-saturation-to-new-joint-sync-ledger.json
```

同步结果：

```text
latest_phi_lpf_terminal_gate_imported=true
pdec_clean_kls_split_imported=true
pdec_arm_scope_still_open=true
clean_kls_kuznetsov_route_returns_terminal=true
pdec_scope_branch_saturated_to_new_joint=true
global_crt_saturation_agrees=true
new_joint_obligation_imported=true
old_joint_route_is_fixed_point=true
terminal_descent_alternative_macrocycle=true
lpf_phi_unsigned_boundary_retained=true
new_explicit_joint_constructor_formula_artifact_present=false
pdec_cap_or_internal_clean_kls_large_sieve_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
```

formal-to-actual 含义是：上一节留下的 PDEC/CleanKLS 终端门继续饱和：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve
-> AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
   OR SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks
-> NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
```

这里的箭头不是证明箭头。Kuznetsov/DLS 线回到 strict acyclic 终端家族；PDEC scope
线可作为新 scope 证书或外部 DIBFI 条件线，但在当前内部语料中不再给独立非循环出口。
旧 joint constructor 展开会回到 signed-source 固定点，terminal descent 替代也已是宏循环。

因此当前严格内部主攻更新为：

```text
NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
```

并行仍需 ExactUV、fixed-key、signed row law、模型余量、Rate 与 DStructure。行/列命题仍未无条件闭合。

## 368. Phi-LPF latest new-joint to antisplit atom sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_new_joint_antisplit_atom_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-antisplit-atom-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-antisplit-atom-sync-router.json
data/prime-matrix-phi-lpf-latest-new-joint-antisplit-atom-sync-ledger.json
```

同步结果：

```text
latest_new_joint_target_imported=true
terminal_obligation_imported=true
old_split_formula_route_synced=true
old_split_formula_route_is_nonproof_cycle=true
antisplit_joint_formula_target_imported=true
lpf_phi_unsigned_boundary_retained=true
non_split_actual_joint_formula_proved=false
known_antisplit_downstream_available=true
row_column_unconditional_closed=false
next_primary_attack_target=NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection
```

formal-to-actual 含义是：new-joint 的旧拆分路线不能再作为证明路线：

```text
NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
-> old split alpha/delta route
-> row-level/signed-source fixed point
```

因此最新非循环主攻必须改为反分裂同排原子：

```text
NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection
```

它要求在 alpha-side 投影前同一行生成 primitive word、signed coefficient、
alpha/delta payload、exact `(u,v)`、key/local factor、prepushforward identity 与 no-split
证书。LPF/Phi 桶恒等式只给无符号 support/capacity，不给 signed coefficient。

已有下游表明该反分裂原子若继续追击，会压到 built-in pairing 与 ExactUV entropy/fiber：

```text
BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
AND ActualEmitterSourceDomainEntropyLedger
AND ExactUVMapFixedPairPolylogFiberBoundLedger
```

这些输入仍未证明，且 fixed-key、signed row law、模型余量、Rate 与 DStructure 仍并行开放。行/列命题仍未无条件闭合。

## 369. Phi-LPF latest new-joint antisplit downstream sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_new_joint_antisplit_downstream_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-antisplit-downstream-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-antisplit-downstream-sync-router.json
data/prime-matrix-phi-lpf-latest-new-joint-antisplit-downstream-sync-ledger.json
```

同步结果：

```text
latest_antisplit_atom_imported=true
strict_antisplit_downstream_edges_imported=true
antisplit_firewall_to_atomic_rows_imported=true
atomic_rows_reduced_to_builtin_pairing=true
exactuv_entropy_fiber_split_imported=true
built_in_signed_pairing_proved=false
actual_emitter_source_domain_entropy_proved=false
exact_uv_map_fixed_pair_polylog_fiber_bound_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
parallel_primary_attack_target=ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
```

formal-to-actual 含义是：反分裂目标继续下钻为：

```text
NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection
-> AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing
-> BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
```

这条边不是证明边；它说明若要真正构造反分裂同排行，就必须给出 atomic rows 的内置
signed coefficient/pairing 闭式，且不能退回 signed-value/origin-table 固定点。

并行 ExactUV 门被拆为：

```text
ActualEmitterSourceDomainEntropyLedger
AND ExactUVMapFixedPairPolylogFiberBoundLedger
```

因此最新直接主攻是 `BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows`，并行主攻是
source-domain entropy 与 fixed-pair fiber bound。complete/fixed-key、signed row law、模型余量、
Rate 与 DStructure 仍开放。行/列命题仍未无条件闭合。

## 370. Phi-LPF latest current built-in pairing to branch trace sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_new_joint_builtin_pairing_trace_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-builtin-pairing-trace-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-builtin-pairing-trace-sync-router.json
data/prime-matrix-phi-lpf-latest-new-joint-builtin-pairing-trace-sync-ledger.json
```

同步结果：

```text
current_latest_builtin_pairing_imported=true
legacy_builtin_trace_router_same_target=true
strict_builtin_frontier_imported=true
global_branch_trace_frontier_aligned=true
signed_lane_cycle_imported=true
branch_trace_self_proof_rejected=true
new_primitive_payload_or_trace_artifact_present=false
exactuv_entropy_fiber_pair_carried=true
row_column_unconditional_closed=false
next_primary_attack_target=NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact
parallel_primary_attack_target=ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
```

formal-to-actual 含义是：当前 latest built-in pairing 可以直接接到既有 branch trace 下游：

```text
BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
-> ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn
```

但 exact branch trace 的现有 signed/payload/origin/common packet 展开已经形成自证环。排除该环后，
最新非循环硬点是：

```text
NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact
```

或者走受控出口 `AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate` 与
`AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate`。并行 ExactUV 仍需 source entropy/fixed
fiber；fixed fiber 已进一步落到 complete key polylog 分区与 fixed-key O(1) 局部重数。行/列命题仍未无条件闭合。

## 371. Phi-LPF latest new-joint trace-exit source-rank sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_new_joint_trace_exit_source_rank_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-trace-exit-source-rank-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-trace-exit-source-rank-sync-router.json
data/prime-matrix-phi-lpf-latest-new-joint-trace-exit-source-rank-sync-ledger.json
```

同步结果：

```text
current_new_joint_trace_exit_imported=true
controlled_trace_exits_carried=true
latest_new_payload_source_atom_alignment_imported=true
older_trace_exit_convergence_same_absorber_imported=true
post_antisplit_convergence_imported=true
source_packet_guard_confirms_no_lpf_signed_shortcut=true
pointwise_kernel_frontier_imported=true
exactuv_entropy_fiber_pair_carried=true
row_column_unconditional_closed=false
next_primary_attack_target=AlphaRowAnchorPhaseEmissionFormulaLedger
```

formal-to-actual 含义是：当前 new-joint trace-exit 的 `NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact`
没有形成新的无名终端。若它是真正的新 primitive signed 工件，就必须提交 actual source-rank/no-collapse
包；而已有 source-atom 与 post-antisplit 收敛证书已经把该包下压到同 formal-unit 的逐点
primitive alpha/delta 核表。

因此最新直接硬点从 new payload 名称推进为：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger
```

并行硬点为：

```text
IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward
PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward
```

这仍是非循环前沿同步，不是 alpha row 发射公式、算术恒等式、rank/multiplicity 或 ExactUV
的证明。行/列命题仍未无条件闭合。

## 372. Phi-LPF latest new-joint alpha terminal three-atoms sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_new_joint_alpha_terminal_three_atoms_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-alpha-terminal-three-atoms-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-alpha-terminal-three-atoms-sync-router.json
data/prime-matrix-phi-lpf-latest-new-joint-alpha-terminal-three-atoms-sync-ledger.json
```

同步结果：

```text
current_new_joint_alpha_frontier_imported=true
legacy_alpha_terminal_same_target_imported=true
alpha_local_frontier_terminal_synced=true
terminal_three_atoms_pinned=true
new_joint_trace_cycle_still_absorbed=true
independent_moving_atom_chosen_as_narrowest=true
row_column_unconditional_closed=false
next_primary_attack_target=IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore
```

formal-to-actual 含义是：当前 new-joint latest 的 alpha row 前沿可直接接入已有
alpha-terminal 三原子证书。alpha 局部几何只关闭 unsigned skeleton、carry-shell 和 phase
兼容；signed lift 与 anchor-overload 分支回到终端容量/模型门。旧 joint/new joint/trace/payload
路线则回到 signed-lane 自证环。

因此最新直接硬点推进为：

```text
IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore
```

并行保留：

```text
AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
A1CleanBranchCanonicalSourceAdmission
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward
PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward
ExplicitModelGapAndFiniteDPRCLedger
RatePreservationLedger_FOR_moving_atom_packet
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本层仍是同步和前沿压缩；moving atom 独立非终端排斥、canonical-lock、A1 admission 与晋级门均未证明。
行/列命题仍未无条件闭合。

## 373. Phi-LPF latest new-joint moving-atom signed-table sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_new_joint_moving_atom_signed_table_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-moving-atom-signed-table-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-moving-atom-signed-table-sync-router.json
data/prime-matrix-phi-lpf-latest-new-joint-moving-atom-signed-table-sync-ledger.json
```

同步结果：

```text
current_new_joint_moving_atom_frontier_imported=true
moving_atom_source_bucket_preimage_imported=true
lpf_bucket_identity_sample_carried=true
signed_injection_split_imported=true
half_mass_finite_algebra_imported=true
pointwise_signed_table_proved=false
signed_survival_and_row_mass_proved=false
latest_moving_atom_exclusion_after_signed_split_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
```

formal-to-actual 含义是：当前 latest moving-atom 硬点可同步进入已有 Phi-LPF moving-atom
source-bucket 前像与 signed-injection split。前者删除无主、prime-row 与 virtual-unit
source escape；后者把剩余问题压到同 formal unit 的 signed 表，而不是新的 unsigned
计数出口。

因此最新直接硬点推进为：

```text
PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
```

并行保留：

```text
PhiLPFBucketSignedCoefficientLawBeforePushforward
ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward
NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet
HighSegmentModelGapAlpha043C3AnalyticLedger
RatePreservationLedger_FOR_moving_atom_packet
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward
PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward
```

本层仍是前沿同步，不是逐点 signed 表、signed survival/row-mass、速率包或行/列命题的
无条件证明。

## 374. Phi-LPF latest new-joint pointwise-table origin sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_new_joint_pointwise_table_origin_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-pointwise-table-origin-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-pointwise-table-origin-sync-router.json
data/prime-matrix-phi-lpf-latest-new-joint-pointwise-table-origin-sync-ledger.json
```

同步结果：

```text
latest_pointwise_table_imported=true
pointwise_frontier_imported=true
pointwise_table_first_field_signed_weight_imported=true
phi_lpf_signed_survival_boundary_imported=true
primitive_expression_to_origin_identity_imported=true
reverse_recovery_blocked_imported=true
existing_expansion_hits_breaker_triad=true
pointwise_signed_table_proved=false
primitive_summand_origin_identity_proved=false
signed_survival_and_row_mass_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward
```

formal-to-actual 含义是：逐点 Phi-LPF signed 表作为 direct bypass 仍未证明；它不能从
LPF/Phi 桶恒等式反推得到。既有逐行 signed alpha weight 与 primitive summand 证书说明，
这张表的实际首字段会落到 pre-Cauchy source tuple 来源恒等式。

因此最新直接硬点推进为：

```text
PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward
```

并行保留：

```text
NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward
PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward
ExplicitModelGapAndFiniteDPRCLedger
RatePreservationLedger_FOR_moving_atom_packet
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本层仍是最窄字段同步；来源恒等式、signed survival/row-mass、三破环出口与最终晋级门均未证明。

## 375. Phi-LPF latest new-joint origin-identity cycle-cut sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_new_joint_origin_identity_cyclecut_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-origin-identity-cyclecut-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-origin-identity-cyclecut-sync-router.json
data/prime-matrix-phi-lpf-latest-new-joint-origin-identity-cyclecut-sync-ledger.json
```

同步结果：

```text
latest_origin_identity_imported=true
origin_identity_to_row_table_imported=true
row_table_to_signed_emitter_imported=true
reverse_and_unsigned_routes_blocked=true
coordinate_source_cycle_guard_imported=true
latest_nonrecursive_breaker_triad_imported=true
primitive_summand_origin_identity_proved=false
seed_cycle_cut_input_proved=false
acyclic_same_set_scope_match_proved=false
new_explicit_joint_constructor_formula_artifact_present=false
row_column_unconditional_closed=false
next_primary_attack_target=AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput_OR_AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate_OR_NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
```

formal-to-actual 含义是：来源恒等式若不作为全新无环工件正向给出，就必须落到逐行
clean-core 原始生成表；该表再落到无环 seed signed-row emitter。现有展开链已经被坐标-来源
环守卫判定为闭合依赖环，不能作为证明。

因此最新直接硬点推进为：

```text
AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput
OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
```

并行保留：

```text
AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
ExplicitModelGapAndFiniteDPRCLedger
RatePreservationLedger_FOR_moving_atom_packet
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本层仍是非循环前沿同步；三破环口、terminal WFD 和最终晋级门均未证明。

## 376. Phi-LPF latest new-joint triad constructor sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_new_joint_triad_constructor_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-triad-constructor-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-triad-constructor-sync-router.json
data/prime-matrix-phi-lpf-latest-new-joint-triad-constructor-sync-ledger.json
```

同步结果：

```text
latest_triad_imported=true
seed_cycle_cut_saturation_imported=true
pdec_scope_internal_saturation_imported=true
strict_unified_declaration_line_imported=true
joint_emitter_field_atom_imported=true
declaration_constructor_sync_imported=true
antisplit_boundary_carried=true
explicit_joint_alpha_delta_constructor_rule_proved=false
joint_constructor_field_basis_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple
```

formal-to-actual 含义是：当前三破环口继续收窄为一个 constructor 单点：

```text
AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput
OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
-> PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple
-> ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple
```

第一箭头来自 cycle-cut/PDEC/new-joint 统一前沿与 PDEC 内部分支饱和；第二箭头来自 joint
declaration/constructor 同步。这里仍不是证明箭头：它只说明若要破掉已登记的
signed-source 自证环，就必须正向写出显式 joint alpha/delta primitive constructor rule。

完整未闭合字段基为：

```text
ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple
AND JointConstructorDomainCleanCoreMembershipAndSameSourceTupleLedger
AND JointConstructorFormulaEmitsBasisWordUVKeySignLocalFactorCoefficientRowsLedger
AND SameFormalUnitPreCauchyTimestampLockLedger
AND NoncanonicalJointDeclarationNoCanonicalOrExternalLeakLedger
AND JointConstructorFormulaFailureReturnTagsLedger
```

该规则还必须兼容 anti-split 同排行边界，不能回到旧 split alpha/delta 路线。ExactUV、
complete/fixed-key、signed survival/row-mass、terminal/canonical/independent bridge、
模型、Rate 与 DStructure 仍开放。行/列命题仍未无条件闭合。

## 377. Phi-LPF latest new-joint constructor anti-split downstream sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_new_joint_constructor_antisplit_downstream_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-antisplit-downstream-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-antisplit-downstream-sync-router.json
data/prime-matrix-phi-lpf-latest-new-joint-constructor-antisplit-downstream-sync-ledger.json
```

同步结果：

```text
latest_constructor_imported=true
ordinary_constructor_fixed_point_imported=true
antisplit_atomic_route_imported=true
atomic_rows_to_builtin_pairing_imported=true
exactuv_entropy_fiber_parallel_imported=true
built_in_signed_pairing_proved=false
actual_emitter_source_domain_entropy_proved=false
exact_uv_map_fixed_pair_polylog_fiber_bound_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
parallel_primary_attack_target=ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
```

formal-to-actual 含义是：显式 constructor 的普通展开路线不是非循环证明，而是：

```text
ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple
-> alpha-side / same-row / row-level signed-source fixed point
```

删除该固定点后，productive 路线必须走 anti-split atomic rows，并进一步压到：

```text
BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
```

并行 ExactUV 主攻保持为：

```text
ActualEmitterSourceDomainEntropyLedger
AND ExactUVMapFixedPairPolylogFiberBoundLedger
```

本层关闭的是 constructor 名称停留与普通展开误出口；built-in pairing、source entropy、fixed
fiber、complete/fixed-key、signed survival/row-mass、terminal/PDEC/外部谱、模型、Rate 与
DStructure 仍未证明。行/列命题仍未无条件闭合。

## 378. Phi-LPF latest new-joint constructor built-in trace sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_new_joint_constructor_builtin_trace_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-builtin-trace-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-builtin-trace-sync-router.json
data/prime-matrix-phi-lpf-latest-new-joint-constructor-builtin-trace-sync-ledger.json
```

同步结果：

```text
latest_constructor_builtin_pairing_imported=true
generic_builtin_trace_same_target_imported=true
strict_builtin_frontier_imported=true
branch_trace_payload_frontier_imported=true
signed_lane_cycle_guard_imported=true
new_primitive_payload_or_trace_artifact_present=false
exactuv_parallel_carried=true
row_column_unconditional_closed=false
intermediate_primary_attack_target=ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn
next_primary_attack_target=NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact
parallel_primary_attack_target=ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
```

formal-to-actual 含义是：built-in pairing 的直接 trace 路线不是闭合证明，而是通向已登记
signed-lane 自证环：

```text
BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
-> ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn
-> AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
-> signed-lane cycle
```

删除该环后，latest 非循环主攻推进为：

```text
NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact
```

并行门仍是：

```text
ActualEmitterSourceDomainEntropyLedger
AND ExactUVMapFixedPairPolylogFiberBoundLedger
```

本层关闭的是 branch-trace 自证误出口；new primitive payload/trace、terminal descent、
same-set PDEC、ExactUV entropy/fiber、complete/fixed-key、模型、Rate 与 DStructure 仍未证明。
行/列命题仍未无条件闭合。

## 379. Phi-LPF latest constructor trace source-rank sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_new_joint_constructor_trace_source_rank_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-trace-source-rank-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-trace-source-rank-sync-router.json
data/prime-matrix-phi-lpf-latest-new-joint-constructor-trace-source-rank-sync-ledger.json
```

同步结果：

```text
constructor_trace_exit_imported=true
controlled_exit_basis_carried=true
prior_trace_source_rank_absorber_imported=true
latest_new_payload_source_atom_alignment_imported=true
post_antisplit_convergence_imported=true
lpf_phi_unsigned_bucket_no_signed_shortcut=true
pointwise_kernel_frontier_imported=true
exactuv_entropy_fiber_pair_carried=true
row_column_unconditional_closed=false
next_primary_attack_target=AlphaRowAnchorPhaseEmissionFormulaLedger
```

formal-to-actual 含义是：constructor trace 口径下的 `NewPrimitive...` 出口已经和既有
trace-exit/source-rank absorber 对齐；它不是新的独立闭合点，而是必须提交 source-rank/
no-collapse 三原子，随后进入同 formal-unit 的逐点 primitive alpha/delta 核表。

LPF/Phi 桶恒等式关闭的是无符号 owner/support/capacity/root 账本，不生成 signed payload。
因此 latest 直接主攻推进为：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger
```

完整剩余基为：

```text
((AlphaRowAnchorPhaseEmissionFormulaLedger
AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows)
OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
OR ExternalDIBFIKuznetsovDispersionTheoremMatch
OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
OR ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
OR (PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward
AND PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward))
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

行/列命题仍未无条件闭合。

## 380. Phi-LPF latest constructor alpha terminal three-atoms sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_new_joint_constructor_alpha_terminal_three_atoms_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-alpha-terminal-three-atoms-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-alpha-terminal-three-atoms-sync-router.json
data/prime-matrix-phi-lpf-latest-new-joint-constructor-alpha-terminal-three-atoms-sync-ledger.json
```

同步结果：

```text
current_constructor_alpha_frontier_imported=true
legacy_alpha_terminal_same_target_imported=true
alpha_local_frontier_terminal_synced=true
terminal_three_atoms_pinned=true
new_joint_trace_cycle_still_absorbed=true
independent_moving_atom_chosen_as_narrowest=true
row_column_unconditional_closed=false
next_primary_attack_target=IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore
```

formal-to-actual 含义是：constructor-alpha 前沿不能在 alpha 局部公式内闭合；unsigned
几何分支只给 carry-shell/phase 形状，signed-lift 和 overload 分支回到终端容量、模型与
DStructure 门。new joint/trace/payload 逆路也已被 signed-lane cycle 删除。

因此当前 strict 三原子为：

```text
AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
OR A1CleanBranchCanonicalSourceAdmission
OR ActualNoncanonicalCleanCoreMovingAtomExclusion
```

最新最窄直接主攻：

```text
IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore
```

并行主攻仍包括：

```text
AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
A1CleanBranchCanonicalSourceAdmission
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward
AND PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward
ExplicitModelGapAndFiniteDPRCLedger
RatePreservationLedger_FOR_moving_atom_packet
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

行/列命题仍未无条件闭合。

## 381. Phi-LPF latest constructor moving-atom signed-table sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_new_joint_constructor_moving_atom_signed_table_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-moving-atom-signed-table-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-moving-atom-signed-table-sync-router.json
data/prime-matrix-phi-lpf-latest-new-joint-constructor-moving-atom-signed-table-sync-ledger.json
```

同步结果：

```text
current_constructor_moving_atom_frontier_imported=true
moving_atom_source_bucket_preimage_imported=true
lpf_bucket_identity_sample_carried=true
signed_injection_split_imported=true
half_mass_finite_algebra_imported=true
pointwise_signed_table_proved=false
signed_survival_and_row_mass_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
```

formal-to-actual 含义是：moving atom 的 unsigned source preimage 已被 LPF ownership 和
Phi 递推固定；真正的 actual-load 缺口不再是“有没有桶”，而是桶上逐点 signed value、
非零 signed row 存活、同 formal unit row-mass/no-heavy-row 与速率型终端包。

最新直接主攻：

```text
PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
```

完整剩余基为：

```text
((PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
OR PhiLPFBucketSignedCoefficientLawBeforePushforward
OR ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward)
AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger)
OR (PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND RatePreservationLedger_FOR_moving_atom_packet)
OR ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
OR (PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward
AND PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward)
```

行/列命题仍未无条件闭合。

## 382. Phi-LPF latest constructor pointwise-origin sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_new_joint_constructor_pointwise_origin_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-pointwise-origin-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-pointwise-origin-sync-router.json
data/prime-matrix-phi-lpf-latest-new-joint-constructor-pointwise-origin-sync-ledger.json
```

同步结果：

```text
current_constructor_pointwise_table_imported=true
general_pointwise_origin_router_imported=true
pointwise_frontier_imported=true
pointwise_table_first_field_signed_weight_imported=true
primitive_expression_to_origin_identity_imported=true
reverse_recovery_blocked_imported=true
existing_expansion_hits_breaker_triad=true
pointwise_signed_table_proved=false
primitive_summand_origin_identity_proved=false
signed_survival_and_row_mass_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward
```

formal-to-actual 含义是：constructor moving-atom 口径已进入逐点 signed 表，但逐点表不是
LPF/Phi support/capacity 的推论。它必须拆成 signed weight、primitive summand signed
expression，并最终给出 pre-Cauchy source tuple 的 origin identity。现有来源展开会回到
signed-source 固定点，所以不能作为非循环证明。

最新直接主攻：

```text
PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward
```

完整剩余基为：

```text
(PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward
AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger)
OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput
OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
```

ExactUV、rough-cofactor transport/coherence、模型、Rate 与 DStructure 仍开放。行/列命题
仍未无条件闭合。

## 383. Phi-LPF latest constructor origin-cyclecut sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_new_joint_constructor_origin_cyclecut_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-origin-cyclecut-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-origin-cyclecut-sync-router.json
data/prime-matrix-phi-lpf-latest-new-joint-constructor-origin-cyclecut-sync-ledger.json
```

同步结果：

```text
current_constructor_origin_identity_imported=true
general_origin_cyclecut_router_imported=true
origin_identity_to_row_table_imported=true
row_table_to_signed_emitter_imported=true
reverse_unsigned_and_source_loop_routes_blocked=true
coordinate_source_cycle_guard_imported=true
latest_nonrecursive_breaker_triad_imported=true
primitive_summand_origin_identity_proved=false
seed_cycle_cut_input_proved=false
acyclic_same_set_scope_match_proved=false
new_explicit_joint_constructor_formula_artifact_present=false
row_column_unconditional_closed=false
next_primary_attack_target=AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput_OR_AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate_OR_NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
```

formal-to-actual 含义是：primitive summand origin identity 不是新的自由原子；它必须展开为
row-level origin generation table，再由 acyclic seed signed-row emitter 生成。现有 signed
coordinate/source 展开只回到闭环，所以 constructor 口径不能把这个环当成证明。

最新直接主攻：

```text
AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput
OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
```

完整剩余基为：

```text
(AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput
OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate)
AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
AND ActualEmitterSourceDomainEntropyLedger
AND ExactUVMapFixedPairPolylogFiberBoundLedger
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

行/列命题仍未无条件闭合。

## 384. Phi-LPF latest constructor triad-unified sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_new_joint_constructor_triad_unified_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-triad-unified-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-triad-unified-sync-router.json
data/prime-matrix-phi-lpf-latest-new-joint-constructor-triad-unified-sync-ledger.json
```

同步结果：

```text
current_constructor_triad_imported=true
strict_unified_frontier_imported=true
seed_cycle_cut_branch_saturated_imported=true
pdec_scope_internal_saturation_imported=true
new_joint_reduced_to_declaration_line_imported=true
joint_field_basis_still_open=true
terminal_wfd_parallel_macrocycle_imported=true
seed_cycle_cut_input_proved=false
acyclic_same_set_scope_match_proved=false
new_explicit_joint_constructor_formula_artifact_present=false
pre_cauchy_joint_declaration_line_proved=false
joint_productive_field_basis_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple
```

formal-to-actual 含义是：三破环口被 strict 统一前沿消去为一个更窄的生产性单点。cycle-cut
分支不再给内部自足闭合，PDEC scope 不再给内部自足闭合，new-joint 必须提交 pre-Cauchy
joint declaration line。

最新直接主攻：

```text
PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple
```

完整剩余基为：

```text
((PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple
AND JointEmitterPrimitiveSummandRowsFormulaBeforePushforward
AND JointEmitterPrepushforwardWordCoefficientIdentityLedger
AND JointEmitterNoDownstreamRecoveryAndNamedReturnLedger)
OR AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
OR IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop
OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
OR ExternalDIBFIKuznetsovDispersionTheoremMatch)
AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
AND ActualEmitterSourceDomainEntropyLedger
AND ExactUVMapFixedPairPolylogFiberBoundLedger
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

行/列命题仍未无条件闭合。

## 385. Phi-LPF latest constructor joint-declaration antisplit sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_new_joint_constructor_joint_declaration_antisplit_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-joint-declaration-antisplit-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-joint-declaration-antisplit-sync-router.json
data/prime-matrix-phi-lpf-latest-new-joint-constructor-joint-declaration-antisplit-sync-ledger.json
```

同步结果：

```text
current_constructor_joint_declaration_imported=true
strict_antisplit_downstream_imported=true
ordinary_joint_declaration_synced_to_constructor_rule=true
ordinary_constructor_route_rejected_as_fixed_point=true
antisplit_firewall_imported=true
atomic_rows_reduced_to_builtin_pairing=true
exactuv_entropy_fiber_split_imported=true
pre_cauchy_joint_declaration_line_proved=false
atomic_antisplit_declaration_proved=false
built_in_signed_pairing_proved=false
actual_emitter_source_domain_entropy_proved=false
exact_uv_map_fixed_pair_polylog_fiber_bound_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
```

formal-to-actual 含义是：joint declaration line 不能直接闭合 signed 信息。普通 declaration
路线回到 fixed point；anti-split 路线把 atomic joint rows 的 signed 首缺口压到 built-in
pairing。ExactUV entropy/fiber 仍是并行门，不由 built-in pairing 自动支付。

最新直接主攻：

```text
BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
```

完整剩余基为：

```text
((BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
AND ActualEmitterSourceDomainEntropyLedger
AND ExactUVMapFixedPairPolylogFiberBoundLedger)
OR AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
OR IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop
OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
OR ExternalDIBFIKuznetsovDispersionTheoremMatch)
AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
AND ExplicitModelGapAndFiniteDPRCLedger
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

行/列命题仍未无条件闭合。

## 386. Phi-LPF latest constructor macrocycle cut signed-survival sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_new_joint_constructor_macrocycle_cut_signed_survival_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-macrocycle-cut-signed-survival-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-macrocycle-cut-signed-survival-sync-router.json
data/prime-matrix-phi-lpf-latest-new-joint-constructor-macrocycle-cut-signed-survival-sync-ledger.json
```

同步结果：

```text
constructor_signed_macrocycle_closed=true
constructor_macrocycle_self_proof_rejected=true
signed_survival_gate_mandatory_in_latest_basis=true
signed_survival_reduced_to_row_level_origin_table=true
source_entropy_builtin_cycle_carried=true
row_level_clean_core_origin_generation_table_proved=false
nonzero_signed_row_survival_proved=false
same_formal_unit_row_mass_normalization_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands
```

formal-to-actual 含义是：latest constructor built-in pairing 继续展开后会回到
constructor signed 宏循环，不是新的非循环闭合。宏循环为：

```text
BuiltIn -> NewPayload -> AlphaRow -> MovingAtom -> PointwiseSignedTable
-> OriginIdentity -> Triad -> JointDeclaration -> BuiltIn
```

所以本层把环内回代从证明路径删除。当前可推进的实际 signed 侧门是：

```text
RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands
```

它仍只是 `NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward` 的前置表；row-mass、
ExactUV entropy/fiber、complete/fixed key、terminal/PDEC/external 出口、模型、Rate 和
DStructure 仍开放。行/列命题仍未无条件闭合。

## 387. Phi-LPF latest constructor row-origin bucket-law sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_row_origin_bucket_law_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-row-origin-bucket-law-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-row-origin-bucket-law-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-row-origin-bucket-law-sync-ledger.json
```

同步结果：

```text
latest_row_origin_table_imported=true
row_table_requires_seed_emitter_imported=true
signed_source_fixed_point_cut_imported=true
row_origin_bucket_sync_imported=true
phi_lpf_support_stripping_imported=true
phi_lpf_support_and_capacity_closed=true
row_origin_table_reduced_to_phi_lpf_bucket_signed_law=true
phi_lpf_bucket_signed_coefficient_law_proved=false
same_formal_unit_row_mass_normalization_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFBucketSignedCoefficientLawBeforePushforward
```

formal-to-actual 含义是：row-level origin table 的 signed-source 固定点被切断后，LPF/Phi
已经支付所有无符号支撑与容量。当前真正未闭合的是桶级 signed law：

```text
PhiLPFBucketSignedCoefficientLawBeforePushforward
```

该 law 必须在 Cauchy/Phi/payment 前为每个 `(p,m)` support key 生成 signed coefficient、
sign/local factor、branch key 与推前前 alpha/delta 求和恒等式。row-mass、signed survival、
ExactUV、complete/fixed key、terminal/PDEC、模型、Rate 与 DStructure 仍开放。行/列命题仍未
无条件闭合。

## 388. Phi-LPF latest constructor bucket transport-stack sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_bucket_transport_stack_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-bucket-transport-stack-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-bucket-transport-stack-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-bucket-transport-stack-sync-ledger.json
```

同步结果：

```text
latest_constructor_bucket_law_imported=true
constructor_side_gates_carried=true
bucket_transport_router_imported=true
unit_seed_boundary_imported=true
ordered_coherence_closed=true
step_update_reduced_to_edge_multiplier=true
square_base_private_escape_removed=true
common_packet_cycle_guard_imported=true
edge_signed_multiplier_table_proved=false
nonzero_signed_row_survival_proved=false
same_formal_unit_row_mass_normalization_proved=false
pointwise_signed_table_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward
```

formal-to-actual 含义是：LPF/Phi 桶恒等式只支付 support/capacity，不能产生 signed coefficient。
constructor-latest bucket signed law 若走递推路线，就必须经过 rough-cofactor transport；
ordered coherence 和 square-base 私有出口已剥离，剩余是逐 edge signed multiplier 与
source-packet 三原子：

```text
PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward
AND AlphaRowAnchorPhaseEmissionFormulaLedger
AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
```

同时 `NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward` 与
`SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger` 仍是 constructor 侧强制门。
ExactUV、complete/fixed key、pointwise signed table、terminal/PDEC、模型、Rate 与 DStructure
仍开放。行/列命题仍未无条件闭合。

## 389. Phi-LPF latest constructor edge multiplier slab sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_edge_multiplier_slab_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-edge-multiplier-slab-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-edge-multiplier-slab-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-edge-multiplier-slab-sync-ledger.json
```

同步结果：

```text
latest_constructor_transport_hardpoint_imported=true
constructor_side_gates_carried=true
first_edge_slab_router_imported=true
edge_multiplier_split_synced_to_constructor_basis=true
first_edge_phi_fiber_formula_imported=true
phi_fiber_unsigned_only_guard=true
semiprime_first_edge_signed_seed_table_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
nonzero_signed_row_survival_proved=false
same_formal_unit_row_mass_normalization_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward
```

formal-to-actual 含义是：edge multiplier 的无符号路径已经由 LPF ordered factorization 固定。
first-edge slab 只给第一边 q-rough fiber：

```text
mass(p,q)=Phi(floor(N/(p*q)),q)
```

这仍然只是 occurrence 质量，不是 signed seed 或 local-factor transition。真正未闭合的是：

```text
PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward
AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
AND AlphaRowAnchorPhaseEmissionFormulaLedger
AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
```

complete/fixed key、ExactUV、pointwise signed table、terminal/PDEC、模型、Rate 与 DStructure
仍开放。行/列命题仍未无条件闭合。

## 390. Phi-LPF latest constructor semiprime seed diagonal sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_semiprime_seed_diagonal_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-semiprime-seed-diagonal-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-semiprime-seed-diagonal-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-semiprime-seed-diagonal-sync-ledger.json
```

同步结果：

```text
latest_constructor_first_seed_hardpoint_imported=true
constructor_side_gates_carried=true
semiprime_diagonal_router_imported=true
diagonal_offdiagonal_support_split_closed=true
diagonal_private_escape_removed=true
common_packet_cycle_guard_carried_forward=true
latest_basis_replaces_first_seed_with_offdiag_seed=true
offdiagonal_ordered_semiprime_signed_seed_table_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
nonzero_signed_row_survival_proved=false
same_formal_unit_row_mass_normalization_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward
```

formal-to-actual 含义是：`p=q` diagonal seed 不是新的 signed 生成自由度；它已并回 common
source packet，并由 source-packet 三原子携带。剩余新增 seed 口为 offdiagonal 表：

```text
PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward
```

同时仍需：

```text
PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
AND AlphaRowAnchorPhaseEmissionFormulaLedger
AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
```

complete/fixed key、ExactUV、pointwise signed table、terminal/PDEC、模型、Rate 与 DStructure
仍开放。行/列命题仍未无条件闭合。

## 391. Phi-LPF latest constructor offdiagonal seed tuple sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_offdiagonal_seed_tuple_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-offdiagonal-seed-tuple-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-offdiagonal-seed-tuple-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-offdiagonal-seed-tuple-sync-ledger.json
```

同步结果：

```text
latest_constructor_offdiagonal_seed_hardpoint_imported=true
constructor_side_gates_carried=true
offdiagonal_tuple_fields_router_imported=true
offdiagonal_source_tuple_bijection_synced=true
offdiagonal_phi_tail_fiber_mass_synced=true
offdiagonal_unsigned_tuple_fields_closed=true
lpf_phi_unsigned_scope_exhausted_for_offdiag_seed=true
latest_basis_replaces_offdiag_seed_with_tuple_payload=true
offdiagonal_signed_seed_formula_proved=false
offdiagonal_orientation_parity_law_proved=false
offdiagonal_exactuv_fixed_pair_return_ledger_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
nonzero_signed_row_survival_proved=false
same_formal_unit_row_mass_normalization_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward
```

formal-to-actual 含义是：LPF/Phi 桶恒等式只能把 offdiagonal occurrence 读成
`(owner_p, first_q, q_rough_tail_t)`，并以 `sum_{p<q} Phi(floor(N/(p*q)),q)`
支付 tail fiber mass。这个无符号账本切断了“从容量反推 signed seed”的跳步。

新的 constructor 最新窄口为：

```text
PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward
```

同时仍需：

```text
PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
```

complete/fixed key、ExactUV、pointwise signed table、terminal/PDEC、模型、Rate 与 DStructure
仍开放。行/列命题仍未无条件闭合。

## 392. Phi-LPF latest constructor pure-pair atom sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_pure_pair_atom_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-pure-pair-atom-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-pure-pair-atom-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-pure-pair-atom-sync-ledger.json
```

同步结果：

```text
latest_constructor_source_tuple_signed_formula_imported=true
constructor_side_gates_carried=true
pure_pair_atom_router_imported=true
pure_pair_atom_bijection_synced=true
tail_lift_phi_minus_one_synced=true
tail_lift_no_new_first_seed_closed=true
latest_basis_replaces_tuple_formula_with_pure_atom=true
pure_semiprime_pair_signed_seed_atom_proved=false
offdiagonal_orientation_parity_law_proved=false
offdiagonal_exactuv_fixed_pair_return_ledger_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
nonzero_signed_row_survival_proved=false
same_formal_unit_row_mass_normalization_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward
```

formal-to-actual 含义是：source tuple signed seed formula 的 first-seed 原子已经被强制定位到
`(p,q,t=1)`。所有 `t>1` 的 `q`-rough continuation 都是同一 first atom 之后的 lift，
其质量为 `Phi(floor(N/(p*q)),q)-1`，必须交给 internal prime-adjoin transition
compatibility，不能作为新的 signed seed 原子。

新的 constructor 最新窄口为：

```text
PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward
```

同时仍需：

```text
PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
```

complete/fixed key、ExactUV、pointwise signed table、terminal/PDEC、模型、Rate 与 DStructure
仍开放。行/列命题仍未无条件闭合。

## 393. Phi-LPF latest constructor pure-pair Ferrers support sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_pure_pair_ferrers_support_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-pure-pair-ferrers-support-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-pure-pair-ferrers-support-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-pure-pair-ferrers-support-sync-ledger.json
```

同步结果：

```text
latest_constructor_pure_pair_atom_imported=true
constructor_side_gates_carried=true
ferrers_support_router_imported=true
ferrers_support_rule_synced=true
ferrers_degree_ledger_synced=true
support_graph_signed_kernel_emission_proved=false
latest_basis_replaces_pure_atom_with_two_prime_kernel=true
two_prime_signed_interaction_kernel_proved=false
offdiagonal_orientation_parity_law_proved=false
offdiagonal_exactuv_fixed_pair_return_ledger_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
nonzero_signed_row_survival_proved=false
same_formal_unit_row_mass_normalization_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward
```

formal-to-actual 含义是：constructor 最新 pure-pair atom 先剥离 Ferrers support。这个账本只
说明哪些 `(p,q)` 边存在、左/右度数是多少、总边数是多少；它不能替代两素数 signed
interaction kernel，也不能给 orientation parity、ExactUV return 或 local factor。

新的 constructor 最新窄口为：

```text
PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward
```

同时仍需：

```text
PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
```

complete/fixed key、ExactUV、pointwise signed table、terminal/PDEC、模型、Rate 与 DStructure
仍开放。行/列命题仍未无条件闭合。

## 394. Phi-LPF latest constructor two-prime no-swap sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_two_prime_no_swap_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-two-prime-no-swap-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-two-prime-no-swap-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-two-prime-no-swap-sync-ledger.json
```

同步结果：

```text
latest_constructor_two_prime_kernel_imported=true
constructor_side_gates_carried=true
no_swap_router_imported=true
lpf_owner_ordered_no_swap_synced=true
product_symmetry_signed_emission_proved=false
latest_basis_replaces_two_prime_kernel_with_edge_local_formula=true
edge_local_two_prime_signed_formula_proved=false
two_prime_signed_interaction_kernel_proved=false
offdiagonal_orientation_parity_law_proved=false
offdiagonal_exactuv_fixed_pair_return_ledger_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
nonzero_signed_row_survival_proved=false
same_formal_unit_row_mass_normalization_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward
```

formal-to-actual 含义是：constructor 最新 two-prime kernel 不能利用 `pq=qp` 制造反向
signed source。canonical LPF owner edge 已经强制为 `(p,q), p<q`，所以 no-swap 只删除
交换伪出口，不提交 edge-local signed formula。

新的 constructor 最新窄口为：

```text
PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward
```

同时仍需：

```text
PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
```

complete/fixed key、ExactUV、pointwise signed table、terminal/PDEC、模型、Rate 与 DStructure
仍开放。行/列命题仍未无条件闭合。

## 395. Phi-LPF latest constructor edge-local field-cut sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_edge_local_field_cut_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-edge-local-field-cut-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-edge-local-field-cut-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-edge-local-field-cut-sync-ledger.json
```

同步结果：

```text
latest_constructor_edge_local_formula_imported=true
constructor_side_gates_carried=true
field_cut_router_imported=true
closed_unsigned_edge_label_ledger_synced=true
edge_atom_multiplicity_one_synced=true
lpf_phi_unsigned_scope_exhausted_for_edge_local=true
constructor_side_gates_not_paid_by_field_cut=true
latest_constructor_basis_replaces_edge_local_formula_with_signed_atom_fields=true
signed_atom_field_table_proved=false
orientation_parity_branch_side_proved=false
exactuv_fixed_pair_return_tag_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
nonzero_signed_row_survival_proved=false
same_formal_unit_row_mass_normalization_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward
```

formal-to-actual 含义是：constructor 最新 edge-local formula 已完成无符号 field-cut。
LPF/Phi/Ferrers 只支付 canonical edge 的 owner、first prime、product、rank/degree 与
multiplicity-one label；它不支付 sign、local factor、orientation、ExactUV return 或
source-row emission。

新的 constructor 最新窄口为：

```text
PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward
```

同时仍需：

```text
PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
```

complete/fixed key、ExactUV、pointwise signed table、terminal/PDEC、模型、Rate 与 DStructure
仍开放。行/列命题仍未无条件闭合。

## 396. Phi-LPF latest constructor signed atom trace-sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_signed_atom_trace_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-signed-atom-trace-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-signed-atom-trace-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-signed-atom-trace-sync-ledger.json
```

同步结果：

```text
latest_constructor_signed_atom_fields_imported=true
constructor_side_gates_carried=true
trace_sync_router_imported=true
closed_unsigned_labels_carried=true
same_trace_key_and_named_return_matrix_synced=true
constructor_source_atoms_carried_forward=true
constructor_side_gates_not_paid_by_trace_sync=true
trace_self_proof_cycle_cut_synced=true
latest_constructor_basis_replaces_signed_atom_fields_with_new_payload_or_exits=true
new_primitive_payload_or_trace_artifact_present=false
edge_local_signed_atom_fields_proved=false
nonzero_signed_row_survival_proved=false
same_formal_unit_row_mass_normalization_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact
```

formal-to-actual 含义是：constructor 最新 signed atom fields 已被接入同 trace key 与命名
return 矩阵。无符号 LPF/Phi/Ferrers label 只给输入域；它不能生成 signed payload。
若同一 edge 的 signed value、local factor、orientation、alpha/delta side、ExactUV fixed pair
或 source row 缺失/冲突/跨 key，则必须进入命名 return/PDEC。

新的 constructor 最新窄口为：

```text
NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact
```

同时仍需：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
CompletePrimitiveEmitterKeyPartitionLedger
FixedKeyExactUVLocalMultiplicityO1Ledger
```

terminal descent、same-set PDEC、逐点 signed table、ExactUV、模型、Rate 与 DStructure
仍开放。行/列命题仍未无条件闭合。

## 397. Phi-LPF latest constructor new-payload source-atom alignment sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_latest_constructor_new_payload_source_atom_alignment_sync_router.py
docs/monograph/prime-matrix-phi-lpf-latest-constructor-new-payload-source-atom-alignment-sync-router.md
docs/monograph/prime-matrix-phi-lpf-latest-constructor-new-payload-source-atom-alignment-sync-router.json
data/prime-matrix-phi-lpf-latest-constructor-new-payload-source-atom-alignment-sync-ledger.json
```

同步结果：

```text
latest_constructor_new_payload_imported=true
constructor_source_and_side_gates_carried=true
latest_unsigned_labels_cannot_pay_payload=true
signed_lane_cycle_cut_carried=true
strict_new_payload_alignment_imported=true
latest_constructor_new_payload_reduced_to_source_rank_atom=true
constructor_source_atoms_carried_forward=true
constructor_row_mass_and_survival_still_open=true
independent_new_payload_terminal_present=false
actual_source_domain_entropy_proved=false
complete_primitive_emitter_key_partition_proved=false
fixed_key_exact_uv_local_multiplicity_proved=false
nonzero_signed_row_survival_proved=false
same_formal_unit_row_mass_normalization_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=ActualPreCauchySourceDomainAbsoluteEntropyLedger
```

formal-to-actual 含义是：constructor latest new-payload 若要成为真正新工件，必须落到
actual source-rank/no-collapse 包，而不是作为未解析黑箱停留。无符号 LPF/Phi/Ferrers
label 与同 trace-key return 矩阵只给出输入域和失败命名，不给 source-domain entropy。

新的 constructor 最新窄口为：

```text
ActualPreCauchySourceDomainAbsoluteEntropyLedger
```

同时仍需：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
CompletePrimitiveEmitterKeyPartitionLedger
FixedKeyExactUVLocalMultiplicityO1Ledger
```

terminal descent、same-set PDEC、逐点 signed table、ExactUV、模型、Rate 与 DStructure
仍开放。行/列命题仍未无条件闭合。

## 329. Phi-LPF source packet cycle guard sync frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_source_packet_cycle_guard_sync_router.py
docs/monograph/prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.md
docs/monograph/prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.json
data/prime-matrix-phi-lpf-source-packet-cycle-guard-sync-ledger.json
```

同步结果：

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

formal-to-actual 含义是：LPF/Phi 的 square-base 几何已经完成其职责；继续推进 common
packet 会落入 signed-lane 自证闭环。非循环推进必须新增 signed 信息，或证明回流严格下降/
同集 PDEC scope，而不是从 Phi support/capacity 反推 signed payload。既有 post-antisplit
收敛证书已经把 NewPrimitive/terminal 出口吸收到 source-rank/no-collapse 与逐点 primitive
核表，因此本层同步到更靠后的共同核表原子。

当前真正非循环出口为：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger
AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
```

并行仍需：

```text
ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward
PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward
```

行/列命题仍未无条件闭合。

## 328. Phi-LPF square-base source packet reduction frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_square_base_source_packet_reduction_router.py
docs/monograph/prime-matrix-phi-lpf-square-base-source-packet-reduction-router.md
docs/monograph/prime-matrix-phi-lpf-square-base-source-packet-reduction-router.json
data/prime-matrix-phi-lpf-square-base-source-packet-reduction-ledger.json
```

同步结果：

```text
lpf_root_and_prime_leak_fields_fixed=true
declaration_field_map_complete=true
no_square_base_private_signed_escape_proved=true
pre_cauchy_actual_noncanonical_emitter_source_declaration_packet_proved=false
built_in_signed_coefficient_pairing_closed_form_proved=false
exactuv_entropy_fiber_pair_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：square-base root 的 LPF 几何字段已经是前置已固定字段；
它不再提供新的 signed 生成自由度。若要为 `(p,p)` 生成 actual signed source，只能提交
同一 common pre-Cauchy packet 中的 source tuple、primitive rows、basis-word/coefficient
identity、prepushforward identity、ExactUV entropy/fiber 和 named return partition。

本层关闭的是 square-base 私有 signed 出口。真正未闭合的是：

```text
PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket
AND BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
AND ActualEmitterSourceDomainEntropyLedger
AND ExactUVMapFixedPairPolylogFiberBoundLedger
AND PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward
AND PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward
```

并行替代仍是直接提交
`PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward`。行/列命题仍未
无条件闭合。

## 327. Phi-LPF square-base diagonal source frontier

新增文件

```text
experiments/prime_matrix_phi_lpf_square_base_diagonal_source_router.py
docs/monograph/prime-matrix-phi-lpf-square-base-diagonal-source-router.md
docs/monograph/prime-matrix-phi-lpf-square-base-diagonal-source-router.json
data/prime-matrix-phi-lpf-square-base-diagonal-source-ledger.json
```

同步结果：

```text
virtual_unit_not_composite_support_proved=true
square_base_minimal_support_root_proved=true
no_support_predecessor_below_square_base_proved=true
virtual_seed_collapses_to_square_base_declaration=true
square_base_diagonal_root_signed_source_declaration_proved=false
phi_lpf_rough_cofactor_signed_transport_law_proved=false
row_column_unconditional_closed=false
```

formal-to-actual 含义是：virtual-unit seed 不能作为独立 actual signed source。`(p,1)`
只指向被 Phi 公式排除的 prime row；在 composite support 中，owner bucket `p` 的最小
真实 rough cofactor 是 `m=p`，即 square-base key `(p,p)`。因此 seed 接口不再是
“prime row 或 square-base 二选一”，而是必须在 square-base root 上正向声明 signed source。

本层关闭的是 virtual-unit 独立出口和 square-base minimal-root 结构。真正未闭合的是：

```text
PhiLPFSquareBaseDiagonalRootSignedSourceDeclarationBeforePushforward
AND PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward
AND PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward
```

并行替代仍是直接提交
`PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward`。行/列命题仍未
无条件闭合。
