# Prime Matrix Phi-LPF strict k endpoint bucket cancellation 证书

**状态：** `strict_k_endpoint_bucket_cancellation_closed_but_internal_row_positivity_open`

严格 1<k<P 时，闭区间 [kP,kP+P] 比内部行只多两个合数端点。Phi-LPF 桶差分逐桶显示，这两个端点分别支付给 LPF(k) 与 LPF(k+1) owner 桶；闭区间多出的长度 2 被合数桶增量精确抵消。因此端点差分没有隐藏正性余量，剩余仍是内部行 LPF 合数桶增量和小于 P-1。

## 1. 桶抵消恒等式

```text
pi(kP+P)-pi(kP-1)=pi(kP+P-1)-pi(kP)
Delta_closed_p-Delta_internal_p = 1_{p=LPF(k)} + 1_{p=LPF(k+1)} for [kP,kP+P], 1<k<P
```

这里 `Delta_closed_p` 是 `[kP,kP+P]` 的第 `p` 个 LPF 桶端点增量，
`Delta_internal_p` 是 `[kP+1,kP+P-1]` 的第 `p` 个 LPF 桶端点增量。

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `StrictKEndpointCompositeMassTwo` | `true` | `true` | 当 1<k<P 时，闭区间 [kP,kP+P] 比内部行多出的两个端点都是合数。 | endpoint composite mass is exactly two |
| `EndpointLPFOwnerBucketsPinned` | `true` | `true` | 左端点归入 LPF(k) 桶，右端点归入 LPF(k+1) 桶；若 k+1=P，则右端点归入 P 桶。 | owner multiset {LPF(k), LPF(k+1)} |
| `ClosedMinusInternalBucketDeltaEqualsEndpointOwners` | `true` | `true` | 闭区间 LPF 桶端点增量减去内部行增量，逐桶等于两个端点 owner 的计数。 | bucket-level cancellation identity |
| `NoEndpointSlackForRowPositivity` | `true` | `true` | 闭区间多出的长度 2 被两个端点合数桶精确吃掉，不能产生额外素数正性余量。 | strict-k endpoint shortcut removed |
| `InternalRowCompositeDeltaInequalityStillNeeded` | `false` | `false` | 要证明行内有素数，仍需内部行合数桶增量和小于 P-1。 | same full-root uncovered-slot positivity |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本层排除了端点余量捷径，但未证明内部行正性。 | Q1/Q2 transport, seed/PDEC scope, signed table, Rate, DStructure |

## 3. 样本审计

| P | k | closed | internal | closed primes | internal primes | delta total | bucket diff | endpoint owners | ok |
| ---: | ---: | --- | --- | ---: | ---: | ---: | --- | --- | --- |
| 5 | 4 | [20, 25] | [21, 24] | 1 | 1 | 2 | `{2: 1, 5: 1}` | `{2: 1, 5: 1}` | `true` |
| 11 | 10 | [110, 121] | [111, 120] | 1 | 1 | 2 | `{2: 1, 11: 1}` | `{2: 1, 11: 1}` | `true` |
| 17 | 16 | [272, 289] | [273, 288] | 3 | 3 | 2 | `{2: 1, 17: 1}` | `{2: 1, 17: 1}` | `true` |
| 101 | 50 | [5050, 5151] | [5051, 5150] | 11 | 11 | 2 | `{2: 1, 3: 1}` | `{2: 1, 3: 1}` | `true` |
| 101 | 100 | [10100, 10201] | [10101, 10200] | 12 | 12 | 2 | `{2: 1, 101: 1}` | `{2: 1, 101: 1}` | `true` |

## 4. 有限审计边界

```text
max_prime=97
case_count=1010
all_endpoint_bucket_cancellations_verified=true
same_owner_endpoint_cases=0
distinct_owner_endpoint_cases=1010
finite_evidence_not_used_as_global_proof=true
```

## 5. 结论

闭区间端点没有给出新的正性来源：多出的两个位置被两个端点合数的 LPF owner 桶精确抵消。
因此 `[kP,kP+P]` 的 Phi-LPF 端点差分路线已经完全回到内部行不等式
`sum Delta_internal_p < P-1`。该不等式仍等价于 full-root 未覆盖槽存在，不能作为内部黑箱。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_strict_k_endpoint_bucket_cancellation_router.py` | `6d118e89e60ef03f42bd05f73df6e117d45e38c328297fd6630a39d8140bc7d3` |
| `docs/monograph/prime-matrix-phi-lpf-k-less-p-row-interval-difference-router.json` | `fda512a55d40c2b2e3dbac432b0bcff1c47efd7bea9e5b96e9bb291804214316` |
| `docs/monograph/prime-matrix-phi-lpf-endpoint-interval-difference-router.json` | `e0b7301c85ca5828aca8fc99ab225cbccc166f860ad2a62dfcbf7bfcda350e65` |
| `docs/monograph/prime-matrix-short-interval-rough-residue-barrier-router.json` | `29531aaae09ccded34fee1864cffa649834298d947fd7ba74637a85fd88c9b40` |
