# Triad-A1 DI/BFI full-S dispersion atom 路由器

**状态：** `full_s_dispersion_atom_reduced_to_external_dibfi_match_open`

`NewFullSDispersionAtom` 已被精确改写为 `ExternalFullSDIBFIAtomMatch`：要么提交适配 S_common≈X^(1/2)、z≈X 的原始 DI/BFI full-S 定理合同，要么继续攻 non-AP 对象侧的未中心化无投影恒等式。

## 1. 结构律

The latest scale gap is no longer a parameter optimization problem. Maynard-W4 cannot accept S≈X^(1/2) when q≈1/2, short-S subwindows do not change the magnitude of z=s1*s2, and the existing KE-13/WFD-core text is an open deep kernel rather than a closed proof. Thus the honest full-S route is a precise original DI/BFI dispersion atom for the current full-S window, with no hidden centering/projection.

```text
previous terminal:
  NewFullSDispersionAtom;

new terminal:
  ExternalFullSDIBFIAtomMatch;

expansion:
  ['ExternalFullSDIBFIAtomMatch', 'UncenteredWFDToKE13NoProjectionIdentity'].
```

## 2. 汇总

- `full_s_dispersion_atom_closed=false`。
- `closed_atom_gates=['PriorNewFullSAtomFrontierAvailable', 'FullSAtomStatementPinned', 'MaynardW4RouteAlreadyRejected', 'ExistingKZEWFDCoreIsSameShapeButOpen', 'DirectBFIAPBranchDoesNotCloseNonAPFullS', 'OriginalDIBFITheoremLocationsPinned']`。
- `open_atom_gates=['UncenteredNoProjectionCompatibilityStillOpen', 'ExternalFullSDIBFIAtomMatch']`。
- `terminal_gap_after_router=ExternalFullSDIBFIAtomMatch`。

## 3. 原子账本表

| gate | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- |
| `PriorNewFullSAtomFrontierAvailable` | `true` | 短 S 子窗口退路已排除，上游终端单点化为 NewFullSDispersionAtom。 | none at prior-frontier level | `FullSAtomStatementPinned` |
| `FullSAtomStatementPinned` | `true` | full-S 原子被固定为 S_common≈X^(1/2)、z≈X 的原始 DI/BFI dispersion 输入。 | none at statement-naming level | `ExternalFullSDIBFIAtomMatch` |
| `MaynardW4RouteAlreadyRejected` | `true` | Maynard W4 路线需要 S_May<=X^(3/10-o(1))；full-S 保留会强制 S_May≈X^(1/2)。 | 不能再从 Maynard-W4 锥内取得 full-S 结论。 | `ExternalFullSDIBFIAtomMatch` |
| `ExistingKZEWFDCoreIsSameShapeButOpen` | `true` | KZ-E spine 已有 KE-13/WFD-core 形状，但文档明确标注该核尚未自足证明。 | 不能把 KE-13/WFD-core 当作已闭合 full-S 原子。 | `ExternalFullSDIBFIAtomMatch` |
| `DirectBFIAPBranchDoesNotCloseNonAPFullS` | `true` | AP-source 直接 BFI 分支已闭合；当前剩余是 non-AP generic WFD fallback。 | 必须给出 non-AP full-S 原始 dispersion 假设匹配，或回到无投影对象恒等式。 | `ExternalFullSDIBFIAtomMatch` |
| `OriginalDIBFITheoremLocationsPinned` | `true` | 外部 DI/BFI 定理位置已固定为 BFI Theorem 10 与 DI Theorem 12。 | 定理位置不是问题；问题是 full-S 当前窗口假设逐项匹配。 | `ExternalFullSDIBFIAtomMatch` |
| `UncenteredNoProjectionCompatibilityStillOpen` | `false` | non-AP 对象账本仍开放：['DispersionCauchyNoCenteringIdentity', 'KE13DyadicExhaustionNoProjection']。 | 证明 full-S 外部原子应用时没有隐藏中心化、投影或 dyadic 主块遗漏。 | `UncenteredWFDToKE13NoProjectionIdentity` |
| `ExternalFullSDIBFIAtomMatch` | `false` | NC-BLK 外部路由也要求 precise DI/BFI original dispersion citation；external_dibfi_open=True。 | 需要写出 full-S 原始 dispersion 定理/引用合同，并逐项验证当前 S_common≈X^(1/2)、z≈X 窗口满足其假设。 | `ExternalFullSDIBFIAtomMatch` |

## 4. 当前结论

最新最窄剩余为：

```text
ExternalFullSDIBFIAtomMatch:
  full-S original DI/BFI theorem/citation for S_common≈X^(1/2), z≈X;
  current-window hypothesis match;
  no hidden centering/projection in the non-AP WFD application.
```

这一步没有宣称行命题闭合；它把 full-S 缺口从笼统新原子改成可审计外部定理合同。
