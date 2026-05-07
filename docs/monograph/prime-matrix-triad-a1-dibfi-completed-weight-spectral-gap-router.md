# Triad-A1 DI/BFI completed-weight spectral gap 路由器

**状态：** `modulus_dependent_completed_kls_reduced_to_c_dependent_residue_spectral_input_open`

`ModulusDependentCompletedFullSKLSInput` 已被压成 `CDependentResidueWeightSpectralCancellationInput`：L2/Weil、普通大筛和平坦 residue 捷径都不足，必须证明或引用处理 B_{c,x} 的谱/dispersion 平均抵消。

## 1. 结构律

After full-S completion, the remaining obstacle is not the length of the s-window. The residue weights B_{c,x} have an L2 budget, but they are c-dependent and not flat or centered. Pointwise Weil with Cauchy reaches only the natural/root scale and ordinary large sieve lacks the required c,h dispersion structure. Therefore the next honest atom is a spectral cancellation theorem for c-dependent completed residue weights.

```text
previous terminal:
  ModulusDependentCompletedFullSKLSInput;

new terminal:
  CDependentResidueWeightSpectralCancellationInput;

expansion:
  ['CDependentResidueWeightSpectralCancellationInput'].
```

## 2. 尺度诊断

- `L_c=S/c=log^O(P)`。
- `sum_x |B_{c,x}|^2 <= log^O(P) sum_s |beta_s|^2`。
- `pointwise Weil + L2 reaches only natural/root scale`。
- `arbitrary log-saving requires spectral averaging over c,h`。

## 3. 必要定理条款

- `handles c-dependent residue weights B_{c,x}`。
- `uses well-factorable lambda_c and smooth omega_h over c,h`。
- `goes beyond pointwise Weil and ordinary large sieve`。
- `keeps the uncentered no-projection non-AP WFD target`。
- `delivers NaturalWFDScale/log^A P for every A>0`。

## 4. 汇总

- `completed_weight_spectral_gap_closed=false`。
- `closed_spectral_gap_gates=['PriorCompletedFullSKLSInputAvailable', 'CompletedResidueL2BudgetAvailable', 'FlatResidueShortcutStillBlocked', 'PointwiseWeilL2NoLogSaving', 'OrdinaryLargeSieveNoCDependentWeight', 'CDependentResidueSpectralAtomPinned']`。
- `open_spectral_gap_gates=['CDependentResidueWeightSpectralCancellationInput']`。
- `terminal_gap_after_router=CDependentResidueWeightSpectralCancellationInput`。

## 5. 谱缺口账本表

| gate | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- |
| `PriorCompletedFullSKLSInputAvailable` | `true` | previous terminal=ModulusDependentCompletedFullSKLSInput; open=['ModulusDependentCompletedFullSKLSInput']. | none at previous-frontier level | `CDependentResidueWeightSpectralCancellationInput` |
| `CompletedResidueL2BudgetAvailable` | `true` | B_{c,x}=sum_k beta_{x+kc}; L_c=S/c=log^O(P); divisor-bounded beta gives sum_x \|B_{c,x}\|^2 <= log^O(P) sum_s \|beta_s\|^2. | L2 控制只给自然尺度账本，不给任意 log-saving。 | `CDependentResidueWeightSpectralCancellationInput` |
| `FlatResidueShortcutStillBlocked` | `true` | generic beta_s 没有 residue 平坦/零均值；SOURCE-CEN no-go 禁止免费中心化。 | 不能把 B_{c,x} 当作常数或已中心化权重。 | `CDependentResidueWeightSpectralCancellationInput` |
| `PointwiseWeilL2NoLogSaving` | `true` | KLS 自足脊柱已记录点态 Weil+Cauchy 只能给临界平方根级控制，不能产生任意 log^{-A}。 | 需要模数族与频率族上的谱平均抵消。 | `CDependentResidueWeightSpectralCancellationInput` |
| `OrdinaryLargeSieveNoCDependentWeight` | `true` | KZ-E spine 已记录普通大筛在平衡 Type-II 块差一个主尺度。 | 完成型权重依赖 c，不能由不带 dispersion/Kuznetsov 结构的普通大筛闭合。 | `CDependentResidueWeightSpectralCancellationInput` |
| `CDependentResidueSpectralAtomPinned` | `true` | 所有朴素出口已排除；剩余必须利用 c,h 族上的谱/dispersion 平均抵消。 | none at target-definition level | `CDependentResidueWeightSpectralCancellationInput` |
| `CDependentResidueWeightSpectralCancellationInput` | `false` | 仓库尚无针对 c 依赖 residue 权重 B_{c,x} 的谱/dispersion 抵消定理或自足证明。 | 证明或引用能处理 B_{c,x} 的完成型 Kuznetsov/DI-BFI 谱平均定理。 | `CDependentResidueWeightSpectralCancellationInput` |

## 6. 当前结论

唯一剩余继续变窄为：

```text
CDependentResidueWeightSpectralCancellationInput:
  prove/cite spectral DI/BFI/Kuznetsov cancellation
  for completed Kloosterman sums with c-dependent B_{c,x}.
```

这一步没有证明该谱定理；它排除了点态 Weil、普通大筛和 residue 平坦捷径。
