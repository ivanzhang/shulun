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
