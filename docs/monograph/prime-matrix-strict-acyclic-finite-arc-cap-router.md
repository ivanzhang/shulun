# Prime Matrix strict acyclic 有限弧 cap 路由器

**状态：** `acyclic_finite_arc_cap_independent_input_removed_clean_kls_remaining`

本步直接攻 `AcyclicFiniteArcCapMassBoundsOrNamedReturn`。有限弧是同一 finite formal unit 中的秩一字符弧；高质量弧若有低横向支撑、持久横向偏斜、列/壳集中或新增层偏斜，都会命名回流到 SAE、ColumnCRT 或 refined/new-layer PDEC；若这些缺陷全部剥离，剩余就是横向 L2-flat clean residual，必须进入 `DirectAcyclicCleanKLSDLSEstimateWithNamedReturn`。因此有限弧 cap 不再是独立剩余，但 clean KLS/DLS 估计仍未证明，完整命题仍未闭合。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
same_set_count_vector_imported=true
finite_arc_rank_one_slice_imported=true
low_transverse_support_named_return_closed=true
persistent_transverse_bias_named_return_closed=true
transverse_flat_residual_clean_admission_closed=true
acyclic_finite_arc_no_unnamed_exit_closed=true
acyclic_finite_arc_independent_input_removed=true
acyclic_finite_arc_cap_mass_bounds_proved=false
direct_acyclic_same_set_pdec_dual_proved=false
direct_acyclic_clean_kls_dls_proved=false
strict_terminal_family_proved=false
row_column_unconditional_closed=false
```

## 1. 有限弧三分

```text
finite arc cap chi^{-1}(I) inside same g_B
  low transverse support / short sparse / column-shell concentration
    => SAE / ColumnCRT / fixed-shell PDEC return
  persistent transverse or new-layer bias
    => refined PDEC / new-layer PDEC return
  otherwise
    => transverse L2-flat clean residual
    => DirectAcyclicCleanKLS/DLS
```

## 2. 终端门更新

更新前：

```text
AcyclicFiniteArcCapMassBoundsOrNamedReturn
```

更新后：

```text
(AcyclicSeedCanonicalBranchAdmissionBeforeCauchy AND AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity AND AcyclicSeedNoSourceReplacementOrPayloadCreation AND TerminalCertificateSameSetPushforwardIdentity AND NoNoncanonicalPayloadSurvivesCanonicalProjection) OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn
```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `AcyclicFiniteArcCapActive` | `true` | `false` | 上一层 direct PDEC 剩余为同一 g_B 上的有限循环弧 cap 质量上界或命名回流。 | AcyclicFiniteArcCapMassBoundsOrNamedReturn |
| `SameSetCountVectorImported` | `true` | `true` | 已固定 acyclic formal unit G、坏窗集合 B、同一 count vector g_B 与质量 M。 | 只允许在同一 g_B 上做弧 cap 判定。 |
| `FiniteArcRankOneSliceImported` | `true` | `true` | 任意方向帽都是非平凡字符有限像上的循环弧预像，即秩一切片。 | 检查弧内横向变量。 |
| `LowTransverseSupportNamedReturn` | `true` | `true` | 高质量弧若由低横向支撑、孤立短窗、列位移或固定壳承担，则生成 SAE/ColumnCRT/fixed-shell PDEC return。 | 无；它不保留为 cap-stable PDEC 核。 |
| `PersistentTransverseBiasNamedReturn` | `true` | `true` | 高质量弧若有持久横向偏斜，则弧指标并入签名，得到 refined/new-layer PDEC；有限层细化无循环。 | 无；它回到 PDEC 命名路线。 |
| `LowModArcClassificationImported` | `true` | `true` | 固定轮弧、新增层弧、高模平坦弧分别进入 W-unit PDEC、new-layer PDEC、flat DLS/KLS。 | 高模平坦弧进入 clean DLS，不再是 PDEC 弧 cap 独立输入。 |
| `TransverseFlatResidualCleanAdmission` | `true` | `true` | 若弧内没有低支撑、持久偏斜或列/壳集中，则剩余是横向 L2-flat clean residual，准入 DirectAcyclicCleanKLS/DLS。 | DirectAcyclicCleanKLSDLSEstimateWithNamedReturn |
| `FiniteArcNoUnnamedExitClosed` | `true` | `true` | 有限弧 cap 不能作为第四类无名出口；它要么命名回流，要么成为 clean DLS/KLS residual。 | 证明 clean DLS/KLS 吸收。 |
| `AcyclicFiniteArcIndependentInputRemoved` | `true` | `true` | AcyclicFiniteArcCapMassBoundsOrNamedReturn 作为独立 PDEC 剩余已删除；未闭合部分转到 direct clean KLS/DLS。 | DirectAcyclicCleanKLSDLSEstimateWithNamedReturn |
| `DirectAcyclicPDECDualProved` | `true` | `false` | PDEC 分支已无独立有限弧逃逸，但没有证明所有弧质量均低于阈值；平坦弧转入 clean 分支。 | DirectAcyclicCleanKLSDLSEstimateWithNamedReturn |
| `DirectCleanKLSStillOpen` | `true` | `false` | 当前真正最窄终端硬点变成 strict acyclic clean residual 的内部 KLS/DLS 大筛估计或命名回流。 | DirectAcyclicCleanKLSDLSEstimateWithNamedReturn |

## 4. 最新严格基

若接受外部 Mertens/theta 显式定理，高段解析缺口移出后，当前 strict 基为：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND ((AcyclicSeedCanonicalBranchAdmissionBeforeCauchy AND AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity AND AcyclicSeedNoSourceReplacementOrPayloadCreation AND TerminalCertificateSameSetPushforwardIdentity AND NoNoncanonicalPayloadSurvivesCanonicalProjection) OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn) AND SelfContainedDStructureTailLog4FiniteRankinReplacementPackage
```

## 5. 下一主攻合同

主攻名：`DirectAcyclicCleanKLSDLSEstimateWithNamedReturn`。

必须证明：
- 对已剥离 PDEC/SAE/ColumnCRT 的 acyclic clean residual 验证 K1--K9 clean admission。
- 给出同一 formal unit 上的 L2-flat 系数账本和窗口化 Kloosterman/dispersion 参数映射。
- 证明内部 DLS/KLS 大筛吸收，或把失败命名回流到 PDEC/SAE/ColumnCRT/Multiplicity。
- 若使用外部 DI/BFI/Kuznetsov 定理，必须明确标记为外部条件路线，不能声明严格自足闭合。

不能作为证明使用：
- 把有限弧无第四出口当成 clean 大筛估计。
- 把 canonical-source NC-BLK 吸收直接导入 acyclic/noncanonical clean residual。
- 把 K1--K9 准入当成大筛证明；准入后仍需 KLS/DLS 界。
- 用有限实验中弧 cap 消失替代全局横向平坦估计。
