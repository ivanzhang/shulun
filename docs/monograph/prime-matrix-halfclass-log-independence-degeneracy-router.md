# Prime Matrix Half-class Log Independence Degeneracy Router

**状态：** `twist_pair_orbit_lock_routed_to_log_independence_zero_support_degeneracy_open`

本步继续下钻 `QuadraticTwistPairCharacterOrbitLockExclusionOrColumnCRTPDEC`。若 punctured 半类出现精确平铺，则任意两个不同 residue 的 theta 值相等。但 theta 是对应素数集合乘积的对数；唯一分解给出不同 residue 的正 theta 值不可能精确相等。因此精确轨道锁只能退化为 `c=0` 且同半类除缺孔外全部 residue 在 `P^2` 内无素数到达。最新硬点压成 `PuncturedHalfClassZeroSupportDegeneracyExclusionOrColumnCRTPDEC`。

```text
log_prime_product_independence_closed=true
positive_exact_punctured_flatness_excluded=true
orbit_lock_routed_to_zero_support_degeneracy=true
punctured_halfclass_zero_support_degeneracy_excluded=false
row_column_unconditional_closed=false
next_direct_attack_target=PuncturedHalfClassZeroSupportDegeneracyExclusionOrColumnCRTPDEC
```

## 1. 公式账本

| item | formula |
| --- | --- |
| `residue prime support` | `S_a(P)={ell prime: ell<=P^2, ell!=P, ell=a mod P}` |
| `theta support product` | `theta_a=log(prod_{ell in S_a(P)} ell)` |
| `log-prime independence` | `theta_a=theta_b and a!=b imply S_a(P)=S_b(P)=empty` |
| `exact punctured flatness degeneration` | `P>=7 and theta_{a0u}=c for all u!=1 in Q imply c=0 and S_{a0u}=empty for every u!=1` |
| `new hardpoint` | `exclude punctured half-class zero-support degeneracy or register ColumnCRT/PDEC/moving-family` |

## 2. 分支压缩

| branch | route | status | meaning |
| --- | --- | --- | --- |
| `QuadraticTwistPairCharacterOrbitLockExclusionOrColumnCRTPDEC` | PuncturedHalfClassZeroSupportDegeneracyExclusionOrColumnCRTPDEC | sharpened but open | 全配对角色轨道锁若是精确平铺，则正平铺由素数对数独立性排除，只剩 punctured 半类全零支撑退化。 |
| `positive exact half-class flatness` | log-prime product independence | closed as algebraic identity | 不同 residue 的素数支撑互不相交，两个正 theta 值不可能完全相等。 |
| `all-pair orbit lock` | punctured zero-support degeneracy | not excluded in corpus | 剩余出口要求同半类除缺孔外没有任何 P^2 内素数到达。 |
| `PuncturedHalfClassZeroSupportDegeneracyExclusionOrColumnCRTPDEC` | exclude zero-support degeneracy or route to ColumnCRT/PDEC/moving-family | not proved in corpus | 这是当前非实 AP 分支的最新最窄接口。 |

## 3. 有限诊断

有限扫描只用于定位零支撑退化，不作为无限证明输入。

```text
min_p=7
max_p=1000
prime_moduli_checked=165
punctured_halfclass_instances_checked=75952
min_active_punctured_support_count=2
degenerate_instances_found=0
```

### 3.1 最接近零支撑退化的记录

| P | halfclass | puncture | puncture support | active punctured | zero punctured | first active punctured residues |
| --- | --- | --- | --- | --- | --- | --- |
| `7` | `quadratic_residue` | `1` | `2` | `2` | `0` | `[2, 4]` |
| `7` | `quadratic_residue` | `2` | `3` | `2` | `0` | `[1, 4]` |
| `7` | `quadratic_nonresidue` | `3` | `3` | `2` | `0` | `[5, 6]` |
| `7` | `quadratic_residue` | `4` | `1` | `2` | `0` | `[1, 2]` |
| `7` | `quadratic_nonresidue` | `5` | `3` | `2` | `0` | `[3, 6]` |
| `7` | `quadratic_nonresidue` | `6` | `2` | `2` | `0` | `[3, 5]` |
| `11` | `quadratic_residue` | `1` | `3` | `4` | `0` | `[3, 4, 5, 9]` |
| `11` | `quadratic_nonresidue` | `2` | `4` | `4` | `0` | `[6, 7, 8, 10]` |
| `11` | `quadratic_residue` | `3` | `3` | `4` | `0` | `[1, 4, 5, 9]` |
| `11` | `quadratic_residue` | `4` | `3` | `4` | `0` | `[1, 3, 5, 9]` |
| `11` | `quadratic_residue` | `5` | `2` | `4` | `0` | `[1, 3, 4, 9]` |
| `11` | `quadratic_nonresidue` | `6` | `3` | `4` | `0` | `[2, 7, 8, 10]` |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreviousTwistPairTargetImported` | `true` | `true` | 上一层把 ratio-Fourier 锁压成二次扭曲角色配对轨道锁。 | QuadraticTwistPairCharacterOrbitLockExclusionOrColumnCRTPDEC |
| `LogPrimeProductIndependenceClosed` | `true` | `true` | 不同 residue 的 theta 精确相等只能同时为空支撑。 | none |
| `PositiveExactPuncturedFlatnessExcluded` | `true` | `true` | P>=7 时，punctured 半类的正精确平铺与唯一分解矛盾。 | none |
| `OrbitLockRoutedToZeroSupportDegeneracy` | `true` | `true` | 精确轨道锁若持久，只能退化为 punctured 半类全零支撑。 | PuncturedHalfClassZeroSupportDegeneracyExclusionOrColumnCRTPDEC |
| `PuncturedHalfClassZeroSupportDegeneracyExcluded` | `false` | `false` | 当前语料尚未自足排斥同半类除缺孔外全无 P^2 内素数到达。 | PuncturedHalfClassZeroSupportDegeneracyExclusionOrColumnCRTPDEC |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只排除正精确平铺，不证明行/列命题。 | global final inputs remain open |

## 5. 最新活动基

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn OR ((QuadraticHalfClassSquareScaleBiasMarginTheorem OR EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale) AND PuncturedHalfClassZeroSupportDegeneracyExclusionOrColumnCRTPDEC)) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件排除的是精确正平铺。它没有证明 punctured 半类全零支撑退化不可能，也没有排斥相应 ColumnCRT/PDEC/moving-family 出口。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-halfclass-twist-pair-character-lock-router.json` | `7bbb273f91e774b561791f52bf3ed36aa1b4e537bba97f67364f47b3d718546f` |
| `docs/monograph/prime-matrix-halfclass-ratio-fourier-lock-router.json` | `59af5b66fc0a0beec9168743d20a95339e546f96aed9185a2fed627ac137f184` |
| `docs/monograph/claim-status-table.md` | `46e354c13973286f6530ccbf5604d797bc03d41ca611b91822f1079dbdbd22a8` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `c1c4d5dfd96d34b1d2b37bbcd3266049643b60ccb0339f697241abfa6c89876a` |
| `docs/monograph/three-claims-formal-to-actual-critical-load-frontier.md` | `3492c9a36ad2f7ea20c8f56e5c135c9dfc471ef1d06d53858ce672363aba0ad7` |
| `docs/final-proof-draft.md` | `c8958bc1f15441975c2f7c2b206609eb88fa43adc21313e26742b3bb1addea9b` |
| `docs/prime-density-waves-X.md` | `512245acdfc1bf8085de9e6de6580f41acdb1c05d9039ea44f84cf82751626fe` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `e9a8dfcfc7d001b13aa635be5f23e9dee8851c2bf9281c743d670659aa10d963` |
