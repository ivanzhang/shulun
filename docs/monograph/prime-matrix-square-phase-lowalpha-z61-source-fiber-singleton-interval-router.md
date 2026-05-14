# Prime Matrix square-phase low-alpha z=61 源纤维 singleton interval

**状态：** `z61_source_fiber_ladder_reduced_to_singleton_interval_gate_open`

三条 PrefixGate 源纤维均由同一个 singleton interval gate 产生：`a=floor(p^2/(bq))+1`，且 `0<abq-p^2<p`。所有 `a` 区间宽度都小于 `1`，实际最大仅约 `0.048834`；因此剩余硬点可改写为这些短窗 singleton 残基门的有符号计数平衡，或登记 Interval-PDEC。

```text
all_source_fibers_are_singleton_interval_gates=true
max_a_interval_width=0.048834
positive_singleton_interval_count=2
negative_singleton_interval_count=1
row_column_unconditional_closed=false
```

## 1. Singleton Interval

| quotient | sign | p | q | a | b | width | left/p | right/p | n interval |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | `negative` | 36739 | 53 | 883 | 28842 | 0.024034 | 0.616157 | 0.383843 | `[46799, 46799]` |
| 2 | `positive` | 200003 | 71 | 9767 | 57684 | 0.048834 | 0.867882 | 0.132118 | `[693454, 693457]` |
| 4 | `positive` | 200003 | 37 | 9371 | 115368 | 0.046854 | 0.002635 | 0.997365 | `[346727, 346728]` |

## 2. 证明边界

- 已闭合：singleton 源纤维到短窗 interval gate 的样本恒等式。
- 未闭合：短窗残基门的有符号计数平衡，或 Interval-PDEC 排斥。
- 下一目标：`SingletonIntervalResidueGateBalanceOrIntervalPDEC`。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-prefix-gate-source-fiber-router.json` | `3d7220fa3e430a443bee11837833f2ecb06a5ebde3c2bf5d6856024924e9e86e` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_source_fiber_singleton_interval_router.py` | `9852a112a724f13489cbaab29eae84aad7edeac987535f7178e562480bd6151f` |
