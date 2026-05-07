# Triad-A1 HoleResidueOccupancy 审计：Q=2310 -> Q=30030

**状态：** `hole_residue_occupancy_materialized`

本审计把 TailIndependentCompletion 的上界项 |Occ_t|/r 物化。当前层的非空旧洞在新增素数 residue 上占用比例明显低于 1，删除势主要来自未占用且不能被 Tail 独立完成的 zero-cover residue。

## 1. 结构等式

本层 promoted prime 为 `r=13`。固定旧活跃相位 `t` 与旧洞集 `H_Q(t)`：

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
| `base_multiplicity_json` | `5bcfa7c286e716b3b626c312becf303fee3b9d72142aaa30be63f849cb21162d` |
| `lift_multiplicity_json` | `c62dea9f85ebdf6fb69eb9870b0a4e4af89dd88ac696a2247b48dd22c4a4bbba` |

## 3. 总表

| P | nonempty phases | empty phases | occ rate | TI rate | union bound | actual survival | certified deletion lb | actual deletion | max occ | max TI |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 17 | 28 | 0 | 0.0769231 | 0 | 0.0769231 | 0.0769231 | 0.923077 | 0.923077 | 0.0769231 | 0 |
| 19 | 140 | 0 | 0.149451 | 0.0527473 | 0.202198 | 0.202198 | 0.797802 | 0.797802 | 0.153846 | 0.923077 |
| 23 | 232 | 0 | 0.222812 | 0.0875332 | 0.310345 | 0.310345 | 0.689655 | 0.689655 | 0.230769 | 0.846154 |
| 29 | 150 | 0 | 0.302564 | 0.0410256 | 0.34359 | 0.312821 | 0.65641 | 0.687179 | 0.307692 | 0.769231 |

## 4. cover 类型分解

| P | positive-cover survived | positive-cover killed | zero-cover survived/TI | zero-cover killed | empty-H survived | empty-H killed |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 17 | 28 | 0 | 0 | 336 | 0 | 0 |
| 19 | 272 | 0 | 96 | 1452 | 0 | 0 |
| 23 | 672 | 0 | 264 | 2080 | 0 | 0 |
| 29 | 530 | 60 | 80 | 1280 | 0 | 0 |

## 5. 按旧洞数分桶

### P=17

| old holes | phases | occ rate | TI rate | union bound | actual survival | certified deletion lb | min occ | max occ |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 28 | 0.0769231 | 0 | 0.0769231 | 0.0769231 | 0.923077 | 1 | 1 |

### P=19

| old holes | phases | occ rate | TI rate | union bound | actual survival | certified deletion lb | min occ | max occ |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 8 | 0.0769231 | 0.923077 | 1 | 1 | 0 | 1 | 1 |
| 2 | 132 | 0.153846 | 0 | 0.153846 | 0.153846 | 0.846154 | 2 | 2 |

### P=23

| old holes | phases | occ rate | TI rate | union bound | actual survival | certified deletion lb | min occ | max occ |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | 24 | 0.153846 | 0.846154 | 1 | 1 | 0 | 2 | 2 |
| 3 | 208 | 0.230769 | 0 | 0.230769 | 0.230769 | 0.769231 | 3 | 3 |

### P=29

| old holes | phases | occ rate | TI rate | union bound | actual survival | certified deletion lb | min occ | max occ |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 3 | 8 | 0.230769 | 0.769231 | 1 | 1 | 0 | 3 | 3 |
| 4 | 122 | 0.306431 | 0 | 0.306431 | 0.306431 | 0.693569 | 3 | 4 |
| 5 | 20 | 0.307692 | 0 | 0.307692 | 0.0769231 | 0.692308 | 4 | 4 |

## 6. 读法

本审计完成了 `TailIndependentCompletion` 后缺失的一块：`|Occ_t|/r` 不再是抽象项，而是可逐相位核验的占用率。

若后续无限塔中 `occupied_rate + TI_rate` 长期低于 `1`，则删除势发散。若该和趋近 `1`，只能发生两种结构事件：

```text
occupied_rate -> 1：旧洞集在新增素数 residue 上近乎满占用，进入容量/PDEC；
TI_rate       -> 1：promoted prime 近乎非必要，进入 NoDeletion-KL/CleanKLS。
```

因此下一步不再是数值逼近，而是证明这两个逃逸方向都必须回流到命名终端证书。
