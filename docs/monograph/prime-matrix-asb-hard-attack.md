# ASB-Fail 直接硬攻：低筛余量与高素点覆盖容量

**状态：** `asb_reduced_to_relative_high_prime_point_coverage`

本报告直接硬攻 `ASB-Fail`。核心结论：不要再从全局素数间隙证明 `ASB`；应把 `ASB-Fail` 写成一个长度 `q` 的真实空窗，然后用“低素数先筛出的剩余量”压倒“高素数补洞的有效点覆盖能力”。这给出一个具体、可量化、可继续证明的矛盾不等式。

## 1. ASB-Fail 的反例窗口

设 `q=p+g` 为 `p` 后的下一素数。对实际采样的新 `q` 行

\[
J=J_s^{(q)}=[(s-1)q+1,sq]\subset [1,p^2],
\]

令

\[
r_s=(s-1)q\bmod p=(s-1)g\bmod p.
\]

当 `r_s>g` 时，`J` 不含完整旧 `p` 行，而是分成旧行尾段与下一旧行头段。`ASB-Fail` 是

\[
\sigma_{t_s}\ge p-r_s,\qquad
\pi_{t_s+1}\ge r_s+g,
\tag{ASB-Fail}
\]

等价于

\[
J\cap\mathbb P=\varnothing.
\tag{Empty-J}
\]

由于 `J\subset[1,p^2]`，若 `n\in J` 为合数，则 `n` 必有素因子 `\ell\le p`。

## 2. 低筛余集与高素覆盖

取参数

\[
z=p^\alpha,\qquad 0<\alpha<1.
\]

令

\[
P(z)=\prod_{\ell\le z}\ell,
\qquad
R_z(J)=\{n\in J:(n,P(z))=1\}.
\]

即 `R_z(J)` 是先删除所有小素数 `<=z` 斜线后的粗剩余。若 `ASB-Fail` 成立，则 `R_z(J)` 中每个数仍是合数；又因 `n<=p^2`，每个这样的合数至少有一个素因子

\[
z<\ell\le p.
\]

令高素覆盖点集为

\[
D_z(J)=\bigcup_{z<\ell\le p}\left(R_z(J)\cap \ell\mathbb Z\right).
\]

所以必有覆盖下界

\[
|R_z(J)|
\le
|D_z(J)|.
\tag{Cover-LB}
\]

因此只要能证明相反方向的严格上界

\[
|D_z(J)|
\le
(1-\eta)|R_z(J)|
\tag{RHC}
\]

对某个固定 `eta>0` 成立，就得到矛盾，从而排除 `ASB-Fail`。

这就是当前最小硬点：**相对高素点覆盖不等式** `RHC`。

注意：不能把 `D_z(J)` 简单替换为总 incidence

\[
\sum_{z<\ell\le p}|R_z(J)\cap \ell\mathbb Z|.
\]

后排遮挡审计显示，小样本中该总 incidence 可以超过 `|R_z(J)|`；重复命中会吃掉裸平均余量。因此真正目标必须是并集点覆盖，或等价地给出重复命中扣除后的有效覆盖上界。

## 3. 为什么这个不等式有希望

启发式上，低筛余集大小为

\[
|R_z(J)|
\approx
q\prod_{\ell\le z}\left(1-{1\over \ell}\right)
\sim
{e^{-\gamma}q\over \log z}.
\]

对一个已经通过低筛的点，再被某个高素数 `\ell` 命中的总 incidence 平均约为 `1/\ell`，因此

\[
{\sum_{z<\ell\le p}|R_z(J)\cap \ell\mathbb Z|
\over |R_z(J)|}
\approx
\sum_{z<\ell\le p}{1\over \ell}
\approx
\log{\log p\over \log z}
=\log {1\over \alpha}.
\]

这只说明第一矩有希望小于 `1`。遮挡审计修正了这一点：第一矩不是最终对象，最终对象是并集点覆盖；若存在重复命中，则必须用二阶交叉扣除把 incidence 压成有效点覆盖。若

\[
\alpha>e^{-1},
\]

则

\[
\log {1\over \alpha}<1.
\]

另一方面，线性筛在长度 `q\asymp p` 的窗口中要给出低筛余集正下界，通常要求筛层 `z=p^\alpha` 不超过可用筛水平的平方根，即需要

\[
\alpha< {1\over 2}.
\]

关键是区间

\[
e^{-1}<\alpha< {1\over 2}
\]

非空。这是本路线的真正结构性余量：低筛仍有正余量，而高素补洞的第一矩处于可控区间；剩余工作是把第一矩转化为点覆盖上界，或直接证明粗剩余中素数占正比例。

## 4. 现有一阶约束如何进入

`RHC` 不是裸平均估计。它必须利用此前方阵/CRT 矛盾场中已经稳定的刚性约束：

1. **相邻互质刚性。** 连续位置不能由同一个高素因子解释；高素覆盖在短窗内天然稀疏。
2. **旧/新双分块刚性。** `J` 同时是一个完整 `q` 行，又跨越两个旧 `p` 行端点；覆盖必须兼容 `r_s` 给出的拼接位置。
3. **CRT 漂移刚性。** `r_s=(s-1)g mod p` 不是任意参数，而是步长 `g` 的模 `p` 漂移；异常集中会在相邻样本间产生可检测的残基相关。
4. **斜线锁层刚性。** `<=z` 的小素数斜线已经被硬删除，高素数只能在粗剩余 `R_z(J)` 上补洞，不能重复利用小素锁层贡献。
5. **平方界刚性。** 因为 `J\subset[1,p^2]`，任意合数必有 `<=p` 的素因子；高素覆盖族完整，不存在外逃因子。

这些刚性共同服务于 `RHC`：不是证明某个任意短区间必有素数，而是证明在方阵递推采样窗口中，高素补洞的有效点覆盖覆盖不了低筛粗剩余。

## 5. 为什么普通容量法还不够

若直接用

\[
\sum_{\ell\le p}{q\over \ell},
\]

则得到约 `q log log p`，远大于 `q`，没有矛盾。必须先筛去 `<=z` 小素锁层，再估计高素数在粗剩余上的有效点覆盖，并扣除重复命中。

若使用粗糙的上下筛常数分开估计，可能出现常数损失：

\[
\text{高素上界常数} / \text{低筛下界常数}>1,
\]

从而吃掉 `log(1/alpha)<1` 的余量。因此 `RHC` 应尽量写成同一权重、同一归一化下的相对估计，而不是两个互不匹配的粗筛估计。这与此前 `RRD` 同权归一化的经验一致。

## 6. 可审稿的下一步目标

定义相对高素点覆盖率

\[
\mathcal C_z(J)=
{1\over |R_z(J)|}
|D_z(J)|.
\]

下一步只需证明存在可选参数

\[
e^{-1}<\alpha<1/2
\]

和固定 `eta>0`，使所有 `ASB` 采样窗口满足

\[
\mathcal C_{p^\alpha}(J)\le 1-\eta.
\tag{ASB-RHC}
\]

则：

```text
ASB-Fail
=> |R_z(J)| <= high-prime point coverage
=> |R_z(J)| <= (1-eta)|R_z(J)|
=> contradiction.
```

于是得到

```text
ASB(p,q)
=> Seam(p,q)
=> old-core Row(q).
```

再配合 `Annulus(p,q)` 即可完成递推路线。

## 7. 审稿结论

本轮硬攻没有把 `ASB` 宣称为已证，而是把唯一剩余压成一个明确的不等式 `ASB-RHC`。这是比全局 `SEB` 更合理的方向：它不要求证明所有长度 `q` 的区间含素数，而只要求在实际递推采样窗口中，低筛粗剩余不能被高素数补洞完全覆盖。遮挡审计进一步修正：裸 incidence 不够，必须证明点覆盖并集上界，或者等价地证明低筛粗剩余中的素数/不可覆盖点占正比例。下一步应专攻 `ASB-RHC` 的同权筛估计、重复命中扣除和 CRT 漂移异常出口。

## 8. RHC 的等价硬点更新

后续扫描见 `docs/monograph/prime-matrix-asb-rhc-alpha-sweep.md`。由于 `D_z(J)` 正好是低筛粗剩余中的合数点集，

\[
|D_z(J)|=|R_z(J)|-|R_z(J)\cap\mathbb P|.
\]

因此 `ASB-RHC` 等价于低筛粗剩余素数比例下界

\[
|R_z(J)\cap\mathbb P|\ge \eta |R_z(J)|.
\tag{RPD}
\]

这一步把真正硬点暴露得更清楚：若能证明 `RPD`，`ASB-Fail` 立即矛盾；但 `RPD` 本质是 ASB 采样短窗口中的粗剩余素数下界，不能由普通容量法自动推出。下一步应攻二分出口：

```text
RPD holds
or failure of RPD creates CRTDefect / Tail-anchor / OSPC exceptional structure.
```

## 9. RPD 失败的粗合数投影更新

后续扫描见 `docs/monograph/prime-matrix-rpd-failure-structure.md`。`RPD` 失败意味着低筛粗合数集

\[
C_z(J)=R_z(J)\setminus\mathbb P
\]

过密。样本最坏窗口显示，粗合数主要来自半素数或少因子乘积：在最坏 `40` 个窗口中，半素数占粗合数比例约 `0.858322`。因此下一步更窄的攻坚目标是

```text
Semiprime projection bound
or semiprime over-density => CRTDefect/Tail-anchor/OSPC.
```

这把 `RPD-or-CRTDefect` 从“证明短窗口粗剩余素数比例”进一步拆成两类可审稿投影：半素数双线性短区间上界与多因子能量异常出口。

## 10. 半素数锚层投影更新

后续审计见 `docs/monograph/prime-matrix-semiprime-anchor-projection.md`。对粗半素数 `n=ab` 取最小因子 `a` 为锚，半素数投影写为

\[
\sum_{a\in(z,p]} S_a(J).
\]

样本最坏窗口显示，半素数总数 `1248`，锚容量总和 `10785`，总体容量效率约 `0.115716`。压力并非单锚完全复用，而是分散在多个锚层；其中高锚层 `[0.90,1.01)` 容量效率最高，约 `0.613707`。

因此更细的最小硬点是：

```text
Anchor-layer semiprime bound
or anchor-layer over-efficiency => CRTDefect/Tail-anchor/OSPC.
```

## 11. 互补素数短区间更新

后续审计见 `docs/monograph/prime-matrix-anchor-cofactor-interval-audit.md`。锚层半素数贡献可精确写为

\[
S_a(J)=\pi(\lfloor R/a\rfloor)-\pi(\max(a,\lceil L/a\rceil)-1).
\]

因此 `RPD` 失败的半素数压力不再是抽象锚容量问题，而是互补素数短区间平均问题。最新最坏窗口账本显示，聚合素互补密度约 `0.176122`，但单窗半素数/粗合数比例可达 `1.000000`。这说明下一步不能只证明全局平均；必须证明逐窗口形式

\[
\sum_{z<a\le p}S_a(J)+M_{\ge3}(J)\le (1-\eta)|R_z(J)|
\]

或证明失败时产生 `CRTDefect/Tail-anchor/OSPC` 异常。当前最小硬点更新为：

```text
Average prime-cofactor interval bound
+ M_{>=3} budget
or density/energy spike => CRTDefect/Tail-anchor/OSPC.
```

## 12. M>=3 低锚复合互补因子更新

后续审计见 `docs/monograph/prime-matrix-mge3-budget-audit.md`。对 `M_{\ge3}` 项取最小素因子锚 `a=P^-(n)`，可得精确恒等式

\[
M_{\ge3}(J)=\sum_{z<a\le R^{1/3}}
\#\{c:\lceil L/a\rceil\le c\le\lfloor R/a\rfloor,\ c\ \text{composite},\ P^-(c)\ge a\}.
\]

最坏 `40` 个窗口中，`M_{\ge3}=206`，占粗合数 `0.141678`，占粗剩余 `0.102897`；恒等式校验差为 `0`。这说明剩余预算不再是未知多因子黑箱，而是低锚复合互补因子计数。当前 ASB/RPD 最小证明义务最终压缩为：

```text
prime-cofactor interval bound
+ low-anchor composite-cofactor bound
or corresponding density spikes => CRTDefect/Tail-anchor/OSPC.
```

## 13. 第二锚粗尾更新

后续审计见 `docs/monograph/prime-matrix-mge3-second-anchor-audit.md`。低锚复合互补因子可继续写成第二锚粗尾恒等式：

\[
M_{\ge3}(J)=\sum_{z<a\le b}
\#\{d:\lceil L/(ab)\rceil\le d\le\lfloor R/(ab)\rfloor,\ P^-(d)\ge b\}.
\]

最坏 `40` 个窗口中，第二锚恒等式计数为 `206`，校验差为 `0`，整数容量为 `1012`，容量效率为 `0.203557`，尾因子为素数比例为 `0.980583`。这把 `M_{\ge3}` 的实际压力压成三粗素因子/第二锚短尾问题。当前最终窄接口为：

```text
prime-cofactor interval bound
+ second-anchor b-rough tail bound
or density spikes => CRTDefect/Tail-anchor/OSPC.
```

## 14. 第二锚 Mertens 包络更新

后续审计见 `docs/monograph/prime-matrix-mge3-tail-envelope-audit.md`。对第二锚 `b`，用

\[
V(b)=\prod_{\ell<b}(1-1/\ell)
\]

作为 `b`-rough 尾因子密度包络。同批最坏窗口中，第二锚整数容量 `1012`，实际 `b`-rough 尾数 `206`，Mertens 包络 `165.810608`，所需全局放大常数 `1.242381`。最大层级常数为 `[2/3,0.80)` 层的 `1.700839`；最高窗口尖峰为 `3.400694`，来自极短尾区间。

因此 `M_{\ge3}` 当前不再是容量问题，而是：

```text
Aggregated second-anchor Mertens envelope
or localized tail-density spike => CRTDefect/Tail-anchor/OSPC.
```

与半素数互补素数短区间接口合并后，ASB/RPD 的当前最小证明义务为：

```text
prime-cofactor interval bound
+ aggregated second-anchor Mertens envelope
or density spikes => CRTDefect/Tail-anchor/OSPC.
```

## 15. Singleton-prime corridor 尖峰出口更新

后续审计见 `docs/monograph/prime-matrix-tail-spike-localization-audit.md`。第二锚 Mertens 包络中的高尖峰主要来自尾区间长度为 `1` 的 singleton 事件：`957` 个 pair 尾区间中，singleton 粗尾 `182` 个，其中 singleton 素尾 `181` 个，singleton 粗合尾仅 `1` 个。

若尾区间为单点 `d`，则

\[
\lceil L/(ab)\rceil=\lfloor R/(ab)\rfloor=d
\]

等价于

\[
\max(\lceil L/d\rceil,\lfloor R/(d+1)\rfloor+1)\le ab\le
\min(\lfloor R/d\rfloor,\lceil L/(d-1)\rceil-1).
\]

因此尖峰不再是一般短区间筛异常，而是 `ab` 落入极窄双曲走廊且 `d` 为素数的事件。当前 `M_{\ge3}` 侧最窄接口为：

```text
Aggregated Mertens envelope outside singleton corridors
+ singleton-prime corridor bound
or corridor spike => CRTDefect/Tail-anchor/OSPC.
```

## 16. Singleton 走廊 z-rough 上界更新

后续审计见 `docs/monograph/prime-matrix-singleton-corridor-bound-audit.md`。对 singleton-prime corridor `C_d(J)`，唯一分解和低筛约束给出确定链：

\[
\#\{(a,b):ab\in C_d,\ z<a\le b\le d\}
\le \#\{m\in C_d:(m,P(z))=1\}\le |C_d|.
\]

样本中，唯一走廊数 `175`，走廊宽度总和 `542`，合法 semiprime 对数 `181`，semiprime/宽度 `0.333948`。宽度 `1` 走廊由确定宽度界直接吸收；宽度 `>=2` 的 semiprime/`Vz` 为 `1.388255`。混合包络 `width1 + Vz(width>=2)` 为 `139.329004`，所需常数 `1.299083`。

因此当前 singleton 侧最小接口为：

```text
Singleton corridor z-rough Selberg bound
or sustained z-rough saturation => CRTDefect/Tail-anchor/OSPC.
```

这一步显式使用了矛盾场中的三类刚性：唯一分解、低素数非零同余约束、以及走廊饱和导致的有向 CRT 缺陷。

## 17. Singleton 走廊不相交更新

后续审计见 `docs/monograph/prime-matrix-singleton-corridor-overlap-audit.md`。同一 ASB 窗口内 singleton 走廊完全不重叠：走廊数 `175`，走廊宽度和 `542`，同窗口并集宽度 `542`，重叠冗余 `0`，最大重叠度 `1`。因此 singleton 侧不需要处理多重覆盖；它已经压缩为不相交短区间族上的 `z`-rough 上筛：

```text
z-rough upper sieve on disjoint singleton-corridor unions
or high local density => Tail-anchor/CRTDefect.
```

这一步新增使用的刚性是单调商分层：不同 singleton 尾值 `d` 对应的 `ab` 双曲走廊在同一窗口内按商值分层，不能相互重叠。

## 18. Singleton 走廊闭合引理

后续严写见 `docs/monograph/prime-matrix-singleton-corridor-closure-lemma.md`。该文档给出三个确定步骤：

1. **不相交。** 固定 `J=[L,R]` 时，若 `m\in C_d(J)`，则
   \[
   d=\lceil L/m\rceil=\lfloor R/m\rfloor
   \]
   由 `m` 唯一确定，因此不同 `d` 的走廊不相交。
2. **唯一分解。** `(a,b)\mapsto ab` 对 `a\le b` 的素因子对是单射。
3. **低筛注入。** 若 `z<a\le b`，则 `ab` 必为 `z`-rough。

所以 singleton 侧严格归约为

\[
\sum_d \#\{(a,b):ab\in C_d,\ z<a\le b\le d\}
\le
\#\{m\in \cup_d C_d:(m,P(z))=1\}.
\]

当前小硬点由此闭合为标准上筛接口：

```text
standard upper sieve on disjoint singleton-corridor unions
or low-mod endpoint defect => CRTDefect/Tail-anchor/OSPC.
```

注意：这只闭合 singleton-prime corridor 子问题；ASB/RPD 全链仍依赖素互补因子短区间、聚合 Mertens 包络、Annulus 和异常出口排斥。

## 19. 加权区间筛内核更新

后续严写见 `docs/monograph/prime-matrix-asb-rpd-weighted-sieve-kernel.md`。该文档把剩余两个分布输入统一为同一个加权区间 Selberg 二次型。

进一步补正见 `docs/monograph/prime-matrix-rpd-first-anchor-identity.md`：粗合数侧不应拆成“半素数 + M_{\ge3}` 两套预算。对任意粗合数 `n`，取第一锚 `a=P^-(n)` 与互补因子 `c=n/a`，则

\[
S_z(J)+M_{\ge3}(J)
=
\sum_{\substack{z<a\le p\\a\in\mathbb P}}
\#\{c\in I_a(J):P^-(c)\ge a\}.
\tag{FAC}
\]

按锚层 `A_\nu<=a<A_{\nu+1}` 分组时，`P^-(c)\ge a>=A_\nu` 给出

\[
1_{P^-(c)\ge a}\le 1_{(c,P_{<A_\nu})=1}.
\]

所以全部粗合数可由第一锚加权 `P_{<A_\nu}`-rough 区间上筛控制。这样不会把复合互补因子在半素数预算和 `M_{\ge3}` 预算中双计数。

因此 ASB/RPD 主预算可写成单一不等式：

\[
U_{\rm FAC}(J)+E_{\rm lowmod}(J)
\le
(1-\eta)R_z^-(J).
\tag{RPD-Budget}
\]

若该式成立，则 `RPD` 成立；若失败，则失败必是同权低模端点缺陷或低筛粗剩余下界缺陷，可进入 `CRTDefect/Tail-anchor/OSPC` 出口。

当前 ASB/RPD 的最小硬点更新为：

```text
first-anchor weighted rough-cofactor budget
vs lower rough-residue budget
or weighted low-mod defect => CRTDefect/Tail-anchor/OSPC
+ Annulus(p,q).
```

审计文件 `docs/monograph/prime-matrix-rpd-first-anchor-identity-audit.md` 已在 `max_p=2000`、`alpha=0.43`、后排 `25%`、最坏 `40` 个窗口中验证该恒等式：粗合数 `1454`，第一锚粗互补因子 `1454`，恒等式差 `0`。这说明下一步应直接数值化第一锚加权 Selberg 预算，而不是继续分别优化半素数和 `M_{\ge3}`。

## 20. FAC 预算常数硬点定位

新增审计见 `docs/monograph/prime-matrix-rpd-fac-budget-audit.md`。用

\[
U_{\rm FAC}^{\rm model}(J)=
\sum_{z<a\le p}{\rm cap}(I_a(J))V(<a),
\qquad
V(<a)=\prod_{\ell<a}(1-1/\ell),
\]

对同批压力窗口核查后得到：

- 总模型量 `1075.256057`，真实 FAC 粗互补因子 `1454`，全局所需常数 `1.352236`。
- `eta=0.10` 的全局允许常数 `1.675694`，`eta=0.18` 的全局允许常数 `1.526743`。
- 但逐窗口最大所需常数为 `1.695703`，已经大于 `eta=0.10` 的逐窗口最小允许常数 `1.570917`。

这说明当前最后硬点不是恒等式，也不是全局平均，而是**逐窗口 FAC 常数尖峰**。可审稿的攻击目标应固定为：

```text
FAC 尖峰由端点/低模相位造成
=> weighted low-mod endpoint defect
=> CRTDefect/Tail-anchor/OSPC；
否则分层 FAC-Selberg 预算逐窗口吸收尖峰。
```

因此下一步不应回到旧的半素数与 `M_{\ge3}` 分预算路线，而应专攻第一锚端点误差的结构化排斥：证明尖峰窗口必有可检测的低模偏置，或通过更细锚层常数把 `1.695703` 型局部峰值压回逐窗口允许余量内。

## 21. FAC 尖峰的低模端点缺陷证据

新增 `docs/monograph/prime-matrix-rpd-fac-lowmod-defect-audit.md` 直接审计截断低模端点缺陷 `D_T(J)`。结果显示，FAC 尖峰不是只在高锚尾部才出现，而是在小模层已经显著累积：

- `40` 个压力窗口全部有 FAC 正缺陷。
- `T=67` 的平均捕获率为 `0.915007`。
- `T=101` 的最小捕获率为 `0.804688`、平均捕获率为 `0.959096`。
- 最尖峰窗口 `p=53,q_row=43,J=[2479,2537]` 在 `T=17` 已捕获 `0.909089` 的最终 FAC 缺陷。

这把下一硬点从“解释 FAC 尖峰”压缩为一个更窄的命题：

```text
若 D_T(J) 在小/中等 T 上达到 FAC 缺陷的大比例，
则 q 行漂移残基与第一锚互补区间端点
在 CRT 低模周期中产生有向集中；
该集中触发 CRTDefect/Tail-anchor/OSPC。
```

目前仍不能宣称 `ASB/RPD` 闭合，因为最后的 `D_T=>CRTDefect` 还需要逐行证明。但旧的全局平均路线已经被排除，当前真正单点硬核就是低模端点缺陷到矛盾场出口的严格桥接。

## 22. Annulus 的平方壳层简化

递推链还包含 `Annulus(p,q)`。新增 `docs/monograph/prime-matrix-square-annulus-lift-lemma.md` 证明：若 `p<q` 为相邻素数且

\[
n\in(p^2,q^2],\qquad (n,\prod_{\ell\le p}\ell)=1,
\]

则 `n` 是素数或 `q^2`。所以壳层中的旧筛幸存点除 `q^2` 外自动为素数。新增素数 `q` 对旧筛幸存集合真正新增删除的也只有 `q^2`；`pq` 虽然是 `q` 的倍数，但已被旧素数 `p` 删除。

因此 `Annulus(p,q)` 不应再表述为完整壳层素数分布命题，而应表述为：

```text
Annulus-Rough(p,q):
每个由壳层负责的 q 行段含旧 p-筛幸存者，且不只含 q^2。
```

审计 `docs/monograph/prime-matrix-square-annulus-sieve-lift-audit.md` 在 `max_p=2000` 下验证壳层幸存合数例外失败数为 `0`，完整壳层 `q` 行旧筛幸存者空段数为 `0`。这说明 Annulus 侧已经被压成纯 CRT 非空问题；但仍需给出全局非空证明，不能只凭样本闭合。

## 23. 统一有符号低模桥接

新增 `docs/monograph/prime-matrix-annulus-rough-nonempty-hard-attack.md` 后，ASB 与 Annulus 的最后硬点可以合并。

- ASB/RPD 失败表现为第一锚 FAC 预算的正低模端点尖峰；
- Annulus-Rough 失败表现为壳层行段旧筛剩余为空，即负低模端点亏损。

二者统一为：

```text
large signed low-mod endpoint defect
=> directed CRTDefect/Tail-anchor/OSPC.
```

这给出最清晰的递推闭合候选链：

```text
Row(p)
+ ASB/RPD-or-positive-lowmod-exit
+ Annulus-Rough-or-negative-lowmod-exit
+ Signed-LowMod-Bridge
=> Row(q).
```

已经严格完成的是壳层结构简化：旧 `p`-筛幸存者除 `q^2` 外自动是素数。尚未完成的是统一桥接：大的有符号低模端点异常必须严格推出已有矛盾场出口。

## 24. Signed-LowMod-Bridge 的端点锯齿形式

新增 `docs/monograph/prime-matrix-signed-lowmod-bridge-hard-attack.md` 后，统一桥接被精确写成 Möbius 端点场：

\[
D_T([L,R])
=
\sum_{d\mid P_T}\mu(d)
\left(
\left\{{L-1\over d}\right\}
-
\left\{{R\over d}\right\}
\right).
\]

对完整 `q` 行，端点相位为

\[
\left\{{(s-1)q\over d}\right\}
-
\left\{{sq\over d}\right\},
\]

且 `(q,d)=1`，所以它随行号 `s` 是模 `d` 的单位旋转锯齿。于是最后硬点不再是抽象低模缺陷，而是：

```text
large endpoint sawtooth projection
=> q-rotation + CRT rigidity contradiction.
```

该文档已经证明 `large D_T` 到低模端点投影的确定桥；仍未证明的是 `SESE-low`：大投影必须触发 `CRTDefect/Tail-anchor/OSPC`。

## 25. SESE-low 到 DEC/OSPC* 的闭合

新增 `docs/monograph/prime-matrix-directed-endpoint-crtdefect-bridge.md` 后，上一节的 `SESE-low` 已经接到命名出口。该文档定义 `Directed Endpoint CRTDefect`：

\[
\mathcal E_B(I)=
\sum_{d\in B}\mu(d)
\left(\{(L-1)/d\}-\{R/d\}\right),
\]

若某个低模字典块 `B` 的 `|\mathcal E_B(I)|` 超过阈值，则进入端点型 CRTDefect。鸽巢桥证明：

```text
large signed D_T + tail controlled
=> Directed Endpoint CRTDefect / OSPC*.
```

所以当前 ASB/Annulus 递推支线的剩余不再是低模桥接，而是：

```text
Directed Endpoint CRTDefect / OSPC*
=> Tail-anchor / CRT rigidity contradiction.
```

若该出口排斥沿用主链已有 OSPC/CRTDefect 排斥定理，则递推链可以接上；若没有，该出口排斥就是最后剩余。
