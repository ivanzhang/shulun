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
