# Prime Matrix Phi-LPF strict k top-row Oppermann alignment 证书

**状态：** `top_row_identified_as_prime_indexed_oppermann_left_half`

顶行 `k=P-1` 给出：

```text
N_top(P)=pi(P^2-1)-pi(P^2-P).
```

这正是 Oppermann 左半窗 `(n^2-n,n^2)` 在 `n=P` 且 `P` 为素数时的特例。
它比 Legendre 在 `((P-1)^2,P^2)` 的存在性更靠右；Legendre 允许素数落在
`((P-1)^2,P^2-P]`，因此不能推出顶行正性。

## 1. 有限审计

```text
max_prime=5003
prime_base_count=669
all_prime_bases_left_half_positive=true
all_prime_bases_right_half_positive=true
minimum_left_oppermann_count=1
minimum_right_oppermann_count=1
finite_evidence_not_used_as_global_proof=true
```

左半窗最小样本：

```text
P=3, left_oppermann_count=1; P=5, left_oppermann_count=1; P=11, left_oppermann_count=1
```

右半窗最小样本：

```text
P=3, right_oppermann_count=1; P=5, right_oppermann_count=1; P=7, right_oppermann_count=1; P=17, right_oppermann_count=1
```

## 2. 样本行

| P | left count | left first | left last | right count | right first | Legendre count |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 5 | 1 | 23 | 23 | 1 | 29 | 3 |
| 11 | 1 | 113 | 113 | 2 | 127 | 5 |
| 17 | 3 | 277 | 283 | 1 | 293 | 7 |
| 101 | 12 | 10103 | 10193 | 11 | 10211 | 23 |
| 499 | 44 | 248509 | 248987 | 40 | 249017 | 88 |
| 5003 | 281 | 25025041 | 25029959 | 282 | 25030013 | 569 |

## 3. 外部引理边界

- 完整 Oppermann 猜想会直接关闭顶行左半窗和平方右半窗，但它仍是未证猜想。
- Legendre 只给两个平方之间的某处有素数，不能强制落在 `(P^2-P,P^2)`。
- 已知通用短区间指数在 `X=P^2` 上仍长于 `P`，不能关闭长度 `P` 的平方端点窗口。

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| TopRowEqualsPrimeIndexedOppermannLeftHalf | `true` | `true` | k=P-1 顶行正性正是 Oppermann 左半窗 (P^2-P,P^2) 在素数底 P 上的特例。 | exact alignment |
| FullOppermannWouldCloseTopRow | `true` | `false` | 完整 Oppermann 猜想会同时关闭 P^2 左右两个长度 P 半窗，但它不是已知定理。 | Oppermann remains conjectural |
| LegendreDoesNotForceTopHalf | `true` | `true` | Legendre 只要求 ((P-1)^2,P^2) 内有素数，可能落在下半段，不能推出 (P^2-P,P^2) 非空。 | need Oppermann-left strength |
| FiniteLegendreVerificationDoesNotCloseGlobalTopRow | `true` | `true` | Legendre 的有限计算验证只给有限范围且不是左半窗定理，不能作为全局证明。 | finite audit only |
| KnownExternalTheoremsCloseTopRow | `false` | `false` | 当前接入的无条件外部短区间定理没有达到每个素数平方端点长度 P 的半窗强度。 | sqrt-scale or square-phase proof |
| UnifiedPositiveCoreProved | `false` | `false` | 本层只把最坏子核命名为 prime-indexed Oppermann-left；未证明单核正性。 | SquarePhaseSpecialPhaseLongBlockPDECExclusion OR SquarePhaseRoughSurvivorUniformLowerBound |

## 5. 结论

strict 顶行的真实硬点不是 Legendre，而是 Oppermann 左半窗的素数底特例。完整 Oppermann 可关闭该子核，但它是猜想；Legendre 及其有限验证不强制素数落在上半段。当前非循环突破必须直接证明 square-phase 特殊相位不能形成长度 P-1 的低筛全覆盖，或把该全覆盖登记并排斥为 PDEC/SAE/ColumnCRT。

因此 `UnifiedPositiveCore` 的最坏子核可更精确写为：

```text
PrimeIndexedOppermannLeftHalf(P):
  pi(P^2-1)-pi(P^2-P)>=1 for every prime P.
```

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-unified-positive-core-router.json` | `f203a0d971a15e543b30bf22eb2bfea0b62524939af19781cf0ae23d4b92446d` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-square-collar-router.json` | `d1a4c61c54b866038f6263dd795dad16f3d486faf53a9fcbaa45e0ae2228f058` |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-perfect-tiling-router.json` | `6180246c2e8eae53ef5b16c3731190746c95a781e528a85d08188efbc328ee6c` |
| `docs/monograph/prime-matrix-terminal-row-square-phase-bridge-router.md` | `804d2a5a03928e8effc65757870788aefe1dcee4f4efb8dcb9c1a0fc8edbf52b` |
| `docs/monograph/prime-matrix-prime-base-exponent-half-barrier-router.json` | `37d15f13627b753f3c8c322e7836e888f06f1824212537a1fe87e77b58880aee` |
