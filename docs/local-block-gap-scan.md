# sqrt(P) 短块补洞缺口扫描

**状态：** `sqrt_blocks_still_have_unpatched_points_in_samples`

按 sqrt(P) 分块后，每个被扫描行的短块仍出现未补洞点。这支持把全局缺口降维为局部块引理：在长度约 sqrt(P) 的块中，大因子互斥无法填满小筛洞。

## 摘要
- P=401 Y=20 max_block_patch=1.000 min_block_unpatched=0
- P=809 Y=28 max_block_patch=1.000 min_block_unpatched=0
- P=1601 Y=40 max_block_patch=1.000 min_block_unpatched=0
- P=3203 Y=56 max_block_patch=1.000 min_block_unpatched=0
- P=6421 Y=80 max_block_patch=0.909 min_block_unpatched=1

## 下一证明义务
- 形式化短块内共享大因子的互斥：同一大因子在长度 sqrt(P) 块中至多出现一次。
- 估计短块小筛洞数下界。
- 估计短块可用不同大因子命中数上界，并证明小于洞数。
