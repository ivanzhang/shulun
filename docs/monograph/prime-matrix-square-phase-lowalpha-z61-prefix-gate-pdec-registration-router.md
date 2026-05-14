# Prime Matrix square-phase low-alpha z=61 PrefixGate-PDEC 登记

**状态：** `z61_prefix_gate_pdec_registered_not_excluded`

Prefix interval gate 分支已登记为具体 PDEC 对象：相位条件是 `b≡0 mod 28842`，对应 `C=4807` 的 `2C/3C` 同核双命中。该登记闭合的是失败对象的形式化与可审查性，不是排斥证明；下一步必须排斥该 PrefixGate-PDEC，或证明全局 prefix gate 容量界。

```text
prefix_gate_pdec_registration_closed=true
formal_unit_key=z61|bucket=unbalanced<=8|omega=4|p=36739|C=4807|b=28842|prefixes=2,3
phase_condition=b ≡ 0 (mod 28842)
overlap_weight=0.555427
needed_lift_to_reach_model_scale=0.431957
overlap_lift_surplus_over_model=0.123469
prefix_gate_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. PDEC 对象

| field | value |
| --- | --- |
| formal unit | `z61|bucket=unbalanced<=8|omega=4|p=36739|C=4807|b=28842|prefixes=2,3` |
| phase | `b ≡ 0 (mod 28842)` |
| common core | `4807=[11, 19, 23]` |
| hit moduli | `[9614, 14421]` |
| prefixes | `[2, 3]` |
| selected splits | `[{'core_split': [23, 209], 'selected_prefixes': [2], 'selected_weight': 0.20202867877781977, 'prefix_interval': [1.1358695652173914, 2.2717391304347827]}, {'core_split': [19, 253], 'selected_prefixes': [2, 3], 'selected_weight': 0.3533979543127059, 'prefix_interval': [1.6644736842105263, 3.3289473684210527]}]` |

## 2. 证明边界

- 已闭合：PrefixGate-PDEC 失败对象登记。
- 未闭合：该 PDEC 的排斥，或全局 prefix gate 容量界。
- 下一目标：`PrefixGatePDECExclusionOrGlobalPrefixGateCapacityBound`。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-common-core-prefix-gate-router.json` | `56b5207324e01d527f6c9527df039385f562694b673051098784c076c3c7363f` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-hit-overlap-flip-router.json` | `ee5c1ebcec70df322e5c6df2c862ce7c43a7c6b0978df815cd8ae456920b31b5` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-overlap-common-core-router.json` | `4784443770637bbe4832130b0d33a9d72035071ad39e497e65ff67571c5d16d1` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_prefix_gate_pdec_registration_router.py` | `fa6b72456499c6e653750272300737a478f120edc386fe4b402323c82ead1a06` |
