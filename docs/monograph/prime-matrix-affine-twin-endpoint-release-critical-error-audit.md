# Prime Matrix AffineTwin endpoint-release critical-error audit

**状态：** `current_sweep_endpoint_release_critical_error_structured_global_open`

本审计把 support-motion 的剩余逃逸接入临界误差框架：

```text
critical error = actual endpoint-release load / support width - 1
```

这里的 `support width` 是当前 primitive 双槽共同支撑窗口宽度；`actual endpoint-release load` 是为了把空窗 CRT 代表纳入支撑，generator 与 shifted-fill 两个端点必须同步释放的总量。

```text
support_motion_candidate_count=11
critical_capacity_support_width=20
total_endpoint_release_load=4929
total_window_capacity_budget=220
total_endpoint_release_critical_error=21.4045454545
min_endpoint_release_critical_error=2.5
max_endpoint_release_critical_error=42.15
all_endpoint_release_loads_supercritical=true
all_same_orientation_rematerialization_absent=true
endpoint_release_critical_error_structured_current_sweep=true
```

## 1. endpoint-release 临界误差表

| pair | side | load | capacity | critical error | moving q | route |
| --- | --- | ---: | ---: | ---: | --- | --- |
| `13:8` | `below` | 140 | 20 | 6 | `96,181` | `96:CompositeQ,181:PrimeButNotTwinAffine` |
| `13:9` | `above` | 677 | 20 | 32.85 | `1375` | `1375:CompositeQ` |
| `13:12` | `below` | 256 | 20 | 11.8 | `154,297` | `154:CompositeQ,297:CompositeQ` |
| `13:28` | `below` | 720 | 20 | 35 | `386,761` | `386:CompositeQ,761:PrimeButNotTwinAffine` |
| `15:8` | `below` | 78 | 20 | 2.9 | `65,119` | `65:CompositeQ,119:CompositeQ` |
| `15:9` | `above` | 739 | 20 | 35.95 | `1499` | `1499:PrimeButNotTwinAffine` |
| `15:12` | `below` | 194 | 20 | 8.7 | `123,235` | `123:CompositeQ,235:CompositeQ` |
| `15:28` | `below` | 658 | 20 | 31.9 | `355,699` | `355:CompositeQ,699:CompositeQ` |
| `19:9` | `above` | 863 | 20 | 42.15 | `1747` | `1747:PrimeButNotTwinAffine` |
| `19:12` | `below` | 70 | 20 | 2.5 | `61,111` | `61:PrimeButNotTwinAffine,111:CompositeQ` |
| `19:28` | `below` | 534 | 20 | 25.7 | `293,575` | `293:PrimeButNotTwinAffine,575:CompositeQ` |

## 2. 最窄显式超界点

最窄 atom 为 `19:12`，side `below`。它的端点释放负载为 `70`，临界窗口容量为 `20`，所以临界误差为 `50/20=2.5`。
该 atom 的 moving q 候选是 `[61, 111]`；上一层 source-rematerialization 审计已经证明这些候选不能同向重物化为 AffineTwin source。因此这个正临界误差不能作为普通波动隐藏，只能显化为 `EndpointReleaseCoupling-PDEC`。

## 3. 最大局部超界波

最大 atom 为 `19:9`，side `above`，端点释放负载 `863` 对容量 `20`，临界误差 `843/20=42.15`。

## 4. 结论边界

- 当前 `11` 个 support-motion 候选全部为正临界误差，并且全部需要双端点同步释放。
- 固定 primitive key 的深度缺陷总量与端点释放负载逐项相同，说明这不是记账重复，而是同一个结构刚性的两种投影。
- 同向 moving-key source-rematerialization 已缺席，所以当前 sweep 的匿名临界误差被消去，全部登记为 `EndpointReleaseCoupling-PDEC`。
- 本步仍不证明全局行/列命题；全局剩余是排斥 `EndpointReleaseCoupling-PDEC` 持久复现，或处理方向改变/source 重物化出口。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-support-motion-depth-ledger.json` | `0e2786c4a32ee35a38c027a4cadfe59cda82e09b51939d935fb476762c9700c7` |
| `data/prime-matrix-affine-twin-support-motion-primitive-defect-ledger.json` | `7c63e2c3bd443a430ef7f633d1359f88c65ead388b69f34a0e0f9d72ccb32ef4` |
| `data/prime-matrix-affine-twin-moving-key-source-rematerialization-ledger.json` | `b7d9016b2e43da9d390efdde3012739d24305e4843ed29efc8c295d16dc52fd6` |
