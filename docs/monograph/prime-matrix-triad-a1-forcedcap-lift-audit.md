# Triad-A1 ForcedCap 升层审计

**状态：** `forced_persistent_caps_lifted_to_target_q`

ForcedPersistentByDensityBarrier cap 已升层为 target_q support 账本。本审计只判定 lift support 是否非空，不计算完整 multiplicity；它说明固定 Q 密度屏障不会停在同层循环，而会转化为 fiber 删除压力或继续持久的 column-tail/next-lift 义务。

## 1. 证书语义

对 `Q=2310` 中由密度屏障强制的 persistent cap，不再尝试在同一层反复压缩。
本文把 cap 的旧相位 `t mod Q` lift 到 `target_q` 的全部 fiber，并只检查每个 lift 槽是否存在补洞完成：

```text
t -> t + Q*s, 0<=s<target_q/Q；
若 lift support 为空或稀疏 => LocalSurvivor / finite PDEC；
若出现显著删除 => FiberDeletionPressure；
若仍持久 => 必须加 column-tail 行或继续升层，不能同层循环。
```

## 2. 来源指纹

| source | sha256 |
| --- | --- |
| `forcedcap_lift_script` | `f4c5c82cae31837a758afdd80abd520ebd52e85cc85157fd6448e494fd400d13` |
| `dualcap_json` | `b6bf0fc2a4305656fa7aef8cac33aa9b7dd1867617611fe7b96a23e8ba251c53` |
| `multiplicity_cap_json` | `5bcfa7c286e716b3b626c312becf303fee3b9d72142aaa30be63f849cb21162d` |

## 3. 汇总

- `forced_cap_count=24`。
- `lift_class_counts={'LiftPersistentNeedsColumnTailOrNextLift': 24}`。
- `all_old_intersections_recomputed=True`。

| P | target support | target density | unique hole patterns | fiber hist all phases |
| ---: | ---: | ---: | ---: | --- |
| 43 | 15028 | 0.500433 | 11880 | `{0: 260, 1: 276, 2: 160, 5: 56, 6: 392, 7: 372, 8: 206, 9: 24, 13: 564}` |
| 47 | 21386 | 0.712155 | 14790 | `{0: 44, 1: 156, 2: 140, 6: 112, 7: 320, 8: 256, 9: 160, 10: 12, 13: 1110}` |

## 4. ForcedCap lift 明细

| P | alpha | h | dir | old inter | lift slots | survival | deletion | fiber hist on cap | lift class |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 43 | 0 | 805 | 0.25 | 1077 | 8781 | 0.627169 | 0.372831 | `{1: 84, 2: 93, 5: 41, 6: 193, 7: 174, 8: 90, 9: 4, 13: 398}` | `LiftPersistentNeedsColumnTailOrNextLift` |
| 43 | 0 | 1505 | 0.75 | 1081 | 8784 | 0.625062 | 0.374938 | `{1: 81, 2: 98, 5: 42, 6: 198, 7: 175, 8: 87, 9: 3, 13: 397}` | `LiftPersistentNeedsColumnTailOrNextLift` |
| 43 | 0.5 | 805 | 0.25 | 734 | 6106 | 0.639908 | 0.360092 | `{1: 50, 2: 70, 5: 32, 6: 124, 7: 112, 8: 54, 13: 292}` | `LiftPersistentNeedsColumnTailOrNextLift` |
| 43 | 0.5 | 1505 | 0.75 | 734 | 6106 | 0.639908 | 0.360092 | `{1: 50, 2: 70, 5: 32, 6: 124, 7: 112, 8: 54, 13: 292}` | `LiftPersistentNeedsColumnTailOrNextLift` |
| 43 | 0 | 770 | 0.5 | 1370 | 10087 | 0.566367 | 0.433633 | `{1: 174, 2: 110, 5: 38, 6: 268, 7: 262, 8: 125, 9: 12, 13: 381}` | `LiftPersistentNeedsColumnTailOrNextLift` |
| 43 | 0 | 1540 | 0.5 | 1370 | 10087 | 0.566367 | 0.433633 | `{1: 174, 2: 110, 5: 38, 6: 268, 7: 262, 8: 125, 9: 12, 13: 381}` | `LiftPersistentNeedsColumnTailOrNextLift` |
| 43 | 0.5 | 1155 | 0 | 1025 | 7514 | 0.563902 | 0.436098 | `{1: 138, 2: 80, 5: 28, 6: 196, 7: 186, 8: 103, 9: 12, 13: 282}` | `LiftPersistentNeedsColumnTailOrNextLift` |
| 43 | 0.5 | 1155 | 0.5 | 1025 | 7514 | 0.563902 | 0.436098 | `{1: 138, 2: 80, 5: 28, 6: 196, 7: 186, 8: 103, 9: 12, 13: 282}` | `LiftPersistentNeedsColumnTailOrNextLift` |
| 43 | 0.9 | 1155 | 0 | 1025 | 7514 | 0.563902 | 0.436098 | `{1: 138, 2: 80, 5: 28, 6: 196, 7: 186, 8: 103, 9: 12, 13: 282}` | `LiftPersistentNeedsColumnTailOrNextLift` |
| 43 | 0.9 | 1155 | 0.5 | 1025 | 7514 | 0.563902 | 0.436098 | `{1: 138, 2: 80, 5: 28, 6: 196, 7: 186, 8: 103, 9: 12, 13: 282}` | `LiftPersistentNeedsColumnTailOrNextLift` |
| 43 | 0.9 | 1155 | 0 | 1025 | 7514 | 0.563902 | 0.436098 | `{1: 138, 2: 80, 5: 28, 6: 196, 7: 186, 8: 103, 9: 12, 13: 282}` | `LiftPersistentNeedsColumnTailOrNextLift` |
| 43 | 0.9 | 1155 | 0.5 | 1025 | 7514 | 0.563902 | 0.436098 | `{1: 138, 2: 80, 5: 28, 6: 196, 7: 186, 8: 103, 9: 12, 13: 282}` | `LiftPersistentNeedsColumnTailOrNextLift` |
| 47 | 0 | 665 | 0.25 | 1150 | 11480 | 0.767893 | 0.232107 | `{1: 51, 2: 78, 6: 64, 7: 158, 8: 92, 9: 33, 10: 4, 13: 670}` | `LiftPersistentNeedsColumnTailOrNextLift` |
| 47 | 0 | 1645 | 0.75 | 1145 | 11405 | 0.766208 | 0.233792 | `{1: 51, 2: 78, 6: 66, 7: 161, 8: 90, 9: 30, 10: 4, 13: 665}` | `LiftPersistentNeedsColumnTailOrNextLift` |
| 47 | 0 | 770 | 0.5 | 1512 | 14462 | 0.735755 | 0.264245 | `{1: 93, 2: 93, 6: 71, 7: 206, 8: 174, 9: 107, 10: 8, 13: 760}` | `LiftPersistentNeedsColumnTailOrNextLift` |
| 47 | 0 | 1540 | 0.5 | 1512 | 14462 | 0.735755 | 0.264245 | `{1: 93, 2: 93, 6: 71, 7: 206, 8: 174, 9: 107, 10: 8, 13: 760}` | `LiftPersistentNeedsColumnTailOrNextLift` |
| 47 | 0.5 | 1001 | 0.25 | 757 | 8188 | 0.832029 | 0.167971 | `{1: 31, 2: 3, 6: 5, 7: 60, 8: 133, 9: 44, 10: 4, 13: 477}` | `LiftPersistentNeedsColumnTailOrNextLift` |
| 47 | 0.5 | 1309 | 0.75 | 757 | 8188 | 0.832029 | 0.167971 | `{1: 31, 2: 3, 6: 5, 7: 60, 8: 133, 9: 44, 10: 4, 13: 477}` | `LiftPersistentNeedsColumnTailOrNextLift` |
| 47 | 0.5 | 1155 | 0 | 1133 | 10693 | 0.725983 | 0.274017 | `{1: 78, 2: 70, 6: 56, 7: 160, 8: 128, 9: 80, 10: 6, 13: 555}` | `LiftPersistentNeedsColumnTailOrNextLift` |
| 47 | 0.5 | 1155 | 0.5 | 1133 | 10693 | 0.725983 | 0.274017 | `{1: 78, 2: 70, 6: 56, 7: 160, 8: 128, 9: 80, 10: 6, 13: 555}` | `LiftPersistentNeedsColumnTailOrNextLift` |
| 47 | 0.9 | 1155 | 0 | 1133 | 10693 | 0.725983 | 0.274017 | `{1: 78, 2: 70, 6: 56, 7: 160, 8: 128, 9: 80, 10: 6, 13: 555}` | `LiftPersistentNeedsColumnTailOrNextLift` |
| 47 | 0.9 | 1155 | 0.5 | 1133 | 10693 | 0.725983 | 0.274017 | `{1: 78, 2: 70, 6: 56, 7: 160, 8: 128, 9: 80, 10: 6, 13: 555}` | `LiftPersistentNeedsColumnTailOrNextLift` |
| 47 | 0.9 | 1155 | 0 | 1133 | 10693 | 0.725983 | 0.274017 | `{1: 78, 2: 70, 6: 56, 7: 160, 8: 128, 9: 80, 10: 6, 13: 555}` | `LiftPersistentNeedsColumnTailOrNextLift` |
| 47 | 0.9 | 1155 | 0.5 | 1133 | 10693 | 0.725983 | 0.274017 | `{1: 78, 2: 70, 6: 56, 7: 160, 8: 128, 9: 80, 10: 6, 13: 555}` | `LiftPersistentNeedsColumnTailOrNextLift` |

## 5. 结构读数

这一步没有排除全部 forced persistent cap；它完成的是升层后的账本化。
若 cap 仍保持高 survival，说明固定低模方向帽不是最终证书，必须引入 column-tail 相位兼容行或继续升层。
若后续层 survival 连续下降，则进入 FiberDeletion/删除势；若下降停止，则进入 PDECEntropy 或 CleanKLS。
