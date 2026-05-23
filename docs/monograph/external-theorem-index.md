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
