# Prime Matrix registered capacity multiplier discipline 路由器

**状态：** `registered_capacity_multiplier_discipline_closed_exact_uv_support_open`

容量乘子纪律已作为账本门闭合：Type 分解、dyadic、CRT、Fourier 尾项、gcd、平滑、full-S completion fiber 与 tail-label 成本都已登记为同一 formal unit 中的 log-power 乘子。本步没有调用外部 DI/BFI 无投影相消，也没有证明支撑下界。因此完全自足源核心剩余从两个微输入压成单个 `ActualNoncanonicalExactUVSupportLowerBound`，另加 DStructure/Rankin 独立验收。

```text
registered_capacity_multiplier_discipline_closed=true
exact_uv_support_proved=false
actual_final_capacity_antiatom_proved=false
dstructure_rankin_independent_acceptance_completed=false
row_column_unconditional_closed=false
```

## 1. 主判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreviousMicroatomPinned` | `true` | `true` | 上一层已把支撑-only 偷换排除，并命名乘子纪律微输入。 | 可直接审查该乘子纪律是否只是账本门。 |
| `KnownMultipliersRegistered` | `true` | `true` | Type、dyadic、CRT、Fourier、gcd、smoothing、completion 与 tail-label 乘子均有同 formal-unit 登记行。 | 无账外乘子；所有成本并入最终 M_{u,v} 或 log-loss 指数 E。 |
| `ExternalNoProjectionNotUsed` | `true` | `true` | 本步只关闭内部乘子账本，不调用外部 DI/BFI 无投影相消。 | 外部 theorem-match 分支仍按原状态开放，不能被本步偷渡关闭。 |
| `MultiplierDisciplineClosed` | `true` | `true` | 所有已知 Type/Fourier/fiber 成本都成为最终容量测度的登记乘子，并统一受 log^E 控制。 | 若要推出 final anti-atom，现在只缺 actual exact u/v 支撑下界。 |
| `ExactUVSupportStillOpen` | `true` | `false` | ExactUVSupport 仍未证明，且不能由 K4/K6 或朴素 incidence 推出。 | 证明 actual noncanonical exact u/v 支撑下界，或直接证明 final capacity anti-atom。 |
| `DStructureRankinStillIndependent` | `true` | `false` | DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。 | 完整行/列定理仍需独立验收。 |

## 2. 乘子登记表

| source | registered | bound | evidence | role |
| --- | --- | --- | --- | --- |
| Type/Vaughan-Heath-Brown/dyadic | `true` | `log^C` | TypeDecompositionLogBudget + TypeProductQuantified | 分解层数和 dyadic 求和进入同一 formal unit 的 log-loss 账本。 |
| CRT phase normalization | `true` | `1` | CRTPhaseSymbolUnification | 相位归一化是恒等式，不产生容量乘子。 |
| Fourier h-window and tail | `true` | `log^C` | FrequencyWindowAndTail | 非零频窗口与尾项截断由 B(A) 吸收，不允许账外频率质量。 |
| coefficient/gcd/endpoint/smoothing | `true` | `log^C` | LogLossC0Extraction | 系数、gcd、端点和平滑损失统一进入符号化 C0。 |
| full-S completion fiber | `true` | `log^C` | CompletionRatioPolylogPinned | completion fiber 长度为 S/c=log^O(P)，是登记乘子而非新相消输入。 |
| balanced factorization shape | `true` | `shape-only` | BalancedFactorizationPinned | c=uv 与 U,V=C^{1/2}log^O 固定同一个 moving pair 坐标。 |
| dyadic/tail-label bookkeeping | `true` | `log^C` | K6DyadicBookkeeping available polylog split count | K6 不能证明支撑下界，但足以说明尾标签数量是已登记 log 乘子。 |

## 3. 最新输入基

上一层：

```text
ActualFinalCapacityAntiAtomLedgerForNoncanonicalFullS AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

当前：

```text
ActualNoncanonicalExactUVSupportLowerBound AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 乘子纪律律

Type/Fourier/fiber 乘子纪律是账本门而不是新的相消定理：所有已知乘子已经在同一个 actual formal unit 中登记，并被统一吸收到最终 M_{u,v} 的 log^E 成本里。本步不使用外部 DI/BFI no-projection 证明。

## 5. 支撑推出反原子的剩余阈值

乘子纪律闭合后，若证明 actual exact u/v 支撑满足 S_u*S_v >= L^(2A+4C+E)，则 final capacity anti-atom max M_{u,v}/sum M_{u,v} <= L^(-2A) 立即成立。

| k | log y | A | C | E | required power | required pair support |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 3 | 6.90776 | 2.0 | 2.0 | 5.0 | 17.0 | 185664143359702 |
| 4 | 9.21034 | 2.0 | 2.0 | 5.0 | 17.0 | 24699408928878996 |
| 5 | 11.5129 | 2.0 | 2.0 | 5.0 | 17.0 | 1096874099498946944 |
| 6 | 13.8155 | 2.0 | 2.0 | 5.0 | 17.0 | 24335370598442758144 |
| 7 | 16.1181 | 2.0 | 2.0 | 5.0 | 17.0 | 334451684862452432896 |
| 8 | 18.4207 | 2.0 | 2.0 | 5.0 | 17.0 | 3237400927126027763712 |
| 9 | 20.7233 | 2.0 | 2.0 | 5.0 | 17.0 | 23976697736727197908992 |

## 6. 当前结论

本步闭合的是 `RegisteredCapacityMultiplierDiscipline`：所有已知 Type/Fourier/fiber 成本均已登记为 log-power 乘子。
它不证明 `ExactUVSupport`，也不关闭外部 DI/BFI no-projection 分支。
完全自足源核心的真正剩余现在是 `ActualNoncanonicalExactUVSupportLowerBound`，另加 DStructure/Rankin 独立验收。
