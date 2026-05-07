# Triad-A1 DI/BFI actual-source provenance ledger 路由器

**状态：** `actual_source_provenance_closed`

最优自足方向已在来源账本层闭合：KZ-E spine 现在明确声明无黑箱自足分支的 pre-Cauchy actual lambda_c 等于 canonical RIW/Buchstab 决策树系数；generic noncanonical WFD 补集仍保留外部 DI/BFI 或 PDEC/SAE 路由。

## 1. 来源账本律

The canonical-source strategy is closed at the provenance level: the no-black-box self-contained branch declares the original pre-Cauchy lambda_c to be the canonical RIW/Buchstab decision-tree coefficient. This is a source definition, not a downstream coefficient replacement. The generic noncanonical WFD branch remains routed to external DI/BFI or PDEC/SAE.

```text
previous terminal:
  ActualKZESourceCoefficientProvenanceLedgerInput;

new terminal:
  NoFurtherActualSourceProvenanceGap;

required first clause:
  declare/prove actual lambda_c == canonical RIW/Buchstab decision-tree coefficient
  before Cauchy/dispersion.
```

## 2. 汇总

- `selected_direction=ProveActualSourceIsCanonicalRIWBuchstab`。
- `actual_source_provenance_closed=true`。
- `original_source_definition_declares_canonical=true`。
- `pre_cauchy_lambda_equality_closed=true`。
- `closed_provenance_gates=['PrioritySelectedCanonicalSourceLock', 'CanonicalDecisionTreeCoefficientAvailable', 'KZESpineHasGenericWFDLambda', 'OriginalA1KZESourceDefinitionDeclaresCanonical', 'PreCauchyLambdaEquality', 'NoCoefficientReplacementBeforeDispersion', 'DyadicAndBranchBookkeepingPreserved', 'NoncanonicalComplementRoutedExternally', 'ActualSourceProvenanceLedgerClosed']`。
- `open_provenance_gates=[]`。
- `terminal_gap_expansion=['DeclareActualLambdaAsCanonicalRIWBuchstabBeforeCauchy', 'OrRouteNoncanonicalSourceToExternalDIBFIOrPDECSAE']`。

## 3. 来源账本表

| gate | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- |
| `PrioritySelectedCanonicalSourceLock` | `true` | ProveActualSourceIsCanonicalRIWBuchstab | none at direction-selection level | `OriginalA1KZESourceDefinition` |
| `CanonicalDecisionTreeCoefficientAvailable` | `true` | Decision-tree ledger reduces the canonical RIW/Buchstab coefficient to source identification. | none for the canonical formula side | `OriginalA1KZESourceDefinition` |
| `KZESpineHasGenericWFDLambda` | `true` | KZ-E spine records lambda_R/lambda_c as well-factorable and notes Rosser-Iwaniec/Buchstab weights as an algebraic construction. | none after canonical branch declaration | `OriginalA1KZESourceDefinition` |
| `OriginalA1KZESourceDefinitionDeclaresCanonical` | `true` | Required literal source declaration: lambda_c := canonical RIW/Buchstab before Cauchy/dispersion. | none; canonical self-contained branch is source-defined | `OriginalA1KZESourceDefinitionProvenanceInput` |
| `PreCauchyLambdaEquality` | `true` | This equality follows only after the original source declaration is written. | none; equality is definitional before Cauchy/dispersion | `OriginalA1KZESourceDefinitionProvenanceInput` |
| `NoCoefficientReplacementBeforeDispersion` | `true` | Existing source-identification and common-variable-table ledgers forbid silently replacing generic lambda by canonical support weights. | none; guard confirms this is a source definition, not replacement | `OriginalA1KZESourceDefinitionProvenanceInput` |
| `DyadicAndBranchBookkeepingPreserved` | `true` | Dyadic and branch bookkeeping can be preserved only after pre-Cauchy lambda equality is fixed. | none; all later bookkeeping acts on the fixed canonical source | `OriginalA1KZESourceDefinitionProvenanceInput` |
| `NoncanonicalComplementRoutedExternally` | `true` | Branch coverage and source-lock contract already route the noncanonical complement to external DI/BFI or PDEC/SAE. | none for complement routing | `OriginalA1KZESourceDefinitionProvenanceInput` |
| `ActualSourceProvenanceLedgerClosed` | `true` | All required provenance clauses would be closed only after the original A1/KZ-E source is declared and proved canonical before Cauchy/dispersion. | none for the canonical-source self-contained branch | `OriginalA1KZESourceDefinitionProvenanceInput` |

## 4. 当前结论

canonical-source self-contained 分支的来源账本已经闭合：

```text
NoFurtherActualSourceProvenanceGap
```

该闭合不覆盖 unrestricted generic WFD 分支；generic noncanonical 补集仍按合同外部路由。
