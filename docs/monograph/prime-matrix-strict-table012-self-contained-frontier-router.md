# Prime Matrix strict table_012 自足前沿下钻证书

**状态：** `table012_self_contained_frontier_reduced_to_generator_or_independent_theta_extremal_archive`

严格自足线的 P5.1 低段剩余已压到 table_012 的来源证明：已发表表行的 b1<0 覆盖可以外部使用，但作者侧自足版还缺原始生成器/输入/hash，或一份独立重算的 34 区间 theta 极值归档。因此下一最窄点不是再拼接 P5.1，而是 `Table012OriginalGeneratorOrIndependentThetaExtremalArchiveLedger`。

```text
theta_less_than_identity_to_8e11_external_closed=true
theta_less_than_identity_to_8e11_self_contained_closed=false
dusart_p51_full_theta_statement_external_closed=true
dusart_p51_full_theta_statement_self_contained_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 自足缺口

```text
ThetaLessThanIdentityFiniteTableTo8e11SelfContainedLedger
  =>
Table012OriginalGeneratorOrIndependentThetaExtremalArchiveLedger AND Table012DirectedRoundingAndIntervalPropagationLedger

Table012OriginalGeneratorOrIndependentThetaExtremalArchiveLedger
  =>
PublishedTable012GeneratorArtifactAndHashLedger OR IndependentThetaExtremalArchiveForTable012IntervalsLedger
```

## 2. 规模与边界

| field | value |
| --- | --- |
| `interval_count` | `34` |
| `range_width_integer_count` | `7.999E+11` |
| `prime_jump_count_scale_estimate_x_over_logx` | `29188688475.2017810894038403484547164368961151948828031619949` |
| `worst_published_margin_label` | `7E+11` |
| `worst_published_margin_right` | `800000000000` |
| `worst_published_relative_margin` | `3.64858605940022263617548004355683955461201439936035039524937E-7` |

## 3. 必补账本

| ledger | closed | role | remaining |
| --- | --- | --- | --- |
| `Table012StatementAndIntervalRuleLedger` | `true` | 确认 table_012 的区间口径和 b1 上界公式。 | none |
| `Table012TranscriptionNegativeB1CoverLedger` | `true` | 确认已发表表行若被接受，则 b1<0 连续覆盖 [1e8,8e11]。 | none on external lane |
| `PublishedTable012GeneratorArtifactAndHashLedger` | `false` | 取得原始 table_012 生成文件、算法说明、输入数据和 hash。 | theta_pk/tables/table_012.tex or equivalent published artifact |
| `IndependentThetaExtremalArchiveForTable012IntervalsLedger` | `false` | 独立重算 34 个区间内 theta 极值，证明每个 b1 为外向上界。 | per-interval extremal theta archive with hash |
| `Table012DirectedRoundingAndIntervalPropagationLedger` | `false` | 证明表值小数截断/舍入方向是外向安全的，而不是仅复录小数。 | PublishedTable012GeneratorArtifactAndHashLedger OR IndependentThetaExtremalArchiveForTable012IntervalsLedger |

## 4. 可攻路线

| route | target | status | action |
| --- | --- | --- | --- |
| `published_artifact_route` | `PublishedTable012GeneratorArtifactAndHashLedger` | `open` | 补入 table_012 的原始生成工件、输入文件、外向舍入日志和 hash。 |
| `independent_regeneration_route` | `IndependentThetaExtremalArchiveForTable012IntervalsLedger` | `open` | 实现分段 theta 极值 runner，输出 34 个区间的最大归一化误差和可复现 hash。 |
| `analytic_bypass_route` | `DirectThetaLtIdentity1e8To8e11AnalyticLedger` | `open but not narrower than table artifact route` | 用更强显式 PNT/零点自由区直接证明 theta(x)<x；这会回到内部 Dusart/PNT 包。 |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只下钻 P5.1 低段有限表输入，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `P51ExternalLaneAlreadyClosed` | `true` | `true` | 接受外部 FK/Dusart 表时，P5.1 theta 上界已闭合；本步只处理严格自足剩余。 | DusartP51ThetaUpperFullSelfContainedLedger |
| `StrictTable012SelfContainedGateActive` | `true` | `true` | P5.1 自足缺口唯一落在 table_012 原始有限计算/hash。 | ThetaLessThanIdentityFiniteTableTo8e11SelfContainedLedger |
| `PublishedTable012StatementAndNegativeB1Cover` | `true` | `true` | 表陈述、区间规则和 b1<0 复录审计已闭合；这是外部表可用性，不是自足生成证明。 | external table lane closed |
| `Table012GeneratorArtifactPresent` | `false` | `false` | 仓库没有 table_012 原始生成文件或可复现计算日志。 | PublishedTable012GeneratorArtifactAndHashLedger |
| `IndependentThetaExtremalArchivePresent` | `false` | `false` | 仓库没有 34 区间 theta 极值归档；中段 psi 节点表从 8e11 开始，不能替代 [1e8,8e11] 的 theta 表。 | IndependentThetaExtremalArchiveForTable012IntervalsLedger |
| `ThetaLessThanIdentityFiniteTableTo8e11SelfContainedLedger` | `false` | `false` | 严格自足版必须补原始表生成器或独立极值归档，并证明外向舍入。 | Table012OriginalGeneratorOrIndependentThetaExtremalArchiveLedger AND Table012DirectedRoundingAndIntervalPropagationLedger |
| `DirectUnconditionalContradictionFound` | `false` | `false` | table_012 自足化只是解析输入补强，不产生反例链与真实链终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `RowColumnUnconditionalClosed` | `false` | `false` | 行/列命题仍未作者侧无条件闭合。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 6. 下一最窄点

```text
Table012OriginalGeneratorOrIndependentThetaExtremalArchiveLedger
```

