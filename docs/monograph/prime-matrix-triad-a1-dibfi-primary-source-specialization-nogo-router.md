# Triad-A1 DI/BFI primary-source specialization no-go 路由器

**状态：** `dibfi_primary_source_specialization_rejected_new_theorem_or_ap_lift_open`

`DIBFIPrimarySourceSpecializationProof` 被主来源尺度条件阻断：现有 BFI/DI 可闭合 AP-source 分支，但不能推出当前 full-S non-AP KLS-ext。最后剩余改写为 `NewFullSTheoremInputOrAPSourceLift`。

## 1. 结构律

The final primary-source check is not a missing citation. BFI Theorem 10, correctly located in the 1986 Acta Math paper, closes AP-source discrepancies with positive level slack, but the current remaining branch is non-AP WFD. The DI/Maynard Kloosterman J-scale cannot supply the custom full-S KLS-ext theorem when s=q=1/2, since n+2r+5s+q<=2 already fails before adding n and r. Therefore deriving FullS-KLS-ext from existing DI/BFI primary sources is rejected.

```text
previous terminal:
  DIBFIPrimarySourceSpecializationProof;

new terminal:
  NewFullSTheoremInputOrAPSourceLift;

expansion:
  ['NewFullSTheoremInput', 'APSourceLift'].
```

## 2. 汇总

- `primary_source_specialization_closed=false`。
- `closed_nogo_gates=['PriorPrimarySourceGapAvailable', 'BFIPrimarySourceCorrected', 'BFIAPAtomOnly', 'DIJScaleFullSObstruction', 'DIBFIPrimarySourceSpecializationRejected']`。
- `open_nogo_gates=['NewFullSTheoremInput', 'APSourceLift']`。
- `terminal_gap_after_router=NewFullSTheoremInputOrAPSourceLift`。

## 3. No-go 账本表

| gate | closed | evidence | remaining | next target |
| --- | --- | --- | --- | --- |
| `PriorPrimarySourceGapAvailable` | `true` | 上一层已把外部合同版闭合后剩余单点定为 DIBFIPrimarySourceSpecializationProof。 | none at prior-frontier level | `BFIPrimarySourceCorrected` |
| `BFIPrimarySourceCorrected` | `true` | Maynard 交叉来源显示 BFI Theorem 10 主来源是 1986 Acta Math；外部索引已修正。 | 需逐步替换历史 BFI1987 别名；但主定理定位不再含糊。 | `BFIAPAtomOnly` |
| `BFIAPAtomOnly` | `true` | BFI Theorem 10 直接估计 well-factorable prime-AP discrepancy，不直接估计 non-AP KE-13/WFD full-S kernel。 | 若能证明 APSourceLift，则可回到直接 BFI；否则不能用 AP 定理关闭 non-AP kernel。 | `APSourceLiftOrNewFullSTheoremInput` |
| `DIJScaleFullSObstruction` | `true` | DI/Maynard W4 condition n+2r+5s+q<=2 fails for q=s=1/2: minimal left side=3/1>2/1。 | 现有 DI/Maynard J-scale 不能推出 full-S KLS-ext。 | `NewFullSTheoremInput` |
| `DIBFIPrimarySourceSpecializationRejected` | `true` | 现有 BFI AP theorem 与 DI J-scale 不推出本文自定义 full-S KLS-ext。 | 必须新增更强 full-S 外部定理，或证明当前 non-AP 对象可提升回 AP-source。 | `NewFullSTheoremInputOrAPSourceLift` |
| `NewFullSTheoremInput` | `false` | 仓库尚无强于现有 DI/BFI J-scale、直接覆盖 S≈X^(1/2) full-S kernel 的定理。 | 需要独立外部深定理或新证明。 | `NewFullSTheoremInputOrAPSourceLift` |
| `APSourceLift` | `false` | 此前 AP-source 分支已闭合，但 non-AP generic WFD fallback 没有无损提升回 AP discrepancy。 | 若证明该提升，可使用 BFI1986-Theorem10 直接闭合。 | `NewFullSTheoremInputOrAPSourceLift` |

## 4. 当前结论

不能把 `DIBFIPrimarySourceSpecializationProof` 标记为已证。当前真实剩余为：

```text
NewFullSTheoremInputOrAPSourceLift:
  NewFullSTheoremInput;
  APSourceLift.
```

这一步排除的是“现有 DI/BFI 主来源可直接推出 full-S KLS-ext”的最后隐含跳步。
