# Prime Matrix square-phase off-band prefix gap shadow shape router

**状态：** `multivoid_gap_shadow_reduced_to_shape_pdec_or_moving_depth_sae_open`

本步把多 atom prime-void gap shadow 进一步登记成形状键：每个失败模板由 side、W、实际前缀数 N、强制空 atom 数 V，以及有序 band/k 原子确定。持久失败若形状固定且 k 有界，则进入 FixedSmallK-PDEC/ColumnCRT；若 k 或深度漂移，则进入 MovingDepth-SAE。有限账本只给出形状样本，不构成全局排斥。

```text
input_ledger=data/square-phase-offband-prefix-gap-shadow-ledger.json
template_count=27
shape_count=15
active_shadow_count=0
row_column_unconditional_closed=false
```

## 1. 形状键

每个 failure 模板登记为

```text
shape_key = side | W | N | V | ordered(band:k)
```

其中 `V` 是 failure 强制 prime-void 的 atom 数。这个键只记录结构形状，不把有限样本当成全局规律。

## 2. 分流

| route | count |
| --- | ---: |
| `FixedSmallK-PDEC/ColumnCRT` | 27 |

固定小 `k` 的持久形状进入 PDEC/ColumnCRT；随 `k` 或深度漂移的形状进入 MovingDepth-SAE。

## 3. 形状摘要

| count | route | shape | P range | candidates | examples |
| ---: | --- | --- | --- | --- | --- |
| 5 | `FixedSmallK-PDEC/ColumnCRT` | `side=minus|W=1|N=3|V=3|plus_only_noslot:k0,both_offband_middle:k0,plus_only_noslot:k1` | 73..419 | 5..13 | P=73 minus ['plus_only_noslot:k0:67-71', 'both_offband_middle:k0:65-65', 'plus_only_noslot:k1:61-61']; P=157 minus ['plus_only_noslot:k0:147-155', 'both_offband_middle:k0:145-145', 'plus_only_noslot:k1:139-139']; P=199 minus ['plus_only_noslot:k0:187-197', 'both_offband_middle:k0:185-185', 'plus_only_noslot:k1:177-179'] |
| 3 | `FixedSmallK-PDEC/ColumnCRT` | `side=minus|W=1|N=2|V=2|plus_only_noslot:k0,both_offband_middle:k0` | 37..47 | 3..3 | P=37 minus ['plus_only_noslot:k0:33-35', 'both_offband_middle:k0:31-31']; P=43 minus ['plus_only_noslot:k0:39-41', 'both_offband_middle:k0:37-37']; P=47 minus ['plus_only_noslot:k0:43-45', 'both_offband_middle:k0:41-41'] |
| 3 | `FixedSmallK-PDEC/ColumnCRT` | `side=plus|W=1|N=3|V=3|both_offband_middle:k0,minus_only_noslot:k0,both_offband_middle:k1` | 421..683 | 6..6 | P=421 plus ['both_offband_middle:k0:401-401', 'minus_only_noslot:k0:393-399', 'both_offband_middle:k1:387-387']; P=523 plus ['both_offband_middle:k0:501-501', 'minus_only_noslot:k0:493-499', 'both_offband_middle:k1:485-485']; P=683 plus ['both_offband_middle:k0:657-657', 'minus_only_noslot:k0:649-655', 'both_offband_middle:k1:639-639'] |
| 3 | `FixedSmallK-PDEC/ColumnCRT` | `side=plus|W=1|N=3|V=3|both_offband_middle:k0,minus_only_noslot:k0,minus_only_noslot:k1` | 73..487 | 3..8 | P=73 plus ['both_offband_middle:k0:65-65', 'minus_only_noslot:k0:63-63', 'minus_only_noslot:k1:59-59']; P=113 plus ['both_offband_middle:k0:103-103', 'minus_only_noslot:k0:99-101', 'minus_only_noslot:k1:95-95']; P=487 plus ['both_offband_middle:k0:465-465', 'minus_only_noslot:k0:457-463', 'minus_only_noslot:k1:445-449'] |
| 2 | `FixedSmallK-PDEC/ColumnCRT` | `side=minus|W=2|N=3|V=2|plus_only_noslot:k0,plus_only_noslot:k1` | 673..691 | 15..16 | P=691 minus ['plus_only_noslot:k0:667-689', 'plus_only_noslot:k1:649-653']; P=673 minus ['plus_only_noslot:k0:649-671', 'plus_only_noslot:k1:631-637'] |
| 2 | `FixedSmallK-PDEC/ColumnCRT` | `side=plus|W=1|N=3|V=3|minus_only_noslot:k0,minus_only_noslot:k1,minus_only_noslot:k2` | 313..1129 | 8..14 | P=313 plus ['minus_only_noslot:k0:289-295', 'minus_only_noslot:k1:281-283', 'minus_only_noslot:k2:273-275']; P=1129 plus ['minus_only_noslot:k0:1083-1095', 'minus_only_noslot:k1:1065-1071', 'minus_only_noslot:k2:1051-1055'] |
| 1 | `FixedSmallK-PDEC/ColumnCRT` | `side=minus|W=2|N=3|V=2|both_offband_middle:k0,plus_only_noslot:k1` | 691..691 | 4..4 | P=691 minus ['both_offband_middle:k0:665-665', 'plus_only_noslot:k1:649-653'] |
| 1 | `FixedSmallK-PDEC/ColumnCRT` | `side=minus|W=2|N=3|V=2|plus_only_noslot:k0,both_offband_middle:k0` | 691..691 | 13..13 | P=691 minus ['plus_only_noslot:k0:667-689', 'both_offband_middle:k0:665-665'] |
| 1 | `FixedSmallK-PDEC/ColumnCRT` | `side=minus|W=2|N=3|V=2|plus_only_noslot:k0,plus_only_noslot:k2` | 673..673 | 15..15 | P=673 minus ['plus_only_noslot:k0:649-671', 'plus_only_noslot:k2:619-623'] |
| 1 | `FixedSmallK-PDEC/ColumnCRT` | `side=minus|W=2|N=3|V=2|plus_only_noslot:k1,plus_only_noslot:k2` | 673..673 | 7..7 | P=673 minus ['plus_only_noslot:k1:631-637', 'plus_only_noslot:k2:619-623'] |
| 1 | `FixedSmallK-PDEC/ColumnCRT` | `side=plus|W=1|N=1|V=1|both_offband_middle:k0` | 23..23 | 1..1 | P=23 plus ['both_offband_middle:k0:19-19'] |
| 1 | `FixedSmallK-PDEC/ColumnCRT` | `side=plus|W=1|N=3|V=3|minus_only_noslot:k0,both_offband_middle:k1,minus_only_noslot:k1` | 293..293 | 6..6 | P=293 plus ['minus_only_noslot:k0:271-275', 'both_offband_middle:k1:265-265', 'minus_only_noslot:k1:261-263'] |
| 1 | `FixedSmallK-PDEC/ColumnCRT` | `side=plus|W=2|N=3|V=2|minus_only_noslot:k0,both_offband_middle:k2` | 733..733 | 6..6 | P=733 plus ['minus_only_noslot:k0:697-705', 'both_offband_middle:k2:675-675'] |
| 1 | `FixedSmallK-PDEC/ColumnCRT` | `side=plus|W=2|N=3|V=2|minus_only_noslot:k0,minus_only_noslot:k1` | 733..733 | 9..9 | P=733 plus ['minus_only_noslot:k0:697-705', 'minus_only_noslot:k1:681-687'] |
| 1 | `FixedSmallK-PDEC/ColumnCRT` | `side=plus|W=2|N=3|V=2|minus_only_noslot:k1,both_offband_middle:k2` | 733..733 | 5..5 | P=733 plus ['minus_only_noslot:k1:681-687', 'both_offband_middle:k2:675-675'] |

## 4. 命题行

| name | status | statement |
| --- | --- | --- |
| `gap_shadow_template_shape_key` | `closed` | Every multi-void prefix failure template has a canonical shape key built from side, W, N, V and ordered band/k atoms. |
| `fixed_shape_or_moving_depth_route` | `closed` | A persistent shadow must enter either a fixed small-k PDEC/ColumnCRT family or a moving-depth SAE family. |
| `finite_shape_ledger` | `finite_evidence` | The finite ledger lists the observed hypothetical shadow shapes and their examples. |
| `global_shape_family_exclusion` | `open` | A global proof still needs to exclude every fixed shape family or supply a summable moving-depth SAE bound. |

## 5. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `ShapeKeyRegistrationClosed` | `true` | `true` | 多空 atom 失败模板已有规范形状键。 | closed |
| `FixedShapeOrMovingDepthDichotomyClosed` | `true` | `true` | 持久失败分流为固定形状 PDEC/ColumnCRT 或移动深度 SAE。 | closed |
| `FiniteNoActiveShapeFailure` | `true` | `false` | 有限账本没有真实 active shadow；这里只是形状证据。 | finite evidence only |
| `GlobalShapeFamiliesExcluded` | `false` | `false` | 仍需排斥固定形状族或给出移动深度可求和。 | FixedPrefixGapShadowShapePDECOrMovingDepthSAEExclusion |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只完成形状分流，不关闭全局行/列命题。 | FixedPrefixGapShadowShapePDECOrMovingDepthSAEExclusion |

## 6. 下一步

- 主攻：`FixedPrefixGapShadowShapePDECOrMovingDepthSAEExclusion`。
- 对固定小 `k` 形状，需要构造 ColumnCRT/PDEC 排斥。
- 对移动深度形状，需要给出可求和 SAE 或证明其不可能持久。
- 当前仍未证明全局行/列无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_shape_router.py` | `d48eb4ffecbe7bd236bdb568f1db7b1443da0e4718165aafa02b2349911a9ba2` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_router.py` | `6fac77056cdc883354f2d7c8ffe2e2331928cfaadb9e849960fbde9b36d23c65` |
| `data/square-phase-offband-prefix-gap-shadow-ledger.json` | `f80e634e8dd67f202e02c0466af8df409217cc4b623b72d519612ee873fd3a74` |
| `data/square-phase-offband-prefix-gap-shadow-shape-ledger.json` | `dbe7b6ec327be0078b515b824004ffea5461a9e5285d85ea5539930ccea79e0d` |
