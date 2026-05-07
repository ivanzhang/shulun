# Triad-A1 Tail 容量压力审计：Q=30030 -> Q=510510

**状态：** `tail_capacity_pressure_materialized`

本审计把每个 promoted fiber 的残余洞集交给同一 Tail CRT set-cover DP。容量/Hall 失败直接证明 fiber 死亡；高负载仍幸存的槽位则是 KL/PDEC 压力输入。

## 1. 审计语义

本层 promoted prime 为 `r=17`。对旧洞集 `H_Q(t)` 和 residue `b`：

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
| `base_multiplicity_json` | `c62dea9f85ebdf6fb69eb9870b0a4e4af89dd88ac696a2247b48dd22c4a4bbba` |
| `lift_multiplicity_json` | `400fadeec3a97b7cd6c22ed0bd5e1271c703ebda07ee074db7db549d43d9b4fd` |

## 3. 总表

- `consistency_mismatch_count=0`。

| P | tail primes | M_tail | slots | survival | deletion | cap-def dead | Hall dead | Hall uncert dead | avg load | avg survivor load | avg KL floor | max KL floor |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 19 | `[]` | 1 | 6120 | 0.0588235 | 0.941176 | 0.941176 | 0.941176 | 0 | n/a | n/a | 0 | 0 |
| 23 | `[19]` | 19 | 15912 | 0.162896 | 0.837104 | 0.837104 | 0.837104 | 0 | 1.83964 | 1 | 2.88991 | 2.94444 |

## 4. 按残余洞数分桶

### P=19

| residual holes | slots | survival | cap-def dead | Hall dead | completion mass | max completion | max simple cap | avg KL floor | max KL floor |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 360 | 1 | 0 | 0 | 360 | 1 | 0 | 0 | 0 |
| 1 | 5760 | 0 | 1 | 1 | 0 | 0 | 0 | n/a | 0 |

### P=23

| residual holes | slots | survival | cap-def dead | Hall dead | completion mass | max completion | max simple cap | avg KL floor | max KL floor |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 48 | 1 | 0 | 0 | 912 | 19 | 0 | 0 | 0 |
| 1 | 2544 | 1 | 0 | 0 | 2544 | 1 | 1 | 2.94444 | 2.94444 |
| 2 | 13320 | 0 | 1 | 1 | 0 | 0 | 1 | n/a | 0 |

## 5. 读法

若 `cap-def dead` 或 `Hall dead` 占主导，则 Tail 容量不足直接支付删除势。
若高残余洞数、高负载下仍有大量 `survival`，则正式质量被迫落入很小的 Tail 完成集合；
相对 Tail 均匀基准的单槽 KL 下界为 `log(M_tail/completion_count)`，因此进入 `NoDeletion-KL/PDEC/CleanKLS`。

本审计不声称终端闭合；它把 `OccupancySaturation` 的后续义务压成了可复用的 Tail set-cover 容量证书。
