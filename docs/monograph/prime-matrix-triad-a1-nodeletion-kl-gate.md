# Triad-A1 NoDeletion-KL 门控审计

**状态：** `nodeletion_kl_gate_materialized_current_layers_deleting`

当前已物化层没有触发 NoDeletion；全部仍在 FiberDeletion。本文件给出后续层一旦删除停止时的 KL 分流接口。

## 1. 门控律

若 survival 未趋近 1，则仍在 FiberDeletion。若 survival->1 且 KL 在正质量层上累计，进入 new-layer PDEC；若 KL 可求和并趋零，则进入 CleanKLS/DLS。

有限审计阈值：

- `nodeletion_survival=0.9`。
- `kl_pdec_threshold=0.25`。
- `clean_kl_threshold=0.05`。

这些阈值只用于当前报告分流；正式极限命题使用 `survival->1` 与 `sum KL`。

## 2. 来源指纹

| source | sha256 |
| --- | --- |
| `nodeletion_kl_gate_script` | `c05adcb46bd58d677a27863a112596956d2575e79838cbae47a31c4dc8a89e4f` |
| `audit_1` | `a0cf1d6b5560d5568754bf9fb23462924bcf53453889cc2e3fa85357b576e504` |
| `audit_2` | `f07a7ba629db204c7b1d948851b52f35ac7f76697d434f68ea8dad21afdf31ed` |

## 3. 门控统计

- `current_nodeletion_triggered=False`。
- `gate_counts={'FiberDeletion': 6}`。

## 4. 明细

| layer | P | survival | deletion | drop | norm entropy | norm KL | KL nats | Pinsker TV | gate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Q=2310->30030 | 17 | 0.0769231 | 0.923077 | 13 | 0 | 1 | 2.56495 | 1 | `FiberDeletion` |
| Q=2310->30030 | 19 | 0.202198 | 0.797802 | 4.94565 | 0.455023 | 0.544977 | 1.39784 | 0.836014 | `FiberDeletion` |
| Q=2310->30030 | 23 | 0.310345 | 0.689655 | 3.22222 | 0.565879 | 0.434121 | 1.1135 | 0.746157 | `FiberDeletion` |
| Q=2310->30030 | 29 | 0.312821 | 0.687179 | 3.19672 | 0.576893 | 0.423107 | 1.08525 | 0.73663 | `FiberDeletion` |
| Q=30030->510510 | 19 | 0.0792839 | 0.920716 | 12.6129 | 0.274194 | 0.725806 | 2.05636 | 1 | `FiberDeletion` |
| Q=30030->510510 | 23 | 0.162896 | 0.837104 | 6.13889 | 0.461487 | 0.538513 | 1.52572 | 0.873419 | `FiberDeletion` |

## 5. 读法

当前没有 `NoDeletion` 行，说明已物化层仍靠 fiber 删除推进。后续若出现 `NoDeletionCleanKLSCandidate`，
必须检查 CleanKLS admission；若出现 `NoDeletionKLPDEC`，则把该层作为 refined/new-layer PDEC 输入。
