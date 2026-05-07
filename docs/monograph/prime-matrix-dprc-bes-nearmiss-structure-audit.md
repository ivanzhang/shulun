# DPRC-BES 近危险结构审计

**状态：** `audit_not_a_proof`

本文接续 `DPRC-BES 对偶大筛路线`，对 `BES` 近危险样本做三出口解剖：

```text
PointLoad  -> ColumnCRT/tail-anchor；
ShortWindow -> SAE；
LowPhase -> PDEC。
```

## 1. 审计对象

脚本：

```text
experiments/prime_matrix_dprc_bes_nearmiss_structure_audit.py
```

报告：

```text
docs/dprc_bes_nearmiss_structure_audit_extended_20260506.md
docs/dprc_bes_nearmiss_structure_audit_extended_20260506.json
```

代表样本包含：

```text
最高 L1:        P=30137 minus；
最高 L2:        P=83267 plus；
高有效维数:     P=80489 minus；
高正偏差样本:   P=19997 minus, P=21149 plus；
各 beta 桶尖峰: P=72701 plus, P=93139 minus, P=99439 plus,
                P=34501 minus, P=16339 plus。
```

## 2. 结果摘要

| record | L1 | L2 | eff dim | max point load | top low phase |
|---|---:|---:|---:|---:|---|
| `30137 minus` | `2.468627` | `1.138250` | `4.703659` | `4` | `mod30 max=0.544278` |
| `83267 plus` | `2.078474` | `1.233496` | `2.839314` | `4` | `mod30 max=0.670042` |
| `19997 minus` | `2.293071` | `1.013372` | `5.120320` | `4` | `mod30 max=0.707865` |
| `21149 plus` | `2.442672` | `1.177635` | `4.302378` | `4` | `mod30 max=0.902430` |
| `80489 minus` | `1.618003` | `0.663972` | `5.938250` | `4` | `mod30 max=0.648621` |
| `72701 plus` | `1.598250` | `1.155303` | `1.913805` | `4` | `mod30 max=0.458122` |
| `93139 minus` | `1.497758` | `1.174084` | `1.627364` | `4` | `mod30 max=0.348157` |
| `99439 plus` | `1.719104` | `0.992818` | `2.998230` | `4` | `mod30 max=0.460505` |
| `34501 minus` | `1.297777` | `0.915741` | `2.008422` | `4` | `mod30 max=0.418148` |
| `16339 plus` | `1.375712` | `1.088110` | `1.598488` | `4` | `mod30 max=0.335944` |

主要观察：

```text
PointLoad:
  10 个代表样本最大单点剩余高素标签负载均为 4；
  近危险样本没有出现单列爆炸。

ShortWindow:
  最强 q 子窗峰值约 0.25 到 0.38 sqrt(S)；
  有些高 q 桶 share 很高，但绝对峰值不够形成 BES 危险交集。

LowPhase:
  最稳定信号是 mod 30 单位类内部偏斜；
  all/mod30 最大峰值从 0.335944 到 0.902430 sqrt(S)。
```

## 3. mod30 顶峰是单位类内部偏斜

审计把 `k mod 30` 转成真实整数值

\[
P^2\pm k\pmod {30}.
\]

所有代表样本的 `mod30` 顶峰都落在单位类：

| record | top `k mod 30` | top `P^2±k mod 30` | unit |
|---|---:|---:|---|
| `30137 minus` | `18` | `1` | `true` |
| `83267 plus` | `18` | `7` | `true` |
| `19997 minus` | `26` | `23` | `true` |
| `21149 plus` | `28` | `29` | `true` |
| `80489 minus` | `8` | `23` | `true` |
| `72701 plus` | `16` | `17` | `true` |
| `93139 minus` | `24` | `7` | `true` |
| `99439 plus` | `18` | `19` | `true` |
| `34501 minus` | `20` | `11` | `true` |
| `16339 plus` | `6` | `7` | `true` |

这说明近危险偏差不是“漏掉小素数筛”，而是已经通过 `2,3,5` 筛后的单位类内部方向性偏斜。

## 4. 新硬点：WheelUnitPhaseBalance

当前更准确的结构目标是：

```text
WheelUnitPhaseBalance(W):
  在 W=30/210/2310 的单位类骨架上，
  剩余高素 q 的中心化命中核不能在少数单位残基上
  同时产生高 L1 与高 L2；
  若产生，则该单位残基偏斜给出 PDEC 证书。
```

形式上，令 `U_W` 为 `W` 的单位类。对 `a in U_W` 定义

\[
E_a=\sum_{\substack{k\in S\\ P^2\pm k\equiv a\pmod W}}
\sum_{Y<q<P}\left(1_{q\mid P^2\pm k}-{1\over q}\right).
\]

若某个 `E_a` 超过阈值，则进入低模相位缺陷：

```text
max_a E_a >= lambda sqrt(S)
=> W-unit PDEC。
```

若所有 `E_a` 都低，则 `LowPhase` 被吸收，剩余只能是真正高模分散能量，由大筛控制。

## 5. 下一步

不要再把“素数规律”压成单个固定模板。这里的结构更像逐层提升：

```text
2,3,5 轮筛给出第一层单位类；
7,11,13,... 动态提升进入底座，产生更细单位类骨架；
剩余高素 q 只能在这些单位类内部产生短暂偏斜；
若偏斜跨尺度同步，就形成 PDEC/SAE/ColumnCRT 证书。
```

因此下一步最小硬点应是：

```text
DLS-LowPhase(W=30):
  证明 mod30 单位类偏斜峰不能与 BES 高能量高正和交集同步；
  或把同步峰物化为 W-unit PDEC 证书。
```

随后把 `W=30` 的证书提升到 `W=210`、`W=2310`，形成动态轮的层叠排斥。
