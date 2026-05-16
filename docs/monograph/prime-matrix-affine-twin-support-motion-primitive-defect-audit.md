# Prime Matrix AffineTwin support-motion primitive-depth defect audit

**状态：** `current_sweep_support_motion_primitive_defects_closed_global_open`

本审计继续下钻 `SupportMotionDepth`：若支撑移动仍试图保持当前 `q=31` AffineTwin primitive key，则所需共同侧深度会同时打破 generator 与 fill 的 AffineTwin 深度恒等式。

```text
support_motion_primitive_defect_candidate_count=11
support_motion_side_histogram={'above': 3, 'below': 8}
min_total_affine_depth_defect=70
max_total_affine_depth_defect=863
all_support_motion_breaks_both_depth_identities=true
fixed_primitive_key_support_motion_absorption_closed_current_sweep=true
```

## 1. primitive-depth defect 表

| pair | side | rep | required depth | g rhs | f rhs | g defect | f defect | total |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `13:8` | `below` | 2594 | 93 | 18 | 28 | 75 | 65 | 140 |
| `13:9` | `above` | 3029 | 342 | 6 | 1 | 336 | 341 | 677 |
| `13:12` | `below` | 2536 | 151 | 18 | 28 | 133 | 123 | 256 |
| `13:28` | `below` | 2304 | 383 | 18 | 28 | 365 | 355 | 720 |
| `15:8` | `below` | 2625 | 62 | 18 | 28 | 44 | 34 | 78 |
| `15:9` | `above` | 3060 | 373 | 6 | 1 | 367 | 372 | 739 |
| `15:12` | `below` | 2567 | 120 | 18 | 28 | 102 | 92 | 194 |
| `15:28` | `below` | 2335 | 352 | 18 | 28 | 334 | 324 | 658 |
| `19:9` | `above` | 3122 | 435 | 6 | 1 | 429 | 434 | 863 |
| `19:12` | `below` | 2629 | 58 | 18 | 28 | 40 | 30 | 70 |
| `19:28` | `below` | 2397 | 290 | 18 | 28 | 272 | 262 | 534 |

## 2. 当前读数

- 最小 fixed-primitive 缺陷 atom 是 `19:12`，side `below`，nearest representative `2629`。
- 它需要共同侧深度 `58`；但当前 AffineTwin 深度恒等式给出 generator 缺陷 `40`、fill 缺陷 `30`，总缺陷 `70`。
- 所有 `11` 个 support-motion 候选都同时打破 generator 与 fill 的固定 q 深度恒等式。

## 3. 结论边界

- 本步关闭当前 sweep 的 fixed primitive key absorption：support motion 不能在保持当前 `q=31` primitive key 的同时吞掉空窗 CRT 代表。
- 本步不证明 moving primitive key 全局不复现；全局剩余是排斥 primitive key 迁移，或路由到 `MovingPrimitiveKey-PDEC/SAE`、`MovingSupportDepthInflation-PDEC/SAE`、`EndpointReleaseCoupling-PDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-support-motion-depth-ledger.json` | `0e2786c4a32ee35a38c027a4cadfe59cda82e09b51939d935fb476762c9700c7` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-ledger.json` | `a8048685a2c6449b42ed5d2190aa47e75b20abf36a18e18c4d1ddb223cba033f` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-primitive-identity-ledger.json` | `c4a2bfa9e30b4444723f339d4501c3ea14b97fc62954ac659095bacc80c2d5f1` |
