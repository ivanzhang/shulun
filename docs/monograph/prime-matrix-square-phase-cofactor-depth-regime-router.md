# Prime Matrix square-phase cofactor 因子深度分层路由器

**状态：** `short_cofactor_rough_load_split_by_factor_depth_open`

dyadic cofactor rough 负载已按因子深度分层。若块左端 `z>P^{2/3}`，互补因子只能是素数，直接并入 RFP/reciprocal-floor 路线；若 `z>P^{1/2}`，互补因子至多半素数，剩余为 pair-correlation/PDEC；低于平方根阈值的块才需要真正的多层 Buchstab cofactor 负载上界。这一步没有排除各层负载，只把一阶负载硬点拆成三个有边界的层。

```text
cofactor_depth_inequality_closed=true
high_alpha_prime_cofactor_route_closed=true
middle_alpha_semiprime_route_closed=true
short_cofactor_load_bound_closed=false
row_column_unconditional_closed=false
```

## 1. 深度阈值

| max depth | alpha threshold | statement |
| ---: | ---: | --- |
| 1 | 1.000000 | if z>P^1.000000, then z-rough cofactor has at most 1 prime factors |
| 2 | 0.666667 | if z>P^0.666667, then z-rough cofactor has at most 2 prime factors |
| 3 | 0.500000 | if z>P^0.500000, then z-rough cofactor has at most 3 prime factors |
| 4 | 0.400000 | if z>P^0.400000, then z-rough cofactor has at most 4 prime factors |
| 5 | 0.333333 | if z>P^0.333333, then z-rough cofactor has at most 5 prime factors |

## 2. 样本 dyadic 块

| P | block | alpha(left) | max factor depth | regime |
| ---: | --- | ---: | ---: | --- |
| 10007 | `(31,62]` | 0.372812 | 4 | `LowAlphaBuchstabCofactorLoadBoundOrPDEC` |
| 10007 | `(62,124]` | 0.448064 | 3 | `LowAlphaBuchstabCofactorLoadBoundOrPDEC` |
| 10007 | `(124,248]` | 0.523316 | 2 | `MiddleAlphaSemiprimeCofactorPairCorrelationPDEC` |
| 10007 | `(248,496]` | 0.598567 | 2 | `MiddleAlphaSemiprimeCofactorPairCorrelationPDEC` |
| 10007 | `(496,992]` | 0.673819 | 1 | `HighAlphaPrimeCofactorRFPOrReciprocalFloorPDEC` |
| 10007 | `(992,1984]` | 0.749071 | 1 | `HighAlphaPrimeCofactorRFPOrReciprocalFloorPDEC` |
| 10007 | `(1984,3681]` | 0.824323 | 1 | `HighAlphaPrimeCofactorRFPOrReciprocalFloorPDEC` |
| 36739 | `(31,62]` | 0.326686 | 5 | `LowAlphaBuchstabCofactorLoadBoundOrPDEC` |
| 36739 | `(62,124]` | 0.392627 | 4 | `LowAlphaBuchstabCofactorLoadBoundOrPDEC` |
| 36739 | `(124,248]` | 0.458568 | 3 | `LowAlphaBuchstabCofactorLoadBoundOrPDEC` |
| 36739 | `(248,496]` | 0.524509 | 2 | `MiddleAlphaSemiprimeCofactorPairCorrelationPDEC` |
| 36739 | `(496,992]` | 0.590450 | 2 | `MiddleAlphaSemiprimeCofactorPairCorrelationPDEC` |
| 36739 | `(992,1984]` | 0.656392 | 2 | `MiddleAlphaSemiprimeCofactorPairCorrelationPDEC` |
| 36739 | `(1984,3968]` | 0.722333 | 1 | `HighAlphaPrimeCofactorRFPOrReciprocalFloorPDEC` |
| 36739 | `(3968,7936]` | 0.788274 | 1 | `HighAlphaPrimeCofactorRFPOrReciprocalFloorPDEC` |
| 36739 | `(7936,13515]` | 0.854215 | 1 | `HighAlphaPrimeCofactorRFPOrReciprocalFloorPDEC` |
| 83561 | `(31,62]` | 0.302999 | 5 | `LowAlphaBuchstabCofactorLoadBoundOrPDEC` |
| 83561 | `(62,124]` | 0.364159 | 4 | `LowAlphaBuchstabCofactorLoadBoundOrPDEC` |
| 83561 | `(124,248]` | 0.425319 | 3 | `LowAlphaBuchstabCofactorLoadBoundOrPDEC` |
| 83561 | `(248,496]` | 0.486479 | 3 | `LowAlphaBuchstabCofactorLoadBoundOrPDEC` |
| 83561 | `(496,992]` | 0.547639 | 2 | `MiddleAlphaSemiprimeCofactorPairCorrelationPDEC` |
| 83561 | `(992,1984]` | 0.608799 | 2 | `MiddleAlphaSemiprimeCofactorPairCorrelationPDEC` |
| 83561 | `(1984,3968]` | 0.669959 | 1 | `HighAlphaPrimeCofactorRFPOrReciprocalFloorPDEC` |
| 83561 | `(3968,7936]` | 0.731119 | 1 | `HighAlphaPrimeCofactorRFPOrReciprocalFloorPDEC` |
| 83561 | `(7936,15872]` | 0.792279 | 1 | `HighAlphaPrimeCofactorRFPOrReciprocalFloorPDEC` |
| 83561 | `(15872,30740]` | 0.853439 | 1 | `HighAlphaPrimeCofactorRFPOrReciprocalFloorPDEC` |
| 200003 | `(31,62]` | 0.281334 | 6 | `LowAlphaBuchstabCofactorLoadBoundOrPDEC` |
| 200003 | `(62,124]` | 0.338121 | 4 | `LowAlphaBuchstabCofactorLoadBoundOrPDEC` |
| 200003 | `(124,248]` | 0.394908 | 4 | `LowAlphaBuchstabCofactorLoadBoundOrPDEC` |
| 200003 | `(248,496]` | 0.451695 | 3 | `LowAlphaBuchstabCofactorLoadBoundOrPDEC` |
| 200003 | `(496,992]` | 0.508482 | 2 | `MiddleAlphaSemiprimeCofactorPairCorrelationPDEC` |
| 200003 | `(992,1984]` | 0.565269 | 2 | `MiddleAlphaSemiprimeCofactorPairCorrelationPDEC` |
| 200003 | `(1984,3968]` | 0.622056 | 2 | `MiddleAlphaSemiprimeCofactorPairCorrelationPDEC` |
| 200003 | `(3968,7936]` | 0.678843 | 1 | `HighAlphaPrimeCofactorRFPOrReciprocalFloorPDEC` |
| 200003 | `(7936,15872]` | 0.735630 | 1 | `HighAlphaPrimeCofactorRFPOrReciprocalFloorPDEC` |
| 200003 | `(15872,31744]` | 0.792417 | 1 | `HighAlphaPrimeCofactorRFPOrReciprocalFloorPDEC` |
| 200003 | `(31744,63488]` | 0.849204 | 1 | `HighAlphaPrimeCofactorRFPOrReciprocalFloorPDEC` |
| 200003 | `(63488,73576]` | 0.905991 | 1 | `HighAlphaPrimeCofactorRFPOrReciprocalFloorPDEC` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `CofactorDepthInequalityClosed` | `true` | `true` | 若 q>z 且 m<=P^2/z 为 z-rough，则 m 的素因子数由 z^t<P^2/z 控制。 | none |
| `HighAlphaPrimeCofactorRoute` | `true` | `true` | z>P^{2/3} 时 cofactor 必为素数，回到 RFP/reciprocal-floor 素互补因子路线。 | HighAlphaPrimeCofactorRFPOrReciprocalFloorPDEC |
| `MiddleAlphaSemiprimeRoute` | `true` | `true` | z>P^{1/2} 时 cofactor 至多半素数，剩余是双素因子 pair-correlation/PDEC。 | MiddleAlphaSemiprimeCofactorPairCorrelationPDEC |
| `LowAlphaBuchstabRoute` | `true` | `false` | z<=P^{1/2} 仍需 Buchstab 多层 cofactor 负载账本或 PDEC。 | LowAlphaBuchstabCofactorLoadBoundOrPDEC |
| `ShortCofactorLoadBoundClosed` | `false` | `false` | 因子深度分层已完成，但各层负载上界尚未排除。 | LowAlphaBuchstabCofactorLoadBoundOrPDEC OR MiddleAlphaSemiprimeCofactorPairCorrelationPDEC OR HighAlphaPrimeCofactorRFPOrReciprocalFloorPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未排除所有 cofactor 负载层与 RFP reciprocal-floor 缺陷。 | cofactor layer bounds + RFP reciprocal-floor exclusion |

## 4. 下一步

- 主攻 `LowAlphaBuchstabCofactorLoadBoundOrPDEC`：低 alpha 块的多层 Buchstab cofactor 负载上界，或失败 PDEC。
- 并行保留 `MiddleAlphaSemiprimeCofactorPairCorrelationPDEC` 与 `HighAlphaPrimeCofactorRFPOrReciprocalFloorPDEC`，分别处理中高 alpha 的半素数/素互补因子层。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-dyadic-first-moment-cofactor-duality.json` | `071d009e1b6c5271a6957acabc4002f13b7be7e324a10e53bb804a6ddd1285de` |
| `docs/monograph/prime-matrix-square-phase-rfp-excess-dimension-collapse-router.json` | `e02f20abf0485d8f0ef78e16c1a2262984c3d4c835359326dc5ef063ec05157e` |
| `experiments/prime_matrix_square_phase_cofactor_depth_regime_router.py` | `20b97190299e44adc16fb6fce887cef7fc61464c0364edf9abd9190a2df8f63f` |
