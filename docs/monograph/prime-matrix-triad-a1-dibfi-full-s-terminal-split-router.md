# Triad-A1 DI/BFI full-S terminal split 路由器

**状态：** `full_s_external_contract_closed_self_contained_antiatom_input_open`

full-S 终端已拆分：外部合同版由 `FullS-KLS-ext` 闭合；完全自足/主来源逐项版只剩 `NewFullSNonAPSourceAntiAtomTheoremInput`。

## 1. 版本边界

- `external_contract_version_closed=true`。
- `self_contained_version_closed=false`。
- `external_contract=FullS-KLS-ext`。
- `self_contained_boundary=External-contract version may accept FullS-KLS-ext. Fully self-contained or primary-source-specialized version still needs a new source anti-atom theorem.`。

## 2. 结构律

The current full-S terminal is no longer a hidden structural ambiguity. If FullS-KLS-ext is accepted as an external theorem, the external branch is closed. If the proof must be self-contained or derived from existing DI/BFI primary sources, the only remaining input is a new anti-atom theorem for the final full-S non-AP source measure.

```text
previous terminal:
  FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov;

new self-contained terminal:
  NewFullSNonAPSourceAntiAtomTheoremInput;

expansion:
  ['NewFullSNonAPSourceAntiAtomTheoremInput'].
```

## 3. 汇总

- `closed_split_gates=['PriorSourceAntiAtomTerminalPinned', 'ExternalFullSKLSExtContractAvailable', 'PrimarySourceSpecializationRejected', 'APSourceLiftRejected', 'SourceAntiAtomIsNewTheoremInput', 'TerminalSplitClosedAtRoutingLevel']`。
- `open_split_gates=['NewFullSNonAPSourceAntiAtomTheoremInput']`。
- `terminal_gap_after_router=NewFullSNonAPSourceAntiAtomTheoremInput`。

## 4. 路由账本表

| gate | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- |
| `PriorSourceAntiAtomTerminalPinned` | `true` | previous terminal=FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov; open=['FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov']. | none at previous-frontier level | `ExternalContractOrSelfContainedInputSplit` |
| `ExternalFullSKLSExtContractAvailable` | `true` | FullS-KLS-ext is already materialized as an external theorem contract for the current uncentered no-projection full-S non-AP WFD object. | closed only for the external-theorem version | `ExternalContractVersionClosed` |
| `PrimarySourceSpecializationRejected` | `true` | Existing DI/BFI primary sources do not imply the custom full-S KLS-ext theorem. | no primary-source self-contained derivation is available | `NewFullSSourceAntiAtomTheoremInput` |
| `APSourceLiftRejected` | `true` | APSourceLift was rejected; non-AP full-S WFD cannot return to the AP-source BFI branch. | no AP lift shortcut remains | `NewFullSSourceAntiAtomTheoremInput` |
| `SourceAntiAtomIsNewTheoremInput` | `true` | Since formal WFD/K4/K6/incidence/canonical shortcuts are blocked and AP lift is rejected, the strengthened anti-atom contract is a genuinely new source theorem input. | prove or assume this new source theorem for the self-contained route | `NewFullSNonAPSourceAntiAtomTheoremInput` |
| `TerminalSplitClosedAtRoutingLevel` | `true` | The full-S branch is now separated into external-contract closure and self-contained new-input obligation. | none at split-definition level | `NewFullSNonAPSourceAntiAtomTheoremInput` |
| `NewFullSNonAPSourceAntiAtomTheoremInput` | `false` | The repository still lacks a proof of the source anti-atom theorem for the final full-S non-AP WFD capacity measure. | prove this new anti-atom theorem, or explicitly accept FullS-KLS-ext as external input | `NewFullSNonAPSourceAntiAtomTheoremInput` |

## 5. 当前结论

若接受外部深定理合同，full-S non-AP 分支由 `FullS-KLS-ext` 关闭。
若要求完全自足或现有 DI/BFI 主来源逐项推出，唯一剩余为：

```text
NewFullSNonAPSourceAntiAtomTheoremInput
```

这一步不宣称自足闭合；它把外部合同版与自足版边界固定下来。
