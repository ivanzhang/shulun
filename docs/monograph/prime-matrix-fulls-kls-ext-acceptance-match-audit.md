# Prime Matrix FullS-KLS-ext 外部引理接受匹配审计

**状态：** `fulls_kls_ext_strict_match_accepted_external_math_lane_closed_rankin_open`

FullS-KLS-ext 与当前 non-AP full-S WFD 终端目标严格匹配：对象、相位、尺度、权重、强度和无中心化/无投影边界都逐项对齐。按用户允许的外部黑箱口径，可以接受该合同，并关闭 noncanonical full-S 外部数学 lane。但这不是 DI/BFI 原文逐项推出；无黑箱版本仍需 DIBFIPrimarySourceSpecializationProof 或新证明。完整行/列无条件闭合仍差 DStructure/Rankin 独立验收。

```text
strict_contract_match=true
accepted_as_external_blackbox_input=true
external_math_lane_closed_after_acceptance=true
primary_source_derivation_closed=false
dstructure_rankin_independent_acceptance_completed=false
row_column_unconditional_closed=false
```

## 1. 外部引理具体内容

- `object`: W_full(C,S,H)=sum_{c~C} lambda_c sum_{0<|h|<=H} omega_h sum_{s~S,(s,c)=1} beta_s e_c(a_h s + b_h bar{s})
- `range`: X≈P^2, C≈P/log^O P, S≈P, 0<|h|<=H<=P/log^O P, Q<=P log^O P
- `weights`: lambda well-factorable, beta divisor-bounded, omega smooth
- `strength`: |W_full(C,S,H)| <= NaturalWFDScale(C,S,H)/log^A P for every A>0
- `loss_budget`: dyadic/gcd/smoothing/endpoint losses absorbed by B(A)
- `boundary`: no AP-source lift, no canonical import, no hidden centering/projection

## 2. 接受后的输入基

```text
AcceptFullSKLSExtExternalContract AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 3. 严格匹配表

| item | required by target | external lemma clause | match | caveat |
| --- | --- | --- | --- | --- |
| `对象` | 当前 non-AP、未中心化、无投影 WFD 窗口。 | Theorem 直接估计 W_full(C,S,H)，并声明不插入中心化、不投影到 AP/canonical 对象。 | `true` | 匹配的是外部合同对象；若不用外部合同，内部仍需证明对象恒等式。 |
| `相位` | CRT 相位必须为 e_c(a_h s + b_h bar{s})。 | 适配条件显式列出 phase: CRT 相位归一化为 e_c(a_h s + b_h bar{s})。 | `true` | 最终稿仍应保持符号与 KE-13/共同变量表一致。 |
| `尺度` | X≈P^2, C≈P/log^O P, S≈P, 0<\|h\|<=H<=P/log^O P。 | Theorem FullS-KLS-ext 逐项列出同一 full-S 窗口。 | `true` | 该条作为外部定理合同吸收 DI J-scale 代入；不是 DI 原文逐项证明。 |
| `权重` | lambda well-factorable, beta divisor-bounded, omega smooth。 | Theorem 条款逐项列出 lambda_c、beta_s、omega_h。 | `true` | lambda 不能替换为 canonical RIW/Buchstab 支撑权。 |
| `变量一致性` | X,Q,N,M,C,S,H,lambda,beta,omega,A,B(A) 必须共用同一表。 | 共同变量表已物化，FullS-KLS-ext 使用同一 C,S,H 和 log-saving 预算。 | `true` | 变量表完成不等于内部 scale certificate 已证明；外部合同可直接吸收该证书。 |
| `强度` | 输出必须是 NaturalWFDScale/log^A P，且 A 任意。 | Theorem 给出 \|W_full\| <= NaturalWFDScale(C,S,H)/log^A P。 | `true` | 所有 dyadic/gcd/smoothing/endpoint 损失由 B(A) 吸收。 |
| `终端输入` | 外部无黑箱路线的原子必须正是 FullSNonAPWFDKLSTheoremInput。 | NewFullSTheoremInput 已压成 FullSNonAPWFDKLSTheoremInput。 | `true` | 这说明合同命题与剩余外部原子同名同对象。 |
| `外部合同状态` | 若作为黑箱外部定理接受，应关闭 noncanonical full-S 数学 lane。 | specialization router 标记 external theorem contract closed。 | `true` | 接受合同不等于完成 DIBFIPrimarySourceSpecializationProof。 |

## 4. 接受后仍剩

- `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`

## 5. 自足路线剩余

- ActualNoncanonicalCleanCoreMovingAtomExclusion
- or ActualNoncanonicalExactUVSupportLowerBound plus registered multiplier discipline

## 6. 判定

可以接受的是 `FullS-KLS-ext` 作为外部黑箱定理输入；不能把它写成已经从 DI/BFI 原文逐项推出。接受后外部数学 lane 闭合，但完整行/列命题仍需 DStructure/Rankin 独立验收。
