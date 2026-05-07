# DPRC层叠轮 Fourier 能量路线

**状态：** `proof_route_not_a_proof`

本文接续 `圆柱斜线与层叠轮筛的夹击矛盾场`，把

```text
W=30 -> 210 -> 2310 -> ...
```

的单位类偏斜，改写成 Fourier/PDEC 证书路线。

## 1. 单位类偏差向量

固定动态提升轮 `Y=P^0.43` 与小模连乘轮 `W`。令

\[
U_W=(\mathbb Z/W\mathbb Z)^\times,\qquad N_W=|U_W|=\varphi(W).
\]

对 `a in U_W` 定义单位类中心化补洞偏差

\[
E_W(a)=
\sum_{\substack{k\in S_Y^\pm(P)\\ P^2\pm k\equiv a\pmod W}}
\sum_{Y<q<P}
\left(1_{q\mid P^2\pm k}-{1\over q}\right).
\tag{LFE-1}
\]

`E_W(a)` 表示剩余高素斜线在第 `W` 层轮单位类 `a` 上的净正负偏斜。

## 2. Fourier 显化

写平均项

\[
\bar E_W={1\over N_W}\sum_{a\in U_W}E_W(a),
\qquad
F_W(a)=E_W(a)-\bar E_W.
\]

若某个单位类峰值很高，

\[
E_W(a_0)\ge \lambda\sqrt{|S|},
\tag{LFE-2}
\]

则有二分：

```text
Mean-dominated:
  平均项本身很大，说明全体单位类都有正偏差，回到 BES L1/容量压力；

Centered-spike:
  F_W(a0) 仍很大，由 Parseval 强制存在非平凡 Fourier 模式偏大。
```

具体地，若

\[
F_W(a_0)\ge \eta\sqrt{|S|},
\]

则

\[
\|F_W\|_2\ge \eta\sqrt{|S|}.
\]

把 `F_W` 延拓为 `Z/WZ` 上非单位处为零的函数后，在加性 Fourier 频率下由 Parseval 得到某个非零 `h mod W` 满足

\[
\left|\sum_{a\in U_W}F_W(a)e^{2\pi iha/W}\right|
\ge \eta\sqrt{|S|}.
\tag{LFE-3}
\]

这正是 `W-unit PDEC` 证书：剩余高素斜线补洞在一个低模加性 Fourier 方向上有持续偏斜。

## 3. 与层叠轮扫描的关系

全扫 `P<=100000`，`P>=10007` 的读数：

| W | phi(W) | max unit peak | high L1 max peak | max peak * sqrt(phi) |
|---:|---:|---:|---:|---:|
| `30` | `8` | `1.076781` | `0.902430` | `3.045597` |
| `210` | `48` | `0.617936` | `0.331095` | `4.281183` |
| `2310` | `480` | `0.293727` | `0.175276` | `6.435243` |

读法：

```text
单单位类峰值随 W 提升下降；
但 max peak * sqrt(phi(W)) 不下降，
说明不能用朴素“随机均匀到 phi(W) 个类”一刀切证明；
必须利用 Fourier/PDEC 二分：
  未稀释的峰不是随机误差，而是可证书化的低模相干。
```

这正符合层叠轮筛的本质：每一层都揭示一批真实偏斜，但若这些偏斜想支撑零行，就必须跨层同步；跨层同步会变成低模 Fourier 证书。

## 4. 夹击证明接口

当前 `LayeredClamp` 可以细化为：

```text
Zero row
=> DPRC capacity pressure
=> BES danger intersection
=> Layered wheel unit spike or dispersed high-mod energy
```

对单位 spike 分支：

```text
存在 W in {30,210,2310,...} 与 a in U_W:
  E_W(a) >= lambda_W sqrt(S)

=> Mean-dominated or Centered-spike
=> BES pressure or W-unit PDEC。
```

对非 spike 分支：

```text
所有有限 W 的单位峰都低；
=> 低模投影不能解释 BES 危险交集；
=> 剩余偏差必须在高模上分散；
=> 大筛/分散估计给 D_+<=3sqrt(S)。
```

## 5. 下一步硬点

现在最小硬点不是“找一个固定轮规律”，而是证明一个层叠二分：

```text
Layered Fourier Clamp:
  对某个有限 W<=W*(P)，若单位类峰未稀释，
  则存在 W-unit Fourier/PDEC 证书；
  若所有 W<=W*(P) 都已稀释，
  则 BES 危险交集无法由低模相位支撑，
  只能由高模分散能量承担，并被大筛吸收。
```

这里 `W*(P)` 不必固定为常数；它可以随 `P` 缓慢增长，但始终低于动态提升轮 `Y=P^0.43`。这给出了极限意义上的描述：

```text
素数的同余规律不是单层静态规律；
它是 W=30,210,2310,... 逐层展开的禁止类结构；
每层真实但不终局；
零行若想存在，必须让这些层级偏斜同步；
同步一旦足够强，就成为 PDEC/SAE/ColumnCRT 证书。
```

这就是层叠轮筛与圆柱斜线容量夹击的当前主攻方向。

## 6. Fourier 继承分类更新

新增 `docs/monograph/prime-matrix-dprc-fourier-inheritance-classifier.md` 与脚本
`experiments/prime_matrix_dprc_fourier_inheritance_classifier.py` 后，强频率进一步分成两类：

```text
inherited:
  top period 已整除上一层轮，只是旧相位提升；

new-layer:
  top period 不整除上一层轮，必须使用新增素因子层，
  因而是新层 PDEC 候选方向。
```

对 `docs/dprc_layered_wheel_fourier_audit_20260506.json` 的 `8` 条代表样本：

| W | inherited/new-layer | 新增因子 | max Fourier/sqrt | max centered peak/sqrt |
|---:|---|---|---:|---:|
| `30` | `base: 8` | - | `1.833925` | `1.021564` |
| `210` | `inherited: 2, new-layer: 6` | `7` | `2.168333` | `0.611625` |
| `2310` | `new-layer: 8` | `11` | `2.252895` | `0.292146` |

读法是：升到 `2310` 后单单位类峰已经明显稀释，但最强 Fourier 频率全部进入新增因子 `11`
方向。这支持更精确的夹击二分：

```text
新增层频率持续同步 => new-layer W-unit PDEC；
新增层频率不持续同步 => 低模相位不能支付 BES 危险交集，只能走高模分散大筛。
```
