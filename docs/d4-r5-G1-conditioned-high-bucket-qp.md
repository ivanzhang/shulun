# D4/R5 G1 条件化高桶补偿 QP 分族审计

**状态：** `conditioned_high_bucket_compensation_tested_remaining_failures_identified`

按高桶是否非空进行 A/B/C 条件化 QP 后，可以精确看到哪些分族仍未闭合。若条件化高桶补偿仍失败，则下一步不应继续盲目加全局斜率，而应对失败分族反解最小补偿常数。

## 全体失败计数
- `conditioned_strong`：`20`

## 分族失败计数
- `B_tau_33_59`：{'count': 13, 'failure_counts': {'conditioned_strong': 13}}
- `C_heavy_short`：{'count': 7, 'failure_counts': {'conditioned_strong': 7}}

## 下一证明义务
- 查看 conditioned_strong 的失败分族，并只对失败分族反解 lambda。
- 对 A_no_high 反解所需 d4/d3；对 B 反解所需 d5/d4；对 C 反解所需 d6/d5 或 d6/d4。
- 把反解常数与实际数据下界比较，选择可证明且不过强的有理常数。
