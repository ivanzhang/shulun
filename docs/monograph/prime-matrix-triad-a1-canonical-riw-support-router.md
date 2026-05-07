# Triad-A1 CanonicalRIWFactorSupport 路由审计

**状态：** `canonical_riw_support_reduced_to_squarefree_buchstab_layer_support`

CanonicalRIWFactorSupportLowerBound 已被压缩为一个更初等的组合筛支撑命题：固定 exact Rosser/Iwaniec-Buchstab 分解后，只需证明 surviving balanced dyadic factor interval 中有足够多非零 squarefree Buchstab-layer products，并把薄区间返回 edge/PDEC/SAE。当前 ledger 尚未提供这个局部支撑下界。

## 1. 归约律

Canonical RIW support is not a spectral problem. Once the exact factorization is fixed, it follows from a local lower bound for squarefree Buchstab-layer products in every surviving balanced dyadic interval, plus nonzero transfer of those products into the canonical alpha and delta coefficients.

```text
fix canonical RIW/Buchstab factorization alpha*delta;
prove many squarefree Buchstab-layer products in each surviving balanced interval;
prove those products carry nonzero alpha/delta coefficients;
then sum |alpha_u|, sum |delta_v| have log-power lower bounds.
```

## 2. 汇总

- `incidence_input_status=factor_residue_incidence_bridge_blocked_by_internal_atom_fiber`。
- `conditional_squarefree_support_implies_riw_support=True`。
- `canonical_riw_support_closed=False`。
- `all_model_rows_support_lemma_suffices=True`。
- `next_internal_target=SquarefreeBuchstabLayerSupportLowerBound`。
- `terminal_gap_after_router=SquarefreeBuchstabLayerSupportLowerBoundOrExternalDIBFIOriginalDispersion`。

## 3. 门控表

| gate | available | needed | gap | route | closed |
| --- | --- | --- | --- | --- | --- |
| `CanonicalFactorizationFixed` | WFD ledger uses existence of well-factorable splitting | a specified canonical Rosser/Iwaniec-Buchstab splitting alpha*delta | support statements are meaningless until the splitting is fixed | define the exact RIW/Buchstab factorization used in KZ-E | `False` |
| `SquarefreeBuchstabLayerSupport` | not present as a local lower-bound lemma | many squarefree products in each surviving balanced dyadic factor interval | this is a short multiplicative interval support theorem, not a Kloosterman estimate | prove by Buchstab recursion/Mertens product or route thin intervals to edge/PDEC | `False` |
| `NonzeroCoefficientTransfer` | RIW factors are divisor-bounded | squarefree products counted by the support lemma carry nonzero canonical coefficients | parity/layer truncation can zero out a combinatorial class unless layer admission is recorded | record layer support and parity nonvanishing for the exact construction | `False` |
| `SmallOrThinIntervalReturn` | K1/K3/K6 and finite PDEC/SAE exits exist | balanced intervals too short for support lemma do not remain in clean branch | threshold return is not yet connected to canonical support | prove thin support => edge/endpoint/tail-label failure | `False` |
| `SupportLemmaImpliesRIWSupport` | elementary once previous gates hold | sum \|alpha_u\| >= U/log^C and sum \|delta_v\| >= V/log^C | conditional implication is clear; hypotheses remain | SquarefreeBuchstabLayerSupport + NonzeroCoefficientTransfer | `True` |

## 4. 阈值模型表

| k | log y | interval size | expected sqfree products | required mass | suffices |
| ---: | ---: | ---: | ---: | ---: | --- |
| 3 | 6.90776 | 750514 | 15728.4 | 2276.92 | `True` |
| 4 | 9.21034 | 5.6225e+06 | 66279.4 | 7196.19 | `True` |
| 5 | 11.5129 | 2.68102e+07 | 202269 | 17568.8 | `True` |
| 6 | 13.8155 | 9.60657e+07 | 503309 | 36430.7 | `True` |
| 7 | 16.1181 | 2.82616e+08 | 1.08785e+06 | 67492.4 | `True` |
| 8 | 18.4207 | 7.1968e+08 | 2.12094e+06 | 115139 | `True` |
| 9 | 20.7233 | 1.64137e+09 | 3.822e+06 | 184431 | `True` |

## 5. 结论

当前新最窄目标为：

```text
SquarefreeBuchstabLayerSupportLowerBound:
  every surviving balanced dyadic factor interval contains enough nonzero
  squarefree products in the canonical RIW/Buchstab layer.
```

这仍不是行命题最终证明；它把 canonical RIW 支撑问题降到局部组合筛支撑下界。
