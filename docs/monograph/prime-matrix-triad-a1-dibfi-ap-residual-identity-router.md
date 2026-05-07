# Triad-A1 DI/BFI AP 残差源等式路由器

**状态：** `ap_residual_identity_reduced_to_upstream_source_definition_open`

唯一剩余 AP 对象等式被压成源头定义合同：必须证明原始 clean A1 残差在进入 Cauchy/dispersion 前就是 BFI prime-AP discrepancy 的 dyadic 总和。不能从 KE-13/WFD 下游窗口倒推该等式；若源头等式失败，直接 BFI 路线必须退回 fallback。

## 1. 结构律

OriginalResidualEqualsBFIAPError is a source-level identity, not a downstream Kloosterman-window estimate. The AP formula, WFD-core, phase normalization and level ledger are all available, but they do not prove that the clean A1 residual before Cauchy/dispersion is exactly the BFI prime-AP discrepancy. That equality must be written at the upstream definition layer, including Delta_q main term, lambda_q, dyadic weights, endpoint losses and coefficient provenance.

```text
previous terminal:
  OriginalResidualEqualsBFIAPError;

new terminal:
  UpstreamCleanA1APSourceDefinition;

open gates:
  ['UpstreamCleanA1ResidualDefinition', 'MainTermAndCoefficientMatch'].
```

## 2. 汇总

- `ap_residual_identity_closed=false`。
- `open_gates=['UpstreamCleanA1ResidualDefinition', 'MainTermAndCoefficientMatch']`。
- `terminal_gap_after_router=UpstreamCleanA1APSourceDefinition`。

## 3. 对象等式门控表

| gate | status | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- | --- |
| `APErrorFormulaAvailable` | `closed_formula_only` | `true` | E_AP(X,Q)=sum_{q<=Q} lambda_q sum_{nm≈X} a_n b_m Delta_q(nm) | 公式已命名，但不等于源对象等式。 | `none` |
| `DownstreamWFDObjectIdentified` | `closed_as_diagnostic_not_identity` | `true` | KZ-E spine 与 generic WFD 合同锁定当前下游对象为未中心化 WFD/KE-13 核。 | 这只能说明下游对象是什么，不能从下游反推出 AP 源等式。 | `UpstreamCleanA1APSourceDefinition` |
| `NoDownstreamBackProjectionShortcut` | `closed_negative_shortcut_blocked` | `true` | SOURCE-CEN no-go 排除免费中心化/投影替换；下游 KE-13 不能自动替代原始 AP 残差。 | 必须从 Cauchy/dispersion 之前的原始残差定义写等式。 | `UpstreamCleanA1APSourceDefinition` |
| `TransferScaleAlreadyMarksAPRepresentationOpen` | `open_confirmed_by_previous_certificate` | `true` | open_transfer_gates=['APErrorRepresentation', 'DispersionCauchyNoCenteringIdentity', 'KE13DyadicExhaustionNoProjection'] | 上游证书明确把 APErrorRepresentation 作为未闭合项。 | `UpstreamCleanA1APSourceDefinition` |
| `UpstreamCleanA1ResidualDefinition` | `open_source_definition_missing` | `false` | 尚未找到 clean A1 原始残差在进入 Cauchy/dispersion 前等于 AP discrepancy 的逐项定义。 | 需给出 R_clean = dyadic sum of E_AP(X,Q) + acceptable endpoints 的源头等式。 | `UpstreamCleanA1APSourceDefinition` |
| `MainTermAndCoefficientMatch` | `open_delta_q_main_term_match_missing` | `false` | AP 公式中的 Delta_q(nm) 已命名，但主项扣除、残基类 a(q) 与 lambda_q 符号尚未逐项接到 clean A1 残差。 | 需核对主项、端点、dyadic 权、lambda_q 与 alpha/beta 系数完全同源。 | `UpstreamCleanA1APSourceDefinition` |

## 4. 当前结论

现在的终端硬点已经不能再写成泛泛的 BFI 适配问题，而是一个源头定义等式：

```text
UpstreamCleanA1APSourceDefinition:
  R_clean
  = sum_dyadic E_AP(X,Q; lambda_q, alpha, beta, Delta_q)
    + endpoint/log-budget errors.
```

这条等式必须出现在 Cauchy、dispersion、KE-13 和任何中心化/投影操作之前。
否则直接 BFI prime-AP 原子不可用，只能走 KE-13 无投影 fallback 或另写外部原始 dispersion 定理。
