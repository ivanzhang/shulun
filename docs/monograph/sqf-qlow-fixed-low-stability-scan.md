# QLOW-STAB fixed-low 稳定性扫描

**状态：** `fixed_low_stability_scan_not_a_proof`

扫描归一化频率

\[
u=t\log R,\qquad Q(iu/\log R)/\mathcal V_\omega.
\]

目标是判断 fixed-low 段是否有统一固定节省，并定位最后需要证明的频带。

## 摘要
- P=2003 R=P^0.3 R=9 Q0=0.122 maxUltra=0.126 max0.5-2=0.239 max2-6=0.698 max6+=0.691 top u=5.70 ratio=0.698
- P=2003 R=P^0.35 R=14 Q0=0.090 maxUltra=0.092 max0.5-2=0.176 max2-6=0.583 max6+=0.583 top u=6.00 ratio=0.583
- P=5003 R=P^0.3 R=12 Q0=0.101 maxUltra=0.105 max0.5-2=0.194 max2-6=0.638 max6+=0.638 top u=6.00 ratio=0.638
- P=5003 R=P^0.35 R=19 Q0=0.081 maxUltra=0.083 max0.5-2=0.151 max2-6=0.531 max6+=0.536 top u=6.70 ratio=0.536
- P=10007 R=P^0.3 R=15 Q0=0.086 maxUltra=0.088 max0.5-2=0.166 max2-6=0.582 max6+=0.582 top u=6.00 ratio=0.582
- P=10007 R=P^0.35 R=25 Q0=0.073 maxUltra=0.075 max0.5-2=0.131 max2-6=0.492 max6+=0.508 top u=10.50 ratio=0.508

## 判读

- 若最大值始终出现在 `u≈0`，则 fixed-low 段由零频极小化和连续性共同控制。
- 若 `u≈1` 附近反弹，则需要证明优化权的低频稳定，而不是只证明 `Q(0)`。
- 若 `u>=2` 后持续下降，可用欧拉局部相位离散量给出振荡节省。

## 最窄证明接口

实验把 `QLOW-STAB fixed-low` 进一步拆为：

```text
QLOW-ULTRA: 0 <= u <= 1/2，矩阵扰动/Lipschitz；
QLOW-TRANS: 1/2 < u <= 2，有限宽过渡稳定；
QLOW-OSC: u > 2，Euler 局部相位振荡。
```

其中 `QLOW-TRANS` 是新的最后最窄接口。
