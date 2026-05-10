# Prime Matrix strict DStructure/Tail-log4/Rankin 自足替代包压缩证书

**状态：** `self_contained_replacement_package_compressed_to_rks_log_reciprocal_kloosterman_core`

本轮把 `SelfContainedDStructureTailLog4FiniteRankinReplacementPackage` 继续压缩。finite Rankin 子账本已经由 manifest/data 与 batch pass-or-return 闭合；A/B 到 D 与 D 组结构壳也已附录化。Tail-log4 中，平滑端点和中谱大模数层已拆成可审查账本，真正未内联的数学核心只剩 `RKS-log`：倒数 Kloosterman/BG 型对数节省及相关 EXT 解析输入。新近闭合的 Burgess 乘法角色和不能替代它，因为 RKS-log 是加性倒数相位问题。因此当前唯一内部自足最窄点是证明 `SelfContainedRKSLogReciprocalKloostermanTailLog4Input`；行/列命题仍未无条件闭合。

```text
finite_rankin_replacement_closed=true
dstructure_formal_replacement_shell_closed=true
tail_log4_formal_decomposition_closed=true
rks_log_reciprocal_kloosterman_atom_isolated=true
rks_log_reciprocal_kloosterman_internalized=false
self_contained_dstructure_tail_log4_finite_rankin_replacement_package_proved=false
row_column_unconditional_closed=false
```

## 1. 替代包压缩

| field | value |
| --- | --- |
| `rankin` | full Rankin ledger and batch pass-or-return are closed; no longer the active internal obstruction |
| `dstructure` | A/B to D matching and D Structured-EHPD formal shell are present; remaining dependence is analytic EXT inputs |
| `tail_log4` | TL4 is split into smooth, middle, and low-spectrum/RKS-log branches |
| `tail_smooth` | TL4-S is elementary smoothing/endpoint bookkeeping and is closed in the formal appendix |
| `tail_mid` | TL4-M large-modulus layer is reduced to Selberg upper sieve plus averaged singular series ledger |
| `tail_low` | TL4-L is compressed to the RKS-log reciprocal Kloosterman log-saving theorem |
| `not_replaced` | EXT-BG/RKS-log and the external analytic input family are registered but not self-containedly proved here |

## 2. Burgess 不能替代 RKS-log

| field | value |
| --- | --- |
| `burgess_closed_object` | multiplicative character sums on intervals modulo P |
| `rks_log_object` | additive reciprocal Kloosterman sums e_P(xi/(mn)) with prime/dyadic variables |
| `orthogonality_mismatch` | multiplicative characters diagonalize product ratios; RKS-log needs additive trace/reciprocal phases |
| `consequence` | the newly closed Burgess/RKS23 character moment cannot be reused as a proof of TL4-L/RKS-log |

## 3. 当前前沿

| field | value |
| --- | --- |
| `current_internal_replacement_status` | replacement shell closed, analytic core open |
| `narrowest_math_atom` | SelfContainedRKSLogReciprocalKloostermanTailLog4Input |
| `supporting_external_family` | SelfContainedExternalAnalyticInputsForDStructureTailLog4 |
| `parallel_non_internal_route` | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `row_column_boundary` | false until either the self-contained analytic core is proved or the independent promotion gate is accepted |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ReplacementPackageTargetActive` | `true` | `true` | 上一证书已把唯一内部自足剩余指向 DStructure/Tail-log4/finite Rankin 替代包。 | SelfContainedDStructureTailLog4FiniteRankinReplacementPackage |
| `FiniteRankinReplacementClosed` | `true` | `true` | finite Rankin 子账本已有 manifest/data 与 batch pass-or-return，内部替代部分闭合。 | closed |
| `DStructureFormalReplacementShellClosed` | `true` | `true` | A/B 到 D 匹配与 D 组 OMR/CGTP/LSMP/FCT 正式接口已经形成作者侧证明壳。 | SelfContainedExternalAnalyticInputsForDStructureTailLog4 |
| `TailLog4FormalDecompositionClosed` | `true` | `true` | Tail-log4 已拆成 TL4-S、TL4-M、TL4-L/RKS-log 三个可审查分支。 | SelfContainedRKSLogReciprocalKloostermanTailLog4Input |
| `TailLog4SmoothAndMidLedgerCompressed` | `true` | `true` | 平滑端点账本闭合，大模数中谱层不再是独立黑箱。 | SelfContainedRKSLogReciprocalKloostermanTailLog4Input |
| `RKSLogReciprocalKloostermanAtomIsolated` | `true` | `true` | Tail-log4 低谱真正剩余已压成 RKS-log/BG 倒数 Kloosterman 对数节省。 | SelfContainedRKSLogReciprocalKloostermanTailLog4Input |
| `BurgessPointwiseDoesNotReplaceRKSLog` | `true` | `true` | Burgess 角色和处理乘法角色；RKS-log 是加性倒数相位，二者正交对象不同。 | SelfContainedRKSLogReciprocalKloostermanTailLog4Input |
| `SelfContainedRKSLogReciprocalKloostermanTailLog4Input` | `false` | `false` | 当前仓库尚未内联证明 BG/RKS-log 倒数 Kloosterman 对数节省。 | prove BG/RKS-log or exact self-contained replacement |
| `SelfContainedExternalAnalyticInputsForDStructureTailLog4` | `false` | `false` | EXT-KL/BG/Vaaler/Selberg/Vaughan 已登记引用，但没有全部改写成自足附录证明。 | internalize or explicitly keep as external theorem package |
| `SelfContainedDStructureTailLog4FiniteRankinReplacementPackage` | `false` | `false` | 替代包的形式壳已闭合，但解析核心未自足内联，因此替代包未完整证明。 | SelfContainedRKSLogReciprocalKloostermanTailLog4Input |
| `RowColumnUnconditionalClosed` | `false` | `false` | 最终行/列无条件闭合仍需自足证明解析核心，或走独立晋级接受事件。 | SelfContainedRKSLogReciprocalKloostermanTailLog4Input |

## 5. 下一唯一内部自足最窄点

```text
SelfContainedRKSLogReciprocalKloostermanTailLog4Input
```
