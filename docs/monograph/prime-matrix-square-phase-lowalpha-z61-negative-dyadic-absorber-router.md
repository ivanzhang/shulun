# Prime Matrix square-phase low-alpha z=61 negative dyadic absorber

**状态：** `z61_negative_support_absorbed_by_lcm_anchored_dyadic_lifts_global_proof_open`

唯一负多命中支撑不只是被正计数覆盖，而是呈现更刚性的 dyadic lift 吸收：负原子 `b=28842` 等于 hit-moduli `[9614,14421]` 的 lcm，同组两条正记录正好位于 `2b` 与 `4b`，且单位权重完全相同。因此样本内负-only 失败对象被压成一个更窄的全局输入：证明所有负多命中 lcm 锚都有足够 dyadic 正升格，或登记 DyadicLift-PDEC。

```text
negative_group_count=1
absorber_atom_count=1
all_negative_atoms_lcm_anchored=true
all_negative_atoms_have_two_dyadic_lifts=true
all_negative_groups_locally_absorbed=true
dyadic_absorber_criterion_closed_for_sample=true
global_dyadic_lift_absorber_proved=false
row_column_unconditional_closed=false
```

## 1. 吸收器表

| hit moduli | lcm | negative p | negative b | dyadic quotients | positive surplus | signed weight | closed |
| --- | ---: | ---: | ---: | --- | ---: | ---: | --- |
| `[9614, 14421]` | 28842 | 36739 | 28842 | `[2, 4]` | 1 | 0.555427 | true |

## 2. 正向 lift 见证

| negative b | positive p | positive b | quotient | power of two | same weight |
| ---: | ---: | ---: | ---: | --- | --- |
| 28842 | 200003 | 57684 | 2 | true | true |
| 28842 | 200003 | 115368 | 4 | true | true |

## 3. 自足小引理

在固定 hit-moduli 组中，所有原子的单位权重只由该组决定。若负原子数为 `N_-`，同组正原子数为 `N_+`，且 `N_+>=N_-`，则该组 signed count 与 signed weight 均非负。本证书进一步确认样本中的唯一负组满足更强条件：负 `b` 等于 hit lcm，正见证为同组 `2b,4b` 两个 dyadic lift。

## 4. 证明边界

- 已闭合：样本目标格中唯一负多命中原子由 `2b,4b` 两个同权正 lift 吸收。
- 未闭合：全局 dyadic lift 吸收器存在性，或 DyadicLift-PDEC 排斥。
- 下一目标：`GlobalDyadicLiftAbsorberProofOrDyadicLiftPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-negative-support-isolation-router.json` | `e847e9645e047e97fe03aa92d9093c5c98718e202a3d1fe4c3e52de46ebe1676` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_negative_dyadic_absorber_router.py` | `2304105cb77cf851885916d983ab058456f4b63a27c8be00aa0193cf421c0637` |
