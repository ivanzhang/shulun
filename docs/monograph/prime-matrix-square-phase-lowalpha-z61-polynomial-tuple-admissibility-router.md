# Prime Matrix square-phase low-alpha z=61 polynomial tuple admissibility

**状态：** `z61_polynomial_prime_tuple_admissible_but_requires_schinzel_level_input_open`

当前三元组 `p(t),a4(t),a2(t)` 已经精确可容许：三个多项式均为 primitive，`p(t)` 线性不可约，两个二次多项式判别式非平方，因此在 Z 上不可约；乘积多项式 degree=5 且 content=1。若存在固定素因子，除非素数不超过 degree，否则非零多项式模该素数不可能在所有剩余类上为零；检查 2,3,5 均有幸存类。所以局部障碍路线关闭。剩余正是 Schinzel Hypothesis H / Bateman-Horn 等级的多项式素性输入，或 PersistentPhase-PDEC 排斥。

```text
product_degree=5
product_content=1
no_fixed_prime_divisor_proved=true
exact_admissibility_closed=true
schinzel_hypothesis_h_level_input_proved=false
row_column_unconditional_closed=false
```

## 1. 多项式验收

| polynomial | degree | content | discriminant | irreducible |
| --- | ---: | ---: | ---: | --- |
| `p(t)` | 1 | 1 | None | true |
| `a4(t)` | 2 | 1 | -10626428 | true |
| `a2(t)` | 2 | 1 | -3802074416 | true |

## 2. 固定素因子

| prime | surviving residues | fixed divisor |
| ---: | --- | --- |
| 2 | `[0, 1]` | false |
| 3 | `[0, 1]` | false |
| 5 | `[0, 4]` | false |

## 3. 精确引理

令 `F(t)=p(t)a4(t)a2(t)`，`deg F=5` 且 `content(F)=1`。若某素数 `ell>5` 对所有整数 `t` 都整除 `F(t)`，则 `F mod ell` 作为非零次数至多 5 的多项式会在 `ell>5` 个剩余类上全为零，矛盾。因此只需检查 `ell<=5`；`2,3,5` 均有幸存剩余类，所以没有固定素因子。

## 4. 证明边界

- 已闭合：primitive、不可约、无固定素因子，即精确可容许性。
- 未闭合：可容许多项式三元组是否取同步素值；这是 Schinzel/Bateman-Horn 等级输入。
- 结论：不能从可容许性推出无条件全局 companion。
- 下一目标：`SchinzelHypothesisHLevelInputOrPersistentPhasePDECExclusion`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-quadratic-prime-triple-param-router.json` | `cd9ca8bbd7c90b9bbf51bc802b5bf5716929247a6b9d718b9784c5206d95233e` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_polynomial_tuple_admissibility_router.py` | `da3a924e7a2e99a0b4acc7954d2752a4f60c33198a9886c669649f9e1502d1cb` |
