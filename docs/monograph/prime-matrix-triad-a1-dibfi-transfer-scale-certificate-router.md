# Triad-A1 DI/BFI 转移/尺度证书路由器

**状态：** `dibfi_transfer_scale_certificate_reduced_to_quantified_no_projection_certificate_open`

共同变量表的合取证书已被继续压缩：账本型行已经关闭，真正剩余不是新的统计实验，而是 `NoProjectionUncenteredDispersionIdentity` 与 `QuantifiedDIBFIWindowSubstitution` 两项合并证书。二者同时成立才可把 generic WFD 外部 DI/BFI 分支标记闭合。

## 1. 结构律

The common-variable certificate cannot be closed by another qualitative checklist. The local ledger rows split cleanly: Type decomposition, CRT phase, Fourier tail and symbolic log-loss absorption are closed at ledger level. The true remaining content is exactly twofold: an uncentered no-projection dispersion identity, and a quantified substitution of X,Q,N,M,C,S,H into BFI Theorem 10 and DI Theorem 12, including the DI J-scale dominance.

```text
previous:
  DIBFICommonVariableTransferScaleCertificate;

ledger rows closed:
  TypeDecompositionLogBudget;
  CRTPhaseSymbolUnification;
  FrequencyWindowAndTail;
  LogLossC0Extraction;

terminal:
  DIBFIQuantifiedNoProjectionWindowCertificate.
```

## 2. 汇总

- `all_transfer_closed=false`。
- `all_scale_closed=false`。
- `all_certificate_rows_closed=false`。
- `open_transfer_gates=['APErrorRepresentation', 'DispersionCauchyNoCenteringIdentity', 'KE13DyadicExhaustionNoProjection']`。
- `open_scale_gates=['BFILevelQuantified', 'KLSModulusWindowQuantified', 'InverseVariableWindowQuantified', 'DIJScaleDominanceSubstitution']`。
- `open_terminal_targets=['NoProjectionUncenteredDispersionIdentity', 'QuantifiedDIBFIWindowSubstitution']`。
- `terminal_gap_after_router=DIBFIQuantifiedNoProjectionWindowCertificate`。

## 3. 对象转移证书行

| gate | common step | status | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- | --- | --- |
| `APErrorRepresentation` | `APError` | `interface_named_but_exact_residual_identity_open` | `false` | E_AP(X,Q)=sum_{q<=Q} lambda_q sum_{nm≈X} a_n b_m Delta_q(nm) | 仍需把 clean A1 generic WFD 残差逐项写成该 AP error 或其 dyadic 总和。 | `APToUncenteredDispersionIdentity` |
| `TypeDecompositionLogBudget` | `TypeDecomposition` | `ledger_closed_conditioned_on_ap_error_identity` | `true` | KZ-E spine 已登记 Vaughan/Heath-Brown、Type-I/II 与 dyadic/log 账本。 | 该行只关闭分解账本；不替代 APErrorRepresentation。 | `none` |
| `DispersionCauchyNoCenteringIdentity` | `DispersionCauchy` | `open_no_centering_shortcut_available` | `false` | SOURCE-CEN 已反证，不能免费插入块中心化或删同块对角。 | 必须从 BFI 原始 dispersion 写出 Cauchy 展开到 KE-5 的逐项恒等式。 | `NoProjectionUncenteredDispersionIdentity` |
| `CRTPhaseSymbolUnification` | `CRTPhase` | `closed` | `true` | KZ-E 的 KE-8 与 KLS 模板的相位归一化同指向标准 e_c(a s+b bar{s})。 | 最终稿只需统一符号；不再是独立数学缺口。 | `none` |
| `KE13DyadicExhaustionNoProjection` | `KE13Identification` | `open_main_target_transfer_blocker` | `false` | E_disp main nonzero-frequency blocks = WFD_core(C,S,H,lambda,beta,omega) | 需证明所有 dyadic 主块完全覆盖，且没有额外中心化、投影、块对角删除或端点遗漏。 | `NoProjectionUncenteredDispersionIdentity` |

## 4. 尺度不等式证书行

| gate | common inequality | status | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- | --- | --- |
| `TypeProductQuantified` | `TypeProduct` | `closed_at_dyadic_product_level` | `true` | N*M≈X | N*M≈X 本身已是 Type 分块恒等式；仍不决定 Q,C,S,H 的外部定理范围。 | `none` |
| `BFILevelQuantified` | `BFILevel` | `open_exact_x_q_exponent_substitution_missing` | `false` | Q<=X^(4/7-eps) or an explicitly stronger admitted range | 需要给出 X、Q 与 prime-matrix 参数的显式关系，并代入 BFI Theorem 10 的 level 条件。 | `QuantifiedDIBFIWindowSubstitution` |
| `KLSModulusWindowQuantified` | `KLSModulusWindow` | `open_qualitative_range_only` | `false` | C is a dyadic sublevel of Q and matches the DI modulus family | 当前 C≈P/log^{O(1)}P 只是定性窗口，需匹配 DI/BFI 原文模数族与 dyadic level。 | `QuantifiedDIBFIWindowSubstitution` |
| `InverseVariableWindowQuantified` | `InverseVariableWindow` | `open_completion_length_substitution_missing` | `false` | S matches the DI inverse-variable length after completion | 需从 completion 后的 s 变量长度推出 DI 逆元变量窗口允许范围。 | `QuantifiedDIBFIWindowSubstitution` |
| `FrequencyWindowAndTail` | `FrequencyWindow` | `tail_ledger_closed_di_range_still_in_quantified_substitution` | `true` | 0<\|h\|<=H and Fourier tail is absorbed by B(A) | Fourier 尾项账本已关；h 作为 DI/BFI 频率参数的精确范围并入量化代入证书。 | `QuantifiedDIBFIWindowSubstitution` |
| `DIJScaleDominanceSubstitution` | `DIJScaleDominance` | `open_main_scale_blocker` | `false` | DI Theorem 12 J-scale bound is <= natural WFD scale/log^A after substitution | 需把 DI Theorem 12 的 J-scale 项逐项代入 C,S,H,N,M,Q，并证明小于 WFD 自然尺度/log^A。 | `QuantifiedDIBFIWindowSubstitution` |
| `LogLossC0Extraction` | `LogLossAbsorption` | `closed_symbolic_log_ledger` | `true` | B(A)=A+C0+10 absorbs dyadic, gcd, endpoint, coefficient and smoothing costs | C0 仍可保持符号化；若最终稿要求显式常数，再逐项抽取 C_i。 | `none` |

## 5. 终端目标

| terminal | covers | status | reason | closed |
| --- | --- | --- | --- | --- |
| `NoProjectionUncenteredDispersionIdentity` | APErrorRepresentation, DispersionCauchyNoCenteringIdentity, KE13DyadicExhaustionNoProjection | `open` | 对象转移仍必须证明原始未中心化目标在 BFI dispersion 展开中逐项保持。 | `false` |
| `QuantifiedDIBFIWindowSubstitution` | BFILevelQuantified, KLSModulusWindowQuantified, InverseVariableWindowQuantified, DIJScaleDominanceSubstitution | `open` | 尺度侧仍缺少把 X,Q,N,M,C,S,H 代入 BFI Theorem 10 与 DI Theorem 12 的逐项不等式。 | `false` |
| `ExternalWindowedKLSAlternative` | HLC-KLS-core / CORE-5 | `available_for_hlc_clean_branch_not_generic_wfd_certificate` | HLC clean 分支已有外部深定理适配；但当前 generic WFD 共同变量表仍要求原始未中心化对象与量化尺度的同表证书，不能直接替代。 | `true` |

## 6. 当前结论

这一轮没有把缺口继续横向拆散，而是把共同变量表上的剩余压成一个更小的合取证书：

```text
DIBFIQuantifiedNoProjectionWindowCertificate
  = NoProjectionUncenteredDispersionIdentity
    + QuantifiedDIBFIWindowSubstitution.
```

其中第一项是对象恒等式问题，第二项是原文定理尺度代入问题。二者未同时完成前，不能诚实宣称 generic WFD 外部 DI/BFI 分支已经闭合。
