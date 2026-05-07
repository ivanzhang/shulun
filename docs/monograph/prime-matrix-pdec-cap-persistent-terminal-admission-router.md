# Prime Matrix PDEC-CAP 持久终端准入路由器

**状态：** `persistent_terminal_reduced_to_primitive_multiatom_pdec_certificate`

`PersistentFiniteSignaturePDECColumnCRT` 已被压到准入门：不能以裸持久签名、列位移、对偶失败或多重口径作为终端。当前已物化 primitive 非二点候选为零；未来只有通过同 formal unit、去重后三点以上、非二点 tautology、未被 SAE/Endpoint 吸收的对象，才是真正剩余的 `PrimitiveMultiAtomSameFormalUnitPDECCertificate`。

## 1. 准入律

PersistentFiniteSignaturePDECColumnCRT is not admitted as a raw label. Before it can be a terminal certificate, ColumnCRT must be converted into displacement PDEC or SAE, dual failure must be converted into cap refinement or SAE, and multiplicity mismatch must be normalized to one formal unit. The current materialized primitive frontier has no non-tautological candidate. Therefore the remaining global family is exactly: primitive multi-atom same-formal-unit PDEC certificates, each requiring U_CRT<L_PDEC on the same bad-window count function.

```text
PersistentFiniteSignaturePDECColumnCRT
  => normalize formal unit;
  => absorb ColumnCRT as displacement/primitive PDEC or SAE;
  => absorb dual failure as cap refinement / SAE / ColumnCRT;
  => remove multiplicity and two-point tautology;
  => admitted terminal only if primitive multi-atom same-formal-unit PDEC.
```

## 2. 汇总

- `persistent_terminal_admission_boundary_closed=true`。
- `current_materialized_persistent_terminal_instances_closed=true`。
- `primitive_multiatom_same_formal_unit_pdec_closed=false`。
- `row_column_unconditional_closed=false`。
- `narrowest_next_hardpoint=PrimitiveMultiAtomSameFormalUnitPDECCertificate`。
- `open_final_gates=['PrimitiveMultiAtomSameFormalUnitPDECCertificate']`。

## 3. 审查表

| gate | closed | blocks final | evidence | meaning |
| --- | --- | --- | --- | --- |
| `PersistentTerminalIsActive` | `true` | `false` | PersistentFiniteSignaturePDECColumnCRT | SC-9 调和后，当前 PDEC-CAP 只剩持久有限签名 PDEC/ColumnCRT 终端。 |
| `PDECCertificateContractRegistered` | `true` | `false` | formal unit / signature group / U_CRT<L_PDEC | 任何持久终端必须先提交同 formal unit 的 PDEC 证书字段，而不是裸 Fourier 常数。 |
| `ColumnCRTAbsorbedBeforeAdmission` | `true` | `false` | ColumnCRT => displacement PDEC / SAE / primitive quotient | 列位移持久不会作为独立终端准入；它先改写为 displacement/primitive PDEC 或 SAE。 |
| `PDECDualFailureAbsorbedBeforeAdmission` | `true` | `false` | dual failure => cap localization / refined PDEC / ColumnCRT / SAE | 对偶失败不是准入对象；它必须先输出 cap 细化、ColumnCRT、SAE 或口径义务。 |
| `MultiplicityNormalizedBeforeAdmission` | `true` | `false` | weighted PDEC / quotient primitive PDEC / reuse defect | 多重或拼接口径不一致必须先规范化为同 formal unit，或回流复用缺陷。 |
| `CurrentMaterializedPrimitiveCandidatesExhausted` | `true` | `false` | count=0 | 当前已物化 primitive 非二点 PDEC 候选为零；二点 tautology 与 SAE/Endpoint 已吸收。 |
| `PrimitiveMultiAtomAdmissionBoundaryDerived` | `true` | `false` | same formal unit + >=3 physical primitive atoms + non-tautological + not SAE | 未来真正可进入终端的对象只能是 primitive 多原子同集 PDEC 证书。 |
| `PrimitiveMultiAtomSameFormalUnitPDECCertificate` | `false` | `true` | global U_CRT<L_PDEC for every admitted primitive multi-atom formal unit not submitted | 剩余全球硬点是证明所有准入后的 primitive 多原子同 formal unit PDEC 满足容量排斥。 |

## 4. 未来准入要求

- `same formal unit and one fixed phase map`
- `at least three physical primitive atoms after all quotients`
- `not a two-point Fourier tautology`
- `not a ColumnCRT displacement before absorption`
- `not a cap-refinement failure before no-cycle processing`
- `not absorbed by LocalSurvivor/SAE/Endpoint`

## 5. 剩余

本路由器关闭的是持久终端的准入边界和当前已物化实例，不关闭全局 PDEC family。下一步硬点是对所有准入后的 primitive 多原子同 formal unit 证明 `U_CRT<L_PDEC`，或给出失败时的 cap/SAE/ColumnCRT 回流证书。
