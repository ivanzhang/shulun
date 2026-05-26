# Prime Matrix Phi-LPF corrected-LPF signed-trace breakthrough 路由

**状态：** `corrected_lpf_routes_to_signed_trace_not_unsigned_closure`
**核验日期：** `2026-05-26`

## 1. 总裁定

```text
lpf_exact_count_fixed=true
lpf_exact_count_formula=C_p(N)=Phi(floor(N/p);q<p)-1=Phi(floor(N/p);q<p)-Phi(p-1;q<p)
phi_endpoint_singleton=Phi(p-1;q<p)=1
finite_euler_truncation_error_type=primorial periodic boundary term, not half-main saving
von_mangoldt_lift_requires_global_signed_payload=true
top_row_oppermann_necessary_not_sufficient=true
all_external_inputs_require_internal_admissible_family=true
row_column_unconditional_closed=false
phi_lpf_parity_barrier_globally_broken=false
```

## 2. 路线裁定表

| route | priority | closed assets | remaining blocker | next required object | direct close |
| --- | --- | --- | --- | --- | --- |
| corrected LPF/Phi exact count | supporting | C_p(N)=Phi(floor(N/p);q<p)-1<br>C_p(N)=Phi(floor(N/p);q<p)-Phi(p-1;q<p)<br>Phi(p-1;q<p)=1<br>periodic primorial boundary error identified | unsigned counts do not distinguish prime emission from composite tails | global Mobius/von-Mangoldt signed divisor payload | false |
| ordinary short intervals and Oppermann top row | boundary | theta>1/2 closes only zero-density low rows<br>sqrt C<=1 is the sharp row containment threshold<br>top row equals prime-indexed Oppermann-left<br>top row is necessary but not sufficient for all rows | need h(kP)<P for every 1<=k<P, not just k=P-1 | pointwise sqrt-scale row psi input or internal signed substitute | false |
| terminal signed monotone-run payload | fastest | finite terminal run ledger closed<br>atom adjacent-cancellation decomposition closed<br>selected negative excess beats finite extra atom survivor | uniform adjacent-run cancellation family or named PDEC/SAE return | admissible signed trace/Type-II family or LocalSurvivor/PDEC theorem | false |
| two-point sieve / quadratic secondary sieve | second | DI/BFI/KLS direction identified<br>same-convention numerator/denominator contract stated | denominator floor and numerator load must be proved in the same singular-series convention | BMD=>TLI without hidden denominator/parity gap | false |
| RH contradiction-field controlled exits | verification | controlled exits and D-structure/Rankin boundaries recorded | independent referee acceptance of all controlled exits | verification package, not first-break route | false |

## 3. 外部前沿适配

| input | input signature | usable after | current blocker | direct close | url |
| --- | --- | --- | --- | --- | --- |
| Runbo Li short intervals | ordinary prime in [x-x^theta,x], theta=13/25 | strict row containment with k+1<P^(12/13) | zero-density low rows only; top band still needs sqrt-scale pointwise input | false | https://arxiv.org/abs/2308.04458 |
| Runbo Li large-modulus AP / Harman sieve | average large-modulus/AP distribution input | project weights are promoted to an admissible averaged AP family | row-column target is pointwise at P^2, not merely averaged | false | https://arxiv.org/abs/2602.20917 |
| Milicevic-Qin-Wu Kloosterman bilinear sums | bilinear Kloosterman-type family | moving Beatty numerator becomes a genuine two-variable Kloosterman family | no admissible two-variable trace family has been constructed from LPF buckets | false | https://arxiv.org/abs/2511.07550 |
| Pascadi composite-modulus Type-II | composite-modulus Type-II sums with admissible coefficients | terminal/LPF weights are converted into well-factorable signed coefficients | unsigned LPF ownership counts are not Type-II coefficients | false | https://arxiv.org/abs/2511.08445 |
| Wright trilinear Kloosterman fractions | trilinear Kloosterman-fraction convolution | terminal payload is upgraded to a trilinear convolution with equidistributed beta sequence | current payload is finite and one-dimensional, not a trilinear family | false | https://arxiv.org/abs/2604.25177 |
| spectral gap / finite-group expansion inputs | finite-group orbit expansion or anti-concentration | a genuine group orbit model is constructed from phase residues | no orbit expansion family has been proved for the row-column payload | false | https://arxiv.org/abs/2512.15364 |

## 4. 最快非循环突破口

```text
fastest_first_break_candidate=Prime Matrix terminal signed monotone-run payload
fastest_first_break_gate=UniformAdjacentRunCancellationFamilyOrPDEC AND AtomLocalSurvivorPaymentOrPDEC AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

## 5. 最新开放口

```text
CorrectedLPFExactCountsAndPeriodicErrorsDoNotGivePrimeEmission AND PureShortIntervalOrTopRowInputsDoNotCloseAllRows AND FastestPrimeMatrixRouteRequiresSignedTraceOrTypeIIFamily AND UniformAdjacentRunCancellationOrNamedPDECSAEStillOpen
```

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_corrected_lpf_signed_trace_breakthrough_router.py` | `86b934fc986bd1f7d0bdc177e95a9d8ec601e05aa3b29c2d036f2b0ea45795b7` |
| `docs/monograph/prime-matrix-phi-lpf-exact-bucket-endpoint-equivalence-audit.json` | `92468974eceab624e5a553bb3a24e20a85b9e3f5424b674bb9f00057a53ccfc5` |
| `docs/monograph/prime-matrix-phi-lpf-legendre-phi-periodic-truncation-error-audit.json` | `975aa118af686bd729414f291af1efd9fa60082d622ac687d7f87772246acd6e` |
| `docs/monograph/prime-matrix-phi-lpf-affine-lpf-first-hit-von-mangoldt-lift-router.json` | `f745ed6c597dfcceed10f50249df139235cac727fd8086737b81bb894bda3a4c` |
| `docs/monograph/prime-matrix-phi-lpf-prime-power-tail-sublinear-threshold-audit.json` | `22fec026bad79e0d8ec10bff215385c10fdee931213702bd67e4cebea47ec238` |
| `docs/monograph/prime-matrix-phi-lpf-theta-short-interval-zero-density-band-router.json` | `33ae5e4a006144f31f60066292586d3fe6da1ff13fe69a3d8dd2011920000978` |
| `docs/monograph/prime-matrix-phi-lpf-sqrt-constant-threshold-router.json` | `26d483db1f25930b40cd2389a16de1e30f01973723adcf5afb54d8b18d2f9191` |
| `docs/monograph/prime-matrix-phi-lpf-oppermann-subcore-not-full-closure-router.json` | `6c66e0256c2481244ed42dd3d960241af0cf524643e0dde78aea51e62e0d6223` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-monotone-run-total-to-net-compression-frontier-router.json` | `ec3616097527b1bf9d426727572ea66b66e15f92ca243d44221f5973437d8613` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `db37ce154c8f070146b930cab23d170e6cd662630477f04294aac1391d272411` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `f6e2ce843b8f44e7b9953a90177c4867d5b2a98cb8b9e7241c1541bbf92197ee` |
| `docs/monograph/external-theorem-index.md` | `40ab8428df5d2610936cfab80eccf11406bcf9e5898260357e4b7e519d0ecf92` |
