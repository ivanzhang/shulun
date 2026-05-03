# PTA-GSL 硬攻：Selberg 展开后的最小障碍

## 0. 目标

当前方阵行列路线的最小硬点是：

```text
PTA-GSL: GSL 删除 p 变量小素合数层后，p 候选在粗锚 m 平均上具有 1/log P 密度上界。
```

本文件直接展开这个命题，检查它是否能由现有圆柱斜线锁、`Y`-rough 互补商、大因子短窗不可复用和 CRT 均衡无条件推出。

结论先行：

```text
GSL 完全组织了 p 的小素合数层；
但要获得 1/log P，需要一个双线性短区间筛余分布估计；
该估计是当前新的最小硬点，记为 BSI。
```

## 1. PTA-GSL 的对象

在尾段中，

\[
P/Y<p\le P,\qquad Y=P^\alpha,\quad e^{-1}<\alpha<1/2.
\]

对 dyadic `m~M`，定义

\[
T(M)=
\sum_{\substack{m\sim M\\P^-(m)>Y}}
\#\left\{
p\in\mathbb P:
\frac Xm\le p<\frac{X+H}{m}
\right\}.
\]

其中 `H≈P`。目标是证明

\[
T(M)
\le
(1+\varepsilon)
\frac{H}{\log P}
\sum_{\substack{m\sim M\\P^-(m)>Y}}\frac1m
+
E_M.
\tag{PTA-GSL}
\]

## 2. GSL 对 `p` 变量的精确意义

若 `p<=P` 是合数，则存在素数

\[
q\le\sqrt P,\qquad q|p.
\]

扩展斜线锁 `P±t` 能把每个 `q<=sqrt(P)` 的合数相位层写成圆柱螺旋相位块。因此，从结构上：

```text
p 是素数
<=>
p 没有任何 q<=sqrt(P) 的 GSL 小素相位锁。
```

这一步是严格的，但它只是把素数条件几何化为“避开所有小素锁”。要得到 `1/log P` 密度，还必须证明这些锁在粗锚平均中具有正确覆盖效率。

## 3. Selberg 上界筛展开

用 Selberg 上界筛替代素数条件。令 `z=sqrt(P)`，取筛权 `lambda_d` 支持在 `d|P(z)`、`d<=R`。形式上有

\[
1_{\mathbb P}(p)
\le
\left(\sum_{\substack{d|p\\d\le R}}\lambda_d\right)^2
\]

对 `p<=P` 的上界筛意义成立。

代入 `T(M)`：

\[
T(M)\le
\sum_{d_1,d_2\le R}\lambda_{d_1}\lambda_{d_2}
\sum_{\substack{m\sim M\\P^-(m)>Y}}
\#\left\{
p:
[d_1,d_2]|p,\quad
pm\in I
\right\}.
\]

设

\[
\ell=[d_1,d_2].
\]

写 `p=ell a`，则内层为

\[
N_\ell(M)
=
\sum_{\substack{m\sim M\\P^-(m)>Y}}
\#\left\{
a:\ X\le \ell a m<X+H
\right\}.
\]

也就是

\[
N_\ell(M)
=
\sum_{\substack{m\sim M\\P^-(m)>Y}}
\left(
\left\lfloor\frac{X+H}{\ell m}\right\rfloor
-
\left\lfloor\frac{X}{\ell m}\right\rfloor
\right).
\tag{1}
\]

## 4. 主项与余项

主项为

\[
N_\ell^{main}(M)
=
\frac H\ell
\sum_{\substack{m\sim M\\P^-(m)>Y}}\frac1m.
\]

如果对所有 Selberg 相关的 `ell` 都有

\[
N_\ell(M)
=
N_\ell^{main}(M)+
O(E_\ell(M)),
\tag{2}
\]

且

\[
\sum_{d_1,d_2\le R}
|\lambda_{d_1}\lambda_{d_2}|E_{[d_1,d_2]}(M)
\ll
o(|G_Y(I)|),
\tag{3}
\]

则 Selberg 筛给出 `1/log P` 主项，`PTA-GSL` 成立。

因此真正的数学核心不是再描述斜线，而是证明 `(1)` 的短区间双线性余项满足 `(2)(3)`。

## 5. 为什么平凡余项不够

对每个 `m`，地板函数余项是 `O(1)`。平凡求和给

\[
N_\ell(M)
=
\frac H\ell\sum_{m\sim M,P^-(m)>Y}\frac1m
+
O(\#\{m\sim M:P^-(m)>Y\}).
\]

这个余项代入 Selberg 展开后太大。它正是上一轮发现的缺失：

```text
纯几何只给 O(1) 命中；
目标需要 1/log P 密度节省。
```

换句话说，必须利用 `m` 的平均，而不能逐点估计。

## 6. 新的最小硬点：BSI

把所需估计命名为：

**BSI（Bilinear Short-Interval rough divisor estimate）。** 对 `M` 位于尾段 dyadic 范围、`ell` 位于 Selberg 筛所需范围，成立

\[
\sum_{\substack{m\sim M\\P^-(m)>Y}}
\left(
\left\lfloor\frac{X+H}{\ell m}\right\rfloor
-
\left\lfloor\frac{X}{\ell m}\right\rfloor
-
\frac{H}{\ell m}
\right)
\]

在 Selberg 二次权平均后为

\[
o(|G_Y(I)|).
\tag{BSI}
\]

若 `BSI` 成立，则：

\[
BSI+GSL\Rightarrow PTA\text{-}GSL
\Rightarrow PM\text{-}R2B
\Rightarrow RHI.
\]

## 7. BSI 可用刚性

### 7.1 圆柱相位块

地板差值异常表示双曲线条带

\[
X\le \ell am<X+H
\]

在粗锚 `m` 上取整异常集中。映射回方阵，异常集中对应一簇圆柱螺旋相位块同向穿过短窗口。

若这种集中持续出现，应产生：

- 小素锁避让异常；
- 同一相位块过度穿越；
- CRT 完整周期中非零类局部偏差。

这给 BSI 的自足证明提供了几何入口。

### 7.2 `Y`-rough 互补商

`m` 不是任意变量，而是 `P^-(m)>Y`。这会减少短周期共振：若某个小模 `q<=Y` 造成相位聚集，则 `m` 不能落在 `0 mod q`，并且所有非零类应由 CRT 均衡约束。

### 7.3 大因子短窗不可复用

若多个 `ell a m` 落在同一短窗口中并共享结构因子，则差值

\[
|\ell a_1m_1-\ell a_2m_2|<H
\]

产生强整除限制。该限制可用于排除高重数簇，但仍需转化成平均余项节省。

## 8. 外部解析版本

若允许外部解析输入，BSI 可写成加权短区间 divisor switching 定理：

```text
粗数权 1_{P^-(m)>Y} 对双曲线条带 X<=ell a m<X+H
在 ell 的 Selberg 二次平均中具有模型主项和可吸收误差。
```

这类似 Type-I/dispersion 估计，而不是单纯 PNT。它的优势是平均变量为 `m` 和 `ell`，不要求每个单独短区间 `[X/m,(X+H)/m]` 都有素数定理。

## 9. 自足版本的当前障碍

若不引用外部解析定理，仅靠目前文内刚性还不能推出 BSI。原因：

1. GSL 只说明小素锁的几何位置；
2. 大因子不可复用只给局部重数限制；
3. CRT 均衡在完整周期内成立，但 BSI 是短区间双曲线条带问题；
4. 需要把短区间条带异常转成完整周期均衡缺陷或相位块过度复用。

这最后一步尚未证明，是当前真正硬点。

## 10. 本轮硬攻结论

当前链条已进一步压缩为：

```text
GSL
=> Selberg 展开
=> BSI
=> PTA-GSL
=> PM-R2B
=> RHI
```

其中 `BSI` 是新的最小不可跳过接口。它比 `PTA-GSL` 更具体：

- 变量明确：`m, ell, a`；
- 误差明确：地板函数短区间余项；
- 平均明确：Selberg 二次权平均；
- 可用刚性明确：圆柱相位块、`Y`-rough 互补商、短窗不可复用、CRT 均衡。

下一步若继续硬攻，应直接专攻 BSI：证明短区间双曲线条带异常必然触发一个已知刚性出口。

## 11. BSI 的 sawtooth 展开

令

\[
\psi(x)=x-\lfloor x\rfloor-\frac12.
\]

则

\[
\left\lfloor\frac{X+H}{\ell m}\right\rfloor
-
\left\lfloor\frac X{\ell m}\right\rfloor
-
\frac{H}{\ell m}
=
\psi\left(\frac X{\ell m}\right)
-
\psi\left(\frac{X+H}{\ell m}\right)
+
O(1_{\ell m|X}+1_{\ell m|X+H}).
\]

端点项在 dyadic 平均中可单独放入 divisor-bound 误差；真正硬点是 sawtooth 差。

用 Vaaler 截断，对任意 `K>=1`，

\[
\psi(x)=
\sum_{1\le |h|\le K}c_h e(hx)
+
O\left(\min\left(1,\frac1{K\|x\|}\right)\right),
\qquad c_h\ll\frac1{|h|}.
\]

于是 BSI 归结为控制

\[
S_{h,\ell}(M)
=
\sum_{\substack{m\sim M\\P^-(m)>Y}}
e\left(\frac{hX}{\ell m}\right)
\left(
1-e\left(\frac{hH}{\ell m}\right)
\right).
\tag{RSE}
\]

这就是当前真正的相位对象：粗数倒数指数和。

## 12. 关键相位尺度

在尾段中，`X/m` 是对应的 `p` 尺度，记

\[
P_m:=X/M.
\]

则

\[
P/Y\lesssim P_m\lesssim P.
\]

相位

\[
f(m)=\frac{hX}{\ell m}
\]

满足

\[
|f'(m)|\asymp \frac{hX}{\ell M^2}
\asymp \frac{hP_m}{\ell M},
\]

而整个 dyadic 块上的相位总变化约为

\[
M|f'(m)|\asymp \frac{hP_m}{\ell}.
\]

因此若

\[
\ell\ll hP_m,
\]

倒数相位存在可用振荡；若

\[
\ell\gg hP_m,
\]

该相位在 dyadic 块上几乎不振荡，必须依赖筛权平均或其他结构。

## 13. 筛水平与相位抵消的张力

Selberg 上界筛要获得接近 `1/log P` 的主项，需要足够高的筛水平。若筛权支持 `d<=R`，则

\[
\ell=[d_1,d_2]\le R^2.
\]

另一方面，尾段最小 `p` 尺度为

\[
P_m\ge P/Y=P^{1-\alpha}.
\]

若希望对所有相关 `ell` 都有基本相位振荡，需要

\[
R^2\lesssim P^{1-\alpha},
\qquad
R\lesssim P^{(1-\alpha)/2}.
\tag{LC}
\]

但 `R` 越小，Selberg 上界筛主常数越差；`R` 越大，RSE 的倒数相位越不振荡。这就是当前硬点的核心张力：

```text
高筛水平给 1/log P；
低筛水平给倒数相位抵消；
二者必须兼容。
```

## 14. 可控区间与临界区间

把 Selberg 平均按 `ell` 分成两段。

### 14.1 振荡区间

\[
\ell\le P_m/(\log P)^A.
\]

此时 `f(m)` 在 dyadic 块中有足够总变化。对无粗数权的和，可用 van der Corput/Kusmin--Landau 得到非平凡抵消；带 `Y`-rough 权后，可用 Buchstab 分解把粗数权拆成短 Dirichlet 多项式，再对每段应用倒数相位估计。

该段是最有希望完全自足证明的部分。

### 14.2 临界/非振荡区间

\[
\ell> P_m/(\log P)^A.
\]

此时倒数相位变化不足，不能指望单个 `ell` 上抵消。必须使用：

- Selberg 权重中 `ell` 的平均；
- well-factorable 分解；
- 圆柱相位块异常排斥；
- 或外部 dispersion 型输入。

这正是 BSI 的最小剩余硬核。

## 15. 新的更细接口：RSE

将 BSI 进一步压缩为：

**RSE（Rough reciprocal-sum estimate）。** 对所有 dyadic `M`、Selberg 相关 `ell` 和 Vaaler 频率 `h`，有

\[
\sum_{\ell}
\omega_\ell
\sum_{1\le |h|\le K}\frac1{|h|}
|S_{h,\ell}(M)|
\le
o(|G_Y(I)|)
\]

其中 `omega_ell` 是由 `lambda_{d_1}lambda_{d_2}` 合成的 Selberg 二次权。

若 `RSE` 成立，则

\[
RSE\Rightarrow BSI\Rightarrow PTA\text{-}GSL.
\]

## 16. 当前硬攻结论

`BSI` 已进一步转化为可分析的倒数相位问题：

```text
RSE: 粗数权倒数指数和在 Selberg 二次权平均中可吸收。
```

新增洞察是筛水平张力 `(LC)`：

\[
R\lesssim P^{(1-\alpha)/2}
\]

有利于相位抵消，但可能削弱 Selberg 主常数；提高 `R` 又会进入非振荡区间。下一步真正要攻的是这个兼容性：

1. 在振荡区间内用 van der Corput + Buchstab 分解证明 RSE；
2. 在临界区间内用 Selberg 权平均或外部 dispersion 证明 RSE；
3. 若二者都能闭合，则 `PTA-GSL` 才能升级。

## 17. RSE 数值压力测试

新增脚本：

```text
experiments/rse_reciprocal_sum_scan.py
```

对应输出：

```text
docs/monograph/rse-reciprocal-sum-scan.md
docs/monograph/rse-reciprocal-sum-scan.json
```

扫描对象正是 `(RSE)`：

\[
S_{h,\ell}(M)
=
\sum_{\substack{m\sim M\\P^-(m)>Y}}
e\left(\frac{hX}{\ell m}\right)
\left(1-e\left(\frac{hH}{\ell m}\right)\right).
\]

实验参数覆盖 `P=1009,2003,5003`、`Y=P^{0.45}`、`M=P^u`
其中 `u=1,1.15,1.3,1.45`，并按

\[
\Theta=\frac{hP_m}{\ell}
\]

分成三段：

```text
oscillatory: Theta >= 10
critical:    1 <= Theta < 10
flat:        Theta < 1
```

结果稳定显示：

- 振荡区 `|S|/sum|amp|` 通常很小，符合倒数相位抵消预期；
- 平坦区 `|S|/sum|amp|` 接近 1，但 `|S|/N` 已因振幅因子很小而随 `P` 下降；
- 临界区既没有充分振荡，也没有充分振幅衰减，是当前真实硬核；
- 地板余项 `E/N` 在样本中很小，但这只能定位瓶颈，不能替代证明。

因此 `RSE` 不应再作为单块硬点处理，而应拆为三段。

## 18. 三段化后的最小证明接口

取 `L=(\log P)^A`。把 `(RSE)` 写成：

### 18.1 RSE-OSC

\[
\frac{hP_m}{\ell}\ge L.
\]

目标是证明粗数权倒数相位有非平凡抵消：

\[
\sum_{\substack{m\sim M\\P^-(m)>Y}}
e\left(\frac{hX}{\ell m}\right)b_m
\ll
o(1)\sum_{\substack{m\sim M\\P^-(m)>Y}}|b_m|
\]

其中 `b_m=1-e(hH/ell m)` 或 Buchstab 分解后的短 Dirichlet 系数。
这是最可攻部分：可用 van der Corput/Kusmin--Landau 加 Buchstab 拆分。

### 18.2 RSE-AMP

\[
\frac{hP_m}{\ell}\le L^{-1}.
\]

此时不要求相位抵消，而用

\[
\left|1-e\left(\frac{hH}{\ell m}\right)\right|
\ll
\frac{hH}{\ell M}.
\]

Vaaler 权重中的 `1/h` 与上式的 `h` 抵消，因此该段应归入振幅账本：

\[
\sum_{\ell\ \text{flat}}\omega_\ell
\sum_h \frac1h |S_{h,\ell}(M)|
\ll
H
\sum_{\ell\ \text{flat}}\frac{|\omega_\ell|}{\ell}
\sum_{\substack{m\sim M\\P^-(m)>Y}}\frac1m.
\]

若 Selberg 合成权在平坦段满足可吸收的调和尾界，则 `RSE-AMP` 闭合。

### 18.3 RSE-CRIT

\[
L^{-1}<\frac{hP_m}{\ell}<L.
\]

这是唯一真正剩余硬点。该带宽在对数尺度上很薄，但不能靠单点估计处理。
可行路线是证明 Selberg 合成权在临界曲线

\[
\ell\asymp hP_m
\]

附近没有足够质量，或者证明临界带的 sawtooth 同步若持续出现，就会推出
CRT 相位块异常集中，从而触发既有的圆柱锁、短窗不可复用或完整周期均衡缺陷。
该二分已单独整理为 `docs/monograph/rse-critical-band-hard-attack.md` 中的 `CWM/CRD` 接口。
模型权扫描 `docs/monograph/cwm-selberg-critical-mass-scan.md` 显示绝对 `CWM` 在尾部 dyadic 桶不应作为主假设；核剖面扫描 `docs/monograph/scwm-crd-profile-scan.md` 显示必须保留 Selberg 符号与真实 RSE 核；双出口扫描 `docs/monograph/kscwm-crd-dual-obstruction-scan.md` 进一步显示普通小素支撑集中不足以推出缺陷；SKT 扫描 `docs/monograph/skt-smooth-transform-scan.md` 显示平滑项可线性化为 Selberg 二次型变换；SQF 扫描 `docs/monograph/sqf-quadratic-form-scan.md` 显示主瓶颈在低频 `Q(it)`；最优权扫描 `docs/monograph/sqf-qlow-optimal-weight-scan.md` 显示精确最优 Selberg 权可进一步降低零频预算；fixed-low 扫描 `docs/monograph/sqf-qlow-fixed-low-stability-scan.md` 显示裸 `Q` 在 `u>2` 会反弹；中频带权扫描 `docs/monograph/sqf-qlow-mid-weighted-absorption-scan.md` 把它压缩为固定紧区间常数界；紧区间证书 `docs/monograph/qlow-mid-comp-grid-certificate.md` 进一步显示导数余量后仍有 `certified≈0.21--0.23<0.35` 的模型余量。因此当前最稳接口为 `QLOW-MID-COMP(intervalized)/RRD/OSPC`：紧区间带权常数证书、粗数替换误差、有向小素支撑集中到 CRTDefect。

### 18.4 更新后的闭合链

新的最小链条为：

```text
RSE-OSC + RSE-AMP + RSE-CRIT
=> RSE
=> BSI
=> PTA-GSL
=> PM-R2B
=> RHI。
```

审稿状态必须写为：

```text
RSE-OSC/RSE-AMP: 有明确解析路线，待逐行证明；
RSE-CRIT: 当前唯一实质硬点；
PTA-GSL: 条件于 RSE 三段闭合。
```
