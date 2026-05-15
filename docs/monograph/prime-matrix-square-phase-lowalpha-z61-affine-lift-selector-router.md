# Prime Matrix square-phase low-alpha z=61 affine lift selector

**状态：** `z61_prime_factor_lifts_reduced_to_affine_root_selector_open`

素因子提升门可完全消去大平方：一级根 `r` 满足 `r^2+delta=M*k0`，而固定商 `h=floor(p/M)` 后，`K=(p^2+delta)/M` 等于 `k0+2hr+h^2M`。样本中所有候选根都有同一 `h=3`，`K mod 37` 与 `K+74 mod 71` 两个仿射门各自唯一选中 `r=26951`。因此最新硬点从提升同余进一步收窄为一级 CRT 根上的仿射选择器容量界，或登记 AffineLift-PDEC。

```text
affine_lift_selector_group_count=1
all_affine_lift_selectors_closed=true
affine_root_lift_selector_global_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 仿射门摘要

| M | h values | roots | q4 pass | q2 pass | combined pass | selected | closed |
| ---: | --- | ---: | --- | --- | --- | ---: | --- |
| 57684 | `[3]` | 32 | `[26951]` | `[26951]` | `[26951]` | 26951 | true |

## 2. 素数候选的仿射残差

| root | p | k0 | K | K mod 37 | K+74 mod 71 | combined | prime p | full source |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1891 | 174943 | 62 | 530564 | 21 | 55 | 2611 | true | false |
| 3961 | 177013 | 272 | 543194 | 34 | 47 | 2106 | true | false |
| 8009 | 181061 | 1112 | 568322 | 2 | 41 | 964 | true | false |
| 11219 | 184271 | 2182 | 588652 | 19 | 65 | 278 | true | false |
| 11771 | 184823 | 2402 | 592184 | 36 | 47 | 1183 | true | false |
| 24881 | 197933 | 10732 | 679174 | 2 | 62 | 1482 | true | false |
| 26951 | 200003 | 12592 | 693454 | 0 | 0 | 0 | true | true |
| 34495 | 207547 | 20628 | 746754 | 20 | 50 | 760 | true | false |
| 46465 | 219517 | 37428 | 835374 | 25 | 62 | 62 | true | false |

## 3. 自足小引理

若 `p=hM+r` 且 `r^2+delta=M*k0`，则

```text
(p^2+delta)/M = k0 + 2*h*r + h^2*M.
```

所以 `K mod q4` 与 `K+2q4 mod q2` 都是一级根 `r` 上的仿射选择条件，无需再处理大平方或大提升模数。

## 4. 证明边界

- 已闭合：样本 q2/q4 提升门等价于一级根上的两个仿射门，且二者各自唯一选中同一根。
- 未闭合：全局仿射根选择器容量界，或 AffineLift-PDEC 排斥。
- 下一目标：`AffineRootLiftSelectorGlobalBoundOrAffineLiftPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-quotient-factor-lift-router.json` | `13e9c08af07e9334f12512d78c5f75889a0e4b17fb1669d15f308044a28d4502` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_affine_lift_selector_router.py` | `475ad767f2c1a33fc176cf559354d48e937f75629648cfd76791d59acc296610` |
