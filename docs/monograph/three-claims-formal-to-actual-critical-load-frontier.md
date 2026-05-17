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
