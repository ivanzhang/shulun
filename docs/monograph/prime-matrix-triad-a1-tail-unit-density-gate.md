# Triad-A1 Tail unit-density KL 门控

**状态：** `tail_unit_density_kl_floor_materialized`

任一非空残余洞都会留下 Tail unit-density 的未命中体积。因此 Tail 完成集合不能接近满层；若正式质量仍要落在其中，则支付统一 KL 下界。

## 1. 结构上界

对任一非空残余洞集 `Residual_b`，取其中一个洞 `c0`。Tail 要完成整个残余洞集，至少要覆盖 `c0`。
对每个 Tail 素数 `ell`，覆盖 `c0` 只占一个 `y mod ell` 残基；所以所有 Tail 素数都不覆盖 `c0` 的密度为：

```text
u_tail = product_{ell in Tail} (1-1/ell)。
```

因此：

```text
m_b/M_tail <= 1-u_tail
KL >= -log(1-u_tail)。
```

## 2. 来源指纹

| source | sha256 |
| --- | --- |
| `tail_unit_density_gate_script` | `de7a769c338285d6e9ba31a90b5e7b45bb22b050066a91d893ad531867ccdcb4` |
| `audit_1` | `17e00964a8d3bfd4b75a3c9d9ba943600eb24419a9881e5a105d87c6a24797af` |
| `audit_2` | `d08e44f727ca7b006fddcc672f1cd3066405f66e5987ce360f09642490767428` |

## 3. 总表

- `all_unit_density_bounds_pass=True`。

| layer | P | tail primes | u_tail | 1-u_tail | KL floor | positive residual survival | max actual completion ratio | positive actual avg KL | pass |
| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Q=2310->30030 | 17 | `[]` | 1 | 0 | infinity | 0 | 0 | infinity | `True` |
| Q=2310->30030 | 19 | `[17]` | 0.941176 | 0.0588235 | 2.83321 | 0.198675 | 0.0588235 | 2.83321 | `True` |
| Q=2310->30030 | 23 | `[17, 19]` | 0.891641 | 0.108359 | 2.2223 | 0.310345 | 0.108359 | 4.93773 | `True` |
| Q=2310->30030 | 29 | `[17, 19, 23]` | 0.852874 | 0.147126 | 1.91647 | 0.312821 | 0.0150761 | 6.99664 | `True` |
| Q=30030->510510 | 19 | `[]` | 1 | 0 | infinity | 0 | 0 | infinity | `True` |
| Q=30030->510510 | 23 | `[19]` | 0.947368 | 0.0526316 | 2.94444 | 0.160363 | 0.0526316 | 2.94444 | `True` |

## 4. 读法

若非空残余洞大量幸存且 `u_tail` 不趋零，则每层都有正 KL 成本，进入 PDEC。
若 KL 成本要趋零，只能让 `u_tail->0` 或让幸存残余洞趋于空；前者是高 Tail 密度极限，后者回到 promoted-prime 删除/空洞分支。
