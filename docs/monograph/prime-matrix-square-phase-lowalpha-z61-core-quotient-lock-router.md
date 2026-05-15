# Prime Matrix square-phase low-alpha z=61 core quotient lock

**状态：** `z61_core_factor_residue_identities_reduced_to_unique_quotient_lock_open`

核心因子残差身份可压成两个精确商锁：`a*c+6=7*(2*b-1)` 与 `a*b+4=3*(3*c+2)`。消去 `c` 得 `b=(2a-117)/(a^2-126)`；正整数解被符号区间和 `a<=11` 的有限检查压成唯一解 `(a,b,c)=(11,19,23)`，从而 `q4=37,q2=71`。

```text
q4_exact_quotient_lock_closed=true
q2_exact_quotient_lock_closed=true
eliminated_b_formula=b=(2*a-117)/(a^2-126)
positive_integer_solution_unique_in_scan=true
quotient_lock_unique_positive_integer_solution_proved=true
row_column_unconditional_closed=false
```

## 1. 精确商锁

| side | equation | quotient | closed |
| --- | --- | ---: | --- |
| q4 | `a*c+6=7*(2*b-1)` | 7 | true |
| q2 | `a*b+4=3*(3*c+2)` | 3 | true |

## 2. 消元

设 `q4=2b-1`、`q2=3c+2`，两个商锁为：

```text
ac+6=7(2b-1),
ab+4=3(3c+2).
```

第二式给 `c=(ab-2)/9`。代回第一式得：

```text
b(a^2-126)=2a-117,
b=(2a-117)/(a^2-126).
```

12<=a<=58 gives numerator<0<denominator; a>=59 gives 0<(2a-117)/(a^2-126)<1; therefore only a<=11 needs finite checking.

## 3. 小 a 有限检查

| a | b formula | positive integer |
| ---: | ---: | --- |
| 1 | `23/25` | false |
| 2 | `113/122` | false |
| 3 | `37/39` | false |
| 4 | `109/110` | false |
| 5 | `107/101` | false |
| 6 | `7/6` | false |
| 7 | `103/77` | false |
| 8 | `101/62` | false |
| 9 | `11/5` | false |
| 10 | `97/26` | false |
| 11 | `19` | true |

## 4. 正整数解

| a | b | c | q4 | q2 |
| ---: | ---: | ---: | ---: | ---: |
| 11 | 19 | 23 | 37 | 71 |

## 5. 证明边界

- 已闭合：同一精确商锁模板下，正整数解唯一，必为 `11,19,23`。
- 未闭合：全局排斥该唯一商锁模板作为反例贴边源，或登记并排斥 QuotientLock-PDEC。
- 下一目标：`CoreQuotientLockGlobalExclusionOrQuotientLockPDEC`。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-core-factor-residue-identity-router.json` | `fca0924568678b13e471b25fa9bb90ee495cc642de76e23dfeec9d52689151f7` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_core_quotient_lock_router.py` | `e39ce6dc85c75462824ad8c030c30d4b61f497c200ef8fdfd77c1106df8965fe` |
