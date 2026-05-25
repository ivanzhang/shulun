# 外部定理引用索引

## 0. 用途

本索引用于把合著稿中所有外部深输入固定到可审稿对象，避免“引用某个标准定理”但未说明用途、变量和适用条件。

状态等级：

- `required`：当前主线必须使用；
- `optional-strong`：强于必要条件，可作备选；
- `legacy`：历史章节使用，主线不优先依赖；
- `warning`：不能替代当前硬点。

## 1. DI 谱 Kloosterman 大筛

- **来源**：Deshouillers, J.-M.; Iwaniec, H., *Kloosterman sums and Fourier coefficients of cusp forms*, Inventiones Mathematicae 70(2), 219--288, 1982, DOI `10.1007/BF01390728`.
- **状态**：`required` for external-theorem version.
- **用于**：`KLS-window` 的 Kloosterman 模数族与频率族平均抵消。
- **对应链条**：`DI => KLS-window => BE2-3K`.
- **必须核对**：
  - Kloosterman 相位与第 438 节相位一致；
  - 模数范围 `C≈P/log^{O(1)}P`；
  - 频率范围 `H<=P/log^{O(1)}P`；
  - 平滑截断可由 dyadic partition 实现；
  - 系数二范数/除数型界满足谱大筛假设。

## 2. BFI dispersion 与 well-factorable 权重

- **主来源**：Bombieri, E.; Friedlander, J. B.; Iwaniec, H., *Primes in Arithmetic Progressions to Large Moduli*, Acta Mathematica 156(3--4), 203--251, 1986, Theorem 10.
- **相关续篇**：Bombieri, E.; Friedlander, J. B.; Iwaniec, H., *Primes in Arithmetic Progressions to Large Moduli. II*, Mathematische Annalen 277(3), 361--393, 1987, DOI `10.1007/BF01458321`.
- **状态**：`required` for external-theorem version.
- **用于**：把 DI Kloosterman 平均接入 well-factorable Rosser/Buchstab 权重和 Dirichlet 多项式卷积。
- **对应链条**：`BFI + DI => KLS-window => WBE2`.
- **当前定位**：`BFI1986-Theorem10`，即 well-factorable 加权素数等差级数分布估计；Maynard
  `arXiv:2006.07088` 的 Theorem A 明确引用该结果为 `[BFI1, Theorem 10]`，其中 `BFI1`
  是 1986 年 Acta Mathematica 论文。旧标识 `BFI1987-Theorem10` 只保留为历史兼容别名，
  不再作为该 AP 定理的主来源。
- **必须核对**：
  - `lambda_d` 的 well-factorable level；
  - `E_2` 受限卷积是否落入 BFI 处理的 convolution/Dirichlet polynomial 框架；
  - 端点与平滑权损失是否为多对数；
  - `B(A)` 是否可吸收所有 dyadic、gcd、sawtooth 损失。

## 3. BV-E2 强版本

- **来源**：Bombieri--Vinogradov 型 `E_2` 序列平均分布，可由 BFI/dispersion 工具导出。
- **状态**：`optional-strong`.
- **用于**：直接推出 BMD 的充分条件。
- **为什么非最优**：BMD 实际只需固定类 `2 mod d` 与 well-factorable 权重的 `WBE2`，不需要 `max_a`。
- **必须核对**：
  - level `Q<=N^{1/2}/log^B N`；
  - 序列 `a_n` 为受限二素数卷积；
  - 模 `2` 已确定剥离，只处理奇平方自由模；
  - 误差强度 `N/log^A N` 足以除以 `|U_Y|≈N/log^2P`。

## 4. Vaughan / Heath-Brown 恒等式

- **来源**：标准解析数论素数权分解。
- **状态**：`required` for self-contained expansion, but hidden inside BFI if cited.
- **用于**：把素数权 `1_P(p)1_P(m)` 转换为 Type-I/Type-II 双线性形式。
- **必须核对**：
  - 截断参数；
  - 系数 divisor-bounded；
  - dyadic 分块数量；
  - Type-II 平衡块 `R,S≈P` 被覆盖。

## 5. Kuznetsov trace formula / spectral large sieve

- **来源**：DI 工具的谱理论底层。
- **状态**：`required only for fully self-contained no-black-box version`.
- **用于**：若不引用 DI，必须从这里重证 KLS-window。
- **必须核对**：
  - cusp forms、Eisenstein spectrum、Bessel transform；
  - Kloosterman sum normalization；
  - 大筛常数和权重平滑性；
  - 对本文窗口 `C,S,H` 的专门化。

## 6. Explicit formula

- **来源**：ζ 函数显式公式。
- **状态**：`required` in RH branch.
- **用于**：离线零点到素数计数异常入口。
- **必须核对**：
  - 平滑核；
  - 零点贡献；
  - 尾项；
  - 阈值和误差项；
  - controlled exits 是否真正覆盖异常。

## 7. BG / Baker 类输入

- **来源**：历史方阵/RH 局部估计中使用的解析数论输入。
- **状态**：`legacy` unless in current main theorem statement.
- **用于**：旧版本常数、阈值、局部指数和估计。
- **必须核对**：
  - 当前主线是否仍依赖；
  - 若依赖，精确版本和常数；
  - 若不依赖，移入历史注记。

## 8. 显式 Mertens/prime-count 常数包

- **来源**：Rosser, J. B.; Schoenfeld, L., *Approximate formulas for some functions of prime numbers*, Illinois Journal of Mathematics 6(1), 64--94, 1962.
- **状态**：`required` for `BPN-LHB` tail `P>=13208`.
- **用于**：把 `prime-matrix-bpn-low-hole-bucket-capacity-theorem.md` 中的连续乘积不等式
  \[
  H_{\max}(P)\prod_{13\le \ell\le P/5}\left(1-{1\over \ell}\right)
  \le \pi(P-1)-\pi(P/5)
  \]
  变成显式常数核查。
- **本文所需不等式**：
  - Corollary 1, formula `(3.5)`, p. 69: `pi(x) > x/log x` for `x>=17`，用于 `x=P-1` 的下界；
  - Corollary 1, formula `(3.6)`, p. 69: `pi(x) < 1.25506 x/log x` for `x>1`，用于 `x=floor(P/5)` 的上界；
  - Theorem 7, formula `(3.26)`, p. 70:
    `prod_{p<=x}(1-1/p) < e^{-gamma}(1+1/(2log^2 x))/log x` for `x>1`，并在 `x>=2641`
    时放宽为 `e^{-gamma}(1.03)/log x`。
- **范围核查**：`P>=13208` 时 `floor(P/5)>=2641`，所以 Mertens 放宽常数满足
  `1+1/(2log^2 floor(P/5))<1.009<1.03`；素数计数上下界的输入点均远大于
  `17`。因此 `prime-matrix-bpn-lhb-explicit-tail-constant-audit.md` 的
  `stable_from_in_scan=13208` 可作为外部定理版解析闭合阈值。
- **必须核对**：
  - 最终稿中把 `P/5` 的取整统一为 `floor(P/5)`；
  - 参考文献表使用标签 `RS1962`；
  - 若后续改用 Dusart 型更强常数，必须重新运行 `explicit-tail-constant-audit`。

## 8A. 经典 Backlund 缩进成本引理

- **来源**：
  - Backlund/Rosser--McCurley 方法的现代显式版本：Trudgian, T. S., *An improved upper bound for the argument of the Riemann zeta-function on the critical line II*, Journal of Number Theory 134, 280--292, 2014, arXiv `1208.5846`。
  - 显式 `S(T)` 上界与 Backlund 轮廓处理：Trudgian, T. S., *An improved upper bound for the argument of the Riemann zeta-function on the critical line*, Mathematics of Computation 81(278), 1053--1061, 2012, DOI `10.1090/S0025-5718-2011-02537-8`。
- **状态**：`optional-cross-check` for external-Backlund route; strictly self-contained
  Backlund analytic package is now closed by
  `BacklundSymmetricHeightMaxPremiumClosedByCommonHighHeightEnvelope`.
- **用于**：外部旁证路线中可把 `BacklundZeroProximityIndentationCostLedger` 替换为
  `ClassicalBacklundZeroIndentationCostExternalAccepted`，即接受经典 Backlund
  零点避让/缩进 convention 不额外产生本文 `C_S=8` 预算之外的正比例 jump 成本。
- **内部化后的精确微输入**：
  `BacklundSymmetricHeightMaxPremiumBelowC16MarginLedger`。当前文内已把经典
  Backlund 缩进成本压成高幂辅助函数
  `B_{T,theta,N}(z)=1/2(e^{-iNtheta}xi(z+iT)^N+e^{iNtheta}xi(z-iT)^N)`
  的对称高度 `max` 溢价不等式。新增共同高高度包络证明表明两个镜像分支共用同一
  `sigma` 分区点态包络，`T±4sin(phi)` 的高度差只进入 `O(1)`，因此对称
  `max` 的新增 `log(T+3)` 系数为 `0`；C16 分子仍为 signed-mean 的 `7`，
  小于 `16 log(4/sqrt(5))=9.305206478445...`。外部 Backlund 引理仍可作为旁证，
  但不再是本文 Backlund 解析包的必要输入。
- **对应链条**：
  `BacklundSymmetricHeightMaxPremiumBelowC16MarginLedger`
  `=> BacklundSymmetricHeightMaxPremiumClosedByCommonHighHeightEnvelope`
  `=> BacklundHighPowerAuxiliarySignedMeanC16AggregationClosedByCommonEnvelope`
  `=> ClassicalBacklundZeroIndentationCostInternalProofClosedByHighPowerCommonEnvelope`
  或引用
  `ClassicalBacklundZeroIndentationCostExternalAccepted`
  `=> BacklundCS8SlackAfterBridgeClosedTightHalf`
  `=> EndpointZeroAvoidanceMultiplicityConventionClosedByLimit`
  `=> RVMToCN16LocalInequalityClosedWithRawArgCS8`
  `=> DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。
- **必须核对**：
  - 外部定理使用的是原始 `arg zeta`/`S(T)` 归一化，不能把本文重标度后的 `C_N=16`
    反向代入 Backlund 证明；
  - 端点落零必须先取避零序列再取极限，零点按解析重数登记；
  - 缩进弧、水平边与右/左边界常数不能重复计费；
  - 引用只作为外部旁证，不关闭 `DStructure/Rankin` 独立验收门；
  - 严格自足 Backlund 解析包的当前证据文件为
    `docs/monograph/prime-matrix-backlund-common-envelope-internal-closure-router.md`。

## 8B. 有限 sqrt-gap 计算输入

- **来源**：Erdős, P. L.; Harcos, G.; Kharel, S. R.; Maga, P.; Mezei, T. R.; Toroczkai, Z.,
  *The sequence of prime gaps is graphic*, Mathematische Annalen 388, 2195--2215, 2024,
  Lemma 2.7, DOI `10.1007/s00208-023-02574-1`.
- **底层计算来源**：Oliveira e Silva, T.; Herzog, S.; Pardi, S.,
  *Empirical verification of the even Goldbach conjecture and computation of prime gaps up to*
  `4*10^18`, Mathematics of Computation 83, 2033--2060, 2014,
  DOI `10.1090/S0025-5718-2013-02787-1`.
- **状态**：`required-finite-bridge` for the finite strict-k Phi-LPF segment; not an infinite-tail theorem.
- **用于**：`Phi-LPF strict-k finite sqrt square-phase tail` 层。若 `x=kP` 且 `1<k<P`，
  则 `sqrt(x)<P`；外部 Lemma 2.7 的 `117<=x<=10^18` 区间素数存在性推出
  `N_P(k)=pi((k+1)P-1)-pi(kP)>=1`。
- **当前有限覆盖**：
  - `x<117` 的 strict 行由脚本直接核查；
  - `117<=kP<=10^18` 的 strict 行由有限 sqrt-gap 输入覆盖；
  - 顶行 `x=P^2-P` 因此覆盖到最大素数底 `P<=999999937`。
- **不能替代**：
  - 不能证明 `x>10^18` 的无限尾段；
  - 不能替代 `SquarePhaseTailLongBlockPDECExclusion`；
  - 不能替代真正的全局 `H(x)<=sqrt(x)` 短区间定理。

## 9. 不能误用的输入

| 输入 | 不能替代什么 | 原因 |
| --- | --- | --- |
| RC-Prime | BMD/WBE2 | 只给非空性，不给有符号分布 |
| 普通大筛 | BE2-3K/KLS-window | 平衡块差一个 `P` 量级 |
| 点态 Weil | KLS-window | 只给单模抵消，不给总平均 `log^{-A}` |
| 实验扫描 | 证明 | 只能作为常数与结构证据；无限尾段必须接显式外部不等式 |
| 完整 CRT 周期均衡 | 短窗口真实分布 | 短窗口不等于完整周期 |
| 外部 Backlund 缩进引理 | DStructure/Rankin 独立验收门 | 它只处理解析 `arg zeta` 缩进成本，不证明 Rankin 晋级包。 |
| Legendre 有限验证 | `k=P-1` 顶行正性 | Legendre 只保证 `((P-1)^2,P^2)` 内某处有素数；顶行需要更右侧的 `(P^2-P,P^2)`。 |
| Oppermann 猜想 | 无条件证明 | 完整 Oppermann 会关闭顶行左半窗和平方右半窗，但当前只能作为未证强输入或条件定理假设。 |
| BHP/Li 通用短区间指数 | 长度 `P` 的平方端点窗口 | 在 `X=P^2` 下分别给 `P^1.05`、`P^1.04` 级窗口，仍长于目标 `P`。 |
| 有限 sqrt-gap 计算输入 | 无限尾段 strict 行正性 | 它只覆盖 `kP<=10^18`，顶行只到素数底 `P<=999999937`。 |

## 10. 下一步核查任务

1. `docs/monograph/kls-window-di-bfi-adaptation-template.md` 已把 DI/BFI 到 KLS-window 的相位、模数、频率、逆元变量、权重、gcd 层、端点平滑和 `B(A)` 损失账本写成独立适配模板。
2. 在主稿中把“引用版闭合”和“完全自足版未闭合”继续分开定理化。
3. 把 Rosser--Schoenfeld 显式 Mertens/prime-count 常数写入主稿参考文献和定理模板。
4. 把共同包络内部闭合写入主稿解析输入表：外部 Backlund 保留为可接受旁证，自足路线采用
   `ClassicalBacklundZeroIndentationCostInternalProofClosedByHighPowerCommonEnvelope`。
5. 若投稿要求外部文献原文定理号，逐页核对 DI/BFI 与 Backlund 的对应定理编号；这属于书目精确化，不改变当前 H7 外部定理版逻辑链。

## 11. KLS-window 变量适配核查表

这是当前二点筛链条最需要继续压实的审稿表。只有该表逐项完成后，`DI+BFI=>KLS-window` 才能从“方向正确”升级为“引用适配充分”。

| 核查项 | 本文对象 | 外部定理对象 | 当前状态 | 补正动作 |
| --- | --- | --- | --- | --- |
| Kloosterman 相位 | `e(-2h \bar{s_1}\bar{d_2}/d_1-2h \bar{s_2}\bar{d_1}/d_2)` | DI/BFI 的逆元相位或 Kloosterman 和 | 待逐项归一化 | 写出从 CRT 相位到标准 `S(a,b;c)` 的换元 |
| 模数族 | `d,c≈P/log^{O(1)}P` | Kloosterman 模数/level | 方向匹配 | 核对外部定理允许的 dyadic level 与 well-factorable level |
| 频率族 | `0<|h|<=H`, `H<=P/log^{O(1)}P` | Fourier/Bessel 频率 | 方向匹配 | 给出 sawtooth 截断与 Bessel transform 的损失账本 |
| 逆元变量 | `s≈P`, `(s,d)=1` | Kloosterman 分子中的可逆类 | 方向匹配 | 核对 `beta_s` 的 divisor-bounded 与平滑分割条件 |
| 权重 | `lambda_d` Rosser/Buchstab well-factorable | BFI well-factorable weights | 方向匹配 | 明确 level 分解 `Q=Q_1Q_2` 后每层支持 |
| gcd 层 | `(d_1,d_2)=g` 强迫 `s_1≡s_2 mod g` | 非互素模数处理 | 已有多对数账本草案 | 写入主稿为 lemma，损失记入 `log^C P` |
| 端点和平滑 | dyadic、sawtooth、窗口边界 | 平滑权/partial summation | 待量化 | 建立 `B(A)` 吸收账本 |
| 目标强度 | `K<<N^2/(R log^A P)` | 任意对数节省 | 依赖外部定理 | 明确选择 `B=B(A)` 的顺序 |

## 12. 审稿级输出格式

主稿中建议把外部输入写为两层。

第一层是可引用定理：

`Theorem KLS-ext (DI/BFI).` 在第 10 节变量条件全部满足时，`KLS-window` 成立。

第二层是应用命题：

`Proposition.` `KLS-window=>BE2-3K=>BE2-3=>WBE2=>BMD`。

这样审稿人可以分别检查“外部定理是否可引用”和“引用后是否真的推出本文所需命题”，避免把两个问题混在一起。

## 13. H3-DSB-KLS 适配新增核查

新增 H3 单点尾块分支后，DI/BFI 的潜在用途不再只限二点筛 BMD。文件
`docs/monograph/prime-matrix-h3-dsb-kloosterman-window-reduction.md` 给出新的 Kloosterman 核：

```text
e(-h*rho(c)*bar(ell)/R(c)).
```

若要引用 DI/BFI 覆盖该 H3 分支，必须另行核验：

| 核查项 | H3-DSB 对象 | 当前风险 |
| --- | --- | --- |
| 模数 | `R(c)=lcm(r_-,r_+)<=y^2` | 可超过 `q`，需 high-lcm 分支 |
| 逆元变量 | `ell in (y,p]` | 与 DI 逆元变量方向匹配 |
| 互补窗口 | `J_ell=I/ell`, 长度 `<=q/ell` | 极短窗口，需平滑/端点账本 |
| 频率 | `1<=h<R(c)` | 高频尾需 Vaaler/sawtooth 吸收 |
| 权重 | `Lambda(m)` 与素数 `ell` | 需 Vaughan/Heath-Brown 或 BFI 权重 |
| 缺陷出口 | high-lcm/high-frequency/coefficient concentration | 必须分别路由，不能由 KLS 一句带过 |

新增 `docs/monograph/prime-matrix-h3-dsb-high-lcm-clamp-routing.md` 后，high-lcm 项已获得
独立路由：大质量高 `R(c)` 分支必稀疏化，并进入 `Persistent-HLC=>PDEC/ColumnCRT`
或 `Sparse-HLC=>SAE`。因此 DI/BFI 只应覆盖低 `R(c)` 的 `KLS-window` 主分支；
不能把 high-lcm 质量算入同一个外部定理输入。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-fourier-energy-clamp.md` 后，high-lcm
路由有了精确能量账本：同模块非零 Fourier 能量为 `R sum mu(a)^2-U^2`。该项不是
DI/BFI 输入，而是内部 CRT/Plancherel 恒等式；其后续排斥必须接入 `PDEC/ColumnCRT`
或 `SAE/endpoint`。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-pdec-threshold-bridge.md` 后，high-lcm
persistent 分支已经转成内部 PDEC 阈值 `L_HLC(B)`。DI/BFI 仍只覆盖低 `R` 的 KLS 主分支；
`U_CRT(B)<L_HLC(B)` 是 Prime Matrix 自身的 CRT/PDEC 证书义务，不应归入外部
Kloosterman 定理。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-pdec-failure-localization.md` 后，PDEC 上界
失败被内部 Fourier 凸性引理局部化为 Bohr-cap 集中；这也不是 DI/BFI 输入。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-bohr-cap-component-route.md` 后，Bohr-cap
组件分解同样是有限循环群几何，不属于外部 Kloosterman 定理输入。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-high-gcd-descent.md` 后，high-gcd 下降也是
内部有限 Fourier 恒等式；只有下降终点若落入低 `R` KLS-window，才可能再次调用 DI/BFI。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-short-arc-density-pressure.md` 后，short-arc
压力判据也是内部密度账本；外部 DI/BFI 只可能用于压力低残余进入低模 KLS-window 时。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-short-arc-pressure-optimizer.md` 后，外部输入
接口更明确：DI/BFI 若被使用，只能作用于 L2-flat residual 的 KLS-window 核验，而不是
用于证明 short-arc 压力公式本身。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-l2-flat-kls-admission.md` 后，H3-HLC 对外部
DI/BFI 的入口被限制为 K1--K6 全部通过后的 KLS-window；K4 由 L2 平坦性供给，其余条件
需逐项核验。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-clean-kls-reduction.md` 后，外部索引中的
H3-HLC 待核验项写为 `HLC-KLS-ext`：DI/BFI/Kuznetsov 是否覆盖 clean HLC 窗口对象
`(CKR-4)` 并给出 `O(q/log^2 y)` 或任意对数节省。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kls-external-adaptation.md` 后，该核验项已形成
外部深定理版适配表：

| 核查项 | H3-HLC 结论 |
| --- | --- |
| 相位 | `e(-h rho(c) bar(ell)/R(c))` 归一化为标准 `S(a,b;R)` 的逆元相位，`b=-h rho(c)` |
| 模数 | K1 与 high-lcm clamp 保证只把低有效模 dyadic level 交给 KLS |
| 频率 | K2 与 sawtooth 截断给出 `0<|h|<=H0` |
| 窗口 | K3 平滑 `J_ell=I/ell`，端点只付多对数损失 |
| 权重 | `Lambda(m)` 经 Vaughan/Heath-Brown 分解，`alpha_ell,beta_{c,h}` 由 K4 控制二范数 |
| gcd/unit | K5 把非单位和 gcd 层压为多对数损失 |
| 分块 | K6 保证 dyadic/tail-label 分块为多对数级 |

因此 H3-HLC clean branch 在允许引用 DI/BFI/Kuznetsov 窗口化 Kloosterman 输入时可标为
`external-theorem closed`。完全自足无黑箱版仍需在文内重证对应谱/dispersion 定理。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kls-core-reduction.md` 后，完全自足版的引用边界
进一步收窄为 `HLC-KLS-core`：

```text
windowed Kloosterman spectral/dispersion theorem
=> HLC-KLS-core (CORE-5)
=> HLC-KLS-ext (CKR-5)
=> clean HLC branch contradiction.
```

外部文献核对时应优先寻找能直接推出 `(CORE-5)` 的定理形式；若不能直接推出，则必须补
从外部定理到 `(CORE-5)` 的变量、权重、平滑和二范数转换。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kls-core-self-contained-spine.md` 后，外部引用
还可进一步按 `SC-9` 核验：外部定理若能直接给出本文窗口族上的
`Kuznetsov-LS atom (SC-9)`，则由该文件已证明的账本推出 `(CORE-5)`。若外部定理只给点态
Weil 或单模估计，则不够；文件第 7 节已记录其量级不足。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kuznetsov-ls-atom-expansion.md` 后，外部引用
可继续细分核验：若外部文献分别提供 KZ-B、KZ-C、KZ-D、KZ-E，则本文已有
`KZ-A--KZ-E=>SC-9` 的推导。若只提供 trace formula 而无 spectral large sieve 或
well-factorable dispersion，对数节省仍未闭合。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kz-c-bessel-transform-decay.md` 后，KZ-C 不再需要
外部引用；当时外部索引只需继续核对 KZ-B、KZ-D、KZ-E。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kz-d-spectral-large-sieve-spine.md` 后，KZ-D 的
外部核验点改为 `PTK-D`。外部谱大筛若能给出 diagonal `T^2` 和 off-diagonal `N0` 的
Schur 行列和上界，即可由该文件推出 KZ-D；否则还需补 pre-trace kernel 证明。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-ptk-d-pretrace-kernel-bound.md` 后，外部核验点
进一步改为 `LPC-D`。若外部几何/预迹估计能给出空间侧 row-column correlation bound，
则本文已有 `LPC-D=>PTK-D=>KZ-D`。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-lpc-d-spatial-correlation-split.md` 后，外部核验点
进一步改为 `GHLC-D`。任何外部或内部几何计数若给出 generic hyperbolic local correlation
的 Schur 行列和，即可接回 `GHLC-D=>LPC-D=>PTK-D`。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-ghlc-d-local-schur-closure.md` 后，GHLC-D 已由
局部积分核质量闭合，不再需要外部几何计数。KZ-D 分支随之闭合；外部索引对 H3-HLC 完全
自足版的剩余核验点缩为：

```text
KZ-B: specialized Kuznetsov trace formula;
KZ-E: BFI/well-factorable dispersion logarithmic saving.
```

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kz-b-kuznetsov-trace-specialization.md` 后，KZ-B
也不再需要外部引用。该文件只使用 Poincare unfolding、双陪集分解和谱 Plancherel 来推出
本文需要的 trace formula 专门化。外部索引对 H3-HLC 完全自足版的剩余核验点现在只有：

```text
KZ-E: BFI/well-factorable dispersion logarithmic saving.
```

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kz-e-well-factorable-dispersion-spine.md` 后，KZ-E
本身被压缩为 `WFD-core`。外部索引现在只需核验 DI/BFI 是否直接提供该窗口化
well-factorable Kloosterman dispersion 平均估计；完全自足版则必须在文内证明：

```text
WFD-core: windowed well-factorable Kloosterman dispersion mean estimate.
```

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-wfd-core-balanced-factor-reduction.md` 后，外部核验
点进一步缩为：

```text
BWFD-core: balanced two-modulus well-factorable Kloosterman dispersion mean estimate.
```

DI/BFI 若要作为外部定理使用，必须覆盖该平方根双模数窗口，而不仅是单模 Kloosterman
点态估计。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-bwfd-core-spectral-completion-attack.md` 后，外部核验
点进一步缩为：

```text
BSC-core: balanced complete Kloosterman bilinear correlation logarithmic saving.
```

外部 DI/BFI 适配若要闭合该点，必须在完成 Kloosterman 形 `(BSA-9)` 上给出任意 `log^{-A}`
节省，并覆盖同一全局 `\beta_s` 诱导的 Fourier 系数族 `(BSA-4)`；只给普通 spectral large
sieve 或点态 Weil bound 不足。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-bsc-core-kloosterman-fraction-attack.md` 后，外部核验
点进一步缩为：

```text
KFLS-core: balanced Kloosterman-fraction large sieve logarithmic saving.
```

外部 DI/BFI 若要匹配该点，必须能覆盖相位
`e(\bar vR/u+\bar uT/v)` 的平衡双模数平均，并处理退化二次同余层的 gcd/divisor 账本。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kfls-core-square-kernel-attack.md` 后，外部核验点
进一步缩为：

```text
CFQK-core: centered four-modulus Kloosterman-fraction correlation saving.
```

外部定理若要覆盖该点，必须提供中心化四模数相关的对数节省，而不能只给全核绝对 Schur；
后者被精确对角层阻断。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-cfqk-core-block-centering-attack.md` 后，外部核验点
进一步修正为：

```text
BD-CEN + OSQK-core + TFQK-core.
```

外部定理若要匹配该点，必须说明是否已扣除同 `(u,v)` 块局部方差；若没有该中心化，单靠
Kloosterman 平均估计不能越过块对角障碍。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-bd-cen-dispersion-centering-audit.md` 后，外部核验点
优先级更新：必须先核对外部 DI/BFI dispersion 定理是否在进入 Kloosterman 平均前已经扣除
同块局部方差，即是否提供 `(BDC-5)`。若外部定理只陈述非零 Fourier 频率或普通方差式，
不能自动视为 `BD-CEN`。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-bd-cen-no-go-route-fork.md` 后，外部引用路线的重要性
进一步明确：当前内部对象不满足 `BD-CEN`。若使用外部 DI/BFI，必须直接引用其原始 dispersion
结论，而不是把本文当前平方核中心化误认为已经自足证明。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-source-cen-no-go.md` 与
`docs/monograph/prime-matrix-h3-dsb-hlc-blk-energy-core-obstruction.md` 后，外部引用接口再收紧：
`SOURCE-CEN` 不能免费改变当前 WFD 对象；裸 `BLK-energy-core` 也不能作为平方核层任意
系数数组定理成立。若外部 DI/BFI 用于 H3-HLC/KZ-E，必须直接提供以下二者之一：

```text
original dispersion estimate for the uncentered WFD target,
or a theorem implying NC-BLK block non-concentration for the actual WFD coefficients.
```

只给普通跨块 Kloosterman 平均而未处理同 `(u,v)` 块能量的外部定理，不能闭合当前接口。

新增 `experiments/prime_matrix_triad_a1_generic_wfd_dibfi_router.py` 后，A1 的 generic noncanonical
WFD 外部接口已从“引用 DI/BFI 原始 dispersion”压缩为以下单点：

```text
DIBFIOriginalDispersionTheoremLocationAndHypothesisMatch.
```

外部引用版现在需要最终补齐：

1. 精确指出 DI/BFI 原文或现代等价版本中的 theorem/proposition/page；
2. 逐条核对该定理是否估计未中心化的原始 WFD 目标，而不是事后插入 SOURCE-CEN/BD-CEN；
3. 核对 Kloosterman 逆元相位、well-factorable level、Type-I/II 双变量范围、gcd/unit 层、
   dyadic/平滑端点和任意 `log^{-A}` 节省是否全部匹配；
4. 若外部定理只给中心化、跨块或不同权重的版本，必须另写转移引理，不能直接标记为闭合。

因此当前外部定理索引的最新任务不是再寻找新的内部 canonical support，而是完成 DI/BFI 原始
dispersion 的精确引用定位与假设对账。

新增 `experiments/prime_matrix_triad_a1_dibfi_theorem_location_router.py` 后，定理定位部分已从该
单点中剥离：

```text
BFI1986-Theorem10:
  Bombieri--Friedlander--Iwaniec, Acta Math. 156(3--4), 203--251, 1986;

BFI1987-Theorem10:
  historical compatibility alias only; do not use as the primary location for the
  well-factorable AP Theorem 10 unless the exact theorem statement is separately checked;

DI1982-Theorem12:
  Deshouillers--Iwaniec, Invent. Math. 70, 219--288, 1982,
  DOI 10.1007/BF01390728;

Maynard2020-CrossCheck:
  arXiv:2006.07088 quotes BFI Theorem 10 and DI Theorem 12.
```

因此最新外部剩余改为：

```text
DIBFIOriginalDispersionCurrentWindowHypothesisMatch.
```

也就是说，下一步不再是寻找定理号，而是把当前未中心化 `KE-13/WFD-core` 窗口逐项放进
`BFI1986-Theorem10 + DI1982-Theorem12` 的假设中。

## Landau-Page 例外零唯一性输入

行/列命题的 `SquareScaleQuadraticBetaGapAndZeroPacketResidualBudgetAtP2`
接口新增一个外部输入名：

```text
LandauPageExceptionalZeroUniquenessWithAdaptedConstants
```

所需内容是标准 Page/Landau 例外零唯一性形态：对导子 `q<=Q` 的 primitive 实角色，
在区域

```text
beta > 1 - c_Page/log Q
```

内至多存在一个例外实零载体。当前仓库只使用它来排除“同一 `Q` 范围中出现多个
`beta>1-C/P` 超近实零载体”的固定周期/正密度 CRT 复现形态。

边界：

1. 本仓库尚未内化 `c_Page` 的显式常数，也未把该常数适配到 `P^2` 高区间二次角色投影预算。
2. Page 稀疏性只能排除多载体族，不能排除每个尺度一个的 moving singleton 例外载体。
3. 该输入不处理非实零包、端点项或素数幂残差的同向相干。

因此它只能把当前最窄口压成

```text
PageExceptionalSingletonCarrierOrNonrealZeroPacketResidualBudget
```

不能单独闭合行/列命题。

## Full-S non-AP WFD theorem-match 矩阵

新增机器证书：

```text
experiments/prime_matrix_fulls_nonap_wfd_theorem_match_matrix_router.py
data/prime-matrix-fulls-nonap-wfd-theorem-match-matrix-ledger.json
docs/monograph/prime-matrix-fulls-nonap-wfd-theorem-match-matrix-router.md
docs/monograph/prime-matrix-fulls-nonap-wfd-theorem-match-matrix-router.json
```

本证书把 `H_P`/full-S 外部解析输入固定为逐项 theorem-match，而不是引用名称。当前目标对象为：

```text
W_full(C,S,H)=sum_{c~C} lambda_c sum_{0<|h|<=H} omega_h
              sum_{s~S,(s,c)=1} beta_s e_c(a_h s + b_h bar{s})
X≈P^2, C≈P/log^O P, S≈P, H<=P/log^O P
boundary=non-AP, uncentered, no hidden projection, no AP-source lift
required_strength=NaturalWFDScale/log^A P for every A>0
```

逐项核查列为：

```text
object, weights, window, moduli, smoothing_projection, saving_strength, conclusion
```

当前判定：

1. BHP/Li 普通短区间输入不匹配 full-S WFD 对象，且 `theta>1/2` 不覆盖 `x≈P^2` 的长度 `P≈sqrt(x)` 顶端带。
2. Friedlander-Iwaniec 只作为 parity-breaking 技术范型；其 `x^2+y^4` 特殊对象不等于当前 full-S non-AP WFD 窗口。
3. BFI AP 定理只有在另证 `APSourceLift` 后才可用；它本身不是未中心化、无投影的 non-AP WFD 结论。
4. DI/Kuznetsov 谱工具在相位/模数/频率上部分匹配，但尚未给出当前 `c`-dependent completed weights 的 ready-made corollary。
5. Maynard/GPY 的结论类型与每个 `sqrt` 窗非空性不匹配；仓库已有 Maynard-S compression no-go。
6. `FullS-KLS-ext` 与当前对象逐项匹配，但只能作为新的外部黑箱合同，不能登记为已由 DI/BFI 原文推出。
7. 新自守/dispersion 证明路线对象匹配，但仍缺任意 `log^{-A}` 节省和最终结论。

因此最新外部输入纪律为：

```text
ReadyMadePrimarySourceMatchFound=false
PrimarySourceDerivationClosed=false
UnconditionalHPClosureReached=false
```

真正剩余是：

```text
FullSNonAPWFDKLSTheoremInput
OR APSourceLift
OR NCBLKActualBlockNonConcentration
```

任何 FI/DI/BFI/Maynard/自守 L 函数方向的后续推进，都必须先填满上述七列，而不能只登记为“标准深定理可用”。

## Full-S theorem-match 后的真剩余切割

新增机器证书：

```text
experiments/prime_matrix_fulls_theorem_match_true_remainder_cut_router.py
data/prime-matrix-fulls-theorem-match-true-remainder-cut-ledger.json
docs/monograph/prime-matrix-fulls-theorem-match-true-remainder-cut-router.md
docs/monograph/prime-matrix-fulls-theorem-match-true-remainder-cut-router.json
```

该证书把 theorem-match 矩阵的三口结果进一步切成真正可攻的输入基：

```text
(ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch
 OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

外部黑箱条件版为：

```text
AcceptedFullSKLSExt
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

切割规则：

1. `APSourceLift` 已被 no-go 证书过滤；它不能作为当前 non-AP、未中心化、无投影对象的活动外部引用路线。
2. `NCBLKActualBlockNonConcentration` 不再作为黑箱终端保留；它展开为 actual noncanonical full-S 源的支撑/容量核心。
3. generic full-S WFD 反原子被 moving-delta 模型反证，不能作为自足证明。
4. `FullS-KLS-ext` 可以作为外部黑箱合同，但仍不是 DI/BFI/Maynard 主来源逐项推出的结论。

因此，后续外部定理核查有两条合法任务：

- 精确证明或引用 `ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch`；
- 或完全避开外部谱定理，直接证明 `ActualNoncanonicalFullSFactorSupportCapacityTheoremInput`。

两者都不能省略最终的 `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` 晋级验收。

## 外部引理版 / 内部自足版双闭合边界

新增机器证书：

```text
experiments/prime_matrix_dual_closure_external_internal_hardpoint_router.py
data/prime-matrix-dual-closure-external-internal-hardpoint-ledger.json
docs/monograph/prime-matrix-dual-closure-external-internal-hardpoint-router.md
docs/monograph/prime-matrix-dual-closure-external-internal-hardpoint-router.json
```

该证书把“外部引理版”和“内部自足版”分开登记，避免把条件闭合误读为无条件闭合。

外部引理版的严格闭合包为：

```text
AcceptedFullSKLSExtExternalContract
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

在这个包被接受时，外部引理版的反例链无剩余数学出口。但当前语料库尚未独立接受最终
DStructure/Tail-log4/finite Rankin 晋级包，所以它仍不是当前仓库的无条件定理。

无黑箱外部主来源版仍需：

```text
ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch
OR NewAutomorphicDispersionProof
```

内部自足版的高层硬点为：

```text
ActualNoncanonicalCleanCoreMovingAtomExclusion
AND SelfContainedDStructureTailLog4FiniteRankinProofPackage
```

继续展开 source 侧后，当前最实在的 signed-source 表输入为：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger
AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
AND PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward
AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
AND PrimitiveRowSupportLowerBoundBeforeExactUVProjectionLedger
AND RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger
AND FixedKeyExactUVLocalMultiplicityO1Ledger
```

Phi-LPF/LPF 端点差公式继续保留为精确计数和有限审计工具，但不作为短区间正性的外部引理。

## 15. `1<k<P` 端点差修正后的外部输入边界

新增机器证书：

```text
experiments/prime_matrix_k_less_p_endpoint_correction_author_residue_router.py
data/prime-matrix-k-less-p-endpoint-correction-author-residue-ledger.json
docs/monograph/prime-matrix-k-less-p-endpoint-correction-author-residue-router.md
docs/monograph/prime-matrix-k-less-p-endpoint-correction-author-residue-router.json
```

该证书修正一个容易误用的边界：`P=5,k=8166` 的 CRT 全合数样本满足 `k>P`，所以不能
用于否定 restricted row 目标 `1<k<P`。对 restricted row，Phi-LPF 端点差已经给出精确
计数，且闭区间端点不贡献素数；但正性仍等价于 strict row 内存在 full-root 未覆盖槽。

因此外部输入边界保持为：

```text
ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch
OR NewAutomorphicDispersionProof
OR SpecialSquarePhaseStructuralLowerBoundBeyondParity
```

外部引理版若使用 `AcceptedFullSKLSExtExternalContract`，仍必须同时保留最终晋级门：

```text
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

内部自足版不得把 restricted Phi-LPF 端点差当作正性黑箱；它必须提交 signed-source 细包和
`SelfContainedDStructureTailLog4FiniteRankinProofPackage`。

## 16. 两条替代线的外部主来源与内部 RKS-log 边界

新增机器证书：

```text
experiments/prime_matrix_two_replacement_lines_terminal_attack_router.py
data/prime-matrix-two-replacement-lines-terminal-attack-ledger.json
docs/monograph/prime-matrix-two-replacement-lines-terminal-attack-router.md
docs/monograph/prime-matrix-two-replacement-lines-terminal-attack-router.json
```

本证书把 FI/DI/BFI/Maynard/自守 L 函数方向重新登记为逐项 theorem-match，而不是名称引用。
外部无黑箱线的目标对象为：

```text
W_full(C,S,H), C≈P/log^O(P), S≈P, H<=P/log^O(P),
well-factorable lambda_c, divisor-bounded beta_s, smooth omega_h,
c-dependent completed residue weights,
non-AP, uncentered, no hidden projection, no AP-source lift,
NaturalWFDScale/log^A(P) saving for every fixed A.
```

当前判定：

1. BFI 1986 Theorem 10 和 Maynard 后续大模数结果属于 AP / well-factorable residue-class
   分布；没有 APSourceLift 时不能直接覆盖 full-S non-AP WFD。
2. DI/Kuznetsov 谱大筛是新证明的核心技术模板，但它从完成后的 Kloosterman 平均和给定系数
   出发；`c`-dependent completed weights、无投影 de-completion 和 arbitrary `log^{-A}`
   保存仍未逐项证明。
3. FI parity-breaking 可作为 Type-II/奇偶屏障突破的技术范型，但不是当前 `W_full` 的直接定理。
4. 因此外部无黑箱线仍为：

```text
ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch
OR NewAutomorphicDispersionProof
```

内部自足线的 DStructure/Rankin 替代包被压到 Tail-log4/RKS-log 解析原子：

```text
SelfContainedTailLog4RKSLogReciprocalKloostermanFixedSaving
```

其目标是 prime modulus 下倒数 Kloosterman 双/多线性固定对数节省，覆盖 RKS/BG 低谱账本所需的
`e_P(xi/(mn))` 相位与 Vaughan/RKS divisor-bounded 系数。Baker 单频率素变量估计不能替代该
coherent frequency average。

## 17. RNRS 回填后的 completed KLS 与 ExactUV 边界

新增机器证书：

```text
experiments/prime_matrix_two_replacement_lines_after_rnrs_exactuv_sync_router.py
data/prime-matrix-two-replacement-lines-after-rnrs-exactuv-sync-ledger.json
docs/monograph/prime-matrix-two-replacement-lines-after-rnrs-exactuv-sync-router.md
docs/monograph/prime-matrix-two-replacement-lines-after-rnrs-exactuv-sync-router.json
```

本证书同步了一个重要边界：RKS-log/RNRS 作者侧解析输入已经由仓库后续证书闭合，因此内部
自足线的最新 hardpoint 不再是 BG/RKS-log，而是 ExactUV/source entropy。外部无黑箱线的
标准形也进一步固定为：

```text
ModulusDependentCompletedFullSKLSInput
OR ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch
OR NewAutomorphicDispersionProof
```

这里的 `ModulusDependentCompletedFullSKLSInput` 必须保留以下项目：

1. full-S non-AP WFD 完成型对象；
2. `c`-dependent completed residue weights；
3. well-factorable modulus weights；
4. 不退回 APSourceLift 或 AP discrepancy；
5. 无中心化/投影隐藏损失；
6. de-completion 与端点误差保存；
7. 任意固定 `log^{-A}` 节省，并能穿过下游 loss ledger。

内部自足线同步为：

```text
ExactCleanCoreFullSNonAPWFDSourceEntropy
ActualNoncanonicalExactUVSupportLowerBound
CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn
```

因此后续若继续走 FI/DI/BFI/Maynard/自守 L 函数路线，应优先尝试证明 completed KLS 标准形；
若走内部路线，应优先证明 clean-core exact 层承认、非零转移和 thin-return，而不是继续重攻
已经由 RNRS 回填的 RKS-log。

## 18. exact-layer/completed-KLS 深攻后的外部输入边界

新增机器证书：

```text
experiments/prime_matrix_two_replacement_lines_exact_layer_completed_kls_attack_router.py
data/prime-matrix-two-replacement-lines-exact-layer-completed-kls-attack-ledger.json
docs/monograph/prime-matrix-two-replacement-lines-exact-layer-completed-kls-attack-router.md
docs/monograph/prime-matrix-two-replacement-lines-exact-layer-completed-kls-attack-router.json
```

外部无黑箱线现在应写成如下精确审稿对象：

```text
CDependentResidueWeightSpectralCancellationInput
```

该对象不是普通 DI、BFI、FI 或 Maynard 定理名称的直接替换。它必须逐项匹配：

| 核查项 | 本文对象 | 必须保持的条件 |
| --- | --- | --- |
| 完成后权重 | `B_{c,x}=sum_k beta_{x+k c}` | 允许依赖模数 `c`，不得假设 residue 平坦或已中心化 |
| 模数/频率平均 | well-factorable `lambda_c` 与 smooth `omega_h` | 谱/dispersion 平均必须同时作用在 `c,h` 族上 |
| 目标对象 | full-S non-AP WFD | 不得退回 APSourceLift、AP discrepancy 或投影中心化目标 |
| 误差账本 | gcd、smoothing、endpoint、de-completion | 必须全部进入 `B(A)`，并保留下游 loss ledger |
| 强度 | `NaturalWFDScale/log^A(P)` | 对每个固定 `A>0` 有可选择的参数余量 |

若外部文献不能直接给出这一 completed、模数依赖、no-projection 版本，则外部无黑箱版仍只能写为：

```text
CDependentResidueWeightSpectralCancellationInput
OR ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch
OR NewAutomorphicDispersionProof
```

外部引理版可以继续使用 `AcceptedFullSKLSExtExternalContract`，但必须保留
`DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`；这不是作者侧可自行删除的数学输入。

## 19. 两条替代线深终端同步后的外部输入边界

新增机器证书：

```text
experiments/prime_matrix_two_replacement_lines_deep_terminal_sync_router.py
data/prime-matrix-two-replacement-lines-deep-terminal-sync-ledger.json
docs/monograph/prime-matrix-two-replacement-lines-deep-terminal-sync-router.md
docs/monograph/prime-matrix-two-replacement-lines-deep-terminal-sync-router.json
```

深同步后的无黑箱外部线不再停在旧的 `CDependentResidueWeightSpectralCancellationInput`
标签。若不把该输入作为外部定理接受，它经有限 Fourier/BWFD/BSC/KFLS 进入
`NCBLKActualBlockNonConcentrationOrExternalDIBFI`，再对齐到 exact source entropy、
support/capacity package 与 source anti-atom。由于 generic self-contained anti-atom
已被 moving-delta 模型反证，真正非循环外部目标固定为：

```text
ExternalDIBFIKuznetsovDispersionTheoremMatch
```

该 theorem-match 仍必须保持 section 18 的全部对象条件：full-S non-AP WFD、`c`-dependent
completed residue weights、well-factorable `lambda_c`、smooth `omega_h`、无 APSourceLift、
无中心化/投影偷渡、de-completion 与端点误差预算，以及任意固定 `log^{-A}` 节省。

外部引理版仍只在接受

```text
AcceptedFullSKLSExtExternalContract
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

时条件闭合；无黑箱外部版仍未闭合。

## 20. 最新真剩余同步后的外部输入边界

新增机器证书：

```text
experiments/prime_matrix_two_replacement_lines_latest_true_remainder_sync_router.py
data/prime-matrix-two-replacement-lines-latest-true-remainder-sync-ledger.json
docs/monograph/prime-matrix-two-replacement-lines-latest-true-remainder-sync-router.md
docs/monograph/prime-matrix-two-replacement-lines-latest-true-remainder-sync-router.json
```

本层把上一节的 `ExternalDIBFIKuznetsovDispersionTheoremMatch` 继续替换为可审稿的真剩余。
`prime-matrix-fulls-nonap-wfd-theorem-match-matrix-router` 已经逐项筛查普通短区间、FI、
BFI、DI/Kuznetsov、Maynard 与 FullS-KLS-ext；`prime-matrix-fulls-theorem-match-true-remainder-cut-router`
进一步删除 `APSourceLift` 与 generic source anti-atom。无黑箱外部版因此不是“再引用
DI/BFI/Kuznetsov 名称”，而是：

```text
(ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch
 OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput
 OR NewAutomorphicDispersionProof)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

外部引理版仍只在接受如下完整包时条件闭合：

```text
AcceptedFullSKLSExtExternalContract
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

该条件闭合不等于从 DI/BFI 主来源逐行推出，也不删除 DStructure/Rankin 独立验收门。若要
改写成无黑箱主来源版，必须逐项证明同一个 completed full-S non-AP WFD 对象、`c`-dependent
completed residue weights、well-factorable `lambda_c`、smooth `omega_h`、无 AP-source lift、
无中心化/投影偷渡、de-completion 与端点误差预算，以及任意固定 `log^{-A}` 节省。

## 21. 原子化硬包后的外部/条件边界

新增机器证书：

```text
experiments/prime_matrix_two_replacement_lines_atomized_hard_package_router.py
data/prime-matrix-two-replacement-lines-atomized-hard-package-ledger.json
docs/monograph/prime-matrix-two-replacement-lines-atomized-hard-package-router.md
docs/monograph/prime-matrix-two-replacement-lines-atomized-hard-package-router.json
```

本层没有改变外部输入的基本边界，但把内部 hard package 的若干尾段子原子继续压窄。外部线仍为：

```text
((AcceptedFullSKLSExtExternalContract)
 OR ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch
 OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput
 OR NewAutomorphicDispersionProof)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

其中 `AcceptedFullSKLSExtExternalContract` 是条件外部引理版；若走无黑箱版，仍需
`ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch`、actual source support/capacity 新定理，
或新的自守/dispersion 证明。内部的 beta-sieve 和 sawtooth 原子化不能替代该外部 theorem-match，
也不能删除 DStructure/Rankin 独立验收门。

## 22. B=3 离散误差深同步后的外部/自足边界

新增机器证书：

```text
experiments/prime_matrix_two_replacement_lines_b3_deep_sync_router.py
data/prime-matrix-two-replacement-lines-b3-deep-sync-ledger.json
docs/monograph/prime-matrix-two-replacement-lines-b3-deep-sync-router.md
docs/monograph/prime-matrix-two-replacement-lines-b3-deep-sync-router.json
```

本层只替换内部 beta-sieve 的粗原子
`B3DiscretePrimeSumUniformErrorPGe100000`。仓库已有的 B=3 深层链说明：
离散素和误差先压成 Stieltjes prime-word 账本与交错边界余项；prime-harmonic/Mertens
包络再压成有限阶梯与显式 reciprocal-prime Mertens 尾段；接受 Dusart/Rosser-Schoenfeld
型外部显式定理后，20000 锚点与 delay-kernel BV 乘子把 B=3 边界变差的一百分点预算关闭。
因此外部 Mertens 版的 B=3 分支已经到：

```text
(DusartPrimeReciprocalMertensEnvelopeXGe286ExternalAccepted
 AND B3RosserFaceDictionaryClosedAlpha043
 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

这仍不是无条件闭合，因为最后一项仍是独立验收门。若坚持完全自足，则不能引用
Dusart 尾段，必须内联：

```text
SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000
AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000
```

外部无黑箱主线仍保持上一节的 FullS-KLS/no-projection theorem-match 边界；B=3
Mertens 同步只缩小内部 beta-sieve 子包，不替代 FullS theorem-match、source-root、
PDEC/CleanKLS 或 DStructure/Rankin。

## 23. Rate-bearing Mertens 尾段闭合同步后的两线边界

新增机器证书：

```text
experiments/prime_matrix_two_replacement_lines_rate_tail_mertens_closed_sync_router.py
data/prime-matrix-two-replacement-lines-rate-tail-mertens-closed-sync-ledger.json
docs/monograph/prime-matrix-two-replacement-lines-rate-tail-mertens-closed-sync-router.md
docs/monograph/prime-matrix-two-replacement-lines-rate-tail-mertens-closed-sync-router.json
```

后续 strict rate-bearing Mertens 同步表明，直接内部 Dusart theta/PNT 包络、
非平滑 Perron 常数层与 Meissel-Mertens B1 区间均已由自足证书导入；因此
`SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000` 和
`SelfContainedMeisselMertensConstantIntervalLedgerAt20000` 不再是两条替代线的活动硬点。

外部线不变：

```text
((AcceptedFullSKLSExtExternalContract)
 OR ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch
 OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput
 OR NewAutomorphicDispersionProof)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

内部线压缩为：

```text
source-root / terminal alternative
AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet
AND RatePreservationLedger_FOR_moving_atom_packet
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

这一步只删除解析尾段旧硬点；它不替代 FullS theorem-match，也不产生 DStructure/Rankin
独立验收事件。

## 24. Source-root/no-cycle 同步后的两线边界

新增机器证书：

```text
experiments/prime_matrix_two_replacement_lines_source_root_nocycle_sync_router.py
data/prime-matrix-two-replacement-lines-source-root-nocycle-sync-ledger.json
docs/monograph/prime-matrix-two-replacement-lines-source-root-nocycle-sync-router.md
docs/monograph/prime-matrix-two-replacement-lines-source-root-nocycle-sync-router.json
```

本层把上一节内部线中保留的 `source-root / terminal alternative`
继续同步到已有 strict source-root 终端环、direct PDEC scope 饱和、
KZ no-cycle 与 KZ-E source-bridge 证书。结论是：
`ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn` 不应继续作为
两条替代线的活动证明原子。内部自足线的 source-root 支路被替换为：

```text
A1CleanBranchCanonicalSourceAdmission
OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
```

并仍需携带：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet
AND RatePreservationLedger_FOR_moving_atom_packet
AND (DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
     OR SelfContainedDStructureTailLog4FiniteRankinProofPackage)
```

外部引理版的条件闭合口径保持为：

```text
AcceptedFullSKLSExtExternalContract
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

无黑箱外部版仍需：

```text
(ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch
 OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput
 OR NewAutomorphicDispersionProof)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

因此 FI/DI/BFI/Kuznetsov/Maynard 只能作为待匹配来源方向，不能只按名称引用。
必须逐项匹配同一个 completed full-S non-AP WFD 对象、权重、窗口、模数范围、
投影限制、de-completion 与端点误差预算，以及所需的固定 `log^{-A}` 节省。

## 25. A1 source-admission 吸收后的两线边界

新增机器证书：

```text
experiments/prime_matrix_two_replacement_lines_source_admission_absorption_sync_router.py
data/prime-matrix-two-replacement-lines-source-admission-absorption-sync-ledger.json
docs/monograph/prime-matrix-two-replacement-lines-source-admission-absorption-sync-router.md
docs/monograph/prime-matrix-two-replacement-lines-source-admission-absorption-sync-router.json
```

本层把上一节内部线中的 `A1CleanBranchCanonicalSourceAdmission` 继续同步到
strict source-admission branch absorption 与 post-source-admission macrocycle。A1 准入
是 scoped 分支陈述：canonical RIW/Buchstab 分支可内部处理，但 generic/noncanonical
分支仍必须外部化或回流。把它作为独立 OR 终端会把分支边界误当全局矛盾。

最新内部自足线删除 A1 活动标签，改写为：

```text
(AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput
 OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR NewPrimitiveJointPayloadArtifactOutsideSignedLaneCycle
 OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact)
AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet
AND RatePreservationLedger_FOR_moving_atom_packet
AND (DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
     OR SelfContainedDStructureTailLog4FiniteRankinProofPackage)
```

条件外部 KZ 支路可替换其中的循环外 payload 为：

```text
ExactExternalDIBFIKuznetsovNoProjectionCertificate_FOR_NONCIRCULAR_KZ_ONLY
```

但这仍只是条件输入；无黑箱外部版仍保留上一节的 FullS theorem-match / source-capacity /
new-dispersion 三择一边界。

## 26. Seed/payload 饱和后的两线边界

新增机器证书：

```text
experiments/prime_matrix_two_replacement_lines_seed_payload_saturation_sync_router.py
data/prime-matrix-two-replacement-lines-seed-payload-saturation-sync-ledger.json
docs/monograph/prime-matrix-two-replacement-lines-seed-payload-saturation-sync-router.md
docs/monograph/prime-matrix-two-replacement-lines-seed-payload-saturation-sync-router.json
```

本层继续同步 strict seed-cycle-cut、signed-lane cycle、new primitive payload/source-atom
alignment 与 preterminal source-rank atomization。结论是：

```text
AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput
```

不能再作为两条替代线的独立活动 OR；它已经饱和到：

```text
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
```

同时：

```text
NewPrimitiveJointPayloadArtifactOutsideSignedLaneCycle
```

若不只是 signed-lane 环内改名，必须实例化为 pre-Cauchy atomic signed payload/trace，
并进一步支付 source-rank/no-collapse 三原子：

```text
ActualPreCauchySourceDomainAbsoluteEntropyLedger
AND CompletePrimitiveEmitterKeyPartitionLedger
AND FixedKeyExactUVLocalMultiplicityO1Ledger
```

因此最新内部真剩余为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
 OR (ActualPreCauchySourceDomainAbsoluteEntropyLedger
     AND CompletePrimitiveEmitterKeyPartitionLedger
     AND FixedKeyExactUVLocalMultiplicityO1Ledger)
 OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
 OR ExactExternalDIBFIKuznetsovNoProjectionCertificate_FOR_NONCIRCULAR_KZ_ONLY)
AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet
AND RatePreservationLedger_FOR_moving_atom_packet
AND (DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
     OR SelfContainedDStructureTailLog4FiniteRankinProofPackage)
```

外部引理版仍只是：

```text
AcceptedFullSKLSExtExternalContract
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

无黑箱外部版仍需同对象 FullS theorem-match、actual source-capacity 新定理或
new automorphic/dispersion proof。FI/DI/BFI/Kuznetsov/Maynard 方向仍必须逐项匹配
当前 completed full-S non-AP WFD 对象、权重、窗口、模数范围、投影与误差预算。

## 27. Source-rank/terminal 核表同步后的两线边界

新增机器证书：

```text
experiments/prime_matrix_two_replacement_lines_sourcerank_terminal_kernel_sync_router.py
data/prime-matrix-two-replacement-lines-sourcerank-terminal-kernel-sync-ledger.json
docs/monograph/prime-matrix-two-replacement-lines-sourcerank-terminal-kernel-sync-router.md
docs/monograph/prime-matrix-two-replacement-lines-sourcerank-terminal-kernel-sync-router.json
```

本层把 source-rank/no-collapse 三原子与 terminal descent 下游接到同一
formal-unit 逐 primitive alpha/delta 核表。于是：

```text
ActualPreCauchySourceDomainAbsoluteEntropyLedger
AND CompletePrimitiveEmitterKeyPartitionLedger
AND FixedKeyExactUVLocalMultiplicityO1Ledger
```

不再作为粗包活动口保留；`AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate`
也不再作为 standalone 出口。两者共同压到：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger
AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
```

最新内部线为：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
 OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
 OR (AlphaRowAnchorPhaseEmissionFormulaLedger
     AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
     AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows)
 OR ExactExternalDIBFIKuznetsovNoProjectionCertificate_FOR_NONCIRCULAR_KZ_ONLY)
AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet
AND RatePreservationLedger_FOR_moving_atom_packet
AND (DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
     OR SelfContainedDStructureTailLog4FiniteRankinProofPackage)
```

外部引理版和无黑箱外部版仍保持上一节边界；本层没有证明 FullS theorem-match、
new automorphic/dispersion proof 或 DStructure/Rankin 独立验收。

## 28. Terminal-leaf/source-bridge 同步后的两线边界

新增机器证书：

```text
experiments/prime_matrix_two_replacement_lines_terminal_leaf_source_bridge_sync_router.py
data/prime-matrix-two-replacement-lines-terminal-leaf-source-bridge-sync-ledger.json
docs/monograph/prime-matrix-two-replacement-lines-terminal-leaf-source-bridge-sync-router.md
docs/monograph/prime-matrix-two-replacement-lines-terminal-leaf-source-bridge-sync-router.json
```

本层继续把上一节的三输入核表旧前沿接到既有 strict 证书：

```text
pointwise kernel triad
-> NonrecursivePointwisePrimitiveKernelTableConstructionWithoutTerminalReturn
-> terminal leaf firewall
-> AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
   OR actual source bridge
```

同步后，内部自足线不能再把三输入核表或旧 joint-alpha 路径当作新出口。
最新内部实际承重门为：

```text
(NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
 OR AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
 OR A1CleanBranchCanonicalSourceAdmission
 OR ExactCleanCoreFullSNonAPWFDSourceEntropy)
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet
AND RatePreservationLedger_FOR_moving_atom_packet
AND (DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
     OR SelfContainedDStructureTailLog4FiniteRankinProofPackage)
```

外部引理版仍只是条件闭合：

```text
AcceptedFullSKLSExtExternalContract
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

无黑箱外部版仍需：

```text
(ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch
 OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput
 OR NewAutomorphicDispersionProof)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

因此 FI/DI/BFI/Kuznetsov/Maynard/自守 \(L\) 函数方向若要继续推进，
必须逐项匹配上述同对象 FullS/actual-source 输入；不能只把旧 kernel
三输入改名为外部谱输入。

## 29. Alpha-return/source-bridge 同步后的两线边界

新增机器证书：

```text
experiments/prime_matrix_two_replacement_lines_alpha_return_bridge_sync_router.py
data/prime-matrix-two-replacement-lines-alpha-return-bridge-sync-ledger.json
docs/monograph/prime-matrix-two-replacement-lines-alpha-return-bridge-sync-router.md
docs/monograph/prime-matrix-two-replacement-lines-alpha-return-bridge-sync-router.json
```

本层继续导入 `strict-terminal-atoms-to-alpha-return-bridge-sync`。它把上一节的

```text
A1CleanBranchCanonicalSourceAdmission
OR ExactCleanCoreFullSNonAPWFDSourceEntropy
```

重分类为 scoped canonical 分支或 alpha-return 回边。同步后，内部自足线的活动前沿为：

```text
(NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
 OR AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
 OR IndependentActualSourceBridgeNotFactoredThroughAlphaReturn)
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet
AND RatePreservationLedger_FOR_moving_atom_packet
AND (DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
     OR SelfContainedDStructureTailLog4FiniteRankinProofPackage)
```

外部引理版仍为：

```text
AcceptedFullSKLSExtExternalContract
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

无黑箱外部版仍为：

```text
(ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch
 OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput
 OR NewAutomorphicDispersionProof)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

这一步不新增外部定理引用；它只说明若使用 FI/DI/BFI/Kuznetsov/Maynard/自守 \(L\)
函数方向，外部输入必须真正命中 FullS/actual-source 对象，而不是命中已经被判为回边的
alpha/pointwise 表展开。

## 30. Source-identity/antiatom 同步后的两线边界

新增机器证书：

```text
experiments/prime_matrix_two_replacement_lines_source_identity_antiatom_sync_router.py
data/prime-matrix-two-replacement-lines-source-identity-antiatom-sync-ledger.json
docs/monograph/prime-matrix-two-replacement-lines-source-identity-antiatom-sync-router.md
docs/monograph/prime-matrix-two-replacement-lines-source-identity-antiatom-sync-router.json
```

本层不新增外部定理引用。它把上一节的

```text
IndependentActualSourceBridgeNotFactoredThroughAlphaReturn
```

同步到 strict outside-loop 攻击证书中的两个真实非循环接口：

```text
ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab
OR FullSNonAPStrengthenedSourceAntiAtomForActualSource
```

含义是：若不接受外部 FullS-KLS 合同，则外部无黑箱路线仍必须证明同对象
FullS theorem-match、actual source capacity 新定理，或新的 automorphic/dispersion
证明；不能把 FI/DI/BFI/Kuznetsov/Maynard 的名称直接替换成 source identity 或
strengthened antiatom。

外部引理版仍为：

```text
AcceptedFullSKLSExtExternalContract
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

无黑箱外部版仍为：

```text
(ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch
 OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput
 OR NewAutomorphicDispersionProof)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

因此本层只是删除 `independent bridge` 粗名出口；不是任何外部深定理的新增
theorem-match，也不是目标命题的无条件闭合。

## 31. Canonical exact-certificate 同步后的两线边界

新增机器证书：

```text
experiments/prime_matrix_two_replacement_lines_canonical_exact_certificate_sync_router.py
data/prime-matrix-two-replacement-lines-canonical-exact-certificate-sync-ledger.json
docs/monograph/prime-matrix-two-replacement-lines-canonical-exact-certificate-sync-router.md
docs/monograph/prime-matrix-two-replacement-lines-canonical-exact-certificate-sync-router.json
```

本层同样不新增外部定理引用。它把

```text
AcyclicTerminalCanonicalLockToCanonicalSourceBoundary
```

同步到 strict canonical-lock nonrecursive exit 证书：

```text
AcyclicCanonicalExactSameSetPromotionCertificate
OR NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem
```

其中 exact same-set certificate 由五项账本组成：

```text
AcyclicSeedCanonicalBranchAdmissionBeforeCauchy
AND AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity
AND AcyclicSeedNoSourceReplacementOrPayloadCreation
AND TerminalCertificateSameSetPushforwardIdentity
AND NoNoncanonicalPayloadSurvivesCanonicalProjection
```

FI/DI/BFI/Kuznetsov/Maynard/自守 \(L\) 函数方向仍只能作用于同对象
FullS/actual-source theorem-match，不能替代这五项 same-set 账本，也不能替代新的
actual-source entropy 定理。

外部引理版仍为：

```text
AcceptedFullSKLSExtExternalContract
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

无黑箱外部版仍为：

```text
(ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch
 OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput
 OR NewAutomorphicDispersionProof)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本层只删除 `canonical-lock` 粗名出口；不构成新的外部引理闭合。

## 32. New-joint six-field 同步后的两线边界

新增机器证书：

```text
experiments/prime_matrix_two_replacement_lines_new_joint_sixfield_sync_router.py
data/prime-matrix-two-replacement-lines-new-joint-sixfield-sync-ledger.json
docs/monograph/prime-matrix-two-replacement-lines-new-joint-sixfield-sync-router.md
docs/monograph/prime-matrix-two-replacement-lines-new-joint-sixfield-sync-router.json
```

本层不新增外部定理引用。它把

```text
NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact
```

同步为更窄的 six-field actual formula 工件：

```text
NewActualJointAlphaDeltaSixFieldConstructorArtifact
```

六字段为：

```text
actual_noncanonical_source_tuple_domain
joint_row_index_and_formal_unit
basis_word_formula
signed_coefficient_formula
uv_phi_pairing
budget_and_failure_return
```

旧 joint rule 经 alpha-side、same-row、row-level、signed-emitter 返回 signed-source
固定点；terminal descent 替代路线返回宏循环；pair-energy 也不能生产逐行公式。因此
FI/DI/BFI/Kuznetsov/Maynard/自守 \(L\) 函数方向即使可作为外部谱输入，也不能替代这个
pre-Cauchy six-field 构造公式。

外部引理版仍为：

```text
AcceptedFullSKLSExtExternalContract
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

无黑箱外部版仍为：

```text
(ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch
 OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput
 OR NewAutomorphicDispersionProof)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本层只删除 `NewExplicit...` 粗名出口；不构成新的 theorem-match 或无条件闭合。

## 33. 两条替代线非循环硬攻后的外部/内部边界

新增机器证书：

```text
experiments/prime_matrix_two_replacement_lines_noncycle_hard_attack_router.py
data/prime-matrix-two-replacement-lines-noncycle-hard-attack-ledger.json
docs/monograph/prime-matrix-two-replacement-lines-noncycle-hard-attack-router.md
docs/monograph/prime-matrix-two-replacement-lines-noncycle-hard-attack-router.json
```

本层不新增外部定理引用；它只把外部引理版、无黑箱外部版和内部自足版的边界分开。

外部引理版作者侧条件基保持为：

```text
AcceptedFullSKLSExtExternalContract
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

这表示：接受 FullS-KLS-ext 作为外部黑箱，并接受 DStructure/Rankin 晋级包时，
作者侧普通剩余已经归零。它不是绝对无条件定理。

若要求无黑箱/绝对无条件化，外部侧必须替换为：

```text
(ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch
 OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput
 OR NewAutomorphicDispersionProof)
AND (DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
     OR SelfContainedDStructureTailLog4FiniteRankinProofPackage)
```

内部自足版必须支付：

```text
(NewActualJointAlphaDeltaSixFieldConstructorArtifact
 OR AcyclicCanonicalExactSameSetPromotionCertificate
 OR NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem
 OR ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab
 OR FullSNonAPStrengthenedSourceAntiAtomForActualSource)
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet
AND RatePreservationLedger_FOR_moving_atom_packet
AND SelfContainedDStructureTailLog4FiniteRankinProofPackage
```

Euler/Gauss/Riemann 三条纪律在本层只作为非循环守门规则：source/product 必须先于
pushforward，CRT/相位必须同集同对象，谱估计只能在 signed coefficient 已生成后使用。
它们不替代任何 theorem input。

## 34. 两条替代线共同无条件核

新增机器证书：

```text
experiments/prime_matrix_two_replacement_lines_common_unconditional_kernel_router.py
data/prime-matrix-two-replacement-lines-common-unconditional-kernel-ledger.json
docs/monograph/prime-matrix-two-replacement-lines-common-unconditional-kernel-router.md
docs/monograph/prime-matrix-two-replacement-lines-common-unconditional-kernel-router.json
```

本层不新增外部定理引用；它把绝对无条件外部线与内部自足线的共同核从各自前端中分离。
共同核为：

```text
SelfContainedDStructureTailLog4FiniteRankinProofPackage
```

该包展开为：

```text
SelfContainedDStructureStructuredEHPDDefinitionsAndABReductionProof
AND SelfContainedTailLog4BGOrRKSTailAdapterWithExactTheoremNumbersAndConstants
AND ReproducibleFiniteVerificationArchiveWithHashesAndIndependentRunner
AND SelfContainedFullRankinPassOrReturnLedgerAndDownstreamReturnIntegration
```

外部绝对无条件作者证明版仍需：

```text
(ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch
 OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput
 OR NewAutomorphicDispersionProof)
AND SelfContainedDStructureTailLog4FiniteRankinProofPackage
```

内部自足版仍需：

```text
(NewActualJointAlphaDeltaSixFieldConstructorArtifact
 OR AcyclicCanonicalExactSameSetPromotionCertificate
 OR NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem
 OR ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab
 OR FullSNonAPStrengthenedSourceAntiAtomForActualSource)
AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
AND HighSegmentModelGapAlpha043C3AnalyticLedger
AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet
AND RatePreservationLedger_FOR_moving_atom_packet
AND SelfContainedDStructureTailLog4FiniteRankinProofPackage
```

禁止代偿：FullS theorem-match 不支付 six-field/source/ExactUV/model/rate；six-field/source
不支付 FullS-KLS 谱估计；DStructure/Rankin 自足包也不支付任一前端，它只是两条绝对路线的共同尾门。

## 35. 两条替代线 RKS-log 最终原子

新增机器证书：

```text
experiments/prime_matrix_two_replacement_lines_rks_log_final_atom_sync_router.py
data/prime-matrix-two-replacement-lines-rks-log-final-atom-sync-ledger.json
docs/monograph/prime-matrix-two-replacement-lines-rks-log-final-atom-sync-router.md
docs/monograph/prime-matrix-two-replacement-lines-rks-log-final-atom-sync-router.json
```

本层不新增外部定理；它把共同核继续下钻到 Tail-log4 低谱的 RKS-log 原子。
Structured-EHPD 作者侧接口、finite Rankin pass-or-return、Tail-log4 smooth/mid 与参数账本
均不再是当前最窄点。

外部引理条件版仍为：

```text
AcceptedFullSKLSExtExternalContract
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

外部定理替代版可写为：

```text
AcceptedFullSKLSExtExternalContract
AND AcceptEXTBGForRKSLogFixedSaving
AND AuthorSideStructuredEHPDInterfaceAuditClosed
AND ReproducibleFiniteVerificationArchiveWithHashesAndIndependentRunner
AND SelfContainedFullRankinPassOrReturnLedgerAndDownstreamReturnIntegration
```

严格自足版必须重证：

```text
MultilinearReciprocalKloostermanFixedLogSavingForRKSBlocks
OR BakerFrequencyLargeSieveOrDBGAverageReplacement
```

禁止误用：Burgess 乘法角色和不能替代 RKS-log 加性倒数相位；EXT-BG 接受也不能当成自足重证。

## 36. 两条替代线 RKS-log/RNRS 版本调和

新增机器证书：

```text
experiments/prime_matrix_two_replacement_lines_rks_log_rnrs_version_reconciliation_router.py
data/prime-matrix-two-replacement-lines-rks-log-rnrs-version-reconciliation-ledger.json
docs/monograph/prime-matrix-two-replacement-lines-rks-log-rnrs-version-reconciliation-router.md
docs/monograph/prime-matrix-two-replacement-lines-rks-log-rnrs-version-reconciliation-router.json
```

本层不新增外部定理引用；它把最新 `RKS-log final atom` 与旧
`RNRS/Rudnev transfer closure` 做版本调和。哈希审计给出：

```text
same_rks_log_object_reconciled=true
same_log118_parameter_reconciled=true
rnrs_imports_exact_statement=true
noncycle_dependency_direction_closed=true
latest_rks_log_open_flag_superseded_by_rnrs=true
rks_log_current_active_obstruction=false
```

含义：RNRS/Rudnev 链处理的是同一个 Tail-log4/RKS2/RKS3 倒数 Kloosterman
`log^-118` 输入，且其依赖方向只从 strict RKS/Rudnev/RNRS 文件导入两条替代线，
不反向调用两条替代线结论。因此最新 RKS-log open 标记被删除。

最新内部活动硬点回到：

```text
ExactCleanCoreFullSNonAPWFDSourceEntropy
OR ActualNoncanonicalExactUVSupportLowerBound
OR CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn
```

外部引理版仍只是条件闭合：

```text
AcceptedFullSKLSExtExternalContract
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

无黑箱外部版仍需同对象来源或谱证明：

```text
(ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch
 OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput
 OR NewAutomorphicDispersionProof)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

本层不把 RNRS 回填误写为目标命题闭合：ExactUV/source、FullS theorem-match、
模型、PDEC/CleanKLS、Rate 与独立验收门仍需另行支付。

## 37. 两条替代线 ExactUV/source 非循环前沿

新增机器证书：

```text
experiments/prime_matrix_two_replacement_lines_exactuv_source_noncycle_frontier_router.py
data/prime-matrix-two-replacement-lines-exactuv-source-noncycle-frontier-ledger.json
docs/monograph/prime-matrix-two-replacement-lines-exactuv-source-noncycle-frontier-router.md
docs/monograph/prime-matrix-two-replacement-lines-exactuv-source-noncycle-frontier-router.json
```

本层不新增外部定理引用；它把 RKS/RNRS 调和后的 ExactUV/source 三标签做非循环下钻。
同步读数为：

```text
rks_log_current_active_obstruction=false
exactuv_entropy_layer_labels_are_ordered_interfaces=true
source_loop_cut_closed=true
acyclic_seed_current_corpus_proved=false
moving_atom_exclusion_current_corpus_proved=false
latest_internal_source_hardpoint=AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn
  AND ActualNoncanonicalCleanCoreMovingAtomExclusion
row_column_unconditional_closed=false
```

含义：`ExactCleanCoreFullSNonAPWFDSourceEntropy`、`ActualNoncanonicalExactUVSupportLowerBound`
和 `CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn` 是同一源侧链条的连续接口，不是
三个可循环替换的证明。该链经 clean-core 原始生成账本继续下钻后，旧
`origin ledger -> constructor -> formula -> emitter -> origin ledger` 路径形成来源闭环，不能
当作证明。

当前内部源侧标准形为：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn
AND ActualNoncanonicalCleanCoreMovingAtomExclusion
```

若坚持 ExactUV/pair-mass 路线，独立输入为：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn
AND IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed
```

无黑箱外部版仍需：

```text
(ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch
 OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput
 OR NewAutomorphicDispersionProof
 OR CDependentResidueWeightSpectralCancellationInput
 OR ExternalDIBFIKuznetsovDispersionTheoremMatch)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

外部引理版仍只是 `AcceptedFullSKLSExtExternalContract AND
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` 条件闭合；本层不支付无环源种子、
moving atom 排斥、模型、PDEC/CleanKLS、Rate 或 DStructure 门。

## 38. 两条替代线 seed/moving-atom/global-terminal 同步

新增机器证书：

```text
experiments/prime_matrix_two_replacement_lines_seed_moving_atom_global_terminal_sync_router.py
data/prime-matrix-two-replacement-lines-seed-moving-atom-global-terminal-sync-ledger.json
docs/monograph/prime-matrix-two-replacement-lines-seed-moving-atom-global-terminal-sync-router.md
docs/monograph/prime-matrix-two-replacement-lines-seed-moving-atom-global-terminal-sync-router.json
```

本层不新增外部定理引用；它把上一节的 moving atom 硬点与 strict
moving-atom/global-terminal 证书对齐。同步读数为：

```text
moving_atom_isolated_hardpoint_removed=true
latest_internal_terminal_hardpoint=AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn
  AND GlobalPDECorSparseTerminalExclusion
  AND ExplicitModelGapAndFiniteDPRCLedger
acyclic_seed_current_corpus_proved=false
global_pdec_sparse_terminal_exclusion_proved=false
explicit_model_gap_and_finite_dprc_ledger_proved=false
rate_preservation_ledger_proved=false
row_column_unconditional_closed=false
```

含义：`ActualNoncanonicalCleanCoreMovingAtomExclusion` 不再作为独立外部/内部出口保留。
若无环 seed 下仍有 clean-core moving atom，它必须进入全局 PDEC/sparse terminal packet，
并保留 `ExplicitModelGapAndFiniteDPRCLedger`。

外部引理版仍只是条件闭合：

```text
AcceptedFullSKLSExtExternalContract
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

无黑箱外部版仍需同对象来源或谱证明：

```text
(ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch
 OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput
 OR NewAutomorphicDispersionProof
 OR CDependentResidueWeightSpectralCancellationInput
 OR ExternalDIBFIKuznetsovDispersionTheoremMatch)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

严格自足版仍需 seed、`GlobalPDECorSparseTerminalExclusion`、模型/DPRC、Rate 与自足
DStructure/Rankin 替代包。本层不把 terminal reduction 写成目标命题无条件闭合。

## 39. 外部前沿定理压力测试：短区间、Linnik 与 P2 almost-prime

新增机器证书：

```text
experiments/prime_matrix_external_frontier_theorem_stress_router.py
data/prime-matrix-external-frontier-theorem-stress-ledger.json
docs/monograph/prime-matrix-external-frontier-theorem-stress-router.md
docs/monograph/prime-matrix-external-frontier-theorem-stress-router.json
```

本层主动引入并核对当前对行/列命题有帮助的外部前沿定理：

```text
Baker-Harman-Pintz 2001: pointwise short interval theta=0.525
Runbo Li 2025 preprint: claimed theta=0.52
Guth-Maynard 2024/2026: theta>17/30 short-interval PNT context
Gafni-Tao 2025: exceptional short intervals / zero-density transfer context
Xylouris 2011/2018: Linnik exponent 5.2 and <5
Meng 2001: bounded-cubic-part modulus exponent 4.5
Li-Zhang-Cai 2021: least P2 almost-prime in AP exponent 1.8345
```

压力测试读数：

```text
target_short_interval_theta=0.5
best_published_pointwise_short_interval_theta=0.525
best_frontier_preprint_pointwise_short_interval_theta=0.52
best_published_empty_row_run_exponent_bound=0.05
best_frontier_preprint_empty_row_run_exponent_bound=0.04
target_linnik_exponent=2
best_general_linnik_exponent_recorded=<5
best_special_prime_modulus_compatible_linnik_exponent_recorded=4.5
least_almost_prime_ap_exponent_inside_square=1.8345
row_column_unconditional_closed=false
```

真实副产品：Baker-Harman-Pintz 2001 非循环推出连续空行串不能有长度 `P^(0.05+eps)`
量级；若 Runbo Li 2025 预印本被接受，该指数可降至 `0.04+eps`。Xylouris/Meng
给列方向最终有素数，但高度仍在 `P^5` 或 `P^4.5`，不能进入 `P^2` 方阵。P2
almost-prime 结果能进入 `P^2`，但对象不是素数，正好标记奇偶屏障。

因此当前外部或内部真正需要的新突破仍是：

```text
PointwiseShortIntervalPrimeTheoremThetaLeHalf
OR LinnikExponentLeTwoWithSquareWindowConstants
OR GridTransferredShortIntervalSecondMomentAtThetaHalf
OR NonlinearParityBreakingActualSourceConstructor
```

## 47. P2 到素数转移原子审计

本层继续下钻 Li--Zhang--Cai `P2` almost-prime 输入，新增：

```text
experiments/prime_matrix_p2_to_prime_transfer_atom_audit.py
data/prime-matrix-p2-to-prime-transfer-atom-ledger.json
docs/monograph/prime-matrix-p2-to-prime-transfer-atom-audit.json
docs/monograph/prime-matrix-p2-to-prime-transfer-atom-audit.md
```

外部输入仍是：

```text
Li-Zhang-Cai arXiv:2103.13360v2:
  least P2 almost-prime in AP with exponent 1.8345

Ford-Maynard arXiv:2407.14368:
  prime-producing sieve framework, useful as source-design guidance only
```

新闭合的自足原子：

```text
If P is prime, 1<=a<P, n≡a mod P, Ω(n)=2 and n<P^2,
then n=r*m with prime r<P and m≡a*r^{-1} mod P.
If n<=P^sigma with sigma<2, then r<=P^(sigma/2).
```

因此 Li--Zhang--Cai 的 `sigma=1.8345` 把合成 P2 见证压成：

```text
r <= P^0.91725
m ≡ a*r^{-1} (mod P)
```

有限读数 `P<=997`：

```text
cofactor_ap_identity_closed=true
small_factor_bound_sample_closed=true
lzc_small_factor_bound_sample_closed=true
max_semiprime_to_prime_ratio_square: P=997, ratio=2.673362
max_least_p2_composite_share_square: P=929, share=0.641164
```

最新剩余基：

```text
SmallFactorCofactorAPCompositeFiberDominanceBound
OR PrimeBeforeCompositeP2SelectorInEveryFixedClass
OR FixedPrimeModulusZeroExceptionTransferForPrimeObjects
OR SameObjectNonlinearActualSourceConstructorBeforeProjection
OR PointwiseShortIntervalPrimeTheoremThetaLeHalf
OR LinnikExponentLeTwoWithSquareWindowConstants
```

状态边界：

```text
p2_to_prime_transfer_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
row_column_unconditional_closed=false
```

## 48. P2 最早见证选择器路线反证审计

本层继续下钻 P2-to-prime 转移，新增：

```text
experiments/prime_matrix_p2_selector_route_rejection_audit.py
data/prime-matrix-p2-selector-route-rejection-ledger.json
docs/monograph/prime-matrix-p2-selector-route-rejection-audit.json
docs/monograph/prime-matrix-p2-selector-route-rejection-audit.md
```

外部背景仍是 Li--Zhang--Cai 的 least-`P2` AP 定理；本层证明不能把该 least-`P2`
选择器升级为 prime 选择器。即使要求 `n>P`，有限反例已经出现：

```text
P=3, a=1, least_P2_after_P=4=2^2
```

大样本读数：

```text
P=101: first P2 composite share 0.570000
P=199: first P2 composite share 0.616162
P=499: first P2 composite share 0.640562
P=997: first P2 composite share 0.643574
large_sample_all_have_counterexamples=true
```

因此删除的路线：

```text
PrimeBeforeCompositeP2SelectorInEveryFixedClass
```

更新后的剩余基：

```text
SmallFactorCofactorAPCompositeFiberDominanceBound
OR NonleastPrimeSelectorRequiresAdditionalDistributionInput
OR FixedPrimeModulusZeroExceptionTransferForPrimeObjects
OR SameObjectNonlinearActualSourceConstructorBeforeProjection
OR PointwiseShortIntervalPrimeTheoremThetaLeHalf
OR LinnikExponentLeTwoWithSquareWindowConstants
```

状态边界：

```text
selector_route_rejected=true
p2_to_prime_transfer_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
row_column_unconditional_closed=false
```

## 49. 合成 P2 支持饱和审计

本层继续下钻 P2-to-prime 转移，新增：

```text
experiments/prime_matrix_composite_p2_support_saturation_audit.py
data/prime-matrix-composite-p2-support-saturation-ledger.json
docs/monograph/prime-matrix-composite-p2-support-saturation-audit.json
docs/monograph/prime-matrix-composite-p2-support-saturation-audit.md
```

外部背景仍是 Li--Zhang--Cai 的 least-`P2` AP 定理（`P^1.8345` 尺度）。
本层审计一个更弱但常被误用的 support-only 出口：若只知道每个 residue class
有 `P2` 支持，能否由支持信息推出 prime 支持。有限样本给出否定诊断：

```text
P=101,199,499,997,2003,5003:
  composite P2 support covers every nonzero residue below floor(P^1.8345)
P=499:
  every nonzero residue has strictly more composite P2 objects than prime objects
P=5003:
  min(composite_P2_count - prime_count)=95
  total composite_P2 / prime count ratio = 2.826571
```

因此删除的路线：

```text
ResidueSupportOnlyP2ToPrimeTransfer
```

更新后的剩余基：

```text
ObjectSensitivePrimeMinusCompositeP2SeparationInput
OR SmallFactorCofactorAPCompositeFiberDominanceBound
OR NonleastPrimeSelectorRequiresAdditionalDistributionInput
OR FixedPrimeModulusZeroExceptionTransferForPrimeObjects
OR SameObjectNonlinearActualSourceConstructorBeforeProjection
OR PointwiseShortIntervalPrimeTheoremThetaLeHalf
OR LinnikExponentLeTwoWithSquareWindowConstants
```

状态边界：

```text
support_only_p2_to_prime_transfer_rejected=true
p2_to_prime_transfer_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
row_column_unconditional_closed=false
```

## 50. Phi-LPF punctured endpoint 6-wheel capacity 证书

本层回到 Phi-LPF 奇偶屏障主线，新增：

```text
experiments/prime_matrix_phi_lpf_punctured_endpoint_wheel6_capacity_router.py
data/prime-matrix-phi-lpf-punctured-endpoint-wheel6-capacity-ledger.json
docs/monograph/prime-matrix-phi-lpf-punctured-endpoint-wheel6-capacity-router.json
docs/monograph/prime-matrix-phi-lpf-punctured-endpoint-wheel6-capacity-router.md
```

上一层 parity capacity 已证明：

```text
|F(P,k)| <= C_par(P,k)=W_int(P,k)-E_even(P,k).
```

本层加入 Euler `6`-wheel 的第二个局部筛除：若 reciprocal cofactor
`m>3` 且 `3|m`，则 `m` 不可能为素数。因此

```text
|F(P,k)| <= C_6(P,k)=W_int(P,k)-E_{2,3}(P,k)
DeltaPhi_half(P,k)>C_6(P,k) => pi((k+1)P-1)-pi(kP)>0
```

有限审计读数：

```text
max_prime=1009
row_count=76789
closed_by_parity_ceiling_count=76788
closed_by_wheel6_ceiling_count=76789
parity_not_closed_count=1
wheel6_not_closed_count=0
```

上一层唯一 parity 等号行被删除：

```text
P=19, k=15, Delta=3, C_par=3, C_6=2, Delta-C_6=1
```

新的剩余基：

```text
PuncturedWheel6EndpointCapacityInequalityOrReciprocalPrimePairWheel6SaturationPDEC
OR ExactExternalSqrtScaleOrFullSNonAPWFDKLSTheoremMatch
OR NewAutomorphicDispersionProof
OR SpecialSquarePhaseStructuralLowerBoundBeyondParity
```

外部源状态未改变：Runbo Li/短区间 `0.52` 仍大于 `1/2`，Runbo Li 2026
大模数 AP 仍是平均型输入，Ford--Maynard 仍是 prime-producing sieve 框架而
非本文同对象 Phi-LPF signed value table。

状态边界：

```text
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65AI. Phi-LPF terminal boundary bulk carry-chain normal form 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_boundary_bulk_carry_chain_normal_form_router.py
data/prime-matrix-phi-lpf-terminal-boundary-bulk-carry-chain-normal-form-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bulk-carry-chain-normal-form-router.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bulk-carry-chain-normal-form-router.md
```

本层把上一节的 `36` 个 bulk new residual 从散点压缩为 carry-chain normal form：

```text
new_residual_event_count=42
bulk_unmatched_new_residual_event_count=36
atom_count=7
carry_segment_count=11
carry_transition_count=31
carry_break_count=4
tail_closed_segment_count=6
open_segment_count=5
all_carry_transitions_exact=true
bulk_carry_chain_normal_form_closed=true
row_column_unconditional_closed=false
```

外部前沿匹配边界：谱分析与群论工具的作用更精确了。FKMS/Milićević--Qin--Wu/
Wright 型 trace/Kloosterman 工具需要把 `11` 个 segment root 变成 completed
averaged signed family；Pascadi/Type-II 需要二维 box 或 well-factorable 平均；
thin-group/expander/affine sieve 需要真正的 finite group orbit 与 expansion。当前证书
只给 finite carry normal form，没有给这些 admissible family。

最新开放口：

```text
BoundaryBulkCarrySegmentRootSourceLawOrPDEC
AND RightSelectedTerminalTailOverhangPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

## 65AH-2. Phi-LPF terminal double-Awrap sibling q-spine kernel 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_double_awrap_sibling_qspine_kernel_router.py
data/prime-matrix-phi-lpf-terminal-double-awrap-sibling-qspine-kernel-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-double-awrap-sibling-qspine-kernel-router.json
docs/monograph/prime-matrix-phi-lpf-terminal-double-awrap-sibling-qspine-kernel-router.md
```

本层继续收窄外部 theorem 的前置对象：terminal double-Awrap endpoint collar
已经被写成 paid sibling 与 P-scaled q-spine 三分母 kernel。

审计读数：

```text
same_q_path=true
same_turn_words=true
same_gap_carry=true
paid_sibling_tail_closed=true
sibling_gap_is_ten_internal_units=true
endpoint_offset_is_three_endpoint_units=true
target_kernel_identity_closed=true
p_scaled_kernel_identity_closed=true
terminal_double_awrap_sibling_qspine_kernel_closed=true
terminal_double_awrap_sibling_qspine_kernel_payment_law_proved=false
row_column_unconditional_closed=false
phi_lpf_parity_barrier_globally_broken=false
```

核心恒等式：

```text
179065/215287
= 123221/205013 + 36420/202379 + 10926/215287
= 607*(203/(439*467) + 60/(439*461) + 18/(461*467)).
```

外部定理边界：MQW/FKMS/Wright/Pascadi 型 trace、Kloosterman、Type-II 输入现在
必须作用在这个 P-scaled q-spine kernel 的可平均族上；Becker--Breuillard 型谱隙仍
需要先构造有限群轨道或 thin-group sieve family。最新非循环口为：

```text
BridgeRootQSpinePivotEnclosureLawOrPDEC
AND TerminalDoubleAwrapSiblingQSpineKernelPaymentOrPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

## 65AH-3. Phi-LPF terminal sibling q-spine integer-balance 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_sibling_qspine_integer_balance_router.py
data/prime-matrix-phi-lpf-terminal-sibling-qspine-integer-balance-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-sibling-qspine-integer-balance-router.json
docs/monograph/prime-matrix-phi-lpf-terminal-sibling-qspine-integer-balance-router.md
```

本层继续收窄外部 theorem 的前置对象：P-scaled q-spine 三分母 kernel
已经被写成 right-side q-spine `[439,461,467]` 上的整数守恒。

审计读数：

```text
denominators_closed=true
normalized_identity_closed=true
integer_balance_closed=true
endpoint_coefficients_closed=true
endpoint_offset_formula_closed=true
terminal_sibling_qspine_integer_balance_closed=true
terminal_sibling_qspine_integer_balance_payment_law_proved=false
row_column_unconditional_closed=false
phi_lpf_parity_barrier_globally_broken=false
```

核心恒等式：

```text
295/(461*467)
= 203/(439*467) + 60/(439*461) + 18/(461*467)
295*439 = 203*461 + 60*467 + 18*439 = 129505.
```

外部定理边界没有改变：MQW/FKMS/Wright/Pascadi 型 trace、Kloosterman、
Type-II 输入仍需要把这个整数 balance 升成可平均 signed family；
Becker--Breuillard 型谱隙仍需要有限群轨道或 thin-group sieve family。最新非循环口为：

```text
BridgeRootQSpinePivotEnclosureLawOrPDEC
AND TerminalSiblingQSpineIntegerBalancePaymentOrPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

## 65AH-4. Phi-LPF terminal sibling q-spine gap-drift 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_sibling_qspine_gap_drift_router.py
data/prime-matrix-phi-lpf-terminal-sibling-qspine-gap-drift-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-sibling-qspine-gap-drift-router.json
docs/monograph/prime-matrix-phi-lpf-terminal-sibling-qspine-gap-drift-router.md
```

本层继续收窄外部 theorem 的前置对象：terminal integer balance 已被改写为
primitive q-spine gap-drift，并显式剥离 LPF-threshold 因子 `7`。

审计读数：

```text
q_gaps_from_prefix=[22,28]
primitive_gap_vector=[11,14]
offset_cancels_from_gap_drift=true
gap_drift_identity_closed=true
primitive_gap_drift_identity_closed=true
lpf_factor_peeling_closed=true
terminal_sibling_qspine_gap_drift_closed=true
terminal_sibling_qspine_gap_drift_payment_law_proved=false
row_column_unconditional_closed=false
phi_lpf_parity_barrier_globally_broken=false
```

核心恒等式：

```text
(295-203-60-18)*439 = 22*203 + 28*60
14*439 = 22*203 + 28*60
7*439 = 11*203 + 14*60
439 = 11*29 + 2*60.
```

外部定理边界仍不变：MQW/FKMS/Wright/Pascadi 型 trace、Kloosterman、Type-II
输入必须作用在可平均的 signed gap-drift family 上；Becker--Breuillard 型谱隙
仍需要有限群轨道或 thin-group sieve family。最新非循环口为：

```text
BridgeRootQSpinePivotEnclosureLawOrPDEC
AND TerminalSiblingQSpinePrimitiveGapDriftPaymentOrPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

## 65AH-5. Phi-LPF terminal sibling q-spine 30-wheel residue-carrier 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_sibling_qspine_wheel_residue_router.py
data/prime-matrix-phi-lpf-terminal-sibling-qspine-wheel-residue-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-sibling-qspine-wheel-residue-router.json
docs/monograph/prime-matrix-phi-lpf-terminal-sibling-qspine-wheel-residue-router.md
```

本层继续收窄外部 theorem 的前置对象：7-peeled primitive gap-drift 已被改写为
30-wheel residue-carrier。

审计读数：

```text
q_prefix=439
wheel_modulus=30
residue_carrier=319
wheel_neutral_mass=120
residue_match_closed=true
wheel_lift_closed=true
carrier_identity_closed=true
terminal_sibling_qspine_wheel_residue_closed=true
terminal_sibling_qspine_wheel_residue_payment_law_proved=false
row_column_unconditional_closed=false
phi_lpf_parity_barrier_globally_broken=false
```

核心恒等式：

```text
439 = 11*29 + 4*30
439 mod 30 = (11*29) mod 30 = 19
4 = 2*(60/30).
```

外部定理边界仍不变：MQW/FKMS/Wright/Pascadi 型 trace、Kloosterman、Type-II
输入必须作用在可平均的 signed wheel-residue carrier family 上；Becker--Breuillard
型谱隙仍需要有限群轨道或 thin-group sieve family。最新非循环口为：

```text
BridgeRootQSpinePivotEnclosureLawOrPDEC
AND TerminalSiblingQSpineWheelResidueCarrierPaymentOrPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

## 65AI-3. Phi-LPF final negative-run endpoint-collar 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_right_tail_final_negative_run_endpoint_collar_router.py
data/prime-matrix-phi-lpf-right-tail-final-negative-run-endpoint-collar-ledger.json
docs/monograph/prime-matrix-phi-lpf-right-tail-final-negative-run-endpoint-collar-router.json
docs/monograph/prime-matrix-phi-lpf-right-tail-final-negative-run-endpoint-collar-router.md
```

本层继续收窄外部 theorem 的前置对象：上一层的 final negative run 实际是两步
terminal endpoint-collar wrap debt，而不是 completed trace family 或 group orbit。

审计读数：

```text
q_path=[461,463,467]
A_path=[417,87,34]
D_path=[44,376,433]
two_edge_sum_matches_variation_and_tail=true
endpoint_telescoping_closed=true
middle_phase_cancels=true
endpoint_collar_debt_formula_closed=true
double_awrap_same_lift_word_closed=true
right_tail_final_negative_run_endpoint_collar_reduction_closed=true
terminal_double_awrap_endpoint_collar_payment_law_proved=false
row_column_unconditional_closed=false
phi_lpf_parity_barrier_globally_broken=false
```

核心恒等式：

```text
179065/215287 = 417/461 - 34/467 = 1 - 44/461 - 34/467
```

外部定理边界因此更明确：MQW/FKMS/Wright/Pascadi 型 trace、Kloosterman、
Type-II 输入仍需先把 terminal double-Awrap collars 聚合成可平均的
moving-denominator family；Becker--Breuillard 型谱隙仍需先构造有限群轨道或
thin-group sieve family。最新非循环口为：

```text
BridgeRootQSpinePivotEnclosureLawOrPDEC
AND TerminalDoubleAwrapEndpointCollarPaymentOrPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

## 65AJ. Phi-LPF terminal boundary carry-break source-packet 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_boundary_carry_break_source_packet_router.py
data/prime-matrix-phi-lpf-terminal-boundary-carry-break-source-packet-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-carry-break-source-packet-router.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-carry-break-source-packet-router.md
```

本层把上一节的 `4` 个 carry break 拆成 `2` 个 bridge-root debt 与 `2` 个
unit old-return echo：

```text
carry_break_count=4
unit_old_return_echo_break_count=2
bridge_root_debt_break_count=2
paired_bridge_unit_packet_count=2
unmatched_unit_break_count=0
carry_break_source_packet_reduction_closed=true
bridge_root_source_law_proved=false
row_column_unconditional_closed=false
```

外部前沿匹配边界更加尖锐：单位步 echo 已回到 old-return 账本，不能再当作新的
trace/Kloosterman 平均对象；真正需要外部输入的只剩两个 bridge-root debt 和一个
right-tail overhang。FKMS/Milićević--Qin--Wu/Wright 型工具仍需要这些 bridge roots
先形成 completed averaged signed family；Pascadi/Type-II 仍需要二维可平均 box；
thin-group/expander 仍需要可证明的有限群轨道和扩张。

最新开放口：

```text
BoundaryBridgeRootDebtSourceLawOrPDEC
AND RightSelectedTerminalTailOverhangPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

## 65AK. Phi-LPF terminal boundary bridge-root q-spine microtemplate 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_boundary_bridge_root_qspine_microtemplate_router.py
data/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-microtemplate-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-microtemplate-router.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-microtemplate-router.md
```

本层把上一节的两个 bridge-root debt 压成共享 `q=607` 枢轴的 AD-singleton
q-spine 微模板：

```text
bridge_root_packet_count=2
all_bridge_roots_share_ad_singleton_template=true
unit_to_bridge_pivot_alignment_closed=true
shared_pivot_q=607
m_gap_between_bridge_packets=4
root_micro_q_shift=30
bridge_root_qspine_microtemplate_closed=true
bridge_root_qspine_source_law_proved=false
row_column_unconditional_closed=false
```

外部前沿匹配边界继续收窄：FKMS/Milićević--Qin--Wu/Wright 型 trace/Kloosterman、
Pascadi Type-II、以及 thin-group/expander 方法现在只可能作用在这个
AD-singleton q-spine 生成的 averaged signed family 上。当前证书只给 finite
microtemplate 和 shared pivot，不给可求和 family 或群轨道。

外部源核对（2026-05-25）：`arXiv:2511.09459` 是 trace-function 双线性平均；
`arXiv:2511.07550` 是任意模 Kloosterman 双线性平均；`arXiv:2505.00653`
处理 primes/smooth numbers 的分布指数与 Type-II/平均问题；`arXiv:2604.25177`
处理三线性 Kloosterman fractions；`arXiv:2411.12113` 处理 square-free/smooth
整数参数化的 Kloosterman sums。它们都要求先有 completed/averaged family，
不能替代本节的 `BridgeRootADSingletonQSpineSourceLawOrPDEC`。

最新开放口：

```text
BridgeRootADSingletonQSpineSourceLawOrPDEC
AND RightSelectedTerminalTailOverhangPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

## 65AL. Phi-LPF terminal boundary bridge-root q-spine Beatty margin 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_boundary_bridge_root_qspine_beatty_margin_router.py
data/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-beatty-margin-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-beatty-margin-router.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-beatty-margin-router.md
```

本层把 AD-singleton q-spine 的局部源律降到 Beatty 整数分子恒等式。若
`m=P+r`、`q'=q+g`、`a=floor(qr/P)`、`D=qr-aP`、
`s=floor((D+gr)/P)`，则四个微转移都满足

```text
phase_delta_num = lift_step*q*q_next + P*(s*q-a*g)
```

有限读数：

```text
micro_transition_count=4
beatty_numerator_identity_closed=true
A_singleton_negative_pure_P_multiple_closed=true
D_singleton_positive_margin_closed=true
bridge_root_qspine_beatty_margin_closed=true
bridge_root_uniform_beatty_margin_source_law_proved=false
row_column_unconditional_closed=false
```

外部前沿匹配边界随之更新：FKMS/Milićević--Qin--Wu/Wright 型 trace/Kloosterman
与 Pascadi Type-II 工具现在只能在这个 Beatty margin 对象被提升为 completed
averaged family 后进入；thin-group/expander 方法仍需要把 `r,a,s,B` 的有限
状态组织成真实有限群轨道与 expansion。当前证书给的是点态整数恒等式，不给
平均族、谱变量或群扩张。

最新开放口：

```text
BridgeRootADSingletonBeattyMarginSourceLawOrPDEC
AND RightSelectedTerminalTailOverhangPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

## 65AM. Phi-LPF terminal boundary bridge-root endpoint slack 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_boundary_bridge_root_endpoint_slack_router.py
data/prime-matrix-phi-lpf-terminal-boundary-bridge-root-endpoint-slack-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-endpoint-slack-router.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-endpoint-slack-router.md
```

本层把 D-singleton 的 Beatty 正 margin 继续拆成 endpoint slack 与 residual
项：

```text
D-singleton phase_delta_num = q*(P-q-g*(1+r)) + g*D
A-singleton phase_delta_num = -P*a*g
```

有限读数：

```text
bridge_root_endpoint_slack_reduction_closed=true
D_singleton_min_endpoint_slack=0
D_singleton_min_positive_margin=3954
D_singleton_zero_slack_rows=['m761 q601->607']
bridge_root_uniform_endpoint_slack_law_proved=false
row_column_unconditional_closed=false
```

外部前沿匹配边界进一步收窄：当前需要的不是一个一般 Kloosterman/Type-II
平均估计，而是先证明同对象的 endpoint slack 非负源律，或把 slack 负值行
命名为 PDEC。FKMS、Milićević--Qin--Wu、Wright、Pascadi 与 thin-group 工具
仍只能在该 slack 对象被提升成 completed averaged family 或有限群轨道后进入。

最新开放口：

```text
BridgeRootEndpointSlackNonnegativeLawOrPDEC
AND RightSelectedTerminalTailOverhangPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

## 65AN. Phi-LPF terminal boundary bridge-root moving endpoint barrier 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_boundary_bridge_root_moving_endpoint_barrier_router.py
data/prime-matrix-phi-lpf-terminal-boundary-bridge-root-moving-endpoint-barrier-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-moving-endpoint-barrier-router.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-moving-endpoint-barrier-router.md
```

本层把 endpoint slack 非负门继续压成 moving endpoint barrier 顺序：

```text
D-singleton endpoint_slack = (P-g*r)-q_bridge, where q_bridge=q_next
```

有限读数：

```text
bridge_root_moving_endpoint_barrier_reduction_closed=true
q_spine_nodes=[577, 607, 631]
all_barriers_lie_on_qspine=true
all_bridge_roots_lie_on_qspine=true
finite_bridge_root_barrier_order_closed=true
zero_barrier_contact_count=1
bridge_root_uniform_barrier_order_law_proved=false
row_column_unconditional_closed=false
```

外部前沿匹配边界同步收窄：Wright 型 unbalanced Kloosterman fractions、
Milićević--Qin--Wu 型 arbitrary-modulus Kloosterman 平均、Pascadi Type-II
分布、FKMS trace family 以及 thin-group/expander 工具，都不能直接证明
`q_bridge <= P-gr`。它们仍需要先把该 barrier-order 对象提升成 completed
averaged signed family、Type-II bilinear family 或真实有限群轨道。当前证书只给出
点态 q-spine 顺序账本和一个精确接触行。

最新开放口：

```text
BridgeRootMovingEndpointBarrierOrderLawOrPDEC
AND RightSelectedTerminalTailOverhangPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

## 65AO. Phi-LPF terminal boundary bridge-root q-spine index-gap 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_boundary_bridge_root_qspine_index_gap_router.py
data/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-index-gap-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-index-gap-router.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-index-gap-router.md
```

本层把 moving endpoint barrier 顺序继续压成 q-spine index-gap：

```text
endpoint_slack = sum of adjacent q-spine gaps from bridge index to barrier index
```

有限读数：

```text
bridge_root_qspine_index_gap_reduction_closed=true
q_spine_gap_vector=[30, 24]
qspine_index_gaps=[2, 0]
endpoint_slack_equals_qspine_gap_sum_closed=true
finite_qspine_index_order_closed=true
zero_index_contact_count=1
bridge_root_uniform_qspine_index_order_law_proved=false
row_column_unconditional_closed=false
```

外部前沿匹配边界再次收窄：目前缺的不是一般 Kloosterman/Type-II 平均，也不是
抽象 expansion，而是同一 q-spine 上 bridge index 不超过 barrier index 的点态顺序律。
FKMS、Milićević--Qin--Wu、Pascadi、Wright 与 thin-group/expander 工具仍只能在该
index-gap 对象被提升成 completed averaged signed family、Type-II bilinear family
或真实有限群轨道后进入。

最新开放口：

```text
BridgeRootQSpineIndexBarrierOrderLawOrPDEC
AND RightSelectedTerminalTailOverhangPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

## 65AP. Phi-LPF terminal boundary bridge-root q-spine pivot-enclosure 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_boundary_bridge_root_qspine_pivot_enclosure_router.py
data/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-pivot-enclosure-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-pivot-enclosure-router.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-pivot-enclosure-router.md
```

本层把 q-spine index-gap 顺序继续压成 shared-pivot enclosure：

```text
bridge_index <= pivot_index <= barrier_index
```

有限读数：

```text
bridge_root_qspine_pivot_enclosure_reduction_closed=true
shared_pivot_q=607
shared_pivot_index=1
finite_pivot_enclosure_closed=true
endpoint_slack_equals_pivot_gap_sum_closed=true
exact_pivot_contact_count=1
bridge_root_uniform_qspine_pivot_enclosure_law_proved=false
row_column_unconditional_closed=false
```

外部前沿匹配边界再次收窄：当前缺的是同一个 terminal q-spine 上 shared pivot
`607` 的点态包围律。FKMS、Milićević--Qin--Wu、Pascadi、Wright 与
thin-group/expander 工具不能直接推出这种 pivot enclosure；它们仍要求先构造
completed averaged signed family、Type-II bilinear family 或有限群轨道。

最新开放口：

```text
BridgeRootQSpinePivotEnclosureLawOrPDEC
AND RightSelectedTerminalTailOverhangPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

## 65AG. Phi-LPF terminal boundary new-residual tail alignment 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_boundary_new_residual_tail_alignment_router.py
data/prime-matrix-phi-lpf-terminal-boundary-new-residual-tail-alignment-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-new-residual-tail-alignment-router.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-new-residual-tail-alignment-router.md
```

本层承接 terminal boundary residual-flow 与 old-residual return alignment，把
new-side residual 的 tail-return 逐项核对：

```text
previous_residual_flow_side_decomposition_closed=true
previous_old_residual_return_alignment_closed=true
new_residual_event_count=42
tail_survivor_count=7
new_residual_tail_matched_event_count=6
new_residual_tail_alignment_partial_closed=true
new_residual_tail_matched_mass=1.580044997219
new_residual_unmatched_after_tail_event_count=36
new_residual_unmatched_after_tail_mass=11.684494473663
tail_survivor_unmatched_count=1
tail_survivor_unmatched_mass=0.831750175347
all_new_residual_return_alignment_closed=false
row_column_unconditional_closed=false
```

外部 theorem 边界同步收紧：FKMS trace bilinear、Milićević--Qin--Wu arbitrary-modulus
Kloosterman、Pascadi distribution/Type-II、Wright unbalanced Kloosterman fractions、
Shao--Shparlinski--Wijaya smooth/squarefree Kloosterman，以及 affine/thin-group
expansion 工具，都不能直接消去这 `36` 个 bulk residual 或 `1` 个 right-tail
overhang。它们只有在这些对象先被组织成可平均 signed trace/Type-II family 或
可扩张的有限群轨道族后才能进入。

最新开放口：

```text
BoundaryBulkNewResidualSourceLawOrPDEC
AND RightSelectedTerminalTailOverhangPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

## 附录 Q13AC43：terminal boundary residual-flow obstruction（2026-05-25）

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_boundary_residual_flow_obstruction_router.py
data/prime-matrix-phi-lpf-terminal-boundary-residual-flow-obstruction-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-residual-flow-obstruction-router.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-residual-flow-obstruction-router.md
```

本层继续 Q13AC42，不引入新的外部定理结论，而是重新定位外部定理能够进入的位置。
有限证书给出：

```text
residual_flow_side_decomposition_closed=true
new_residual_side_event_count=42
old_residual_side_event_count=5
new_residual_mass_total=13.264539470882
old_residual_mass_total=0.215539338772
net_new_minus_old_residual_mass=13.049000132111
finite_boundary_local_opposite_side_cancellation_refuted=true
row_column_unconditional_closed=false
```

外部前沿匹配边界：

```text
Kowalski-Michel-Sawin bilinear Kloosterman input: 后置求和工具，不能生成 source-key residual law.
Milicevic-Qin-Wu arbitrary-modulus Kloosterman saving: 需要 admissible family，不能替代边界残差源项。
Shao-Shparlinski-Wijaya smooth/squarefree Kloosterman input: 控制模数族求和，不控制 47 个局部 run residual side。
Matomaki-Merikoski-Teravainen L-function-free sieve input: 可作筛法比较，不给出 Phi-LPF pre-pushforward signed payload。
```

因此下一条可调用外部定理的合同不是“local opposite-side cancellation”，而是：

```text
BoundaryDominantNewResidualSourceLawOrPDEC
AND BoundaryResidualTransportToNonBoundaryInternalReturnsOrPDEC
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

状态边界：

```text
boundary_residual_flow_source_key_conservation_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
```

## 附录 Q13AC44：terminal boundary old-residual return alignment（2026-05-25）

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_boundary_old_residual_return_alignment_router.py
data/prime-matrix-phi-lpf-terminal-boundary-old-residual-return-alignment-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-old-residual-return-alignment-router.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-old-residual-return-alignment-router.md
```

本层不调用新的外部定理，而是把外部定理入口进一步推后：old-side residual 已经在
有限 source-key ledger 内精确返回。

```text
old_residual_return_alignment_closed=true
old_residual_event_count=5
nonboundary_record_jump_event_count=4
internal_survivor_return_count=1
old_residual_equals_nonboundary_plus_internal_obstruction=true
unmatched_old_residual_return_mass=0
new_residual_mass_total_still_open=13.264539470882
row_column_unconditional_closed=false
```

外部前沿匹配边界更新：Kloosterman、Type-II、DI/BFI/Kuznetsov 或 L-function-free
sieve 输入不需要解释 old-side residual；该子门已经由 finite source-key return
alignment 支付。它们仍然不能替代以下缺失对象：

```text
BoundaryDominantNewResidualSourceLawOrPDEC
AND BoundaryNewResidualReturnOrPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
```

只有在 new-side source/return 被构造成 admissible signed family 后，外部求和定理才有
可验证入口。

## 附录 Q13AC42：terminal boundary split ratio obstruction（2026-05-25）

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_boundary_split_ratio_obstruction_router.py
data/prime-matrix-phi-lpf-terminal-boundary-split-ratio-obstruction-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-split-ratio-obstruction-router.json
docs/monograph/prime-matrix-phi-lpf-terminal-boundary-split-ratio-obstruction-router.md
```

本层继续 Q13AC41，把最大的 q-boundary split 分支压成相邻 run 质量比率谱：

```text
boundary_ratio_spectrum_closed=true
q_boundary_synthetic_split_event_count=47
boundary_adjacency_closed=true
whole_equal_pair_event_count=0
old_consumed_new_residual_event_count=42
old_residual_new_consumed_event_count=5
negative_to_positive_event_count=24
positive_to_negative_event_count=23
```

比率谱读数：

```text
ratio_min=0.013003592969
ratio_max=0.967151620496
boundary_chunk_mass_total=14.631796550631
boundary_residual_gap_mass_total=13.480078809654
boundary_residual_gap_mass_max=0.861355534983
```

外部 trace/Kloosterman/Type-II 工具仍不能直接接入：边界定位已经闭合，缺的是
相邻 run 质量比率律或 source-key 残流守恒律。

最新非循环口：

```text
BoundaryAdjacentRunMassRatioLawOrPDEC
AND BoundaryResidualFlowSourceKeyConservationOrPDEC
AND NonBoundaryPrefixRecordJumpSourceKeyLiftOrPDEC
AND InternalPrefixRecordSurvivorPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

## 附录 Q13AC41：terminal source-key obstruction partition（2026-05-25）

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_source_key_obstruction_partition_router.py
data/prime-matrix-phi-lpf-terminal-source-key-obstruction-partition-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-source-key-obstruction-partition-router.json
docs/monograph/prime-matrix-phi-lpf-terminal-source-key-obstruction-partition-router.md
```

本层继续 Q13AC40，把 `PrefixRecordSourceKeyLiftOrPDEC` 拆成三个 actual 缺口：

```text
source_key_obstruction_partition_closed=true
cancellation_event_count=51
whole_run_pair_event_count=0
synthetic_split_event_count=51
q_boundary_synthetic_split_event_count=47
nonboundary_record_jump_event_count=4
nonboundary_record_jump_atom_count=2
tail_survivor_fragment_count=7
internal_survivor_fragment_count=1
```

有限标量检查显示，非边界 jump 与内部 survivor 的合计质量不是当前最大数值障碍：

```text
nonboundary_plus_internal_obstruction_mass=0.215539338772
finite_selected_margin_after_nonboundary_internal_payment=0.333307310624
finite_margin_after_nonboundary_internal_payment_positive=true
```

但这不是证明。外部 trace/Kloosterman/Type-II 工具仍不能直接接入，因为 q-boundary
split ratio、non-boundary record jump 与 internal survivor 都没有 source-key lift。

最新非循环口：

```text
BoundarySyntheticSplitRatioSourceKeyLawOrPDEC
AND NonBoundaryPrefixRecordJumpSourceKeyLiftOrPDEC
AND InternalPrefixRecordSurvivorPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

## 附录 Q13AC40：terminal prefix-record reflection source-key obstruction（2026-05-25）

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_prefix_record_source_key_obstruction_router.py
data/prime-matrix-phi-lpf-terminal-prefix-record-source-key-obstruction-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-prefix-record-source-key-obstruction-router.json
docs/monograph/prime-matrix-phi-lpf-terminal-prefix-record-source-key-obstruction-router.md
```

本层继续上一层 adjacent-run Jordan cancellation，把形式抵消写成 prefix-record/reflection
账本。确定性一维账本已经闭合：

```text
previous_formal_jordan_cancellation_law_closed=true
terminal_atom_count=7
terminal_run_count_total=59
prefix_record_reflection_schema_closed=true
cancellation_event_count=51
```

但是这仍不能直接调用外部 trace/Kloosterman/Type-II 定理，因为抵消块没有 source-key
lift：

```text
whole_run_pair_event_count=0
synthetic_split_event_count=51
q_boundary_pair_event_count=47
non_q_boundary_pair_event_count=4
survivor_fragment_count_total=8
internal_survivor_fragment_count=1
prefix_record_source_key_lift_constructed=false
row_column_unconditional_closed=false
```

外部输入边界相应收窄为：

| 外部输入 | 主源 | 当前缺口 |
| --- | --- | --- |
| Fouvry--Kowalski--Michel--Sawin, bilinear trace functions | https://arxiv.org/abs/2511.09459 | 需要先把 prefix-record chunks 晋级为带 source-key 的 trace-function bilinear family |
| Milićević--Qin--Wu, arbitrary-modulus Kloosterman bilinear forms | https://arxiv.org/abs/2511.07550 | 需要把 moving Beatty phase 与 prefix record 同时完成成双变量 Kloosterman family |
| Pascadi, distribution of primes and smooth numbers | https://arxiv.org/abs/2505.00653 | 需要把 pointwise terminal load 改写成 well-factorable AP averages |
| Wright, trilinear Kloosterman fractions | https://arxiv.org/abs/2604.25177 | 需要三线性 convolution、source-key lift 与 equidistributed beta sequence |

最新非循环口：

```text
PrefixRecordSourceKeyLiftOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

## 附录 Q13AC39：terminal adjacent-run Jordan cancellation source obstruction（2026-05-25）

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_adjacent_run_jordan_cancellation_source_obstruction_router.py
data/prime-matrix-phi-lpf-terminal-adjacent-run-jordan-cancellation-source-obstruction-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-adjacent-run-jordan-cancellation-source-obstruction-router.json
docs/monograph/prime-matrix-phi-lpf-terminal-adjacent-run-jordan-cancellation-source-obstruction-router.md
```

本层把 `UniformAdjacentRunCancellationFamilyOrPDEC` 分成形式恒等式与 actual
source-preserving 两层。形式层已经闭合：

```text
terminal_phase_path_count=7
terminal_transition_count_total=126
terminal_run_count_total=59
sign_matches_Awrap_all_transitions=true
signed_telescoping_identity_closed=true
formal_jordan_cancellation_law_closed=true
```

但外部定理仍不能直接接入，因为当前抵消不是完整 run involution：

```text
cancellation_event_count=51
complete_whole_run_pair_event_count=0
synthetic_split_cancellation_event_count=51
internal_survivor_fragment_count=1
source_preserving_adjacent_run_pairing_constructed=false
```

外部输入边界相应更新：

| 外部输入 | 主源 | 当前缺口 |
| --- | --- | --- |
| Fouvry--Kowalski--Michel--Sawin, bilinear trace functions | https://arxiv.org/abs/2511.09459 | 需要把 adjacent-run chunks 晋级为 trace-function bilinear family |
| Milićević--Qin--Wu, arbitrary-modulus Kloosterman bilinear forms | https://arxiv.org/abs/2511.07550 | 需要把 moving Beatty phase 完成成双变量 Kloosterman family |
| Pascadi, distribution of primes and smooth numbers | https://arxiv.org/abs/2505.00653 | 需要把逐行/逐列点态负载转成 well-factorable AP averages |
| Wright, trilinear Kloosterman fractions | https://arxiv.org/abs/2604.25177 | 需要三线性 convolution 与 equidistributed beta sequence |

最新非循环口：

```text
SourcePreservingAdjacentRunPairingOrInternalSurvivorPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

## 附录 Q13AC38：terminal monotone-run total-to-net compression frontier（2026-05-25）

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_monotone_run_total_to_net_compression_frontier_router.py
data/prime-matrix-phi-lpf-terminal-monotone-run-total-to-net-compression-frontier-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-monotone-run-total-to-net-compression-frontier-router.json
docs/monograph/prime-matrix-phi-lpf-terminal-monotone-run-total-to-net-compression-frontier-router.md
```

本层沿上一轮的 `MonotoneRunTotalToNetCompressionOrPDEC` 开口继续下钻。机器读数为：

```text
terminal_run_count_total=59
selected_terminal_run_count=35
extra_shell_run_count=24
run_local_compression_ratio_min=1
run_local_compression_ratio_max=1
strict_run_local_compression_count=0
atom_adjacent_cancellation_decomposition_closed=true
finite_absorption_would_close_after_uniform_cancellation_law=true
monotone_run_total_to_net_compression_proved=false
```

因此，finite run ledger 的真实结构不是“run 内变差自动变小”，而是：

```text
total variation = adjacent opposite-run cancelled chunks + atom-local survivor.
```

若可证明统一相邻 run 抵消律，extra total variation
`14.109301881162` 会压到 extra atom-local survivor `0.907719323182`，
并被 selected negative excess `1.456565972578` 支付。但目前外部定理仍不能直接给出这条律。

外部适配边界更新：

| 外部输入 | 可用前提 | 当前缺口 |
| --- | --- | --- |
| FKMS trace/bilinear, arXiv:2511.09459v3 | terminal runs 晋级为带 monodromy 数据的 bilinear trace-function family | 当前只是有限 run ledger |
| Milićević--Qin--Wu, arXiv:2511.07550v1 | moving Beatty numerator 完成成真正双变量 Kloosterman family | prime-`q` prefix 尚未构成可求和族 |
| Pascadi, arXiv:2505.00653v2 | 权重成为 triply-well-factorable AP averages | 所需是 `P^2` 尺度逐行/逐列正性 |
| Wright, arXiv:2604.25177v1 | payload 晋级为三线性 Kloosterman-fraction convolution | 当前没有二维/三维 beta 序列 |

最新非循环口压成：

```text
UniformAdjacentRunCancellationFamilyOrPDEC
AND AtomLocalSurvivorPaymentOrPDEC
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

## 附录 Q13AC37：terminal signed payload measure absorption frontier（2026-05-25）

新增证书：

```text
experiments/prime_matrix_phi_lpf_terminal_signed_payload_measure_absorption_frontier_router.py
data/prime-matrix-phi-lpf-terminal-signed-payload-measure-absorption-frontier-ledger.json
docs/monograph/prime-matrix-phi-lpf-terminal-signed-payload-measure-absorption-frontier-router.json
docs/monograph/prime-matrix-phi-lpf-terminal-signed-payload-measure-absorption-frontier-router.md
```

本层把 terminal/extra phase-turn 数据压成有限 signed payload measure `mu(q,m,packet)`，
并检查它是否已经满足外部 trace/Kloosterman/Type-II 输入所需的 averaged family 条件。
读数为：

```text
terminal_signed_payload_measure_schema_closed=true
mu_transition_count=126
selected_net_excess_beats_extra_net_excess=true
selected_net_excess_beats_extra_total_variation=false
admissible_averaged_trace_family_created=false
trace_or_kloosterman_completion_ready=false
```

FKMS 与 DI/BFI/Kuznetsov 可在 `mu` 晋级为 averaged trace family 后进入；Milićević--Qin--Wu
与 Wright 型 Kloosterman/fraction 输入需要 moving Beatty numerator `A(q)/q` 的可求和完成；
Pascadi Type-II 需要真正二维 Type-II rectangle。当前对象仍只是两个 `P` packet、七个
fixed-`m` atoms 的一维 prime-`q` prefix transition measure。

最新外部适配入口压成：

```text
MonotoneRunTotalToNetCompressionOrPDEC
AND ExtraTotalVariationAbsorptionOrLocalSurvivor
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

## 附录 Q13AC36：factor-word parity shadow orientation no-go（2026-05-25）

新增证书：

```text
experiments/prime_matrix_phi_lpf_factor_word_parity_shadow_orientation_nogo_router.py
data/prime-matrix-phi-lpf-factor-word-parity-shadow-orientation-nogo-ledger.json
docs/monograph/prime-matrix-phi-lpf-factor-word-parity-shadow-orientation-nogo-router.json
docs/monograph/prime-matrix-phi-lpf-factor-word-parity-shadow-orientation-nogo-router.md
```

本层不引入新外部定理，而是审计外部定理是否能直接吃掉 factor-word parity shadow。
结论是否定的：

```text
factor_word_mobius_shadow_closed=true
factor_word_liouville_shadow_closed=true
depth_parity_shadow_closed=true
shadow_depends_only_on_unsigned_factor_word=true
shadow_lacks_precauchy_source_key=true
shadow_lacks_orientation_branch_trace=true
shadow_lacks_exactuv_payload=true
factor_word_shadow_proves_orientation_local_factor_law=false
factor_word_shadow_proves_builtin_pairing=false
```

FKMS、Milićević--Qin--Wu、Pascadi、Wright 型 trace/Kloosterman/Type-II 输入仍需
可求和的 averaged signed payload family；DI/BFI/Kuznetsov 仍需相位、模数、频率与
well-factorable 权重同口径化。Möbius/Liouville/depth parity 只是 pointwise
post-factorization label，不能作为这些外部定理的 admissible family。

最新外部适配入口保持为：

```text
PrimitiveOrientationLocalFactorProductLawBeforePushforward
OR BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
OR admissible averaged signed trace/Kloosterman/Type-II family with named returns
```

---

## 附录 Q13AC28：三命题突破路线总合成的外部定理边界（2026-05-25）

新增归档：

```text
docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md
```

本层不是新增外部定理引用，而是重新排序外部定理可用边界：

```text
three_claim_breakthrough_synthesis_archived=true
external_theorem_requires_admissible_family=true
support_only_is_parity_blind=true
rankone_ap_positivity_direct_route_not_closed=true
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
phi_lpf_parity_barrier_globally_broken=false
```

外部前沿输入的准确使用纪律如下。

| 输入 | 当前可用位置 | 仍缺的项目 |
| --- | --- | --- |
| DI/BFI/Kuznetsov | 二点筛 `BMD/KLS-window` 外部版；可服务 well-factorable 权重与 Kloosterman 平均 | `BMD=>TLI` 的 actual denominator floor 与同 convention 误差优势 |
| FKMS trace/bilinear、Milićević--Qin--Wu、Pascadi、Wright | Prime Matrix/Phi-LPF 线只有在 terminal signed payload 被构造成 averaged trace/Kloosterman/Type-II family 后才能调用 | 当前 terminal phase variation budget 还不是可求和完成型族 |
| Li short intervals、Maynard small gaps | 可作为邻近素数分布背景 | 不控制每个 row、每个 residue class 或 terminal signed variation |
| Dong--Robles--Zeindler withdrawn item | 只保留为不可用边界 | 不得作为证明输入 |

本层把下一步外部定理接口压成：

```text
ActualSignedPayloadTraceConstructorBeforeAssignmentOrReturn
OR MonotoneRunPhaseSavingWithExtraBudgetAbsorption
OR PDEC/SAE/LocalSurvivor named return
```

因此后续若引用 FKMS、Milićević--Qin--Wu、Pascadi 或 Wright，必须先提交
admissible family constructor；若无法构造，则失败必须回流到命名
PDEC/SAE/LocalSurvivor 出口，不能保留匿名 parity gap。

---

## 附录 Q13AC29：affine `2n+1` Euler-LPF 诊断的外部定理边界（2026-05-25）

新增证书：

```text
experiments/prime_matrix_affine_2n_plus_1_euler_lpf_parity_audit.py
data/prime-matrix-affine-2n-plus-1-euler-lpf-parity-ledger.json
docs/monograph/prime-matrix-affine-2n-plus-1-euler-lpf-parity-audit.json
docs/monograph/prime-matrix-affine-2n-plus-1-euler-lpf-parity-audit.md
```

本层不需要新的外部定理。它是一个归一化与筛余双射审计：

```text
n = kP + (P-1)/2
2n+1 = (2k+1)P
p | (2n+1) <=> n == (p-1)/2 mod p
```

审计结论：

```text
affine_sieve_bijection_verified_all_samples=true
apparent_half_main_gap_explained_by_missing_p2_all_samples=true
euler_product_half_main_error_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
```

外部定理边界因此保持不变：该 affine map 只把 `m` 侧零同余类转成 `n` 侧 shifted
同余类。若在 `m` 侧漏掉 `p=2` 或不先限制到奇数样本空间，就会出现半主项 gap
假象；这不是 FKMS、Milićević--Qin--Wu、Pascadi、Wright 或 DI/BFI 可以直接使用的
相消 family。要调用这些外部输入，仍必须先构造 admissible averaged signed
payload family；要用该 affine 路线破奇偶，仍需

```text
AffineShiftedResidueSieveSignedPayloadConstructorOrReturn
AND PrimeExtractionFrom2nPlus1RoughSurvivorsBeyondParity
```

---

## 附录 Q13AC30：power-two affine/Phi-LPF 迭代无新增益边界（2026-05-25）

新增证书：

```text
experiments/prime_matrix_affine_power_two_phi_lpf_iteration_no_gain_audit.py
data/prime-matrix-affine-power-two-phi-lpf-iteration-no-gain-ledger.json
docs/monograph/prime-matrix-affine-power-two-phi-lpf-iteration-no-gain-audit.json
docs/monograph/prime-matrix-affine-power-two-phi-lpf-iteration-no-gain-audit.md
```

本层不引入新外部定理。它把 `2n+1` 推广为

```text
m_t = 2^t n + (2^t-1)
```

并验证对每个奇素数 `p`：

```text
p | m_t  <=>  n == -(2^t-1)*(2^t)^(-1) mod p.
```

审计边界：

```text
all_shifted_residue_formula_verified=true
naive_gap_tracks_two_adic_density=true
iteration_creates_new_phi_lpf_information=false
euler_product_half_main_error_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
```

因此 affine/Phi-LPF 迭代不能作为外部 trace/Kloosterman 输入的替代品。它仍只是
shifted-residue conjugacy；要使用 FKMS、Milićević--Qin--Wu、Pascadi、Wright 或
DI/BFI/Kuznetsov，仍必须先构造 averaged signed payload family。新的开放口为：

```text
PowerTwoAffineShiftedResidueSignedPayloadConstructorOrNamedReturn
AND PrimeExtractionFromAffineRoughSurvivorsBeyondParity
```

## 65AH. Phi-LPF repeated-step affine-skeleton packet-enclosure 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_repeated_step_affine_skeleton_packet_enclosure_audit.py
data/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-affine-skeleton-packet-enclosure-ledger.json
docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-affine-skeleton-packet-enclosure-audit.json
docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-affine-skeleton-packet-enclosure-audit.md
```

本层承接 65AG，把 one-pair affine skeleton 嵌回实际 right-tail shell-step
packets：

```text
packet_enclosure_ledger_closed=true
unique_left_packet_indices=[2842]
unique_right_packet_indices=[1887]
left_q_prefix_count=28
right_q_prefix_count=7
q_prefix_count_delta=-21
left_m_shell_prime_count=4
right_m_shell_prime_count=3
left_edge_count=112
right_edge_count=21
all_q_windows_disjoint=true
all_m_shells_disjoint=true
all_selected_pairs_terminal=true
```

具体包络为：

```text
packet2842: P739, q-window [541,709], m={719,751,757,761}
packet1887: P607, q-window [439,467], m={479,769,773}
```

这把 affine-skeleton obstruction 进一步定位到两个不相交 q-window 与两个不相交
m-shell 的 right-tail packet enclosure。外部 theorem 边界仍不变：
trace/Kloosterman 平均输入需要把该固定包络扩展为可求和族；Maynard 小间距与
Li 短区间素数不控制该固定包络的相消。

状态边界：

```text
packet_enclosure_ledger_closed=true
packet_enclosure_uniform_bound_proved=false
summable_family_created=false
trace_or_kloosterman_completion_ready=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65AI. Phi-LPF repeated-step packet-enclosure terminal line-atom 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_repeated_step_packet_enclosure_terminal_line_atom_audit.py
data/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-line-atom-ledger.json
docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-line-atom-audit.json
docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-line-atom-audit.md
```

本层承接 65AH，把两个 right-tail packet 的唯一支撑拆成固定 `m` 的
q-prefix line atoms，并区分 selected terminal 支撑与 extra shell 支撑：

```text
terminal_line_atom_ledger_closed=true
support_packet_indices=[2842,1887]
support_packet_edge_mass=133
unique_line_atom_count_total=7
unique_line_atom_edge_mass_total=133
selected_terminal_line_atom_count=4
selected_terminal_line_atom_edge_mass=70
extra_line_atom_count=3
extra_line_atom_edge_mass=63
selected_and_extra_edges_disjoint=true
all_line_atoms_qprefix_contiguous=true
all_selected_line_atoms_terminal=true
packet_line_atom_mass_identity_verified=true
splice_incidence_selected_edge_mass=140
splice_incidence_extra_edge_mass=126
```

selected terminal line atoms 为
`(P739,m=757),(P739,m=761),(P607,m=769),(P607,m=773)`；extra line atoms
为 `(P739,m=719),(P739,m=751),(P607,m=479)`。两条 splice 共享同一 packet
支撑，所以 incidence 质量只是唯一支撑质量的两倍，不是新的相消来源。

外部 theorem 边界仍不变：FKMS、Milićević--Qin--Wu、Pascadi 与 Wright 型
trace/Kloosterman/Type-II 输入需要 completed moving-denominator family；Li
短区间素数与 Maynard 小间距不控制这些固定 terminal line atoms 的相位。

状态边界：

```text
terminal_line_atom_ledger_closed=true
selected_terminal_line_atom_uniform_bound_proved=false
packet_extra_line_atom_absorption_proved=false
summable_family_created=false
trace_or_kloosterman_completion_ready=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65AJ. Phi-LPF repeated-step packet-enclosure terminal phase-normal-form 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_repeated_step_packet_enclosure_terminal_phase_normal_form_audit.py
data/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-normal-form-ledger.json
docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-normal-form-audit.json
docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-normal-form-audit.md
```

本层承接 65AI，对 7 个 terminal/extra line atoms 的每条边写

```text
q*m=k*P+D,  0<D<P,  A(q)=-D mod q,
e(h*k*P/q)=e(-h*D/q)=e(h*A(q)/q).
```

有限审计读数：

```text
terminal_phase_normal_form_closed=true
terminal_phase_normal_form_atom_count_total=7
terminal_phase_normal_form_edge_count_total=133
selected_terminal_phase_atom_count=4
selected_terminal_phase_edge_count=70
extra_phase_atom_count=3
extra_phase_edge_count=63
product_division_mismatch_count=0
phase_congruence_mismatch_count=0
D_out_of_range_count=0
A_zero_count=0
all_phase_k_strictly_increasing=true
selected_terminal_all_moving_numerator=true
selected_terminal_all_full_distinct_numerator=true
selected_terminal_fixed_numerator_atom_count=0
```

结论是更窄但仍未闭合：四个 selected terminal atoms 全部是 moving 且
full-distinct 的 Beatty numerator orbit。外部 theorem 边界进一步精确为：
FKMS/Milićević--Qin--Wu/Wright/Pascadi 仍需要 completed family 或 Type-II box；
Li 短区间素数与 Maynard 小间距不估计 `e(h*A(q)/q)`。

状态边界：

```text
terminal_phase_normal_form_closed=true
selected_terminal_fixed_numerator_kloosterman_ready=false
selected_terminal_moving_beatty_numerator_phase_saving_proved=false
extra_phase_absorption_proved=false
summable_family_created=false
trace_or_kloosterman_completion_ready=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65AK. Phi-LPF repeated-step packet-enclosure terminal phase carry-orbit 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_repeated_step_packet_enclosure_terminal_phase_carry_orbit_audit.py
data/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-carry-orbit-ledger.json
docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-carry-orbit-audit.json
docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-carry-orbit-audit.md
```

本层承接 65AJ，把 moving Beatty numerator 的相邻 prime-q 运动写成
确定性 carry recurrence。若 `q'=q+g` 且

```text
q*m=k*P+D,  q'*m=k'*P+D',
c=floor((D+g*m)/P),
```

则

```text
k'=k+c,  D'=D+g*m-c*P,  A(q')=-D' mod q'.
```

有限审计读数：

```text
terminal_phase_carry_orbit_closed=true
terminal_carry_atom_count_total=7
terminal_carry_transition_count_total=126
selected_terminal_transition_count=66
extra_transition_count=60
selected_terminal_A_wrap_count=49
selected_terminal_D_wrap_count=11
selected_terminal_A_wrap_fraction=49/66
selected_terminal_D_wrap_fraction=11/66
carry_identity_mismatch_count=0
prime_gap_carry_word_phase_saving_proved=false
```

selected terminal carry rows：

```text
P739,m=757: transitions=27, q_gap=[2,12], carry=[2,12], A_wrap=21/27, D_wrap=4/27
P739,m=761: transitions=27, q_gap=[2,12], carry=[2,13], A_wrap=20/27, D_wrap=5/27
P607,m=769: transitions=6,  q_gap=[2,8],  carry=[2,10], A_wrap=4/6,  D_wrap=1/6
P607,m=773: transitions=6,  q_gap=[2,8],  carry=[2,10], A_wrap=4/6,  D_wrap=1/6
```

外部 theorem 边界保持诚实：FKMS trace/bilinear、
Milićević--Qin--Wu arbitrary-modulus Kloosterman、Wright unbalanced
Kloosterman fractions 和 Pascadi composite Type-II 都需要 completed family、
可平均变量或 Type-II rectangle；当前对象只是有限 prime-gap/carry word。Li 的
`x^0.52` 短区间素数与 Maynard 小间距只给存在性或 gap 结构，不估计 carry-word
的 signed phase。

状态边界：

```text
terminal_phase_carry_orbit_closed=true
selected_terminal_carry_orbit_recurrence_closed=true
prime_gap_carry_word_phase_saving_proved=false
extra_carry_orbit_absorption_proved=false
summable_family_created=false
trace_or_kloosterman_completion_ready=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65AL. Phi-LPF repeated-step packet-enclosure terminal phase-turn word 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_repeated_step_packet_enclosure_terminal_phase_turn_word_audit.py
data/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-turn-word-ledger.json
docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-turn-word-audit.json
docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-turn-word-audit.md
```

本层承接 65AK，把 carry orbit 的相位本身继续下钻。由于
`q>P/2` 且 `0<D<P`，每个边都有 two-lift 表示

```text
A(q)=lambda(q)*q-D(q),  lambda(q) in {1,2}.
```

有限审计进一步逐 transition 检查
`sign(A(q')/q'-A(q)/q)`。读数为：

```text
terminal_phase_turn_word_closed=true
terminal_phase_turn_transition_count_total=126
terminal_phase_turn_run_count_total=59
selected_terminal_transition_count=66
selected_terminal_positive_transition_count=17
selected_terminal_negative_transition_count=49
selected_terminal_phase_run_count=35
selected_terminal_phase_run_max_length=6
extra_transition_count=60
extra_positive_transition_count=27
extra_negative_transition_count=33
extra_phase_run_count=24
extra_phase_run_max_length=8
phase_direction_Awrap_mismatch_count=0
lift_identity_mismatch_count=0
zero_phase_delta_count=0
phase_turn_word_phase_saving_proved=false
```

结论是：在本 finite ledger 中，`A(q)/q` 的相位下降恰好等于 `A_wrap`，
相位上升恰好等于 no-wrap。selected terminal 的硬点因此从一般 carry word
进一步缩成 `66` 个 phase turns 的 A-wrap signed word：`49` 个 negative/A-wrap，
`17` 个 positive/no-wrap，分成 `35` 个单调 runs，最长 selected run 为 `6`。

外部 theorem 边界仍不变。FKMS、Milićević--Qin--Wu、Pascadi 与 Wright 型
trace/Kloosterman/Type-II 输入都需要 completed averaging family、可控 summation
变量或 Type-II box；Li 短区间素数和 Maynard 小间距不估计这个 finite
A-wrap phase-turn word 的 signed imbalance。

状态边界：

```text
terminal_phase_turn_word_closed=true
selected_terminal_phase_turn_word_closed=true
phase_turn_word_phase_saving_proved=false
extra_phase_turn_run_absorption_proved=false
summable_family_created=false
trace_or_kloosterman_completion_ready=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65AM. Phi-LPF repeated-step packet-enclosure terminal phase variation-budget 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_repeated_step_packet_enclosure_terminal_phase_variation_budget_audit.py
data/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-variation-budget-ledger.json
docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-variation-budget-audit.json
docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-variation-budget-audit.md
```

本层承接 65AL，把 phase-turn word 进一步压成 signed variation budget：

```text
total variation = positive variation + negative variation
net displacement = positive variation - negative variation
```

有限审计读数：

```text
terminal_phase_variation_budget_closed=true
terminal_phase_variation_transition_count_total=126
terminal_phase_variation_run_count_total=59
selected_terminal_transition_count=66
selected_terminal_phase_run_count=35
selected_terminal_phase_run_max_length=6
selected_terminal_positive_transition_count=17
selected_terminal_negative_transition_count=49
selected_terminal_positive_variation=8.261301579660
selected_terminal_negative_variation=9.717867552237
selected_terminal_total_variation=17.979169131897
selected_terminal_net_phase_displacement=-1.456565972578
extra_transition_count=60
extra_phase_run_count=24
extra_total_variation=14.109301881162
extra_net_phase_displacement=-0.907719323182
bad_atom_variation_identity_count=0
bad_role_variation_identity_count=0
phase_variation_budget_phase_saving_proved=false
```

外部 theorem 边界进一步明确：当前对象仍只是 finite variation ledger，不是
completed trace/bilinear sum、Kloosterman variable 或 Type-II box。FKMS、
Milićević--Qin--Wu、Pascadi、Wright 仍只可能在后续构造出 averaging family 后
使用。`arXiv:2601.00292` 的 Kloosterman-fraction 双线性形式已撤稿，本文只把它
记录为不可用边界，不作为输入。Li 短区间素数与 Maynard 小间距不估计 signed
variation imbalance。

状态边界：

```text
terminal_phase_variation_budget_closed=true
selected_terminal_variation_budget_closed=true
phase_variation_budget_phase_saving_proved=false
extra_variation_budget_absorption_proved=false
summable_family_created=false
trace_or_kloosterman_completion_ready=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65AG. Phi-LPF dominant sign-word repeated-step occurrence-splice affine-skeleton 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_repeated_step_occurrence_splice_affine_skeleton_audit.py
data/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-occurrence-splice-affine-skeleton-ledger.json
docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-occurrence-splice-affine-skeleton-audit.json
docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-occurrence-splice-affine-skeleton-audit.md
```

本层承接 65AF，把两条 same-atom occurrence splice 继续解析为同一个
left/right witness-pair 的仿射骨架：

```text
shared_witness_pair_affine_skeleton_ledger_closed=true
splice_count=2
splice_mass_total=40
distinct_witness_pair_count=1
shared_witness_pair=true
all_same_affine_deltas=true
affine_identity_offset_delta_equals_m_delta_minus_P_delta=true
coordinate_atom_recheck_closed=true
```

共享 witness-pair 与统一仿射差分为：

```text
P739_packet2842_q28_mpair_757_761 -> P607_packet1887_q7_mpair_769_773
P_delta=-132
q_delta=-21
packet_delta=-955
m_pair_delta=[12,12]
offset_delta=[144,144]
```

这把 occurrence-splice obstruction 进一步压缩为一个 one-pair affine
skeleton。外部 theorem 边界仍不变：FKMS、Milićević--Qin--Wu 与 Wright
型 trace/Kloosterman 平均输入需要可求和族；Maynard 小间距与 Li 短区间素数
不控制这种 fixed witness-pair affine skeleton。

状态边界：

```text
shared_witness_pair_affine_skeleton_ledger_closed=true
shared_witness_pair_affine_skeleton_uniform_bound_proved=false
summable_family_created=false
trace_or_kloosterman_completion_ready=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65P. Phi-LPF q-prefix single-P local template occurrence class 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_template_occurrence_class_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-template-occurrence-class-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-template-occurrence-class-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-template-occurrence-class-audit.md
```

本层继续下钻 `LocalOccurrenceMultiplicityUniformBound` 中真正有重数的部分。
上一层显示 `4915` 个 single-P local endpoint templates 中只有 `97` 个重复；
本层把这 `97` 个 occurrence-count 大于一的模板分成三类：

```text
single_P_local_template_occurrence_class_ledger_closed=true
repeated_template_count=97
repeated_template_edge_mass=872
repeated_template_edge_ratio=0.03259447538593802
single_packet_multi_m_repeated_template_count=78
single_packet_multi_m_repeated_edge_mass=720
multi_packet_repeated_template_count=17
multi_packet_repeated_edge_mass=136
single_packet_single_m_multi_cycle_template_count=2
single_packet_single_m_multi_cycle_edge_mass=16
unclassified_repeated_template_count=0
observed_repeated_templates_single_strip=true
repeated_template_packet_support_count_max=2
repeated_template_m_value_support_count_max=4
repeated_template_q_prefix_support_count_max=2
repeated_template_m_shell_support_count_max=2
```

这把 occurrence 门从一个单一黑箱进一步拆成：

```text
SinglePacketMultiMCollisionBound
AND MultiPacketDuplicateTransportBound
AND SinglePacketSingleMMultiCycleSuppression
AND RepeatedOccurrenceAggregationOrPDEC
```

外部前沿边界：FKMS、Milićević--Qin--Wu、Wright、Pascadi、
Shao--Shparlinski--Wijaya、Xu--Zhang 仍是平均型、双线性、参数型或集合变量
输入；它们不直接给出 width-one local repeated-template collision bound。Li 的
短区间素数存在结果也不估计 signed endpoint occurrence classes。

状态边界：

```text
single_P_local_template_occurrence_class_ledger_closed=true
single_packet_multi_m_collision_bound_proved=false
multi_packet_duplicate_transport_bound_proved=false
single_packet_single_m_multi_cycle_suppression_proved=false
repeated_occurrence_aggregation_or_pdec_closed=false
local_occurrence_multiplicity_uniform_bound_proved=false
local_template_multiplicity_uniform_bound_proved=false
single_P_slice_endpoint_packet_summation_closed=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65Q. Phi-LPF q-prefix single-P local same-packet multi-m gap 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_same_packet_multi_m_gap_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-same-packet-multi-m-gap-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-same-packet-multi-m-gap-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-same-packet-multi-m-gap-audit.md
```

本层继续下钻 `SinglePacketMultiMCollisionBound`。上一层显示 same-packet
multi-m repeated templates 为 `78` 个、质量 `720`；本层按 selected m-values
的整数 gap 与素数序号 gap 拆成：

```text
single_P_local_same_packet_multi_m_gap_ledger_closed=true
same_packet_multi_m_template_count=78
same_packet_multi_m_edge_mass=720
adjacent_prime_pair_collision_template_count=71
adjacent_prime_pair_collision_edge_mass=662
nonadjacent_prime_pair_collision_template_count=6
nonadjacent_prime_pair_collision_edge_mass=50
adjacent_prime_chain_collision_template_count=1
adjacent_prime_chain_collision_edge_mass=8
same_packet_multi_m_prime_index_gap_max=3
same_packet_multi_m_integer_gap_max=18
```

主导形状是相邻素数对 collision；整数 m-gap 主项为 `[4]` 与 `[2]`：

```text
integer_gap_[4]_edge_mass=316
integer_gap_[2]_edge_mass=296
prime_index_gap_[1]_edge_mass=662
```

最新 occurrence 门改写为：

```text
AdjacentPrimePairCollisionBound
AND NonAdjacentPrimePairCollisionBound
AND AdjacentPrimeChainCollisionBound
AND MultiPacketDuplicateTransportBound
AND SinglePacketSingleMMultiCycleSuppression
AND RepeatedOccurrenceAggregationOrPDEC
```

外部前沿边界：trace/Kloosterman 平均输入需要非局部求和变量；普通 prime-gap
信息不能控制 adjacent m-values 上的 signed template equality；短区间素数存在
结果不估计 same-packet signed collision classes。

状态边界：

```text
single_P_local_same_packet_multi_m_gap_ledger_closed=true
adjacent_prime_pair_collision_bound_proved=false
nonadjacent_prime_pair_collision_bound_proved=false
adjacent_prime_chain_collision_bound_proved=false
same_packet_multi_m_collision_bound_proved=false
local_occurrence_multiplicity_uniform_bound_proved=false
single_P_slice_endpoint_packet_summation_closed=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65R. Phi-LPF q-prefix single-P local adjacent-prime-pair exact-gap 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_adjacent_prime_pair_gap_class_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-adjacent-prime-pair-gap-class-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-adjacent-prime-pair-gap-class-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-adjacent-prime-pair-gap-class-audit.md
```

上一层把 same-packet multi-m 主量压到相邻素数对 collision：

```text
adjacent_prime_pair_template_count=71
adjacent_prime_pair_edge_mass=662
```

本层继续按精确整数素数间隔分类：

```text
gap2_twin_adjacent_pair_template_count=33
gap2_twin_adjacent_pair_edge_mass=296
gap4_cousin_adjacent_pair_template_count=31
gap4_cousin_adjacent_pair_edge_mass=316
gap6_sexy_adjacent_pair_template_count=5
gap6_sexy_adjacent_pair_edge_mass=36
gap_ge8_adjacent_pair_template_count=2
gap_ge8_adjacent_pair_edge_mass=14
bad_adjacent_pair_template_count=0
observed_gap2_or_gap4_edge_ratio=0.9244712990936556
```

因此 `AdjacentPrimePairCollisionBound` 被实际拆成：

```text
Gap2TwinAdjacentPairCollisionBound
AND Gap4CousinAdjacentPairCollisionBound
AND Gap6SexyAdjacentPairCollisionBound
AND GapGe8AdjacentPairCollisionBound
```

外部 theorem 匹配边界：

```text
FKMS 2025 trace bilinear estimates:
  useful only after nonlocal trace-family completion; not a fixed-packet
  adjacent-pair equality theorem.

Milićević--Qin--Wu 2025 arbitrary-modulus Kloosterman sums:
  useful for completed bilinear Kloosterman inputs; not a local gap-2/gap-4
  signed template collision bound.

Wright 2026 unbalanced Kloosterman fractions:
  useful as an average reciprocal-fraction input; not pointwise for one
  endpoint packet.

Maynard small prime gaps and Li short-interval primes:
  give prime-gap or prime-existence information, but do not estimate equality
  of Phi-LPF signed templates across adjacent m-pairs.
```

状态边界：

```text
single_P_local_adjacent_prime_pair_gap_class_ledger_closed=true
adjacent_prime_pair_collision_bound_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65S. Phi-LPF q-prefix single-P local gap2/gap4 route-superclass 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_route_superclass_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-route-superclass-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-route-superclass-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-route-superclass-audit.md
```

上一层显示相邻素数对 collision 主量集中在 gap 2 与 gap 4：

```text
gap2_twin_adjacent_pair_edge_mass=296
gap4_cousin_adjacent_pair_edge_mass=316
observed_gap2_or_gap4_edge_mass=612
```

本层继续按几何 route-superclass 分类：

```text
single_P_local_gap2_gap4_route_superclass_ledger_closed=true
gap2_gap4_template_count=64
gap2_gap4_edge_mass=612
gap2_wing_template_count=32
gap2_wing_edge_mass=290
gap2_right_tail_template_count=1
gap2_right_tail_edge_mass=6
gap4_right_tail_template_count=28
gap4_right_tail_edge_mass=288
gap4_wing_template_count=3
gap4_wing_edge_mass=28
dominant_aligned_edge_mass=578
dominant_aligned_edge_ratio=0.9444444444444444
```

因此 gap 2/gap 4 的两个主门被实际拆成：

```text
Gap2WingTwinAdjacentPairCollisionBound
AND Gap2RightTailTwinResidualCollisionBound
AND Gap4RightTailCousinAdjacentPairCollisionBound
AND Gap4WingCousinResidualCollisionBound
```

外部 theorem 匹配边界没有变化：trace/Kloosterman 输入需要非局部 completion；
Maynard 小间隔与 Li 短区间结果只给 prime-gap/prime-existence 信息，不给固定
endpoint packet 的 signed route-superclass equality。

状态边界：

```text
single_P_local_gap2_gap4_route_superclass_ledger_closed=true
gap2_wing_twin_collision_bound_proved=false
gap4_right_tail_cousin_collision_bound_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65T. Phi-LPF q-prefix single-P local gap2/gap4 exact route-class 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_exact_route_class_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-exact-route-class-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-exact-route-class-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-exact-route-class-audit.md
```

上一层把 gap 2/gap 4 主量压成四个 route-superclass carrier。本层继续拆到 exact route class：

```text
single_P_local_gap2_gap4_exact_route_class_ledger_closed=true
gap2_gap4_template_count=64
gap2_gap4_edge_mass=612
gap4_right_tail_two_sided_edge_mass=258
gap2_upper_wing_edge_mass=212
gap2_lower_wing_edge_mass=78
gap4_right_tail_left_collar_edge_mass=30
gap4_upper_wing_edge_mass=22
gap2_right_tail_two_sided_edge_mass=6
gap4_lower_wing_edge_mass=6
top_two_route_edge_mass=470
top_two_route_edge_ratio=0.7679738562091504
residual_route_edge_mass=142
residual_route_edge_ratio=0.23202614379084968
```

因此 route-superclass 门继续被替换为 exact-route 门：

```text
Gap2UpperWingTwinCollisionBound
AND Gap2LowerWingTwinCollisionBound
AND Gap2RightTailTwoSidedTwinResidualCollisionBound
AND Gap4RightTailTwoSidedCousinCollisionBound
AND Gap4RightTailLeftCollarCousinCollisionBound
AND Gap4UpperWingCousinResidualCollisionBound
AND Gap4LowerWingCousinResidualCollisionBound
```

外部 theorem 匹配边界仍不变：trace/Kloosterman 平均型输入、Maynard 小间隔素数定理与
Li 短区间素数存在性都不直接估计固定 endpoint packet 中的 signed exact-route equality。

状态边界：

```text
single_P_local_gap2_gap4_exact_route_class_ledger_closed=true
gap2_upper_wing_twin_collision_bound_proved=false
gap4_right_tail_two_sided_cousin_collision_bound_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65U. Phi-LPF q-prefix single-P local gap2/gap4 top-two sign-cycle 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_top_two_sign_cycle_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-sign-cycle-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-sign-cycle-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-sign-cycle-audit.md
```

上一层显示两个最大 exact routes 是 `gap4 right-tail two-sided` 与 `gap2 upper wing`。
本层只处理这两口：

```text
top_two_exact_route_sign_cycle_ledger_closed=true
top_two_exact_route_template_count=48
top_two_exact_route_edge_mass=470
gap4_right_tail_two_sided_edge_mass=258
gap2_upper_wing_edge_mass=212
all_top_two_templates_pairwise_occurrence=true
occurrence_count_gt2_edge_mass=0
all_top_two_templates_mixed_positive_negative=true
all_positive_edge_mass=0
cycle_length_min=2
cycle_length_max=8
sign_switch_count_max=6
cycle_4_5_6_edge_mass=362
sign_switch_le3_edge_mass=332
cycle_4_5_6_and_switch_le3_edge_mass=270
```

外部 theorem 边界继续保持：trace/Kloosterman 输入需要先把这些局部 sign-cycle words
完成到可估计双线性族；prime-gap 与 short-interval prime theorem 不识别 signed word
或 fixed packet cycle carrier。

状态边界：

```text
top_two_exact_route_sign_cycle_ledger_closed=true
gap4_right_tail_two_sided_sign_cycle_bound_proved=false
gap2_upper_wing_sign_cycle_bound_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65V. Phi-LPF q-prefix single-P local gap2/gap4 top-two core route-cycle-switch 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_top_two_core_route_cycle_switch_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-route-cycle-switch-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-route-cycle-switch-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-route-cycle-switch-audit.md
```

上一层留下的最集中核心为：

```text
cycle_length in {4,5,6}
sign_switch_count <= 3
edge_mass=270
```

本层把该核心继续拆成 `route x cycle_length x sign_switch_count` 原子：

```text
top_two_core_route_cycle_switch_ledger_closed=true
core_template_count=29
core_edge_mass=270
noncore_top_two_edge_mass=200
route_cycle_switch_atom_count=11
largest_route_cycle_switch_atom_edge_mass=70
gap2_upper_wing_core_edge_mass=140
gap4_right_tail_two_sided_core_edge_mass=130
cycle5_core_edge_mass=150
cycle4_core_edge_mass=96
cycle6_core_edge_mass=24
sign_switch3_core_edge_mass=146
sign_switch1_core_edge_mass=64
sign_switch2_core_edge_mass=60
```

外部 theorem 边界仍不变：trace/Kloosterman 平均输入只有在这些局部 atom
被完成为可估计的双线性或 trace-family 对象后才可调用；prime-gap 与 short-interval
prime theorem 不直接控制 fixed endpoint packet 内的 signed atom equality。

状态边界：

```text
top_two_core_route_cycle_switch_ledger_closed=true
core_route_cycle_switch_collision_bound_proved=false
largest_core_atom_collision_bound_proved=false
top_two_noncore_residual_bound_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65W. Phi-LPF q-prefix single-P local gap2/gap4 top-two core largest-atom template-witness 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_top_two_core_largest_atom_template_witness_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-template-witness-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-template-witness-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-template-witness-audit.md
```

上一层最大 core atom 为：

```text
route=gap4_right_tail_two_sided
cycle_length=5
sign_switch_count=3
edge_mass=70
```

本层把该最大 atom 拆成 7 个等质量模板见证：

```text
largest_atom_template_witness_ledger_closed=true
witness_template_count=7
witness_edge_mass=70
all_witness_edge_mass_equals_10=true
distinct_sign_word_count=5
dominant_sign_word=--+-+
dominant_sign_word_edge_mass=30
q_prefix_band_q_le_10_edge_mass=30
q_prefix_band_q_le_20_edge_mass=10
q_prefix_band_q_gt_20_edge_mass=30
m_shell_band_m_le_4_edge_mass=30
m_shell_band_m_le_8_edge_mass=40
```

外部 theorem 边界仍不变：FKMS trace bilinear、Milićević--Qin--Wu
arbitrary-modulus Kloosterman 与 Wright unbalanced Kloosterman inputs 需要先有
local witness 到双线性/trace family 的 completion；Li `x^0.52` 短区间输入仍不触及
`theta=1/2` fixed endpoint witness。

状态边界：

```text
largest_atom_template_witness_ledger_closed=true
largest_atom_template_family_bound_proved=false
dominant_sign_word_family_bound_proved=false
all_seven_witness_families_bound_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65X. Phi-LPF q-prefix single-P local gap2/gap4 top-two core largest-atom dominant sign-word path 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_top_two_core_largest_atom_dominant_sign_word_path_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-dominant-sign-word-path-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-dominant-sign-word-path-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-dominant-sign-word-path-audit.md
```

上一层最大 atom 的 dominant sign word 为 `--+-+`，质量 `30`。本层把它继续拆成
3 个路径见证：

```text
dominant_sign_word_path_ledger_closed=true
target_sign_word=--+-+
path_template_count=3
path_edge_mass=30
all_path_edge_mass_equals_10=true
all_path_occurrence_count_equals_2=true
all_path_integer_gap_equals_4=true
all_path_m_shell_band_m_le_4=true
all_path_sign_balance_plus2_minus3=true
distinct_raw_base_template_count=3
distinct_signed_child_count=3
distinct_m_pair_count=2
dominant_m_pair=[769, 773]
dominant_m_pair_edge_mass=20
q_prefix_band_q_le_10_edge_mass=20
q_prefix_band_q_gt_20_edge_mass=10
```

外部 theorem 边界仍不变：trace/Kloosterman 平均型输入需要从这 3 个路径见证
完成到非局部双线性或 trace-family；prime-gap 与短区间素数定理仍不直接估计
fixed endpoint signed path equality。

状态边界：

```text
dominant_sign_word_path_ledger_closed=true
dominant_sign_word_path_family_bound_proved=false
other_largest_atom_template_witness_family_bounds_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 59. Phi-LPF dynamic Ramanujan unit expansion 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_dynamic_ramanujan_unit_expansion_audit.py
data/prime-matrix-phi-lpf-qsupport-dynamic-ramanujan-unit-expansion-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-dynamic-ramanujan-unit-expansion-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-dynamic-ramanujan-unit-expansion-audit.md
```

本层继续从动态 primorial 单位类

```text
selected iff gcd(Q_odd,W_P)=1
```

下钻到 Ramanujan 加性字符正规形：

```text
1_{(n,W)=1}=phi(W)/W * sum_{d|W} mu(d)c_d(n)/phi(d)
c_d(n)=sum_{a mod d, (a,d)=1} e(a*n/d)
```

平方自由 `W_P` 上，该式等价于逐素数局部乘积；完全打开所有 `c_d`
后，模式数精确为：

```text
sum_{d|W_P} phi(d)=W_P
```

有限审计读数：

```text
max_prime=1009
row_count=76954
active_ramanujan_identity_row_count=56196
ramanujan_product_identity_checked_total=951378
ramanujan_product_identity_mismatch_total=0
ramanujan_divisor_sum_sample_checked_total=111
ramanujan_divisor_sum_sample_mismatch_total=0
primorial_unit_selected_total=299977
primorial_unit_rejected_total=651401
max_dynamic_primorial_modulus=200560490130
max_dynamic_primorial_prime_count=11
max_ramanujan_divisor_terms_per_candidate=2048
max_full_additive_character_modes_per_candidate=200560490130
```

外部前沿影响：Wright 2026、Milićević--Qin--Wu 2025 与 Pascadi 2025
仍可作为未来 Kloosterman/Type-II 组织的候选技术源，但它们没有直接处理
这个随 `P` 增长的 `W_P` Ramanujan 模式族；撤回的 `arXiv:2601.00292`
仍不可引用。

新的最新最窄口：

```text
DynamicRamanujanUnitExpansionToUsableKloostermanCompletionBridge
AND UniformRamanujanModeCancellationOrTruncation
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
dynamic_ramanujan_unit_expansion_closed=true
ramanujan_product_identity_globally_proved=true
full_additive_mode_count_ledger_closed=true
usable_kloosterman_completion_bridge_closed=false
uniform_ramanujan_mode_cancellation_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 60. Phi-LPF full Ramanujan spectrum obstruction 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_full_ramanujan_spectrum_obstruction_audit.py
data/prime-matrix-phi-lpf-qsupport-full-ramanujan-spectrum-obstruction-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-full-ramanujan-spectrum-obstruction-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-full-ramanujan-spectrum-obstruction-audit.md
```

本层继续处理上一节留下的：

```text
UniformRamanujanModeCancellationOrTruncation
```

结论是：精确 truncation 分支被关闭。对

```text
f_W(n)=1_{gcd(n,W_P)=1}
```

其加性 Fourier 系数为：

```text
fhat(a)=c_{W_P}(a)/W_P
c_W(a)=prod_{ell|W, ell|a}(ell-1) prod_{ell|W, ell not|a}(-1)
```

因为 `W_P` 平方自由，每个局部因子都是 `ell-1` 或 `-1`，所以每个
`a mod W_P` 的 Fourier 系数都非零。故精确重建需要全部 `W_P` 个模式，
任何 proper additive-mode truncation 都改变同对象 selector。

有限审计读数：

```text
max_prime=1009
P_value_count=165
max_full_additive_frequency_count=200560490130
max_ramanujan_divisor_terms=2048
max_sqrt_sieve_prime_count=11
max_l1_norm=27179089920/86822723
bad_frequency_count_total=0
bad_nonzero_frequency_total=0
bad_l1_formula_total=0
bad_l2_parseval_total=0
proper_exact_mode_truncation_possible_for_any_P=false
```

外部前沿影响：新增核对 Fouvry--Kowalski--Michel--Sawin 2025
`arXiv:2511.09459` 的 trace-function 双线性技术；它与 Wright 2026、
Milićević--Qin--Wu 2025、Pascadi 2025、Shao--Shparlinski--Wijaya 2024
一样，只有在本文 full `W_P` 动态谱被包装成可用 trace/Kloosterman/Type-II
系数族之后才可能接入。撤回的 `arXiv:2601.00292` 仍不可引用。

新的最新最窄口：

```text
DynamicFullRamanujanSpectrumToUsableKloostermanCompletionBridge
AND UniformCancellationAcrossFullDynamicRamanujanSpectrum
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
full_ramanujan_spectrum_obstruction_closed=true
additive_fourier_full_support_proved=true
exact_mode_truncation_rejected=true
full_spectrum_cancellation_closed=false
usable_kloosterman_completion_bridge_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 61. Phi-LPF conductor-stratified Ramanujan spectrum 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_conductor_stratified_ramanujan_spectrum_audit.py
data/prime-matrix-phi-lpf-qsupport-conductor-stratified-ramanujan-spectrum-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-conductor-stratified-ramanujan-spectrum-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-conductor-stratified-ramanujan-spectrum-audit.md
```

本层把 full `W_P` additive spectrum 按真实 additive conductor 分层。若：

```text
q=W_P/gcd(a,W_P),
```

则：

```text
c_W(a)/W = mu(q)*phi(W)/(W*phi(q)).
```

exact conductor `q` 层含 `phi(q)` 个 primitive 频率，因此每一层总 L1 质量为：

```text
phi(q) * phi(W)/(W*phi(q)) = phi(W)/W.
```

所以低 conductor 层并不自动承载主质量；丢弃高 conductor 层不是精确同对象截断。

有限审计读数：

```text
max_prime=1009
P_value_count=165
max_conductor_layer_count=2048
max_full_additive_frequency_count=200560490130
max_sqrt_sieve_prime_count=11
bad_frequency_count_total=0
bad_layer_l1_equality_total=0
bad_total_l1_formula_total=0
bad_total_l2_parseval_total=0
all_conductor_strata_nonempty_and_equal_l1=true
proper_conductor_layer_truncation_exact_possible_for_any_P=false
```

外部前沿影响：Wright 2026、Fouvry--Kowalski--Michel--Sawin 2025、
Milićević--Qin--Wu 2025、Pascadi 2025、Shao--Shparlinski--Wijaya 2024
仍只能作为未来输入。当前还缺把这些 conductor layers 组织成同对象
Kloosterman/trace-function/Type-II 系数族的桥。

新的最新最窄口：

```text
ConductorStratifiedSpectrumToKloostermanOrTraceFamilyBridge
AND UniformCancellationAcrossAllPrimorialConductorLayers
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
conductor_stratification_closed=true
equal_l1_mass_per_conductor_layer_proved=true
low_conductor_exact_truncation_rejected=true
uniform_conductor_layer_cancellation_closed=false
usable_kloosterman_or_trace_family_bridge_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 61A. Phi-LPF complementary conductor pair 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_complementary_conductor_pair_audit.py
data/prime-matrix-phi-lpf-qsupport-complementary-conductor-pair-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-complementary-conductor-pair-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-complementary-conductor-pair-audit.md
```

本层继续沿 Ramanujan conductor 分层下钻，检验互补对偶：

```text
q^vee=W_P/q.
```

它确实把低 conductor 层与高 conductor 层一一配对，并保留相同的整层 L1 质量：

```text
L1(q)=L1(q^vee)=phi(W_P)/W_P.
```

但这不是自动相位抵消。符号只满足：

```text
mu(q^vee)=mu(W_P)mu(q),
```

因此当 `omega(W_P)` 为偶数时互补对同号，当 `omega(W_P)` 为奇数时互补对异号。
即使在异号层，归一化配对核

```text
mu(q)c_q(n)/phi(q)+mu(q^vee)c_{q^vee}(n)/phi(q^vee)
```

也不恒为零；每个互补对都有显式非零见证。

有限审计读数：

```text
max_prime=1009
P_value_count=165
max_conductor_layer_count=2048
max_complementary_pair_count=1024
pair_count_total=32554
same_sign_P_count=85
opposite_sign_P_count=80
frequency_count_equal_pair_total=0
frequency_count_unequal_pair_total=32554
max_primitive_frequency_count_ratio_in_pair=30656102400
bad_low_high_balance_total=0
identity_zero_pair_total=0
all_low_high_complementary_pairs_balanced=true
all_pair_kernels_nonzero_somewhere=true
automatic_complementary_pair_cancellation_possible_for_any_P=false
```

外部前沿影响：Wright 2026、Fouvry--Kowalski--Michel--Sawin 2025、
Milićević--Qin--Wu 2025、Pascadi 2025、Shao--Shparlinski--Wijaya 2024
仍不能直接闭合；它们需要先把这些非零配对核包装成同对象的
Kloosterman/trace-function/Type-II 系数族。Dong--Robles--Zeindler 2026
撤回结论不能作为闭合输入。

新的最新最窄口：

```text
ComplementaryConductorPairPhaseMatchingOrTraceFamilyBridge
AND UniformCancellationAcrossComplementaryPrimorialConductorPairs
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
complementary_conductor_mass_duality_closed=true
complementary_conductor_sign_ledger_closed=true
automatic_complementary_pair_cancellation_rejected=true
uniform_complementary_pair_cancellation_closed=false
usable_kloosterman_or_trace_family_bridge_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 61B. Phi-LPF complementary pair radial tensor 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_complementary_pair_radial_tensor_audit.py
data/prime-matrix-phi-lpf-qsupport-complementary-pair-radial-tensor-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-complementary-pair-radial-tensor-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-complementary-pair-radial-tensor-audit.md
```

本层继续沿互补 conductor 对偶下钻。令：

```text
rho_l(n)=1 if l|n, else -1/(l-1).
```

则每个互补配对核有精确 local Ramanujan tensor 正规形：

```text
K_q(n)=mu(q)*prod_{l|q}rho_l(n)+mu(W_P/q)*prod_{l|W_P/q}rho_l(n).
```

因此 `K_q` 只依赖 `gcd(n,W_P)`，对单位群 `(Z/W_PZ)^*` 的乘法作用径向不变。
若 `q` 与 `W_P/q` 都非平凡，则把 divisibility states 按两侧切开后，
该矩阵为 two-cylinder sum，rank 精确为 `2`；只有端点互补对 `{1,W_P}`
为 rank `1`。

有限审计读数：

```text
max_prime=1009
P_value_count=165
pair_count_total=32554
rank_one_endpoint_pair_total=165
rank_two_nontrivial_pair_total=32389
max_complementary_pair_count=1024
max_rank_two_nontrivial_pair_count=1023
radial_bad_total=0
reciprocal_phase_present_total=0
all_pair_kernels_unit_orbit_radial=true
all_nonendpoint_pairs_rank_two=true
direct_kloosterman_trace_input_available_for_any_pair=false
```

外部前沿影响：Fouvry--Kowalski--Michel--Sawin 2025/2026 的 trace-function
双线性估计、Milićević--Qin--Wu 2025 任意模 Kloosterman 双线性估计、
Pascadi 2025 复合模非交换放大、Wright 2026 Kloosterman fractions/unbalanced
convolution、Shao--Shparlinski--Wijaya 2024 squarefree/smooth 模数估计，都还
需要先建立“radial 支撑核与 reciprocal/trace 相位的同对象耦合桥”。原始配对核
没有 modular inverse phase，不能直接作为这些定理的输入。

新的最新最窄口：

```text
RadialPairKernelToReciprocalTracePhaseCouplingBridge
AND UniformCancellationAcrossComplementaryPrimorialConductorPairsAfterCoupling
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
complementary_pair_local_tensor_normal_form_closed=true
complementary_pair_unit_orbit_radiality_closed=true
complementary_pair_two_cylinder_rank_ledger_closed=true
direct_kloosterman_trace_input_from_pair_kernel_rejected=true
radial_pair_to_reciprocal_trace_phase_bridge_closed=false
uniform_complementary_pair_cancellation_after_coupling_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 61C. Phi-LPF radial pair coupled phase 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_radial_pair_coupled_phase_audit.py
data/prime-matrix-phi-lpf-qsupport-radial-pair-coupled-phase-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-radial-pair-coupled-phase-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-radial-pair-coupled-phase-audit.md
```

本层把互补 radial pair kernel 与 actual q-support reciprocal phase 精确耦合。
固定 residual cofactor：

```text
m=r*beta, r>=7 prime, beta r-rough.
```

令 `Q_{P,k}(m)` 为 reverse window

```text
[max(P/2+1,floor(kP/m)+1), min(P-1,m,floor(((k+1)P-1)/m))]
```

中的唯一奇候选。则 actual phase atom 精确为：

```text
1_{gcd(Q_{P,k}(m),W_P)=1} * e(h*k*P/Q_{P,k}(m)).
```

同时单位类选择器可以按互补 conductor pair 分组：

```text
1_{gcd(Q,W_P)=1}
= phi(W_P)/W_P * sum_{unordered {d,W_P/d}} K_d(Q).
```

有限审计读数：

```text
max_prime=1009
row_count=76954
active_residual_row_count=52697
total_actual_phase_atoms=299977
total_coupled_selected_phase_atoms=299977
actual_phase_atoms_equal_coupled_phase_atoms=true
missing_actual_phase_atoms_total=0
extra_coupled_phase_atoms_total=0
windows_with_odd_candidate_total=951378
local_coupled_identity_checked_total=951378
local_coupled_identity_mismatch_total=0
paired_kernel_identity_sample_checked_total=27
paired_kernel_identity_sample_mismatch_total=0
max_complementary_pair_kernels_per_candidate=1024
max_full_ramanujan_divisor_terms_per_candidate=2048
max_full_additive_modes_per_candidate=200560490130
phase_denominator_is_floor_defined_Q_odd=true
direct_trace_or_kloosterman_family_available=false
```

外部前沿影响：Fouvry--Kowalski--Michel--Sawin 2025/2026、Milićević--Qin--Wu
2025、Pascadi 2025、Wright 2026、Shao--Shparlinski--Wijaya 2024 仍是后续候选
输入，但本层显示当前耦合后的分母是 floor-defined `Q_{P,k}(m)`，不是已经完成的
trace/Kloosterman 变量。Dong--Robles--Zeindler 2026 仍不可用。

新的最新最窄口：

```text
FloorRadialReciprocalPhaseToTraceFamilyBridge
AND UniformCancellationAcrossCoupledFloorRadialPairKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
radial_pair_coupled_phase_normal_form_closed=true
complementary_pair_grouped_ramanujan_selector_identity_closed=true
floor_denominator_phase_ledger_closed=true
direct_trace_family_from_coupled_floor_radial_phase_rejected=true
floor_radial_reciprocal_phase_to_trace_family_bridge_closed=false
uniform_cancellation_across_coupled_floor_radial_pair_kernels_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 61D. Phi-LPF q-support floor-cell radial support 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_floor_cell_radial_support_audit.py
data/prime-matrix-phi-lpf-qsupport-floor-cell-radial-support-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-floor-cell-radial-support-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-floor-cell-radial-support-audit.md
```

本层把上一轮的 floor-defined denominator 压回正向 q-cell 支撑。对

```text
Q_{P,k}(m)=least odd integer in
[max(P/2+1,floor(kP/m)+1), min(P-1,m,floor(((k+1)P-1)/m))]
```

有精确等价：

```text
Q_{P,k}(m)=q
iff
m in I_{P,k}(q)
I_{P,k}(q)=[max(P/2+1,q,floor(kP/q)+1),
            min(2P-1,floor(((k+1)P-1)/q))]
```

并且 selected atom 仍是同一个：

```text
1_{gcd(q,W_P)=1} * 1_{m in I_{P,k}(q)} * e(h*k*P/q).
```

有限审计读数：

```text
max_prime=1009
row_count=76954
active_residual_row_count=52697
total_actual_phase_atoms=299977
total_floor_cell_selected_terms=299977
total_reverse_selected_terms=299977
total_product_cell_residual_atoms=951378
total_reverse_odd_residual_atoms=951378
floor_cell_terms_equal_actual_phase_atoms=true
floor_cell_terms_equal_reverse_selected_terms=true
product_cell_atoms_equal_reverse_odd_atoms=true
product_cell_to_reverse_mismatch_total=0
reverse_to_product_cell_mismatch_total=0
bad_product_cell_window_size_total=0
bad_product_cell_odd_count_total=0
bad_reverse_window_size_total=0
bad_reverse_odd_count_total=0
bad_unit_q_not_prime_total=0
q_floor_cells_checked_total=12532624
max_product_cell_window_size=2
max_reverse_window_size=2
completed_trace_or_kloosterman_family_available=false
```

外部前沿影响：Fouvry--Kowalski--Michel--Sawin 2025/2026、Milićević--Qin--Wu
2025、Pascadi 2025、Wright 2026、Shao--Shparlinski--Wijaya 2024 仍只是在完成桥
之后可能可用；当前只是确定性 floor-cell 恒等式，不是 trace/Kloosterman
或 Type-II 相消输入。Dong--Robles--Zeindler 2026 撤回结论仍不可用。

新的最新最窄口：

```text
FloorCellRadialSupportToCompletedTraceFamilyBridge
AND UniformCancellationAcrossFloorCellsWithRadialPairKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
floor_denominator_cell_decomposition_closed=true
reverse_forward_floor_cell_equivalence_closed=true
floor_cell_radial_support_exact_reconstruction_closed=true
floor_cell_to_completed_trace_family_bridge_closed=false
uniform_cancellation_across_floor_cells_with_radial_pair_kernels_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 61E. Phi-LPF q-support floor-cell Type-II fiber obstruction 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_floor_cell_typeii_fiber_obstruction_audit.py
data/prime-matrix-phi-lpf-qsupport-floor-cell-typeii-fiber-obstruction-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-floor-cell-typeii-fiber-obstruction-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-floor-cell-typeii-fiber-obstruction-audit.md
```

本层检验 floor-cell 正规形是否已经足以直接喂给 Type-II/Kloosterman 外部定理。
检查的同对象纤维为：

```text
q -> m
m -> q
q -> (r,beta)
(q,r) -> beta
(q,beta) -> r
(r,beta) -> q
```

有限审计读数：

```text
max_prime=1009
row_count=76954
active_residual_row_count=52697
total_floor_cell_residual_atoms=951378
total_floor_cell_selected_terms=299977
q_floor_cells_checked_total=12532624
bad_product_cell_window_size_total=0
bad_product_cell_odd_count_total=0
max_product_cell_window_size=2
max_product_cell_odd_count=1
max_q_to_m_fiber=1
max_m_to_q_fiber=1
max_q_to_factor_pair_fiber=1
max_qr_to_beta_fiber=1
max_qbeta_to_r_fiber=1
max_rbeta_to_q_fiber=1
max_selected_q_to_m_fiber=1
max_selected_qr_to_beta_fiber=1
rows_with_long_same_object_fiber=0
same_object_long_fiber_available_for_any_row=false
direct_typeii_bilinear_fiber_available=false
direct_kloosterman_variable_available=false
phase_is_denominator_graph_phase_not_inverse_variable=true
```

外部前沿影响：FKMS trace-function 双线性、Milićević--Qin--Wu 任意模
Kloosterman 双线性、Pascadi 复合模 Type-II 放大、Wright unbalanced
Kloosterman fractions/convolution、Shao--Shparlinski--Wijaya smooth/squarefree
参数估计都仍需要一个真正的 same-object trace/Kloosterman/dispersion 嵌入。
floor-cell 本身给出的只是单点图纤维，不能直接作为长双线性变量。

新的最新最窄口：

```text
SameObjectAveragedGraphDispersionOrTraceEmbedding
AND UniformCancellationAcrossGraphSupportedRadialKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
floor_cell_same_object_fiber_singleton_ledger_closed=true
direct_floor_cell_typeii_completion_rejected=true
direct_kloosterman_variable_from_floor_cell_rejected=true
same_object_averaged_graph_dispersion_or_trace_embedding_closed=false
uniform_cancellation_across_graph_supported_radial_kernels_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 61F. Phi-LPF q-support row-averaged mixed-modulus graph 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_mixed_modulus_graph_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-mixed-modulus-graph-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-mixed-modulus-graph-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-mixed-modulus-graph-audit.md
```

本层沿 `SameObjectAveragedGraphDispersionOrTraceEmbedding` 继续下钻。把
所有 `1<=k<P` 行合并后，每条同对象边由 `(q,m)` 唯一决定：

```text
k=floor(q*m/P)
D=q*m-k*P=q*m mod P
e(h*k*P/q)=e(-h*D/q)
```

跨行平均确实恢复长纤维，但产生的是 mixed-modulus graph phase：相位分子
`D` 按模 `P` 取余，分母却是 `q`。

有限审计读数：

```text
max_prime=1009
P_value_count=165
total_row_averaged_residual_edges=951378
total_row_averaged_selected_edges=299977
previous_single_row_selected_edge_total=299977
row_averaged_selected_edges_match_previous_total=true
floor_cell_membership_mismatch_total=0
floor_cell_odd_candidate_mismatch_total=0
bad_floor_cell_odd_count_total=0
bad_zero_displacement_total=0
max_q_to_m_fiber=193
max_m_to_q_fiber=252
max_q_to_k_fiber=193
max_k_to_q_fiber=59
max_selected_q_to_m_fiber=192
max_selected_m_to_q_fiber=73
max_selected_q_to_k_fiber=192
max_selected_k_to_q_fiber=23
P_values_with_long_selected_q_fibers=155
trace_mod_q_conflict_residue_count_total=2811
trace_mod_q_conflict_q_count_total=767
P_values_with_trace_mod_q_conflict=129
first_trace_mod_q_conflict=P=83,q=47,m_mod_q=2,D_mod_q_values=[15, 34]
same_modulus_trace_family_available_directly=false
kloosterman_inverse_variable_available_directly=false
```

外部前沿影响：跨行平均给出了长纤维，但 FKMS trace-function 双线性、
Milićević--Qin--Wu 任意模 Kloosterman、Pascadi composite Type-II、Wright
unbalanced Kloosterman fractions/convolution 与 Shao--Shparlinski--Wijaya
smooth/squarefree 参数估计仍不能直接套用；它们需要先把 mixed-modulus graph
phase 嵌入同模 trace/Kloosterman/dispersion 对象。

新的最新最窄口：

```text
MixedModulusRowAveragedGraphToTraceOrKloostermanEmbedding
AND UniformCancellationAcrossRowAveragedMixedModulusRadialGraph
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
row_averaged_qsupport_graph_normal_form_closed=true
row_averaging_long_fiber_gain_ledger_closed=true
mixed_modulus_phase_ledger_closed=true
direct_same_modulus_trace_embedding_from_row_average_closed=false
uniform_cancellation_across_row_averaged_mixed_modulus_radial_graph_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 61G. Phi-LPF q-support row-averaged additive-k support 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_support_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-support-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-support-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-support-audit.md
```

本层把上一轮 mixed-modulus phase 再压细一步。因为

```text
D=q*m-k*P
D == -k*P (mod q)
```

所以

```text
e(-hD/q)=e(h*P*k/q)
```

是模 `q` 上的 `k` 加性角色。相位重标记门闭合；但 q-bucket 内的
`k=floor(q*m/P)` 支撑由 residual LPF cofactor 集诱导，不是完整区间。

有限审计读数：

```text
max_prime=1009
P_value_count=165
total_selected_edges=299977
previous_row_averaged_selected_edges=299977
selected_edges_match_previous_total=true
selected_q_bucket_count_total=6020
phase_congruence_checked_total=299977
phase_congruence_mismatch_total=0
floor_cell_membership_mismatch_total=0
floor_cell_odd_candidate_mismatch_total=0
bad_floor_cell_odd_count_total=0
bad_zero_displacement_total=0
max_q_to_k_fiber=192
max_q_to_kmod_fiber=174
q_buckets_with_kmod_collision_total=1237
total_kmod_collision_edges=6664
q_buckets_with_noncomplete_k_interval_total=5920
total_k_support_count=299977
total_k_span_length=1602928
total_k_interval_holes=1302951
max_k_support_count_per_q=192
max_k_span_length_per_q=748
max_k_interval_holes_per_q=556
first_noncomplete_k_support=P=43,q=23,min_k=26,max_k=41,count=2,span=16,holes=14
additive_character_phase_relabeling_closed=true
complete_interval_additive_character_sum_available=false
sparse_lpf_k_support_completion_closed=false
```

外部前沿影响：相位现在可看成 `k mod q` 加性角色，但 FKMS trace-function、
Milićević--Qin--Wu Kloosterman、Pascadi Type-II、Wright unbalanced
convolution 与 Shao--Shparlinski--Wijaya smooth/squarefree 参数估计仍需先把
LPF 诱导的 sparse `k` 支撑完成或估计为可控 dispersion/convolution family。

新的最新最窄口：

```text
SparseLPFKSupportCompletionOrDispersion
AND UniformCancellationAcrossSparseKSupportRadialKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
mixed_modulus_phase_to_k_additive_character_relabeling_closed=true
row_averaged_selected_edge_consistency_closed=true
direct_complete_interval_additive_character_completion_rejected=true
sparse_lpf_k_support_completion_or_dispersion_closed=false
uniform_cancellation_across_sparse_k_support_radial_kernels_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 61H. Phi-LPF q-support row-averaged additive-k completion tax 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_completion_tax_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-completion-tax-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-completion-tax-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-completion-tax-audit.md
```

本层继续选择 row/column Phi-LPF 的 additive-k 路线。若把真实支撑

```text
K_{P,q}={floor(q*m/P): m is a selected residual LPF cofactor}
```

补成完整区间 `[min K_{P,q}, max K_{P,q}]`，则完整区间精确分解为真实
sparse 支撑加 completion holes。每个 hole 的 product-cell 长度小于 2，
至多有一个奇候选；若这个奇候选是 residual LPF cofactor，则该 `k`
已经属于真实支撑。因此 hole correction 不是同对象项。

有限审计读数：

```text
max_prime=1009
P_value_count=165
selected_q_bucket_count_total=6020
real_k_count_total=299977
completion_span_total=1602928
completion_holes_total=1302951
completion_holes_match_previous_total=true
real_k_count_matches_previous_total=true
completion_span_matches_previous_total=true
completion_tax_ratio_total=4.343503
holes_without_odd_candidate_total=373676
holes_with_nonresidual_odd_candidate_total=929275
holes_with_residual_candidate_total=0
bad_odd_count_over_one_total=0
odd_candidate_prime_total=355919
odd_candidate_small_lpf_3_total=409713
odd_candidate_small_lpf_5_total=163643
odd_candidate_other_nonresidual_total=0
max_completion_holes_per_q=556
max_completion_tax_ratio_per_q=11.500000
first_completion_hole=P=43,q=23,k=27,I=[51,52],m=51,class=odd_candidate_small_lpf_3
residual_candidate_holes_absent=true
complete_interval_replacement_object_preserving=false
completion_correction_control_closed=false
```

外部前沿影响：FKMS trace-function、Milićević--Qin--Wu 任意模 Kloosterman、
Pascadi composite Type-II、Wright unbalanced convolution/Kloosterman fractions
和 Shao--Shparlinski--Wijaya smooth/squarefree Kloosterman 参数估计，都仍不能
直接吞掉这个 completion correction。它包含无奇候选、prime 候选以及小 LPF
候选，必须先证明 correction cancellation/absorption 或保持 sparse 支撑直接做
dispersion。

新的最新最窄口：

```text
CompletionCorrectionCancellationOrAbsorptionForSparseLPFKSupport
AND UniformCancellationAcrossSparseKSupportRadialKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
sparse_k_completion_tax_ledger_closed=true
residual_candidate_hole_exclusion_closed=true
direct_complete_interval_object_preservation_closed=false
completion_correction_control_closed=false
uniform_cancellation_across_sparse_k_support_radial_kernels_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 61I. Phi-LPF q-support row-averaged additive-k completion correction phase 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_completion_correction_phase_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-completion-correction-phase-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-completion-correction-phase-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-completion-correction-phase-audit.md
```

本层把 completion tax 推到相位层。对任意整数 `h`，真实 sparse 支撑相位和满足：

```text
S_K(h)=sum_{k in K_{P,q}} e(hPk/q)
S_C(h)=sum_{k=minK}^{maxK} e(hPk/q)
S_H(h)=sum_{k in H_{P,q}} e(hPk/q)
S_K(h)=S_C(h)-S_H(h)
```

其中 `S_C(h)` 是完整区间上的显式几何和。由于 `P` 在模 `q` 下可逆，
当 `h` 不被 `q` 整除时，

```text
S_C(h)=e(hP*minK/q)*(1-e(hP*(maxK-minK+1)/q))/(1-e(hP/q)).
```

因此完整区间相位部分已经闭合；真正剩余是 completion-hole correction
`S_H(h)` 的相消或吸收。

有限审计读数（`h=1` 用于幅度诊断；符号恒等式对所有 `h` 成立）：

```text
max_prime=1009
P_value_count=165
q_bucket_count_total=6020
real_k_count_total=299977
complete_span_total=1602928
hole_count_total=1302951
phase_identity_counts_match_completion_tax=true
geometric_formula_verified=true
correction_phase_identity_verified=true
max_geometric_formula_error=3.329e-11
max_correction_identity_error=1.641e-13
sum_abs_sparse_sum_h1=53897.476591
sum_abs_complete_geometric_sum_h1=12232.215742
sum_abs_hole_correction_sum_h1=56664.077674
max_abs_complete_geometric_sum_h1=158.704702
max_abs_hole_correction_sum_h1=118.782265
max_hole_over_complete_abs_ratio_h1=4699.709076
hole_abs_gt_complete_abs_bucket_count_h1=5150
sparse_abs_gt_complete_abs_bucket_count_h1=5000
complete_near_zero_with_nonzero_hole_bucket_count_h1=10
hole_label_no_odd_candidate_total=373676
hole_label_odd_candidate_prime_total=355919
hole_label_odd_candidate_small_lpf_3_total=409713
hole_label_odd_candidate_small_lpf_5_total=163643
hole_label_residual_candidate_total=0
first_hole_dominates_complete=P=43,q=23,holes=14,abs_complete=0.677199,abs_hole=1.304173,abs_sparse=1.981372
complete_interval_geometric_part_closed=true
hole_correction_phase_control_closed=false
```

外部前沿影响：完整区间部分不再需要 FKMS trace-function、Milićević--Qin--Wu
任意模 Kloosterman、Pascadi composite Type-II、Wright unbalanced
convolution/Kloosterman fractions 或 Shao--Shparlinski--Wijaya smooth/squarefree
参数估计；它已经是初等几何和。上述外部结果若要进入，必须作用在
`S_H` 的 no-odd/prime/small-LPF hole correction 上，或绕过 completion
直接给 sparse 支撑相消。

新的最新最窄口：

```text
HoleCorrectionPhaseCancellationOrAbsorptionForNoOddPrimeSmallLPFCells
AND UniformCancellationAcrossSparseKSupportRadialKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
complete_interval_geometric_phase_closed=true
sparse_support_minus_hole_correction_identity_closed=true
hole_correction_phase_control_closed=false
uniform_cancellation_across_sparse_k_support_radial_kernels_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 61J. Phi-LPF q-support row-averaged additive-k hole-class phase decomposition 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_hole_class_phase_decomposition_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-class-phase-decomposition-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-class-phase-decomposition-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-class-phase-decomposition-audit.md
```

本层把上一节的 completion-hole correction `S_H` 继续拆成局部相位包。每个
hole 的 product-cell 长度 `<2`，所以它要么是 empty cell，要么是 even
singleton，要么有唯一奇候选 `m`。若这个奇候选是奇合数且 `LPF(m)>=7`，
则写作 `m=r*beta` 后自动满足 `beta>=r` 且 `LPF(beta)>=r`，因此它就是
residual LPF cofactor，不可能是 hole。于是奇候选 hole 只能是：

```text
prime candidate
LPF=3 candidate
LPF=5 candidate
```

因此

```text
S_H = S_empty + S_even + S_prime + S_lpf3 + S_lpf5
```

是精确同对象 correction 分解。

有限审计读数（`h=1` 相位诊断）：

```text
max_prime=1009
P_value_count=165
q_bucket_count_total=6020
hole_count_total=1302951
classified_hole_count_total=1302951
counts_match_previous_correction_phase=true
hole_class_identity_verified=true
max_class_identity_error=9.664e-14
forbidden_class_count_total=0
only_empty_even_prime_lpf3_lpf5_classes_seen=true
count_empty_cell_total=0
count_even_singleton_total=373676
count_odd_candidate_prime_total=355919
count_odd_candidate_lpf3_total=409713
count_odd_candidate_lpf5_total=163643
sum_abs_empty_cell_sum_h1=0.000000
sum_abs_even_singleton_sum_h1=178003.033657
sum_abs_odd_candidate_prime_sum_h1=61696.864692
sum_abs_odd_candidate_lpf3_sum_h1=65968.241426
sum_abs_odd_candidate_lpf5_sum_h1=30865.060099
dominant_hole_phase_class_bucket_counts_h1={"even_singleton":5166,"none":100,"odd_candidate_lpf3":200,"odd_candidate_lpf5":189,"odd_candidate_prime":365}
class_phase_control_closed=false
```

外部前沿影响：FKMS trace-function、Milićević--Qin--Wu 任意模 Kloosterman、
Pascadi composite Type-II、Wright unbalanced convolution/Kloosterman fractions
与 Shao--Shparlinski--Wijaya smooth/squarefree Kloosterman 参数估计，仍需要先
把五类 packet 中的某一类嵌入 trace/Kloosterman/Type-II/convolution 支撑；
五类分解本身还不是相消定理。

新的最新最窄口：

```text
FiveClassHolePhaseCancellationOrAbsorption
AND UniformCancellationAcrossSparseKSupportRadialKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
hole_class_partition_closed=true
odd_hole_prime_or_small_lpf_reduction_closed=true
hole_class_phase_identity_closed=true
five_class_phase_control_closed=false
uniform_cancellation_across_sparse_k_support_radial_kernels_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 61K. Phi-LPF q-support row-averaged additive-k hole nonempty four-class reduction 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_hole_nonempty_four_class_reduction_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-nonempty-four-class-reduction-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-nonempty-four-class-reduction-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-nonempty-four-class-reduction-audit.md
```

本层继续下钻五类分解中的 `empty_cell` packet。固定 `P,q` 后，carrier
区间

```text
M_{P,q}=[max(P/2+1,q),2P-1]∩Z
```

上的映射 `m -> floor(qm/P)` 单调，且因为 `q<P`，相邻载体的 `k` 值增量
只能是 `0` 或 `1`。因此其像集没有中间缺口。既然真实 sparse 支撑
`K_{P,q}` 的 `minK` 与 `maxK` 都来自这个像集，则 `[minK,maxK]` 内每个
completion hole 都有至少一个载体整数 `m`；hole 不能是 empty cell。

所以 correction 恒等式从五类进一步压成四类：

```text
S_H = S_even + S_prime + S_lpf3 + S_lpf5
```

有限审计读数：

```text
max_prime=1009
P_value_count=165
q_bucket_count_total=6020
previous_q_bucket_count_total=6020
real_k_count_total=299977
previous_real_k_count_total=299977
hole_count_total=1302951
previous_hole_count_total=1302951
four_class_hole_count_total=1302951
carrier_gap_count_total=0
selected_span_missing_count_total=0
empty_hole_count_total=0
previous_empty_hole_count_total=0
forbidden_hole_count_total=0
max_carrier_fiber_size=2
counts_match_previous_hole_class_audit=true
carrier_floor_map_no_skip_verified=true
selected_span_nonempty_verified=true
empty_class_eliminated=true
four_class_reduction_closed=true
count_even_singleton_total=373676
count_odd_candidate_prime_total=355919
count_odd_candidate_lpf3_total=409713
count_odd_candidate_lpf5_total=163643
four_class_phase_control_closed=false
```

外部前沿影响：FKMS trace-function、Milićević--Qin--Wu 任意模 Kloosterman、
Pascadi composite Type-II、Wright 2026 unbalanced convolution/Kloosterman
fractions 与 Shao--Shparlinski--Wijaya smooth/squarefree Kloosterman 参数估计，
仍需要先把四类 packet 中的一类嵌入 trace/Kloosterman/Type-II/convolution
支撑。本层只删除空载体 packet，不提供四类 packet 的相消。

新的最新最窄口：

```text
FourClassHolePhaseCancellationOrAbsorption
AND UniformCancellationAcrossSparseKSupportRadialKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
carrier_floor_map_no_skip_closed=true
selected_span_nonempty_closed=true
empty_hole_class_eliminated=true
four_class_hole_phase_identity_closed=true
four_class_phase_control_closed=false
uniform_cancellation_across_sparse_k_support_radial_kernels_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 61L. Phi-LPF q-support row-averaged additive-k hole blocking-cofactor pushforward 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_hole_blocking_cofactor_pushforward_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-blocking-cofactor-pushforward-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-blocking-cofactor-pushforward-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-blocking-cofactor-pushforward-audit.md
```

本层把四类 completion-hole correction 从缺失 `k` 推到唯一 blocking cofactor
`m_h`。若 product-cell 有奇候选，则 residual LPF cofactor 只能落在这个唯一
奇候选上，所以 blocker 取该奇候选；若没有奇候选，则上一层 nonempty 定理
强制 cell 是偶 singleton，blocker 取该偶数。于是 blocker 的最小素因子只有
四种可能：

```text
LPF(m_h)=2, 3, 5, or m_h is prime
```

相位同时被推前为：

```text
e(hPk/q) = e(hP floor(q*m_h/P)/q).
```

因此四类 correction 可重写为两个来源：

```text
S_H = S_{30-wheel-blocker} + S_{prime-blocker}
```

其中第一项是 finite 30-wheel 小 LPF 阻塞包，第二项是 prime blocker 动态素性
包。

有限审计读数：

```text
max_prime=1009
P_value_count=165
q_bucket_count_total=6020
previous_q_bucket_count_total=6020
real_k_count_total=299977
previous_real_k_count_total=299977
hole_count_total=1302951
previous_hole_count_total=1302951
blocking_cofactor_count_total=1302951
small_lpf_blocker_count_total=947032
prime_blocker_count_total=355919
small_lpf_blocker_ratio=0.726836
prime_blocker_ratio=0.273164
count_blocker_lpf2_even_total=373676
count_blocker_lpf3_total=409713
count_blocker_lpf5_total=163643
count_blocker_prime_total=355919
bad_empty_total=0
bad_odd_multiplicity_total=0
bad_floor_mismatch_total=0
bad_residual_blocker_total=0
bad_class_mismatch_total=0
duplicate_blocker_m_total=0
total_bad_pushforward_count=0
max_pushforward_identity_error=9.334e-14
pushforward_identity_verified=true
counts_match_previous_four_class_reduction=true
unique_blocker_per_hole_verified=true
two_family_split_closed=true
sum_abs_small_lpf_blocker_sum_h1=104345.004183
sum_abs_prime_blocker_sum_h1=61696.864692
dominant_two_family_bucket_counts_h1={"prime_blocker":757,"small_lpf_blocker":5263}
two_family_phase_control_closed=false
```

外部前沿影响：FKMS trace-function、Milićević--Qin--Wu 任意模 Kloosterman、
Pascadi composite Type-II、Wright 2026 unbalanced convolution/Kloosterman
fractions 与 Shao--Shparlinski--Wijaya smooth/squarefree Kloosterman 参数估计，
仍不直接估计这个 floor blocker selector。它们需要先完成 blocker phase 到
trace/Kloosterman/Type-II/completed convolution 支撑的对象嵌入。

新的最新最窄口：

```text
TwoFamilyBlockerPhaseCancellationOrAbsorption
AND PrimeBlockerDynamicSqrtSieveOrTraceEmbedding
AND FiniteThirtyWheelSmallLPFBlockerPacketControl
AND UniformCancellationAcrossSparseKSupportRadialKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
unique_blocking_cofactor_closed=true
hole_phase_pushforward_closed=true
thirty_wheel_vs_prime_blocker_split_closed=true
two_family_phase_control_closed=false
prime_blocker_trace_embedding_closed=false
small_lpf_blocker_packet_control_closed=false
uniform_cancellation_across_sparse_k_support_radial_kernels_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 61M. Phi-LPF q-support row-averaged additive-k hole primorial escalation 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_hole_primorial_escalation_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-primorial-escalation-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-primorial-escalation-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-hole-primorial-escalation-audit.md
```

本层检验 `30 -> 210 -> 2310 -> ...` 在 blocker 正规形中是否仍有独立杀伤。
上一节已证明每个 blocker 满足：

```text
LPF(m_h) in {2,3,5} or m_h is prime.
```

因此 cutoff `y` 的 primorial wheel 对 blocker 的作用精确为：

```text
killed_y(m_h) iff LPF(m_h)<=y.
```

所以 `30-wheel` 已经删除全部小 LPF blocker；继续加入 `7,11,13,...` 不会
产生新的 rough-composite blocker shell。剩余 prime blocker 只有当 cutoff
达到该 prime blocker 本身时才会被删除。特别地，`sqrt(2P-1)<P/2<m_h`，
所以动态 sqrt wheel 与 `30-wheel` 在 blocker 上同效。

有限审计读数：

```text
max_prime=1009
P_value_count=165
blocker_count_total=1302951
small_lpf_blocker_count_total=947032
prime_blocker_count_total=355919
prime_blocker_min=53
prime_blocker_max=1987
prime_blocker_le_P_total=140983
prime_blocker_gt_P_total=214936
counts_match_previous_blocker_audit=true
thirty_wheel_kills_all_small_lpf_blockers=true
fixed_210_2310_and_beyond_new_rough_shell_count_total=0
fixed_primorial_extra_kills_over_30_total=0
sqrt_cutoff_killed_count=947032
sqrt_cutoff_extra_killed_over_30=0
sqrt_cutoff_same_as_30_verified=true
P_cutoff_prime_killed_total=140983
P_cutoff_prime_survived_total=214936
full_2P_minus_1_cutoff_closes_all=true
full_2P_minus_1_cutoff_is_prime_oracle=true
nonoracle_primorial_escalation_closes_target=false
```

primorial cutoff 摘要：

```text
W_5=30: killed=947032, survived=355919, prime_killed=0
W_7=210: killed=947032, survived=355919, prime_killed=0
W_11=2310: killed=947032, survived=355919, prime_killed=0
W_31=200560490130: killed=947032, survived=355919, prime_killed=0
W_sqrt(2P-1): killed=947032, survived=355919, prime_killed=0
W_P: killed=1088015, survived=214936, prime_killed=140983
W_{2P-1}: killed=1302951, survived=0, prime_killed=355919
```

外部前沿影响：FKMS trace-function、Milićević--Qin--Wu 任意模 Kloosterman、
Pascadi composite Type-II、Wright 2026 unbalanced convolution/Kloosterman
fractions 与 Shao--Shparlinski--Wijaya smooth/squarefree Kloosterman 参数估计，
仍可能是 prime-blocker 非轮筛相位控制的候选输入；但单纯 primorial 升级不
产生可交给这些定理的新 composite shell。

新的最新最窄口：

```text
PrimeBlockerNonWheelPhaseSavingOrTraceEmbedding
AND NonOracleControlOfPrimeBlockerDynamicSqrtSieve
AND FiniteThirtyWheelSmallLPFBlockerPacketControl
AND UniformCancellationAcrossSparseKSupportRadialKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
primorial_cutoff_action_closed=true
no_new_rough_composite_shell_after_30_closed=true
sqrt_primorial_equals_30_on_blockers_closed=true
nonoracle_primorial_escalation_closes_target=false
prime_blocker_trace_embedding_closed=false
small_lpf_blocker_packet_control_closed=false
uniform_cancellation_across_sparse_k_support_radial_kernels_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 61N. Phi-LPF q-support row-averaged additive-k prime-blocker dynamic sqrt-sieve 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_blocker_dynamic_sqrt_sieve_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-blocker-dynamic-sqrt-sieve-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-blocker-dynamic-sqrt-sieve-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-blocker-dynamic-sqrt-sieve-audit.md
```

本层把上一节留下的 `prime blocker` 从素性黑箱改写为逐点动态
`sqrt(m_h)` 筛幸存者。对每个 blocker：

```text
m_h is prime  iff  m_h mod ell != 0 for every prime ell<=sqrt(m_h)
S_{prime-blocker}=S_{sqrt-sieve-survivor}
```

有限审计读数：

```text
max_prime=1009
blocker_count_total=1302951
small_lpf_blocker_count_total=947032
prime_blocker_count_total=355919
sqrt_sieve_survivor_count_total=355919
sqrt_sieve_rejected_count_total=947032
total_bad_dynamic_sqrt_sieve_count=0
q_bucket_prime_phase_mismatch_count=0
max_prime_packet_phase_identity_error=0
obstruction_counts={2:373676,3:409713,5:163643,none:355919}
max_pi_sqrt_prime_blocker=14
max_mobius_terms_per_blocker=16384
prime_blocker_full_sqrt_tests_total=3373946
prime_blocker_mobius_terms_full_expansion_total=399176624
```

逐层 cutoff 显示 `5` 之后没有新拒绝：

```text
cutoff=2: rejected=373676, survived=929275
cutoff=3: rejected=783389, survived=519562
cutoff=5: rejected=947032, survived=355919
cutoff=7,11,...,43: rejected=947032, survived=355919
```

外部前沿影响：FKMS trace-function bilinear、Milićević--Qin--Wu 任意模
Kloosterman、Pascadi composite Type-II、Wright 2026 unbalanced convolution
与 Shao--Shparlinski--Wijaya smooth/squarefree Kloosterman 估计仍是候选工具，
但只有在 moving survivor packet 被真正嵌入 completed trace/Type-II/convolution
对象后才可使用。Runbo Li 的 `x^0.52` 短区间素数输入仍高于点态 `theta=1/2`
尺度，不能直接闭合该 packet。

新的最新最窄口：

```text
PrimeBlockerSqrtSieveSurvivorPhaseSavingOrTraceEmbedding
AND MovingPrimorialMobiusExpansionCompression
AND FiniteThirtyWheelSmallLPFBlockerPacketControl
AND UniformCancellationAcrossSparseKSupportRadialKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
prime_blocker_dynamic_sqrt_sieve_identity_closed=true
prime_blocker_phase_packet_pushforward_closed=true
no_rough_composite_sqrt_rejection_after_30_closed=true
moving_primorial_mobius_compression_closed=false
prime_blocker_survivor_phase_saving_closed=false
small_lpf_blocker_packet_control_closed=false
uniform_cancellation_across_sparse_k_support_radial_kernels_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 61O. Phi-LPF q-support row-averaged additive-k prime-blocker Mobius involution 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_blocker_mobius_involution_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-blocker-mobius-involution-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-blocker-mobius-involution-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-blocker-mobius-involution-audit.md
```

本层把 moving sqrt-sieve survivor 的 Mobius 展开继续拆开：

```text
1_prime(m_h)=sum_{d|m_h,d|W(m_h)} mu(d)
W(m_h)=prod_{ell<=sqrt(m_h)} ell
```

若 blocker 是小 LPF 合数，令 `s` 为第一个阻碍素数，则 squarefree divisor
项按 Euler involution：

```text
d <-> s*d
```

成对抵消。若 blocker 是 prime survivor，则没有非平凡 divisor 项，只剩
`d=1` 单层。

有限审计读数：

```text
max_prime=1009
blocker_count_total=1302951
small_lpf_blocker_count_total=947032
prime_blocker_count_total=355919
mobius_survivor_weight_total=355919
active_divisor_terms_total=4321483
prime_singleton_terms_total=355919
composite_cancelled_terms_total=3965564
composite_involution_pair_count_total=1982782
previous_prime_blocker_mobius_terms_full_expansion_total=399176624
active_terms_vs_previous_formal_ratio=0.01082599
max_basis_size=4
max_active_terms=16
total_bad_mobius_involution_count=0
max_mobius_packet_phase_identity_error=0
```

分桶读数：

```text
basis_size_counts={0:355919,1:457984,2:268999,3:193398,4:26651}
first_obstruction_counts={2:373676,3:409713,5:163643,none:355919}
```

外部前沿影响：FKMS trace-function bilinear、Milićević--Qin--Wu 任意模
Kloosterman、Pascadi composite Type-II、Wright 2026 unbalanced convolution
与 Shao--Shparlinski--Wijaya smooth/squarefree Kloosterman 估计仍不能直接作用
于这个点态 involution。它们仍需要把 prime survivor singleton layer 嵌入
completed trace/Type-II/convolution 对象。Runbo Li 的 `x^0.52` 短区间输入仍
没有达到点态 `theta=1/2`。

新的最新最窄口：

```text
PrimeSurvivorSingletonLayerPhaseSavingOrTraceEmbedding
AND NonPointwiseCompressionBeyondEulerMobiusInvolution
AND FiniteThirtyWheelSmallLPFBlockerPacketControl
AND UniformCancellationAcrossSparseKSupportRadialKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
moving_mobius_divisor_expansion_identity_closed=true
euler_involution_cancels_rejected_blockers_closed=true
prime_survivor_singleton_layer_reduction_closed=true
moving_mobius_expansion_self_compression_phase_saving_closed=false
prime_survivor_singleton_layer_phase_saving_closed=false
small_lpf_blocker_packet_control_closed=false
uniform_cancellation_across_sparse_k_support_radial_kernels_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 61P. Phi-LPF q-support row-averaged additive-k prime-survivor floor-span completion 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_floor_span_completion_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-floor-span-completion-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-floor-span-completion-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-floor-span-completion-audit.md
```

本层承接 61O：Mobius involution 后唯一剩余的 `d=1` prime survivor
singleton layer，可按每个活动 `(P,q)` 桶写成 prime interval floor-span：

```text
M_prime(P,q)={prime m in [L_{P,q},U_{P,q}]} \ {P}
S_prime-survivor=sum_q sum_{m prime in [L_q,U_q],m!=P} e(hP floor(qm/P)/q)
```

其中 `m=P` 对应 `k=q,D=0`，不是 blocker；若把 span 中的素数补全，必须把
这个 diagonal ghost 显式扣除。

有限审计读数：

```text
max_prime=1009
prime_survivor_edge_count_total=355919
q_bucket_count_total=5848
span_prime_count_total=361626
raw_missing_count_total=5707
raw_extra_count_total=0
diagonal_ghost_count_total=5707
bucket_with_only_diagonal_ghost_count=5707
bucket_with_no_raw_missing_count=141
expected_missing_after_diagonal_subtraction_total=0
expected_extra_after_diagonal_subtraction_total=0
total_bad_prime_survivor_floor_span_count=0
max_span_completion_phase_error=1.421e-14
```

完整 prime-prime rectangle 仍不可直接使用：

```text
q_eligible_prime_count_total=6115
m_eligible_prime_count_without_diagonal_total=17299
full_prime_prime_rectangle_edge_count_without_diagonal_total=849334
prime_survivor_to_full_rectangle_without_diagonal_density=0.41905658
dense_rectangle_completion_missing_edge_count_without_diagonal=493415
full_prime_prime_rectangle_completion_available_directly=false
```

外部前沿影响：FKMS trace-function bilinear、Milićević--Qin--Wu 任意模
Kloosterman、Pascadi composite Type-II、Wright 2026 unbalanced convolution
与 Shao--Shparlinski--Wijaya smooth/squarefree Kloosterman 估计仍只是在把该
floor-span graph 嵌入 completed trace/Type-II/convolution 对象后才可用。
Runbo Li 的 `x^0.52` 短区间输入仍未达到点态 `theta=1/2`。

新的最新最窄口：

```text
PrimeSurvivorPrimeIntervalFloorSpanPhaseSavingOrTraceEmbedding
AND DiagonalPGhostSubtractionDiscipline
AND DenseRectangleCompletionOrBilinearTraceEmbeddingForPrimePrimeFloorGraph
AND FiniteThirtyWheelSmallLPFBlockerPacketControl
AND UniformCancellationAcrossSparseKSupportRadialKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
prime_survivor_floor_span_identity_closed=true
diagonal_P_ghost_completion_tax_closed=true
prime_survivor_phase_packet_span_rewrite_closed=true
full_prime_prime_rectangle_completion_closed=false
prime_floor_span_trace_or_typeii_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 61Q. Phi-LPF q-support row-averaged additive-k prime-survivor q-prefix unimodal 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_qprefix_unimodal_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-qprefix-unimodal-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-qprefix-unimodal-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-qprefix-unimodal-audit.md
```

本层转置 61P 的 floor-span graph：固定 `(P,m)` 后，有限审计范围内的
q-neighbourhood 是从本行第一个 eligible prime `q0(P)` 开始的完整 prime-q prefix：

```text
Q_prime(P,m)={prime q: q0(P)<=q<=Q*(P,m)}.
```

同一行中 `Q*(P,m)` 沿 prime `m` 序列先不降、后不升，形成单峰 cap。

有限审计读数：

```text
max_prime=1009
prime_survivor_edge_count_total=355919
pm_bucket_count_total=16328
q_prefix_count_total=355919
lower_endpoint_not_row_first_total=0
q_prefix_missing_count_total=0
q_prefix_extra_count_total=0
bad_q_prefix_identity_count=0
max_q_prefix_phase_error=0
active_P_count=155
cap_unimodality_bad_row_count=0
cap_turn_count_distribution={0:1,1:154}
total_bad_qprefix_unimodal_count=0
```

外部前沿影响：该 prefix-cap 形态比一般稀疏点集更接近 bilinear/trace 输入，
但仍未生成 completed trace family、completed Kloosterman variable、或具有可用长度的
Type-II fibres。FKMS、Milićević--Qin--Wu、Pascadi、Wright 2026 与
Shao--Shparlinski--Wijaya 仍只是后续嵌入候选；Runbo Li 的 `x^0.52` 仍不闭合
点态 `theta=1/2`。

新的最新最窄口：

```text
GlobalPrimeSurvivorQPrefixUnimodalCapProofOrReplacement
AND PrefixCapTraceOrTypeIIPhaseSaving
AND DiagonalPGhostSubtractionDiscipline
AND DenseRectangleCompletionOrBilinearTraceEmbeddingForPrimePrimeFloorGraph
AND FiniteThirtyWheelSmallLPFBlockerPacketControl
AND UniformCancellationAcrossSparseKSupportRadialKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
finite_q_prefix_neighbourhood_audit_closed=true
finite_unimodal_cap_audit_closed=true
prefix_cap_phase_packet_rewrite_closed_on_audited_range=true
global_qprefix_unimodal_theorem_proved=false
prefix_cap_trace_or_typeii_embedding_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 61R. Phi-LPF q-support row-averaged additive-k prime-survivor rough-envelope cap 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_rough_envelope_cap_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-rough-envelope-cap-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-rough-envelope-cap-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-rough-envelope-cap-audit.md
```

本层解释 61Q 的 q-prefix/unimodal cap 来源。令 `R_P` 为 fixed row 的 residual
rough composite cofactor 集，则 selected residual support 满足显式 envelope：

```text
R_{P,q}=R_P cap [q,P^2/q).
A_q=min R_{P,q}, B_q=max R_{P,q}.
M_prime(P,q)={prime m in [A_q,B_q]} \ {P}.
Q*(P,m)=min(max{q:A_q<m}, max{q:B_q>m}).
```

有限审计读数：

```text
max_prime=1009
q_checked_count=6115
nonempty_envelope_q_count=6020
selected_formula_m_count_total=299977
selected_existing_m_count_total=299977
selected_envelope_formula_mismatch_count=0
actual_prime_edge_count_total=355919
predicted_prime_edge_count_total=355919
prime_envelope_missing_count=0
prime_envelope_extra_count=0
A_monotonicity_bad_step_count=0
B_monotonicity_bad_step_count=0
pm_bucket_count=16328
cap_min_threshold_mismatch_count=0
predicted_qprefix_mismatch_count=0
total_bad_rough_envelope_cap_count=0
```

外部前沿影响：support shape 现在已压成 nested rough envelope cap，但仍没有
completed trace family、completed Kloosterman variable、可用 Type-II fibre 长度或
unbalanced convolution identity。因此 FKMS、Milićević--Qin--Wu、Pascadi、
Wright 2026 与 Shao--Shparlinski--Wijaya 仍只是候选工具；Runbo Li 的 `x^0.52`
仍不闭合点态半尺度。

新的最新最窄口：

```text
PrefixCapTraceOrTypeIIPhaseSavingFromNestedRoughEnvelope
AND CompletedTraceOrKloostermanVariableForMovingPrimeDenominator
AND DiagonalPGhostSubtractionDiscipline
AND FiniteThirtyWheelSmallLPFBlockerPacketControl
AND UniformCancellationAcrossSparseKSupportRadialKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
selected_residual_rough_envelope_formula_closed=true
prime_survivor_rough_envelope_identity_closed=true
nested_envelope_endpoint_monotonicity_closed=true
global_qprefix_unimodal_structure_explained=true
prefix_cap_trace_or_typeii_embedding_closed=false
completed_trace_or_kloosterman_variable_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 61S. Phi-LPF q-support row-averaged additive-k prime-survivor bulk-rectangle Type-II 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_bulk_rectangle_typeii_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-bulk-rectangle-typeii-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-bulk-rectangle-typeii-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-bulk-rectangle-typeii-audit.md
```

本层承接 61R：rough-envelope cap 已把支撑压成 nested staircase，但外部
Type-II/trace/Kloosterman 定理首先需要可识别的双变量 product rectangle。对每个
固定 `P`，本证书抽取实际 prime-survivor edge graph 中最大的完整 prime `q` x
prime `m` bulk rectangle，并直接复核无缺边。

有限审计读数：

```text
max_prime=1009
active_P_count=155
actual_prime_edge_count_total=355919
bulk_rectangle_edge_count_total=178404
boundary_edge_count_total=177515
bulk_fraction_total=0.501248879661
boundary_fraction_total=0.498751120339
row_full_rectangle_count_total=795159
row_completion_extra_count_total=439240
row_completion_ratio_total=2.234101017366
row_completion_extra_to_actual_ratio_total=1.234101017366
bulk_fraction_min=0.485227517792
bulk_fraction_median=0.511806375443
bulk_fraction_max=1.000000000000
bulk_fraction_ge_half_rows=99
bulk_fraction_ge_45pct_rows=155
bulk_missing_count_total=0
total_bad_bulk_rectangle_typeii_count=0
```

外部前沿影响：FKMS、Milićević--Qin--Wu、Pascadi、Wright 2026 等工具现在有
一个更接近假设的 bulk rectangle 入口，但该入口只覆盖约一半 prime-survivor
edges。剩余 staircase boundary 与 bulk 同阶，不能作为误差丢弃；Runbo Li 的
`x^0.52` 短区间素数输入也不替代这里需要的半尺度边界相消。

新的最新最窄口：

```text
BoundaryPhaseSavingForNestedRoughEnvelopeStaircase
AND CompletedTraceFamilyForPrimePrimeBulkRectangle
AND StaircaseBoundaryCompletionWithoutComparableLoss
AND DiagonalPGhostSubtractionDiscipline
AND UniformCancellationAcrossSparseKSupportRadialKernels
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
bulk_product_rectangle_verified=true
bulk_boundary_comparable_obstruction_closed=true
direct_bulk_only_typeii_closure_available=false
boundary_phase_saving_or_staircase_completion_required=true
prefix_cap_trace_or_typeii_embedding_closed=false
completed_trace_or_kloosterman_variable_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 61T. Phi-LPF q-support row-averaged additive-k prime-survivor boundary strip decomposition 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_strip_decomposition_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-strip-decomposition-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-strip-decomposition-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-strip-decomposition-audit.md
```

本层承接 61S。上一层显示 bulk rectangle 只覆盖约一半 prime-survivor edges，
boundary 同阶。本证书进一步把 boundary 从任意 leftover 集合压成三条单调
prime-interval strip：

```text
boundary = lower_wing disjoint union upper_wing disjoint union right_tail,
left_tail = 0.
```

有限审计读数：

```text
max_prime=1009
active_P_count=155
boundary_edge_count_total=177515
strip_boundary_count_total=177515
left_tail_count_total=0
lower_wing_count_total=29144
upper_wing_count_total=61620
right_tail_count_total=86751
lower_wing_fraction_of_boundary=0.164177675126
upper_wing_fraction_of_boundary=0.347125595020
right_tail_fraction_of_boundary=0.488696729854
q_start_not_row_first_count=0
left_tail_active_row_count=0
strip_prime_interval_mismatch_count_total=0
noncontiguous_strip_count_total=0
strip_length_monotonicity_bad_steps_total=0
total_bad_boundary_strip_decomposition_count=0
```

外部前沿影响：边界现在不再是任意稀疏 leftover，而是三条单调 endpoint packet。
这使 FKMS 型 trace bilinear、Milićević--Qin--Wu 型 Kloosterman、Pascadi/Wright
型 Type-II 或 unbalanced convolution 的接口更具体；但这些外部定理仍没有直接给出
三条 endpoint strip 的无损完成或相消。Runbo Li 的 `x^0.52` 仍不闭合这里的
半尺度 endpoint 控制。

新的最新最窄口：

```text
BoundaryPhaseSavingForThreeMonotonePrimeIntervalStrips
AND CompletedTraceFamilyForPrimePrimeBulkRectangle
AND StripEndpointSummationByPartsWithoutComparableLoss
AND DiagonalPGhostSubtractionDiscipline
AND UniformCancellationAcrossSparseKSupportRadialKernels
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
bulk_prefix_start_verified=true
left_tail_vanishes_verified=true
boundary_three_strip_identity_verified=true
boundary_strips_are_monotone_prime_interval_packets=true
boundary_phase_saving_closed=false
strip_completion_without_loss_closed=false
completed_trace_or_kloosterman_variable_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 61U. Phi-LPF q-support row-averaged additive-k prime-survivor boundary layer-cake rectangles 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_layercake_rectangles_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-layercake-rectangles-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-layercake-rectangles-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-layercake-rectangles-audit.md
```

本层承接 61T。三条 monotone boundary strips 可以用 layer-cake/Ferrers
分解写成互不重叠的 strip-local `q`-prefix x prime `m`-shell product
rectangles。有限审计读数：

```text
max_prime=1009
active_P_count=155
boundary_edge_count_total=177515
layercake_rectangle_count_total=6190
layercake_edge_count_total=177515
lower_wing_rectangle_count_total=1032
upper_wing_rectangle_count_total=1967
right_tail_rectangle_count_total=3191
lower_wing_edge_count_total=29144
upper_wing_edge_count_total=61620
right_tail_edge_count_total=86751
row_rectangle_count_min=1
row_rectangle_count_median=38.5
row_rectangle_count_max=81
row_rectangle_count_average=40.194805194805
max_rectangle_edge_count=261
nested_bad_steps_total=0
missing_count_total=0
extra_count_total=0
total_bad_boundary_layercake_rectangle_count=0
```

外部前沿影响：边界现在已贴近 Type-II/trace 的 product-shape 输入；但 `6190`
个层矩形仍需要统一 completed family、移动 prime denominator 的 Kloosterman
变量和跨层求和控制。FKMS、Milićević--Qin--Wu、Pascadi、Wright 等外部输入
仍没有直接给出这些层的无条件相消。

新的最新最窄口：

```text
UniformPhaseSavingAcrossBoundaryLayerCakeRectangles
AND CompletedTraceFamilyForPrimePrimeBulkRectangle
AND CompletedKloostermanVariableForMovingPrimeDenominatorOnLayers
AND StripEndpointSummationByPartsWithoutComparableLoss
AND DiagonalPGhostSubtractionDiscipline
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
boundary_layercake_rectangle_identity_verified=true
all_layers_are_complete_product_rectangles=true
boundary_phase_saving_closed=false
completed_trace_or_kloosterman_variable_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 62. Phi-LPF q-support floor prime LPF selector 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_floor_prime_lpf_selector_audit.py
data/prime-matrix-phi-lpf-qsupport-floor-prime-lpf-selector-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-floor-prime-lpf-selector-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-floor-prime-lpf-selector-audit.md
```

上一层 fixed-cofactor reverse selector 的窗口为：

```text
L=max(P/2+1, floor(kP/m)+1)
U=min(P-1, m, floor(((k+1)P-1)/m)).
```

本层把 prime-q selector 再原子化为：

```text
Q_odd = L if L is odd, else L+1
selected iff Q_odd<=U and LPF(Q_odd)=Q_odd.
```

因此 floor-defined prime selector 已不再是黑箱；它是唯一奇候选加 LPF 素性
测试。有限审计读数：

```text
max_prime=1009
row_count=76954
active_residual_row_count=52697
total_actual_support_terms=299977
total_lpf_prime_selector_terms=299977
actual_equals_lpf_prime_selector_terms=true
missing_actual_terms_total=0
extra_lpf_prime_selector_terms_total=0
max_reverse_window_size=2
max_odd_count_per_reverse_window=1
max_prime_count_per_reverse_window=1
windows_with_odd_candidate_total=951378
odd_prime_selected_total=299977
bad_lpf_prime_test_total=0
bad_prime_multiplicity_total=0
```

选择器分布：

```text
empty_window=7273864
even_singleton_rejected=835050
odd_composite_lpf_rejected=651401
odd_prime_selected=299977
```

本层对外部 theorem-match 的影响是把 `FloorPrimeSelector...` 精细化为
`OddCandidateLPFPrimeSelector...`。Wright、Milićević--Qin--Wu、Pascadi 与
Ford--Maynard 仍然需要 completed convolution、admissible coefficients、
Type-II organisation 或 object-specific Type-I/II hypotheses；不能直接估计
这个逐点 LPF-prime selector。

新的最新最窄口：

```text
OddCandidateLPFPrimeSelectorToCompletedKloostermanConvolutionBridge
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
floor_prime_selector_atomized=true
unique_odd_candidate_formula_closed=true
prime_lpf_test_atomized=true
actual_equals_lpf_prime_selector_graph=true
floor_prime_selector_completion_bridge_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 64. Phi-LPF q-support dynamic primorial unit selector 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_dynamic_primorial_unit_selector_audit.py
data/prime-matrix-phi-lpf-qsupport-dynamic-primorial-unit-selector-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-dynamic-primorial-unit-selector-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-dynamic-primorial-unit-selector-audit.md
```

上一层动态筛为：

```text
Q_odd mod ell != 0 for every prime ell<=sqrt(P-1).
```

本层令：

```text
W_P=product_{ell prime, ell<=sqrt(P-1)} ell.
```

于是 selector 精确等价于：

```text
Q_odd exists and gcd(Q_odd,W_P)=1.
```

并有有限 Mobius 乘积正规形：

```text
1_{gcd(Q_odd,W_P)=1}=sum_{d|W_P, d|Q_odd} mu(d).
```

有限审计读数：

```text
max_prime=1009
row_count=76954
active_residual_row_count=52697
total_actual_support_terms=299977
total_primorial_unit_selector_terms=299977
actual_equals_primorial_unit_selector_terms=true
missing_actual_terms_total=0
extra_primorial_unit_selector_terms_total=0
max_dynamic_primorial_modulus=200560490130
max_dynamic_primorial_prime_count=11
max_formal_mobius_terms_per_candidate=2048
primorial_unit_selected_total=299977
bad_gcd_obstruction_mismatch_total=0
bad_unit_survivor_not_prime_total=0
```

非单位拒绝分桶：

```text
ell=3:316468, ell=5:126802, ell=7:73656, ell=11:41695,
ell=13:35245, ell=17:26918, ell=19:19798, ell=23:10019,
ell=29:759, ell=31:41
```

外部前沿影响：Wright 2026、Milićević--Qin--Wu 2025、Pascadi 2025 仍需要
completed/unbalanced convolution、bilinear coefficient families 或 Type-II
Kloosterman organisation。动态 `W_P` 单位类是逐点 selector，不是这些定理
直接估计的 completed coefficient family。撤回的 `arXiv:2601.00292` 仍不能
作为输入。

新的最新最窄口：

```text
DynamicPrimorialUnitSelectorToCompletedKloostermanConvolutionBridge
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
dynamic_primorial_unit_selector_closed=true
dynamic_sqrt_sieve_equals_primorial_unit_class=true
primorial_mobius_product_identity_closed=true
actual_equals_dynamic_primorial_unit_selector_graph=true
static_modulus_completion_shortcut_valid=false
dynamic_primorial_completion_bridge_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 63. Phi-LPF q-support dynamic sqrt-sieve selector 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_dynamic_sqrt_sieve_selector_audit.py
data/prime-matrix-phi-lpf-qsupport-dynamic-sqrt-sieve-selector-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-dynamic-sqrt-sieve-selector-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-dynamic-sqrt-sieve-selector-audit.md
```

上一层把 prime-q selector 写成：

```text
selected iff Q_odd<=U and LPF(Q_odd)=Q_odd.
```

本层继续原子化。因为 `Q_odd<P`，素性等价于动态 sqrt-sieve：

```text
selected iff Q_odd exists and Q_odd mod ell != 0
for every prime ell<=sqrt(P-1).
```

每个被拒绝的奇合数候选由其最小小素数因子唯一分桶。这把 LPF 素性门
改写成有限 CRT 排除族，但动态上限 `sqrt(P)` 是目标素性选择的一部分，
不是固定 finite wheel。

有限审计读数：

```text
max_prime=1009
row_count=76954
active_residual_row_count=52697
total_actual_support_terms=299977
total_sqrt_sieve_selector_terms=299977
actual_equals_sqrt_sieve_selector_terms=true
missing_actual_terms_total=0
extra_sqrt_sieve_selector_terms_total=0
max_reverse_window_size=2
max_odd_count_per_reverse_window=1
max_dynamic_sqrt_sieve_prime_count=11
windows_with_odd_candidate_total=951378
sqrt_sieve_survivor_selected_total=299977
bad_sieve_survivor_not_prime_total=0
```

拒绝分桶：

```text
ell=3:316468, ell=5:126802, ell=7:73656, ell=11:41695,
ell=13:35245, ell=17:26918, ell=19:19798, ell=23:10019,
ell=29:759, ell=31:41
```

外部前沿影响：Wright 2026、Milićević--Qin--Wu 2025、Pascadi 2025 仍需要
completed/unbalanced convolution、bilinear coefficient families 或 Type-II
Kloosterman organisation；它们不直接估计这个动态小素数排除 selector。
Dong--Robles--Zeindler 2026 `arXiv:2601.00292` 已撤回，不能作为外部输入。

新的最新最窄口：

```text
DynamicSqrtSieveSelectorToCompletedKloostermanConvolutionBridge
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
dynamic_sqrt_sieve_selector_atomized=true
prime_lpf_selector_equals_dynamic_sqrt_sieve=true
odd_composite_rejection_partition_closed=true
actual_equals_dynamic_sqrt_sieve_selector_graph=true
fixed_finite_wheel_suffices_for_prime_selector=false
dynamic_sqrt_sieve_completion_bridge_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 59. Phi-LPF q-support external theorem match 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_external_theorem_match_audit.py
data/prime-matrix-phi-lpf-qsupport-external-theorem-match-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-external-theorem-match-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-external-theorem-match-audit.md
```

上一层已经证明完整叶子相位塌缩为：

```text
e(-hD/q)=e(h*kP/q)
```

因此本层的真实对象是：

```text
sum_{q in S(P,k)} e(h*kP/q)
q prime in (P/2,P)
S(P,k)=actual Phi-LPF residual q-support
```

本轮选择合著稿三个命题中最快可推进的行/列 Phi-LPF 线，逐项匹配当前
q-support reciprocal phase 与最新 Kloosterman/Type-II 外部候选：

```text
Wright 2026 arXiv:2604.25177:
  trilinear Kloosterman fractions / partially fixed moduli.
  requires completed mn=a mod q convolution, dyadic ranges, and SW factor.

Milićević--Qin--Wu 2025 arXiv:2511.07550:
  arbitrary-q bilinear Kloosterman forms.
  requires bilinear Kloosterman form with admissible coefficient norms.

Pascadi 2025 arXiv:2511.08445:
  Type-II Kloosterman sums with composite moduli.
  requires composite-modulus Type-II organisation.

Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113:
  Kloosterman sums parametrised by square-free and smooth integers.
  requires completed square-free/smooth parameter family.

Ford--Maynard 2024 arXiv:2407.14368:
  prime-producing sieve framework with Type-I/II hypotheses.
  requires object-specific Type-I and Type-II inputs.
```

有限接口审计读数：

```text
max_prime=1009
row_count=76954
active_qsupport_row_count=52697
total_prime_q_instances=3874554
total_qsupport_instances=299977
max_prime_q_count=73
max_support_q_count=23
completed_mn_congruence_representation_available=false
siegel_walfisz_factor_certificate_available=false
type_ii_dyadic_ranges_certificate_available=false
```

结论：这些外部定理都是有用候选，但没有一个可按名称直接估计当前
`0/1` q-support 谓词乘以 `e(h*kP/q)` 的逐行对象。本轮关闭的是
direct-name-citation 伪出口，并把 completion 门精确化为同对象桥。

新的最新最窄口：

```text
QSupportToCompletedBilinearOrTrilinearKloostermanConvolutionWithSWFactor
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
external_theorem_match_completed=true
direct_external_closure_available=false
q_support_convolution_bridge_closed=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 60. Phi-LPF q-support LPF bucket completion bridge 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_lpf_bucket_completion_bridge_audit.py
data/prime-matrix-phi-lpf-qsupport-lpf-bucket-completion-bridge-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-lpf-bucket-completion-bridge-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-lpf-bucket-completion-bridge-audit.md
```

上一层把当前对象压成：

```text
sum_{q in S(P,k)} e(h*kP/q)
```

本层继续把支撑谓词原子化。对每个 `q prime in (P/2,P)`，q 侧
clipped 窗口至多含一个奇候选 `omega_{P,k}(q)`。于是：

```text
q in S(P,k)
iff omega_{P,k}(q) is composite and LPF(omega_{P,k}(q))>=7
iff omega=r*beta, r=LPF(omega)>=7, beta>=r, LPF(beta)>=r
```

对应 rough-Mobius 桶公式为：

```text
1_S(q)=sum_{7<=r<=sqrt(omega), r prime, r|omega}
       1_{P^-(omega)>=r} 1_{omega/r>=r}

1_{P^-(omega)>=r}
  = sum_{d|omega, P^+(d)<r} mu(d)
```

有限审计读数：

```text
max_prime=1009
row_count=76954
active_residual_row_count=52697
total_prime_q_instances=3874554
total_odd_candidate_instances=1266932
total_residual_support_instances=299977
total_lpf_bucket_terms=299977
actual_support_equals_lpf_bucket_terms=true
max_terms_per_candidate=1
max_reverse_prime_count_per_lpf_bucket=1
bad_candidate_count=0
bad_bucket_formula_total=0
bad_reverse_window_total=0
```

LPF 桶分布：

```text
{7:96700, 11:52080, 13:44104, 17:34414, 19:29723,
 23:22368, 29:11815, 31:6916, 37:1559, 41:262, 43:36}
```

因此每个 support term 都是稀疏 product-window 三元组：

```text
kP < q*r*beta < (k+1)P
q prime, r prime, beta r-rough
```

并且反向固定 `r*beta` 后 prime-q 重数最大为 `1`。这是真推进：
它关闭了 q-support 谓词未原子化的口。但它同时排除一个伪出口：
不能把该稀疏图直接填充为外部 Kloosterman theorem 所需的密集 completed
dyadic convolution；填充会加入非同对象项。

新的最新最窄口：

```text
SparseLPFBucketProductWindowGraphToCompletedKloostermanConvolutionBridge
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

外部定理状态：

```text
Wright 2026: still requires completed convolution plus SW/equidistribution factor
Milićević--Qin--Wu 2025: still requires admissible bilinear coefficients
Pascadi 2025: still requires target Type-II organisation
Ford--Maynard 2024: still requires object-specific Type-I/II inputs
```

状态边界：

```text
lpf_bucket_normal_form_closed=true
rough_mobius_identity_closed=true
sparse_product_window_normal_form_closed=true
dense_completed_convolution_available=false
siegel_walfisz_factor_extracted=false
same_object_kloosterman_bridge_closed=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 61. Phi-LPF q-support reverse prime selector completion bridge 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_reverse_prime_selector_completion_bridge_audit.py
data/prime-matrix-phi-lpf-qsupport-reverse-prime-selector-completion-bridge-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-reverse-prime-selector-completion-bridge-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-reverse-prime-selector-completion-bridge-audit.md
```

上一层把支撑项压成 sparse product-window triple：

```text
kP < q*r*beta < (k+1)P
q prime in (P/2,P), r prime >= 7, beta r-rough
```

本层固定粗余因子：

```text
m=r*beta
```

反向 q-window 为：

```text
max(P/2+1, floor(kP/m)+1)
  <= q <=
min(P-1, m, floor(((k+1)P-1)/m)).
```

因为 `m>P/2`，该窗口长度 `<2`，所以最多两个连续整数；又因 admissible
`q>P/2>2` 为素数，窗口内最多一个奇素数。于是实际 q-support 等于 fixed
cofactor reverse prime selector graph。

有限审计读数：

```text
max_prime=1009
row_count=76954
active_residual_row_count=52697
total_actual_support_terms=299977
total_reverse_selector_terms=299977
actual_equals_reverse_selector_terms=true
missing_actual_terms_total=0
extra_reverse_terms_total=0
max_reverse_window_size=2
max_odd_count_per_reverse_window=1
max_prime_count_per_reverse_window=1
bad_reverse_window_size_total=0
bad_prime_multiplicity_total=0
bad_selected_not_odd_total=0
```

选择器分布：

```text
empty=7273864
singleton_nonprime=1408320
singleton_prime=263786
two_point_first_odd_prime=18261
two_point_odd_nonprime=78131
two_point_second_odd_prime=17930
```

这是真推进：它把 sparse product-window bridge 的同对象源压成
floor-defined prime selector：

```text
phase=e(h*kP/Q_{P,k}(r*beta)).
```

但这仍不是 completed Kloosterman family。把两点窗口中的非选中整数也加入
dense completion 会改变对象；Wright、Milićević--Qin--Wu、Pascadi 与
Ford--Maynard 的外部输入仍需要 completed convolution、admissible
coefficients、Type-II organisation 或 object-specific Type-I/II hypotheses。

新的最新最窄口：

```text
FloorPrimeSelectorToCompletedKloostermanConvolutionBridge
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
reverse_prime_selector_normal_form_closed=true
actual_equals_reverse_selector_graph=true
dense_completion_by_filling_window_rejected=true
floor_prime_selector_completion_bridge_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65. Phi-LPF reciprocal graph Kloosterman gateway 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_reciprocal_graph_kloosterman_gateway_audit.py
data/prime-matrix-phi-lpf-reciprocal-graph-kloosterman-gateway-ledger.json
docs/monograph/prime-matrix-phi-lpf-reciprocal-graph-kloosterman-gateway-audit.json
docs/monograph/prime-matrix-phi-lpf-reciprocal-graph-kloosterman-gateway-audit.md
```

本层继续下钻：

```text
FMTypeIISameRowReciprocalGraphBilinearDispersion
```

目标是验收可相关的外部 Kloosterman/dispersion 定理是否能直接匹配
Phi-LPF same-row reciprocal graph。

同一行对象保持为：

```text
R_30(P,k)=# {(q,r,a): P/2<q<P, q prime, m=r*a in I_q(P,k),
                 r=LPF(m)>=7, a>=r, a is r-rough}
I_q(P,k)=[max(q,floor(kP/q)+1), min(2P-1,floor(((k+1)P-1)/q))]
#I_q(P,k)<=2
#{q:m in I_q(P,k)}<=2
#{a:kP<q*r*a<(k+1)P}<=1
```

频率入口：

```text
floor_sawtooth_endpoint_route:
  psi(kP/u), psi(((k+1)P-1)/u) -> e(h*kP/u)
  defect: reciprocal phase, not modular inverse Kloosterman fraction

product_window_fourier_route:
  1_{kP<uv<(k+1)P} -> e(t*u*v/Y)
  defect: additive bilinear phase, not yet DI/DFI/BC inverse-fraction phase

crt_character_average_route:
  sum_a mu_S(a) chi(a)
  defect: fixed cellwise dominance is false; still needs signed dispersion
```

外部 theorem-match：

```text
Duke-Friedlander-Iwaniec 1997:
  bilinear Kloosterman fractions e(a*bar m/n)
  not direct: present graph first emits floor/reciprocal or product-window phases

Bettin-Chandee 2015/2018:
  trilinear Kloosterman fractions e(theta*a*bar m/n)
  not direct: present LPF tail has q prime and one-point m/a fibres, not the BC averaged package

Wright 2026 arXiv:2604.25177:
  partially fixed moduli and unbalanced AP convolution discrepancy
  not direct: theorem averages AP convolutions over q~Q with Siegel-Walfisz beta;
  H_P is a fixed pointwise product-window row

Dong-Robles-Zeindler 2026 arXiv:2601.00292:
  withdrawn; not an accepted theorem source
```

新原子门：

```text
ReciprocalGraphToKloostermanCompletionIdentity
CompletedKloostermanMeanForPrimeQAndLPFShellWeights
SawtoothTailLogSavingForThinReciprocalFibres
```

最新最窄口：

```text
ReciprocalGraphToKloostermanCompletionIdentity
AND CompletedKloostermanMeanForPrimeQAndLPFShellWeights
AND SawtoothTailLogSavingForThinReciprocalFibres
```

状态边界：

```text
direct_external_closure_reached=false
same_row_reciprocal_typeii_still_main_attack=true
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 64. Phi-LPF Ford--Maynard embedding obligation 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_ford_maynard_embedding_obligation_audit.py
data/prime-matrix-phi-lpf-ford-maynard-embedding-obligation-ledger.json
docs/monograph/prime-matrix-phi-lpf-ford-maynard-embedding-obligation-audit.json
docs/monograph/prime-matrix-phi-lpf-ford-maynard-embedding-obligation-audit.md
```

外部论文：

```text
Kevin Ford and James Maynard, On the theory of prime-producing sieves,
arXiv:2407.14368v1.
```

精读验收结论：Ford--Maynard 不是直接证明 `H_P` 的黑箱，而是
Type-I/Type-II theorem-match 框架。它要求目标序列 `w_n=a_n-b_n` 自己满足：

```text
Type I divisor-sliced interval estimates
Type II arbitrary divisor-bounded bilinear estimates
local-density comparison prime mass
positive C^-(gamma,theta,nu) lower-bound region
```

本文嵌入：

```text
x≈P^2
I_{P,k}=(kP,(k+1)P)
H=P=x^(1/2)
a_{P,k}(n)=(x/H) 1_{I_{P,k}}(n)
sum_p a_{P,k}(p)>0 <=> pi((k+1)P-1)-pi(kP)>0
```

LPF-tail Type-II 尺度匹配但支撑不匹配普通矩形盒：

```text
q,m≈P≈x^(1/2)
I_q(P,k)=[max(q, floor(kP/q)+1), min(2P-1, floor(((k+1)P-1)/q))]
# I_q(P,k)<=2
# {q:m in I_q(P,k)}<=2
# {a:kP<q*r*a<(k+1)P}<=1
```

Theorem-match 表：

```text
NonnegativeTargetSequence: closed=true, proved=true
PrimeSumTargetEqualsHPRow: closed=true, proved=true
FMTypeIShortRowDivisorSwitchEstimate: closed=false, proved=false
FMTypeIISameRowReciprocalGraphBilinearDispersion: closed=false, proved=false
FMLocalDensityForWheelRowComparisonSequence: closed=false, proved=false
FMPointwiseUniformAllRowsUpgrade: closed=false, proved=false
FixedCRTUnitCellRouteRejected: closed=true, proved=true
HPUnconditionalClosure: closed=false, proved=false
```

条件外部引理 schema：

```text
If every sufficiently large prime P and every strict row k satisfies
Ford--Maynard Type-I, Type-II, local-density and positive-C^- hypotheses
for the normalized row sequence, then H_P follows for those rows.
```

该 schema 是有效的条件接口；但四个输入均未证明，因此不能升级为外部引理版或
内部自足版的无条件闭合。

新的剩余基：

```text
FMTypeIShortRowDivisorSwitchEstimate
FMTypeIISameRowReciprocalGraphBilinearDispersion
FMLocalDensityForWheelRowComparisonSequence
FMPointwiseUniformAllRowsUpgrade
CharacterAveragedSameRowCRTDispersionForLPFTail
SquarePhaseEndpointLowerBound
```

状态边界：

```text
ford_maynard_embedding_complete=true
ford_maynard_hypotheses_verified_for_hp=false
same_row_reciprocal_typeii_still_main_attack=true
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 63. Phi-LPF CRT signed residue projection gate 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_crt_signed_residue_projection_gate_audit.py
data/prime-matrix-phi-lpf-crt-signed-residue-projection-gate-ledger.json
docs/monograph/prime-matrix-phi-lpf-crt-signed-residue-projection-gate-audit.json
docs/monograph/prime-matrix-phi-lpf-crt-signed-residue-projection-gate-audit.md
```

本层把同一行 prime-minus-tail 量投影到固定 wheel 的单位剩余类。对
`W_S=prod(S)` 定义：

```text
mu_S(a;P,k)=#{row primes n: n≡a mod W_S}
            - #{S-wheel residual composites n=q*m: n≡a mod W_S}
sum_a mu_S(a;P,k)=N(P,k)-R_S(P,k)
```

当 `P>2 max(S)` 时，高素因子 `q` 不在 wheel 内，row primes 与 residual
atoms 都落在 `W_S` 的单位类。若固定 CRT 单位格逐类支付成立，应有每个单位类
`mu_S(a;P,k)>=0`。有限审计直接否定该路线：

```text
[30-wheel]
modulus=30
stable_row_count=76789
stable_active_residual_row_count=52697
stable_total_prime_count=4172483
stable_total_residual_count=299977
stable_total_surplus=3872506
stable_rows_with_negative_unit_cell_surplus=976
stable_negative_unit_cell_count=998

[210-wheel]
modulus=210
stable_active_residual_row_count=49388
stable_total_residual_count=203277
stable_rows_with_negative_unit_cell_surplus=37115
stable_negative_unit_cell_count=67547

[2310-wheel]
modulus=2310
stable_active_residual_row_count=45472
stable_total_residual_count=151197
stable_rows_with_negative_unit_cell_surplus=45472
stable_negative_unit_cell_count=151197

[30030-wheel]
modulus=30030
stable_active_residual_row_count=39964
stable_total_residual_count=107093
stable_rows_with_negative_unit_cell_surplus=39964
stable_negative_unit_cell_count=107093
```

代表负格：

```text
30-wheel:   P=313, k=183, residue=11, prime_count=0, residual_count=4, surplus=-4
210-wheel:  P=463, k=448, residue=167, prime_count=0, residual_count=3, surplus=-3
2310-wheel: P=97,  k=92,  residue=2027, prime_count=0, residual_count=1, surplus=-1
30030-wheel:P=157, k=145, residue=22831, prime_count=0, residual_count=1, surplus=-1
```

这是真推进：CRT 投影给出精确 signed ledger，但固定剩余类逐格匹配不是
Type-I/Type-II 输入，也不能突破奇偶屏障。下一步若继续走 CRT 路线，必须是
跨单位类的 character 平均或同对象 signed dispersion：

```text
CharacterAveragedSameRowCRTDispersionForLPFTail
OR SameRowReciprocalWindowTypeIIDispersionForLPFTail
OR SquarePhaseEndpointLowerBound
```

外部前沿验收边界不变：Ford--Maynard prime-producing sieve 框架说明需要目标
序列的 Type-I/II；本层说明固定 CRT cellwise dominance 不是这种输入。

状态边界：

```text
signed_residue_projection_identity_closed=true
stable_unit_class_support_closed=true
fixed_crt_classwise_dominance_proved=false
character_averaged_dispersion_required=true
prime_count_dominates_lpf_tail_shell_sum_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 62. Phi-LPF LPF tail Type-II obligation 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_lpf_tail_typeii_obligation_audit.py
data/prime-matrix-phi-lpf-lpf-tail-typeii-obligation-ledger.json
docs/monograph/prime-matrix-phi-lpf-lpf-tail-typeii-obligation-audit.json
docs/monograph/prime-matrix-phi-lpf-lpf-tail-typeii-obligation-audit.md
```

本层把 `30-wheel` 后的 LPF tail residual 写成同一行三变量对象：

```text
R_30(P,k)=# {(q,r,a): P/2<q<P, q prime, m=r*a in I_q(P,k),
                 r=LPF(m)>=7, a>=r, a is r-rough}
```

其中

```text
I_q(P,k)=[max(q, floor(kP/q)+1), min(2P-1, floor(((k+1)P-1)/q))]
```

但这不是普通矩形 Type-II 盒。由于 `q>P/2`、`m>=q>P/2`、`r>=7`：

```text
# I_q(P,k) <= 2
# {q: m in I_q(P,k)} <= 2
# {a: kP<q*r*a<(k+1)P} <= 1
```

有限审计读数：

```text
max_prime=1009
row_count=76789
active_residual_row_count=52697
total_R30=299977
total_direct_prime_count=4172483
total_prime_count_minus_R30=3872506
all_q_m_windows_have_at_most_two_points=true
all_m_q_reverse_fibers_have_at_most_two_points=true
all_qr_a_fibers_have_at_most_one_point=true
all_residual_qr_steps_exceed_row_length=true
```

代表最大 residual 行：

```text
P=971, k=936
N=80, W_int=97, R30=23, N-R30=57
q_count=71, m_span=915, support_density=0.00149311
max_m_per_q=2, max_q_per_m=1, max_a_per_qr=1, min_qr_minus_P=3600
```

最稀疏 finite reciprocal graph 行：

```text
P=1009, k=965
W_int=87
q_count=72
m_span=924
rectangle_hull_area=66528
support_density=0.0013077201
```

外部前沿验收边界：

```text
Runbo Li arXiv:2308.04458v8 theta=0.52 -> X=P^2 gives P^1.04, not P
Ford-Maynard arXiv:2407.14368 -> useful prime-producing sieve paradigm,
  but still requires Type-I/Type-II input for the exact target sequence
```

因此 Ford--Maynard/Heath-Brown 型路线若要进入本文，不能只引用“有 Type-II
技术”或使用普通 rough-number 密度；必须证明同对象命题：

```text
SameRowReciprocalWindowTypeIIDispersionForLPFTail
OR PrimeCountDominatesLPFTailShellSum
OR SquarePhaseEndpointLowerBound
```

状态边界：

```text
lpf_tail_triple_representation_closed=true
reciprocal_graph_thin_fibers_closed=true
quotient_fiber_cancellation_available=false
external_prime_producing_sieve_applies_directly=false
prime_count_dominates_lpf_tail_shell_sum_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 61. Phi-LPF adjacent-coprime parity-trap 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_adjacent_coprime_parity_trap_audit.py
data/prime-matrix-phi-lpf-adjacent-coprime-parity-trap-ledger.json
docs/monograph/prime-matrix-phi-lpf-adjacent-coprime-parity-trap-audit.json
docs/monograph/prime-matrix-phi-lpf-adjacent-coprime-parity-trap-audit.md
```

本层审计相邻互质与商相邻互质是否能把 `30-wheel` 后的 LPF tail residual
转成素数支付通道。设 residual 候选为：

```text
n=q*m
m=r*a
r=LPF(m)
```

因为 `m` 已通过 `30-wheel`，所以 `m` 没有 `2,3,5` 因子；若 `m` 合成，则
`r>=7`。又 `q>P/2` 为奇素数，所以：

```text
q,m,r,a are odd
qm±1, m±1, a±1 are even and >2
```

于是相邻互质恒等式虽然成立：

```text
gcd(qm,qm±1)=1
gcd(m,m±1)=1
gcd(a,a±1)=1
```

但这些相邻数全部被奇偶性强迫为合数。商相邻提升也离开本行：

```text
q*r*(a±1)=q*r*a ± q*r
q*r > (P/2)*7 > P
```

有限审计读数：

```text
max_prime=1009
row_count=76789
active_residual_row_count=52697
total_R30=299977
total_same_row_adjacent_slots=595083
total_same_row_adjacent_prime_shadows=0
total_cofactor_adjacent_prime_shadows=0
total_quotient_adjacent_prime_shadows=0
total_quotient_lift_inside_row=0
all_active_adjacent_coprime_but_even_composite=true
```

代表行：

```text
P=971, k=936
R30=23
same_row_adjacent_slots=44
same_row_adjacent_prime_shadows=0
cofactor_checked=46
quotient_checked=46
quotient_lift_inside=0
```

大样本 `P=100003,300007` 抽样：

```text
sample_count=10
active_residual_row_count=6
total_R30=10782
total_same_row_adjacent_prime_shadows=0
total_quotient_lift_inside_row=0
all_active_adjacent_coprime_but_even_composite=true
```

这是真推进：它把一个看似有用的“互质相邻支付”通道精确判定为奇偶陷阱。
Ford--Maynard 型 prime-producing sieve 框架仍然相关，但它需要与对象匹配的
Type-I/Type-II 或双线性输入；单纯相邻互质既不破奇偶，在 `30-wheel`
residual 上还直接给出偶合数。

状态边界：

```text
adjacent_coprime_identity_closed=true
post30_adjacent_parity_trap_closed=true
quotient_adjacent_lift_leaves_row_closed=true
adjacent_coprime_prime_payment_proved=false
external_prime_producing_sieve_applies_directly=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 60. Phi-LPF LPF shell decrement 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_lpf_shell_decrement_audit.py
data/prime-matrix-phi-lpf-lpf-shell-decrement-ledger.json
docs/monograph/prime-matrix-phi-lpf-lpf-shell-decrement-audit.json
docs/monograph/prime-matrix-phi-lpf-lpf-shell-decrement-audit.md
```

本层把 fixed-wheel residual 继续原子化到最小素因子 shell。对每个合成
reciprocal cofactor `m`，令 `r=LPF(m)`，则：

```text
m=r*a,  a>=r,  every prime divisor of a is >=r
```

因此若 `C_y` 表示删去所有 `LPF<=y` 的 primorial wheel 容量，固定 wheel
residual 与相邻 wheel decrement 满足：

```text
R_y(P,k)=sum_{r>y} Shell_r(P,k)
C_y(P,k)-C_y'(P,k)=sum_{y<r<=y'} Shell_r(P,k)
```

有限审计读数：

```text
max_prime=1009
row_count=76789
all_lpf_factorizations_ordered=true
all_capacity_reconstructed_from_lpf_shells=true
all_adjacent_decrements_equal_lpf_shells=true
```

有限 LPF shell 总账：

```text
2=1269907
3=423339
5=169232
7=96700
11=52080
13=44104
tail_ge_17=107093
```

代表行：

```text
P=1009, k=1008
Delta=89, N=70, holes=19, W_int=101, C_30=28
R_30=9, R_210=8, R_2310=7, R_sqrt=0
LPF shells: 2:47, 3:20, 5:6, 7:1, 11:1, 13:2, tail_ge_17:5
```

大样本 `P=100003,300007` 抽样：

```text
sample_count=10
all_lpf_factorizations_ordered=true
all_capacity_reconstructed_from_lpf_shells=true
all_adjacent_decrements_equal_lpf_shells=true
tail_ge_17=3016
```

这是真推进：`R_y` 不再是黑箱尾项，而是互斥 LPF shell 尾和。继续加
primorial wheel 的每一步只是在剥离下一段 LPF shell。全局闭合仍需证明同一行
素数数支配整条 LPF 尾和：

```text
PrimeCountDominatesLPFTailShellSum
OR signed shell cancellation
OR square-phase endpoint lower bound
```

外部 rough-number 短区间与方差理论可作为密度诊断，但它们控制的是普通 rough
集合或平均/方差对象；本文需要的是 `reciprocal-window` 加权、逐行点态、同对象的
prime-minus-shell-tail 支配。因此现有外部 rough-number 输入不能直接替代上面的
同对象 residual theorem。

状态边界：

```text
lpf_shell_decrement_law_closed=true
fixed_wheel_residual_dominance_global_closed=false
external_rough_number_theorem_closes_pointwise_rows=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 59. Phi-LPF fixed-wheel rough-composite residual 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_fixed_wheel_residual_rough_composite_audit.py
data/prime-matrix-phi-lpf-fixed-wheel-residual-rough-composite-ledger.json
docs/monograph/prime-matrix-phi-lpf-fixed-wheel-residual-rough-composite-audit.json
docs/monograph/prime-matrix-phi-lpf-fixed-wheel-residual-rough-composite-audit.md
```

本层把 primorial-wheel limit 的精确边界进一步拆开。对任意固定 wheel
prime set `S`，令 `C_S(P,k)` 为删去 `S` 强迫合成 cofactor 后的 reciprocal
window 容量，令 `R_S(P,k)` 为仍未被删去的合成 cofactor 重数。则：

```text
C_S(P,k)=|F(P,k)|+R_S(P,k)
DeltaPhi_half(P,k)-C_S(P,k)=N(P,k)-R_S(P,k)
N(P,k)=pi((k+1)P-1)-pi(kP)
```

因此固定 wheel 的正性条件 `DeltaPhi_half>C_S` 不是目标命题的等价式，而是更强的
`N(P,k)>R_S(P,k)`。这把最新硬点从“继续加 wheel”压成：

```text
PrimeCountDominatesFixedWheelRoughCompositeResidual
OR same-object signed dispersion
OR special square-phase lower bound
```

有限审计读数：

```text
max_prime=1009
row_count=76789
all_sqrt_residual_zero=true
all_fixed_capacity_decomposition_holds=true
all_delta_minus_capacity_equals_prime_minus_residual=true
```

代表行：

```text
P=1009, k=1008
Delta=89, N=70, holes=19
R_30=9, R_210=8, R_2310=7, R_sqrt=0
```

有限汇总显示 fixed wheel residual 会随 wheel 扩张单调收缩：

```text
30-wheel: total_R=299977, max_R=23, min(N-R)=1
210-wheel: total_R=203277, max_R=18, min(N-R)=1
2310-wheel: total_R=151197, max_R=14, min(N-R)=1
sqrt(2P)-wheel: total_R=0, max_R=0
```

大样本 `P=100003,300007` 的抽样读数仍只作证据，不作全局证明：

```text
30-wheel: max_R=3213, min(N-R)=3215
210-wheel: max_R=2552, min(N-R)=3453
2310-wheel: max_R=2197, min(N-R)=3598
sqrt(2P)-wheel: max_R=0, min(N-R)=4385
```

外部前沿状态未改变：已发表 BHP `0.525` 与 Runbo Li `0.52` 仍大于 `1/2`；
AP 平均分布、P2 almost-prime 与 prime-producing sieve 框架仍不能直接给出本文
同对象 fixed-row positivity。固定 wheel 线现在的精确外部引理版需求是
`PrimeCountDominatesFixedWheelRoughCompositeResidual`，内部自足版则需相同对象的
signed residual 分离。

状态边界：

```text
fixed_wheel_residual_decomposition_closed=true
sqrt_wheel_residual_zero_closed=true
fixed_wheel_residual_dominance_global_closed=false
primorial_limit_independent_proof=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 59. Phi-LPF boundary layer-cake phase-interface 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_layercake_phase_interface_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-layercake-phase-interface-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-layercake-phase-interface-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-layercake-phase-interface-audit.md
```

上一层已把 boundary 拆成 `6190` 个完整 product rectangles。本层继续检查这些
rectangles 是否已可直接作为长双变量 Type-II/trace 输入。有限审计读数：

```text
layercake_rectangle_count_total=6190
edge_count_total=177515
genuine_qm_product_layer: rectangles=3880, edges=147181
q_prefix_line_layer: rectangles=1955, edges=29172
m_shell_line_layer: rectangles=296, edges=1103
point_layer: rectangles=59, edges=59
q_prefix_count_median=11
q_prefix_count_max=37
m_shell_prime_count_median=2
m_shell_prime_count_max=12
both>=16: rectangles=0, edges=0
naive_layer_sqrt_loss_factor=71.553080825699
```

结论是：多数边数确实落入 q-m product 层，但 `m` 侧是短 prime shell，
逐层并不是现有长变量 Type-II 定理的直接输入。最新最窄接口改写为：

```text
UniformShortPrimeShellCompletionAcrossLayerCakeRectangles
AND MovingPrimeQDenominatorCompletedTraceFamily
AND NoLossLayerAggregationFor6190ShortShellPackets
AND EndpointSummationByPartsForQPrefixLineLayers
AND DiagonalPGhostSubtractionDiscipline
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

外部定理匹配：

```text
FKMS trace bilinear:
  product layers are present, but thin m-shell and cross-layer aggregation are not supplied.

Milićević--Qin--Wu arbitrary-modulus Kloosterman:
  relevant only after the moving prime q denominator is completed layerwise.

Pascadi composite/non-abelian Type-II:
  does not by itself absorb q-prefix line layers or short endpoint shells.

Wright unbalanced Kloosterman fractions:
  promising for q-long/m-short layers, still conditional on the exact reciprocal phase model.

Li x^0.52 short intervals:
  still does not yield half-scale or short-shell endpoint positivity.
```

状态边界：

```text
phase_interface_shape_verified=true
direct_long_typeii_layer_closure_available=false
boundary_phase_saving_closed=false
completed_trace_or_kloosterman_variable_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 60. Phi-LPF boundary shell-step packet aggregation 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_shell_step_packet_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-shell-step-packet-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-shell-step-packet-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-shell-step-packet-audit.md
```

上一层显示 `6190` 个 layer rectangles 多数是 q-long/m-short。本层把同一 row、
同一 strip、同一 q-prefix step 的 m-blocks 合并为一个 shell-step packet。有限审计读数：

```text
previous_layer_rectangle_count_total=6190
shell_step_packet_count_total=5106
rectangle_to_packet_reduction=1084
edge_count_total=177515
packet_identity_verified=true
m_block_count_min=1
m_block_count_median=1
m_block_count_max=3
m_block_count distribution: 1/2/3 packets = 4023/1082/1
m_block_count distribution edges = 116221/61258/36
m_shell_prime_count_median=3
m_shell_prime_count_max=12
no_large_balanced_packet_ge_16=true
naive_packet_sqrt_loss_factor=64.519277044879
previous_layer_sqrt_loss_factor=71.553080825699
```

这是真推进：跨层对象从 `6190` 个 layer rectangles 压成 `5106` 个 shell-step packets，
并证明每个 packet 的 m 侧最多由 `3` 个 prime blocks 组成。但它仍只是支撑聚合
和求和账本收紧，不是相位节省。

最新最窄接口：

```text
UniformShortShellPhaseSavingForAtMostThreeBlockPackets
AND MovingPrimeQDenominatorCompletedTraceFamilyOnShellStepPackets
AND NoLossAggregationAcross5106ShellStepPackets
AND EndpointSummationByPartsForQPrefixLinePackets
AND DiagonalPGhostSubtractionDiscipline
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

外部定理匹配仍保持候选状态：FKMS trace bilinear、Milićević--Qin--Wu 任意模
Kloosterman、Pascadi composite Type-II 和 Wright unbalanced Kloosterman 可以作为
后续接口，但均未直接给出 at-most-three-block 短壳 packet 的固定行相消。

状态边界：

```text
packet_identity_verified=true
layer_aggregation_support_closed=true
short_shell_phase_saving_closed=false
moving_q_denominator_completed_trace_closed=false
no_loss_layer_aggregation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 61. Phi-LPF boundary right-tail gap localization 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_right_tail_gap_localization_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-right-tail-gap-localization-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-right-tail-gap-localization-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-right-tail-gap-localization-audit.md
```

上一层将 boundary 压成 `5106` 个 shell-step packets。本层继续定位多段
`m`-block 的来源。有限审计读数：

```text
shell_step_packet_count_total=5106
edge_count_total=177515
single_block_packet_count=4023
single_block_edge_count=116221
multi_block_packet_count=1083
multi_block_edge_count=61294
multi_block_packet_strip_set=['right_tail']
all_multi_block_packets_are_right_tail=true
lower_wing_multi_block_packet_count=0
upper_wing_multi_block_packet_count=0
right_tail_multi_block_packet_count=1083
right_tail_single_block_packet_count=1024
gap_count_total=1084
gap_size_min=1
gap_size_median=26
gap_size_max=79
gap_size_average=28.690959409594
```

因此 multi-block gap 不是全局短壳复杂性，而是完全定位到 `right_tail`。
`lower_wing` 与 `upper_wing` 都是 single-block endpoint packets。最新接口：

```text
RightTailMultiBlockGapPacketPhaseSaving
AND SingleBlockEndpointPacketSummationByParts
AND MovingPrimeQDenominatorCompletedTraceFamilyOnRightTailAndSingleBlockPackets
AND NoLossAggregationAcross5106ShellStepPackets
AND DiagonalPGhostSubtractionDiscipline
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

外部定理匹配不变：FKMS trace bilinear、Milićević--Qin--Wu 任意模
Kloosterman、Pascadi composite Type-II 与 Wright unbalanced Kloosterman 仍是
候选接口；它们没有直接给出 right-tail gap packet 的固定行相消。

状态边界：

```text
right_tail_gap_localization_closed=true
single_block_endpoint_packet_support_closed=true
right_tail_multi_block_phase_saving_closed=false
single_block_packet_phase_saving_closed=false
moving_q_denominator_completed_trace_closed=false
no_loss_packet_aggregation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 62. Phi-LPF right-tail gap diagonal/core 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_right_tail_gap_diagonal_core_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-right-tail-gap-diagonal-core-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-right-tail-gap-diagonal-core-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-right-tail-gap-diagonal-core-audit.md
```

上一层定位了 `1083` 个 right-tail multi-block packets。本层继续拆解它们的
`1084` 个 internal prime gaps。有限审计读数：

```text
gap_decomposition_verified=true
unexplained_gap_count=0
gap_missing_prime_count_total=31101
carried_core_prime_count_total=30018
diagonal_ghost_count_total=1083
diagonal_ghost_gap_count=1083
no_diagonal_gap_count=1
```

gap class：

```text
diagonal_plus_carried_core=1006
pure_diagonal_slit=77
carried_core_without_diagonal=1
```

因此 every right-tail internal gap 具有支撑恒等式：

```text
missing primes = successor-fibre carried core disjoint union optional {P}.
```

外部定理匹配相应收窄：FKMS trace bilinear、Milićević--Qin--Wu 任意模
Kloosterman、Pascadi composite Type-II 与 Wright unbalanced Kloosterman 若要进入，
现在必须作用在 successor-fibre carried core 的移动分母相位和 packet 求和上；
它们仍没有直接给出固定行 unconditional phase saving。

状态边界：

```text
right_tail_gap_diagonal_core_identity_closed=true
right_tail_diagonal_p_ghost_support_subtraction_closed=true
right_tail_successor_fibre_core_phase_saving_closed=false
single_block_packet_phase_saving_closed=false
moving_q_denominator_completed_trace_closed=false
no_loss_packet_aggregation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 63. Phi-LPF right-tail interval completion 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_right_tail_interval_completion_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-right-tail-interval-completion-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-right-tail-interval-completion-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-right-tail-interval-completion-audit.md
```

上一层把 right-tail internal gap 分成 successor core 与 diagonal `P` ghost。
本层进一步确认 successor core 来自嵌套 punctured interval，而不是任意稀疏集合。
有限审计读数：

```text
right_tail_fibre_count_total=3011
right_tail_fibre_contiguous_count=138
right_tail_fibre_p_punctured_count=2873
right_tail_fibre_other_holes_count=0
all_right_tail_fibres_are_punctured_intervals=true
multi_block_interval_completion_packet_count=1083
multi_block_completion_other_holes_packet_count=0
all_multi_block_packets_complete_to_intervals=true
```

因此 right-tail 支撑变成：

```text
right-tail fibre = prime interval minus optional {P};
multi-block shell = difference of two nested P-punctured prime intervals.
```

外部定理匹配相应收窄：FKMS trace bilinear、Milićević--Qin--Wu 任意模
Kloosterman、Pascadi composite Type-II 与 Wright unbalanced Kloosterman 若要进入，
现在必须作用在 `P`-punctured interval difference 的 moving-denominator 相位上；
Runbo Li 的 `x^0.52` 短区间素数存在仍不能提供 fixed-row reciprocal phase saving。

状态边界：

```text
right_tail_fibre_punctured_interval_identity_closed=true
right_tail_multi_block_successor_core_interval_completion_closed=true
right_tail_punctured_interval_phase_saving_closed=false
single_block_packet_phase_saving_closed=false
moving_q_denominator_completed_trace_closed=false
no_loss_packet_aggregation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 64. Phi-LPF right-tail endpoint collar 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_right_tail_endpoint_collar_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-right-tail-endpoint-collar-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-right-tail-endpoint-collar-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-right-tail-endpoint-collar-audit.md
```

上一层把 right-tail shell 写成 nested `P`-punctured interval difference。
本层进一步确认每个 shell 是 endpoint collar flux，有限审计读数：

```text
right_tail_packet_count=2107
right_tail_edge_count=86751
right_tail_single_block_packet_count=1024
right_tail_multi_block_packet_count=1083
right_tail_endpoint_collar_identity_verified=true
bad_endpoint_collar_packet_count=0
terminal_full_interval_packet_count=150
two_sided_collar_packet_count=1007
one_sided_collar_packet_count=950
p_punctured_packet_count=146
completed_collar_count_median=3
completed_collar_count_max=13
```

因此 right-tail 支撑变成：

```text
right-tail shell = endpoint collar flux minus optional {P}.
```

外部定理匹配相应收窄：FKMS trace bilinear、Milićević--Qin--Wu 任意模
Kloosterman、Pascadi composite Type-II 与 Wright unbalanced Kloosterman 若要进入，
现在必须作用在 endpoint collar flux 的 moving-denominator 相位上；Runbo Li 的
`x^0.52` 短区间素数存在仍不能给出 fixed-row reciprocal phase saving。

状态边界：

```text
right_tail_endpoint_collar_flux_identity_closed=true
right_tail_endpoint_collar_phase_saving_closed=false
single_block_packet_phase_saving_closed=false
moving_q_denominator_completed_trace_closed=false
no_loss_packet_aggregation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65. Phi-LPF boundary endpoint-flux unification 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_unification_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-unification-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-unification-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-unification-audit.md
```

上一层把 right-tail shell 写成 endpoint collar flux。本层把 lower/upper single-block
endpoint packets 也并入同一个 endpoint-flux family。有限审计读数：

```text
boundary_endpoint_flux_packet_count=5106
boundary_endpoint_flux_edge_count=177515
lower_upper_single_endpoint_packet_count=2999
right_tail_endpoint_collar_packet_count=2107
single_block_endpoint_flux_packet_count=4023
multi_block_endpoint_flux_packet_count=1083
boundary_endpoint_flux_identity_verified=true
bad_endpoint_flux_packet_count=0
actual_shell_prime_count_max=12
completed_flux_support_count_max=13
```

因此 boundary 支撑变成：

```text
boundary shell-step packet = endpoint-flux packet.
```

外部定理匹配相应收窄：FKMS trace bilinear、Milićević--Qin--Wu 任意模
Kloosterman、Pascadi composite Type-II 与 Wright unbalanced Kloosterman 若要进入，
现在必须作用在统一 endpoint-flux family 的 moving-denominator 相位上；Runbo Li
的 `x^0.52` 短区间素数存在仍不能提供 fixed-row reciprocal phase saving。

状态边界：

```text
boundary_endpoint_flux_unification_closed=true
boundary_endpoint_flux_phase_saving_closed=false
moving_q_denominator_completed_trace_closed=false
no_loss_endpoint_flux_aggregation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65A. Phi-LPF boundary endpoint-flux q-prefix atom 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_atom_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-atom-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-atom-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-atom-audit.md
```

上一层把 boundary 支撑统一为 endpoint-flux packets。本层进一步把每个 packet
拆成固定 `m` 的 q-prefix line atom。有限审计读数：

```text
qprefix_line_atom_count_total=15439
qprefix_line_atom_edge_count_total=177515
expanded_edge_set_size=177515
duplicate_atom_edge_count=0
qprefix_line_atom_identity_verified=true
bad_qprefix_atom_count=0
q_prefix_count_median=11
q_prefix_count_max=37
```

因此 boundary 支撑变成：

```text
endpoint-flux packet = disjoint union of {m} x [q_start,q_end]_prime atoms.
```

外部定理匹配相应收窄：FKMS trace bilinear、Milićević--Qin--Wu 任意模
Kloosterman、Pascadi composite Type-II 与 Wright unbalanced Kloosterman 若要进入，
现在必须作用在 fixed-`m` q-prefix reciprocal orbit 的 completed phase 上；Runbo Li
的 `x^0.52` 短区间素数存在仍不能提供 q-prefix reciprocal phase saving。

状态边界：

```text
qprefix_line_atomization_closed=true
qprefix_line_atom_phase_saving_closed=false
moving_q_denominator_completed_trace_closed=false
no_loss_qprefix_atom_aggregation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65B. Phi-LPF boundary endpoint-flux q-prefix phase normal-form 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_phase_normal_form_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-phase-normal-form-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-phase-normal-form-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-phase-normal-form-audit.md
```

上一层得到固定 `m` 的 q-prefix line atom。本层把每条边的 endpoint phase
正规化。对每个边 `(P,q,m)` 写

```text
q*m = k*P + D,  1<=k<P, 1<=D<P,
A(q) = -D mod q.
```

于是

```text
e(h*k*P/q)=e(-h*D/q)=e(h*A(q)/q).
```

有限审计读数：

```text
phase_normal_form_atom_count_total=15439
phase_normal_form_edge_count_total=177515
product_division_mismatch_count=0
phase_congruence_mismatch_count=0
k_out_of_strict_row_range_count=0
D_out_of_range_count=0
A_zero_count=0
k_nonincreasing_step_count=0
phase_normal_form_identity_verified=true
```

orbit 形状：

```text
singleton_q atoms/edges = 1162/1162
strict_beatty_k_multiq atoms/edges = 14277/176353
constant_normalized_numerator atoms/edges = 1164/1166
moving_beatty_numerator atoms/edges = 14275/176349
```

外部定理匹配进一步收窄：FKMS trace bilinear、Milićević--Qin--Wu 任意模
Kloosterman、Pascadi composite Type-II 与 Wright unbalanced Kloosterman 若要进入，
现在必须先把 moving Beatty numerator `A(q)/q` 转为可用的 completed trace 或
Kloosterman family。Runbo Li 的 `x^0.52` 短区间素数存在仍不能提供该 reciprocal
orbit 的相位节省。

状态边界：

```text
phase_normal_form_closed=true
fixed_numerator_completed_kloosterman_input_available=false
moving_q_denominator_completed_trace_closed=false
qprefix_line_atom_phase_saving_closed=false
no_loss_qprefix_atom_aggregation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65C. Phi-LPF boundary endpoint-flux q-prefix carry dynamics 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_dynamics_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-dynamics-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-dynamics-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-dynamics-audit.md
```

上一层把 phase atoms 写成 `A(q)/q`。本层进一步对同一 atom 中相邻素数
`q<q'` 写

```text
g=q'-q,
D' = D + m*g - P*c,
c = k' - k = floor((D+m*g)/P).
```

有限审计读数：

```text
carry_dynamics_atom_count_total=15439
multiq_atom_count=14277
singleton_q_atom_count=1162
successor_transition_count_total=162076
carry_formula_mismatch_count=0
D_successor_mismatch_count=0
A_successor_mismatch_count=0
successor_carry_identity_verified=true
q_gap_min/median/max=2/6/20
carry_delta_k_min/median/max=1/6/33
```

dominant shape：

```text
variable_carry_word atoms = 13317
constant_carry_word atoms = 960
variable_prime_gap_word atoms = 13315
A_mixed_sawtooth atoms = 12895
A_strict_increasing/decreasing atoms = 782/598
A_constant atoms = 2
```

外部定理匹配继续收窄：FKMS trace bilinear、Milićević--Qin--Wu 任意模
Kloosterman、Pascadi composite Type-II 与 Wright unbalanced Kloosterman 都仍需要先
把 prime-gap carry word 完成到可用 trace/Kloosterman family。Li 的 `x^0.52`
短区间素数存在不估计 carry-driven reciprocal phase。

状态边界：

```text
successor_carry_dynamics_closed=true
constant_step_rotation_reduction_available=false
moving_numerator_phase_saving_closed=false
completion_to_external_trace_or_kloosterman_closed=false
no_loss_qprefix_phase_atom_aggregation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65D. Phi-LPF q-prefix carry letter/run 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_letter_run_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-letter-run-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-letter-run-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-letter-run-audit.md
```

上一层把 moving numerator 的相邻 prime-q 演化压成 successor carry：

```text
D' = D + m*(q'-q) - P*c,
c = k' - k.
```

本层继续把每条转移写成有限字母：

```text
raw letter    L=(q'-q,c)
signed letter L+=(q'-q,c,sign(A'-A))
```

有限审计读数：

```text
carry_letter_atom_count_total=15439
multiq_atom_count=14277
singleton_q_atom_count=1162
successor_transition_count_total=162076
raw_letter_run_length_sum=162076
signed_letter_run_length_sum=162076
letter_run_decomposition_closed=true
raw_carry_letter_alphabet_count/capacity=117/297
signed_carry_letter_alphabet_count/capacity=256/891
raw_constant/variable_letter_atom_count=946/13331
signed_constant/variable_letter_atom_count=934/13343
raw_run_length_min/median/max=1/1/3
signed_run_length_min/median/max=1/1/3
raw_switch_count/ratio=142197/0.962097172511316
signed_switch_count/ratio=144439/0.9772664226415605
```

最高频 raw letters 为 `(2,2)`、`(2,3)`、`(4,4)`、`(6,6)`，对应计数
`12515,9894,9877,9045`。这说明 q-prefix carry word 已经不是任意黑箱；
但 run 中位长度为 `1` 且最大仅 `3`，所以也不存在可直接利用的长常字母块。

外部定理匹配边界进一步收窄：FKMS trace bilinear、Milićević--Qin--Wu 任意模
Kloosterman、Pascadi composite Type-II 与 Wright unbalanced Kloosterman 仍然要求先把
finite carry-letter word 完成到 admissible trace/Kloosterman family。Li 的 `x^0.52`
短区间素数存在仍不估计这类 reciprocal phase cancellation。

状态边界：

```text
finite_carry_letter_alphabet_closed=true
long_constant_letter_block_route_available=false
finite_letter_exponential_sum_saving_closed=false
completion_to_external_trace_or_kloosterman_closed=false
no_loss_qprefix_letter_atom_aggregation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65E. Phi-LPF q-prefix carry switch graph 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_switch_graph_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-switch-graph-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-switch-graph-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-switch-graph-audit.md
```

上一层把每条转移写成 finite carry letters：

```text
L=(q_next-q,k_next-k),
L_plus=(q_next-q,k_next-k,sign(A_next-A)).
```

本层继续把连续两条转移之间的切换写成 directed switch graph：

```text
L_i -> L_{i+1},
L_i^+ -> L_{i+1}^+.
```

有限审计读数：

```text
carry_switch_atom_count_total=15439
multiq_atom_count=14277
singleton_q_atom_count=1162
successor_transition_count_total=162076
adjacent_letter_pair_count_inside_atoms=147799
raw_switch_pair_count_total=147799
signed_switch_pair_count_total=147799
switch_graph_decomposition_closed=true
raw_graph_nodes/edges/density=117/1161/0.08481262327416174
signed_graph_nodes/edges/density=256/4017/0.0612945556640625
raw_outdegree_min/median/max=0/8/54
signed_outdegree_min/median/max=0/10/100
raw_largest_weak/scc=117/115
signed_largest_weak/scc=255/250
raw_changed_letter_pair_count/ratio=142197/0.962097172511316
changed_gap_pair_count/ratio=136761/0.9253174919992693
changed_carry_pair_count/ratio=140789/0.9525707210468272
changed_A_step_sign_pair_count/ratio=91187/0.6169662852928639
```

这一步把 `PrimeGapCarrySwitchingLaw` 的对象从自由词压成有限有向图。它同时给出
负面边界：raw 图最大出度 `54`、signed 图最大出度 `100`，且主要节点落入大强连通块，
因此当前对象不是低分支确定性自动机，也不能直接化为常步长旋转。

外部定理匹配边界继续保持：FKMS trace bilinear、Milićević--Qin--Wu 任意模
Kloosterman、Pascadi composite Type-II 与 Wright unbalanced Kloosterman 都仍要求先把
high-branch switch paths 完成到 admissible trace/Kloosterman family。Li 的 `x^0.52`
短区间素数存在仍不估计 switch-graph reciprocal phases。

状态边界：

```text
finite_switch_graph_closed=true
deterministic_switching_law_closed=false
low_branch_switch_graph_available=false
finite_switch_graph_phase_saving_closed=false
completion_to_external_trace_or_kloosterman_closed=false
no_loss_qprefix_switch_atom_aggregation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65F. Phi-LPF q-prefix carry switch flow decomposition 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_switch_flow_decomposition_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-switch-flow-decomposition-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-switch-flow-decomposition-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-switch-flow-decomposition-audit.md
```

上一层得到 high-branch finite switch graph。本层对每个 fixed-`m` atom 的 switch path
做确定性 loop erasure：

```text
repeated active letter => peel one directed cycle
remaining active stack => endpoint residual path
```

有限审计读数：

```text
flow_decomposition_atom_count_total=15439
switch_atom_count=13355
non_switch_atom_count=2084
adjacent_letter_pair_count_inside_atoms=147799
loop_erased_flow_decomposition_closed=true
raw_cycle_packet_count=45178
raw_cycle_edge_mass=117733
raw_residual_edge_mass=30066
raw_cycle_edge_ratio=0.7965750783158209
raw_cycle_length_min/median/max=1/2/10
raw_residual_length_min/median/max=0/2/9
signed_cycle_packet_count=36330
signed_cycle_edge_mass=107677
signed_residual_edge_mass=40122
signed_cycle_edge_ratio=0.7285367289359197
signed_cycle_length_min/median/max=1/2/14
signed_residual_length_min/median/max=0/3/15
```

这一步把 switch-graph path 的质量拆成多数 loop-erased cycle core 与短 endpoint
residual paths。它不是相消证明：cycle packet 仍需相位节省，residual endpoint path
仍需无损求和，二者还要完成到外部 trace/Kloosterman family 或内部自足替代输入。

外部定理匹配边界继续保持：FKMS trace bilinear、Milićević--Qin--Wu 任意模
Kloosterman、Pascadi composite Type-II 与 Wright unbalanced Kloosterman 都仍要求先把
cycle/residual packets 变成 admissible analytic family。Li 的 `x^0.52` 短区间素数存在
仍不估计 loop-erased switch-cycle phases。

状态边界：

```text
loop_erased_cycle_flow_core_closed=true
cycle_packet_phase_saving_closed=false
residual_endpoint_path_summation_closed=false
completion_to_external_trace_or_kloosterman_closed=false
no_loss_qprefix_flow_atom_aggregation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65G. Phi-LPF q-prefix carry cycle signature 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-audit.md
```

上一层把 high-branch switch paths 拆成 loop-erased cycle core 与 endpoint
residual paths。本层只继续拆 cycle core：每个 directed cycle 取规范旋转模板，
再按长度、gap/carry 载荷与 `A` 符号形状分桶。

有限审计读数：

```text
cycle_signature_atom_count_total=15439
switch_atom_count=13355
non_switch_atom_count=2084
adjacent_letter_pair_count_inside_atoms=147799
cycle_signature_decomposition_closed=true
raw_cycle_packet_count=45178
raw_cycle_edge_mass=117733
raw_cycle_signature_count=3546
raw_cycle_shape_count=2718
raw_template_max_edge_ratio=0.0161212234462725
raw_template_top20_edge_ratio=0.13926426745262585
raw_template_top100_edge_ratio=0.34888264123058105
signed_cycle_packet_count=36330
signed_cycle_edge_mass=107677
signed_cycle_signature_count=8691
signed_cycle_shape_count=5905
signed_A_sign_variable_cycle_count=26038
signed_template_max_edge_ratio=0.006909553572257771
signed_template_top20_edge_ratio=0.06297538007188165
signed_template_top100_edge_ratio=0.18002916128792593
```

这一步说明 cycle core 不是少数模板支配的平凡对象：raw top-20 模板只覆盖约
`13.93%` 的 raw cycle-edge mass，signed top-20 只覆盖约 `6.30%`。因此最新缺口
不是“找到一个主模板并抵消”，而是 weighted signature buckets 上的相位节省。

外部定理匹配边界继续保持：FKMS trace bilinear、Milićević--Qin--Wu 任意模
Kloosterman、Pascadi composite Type-II 与 Wright unbalanced Kloosterman 仍要求先把
cycle signatures 完成到 admissible trace/Kloosterman family。Li 的 `x^0.52`
短区间素数存在仍不估计 weighted cycle-signature phases。

状态边界：

```text
cycle_signature_ledger_closed=true
cycle_signature_weighted_phase_saving_closed=false
residual_endpoint_path_summation_closed=false
completion_to_external_trace_or_kloosterman_closed=false
no_loss_qprefix_flow_atom_aggregation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65H. Phi-LPF q-prefix carry cycle signature weight-carrier 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_weight_carrier_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-weight-carrier-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-weight-carrier-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-weight-carrier-audit.md
```

上一层把 cycle core 拆成 finite directed signatures。本层继续拆
`CycleSignatureWeightedPhaseSaving` 的真实载体：对每个 raw/signed signature
登记 P-support、strip-support、endpoint-flux class，并把 raw-base template 到
signed-child template 的碎裂关系单独成账。

有限审计读数：

```text
cycle_signature_weight_carrier_ledger_closed=true
raw_cycle_packet_count=45178
raw_cycle_edge_mass=117733
raw_cycle_signature_count=3546
raw_multi_P_edge_ratio=0.9341560989697026
raw_multi_strip_edge_ratio=0.04405731613056662
signed_cycle_packet_count=36330
signed_cycle_edge_mass=107677
signed_cycle_signature_count=8691
signed_multi_P_edge_ratio=0.7385606954131337
signed_multi_strip_edge_ratio=0.014441338447393594
signed_P_support_width_min/median/max=1/1/95
raw_base_signed_refinement_count=5359
raw_base_with_multiple_signed_children_count=1823
raw_base_fragmented_signed_edge_ratio=0.7569583105027071
```

signed A-class 边质量：

```text
all_negative edge_ratio=0.08515281815057997
all_positive edge_ratio=0.0926846030257158
mixed_positive_negative edge_ratio=0.8184106169376932
mixed_with_zero edge_ratio=0.0037519618860109402
```

这一步不是相消证明；它把 weighted phase saving 的真实对象拆成三道更窄门：
signed carrier 本身的相位节省、raw-base 到 signed-child 的权重协调、以及
median P-support 为 `1` 的 thin carrier 无损求和。

外部定理匹配边界继续保持：FKMS trace bilinear、Milićević--Qin--Wu 任意模
Kloosterman、Pascadi composite Type-II 与 Wright unbalanced Kloosterman 都要求先把
这些 carriers 变成 admissible trace/Kloosterman 或 Type-II analytic family。Li 的
`x^0.52` 短区间素数存在仍不估计 signature carrier phases。

状态边界：

```text
cycle_signature_weight_carrier_closed=true
cycle_signature_weighted_phase_saving_closed=false
signed_refinement_weight_reconciliation_closed=false
thin_P_support_carrier_summation_closed=false
residual_endpoint_path_summation_closed=false
completion_to_external_trace_or_kloosterman_closed=false
no_loss_qprefix_flow_atom_aggregation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65I. Phi-LPF q-prefix carry signed-child mirror reconciliation 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_signed_child_mirror_reconciliation_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-signed-child-mirror-reconciliation-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-signed-child-mirror-reconciliation-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-signed-child-mirror-reconciliation-audit.md
```

上一层把 weighted phase saving 的组合载体拆成 signed carriers、raw-base/signed-child
fragmentation 与 thin P-support carriers。本层测试一个最自然的非循环候选：
同一 raw-base 内用 `A`-step 符号镜像 `positive <-> negative` 做 signed-child 配平。

有限审计读数：

```text
signed_child_mirror_reconciliation_ledger_closed=true
signed_cycle_packet_count=36330
signed_cycle_edge_mass=107677
signed_cycle_signature_count=8691
raw_base_signed_refinement_count=5359
raw_base_with_multiple_signed_children_count=1823
raw_base_multi_child_signed_edge_ratio=0.7569583105027071
mirror_balanced_edge_mass=31334
mirror_balanced_edge_ratio=0.2909999349907594
mirror_imbalance_edge_mass=76343
mirror_imbalance_edge_ratio=0.7090000650092406
missing_mirror_edge_ratio=0.5848974247053689
raw_base_exact_mirror_balance_count=25
raw_base_exact_mirror_balance_ratio=0.0046650494495241645
raw_base_mirror_imbalance_ratio_min/median/max=0.0/1.0/1.0
```

结论：符号镜像配对本身不能闭合 raw-base/signed-child reconciliation。它只配平
约 `29.10%` signed edge mass，剩余约 `70.90%` 变成 mirror-imbalance
signed-child carriers。因此最新硬点从“是否有自然符号配对”下钻为
mirror-imbalance carrier 的相位节省。

外部定理匹配边界继续保持：FKMS trace bilinear、Milićević--Qin--Wu 任意模
Kloosterman、Pascadi composite Type-II 与 Wright unbalanced Kloosterman 仍要求先把
mirror-imbalance carriers 变成 admissible trace/Kloosterman 或 Type-II family。
Li 的 `x^0.52` 短区间素数存在仍不估计 mirror-pair imbalance。

状态边界：

```text
signed_child_mirror_reconciliation_ledger_closed=true
mirror_pairing_enough_for_reconciliation_closed=false
raw_base_to_signed_child_weight_reconciliation_closed=false
signed_child_mirror_imbalance_phase_saving_closed=false
thin_P_support_carrier_summation_closed=false
residual_endpoint_path_summation_closed=false
completion_to_external_trace_or_kloosterman_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65J. Phi-LPF q-prefix mirror-imbalance support 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_mirror_imbalance_support_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-mirror-imbalance-support-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-mirror-imbalance-support-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-mirror-imbalance-support-audit.md
```

本层接在 signed-child mirror reconciliation 之后，不再把剩余项只称为
mirror-imbalance，而是把 `76343` edge mass 精确拆成两类 residual carriers：

```text
mirror_imbalance_support_ledger_closed=true
mirror_imbalance_edge_mass=76343
missing_mirror_edge_mass=62980
missing_mirror_within_imbalance_ratio=0.824961031135795
unequal_mirror_pair_residual_edge_mass=13363
unequal_mirror_pair_within_imbalance_ratio=0.17503896886420497
missing_mirror_pair_count=7156
unequal_mirror_pair_residual_count=639
residual_carrier_count=7795
multi_P_residual_edge_ratio=0.6484419003706954
P_support_width_min/median/max=1/1/94
multi_strip_residual_edge_ratio=0.006326709717983312
strip_support_width_min/median/max=1/1/2
```

因此前一层的

```text
SignedChildMirrorImbalancePhaseSaving
AND NonMirrorSignedChildCarrierControl
```

被压成更具体的

```text
MissingMirrorCarrierPhaseSaving
AND UnequalMirrorPairResidualPhaseSaving
```

外部前沿匹配边界不变但更精确：FKMS trace bilinear、Milićević--Qin--Wu
任意模 Kloosterman、Pascadi composite Type-II 与 Wright 2026 unbalanced
Kloosterman fractions 只有在这些 missing/unequal residual carriers 被完成为
admissible trace/Kloosterman 或 Type-II family 后才可能使用；Runbo Li 的
`x^0.52` 短区间素数存在仍不估计 signed-child residual phase。

状态边界：

```text
mirror_imbalance_support_ledger_closed=true
missing_mirror_carrier_phase_saving_closed=false
unequal_mirror_pair_residual_phase_saving_closed=false
thin_P_support_carrier_summation_closed=false
residual_endpoint_path_summation_closed=false
completion_to_external_trace_or_kloosterman_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65K. Phi-LPF q-prefix missing-mirror structure 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_missing_mirror_structure_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-missing-mirror-structure-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-missing-mirror-structure-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-missing-mirror-structure-audit.md
```

本层优先处理上一层中占主导的 missing-mirror residual。有限审计读数：

```text
missing_mirror_structure_ledger_closed=true
missing_mirror_edge_mass=62980
missing_mirror_pair_count=7156
missing_raw_base_count=5114
single_P_missing_edge_mass=26797
single_P_missing_edge_ratio=0.4254842807240394
single_strip_missing_edge_mass=62952
single_strip_missing_edge_ratio=0.9995554144172754
wing_single_shell_missing_edge_mass=30538
wing_single_shell_missing_edge_ratio=0.48488409018736106
right_tail_missing_edge_mass=32442
right_tail_missing_edge_ratio=0.5151159098126389
missing_A_class_mixed_positive_negative_edge_ratio=0.9735947919974595
```

几何拆分为：

```text
right_tail_two_sided_collar=21925
upper_wing_single_shell=20318
lower_wing_single_shell=10220
right_tail_right_collar=5091
right_tail_left_collar=3925
right_tail_terminal_full_interval=1501
```

因此 missing-mirror 口进一步从

```text
MissingMirrorCarrierPhaseSaving
```

压成：

```text
MissingMirrorEndpointCarrierPhaseSaving
AND MissingMirrorTraceKloostermanCompletion
```

外部前沿匹配边界：FKMS trace bilinear、Milićević--Qin--Wu 任意模
Kloosterman、Pascadi composite Type-II、Wright 2026 unbalanced Kloosterman
fractions 目前仍只是候选接口，因为 missing-mirror endpoint carriers 还没有
被完成为 trace/Kloosterman 或 Type-II 变量族；Li 的 `x^0.52` 短区间素数存在
不估计 signed missing-mirror carrier phases。

状态边界：

```text
missing_mirror_structure_ledger_closed=true
missing_mirror_carrier_phase_saving_closed=false
missing_mirror_to_trace_completion_closed=false
unequal_mirror_pair_residual_phase_saving_closed=false
thin_P_support_carrier_summation_closed=false
residual_endpoint_path_summation_closed=false
completion_to_external_trace_or_kloosterman_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65L. Phi-LPF q-prefix missing-mirror endpoint-router 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_missing_mirror_endpoint_router_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-missing-mirror-endpoint-router-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-missing-mirror-endpoint-router-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-missing-mirror-endpoint-router-audit.md
```

本层继续处理 missing-mirror endpoint carriers，检查 signed-child template 层面能否
先无损路由为纯 endpoint 模板和混合 endpoint 模板。有限审计读数：

```text
missing_mirror_endpoint_router_ledger_closed=true
missing_mirror_edge_mass=62980
missing_mirror_template_count=7156
pure_endpoint_template_edge_mass=48636
pure_endpoint_template_edge_ratio=0.7722451571927597
mixed_endpoint_template_edge_mass=14344
mixed_endpoint_template_edge_ratio=0.2277548428072404
mixed_right_tail_endpoint_edge_mass=14316
mixed_right_tail_endpoint_edge_ratio=0.22731025722451573
mixed_wing_tail_endpoint_edge_mass=28
mixed_wing_tail_endpoint_edge_ratio=0.0004445855827246745
single_strip_pure_endpoint_edge_mass=48636
single_strip_pure_endpoint_edge_ratio=0.7722451571927597
endpoint_group_width_min/median/max=1/1.0/3
```

route 质量分解：

```text
pure_upper_wing_single_shell=20314
mixed_right_tail_endpoint=14316
pure_right_tail_two_sided_collar=13310
pure_lower_wing_single_shell=10208
pure_right_tail_right_collar=2347
pure_right_tail_left_collar=1769
pure_right_tail_terminal_full_interval=688
mixed_wing_and_tail_endpoint=28
```

因此上一层的

```text
MissingMirrorEndpointCarrierPhaseSaving
AND MissingMirrorTraceKloostermanCompletion
```

被压成：

```text
PureEndpointMissingMirrorCarrierPhaseSaving
AND MixedRightTailEndpointRouterNoLoss
AND MissingMirrorTraceKloostermanCompletion
```

外部前沿匹配边界继续保持：FKMS trace bilinear、Milićević--Qin--Wu 任意模
Kloosterman 与 Wright unbalanced Kloosterman fractions 只有在 endpoint-routed
carriers 被完成为 trace/Kloosterman 变量后才可能接入；Pascadi composite Type-II
仍要求 Type-II box，而不是只要 endpoint-routed signed templates。

状态边界：

```text
missing_mirror_endpoint_router_ledger_closed=true
pure_endpoint_carrier_phase_saving_closed=false
mixed_right_tail_endpoint_router_no_loss_closed=false
missing_mirror_trace_completion_closed=false
unequal_mirror_pair_residual_phase_saving_closed=false
thin_P_support_carrier_summation_closed=false
residual_endpoint_path_summation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65M. Phi-LPF q-prefix pure endpoint phase-interface 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_pure_endpoint_phase_interface_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-pure-endpoint-phase-interface-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-pure-endpoint-phase-interface-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-pure-endpoint-phase-interface-audit.md
```

本层只处理 missing-mirror endpoint-router 中的 pure endpoint 主体，把 `48636`
edge mass 拆成 single-`P` local packets 与 multi-`P` trace candidates：

```text
pure_endpoint_phase_interface_ledger_closed=true
pure_endpoint_edge_mass=48636
pure_endpoint_template_count=6408
single_P_pure_endpoint_edge_mass=26753
single_P_pure_endpoint_edge_ratio=0.5500657948844477
multi_P_pure_endpoint_edge_mass=21883
multi_P_pure_endpoint_edge_ratio=0.44993420511555227
multi_P_wing_pure_endpoint_edge_mass=16982
multi_P_right_tail_pure_endpoint_edge_mass=4901
P_support_width_min/median/max=1/1.0/54
```

phase-interface 分解：

```text
single_P_local_endpoint_packet=26753
multi_P_wing_endpoint_trace_candidate=16982
multi_P_right_tail_endpoint_trace_candidate=4901
```

这说明外部 trace/Kloosterman 定理不能直接吃掉 pure endpoint 全量；必须先处理
single-`P` local packets，同时把 multi-`P` 候选完成为合法 trace/Kloosterman
变量族。

最新最窄口：

```text
SinglePLocalPureEndpointPacketBound
AND MultiPPureEndpointTraceKloostermanCompletion
AND PureEndpointCarrierPhaseSaving
AND MixedRightTailEndpointRouterNoLoss
AND UnequalMirrorPairResidualPhaseSaving
AND ThinPSupportCarrierSummationWithoutLoss
AND ResidualEndpointPathSummationWithoutBoundaryLoss
AND NoLossAggregationAcross15439QPrefixFlowAtoms
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

外部前沿边界：FKMS trace bilinear、Milićević--Qin--Wu 任意模 Kloosterman 与
Wright unbalanced Kloosterman 只能作用在已经完成的 multi-`P` trace/Kloosterman
变量上；Dong--Robles--Zeindler Kloosterman-fraction bilinear forms 已撤回，
不可作为外部输入；Li 的 `x^0.52` 短区间素数存在不估计 signed pure endpoint
carriers。

状态边界：

```text
pure_endpoint_phase_interface_ledger_closed=true
single_P_local_endpoint_packet_bound_closed=false
multi_P_trace_completion_closed=false
pure_endpoint_carrier_phase_saving_closed=false
mixed_right_tail_endpoint_router_no_loss_closed=false
unequal_mirror_pair_residual_phase_saving_closed=false
thin_P_support_carrier_summation_closed=false
residual_endpoint_path_summation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65N. Phi-LPF q-prefix single-P local endpoint packet 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_endpoint_packet_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-endpoint-packet-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-endpoint-packet-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-endpoint-packet-audit.md
```

本层只处理 pure endpoint phase-interface 中的 `single_P_local_endpoint_packet`
支路，把 `26753` edge mass 拆成局部模板、P-slice、route 与 endpoint shell
负载账本：

```text
single_P_local_endpoint_structure_ledger_closed=true
single_P_local_endpoint_edge_mass=26753
single_P_local_endpoint_template_count=4915
single_P_support_prime_count=128
single_P_support_P_min/max=97/1009
single_P_edge_mass_per_P_min/median/max=2/167.5/827
single_P_template_edge_mass_min/median/max=1/5/16
observed_local_template_edge_mass_le_16=true
wing_single_P_local=13540
right_tail_single_P_local=13213
observed_width_one_route_superclass_balance_gap=327
```

真推进点：`SinglePLocalPureEndpointPacketBound` 不是一个可直接套平均型
Kloosterman/trace theorem 的对象。它先被压成两个实际门：

```text
LocalTemplateMultiplicityUniformBound
AND SinglePSliceEndpointPacketSummationOrPDEC
```

外部前沿边界：FKMS、Milićević--Qin--Wu、Wright 与 Xu--Zhang 的
trace/Kloosterman 输入都需要显式长变量、双线性变量或有限域集合变量；
它们不能直接估计 `P_support_width=1` 的 signed local packets。Li 的
`x^0.52` 短区间素数存在也不估计 signed carrier phase。

状态边界：

```text
single_P_local_endpoint_structure_ledger_closed=true
local_template_multiplicity_uniform_bound_proved=false
single_P_slice_endpoint_packet_summation_closed=false
single_P_local_endpoint_packet_bound_closed=false
multi_P_trace_completion_closed=false
pure_endpoint_carrier_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65O. Phi-LPF q-prefix single-P local template multiplicity 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_template_multiplicity_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-template-multiplicity-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-template-multiplicity-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-template-multiplicity-audit.md
```

本层把 `LocalTemplateMultiplicityUniformBound` 的有限对象拆成
`edge_mass = cycle_length * occurrence_count`：

```text
single_P_local_template_multiplicity_factor_ledger_closed=true
single_P_local_endpoint_edge_mass=26753
single_P_local_endpoint_template_count=4915
single_occurrence_template_count=4818
single_occurrence_edge_mass=25881
repeated_template_count=97
repeated_template_edge_mass=872
multi_packet_template_count=17
multi_packet_template_edge_mass=136
template_edge_mass_min/median/max=1/5/16
cycle_length_min/median/max=1/5/14
occurrence_count_min/median/max=1/1/4
```

最新实际门：

```text
LocalCycleLengthUniformBound
AND LocalOccurrenceMultiplicityUniformBound
AND CycleOccurrenceProductBoundOrPDEC
```

外部前沿边界：FKMS、Milićević--Qin--Wu、Wright 与 Xu--Zhang 都是
平均/双线性/集合变量输入，不能直接证明 width-one signed cycle template 的
occurrence multiplicity。这里需要组合结构界或超额模板回流 PDEC/SAE。

状态边界：

```text
single_P_local_template_multiplicity_factor_ledger_closed=true
local_cycle_length_uniform_bound_proved=false
local_occurrence_multiplicity_uniform_bound_proved=false
cycle_occurrence_product_bound_proved=false
local_template_multiplicity_uniform_bound_proved=false
single_P_slice_endpoint_packet_summation_closed=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 66. Phi-LPF sawtooth reciprocal tail gateway 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_sawtooth_reciprocal_tail_gateway_audit.py
data/prime-matrix-phi-lpf-sawtooth-reciprocal-tail-gateway-ledger.json
docs/monograph/prime-matrix-phi-lpf-sawtooth-reciprocal-tail-gateway-audit.json
docs/monograph/prime-matrix-phi-lpf-sawtooth-reciprocal-tail-gateway-audit.md
```

本层在三个最新原子门中选择最快可推进的

```text
SawtoothTailLogSavingForThinReciprocalFibres
```

并把它拆成无权基准与真实带权对象两层。endpoint floor/sawtooth 给出
倒数相位

```text
e(h*k*P/u)
```

对无权模型

```text
S(A;N)=sum_{N<n<=2N} e(A/n), A=h*k*P, N=P
```

经典 van der Corput/Kusmin--Landau 二阶导数估计给

```text
S(A;N) << sqrt(A/N)+sqrt(N^3/A)
       = sqrt(h*k)+P/sqrt(h*k).
```

当 high-q reciprocal graph 非空时，`q,m>P/2` 迫使 `k+1>P/4`，所以活动行
处在 `P` 尺度。取 `H=(log P)^B` 后，无权 finite sawtooth modes 贡献
`O(P^(1/2)H^(1/2))`，截断尾项为 `O(P/H)`，因此无权 endpoint benchmark
已有任意对数节省余量。

外部定理匹配：

```text
classical second-derivative estimate:
  matches unweighted real reciprocal phase;
  does not handle prime-q/LPF-shell weights.

Duke--Friedlander--Iwaniec 1997:
  bilinear Kloosterman fractions after inverse-modulus completion;
  still needs ReciprocalGraphToKloostermanCompletionIdentity.

Bettin--Chandee 2015/2018 and Wright 2026:
  trilinear Kloosterman fractions and partially fixed-moduli dispersion;
  still need CompletedKloostermanMeanForPrimeQAndLPFShellWeights.

Shao--Shparlinski--Wijaya 2025/2026:
  square-free/smooth Kloosterman sum power savings;
  useful frontier input after finite-field completion, but not a direct theorem
  for the real phase e(A/q) with prime q and LPF-shell row weights.
```

最新 sawtooth 最窄口：

```text
PrimeQLPFShellWeightedReciprocalPhaseSaving
AND WeightExtractionFromLPFShellToBilinearKloostermanOrVaughanTypeII
AND UniformFiniteHTruncationWithHPolylog
```

状态边界：

```text
unweighted_sawtooth_benchmark_closed=true
weighted_sawtooth_phi_lpf_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 67. Phi-LPF finite-H truncation closure 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_finite_h_truncation_closure_audit.py
data/prime-matrix-phi-lpf-finite-h-truncation-closure-ledger.json
docs/monograph/prime-matrix-phi-lpf-finite-h-truncation-closure-audit.json
docs/monograph/prime-matrix-phi-lpf-finite-h-truncation-closure-audit.md
```

本层在合著稿三命题中选择最快可完全闭合的子门：

```text
Prime Matrix row/column Phi-LPF:
  UniformFiniteHTruncationWithHPolylog
```

选择理由：二点筛仍需 `BMD=>TLI without hidden denominator/parity gap`，RH 线仍是
controlled exits 的 independent referee package；而 finite-H 截断只需
Vaaler/截断账本与 reciprocal thin-fibre 质量上界。

截断账本：

```text
W_int(P,k) <= 2*pi(P) < 2P
two endpoint sawtooth tails have absolute mass <= 4P/H
choose H=ceil((log P)^(A+2))
tail = O(P/log^(A+2)P) = O(P/log^A P)
finite remaining modes: |h|<=H, harmonic coefficient cost O(log H)=O(log log P)
```

因此：

```text
UniformFiniteHTruncationWithHPolylog=true
```

但剩余 finite modes 仍必须证明带权抵消。最新最窄口变为：

```text
PrimeQLPFShellWeightedReciprocalPhaseSaving
AND WeightExtractionFromLPFShellToBilinearKloostermanOrVaughanTypeII
```

外部前沿匹配：

```text
Vaaler finite Fourier approximation:
  accepted for deterministic truncation gate.

Milićević--Qin--Wu 2025 arXiv:2511.07550:
  power-saving bilinear forms with Kloosterman sums modulo arbitrary q;
  useful after completion, not direct for current real phase and LPF weights.

Pascadi 2025 arXiv:2511.08445:
  non-abelian amplification for composite-modulus Kloosterman sums;
  useful frontier input, not direct for prime-q LPF-weighted sawtooth phase.

Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113:
  square-free/smooth Kloosterman parameter sums;
  still requires finite-field completion and LPF-shell transfer.
```

状态边界：

```text
uniform_finite_h_truncation_closed=true
weighted_sawtooth_phi_lpf_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 68. Phi-LPF weight extraction norm closure 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_weight_extraction_norm_closure_audit.py
data/prime-matrix-phi-lpf-weight-extraction-norm-closure-ledger.json
docs/monograph/prime-matrix-phi-lpf-weight-extraction-norm-closure-audit.json
docs/monograph/prime-matrix-phi-lpf-weight-extraction-norm-closure-audit.md
```

本层继续按“合著稿三命题哪个更快闭合就先攻”的原则选择行/列
Phi-LPF 的纯代数子门：

```text
LPFShellWeightBoundedCoefficientExtraction
NoMobiusL1ExplosionNeeded
```

finite-H 截断后，真实剩余 finite modes 可把 LPF-shell 权重无损写为：

```text
R_30(P,k)=sum beta(q,r,a) 1_{kP<qra<(k+1)P}
P/2<q<P, q prime
r=LPF(m)>=7
a>=r, P^-(a)>=r
beta(q,r,a) in {0,1}
```

由于 `q>P/2` 且 `r>=7`，固定 `(q,r)` 的 quotient 纤维至多一个点；
投影到 prime `q` 后：

```text
0 <= b(q) <= #I_q(P,k) <= 2
sum_q b(q) = R_30(P,k) <= W_int(P,k) <= 2*pi(P) < 2P
```

因此 LPF 权重抽取不会造成系数范数爆炸；不需要把 rough 条件完整展开成
所有小素数的 Möbius 排斥和。有限实现审计读数：

```text
max_prime=1009
k_range=1<=k<P in this implementation audit
row_count=76954
active_residual_row_count=52697
total_R30=299977
max_projected_q_weight_seen=1
max_qr_fiber_weight_seen=1
violation_count=0
```

外部前沿匹配：

```text
Vaughan/Heath-Brown Type-I/II identity framework:
  bounded coefficient sequences are compatible after a valid bilinear decomposition;
  still no direct same-row reciprocal graph estimate.

Duke-Friedlander-Iwaniec and Bettin--Chandee:
  bounded coefficients are compatible after inverse-fraction completion;
  the completion identity remains open.

Milićević--Qin--Wu 2025, Pascadi 2025, Shao--Shparlinski--Wijaya 2024/2025:
  useful Kloosterman-frontier candidates after completion;
  not direct fixed-row prime-q real reciprocal phase estimates.
```

最新最窄口进一步压成：

```text
PrimeQBoundedLPFCoefficientReciprocalPhaseSaving
AND CompletionToExternalKloostermanOrVaughanTypeII
```

状态边界：

```text
lpf_weight_bounded_coefficient_extraction_closed=true
weighted_reciprocal_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 69. Phi-LPF boolean q-projection closure 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_boolean_q_projection_closure_audit.py
data/prime-matrix-phi-lpf-boolean-q-projection-closure-ledger.json
docs/monograph/prime-matrix-phi-lpf-boolean-q-projection-closure-audit.json
docs/monograph/prime-matrix-phi-lpf-boolean-q-projection-closure-audit.md
```

本层继续按“合著稿三命题哪个更快闭合就先攻”的原则选择行/列
Phi-LPF 的 prime-q 投影子门：

```text
PrimeQBooleanProjectionForLPFShellResidual
NoDoubleMultiplicityPrimeQNoise
```

上一层给出 `0<=b(q)<=#I_q(P,k)<=2`。本层把它 sharpen 为布尔权重。
原因是：

```text
q>P/2 => #I_q(P,k)<=2
if #I_q(P,k)=2, the two integers are consecutive
LPF residual m is composite and LPF(m)>=7, hence m is odd
two consecutive integers contain at most one odd integer
therefore b_{P,k}(q) in {0,1}
```

有限实现审计读数：

```text
max_prime=1009
k_range=1<=k<P in this implementation audit
row_count=76954
active_residual_row_count=52697
total_R30=299977
max_window_size_seen=2
total_two_point_windows=876803
total_two_point_windows_with_residual=208481
max_projected_q_weight_seen=1
violation_count=0
```

外部前沿匹配：

```text
Classical parity/2-wheel observation:
  closes only the q-projected multiplicity gate.

Milićević--Qin--Wu 2025 arXiv:2511.07550:
  arbitrary-modulus Kloosterman power savings remain useful only after completion.

Pascadi 2025 arXiv:2511.08445:
  composite-modulus Kloosterman amplification is not a fixed-row real reciprocal phase theorem.

Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113:
  square-free/smooth Kloosterman sums need finite-field completion before they can be relevant.
```

最新最窄口进一步压成：

```text
PrimeQBooleanSubsetReciprocalPhaseSaving
AND CompletionToExternalKloostermanOrVaughanTypeII
```

状态边界：

```text
prime_q_boolean_projection_closed=true
weighted_reciprocal_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 70. Phi-LPF matching graph closure 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_matching_graph_closure_audit.py
data/prime-matrix-phi-lpf-matching-graph-closure-ledger.json
docs/monograph/prime-matrix-phi-lpf-matching-graph-closure-audit.json
docs/monograph/prime-matrix-phi-lpf-matching-graph-closure-audit.md
```

本层继续按“合著稿三命题哪个更快闭合就先攻”的原则选择行/列
Phi-LPF 的反向纤维子门：

```text
ReversePrimeQFiberBooleanForResidualM
ReciprocalResidualGraphIsPartialMatching
```

上一层已经证明 prime-q 侧投影是布尔的。本层再证明 residual cofactor 侧
也是布尔：

```text
fixed residual m>P/2
possible q lie in an integer interval of length P/m<2
if two integer q candidates are present, they are consecutive
q>P/2>2 and q prime => at most one candidate is prime
```

因此 `(q,m)` residual graph 两侧最大度均为 `1`，是部分匹配。有限实现审计读数：

```text
max_prime=1009
k_range=1<=k<P in this implementation audit
row_count=76954
active_residual_row_count=52697
total_edges_R30=299977
max_q_degree_seen=1
max_m_degree_seen=1
max_reverse_q_window_size_seen=2
total_two_point_reverse_windows_on_edges=36191
all_rows_matching_graph=true
violation_count=0
```

外部前沿匹配：

```text
Classical parity/twin-prime exception observation:
  closes only the graph matching gate.

Milićević--Qin--Wu 2025 arXiv:2511.07550:
  arbitrary-modulus Kloosterman estimates remain useful only after completion.

Pascadi 2025 arXiv:2511.08445:
  composite-modulus Kloosterman amplification is not a pointwise fixed-row
  real reciprocal matching theorem.

Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113:
  square-free/smooth Kloosterman sums need finite-field completion first.
```

最新最窄口进一步压成：

```text
PrimeQMatchingSubsetReciprocalPhaseSaving
AND CompletionToExternalKloostermanOrVaughanTypeII
```

状态边界：

```text
reciprocal_residual_graph_matching_closed=true
weighted_reciprocal_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 71. Phi-LPF matched displacement phase closure 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_matched_displacement_phase_closure_audit.py
data/prime-matrix-phi-lpf-matched-displacement-phase-closure-ledger.json
docs/monograph/prime-matrix-phi-lpf-matched-displacement-phase-closure-audit.json
docs/monograph/prime-matrix-phi-lpf-matched-displacement-phase-closure-audit.md
```

本层继续按“合著稿三命题哪个更快闭合就先攻”的原则选择行/列
Phi-LPF 的相位正规形子门：

```text
MatchedDisplacementPhaseNormalForm
TwoSidedEndpointSelectorNormalForm
```

matching graph 闭合后，每条 residual 边是唯一匹配边 `(q,m)`。定义

```text
d=q*m-kP.
```

由于 `kP<qm<(k+1)P`，所以 `1<=d<P`。又因为 `kP=qm-d`，对任意整数
`h` 有

```text
e(h*kP/q)=e(h*m-h*d/q)=e(-h*d/q).
```

这把 large numerator `h*kP` 的倒数相位精确改写为 matched displacement
相位。两侧端点选择也被固定：`m` 是 q 侧 clipped floor 窗口端点之一，
`q` 是 m 侧反向 clipped floor 窗口端点之一。

有限实现审计读数：

```text
max_prime=1009
k_range=1<=k<P in this implementation audit
row_count=76954
active_residual_row_count=52697
total_edges_R30=299977
global_min_displacement=1
global_max_displacement=1008
all_displacements_in_1_to_Pminus1=true
all_phase_congruences_verified=true
all_endpoint_selectors_verified=true
bad_displacement_total=0
bad_phase_total=0
bad_endpoint_total=0
bad_edge_total=0
```

外部前沿匹配：

```text
Elementary integer phase reduction:
  closes the normal-form gate.

Milićević--Qin--Wu 2025 arXiv:2511.07550:
  arbitrary-modulus bilinear Kloosterman estimates remain useful only
  after completion.

Pascadi 2025 arXiv:2511.08445:
  composite-modulus/non-abelian amplification is not a pointwise fixed-row
  matched-displacement phase theorem.

Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113:
  square-free/smooth Kloosterman parameter sums still need finite-field
  completion first.
```

最新最窄口进一步压成：

```text
PrimeQMatchedDisplacementPhaseSaving
AND CompletionToExternalKloostermanOrVaughanTypeII
```

状态边界：

```text
matched_displacement_phase_normal_form_closed=true
weighted_reciprocal_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 72. Phi-LPF floor residue branch phase closure 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_floor_residue_branch_phase_closure_audit.py
data/prime-matrix-phi-lpf-floor-residue-branch-phase-closure-ledger.json
docs/monograph/prime-matrix-phi-lpf-floor-residue-branch-phase-closure-audit.json
docs/monograph/prime-matrix-phi-lpf-floor-residue-branch-phase-closure-audit.md
```

本层继续按“合著稿三命题哪个更快闭合就先攻”的原则选择行/列
Phi-LPF 的 q 侧 floor-residue branch 子门：

```text
PrimeQBoundaryCapFreeForResidualEdges
PrimeQFloorResidueBranchNormalForm
```

上一层已把每条 residual 边写成 matched displacement：

```text
d=q*m-kP,  1<=d<P,  e(h*kP/q)=e(-h*d/q).
```

本层证明 q-window 的两个剪裁边界不是 residual edge 的真实来源。
lower cap `m=q` 不可用，因为 `m=q` 是素数；若窗口还包含唯一邻点
`q+1`，它是偶数，也不可能满足 `LPF(m)>=7`。upper cap `m=2P-1`
也不可用，因为对整数 `q>P/2` 有：

```text
q*(2P-1)>P^2 >= (k+1)P.
```

若只退到邻点 `2P-2`，它仍是偶数。因此 residual edge 只能来自
lower/upper floor endpoint。于是设

```text
rho=(kP mod q)
sigma=(((k+1)P-1) mod q)
```

则有精确分支：

```text
lower branch: d=q-rho, 1<=d<=q
upper branch: d=P-1-sigma, P-q<=d<=P-1
```

有限实现审计读数：

```text
max_prime=1009
k_range=1<=k<P in this implementation audit
row_count=76954
active_residual_row_count=52697
total_edges_R30=299977
branch_totals={lower:104807, upper:103674, both:91496, interior:0}
all_q_side_boundary_caps_absent=true
all_edges_floor_branch_covered=true
all_floor_residue_formulas_verified=true
bad_cap_total=0
bad_floor_coverage_total=0
bad_residue_formula_total=0
```

外部前沿匹配：

```text
Elementary floor-residue algebra:
  closes this branch normal-form gate.

Milićević--Qin--Wu 2025 arXiv:2511.07550:
  bilinear Kloosterman estimates remain useful only after completion.

Pascadi 2025 arXiv:2511.08445:
  non-abelian amplification is not a pointwise fixed-row branch-phase theorem.

Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113:
  square-free/smooth Kloosterman sums still need finite-field completion first.

Dong--Robles--Zeindler 2026 arXiv:2601.00292:
  Kloosterman-fraction bilinear-form near miss is withdrawn on arXiv and
  cannot be cited as a valid external input.
```

最新最窄口进一步压成：

```text
PrimeQFloorResidueBranchPhaseSaving
AND CompletionToExternalKloostermanOrVaughanTypeII
```

状态边界：

```text
floor_residue_branch_normal_form_closed=true
floor_residue_branch_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 73. Phi-LPF parity selected branch phase closure 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_parity_selected_branch_phase_closure_audit.py
data/prime-matrix-phi-lpf-parity-selected-branch-phase-closure-ledger.json
docs/monograph/prime-matrix-phi-lpf-parity-selected-branch-phase-closure-audit.json
docs/monograph/prime-matrix-phi-lpf-parity-selected-branch-phase-closure-audit.md
```

本层继续按“合著稿三命题哪个更快闭合就先攻”的原则选择行/列
Phi-LPF 的端点侧选择子门：

```text
TwoPointFloorWindowParitySelector
SingletonBothBranchConsistency
```

上一层已把 q 侧候选端点写为：

```text
L=floor(kP/q)+1
U=floor(((k+1)P-1)/q)
```

并去除了 boundary cap。由于 `P/q<2`，每条 residual edge 上有：

```text
U-L in {0,1}.
```

若 `U=L`，该边是 singleton，同时属于 lower/upper，且两个余数公式给同一
`d`。若 `U=L+1`，两个端点连续；而 `LPF(m)>=7` 强制 residual cofactor
`m` 为奇数，所以端点侧选择由奇偶性唯一决定：

```text
lower branch iff L is odd
upper branch iff U is odd
```

相位公式仍为：

```text
lower: d=q-(kP mod q)
upper: d=P-1-(((k+1)P-1) mod q)
```

有限实现审计读数：

```text
max_prime=1009
k_range=1<=k<P in this implementation audit
row_count=76954
active_residual_row_count=52697
total_edges_R30=299977
width_totals={singleton_width_0:91496, two_point_width_1:208481}
actual_branch_totals={lower:104807, upper:103674, both:91496}
predicted_branch_totals={lower:104807, upper:103674, both:91496}
all_edges_width_zero_or_one=true
all_two_point_branches_parity_selected=true
all_residual_cofactors_odd=true
all_branch_phase_formulas_verified=true
all_singleton_branch_formulas_consistent=true
bad_width_total=0
bad_parity_total=0
bad_prediction_total=0
bad_phase_formula_total=0
bad_singleton_formula_total=0
```

外部前沿匹配：

```text
Euler 2-wheel parity plus floor-window algebra:
  closes this endpoint-side selection gate.

Milićević--Qin--Wu 2025 arXiv:2511.07550:
  bilinear Kloosterman estimates remain useful only after completion.

Pascadi 2025 arXiv:2511.08445:
  non-abelian amplification is not a pointwise fixed-row branch-phase theorem.

Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113:
  square-free/smooth Kloosterman sums still need finite-field completion first.

Dong--Robles--Zeindler 2026 arXiv:2601.00292:
  Kloosterman-fraction bilinear-form near miss is withdrawn on arXiv and
  cannot be cited as a valid external input.
```

最新最窄口进一步压成：

```text
PrimeQParitySelectedFloorResidueBranchPhaseSaving
AND CompletionToExternalKloostermanOrVaughanTypeII
```

状态边界：

```text
parity_selected_branch_normal_form_closed=true
parity_selected_branch_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 74. Phi-LPF unique odd candidate projection closure 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_unique_odd_candidate_projection_closure_audit.py
data/prime-matrix-phi-lpf-unique-odd-candidate-projection-closure-ledger.json
docs/monograph/prime-matrix-phi-lpf-unique-odd-candidate-projection-closure-audit.json
docs/monograph/prime-matrix-phi-lpf-unique-odd-candidate-projection-closure-audit.md
```

本层继续按“合著稿三命题哪个更快闭合就先攻”的原则选择行/列
Phi-LPF 的 q 单值候选投影门：

```text
PrimeQUniqueOddCandidateProjection
LPFResidualAsQSubsetPredicate
```

对每个 prime `q in (P/2,P)` 定义 clipped reciprocal window：

```text
J_q(P,k)=[max(q,floor(kP/q)+1), min(2P-1,floor(((k+1)P-1)/q))].
```

因为 `q>P/2`，该窗口至多含两个连续整数，故至多含一个奇数。记这个奇数为
`omega_{P,k}(q)`。本层证明：

```text
(q,m) is a residual edge
iff omega_{P,k}(q) exists,
    m=omega_{P,k}(q),
    omega is composite,
    LPF(omega)>=7.
```

于是 residual graph 被压成 q 上的单值候选函数加 LPF 子集谓词；后续不再有
端点、分支或多重图自由度。相位变为：

```text
D(q)=q*omega_{P,k}(q)-kP
e(h*kP/q)=e(-h*D(q)/q)
```

有限实现审计读数：

```text
max_prime=1009
k_range=1<=k<P in this implementation audit
row_count=76954
active_residual_row_count=52697
total_prime_q_instances=3874554
total_odd_candidate_instances=1266932
actual_total_edges_R30=299977
predicted_total_edges_R30=299977
reason_totals={no_odd_candidate:2607622, prime:374384, small_lpf_3:423339, small_lpf_5:169232, residual_lpf_ge_7_composite:299977}
branch_totals_on_candidates={both:390129, lower:440801, upper:436002}
window_width_totals={-1:2214518, 0:783233, 1:876803}
max_odd_candidates_per_q=1
unique_odd_candidate_per_q=true
predicted_edges_equal_actual_edges=true
all_predicted_displacements_in_1_to_Pminus1=true
bad_candidate_total=0
bad_phase_displacement_total=0
missing_edge_total=0
extra_edge_total=0
```

外部前沿匹配：

```text
Euler parity plus clipped reciprocal window algebra:
  closes this unique odd candidate projection gate.

Milićević--Qin--Wu 2025 arXiv:2511.07550:
  bilinear Kloosterman estimates remain useful only after completion.

Pascadi 2025 arXiv:2511.08445:
  non-abelian amplification is not a pointwise fixed-row q-subset phase theorem.

Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113:
  square-free/smooth Kloosterman sums still need finite-field completion first.

Dong--Robles--Zeindler 2026 arXiv:2601.00292:
  Kloosterman-fraction bilinear-form near miss is withdrawn on arXiv and
  cannot be cited as a valid external input.
```

最新最窄口进一步压成：

```text
PrimeQUniqueOddCandidateLPFSubsetPhaseSaving
AND CompletionToExternalKloostermanOrVaughanTypeII
```

状态边界：

```text
unique_odd_candidate_projection_closed=true
unique_odd_candidate_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 75. Phi-LPF unique odd candidate LPF partition closure 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_unique_odd_candidate_lpf_partition_closure_audit.py
data/prime-matrix-phi-lpf-unique-odd-candidate-lpf-partition-closure-ledger.json
docs/monograph/prime-matrix-phi-lpf-unique-odd-candidate-lpf-partition-closure-audit.json
docs/monograph/prime-matrix-phi-lpf-unique-odd-candidate-lpf-partition-closure-audit.md
```

本层继续选择行/列 Phi-LPF 的最快可闭合子门：

```text
UniqueOddCandidateFiveWayLPFPartition
LPFResidualAsWheel30CompositeSurvivor
CandidatePhaseFourTermExactDecomposition
```

上一层已经证明每个 prime `q in (P/2,P)` 至多有一个奇候选
`omega_{P,k}(q)`。本层把该候选分入五个互斥点态状态：

```text
no_odd_candidate
prime
small_lpf_3
small_lpf_5
residual_lpf_ge_7_composite
```

因为 `omega` 为奇数，`LPF(omega)<7` 只能是 `3` 或 `5`。因此：

```text
residual edge
iff omega exists, gcd(omega,30)=1, and omega is composite.
```

候选相位随之有精确四项分解：

```text
S_candidate(h)=S_prime(h)+S_LPF3(h)+S_LPF5(h)+S_residual(h),
phase=e(-hD(q)/q).
```

有限实现审计读数：

```text
max_prime=1009
k_range=1<=k<P in this implementation audit
row_count=76954
active_residual_row_count=52697
total_prime_q_instances=3874554
total_odd_candidate_instances=1266932
actual_total_edges_R30=299977
predicted_total_edges_R30=299977
reason_totals={no_odd_candidate:2607622, prime:374384, small_lpf_3:423339, small_lpf_5:169232, residual_lpf_ge_7_composite:299977}
wheel30_survivor_candidate_total=674361
prime_candidate_total=374384
residual_lpf_ge_7_composite_total=299977
forced_composite_by_30wheel_total=592571
five_way_partition_exhaustive=true
candidate_partition_exhaustive=true
wheel30_survivor_identity_verified=true
forced_composite_identity_verified=true
residual_cell_equals_actual_edges=true
all_candidate_displacements_in_1_to_Pminus1=true
bad_candidate_total=0
bad_candidate_displacement_total=0
bad_small_lpf_partition_total=0
bad_five_way_partition_total=0
bad_candidate_partition_total=0
bad_wheel30_split_total=0
missing_edge_total=0
extra_edge_total=0
```

外部前沿匹配：

```text
Milićević--Qin--Wu 2025 arXiv:2511.07550:
  useful only after a completion from omega(q) phases to bilinear
  Kloosterman sums; it does not split prime/composite wheel-30 survivors.

Pascadi 2025 arXiv:2511.08445:
  Type-II Kloosterman source after a valid completion identity; not a
  pointwise fixed-row LPF partition theorem.

Shao--Shparlinski--Wijaya 2024 arXiv:2411.12113:
  relevant only after a finite-field/completion bridge to their parameter
  family.

Dong--Robles--Zeindler 2026 arXiv:2601.00292:
  withdrawn on arXiv v2; near-miss diagnostic only.
```

最新最窄口进一步压成：

```text
PrimeQUniqueOddCandidateWheel30CompositeSurvivorPhaseSaving
AND CompletionToExternalKloostermanOrVaughanTypeII
```

状态边界：

```text
unique_odd_candidate_lpf_partition_closed=true
wheel30_survivor_prime_composite_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 76. Phi-LPF wheel30 composite LPF descent closure 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_wheel30_composite_lpf_descent_closure_audit.py
data/prime-matrix-phi-lpf-wheel30-composite-lpf-descent-closure-ledger.json
docs/monograph/prime-matrix-phi-lpf-wheel30-composite-lpf-descent-closure-audit.json
docs/monograph/prime-matrix-phi-lpf-wheel30-composite-lpf-descent-closure-audit.md
```

本层继续选择行/列 Phi-LPF 的最快可闭合子门：

```text
Wheel30CompositeLPFDescentUniqueRoughQuotient
FixedPrimeQSmallRQuotientIntervalSingleton
ResidualAsPrimeQSmallRoughQuotientCandidateGraph
```

上一层已经把 residual cell 精确定位为 `30`-wheel survivor 的 composite
部分。本层对每条 residual 写：

```text
omega=r*a
r=LPF(omega)
7<=r<=sqrt(2P-1)
a>=r
LPF(a)>=r
```

固定 prime `q in (P/2,P)` 与 prime `r>=7` 后，商 `a` 必须满足：

```text
kP < q*r*a < (k+1)P.
```

该实区间长度为：

```text
P/(q*r) < 2/r < 1.
```

所以至多一个整数商，唯一候选为：

```text
alpha_{P,k}(q,r)=floor(kP/(q*r))+1.
```

于是 residual edge 等价于：

```text
alpha<=floor(((k+1)P-1)/(q*r))
alpha>=r
q<=r*alpha<=2P-1
LPF(alpha)>=r
```

相位变成：

```text
D(q,r)=q*r*alpha_{P,k}(q,r)-kP
e(h*kP/q)=e(-h*D(q,r)/q).
```

有限实现审计读数：

```text
max_prime=1009
k_range=1<=k<P in this implementation audit
row_count=76954
active_residual_row_count=52697
total_prime_q_instances=3874554
total_lpf_r_row_instances=638542
total_qr_pair_instances=34664566
actual_total_edges_R30=299977
predicted_total_edges_R30=299977
predicted_total_triples=299977
reason_totals_on_qr={no_integer_quotient:31685737, quotient_below_lpf:894284, residual_lpf_descent_triple:299977, quotient_not_r_rough:918968, cofactor_clip_fail:865600}
lpf_r_bucket_totals={7:96700, 11:52080, 13:44104, 17:34414, 19:29723, 23:22368, 29:11815, 31:6916, 37:1559, 41:262, 43:36}
distinct_lpf_r_count=11
max_lpf_r_seen=43
max_quotient_interval_points=1
max_reverse_m_multiplicity=1
quotient_interval_unique_for_each_qr=true
predicted_edges_equal_actual_edges=true
predicted_triples_equal_edges=true
all_predicted_displacements_in_1_to_Pminus1=true
all_predicted_triples_have_lpf_descent=true
reverse_m_multiplicity_le_1=true
bad_quotient_interval_total=0
bad_displacement_total=0
bad_lpf_descent_total=0
missing_edge_total=0
extra_edge_total=0
```

外部前沿匹配：

```text
Milićević--Qin--Wu 2025 arXiv:2511.07550:
  relevant only after the (q,r,alpha) graph is completed to a genuine
  bilinear Kloosterman form.

Pascadi 2025 arXiv:2511.08445:
  possible Type-II completion technology, but not a pointwise estimate
  for this prime-q/small-r rough quotient graph.

Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113:
  relevant only after a finite-field/completion bridge; the present alpha
  graph is not already their square-free/smooth parameter family.

Dong--Robles--Zeindler 2026 arXiv:2601.00292:
  withdrawn on arXiv v2 and usable only as a near-miss diagnostic.
```

最新最窄口进一步压成：

```text
PrimeQSmallRoughQuotientCandidatePhaseSaving
AND CompletionToExternalKloostermanOrVaughanTypeII
```

状态边界：

```text
wheel30_composite_lpf_descent_closed=true
rough_quotient_graph_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 77. Phi-LPF rough quotient second LPF split closure 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_rough_quotient_second_lpf_split_closure_audit.py
data/prime-matrix-phi-lpf-rough-quotient-second-lpf-split-closure-ledger.json
docs/monograph/prime-matrix-phi-lpf-rough-quotient-second-lpf-split-closure-audit.json
docs/monograph/prime-matrix-phi-lpf-rough-quotient-second-lpf-split-closure-audit.md
```

本层继续选择行/列 Phi-LPF 的最快可闭合子门：

```text
RoughQuotientPrimeOrSecondLPFPartition
FixedPrimeQRSecondLPFQuotientSingleton
ResidualAsSemiprimeAlphaOrSecondRoughQuotientGraph
```

上一层已经把 residual edge 写成唯一三元图：

```text
m=r*alpha
r=LPF(m)
alpha=alpha_{P,k}(q,r)
LPF(alpha)>=r
```

本层把 `alpha` 分成两类：

```text
alpha is prime
OR
alpha=s*beta, s=LPF(alpha)>=r, beta>=s, LPF(beta)>=s.
```

固定 `(q,r,s)` 后，二级商区间长度为：

```text
P/(q*r*s)<2/(r*s)<=2/49<1.
```

所以至多一个整数商，唯一候选为：

```text
beta_{P,k}(q,r,s)=floor(kP/(q*r*s))+1.
```

相位仍为：

```text
D=q*r*alpha-kP
or D=q*r*s*beta-kP
phase=e(-hD/q).
```

有限实现审计读数：

```text
max_prime=1009
k_range=1<=k<P in this implementation audit
row_count=76954
active_residual_row_count=52697
actual_total_edges_R30=299977
predicted_total_edges_R30=299977
semiprime_alpha_total_edges=274812
second_lpf_total_edges=25165
predicted_second_quadruple_total=25165
split_totals_on_edges={semiprime_alpha_prime:274812, second_lpf_descent_cell:25165}
lpf_r_bucket_totals={7:96700, 11:52080, 13:44104, 17:34414, 19:29723, 23:22368, 29:11815, 31:6916, 37:1559, 41:262, 43:36}
second_rs_bucket_totals={7,7:15091, 7,11:6978, 7,13:1882, 11,11:1181, 11,13:33}
max_beta_interval_points=1
beta_interval_unique_for_each_qrs=true
predicted_edges_equal_actual_edges=true
two_cell_partition_exhaustive=true
second_quadruples_equal_second_edges=true
all_predicted_displacements_in_1_to_Pminus1=true
all_alpha_formulas_verified=true
all_beta_formulas_verified=true
all_second_lpf_descent_valid=true
bad_beta_interval_total=0
bad_alpha_formula_total=0
bad_beta_formula_total=0
bad_second_lpf_total=0
bad_displacement_total=0
missing_edge_total=0
extra_edge_total=0
```

外部前沿匹配：

```text
Milićević--Qin--Wu 2025 arXiv:2511.07550:
  useful only after completing the iterated rough quotient graph to a
  genuine bilinear Kloosterman form.

Pascadi 2025 arXiv:2511.08445:
  possible Type-II completion technology, not a pointwise estimate for
  this prime-q iterated quotient graph.

Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113:
  relevant only after a bridge to their square-free/smooth parameter family.

Dong--Robles--Zeindler 2026 arXiv:2601.00292:
  withdrawn on arXiv v2 and usable only as a near-miss diagnostic.
```

最新最窄口进一步压成：

```text
PrimeQIteratedRoughQuotientTwoCellPhaseSaving
AND CompletionToExternalKloostermanOrVaughanTypeII
```

状态边界：

```text
rough_quotient_second_lpf_split_closed=true
iterated_rough_quotient_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 78. Phi-LPF complete rough factor tree closure 审计

本层继续选择行/列 Phi-LPF 的最快可闭合子门：

```text
experiments/prime_matrix_phi_lpf_complete_rough_factor_tree_closure_audit.py
data/prime-matrix-phi-lpf-complete-rough-factor-tree-closure-ledger.json
docs/monograph/prime-matrix-phi-lpf-complete-rough-factor-tree-closure-audit.json
docs/monograph/prime-matrix-phi-lpf-complete-rough-factor-tree-closure-audit.md
```

上一层把 residual object 压成 semiprime-alpha 与 second-LPF 两个相位单元。
本层不再停在二级商，而是把每条 R30 residual cofactor 完整写成：

```text
m=p1*p2*...*pt
7<=p1<=p2<=...<=pt
```

对每个真前缀 `G_j=p1*...*pj`，剩余商 `A_j=m/G_j` 满足唯一公式：

```text
A_j=floor(kP/(q*G_j))+1
P/(q*G_j)<2/G_j<=2/7<1
```

因此本层关闭：

```text
CompleteRoughFactorTreeNormalForm
EveryPrefixRoughQuotientSingleton
DeterministicLPFDescentExhausted
```

有限审计读数：

```text
max_prime=1009
row_count=76954
active_residual_row_count=52697
actual_total_edges_R30=299977
predicted_complete_leaf_total=299977
max_factor_depth_observed=3
depth_totals={2:274812,3:25165}
max_prefix_interval_points=1
prefix_interval_unique_for_every_prefix=true
predicted_complete_leaves_equal_actual_edges=true
complete_factorization_valid=true
all_prefix_formulas_verified=true
all_predicted_displacements_in_1_to_Pminus1=true
bad_prefix_formula_total=0
bad_prefix_interval_total=0
bad_displacement_total=0
bad_factorization_total=0
missing_edge_total=0
extra_edge_total=0
```

外部前沿匹配：

```text
Milićević--Qin--Wu 2025 arXiv:2511.07550:
  candidate target only after completing complete rough-factor leaves to
  a genuine bilinear Kloosterman family.

Pascadi 2025 arXiv:2511.08445:
  possible Type-II technology only after reorganising the leaf tree into
  composite-modulus Type-II sums.

Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113:
  relevant only after replacing the pointwise floor-suffix graph by a
  completed square-free/smooth parameter family.

Ford--Maynard 2024 arXiv:2407.14368:
  prime-producing sieve guidance, but it requires object-specific
  Type-I/II inputs for these exact leaves.
```

最新最窄口进一步压成：

```text
PrimeQCompleteRoughFactorTreeLeafPhaseSaving
AND CompletionToExternalKloostermanOrVaughanTypeII
```

状态边界：

```text
complete_rough_factor_tree_closed=true
deterministic_lpf_descent_exhausted=true
complete_leaf_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 79. Phi-LPF complete leaf phase collapse 审计

本层继续选择行/列 Phi-LPF 的最快可闭合子门：

```text
experiments/prime_matrix_phi_lpf_complete_leaf_phase_collapse_audit.py
data/prime-matrix-phi-lpf-complete-leaf-phase-collapse-ledger.json
docs/monograph/prime-matrix-phi-lpf-complete-leaf-phase-collapse-audit.json
docs/monograph/prime-matrix-phi-lpf-complete-leaf-phase-collapse-audit.md
```

上一层已经把 residual object 写成完整粗因子叶子。本层关闭相位塌缩：

```text
D=qm-kP
D == -kP (mod q)
e(-hD/q)=e(h*kP/q)
```

因此完整因子树不提供固定 `q` 内部振荡；它只决定 prime-q 支撑集合。
本层关闭：

```text
CompleteLeafPhaseDependsOnlyOnPrimeQ
NoInternalFactorTreeOscillation
LeafTreePhaseSavingReducedToPrimeQSupportPhase
```

有限审计读数：

```text
max_prime=1009
row_count=76954
active_residual_row_count=52697
actual_total_edges_R30=299977
support_q_total=299977
support_q_total_equals_edge_total=true
max_q_leaf_multiplicity=1
q_multiplicity_totals={1:299977}
max_phase_residue_count_per_q=1
phase_residue_q_only_for_every_leaf=true
all_predicted_displacements_in_1_to_Pminus1=true
all_factor_leaves_valid=true
bad_phase_residue_total=0
bad_displacement_total=0
bad_factor_leaf_total=0
```

外部前沿匹配：

```text
Milićević--Qin--Wu 2025 arXiv:2511.07550:
  possible target only after converting the q-support reciprocal phase
  into a genuine bilinear Kloosterman family.

Pascadi 2025 arXiv:2511.08445:
  candidate only after reorganising the q-support phase into Type-II sums.

Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113:
  relevant only after a bridge to completed square-free/smooth parameter sums.

Ford--Maynard 2024 arXiv:2407.14368:
  prime-producing sieve guidance, but it does not verify Type-I/II
  estimates for this q-support set.
```

最新最窄口进一步压成：

```text
PrimeQSupportSetReciprocalPhaseSavingBeyondParity
AND CompletionToExternalKloostermanOrVaughanTypeII
```

状态边界：

```text
complete_leaf_phase_collapsed=true
internal_factor_tree_oscillation_available=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 46. 破奇偶候选源障碍审计

本层新增一个独立外部源筛查证书：

```text
experiments/prime_matrix_parity_breaking_obstruction_audit.py
data/prime-matrix-parity-breaking-obstruction-ledger.json
docs/monograph/prime-matrix-parity-breaking-obstruction-audit.json
docs/monograph/prime-matrix-parity-breaking-obstruction-audit.md
```

审计目的：把“破奇偶”候选源逐项验收到本文目标，而不是把不同结论类型直接导入。
五门为：

```text
PrimeObjectNotP2AlmostPrime
SquareScaleWindowOrP2ColumnCompatibility
RigidPointwiseGridOrFixedPrimeModulusZeroException
SameObjectNonlinearActualSourceConstructorBeforeProjection
UnconditionalPublishedOrIndependentlyAcceptedInput
```

当前读数：

```text
Li-Zhang-Cai P2 AP        -> square-compatible but wrong object
Friedlander-Iwaniec       -> genuine nonlinear prime model but not same object
BFI/DI/Kuznetsov/Maynard  -> technology class, no fixed q=P zero-exception theorem
Ford-Maynard framework    -> source-design guidance, no current matrix constructor
Maynard small gaps        -> prime object, wrong conclusion type
Rosser-Iwaniec sieve      -> parity-limited negative control
```

因此可引用的外部源仍未提供直接行/列闭合。最新剩余基为：

```text
PrimeObjectNotP2AlmostPrime
OR RigidPointwiseGridOrFixedPrimeModulusZeroException
OR SameObjectNonlinearActualSourceConstructorBeforeProjection
OR MeanValueAPToFixedPrimeModulusZeroExceptionTransfer
OR PointwiseShortIntervalPrimeTheoremThetaLeHalf
OR LinnikExponentLeTwoWithSquareWindowConstants
```

状态边界：

```text
direct_closure_candidate_count=0
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
row_column_unconditional_closed=false
```

## 42. 2026 AP 平均分布与条件 Linnik 近门槛压力层

本层继续更新 `experiments/prime_matrix_external_frontier_theorem_stress_router.py`
并重生成外部压力证书。新增外部输入：

```text
Stadlmann arXiv:2309.00425v3:
  smooth moduli average distribution to x^(1/2+1/40-eps)

Runbo Li arXiv:2505.09629v3:
  smooth-moduli prime minorant distribution level 10/19

Pascadi arXiv:2505.00653v2:
  weighted/well-factorable distribution up to x^(5/8-o(1))

Runbo Li arXiv:2602.20917v5:
  bilinear moduli x^(9/17), trilinear moduli x^(17/32), almost-all q AP bounds

Bruna arXiv:2603.25612v1:
  under generalized Lindelof, least AP prime p(a mod q) <<_eps q^(2+eps)
```

换算到 `x=P^2`：

```text
1/2+1/40 -> P^(1.05-o(1)) modulus range
10/19    -> P^(20/19) modulus range
5/8      -> P^(5/4-o(1)) modulus range
9/17     -> P^(18/17) modulus range
17/32    -> P^(17/16) modulus range
2+eps    -> P^(2+eps) conditional least-prime height
```

真实推进是新增门槛：

```text
mean_value_ap_to_fixed_prime_modulus:
  AP 平均分布即使越过 x^1/2，也不推出固定素模数 q=P 的全部 reduced residue classes
  在 P^2 方阵内同时有素数。需要零例外 fixed-prime-modulus transfer。
```

因此最新列方向硬点压缩为：

```text
MeanValueAPToFixedPrimeModulusZeroExceptionTransfer
OR ConditionalLinnikTwoPlusEpsilonToUnconditionalLinnikLeTwoWithConstants
OR NonlinearParityBreakingActualSourceConstructor
```

本层不把平均分布、smooth-moduli、weighted mean-value、minorant 或 GLH 条件近门槛误写为
无条件列闭合。

本层不把任何已知外部定理误写为目标命题无条件闭合。

## 40. K3''''/K3*-three-term：Dusart 三项显式 PNT 加强

新增文件：

```text
experiments/k3_threeterm_dusart_bound_check.py
docs/k3_threeterm_dusart_bound_check_run_20260522.txt
```

本层引入 Dusart 2010 三项显式下界：

```text
pi(x) >= x/log x * (1 + 1/log x + 1.8/log^2 x),  x >= 32299
```

把 K3''' 的单项 Dusart 加强推进为：

```text
K3'''':
|E(P)| < 3P/4 - P/(8 log P) - 0.1125 P/log^2 P,  P>=180

K3*-three-term:
|E*(P)| < 3P/4 - P/(8 log P) - 0.1125 P/log^2 P,  P>=180
```

数值核对 `P in [180,500]` 全部通过：

```text
all_pass_Dusart_3term_lower=true
all_pass_K3''''=true
all_pass_K3*-3term=true
```

这是真实的外部显式 PNT 常数推进；但主项仍为 `3P/4`，所以不关闭目标命题。它与
Baker-Harman-Pintz 连续空行块界合并后给出新的分布刚性：例外行即使存在，也不能聚成
长度超过 `P^(0.05+eps)` 的连续块，同时总量满足上述三项 K3'''' 上界。

## 43. K3'''' 系数自审纠错与 Dusart 上界常数收紧

新增文件：

```text
experiments/k3_quadruple_prime_corrected_check.py
docs/k3_quadruple_prime_corrected_check_run_20260523.txt
```

逐行重算 Dusart 三项贡献：

```text
0.225 P^2/log^3 P * logP/(2P) = 0.1125 P/log^2 P
```

因此早期 `0.05625` 系数是因子 2 算术偏差。修正后：

```text
K3''''-corrected:
|E(P)| < 3P/4 - P/(8 log P) - 0.1125 P/log^2 P,  P>=180

K3*-three-term-corrected:
|E*(P)| < 3P/4 - P/(8 log P) - 0.1125 P/log^2 P,  P>=180

K3-united-three-term-corrected:
|E(P)|+|E*(P)| < 3P/2 - P/(4 log P) - 0.225 P/log^2 P,  P>=180
```

另引入 Dusart 2010 上界 `pi(x)<=x/(log x-1.1)`，对 `P>=60184` 得到行方向精确常数项：

```text
|E(P)| <= 3P/4 - P/(8 log P) - 0.1125P/log^2 P
          - 1 + logP/(2(logP-1.1)).
```

数值核对 `P in [180,500]`：

```text
all_pass_K3''''_corrected_row=true
all_pass_K3''''_corrected_col=true
```

这是真实非循环纠错与常数推进；主项仍为 `3P/4`，所以不关闭目标命题。

## 44. K3-trivial-three-term-Li 内部自足三项加强

新增文件：

```text
experiments/k3_trivial_three_term_li_check.py
docs/k3_trivial_three_term_li_check_run_20260523.txt
```

用 `Li(x)` 的标准渐近展开

```text
Li(x) = x/log x * (1 + 1/log x + 2!/log^2 x + ...)
```

代入 `x=P^2` 后，第三项给出

```text
P^2/(2 log P) * 2/(4 log^2 P) = P^2/(4 log^3 P).
```

因此内部自足版推进为：

```text
K3-trivial-three-term-Li:
|E(P)| <= P - P/(2 log P) - P/(4 log^2 P) - P/(4 log^3 P)
          + O(P/log^4 P).

K3*-trivial-three-term-Li:
|E*(P)| <= P - P/(2 log P) - P/(4 log^2 P) - P/(4 log^3 P)
           + O(P/log^4 P).
```

数值审计 `P in [100,500]`：

```text
all_pass_K3-trivial-3term-Li_row=true
all_pass_K3-trivial-3term-Li_col=true
```

这是 PNT-only 内部链的真实三项推进；但主项仍为 `P`，弱于外部 sieve 链的 `3P/4`，
所以不关闭目标命题。

## 45. 外部前沿 residual-gap 审计

新增文件：

```text
experiments/prime_matrix_external_frontier_residual_gap_audit.py
data/prime-matrix-external-frontier-residual-gap-ledger.json
docs/monograph/prime-matrix-external-frontier-residual-gap-audit.json
docs/monograph/prime-matrix-external-frontier-residual-gap-audit.md
```

统一转换规则：

```text
pointwise short interval x^theta  ->  empty row-run residual P^(2theta-1+o(1))
least AP prime p(a mod P) << P^L ->  column square closure only if L<=2
average AP distribution           ->  needs fixed-prime-modulus zero-exception transfer
P2 almost-prime in AP              ->  enters square but wrong parity object
```

最新读数：

```text
Baker-Harman-Pintz theta=0.525      -> run residual exponent 0.05
Runbo Li v8 theta=0.52              -> run residual exponent 0.04 if accepted
Guth-Maynard/Hieu theta=17/30       -> row thickening P^(2/15+o(1))
Meng prime-modulus-compatible L=4.5 -> P^2.5 overshoot beyond P^2
Bruna GLH L=2+epsilon               -> conditional + P^epsilon overshoot
Li-Zhang-Cai P2 exponent 1.8345     -> square margin 0.1655 but wrong object
Pascadi weighted AP exponent 5/8    -> modulus range P^(5/4-o(1)), fixed q=P transfer open
```

因此最新真剩余基为：

```text
PointwiseShortIntervalPrimeTheoremThetaLeHalf
OR GridTransferredShortIntervalSecondMomentAtThetaHalf
OR LinnikExponentLeTwoWithSquareWindowConstants
OR MeanValueAPToFixedPrimeModulusZeroExceptionTransfer
OR ConditionalLinnikTwoPlusEpsilonToUnconditionalLinnikLeTwoWithConstants
OR NonlinearParityBreakingActualSourceConstructor
```

本层是真实的残差量化和防误用推进；它不关闭目标命题。

## 41. 2026-05-23 最新外部前沿版本核验与转换门槛

本层更新 `experiments/prime_matrix_external_frontier_theorem_stress_router.py`
并重生成：

```text
data/prime-matrix-external-frontier-theorem-stress-ledger.json
docs/monograph/prime-matrix-external-frontier-theorem-stress-router.json
docs/monograph/prime-matrix-external-frontier-theorem-stress-router.md
```

新增核验字段：

```text
frontier_verified_date=2026-05-23
best_arxiv_uniform_structural_theta=17/30
HieuPrimeAPsTheta17over30_structural_abundance_no_row_closure
```

外部源版本快照：

```text
BHP 2001 published: theta=0.525
Runbo Li arXiv:2308.04458v8 (2025-10-16): claimed theta=0.52
Guth-Maynard arXiv:2405.20552v2 (2026-04-07): theta>17/30 zero-density / short-interval PNT
Gafni-Tao arXiv:2505.24017v1 (2025-05-29): exceptional intervals / almost-all interface
Le Duc Hieu arXiv:2509.04883v2 (2025-09-24): prime AP abundance in theta>17/30 intervals
Li-Zhang-Cai arXiv:2103.13360v2: P2 almost-prime in AP with exponent 1.8345
Xylouris/Meng: Linnik/AP prime exponents still above 2
```

新增转换门槛：

```text
pointwise short interval theta  ->  empty-row-run exponent 2theta-1
least AP prime exponent L       ->  P^2 square only if L<=2
almost-all x                    ->  no rigid P-grid closure without a grid-transfer theorem
```

因此 Runbo Li v8 即便接受也只把连续空行串指数从 `0.05` 改进到 `0.04`；
Guth--Maynard/Hieu 的 `17/30` 结构结果只给 `P^(2/15+o(1))` 行厚度，
不能推出每个单行区间含素数。目标仍需：

```text
PointwiseShortIntervalPrimeTheoremThetaLeHalf
OR LinnikExponentLeTwoWithSquareWindowConstants
OR GridTransferredShortIntervalSecondMomentAtThetaHalf
OR NonlinearParityBreakingActualSourceConstructor
```

## 51. Prime-square half-scale specialization 审计

新增证书：

```text
experiments/prime_matrix_prime_square_halfscale_specialization_audit.py
data/prime-matrix-prime-square-halfscale-specialization-ledger.json
docs/monograph/prime-matrix-prime-square-halfscale-specialization-audit.json
docs/monograph/prime-matrix-prime-square-halfscale-specialization-audit.md
```

本层专门回答一个尺度问题：若通用短区间素数定理给出 `x^0.52`，
把端点限制为素数平方 `X=P^2` 是否因 `P` 的因子结构自动降到
`X^1/2=P`。结论是否定的：

```text
Baker-Harman-Pintz theta=0.525 -> X=P^2 gives P^1.05
Runbo Li v8 theta=0.52         -> X=P^2 gives P^1.04
target half-scale              -> P
```

`P` 为素数确实给出三个可证明结构收益：

```text
q=P is harmless for P^2±r, 1<=r<P
q<P gives square-phase forbidden residues r≡∓P^2 (mod q)
full avoidance of all q<P turns the survivor into a prime
```

但这些收益只是平方相位攻击面，不是外部短区间定理。右侧目标仍是：

```text
PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP:
  pi(P^2+P)-pi(P^2)>0
```

左侧 top-row 目标仍是：

```text
PrimeIndexedOppermannLeftTopRow:
  pi(P^2-1)-pi(P^2-P)>0
```

既有右侧有限审计 `P<=200000` 零失败只登记为有限证据，不升级为证明。
新的剩余基为：

```text
SquarePhaseSpecialPhaseLongBlockPDECExclusion
OR TwoSidedSquarePhaseLayeredWheelSurvivorLowerBound
OR PrimeSquareEndpointNoExceptionalPhaseTheorem
OR PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP
OR PuncturedWheel6EndpointCapacityInequalityOrReciprocalPrimePairWheel6SaturationPDEC
OR ExactExternalSqrtScaleOrFullSNonAPWFDKLSTheoremMatch
OR NewAutomorphicDispersionProof
```

边界状态：

```text
prime_square_halfscale_auto_drop_closed=false
square_phase_attack_surface_identified=true
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
row_column_unconditional_closed=false
```

## 52. Prime-square `P^2±1` sandwich 审计

新增证书：

```text
experiments/prime_matrix_prime_square_pm1_sandwich_audit.py
data/prime-matrix-prime-square-pm1-sandwich-ledger.json
docs/monograph/prime-matrix-prime-square-pm1-sandwich-audit.json
docs/monograph/prime-matrix-prime-square-pm1-sandwich-audit.md
```

本层审计更强的夹击想法：对 `X=P^2-1` 与 `X=P^2+1` 同时应用
`x^0.52` 短区间素数输入，能否把素数压进 `P^2` 两侧长度 `P` 的半窗。

尺度展开为：

```text
(P^2±1)^theta = P^(2theta)(1+O(P^-2))
theta=0.52
(P^2±1)^0.52 = P^1.04(1+O(P^-2))
absolute ±1 length change = O(P^-0.96)
```

因此 `±1` 只改变端点相位，不改变指数。夹击得到的是：

```text
right container: (P^2+1, P^2+1+(P^2+1)^0.52]
target right:    (P^2, P^2+P)
open outer tail: [P^2+P, P^2+P^1.04+O(1)]

left container:  [P^2-1-(P^2-1)^0.52, P^2-1)
target left:     (P^2-P, P^2)
open outer tail: [P^2-P^1.04+O(1), P^2-P]
```

单个短区间定理只给容器内 `at_least_one_prime`。外尾段长度仍为
`P^1.04-P`，Brun--Titchmarsh 型容量仍有 `P^1.04/log P` 量级；它不为空，
所以无法推出保证素数落入内侧长度 `P` 的半窗。

新的剩余基为：

```text
PM1OuterTailExclusionForTheta052Containers
OR PrimeSquareNearestPrimeWithinPOnAtLeastOneSide
OR TwoSidedSquarePhaseInnerWindowLocalization
OR SquarePhaseSpecialPhaseLongBlockPDECExclusion
OR PuncturedWheel6EndpointCapacityInequalityOrReciprocalPrimePairWheel6SaturationPDEC
OR ExactExternalSqrtScaleOrGridTransferredThetaHalfSecondMoment
OR NewSameObjectSignedDispersionOrAutomorphicProof
```

边界状态：

```text
pm1_sandwich_halfscale_closed=false
pm1_sandwich_no_go_closed=true
prime_square_halfscale_auto_drop_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
row_column_unconditional_closed=false
```

## 53. Legendre-frontier 外部定理审计

新增证书：

```text
experiments/prime_matrix_legendre_frontier_external_audit.py
data/prime-matrix-legendre-frontier-external-ledger.json
docs/monograph/prime-matrix-legendre-frontier-external-audit.json
docs/monograph/prime-matrix-legendre-frontier-external-audit.md
```

本层登记 2026 年 Legendre/平方间隔方向最相关的新外部源，并统一映射到
`P^2±P` 半窗目标。

外部源快照：

```text
Chamberland--Straub 2026:
  RH 条件 primes between x^(2+delta) and (x+1)^(2+delta), delta>0.
  不含 delta=0；非无条件。

Campbell 2026:
  every square interval contains a P3 almost-prime.
  位置正确；对象不是 prime。

Bordignon--Johnston--Starichkova:
  explicit Chen / linear sieve 技术。
  支撑 almost-prime 结果；仍受 parity barrier。

Guth--Maynard 2026 Annals:
  theta=17/30 short-interval PNT technology.
  X=P^2 后仍需 P^(2/15) 行厚度。

Lee 2026:
  kth-power zero-free-region progress for large k.
  不触及 k=2 square case。
```

RH larger-powers 的尺度为：

```text
length exponent = (1+delta)/(2+delta)
                 = 1/2 + delta/(2(2+delta)).
```

因此 `delta=1/4` 给 `5/9`，`delta=0.01` 仍给 `0.502487...`；
极限接近 `1/2`，但 `delta=0` 正是 Legendre/prime-square halfscale 硬点。

新的剩余基为：

```text
DeltaZeroLegendreOrPrimeSquareHalfscaleTheorem
OR P3ToPrimeParityBreakingTransferOrObjectSensitiveSignedSieve
OR ThetaLeHalfPointwiseShortIntervalPrimeTheorem
OR GridTransferredThetaHalfSecondMoment
OR PrimeSquareSpecialPhaseNoOuterTailTheorem
OR NewSameObjectSignedDispersionOrAutomorphicProof
```

边界状态：

```text
legendre_frontier_external_inputs_imported=true
rh_larger_powers_delta_zero_closed=false
p3_to_prime_transfer_closed=false
prime_square_halfscale_closed=false
row_column_unconditional_closed=false
```

## 54. 短区间转移法奇偶审计

新增证书：

```text
experiments/prime_matrix_short_interval_transference_parity_audit.py
data/prime-matrix-short-interval-transference-parity-ledger.json
docs/monograph/prime-matrix-short-interval-transference-parity-audit.json
docs/monograph/prime-matrix-short-interval-transference-parity-audit.md
```

本层审计短区间 AP/Green--Tao 转移、BDH 均方和 L-function-free 技术是否
能从外部突破 Phi-LPF 奇偶障碍。

外部源快照：

```text
Le Duc Hieu 2025:
  k-term prime APs in [x,x+x^theta], theta>17/30.
  这是厚短区间素数模式丰度，不是 prime-square 首行定位。

Guth--Maynard 2026:
  theta=17/30 short-interval PNT technology.
  X=P^2 后仍有 P^(2/15) 行厚度。

Green--Tao/W-trick:
  转移素数模式和小素数偏差。
  不等于筛掉所有 q<P 的 Phi-LPF residue covers。

BDH/平均 AP 输入:
  控制多数模数或均方误差。
  不排除所有 prime-square exceptional phase。

Matomaki--Merikoski--Teravainen:
  L-function-free AP/short-interval 技术有方法价值。
  尺度仍远大于半窗。
```

尺度换算：

```text
X=P^2, interval length X^theta=P^(2theta).
target theta=1/2 -> P.
theta=17/30 -> P^(17/15)=P*P^(2/15).
theta=17/30+epsilon -> P^(17/15+2epsilon).
```

因此，只要 `theta>1/2`，容器

```text
(P^2, P^2+P^(2theta)]
```

的外尾段

```text
[P^2+P, P^2+P^(2theta)]
```

长度仍与整个厚容器同阶；素数 AP 或素数丰度完全可能被外尾段吸收。

新的剩余基为：

```text
ThetaLeHalfUniformShortIntervalPrimeTheorem
OR APPatternLocalizationInsidePrimeSquareHalfWindow
OR BDHNoExceptionalPrimeSquarePhaseTheorem
OR WTrickToFullPhiLPFObjectSensitiveSieve
OR MaynardClusterAnchoredAtEveryPrimeSquare
OR SameObjectSignedDispersionOrAutomorphicEndpointProof
```

边界状态：

```text
short_interval_transference_inputs_imported=true
prime_pattern_to_first_row_transfer_closed=false
w_trick_phi_lpf_parity_closed=false
bdh_pointwise_all_rows_closed=false
prime_square_halfscale_closed=false
row_column_unconditional_closed=false
```

## 55. almost-all 例外脊线审计

新增证书：

```text
experiments/prime_matrix_almost_all_exceptional_spine_audit.py
data/prime-matrix-almost-all-exceptional-spine-ledger.json
docs/monograph/prime-matrix-almost-all-exceptional-spine-audit.json
docs/monograph/prime-matrix-almost-all-exceptional-spine-audit.md
```

本层审计 almost-all 短区间素数、exceptional intervals 和高阶一致性输入是否
能绕开 Phi-LPF 奇偶障碍。

外部源快照：

```text
Runbo Li 2025:
  almost all [n,n+n^(1/21.5+epsilon)] contain primes.
  X=P^2 后长度 P^(4/43)，若点态化则强过目标。

Runbo Li II working paper:
  almost all left intervals of length n^(1/22+epsilon).
  X=P^2 后长度 P^(1/11)，但仍是 working paper 与 almost-all。

Gafni--Tao 2025:
  exceptional intervals framework; all x for theta>17/30, almost all x for theta>2/15.
  X=P^2 后 theta=2/15 给 P^(4/15)，但例外集未排除 prime-square spine。

Matomaki--Radziwill--Shao--Tao--Teravainen:
  almost all short intervals higher uniformity for Lambda/mu/divisor functions.
  深层一致性输入，不是每个 P^2 端点的点态定理。
```

素数平方脊线在 dyadic 块中的大小为：

```text
{P^2: P prime, X<=P^2<=2X}
size asymp X^(1/2)/log X
density asymp 1/(X^(1/2)log X)
```

因此 `almost all x` 允许的稀疏例外集原则上仍可包含全部素数平方端点。
要把 almost-all 输入升级为 Prime Matrix 闭合，必须新增：

```text
ExceptionalPrimeSquareSpineDisjointness
OR PointwiseEndpointUniformityAtEveryPrimeSquare
OR AlmostAllToAllRowsUpgradeWithArithmeticSpineRepulsion
```

新的剩余基为：

```text
ExceptionalPrimeSquareSpineDisjointness
OR PointwiseEndpointUniformityAtEveryPrimeSquare
OR AlmostAllToAllRowsUpgradeWithArithmeticSpineRepulsion
OR NoPrimeSquareExceptionalPhaseForGafniTaoBounds
OR PhiLPFObjectSensitiveSignedSieveOnSparseSpine
OR ThetaLeHalfPointwiseShortIntervalPrimeTheorem
```

边界状态：

```text
almost_all_short_interval_inputs_imported=true
scale_stronger_than_halfwindow_if_pointwise=true
exceptional_prime_square_spine_excluded=false
pointwise_every_prime_square_endpoint_closed=false
phi_lpf_parity_closed=false
row_column_unconditional_closed=false
```

## 56. prime-power slope sandwich 审计

新增证书：

```text
experiments/prime_matrix_prime_power_slope_sandwich_audit.py
data/prime-matrix-prime-power-slope-sandwich-ledger.json
docs/monograph/prime-matrix-prime-power-slope-sandwich-audit.json
docs/monograph/prime-matrix-prime-power-slope-sandwich-audit.md
```

本层审计用户提出的新夹击：

```text
(P^(50/24))^0.52 and (P^(50/26))^0.52
target: (P^(50/25))^0.5 = P
```

取 `0.52=13/25`，则指数恒等式为：

```text
lower endpoint: P^(50/26)=P^(25/13)
(P^(25/13))^(13/25)=P

center endpoint: P^(50/25)=P^2
(P^2)^(1/2)=P

upper endpoint: P^(50/24)=P^(25/12)
(P^(25/12))^(13/25)=P^(13/12)
```

这里确有长度巧合，但容器位置不对。下端容器位于 `P^(25/13)` 附近，
到 `P^2` 的距离为：

```text
P^2-P^(25/13)=P^2(1-P^(-1/13)) asymp P^2,
```

而保证半径只有 `P`。上端容器位于 `P^(25/12)` 附近，到 `P^2` 的距离为：

```text
P^(25/12)-P^2=P^2(P^(1/12)-1) asymp P^(25/12),
```

而保证半径只有 `P^(13/12)`。两端都差一个 `P` 因子，不能触及 `P^2`
半窗。

一般形式：

```text
X=P^a, short interval length X^theta=P^(a theta).
location at P^2 requires a=2.
radius P requires a theta=1.
simultaneous solution requires theta=1/2.
```

对 `theta=13/25`，半径 `P` 强制 `a=25/13`，这恰好偏离 `P^2`。

新的剩余基为：

```text
PrimeSquareEndpointLocalizationNotExponentInterpolation
OR ThetaEqualsHalfOrPrimeSquareSpecificPointwiseTheorem
OR P2CenteredContainerPrimeLowerBound
OR OuterScaleGapBridgeBetweenP25Over13AndP2
OR SameObjectSignedDispersionOrAutomorphicEndpointProof
```

边界状态：

```text
prime_power_slope_sandwich_no_go_closed=true
exponent_length_coincidence_closed=true
lower_container_reaches_p2=false
upper_container_reaches_p2=false
prime_square_halfscale_closed=false
row_column_unconditional_closed=false
```

## 57. Phi-LPF punctured endpoint 30-wheel capacity 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_punctured_endpoint_wheel30_capacity_router.py
data/prime-matrix-phi-lpf-punctured-endpoint-wheel30-capacity-ledger.json
docs/monograph/prime-matrix-phi-lpf-punctured-endpoint-wheel30-capacity-router.json
docs/monograph/prime-matrix-phi-lpf-punctured-endpoint-wheel30-capacity-router.md
```

上一层已经得到 Euler `6`-wheel ceiling：

```text
|F(P,k)| <= C_6(P,k)=W_int(P,k)-E_{2,3}(P,k).
```

本层继续加入 `5` 的 forced-composite 扣除。若 reciprocal cofactor
候选 `m>5` 且 `5|m`，则 `m` 不可能为素数，因此

```text
|F(P,k)| <= C_30(P,k)=W_int(P,k)-E_{2,3,5}(P,k)
DeltaPhi_half(P,k)>C_30(P,k) => pi((k+1)P-1)-pi(kP)>0
```

有限审计读数：

```text
max_prime=1009
row_count=76789
closed_by_wheel6_ceiling_count=76789
closed_by_wheel30_ceiling_count=76789
wheel6_not_closed_count=0
wheel30_not_closed_count=0
wheel30_nonpositive_margin_count=0
```

关键样本：

```text
P=1009, k=1008, Delta=89, W_int=101, C_6=34, C_30=28, Delta-C_30=61
P=997, k=952, maximum extra deletion beyond C_6 = 16
```

大样本 `P=100003,300007` 的抽样最小 `Delta-C_30` 为 `3215`。
这是真推进：它把 6-wheel endpoint capacity 严格收紧到 30-wheel
endpoint capacity。但它仍只是 forced-composite 容量层，不是全局
Phi-LPF 奇偶障碍突破。

新的剩余基：

```text
PuncturedWheel30EndpointCapacityInequalityOrReciprocalPrimePairWheel30SaturationPDEC
OR ExactExternalSqrtScaleOrFullSNonAPWFDKLSTheoremMatch
OR NewAutomorphicDispersionProof
OR SpecialSquarePhaseStructuralLowerBoundBeyondParity
OR PhiLPFObjectSensitiveSignedValueTable
```

外部源状态未改变：Baker--Harman--Pintz `0.525` 与 Runbo Li `0.52`
短区间指数仍大于 `1/2`；AP 平均分布、P2 almost-prime 与
prime-producing sieve 框架仍不能直接给出本文同对象 fixed-row positivity。

状态边界：

```text
phi_lpf_wheel30_capacity_tightened=true
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 58. Phi-LPF primorial-wheel limit 审计

新增证书：

```text
experiments/prime_matrix_phi_lpf_primorial_wheel_limit_audit.py
data/prime-matrix-phi-lpf-primorial-wheel-limit-ledger.json
docs/monograph/prime-matrix-phi-lpf-primorial-wheel-limit-audit.json
docs/monograph/prime-matrix-phi-lpf-primorial-wheel-limit-audit.md
```

本层回答 `30-wheel` 是否可继续到：

```text
210, 2310, 30030, ..., 2*3*5*7*11*...*p_j
```

答案分成两部分。首先，有限 primorial wheel ladder 确实单调收紧，因为每一层
只删除更多被小素数强迫合成的 reciprocal cofactor 候选。有限审计读数：

```text
max_prime=1009
row_count=76789
all_exact_capacity_equals_holes=true
all_exact_margin_equals_direct_prime_count=true
```

代表行：

```text
P=1009, k=1008
Delta=89, W_int=101, C_30=28, C_210=27, C_2310=26, C_sqrt=19, holes=19, primes=70
```

其次，当 wheel primes 覆盖到 `sqrt(2P-1)` 后，所有合数 `m<2P` 都被删除，
未删的 cofactor `m` 恰好是素数。因此：

```text
C_sqrt(P,k)=|F(P,k)|
DeltaPhi_half(P,k)-C_sqrt(P,k)=pi((k+1)P-1)-pi(kP)
```

这说明 infinite primorial-wheel limit 是目标命题的精确等价形式，不是一个
独立证明。继续加 wheel 可以把容量上界逼近真实 holes，但要证明目标仍必须证明
这个精确差为正，或提供新的带符号/谱/结构性输入。

新的剩余基：

```text
PuncturedSqrtWheelExactForestHolePositivityOrSignedDispersionOrSpecialSquarePhaseLowerBound
OR ExactExternalSqrtScaleOrFullSNonAPWFDKLSTheoremMatch
OR NewAutomorphicDispersionProof
OR PhiLPFObjectSensitiveSignedValueTable
OR PointwiseShortIntervalPrimeTheoremThetaLeHalf
```

外部前沿状态未改变：已发表 BHP `0.525` 与 Runbo Li `0.52` 仍大于 `1/2`；
AP 平均分布、P2 almost-prime 与 prime-producing sieve 框架仍不能直接给出本文
同对象 fixed-row positivity。

状态边界：

```text
primorial_wheel_ladder_tightened=true
sqrt_wheel_limit_exact=true
primorial_limit_independent_proof=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
## 65Y. Phi-LPF q-prefix single-P local gap2/gap4 top-two core largest-atom dominant sign-word dominant m-pair path 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_qsupport_row_averaged_additive_k_prime_survivor_boundary_endpoint_flux_qprefix_carry_cycle_signature_single_p_local_gap2_gap4_top_two_core_largest_atom_dominant_sign_word_dominant_m_pair_path_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-dominant-sign-word-dominant-m-pair-path-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-dominant-sign-word-dominant-m-pair-path-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-dominant-sign-word-dominant-m-pair-path-audit.md
```

上一层 dominant sign word `--+-+` 的最大 `m_pair` 子块为 `[769, 773]`，
质量 `20`。本层把该子块继续拆成 2 个端点坐标路径见证：

```text
dominant_m_pair_endpoint_coordinate_path_ledger_closed=true
target_sign_word=--+-+
target_m_pair=[769, 773]
endpoint_coordinate_witness_count=2
endpoint_coordinate_edge_mass=20
all_endpoint_edge_mass_equals_10=true
all_endpoint_integer_gap_equals_4=true
all_endpoint_occurrence_count_equals_2=true
all_endpoint_q_prefix_band_q_le_10=true
all_endpoint_m_shell_band_m_le_4=true
all_endpoint_cycle_length_equals_5=true
all_endpoint_sign_word_is_target=true
all_endpoint_sign_switch_count_equals_3=true
distinct_raw_base_template_count=2
distinct_signed_child_count=2
```

坐标上，一个 witness 是 `P=607` 的 `above_P` 路径，offset `[162,166]`；
另一个是 `P=953` 的 `below_P` 路径，offset `[-184,-180]`。这一步删除了
dominant `m_pair` 仍可隐藏 20 质量整体黑箱的说法。

外部 theorem 边界仍不变：FKMS trace bilinear、Milićević--Qin--Wu
任意模 Kloosterman、Wright unbalanced Kloosterman fractions 等平均型输入
仍需要先把这两个 fixed endpoint coordinate witness 完成到非局部 family；
Maynard small gaps 与 Li short interval primes 不直接估计 fixed signed path equality。

状态边界：

```text
dominant_m_pair_endpoint_coordinate_path_ledger_closed=true
dominant_m_pair_endpoint_coordinate_family_bound_proved=false
dominant_sign_word_path_family_bound_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
## 65Z. Phi-LPF q-prefix single-P local gap2/gap4 top-two core largest-atom dominant sign-word m-pair coordinate partition 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_dominant_sign_word_mpair_coordinate_partition_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-dominant-sign-word-m-pair-coordinate-partition-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-dominant-sign-word-m-pair-coordinate-partition-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-dominant-sign-word-m-pair-coordinate-partition-audit.md
```

本层把 dominant sign word `--+-+` 的全部 30 质量统一落到 m-pair/offset/orientation
坐标分区：

```text
dominant_sign_word_m_pair_coordinate_partition_ledger_closed=true
path_template_count=3
path_edge_mass=30
all_path_edge_mass_equals_10=true
all_path_integer_gap_equals_4=true
all_path_occurrence_count_equals_2=true
all_path_m_shell_band_m_le_4=true
all_path_cycle_length_equals_5=true
all_path_sign_word_is_target=true
distinct_m_pair_count=2
dominant_m_pair=[769, 773]
dominant_m_pair_edge_mass=20
residual_singleton_m_pair=[757, 761]
residual_singleton_m_pair_edge_mass=10
residual_singleton_coordinate_closed=true
above_P_edge_mass=20
below_P_edge_mass=10
q_prefix_band_q_le_10_edge_mass=20
q_prefix_band_q_gt_20_edge_mass=10
```

三个坐标 witness 为：

```text
P=607, m_pair=[769,773], above_P, offsets=[162,166], q_prefix_count=7
P=739, m_pair=[757,761], above_P, offsets=[18,22], q_prefix_count=28
P=953, m_pair=[769,773], below_P, offsets=[-184,-180], q_prefix_count=10
```

外部 theorem 边界仍不变：trace/Kloosterman 平均型输入仍需要先完成到非局部
family；prime-gap 与短区间素数输入仍不直接估计 fixed endpoint-coordinate
signed equality。

状态边界：

```text
dominant_sign_word_m_pair_coordinate_partition_ledger_closed=true
dominant_sign_word_endpoint_coordinate_family_bound_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
## 65AA. Phi-LPF q-prefix single-P local gap2/gap4 top-two core largest-atom dominant sign-word step-transition 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_dominant_sign_word_step_transition_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-dominant-sign-word-step-transition-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-dominant-sign-word-step-transition-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-dominant-sign-word-step-transition-audit.md
```

本层把 dominant sign word `--+-+` 的三条 m-pair coordinate path 拆成
signed step atoms 与 adjacent transition atoms：

```text
dominant_sign_word_step_transition_ledger_closed=true
coordinate_witness_count=3
coordinate_witness_edge_mass=30
step_atom_count=15
step_atom_mass=150
transition_atom_count=12
transition_atom_mass=120
all_witness_length_equals_5=true
all_step_atom_mass_equals_10=true
all_transition_atom_mass_equals_10=true
all_initial_steps_negative=true
all_terminal_steps_positive=true
sign_word_position_law_closed=true
transition_sign_law_closed=true
negative_step_mass=90
positive_step_mass=60
same_sign_transition_mass=30
sign_switch_transition_mass=90
distinct_signed_step_atom_count=13
repeated_signed_step_atom_count=2
```

重复 step 原子恰为：

```text
g=2,c=2,A=negative -> mass 20
g=6,c=7,A=positive -> mass 20
```

外部 theorem 边界仍不变：这些 step/transition atoms 仍需先聚合为非局部
trace、bilinear 或 Kloosterman family；FKMS、Milićević--Qin--Wu、Wright
等平均型输入不直接估计固定 grammar，Maynard prime gaps 与 Li short intervals
也不直接给出 signed path equality。

状态边界：

```text
dominant_sign_word_step_transition_ledger_closed=true
dominant_sign_word_step_transition_family_bound_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65AB. Phi-LPF q-prefix single-P local gap2/gap4 top-two core largest-atom dominant sign-word repeated-step occurrence 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_repeated_step_occurrence_audit.py
data/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-dominant-sign-word-repeated-step-occurrence-ledger.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-dominant-sign-word-repeated-step-occurrence-audit.json
docs/monograph/prime-matrix-phi-lpf-qsupport-row-averaged-additive-k-prime-survivor-boundary-endpoint-flux-qprefix-carry-cycle-signature-single-p-local-gap2-gap4-top-two-core-largest-atom-dominant-sign-word-repeated-step-occurrence-audit.md
```

本层承接 65AA，只处理 step-transition 账本里的两个 repeated signed step
atoms，把它们拆成 occurrence 位置与 touching transition：

```text
dominant_sign_word_repeated_step_occurrence_ledger_closed=true
repeated_signed_step_atom_count=2
repeated_signed_step_atoms={g=2,c=2,A=negative:20, g=6,c=7,A=positive:20}
repeated_step_occurrence_count=4
repeated_step_occurrence_mass=40
endpoint_role_law_closed=true
touching_transition_count=5
touching_transition_mass=50
touching_transition_repeated_endpoint_incidence_count=6
touching_transition_repeated_endpoint_incidence_mass=60
```

精确 occurrence 为：

```text
g=2,c=2,A=negative: P607 step1 [769,773] above_P; P739 step4 [757,761] above_P
g=6,c=7,A=positive: P607 step3 [769,773] above_P; P739 step5 [757,761] above_P
```

外部 theorem 边界仍不变：FKMS、Milićević--Qin--Wu 与 Wright 型
trace/Kloosterman 平均输入需要先把这些局部 grammar 数据提升为非局部可求和族；
Maynard 小间距与 Li 短区间素数结果也不直接推出 repeated-step uniform
collision bound。

状态边界：

```text
dominant_sign_word_repeated_step_occurrence_ledger_closed=true
dominant_sign_word_repeated_step_family_bound_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65AC. Phi-LPF dominant sign-word repeated-step directed-incidence graph 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_repeated_step_incidence_graph_audit.py
data/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-directed-incidence-graph-ledger.json
docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-directed-incidence-graph-audit.json
docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-directed-incidence-graph-audit.md
```

本层承接 65AB，把 repeated-step 的五条 touching transition 视为有向
incidence graph：

```text
repeated_step_directed_incidence_graph_ledger_closed=true
node_count=5
repeated_node_count=2
neighbor_node_count=3
directed_edge_count=5
directed_edge_mass=50
repeated_endpoint_incidence_count=6
weak_component_count=1
directed_acyclic=true
source_nodes=[g=6,c=6,A=positive]
sink_nodes=[g=8,c=10,A=negative]
longest_directed_path_length=4
cross_repeated_bridge_edge_count=1
```

edge-class 质量为：

```text
neighbor_to_repeated=20
repeated_to_neighbor=20
repeated_to_repeated=10
```

最长有向链为：

```text
g=6,c=6,A=positive
-> g=2,c=2,A=negative
-> g=4,c=5,A=negative
-> g=6,c=7,A=positive
-> g=8,c=10,A=negative
```

外部 theorem 边界仍不变：该有限 DAG 仍不是 trace/bilinear/Kloosterman
可求和族；FKMS、Milićević--Qin--Wu、Wright 的平均型输入，以及 Maynard
小间距和 Li 短区间素数结果，都不直接给出这个 directed-incidence family
bound。

状态边界：

```text
repeated_step_directed_incidence_graph_ledger_closed=true
repeated_step_directed_incidence_graph_family_bound_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65AD. Phi-LPF dominant sign-word repeated-step source-sink path-cover 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_repeated_step_path_cover_audit.py
data/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-source-sink-path-cover-ledger.json
docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-source-sink-path-cover-audit.json
docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-source-sink-path-cover-audit.md
```

本层承接 65AC，把 repeated-step DAG 的所有 source-sink 图路径枚举为
path-cover 账本：

```text
repeated_step_source_sink_path_cover_ledger_closed=true
source_node=g=6,c=6,A=positive
sink_node=g=8,c=10,A=negative
source_sink_path_count=2
source_sink_path_edge_incidence_count=7
source_sink_path_edge_incidence_mass=70
edge_cover_complete=true
shared_edge_count=2
shared_edge_mass=20
shared_edge_path_incidence_mass=40
single_witness_source_sink_path_count=0
mixed_witness_source_sink_path_count=2
all_source_sink_paths_mixed_P=true
all_source_sink_paths_have_one_P_switch=true
diamond_decomposition_closed=true
single_witness_orbit_interpretation_valid=false
```

两条图路径为：

```text
g=6,c=6,A=positive -> g=2,c=2,A=negative -> g=4,c=5,A=negative -> g=6,c=7,A=positive -> g=8,c=10,A=negative
g=6,c=6,A=positive -> g=2,c=2,A=negative -> g=6,c=7,A=positive -> g=8,c=10,A=negative
```

关键边界：两条 source-sink 图路径都混合 `P=607` 与 `P=739`，所以它们
只是 signature graph stitching，不能当作 single witness orbit。FKMS、
Milićević--Qin--Wu 与 Wright 型 trace/Kloosterman 平均输入仍需要先把这个
mixed-P stitching 提升为可求和族；Maynard 小间距与 Li 短区间素数结果也不
直接推出该 path-cover uniform bound。

状态边界：

```text
repeated_step_source_sink_path_cover_ledger_closed=true
repeated_step_source_sink_path_cover_family_bound_proved=false
single_witness_orbit_interpretation_valid=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65AE. Phi-LPF dominant sign-word repeated-step P-switch cut 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_repeated_step_p_switch_cut_audit.py
data/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-p-switch-cut-ledger.json
docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-p-switch-cut-audit.json
docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-p-switch-cut-audit.md
```

本层承接 65AD，把 mixed-P source-sink path cover 中每条路径的唯一
P-switch 局部化到 adjacent edge pair：

```text
repeated_step_p_switch_cut_ledger_closed=true
path_switch_cut_count=2
switch_nodes=[g=2,c=2,A=negative, g=6,c=7,A=positive]
repeated_switch_node_cover_complete=true
neighbor_switch_node_count=0
all_switches_at_repeated_nodes=true
all_switches_high_to_low=true
all_switches_739_to_607=true
switch_pair_edge_mass_total=40
switch_edge_incidence_count=4
switch_edge_incidence_mass=40
switch_edge_unique_count=4
non_switch_edge_unique_count=1
```

两个 cut 为：

```text
path_1: g=6,c=6,A=positive -> g=2,c=2,A=negative || g=2,c=2,A=negative -> g=4,c=5,A=negative
path_2: g=2,c=2,A=negative -> g=6,c=7,A=positive || g=6,c=7,A=positive -> g=8,c=10,A=negative
```

这把 mixed-P obstruction 从整条 graph path 压缩到两个 repeated nodes 上的
`739_to_607` cut。外部 theorem 边界仍不变：FKMS、Milićević--Qin--Wu 与
Wright 型 trace/Kloosterman 平均输入需要可求和族；Maynard 小间距与 Li
短区间素数不控制这种 signed grammar P-switch cut。

状态边界：

```text
repeated_step_p_switch_cut_ledger_closed=true
p_switch_cut_uniform_family_bound_proved=false
single_p_orbit_repair_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 附录 Q13AC35：small-to-large factor-peeling signed-state 边界（2026-05-25）

新增证书：

```text
experiments/prime_matrix_phi_lpf_small_to_large_factor_peeling_signed_state_boundary_router.py
data/prime-matrix-phi-lpf-small-to-large-factor-peeling-signed-state-boundary-ledger.json
docs/monograph/prime-matrix-phi-lpf-small-to-large-factor-peeling-signed-state-boundary-router.json
docs/monograph/prime-matrix-phi-lpf-small-to-large-factor-peeling-signed-state-boundary-router.md
```

本层不引入新外部定理。它把 LPF-owned composite buckets 的 cofactor 从小到大剥离，
并把 squarefree、Möbius、Liouville 与 depth parity 全部登记为 factor word 的机械状态。
审计边界：

```text
small_to_large_factor_peeling_verified_all_samples=true
mobius_liouville_state_computable_from_factor_word_all_samples=true
peeling_generates_new_precauchy_signed_payload=false
orientation_local_factor_law_proved=false
built_in_signed_pairing_proved=false
row_column_unconditional_closed=false
```

因此外部 trace/Kloosterman/Type-II 定理仍没有新的 admissible family 入口。若要调用
FKMS、Milićević--Qin--Wu、Pascadi、Wright 或 DI/BFI/Kuznetsov，仍必须先提交
pre-Cauchy signed payload 或 atomic built-in pairing。新的开放口为：

```text
PrimitiveOrientationLocalFactorProductLawBeforePushforward
OR BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows
```

## 65AF. Phi-LPF dominant sign-word repeated-step occurrence-splice 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_repeated_step_occurrence_splice_audit.py
data/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-occurrence-splice-ledger.json
docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-occurrence-splice-audit.json
docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-occurrence-splice-audit.md
```

本层承接 65AE，把两个 repeated-node P-switch cut 的左右端点解析回具体
occurrence：

```text
repeated_step_occurrence_splice_ledger_closed=true
occurrence_splice_count=2
occurrence_splice_mass_total=40
occurrence_splice_endpoint_count=4
occurrence_splice_endpoint_mass=40
occurrence_splice_endpoint_cover_complete=true
all_splices_same_signed_atom=true
all_splices_same_gap_carry=true
all_splices_same_sign=true
all_splices_same_orientation=true
all_splices_739_to_607=true
all_splices_m_pair_delta_12_12=true
all_splices_q_delta_minus_21=true
all_splices_step_rewind=true
step_rewind_total=5
```

两条 splice 为：

```text
g=2,c=2,A=negative: P739 step4 [757,761] q28 -> P607 step1 [769,773] q7
g=6,c=7,A=positive: P739 step5 [757,761] q28 -> P607 step3 [769,773] q7
```

这把 repeated-node `739_to_607` cut 进一步压缩为 same signed atom 的
cross-witness occurrence splice。外部 theorem 边界仍不变：trace/bilinear/
Kloosterman 前沿输入需要可求和族；Maynard 小间距与 Li 短区间素数不控制这种
同 atom、跨 witness、跨 step slot 的局部 splice。

状态边界：

```text
repeated_step_occurrence_splice_ledger_closed=true
occurrence_splice_uniform_family_bound_proved=false
single_occurrence_orbit_repair_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```

## 65AG. 2026-05-25 外部前沿可用性同步

新增证书：

```text
experiments/prime_matrix_external_live_frontier_applicability_sync_20260525.py
data/prime-matrix-external-live-frontier-applicability-sync-20260525-ledger.json
docs/monograph/prime-matrix-external-live-frontier-applicability-sync-20260525.json
docs/monograph/prime-matrix-external-live-frontier-applicability-sync-20260525.md
```

本层核对四类最新外部输入对当前 PM/Phi-LPF 门的可用性：

| 外部输入 | 主源 | 当前可用边界 |
| --- | --- | --- |
| Milićević--Qin--Wu arbitrary-modulus Kloosterman bilinear forms | https://arxiv.org/abs/2511.07550 | 需要 moving Beatty numerator 与 source-key 被完成成双变量 Kloosterman family；当前只是 finite pivot/right-tail/adjacent-run ledger |
| Wright trilinear Kloosterman fractions | https://arxiv.org/abs/2604.25177 | 需要三线性 convolution 与 equidistributed beta sequence；当前没有 source-key lift |
| Runbo Li large-modulus AP primes / Harman sieve refinements | https://arxiv.org/abs/2602.20917 | 属于大模数平均型/almost-all AP 输入；不能直接给逐行逐列 `x=P^2` 点态正性 |
| Becker--Breuillard uniform spectral gaps and anti-concentration | https://arxiv.org/abs/2512.15364 | 需要先构造 finite-group orbit 或 thin-group sieve family；当前 q-spine pivot 账本不是群轨道 |

审计读数：

```text
external_input_count=4
all_inputs_require_admissible_family_before_use=true
admissible_averaged_signed_trace_family_constructed=false
admissible_finite_group_orbit_family_constructed=false
pointwise_row_column_ap_positivity_imported=false
row_column_unconditional_closed=false
phi_lpf_parity_barrier_globally_broken=false
```

因此，本轮外部前沿没有改变闭合边界。非循环下一步仍是先构造
`SourceKeyLift/PrimitiveOrientationLocalFactorProduct`，或把失败回流为
PDEC/SAE/LocalSurvivor；然后才可调用 trace/Kloosterman/Type-II/expander 输入。

## 65AH. Phi-LPF right-tail overhang excess decomposition 证书

新增证书：

```text
experiments/prime_matrix_phi_lpf_right_tail_overhang_excess_decomposition_router.py
data/prime-matrix-phi-lpf-right-tail-overhang-excess-decomposition-ledger.json
docs/monograph/prime-matrix-phi-lpf-right-tail-overhang-excess-decomposition-router.json
docs/monograph/prime-matrix-phi-lpf-right-tail-overhang-excess-decomposition-router.md
```

本层不引入新外部定理，而是继续压缩外部定理的前置对象：唯一 right-tail
overhang 不是 completed Kloosterman/trace family，也不是群轨道；它被证明为
m773 final negative run 的剩余负变差。

审计读数：

```text
negative_excess_equals_internal_plus_tail=true
tail_overhang_equals_excess_after_internal_return=true
internal_survivor_old_return_paid=true
final_run_tail_matches=true
right_tail_overhang_excess_decomposition_closed=true
right_tail_final_negative_run_payment_law_proved=false
row_column_unconditional_closed=false
phi_lpf_parity_barrier_globally_broken=false
```

因此外部 theorem 边界进一步收窄但未闭合：FKMS/Milićević--Qin--Wu/Wright/Pascadi
仍需要 final negative-tail 对象被提升为可平均 signed family；Becker--Breuillard 型
谱隙仍需要有限群轨道。最新非循环口为：

```text
BridgeRootQSpinePivotEnclosureLawOrPDEC
AND RightSelectedTerminalFinalNegativeRunExcessPaymentOrPDEC
AND BoundaryAdjacentRunMassRatioLawOrPDEC
AND PrimitiveOrientationLocalFactorProductLawBeforePushforward
AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving
AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```
