# Prime Matrix square-phase low-alpha z=61 half-residue gap source

**状态：** `z61_gap3_crt_structure_reduced_to_half_residue_gap_source_open`

gap-3 CRT 的差值 `a-b=3` 可继续上提为半模残差源模板：`M≡1 (mod 37)` 强制 `M/2≡(37+1)/2=19`，`M≡37-5=32 (mod 71)` 强制 `M/2≡(37-5)/2=16`。因此 `19-16=3`，并继续给出 `19-2*37=-55`。

```text
modulus_equals_12_core=true
q2_equals_2q4_minus_3=true
m_mod_q4_source_closed=true
m_mod_q2_source_closed=true
half_residue_gap_from_source=3
structural_signed_crt_from_source=-55
gap_source_closed_for_formal_unit=true
row_column_unconditional_closed=false
```

## 1. 上游因子源

| M | factorization | core | core factorization |
| ---: | --- | ---: | --- |
| 57684 | `[2, 2, 3, 11, 19, 23]` | 4807 | `[11, 19, 23]` |

这里 `M=12C`，`C=11*19*23`，与前序 common-core 证书中的核心一致。

## 2. 残差源模板

| modulus | M residue | source value | half residue | formula |
| ---: | ---: | ---: | ---: | ---: |
| 37 | 1 | 1 | 19 | 19 |
| 71 | 32 | 32 | 16 | 16 |

若同时有 `q2=2q4-3`、`M≡1 (mod q4)`、`M≡q4-5 (mod q2)`，则

```text
a = M/2 mod q4 = (q4+1)/2,
b = M/2 mod q2 = (q4-5)/2,
a-b = 3,
x = a-2q4.
```

在当前 formal unit 中，`x=19-74=-55`。

## 3. 证明边界

- 已闭合：`-55` 的来源从 gap-3 CRT 进一步上提到 `M` 的两个残差源。
- 未闭合：全局证明这种残差源模板不能形成持续贴边，或登记并排斥 GapSource-PDEC。
- 下一目标：`HalfResidueGapSourceGlobalBoundOrGapSourcePDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-gap3-crt-structure-router.json` | `b3f4dcecab52175d2c003ce4ccac3c4c611318a88add2c5d593a440d98fda2d1` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_half_residue_gap_source_router.py` | `0b47dd581377ec0218ef2b6ab65953cc784d744640fa244f266ae1c1939cc610` |
