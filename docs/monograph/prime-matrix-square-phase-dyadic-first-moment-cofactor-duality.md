# Prime Matrix square-phase dyadic 一阶负载 cofactor 对偶账本

**状态：** `dyadic_first_moment_exactly_reduced_to_short_cofactor_rough_intervals_open`

dyadic 一阶负载 `H_B` 与互补因子短区间计数完全相同：`q` 命中进入块幸存列 `k` 当且仅当存在 `m` 使 `P^2+k=q*m`，且 `m` 位于 `(P^2/q,(P^2+P)/q]`。由于 `k` 已避开 `<=z` 的负平方相位，该 `m` 也没有 `<=z` 的素因子。当前已核验该对偶身份，下一硬点是这些短 cofactor rough 区间的负载上界或 PDEC。

```text
cofactor_duality_identity_checked=true
cofactor_duality_mismatch_count=0
short_cofactor_interval_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 对偶恒等式

对进入块幸存集 `S_z` 与 dyadic 块 `B=(z,z']`，

```text
H_B=sum_{q in B} |S_z cap {-P^2 mod q}|
   =sum_{q in B} #{m: P^2/q < m <= (P^2+P-1)/q, q*m-P^2 in S_z}.
```

若 `q*m-P^2 in S_z`，则 `m` 没有 `<=z` 的素因子；否则对应小素数也会整除 `P^2+k`，与 `k in S_z` 矛盾。

## 2. 极值

| item | P | block | cofactor hits | capacity | hit density | prime share | max q hit | max q capacity |
| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `worst_hits` | 200003 | `(31,62]` | 4540 | 29633 | 0.153208 | 0.320705 | 825 | 5406 |
| `worst_density` | 10007 | `(31,62]` | 232 | 1484 | 0.156334 | 0.461207 | 42 | 271 |

## 3. 每个 P 的最大 cofactor 负载

| P | y | block | cofactor hits | prime hits | composite hits | prime share | capacity | density |
| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 10007 | 3681 | `(31,62]` | 232 | 107 | 125 | 0.461207 | 1484 | 0.156334 |
| 36739 | 13515 | `(31,62]` | 831 | 306 | 525 | 0.368231 | 5446 | 0.152589 |
| 83561 | 30740 | `(31,62]` | 1892 | 650 | 1242 | 0.343552 | 12381 | 0.152815 |
| 200003 | 73576 | `(31,62]` | 4540 | 1456 | 3084 | 0.320705 | 29633 | 0.153208 |

## 4. 证明边界

- 已闭合：`DyadicSquarePhaseFirstMomentLoadPDEC` 的 cofactor 对偶身份。
- 未闭合：`DyadicShortCofactorRoughIntervalLoadBoundOrPDEC`，即短 cofactor interval 的 rough 负载上界，或其失败进入 PDEC/SAE。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-dyadic-deletion-excess-split-router.json` | `34770fe0730a11c7fc7346ce7eaad7a3b70d0a347f51ca8bbb683279322ab42e` |
| `docs/monograph/prime-matrix-square-phase-dyadic-first-moment-ledger.json` | `befbb3c4a4d0f36737eec7f8a956f938f9b7230ec6308af98cb8e45f8c87bf3e` |
| `experiments/prime_matrix_square_phase_dyadic_first_moment_cofactor_duality.py` | `20b3c6bd4026ddf28e6de32c7c9c392e7961c26dad81a404f3b7aace7aa6d51e` |
