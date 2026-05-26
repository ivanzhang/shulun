# Prime Matrix Phi-LPF Oppermann subcore not-full-closure 路由

**状态：** `top_row_oppermann_left_is_necessary_but_not_sufficient`
**核验日期：** `2026-05-26`

## 1. 逻辑边界

```text
For each prime P, strict-row positivity asks pi((k+1)P-1)-pi(kP)>=1 for every 1<=k<P.
The top row k=P-1 is pi(P^2-1)-pi(P^2-P)>=1, i.e. prime-indexed Oppermann-left.
All strict rows are positive iff h(kP)<P for every 1<=k<P, where h(x)=next_prime_after(x)-x.
The top row alone is h(P^2-P)<P.
```

核心判定：

```text
row_column_strict_positivity_implies_toprow=true
top_row_input_alone_closes_all_strict_rows=false
top_row_input_is_necessary_not_sufficient=true
all_rows_equivalent_to_prime_gap_bound_h_kP_less_than_P=true
row_column_unconditional_closed=false
phi_lpf_parity_barrier_globally_broken=false
```

## 2. 有限样本

| P | strict rows | rows covered by top input | coverage fraction | sample rows with prime | top primes | max h(kP) | all h(kP)<P |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 3 | 2 | 1 | 0.500000000 | 2 | 1 | 2 | true |
| 5 | 4 | 1 | 0.250000000 | 4 | 1 | 3 | true |
| 11 | 10 | 1 | 0.100000000 | 10 | 1 | 4 | true |
| 31 | 30 | 1 | 0.033333333 | 30 | 4 | 14 | true |
| 101 | 100 | 1 | 0.010000000 | 100 | 12 | 28 | true |
| 1009 | 1008 | 1 | 0.000992063 | 1008 | 70 | 70 | true |

样本列只检验实现与等价关系；全局闭合仍需要逐行 `h(kP)<P`，不能由单个 top row 输入替代。

## 3. 最新开放口

```text
TopRowOppermannLeftIsNecessarySubcoreNotFullClosure AND FullRowsRequireGapBoundHkPLessThanPForEveryK AND LPFPhiExactCountsRemainUnsignedParityBlind AND PointwisePsiAtSharpSqrtScaleOrAdmissibleSignedTypeIIFamilyStillOpen
```

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_oppermann_subcore_not_full_closure_router.py` | `3fb036db0c793bb490deca7cd65b86de3acd9bf3539fddac090513dec0ff1779` |
| `docs/monograph/prime-matrix-phi-lpf-sqrt-oppermann-toprow-alignment-router.json` | `44cdef5d82dccf99d5dbfd4ef3a8cecde44b77e9f75e5fb04921085498e0cb75` |
| `docs/monograph/prime-matrix-phi-lpf-sqrt-constant-threshold-router.json` | `26d483db1f25930b40cd2389a16de1e30f01973723adcf5afb54d8b18d2f9191` |
| `docs/monograph/prime-matrix-phi-lpf-legendre-phi-periodic-truncation-error-audit.json` | `975aa118af686bd729414f291af1efd9fa60082d622ac687d7f87772246acd6e` |
| `docs/monograph/prime-matrix-phi-lpf-exact-bucket-endpoint-equivalence-audit.json` | `92468974eceab624e5a553bb3a24e20a85b9e3f5424b674bb9f00057a53ccfc5` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `5ed4fd3275a2cafff9851c7190b3198675062644569f6baca0db0b961668bc09` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `e77b2b653c04a9f97e59e6defb818204eecbca265143409bcdd87a73d111121a` |
| `docs/monograph/external-theorem-index.md` | `388eb5db14b01a7e66e8ebd35edb1334e22d0d05c7780fc142d102bfa4155dbd` |
