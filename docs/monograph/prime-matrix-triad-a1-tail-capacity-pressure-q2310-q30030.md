# Triad-A1 Tail 容量压力审计：Q=2310 -> Q=30030

**状态：** `tail_capacity_pressure_materialized`

本审计把每个 promoted fiber 的残余洞集交给同一 Tail CRT set-cover DP。容量/Hall 失败直接证明 fiber 死亡；高负载仍幸存的槽位则是 KL/PDEC 压力输入。

## 1. 审计语义

本层 promoted prime 为 `r=13`。对旧洞集 `H_Q(t)` 和 residue `b`：

```text
R_b(H)={c in H_Q(t): ((t+bQ-1)P+c)=0 mod r}
Residual_b=H_Q(t)\R_b(H)
b 幸存 <=> Tail_{>r} 能完成 Residual_b
```

审计对每个 `(t,b)` 重新调用同一 `high_completion_stats`，并校验它与 lift 层 `M(t+bQ)` 一致。

## 2. 来源指纹

| source | sha256 |
| --- | --- |
| `tail_capacity_pressure_script` | `12340f0f0d2b3369f2fc5e9870462f7c3dcbc6606b5678ff5a9205bb282f29f5` |
| `capacity_script` | `6b00cd84807501d7a1f228aef5f24c23642a55caf56e7a6f957ef63ba8fcc568` |
| `base_multiplicity_json` | `5bcfa7c286e716b3b626c312becf303fee3b9d72142aaa30be63f849cb21162d` |
| `lift_multiplicity_json` | `c62dea9f85ebdf6fb69eb9870b0a4e4af89dd88ac696a2247b48dd22c4a4bbba` |

## 3. 总表

- `consistency_mismatch_count=0`。

| P | tail primes | M_tail | slots | survival | deletion | cap-def dead | Hall dead | Hall uncert dead | avg load | avg survivor load | avg KL floor | max KL floor |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 17 | `[]` | 1 | 364 | 0.0769231 | 0.923077 | 0.923077 | 0.923077 | 0 | n/a | n/a | 0 | 0 |
| 19 | `[17]` | 17 | 1820 | 0.202198 | 0.797802 | 0.797802 | 0.797802 | 0 | 1.80132 | 1 | 2.77162 | 2.83321 |
| 23 | `[17, 19]` | 323 | 3016 | 0.310345 | 0.689655 | 0.689655 | 0.689655 | 0 | 1.33687 | 0.974359 | 4.93773 | 5.08451 |
| 29 | `[17, 19, 23]` | 7429 | 1950 | 0.312821 | 0.687179 | 0.687179 | 0.687179 | 0 | 1.25538 | 0.985792 | 6.99664 | 7.12139 |

## 4. 按残余洞数分桶

### P=17

| residual holes | slots | survival | cap-def dead | Hall dead | completion mass | max completion | max simple cap | avg KL floor | max KL floor |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 28 | 1 | 0 | 0 | 28 | 1 | 0 | 0 | 0 |
| 1 | 336 | 0 | 1 | 1 | 0 | 0 | 0 | n/a | 0 |

### P=19

| residual holes | slots | survival | cap-def dead | Hall dead | completion mass | max completion | max simple cap | avg KL floor | max KL floor |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 8 | 1 | 0 | 0 | 136 | 17 | 0 | 0 | 0 |
| 1 | 360 | 1 | 0 | 0 | 360 | 1 | 1 | 2.83321 | 2.83321 |
| 2 | 1452 | 0 | 1 | 1 | 0 | 0 | 1 | n/a | 0 |

### P=23

| residual holes | slots | survival | cap-def dead | Hall dead | completion mass | max completion | max simple cap | avg KL floor | max KL floor |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 48 | 1 | 0 | 0 | 1680 | 35 | 2 | 2.2223 | 2.2223 |
| 2 | 888 | 1 | 0 | 0 | 1776 | 2 | 2 | 5.08451 | 5.08451 |
| 3 | 2080 | 0 | 1 | 1 | 0 | 0 | 2 | n/a | 0 |

### P=29

| residual holes | slots | survival | cap-def dead | Hall dead | completion mass | max completion | max simple cap | avg KL floor | max KL floor |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | 26 | 1 | 0 | 0 | 2912 | 112 | 3 | 4.19465 | 4.19465 |
| 3 | 584 | 1 | 0 | 0 | 3504 | 6 | 3 | 7.12139 | 7.12139 |
| 4 | 1160 | 0 | 1 | 1 | 0 | 0 | 3 | n/a | 0 |
| 5 | 180 | 0 | 1 | 1 | 0 | 0 | 3 | n/a | 0 |

## 5. 读法

若 `cap-def dead` 或 `Hall dead` 占主导，则 Tail 容量不足直接支付删除势。
若高残余洞数、高负载下仍有大量 `survival`，则正式质量被迫落入很小的 Tail 完成集合；
相对 Tail 均匀基准的单槽 KL 下界为 `log(M_tail/completion_count)`，因此进入 `NoDeletion-KL/PDEC/CleanKLS`。

本审计不声称终端闭合；它把 `OccupancySaturation` 的后续义务压成了可复用的 Tail set-cover 容量证书。
