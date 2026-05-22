# Prime Matrix Phi-LPF strict k raw rejection balance 证书

**状态：** `strict_k_raw_rejection_balance_identity_closed_but_strict_excess_open`

严格 1<k<P 的内部行中，若先数所有根内素数的原始命中，再把非 LPF-owner 的命中作为已由更小素因子筛掉的拒绝量，则行内素数数目精确等于拒绝量超过原始超容量的差。零行反例因此不是普通容量饱和，而是 raw surplus 与 LPF rejection 的精确临界平衡。

## 1. Raw / rejection 平衡恒等式

```text
RawTotal=OwnerMass+RejectionMass, row_prime_count=RejectionMass-(RawTotal-(P-1))
zero row iff RejectionMass=RawTotal-(P-1), positive row iff RejectionMass>RawTotal-(P-1)
```

这里 `RawTotal` 是所有 `p<=sqrt(kP+P-1)` 且 `p | kP+a` 的原始命中总数；
`OwnerMass` 是 LPF-owner 总质量；`RejectionMass` 是那些命中里不是最小素因子的部分。

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `RawIncidenceOwnerRejectionPartition` | `true` | `true` | 根内原始命中逐项分成 LPF-owner 命中与非 owner 拒绝命中。 | raw incidence ledger |
| `PrimeCountEqualsRejectionExcess` | `true` | `true` | 行内素数数目等于 LPF 拒绝量减去原始命中相对行长的超容量。 | prime_count = rejection - raw_surplus |
| `ZeroRowIffExactRawRejectionBalance` | `true` | `true` | 零行反例等价于 rejection_total 与 raw_surplus_over_row 精确相等。 | zero row exact balance |
| `RawCapacityOnlyContradictionRejected` | `true` | `true` | 原始命中容量通常超过行长；超容量可被非 owner 拒绝吸收，不能单独推出正性。 | need strict rejection excess |
| `PositiveRejectionExcessProved` | `false` | `false` | 尚未证明每条严格行都有 rejection_total > raw_surplus_over_row。 | same full-root uncovered-slot positivity |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本层只把正缺陷改写为 raw/rejection 失衡；未排除精确平衡。 | Q1/Q2 transport, seed/PDEC scope, signed table, Rate, DStructure |

## 3. 样本审计

| P | k | interval | raw total | owner | rejection | raw surplus | prime count | rejection excess | identities |
| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 5 | 4 | [21, 24] | 4 | 3 | 1 | 0 | 1 | 1 | `true` |
| 11 | 10 | [111, 120] | 13 | 9 | 4 | 3 | 1 | 1 | `true` |
| 17 | 16 | [273, 288] | 24 | 13 | 11 | 8 | 3 | 3 | `true` |
| 101 | 50 | [5051, 5150] | 173 | 89 | 84 | 73 | 11 | 11 | `true` |
| 101 | 100 | [10101, 10200] | 183 | 88 | 95 | 83 | 12 | 12 | `true` |

## 4. 槽位样本

| P | k | slot | n | owner | raw hits | rejected hits | prime |
| ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| 5 | 4 | 1 | 21 | 3 | `[3]` | `[]` | `false` |
| 5 | 4 | 2 | 22 | 2 | `[2]` | `[]` | `false` |
| 5 | 4 | 3 | 23 | None | `[]` | `[]` | `true` |
| 5 | 4 | 4 | 24 | 2 | `[2, 3]` | `[3]` | `false` |
| 11 | 10 | 1 | 111 | 3 | `[3]` | `[]` | `false` |
| 11 | 10 | 2 | 112 | 2 | `[2, 7]` | `[7]` | `false` |
| 11 | 10 | 3 | 113 | None | `[]` | `[]` | `true` |
| 11 | 10 | 4 | 114 | 2 | `[2, 3]` | `[3]` | `false` |
| 11 | 10 | 5 | 115 | 5 | `[5]` | `[]` | `false` |
| 11 | 10 | 6 | 116 | 2 | `[2]` | `[]` | `false` |
| 11 | 10 | 7 | 117 | 3 | `[3]` | `[]` | `false` |
| 11 | 10 | 8 | 118 | 2 | `[2]` | `[]` | `false` |
| 11 | 10 | 9 | 119 | 7 | `[7]` | `[]` | `false` |
| 11 | 10 | 10 | 120 | 2 | `[2, 3, 5]` | `[3, 5]` | `false` |
| 17 | 16 | 1 | 273 | 3 | `[3, 7, 13]` | `[7, 13]` | `false` |
| 17 | 16 | 2 | 274 | 2 | `[2]` | `[]` | `false` |
| 17 | 16 | 3 | 275 | 5 | `[5, 11]` | `[11]` | `false` |
| 17 | 16 | 4 | 276 | 2 | `[2, 3]` | `[3]` | `false` |
| 17 | 16 | 5 | 277 | None | `[]` | `[]` | `true` |
| 17 | 16 | 6 | 278 | 2 | `[2]` | `[]` | `false` |
| 17 | 16 | 7 | 279 | 3 | `[3]` | `[]` | `false` |
| 17 | 16 | 8 | 280 | 2 | `[2, 5, 7]` | `[5, 7]` | `false` |
| 17 | 16 | 9 | 281 | None | `[]` | `[]` | `true` |
| 17 | 16 | 10 | 282 | 2 | `[2, 3]` | `[3]` | `false` |

## 5. 有限审计边界

```text
max_prime=97
case_count=1010
all_raw_rejection_balance_identities_verified=true
zero_rows_found_in_finite_sweep=[]
minimum_rejection_excess_over_raw_surplus=1
maximum_raw_surplus_case={'P': 97, 'k': 62, 'raw_surplus': 78}
finite_evidence_not_used_as_global_proof=true
```

最小 rejection excess 样本：

| P | k | excess |
| ---: | ---: | ---: |
| 3 | 2 | 1 |
| 5 | 4 | 1 |
| 7 | 3 | 1 |
| 11 | 10 | 1 |
| 13 | 9 | 1 |
| 17 | 12 | 1 |
| 19 | 15 | 1 |

## 6. 结论

本层把 owner 饱和硬点继续拆成两股完全显式的量：raw incidence 的超容量和 LPF rejection。
若要非循环证明 `[kP,kP+P]` 在 `1<k<P` 时有素数，必须证明 LPF rejection 严格大于 raw surplus。
精确相等就是零行反例。因此下一步最窄口是一个 signed/transport 型的严格失衡定理，
不能由 Phi-LPF 恒等式或样本容量本身推出。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_strict_k_raw_rejection_balance_router.py` | `3fe9295a5d5e330d3d6783d2aa12348da3b25a02fb8fd643b2d80e2d0de617af` |
| `docs/monograph/prime-matrix-phi-lpf-k-less-p-row-interval-difference-router.json` | `fda512a55d40c2b2e3dbac432b0bcff1c47efd7bea9e5b96e9bb291804214316` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-endpoint-bucket-cancellation-router.json` | `dbd0f06356306594afff56e4a199bdc4b27c7eb43688825b17cfd189ca8efa1c` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-internal-owner-saturation-router.json` | `d0b1755f1ba90db1c954b73254aad74aef846825e80dc38b7a128638e7550b6c` |
| `docs/monograph/prime-matrix-lowroot-sifted-deficit-frontier-router.json` | `80ae10c28cd1700bb3e5fb1280198a2332468800f9ea8e306dd8d699a22716f6` |
| `docs/monograph/prime-matrix-short-interval-rough-residue-barrier-router.json` | `29531aaae09ccded34fee1864cffa649834298d947fd7ba74637a85fd88c9b40` |
