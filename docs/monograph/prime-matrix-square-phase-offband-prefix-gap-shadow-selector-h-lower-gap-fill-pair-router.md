# Prime Matrix square-phase off-band prefix gap shadow selector H lower gap fill pair router

**状态：** `gap_fill_pairs_materialized_immediate_repair_current_sweep_global_bound_open`

本步把三次端点运动缺口都压成生成-填充二元组。当前扫描中每个缺口都由下一次 `ell` 首次激活立刻修复，且修复后活跃 `ell` 集合重新成为连续素数带；三个完整 pair key 互异，没有当前复现。全局剩余是证明 immediate repair 机制，或排斥持久 GapFillPair-PDEC。

```text
gap_pair_count=3
unique_gap_fill_pair_key_count=3
repeated_gap_fill_pair_key_count=0
all_gaps_are_next_activation_repairs=true
all_repairs_restore_exact_interval=true
max_activation_rank_delay=1
max_p_delay=80
row_column_unconditional_closed=false
```

## 1. 缺口生成-填充二元组

| gap ell | direction | generator | filler | rank delay | P delay | slot delta | residue delta | post-fill interval |
| ---: | --- | --- | --- | ---: | ---: | --- | ---: | ---: |
| 43 | `upper` | `2063:plus:47` | `2137:minus:43` | 1 | 74 | `db=21,du=8` | -12 | `true` |
| 31 | `lower` | `2687:minus:29` | `2767:plus:31` | 1 | 80 | `db=-13,du=-7` | -11 | `true` |
| 59 | `upper` | `3187:minus:61` | `3257:minus:59` | 1 | 70 | `db=58,du=23` | -3 | `true` |

## 2. PDEC 键

| gap ell | key |
| ---: | --- |
| 43 | `dir=upper|gen=47|gap=43|fill=43|sides=plus->minus|dp=74|db=21|du=8|dr=-12` |
| 31 | `dir=lower|gen=29|gap=31|fill=31|sides=minus->plus|dp=80|db=-13|du=-7|dr=-11` |
| 59 | `dir=upper|gen=61|gap=59|fill=59|sides=minus->minus|dp=70|db=58|du=23|dr=-3` |

## 3. 结构结论

- 当前缺口没有形成长链：所有缺口的激活序列延迟均为 1。
- 每次填充后立即恢复连续素数带，因此持久缺口若存在，必须破坏 immediate-repair 机制。
- 三个完整 pair key 当前互异；全局复现将进入显式 GapFillPair-PDEC。

## 4. 下一步

- 主攻：`ImmediateGapRepairBoundOrGapFillPairPDECExclusion`。
- 将 `rank delay=1` 的局部事实提升为端点跳跃的结构约束，或证明违反者必产生重复 pair key / SAE 稀疏化。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_gap_fill_pair_router.py` | `3eb5a8a6281bc61bd58a75306aeca9030c29e7ef2d42872a22fcc4a9564c44db` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-gap-ledger.json` | `49723eba352f20363d6be36712caf088dbebab1a89f2ed5707d7c0ce76a228e9` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json` | `abfda31e733d7c1e274ded997056cf5e55d39d555a72f4f8ca35ac689c62ae1e` |
