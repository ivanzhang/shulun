# Triad-A1 HoleResidueOccupancy 审计：Q=30030 -> Q=510510

**状态：** `hole_residue_occupancy_materialized`

本审计把 TailIndependentCompletion 的上界项 |Occ_t|/r 物化。当前层的非空旧洞在新增素数 residue 上占用比例明显低于 1，删除势主要来自未占用且不能被 Tail 独立完成的 zero-cover residue。

## 1. 结构等式

本层 promoted prime 为 `r=17`。固定旧活跃相位 `t` 与旧洞集 `H_Q(t)`：

```text
Occ_t={b: exists c in H_Q(t), ((t+bQ-1)P+c)=0 mod r}
TI_t ={b: b notin Occ_t, 且 lift 后该 fiber 仍幸存}
S_t  ={b: lift 后该 fiber 幸存}
```

对非空 `H_Q(t)`：

```text
S_t subset Occ_t union TI_t
|S_t|/r <= |Occ_t|/r + |TI_t|/r
|Occ_t| <= min(|H_Q(t)|, r)
```

所以只要 `Occ_t` 与 `TI_t` 不同时接近满层，fiber 删除势就不能消失。

## 2. 来源指纹

| source | sha256 |
| --- | --- |
| `hole_residue_occupancy_script` | `b676200f2527e4bda6776111dd34960253fd24e314d4957d36104f7b7da8802f` |
| `base_multiplicity_json` | `c62dea9f85ebdf6fb69eb9870b0a4e4af89dd88ac696a2247b48dd22c4a4bbba` |
| `lift_multiplicity_json` | `400fadeec3a97b7cd6c22ed0bd5e1271c703ebda07ee074db7db549d43d9b4fd` |

## 3. 总表

| P | nonempty phases | empty phases | occ rate | TI rate | union bound | actual survival | certified deletion lb | actual deletion | max occ | max TI |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 19 | 360 | 8 | 0.0588235 | 0 | 0.0588235 | 0.0588235 | 0.941176 | 0.941176 | 0.0588235 | 0 |
| 23 | 936 | 0 | 0.11463 | 0.0482655 | 0.162896 | 0.162896 | 0.837104 | 0.837104 | 0.117647 | 0.941176 |

## 4. cover 类型分解

| P | positive-cover survived | positive-cover killed | zero-cover survived/TI | zero-cover killed | empty-H survived | empty-H killed |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 19 | 360 | 0 | 0 | 5760 | 136 | 0 |
| 23 | 1824 | 0 | 768 | 13320 | 0 | 0 |

## 5. 按旧洞数分桶

### P=19

| old holes | phases | occ rate | TI rate | union bound | actual survival | certified deletion lb | min occ | max occ |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 8 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| 1 | 360 | 0.0588235 | 0 | 0.0588235 | 0.0588235 | 0.941176 | 1 | 1 |

### P=23

| old holes | phases | occ rate | TI rate | union bound | actual survival | certified deletion lb | min occ | max occ |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 48 | 0.0588235 | 0.941176 | 1 | 1 | 0 | 1 | 1 |
| 2 | 888 | 0.117647 | 0 | 0.117647 | 0.117647 | 0.882353 | 2 | 2 |

## 6. 读法

本审计完成了 `TailIndependentCompletion` 后缺失的一块：`|Occ_t|/r` 不再是抽象项，而是可逐相位核验的占用率。

若后续无限塔中 `occupied_rate + TI_rate` 长期低于 `1`，则删除势发散。若该和趋近 `1`，只能发生两种结构事件：

```text
occupied_rate -> 1：旧洞集在新增素数 residue 上近乎满占用，进入容量/PDEC；
TI_rate       -> 1：promoted prime 近乎非必要，进入 NoDeletion-KL/CleanKLS。
```

因此下一步不再是数值逼近，而是证明这两个逃逸方向都必须回流到命名终端证书。
