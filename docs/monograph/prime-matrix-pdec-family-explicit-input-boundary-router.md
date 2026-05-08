# Prime Matrix PDEC Family 显式输入边界路由器

**状态：** `pdec_family_boundary_closed_current_frontier_zero_future_schema_required`

广义 PDEC family 的当前边界已闭合：当前已物化合法非二点 primitive PDEC 候选为零，canonical-source PDEC-CAP 已接回最终自足边界；未来若出现真正 PDEC 障碍，必须以显式 primitive 同 formal unit、二秩以上、cap-stable schema 进入。完整行/列无条件命题仍未闭合。

## 1. 边界律

PDEC family 不再是模糊终端输入。当前已物化 PDEC 候选已经耗尽；canonical-source PDEC-CAP 路线已经由横向来源嵌入和 canonical 层转移闭合；每一种 cap 失败、低秩、重复、二点、ColumnCRT、sparse 或 clean 残差都有命名回流。因此未来若出现 PDEC 障碍，必须作为显式 primitive 同 formal unit、二秩以上、cap-stable schema 引入。generic/external 分支已由 noncanonical 三歧包接管，最终定理晋级仍受 DStructure/Rankin 验收阻断。

```text
pdec_family_explicit_input_boundary_closed=true
current_materialized_pdec_frontier_closed=true
canonical_source_pdec_cap_closed=true
global_pdec_family_unconditional_closed=false
row_column_unconditional_closed=false
```

## 2. 审查表

| gate | closed | evidence | meaning | remaining |
| --- | --- | --- | --- | --- |
| `SAEIndependentTerminalRemoved` | `true` | SAE absorption router | 第一包当前只需处理广义 PDEC 与未来显式 sparse schema。 | PDEC boundary, future explicit sparse schema |
| `PersistentPDECAdmissionBoundary` | `true` | persistent terminal admission router | 裸持久签名、裸 ColumnCRT、对偶失败和口径错配都不能直接准入。 | primitive multi-atom same-formal-unit PDEC only |
| `NoCurrentMaterializedNonTautologicalCandidate` | `true` | non-tautological PDEC admission audit | 当前已物化前沿没有合法非二点 primitive PDEC 候选。 | future candidate must pass admission schema |
| `PrimitiveRankBoundary` | `true` | primitive multi-atom rank router | 零秩/一秩/二点/固定壳/ColumnCRT/cap 失败全部回流命名路线。 | rank >= 2 cap-stable primitive kernel |
| `RankTwoKernelInverseBoundary` | `true` | rank-two cap-stable kernel router | 二秩核不等式已逆否化为统一 cap-stability 证书。 | uniform cap stability certificate |
| `UniformCapFiniteBasis` | `true` | uniform cap finite basis router | 连续方向帽搜索压成有限循环弧 cap 质量界。 | finite cyclic-arc cap mass bounds |
| `FiniteArcNoUnnamedExit` | `true` | finite arc transverse router | 高质量有限弧若失败，回流 SAE/refined PDEC/ColumnCRT/CleanKLS。 | transverse fiber expansion or named return |
| `TransverseCleanReduction` | `true` | transverse clean reduction router | 横向非平坦缺陷全部命名；平坦残差只进入 clean 大筛原子。 | CleanKLS/SC-9 frontier |
| `CleanFrontierNamed` | `true` | transverse clean atom frontier router | clean 原子不是第四终端；自足入 canonical source，外部入 DI/BFI。 | canonical source transfer or external FullS-KLS/DI-BFI |
| `CanonicalPDECCapClosed` | `true` | canonical layer closure router | canonical-source 分支内的 PDEC-CAP 已经闭合到 A1 最终边界。 | generic/external branch only |
| `PDECBoundaryLifted` | `true` | self-contained PDEC-CAP boundary lift router | 旧 PDEC-CAP 自足瓶颈已提升；全局终端家族仍不是无条件闭合。 | global family promotion / final inputs |
| `GenericExternalBranchAccounted` | `true` | noncanonical complement trilemma | generic/external 分支已归入第二包三歧输入。 | source identity, strengthened anti-atom, or FullS-KLS-ext |
| `FinalPromotionAccounted` | `true` | DStructure/Rankin promotion acceptance router | 最终晋级门已命名但未独立接受。 | DStructure/Rankin independent acceptance |

## 3. 未来 PDEC schema 准入条件

- 同一个 formal unit，且只有一个固定 phase map
- 全部去重后至少有三个物理 primitive 原子
- 不是二点 Fourier tautology
- 不是尚未吸收的 ColumnCRT/displacement
- 商去 shell/column 退化后秩至少为 2
- 对每个有限循环弧 localization 都 cap-stable
- 横向支撑既非 sparse，也非持久偏斜，也未进入 clean 外部化

## 4. PDEC 边界后的剩余

- `若未来引入真正可准入的 PDEC family，必须提交 FutureExplicitPrimitivePDECSchema`
- `generic/external 分支进入 NoncanonicalFullSComplementTrilemma 输入`
- `最终定理晋级需要 DStructureRankinPromotion 独立接受`

## 5. 判定

这一步不声称全局 PDEC family 已无条件排斥；它把 PDEC 从泛称终端改写为显式准入 schema。当前材料中已经物化的 PDEC 候选全部清零，canonical-source PDEC-CAP 也已经闭合。未来任何新 PDEC 必须先提交同 formal unit、三物理原子以上、非二点 tautology、二秩以上、cap-stable 且未被 sparse/ColumnCRT/CleanKLS 吸收的完整证书字段。
