# Prime Matrix square-phase low-alpha z=61 overlap 翻转原子

**状态：** `z61_hit_support_scale_drift_reduced_to_single_double_hit_overlap_open`

四个目标 profile 的 `52` 个支撑原子中，只有一个多模数重叠原子：`p=36739, omega=4, b=28842`，命中模数 `9614` 与 `14421`。删去该原子后 `36739` 的 actual 高/低尺度低于公共模型尺度；加入该原子后才翻到模型上方。因此当前最窄硬点已从整体支撑漂移压到单个 double-hit overlap 原子的可容许性，或其持续出现形成 Overlap-PDEC。

```text
support_atom_count=52
single_modulus_atom_count=51
multi_modulus_atom_count=1
overlap_contribution=0.555427
overlap_contribution_share_of_total_actual=0.043741
single_double_hit_overlap_flip_identity_closed=true
row_column_unconditional_closed=false
```

## 1. 唯一 overlap 原子

| p | omega | b | mult | contribution | hit moduli |
| ---: | ---: | ---: | ---: | ---: | --- |
| 36739 | 4 | 28842 | 1 | 0.555427 | `9614:0.390406, 14421:0.165021` |

## 2. 删除 overlap 后的尺度

| p | full scale | no-overlap scale | model scale | full drift | no-overlap drift | lift surplus | flips |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 10007 | 1.871028 | 1.871028 | 2.049869 | -0.087245 | -0.087245 | -0.037306 | false |
| 36739 | 2.081312 | 1.939863 | 2.049869 | 0.015339 | -0.053665 | 0.123469 | true |

## 3. 证明边界

- 已闭合：支撑尺度漂移到唯一 double-hit overlap 原子的翻转审计。
- 未闭合：该 overlap 原子的全局上界/不可持续性，或 Overlap-PDEC 排斥。
- 下一目标：`SingleDoubleHitOverlapAtomBoundOrOverlapPDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-hit-support-scale-router.json` | `5e65ff61fcd74d7a23a89d8f2799bb7dd8ff9ca9ceb8ac62789d055c44c7bea7` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_hit_overlap_flip_router.py` | `cd9f49abad64217111b564dfbe0a1b090b62cfd8edcd865f425d79a2692b9a88` |
