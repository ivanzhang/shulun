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
