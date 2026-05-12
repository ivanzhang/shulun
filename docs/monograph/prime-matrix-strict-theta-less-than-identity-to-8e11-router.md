# Prime Matrix strict theta(x)<x 到 8e11 外部表证书

**状态：** `theta_less_than_identity_to_8e11_external_closed_self_contained_table_hash_remains_open`

`theta(x)<x` 到 `8e11` 已在外部表路线闭合：`x<=1e8` 由本地有限筛检查素数跳点，`1e8<=x<=8e11` 由 Dusart `table_012` 的负 `b1` 列推出 `theta(x)<=x+b1*x/log(x)<x`。严格自足版仍缺 table_012 背后的原始有限计算/hash，但接受发表表格时，P5.1 的非 psi 输入已经齐备。

```text
theta_less_than_identity_to_8e11_external_closed=true
theta_less_than_identity_to_8e11_self_contained_closed=false
dusart_p51_full_theta_statement_closed=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 低段有限审计

| field | value |
| --- | ---: |
| `limit` | `100000000` |
| `prime_count` | `5761455` |
| `min_surplus_p_minus_theta_p` | `1.208240530771945` |
| `min_surplus_prime` | `3` |
| `max_theta_over_p` | `0.9999380296189334` |
| `max_ratio_prime` | `30909673` |
| `rounding_guard` | `1.0` |
| `audit_hash` | `aa0da4de5f728bb14a60da5ca009ccf65faf676d560ad0e7207afa3be3fec479` |

## 2. Dusart table_012 审计

| field | value |
| --- | --- |
| `interval_count` | `34` |
| `covers_from` | `100000000` |
| `covers_to` | `800000000000` |
| `continuous_cover_from_1e8_to_8e11` | `true` |
| `all_b1_negative` | `true` |
| `worst_margin_label` | `7E+11` |
| `worst_margin_right` | `800000000000` |
| `worst_relative_margin_at_right` | `3.64858605940022263617548004355683955461201439936035039524937E-7` |
| `table_transcription_hash` | `c3b1c58f995fc2521e7b7a30af82c8d10724f22570f97cf9c312d0708a81b0b0` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只补 P5.1 的低段 theta 输入，不使用真实零行缺席。 | 保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。 |
| `ThetaFiniteTableGateActive` | `true` | `true` | 上一证书已把下一最窄点设为 theta(x)<x 到 8e11 的有限表/证书。 | ThetaLessThanIdentityFiniteTableTo8e11SelfContainedLedger |
| `SmallSegmentSelfContainedFiniteAuditTo1e8` | `true` | `true` | 对 x<=1e8，仅需检查 theta 在素数跳点 p 的值；本地筛验算 theta(p)<p 有大于 1 的保护余量。 | aa0da4de5f728bb14a60da5ca009ccf65faf676d560ad0e7207afa3be3fec479 |
| `DusartTable012SourceIdentified` | `true` | `true` | 本地 arXiv 源 `/tmp/Estimates2.tex` 含 table_012 和 P5.1 使用点。 | 684c06ddd78deb4b7a7a6d0b3d275fc9fb3d8c1cca6e3acb8cdd8c9d9763befc |
| `DusartTable012NegativeB1Cover` | `true` | `true` | table_012 的每个区间都有 b1<0，故 theta(x)<=x+b1*x/log x < x，连续覆盖 [1e8,8e11]。 | c3b1c58f995fc2521e7b7a30af82c8d10724f22570f97cf9c312d0708a81b0b0 |
| `ThetaLessThanIdentityTo8e11ExternalClosed` | `true` | `true` | 低段有限审计加 Dusart table_012 外部表，给出 0<x<=8e11 上 theta(x)<x。 | external table accepted |
| `ThetaLessThanIdentityFiniteTableTo8e11SelfContainedLedger` | `false` | `false` | 严格作者侧自足版仍缺 table_012 的原始计算数据/hash；当前闭合为外部表路线。 | need reproducible finite computation/hash up to 8e11 for fully self-contained route |
| `P51NonPsiInputsReadyOnExternalLane` | `true` | `true` | P5.1 的两个非 psi 输入已在外部/半自足路线齐备：theta<x 到 8e11，psi-theta 中段下界。 | DusartP51ThetaUpperFullSyncLedger |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步关闭的是 P5.1 低段 theta 输入，不直接产生早期零行反例链与真实结构链的终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一最窄点

```text
DusartP51ThetaUpperFullSyncLedger
```

