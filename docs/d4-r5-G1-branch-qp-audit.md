# D4/R5 G1 low 分支严格 QP 审计

**状态：** `enhanced_l34_alone_not_sufficient_low_branch_needs_floor_or_second_enhancement`

严格 QP 显示：low<=3/5 分支已闭合；但把 d4/d3 增强到 8/5 若不显式使用 low>3/5 下界，仍不足以全域闭合。因此 low>3/5 分支的证明必须真正利用 low floor，而不能只添加一个全域增强斜率。下一步需扩展 QP 证书支持 low_sum>=3/5，并验证 floor + d4/d3>=8/5 是否闭合。

## 失败计数
- `base_ladder_low_le_3over5`：`0`
- `enhanced_l34_8over5_no_low_cap`：`20`
- `enhanced_l23_3over2_l34_8over5_low31over50`：`6`
- `strong_l12_8over5_l23_3over2_l34_8over5_no_cap`：`20`

## 下一证明义务
- 扩展严格 QP 主动集，加入 low_sum>=3/5 约束。
- 验证 low_sum>=3/5 与 d4/d3>=8/5、d2/d1>=3/2、d3/d2>=3/2 的组合。
- 若仍不足，加入 d2/d1>=8/5 或 d3/d2>=3/2+epsilon 的二选一增强。
