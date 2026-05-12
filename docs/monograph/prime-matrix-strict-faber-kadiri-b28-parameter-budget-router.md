# Prime Matrix strict Faber-Kadiri b0=28 参数包与预算证书

**状态：** `faber_kadiri_corrected_b28_budget_closed_high_tail_replacement_closed`

Faber-Kadiri 校正版 b0=28 参数包已经给出比旧 Table 6.3 更强的高尾输入：`epsilon0` 约为 1.2618e-5，并可外向舍入为 0.00001262。这小于旧表值 0.00002224，也小于 `1/36260`，即使额外保留端点税 `14/e^28` 仍有明显余量。因此旧 Table 6.3 b=28 的原始生成算法虽未取得，但当前命题需要的 psi 高尾输入可由 FK 平滑核路线闭合。

```text
faber_kadiri_corrected_b28_parameter_packet_closed=true
faber_kadiri_b28_directed_rounding_and_hash_closed=true
table63_b28_theorem_needed_high_tail_replacement_closed=true
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 参数包

| field | value |
| --- | ---: |
| `b0` | `28` |
| `m` | `2` |
| `delta` | `0.000004` |
| `sigma0` | `0.89` |
| `H` | `30610046000` |
| `T0` | `1132491` |
| `T1` | `1132492` |
| `s0` | `11.637732` |
| `R0` | `5.69693` |
| `a1` | `0.137` |
| `a2` | `0.443` |
| `a3` | `1.588` |
| `c1` | `0.4617` |
| `c2` | `0.6644` |
| `c3` | `-340272` |

## 2. 预算结果

| field | value |
| --- | ---: |
| `epsilon_plus` | `0.0000126176152601915665105243845052283711331741889267373185783209873290876625103192168012688873` |
| `epsilon_minus` | `0.0000126175652660568421415646099172490530576401606300331388459429310219251688102087976227666620` |
| `epsilon0_max` | `0.0000126176152601915665105243845052283711331741889267373185783209873290876625103192168012688873` |
| `directed_epsilon_upper` | `0.00001262` |
| `published_table63_epsilon_psi_28` | `0.00002224` |
| `target_1_over_36260` | `0.0000275785990071704357418643132928847214561500275785990071704357418643132928847214561500275786` |
| `endpoint_tax_14_over_e28` | `9.68016014971628421317761852223797297965413821488452679870226640631531210695472683808585229E-12` |
| `margin_to_published_table63_epsilon` | `0.0000096223847398084334894756154947716288668258110732626814216790126709123374896807831987311127` |
| `margin_to_target_1_over_36260` | `0.0000149609837469788692313399287876563503229758386518616885921147545352256303744022393487586913` |
| `margin_to_target_after_endpoint_tax` | `0.0000149609740668187195150557156100378280850028589977234737075879558329592240590901323940318532` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只补假设反例链可调用的 psi 高尾输入，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `FaberKadiriB28ParameterPacketGateActive` | `true` | `true` | 上一证书已把旧 Table 6.3 核缺口压成 Faber-Kadiri b0=28 校正版参数包。 | FaberKadiriCorrectedB28ParameterPacketAndBudgetLedger |
| `FaberKadiriSmoothedExplicitFormulaKernelConventionLedger` | `true` | `true` | Faber-Kadiri 光滑核 convention 已定位：普通 psi 由 S^- 与 S^+ 夹住。 | FaberKadiriSmoothedExplicitFormulaKernelConventionLedger |
| `CorrectedFormulaParameterPacketDeclared` | `true` | `true` | 采用 corrigendum 公式，参数为 b0=28、m=2、delta=4.0e-6、sigma0=0.89、Platt H、T1=T0+1。 | parameter packet fixed |
| `CorrectedB28BudgetBeatsPublishedTable63` | `true` | `true` | 计算得 epsilon0 < 1.262e-5，强于旧 Table 6.3 的 epsilon_psi(28)=2.224e-5。 | epsilon0 <= 0.00001262 < 0.00002224 |
| `CorrectedB28BudgetBeatsP51HighTailTarget` | `true` | `true` | 即使保留上一层端点税，0.00001262+14/e^28 仍小于 1/36260。 | psi high-tail target closed with explicit surplus |
| `FaberKadiriB28DirectedRoundingAndComputationHashLedger` | `true` | `true` | 本脚本用固定参数、解析 m=2 的 M(a,b,2) 积分和 Decimal 预算写出可复现 hash，并外向舍入到 0.00001262。 | be73023a58b97352516c440ebc8745ba17a4ff9ceed64e30d75e193344265cfc |
| `FaberKadiriCorrectedB28ParameterPacketAndBudgetLedger` | `true` | `true` | Faber-Kadiri 替代路线的 b0=28 参数包与预算闭合；旧表原始生成算法仍未取得，但定理所需高尾输入已有更强替代。 | Table63B28TheoremNeededHighTailPsiUpperReplacementLedger |
| `Table63B28KernelTruncationAndSmoothingConventionLedger` | `true` | `true` | 通过外部 FK 平滑核替代路线，Table 6.3 b=28 的核/截断/平滑缺口对当前高尾目标已关闭。 | FaberKadiriSmoothedExplicitFormulaKernelConventionLedger AND FaberKadiriCorrectedB28ParameterPacketAndBudgetLedger AND FaberKadiriB28DirectedRoundingAndComputationHashLedger |
| `Table63B28TheoremNeededHighTailPsiUpperReplacementLedger` | `true` | `true` | 对所有 x>=e^28，外部 FK 校正版公式给出 \|psi(x)-x\|/x <= 0.00001262，从而 psi(x)-x<x/36260。 | high-tail replacement closed |
| `RowColumnUnconditionalClosed` | `false` | `false` | 该步关闭的是 psi 高尾外部输入，不直接产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 预算 Hash

```text
be73023a58b97352516c440ebc8745ba17a4ff9ceed64e30d75e193344265cfc
```

## 5. 下一最窄点

```text
Table63B28HighTailInputToDusartP51SpliceSyncLedger
```

