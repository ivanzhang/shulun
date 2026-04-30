# 显式 P0 常数包状态

**状态：** 未完成；不能伪造数值 `P0`。

## 1. 已建立文件

- 模板：`docs/explicit-p0-constants.template.json`
- 抽取脚本：`experiments/extract_p0.py`

## 2. 当前阻塞常数

### BG 多线性倒数 Kloosterman

所需字段：

- `delta_BG_multilinear`
- `C_BG_multilinear`
- `delta_BG_bilinear`
- `C_BG_bilinear`

复查 Bourgain--Garaev 源文后，定理以 `for some δ`、`o(1)`、隐含 `<<` 常数表述。尤其 `Kloost 1/2` 的证明依赖 Lemma B2 与若干加性组合估计，未给出可直接代入的数值 `δ,C`。

结论：不能直接从论文文本读取显式常数；若要得到数值，需要重写 BG 证明链，把所有 `o(1)` 与隐含常数有效化。

### Selberg 二维线性上筛

所需字段：

- `C_selberg_2linear`
- `C_selberg_remainder`

该部分原则上比 BG 更容易显式化：可使用标准 Selberg 上筛基本引理的显式版本，配合 divisor-sum 平均界。但仍需在本文参数范围内写出具体筛水平、局部因子上界与余项常数。

### 本文内部常数

所需字段：

- `C_vaughan_blocks`
- `C_rect_variation`
- `C_divisor_coeff`
- `c_R`
- `C_sieve`
- `eta`
- `rho_tail`
- `B_log`
- `A_star`

这些可以由本文证明工程给出，但尚未逐项数值化。

## 3. 两条可行路线

### 路线 A：重证 BG 显式版

优点：保留当前理论证明链。

缺点：工作量最大，需要显式化 sum-product / additive combinatorics 核心，数值阈值可能极大。

### 路线 B：替换 BG 为显式较弱界

尝试用 Karatsuba/Weil/完成和给出完全显式但较弱的 RIE 节省。如果仍足够提供固定 `c_R>0`，则可绕开 BG 非显式常数。

风险：较弱界可能不足以闭合行主体 RPO。

## 4. 当前建议

优先攻路线 B：先测试显式 Weil/完成和/双完成界能否给 `Coherent-RIE-fixed-saving` 所需的固定正节省。若失败，再回到路线 A 重证 BG 显式版。

## 5. 路线 B 初步判定：双完成显式界不足以完全替代 BG

对核心双线性倒数和

`S=Σ_{m∼M}Σ_{v∼V}A_mB_v e_P(c m^{-1}v^{-1})`

双完成/谱范数给出显式型界

`|S| <= C P^{1/2}(M^2/P+M)^{1/2}(V^2/P+V)^{1/2} log^C P`。

在平衡临界区 `M≈V≈P^{1/2}` 时，该界为

`≈ C P log^C P`，

无法给 `P/log^{A_*}P` 的固定节省。单变量完成和也只能给同阶或更弱界。

因此，仅靠 Weil/完成和/双完成的显式界不足以替代 BG。真正需要的是 BG/sum-product 型在临界体积 `MV≈P` 附近提供的幂节省。

结论：路线 B 不能单独闭合新版 `P0`；必须走路线 A，即显式化 BG 或寻找已有的显式 Bourgain/Baker 型双线性 Kloosterman 定理。

## 6. 最短新突破口：Baker 显式 Bourgain 双线性结果

BG 原文在介绍双线性 Kloosterman 和时明确写道：Bourgain 的结果已有 Baker 的 full explicit version，引用为：

R. C. Baker, `Kloosterman sums with prime variable`, Acta Arith.

这可能是显式化 `delta_BG_bilinear,C_BG_bilinear` 的最短路径。

但仍需核查三点：

1. Baker 结果是否覆盖任意区间位置 `M_1,M_2`，还是只覆盖从原点开始或 prime variable；
2. Baker 的显式常数是否足以给本文需要的 `P/log^{A_*}P` 固定节省；
3. 多线性 `Kloost 1/2` 是否仍需 BG 非显式定理，还是本文 T1 可完全改写为双线性 Baker 覆盖。

若第 3 点成立，则无需显式化 BG 多线性，只需显式 Baker 双线性 + 显式 Selberg，即可抽取 `P0`。

## 7. Selberg/内部常数的保守占位包

已新增：

`docs/explicit-p0-constants.partial.json`

其中对 Selberg 与本文内部常数给出保守占位值：

- `C_selberg_2linear=10000`
- `C_selberg_remainder=10000`
- `C_vaughan_blocks=C_rect_variation=C_divisor_coeff=1000`
- `c_R=0.001`, `C_sieve=1000`
- `eta=0.20`, `rho_tail=0.10`, `B_log=1000`, `A_star=2`

这些数值不是最终审稿常数，只是为了验证 `extract_p0.py` 的常数包格式。脚本目前仍因 BG 常数缺失而拒绝输出 `P0`，这是正确行为。

## 8. Baker 显式双线性核查任务

BG 原文引用 Baker 的 full explicit version。下一步必须完成：

1. 获取 Baker, `Kloosterman sums with prime variable`, Acta Arith. 156 (2012), 351--372；
2. 抽取其主定理中的显式指数与常数；
3. 判断其对象是 prime variable 还是任意系数 bilinear reciprocal sum；
4. 若只覆盖 prime variable，判断能否覆盖本文 Vaughan 后的素数倒数和；
5. 若覆盖，填入 `delta_BG_bilinear,C_BG_bilinear`，并重写 T1 避免多线性 BG。

这是当前最短突破口。

## 9. Baker 文献元数据已确认

可引用元数据：

Roger C. Baker, `Kloosterman sums with prime variable`, Acta Arithmetica 156 (2012), no. 4, 351--372, DOI `10.4064/aa156-4-4`。

BG 原文说明该文是 Bourgain 双线性 Kloosterman 结果的 full explicit version。

当前仍需全文定理核验。若 PDF 暂时无法自动下载，可通过 DOI/EuDML/IMPAN 手工获取。

## 10. 若 Baker 只覆盖 prime variable 的改写策略

本文 T1 原式本来就是素数变量 `n` 上的倒数和：

`Σ_n Λ(n)w(n)e_P(c d^{-1}n^{-1})`。

因此若 Baker 给的是 prime variable Kloosterman 和，而非任意 Vaughan 后系数双线性和，反而可能更贴近 T1。可尝试直接对固定 coherent d-平均应用 Baker 的 prime variable 估计：

`Σ_{p∈I} e_P(a p^{-1})`。

需要核查：

1. Baker 是否允许任意乘法系数/外层 d 平均；
2. 是否给对 `a` uniform 的界；
3. 区间长度阈值是否覆盖本文所有 `I`；
4. 对短 `I` 是否可由平凡估计吸收。

若成立，T1 可绕过 Vaughan 分解，常数包更简单。

## 11. 常数模板更新：Baker-only 模式

已把 `docs/explicit-p0-constants.template.json` 扩展出 Baker 相关字段：

- `use_baker_only`
- `delta_Baker_prime_or_bilinear`
- `C_Baker_prime_or_bilinear`
- `baker_range_theta`

用途：若 Baker 主定理足以覆盖 T1，就可启用 `use_baker_only=true`，用 Baker 常数替代 BG 多线性常数。

仍需更新 `experiments/extract_p0.py`，使其在 Baker-only 模式下不要求 `delta_BG_multilinear,C_BG_multilinear`。

## 12. `extract_p0.py` 已支持 Baker-only 模式

已更新 `experiments/extract_p0.py`：

- 当 `use_baker_only=false`，仍要求 BG 多线性与双线性常数；
- 当 `use_baker_only=true`，不再要求 `delta_BG_multilinear,C_BG_multilinear,delta_BG_bilinear,C_BG_bilinear`，改用：
  - `delta_Baker_prime_or_bilinear`
  - `C_Baker_prime_or_bilinear`
  - `baker_range_theta`

烟测显示：若内部对数损失取极保守占位 `C_vaughan_blocks+C_rect_variation+C_divisor_coeff≈3000`，即使假设 Baker 有 `δ≈0.001` 也很难给可用阈值。因此常数包需要两项同时推进：

1. 从 Baker 抽取尽可能强的显式幂节省；
2. 大幅锐化本文内部对数损失常数，不能保守取 1000 级别。

## 13. Baker 主定理抽取成功

已用纯 Python 解压 PDF 流并抽取 Baker Theorem 1。转写如下。

设

`S_q(a;x)=Σ_{x<p<=2x,(p,q)=1} e_q(a \bar p)`。

令 `q=uv`，`(u,v)=1`，`u` squarefree，`v` squarefull。若

- `x>=2`, `q>=2`, `v<=x^{1/4}`；
- `0<α<=1/24`；
- `(a,q)=1`；
- `v q^{1/2+α} <= x <= q^{3/4+α}`；

则

`S_q(a;x) <<_α x^{1-α^4/2000}`。

这里论文符号显示为 `<<_α`，因此指数显式为 `δ_Baker=α^4/2000`，但乘法常数仍依赖 `α`，未在定理行中给出数值。

## 14. Baker 定理对本文 T1 的覆盖分析

本文 T1 的模数为素数 `P`，频率为 `a=c d^{-1}`，素变量长度为 `x≈N`。若直接应用 Baker Theorem 1，取 `q=P`，则 `u=P`、`v=1`，squarefull 条件满足，`v<=x^{1/4}` 自动成立。

范围要求变为：

`P^{1/2+α} <= x <= P^{3/4+α}`。

因此 Baker 直接覆盖素变量区间长度 `N` 位于 `[P^{1/2+α}, P^{3/4+α}]` 的 T1 块，并给显式指数 `α^4/2000`。

但 T1 还含有：

1. `N>P^{3/4+α}` 的长素区间；
2. `N<P^{1/2+α}` 的短素区间；
3. d 层绝对值平均 `Σ_d |S_P(c d^{-1};N)|`。

长素区间可分割为 dyadic/short blocks 并用 Baker 覆盖，或用完成和处理。短素区间若总量 `D N<=P/log^B P` 可平凡吸收；否则仍需 Vaughan/BG 双线性或其他工具。

最关键问题是 d 层：Baker 给每个频率 `a` 的点态素变量和界。若直接相加，得到

`Σ_{d<=R}|S_P(c d^{-1};N)| <= R N^{1-δ_Baker}`。

这要小于 `P/log^A P`，需要 `R N^{1-δ} <= P/log^A P`。在最坏 `R≈P^{1/2}`、`N≈P` 时不成立。

因此 Baker Theorem 1 不能单独替代 coherent d-平均。它可覆盖 T1 的部分块，但仍需外层 d 的平均相消，或者使用 Baker 的方法重证带 d 平均的双变量版本。

## 15. Baker 可用范围与新窄硬点

取 `α=1/24`，Baker Theorem 1 给显式节省

`δ_Baker=1/663552000`。

对本文 `q=P`，覆盖素变量长度

`P^{13/24} <= N <= P^{19/24}`。

但 T1 需要 d 层绝对值平均。直接逐 d 求和过大。因此 Baker 单频率定理只能消去内层相消的非显式性，不能单独给 `P0`。

新的最窄硬点是：利用 Baker 证明中的大谱集合 Lemma 4，证明倒数频率集 `{c d^{-1}:d<=D}` 与大谱集合交集小，从而得到 d 平均。

这可称为 `Baker-frequency-large-sieve`。若该命题显式闭合，则无需完整 BG 多线性常数。


## 16. 重要修正：Baker 大谱只闭合到 `θ<5/8`

复核 `Baker-frequency-large-sieve` 后，发现旧说法“闭合 `P^{13/24}<=N<=P^{19/24}`”过强。大谱分解给

`D M P^{-δ}+C P^{1+5δ+ε}/M`。

令 `D<=P^{1/2}`、`M=P^θ`。要两项都小于 `P/log^A P`，必须有

`δ>θ-1/2`, `δ<θ/5`。

所以仅当 `θ<5/8` 时存在可用 `δ`。Baker Lemma 4 的真实显式闭合区应写为

`P^{1/2+α}<=N<=P^{5/8-σ}`。

这不是失败，而是把剩余硬点定位得更精确：现在主要缺口是 `θ>=5/8` 的频率平均横截性，而非泛泛的 BG 常数。

## 17. 新最小硬点：倒数频率横截常数

需要新增原子接口：

- `C_reciprocal_spectrum_transversal`
- `kappa_reciprocal_spectrum`
- `epsilon_reciprocal_spectrum`

目标形式：

`|{c d^{-1}:d<=D}∩Ω(I,δ)| <= C P^{1+kappa*δ+ε}M^{-2}`。

Baker 原始 Lemma 4 对任意频率集对应 `kappa=5`。若能对倒数短频率集证明：

- `kappa<5`：可实质推进阈值；
- `kappa<=3`：可覆盖到 `θ<3/4`；
- `kappa<=2+ε`：几乎覆盖全部高中长层。

因此下一步不是继续跑有限验证，而是硬攻这个横截引理，并把它常数化。


## 18. 横截引理的下一层归约：RST-4

倒数频率横截可先降为四阶矩充分条件：

`Σ_{d<=D}|Σ_{p∈I}e_P(c d^{-1}p^{-1})|^4 <= C_4 P^{1-η_4}M^2`。

若成立，则由 Markov 得

`|A_D∩Ω(I,δ)| <= C_4 P^{1-η_4+4δ}M^{-2}`，

即得到 `kappa=4` 的横截改进，已经优于 Baker 任意频率的 `kappa=5`。它只能先把高中层推进到约 `θ<2/3`，但这是可审查的第一道真突破。

RST-4 的核心计数对象为

`X=p1^{-1}+p2^{-1}-p3^{-1}-p4^{-1}`

以及短倒数和

`K_D(X)=Σ_{d<=D}e_P(cXd^{-1})`。

下一步应证明零相位四元组近对角，非零相位重数无大峰值。这个问题比完整 BG sum-product 窄，直接对应方阵斜线覆盖的相位互斥刚性。


## 19. RST-4 修正为 DFI-4 双场横截

进一步复核后，`RST-4` 作为直接四阶矩随机界偏强。更准确的最小接口是：

`DFI-4: Σ_X R_I(X)|K_D(X)| <= C_{DFI}P^{1-η}M^2`。

这里 `R_I(X)` 是素数倒数四元组相位重数，`K_D(X)` 是短 d 倒数 Fourier 和。该式直接表达两个场不能高层对齐。

若 DFI-4 成立，则得到 `kappa=4` 的横截改进；若能建立高阶 `DFI-2r` 递推，则可把有效 `kappa` 压向 `2+ε`，这是闭合高中长层并抽取显式 `P0` 的最有希望路线。


## 20. DFI-4 绝对值版被修正为 BDFI/F4S

严格尺度复核显示：

`Σ_X R_I(X)|K_D(X)| <= P^{1-η}M^2`

作为绝对值命题过强，因为 `R_I` 的均匀背景与 `|K_D|` 有随机背景贡献。正确做法是利用 Fourier 正交：均匀背景项满足 `Σ_XK_D(X)=0`，必须先平衡化。

新的正确接口为：

`F4S: Σ_{d<=D}|Σ_{p∈I}e_P(c d^{-1}p^{-1})|^4 <= C(DM^2+P^{1-η}M^2)`。

这保留不可避免的对角主项 `DM^2`，并要求非对角部分有幂节省。若 F4S 成立，则得到 `kappa=4` 的横截改进。下一步应专攻 F4S 的非对角有符号相消，而不是 DFI 的绝对值版本。


## 21. F4S 再修正：必须加入 Parseval 背景

进一步复核显示，F4S 还需加入非零频率随机背景项 `D M^4/P`。正确接口是：

`F4S+: Σ_{d<=D}|F(c d^{-1})|^4 <= C(DM^2+D M^4/P+P^{1-η}M^2)`。

这个背景项不能相消，也不能忽略。它使四阶法的自然推进范围达到约 `θ<3/4`，而非直接覆盖全部高中长层。

因此最终路线应是：

`Baker θ<5/8` -> `F4S+ 推进到 θ<3/4` -> `F6S+/F8S+ ... 层叠剥离推进到 θ<1`。

下一步应专攻 F4S+ 的超随机非对角峰值相消。


## 22. F4S+ 归约为 MRE-6

F4S+ 可进一步归约为受限能量均匀性 REU-4，再归约为六变量混合倒数能量命题 MRE-6：

`p1^{-1}+p2^{-1}-p3^{-1}-p4^{-1}=d1^{-1}-d2^{-1}`。

当前链条为：

`MRE-6 -> REU-4 -> F4S+ -> kappa=4 -> θ<3/4`。

MRE-6 是下一步最小硬点：证明短倒数频率大谱层上，素数倒数二和差质量不能显著超过随机背景。该命题直接体现互质刚性、大因子不可复用和圆柱斜率相位横截。

## 23. REU-4 严格版本

F4S+ 的当前严格充分条件是 REU-4-strict：

1. `E_+(I^{-1})<=C(M^2+M^4/P)`；
2. `|Σ_{h≠0}(ν_B(h)-M^4/P)K_A(h)|<=C P^{1-η}M^2`。

其中 `B=I^{-1}`，`A=A_D`，`K_A(h)=Σ_{a∈A}e_P(ah)`。第一项是倒数素数集加性能量；第二项是受限均匀性，也是下一步真正硬点。它严格推出 F4S+，再推出 `kappa=4` 横截收益。


## 24. MRE-6 细分为 RSL 与 NDMRE

MRE-6 进一步拆成：

1. `RSL`：短倒数频率大谱层 `H_U={h:|K_A(h)|>=U}` 可由短分母有理盒控制；
2. `NDMRE`：排除 p 对角、均匀背景、重复变量后，六变量真非对角解数有固定幂节省。

目标形式：

`N_nondiag <= C P^{-η}(M^4D^2/P+M^2D)P^ε`。

下一步最优先攻 d 侧 `RSL`，因为它只涉及短倒数和 `K_A(h)=Σ_{d<=D}e_P(chd^{-1})`，应最容易严格化。


## 25. RSL-weak 已可证明，剩余为 RSL-cross

RSL 的第一层已严格化：

1. `Σ_h|K_A(h)|^2=PD`，故 `|H_U|<=PD/U^2`；
2. 若 `h∈H_U`，则存在 `D_h⊂[1,D]`、`|D_h|>=cU`，使 `chd^{-1}/P` 在长度 `O(U/D)` 的相位盒内集中；
3. 因而所有 `d1,d2∈D_h` 给出二差分约束 `||ch(d1^{-1}-d2^{-1})/P||<=CU/D`。

这给出 `RSL-weak`。剩余硬点是 `RSL-cross`：证明这些大量短分母二差分薄带与 p 侧倒数四元组高重数层的交集有固定幂节省。


## 26. RSL-cross 压缩为 DNR

RSL-cross 可用匹配薄带模型推进：从 `D_h` 中抽取匹配 `M_h`，每条边给出短倒数差

`α=d_2^{-1}-d_1^{-1}`。

若这些 `α` 不大量落入同一小有理倍数类，则多薄带交集比单薄带有固定幂衰减。新的最小硬点为 `DNR`：短整数倒数差集合的比例非聚集。

最新链条：

`DNR -> matching thin-band decay -> RSL-cross -> MRE-6 -> REU-4-strict -> F4S+ -> θ<3/4`。

下一步最优先攻 DNR；它只涉及短整数 `d<=D`，比原素数六变量问题更窄。

## 27. DNR 修正为相位一致 PC-DNR

“任意匹配”版 DNR 过强，可能被人为固定差值或有理曲线匹配破坏。正确版本必须利用匹配来自同一个 RSL 相位盒：所有端点满足

`||chd^{-1}/P-β||<=ρ`。

新的最小硬点为 `PC-DNR-weak`：在相位 Bohr 集 `B(h,β,ρ)` 内，剔除低差边和同簇退化边后，匹配倒数差的比例能量接近随机。

链条更新：

`PC-DNR-weak -> matching thin-band decay -> RSL-cross -> MRE-6 -> REU-4-strict -> F4S+`。

下一步专攻 Bohr 集簇分解与低差退化估计。

## 28. PC-DNR-weak 修正版

Bohr 集簇分解复核后，低差边和同簇边不能声称自动很少；它们必须作为退化账本单独吸收。修正版 PC-DNR-weak 将边分为：

1. 低差边；
2. 同簇边；
3. 横截边。

只对横截边证明比例能量随机性；低差与同簇边需在 MRE-6 分层中用一维单调曲线计数吸收。下一步应专攻退化吸收。

## 29. 退化吸收已压缩为二阶谱账本

低差边与同簇边不需证明稀少。它们诱导的退化谱满足二阶复杂度界即可：

- 低差谱：`Σ_h|K_low(h)|^2 <= P R0^2D^{1+ε}`；
- 同簇谱：`Σ_h|K_samecluster(h)|^2 <= P D^{1+ε}`。

配合 p 侧中心化能量 `Σ_h|ν_B^0(h)|^2 <= C(M^4/P+M^2)P^ε`，二者可吸收到 `P^{1-η}M^2` 误差项。PC-DNR 当前剩余核心为横截边比例能量的 divisor-bound 严格证明。

## 30. 横截边比例能量已压缩为 TPE

横截边 `e=(d,d+r)` 的倒数差为 `α_e=-r/(d(d+r))`。对固定比例 `λ=a/b`，方程 `α_e=λ α_f` 化为

`b r e(e+s)=a s d(d+r)`。

固定 `(d,r,s)` 后是关于 e 的二次方程，正整数解至多一个；因 `s>R0`，得到 `R0^{-1}` 节省。比例盒版本由二次多项式导数下界处理。

得到 TPE：

`#{(e,f): α_e/α_f∈Λ} <= C|M|^2|Λ|/P+C|M|^2R0^{-1}+C|M|D^ε`。

PC-DNR-weak 现已闭合到“退化账本 + TPE”。下一步硬点是证明“比例能量低 -> 多薄带交集容量衰减”。

## 31. 桥接引理 MTD

已将“比例能量低 -> 多薄带交集容量衰减”写成 MTD：若横截匹配边频率集合满足 TPE，则

`|{x: #{α:x∈T(α,ρ)}>=qL}| <= C Pρ(ρ+R0^{-1}+D^ε/U)+C`。

中高谱层可取参数得到 `<=C PρD^{-η}`；极高谱层由大谱容量 `|H_U|<=PD/U^2` 单独吸收。

链条推进为：

`TPE + 退化账本 -> MTD -> RSL-cross`。

下一步应把 RSL-cross 与 `ν_B(h)` 分层求和相接，推出 MRE-6。

## 32. RSL-cross 接回 MRE-6 时需 L2 加权

直接用一阶层求和 `Σ_T T|G_T|` 会过粗，因 `Σ_hν_B(h)=M^4` 太大。正确对象是中心化 `ν_B^0` 的二阶能量：

`Σ_h|ν_B^0(h)|^2 <= C(M^4/P+M^2)P^ε`。

因此 MRE-6 需改为 L2 加权版：

`Σ_{h∈H_U}|ν_B^0(h)||K_A(h)| <= random L2 projection + C P^{1-η}M^2`。

下一步硬点：把 MTD 的集合容量衰减升级为对 `ν_B^0` 层的 L2 质量衰减。

## 33. MTD-L2 归约为 PBL2

集合容量版 MTD 不足以控制 `ν_B^0` 的 L2 质量。需要相对层版本：

`T^2|G_T^+∩X_*| <= D^{-η}T^2|G_T^+| + C P^εE_BD^{-η}`。

该 MTD-L2 可由 TPE 加一个新的 p 侧输入 PBL2 推出：高能层 `G_T^+` 对两个非坏薄带交集没有异常集中。

链条更新：

`PBL2 + TPE + 退化账本 -> MTD-L2 -> MRE-6-energy -> REU-4-strict -> F4S+`。

下一步专攻 PBL2。

## 34. PBL2 归约为 DBR-4

PBL2 不能仅由全局二阶能量推出；需要使用 `ν_B^0` 来自倒数素数二和差。Fourier 展开后，PBL2 归约为双 Bohr 集 Fourier 限制估计 DBR-4：

`Σ_{|m|,|n|<=H}' |Σ_{p∈I}e_P((mα+nβ)p^{-1})|^4 <= C H^2(M^2+M^4/P)+C P^{1-η}M^2`。

这里 `(α,β)` 非坏，`H≈ρ^{-1}`。链条更新：

`DBR-4 -> PBL2 -> MTD-L2 -> MRE-6-energy -> REU-4-strict -> F4S+`。

下一步专攻 DBR-4，先证明二维格频率集合的重数与近零频可控。

## 35. DBR-4 第一子引理：二维频率格控制

对 `Λ_{α,β,H}={mα+nβ}`，若非坏条件排除所有短关系

`|uα+vβ|_P>P/M`, `|u|,|v|<=2H`,

则 Λ 在盒中单射、无近零频，并且近零壳频率数满足 `<=CH^2Y/P+CH`。

DBR-4 剩余硬点变为：二维短格 Λ 与 Baker 大谱 `Ω(δ)` 的横截交集要小于任意集合交集。即 lattice-spectrum-transversal。

## 36. DBR-4 等价压缩为 BRI-4

展开二维格四阶矩后，内层是 `D_H(αX)D_H(βX)`，其中

`X=p1^{-1}+p2^{-1}-p3^{-1}-p4^{-1}`。

因此 DBR-4 等价于 p 侧倒数四元组差在两个非坏 Bohr 条件下的面积型分布。新的基础接口为 BRI-4：

`#{四元组: ||αX/P||<=ρ, ||βX/P||<=ρ} <= Cρ^2M^4+CM^2+CP^{1-η}M^2/H^2`。

链条更新：

`BRI-4 -> DBR-4 -> PBL2 -> MTD-L2 -> MRE-6-energy -> REU-4-strict -> F4S+`。

下一步专攻 BRI-4。

## 37. BRI-4 的长层突破

素数版 BRI-4 可由整数区间版 IBRI-4 推出。对整数区间倒数和，Weil 完成和给 `|S_J(t)|<=CP^{1/2}logP`。因此当 `M>=P^{3/4+ε}` 时，二维频率四阶和

`<=H^2P^2log^C P`

被目标主项 `H^2M^4/P` 吸收。

这说明长层 `θ>3/4` 可由整数完成和闭合；四阶 F4S+ 路线覆盖 `θ<3/4`。剩余压缩到 `θ=3/4` 附近的窄临界层。

## 38. 临界层拼接完成到参数义务

完成和侧覆盖

`θ >= 3/4 + C_1 loglogP/logP`，

F4S+ 因 `D<=P^{1/2}/log^K P` 的对数余量覆盖

`θ <= 3/4 + C_2 K loglogP/logP`。

选择 K 足够大即可让两侧重叠，因此 `θ=3/4` 临界层可拼接，无需 F6S+。高中长层闭合转化为显式常数义务：完成和常数 `C_W,A_W`、F4S+ 常数 `C_F`、以及筛参数 K。

## 39. 临界拼接字段已加入常数包

已加入字段：

- `C_weil_completion`
- `A_weil_completion_log`
- `K_sieve_log_saving`
- `C_f4s_background`
- `critical_overlap_margin`

脚本新增校验：

`K_sieve_log_saving > 2*A_weil_completion_log + critical_overlap_margin`。

该条件对应第 1062--1063 节的临界拼接要求：F4S+ 的 `log^{-K}` 余量必须压过完成和侧的对数损失。

## 40. 临界拼接常数的保守显式赋值

通过区间 Fourier 展开 + Weil Kloosterman 界：

`|Σ_{x∈J}e_P(tx^{-1})| <= 6P^{1/2}logP`。

四阶求和后可保守取：

- `C_weil_completion=11664`
- `A_weil_completion_log=4`

F4S+ 背景常数暂取：

- `C_f4s_background=100`

临界拼接参数可取：

- `critical_overlap_margin=4`
- `K_sieve_log_saving=16`

这些只完成临界拼接常数块；其他接口常数仍需补齐后才能抽取 P0。

## 41. F4S+ 常数拆分

`C_f4s_background=100` 只覆盖 F4S+ 的随机背景常数，不等于完整 F4S+ 已证。真正剩余节省项拆成两个原子接口：

- `C_bri4_incidence`, `eta_bri4_incidence`：BRI-4 双 Bohr 倒数四点入射节省；
- `C_reu4_energy`, `eta_reu4_energy`：REU-4 中心化能量传递节省。

脚本已要求这些字段在三接口模式下为正，并把其幂节省纳入阈值检查。当前仍不能抽取 P0，直到这两个接口完成显式证明或引用。

## 42. BRI-4 分区路线

有限域 incidence 工具（Rudnev 点-平面 incidence、Roche-Newton--Rudnev--Shkredov sum-product 能量估计）可作为 BRI-4 的中层输入，但粗误差通常只覆盖 `M` 靠近 `P^{1/2}` 的区域，不能单独覆盖 `M≈P^{3/4}`。

正确分区：

1. 中层：incidence；
2. 临界低侧：F4S+/REU 链条；
3. 长层：Weil 完成和，已显式化。

因此 `C_bri4_incidence, eta_bri4_incidence` 在常数包中应理解为“中层 incidence 输入”，不是全范围 BRI-4 的单一证明。

## 43. Incidence 中层接口 BRI-mid

引用 Rudnev 点-平面 incidence / RNRS sum-product 能量估计，可将 BRI-4 中层压缩为：若

`M H^2 <= P^{1-η_mid}`，

则

`E_W(B)<=C_mid(ρ^2M^4+M^2+P^{1-η_mid}M^2/H^2)`。

`C_bri4_incidence, eta_bri4_incidence` 应对应这里的 `C_mid,η_mid`。当前仍需从引用定理显式抽取常数；不能伪造数值。

## 44. REU-4 常数拆成 CBE-8 与 MTD-L2 节省

**历史记录，已由第 45--46 节修正。** 本节中的 CBE-8 随机尺度解释已经被第 45 节否定；常数包后续以 RCE-local 的局部双 Bohr 受限能量解释为准。

REU-4 的核心输入是中心化六/八变量能量：

`E_B=Σ_h|ν_B(h)-M^4/P|^2 <= C_8P^ε(M^4/P+M^2)`。

该输入记为 CBE-8。`C_reu4_energy` 应对应 `C_8`；`eta_reu4_energy` 应对应 MTD-L2/RSL-cross 传递中的 `D^{-η}` 节省，而不是 CBE-8 自身必须有幂节省。

下一步需要查找或证明 CBE-8 的标准 sum-product/高阶能量版本。

## 45. CBE-8 随机尺度过强，改为 RCE-4

原目标

`Σ_h|ν_B(h)-M^4/P|^2 <= C(M^4/P+M^2)P^ε`

不可能成立，因为 `ν_B(0)^2` 至少给 `M^4` 级贡献。必须先剥离对角和低维退化。

可用全局弱能量 `E_8≈M^5+M^8/P` 只覆盖较短中层；临界低侧仍需双 Bohr 受限节省。故 `C_reu4_energy, eta_reu4_energy` 应解释为 RCE-4：在 d 侧高谱诱导的坏集上，对剥离后的 `ν_B^{nd}` 的 L2 质量有 `D^{-η}` 节省。

下一步应严写 RCE-4/PBL2 的对角剥离版本。


## 46. RCE-4/PBL2 的审稿级重定义

REU 常数包已进一步收缩为局部受限能量问题。正确对象不是全局

`Σ_h|ν_B(h)-M^4/P|^2`，

而是剥离完全对角、单变量退化、均匀背景后的

`ν_B^{nd}(h)=ν_B(h)-ν_diag(h)-ν_deg(h)-M^4/P`。

所有剥离项必须回到 F4S+ 背景 `DM^2+DM^4/P`，不能占用节省项。

当前 `C_reu4_energy, eta_reu4_energy` 的含义应解释为 `RCE-local` 的显式常数：对 d 侧高谱诱导的双 Bohr 横截坏集，`ν_B^{nd}` 的局部 L2 质量必须带横截面积因子和幂节省。仅有全局弱能量 `M^5+M^8/P` 不足以覆盖 `M≈P^{3/4}` 临界层。

因此 P0 抽取仍被正确阻塞。下一步原子义务是证明或引用：

`RCE-local:` 对每个 `W(α,β;ρ)`，

`Σ_{h∈W}|ν_B^{nd}(h)|^2 <= C_R P^ε(ρ^2(M^5+M^8/P)+可吸收误差)`，

并证明 d 侧坏集分解满足 `Σρ_j^2 <= C D^{-η}`。


## 47. RCE-local 拆成两个原子

`RCE-local` 当前被拆成两个可审查原子：

1. d 侧横截面积原子：高谱坏集由非退化双 Bohr 横截覆盖，且 `Σρ_j^2 <= C P^εD^{-η}`；
2. p 侧非退化入射原子：倒数区间非退化四点差在每个双 Bohr 横截上的 L2 质量带 `ρ^2` 面积因子。

退化横截不能计入面积节省，必须进入 `DM^2+DM^4/P` 背景账本。当前最优专攻顺序是先证明 d 侧横截面积原子，再用 incidence/完成和处理 p 侧非退化入射原子。

## 48. 新最小硬点 MAL

d 侧横截面积原子不能只靠 Parseval 容量推出。必须证明多锚点引理 MAL：若 `h` 位于高谱层 `H_U`，则相位聚集不仅给出一个短弧，还给出足够多的非退化锚点对 `(d_1,d_2)`，并且这些锚点对的全局复用受乘法能量控制。

可审查目标为：定义

`R_U(h)=#{(d_1,d_2): ||h(d_1^{-1}-d_2^{-1})/P||<=ρ}`，

证明高谱下界 `R_U(h)>=cU^2`，或在归一化权重下证明 `D^{-1}R_U(h)>=cU^2/D`，同时证明全局上界

`Σ_h R_U(h)<=CP^ε(D^2ρ+D+P^{-η}D^2)`。

MAL 成立后，`Σρ_j^2<=CP^εD^{-η}` 才成为可证结论；否则 RCE-local 仍停留在路线图层面。

## 49. MAL 降级为 WMAL

进一步审查发现：硬短弧版本 `h∈H_U => R_U(h)>=cU^2` 不能仅由高谱条件推出。大相位和只给相关能量下界，不保证宽度 `ρ=U/D` 的某个短弧中含有 `cU` 个锚点。

因此当前最小硬点改为 WMAL：使用正定相关核 `Ψ_L` 定义

`R_L(h)=Σ_{d_1,d_2∈A}Ψ_L(h(d_1^{-1}-d_2^{-1}))`，

从 `|K_A(h)|>U` 推出加权相关下界，再通过 dyadic level set 转化为加权硬横截面积账本。后续证明必须以 WMAL 为准，不能使用未证的硬短弧 MAL 下界。

## 50. WMAL 进一步改为 MSD + FE

继续审查发现：正定核也不能无条件推出任意短尺度主峰；高谱只给方向相关，不给短弧聚集。因此 WMAL 必须改为二分/递推结构。

新的接口为：

`MSD + FE -> WMAL/PBL2-a`。

其中 MSD（多尺度谱二分）要求：对 `h∈H_U`，要么存在终端短簇 `M_J(h)>=cU`，要么存在非平凡小倍频 `2<=|m|<=CD/U` 使 `mh∈H_{cU}`。FE（频率逃逸）要求：高谱集合不能在大量小倍频映射下保持闭包；否则会形成乘法近似不变性，与 Parseval 容量和倒数区间完成和冲突。

当前状态：MSD 与 FE 都是待证接口，不能作为已闭合结论。下一步最优专攻是先证明 MSD 的一维多尺度分解。

## 51. MSD 进一步窗口化为 WMSD + WFE

继续审查发现：局部父弧内的 Fourier 偏置只能推出窗口化高谱证书，不能推出全局 `mh∈H_{cU}`，因为父弧外贡献可能相消。

因此当前接口进一步改为：

`WMSD + WFE -> PBL2-a/RCE-local`。

WMSD 使用窗口化和

`K_{A,w}(ξ)=Σ_{d∈A}w(d)e_P(ξd^{-1})`，

产生状态 `(ξ,w,U)`；WFE 则是窗口化频率逃逸/ Lyapunov 递推，证明非终端递推不能无限延续。旧的全局 MSD/FE 只能作为历史中间形式，后续不能直接调用。

## 52. WMSD-local 改为三输出版本

继续审查发现：二输出版 WMSD-local 对任意加权点集仍过强。纯一阶余弦偏置可能没有终端短簇，也没有非平凡倍频。

因此 WMSD-local 当前正确形式为三输出：

1. 终端短簇，进入硬横截；
2. 非平凡倍频，频率复杂度增加但谱密度不降；
3. 一阶密度增量，频率不变但 `Λ=U/r` 增加至少 `cΛ^2`。

后续 WFE 只需处理非平凡倍频长链；一阶密度增量链由 `Λ<=1` 自动有限终止。

## 53. 一阶密度增量改为层蛋糕阈值版本

进一步审查发现：固定半圆截取不能直接推出 `Λ' >= Λ+cΛ^2`。正确做法是对投影

`x_d=Re(e_P(ξd^{-1})\bar v)`

使用层蛋糕阈值 `w_τ=w1_{x_d>=τ}`。当前可证目标改为：若 `Λ=U/r<=1/2` 且无终端短簇，则存在阈值窗口使

`Λ' >= Λ(1+cΛ)`，且 `r' >= cΛr`，复杂度只增加 `logP` 因子。

高密尾部 `Λ>1/2` 单独处理，应在有限步内进入终端短簇或非平凡倍频。

## 54. 层蛋糕进一步修正为 HPD 二分

继续审查发现：层蛋糕阈值集合的复向量方向可能损失，不能保证单独推出 `Λ' >= Λ(1+cΛ)`。因此一阶结构态应改为 HPD（高投影二分）：

若加权圆周测度满足 `|μ̂(1)|>=Λμ(T)` 且无终端短簇，则至少发生：

1. 存在高投影阈值层，给出真正密度增量；
2. 或存在非平凡频率 `2<=|m|<=C/Λ`，满足 `|μ̂(m)|>=cΛ^2μ(T)`，转入倍频输出。

后续 WMSD-local 应使用四输出：终端短簇、非平凡倍频、高投影密度增量、高密尾部。HPD 是当前最小纯一维待证引理。

## 55. HPD 降级为 HPD-safe

单一余弦密度模型显示：原 HPD 的 `Λ^2` 非平凡频率输出可能过强。当前采用 HPD-safe：

1. 高投影增量分支只要求条件投影相对原均值有固定比例增益，`Λ' >= (1+c)Λ`，且质量 `r' >= cΛr`；
2. 若无高投影增量，则推出较弱非平凡频率 `max_{2<=|m|<=C/Λ}|μ̂(m)| >= cΛ^3 μ(T)`。

该弱化增加 WFE 压力，但避免使用不可证的 `Λ^2` 输出。下一步应把 HPD-safe 写成正式引理并检查 `Λ^3` 是否仍可被后续 WFE/BG 常数包吸收。

## 56. `Λ^3` 输出迫使 WFE 树状化

参数审查显示：HPD-safe 的非平凡倍频输出只给谱密度 `>=cΛ^3`。若沿单路径迭代，谱密度会按 `Λ -> Λ^3` 快速衰减，单路径 WFE 不足。

必须改为 Tree-WFE：保留每步产生的候选倍频分支。单层 Parseval 只给阈值 `Λ^5r`，在中高谱 `Λ=U/D`、`r=D` 下为 `U^5/D^4`，通常远小于 `P`，不足以矛盾。

下一步真正硬点是 Tree-WFE：利用多层乘法扩张、BG/Selberg 谱膨胀、以及终端短簇分支累计横截面积，证明弱 `Λ^3` 倍频输出仍能导向容量矛盾或足够横截覆盖。

## 57. Tree-WFE 拆成三个原子

Tree-WFE 当前拆成三个可审查原子：

1. Branch-Carleson：兄弟窗口满足逐点账本 `Σ_m w_{v,m}<=Cw_v`，否则 Parseval 不能用于不同窗口；
2. Multiplier-expansion：路径乘积集低乘法能量，保证不同路径产生足够多不同频率；这是 BG/Selberg 常数包接口；
3. Terminal-mass：若乘法扩张失败，结构退化必须产生足够多终端短簇横截，供 RCE-local 使用。

当前最小内部硬点是 Branch-Carleson；它属于 WMSD/HPD-safe 的一维分解账本，优先于外部 BG/Selberg 接口。

## 58. Branch-Carleson 改为同尺度环带版本

Branch-Carleson 不能从任意 HPD-safe 频率窗口自动得到；兄弟窗口可能高度重叠。当前安全版本为：在同一个 dyadic 投影尺度上，把投影区间分解为两两不交环带，每个环带最多选择一个代表频率。

目标接口：对非终端、非高投影增量状态，输出二择一：

1. 存在不交环带窗口 `{w_a}`，满足 `Σ_aw_a<=w_v`、`#a>=c/Λ_v`，且每个环带有代表乘子给 `Λ_v^3` 级窗口谱密度；
2. 若有效环带不足或同环带多频高能，则进入 Terminal-mass 或局部 Parseval 吸收。

下一步最小内部硬点是环带计数引理：证明无高投影增量时，必须存在足够多有效不交环带，除非已经终端或退化。

## 59. Branch-Carleson 改为加权版本

继续审查发现：要求 `#a>=c/Λ` 个有效环带可能过强。当前安全版本为 Weighted Branch-Carleson：不要求环带个数，而要求不交环带承载足够加权平方谱质量。

目标为：存在不交环带窗口 `{w_a}` 和代表乘子 `m_a`，满足

`Σ_aw_a<=w_v`,

`Σ_a ||w_a||_1 Λ_a^2 >= cΛ_v^6r_v`,

其中 `Λ_a=|K_{A,w_a}(m_aξ_v)|/||w_a||_1`。

若有效总质量不足，则剩余质量必须进入高投影增量、终端短簇或低频平滑退化。当前最小任务是证明这个加权环带质量下界。

## 60. WBC 需要能量化 EHPD-safe

继续严写发现：HPD-safe 的“存在一个非平凡频率”不足以推出 Weighted Branch-Carleson 的平方谱质量下界。当前需要 EHPD-safe（能量化 HPD-safe）：在无高投影增量、无终端短簇时，输出不交环带分解并满足

`Σ_aΣ_{2<=|m|<=C/Λ}|μ̂_a(m)|^2/μ_a(T) >= cΛ^6μ(T)`。

由 EHPD-safe 推 WBC 时，若每个环带只选一个最大频率会损失 `1/Λ`。因此 WBC 需要允许“环带-频率”加权分配 `{w_{a,m}}`，保持 `Σ_{a,m}w_{a,m}<=w_v` 并保留平方能量。

新风险：缩放窗口权重会改变谱密度与质量账本；下一步需严审能量分配是否真的保留 `Σ||w_{a,m}||_1Λ_{a,m}^2`。

## 61. WBC 改为 VWBC 向量值版本

严审后确认：按频率缩放拆窗口 `w_{a,m}=α_{a,m}w_a` 只能保留多频能量的凸组合，不能保留总平方能量，会造成 `1/Λ` 损失。因此旧 WBC 拆窗口版本作废。

当前采用 VWBC：每个不交环带窗口携带多个频率，目标为

`Σ_aΣ_{2<=|m|<=C/Λ_v}|K_{A,w_a}(mξ_v)|^2/||w_a||_1 >= cΛ_v^6r_v`,

并保持 `Σ_aw_a<=w_v`。

后续 Tree-WFE 应使用向量值 Parseval，而不是为每个频率复制窗口。

## 62. EHPD-safe 与 VWBC 容量账本

已将 EHPD-safe 写成正式一维引理：若 `|μ̂(1)|>=Λμ(T)`，无高投影增量且无终端短簇，则存在不交投影环带，使

`Σ_aΣ_{2<=|m|<=C/Λ}|μ̂_a(m)|^2/μ_a(T) >= cΛ^6μ(T)`。

VWBC 是该引理的自然输出。向量值 Parseval 应逐环带使用，以避免共享频率交叉项。单层容量仍不足，因为 VWBC 带有分母 `||w_a||_1`；去分母需要小环带质量截断，通常不能单层矛盾。

当前最小硬点转为：Tree-WFE 如何在多层递推中累积 VWBC 的归一化能量，同时控制小质量环带吸收。

## 63. 小质量环带改为 Layered Tree-WFE

继续严写发现：VWBC 的归一化能量 `|K|^2/||w_a||_1` 可能主要来自许多小质量环带，不能简单丢弃。当前处理改为按环带质量 dyadic 分层。

在质量层 `r_a≈R` 上，VWBC 给真实平方能量下界

`Σ_{a:r_a≈R,m}|K_{w_a}(mξ)|^2 >= cRΛ^6r/logP`。

若单层 Parseval 不矛盾，则该质量层作为下一代窗口继续递推。于是小质量环带成为 Lyapunov 下降机制，而非漏洞。

当前最小硬点是 Layered Tree-WFE：证明多层递推中，要么窗口质量乘积快速下降到可吸收范围，要么频率树经 BG/Selberg 扩张后与累计能量下界矛盾，要么终端短簇累计足够进入 RCE-local。

## 64. Layered Tree-WFE 的参数闭合判据

已将 Layered Tree-WFE 写成统一递推账本。对非终端路径定义质量保留比例 `q_i=R_i/r_i`、`Q_t=Π_iq_i`。谱密度最坏按 `Λ_{i+1}>=cΛ_i^3` 衰减。

若深度 `t` 的频率扩张有效数为 `B_t`，保守闭合条件为

`B_t Λ_0^{6·3^t} r_0 Q_t^2 >= C P logP`。

若该条件失败且 `Q_t` 不小，则当前 Tree-WFE 仍不足，必须依赖更强 BG/Selberg 扩张、更强 HPD 输出，或证明终端短簇/高投影增量频繁发生。

下一步最优专攻：评估 BG/Selberg 可提供的 `B_t` 是否可能压过 `Λ_0^{6·3^t}` 损失。

## 65. `Λ^3` Tree-WFE 参数不可闭合

代入中高谱参数 `D≈P^{1/2}`、`Λ_0=U/D>=D^{-1/2+σ}` 后，即使取理论最大频率扩张 `B_t=P`，闭合仍要求

`Λ_0^{6·3^t}D Q_t^2 >= logP`。

最有利的 `t=1,Q_t≈1` 给 `D^{-8+18σ}`，需 `σ>4/9` 才可能；而实际中高谱只允许小 `σ`。`t=0` 也需 `σ>1/3`。

结论：当前“纯一维 HPD-safe 的 `Λ^3` 输出 + Tree-WFE + BG扩张”路线参数不可闭合。下一步应转向 Structured-EHPD，利用倒数相位结构把非平凡低频能量从 `Λ^3` 提升到接近 `Λ^2`，或证明终端短簇/高投影增量频繁发生。

## 66. Structured-EHPD 转向

当前最优路线转向 Structured-EHPD：在实际倒数相位 `θ_d=ξd^{-1}/P` 上，若无终端短簇和无高投影增量，目标证明

`Σ_aΣ_{2<=|m|<=C/Λ}|Σ_{d∈A_a}w(d)e_P(mξd^{-1})|^2/Σ_{d∈A_a}w(d) >= cΛ^{2+ε_s}r`。

若能达到接近 `Λ^2`，则中高谱参数下 `Λ_0^2D=D^{2σ}` 可压过对数，恢复参数闭合可能。

Structured-EHPD 拆为三个原子：Inverse-curve rigidity、Ring energy transfer、Sieve-window stability。当前最小硬点是 Inverse-curve rigidity：证明倒数相位集不能模拟只有一阶 Fourier 的纯余弦密度。

## 67. ICR 必须加入窗口类限制

严写 ICR 后发现：对任意权重 `w` 命题为假，因为可人为取 `w(d)≈1+2ΛRe e_P(ξd^{-1})` 制造纯一阶偏置。因此必须改为 ICR-safe：权重 `w` 属于低复杂度窗口类 `𝓦(K)`，且不能含当前相位的一阶调制。

ICR-safe 目标为：若 `w∈𝓦(K)`、`|Σw(d)e_P(ξd^{-1})|>=Λr` 且无终端短簇/高投影增量，则

`Σ_{2<=m<=C/Λ}|Σw(d)e_P(mξd^{-1})|^2 >= cΛ^{2+ε_s}r^2 - Err(K)`。

当前最小硬点更新为：先严写窗口类 `𝓦(K)` 并证明递推中所有窗口保持低复杂度，再用完成和/Weil 或倒数相位大筛证明 ICR-safe。

## 68. 窗口类 `𝓦(K)` 与 Window-control

已定义窗口类 `𝓦(K)`：由 d 区间、低复杂度筛剩余类、投影环带、质量 dyadic 层、Selberg 平滑主函数经有限布尔操作生成。复杂度记录生成树叶数、频率数、阈值数和截断高度。

递推闭包性：WMSD/HPD/VWBC 的阈值截取、环带分解、质量分层和平滑操作使

`K_t <= K_0(CΛ^{-1}logP)^{Ct}`。

在有效短深度 `t<=O(loglogP)` 且 `Λ>=P^{-c}` 时可保持 `K_t<=P^ε`。ICR-safe 误差可取 `Err(K)<=CKP^{1/2}log^CP`，在中高谱主项 `Λ^{2+ε_s}P` 下可被吸收，只要 `K<=P^{o(1)}` 并有对数余量。

当前最小硬点转为 Reciprocal-completion：对 `w∈𝓦(K)` 证明倒数相位反集中/完成和估计，获得接近 `Λ^2` 的结构能量下界。

## 69. Reciprocal-completion 拆成证书与完成和

Reciprocal-completion 已写成反证形式：若 `|S(1)|>=Λr` 但 `Σ_{2<=m<=C/Λ}|S(m)|^2` 很小，则构造低频三角证书 `F`，使 `Σw(d)F(ξd^{-1}/P)` 一方面由 `S(1)` 给大下界，另一方面由完成和给小上界。

当前拆成两个子问题：

1. Zero-mean certificate：构造平均为零、低 `A` 范数、强一阶检测的低频 `F`；
2. Windowed completion：对 `w∈𝓦(K)` 证明 `Σw(d)F(ξd^{-1}/P)=O(KP^{1/2}log^CP||F||_A)`。

新风险：若 `F` 平均项不为零，主项 `c_0r` 会掩盖矛盾。因此下一步最小硬点是 Zero-mean certificate。

## 70. Zero-mean certificate 严审与 Relative-ICR 修正

继续严写发现：绝对零均值线性证书是错误接口。若完成和上界对所有平均为零低频测试函数成立，则取 `F(θ)=e^{-iφ}e(θ)+e^{iφ}e(-θ)` 会直接推出 `|S(1)|<=CKP^{1/2}log^CP`，从而排除当前高谱本身。这与递推语境冲突，因为 `S(1)` 大是已观察到的高谱方向，不能被普通完成和直接禁止。

因此 Reciprocal-completion 必须改为相对形式：当前一阶方向作为允许主模态，只证明它不能在倒数曲线窗口上孤立存在。新的目标是 Relative-ICR：若 `w∈𝓦(K)`、`|S(1)|>=Λr`，且无终端短簇和无高投影增量，则

`Σ_{2<=|m|<=C/Λ}|S(m)|^2 >= cΛ^{2+ε_s}r^2 - Err(K)`。

当前最小硬点更新为 LBE（Layer-boundary energy）：从一阶偏置构造正弧层窗口 `w_τ=w1_{Re(e^{-iφ}u)>=τ}`，证明层边界质量若不集中成终端短簇或高投影层，就必须泄漏到 `m>=2` 的短频能量。若 LBE 成立，则 Structured-EHPD 的 `Λ^2` 级输出有真实闭合路径；若失败，失败样本应自动进入两个终端分支之一。

## 71. LBE 拆分与残差型修正

继续严写 LBE 后发现：原始层边界能量不等式仍偏强，因为层差 `B_j` 的 Fourier 展开中，均匀项 `a_{j,0}r` 与当前允许的一阶项 `a_{j,1}S(1)` 都可能解释大量层质量；短频 `m>=2` 只能控制残差

`Δ_j=μ(B_j)-a_{j,0}r-2Re(a_{j,1}S(1))`。

因此 LBE 必须改为残差型：若无终端短簇和无高投影增量，则有效层族上的一阶模型残差满足

`Σ_j |Δ_j|^2/μ(E_j) >= cΛ^{2+ε_s}r^2 - Err(K)`。

而 Fourier 截断与 Cauchy 给出反向上界

`Σ_j |Δ_j|^2/μ(E_j) <= Clog^C(1/Λ)Σ_{2<=|m|<=C/Λ}|S(m)|^2 + Err(K)`。

当前最小硬点进一步精确为 OMR（One-mode rigidity）：证明倒数相位窗口若在所有有效层上都近似服从“均匀项 + 一阶偏置项”，则必然产生终端短簇、高投影增量，或需要引入当前相位一阶调制而使窗口复杂度越界。逻辑链更新为：`OMR -> residual LBE -> Relative-ICR -> Structured-EHPD`。

## 72. 审稿级链条复核与 P0 抽取状态

本轮严格复核结论：当前文档不能抽取最终有限验证阈值 `P0`，原因不是脚本问题，而是证明链仍含未闭合原子接口。

已闭合或已机械化的部分：

1. `experiments/extract_p0.py` 能读取显式常数表并机械搜索 `log(P0)`；
2. 脚本具有安全阻塞机制，若缺少原子常数不会输出伪阈值；
3. `python3 -m py_compile experiments/extract_p0.py` 通过；
4. 使用 `docs/explicit-p0-constants.partial.json` 运行时正确阻塞。

阻塞信息为：

`缺少原子常数，不能抽取 P0：delta_BG_multilinear, C_BG_multilinear, delta_BG_bilinear, C_BG_bilinear`。

此外，最新理论链条中 `Structured-EHPD` 仍依赖

`OMR -> residual LBE -> Relative-ICR -> Structured-EHPD`，

其中 OMR 与 residual LBE 目前是明确的待证接口，不应记为已证。因此即使补齐旧 BG 常数，也还必须确认这些新接口已转化为显式常数包，否则不能宣称无条件闭合到全部奇素数。

当前可审稿结论：

- 不能给出最终 `P0`；
- 不能启动“全部小于 P0 的奇素数有限验证”作为闭合证明的一部分；
- 下一步必须先完成并显式化 OMR/residual-LBE/Relative-ICR 或退回已完全证明的旧路线常数包；
- 一旦所有原子常数补齐，有限验证阈值抽取命令固定为：

`python3 experiments/extract_p0.py --constants docs/explicit-p0-constants.json --max-log <Y>`。

## 73. OMR 显式化常数槽

本轮将 OMR 改写为显式参数接口。主文档新增 `C_OMR_layer`、`C_OMR_model`、`C_OMR_projection`、`kappa_OMR`、`A_OMR_log`、`epsilon_OMR_power` 等常数槽，并把 OMR 拆为三项：

1. OMR-1：层残差到一阶矩匹配，负责平滑层逼近和 Fourier 误差；
2. OMR-2：一阶圆周模型的显式层质量偏差计算；
3. OMR-3：稳定一阶倾斜迫使高投影增量或非法当前相位调制。

已将这些常数槽接入 `experiments/extract_p0.py`，并用 `use_omr_pack` 开关控制。默认关闭，因此不会影响旧 BG/Baker 路线的安全阻塞；开启后脚本会要求 OMR 常数为正，并检查 `kappa_OMR<1`、`epsilon_OMR_power>4`。

当前状态：OMR 已经可进入常数表框架，但仍未证明完成。真正最小硬点是 OMR-3，即证明“纯一阶分散倾斜”不能在相位独立窗口中长期存在；它必须转化为合法高投影增量，或暴露出非法当前相位调制。

## 74. OMR-3 压缩为 GTP

继续专攻 OMR-3 后，已将“纯一阶分散倾斜不可能”改写为生成树投影定理 GTP（Generation-tree projection）。核心思想是：对窗口生成树 `Tree(w)` 建立当前相位相关 `Corr_ξ(v)` 的望远镜账本。若所有节点都没有高投影增量，则根节点的一阶相关只能来自叶子相关；而叶子相关由相位独立性与非共振倒数完成和控制为 `O(KP^{1/2}log^CP)`，不足以解释 `|S(1)|>=Λr`。

因此 OMR-3 当前被压缩为两个可审查技术义务：

1. `disjoint refinement`：窗口生成树可按层不交细化，复杂度只增至 `Klog^CK`，从而避免增量常数损失 `1/K`；
2. `nonresonant reciprocal completion`：祖先投影环带与当前频率非共振时，倒数相位完成和给 `P^{1/2}log^C P` 上界；若共振，则等价于非法当前相位调制。

若这两项成立，则 GTP 成立；GTP 给 OMR-3；OMR-3 与 OMR-1、OMR-2 合成显式 OMR。下一步最优专攻是 `nonresonant reciprocal completion`，因为它可由 Weil/完成和估计支撑，是最接近外部可引用定理的环节。

## 75. NRC 非共振完成和严写

继续专攻后，已将 `nonresonant reciprocal completion` 写成 NRC 接口。叶子窗口展开后，每项都化为

`Σ_{d∈I, d≡a mod q} e_P(αd^{-1})`，

其中 `α=ξ+Σ_i m_iξ_i`。只要 `α not≡0 mod P`，完成法把不完全和转为完整 Kloosterman 型和

`Σ_{t mod P} e_P(αt^{-1}+ht)`，

由 Weil 界给 `O(P^{1/2})`，再由完成和带来 `logP` 损失。因此 NRC 解析常数可复用已有 `C_weil_completion` 与 `A_weil_completion_log`，不需要新增解析黑箱。

唯一新增的是结构性非共振条件：当前频率 `ξ` 不能落入祖先频率的有限低频整数组合 `Span_H(Ξ(w))`。若该条件失败，不应算作误差，而应作为 `frequency-collision terminal` 回流到 Tree-WFE 的频率闭包/碰撞分支。

当前 OMR-3 的解析部分基本闭合；剩余组合义务是 `disjoint refinement`：把窗口生成树按层不交细化，使叶子相关账本损失从 `K` 降到 `log^C K` 级别。

## 76. P0 抽取剩余障碍与 DR/CGTP 修正

本轮复跑阈值抽取，脚本仍正确阻塞：

`缺少原子常数，不能抽取 P0：delta_BG_multilinear, C_BG_multilinear, delta_BG_bilinear, C_BG_bilinear`。

进一步严攻 OMR-3 的 `disjoint refinement` 后发现：原先希望用同层不交细化把 L1 叶子相关损失从 `K` 降到 `log^C K`，这一目标偏强。对不交原子更自然、可证的是平方能量账本。因此 GTP 应修正为 CGTP（Carleson-energy GTP）：若根相关 `|S(1)|>=Λr`，则某层归一化平方能量

`E_s(ξ)=Σ_α |Σ_dP_{s,α}(d)e_P(ξd^{-1})|^2/||P_{s,α}||_1`

必须达到 `cΛ^2r/log^A K`，除非某个操作已经产生高投影增量。NRC 控制大质量原子的小背景，小质量原子需要 Carleson packing 吸收。

当前 P0 抽取有四个真实障碍：

1. 常数表仍缺旧 BG 四个常数；
2. 若采用 Structured-EHPD 新路线，必须证明并显式化 OMR/residual-LBE/Relative-ICR；
3. OMR 的剩余核心是 CGTP 的能量账本与小质量原子吸收；
4. NRC 引出的 `frequency-collision terminal` 必须接入 Tree-WFE，证明频率碰撞分支能闭合。

所以当前不能成功抽取 `P0`。下一步最小真实突破点是 CGTP，而不是继续填伪常数。

## 77. CGTP 条件闭合与 Λ⁴ 风险

本轮专攻 CGTP，已将其写成三段条件闭合链：

`martingale energy increment -> variance-to-density -> small-mass packing`。

关键构造：同层不交原子 `𝒫_s` 给出条件平均能量

`E_s(ξ)=Σ_A |Σ_{d∈A}w(d)e_P(ξd^{-1})|^2/Σ_{d∈A}w(d)`。

根相关 `|S(1)|>=Λr` 给 `E_s>=Λ^2r`。若相邻层能量增量大，则父原子切分存在加权方差；方差若不由小质量块承担，就通过 `Variance-to-density` 给高投影增量。小质量块由 Carleson packing 吸收：若小块总质量大，则边界层本身给高投影增量；若小，则平凡能量贡献可吸收。

保守合并后得到条件：

`Λ^4 r >= C_CGTP K_eff P log^{A_CGTP}P`

时，若无频率碰撞、无非法调制，就必须有高投影增量。因此 CGTP 当前可条件闭合 OMR-3，但带来 `Λ^4` 门槛，而不是理想 `Λ^2`。

这暴露出新的参数风险：若 `Λ^4` 回代 Structured-EHPD/Tree-WFE 后仍不可闭合，则必须强化 small-mass packing，把 `ρ^{-1}≈Λ^{-2}` 损失降到对数级。下一步应优先做参数回代，判断 `Λ^4` 是否还能支撑最终 P0 路线。

## 78. Λ⁴ 回代失败与 LSMP 新硬点

本轮将 CGTP 的保守门槛 `Λ^4r` 回代到中高谱尺度：取 `r≈D`、`D≈P^{1/2}`、`Λ=U/D`、`U>=D^{1/2+σ}`，则

`Λ^4r=U^4/D^3>=D^{-1+4σ}=P^{-1/2+2σ}`。

这无法压过完成和背景，也比 Structured-EHPD 所需的 `Λ^2D=D^{2σ}` 少了因子 `Λ^2=D^{-1+2σ}`。因此保守 CGTP 的 `Λ^4` 门槛不足，不能用于最终 `P0` 闭合。

新的最小硬点是 LSMP（Log-loss small-mass packing）：证明小质量原子若携带大相位能量，则必须回流到终端短簇、高投影增量或频率碰撞；在无这些终端时，小质量原子只造成对数损失，而不造成 `Λ^{-2}` 损失。

若 LSMP 成立，CGTP 可恢复 `Λ^2` 门槛；若 LSMP 失败，失败样本本身应给出新的结构终端。因此下一步必须专攻 LSMP。

## 79. LSMP 局部化为边界层二分

本轮专攻 LSMP，已把“小质量大能量必回流”局部化。固定父原子 `A`，小质量子块来自允许阈值函数 `T` 的薄层

`B(t,h)=A∩{t<=T<t+h}`。

若小质量能量 `E_small(A)>=ηΛ^2R`，coarea 压缩给出一族薄边界层，总质量至少 `cηΛ^2R/log^AK`。再按当前相位投影进行聚集/分散二分：

1. 聚集：若某个长度 `C/Λ` 的相位弧承载足够边界层质量，则得到终端短簇；
2. 分散：若无短簇，则边界层分布在许多相位分离弧上；其允许环带并集应给高投影增量；
3. 若分散却不能形成合法增量，则说明边界层由祖先频率低频组合追踪当前频率，回流为 frequency-collision terminal。

同时加入方差方向筛选：从 `ηΛ^2R` 能量中抽出同向偏移块，其质量达到 `cηΛR/log^AK`，从而匹配短簇/投影增量所需尺度。

当前 LSMP 剩余两个严审点：coarea 压缩常数；分散相位弧族到合法高投影增量。下一步应优先严写第二点。

## 80. LSMP 的分散到增量：DPI

本轮专攻 LSMP 的第二严审点，已将“分散相位弧族推出高投影增量”写成 DPI（Dispersed projection increment）。核心修正是引入父模型测度

`μ_A^{geo}(B)=μ(A)|B|/|A|`，

高投影增量必须相对于父原子内部几何期望定义，而不能相对于全局均匀测度。

DPI 断言：若边界层族总有效质量达到 `cηΛR/log^AK`、无短簇、无频率碰撞，且 `Λ` 乘以有效质量压过 NRC 背景，则存在允许并集窗口 `B_*` 满足

`μ(B_*) >= (1+cηΛ^2/log^AK) μ_A^{geo}(B_*)`。

潜在风险是倒数映射在父窗口 `A` 上相对相位弧不均匀；该风险也由非共振倒数完成和控制，若无法控制则回流为高投影增量或 frequency-collision terminal。因此 DPI 不引入新解析黑箱。

当前 LSMP 剩余唯一核心是 coarea 压缩常数：从小质量子块族抽取薄边界层族时，保持有效质量和复杂度只有对数损失。

## 81. LSMP 条件闭合与 CGTP 恢复 Λ²

本轮专攻剩余 coarea 压缩常数，新增离散 coarea 压缩引理：小质量有效块族在阈值函数 `T` 的 dyadic 网格上，可抽取一层薄边界层族 `B=A∩{a<=T<a+h}`，总有效质量只损失 `logK`，复杂度只增 `log^CK`。

结合方向筛选，若 `E_small(A)>=ηΛ^2R`，则可得到总质量 `>=cηΛR/log^AK` 的同向薄边界层族。再由 DPI，若无短簇、无高投影增量、无频率碰撞且 NRC 背景可吸收，则矛盾。因此 LSMP 条件闭合：无终端时小质量能量 `<ηΛ^2R`。

代回 CGTP，小质量原子不再造成 `Λ^{-2}` 损失，CGTP 恢复 `Λ^2` 门槛：

`Λ^2r >= C K_eff P^{1/2}log^A P`。

中高谱回代为 `Λ^2D=D^{2σ}`，可压过固定对数损失。当前剩余不再是 LSMP，而是两个上层接口：将 `frequency-collision terminal` 接入 Tree-WFE；将 OMR/CGTP/LSMP 常数槽正式并入 `extract_p0.py` 的阈值检查。

## 82. 剩余接口完善：频率碰撞与常数槽

本轮完善两个上层接口。

首先，将 `frequency-collision terminal` 接入 Tree-WFE。若当前频率 `ξ` 落入祖先频率低频 span，

`ξ∈Span_H(Ξ)={-Σ_i m_iξ_i:Σ|m_i|<=H}`，

则该节点不再作为新频率扩张，而进入低维频率闭包账本。频繁碰撞时，要么低维 span 内能量超过 Parseval 容量，要么某个 span 原子给高投影增量，要么质量集中给短簇。因此频率碰撞不是漏洞，而是 Tree-WFE 的第四终端分支。

其次，将 OMR 包的常数槽扩展到 CGTP/LSMP/碰撞账本：`C_CGTP,A_CGTP_log,C_LSMP,A_LSMP_log,C_collision_span,A_collision_span_log`。`extract_p0.py` 在 `use_omr_pack=true` 时会要求这些常数为正，并检查 OMR/CGTP/LSMP/碰撞账本总对数损失小于 `K_sieve_log_saving`。

当前接口状态：LSMP 已条件闭合，frequency-collision 已接入 Tree-WFE，抽取器已有常数槽。但仍不能抽取最终 `P0`，因为常数文件尚未提供完整数值，且旧 BG/Baker 或三接口路线常数仍缺失。

## 83. 结构化路线从 BG 常数阻塞中解耦

本轮继续处理剩余障碍：将 Structured-EHPD/OMR 路线从旧 BG 四常数阻塞中独立出来。`extract_p0.py` 新增 `use_structured_ehpd` 开关；当 `use_structured_ehpd=true` 且 `use_omr_pack=true` 时，脚本不再要求 `delta_BG_multilinear,C_BG_multilinear,delta_BG_bilinear,C_BG_bilinear`，也不要求 Baker-only 常数，而改为要求 OMR/CGTP/LSMP/碰撞账本常数。

新增模板 `docs/explicit-p0-constants.structured-template.json`。用该模板运行时，当前阻塞已精准变为：

`C_OMR_layer, C_OMR_model, C_OMR_projection, kappa_OMR, A_OMR_log, epsilon_OMR_power, C_CGTP, A_CGTP_log, C_LSMP, A_LSMP_log, C_collision_span, A_collision_span_log`。

这说明抽取器层面的路线阻塞已排除；剩余障碍是给这些结构常数赋显式数值，并审查它们满足对数损失约束。

## 84. 条件结构常数包的阈值抽取

本轮为 Structured-EHPD/OMR 路线建立了一个条件常数文件：

`docs/explicit-p0-constants.structured-conditional.json`。

该文件不是最终审稿常数，而是用于验证抽取管线和参数余量的条件候选。使用命令

`python3 experiments/extract_p0.py --constants docs/explicit-p0-constants.structured-conditional.json --max-log 100000 --step 1`

得到机器阈值结果：

`docs/explicit-p0-structured-conditional-result.json`

其中

`log_P0_upper = 7550`, 即 `P0 <= exp(7550)`。

重要审查说明：这是条件阈值，不是无条件最终阈值。它依赖当前赋值的结构常数，尤其是 OMR/CGTP/LSMP/碰撞账本常数与 `tail_error_power=4.0`。要升级为最终 `P0`，必须把这些常数逐项从正文证明中显式推出，而不是作为候选赋值使用。

## 85. 条件阈值优化：主瓶颈与优化版

本轮对 `exp(7550)` 条件阈值做敏感性分析。结论：当前瓶颈不是 OMR/CGTP/LSMP 常数，而是 C 区平凡估计中的总对数损失

`C_vaughan_blocks + C_rect_variation + C_divisor_coeff`。

在原条件包中三项总和为 `60`，阈值为 `logP0=7550`。扫描结果如下：

- 总损失 `45`：`logP0=5523`；
- 总损失 `30`：`logP0=3570`；
- 总损失 `24`：`logP0=2817`；
- 总损失 `18`：`logP0=2085`；
- 总损失 `12`：`logP0=1381`；
- 总损失 `9`：`logP0=1043`；
- 总损失 `6`：`logP0=718`；
- 总损失 `3`：`logP0=411`。

已生成优化候选常数包：

`docs/explicit-p0-constants.structured-optimized.json`

其中取 `C_vaughan_blocks=C_rect_variation=C_divisor_coeff=4`，总损失 `12`。机器抽取得到：

`docs/explicit-p0-structured-optimized-result.json`

结果为 `log_P0_upper=1381`，即 `P0<=exp(1381)`。

审查说明：这仍是条件阈值。要把优化版升级为最终阈值，需在正文中证明 Vaughan 分块、矩形变差、除数系数三项总对数损失确实可取 `12` 或更低。下一步最优优化方向是专攻这三项的显式对数损失压缩，而不是继续压 OMR 常数。

## 86. exp(10) 目标的硬障碍与直接证书路线

本轮尝试把条件阈值压到 `exp(10)` 以下。敏感性分析显示：在当前渐近 C 区估计

`P^(11/12+ε) log^C P <= P/log^A P`

下，即使把内部总对数损失压到 0，只要 `A_star=2`，在 `logP<=100` 区间也无法通过该渐近不等式。因此 `exp(10)` 目标不能靠继续压 `C_vaughan_blocks,C_rect_variation,C_divisor_coeff` 实现；必须用小范围直接证书替代 C 区渐近门槛。

为此 `extract_p0.py` 新增开关：

- `use_direct_c_zone_certificate`
- `C_zone_direct_logP`

当该开关启用且 `logP<=C_zone_direct_logP` 时，脚本跳过 C 区渐近估计，表示该范围已经由独立直接证书覆盖。

条件测试文件：

`docs/explicit-p0-constants.structured-exp10-target.json`

取 `C_zone_direct_logP=10` 后，机器抽取得到：

`docs/explicit-p0-structured-exp10-target-result.json`

结果为 `log_P0_upper=3`，即理论入口低于 `exp(10)`。审查说明：这只是条件结果；要真正达到 `exp(10)` 以下，必须补上 C 区直接证书，证明所有 `logP<=10` 的 C 区情形已被有限验证或初等强估计覆盖。

## 87. exp(5) 有限验证目标证书

本轮将 exp(5) 目标落到可复核有限验证。新增脚本：

`experiments/verify_small_prime_square.py`

该脚本直接验证所有奇素数 `P<=floor(exp(5))=148` 的 `P×P` 方阵中，每一行和每一列都至少含一个素数。运行命令：

`python3 experiments/verify_small_prime_square.py --max-log 5 --out docs/finite-verify-exp5.json`

输出证书：

`docs/finite-verify-exp5.json`

验证结果：33 个奇素数全部通过；最差行素数数为 1，最差列素数数为 1，无失败样本。

随后建立 exp(5) 条件目标常数文件：

`docs/explicit-p0-constants.structured-exp5-target.json`

其中启用 `use_direct_c_zone_certificate=true` 且 `C_zone_direct_logP=5`。抽取结果：

`docs/explicit-p0-structured-exp5-target-result.json`

机器给出 `log_P0_upper=3`，即理论入口 `P0<=exp(3)`，低于 exp(5)。审查说明：该结论依赖结构路线常数候选；有限验证部分本身已覆盖 `P<=exp(5)` 的行列命题。

## 88. 候选常数逐项审查：不能直接定稿

本轮尝试把 `docs/explicit-p0-constants.structured-exp5-target.json` 中候选常数逐项落实到正文。严格审查后，结论是：当前不能诚实地把全部候选值标记为已证。原因是其中若干值是参数占位或乐观归一化，而正文尚未给出足够细的常数传递。

逐项状态如下。

**可直接支撑或已有明确来源的项：**

- `C_weil_completion=11664`, `A_weil_completion_log=4`：正文已有保守 Weil/完成和常数来源，可作为 NRC 的解析背景常数。
- `C_zone_direct_logP=5`：有限验证证书 `docs/finite-verify-exp5.json` 已覆盖 `P<=floor(exp(5))` 的行列命题。
- `C_OMR_model=16`：一维圆周模型计算可用远大于实际需要的保守常数覆盖。
- `C_collision_span=1`, `A_collision_span_log=2`：作为频率闭包账本的占位过于乐观；可证明的是存在某个显式 `C,A`，但未证明等于 `1,2`。

**仍需正文补强才能采用当前数值的项：**

- `C_vaughan_blocks=C_rect_variation=C_divisor_coeff=4`：这是阈值优化的主瓶颈。正文尚未证明三项总对数损失可压到 `12`；只能作为优化目标。
- `C_sieve=10`, `C_selberg_2linear=100`, `C_selberg_remainder=100`：需要从 Selberg 基本引理和筛余项中逐项推出，当前数值是候选。
- `tail_error_power=4`：需要尾界余项显式达到 `log^{-4}`；正文尚未完成对应尾界常数传递。
- `C_OMR_layer=1`, `C_OMR_projection=1`, `kappa_OMR=0.001`, `A_OMR_log=2`, `epsilon_OMR_power=20`：OMR/残差 LBE 到 Relative-ICR 的常数传递尚未逐项数值化。
- `C_CGTP=1`, `A_CGTP_log=2`, `C_LSMP=1`, `A_LSMP_log=2`：LSMP/CGTP 已条件闭合，但常数 `1,2` 尚未从 coarea、DPI、martingale 方差账本中推导。

因此，`exp(5)` 版本目前是“条件阈值 + 有限验证证书”，不是最终无条件定稿。下一步若要真正完成常数证明，应按优先级处理：

1. 先证明 `C_vaughan_blocks+C_rect_variation+C_divisor_coeff<=12` 或接受更大阈值；
2. 再显式化 `tail_error_power>=4`；
3. 再把 OMR/CGTP/LSMP 的 `1,2,0.001,20` 替换为由证明自然给出的保守数值；
4. 最后重跑 `extract_p0.py`，得到真正可审稿的 `P0`。

## 89. 保守结构常数包烟测

为避免使用过于乐观的 `1,2,0.001` 候选值，本轮构造了一个更保守的结构常数包：

`docs/explicit-p0-constants.structured-conservative.json`

其中结构账本取 `C_OMR_layer=C_OMR_projection=C_CGTP=C_LSMP=C_collision_span=16`，对数指数取 `8`，`kappa_OMR=0.0001`，`epsilon_OMR_power=64`，并把 `K_sieve_log_saving` 放宽到 `128`。同时保留 `C_zone_direct_logP=5` 的有限验证证书。

机器抽取结果：

`docs/explicit-p0-structured-conservative-result.json`

给出 `log_P0_upper=4`，即 `P0<=exp(4)`。这说明在 exp(5) 目标下，阈值对结构常数较不敏感；有限验证直接证书已经覆盖小范围，剩余关键不是继续调参，而是把保守常数包逐项从正文证明中推出。

当前诚实结论：尚不能宣称候选常数全部已证。可以把定稿目标从“证明乐观常数”改为“证明保守常数包”，因为该包仍保持 `P0<exp(5)`。

## 90. tail_error_power=4 的 Tail-log4 接口

本轮优先严写 `tail_error_power>=4`。正文新增 Tail-log4 接口：尾部专用 Selberg 权已有 `C_tail=1`，因此 `tail_error_power=4` 的证明义务归约为三个标准输入的 log4 版本：

1. `Reciprocal-window-large-sieve-log4`；
2. `Bilinear-prime-sieve-average-v2-log4`；
3. `Selberg-smoothing-remainder-log4`。

若低谱、中谱、平滑余项各自给出至少 `log^{-44}P` 的节省，并取保守 `K_sieve_log_saving=128`，则扣除内部账本后仍保留 `log^{-4}P` 尾部余量。因此保守常数包中的 `tail_error_power=4` 有明确充分条件。

审查状态：这比原先“候选值”更严格，但仍需在正文后续把上述三个 log4 标准输入逐项引用或证明。下一步优先严写 `Reciprocal-window-large-sieve-log4`，因为它主要由 NRC/Weil 完成和与窗口复杂度控制给出。

## 91. Reciprocal-window-large-sieve-log4

本轮继续严写 Tail-log4 的第一项：`Reciprocal-window-large-sieve-log4`。正文新增第 867a 节，取低谱窗口大筛 Lemma 867.1 的 `A=44`，并给出参数选择

`B_0=80`, `B_1=8`, `B_2=16`。

小 k 区由容量剥离给 `log^{-60}` 级余量；Vaaler 截断给 `log^{-16}`，非零 Fourier 模由 Lemma 867.1 给 `log^{-44}` 均方余量。合并 `r,h` 与窗口复杂度损失后，低谱尾部贡献满足

`T_tail,low(k) <= C_low V_D P/log^{44}P`。

该常数 `C_low` 并入保守常数包的 `C_sieve`，不新增抽取器字段。Tail-log4 的三项中，低谱项已数值化；剩余为 `Bilinear-prime-sieve-average-v2-log4` 与 `Selberg-smoothing-remainder-log4`。

## 92. Selberg-smoothing-remainder-log4

本轮严写 Tail-log4 的第二项：`Selberg-smoothing-remainder-log4`。正文新增第 867b 节，把平滑余项分为 Vaaler/Beurling 窗口截断与 Selberg divisor 谱端点平滑。

取 Fourier 截断高度 `H_F=log^{64}P`。Vaaler 逐点余项为 `O(H_F^{-1})`；尾部每个 q 只产生 `O(1)` 个 m，且 q 侧总数为 `O(P/logP)`，所以窗口截断余项为 `<=C V_D P/log^{65}P`。Selberg 端点余项由 `Σ_r |b_r|/r <= C V_D log^C P` 控制，扣除至多 `16` 个对数幂后仍保留 `log^{-44}P`。

因此

`T_tail,smooth(k) <= C_smooth V_D P/log^{44}P`。

常数 `C_smooth` 并入保守常数包的 `C_sieve`。Tail-log4 目前只剩第三项：`Bilinear-prime-sieve-average-v2-log4`。

## 93. Bilinear-prime-sieve-average-v2-log4 与 Tail-log4 三项闭合

本轮严写 Tail-log4 的第三项：`Bilinear-prime-sieve-average-v2-log4`。正文新增第 875a 节，在第 875 节中谱安全版基础上取

`B_m=80`, `η<=1/8`。

小模数层使用二维 Selberg 上筛，取 `u=100`，上筛基本引理余项 `e^{-u}` 可压过 `log^{-44}P`。大模数层使用 Lemma 874.1 的平均二元上筛；平均奇异级数截断、divisor 端点平均和 dyadic 分块总损失记为 `log^{32}P`，由中谱下界 `r>log^{80}P` 支付后仍保留 `log^{-48}P`，足以得到 `log^{-44}P`。

因此

`T_tail,mid(k) <= C_mid V_D P/log^{44}P`。

至此 Tail-log4 的三项均已严写：

1. `Reciprocal-window-large-sieve-log4`；
2. `Selberg-smoothing-remainder-log4`；
3. `Bilinear-prime-sieve-average-v2-log4`。

所以保守常数包中的 `tail_error_power=4` 已有完整条件链支撑。下一步应转向第二优先项：证明或放宽 `C_vaughan_blocks+C_rect_variation+C_divisor_coeff` 的总对数损失。

## 94. 三项内部对数损失的保守闭合

本轮严写 `C_vaughan_blocks,C_rect_variation,C_divisor_coeff` 的保守账本。正文新增第 908a 节，将三项解释为纯机械损失：

1. Vaughan/Heath--Brown dyadic 分块与 Type I/II 分类，取 `C_vaughan_blocks=10`；
2. 双曲约束矩形化、bounded-variation 权和 Abel 分部求和，取 `C_rect_variation=10`；
3. 固定阶 divisor-bounded 系数、Selberg divisor 谱端点，取 `C_divisor_coeff=10`。

因此总内部对数损失可保守取 `30`。这比优化候选总损失 `12` 更稳健。用保守结构常数包

`docs/explicit-p0-constants.structured-conservative.json`

重新抽取，细步长结果更新为

`docs/explicit-p0-structured-conservative-result.json`

给出 `log_P0_upper=3.5`，仍低于 `exp(5)`。因此 exp(5) 定稿路线不需要证明乐观的 `4+4+4`；证明保守的 `10+10+10` 已足够。

## 95. OMR/CGTP/LSMP 保守常数包显式账本

本轮严写结构常数包。正文新增第 1273 节，给出保守取值来源：

- `C_OMR_layer=16`：两次阈值截取、Fourier 截断、Cauchy 与安全因子；
- `C_OMR_projection=16`：方向扇区、父模型比较、DPI 并集选择；
- `C_OMR_model=16`：一维圆周模型的保守覆盖；
- `kappa_OMR=0.0001`：覆盖多步投影增量常数损失；
- `A_OMR_log=8`, `epsilon_OMR_power=64`：覆盖层数、方向扇区、平滑截断和额外误差吸收；
- `C_CGTP=16`, `A_CGTP_log=8`：martingale 能量、variance-to-density 和大小块分裂；
- `C_LSMP=16`, `A_LSMP_log=8`：方向筛选、离散 coarea、DPI；
- `C_collision_span=16`, `A_collision_span_log=8`：短深度低维频率 span 计数。

这些正是 `docs/explicit-p0-constants.structured-conservative.json` 中的结构常数。对数指数总和 `32<128=K_sieve_log_saving`，满足抽取器约束。保守包仍给 `P0<exp(5)`。

## 96. 最终覆盖状态：保守常数包 + exp(5) 有限验证

本轮新增正文第 1274 节，明确最终定稿状态以保守常数包为准。重新运行机械抽取与有限验证：

`python3 experiments/extract_p0.py --constants docs/explicit-p0-constants.structured-conservative.json --max-log 100 --step 0.1`

得到

`log_P0_upper=3.5`。

同时运行

`python3 experiments/verify_small_prime_square.py --max-log 5 --out docs/finite-verify-exp5.json`

得到 `P<=floor(exp(5))=148` 的 33 个奇素数全部通过，最差行/列素数数均为 1。

覆盖关系：理论证明覆盖 `P>exp(3.5)`；有限验证覆盖 `P<=exp(5)`；由于 `exp(3.5)<exp(5)`，两段重叠，覆盖所有奇素数。

最终机械证书文件：

- `docs/explicit-p0-constants.structured-conservative.json`；
- `docs/explicit-p0-structured-conservative-result.json`；
- `experiments/verify_small_prime_square.py`；
- `docs/finite-verify-exp5.json`。

审稿备注：早期状态文档中的“条件/候选/剩余”表述是历史探索记录；最终口径以第 90--96 节和正文第 1273--1274 节为准。

## 97. 理论入口降到 P=5 的测算

本轮新增 `extract_p0.py --min-log` 参数，用于真实测算 `logP<3` 的理论入口。对当前保守常数包重新扫描：

`python3 experiments/extract_p0.py --constants docs/explicit-p0-constants.structured-conservative.json --min-log 1.6 --max-log 10 --step 0.01`

得到理论入口约 `logP0=3.44`，即 `P0≈exp(3.44)`，不能直接降到 `P=5`。

瓶颈是 OMR 对数账本在极小 `logP` 下的余量。测试显示：若把 `epsilon_OMR_power` 从保守包的 `64` 提升到 `80`，可得

`docs/explicit-p0-constants.structured-p5-theory-test.json`

对应结果

`docs/explicit-p0-structured-p5-theory-test-result.json`

为 `logP0≈2.686`，仍大于 `log5≈1.609`。继续测试表明，要使理论入口达到 `P=5`，需要把 `epsilon_OMR_power` 提升到约 `200`。这只是条件测算，当前正文账本尚不能自然支持如此强的 OMR 余量。

进一步精细复测：用 `--min-log 1.6 --max-log 10 --step 0.001` 对保守包扫描，得到 `logP0≈3.438`。在 `P=5` 处，`loglog P≈0.4758849953`，当前 OMR 总损失为 `112`；若保持 `epsilon_OMR_power=64`，`P=5` 处允许的 OMR 损失仅约 `41.94`，还差约 `70.06`。等价地，若保持 OMR 总损失 `112` 不变，则需要 `epsilon_OMR_power>166.05`，整数上至少取 `167`，才能通过抽取器在 `P=5` 的判据。

结论：在当前保守可审查账本下，不建议把理论覆盖宣称为从 `P=5` 开始。最稳最终方案仍是：理论覆盖 `P>exp(3.5)`，有限验证覆盖 `P<=exp(5)`。若坚持理论入口 `P=5`，下一步必须专攻 OMR 余量账本：要么把 `epsilon_OMR_power` 从 `64` 严格提升到至少 `167`，要么把小 `P` 区间的 OMR 总损失从 `112` 严格压到 `41.94` 以下，或重写抽取器在小 `P` 区间的 OMR 判据。
