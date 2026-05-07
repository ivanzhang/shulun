# DPRC beta桶偏差包络扫描

**状态：** `block_envelope_scan_not_a_proof`

## 参数

- `max_p`: `100000`
- `alpha`: `0.43`
- `thresholds`: `[2003, 10007]`
- `prime_count`: `9587`

## P>=2003

- `record_count`: `18578`
- `max_total_positive_over_sqrt`: `2.468627`
- `max_positive_bucket_sum_over_sqrt`: `2.468627`
- `max_positive_bucket_l2_over_sqrt`: `1.233496`
- `sqrt(6)*max_positive_bucket_l2`: `3.021437`
- `max_bucket_l2_over_sqrt`: `1.400329`
- `max_positive_bucket_effective_dimension`: `5.938250`
- `max_positive_bucket_cauchy6_bound_over_sqrt`: `3.021437`
- `min_cauchy6_slack_when_bound_ge_3`: `0.942963`

| beta bucket | max positive/sqrt | positive record | max abs/sqrt | abs record |
|---|---:|---|---:|---|
| [0.43,0.50) | 0.683635 | P=99439 plus D=71.886 | 0.696849 | P=4259 minus D=-17.711 |
| [0.50,0.60) | 0.862449 | P=34501 minus D=55.893 | 0.953624 | P=66629 minus D=-83.506 |
| [0.60,0.70) | 1.120079 | P=72701 plus D=102.326 | 1.120079 | P=72701 plus D=102.326 |
| [0.70,0.80) | 1.124010 | P=93139 minus D=114.798 | 1.124010 | P=93139 minus D=114.798 |
| [0.80,0.90) | 1.060012 | P=83267 plus D=103.203 | 1.060012 | P=83267 plus D=103.203 |
| [0.90,1.00) | 1.032597 | P=16339 plus D=47.880 | 1.128940 | P=59471 plus D=-93.777 |

### 同步性阈值

| positive sum threshold | records | max effective dimension | max positive L2/sqrt | min sqrt6 slack |
|---:|---:|---:|---:|---:|
| 1.5 | 243 | 5.938250 | 1.233496 | 0.008391 |
| 2.0 | 7 | 5.120320 | 1.233496 | 0.189174 |
| 2.2 | 3 | 5.120320 | 1.177635 | 0.189174 |
| 2.4 | 2 | 4.703659 | 1.177635 | 0.319504 |

### 能量阈值

| positive L2 threshold | records | max positive sum | max effective dimension | min sqrt6 slack |
|---:|---:|---:|---:|---:|
| 1.000000 | 46 | 2.468627 | 5.120320 | 0.189174 |
| 1.100000 | 9 | 2.468627 | 4.703659 | 0.319504 |
| 1.224745 | 1 | 2.078474 | 2.839314 | 0.942963 |
| 1.200000 | 1 | 2.078474 | 2.839314 | 0.942963 |

### 危险交集

| intersection | L1 threshold | L2 threshold | records | max L1 | max L2 |
|---|---:|---:|---:|---:|---:|
| l1_ge_12_5_and_l2_gt_6_5 | 2.400000 | 1.200000 | 0 | 0.000000 | 0.000000 |
| l1_ge_12_5_and_l2_gt_3_sqrt6 | 2.400000 | 1.224745 | 0 | 0.000000 | 0.000000 |

## P>=10007

- `record_count`: `16726`
- `max_total_positive_over_sqrt`: `2.468627`
- `max_positive_bucket_sum_over_sqrt`: `2.468627`
- `max_positive_bucket_l2_over_sqrt`: `1.233496`
- `sqrt(6)*max_positive_bucket_l2`: `3.021437`
- `max_bucket_l2_over_sqrt`: `1.400329`
- `max_positive_bucket_effective_dimension`: `5.938250`
- `max_positive_bucket_cauchy6_bound_over_sqrt`: `3.021437`
- `min_cauchy6_slack_when_bound_ge_3`: `0.942963`

| beta bucket | max positive/sqrt | positive record | max abs/sqrt | abs record |
|---|---:|---|---:|---|
| [0.43,0.50) | 0.683635 | P=99439 plus D=71.886 | 0.683635 | P=99439 plus D=71.886 |
| [0.50,0.60) | 0.862449 | P=34501 minus D=55.893 | 0.953624 | P=66629 minus D=-83.506 |
| [0.60,0.70) | 1.120079 | P=72701 plus D=102.326 | 1.120079 | P=72701 plus D=102.326 |
| [0.70,0.80) | 1.124010 | P=93139 minus D=114.798 | 1.124010 | P=93139 minus D=114.798 |
| [0.80,0.90) | 1.060012 | P=83267 plus D=103.203 | 1.060012 | P=83267 plus D=103.203 |
| [0.90,1.00) | 1.032597 | P=16339 plus D=47.880 | 1.128940 | P=59471 plus D=-93.777 |

### 同步性阈值

| positive sum threshold | records | max effective dimension | max positive L2/sqrt | min sqrt6 slack |
|---:|---:|---:|---:|---:|
| 1.5 | 229 | 5.938250 | 1.233496 | 0.008391 |
| 2.0 | 7 | 5.120320 | 1.233496 | 0.189174 |
| 2.2 | 3 | 5.120320 | 1.177635 | 0.189174 |
| 2.4 | 2 | 4.703659 | 1.177635 | 0.319504 |

### 能量阈值

| positive L2 threshold | records | max positive sum | max effective dimension | min sqrt6 slack |
|---:|---:|---:|---:|---:|
| 1.000000 | 45 | 2.468627 | 5.120320 | 0.189174 |
| 1.100000 | 9 | 2.468627 | 4.703659 | 0.319504 |
| 1.224745 | 1 | 2.078474 | 2.839314 | 0.942963 |
| 1.200000 | 1 | 2.078474 | 2.839314 | 0.942963 |

### 危险交集

| intersection | L1 threshold | L2 threshold | records | max L1 | max L2 |
|---|---:|---:|---:|---:|---:|
| l1_ge_12_5_and_l2_gt_6_5 | 2.400000 | 1.200000 | 0 | 0.000000 | 0.000000 |
| l1_ge_12_5_and_l2_gt_3_sqrt6 | 2.400000 | 1.224745 | 0 | 0.000000 | 0.000000 |

## 结构解释

若全局 `D_+<=3sqrt(S)` 要用桶级不等式证明，表中的 `max positive/sqrt` 给出每个 beta 桶需要覆盖的目标常数。若各桶最坏点不同，说明全局最大值不是单一尺度尖峰，而是多尺度中等偏差叠加；这更适合大筛/能量型证明。新增同步性阈值记录正偏差桶向量的有效维数与 Cauchy 松弛量：若 `sqrt(6)*L2` 只略超 3，但所有超界记录都有稳定松弛，就可以把硬点从单桶界推进到“六个尺度不能同时平坦同向”的结构命题。若某一桶长期主导，则应转入该桶的局部 PDEC/SAE 证书。
