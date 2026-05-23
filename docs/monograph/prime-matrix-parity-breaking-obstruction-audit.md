# Prime Matrix 破奇偶候选源障碍审计

**状态**：`parity_breaking_candidates_screened_no_direct_closure`
**核验日期**：`2026-05-23`

## 1. 原子结论

- 当前没有任何外部破奇偶候选源同时通过五个门。
- Li--Zhang--Cai 的 `P2` AP 结果进入 `P^2` 方阵，但对象不是素数。
- Friedlander--Iwaniec 是真正非线性破奇偶模型，但对象不是 Prime Matrix 行/列。
- BFI/DI/Kuznetsov/Maynard 技术只能作为未来同对象 theorem-match 或构造器的工具，不能直接替代固定网格点态正性。
- 因此最新硬点不是“再找一个筛恒等式”，而是构造同对象实际素数源，或证明 fixed `q=P` 零例外转移。

## 2. 五门验收

```text
PrimeObjectNotP2AlmostPrime
SquareScaleWindowOrP2ColumnCompatibility
RigidPointwiseGridOrFixedPrimeModulusZeroException
SameObjectNonlinearActualSourceConstructorBeforeProjection
UnconditionalPublishedOrIndependentlyAcceptedInput
```

## 3. 候选源审计表

| candidate | category | status | direct closure | failed gates | usable as | obstruction |
|---|---|---|---|---|---|---|
| Li-Zhang-Cai least P2 almost-prime in AP | `P2_almost_prime_AP` | `arXiv_v2_wrong_parity_object` | `false` | PrimeObjectNotP2AlmostPrime, SameObjectNonlinearActualSourceConstructorBeforeProjection, UnconditionalPublishedOrIndependentlyAcceptedInput | sharp_column_parity_barrier_marker | 给出的是至多两个素因子的 almost-prime，不是素数；正好卡在奇偶对象门。 |
| Friedlander-Iwaniec polynomial X^2+Y^4 | `nonlinear_prime_values` | `published_model_primary_arxiv_available` | `false` | SquareScaleWindowOrP2ColumnCompatibility, RigidPointwiseGridOrFixedPrimeModulusZeroException, SameObjectNonlinearActualSourceConstructorBeforeProjection | technical_model_not_importable_closure | 证明不同非线性多项式族含无穷多素数；没有把每个 Prime Matrix 行/列嵌入该族的同对象源构造。 |
| Bombieri-Friedlander-Iwaniec / Maynard well-factorable large-moduli AP | `well_factorable_AP_dispersion` | `external_dispersion_technology_class` | `false` | SquareScaleWindowOrP2ColumnCompatibility, RigidPointwiseGridOrFixedPrimeModulusZeroException, SameObjectNonlinearActualSourceConstructorBeforeProjection | candidate_external_theorem_match_after_exact_variable_translation | 提供 AP/权重平均分布技术；未给固定素模数 P、每个剩余类、P^2 方阵内的零例外定理，也未匹配本文 full-S non-AP WFD 对象。 |
| Deshouillers-Iwaniec / Kuznetsov spectral large sieve | `kloosterman_spectral_dispersion` | `published_spectral_tool` | `false` | PrimeObjectNotP2AlmostPrime, SquareScaleWindowOrP2ColumnCompatibility, RigidPointwiseGridOrFixedPrimeModulusZeroException, SameObjectNonlinearActualSourceConstructorBeforeProjection | subtool_for_exact_KLS_match_only | 谱大筛是 Kloosterman 平均抵消工具，不直接产生素数对象或刚性行列点态正性。 |
| Ford-Maynard prime-producing sieve framework | `prime_producing_sieve_theory` | `frontier_framework` | `false` | SquareScaleWindowOrP2ColumnCompatibility, RigidPointwiseGridOrFixedPrimeModulusZeroException, SameObjectNonlinearActualSourceConstructorBeforeProjection, UnconditionalPublishedOrIndependentlyAcceptedInput | design_guidance_for_future_internal_constructor | 给出 prime-producing sieve 的理论框架；尚未包含本文 P 行/列方阵的实际构造器与逐点窗口常数。 |
| Maynard small gaps / multidimensional Selberg weights | `multidimensional_sieve` | `published_prime_object_wrong_conclusion_type` | `false` | SquareScaleWindowOrP2ColumnCompatibility, RigidPointwiseGridOrFixedPrimeModulusZeroException, SameObjectNonlinearActualSourceConstructorBeforeProjection | wrong_conclusion_type | 结论是无穷多 admissible tuple 中多素数，而不是每个长度 P 的刚性区间或每个 mod P 列中有素数。 |
| Rosser-Iwaniec beta sieve / linear sieve | `linear_sieve` | `classical_published_but_parity_limited` | `false` | PrimeObjectNotP2AlmostPrime, SquareScaleWindowOrP2ColumnCompatibility, RigidPointwiseGridOrFixedPrimeModulusZeroException, SameObjectNonlinearActualSourceConstructorBeforeProjection | negative_control | 在 H_P 的 s<=2 区域下界函数退化为 0；它解释屏障而不提供破屏障源。 |

## 4. 最新剩余基

```text
PrimeObjectNotP2AlmostPrime
RigidPointwiseGridOrFixedPrimeModulusZeroException
SameObjectNonlinearActualSourceConstructorBeforeProjection
MeanValueAPToFixedPrimeModulusZeroExceptionTransfer
PointwiseShortIntervalPrimeTheoremThetaLeHalf
LinnikExponentLeTwoWithSquareWindowConstants
```

## 5. 边界声明

本审计不把 P2、平均 AP 或不同非线性多项式改名为证明；它把破奇偶路线压成同对象实际源构造或固定素模数零例外转移。

```text
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
row_column_unconditional_closed=false
direct_closure_candidate_count=0
```
