# Prime Matrix 非二点 PDEC 准入审计

**状态：** `no_current_materialized_nontautological_primitive_pdec`

当前已物化前沿没有非二点 primitive PDEC 候选。raw 三点强信号已被同 formal unit、嵌套重复、weighted Hall 与 cross-q 图重叠逐层降口径；物理 primitive 只剩二点 Fourier tautology，且二点原子已由 LocalSurvivor witness 吸收。该项不关闭全局 PDEC family，只给未来新候选固定准入门槛。

## 1. 准入律

A non-tautological primitive PDEC candidate must survive every quotient already introduced by the FO-PDEC audits: same-formal-unit legality, nested duplicate removal, weighted Hall non-recovery, cross-q physical deduplication, and the two-point tautology test. The current materialized frontier has no such survivor: the raw three-point signal is not an admissible primitive unit, and the physical primitive remnant has only two atoms, both absorbed by SAE/Endpoint witnesses.

```text
current materialized frontier:
  raw three-point signal -> illegal as one primitive formal unit;
  physical primitive remnant -> two-point Fourier tautology;
  two physical atoms -> LocalSurvivor/SAE witness absorption;
therefore:
  current non-tautological primitive PDEC candidate count = 0.
```

## 2. 汇总

- `all_current_routes_blocked_or_absorbed=true`。
- `current_materialized_nontautological_pdec_candidate_count=0`。
- `global_pdec_family_closed=false`。

## 3. 审计表

| gate | closed | evidence | verdict |
| --- | --- | --- | --- |
| `RawLibraryThreePointSignal` | `true` | raw support=3, Fourier=3.959247567099438 | not_admissible_without_same_formal_unit_and_independence |
| `NestedDuplicateUnitMass` | `true` | NestedBlockFullMultiplicityRejectedForAuditedFO-PDEC | nested coordinate repeats cannot count as independent PDEC atoms |
| `WeightedHallDuplicateRecovery` | `true` | FractionalWeightedHallCannotRecoverFullNestedDuplicateMass | fractional weighted Hall cannot recover the duplicate mass |
| `CrossQCoordinatePersistence` | `true` | CrossQCoordinatePersistenceRejectedForAuditedFO-PDEC | cross-q reuse is chart overlap, not persistent independent atoms |
| `PhysicalPrimitiveAtomCount` | `true` | physical_event_count=2; bound=1.9997507790353146 | physical primitive branch is two-point tautology, not non-tautological PDEC |
| `TwoAtomSAEEndpointAbsorption` | `true` | physical_atom_count=2; witnessed=True | remaining two atoms are absorbed by local survivor witnesses |
| `MaterializedLedgerNoOpenPDECObligation` | `true` | finite_pdec_atom_count=25; open=0 | current materialized PDEC/SAE packets have no open local obligation |

## 4. 未来候选准入要求

- `same formal unit with one fixed phase map`
- `at least three physical primitive atoms after deduplication`
- `not a two-point Fourier tautology`
- `not nested duplicate mass or weighted-Hall duplicate recovery`
- `not cross-q coordinate chart overlap`
- `not absorbed by LocalSurvivor/SAE/Endpoint witness`
