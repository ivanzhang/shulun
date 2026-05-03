# KSCWM / CRD-SPC 双出口压力扫描

**状态：** `experimental_obstruction_split_not_a_proof`

本实验把当前两个硬点拆成两个可审查问题：

1. `KSCWM` 是否主要来自平滑 dyadic 核上的 Selberg 符号相消；
2. `SPC` 是否能在辅助模上产生可检测的有向能量缺陷。

## 摘要
- P=2003 M=P^1.2 R=P^0.3 terms=27 actual/env=0.438 smooth/env=0.348 roughDiff/env=0.108 topPrime=2 share=0.340 bestAux=29 energy=0.004 maxAbs/unif=1.06 zeroShare=0.000
- P=2003 M=P^1.2 R=P^0.35 terms=108 actual/env=0.223 smooth/env=0.180 roughDiff/env=0.051 topPrime=2 share=0.285 bestAux=29 energy=0.002 maxAbs/unif=1.06 zeroShare=0.000
- P=2003 M=P^1.4 R=P^0.3 terms=58 actual/env=0.025 smooth/env=0.014 roughDiff/env=0.011 topPrime=2 share=0.363 bestAux=29 energy=0.001 maxAbs/unif=1.10 zeroShare=0.000
- P=2003 M=P^1.4 R=P^0.35 terms=154 actual/env=0.090 smooth/env=0.082 roughDiff/env=0.009 topPrime=2 share=0.320 bestAux=23 energy=0.001 maxAbs/unif=1.12 zeroShare=0.000
- P=5003 M=P^1.2 R=P^0.3 terms=51 actual/env=0.179 smooth/env=0.077 roughDiff/env=0.200 topPrime=5 share=0.283 bestAux=23 energy=0.001 maxAbs/unif=1.11 zeroShare=0.000
- P=5003 M=P^1.2 R=P^0.35 terms=181 actual/env=0.064 smooth/env=0.014 roughDiff/env=0.076 topPrime=2 share=0.241 bestAux=31 energy=0.000 maxAbs/unif=1.14 zeroShare=0.000
- P=5003 M=P^1.4 R=P^0.3 terms=100 actual/env=0.104 smooth/env=0.088 roughDiff/env=0.016 topPrime=2 share=0.372 bestAux=31 energy=0.001 maxAbs/unif=1.22 zeroShare=0.000
- P=5003 M=P^1.4 R=P^0.35 terms=250 actual/env=0.082 smooth/env=0.076 roughDiff/env=0.007 topPrime=2 share=0.318 bestAux=31 energy=0.001 maxAbs/unif=1.22 zeroShare=0.000

## 判读

- `smooth/env` 小且 `roughDiff/env` 小：`KSCWM` 可先化为平滑 Selberg 变换相消。
- `smooth/env` 小但 `roughDiff/env` 不小：需加入粗数分布误差，即 Buchstab/CRT 均衡输入。
- `topPrime share` 大但辅助能量不大：仅有 lcm 支撑集中还不足以推出 `CRD-SPC`，必须增加“有向相位集中”条件。
- 辅助能量大：可把 `SPC` 转化为辅助模 CRTDefect 或短差值能量超标。

## 当前严谨修正

`SPC` 不能单独作为 `CRD-SPC` 的充分条件；它必须升级为 oriented-SPC：临界质量不仅集中在 `q|ell`，还要在某个辅助模或短差值方向上保持同向相位。否则小素支撑集中可能只是 Selberg 权结构，而不一定给出真实 CRT 缺陷。
