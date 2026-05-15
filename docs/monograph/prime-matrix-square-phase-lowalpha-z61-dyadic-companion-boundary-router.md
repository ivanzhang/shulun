# Prime Matrix square-phase low-alpha z=61 dyadic companion boundary

**状态：** `z61_dyadic_companion_boundary_requires_independent_square_window_input_open`

dyadic lift companion 的局部等价链已经闭合，但仓库内尚无独立的全局输入：`ShiftedLinearPrimePairGlobalBound`、`ShiftedSquareWindowGlobalBound`、`dyadic_lift_companion_proved_globally` 与 `PersistentPhase/MissingLift-PDEC` 排斥均未完成。因而当前自足路线的真正闭合边界是：提交独立 shifted-square-window 全局输入，或排斥该命名持久相位 PDEC。

```text
local_dyadic_companion_equivalence_closed=true
all_required_global_inputs_available=false
self_contained_row_column_closure_reached=false
row_column_unconditional_closed=false
```

## 1. Companion 公式

| object | value |
| --- | --- |
| phase modulus | `28842` |
| negative anchor | `{'quotient': 1, 'condition': 'one negative phase hit of weight w'}` |
| positive quotients | `[2, 4]` |
| same-p | `200003` |
| carry equation | `71*9767 - 2*37*9371 = 3` |
| linear forms | `{'a4': '71*132-1', 'a2': '74*132-1'}` |
| square congruence | `p^2 ≡ -527 mod 57684` |
| square window | `delta + M*span <= p-1 < delta + M*(span+1)` |
| recovered s | `132` |

## 2. 全局输入验收

| input | available |
| --- | --- |
| `dyadic_lift_companion_proved_globally` | false |
| `shifted_linear_prime_pair_global_bound_proved` | false |
| `shifted_square_window_global_bound_proved` | false |
| `positive_dyadic_lift_existence_proved_globally` | false |
| `persistent_phase_pdec_excluded` | false |
| `missing_lift_pdec_excluded` | false |

## 3. 证明边界

- 已闭合：当前 formal unit 的 dyadic companion 局部等价链。
- 未闭合：独立 shifted-square-window/shifted-prime-pair 全局输入，或命名 PersistentPhase/MissingLift-PDEC 排斥。
- 结论：不能据此宣称行/列命题无条件闭合。
- 下一目标：`IndependentShiftedSquareWindowInputOrPersistentPhasePDECExclusion`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-endpoint-shifted-factor-router.json` | `57d4e18eadd1bb072db598f782533b7ecefc942472cc8f26d9f0a285e97ad40e` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-fixed-core-cycle-nonpersistence-comparator.json` | `4355ad699530fda432357db4b1e8ddbdc0a021fc05f3c550110ecc3d580454d0` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-shifted-pair-bridge-router.json` | `25c354e6440e1f1f9a945cf96f54b86c1f854f20fdd804c109c4685d06596772` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-prefix-gate-signed-balance-router.json` | `b61d0ab0d155872ee3593f887979852ab2eed646cfa221751b3506ade13ee610` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-shifted-square-window-router.json` | `26ed4354b18ce54dc2ea66ce943e628fc02f80cacee97084cc3331a15cd17b83` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_dyadic_companion_boundary_router.py` | `a9271b5676552adb8acb3b01d757aa3d7a518645b902d13fc53663a64066cef4` |
