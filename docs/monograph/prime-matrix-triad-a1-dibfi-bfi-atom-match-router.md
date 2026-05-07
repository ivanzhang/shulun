# Triad-A1 DI/BFI BFI 原子匹配路由器

**状态：** `dibfi_direct_bfi_atom_match_reduced_to_ap_identity_and_level_ledger_open`

直接 BFI 原子匹配被压成两个终端硬点：`OriginalResidualEqualsBFIAPError` 与 `BFILevelExponentLedger`。权重类别与 Type 分解账本已关闭；剩余不是 DI/J-scale，而是 AP 源对象等式和 BFI level 指数账本。

## 1. 结构律

Direct BFI no longer asks for KE-13 no-projection or DI J-scale. The remaining BFI atom match has exactly two independent contents: first, the original residual must equal the BFI prime-AP discrepancy before Cauchy/dispersion; second, the X,Q and lambda support levels must be quantified against BFI Theorem 10.

```text
previous:
  DIBFIDirectBFIAPAtomMatchOrKE13NoProjection;

new terminal:
  BFIAPResidualIdentityAndLevelLedger;

open terminal targets:
  ['OriginalResidualEqualsBFIAPError', 'BFILevelExponentLedger'].
```

## 2. 汇总

- `bfi_atom_match_closed=false`。
- `open_gates=['PrimeAPResidualRepresentation', 'BFILevelSubstitution', 'WellFactorableLambdaLevel']`。
- `open_terminal_targets=['OriginalResidualEqualsBFIAPError', 'BFILevelExponentLedger']`。
- `terminal_gap_after_router=BFIAPResidualIdentityAndLevelLedger`。

## 3. 门控表

| gate | status | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- | --- |
| `BFIAtomPinned` | `closed` | `true` | BFI1987-Theorem10 已由定理定位路由固定，直接 BFI 原子可用。 | none | `none` |
| `APErrorFormulaNamed` | `formula_available_not_source_identification` | `true` | E_AP(X,Q)=sum_{q<=Q} lambda_q sum_{nm≈X} a_n b_m Delta_q(nm) | 公式已命名；仍需证明当前残差等于该对象。 | `OriginalResidualEqualsBFIAPError` |
| `PrimeAPResidualRepresentation` | `open_main_object_identity` | `false` | 共同变量表只给 APError 接口，尚未给 clean A1 残差到该接口的逐项等式。 | 必须从原始行/triad clean 残差出发写出 E_AP(X,Q) 的等号，而不是从 KE-13 子窗口倒推。 | `OriginalResidualEqualsBFIAPError` |
| `TypeDecompositionToBFIInput` | `closed_conditioned_on_ap_identity` | `true` | KZ-E spine 已登记 Vaughan/Heath-Brown、Type-I/II、dyadic 与 well-factorable 账本。 | 该行只说明 AP 对象一旦建立，可进入 BFI 的 Type/dispersion 框架。 | `none` |
| `WellFactorableLambdaClass` | `closed_at_weight_class_level` | `true` | generic WFD 合同与共同变量表均登记 lambda 为 BFI well-factorable 权重类别。 | 权重类别已闭合；数值 level 与 q-support 仍属 BFILevelExponentLedger。 | `BFILevelExponentLedger` |
| `BFILevelSubstitution` | `open_exponent_and_support_ledger_missing` | `false` | 当前文档只有 Q<=X^(4/7-eps) 的目标语句，尚未给出 X,Q 的原始参数等式。 | 需提交 X、Q、q-support、dyadic loss 的显式不等式账本。 | `BFILevelExponentLedger` |
| `WellFactorableLambdaLevel` | `open_level_not_class` | `false` | lambda 的 well-factorable 类别已登记，但支撑 level 与 BFI 定理输入仍未量化。 | 需证明 lambda_q 的 support level、factorization depth 与 BFI Theorem 10 的 level 条件一致。 | `BFILevelExponentLedger` |

## 4. 终端表

| terminal | covers | closed | meaning |
| --- | --- | --- | --- |
| `OriginalResidualEqualsBFIAPError` | PrimeAPResidualRepresentation | `false` | 证明当前 clean A1/generic WFD 残差在进入 Cauchy/dispersion 前就是 BFI prime-AP discrepancy 的 dyadic 总和。 |
| `BFILevelExponentLedger` | BFILevelSubstitution, WellFactorableLambdaLevel | `false` | 给出 X,Q 与 lambda_q support level 的显式指数账本，并核验 BFI Theorem 10 的 level/well-factorable 输入。 |

## 5. 当前结论

本步把直接 BFI 原子的三个门控进一步分层：

```text
closed ledger:
  BFIAtomPinned;
  APErrorFormulaNamed;
  TypeDecompositionToBFIInput;
  WellFactorableLambdaClass;

open core:
  OriginalResidualEqualsBFIAPError;
  BFILevelExponentLedger.
```

因此下一步应直接写 AP 源对象等式，或给出 BFI level 指数表；继续重证 DI/Kloosterman 不是当前外部 BFI 路线的最短路径。
