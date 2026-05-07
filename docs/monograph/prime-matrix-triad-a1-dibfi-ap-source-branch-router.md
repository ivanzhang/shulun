# Triad-A1 DI/BFI AP-source 分支路由器

**状态：** `ap_source_direct_bfi_branch_closed_nonap_fallback_open`

AP-source 分支已按定义性合同闭合：若原始 clean A1 残差在 Cauchy/dispersion 前就是 BFI prime-AP discrepancy 的 dyadic 总和，则直接 BFI 原子可用且 level 已闭合。非 AP-source generic WFD 不能偷用该结论，剩余转为原始 dispersion 外部定理匹配。

## 1. 分支律

The upstream AP source identity can be closed only as an explicit branch statement: on the AP-source branch, R_clean is defined before Cauchy/dispersion as the dyadic BFI prime-AP discrepancy with matching Delta_q, lambda_q and Type coefficients, so BFI Theorem 10 applies directly. The complement is not lost or silently upgraded; a non-AP generic WFD source must use the KE-13 no-projection/original-dispersion fallback. Thus the direct BFI route is closed for AP-source inputs, while the broader generic non-AP branch remains a precise external theorem match.

```text
AP-source branch:
  R_clean is an upstream dyadic BFI prime-AP discrepancy;
  BFI atom and level ledger are closed;

non-AP generic WFD branch:
  no downstream back-projection to AP is allowed;
  must use KE-13 no-projection / original-dispersion fallback;

no silent AP upgrade.
```

## 2. 汇总

- `previous_terminal_gap=UpstreamCleanA1APSourceDefinition`。
- `ap_source_branch_closed=true`。
- `generic_nonap_fallback_closed=false`。
- `closed_branches=['APSourceDirectBFI', 'CoverageDichotomy', 'NoSilentAPUpgrade', 'GenericFallbackRegistered']`。
- `open_branches=['NonAPSourceGenericWFD']`。
- `terminal_gap_after_router=DIBFIOriginalDispersionTheoremLocationAndHypothesisMatchForNonAPSource`。

## 3. 分支表

| branch | scope | closed | evidence | remaining | route |
| --- | --- | --- | --- | --- | --- |
| `APSourceDirectBFI` | R_clean is defined upstream as dyadic BFI prime-AP discrepancy with matching main term and coefficients | `true` | BFI atom is pinned; BFI level ledger is closed; the remaining AP identity gates are definitional on this branch. | none on AP-source branch | use BFI1987-Theorem10 as one prime-AP atom |
| `NonAPSourceGenericWFD` | the clean residual is only an uncentered WFD/KE-13 window, not an upstream AP discrepancy | `false` | SOURCE-CEN no-go and AP residual router block downstream back-projection; direct BFI AP atom cannot be used. | SeparateKE13DIBFIWindow or external original-dispersion theorem | fallback |
| `CoverageDichotomy` | a source object is either declared/proved AP-source before Cauchy, or it is not | `true` | AP residual router isolated exactly the two source-definition gates; branch coverage pattern is already used in A1 source statements. | none after explicit branch statement | AP-source vs non-AP-source dichotomy |
| `NoSilentAPUpgrade` | generic WFD cannot be silently upgraded to prime-AP discrepancy | `true` | AP residual identity router records that downstream WFD identification is diagnostic, not a source identity. | none | non-AP source stays fallback |
| `GenericFallbackRegistered` | non-AP generic WFD has an external route already materialized at contract level | `true` | generic WFD DI/BFI contract is materialized except for exact citation/hypothesis match. | precise external theorem match or self-contained KE-13 no-projection | DIBFIOriginalDispersionTheoremLocationAndHypothesisMatch |

## 4. 当前结论

直接 BFI prime-AP 路线已在 AP-source 分支上闭合；但这不是 generic WFD 宽口径的无条件闭合。

```text
closed:
  APSourceDirectBFI;

still open:
  DIBFIOriginalDispersionTheoremLocationAndHypothesisMatchForNonAPSource.
```

因此下一步若坚持闭合 broader generic WFD 分支，必须攻原始 dispersion 外部定理假设匹配，或回到 KE-13 无投影逐项证明。
