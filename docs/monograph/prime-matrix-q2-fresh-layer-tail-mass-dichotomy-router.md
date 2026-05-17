# Q2 fresh-layer tail-mass 二分路由

**状态：** `controlled_fresh_layer_tail_mass_sae_or_aperture_explosion_not_global_proof`

无 PDEC 的 fresh endpoint 级联若仍保持局部/受控孔径，则每个新素层只贡献一个单余类质量，其总量由 sum W_j/B_j 控制。由于 fresh modulus 对数至少倍增，而端点替换孔径只线性增长，该质量可求和并进入 SAE。若孔径增长到能追赶 fresh modulus，则已经是孔径爆炸/全局支撑运动，必须回到 H3-DSB 或 moving-support PDEC。

```text
previous_hardpoint=FreshEndpointLayerCascadeNoFiniteCRTPeriodOrPDECSAEH3TailSieve;GlobalFinalInputsStillOpen
one_residue_fresh_layer_mass_model=true
linear_aperture_fresh_mass_summable=true
subexponential_controlled_aperture_summable=true
aperture_explosion_dichotomy=true
persistent_fresh_layer_correlation_routes_to_pdec=true
controlled_non_pdec_fresh_tail_routes_to_sae=true
row_column_unconditional_closed=false
next_direct_attack_target=ControlledFreshLayerTailMassSAEOrApertureExplosionH3PDEC;GlobalFinalInputsStillOpen
```

## 1. 单余类质量界

无 PDEC 的 fresh-layer 不能承载持久相关尖峰；它只能以“每个新素数层一个禁相位/零类”的形式进入 tail-sieve。
若该层素数为 `B_j`，局部孔径为 `W_j`，则形式质量至多为

\[
\frac{W_j}{B_j}.
\]

上一证书给出 fresh modulus `M_j` 的对数至少按倍增级联增长，且 `B_{j+1}>M_j`。在线性孔径 `W_j=W0+2j` 下，

\[
\sum_j \frac{W_0+2j}{B_j}<\infty.
\]

因此受控 fresh-tail 不能支撑无限反例链，只能是 SAE。

## 2. 孔径爆炸二分

若孔径增长不受控，满足 `log W_j` 反复追赶 `log M_j`，则这已经不是端点替换的局部线性债务，
而是孔径爆炸或全局支撑运动；该分支必须回到 `H3-DSB`、moving-support `PDEC` 或新的显式支撑运动账本。

## 3. 样本 tail-mass 读数

| P | x0 | Q2 | first log10 mass | partial log10 tail mass | last log10 mass |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 13 | 168 | 2203 | -924.084516 | -924.084516 | -236921.895952 |
| 17 | 1210 | 20593 | -8858.27719 | -8858.27719 | -2268099.077214 |
| 19 | 3658 | 69539 | -30046.573149 | -30046.573149 | -7692333.842973 |
| 23 | 58 | 1361 | -567.117821 | -567.117821 | -145575.736014 |

## 4. 三分流

| behavior | route | reason |
| --- | --- | --- |
| 受控孔径、无 PDEC fresh-tail | `SAE` | `sum W_j/B_j` 收敛。 |
| fresh-layer 命中持久相关集中 | `ColumnCRT/PDEC` | 违反单余类稀疏模型。 |
| 孔径增长追赶 fresh modulus | `H3-DSB/moving-support PDEC` | 已变成全局支撑运动或孔径爆炸。 |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| OneResidueFreshLayerMassModel | `true` | `true` | 无 PDEC 的 fresh-layer 只能作为每个新素数层一个禁相位/零类；在孔径 W 内的形式质量不超过 W/B。 | closed as model interface |
| LinearApertureFreshMassSummable | `true` | `true` | 在端点替换给出的线性孔径 W_j=W0+2j 下，fresh modulus 的对数至少倍增且 B_{j+1}>M_j，故 sum W_j/B_j 收敛。 | closed |
| SubexponentialControlledApertureSummable | `true` | `true` | 更一般地，若 log W_j=o(log M_j) 且 B_{j+1}>M_j，则 tail mass 仍由双指数分母压成可求和 SAE。 | closed as conditional router |
| ApertureExplosionDichotomy | `true` | `true` | 若 log W_j 不能受 log M_j 控制而无限追赶 fresh modulus，则它是孔径爆炸/全局支撑运动，不是局部端点替换。 | H3-DSB or moving-support PDEC |
| PersistentFreshLayerCorrelationRoutesToPDEC | `true` | `true` | 若 fresh-layer 命中不是单余类稀疏质量而是持久相关集中，则按定义进入 ColumnCRT/PDEC。 | closed as router |
| ControlledNonPDECFreshTailRoutesToSAE | `true` | `true` | 受控孔径且无 PDEC 的 fresh-layer 级联是可求和 SAE，不能支撑无限反例链。 | closed as controlled SAE |
| GlobalRowColumnUnconditionalClosureReached | `false` | `false` | 本步关闭受控 fresh-tail 质量；仍需排斥孔径爆炸、moving-support H3/DSB 与 fresh-layer PDEC。 | ControlledFreshLayerTailMassSAEOrApertureExplosionH3PDEC;GlobalFinalInputsStillOpen |

## 6. 最新剩余

```text
ControlledFreshLayerTailMassSAEOrApertureExplosionH3PDEC;GlobalFinalInputsStillOpen
```

本证书关闭的是受控孔径下的 non-PDEC fresh-tail 质量；它没有排斥孔径爆炸、moving-support H3/DSB 或 fresh-layer PDEC，
因此不构成行/列命题的全局无条件证明。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-q2-endpoint-fresh-layer-cascade-router.json` | `b200710347f0c8931c47081c87433097ee673a2919ec4a1833d887db6b7f73d2` |
| `docs/monograph/prime-matrix-q2-endpoint-replacement-aperture-growth-router.json` | `7a2c070b16c1642d4ffd1986ddca501aecf756f86223bab30cc397b4d88276e4` |
| `docs/monograph/prime-matrix-cycle-debt-fresh-modulus-tail-sieve-bridge-router.md` | `66ee650567d9e1db1192127c141d30392936eec6b2c59ba3c70d0ca5bece4d4a` |
| `docs/monograph/prime-matrix-cycle-debt-fresh-modulus-tail-self-contained-sync-router.md` | `d9441992110b21a3f435c755a6fbd048e211c5afb70e6dc5538c00db8b7bf2c1` |
