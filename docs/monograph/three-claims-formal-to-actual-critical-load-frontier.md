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
