# Prime Matrix square-phase low-alpha z=61 PrefixGate 源纤维

**状态：** `z61_quotient_ladder_reduced_to_singleton_prime_a_source_fibers_open`

PrefixGate quotient ladder 的三个相位命中均来自唯一 prime-a singleton 源纤维，且这些 `b` 都是 composite prime-b 失败点。负侧有一条源纤维，正侧有两条源纤维。因此 dyadic quotient count balance 可进一步改写为 singleton prime-a 源纤维配对/容量问题，或登记 Fiber-PDEC。

```text
source_fiber_count=3
all_quotient_hits_have_unique_singleton_prime_a_source=true
positive_source_fiber_count=2
negative_source_fiber_count=1
source_fiber_ladder_identity_closed=true
row_column_unconditional_closed=false
```

## 1. Singleton 源纤维

| quotient | sign | p | b | q | a | n | a interval | singleton |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | `negative` | 36739 | 28842 | 53 | 883 | 46799 | `[883, 883]` | true |
| 2 | `positive` | 200003 | 57684 | 71 | 9767 | 693457 | `[9767, 9767]` | true |
| 4 | `positive` | 200003 | 115368 | 37 | 9371 | 346727 | `[9371, 9371]` | true |

## 2. 证明边界

- 已闭合：quotient ladder 到 singleton prime-a 源纤维的样本恒等式。
- 未闭合：singleton 源纤维配对/容量全局证明，或 Fiber-PDEC 排斥。
- 下一目标：`SingletonPrimeAFiberLadderBalanceOrFiberPDEC`。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-prefix-gate-quotient-ladder-router.json` | `e643292f87a63f8164b083991c9166f865e6e1b499dc6a3a9817cf6fd9364387` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_prefix_gate_source_fiber_router.py` | `34c08c16ab705b114964a033c6985542e50e88f84790300a08fc99e1063d1baf` |
