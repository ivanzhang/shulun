# Prime Matrix AffineTwin endpoint-release cut-anchor ColumnCRT compression audit

**状态：** `current_sweep_cut_anchor_columncrt_compression_closed_global_open`

本审计继续下钻 cut-anchor sweep 的剩余出口：圆周 cut 是分析切口，不是新的 actual residue 自由度。若保留同一个 actual packet，全部 cut 都压回同一个 `P mod q(q-2)` 的 ColumnCRT 原子。

```text
cut_count=12
combined_crt_modulus=899
actual_anchor_pair=19:8
actual_representatives_used_by_cuts=[2687, 3586]
actual_crt_residue=889
unique_actual_crt_residue_count=1
cut_to_actual_residue_compression_factor=12
fixed_actual_columncrt_mass=1/899
naive_cut_counting_mass=12/899
mass_saved_by_cut_compression=11/899
same_orientation_cut_anchor_closed_current_sweep=true
fixed_q_fixed_residue_columncrt_registered=true
moving_family_candidate_q_values=[31, 43, 103]
cut_anchor_columncrt_compression_closed_current_sweep=true
```

## 1. cut 到 actual residue 的压缩

| cut | actual rep | actual residue | position | arc width | release | same-orientation closed |
| --- | ---: | ---: | --- | ---: | ---: | --- |
| `13:9->15:9` | 3586 | 889 | `arc_interior` | 869 | 1683 | `true` |
| `15:9->19:9` | 3586 | 889 | `arc_interior` | 838 | 1621 | `true` |
| `19:9->13:28` | 2687 | 889 | `arc_interior` | 819 | 1583 | `true` |
| `13:28->15:28` | 2687 | 889 | `arc_interior` | 869 | 1683 | `true` |
| `15:28->19:28` | 2687 | 889 | `arc_interior` | 838 | 1621 | `true` |
| `19:28->13:12` | 2687 | 889 | `arc_interior` | 761 | 1467 | `true` |
| `13:12->15:12` | 2687 | 889 | `arc_interior` | 869 | 1683 | `true` |
| `15:12->13:8` | 2687 | 889 | `arc_interior` | 873 | 1691 | `true` |
| `13:8->15:8` | 2687 | 889 | `arc_interior` | 869 | 1683 | `true` |
| `15:8->19:12` | 2687 | 889 | `arc_interior` | 896 | 1737 | `true` |
| `19:12->19:8` | 2687 | 889 | `arc_start` | 842 | 1675 | `true` |
| `19:8->13:9` | 3586 | 889 | `arc_end` | 558 | 1068 | `true` |

## 2. PDEC/ColumnCRT 输入对象

```text
schema=CutAnchorColumnCRT-PDEC
X=current q=31 actual-retained cut-anchor formal cut set
tau.P=P == 889 mod 899
tau.generator=P == 19 mod 29
tau.shifted_fill=P == 21 mod 31
registered_mass=1/899
```

## 3. 逃逸路线压缩

| escape | status | capacity object | reason |
| --- | --- | --- | --- |
| `same_orientation_actual_retained_cut_anchor` | `closed_current_sweep` | `none` | all cuts fail left D=8 or right D=1 formula gates |
| `fixed_q_fixed_actual_residue_orientation_changing` | `registered_columncrt_pdec` | `P == 889 mod 899` | changing orientation cannot create new cut mass while q and the actual slot residue stay fixed |
| `moving_q_or_moving_residue` | `routed_existing_moving_family_sae_columncrt` | `[31, 43, 103]` | moving q leaves the fixed cut ledger and enters the existing AffineTwin moving-family ledger |
| `cut_multiplicity_as_capacity_source` | `closed_current_sweep` | `1/899 not 12/899` | all cuts share the same actual CRT residue |

## 4. 显式容量矛盾点

若错误地把 `12` 个 cut 当成独立 actual 相位，质量会被记成 `12/899`。但所有 cut 的 actual representative 都同余于 `889 mod 899`，因此固定 `q=31`、固定 actual 槽的真实 ColumnCRT 质量只有 `1/899`，多出来的 `11/899` 是切口重数假象。

因此，same-orientation 已被 cut-anchor sweep 关闭后，固定 `q` 固定残基的方向改变逃逸不能获得新的容量；它只能作为 `CutAnchorColumnCRT-PDEC` 输入对象被登记。若 `q` 或残基移动，则已经离开本固定 cut 账本，回到既有 AffineTwin moving-family SAE/ColumnCRT 账本。

## 5. 结论边界

- 本步关闭当前 sweep 中“切口多重性作为容量来源”的解释。
- 本步仍不排斥全局 `CutAnchorColumnCRT-PDEC`，也不关闭行/列无条件命题。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-endpoint-release-cut-anchor-sweep-ledger.json` | `f1332cd35239182d09c025cba138653c105c0e5566ad4682f85860923dccd946` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-ledger.json` | `a8048685a2c6449b42ed5d2190aa47e75b20abf36a18e18c4d1ddb223cba033f` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-moving-family-sae-columncrt-ledger.json` | `2e401269ab68cb196babfb74e6f7b63c946ee9de37bc6ab5d502f49deaa7bf28` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sparse-sae-global-envelope-ledger.json` | `18a67505beef2a1ba7ec53a6088bb26da6a3955e2f63c02f5e215cfe171a8063` |
