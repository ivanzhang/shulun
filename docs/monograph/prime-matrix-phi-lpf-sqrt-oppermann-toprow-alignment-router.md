# Prime Matrix Phi-LPF sqrt-Oppermann top-row alignment 路由

**状态：** `sqrt_C_one_equals_prime_indexed_oppermann_left_toprow`
**核验日期：** `2026-05-26`

## 1. 精确对齐

```text
k=P-1 gives I_top=(P^2-P,P^2)
X=P^2 and [X-sqrt(X),X]=[P^2-P,P^2]
Both endpoints P^2-P and P^2 are composite, so any prime in the closed C=1 interval lies in the open top row.
((P-1)^2,P^2)=((P-1)^2,P^2-P] union (P^2-P,P^2), with P-1 integers in each half.
```

核心判定：

```text
top_row_equals_prime_indexed_oppermann_left_half=true
sqrt_C_one_right_endpoint_equivalent_to_top_row=true
legendre_interval_splits_into_equal_lower_leak_and_target_halves=true
legendre_wide_square_interval_implies_top_row=false
row_column_unconditional_closed=false
```

## 2. 样本半窗

| P | lower leak count | top row count | lower primes | top primes | equal halves |
| ---: | ---: | ---: | ---: | ---: | --- |
| 3 | 2 | 2 | 1 | 1 | true |
| 5 | 4 | 4 | 2 | 1 | true |
| 11 | 10 | 10 | 4 | 1 | true |
| 31 | 30 | 30 | 4 | 4 | true |
| 101 | 100 | 100 | 11 | 12 | true |
| 1009 | 1008 | 1008 | 71 | 70 | true |
| 10007 | 10006 | 10006 | 548 | 566 | true |

## 3. 常数泄漏样本

| P | C label | top row isolated | lower leak count | meaning |
| ---: | --- | --- | ---: | --- |
| 3 | C=1 | true | 0 | C=1 isolates top row; fixed C>1 creates lower leak strip |
| 3 | C=1.0001 | false | 1 | C=1 isolates top row; fixed C>1 creates lower leak strip |
| 3 | C=sqrt(2) lower bound | false | 1 | positive fixed-proportion leakage below P^2-P |
| 3 | Legendre C=(2P-1)/P | false | 2 | Legendre open square interval splits into two equal integer halves |
| 3 | C=2 | false | 3 | C=1 isolates top row; fixed C>1 creates lower leak strip |
| 5 | C=1 | true | 0 | C=1 isolates top row; fixed C>1 creates lower leak strip |
| 5 | C=1.0001 | false | 1 | C=1 isolates top row; fixed C>1 creates lower leak strip |
| 5 | C=sqrt(2) lower bound | false | 2 | positive fixed-proportion leakage below P^2-P |
| 5 | Legendre C=(2P-1)/P | false | 4 | Legendre open square interval splits into two equal integer halves |
| 5 | C=2 | false | 5 | C=1 isolates top row; fixed C>1 creates lower leak strip |
| 11 | C=1 | true | 0 | C=1 isolates top row; fixed C>1 creates lower leak strip |
| 11 | C=1.0001 | false | 1 | C=1 isolates top row; fixed C>1 creates lower leak strip |
| 11 | C=sqrt(2) lower bound | false | 4 | positive fixed-proportion leakage below P^2-P |
| 11 | Legendre C=(2P-1)/P | false | 10 | Legendre open square interval splits into two equal integer halves |
| 11 | C=2 | false | 11 | C=1 isolates top row; fixed C>1 creates lower leak strip |
| 31 | C=1 | true | 0 | C=1 isolates top row; fixed C>1 creates lower leak strip |
| 31 | C=1.0001 | false | 1 | C=1 isolates top row; fixed C>1 creates lower leak strip |
| 31 | C=sqrt(2) lower bound | false | 12 | positive fixed-proportion leakage below P^2-P |
| 31 | Legendre C=(2P-1)/P | false | 30 | Legendre open square interval splits into two equal integer halves |
| 31 | C=2 | false | 31 | C=1 isolates top row; fixed C>1 creates lower leak strip |
| 101 | C=1 | true | 0 | C=1 isolates top row; fixed C>1 creates lower leak strip |
| 101 | C=1.0001 | false | 1 | C=1 isolates top row; fixed C>1 creates lower leak strip |
| 101 | C=sqrt(2) lower bound | false | 41 | positive fixed-proportion leakage below P^2-P |
| 101 | Legendre C=(2P-1)/P | false | 100 | Legendre open square interval splits into two equal integer halves |
| 101 | C=2 | false | 101 | C=1 isolates top row; fixed C>1 creates lower leak strip |
| 1009 | C=1 | true | 0 | C=1 isolates top row; fixed C>1 creates lower leak strip |
| 1009 | C=1.0001 | false | 1 | C=1 isolates top row; fixed C>1 creates lower leak strip |
| 1009 | C=sqrt(2) lower bound | false | 417 | positive fixed-proportion leakage below P^2-P |
| 1009 | Legendre C=(2P-1)/P | false | 1008 | Legendre open square interval splits into two equal integer halves |
| 1009 | C=2 | false | 1009 | C=1 isolates top row; fixed C>1 creates lower leak strip |
| 10007 | C=1 | true | 0 | C=1 isolates top row; fixed C>1 creates lower leak strip |
| 10007 | C=1.0001 | false | 2 | C=1 isolates top row; fixed C>1 creates lower leak strip |
| 10007 | C=sqrt(2) lower bound | false | 4145 | positive fixed-proportion leakage below P^2-P |
| 10007 | Legendre C=(2P-1)/P | false | 10006 | Legendre open square interval splits into two equal integer halves |
| 10007 | C=2 | false | 10007 | C=1 isolates top row; fixed C>1 creates lower leak strip |

## 4. 最新开放口

```text
PrimeIndexedOppermannLeftTopRowOrSharpCOneSqrtInputStillOpen AND LegendreWideSquareIntervalDoesNotImplyTopRow AND AnyFixedSqrtConstantGreaterThanOneHasLowerLeakStrip AND PointwisePsiAtSharpSqrtScaleOrAdmissibleSignedTypeIIFamilyStillOpen
```

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_sqrt_oppermann_toprow_alignment_router.py` | `f163753942294fc77c3bf0a21962d35401e05c2e0a3f17fd884a6c7679902fb8` |
| `docs/monograph/prime-matrix-phi-lpf-sqrt-constant-threshold-router.json` | `26d483db1f25930b40cd2389a16de1e30f01973723adcf5afb54d8b18d2f9191` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-square-collar-router.json` | `d1a4c61c54b866038f6263dd795dad16f3d486faf53a9fcbaa45e0ae2228f058` |
| `docs/monograph/prime-matrix-phi-lpf-sqrt-constant-threshold-router.md` | `45a9c72f0cdd008e76b9ee0f1b6e445fc6101ce569784c4278921ca660c09988` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `b7b27008481045b6017de0210e01af835b8d8c498ff3134a4f81bcf6a03f9883` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `47fe5479f28561d4e35268a1851f9637cacb1d5086de5e485f5e7bdc3fad9453` |
| `docs/monograph/external-theorem-index.md` | `c0d27706c9114d73ff3b0b872cd863b305b06a774e1c3e0b60788ce9f70ce464` |
