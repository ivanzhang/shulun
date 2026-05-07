# DPRC 新增轮层能量分散

**状态：** `audit_and_reduction_not_a_proof`

本文接续 `Fourier 频率继承分类`。上一步说明强频率常落在新增素因子层；本文进一步把整层 Fourier 能量精确拆成旧层继承与新增层能量，并检查新增层能量是否与 `BES` 危险门槛同步。

## 1. 精确能量拆分

设

```text
W = r W0
```

其中 `r` 是本层新增素因子，例如 `30 -> 210` 的 `r=7`，`210 -> 2310` 的 `r=11`。令 `F_W(a)` 是 `U_W` 上的中心化单位类偏差，并在非单位类上取 `0`。

加性 Fourier 频率满足：

```text
r | h     => 继承自 W0 的旧层频率；
r ∤ h     => 新增素因子层频率。
```

由 Parseval 和按 `mod W0` 折叠可得精确恒等式：

\[
\sum_{r\mid h}|\widehat F_W(h)|^2
=
W_0\sum_{b\bmod W_0}
\left|\sum_{\substack{a\in U_W\\ a\equiv b\bmod W_0}}F_W(a)\right|^2.
\tag{NLE-1}
\]

因此新增层能量为

\[
E_{\rm new}(W)
=
W\sum_{a\in U_W}|F_W(a)|^2
-
W_0\sum_{b\bmod W_0}
\left|\sum_{\substack{a\in U_W\\ a\equiv b\bmod W_0}}F_W(a)\right|^2.
\tag{NLE-2}
\]

这个拆分是恒等式，不是统计模型。

## 2. 全扫结果

新增脚本：

```text
experiments/prime_matrix_dprc_newlayer_energy_scan.py
```

生成：

```text
docs/dprc_newlayer_energy_scan_p100000_20260506.md
docs/dprc_newlayer_energy_scan_p100000_20260506.json
```

全扫参数：

```text
P <= 100000
alpha = 0.43
W = 30,210,2310
P >= 10007 records = 16726
```

核心结果：

| 层 | 新增因子 | 新增能量占比 min/avg/max | centered peak 最大值 | 高 L1 段 peak 最大值 | 高 L2 段 peak 最大值 |
|---:|---:|---:|---:|---:|---:|
| `30 -> 210` | `7` | `0.580510 / 0.897118 / 0.997260` | `0.611625` | `0.280206` | `0.271803` |
| `210 -> 2310` | `11` | `0.854837 / 0.926300 / 0.973218` | `0.292146` | `0.170133` | `0.114485` |

同时：

```text
danger_l1_l2_6_5_count = 0
danger_l1_l2_cauchy_count = 0
```

## 3. 关键读法

这组数据排除的是一个错误直觉：不能说“升层后新增素因子层不重要”。事实上，`2310` 层的 Fourier 能量平均有 `0.926300` 在新增因子 `11` 的频率上。

真正有用的结构是：

```text
新增层能量很大；
但它不是集中成单个可覆盖整行的同步峰；
在高 BES L1/L2 门槛附近，单相位 centered peak 明显下降。
```

最紧样本显示：

| 类型 | P/side | BES L1 | BES L2 | W=2310 centered peak | centered L2 | 新增层占比 |
|---|---|---:|---:|---:|---:|---:|
| 高 L1 | `30137 minus` | `2.468627` | `1.138250` | `0.170133` | `0.888733` | `0.923732` |
| 高 L1 | `21149 plus` | `2.442672` | `1.177635` | `0.138382` | `0.935898` | `0.923053` |
| 高 L2 | `83267 plus` | `2.078474` | `1.233496` | `0.114485` | `0.851710` | `0.924057` |

换言之，新增层能量很强，但在高 `BES` 压力处高度分散。粗略相位有效维数

\[
D_{\rm phase}\approx
\left({\|F_W\|_2\over \|F_W\|_\infty}\right)^2
\]

分别约为 `27.3`、`45.8`、`55.3`，不像一个低维同步峰。

## 4. 新硬点

当前最小硬点应从“新增层是否存在”改成“新增层是否可同步”：

```text
NewLayer Dispersion Clamp:
  若 E_new(W) 高且 concentrated peak 高，
  则产生 new-layer W-unit PDEC；

  若 E_new(W) 高但 phase dimension 高，
  则新增层只是高维相位振荡，
  不能与 BES 高 L1、高 L2 同时支付全覆盖压力；

  若所有提升层都如此分散，
  则零行只能依赖高模分散能量，
  进入对偶大筛吸收。
```

该项仍不是最终证明。它把下一步可审稿目标压成一个明确不等式：证明 `BES` 危险交集若存在，则某层新增 Fourier 能量必须低维集中；反过来，若各新增层满足相位维数下界，则 `D_+<=3sqrt(S)`。

