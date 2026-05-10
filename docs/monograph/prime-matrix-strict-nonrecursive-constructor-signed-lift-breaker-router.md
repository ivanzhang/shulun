# Prime Matrix strict 非递归 constructor/signed-lift 破环输入审查

**状态：** `nonrecursive_constructor_signed_lift_breaker_atomized_kernel_identity_open`

本步直接审查真正破环输入。结论是：六个内部基的证据路线大多已定位，但都没有在当前材料中被非递归证明；若逐腿推进，它们会回流到 source table、emitter、PDEC/CleanKLS 或命名回流固定点。因此当前最窄点不是再拆六项，而是提交一个同一 formal unit 下的 pre-Cauchy alpha/delta 核恒等式，同时携带 signed source、Phi 推前、变差预算和 exact-UV 分散。在该核恒等式给出前，目标命题仍未无条件闭合。

```text
terminal_cycle_breaker_target_active=true
current_internal_route_is_fixed_point=true
all_basis_evidence_routes_closed=true
nonrecursive_breaker_package_proved=false
same_formal_unit_kernel_identity_proved=false
current_route_still_fixed_point_without_new_kernel_identity=true
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 内部基审查

| atom | evidence_closed | proved | current evidence | obstruction | needed |
| --- | --- | --- | --- | --- | --- |
| `ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter` | `true` | `false` | alpha/delta 规则已压成两侧 primitive rule 与 pairing nonzero 检查。 | 该规则仍依赖 actual noncanonical source tuple；没有非递归来源表时不能独立生成 constructor。 | 同一 formal unit 的 primitive summand 公式、u/v map、sign/local factor 与非零/回流表。 |
| `ActualSignedAlphaSourceMeasureForCarryShellRowsLedger` | `true` | `false` | 早期零行和几何链已被审查为 unsigned covering/payment 数据。 | unsigned carry-shell、斜线覆盖、P列锚和层叠轮不定义 signed alpha source measure。 | pre-Cauchy 阶段直接定义 signed measure nu_alpha，并列出每个 carry-shell row 的来源。 |
| `AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger` | `true` | `false` | 权重律已同步到 IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger。 | 现有下游路线把权重律送回 moving block、NCBLK 与 PDEC/CleanKLS 终端门，形成固定点。 | 一个不调用终端门的算术核恒等式，直接给出 alpha 权重、符号和 local factor。 |
| `AlphaRowsPhiPushforwardCompatibilityLedger` | `true` | `false` | 几何 Phi/payment base 可用；解积分形式上说明给定 signed source 后可逐纤维推前。 | Phi_*nu 等于 payment-side alpha 系数不是几何覆盖自动推出的等式。 | 同一核恒等式必须同时给出 source 侧和 payment 侧，并证明逐纤维求和相等。 |
| `AlphaSignedLiftVariationBranchBudgetLedger` | `true` | `false` | 圆柱斜线、P列锚和层叠轮给出支撑/相位/branch 字母表与预算候选形状。 | 绝对支撑预算不能替代 signed 总变差预算；branch key 爆炸也不能靠 unsigned 模型消除。 | 同一 formal unit 下的总变差、绝对支撑、branch key 数和失败命名回流预算。 |
| `PreTerminalExactUVFiberAbsoluteMassDispersionTheorem` | `true` | `false` | fiber 非集中已压成 pre-pushforward primitive emitter 的绝对质量/multiplicity 分散。 | 该分散仍未独立证明；向下会进入 emitter/source table/constructor，最终回到同一 signed source 包。 | 核恒等式需同时给出 exact-UV fiber 的绝对质量分散或 bounded multiplicity 证明。 |
| `NonrecursiveSourceOriginCondition` | `true` | `false` | pre-Cauchy 来源律显示需要原始生成账本；来源环切断拒绝 downstream 反推。 | payment skeleton、终端证书、有限投影或早期零行覆盖都不能作为 primitive source 的来源证明。 | 证明必须在 Cauchy、dispersion、terminal extraction 之前提交原始来源。 |

## 2. 新最窄破环输入

```text
SameFormalUnitPreCauchyAlphaDeltaKernelIdentityWithSignedPhiAndFiberDispersion
```

SameFormalUnitPreCauchyAlphaDeltaKernelIdentityWithSignedPhiAndFiberDispersion: 在同一 formal unit、Cauchy/dispersion/terminal extraction 之前，一次性给出 actual noncanonical alpha/delta primitive constructor、signed alpha source measure、pre-Cauchy 权重律、Phi 推前恒等式、signed 变差/branch 预算和 exact-UV fiber 分散；证明过程不得回调 PDEC/CleanKLS 终端门、canonical scoped import、source entropy 目标自身，也不得从早期零行 unsigned covering data 反向生成 source。

## 3. 核恒等式字段

| field | requirement |
| --- | --- |
| `formal_unit` | 固定同一 formal unit；不得在 source、Phi、fiber 或 terminal 侧更换 witness 集合。 |
| `primitive_constructor` | 列出 alpha/delta primitive summand 的 u/v map、branch key、sign、local factor 和非零条件。 |
| `signed_source_measure` | 在 carry-shell rows 上定义 actual signed alpha source measure，而不是 unsigned cover。 |
| `arithmetic_weight_identity` | 用 pre-Cauchy 算术恒等式给出权重律，不能回调 PDEC/CleanKLS 或 source entropy 目标。 |
| `phi_pushforward` | 证明 Phi_*nu_alpha 等于 payment-side alpha 系数，含端点、重数和符号。 |
| `variation_branch_budget` | 同时控制 signed 总变差、绝对支撑、branch key 数，超预算时命名回流。 |
| `exact_uv_fiber_dispersion` | 给出 exact-UV fiber 绝对质量分散或 bounded multiplicity，且与同一 source measure 兼容。 |
| `failure_return` | 任何字段缺失、Phi 不兼容、变差超预算、canonical 泄漏或 terminal-dependent key 都登记到同一命名出口。 |

## 4. 判定

六个内部基可在同一 witness 集上合取，NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage 才成为真正破环输入；随后可重新进入 exact-UV/source entropy 链，检查是否推出终端矛盾。

现有内部路线只能回到 PDEC/CleanKLS 固定点；不能声明行/列命题作者侧无条件闭合。

并行保留验收线：

```text
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks
ExplicitModelGapAndFiniteDPRCLedger
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```
