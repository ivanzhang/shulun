# Prime Matrix square-phase dyadic 一阶负载账本

**状态：** `dyadic_first_moment_and_overlap_ledger_materialized_defect_exclusion_open`

本账本在同一进入块幸存集 `S_z` 上同时物化 union 删除量、一阶负载和重叠质量。它显示每个 dyadic 过删都可以被精确分摊到一阶负载超额或重叠不足。当前仍是审计与对象固定，不是全局排斥证明。

```text
first_moment_ledger_materialized=true
first_moment_load_pdec_excluded=false
overlap_deficit_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. 全局极值

| item | P | block | union excess/sqrtP | first excess/sqrtP | overlap deficit/sqrtP |
| --- | ---: | --- | ---: | ---: | ---: |
| `worst_union` | 200003 | `(31744,63488]` | 0.680203 | 0.631417 | 0.048786 |
| `worst_first` | 200003 | `(31744,63488]` | 0.680203 | 0.631417 | 0.048786 |
| `worst_overlap` | 200003 | `(3968,7936]` | 0.004293 | -0.088695 | 0.092988 |

## 2. 每个 P 的最坏行

| P | y | worst union block | union excess/sqrtP | worst first block | first excess/sqrtP | worst overlap block | overlap deficit/sqrtP |
| ---: | ---: | --- | ---: | --- | ---: | --- | ---: |
| 10007 | 3681 | `(1984,3681]` | 0.230215 | `(1984,3681]` | 0.208002 | `(496,992]` | 0.044768 |
| 36739 | 13515 | `(3968,7936]` | 0.366819 | `(3968,7936]` | 0.327135 | `(1984,3968]` | 0.052834 |
| 83561 | 30740 | `(15872,30740]` | 0.511921 | `(15872,30740]` | 0.478402 | `(1984,3968]` | 0.078804 |
| 200003 | 73576 | `(31744,63488]` | 0.680203 | `(31744,63488]` | 0.631417 | `(3968,7936]` | 0.092988 |

## 3. 证明边界

已物化：

```text
U_B = union_delete(S_z,B)
H_B = sum_{q in B} |S_z cap {-P^2 mod q}|
overlap_mass = H_B-U_B
union_excess = first_excess + overlap_deficit
```

未闭合：

- `DyadicSquarePhaseFirstMomentLoadPDEC`：一阶负载超额的 Fourier/PDEC 排斥。
- `DyadicSquarePhaseOverlapDeficitOrPairCorrelationPDEC`：重叠不足或 pair-correlation 缺陷排斥。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-dyadic-deletion-excess-split-router.json` | `34770fe0730a11c7fc7346ce7eaad7a3b70d0a347f51ca8bbb683279322ab42e` |
| `docs/monograph/prime-matrix-square-phase-moving-cutoff-dyadic-defect-router.json` | `4515b50a029982ce414c9ef9b290c4dbf026bba67099c6048cb1979ced0891f6` |
| `experiments/prime_matrix_square_phase_dyadic_first_moment_ledger.py` | `29e201d10588b46eff3a9bb240b55ab53e33049876ebcd6252559aeae1f4c86f` |
