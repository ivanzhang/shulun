# Prime Matrix AffineTwin support-motion depth audit

**状态：** `current_sweep_support_motion_depths_closed_global_open`

本审计继续下钻 `SupportMotionEscape`：如果不移动 residue pair，而是移动共同支撑窗口来吞掉空窗 CRT 代表，则相关同侧的 generator 与 shifted-fill 端点都必须释放，且两侧深度必须同时膨胀到同一个代表距离。

```text
support_motion_candidate_count=11
support_motion_side_histogram={'above': 3, 'below': 8}
support_width_current=20
min_required_common_side_depth=58
max_required_common_side_depth=435
min_endpoint_release_total_required=70
max_endpoint_release_total_required=863
min_extra_release_beyond_window_distance=30
support_motion_depth_closed_current_sweep=true
```

## 1. support-motion depth 表

| pair | side | nearest rep | window gap | common depth | g depth + | f depth + | endpoint release total | extra over gap |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `13:8` | `below` | 2594 | 75 | 93 | 75 | 65 | 140 | 65 |
| `13:9` | `above` | 3029 | 341 | 342 | 336 | 341 | 677 | 336 |
| `13:12` | `below` | 2536 | 133 | 151 | 133 | 123 | 256 | 123 |
| `13:28` | `below` | 2304 | 365 | 383 | 365 | 355 | 720 | 355 |
| `15:8` | `below` | 2625 | 44 | 62 | 44 | 34 | 78 | 34 |
| `15:9` | `above` | 3060 | 372 | 373 | 367 | 372 | 739 | 367 |
| `15:12` | `below` | 2567 | 102 | 120 | 102 | 92 | 194 | 92 |
| `15:28` | `below` | 2335 | 334 | 352 | 334 | 324 | 658 | 324 |
| `19:9` | `above` | 3122 | 434 | 435 | 429 | 434 | 863 | 429 |
| `19:12` | `below` | 2629 | 40 | 58 | 40 | 30 | 70 | 30 |
| `19:28` | `below` | 2397 | 272 | 290 | 272 | 262 | 534 | 262 |

## 2. 当前读数

- 当前 generator phase 为 `[2669, 2693]`，shifted-fill phase 为 `[2659, 2688]`，共同支撑为 `[2669, 2688]`。
- 因此左侧支撑由 generator lower 与 shifted-fill lower 共同限制，右侧支撑由 generator upper 与 shifted-fill upper 共同限制；吞掉空窗代表需要同侧两个端点同时释放。
- 最小深度膨胀 atom 是 `19:12`，nearest representative `2629`，需要共同侧深度 `58`，generator 深度额外 `40`，fill 深度额外 `30`。
- 当前最小总端点释放为 `70`，仍比原 window gap 多 `30`。

## 3. 结论边界

- 本步关闭当前 sweep 的 support-motion depth 账本：每个空窗若靠移动支撑变 actual，都必须同时释放两个相关端点，并同步增加 generator/fill 侧深度。
- 本步不证明全局 support motion 不复现；全局剩余是排斥这种同步深度膨胀的持久复现，或路由到 `MovingSupportDepthInflation-PDEC/SAE`、`EndpointReleaseCoupling-PDEC`、`PrimitiveTwinSlotSupportEscape-PDEC/SAE`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-crt-window-gap-ledger.json` | `4822729687dfb1818e8d917ca278f2eeda8d167825456f1dc1dd0456e142f71f` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-ledger.json` | `a8048685a2c6449b42ed5d2190aa47e75b20abf36a18e18c4d1ddb223cba033f` |
| `data/prime-matrix-affine-twin-unused-target-arrival-ledger.json` | `cc69729e33a77e2389eb185ee4e5fb959e4fe3087549bb31f6cba497f0b0caa3` |
| `data/prime-matrix-affine-twin-existing-actual-collision-jump-ledger.json` | `03c1a8e792df574299275b99c00caaf7901382e7414e08af20f7ee55c42c0e2b` |
