# Prime Matrix strict cold 产品支撑稀疏化路由器

**状态：** `cold_product_sparsification_reduced_to_overload_block_hot_kernel_or_rankin_open`

`ColdProductSupportSparsificationBeyondTauLedger` 已被压成 dyadic 过载块三分法：若总 cold 产品支撑超过 `P^0.18`，则某个产品 dyadic 块过载；过载块若局部集中，就登记为热除数密度/PDEC/SAE；若共享低乘子共同核，就进入共同核下降或 PDEC；若既不集中也无共同核，则只剩原始分散支撑，需要逐素数 Rankin/Euler 账本。本步关闭的是拆分和过载证书，不关闭三类终端排斥。

```text
dyadic_overload_certificate_closed=true
overload_block_structural_split_closed=true
hot_density_or_common_kernel_exclusion_proved=false
primitive_product_support_rankin_ledger_proved=false
cold_product_support_sparsification_beyond_tau_ledger_proved=false
cold_filtered_divisor_support_p018_envelope_proved=false
row_column_unconditional_closed=false
```

## 1. Dyadic 过载阈值

| P | dyadic blocks | P^0.18 | block overload threshold | meaning |
| ---: | ---: | ---: | ---: | --- |
| 100000 | 17 | 7.943282 | 0.467252 | if total support exceeds P^0.18, some block exceeds this threshold |
| 1000000 | 20 | 12.022644 | 0.601132 | if total support exceeds P^0.18, some block exceeds this threshold |
| 100000000 | 27 | 27.542287 | 1.020085 | if total support exceeds P^0.18, some block exceeds this threshold |
| 1000000000000 | 40 | 144.543977 | 3.613599 | if total support exceeds P^0.18, some block exceeds this threshold |

## 2. 过载块分支

| case | trigger | closed part | remaining | meaning |
| --- | --- | --- | --- | --- |
| dense_local_window | many cold products occupy one short multiplicative window with large reciprocal/count mass | hot density certificate can be produced | ShortWindowHotDivisorDensityPDECorSAEReturnExclusion | 局部集中不是普通除数支撑，而是热窗口/PDEC/SAE/ColumnCRT 终端。 |
| common_kernel_cluster | many products share a low multiplier kernel or repeated quotient type | free return cycle excluded; persistent finite type routes to PDEC | CommonKernelReturnCycleDescentOrPDECLedger | 共同核不能免费循环，但仍需排斥 PDEC/命名回流或完成预算吸收。 |
| primitive_dispersion | products stay sparse in every short window and avoid common-kernel clustering | this is the only remaining nonlocal support mode | PrimitiveProductSupportRankinLedger | 分散支撑必须由逐素数 Rankin/Euler 原始支撑账本给出小于 P^0.18 的总界。 |
| pure_tau_fallback | ignore cold structure and bound all divisors | recognized as a separate route | ExplicitDivisorSupportP018TailWithFiniteBoundaryCertificate | 需要显式除数尾界和有限边界；不能替代 cold 结构稀疏化。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ColdSparsificationTargetImported` | `true` | `true` | 上一层已把支撑域限制为商化后的 cold/nonpersistent/no-return 产品除数。 | ColdProductSupportSparsificationBeyondTauLedger |
| `DyadicOverloadCertificateClosed` | `true` | `true` | 若总 cold 产品支撑超过 P^0.18，则某个 dyadic 产品块必超过 P^0.18/(floor(log2 P)+1)。 | DyadicColdProductBlockOverloadCertificate |
| `PrimePowerSupportCascadeAlreadyRemoved` | `true` | `true` | 素数幂有序级联已经被产品商化压成指数状态，不能再作为本硬点阻塞。 | closed for support |
| `OverloadBlockStructuralSplitClosed` | `true` | `true` | 一个过载 dyadic 块若不进入热窗口，就必须进入共同核簇或原始分散支撑。 | ShortWindowHotDivisorDensityPDECorSAEReturnExclusion OR CommonKernelReturnCycleDescentOrPDECLedger OR PrimitiveProductSupportRankinLedger |
| `HotDensityOrCommonKernelExclusionProved` | `false` | `false` | 热窗口、PDEC/SAE/ColumnCRT 和共同核命名回流尚未全部排斥。 | ShortWindowHotDivisorDensityPDECorSAEReturnExclusion AND CommonKernelReturnCycleDescentOrPDECLedger |
| `PrimitiveProductSupportRankinLedgerProved` | `false` | `false` | 分散产品支撑的逐素数 Rankin/Euler 总界尚未给出。 | PrimitiveProductSupportRankinLedger |
| `ColdProductSupportSparsificationBeyondTauLedgerProved` | `false` | `false` | 本步完成过载块三分法，但未证明三类坏情形都被排斥或吸收。 | ShortWindowHotDivisorDensityPDECorSAEReturnExclusion AND CommonKernelReturnCycleDescentOrPDECLedger AND PrimitiveProductSupportRankinLedger |
| `ColdFilteredDivisorSupportP018EnvelopeProved` | `false` | `false` | cold 稀疏化未闭合，纯除数尾界也未闭合，因此产品支撑 envelope 仍开。 | ColdProductSupportSparsificationBeyondTauLedger OR ExplicitDivisorSupportP018TailWithFiniteBoundaryCertificate |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未形成排除早期零行反例链的终端矛盾。 | PrimitiveProductSupportRankinLedger AND UnifiedTerminalBudgetStrictInequality AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一步最窄点

- 主攻：`PrimitiveProductSupportRankinLedger`。
- 并行排斥：`ShortWindowHotDivisorDensityPDECorSAEReturnExclusion`、`CommonKernelReturnCycleDescentOrPDECLedger`。
- 备选：`ExplicitDivisorSupportP018TailWithFiniteBoundaryCertificate`。
- 边界：本步不声明 cold 产品支撑稀疏化已完成。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-strict-cold-filtered-divisor-support-router.json` | `c37398e74be3f912c6d753868ae8a973f7c61df6aa9fe834e420fd0a893ed7b7` |
| `docs/monograph/prime-matrix-strict-cold-history-prefix-branching-attack-router.json` | `ec7b96227c0b8752620609589fb1367d7483f2c46db66c705a13e68523002e86` |
| `docs/monograph/prime-matrix-strict-common-kernel-return-cycle-descent-router.json` | `133a5b59827c92d7e6e3b2cefcadf6f8c67b5b999fa6a1b5e7cbda57b8d4e671` |
| `docs/monograph/prime-matrix-strict-product-fiber-multiplicity-router.json` | `207253ea5e911247addc82f0e59edfdf1d034a6591d762a9928b493792500d4a` |
| `docs/monograph/prime-matrix-strict-weighted-reciprocal-common-divisor-envelope-router.json` | `9eef33defabab6ff2bddfd3627b5034984171d98db34e55d04cecee3b4d15f56` |
| `docs/monograph/prime-matrix-strict-windowed-reciprocal-divisor-density-router.json` | `1a367725b5a64d16447823d3bd619ac9955dd634eba4f31ad09326be20ccf57c` |
| `experiments/prime_matrix_strict_cold_product_support_sparsification_router.py` | `137ebfc70078c26387a37ce8561d39d0e8c6f367fe3e89dec5d2a748c7f721ff` |
