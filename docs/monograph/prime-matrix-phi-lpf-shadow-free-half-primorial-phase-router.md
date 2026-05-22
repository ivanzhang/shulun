# Prime Matrix Phi-LPF shadow-free half-primorial phase 证书

**状态：** `shadow_free_lane_reduced_to_half_primorial_special_phase_avoidance`

本层只处理上一层拆出的 shadow-free 子带。设

```text
M_half(P)=prod_{q<=P/2, q prime} q.
```

在条件 `4*((k+1)P-1)<=P^2` 下，two-prime shadow 为空。因此该行正性等价于

```text
exists 1<=t<P such that gcd(kP+t, M_half(P))=1.
```

并且任何这样的 survivor 自动是素数。换句话说，失败当且仅当特殊相位
`kP+1 mod M_half(P)` 启动了一个长度 `P-1` 的 half-primorial 低筛覆盖块。

## 1. 有限行相位审计

```text
max_prime=1009
audited_shadow_free_high_rows=0
all_shadow_free_high_rows_have_survivor=true
failure_count=0
minimum_survivor_count=None
finite_evidence_not_used_as_global_proof=true
```

最小 survivor 行样本：

```text
无
```

大尺度 shadow-free 交集样本：

```text
sample_seeds=[3000000, 5000000]
sample_count=6
all_sampled_rows_have_survivor=true
large_samples_are_evidence_not_global_proof=true
```

| P | k | high lower | free cap | survivors | first survivor | first prime checked |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 3000017 | 724862 | 724862 | 750003 | 105344 | 2174598322669 | `true` |
| 3000017 | 737432 | 724862 | 750003 | 105760 | 2212308536359 | `true` |
| 3000017 | 750003 | 724862 | 750003 | 106056 | 2250021750167 | `true` |
| 5000011 | 1150731 | 1150731 | 1250001 | 170776 | 5753667658051 | `true` |
| 5000011 | 1200366 | 1150731 | 1250001 | 170171 | 6001843204031 | `true` |
| 5000011 | 1250001 | 1150731 | 1250001 | 169983 | 6250018750021 | `true` |

## 2. 小 half-primorial 全周期扫描

```text
max_full_period_prime=43
profile_count=10
all_scanned_half_primorial_periods_have_max_run_less_than_P_minus_1=true
period_scan_is_small_and_not_global_proof=true
```

| P | cutoff | M_half | max covered run | P-1 | uniform closes | start mod M |
| ---: | ---: | ---: | ---: | ---: | --- | ---: |
| 11 | 5 | 30 | 5 | 10 | `true` | 2 |
| 13 | 6 | 30 | 5 | 12 | `true` | 2 |
| 17 | 8 | 210 | 9 | 16 | `true` | 2 |
| 19 | 9 | 210 | 9 | 18 | `true` | 2 |
| 23 | 11 | 2310 | 13 | 22 | `true` | 114 |
| 29 | 14 | 30030 | 21 | 28 | `true` | 9440 |
| 31 | 15 | 30030 | 21 | 30 | `true` | 9440 |
| 37 | 18 | 510510 | 25 | 36 | `true` | 217128 |
| 41 | 20 | 9699690 | 33 | 40 | `true` | 60044 |
| 43 | 21 | 9699690 | 33 | 42 | `true` | 60044 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ShadowFreeSurvivorEqualsHalfPrimorialCoprimeHit | `true` | `true` | 在 shadow-free 子带，R_half(P,k)>0 等价于区间 kP+1..kP+P-1 命中一个与 M_{<=P/2} 互素的 residue。 | exact equivalence |
| ShadowFreeSurvivorIsPrime | `true` | `true` | 由于整行低于 P^2/4，任意 q,m>P/2 的合成 shadow 不存在；half-rough survivor 必为素数。 | none |
| UniformHalfPrimorialJacobsthalWouldCloseShadowFreeLane | `true` | `true` | 若 half-primorial 周期中最大低筛覆盖块长度 < P-1，则所有 shadow-free 行自动闭合。 | needs uniform half-primorial bound |
| SpecialRowPhaseAvoidanceIdentified | `true` | `true` | 即使没有全周期 Jacobsthal 上界，也只需排斥特殊相位 kP+1 命中长度 P-1 覆盖块。 | HalfPrimorialSpecialPhaseAvoidsLongCoveredBlockOrPDEC |
| FiniteAuditSupportsButDoesNotProve | `true` | `true` | 有限行审计与小周期扫描均正常，但不作为全局证明。 | finite evidence only |
| ShadowFreeLaneClosedGlobally | `false` | `false` | 尚未证明 uniform half-primorial Jacobsthal bound 或特殊相位避让。 | HalfPrimorialSpecialPhaseAvoidsLongCoveredBlockOrPDEC |
| UnifiedPositiveCoreProved | `false` | `false` | 本层只把 shadow-free 子带压成半 primorial 特殊相位问题，不证明三目标命题。 | upper-band shadow excess still open |

## 4. 结论

shadow-free 子带的正性已经无损转为半 primorial 特殊相位避让：行失败当且仅当相位 kP+1 在 M_{<=P/2} 周期中启动一个长度 P-1 的低筛覆盖块。全周期 Jacobsthal 上界会立即闭合该子带；若全周期上界不可得，剩余就是特殊行相位避让或 PDEC。

当前 shadow-free 子带的最窄直接口是：

```text
HalfPrimorialSpecialPhaseAvoidsLongCoveredBlockOrPDEC
```

这仍不是最终闭合；upper-band 的 two-prime shadow excess 也仍然开放。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-strict-k-half-rough-shadow-band-split-router.json` | `9db4d90a17cdd1c8e1730e6b8d5d86caa454ea43951ddc4c3ce713a09acf373f` |
| `docs/monograph/prime-matrix-primorial-jacobsthal-central-block-router.json` | `35ae489251780714fd8168bb39108b636a4882d967acd642f4c24a6a046fbcfb` |
| `docs/monograph/prime-matrix-terminal-row-square-phase-bridge-router.json` | `328ee462d76cb6213f976eee33133885f20109157d16cf80d236ae27d78d8993` |
