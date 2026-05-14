# Prime Matrix square-phase low-alpha squarefree PDEC 跨模数配对账本

**状态：** `cross_modulus_pairing_ledger_materialized_structural_invariant_open`

同一 `m` 纵向自取消被排除后，阈值包的可见取消只能在同一 `z` 层跨不同模数发生。本账本把每层正负包配对成边，并把未配对量压成 signed residual。这一步闭合的是算术收费格式：除 signed residual 外，所有阈值质量都可被异号包账面配对；尚未闭合的是这些配对边为何由结构强制、以及 residual 是否必然形成 PDEC/SAE。

```text
pairing_ledger_materialized=true
all_threshold_packet_mass_pairable_except_signed_residual=true
structural_cross_modulus_partner_invariant_proved=false
residual_signed_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. 配对总览

| total abs | residual after pairing | residual/abs |
| ---: | ---: | ---: |
| 1663.929367 | 108.368334 | 0.065128 |

## 2. 分层配对

| z | + packets | - packets | + abs | - abs | paired mass | residual side | residual | residual/abs | edges |
| ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: |
| 7 | 2 | 2 | 68.321811 | 84.917915 | 136.643621 | `negative` | 16.596104 | 0.108302 | 3 |
| 13 | 4 | 4 | 133.294909 | 162.932278 | 266.589818 | `negative` | 29.637369 | 0.100049 | 6 |
| 31 | 8 | 8 | 286.326561 | 269.626432 | 539.252864 | `positive` | 16.700129 | 0.030039 | 15 |
| 61 | 9 | 10 | 306.537365 | 351.972096 | 613.074730 | `negative` | 45.434731 | 0.068996 | 16 |

## 3. 重复配对边

| +m | -m | z values | occurrences | total paired | max paired |
| ---: | ---: | --- | ---: | ---: | ---: |
| 17 | 2 | `[31, 61]` | 2 | 126.711196 | 63.355598 |
| 3 | 2 | `[7, 13]` | 2 | 80.575708 | 40.287854 |
| 13 | 11 | `[13, 61]` | 2 | 42.321165 | 32.694455 |
| 33 | 11 | `[13, 61]` | 2 | 39.788121 | 32.029614 |
| 3 | 11 | `[31, 61]` | 2 | 39.183824 | 37.980460 |
| 42 | 5 | `[7, 31]` | 2 | 18.995425 | 14.029212 |
| 33 | 22 | `[13, 31]` | 2 | 1.605220 | 1.356190 |
| 3 | 37 | `[61]` | 1 | 39.084490 | 39.084490 |
| 13 | 22 | `[31]` | 1 | 32.694455 | 32.694455 |
| 33 | 34 | `[31]` | 1 | 30.922454 | 30.922454 |
| 38 | 51 | `[31]` | 1 | 28.385054 | 28.385054 |
| 42 | 22 | `[13]` | 1 | 28.033957 | 28.033957 |
| 33 | 53 | `[61]` | 1 | 24.520137 | 24.520137 |
| 42 | 2 | `[7]` | 1 | 23.067744 | 23.067744 |
| 13 | 2 | `[13]` | 1 | 23.067744 | 23.067744 |
| 23 | 51 | `[61]` | 1 | 21.473954 | 21.473954 |
| 42 | 34 | `[61]` | 1 | 21.122856 | 21.122856 |
| 29 | 19 | `[31]` | 1 | 21.061656 | 21.061656 |
| 258 | 19 | `[61]` | 1 | 20.210804 | 20.210804 |
| 29 | 22 | `[61]` | 1 | 19.178643 | 19.178643 |
| 38 | 22 | `[61]` | 1 | 17.179395 | 17.179395 |
| 38 | 53 | `[61]` | 1 | 15.065172 | 15.065172 |
| 42 | 58 | `[31]` | 1 | 14.004745 | 14.004745 |
| 29 | 34 | `[61]` | 1 | 10.343745 | 10.343745 |

## 4. 证明边界

- 已物化：每个 `z` 层阈值包的正负配对边和 residual。
- 已压缩：若能证明配对边有统一结构不变量，则 coefficient cancellation 可进入定理化预算。
- 未闭合：当前配对是账本配对，不是结构证明。
- 未闭合：若结构配对失败，需证明 residual 触发 `PDEC/SAE/ColumnCRT`，或排斥 residual signed PDEC。
- 下一目标：`StructuralCrossModulusPartnerInvariantOrResidualSignedPDECExclusion`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-selberg-remainder-attribution-router.json` | `0d1bdccce7bb03e1110bbd6a937b914c354c1d365d403abde42be12aebf9cba2` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-squarefree-pdec-cancellation-router.json` | `e8176a094913157954eb9a5f83013ef1c2f23c1898537fa639e724e70a573ab0` |
| `experiments/prime_matrix_square_phase_lowalpha_squarefree_pdec_pairing_ledger_router.py` | `b982d2cddc4ccca6c0b61fcddbc690a1665466383a732a0103dc62f32696a327` |
