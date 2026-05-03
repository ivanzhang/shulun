# H3 孤立尾点夹逼相位的容量与缺陷判据

**状态：** `singleton_clamp_capacity_criterion_proved_bilinear_obstruction_added`

本文继续攻击当前唯一剩余硬障碍：

```text
Singleton Tail Exclusion:
大量孤立 y-rough 尾点若全部为合数，是否必然触发 PDEC/ColumnCRT/endpoint/cofactor 缺陷？
```

前一层已经证明，宏观尾链被二维上筛排除后，尾部压力主要落在孤立尾点上。本文把孤立尾点的
左右夹逼相位写成精确 CRT 容量公式，并诚实指出：单靠这些容量上界仍不能无条件排除全部孤立
双粗合数；最后剩余是素数与双粗半素数的符号分离，也就是筛法奇偶障碍的单点版本。

## 1. 孤立尾点数据

令 `U_y` 为 H3 行中所有孤立尾点。对 `a in U_y` 选择唯一的尾标签

\[
\ell(a)=P^-(a)>y,
\tag{SCD-1}
\]

并选择左右小骨架标签 `r_-(a),r_+(a)<=y`，满足

\[
a-\delta_-(a)\equiv0\pmod{r_-(a)},\qquad
a+\delta_+(a)\equiv0\pmod{r_+(a)},
\tag{SCD-2}
\]

其中

\[
\delta_-(a),\delta_+(a)\in\{2,4\}.
\tag{SCD-3}
\]

等价地，

\[
a\equiv \delta_-(a)\pmod{r_-(a)},\qquad
a\equiv -\delta_+(a)\pmod{r_+(a)}.
\tag{SCD-4}
\]

若左右邻点不存在，则只使用存在的一侧；端点孤立尾点只有 `O(1)` 个，可并入端点出口。以下只写
双侧内部点。

## 2. 夹逼 CRT 单元

固定

\[
c=(\delta_-,\delta_+,r_-,r_+),
\qquad r_\pm\le y.
\tag{SCD-5}
\]

定义低模

\[
R(c)=\operatorname{lcm}(r_-,r_+).
\tag{SCD-6}
\]

夹逼同余

\[
a\equiv \delta_-\pmod{r_-},
\qquad
a\equiv -\delta_+\pmod{r_+}
\tag{SCD-7}
\]

有解当且仅当

\[
\delta_-\equiv-\delta_+\pmod{\gcd(r_-,r_+)}.
\tag{SCD-8}
\]

若无解，则该夹逼单元贡献为零。若有解，则存在唯一剩余类

\[
\rho(c)\pmod{R(c)}
\tag{SCD-9}
\]

使所有属于该夹逼单元的孤立尾点满足

\[
a\equiv\rho(c)\pmod{R(c)}.
\tag{SCD-10}
\]

这一步是严格 CRT；它把左右小骨架夹逼压成一个低模相位。

## 3. 加入尾标签后的容量

再固定尾标签 `ell>y`。因为 `ell>y>=r_\pm`，有

\[
\gcd(\ell,R(c))=1.
\tag{SCD-11}
\]

于是

\[
a\equiv0\pmod\ell,\qquad a\equiv\rho(c)\pmod{R(c)}
\tag{SCD-12}
\]

在模

\[
Q(\ell,c)=\ell R(c)
\tag{SCD-13}
\]

下给出唯一剩余类。若行窗口长度至多 `q+O(1)`，则

\[
\mathcal N(\ell,c)
\le
1+\left\lfloor {q+O(1)\over \ell R(c)}\right\rfloor .
\tag{SCD-14}
\]

特别地，若

\[
\ell R(c)>q+O(1),
\tag{SCD-15}
\]

则每个 `(ell,c)` 在一行内至多贡献一个孤立尾点。

这是单点尾块层面的基本容量公式。

## 4. 三出口判据

令 `U=|U_y|`。给定阈值 `L_tail,L_clamp,L_err`。若孤立尾点全部由双粗合数解释，则必有以下三者之一：

1. **Tail-label concentration**

\[
\max_{\ell>y}\#\{a\in U_y:\ell(a)=\ell\}>L_{\rm tail};
\tag{SCD-16}
\]

2. **Clamp concentration**

\[
\max_c\#\{a\in U_y:a\equiv\rho(c)\pmod{R(c)}\}>L_{\rm clamp};
\tag{SCD-17}
\]

3. **Distributed singleton capacity**

\[
U
\le
\sum_{\ell>y}\sum_c
\left(1+\left\lfloor {q+O(1)\over \ell R(c)}\right\rfloor\right)
\mathbf 1_{\mathcal N(\ell,c)>0}
+L_{\rm err}.
\tag{SCD-18}
\]

证明只是抽屉原理加 `(SCD-14)`：若没有尾标签集中和夹逼低模集中，则所有质量都必须由分散的
`(ell,c)` 单元承载，而每个单元受 `(SCD-14)` 限制。

解释：

- `(SCD-16)` 是尾锚/ColumnCRT 缺陷；
- `(SCD-17)` 是低模夹逼相位缺陷，可进入 `PDEC/endpoint`；
- `(SCD-18)` 是分散容量分支。

## 5. 为什么分散容量分支仍未闭合

关键事实是：`(SCD-18)` 的右侧在自然参数下并不会自动小于 `U`。

若只取粗略上界，则

\[
\sum_{\ell>y}{q\over\ell}
\asymp q\log{\log p\over\log y},
\tag{SCD-19}
\]

而夹逼标签的可选数很多。即使用最小标签唯一化，分散单元仍可承载

\[
\asymp {q\over\log y}
\tag{SCD-20}
\]

量级的孤立双粗点。这与 H3 所需的素数余量同阶。

因此，孤立尾点层已经到达真正的奇偶障碍：

```text
同一局部同余系统既允许素数幸存，也允许双粗半素数幸存；
普通上筛只能给二者合计容量，不能给“至少一个是素数”的符号下界。
```

这说明当前硬点不是缺少一次抽屉，而是需要一个能区分孤立双粗合数与素数的额外结构输入。

## 6. 当前最窄可闭合命题

由以上判据，H3 行命题的剩余可精确写成：

```text
Singleton Clamp Defect Exclusion.
For every adjacent p<q and every H3 row, if U_y has size comparable to q/log y
and all its points are composite with least prime factor in (y,p],
then either (SCD-16) tail concentration or (SCD-17) clamp concentration occurs,
or the distributed capacity branch (SCD-18) has a signed semiprime excess over
the prime survivor channel.  This signed excess must be routed to
PDEC/ColumnCRT/endpoint/cofactor.
```

这仍然是原命题内部的唯一闭合目标。它没有转到 RH、孪生素数或新的平均命题；它只把最后障碍
压到“孤立尾点的有符号半素数过剩”这一层。

## 7. 审稿级结论

本步可以严格宣称：

1. 左右小骨架夹逼给出唯一低模 CRT 类；
2. 加尾标签后给出模 `ell R(c)` 的唯一类；
3. 每个 `(ell,c)` 单元在一行中的容量满足 `(SCD-14)`；
4. 大量孤立尾点若存在，必进入尾标签集中、夹逼低模集中或分散容量三分支。

本步不能宣称：

```text
Singleton Tail Exclusion 已无条件证明。
```

原因是分散容量分支仍可在自然量级上容纳 `q/log y` 个孤立双粗点。要完成无条件闭合，下一步
必须专攻有符号半素数过剩排斥，或证明分散容量达到自然量级时必产生低模/端点/互补商缺陷。

## 8. 分散分支的双线性化

后续文件

```text
docs/monograph/prime-matrix-h3-distributed-singleton-bilinear-obstruction.md
```

把第 7 节的分散容量分支进一步写成尾标签--互补商双线性计数。在 `y>q^(2/3)` 下，每个孤立
尾点严格为

\[
a=\ell m,\qquad y<\ell\le p,\qquad m\in\mathbb P.
\]

夹逼类 `rho(c) mod R(c)` 给出互补商同余

\[
m\equiv \ell^{-1}\rho(c)\pmod{R(c)}.
\]

因此分散孤立尾点过剩等价于大量短互补商区间 `I/ell` 中的有符号素数偏差。该文件证明了
从分散坏行到双线性缺陷的确定性路由；仍未证明的是该有符号双线性缺陷必被
`PDEC/ColumnCRT/endpoint/cofactor` 排除。
