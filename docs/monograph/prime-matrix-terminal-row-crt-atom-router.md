# Prime Matrix 终端行 CRT 原子路由

**状态：** `specified_terminal_atoms_closed_but_global_localization_open`

P=5 的 23,29 与 P=7 的 43,47,53 都是对应 M_{<=P} 周期中的单位原子；假设它们能被 <=P 小素数整除，与 CRT 余数向量直接矛盾。并且它们都小于下一素数平方，所以单位原子一旦存在就被平方根门强制为真实素数。可推广的严格部分是这个原子级引理；不可跳过的开放部分是证明任意大 P 的目标短行中必存在这样的单位原子。完整 CRT 周期对称性本身只给全周期均匀，不给短行局部化，因此全局路线仍回到局部化 P-CRT/Linnik=2、AP 零点包、Page 稀疏 moving singleton/非实零包残差或 signed payload/PDEC 前沿。

```text
next_direct_attack_target=TerminalRowReducedResidueExistenceOrLocalizedPCRTTransfer
fallback_target=PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2OrAPZeroPacketFrontier
page_frontier_target=PageExceptionalSingletonCarrierOrNonrealZeroPacketResidualBudget
row_column_unconditional_closed=false
```

## 1. 用户例子核查

### P=5

```text
M_le_P=30
base_primes=[2, 3, 5]
next_prime=7
last_row=[21, 22, 23, 24, 25]
next_row=[26, 27, 28, 29, 30]
last_row_units=[23]
next_row_units=[29]
```

| n | position | CRT vector mod q<=P | small factor <=P | unit | forced prime | mirror mod M |
| --- | --- | --- | --- | --- | --- | --- |
| `23` | `last_row` | `{'2': 1, '3': 2, '5': 3}` | `None` | `true` | `true` | `7` |
| `29` | `next_row` | `{'2': 1, '3': 2, '5': 4}` | `None` | `true` | `true` | `1` |

### P=7

```text
M_le_P=210
base_primes=[2, 3, 5, 7]
next_prime=11
last_row=[43, 44, 45, 46, 47, 48, 49]
next_row=[50, 51, 52, 53, 54, 55, 56]
last_row_units=[43, 47]
next_row_units=[53]
```

| n | position | CRT vector mod q<=P | small factor <=P | unit | forced prime | mirror mod M |
| --- | --- | --- | --- | --- | --- | --- |
| `43` | `last_row` | `{'2': 1, '3': 1, '5': 3, '7': 1}` | `None` | `true` | `true` | `167` |
| `47` | `last_row` | `{'2': 1, '3': 2, '5': 2, '7': 5}` | `None` | `true` | `true` | `163` |
| `53` | `next_row` | `{'2': 1, '3': 2, '5': 3, '7': 4}` | `None` | `true` | `true` | `157` |

## 2. 可推广的严格引理

| name | statement |
| --- | --- |
| `specified atom CRT contradiction` | 若指定 n 在所有 q<=P 下均非零，则假设 n 可被 q<=P 整除立即与其 CRT 坐标矛盾。 |
| `terminal sqrt gate` | 若 1<n<p_next^2 且 gcd(n,M_{<=P})=1，则 n 为素数；否则最小素因子至少 p_next，合数至少 p_next^2。 |
| `complete wheel non-localization` | 完整 CRT 周期中单位残基的均匀和反射只给全周期身份，不给初始 P x P 或末端短行的点态存在性。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `SpecifiedTerminalAtomsSmallFactorAbsorptionImpossible` | `true` | `true` | 23,29,43,47,53 等指定原子在对应小素 CRT 向量中没有零坐标，不能被 <=P 小素数整除。 | none for specified atoms |
| `TerminalSqrtGate` | `true` | `true` | 若 n<p_next^2 且 n 对所有 q<=P 非零，则 n 不能为合数，故为素数。 | none for existing reduced atoms |
| `CompleteWheelSymmetryIdentity` | `true` | `true` | 完整 M_{<=P} 周期中单位残基按 CRT 周期重复，并在 n->-n 下反射配对。 | full-period identity only |
| `FullWheelSymmetryLocalizesToTerminalRows` | `false` | `false` | 完整周期单位残基均匀性不能自动保证任意给定短行中有单位残基。 | TerminalRowReducedResidueExistenceOrLocalizedPCRTTransfer |
| `GlobalTerminalRowNoMissingPrimeProved` | `false` | `false` | 要推广到全体奇素数，仍需证明末行或下一行总有 reduced atom，等价于短区间/点态 AP 输入。 | PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2OrAPZeroPacketFrontier |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只把用户给定终端例子变成严格 CRT 原子证书，不闭合全局行/列命题。 | PageExceptionalSingletonCarrierOrNonrealZeroPacketResidualBudget |

## 4. 最新活动基

```text
(TerminalRowReducedResidueExistenceOrLocalizedPCRTTransfer OR PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2 OR PageExceptionalSingletonCarrierOrNonrealZeroPacketResidualBudget OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件没有证明短行单位原子存在性、Linnik=2 型点态 AP、Page moving singleton 排斥、非实零包残差预算、signed payload、PDEC scope 或 DStructure/Rankin 晋级门。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-predecessor-gap-pcrt-uniformity-router.json` | `8569aefb62fc30395f527b8aaa3966bab18e6a0dfd5ed1d6dffb83a9acde57d6` |
| `docs/monograph/prime-matrix-localized-pcrt-transfer-linnik2-barrier-router.json` | `98232747aaf27a93f4cc68cc5bc8d29d80c5d0786bfeead635a6b42293ba6107` |
| `docs/monograph/prime-matrix-early-zero-gap-crt-asymmetry-router.json` | `9f10be0a0445eef5185d4e9d03dab884b330a0ae06b9ff9c7a0ffb910086a804` |
| `docs/monograph/prime-matrix-beta-gap-page-sparsity-router.json` | `eb53bcf1653d6b09c9d09c021a8418a1883bdc8cb3eba102ba0810ea3cefdc44` |
| `docs/monograph/claim-status-table.md` | `d490c8dc4baaaeaebbc6f5d33cb840b4a0e484d7b21f10716c3384956bc77666` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `46f82cd6921106c8d02fedbe681266f6bf6a31ac0fcab819dd348b2332f59f4d` |
| `docs/monograph/three-claims-formal-to-actual-critical-load-frontier.md` | `106b17a1b505da81db273579055f45bd6c1937123b3e1b333909ea5b88aa80de` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `284d63630a46bd46f3d15f2864378f92bd8a1f596c38ad0cc618a8c7eba68f76` |
