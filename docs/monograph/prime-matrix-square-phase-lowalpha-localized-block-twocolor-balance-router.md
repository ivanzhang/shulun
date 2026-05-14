# Prime Matrix square-phase low-alpha 局部块两色质量平衡

**状态：** `localized_block_signed_caps_reduced_to_twocolor_balance_open`

`signed/abs<=theta` 已等价改写为正负两色质量比 `max(P,N)/min(P,N)<=(1+theta)/(1-theta)`。`z=31` 的 cap 只需排除约 `3.895:1` 的正负质量偏斜，`z=61` 的 cap 需要排除约 `1.569:1` 的偏斜。因此最终局部块硬点变为两色质量平衡，若失败则直接给出 LocalizedBlock-PDEC。

```text
signed_ratio_to_twocolor_equivalence_closed=true
z31_wide_ratio_contract_materialized=true
z61_tight_ratio_contract_materialized=true
z31_twocolor_balance_proved=false
z61_twocolor_balance_proved=false
row_column_unconditional_closed=false
```

## 1. 两色合同

| atom | route | required ratio | observed ratio | slack | positive abs | negative abs |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `LocalizedBlockPDEC(z=31,bucket=balanced<=2)` | `BilinearDispersion` | 3.893245 | 1.056381 | 2.836864 | 82.658208 | 78.246622 |
| `LocalizedBlockPDEC(z=31,bucket=mid<=4)` | `BilinearDispersion` | 3.893245 | 1.004307 | 2.888937 | 87.918548 | 87.541468 |
| `LocalizedBlockPDEC(z=31,bucket=unbalanced<=8)` | `EndpointPDEC` | 3.893245 | 1.174004 | 2.719241 | 97.175560 | 82.772791 |
| `LocalizedBlockPDEC(z=31,bucket=far>8)` | `EndpointPDEC` | 3.893245 | 1.000145 | 2.893100 | 191.002773 | 190.975054 |
| `LocalizedBlockPDEC(z=61,bucket=balanced<=2)` | `BilinearDispersion` | 1.569115 | 1.065521 | 0.503594 | 242.756269 | 227.828604 |
| `LocalizedBlockPDEC(z=61,bucket=mid<=4)` | `BilinearDispersion` | 1.569115 | 1.043104 | 0.526011 | 197.944265 | 206.476448 |
| `LocalizedBlockPDEC(z=61,bucket=unbalanced<=8)` | `EndpointPDEC` | 1.569115 | 1.059236 | 0.509879 | 171.893492 | 162.280626 |
| `LocalizedBlockPDEC(z=61,bucket=far>8)` | `EndpointPDEC` | 1.569115 | 1.092816 | 0.476299 | 324.145990 | 354.232023 |

## 2. 证明边界

- 已闭合：signed-ratio cap 与两色质量比合同的等价转换。
- `z=31` 需要正负质量比不超过 `3.893245`。
- `z=61` 需要正负质量比不超过 `1.569115`。
- 未闭合：`z=31` 宽比例合同。
- 未闭合：`z=61` 紧比例合同，这是当前最窄点。
- 下一目标：`Z61TwoColorMassBalanceRatio1569OrLocalizedBlockPDEC`。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-coprime-boundary-bilinear-router.json` | `314e3b5b439a6928a478d24c1c439fcf692303883334747ac84e95f510dd569d` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-signed-ratio-budget-table-router.json` | `cd8a625bc18931335b1e7db7248ccf3517479b7040a8cf8e13f11338c42d90cd` |
| `experiments/prime_matrix_square_phase_lowalpha_localized_block_twocolor_balance_router.py` | `8c8e6e5cd8c506c78afda2a4e06c0eb7b02f19930111c69da7b6152fdd99a262` |
