# Prime Matrix square-phase low-alpha z=61 gap-3 CRT structure

**状态：** `z61_halfmod_factor_separation_reduced_to_gap3_crt_structure_open`

half-modulus flip 的 CRT 小余量可进一步解释为 gap-3 结构：`q2=71=2*37-3`，而 `M/2` 的因子残差为 `a=19 mod37`、`b=16 mod71`，满足 `a-b=3`。因此 CRT 解无需一般合成，直接是 `a-2*q4=19-74=-55`。这说明最近余量来自 q2 与 2q4 的 gap-3 因子关系和半模残差差值同步，而非任意 CRT 偶合。

```text
q2_equals_2q4_minus_3=true
half_residue_gap_a_minus_b=3
gap_matches_q_relation_gap=true
structural_signed_crt=-55
gap3_crt_structure_closed_for_formal_unit=true
row_column_unconditional_closed=false
```

## 1. Gap-3 数据

| q4 | q2 | 2q4-q2 | a=M/2 mod q4 | b=M/2 mod q2 | a-b |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 37 | 71 | 3 | 19 | 16 | 3 |

## 2. M 残差来源

| modulus | M residue | half residue | expected |
| ---: | ---: | ---: | ---: |
| 37 | 1 | 19 | 19 |
| 71 | 32 | 16 | 16 |

## 3. 结构 CRT

由 `q2=2q4-3` 可得 `2q4≡3 (mod q2)`。若 `a-b=3`，则

```text
x = a-2q4
x ≡ a (mod q4),
x ≡ a-2q4 ≡ a-3 = b (mod q2).
```

所以 `x=19-74=-55`，即当前最近 offset。

## 4. 证明边界

- 已闭合：当前 z=61 formal unit 的 `-55` 来自 gap-3 CRT 结构。
- 未闭合：全局排斥 gap-3 型持续贴边，或登记 Gap-PDEC。
- 下一目标：`GapThreeCRTStructureGlobalBoundOrGapPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-halfmod-factor-separation-router.json` | `bb92909f03c1a3f23cb67e6ea78733b26b3452627aaeef0a1884dafe0d00c338` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_gap3_crt_structure_router.py` | `6ffdb3a6d336a821bffe21c4007b04c1b753d4fb50ab6b3a838516024283b457` |
