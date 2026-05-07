# Triad-A1 DI/BFI 当前窗口匹配路由器

**状态：** `dibfi_window_match_reduced_to_target_transfer_and_scale_inequalities`

当前窗口假设匹配已被压成两个最小硬点：一是 AP discrepancy 到 KE-13/WFD-core 的对象不变转移；二是 C,S,H,Q,N,M 等 dyadic 尺度满足 BFI/DI 的显式范围。

## 1. 结构律

The current-window match is not a vague citation issue anymore. All fixed interfaces are ready: theorem locations, generic-WFD branch selection, uncentered target choice, Kloosterman phase/smoothing ledger, and formal coefficient class. The remaining proof has exactly two active obligations: show the AP discrepancy to KE-13/WFD transfer is a target-preserving application of BFI/DI, and prove the dyadic window scale inequalities fit the BFI/DI admissible ranges.

```text
fixed:
  BFI Theorem 10 and DI Theorem 12 are located;
  generic WFD external branch is selected;
  uncentered target is preserved;
  Kloosterman phase and smoothing ledger are ready;
  coefficient class is registered;

open:
  OriginalAPToWFDTargetTransfer;
  WindowScaleInequalities;

terminal: DIBFIWindowScaleAndTargetTransferMatch.
```

## 2. 汇总

- `all_gates_closed=false`。
- `open_gates=['OriginalAPToWFDTargetTransfer', 'WindowScaleInequalities']`。
- `next_external_target=DIBFIWindowScaleAndTargetTransferMatch`。
- `terminal_gap_after_router=DIBFIWindowScaleAndTargetTransferMatch`。

## 3. 门控表

| gate | available | needed | gap | route | closed |
| --- | --- | --- | --- | --- | --- |
| `TheoremLocationsPinned` | BFI Theorem 10 and DI Theorem 12 are registered | do not spend proof effort on theorem-number search | none | use theorem-location router output | `true` |
| `GenericWFDContractReady` | previous router fixes the generic noncanonical WFD external branch | avoid reopening canonical RIW/Buchstab support branch | none | stay on generic WFD external branch | `true` |
| `UncenteredTargetPreserved` | SOURCE-CEN no-go blocks free centering; generic router chooses direct uncentered estimate | external theorem application must estimate the original uncentered target | none at target-choice level | direct original dispersion, no SOURCE-CEN insertion | `true` |
| `KloostermanPhaseAndSmoothLedgerReady` | KLS template records CRT phase, smooth windows, gcd and B(A) log ledger | local variables can be compared row-by-row to DI Theorem 12 | none at checklist level | use template as the DI hypothesis table | `true` |
| `CoefficientClassReady` | KZ-E spine states well-factorable lambda_c, divisor-bounded beta_s, smooth omega_h | coefficient class must match BFI/DI admissible weights | none at formal coefficient-class level | lambda_c/beta_s/omega_h enter the external theorem hypotheses | `true` |
| `OriginalAPToWFDTargetTransfer` | KZ-E spine has a dispersion identity from AP discrepancy to WFD-core | prove this transfer uses exactly BFI Theorem 10/DI Theorem 12 without changing target | not yet written as a theorem-by-theorem implication | write AP discrepancy -> dispersion -> KE-13 transfer lemma | `false` |
| `WindowScaleInequalities` | KLS template names C,S,H; KZ-E spine names R0,L0/completion lengths | derive explicit inequalities putting current dyadic windows in BFI/DI admissible ranges | current docs name ranges qualitatively but do not yet prove the exact exponent inequalities | compute C,S,H,Q,N,M against BFI x^(4/7-eps) and DI J-scale terms | `false` |

## 4. 当前结论

定理位置和普通账本都不再是终端。下一步只剩：

```text
DIBFIWindowScaleAndTargetTransferMatch
```

也就是同时完成对象不变转移与尺度不等式。若任一项失败，外部 DI/BFI 不能诚实闭合当前 generic WFD 分支。
