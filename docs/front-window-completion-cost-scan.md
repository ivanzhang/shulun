# 前窗口残洞核完整消除代价扫描

**状态：** `front_hole_killing_constraints_need_completion_cost_not_only_local_patch_cost`

残洞核可被局部 CRT 约束以很小相位补掉，但一旦要求补洞约束同时延拓为完整零行，最早完成相位在样本中回到首个完整覆盖相位，并全部位于 x>=P。这支持‘前窗口残洞核的真正消除代价是全局相位跨越’。

## 摘要
- P=13 front_min_holes=1 first_full_x=168
  - front_x=9 holes=[10] assignments=5 min_forced_x=0 first_full_patch={'x': 168}
- P=17 front_min_holes=1 first_full_x=1210
  - front_x=12 holes=[7] assignments=6 min_forced_x=0 first_full_patch={'x': 1210}
- P=19 front_min_holes=1 first_full_x=3658
  - front_x=15 holes=[8] assignments=7 min_forced_x=0 first_full_patch={'x': 3658}
- P=23 front_min_holes=2 first_full_x=58
  - front_x=14 holes=[9, 15] assignments=58 min_forced_x=0 first_full_patch={'x': 58}
- P=29 front_min_holes=3 first_full_x=5209
  - front_x=11 holes=[12, 18, 28] assignments=545 min_forced_x=0 first_full_patch=None
  - front_x=18 holes=[1, 19, 25] assignments=554 min_forced_x=1 first_full_patch={'x': 5209}
  - front_x=24 holes=[5, 13, 23] assignments=545 min_forced_x=0 first_full_patch={'x': 5209}
- P=31 front_min_holes=2 first_full_x=60794
  - front_x=25 holes=[12, 22] assignments=92 min_forced_x=0 first_full_patch={'x': 60794}

## 下一证明义务
- 把 forced_scheme 的等差枚举改写为理论命题：局部补洞约束必须兼容全部列覆盖。
- 证明若 forced_scheme 在 x<P 内补掉最终残洞，则必产生新的未覆盖列，形成残洞迁移守恒。
- 把残洞迁移守恒与 FSC: min full x >= P 连接，形成非有限模板的势垒不等式。
