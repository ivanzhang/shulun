# Prime Matrix Phi-LPF affine endpoint LPF first-hit 证书

**状态：** `endpoint_prime_leak_lpf_first_hit_partition_closed_prime_extraction_open`
**核验日期：** `2026-05-25`

本证书把 `m=2n+1` 轴上的奇素数零类按最小素因子第一次命中精确分割。

## 1. 核心身份

```text
m=p           -> endpoint prime leak, k=0
m=p(2k+1)     -> composite LPF tail, k>=1
2n+1=p(2k+1)  -> n=kp+(p-1)/2
LPF(2k+1)>=p  -> LPF(2n+1)=p
```

这给 Phi-LPF 递推提供了从小到大剥离素因子的精确 first-hit 账本：
端点素数 `m=p` 必须单独作为 prime leak 发射；合数尾才进入 LPF bucket。

## 2. 审计读数

```text
endpoint_prime_leak_separated=true
lpf_tail_composite_partition_closed=true
zero_class_duplicate_overcount_positive=true
cofactor_parity_mixture_present_in_tail=true
prime_extraction_from_lpf_tail_proved=false
signed_payload_or_von_mangoldt_weight_constructed=false
row_column_unconditional_closed=false
```

| X | M=2X+1 | odd m | endpoint primes | composite tails | zero-class duplicate overcount | semiprime tails | higher tails |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 100 | 201 | 100 | 45 | 55 | 50 | 38 | 17 |
| 1000 | 2001 | 1000 | 302 | 698 | 831 | 409 | 289 |
| 10000 | 20001 | 10000 | 2261 | 7739 | 10829 | 3852 | 3887 |
| 50000 | 100001 | 50000 | 9591 | 40409 | 61448 | 18246 | 22163 |

`zero-class duplicate overcount` 为正说明：所有零类命中不能直接相加，必须按
`LPF(m)` first-hit 分配，否则同一个合数会被多个素因子重复计算。

## 3. 尾部仍是奇偶性障碍

合数尾中同时存在 cofactor 为素数的半素数层和更高合数层。仅靠 Euler product、
forbidden residue、Phi 递推或 LPF 桶计数，不会自动生成区分这些层的符号权重。
因此本层闭合的是 first-hit partition，不是 prime extraction。

## 4. 最新开放口

```text
EndpointPrimeLeakSeparatedFromLPFTailButPrimeExtractionStillParityBlocked AND TerminalSiblingQSpineWheelGapLockPaymentOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_affine_endpoint_lpf_first_hit_router.py` | `0f19905b882e24d7251f745d7e664da4974a6b3b5129f776f2f49525e713640d` |
| `docs/monograph/prime-matrix-phi-lpf-affine-odd-euler-normalization-router.json` | `6f0a674fbf664cebc3a17c49a62fb8757a8ca3dd004403d023c0fc1746c23ecc` |
| `docs/monograph/prime-matrix-affine-2n-plus-1-euler-lpf-parity-audit.json` | `ea96150bd831cd8bc6bad2fe47b848ba78ea11325b97faeb5961be4046515c88` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `3964ebad90ad537f88fdc7a0b718af9ec69c7064c432579542f46f85df3734cd` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `e87d2a15e2f8b91c6bafba5abb7dfd203add7beec055e10a360a3d84395616e7` |
| `docs/monograph/external-theorem-index.md` | `f16a2bb8ab4ea23b127c5d9d399fe018724816f2e7293768833e0f3bc081ae2c` |
