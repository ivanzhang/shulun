# Triad-A1 Kuznetsov-LS 原子前沿路由器

**状态：** `a1_sc9_frontier_routed_to_ncblk_or_external_dibfi`

A1 的 SC-9 谱大筛口已经继续压缩：不是泛泛的 Kuznetsov 大筛缺口，而是 KZ-E 内部路线的真实阻断 `NC-BLK`，或明确转入外部 DI/BFI 原始 dispersion 引用。

## 1. 结构律

The A1 clean branch reaches SC-9 only after K1--K9 admission. Existing HLC/KLS documents expand SC-9 into KZ-A--KZ-E. KZ-A--KZ-D are routed by smoothing, trace specialization, Bessel decay, and spectral large-sieve/pretrace chains. KZ-E is not closed internally: block-centering identities and raw block-energy estimates have been refuted, leaving NC-BLK for actual WFD coefficients or an external DI/BFI original dispersion theorem.

```text
A1 clean KLS input
  => SC-9 Kuznetsov-LS atom;
SC-9
  => KZ-A + KZ-B + KZ-C + KZ-D + KZ-E;
KZ-A--KZ-D
  => already routed by existing self-contained spines;
KZ-E
  => NC-BLK actual block non-concentration
  or external DI/BFI original dispersion.
```

## 2. 汇总

- `a1_clean_input_status=a1_clean_kls_external_input_registered_self_contained_atom_open`。
- `a1_external_kls_input_registered=True`。
- `all_sc9_subatoms_routed=True`。
- `terminal_gap_after_router=NCBLKOrExternalDIBFIOriginalDispersion`。
- `self_contained_version_status=open_at_ncblk_actual_block_nonconcentration`。
- `external_deep_theorem_version_status=closed_for_a1_clean_branch_if_original_di_bfi_dispersion_or_equivalent_windowed_kls_is_accepted`。

## 3. SC-9 子原子

| subatom | role | status | remaining |
| --- | --- | --- | --- |
| `KZ-A` | Kloosterman modulus smoothing and L2 bookkeeping | `closed_elementary_smoothing` | none |
| `KZ-B` | Kuznetsov trace formula specialization | `closed_by_trace_specialization_document` | none |
| `KZ-C` | Bessel transform window decay | `closed_by_bessel_decay_document` | none |
| `KZ-D` | spectral large sieve with oldform/Eisenstein bookkeeping | `closed_by_pretrace_kernel_chain` | none |
| `KZ-E` | well-factorable dispersion logarithmic saving | `reduced_to_ncblk_or_external_dibfi` | NC-BLK actual block non-concentration or external DI/BFI original dispersion |

## 4. KZ-E 阻断与剩余路线

| candidate | verdict | reason |
| --- | --- | --- |
| `BD-CEN identity` | `blocked` | h=0 frequency centering is not same-(u,v) block centering |
| `SOURCE-CEN identity` | `refuted` | it changes the current WFD target rather than rewriting it |
| `raw BLK-energy-core` | `false_for_arbitrary_coefficient_arrays` | single-block single-atom test defeats arbitrary log saving |
| `NC-BLK` | `remaining_internal_route` | must prove actual WFD coefficients are block-nonconcentrated |
| `external DI/BFI` | `remaining_external_route` | original dispersion theorem may supply the needed block variance subtraction |

## 5. 当前结论

A1 clean KLS 的自足版硬点现在不应再写成宽泛的 `SC-9`：

```text
self-contained route => prove NC-BLK for actual WFD coefficients；
external route        => cite DI/BFI original dispersion or equivalent windowed KLS theorem。
```

这一步仍不是最终无黑箱证明；它排除了块中心化伪恒等式和裸块能量伪路线，留下真实最窄硬点。
