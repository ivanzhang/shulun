# Prime Matrix LowMod endpoint formal-unit 路由器

**状态：** `lowmod_endpoint_routed_to_future_pdec_schema_or_sparse_sae`

本步把 LowMod endpoint CRTDefect 的准入纪律闭合：它不能作为无名出口，也不能被当前 PDEC 候选为零直接排除。若坏行在同一低模块上持续出现，它必须提交同 formal unit 的 future primitive PDEC schema；若只稀疏出现，它必须进入 SAE/local survivor 或 ColumnCRT 位移吸收。真正未闭合的是这些准入后的排斥。

```text
lowmod_formal_unit_admission_boundary_closed=true
current_pdec_zero_not_future_exclusion=true
lowmod_endpoint_exclusion_closed=false
row_column_unconditional_closed=false
terminal_gap_after_router=LowModFuturePDECSchemaExclusionOrSparseSAE
```

## 1. Formal Unit 形状

| field | value |
| --- | --- |
| `Omega` | bad aligned rows x triggering the same LowMod block B and sign |
| `phase_map` | x mod Q_B where Q_B=lcm(d: d in B) |
| `test_function` | f_B(x)=sum_{d in B} mu(d) epsilon_d(x) |
| `bad_set` | S={x: sign*f_B(x)>=kappa_B} |
| `persistent_branch` | \|S\|>=beta Q_B => nonzero Fourier defect => future primitive PDEC schema |
| `sparse_branch` | \|S\| small => SAE/local survivor or endpoint escape exclusion |

关键纪律是：单点 LowMod 端点尖峰不是矛盾；只有同一低模块、同一符号、同一相位图上的坏行集合，
才能形成可审查的 persistent PDEC 输入。否则就是 sparse/local escape，需要 SAE 或局部幸存者排斥。

## 2. 判定表

| gate | closed | proved | meaning | output |
| --- | --- | --- | --- | --- |
| `LowModBranchImported` | `true` | `true` | 上一轮已把一素分支为零路由到 LowMod endpoint CRTDefect 或 Tail/Core concentration。 | `本步只处理 LowMod endpoint 分支。` |
| `FiniteLowModSawtoothUnit` | `true` | `true` | LowMod 分支是 d<=D 的有限 squarefree 模 sawtooth 线性组合，依赖同一个 x 相位。 | `可定义同一 formal unit Omega=S, tau=d-block, w=mu(d)。` |
| `PersistentSparseDichotomyImported` | `true` | `true` | DEC 文档已证明单点 DEC 不能排斥；必须二分为 persistent DEC 或 sparse/local escape。 | `PersistentLowModPDECOrSparseSAE。` |
| `PersistentToFourierDefect` | `true` | `true` | 若同一低模块坏行有正密度，坏行指示函数产生非零 Fourier/CRT 缺陷。 | `可进入 PDEC admission，而不是单点均衡矛盾。` |
| `ExplicitPDECSchemaDiscipline` | `true` | `true` | 未来 LowMod PDEC 必须满足同 formal unit、非二点、至少三物理原子、二秩以上、cap-stable。 | `LowModFutureExplicitPrimitivePDECSchemaRequired。` |
| `LowRankColumnSparseAbsorption` | `true` | `true` | 若 LowMod 缺陷低秩、单窗、稀疏或固定列位移复用，则不准作为新 PDEC，回流 SAE/ColumnCRT/PDEC 吸收。 | `NoFourthLowModExit。` |
| `CurrentMaterializedPDECCandidatesDoNotExcludeFutureLowMod` | `true` | `true` | 当前已物化 PDEC 候选为零只说明现有材料清零；假设反例产生的新 LowMod formal unit 仍必须单独验收。 | `不能用 current_materialized_pdec_frontier_closed 直接排斥反例。` |
| `LowModEndpointExclusion` | `false` | `false` | 尚未证明所有准入后的 persistent LowMod PDEC 都满足 U_CRT<L_PDEC，或所有 sparse LowMod 窗口被 SAE 排除。 | `LowModFuturePDECSchemaExclusionOrSparseSAE。` |

## 3. 本步排除的错误跳步

```text
错误：LowMod endpoint CRTDefect 出现 => 当前 PDEC 候选为零 => 矛盾。
正确：LowMod endpoint CRTDefect 出现 => future explicit PDEC schema 或 sparse SAE。
```

当前 PDEC family 边界只清零现有已物化候选；反例假设若产生新的 LowMod formal unit，
仍必须提交同 formal unit、非二点、二秩以上、cap-stable 的完整字段，然后再证明 `U_CRT<L_PDEC`。

## 4. 新最窄剩余

```text
LowModFuturePDECSchemaExclusionOrSparseSAE
  = PersistentLowModPrimitivePDECSchemaAdmission
    AND PersistentLowModPDECInequality_UCRT_LT_LPDEC
    AND SparseLowModSAELocalSurvivorExclusion
    AND LowRankOrColumnDisplacementAbsorption
    AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance.
```

这一步仍不是无条件闭合；它把 LowMod 分支从泛称出口压成 future PDEC schema 与 sparse SAE 两个可验收输入。
