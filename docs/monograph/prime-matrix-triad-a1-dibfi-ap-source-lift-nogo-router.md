# Triad-A1 DI/BFI APSourceLift no-go 路由器

**状态：** `ap_source_lift_rejected_new_full_s_theorem_input_open`

`APSourceLift` 被当前分支定义和对象账本阻断：AP-source 只能作为上游源等式分支使用，non-AP generic WFD 补集不能无损回提为 BFI prime-AP discrepancy。剩余单点压成 `NewFullSTheoremInput`。

## 1. 结构律

APSourceLift is not an estimate; it is a source-level reclassification. The AP branch is legal only when the clean residual is declared before Cauchy/dispersion as a BFI prime-AP discrepancy with matching main term and coefficients. The non-AP generic WFD branch is the complement: its object ledger removes APErrorRepresentation and leaves only uncentered WFD-to-KE13 no-projection identities. SOURCE-CEN and BD-CEN block the free centering/projection shortcut. Therefore the current contracts reject a silent lift from non-AP WFD back to AP-source.

```text
previous terminal:
  NewFullSTheoremInputOrAPSourceLift;

rejected:
  ['APSourceLift'];

new terminal:
  NewFullSTheoremInput;

expansion:
  ['NewFullSTheoremInput'].
```

## 2. 汇总

- `ap_source_lift_available=false`。
- `ap_source_lift_rejected=true`。
- `closed_nogo_gates=['PriorDualGapContainsAPSourceLift', 'ExplicitAPNonAPDichotomy', 'SourceIdentityRequiredAndStillMissing', 'TransferScaleDoesNotProvideAPRepresentation', 'NonAPObjectLedgerRemovesAPError', 'ProjectionCenteringShortcutBlocked', 'APSourceLiftRejected']`。
- `open_terminal_gates=['NewFullSTheoremInput']`。
- `terminal_gap_after_router=NewFullSTheoremInput`。

## 3. No-go 账本表

| gate | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- |
| `PriorDualGapContainsAPSourceLift` | `true` | previous=NewFullSTheoremInputOrAPSourceLift; open=['NewFullSTheoremInput', 'APSourceLift'] | none at previous-frontier level | `APSourceLift` |
| `ExplicitAPNonAPDichotomy` | `true` | AP-source branch is closed only when source identity is declared upstream; open_branches=['NonAPSourceGenericWFD']. | non-AP branch is the complement, not an implicit AP branch. | `NoSilentAPUpgrade` |
| `SourceIdentityRequiredAndStillMissing` | `true` | AP identity open_gates=['UpstreamCleanA1ResidualDefinition', 'MainTermAndCoefficientMatch']; NoDownstreamBackProjectionShortcut is closed. | APSourceLift would have to add a new upstream source identity. | `NewSourceIdentityOrNewFullSTheoremInput` |
| `TransferScaleDoesNotProvideAPRepresentation` | `true` | open_transfer_gates=['APErrorRepresentation', 'DispersionCauchyNoCenteringIdentity', 'KE13DyadicExhaustionNoProjection'] | APErrorRepresentation remains an open transfer gate, not a proved lift. | `NewSourceIdentityOrNewFullSTheoremInput` |
| `NonAPObjectLedgerRemovesAPError` | `true` | removed=['APErrorRepresentation']; terminal=UncenteredWFDToKE13NoProjectionIdentity | non-AP object side is uncentered WFD-to-KE13 no-projection identity. | `NewFullSTheoremInput` |
| `ProjectionCenteringShortcutBlocked` | `true` | SOURCE-CEN and BD-CEN block free centering/projection/back-projection. | no silent route from non-AP WFD object to prime-AP discrepancy. | `NewFullSTheoremInput` |
| `APSourceLiftRejected` | `true` | A lift from the declared non-AP generic WFD complement to AP-source would contradict the current branch split unless a new source identity theorem is added. | APSourceLift is rejected under the current contracts. | `NewFullSTheoremInput` |
| `NewFullSTheoremInput` | `false` | No current DI/BFI primary-source theorem covers the full-S non-AP WFD kernel. | 需要新增 full-S 外部深定理或新解析证明。 | `NewFullSTheoremInput` |

## 4. 当前结论

双点剩余已被压成单点：

```text
rejected:
  APSourceLift;

still open:
  NewFullSTheoremInput.
```

这不是行命题完全闭合；它说明若不接受 FullS-KLS-ext 外部合同版，完全自足/主来源逐项版仍需要新的 full-S 定理输入或新证明。
