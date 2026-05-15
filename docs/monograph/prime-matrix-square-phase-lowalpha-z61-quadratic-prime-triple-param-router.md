# Prime Matrix square-phase low-alpha z=61 quadratic prime triple parameterization

**状态：** `z61_quadratic_prime_triple_reduced_to_polynomial_prime_tuple_input_open`

选择平方根类 `p≡200003 (mod A)` 后，companion 输入变成单参数多项式素性三元组：`p(t)=A t+200003`、`s(t)=A t^2+400006t+132`、`a4(t)=71s(t)-1`、`a2(t)=74s(t)-1`。小素数局部审计未发现覆盖性局部障碍，但这仍是多项式素数值输入，不是已证标准定理；必须作为新输入证明，或排斥 PersistentPhase-PDEC。

```text
sample_polynomial_recovery_closed=true
local_audit_prime_bound=199
no_local_obstruction_up_to_bound=true
polynomial_prime_tuple_input_proved=false
row_column_unconditional_closed=false
```

## 1. 单参数多项式

| polynomial | coefficients `[c2,c1,c0]` |
| --- | --- |
| `p(t)` | `[0, 303071736, 200003]` |
| `s(t)` | `[303071736, 400006, 132]` |
| `a4(t)=71s(t)-1` | `[21518093256, 28400426, 9371]` |
| `a2(t)=74s(t)-1` | `[22427308464, 29600444, 9767]` |

## 2. 局部障碍审计

| prime | surviving residues | first residues | obstruction |
| ---: | ---: | --- | --- |
| 2 | 2 | `[0, 1]` | false |
| 3 | 2 | `[0, 1]` | false |
| 5 | 2 | `[0, 4]` | false |
| 7 | 6 | `[0, 1, 2, 3, 5, 6]` | false |
| 11 | 9 | `[0, 1, 2, 3, 4, 5, 6, 7, 8]` | false |
| 13 | 10 | `[0, 1, 2, 3, 4, 5, 6, 7, 11, 12]` | false |
| 17 | 14 | `[0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 13]` | false |
| 19 | 17 | `[0, 1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 13]` | false |
| 23 | 21 | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]` | false |
| 29 | 26 | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]` | false |
| 31 | 30 | `[0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12]` | false |
| 37 | 36 | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]` | false |
| 41 | 40 | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]` | false |
| 43 | 42 | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]` | false |
| 47 | 44 | `[0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]` | false |
| 53 | 50 | `[0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12]` | false |
| 59 | 56 | `[0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]` | false |
| 61 | 56 | `[0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13]` | false |
| 67 | 64 | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]` | false |
| 71 | 70 | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]` | false |
| 73 | 70 | `[0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]` | false |
| 79 | 76 | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]` | false |
| 83 | 82 | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]` | false |
| 89 | 88 | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]` | false |
| 97 | 96 | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]` | false |
| 101 | 98 | `[0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12]` | false |
| 103 | 98 | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]` | false |
| 107 | 106 | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]` | false |
| 109 | 108 | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]` | false |
| 113 | 110 | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]` | false |

## 3. 证明边界

- 已闭合：选定 CRT 根类下的单参数多项式正规形。
- 已检查：小素数局部障碍未在审计范围内出现。
- 未闭合：证明该多项式素性三元组有全局 companion，或排斥 PersistentPhase-PDEC。
- 结论：这仍是强素性输入，不能作为已证事实调用。
- 下一目标：`PolynomialPrimeTupleInputOrPersistentPhasePDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-shifted-square-window-algebraic-normal-form-router.json` | `3106b08898673dceec88f43cb038db997802b0cf966bda9a04ef4f4675f01293` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_quadratic_prime_triple_param_router.py` | `6aa1d8dac7bfe23ec64775f70baeb5330138ef121d94d60634584d66e0c13d96` |
