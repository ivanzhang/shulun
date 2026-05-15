# Prime Matrix square-phase low-alpha z=61 fixed-core cycle ledger

**状态：** `z61_positive_lift_signed_sum_reenters_fixed_core_dyadic_cycle_open`

当前 z=61 low-alpha 剩余不是新的自由局部参数：positive-lift carry 纤维接入 five-term signed-sum 后，经 dominant peel、terminal forcing、branch margin、offset-55 halfmod、core quotient lock、固定核心 dyadic balance，又回到同一个 `--++- / carry=6 / r=26951` positive-lift carry 门。该账本闭合的是 formal-unit 同一性；全局仍需证明固定核心回流不能持久，或排斥 PersistentPhase-PDEC。

```text
chain_step_count=23
all_local_bridges_closed=true
cycle_returns_to_same_carry_signed_sum_gate=true
z61_fixed_core_cycle_ledger_closed_for_formal_unit=true
fixed_core_cycle_global_nonpersistence_proved=false
row_column_unconditional_closed=false
```

## 1. 闭环锚点

| field | value |
| --- | --- |
| target | `unbalanced<=8, omega=4, shell=(8D,16D]` |
| core | `4807=[11, 19, 23]` |
| M, q4, q2 | `57684, 37, 71` |
| selected root | `26951` |
| selected carry/sign | `6 / --++-` |
| peel sign | `++---` |
| selected signed sum | `373055` |
| halfmod flip | `28842`, separation `-55` |
| dyadic positive quotients | `[2, 4]` |

## 2. 链条账本

| step | certificate | closed key | closed | next target |
| ---: | --- | --- | --- | --- |
| 1 | `positive_lift_carry_to_signed_sum` | `positive_lift_carry_to_signed_sum_bridge_closed_for_sample` | true | `FiveTermSignedSumIntervalResidueGlobalBoundOrSumResiduePDEC` |
| 2 | `signed_sum_residue_gate` | `all_signed_sum_residue_gates_closed` | true | `FiveTermSignedSumIntervalResidueGlobalBoundOrSumResiduePDEC` |
| 3 | `dominant_peel` | `all_dominant_peels_closed` | true | `DominantPeelSignedSumGlobalBoundOrPeelPDEC` |
| 4 | `terminal_sign_forcing` | `all_terminal_sign_forcings_closed` | true | `TerminalSignForcingGlobalBoundOrTerminalPDEC` |
| 5 | `branch_decision_ledger` | `branch_decision_ledger_closed` | true | `GlobalBranchDecisionPatternBoundOrBranchDecisionPDEC` |
| 6 | `branch_decision_margin` | `branch_decision_margin_stability_proved_for_formal_unit` | true | `BranchDecisionMarginStabilityGlobalBoundOrMarginPDEC` |
| 7 | `margin_pdec_registration` | `margin_pdec_registration_closed` | true | `GlobalNoMarginCollapseOrMarginPDECExclusion` |
| 8 | `nearest_margin_collision` | `offset55_collision_pattern_closed_for_formal_unit` | true | `Offset55MarginCollisionExclusionOrOffsetPDEC` |
| 9 | `offset55_halfmod_flip` | `offset55_halfmod_flip_closed_for_formal_unit` | true | `HalfModulusFlipSeparationGlobalBoundOrHalfFlipPDEC` |
| 10 | `halfmod_factor_separation` | `halfmod_factor_separation_closed_for_formal_unit` | true | `HalfModulusFlipFactorSeparationGlobalBoundOrFactorPDEC` |
| 11 | `gap3_crt_structure` | `gap3_crt_structure_closed_for_formal_unit` | true | `GapThreeCRTStructureGlobalBoundOrGapPDEC` |
| 12 | `half_residue_gap_source` | `gap_source_closed_for_formal_unit` | true | `HalfResidueGapSourceGlobalBoundOrGapSourcePDEC` |
| 13 | `core_factor_residue_identity` | `core_factor_residue_identity_closed_for_formal_unit` | true | `CoreFactorResidueIdentityGlobalBoundOrCoreFactorPDEC` |
| 14 | `core_quotient_lock` | `quotient_lock_unique_positive_integer_solution_proved` | true | `CoreQuotientLockGlobalExclusionOrQuotientLockPDEC` |
| 15 | `quotient_lock_pdec_registration` | `quotient_lock_pdec_registration_closed` | true | `QuotientLockPDECExclusionByFixedCoreCheckOrGlobalTemplateBound` |
| 16 | `quotient_lock_fixed_core_bridge` | `quotient_lock_fixed_core_bridge_closed_for_sample` | true | `FixedCoreDyadicAbsorberGlobalizationOrPersistentPhasePDEC` |
| 17 | `fixed_core_dyadic_balance` | `fixed_core_dyadic_balance_lemma_closed_for_sample` | true | `PositiveDyadicLiftExistenceForFixedCoreOrMissingLiftPDEC` |
| 18 | `positive_lift_shifted_pair` | `positive_lift_shifted_pair_bridge_closed_for_sample` | true | `ShiftedSquareWindowGlobalBoundOrMissingLiftPDEC` |
| 19 | `positive_lift_root_selector` | `positive_lift_root_selector_bridge_closed_for_sample` | true | `CRTRootIntegralSelectorGlobalBoundOrMissingLiftPDEC` |
| 20 | `positive_lift_factor_gate` | `positive_lift_factor_gate_bridge_closed_for_sample` | true | `PrimeFactorLiftGateGlobalBoundOrMissingLiftPDEC` |
| 21 | `positive_lift_projection_gate` | `positive_lift_projection_gate_bridge_closed_for_sample` | true | `RootProjectionGateGlobalBoundOrMissingLiftPDEC` |
| 22 | `positive_lift_signed_projection` | `positive_lift_signed_projection_bridge_closed_for_sample` | true | `SignedCRTSupportCarryBoundOrMissingLiftPDEC` |
| 23 | `positive_lift_carry_layer` | `positive_lift_carry_layer_bridge_closed_for_sample` | true | `CarryLayerTargetFiberGlobalBoundOrMissingLiftPDEC` |

## 3. 证明边界

- 已闭合：当前 formal unit 的回流链条同一性，且没有引入新自由参数。
- 未闭合：固定核心回流的全局非持久性，或 PersistentPhase-PDEC 排斥。
- 下一目标：`FixedCoreCycleNonPersistenceOrPersistentPhasePDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-branch-decision-ledger-router.json` | `727ffcb802fd6a005bb546bd7708d1fafafe332f96a703cfcfb65753714d8d28` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-branch-decision-margin-router.json` | `b0657f1f734480164be0235a26ccf8ddb8c49e9ad4c3af257b3ed0de0e1640ae` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-core-factor-residue-identity-router.json` | `fca0924568678b13e471b25fa9bb90ee495cc642de76e23dfeec9d52689151f7` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-core-quotient-lock-router.json` | `abbde832ff4cea92c7e3cbec2f0ce7436b8e8d7d51670c8ab220c6eddb92bce5` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-fixed-core-dyadic-balance-lemma-router.json` | `7f3175f133abcd84096c6d522a5219f06547614f22eab2af265171e602fbbfe2` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-gap3-crt-structure-router.json` | `b3f4dcecab52175d2c003ce4ccac3c4c611318a88add2c5d593a440d98fda2d1` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-half-residue-gap-source-router.json` | `fa55b234b083c663516a43dff536d84fb66ad93d9ebbaf6e4109dc9d77b1288a` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-halfmod-factor-separation-router.json` | `bb92909f03c1a3f23cb67e6ea78733b26b3452627aaeef0a1884dafe0d00c338` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-margin-pdec-registration-router.json` | `a9b90b319ca2f4c0d0c5ebce61300e3fc565d402d702af55dd042d47939d17ca` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-nearest-margin-collision-router.json` | `3921407feb8f169db2f169b990378889f5302328e66e1d3f4cd9e735bff2ceec` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-offset55-halfmod-flip-router.json` | `b46ab34b1d1ca71dabb016823809049e3fb2e7546798cfc6c8457b31977c2871` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-carry-layer-bridge-router.json` | `1bc52831b0aacaceb4e4e3979b91b5fe0563a7b62361d08d6b3ebf166befeb48` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-carry-to-signed-sum-bridge-router.json` | `becac576708c76692573222901ee8da888f6c7545b38d9769dd83f3b58053f04` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-factor-gate-bridge-router.json` | `72589dcf151e37a2602f41b121da0f9576841e343d6fb4faf257b7d7274512b1` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-projection-gate-bridge-router.json` | `7038c8bfdfd00396f9e643e47812ce9d4d38279bc136faed20a5d1415f6f9525` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-root-selector-bridge-router.json` | `c66831f311c44073cdb40319bbf5be0d2b2871fa38f41759c97898b14a39289b` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-shifted-pair-bridge-router.json` | `25c354e6440e1f1f9a945cf96f54b86c1f854f20fdd804c109c4685d06596772` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-signed-projection-bridge-router.json` | `ddccdcb319311d455f2c03fb85e7b1e55b8e9d401a88f1b72da9dc2f58868897` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-quotient-lock-fixed-core-bridge-router.json` | `b35e0485419f8a462a1dfc40b2bbdcf1aff19d97415544ef995dd00fb057e7fc` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-quotient-lock-pdec-registration-router.json` | `de2e08cee034406c26eafaed8b009646d6310f645e4c04d8d552f77cd5df216e` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-signed-sum-dominant-peel-router.json` | `bd408eb36e3b1a42cb0b24c07eff5dcbbc55684c54633cc1cb2ee90eb8952756` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-signed-sum-residue-gate-router.json` | `000bb6e26dec4b78c4215118876df470f40659f120db560c9bee5cf6a80fd0c7` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-terminal-sign-forcing-router.json` | `fe82db8bed8550d35f4778fde4f6f1dbd590e45035dc0aa9e3d97e385f0cd179` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_fixed_core_cycle_ledger_router.py` | `d9fe6acf9659cf710f610acc6b6b95d5347832651ab1e544b7710df7388a6be1` |
