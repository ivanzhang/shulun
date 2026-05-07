# Prime Matrix PDEC-CAP primitive 多原子秩边界路由器

**状态：** `primitive_multiatom_pdec_reduced_to_rank_two_cap_stable_kernel`

primitive 多原子同 formal unit PDEC 已不再作为黑箱终端保留。低秩退化、二点 Fourier tautology、固定壳/ColumnCRT、对偶 cap 失败和口径不一致都必须先回流到已命名路线。当前已物化 primitive 多原子实例仍为零；未来真正剩余只可能是二秩以上、cap-stable、同 formal unit 的 primitive PDEC 核不等式。该项没有证明完整行/列无条件定理。

## 1. 秩边界律

PrimitiveMultiAtomSameFormalUnitPDECCertificate is not admitted as a raw terminal label. After the same-formal-unit and same-set capacity protocol is fixed, quotient the physical primitive atoms by already registered duplicate, cross-chart, and two-point tautology relations. Rank 0 is non-primitive or reuse. Rank 1 is a one-dimensional shell/column/displacement signature and therefore routes to fixed-shell PDEC, ColumnCRT, or SAE; the current two-point case is already absorbed. If a higher-rank candidate fails U_CRT<L_PDEC, the dual-failure contract outputs a cap; sparse caps route to SAE, persistent caps to refined PDEC/ColumnCRT, and mismatched caps to multiplicity normalization. PDEC cap refinement has no fixed-level cycle. Therefore the only remaining kernel is rank at least two, cap-stable, same-formal-unit primitive PDEC.

```text
PrimitiveMultiAtomSameFormalUnitPDECCertificate
  => same formal unit and same-set capacity protocol;
  => quotient duplicate / cross-chart / two-point tautology;
  => rank 0: non-primitive or reuse defect;
  => rank 1: fixed shell / ColumnCRT / SAE / refined PDEC;
  => dual cap failure: SAE / refined PDEC / ColumnCRT / multiplicity;
  => no fixed-level cap cycle;
  => remaining terminal:
       RankTwoCapStablePrimitivePDECKernelInequality.
```

## 2. 汇总

- `primitive_multiatom_rank_boundary_closed=true`。
- `current_materialized_primitive_multiatom_instances_closed=true`。
- `primitive_rank_two_cap_stable_kernel_closed=false`。
- `row_column_unconditional_closed=false`。
- `narrowest_next_hardpoint=RankTwoCapStablePrimitivePDECKernelInequality`。
- `open_final_gates=['RankTwoCapStablePrimitivePDECKernelInequality']`。

## 3. 审查表

| gate | closed | blocks final | evidence | meaning |
| --- | --- | --- | --- | --- |
| `PrimitiveMultiAtomAdmissionGateActive` | `true` | `false` | PrimitiveMultiAtomSameFormalUnitPDECCertificate | 上一层已经证明裸持久签名不能直接作为终端，只能先进入 primitive 多原子同 formal unit 准入门。 |
| `SameFormalUnitCapacityProtocolRegistered` | `true` | `false` | formal unit + Same-Set Law + U_CRT<L_PDEC | 容量比较必须在同一 formal unit、同一坏窗计数函数和同一相位映射上进行。 |
| `DegenerateOneTwoAtomCasesAbsorbed` | `true` | `false` | current primitive candidate count=0; future admission requires >=3 atoms | 一原子、重复原子、物理二点 Fourier tautology 和当前二点 SAE/Endpoint 已不再是 PDEC 终端。 |
| `RankZeroOnePrimitiveBranchNamed` | `true` | `false` | duplicate / two-point / fixed-shell / ColumnCRT routes | 若去重后原子只生成零秩或一秩相位结构，它不是真正多原子核：只能回到重复口径、二点 tautology、固定壳 PDEC/ColumnCRT 或 SAE。 |
| `DualCapFailureAbsorbedBeforeTerminal` | `true` | `false` | CapSparse / CapPersistent / CapColumn / Multiplicity-Stitching | 任何尚未证明 U_CRT<L_PDEC 的方向，若失败，必须先输出帽集中并回流 SAE、refined PDEC、ColumnCRT 或口径规范化。 |
| `CapRefinementNoCycleBeforeTerminal` | `true` | `false` | finite Boolean algebra refinement or new-layer entropy dichotomy | 持久帽细化不能在固定签名群内无限循环；升层也必须命名为 new-layer PDEC 或 CleanKLS/DLS。 |
| `PrimitiveRankBoundaryDerived` | `true` | `false` | rank 0/1 and cap-failure exits removed before final kernel | primitive 多原子同 formal unit 终端已被规范化为低秩退化、cap 失败回流、或真正二秩以上 cap-stable 核三类。 |
| `RankTwoCapStablePrimitivePDECKernelInequality` | `false` | `true` | global U_CRT<L_PDEC for rank>=2 cap-stable primitive kernels not submitted | 剩余全球硬点是证明所有二秩以上且无可回流 cap 的 primitive 同 formal unit 核满足严格容量排斥。 |

## 4. 剩余

下一步不再攻击宽口径 `PrimitiveMultiAtomSameFormalUnitPDECCertificate`，而是直接攻击 `RankTwoCapStablePrimitivePDECKernelInequality`：对所有二秩以上、同 formal unit、且没有 SAE/refined PDEC/ColumnCRT/multiplicity 回流帽的 primitive 核，证明同一坏窗上的 `U_CRT<L_PDEC`。
