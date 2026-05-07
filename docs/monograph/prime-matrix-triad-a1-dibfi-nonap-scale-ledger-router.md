# Triad-A1 DI/BFI 非 AP-source scale ledger 路由器

**状态：** `nonap_scale_ledger_reduced_to_di_kloosterman_window_substitution_open`

非 AP-source 的尺度侧已压成 DI Kloosterman 窗口代入账本：BFI level、Type product、频率尾项与 log 损失不再是终端；剩余是 C/S/H 模数-逆元-频率窗口和 DI J-scale 的精确代入。

## 1. 结构律

The non-AP scale side no longer needs the BFI prime-AP level ledger: Q<=P log^O P and X≈P^2 give positive BFI exponent slack. Type product, frequency tail and log loss are also ledger-closed. The remaining scale content is specifically DI-side: match C,S,H and the J-scale term of DI Theorem 12 to the current WFD natural scale.

```text
previous terminal:
  DIBFIQuantifiedNoProjectionWindowCertificateForNonAPSource;

new scale terminal:
  DIKloostermanWindowSubstitutionLedger;

open scale gates:
  ['KLSModulusWindowQuantified', 'InverseVariableWindowQuantified', 'DIJScaleDominanceSubstitution'].
```

## 2. 汇总

- `quantified_window_substitution_closed=false`。
- `closed_scale_gates=['TypeProductQuantified', 'BFILevelQuantified', 'FrequencyWindowAndTail', 'LogLossAbsorption', 'TemplateHasAllVariables']`。
- `open_scale_gates=['KLSModulusWindowQuantified', 'InverseVariableWindowQuantified', 'DIJScaleDominanceSubstitution']`。
- `terminal_gap_after_router=DIKloostermanWindowSubstitutionLedger`。

## 3. 尺度账本表

| gate | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- |
| `TypeProductQuantified` | `true` | N*M≈X 已由 transfer-scale 证书按 dyadic product 关闭。 | none | `none` |
| `BFILevelQuantified` | `true` | 同一 X≈P^2、Q<=P log^O P 账本给 Q<=X^{1/2+o(1)}<X^{4/7-eps}。 | none | `none` |
| `FrequencyWindowAndTail` | `true` | transfer-scale 证书已把 Fourier tail 和 B(A) 吸收关闭。 | h 作为 DI 频率参数的精确范围仍并入 DIKloostermanWindowSubstitution。 | `DIKloostermanWindowSubstitutionLedger` |
| `LogLossAbsorption` | `true` | B(A)=A+C0+10 的 symbolic log ledger 已关闭。 | 若最终稿要求显式 C_i，再抽常数；当前非终端。 | `none` |
| `KLSModulusWindowQuantified` | `false` | C≈P/log^{O(1)}P 已命名，但尚未逐项代入 DI Theorem 12 的模数变量。 | 需把 C 与 DI 模数 family、dyadic support 和 gcd 剥离后的 level 精确同一化。 | `DIKloostermanWindowSubstitutionLedger` |
| `InverseVariableWindowQuantified` | `false` | S≈P / completion length 已命名，但尚未与 DI 逆元变量窗口逐项匹配。 | 需从 completion 后的 s 变量长度推出 DI Theorem 12 允许范围。 | `DIKloostermanWindowSubstitutionLedger` |
| `DIJScaleDominanceSubstitution` | `false` | C,S,H,N,M,Q 已在共同变量表中固定，但 DI J-scale bound 尚未代入并压到自然 WFD 尺度/log^A。 | 需写出 DI Theorem 12 的 J-scale 项，并逐项比较到 WFD 自然尺度。 | `DIKloostermanWindowSubstitutionLedger` |
| `TemplateHasAllVariables` | `true` | KLS 模板与 KZ-E spine 已给 C,S,H 的定性窗口；共同变量表固定 C,S,H。 | 该行只是资料可用性，不关闭 DI 精确代入。 | `DIKloostermanWindowSubstitutionLedger` |

## 4. 当前结论

尺度侧的最窄剩余为：

```text
DIKloostermanWindowSubstitutionLedger:
  KLSModulusWindowQuantified;
  InverseVariableWindowQuantified;
  DIJScaleDominanceSubstitution.
```

对象侧仍另有 `NoProjectionUncenteredDispersionIdentity`；二者合取才可关闭非 AP-source fallback。
