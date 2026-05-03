# QLOW-MID 带权吸收扫描

**状态：** `weighted_mid_absorption_scan_not_a_proof`

本实验直接扫描

\[
\int_{u>2}|\widehat\Phi(iu/\log R)|\,|H(iu/\log R)|\,|Q(iu/\log R)|\,\frac{du}{\log R}.
\]

并按 `u` 段分解预算，检查裸 `Q` 反弹是否被 `Phihat/H` 带权吸收。

## 摘要
- P=2003 R=P^0.3 R=9 totalRatio=0.148 midRatio=0.151 midShare=0.699 topU=0.00 topBand=ultra_0_0p5 pointRatio=0.122
- P=2003 R=P^0.35 R=14 totalRatio=0.131 midRatio=0.141 midShare=0.762 topU=0.00 topBand=ultra_0_0p5 pointRatio=0.090
- P=5003 R=P^0.3 R=12 totalRatio=0.136 midRatio=0.145 midShare=0.730 topU=0.00 topBand=ultra_0_0p5 pointRatio=0.101
- P=5003 R=P^0.35 R=19 totalRatio=0.126 midRatio=0.139 midShare=0.783 topU=2.80 topBand=mid_2_6 pointRatio=0.197
- P=10007 R=P^0.3 R=15 totalRatio=0.128 midRatio=0.140 midShare=0.757 topU=0.00 topBand=ultra_0_0p5 pointRatio=0.086
- P=10007 R=P^0.35 R=25 totalRatio=0.120 midRatio=0.135 midShare=0.800 topU=3.20 topBand=mid_2_6 pointRatio=0.205

## 分段预算

### P=2003 R=P^0.3
- ultra_0_0p5: ratio=0.122 shareBudget=0.094 maxQ=0.124 maxH=1.000
- trans_0p5_2: ratio=0.152 shareBudget=0.207 maxQ=0.239 maxH=0.984
- mid_2_6: ratio=0.257 shareBudget=0.327 maxQ=0.698 maxH=0.802
- mid_6_12: ratio=0.170 shareBudget=0.138 maxQ=0.687 maxH=0.364
- tail_12_30: ratio=0.083 shareBudget=0.093 maxQ=0.879 maxH=0.329
- tail_30_plus: ratio=0.100 shareBudget=0.142 maxQ=0.936 maxH=0.648

### P=2003 R=P^0.35
- ultra_0_0p5: ratio=0.090 shareBudget=0.070 maxQ=0.091 maxH=1.000
- trans_0p5_2: ratio=0.114 shareBudget=0.169 maxQ=0.176 maxH=0.989
- mid_2_6: ratio=0.236 shareBudget=0.360 maxQ=0.583 maxH=0.859
- mid_6_12: ratio=0.178 shareBudget=0.172 maxQ=0.582 maxH=0.370
- tail_12_30: ratio=0.069 shareBudget=0.091 maxQ=0.515 maxH=0.329
- tail_30_plus: ratio=0.087 shareBudget=0.139 maxQ=0.884 maxH=0.573

### P=5003 R=P^0.3
- ultra_0_0p5: ratio=0.102 shareBudget=0.082 maxQ=0.103 maxH=1.000
- trans_0p5_2: ratio=0.127 shareBudget=0.188 maxQ=0.194 maxH=0.987
- mid_2_6: ratio=0.242 shareBudget=0.342 maxQ=0.638 maxH=0.842
- mid_6_12: ratio=0.179 shareBudget=0.160 maxQ=0.637 maxH=0.364
- tail_12_30: ratio=0.072 shareBudget=0.087 maxQ=0.513 maxH=0.329
- tail_30_plus: ratio=0.093 shareBudget=0.142 maxQ=0.922 maxH=0.573

### P=5003 R=P^0.35
- ultra_0_0p5: ratio=0.081 shareBudget=0.063 maxQ=0.082 maxH=1.000
- trans_0p5_2: ratio=0.101 shareBudget=0.154 maxQ=0.151 maxH=0.991
- mid_2_6: ratio=0.223 shareBudget=0.362 maxQ=0.531 maxH=0.885
- mid_6_12: ratio=0.188 shareBudget=0.189 maxQ=0.536 maxH=0.411
- tail_12_30: ratio=0.074 shareBudget=0.101 maxQ=0.487 maxH=0.329
- tail_30_plus: ratio=0.079 shareBudget=0.130 maxQ=0.876 maxH=0.562

### P=10007 R=P^0.3
- ultra_0_0p5: ratio=0.086 shareBudget=0.072 maxQ=0.087 maxH=1.000
- trans_0p5_2: ratio=0.108 shareBudget=0.170 maxQ=0.166 maxH=0.989
- mid_2_6: ratio=0.232 shareBudget=0.356 maxQ=0.582 maxH=0.866
- mid_6_12: ratio=0.181 shareBudget=0.173 maxQ=0.581 maxH=0.377
- tail_12_30: ratio=0.070 shareBudget=0.091 maxQ=0.509 maxH=0.329
- tail_30_plus: ratio=0.085 shareBudget=0.137 maxQ=0.883 maxH=0.573

### P=10007 R=P^0.35
- ultra_0_0p5: ratio=0.073 shareBudget=0.058 maxQ=0.074 maxH=1.000
- trans_0p5_2: ratio=0.090 shareBudget=0.142 maxQ=0.131 maxH=0.993
- mid_2_6: ratio=0.212 shareBudget=0.367 maxQ=0.492 maxH=0.903
- mid_6_12: ratio=0.187 shareBudget=0.197 maxQ=0.508 maxH=0.458
- tail_12_30: ratio=0.077 shareBudget=0.111 maxQ=0.488 maxH=0.325
- tail_30_plus: ratio=0.073 shareBudget=0.124 maxQ=0.845 maxH=0.454

## 判读

- 若 `midShare` 小，说明中频峰虽高但总预算很小，可由 `Phihat` 衰减吸收。
- 若 `midRatio` 小，说明 `Q/H` 在中频整体仍有固定节省。
- 若主预算集中于 `u<=2`，则 `QLOW-MID` 已不是主障碍，应回到 `QLOW-TRANS` 的有限宽证明。

## 证明接口

实验支持把 `QLOW-MID` 写成带权积分命题，而不是裸 `Q` 命题：

```text
QLOW-MID-W: 中频峰的带权总预算小；
QLOW-MID-PHI: u>U0 的尾部由 Phihat 衰减吸收；
QLOW-MID-COMP: 2<u<=U0 的有限中频由显式常数积分界吸收。
```
