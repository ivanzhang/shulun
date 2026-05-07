# Prime Matrix 行列无条件自足前沿路由器

**状态：** `row_column_unconditional_frontier_routed_not_closed`

行列无条件自足版尚未闭合。已闭合的是 canonical-source Triad-A1 边界；已排除的是 unrestricted generic WFD 自足版；当前已审计 FO-PDEC ell=199 强信号链已经依次通过嵌套重复、weighted Hall、cross-q 坐标图、physical 二点 tautology 和二点 SAE/Endpoint 本地 witness 吸收；已物化 LocalSurvivor/SAE 包总账也全部闭合。已知 LocalSurvivor packet extractor 入口也全部覆盖，且无未命名新 sparse 入口。CleanKLS/DLS 宽口径已由现有路由压到 NC-BLK，并已通过边界核查消除无名出口歧义。非二点 PDEC 准入审计确认当前已物化合法候选为 0。下一步应攻全局终端家族的普遍生成/排斥，而不是继续复用当前已耗尽的局部样本。

## 1. 总裁定

```text
row_column_unconditional_closed: false
canonical_source_boundary_closed: true
generic_unrestricted_self_contained_refuted: true
terminal_triad_routed_no_fourth_exit: true
```

## 2. 前沿门控表

| gate | status | evidence | remaining | next action |
| --- | --- | --- | --- | --- |
| CanonicalSourceSelfContainedBoundary | closed | CANONICAL_SOURCE_BOUNDARY_MERGED_NO_GLOBAL_OVERCLAIM | 无 theorem-boundary 剩余；只限 canonical RIW/Buchstab source branch。 | 保持边界，不把它升级成完整行列无条件定理。 |
| UnrestrictedGenericWFD | refuted_not_claimed | Unrestricted generic full-S well-factorable WFD self-contained theorem. | 不得作为自足闭合路线继续使用。 | 禁止回到 generic full-S WFD 自足版。 |
| TerminalTriadNoFourthExit | routed_not_closed | A1 当前所有物化分支已汇合到终端三证书接口，且当前 P×P 早期出口已关闭。这仍不是最终行命题证明；剩余是三终端证书全集，首要是 PDEC 同集容量上界。 | 三终端证书全集仍未提交。 | 只在 PDEC / LocalSurvivor / CleanKLS 三终端内继续推进。 |
| A:PDECFamily | open_terminal | A:PDEC family same-set capacity upper U_CRT<L_PDEC. | explicit/profinite/weighted/primitive/cofactor/displacement/gcd-stratum 全部需要 U_CRT<L_PDEC 或回流。 | 优先攻同一 formal unit 的 PDEC 合法性和容量上界。 |
| A1-FO-PDEC-SameFormalUnit | current_materialized_nontautological_pdec_absent_global_family_open | raw ell=199, h=95, Fourier=3.959247567099438; coordinate-cap Fourier=2.9698366905785227; physical-cap Fourier=1.9997507790353146; q-row dedup best=1.0; block-local best=1.0; nested_unit_blocked=True; weighted_full_duplicate_blocked=True; cross_q_chart_overlap_blocked=True; physical_two_point_tautology=True; two_atom_sae_endpoint_absorbed=True | 当前已审计 FO-PDEC 样本链中，raw、coordinate-cap、physical 二点阈值和二点 SAE/Endpoint 均已被降口径或本地 witness 吸收；非二点 PDEC 准入审计进一步确认当前已物化的合法非二点 primitive PDEC 候选数为 0。但完整 PDEC family 对未来非二点、非同图重叠 formal unit 仍未闭合。 | 停止优化当前 U_CRT 常数；若未来出现新 PDEC 候选，必须先通过同 formal unit、三物理原子、非 tautology、非图重叠和非 SAE witness 的准入门。 |
| B:LocalSurvivorFamily | materialized_packets_closed_global_generation_open | materialized_packets=9; witnesses=5; open_materialized=0; known_extractors_covered=True; no_new_sparse_entry=True | 当前已物化 LocalSurvivor/SAE 包全部闭合；全局剩余是 packet-generation：已知入口 extractor 均覆盖；当前也不存在未命名新 sparse 入口。未来若新增显式 sparse 路线，必须提交同类 extractor。 | LocalSurvivor 当前分支转为条件闭合；主攻非二点 PDEC 或 CleanKLS/DLS。 |
| C:CleanKLS-DLS | ncblk_reconciled_with_boundary_global_family_open | clean_admission=KuznetsovLSAtomSC9OrExternalCitation; sc9_frontier=NCBLKOrExternalDIBFIOriginalDispersion; ncblk_reconciled=True | CleanKLS 宽口径已收缩并核查边界：canonical-source 分支中的 NC-BLK 已由既有同集容量边界吸收；generic full-S non-AP 分支仍是外部/精确源熵路线，不能冒充自足闭合。 | 不再把 NC-BLK 当无名出口；剩余提升只能来自全局终端家族排斥或外部/referee 接口。 |
| D-structure/Tail-log4/RankinReferee | referee_block_guarded | PM-16 保持 BLOCK-REFEREE；主稿保留 D-structure/Tail-log4/Rankin 边界。 | 独立接受 D-structure/Tail-log4/finite Rankin 接口前不能升级全局定理。 | 与三终端并行保持为最终晋级输入，不得由 A1 边界替代。 |
| ClaimStatusDiscipline | guarded | claim-status table records boundary merge and remaining global obligations. | 状态表必须继续区分已闭合边界、已反证分支和未闭合全局命题。 | 本路由器归档后补入状态表和合著总览。 |

## 3. 当前最窄硬点

```text
name: CurrentMaterializedFrontierExhausted_GlobalTerminalFamiliesOpen
subgate_closed_this_round: NoCurrentMaterializedNonTautologicalPDECAndNCBLKReconciled
raw_best: {'factor': 199, 'frequency': 95, 'fourier': 3.959247567099438, 'mass': 4, 'support': 3, 'residues': [{'residue': 40, 'load': 2}, {'residue': 126, 'load': 1}, {'residue': 61, 'load': 1}]}
coordinate_cap_best: {'factor': 199, 'fourier': 2.9698366905785227, 'frequency': 95, 'mass': 3, 'support': 3, 'top_residues': [{'load': 1, 'residue': 40}, {'load': 1, 'residue': 126}, {'load': 1, 'residue': 61}]}
physical_cap_best: {'factor': 199, 'fourier': 1.9997507790353146, 'frequency': 81, 'mass': 2, 'support': 2, 'top_residues': [{'load': 1, 'residue': 40}, {'load': 1, 'residue': 126}]}
```

PDEC 是三终端中最直接连接 A1 已闭合边界的端口；当前已审计 FO-PDEC 强信号链已被逐层降口径，最后两个物理原子由同固定偏移纤维的本地素数见证吸收；已物化 LocalSurvivor/SAE 包总账也无开放窗口；已知 packet extractor 入口全覆盖，且无未命名新 sparse 入口。LocalSurvivor 当前分支只剩未来显式新增入口的条件义务；CleanKLS/DLS 宽口径已由 K1--K9 准入和 SC-9 展开压成 NC-BLK，并由边界核查说明 canonical-source 分支已吸收、generic 分支仍外部化；非二点 PDEC 准入审计也确认当前已物化合法候选为 0。因此当前没有新的已物化终端硬点可继续局部消元；真正剩余上升为全局终端家族的普遍生成/排斥，以及 D-structure/Rankin/referee 接口。

下一步只应在以下路线中择一推进：

- `prove a universal terminal-generation theorem that every future counterexample emits one of the existing certificate schemas`
- `prove global PDEC-family exclusion beyond the currently materialized zero-candidate frontier`
- `admit any future sparse route only with extractor schema and finite ledger`
- `settle D-structure/Rankin/referee interfaces before final theorem promotion`

## 4. 开放全局门

- `TerminalTriadNoFourthExit`
- `A:PDECFamily`
- `A1-FO-PDEC-SameFormalUnit`
- `B:LocalSurvivorFamily`
- `C:CleanKLS-DLS`
- `D-structure/Tail-log4/RankinReferee`
