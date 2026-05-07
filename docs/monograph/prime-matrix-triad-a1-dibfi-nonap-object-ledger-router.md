# Triad-A1 DI/BFI 非 AP-source object ledger 路由器

**状态：** `nonap_object_ledger_reduced_to_uncentered_wfd_no_projection_identity_open`

非 AP-source 对象侧已压成 `UncenteredWFDToKE13NoProjectionIdentity`：`APErrorRepresentation` 已归入 AP-source 直接 BFI 分支；非 AP fallback 只剩 `DispersionCauchyNoCenteringIdentity` 与 `KE13DyadicExhaustionNoProjection`。

## 1. 结构律

The non-AP fallback object is not a prime-AP discrepancy. APErrorRepresentation belongs to the AP-source/direct-BFI branch and is removed from the non-AP terminal. SOURCE-CEN and BD-CEN block any free centering/projection shortcut. Therefore the non-AP object side is exactly the uncentered WFD-to-KE13 no-projection identity: derive the raw dispersion/Cauchy object without centering, then prove KE-13 dyadic exhaustion without projection or endpoint loss.

```text
previous terminal:
  DIBFIQuantifiedNoProjectionWindowCertificateForNonAPSource;

removed from non-AP object terminal:
  ['APErrorRepresentation'];

new object terminal:
  UncenteredWFDToKE13NoProjectionIdentity;

expansion:
  ['DispersionCauchyNoCenteringIdentity', 'KE13DyadicExhaustionNoProjection'].
```

## 2. 汇总

- `ap_error_representation_not_nonap_terminal=true`。
- `nonap_object_ledger_closed=false`。
- `closed_object_gates=['APErrorRepresentationSeparated', 'NoSilentProjectionOrCentering', 'ObjectTerminalDefined']`。
- `open_object_gates=['DispersionCauchyNoCenteringIdentity', 'KE13DyadicExhaustionNoProjection']`。
- `terminal_gap_after_router=UncenteredWFDToKE13NoProjectionIdentity`。

## 3. 对象账本表

| gate | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- |
| `APErrorRepresentationSeparated` | `true` | AP-source 直接 BFI 分支已闭合；非 AP generic WFD 是其补集，不能把 APErrorRepresentation 当作非 AP fallback 的对象终端。 | none for non-AP object ledger | `UncenteredWFDToKE13NoProjectionIdentity` |
| `NoSilentProjectionOrCentering` | `true` | SOURCE-CEN 会改变 WFD 目标对象；BD-CEN 只证明 h=0 主项抵消，未证明同块中心化扣除。 | 不能免费插入块中心化、投影或删同块对角。 | `DispersionCauchyNoCenteringIdentity` |
| `DispersionCauchyNoCenteringIdentity` | `false` | 该门仍在 transfer-scale open_transfer_gates 中；需要从 BFI 原始 dispersion/Cauchy 展开逐项得到当前未中心化对象。 | 写出 E_{N,M}->E_disp 的逐项恒等式，确认没有块中心化插入和同块对角删除。 | `UncenteredWFDToKE13NoProjectionIdentity` |
| `KE13DyadicExhaustionNoProjection` | `false` | 共同变量表已定位 KE13Identification 为 target_preserved=false；所有 dyadic 主块是否完全覆盖 WFD_core 尚未证明。 | 证明主非零频块完全等于 WFD_core(C,S,H,lambda,beta,omega)，且无端点遗漏。 | `UncenteredWFDToKE13NoProjectionIdentity` |
| `ObjectTerminalDefined` | `true` | nonap terminal targets=['NoProjectionUncenteredDispersionIdentity', 'QuantifiedDIBFIWindowSubstitution']；对象侧只保留两个未闭合恒等式。 | two object identities remain open | `UncenteredWFDToKE13NoProjectionIdentity` |

## 4. 当前结论

对象侧的最窄剩余为：

```text
UncenteredWFDToKE13NoProjectionIdentity:
  DispersionCauchyNoCenteringIdentity;
  KE13DyadicExhaustionNoProjection.
```

这一步只改变终端账本，不声称对象恒等式已经证明；它排除了把 AP-source 身份或块中心化
偷带入非 AP fallback 的路径。
