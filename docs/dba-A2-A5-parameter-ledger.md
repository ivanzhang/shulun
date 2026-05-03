# DBA-A2/A5 高度传播与参数吸收账本

**状态：** `A2_standard_height_closed_conditionally_on_fixed_degree_atlas; A5_numeric_inequalities_pass`

## 参数
- `B=20`
- `C_*=160`
- `B1=960`
- `B2=880`
- `B4=820`
- `B5_min=103`

## A2 高度传播规则
- `addition_multiplication_substitution`：次数 `O_r(1)`；高度 `P^{O_r(1)}`；状态 `standard_closed`
- `derivative`：次数 `d -> d-1`；高度 `H(P') <= d H(P)`；状态 `standard_closed`
- `univariate_resultant_discriminant`：次数 `O(d^2)`；高度 `H(Res(P,Q)) <= (2d)^{O(d)} H(P)^{O(d)} H(Q)^{O(d)}`；状态 `standard_closed_for_fixed_d`
- `multivariate_elimination_resultant`：次数 `D^{O_n(1)} for fixed variable count n`；高度 `H <= (C D)^{O_n(D^n)} prod_i H_i^{O_n(D^n)}; fixed D,n gives P^{O_r(1)}`；状态 `closed_if_fixed_variable_count_and_degree_are_explicitly_recorded`
- `integer_factor_resonance`：次数 `linear factors only`；高度 `<= P^{O(1)}`；状态 `standard_closed_plus_step_average`

## A5 参数不等式
| 名称 | 左边 | 右边 | 余量 |
|---|---:|---:|---:|
| thickness_delta | 960 | 190 | 770 |
| small_root_density | 880 | 220 | 660 |
| step_frequency_T | 820 | 220 | 600 |
| KS_margin_B1 | 960 | 740 | 220 |
| KS_margin_B2 | 880 | 740 | 140 |
| Stieltjes_B5_min | 103 | 103 | 0 |

## 剩余显式化义务
- 在论文正文或附录中记录每个 atlas 项的变量数 n 和次数 D 的固定上界符号 d_i(r)。
- 对 multivariate_elimination_resultant 引用标准 Macaulay/resultant 高度界，说明 fixed n,D 下为 P^{O_r(1)}。
- 对 rank_failure_high_dimensional_factor 说明若非零多项式低 rank，则进入系数/resultant atlas，而非正常层。

## 解释
With B=20 and C_star=160, B1=960, B2=880, B4=820. The Kloosterman margins are positive; parameter absorption is no longer the main structural blocker once A1/A2 explicitness is accepted.
