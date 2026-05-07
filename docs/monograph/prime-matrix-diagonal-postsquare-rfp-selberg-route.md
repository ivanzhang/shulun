# 对角平方后端点 RFP-Upper 的二维 Selberg 路线

**状态：** `rfp_upper_reduced_to_hyperbolic_strip_selberg_constant`

本文专攻 `primepair dimension gap` 中的第二个输入：

```text
RFP-Upper: B(P) <= 1.50 P/log^2 P。
```

目标是把三条倒数地板曲线的素-素命中，改写为一个双曲窄带二维上筛常数包。

## 1. 双曲窄带母集合

令

\[
y=\max(2,\lfloor P/e\rfloor)
\]

并定义整数点窄带

\[
\mathcal R_P=
\{(a,b)\in\mathbb Z^2:\ y<a<P,\ P<b,\ P^2<ab<P^2+P\}.
\tag{RFP-1}
\]

它的原始体量为

\[
X(P)=|\mathcal R_P|
=
\sum_{a=y+1}^{P-1}
\left(
\left\lfloor {P^2+P-1\over a}\right\rfloor
-
\left\lfloor {P^2\over a}\right\rfloor
\right).
\tag{RFP-2}
\]

由于

\[
\int_y^P {P\over t}\,dt=P\log(P/y)\approx P,
\]

`X(P)` 的自然尺度是 `P`。样本中它非常贴近 `P`，例如：

```text
P=461:   X(P)=454；
P=2029:  X(P)=2017；
P=10007: X(P)=9986；
P=50021: X(P)=50015。
```

## 2. RFP 计数是二维素点筛

`B(P)` 正是 `R_P` 中两个坐标都为素数的点数：

\[
B(P)=\#\{(a,b)\in\mathcal R_P:\ a,b\in\mathbb P\}.
\tag{RFP-3}
\]

局部筛维数为 `2`：对任意小素数 `r<P`，除端点截断误差外，需同时避开

\[
a\equiv0\pmod r,\qquad b\equiv0\pmod r.
\]

因此标准二维 Selberg/Brun 上筛的目标形态是

\[
B(P)
\le
C_{\rm RFP}\,{X(P)\over(\log P)^2}
+E_{\rm edge}(P)+E_{\rm disc}(P).
\tag{RFP-4}
\]

这里：

- `C_RFP` 是二维 Selberg 主常数；
- `E_edge` 来自 `a` 接近 `y` 或 `P` 的短边；
- `E_disc` 来自双曲地板函数的模分布误差。

## 3. 与 1.50 常数的关系

低范围存在真实小波动，不能声称 `X(P)<=1.02P` 从 `P=23` 起成立。正确的尾段合同是：对
`P>=2003` 证明

\[
X(P)\le 1.02P
\tag{RFP-5}
\]

并对 `23<=P<2003` 使用有限证书。再若能证明

\[
C_{\rm RFP}{X(P)\over P}
 + {(\log P)^2\over P}(E_{\rm edge}+E_{\rm disc})
\le 1.50,
\tag{RFP-6}
\]

则得到 `RFP-Upper`。审计到 `P<=100000` 的真实最大值为

\[
\max B(P){(\log P)^2\over P}=1.4688379348569027,
\]

发生在 `P=461`。因此 `1.50` 是带少量安全余量的候选常数，不是宽松常数。

面积审计：

```text
experiments/prime_matrix_diagonal_postsquare_hyperbolic_area_audit.py
docs/diagonal_postsquare_hyperbolic_area_audit_p10000_20260505.md
```

给出：

```text
P<=10000 全审计：
max X(P)/P = 1.0530973451327434 at P=113；
P>=2003 后 max X(P)/P = 1.019810895992796 at P=2221。

高点抽样：
P=10007:  X/P=0.997901；
P=20011:  X/P=1.001549；
P=50021:  X/P=0.999880；
P=98327:  X/P=1.000905；
P=200003: X/P=1.000685。
```

所以 `RFP-Area` 的当前目标应写为：

```text
23<=P<2003: finite area/primepair certificate；
P>=2003: prove X(P)<=1.02P or route failure to HyperbolicDiscFailure。
```

低段有限证书已生成：

```text
docs/diagonal_postsquare_lowband_finite_certificate_p2003_20260505.md
```

它确认 `P<=2003` 中端点素数直接存在，且 `P>=23` 的维数差全部正余量。

进一步的面积进位分解见：

```text
experiments/prime_matrix_diagonal_postsquare_area_carry_audit.py
docs/diagonal_postsquare_area_carry_audit_p10000_20260505.md
```

对 `a in (y,P)`，`floor(P/a)` 只能为 `1` 或 `2`，所以

\[
X(P)=B_0(P)+C(P),
\qquad
B_0(P)=P+\lfloor P/2\rfloor-1-2y.
\tag{RFP-7}
\]

其中 `C(P)` 是二次剩余进位计数。`X(P)<=1.02P` 等价于

\[
C(P)\le 1.02P-B_0(P).
\tag{RFP-8}
\]

审计到 `P<=10000` 显示 `X(P)<=1.02P` 的最后失败是 `P=1873`；`P>=2003` 全部通过。
最紧尾段样本为

```text
P=2221；
base=1696；
carry=569；
allowance=569.42；
slack=0.42。
```

因此 `RFP-Area` 的真正硬点已不是面积积分，而是进位计数：

```text
AreaCarryBound:
证明 P>=2003 时 C(P)<=1.02P-B_0(P)，
或把进位过密路由到 HyperbolicDiscFailure/PDEC。
```

再进一步，相位偏差审计见：

```text
experiments/prime_matrix_diagonal_postsquare_carry_phase_discrepancy_audit.py
docs/diagonal_postsquare_carry_phase_discrepancy_audit_p10000_20260505.md
```

令 `q=floor(P/a)`、`h=P-qa`。进位条件等价于

\[
\{h^2/a\}>1-h/a.
\tag{RFP-9}
\]

所以

\[
C(P)=W(P)+D(P),
\qquad
W(P)=\sum_{y<a<P}{h\over a},
\tag{RFP-10}
\]

其中 `D(P)` 是二次分数部分偏差。审计到 `P<=10000`：

```text
max positive D/sqrt(P)=1.109666 at P=4547；
max absolute D/sqrt(P)=1.256024 at P=9343；
tail tight point P=2221:
  allowance-W=46.115249；
  D=45.695249；
  allowance-C=0.42。
```

因此面积证明可拆为：

```text
CarryMain:
证明 W(P) <= allowance(P) - A sqrt(P)；

CarryDiscrepancy:
证明 D(P) <= A sqrt(P)，或把更大正偏差路由到 HyperbolicDisc/PDEC。
```

`CarryMain` 已有初等调和恒等式：

```text
experiments/prime_matrix_diagonal_postsquare_carry_main_identity_audit.py
docs/diagonal_postsquare_carry_main_identity_audit_p100000_20260505.md
```

精确地，

\[
allowance(P)-W(P)=P\left(1.02-(H_{P-1}-H_y)\right).
\tag{RFP-11}
\]

由单调积分

\[
H_{P-1}-H_y\le \log{P-1\over y}
\le \log{P-1\over P/e-1}.
\tag{RFP-12}
\]

因此 `CarryMain` 已降为初等不等式。审计到 `P<=100000` 给出尾段余量：

```text
P>=2003:  actual min (allowance-W)/sqrt(P)=0.884250；
P>=5003:  floor-free lower bound >=1.390336；
P>=10007: floor-free lower bound >=1.983520；
P>=20011: floor-free lower bound >=2.817057。
```

所以可把面积尾段再切成：

```text
2003<=P<10007: finite carry certificate；
P>=10007: CarryMain supplies at least 1.98 sqrt(P);
           need CarryDiscrepancy D(P)<=1.98 sqrt(P),
           or route larger D(P) to HyperbolicDisc/PDEC。
```

`CarryDiscrepancy` 的专门路线见：

```text
docs/monograph/prime-matrix-diagonal-postsquare-carry-discrepancy-pdec-route.md
docs/monograph/prime-matrix-diagonal-postsquare-carry-reciprocal-frequency.md
docs/monograph/prime-matrix-diagonal-postsquare-endpoint-reciprocal-osc-hard-attack.md
```

该路线进一步利用

\[
\{P/a\}=h/a,\qquad \{P^2/a\}=\{h^2/a\}
\]

把 `D(P)>1.98sqrt(P)` 改写为端点倒数相位

\[
\sum_{y<a<P} e(rP^2/a)(1-e(rP/a))
\]

的低频集中，并路由到 `RSE-OSC` 或 `HyperbolicDisc/PDEC`。

## 4. 失败路由

`(RFP-4)` 若无法以 `1.50` 常数闭合，失败不会再是模糊的“素数太多”，而只能来自三类可命名缺陷：

```text
SelbergConstantFailure:
二维筛权常数本身不够，需要优化权或提高有限阈值。

HyperbolicDiscFailure:
双曲地板窄带在许多小模上分布异常，进入 PDEC。

TailAnchorPrimeSpike:
某些短 a 区间或 b 区间中素-素点异常集中，进入 Tail-anchor/SAE。
```

其中第二类最贴合既有端点 `PDEC`：若 `R_P` 在同一批小模残基上持续偏离二维均匀分布，则可抽取固定端点相位的非零 Fourier 缺陷。

## 5. 当前最小工程义务

下一步不应继续扩大普通数值表，而应提交三个可审稿子证书：

```text
RFP-Area:
证明 P>=2003 时 X(P)<=1.02P，低段走有限证书；若尾段失败，路由到 HyperbolicDiscFailure。

RFP-Selberg:
构造二维 Selberg 权，证明 C_RFP 主常数加边界误差 <=1.50。

RFP-Defect:
若 RFP-Selberg 超预算，则抽取具体低模相位向量，接入 PDEC/Tail-anchor。
```

一旦 `RFP-Upper` 与 `LDG-Lower` 同时完成，平方后端点按维数差合同闭合。
