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

## 7. 审稿边界

```text
finite_ledgers_are_evidence_not_final_proof=true
actual_load_not_formal_envelope=true
support_only_is_parity_blind=true
external_theorem_requires_admissible_family=true
rankone_ap_positivity_direct_route_not_closed=true
```

本文件的作用是防止回到循环路线：它没有宣称完成任何三命题的无条件证明，而是把下一步真突破压成可验证的 signed-payload/trace-constructor 或 named-return 合同。
