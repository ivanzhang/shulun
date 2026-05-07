# Triad-A1 FactorResidueIncidence 路由审计

**状态：** `factor_residue_incidence_bridge_blocked_by_internal_atom_fiber`

FactorResidueIncidenceBridge 的朴素形式被内部 fiber 阻断：一个 moving `(u,v)` 块内可含许多 residue/phase 原子，质量在内部原子上平坦，但在 factor-pair 层仍完全集中。因此 clean K4/K6 不能通过 incidence 桥推出 ExactFactorSupport。内部路线只剩直接证明 CanonicalRIWFactorSupportLowerBound，否则走外部 DI/BFI。

## 1. 内部 fiber 阻断律

A moving factor-pair b=(u,v) is not a single K4 atom. It contains a growing internal fiber of h, ell, completion and Kloosterman variables. Mass can be flat on that internal fiber while remaining completely concentrated on one moving factor pair. Therefore small factor support does not force K4 coefficient concentration or K6 tail-label concentration.

```text
one moving factor pair b=(u,v)
  contains many internal atoms (h, ell, x, z, completion labels);
mass can be flat on those internal K4 atoms
  while remaining concentrated on b;
therefore K4/K6 do not imply ExactFactorSupport through naive incidence.
```

## 2. 汇总

- `factor_support_input_status=exact_factor_support_not_implied_by_k4_k6_without_incidence_bridge`。
- `all_rows_k4_flat_inside_one_factor_pair=True`。
- `naive_incidence_bridge_valid=False`。
- `factor_residue_incidence_bridge_closed=False`。
- `next_internal_target=CanonicalRIWFactorSupportLowerBound`。
- `terminal_gap_after_router=CanonicalRIWFactorSupportLowerBoundOrExternalDIBFIOriginalDispersion`。

## 3. 门控表

| gate | available | needed | gap | route | closed |
| --- | --- | --- | --- | --- | --- |
| `BoundedIncidenceMultiplicity` | not present | one moving (u,v) block hits only polylog-small residue/phase atoms | actual Kloosterman expansion has many h,ell,x,z atoms inside one (u,v) block | cannot be assumed; must be proved as arithmetic incidence, and naive form is false | `False` |
| `K4ConcentrationReturn` | K4 returns if a residue/phase atom is large | small factor support creates a large residue/phase atom | a single factor pair can distribute its mass over many internal atoms and stay K4-flat | requires block-level capacity, which is NC-BLK/DI-BFI again | `False` |
| `K6TailLabelReturn` | K6 returns if dyadic/tail-label splitting is excessive | small factor support creates excessive splitting | one factor pair inside one dyadic block is not excessive splitting | K6 does not see missing internal support | `False` |
| `CanonicalSupportFallback` | still logically possible | direct support theorem for exact RIW/Buchstab factors | not yet proved or cited | CanonicalRIWFactorSupportLowerBound | `False` |

## 4. 阻断模型表

| k | log y | factor pairs | internal atoms | max internal share | K4 flat | factor share | factor support fails |
| ---: | ---: | ---: | ---: | ---: | --- | ---: | --- |
| 3 | 6.90776 | 1 | 750514 | 1.33242e-06 | `True` | 1 | `True` |
| 4 | 9.21034 | 1 | 5622504 | 1.77857e-07 | `True` | 1 | `True` |
| 5 | 11.5129 | 1 | 26810188 | 3.72993e-08 | `True` | 1 | `True` |
| 6 | 13.8155 | 1 | 96065750 | 1.04095e-08 | `True` | 1 | `True` |
| 7 | 16.1181 | 1 | 282615581 | 3.53838e-09 | `True` | 1 | `True` |
| 8 | 18.4207 | 1 | 719680491 | 1.38951e-09 | `True` | 1 | `True` |
| 9 | 20.7233 | 1 | 1641373385 | 6.09246e-10 | `True` | 1 | `True` |

## 5. 结论

当前可删去一个伪出口：

```text
FactorResidueIncidenceBridge, in the naive bounded-multiplicity form, is blocked.
```

继续无黑箱路线只剩：

```text
CanonicalRIWFactorSupportLowerBound:
  prove exact Rosser/Iwaniec-Buchstab factors have broad balanced support.
```

外部路线仍是 `DI/BFI original dispersion`。
