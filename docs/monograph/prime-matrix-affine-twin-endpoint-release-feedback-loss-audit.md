# Prime Matrix AffineTwin endpoint-release feedback-loss audit

**状态：** `current_sweep_endpoint_release_feedback_loss_structured_global_open`

本审计继续下钻端点释放临界误差：即使把端点移动造成的几何支撑扩张全部记作容量回补，双端点同步仍留下不可回收的第二端点反馈损耗。

```text
feedback loss = endpoint release load - geometric support gain credit
geometric support gain credit = max(generator release, fill release)
feedback loss = min(generator release, fill release)
post-credit feedback error = feedback loss / support width - 1
```

```text
support_motion_candidate_count=11
support_width=20
total_endpoint_release_load=4929
total_geometric_support_gain_credit=2512
total_coupled_second_endpoint_feedback_loss=2417
total_post_credit_feedback_error=9.98636363636
min_feedback_loss=30
max_feedback_loss=429
min_post_credit_feedback_error=0.5
all_feedback_losses_exceed_support_width=true
endpoint_release_feedback_loss_structured_current_sweep=true
```

## 1. feedback-loss 表

| pair | side | load | gain credit | feedback loss | support width | post-credit error | route |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `13:8` | `below` | 140 | 75 | 65 | 20 | 2.25 | `EndpointReleaseFeedbackLoss-PDEC` |
| `13:9` | `above` | 677 | 341 | 336 | 20 | 15.8 | `EndpointReleaseFeedbackLoss-PDEC` |
| `13:12` | `below` | 256 | 133 | 123 | 20 | 5.15 | `EndpointReleaseFeedbackLoss-PDEC` |
| `13:28` | `below` | 720 | 365 | 355 | 20 | 16.75 | `EndpointReleaseFeedbackLoss-PDEC` |
| `15:8` | `below` | 78 | 44 | 34 | 20 | 0.7 | `EndpointReleaseFeedbackLoss-PDEC` |
| `15:9` | `above` | 739 | 372 | 367 | 20 | 17.35 | `EndpointReleaseFeedbackLoss-PDEC` |
| `15:12` | `below` | 194 | 102 | 92 | 20 | 3.6 | `EndpointReleaseFeedbackLoss-PDEC` |
| `15:28` | `below` | 658 | 334 | 324 | 20 | 15.2 | `EndpointReleaseFeedbackLoss-PDEC` |
| `19:9` | `above` | 863 | 434 | 429 | 20 | 20.45 | `EndpointReleaseFeedbackLoss-PDEC` |
| `19:12` | `below` | 70 | 40 | 30 | 20 | 0.5 | `EndpointReleaseFeedbackLoss-PDEC` |
| `19:28` | `below` | 534 | 272 | 262 | 20 | 12.1 | `EndpointReleaseFeedbackLoss-PDEC` |

## 2. 最窄反馈损耗点

最窄 atom 为 `19:12`，side `below`。端点释放负载为 `70`，其中可全部记作几何支撑扩张的最大信用为 `40`，仍余不可回收反馈损耗 `30`。
由于当前 support width 为 `20`，即便在全额回补后，post-credit feedback error 仍为 `0.5`。这把 `EndpointReleaseCoupling` 继续压成 `EndpointReleaseFeedbackLoss-PDEC`。

## 3. 最大反馈损耗波

最大 atom 为 `19:9`，side `above`，反馈损耗 `429` 对 support width `20`，post-credit feedback error `20.45`。

## 4. 结论边界

- 当前 `11` 个 support-motion 候选在全额几何支撑回补后，反馈损耗仍全部超过原 support width。
- 反馈损耗逐项等于较小端点释放量，说明它是双端点同步耦合的真实结构税，不是 formal envelope 重复记账。
- 本步不关闭全局行/列命题；它把持久端点耦合的剩余硬点进一步压成 `EndpointReleaseFeedbackLoss-PDEC` 的全局排斥或路由。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-support-motion-depth-ledger.json` | `0e2786c4a32ee35a38c027a4cadfe59cda82e09b51939d935fb476762c9700c7` |
| `data/prime-matrix-affine-twin-endpoint-release-critical-error-ledger.json` | `a7354165b75698539a4f0cc2cef63bb03373b5329f359d5d327f2a9ddfb4d078` |
