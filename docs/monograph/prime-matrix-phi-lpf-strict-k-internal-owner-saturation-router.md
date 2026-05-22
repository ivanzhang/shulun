# Prime Matrix Phi-LPF strict k internal owner saturation 证书

**状态：** `strict_k_internal_owner_saturation_identity_closed_but_positive_defect_open`

严格 1<k<P 的内部行中，Phi-LPF 桶端点增量不是近似量，而是直接 LPF-owner 分桶计数。行内素数数目等于 P-1 减去所有 owner 桶质量。因此零行反例被精确改写为 owner 桶全饱和；剩余硬点是证明饱和缺陷始终为正。

## 1. Owner 饱和恒等式

```text
row_prime_count=(P-1)-sum_p Delta_internal_p=P-1-sum_p OwnerMass_p
zero row iff sum_p OwnerMass_p=P-1 iff LPF-owner buckets saturate every internal slot
```

若内部槽 `a` 由 owner `p` 负责，则：

```text
a == -kP mod p,  (kP+a)/p is p-rough
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `InternalPhiBucketEqualsLPFOwnerPartition` | `true` | `true` | 内部行的 Phi 桶端点增量逐桶等于直接 LPF-owner 分桶计数。 | exact owner ledger |
| `OwnerResidueEquationPinned` | `true` | `true` | 若槽 a 归入 owner p，则 a == -kP mod p 且 (kP+a)/p 为 p-rough。 | CRT residue plus rough cofactor |
| `SaturationDefectEqualsPrimeCount` | `true` | `true` | P-1 减去 owner 桶总质量，正是内部行素数数目。 | defect = row prime count |
| `ZeroRowIffOwnerSaturation` | `true` | `true` | 零行反例等价于 LPF-owner 桶完全饱和 P-1 个内部槽。 | zero row means no saturation defect |
| `CapacityOnlyContradictionRejected` | `true` | `true` | owner 桶容量或样本正缺口不排除全饱和；仍需证明饱和缺陷为正。 | need non-circular lower bound |
| `PositiveSaturationDefectProved` | `false` | `false` | 尚未证明每个 1<k<P 内部行的饱和缺陷为正。 | full-root uncovered-slot positivity |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本层只把零行反例改写成 owner 饱和条件；未排除该条件。 | Q1/Q2 transport, seed/PDEC scope, signed table, Rate, DStructure |

## 3. 样本审计

| P | k | interval | owner mass | prime count | saturation defect | phi=owner | defect=prime |
| ---: | ---: | --- | ---: | ---: | ---: | --- | --- |
| 5 | 4 | [21, 24] | 3 | 1 | 1 | `true` | `true` |
| 11 | 10 | [111, 120] | 9 | 1 | 1 | `true` | `true` |
| 17 | 16 | [273, 288] | 13 | 3 | 3 | `true` | `true` |
| 101 | 50 | [5051, 5150] | 89 | 11 | 11 | `true` | `true` |
| 101 | 100 | [10101, 10200] | 88 | 12 | 12 | `true` | `true` |

## 4. Owner residue 样本

| P | k | owner | residue a mod owner | slots sample | ok |
| ---: | ---: | ---: | ---: | --- | --- |
| 5 | 4 | 2 | 0 | `[2, 4]` | `true` |
| 5 | 4 | 3 | 1 | `[1]` | `true` |
| 11 | 10 | 2 | 0 | `[2, 4, 6, 8, 10]` | `true` |
| 11 | 10 | 3 | 1 | `[1, 7]` | `true` |
| 11 | 10 | 5 | 0 | `[5]` | `true` |
| 11 | 10 | 7 | 2 | `[9]` | `true` |
| 17 | 16 | 2 | 0 | `[2, 4, 6, 8, 10, 12, 14, 16]` | `true` |
| 17 | 16 | 3 | 1 | `[1, 7, 13]` | `true` |
| 17 | 16 | 5 | 3 | `[3]` | `true` |
| 17 | 16 | 7 | 1 | `[15]` | `true` |

## 5. 有限审计边界

```text
max_prime=97
case_count=1010
all_owner_saturation_identities_verified=true
zero_rows_found_in_finite_sweep=[]
minimum_saturation_defect=1
finite_evidence_not_used_as_global_proof=true
```

最小饱和缺陷样本：

| P | k | saturation defect |
| ---: | ---: | ---: |
| 3 | 2 | 1 |
| 5 | 4 | 1 |
| 7 | 3 | 1 |
| 11 | 10 | 1 |
| 13 | 9 | 1 |
| 17 | 12 | 1 |
| 19 | 15 | 1 |

## 6. 结论

Phi-LPF 已经把内部行完全变成 owner 桶账本。要证明 `[kP,kP+P]` 在 `1<k<P` 时有素数，
等价于证明 owner 桶不能把 `P-1` 个内部槽全饱和。这个正缺陷仍是 row-prime 内容本身；
下一步必须从 Q1/Q2 传输、seed/PDEC 作用域、signed table 或外部短区间输入中获得非循环信息。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_strict_k_internal_owner_saturation_router.py` | `8c79653d03fd532b00476827488f4116c6299816531551efa8991bb9cf1a89db` |
| `docs/monograph/prime-matrix-phi-lpf-k-less-p-row-interval-difference-router.json` | `fda512a55d40c2b2e3dbac432b0bcff1c47efd7bea9e5b96e9bb291804214316` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-endpoint-bucket-cancellation-router.json` | `dbd0f06356306594afff56e4a199bdc4b27c7eb43688825b17cfd189ca8efa1c` |
| `docs/monograph/prime-matrix-lowroot-sifted-deficit-frontier-router.json` | `80ae10c28cd1700bb3e5fb1280198a2332468800f9ea8e306dd8d699a22716f6` |
| `docs/monograph/prime-matrix-short-interval-rough-residue-barrier-router.json` | `29531aaae09ccded34fee1864cffa649834298d947fd7ba74637a85fd88c9b40` |
