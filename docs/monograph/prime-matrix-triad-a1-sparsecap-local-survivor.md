# Triad-A1 SparseCap 到 LocalSurvivor / finite PDEC 审计

**状态：** `sparsecap_atoms_routed_to_local_survivor_or_finite_pdec`

SparseCap 路由已去重到有限相位原子。所有枚举到的 sparse 完成行都不在 P 行以内；phase<=P 但 y=0 不能完成的原子给出显式 LocalSurvivor 列见证，其余原子转入 finite PDEC packet。

## 1. 证书语义

`DualCap` 的 `SparseCap` 不能继续停在路由标签上。本文把它去重为有限相位集，并逐相位检查：

```text
row = phase + Q*y；
y=0 且 phase<=P 代表 P 行以内真实早期行；
若该行未被高素数补完，则输出未覆盖列 LocalSurvivor witness；
若完成只发生在 y>0 或 phase>P，则该 sparse 原子转入 finite PDEC packet。
```

## 2. 来源指纹

| source | sha256 |
| --- | --- |
| `sparsecap_local_survivor_script` | `2ff8637a2726f10c2d69982f25fb3a915bdc5c45f7928a20a34c86ad0472534e` |
| `dualcap_json` | `b6bf0fc2a4305656fa7aef8cac33aa9b7dd1867617611fe7b96a23e8ba251c53` |
| `multiplicity_cap_json` | `5bcfa7c286e716b3b626c312becf303fee3b9d72142aaa30be63f849cb21162d` |

## 3. 汇总

- `sparse_descriptor_count=16`。
- `unique_sparse_cap_count=3`。
- `phase_atom_count_with_multiplicity=36`。
- `unique_phase_atom_count=26`。
- `early_completion_conflict_count=0`。
- `unique_early_completion_conflict_count=0`。
- `all_sparse_caps_closed_for_pxP=True`。
- `local_survivor_witness_count=1`。
- `unique_local_survivor_witness_count=1`。
- `finite_pdec_atom_count=35`。
- `unique_finite_pdec_atom_count=25`。

| P | descriptors | phases | first completion row | equals P^2 | local witnesses | finite atoms | route |
| ---: | ---: | ---: | ---: | --- | ---: | ---: | --- |
| 13 | 12 | 4 | 169 | `True` | 0 | 4 | `SparseCapClosedForPxPAndRoutedToFinitePDEC` |
| 17 | 2 | 16 | 1211 | `False` | 1 | 15 | `SparseCapClosedForPxPAndRoutedToFinitePDEC` |
| 17 | 2 | 16 | 1211 | `False` | 0 | 16 | `SparseCapClosedForPxPAndRoutedToFinitePDEC` |

## 4. 相位原子

### P=13 sparse phase set

- residues mod `2310`: `[169, 702, 1609, 2142]`。
- finite PDEC mass upper bound: `4`。

| phase | holes | y completions | completion rows | y=0 complete | witness col | route |
| ---: | --- | --- | --- | --- | --- | --- |
| 169 | `[]` | `[0]` | `[169]` | `True` | None | `FinitePDECAtomBeyondP` |
| 702 | `[]` | `[0]` | `[702]` | `True` | None | `FinitePDECAtomBeyondP` |
| 1609 | `[]` | `[0]` | `[1609]` | `True` | None | `FinitePDECAtomBeyondP` |
| 2142 | `[]` | `[0]` | `[2142]` | `True` | None | `FinitePDECAtomBeyondP` |

### P=17 sparse phase set

- residues mod `2310`: `[13, 124, 260, 611, 613, 828, 964, 1100, 1211, 1347, 1483, 1698, 1700, 2051, 2187, 2298]`。
- finite PDEC mass upper bound: `16`。

| phase | holes | y completions | completion rows | y=0 complete | witness col | route |
| ---: | --- | --- | --- | --- | --- | --- |
| 13 | `[7]` | `[1]` | `[2323]` | `False` | 7 | `LocalSurvivorWitnessAtRowLeP` |
| 124 | `[8]` | `[2]` | `[4744]` | `False` | None | `FinitePDECAtomBeyondP` |
| 260 | `[6]` | `[5]` | `[11810]` | `False` | None | `FinitePDECAtomBeyondP` |
| 611 | `[9]` | `[6]` | `[14471]` | `False` | None | `FinitePDECAtomBeyondP` |
| 613 | `[7]` | `[8]` | `[19093]` | `False` | None | `FinitePDECAtomBeyondP` |
| 828 | `[12]` | `[6]` | `[14688]` | `False` | None | `FinitePDECAtomBeyondP` |
| 964 | `[10]` | `[9]` | `[21754]` | `False` | None | `FinitePDECAtomBeyondP` |
| 1100 | `[8]` | `[12]` | `[28820]` | `False` | None | `FinitePDECAtomBeyondP` |
| 1211 | `[9]` | `[0]` | `[1211]` | `True` | None | `FinitePDECAtomBeyondP` |
| 1347 | `[7]` | `[3]` | `[8277]` | `False` | None | `FinitePDECAtomBeyondP` |
| 1483 | `[5]` | `[6]` | `[15343]` | `False` | None | `FinitePDECAtomBeyondP` |
| 1698 | `[10]` | `[4]` | `[10938]` | `False` | None | `FinitePDECAtomBeyondP` |
| 1700 | `[8]` | `[6]` | `[15560]` | `False` | None | `FinitePDECAtomBeyondP` |
| 2051 | `[11]` | `[7]` | `[18221]` | `False` | None | `FinitePDECAtomBeyondP` |
| 2187 | `[9]` | `[10]` | `[25287]` | `False` | None | `FinitePDECAtomBeyondP` |
| 2298 | `[10]` | `[11]` | `[27708]` | `False` | None | `FinitePDECAtomBeyondP` |

### P=17 sparse phase set

- residues mod `2310`: `[124, 378, 401, 551, 611, 828, 964, 1211, 1347, 1488, 1601, 1638, 1698, 2051, 2187, 2298]`。
- finite PDEC mass upper bound: `16`。

| phase | holes | y completions | completion rows | y=0 complete | witness col | route |
| ---: | --- | --- | --- | --- | --- | --- |
| 124 | `[8]` | `[2]` | `[4744]` | `False` | None | `FinitePDECAtomBeyondP` |
| 378 | `[12]` | `[4]` | `[9618]` | `False` | None | `FinitePDECAtomBeyondP` |
| 401 | `[3]` | `[10]` | `[23501]` | `False` | None | `FinitePDECAtomBeyondP` |
| 551 | `[3]` | `[2]` | `[5171]` | `False` | None | `FinitePDECAtomBeyondP` |
| 611 | `[9]` | `[6]` | `[14471]` | `False` | None | `FinitePDECAtomBeyondP` |
| 828 | `[12]` | `[6]` | `[14688]` | `False` | None | `FinitePDECAtomBeyondP` |
| 964 | `[10]` | `[9]` | `[21754]` | `False` | None | `FinitePDECAtomBeyondP` |
| 1211 | `[9]` | `[0]` | `[1211]` | `True` | None | `FinitePDECAtomBeyondP` |
| 1347 | `[7]` | `[3]` | `[8277]` | `False` | None | `FinitePDECAtomBeyondP` |
| 1488 | `[4]` | `[8]` | `[19968]` | `False` | None | `FinitePDECAtomBeyondP` |
| 1601 | `[11]` | `[5]` | `[13151]` | `False` | None | `FinitePDECAtomBeyondP` |
| 1638 | `[4]` | `[0]` | `[1638]` | `True` | None | `FinitePDECAtomBeyondP` |
| 1698 | `[10]` | `[4]` | `[10938]` | `False` | None | `FinitePDECAtomBeyondP` |
| 2051 | `[11]` | `[7]` | `[18221]` | `False` | None | `FinitePDECAtomBeyondP` |
| 2187 | `[9]` | `[10]` | `[25287]` | `False` | None | `FinitePDECAtomBeyondP` |
| 2298 | `[10]` | `[11]` | `[27708]` | `False` | None | `FinitePDECAtomBeyondP` |

## 5. 结构读数

本审计确认：在当前 `Q=2310` 的 sparse 失败帽中，没有一个完成态落在 `row<=P` 的早期方阵内。
尤其 `P=13` 的最早 sparse 完成行为 `169=P^2`，正对应“必须到 P 与 P^2 连线后才出现完整斜线”的几何直觉。

因此 `SparseCap` 路由已被压成：

```text
早期 phase<=P 且 y=0 不完成 => LocalSurvivor witness；
完成行全部在 P 之后         => finite PDEC / column-tail 后续证书输入。
```

这仍不是整个行命题闭合；它关闭的是 `DualCap` 中 `SparseCap` 的 P×P 早期出口，并把持久稀疏复现交给 finite PDEC packet。
