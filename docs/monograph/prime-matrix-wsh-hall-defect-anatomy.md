# WSH-Hall 缺陷解剖审计

**状态：** `forced_defect_anatomy_not_global_proof`

本文档故意把已知可匹配行的半径压到最小 Hall 半径以下，观察缺陷如何显形。目标是为全局证明准备三出口模板：端点素数亏损、尾标签集中、轮筛/固定偏移相位集中。

## 参数

- `source_certificate`: `docs/monograph/prime-matrix-wsh-hall-phase-certificate.json`
- `max_records`: `44`
- `wheel_primes`: `[2, 3, 5, 7, 11, 13]`

## 摘要

- 输入证书行数：`44`。
- 分析行数：`44`。
- 强制半径场景数：`124`。
- 找到 Hall 缺陷数：`124`。
- 最大缺陷超额：`5`。
- 最大尾标签负载：`2`。
- 最大轮筛相位负载：`1`。
- 最大允许偏移负载：`5`。

## 最大缺陷样本

| p | q | row | kind | R | semis | primes | excess | exits | mirror span |
| ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | --- | --- |
| 1123 | 1129 | 436 | quarter_radius | 21 | 5 | 0 | 5 | Endpoint-deficit,PDEC/fixed-offset-candidate | [782417, 782519] |
| 1019 | 1021 | 483 | quarter_radius | 21 | 4 | 0 | 4 | Endpoint-deficit,PDEC/fixed-offset-candidate | [550217, 550319] |
| 127 | 131 | 46 | quarter_radius | 4 | 4 | 0 | 4 | Endpoint-deficit,PDEC/fixed-offset-candidate | [11188, 11248] |
| 109 | 113 | 39 | quarter_radius | 2 | 4 | 0 | 4 | Endpoint-deficit | [8380, 8464] |
| 61 | 67 | 21 | quarter_radius | 1 | 3 | 0 | 3 | Endpoint-deficit,Tail-anchor-candidate | [3085, 3133] |
| 31 | 37 | 11 | critical_minus_one | 1 | 3 | 0 | 3 | Endpoint-deficit,Tail-anchor-candidate | [965, 993] |
| 1721 | 1723 | 853 | quarter_radius | 33 | 3 | 0 | 3 | Endpoint-deficit,PDEC/fixed-offset-candidate | [1500665, 1500759] |
| 1123 | 1129 | 436 | half_radius | 43 | 3 | 0 | 3 | Endpoint-deficit,PDEC/fixed-offset-candidate | [782417, 782515] |
| 1019 | 1021 | 483 | half_radius | 42 | 3 | 0 | 3 | Endpoint-deficit,PDEC/fixed-offset-candidate | [550218, 550340] |
| 1069 | 1087 | 366 | quarter_radius | 22 | 3 | 0 | 3 | Endpoint-deficit,PDEC/fixed-offset-candidate | [784754, 784812] |
| 1091 | 1093 | 364 | quarter_radius | 22 | 3 | 0 | 3 | Endpoint-deficit,PDEC/fixed-offset-candidate | [797834, 797892] |
| 101 | 103 | 58 | quarter_radius | 5 | 3 | 0 | 3 | Endpoint-deficit,PDEC/fixed-offset-candidate | [4641, 4697] |
| 103 | 107 | 56 | quarter_radius | 4 | 3 | 0 | 3 | Endpoint-deficit,PDEC/fixed-offset-candidate | [5482, 5536] |
| 107 | 109 | 55 | quarter_radius | 4 | 3 | 0 | 3 | Endpoint-deficit,PDEC/fixed-offset-candidate | [5914, 5968] |
| 41 | 43 | 17 | quarter_radius | 1 | 3 | 0 | 3 | Endpoint-deficit | [1135, 1153] |
| 929 | 937 | 512 | quarter_radius | 20 | 4 | 2 | 2 | Endpoint-deficit,PDEC/fixed-offset-candidate | [398212, 398920] |
| 61 | 67 | 21 | critical_minus_one | 3 | 3 | 1 | 2 | Endpoint-deficit,Tail-anchor-candidate | [3083, 3135] |
| 61 | 67 | 21 | half_radius | 2 | 3 | 1 | 2 | Endpoint-deficit,Tail-anchor-candidate | [3084, 3134] |
| 1721 | 1723 | 853 | half_radius | 66 | 3 | 1 | 2 | Endpoint-deficit,PDEC/fixed-offset-candidate | [1500632, 1500792] |
| 1033 | 1039 | 468 | half_radius | 54 | 3 | 1 | 2 | Endpoint-deficit,PDEC/fixed-offset-candidate | [594228, 594348] |
| 1069 | 1087 | 366 | half_radius | 44 | 3 | 1 | 2 | Endpoint-deficit,PDEC/fixed-offset-candidate | [784732, 784834] |
| 1091 | 1093 | 364 | half_radius | 44 | 3 | 1 | 2 | Endpoint-deficit,PDEC/fixed-offset-candidate | [797812, 797914] |
| 1033 | 1039 | 468 | quarter_radius | 27 | 3 | 1 | 2 | Endpoint-deficit,PDEC/fixed-offset-candidate | [594255, 594321] |
| 73 | 79 | 40 | quarter_radius | 4 | 3 | 1 | 2 | Endpoint-deficit | [3088, 3118] |
| 41 | 43 | 17 | half_radius | 3 | 3 | 1 | 2 | Endpoint-deficit | [1133, 1155] |
| 17 | 19 | 5 | critical_minus_one | 1 | 2 | 0 | 2 | Endpoint-deficit,Tail-anchor-candidate | [269, 285] |
| 1861 | 1867 | 1078 | half_radius | 56 | 2 | 0 | 2 | Endpoint-deficit,PDEC/fixed-offset-candidate | [1474836, 1474976] |
| 1861 | 1867 | 1078 | quarter_radius | 28 | 2 | 0 | 2 | Endpoint-deficit,PDEC/fixed-offset-candidate | [1474864, 1474948] |
| 1697 | 1699 | 985 | half_radius | 50 | 2 | 0 | 2 | Endpoint-deficit,PDEC/fixed-offset-candidate | [1214710, 1214818] |
| 1697 | 1699 | 985 | quarter_radius | 25 | 2 | 0 | 2 | Endpoint-deficit,PDEC/fixed-offset-candidate | [1214735, 1214793] |

## 结构解释

一维 Hall 失败不是抽象坏事件：它必然给出连续半素数块 `B`，其半径邻域 `N_R(B)` 中素数数量小于 `|B|`。这已经是端点素数亏损。若同一块中尾标签或尾因子对负载过高，则它进入 Tail-anchor；若块集中在少数小轮相位或依赖少数固定偏移通道，则进入 PDEC/固定偏移 CRT 缺陷。

镜像列 `q^2-n` 在报告中作为 `q_square_mirror_span` 记录。它不把缺陷变成更小方阵零行，但把终端缺陷转成早期非零类块，供端点/PDEC 分支使用。这是当前路线中可用的镜像关系，不能误用为短周期复现。

## 下一步严格目标

把本审计中的观察升级为定理时，必须证明：任意正式反例诱导的 Hall 缺陷块，要么满足显式尾标签负载阈值，要么满足显式固定偏移/轮筛相位负载阈值，要么端点素数亏损达到 PDEC 可吸收下界。有限样本只帮助确定证书字段和阈值形状。
