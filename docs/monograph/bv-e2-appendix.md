# BV-E2 附录：受限二素数卷积的平均分布接口

## 1. 目标

本附录服务于二点筛 BMD。令

`N≈P^2`, `Y=P^alpha`, `2/3<alpha<1`,

并定义受限二素数卷积

`a_n=#\{(p,m):Y<p<=P, m prime, n=pm, n in I\}`。

`w=2` 时模 `2` 已确定剥离；以下 `d` 均为奇平方自由数。

较强、便于引用的分布输入是：

**BV-E2。** 对任意 `A>0`，存在 `B=B(A)`，使

`Q=P/(log P)^B`

时成立

`sum_{d<=Q} max_{(a,d)=1} |sum_{n in I, n=a mod d} a_n - phi(d)^(-1) sum_{n in I,(n,d)=1}a_n| <<_A N/(log N)^A`。

若该定理可引用，则 BMD 误差项立即为 `o(|U_Y|)`。

但 BMD 实际需要的比 `BV-E2` 更弱。因为 Rosser/Buchstab 权重不是任意 `max_a` 权重，而是固定剩余类 `a=2` 上的 well-factorable 筛权线性组合。

**WBE2（weighted BV-E2）。** 对任意 `A>0`，存在 `B=B(A)`，使任意 level `Q=P/(log P)^B` 的 well-factorable 奇平方自由权重 `lambda_d` 满足

`sum_{d<=Q} lambda_d (sum_{n in I,n=2 mod d}a_n - phi(d)^(-1)sum_{n in I,(n,d)=1}a_n) <<_A N/(log N)^A`。

显然 `BV-E2 => WBE2`。反过来，BMD 只需要 `WBE2`，不需要完整的 `max_a` 版本。因此无黑箱化时应专攻 `WBE2` 的 Type-II dispersion，而不是过强的全剩余类最大值定理。

## 2. 从 WBE2 到 BMD

Rosser/Buchstab 权重满足 `|lambda_d|<=1`、`d<=Q`，并且可取为 well-factorable 权重。因此由 WBE2，

`sum lambda_d R_d <<_A N/(log N)^A`。

另一方面二点粗剩余主量为

`|U_Y(I)|≈N prod_{3<=q<=Y}(1-2/q)≈N/(log P)^2`。

取 `A>3` 即得

`sum lambda_d R_d=o(|U_Y(I)|)`。

这正是 BMD 需要的加权误差估计。

## 3. 为什么普通大筛不够

把非主角色项粗写为

`sum_{d<=Q} phi(d)^(-1) sum_{chi!=chi0} |P_chi M_chi|`。

直接用乘法大筛与 Cauchy 得到的典型上界为

`((Q^2+P_1)(Q^2+M_1)P_1M_1)^(1/2)`。

在最平衡块 `P_1≈M_1≈P` 且 `Q≈P/log^B P` 时，该界约为

`P^3/log^{2B}P`,

而目标是

`N/log^A N≈P^2/log^A P`。

因此普通大筛单独差一个 `P` 量级。自足证明必须使用 dispersion / Kloosterman cancellation / Type-II 结构，而不能只写“大筛显然”。

## 4. 可引用的标准外部输入

可引用的方向是 Bombieri--Friedlander--Iwaniec 型 dispersion 方法：其主题包括 Bombieri--Vinogradov 型平均、Kloosterman 平均、Dirichlet 多项式乘积与卷积。

本项目引用版可把 BV-E2 作为外部标准输入，并在参考文献中列入：

Bombieri, E.; Friedlander, J. B.; Iwaniec, H., *Primes in Arithmetic Progressions to Large Moduli. II.*, Mathematische Annalen 277 (1987), 361--394.

该文献入口记录了关键词：dispersion method, mean value theorems, Bombieri--Vinogradov theorem, averages of Kloosterman sums, products of Dirichlet polynomials, convolutions。

## 5. 自足化证明义务

若要求完全自足，需要逐行补齐以下四步。

### BE2-1：dyadic 平滑分解

把 `p,m` 分解到 dyadic 块：

`p~P_1`, `m~M_1`, `P^alpha<P_1<=P`, `M_1≈N/P_1`。

边界由平滑权和 partial summation 吸收，损失 `log^C P`。

### BE2-2：素数权替换

用 Vaughan 或 Heath-Brown 恒等式把 `1_P(p)1_P(m)` 换成有限个 Type-I/Type-II 双线性和。

目标是把所有块化为

`sum_{r~R} alpha_r sum_{s~S} beta_s 1_{rs=a mod d}`，

其中 `RS≈N`，系数满足 divisor-bounded 与二范数控制。

### BE2-3：核心 weighted Type-II dispersion

证明对所有平衡块、所有 level `Q` 的 well-factorable 权重 `lambda_d`，

`R,S >= P^{2/3-o(1)}`, `RS≈N`, `Q<=N^{1/2}/log^B N`,

有

`sum_{d<=Q} lambda_d (sum_{rs=2 mod d} alpha_r beta_s - phi(d)^(-1) main) << N/log^A N`。

这是唯一真正深的步骤。普通大筛不足，必须使用 dispersion 展开、互换同余、Poisson/Kloosterman 型消去或等价的 Type-II 均值定理。

### BE2-4：重组与主项

把所有 dyadic 块、主角色项、边界项和小素因子剥离项重组，恢复 BV-E2 的原始不平滑形式。

## 6. 审稿结论

当前 BMD 链条的准确状态是：

- 引用版：`BV-E2` 或更贴合的 `WBE2` 作为标准外部输入时，BMD 闭合；
- 自足版：BMD 剩余义务等价于 `BE2-3` 核心 weighted Type-II dispersion；
- 行列素数输入只支持 BMD-Zero，不能替代 `BE2-3`。

因此下一步若继续“无外部黑箱化”，必须专攻 `BE2-3`，而不是再回到有限模板、零行零列或普通大筛。

## 7. BE2-3 的 dispersion 展开

固定一个平衡 dyadic 块：

`R≈S≈P`, `RS≈N`,

并考虑

`E=sum_{d<=Q}lambda_d(sum_{rs=2 mod d}alpha_r beta_s - phi(d)^(-1)main)`.

对每个 `d`，因为 `(r,d)=1` 的坏项可并入小误差，主和可写为

`sum_r alpha_r (sum_{s=2 r^{-1} mod d} beta_s - phi(d)^(-1)sum_{(s,d)=1}beta_s)`。

令

`T_r=sum_{d<=Q}lambda_d (sum_{s=2 r^{-1} mod d} beta_s - phi(d)^(-1)sum_{(s,d)=1}beta_s)`。

由 Cauchy，

`|E|^2 <= (sum_r |alpha_r|^2) (sum_r |T_r|^2)`。

第一因子由 divisor-bounded 系数给出 `<< R log^C P`。于是 BE2-3 归结为证明

`sum_r |T_r|^2 << S^2 Q^2 /(R log^A P)`

的强型 dispersion 方差界。

展开 `sum_r |T_r|^2` 后得到四类项：

1. 主项-主项，精确抵消；
2. 同模或近对角项，可由 divisor bound 与 `Q<=P/log^B P` 控制；
3. 非对角同余交叉项；
4. 边界 sawtooth 项。

真正深的是第 3 项。

## 8. 非对角项的 Kloosterman 核

非对角项含有条件

`r s_1 == 2 mod d_1`, `r s_2 == 2 mod d_2`。

当 `(d_1,d_2)=1` 且所有变量与模数互素时，CRT 给出唯一剩余类

`r == rho(s_1,s_2;d_1,d_2) mod d_1 d_2`,

其中

`rho=2 \bar{s_1} d_2 \bar{d_2} + 2 \bar{s_2} d_1 \bar{d_1} mod d_1d_2`。

对 `r` 的区间计数写成主项加 Fourier 边界：

`1_{r==rho mod D}=D^{-1}sum_h e(h(r-rho)/D)`。

主频 `h=0` 与分布主项抵消；非零频率产生 Kloosterman 型相位

`e(-2h \bar{s_1}\bar{d_2}/d_1) e(-2h \bar{s_2}\bar{d_1}/d_2)`。

所以 BE2-3 的核心核是

`K=sum_{d_1,d_2}lambda_{d_1}lambda_{d_2} sum_{s_1,s_2}beta_{s_1}\bar{beta}_{s_2} sum_{0<|h|<=H} c_h e(-2h \bar{s_1}\bar{d_2}/d_1-2h \bar{s_2}\bar{d_1}/d_2)`。

这是 BFI dispersion 方法中的真正抵消来源：不是单个模的大筛，而是非对角 CRT 互换后出现的双 Kloosterman 相位平均。

## 9. BE2-3K：最后无黑箱核

可以把 BE2-3 的最后未证部分命名为：

**BE2-3K（weighted bilinear Kloosterman dispersion）。** 对所有 divisor-bounded `beta_s`、well-factorable `lambda_d`、平衡参数 `S≈Q≈P/log^{O(1)}P`，第 8 节的非对角 Kloosterman 核满足足够强的对数幂节省：

`K << N^2/(R log^A P)`。

若 BE2-3K 成立，则：

`BE2-3K => BE2-3 => WBE2 => BMD`。

这一步就是当前无黑箱化的最小真正核心。它已经不再是筛论结构问题，而是 Kloosterman 双线性平均定理。完全自足证明必须在这里引入或证明 Weil/Kuznetsov/Deshouillers-Iwaniec 型 Kloosterman 平均工具；否则只能把 BE2-3K 作为外部深定理引用。
