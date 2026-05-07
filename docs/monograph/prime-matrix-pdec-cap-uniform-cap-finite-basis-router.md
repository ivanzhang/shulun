# Prime Matrix PDEC-CAP 统一帽稳定有限基路由器

**状态：** `uniform_cap_stability_reduced_to_finite_cyclic_arc_cap_bounds`

统一帽稳定证书已从连续的 `(h,zeta,alpha)` 搜索压成有限循环弧 cap 质量界。固定 formal unit 后，字符像是有限循环集，方向帽只是循环弧预像；高质量弧 cap 回流 `SAE/refined PDEC/ColumnCRT/multiplicity`，反复细化也无同层循环。最新最窄剩余是有限循环弧 cap 质量界全集。

## 1. 有限循环弧律

The apparent continuum of cap-stability tests is finite at every fixed formal unit. For a nontrivial character chi_h on the finite signature group G, the coefficients Re(zeta chi_h(a)) are points on a finite cyclic image. Varying zeta and alpha only selects preimages of circular arcs in that image; the cap set changes only when an endpoint crosses one of the finitely many image points. Thus uniform cap stability is equivalent to finite cyclic-arc cap mass bounds for every nontrivial character. Any arc whose mass exceeds the localization threshold is already a named cap return.

```text
UniformCapStabilityCertificateForRankTwoPrimitiveKernels
  for each nontrivial character chi_h on finite G:
    direction caps C_alpha(h,zeta) are preimages of cyclic arcs;
    zeta/alpha continuum changes only at finite arc endpoints;
  therefore check finite cyclic arc cap basis;
  high arc mass => SAE / refined PDEC / ColumnCRT / multiplicity;
  all arc masses below threshold => uniform cap stability.

remaining:
  FiniteCyclicArcCapMassBoundsForRankTwoPrimitiveKernels.
```

## 2. 汇总

- `uniform_cap_finite_basis_closed=true`。
- `finite_cyclic_arc_cap_mass_bounds_closed=false`。
- `row_column_unconditional_closed=false`。
- `narrowest_next_hardpoint=FiniteCyclicArcCapMassBoundsForRankTwoPrimitiveKernels`。
- `open_final_gates=['FiniteCyclicArcCapMassBoundsForRankTwoPrimitiveKernels']`。

## 3. 审查表

| gate | closed | blocks final | evidence | meaning |
| --- | --- | --- | --- | --- |
| `UniformCapStabilityActive` | `true` | `false` | UniformCapStabilityCertificateForRankTwoPrimitiveKernels | 上一层已把二秩 primitive 核不等式改写为统一帽稳定证书。 |
| `FiniteSignatureGroupRegistered` | `true` | `false` | finite signature group G and count function g | 每个 PDEC formal unit 的帽都发生在有限签名群或有限签名集上。 |
| `AllDirectionsUseCharacters` | `true` | `false` | all h!=0 and zeta directions in U_CRT | 需要检查的方向来自非平凡字符及外向实方向，而不是无限维自由函数。 |
| `ZetaAlphaContinuumReducedToCyclicArcs` | `true` | `false` | preimage of a circular arc under chi_h | 固定非平凡字符后，任意方向帽都是字符像有限循环序上的弧预像；阈值只在有限临界弧上改变。 |
| `HighArcCapRoutesNamed` | `true` | `false` | SAE / refined PDEC / ColumnCRT / Multiplicity | 若某个有限循环弧 cap 质量达到帽定位阈值，它必须回流命名出口，不能保留为 cap-stable 核。 |
| `FiniteArcRefinementNoCycle` | `true` | `false` | finite Boolean algebra of cap arcs or new-layer entropy | 有限弧 cap 反复细化只会生成有限 Boolean 分区；升层则进入 new-layer PDEC/CleanKLS。 |
| `UniformCapFiniteBasisDerived` | `true` | `false` | all zeta/alpha caps reduce to finite cyclic arc cap basis | 统一帽稳定证书已从连续方向帽族压成有限循环弧 cap 质量界。 |
| `FiniteCyclicArcCapMassBoundsForRankTwoPrimitiveKernels` | `false` | `true` | global mass bounds for every finite character-arc cap not submitted | 剩余全球硬点是证明所有二秩 primitive 同 formal unit 核的有限循环弧 cap 质量低于阈值，或输出命名回流。 |

## 4. 剩余

下一步直接攻 `FiniteCyclicArcCapMassBoundsForRankTwoPrimitiveKernels`：对每个二秩以上 primitive 同 formal unit 核、每个非平凡字符和每个有限循环弧，证明该弧预像上的坏窗质量低于帽定位阈值，或输出命名 cap 回流证书。
