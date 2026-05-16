# Prime Matrix AffineTwin endpoint-release moving-slot graph-cap route audit

**状态：** `current_sweep_anonymous_moving_slot_support_escape_routed_global_open`

本审计把上一层 `support-graph cap` 的剩余 moving-slot 出口拆成可检查路由：固定或同向移动的 AffineTwin 槽仍受图容量控制；真正移动支撑则必须支付双端点释放、破坏固定 primitive 深度身份，或进入 moving-key/source/ColumnCRT/SAE 出口。

```text
current_q=31
current_support_graph_cap=20
current_sqrt_floor=29
fixed_candidate_q_values=[31, 43, 103]
all_fixed_candidate_graph_caps_passed=true
support_motion_candidate_count=11
all_support_motion_requires_both_endpoint_release=true
exact_rematerialized_q_values=[]
anonymous_moving_slot_actual_overload_closed_current_sweep=true
```

## 1. fixed-family graph cap

| q | width | sqrt floor | width^2 | q(q-2)-width^2 | symbolic margin | realized | graph cap passed |
| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 31 | 20 | 29 | 400 | 499 | 1996 | true | true |
| 43 | 26 | 41 | 676 | 1087 | 4348 | false | true |
| 103 | 56 | 101 | 3136 | 7267 | 29068 | false | true |

## 2. moving-slot route table

| gate | closed | route if fails | evidence |
| --- | --- | --- | --- |
| `FixedOrMovedAffineTwinGraphCap` | true | `ProjectionCollision-PDEC / ProductAccountingTightening` | all candidate widths W=(q+9)/2 satisfy W^2<=q(q-2); current fixed q=31 has graph cap 20 and sqrt floor 29 |
| `SamePrimitiveSupportMotion` | true | `MovingSupportDepthInflation-PDEC/SAE` | 11 candidates all require both endpoint releases; narrowest atom 19:12 needs release 70 against support width 20 |
| `FixedPrimitiveDepthIdentity` | true | `MovingPrimitiveKey-PDEC/SAE` | all 11 candidates break both generator and fill depth identities; minimum defect is 70 |
| `SameOrientationMovingKeyDepthFormula` | true | `OrientationChangingPrimitiveKey-PDEC/SAE` | no support-motion depth gives a common q; narrowest atom 19:12 gives q_g=111 and q_f=61 |
| `MovingKeySourceRematerialization` | true | `SourceRematerialization-PDEC/SAE` | 19 candidate q values; exact rematerialized q values = []; route histogram = {'CompositeQ': 13, 'PrimeButNotTwinAffine': 6} |
| `MovingFamilyColumnCRTOrSAE` | true | `ColumnCRT/PDEC or moving-family SAE` | moving-family candidate q values = [31, 43, 103]; realized q values = [31]; fixed q/fixed residue ColumnCRT routing is closed in the current ledger |

## 3. 当前显式矛盾读数

- 固定 actual 图像：`support_graph_cap=20`，而 `sqrt_floor=29`，固定槽没有 actual 超平方根负载。
- 最窄支撑运动 atom `19:12` 要求共同深度 `58`，端点释放 `70`，是支撑宽度 `20` 的 `3.50` 倍。
- 同向 moving-key 深度公式在最窄 atom `19:12` 给出 `q_g=111` 与 `q_f=61`，差 `50`，不能形成同一 primitive key。
- 深度公式吐出的 `19` 个候选 `q` 没有任何精确 source 重物化：`exact_rematerialized_q_values=[]`，路由直方图为 `{'CompositeQ': 13, 'PrimeButNotTwinAffine': 6}`。

## 4. 结论边界

当前 sweep 内不存在匿名 moving-slot actual overload：若仍保留 AffineTwin 固定图像，图容量自动低于平方根门；若移动支撑，则必须进入双端点释放、深度身份破坏、moving-key 公式失败、source 重物化失败或 ColumnCRT/SAE 路由。

这一步仍不是行/列命题的全局无条件闭合。全局剩余被压成 `MovingSlotFamilyPersistenceNoGo`、方向改变 primitive key、source-rematerialization、`ColumnCRT/PDEC` 与 unused-target arrival 的族级排斥或可求和控制。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-endpoint-release-support-graph-cap-ledger.json` | `51c3143a936264617d47fff2643948dc806b44fabe3bcbf8380508634fd3b966` |
| `data/prime-matrix-affine-twin-support-motion-depth-ledger.json` | `0e2786c4a32ee35a38c027a4cadfe59cda82e09b51939d935fb476762c9700c7` |
| `data/prime-matrix-affine-twin-support-motion-primitive-defect-ledger.json` | `7c63e2c3bd443a430ef7f633d1359f88c65ead388b69f34a0e0f9d72ccb32ef4` |
| `data/prime-matrix-affine-twin-moving-key-depth-formula-ledger.json` | `a7b409c9a56a1d073c4cc77577aa128bc872b7b2c688381d3467e85ddd665583` |
| `data/prime-matrix-affine-twin-moving-key-source-rematerialization-ledger.json` | `b7d9016b2e43da9d390efdde3012739d24305e4843ed29efc8c295d16dc52fd6` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-moving-family-sae-columncrt-ledger.json` | `2e401269ab68cb196babfb74e6f7b63c946ee9de37bc6ab5d502f49deaa7bf28` |
