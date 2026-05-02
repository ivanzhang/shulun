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

## 10. 点态 Weil 界的压力测试

先检查最直接路线是否足够：对每个固定模数使用点态 Weil 界。

在第 8 节的非对角核中，典型不完整倒数和为

`B_d(A)=sum_{s~S} beta_s e(A \bar{s}/d)`。

完成到模 `d` 后，点态 Weil 界给出粗型估计

`B_d(A) << tau(d)(S/d+1)d^{1/2} log d`

对 divisor-bounded `beta_s` 成立。

在最危险平衡区间

`S≈P`, `d≈Q≈P/log^B P`

时，这只有

`B_d(A) << P^{1/2} log^{B/2+C}P`。

该界对单个模数是非平凡的，但 BE2-3K 需要同时平均 `d_1,d_2,h,s_1,s_2`，并取得任意预设的 `log^{-A}` 节省。逐模 Weil 界不能利用 well-factorable 权重、不能利用 `d_1,d_2` 双平均，也不能利用非对角相位在模数族中的谱抵消。

因此点态 Weil 路线最多给出临界级控制，不能作为顶刊级 BE2-3K 证明。真正需要的是 Kloosterman 平均，而不是单个 Kloosterman 和的平方根界。

## 11. well-factorable 权重的必要拆分

Rosser/Buchstab 权重的优势在于 well-factorable。对任意分解 `Q=Q_1Q_2`，可写

`lambda_d=sum_{d=uv} lambda^{(1)}_u lambda^{(2)}_v`,

其中

`u<=Q_1`, `v<=Q_2`, `|lambda^{(i)}|<=1`。

在 BE2-3K 中必须选择分解使一部分模数进入 Kloosterman 模数，另一部分进入平滑平均变量。形式上，

`d_i=u_i v_i`

后，CRT 非对角相位拆成

`mod u_1u_2` 的 Kloosterman 部分与 `mod v_1v_2` 的平滑权重部分。

这个拆分是 BFI dispersion 方法的关键：它把原来过硬的 `d_1,d_2` 双模数平均变成“一个 Kloosterman 模数族 + 一个可大筛/平滑处理的外层平均”。没有 well-factorability，BE2-3K 的平均结构不够稳定。

## 12. gcd 层与坏公共因子

第 8 节先写了 `(d_1,d_2)=1` 的主情形。完全证明必须分层处理

`g=(d_1,d_2)>1`。

设 `d_i=g e_i`，`(e_1,e_2)=1`。两个同余

`r s_1 == 2 mod d_1`, `r s_2 == 2 mod d_2`

在公共因子 `g` 上要求

`s_1 == s_2 mod g`

因为 `2r^{-1}` 在 `mod g` 中唯一。若该相容条件失败，交叉项为零；若成立，则公共因子层强迫 `s_1,s_2` 落入同一 `mod g` 类。

于是 gcd 层贡献带有额外稀疏因子约 `1/g`。求和时得到

`sum_g tau(g)^C/g`

型多对数损失，可并入 `log^C P`。因此 gcd 层不是真正硬点；真正硬点仍在互素主层的 Kloosterman 平均。

## 13. BE2-3K 的可接受充分定理：KLS-window

为避免继续混淆，把 BE2-3K 的最后分析工具命名为一个明确充分输入。

**KLS-window（窗口化 Kloosterman 谱大筛）。** 令 `C≈P/log^{O(1)}P`, `S≈P`，`H<=P/log^{O(1)}P`。对 divisor-bounded `beta_s`、well-factorable 模权 `lambda_c`、平滑窗口权 `gamma_h`，成立

`sum_{c~C} lambda_c sum_{0<|h|<=H} gamma_h sum_{s~S} beta_s e(a h \bar{s}/c) <<_A P C / log^A P`

在 BE2-3K 所需的双线性范数意义下成立；等价地，其二次型版本控制第 8 节的非对角核：

`K << N^2/(R log^A P)`。

该命题不是普通大筛，而是 Kuznetsov/谱大筛型平均 Kloosterman 定理的窗口化版本。

## 14. KLS-window 推出 BE2-3K

证明结构如下。

1. 用 well-factorable 分解把 `lambda_{d_1}lambda_{d_2}` 拆成内外两组模数。
2. 用第 12 节剥离 gcd 层，把非相容公共因子项置零，相容项付出多对数损失。
3. 对互素主层应用第 8 节 CRT 公式，把非对角项写成 Kloosterman 相位平均。
4. 对 `s` 与 `h` 做平滑分割，边界 sawtooth 由 Fourier 系数的绝对可和性付出多对数损失。
5. 应用 KLS-window 得到 `log^{-A}` 节省。
6. 汇总 dyadic 块与 well-factorable 分解，得到 BE2-3K。

因此：

`KLS-window => BE2-3K => BE2-3 => WBE2 => BMD`。

## 15. 本轮硬攻结论

本轮把 BE2-3K 再压缩了一层：

- gcd 层可控，只造成多对数损失；
- 点态 Weil 界不足，不能给任意 `log^{-A}`；
- well-factorable 权重是必须使用的结构；
- 最后硬核是 KLS-window，即窗口化 Kloosterman 谱大筛。

所以完全无黑箱版的唯一剩余已经从

`BE2-3K`

进一步定位为

`KLS-window`。

若引用 Kuznetsov/Deshouillers--Iwaniec 型谱大筛，链条闭合为外部深定理版；若坚持完全自足，下一步必须证明 KLS-window。

## 16. KLS-source：可引用外部定理包

为把引用关系精确落地，本文把 KLS-window 关联到以下两个标准外部输入。

### KLS-source-1：DI 谱 Kloosterman 大筛

引用：

Deshouillers, J.-M.; Iwaniec, H., *Kloosterman sums and Fourier coefficients of cusp forms*, Inventiones Mathematicae 70(2), 219--288, 1982, DOI `10.1007/BF01390728`.

该文的核心工具是 Kuznetsov/谱分解下的 Kloosterman 和平均估计。它提供的不是单个 Kloosterman 和的点态 Weil 界，而是模数族与频率族上的平均抵消，正好对应 KLS-window 的分析需求。

### KLS-source-2：BFI dispersion 与 well-factorable 权重

引用：

Bombieri, E.; Friedlander, J. B.; Iwaniec, H., *Primes in Arithmetic Progressions to Large Moduli. II*, Mathematische Annalen 277, 361--394, 1987.

该文关键词包括 dispersion method、Bombieri--Vinogradov theorem、averages of Kloosterman sums、products of Dirichlet polynomials、convolutions。它正是把 DI 型 Kloosterman 平均与 well-factorable 权重、Dirichlet 多项式卷积结合起来的标准来源。

## 17. KLS-source 到 KLS-window 的变量匹配

KLS-window 中的变量对应如下：

| 本文变量 | 外部定理角色 |
| --- | --- |
| `c` 或 `d` | Kloosterman 模数/level 变量 |
| `h` | 加法频率或 Bessel/Kuznetsov 变换中的 Fourier 频率 |
| `s` | 乘法逆元变量，对应 Kloosterman 分子中的可逆类 |
| `beta_s` | divisor-bounded Dirichlet 多项式系数 |
| `lambda_d` | well-factorable sieve weight |
| `C,S,H≈P/log^{O(1)}P` | BFI/DI 可处理的均衡窗口 |

第 8 节的相位

`e(-2h \bar{s_1}\bar{d_2}/d_1-2h \bar{s_2}\bar{d_1}/d_2)`

在 well-factorable 分解与 CRT 互换后，成为标准 Kloosterman 平均中的双线性逆元相位。平滑窗口和 dyadic 分割只引入多对数损失。

## 18. 外部定理版闭合命题

**Theorem KLS-ext（KLS-window 的外部定理版）。** 接受 DI 谱 Kloosterman 大筛与 BFI dispersion/well-factorable 权重定理后，第 13 节的 KLS-window 成立。

**证明。** 由第 11 节对 `lambda_d` 作 well-factorable 分解，把模数分为 Kloosterman 模数与外层平滑平均两组。由第 12 节剥离 gcd 层，非相容层为零，相容层只付出多对数损失。互素主层由第 8 节化为 Kloosterman 逆元相位平均。对该平均应用 DI 的谱 Kloosterman 大筛；对 well-factorable 模权和卷积结构应用 BFI dispersion 框架。dyadic 块、平滑截断与 sawtooth Fourier 尾只造成多对数损失，调大外部定理中的 `B(A)` 即吸收。故得到 KLS-window 的 `log^{-A}` 节省。证毕。

因此在外部引用版中：

`DI + BFI => KLS-window => BE2-3K => BE2-3 => WBE2 => BMD`。

## 19. 审稿边界

这已经实现“外部引用定理版”的闭合：每个剩余分析输入都被关联到具体经典定理源。

但它仍不是“完全无黑箱自证”。若审稿要求本文内部从 Kuznetsov trace formula 开始重证 DI/谱大筛，再重证 BFI dispersion，则还需新增独立长篇谱理论附录。当前论著的准确状态应写为：

- **外部深定理版：闭合。**
- **完全自足无黑箱版：尚需内联证明 DI/ KLS-source。**
