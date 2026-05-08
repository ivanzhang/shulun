# Prime Matrix 对齐一素主分支缺陷路由器

**状态：** `aligned_prime_main_reduced_to_lowmod_tail_defect_exclusions`

本步把 `UniformBuchstabOnePrimeBranchLowerBound` 从模型常数问题改写为精确缺陷二分：若某个对齐行的一素分支为零，它就是 EDA 失败行；EDA-BK 已迫使该行产生正主项端点缺陷，并进入 LowMod endpoint CRTDefect 或 Tail/Core concentration。因此 Buchstab 常数本身不是终局证明，真正剩余是排斥这两个命名出口。

```text
prime_free_row_to_edabk_defect_closed=true
buchstab_constants_standalone_rejected=true
lowmod_tail_defect_exclusions_closed=false
row_column_unconditional_closed=false
terminal_gap_after_router=LowModTailCoreDefectExclusionPackage
```

## 1. 精确二分链

```text
PrimeSurvivors_x=0
=> EDA failure at the same aligned row x
=> positive-main endpoint defect by EDA-BK
=> LowMod endpoint CRTDefect OR Tail/Core concentration
=> named PDEC/SAE/ColumnCRT/Tail-anchor exits; no unnamed Buchstab exit
```

这说明当前硬点不能继续写成“Buchstab 常数应为正”。正主项为正只说明若行为空，必须有端点缺陷或尾项集中；
它本身不排斥这些缺陷。

## 2. 判定表

| gate | closed | proved | meaning | output |
| --- | --- | --- | --- | --- |
| `VariableRowDimensionGapImported` | `true` | `true` | 上一轮已证明 PrimeSurvivors_x=G_x(P)-B_x(P)。 | `一素主分支为零就是变量行维数差失败。` |
| `PrimeFreeRowImpliesEDAFailure` | `true` | `true` | 若 sqrt(P)<=x<P 且 PrimeSurvivors_x=0，则该 P 对齐行没有素数，正是 EDA 失败行。 | `可直接调用 EDA-BK endpoint defect dichotomy。` |
| `PositiveMainEndpointDefectImported` | `true` | `true` | EDA-BK 已证明任一失败行给出正主项端点缺陷，并二分为 LowMod 或 Tail。 | `LowMod endpoint CRTDefect or Tail/Core concentration。` |
| `BuchstabConstantsNotStandalone` | `true` | `true` | 普通 Buchstab/Brun/Selberg 常数只给模型主项；在 H=P,z=P 时普通下界筛 level 不足。 | `不能把 UniformBuchstabConstants 当成独立闭合证明。` |
| `BKDECBridgeCompatibility` | `true` | `true` | BPN-BK 链条已把大端点 sawtooth 缺陷桥接到 Directed Endpoint CRTDefect。 | `LowMod 分支可接 PDEC/SAE/DEC 审稿门。` |
| `TailCoreBucketCompatibility` | `true` | `true` | 大尾项失败已定位为 TailCoreBucket/CoreK-Density，再进入 Tail-anchor 或 distributed corridor。 | `Tail/Core 分支不再是自由误差。` |
| `DirectedEndpointDefectSchema` | `true` | `true` | DEC/OSPC 文档已给出有向端点 CRT 缺陷的 schema；但 schema 不是排斥。 | `DirectedEndpointCRTDefectPDECSAEExclusion remains open。` |
| `LowModAndTailExclusion` | `false` | `false` | 尚未证明 LowMod endpoint CRTDefect 与 Tail/Core concentration 均不可持续或必被 SAE/PDEC 排除。 | `LowModEndpointCRTDefectExclusion AND TailCoreConcentrationAbsorption。` |

## 3. 审稿边界

已闭合的是从一素分支为零到命名缺陷出口的路由：

```text
Prime-free aligned row => LowMod endpoint CRTDefect OR Tail/Core concentration.
```

未闭合的是出口排斥：

```text
LowMod endpoint CRTDefect cannot persist / is PDEC-excluded;
Tail/Core concentration is absorbed by Tail-anchor, Rankin ledger, or PDEC/SAE;
single-window sparse escapes are SAE-excluded;
fixed column displacement reuse is PDEC-excluded.
```

## 4. 新最窄剩余

```text
LowModTailCoreDefectExclusionPackage
  = LowModEndpointCRTDefectExclusionOrPDEC
    AND TailCoreConcentrationAbsorptionOrTailAnchorPDEC
    AND SparseSingleWindowSAEExclusion
    AND ColumnDisplacementReusePDEC
    AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance.
```

这一步仍不是无条件闭合；它把“证明一素分支正性”的任务改写为两个命名出口的排斥任务。
