# Prime Matrix strict 低乘子共同核最新同步路由器

**状态：** `low_multiplier_common_kernel_unnamed_exit_removed_return_descent_open`

`LowMultiplierCommonKernelColumnCRTOrPDECRoute` 已同步到最新前沿：共同核不再是无名出口。它先被旧证书拆成大成对差值锁或多源 fan-in；大成对分支已经压成有限商字母表，并在固定商型下具有 `h -> h/(bc)` 的严格高度下降；多源 fan-in 已压成 `q<2Lambda` 的有界小商，并接到稀疏终端 SAE/PDEC 与有效冷历史剪枝链。因此当前真正剩余不是重新证明低乘子分流，而是处理回流：若非持久分支经终端反级联、兄弟收费和 collar 宽度 LCM 又返回共同核，必须给出严格下降量；若没有严格下降，该返回链就是固定历史、ColumnCRT 或 PDEC。此返回下降/PDEC 账本尚未证明，所以行/列命题仍未无条件闭合。

```text
width_lcm_imports_low_kernel=true
low_kernel_pair_or_fanin_dichotomy_closed=true
pair_branch_finite_quotient_alphabet_closed=true
fixed_quotient_height_descent_imported=true
fanin_independent_alphabet_removed=true
sparse_terminal_independent_hardpoint_removed=true
effective_pruning_latest_sync_closed=true
sibling_charging_ledger_closed=true
unnamed_low_kernel_exit_removed=true
common_kernel_return_cycle_descent_or_pdec_proved=false
low_multiplier_common_kernel_excluded=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 同步链

| stage | closed fact | remaining |
| --- | --- | --- |
| width LCM return | collar width overflow routes to LCM height or low-multiplier common kernel | LowMultiplierCommonKernelColumnCRTOrPDECRoute |
| pair/fan-in split | K_t divides the lcm of pair gcds, hence pair or fan-in | LargePairKernelDifferenceColumnCRTExclusion OR MultiSourceKernelFanInSAEOrPDECExclusion |
| large pair quotient alphabet | g=kb, g'=k(b+a), 1<=b,b+a<2Lambda | FixedQuotientTypePDECColumnCertificateExclusion OR BoundedQuotientTypeSAEAbsorption |
| fixed quotient descent | fixed coprime quotient gives h -> h/(bc) with bc>=2 | threshold collapse, fixed PDEC, or LCM height |
| fan-in bounded quotient | g_t=K_t q_t with q_t<2Lambda; cover hypergraph adds no new alphabet | SparseTerminalHistorySAEAbsorptionOrPDECExclusion |
| sparse terminal sync | finite history encoding and nonpersistent SAE formula are available | EffectiveColdHistoryPruningOrHotFixedReturnTheorem |
| terminal anti-cascade return | effective pruning latest sync reaches sibling cold-window charging and collar width LCM | CommonKernelReturnCycleDescentOrPDECLedger |

## 2. 固定商型下降样本

| h | b | c | bc | h/(bc) | divides | strict descent |
| --- | --- | --- | --- | --- | --- | --- |
| `840` | `1` | `2` | `2` | `420` | `true` | `true` |
| `2310` | `2` | `3` | `6` | `385` | `true` | `true` |
| `30030` | `3` | `5` | `15` | `2002` | `true` | `true` |
| `510510` | `5` | `7` | `35` | `14586` | `true` | `true` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `WidthLCMImportsLowKernel` | `true` | `true` | 最新兄弟 collar 宽度压缩把剩余导向低乘子共同核。 | LowMultiplierCommonKernelColumnCRTOrPDECRoute |
| `LowKernelPairOrFanInDichotomyClosed` | `true` | `true` | 低乘子共同核已拆成大成对差值锁或多源 fan-in。 | LargePairKernelDifferenceColumnCRTExclusion OR MultiSourceKernelFanInSAEOrPDECExclusion |
| `PairBranchFiniteQuotientAlphabetClosed` | `true` | `true` | 大成对核差值锁已压成有限商字母表。 | FixedQuotientTypeColumnCRTOrPDECExclusion OR BoundedQuotientTypeSAEAbsorption |
| `FixedQuotientHeightDescentImported` | `true` | `true` | 固定互素商型递归每步使正式频率高度至少折半。 | FixedQuotientTypeColumnCRTOrPDECExclusion |
| `FanInIndependentAlphabetRemoved` | `true` | `true` | 多源 fan-in 只留下有界小商，不再产生独立无限字母表。 | BoundedQuotientTypeSAEAbsorption OR SparseTerminalHistorySAEAbsorptionOrPDECExclusion |
| `SparseTerminalIndependentHardpointRemoved` | `true` | `true` | 非持久 SAE/稀疏终端已同步到有效冷历史剪枝。 | EffectiveColdHistoryPruningOrHotFixedReturnTheorem |
| `UnnamedLowKernelExitRemoved` | `true` | `true` | 低乘子共同核不再是无名出口；所有分支已命名为 PDEC/SAE/热回流/返回链。 | FixedQuotientTypePDECColumnCertificateExclusion OR BoundedQuotientTypeSAEAbsorption OR TerminalCoreHotDivisorWindowPDECorSAE OR CommonKernelReturnCycleDescentOrPDECLedger |
| `CommonKernelReturnCycleDescentOrPDECProved` | `false` | `false` | 若非持久分支经终端反级联回到兄弟 collar/LCM/共同核，仍需证明严格下降；否则要登记固定历史或 PDEC。 | CommonKernelReturnCycleDescentOrPDECLedger |
| `LowMultiplierCommonKernelExcluded` | `false` | `false` | 当前只删除无名共同核出口，没有排斥所有命名出口。 | CommonKernelReturnCycleDescentOrPDECLedger AND FixedQuotientTypePDECColumnCertificateExclusion AND TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到早期零行反例链的终端矛盾。 | CommonKernelReturnCycleDescentOrPDECLedger AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一步最窄点

- 主攻：`CommonKernelReturnCycleDescentOrPDECLedger`。
- 含义：证明共同核回流链每次都降低一个正式良基量；若不能降低，则该回流链必须登记为固定历史、ColumnCRT 或 PDEC。
- 边界：本步只删除无名共同核出口，不排斥所有命名出口，不宣称行/列命题无条件闭合。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-strict-cold-window-sibling-charging-router.json` | `be05fb4b2dee03515ca4eea8e086eff6341c0e04d69da9501072cccf74414591` |
| `docs/monograph/prime-matrix-strict-effective-pruning-latest-sync-router.json` | `ed70b01806e4ff545cc7ab3d3d051009e33cf6e1e43190141f5278ed9d73c126` |
| `docs/monograph/prime-matrix-strict-fixed-quotient-density-transfer-router.json` | `f2b0c000ddb05b2504eb547a318d94a219fd70ac27ff34089b01524caa1688f7` |
| `docs/monograph/prime-matrix-strict-fixed-quotient-type-columncrt-router.json` | `2604e2de93bc17bbe7678dddccf958b8a747714286d2c1ab8d5734246be78733` |
| `docs/monograph/prime-matrix-strict-iterated-scaled-core-density-router.json` | `5e2e4c2cac4e9f0e2afcad98e083f52bf5b4e980b7c516d186a934b65ba4f64f` |
| `docs/monograph/prime-matrix-strict-iterated-threshold-collapse-router.json` | `22c87665aa776cfb358736a8c6624361ad9cba95830f46c56ad95bc40ff99e74` |
| `docs/monograph/prime-matrix-strict-large-pair-kernel-difference-router.json` | `fc58ab04aae06d90742f61628fa0240994fc110225ce6a1dbce763eb05efe7cc` |
| `docs/monograph/prime-matrix-strict-low-multiplier-common-kernel-router.json` | `314a0d156a5301b0a4eaedfe4c782f06b69c02ff5f2bd8d575e7c3c57e2f54a8` |
| `docs/monograph/prime-matrix-strict-multisource-fanin-small-quotient-router.json` | `89d82ac6d13034c0b3db3d67585df32e9cc2ad534ddec16ddc9c6eb89c22eda4` |
| `docs/monograph/prime-matrix-strict-sibling-collar-width-lcm-kernel-router.json` | `973a1c986598cb27dd132354715b336eae7938103c89d09da451123f2ade08de` |
| `docs/monograph/prime-matrix-strict-sparse-terminal-absorption-latest-sync-router.json` | `4ec39bb552f9cc5f120b20ae937e8569370f7aa75322dda2d4ee669b2897985b` |
| `docs/monograph/prime-matrix-strict-terminal-cold-window-anticascade-attack-router.json` | `c2ef211342a04f992f35f62a595d3c1647663d1a9fde5d1e78ff57c735bf63d6` |
| `experiments/prime_matrix_strict_low_multiplier_common_kernel_latest_sync_router.py` | `b7a1e254819e811d7559ea1706731e016da8533290e85bb327cd8361e420d283` |
