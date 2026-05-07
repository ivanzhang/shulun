# Prime Matrix PDEC-CAP 有限弧横向路由器

**状态：** `finite_arc_cap_bounds_reduced_to_transverse_expansion`

有限循环弧 cap 质量界已被拆成横向结构：低横向支撑回 `SAE/ColumnCRT/固定壳PDEC`，横向偏斜持久回 refined PDEC，横向平坦分散进入 `CleanKLS/DLS` 或外部大筛输入。因此最新最窄剩余是高质量有限弧内的统一横向纤维扩张估计。

## 1. 横向分裂律

A finite cyclic-arc cap is a rank-one slice of the finite signature space. If a high-mass arc has low transverse support, it is sparse/SAE, fixed-shell PDEC, ColumnCRT, or Hall deletion. If the transverse bias persists, the arc indicator becomes a refined PDEC signature, and fixed-level refinement has no cycle. If neither happens, the cap mass is genuinely transverse and flat, so the branch is a CleanKLS/DLS or external large-sieve input. Hence finite arc caps have no unnamed exit; the remaining estimate is transverse fiber expansion.

```text
FiniteCyclicArcCapMassBoundsForRankTwoPrimitiveKernels
  finite cyclic arc = rank-one character slice;
  low transverse support
    => SAE / ColumnCRT / fixed-shell PDEC / Hall deletion;
  persistent transverse bias
    => refined PDEC, no fixed-level cap cycle;
  transverse flat dispersion
    => CleanKLS/DLS or external large-sieve input;
  remaining:
    TransverseFiberExpansionForFiniteArcCaps.
```

## 2. 汇总

- `finite_arc_no_unnamed_exit_closed=true`。
- `transverse_fiber_expansion_closed=false`。
- `row_column_unconditional_closed=false`。
- `narrowest_next_hardpoint=TransverseFiberExpansionForFiniteArcCaps`。
- `open_final_gates=['TransverseFiberExpansionForFiniteArcCaps']`。

## 3. 审查表

| gate | closed | blocks final | evidence | meaning |
| --- | --- | --- | --- | --- |
| `FiniteArcCapBoundsActive` | `true` | `false` | FiniteCyclicArcCapMassBoundsForRankTwoPrimitiveKernels | 上一层已把连续帽稳定压成有限循环弧 cap 质量界。 |
| `FiniteArcIsRankOneSlice` | `true` | `false` | character arc preimage | 每个有限循环弧 cap 是一个非平凡字符方向上的秩一薄片，横向变量仍可被审查。 |
| `LowTransverseSupportRoutesNamed` | `true` | `false` | CapSparse / CapColumn / fixed-shell / Hall deletion | 若高质量弧只由低横向支撑或固定壳承担，则进入 SAE、ColumnCRT、固定壳 PDEC 或容量/Hall 删除。 |
| `PersistentTransverseBiasRoutesToRefinedPDEC` | `true` | `false` | CapPersistent + finite cap no-cycle | 若弧内横向偏斜持久，就把弧指标并入签名，得到 refined PDEC；固定层细化不能无限循环。 |
| `FlatTransverseDispersionRoutesToClean` | `true` | `false` | Flat => CleanKLS/DLS admission | 若弧内既无低横向支撑也无持久偏斜，则剩余是横向平坦分散输入，进入 CleanKLS/DLS 或已登记外部输入。 |
| `FiniteArcNoUnnamedExit` | `true` | `false` | low support / persistent bias / flat transverse dispersion | 有限循环弧 cap 没有第四类出口；剩余只是真正横向扩张或平坦大筛估计。 |
| `TransverseFiberExpansionForFiniteArcCaps` | `false` | `true` | uniform transverse expansion or clean large-sieve estimate not submitted | 剩余全球硬点是在每个高质量有限弧内证明横向纤维扩张不足以支持反例，或把失败送入命名 PDEC/SAE/ColumnCRT/CleanKLS。 |

## 4. 剩余

下一步直接攻 `TransverseFiberExpansionForFiniteArcCaps`：对每个高质量有限字符弧，证明弧内横向纤维无法同时保持 primitive 二秩、同 formal unit、cap-stable 和足够质量；若证明失败，必须输出 `SAE/refined PDEC/ColumnCRT/CleanKLS` 回流证书。
