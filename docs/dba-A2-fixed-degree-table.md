# DBA-A2 固定变量数/次数表

**状态：** `A2_fixed_variable_degree_bounds_recorded`

Each n_i(r), D_i(r) depends only on r and not on P; hence all resultants have height P^{O_r(1)}.

| Atlas 项 | 变量数上界 | 次数上界 | 高度理由 |
|---|---:|---:|---|
| `denominator_pole` | `<= 2*r + 8` | `<= 4*r + 16` | 平移、乘积、代入；参数 U,m,t,h <= P^{O(1)} |
| `derivative_zero` | `<= 2*r + 8` | `<= 8*r + 32` | N'D-ND' 的次数至多 deg N + deg D - 1；高度由求导和乘法规则控制 |
| `ramification` | `<= 2*r + 9 including level parameter c` | `<= (8*r + 32)^2` | Disc_x(N-cD) 与 Res_x(N-cD,N'D-ND') 是一变量 resultant；固定次数下高度 P^{O_r(1)} |
| `four_point_rank_failure` | `<= 8*r + 16; KS four-point normal form uses <= 8 free u-coordinates plus fixed auxiliary inverse variables` | `<= 32*r + 128` | 四点清分母多项式由四个固定次数正规形相乘相加；rank 失效由系数集合或固定次数 gcd/resultant atlas 记录 |
| `jacobian_common_branch` | `<= 8*r + 16` | `<= (32*r + 128)^4` | E 与 J_i 的多变量消元；变量数和次数只依赖 r，Macaulay/resultant 高度界给 P^{O_r(1)} |
| `step_frequency_resonance` | `<= 6 parameters h,t,m,U,T,d` | `<= 3` | 线性或低次数整数因子；高度 <= P^{O(1)}，平均损失由 A3 处理 |
| `layering_endpoint_low_volume` | `not a DBA polynomial atlas item` | `not applicable` | A4 非多项式预算项；由 C_L/C_KS/低体积账本吸收，不进入 A2 高度传播 |

## 结论
所有 DBA 多项式 atlas 项的变量数和次数只依赖 `r`，因此标准 Macaulay/resultant 高度界给出 `P^{O_r(1)}`。`layering_endpoint_low_volume` 不是 DBA 多项式项，已由 A4 预算吸收。
