# Triad-A1 新层 fiber 删除审计：Q=30030 -> Q=510510

**状态：** `newlayer_fiber_deletion_entropy_audited`

本审计把固定 Q 密度屏障后的升层动作改写为精确 fiber 删除账本。若新增层真实删除旧相位 fiber，则支撑密度按恒等式下降；若不删除而趋近均匀，则转入 CleanKLS/DLS；若出现旧零相位新增激活，则进入 Stitching/坐标商归一化。

## 1. 结构恒等式

令 `Q'=rQ`，旧相位 `t mod Q` 的新层 fiber 为：

```text
t, t+Q, t+2Q, ..., t+(r-1)Q。
```

记 `A_Q={t:M_Q(t)>0}`，并令

```text
s(t)=#{b in [0,r): M_{Q'}(t+bQ)>0}。
```

若新层支撑没有落在旧零相位上，则有精确恒等式：

```text
|supp(M_{Q'})| = sum_{t in A_Q} s(t),
density(M_{Q'}) = density(M_Q) * average_{t in A_Q}(s(t)/r)。
```

这就是固定层密度屏障之后的递归剥离入口：`s(t)<r` 的系统性出现会重新稀疏。

## 2. 来源指纹

| source | sha256 |
| --- | --- |
| `fiber_audit_script` | `d6ba98c8daa54fc165a808563461af6e5db53394f54cf5099959e908e638c47a` |
| `base_multiplicity_json` | `c62dea9f85ebdf6fb69eb9870b0a4e4af89dd88ac696a2247b48dd22c4a4bbba` |
| `lift_multiplicity_json` | `400fadeec3a97b7cd6c22ed0bd5e1271c703ebda07ee074db7db549d43d9b4fd` |

## 3. 总表

| P | old support | lifted support | survival | deletion | density drop | support hist | entropy | class |
| ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | --- |
| 19 | 368 | 496 | 0.0792839 | 0.920716 | 12.6129 | `{'1': 360, '17': 8}` | 0.274194 | `ReSparsifiedByFiberDeletion` |
| 23 | 936 | 2592 | 0.162896 | 0.837104 | 6.13889 | `{'17': 48, '2': 888}` | 0.461487 | `ReSparsifiedByFiberDeletion` |

## 4. 当前读数

- `all_support_identities_hold=True`。
- `all_monotone_lift_support=True`。
- `all_classified_resparse=True`。

本次 `Q=30030 -> 510510` 的共同 P 上没有旧零相位新增激活；所以密度下降不是统计口号，
而是由 fiber 删除恒等式逐相位核算出来的。

## 5. 二分出口

```text
FiberDeletion:  s(t)/r 在正比例质量上小于 1
  => 新层重新稀疏，回到更细层 Empty/Sparse/PDEC 审计；

NearUniform:    s(t) 接近 r 且 fiber 熵接近 1
  => 新层不再提供定向覆盖，转 CleanKLS/DLS；

NewActivation:  supp(M_{Q'}) 投到旧零相位
  => 口径不一致，转 Stitching/坐标商/复用缺陷吸收。
```
