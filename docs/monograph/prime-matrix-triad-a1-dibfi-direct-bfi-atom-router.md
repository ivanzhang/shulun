# Triad-A1 DI/BFI 直接 BFI 原子路由器

**状态：** `dibfi_quantified_no_projection_reduced_to_direct_bfi_atom_or_ke13_fallback_open`

量化无投影终端已被继续压缩为一个分叉：首选路线是直接 BFI prime-AP 原子，只剩 prime-AP 残差表示、BFI level 代入和 well-factorable level；若不能提升回 AP 原子，则回到 KE-13 无投影逐项路线。

## 1. 结构律

If the current residual can be represented at the prime-AP level, BFI Theorem 10 should be used as one atom: its internal dispersion and DI/Kloosterman estimates absorb the no-projection and J-scale obligations. If the proof only has an isolated KE-13/WFD window, those obligations remain external and must be proved separately.

```text
previous:
  DIBFIQuantifiedNoProjectionWindowCertificate;

new terminal:
  DIBFIDirectBFIAPAtomMatchOrKE13NoProjection;

preferred route:
  DirectBFIPrimeAPAtom;

fallback route:
  SeparateKE13DIBFIWindow.
```

## 2. 汇总

- `direct_bfi_atom_available=true`。
- `direct_bfi_atom_closed=false`。
- `ke13_fallback_open=true`。
- `open_gates=['PrimeAPResidualRepresentation', 'BFILevelSubstitution', 'WellFactorableLambdaLevel']`。
- `terminal_gap_after_router=DIBFIDirectBFIAPAtomMatchOrKE13NoProjection`。

## 3. 路线表

| route | role | available | closed | absorbs | still needs | reason |
| --- | --- | --- | --- | --- | --- | --- |
| `DirectBFIPrimeAPAtom` | `preferred_if_source_can_be_lifted_to_prime_ap_error` | `true` | `false` | DispersionCauchyNoCenteringIdentity, KE13DyadicExhaustionNoProjection, KLSModulusWindowQuantified, InverseVariableWindowQuantified, DIJScaleDominanceSubstitution | PrimeAPResidualRepresentation, BFILevelSubstitution, WellFactorableLambdaLevel | 若直接引用 BFI Theorem 10，则 dispersion/DI J-scale 是定理证明内部内容；外部引用版不应再要求本文重证 KE-13 的无投影逐项展开。 |
| `SeparateKE13DIBFIWindow` | `fallback_if_only_ke13_window_is_available` | `true` | `false` |  | NoProjectionUncenteredDispersionIdentity, QuantifiedDIBFIWindowSubstitution | 若上游只能给出孤立 KE-13/WFD-core 窗口，而不能提升回 BFI prime-AP 误差，则必须继续证明无中心化、无投影、无 dyadic 主块遗漏，并逐项代入 DI/BFI 尺度。 |
| `HLCWindowedKLSAtom` | `closed_for_clean_hlc_branch_only` | `true` | `true` | CleanHLCWindow |  | A1 clean/HLC 分支已有窗口化外部 KLS 适配；但它不是 generic WFD 共同变量表的直接替代品。 |
| `CurrentTransferScaleFrontier` | `input_being_reduced` | `true` | `false` |  | NoProjectionUncenteredDispersionIdentity, QuantifiedDIBFIWindowSubstitution | 上一轮终端被本轮二分为 DirectBFIPrimeAPAtom 或 SeparateKE13DIBFIWindow。 |

## 4. 门控表

| gate | closed | needed | if fail |
| --- | --- | --- | --- |
| `BFIAtomAvailable` | `true` | BFI Theorem 10 is pinned as a well-factorable prime-AP dispersion atom | cannot use direct BFI route |
| `PrimeAPResidualRepresentation` | `false` | 把当前 clean A1/generic WFD 残差提升为 BFI prime-AP discrepancy，而不是只给一个孤立 KE-13 子窗口。 | fall back to SeparateKE13DIBFIWindow |
| `BFILevelSubstitution` | `false` | 显式证明 Q <= X^(4/7-eps) 或采用已定位定理允许的等价更强范围。 | direct BFI route not closed |
| `WellFactorableLambdaLevel` | `false` | 证明 lambda_q 的 level 与 well-factorable 分解正是 BFI Theorem 10 输入。 | direct BFI route not closed |
| `KE13FallbackStillAvailable` | `true` | 若直接 BFI 不可用，保留 KE-13 无投影逐项路线。 | both external routes malformed |

## 5. 当前结论

这一步把 DI/BFI 终端的逻辑顺序纠正为：优先尝试回到 BFI 的 prime-AP 原始误差对象。若成功，则不需要本文重证 DI 的 J-scale 或 KE-13 无投影展开；那些是 BFI 原子内部内容。若不能成功，才继续走 KE-13 逐项路线。

因此下一硬点从两个并列大项压成：

```text
DIBFIDirectBFIAPAtomMatchOrKE13NoProjection
  preferred: PrimeAPResidualRepresentation + BFILevelSubstitution + WellFactorableLambdaLevel;
  fallback:  NoProjectionUncenteredDispersionIdentity + QuantifiedDIBFIWindowSubstitution.
```
