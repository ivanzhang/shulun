# Prime Matrix PDEC-CAP 二秩 cap-stable 核路由器

**状态：** `ranktwo_capstable_kernel_inequality_reduced_to_uniform_cap_stability`

二秩 cap-stable primitive 核的不等式本身已被改写为 cap localization 的逆否命题：只要所有合法方向帽都低于阈值，就自动得到 `U_CRT<L_PDEC`；若某个方向帽达到阈值，该对象就不再是 cap-stable 核，而必须回流 `SAE/refined PDEC/ColumnCRT/multiplicity`。因此最新最窄剩余不是抽象核不等式，而是统一帽稳定证书。

## 1. Cap-stable 逆否律

For a rank-at-least-two primitive same-formal-unit PDEC kernel, fix one direction (h,zeta). The same-set LP computes U_CRT on the same count vector g. If U_CRT reaches L_PDEC, cap localization gives a direction cap C_alpha(h,zeta) with mass at least (L_PDEC-alpha M)/(1-alpha). Such a cap is not allowed to remain inside a cap-stable kernel: sparse caps route to SAE, persistent caps route to refined PDEC or ColumnCRT, and mismatched caps route to multiplicity normalization. Conversely, if every legal cap is certified below the corresponding threshold, then no direction can reach L_PDEC, hence U_CRT<L_PDEC for the kernel.

```text
RankTwoCapStablePrimitivePDECKernelInequality
  fix direction (h,zeta);
  if U_CRT(h,zeta) >= L_PDEC:
    cap localization gives C_alpha with mass >= (L-alpha M)/(1-alpha);
    this is SAE / refined PDEC / ColumnCRT / multiplicity;
    hence not cap-stable;
  therefore cap-stable + all legal caps below threshold => U_CRT<L_PDEC.

remaining:
  UniformCapStabilityCertificateForRankTwoPrimitiveKernels.
```

## 2. 汇总

- `ranktwo_capstable_kernel_inequality_closed=true`。
- `uniform_cap_stability_certificate_closed=false`。
- `row_column_unconditional_closed=false`。
- `narrowest_next_hardpoint=UniformCapStabilityCertificateForRankTwoPrimitiveKernels`。
- `open_final_gates=['UniformCapStabilityCertificateForRankTwoPrimitiveKernels']`。

## 3. 审查表

| gate | closed | blocks final | evidence | meaning |
| --- | --- | --- | --- | --- |
| `RankTwoCapStableKernelActive` | `true` | `false` | RankTwoCapStablePrimitivePDECKernelInequality | 上一层已把 primitive 多原子终端压成二秩以上且无可回流 cap 的核。 |
| `SameSetLPDirectionProtocolRegistered` | `true` | `false` | U_CRT(h,zeta;theta) over P_theta | 每个方向上界都必须在同一坏窗计数多面体 P_theta 上计算。 |
| `CapLocalizationThresholdRegistered` | `true` | `false` | g(C_alpha)>=(U-alpha M)/(1-alpha) | 若某方向线性泛函达到 L_PDEC，则存在对应方向帽的强质量下界。 |
| `CapFailureRoutesNamed` | `true` | `false` | SAE / refined PDEC / ColumnCRT / Multiplicity | 超过阈值的方向帽不能留在 cap-stable 核内，必须回流到已命名路线。 |
| `CapRefinementNoCycleRegistered` | `true` | `false` | finite Boolean algebra or new-layer entropy dichotomy | 持久帽细化不会产生同层无限循环；升层也进入命名 new-layer PDEC/CleanKLS。 |
| `PDECTerminalInterfaceRegistered` | `true` | `false` | terminal triad PDEC family contract | cap 失败只允许回到三终端合同中的 PDEC/SAE/CleanKLS 路线，不能形成第四出口。 |
| `RankTwoCapStableKernelInequalityByContrapositive` | `true` | `false` | if every legal cap is below threshold then every direction has U_CRT<L_PDEC | 二秩 cap-stable 核不等式本身由 cap localization 逆否命题闭合；真正难点转为证明统一帽稳定阈值。 |
| `UniformCapStabilityCertificateForRankTwoPrimitiveKernels` | `false` | `true` | global legal cap bounds for every rank>=2 primitive same-formal-unit kernel not submitted | 剩余全球硬点是为所有二秩以上 primitive 核提交合法方向帽上界，或输出命名 cap 回流证书。 |

## 4. 剩余

下一步直接攻 `UniformCapStabilityCertificateForRankTwoPrimitiveKernels`：对每个二秩以上 primitive 同 formal unit 核、每个合法方向 `(h,zeta)` 与阈值 `alpha`，证明方向帽质量低于 `(L_PDEC-alpha M)/(1-alpha)`，或输出 `SAE/refined PDEC/ColumnCRT/multiplicity` 回流证书。
