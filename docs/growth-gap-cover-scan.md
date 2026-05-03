# 增量覆盖增长缺口实验

**状态：** `small_sieve_holes_not_exhausted_by_large_prime_patch_in_samples`

按 sqrt(P) 分层后，大根基素数补洞数始终小于小筛洞数；剩余未补洞点正是行内素数。实验支持有效覆盖增量不足路线：全行覆盖必须要求 large_patch/small_holes=1，但样本远低于 1。

## 扫描摘要
- P=101：max_patch_ratio=0.5909, min_prime_gap_ratio=0.4091
- P=211：max_patch_ratio=0.6279, min_prime_gap_ratio=0.3488
- P=401：max_patch_ratio=0.5217, min_prime_gap_ratio=0.4783
- P=809：max_patch_ratio=0.5659, min_prime_gap_ratio=0.4341
- P=1601：max_patch_ratio=0.5336, min_prime_gap_ratio=0.4664
- P=3203：max_patch_ratio=0.5492, min_prime_gap_ratio=0.4485

## 下一证明义务
- 将 small_holes 估计为 P*prod_{q<=sqrt(P)}(1-1/q) 的显式下界。
- 将 large_patch 上界转化为 sqrt(P)-粗合数计数上界。
- 证明二者之间存在正缺口，得到每行至少一个素数。
