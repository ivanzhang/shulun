# Prime Matrix square-phase low-alpha z=61 offset-55 half-modulus flip

**状态：** `z61_offset55_collision_reduced_to_half_modulus_flip_open`

最近 offset-55 碰撞族可继续压缩：三条最近原子其实是同一完整替代路径 `+++--` 在不同剥离深度的投影。它与选中路径 `++---` 只差第三个符号，即翻转系数 `14421=M/4`；两条完整 signed-sum 的差为 `2*14421=M/2=28842`。模 `2627=37*71` 下 `M/2≡-55`，所以 offset-55 的来源是 2-adic half-modulus flip，不是独立随机碰撞。全局剩余变成 half-modulus flip 分离下界，或 HalfFlip-PDEC。

```text
selected_peel_sign_word=++---
alternative_peel_sign_word=+++--
single_flip_position=3
single_flip_coefficient=14421
flip_delta=28842
signed_separation_mod_target=-55
separation_circular_margin=55
offset55_halfmod_flip_closed_for_formal_unit=true
row_column_unconditional_closed=false
```

## 1. 两条完整路径

| path | sign word | signed sum | mod 2627 |
| --- | --- | ---: | ---: |
| selected | `++---` | 373055 | 21 |
| nearest alternative | `+++--` | 401897 | 2593 |

## 2. 最近原子重构

| step | prefix | branch | suffix | full word | full sum mod 2627 | atom offset |
| ---: | --- | --- | --- | --- | ---: | ---: |
| 1 | `` | `+` | `++--` | `+++--` | 2593 | -55 |
| 2 | `+` | `+` | `+--` | `+++--` | 2593 | -55 |
| 3 | `++` | `+` | `--` | `+++--` | 2593 | -55 |

## 3. 结构恒等式

最近替代路径与选中路径只差第三个符号，因此

```text
S(++ + --) - S(++ - --) = 2*14421 = 28842 = M/2.
M/2 mod (37*71) = -55.
```

由于 `gcd(M/2,37*71)=1`，精确重合不发生；但最小环距离为 `55`，这就是当前 formal unit 的最近 Margin-PDEC 来源。

## 4. 证明边界

- 已闭合：当前 z=61 formal unit 的 offset-55 最近碰撞全部来自同一个 half-modulus flip。
- 未闭合：全局 half-modulus flip 分离下界，或 HalfFlip-PDEC 排斥。
- 下一目标：`HalfModulusFlipSeparationGlobalBoundOrHalfFlipPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-branch-decision-ledger-router.json` | `727ffcb802fd6a005bb546bd7708d1fafafe332f96a703cfcfb65753714d8d28` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-nearest-margin-collision-router.json` | `3921407feb8f169db2f169b990378889f5302328e66e1d3f4cd9e735bff2ceec` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-signed-sum-residue-gate-router.json` | `000bb6e26dec4b78c4215118876df470f40659f120db560c9bee5cf6a80fd0c7` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_offset55_halfmod_flip_router.py` | `f1f4b29e7ec218b5045a6f3907bdc1d28f80b441354bfcf521e1673c9be22171` |
