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

- **来源**：Bombieri, E.; Friedlander, J. B.; Iwaniec, H., *Primes in Arithmetic Progressions to Large Moduli. II*, Mathematische Annalen 277, 361--394, 1987.
- **状态**：`required` for external-theorem version.
- **用于**：把 DI Kloosterman 平均接入 well-factorable Rosser/Buchstab 权重和 Dirichlet 多项式卷积。
- **对应链条**：`BFI + DI => KLS-window => WBE2`.
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

## 9. 不能误用的输入

| 输入 | 不能替代什么 | 原因 |
| --- | --- | --- |
| RC-Prime | BMD/WBE2 | 只给非空性，不给有符号分布 |
| 普通大筛 | BE2-3K/KLS-window | 平衡块差一个 `P` 量级 |
| 点态 Weil | KLS-window | 只给单模抵消，不给总平均 `log^{-A}` |
| 实验扫描 | 证明 | 只能作为常数与结构证据；无限尾段必须接显式外部不等式 |
| 完整 CRT 周期均衡 | 短窗口真实分布 | 短窗口不等于完整周期 |

## 10. 下一步核查任务

1. `docs/monograph/kls-window-di-bfi-adaptation-template.md` 已把 DI/BFI 到 KLS-window 的相位、模数、频率、逆元变量、权重、gcd 层、端点平滑和 `B(A)` 损失账本写成独立适配模板。
2. 在主稿中把“引用版闭合”和“完全自足版未闭合”继续分开定理化。
3. 把 Rosser--Schoenfeld 显式 Mertens/prime-count 常数写入主稿参考文献和定理模板。
4. 若投稿要求外部文献原文定理号，逐页核对 DI/BFI 的对应定理编号；这属于书目精确化，不改变当前 H7 外部定理版逻辑链。

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
外部引用；外部索引只需继续核对 KZ-B、KZ-D、KZ-E。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kz-d-spectral-large-sieve-spine.md` 后，KZ-D 的
外部核验点改为 `PTK-D`。外部谱大筛若能给出 diagonal `T^2` 和 off-diagonal `N0` 的
Schur 行列和上界，即可由该文件推出 KZ-D；否则还需补 pre-trace kernel 证明。
