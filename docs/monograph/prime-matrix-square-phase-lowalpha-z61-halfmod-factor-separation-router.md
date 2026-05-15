# Prime Matrix square-phase low-alpha z=61 half-mod factor separation

**状态：** `z61_half_modulus_flip_reduced_to_factor_separation_open`

half-modulus flip 的最近分离可在素因子上解释：`M/2=28842` 在 `37` 下为 `19`（最小代表 `-18`），在 `71` 下为 `16`。这两个非零因子残差经 CRT 合成后得到 `2572≡-55 mod 2627`，正是上一层最近 offset。因此 exact collision 已由两个因子非零排除；全局剩余是证明这种 CRT 合成不会持久贴近 0，或登记 Factor-PDEC。

```text
half_modulus=28842
q4_half_residue=19
q2_half_residue=16
combined_signed_residue=-55
combined_circular_margin=55
halfmod_factor_separation_closed_for_formal_unit=true
row_column_unconditional_closed=false
```

## 1. 因子分离

| factor | residue of M/2 | signed residue | nonzero |
| ---: | ---: | ---: | --- |
| 37 | 19 | -18 | true |
| 71 | 16 | 16 | true |

## 2. CRT 合成

| modulus | CRT residue | signed residue | circular margin |
| ---: | ---: | ---: | ---: |
| 2627 | 2572 | -55 | 55 |

## 3. 自足小引理

若 half-modulus flip 造成 exact collision，则必须有

```text
M/2 ≡ 0 (mod 37) and M/2 ≡ 0 (mod 71).
```

当前两个因子残差分别为 `19` 与 `16`，所以 exact collision 被排除。最近余量 `55` 是这两个非零残差的 CRT 合成结果。

## 4. 证明边界

- 已闭合：当前 z=61 formal unit 的 half flip exact collision 被因子非零排除，且 CRT 合成恢复 offset `-55`。
- 未闭合：全局 CRT 合成分离下界，或 Factor-PDEC 排斥。
- 下一目标：`HalfModulusFlipFactorSeparationGlobalBoundOrFactorPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-offset55-halfmod-flip-router.json` | `b46ab34b1d1ca71dabb016823809049e3fb2e7546798cfc6c8457b31977c2871` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_halfmod_factor_separation_router.py` | `01ddebcbcb907b17ad07cdf5db1b64d5427c920031e4ab519fe1d3c5499379fe` |
