# Triad-A1 ExactFactorSupport 路由审计

**状态：** `exact_factor_support_not_implied_by_k4_k6_without_incidence_bridge`

ExactFactorSupportLowerBound 不能从当前 K4/K6 clean admission 自动推出：存在 residue-flat 但 factor-concentrated 的投影错配模型。下一步必须证明 factor-residue incidence 桥，说明少数 moving factor pairs 会触发既有 K4/K6 失败；或者直接证明 canonical Rosser/Iwaniec-Buchstab 因子支撑下界。

## 1. 投影错配律

K4 controls residue/phase atoms, while ExactFactorSupport controls moving factor-pair atoms. K6 controls how many dyadic blocks exist, not how much support each block contains. Without an incidence bridge bounding how many residue atoms one moving factor pair can hide behind, K4/K6 do not imply factor support lower bounds.

```text
K4 flatness lives on residue/phase atoms;
ExactFactorSupport lives on moving factor-pair atoms b=(u,v);
K6 limits the number of dyadic blocks, not the internal support of each block;
therefore K4+K6 need an incidence bridge before they can imply factor support.
```

## 2. 条件闭合律

ExactFactorSupport can still be closed internally in either of two ways: prove the canonical Rosser/Iwaniec-Buchstab factor support lower bound directly, or prove that any failure of factor support triggers existing clean-branch failures through a FactorResidueIncidenceBridge.

## 3. 汇总

- `exact_wfd_input_status=exact_wfd_source_entropy_reduced_to_factor_support_lower_bound`。
- `all_rows_k4_flat_but_factor_support_fails=True`。
- `k4_k6_imply_exact_factor_support=False`。
- `current_internal_exact_factor_support_closed=False`。
- `next_internal_target=FactorResidueIncidenceBridgeOrCanonicalRIWFactorSupport`。
- `terminal_gap_after_router=FactorResidueIncidenceBridgeOrCanonicalRIWFactorSupportOrExternalDIBFIOriginalDispersion`。

## 4. 门控表

| gate | available | needed | gap | route | closed |
| --- | --- | --- | --- | --- | --- |
| `K4ResidueFlatness` | L2 flatness on fixed residue/phase atoms, support A_B >= R/C_flat | many moving factor pairs (u,v) carry the exact WFD capacity | a single moving factor pair may split into many residue atoms unless incidence is bounded | prove FactorResidueIncidenceBridge or use direct canonical factor support | `False` |
| `K6DyadicBookkeeping` | dyadic/tail-label split count is polylog and over-splitting is routed | each surviving dyadic block has broad internal u- and v-support | polylog many blocks does not imply lower support inside a block | small internal support must be named as a failure route or proved impossible for exact weights | `False` |
| `CanonicalRIWFactorSupport` | not recorded for the exact Rosser/Iwaniec-Buchstab factorization used by KZ-E | sum \|alpha_u\| >= U/log^C and sum \|delta_v\| >= V/log^C | well-factorable existence alone permits sparse formal factors | prove direct exact sieve-factor support lemma | `False` |
| `FactorResidueIncidenceBridge` | not present in current ledger | bounded multiplicity from one moving (u,v) block into K4 residue atoms | without this bridge, residue flatness and factor support live on different sigma-algebras | prove concentration on few factor pairs triggers coefficient/tail-label PDEC/SAE failure | `False` |
| `SupportFailureReturn` | clean branch routes coefficient concentration and tail-label concentration | factor-support failure is shown to be one of those named failures | the implication is not yet proved; it is exactly the incidence bridge | FactorResidueIncidenceBridge | `False` |

## 5. 阻断模型表

| k | log y | residue atoms | max residue share | K4 flat | factor pairs | factor share | support needed | factor support fails |
| ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | --- |
| 3 | 6.90776 | 750514 | 1.33242e-06 | `True` | 1 | 1 | 108648 | `True` |
| 4 | 9.21034 | 5622504 | 1.77857e-07 | `True` | 1 | 1 | 610456 | `True` |
| 5 | 11.5129 | 26810188 | 3.72993e-08 | `True` | 1 | 1 | 2328704 | `True` |
| 6 | 13.8155 | 96065750 | 1.04095e-08 | `True` | 1 | 1 | 6953471 | `True` |
| 7 | 16.1181 | 282615581 | 3.53838e-09 | `True` | 1 | 1 | 17534056 | `True` |
| 8 | 18.4207 | 719680491 | 1.38951e-09 | `True` | 1 | 1 | 39069159 | `True` |
| 9 | 20.7233 | 1641373385 | 6.09246e-10 | `True` | 1 | 1 | 79204379 | `True` |

## 6. 可接受输入

| input | statement | would imply | status |
| --- | --- | --- | --- |
| `CanonicalRIWFactorSupportLowerBound` | the exact Rosser/Iwaniec-Buchstab well-factorable factors used in KZ-E have log-power lower absolute support in every surviving balanced block | ExactFactorSupportLowerBound directly | `not_present_in_current_ledger` |
| `FactorResidueIncidenceBridge` | if moving factor support is too small, then K4 coefficient concentration or K6 tail-label concentration is triggered | ExactFactorSupportLowerBound on the clean branch by contrapositive | `not_present_in_current_ledger` |
| `ExternalDIBFIOriginalDispersion` | original DI/BFI dispersion supplies block variance saving without proving internal support | A1 clean branch closed in external theorem version | `acceptable_external_route` |

## 7. 结论

当前推进不是证明失败，而是排除一次偷换：

```text
residue-flat + dyadic-bookkeeping
  does not imply moving factor-pair support lower bound.
```

下一步若继续无黑箱路线，应直接证明：

```text
FactorResidueIncidenceBridge:
  small moving factor support forces an existing K4/K6 failure;
or
CanonicalRIWFactorSupport:
  exact Rosser/Iwaniec-Buchstab factors have broad support in each surviving balanced block.
```

否则仍只能切到外部 `DI/BFI original dispersion`。
