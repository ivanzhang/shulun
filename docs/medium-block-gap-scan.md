# C sqrt(P) 中块补洞缺口扫描

**状态：** `larger_blocks_reduce_full_patch_blocks_but_tail_blocks_need_care`

增大到 C sqrt(P) 后满补块减少；但末端短块会干扰最小值。可证路线应使用滑动中块或整行累计缺口，而非固定分块逐块命题。

## 摘要
- P=809：C=1 max_patch=1.000 full_blocks=10; C=2 max_patch=0.889 full_blocks=0; C=3 max_patch=0.857 full_blocks=0; C=4 max_patch=0.833 full_blocks=0; C=5 max_patch=0.727 full_blocks=0; C=8 max_patch=0.730 full_blocks=0; C=10 max_patch=0.634 full_blocks=0
- P=1601：C=1 max_patch=1.000 full_blocks=5; C=2 max_patch=0.923 full_blocks=0; C=3 max_patch=0.714 full_blocks=0; C=4 max_patch=0.739 full_blocks=0; C=5 max_patch=0.688 full_blocks=0; C=8 max_patch=0.604 full_blocks=0; C=10 max_patch=0.617 full_blocks=0
- P=3203：C=1 max_patch=1.000 full_blocks=1; C=2 max_patch=0.800 full_blocks=0; C=3 max_patch=1.000 full_blocks=1; C=4 max_patch=0.679 full_blocks=0; C=5 max_patch=0.667 full_blocks=0; C=8 max_patch=0.667 full_blocks=0; C=10 max_patch=0.643 full_blocks=0
- P=6421：C=1 max_patch=0.909 full_blocks=0; C=2 max_patch=0.810 full_blocks=0; C=3 max_patch=0.767 full_blocks=0; C=4 max_patch=0.703 full_blocks=0; C=5 max_patch=0.729 full_blocks=0; C=8 max_patch=0.667 full_blocks=0; C=10 max_patch=0.667 full_blocks=0
- P=12809：C=1 max_patch=0.929 full_blocks=0; C=2 max_patch=0.786 full_blocks=0; C=3 max_patch=0.703 full_blocks=0; C=4 max_patch=0.717 full_blocks=0; C=5 max_patch=0.656 full_blocks=0; C=8 max_patch=0.667 full_blocks=0; C=10 max_patch=0.614 full_blocks=0

## 下一证明义务
- 改用滑动窗口而非固定尾块。
- 证明满补中块不能连续覆盖整行。
- 将连续满补块转化为 CRT 短周期或大因子乘积矛盾。
