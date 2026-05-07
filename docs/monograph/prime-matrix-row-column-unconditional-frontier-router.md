# Prime Matrix 行列无条件自足前沿路由器

**状态：** `row_column_unconditional_frontier_routed_not_closed`

行列无条件自足版尚未闭合。已闭合的是 canonical-source Triad-A1 边界；已排除的是 unrestricted generic WFD 自足版；当前已审计 FO-PDEC ell=199 强信号链已经依次通过嵌套重复、weighted Hall、cross-q 坐标图、physical 二点 tautology 和二点 SAE/Endpoint 本地 witness 吸收；已物化 LocalSurvivor/SAE 包总账也全部闭合。下一步应攻 LocalSurvivor packet-generation 定理，或寻找未来非二点 primitive PDEC formal unit。

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
| A1-FO-PDEC-SameFormalUnit | audited_current_sample_subgates_closed_global_family_open | raw ell=199, h=95, Fourier=3.959247567099438; coordinate-cap Fourier=2.9698366905785227; physical-cap Fourier=1.9997507790353146; q-row dedup best=1.0; block-local best=1.0; nested_unit_blocked=True; weighted_full_duplicate_blocked=True; cross_q_chart_overlap_blocked=True; physical_two_point_tautology=True; two_atom_sae_endpoint_absorbed=True | 当前已审计 FO-PDEC 样本链中，raw、coordinate-cap、physical 二点阈值和二点 SAE/Endpoint 均已被降口径或本地 witness 吸收；但完整 PDEC family 对未来非二点、非同图重叠 formal unit 仍未闭合。 | 停止优化当前 U_CRT 常数；转向 packet-generation，或寻找至少三点非退化 primitive PDEC formal unit。 |
| B:LocalSurvivorFamily | materialized_packets_closed_global_generation_open | materialized_packets=9; witnesses=5; open_materialized=0 | 当前已物化 LocalSurvivor/SAE 包全部闭合；全局剩余是 packet-generation：证明任意未来 sparse escape 必物化为同类有限包或持久化为 PDEC/ColumnCRT/CleanKLS。 | 攻 LocalSurvivor packet-generation theorem，禁止在已闭合物化包上重复找缺口。 |
| C:CleanKLS-DLS | open_terminal_or_external | C:CleanKLS/DLS admission plus large-sieve or explicit external input. | 所有 clean residual 仍需内部大筛证书或明确 ExternalKLS 输入。 | 只有在 PDEC/SAE/column/tail/fiber 峰全部剥离后才调用。 |
| D-structure/Tail-log4/RankinReferee | referee_block_guarded | PM-16 保持 BLOCK-REFEREE；主稿保留 D-structure/Tail-log4/Rankin 边界。 | 独立接受 D-structure/Tail-log4/finite Rankin 接口前不能升级全局定理。 | 与三终端并行保持为最终晋级输入，不得由 A1 边界替代。 |
| ClaimStatusDiscipline | guarded | claim-status table records boundary merge and remaining global obligations. | 状态表必须继续区分已闭合边界、已反证分支和未闭合全局命题。 | 本路由器归档后补入状态表和合著总览。 |

## 3. 当前最窄硬点

```text
name: LocalSurvivorPacketGenerationOrNonTautologicalPDEC
subgate_closed_this_round: MaterializedLocalSurvivorPacketsExhausted
raw_best: {'factor': 199, 'frequency': 95, 'fourier': 3.959247567099438, 'mass': 4, 'support': 3, 'residues': [{'residue': 40, 'load': 2}, {'residue': 126, 'load': 1}, {'residue': 61, 'load': 1}]}
coordinate_cap_best: {'factor': 199, 'fourier': 2.9698366905785227, 'frequency': 95, 'mass': 3, 'support': 3, 'top_residues': [{'load': 1, 'residue': 40}, {'load': 1, 'residue': 126}, {'load': 1, 'residue': 61}]}
physical_cap_best: {'factor': 199, 'fourier': 1.9997507790353146, 'frequency': 81, 'mass': 2, 'support': 2, 'top_residues': [{'load': 1, 'residue': 40}, {'load': 1, 'residue': 126}]}
```

PDEC 是三终端中最直接连接 A1 已闭合边界的端口；当前已审计 FO-PDEC 强信号链已被逐层降口径，最后两个物理原子由同固定偏移纤维的本地素数见证吸收；已物化 LocalSurvivor/SAE 包总账也无开放窗口。下一硬点不再是已物化样本，而是 packet-generation 定理或未来非二点 primitive PDEC 家族。

下一步只应在以下路线中择一推进：

- `LocalSurvivor packet-generation theorem for unaudited sparse windows`
- `future primitive PDEC only if a same-formal-unit family has at least three non-tautological physical atoms or extra constraints`
- `CleanKLS/DLS and D-structure/Rankin referee inputs for final theorem promotion`

## 4. 开放全局门

- `TerminalTriadNoFourthExit`
- `A:PDECFamily`
- `A1-FO-PDEC-SameFormalUnit`
- `B:LocalSurvivorFamily`
- `C:CleanKLS-DLS`
- `D-structure/Tail-log4/RankinReferee`
