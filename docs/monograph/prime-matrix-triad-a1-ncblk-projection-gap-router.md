# Triad-A1 NC-BLK 投影缺口路由器

**状态：** `ncblk_requires_moving_block_spread_or_external_dibfi`

NC-BLK 不能由当前 A1 fixed-projection diffuse 账本直接推出。当前最窄硬点继续压缩为：证明 moving-block spread 定理，或精确引用外部 DI/BFI 原始 dispersion。

## 1. 结构律

A1 diffuse/clean admission controls fixed finite signatures. NC-BLK is a moving-block statement over balanced same-(u,v) blocks created after well-factorable splitting. A sequence may be flat on every fixed finite projection while concentrating on a block whose label moves with the scale. Therefore fixed-projection flatness does not imply NC-BLK. Since BD-CEN, SOURCE-CEN, and raw BLK-energy have been blocked, the only honest internal route is a new moving-block spread theorem for the actual WFD coefficients; the honest external route is original DI/BFI dispersion with the required local variance subtraction.

```text
A1 diffuse branch controls fixed finite signatures;
NC-BLK asks for moving same-(u,v) block non-concentration;
fixed projection flatness does not control moving labels;
therefore NC-BLK needs MovingBlockSpread or external DI/BFI.
```

## 2. 汇总

- `a1_clean_status=a1_clean_kls_external_input_registered_self_contained_atom_open`。
- `sc9_frontier_status=a1_sc9_frontier_routed_to_ncblk_or_external_dibfi`。
- `fixed_projection_gap_exists=True`。
- `current_internal_ncblk_closed=False`。
- `terminal_gap_after_router=MovingBlockSpreadNCBLKOrExternalDIBFIOriginalDispersion`。
- `internal_route_status=open_needs_moving_block_spread_theorem`。
- `external_route_status=open_needs_precise_di_bfi_original_dispersion_citation`。

## 3. 缺口表

| gate | available from A1 | needed for NC-BLK | gap | route | closed |
| --- | --- | --- | --- | --- | --- |
| `FixedProjectionDiffuse` | for every fixed finite payment signature, mass tends to zero on the diffuse branch | uniform control over moving same-(u,v) blocks whose labels grow with the scale | fixed projections do not see moving blocks | needs moving-block spread input or external dispersion | `False` |
| `L2FlatFiniteAtoms` | max atom/L2-flat admission language after finite-projection dichotomy | arbitrary log saving in sum_b |S_b|^2 for actual WFD blocks | L2 flatness at fixed level gives no log^{-A} saving for an adversarial moving block family | needs scale-uniform L2 block-energy decay | `False` |
| `WellFactorableSupport` | well-factorable/dyadic decomposition of moduli | block non-concentration inside each balanced factor pair | well-factorable factorization allows decomposition but does not force each factor block to have zero local mean | needs original DI/BFI dispersion centering or source spread theorem | `False` |
| `CurrentNoGoResults` | BD-CEN, SOURCE-CEN, and raw BLK-energy routes are refuted/blocked | a new true source statement for actual coefficients | the existing square-kernel object cannot manufacture block centering after the fact | prove NC-BLK from upstream coefficient generation, not from the current kernel alone | `True` |

## 4. 可接受输入

| input | statement | would imply | status |
| --- | --- | --- | --- |
| `MovingBlockSpread` | for every balanced block b=(u,v), actual WFD mass in b has max block share o(log^{-A}) after dyadic/Type decomposition | NC-BLK block energy saving | `not_present_in_current_a1_ledger` |
| `SourceDispersionCentering` | the original dispersion identity enters KZ-E with same-(u,v) local variance already subtracted | BD-CEN/NC-BLK without changing the target | `refuted_for_current_rewritten_WFD_object; possible only from original DI/BFI theorem` |
| `ExternalDIBFIOriginalDispersion` | an external theorem directly estimates the uncentered WFD target or supplies the required local block variance subtraction | A1 clean branch closed in external-deep-theorem version | `acceptable_external_route` |

## 5. 当前结论

当前不能把 `NC-BLK` 标为已证。真正剩余已经比上一轮更窄：

```text
内部无黑箱版：证明 MovingBlockSpreadNCBLK；
外部深定理版：引用带局部方差扣除的 DI/BFI 原始 dispersion。
```

这一步的作用是排除“fixed-projection flat => moving-block NC-BLK”的隐含跳步。
