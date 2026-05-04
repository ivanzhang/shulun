# EDA-Gap Barrier：早期对角避让的短区间屏障与对偶路线

**状态：** `eda_equivalent_to_special_prime_gap_input_plus_crt_dual_route`

本文继续攻 `Early-Diagonal-Avoidance`。目标不是换命题，而是把“首个零行必在对角区段之后”的
真实难度再压实：它既有 CRT 覆盖证书形式，也等价于一族 `p` 对齐短区间素数存在命题。

## 1. 三个等价对象

令

\[
M_p=\prod_{q<p,\ q\ {\rm prime}}q,\qquad
U_p(x)=\#\{1\le k<p:(px+k,M_p)=1\}.
\tag{EGB-1}
\]

对 `1<=x<=p`，上一文件已证明：

\[
U_p(x)=\pi(px+p-1)-\pi(px).
\tag{EGB-2}
\]

因此以下三命题等价：

```text
EDA(p):      U_p(x)>0 for all 1<=x<=p.
PrimeGap(p): every interval (px,p(x+1)), 1<=x<=p, contains a prime.
MinRep(p):  every full-cover CRT certificate has least positive representative >p.
```

证明链为：

1. `EDA(p)<=>PrimeGap(p)`：由 `(EGB-2)`；
2. `EDA(p)<=>MinRep(p)`：由覆盖证书分解
   \[
   Z_p=\bigcup_{\tau\in\mathcal C_p}\{x:x\equiv r_\tau\pmod {D_\tau}\}.
   \tag{EGB-3}
   \]

这说明 `EDA` 没有比短区间素数命题更弱；它只是用 CRT 语言重写了同一屏障。

## 2. 对角端点给出的硬下界

取 `x=p`，`EDA(p)` 包含

\[
\pi(p^2+p-1)-\pi(p^2)>0.
\tag{EGB-4}
\]

若 `(EGB-4)` 失败，则区间

\[
p^2+1,\ldots,p^2+p-1
\tag{EGB-5}
\]

没有素数。由于每个数都 `<=p^2+p-1`，若其中某数合成且没有 `<=p` 的素因子，则它至少为
`(p+2)^2>p^2+p-1`，矛盾。因此每个数都有 `<p` 的素因子，`x=p` 就是早期零行。

所以：

\[
X_0(p)>p\quad\Longrightarrow\quad
\pi(p^2+p-1)-\pi(p^2)>0.
\tag{EGB-6}
\]

反过来，若要证明 `X_0(p)>p`，至少必须证明 `(EGB-4)`。这是素数平方后一半区间的
Oppermann 型子命题。

## 3. 现有普通方法为什么不够

任意一般素数间隔定理若只给

\[
p_{n+1}-p_n\ll N^\theta
\tag{EGB-7}
\]

要覆盖 `N=px<=p^2` 的窗口长度 `p`，必须有

\[
N^\theta\le p\asymp N^{1/2}.
\tag{EGB-8}
\]

也就是说，指数必须达到 `theta<=1/2`，并且常数还要适配端点。任何 `theta>1/2` 的一般短区间
素数定理，即使非常强，也不能直接闭合全部 `EDA`。

因此，如果完全自足路线继续推进，必须使用 `p` 对齐和 CRT 对角结构，而不是只引用普通
`N^theta` 型短区间定理。

## 4. 初等可闭合的窄行

虽然全体 `1<=x<=p` 很硬，但固定小 `x` 可以由较粗的素数间隔输入闭合。

若存在常数 `A>1`，使对所有足够大 `N`，区间 `(N,AN)` 有素数，则当

\[
{x+1\over x}\ge A
\tag{EGB-9}
\]

时，`(px,p(x+1))` 含素数。即：

\[
x\le {1\over A-1}.
\tag{EGB-10}
\]

例如 Bertrand 型输入只闭合 `x=1`；更强的固定比例输入可闭合有限多个小 `x`。但 `x` 接近 `p`
时，比例

\[
{x+1\over x}=1+O(1/p)
\tag{EGB-11}
\]

逼近 `1`，固定比例定理完全失效。

## 5. CRT 对偶路线的真正任务

由 Möbius 反演，

\[
U_p(x)=\sum_{d\mid M_p}\mu(d)N_d(x),
\tag{EGB-12}
\]

其中

\[
N_d(x)=\#\{1\le k<p:\ k\equiv -px\pmod d\}.
\tag{EGB-13}
\]

`EDA-Dual` 的目标是构造一个非负下界证书：

\[
\sum_{d\mid M_p}\lambda_d N_d(x)>0
\quad(1\le x\le p),
\tag{EGB-14}
\]

其中权重 `lambda_d` 应满足：

1. 对所有被小素数覆盖的列给出上筛主控；
2. 对未覆盖列给出正质量；
3. 尾项不会吞掉 `p/log p` 级主余量；
4. 若尾项或低模端点项异常大，则转入 `PDEC/SAE` 缺陷出口。

这就是 CRT 语言中可继续硬攻的非循环目标。

## 6. 证书最小代表路线的真正任务

覆盖证书 `tau` 给出

\[
x\equiv r_\tau\pmod {D_\tau}.
\tag{EGB-15}
\]

若 `r_\tau^+<=p`，则证书命中早期对角段并产生反例。因此 `Certificate-MinRep Barrier` 要证明：

\[
r_\tau^+>p\quad\text{for every full-cover compatible certificate }\tau.
\tag{EGB-16}
\]

结构刚性来自：

1. 若同一 `q` 覆盖两列，则 `q` 整除列差；
2. 高素数 `q>p/2` 只能单列补洞；
3. 多个高标签的 CRT 同时命中一个小代表 `x<=p` 时，会强制很多同余
   \[
   x\equiv -k p^{-1}\pmod q
   \tag{EGB-17}
   \]
   由同一个小整数 `x` 承担。

这条路线不直接数素数，而是证明所有完整覆盖证书的最小代表都晚于对角区段。

## 7. 当前最优攻坚顺序

下一步不应再讨论“零行是否等价于光滑数”或“完整周期是否有零行”。这些已经解决。最优顺序是：

1. **EDA-Dual-K。** 构造可变阶 Bonferroni/Selberg 权重，证明低阶主项留下正余量，失败则给出
   endpoint CRT defect。
2. **High-Label-MinRep。** 对 `q>p/2` 的单列标签建立 CRT 最小代表下界；先证明高标签无法独自
   补完低骨架残洞。
3. **Low-Skeleton Defect。** 固定 `2,3,5,...,L` 低骨架，若剩余洞过少，则说明早期 `x` 在低模
   上异常集中，进入 `PDEC/SAE`。
4. **Tail absorption。** 对 `d>D` 的高阶交项建立 Rankin/Selberg 尾界，防止包含排除尾项吞掉
   正主项。

本步的突破是把剩余难度定性为：

```text
不是覆盖容量不足；
不是连续光滑数；
不是完整 CRT 周期稀疏性；
而是 p 对齐短区间素数屏障 + CRT 证书最小代表屏障。
```

后续若能闭合 `EDA-Dual-K` 或 `High-Label-MinRep` 中任一条，就能实质推进 `X_0(p)>p`。
