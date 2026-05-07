# Triad-A1 SourceBlockEntropy 路由审计

**状态：** `source_block_entropy_not_forced_by_formal_wfd_inputs`

SourceBlockEntropy 是足够强的正确入口：一旦证明，即可推出 NC-BLK。但它不由当前形式 WFD/Type-I-II/Fourier 准入条件强制；moving-delta well-factorable 模型在每个尺度集中到一个新 `(u,v)` 块，仍能通过形式模板。内部无黑箱路线必须继续证明 exact WFD source entropy，外部路线仍是 DI/BFI 原始 dispersion。

## 1. 条件闭合律

若实际源块满足 max_b M_b/M <= log(y)^(-2A)，则 sum_b |S_b|^2 <= sum_b M_b^2 <= max_b(M_b/M) M^2，从而得到 NC-BLK 所需的任意对数块能量节省。

写成结构公式：

```text
M_b = Cauchy capacity of moving block b=(u,v)
M   = sum_b M_b
if max_b M_b/M <= log(y)^(-2A), then
  sum_b |S_b|^2 <= sum_b M_b^2 <= log(y)^(-2A) M^2.
```

因此 `SourceBlockEntropyNCBLK` 本身是正确的充分条件；问题只剩它是否能从上游结构推出。

## 2. moving-delta 阻断律

形式 well-factorable/Type/Fourier 模板只限制因子可分解性、系数大小与频率平滑，不禁止每个尺度选择一个新的 moving block b_y=(u_y,v_y) 承载全部容量。因此 SourceBlockEntropy 不能由当前形式输入自动推出。

```text
well-factorable convolution permits bounded point-supported factors at template level；
Type-I/II decomposition is algebraic and does not create block entropy；
Fourier smoothing controls h, not the moving block b=(u,v)；
fixed-projection diffuse cannot see a block label moving with the scale。
```

## 3. 汇总

- `moving_block_input_status=moving_block_spread_not_implied_by_fixed_projection_diffuse`。
- `conditional_source_entropy_implies_ncblk=True`。
- `source_entropy_gap_exists=True`。
- `current_internal_source_entropy_closed=False`。
- `all_spread_models_satisfy_source_entropy=True`。
- `all_moving_delta_models_violate_source_entropy=True`。
- `next_internal_target=ExactWFDSourceEntropy`。
- `terminal_gap_after_router=ExactWFDSourceEntropyOrExternalDIBFIOriginalDispersion`。

## 4. 缺口表

| gate | available | needed | gap | route | closed |
| --- | --- | --- | --- | --- | --- |
| `WellFactorableConvolution` | lambda_c admits bounded convolution factorizations after choosing dyadic ranges | each moving same-(u,v) block has max capacity share <= log(y)^(-2A) | bounded convolution factors may be point-supported on a moving u and v | prove exact sieve weights have anti-atom entropy, not merely well-factorability | `False` |
| `TypeITypeIIDecomposition` | Vaughan/Heath-Brown blocks with divisor-bounded coefficients | entropy across factor-pair blocks after every Type split | Type decomposition is algebraic and does not forbid one dyadic factor-pair from carrying the mass | add a genuine source anti-concentration theorem for the produced coefficients | `False` |
| `FourierSmoothing` | smooth h-window and finite nonzero Fourier frequencies | non-concentration in the moving block coordinate b=(u,v) | frequency smoothing acts in h, not in the factorization block coordinate | prove block entropy before or inside the dispersion identity | `False` |
| `FixedProjectionDiffuse` | every fixed finite signature eventually has small mass | uniform control of growing labels b_y=(u_y,v_y) | a moving-delta block can evade every fixed projection while staying concentrated | replace fixed-projection diffuse by scale-uniform moving-block entropy | `False` |
| `ConditionalImplicationToNCBLK` | Cauchy capacity identity sum_b M_b^2 <= max_b(M_b/M) M^2 | max_b M_b/M <= log(y)^(-2A) for actual source blocks | the implication is valid, but the hypothesis is not yet proved upstream | ExactWFDSourceEntropy or external original dispersion | `True` |

## 5. 模型审计表

| k | log y | required max share | entropy needed | spread blocks | spread share | delta share | delta violates |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 3 | 6.90776 | 0.00043919 | 7.73058 | 2277 | 0.000439174 | 1 | `True` |
| 4 | 9.21034 | 0.000138962 | 8.88131 | 7197 | 0.000138947 | 1 | `True` |
| 5 | 11.5129 | 5.6919e-05 | 9.77388 | 17569 | 5.69184e-05 | 1 | `True` |
| 6 | 13.8155 | 2.74494e-05 | 10.5032 | 36431 | 2.74492e-05 | 1 | `True` |
| 7 | 16.1181 | 1.48165e-05 | 11.1198 | 67493 | 1.48164e-05 | 1 | `True` |
| 8 | 18.4207 | 8.68515e-06 | 11.6539 | 115140 | 8.68508e-06 | 1 | `True` |
| 9 | 20.7233 | 5.4221e-06 | 12.125 | 184431 | 5.42208e-06 | 1 | `True` |

## 6. 可接受输入

| input | statement | would imply | status |
| --- | --- | --- | --- |
| `ExactWFDSourceEntropy` | for the exact Rosser/Iwaniec-Buchstab + Type-I/II + Fourier coefficients, max moving same-(u,v) block capacity share is <= log(y)^(-2A) | SourceBlockEntropyNCBLK, hence NC-BLK via the Cauchy capacity inequality | `not_present_in_current_ledger` |
| `StrengthenedCleanAdmissionWithMovingEntropy` | upgrade K1--K9 clean admission to include scale-uniform moving-block entropy | internal A1 clean branch closure after proving the upgraded admission from prior routes | `would_be_sufficient_but_unproved` |
| `ExternalDIBFIOriginalDispersion` | original DI/BFI dispersion theorem supplies the needed block variance saving directly | A1 clean branch closed in external-deep-theorem version | `acceptable_external_route` |

## 7. 结论

本步给出一个正向闭合和一个负向阻断：

```text
SourceBlockEntropyNCBLK => NC-BLK;
formal WFD/Type-I-II/Fourier inputs do not imply SourceBlockEntropyNCBLK.
```

所以下一步若继续完全无黑箱路线，目标必须再收窄为：

```text
ExactWFDSourceEntropy:
prove the exact sieve/Type/Fourier coefficients cannot concentrate on a moving same-(u,v) block.
```

否则只能切到外部 `DI/BFI original dispersion`。
