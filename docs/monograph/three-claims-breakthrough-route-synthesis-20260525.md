# 三命题突破路线总合成（2026-05-25）

## 0. 总裁定

本轮重新盘点合著稿三条主命题、Phi-LPF 最新终端相位账本、actual-load 临界原则和外部前沿定理后，结论如下：

```text
three_claim_breakthrough_synthesis_archived=true
row_column_unconditional_closed=false
two_point_unconditional_closed=false
rh_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
phi_lpf_parity_barrier_globally_broken=false
```

完整无条件闭合尚未完成。当前不能把有限账本、局部结构恒等式、wheel 精细化或外部 trace/Kloosterman 候选输入误写成三命题之一的终稿证明。

本轮给出的真实推进是：把“继续向哪里突破”从循环式改名压成一个非循环选择器。最快真推进仍在 Prime Matrix 行/列 Phi-LPF 线，但目标必须改为

```text
ActualSignedPayloadTraceConstructorBeforeAssignmentOrReturn
OR MonotoneRunPhaseSavingWithExtraBudgetAbsorption
OR PDEC/SAE/LocalSurvivor named return
```

而不是继续单纯升级 `30`-wheel 到 `210,2310,...` 或继续追加同类有限相位账本。wheel 能细分局部类，但不能自动产生跨 prime-q 的相消。

## 1. 三命题当前前沿

| 命题 | 当前最好压缩形态 | 真剩余硬点 | 本轮判定 |
| --- | --- | --- | --- |
| Prime Matrix 行/列 | Phi-LPF 支撑、q-prefix、rough envelope、bulk/boundary、hole-class、packet enclosure、terminal phase-turn/variation 均已高度物化 | `PrimeQSupportSetReciprocalPhaseSavingBeyondParity`，最新局部门为 `SelectedTerminalNegativeVariationExcessPhaseSaving` 与 `ExtraNegativeVariationBudgetAbsorption` | 最适合继续做非循环局部推进，但尚非完整命题闭合 |
| 二点筛 / quadratic secondary sieve | `DI/BFI => KLS-window => ... => BMD` 方向清楚，actual-ratio 合同已写成分子/分母同 convention 问题 | `BMD=>TLI without hidden denominator/parity gap`，即 denominator floor 与 numerator load 必须同一奇异级数 convention 匹配 | 若外部 DI/BFI/KLS 适配被接受，完整命题突破可能只剩 denominator-floor 真硬点；但当前仍未闭合 |
| RH contradiction field | controlled exits、Backlund 相关内部包络和 D-structure/Rankin 边界大量物化 | `IndependentRefereeAcceptanceOfAllRHControlledExits` 与 D-structure/Rankin 晋级验收 | 最不适合作为本轮“先突破”目标；更像审稿验证工程 |

## 2. 已探索路线的可复用成果

### 2.1 Phi-LPF / Prime Matrix 线

已闭合的是真结构账本：

- LPF 恒等式、Phi 递推式、P 阶递降、递归剥离给出了候选集合的精确重写；
- q-prefix/unimodal、rough envelope cap、bulk rectangle Type-II、boundary strip、layer-cake rectangles 证明了支撑形状不是黑箱；
- hole correction 已拆成 `empty/even/prime/LPF3/LPF5` 五类，排除了 `LPF>=7` 奇合 hole；
- repeated-step 路线从 DAG、path-cover、P-switch、occurrence splice、affine skeleton、packet enclosure 推进到 terminal line atoms；
- terminal phase normal form、carry orbit、phase-turn word 和 signed variation budget 已闭合，selected terminal 有 `66` transitions、`35` runs、最大 run `6`，负变差超过正变差约 `1.456565972578`。

这些成果的核心价值是：候选结构已经足够窄，可以要求下一步输出一个真正的 signed payload family，而不是继续扩大 formal envelope。

### 2.2 被排除或降级的路线

- P2 最早见证 selector 被反例审计排除；
- composite P2 support saturation 表明支撑层面可完全覆盖素数残差类，support-only 不能破奇偶；
- complete CRT 周期均匀只给完整周期平均，不给短窗口逐类正性；
- rank-one 负评价排斥等价于 `theta(P^2;P,a)>0` 对每个非零类成立，本质上是 sharp pointwise AP positivity / Linnik=2 型硬点；
- `30`-wheel、`210`-wheel、`2310`-wheel 可以细分 parity packets，但若没有新的 signed phase saving 或 actual-load return，只会重命名同一个障碍。

### 2.2A affine `2n+1` Euler-LPF 诊断

用户提出的结构

```text
n = kP + (P-1)/2  =>  2n+1 = (2k+1)P
```

给出一个有用但必须修正口径的 affine 筛余恒等式。`P` 是 `2n+1` 的因子，不是 `n`
的因子；若 `k>=1` 且 `2k+1` 无小于 `P` 的素因子，则 `P=LPF(2n+1)`。

新增审计：

```text
experiments/prime_matrix_affine_2n_plus_1_euler_lpf_parity_audit.py
data/prime-matrix-affine-2n-plus-1-euler-lpf-parity-ledger.json
docs/monograph/prime-matrix-affine-2n-plus-1-euler-lpf-parity-audit.md
docs/monograph/prime-matrix-affine-2n-plus-1-euler-lpf-parity-audit.json
```

它验证了精确双射

```text
p | (2n+1)  <=>  n == (p-1)/2 mod p       (p odd)
```

并在 `P=11,31,101,251,1009`、`x=P^2` 上确认：

```text
affine_sieve_bijection_verified_all_samples=true
apparent_half_main_gap_explained_by_missing_p2_all_samples=true
euler_product_half_main_error_proved=false
phi_lpf_parity_barrier_globally_broken=false
```

结论是：若在 `m=2n+1` 侧用长度约 `2x` 的区间却只乘奇素数部分欧拉乘积，会出现
“exact count 比 naive main 少约一半”的假象；但这是漏掉 `p=2` 或没有先限制到
奇数样本空间造成的归一化错误。正确 odd-space 主项与 `n` 侧 shifted-residue 主项已经对齐。
因此该结构可作为 shifted-residue Phi-LPF 账本迭代，但不能直接推出有限欧拉乘积截断误差为
主项一半，也不能从 rough survivors 中分离素数。

后续 power-two 迭代审计进一步确认这一点：

```text
experiments/prime_matrix_affine_power_two_phi_lpf_iteration_no_gain_audit.py
data/prime-matrix-affine-power-two-phi-lpf-iteration-no-gain-ledger.json
docs/monograph/prime-matrix-affine-power-two-phi-lpf-iteration-no-gain-audit.md
docs/monograph/prime-matrix-affine-power-two-phi-lpf-iteration-no-gain-audit.json
```

对

```text
m_t = 2^t n + (2^t-1)
```

仍有

```text
p | m_t  <=>  n == -(2^t-1)*(2^t)^(-1) mod p     (p odd).
```

有限审计 `P=31,101,251,1009`、`t=1,2,3,4` 显示：

```text
all_shifted_residue_formula_verified=true
iteration_creates_new_phi_lpf_information=false
euler_product_half_main_error_proved=false
phi_lpf_parity_barrier_globally_broken=false
```

naive gap 跟随 `1-2^{-t}`，所以迭代只改变固定 `2^t`-adic residue space；归一化后
仍是 affine rough survivors 的 prime extraction 问题。

### 2.2B small-to-large factor-peeling 诊断

用户提出的“从小到大精细化分剥素因子”是 Phi-LPF 路线中真实可物化的一层，但必须区分
两件事：

```text
closed:  ordered factor word, squarefree, Möbius, Liouville, depth parity
open:    pre-Cauchy signed coefficient, orientation/local factor, ExactUV source trace
```

新增审计：

```text
experiments/prime_matrix_phi_lpf_small_to_large_factor_peeling_signed_state_boundary_router.py
data/prime-matrix-phi-lpf-small-to-large-factor-peeling-signed-state-boundary-ledger.json
docs/monograph/prime-matrix-phi-lpf-small-to-large-factor-peeling-signed-state-boundary-router.md
docs/monograph/prime-matrix-phi-lpf-small-to-large-factor-peeling-signed-state-boundary-router.json
```

对 `N=100,997,5003,10000,30030` 的 LPF-owned composite buckets 逐个剥离 cofactor，
最大样本 `N=30030` 给出：

```text
composite_support_keys=26781
owner_bucket_count=40
total_small_to_large_factor_steps=69651
max_factor_depth=13
tail_mobius_positive/negative/zero=8367/11306/7108
tail_liouville_positive/negative=11810/14971
small_to_large_factor_peeling_verified_all_samples=true
mobius_liouville_state_computable_from_factor_word_all_samples=true
```

因此，所有自然 parity-state 都只是 factor word 的后验标签。它们关闭了“继续剥离也许自动
生成 signed payload”的误出口，但不能替代

```text
PrimitiveOrientationLocalFactorProductLawBeforePushforward
OR BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows.
```

这一步的真实推进是把“剥离素因子”从开放口移入无符号已支付边界，并把非循环主攻继续压在
pre-Cauchy signed law / built-in pairing 上。它没有破奇偶性障碍。

### 2.3 二点筛线

已知强点是外部谱工具方向最接近标准解析数论形态：DI/BFI/Kloosterman 大筛与 well-factorable 权重可以服务 BMD/KLS 分子估计。当前缺口不是“再找一个 Kloosterman 定理”，而是：

```text
actual numerator bound
AND actual denominator floor
AND same singular-series convention
AND delta(alpha)+epsilon(alpha)<1-K(alpha)
```

若 denominator floor 失败，必须变成低模二次型、character defect 或 endpoint smoothing defect，不能藏成 parity gap。

### 2.4 RH 线

RH 线的成果更多是受控出口与审稿包。它适合继续做独立验证、常数核查和 controlled-exit 接口审稿，不适合作为本轮最快突破目标。

## 3. 外部前沿定理的真实作用

| 外部输入 | 可用方向 | 不能替代 |
| --- | --- | --- |
| DI / BFI dispersion / Kuznetsov | 二点筛 BMD/KLS 外部版；若能归一化相位、模数、频率和 well-factorable 权重，可作为深输入 | 不能给 Prime Matrix 的逐 residue `theta(P^2;P,a)>0` |
| FKMS trace/bilinear、Milićević--Qin--Wu arbitrary-modulus Kloosterman、Pascadi composite Type-II、Wright unbalanced Kloosterman fractions | 一旦我们构造出可求和的完成型 trace/Kloosterman/Type-II family，可作为候选相消工具 | 不能直接作用于当前 finite terminal run ledger 或未完成的 real reciprocal phase |
| Li short intervals `x^0.52` | 给通用短区间素数存在性边界 | 在 `x=P^2` 下窗口长于目标 `P`，不能闭合行/列 |
| Maynard 小间距 | 证明存在很多小素数间隙 | 不控制每个固定行、每个 AP 类或 terminal signed variation |
| Dong--Robles--Zeindler 撤稿项 | 只能作为不可用边界记录 | 不得作为证明输入 |

因此外部定理的使用顺序必须是：

```text
先构造 admissible averaged family
再调用 trace/Kloosterman/Type-II theorem
最后把相消返回 actual load 或 named return
```

## 4. 非循环突破选择

### 4.1 不应继续主攻的方向

1. 直接证明 `theta(P^2;P,a)>0` for every `a mod P`：这等价于 sharp AP positivity，现有 GRH-shape、BV 平均、完整 CRT 均不够。
2. 只升级 wheel：wheel 细分类，不产生相消。
3. 只追加有限 terminal ledger：上一轮 variation budget 已显示 selected terminal 并无“自动平衡”；继续同口径只会得到更细的未证 phase-saving 名称。
4. 用 support saturation 代替 prime extraction：这正是奇偶性障碍。

### 4.2 本轮首攻目标

首攻 Prime Matrix / Phi-LPF 线，但目标必须是下述三分定理接口：

```text
Terminal signed payload either
  (A) forms an admissible averaged trace/Kloosterman or Type-II family,
  (B) has monotone-run phase saving large enough to absorb extra variation,
  (C) returns a named PDEC/SAE/LocalSurvivor defect.
```

更具体地说，下一步不能再问“这个 atom 的局部账本还能不能拆”；应问：

```text
给定 selected terminal 的 35 个 monotone runs 与 extra shell 的 24 个 runs，
是否能构造一个统一 signed payload measure mu(q,m,packet)
使得
  selected negative variation excess
  minus extra absorption cost
在每个 non-return branch 上进入可求和 trace family？
```

若不能构造，则失败形态必须被命名为 PDEC/SAE/LocalSurvivor，而不是保留匿名 “phase saving open”。

## 5. 目标命题闭合条件

当前任一完整命题真正闭合需要至少完成下表之一：

| 命题 | 必要闭合包 |
| --- | --- |
| Prime Matrix 行/列 | `PrimeQSupportSetReciprocalPhaseSavingBeyondParity` 或 `ExplicitAPZeroPacketBoundBeatingMainTermAtXEqualsP2` 或 terminal payload 全部回流 PDEC/SAE 且通过 D-structure/Rankin 验收 |
| 二点筛 | `BMD=>TLI` 的 actual-ratio transfer，含 denominator floor、numerator bound、同 convention 误差优势与 parity failure return |
| RH | 所有 controlled exits 独立审稿接受，且 D-structure/Tail-log4/finite Rankin 晋级包接受 |

本轮没有完成上述任何一包。因此完整目标命题仍未无条件闭合。

## 6. 下一步可执行清单

1. 对最新 terminal variation ledger 建立 `mu(q,m,packet)` signed payload schema。
2. 把 selected terminal 与 extra shell 的 run 预算写成同一 absorption inequality。
3. 若 inequality 不能直接闭合，提取最小失败原子并强制分类为 `PDEC/SAE/LocalSurvivor`。
4. 只有在得到 averaged family 后，才调用 FKMS/Milićević--Qin--Wu/Pascadi/Wright 类输入。
5. 并行保留二点筛 denominator-floor 合同作为第二候选突破口。

### 6.1 factor-word parity shadow no-go 更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_factor_word_parity_shadow_orientation_nogo_router.py
data/prime-matrix-phi-lpf-factor-word-parity-shadow-orientation-nogo-ledger.json
docs/monograph/prime-matrix-phi-lpf-factor-word-parity-shadow-orientation-nogo-router.md
docs/monograph/prime-matrix-phi-lpf-factor-word-parity-shadow-orientation-nogo-router.json
```

本轮检验了最直接的“从小到大剥离素因子后用 parity shadow 破 signed law”捷径。
结果是：

```text
factor_word_mobius_shadow_closed=true
factor_word_liouville_shadow_closed=true
depth_parity_shadow_closed=true
shadow_depends_only_on_unsigned_factor_word=true
shadow_lacks_precauchy_source_key=true
shadow_lacks_orientation_branch_trace=true
shadow_lacks_exactuv_payload=true
factor_word_shadow_proves_orientation_local_factor_law=false
factor_word_shadow_proves_builtin_pairing=false
```

这一步把一个看似接近 Euler/Mobius 的入口精确归档为 no-go：它能解释 factorization
parity，却不能生成推前前 signed coefficient。突破选择因此更窄，不再是继续找
factor-word 标签，而是必须提交下列之一：

```text
PrimitiveOrientationLocalFactorProductLawBeforePushforward
OR BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
OR admissible averaged signed trace/Kloosterman/Type-II family with named returns
```

### 6.2 terminal signed payload measure 吸收前沿更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_signed_payload_measure_absorption_frontier_router.py
data/prime-matrix-phi-lpf-terminal-signed-payload-measure-absorption-frontier-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-signed-payload-measure-absorption-frontier-router.md
docs/monograph/prime-matrix-phi-lpf-terminal-signed-payload-measure-absorption-frontier-router.json
```

本层完成了上一轮清单中的第一步和第二步：建立 `mu(q,m,packet)` signed payload schema，
并把 selected terminal 与 extra shell 的预算放进同一个 absorption inequality。读数为：

```text
terminal_signed_payload_measure_schema_closed=true
mu_transition_count=126
selected_net_excess_beats_extra_net_excess=true
net_excess_absorption_margin=0.548846649396
selected_net_excess_beats_extra_total_variation=false
strong_total_variation_absorption_margin=-12.652735908584
selected_excess_to_extra_total_ratio=0.103234446668
```

这是真推进但不是闭合：净超额吸收可过，强总变差吸收不过。下一步不应回到
factor-word、wheel 或有限 run 细分，而应攻击：

```text
MonotoneRunTotalToNetCompressionOrPDEC
AND ExtraTotalVariationAbsorptionOrLocalSurvivor
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

若 total-to-net 压缩失败，失败形态必须命名为 PDEC/SAE/LocalSurvivor，而不能保留为
匿名 phase-saving open。

### 6.3 terminal monotone-run total-to-net compression 前沿更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_monotone_run_total_to_net_compression_frontier_router.py
data/prime-matrix-phi-lpf-terminal-monotone-run-total-to-net-compression-frontier-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-monotone-run-total-to-net-compression-frontier-router.md
docs/monograph/prime-matrix-phi-lpf-terminal-monotone-run-total-to-net-compression-frontier-router.json
```

本层把上一节的 `MonotoneRunTotalToNetCompressionOrPDEC` 真正拆开：

```text
terminal_run_count_total=59
selected_terminal_run_count=35
extra_shell_run_count=24
strict_run_local_compression_count=0
atom_adjacent_cancellation_decomposition_closed=true
finite_absorption_would_close_after_uniform_cancellation_law=true
monotone_run_total_to_net_compression_proved=false
uniform_run_cancellation_family_created=false
```

关键新读数是：每个 monotone run 内部都有

```text
variation=abs(signed_delta)
```

所以 run 内没有任何相消。有限压缩全部来自相邻反向 run 的抵消；按 atom 分解后，
extra total variation 从

```text
14.109301881162
```

压到 atom-local survivor

```text
0.907719323182
```

而 selected negative excess 为

```text
1.456565972578
```

因此若能证明 uniform adjacent-run cancellation law，有限 terminal extra budget 会被支付。
但这恰好是新硬点：有限分解不是全局 phase saving。下一步必须提交以下之一：

```text
UniformAdjacentRunCancellationFamilyOrPDEC
AND AtomLocalSurvivorPaymentOrPDEC
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

### 6.4 terminal adjacent-run Jordan cancellation 源保持障碍更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_adjacent_run_jordan_cancellation_source_obstruction_router.py
data/prime-matrix-phi-lpf-terminal-adjacent-run-jordan-cancellation-source-obstruction-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-adjacent-run-jordan-cancellation-source-obstruction-router.md
docs/monograph/prime-matrix-phi-lpf-terminal-adjacent-run-jordan-cancellation-source-obstruction-router.json
```

本层找到了统一相邻抵消律的形式版本：

```text
sign_matches_Awrap_all_transitions=true
maximal_run_reconstruction_closed=true
signed_telescoping_identity_closed=true
formal_jordan_cancellation_law_closed=true
```

精确说，符号由 `A(q)/q` 是否 wrap 决定；相邻 run 抵消就是一维相位路径的
signed telescoping/Jordan 分解。这是有用的统一结构，但还不是 actual-load 闭合。
阻断点也被精确量化：

```text
cancellation_event_count=51
complete_whole_run_pair_event_count=0
synthetic_split_cancellation_event_count=51
internal_survivor_fragment_count=1
tail_only_survivor_law_proved=false
source_preserving_adjacent_run_pairing_constructed=false
```

也就是说，有限抵消需要切分 run 质量块，并且存在内部 survivor：

```text
right:1887:selected_terminal:m773, run 2, q=[449,457], mass=0.017995938314
```

所以最新非循环口不是“再找形式 telescoping”，而是：

```text
SourcePreservingAdjacentRunPairingOrInternalSurvivorPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

### 6.5 terminal prefix-record source-key lift 障碍更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_prefix_record_source_key_obstruction_router.py
data/prime-matrix-phi-lpf-terminal-prefix-record-source-key-obstruction-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-prefix-record-source-key-obstruction-router.md
docs/monograph/prime-matrix-phi-lpf-terminal-prefix-record-source-key-obstruction-router.json
```

本层不是重复上一轮 Jordan 账本，而是把它继续压成 prefix-record/reflection 账本：

```text
previous_formal_jordan_cancellation_law_closed=true
prefix_record_reflection_schema_closed=true
terminal_atom_count=7
terminal_run_count_total=59
cancellation_event_count=51
```

这给出一个更窄但仍未闭合的真实硬点。所有抵消事件都不是完整 run pair：

```text
whole_run_pair_event_count=0
synthetic_split_event_count=51
q_boundary_pair_event_count=47
non_q_boundary_pair_event_count=4
survivor_fragment_count_total=8
internal_survivor_fragment_count=1
prefix_record_source_key_lift_constructed=false
row_column_unconditional_closed=false
```

因此当前最快路线不是再找一维反射恒等式，而是把 prefix-record chunk 提升为
source-key/source-preserving actual object，或者把内部 survivor 回流为 PDEC/LocalSurvivor，
或者构造可求和的 averaged trace/Kloosterman/Type-II family：

```text
PrefixRecordSourceKeyLiftOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

### 6.6 terminal source-key obstruction partition 更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_source_key_obstruction_partition_router.py
data/prime-matrix-phi-lpf-terminal-source-key-obstruction-partition-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-source-key-obstruction-partition-router.md
docs/monograph/prime-matrix-phi-lpf-terminal-source-key-obstruction-partition-router.json
```

本层继续非循环推进：不再把 `source-key lift` 当成单个黑箱，而是拆成三类明确对象：

```text
source_key_obstruction_partition_closed=true
q_boundary_synthetic_split_event_count=47
nonboundary_record_jump_event_count=4
tail_survivor_fragment_count=7
internal_survivor_fragment_count=1
```

非边界 jump 只出现在两个 selected-terminal atom；内部 survivor 只有一处。有限标量检查：

```text
nonboundary_plus_internal_obstruction_mass=0.215539338772
finite_selected_margin_after_nonboundary_internal_payment=0.333307310624
```

因此下一步不应继续寻找新的形式反射恒等式，而应优先攻击 47 个 q-boundary synthetic
split 的 ratio/source-key law；其余两个出口则是 non-boundary record jump lift 和 internal
survivor PDEC 回流。最新口：

```text
BoundarySyntheticSplitRatioSourceKeyLawOrPDEC
AND NonBoundaryPrefixRecordJumpSourceKeyLiftOrPDEC
AND InternalPrefixRecordSurvivorPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

### 6.7 terminal boundary split ratio obstruction 更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_boundary_split_ratio_obstruction_router.py
data/prime-matrix-phi-lpf-terminal-boundary-split-ratio-obstruction-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-split-ratio-obstruction-router.md
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-split-ratio-obstruction-router.json
```

本层把最大分支 `47` 个 q-boundary synthetic split 压成 exact ratio spectrum：

```text
boundary_ratio_spectrum_closed=true
q_boundary_synthetic_split_event_count=47
boundary_adjacency_closed=true
whole_equal_pair_event_count=0
old_consumed_new_residual_event_count=42
old_residual_new_consumed_event_count=5
```

关键读数：

```text
ratio_min=0.013003592969
ratio_max=0.967151620496
boundary_residual_gap_mass_total=13.480078809654
boundary_residual_gap_mass_max=0.861355534983
```

因此边界分支的下一步不是再证明“相邻”，而是证明相邻 run 质量比率律，或证明残流在
source-key 层可守恒/回流。最新口：

```text
BoundaryAdjacentRunMassRatioLawOrPDEC
AND BoundaryResidualFlowSourceKeyConservationOrPDEC
AND NonBoundaryPrefixRecordJumpSourceKeyLiftOrPDEC
AND InternalPrefixRecordSurvivorPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

### 6.8 terminal boundary residual-flow obstruction 更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_boundary_residual_flow_obstruction_router.py
data/prime-matrix-phi-lpf-terminal-boundary-residual-flow-obstruction-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-residual-flow-obstruction-router.md
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-residual-flow-obstruction-router.json
```

本层不再重复证明 q-boundary adjacency，而是检验 residual-flow 能否在边界内部
opposite-side 抵消。有限审计读数：

```text
residual_flow_side_decomposition_closed=true
new_residual_side_event_count=42
old_residual_side_event_count=5
new_residual_mass_total=13.264539470882
old_residual_mass_total=0.215539338772
net_new_minus_old_residual_mass=13.049000132111
atomwise_unmatched_residual_mass=13.049000132111
finite_boundary_local_opposite_side_cancellation_refuted=true
row_column_unconditional_closed=false
```

因此“统一相邻抵消律”的形式层已经走到边界：方向事件数几乎平衡
`24` 对 `23`，但质量不平衡，且 residual side 极度偏向 new-run。继续寻找
whole-run 等量配对会回到循环；下一条非循环路线必须解释这个 dominant new
residual source，或把它无损搬运到 non-boundary jump/internal survivor/PDEC
合同中。

最新口：

```text
BoundaryDominantNewResidualSourceLawOrPDEC
AND BoundaryResidualTransportToNonBoundaryInternalReturnsOrPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND BoundaryResidualFlowSourceKeyConservationOrPDEC
AND NonBoundaryPrefixRecordJumpSourceKeyLiftOrPDEC
AND InternalPrefixRecordSurvivorPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

### 6.9 terminal boundary old-residual return alignment 更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_boundary_old_residual_return_alignment_router.py
data/prime-matrix-phi-lpf-terminal-boundary-old-residual-return-alignment-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-old-residual-return-alignment-router.md
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-old-residual-return-alignment-router.json
```

本层抓住上一轮的精确重合：5 个 old-side boundary residual 的总质量等于
nonboundary/internal obstruction mass，并逐项检查 atom/run/q key。结果不是仅有总量相等，
而是逐项返回闭合：

```text
old_residual_return_alignment_closed=true
old_residual_event_count=5
nonboundary_record_jump_event_count=4
internal_survivor_return_count=1
old_residual_equals_nonboundary_plus_internal_obstruction=true
old_residual_total=0.215539338772
matched_old_residual_return_mass=0.215539338772
unmatched_old_residual_return_mass=0
row_column_unconditional_closed=false
```

因此 old-side residual transport 子门关闭：四个 nonboundary record jump 和一个 internal
survivor 不是额外残差库，而是正好支付 old-side boundary residual。剩余真正硬点进一步
集中为 dominant new-side residual source：

```text
new_residual_mass_total_still_open=13.264539470882
```

最新口：

```text
BoundaryDominantNewResidualSourceLawOrPDEC
AND BoundaryNewResidualReturnOrPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

### 6.10 terminal boundary new-residual tail alignment 更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_boundary_new_residual_tail_alignment_router.py
data/prime-matrix-phi-lpf-terminal-boundary-new-residual-tail-alignment-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-new-residual-tail-alignment-router.md
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-new-residual-tail-alignment-router.json
```

本层继续追踪上一轮剩余的 new-side residual。结论是：terminal tail survivor
确实支付了其中一部分，但不是全部：

```text
new_residual_event_count=42
tail_survivor_count=7
new_residual_tail_matched_event_count=6
new_residual_tail_alignment_partial_closed=true
new_residual_tail_matched_mass=1.580044997219
new_residual_unmatched_after_tail_event_count=36
new_residual_unmatched_after_tail_mass=11.684494473663
tail_survivor_unmatched_count=1
tail_survivor_unmatched_mass=0.831750175347
all_new_residual_return_alignment_closed=false
row_column_unconditional_closed=false
```

因此非循环推进的真实收益是把 `BoundaryNewResidualReturnOrPDEC` 拆细：`6`
个 new-side residual 已由 tail return 精确关闭；剩余不再是模糊的 return
问题，而是 `36` 个 bulk source event 加 `1` 个 right selected-terminal tail
overhang。继续寻找全局相邻等量配对会回到旧循环；下一步必须证明 bulk
new-residual source law、给出 overhang PDEC，或把这 `36+1` 个对象构造成
可求和的 signed trace/Type-II/群轨道族。

最新口：

```text
BoundaryBulkNewResidualSourceLawOrPDEC
AND RightSelectedTerminalTailOverhangPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

### 6.11 terminal boundary bulk carry-chain normal form 更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_boundary_bulk_carry_chain_normal_form_router.py
data/prime-matrix-phi-lpf-terminal-boundary-bulk-carry-chain-normal-form-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bulk-carry-chain-normal-form-router.md
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bulk-carry-chain-normal-form-router.json
```

本层继续压缩上一层的 `36` 个 bulk new residual。它们并非 `36` 个独立异常，而是
落入 atomwise carry-chain normal form：

```text
new_residual_event_count=42
bulk_unmatched_new_residual_event_count=36
atom_count=7
carry_segment_count=11
carry_transition_count=31
carry_break_count=4
tail_closed_segment_count=6
open_segment_count=5
all_carry_transitions_exact=true
bulk_carry_chain_normal_form_closed=true
row_column_unconditional_closed=false
```

递推原子为：

```text
old_mass(next boundary run) = residual_mass(previous boundary run)
```

这一步的非循环收益是把 bulk source 从散点问题改写为 `11` 个 segment root
和 `4` 个 carry break 的 source law 问题。它不是奇偶性突破：还没有 uniform
segment-root source bound、right-tail overhang PDEC，也没有可接入 FKMS/MQW/Wright/
Pascadi 型 trace/Kloosterman/Type-II 或 thin-group expansion 的 admissible family。

最新口：

```text
BoundaryBulkCarrySegmentRootSourceLawOrPDEC
AND RightSelectedTerminalTailOverhangPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

### 6.12 terminal boundary carry-break source-packet 更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_boundary_carry_break_source_packet_router.py
data/prime-matrix-phi-lpf-terminal-boundary-carry-break-source-packet-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-carry-break-source-packet-router.md
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-carry-break-source-packet-router.json
```

本层继续拆解 carry-chain normal form 中真正不连续的 `4` 个 carry break。审计显示
它们不是四个独立硬点，而是两个同型 bridge/unit packet：

```text
carry_break_count=4
unit_old_return_echo_break_count=2
bridge_root_debt_break_count=2
paired_bridge_unit_packet_count=2
unmatched_unit_break_count=0
all_unit_echo_breaks_source_aligned_to_old_returns=true
all_bridge_roots_packetized_with_following_unit_echo=true
carry_break_source_packet_reduction_closed=true
row_column_unconditional_closed=false
```

两个 `run_gap=1` 断点的 debt 精确等于同 atom 已登记的 old-side
`nonboundary_record_jump` return mass；两个 `run_gap=3` 断点是对应 old-return
endpoint 的 bridge root，其中 `root_boundary_q` 正好等于该 old-return 的
`new_q_start`。因此 carry-break 层的真实剩余从 `4` 个断点降为 `2` 个
bridge-root debt source law/PDEC。

这一步对用户提出的“统一相邻抵消律”给出一个可检查版本：单位步断点已经是 old-return
echo，不再是新源项；但 bridge-root debt 仍没有 uniform source law。外部谱分析、
Kloosterman/Type-II 或 thin-group 工具仍只能在这些 bridge roots 被组织成可平均
signed family 或群轨道后进入。

最新口：

```text
BoundaryBridgeRootDebtSourceLawOrPDEC
AND RightSelectedTerminalTailOverhangPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

### 6.13 terminal boundary bridge-root q-spine microtemplate 更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_boundary_bridge_root_qspine_microtemplate_router.py
data/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-microtemplate-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-microtemplate-router.md
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-microtemplate-router.json
```

本层继续拆解上一层剩余的两个 bridge-root debt。它们不是两个无关 debt，而是同一个
left `P=739`、packet `2842`、selected-terminal 终端对 `m=757,761` 上的
AD-singleton q-spine：

```text
bridge_root_packet_count=2
all_bridge_roots_share_ad_singleton_template=true
unit_to_bridge_pivot_alignment_closed=true
shared_pivot_q=607
m_gap_between_bridge_packets=4
root_micro_q_shift=30
bridge_to_unit_q_gaps=[30,24]
bridge_root_qspine_microtemplate_closed=true
bridge_root_qspine_source_law_proved=false
row_column_unconditional_closed=false
```

局部模板为：

```text
negative A1/D0 carry 2 singleton
then positive A0/D1 carry 7 singleton
```

并且 q-spine 节点为 `577 -> 607 -> 631`，其中第一包的 unit root `q=607`
正好是第二包的 bridge root。这是对“相邻抵消律”的进一步物化：bridge-root 硬点
现在不是任意源项，而是共享 `q=607` 枢轴的 AD-singleton q-spine 源律。

这仍不是奇偶性突破。外部谱分析、Kloosterman/Type-II 或 thin-group 工具的入口
仍要求先把该 q-spine 变成可平均 signed family 或有限群轨道。

最新口：

```text
BridgeRootADSingletonQSpineSourceLawOrPDEC
AND RightSelectedTerminalTailOverhangPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

### 6.14 terminal boundary bridge-root q-spine Beatty margin 更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_boundary_bridge_root_qspine_beatty_margin_router.py
data/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-beatty-margin-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-beatty-margin-router.md
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-beatty-margin-router.json
```

本层不再把 q-spine 源律停留在几何模板上，而是把四个 AD-singleton 微转移的
相位分子全部压成同一个 Beatty 整数恒等式。若 `m=P+r`、`q'=q+g`、
`a=floor(qr/P)`、`D=qr-aP`、`s=floor((D+gr)/P)`，则

```text
phase_delta_num = lift_step*q*q_next + P*(s*q-a*g)
```

有限审计读数：

```text
micro_transition_count=4
beatty_numerator_identity_closed=true
A_singleton_negative_pure_P_multiple_closed=true
D_singleton_positive_margin_closed=true
bridge_root_qspine_beatty_margin_closed=true
bridge_root_uniform_beatty_margin_source_law_proved=false
row_column_unconditional_closed=false
```

四个微转移的整数 margin 是：

```text
m757 q569->571: r=18, a=13, s=0, B=-26, lift_step=0, numerator=-19214
m757 q571->577: r=18, a=13, s=1, B=493, lift_step=-1, numerator=34860
m761 q599->601: r=22, a=17, s=0, B=-34, lift_step=0, numerator=-25126
m761 q601->607: r=22, a=17, s=1, B=499, lift_step=-1, numerator=3954
```

这一步的实际推进是：`BridgeRootADSingletonQSpineSourceLawOrPDEC` 被替换为更具体的
`BridgeRootADSingletonBeattyMarginSourceLawOrPDEC`。第二个 D-singleton 正
margin 只有 `3954`，说明真正硬点不是有限分子恒等式，而是统一证明该 Beatty
正 margin 不会坍塌，或者给出同对象 PDEC。

最新口：

```text
BridgeRootADSingletonBeattyMarginSourceLawOrPDEC
AND RightSelectedTerminalTailOverhangPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

### 6.15 terminal boundary bridge-root endpoint slack 更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_boundary_bridge_root_endpoint_slack_router.py
data/prime-matrix-phi-lpf-terminal-boundary-bridge-root-endpoint-slack-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-endpoint-slack-router.md
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-endpoint-slack-router.json
```

本层继续拆开 D-singleton 的 Beatty 正 margin。对 D-singleton，

```text
phase_delta_num = q*(P-q-g*(1+r)) + g*D
```

对 A-singleton，

```text
phase_delta_num = -P*a*g
```

有限审计读数：

```text
bridge_root_endpoint_slack_reduction_closed=true
D_singleton_min_endpoint_slack=0
D_singleton_min_positive_margin=3954
D_singleton_zero_slack_rows=['m761 q601->607']
row_column_unconditional_closed=false
```

关键点：最薄的 `m761 q601->607` 行不再是不明正 margin；它的 endpoint slack
正好为 `0`，所以正 margin 全部来自 `gD=6*659=3954`。这把上一层的
`BridgeRootADSingletonBeattyMarginSourceLawOrPDEC` 再替换为更小的
`BridgeRootEndpointSlackNonnegativeLawOrPDEC`。

最新口：

```text
BridgeRootEndpointSlackNonnegativeLawOrPDEC
AND RightSelectedTerminalTailOverhangPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

### 6.16 terminal boundary bridge-root moving endpoint barrier 更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_boundary_bridge_root_moving_endpoint_barrier_router.py
data/prime-matrix-phi-lpf-terminal-boundary-bridge-root-moving-endpoint-barrier-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-moving-endpoint-barrier-router.md
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-moving-endpoint-barrier-router.json
```

本层把 D-singleton endpoint slack 进一步改写为 moving endpoint barrier 距离。若
`q_bridge=q_next`，则

```text
endpoint_slack = P-q-g*(1+r) = (P-g*r)-q_bridge
```

有限审计读数：

```text
bridge_root_moving_endpoint_barrier_reduction_closed=true
endpoint_slack_equals_barrier_distance_closed=true
all_barriers_lie_on_qspine=true
all_bridge_roots_lie_on_qspine=true
finite_bridge_root_barrier_order_closed=true
zero_barrier_contact_count=1
row_column_unconditional_closed=false
```

两条 barrier row 为：

```text
m757 q571->577: r=18, bridge q=577, barrier q=P-gr=631, slack=54
m761 q601->607: r=22, bridge q=607, barrier q=P-gr=607, slack=0
```

关键点：`m761 q601->607` 的最薄行是精确 barrier contact，而不是隐藏负项。
两个 barrier 与两个 bridge root 都落在同一条 q-spine `577 -> 607 -> 631` 上。
两包位移满足

```text
bridge_shift=30
barrier_shift=-24
slack_drop=54=bridge_shift-barrier_shift
```

因此最新硬点从 `BridgeRootEndpointSlackNonnegativeLawOrPDEC` 收窄为
`BridgeRootMovingEndpointBarrierOrderLawOrPDEC`：要么证明 bridge root 统一不越过
moving barrier `P-gr`，要么把越界行命名为 PDEC。

最新口：

```text
BridgeRootMovingEndpointBarrierOrderLawOrPDEC
AND RightSelectedTerminalTailOverhangPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

### 6.17 terminal boundary bridge-root q-spine index-gap 更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_boundary_bridge_root_qspine_index_gap_router.py
data/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-index-gap-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-index-gap-router.md
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-index-gap-router.json
```

本层把 moving endpoint barrier 顺序继续离散化。由于 bridge roots 与 moving
barriers 都在同一条 q-spine

```text
577 -> 607 -> 631
```

上，endpoint slack 等于从 bridge index 到 barrier index 的相邻 q-gap 和。

有限审计读数：

```text
bridge_root_qspine_index_gap_reduction_closed=true
q_spine_gap_vector=[30, 24]
qspine_index_gaps=[2, 0]
endpoint_slack_equals_qspine_gap_sum_closed=true
finite_qspine_index_order_closed=true
zero_index_contact_count=1
row_column_unconditional_closed=false
```

两条 index-gap row 为：

```text
m757 q571->577: bridge index 0, barrier index 2, index gap 2, q-gap sum 30+24=54
m761 q601->607: bridge index 1, barrier index 1, index gap 0, q-gap sum 0
```

这一步的实际推进是：`BridgeRootMovingEndpointBarrierOrderLawOrPDEC` 被替换为
更离散的 `BridgeRootQSpineIndexBarrierOrderLawOrPDEC`。现在最新硬点不是一般
整数距离不等式，而是证明 bridge index 不超过 moving-barrier index，或把索引越界行
命名为 PDEC。

最新口：

```text
BridgeRootQSpineIndexBarrierOrderLawOrPDEC
AND RightSelectedTerminalTailOverhangPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

### 6.18 terminal boundary bridge-root q-spine pivot-enclosure 更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_boundary_bridge_root_qspine_pivot_enclosure_router.py
data/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-pivot-enclosure-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-pivot-enclosure-router.md
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-pivot-enclosure-router.json
```

本层把 q-spine index-gap 顺序继续压成 shared-pivot enclosure。共享 pivot 为

```text
shared_pivot_q=607
shared_pivot_index=1
```

有限审计读数：

```text
bridge_root_qspine_pivot_enclosure_reduction_closed=true
finite_pivot_enclosure_closed=true
endpoint_slack_equals_pivot_gap_sum_closed=true
exact_pivot_contact_count=1
row_column_unconditional_closed=false
```

两条 pivot-enclosure row 为：

```text
m757 q571->577: 577 <= 607 <= 631, left gap 30, right gap 24, slack 54
m761 q601->607: 607 = 607 = 607, left gap 0, right gap 0, slack 0
```

这一步的实际推进是：`BridgeRootQSpineIndexBarrierOrderLawOrPDEC` 被替换为
`BridgeRootQSpinePivotEnclosureLawOrPDEC`。最新硬点变成证明 shared pivot 总在
bridge root 与 moving barrier 之间，或把 pivot 越界行命名为 PDEC。

最新口：

```text
BridgeRootQSpinePivotEnclosureLawOrPDEC
AND RightSelectedTerminalTailOverhangPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

## 7. 审稿边界

```text
finite_ledgers_are_evidence_not_final_proof=true
actual_load_not_formal_envelope=true
support_only_is_parity_blind=true
external_theorem_requires_admissible_family=true
rankone_ap_positivity_direct_route_not_closed=true
```

本文件的作用是防止回到循环路线：它没有宣称完成任何三命题的无条件证明，而是把下一步真突破压成可验证的 signed-payload/trace-constructor 或 named-return 合同。

## 8. 外部前沿可用性同步（2026-05-25）

新增证书：

```text
experiments/prime_matrix_external_live_frontier_applicability_sync_20260525.py
data/prime-matrix-external-live-frontier-applicability-sync-20260525-ledger.json
docs/monograph/prime-matrix-external-live-frontier-applicability-sync-20260525.md
docs/monograph/prime-matrix-external-live-frontier-applicability-sync-20260525.json
```

本轮核对 Milićević--Qin--Wu、Wright、Runbo Li 与 Becker--Breuillard 四类
2025-2026 外部前沿输入后，路线选择没有改变：

```text
all_inputs_require_admissible_family_before_use=true
admissible_averaged_signed_trace_family_constructed=false
admissible_finite_group_orbit_family_constructed=false
pointwise_row_column_ap_positivity_imported=false
row_column_unconditional_closed=false
phi_lpf_parity_barrier_globally_broken=false
```

结论：这些输入是后续可调用的强工具，但不是当前有限 q-spine pivot/right-tail/
adjacent-run ledger 的替代证明。下一步仍应先构造
`SourceKeyLift/PrimitiveOrientationLocalFactorProduct`，或把失败回流为明确
PDEC/SAE/LocalSurvivor；得到 admissible averaged family 后再调用
trace/Kloosterman/Type-II/expander 输入。

## 9. right-tail overhang excess decomposition 更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_right_tail_overhang_excess_decomposition_router.py
data/prime-matrix-phi-lpf-right-tail-overhang-excess-decomposition-ledger.json
docs/monograph/prime-matrix-phi-lpf-right-tail-overhang-excess-decomposition-router.md
docs/monograph/prime-matrix-phi-lpf-right-tail-overhang-excess-decomposition-router.json
```

本层把唯一 `RightSelectedTerminalTailOverhangPDEC` 从匿名尾段压成 m773 的
final negative-run 剩余：

```text
negative_excess_equals_internal_plus_tail=true
tail_overhang_equals_excess_after_internal_return=true
internal_survivor_old_return_paid=true
final_run_tail_matches=true
right_tail_overhang_excess_decomposition_closed=true
row_column_unconditional_closed=false
```

精确恒等式为：

```text
m773 selected-terminal negative excess
  = internal survivor return + final negative tail overhang
  = 0.017995938314 + 0.831750175347
  = 0.849746113661.
```

其中 internal survivor 已由 old-side return alignment 支付；未支付对象因此不是
独立 residual pool，而是 `right:1887:selected_terminal:m773` 的最终负 run
`q=461->467`。最新口相应改写为：

```text
BridgeRootQSpinePivotEnclosureLawOrPDEC
AND RightSelectedTerminalFinalNegativeRunExcessPaymentOrPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

这仍不是无条件闭合；下一步必须证明 final negative-tail payment law，或把该最终
负 run 回流为命名 PDEC/LocalSurvivor。

## 10. final negative-run endpoint-collar 更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_right_tail_final_negative_run_endpoint_collar_router.py
data/prime-matrix-phi-lpf-right-tail-final-negative-run-endpoint-collar-ledger.json
docs/monograph/prime-matrix-phi-lpf-right-tail-final-negative-run-endpoint-collar-router.md
docs/monograph/prime-matrix-phi-lpf-right-tail-final-negative-run-endpoint-collar-router.json
```

本层把上一节的 final negative run 继续原子化。它不是任意 tail payment 门，而是
两步 terminal endpoint-collar wrap debt：

```text
q_path=[461,463,467]
A_path=[417,87,34]
D_path=[44,376,433]
phase words:
negative_Awrap1_Dwrap0_L1to1_gap2_carry2
negative_Awrap1_Dwrap0_L1to1_gap4_carry5
```

核心恒等式为：

```text
179065/215287 = 417/461 - 34/467 = 1 - 44/461 - 34/467.
```

中间相位 `87/463` 完全 telescoping 消去。因此最新非循环口进一步改写为：

```text
BridgeRootQSpinePivotEnclosureLawOrPDEC
AND TerminalDoubleAwrapEndpointCollarPaymentOrPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

这仍不是三命题无条件闭合。真正下一步是证明 terminal double-Awrap endpoint-collar
的 uniform payment/exclusion，或把这类 terminal collar 聚合成可调用
trace/Kloosterman/Type-II 或 finite-group orbit family。

## 11. terminal double-Awrap sibling q-spine kernel 更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_double_awrap_sibling_qspine_kernel_router.py
data/prime-matrix-phi-lpf-terminal-double-awrap-sibling-qspine-kernel-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-double-awrap-sibling-qspine-kernel-router.md
docs/monograph/prime-matrix-phi-lpf-terminal-double-awrap-sibling-qspine-kernel-router.json
```

本层把 m773 的 terminal double-Awrap endpoint collar 与同 packet 已支付 sibling
`m769` 对齐。两个 sibling 共享：

```text
q_path=[461,463,467]
phase words:
negative_Awrap1_Dwrap0_L1to1_gap2_carry2
negative_Awrap1_Dwrap0_L1to1_gap4_carry5
```

关键新恒等式为：

```text
179065/215287
= 123221/205013 + 36420/202379 + 10926/215287
= 607*(203/(439*467) + 60/(439*461) + 18/(461*467)).
```

其中 `123221/205013` 是已支付的 m769 sibling tail；`36420/202379` 是 m769
final collar 超出已支付 tail 的部分，等于 `10` 个 m773 internal survivor unit；
`10926/215287` 是 m773 相对 m769 的 endpoint offset，等于同分子 unit 的 `3`
倍。最新非循环口进一步改写为：

```text
BridgeRootQSpinePivotEnclosureLawOrPDEC
AND TerminalDoubleAwrapSiblingQSpineKernelPaymentOrPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

这仍不是无条件闭合；它把 terminal collar payment 从单点相位问题降到 P-scaled
q-spine 三分母 kernel 的 uniform payment/exclusion 或可平均族构造问题。

## 12. terminal sibling q-spine integer-balance 更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_sibling_qspine_integer_balance_router.py
data/prime-matrix-phi-lpf-terminal-sibling-qspine-integer-balance-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-sibling-qspine-integer-balance-router.md
docs/monograph/prime-matrix-phi-lpf-terminal-sibling-qspine-integer-balance-router.json
```

本层把上一节的 P-scaled q-spine 三分母 kernel 再压成一个整数守恒。right-side
q-spine 是 `[439,461,467]`，而 terminal double-Awrap 的本地路径仍是
`[461,463,467]`；两者不能与 bridge-root q-spine 混同。

关键新恒等式为：

```text
295/(461*467)
= 203/(439*467) + 60/(439*461) + 18/(461*467)

295*439 = 203*461 + 60*467 + 18*439 = 129505.
```

同一 endpoint collar 系数公式同时解释 sibling 与 target：

```text
coeff=(461*467 - D_start*467 - A_end*461)/607
m769: (461*467 - 21*467 - 81*461)/607 = 277
m773: (461*467 - 44*467 - 34*461)/607 = 295
offset: ((21-44)*467 + (81-34)*461)/607 = 18
```

最新非循环口进一步改写为：

```text
BridgeRootQSpinePivotEnclosureLawOrPDEC
AND TerminalSiblingQSpineIntegerBalancePaymentOrPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

这仍不是三命题的无条件闭合；它把 terminal payment 的剩余对象从有理三分母核
降到整数 balance 的 uniform payment/exclusion 或 PDEC。

## 13. terminal sibling q-spine gap-drift 更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_sibling_qspine_gap_drift_router.py
data/prime-matrix-phi-lpf-terminal-sibling-qspine-gap-drift-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-sibling-qspine-gap-drift-router.md
docs/monograph/prime-matrix-phi-lpf-terminal-sibling-qspine-gap-drift-router.json
```

本层把上一节的整数 balance 继续改写为 q-spine gap-drift 正规形。将
`461=439+22`、`467=439+28` 代入

```text
295*439 = 203*461 + 60*467 + 18*439
```

并把 offset 系数 `18` 并入左侧 defect，得到：

```text
(295-203-60-18)*439 = 22*203 + 28*60
14*439 = 22*203 + 28*60.
```

除以 gap 公因子 `2` 后是 primitive drift law：

```text
7*439 = 11*203 + 14*60.
```

再剥离 LPF-threshold 因子 `7`：

```text
203=7*29, 14=7*2,
439 = 11*29 + 2*60.
```

最新非循环口进一步改写为：

```text
BridgeRootQSpinePivotEnclosureLawOrPDEC
AND TerminalSiblingQSpinePrimitiveGapDriftPaymentOrPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

这仍不是三命题的无条件闭合；它把 terminal payment 的剩余对象从整数 balance
继续降到 primitive gap-drift 的 uniform payment/exclusion 或 PDEC。

## 14. terminal sibling q-spine 30-wheel residue-carrier 更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_sibling_qspine_wheel_residue_router.py
data/prime-matrix-phi-lpf-terminal-sibling-qspine-wheel-residue-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-sibling-qspine-wheel-residue-router.md
docs/monograph/prime-matrix-phi-lpf-terminal-sibling-qspine-wheel-residue-router.json
```

本层把上一节的 7-peeled primitive gap-drift 继续改写成 30-wheel residue
carrier：

```text
439 = 11*29 + 2*60
    = 11*29 + 4*30.
```

非 30-wheel 周期 residue 完全由 `11*29` 承载：

```text
439 mod 30 = 19
(11*29) mod 30 = 19.
```

而 lift height 正好由 right primitive gap after 7-peel 与 middle wheel units 给出：

```text
4 = 2*(60/30).
```

最新非循环口进一步改写为：

```text
BridgeRootQSpinePivotEnclosureLawOrPDEC
AND TerminalSiblingQSpineWheelResidueCarrierPaymentOrPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

这仍不是三命题的无条件闭合；它把 terminal payment 的剩余对象从 primitive
gap-drift 继续降到 30-wheel residue carrier 的 uniform payment/exclusion 或 PDEC。

## 15. terminal sibling q-spine wheel-gap-lock 更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_sibling_qspine_wheel_gap_lock_router.py
data/prime-matrix-phi-lpf-terminal-sibling-qspine-wheel-gap-lock-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-sibling-qspine-wheel-gap-lock-router.md
docs/monograph/prime-matrix-phi-lpf-terminal-sibling-qspine-wheel-gap-lock-router.json
```

本层把上一节的 30-wheel residue carrier 锁定到 terminal double-Awrap
q-gap/carry path。共同 terminal signature 为：

```text
terminal_q_gap_path=[2,4]
terminal_carry_path=[2,5]
```

关键 gap-lock 恒等式为：

```text
2 = middle_kernel/30 = right_gap_after_7_peel
4 = wheel_lift_height = 2^2
461-439 = 11*2
467-439 = 14*2 = 7*2*2
carry_path=[2,4+1]=[2,5]
```

最新非循环口进一步改写为：

```text
BridgeRootQSpinePivotEnclosureLawOrPDEC
AND TerminalSiblingQSpineWheelGapLockPaymentOrPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

这仍不是三命题的无条件闭合；它把 terminal payment 的剩余对象从
30-wheel residue carrier 继续降到 terminal wheel-gap-lock 的 uniform
payment/exclusion 或 PDEC。

## 16. affine odd Euler normalization 更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_affine_odd_euler_normalization_router.py
data/prime-matrix-phi-lpf-affine-odd-euler-normalization-ledger.json
docs/monograph/prime-matrix-phi-lpf-affine-odd-euler-normalization-router.md
docs/monograph/prime-matrix-phi-lpf-affine-odd-euler-normalization-router.json
```

本层回答 `m=2n+1` 仿射提升与有限欧拉乘积截断是否给出 `1/2` 主项误差的问题。
结论是否定的：对任意奇素数 `p`，

```text
m=0 mod p  iff  n=(p-1)/2 mod p.
```

因此 `m=2n+1` 给出奇素数零同余类与 `n` 轴仿射 forbidden class 的逐点双射。
长度为两倍的完整区间欧拉乘积主项满足

```text
2X*(1-1/2)*prod_{3<=p<=Y}(1-1/p)
  = X*prod_{3<=p<=Y}(1-1/p).
```

这里的因子二被 `p=2` 因子完全归一化，不是有限截断误差的 `1/2` 量级。
审计读数为：

```text
affine_forbidden_class_bijection_verified=true
finite_euler_product_full_with_p2_equals_affine_odd_main=true
finite_euler_product_half_error_claim_supported=false
p2_normalization_explains_factor_two=true
lpf_bucket_identity_verified=true
phi_lpf_iteration_route_closes_parity_barrier=false
row_column_unconditional_closed=false
```

LPF 侧同步为：

```text
n=kP+(P-1)/2
2n+1=P(2k+1)
k>=1 and LPF(2k+1)>=P  =>  LPF(2n+1)=P.
```

`k=0` 是端点素数例外：`2n+1=P`，仍有 LPF 为 `P`，但不是合数。

这条路的价值是校准 Phi 递推与 LPF 分桶，避免把 `p=2` 归一化误读成可支付误差；
它本身不提供 signed cofactor saving。最新非循环口因此不是“Euler product half-error”，
而是：

```text
AffineOddLiftOnlyNormalizesParityNoSignedSaving
AND TerminalSiblingQSpineWheelGapLockPaymentOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

## 17. affine endpoint LPF first-hit 更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_affine_endpoint_lpf_first_hit_router.py
data/prime-matrix-phi-lpf-affine-endpoint-lpf-first-hit-ledger.json
docs/monograph/prime-matrix-phi-lpf-affine-endpoint-lpf-first-hit-router.md
docs/monograph/prime-matrix-phi-lpf-affine-endpoint-lpf-first-hit-router.json
```

本层继续把 `2n+1` 仿射归一化接入从小到大剥离素因子的 LPF first-hit 递推。
对任意奇数 `m>=3`，令 `p=LPF(m)`。则第一次命中恰好分为两类：

```text
m=p           -> endpoint prime leak, k=0
m=p(2k+1)     -> composite LPF tail, k>=1
2n+1=p(2k+1)  -> n=kp+(p-1)/2
LPF(2k+1)>=p  -> LPF(2n+1)=p
```

有限审计读数：

```text
endpoint_prime_leak_separated=true
lpf_tail_composite_partition_closed=true
zero_class_duplicate_overcount_positive=true
cofactor_parity_mixture_present_in_tail=true
prime_extraction_from_lpf_tail_proved=false
signed_payload_or_von_mangoldt_weight_constructed=false
row_column_unconditional_closed=false
```

这一步真正推进了 `k=0` 端点问题：端点素数不再被误塞进合数尾，也不再被解释为
Euler product 的误差；它们是 first-hit 递推中的 prime leak 发射项。合数尾则是
`m=p(2k+1)` 的 LPF bucket。

同时，审计也确认所有零类命中不能直接相加：合数会被多个素因子重复命中，必须按
`LPF(m)` 分配。尾部仍含半素数层与更高合数层，因此仅靠 forbidden residue、Phi
递推和 LPF 计数仍不能完成 prime extraction。最新非循环口为：

```text
EndpointPrimeLeakSeparatedFromLPFTailButPrimeExtractionStillParityBlocked
AND TerminalSiblingQSpineWheelGapLockPaymentOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

## 18. affine LPF first-hit von Mangoldt lift 更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_affine_lpf_first_hit_von_mangoldt_lift_router.py
data/prime-matrix-phi-lpf-affine-lpf-first-hit-von-mangoldt-lift-ledger.json
docs/monograph/prime-matrix-phi-lpf-affine-lpf-first-hit-von-mangoldt-lift-router.md
docs/monograph/prime-matrix-phi-lpf-affine-lpf-first-hit-von-mangoldt-lift-router.json
```

本层把上一节的 LPF first-hit 分割接到 von Mangoldt 的 Möbius 反演恒等式：

```text
Lambda(m) = sum_{d|m} mu(d) log(m/d)
Lambda(m) = log p  if m=p^a
Lambda(m) = 0      otherwise
```

有限审计读数：

```text
mobius_von_mangoldt_identity_closed=true
lpf_first_hit_identity_imported_and_verified=true
tail_prime_power_leak_present=true
nonprimepower_tail_cancelled_only_by_mobius_divisor_sum=true
lpf_local_unsigned_count_sufficient_for_prime_extraction=false
global_divisor_signed_payload_required=true
admissible_typeii_or_trace_family_constructed=false
row_column_unconditional_closed=false
```

这一步给出真正有用的路线校正：若要从 `LPF(m)=p` 的合数尾抽出素数质量，
必须改用全局除子层的 signed payload。端点素数给出 `theta` 质量，尾部
prime powers 仍有小的 `Lambda` 泄漏，而非 prime powers 的消失依赖所有
Möbius 除子的符号抵消。于是仅从小到大剥离 LPF 因子、再做无符号桶计数，
仍无法跨过奇偶性障碍。

样本读数显示 prime-power 泄漏不是闭合主项：

| X | endpoint primes | composite tails | tail prime powers | tail non-prime-powers | tail prime-power Lambda fraction |
| --- | --- | --- | --- | --- | --- |
| 100 | 45 | 55 | 8 | 47 | 0.066686 |
| 1000 | 302 | 698 | 21 | 677 | 0.024339 |
| 10000 | 2261 | 7739 | 53 | 7686 | 0.008123 |
| 50000 | 9591 | 40409 | 93 | 40316 | 0.003556 |

外部前沿输入的作用也因此被精确重写：Milićević--Qin--Wu、Pascadi 与
almost-all short-interval `Lambda` 均不能直接作用于无符号 LPF tail；它们需要
先有 admissible signed divisor/Type-II/trace family，或者给出逐点
`theta` AP positivity at `P^2` 的替代定理。

最新非循环口为：

```text
VonMangoldtLiftRequiresGlobalDivisorSignedPayloadNotLPFLocalCount
AND PointwiseThetaAPPositivityAtP2OrAdmissibleSignedDivisorPayloadTypeIIFamily
AND TerminalSiblingQSpineWheelGapLockPaymentOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
```

## 37. parity barrier atom-cut frontier router

新增证书：

```text
experiments/prime_matrix_phi_lpf_parity_barrier_atom_cut_frontier_router.py
data/prime-matrix-phi-lpf-parity-barrier-atom-cut-frontier-ledger.json
docs/monograph/prime-matrix-phi-lpf-parity-barrier-atom-cut-frontier-router.md
docs/monograph/prime-matrix-phi-lpf-parity-barrier-atom-cut-frontier-router.json
```

本层把上一节“最小破障路线”的粗 signed transport 继续接入最新 atom-cut
前沿。LPF 精确计数修正保持不变：

```text
A_p(N)=Phi(floor(N/p); primes<p)
C_p(N)=Phi(floor(N/p); primes<p)-1
```

这修正了 `(N-p^2)*prod_{ell<=p}(1-1/ell)` 式的三个错误：计数变量应为
cofactor `a<=floor(N/p)`，cofactor 可以含有 `p`，而 floor/primorial 周期边界不能
被替换成普遍 half-main 误差。

审计读数：

```text
atom_cut_frontier_synced=true
legendre_periodic_boundary_not_half_main=true
unsigned_lpf_bucket_count_sufficient_for_prime_extraction=false
more_wheel_or_lpf_refinement_rejected_as_first_break=true
row_column_unconditional_closed=false
```

当前最快非循环硬点不再停在粗
`PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward`，而是同步为：

```text
PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward
PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward
PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
```

并行绕行仍只有：

```text
theta((kP,(k+1)P))>0
psi(I_{P,k})>PrimePowerTail(I_{P,k})
PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
admissible trace/Type-II family
named PDEC/SAE return
```

因此本步推进的是“奇偶性障碍从无符号 LPF 账本压到 signed atom 字段”的精确
定位，不是三命题无条件闭合。

## 38. parity barrier noncircular kernel sync router

新增证书：

```text
experiments/prime_matrix_phi_lpf_parity_barrier_noncircular_kernel_sync_router.py
data/prime-matrix-phi-lpf-parity-barrier-noncircular-kernel-sync-ledger.json
docs/monograph/prime-matrix-phi-lpf-parity-barrier-noncircular-kernel-sync-router.md
docs/monograph/prime-matrix-phi-lpf-parity-barrier-noncircular-kernel-sync-router.json
```

本层继续沿非循环路线把上一节 atom-cut 前沿向下同步。constructor edge signed fields
经同 trace key/命名 return 矩阵后，生产性出口只能是
`NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact`；该出口若不是 signed-lane
改名，又必须携带 source-rank/no-collapse 包，并先落到
`ActualPreCauchySourceDomainAbsoluteEntropyLedger`。继续展开会触发两类闭环：

```text
joint declaration -> built-in pairing -> new payload -> source entropy -> joint declaration
row-level table -> signed source spine -> row-level table
```

因此最新内部主攻不再是 atom 字段名；已有 support stripping 继续剥掉
noncircular kernel 的找行/容量部分，真正剩余是每个 LPF/Phi bucket 的 signed law：

```text
PhiLPFBucketSignedCoefficientLawBeforePushforward
AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
```

kernel 纪律仍由
`NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows`
表达：该 signed law 不能回读 row-level 表、source-entropy payload 环或 Phi/payment
下游结果。

并行 source-rank 路线同步为：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger
AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
```

审计读数：

```text
noncircular_kernel_sync_closed=true
lpf_phi_unsigned_scope_exhausted=true
noncircular_signed_emission_kernel_proved=false
phi_lpf_bucket_signed_coefficient_law_proved=false
alpha_row_anchor_phase_emission_formula_proved=false
external_trace_typeii_family_directly_attaches_now=false
row_column_unconditional_closed=false
```

外部最前沿输入的边界也同步收缩：Guth--Maynard、Runbo Li 等短区间输入仍未达到
每个 strict row 所需的 \(x^{1/2}\) 点态尺度；FKMS、Milićević--Qin--Wu、Wright、
Pascadi 等 trace/Type-II 工具仍需先由上述 bucket signed law/非循环 kernel 产生
source-keyed signed coefficient family。

## 39. parity barrier transport-edge sync router

新增证书：

```text
experiments/prime_matrix_phi_lpf_parity_barrier_transport_edge_sync_router.py
data/prime-matrix-phi-lpf-parity-barrier-transport-edge-sync-ledger.json
docs/monograph/prime-matrix-phi-lpf-parity-barrier-transport-edge-sync-router.md
docs/monograph/prime-matrix-phi-lpf-parity-barrier-transport-edge-sync-router.json
```

本层把上一节的 `PhiLPFBucketSignedCoefficientLawBeforePushforward` 继续接入既有
bucket transport stack。bucket signed law 若不直接提交逐点 signed 表，就必须给
rough-cofactor signed transport；该 transport 的 ordered factorization coherence、
unit/square-base 私有出口和 common packet 回环已由既有证书剥离，所以递推支路进一步
落到逐 edge signed multiplier 表。first-edge slab 前沿再把该表拆成两张边表：

```text
PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward
AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
```

继续接入 semiprime diagonal/offdiagonal、offdiagonal tuple-fields 与 pure-pair atom
证书后，diagonal `(p,p)` 被并回 source packet，offdiagonal 的 owner/first-q/tail/Phi
mass 无符号字段被剥离，`tail>1` 不再是新 first seed，而是 internal transition lift。
因此真正窄口继续收缩为：

```text
PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward
AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
```

LPF/Phi 继续能精确支付 `(p,q)` 的 q-rough continuation 纤维大小，但不能产生 signed
seed、orientation parity、ExactUV return、internal transition local factor、branch trace。
因此本轮把“从小到大精细剥离素因子”的可审稿硬点压到：

```text
chosen_primary_attack_target=PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward
paired_required_attack_target=PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
paired_orientation_attack_target=PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
paired_exactuv_attack_target=PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
parallel_source_rank=AlphaRowAnchorPhaseEmissionFormulaLedger
  AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
  AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
```

若不走这条递推 signed edge 表路线，剩余旁路仍是逐点 Phi-LPF signed value table、
完整 branch/atomic trace、same-set PDEC/SAE 回流、点态 `theta/psi` 平方根行输入或
外部 source-keyed trace/Type-II family。三命题仍未无条件闭合。

## 40. row Delta-Phi cover contract router

新增证书：

```text
experiments/prime_matrix_phi_lpf_row_delta_phi_cover_contract_router.py
data/prime-matrix-phi-lpf-row-delta-phi-cover-contract-ledger.json
docs/monograph/prime-matrix-phi-lpf-row-delta-phi-cover-contract-router.md
docs/monograph/prime-matrix-phi-lpf-row-delta-phi-cover-contract-router.json
```

本层专门处理“每行短区间计数是否就是两个前缀计数之差”。答案是肯定的，而且可以
写成完全精确的 LPF/Phi 恒等式。对整数区间 `(A,B]`：

```text
C_p(N)=0 if N<p^2, else Phi(floor(N/p); primes<p)-1
pi(A,B]=B-A-sum_{p<=sqrt(B)}(C_p(B)-C_p(A))
```

因此行内正性等价于严格覆盖缺口：

```text
sum_{p<=sqrt(B)}(C_p(B)-C_p(A)) <= B-A-1.
```

机器审计给出：

```text
row_delta_phi_identity_closed=true
row_delta_phi_prefix_difference_is_exact=true
strict_cover_inequality_proved_uniformly=false
row_delta_phi_positive_lower_bound_proved=false
row_column_unconditional_closed=false
```

该层的关键诚实边界是：覆盖缺口不等式与 `pi(A,B]>0` 等价，不能由恒等式本身推出。
例如 `(90,96]` 的 Delta-Phi 合数覆盖为 `6`、行长为 `6`、素数数为 `0`，前缀差公式
会精确给出零行，而不是自动排除零行。小 `P<=31` 的 Prime Matrix punctured rows
样本均为正，但这仍是有限证据。

最新非循环主攻改写为：

```text
UniformDeltaPhiCoverDefectOrNamedLPFOwnerResiduePDEC
OR PointwiseThetaPsiCOneInputAtSqrtRowScale
OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
OR SourceKeyedMobiusVonMangoldtTraceTypeIIFamily
```

## 41. row inequality breakthrough frontier router

新增证书：

```text
experiments/prime_matrix_phi_lpf_row_inequality_breakthrough_frontier_router.py
data/prime-matrix-phi-lpf-row-inequality-breakthrough-frontier-ledger.json
docs/monograph/prime-matrix-phi-lpf-row-inequality-breakthrough-frontier-router.md
docs/monograph/prime-matrix-phi-lpf-row-inequality-breakthrough-frontier-router.json
```

本层把上一节的行级 Delta-Phi 恒等式继续压成真正破障公式前沿。现在目标不是再
重写 `pi(A,B]`，而是证明下面四类之一：

```text
UniformDeltaPhiCoverDefect:
  sum_{p<=sqrt(B)}(C_p(B)-C_p(A)) <= B-A-1
NamedLPFOwnerResiduePDEC:
  Delta-Phi cover equality => forbidden LPF-owner residue/phase packet
PointwiseThetaPsiCOneInputAtSqrtRowScale:
  theta(B)-theta(A)>0, or psi(B)-psi(A)>PrimePowerTail(A,B)
SourceKeyedMobiusVonMangoldtTraceTypeIIFamily:
  signed divisor/trace/Type-II error < row main term
```

尺度换算固定为：

```text
x=P^2
row_length=P=x^(1/2)
expected_prime_count=P/(2 log P)
```

因此外部短区间定理若只有 `theta>1/2`，在当前行尺度上仍是加厚行结果。
Guth--Maynard 与 Hieu 的 `theta=17/30` 给出约 `P^(2/15)` 行厚度，Runbo Li
的 `theta=13/25` 仍有 `P^(1/25)` 行厚度，不能直接闭合每一固定行。

机器审计给出：

```text
breakthrough_formula_frontier_synced=true
strict_cover_inequality_proved_uniformly=false
row_column_unconditional_closed=false
```

最新非循环主攻因此固定为：

```text
UniformDeltaPhiCoverDefectOrNamedLPFOwnerResiduePDEC
OR PointwiseThetaPsiCOneInputAtSqrtRowScale
OR SourceKeyedMobiusVonMangoldtTraceTypeIIFamily
OR SpectralKloostermanTraceLift
```

## 42. row inequality target residue-cover router

新增证书：

```text
experiments/prime_matrix_phi_lpf_row_inequality_target_residue_cover_router.py
data/prime-matrix-phi-lpf-row-inequality-target-residue-cover-ledger.json
docs/monograph/prime-matrix-phi-lpf-row-inequality-target-residue-cover-router.md
docs/monograph/prime-matrix-phi-lpf-row-inequality-target-residue-cover-router.json
```

本层把上一节的抽象行级严格不等式继续压成目标行 residue-cover 标准形，并排除一个
会循环的错误推广：该不等式不能作为任意短区间命题。普通短区间已有 full-cover 等号：

```text
(90,96]:  length=6,  Delta-Phi cover=6,  primes=0
(114,126]: length=12, Delta-Phi cover=12, primes=0
(200,210]: length=10, Delta-Phi cover=10, primes=0
```

因此真正目标必须保持为 Prime Matrix punctured 行

```text
R_{P,k}={kP+r:1<=r<=P-1}, 1<=k<=P-1.
```

在该行上，每个 `p<P` 给出一个确定 residue fiber：

```text
D_p(P,k)={r: 1<=r<=P-1, r == -kP mod p}
O_p(P,k)=D_p(P,k) minus union_{q<p}D_q(P,k)
```

行级失败态等价于

```text
union_{p<=sqrt((k+1)P-1)} D_p(P,k) = [1,P-1].
```

有限扫描 `P=31,101,251,499,1009` 的全部 punctured 行未见 full-cover；最小素数数分别为
`2,7,18,29,52`。这只是定位结构，不作为证明。

机器审计给出：

```text
target_row_residue_cover_standard_form_synced=true
generic_interval_uniform_defect_false=true
target_punctured_row_full_cover_found_in_scan=false
strict_cover_inequality_proved_uniformly=false
row_column_unconditional_closed=false
```

最新非循环主攻收窄为：

```text
FullCoverOwnerResiduePDEC
OR MobiusResidueCoverSignedTrace
OR SpectralKloostermanResidueLift
```

## 43. full-cover owner PDEC stress router

新增证书：

```text
experiments/prime_matrix_phi_lpf_full_cover_owner_pdec_stress_router.py
data/prime-matrix-phi-lpf-full-cover-owner-pdec-stress-ledger.json
docs/monograph/prime-matrix-phi-lpf-full-cover-owner-pdec-stress-router.md
docs/monograph/prime-matrix-phi-lpf-full-cover-owner-pdec-stress-router.json
```

本层直接攻击上一节选择的 `FullCoverOwnerResiduePDEC`，结论是：只依赖 LPF owner 分桶、
owner fibers 互不相交、一素数一同余类、Euler/wheel 容量等普通支撑性质的 PDEC
会被普通 full-cover 短区间反例排除。例如：

```text
(90,96], (114,126], (200,210]
```

这些区间均为零素数 full-cover，并且同样满足 owner 分桶、互不相交和一素数一同余类。
因此 naive owner-only PDEC 已经被压力测试否定。

目标行有限扫描扩展到：

```text
P=31,101,251,499,1009,2003,5003
```

未见 full-cover；最小素数数分别为：

```text
2, 7, 18, 29, 52, 113, 260
```

这仍只是证据，不是证明。真正还能非循环的 PDEC 必须同时使用：

```text
target_affine_anchor: A=kP, length=P-1, P prime, 1<=k<=P-1
global_residue_coupling: a_p=-kP mod p
owner_minimality: O_p=D_p minus union_{q<p}D_q
signed_or_phase_payload: Mobius/Von Mangoldt/trace/CRT phase before pushforward
```

机器审计给出：

```text
full_cover_owner_pdec_stress_synced=true
owner_only_pdec_rejected=true
target_affine_owner_pdec_proved=false
target_scan_no_full_cover=true
row_column_unconditional_closed=false
```

最新非循环主攻收窄为：

```text
TargetAffineFullCoverOwnerResiduePDEC
OR MobiusResidueCoverSignedTraceWithTargetAffineAnchor
OR SpectralKloostermanResidueLiftWithSourceKeys
```

## 44. target-affine gap equivalence router

新增证书：

```text
experiments/prime_matrix_phi_lpf_target_affine_gap_equivalence_router.py
data/prime-matrix-phi-lpf-target-affine-gap-equivalence-ledger.json
docs/monograph/prime-matrix-phi-lpf-target-affine-gap-equivalence-router.md
docs/monograph/prime-matrix-phi-lpf-target-affine-gap-equivalence-router.json
```

本层继续攻击上一节剩余的 target-affine 口。结论是：目标仿射锚
`A=kP,length=P-1` 是必要字段，但它本身不产生 PDEC；它把 full-cover 等号精确改写为
目标行无素数，即一个 prime gap 覆盖整行：

```text
union_{p<=sqrt((k+1)P-1)}D_p(P,k)=[1,P-1]
<=> pi(kP,(k+1)P)=0
```

最坏 `k≈P` 时这是 `x≈P^2,H≈sqrt(x)` 的 `C=1` 点态短区间问题；top row
`k=P-1` 正是 prime-indexed Oppermann-left 半窗。Baker-Harman-Pintz `21/40`、
Guth-Maynard `17/30`、Runbo Li `13/25` 在 `x=P^2` 分别仍厚出
`P^(1/20),P^(2/15),P^(1/25)` 行，因此不能直接支付单行正性。

机器审计给出：

```text
target_affine_gap_equivalence_synced=true
owner_only_pdec_rejected_imported=true
target_affine_anchor_alone_closes=false
target_affine_owner_pdec_proved=false
row_column_unconditional_closed=false
```

最新非循环主攻收窄为：

```text
TargetAffineSignedPhasePayload
OR PointwiseSqrtPrimeInputCOne
OR SpectralKloostermanResidueLiftWithSourceKeys
```

## 45. target-affine signed phase contract router

新增证书：

```text
experiments/prime_matrix_phi_lpf_target_affine_signed_phase_contract_router.py
data/prime-matrix-phi-lpf-target-affine-signed-phase-contract-ledger.json
docs/monograph/prime-matrix-phi-lpf-target-affine-signed-phase-contract-router.md
docs/monograph/prime-matrix-phi-lpf-target-affine-signed-phase-contract-router.json
```

本层继续拆上一节的 `TargetAffineSignedPhasePayload`。核心结论：target-affine 的第一层
phase 恒等式确实闭合，但它只是等价检测，不是非循环正性。对任意 \(h\bmod P\)，有：

```text
row indicator = LPF owner composite indicator + prime survivor indicator
```

所以 row Fourier defect 精确等于 prime survivor Fourier transform。有限审计中
`P=31,101,251,499,1009,2003,5003` 的最小素数行均满足 owner/prime partition 和 Parseval
恒等式，最大非零 Fourier 幅度为：

```text
1.9897, 5.2476, 12.8124, 18.4850, 34.1045, 73.7658, 170.9404
```

这说明 phase 可以检测 survivor；但要给出非零/正下界仍等价于证明行内有素数。只使用
`a_p=-kP mod p` 或 offset Fourier 相位会回到 full-cover/prime-gap 等价式；直接引入
`Lambda/Mobius` 行负载则变成 `theta/psi` 点态短区间输入。

机器审计给出：

```text
target_affine_signed_phase_contract_synced=true
row_fourier_defect_identity_closed=true
row_fourier_positive_lower_bound_proved=false
source_keyed_owner_phase_emission_formula_proved=false
completed_trace_kloosterman_family_from_owner_fibers_proved=false
row_column_unconditional_closed=false
```

最新非循环主攻收窄为：

```text
SourceKeyedOwnerPhaseEmissionFormula
OR PointwiseSqrtPrimeInputCOne
OR CompletedTraceKloostermanFamilyFromOwnerFibers
```

## 46. target-affine source-keyed product phase router

新增证书：

```text
experiments/prime_matrix_phi_lpf_target_affine_source_keyed_product_phase_router.py
data/prime-matrix-phi-lpf-target-affine-source-keyed-product-phase-ledger.json
docs/monograph/prime-matrix-phi-lpf-target-affine-source-keyed-product-phase-router.md
docs/monograph/prime-matrix-phi-lpf-target-affine-source-keyed-product-phase-router.json
```

本层把上一节的抽象 `SourceKeyedOwnerPhaseEmissionFormula` 具体闭合为显式 product-window
相位恒等式。对每个 LPF owner 元素：

```text
n=pm=kP+r
```

有：

```text
r == pm (mod P)
e_P(h r)=e_P(h p m)
```

其中 `p=LPF(n)`，`m` 为 `p`-rough，且 `kP<pm<(k+1)P`。有限审计对
`P=31,101,251,499,1009,2003,5003` 的目标行全部验证：

```text
source_keyed_product_phase_congruence_ok=true
rough_cofactor_condition_ok=true
product_window_condition_ok=true
selected_frequency_phase_error=0
```

这是真推进：source key 从形式名词变成了 `(p,m)` product phase。但它仍只是恒等式。
若 full-cover 成立，owner product residues 正好成为 `F_P^*` 的排列，所有非零频率和为
`-1`。因此非循环突破现在被压成：

```text
ProductWindowBilinearAdditivePhaseSavingOrPDEC
OR ProductWindowToCompletedKloostermanOrTraceBridge
OR PointwiseSqrtPrimeInputCOne
```

## 47. product-window additive saving firewall router

新增证书：

```text
experiments/prime_matrix_phi_lpf_product_window_additive_saving_firewall_router.py
data/prime-matrix-phi-lpf-product-window-additive-saving-firewall-ledger.json
docs/monograph/prime-matrix-phi-lpf-product-window-additive-saving-firewall-router.md
docs/monograph/prime-matrix-phi-lpf-product-window-additive-saving-firewall-router.json
```

本层把上一节的 product-window 硬点再压缩一步：普通 additive saving 不是可闭合主门。
理由是 full-cover 自身已经具有极小的非零频率指纹：

```text
sum_{r in F_P^*} e_P(hr) = -1  for every h!=0.
```

所以任何 `|S_h|<=B(P)` 且 `B(P)>=1` 的上界都不能排除 full-cover。有限审计只核验
恒等式：

```text
complete_nonzero_residue_fourier_fingerprint_closed=true
finite_complete_measure_identity_all_ok=true
ordinary_product_window_additive_saving_rejected_as_primary_gate=true
```

外部前沿压力测试同步显示：Guth--Maynard `17/30` 短区间、Hieu 的 `theta>17/30`
输入、Pascadi 复合模 Kloosterman Type-II、Shao--Shparlinski--Wijaya smooth/square-free
Kloosterman 求和都不能直接闭合本行；它们必须先接入带 signed defect 的 completed
trace/Kloosterman family，或改由点态 `C=1` sqrt 素数输入。

最新非循环口：

```text
ProductWindowExactCoefficientSeparationOrSubunitFourierContradictionOrPDEC
OR ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefect
OR PointwiseSqrtPrimeInputCOne
```

## 48. product-window exact separation equivalence router

新增证书：

```text
experiments/prime_matrix_phi_lpf_product_window_exact_separation_equivalence_router.py
data/prime-matrix-phi-lpf-product-window-exact-separation-equivalence-ledger.json
docs/monograph/prime-matrix-phi-lpf-product-window-exact-separation-equivalence-router.md
docs/monograph/prime-matrix-phi-lpf-product-window-exact-separation-equivalence-router.json
```

本层把 `exact coefficient separation/subunit Fourier contradiction` 再压缩为等价边界。
记 `s` 为目标行 prime survivor 数，owner 测度与完整非零剩余类测度之差就是负
survivor 测度，因此

```text
sum_{h=1}^{P-1} |defect_hat(h)|^2 = P*s-s^2.
```

所以 standalone exact separation、非 `-1` Fourier 指纹、subunit contradiction 都不是
独立证明；没有 pushforward 前的 signed defect emission 时，它们与“行内有素数”
完全等价。

最新非循环口：

```text
IndependentSignedDefectEmissionBeforeProductWindowPushforward
OR ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefectAndAdmissibleCoefficients
OR PointwiseSqrtPrimeInputCOne
OR NonTautologicalProductWindowPDEC
```

## 48A. product-window independent signed defect source router

新增证书：

```text
experiments/prime_matrix_phi_lpf_product_window_independent_signed_defect_source_router.py
data/prime-matrix-phi-lpf-product-window-independent-signed-defect-source-ledger.json
docs/monograph/prime-matrix-phi-lpf-product-window-independent-signed-defect-source-router.md
docs/monograph/prime-matrix-phi-lpf-product-window-independent-signed-defect-source-router.json
```

本层把上一节留下的抽象 `IndependentSignedDefectEmissionBeforeProductWindowPushforward`
继续压到可审计对象：独立 signed defect 不能由 survivor 后验定义，也不能由无符号
LPF/Phi support、owner 分桶、rough cofactor split 或 product phase identity 自动发射。
若不走点态平方根级素数输入或非平凡 PDEC，则必须提交真正的
`PhiLPFBucketSignedCoefficientLawBeforePushforward`。

所需 payload 字段是：

```text
owner_key
signed_coefficient
local_factor
orientation_and_branch
source_identity
pushforward_identity
admissible_norms
return_tag
```

最新非循环口：

```text
PhiLPFBucketSignedCoefficientLawBeforePushforward
OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
OR PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward
OR ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefectAndAdmissibleCoefficients
OR NonTautologicalProductWindowPDEC
OR PointwiseSqrtPrimeInputCOne
```

## 49. minimal parity-breaker route-forcing router

新增证书：

```text
experiments/prime_matrix_phi_lpf_minimal_parity_breaker_route_forcing_router.py
data/prime-matrix-phi-lpf-minimal-parity-breaker-route-forcing-ledger.json
docs/monograph/prime-matrix-phi-lpf-minimal-parity-breaker-route-forcing-router.md
docs/monograph/prime-matrix-phi-lpf-minimal-parity-breaker-route-forcing-router.json
```

本层把 parity-barrier contract 继续推进为“最小破障路线强制”：若要真正闭合三命题之一，
不能再把 LPF/Phi 支撑精细化当作突破。可破障对象被压成四类：

```text
Pointwise theta/gap:
  theta((kP,(k+1)P))>0, equivalently h(kP)<P
Pointwise psi:
  psi(I_{P,k})>PrimePowerTail(I_{P,k})
Internal signed transport:
  a_p(q*m) transport law before pushforward
Trace/Type-II/PDEC:
  source-keyed signed family or controlled contradiction return
```

证书读数：

```text
minimal_route_forcing_closed=true
more_wheel_or_lpf_refinement_rejected_as_first_break=true
chosen_next_primary_attack_target=PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward
chosen_parallel_attack_target=PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
row_column_unconditional_closed=false
```

因此最快非循环突破口不再是“继续升级 210/2310/... wheel”，而是把从小到大剥离素因子的
LPF cofactor multiplication 写成推前前 signed 传输律；外部 FKMS/MQW/Wright/Pascadi
等工具必须等该 signed family 或等价 trace family 构造完成后才能实际接入。

## 19. LPF bucket count formula 更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_lpf_bucket_count_formula_audit.py
data/prime-matrix-phi-lpf-lpf-bucket-count-formula-ledger.json
docs/monograph/prime-matrix-phi-lpf-lpf-bucket-count-formula-audit.md
docs/monograph/prime-matrix-phi-lpf-lpf-bucket-count-formula-audit.json
```

本层严格审计如下草式：

```text
LPF(P) = (N-P^2) * prod_{q<=P} 1/q.
```

结论：`N-P^2` 的截断方向抓到了 composite bucket 的起点，但密度因子写错。
精确 composite LPF bucket 是 Legendre-Phi 粗数计数：

```text
C_p(N) = #{n<=N composite : LPF(n)=p}
       = Phi(floor(N/p); primes<p)-1.
```

正确连续主项是：

```text
(N/p-p) * prod_{q<p}(1-1/q)
  = (N-p^2)/p * prod_{q<p}(1-1/q).
```

这里 `-1` 去掉端点素数 `n=p`。对每个小素数 `q<p`，应当保留所有非零同余类，
密度是 `1-1/q`，不是只保留一个同余类的 `1/q`。因此用户草式在 `p=2,3`
因低阶偶然相同，从 `p=5` 起系统性低估。

有限审计读数：

```text
exact_lpf_bucket_identity_closed=true
user_reciprocal_density_formula_supported=false
unsigned_lpf_bucket_count_sufficient_for_prime_extraction=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
```

样本总量：

| N | exact LPF total | composite count | corrected total/exact | user total/exact |
| --- | --- | --- | --- | --- |
| 100 | 74 | 74 | 0.947426 | 0.890669 |
| 1000 | 831 | 831 | 0.980306 | 0.843087 |
| 10000 | 8770 | 8770 | 0.985832 | 0.803612 |
| 100000 | 90407 | 90407 | 0.988315 | 0.780010 |

这一步的作用是把 LPF 分桶计数从“全 reciprocal product”纠正为精确
Legendre-Phi 递推。它不产生 signed saving；因此它与上一节的结论相合：
无符号 LPF bucket 身份闭合，但 prime extraction 仍必须走 von Mangoldt/Möbius
signed divisor payload、Type-II/trace family 或点态 `theta` AP 正性。

最新非循环口为：

```text
ExactLPFBucketCountIsLegendrePhiNotReciprocalDensity
AND UnsignedLPFBucketCountStillParityBlind
AND VonMangoldtLiftRequiresGlobalDivisorSignedPayloadNotLPFLocalCount
AND PointwiseThetaAPPositivityAtP2OrAdmissibleSignedDivisorPayloadTypeIIFamily
```

## 20. LPF bucket inclusive survival formula 更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_lpf_bucket_inclusive_survival_formula_audit.py
data/prime-matrix-phi-lpf-lpf-bucket-inclusive-survival-formula-ledger.json
docs/monograph/prime-matrix-phi-lpf-lpf-bucket-inclusive-survival-formula-audit.md
docs/monograph/prime-matrix-phi-lpf-lpf-bucket-inclusive-survival-formula-audit.json
```

本层审计用户修正后的草式：

```text
LPF(P) = (N-P^2) * prod_{q<=P}(1-1/q).
```

结论：这一步已经把上一版中 `q<P` 的小素数生存密度改对，但 `P` 自身不能按
`1-1/P` 处理。对 `LPF(n)=P` 的 bucket，`n` 必须满足

```text
n = 0 mod P,
```

所以 `P` 这一层是一个指定零类，密度为 `1/P`。小素数 `q<P` 才是避开零类，
密度为 `1-1/q`。因此正确的 n 轴连续主项为：

```text
(N-P^2) * (1/P) * prod_{q<P}(1-1/q).
```

精确式仍是：

```text
C_P(N)=Phi(floor(N/P); primes<P)-1.
```

用户修正版与正确 n 轴主项相差因子：

```text
P*(1-1/P)=P-1.
```

所以只在 `P=2` 偶然相同，从 `P=3` 起系统性高估。

有限审计读数：

```text
exact_lpf_bucket_identity_closed=true
inclusive_survival_formula_supported=false
unsigned_lpf_bucket_count_sufficient_for_prime_extraction=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
```

样本总量：

| N | exact LPF total | composite count | correct total/exact | user total/exact |
| --- | --- | --- | --- | --- |
| 100 | 74 | 74 | 0.947426 | 1.486358 |
| 1000 | 831 | 831 | 0.980306 | 2.398928 |
| 10000 | 8770 | 8770 | 0.985832 | 4.047312 |
| 100000 | 90407 | 90407 | 0.988315 | 7.385319 |

这把 LPF 分桶的局部密度口径完全固定：`q<P` 是 survival classes，`P`
是 divisibility owner class。该修正仍不提供 signed saving；无符号分桶只能告诉我们
合数由唯一最小素因子拥有，不能从 bucket 中抽出素数质量。

最新非循环口为：

```text
PrimeDivisibilityClassIsOneOverPNotOneMinusOneOverP
AND ExactLPFBucketCountIsLegendrePhiNotInclusiveSurvivalProduct
AND UnsignedLPFBucketCountStillParityBlind
AND VonMangoldtLiftRequiresGlobalDivisorSignedPayloadNotLPFLocalCount
```

## 21. Legendre-Phi periodic truncation error 更新

新增证书：

```text
experiments/prime_matrix_phi_lpf_legendre_phi_periodic_truncation_error_audit.py
data/prime-matrix-phi-lpf-legendre-phi-periodic-truncation-error-ledger.json
docs/monograph/prime-matrix-phi-lpf-legendre-phi-periodic-truncation-error-audit.md
docs/monograph/prime-matrix-phi-lpf-legendre-phi-periodic-truncation-error-audit.json
```

本层把“有限欧拉乘积截断误差是否为半主项”的问题改写为精确周期公式。设

```text
W_<p = prod_{q<p} q.
```

则

```text
Phi(x; primes<p)=floor(x/W_<p)*phi(W_<p)+R_p(x mod W_<p).
```

因此 composite LPF bucket 的端点修正式为：

```text
C_p(N)=Phi(floor(N/p); primes<p)-Phi(p-1; primes<p)
      =(floor(N/p)-p+1)*phi(W_<p)/W_<p
       + B_p(floor(N/p))-B_p(p-1),
|B_p(t)| <= phi(W_<p).
```

结论：截断误差是 primorial 周期余数边界项，不是普遍 `1/2 main`。这进一步修正
前几轮的密度口径：`p=2` 归一化、owner-prime divisibility class 与端点 `Phi(p-1)`
都必须同时保留。

有限审计读数：

```text
legendre_phi_periodic_truncation_error_closed=true
exact_lpf_bucket_identity_closed=true
half_main_truncation_error_claim_supported=false
truncation_error_is_periodic_residue_boundary=true
unsigned_lpf_bucket_count_sufficient_for_prime_extraction=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
```

同步外部前沿：Milićević--Qin--Wu Kloosterman 双线性、Zheng simultaneous AP、
Runbo Li 大模数 AP/Harman、Wright 三线性 Kloosterman fractions 与
Becker--Breuillard 谱间隙/反集中均仍需先构造 admissible signed trace/Type-II
或 finite-group orbit family。它们不能直接把周期边界误差变成素数抽取。

最新非循环口为：

```text
LegendrePhiTruncationErrorIsPeriodicBoundaryNotHalfMain
AND UnsignedLPFBucketCountStillParityBlind
AND VonMangoldtLiftRequiresGlobalDivisorSignedPayloadNotLPFLocalCount
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

## 22. LPF exact bucket endpoint equivalence 修正

新增证书：

```text
experiments/prime_matrix_phi_lpf_exact_bucket_endpoint_equivalence_audit.py
data/prime-matrix-phi-lpf-exact-bucket-endpoint-equivalence-ledger.json
docs/monograph/prime-matrix-phi-lpf-exact-bucket-endpoint-equivalence-audit.md
docs/monograph/prime-matrix-phi-lpf-exact-bucket-endpoint-equivalence-audit.json
```

本层修正 LPF 精确计数公式中最容易混淆的端点口径。对 `p<=sqrt(N)`：

```text
C_p(N)=Phi(floor(N/p); primes<p)-1
      =Phi(floor(N/p); primes<p)-Phi(p-1; primes<p),
Phi(p-1; primes<p)=1.
```

因此 `-1` 与 `-Phi(p-1)` 没有冲突；它们是同一个 endpoint singleton。
真正错误的读法是把连续 Euler 主项当成精确计数：

```text
(N-p^2)*(1/p)*prod_{q<p}(1-1/q)
```

它只是连续主项，不含 `floor(N/p)`、端点 singleton 和 primorial 周期边界项。

有限审计读数：

```text
exact_endpoint_singleton_fixed=true
minus_one_and_endpoint_forms_equivalent=true
exact_lpf_bucket_identity_closed=true
continuous_euler_main_is_exact_count=false
floor_endpoint_and_periodic_boundary_required=true
unsigned_lpf_bucket_count_sufficient_for_prime_extraction=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
```

最新非循环口为：

```text
ExactLPFBucketEndpointSingletonFixed
AND FloorEndpointAndPeriodicBoundaryRetained
AND ContinuousEulerMainNotExactCount
AND UnsignedLPFBucketCountStillParityBlind
AND VonMangoldtLiftRequiresGlobalDivisorSignedPayloadNotLPFLocalCount
```

## 23. LPF von Mangoldt pure-power compression 修正

新增证书：

```text
experiments/prime_matrix_phi_lpf_von_mangoldt_pure_power_compression_audit.py
data/prime-matrix-phi-lpf-von-mangoldt-pure-power-compression-ledger.json
docs/monograph/prime-matrix-phi-lpf-von-mangoldt-pure-power-compression-audit.md
docs/monograph/prime-matrix-phi-lpf-von-mangoldt-pure-power-compression-audit.json
```

本层修正 `LPF -> Lambda` lift 的精确口径。标准线性形式仍是：

```text
Lambda(m)=sum_{d|m} mu(d) log(m/d)
```

但点态身份可由 LPF 剥离压缩为：

```text
Lambda(m)=log(LPF(m)) if m is a power of LPF(m), else 0.
```

因此，“von Mangoldt lift 必须使用全局 Mobius divisor signed payload”只应理解为
“若要接入平均定理，仍需可线性化的 signed distribution family”；作为点态恒等式，
LPF 纯素幂选择器已经足够。真正仍未突破的是：该选择器是非线性 factorization
predicate，不是 Type-II、trace/Kloosterman、simultaneous AP 或 finite-group orbit
可直接调用的加性有符号族。

有限审计读数：

```text
lpf_pure_power_compression_closed=true
lambda_mass_reconstructed_from_endpoint_plus_prime_power_tail=true
mixed_composites_cancel_to_zero_pointwise=true
prime_power_tail_separated=true
pure_power_selector_supplies_additive_signed_distribution_family=false
pointwise_ap_theta_lower_bound_proved=false
admissible_typeii_or_trace_family_constructed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
```

外部前沿的重新定位：

- Milićević--Qin--Wu、Pascadi、Wright 的 Kloosterman/Type-II 工具需要先构造双线性或三线性 trace family；
- Zheng simultaneous AP 与 Runbo Li 大模数 AP/Harman 是平均型输入，不能替代 `x=P^2` 每行点态 `theta` 正性；
- Becker--Breuillard 谱间隙/反集中需要 finite-group orbit；
- Matomäki--Radziwiłł--Shao--Tao--Teräväinen almost-all short-interval uniformity 不是每个 row/residue 的点态定理。

最新非循环口为：

```text
LPFPurePowerVonMangoldtCompressionClosed
AND PrimePowerTailSeparated
AND PurePowerSelectorNotAnAdditiveSignedDistributionFamily
AND PointwiseAPThetaLowerBoundOrAdmissibleSignedTypeIIFamilyStillOpen
```

## 24. LPF prime-power tail absorption 修正

新增证书：

```text
experiments/prime_matrix_phi_lpf_prime_power_tail_absorption_audit.py
data/prime-matrix-phi-lpf-prime-power-tail-absorption-ledger.json
docs/monograph/prime-matrix-phi-lpf-prime-power-tail-absorption-audit.md
docs/monograph/prime-matrix-phi-lpf-prime-power-tail-absorption-audit.json
```

本层把上一节的点态 `Lambda` 压缩继续推进到 Prime Matrix strict row。对

```text
I_{P,k}=(kP,(k+1)P),  kP<n<(k+1)P
```

有：

```text
psi(I_{P,k})=theta(I_{P,k})+sum_{p^a in I_{P,k}, a>=2}log p.
```

因此行内素数存在性可替换为素幂尾巴吸收阈值：

```text
theta(I_{P,k})>0 iff psi(I_{P,k})>prime_power_tail(I_{P,k}).
```

尾巴有确定性整数根上界：

```text
prime_power_tail(I_{P,k})
 <= log(P)*sum_{a>=2}(floor(((k+1)P-1)^(1/a))-floor((kP)^(1/a))).
```

有限审计 `P=31,101,251,1009` 逐行确认：

```text
psi_theta_tail_identity_all_samples=true
prime_power_tail_bound_all_samples=true
psi_tail_absorption_equivalent_to_prime_presence_all_samples=true
prime_power_tail_absorption_threshold_closed=true
pointwise_psi_row_lower_bound_beyond_tail_proved=false
pointwise_theta_ap_lower_bound_proved=false
admissible_signed_typeii_or_trace_family_constructed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
```

最大样本 `P=1009` 中，最大合数素幂尾巴出现在 `k=1`，尾巴质量为 `14.176733`，
整数根上界为 `124.500870`；同一行实际 `theta` 质量为 `999.495375`。这些有限数据
说明尾巴不是主障碍，但证明仍需要逐行 `psi` 下界超过该尾巴，或构造可平均的 signed
Type-II/trace family。

最新非循环口为：

```text
LPFPurePowerVonMangoldtCompressionClosed
AND PrimePowerTailAbsorptionThresholdClosed
AND NeedPointwisePsiRowLowerBoundBeyondPrimePowerTail
AND PointwiseAPThetaLowerBoundOrAdmissibleSignedTypeIIFamilyStillOpen
```

## 25. LPF prime-power tail sublinear threshold 修正

新增证书：

```text
experiments/prime_matrix_phi_lpf_prime_power_tail_sublinear_threshold_audit.py
data/prime-matrix-phi-lpf-prime-power-tail-sublinear-threshold-ledger.json
docs/monograph/prime-matrix-phi-lpf-prime-power-tail-sublinear-threshold-audit.md
docs/monograph/prime-matrix-phi-lpf-prime-power-tail-sublinear-threshold-audit.json
```

本层继续修正 LPF 精确计数和 `Lambda` lift 的剩余误差口径：合数素幂尾巴不是半主项，
也不是新的奇偶性来源，而是 strict row 长度 `P` 的次线性阈值。

```text
prime_power_tail(I_{P,k})
 <= log(P)*((sqrt(2)-1)*sqrt(P)+1
    +(floor(log2(P^2-1))-2)*((2^(1/3)-1)*P^(1/3)+1))
 = O(sqrt(P)*log(P)+P^(1/3)*log(P)^2)=o(P).
```

有限审计 `P=31,101,251,1009,3001,10007` 逐行确认：

```text
actual_tail_bound_all_samples=true
sublinear_tail_bound_all_samples=true
prime_power_tail_sublinear_threshold_closed=true
positive_proportion_psi_would_close_rows_eventually=true
known_short_interval_input_reaches_sqrt_window=false
pointwise_psi_row_positive_proportion_proved=false
admissible_signed_typeii_or_trace_family_constructed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
```

最大样本 `P=10007` 的最大合数素幂尾巴仍在 `k=1`，尾巴质量为 `53.795750`，
即 `0.005376P`；统一次线性上界为 `0.184886P`。解析趋势显示该上界比例随 `P`
下降到 `0`。因此真正剩余的不是尾巴大小，而是逐行 `psi` 正比例下界：

```text
psi(I_{P,k}) >= eta*P  (eta>0 fixed)
```

一旦有这个输入，素幂尾巴可被自动吸收，`theta(I_{P,k})>0` 随之成立。当前外部定理仍未
到达这个口：Runbo Li 的短区间指数 `0.52` 在 `x=P^2` 处需要长度 `P^1.04`，
仍长于目标行长 `P`；大模数 AP 平均、Milićević--Qin--Wu、Pascadi、Wright
等 Kloosterman/Type-II 工具则需要先构造 admissible signed trace family。

最新非循环口为：

```text
LPFPurePowerVonMangoldtCompressionClosed
AND PrimePowerTailAbsorptionThresholdClosed
AND PrimePowerTailSublinearThresholdClosed
AND NeedPointwisePsiRowPositiveProportionAtSqrtScale
AND PointwiseAPThetaLowerBoundOrAdmissibleSignedTypeIIFamilyStillOpen
```

## 26. Runbo Li short-interval low-row band bridge

新增证书：

```text
experiments/prime_matrix_phi_lpf_runbo_li_low_row_band_bridge_audit.py
data/prime-matrix-phi-lpf-runbo-li-low-row-band-bridge-ledger.json
docs/monograph/prime-matrix-phi-lpf-runbo-li-low-row-band-bridge-audit.md
docs/monograph/prime-matrix-phi-lpf-runbo-li-low-row-band-bridge-audit.json
```

本层把上一节的平方根尺度 `psi/theta` 硬点与已知最强短区间输入精确对接。Runbo Li
证明充分大 `X` 时 `[X-X^0.52,X]` 含素数。对 strict row 取右端点

```text
X=(k+1)P.
```

若

```text
((k+1)P)^(13/25)<P  <=>  (k+1)^13<P^12,
```

则 Li 短区间完全落在 `(kP,(k+1)P)` 内；右端点 `(k+1)P` 是合数，因此该 row
无条件含素数。于是低行带

```text
1<=k<=P^(12/13)-1
```

由外部定理闭合。有限审计记录精确整数条件：例如 `P=1009` 时闭合 `591/1008`
行，`P=1000003` 时闭合 `345510/1000002` 行。

这是真推进，但不是完整闭合：闭合行数约 `P^(12/13)`，占全部 strict rows 的比例约
`P^(-1/13)`，趋向 `0`。主硬点仍集中在

```text
k+1>=P^(12/13)
```

的 top band，尤其 `k~P` 的平方根尺度行窗口。

最新非循环口为：

```text
RunboLiLowRowBandClosedForKPlusOneLessThanPTo12Over13
AND TopBandKPlusOneAtLeastPTo12Over13StillRequiresSqrtScalePointwisePsi
AND PrimePowerTailSublinearThresholdClosed
AND PointwiseAPThetaLowerBoundOrAdmissibleSignedTypeIIFamilyStillOpen
```

## 27. fixed theta short-interval zero-density band router

新增证书：

```text
experiments/prime_matrix_phi_lpf_theta_short_interval_zero_density_band_router.py
data/prime-matrix-phi-lpf-theta-short-interval-zero-density-band-ledger.json
docs/monograph/prime-matrix-phi-lpf-theta-short-interval-zero-density-band-router.md
docs/monograph/prime-matrix-phi-lpf-theta-short-interval-zero-density-band-router.json
```

本层把上一节的 Runbo Li 低行带桥接升级为一般路由。对任意固定
`theta>1/2` 的点态短区间输入，取 strict row 右端点

```text
X=(k+1)P.
```

要让长度 `X^theta` 的保证区间完全落入 `(kP,(k+1)P)`，必须满足

```text
X^theta<P  =>  k+1<P^((1-theta)/theta).
```

令 `alpha=(1-theta)/theta`。当 `theta>1/2` 时 `alpha<1`，所以外部输入最多闭合
`P^alpha` 量级低行，闭合比例 `P^(alpha-1)` 趋向 `0`；未闭合 top band 的密度趋向
`1`。Baker--Harman--Pintz `21/40`、Runbo Li `13/25`、Hieu/AP scale
representative `17/30` 以及任意固定 `0.5001` 级别输入都服从同一结论。

这一步的实际价值是排除一整类循环希望：继续把普通短区间指数从 `0.525` 改到
`0.52`、`0.5001` 等，只要仍是固定大于 `1/2`，就不能靠有限核查闭合全部 strict rows。
真正门槛是 `theta=1/2` 点态正比例 `psi/theta`，或绕过普通短区间框架的 structural
signed Type-II/trace family。

最新非循环口为：

```text
AllFixedThetaGreaterThanHalfShortIntervalInputsCloseOnlyZeroDensityLowRows
AND DensityOneTopBandStillRequiresThetaHalfPointwisePsiOrStructuralParityBreak
AND PrimePowerTailSublinearThresholdClosed
AND PointwiseAPThetaLowerBoundOrAdmissibleSignedTypeIIFamilyStillOpen
```

## 28. sqrt constant threshold router

新增证书：

```text
experiments/prime_matrix_phi_lpf_sqrt_constant_threshold_router.py
data/prime-matrix-phi-lpf-sqrt-constant-threshold-ledger.json
docs/monograph/prime-matrix-phi-lpf-sqrt-constant-threshold-router.md
docs/monograph/prime-matrix-phi-lpf-sqrt-constant-threshold-router.json
```

本层继续非循环推进：既然固定 `theta>1/2` 已经被排除为完整闭合路线，就必须审计
`theta=1/2` 自身的常数。对左端点输入

```text
(kP, kP + C sqrt(kP)]
```

落入 strict row 的条件是 `C^2 k<=P`；对右端点输入

```text
[(k+1)P-C sqrt((k+1)P),(k+1)P]
```

落入 strict row 的条件是 `C^2(k+1)<=P`。端点等号不造成素数泄漏，因为 `kP`
和 `(k+1)P` 都是合数端点。

结论是平方根路线的尖点不是“任意常数的 `sqrt(x)`”，而是 `C<=1`。任意固定
`C>1` 只闭合约 `P/C^2` 条低行，留下密度

```text
1-1/C^2
```

的 top band。例如 `C=1.0001` 仍留下约 `0.000199970` 的正密度顶层带；
`C=sqrt(2)` 留下一半顶层带。

这一步不证明新的素数存在定理，但把纯短区间路线的最后尺度口精确化：

```text
需要 C<=1 的点态 sqrt-scale 输入
OR 需要 structural parity break / admissible signed Type-II/trace family.
```

最新非循环口为：

```text
SqrtScaleConstantAtMostOnePointwiseInputWouldCloseStrictRows
AND AnyFixedSqrtConstantGreaterThanOneLeavesPositiveDensityTopBand
AND PrimePowerTailSublinearThresholdClosed
AND PointwisePsiAtSharpSqrtScaleOrAdmissibleSignedTypeIIFamilyStillOpen
```

## 29. sqrt-Oppermann top-row alignment router

新增证书：

```text
experiments/prime_matrix_phi_lpf_sqrt_oppermann_toprow_alignment_router.py
data/prime-matrix-phi-lpf-sqrt-oppermann-toprow-alignment-ledger.json
docs/monograph/prime-matrix-phi-lpf-sqrt-oppermann-toprow-alignment-router.md
docs/monograph/prime-matrix-phi-lpf-sqrt-oppermann-toprow-alignment-router.json
```

本层把上一节 `C<=1` 的平方根门槛在最坏 top row 上完全对齐。令 `k=P-1`，则

```text
I_top=(P^2-P,P^2).
```

右端点取 `X=P^2` 时，`C=1` 的平方根区间是

```text
[X-sqrt(X),X]=[P^2-P,P^2].
```

由于两个端点都是合数，任何由该闭区间输入给出的素数都必须落在开 top row 中。因此
`C=1` right-endpoint sqrt input 在 top row 上等价于 prime-indexed Oppermann left half：

```text
pi(P^2-1)-pi(P^2-P)>=1   (P prime).
```

同时，本层把 Legendre 型误出口切掉。Legendre 区间满足

```text
((P-1)^2,P^2)
=((P-1)^2,P^2-P] union (P^2-P,P^2),
```

且左右两半各有 `P-1` 个整数。Legendre theorem 允许素数全部出现在 lower leak half，
所以不能推出 top row。任意固定 `C>1` 的平方根输入同样包含 `P^2-P` 以下的泄漏带；
`C=sqrt(2)` 已有固定比例泄漏，`C=2` 比 Legendre 还多一个整数层。

最新非循环口为：

```text
PrimeIndexedOppermannLeftTopRowOrSharpCOneSqrtInputStillOpen
AND LegendreWideSquareIntervalDoesNotImplyTopRow
AND AnyFixedSqrtConstantGreaterThanOneHasLowerLeakStrip
AND PointwisePsiAtSharpSqrtScaleOrAdmissibleSignedTypeIIFamilyStillOpen
```

## 30. Oppermann subcore not-full-closure router

新增证书：

```text
experiments/prime_matrix_phi_lpf_oppermann_subcore_not_full_closure_router.py
data/prime-matrix-phi-lpf-oppermann-subcore-not-full-closure-ledger.json
docs/monograph/prime-matrix-phi-lpf-oppermann-subcore-not-full-closure-router.md
docs/monograph/prime-matrix-phi-lpf-oppermann-subcore-not-full-closure-router.json
```

本层切掉一个更细的误闭合出口：prime-indexed Oppermann-left top row 是完整
strict-row 正性的必要子核，但不是完整闭合本身。对每个素数 `P`，完整行正性要求

```text
pi((k+1)P-1)-pi(kP)>=1   for every 1<=k<P.
```

而 top row 只给 `k=P-1`：

```text
pi(P^2-1)-pi(P^2-P)>=1.
```

令 `h(x)=next_prime_after(x)-x`，则完整行正性等价于

```text
h(kP)<P   for every 1<=k<P,
```

top-row/Oppermann-left 只等价于单点 `h(P^2-P)<P`。因此它是必要条件，
但 containment 嵌入下只覆盖 `1` 行，不能替代其余 `P-2` 行。

审计读数：

```text
row_column_strict_positivity_implies_toprow=true
top_row_input_alone_closes_all_strict_rows=false
top_row_input_is_necessary_not_sufficient=true
all_rows_equivalent_to_prime_gap_bound_h_kP_less_than_P=true
row_column_unconditional_closed=false
phi_lpf_parity_barrier_globally_broken=false
```

最新非循环口进一步收窄为：

```text
TopRowOppermannLeftIsNecessarySubcoreNotFullClosure
AND FullRowsRequireGapBoundHkPLessThanPForEveryK
AND LPFPhiExactCountsRemainUnsignedParityBlind
AND PointwisePsiAtSharpSqrtScaleOrAdmissibleSignedTypeIIFamilyStillOpen
```

## 31. corrected-LPF signed-trace breakthrough router

新增证书：

```text
experiments/prime_matrix_phi_lpf_corrected_lpf_signed_trace_breakthrough_router.py
data/prime-matrix-phi-lpf-corrected-lpf-signed-trace-breakthrough-ledger.json
docs/monograph/prime-matrix-phi-lpf-corrected-lpf-signed-trace-breakthrough-router.md
docs/monograph/prime-matrix-phi-lpf-corrected-lpf-signed-trace-breakthrough-router.json
```

本层把 LPF 精确计数修正、有限 Euler 截断误差、Oppermann top-row 子核和外部
Type-II/trace 输入放在同一门控表里。结论不是三命题闭合，而是把最快非循环路线
明确改写为 signed payload 路线：

```text
lpf_exact_count_formula=C_p(N)=Phi(floor(N/p);q<p)-1
                    =Phi(floor(N/p);q<p)-Phi(p-1;q<p)
Phi(p-1;q<p)=1
finite_euler_truncation_error_type=primorial periodic boundary term
von_mangoldt_lift_requires_global_signed_payload=true
top_row_oppermann_necessary_not_sufficient=true
all_external_inputs_require_internal_admissible_family=true
row_column_unconditional_closed=false
```

路线裁定为：

```text
corrected LPF/Phi exact count        -> supporting only
ordinary short intervals/Oppermann   -> boundary only
terminal signed monotone-run payload -> fastest first-break candidate
two-point sieve                      -> second candidate
RH controlled exits                  -> verification package
```

外部前沿输入的适配判定也被统一：Runbo Li 短区间/大模 AP、Milićević--Qin--Wu
Kloosterman、Pascadi Type-II、Wright trilinear Kloosterman 与谱/群扩张工具都不能
直接从无符号 LPF bucket 使用；它们都要求先构造项目内部 admissible signed family。

最新非循环口进一步收窄为：

```text
CorrectedLPFExactCountsAndPeriodicErrorsDoNotGivePrimeEmission
AND PureShortIntervalOrTopRowInputsDoNotCloseAllRows
AND FastestPrimeMatrixRouteRequiresSignedTraceOrTypeIIFamily
AND UniformAdjacentRunCancellationOrNamedPDECSAEStillOpen
```

## 32. terminal-run trace-admissibility contract router

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_run_trace_admissibility_contract_router.py
data/prime-matrix-phi-lpf-terminal-run-trace-admissibility-contract-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-run-trace-admissibility-contract-router.md
docs/monograph/prime-matrix-phi-lpf-terminal-run-trace-admissibility-contract-router.json
```

本层继续上一节的最快非循环路线，但把“terminal signed monotone-run payload 能否接外部
trace/Type-II 定理”改写成明确合同。有限账本已经闭合：

```text
terminal_run_count_total=59
selected_terminal_run_count=35
extra_shell_run_count=24
strict_run_local_compression_count=0
selected_negative_excess=1.456565972578
extra_atom_local_survivor_total=0.907719323182
selected_negative_excess_minus_extra_atom_survivor=0.548846649396
finite_absorption_would_close_after_uniform_cancellation_law=true
```

但这还不是 admissible trace/Type-II family。要真正调用 FKMS trace functions、
Milićević--Qin--Wu Kloosterman、Pascadi Type-II、Wright trilinear Kloosterman 或
Runbo Li AP/Harman sieve，至少必须补齐六个接口：

```text
TerminalRunKernelFormula
SameTraceKeySourceConsistency
UniformFamilyInP
TypeIICoefficientFactorability
ConductorOrModulusControl
UniformAdjacentRunCancellation
```

因此本层的推进是把最快突破口从“找一个外部定理可套”收缩为“先构造内部 signed kernel
或返回命名 PDEC/SAE/LocalSurvivor”。最新非循环口为：

```text
TerminalRunTraceAdmissibilityContractPinned
AND FiniteSignedRunLedgerIsNotYetUniformTraceFamily
AND NeedTraceKernelOrTypeIICoefficientFormulaOrNamedPDECSAE
AND UniformAdjacentRunCancellationStillOpen
```

## 33. terminal trace-kernel source-key lift router

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_trace_kernel_source_key_lift_router.py
data/prime-matrix-phi-lpf-terminal-trace-kernel-source-key-lift-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-trace-kernel-source-key-lift-router.md
docs/monograph/prime-matrix-phi-lpf-terminal-trace-kernel-source-key-lift-router.json
```

本层把上一节六接口合同中的 `TerminalRunKernelFormula` 和
`SameTraceKeySourceConsistency` 继续向下拆。结论是：形式相位核已经存在，
但它是 post-pushforward 的 Jordan 账本，还不是 pre-Cauchy trace kernel。

已闭合的有限部分：

```text
formal_jordan_phase_kernel_closed=true
prefix_record_reflection_schema_closed=true
source_key_obstruction_partition_closed=true
boundary_ratio_spectrum_closed=true
sibling_qspine_finite_kernel_closed=true
```

未闭合的 actual source-key 门：

```text
q_boundary_synthetic_split_event_count=47
nonboundary_record_jump_event_count=4
internal_survivor_fragment_count=1
terminal_double_awrap_sibling_qspine_kernel_payment_law_proved=false
```

因此最快下一攻击点不再是抽象 trace theorem，而是 `BoundaryRatioSourceKeyLawOrPDEC`。
边界比率谱已经精确到：

```text
ratio_min=0.013003592969
ratio_max=0.967151620496
whole_equal_pair_event_count=0
```

最新非循环口为：

```text
TraceKernelSourceKeyLiftReductionClosed
AND BoundaryRatioSourceKeyLawOrPDEC
AND NonBoundaryRecordJumpSourceKeyLiftOrPDEC
AND InternalSurvivorPDEC
AND TerminalSiblingQSpinePaymentOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND UniformAdjacentRunCancellationStillOpen
```

## 34. boundary ratio q-spine pivot reduction router

新增证书：

```text
experiments/prime_matrix_phi_lpf_boundary_ratio_qspine_pivot_reduction_router.py
data/prime-matrix-phi-lpf-boundary-ratio-qspine-pivot-reduction-ledger.json
docs/monograph/prime-matrix-phi-lpf-boundary-ratio-qspine-pivot-reduction-router.md
docs/monograph/prime-matrix-phi-lpf-boundary-ratio-qspine-pivot-reduction-router.json
```

本层把上一节的 `BoundaryRatioSourceKeyLawOrPDEC` 继续降维。47 个 q-boundary split
不再是散乱比率谱，而是沿 residual-flow 链压到 q-spine pivot enclosure：

```text
old_residual_side_closed=true
new_residual_tail_alignment_partial_closed=true
bulk_carry_chain_normal_form_closed=true
carry_break_source_packet_reduction_closed=true
bridge_root_qspine_pivot_enclosure_reduction_closed=true
boundary_ratio_source_key_law_reduced_to_qspine_pivot=true
```

实际账本：

```text
new_residual_side_event_count=42
old_residual_side_event_count=5
old_residual_return_aligned_event_count=5
new_residual_tail_matched_event_count=6
new_residual_unmatched_after_tail_event_count=36
carry_segment_count=11
carry_transition_count=31
bridge_root_debt_break_count=2
bridge_root_debt_still_open=0.209830550963
q_spine_nodes=[577,607,631]
shared_pivot_q=607
```

因此真正剩余不再是一般 boundary ratio law，而是：

```text
BoundaryRatioQSpinePivotReductionClosed
AND BridgeRootQSpinePivotEnclosureLawOrPDEC
AND RightSelectedTerminalTailOverhangPDEC
AND TerminalSiblingQSpinePaymentOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

## 35. bridge-root shared-pivot hinge contract router

新增证书：

```text
experiments/prime_matrix_phi_lpf_bridge_root_shared_pivot_hinge_contract_router.py
data/prime-matrix-phi-lpf-bridge-root-shared-pivot-hinge-contract-ledger.json
docs/monograph/prime-matrix-phi-lpf-bridge-root-shared-pivot-hinge-contract-router.md
docs/monograph/prime-matrix-phi-lpf-bridge-root-shared-pivot-hinge-contract-router.json
```

本层不重复上一节的 finite pivot-enclosure，而是把 `BridgeRootQSpinePivotEnclosureLawOrPDEC`
拆成更小的 shared-pivot hinge 合同。两个 bridge-root packet 满足：

```text
q_spine_nodes=[577,607,631]
shared_pivot_q=607
endpoint_slack=moving_barrier_q-bridge_root_q=P-q-g*(1+r)
packet1.unit_root=packet2.bridge_root=packet2.barrier=607
packet1.barrier=packet2.unit_root=631
bridge_root_qspine_pivot_to_shared_hinge_contract_closed=true
```

这给出一个非循环推进：boundary ratio source-key 的剩余硬口不再是抽象的
`q=607` pivot 描述，而是三类具体统一律：

```text
BridgeRootSharedPivotHingeLawOrPDEC
BridgeRootEndpointSlackNonnegativeLawOrPDEC
BridgeRootQSpineGapPaymentLawOrPDEC
```

同时本层重新锁定 LPF/Phi 边界：正确 LPF bucket 精确公式仍是

```text
C_p(N)=Phi(floor(N/p); primes<p)-1
```

有限 Euler half-main 现象不是截断误差定理，而是 odd-axis 归一化问题；因此
无符号 LPF 计数仍不能替代 signed payload。

最新开放口：

```text
BoundaryRatioQSpinePivotReductionClosed
AND BridgeRootSharedPivotHingeLawOrPDEC
AND BridgeRootEndpointSlackNonnegativeLawOrPDEC
AND BridgeRootQSpineGapPaymentLawOrPDEC
AND TerminalDoubleAwrapSiblingQSpineKernelPaymentOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

外部前沿定理的使用边界同步收缩：FKMS、Kloosterman/Type-II、Wright 三线性、
Runbo Li Harman sieve 和 thin-group expansion 都仍需先从该 hinge 合同构造
admissible signed family；当前尚不能直接闭合三命题之一。

## 36. parity barrier prime-distribution contract router

新增证书：

```text
experiments/prime_matrix_phi_lpf_parity_barrier_prime_distribution_contract_router.py
data/prime-matrix-phi-lpf-parity-barrier-prime-distribution-contract-ledger.json
docs/monograph/prime-matrix-phi-lpf-parity-barrier-prime-distribution-contract-router.md
docs/monograph/prime-matrix-phi-lpf-parity-barrier-prime-distribution-contract-router.json
```

本层回答“奇偶性障碍究竟是什么”。经过 LPF 精确计数、Legendre-Phi 周期截断误差、
affine `2n+1` 归一化、von Mangoldt 纯素幂压缩、prime-power tail absorption、
terminal trace contract 与 shared-pivot hinge 的串联审计，结论是：

```text
parity_barrier_diagnosis_closed=true
lpf_correction_closed=true
lpf_bucket_exact_formula=C_p(N)=Phi(floor(N/p); primes<p)-1
legendre_periodic_boundary_not_half_main=true
unsigned_lpf_bucket_count_sufficient_for_prime_extraction=false
trace_or_typeii_family_admissible_now=false
row_column_unconditional_closed=false
```

障碍的本质不是“还少一个更精细 Euler product”。无符号粗数 survivor 计数即使完全精确，
仍同时容纳素数、P2、P3 和更深粗合数；它没有 Möbius/von Mangoldt 符号相消，也没有
trace/Kloosterman 的相位取消。因此真正能越过障碍的合同只有几类：

```text
PointwiseThetaShortIntervalAtSqrtScale:
  theta((kP,(k+1)P))>0
PsiBeyondPrimePowerTail:
  psi((kP,(k+1)P)) > prime_power_tail((kP,(k+1)P))
SignedMobiusVonMangoldtTypeITypeII:
  source-key consistent Type-I/II or Vaughan/Heath-Brown family
TraceKloostermanFamilyFromQSpineHinge:
  completed source-keyed Kloosterman/trace sums
NamedPDECOrSAEReturn:
  uniform-law failure returns to a controlled contradiction
```

最新开放口：

```text
ParityBarrierContractPinned
AND NeedPointwiseThetaOrPsiRowLowerBoundBeyondPrimePowerTail
AND NeedAdmissibleSignedDivisorTraceOrTypeIIFamily
AND BridgeRootSharedPivotHingeLawOrPDEC
AND TerminalDoubleAwrapSiblingQSpineKernelPaymentOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
```
