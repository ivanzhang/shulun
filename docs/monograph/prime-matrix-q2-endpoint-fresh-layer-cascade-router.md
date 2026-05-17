# Q2 端点新素层级联扩模路由

**状态：** `fresh_endpoint_layer_cascade_routed_not_global_proof`

有界孔径被排除后，扩孔/移动若继续沿全轮端点复现推进，就必须不断引入新的右端素数层。每个新右端素数在下一阶全轮中又被自身零类杀掉，因此形成 fresh-endpoint 级联。该级联使 CRT 模数对数至少逐阶倍增，而端点替换孔径只线性加二；所以任何固定有限 CRT 周期都不能作为无限反例链的终端稳定结构。

```text
previous_hardpoint=EndpointReplacementApertureGrowthNoBoundedReplayOrMovingSupportPDECSAEH3DSB;GlobalFinalInputsStillOpen
fresh_endpoint_after_each_replacement=true
next_full_wheel_kills_fresh_endpoint=true
log_modulus_at_least_doubles_per_endpoint_cascade=true
aperture_lower_bound_growth_linear_plus_two=true
finite_crt_period_terminal_possible=false
persistent_fresh_endpoint_pattern_routes_to_pdec_columncrt=true
sparse_fresh_endpoint_cascade_routes_to_sae=true
non_pdec_fresh_layer_cascade_routes_to_tail_sieve_h3=true
row_column_unconditional_closed=false
next_direct_attack_target=FreshEndpointLayerCascadeNoFiniteCRTPeriodOrPDECSAEH3TailSieve;GlobalFinalInputsStillOpen
```

## 1. 级联引理

设第 `j` 阶全轮模数为 `M_j`，右端真实相邻素数为 `B_j`。上一张证书已证明，
全轮复现会把当前闭载体块变成闭复合块，故下一真实右端素数满足

\[
B_{j+1}>\text{right edge of the copied block}\ge M_j.
\]

于是 `B_{j+1}` 是旧有限端点层之外的新素层。若下一步使用完整 `B_{j+1}` 阶轮，则该新端点也被纳入模数，
下一次复现时它的复制点被 `B_{j+1}` 自身整除。令 `L_j=log M_j`，则

\[
L_{j+1}\ge L_j+\log B_{j+1}>2L_j.
\]

这说明端点替换链不是固定有限 CRT 周期，而是新素层不断加入的扩模级联。

## 2. 与孔径增长的尺度错位

端点替换只强制闭孔径下界每次增加 `2`；但模数对数至少倍增。固定有限 CRT 周期无法同时容纳无界新素层。

## 3. 样本级联读数

| P | x0 | Q2 | stage | width lower | log10 modulus lower | log10 modulus - log10 width |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 13 | 168 | 2203 | 0 | 25 | 925.482456 | 924.084516 |
| 13 | 168 | 2203 | 1 | 27 | 1850.964912 | 1849.533548 |
| 13 | 168 | 2203 | 2 | 29 | 3701.929824 | 3700.467426 |
| 13 | 168 | 2203 | 3 | 31 | 7403.859648 | 7402.368286 |
| 13 | 168 | 2203 | 4 | 33 | 14807.719296 | 14806.200782 |
| 17 | 1210 | 20593 | 0 | 31 | 8859.768552 | 8858.27719 |
| 17 | 1210 | 20593 | 1 | 33 | 17719.537104 | 17718.01859 |
| 17 | 1210 | 20593 | 2 | 35 | 35439.074208 | 35437.53014 |
| 17 | 1210 | 20593 | 3 | 37 | 70878.148416 | 70876.580214 |
| 17 | 1210 | 20593 | 4 | 39 | 141756.296832 | 141754.705767 |
| 19 | 3658 | 69539 | 0 | 41 | 30048.185933 | 30046.573149 |
| 19 | 3658 | 69539 | 1 | 43 | 60096.371866 | 60094.738398 |
| 19 | 3658 | 69539 | 2 | 45 | 120192.743732 | 120191.090519 |
| 19 | 3658 | 69539 | 3 | 47 | 240385.487464 | 240383.815366 |
| 19 | 3658 | 69539 | 4 | 49 | 480770.974928 | 480769.284732 |
| 23 | 58 | 1361 | 0 | 35 | 568.661889 | 567.117821 |
| 23 | 58 | 1361 | 1 | 37 | 1137.323778 | 1135.755576 |
| 23 | 58 | 1361 | 2 | 39 | 2274.647556 | 2273.056491 |
| 23 | 58 | 1361 | 3 | 41 | 4549.295112 | 4547.682328 |
| 23 | 58 | 1361 | 4 | 43 | 9098.590224 | 9096.956756 |

## 4. 三分流

| behavior | route | reason |
| --- | --- | --- |
| 试图停在固定有限 CRT 周期 | `impossible` | 新右端素数层无界加入，有限周期不含这些素层。 |
| 新素层以固定相位模板持久复现 | `ColumnCRT/PDEC` | fresh endpoint 相位成为同一 formal unit。 |
| 级联只孤立出现 | `SAE` | 不能支撑无限反例链。 |
| 无 PDEC 的无界新素层 | `tail-sieve/H3-DSB/KLS` | 每个新素层只留下一个禁相位，回到尾段粗筛/短窗硬核。 |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| FreshEndpointAfterReplacement | `true` | `true` | 每次闭复合块复现后，右侧真实相邻素数 B_new 位于块外且大于旧全轮平移边界，因此是旧端点层之外的新素层。 | closed |
| NextFullWheelKillsFreshEndpoint | `true` | `true` | 一旦 B_new 被纳入下一阶全轮 M_{<=B_new}，下一次全轮复现会令 B_new 的复制点被自身整除。 | closed |
| LogModulusAtLeastDoublesPerEndpointCascade | `true` | `true` | 若 L_j=log M_j，则 B_{j+1}>M_j，故 L_{j+1}>=L_j+log B_{j+1}>2L_j。 | closed |
| ApertureOnlyLinearUnderReplacementDebt | `true` | `true` | 端点替换给出的强制孔径下界每阶只增加 2，因此与模数对数倍增形成容量尺度错位。 | closed |
| NoFiniteCRTPeriodTerminalStructure | `true` | `true` | 有限 CRT 周期只能含有限素层；端点级联要求无界新素端点加入，故不能作为无限反例链终端。 | closed as finite-period no-go |
| PersistentFreshEndpointPatternRoutesToPDECColumnCRT | `true` | `true` | 若新端点层仍以固定相位模板持久复现，则形成 fresh-endpoint ColumnCRT/PDEC formal unit。 | closed as router |
| SparseFreshEndpointCascadeRoutesToSAE | `true` | `true` | 若级联只在孤立窗口出现，则为 SAE 单窗原子。 | closed as router |
| NonPDECFreshLayerCascadeRoutesToTailSieveH3 | `true` | `true` | 若无界新素层不物化为 PDEC/ColumnCRT，则只剩每个新素层禁一个相位的 tail-sieve/H3-DSB/KLS 对象。 | tail-sieve/H3-DSB global input |
| GlobalRowColumnUnconditionalClosureReached | `false` | `false` | 本步排除有限 CRT 周期终端，不排斥全部 fresh-layer PDEC、SAE 与 tail-sieve/H3 出口。 | FreshEndpointLayerCascadeNoFiniteCRTPeriodOrPDECSAEH3TailSieve;GlobalFinalInputsStillOpen |

## 6. 最新剩余

```text
FreshEndpointLayerCascadeNoFiniteCRTPeriodOrPDECSAEH3TailSieve;GlobalFinalInputsStillOpen
```

本证书排除固定有限 CRT 周期终端；它没有排斥全部 fresh-layer PDEC/ColumnCRT、SAE 与 tail-sieve/H3 出口，
因此不构成行/列命题的全局无条件证明。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-q2-endpoint-replacement-aperture-growth-router.json` | `7a2c070b16c1642d4ffd1986ddca501aecf756f86223bab30cc397b4d88276e4` |
| `docs/monograph/prime-matrix-q2-carrier-stage-crt-asymmetry-router.json` | `6f8c7992da2fcdc0925902c500eb5f568601db52cda061b8c21b38d87becf914` |
| `docs/monograph/prime-matrix-cycle-debt-branch-replay-fresh-modulus-escalation-router.md` | `36b007c325ca47aca03bfe9e2a25c8410674958e519f0700c48c8b5b95fef7b2` |
| `docs/monograph/prime-matrix-cycle-debt-fresh-modulus-tail-sieve-bridge-router.md` | `66ee650567d9e1db1192127c141d30392936eec6b2c59ba3c70d0ca5bece4d4a` |
