# Prime Matrix square-phase low-alpha z=61 core factor residue identity

**状态：** `z61_half_residue_gap_source_reduced_to_core_factor_identities_open`

`M` 的两个残差源来自核心 `C=11*19*23` 的两个小同余身份：`37=2*19-1` 使 `2C≡11*23≡-6 (mod37)`，故 `C≡-3`、`12C≡1`；`71=3*23+2` 且 `11*19≡-4 (mod71)`，故 `3C≡8`、`12C≡32=37-5`。

```text
q4_anchor_gap_2f19_minus_q4=1
q4_pair_11_23_signed=-6
core_mod_q4_signed=-3
twelve_core_mod_q4=1
q2_anchor_gap_q2_minus_3f23=2
q2_pair_11_19_signed=-4
core_mod_q2_signed=-21
twelve_core_mod_q2=32
core_factor_residue_identity_closed_for_formal_unit=true
row_column_unconditional_closed=false
```

## 1. q4 侧身份

| identity | value | consequence |
| --- | ---: | --- |
| `q4=2*19-1` | 1 | `2*19≡1 (mod37)` |
| `11*23 mod37` | 31 | signed `-6` |
| `2C mod37` | 31 | signed `-6` |
| `C mod37` | 34 | signed `-3` |
| `12C mod37` | 1 | gives `M≡1` |

## 2. q2 侧身份

| identity | value | consequence |
| --- | ---: | --- |
| `q2=3*23+2` | 2 | `3*23≡-2 (mod71)` |
| `11*19 mod71` | 67 | signed `-4` |
| `3C mod71` | 8 | signed `8` |
| `C mod71` | 50 | signed `-21` |
| `12C mod71` | 32 | gives `M≡37-5` |

## 3. 证明边界

- 已闭合：`M` 的两个残差源已经拆为 `C` 的核心因子同余身份。
- 未闭合：全局排斥这种核心因子身份模板持续导致贴边，或登记 CoreFactor-PDEC。
- 下一目标：`CoreFactorResidueIdentityGlobalBoundOrCoreFactorPDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-half-residue-gap-source-router.json` | `fa55b234b083c663516a43dff536d84fb66ad93d9ebbaf6e4109dc9d77b1288a` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_core_factor_residue_identity_router.py` | `0549cb71946ffed2ebe8af2ecb506f1eb42c92b9f27045ef6487bbfd478554cc` |
