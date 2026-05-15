# Prime Matrix square-phase BadTail parity/LPF router

**状态：** `square_phase_bad_tail_split_into_forced_parity_and_residual_lpf_layers_open`

`BadTail` 已进一步分解为两个刚性层：奇数 `t` 槽由奇偶性强制成为偶余因子坏槽；剩余坏槽只能发生在偶数 `t` 上，并且由一个奇最小素因子 `ell<=sqrt(m)` 解释。固定 `(q,ell)` 在同一侧不能复用槽，因为对应乘积区间长度小于 `1`。因此剩余硬点变为：平方锚素数数必须压过强制奇偶坏槽与残余 LPF 层；若残余层过密，则它应回流为低模最小因子 PDEC/SAE。

```text
max_p=5000
finite_prime_count=668
total_parity_failure_count=0
total_residual_lpf_failure_count=0
total_layer_reuse_failure_count=0
prime_beats_forced_plus_residual_proved=false
row_column_unconditional_closed=false
```

## 1. 奇偶强制层

对奇素数 `P` 与尾素 `q`，`a=P-q` 为偶数。槽余因子为

```text
m=P+a+t.
```

因此 `m` 的奇偶性只由 `t` 决定：`t` 为奇数时 `m` 为偶数且 `m>P>2`，所以必为合数。这部分 BadTail 是完全强制的，不是分布异常。

## 2. 残余 LPF 层

非奇偶强制的 BadTail 必在偶数 `t` 上，此时 `m` 为奇合数。取其最小素因子 `ell`，则

```text
ell <= sqrt(m),    m=P+a+t < 5P/4+2.
```

并且固定同侧 `q,ell` 至多贡献一个槽：因为 `q*ell*h` 落在长度为 `P` 的平方锚窗口内，而
`P/(q*ell)<1`。

## 3. 确定性判据

| name | status | statement |
| --- | --- | --- |
| `forced_parity_bad_tail` | `closed` | For odd P and tail prime q, a=P-q is even; hence m=P+a+t is even exactly when t is odd, so every odd-t slot is forced BadTail. |
| `residual_lpf_layer` | `closed` | Every BadTail not forced by parity has even t, odd composite m, and an odd least prime factor ell<=sqrt(m)<sqrt(5P/4+2). |
| `fixed_q_ell_nonreuse` | `closed` | For fixed sign, q, and ell, the product interval has length P/(q ell)<1, so a residual least-prime-factor layer contributes at most one slot. |
| `remaining_prime_vs_forced_plus_residual` | `open` | A global proof still needs square-anchor primes to beat forced parity slots plus residual LPF layers, or a PDEC/SAE return from residual over-density. |

## 4. 有限审计摘要

| metric | plus | minus | combined |
| --- | ---: | ---: | ---: |
| square-anchor primes | 97145 | 97396 | 194541 |
| forced parity BadTail | 22899 | 20298 | 43197 |
| residual LPF BadTail | 15333 | 17440 | 32773 |
| total BadTail | 38232 | 37738 | 75970 |

最紧单侧样本：`P=3`，`sign=plus`，`Prime=1`，`Forced=0`，`Residual=0`，`margin=1`。

## 5. 样本表

| P | sign | Prime | BadTail | forced parity | residual LPF | Prime-Bad | Prime-Forced |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 13 | `plus` | 3 | 1 | 1 | 0 | 2 | 2 |
| 13 | `minus` | 3 | 1 | 0 | 1 | 2 | 3 |
| 17 | `plus` | 1 | 0 | 0 | 0 | 1 | 1 |
| 17 | `minus` | 3 | 0 | 0 | 0 | 3 | 3 |
| 19 | `plus` | 3 | 1 | 1 | 0 | 2 | 2 |
| 19 | `minus` | 4 | 1 | 0 | 1 | 3 | 4 |
| 23 | `plus` | 2 | 1 | 1 | 0 | 1 | 1 |
| 23 | `minus` | 3 | 1 | 0 | 1 | 2 | 3 |
| 29 | `plus` | 4 | 0 | 0 | 0 | 4 | 4 |
| 29 | `minus` | 5 | 0 | 0 | 0 | 5 | 5 |
| 31 | `plus` | 5 | 1 | 1 | 0 | 4 | 4 |
| 31 | `minus` | 4 | 1 | 0 | 1 | 3 | 4 |
| 101 | `plus` | 11 | 4 | 2 | 2 | 7 | 9 |
| 101 | `minus` | 12 | 3 | 2 | 1 | 9 | 10 |
| 499 | `plus` | 40 | 16 | 11 | 5 | 24 | 29 |
| 499 | `minus` | 44 | 17 | 8 | 9 | 27 | 36 |
| 1009 | `plus` | 72 | 25 | 20 | 5 | 47 | 52 |
| 1009 | `minus` | 70 | 27 | 14 | 13 | 43 | 56 |
| 2003 | `plus` | 125 | 47 | 31 | 16 | 78 | 94 |
| 2003 | `minus` | 139 | 52 | 24 | 28 | 87 | 115 |
| 4999 | `plus` | 300 | 117 | 74 | 43 | 183 | 226 |
| 4999 | `minus` | 289 | 114 | 56 | 58 | 175 | 233 |

## 6. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `ForcedParityLayerClosed` | `true` | `true` | 奇数 t 槽必为偶余因子，因而必是 BadTail。 | closed |
| `ResidualLPFLayerClosed` | `true` | `true` | 非奇偶强制的 BadTail 已压成互不复用的最小素因子层。 | closed |
| `PrimeBeatsForcedPlusResidual` | `false` | `false` | 仍需全局证明平方锚素数数压过强制奇偶坏槽与残余 LPF 层总量。 | SquarePhasePrimeBeatsForcedParityPlusResidualLPFLayers |
| `ResidualLayerPDECReturn` | `false` | `false` | 若残余 LPF 层过密，必须抽取固定低模最小因子相位缺陷。 | ResidualLPFLayerPDECSAEReturn |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只关闭 BadTail 内部分层，不关闭全局行/列命题。 | SquarePhasePrimeBeatsForcedParityPlusResidualLPFLayers OR ResidualLPFLayerPDECSAEReturn |

## 7. 下一步

- 主攻：`SquarePhasePrimeBeatsForcedParityPlusResidualLPFLayers`。
- 备选回流：`ResidualLPFLayerPDECSAEReturn`。
- 必须诚实保留边界：本步没有证明平方锚素数全局下界；它只把 BadTail 的内部坏槽来源拆成强制奇偶层与残余 LPF 层。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/square-phase-bad-tail-parity-lpf-ledger.json` | `32e5c6d2daa9306d21847383e87284e626e8362d32d37814ec8b84753bf1d8fd` |
| `experiments/prime_matrix_square_phase_bad_tail_parity_lpf_router.py` | `1fdc832688665a10c7e7fccb56a6b68b28e4133a984672fd1fa4eebfd7db2cde` |
