# Triad-A1 Canonical Layer Transfer 路由审计

**状态：** `layer_transfer_reduced_to_selector_retention_or_clean_return`

exact 层承认、非零转移与薄块回流已被压成一个更尖锐的合同：先固定 alpha/delta 的 canonical 系数公式；随后非零转移按定义闭合；真正需要证明的是 selector 在每个 clean 厚块中至少保留 log-power 比例的 Buchstab 支撑，否则该块必须从 clean 分支退出到 edge/PDEC/SAE。

## 1. 选择器保留律

Layer admission and nonzero transfer should not be treated as two mysterious analytic estimates. Once the exact canonical coefficient formula is fixed, admission can be defined by nonzero coefficient support. The only real quantitative obligation is selector retention: the canonical selector must retain a log-power fraction of the raw thick Buchstab support in every clean block; if it does not, that block must be rejected into an existing edge/PDEC/SAE exit.

```text
raw thick Buchstab support >= interval/log^E;
canonical selector retains >= log^-R of that support;
if E+R <= C, retained nonzero coefficients >= interval/log^C;
if selector retention fails, the block must return to edge/PDEC/SAE.
```

## 2. 汇总

- `squarefree_input_status=raw_thick_squarefree_support_closed_layer_transfer_open`。
- `squarefree_input_next_target=CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn`。
- `all_retention_model_rows_suffice=True`。
- `conditional_selector_retention_implies_layer_transfer=True`。
- `layer_transfer_closed=False`。
- `next_internal_target=CanonicalSelectorRetentionOrCleanReturn`。
- `terminal_gap_after_router=CanonicalSelectorRetentionOrCleanReturnOrExternalDIBFIOriginalDispersion`。

## 3. 门控表

| gate | available | needed | gap | route | closed |
| --- | --- | --- | --- | --- | --- |
| `ExactCoefficientFormulaFixed` | RIW/Buchstab factors are named but the exact selector is not ledgered here | an explicit formula for alpha_u and delta_v on the canonical layer | without the formula, layer admission is a label rather than a checkable predicate | record the canonical RIW path selector, parity rule and dyadic truncation rule | `False` |
| `SelectorRetentionLowerBound` | raw thick Buchstab support has already been paid | the exact selector keeps at least a log-power fraction of raw support | a selector could be formally well-factorable but keep a sparse sublayer | prove retained_support >= raw_support/log^R in every clean thick block | `False` |
| `NonzeroTransferAfterSelection` | once selected support is defined by alpha_u != 0 or delta_v != 0 | selected products carry nonzero coefficients in absolute support | this is tautological only after the exact coefficient formula is fixed | define admission by nonzero coefficient, then no extra cancellation gate remains | `True` |
| `RejectedOrThinCleanReturn` | edge/PDEC/SAE exits exist elsewhere | blocks failing thickness or selector retention cannot stay in clean A1 | clean admission has not yet been stated as the contrapositive of this failure | add clean-branch contract: low retention => endpoint/edge/tail-label/PDEC exit | `False` |
| `LayerTransferImpliesSquarefreeSupport` | previous squarefree router closed raw thick support | selector retention plus return contract | conditional implication is direct; the selector/return contract remains | combine retained support with nonzero transfer | `True` |

## 4. 保留率阈值模型

| k | log y | raw support | retained support | required support | max selector loss | suffices |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 3 | 6.90776 | 15728.4 | 2276.92 | 2276.92 | 1 | `True` |
| 4 | 9.21034 | 66279.4 | 7196.19 | 7196.19 | 1 | `True` |
| 5 | 11.5129 | 202269 | 17568.8 | 17568.8 | 1 | `True` |
| 6 | 13.8155 | 503309 | 36430.7 | 36430.7 | 1 | `True` |
| 7 | 16.1181 | 1.08785e+06 | 67492.4 | 67492.4 | 1 | `True` |
| 8 | 18.4207 | 2.12094e+06 | 115139 | 115139 | 1 | `True` |
| 9 | 20.7233 | 3.822e+06 | 184431 | 184431 | 1 | `True` |

## 5. 结论

新最窄内部目标为：

```text
CanonicalSelectorRetentionOrCleanReturn:
  fix the exact canonical RIW/Buchstab coefficient selector;
  prove it retains a log-power fraction of thick Buchstab support in every clean block;
  otherwise prove the block exits to edge/PDEC/SAE.
```

这仍不是行命题最终闭合；但它把 nonzero transfer 的语义问题压成了一个可审稿的选择器保留率/clean 反向退出合同。
