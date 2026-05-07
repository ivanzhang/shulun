# Triad-A1 DI/BFI full-S completion reduction 路由器

**状态：** `full_s_nonap_wfd_kls_input_reduced_to_modulus_dependent_completed_kls_open`

`FullSNonAPWFDKLSTheoremInput` 已被完成分解压成 `ModulusDependentCompletedFullSKLSInput`：full-S 长度可按模 c 完成，真正剩余是处理依赖 c 的 residue 权重 B_{c,x} 的完整 Kloosterman 平均定理。

## 1. 结构律

Because S≈P while C≈P/log^O P, the full-S inverse window contains only polylog many complete residue blocks modulo each c. Thus the incomplete s-window itself is no longer the sharp obstruction: it can be completed algebraically. The obstruction moves to the completed residue weights B_{c,x}, which depend on c and are not flat for generic divisor-bounded beta_s. Therefore the remaining theorem input is a modulus-dependent completed Kloosterman average, not a vague full-S estimate.

```text
previous terminal:
  FullSNonAPWFDKLSTheoremInput;

new terminal:
  ModulusDependentCompletedFullSKLSInput;

expansion:
  ['ModulusDependentCompletedFullSKLSInput'].
```

## 2. 完成公式

- `residue_weight=B_{c,x}=sum_{k: x+k*c in S-block} beta_{x+k*c} W((x+k*c)/S)`。
- `completed_sum=sum_{c~C} lambda_c sum_{0<|h|<=H} omega_h sum_{x mod c}^* B_{c,x} e_c(a_h*x+b_h*bar{x})`。
- `block_count=L_c=S/c=log^O(P)`。

## 3. 汇总

- `full_s_completion_reduction_closed=false`。
- `closed_completion_gates=['PriorFullSNonAPWFDKLSInputAvailable', 'FullSOverModulusRatioIsPolylog', 'CommonVariablesSupportCompletion', 'FullSCompletionDecomposition', 'EndpointAndGcdLossAbsorbed', 'FlatResidueMassShortcutUnavailable', 'ModulusDependentCompletedAtomPinned']`。
- `open_completion_gates=['ModulusDependentCompletedFullSKLSInput']`。
- `terminal_gap_after_router=ModulusDependentCompletedFullSKLSInput`。

## 4. 必要定理条款

- `handles c-dependent residue weights B_{c,x}`。
- `keeps the current uncentered no-projection non-AP object`。
- `uses C≈P/log^O P, S≈P and H<=P/log^O P`。
- `absorbs endpoint, gcd, dyadic and smoothing losses into B(A)`。
- `delivers NaturalWFDScale/log^A P for every A>0`。

## 5. 完成型账本表

| gate | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- |
| `PriorFullSNonAPWFDKLSInputAvailable` | `true` | previous terminal=FullSNonAPWFDKLSTheoremInput; open=['FullSNonAPWFDKLSTheoremInput']. | none at previous-frontier level | `FullSCompletionDecomposition` |
| `FullSOverModulusRatioIsPolylog` | `true` | Full-S contract and KLS template give S≈P and C≈P/log^O P, hence S/C=log^O P. | none at scale-ratio level | `FullSCompletionDecomposition` |
| `CommonVariablesSupportCompletion` | `true` | 共同变量表固定 c,C 与 s,S；完成分解不引入新变量叉路。 | none at variable-table level | `FullSCompletionDecomposition` |
| `FullSCompletionDecomposition` | `true` | 对每个 c~C，把 s~S 写成 x+k c；完整块数 L_c≈S/c=log^O P，相位变成完整 residue Kloosterman 相位 e_c(a_h x+b_h bar{x})。 | 端点、非互素层和平滑只进入多对数损失账本。 | `ModulusDependentCompletedFullSKLSInput` |
| `EndpointAndGcdLossAbsorbed` | `true` | FullS-KLS-ext 与 KLS 模板已有 dyadic/gcd/smoothing/endpoint 的 B(A) 损失账本。 | none after choosing B(A) larger | `ModulusDependentCompletedFullSKLSInput` |
| `FlatResidueMassShortcutUnavailable` | `true` | 当前 generic beta_s 只要求 divisor-bounded；SOURCE-CEN no-go 已记录未中心化对象没有块内零均值/平坦性。 | 不能把 residue 权重当作常数后只用完整 Weil 和。 | `ModulusDependentCompletedFullSKLSInput` |
| `ModulusDependentCompletedAtomPinned` | `true` | 完成后 residue 权重 B_{c,x}=sum_k beta_{x+kc} 依赖模数 c；这正是 full-S 输入的不可再逃避核心。 | none at target-definition level | `ModulusDependentCompletedFullSKLSInput` |
| `ModulusDependentCompletedFullSKLSInput` | `false` | 仓库尚无针对 B_{c,x} 模数依赖 residue 权重的完成型 KLS/dispersion 定理。 | 证明或引用完成型、模数依赖 residue 权重的 full-S Kloosterman 平均估计。 | `ModulusDependentCompletedFullSKLSInput` |

## 6. 当前结论

唯一剩余继续变窄为：

```text
ModulusDependentCompletedFullSKLSInput:
  prove/cite a completed Kloosterman average with c-dependent residue weights B_{c,x}.
```

这一步没有证明该完成型定理；它利用 full-S 长度把非完整窗口硬点剥离掉，暴露出真正剩余的模数依赖权重问题。
