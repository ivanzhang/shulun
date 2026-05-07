# Triad-A1 新层塔门控汇总

**状态：** `newlayer_tower_gate_materialized_not_global_proof`

已物化两层提升均为 FiberDeletionLayer：支撑恒等式成立、投影单调、且新层通过 fiber 删除重新稀疏。投影单调性已可由同一全周期完成集合 C_P 解释；这给出递归剥离路线的第二层证据；全局闭合仍需证明任意后继层的同一门控必然可验收。

## 1. 塔门控律

每次 Q->rQ 升层必须落入 FiberDeletion、ProjectionStitching、PDECEntropy 或 CleanKLS 之一。对同一 LHB allowed-set 的 M_Q 支撑，ProjectionStitching 已由投影单调性引理排除。该文件只汇总已物化层，不声称覆盖所有未来层。

形式上，每层都检查：

```text
Q' = rQ
|A_Q'| = sum_{t in A_Q}s(t) + |N|
N=empty        => 可谈 fiber 删除或近均匀；
N nonempty     => 一般 formal unit 下的 Projection/Stitching；
LHB M_Q 同口径 => 投影单调性给出 N=empty；
删除不足且偏斜 => PDECEntropy；
删除不足且平坦 => CleanKLS/DLS。
```

## 2. 来源指纹

| source | sha256 |
| --- | --- |
| `tower_gate_script` | `f9a476f360a0f778b782802b85d31916e3eb6399860c2875d4e1988bb45686e9` |
| `audit_1` | `a0cf1d6b5560d5568754bf9fb23462924bcf53453889cc2e3fa85357b576e504` |
| `audit_2` | `f07a7ba629db204c7b1d948851b52f35ac7f76697d434f68ea8dad21afdf31ed` |

## 3. 层摘要

| layer | r | P values | class | monotone | resparse | min drop | max survival | max entropy |
| --- | ---: | --- | --- | --- | --- | ---: | ---: | ---: |
| Q=2310->30030 | 13 | `[17, 19, 23, 29]` | `FiberDeletionLayer` | `True` | `True` | 3.19672 | 0.312821 | 0.576893 |
| Q=30030->510510 | 17 | `[19, 23]` | `FiberDeletionLayer` | `True` | `True` | 6.13889 | 0.162896 | 0.461487 |

## 4. P 级明细

### Q=2310 -> 30030

| P | old support | lifted support | survival | deletion | drop | hist | class |
| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 17 | 28 | 28 | 0.0769231 | 0.923077 | 13 | `{'1': 28}` | `ReSparsifiedByFiberDeletion` |
| 19 | 140 | 368 | 0.202198 | 0.797802 | 4.94565 | `{'13': 8, '2': 132}` | `ReSparsifiedByFiberDeletion` |
| 23 | 232 | 936 | 0.310345 | 0.689655 | 3.22222 | `{'13': 24, '3': 208}` | `ReSparsifiedByFiberDeletion` |
| 29 | 150 | 610 | 0.312821 | 0.687179 | 3.19672 | `{'1': 20, '13': 8, '3': 2, '4': 120}` | `ReSparsifiedByFiberDeletion` |

### Q=30030 -> 510510

| P | old support | lifted support | survival | deletion | drop | hist | class |
| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 19 | 368 | 496 | 0.0792839 | 0.920716 | 12.6129 | `{'1': 360, '17': 8}` | `ReSparsifiedByFiberDeletion` |
| 23 | 936 | 2592 | 0.162896 | 0.837104 | 6.13889 | `{'17': 48, '2': 888}` | `ReSparsifiedByFiberDeletion` |

## 5. 当前边界

本汇总完成的是有限塔证据：`2310 -> 30030 -> 510510` 已按同一门控重复通过。
它仍未证明所有未来素因子层都会通过；下一步需把 `N=empty` 或 `N` 的 Stitching 吸收写成
针对任意新增素因子 `r` 的投影兼容判据。
