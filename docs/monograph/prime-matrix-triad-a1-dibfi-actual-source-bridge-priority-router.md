# Triad-A1 DI/BFI actual-source bridge priority 路由器

**状态：** `actual_source_bridge_best_direction_selected`

两个自足方向中，最优硬攻方向是证明实际 full-S non-AP 源头为 canonical RIW/Buchstab。该方向可直接接入已闭合的 canonical-restricted 链；strengthened anti-atom 方向必须先获得实际源头结构，否则回到已反证的 generic WFD 反原子。

## 1. 优先级律

The canonical-source route is the optimal self-contained direction because it turns the actual-source bridge into a deterministic provenance identity for lambda_c. The strengthened anti-atom route is not abandoned forever, but it is not the next best move: without first proving actual-source structure it repeats the generic WFD anti-atom statement already refuted by the moving-delta model.

```text
previous terminal:
  ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput;

selected direction:
  ProveActualSourceIsCanonicalRIWBuchstab;

new terminal:
  ActualKZESourceCoefficientProvenanceLedgerInput.
```

## 2. 下一账本必备条款

- `OriginalA1KZESourceDefinition`。
- `PreCauchyLambdaEquality`。
- `NoCoefficientReplacementBeforeDispersion`。
- `DyadicAndBranchBookkeepingPreserved`。
- `NoncanonicalComplementRoutedExternally`。

## 3. 方向比较表

| direction | selected | score | evidence | obstruction | next target |
| --- | --- | --- | --- | --- | --- |
| `ProveActualSourceIsCanonicalRIWBuchstab` | `true` | `3` | canonical-restricted branch is already internally closed; source lock feeds the support chain; the remaining proof is a coefficient-provenance identity before Cauchy/dispersion. | actual A1/KZ-E lambda_c provenance is not yet written as a ledger | `ActualKZESourceCoefficientProvenanceLedgerInput` |
| `ProveActualSourceStrengthenedAntiAtom` | `false` | `1` | generic anti-atom refuted=True; source anti-atom contract still open=True. | without first proving actual-source structure, this collapses back to the moving-delta no-go for generic WFD | `ActualSourceStructureFirstOrNewAntiAtomAxiom` |

## 4. 当前结论

下一步不应继续攻击 unrestricted generic anti-atom。最窄可攻输入是：

```text
ActualKZESourceCoefficientProvenanceLedgerInput
```

这一步要证明的是实际 lambda_c 的来源等式，而不是新的统计逼近。
