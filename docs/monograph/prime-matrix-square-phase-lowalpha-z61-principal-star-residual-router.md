# Prime Matrix square-phase low-alpha z=61 主星形残量路由

**状态：** `z61_principal_star_reduces_to_two_secondary_residual_buckets_open`

z=61 的 profile 信用已分离为主星形 `83561->*` 与次级残量。样本中主星形单独覆盖 balanced/far 两个 bucket，剩余只在 mid<=4 与 unbalanced<=8 两个 bucket 出现；因此下一步无需再处理全部 pair，只需证明这两个残量口的次级 pair 信用下界，或登记 Residual-PDEC。

```text
principal_positive_p=83561
principal_star_residual_identity_closed=true
principal_star_covers_bucket_count=2
residual_bucket_count=2
secondary_credit_covers_all_residuals_in_sample=true
principal_star_lower_bound_proved=false
secondary_residual_credit_bound_proved=false
row_column_unconditional_closed=false
```

## 1. bucket 主星形/残量

| bucket | need | principal star | residual need | secondary | secondary surplus | star covers |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `balanced<=2` | 0.226278 | 0.241506 | 0.000000 | 0.029031 | 0.029031 | true |
| `mid<=4` | 0.181224 | 0.138944 | 0.042281 | 0.081573 | 0.039293 | false |
| `unbalanced<=8` | 0.209925 | 0.172725 | 0.037200 | 0.053785 | 0.016585 | false |
| `far>8` | 0.051076 | 0.120970 | 0.000000 | 0.036441 | 0.036441 | true |

## 2. 残量 bucket 的次级覆盖

| bucket | residual need | secondary surplus | cover pairs | pair list |
| --- | ---: | ---: | ---: | --- |
| `mid<=4` | 0.042281 | 0.039293 | 1 | `200003->36739:0.053280` |
| `unbalanced<=8` | 0.037200 | 0.016585 | 3 | `36739->200003:0.020224, 200003->36739:0.013964, 200003->10007:0.005191` |

## 3. 主星形 pair

| bucket | pair | credit/bucket abs | cells | top3 share |
| --- | --- | ---: | ---: | ---: |
| `balanced<=2` | `83561->200003` | 0.143733 | 8 | 0.807729 |
| `balanced<=2` | `83561->36739` | 0.080227 | 10 | 0.545949 |
| `balanced<=2` | `83561->10007` | 0.017546 | 6 | 0.836954 |
| `mid<=4` | `83561->200003` | 0.068517 | 5 | 0.796573 |
| `mid<=4` | `83561->36739` | 0.055282 | 8 | 0.819595 |
| `mid<=4` | `83561->10007` | 0.015145 | 9 | 0.746074 |
| `unbalanced<=8` | `83561->200003` | 0.090805 | 4 | 0.851359 |
| `unbalanced<=8` | `83561->36739` | 0.053273 | 7 | 0.742059 |
| `unbalanced<=8` | `83561->10007` | 0.028647 | 6 | 0.777434 |
| `far>8` | `83561->36739` | 0.078489 | 8 | 0.831538 |
| `far>8` | `83561->200003` | 0.029662 | 3 | 1.000000 |
| `far>8` | `83561->10007` | 0.012819 | 5 | 0.908655 |

## 4. 证明边界

- 已闭合：pair 信用分解为主星形与次级残量的恒等式。
- 已压缩：主星形单独闭合 `balanced<=2` 与 `far>8`。
- 剩余：`mid<=4` 与 `unbalanced<=8` 的次级残量信用下界。
- 下一目标：`SecondaryPairResidualCreditForMidUnbalancedOrResidualPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-profile-pair-credit-router.json` | `a39098dbe0a99b79259bc828641a2de7c7e6596bea21ea553e44f2088f9a9770` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-profile-pair-phase-cooccurrence-router.json` | `939645f0708e01e6e1d16871aa1545c15ea15ade125244c5bade78a4196f07b4` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-profile-pair-support-router.json` | `130434e1af6983603b965fc0185055ecd897f538e76e9e59d2d0e024d8955dc9` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_principal_star_residual_router.py` | `fcb7273166d295f90ad17fc6e476fee0a57fbc7bb1f3a0269ce0ddfe66064d6d` |
