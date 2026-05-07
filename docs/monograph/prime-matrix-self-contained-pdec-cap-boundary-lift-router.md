# Prime Matrix PDEC-CAP 自足边界提升路由器

**状态：** `self_contained_pdec_cap_boundary_lifted_global_not_closed`

PDEC-CAP 的旧自足瓶颈已经完成边界提升：在 canonical-source 分支内，`PDEC_CAP_SameSetGlobalDualCertificate` 不再是开放硬点；最新剩余 `DIBFIQuantifiedNoProjectionWindowCertificate` 只属于 generic/external 原始 DI/BFI 路线。完整行/列无条件定理仍未闭合，剩余是全局终端家族晋级审查与 `DStructureRankinReferee`。

## 1. 提升律

The former self-contained PDEC-CAP bottleneck is closed only after restricting to the canonical RIW/Buchstab source branch and using the transverse source embedding plus canonical layer transfer. The remaining DIBFI gate is an external/generic branch, not a canonical-source self-contained gap. This does not close the full row/column theorem, because global terminal-family promotion and the D-structure/Rankin referee interface remain open.

```text
old self-contained bottleneck:
  PDEC_CAP_SameSetGlobalDualCertificate

after canonical-source lift:
  NoFurtherCanonicalSourceSelfContainedPDECCapGap

remaining outside that boundary:
  generic/external DI/BFI quantified no-projection certificate;
  global terminal-family promotion review;
  D-structure/Tail-log4/finite Rankin referee interface.
```

## 2. 汇总

- `closed_nonfinal_lift_gates=true`。
- `canonical_source_self_contained_pdec_bottleneck_closed=true`。
- `pdec_cap_same_set_global_dual_closed=false`。
- `generic_external_dibfi_boundary_open=true`。
- `d_structure_rankin_referee_open=true`。
- `row_column_unconditional_closed=false`。
- `narrowest_self_contained_boundary=NoFurtherCanonicalSourceSelfContainedPDECCapGap`。
- `narrowest_global_next_hardpoint=GlobalTerminalFamilyPromotionReview_OR_DStructureRankinReferee`。
- `external_next_hardpoint=DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY`。

## 3. 审查表

| gate | closed | blocks final | evidence | lifted meaning | boundary warning |
| --- | --- | --- | --- | --- | --- |
| `PreviousSelfContainedPDECBottleneckAccepted` | `true` | `false` | PDEC_CAP_SameSetGlobalDualCertificate | 上一层已经把 canonical-source 自足路线的独立数学瓶颈压到 PDEC-CAP。 | 这是旧瓶颈定位，不是最终全局定理。 |
| `CanonicalSourcePDECCapBranchClosed` | `true` | `false` | canonical=True; materialized=True | PDEC-CAP 内部的来源嵌入、横向商、canonical 层转移和已物化门控已经闭合。 | 闭合范围只限 canonical RIW/Buchstab source branch。 |
| `NoFurtherCanonicalSelfContainedPDECGate` | `true` | `false` | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY | 旧 `PDEC_CAP_SameSetGlobalDualCertificate` 不再是 canonical-source 自足分支的开门。 | `DIBFIQuantifiedNoProjectionWindowCertificate` 只属于 generic/external 原始 DI/BFI 路线。 |
| `GenericExternalDIBFIBoundarySeparated` | `true` | `false` | DIBFIQuantifiedNoProjectionWindowCertificate | 外部 DI/BFI 量化证书被保留为外部分支，不再污染 canonical-source 自足声明。 | 若要关闭 generic/external 版本，仍需提交无投影对象恒等式与量化尺度代入。 |
| `RowFrontierBoundaryDisciplinePreserved` | `true` | `false` | CurrentMaterializedFrontierExhausted_GlobalTerminalFamiliesOpen | 行列前沿仍区分已闭合 canonical 边界、已反证 generic 分支和未闭合全局命题。 | 不能把 PDEC-CAP 的 canonical 闭合升级为行/列无条件定理。 |
| `GlobalTerminalFamiliesStillOpen` | `false` | `true` | PDEC_CAP_OR_KLS_EXT_OR_REFEREE | 完整行/列命题仍需全局终端家族排斥或外部输入。 | PDEC、LocalSurvivor、CleanKLS/DLS 的全局生成/排斥仍是最终晋级前沿。 |
| `DStructureRankinRefereeStillOpen` | `false` | `true` | BLOCK-REFEREE | 最终定理升级仍需 D-structure/Tail-log4/finite Rankin 接口通过独立审稿。 | 该门不能由 A1/PDEC-CAP canonical 边界替代。 |

## 4. 下一步

下一步不再把 canonical-source 自足路线写成缺一个 PDEC-CAP 估计。真正剩余应分层处理：若坚持自足 canonical-source 分支，当前边界已经没有 PDEC-CAP 开门；若攻完整行/列无条件定理，则必须处理全局终端家族晋级和 D-structure/Rankin 审稿门；若攻 generic/external 版本，则另行提交 DI/BFI 无投影量化证书。
