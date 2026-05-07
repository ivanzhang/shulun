# Triad-A1 DI/BFI NewFullSTheoremInput 路由器

**状态：** `new_full_s_theorem_input_reduced_to_full_s_nonap_wfd_kls_input_open`

`NewFullSTheoremInput` 已被压成唯一可审稿原子 `FullSNonAPWFDKLSTheoremInput`。这一步没有证明新定理；它完成了目标定义层闭合，把剩余变成一个必须引用或新证的 full-S non-AP WFD KLS 定理。

## 1. 结构律

NewFullSTheoremInput is not another combinatorial branch. All old exits are blocked: existing DI/BFI primary sources do not imply the full-S non-AP WFD kernel; APSourceLift is rejected; Maynard-W4 and short-S routes are rejected; SOURCE-CEN/BD-CEN block hidden projection. The remaining atom is therefore a single theorem input: a Kloosterman large sieve/dispersion estimate for the current full-S, uncentered, non-projected non-AP WFD window with arbitrary log saving.

```text
previous terminal:
  NewFullSTheoremInput;

new terminal:
  FullSNonAPWFDKLSTheoremInput;

expansion:
  ['FullSNonAPWFDKLSTheoremInput'].
```

## 2. 汇总

- `new_full_s_theorem_input_closed=false`。
- `closed_input_gates=['PriorSingleGapIsNewFullSTheoremInput', 'ExistingDIBFIPrimarySourcesRejected', 'ExternalFullSContractAlreadyPinsStatement', 'MaynardAndShortSRoutesBlocked', 'NonAPUncenteredNoProjectionObjectPinned', 'SelfContainedCompletionKernelStillOpen', 'FullSNonAPWFDKLSTheoremInputPinned']`。
- `open_input_gates=['FullSNonAPWFDKLSTheoremInput']`。
- `terminal_gap_after_router=FullSNonAPWFDKLSTheoremInput`。

## 3. 必要定理条款

- `object: current non-AP uncentered no-projection WFD window`。
- `range: X≈P^2, C≈P/log^O P, S≈P, 0<|h|<=H<=P/log^O P`。
- `weights: lambda well-factorable, beta divisor-bounded, omega smooth`。
- `loss: dyadic/gcd/smoothing endpoints absorbed into B(A)`。
- `strength: NaturalWFDScale/log^A P for every A>0`。
- `boundary: no AP-source lift, no Maynard-W4 compression, no hidden centering/projection`。

## 4. 定理输入账本表

| gate | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- |
| `PriorSingleGapIsNewFullSTheoremInput` | `true` | APSourceLift rejected=True; terminal=NewFullSTheoremInput. | none at previous-frontier level | `FullSNonAPWFDKLSTheoremInput` |
| `ExistingDIBFIPrimarySourcesRejected` | `true` | BFI AP theorem and DI/Maynard J-scale do not imply the full-S non-AP WFD kernel. | 不能把 NewFullSTheoremInput 写成现有 DI/BFI 主来源逐项推论。 | `FullSNonAPWFDKLSTheoremInput` |
| `ExternalFullSContractAlreadyPinsStatement` | `true` | FullS-KLS-ext 已写明 C≈P/log^O P, S≈P, H<=P/log^O P 和未中心化无投影对象。 | 外部合同版可引用；完全自足版仍需要新证明。 | `FullSNonAPWFDKLSTheoremInput` |
| `MaynardAndShortSRoutesBlocked` | `true` | Maynard-S compression conflicts with full S; short-width subwindows do not reduce the Maynard magnitude. | 不能回到 W4 cone 或短 S 子窗口分解。 | `FullSNonAPWFDKLSTheoremInput` |
| `NonAPUncenteredNoProjectionObjectPinned` | `true` | non-AP object ledger removes APErrorRepresentation and leaves UncenteredWFDToKE13NoProjectionIdentity. | 新定理必须直接估计当前 non-AP WFD 对象，不得换对象。 | `FullSNonAPWFDKLSTheoremInput` |
| `SelfContainedCompletionKernelStillOpen` | `true` | KZ-E 已把内联账本压到 WFD-core；SOURCE-CEN/BD-CEN 阻断免费中心化投影。 | 完成型/Kuznetsov 自足证明仍等价于新增 full-S 深定理。 | `FullSNonAPWFDKLSTheoremInput` |
| `FullSNonAPWFDKLSTheoremInputPinned` | `true` | 所有旧出口已分类；唯一剩余是一个直接作用于 full-S non-AP WFD 的 KLS 定理输入。 | none at target-definition level | `FullSNonAPWFDKLSTheoremInput` |
| `FullSNonAPWFDKLSTheoremInput` | `false` | 仓库尚无该新定理的外部主来源引用或自足解析证明。 | 提交外部深定理引用，或证明完整 full-S non-AP WFD KLS 估计。 | `FullSNonAPWFDKLSTheoremInput` |

## 5. 当前结论

唯一剩余已从泛称压成具体原子：

```text
FullSNonAPWFDKLSTheoremInput:
  prove or cite a full-S Kloosterman large-sieve/dispersion theorem
  for the current non-AP uncentered no-projection WFD window.
```

因此外部合同版可以接受 FullS-KLS-ext 作为输入；完全自足版仍未闭合，因为该 full-S 定理本身尚未在仓库内证明。
