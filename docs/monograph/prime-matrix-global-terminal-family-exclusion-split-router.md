# Prime Matrix 全局终端家族排斥拆分路由器

**状态：** `global_terminal_family_exclusion_reduced_not_closed`

全局终端家族排斥已经进一步拆窄：LocalSurvivor 当前与已知入口不再构成独立终端，NC-BLK 不再构成独立终端，连续终端二分把所有剩余质量送入 PDEC-CAP 或 CleanKLS/DLS。因此完全自足路线的真实剩余是 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve`；若允许外部/审稿输入，还需 `KLS_EXT` 与 `DStructureRankinReferee`。完整行/列定理仍未闭合。

## 1. 拆分律

After the current materialized frontier is exhausted, the terminal family problem has no independent fourth route and no independent current LocalSurvivor or NC-BLK blocker. The finite-projection dichotomy sends positive-limsup terminal mass to PDEC-CAP and diffuse terminal mass to CleanKLS/DLS. Therefore the self-contained mathematical remainder is exactly PDEC-CAP or internal CleanKLS large-sieve; final promotion additionally needs the D-structure/Rankin referee interface.

```text
GlobalTerminalFamilyExclusionCertificates
  => no fourth terminal route;
  => current LocalSurvivor / NC-BLK are not independent blockers;
  => positive-limsup finite signature -> PDEC-CAP;
  => diffuse finite signatures -> CleanKLS/DLS;
  => final theorem promotion still needs D/Rankin referee acceptance.
```

## 2. 汇总

- `closed_nonfinal_reductions=true`。
- `global_terminal_family_exclusion_closed=false`。
- `row_column_unconditional_closed=false`。
- `narrowest_next_hardpoint=PDEC_CAP_OR_KLS_EXT_OR_REFEREE`。
- `self_contained_next_hardpoint=PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve`。

## 3. 拆分表

| gate | closed | blocks final | evidence | reduction | next action |
| --- | --- | --- | --- | --- | --- |
| `MaterializedFrontierAlreadyExhausted` | `true` | `false` | name=CurrentMaterializedFrontierExhausted_GlobalTerminalFamiliesOpen; subgate=NoCurrentMaterializedNonTautologicalPDECAndNCBLKReconciled | 不再存在当前样本层可继续局部消元的 PDEC/LocalSurvivor/NC-BLK 对象。 | 进入全局家族证书，不再优化当前 ell=199 或旧 NC-BLK 标签。 |
| `TerminalSchemaNoFourthExit` | `true` | `false` | Terminal Triad Reduction | 任何最小反例终端对象只能是 PDEC、LocalSurvivor 或 CleanKLS/DLS。 | 只允许在三类证书内继续推进。 |
| `LocalSurvivorNoIndependentGlobalBlocker` | `true` | `false` | open_materialized=0; missing_extractors=0; missing_admission=0; frontier_status=materialized_packets_closed_global_generation_open | 当前孤窗包与已知入口均闭合；未来 sparse 路线若复现则回 PDEC，若升层逃逸则进 CleanKLS/DLS。 | 未来新增 sparse 路线必须同时提交 extractor schema 与有限账本。 |
| `ContinuousTerminalDichotomy` | `true` | `false` | PDEC-CAP: prove the resulting column-tail PDEC capacity inequality U_CRT<L_PDEC; KLS-EXT: prove or import the CleanKLS/DLS large-sieve bound for diffuse payment measures | 正 limsup 有限签名给 PDEC 输入；全部有限签名消散给 L2-flat CleanKLS/DLS 输入。 | 剩余只攻 PDEC-CAP 或 KLS-EXT。 |
| `NCBLKNoIndependentGlobalBlocker` | `true` | `false` | ncblk_reconciled=True; frontier_status=ncblk_reconciled_with_boundary_global_family_open | canonical-source NC-BLK 已吸收；generic NC-BLK 保持外部/精确源熵路线。 | 不再把 NC-BLK 当成新的内部终端家族。 |
| `PDEC_CAP` | `false` | `true` | triad_a1_capacity_upper_route_not_closed | PDEC 家族排斥等价于同一坏窗集合上的 U_CRT<L_PDEC 容量证书。 | 提交全局 LP/对偶容量证书，或把失败 DualCap 回流到 LocalSurvivor/CleanKLS。 |
| `KLS_EXT_OR_INTERNAL_LARGE_SIEVE` | `false` | `true` | cleankls_reduced_to_flat_large_sieve_certificate_or_pdec_not_closed | CleanKLS/DLS 家族排斥等价于内部大筛界，或明确外部 KLS/DI/BFI 输入。 | 证明 L2-flat clean residual 的大筛吸收，或逐项登记外部定理变量适配。 |
| `DStructureRankinReferee` | `false` | `true` | BLOCK-REFEREE | 最终升级仍需 D-structure/Tail-log4/finite Rankin 接口被独立接受。 | 保持为最终晋级门，不由三终端局部边界替代。 |

## 4. 结论边界

本路由器关闭的是“全局终端家族剩余仍含未命名或局部样本硬点”的可能。它没有关闭 `PDEC-CAP`、`CleanKLS/DLS` 大筛估计或 `D/Rankin` 审稿门；因此不能把完整行/列无条件命题标为已证。
