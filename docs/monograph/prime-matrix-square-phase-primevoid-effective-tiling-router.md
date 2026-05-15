# Prime Matrix square-phase prime-void effective tiling

**状态：** `square_phase_primevoid_reduced_to_full_effective_semiprime_tiling_open`

`Prime=0` 反例已被改写成一个完全铺砖对象：`alpha=4/5` 低筛后的每一个幸存列，都必须恰好由一个高尾近方半素数槽 `q(P+a+t)` 覆盖；铺砖缺口数精确等于平方锚素数数。因此下一步不再是抽象短区间素数问题，而是排除这种 full effective semiprime tiling，或把完全铺砖的相位刚性登记为 PDEC/SAE。

```text
max_p=5000
finite_prime_count=668
equivalence_failure_count=0
finite_prime_void_count=0
full_effective_tiling_excluded_proved=false
row_column_unconditional_closed=false
```

## 1. 完全铺砖等价

在有效容量口径下：

```text
H = Prime + GoodShell
C_eff = GoodShell
H-C_eff = Prime.
```

所以 `Prime=0` 当且仅当 `H=C_eff`，也就是低筛后所有幸存列都被有效高尾半素数槽完全铺满。反例不再是无结构的空素数窗口，而是一个 full effective semiprime tiling。

## 2. 确定性判据

| name | status | statement |
| --- | --- | --- |
| `prime_void_full_effective_tiling_equivalence` | `closed` | For each sign, Prime=0 is equivalent to the low-survivor set being fully tiled by effective high-tail semiprime slots. |
| `tiling_deficit_equals_prime_count` | `closed` | The deficit H-C_eff is exactly the square-anchor prime count; the missing columns are precisely prime columns. |
| `prime_void_pdec_object` | `open` | A Prime=0 counterexample is no longer an unstructured prime gap; it is a complete near-square semiprime tiling of every alpha=4/5 low survivor. |

## 3. 有限审计摘要

| metric | plus | minus | combined |
| --- | ---: | ---: | ---: |
| H total | 102191 | 102739 | 204930 |
| effective slots | 5046 | 5343 | 10389 |
| tiling deficit / primes | 97145 | 97396 | 194541 |

最小铺砖缺口样本：`P=3`，`sign=plus`，`deficit=1`。

## 4. 样本表

| P | sign | H | effective slots | deficit | prime count | prime void | full tiling |
| ---: | --- | ---: | ---: | ---: | ---: | --- | --- |
| 13 | `plus` | 3 | 0 | 3 | 3 | `false` | `false` |
| 13 | `minus` | 3 | 0 | 3 | 3 | `false` | `false` |
| 17 | `plus` | 1 | 0 | 1 | 1 | `false` | `false` |
| 17 | `minus` | 3 | 0 | 3 | 3 | `false` | `false` |
| 19 | `plus` | 3 | 0 | 3 | 3 | `false` | `false` |
| 19 | `minus` | 4 | 0 | 4 | 4 | `false` | `false` |
| 23 | `plus` | 3 | 1 | 2 | 2 | `false` | `false` |
| 23 | `minus` | 3 | 0 | 3 | 3 | `false` | `false` |
| 29 | `plus` | 4 | 0 | 4 | 4 | `false` | `false` |
| 29 | `minus` | 5 | 0 | 5 | 5 | `false` | `false` |
| 31 | `plus` | 5 | 0 | 5 | 5 | `false` | `false` |
| 31 | `minus` | 4 | 0 | 4 | 4 | `false` | `false` |
| 101 | `plus` | 11 | 0 | 11 | 11 | `false` | `false` |
| 101 | `minus` | 12 | 0 | 12 | 12 | `false` | `false` |
| 499 | `plus` | 42 | 2 | 40 | 40 | `false` | `false` |
| 499 | `minus` | 45 | 1 | 44 | 44 | `false` | `false` |
| 1009 | `plus` | 79 | 7 | 72 | 72 | `false` | `false` |
| 1009 | `minus` | 77 | 7 | 70 | 70 | `false` | `false` |
| 2003 | `plus` | 132 | 7 | 125 | 125 | `false` | `false` |
| 2003 | `minus` | 144 | 5 | 139 | 139 | `false` | `false` |
| 4999 | `plus` | 317 | 17 | 300 | 300 | `false` | `false` |
| 4999 | `minus` | 303 | 14 | 289 | 289 | `false` | `false` |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `PrimeVoidFullEffectiveTilingEquivalenceClosed` | `true` | `true` | `Prime=0` 与低洞被有效半素数槽完全铺满已严格等价。 | closed |
| `FinitePrimeVoidAbsent` | `true` | `false` | 有限扫描 P<=5000 没有 prime-void 样本。 | finite evidence only |
| `FullEffectiveTilingExcluded` | `false` | `false` | 仍需全局排除完全有效半素数铺砖，或把它转成 PDEC/SAE。 | PrimeVoidFullEffectiveSemiprimeTilingExclusion |
| `FullTilingPDECReturn` | `false` | `false` | 若完全铺砖存在，必须抽取近方半素数槽的全覆盖相位缺陷。 | FullEffectiveTilingPDECSAEReturn |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只关闭反例形态等价，不关闭全局行/列命题。 | PrimeVoidFullEffectiveSemiprimeTilingExclusion OR FullEffectiveTilingPDECSAEReturn |

## 6. 下一步

- 主攻：`PrimeVoidFullEffectiveSemiprimeTilingExclusion`。
- 备选回流：`FullEffectiveTilingPDECSAEReturn`。
- 需要证明 full effective semiprime tiling 不可能全局持续，或证明其完全相位贴合必产生 PDEC/SAE。有限扫描没有 prime-void，但这只作为诊断。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/square-phase-primevoid-effective-tiling-ledger.json` | `2a447bbe68b8a9a2269bdb8ad8882ad77b95f1367689cee5d605bd33f476e779` |
| `experiments/prime_matrix_square_phase_primevoid_effective_tiling_router.py` | `571adc584832e2902c55bd88a85ca9927be237066bed9b156b2c37a575b6ba66` |
