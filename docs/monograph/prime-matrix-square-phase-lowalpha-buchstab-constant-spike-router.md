# Prime Matrix square-phase low-alpha Buchstab 常数/尖峰二分

**状态：** `buchstab_constant_or_local_density_spike_dichotomy_materialized_open`

Buchstab 模型常数问题已严格二分：给定任意常数 `C_B`，若所有 block/尺度桶满足 `actual <= C_B*model`，则 low-alpha 模型负载由该常数支付；否则自动抽取最高超标 block 或尺度桶作为局部密度尖峰 PDEC 候选。本步闭合的是二分逻辑，不是常数证明或 PDEC 排斥。

```text
constant_spike_dichotomy_closed=true
uniform_buchstab_constant_proved=false
local_density_spike_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. 样本最坏比例

| scope | worst actual/model | witness |
| --- | ---: | --- |
| global | 1.414284 | all low-alpha rows |
| block | 1.718336 | `{'p': 83561, 'previous_cutoff': 248, 'cutoff': 496, 'hits': 979, 'model': 569.737366249656, 'actual_over_model': 1.7183356016200053, 'top_hit_predecessor': {'d_minus': 251, 'hits': 36, 'weighted_capacity': 333, 'h': 332.9123505976096, 's': 2.951371870363914, 'model_density': 0.054660685432196855, 'model': 18.20200824892155, 'actual_over_model': 1.9778037405368696}, 'top_model_excess_predecessor': {'d_minus': 337, 'hits': 30, 'weighted_capacity': 248, 'h': 247.95548961424333, 's': 3.0556538737129104, 'model_density': 0.05737662587408745, 'model': 14.229403216773687, 'actual_over_model': 2.1083104851956027}, 'h_bucket_rows': {'H0:<2': {'hits': 14.0, 'weighted_capacity': 14.0, 'model': 14.0, 'predecessors': 7.0, 'weighted_density': 1.0, 'actual_over_model': 1.0}, 'H7:>=128': {'hits': 965.0, 'weighted_capacity': 9612.0, 'model': 555.737366249656, 'predecessors': 41.0, 'weighted_density': 0.1003953391593841, 'actual_over_model': 1.7364317366532618}}}` |
| H-bucket | 1.851466 | `{'p': 10007, 'previous_cutoff': 31, 'cutoff': 62, 'bucket': 'H7:>=128', 'hits': 163.0, 'model': 88.03835213678116, 'actual_over_model': 1.8514658219267253, 'weighted_density': 0.10983827493261455}` |

## 2. 常数门表

| C_B | block sample pass | block failures | bucket sample pass | bucket failures | top bucket failure |
| ---: | ---: | ---: | ---: | ---: | --- |
| 1.500 | false | 4 | false | 17 | `{'p': 10007, 'previous_cutoff': 31, 'cutoff': 62, 'bucket': 'H7:>=128', 'hits': 163.0, 'model': 88.03835213678116, 'actual_over_model': 1.8514658219267253, 'weighted_density': 0.10983827493261455}` |
| 2.000 | true | 0 | true | 0 | `None` |
| 2.500 | true | 0 | true | 0 | `None` |
| 3.000 | true | 0 | true | 0 | `None` |

## 3. 证明边界

- 已闭合：任意常数 `C_B` 下的模型常数/局部尖峰二分。
- 未闭合：证明一个足够小的统一 Buchstab 常数。
- 未闭合：若统一常数失败，排除对应局部密度尖峰 PDEC。
- 下一目标：`UniformBuchstabConstantProofOrDensitySpikePDECExclusion`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-buchstab-model-density-router.json` | `68bfa3535663ae6b05870d4f28ae5dbb06e70e92e5eec2ca3e269fcf53c7914d` |
| `experiments/prime_matrix_square_phase_lowalpha_buchstab_constant_spike_router.py` | `70ab8b2b7968502ac2da19ebca485260051444fee30a9159871d59b41d7ec3b1` |
