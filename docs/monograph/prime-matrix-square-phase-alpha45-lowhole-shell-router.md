# Prime Matrix square-phase alpha=4/5 lowhole shell

**状态：** `square_phase_alpha45_lowhole_shell_reduced_to_prime_vs_badtail_open`

`alpha=4/5` 的平方锚低洞已经从粗下界问题压成精确净余量恒等式：低洞 `H` 等于平方锚素数数加好半素数壳层数，尾容量 `C` 等于同一好半素数壳层数加坏尾复合余因子命中数，所以 `H-C = Prime - BadTail`。有限审计在样本范围内两侧余量均为正；但全局仍需证明 `Prime>BadTail`，或证明失败会产生已登记的 PDEC/SAE 相位缺陷。

```text
max_p=5000
finite_prime_count=668
identity_failure_count=0
finite_prime_dominance_failure_count=0
global_prime_dominates_badtail_proved=false
row_column_unconditional_closed=false
```

## 1. 精确恒等式

设 `y=floor(4P/5)`，`H_y^±(P)` 为 `P^2±r` 中未被 `q<=y` 覆盖的列数，`C_y^±(P)` 为尾素 `y<q<P` 的固定相位容量。

若低洞列对应的 `P^2±r` 合成，则其最小素因子必在 `(y,P)`，余因子必为素数且位于 `P` 之后的短壳层。因此低洞只有两类：平方锚素数，或近方半素数壳层。

同一个近方半素数壳层又恰好贡献尾容量中的 good high 命中，所以逐侧有

```text
H_y^± = Prime^± + GoodShell^±
C_y^± = GoodShell^± + BadTail^±
H_y^± - C_y^± = Prime^± - BadTail^±
```

这一步把 `SquarePhaseAlphaFourFifthsLowHoleLowerBound` 压窄为 `Prime>BadTail` 的净余量问题。

## 2. 壳层相位公式

写尾素因子和余因子为

```text
q=P-a,     m=P+b=P+a+d
```

plus 侧 `P^2+r=(P-a)(P+a+d)`，故

```text
r = P*d - a*(a+d),    1<=r<P.
```

minus 侧 `P^2-r=(P-a)(P+a+d)`，故

```text
r = a*(a+d) - P*d,    1<=r<P.
```

这正是平方锚 `P^2±r` 的薄双曲壳层；两侧分别位于同一相位曲面的上下侧。

## 3. 确定性判据

| name | status | statement |
| --- | --- | --- |
| `alpha45_lowhole_prime_semiprime_dichotomy` | `closed` | For alpha=4/5, every low survivor of P^2±r is either a square-anchor prime or a near-square semiprime (P-a)(P+b) with P-a in (4P/5,P). |
| `tail_capacity_good_bad_split` | `closed` | The high-tail capacity C splits exactly as good semiprime-shell hits plus bad composite-cofactor hits. |
| `net_margin_identity` | `closed` | For each sign, H_{4P/5}^sign-C_{4P/5}^sign equals square-anchor-prime-count minus bad-tail-composite-cofactor-count. |
| `alpha45_finite_prime_dominance` | `diagnostic_only` | In the scanned range, the prime count beats the bad-tail composite-cofactor count on both signs; this is finite evidence only. |
| `remaining_prime_vs_badtail_input` | `open` | A global proof still needs square-anchor primes to dominate bad-tail composite cofactors, or a proof that failure routes to PDEC/SAE. |

## 4. 有限审计摘要

| metric | plus | minus |
| --- | ---: | ---: |
| prime total | 97145 | 97396 |
| bad tail total | 38232 | 37738 |
| semiprime shell total | 5046 | 5343 |

最紧样本：

- plus 最小 `Prime-BadTail`：`P=3`，`Prime=1`，`BadTail=0`，`margin=1`。
- minus 最小 `Prime-BadTail`：`P=3`，`Prime=1`，`BadTail=0`，`margin=1`。
- combined 最小 `Prime-BadTail`：`P=3`，`Prime=2`，`BadTail=0`，`margin=2`。

## 5. 样本表

| P | sign | H | C | Prime | GoodShell | BadTail | Prime-BadTail | shell d-range |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 13 | `plus` | 3 | 1 | 3 | 0 | 1 | 2 | None..None |
| 13 | `minus` | 3 | 1 | 3 | 0 | 1 | 2 | None..None |
| 17 | `plus` | 1 | 0 | 1 | 0 | 0 | 1 | None..None |
| 17 | `minus` | 3 | 0 | 3 | 0 | 0 | 3 | None..None |
| 19 | `plus` | 3 | 1 | 3 | 0 | 1 | 2 | None..None |
| 19 | `minus` | 4 | 1 | 4 | 0 | 1 | 3 | None..None |
| 23 | `plus` | 3 | 2 | 2 | 1 | 1 | 1 | 2..2 |
| 23 | `minus` | 3 | 1 | 3 | 0 | 1 | 2 | None..None |
| 29 | `plus` | 4 | 0 | 4 | 0 | 0 | 4 | None..None |
| 29 | `minus` | 5 | 0 | 5 | 0 | 0 | 5 | None..None |
| 31 | `plus` | 5 | 1 | 5 | 0 | 1 | 4 | None..None |
| 31 | `minus` | 4 | 1 | 4 | 0 | 1 | 3 | None..None |
| 101 | `plus` | 11 | 4 | 11 | 0 | 4 | 7 | None..None |
| 101 | `minus` | 12 | 3 | 12 | 0 | 3 | 9 | None..None |
| 499 | `plus` | 42 | 18 | 40 | 2 | 16 | 24 | 4..8 |
| 499 | `minus` | 45 | 18 | 44 | 1 | 17 | 27 | 10..10 |
| 1009 | `plus` | 79 | 32 | 72 | 7 | 25 | 47 | 2..50 |
| 1009 | `minus` | 77 | 34 | 70 | 7 | 27 | 43 | 0..42 |
| 2003 | `plus` | 132 | 54 | 125 | 7 | 47 | 78 | 6..88 |
| 2003 | `minus` | 144 | 57 | 139 | 5 | 52 | 87 | 0..90 |
| 4999 | `plus` | 317 | 134 | 300 | 17 | 117 | 183 | 2..250 |
| 4999 | `minus` | 303 | 128 | 289 | 14 | 114 | 175 | 0..238 |

## 6. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `Alpha45LowholeShellIdentityClosed` | `true` | `true` | 低洞、尾容量和净余量三条恒等式均已逐项登记。 | closed |
| `FinitePrimeBeatsBadTailBothSigns` | `true` | `false` | 有限扫描 P<=5000 下两侧 prime-bad 余量均为正。 | finite evidence only |
| `GlobalPrimeDominatesBadTailInput` | `false` | `false` | 需要把平方锚素数数压过坏尾复合余因子命中的样本事实升级为全局证明。 | SquarePhaseAlphaFourFifthsPrimeDominatesBadTailCompositeCofactor |
| `BadTailFailureRoutesToPDEC` | `false` | `false` | 若 bad-tail 持久压过 prime count，必须抽取复合余因子的相位异常或端点缺陷证书。 | SquarePhaseBadTailCompositeCofactorPDECSAEReturn |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只关闭精确壳层分解，不关闭全局行/列命题。 | SquarePhaseAlphaFourFifthsPrimeDominatesBadTailCompositeCofactor OR SquarePhaseBadTailCompositeCofactorPDECSAEReturn |

## 7. 下一步

- 主攻：`SquarePhaseAlphaFourFifthsPrimeDominatesBadTailCompositeCofactor`。
- 备选回流：`SquarePhaseBadTailCompositeCofactorPDECSAEReturn`。
- 当前真正净硬点不再是好半素数壳层；它已在 `H-C` 中抵消。必须证明平方锚素数数压过坏尾复合余因子命中，或把坏尾持续优势抽成 PDEC/SAE。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/square-phase-alpha45-lowhole-shell-ledger.json` | `f089338aa00b6d6167031bbe34365ed0d135464a2ed834cae2956ddfb5c3f67a` |
| `experiments/prime_matrix_square_phase_alpha45_lowhole_shell_router.py` | `18f793793731ad9aa27216002b579aaa46b93a0717f446ce8ba357824434213e` |
