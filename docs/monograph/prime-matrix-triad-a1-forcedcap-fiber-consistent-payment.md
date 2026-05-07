# Triad-A1 ForcedCap Fiber-Consistent 支付审计

**状态：** `forcedcap_fiber_consistent_payment_incidence_materialized`

ForcedCap 的 actual-payment incidence 已加入 fiber 一致性：同一 phase 的所有低洞必须来自同一个 CRT fiber y 的完成态。该账本仍是 incidence 上界，不等同于最小支付选择 Gamma；但它比裸 exposure 更接近 ActualPaymentStitching，下一步可在此基础上做持久 MFU 或 CleanKLS 二分。

## 1. 结构语义

这一步把 APS 中的 `Gamma` 约束推进一层：实际完成态不是任意选择暴露边，而是由同一个 fiber 参数 `y` 同时决定所有高素数 residue。

```text
phase t 固定；
row = t + Qy；
同一个 y mod high_period 必须覆盖该 phase 的全部低洞。
```

因此本报告统计的是所有完成 `y` 诱导出的 fiber-consistent cover incidence。

## 2. 汇总

- `forced_cap_count=24`。
- `unique_phase_cache_count=4316`。
- `all_intersections_recomputed=True`。
- `all_completion_counts_match_m_vector=True`。
- `route_counts={'FiberConsistentPaymentMFUOrDistributedCleanKLS': 24}`。

## 3. P 级汇总

| P | caps | max cover/demand | max residue/demand | max colres/demand | max active-prime/completion | max DP states |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 43 | 12 | 1.04206 | 0.021273 | 0.0275565 | 0.973625 | 1024 |
| 47 | 12 | 1.05528 | 0.0240372 | 0.0433302 | 0.968045 | 4096 |

## 4. Cap 明细

| P | alpha | h | dir | mass | demand | cover/demand | max residue/demand | max colres/demand | max active-prime/completion | route |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 43 | 0 | 805 | 0.25 | 520444886 | 3681774070 | 1.04174 | 0.0182644 | 0.0208703 | 0.969283 | `FiberConsistentPaymentMFUOrDistributedCleanKLS` |
| 43 | 0 | 1505 | 0.75 | 520266260 | 3680568532 | 1.04174 | 0.0184065 | 0.0210262 | 0.969283 | `FiberConsistentPaymentMFUOrDistributedCleanKLS` |
| 43 | 0.5 | 805 | 0.25 | 417617864 | 2927527528 | 1.04206 | 0.0195326 | 0.0242935 | 0.966074 | `FiberConsistentPaymentMFUOrDistributedCleanKLS` |
| 43 | 0.5 | 1505 | 0.75 | 417617864 | 2927527528 | 1.04206 | 0.0195326 | 0.0242935 | 0.966074 | `FiberConsistentPaymentMFUOrDistributedCleanKLS` |
| 43 | 0 | 770 | 0.5 | 382559424 | 2767127028 | 1.03973 | 0.0190149 | 0.0275565 | 0.973625 | `FiberConsistentPaymentMFUOrDistributedCleanKLS` |
| 43 | 0 | 1540 | 0.5 | 382559424 | 2767127028 | 1.03973 | 0.0190149 | 0.0275565 | 0.973625 | `FiberConsistentPaymentMFUOrDistributedCleanKLS` |
| 43 | 0.5 | 1155 | 0 | 295544368 | 2122220360 | 1.0395 | 0.021273 | 0.0262624 | 0.971395 | `FiberConsistentPaymentMFUOrDistributedCleanKLS` |
| 43 | 0.5 | 1155 | 0.5 | 295544368 | 2122220360 | 1.0395 | 0.021273 | 0.0262624 | 0.971395 | `FiberConsistentPaymentMFUOrDistributedCleanKLS` |
| 43 | 0.9 | 1155 | 0 | 295544368 | 2122220360 | 1.0395 | 0.021273 | 0.0262624 | 0.971395 | `FiberConsistentPaymentMFUOrDistributedCleanKLS` |
| 43 | 0.9 | 1155 | 0.5 | 295544368 | 2122220360 | 1.0395 | 0.021273 | 0.0262624 | 0.971395 | `FiberConsistentPaymentMFUOrDistributedCleanKLS` |
| 43 | 0.9 | 1155 | 0 | 295544368 | 2122220360 | 1.0395 | 0.021273 | 0.0262624 | 0.971395 | `FiberConsistentPaymentMFUOrDistributedCleanKLS` |
| 43 | 0.9 | 1155 | 0.5 | 295544368 | 2122220360 | 1.0395 | 0.021273 | 0.0262624 | 0.971395 | `FiberConsistentPaymentMFUOrDistributedCleanKLS` |
| 47 | 0 | 665 | 0.25 | 14307723048 | 109225010520 | 1.05521 | 0.0222071 | 0.0310044 | 0.965289 | `FiberConsistentPaymentMFUOrDistributedCleanKLS` |
| 47 | 0 | 1645 | 0.75 | 14240169000 | 108692179512 | 1.05528 | 0.0223099 | 0.0311171 | 0.965215 | `FiberConsistentPaymentMFUOrDistributedCleanKLS` |
| 47 | 0 | 770 | 0.5 | 12484093560 | 96599086824 | 1.05227 | 0.0240372 | 0.0333722 | 0.967477 | `FiberConsistentPaymentMFUOrDistributedCleanKLS` |
| 47 | 0 | 1540 | 0.5 | 12484093560 | 96599086824 | 1.05227 | 0.0240372 | 0.0333722 | 0.967477 | `FiberConsistentPaymentMFUOrDistributedCleanKLS` |
| 47 | 0.5 | 1001 | 0.25 | 10529907264 | 79296544896 | 1.05459 | 0.0212294 | 0.0433302 | 0.960414 | `FiberConsistentPaymentMFUOrDistributedCleanKLS` |
| 47 | 0.5 | 1309 | 0.75 | 10529907264 | 79296544896 | 1.05459 | 0.0212294 | 0.0433302 | 0.960414 | `FiberConsistentPaymentMFUOrDistributedCleanKLS` |
| 47 | 0.5 | 1155 | 0 | 8638014624 | 67088446560 | 1.05198 | 0.0237918 | 0.0300795 | 0.968045 | `FiberConsistentPaymentMFUOrDistributedCleanKLS` |
| 47 | 0.5 | 1155 | 0.5 | 8638014624 | 67088446560 | 1.05198 | 0.0237918 | 0.0300795 | 0.968045 | `FiberConsistentPaymentMFUOrDistributedCleanKLS` |
| 47 | 0.9 | 1155 | 0 | 8638014624 | 67088446560 | 1.05198 | 0.0237918 | 0.0300795 | 0.968045 | `FiberConsistentPaymentMFUOrDistributedCleanKLS` |
| 47 | 0.9 | 1155 | 0.5 | 8638014624 | 67088446560 | 1.05198 | 0.0237918 | 0.0300795 | 0.968045 | `FiberConsistentPaymentMFUOrDistributedCleanKLS` |
| 47 | 0.9 | 1155 | 0 | 8638014624 | 67088446560 | 1.05198 | 0.0237918 | 0.0300795 | 0.968045 | `FiberConsistentPaymentMFUOrDistributedCleanKLS` |
| 47 | 0.9 | 1155 | 0.5 | 8638014624 | 67088446560 | 1.05198 | 0.0237918 | 0.0300795 | 0.968045 | `FiberConsistentPaymentMFUOrDistributedCleanKLS` |

## 5. 读法

如果某个 fiber-consistent 签名持久承担实际支付，它就是 MFU/PDEC 输入。
如果实际支付在这些 fiber-consistent 签名之间持续分散，则进入 CleanKLS/DLS。
