# Triad-A1 DI/BFI self-contained closure taxonomy 路由器

**状态：** `self_contained_closure_taxonomy_closed_actual_source_bridge_open`

自足闭合路线已完成分类：外部 generic 合同版闭合；canonical-restricted 自足分支闭合；unrestricted generic 自足版被 moving-delta 反证。真正剩余不是继续攻击 generic WFD，而是证明实际 full-S non-AP 源头满足 canonical source lock 或 strengthened source anti-atom。

## 1. 实际源头桥合同

`For the actual full-S non-AP A1/KZ-E source entering the dispersion step, prove either lambda_c equals the canonical RIW/Buchstab decision-tree source, or prove the strengthened anti-atom bound max_{u,v} M_{u,v}/sum M_{u,v} <= log^{-2A} for that actual source.`

## 2. 结构律

The self-contained problem has changed type. It is no longer an unrestricted generic WFD dispersion estimate, because that statement is refuted by the moving-delta model. It is also not an external-theorem problem, because FullS-KLS-ext already closes that version. The only honest self-contained bridge is an actual-source theorem: identify the actual source as canonical RIW/Buchstab, or prove that the actual noncanonical source has the strengthened anti-atom property.

```text
external generic theorem:
  closed = true;

canonical-restricted self-contained theorem:
  closed = true;

unrestricted generic self-contained theorem:
  refuted = true;

new actual-source terminal:
  ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput.
```

## 3. 汇总

- `external_contract_version_closed=true`。
- `canonical_restricted_self_contained_version_closed=true`。
- `generic_self_contained_version_refuted=true`。
- `original_unrestricted_self_contained_version_closed=false`。
- `actual_source_bridge_pinned=true`。
- `actual_source_bridge_theorem_closed=false`。
- `terminal_gap_expansion=['ProveActualSourceIsCanonicalRIWBuchstab', 'ProveActualSourceStrengthenedAntiAtom', 'AcceptExternalFullSKLSExtForGenericBranch']`。

## 4. 分类账本表

| gate | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- |
| `ExternalGenericContractClosed` | `true` | terminal_split.external=True; FullS-KLS-ext=True. | none for the external-contract theorem | `DoNotConfuseWithSelfContainedProof` |
| `CanonicalRestrictedSelfContainedClosed` | `true` | Branch coverage records no further internal source-lock gap for the canonical RIW/Buchstab source branch. | only the statement must remain branch-restricted | `ActualSourceBridge` |
| `GenericSelfContainedRefuted` | `true` | The moving-delta capacity model violates the required source anti-atom while passing the current formal generic WFD templates. | unrestricted generic WFD cannot be closed as a self-contained proof | `ActualSourceBridge` |
| `NoSilentCanonicalUpgrade` | `true` | Source-lock and branch-coverage ledgers forbid importing the canonical support chain into the generic WFD branch without proving source identity. | actual source must be locked, not assumed | `ActualSourceBridge` |
| `RouteTaxonomyClosed` | `true` | The routes are now exhaustive: external generic theorem is closed; canonical-restricted self-contained branch is closed; unrestricted generic self-contained branch is refuted. | none at classification level | `ActualA1FullSSourceLockOrStrengthenedAntiAtom` |
| `ActualSourceBridgePinned` | `true` | To convert the conditional canonical closure into the desired self-contained full-S closure, the actual source must either be canonical RIW/Buchstab or satisfy a strengthened source anti-atom theorem. | prove one of the two actual-source bridge theorems | `ActualA1FullSSourceLockOrStrengthenedAntiAtom` |
| `ActualSourceBridgeTheoremClosed` | `false` | No current ledger proves that the actual full-S non-AP WFD source is canonical RIW/Buchstab, and no current ledger proves the strengthened source anti-atom bound for the actual noncanonical source. | this is the new narrowest self-contained theorem input | `ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput` |

## 5. 当前结论

完全自足版不能再以 unrestricted generic WFD 原命题形式推进；该形式已被反例阻断。可继续硬攻的最窄目标是：

```text
ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput
```

它有且只有两个自足证明方向：证明实际源头等于 canonical RIW/Buchstab 决策树源头，或直接证明实际源头的 strengthened anti-atom。
