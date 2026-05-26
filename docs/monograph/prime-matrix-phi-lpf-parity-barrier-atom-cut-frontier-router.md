# Prime Matrix Phi-LPF parity barrier atom-cut frontier 路由

**状态：** `phi_lpf_parity_barrier_synced_to_atom_cut_frontier_open`
**核验日期：** `2026-05-26`

LPF/Phi 的精确计数错误已经修正，但这只关闭了无符号粗数账本。奇偶性障碍的本质仍是缺少能区分素数与 P2/P3 粗合数的有符号信息。当前非循环路线已经从 rough cofactor transport 继续压到两个最细 signed atom：offdiagonal pure-pair seed atom 与 constructor edge-local signed fields。若不改走点态 theta/psi 平方根行分布定理或外部 admissible trace/Type-II family，下一步必须正面提交这些 atom 的 signed formula、orientation、ExactUV return 和 internal transition。

```text
atom_cut_frontier_synced=true
corrected_lpf_formula=C_p(N)=Phi(floor(N/p); primes< p)-1
legendre_periodic_boundary_not_half_main=true
unsigned_lpf_bucket_count_sufficient_for_prime_extraction=false
more_wheel_or_lpf_refinement_rejected_as_first_break=true
row_column_unconditional_closed=false
```

## 1. LPF 精确计数修正

| object | exact formula | why |
| --- | --- | --- |
| all values with least prime factor p, prime p included | `A_p(N)=Phi(floor(N/p); primes<p)` | write m=p*a; the cofactor a may be divisible by p, but may not contain primes below p |
| composites with least prime factor p | `C_p(N)=Phi(floor(N/p); primes<p)-1` | subtract the unit cofactor a=1, i.e. the prime value p itself |
| Legendre-Phi expansion | `Phi(y; primes<p)=sum_{d divides Q_<p} mu(d)*floor(y/d)` | the finite Euler product appears only after replacing floors by y/d |
| periodic boundary | `Phi(y; primes<p)=y*prod_{ell<p}(1-1/ell)+E_p(y)` | E_p is a primorial-periodic floor boundary, not a universal half-main error term |
| rejected heuristic | `(N-p^2)*prod_{ell<=p}(1-1/ell)` | wrong scale, wrong endpoint, and wrongly removes cofactor multiples of p |

## 2. 真正需要的精确分布合同

| contract | formula | breaks parity | current state | blocker |
| --- | --- | --- | --- | --- |
| Pointwise theta at sqrt row scale | `theta((kP,(k+1)P))>0 for every 1<=k<P` | `true` | not proved | requires pointwise prime existence in every length-P row near P^2 |
| Psi beyond prime-power tail | `psi(I_{P,k})>PrimePowerTail(I_{P,k})` | `true` | tail identity closed; lower bound not proved | pure prime-power tail is bounded, but no rowwise positive psi main term is available |
| Signed divisor / Type-I-II family | `source-key consistent Lambda/Mobius decomposition with factorable coefficients` | `true` | not constructed | LPF ownership is still an unsigned support ledger before signed atom emission |
| Trace/Kloosterman/Kuznetsov family | `completed source-keyed trace family with conductor and coefficient control` | `true` | not admissible yet | formal finite trace ledgers lack a uniform source-keyed signed family |
| Named PDEC/SAE return | `failure of a uniform signed law returns to a controlled contradiction packet` | `true` | interfaces named, global return not closed | current atom failures are not yet converted to a theorem-level contradiction |

## 3. 当前 atom-cut 前沿

| frontier | closed unsigned | open signed atom | paired gates | active |
| --- | --- | --- | --- | --- |
| seed-side pure-pair atom | unique tail=1 atom pq and Phi(floor(N/(pq)),q)-1 tail lift | `PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward` | PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows | `true` |
| constructor edge-local field table | owner p, first q, product pq, Ferrers rank/degree and multiplicity-one edge label | `PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward` | PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows | `true` |
| internal tail continuation | tail continuation mass is assigned to the same first seed, not a new first seed | `PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward` | step multiplier compatibility along the ordered LPF word | `true` |
| single-table bypass | Phi-LPF support keys are fixed | `PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward` | complete prepushforward signed value table on all support keys | `true` |

## 4. 可绕行路线

| route | minimal object | open atom | breaks parity | chosen next |
| --- | --- | --- | --- | --- |
| Pointwise theta / gap route | theta((kP,(k+1)P))>0, equivalently h(kP)<P for all strict rows | unconditional pointwise C<=1 sqrt-scale theorem or row-specific substitute | `true` | `false` |
| Pointwise psi beyond prime-power tail | psi(I_{P,k})>PrimePowerTail(I_{P,k}) rowwise | pointwise psi lower bound at exact row scale | `true` | `false` |
| Internal LPF signed cofactor transport | a_p(q*m) transport law with orientation/local-factor/branch updates before pushforward | PhiLPFRoughCofactorMultiplicationSignedTransportLawBeforePushforward | `true` | `true` |
| Trace / Kloosterman / Type-II route | completed source-keyed signed trace family with factorable coefficients and conductor control | source-key lift plus Type-II factorability and conductor range | `true` | `false` |
| Shared-pivot PDEC/SAE return | uniform hinge/payment law failure returns to controlled contradiction | BridgeRootSharedPivotHingeLawOrPDEC plus terminal sibling q-spine payment | `true` | `false` |
| More LPF/Phi/wheel refinement | none; this class only refines unsigned support | not a parity-breaking atom | `false` | `false` |

## 5. 下一手

```text
next_seed_side_attack_target=PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward
next_constructor_side_attack_target=PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward
parallel_direct_bypass=PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
paired_required_attack_targets=PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
```

最新开放口：

```text
(ParityBarrierContractPinned AND MinimalRouteForcingClosed AND PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward AND PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn OR NamedPDECOrSAEReturn
```

行/列命题仍未无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/external-theorem-index.md` | `17d6ac92870af9ae535ab1e6f5018524e6c3ad57794caa9c8623fa0fe28516a0` |
| `docs/monograph/frontier-honest-status-and-true-side-theorems-20260522.md` | `124f6135e955e59a2bdc0298640e3e2f3c42a8982930c0ca0da0b0d4f438a777` |
| `docs/monograph/prime-matrix-phi-lpf-exact-bucket-endpoint-equivalence-audit.json` | `92468974eceab624e5a553bb3a24e20a85b9e3f5424b674bb9f00057a53ccfc5` |
| `docs/monograph/prime-matrix-phi-lpf-latest-constructor-edge-local-field-cut-sync-router.json` | `fe09054d1b948cf0af0f89a13a25b0b4985dd0373d7d1395bf7205669048353c` |
| `docs/monograph/prime-matrix-phi-lpf-latest-offdiagonal-pure-pair-atom-sync-router.json` | `2ef53f76c04a047c30b1afad82054c641e751ec5b4e6dfeedecb3c318a2486e9` |
| `docs/monograph/prime-matrix-phi-lpf-lpf-bucket-count-formula-audit.json` | `1e38c9ee2e7fd682eb787765eb9b5a7b9cf0b15992f1d013f75996bc01fe2bcf` |
| `docs/monograph/prime-matrix-phi-lpf-minimal-parity-breaker-route-forcing-router.json` | `127e2a68aa49568ecc36f2ea3c2b048a396d1e3cd58ccb3bdb7dd7df9b49b8b9` |
| `docs/monograph/prime-matrix-phi-lpf-parity-barrier-prime-distribution-contract-router.json` | `74636f1bc6c8e7088a213b0df5440bf93aadb10482989dca7615eb4edaaf3f06` |
| `docs/monograph/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json` | `c78bc14420695f82fbb46cc5c3de28dbf38c85ba678d9aa4ffe0fb0f1c98d868` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `88aa4471450e765790dfd67c052f5d1879c138f7af542cce9c15da939aa523f9` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `2405f742aaa400e81cd195f76467f6cc76bf1a14f15dee035a73c156e9e06c36` |
| `docs/monograph/three-claims-formal-to-actual-critical-load-frontier.md` | `b9ed1d8e63b4d0c808d5b79ad2706a70dc150e0ae3a99160ab88a6e00ad32a2b` |
| `experiments/prime_matrix_phi_lpf_parity_barrier_atom_cut_frontier_router.py` | `6d43258feb9ec1b10453590744b1c0585802aaa0f4a208a0621ede391017756d` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `97535bdc0032695ecc3f1acc3bf7d859b3833f37e46e3e5b83bf1763b688f8ee` |
