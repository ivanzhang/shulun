# Prime Matrix AffineTwin endpoint-release feedback-horizon audit

**状态：** `current_sweep_endpoint_release_feedback_horizon_structured_global_open`

本审计把 feedback loss 再改写为相位地平线判据：一个空窗 CRT 代表若要被端点自反馈吸收，它到当前支撑窗口的距离必须不超过 `support_width + side_depth_skew`。

```text
feedback horizon = support width + |generator side depth - fill side depth|
phase horizon surplus = window distance - feedback horizon
```

```text
support_motion_candidate_count=11
support_motion_side_histogram={'above': 3, 'below': 8}
support_width=20
total_window_distance=2512
total_feedback_horizon_width=315
total_phase_horizon_surplus=2197
min_phase_horizon_surplus=10
max_phase_horizon_surplus=409
all_feedback_loss_formulas_hold=true
all_representatives_outside_feedback_horizon=true
endpoint_release_feedback_horizon_structured_current_sweep=true
```

## 1. feedback-horizon 表

| pair | side | distance | support | skew | horizon | surplus | route |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `13:8` | `below` | 75 | 20 | 10 | 30 | 45 | `EndpointReleaseFeedbackHorizon-PDEC` |
| `13:9` | `above` | 341 | 20 | 5 | 25 | 316 | `EndpointReleaseFeedbackHorizon-PDEC` |
| `13:12` | `below` | 133 | 20 | 10 | 30 | 103 | `EndpointReleaseFeedbackHorizon-PDEC` |
| `13:28` | `below` | 365 | 20 | 10 | 30 | 335 | `EndpointReleaseFeedbackHorizon-PDEC` |
| `15:8` | `below` | 44 | 20 | 10 | 30 | 14 | `EndpointReleaseFeedbackHorizon-PDEC` |
| `15:9` | `above` | 372 | 20 | 5 | 25 | 347 | `EndpointReleaseFeedbackHorizon-PDEC` |
| `15:12` | `below` | 102 | 20 | 10 | 30 | 72 | `EndpointReleaseFeedbackHorizon-PDEC` |
| `15:28` | `below` | 334 | 20 | 10 | 30 | 304 | `EndpointReleaseFeedbackHorizon-PDEC` |
| `19:9` | `above` | 434 | 20 | 5 | 25 | 409 | `EndpointReleaseFeedbackHorizon-PDEC` |
| `19:12` | `below` | 40 | 20 | 10 | 30 | 10 | `EndpointReleaseFeedbackHorizon-PDEC` |
| `19:28` | `below` | 272 | 20 | 10 | 30 | 242 | `EndpointReleaseFeedbackHorizon-PDEC` |

## 2. 最窄相位地平线缺口

最窄 atom 为 `19:12`，side `below`。其 CRT 代表距窗口 `40`，support width 为 `20`，当前两端点侧深度差为 `10`，所以 feedback horizon 为 `30`，仍有相位地平线缺口 `10`。
这给出当前最精确的局部超界矛盾点：反例链要求支撑移动吸收该代表，真实链给出的最大自反馈吸收地平线却短 `10`。

## 3. 最大地平线缺口

最大 atom 为 `19:9`，side `above`，distance `434` 对 horizon `25`，surplus `409`。

## 4. 结论边界

- `feedback_loss = window_distance - side_depth_skew` 逐项成立，说明上一层 feedback loss 有纯相位公式。
- `phase_horizon_surplus` 逐项等于 post-credit overcritical units，说明几何回补后的正临界误差正是 CRT 代表越过反馈地平线的距离。
- 当前 `11` 个候选全部在 feedback horizon 外，因此当前 sweep 的端点自反馈吸收通道关闭，并登记为 `EndpointReleaseFeedbackHorizon-PDEC`。
- 本步仍不关闭全局行/列命题；全局剩余是排斥该地平线缺口持久复现，或把它路由到方向改变/source 重物化/SAE 出口。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-support-motion-depth-ledger.json` | `0e2786c4a32ee35a38c027a4cadfe59cda82e09b51939d935fb476762c9700c7` |
| `data/prime-matrix-affine-twin-endpoint-release-feedback-loss-ledger.json` | `b011a7b30e71589563e9a5893a068dcf6bf4f3e1168bc36bf0bec195a796d5f9` |
