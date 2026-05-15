# Prime Matrix square-phase low-alpha z=61 shifted-square-window algebraic normal form

**状态：** `z61_shifted_square_window_companion_reduced_to_quadratic_prime_triple_open`

shifted-square-window companion 可化为单一平方进位正规形：`p^2=A*s-C`，其中 `A=2*M*q2*q4=303071736`、`C=delta+2*M*q4=4269143`。当前样本为 `s=132`、`p=200003`，并附加三个素性条件 `p`、`71s-1`、`74s-1` 为素数。因此剩余不是普通短区间素数命题，而是二次剩余类上的三重素性输入，或命名 PersistentPhase-PDEC 排斥。

```text
A=303071736
C=4269143
selected_s=132
selected_p=200003
p^2=A*s-C -> True
crt_root_class_count_mod_A=256
quadratic_residue_class_prime_triple_input_proved=false
row_column_unconditional_closed=false
```

## 1. 正规形

| field | value |
| --- | --- |
| equation | `p^2 = A*s - C` |
| A | `303071736` |
| C | `4269143` |
| selected square | `200003^2 = 40001200009` |
| recovered s | `132` |
| a4, a2 | `9371, 9767` |

## 2. 模 A 平方根

| modulus | target | root count | selected residue | selected is root |
| ---: | ---: | ---: | ---: | --- |
| 8 | 1 | 4 | 3 | true |
| 3 | 1 | 2 | 2 | true |
| 11 | 1 | 2 | 1 | true |
| 19 | 5 | 2 | 9 | true |
| 23 | 2 | 2 | 18 | true |
| 37 | 28 | 2 | 18 | true |
| 71 | 16 | 2 | 67 | true |

## 3. 素性条件

| condition | value |
| --- | --- |
| p | `200003` |
| a4=71s-1 | `9371` |
| a2=74s-1 | `9767` |
| s | `132` |

## 4. 证明边界

- 已闭合：当前 companion 的代数正规形与 CRT 平方根分解。
- 未闭合：二次剩余类上的三重素性输入，或 PersistentPhase-PDEC 排斥。
- 结论：该输入强于普通短区间素数、单线性型 Dirichlet 或普通有界素数间隔。
- 下一目标：`QuadraticResidueClassPrimeTripleInputOrPersistentPhasePDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-endpoint-shifted-factor-router.json` | `57d4e18eadd1bb072db598f782533b7ecefc942472cc8f26d9f0a285e97ad40e` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-shifted-square-window-input-mismatch-router.json` | `655b151d11f502fcc820f82d40809a6451611b284989cd4921c5fbb6bfb71495` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-shifted-square-window-router.json` | `26ed4354b18ce54dc2ea66ce943e628fc02f80cacee97084cc3331a15cd17b83` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_shifted_square_window_algebraic_normal_form_router.py` | `e41a1ef574703efbb9b3f0c7abd102cc4c12b2727d56c24b7992d285447356c5` |
