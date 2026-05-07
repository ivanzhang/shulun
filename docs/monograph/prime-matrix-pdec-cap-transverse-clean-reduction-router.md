# Prime Matrix PDEC-CAP 横向 clean 归约路由器

**状态：** `transverse_expansion_reduced_to_clean_large_sieve_atom`

横向纤维扩张已压成横向商上的 clean 大筛原子：非平坦横向缺陷全部回流命名出口，剩下的只能是 L2-flat clean residual。最新最窄剩余是 `TransverseQuotientCleanLargeSieveAtom`。

## 1. 横向 clean 归约律

Inside a high finite character arc, the arc condition is only rank one. A rank-at-least-two primitive kernel therefore leaves a transverse quotient. If that quotient has sparse support, persistent bias, or column/shell concentration, the branch is SAE, refined PDEC, or ColumnCRT. If none of those named transverse defects occurs, the residual is L2-flat in the transverse quotient and must enter the CleanKLS/DLS large-sieve atom, with the already registered SC-9/NC-BLK boundary.

```text
TransverseFiberExpansionForFiniteArcCaps
  finite arc fixes one character direction;
  rank>=2 primitive kernel leaves transverse quotient;
  transverse sparse/support defect => SAE;
  transverse persistent bias => refined PDEC;
  transverse shell/column concentration => ColumnCRT/PDEC;
  no transverse defect => L2-flat clean residual;
  remaining:
    TransverseQuotientCleanLargeSieveAtom.
```

## 2. 汇总

- `transverse_expansion_reduced_to_clean_atom=true`。
- `transverse_quotient_clean_large_sieve_closed=false`。
- `row_column_unconditional_closed=false`。
- `narrowest_next_hardpoint=TransverseQuotientCleanLargeSieveAtom`。
- `open_final_gates=['TransverseQuotientCleanLargeSieveAtom']`。

## 3. 审查表

| gate | closed | blocks final | evidence | meaning |
| --- | --- | --- | --- | --- |
| `TransverseExpansionActive` | `true` | `false` | TransverseFiberExpansionForFiniteArcCaps | 上一层已把有限弧 cap 质量界压成高质量弧内的横向纤维扩张估计。 |
| `RankOneArcLeavesTransverseQuotient` | `true` | `false` | finite arc is rank-one slice inside rank>=2 primitive kernel | 有限字符弧只钉住一个字符方向；二秩以上 primitive 核在弧内仍有非平凡横向商变量。 |
| `NonFlatTransverseRoutesNamed` | `true` | `false` | CapSparse / CapPersistent / CapColumn | 横向低支撑、横向持久偏斜或列/壳集中均已回流 SAE、refined PDEC 或 ColumnCRT。 |
| `TransverseFlatnessAdmitsCleanKLS` | `true` | `false` | K1-K9 clean admission + LargeSieve/DLS/KLS | 若横向所有命名偏斜都被剥离，剩余正是横向 L2-flat clean residual。 |
| `SC9BoundaryRegisteredForCleanResidual` | `true` | `false` | canonical SC-9 reconciled; generic external/not claimed | 横向 clean 原子必须遵守既有 SC-9/NC-BLK 边界，不能作为新的无名出口。 |
| `TransverseExpansionReducedToCleanAtom` | `true` | `false` | nonflat routes named; flat residual is clean large-sieve atom | 横向纤维扩张硬点已压成横向 clean 大筛原子或命名回流。 |
| `TransverseQuotientCleanLargeSieveAtom` | `false` | `true` | self-contained transverse clean large-sieve estimate not submitted | 剩余全球硬点是证明横向商上的 clean 大筛原子，或明确外部输入；不能把它误称为已闭合行列定理。 |

## 4. 剩余

下一步直接攻 `TransverseQuotientCleanLargeSieveAtom`：证明高质量有限弧的横向商在 K1--K9 clean admission 后满足内部大筛/DLS/KLS 界，或明确登记外部输入；若任一 clean admission 失败，必须回流 PDEC/SAE/ColumnCRT/Multiplicity。
