# Prime Matrix AffineTwin endpoint-release feedback-horizon slack audit

**状态：** `current_sweep_feedback_horizon_slack_structured_global_open`

本审计把 `phase horizon surplus` 再压成“必须新增的 side-depth skew”。若 CRT 代表距离为 `d`、支撑宽度为 `W`，则自反馈吸收至少需要 `max(0,d-W)` 的总 skew；当前 skew 不足的部分正好等于上一层的相位地平线缺口。

```text
required total skew = max(0, window distance - support width)
required extra skew = required total skew - current side-depth skew
required extra skew = phase horizon surplus
pure orientation flip gain = 0
```

```text
support_motion_candidate_count=11
support_width=20
total_required_absorption_skew=2292
total_current_side_depth_skew=95
total_required_extra_skew=2197
current_skew_coverage_ratio=0.0414485165794
extra_skew_deficit_ratio=0.958551483421
min_required_extra_skew=10
max_required_extra_skew=409
all_required_extra_skews_equal_phase_surpluses=true
all_pure_orientation_flips_fail_absorption=true
same_orientation_source_rematerialization_absent=true
feedback_horizon_slack_structured_current_sweep=true
```

## 1. slack 表

| pair | side | distance | support | current skew | required skew | extra skew | moving q candidates | same-source | route |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| `13:8` | `below` | 75 | 20 | 10 | 55 | 45 | `[96, 181]` | false | `EndpointSkewGrowth-PDEC/OrientationChangingPrimitiveKey-SAE` |
| `13:9` | `above` | 341 | 20 | 5 | 321 | 316 | `[1375]` | false | `EndpointSkewGrowth-PDEC/OrientationChangingPrimitiveKey-SAE` |
| `13:12` | `below` | 133 | 20 | 10 | 113 | 103 | `[154, 297]` | false | `EndpointSkewGrowth-PDEC/OrientationChangingPrimitiveKey-SAE` |
| `13:28` | `below` | 365 | 20 | 10 | 345 | 335 | `[386, 761]` | false | `EndpointSkewGrowth-PDEC/OrientationChangingPrimitiveKey-SAE` |
| `15:8` | `below` | 44 | 20 | 10 | 24 | 14 | `[65, 119]` | false | `EndpointSkewGrowth-PDEC/OrientationChangingPrimitiveKey-SAE` |
| `15:9` | `above` | 372 | 20 | 5 | 352 | 347 | `[1499]` | false | `EndpointSkewGrowth-PDEC/OrientationChangingPrimitiveKey-SAE` |
| `15:12` | `below` | 102 | 20 | 10 | 82 | 72 | `[123, 235]` | false | `EndpointSkewGrowth-PDEC/OrientationChangingPrimitiveKey-SAE` |
| `15:28` | `below` | 334 | 20 | 10 | 314 | 304 | `[355, 699]` | false | `EndpointSkewGrowth-PDEC/OrientationChangingPrimitiveKey-SAE` |
| `19:9` | `above` | 434 | 20 | 5 | 414 | 409 | `[1747]` | false | `EndpointSkewGrowth-PDEC/OrientationChangingPrimitiveKey-SAE` |
| `19:12` | `below` | 40 | 20 | 10 | 20 | 10 | `[61, 111]` | false | `EndpointSkewGrowth-PDEC/OrientationChangingPrimitiveKey-SAE` |
| `19:28` | `below` | 272 | 20 | 10 | 252 | 242 | `[293, 575]` | false | `EndpointSkewGrowth-PDEC/OrientationChangingPrimitiveKey-SAE` |

## 2. 最窄 slack 原子

最窄 atom 为 `19:12`，side `below`。它的 CRT 代表距窗口 `40`，support width 为 `20`，因此吸收所需总 skew 为 `20`。当前 skew 只有 `10`，还差 `10`。
该 atom 的 moving-key 公式候选为 `[61, 111]`，继承 source-rematerialization 账本后同向精确重物化为空，所以这 `10` 个单位不能由同向 source 补足。

## 3. 最大 slack 原子

最大 atom 为 `19:9`，side `above`，需要额外 skew `409`，moving-key 公式候选为 `[1747]`。

## 4. 结论边界

- `required extra skew = phase horizon surplus` 逐项成立，说明上一层相位缺口就是新增 skew 缺口。
- 纯方向翻转保持绝对 skew，不改变正 surplus；因此不能作为吸收机制。
- 同向 source 重物化继承为 absent，当前 `11` 个候选全部需要新的 skew-growth 或 orientation-changing primitive key。
- 本步只关闭当前 sweep 的匿名 slack 吸收解释；全局行/列命题仍需排斥 `EndpointSkewGrowth-PDEC`，或把方向改变/source 重物化/SAE 出口逐项闭合。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-endpoint-release-feedback-horizon-ledger.json` | `6ff4fc802d8444efe384a3c85a4688890357a96852d960877c9c92a8cc4f9cdb` |
| `data/prime-matrix-affine-twin-moving-key-source-rematerialization-ledger.json` | `b7d9016b2e43da9d390efdde3012739d24305e4843ed29efc8c295d16dc52fd6` |
