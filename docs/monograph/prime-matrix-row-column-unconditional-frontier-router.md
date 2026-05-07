# Prime Matrix 行列无条件自足前沿路由器

**状态：** `row_column_unconditional_frontier_routed_not_closed`

行列无条件自足版尚未闭合。已闭合的是 canonical-source Triad-A1 边界；已排除的是 unrestricted generic WFD 自足版；当前最窄硬点是 A:PDEC 端口内同一 formal unit 的 FO-PDEC 合法性。嵌套块单位重复本轮已被支配审计阻断，下一步应攻 fractional Weighted Hall dual，或把重复坐标商掉并回流 primitive PDEC/SAE。

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
| A1-FO-PDEC-SameFormalUnit | current_narrowest_open | raw ell=199, h=95, Fourier=3.959247567099438; q-row dedup best=1.0; block-local best=1.0; nested_unit_blocked=True | global_library_raw 强阈值尚未是单分支 PDEC 下界；嵌套单位重复已被坐标支配，仍剩 fractional weighted dual、primitive 阈值、SAE/Endpoint 或 cross-q persistence。 | 先证明 fractional Weighted Hall dual；若失败，坐标商掉 exact duplicates，转攻 primitive PDEC 或 SAE/Endpoint 吸收。 |
| B:LocalSurvivorFamily | open_terminal | B:LocalSurvivor witness/blocker-deficit certificates for sparse packets. | 所有 sparse/孤窗候选集仍需 witness 或 blocker 覆盖不足证书。 | 接收 PDEC 失败后的稀疏重复、Endpoint 和短弧对象，逐窗给 witness/deficit。 |
| C:CleanKLS-DLS | open_terminal_or_external | C:CleanKLS/DLS admission plus large-sieve or explicit external input. | 所有 clean residual 仍需内部大筛证书或明确 ExternalKLS 输入。 | 只有在 PDEC/SAE/column/tail/fiber 峰全部剥离后才调用。 |
| D-structure/Tail-log4/RankinReferee | referee_block_guarded | PM-16 保持 BLOCK-REFEREE；主稿保留 D-structure/Tail-log4/Rankin 边界。 | 独立接受 D-structure/Tail-log4/finite Rankin 接口前不能升级全局定理。 | 与三终端并行保持为最终晋级输入，不得由 A1 边界替代。 |
| ClaimStatusDiscipline | guarded | claim-status table records boundary merge and remaining global obligations. | 状态表必须继续区分已闭合边界、已反证分支和未闭合全局命题。 | 本路由器归档后补入状态表和合著总览。 |

## 3. 当前最窄硬点

```text
name: A1-FO-PDEC-SameFormalUnit
subgate_closed_this_round: NestedBlockFullMultiplicityRejectedForAuditedFO-PDEC
raw_best: {'factor': 199, 'frequency': 95, 'fourier': 3.959247567099438, 'mass': 4, 'support': 3, 'residues': [{'residue': 40, 'load': 2}, {'residue': 126, 'load': 1}, {'residue': 61, 'load': 1}]}
```

PDEC 是三终端中最直接连接 A1 已闭合边界的端口；但 U_CRT 常数比较必须先在同一 formal unit 上合法。

下一步只应在以下路线中择一推进：

- `fractional Weighted Hall dual independence`
- `coordinate quotient / primitive PDEC threshold`
- `exact duplicate SAE/Endpoint absorption`
- `cross-q persistence theorem or cross-level reuse rejection`

## 4. 开放全局门

- `TerminalTriadNoFourthExit`
- `A:PDECFamily`
- `A1-FO-PDEC-SameFormalUnit`
- `B:LocalSurvivorFamily`
- `C:CleanKLS-DLS`
- `D-structure/Tail-log4/RankinReferee`
