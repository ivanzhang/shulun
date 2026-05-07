# Triad-A1 PhaseResidue 完整 CRT 终端审计

**状态：** `phase_residue_atoms_expanded_to_full_crt_terminal_rows`

当前已有下一层数据的 phase-residue 原子全部可展开为完整 CRT 零行相位，且所有终端相位均大于 P^2；它们不能形成 P 行以内零行，只能作为远处 finite/profinite PDEC 数据包。

## 1. 结构律

对每个已有下一层数据的互信息原子，先把每个非零下一 residue 写成相位 v，再枚举剩余高素 CRT 偏移。展开计数必须等于记录的 M(v)；展开得到的相位都是完整 CRT 零行相位。

```text
atom u at Q'；
next residue phase v=u+sQ'；
terminal phase w=v+y*nextQ；
completion_count(v)=#{y: w 是完整 CRT 零行相位}。
```

## 2. 汇总

- `rows_with_next_count=12`。
- `source_route_counts={'NextLayerCleanFiberCandidate': 6, 'NextLayerRefinedPDECEntropy': 6}`。
- `route_counts={'FullCRTTerminalFarBeyondPxP': 12}`。
- `all_terminal_mass_identities_hold=True`。
- `all_residue_mass_identities_hold=True`。
- `all_terminal_phases_gt_p=True`。
- `all_terminal_phases_gt_p2=True`。
- `min_terminal_phase=3659`。
- `min_terminal_phase_over_p=192.579`。
- `min_terminal_phase_over_p2=10.1357`。

## 3. 原子级明细

| P | source route | Q' | next Q | u | terminal count | min terminal | max terminal | route |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 19 | `NextLayerCleanFiberCandidate` | 30030 | 510510 | 23211 | 17 | 23211 | 503691 | `FullCRTTerminalFarBeyondPxP` |
| 19 | `NextLayerCleanFiberCandidate` | 30030 | 510510 | 6820 | 17 | 6820 | 487300 | `FullCRTTerminalFarBeyondPxP` |
| 19 | `NextLayerCleanFiberCandidate` | 30030 | 510510 | 26372 | 17 | 26372 | 506852 | `FullCRTTerminalFarBeyondPxP` |
| 19 | `NextLayerCleanFiberCandidate` | 30030 | 510510 | 3659 | 17 | 3659 | 484139 | `FullCRTTerminalFarBeyondPxP` |
| 19 | `NextLayerCleanFiberCandidate` | 30030 | 510510 | 9981 | 17 | 9981 | 490461 | `FullCRTTerminalFarBeyondPxP` |
| 19 | `NextLayerCleanFiberCandidate` | 30030 | 510510 | 20050 | 17 | 20050 | 500530 | `FullCRTTerminalFarBeyondPxP` |
| 23 | `NextLayerRefinedPDECEntropy` | 30030 | 510510 | 21709 | 35 | 81769 | 9451129 | `FullCRTTerminalFarBeyondPxP` |
| 23 | `NextLayerRefinedPDECEntropy` | 30030 | 510510 | 8322 | 35 | 248562 | 9617922 | `FullCRTTerminalFarBeyondPxP` |
| 23 | `NextLayerRefinedPDECEntropy` | 30030 | 510510 | 16322 | 35 | 466772 | 9685982 | `FullCRTTerminalFarBeyondPxP` |
| 23 | `NextLayerRefinedPDECEntropy` | 30030 | 510510 | 12239 | 35 | 42269 | 9681899 | `FullCRTTerminalFarBeyondPxP` |
| 23 | `NextLayerRefinedPDECEntropy` | 30030 | 510510 | 17792 | 35 | 17792 | 9657422 | `FullCRTTerminalFarBeyondPxP` |
| 23 | `NextLayerRefinedPDECEntropy` | 30030 | 510510 | 13709 | 35 | 13709 | 9232919 | `FullCRTTerminalFarBeyondPxP` |

## 4. 读法

这一步同时处理上一账本中的 `NextLayerCleanFiberCandidate` 与 `NextLayerRefinedPDECEntropy`。
两类在当前已有下一层数据时都已展开为完整 CRT 零行相位，并且全部远离 `P×P` 早期区域。
剩余 `NoNextLayerDataProfiniteObligation` 仍需在更高层按同一规则处理，不能视为已排除。
