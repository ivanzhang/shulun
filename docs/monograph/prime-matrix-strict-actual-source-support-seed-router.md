# Prime Matrix 严格 actual source-support 种子/能量路由器

**状态：** `new_actual_exact_uv_support_reduced_to_acyclic_seed_and_pair_mass_dispersion_open`

NewActualNoncanonicalExactUVSupportTheoremInput 已进一步拆成两个不可混淆的数学原子：先要有无环的 pre-Cauchy actual noncanonical source seed；再要证明该 source 在 exact (u,v) 纤维上没有大原子，即满足最大 pair 质量界或 L2 能量界。一般支撑能量引理本身是初等闭合的：总绝对质量除以最大原子，或 Cauchy 的 M^2/E2，给出 pair 支撑下界；pair 支撑再推出 S_u*S_v 下界。当前材料缺的不是这个初等推理，而是 actual source seed 与 exact pair 质量分散账本。因此仍不能声明行/列无条件闭合。

```text
new_actual_exact_uv_support_boundary_closed=true
elementary_mass_support_lemma_closed=true
acyclic_pre_cauchy_seed_proved=false
exact_uv_pair_mass_dispersion_proved=false
actual_exact_uv_support_proved=false
row_column_unconditional_closed=false
terminal_gap_after_router=AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND ExactUVPairMassDispersionOrMaxAtomBoundLedger
```

## 1. 新压缩链

```text
NewActualNoncanonicalExactUVSupportTheoremInput
  -> AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn
  -> SignRefinedExactPairFamilyForSameFormalUnit
  -> ExactUVPairMassDispersionOrMaxAtomBoundLedger
  -> ElementaryMassSupportLemma
  -> ActualNoncanonicalExactUVSupportLowerBound
```

## 2. 初等支撑能量引理

| form | statement | role |
| --- | --- | --- |
| pair max | For a sign-refined exact pair family w_omega over Omega, if M=sum|w_omega|>0 and max|w_omega|<=M/L^K, then |Omega|>=L^K. | 排除单 pair 大原子。 |
| L2 | If E2=sum|w_omega|^2 and M=sum|w_omega|, then |Omega|>=M^2/E2. | 允许用二次能量替代逐点最大界。 |
| ExactUV | Since |Omega|<=|U_support|*|V_support|, either lower bound implies S_u*S_v>=L^K. | 从 pair 支撑转成 `S_u*S_v`。 |

该引理只关闭形式推理，不证明 actual source 的质量分散。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `NewActualExactUVSupportInputActive` | `true` | `false` | 上一层已把严格自足 ExactUV 主攻点定名为 NewActualNoncanonicalExactUVSupportTheoremInput。 | 把该输入拆成可证明的来源种子与支撑能量原子。 |
| `SourceLoopCutImported` | `true` | `true` | 来源环已被切断，不能从 downstream payment skeleton、有限投影塔或几何覆盖图反推 primitive source。 | 必须提交无环 pre-Cauchy actual noncanonical primitive source seed。 |
| `DisintegrationEquivalenceImported` | `true` | `true` | alpha/delta lift 等价于 signed 源测度在 first-cover payment map 上的注册解积分字典。 | 等价不证明 actual 字典存在；仍需给出 signed source measure 和推前恒等式。 |
| `SourceIdentityAloneInsufficient` | `true` | `true` | 即使有 signed source identity，若所有质量集中到一个 exact (u,v)，也不能推出 ExactUV 支撑。 | 需要 exact pair mass dispersion 或最大原子界。 |
| `ElementaryMassSupportLemmaClosed` | `true` | `true` | 同号/符号细分后，若总绝对质量为 M 且每个 exact pair 质量至多 M/L^K，则 pair 支撑至少 L^K；L2 形式亦由 Cauchy 给出。 | 证明 actual clean-core 源满足这些 M、max-pair 或 L2 能量界。 |
| `ExactUVPairMassDispersionRequired` | `true` | `false` | 支撑下界的真正数值负担是 actual source 在 exact (u,v) 纤维上的最大原子/能量控制。 | ExactUVPairMassDispersionOrMaxAtomBoundLedger。 |
| `AcyclicPreCauchySeedStillRequired` | `true` | `false` | 能量界必须作用在真实 pre-Cauchy source 上；没有无环源种子时，能量账本没有对象。 | AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn。 |
| `CurrentCorpusNoProofOfSupportBearingSeed` | `true` | `false` | 当前语料库没有证明 support-bearing actual source seed，也没有证明 exact pair 最大原子界。 | 新增证明其中两个原子，或转条件外部谱线。 |

## 4. 下一主攻合同

下一数学主攻点：`ExactUVPairMassDispersionOrMaxAtomBoundLedger_FOR_AcyclicPreCauchySeed`。

必须证明：
- 提交不依赖 downstream payment 图的 actual noncanonical pre-Cauchy signed source seed。
- 把 source seed sign-refine 到无抵消 exact path/pair family。
- 给出总绝对质量下界 M0，且该质量属于同一 formal unit。
- 证明每个 exact (u,v) pair 的绝对质量至多 M0/L^(2A+4C+E)，或证明等价 L2 能量界。
- 证明 thin、rejected、path-overbudget、large atom 失败全部命名回流。

不能作为证明使用：
- 从 payment skeleton、CRT 覆盖图或早期零行假设反推 source。
- canonical RIW/Buchstab 来源表跨分支导入。
- generic WFD、K4/K6 或 raw squarefree count。
- 只给 source identity 而不给 exact pair 最大原子/能量界。
- 外部 FullS-KLS 黑箱。

严格自足数学基更新为：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND ExactUVPairMassDispersionOrMaxAtomBoundLedger AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```
