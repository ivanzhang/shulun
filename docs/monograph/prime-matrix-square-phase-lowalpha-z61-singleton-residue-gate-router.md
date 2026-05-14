# Prime Matrix square-phase low-alpha z=61 singleton residue gate

**状态：** `z61_singleton_interval_gate_reduced_to_short_residue_gate_open`

singleton interval gate 已等价改写为短残基门：每条源纤维满足 `p^2 ≡ -delta (mod bq)` 且 `0<delta<p`。因此剩余问题不再是区间宽度，而是这些短残基门的有符号计数平衡，或将持续残基偏斜登记为 Residue-PDEC。

```text
all_residue_gates_closed=true
all_short_delta_bounds_closed=true
positive_residue_gate_count=2
negative_residue_gate_count=1
row_column_unconditional_closed=false
```

## 1. 短残基门

| quotient | sign | p | bq | delta | residue | statement |
| ---: | --- | ---: | ---: | ---: | ---: | --- |
| 1 | `negative` | 36739 | 1528626 | 22637 | 1505989 | `p^2 ≡ 1505989 (mod 1528626)` |
| 2 | `positive` | 200003 | 4095564 | 173579 | 3921985 | `p^2 ≡ 3921985 (mod 4095564)` |
| 4 | `positive` | 200003 | 4268616 | 527 | 4268089 | `p^2 ≡ 4268089 (mod 4268616)` |

## 2. 证明边界

- 已闭合：singleton interval 到短残基门的等价。
- 未闭合：短残基门的有符号计数平衡，或 Residue-PDEC 排斥。
- 下一目标：`SingletonResidueGateSignedCountBalanceOrResiduePDEC`。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-source-fiber-singleton-interval-router.json` | `aecc57280136fb8f2bee303ab38ca4ca52c942bc840f17bb2f2c1f6e725a4a76` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_singleton_residue_gate_router.py` | `e6fcedaa0304625a420acd4c990fcdcb2fc40c6e3995bfd8a1c4984e47029e8a` |
