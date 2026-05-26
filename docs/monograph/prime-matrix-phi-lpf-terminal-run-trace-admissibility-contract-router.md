# Prime Matrix Phi-LPF terminal-run trace-admissibility contract 路由

**状态：** `terminal_run_trace_admissibility_contract_pinned_family_open`
**核验日期：** `2026-05-26`

## 1. 总裁定

```text
terminal_finite_signed_run_ledger_closed=true
finite_adjacent_cancellation_decomposition_closed=true
finite_absorption_would_close_after_uniform_cancellation_law=true
selected_negative_excess_beats_extra_atom_survivor=true
trace_or_typeii_family_admissible_now=false
external_theorems_directly_attach_now=false
all_trace_contracts_proved=false
row_column_unconditional_closed=false
```

## 2. terminal run 摘要

```text
terminal_run_count_total=59
selected_terminal_run_count=35
extra_shell_run_count=24
atom_count=7
strict_run_local_compression_count=0
selected_negative_excess=1.456565972578 (114539441491/78636631397)
extra_total_variation=14.109301881162 (27768758142307772418840319934041830802744822617132968593977647725/1968117088725958506051611620121066252424277248250429833368124847)
extra_atom_local_survivor_total=0.907719323182 (71379989829/78636631397)
selected_negative_excess_minus_extra_atom_survivor=0.548846649396 (43159451662/78636631397)
```

## 3. trace/Type-II 可接入合同

| contract | needed statement | current evidence | proved | failure return |
| --- | --- | --- | --- | --- |
| TerminalRunKernelFormula | give a forward formula K_P(q,m,atom) whose signed value equals the terminal run payload | finite signed_delta and q-interval rows exist | false | MissingTraceKernelFormulaPDEC |
| SameTraceKeySourceConsistency | source row, orientation, local factor, ExactUV pair and signed value share one pre-Cauchy trace key | same-key requirement is named in previous trace-sync routers | false | SameTraceKeySplitPDEC |
| UniformFamilyInP | finite terminal packets extend to a uniform family for all large P and all relevant rows | current ledger has finitely many atoms and runs | false | FiniteLedgerOnlyLocalSurvivor |
| TypeIICoefficientFactorability | signed weights become well-factorable coefficients with nontrivial bilinear/trilinear ranges | LPF tail Type-II obligation identified reciprocal graph thinness | false | TypeIIFactorabilityFailureSAE |
| ConductorOrModulusControl | trace/Kloosterman conductor or AP modulus stays in the required external-theorem range | q-windows are recorded in finite rows | false | ConductorRangePDEC |
| UniformAdjacentRunCancellation | extra total variation compresses to atom-local survivor uniformly, not just in finite ledger | finite cancellation decomposition and selected surplus are closed | false | AdjacentRunCancellationFailureLocalSurvivor |

## 4. 外部定理接入验收

| input | requires | current status | admissible now | url |
| --- | --- | --- | --- | --- |
| Fouvry-Kowalski-Michel-Sawin trace-family technology | ell-adic/trace-function family with monodromy and conductor data | finite terminal run ledger only | false | https://arxiv.org/abs/2511.09459 |
| Milicevic-Qin-Wu bilinear Kloosterman sums | genuine two-variable Kloosterman family over moving q/m variables | q-windows and signed deltas exist, but no Kloosterman kernel formula | false | https://arxiv.org/abs/2511.07550 |
| Pascadi composite-modulus Type-II input | well-factorable signed coefficients and composite-modulus Type-II ranges | LPF/terminal coefficients are finite payload weights, not Type-II coefficients | false | https://arxiv.org/abs/2511.08445 |
| Wright trilinear Kloosterman fractions | trilinear convolution with equidistributed beta sequence | terminal payload has q-runs and atom keys, but no trilinear beta family | false | https://arxiv.org/abs/2604.25177 |
| Runbo Li large-modulus AP/Harman sieve | admissible averaged AP family in the same singular-series convention | row-column target remains pointwise at P^2 scale | false | https://arxiv.org/abs/2602.20917 |

## 5. 最新开放口

```text
TerminalRunTraceAdmissibilityContractPinned AND FiniteSignedRunLedgerIsNotYetUniformTraceFamily AND NeedTraceKernelOrTypeIICoefficientFormulaOrNamedPDECSAE AND UniformAdjacentRunCancellationStillOpen
```

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_terminal_run_trace_admissibility_contract_router.py` | `96551e6f70b84be0be1180d96765a625f5ac74a07d972d900636b5d7c42227c4` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-monotone-run-total-to-net-compression-frontier-router.json` | `ec3616097527b1bf9d426727572ea66b66e15f92ca243d44221f5973437d8613` |
| `docs/monograph/prime-matrix-phi-lpf-corrected-lpf-signed-trace-breakthrough-router.json` | `3a52ce41b6380ad6b884271d246183005d023c29eb162d745a54f668acb16120` |
| `docs/monograph/prime-matrix-phi-lpf-edge-local-signed-atom-trace-sync-router.json` | `49ff41f39b92e54b9cb69a1af808b70115c23c8bc8ef08c0c1d329447e3c68cb` |
| `docs/monograph/prime-matrix-phi-lpf-latest-signed-atom-trace-sync-router.json` | `9391ae3665799bbdc480248f17b0c7900cbafa505cab6ed806b643ea68aa7272` |
| `docs/monograph/prime-matrix-phi-lpf-lpf-tail-typeii-obligation-audit.json` | `16de32e7d4361f9b44dfce7d913d880ba7051a57f3fbd118453db671d5cc6ac5` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `60c0f2d37aa9d351b968bc9ab69236e447dd04ac9154041ff021eb2a1b26b732` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `4c7847cd82a26721dd5611621c797fbeb298d3fb060331ce1f647a244f429ac6` |
| `docs/monograph/external-theorem-index.md` | `ab6ee7fb369cec372fe0d5a57f0350cd5384151601df8405e2c8e3d574fd1654` |
