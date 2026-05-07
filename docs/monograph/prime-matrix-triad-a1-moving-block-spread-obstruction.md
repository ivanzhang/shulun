# Triad-A1 MovingBlockSpread 阻断证书

**状态：** `moving_block_spread_not_implied_by_fixed_projection_diffuse`

当前 ledger 不能直接证明 MovingBlockSpreadNCBLK：存在投影不可见模型，固定投影 diffuse 与 moving-block 集中可同时成立。内部无黑箱路线必须新增 SourceBlockEntropyNCBLK。

## 1. 投影不可见性律

固定投影只记录 fixed signature 的总质量。若每个 fixed signature 下还有随尺度增长的 hidden moving-block fiber，则集中模型和分散模型可以有完全相同的固定投影账本，但 moving-block 二能量相差 hidden_fiber_size 倍。

Fixed-projection diffuse only says each named fixed signature eventually receives small mass. It does not impose arbitrary-log decay on the hidden same-(u,v) moving block energy. Therefore MovingBlockSpreadNCBLK requires a new source-block entropy/non-concentration theorem or an external DI/BFI dispersion theorem.

```text
fixed projection ledger sees only total mass per fixed signature；
moving-block NC-BLK needs energy per growing block b=(u,v)；
hidden moving fibers can concentrate while fixed signatures keep diffusing。
```

## 2. 汇总

- `ncblk_input_status=ncblk_requires_moving_block_spread_or_external_dibfi`。
- `all_rows_concentrated_model_violates_required_energy=True`。
- `max_fixed_signature_mass_decreases=True`。
- `next_internal_target=SourceBlockEntropyNCBLK`。
- `terminal_gap_after_router=SourceBlockEntropyNCBLKOrExternalDIBFIOriginalDispersion`。

## 3. 模型审计表

| k | log y | fixed signatures | hidden fiber | max fixed mass | concentrated energy | spread energy | required | violates | ratio |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| 3 | 6.90776 | 6 | 6 | 0.166667 | 0.166667 | 0.0277778 | 0.00043919 | `True` | 6 |
| 4 | 9.21034 | 9 | 9 | 0.111111 | 0.111111 | 0.0123457 | 0.000138962 | `True` | 9 |
| 5 | 11.5129 | 11 | 11 | 0.0909091 | 0.0909091 | 0.00826446 | 5.6919e-05 | `True` | 11 |
| 6 | 13.8155 | 13 | 13 | 0.0769231 | 0.0769231 | 0.00591716 | 2.74494e-05 | `True` | 13 |
| 7 | 16.1181 | 16 | 16 | 0.0625 | 0.0625 | 0.00390625 | 1.48165e-05 | `True` | 16 |
| 8 | 18.4207 | 18 | 18 | 0.0555556 | 0.0555556 | 0.00308642 | 8.68515e-06 | `True` | 18 |
| 9 | 20.7233 | 20 | 20 | 0.05 | 0.05 | 0.0025 | 5.4221e-06 | `True` | 20 |

## 4. 结论

这不是行命题最终证明，而是排除一个隐藏跳步：

```text
fixed-projection diffuse 不能推出 MovingBlockSpreadNCBLK。
```

下一步若坚持无黑箱路线，必须证明更强的源头块熵命题：

```text
SourceBlockEntropyNCBLK:
actual WFD/Type-I-II/Fourier/well-factorable coefficients distribute over
moving same-(u,v) blocks with enough entropy to force block-energy log saving。
```

否则只能转入外部 `DI/BFI original dispersion` 引用路线。
