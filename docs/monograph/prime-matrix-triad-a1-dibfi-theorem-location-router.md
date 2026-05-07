# Triad-A1 DI/BFI 定理位置路由器

**状态：** `dibfi_theorem_locations_pinned_current_window_hypothesis_match_open`

DI/BFI 原始 dispersion 的“定理位置”部分已从缺口中剥离：BFI 取 Theorem 10，DI 取 Theorem 12，并用 Maynard 公开源码作编号交叉核验。当前剩余改写为当前 KE-13/WFD 窗口对这些定理的假设逐项匹配。

## 1. 结构律

The theorem-location part of the DI/BFI original-dispersion gap is now separated from the mathematical hypothesis match. BFI Theorem 10 supplies the well-factorable prime-AP dispersion location; DI Theorem 12 supplies the Kloosterman spectral estimate location; Maynard's public well-factorable paper cross-checks the numbering. The only remaining task is to prove that the current uncentered KE-13/WFD window satisfies the hypotheses of those located theorems without changing the target object.

```text
previous gap:
  DIBFIOriginalDispersionTheoremLocationAndHypothesisMatch;

theorem locations:
  BFI1987 Theorem 10;
  DI1982 Theorem 12;
  Maynard2020 cross-check;

remaining gap:
  DIBFIOriginalDispersionCurrentWindowHypothesisMatch.
```

## 2. 汇总

- `theorem_locations_pinned=true`。
- `all_gates_closed=false`。
- `next_external_target=DIBFIOriginalDispersionCurrentWindowHypothesisMatch`。
- `terminal_gap_after_router=DIBFIOriginalDispersionCurrentWindowHypothesisMatch`。

## 3. 定理位置表

| source | paper | location | DOI/arXiv | role | located |
| --- | --- | --- | --- | --- | --- |
| `BFI1987-Theorem10` | Bombieri--Friedlander--Iwaniec, Primes in arithmetic progressions to large moduli. II | Mathematische Annalen 277(3), 361--393, 1987, Theorem 10 | `10.1007/BF01458321` | well-factorable weighted prime AP dispersion estimate | `true` |
| `DI1982-Theorem12` | Deshouillers--Iwaniec, Kloosterman sums and Fourier coefficients of cusp forms | Inventiones Mathematicae 70, 219--288, 1982, Theorem 12 | `10.1007/BF01390728` | spectral Kloosterman estimate used inside the dispersion method | `true` |
| `Maynard2020-CrossCheck` | Maynard, Primes in arithmetic progressions to large moduli II: Well-factorable estimates | arXiv:2006.07088, Theorem A cites BFI Theorem 10; Lemma 6.12 cites DI Theorem 12 | `arXiv:2006.07088` | modern public cross-check of theorem numbering and DI estimate formula | `true` |

## 4. 门控表

| gate | available | needed | gap | route | closed |
| --- | --- | --- | --- | --- | --- |
| `BFITheorem10Located` | BFI II theorem number, DOI and pages are pinned | well-factorable weighted AP dispersion source | none at theorem-location level | cite BFI1987 Theorem 10 | `true` |
| `DITheorem12Located` | DI theorem number, DOI and pages are pinned | spectral Kloosterman estimate source | none at theorem-location level | cite DI1982 Theorem 12 | `true` |
| `ModernCrossCheckRegistered` | Maynard arXiv source cross-checks BFI Theorem 10 and DI Theorem 12 numbering | publicly inspectable theorem numbering check | none at numbering cross-check level | use Maynard2020 as a numbering audit, not as a replacement for DI/BFI | `true` |
| `CurrentGenericWFDContractReady` | previous router materialized uncentered generic WFD DI/BFI contract | do not reopen canonical support branch | none | continue only with current-window hypothesis match | `true` |
| `KLSWindowTemplateReady` | local KLS template records phase, level, frequency, gcd and log-loss budgets | use it as the checklist for the final hypothesis match | none at checklist level | compare each KLS-template row against BFI/DI hypotheses | `true` |
| `CurrentWindowHypothesisMatch` | theorem locations and local checklist are now fixed | prove current KE-13/WFD window satisfies every cited DI/BFI hypothesis | not yet checked theorem-by-theorem inside the repository | match uncentered target, level, phase, Type-I/II range, gcd, smoothing and log saving | `false` |

## 5. 当前结论

外部 theorem/proposition/page 的定位已经不再是剩余终端。真正剩余为：

```text
DIBFIOriginalDispersionCurrentWindowHypothesisMatch
```

下一步只能逐项核对当前未中心化 WFD 窗口是否满足 BFI Theorem 10 与 DI Theorem 12 的输入假设；不能再把缺口退回为泛泛的外部引用问题。
