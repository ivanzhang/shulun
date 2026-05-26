# Prime Matrix Phi-LPF row Delta-Phi cover contract 路由

**状态：** `row_delta_phi_exact_identity_closed_but_positive_cover_gap_open`
**核验日期：** `2026-05-26`

行内短区间计数确实等于两个前缀 LPF/Phi 计数之差；这给出完全精确的 Delta-Phi 覆盖恒等式。该恒等式把正性目标化为严格覆盖缺口：LPF 合数桶在目标行内的总覆盖必须小于行长。然而严格缺口本身等价于该行有素数，不能由恒等式自动推出。下一步必须证明统一 Delta-Phi cover defect，或把覆盖等号转化为命名 LPF-owner residue PDEC，或引入点态 theta/psi、signed divisor、trace/Type-II 输入。

```text
row_delta_phi_identity_closed=true
row_delta_phi_prefix_difference_is_exact=true
row_delta_phi_positive_lower_bound_proved=false
strict_cover_inequality_proved_uniformly=false
row_column_unconditional_closed=false
```

## 1. 精确恒等式

```text
C_p(N)=0 if N<p^2, else Phi(floor(N/p); primes<p)-1
pi(A,B]=B-A-sum_{p<=sqrt(B)}(C_p(B)-C_p(A))
sum_{p<=sqrt(B)}(C_p(B)-C_p(A)) <= B-A-1
```

target_cover_inequality is equivalent to pi(A,B]>0, so it cannot be used as an independent proof without a new saving/PDEC/trace input

## 2. 样本行核验

| interval | length | Delta-Phi cover | primes | residual | identity | prime-free |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| `(90,96]` | 6 | 6 | 0 | 0 | `true` | `true` |
| `(100,110]` | 10 | 6 | 4 | 4 | `true` | `false` |
| `(110,120]` | 10 | 9 | 1 | 1 | `true` | `false` |
| `(900,930]` | 30 | 26 | 4 | 4 | `true` | `false` |
| `(990,1020]` | 30 | 25 | 5 | 5 | `true` | `false` |

prime-free 样本说明：前缀差公式会精确给出零素数行，而不是自动排除零行。

```text
interval=(90,96]
length=6
delta_phi_composite_cover=6
prime_count=0
```

## 3. Prime Matrix 小 P punctured row 样本

| P | k range | min primes | max primes | zero rows |
| ---: | --- | ---: | ---: | ---: |
| 5 | `1..4` | 1 | 2 | 0 |
| 7 | `1..6` | 1 | 2 | 0 |
| 11 | `1..10` | 1 | 4 | 0 |
| 13 | `1..12` | 1 | 3 | 0 |
| 17 | `1..16` | 1 | 4 | 0 |
| 19 | `1..18` | 1 | 6 | 0 |
| 31 | `1..30` | 2 | 7 | 0 |

## 4. 真正需要攻克的公式

| route | needed formula | current blocker |
| --- | --- | --- |
| Direct Delta-Phi strict cover inequality | `sum_{p<=sqrt(B)}(C_p(B)-C_p(A)) <= B-A-1 for every target row (A,B]` | this is exactly equivalent to pi(B)-pi(A)>0; no independent saving has been proved |
| Pointwise theta at sqrt row scale | `theta(B)-theta(A)>0 for every target row` | known short-interval inputs still do not give a zero-exception x^(1/2) theorem at this row scale |
| Psi beyond prime-power tail | `psi(B)-psi(A)>prime_power_tail(A,B)` | prime-power tail is bounded, but the required pointwise psi lower bound is still open |
| Signed Mobius/Von Mangoldt Type-I/II | `source-key-consistent signed divisor decomposition with error < one row survivor` | LPF/Phi support ledgers have not produced admissible signed coefficients |
| Trace/Kloosterman/spectral | `completed source-keyed trace family with conductor and coefficient control` | current q-spine/hinge ledgers are finite actual-load ledgers, not uniform trace families |
| Cover-equality PDEC/SAE return | `if Delta-Phi cover equals row length, the induced LPF owner residues create a named contradiction` | the covering equality has not yet been converted into a forbidden structured packet |

## 5. 下一手

```text
next_primary_attack_target=UniformDeltaPhiCoverDefectOrNamedLPFOwnerResiduePDEC
paired_signed_attack_target=PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR SourceKeyedMobiusVonMangoldtTraceTypeIIFamily
paired_distribution_attack_target=PointwiseThetaPsiCOneInputAtSqrtRowScale
```

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/claim-status-table.md` | `ac2bb849e975ac7bfc402ef51d24e50e0246b64c369dd10374274fbf42bdc580` |
| `docs/monograph/external-theorem-index.md` | `e1c6b7800fa5c4784b18b98e77eac8202eb6b482d3fec21603bbed667a2980cd` |
| `docs/monograph/frontier-honest-status-and-true-side-theorems-20260522.md` | `27f86b323f7ab1aeeb90bda019543d00615ff68e868c83fb50b6822b47ca0cf5` |
| `docs/monograph/prime-matrix-phi-lpf-lpf-bucket-count-formula-audit.json` | `1e38c9ee2e7fd682eb787765eb9b5a7b9cf0b15992f1d013f75996bc01fe2bcf` |
| `docs/monograph/prime-matrix-phi-lpf-parity-barrier-prime-distribution-contract-router.json` | `74636f1bc6c8e7088a213b0df5440bf93aadb10482989dca7615eb4edaaf3f06` |
| `docs/monograph/prime-matrix-phi-lpf-parity-barrier-transport-edge-sync-router.json` | `de0f3fdf91e7b571cdf60a07c2457cf1ec36255ae1367a59b2f725b028ed4f5e` |
| `docs/monograph/prime-matrix-phi-lpf-punctured-endpoint-wheel30-capacity-router.json` | `2ec71522b5e0e82fb2f420c5322dd66ad72814be1174acff8f373ac4b00b0393` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `3fb1aec2c06a019bf2e1a2415a6fa07375bb96871dced794fff880e5c4bd41a6` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `ee624a21d9a16be959d42a250f1f8ac99cc0e7d569e7c94799c668d11344b724` |
| `docs/monograph/three-claims-formal-to-actual-critical-load-frontier.md` | `8f40cf7e58e2d51c4faad74d6c9ad8c7c08ab37d0eccc930744af28aade04a76` |
| `experiments/prime_matrix_phi_lpf_row_delta_phi_cover_contract_router.py` | `182a0e66fe13d7228ab55ed1e97c0b00919590153e5c3564c1e99ed1d8b8fe40` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `9384b9f9b45ea5a231033a360b11337ebe0f7dfcf2ab5a158eeda4b6cd49426d` |
