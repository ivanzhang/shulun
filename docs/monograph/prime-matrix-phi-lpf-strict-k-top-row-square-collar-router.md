# Prime Matrix Phi-LPF strict k top row square collar 证书

**状态：** `strict_k_top_row_square_collar_hard_core_identified_positive_open`

在 strict 1<k<P 的全部行中，k=P-1 顶行把 Phi-LPF 正性压到 prime-square 上边界 collar：pi(P^2-1)-pi(P^2-P)>=1。这是全行正性的必要硬核，且它是 sqrt(kP)<P 余量最小的临界行。当前语料没有无条件证明每个素数 P 的该 collar 内必有素数；因此递推正性仍必须来自 prime-square collar 输入、sqrt-gap 输入，或 raw/rejection 严格失衡证明。

## 1. 顶行专化

```text
k=P-1
N_top(P)=pi(P^2-1)-pi(P^2-P)
N_top(P)=P-1-sum_{q<P}[Phi(floor((P^2-1)/q),q)-Phi(floor((P^2-P)/q),q)]
```

这说明任何证明 `1<k<P` 全部行正性的路线，必须先证明每个素数 `P` 的
`(P^2-P,P^2)` 内存在素数。

## 2. 临界 sqrt 余量

对 `x=kP`，行长为 `P`。函数 `P-sqrt(kP)` 随 `k` 增大而减小，
所以顶行 `k=P-1` 是平方根尺度余量最小的 strict 行：

```text
P-sqrt(P(P-1)) = P/(P+sqrt(P(P-1))) in (1/2,1).
```

## 3. 样本审计

| P | interval | top row prime count | P-sqrt(P(P-1)) | positive |
| ---: | --- | ---: | ---: | --- |
| 5 | [21, 24] | 1 | 0.527864 | `true` |
| 11 | [111, 120] | 1 | 0.511912 | `true` |
| 17 | [273, 288] | 3 | 0.507577 | `true` |
| 101 | [10101, 10200] | 12 | 0.501244 | `true` |
| 499 | [248503, 249000] | 44 | 0.500251 | `true` |
| 5003 | [25025007, 25030008] | 281 | 0.500025 | `true` |

## 4. 有限审计边界

```text
max_prime=5003
case_count=669
all_top_rows_positive_in_finite_sweep=true
zero_top_rows_found=[]
minimum_top_row_prime_count=1
finite_evidence_not_used_as_global_proof=true
```

最小顶行素数数样本：

| P | top row prime count |
| ---: | ---: |
| 3 | 1 |
| 5 | 1 |
| 11 | 1 |

尾部样本：

| P | top row prime count | P-sqrt(P(P-1)) |
| ---: | ---: | ---: |
| 4943 | 296 | 0.500025 |
| 4951 | 293 | 0.500025 |
| 4957 | 285 | 0.500025 |
| 4967 | 311 | 0.500025 |
| 4969 | 307 | 0.500025 |
| 4973 | 298 | 0.500025 |
| 4987 | 297 | 0.500025 |
| 4993 | 292 | 0.500025 |
| 4999 | 289 | 0.500025 |
| 5003 | 281 | 0.500025 |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `TopRowSpecializationClosed` | `true` | `true` | strict k=P-1 行专化为 prime-square 上边界 collar (P^2-P,P^2)。 | exact specialization |
| `PhiLPFTopRowExactFormulaClosed` | `true` | `true` | 顶行 Phi-LPF 公式为 pi(P^2-1)-pi(P^2-P) 的精确端点差分。 | exact count only |
| `TopRowNecessaryHardCoreIdentified` | `true` | `true` | 全 strict 行正性必须先证明顶行 square-collar 正性。 | PrimeSquareUpperCollarPrimeInput |
| `TopRowMinimalSqrtSlackClosed` | `true` | `true` | 在 1<k<P 中，k=P-1 使 P-sqrt(kP) 最小，且该余量位于 (1/2,1)。 | critical sqrt margin |
| `TopRowPositiveProvedInCurrentCorpus` | `false` | `false` | 当前语料没有无条件证明每个素数 P 的 (P^2-P,P^2) 内都有素数。 | prime-square upper-collar theorem or rejection-excess proof |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本层只提取必要硬核，不证明全部 strict 行正性。 | all rows still need sqrt-gap or PositiveRejectionExcess |

## 6. 结论

顶行 square-collar 是 strict 行正性的必要硬核，不是完整充分条件。
它把最窄正性口压成 `PrimeSquareUpperCollarPrimeInput`：
`pi(P^2-1)-pi(P^2-P)>=1` 对所有素数 `P` 成立。
当前尚未无条件闭合，因此不能声称 Phi-LPF 递推已经推出正性。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_strict_k_top_row_square_collar_router.py` | `26dd304ba5c7c8da2b4b6c174e22105a013475ba4c87287534456bd82730b2b1` |
| `docs/monograph/prime-matrix-phi-lpf-k-less-p-row-interval-difference-router.json` | `fda512a55d40c2b2e3dbac432b0bcff1c47efd7bea9e5b96e9bb291804214316` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-raw-rejection-balance-router.json` | `59bf235653fb8aef057ba81b7e3e42132d7b8bf1b15283671e52330a9cb6ad0d` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-short-interval-exponent-barrier-router.json` | `9c8b4ae328fe2254bf81e16e4f058921efc6c3ea616a97f196a42482151dd028` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-sqrt-gap-equivalence-router.json` | `f825d0e5df9740a53392e3dc0821ca50208291280e33fe9e9ab04e878a70ab3b` |
