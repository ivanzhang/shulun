# Prime Matrix PDEC-CAP 持久有限签名统一路由器

**状态：** `persistent_signature_unified_to_pdec_columncrt_or_sc9_terminal_estimates_open`

持久 MFU 与固定壳低模持久已经统一：二者本质上都是同一 formal unit 上的有限签名正密度。ColumnCRT 位移、PDEC 对偶失败和口径不一致都已有吸收合同，所以它们不能作为新的平行终端。剩余自足硬点因此压成两项：`PersistentFiniteSignaturePDECColumnCRT` 的终端排斥，以及无持久且多壳平坦时的 `SelfContainedKuznetsovLSAtomSC9`。

## 1. 统一律

Persistent Gamma and fixed-shell low-mod persistence are the same kind of object after the common-variable rewrite. Both are positive-limsup mass on a finite signature inside one formal unit: a phase-bucket/tail-column signature for MFU, or a shell/displacement signature for fixed-shell persistence. If the signature persists, it must submit a same-formal-unit PDEC/ColumnCRT dual capacity certificate. If it does not persist, the mass is diffuse and has already been routed to deletion/NoDeletion-KL/CleanKLS, with the flat clean case named as SC-9. ColumnCRT is absorbed as displacement PDEC, PDEC dual failure is absorbed as cap refinement, and multiplicity mismatch is absorbed by formal-unit normalization. Hence the two previous persistent gates collapse to one terminal family: PersistentFiniteSignaturePDECColumnCRT, plus the separate flat SC-9 atom.

```text
Persistent Gamma / MFU
  => positive-limsup finite phase-bucket formal unit
  => same-set multi-bucket PDEC;

Fixed shell / finite shell packet
  => positive-limsup finite shell/displacement signature
  => displacement PDEC or ColumnCRT-as-PDEC;

formal-unit mismatch
  => weighted PDEC / quotient / reuse defect;

no persistent finite signature
  => diffuse deletion / NoDeletion-KL / CleanKLS;
  flat multishell clean => SelfContainedKuznetsovLSAtomSC9.
```

## 2. 汇总

- `persistent_signature_unification_closed=true`。
- `persistent_finite_signature_pdec_columncrt_closed=false`。
- `self_contained_sc9_closed=false`。
- `row_column_unconditional_closed=false`。
- `narrowest_next_hardpoint=PersistentFiniteSignaturePDECColumnCRT_OR_SelfContainedKuznetsovLSAtomSC9`。
- `open_final_gates=['PersistentFiniteSignaturePDECColumnCRT', 'SelfContainedKuznetsovLSAtomSC9']`。

## 3. 审查表

| gate | closed | blocks final | evidence | meaning |
| --- | --- | --- | --- | --- |
| `APSPositiveBranchIsFiniteSignature` | `true` | `false` | ['SameSetPDECDualComparisonForPersistentMFU', 'DiffuseCleanKLSDLSEstimateOrFiberDeletionNoDeletionKL'] | APS 投影塔的持久分支已经被定义为某个有限签名正 limsup 持久，而不是自由选择出口。 |
| `ForcedGammaFiniteSignatureMaterialized` | `true` | `false` | rows=48; min_margin=0.130733 | 当前 forced Gamma 的有限层 phase-bucket 签名已物化；超过 ambiguous 预算的持久质量必须进入 MFU/PDEC。 |
| `PositiveLimsupPDECInputsMaterialized` | `true` | `false` | signature_rows=40; route_counts={'FiniteSignaturePDECInputMaterialized': 40} | 正 limsup 有限签名已登记为同集 PDEC 输入行；剩余只是不等式 U_CRT<L_PDEC。 |
| `MFUFormalUnitProtocolRegistered` | `true` | `false` | Persistent Formal Unit / Distributed Payment dichotomy | 多桶对象只有在投影兼容且长期承担正质量时才是 formal unit；否则进入分散 CleanKLS/DLS。 |
| `FixedShellIsFiniteShellSignature` | `true` | `false` | FixedShellLowModPersistencePDECOrColumnCRT_OR_SelfContainedKuznetsovLSAtomSC9 | 固定壳或有限壳包正密度等价于同一壳号变量上的有限 shell signature 持久。 |
| `ColumnCRTAbsorbedAsDisplacementPDEC` | `true` | `false` | ColumnCRT => displacement PDEC / SAE / quotient | 固定壳若表现为列位移持久，不是独立终端，而是 displacement PDEC 或合法商后的 primitive PDEC。 |
| `PDECFailureAbsorbsCaps` | `true` | `false` | dual failure => cap concentration => refined PDEC/ColumnCRT/SAE/MS | 持久有限签名的对偶失败只能产生帽集中并回流 PDEC family；它不能生成新的低模黑箱。 |
| `MultiplicitySameFormalUnitAbsorbed` | `true` | `false` | WeightedDualIndependence / CoordinateQuotient / ReuseDefect | 若 MFU、固定壳、ColumnCRT 使用的口径不一致，必须先规范化到同一 formal unit 或回流复用缺陷。 |
| `PersistentFiniteSignatureUnificationClosed` | `true` | `false` | persistent MFU and fixed-shell low-mod persistence share finite-signature formal-unit grammar | 持久 Gamma 与固定壳低模持久不再是两个平行无名硬点；二者统一为同一 formal unit 上的有限签名 PDEC/ColumnCRT 终端证书。 |
| `PersistentFiniteSignaturePDECColumnCRT` | `false` | `true` | terminal U_CRT<L_PDEC or displacement PDEC exclusion not submitted | 仍需证明所有持久有限签名 formal unit 的 PDEC/ColumnCRT 对偶容量排斥。 |
| `SelfContainedKuznetsovLSAtomSC9` | `false` | `true` | flat multishell clean atom remains open | 没有持久有限签名且多壳频率平坦时，自足版仍需证明 SC-9 谱大筛原子。 |

## 4. 剩余

本路由器关闭的是“持久 MFU”和“固定壳低模持久”之间的平行分支膨胀。它不证明 `U_CRT<L_PDEC`，也不证明 SC-9。下一步应直接攻 `PersistentFiniteSignaturePDECColumnCRT` 的同 formal unit 容量证书，或攻 flat multishell clean residual 的 `SC-9` 自足谱原子。
