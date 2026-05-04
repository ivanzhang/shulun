# ThreeEdge 高尾二边同源锚点能量

**状态：** `alpha_tail_threeedge_tailanchor_energy_reduction_open`

本文处理 `ThreeEdge-Parity-PDEC` 的第二个出口：三边高尾奇偶锚。相较二点 `TailParity`，这里一个
未锁高素数命中三点中的一个点时，必同时翻转两条边；因此尾锚不是单边对象，而是三类锚点和五类差值
约束。

## 1. 三边高尾向量

在三点链

\[
d,\qquad d+r,\qquad d+2r
\tag{TTE-1}
\]

的 squarefree 支撑 `T_r` 上，写三边符号向量

\[
E(d)=(\epsilon_{01}(d),\epsilon_{12}(d),\epsilon_{02}(d)).
\tag{TTE-2}
\]

取 cutoff `R`。令 `E_{\le R}(d)` 为低模素数贡献，`E_{>R}(d)` 为高尾贡献，则逐坐标有

\[
E(d)=E_{\le R}(d)\odot E_{>R}(d),
\tag{TTE-3}
\]

其中 `\odot` 表示坐标乘法。

## 2. Telescoping 展开

把高尾素数按大小写成

\[
R<q_1<q_2<\cdots<q_s\le y.
\tag{TTE-4}
\]

令 `L_j(d)` 为 `q_j` 的局部三边状态向量。则

\[
E_{>R}(d)-{\bf 1}
=
\sum_{j=1}^s
\left(\prod_{i<j}L_i(d)\right)\odot\bigl(L_j(d)-{\bf 1}\bigr).
\tag{TTE-5}
\]

这是三边版首锚展开。乘上低模向量并求和，得到高尾向量

\[
T_R^{(3)}(r)
=
\sum_{q} A_q^{(3)}(r)\in\mathbb Z^3.
\tag{TTE-6}
\]

## 3. 三类锚点

若 `q∤r,q>2`，则 `q` 的非平凡锚点只有三类：

| 锚点类 | 条件 | 翻转边 |
|---|---|---|
| `0` | `d≡0 mod q` | `01,02` |
| `-r` | `d≡-r mod q` | `01,12` |
| `-2r` | `d≡-2r mod q` | `12,02` |

若 `q|r`，高尾局部状态恒为 `(+,+,+)`，不贡献。由此得到分解

\[
A_q^{(3)}(r)=A_{q,0}^{(3)}(r)+A_{q,-r}^{(3)}(r)+A_{q,-2r}^{(3)}(r).
\tag{TTE-7}
\]

这比二点尾锚多一类锚点，但也多一条一致性约束：每个锚点必须同时改变两条边，不能只服务一条边。

## 4. 单锚/分散能量二分

若某个线性投影 `u·T_R^{(3)}(r)` 达到阈值 `T_0`，其中 `u in {-1,0,1}^3` 为正式反例抽取得到的
边压力方向，则对任意 `Lambda>0` 至少发生一项：

1. **三边单锚集中。**

\[
\max_{q,c\in\{0,-r,-2r\}}
\left|u\cdot A_{q,c}^{(3)}(r)\right|
\ge \Lambda;
\tag{TTE-8}
\]

2. **三边分散锚点能量。**

\[
\sum_{q,c}
\left|u\cdot A_{q,c}^{(3)}(r)\right|^2
\ge {T_0^2\over N_{R,3}},
\tag{TTE-9}
\]

其中 `N_{R,3}` 是非平凡三类高尾锚点数。

证明与二点尾锚相同：先剥离单锚，再对剩余锚点和用 Cauchy--Schwarz。

## 5. 点负载与跨点相关

展开 `(TTE-9)`，得到

\[
\sum_{q,c}|B_{q,c}|^2
=
\sum_{d\in T_r}\sum_{q,c}|b_{q,c}(d)|^2
+
\sum_{\substack{d_1,d_2\in T_r\\d_1\ne d_2}}
\sum_{q,c_1,c_2} b_{q,c_1}(d_1)b_{q,c_2}(d_2).
\tag{TTE-10}
\]

第一项是点负载，受

\[
\Omega_{>R}(d(d+r)(d+2r))
\tag{TTE-11}
\]

控制，进入 Rankin/Tail 账本。

第二项是跨点相关。若同一高素数 `q` 同时锚住 `d_1,d_2`，则

\[
d_1-d_2\equiv c_1-c_2\pmod q,
\qquad c_i\in\{0,-r,-2r\}.
\tag{TTE-12}
\]

因此固定差值 `s=d_1-d_2` 可复用的高素数必须整除

\[
s(s-r)(s+r)(s-2r)(s+2r).
\tag{TTE-13}
\]

非共振差值由 Rankin 账本控制；共振差值

\[
s\in\{0,\pm r,\pm2r\}
\tag{TTE-14}
\]

不能使用乘积界，必须进入相应的多点光滑链：

```text
s=0       对角点负载；
s=±r      三点链；
s=±2r     间隔二倍的三点/四点链边界。
```

这给三边尾锚提供了比二点情形更尖锐的差值锁：所有跨点复用只可能沿五条同余射线。

## 6. 证书出口

三边高尾锚压力被压成：

```text
Single three-edge anchor certificate
or point-load Rankin/Tail anomaly
or nonresonant five-factor hot-difference Rankin anomaly
or resonant multi-point smooth chain
or finite low-mod PDEC/SAE.
```

其中单锚证书字段为：

```text
p, B, r, R;
q;
c in {0,-r,-2r mod q};
edge projection u;
low-prefix three-edge weight;
centered residue-class mass;
PDEC/SAE route key.
```

## 7. 审稿边界

已证明：

```text
three-edge tail-anchor pressure
=> single three-edge anchor
   or point-load Rankin/Tail
   or five-ray crosspoint correlation
   or resonant multi-point chain
   or PDEC/SAE.
```

尚未证明：

```text
上述所有出口不可能。
```

下一步最小硬点是严写五因子热门差值 Rankin 账本，并把新的共振 `s=±2r` 分支压成四点/间隔二倍三点链。

