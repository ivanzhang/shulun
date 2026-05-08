# 合著论著命题状态总表

本文给出合著论著 `paper/contradiction-field-monograph/contradiction-field-monograph.tex` 的命题状态。状态必须诚实区分：已在文稿中证明、已归约、外部输入、计算证书、仍需独立审稿。

| 模块 | 命题/输入 | 当前状态 | 主要证据 | 是否可称无条件终稿 |
|---|---|---|---|---|
| Prime Matrix A/B | 行/列反例归约到 Structured-EHPD | 已归约/入口定理化完成 | `docs/row-column-reduction-formal-appendix.md`; `docs/monograph/prime-matrix-ab-entrance-theorem-list.md` | 否，仍依赖 D 组排斥 |
| Prime Matrix recursive lift | 相邻素数方阵递推升级路线 | 新增路线审查/粗合数投影已压缩到第一锚粗互补因子同权预算；恒等式审计差为 `0`；FAC 模型审计暴露逐窗口单一常数负余量；低模审计显示尖峰主要由 `D_T` 端点缺陷捕获；Annulus 已压缩为旧筛幸存者非空；正负异常统一为 signed endpoint sawtooth bridge；终端带最新压缩到 `RCI/PDEC`，分散分支进一步压缩到 `WSH-Hall/PDEC`：单尾因子完全抵消，只剩无尾储备与多尾碰撞超额，双粗半素数补洞受固定偏移轮筛容量约束 | `docs/monograph/prime-matrix-recursive-lift-audit.md`, `docs/monograph/prime-matrix-seam-endpoint-audit.md`, `docs/monograph/prime-matrix-seb-unconditionality-audit.md`, `docs/monograph/prime-matrix-asb-pressure-audit.md`, `docs/monograph/prime-matrix-asb-hard-attack.md`, `docs/monograph/prime-matrix-asb-rhc-alpha-sweep.md`, `docs/monograph/prime-matrix-rpd-failure-structure.md`, `docs/monograph/prime-matrix-semiprime-anchor-projection.md`, `docs/monograph/prime-matrix-anchor-cofactor-interval-audit.md`, `docs/monograph/prime-matrix-mge3-budget-audit.md`, `docs/monograph/prime-matrix-mge3-second-anchor-audit.md`, `docs/monograph/prime-matrix-mge3-tail-envelope-audit.md`, `docs/monograph/prime-matrix-tail-spike-localization-audit.md`, `docs/monograph/prime-matrix-singleton-corridor-bound-audit.md`, `docs/monograph/prime-matrix-singleton-corridor-overlap-audit.md`, `docs/monograph/prime-matrix-singleton-corridor-closure-lemma.md`, `docs/monograph/prime-matrix-disjoint-corridor-selberg-lemma.md`, `docs/monograph/prime-matrix-rpd-first-anchor-identity.md`, `docs/monograph/prime-matrix-rpd-first-anchor-identity-audit.md`, `docs/monograph/prime-matrix-rpd-fac-budget-audit.md`, `docs/monograph/prime-matrix-rpd-fac-lowmod-defect-audit.md`, `docs/monograph/prime-matrix-square-annulus-lift-lemma.md`, `docs/monograph/prime-matrix-square-annulus-sieve-lift-audit.md`, `docs/monograph/prime-matrix-annulus-rough-nonempty-hard-attack.md`, `docs/monograph/prime-matrix-signed-lowmod-bridge-hard-attack.md`, `docs/monograph/prime-matrix-directed-endpoint-crtdefect-bridge.md`, `docs/monograph/prime-matrix-dec-ospc-exclusion-hardpoint.md`, `docs/monograph/prime-matrix-terminal-sae-cancellation-identity.md`, `docs/monograph/prime-matrix-terminal-sae-cancellation-audit.md`, `docs/monograph/prime-matrix-asb-rpd-weighted-sieve-kernel.md`, `docs/monograph/prime-matrix-semiprime-wheel-shadow-rigidity.md`, `docs/monograph/prime-matrix-semiprime-wheel-near-offset-audit.md` | 否，最终剩余已精确为 `RCI/PDEC` 的分散出口 `WSH-Hall/PDEC`: 证明轮筛允许 Hall 匹配，或证明失败形成固定偏移 CRTDefect、Tail-anchor、Endpoint/PDEC；否则递推链仍为严格归约 |
| Prime Matrix EDA-Dual | 早期对角避让 `X0(p)>p` 的 Bonferroni/Selberg 对偶路线 | 新增低阶硬攻：`U_p(x)` 已写成小素因子覆盖余量，奇数阶 Bonferroni 下界 `S_K(p,x)` 已严格化为纯 CRT 整除计数；五阶恒等式 `S_5=U_p-\sum_{\omega_p(n)\ge6}{\omega_p(n)-1\choose5}` 精确暴露唯一尾项。实验样本显示 `S_5>0`，但固定阶存在渐近变号风险，不能作为全局证明 | `docs/monograph/prime-matrix-early-diagonal-avoidance-hardpoint.md`, `docs/monograph/prime-matrix-first-zero-equivalence-and-diagonal-barrier.md`, `docs/monograph/prime-matrix-eda-gap-barrier-and-dual-route.md`, `docs/monograph/prime-matrix-eda-dual-bonferroni-hard-attack.md`, `experiments/prime_matrix_eda_bonferroni_audit.py` | 否，剩余为 `EDA-BK/Selberg`：构造可变阶 Bonferroni/Brun/Selberg 正下界，或证明高重合尾项过大必触发 `PDEC/SAE` |
| Prime Matrix full CRT zero row | 首零行全量 CRT 方程组与对角最小代表屏障 | 已逐行证明零行集合等于完整覆盖 CRT 证书残基类并集，`X_0(p)=min_tau r_tau^+`；并证明 `X_0(p)>p` 等价于所有早期 `p` 对齐短区间 `(px,px+p)` 含素数 | `docs/monograph/prime-matrix-zero-row-full-crt-diagonal-minrep.md` | 否，等价式已证；仍需证明 MinRep 屏障、`EDA-Dual` 正余量或排斥 `LowMod/Tail` 出口 |
| Prime Matrix EDA-BK bridge | Bonferroni 下界失败到端点 CRT 缺陷 | 桥接定理已逐行证明：写 `S_K=H G_K+E_K`，其中 `G_K` 是截断 Euler 主项，`E_K` 是端点分数部分锯齿和；若奇数阶 `K` 满足 `G_K>0` 且 `S_K<=0`，则必有 `E_K<=-H G_K`。因此任何 EDA 反例都会产生显式负端点缺陷 | `docs/monograph/prime-matrix-eda-bk-endpoint-defect-bridge.md`, `experiments/prime_matrix_eda_endpoint_defect_audit.py` | 否，桥接已证；正主项阶数由下一行闭合，仍需排斥端点缺陷或将其并入 `PDEC/SAE` 证书 |
| Prime Matrix EDA-BK dichotomy | 正主项阶数与低模/尾项二分 | 已证明存在奇数阶 `K_*(p)` 使 `G_{K_*}(p)>0`；若 EDA 失败，则反例行给出 `E_{K_*}<=-(p-1)G_{K_*}`，并对任意 cutoff `D` 二分为 `LowMod endpoint CRTDefect` 或 `Tail/Core concentration` | `docs/monograph/prime-matrix-eda-bk-lowmod-tail-dichotomy.md` | 否，二分已证；剩余是排斥 LowMod 出口并吸收 Tail/Core 出口 |
| Prime Matrix EDA-LowMod | 低模端点 CRT 缺陷证书路线 | 已把 LowMod 出口写成有限低模端点函数 `F_{p,D}`、阈值坏集 `B_{p,D,T}` 与 Fourier/PDEC 证书条件；并证明固定 `D` 的量级排除 `|F_{p,D}|\le|\mathcal D_{p,D}|-1`。若坏集不命中早期对角段，则 LowMod 出口被排除，否则失败即显式低模相关异常 | `docs/monograph/prime-matrix-eda-lowmod-pdec-certificate-route.md`, `experiments/prime_matrix_eda_lowmod_pdec_audit.py` | 否，证书对象已形式化；仍需全局选择 `D,T` 并证明坏集排斥或接入 PDEC/SAE |
| Prime Matrix EDA-TailCore | 尾项核心桶吸收路线 | 已把 Tail/Core 出口写成尾关联集合 `Omega_{p,K,D}`、尾质量 `U_{p,K,D}`、TailCoreBucket 分桶，并证明尾项过大必进入尾锚集中或分布式走廊饱和；进一步证明危险负尾项等价于奇数阶核心桶相对偶数阶核心桶的 signed imbalance。样本中尾质量大但 signed tail 为正 | `docs/monograph/prime-matrix-eda-tailcore-absorption-route.md`, `experiments/prime_matrix_eda_tailcore_audit.py` | 否，归约已证；仍需证明 `SignedTail-Balance`、EDA 专用 Rankin 走廊账本、Tail-anchor 排斥和 Rankin 失败回流 PDEC/SAE |
| Prime Matrix EDA-SignedTail | 奇偶核心双向影子匹配路线 | 已证明危险 signed tail 若足够负，则必产生最大匹配缺口；缺口进一步二分为孤立奇核心压力或偶影子拥塞。脚本现用相差一个素因子的双向邻接匹配，允许大单素数核心向上配对到偶数二核心 | `docs/monograph/prime-matrix-eda-signedtail-shadow-matching.md`, `experiments/prime_matrix_eda_signedtail_matching_audit.py` | 否，匹配归约已证；仍需吸收孤立奇核心并排斥影子拥塞或接入 PDEC/SAE |
| Prime Matrix EDA variable order | 变量阶布尔消尾 | 已证明取奇数阶 `K_p>=floor(log2(p^2+p-1))` 时，早期区段每个点满足 Bonferroni 权等于精确幸存指示，因此 `S_{K_p}(p,x)=U_p(x)`。固定阶 Tail/Core 惩罚被证明是截断技术障碍，不是最终本质障碍 | `docs/monograph/prime-matrix-eda-variable-order-boolean-cancellation.md`, `experiments/prime_matrix_eda_variable_order_audit.py` | 否，消尾已证；仍需证明精确筛余 `U_p(x)>0`，即 ExactEndpoint-MinRep 缺陷排斥 |
| Prime Matrix EDA ExactEndpoint-MinRep synthesis | 精确端点与最小代表缺陷综合归约 | 已把当前最小硬点写成 `MinRepHit + ExactEndpoint + Low-or-High + FactorDefect + PinnedDivisor` 的同时发生；证明早期零行必给出完整 CRT 证书最小代表 `<=p`，并严格说明因子对偶降阶只有在无泄漏且代表不逃逸时才会递归矛盾。低骨架洞/高标签补洞容量接口已形式化 | `docs/monograph/prime-matrix-eda-exactendpoint-minrep-synthesis.md`, `experiments/prime_matrix_eda_exact_defect_audit.py` | 否，综合归约已证；剩余是排斥这些缺陷在同一早期行同时成立，尤其需给出新的 ExactEndpoint-MinRep 缺陷不等式 |
| Prime Matrix EDA PinnedDivisor Leakage | 钉扎因子与泄漏见证压力 | 已证明若 `pi|x`，则降阶泄漏列不能由任何 `x` 的素因子补洞，只能由 `[pi,p)` 中且不整除 `x` 的外部标签覆盖；同一高标签在 `pi` 前缀内不可复用。若降阶代表不逃逸，则泄漏列数至少为下层早期最小余量 `m(pi)>0` | `docs/monograph/prime-matrix-eda-pinned-divisor-leakage-pressure.md` | 否，压力不等式已证；剩余是证明多层 `RangeEscape` 或外部泄漏见证拥塞必触发 `LowMod/PDEC/HighLabel-MinRep` 矛盾 |
| Prime Matrix EDA PM1 slope descent | `p±1` 斜率递降 | 已证明 `pi|p-1` 或 `pi|p+1` 可把 `p` 零窗改写为 `pi`-网格长窗；若其中存在无 `<pi` 泄漏的对齐 `pi` 子行且代表不逃逸，则下降到 `EDA(pi)` 矛盾。小因子 `2,3` 不给自动下降，反而确定产生泄漏；样本首零行均无强下降子行 | `docs/monograph/prime-matrix-eda-pm1-slope-descent-obstruction.md`, `experiments/prime_matrix_pm1_slope_descent_audit.py` | 否，条件下降已证；剩余是证明 `p±1` 小斜率产生的泄漏不能全部由中高标签补洞而不触发 `PDEC/SAE` |
| Prime Matrix EDA diagonal branch | `x=p` 对角端点屏障 | 已证明 `U_p(p)>0` 当且仅当 `(p^2,p^2+p)` 中存在素数；并指出因子降阶/钉扎泄漏完全不能处理该端点，因为 `x=p` 没有 `<p` 内部素因子。对角零行等价于固定相位族 `k≡-p^2 mod q` 全覆盖 `[1,p-1]` | `docs/monograph/prime-matrix-eda-diagonal-branch-barrier.md` | 否，等价与边界已证；剩余是直接排斥固定相位族全覆盖，即对角 ExactEndpoint-MinRep 缺陷 |
| Prime Matrix EDA diagonal QPL | 对角二次相位锁 | 已证明若 `q|p^2+k`，则 `chi_q(k)=chi_q(-1)`；因此对角覆盖相位不是任意残基，而是被 `-p^2` 的二次字符锁定。并给出强充分条件：若存在偶数 `k<p` 对所有奇 `q<p` 满足反相 Legendre 条件，则 `p^2+k` 为素数 | `docs/monograph/prime-matrix-eda-diagonal-quadratic-phase-lock.md` | 否，二次相位锁已证；剩余是构造这样的短 `k`，或直接证明固定残基族 `k≡-p^2 mod q` 不能全覆盖 |
| Prime Matrix EDA diagonal final hardcore | 对角最终硬核边界 | 已审计并修正路线：Legendre 全反相只是过强充分条件，真实幸存列通常只满足约半数反相；必要充分条件仍是精确相位避让 `k\not\equiv -p^2 mod q`。该分支严格等价于 `pi(p^2+p-1)-pi(p^2)>0` | `docs/monograph/prime-matrix-eda-diagonal-final-hardcore-boundary.md`, `experiments/prime_matrix_diagonal_qpl_audit.py` | 否，边界已压实；剩余是对角精确相位 PDEC、特殊起点 Jacobsthal 边界，或明确外部平方根长度短区间素数输入 |
| Prime Matrix EDA diagonal split capacity | 对角低骨架/高标签精确容量路线 | 已证明判据：若低标签 `q<=alpha p` 留下的洞数大于高标签 `q>alpha p` 的固定相位实际容量，则对角行必有素数。对 `alpha>1/2` 给出高标签容量精确公式；样本在 `alpha≈0.66` 起有稳定正余量 | `docs/monograph/prime-matrix-eda-diagonal-split-capacity-route.md`, `experiments/prime_matrix_diagonal_split_capacity_audit.py` | 否，判据已证；剩余是全局证明 `DSC-LowHole(alpha=2/3)` 低骨架洞下界超过高标签精确容量 |
| Prime Matrix EDA diagonal lowhole shell | 对角低洞半素数壳层 | 已证明当 `y=floor(2p/3)` 时，低洞若不是素数，则必须为 `qr`，其中 `q in (2p/3,p)`、`r in (p,3p/2)` 且二者为素数；等价参数化为 `q=p-a,r=p+a+d` 且 `(d-1)p<a(a+d)<=dp-1` | `docs/monograph/prime-matrix-eda-diagonal-lowhole-semiprime-shell.md` | 否，壳层结构已证；剩余是证明低洞总数下界与近对称半素数壳层上界之间有正余量 |
| Prime Matrix EDA DLS-13 | 低洞下界 Buchstab 屏障 | 已证明 `|H_floor(2p/3)(p)| = pi(p^2+p-1)-pi(p^2)+B_y(p)`，其中 `B_y` 是近对称双素数壳层；并说明普通线性下界筛因可用 level `D≈p`、筛界 `z≈p` 导致 `s≈1<2`，不能给正下界 | `docs/monograph/prime-matrix-eda-dls13-buchstab-barrier.md`, `experiments/prime_matrix_dls13_shell_audit.py` | 否，DLS-13 未闭合；若不引用平方根长度短区间素数输入，剩余必须走特殊起点 `DLS13-PDEC` |
| Prime Matrix EDA DLS13-DEB | DLS13 端点缺陷桥 | 已证明精确恒等式 `H_y=(p-1)V_y+E_y`；若分割容量判据失败 `H_y<=C_y`，则必有 `E_y<=C_y-(p-1)V_y`。样本显示端点虽负但远未达到失败阈值；最小硬点压成 `DLS13-PDEC` | `docs/monograph/prime-matrix-eda-dls13-endpoint-defect-bridge.md`, `experiments/prime_matrix_dls13_endpoint_bridge_audit.py` | 否，桥接已证；剩余是证明固定相位端点缺陷 `E_y` 不能低于失败阈值，或将失败接入 PDEC/SAE |
| Prime Matrix EDA DLS13-DLT | DLS13 低模/尾项二分 | 已证明若分割容量失败，则对任意 `D,theta` 至少发生 `E_{<=D}<=theta T_y` 或 `E_{>D}<=(1-theta)T_y`。低模项是有限 CRT 相位函数，可进入 PDEC；尾项必须进入半素数壳层或高模 core/SAE | `docs/monograph/prime-matrix-eda-dls13-lowmod-tail-dichotomy.md`, `experiments/prime_matrix_dls13_lowmod_tail_audit.py` | 否，二分已证；剩余是排斥 `DLT-LowMod` 与 `DLT-Tail` 两个出口 |
| Prime Matrix EDA DLS13-LowMod exclusion | 固定低模自动排除 | 已证明固定 `D` 时 `|E_{<=D}|<=A(D)`；若主量间隙 `G_y=(p-1)V_y-C_y(p)>=c p/log p`，则 `LowMod-Bad(D,theta)` 对充分大 `p` 自动排除。低模分支由此转化为高标签第二命中容量上界 `HCap-2Hit` | `docs/monograph/prime-matrix-eda-dls13-lowmod-asymptotic-exclusion.md` | 否，条件机制已证；剩余是证明 `MainGap(2/3)` 或尖锐上界 `C_y< (1-eta)(p-1)V_y` |
| Prime Matrix EDA diagonal Alpha-Lift | 对角分割参数优化 | 已证明一般 `alpha>1/2` 分割判据，并指出 `alpha=3/4` 比 `2/3` 给出更大样本余量：低洞只小幅减少，高标签容量显著减少，复合低洞壳层从 `(2p/3,p)x(p,3p/2)` 收窄到 `(3p/4,p)x(p,4p/3)` | `docs/monograph/prime-matrix-eda-diagonal-alpha-lift-route.md`, `experiments/prime_matrix_diagonal_split_capacity_audit.py` | 否，路线优化已证；剩余是证明 `ALP-3/4: |H_floor(3p/4)(p)|>C_floor(3p/4)(p)` |
| Prime Matrix EDA HCap second hit | 高标签第二命中结构 | 已证明对 `q=p-r`，第二命中当且仅当 `r^2 mod (p-r)>=p-2r+1`，等价于层参数 `m=floor(r^2/(p-r))` 下的二次不等式 `r^2+(m+2)r-(m+1)p>=1`。容量公式化为 `C_alpha=pi(p)-pi(alpha p)+S_alpha` | `docs/monograph/prime-matrix-eda-highcap-second-hit-structure.md` | 否，结构已证；剩余是证明 `S_alpha(p)` 的尖锐上界，使 `C_alpha` 与主量之间保留固定正间隙 |
| Prime Matrix EDA Alpha-MainGap | Alpha 主量间隙常数包 | 已证明若显式常数满足 `V_alpha>=c_M/log p` 与 `pi(p)-pi(alpha p)<=C_pi(1-alpha)p/log p`，且 `alpha>1-c_M/(2C_pi)`，则粗容量 `C_alpha<=2(pi(p)-pi(alpha p))` 已给固定正主量间隙。保守常数 `c_M=0.45,Cpi=1.30` 时 `alpha=0.9` 通过 | `docs/monograph/prime-matrix-eda-alpha-main-gap-constant-package.md`, `experiments/prime_matrix_alpha_main_gap_constant_scan.py` | 否，主量间隙条件化闭合；剩余是显式常数逐项核验、有限段验证，以及排斥 `AlphaTail(alpha=0.9)` |
| Prime Matrix EDA AlphaTail exact | AlphaTail 素数-坏命中精确分解 | 已证明 `alpha=0.9` 下高标签唯一，且 `H_alpha-C_alpha=P_alpha-BadHigh_alpha`；好半素数壳层在低洞数和高标签容量中完全抵消。坏命中来自 `q prime in (0.9p,p)` 与复合 `m in (p,1.112p)` 且 `qm in (p^2,p^2+p)` | `docs/monograph/prime-matrix-eda-alpha-tail-prime-vs-bad-hit.md`, `experiments/prime_matrix_alpha_tail_bad_audit.py` | 否，等价分解已证；剩余是证明对角素数数 `P_alpha` 大于坏高标签命中数，或由 PDEC/SAE 替代该短区间素数下界 |
| Prime Matrix EDA AlphaTail bad upper | 坏高标签上界与素数下界边界 | 已证明 `BadHigh_alpha<=2(pi(p)-pi(alpha p))`，若对角短区间素数下界 `P_alpha>=c_P p/log p` 且 `c_P>2Cpi(1-alpha)`，则 AlphaTail 闭合。`alpha` 可把坏命中常数任意压小，但极限会退回“至少一个对角素数”原硬点 | `docs/monograph/prime-matrix-eda-alpha-tail-bad-upper-prime-lower.md` | 否，条件闭合已证；无外部短区间素数输入时，剩余必须证明 `PrimeVoid=>PDEC` |
| Prime Matrix EDA PrimeVoid=>AlphaPDEC | 对角无素数到强端点缺陷 | 已证明若 `(p^2,p^2+p)` 无素数，则对任意 `alpha>1/sqrt2` 有 `H_alpha<=C_alpha`，结合 Alpha-MainGap 得 `E_alpha<=-c_alpha p/log p`。固定低模项为 `O_D(1)`，所以大尺度反例必须进入强负尾项 `AlphaTailStrong` | `docs/monograph/prime-matrix-eda-primevoid-to-alpha-pdec-bridge.md` | 否，桥接已证；剩余是排斥 `AlphaTailStrong` 或证明其必产生 SAE/PDEC 证书矛盾 |
| Prime Matrix EDA AlphaTail dyadic PDEC | 强负尾项显化为 dyadic 端点证书 | 已证明若 `AlphaTailStrong` 成立且远尾 `E_{>D1}` 没有承担固定比例负缺陷，则某个截断 dyadic 块 `I_j` 必有 `E_{I_j}<=-c p/(log p L)` 级有向端点 CRT 偏斜；否则反例进入 `FarTail-Core` 出口。审计脚本已支持表格/JSON 输出并给出样本块集中现象 | `docs/monograph/prime-matrix-eda-alpha-tail-dyadic-pdec-certificate.md`, `experiments/prime_matrix_alpha_tail_dyadic_audit.py` | 否，归约/证书出口已证；仍需排斥 dyadic PDEC 或证明 FarTail-Core 必回流 `SAE/PDEC/ColumnCRT` |
| Prime Matrix EDA AlphaTail high dyadic lock | 高模数块单命中端点锁 | 已证明若 dyadic 缺陷块落在 `d>p-1`，则 `N_d=1_{rho_d(p)<=p-1}`，强负缺陷等价为 Möbius 符号端点命中异常；进一步二分为偶 Möbius 模数命中亏损或奇 Möbius 模数命中过剩 | `docs/monograph/prime-matrix-eda-alpha-tail-highdyadic-endpoint-lock.md` | 否，结构压缩已证；仍需将 `HDL-9/HDL-10` 能量化并排斥，或送入 `ColumnCRT/PDEC/SAE` |
| Prime Matrix EDA AlphaTail HDL-CoreLoad | 高块端点锁到逐列核心负载 | 已证明高块端点命中计数 `A_I^\pm` 精确等于逐列低素核心子集乘积负载和 `sum_k C_I^\pm(k)`；因此 `HDL-9/HDL-10` 被改写为偶核心负载亏损或奇核心负载过剩，可路由到 Tail-anchor、Distributed-CoreLoad、ColumnCRT 或 PDEC | `docs/monograph/prime-matrix-eda-alpha-tail-hdl-coreload-identity.md` | 否，恒等式/路由已证；仍需排斥 CoreLoad 异常出口 |
| Prime Matrix EDA AlphaTail HCL cofactor inversion | 高核心负载到低互补因子带 | 已证明当高块 `B>p-1` 时，每个 `d|p^2+k` 的高低素核心命中等价于小互补因子 `m=(p^2+k)/d<p+2`；`HCL-8` 等价为低互补因子带上的奇符号负载过剩。单个 `m` 满足容量 `L_I^\pm(m)<=1+floor((p-1)/m)`，因此异常二分为 cofactor-anchor 或 distributed-cofactor load。审计样本显示过剩主要分散在大量 `m` 上 | `docs/monograph/prime-matrix-eda-alpha-tail-hcl-cofactor-inversion.md`, `experiments/prime_matrix_alpha_tail_cofactor_audit.py` | 否，反演/容量二分已证；仍需证明 cofactor-anchor 与 distributed-cofactor load 必触发并可排斥 `ColumnCRT/PDEC/SAE` |
| Prime Matrix EDA AlphaTail cofactor intervalization | 互补因子负载短区间化 | 已证明固定互补因子 `m` 后，`L_I^\pm(m)` 精确等于 `D_y^\pm` 中的低素平方自由数落入短区间 `(p^2/m,(p^2+p-1)/m]∩I` 的个数；区间长度为 `(p-1)/m`，在高块 `B=lambda p` 时锁定为常数级。Distributed-cofactor load 被压成 `WSS` 短区间符号过剩或 local/global model mismatch | `docs/monograph/prime-matrix-eda-alpha-tail-cofactor-intervalization.md` | 否，短区间化归约已证；仍需排斥 `WSS` 过剩与模型错配，或送入 `PDEC/ColumnCRT/SAE` |
| Prime Matrix EDA AlphaTail WSS Fourier certificate | WSS短区间过剩到双线性相位证书 | 已证明短区间条件 `p^2<md<=p^2+p-1` 可在大模 `Q>4p^2` 上 Fourier 展开；若 WSS 分散过剩不能由模型错配吸收，则存在非零频率 `h` 使双线性和 `sum_m sum_d exp(2pi i hmd/Q)` 达到异常尺度，从而形成明确 `PDEC/ColumnCRT` 证书 | `docs/monograph/prime-matrix-eda-alpha-tail-wss-bilinear-fourier-certificate.md` | 否，Fourier证书出口已证；仍需证明该双线性和在结构化 `M,D_y^-` 上抵消，或失败进入 `SAE/ColumnCRT` 并排斥 |
| Prime Matrix EDA AlphaTail frequency split | 双线性证书低频/高频分割 | 已证明 WSS 偏差的非零 Fourier 部分必须二分为 `LowFreq-ModelMismatch` 或 `HighFreq-BohrCap`；低频大值是平滑短区间核，不能误标为 PDEC。全矩形审计显示最佳未中心化频率通常为 `h=1`，因此正式链条必须先扣除低频模型后再进入 Bohr-cap | `docs/monograph/prime-matrix-eda-alpha-tail-frequency-split-contract.md`, `experiments/prime_matrix_alpha_tail_bilinear_bohr_audit.py` | 否，分割合同已证；剩余是分别排斥低频模型错配与高频 Bohr-cap |
| Prime Matrix EDA AlphaTail lowfreq return | 低频模型错配返回端点PDEC | 已证明互补因子双曲线带计数满足 `S(D)-H sum_{d in D}1/d=sum_d({p^2/d}-{(p^2+H)/d})`，在高块 `d>H` 下等同于 `sum_d(1_{rho_d<=H}-H/d)`；因此 `LowFreq-ModelMismatch` 不是新黑箱，而是原始 dyadic endpoint PDEC/SAE 返回口 | `docs/monograph/prime-matrix-eda-alpha-tail-lowfreq-endpoint-return.md` | 否，低频分支已回流；仍需排斥 endpoint PDEC/SAE 本身 |
| Prime Matrix EDA AlphaTail bilinear BohrCap | 高频双线性大值到Bohr差集聚集 | 已证明对高频双线性和 `B_h(M,D)`，平方展开给出区间核 `K_M(d-d')`；若普通矩形预算不足以吸收，则 `D` 的差集在频率 `h/Q` 的短 Bohr 弧上大量聚集，形成 `Bohr-cap/PDEC/ColumnCRT/SAE` 证书 | `docs/monograph/prime-matrix-eda-alpha-tail-bilinear-bohrcap-reduction.md` | 否，高频归约已证；仍需 Bohr-cap 差集计数上界或出口排斥 |
| Prime Matrix EDA AlphaTail Bohr additive energy | Bohr差集聚集到加法能量异常 | 已证明 Bohr-cap 对数 `P_T` 满足 `P_T^2<=|R_T|E_+(D)`；因此若有效模数低则进入 `PDEC/ColumnCRT`，若有效模数高且 Bohr 聚集大，则低素 squarefree 高块集合 `D` 必有异常大加法能量 `E_+(D)` | `docs/monograph/prime-matrix-eda-alpha-tail-bohrcap-additive-energy.md` | 否，能量归约已证；仍需 squarefree-smooth 加法能量上界，或失败路由到 `ColumnCRT/PDEC/SAE` |
| Prime Matrix EDA AlphaTail additive-energy shift correlation | 加法能量到位移双光滑相关 | 已证明 `E_+(D)=sum_r C_D(r)^2`，因此能量异常必二分为单热门位移 `ShiftSmooth(r)` 或分散位移能量异常；并明确 `ell|r` 时二禁降一禁降低筛重度，`ell∤r` 时为两禁约束。新增脚本审计能量、差值支撑和最热门位移 | `docs/monograph/prime-matrix-eda-alpha-tail-additive-energy-shift-correlation.md`, `experiments/prime_matrix_alpha_tail_additive_energy_audit.py` | 否，相关归约已证；仍需证明 ShiftSmooth 上界，或失败进入 `PDEC/ColumnCRT/SAE` |
| Prime Matrix EDA AlphaTail ShiftSmooth local ledger | 位移双光滑局部状态账本 | 已证明 `q∤r` 时 `d` 与 `d+r` 的零类分裂为 left-only/right-only 两个剩余类，而 `q|r` 时塌缩为 both 一个剩余类；平方自由局部因子为 `1-a_q(r)/q^2`，其中 `a_q=1` 当 `q^2|r` 否则 `2`。同符号条件用 `1/4(1+sigma mu(d)+sigma mu(d+r)+mu(d)mu(d+r))` 精确分解 | `docs/monograph/prime-matrix-eda-alpha-tail-shiftsmooth-local-ledger.md` | 否，局部账本已证；仍需 Selberg/Rankin 上界包络或失败路由 |
| Prime Matrix EDA AlphaTail ShiftSmooth large-prime sieve | 位移双光滑大素数排除筛包络 | 已证明若 `d,d+r` 都为 `y`-smooth，则对所有 `y<ell<=3B` 必避开 `d≡0,-r mod ell`；若 `ell|r` 两个禁零类合并为一个，形成显式奇异因子增益。由 Selberg 上筛得到 `ShiftSmooth(r)` 的二禁/一禁包络，失败进入端点 `PDEC/SAE`、位移因子 `ColumnCRT` 或 Selberg 常数账本 | `docs/monograph/prime-matrix-eda-alpha-tail-shiftsmooth-largeprime-sieve-envelope.md` | 否，上筛接口已证；仍需选择权重并核验常数足以压住热门位移 |
| Prime Matrix EDA AlphaTail ShiftSmooth near-linear deletion | 近线性块大素数删除恒等式 | 已证明当 `max(d,d+r)<y^2` 时，非 `y`-smooth 数唯一写成小互补因子 `a<y` 乘大素数 `ell>y`；无符号双光滑对数精确等于区间长度减两侧大素数删除集并集。热门位移因此二分为删除亏损或删除重叠异常 | `docs/monograph/prime-matrix-eda-alpha-tail-shiftsmooth-nearlinear-deletion.md`, `experiments/prime_matrix_alpha_tail_nearlinear_deletion_audit.py` | 否，近线性归约已证；仍需排斥删除亏损与删除重叠，或接入 `PDEC/ColumnCRT/SAE` |
| Prime Matrix EDA AlphaTail ShiftSmooth Möbius gate | 删除后同符号过滤闸门 | 已证明在删除后平方自由支撑 `A_r` 上，`C_sigma(r)=1/4(|A_r|+sigma M1+sigma M2+K)`；因此同符号过多必触发一阶 Möbius 偏置 `M1/M2` 或二点 Möbius 相关 `K` 异常 | `docs/monograph/prime-matrix-eda-alpha-tail-shiftsmooth-mobius-gate.md`, `experiments/prime_matrix_alpha_tail_nearlinear_deletion_audit.py` | 否，闸门恒等式已证；仍需排斥 Möbius 偏置/相关异常 |
| Prime Matrix EDA AlphaTail Möbius parity lock | 二点Möbius相关到对称差奇偶锁 | 已证明 `mu(d)mu(d+r)=(-1)^{|Supp(d) triangle Supp(d+r)|}`；`q|r` 的素因子只进入公共部分并提高同符号倾向，`q∤r` 的单边出现会翻转奇偶。因此正相关 `K(r)>0` 二分为共同素因子锁强或对称差奇偶偏置 | `docs/monograph/prime-matrix-eda-alpha-tail-mobius-correlation-parity-lock.md`, `experiments/prime_matrix_alpha_tail_mobius_corr_audit.py` | 否，结构二分已证；仍需共同锁奇异因子上界和 Parity-PDEC 排斥 |
| Prime Matrix EDA AlphaTail Parity-PDEC bridge | 对称差奇偶偏置证书化 | 已证明在 squarefree 支撑上 `mu(d)mu(d+r)=prod_{q<=y} psi_{q,r}(d)`，其中 `psi` 是显式两零类符号函数；任意 cutoff `R` 下，正相关二分为有限低模 `Parity-PDEC` 偏置或高素尾 `TailParity` 偏置 | `docs/monograph/prime-matrix-eda-alpha-tail-parity-pdec-bridge.md` | 否，证书化已证；仍需排斥低模奇偶偏置或证明高尾奇偶平均 |
| Prime Matrix EDA AlphaTail Parity-PDEC Fourier | 中心化低模奇偶偏置到Fourier证书 | 已证明低模符号函数均值为 `m_R=prod_{q<=R,q∤r}(q-4)/q`；扣除均值后，若 `sum_{A_r}(Psi_R-m_R)` 仍大，则有限模 `Q_R` 上存在非零 Fourier/CRT 系数，形成正式 `Parity-PDEC` 证书。新增审计脚本比较低模和高尾承担比例 | `docs/monograph/prime-matrix-eda-alpha-tail-parity-pdec-fourier-certificate.md`, `experiments/prime_matrix_alpha_tail_parity_pdec_audit.py` | 否，Fourier证书已证；仍需 PDEC 上界证书或 SAE 孤窗排斥 |
| Prime Matrix EDA AlphaTail TailParity first anchor | 高尾奇偶到首个高素因子锚点 | 已证明 `Theta-1=sum_j(theta_j-1)prod_{i<j}theta_i`；因 `theta_j-1` 只在 `q_j∤r` 且 `d≡0,-r mod q_j` 时为 `-2`，高尾奇偶偏置精确展开为未锁高素数的单边零类锚点贡献。新增脚本逐项核验 telescoping 并定位最大高素锚点 | `docs/monograph/prime-matrix-eda-alpha-tail-tailparity-first-anchor.md`, `experiments/prime_matrix_alpha_tail_tailparity_anchor_audit.py` | 否，锚点展开已证；仍需排斥高素锚点同号累积，或路由到 `ColumnCRT/PDEC/SAE` |
| Prime Matrix EDA AlphaTail tail-anchor energy | 高尾锚点同号累积到能量异常 | 已证明若高尾总贡献 `T_R` 大，则二分为单个高素锚点 `A_q` 集中，或分散锚点二次能量 `sum_q |A_q|^2 >= T_R^2/N_R`；单锚进入 `ColumnCRT/SAE`，分散能量进入 Rankin/large-sieve/PDEC 出口 | `docs/monograph/prime-matrix-eda-alpha-tail-tailanchor-energy-route.md` | 否，能量路线已证；仍需排斥单锚集中与分散锚点能量 |
| Prime Matrix EDA AlphaTail single anchor certificate | 单高素锚点集中证书 | 已证明若某个高素锚点 `|A_q|>=Lambda`，则 `0` 或 `-r mod q` 中至少一个剩余类承载 `>=Lambda/4` 的低模符号质量；中心化后与 H4 `PDEC-Cert` 字段兼容，孤立时进入 `SAE`。新增脚本输出左右类贡献 | `docs/monograph/prime-matrix-eda-alpha-tail-single-anchor-certificate.md`, `experiments/prime_matrix_alpha_tail_single_anchor_audit.py` | 否，证书对象已物化；仍需 PDEC 上界或 SAE 排斥 |
| Prime Matrix EDA AlphaTail distributed anchor energy | 分散高尾锚点能量拆分 | 已证明 `sum_q |A_q|^2` 可拆成点负载平方和与跨点锚点相关；点负载异常由 `Omega_{>R}(d(d+r))` 控制并进入 Rankin/Tail，跨点相关进入 `PDEC/ColumnCRT`。新增脚本审计 active anchors、总尾贡献、锚点能量和点负载界 | `docs/monograph/prime-matrix-eda-alpha-tail-distributed-anchor-energy-split.md`, `experiments/prime_matrix_alpha_tail_anchor_energy_audit.py` | 否，能量拆分已证；仍需 Rankin 点负载预算和跨点相关排斥 |
| Prime Matrix EDA AlphaTail crosspoint anchor graph | 跨点锚点相关图化 | 已证明固定高素锚点 `q` 时，跨点边只可能满足 `d1-d2≡0,±r mod q`；固定差值 `s` 可复用的高素锚点数由 `omega_{>R}(s(s-r)(s+r))` 控制。跨点相关二分为热门差值、低模符号边相关或 SAE | `docs/monograph/prime-matrix-eda-alpha-tail-crosspoint-anchor-graph.md` | 否，图化归约已证；仍需 Rankin 热门差值上界与符号边 PDEC 排斥 |
| Prime Matrix EDA AlphaTail hot-difference Rankin | 热门差值高素复用账本 | 已证明固定差值 `s` 的高素锚点复用数由 `nu_R(s;r)<=omega_{>R}(s(s-r)(s+r))` 控制；若复用数 `>=L`，则大于 `R` 的前 `L` 个素数乘积必须不超过 `|s(s-r)(s+r)|`。Rankin 矩界给出高复用差值数量上界；新增脚本审计最大复用和最高压力差值 | `docs/monograph/prime-matrix-eda-alpha-tail-hot-difference-rankin-ledger.md`, `experiments/prime_matrix_alpha_tail_hot_difference_audit.py` | 否，账本已证；仍需把复用上界与跨点边数结合成闭合不等式，或输出具体 ColumnCRT 证书 |
| Prime Matrix EDA AlphaTail resonant difference chain | 共振差值三点光滑链 | 已修正热门差值账本：`s=±r` 使 `s∓r=0`，不能用 Rankin 乘积界；它等价于 `d,d+r,d+2r` 三点同时通过的光滑/平方自由链。非共振样本最大复用仅 `3--5`，主要压力来自共振链 | `docs/monograph/prime-matrix-eda-alpha-tail-resonant-difference-chain.md`, `experiments/prime_matrix_alpha_tail_hot_difference_audit.py` | 否，共振识别已证；仍需三点链 Selberg 包络或 PDEC/SAE 排斥 |
| Prime Matrix EDA AlphaTail resonant chain sieve | 共振三点链三禁/一禁包络 | 已证明三点链局部禁零类数为 `b_q(r)=#{0,-r,-2r mod q}`：`q|r` 时一禁，`q∤r,q>2` 时三禁；由 Selberg 上筛得到三点链包络。新增脚本审计三点链数量和三组 Möbius 相关 | `docs/monograph/prime-matrix-eda-alpha-tail-resonant-chain-sieve-envelope.md`, `experiments/prime_matrix_alpha_tail_resonant_chain_audit.py` | 否，三点包络已证；仍需常数核验或 PDEC/SAE 排斥 |
| Prime Matrix EDA AlphaTail resonant chain parity gate | 共振三点链奇偶闸门 | 已证明三点链有符号压力必须进入三组二点 Möbius 相关 `K01,K12,K02` 之一，或无符号三点链包络失败；每个 `Kij` 都可按 Parity-PDEC/TailParity/SAE 路线处理，且同一个未锁素数同时影响两条边提供额外一致性约束 | `docs/monograph/prime-matrix-eda-alpha-tail-resonant-chain-parity-gate.md` | 否，奇偶闸门已证；仍需 ThreeEdge-Parity-PDEC 合并排斥 |
| Prime Matrix EDA AlphaTail ThreeEdge-Parity-PDEC | 三边合并奇偶证书 | 已证明三点链三边符号逐点满足 `epsilon01 epsilon12 epsilon02=1`，只能落在四状态 `A,B,C,D`；未锁素数命中一个点必同时翻转两条边。共振有符号压力因此进入四状态低模 `ThreeEdge-Parity-PDEC`、二边同源高尾锚点或无符号三点链包络失败。新增脚本审计四状态计数和低模中心化偏置 | `docs/monograph/prime-matrix-eda-alpha-tail-threeedge-parity-pdec.md`, `experiments/prime_matrix_alpha_tail_threeedge_parity_audit.py` | 否，合并证书归约已证；仍需提交四状态 PDEC 上界或二边高尾锚点 `ColumnCRT/SAE` 排斥 |
| Prime Matrix EDA AlphaTail ThreeEdge tail-anchor energy | 三边高尾二边同源锚点 | 已证明三边高尾压力可 telescoping 展开为三类锚点 `0,-r,-2r`；单个高素锚点必须同时翻转两条边。分散能量拆成点负载 `Omega_{>R}(d(d+r)(d+2r))` 与跨点五射线相关；固定差值可复用高素数整除 `s(s-r)(s+r)(s-2r)(s+2r)`，共振为 `s=0,±r,±2r`。新增脚本审计三边尾向量、锚点能量和最大点负载 | `docs/monograph/prime-matrix-eda-alpha-tail-threeedge-tailanchor-energy.md`, `experiments/prime_matrix_alpha_tail_threeedge_tailanchor_audit.py` | 否，三边尾锚归约已证；仍需五因子热门差值 Rankin 账本与 `s=±2r` 共振链排斥 |
| Prime Matrix EDA AlphaTail ThreeEdge five-ray Rankin | 五射线热门差值账本 | 已证明三边跨点非共振差值的高素复用数由五因子 `s(s-r)(s+r)(s-2r)(s+2r)` 控制；若复用数 `>=L`，大于 `R` 的前 `L` 个素数乘积不超过该五因子。共振几何已校正：在三点链基集合上 `s=±r` 强制四点链，`s=±2r` 强制五点链。新增脚本审计非共振最大复用与四/五点共振计数 | `docs/monograph/prime-matrix-eda-alpha-tail-threeedge-five-ray-rankin-ledger.md`, `experiments/prime_matrix_alpha_tail_threeedge_five_ray_audit.py` | 否，五因子账本已证；仍需常数并入正式跨点预算，并排斥四点/五点共振链 |
| Prime Matrix EDA AlphaTail ThreeEdge multipoint sieve | 四点/五点共振链包络 | 已证明五射线共振 `s=±r`、`s=±2r` 分别强制四点链 `T_{4,r}` 与五点链 `T_{5,r}`；局部禁零类数精确为 `b_{m,q}(r)=#{-jr mod q:0<=j<m}`，即 `q|r` 时一禁、`q∤r` 时 `min(m,q)` 禁。由 Selberg 上筛得到多点链包络。新增脚本审计 `T3/T4/T5` 和局部禁零类均值 | `docs/monograph/prime-matrix-eda-alpha-tail-threeedge-resonant-multipoint-sieve.md`, `experiments/prime_matrix_alpha_tail_multipoint_chain_audit.py` | 否，多点链包络已证；仍需核验 Selberg 常数足以压住正式共振压力，或把失败路由到 `PDEC/SAE/ColumnCRT` |
| Prime Matrix EDA AlphaTail multipoint resonance budget | 多点共振压力预算接口 | 已证明五射线共振容量精确恒等式：`s=±r` 的有序对数为 `2T4`，`s=±2r` 的有序对数为 `2T5`，故无符号共振容量为 `2T4+2T5`。有符号压力由该容量乘显式投影常数控制；代入四/五点 Selberg 预算后，失败必进入多点包络失败、端点 `PDEC`、奇异因子 `ColumnCRT/Rankin` 或 `SAE`。新增脚本核验恒等式和容量比例 | `docs/monograph/prime-matrix-eda-alpha-tail-multipoint-resonance-budget.md`, `experiments/prime_matrix_alpha_tail_resonance_budget_audit.py` | 否，预算接口已证；仍需选择正式 `z,lambda,C_u` 并核验主预算常数余量，或逐项排斥失败出口 |
| Prime Matrix EDA AlphaTail multipoint mainfactor ledger | 多点主筛因子常数账本 | 已把四点/五点 Selberg 主预算压成显式常数需求 `C_m^{req}=|T_m|/(|I_m|V_m)`，其中 `V_m=prod_{y<q<=z}(1-b_{m,q}/q)`。若正式 Selberg 常数不能覆盖该需求，失败必须输出 `m,r,I_m,V_m,C_req` 并进入权重优化、端点 `PDEC`、奇异因子 `ColumnCRT/Rankin` 或 `SAE` | `docs/monograph/prime-matrix-eda-alpha-tail-multipoint-mainfactor-ledger.md`, `experiments/prime_matrix_alpha_tail_multipoint_mainfactor_audit.py` | 否，常数需求已物化；仍需逐行证明一个足够小的正式 Selberg/Brun 常数 `C_m^{Sel}` 并接入最终压力阈值 |
| Prime Matrix EDA AlphaTail multipoint C1 bridge | 多点主筛 `C=1` 候选桥 | 已把候选 `|T_m|<=|I_m|V_m` 写成端点缺陷命题 `E_m=|T_m|-|I_m|V_m<=0`。若 `C=1` 失败，则正缺陷必经低模/尾项二分进入多点 `PDEC`、高尾 `ColumnCRT/Rankin` 或 `SAE`。新增脚本审计 `C=1` 余量，样本均为负缺陷 | `docs/monograph/prime-matrix-eda-alpha-tail-multipoint-c1-endpoint-bridge.md`, `experiments/prime_matrix_alpha_tail_multipoint_c1_bridge_audit.py` | 否，候选桥已证；仍需无条件证明 `E_m<=0` 或排斥正缺陷的两个出口 |
| Prime Matrix EDA AlphaTail rough/smooth decomposition | 多点 `C=1` 缺陷分解 | 已证明精确恒等式 `E_m=|T_m|-HV=(|R_m|-HV)-(|R_m|-|T_m|)`，即实际缺陷等于大素粗筛端点盈余减去小素平方自由删除量。若 `C=1` 失败，则粗筛端点盈余必须大于全部平方自由删除量；失败因此进入粗筛 `PDEC/SAE` 或小素平方类容量异常。新增脚本核验该恒等式 | `docs/monograph/prime-matrix-eda-alpha-tail-multipoint-rough-smooth-decomposition.md`, `experiments/prime_matrix_alpha_tail_rough_smooth_decomp_audit.py` | 否，分解已证；仍需证明粗筛端点盈余不超过平方自由删除，或排斥失衡证书 |
| Prime Matrix EDA AlphaTail square deletion ledger | 小素平方自由删除账本 | 已把平方自由删除量写成粗筛幸存集上的有限平方剩余类并集 `D_sq=|union E_{a,j}|`，并给出两个下界：Bonferroni `D_sq>=S1-S2` 与命中重数 `D_sq>=S1/Hmax`。样本中二阶 Bonferroni 为负，但 `S1/Hmax` 足以覆盖正粗筛盈余。若平方删除不足，则必须发生平方类总质量不足 `PDEC`、平方类重叠/高重数拥塞 `ColumnCRT/Rankin` 或粗筛盈余过强 `PDEC/SAE` | `docs/monograph/prime-matrix-eda-alpha-tail-square-deletion-ledger.md`, `experiments/prime_matrix_alpha_tail_square_deletion_audit.py` | 否，平方删除证书化已证；仍需证明 `S1/Hmax` 足以覆盖粗筛盈余，或排斥三个失败出口 |
| Prime Matrix EDA AlphaTail square hit product bound | 小素平方命中重数乘积上界 | 已证明若 `n<=z`，其不同素数平方因子数至多 `L2(z)`，其中 `prod_{i<=L2}p_i^2<=z`；因此多点链 `Hmax<=mL2(z)`，给出无条件删除下界 `D_sq>=S1/(mL2(z))`。新增脚本审计该下界，样本均覆盖正粗筛盈余 | `docs/monograph/prime-matrix-eda-alpha-tail-square-hit-product-bound.md`, `experiments/prime_matrix_alpha_tail_square_hit_bound_audit.py` | 否，`Hmax` 上界已证；仍需证明 `S1/(mL2(z))>=rough_surplus` 全局成立，或排斥 `S1` 低质量/粗筛盈余异常出口 |
| Prime Matrix EDA AlphaTail square mass bridge | 平方一阶质量与粗筛盈余桥 | 已把闭合判据 `S1/(mL2)>=rough_surplus` 拆成平方一阶质量下界 `S1>=|R|W_m(y)` 与粗筛端点盈余上界 `|R|W_m/(mL2)>=rough_surplus`。若失败，必进入 `SquareMass-PDEC` 或 `RoughSurplus-PDEC/SAE`。新增脚本审计平方质量模型、缺陷和余量 | `docs/monograph/prime-matrix-eda-alpha-tail-square-mass-rough-surplus-bridge.md`, `experiments/prime_matrix_alpha_tail_square_mass_bridge_audit.py` | 否，桥接已证；仍需排斥平方质量亏损与粗筛盈余异常两个出口，或证明模型余量全局非负 |
| Prime Matrix EDA AlphaTail SquareMass-PDEC | 平方质量亏损证书 | 已证明平方质量亏损可按平方 cutoff `A` 拆成低平方有限模 `Q_A=prod_{a<=A}a^2` 的零均值测试函数 `F_A=H_A-W_A` 与高平方尾质量亏损。若低平方承担亏损，则由 H4-PDEC 模板给出非零 Fourier/CRT 系数；若高平方承担，进入 `SquareTail/Rankin/SAE`。新增脚本审计低平方中心化质量 | `docs/monograph/prime-matrix-eda-alpha-tail-squaremass-pdec-certificate.md`, `experiments/prime_matrix_alpha_tail_squaremass_pdec_audit.py` | 否，证书化已证；仍需排斥低平方 PDEC 与高平方尾亏损 |
| Prime Matrix EDA AlphaTail RoughSurplus-PDEC | 粗筛端点盈余证书 | 已证明大素粗筛盈余可按大素 cutoff `D` 拆成低大素有限模粗筛偏置与高大素尾盈余。低分支是零均值函数 `Phi_{<=D}-V_{<=D}` 的 Fourier/PDEC 证书；高分支进入 `Rankin/SAE/ColumnCRT`。新增脚本审计低大素盈余和尾差 | `docs/monograph/prime-matrix-eda-alpha-tail-roughsurplus-pdec-certificate.md`, `experiments/prime_matrix_alpha_tail_roughsurplus_pdec_audit.py` | 否，证书化已证；仍需排斥低大素 PDEC 与高大素尾盈余 |
| Prime Matrix EDA AlphaTail rough conditional tail | 条件高大素尾盈余 | 已修正粗筛盈余分解为精确恒等式 `Delta_full=V_tail Delta_low+Xi_tail`，其中 `Xi_tail=|R|-|L|V_tail` 是低大素幸存集上的条件尾盈余。若 `Xi_tail>0`，等价于尾大素删除并集低于模型，进入 tail-mass `PDEC`、tail-overlap `Rankin/ColumnCRT` 或 `SAE`。新增脚本核验恒等式与尾一阶删除量 | `docs/monograph/prime-matrix-eda-alpha-tail-roughsurplus-conditional-tail.md`, `experiments/prime_matrix_alpha_tail_roughsurplus_tail_audit.py` | 否，条件分解已证；仍需排斥 tail-mass、tail-overlap、SAE 三出口 |
| Prime Matrix EDA AlphaTail tail-overlap Rankin | 条件尾删除重叠账本 | 已把 `Xi_tail>0` 且 tail-mass 不足以解释的分支转成尾命中重数 `h_T(d)` 与重叠预算 `Omega_T=T1-U_T`。证明了点态乘积上界 `h_T(d)<=L_T(z,m)`，并给出 Rankin 矩展开 `sum rho^{h_T}` 到有限 CRT 交集；持续高重叠必进入 `ColumnCRT/PDEC`，孤窗进入 `SAE`。新增脚本审计 `tail_hit_sum/tail_deleted/max_tail_hits/L_bound/overlap_excess` | `docs/monograph/prime-matrix-eda-alpha-tail-tail-overlap-rankin-ledger.md`, `experiments/prime_matrix_alpha_tail_tail_overlap_rankin_audit.py` | 否，归约已证；仍需排斥 ColumnCRT/PDEC/SAE，或给出全局 Rankin 交集矩常数 |
| Prime Matrix EDA AlphaTail tail intersection moments | 条件尾交集矩证书 | 已证明重叠预算 `Omega_T<=M2`，其中 `M_t=sum_d binom(h_T(d),t)` 等于 `t` 阶尾删除事件交集总量；乘法模型为 `B_t=|L|e_t(b_q/q)`，正偏差 `D_t=M_t-B_t` 即有限 CRT 交集偏差。样本中正 `Xi_tail` 同时伴随显著正 `D2/D3`，当前尾重叠硬点压缩为二阶/三阶 `ColumnCRT/PDEC` 或 `SAE` 排斥 | `docs/monograph/prime-matrix-eda-alpha-tail-tail-intersection-moment-certificate.md`, `experiments/prime_matrix_alpha_tail_tail_intersection_moment_audit.py` | 否，归约已证；仍需把二阶正偏差转成显式 Fourier/PDEC 下界并排斥 |
| Prime Matrix EDA AlphaTail pair CRTDefect Fourier bridge | 二阶尾素对偏差到 PDEC | 已证明 `D2=sum_{q1<q2}E(q1,q2)`，其中 `E` 是低幸存集在模 `Q=q1q2` 上与显式零均值函数 `G_{q1,q2}` 的相关；若 `E>0`，则存在非零 Fourier/CRT 系数满足显式下界，固定点位正偏差直接给出 `ColumnCRT` 尖峰。新增脚本输出每个样本的最热尾素对与点位向量 | `docs/monograph/prime-matrix-eda-alpha-tail-pair-crtdefect-fourier-bridge.md`, `experiments/prime_matrix_alpha_tail_pair_crtdefect_audit.py` | 否，桥接已证；仍需接入 H4-PDEC 模板并排斥热尾素对证书 |
| Prime Matrix EDA AlphaTail PairCRT-H4 attachment | 热尾素对接入 H4-PDEC | 已把固定尾素对与点位 `(q1,q2,j1,j2)` 写成单残基集合 `S_a={d in L:d=a mod q1q2}`，并逐项匹配 H4-PDEC 输入：`tau(d)=d mod Q`、`F_a=1_{t=a}-1/Q`、`kappa=1-1/Q`、`||F||_2=sqrt(1-1/Q)`、`L_PDEC=|S_a|/sqrt(Q)`。新增脚本输出热残基证书常数 | `docs/monograph/prime-matrix-eda-alpha-tail-paircrt-h4-pdec-attachment.md`, `experiments/prime_matrix_alpha_tail_pair_h4_pdec_attachment_audit.py` | 否，接入已证；仍需为 `S_a` 提交结构约束上界 `U_CRT<L_PDEC` 或转入 SAE/ColumnCRT 排斥 |
| Prime Matrix EDA AlphaTail PairCRT correlation-PDEC | 合并尾素对相关下界 | 已修正单残基接入过弱的问题：对合并尾素对事件 `R(q1,q2)` 定义零均值函数 `G_R=1_R-|R|/Q`，证明若偏差 `E(q1,q2)>0`，则低幸存集计数向量在模 `Q=q1q2` 上存在非零 Fourier 系数，显式下界 `L_corr=E sqrt(Q)/(sqrt(Q-1)sqrt(|R|(1-|R|/Q)))≈E/m`。persistent 正相关进入 PDEC，非 persistent 进入 SAE | `docs/monograph/prime-matrix-eda-alpha-tail-paircrt-correlation-pdec-lower-bound.md`, `experiments/prime_matrix_alpha_tail_pair_correlation_pdec_audit.py` | 否，相关下界已证；仍需跨窗口 persistent 聚合账本与 H4 上界排斥 |
| Prime Matrix EDA AlphaTail TailPairResonance peel | 尾素对共振剥离 | 已证明任意尾素对交集点满足乘数方程 `q1*u1-q2*u2=(j1-j2)r`；单位乘数支等价于 `q1-q2=(j1-j2)r`，即尾素对间距锁定为点位差乘以 `|r|`。样本最热尾素对均满足 `q2-q1=|r|`，说明二阶偏差主峰应先剥离为 `TailPairResonance/SAE`，剩余非共振部分才进入 correlation-PDEC | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-resonance-peeling.md`, `experiments/prime_matrix_alpha_tail_tailpair_resonance_audit.py` | 否，剥离恒等式已证；仍需全局上界 `D2_res` 容量不足，或排斥 TailPairResonance/SAE 出口 |
| Prime Matrix EDA AlphaTail TailPairResonance budget | 二阶共振预算上界 | 已把二阶交集矩拆成 `M2_equal+M2_non_equal`；等乘数支满足 `u(q1-q2)=(j1-j2)r`，只能来自有限短差值尾素对 gap 集，保守上界 `M2_equal<=m^2 sum_g #{q,q+g in P_T}`。新增脚本审计 `M2/B2/D2/equal/unit/non_equal` 与主 gap | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-resonance-budget.md`, `experiments/prime_matrix_alpha_tail_tailpair_resonance_budget_audit.py` | 否，预算分解已证；仍需给短差值尾素对计数配显式 Brun/Selberg 上界或有限证书 |
| Prime Matrix EDA AlphaTail TailPair shortgap certificate | 短差值尾素对容量证书 | 已把等乘数共振允许 gap 集显式化为 `G_r(m)={|jr|/u:1<=j<m,u|jr}`，并将粗系数 `m^2` 收紧为精确有向点位系数 `C_{g,m}(r)=#{(j1,j2):-(j1-j2)r>0,g|-(j1-j2)r}`，得到固定窗口证书 `M2_equal<=sum_g C_{g,m}#{q,q+g in P_T}`。脚本核验样本 `upper_pass=True` 并输出压缩倍数 | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-shortgap-certificate.md`, `experiments/prime_matrix_alpha_tail_tailpair_shortgap_certificate_audit.py` | 否，有限窗口精确系数证书已证；全局仍需 Brun/Selberg 固定差值素对常数包或 SAE/Endpoint 排斥 |
| Prime Matrix EDA AlphaTail TailPair geometric certificate | 尾素对共振几何截断 | 已证明固定 `q,g,j1,j2` 的等乘数共振候选起点唯一 `d=qu-j1r`，且必须落入当前窗口 `I_m`；因此 `M2_equal` 可由短 `q` 区间中的固定差值素对计数控制。新增脚本输出纯几何上界与低幸存精确计数，样本中 `low_survivor_exact==equal_actual` | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-geometric-certificate.md`, `experiments/prime_matrix_alpha_tail_tailpair_geometric_certificate_audit.py` | 否，几何截断已证；仍需统一短区间固定差值素对 Brun/Selberg 常数或 SAE/Endpoint 排斥 |
| Prime Matrix EDA AlphaTail TailPair Brun/Selberg envelope | 短区间固定差值素对常数包 | 已把几何截断容量转成固定 gap 短区间素对上界输入 `N_g(J)<=C_BS S_g |J|/log^2 J_- + endpoint`，并给出验收式 `M2_equal<=sum_{g,j1,j2} C_BS S_g |J|/log^2 J_- + endpoint`。新增脚本输出样本所需 `required_C_BS` 与最坏局部短区间 | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-brun-selberg-envelope.md`, `experiments/prime_matrix_alpha_tail_tailpair_brun_constant_audit.py` | 否，接口已证；仍需证明统一 `C_BS` 常数包，或把超预算短区间过密转入 SAE/Endpoint |
| Prime Matrix EDA AlphaTail TailPair Brun acceptance | Brun/Selberg 常数验收账本 | 已把尾素对常数包变成三分验收：`EnvelopePass`、`GlobalConstantGap`、`SAEEndpointCandidate`。给定 `C_global,C_local` 后，脚本严格判断每个窗口是否由平滑常数吸收，或输出最坏短区间素对过密责任项。样本在 `C_global=C_local=1.5` 下通过 | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-brun-acceptance-ledger.md`, `experiments/prime_matrix_alpha_tail_tailpair_brun_acceptance_audit.py` | 否，验收机制已证；仍需证明全局 `1.5` 常数或排斥局部 SAE/Endpoint 尖峰 |
| Prime Matrix EDA AlphaTail TailPair local spike route | 局部短区间尖峰路由 | 已把 `C_loc>C_local` 的失败精确化为 `TailPairLocalSpike` 责任证书 `(g,j1,j2,u,J,A,B,C_loc)`，并用 `d=qu-j1r` 映回原始窗口；责任区间按端点距离三分为 `EndpointSpike`、孤立 `InteriorSAE` 或 persistent `PDEC/ColumnCRT`。新增脚本输出超阈值短区间与回流类型 | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-local-spike-route.md`, `experiments/prime_matrix_alpha_tail_tailpair_local_spike_audit.py` | 否，路由已证；仍需排斥 EndpointSpike 或证明 InteriorSpike 非持久 |
| Prime Matrix EDA AlphaTail TailPair endpoint absorption | 端点尖峰吸收 | 已把 `EndpointSpike` 定义为 `d` 责任区间贴近 `I_m` 端点的局部尖峰，并证明其应回流 Endpoint concentration / Directed endpoint CRTDefect / PDEC-or-SAE；若 `interior_clear` 成立，则内部 TailPairResonance 由 `C_local` 常数包控制。样本在 `C_local=1.2,theta=0.1` 下内区尖峰为零 | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-endpoint-absorption.md`, `experiments/prime_matrix_alpha_tail_tailpair_endpoint_absorption_audit.py` | 否，端点吸收路由已证；仍需全局证明 `interior_clear` 或排斥 Endpoint/PDEC/SAE |
| Prime Matrix EDA AlphaTail TailPair smallshift endpoint | 小位移端点清除 | 已证明确定性充分引理：几何截断责任区间满足 `dist_I(D)<u<=(m-1)|r|`，因此若 `(m-1)|r|<=theta*|I_m|`，则所有局部尖峰都是 `EndpointSpike`，`InteriorSpike` 自动为空。审计显示小位移样本通过；较大位移样本需回到精确 endpoint absorption 审计 | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-smallshift-endpoint-lemma.md`, `experiments/prime_matrix_alpha_tail_tailpair_smallshift_endpoint_audit.py` | 否，小位移内区清除已证；剩余转为 Endpoint/PDEC/SAE 排斥、Brun/Selberg 常数包，以及 smallshift 失败窗口的精确 interior_clear |
| Prime Matrix EDA AlphaTail TailPair endpoint CRTDefect | 端点尖峰到有向CRT缺陷 | 已把 `EndpointSpike` 聚合成端点相位键 `K=(g,j1,j2,u,side)`；同一键的持久超额定义为 `TailPairEndpointDefect(K)`，非持久进入 SAE，持久则桥接到 `Directed Endpoint CRTDefect/PDEC`。新增持久性账本给出跨窗口 `persistent/SAE` 无损二分，样本 `41` 个端点尖峰压缩为 `14` 个持久键与 `13` 个 SAE 键；PDEC 输入包登记 `persistent_total_excess=169.647458`、`sae_total_excess=64.280293`；端点相位测试显式构造 `G_Q=(Z/QZ)^2`、`tau_Q=(D^-,D^+) mod Q` 与 `F_{K,Q}=1_T-|T|/Q^2`；Fourier 目标频率审计在 `Q=210` 下全部 `normalization_pass=True`；Parseval 能量地板证明仅靠质量与支撑大小无法得到 `U_CRT<L_PDEC`；镜像约束分出 `9` 个准入键与 `5` 个缺镜像键；责任频率路由把样本压缩为 `MirrorImbalance` 5 键、`OneSidedEndpoint/ColumnCRT` 8 键、`TwoEndpointMixed` 1 键；轴向锁相审计证明 8 个 OneSided 键全部精确锁到单一右端列残基；列残基反解把这 8 键压缩为两个低模右端列核；容量目标给出 `D^+==4 mod 35` 的 `C_req=20.247349`；嵌套压力抽取精确子目标并声明非不交；精确目标审计发现主列核全部 `10` 条记录实际钉在同一右边界 `D^+=16384`；边界恒等式证明这些记录全部由 `u=1` 强制；单位截断账本证明 `u=1=>D=I_m`；双端相位账本修正正式键为 `(L mod Q,R mod Q,g,j1,j2)`，样本 `26` 条单位截断记录仍全部进入 `UnitPhasePair/SAE`；最新归约把单位截断化为固定 gap 短区间常数问题，样本 `max_required_C=1.253939` | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-endpoint-crtdefect-bridge.md`, `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-endpoint-persistence-ledger.md`, `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-endpoint-pdec-input-ledger.md`, `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-endpoint-phase-test.md`, `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-endpoint-fourier-target.md`, `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-endpoint-energy-floor.md`, `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-endpoint-mirror-constraint.md`, `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-endpoint-frequency-route.md`, `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-endpoint-axis-lock.md`, `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-endpoint-column-residue.md`, `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-endpoint-column-capacity-target.md`, `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-endpoint-column-nested-pressure.md`, `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-endpoint-exact-column-target.md`, `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-endpoint-boundary-identity.md`, `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-endpoint-unit-truncation-ledger.md`, `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-endpoint-unit-phase-pair-ledger.md`, `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-endpoint-unit-shortgap-reduction.md`, `experiments/prime_matrix_alpha_tail_tailpair_endpoint_crtdefect_audit.py`, `experiments/prime_matrix_alpha_tail_tailpair_endpoint_persistence_audit.py`, `experiments/prime_matrix_alpha_tail_tailpair_endpoint_pdec_input_ledger.py`, `experiments/prime_matrix_alpha_tail_tailpair_endpoint_phase_test_audit.py`, `experiments/prime_matrix_alpha_tail_tailpair_endpoint_fourier_target_audit.py`, `experiments/prime_matrix_alpha_tail_tailpair_endpoint_energy_floor_audit.py`, `experiments/prime_matrix_alpha_tail_tailpair_endpoint_mirror_constraint_audit.py`, `experiments/prime_matrix_alpha_tail_tailpair_endpoint_frequency_route_audit.py`, `experiments/prime_matrix_alpha_tail_tailpair_endpoint_axis_lock_audit.py`, `experiments/prime_matrix_alpha_tail_tailpair_endpoint_column_residue_audit.py`, `experiments/prime_matrix_alpha_tail_tailpair_endpoint_column_capacity_target.py`, `experiments/prime_matrix_alpha_tail_tailpair_endpoint_column_nested_pressure.py`, `experiments/prime_matrix_alpha_tail_tailpair_endpoint_exact_column_target.py`, `experiments/prime_matrix_alpha_tail_tailpair_endpoint_boundary_identity.py`, `experiments/prime_matrix_alpha_tail_tailpair_endpoint_unit_truncation_ledger.py`, `experiments/prime_matrix_alpha_tail_tailpair_endpoint_unit_phase_pair_ledger.py`, `experiments/prime_matrix_alpha_tail_tailpair_endpoint_unit_shortgap_reduction.py` | 否，样本 OneSided 主分支已被压到固定差值短区间常数包；全局仍需证明固定 gap 局部常数，或提交有限 SAE/调整 `C_local` 后重审计 |
| Prime Matrix EDA AlphaTail TailPair local constant sensitivity | 固定 gap 局部常数阈值与全链重审计 | 新增局部常数灵敏度账本与全链重审计：样本 `6` 行中 `max_required_C_BS=0.857166`、`max_local_required_C=1.292474`；`C_local=1.2` 时有 `41` 个 EndpointSpike，`C_local=1.254` 时仍有 `7` 个，`C_local=1.3` 时全链输出 `spikes=0 endpoint=0 interior=0 downstream_empty=True`。该项说明样本端点/单位截断/PDEC 下游可由 `C_local=1.3` 吸收，但全局仍需证明固定 gap 短区间常数包或提交 SAE | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-local-constant-sensitivity.md`, `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-local-constant-chain-reaudit.md`, `experiments/prime_matrix_alpha_tail_tailpair_local_constant_sensitivity.py`, `experiments/prime_matrix_alpha_tail_tailpair_local_constant_chain_reaudit.py` | 否，样本阈值与样本全链已闭合；仍需全局固定 gap 常数 `<=1.3`，或有限/可求和 SAE 证书 |
| Prime Matrix EDA AlphaTail TailPair fixed gap C13 admissibility | `C_local=1.3` 的目标窗口族可采纳性 | 新增可采纳性审查：证明无条件“所有固定 gap 区间均满足 `C_local<=1.3`”为假，例如 `g=2,J={5}` 给出比值 `>2.58`；因此正式输入必须限定到目标窗口族并附尺度下界，或把超 `1.3` 窗口全部送入有限/可求和 `SAE/PDEC` 证书。样本最紧局部常数为 `1.292474`，外向余量仅约 `0.007526` | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-fixed-gap-c13-admissibility-audit.md` | 否，审稿边界更精确；剩余是证明目标窗口族的 `FGC-13-admissible` 或提交异常证书 |
| Prime Matrix EDA AlphaTail TailPair target interval scale | 固定 gap 目标区间尺度地板 | 新增尺度账本和脚本：在 `C_local=1.3` 下尺度地板为 `1/1.3=0.769231`；样本 `870` 个目标区间中 `low_scale=0`、`low_scale_positive=0`、`global_min_scale=1.056366`、`global_min_positive_scale=25.371688`。这排除样本中的单命中极短区间伪尖峰，说明剩余压力是中尺度局部素对密度问题 | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-target-interval-scale-ledger.md`, `experiments/prime_matrix_alpha_tail_tailpair_target_interval_scale_audit.py` | 否，样本尺度地板已审计；仍需全局尺度下界和中尺度 `C_local<=1.3` 或 SAE/PDEC 证书 |
| Prime Matrix EDA AlphaTail TailPair C13 integer slack | `C_local=1.3` 整数门槛余量 | 新增整数余量账本：`C13` 失败等价于 `N_g(J)>=floor(1.3B_g(J))+1`；样本 `870` 个目标区间中偶 gap 正命中 `167` 个、失败 `0`、全局最小整数余量 `1`。奇 gap 区间由奇偶刚性全部 `ParityVoid`，真正硬点收窄为偶 gap 中尺度区间的 `OnePairMargin-C13`，即排除跨过门槛的最后一个额外素对或将其证书化 | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-integer-slack-ledger.md`, `experiments/prime_matrix_alpha_tail_tailpair_c13_integer_slack_audit.py` | 否，样本整数余量已审计；仍需全局 `OnePairMargin-C13` 或 SAE/PDEC/ColumnCRT 排斥证书 |
| Prime Matrix EDA AlphaTail TailPair C13 endpoint gate | `C_local=1.3` 近门槛端点门控 | 新增端点门控账本：样本偶 gap 正命中 `167` 个；对 `slack<=1,2,4,8,12,20,40` 的所有近门槛区间，`interior=0`，全部为 `EndpointGate`，最大 `endpoint_ratio=0.000253`。最紧一票余量记录为 `p=997,m=5,gap=24,u=3,actual=65,threshold=66,slack=1`。这把样本 `OnePairMargin-C13` 压回端点链 | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-endpoint-gate-ledger.md`, `experiments/prime_matrix_alpha_tail_tailpair_c13_endpoint_gate_audit.py` | 否，样本近门槛端点化已审计；仍需全局 `EndpointGate-C13`，或将 `InteriorOnePair` 物化为 SAE/PDEC 证书 |
| Prime Matrix EDA AlphaTail TailPair lattice endpoint geometry | 责任区间格点端点几何 | 新增确定性引理：固定 gap 责任区间映回 `d=qu-j_1r` 后，左右端点距离均严格小于步长 `u`；因此若 `u<=theta|I|`，责任区间自动进入 `EndpointGate(theta)`。反之若 `u>theta|I|`，则 `q` 区间长度 `<1/theta+1`，取 `theta=0.1` 时非端点异常至多是 `10` 点短窗口。样本 `870` 条责任区间 `bound_failures=0`，`slack<=40` 的 `123` 条近门槛记录全部 `near_u_forced` | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-lattice-endpoint-geometry-lemma.md`, `experiments/prime_matrix_alpha_tail_tailpair_lattice_endpoint_geometry_audit.py` | 否，端点几何引理已证；剩余是排斥 large-u 短 q 例外，或提交其 InteriorSAE/PDEC 证书 |
| Prime Matrix EDA AlphaTail TailPair large-u short exception | 非端点短 `q` 例外 | 新增 large-`u` 例外账本：由格点几何，`u>0.1|I|` 的非端点责任区间满足 `q_length<=10`；样本中 large-`u` 例外 `12` 条，`positive=0`、`failures=0`，其中 `9` 条由奇 gap 奇偶刚性排除，剩余 `3` 条偶 gap 也无素对命中。该分支已从中尺度常数问题压成有限/可求和短窗口证书对象 | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-large-u-short-exception-ledger.md`, `experiments/prime_matrix_alpha_tail_tailpair_large_u_short_exception_audit.py` | 否，样本 large-u 分支清空；仍需全局短 `q` 例外证书或偶 gap 短窗口门槛排斥 |
| Prime Matrix EDA AlphaTail TailPair C13 two-branch route | 固定 gap `C13` 二分路由 | 新增二分路由定理：任何触及 `C13` 整数门槛的固定 gap 区间，若 `u<=0.1|I|` 则由格点端点引理自动进入 `EndpointGate`；若 `u>0.1|I|` 则 `q_length<=10`，成为 finite short-q `SAE/PDEC` 对象。结合奇 gap 排除，普通中尺度固定 gap 常数包被替换为端点 CRT 缺陷和至多 `10` 点短窗口证书。样本中近门槛全部端点化，large-u 分支无正命中 | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-two-branch-route-theorem.md` | 否，`C13` 路由已归约闭合；仍需端点 `PDEC/SAE/ColumnCRT` 排斥和全局 finite short-q 证书 |
| Prime Matrix EDA AlphaTail TailPair short-q finite certificate | short-`q` 有限证书与 TailCutoffVoid | 新增 short-`q` 证书合同与生成器：large-`u` 分支逐项枚举至多 `10` 个候选 `q`，并核验 `q,q+g` 是否均为 tail primes；若 `q_upper<=floor(alpha*p)`，则由 TailCutoffVoid 引理得 `N_g(J)=0`。样本 `12` 条 large-`u` 行全部 `tail_cutoff_void=True`，`max_q_upper=22`、`min_tail_cutoff=9006`、`positive_rows=0`、`all_certified=True` | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-short-q-finite-certificate.md`, `experiments/prime_matrix_alpha_tail_tailpair_short_q_certificate_builder.py` | 否，样本 short-q 分支证书闭合；仍需全局 TailCutoffVoid 不等式、finite q 证书全集或 persistent short-q PDEC 排斥 |
| Prime Matrix EDA AlphaTail TailPair TailCutoffVoid inequality | short-`q` 分支显式清空不等式 | 新增显式充分条件：large-`u` 分支若 `(B+j_1r)/(theta|I|)<=alpha p`，则 `q_upper<=floor(alpha p)`，由 TailCutoffVoid 得 `N_g(J)=0`。样本 `12` 条 large-`u` 行全部通过，`sufficient_failures=0`、`tail_cutoff_failures=0`、`max_sufficient_ratio=0.002690`、`max_q_upper=22`、`min_tail_cutoff=9006` | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-tail-cutoff-void-inequality-ledger.md`, `experiments/prime_matrix_alpha_tail_tailpair_tail_cutoff_void_inequality_audit.py` | 否，样本充分不等式闭合；仍需目标无限窗口族上的全局 `(TCV-3)` 证明或例外证书 |
| Prime Matrix EDA AlphaTail TailPair C13 endpoint phase ledger | small-`u` 端点相位键接入 | 新增 C13 端点相位键账本：small-`u` 近门槛记录按 `K=(g,j1,j2,u,side)` 接入既有 `Endpoint/PDEC/SAE/ColumnCRT` 链。样本 `slack<=40` 的端点记录 `123` 条、实际失败 `0`、相位键 `59` 个；最紧键为 `(24,2,0,3,left)` 与 `(24,3,1,3,left)`，`min_slack=1`。这把 C13 端点分支从素对常数问题改写为端点相位键持久性问题 | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-endpoint-phase-ledger.md`, `experiments/prime_matrix_alpha_tail_tailpair_c13_endpoint_phase_ledger.py` | 否，样本端点键账本闭合；仍需全局持久端点键排斥或 SAE 可求和账本 |
| Prime Matrix EDA AlphaTail TailPair C13 endpoint persistence contract | C13 端点失败质量出口合同 | 新增 C13 端点持久性合同：定义整数失败质量 `mu_13=max(0,1-slack)`，严格区分真实失败键与 near-threshold watch 键；只有 `mu_13>0` 的键可进入 `PDEC/SAE`，`mu_13=0` 只能作为观察项。样本 `records=123`、`keys=59`、`failure_records=0`、`failure_keys=0`、`failure_mass=0`，全部为 `NearThresholdWatchOnly` | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-endpoint-persistence-contract.md`, `experiments/prime_matrix_alpha_tail_tailpair_c13_endpoint_persistence_contract.py` | 否，端点失败质量口径已闭合且样本无失败；仍需全局证明 `mu_13=0` 或排斥 persistent failure key / 证明 SAE 可求和 |
| Prime Matrix EDA AlphaTail TailPair C13 witness barrier | C13 失败尾素对见证障碍 | 新增见证级障碍：对任意失败责任区间定义 `P_g(J)={q in J:q,q+g tail prime}`，证明失败质量 `mu_13=N_g-(floor(1.3B_g)+1)+1` 可无损物化为同样数量的规范尾素对见证；删除这些见证后整数余量恢复为 `1`。样本 `records=123`、`failures=0`、`failure_mass=0`、`identity_failures=0`、`min_extra_to_failure=1` | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-witness-barrier.md`, `experiments/prime_matrix_alpha_tail_tailpair_c13_witness_barrier.py` | 否，见证障碍已证且样本无失败见证；仍需全局排除 witness set，或将 persistent witness phase 送入 PairPhase-PDEC/ColumnCRT 并排斥 |
| Prime Matrix EDA AlphaTail TailPair C13 witness phase ledger | C13 失败见证相位输入 | 新增见证相位账本：证明任意失败见证 `(q,q+g)` 满足同商数锁定 `d+j1*r=q*u` 与 `d+j2*r=(q+g)*u`，并为每个见证原子登记 `shape_key=(g,j1,j2,u,side)`、`Q_pair=q(q+g)`、`tau_pair=d mod Q_pair`、端点深度 `depth`。样本 `C=1.3` 下 `atoms=0, shapes=0`；压力测试 `C=1.2` 下 `atoms=281, shapes=37, quotient_lock_failures=0`，路由为 `PairPhase-PDEC/ColumnCRT:32, SAEWitness:5` | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-witness-phase-ledger.md`, `experiments/prime_matrix_alpha_tail_tailpair_c13_witness_phase_ledger.py` | 否，见证相位输入已闭合；仍需全局证明 `atoms=0`，或为 persistent shape_key 构造 `U_CRT<L_PDEC`，或给 SAEWitness 可求和账本 |
| Prime Matrix EDA AlphaTail TailPair C13 pairphase modulus route | 固定模/变模见证分流 | 新增固定模/变模分流账本：指出同一 `shape_key` 不必共享同一 `Q_pair=q(q+g)`，因此不能把变模事件直接作为单一 PDEC；证明端点深度阶梯 `s=epsilon+u*h`，并将见证原子无损拆成 `FixedModulus-PDEC`、`MovingModulusDepth-SAE` 与混合分支。样本 `C=1.3` 下 `atoms=0`；压力 `C=1.2` 下 `atoms=281, fixed_atoms=114, moving_atoms=167, depth_failures=0` | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-pairphase-modulus-route.md`, `experiments/prime_matrix_alpha_tail_tailpair_c13_pairphase_modulus_route.py` | 否，模兼容分流已闭合；仍需固定模 `U_CRT<L_PDEC`，以及变模深度阶梯的 SAE 可求和或 cross-modulus stitching |
| Prime Matrix EDA AlphaTail TailPair C13 fixed modulus formal unit | 固定模见证 formal unit 去重 | 新增固定模 formal unit 去重账本：定义物理见证键 `(p,B,r,g,j1,j2,u,side,q,q+g,d)`，规定 `m` 层不构成独立 PDEC 单位；同一物理见证在 `m=4/5` 中重复只能计一次。样本 `C=1.3` 下 `raw_atoms=0`；压力 `C=1.2` 下 `raw_atoms=281, formal_atoms=224, removed_duplicates=57, raw_fixed_atoms=114, formal_fixed_atoms=0` | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-fixed-modulus-formal-unit.md`, `experiments/prime_matrix_alpha_tail_tailpair_c13_fixed_modulus_formal_unit.py` | 否，样本与压力样本的固定模重复已清空；仍需全局证明 `formal_fixed_atoms=0`，或对真实 formal fixed modulus 构造 `U_CRT<L_PDEC` |
| Prime Matrix EDA AlphaTail TailPair C13 moving depth slot budget | 变模见证端点深度槽预算 | 新增变模深度槽预算：formal moving atom 按 `Xi=(p,B,r,K,epsilon,h)` 登记，证明每个深度槽负载至多为有限点位层数 `|M|`。样本 `C=1.3` 下无原子；压力 `C=1.2` 下 `raw=281, formal=224, fixed=0, moving=224, slots=215, slot_capacity=430, max_slot_load=2, capacity_failures=0` | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-moving-depth-slot-budget.md`, `experiments/prime_matrix_alpha_tail_tailpair_c13_moving_depth_slot_budget.py` | 否，变模 SAE 容量单位化已闭合；仍需全局 depth slot 总量可求和，或 persistent depth slot 的 stitching/ColumnCRT 排斥 |
| Prime Matrix EDA AlphaTail TailPair C13 depth band envelope | 深度槽端点带宽 envelope | 新增端点带宽 envelope：若深度 `s<=beta|I|` 且 `s=epsilon+u*h`，则固定 `(p,B,r,K,epsilon)` 的允许槽数至多 `floor((beta|I|-epsilon)/u)+1`；若超带宽则命名为 `BulkDepthOverflow` 出口。样本 `C=1.3` 下无原子；压力 `C=1.2` 下 `moving=224, band=224, overflow=0, groups=38, observed_slots=215, envelope_slots=24029, max_obs_over_env=0.037594` | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-depth-band-envelope.md`, `experiments/prime_matrix_alpha_tail_tailpair_c13_depth_band_envelope.py` | 否，envelope 前置已闭合；仍需 envelope 内 witness slots 的全局稀疏/可求和上界，或高密度 envelope 的 stitching/ColumnCRT 排斥 |
| Prime Matrix EDA AlphaTail TailPair C13 band sparse acceptance | 带宽 envelope 稀疏验收 | 新增稀疏/高密度二分：对每个 envelope group 定义 `rho=observed_slots/envelope_slots`，若 `rho<=eta=1/25` 则进入 `SparseSAE` 并有 atoms `<=|M|*eta*Omega(E)`，否则进入 `HighDensityEnvelope`。样本 `C=1.3` 下无原子；压力 `C=1.2, eta=0.04` 下 `groups=38, accepted=38, high=0, max_density=0.037594, min_eta_slack=0.320000`；`eta=0.03` 路线测试触发 `high=3` | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-band-sparse-acceptance.md`, `experiments/prime_matrix_alpha_tail_tailpair_c13_band_sparse_acceptance.py` | 否，稀疏验收接口已闭合；仍需全局证明所有反例 envelope 稀疏并总量可求和，或排斥 HighDensityEnvelope |
| Prime Matrix EDA AlphaTail TailPair C13 high density envelope certificate | 高密度 envelope 层投影证书 | 新增高密度出口证书：若某 envelope group 满足 `S(E)>eta*Omega(E)`，则存在具体 `m` 层满足 `S_m(E)>=ceil(S(E)/|M|)>eta*Omega(E)/|M|`，形成固定差值端点带高密度尾素对块并进入 stitching/ColumnCRT。压力 `C=1.2, eta=0.04` 下 `high_groups=0`；路线测试 `eta=0.03` 下 `high_groups=3, high_slots=14, max_best_layer_density=0.030075`，并输出具体 witness pairs | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-high-density-envelope-certificate.md`, `experiments/prime_matrix_alpha_tail_tailpair_c13_high_density_envelope_certificate.py` | 否，高密度出口已物化；仍需排斥 LayerHighDensityEndpointPair 或证明全局不出现 HighDensityEnvelope |
| Prime Matrix EDA AlphaTail TailPair C13 layer interval reduction | 高密度层一维固定 gap 区间归约 | 新增一维归约：固定高密度层内 `h` 与 `q` 一一对应，故 `LayerHighDensityEndpointPair` 给出普通 q-区间 `J_band`，其中至少有 `S_m(E)` 个尾素对 `q,q+g`。路线测试 `C=1.2, eta=0.03` 输出 `3` 个高密度区间：`g=12,J=[1390,1522]` 与两个 `g=24` 区间，均有 `4` 个 witness pairs，`max_required_C=0.787594` | `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-layer-interval-reduction.md`, `experiments/prime_matrix_alpha_tail_tailpair_c13_layer_interval_reduction.py` | 否，高密度出口已一维化；仍需全局排斥固定 gap 端点带高密度区间，或证明 `eta=1/25` 下无 HighDensityEnvelope |
| Prime Matrix factor descent | 早期零行乘数因子降阶路线 | 已证明若 `x=pi y` 且前 `pi-1` 列无层级泄漏，则得到 `pi`-筛零行乘数 `P y`；若其 `mod M_pi` 最小正代表 `<=pi`，则与 `EDA(pi)` 矛盾。最小反例因此强制每个 `pi|x` 发生中高标签泄漏或 CRT 代表逃逸 | `docs/monograph/prime-matrix-eda-factor-descent-obstruction.md`, `experiments/prime_matrix_factor_descent_audit.py` | 否，条件下降已证；仍需证明所有因子不能同时支付 Leakage/RangeEscape 而不触发 LowMod/Tail/PDEC 缺陷 |
| Prime Matrix BPN-BK final exits | 边界相位非覆盖最终出口 | 已严格压缩为证书型验收义务：`PDEC-Cert`、`SAE-Cert`、正式着色走廊 `Rankin certificates`；PDEC 上界进一步拆成显式坏窗相位计数证书与线性对偶主控证书；结构约束账本已拆为 mass/mirror/column/tail/core/Rankin 原子；第一批真实系数行已由 `P=23,Q=210` 完整 CRT 枚举生成；`low-hole bucket` 已改写为高层 CRT 残基类 set-cover 容量；列残基刚性证明 `B_{ell,a}` 只由 `c mod ell` 决定；`Q=2310,13<=P<61` 的全部 zero phases 已由低范围最终证书闭合：`15414` 个相位分解为 `15282` 个整洞集亏损、`108` 个桥洞临界、`24` 个 `P=41` 精确 DP 临界；动态贪心证书显示 `P>=61,P<=109` 全相位可补完；固定升序碰撞梯证书进一步显示 `P>=61,P<=149` 全相位可补完，并把转折后硬点压成 `LHB-7` 重复增益不等式；主定理稿已把 `LHB-7` 再拆成列残基碰撞能量下界；鸽巢尾段审计到 `P<=100000` 只剩十个失败素数，`P=107` 起由纯鸽巢递推闭合；`P/5` 分割判据在 `P>=107` 扫描段无失败；连续乘积上界从 `P=233` 起扫描无失败；保守显式常数包给出 `P>=13208` 解析闭合阈值；两段有限尾段证书已生成并通过：`107<=P<=229` 共 `23` 行、`233<=P<=13207` 共 `1520` 行；十个窄带素数 `61<=P<=103` 的 `23100` 个低相位碰撞能量证书已通过 | `docs/monograph/prime-matrix-bpn-bk-selberg-route.md`, `docs/monograph/prime-matrix-bpn-final-exit-acceptance-contract.md`, `docs/monograph/prime-matrix-bpn-final-residual-hard-attack.md`, `docs/monograph/prime-matrix-bpn-pdec-dual-certificate-framework.md`, `docs/monograph/prime-matrix-bpn-pdec-constraint-ledger.md`, `docs/monograph/prime-matrix-bpn-pdec-real-constraint-rows.md`, `docs/monograph/prime-matrix-bpn-low-hole-bucket-capacity-theorem.md`, `docs/monograph/prime-matrix-bpn-low-hole-bucket-capacity.md`, `docs/monograph/prime-matrix-bpn-low-hole-bucket-capacity-q2310.md`, `docs/monograph/prime-matrix-bpn-lhb-bridge-deletion-audit.md`, `docs/monograph/prime-matrix-bpn-lhb-column-residue-rigidity-audit.md`, `docs/monograph/prime-matrix-bpn-lhb-column-residue-rigidity-extended.md`, `docs/monograph/prime-matrix-bpn-lhb-low-range-final-certificate.md`, `docs/monograph/prime-matrix-bpn-lhb-greedy-cover-transition-audit.md`, `docs/monograph/prime-matrix-bpn-lhb-fixed-ladder-audit.md`, `docs/monograph/prime-matrix-bpn-lhb-pigeonhole-tail-audit.md`, `docs/monograph/prime-matrix-bpn-lhb-explicit-tail-constant-audit.md`, `docs/monograph/prime-matrix-bpn-lhb-tail-finite-certificate.md`, `docs/monograph/prime-matrix-bpn-lhb-narrow-band-collision-certificate.md`, `docs/monograph/prime-matrix-bpn-pdec-certificate-audit.md`, `docs/monograph/prime-matrix-bpn-pdec-dual-certificate-audit.md`, `docs/monograph/prime-matrix-bpn-rankin-ledger-acceptance-theorem.md`, `docs/monograph/prime-matrix-bpn-rankin-ledger-certificate-audit.md` | 否，需核验 `P>=13208` 显式常数引用；SAE 全列表和正式 Rankin 证书全集尚未提交 |
| Prime Matrix PTA/RSE | 尾段粗锚短区间分布 | 已压缩为 QLOW-MID-COMP/RRD/OSPC 常数账本；RRD 进一步拆成 low/perp/conversion；OSPC 归一化已修正；low-block 出口已代数化 | `docs/monograph/pta-gsl-hard-attack.md`, `docs/monograph/rse-critical-band-hard-attack.md`, `docs/monograph/qlow-mid-comp-grid-certificate.md`, `docs/monograph/qlow-mid-comp-interval-budget.md`, `docs/monograph/selberg-rational-weight-audit.md`, `docs/monograph/trig-log-interval-oracle-audit.md`, `docs/monograph/qlow-mid-comp-hq-interval-audit.md`, `docs/monograph/qlow-mid-comp-supnorm-audit.md`, `docs/monograph/rse-rrd-ospc-margin-ledger.md`, `docs/monograph/rse-rrd-same-weight-reduction.md`, `docs/monograph/rse-rrd-low-projection-dichotomy.md`, `docs/monograph/rse-low-block-exit-criterion.md` | 否，QLOW-MID-COMP 样本已由 sup-rho 绕开 Phihat；`RRD-low` 已压成加权 CRT 缺陷界 `<=0.0053666` 或 OSPC* 出口；仍需证明该界和 `RRD-perp` 上界 |
| Prime Matrix D | Structured-EHPD 排斥 | 审稿包/需逐行复核 | `docs/final-top-journal-unconditional-review.md` | 否 |
| Prime Matrix finite | 小素数有限验证 | 计算证书 | `docs/finite-verify-exp5.json` 等 | 仅覆盖有限段 |
| RH PC1/PC2 | 离线零点到素数异常与 CRT baseline | 主稿编号化 | `paper/rh-proof/rh-contradiction-field.tex` | 需 referee verification |
| RH C4/C5/C6/C9 | sparse/dense/no-cycle/tail | 主稿编号化 | `paper/rh-proof/rh-contradiction-field.tex` | 需 referee verification |
| RH AEX/GEE | analytic exits 与 global exit exclusion | 主稿合成，审稿包完成 | `docs/rh-final-referee-obligations-closure.md` | 需 referee verification |
| RH EXT | 外部解析输入 | 章节/论文级定位完成 | `docs/rh-u3-ext-reference-table.md` | 专著页码仍需 copyediting |
| RH U5 | LaTeX/PDF/BibTeX | 已完成 | `docs/rh-u5-final-compile-audit.md` | 工程项完成 |

## 结论

合著论著当前应标为“contradiction-field synthesis and verification manuscript”。不得标为“RH 与方阵行列命题的最终无条件证明”。

## 审稿闭合更新

新增 `docs/monograph/referee-review-and-closure-audit.md`。合著论著当前已经闭合的是“审稿结构、依赖边界、状态标注和统一矛盾场方法”；尚未闭合的是“RH 与方阵行列命题作为最终无条件定理”。后者必须等待 Prime Matrix D 组排斥与 RH controlled exits 的独立逐行 referee verification。

## H4-PDEC 证书模板更新

新增 `docs/monograph/h4-pdec-certificate-template.md`。Prime Matrix BPN-BK 的 persistent
出口现在有固定验收格式：先由零均值测试函数得到
`L_PDEC=kappa |S|/(sqrt(Q-1)||F||_2)`，再由同一坏窗集合的结构约束矩阵
`A,b,E,e` 证明 `U_CRT<L_PDEC`。该文件只闭合证书格式；正式 `PDEC exclusion`
仍需提交完整约束来源证明、全频率方向对偶或显式证书，以及严格余量核验。

新增 `docs/monograph/h4-pdec-constraint-source-lemmas.md`。该文件完成 H4-PDEC 的首批
约束来源引理：质量与非负性、相位容量继承、镜像闭合/成对容量、low-hole bucket
容量继承、条件出口路由行。它把可进入 `A,b,E,e` 的行与仍不可用的启发式行区分开；
但尚未提交足以证明 `U_CRT<L_PDEC` 的完整约束表和全频率证书。

新增 `docs/monograph/h4-pdec-admissible-constraint-table.md`。该文件给出第一版准入矩阵，
把 PDEC 候选行分为 `Tautology / FiniteCert / SymbolicReady / ConditionalRouting /
NeedsProof / Rejected`。当前已经明确拒绝 full-cycle balance 直接作用于坏窗子集、
有限样本相位表直接全局推广、以及未证明镜像闭合时使用强 mirror equality。

新增 `docs/monograph/h4-pdec-column-cap-source-lemma.md`。该文件把 column cap 的合法来源
固定为有限列投影容量、符号化列容量定理和条件列路由行，并严写列见证位移非零刚性。
当前状态是来源规则闭合、`B_col(j)` 系数账本与 ColumnDefect 路由证书未填。

新增 `docs/monograph/h4-pdec-column-cap-coefficient-ledger.md`。该文件登记 V1 column cap
系数源：有限列见证半径、RCI/CDB 联合审计界值、`Q=2310` LHB 列残基刚性界值和条件
ColumnDefect 路由模板。当前状态是系数源已登记、机器可读相位块仍未物化。

新增 `experiments/prime_matrix_bpn_lhb_column_phase_blocks.py` 与
`docs/monograph/h4-pdec-lhb-column-phase-blocks.json/md`。`Q=2310`、`13<=p<=47`
的 LHB column rows 已物化为 `45` 条机器行，空异常块全部通过 `bound=0`；诊断支撑行
仍需投影容量证明后才能进入最终 `A,b,E,e`。

新增 `docs/monograph/h4-pdec-lhb-support-to-capacity-transfer.md`。该文件把诊断支撑行转容量行的条件严写为相位指示、多重度界或允许全集投影容量三选一；当前优先硬点是用 `phase_cap_t` 或窗口互斥建立 `T3-multiplicity`。

新增 `docs/monograph/h4-pdec-lhb-multiplicity-cap-route.md`。该文件把 `T3-multiplicity`
正式化为 `M(t)` 输入合同：若同一 `(p,Q,S,tau)` 下有 `g(t)<=M(t)`，则
`WHOLEDEF/BRIDGED` 可用 `bound=sum_{t in C}M(t)` 升级为容量行。该路线防止把
`phase_block_size` 误当作 persistent 容量界。

新增 `experiments/prime_matrix_bpn_lhb_multiplicity_cap_certificate.py` 与
`docs/monograph/h4-pdec-lhb-multiplicity-cap-certificate.json/md`。`Q=2310` 的 `M(t)`
已按高层 CRT 补洞完成数物化；`P=13,17,19,23,29,31,37,43,47` 的 `WHOLEDEF/BRIDGED`
支撑块均给出 `bound=0`。该结论只在已证明 `S subset Z_LHB` 的 LHB allowed-set 分支中
可用；全局 PDEC 仍需接入包含关系或失败路由。

新增 `docs/monograph/h4-pdec-lhb-attachment-lemma.md`。该文件证明 LHB 型坏窗满足
`S subset Z_LHB(p,Q)`，从而上述 `bound=0` 容量行可正式用于 LHB 型 PDEC 分支。
该项把 LHB 接入口闭合；全局 PDEC 仍未排除。

新增 `docs/monograph/h4-pdec-bad-window-classification-lemma.md`。该文件将非空命名
低模坏窗分成 `SAE / LHB-PDEC / Routed-PDEC` 三类；排除非 LHB 出口后的 persistent
剩余分支可使用 LHB `bound=0` 容量行。该项仍是路由闭合，不是出口排斥。

新增 `docs/monograph/h4-pdec-homogeneous-splitting-lemma.md`。该文件闭合 `C0/C4`
口径混合处理：混合坏窗集合必须按 `(Q,tau,F,kappa,p,window-shape)` 无损拆分，拆分后
逐子族应用 `UPS-1` 和坏窗分类。剩余出口不再包含口径混合。

新增 `docs/monograph/h4-pdec-column-defect-routing-contract.md`。该文件把
`ColumnRadius/ColumnCRT` 条件路由写成正式证书对象：`ColumnRadius` 行使用半径阈值
`D_0`、列见证选择器和相位兼容权重 `W_D(t)`；`ColumnCRT` 行使用标签 `ell`、非零位移余类
`a`、阈值 `L_D` 和相位兼容权重 `W_{ell,a}(t)`。该项闭合的是 `CC-COND-RADIUS/CC-COND-DISPLOAD`
的路由元数据，不是出口排斥；下一步仍需物化权重并证明阈值或排除这些出口。

新增 `experiments/prime_matrix_h4_pdec_column_defect_weight_certificate.py` 与
`docs/monograph/h4-pdec-column-defect-weight-certificate.json/md`。证书在有限细化相位
`tau_fin=(p,q,row)` 上覆盖 `835` 条紧行相位，并物化两条空异常块：
`CC-FIN-TIGHT-RADIUS-WEIGHT` 与 `CC-FIN-DISPLOAD-WEIGHT`。观测最大列见证半径为 `81`，
最大位移余类负载为 `2`。该项只升级有限证书行，不升级全局 Prime Matrix 终局。


## 内部逐行复核更新

新增 `docs/monograph/line-by-line-internal-referee-matrix.md`。作者侧逐行复核未发现新的 `BLOCK-MATH`，但 Prime Matrix 终局与 RH 终局仍为 `BLOCK-REFEREE`：必须由独立审稿接受 D-structure/Tail-log4/finite 接口与 RH controlled exits 后，才可升级为最终无条件定理。

## Prime Matrix PTA/RSE 更新

新增 `docs/monograph/pta-gsl-hard-attack.md`、`docs/monograph/rse-reciprocal-sum-scan.md`、`docs/monograph/rse-critical-band-hard-attack.md`、`docs/monograph/cwm-selberg-critical-mass-scan.md`、`docs/monograph/scwm-crd-profile-scan.md`、`docs/monograph/kscwm-crd-dual-obstruction-scan.md`、`docs/monograph/skt-smooth-transform-scan.md`、`docs/monograph/sqf-quadratic-form-scan.md`、`docs/monograph/sqf-qlow-optimal-weight-scan.md`、`docs/monograph/sqf-qlow-fixed-low-stability-scan.md`、`docs/monograph/sqf-qlow-mid-weighted-absorption-scan.md`、`docs/monograph/qlow-mid-comp-grid-certificate.md`、`docs/monograph/qlow-mid-comp-interval-budget.md`、`docs/monograph/selberg-rational-weight-audit.md`、`docs/monograph/trig-log-interval-oracle-audit.md`、`docs/monograph/qlow-mid-comp-hq-interval-audit.md`、`docs/monograph/qlow-mid-comp-supnorm-audit.md`、`docs/monograph/rse-rrd-ospc-margin-ledger.md`、`docs/monograph/rse-rrd-same-weight-reduction.md`、`docs/monograph/rse-rrd-low-projection-dichotomy.md` 与 `docs/monograph/rse-low-block-exit-criterion.md`。`SQF-QLOW` 已进一步拆成 `QLOW-OPT + QLOW-ULTRA + QLOW-TRANS + QLOW-MID + QLOW-VAR`。最新证书显示 `QLOW-MID` 可再拆成固定紧区间 `QLOW-MID-COMP` 与平滑尾部 `QLOW-MID-TAIL`；尾部是标准 Mellin 衰减，最后单点硬核已变成 `2<u<=12` 上的外向舍入常数证书与统一 Selberg 矩常数。误差预算表显示预留 `0.065` 外向舍入误差后，最紧样本仍有 `0.052304` 余量；Selberg 有理审计显示当前样本的 `Aλ=q0e1` 残差精确为零；trig/log 有理 oracle 半径为 `2.333e-67`，对应 H/Q 归一化乘积增量为 `6.600e-67`；sup-rho 旁路给出 `supBound=0.296630<0.35`，从而紧区间不再依赖 Phihat 数值求积。新增 RRD/OSPC 余量账本把剩余主链明确为 `C_RRD+C_OSPC+C_SelbergUniform+C_round<0.053369509758272926`，其中预算目标为 `0.020+0.020+0.008+0.003=0.051`。RRD 同权审查进一步说明旧单密度替换最坏 `roughDiff/env≈0.200`，必须拆为 `RRD-low<=0.006`、`RRD-perp<=0.012`、`RRD-conversion<=0.002`；低模投影审查把 `Pi_{<=Z}` 定义为低模字典正交投影，并将 `OSPC` 修正为 `E_dir>=1+delta_dir`；低模块出口准则进一步给出无 `OSPC*` 时吸收 `RRD-low` 所需的加权 CRT 缺陷界 `0.005366563145999495`。

## Prime Matrix RCI/WSH 更新

新增 `docs/monograph/prime-matrix-semiprime-wheel-shadow-rigidity.md`、`docs/monograph/prime-matrix-semiprime-wheel-shadow-audit.md`、`docs/monograph/prime-matrix-semiprime-wheel-near-offset-audit.md` 与脚本 `experiments/prime_matrix_semiprime_wheel_shadow_audit.py`。`Distributed-RCI` 的半素数补洞硬点已从普通 `LPH/PDEC` 升级为 `WSH-Hall/PDEC`：双粗半素数附近的候选素数偏移必须避开每个小素数的唯一禁类；固定偏移 `d` 的粗相位容量精确为 `rho_z(d)=prod_{r<=z,r∤d}(r-2)/(r-1)`。这严格吸收 `6K±1`、`30` 轮筛和 `P±s` 小素因子层锁现象。状态仍是严格归约：尚需证明轮筛允许 Hall 条件，或证明失败必触发固定偏移 CRTDefect、Tail-anchor 或 Endpoint/PDEC。

新增 `docs/monograph/prime-matrix-wsh-scb1-long-block-expansion-template.md`、
`docs/monograph/prime-matrix-wsh-scb1-long-block-certificate.md/json` 与脚本
`experiments/prime_matrix_wsh_scb1_long_block_certificate.py`。`SCB-1` 长块有限证书显示：
`|B|>=4` 的 `4573823` 个长块最小 Hall 余量为 `3`，负/零余量均为 `0`；全部最紧长块触发
`Fixed-offset-full-load` 与 `Endpoint-margin`。该项只把长块分支压缩为
`long-block expansion or fixed-offset/PDEC absorption`，不能改写为全局 `WSH-Hall` 定理。

新增 `docs/monograph/prime-matrix-wsh-fixed-offset-pdec-absorption.md`、
`docs/monograph/prime-matrix-wsh-fixed-offset-pdec-ledger.md/json` 与脚本
`experiments/prime_matrix_wsh_fixed_offset_pdec_ledger.py`。固定偏移满载已证明无第三逃逸：
满载候选若非素数，必有 `(13,p]` 中解释因子。有限账本核验 `47` 个候选中 `32` 个缺失候选
全部有 `<=p` 因子，`missing_without_factor<=p=0`。该项把剩余压缩为
`FO-PDEC => PDEC/SAE/Endpoint`，仍不能宣称全局无条件闭合。

新增 `docs/monograph/prime-matrix-wsh-fo-pdec-hard-attack.md`、
`docs/monograph/prime-matrix-wsh-fo-pdec-lowmod-audit.md/json` 与脚本
`experiments/prime_matrix_wsh_fo_pdec_lowmod_audit.py`。`FO-PDEC` 的方程层已闭合：
`43` 条低模方程全部满足 CRT 行方程和双尾双线性方程。剩余精确为
`low-mod defect energy >= PDEC threshold or SAE/Endpoint` 的全局不等式，尚不能升级为
方阵行列命题无条件证明。

新增 `docs/monograph/prime-matrix-wsh-fo-pdec-energy-lemma.md`、
`docs/monograph/prime-matrix-wsh-fo-pdec-energy-ledger.md/json` 与脚本
`experiments/prime_matrix_wsh_fo_pdec_energy_ledger.py`。`FO-PDEC` 的能量产生半边已证明：
无高负载解释因子时低模能量 `>= (1-theta)|E|`，有高负载时进入 `Tail/PDEC`。有限账本在
`theta=0.25` 下给出全局单位方程能量 `0.9547817296210457` 且无高负载。剩余仍是同一坏窗集合上的
`PDEC` 阈值比较，不能宣称全局无条件闭合。

新增 `docs/monograph/prime-matrix-wsh-fo-pdec-threshold-comparison.md`、
`docs/monograph/prime-matrix-wsh-fo-pdec-threshold-ledger.md/json` 与脚本
`experiments/prime_matrix_wsh_fo_pdec_threshold_ledger.py`。阈值下界侧已显式到
`ell=199,h=95,M=3.959247567099438`。剩余是证明同一投影的
`U_CRT,199<3.959247567099438`，或将其转入 `SAE/Endpoint`。

新增 `docs/monograph/prime-matrix-wsh-fo-pdec-dual-cluster-route.md`、
`docs/monograph/prime-matrix-wsh-fo-pdec-dual-cluster-audit.md/json` 与脚本
`experiments/prime_matrix_wsh_fo_pdec_dual_cluster_audit.py`。`U_CRT,199` 障碍已定位为
`h=95` 后长度 `11` 的对偶短弧聚簇；纯质量上界只差约 `1.02%`。剩余是
`DualCluster-Exclusion` 或 `SAE/Endpoint` 吸收。

新增 `docs/monograph/prime-matrix-wsh-fo-pdec-multiplicity-legitimacy.md`、
`docs/monograph/prime-matrix-wsh-fo-pdec-primitive-cluster-audit.md/json` 与脚本
`experiments/prime_matrix_wsh_fo_pdec_primitive_cluster_audit.py`。审计显示 `ell=199,h=95`
强阈值依赖 equation/block-local 多重计数；physical 去重后质量为 `2`、Fourier 为
`1.9699193446802263`。剩余新增集合一致性义务：证明多重计数合法，或改用 primitive 口径。

新增 `docs/monograph/prime-matrix-wsh-fo-pdec-formal-unit-route.md`、
`docs/monograph/prime-matrix-wsh-fo-pdec-formal-unit-audit.md/json` 与脚本
`experiments/prime_matrix_wsh_fo_pdec_formal_unit_audit.py`。审计进一步显示强阈值来自跨 `q`
层和嵌套块的有限库聚合；单个正式单元坐标去重后最佳 Fourier 仅为 `1.0`。因此当前最小义务
升级为 `FormalUnit-Stitching / NestedBlock-Independence / SAE-Endpoint absorption`，不能直接用
`3.959...` 宣称全局无条件闭合。

新增 `docs/monograph/prime-matrix-wsh-fo-pdec-branch-separation-theorem.md`、
`docs/monograph/prime-matrix-wsh-fo-pdec-stitching-feasibility-audit.md/json` 与脚本
`experiments/prime_matrix_wsh_fo_pdec_stitching_feasibility_audit.py`。已证明不同 `q` 层不能无
拼接定理合并，同坐标嵌套重复不能无加权 Hall 对偶行重复计数。当前剩余精确为
`Weighted Hall Dual Independence` 或 exact duplicate `SAE/Endpoint` 吸收。

## Prime Matrix CRT 行反射更新

新增 `docs/monograph/prime-matrix-row-reflection-period-audit.md` 与脚本 `experiments/prime_matrix_row_reflection_period_audit.py`。已严格证明：`p` 对齐全覆盖行 `r` 在 CRT 行周期 `N=P(p)/p` 内必有镜像全覆盖行 `N-r+1`。同时审计反驳了“由镜像推出短平移周期或整除条件”的猜想；第二周期复现只给出二面体轨道，相邻间隔交替为 `N-2r+1` 与 `2r-1`。若放宽为“相位组合可变但全覆盖现象复现”，`r,2r,2r-1` 仍不是自动现象周期；已知零行样本均不复现。可用条件引理是：若零行集合对平移 `d` 不变且 `r` 是首个零行，则必须有 `gcd(N,d)>=r`。样本 `p=23,r=59` 中 `N mod (2r-1)=39`，且 `r+59=118`、`r+117=176`、`r+118=177` 都不是零行。可用增益是“两端帽排斥”和条件 gcd 限制；该结论可强化 `PDEC-or-SAE`，但不能替代 `QSurv`。

新增 `docs/monograph/prime-matrix-p23-zero-recurrence-audit.md` 与脚本 `experiments/prime_matrix_p23_zero_recurrence_audit.py`。对 `P=23` 完整 CRT 行周期 `N=9699690` 扫描确认：零行总数 `3456`，第 `59` 行在镜像行之前确有 `3454` 次复现，首次复现在第 `2612` 行；但第 `118=2*59` 行不是零行。复现机制是不同 CRT 相位向量重新覆盖 22 个非平凡列，不是短等差周期。最新分层审计显示：固定 `2,3,5,7` 低骨架 `r≡59 (mod 210)` 后镜像前仍有 `324` 个零行，首个为 `6569`；第 `59` 与 `6569` 行同剩 `5,9,15` 三洞，但高素数补洞标签由 `13,17,19` 置换为 `19,13,17`。该结果支持把零行复现视为“低骨架 + 高标签置换”的稀疏相位证书集合，并接入 `PDEC/SAE` 缺陷账本。

新增 `docs/monograph/prime-matrix-short-recurrence-gap-audit.md` 与脚本 `experiments/prime_matrix_short_recurrence_gap_audit.py`。审计确认“任意零行不可能在 `2P` 行内复现”的全局强命题为假：`P=19` 已有最小间隔 `5` 和 `24` 对短复现，`P=23` 有最小间隔 `20` 和 `20` 对短复现。可保留的是边界版本：首零行 `r0` 与末零行跨周期距离为 `2r0-1`，因此“首尾跨周期间隔 >2P-1”等价于“首零行 >P”。该版本是目标的重写而非独立证明出口；下一步硬点应为首端帽/尾端帽的边界相位非覆盖与 CRT 最小代表下界。

新增 `docs/monograph/prime-matrix-boundary-phase-noncoverage-audit.md`、`docs/monograph/prime-matrix-boundary-phase-noncoverage-hard-attack.md` 与脚本 `experiments/prime_matrix_boundary_phase_noncoverage_audit.py`。边界相位非覆盖 `BPN(P)` 已严格写成三种等价形式：前 `P` 行无零行；每个网格短区间 `[xP+1,xP+P-1]` 含素数；每个完整覆盖证书的 CRT 最小代表 `x_S>=P`。扫描到 `P<=199` 均通过，最薄边界行只有 `1` 个幸存素数，显示余量很薄。已加入 Sylvester 大因子弱输入：每个边界行必有某数含 `>P` 大素因子，但仍需排除它同时有小因子。当前唯一核心接口压缩为 `BPN-RM`：边界帽中补掉最后残洞必释放旧覆盖列，即残洞迁移守恒。该接口未闭合前，不能宣称行命题无条件完成。

新增 `docs/monograph/prime-matrix-boundary-residual-migration-audit.md` 与脚本 `experiments/prime_matrix_boundary_residual_migration_audit.py`。该审计修正 `BPN-RM` 表述：局部补洞并不困难，扫描内最薄行常有许多 `y<P` 可补掉旧残洞；真正现象是补洞后残洞迁移到新列。扫描到 `P<=199` 的最薄行未出现 `y<P` 完整覆盖，最小新残洞数为 `2`。但全局 `BPN-RM` 与 `BPN(P)` 几乎同强，不能作为循环证明。下一步非循环目标是构造残洞势函数 `Phi(R)`，证明任何补洞迁移不能使 `Phi` 降到 `0`。

新增 `docs/monograph/prime-matrix-crt-solution-set-geometry-audit.md` 与脚本 `experiments/prime_matrix_crt_solution_set_geometry_audit.py`。已严格分离 CRT 筛层与数值层：行幸存集合满足精确镜像 `R(N-r+1)=P-R(r)`，零行镜像因此是定理；但中区 `P`-rough 合数密集属于数值层，不能直接推出边界帽 `R(r)≠∅`。扫描 `P=13,17,19,23` 验证镜像计数完全成立；边界最薄幸存者自动为素数，中区幸存者可为素数或粗合数。该结论支持把镜像作为两端帽约束使用，但不能替代 `BPN` 势函数或 `GridPrimeGap` 输入。

新增 `docs/monograph/prime-matrix-crt-zero-solution-distribution-audit.md` 与脚本 `experiments/prime_matrix_crt_zero_solution_distribution_audit.py`。该审计把零行集合写成列覆盖集合交的 CRT 方程组，并完整扫描 `P=13,17,19,23`：边界帽 `2<=r<=P` 零行数均为 `0`，首零行分别为 `169,1211,3659,59`；零行镜像严格成立。审计同时发现各周期十等分的平均幸存列数基本相同，说明边界排除不能从“中区粗合数密集”单调推出。当前最小硬点更新为：证明完整覆盖证书最小代表 `>=P`，或给出独立残洞势函数 `Phi_P(R)`。

新增 `docs/monograph/prime-matrix-zero-row-covering-vs-smoothness-audit.md`、`docs/monograph/prime-matrix-early-diagonal-avoidance-hardpoint.md` 与脚本 `experiments/prime_matrix_early_diagonal_avoidance_audit.py` 后，边界帽硬点进一步校正：旧第 `59` 行对应 `P=23,x=58`，不是 `23*59+1` 起点；零行覆盖只要求“至少一个 `<=P` 小素因子”，不能误用连续 `P`-光滑数/Pell 下界。新最窄接口为 `Early-Diagonal-Avoidance`：证明 `1<=x<=p` 时 `U_p(x)=#{1<=k<p:(px+k,M_p)=1}>0`。早期未覆盖点必为素数，故该接口等价于每个 `p` 对齐短区间 `(px,px+p)` 含素数。审计到 `p<=2000` 无早期零行；完全自足证明仍需 `EDA-Dual` 下界证书或接入 `PDEC/SAE` 出口。

新增 `docs/monograph/prime-matrix-first-zero-equivalence-and-diagonal-barrier.md` 与脚本 `experiments/prime_matrix_first_zero_pattern_audit.py` 后，CRT 首个零行规律被写成覆盖证书最小代表元定理：每个完整覆盖证书 `tau` 给出一个 CRT 进程 `x≡r_tau (mod D_tau)`，首零行 `X0(p)=min_tau r_tau^+`。扫描到 `p<=47,x<=200000` 显示 `X0(p)/p` 高度非单调，例如 `p=23` 为 `58`，`p=31` 为 `60794`，`p=41` 为 `170880`。因此规律不是密度单调，而是低骨架加高标签补洞证书的最小 CRT 代表。`X0(p)>p` 等价于所有证书的 `r_tau^+>p`，也等价于 `p` 对齐短区间素数命题；特别包含素数子序列上的 Oppermann 第一半区间。当前证明路径压缩为 `Certificate-MinRep Barrier` 或 `EDA-Dual`。

新增 `docs/monograph/prime-matrix-eda-gap-barrier-and-dual-route.md` 后，`EDA` 的证明边界进一步明确：`X0(p)>p` 至少要求证明 `pi(p^2+p-1)-pi(p^2)>0`，即素数平方后一半区间的 Oppermann 型子命题。任何普通 `N^theta` 素数间隔输入若 `theta>1/2` 都不能直接闭合全部 `p` 对齐窗口。完全自足路线必须走特殊 CRT 对角结构：`EDA-Dual-K` 可变阶 Bonferroni/Selberg 下界、`High-Label-MinRep` 高标签最小代表约束、`Low-Skeleton Defect` 低骨架缺陷和尾项吸收。

新增 `docs/monograph/prime-matrix-eda-dual-bonferroni-hard-attack.md` 与脚本
`experiments/prime_matrix_eda_bonferroni_audit.py`。`EDA-Dual` 已被写成奇数阶
Bonferroni 下界账本：`S_K(p,x)<=U_p(x)`，若 `min_{1<=x<=p}S_K(p,x)>0` 则闭合
`EDA(p)`。五阶有精确身份
`S_5=U_p-\sum_{\omega_p(n)>=6}{\omega_p(n)-1\choose5}`，把剩余硬点压成高重合
尾项控制；选点样本到 `p=5003` 均为正。但固定阶 Bonferroni 有 `log log p` 尺度
变号风险，不能作为全局证明。下一步必须构造可变阶 `EDA-BK/Selberg` 账本，或证明
高重合尾项过大必触发 `PDEC/SAE`。

新增 `docs/monograph/prime-matrix-zero-row-full-crt-diagonal-minrep.md`。该文件从全量
CRT 方程组严写零行条件：每个完整覆盖标签 `tau` 满足同标签列差可被标签素数整除，
于是给出唯一残基 `x≡r_tau (mod D_tau)`，且 `X_0(p)=min_tau r_tau^+`。同时证明
`X_0(p)>p` 等价于所有 `1<=x<=p` 的短区间 `(px,px+p)` 含素数；这是当前首零行
对角屏障的精确审稿形态。该文件不宣称闭合全局，只把剩余固定为 `MinRep/EDA-Dual/LowMod-Tail`
三种等价出口。

新增 `docs/monograph/prime-matrix-eda-bk-endpoint-defect-bridge.md` 与脚本
`experiments/prime_matrix_eda_endpoint_defect_audit.py`。该步证明精确桥接
`S_K=H G_K+E_K`：若奇数阶 `K` 有 `G_K>0` 而某行 `S_K<=0`，则该行满足
`E_K<=-H G_K`，即出现显式负端点锯齿 CRT 缺陷。该桥接不闭合 `EDA`，但把下一步
从“证明所有行正余量”压缩为“选择正主项变量阶并排斥对应端点缺陷”。

新增 `docs/monograph/prime-matrix-eda-bk-lowmod-tail-dichotomy.md`。该步证明正主项奇数阶
`K_*(p)` 总存在：若 `<p` 素数数目为奇数取全阶，否则取全阶减一阶，并用
`V(p)/e_m=prod_{q<p}(q-1)>1` 证明 `G_{K_*}>0`。结合端点桥，任何 EDA 反例都必须进入
`LowMod endpoint CRTDefect` 或 `Tail/Core concentration`。这不闭合 EDA，但把剩余
精确压成两个已有矛盾场出口的排斥义务。

新增 `docs/monograph/prime-matrix-zero-row-spacing-gradient-audit.md` 与脚本 `experiments/prime_matrix_zero_row_spacing_gradient_audit.py`。该审计确认：若 `r0` 为首个零行，则镜像给出首尾跨周期间隔 `2r0-1`；样本 `P=13,17,19,23` 的该间隔分别为 `337,2421,7317,117`，均大于 `2P`。但该命题等价于 `r0>P`，也就是 `BPN(P)` 本身；同时全局“中心附近零行更密、越靠边界越稀”的十等分梯度不成立。状态更新：边界复现距离可作为 `BPN-Defect` 的目标形式，但不能作为独立证明输入。

新增 `docs/monograph/prime-matrix-bpn-defect-bonferroni-audit.md` 与脚本 `experiments/prime_matrix_bpn_defect_bonferroni_audit.py`。边界帽路线当前最小硬点更新为 `BPN-B5`：证明五阶 Bonferroni 下界 `S5(r)>0`。审计显示三阶下界在 `P<=199` 已有失败，但五阶下界在 `P<=199` 的全部边界行未失败，最坏样本 `P=199` 仍有最小 `S5=12`。这不是无条件闭合；下一步必须逐项证明 `I1-I2+I3-I4+I5<P-1`，或在失败时转入带权筛与 `CRTDefect/Tail-anchor` 出口。

`BPN-B5` 已进一步改写为逐点恒等式：五阶下界等于边界行内素数数目减去含至少六个 `<P` 小素因子的高重合数惩罚。选点扫描 `P=251,503,1009,2003,5003` 均保持正余量；`P=5003` 最薄样本为素数型点 `272`、高重惩罚 `95`、余量 `177`。下一步最小证明义务更新为：控制高重小素因子惩罚，或证明其过大触发小核心乘积过密/`Tail-anchor/CRTDefect`。

新增 `docs/monograph/prime-matrix-bpn-high-omega-core-audit.md` 与脚本 `experiments/prime_matrix_bpn_high_omega_core_audit.py`。该审计将高重惩罚按六小素核心 `core6` 分桶；样本支持二分出口：小/中 `core6` 过密给出固定小核心倍数集中，大 `core6≈n` 过密给出尾锚/端点集中。当前最小接口命名为 `Core6-Density-or-TailAnchor`，仍需证明该二分导致可吸收上界或 CRT/Tail-anchor 缺陷。

新增 `docs/monograph/prime-matrix-bpn-bonferroni-order-risk-audit.md` 与脚本 `experiments/prime_matrix_bpn_bonferroni_order_risk_audit.py`。审计确认固定五阶 `S5` 不能作为全局终局路线：任意固定奇阶截断在 `log log(P^2)` 尺度上有渐近变号风险。状态更新：`BPN-B5/Core6` 降级为低范围证据和缺陷定位工具；当前最小全局接口升级为 `BPN-BK/Selberg`，即可变阶 Bonferroni/Brun 或 Selberg/Brun 非负筛权，并以 `CoreK-Density-or-TailAnchor` 作为失败出口。

新增 `docs/monograph/prime-matrix-bpn-bk-weight-model-audit.md`、`docs/monograph/prime-matrix-bpn-bk-selberg-route.md` 与脚本 `experiments/prime_matrix_bpn_bk_weight_model_audit.py`。审计进一步确认：可变阶 BK 能修正固定阶模型变号，但普通 Selberg/Brun 下界筛在边界行 `H=P,z=P` 只有 `s<=1`，不能单独给出正筛余；正性仍需额外的方阵/CRT 缺陷排斥。当前最小接口因此精确化为 `BK-DEC + CoreK-Density/TailAnchor` 二分：若 `S_K(r)<=0`，必须导出端点 sawtooth 缺陷或高重核心桶过密，并接入 `Directed CRTDefect/Tail-anchor/PDEC-or-SAE`。

新增 `docs/monograph/prime-matrix-bpn-bk-dec-bridge-proof.md`。其中 `BK-DEC` 桥接已严格证明：边界零行加尾项预算 `|R_{K,>D}|<=T_{K,D}` 与正主项余量 `(P-1)V_{K,D}>T_{K,D}`，推出负向端点项 `E_{K,D}(r)<=-((P-1)V_{K,D}-T_{K,D})`；再经低模分块鸽巢推出 `Directed Endpoint CRTDefect`。剩余不再是“BK-DEC 能否成缺陷”，而是两项：证明可用尾项预算，以及排斥该有向端点缺陷（`PDEC-or-SAE`）。

新增 `docs/monograph/prime-matrix-bpn-bk-tail-core-dichotomy.md`。尾项预算接口已被改写为严格二分：边界零行若不触发 `BK-DEC`，则尾关联质量 `U_{K,D}(r)=#{(n,d):n∈I_r,d|n,d|M_{<P},omega(d)<=K,d>D}` 必超过预算；任意 dyadic/相位分块随即给出 `TailCoreBucket/CoreK-Density` 过密证书。当前 BPN-BK 剩余硬点因此精确为两个出口排斥：`Directed Endpoint CRTDefect` 与 `TailCoreBucket/CoreK-Density`。

新增 `docs/monograph/prime-matrix-bpn-tailcore-corridor-reduction.md` 与 `docs/monograph/prime-matrix-bpn-tailanchor-persistence-dichotomy.md`。前者把 `TailCoreBucket/CoreK-Density` 严格归约为 `Tail-anchor concentration` 或 `Distributed corridor saturation`；后者又把 `Tail-anchor concentration` 二分为 `SAE-anchor` 或 `Persistent Tail-anchor defect`，后者经低模 Fourier 展开进入 `Directed CRTDefect`。因此尾锚分支已并回 `PDEC-or-SAE`，当前剩余最小硬点为：`PDEC-or-SAE` 排斥，以及 `Distributed corridor saturation` 的 Selberg/CRTDefect 排斥。

新增 `docs/monograph/prime-matrix-bpn-distributed-corridor-saturation-reduction.md`。分布式走廊饱和已严格拆为 `High-overlap fixed-core defect` 或 `Colored disjoint-corridor budget violation`：前者由固定核心复用过多进入尾锚/低模相位集中，归并到 `PDEC-or-SAE`；后者通过区间图着色化为不相交走廊并集上的核心筛预算，若预算失败则进入 low-mod CRTDefect 或光滑核心包络义务。当前剩余进一步压缩为：`PDEC-or-SAE` 排斥与 `Colored disjoint-corridor core-sieve budget/low-mod CRTDefect`。

新增 `docs/monograph/prime-matrix-bpn-colored-corridor-core-sieve-budget.md`。着色不相交走廊预算已严写为有限 Rankin smooth-core 账本：`N_K(C)<=(2D0)^s sum_{d in C} sigma_K(d)/d^s`。这一步校正了不能把 rough-number Selberg 下界误用于 smooth squarefree core 计数的问题。当前剩余进一步变为：`PDEC-or-SAE` 排斥、有限 Rankin smooth-core ledger 常数闭合、以及 low-mod core CRTDefect 排斥。

新增脚本 `experiments/prime_matrix_bpn_rankin_ledger_certificate_audit.py` 与报告 `docs/monograph/prime-matrix-bpn-rankin-ledger-certificate-audit.md`、`docs/monograph/prime-matrix-bpn-rankin-ledger-certificate-audit.json`。有限 Rankin 账本现有可执行证书格式：输入 `P,K,intervals,phase_moduli`，输出精确 smooth-core 数、Rankin 最优网格与低模相位尖峰。默认合成样本 `P=1009,K=9`、总宽度 `256` 中精确 core 数为 `39`，低模 `210` 的最大相位比均匀模型约 `16.153846`。这说明若正式证书常数超预算，low-mod core CRTDefect 是实际可抽取的出口。

新增 `docs/monograph/prime-matrix-bpn-lowmod-core-crtdefect-bridge.md`。low-mod core CRTDefect 已严格桥接到有限 Fourier/CRT 缺陷：若 residue 尖峰 `N_b-N/Q>=eta`，则存在非平凡角色 `h` 使 `|sum_d sigma_K(d)e_Q(hd)|>=eta`。持续出现进入 `PDEC`，孤立出现进入 `SAE-core`。因此 low-mod core CRTDefect 不再是独立剩余出口，当前 BPN-BK 剩余压缩为 `PDEC-or-SAE` 排斥与 finite Rankin smooth-core ledger 常数闭合。

新增 `docs/monograph/prime-matrix-bpn-unified-pdec-sae-dichotomy.md`。endpoint sawtooth 与 smooth-core 两类低模缺陷已统一为同一测试函数框架：命名低模缺陷必二分为 `Persistent Fourier defect` 或 `Sparse single-window escape`。Persistent 分支经 Parseval/Cauchy 给出坏窗指示函数的非零频率；Sparse 分支就是有限 SAE 义务。当前最终剩余更精确写为：`PDEC exclusion`、`SAE local escape exclusion`、finite Rankin smooth-core ledger constants。

新增 `docs/monograph/prime-matrix-bpn-rankin-ledger-acceptance-theorem.md`，并更新 Rankin 证书脚本输出 `allowed_budget/rankin_budget_pass/exact_budget_pass`。有限 Rankin 常数项现已变成明确证书验收义务：每个颜色类若满足 `Rankin ledger <= allowed budget` 即闭合；不通过者必须触发 low-mod core CRTDefect 或继续细分。当前最终剩余更新为：`PDEC exclusion`、`SAE local escape exclusion`、以及正式着色走廊 Rankin certificates 全部通过或失败者进入 PDEC/SAE。

## Prime Matrix 逆向零行二分更新

新增 `docs/monograph/prime-matrix-reverse-zero-row-dichotomy.md`、`docs/monograph/prime-matrix-reverse-zero-row-dichotomy-audit.md` 与脚本 `experiments/prime_matrix_reverse_zero_row_dichotomy_audit.py`。已严格证明：若 `2<=s<q` 的 `q` 零行存在，则整条 `q` 行已被旧 `p`-筛覆盖；随后按起点相位 `a_s=(s-1)q mod p` 二分为“包含完整 `p` 对齐零行”或“只形成跨相邻 `p` 行的缝合零窗”。因此直接反推 `p` 方阵零行只在第一支成立；第二支必须由 `SeamSafe/ASB/PDEC-or-SAE` 排除。`p<=2000` 几何审计中核心区直接支比例约 `0.00616`，缝合支约 `0.99384`。

## Prime Matrix 递推升级路线

新增 `docs/monograph/prime-matrix-recursive-lift-audit.md`。审查结论：用户提出的“旧核心素数在升级到下一素数筛后不会消失”是正确的；但 `p×p` 行命题不能直接传递到 `q×q`，因为 `q=p+g` 的行边界相对 `p` 行边界漂移。`q` 行包含完整 `p` 行当且仅当 `(-(s-1)q mod p)<=g`，当素数间隙 `g` 很小时，完整行传递比例约为 `(g+1)/p`，多数旧核心 `q` 行是跨两个 `p` 行的尾段+头段。新增 `docs/monograph/prime-matrix-seam-endpoint-audit.md` 将 `Seam(p,q)` 进一步压缩为端点屏障 `SEB(p,q)`：若旧相邻 `p` 行的末端无素数段 `sigma_t` 与下一行首端无素数段 `pi_{t+1}` 满足 `max_t(sigma_t+pi_{t+1})<q`，则旧核心所有新 `q` 行缝合窗口含素数。`p<=10000` 样本中实测 seam 空窗为 `0`，`SEB` 证书失败为 `0`。新增 `docs/monograph/prime-matrix-seb-unconditionality-audit.md` 进一步指出：全局 `SEB` 接近强素数间隙输入 `G(p^2)<=q`，不宜作为当前无条件化最小目标；实际应证明只检查 `q` 行漂移残基的 `ASB(p,q)`。新增 `docs/monograph/prime-matrix-asb-pressure-audit.md` 显示 `p<=10000` 的实际采样 ASB 窗口数为 `5706402`，失败为 `0`。新增 `docs/monograph/prime-matrix-asb-hard-attack.md` 将 `ASB-Fail` 压缩为相对高素点覆盖不等式 `ASB-RHC`。新增 `docs/monograph/prime-matrix-asb-rhc-alpha-sweep.md` 进一步证明该点覆盖不等式等价于粗剩余素数比例下界 `RPD: |R_z(J)∩P|>=eta|R_z(J)|`；`p<=2000`、后排 `25%` 样本中最优 `alpha=0.43` 的最坏粗剩余素数比为 `0.1875`。新增 `docs/monograph/prime-matrix-rpd-failure-structure.md` 显示最坏 `40` 个窗口中半素数占粗合数比例约 `0.858322`。新增 `docs/monograph/prime-matrix-semiprime-anchor-projection.md` 将半素数投影分解为最小因子锚层：总半素数 `1248`，总锚容量 `10785`，总体容量效率 `0.115716`，高锚层 `[0.90,1.01)` 效率最高为 `0.613707`。新增 `docs/monograph/prime-matrix-anchor-cofactor-interval-audit.md` 将锚层半素数精确改写为互补素数短区间计数；最坏 `40` 窗口共有 `1647` 个互补区间、整数容量 `7086`、素互补因子 `1248`，总素密度 `0.176122`，单窗最高半素数/粗合数比例可达 `1.000000`。新增 `docs/monograph/prime-matrix-mge3-budget-audit.md` 将 `M_{\ge3}` 精确改写为低锚复合互补因子恒等式；同批窗口中 `M_{\ge3}=206`，占粗合数 `0.141678`，恒等式校验差为 `0`。新增 `docs/monograph/prime-matrix-mge3-second-anchor-audit.md` 继续分解为第二锚粗尾恒等式；第二锚计数 `206`、校验差 `0`、整数容量 `1012`、容量效率 `0.203557`，尾因子为素数比例 `0.980583`。新增 `docs/monograph/prime-matrix-mge3-tail-envelope-audit.md` 给出第二锚 Mertens 包络：包络 `165.810608`，所需全局放大常数 `1.242381`，最大层级常数 `1.700839`，最高窗口尖峰 `3.400694`。新增 `docs/monograph/prime-matrix-tail-spike-localization-audit.md` 将局部尖峰定位到 singleton-prime corridor：singleton 粗尾 `182`，其中素尾 `181`、粗合尾 `1`，尖峰等价于 `ab` 落入单点 `d` 给出的双曲走廊。新增 `docs/monograph/prime-matrix-singleton-corridor-bound-audit.md` 给出走廊上界账本：唯一走廊 `175`，宽度总和 `542`，合法 semiprime 对数 `181`，semiprime/宽度 `0.333948`，宽度 `>=2` 的 semiprime/`Vz` 为 `1.388255`，混合所需常数 `1.299083`。新增 `docs/monograph/prime-matrix-singleton-corridor-overlap-audit.md` 证明样本中同窗口走廊不重叠：并集宽度 `542`、重叠冗余 `0`、最大重叠度 `1`。新增 `docs/monograph/prime-matrix-singleton-corridor-closure-lemma.md` 严写确定引理：singleton 子问题严格归约为不相交走廊并集上的标准上筛，或低模端点缺陷出口。递推路线若要成立，仍必须证明素互补因子短区间上界、聚合 Mertens 包络、Annulus 和异常出口排斥。

新增 `docs/monograph/prime-matrix-rpd-first-anchor-identity.md` 和 `docs/monograph/prime-matrix-asb-rpd-weighted-sieve-kernel.md` 后，上述“素互补因子短区间上界”和“聚合 Mertens 包络”已被更强地统一压缩为第一锚粗互补因子恒等式 `FAC`。半素数和 `M_{\ge3}` 不再分开加预算；全部粗合数由第一锚加权 rough cofactor 一次计数。当前剩余义务更新为数值化第一锚同权预算、排斥加权低模端点缺陷出口，并证明 `Annulus(p,q)`。

新增 `docs/monograph/prime-matrix-rpd-fac-budget-audit.md` 后，第一锚模型预算已经完成首轮数值化：全局所需常数 `1.352236`，但逐窗口最大所需常数 `1.695703` 大于 `eta=0.10` 的逐窗口最小允许常数 `1.570917`。因此状态更新为：全局平均有余量，裸单一常数不够；剩余义务是分层/端点修正 FAC-Selberg 预算，或从超预算尖峰中抽取低模端点缺陷出口。

新增 `docs/monograph/prime-matrix-rpd-fac-lowmod-defect-audit.md` 后，低模端点缺陷出口已被具体化为 `D_T` 账本。最尖峰窗口在 `T=17` 已捕获 `90.9089%` 的最终 FAC 缺陷；全部 `40` 个压力窗口在 `T=101` 的最小捕获率为 `80.4688%`。当前唯一窄接口是证明大的 `D_T` 必触发有向 CRT 缺陷或 Tail-anchor/OSPC 出口。

新增 `docs/monograph/prime-matrix-square-annulus-lift-lemma.md` 后，`Annulus` 义务同步缩窄：若 `n∈(p^2,q^2]` 避开所有 `<=p` 的素因子，则 `n` 是素数或 `q^2`；`pq` 已被旧素数 `p` 筛掉，不是新增非冗余点。审计 `docs/monograph/prime-matrix-square-annulus-sieve-lift-audit.md` 在 `max_p=2000` 下给出壳层幸存合数例外失败数 `0`、完整壳层行空段数 `0`，但完整壳层行最小旧筛幸存者数只有 `1`。剩余义务是证明相关壳层 `q` 行段存在旧筛幸存者且不只含 `q^2`；该非空性不能由粗平均常数替代。

新增 `docs/monograph/prime-matrix-annulus-rough-nonempty-hard-attack.md` 后，壳层非空失败被统一为负低模端点缺陷；ASB/RPD 的 FAC 尖峰是正低模端点缺陷。当前递推链最短闭合目标变为证明 `Signed-LowMod-Bridge`：任意足够大的有符号低模端点异常都必须触发有向 `CRTDefect/Tail-anchor/OSPC`。

新增 `docs/monograph/prime-matrix-signed-lowmod-bridge-hard-attack.md` 后，`Signed-LowMod-Bridge` 已精确化为 Möbius 端点锯齿恒等式。已证明的是 `large D_T => large low-mod endpoint projection`；仍需证明 `SESE-low`，即大端点锯齿投影在 `q` 行单位旋转与 CRT 刚性下必然触发 `CRTDefect/Tail-anchor/OSPC`。

新增 `docs/monograph/prime-matrix-directed-endpoint-crtdefect-bridge.md`、`docs/monograph/prime-matrix-dec-ospc-exclusion-hardpoint.md`、`docs/monograph/prime-matrix-zero-row-crt-audit.md` 与 `docs/monograph/prime-matrix-zero-row-delay-recursive-lemma.md` 后，递推支线进一步澄清：大端点投影已能进入 `Directed Endpoint CRTDefect/OSPC*`；但单点 DEC 不能自动矛盾。零行审计在 `p<=2000` 内未发现 `q×q` 旧筛 `q` 行失败，且 `p<=200` 中找到的 `p` 对齐零行均晚于 `ceil(q^2/p)`；严格引理为 `QSurv(p,q)=>Row(q)`。剩余义务仍是证明 `QSurv` 失败必由 `PDEC-or-SAE` 排除。

新增 `docs/monograph/prime-matrix-qsurv-gap-structure-audit.md` 与 `docs/monograph/prime-matrix-qsurv-grid-gap-hardpoint.md` 后，`QSurv` 的最终硬点被精确化为 `q` 网格素数荒漠排斥。实验到 `p<=5000` 无零 `q` 行，但最薄行可只有一个素数；还出现普通最大素数间隙 `>q` 而不造成空网格行的样本。因此主线不能改攻普通素数间隙上界，必须证明“素数间隙覆盖完整 `q` 网格单元”不可能，或它触发 `PDEC-or-SAE`。

新增 `docs/monograph/prime-matrix-recursive-peeling-zero-row-hardpoint.md`、
`docs/monograph/prime-matrix-recursive-peeling-zero-row-audit.md` 与脚本
`experiments/prime_matrix_recursive_peeling_zero_row_audit.py` 后，用户提出的递归剥离路线已定式化：
`p`-零窗剥去顶层素数后，幸存者只能来自顶层素数倍数，故第一层是带至多 `1` 或 `2` 个复活点的
punctured zero window，而不是自动下层零行。已知 `5` 个首零行样本中，一步剥离后仍零的有 `2`
个，包含完整下层对齐零行的只有 `1` 个，连续零行对为 `0`。因此该路线的下一硬点不是“推出连续零行”，
而是 `RPZ-Absorption=>ColumnCRT/TailAnchor`：证明复活点被稳定吸收必触发列/尾锚/低模缺陷。

新增 `docs/monograph/prime-matrix-adjacent-shell-recursive-descent-route.md`、
`docs/monograph/prime-matrix-adjacent-shell-descent-ledger.md/json` 与脚本
`experiments/prime_matrix_adjacent_shell_descent_ledger.py` 后，相邻壳层事实被强化：`p<q`
相邻时，`q^2` 内旧 `p`-筛唯一合数幸存者是 `q^2`，有限账本 `p<=2000` 无单点失败。
因此 `q^2` 内零行确实先降为旧 `p`-筛零窗；剩余无损二分为完整 `p` 行或 seam guard。
当前递归路线最小硬点更新为 `SeamGuard-Elimination`：排除两个 guard 持续吸收，否则送入
`SAE/PDEC/ColumnCRT`。

新增 `docs/monograph/prime-matrix-scaled-peeling-halfwidth-audit.md` 与脚本
`experiments/prime_matrix_scaled_peeling_halfwidth_audit.py` 后，进一步核查缩放行号与半宽素数版本：
`nP/p` 只是高度近似，完整包含下层对齐零行需要额外相位条件；同批样本中缩放后含完整前一素数零行的记录
只有 `1/5`。取约半宽素数后，虽然 `P/h>2`，连续半宽零行段最大长度仍为 `0`，因为剥到半宽层会复活
最小素因子在 `(h,P]` 的粗互补因子点。该结果进一步支持把下一硬点定为复活点吸收缺陷，而不是镜像连续零行矛盾。

新增 `docs/monograph/prime-matrix-seam-multilevel-descent-route.md`、
`docs/monograph/prime-matrix-seam-multilevel-descent-audit.md/json`、
`docs/monograph/prime-matrix-seam-multilevel-descent-audit-p2000-sample.md/json` 与脚本
`experiments/prime_matrix_seam_multilevel_descent_audit.py` 后，seam guard 路线被进一步细化：
若 seam 区间在旧 `p`-筛下为零，降到 `h<p` 后复活点精确为
`{n∈I:P^-(n)>h, P^-(n)<=p}` 加终端 `q^2` 穿孔；若某条完整 `h` 行避开该复活集，则得到强制
`h` 零行。全量 `p<=500` 的 `21339` 条 seam 与 `p<=2000,row_stride=25` 的 `11488`
条抽样 seam 均在某层出现强制零行，阻断数 `0`。但该结论仍是条件账本：需证明全局
`SMD-Global Inequality`，或将持久复活点阻断送入 `SAE/PDEC/ColumnCRT`。

新增 `docs/monograph/prime-matrix-seam-tail-mirror-descent-route.md`、
`docs/monograph/prime-matrix-seam-tail-mirror-descent-audit.md/json`、
`docs/monograph/prime-matrix-seam-tail-mirror-descent-audit-p2000-sample.md/json` 与脚本
`experiments/prime_matrix_seam_tail_mirror_descent_audit.py` 后，用户提出的“强制零行经 CRT 尾边界镜像
落回小阶方阵”被精确为行相位条件：对 `h` 层行周期 `N_h`，强制零行 `R` 若满足
`rho=((R-1) mod N_h)+1<=h` 或 `N_h-rho+1<=h`，则周期或尾镜像给出 `h×h` 方阵内条件零行。
全量 `p<=500` 与抽样 `p<=2000,row_stride=25` 均为 `100%` 命中，未命中数 `0`。当前最小硬点
进一步压缩为 `TailMirror-SMD` 全局证明，或将非命中持久相位送入 `SAE/PDEC/ColumnCRT`。

新增 `docs/monograph/prime-matrix-total-zero-row-recursive-descent-route.md`、
`docs/monograph/prime-matrix-total-zero-row-descent-audit.md/json`、
`docs/monograph/prime-matrix-total-zero-row-descent-audit-p2000-sample.md/json` 与脚本
`experiments/prime_matrix_total_zero_row_descent_audit.py` 后，aligned、seam、末行 `q^2` 穿孔、
周期性和尾镜像已统一为总下降模型。全量 `p<=500` 检查 `21936` 条非第一 `q` 行，含
`597` 条 aligned 与 `21339` 条 seam，全部强制命中某个小阶方阵零行；`p<=2000,row_stride=25`
抽样 `11583` 条也全部命中，未闭合 `0`。当前总硬点精确更新为 `TotalDescent-TM`：
证明任意真实高阶零行都存在满足头部/尾镜像相位条件的小阶强制零行，或证明非命中相位触发
`SAE/PDEC/ColumnCRT`。

新增 `docs/monograph/prime-matrix-total-descent-h3-margin-route.md`、
`docs/monograph/prime-matrix-total-descent-h3-margin-audit.md/json` 与脚本
`experiments/prime_matrix_total_descent_h3_margin_audit.py` 后，`TotalDescent-TM` 被进一步压到
固定 `h=3` 的六轮余量接口。对任意相邻 `p<q` 和 `2<=s<=q`，令
`I=[(s-1)q+1,sq]`，完整 3 行的唯一六轮候选为 `c_R`。若
`P^-(c_R)>p`，则 `c_R` 是旧 `p`-筛零窗中的幸存点，反设直接矛盾；若
`5<=P^-(c_R)<=p`，该完整 3 行被复活点阻断。全量 `p<=5000` 审计检查
`1552462` 条 `q` 行，`h=3` 余量全部为正，最小余量为 `1`。正式稿剩余随之收窄为
`H3-SixWheel-Roughness`：证明 `[5,p]` 素因子不能覆盖每个 `q` 行窗口中的全部六轮候选，
或证明全覆盖相位必触发 `SAE/PDEC/ColumnCRT`。该接口仍不能由有限账本或普通素数间隙定理
直接替代。

新增 `docs/monograph/prime-matrix-h3-sixwheel-hard-attack.md` 后，上述接口的强度边界被明确：
`H3-SWR` 推出对应 `q` 行含素数，且处于 `u=2` 的线性筛临界障碍，不能靠普通短区间素数定理闭合。
`H3` 失败被精确写成 first-factor partition
`A_s=sqcup_{5<=ell<=p} A_{s,ell}`，其中 `n=ell m` 落入长度 `q/ell` 的 `ell`-rough cofactor
窗口。下一最小定理是 `H3 Full-Blocking Defect`：全阻断必须出现 first-factor 高负载、分布式
低模 PDEC 能量、稀疏端点 SAE 或持久 ColumnCRT 位移。

新增 `docs/monograph/prime-matrix-h3-full-blocking-defect-audit.md/json` 与脚本
`experiments/prime_matrix_h3_full_blocking_defect_audit.py` 后，数据支撑进一步明确：在 `p<=5000`
的 `1552462` 条 `q` 行中，`margin<=20` 的近失败窗口只有 `4015` 个，最高 `p=317`、最高
`q=331`；聚合 first-factor 负载以 `5:36548, 7:20953, 11:11564, 13:8858` 为主阶梯。
这支持下一步专攻“低层小首因子骨架过载或多标签低模能量”的二分，而不是继续扩展有限模板。

新增 `docs/monograph/prime-matrix-h3-small-factor-envelope-route.md`、
`docs/monograph/prime-matrix-h3-small-factor-envelope-audit.md/json` 与脚本
`experiments/prime_matrix_h3_small_factor_envelope_audit.py` 后，小首因子分支有了确定性包络二分：
对 cutoff `y`，若小骨架覆盖为 `C_y`、剩余为 `R_y`，则全阻断至少需要
`ceil(R_y/(floor(q/ell_+(y))+1))` 个 `>y` 中尾标签，除非 `C_y` 已达到 Tail/PDEC 过载。
近失败账本中 cutoff `31` 与 `43` 的最大强制中尾标签数分别为 `7` 与 `9`。剩余义务是证明
`SmallSkeletonOverload=>Tail/PDEC` 或 `ManyLabel=>H3-PDEC` 的阈值比较。

新增 `docs/monograph/prime-matrix-h3-global-scaling-law-route.md`、
`docs/monograph/prime-matrix-h3-margin-growth-audit.md/json` 与脚本
`experiments/prime_matrix_h3_margin_growth_audit.py` 后，H3 数据洞察被提升为全局尺度规律：
`p<=5000` 中从 `p=331` 起所有素数层最小余量均 `>=21`；bucket 平均余量与
`#A_s prod_{5<=ell<=p}(1-1/ell)` 同阶，随 `q/log q` 增长。全局反例若存在，必须把这个增长尺度
压为 `0`，因此必定表现为小骨架 Tail/PDEC 过载、多中尾标签 PDEC 能量或端点 SAE/ColumnCRT。

新增 `docs/monograph/prime-matrix-h3-universal-scaling-inequality.md`、
`docs/monograph/prime-matrix-h3-scaling-formula-audit.md/json` 与脚本
`experiments/prime_matrix_h3_scaling_formula_audit.py` 后，通用候选不等式被常数化：有限账本支持
`M_H3(p,s)>=0.30*q/log q` 从 `p=113` 起成立，`0.40*q/log q` 从 `p=2011` 起成立。正式证明仍需
缺陷版：若低于 `c*q/log q`，则触发 `SmallSkeletonOverload/ManyLabel-PDEC/Endpoint-SAE-ColumnCRT`。

新增 `docs/monograph/prime-matrix-h3-global-tail-energy-lemma.md` 后，缺陷版的组合核心已升级为
全局无限尺度的确定性二分：对任意相邻 `p<q`、任意 `2<=s<=q`、任意 cutoff `y`、目标 `B`、
能量阈值 `L`，若 `M_H3(p,s)<B`，则
`C_y>#A_s-B-2L` 或存在 `d>=2(floor(q/ell_+(y))+1)` 使尾标签低模能量 `E_y(d)>L`。
代入 `B=c*q/log q`、`L=lambda*q/log q` 即得到全局通用尺度公式。当前状态因此不是“已证
`M_H3>=c*q/log q`”，而是“低于该尺度必进入两个出口”：`SmallSkeletonOverload=>Tail/PDEC`
或 `TailEnergy=>H3-PDEC/ColumnCRT`。

新增 `docs/monograph/prime-matrix-h3-small-skeleton-pdec-bridge.md` 后，第一出口已有确定性桥接：
小骨架过载 `C_y>#A_s-B-2L` 等价于 `y`-rough 剩余 `R_y<B+2L`，从而强制
`D_y=V_y-R_y>V_y-B-2L`。取 `V_y>=(c+2lambda+eta)q/log q` 时得到
`D_y>eta*q/log q`。因此 `SmallSkeletonOverload` 已送入 PDEC 缺陷；未闭合的是 PDEC 缺陷排斥。

新增 `docs/monograph/prime-matrix-h3-tail-energy-fourier-bridge.md` 与
`docs/monograph/prime-matrix-h3-unified-defect-criterion.md` 后，第二出口也已精确桥接：
`E_y(d)>L` 等价于尾标签非零 Fourier 能量 `F_y(d)>dL`。合成定理为：
若 `D_y<=V_y-B-2L` 且 `F_y(d)<=dL`，则 `M_H3(p,s)>=B`。这已经是全局无限尺度的完整
条件闭合判据；未完成的是统一缺陷排斥估计 `D_y` 与 `F_y(d)` 的无条件证明。

新增 `docs/monograph/prime-matrix-h3-first-row-scale-bridge.md` 后，`q/log q` 尺度不再只是数据规律：
由素数定理，方阵第一行素数数目 `Pi_1(q)=pi(q)~q/log q`；由相邻壳层单点性与 PNT，
H3 行平均满足 `avg_s M_H3(p,s)~q/(2log q)~Pi_1(q)/2`。这说明 H3 余量是第一行素数尺度在
`q^2` 平方壳层上的半密度投影。该桥接证明全局平均尺度，不替代逐行统一缺陷排斥。

新增 `docs/monograph/prime-matrix-h3-pointwise-closure-boundary.md` 后，审稿边界进一步明确：
平均尺度桥已严格证明，但逐行闭合等价于点态尺度转移
`M_H3(p,s)>=kappa*pi(q)` 或等价的统一缺陷排斥。不能使用
`avg_s M_H3~pi(q)/2` 直接推出每行 `M_H3>0`。

新增 `docs/monograph/prime-matrix-h3-square-root-short-interval-barrier.md` 后，H3 逐行闭合被定位为
`x≈q^2`、长度 `sqrt x` 的对齐短区间素数下界。普通 PNT、RH 型误差和已知无条件短区间输入
不能直接推出该结论；必须证明 `D_y/F_y` 低模缺陷排斥。

新增 `docs/monograph/prime-matrix-h3-square-root-defect-exclusion-hard-attack.md` 后，唯一闭合目标已
继续内攻：`D_y` 分支可由一维区间筛基本引理在小筛层控制；自然低模下 `F_y/d` 与尾标签总数
`T_y` 常数等价。因此真正硬核是排斥尾标签/双粗点作为整行精确补洞器，而不是再证明平均尺度。

新增 `docs/monograph/prime-matrix-h3-tail-filler-rigidity-hardcore.md` 后，尾补洞硬核已有局部刚性：
相邻和二步候选的大因子族必须完全互斥，同一尾标签复用间距至少 `y/4`，短直径块消耗至少
`2K` 个互异大素因子。剩余是把这些局部短差值单元全局化为 ColumnCRT、端点相位或互补商容量矛盾。

新增 `docs/monograph/prime-matrix-h3-tail-filler-global-chain-capacity.md` 后，全局化接口已被压成
相邻边容量和三连端点容量。若一个连续尾补洞块 `B` 被拼满，则必有
`EdgeCap(B;y)=|B|-1` 且 `TriCap(B;y)=|B|-2`；在 `y>sqrt(q+6)` 时每个有序标签对在一行内
最多贡献一次，在 `y>q^(2/3)` 时尾点全部半素数化。因此当前唯一剩余不是再找平均量级，
而是证明 `EdgeCap<|B|-1` 或 `TriCap<|B|-2`，或把满容量强制送入
`PDEC/ColumnCRT/endpoint/cofactor` 缺陷。

新增 `docs/monograph/prime-matrix-h3-tail-edge-selberg-exclusion.md` 后，宏观满尾链分支已有
二维上筛排斥：若 `3<=y<=q^theta`，任意满尾补洞连续块满足
`|B|<=2+A_*(theta)(q+6)/(log y)^2`。因此整行 `~q/3` 个 H3 候选全由尾标签/双粗点补洞，
在无限尺度上被排除。剩余最窄接口转为：一般混合坏行只能由小骨架把尾点切成许多短块；
必须证明这种高频切割触发 `D_y/PDEC`，或短块相位集中触发 `ColumnCRT/endpoint/cofactor`。

新增 `docs/monograph/prime-matrix-h3-shortblock-singleton-barrier.md` 后，上述接口被进一步校正：
尾块分解有恒等式 `T=J+E`，其中 `T` 是尾点数、`J` 是尾块数、`E` 是内部相邻尾边数。
二维上筛只给 `E=O(q/log^2 y)`，所以 `T~q/log y` 时绝大多数尾块是单点块。
“小骨架切割很多”本身不是 PDEC 缺陷，因为小骨架自然为 `q` 级。当前唯一剩余硬核应写成
`Singleton Tail Exclusion`：大量孤立尾点若全部为双粗合数，则其尾标签与左右小骨架夹逼相位
必须触发 `PDEC/ColumnCRT/endpoint/cofactor`。

新增 `docs/monograph/prime-matrix-h3-singleton-clamp-defect-criterion.md` 后，孤立尾点夹逼相位已
CRT 容量化：固定左右小标签和差值给唯一低模类，叠加尾标签 `ell>y` 后给模
`ell*lcm(r_-,r_+)` 的唯一类，单元容量至多
`1+floor((q+O(1))/(ell*lcm(r_-,r_+)))`。因此大量孤立尾点必进入尾标签集中、夹逼低模集中
或分散容量三分支。当前未闭合的是分散容量分支：它仍能在自然量级容纳 `q/log y` 个孤立双粗点，
需要有符号半素数过剩排斥或路由到 `PDEC/ColumnCRT/endpoint/cofactor`。

新增 `docs/monograph/prime-matrix-h3-distributed-singleton-bilinear-obstruction.md` 后，分散容量
分支被双线性化：在 `y>q^(2/3)` 下孤立尾点必为 `a=ell*m`，其中 `m` 为素数；夹逼类
`rho(c) mod R(c)` 等价于互补商移动同余 `m≡ell^{-1}rho(c) mod R(c)`。因此分散半素数过剩
等价于短互补商区间族中的有符号素数偏差。当前最终硬输入是
`H3 Distributed Singleton Bilinear Exclusion`：无集中时该有符号双线性误差必须为
`O(q/log^2 y)`，或触发 `PDEC/ColumnCRT/endpoint/cofactor`。

新增 `docs/monograph/prime-matrix-h3-bilinear-large-sieve-defect-bridge.md` 后，上述双线性误差
已被非零频率化：对夹逼模 `R(c)` 展开角色，移动同余给相位
`\chi(ell^{-1}rho(c))=\chi(rho(c))*conj(chi(ell))`。因此若误差仍为 `q/log y` 级，
必存在非主角色上的双线性频率缺陷。普通大筛在短互补商窗口上仍不足；最后输入应写成
`H3-DSB-LS/KLS`：证明该频率缺陷由短窗口 dispersion/Kloosterman 抵消排除，或路由到
`PDEC/ColumnCRT/cofactor`。

新增 `docs/monograph/prime-matrix-h3-dsb-kloosterman-window-reduction.md` 后，该频率缺陷已
加性 Kloosterman 化：`m≡rho*bar(ell) mod R` 给逆元核 `e(-h*rho*bar(ell)/R)`，并得到
短互补商窗口和 `(KWR-8)`。最终硬点拆成四个仍属原命题内部的分支：
`KLS-window` 覆盖活跃参数、`high-lcm clamp`、`high-frequency endpoint`、`coefficient concentration`。
其中后三项应路由到既有缺陷；第一项需核验 DI/BFI/KLS-window 是否覆盖本 H3 参数。

新增 `docs/monograph/prime-matrix-h3-dsb-high-lcm-clamp-routing.md` 后，`high-lcm clamp`
分支已不再是未定位参数漏洞：若 `R(c)>R_0` 承载 `q/log y` 级质量，则单元容量
`1+floor((q+O(1))/R_0)` 强制大量稀疏高 `lcm` 单元激活；跨坏行持久时给出
`PDEC/ColumnCRT` 非零 Fourier/CRT 缺陷，非持久时进入 `SAE` 单窗逃逸。当前诚实状态：
高 `lcm` 分支路由已证，`Persistent-HLC` 与 `Sparse-HLC` 出口排斥仍未证。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-fourier-energy-clamp.md` 后，上述两个出口共享的
能量源已严格化：对同模高 `lcm` 相位块，有限 Plancherel 给出
`\sum_{h!=0}|\hat\mu(h)|^2=R sum_a mu(a)^2-U^2`；若 `U<=R/2`，非零能量至少 `RU/2`。
因此高 `lcm` 分支进一步压缩为已知 `PDEC/ColumnCRT` 持久出口或 `SAE/endpoint` 单窗出口；
仍未证明的是这两个出口的最终排斥。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-pdec-threshold-bridge.md` 后，persistent 高 `lcm`
出口已有同口径 PDEC 下界：
`L_HLC(B)=((R sum_a g_B(a)^2-U_B^2)/(R-1))^(1/2)`。稀疏时有统一下界
`L_HLC>=sqrt(R U_B/(2(R-1)))`；稠密例外 `U_B>R/2` 被路由回 `KLS-window`、
`PDEC/ColumnCRT` 或 `SAE/endpoint`。当前剩余精确为：对所有 HLC formal unit 证明
`U_CRT(B)<L_HLC(B)`，或给出失败的 SAE/endpoint 回流证书。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-pdec-failure-localization.md` 后，`U_CRT<L_HLC`
失败不再是自由缺口：若某非零频率方向达到下界 `L`，则任意 `0<=alpha<L/U` 的 Bohr-cap
`\{a:Re(zeta e(ha/R))>=alpha\}` 至少承载 `(L-alpha U)/(1-alpha)` 的质量。该帽集中必须
作为新 PDEC 约束来源或 `SAE/endpoint` 单窗证书处理；尚未完成的是排除全部 Bohr-cap 集中。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-bohr-cap-component-route.md` 后，Bohr-cap 集中
进一步拆成 `d=(h,R)` 的有效模数组件：每个组件长度至多 `d+omega(alpha)R`，且某个组件
承载至少 `(L-alpha U)/(d(1-alpha))` 的质量。剩余因此变为 high-gcd cap 的低有效模集中
排斥，或 short-arc cap 的 PDEC/SAE 证书化。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-high-gcd-descent.md` 后，high-gcd cap 已不再是
独立剩余：若 `d=(h,R)>D_0`，投影到 `R'=R/d` 保持 Fourier 系数与 Bohr-cap 质量，且
有效模数严格下降。当前剩余随之收窄为低有效模 PDEC/KLS 出口和 short-arc cap 排斥。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-short-arc-density-pressure.md` 后，short-arc
cap 已被压成密度压力公式：
`Pi_arc>=R(L-alpha U)/(D0(1-alpha)U(D0+omega(alpha)R))`。若该压力超过 `1+epsilon`，
则强制同一 formal unit 的局部密度尖峰，进入 PDEC 局部密度行或 `SAE/endpoint`；
否则只剩显式参数残余不等式。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-short-arc-pressure-optimizer.md` 后，压力低残余
被写成 `t=L/U` 的一维阈值 `Psi_{D0,R}(t)<=1+epsilon`。该残余推出
`\sum g(a)^2 <= (1+(R-1)tau^2)U^2/R` 与支持下界 `A>=R/(1+(R-1)tau^2)`，因此不再是
short-arc 出口，而是 KLS-window 低二范数输入或 coefficient concentration 失败。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-l2-flat-kls-admission.md` 后，L2-flat residual
已有 KLS admission 表：K1 模数、K2 频率、K3 平滑端点、K4 系数二范数、K5 gcd/unit、
K6 dyadic/尾标签分块。任一失败项都回到既有命名出口；全部通过时才进入 `KLS-window`。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-clean-kls-reduction.md` 后，HLC 内部剩余进一步
收窄：clean formal unit 定义为 E1--E6 均不发生；clean 时 K1--K6 逐项自动通过。
剩余唯一为 `HLC-KLS-ext`：对 clean HLC Kloosterman 窗口对象给出 `O(q/log^2 y)` 上界。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kls-external-adaptation.md` 后，`HLC-KLS-ext`
已有外部深定理版适配：`(CKR-4)` 的相位、模数、频率、短窗口、素数权、二范数、
gcd/unit 与分块条件逐项接入 DI/BFI/Kuznetsov 型窗口化 Kloosterman 输入。当前诚实状态为：
clean HLC 分支在外部深定理版中闭合；完全自足无黑箱版仍需重证该谱/dispersion 定理。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kls-core-reduction.md` 后，完全自足缺口进一步
压缩为单一 `HLC-KLS-core` 命题 `(CORE-5)`。该文严写 dyadic 分块、`Lambda(m)` 分解、
unit/gcd 剥离、L2 账本和多对数吸收，证明 `HLC-KLS-core => HLC-KLS-ext => clean HLC`
反例矛盾。当前唯一未自证行是 `(CORE-5)` 本身。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kls-core-self-contained-spine.md` 后，`(CORE-5)`
又被完全自足化拆解为：平滑 completion、逆元变量 completion、Kloosterman 二次型
`(SC-7)`、系数二范数 `(SC-8)`，以及唯一未内联的 `Kuznetsov-LS atom (SC-9)`。该文件
证明 `SC-9=>CORE-5`，并排除点态 Weil 路线足以闭合的误用。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kuznetsov-ls-atom-expansion.md` 后，`(SC-9)`
继续拆成 KZ-A--KZ-E：Kloosterman 权重平滑化、Kuznetsov trace formula 专门化、Bessel
transform 衰减、spectral large sieve、BFI/well-factorable dispersion 对数节省。该文证明
KZ-A--KZ-E 推出 `(SC-9)`；当时完全自足版剩余为 KZ-B--KZ-E 的内联证明。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kz-c-bessel-transform-decay.md` 后，KZ-C 已用
Bessel 微分方程、自伴算子和反复分部积分证明。当前 `SC-9` 的未闭合子原子剩余为
KZ-B、KZ-D、KZ-E。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kz-d-spectral-large-sieve-spine.md` 后，KZ-D
已对偶化为谱投影核矩阵上界，并完成 oldform、Eisenstein、holomorphic 谱的多对数账本。
该文证明 `PTK-D=>KZ-D`；因此 KZ-D 的唯一未内联核心压缩为 `PTK-D` 预迹核上界。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-ptk-d-pretrace-kernel-bound.md` 后，`PTK-D`
继续压缩为空间侧 `LPC-D` 行列和上界。该文完成谱截断测试函数接口、预迹/Poincare 系数核
展开、对角 `T^2` 体积账本，并证明 `LPC-D=>PTK-D`。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-lpc-d-spatial-correlation-split.md` 后，LPC-D
被拆成 FAR/ID/PAR/HYP 四类。FAR 尾项由 `k_T` 衰减闭合，ID-near 并入 PAR，PAR
cusp/parabolic 分支由 cusp 宽度与除数账本闭合；当前唯一空间侧剩余变为 `GHLC-D`
generic hyperbolic local correlation。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-ghlc-d-local-schur-closure.md` 后，`GHLC-D`
由局部 `L^1` 核质量和 Poincare 包 Schur 检验闭合，继而
`GHLC-D=>LPC-D=>PTK-D=>KZ-D`。因此当前 `SC-9` 的未闭合子原子剩余已缩为
KZ-B、KZ-E。后续 KZ-B 条目已进一步压缩为只剩 KZ-E。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kz-b-kuznetsov-trace-specialization.md` 后，
KZ-B 由 Poincare 包 unfolding、双陪集 Kloosterman 求和和谱 Plancherel 展开内联推导闭合。
该步只闭合公式转换和归一化，不提供对数节省。因此当前 `SC-9` 的未闭合子原子剩余为
KZ-E。

新增 `docs/monograph/prime-matrix-rpz-absorption-defect-route.md`、
`docs/monograph/prime-matrix-rpz-absorption-defect-audit.md` 与脚本
`experiments/prime_matrix_rpz_absorption_defect_audit.py` 后，复活点吸收缺陷已路由为
`survivor/TailAnchor/ColumnCRT/ColumnRadius/Distributed-RPZ`。同批 `5` 个首零行样本中，
半宽复活点总数为 `15`，缺失吸收标签为 `0`，单窗最大吸收标签负载和最大顶层列负载均为 `1`。
因此当前最小硬点进一步更新为 `RPZ-Distributed Barrier`：低负载分散吸收若持续，必须证明其容量
小于 RPZ 复活点需求，或使其回流到 `ColumnCRT/ColumnRadius/TailAnchor` 命名出口。

新增 `docs/monograph/prime-matrix-rpz-sliding-plateau-barrier.md`、
`docs/monograph/prime-matrix-rpz-sliding-plateau-audit.md` 与脚本
`experiments/prime_matrix_rpz_sliding_plateau_audit.py` 后，`Distributed-RPZ` 的滑动平台版本已压缩为
`TailAnchor` 或边界压缩。审计显示同批样本最大滑动零窗平台长度为 `5`，唯一复活源 `16` 个，
吸收事件 `73` 个，阈值 `T_0=4` 下 `5/5` 记录触发持久源 TailAnchor。当前最小硬点更新为
`RPZ-BCB`：排除源删除后的边界层逃逸，或将其路由到 `SAE/PDEC/ColumnCRT`。

新增 `docs/monograph/prime-matrix-rpz-boundary-compressed-core-route.md`、
`docs/monograph/prime-matrix-rpz-bcb-core-audit.md` 与脚本
`experiments/prime_matrix_rpz_bcb_core_audit.py` 后，`RPZ-BCB` 已严格路由为半宽筛零核心：
无 TailAnchor 时 `J_{T0}=[L+A+T0,R+B-T0]` 没有 `h`-筛幸存者。同批样本中中心区间幸存者
总数 `11`，全部为尾锚核心源；条件删除后 `5/5` 中心区间干净且含完整半宽行。当前最小硬点更新为
`BCB-Grid/Endpoint exclusion`：证明中心区间含完整下层行，或端点 seam 缺陷进入
`SAE/PDEC/ColumnCRT`。

新增 `docs/monograph/prime-matrix-rpz-bcb-grid-endpoint-criterion.md`、
`docs/monograph/prime-matrix-rpz-bcb-grid-endpoint-audit.md` 与脚本
`experiments/prime_matrix_rpz_bcb_grid_endpoint_audit.py` 后，`BCB-Grid` 的几何部分已闭合为精确判据：
`N>=delta_h(u)+h` 当且仅当含完整 `h` 对齐行。样本中 `5/5` 满足该判据，端点缺陷为 `0`，
判据与枚举不一致为 `0`；`4/5` 由纯长度条件 `N>=2h-1` 自动闭合。当前最小硬点更新为
`BCB-Endpoint persistence exclusion`：排除端点失败相位持续存在，或送入 `SAE/PDEC/ColumnCRT`。

新增 `docs/monograph/prime-matrix-rpz-bcb-endpoint-persistence-route.md`、
`docs/monograph/prime-matrix-rpz-bcb-endpoint-phase-ledger.md` 与脚本
`experiments/prime_matrix_rpz_bcb_endpoint_phase_ledger.py` 后，端点失败分支已完成命名化：
实际端点失败 `0/5`，可能失败相位总数 `2`；低负载进入 `SAE`，持久同相失败进入
`PDEC/ColumnCRT`。当前 RPZ 链条剩余不再是端点路由，而是 `SAE/PDEC/ColumnCRT` 证书闭合，
或沿已得到的下层 `h`-筛零行继续递归下降。

新增 `docs/monograph/prime-matrix-rpz-dual-track-closure-route.md`、
`docs/monograph/prime-matrix-rpz-lower-zero-descent-audit.md` 与脚本
`experiments/prime_matrix_rpz_lower_zero_descent_audit.py` 后，两条剩余路线已同步推进：
Track A 定义 `RPZ-SAE finite package`、`RPZ-PDEC endpoint phase row`、`RPZ-ColumnCRT endpoint displacement row`；
Track B 证明下层零行下降引理，并在样本中将 `6` 条条件下层零行全部降到 `p=2` 直接矛盾，
阻断节点数为 `0`。当前最小硬点更新为 `LowerDescent-Grid persistence` 与
`RPZ-SAE/PDEC/ColumnCRT certificate materialization`。

新增 `docs/monograph/prime-matrix-rpz-lower-descent-obstruction-ledger.md`、对应 JSON 与脚本
`experiments/prime_matrix_rpz_lower_descent_obstruction_ledger.py` 后，下降阻断已落入有限相位账本：
实际下降转换节点 `20` 个全部为 `success`，实际阻断为 `0`；可能阻断分为 `grid_fail` 与
`puncture_block`。新增 `docs/monograph/prime-matrix-rpz-certificate-materialization-interface.md`
把阻断相位统一接入 `RPZ-SAE-FIN`、`RPZ-PDEC` 与 `RPZ-ColumnCRT` 证书。该项只压缩接口，
不排除这些出口；当前下一步是生成 SAE 候选清单与 PDEC/ColumnCRT 证书骨架。

新增 `docs/monograph/prime-matrix-rpz-certificate-skeleton-package.md`、对应 JSON 与脚本
`experiments/prime_matrix_rpz_certificate_skeleton_builder.py` 后，SAE/PDEC/ColumnCRT 骨架已生成：
endpoint SAE 候选 `2` 个；endpoint PDEC/ColumnCRT 行各 `2` 条；lower-descent `grid_fail`
PDEC/ColumnCRT 行各 `3` 条；lower-descent 可能阻断相位 `1752` 个且全部为 `grid_fail`。
该项仍为证书待填状态；下一步是填写两个 SAE 候选并压制三条 grid_fail 相位行。

新增 `docs/monograph/prime-matrix-rpz-endpoint-sae-finite-certificate.md`、对应 JSON 与脚本
`experiments/prime_matrix_rpz_endpoint_sae_finite_certificate.py` 后，两个 endpoint SAE 候选在
当前有限账本中 actual load 为 `0`，所以 endpoint `RPZ-SAE-FIN` 当前账本真空闭合。该项不升级
全局 SAE 排斥；当前剩余集中到三条 lower-descent `grid_fail` 相位行。

新增 `docs/monograph/prime-matrix-rpz-lower-grid-fail-avoidance-certificate.md`、对应 JSON 与脚本
`experiments/prime_matrix_rpz_lower_grid_fail_avoidance_certificate.py` 后，三条 lower-descent
`grid_fail` 行已转为闭式相位判据并核验当前下降树避开：实际转换节点 `20`、实际 `grid_fail`
节点 `0`、闭式计数不一致 `0`。该项仍不证明全局路径避开；下一硬点是全局相位控制或
`PDEC/ColumnCRT` 排斥。

新增 `docs/monograph/prime-matrix-rpz-formal-descent-phase-inequality.md` 后，状态更新为：
正式下降路径一旦存在，`delta<=p-r` 全程自动成立；全局未闭合点是路径存在性。若不存在，
首阻断相位进入 `SAE/PDEC/ColumnCRT`。因此当前剩余是证明所有正式反例分支存在下降路径，
或排除首阻断相位证书。

新增 `docs/monograph/prime-matrix-rpz-first-obstruction-dichotomy.md` 后，端点穿孔阻断全局排除；
首阻断唯一可能是 `grid_fail` seam 相位。当前 RPZ 剩余更新为 first-grid-fail seam 的
`SAE/PDEC/ColumnCRT` 排斥证书。

新增 `docs/monograph/prime-matrix-rpz-first-grid-fail-seam-certificate.md`、对应 JSON 与脚本
`experiments/prime_matrix_rpz_first_grid_fail_seam_certificate.py` 后，first-grid-fail seam 已标准形化：
`12` 个双帽 seam 相位行覆盖 `1752` 个完整 `Q` 相位，计数不一致为 `0`。当前剩余是这些
双帽 seam 标准形的 `PDEC/ColumnCRT` 证书排斥。

新增 `docs/monograph/prime-matrix-gje-sae-terminal-band-decomposition.md` 后，`GJE-SAE` 又被拆成低行段与终端带：指数 `theta>1/2` 的普通短区间素数输入最多覆盖 `s<=q^{1/theta-1}` 量级低行段，不能覆盖 `s≈q` 的终端行。终端带经 `m=q^2-n` 镜像后成为“每个旧素数 `ell<=p` 只允许非零类 `q^2 mod ell`”的 CRT 覆盖问题。当前最小硬核更新为 `Terminal-SAE/PDEC`。

新增 `docs/monograph/prime-matrix-terminal-sae-split-audit.md` 与 `docs/monograph/prime-matrix-terminal-sae-split-inequality.md` 后，终端带又被压成分层骨架/尾命中不等式。取 `y=max(2,floor(p/e))`，低筛骨架数 `G_y(h)` 若大于尾素数命中重数 `T_y(h)`，则尾素数无法覆盖骨架，终端行必有旧筛幸存者。审计到 `p<=1000` 的全部终端镜像块均满足正余量；当前最小硬点更新为 `TSI-or-PDEC`。

新增 `docs/monograph/prime-matrix-terminal-sae-y-sweep.md`、`docs/monograph/prime-matrix-terminal-tail-cofactor-audit.md` 与 `docs/monograph/prime-matrix-terminal-tail-cofactor-identity.md` 后，`TSI` 的参数与尾项结构更清楚：`y/p` 在 `0.30..0.70` 的样本区间内均安全，`p/e` 不是孤立调参点；尾命中精确等于 `q^2-m=ell*t` 中常数长度互补 `y`-rough 区间计数，样本最大长度为 `4`，复合互补因子最后出现在 `p=19`。右侧 `T_y(h)` 因此可进一步作为极短互补素数窗口总和处理。

新增 `docs/monograph/prime-matrix-terminal-sae-cancellation-identity.md` 与审计 `docs/monograph/prime-matrix-terminal-sae-cancellation-audit.md` 后，`TSI` 又被压缩为单尾抵消恒等式：`G_y(h)-T_y(h)=sum_{P^-(n)>y}(1-omega_tail(n))`。所有恰有一个尾素因子的骨架点贡献为 `0`；当前最小硬核变为 `RCI/PDEC`：证明每个终端块中“无尾储备数 > 多尾碰撞超额”，或证明该失败必触发持续端点/尾锚缺陷。审计到 `p<=1500` 仍无失败，并严格排除了 `n=1,q^2` 的端点误算。

新增 `docs/monograph/prime-matrix-column-assisted-rci-bridge.md` 与审计 `docs/monograph/prime-matrix-column-row-bridge-audit.md` 后，明确了“若列命题作为已证输入”时的最快行命题桥接：列命题不能直接推出固定行非空，但它给每个非平凡列提供素数见证；行内覆盖标签迫使同列见证位移避开相应模数零类。因此 `RCI` 失败应转化为 `CDB`：双尾碰撞集中、端点 CRT 缺陷或列见证半径异常三者之一。样本 `q<=1000` 中非平凡列失败为 `0`，排除第 `q` 平凡列后的最大列见证半径为 `107`。当前行命题最小桥接接口可写为 `RCI-Fail + Col(q) => CDB defect => PDEC/Tail-anchor`。

新增 `docs/monograph/prime-matrix-rci-cdb-parallel-hard-attack.md` 与联合审计 `docs/monograph/prime-matrix-rci-cdb-joint-audit.md` 后，`RCI/PDEC` 与 `CDB/PDEC` 的关系被整理为并行三分支：分散双尾碰撞由 `Distributed-RCI` 直接吸收；尾标签集中进入 Tail-anchor defect；位移余类集中进入 Endpoint/Column CRT defect。样本 `p<=1000` 的紧行最小 `RCI margin=1`，紧行最大尾标签负载和位移余类负载均为 `2`，说明最优先硬攻应是 `CDB-1 / Distributed-RCI`，而不是过强地证明所有列见证半径有小常数界。

新增 `docs/monograph/prime-matrix-distributed-rci-semiprime-reduction.md` 与审计 `docs/monograph/prime-matrix-distributed-rci-semiprime-audit.md` 后，`Distributed-RCI` 被进一步半素数化：在 `y^3>q^2` 后，无尾储备就是素数，负项就是因子均在 `(y,p]` 的平衡双尾半素数。审计到 `p<=2000` 显示最后双尾残因子例外为 `p=13`，最后三尾例外为 `p=7`，最大平衡半素数/无尾比值为 `2/3`。当前最小硬点可写成：终端块内平衡双尾半素数数严格小于素数数；集中例外进入 `CDB-2/CDB-3/PDEC`。

新增 `docs/monograph/prime-matrix-distributed-rci-local-pairing-route.md` 与审计 `docs/monograph/prime-matrix-distributed-rci-pairing-audit.md` 后，平衡半素数不等式再压成局部 Hall 配对问题：每个平衡双尾半素数应能匹配到同一行附近不同素数；若匹配失败，失败区间同时给出半素数过密与素数过疏，可送入 `Tail-anchor/PDEC`。审计 `17<=p<=2000` 中含平衡半素数行 `215074`，配对失败 `0`，最大最小匹配半径 `132`。当前最小硬点更新为 `LPH/PDEC`。

## 两点 P-rough 命题 A/B 状态

新增 `docs/monograph/two-point-rough-pair-propositions.md`。审查结论：A 与 B 在同余条件上等价；由于 `P×P` 方阵内任意大于 1 的 `P`-rough 数必为素数，A/B 对固定偶数 `w` 的全体充分大 `P` 成立将推出固定偶差素数对无穷多，特别 `w=2` 推出孪生素数猜想。这一强后果不是逻辑反驳；若证明链独立、逐行、无缺口，则可升级为无条件定理。当前不能升级的实际原因是关键输入仍以条件链或命名出口形式登记，尚未全部内联证明并通过独立审稿。

## 二次筛研究备忘录更新

新增 `docs/monograph/two-point-secondary-sieve-research.md`。该文档把 A/B 统一为二禁余类问题 `x not≡ 0,w (mod p)`，给出完整 CRT 周期非空、短窗口二点 Jacobsthal 障碍、二次覆盖证书与单线/双线/交叉容量骨架。状态仍为研究方向：要升级为定理，必须证明短窗口二点候选非空或等价的高阶补孔能量矛盾。

## 二次筛与原行列方法迁移审查

`docs/monograph/two-point-secondary-sieve-research.md` 已补充第 14--19 节，逐项比较原长度 `P` 的一次行列窗口与当前长度 `P^2/2` 的二次后半窗口。结论：窗口确实更大，启发式候选更多；但每个素数禁两个相位类且候选自动给出素数对，因此不能简单视为原命题的弱化。可迁移武器包括 CRT 均衡、斜线证书、局部大因子不可复用和剥离思想；真正新接口是“大素数补孔非覆盖命题”。

## 大素数补孔非覆盖硬点更新

`docs/monograph/two-point-secondary-sieve-research.md` 已补充第 20--23 节。已建立补孔二部图、局部分块刚性、跨块固定相位和精确单线骨架容量。审查结论：单纯两层总容量法存在尺度冲突；小素数骨架需要 `y=O(log P)`，而容量排除补孔需要 `y` 接近 `P^c`。因此下一步真正硬点不是总容量，而是相位-骨架相关的非覆盖不等式或缺口传播链。

## 缺口传播链与分层递推更新

`docs/monograph/two-point-secondary-sieve-research.md` 已补充第 24--29 节。审查结论：不分层时大素数覆盖均值过高，唯一证书传播链难以启动；分层后每层可保持边际覆盖状态，适合旧矛盾场的局部传播思想。新的最小硬点是“递推均匀性 / 异常集中二分引理”：每层剩余集要么对下一层素数相位保持均匀、不能被清空；要么异常集中并转化为 CRT 结构矛盾。

## 递推均匀性二分引理审查

`docs/monograph/two-point-secondary-sieve-research.md` 已补充第 30--34 节。已严格给出均匀分支：若层偏差总量小于 `alpha |U|`，则该层保留比例至少 `1-2 sum 1/p-alpha`。异常分支审查显示：完整周期法只能在 `Q_Y<<|I|` 时排除异常，递推到较大层会因 CRT 模数爆炸而失效。新的最小硬点升级为“低阶相关递推引理”：用前层禁线的稀疏历史与有限阶交叉控制下一层相位偏差。

## 45度双锁与粗数带刚性并入

`docs/monograph/two-point-secondary-sieve-research.md` 已补充第 35--39 节。二次筛中旧 45 度小素因子合数线变为双份小素锁层：`q|x` 与 `q|x-w`，在 `q|w` 时重合，在 `q∤w` 时形成双相位平移锁。粗数带 `G_y` 是剥离双锁后的剩余；大素补孔必须满足同侧短窗互斥、异侧 `w mod p` 距离锁和跨块固定相位。新的最小硬点锁定为“相位簇异常排斥引理”。

## 相位簇异常与加权覆盖不等式更新

`docs/monograph/two-point-secondary-sieve-research.md` 已补充第 40--44 节。相位簇异常被量化为低阶小素锁交叉类与大素线的相关偏差；短块互斥给出局部容量上界，但审查发现仍缺“异常集中化”桥。当前最清晰的反例矛盾形式升级为筛权重加权覆盖不等式：反例清空给出加权覆盖下界，而低阶相关控制若能给出小于 1 的加权覆盖上界，则产生矛盾。下一步最小硬点是构造合适的 Selberg/Brun 型非负权重 `W` 并压低 `Err_corr`。

## 结构化筛权重路线更新

`docs/monograph/two-point-secondary-sieve-research.md` 已补充第 45--50 节。传统 Selberg/Brun 低阶权重可控制相关，但难以提供支持在真实剩余集上的下界，存在 parity barrier。新路线是构造结构化筛权重 `W_struct=1_{G_{y0}} V_R Psi`：硬骨架精确剥离小素双锁，`V_R` 控制软历史，几何惩罚 `Psi` 吸收相位簇异常、短块互斥与异侧距离锁。下一步最小硬点是给出可计算的 `Psi` 并验证其能降低 `Err_corr`。

## 最小结构惩罚项 Psi_tau 更新

`docs/monograph/two-point-secondary-sieve-research.md` 已补充第 51--56 节。已定义最小几何惩罚 `Psi_tau`：按短块拥挤度 `Omega_j` 删除过密块；保留块上可得到加权覆盖上界。审查发现新二分：若真实剩余质量在保留块中，则可能闭合；若集中在删除的拥挤块中，则需证明拥挤块导致块二阶能量或相位簇异常超过 CRT 与双相位互斥上界。新的最小硬点为“拥挤块排斥引理”。

## 拥挤块排斥审查与低覆盖块转向

`docs/monograph/two-point-secondary-sieve-research.md` 已补充第 57--62 节。块二阶能量展开显示：高拥挤块代表覆盖资源多，二阶能量只能控制多重度，不能直接排斥有效覆盖；因此“删除拥挤块”的 `Psi_tau` 方向不足。更有希望的矛盾源是低覆盖块：选层使平均块覆盖比低于 1，证明低覆盖块存在且真实剩余集不能完全避开它们。新的最小硬点改为“低覆盖块不可避引理”。

## 低覆盖块不可避引理严写更新

`docs/monograph/two-point-secondary-sieve-research.md` 已补充第 63--69 节。低覆盖块不可避被严格转化为相关问题：若反例避开低覆盖块，则真实剩余集 `U` 与下一层覆盖函数 `D_P` 出现正相关异常；排斥该异常等价于低阶相关递推引理。已证明条件弱版本：若某非负权重 `W` 满足 `sum W D <= beta sum W` 且 `beta<1`，则存在正 `W`-质量的低覆盖点。剩余核心仍是构造结构化下界权重，使这些低覆盖点属于真实剩余集。

## 结构化下界权重真实/虚假质量分解

`docs/monograph/two-point-secondary-sieve-research.md` 已补充第 70--76 节。结构化权重闭合被精确拆成真实质量 `M_true`、虚假质量 `M_false` 与相关上界 `beta`：若 `M_false<=kappa M_true` 且 `beta(1+kappa)<1`，则反例矛盾。审查显示全局降低虚假质量等同近似 `1_{S=0}`，会遭遇低阶可控性/parity barrier；更可攻的是低覆盖块局部化，只在 `Low` 上控制虚假质量。新的最小硬点为“低覆盖块局部真实质量引理”。

## 低覆盖块局部真实质量与近交叉工具

`docs/monograph/two-point-secondary-sieve-research.md` 已补充第 77--84 节。若 `U` 在低覆盖块 `Low` 上太小，则软历史覆盖 `S_B` 在 `Low` 上异常偏大；而 `Low` 是下一层覆盖 `T_B` 偏低区域，因此产生软历史与下一层覆盖的块级负相关。新工具：两条不同层斜线穿过同一长度 `L` 短块的次数可写为 `|h|<L` 的 CRT 近交叉计数，上界约为 `L|I|/(pq)+L`。下一步最小硬点是归一化并优化块级近交叉不等式。

## 块级近交叉不等式归一化审查

`docs/monograph/two-point-secondary-sieve-research.md` 已补充第 85--92 节。对软历史线 `q` 与下一层线 `p` 穿过同一短块的近交叉，已给出双侧 CRT 估计：总量为 `4(2L-1)|I|AB + O(L Q_# P_#)`。归一化误差约 `Q_#P_#/(|I|AB)`，通常可控。但该估计主要控制二阶同现/协方差，不能直接控制 Low 条件化事件。新的最小硬点为“块级阈值相关/浓度引理”：证明 `s_B` 在 `{t_B<theta}` 上的条件均值不异常偏高。

## 块级阈值相关矩方法更新

`docs/monograph/two-point-secondary-sieve-research.md` 已补充第 93--98 节。阈值相关问题被转化为混合矩控制：用低阶多项式逼近 `1_{t<theta}`，需要估计 `E[s t^k]`；CRT 近交叉可给出固定阶混合矩主项和误差。单层软历史覆盖 `s_B` 方差可能过大，新的更可行路线是多软层平均：若真实剩余避开 Low，则多个软历史小层在 Low 上持续偏高，违反跨层近交叉混合矩/浓度估计。新的最小硬点为“多软层块级浓度引理”。

## 多软层块级浓度框架更新

`docs/monograph/two-point-secondary-sieve-research.md` 已补充第 99--107 节。软历史被拆成多个小层 `Q_m`，若真实剩余避开 Low，则累计软覆盖在 Low 上偏高；该偏高必须分配到许多小层或少数异常层。单层与 Low 的相关通过多项式上界 `P_K(t)` 和混合矩 `E[s^{(m)}t^k]` 控制，混合矩由固定阶近交叉 CRT 估计给出。当前未闭合点是实际选择 `mu_m,M,K,T,theta`，验证阈值逼近代价与矩误差能否同时满足。

## 参数可行性审查与累计软覆盖转向

`docs/monograph/two-point-secondary-sieve-research.md` 已补充第 108--116 节。逐小层控制要求每层误差约 `1/M`，过于严格；更可行的是直接控制累计软历史覆盖 `s_tot` 与 Low 的相关。推荐常数级参数目标：`mu_tot≈1/2, nu≈1/2, theta≈1/4, K=2或3, T=3或4`，只需证明 `E[s_tot|Low] <= mu_tot+O(0.2)`。新的最小硬点为“累计软覆盖阈值相关引理”。

## 累计软覆盖阈值与极短块转向

`docs/monograph/two-point-secondary-sieve-research.md` 已补充第 117--124 节。二阶矩和二次多项式阈值上界不足以给出 `E[s_tot|Low]` 的强常数界；关键自由度转为块长 `L`。若取极短块 `L≈(log y0)^2`，使硬骨架每块平均常数个点，则 Low 可简化为下一层零命中事件，更贴近缺口传播与原行列短窗刚性。新的最小硬点为“极短块零命中不可避引理”。

## 极短块零命中模型更新

`docs/monograph/two-point-secondary-sieve-research.md` 已补充第 125--132 节。取块长 `L≈delta_0^{-1}≈(log y0)^2`，使硬骨架每块平均 `c0` 个点。若硬骨架非空块比例 `a(c0)` 与下一层命中均值 `nu` 满足 `a(c0)>nu c0`，则下一层零命中且硬骨架非空的块占正比例。反例要求这些 Zero 块中的硬骨架点全部已被软历史覆盖；新的最小硬点为“Zero 块软历史不可全覆盖引理”。

## Zero块软历史不可全覆盖严攻更新

`docs/monograph/two-point-secondary-sieve-research.md` 已补充第 133--141 节。反例要求在 Zero 块上 `sum S_B 1_{R=0} >= sum X_B 1_{R=0}`；独立预测为 `mu` 倍，其中 `mu<1`。通过 Bonferroni 展开 `1_{R=0}`，问题转化为固定阶混合矩 `sum S_B binom(R_B,k)` 的 CRT 近交叉估计。下一步最小硬点是选择 `mu≈1/2, nu c0≈1/2, K=2或3, T=3`，严查截断与高尾误差能否给出 `epsilon<1-mu`。

## Bonferroni参数常数审查更新

`docs/monograph/two-point-secondary-sieve-research.md` 已补充第 142--149 节。Poisson 常数模型显示：当 `lambda≈1/2` 时二阶 Bonferroni 上界已很准；对 `lambda<=1.5`，四阶 Bonferroni 配合 `mu=1/2` 仍有余量。建议参数 `c0=1/2, nu=1/2, mu=1/2, K=4, T_X=3`。新的最小硬点为“四阶 Bonferroni--近交叉参数引理”：控制 K=4 的 CRT 混合矩误差和硬骨架高 `X_B` 尾部，使总误差小于常数余量。

## K阶近交叉误差与分尺度策略更新

`docs/monograph/two-point-secondary-sieve-research.md` 已补充第 150--156 节。K=4 常数余量好，但若下一层厚度满足 `B≈1/4` 且尺度接近 `P`，CRT 近交叉误差要求 `Q_#Y^4<<P^2`，高尺度不可控。K=2 条件放宽为 `Q_#Y^2<<P^2`，配合 `c0=1/3` 更可行，但最高尺度仍需薄层处理。新的路线为“分尺度极短块引理”：中低尺度用低阶 Bonferroni--近交叉控制厚层，高尺度用薄层短块互斥容量递推。

| 二次筛 A/B 顶尺度容量不足 | 研究中 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 165--170 节。顶尺度清空被化为 `sum_U D_H >= |U|`，目标上界为 `(2 log(1/alpha0)+eta)|U|`。已确认全区间平均和每点大因子个数只给出粗控制，不能闭合；新的最小硬点是 TCA：顶尺度异常集中必须推出互补因子短桶拥挤，并由 CRT 均衡与大因子短窗互斥排除。 |

| 二次筛 A/B TCA 到 SMC 转化 | 研究中 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 171--176 节。通过互补因子参数化 `x=pm`，得到顶尺度命中要求 `m` 为 `Y_H`-rough 且 `p` 避开 `wm^{-1}` 禁类；异常集中被压缩为互补因子桶拥挤和极短块乘法近交叉过多。新的最小硬点为 SMC：证明带二次筛条件的乘法近交叉二阶上界。 |

| 二次筛 SMC 局部因子 | 研究中 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 177--181 节。逐小素 `q` 计算了二次筛近交叉局部因子：坏放大只来自 `q|h` 的对角相位同步，且总放大受 `prod_{q|h}(1+C/q)` 控制。当前最小硬点压缩为 AVG-SS：极短差值范围内奇异级数同步因子的平均需为 `1+o(1)` 或足够小的常数。 |

| 二次筛 AVG-SS 平均同步因子 | 研究中 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 182--186 节。将同步放大权重写成 divisor 型乘法函数 `g(h)=prod_{q|h}(1+A/q)`，无条件得到绝对平均常数界 `prod_q(1+A/q^2)`。为闭合常数余量，需要进一步中心化局部因子，并证明短区间平均 `L^{-1}sum_{h<L}g(h)=1+O(1/log L)` 或足够小的常数界。 |

| 二次筛 C-AVG-SS 中心化接口 | 研究中 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 187--192 节。精确计算显示局部因子 `Gamma_q(h)` 在 `h mod q` 上均值严格等于 1；坏同步仅来自 `h=0,±w mod q`。已用三重平移除数权重给出绝对常数平均框架，并提出用精确中心化乘积替代上包络以证明 `L^{-1}sum G_L=1+o(1)`。 |

| 二次筛 C2-AVG-SS 平方平均路线 | 研究中 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 193--198 节并修正尾部截断。绝对值 Rankin 路线被审查为不足；正确方向改为利用 `phi_q` 零均值、三特殊类稀疏支撑和平方平均 `E|phi_q|^2<<q^{-3}`。新的最小硬点为 C2-AVG-SS：证明 `Phi_S` 的短区间平方平均并完成小/中/超大周期三段求和。 |

| 二次筛 C2-AVG-SS 严写审查 | 研究中 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 199--204 节。固定集合平方平均估计已严写；小周期段由零均值周期相消闭合，中周期主项由 `Q_S^{-3/2}` 尾和闭合。剩余障碍精确定位为尖锐短区间带来的 `Q_S` 级边界项；下一步最优路线是平滑 C2-AVG-SS。 |

| 二次筛旧方阵+CRT约束并入审查 | 研究中 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 205--210 节。审查确认此前尚未充分利用旧矛盾场约束，尤其相邻商互质、45度双锁削峰、周期镜像边界相消仍未完全进入不等式。新路线升级为 SC2-AVG-SS：结构平滑中心化平均，下一步优先专攻 45度削峰引理。 |

| 二次筛45度削峰接口 | 研究中 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 211--215 节。平移同步 `h=±w` 可由端点计数自动削峰；主同步 `h=0` 需要使用大因子短窗互斥、互质商异常、CRT均衡缺陷三者联合削峰。当前最小硬点为 45-Main 削峰引理。 |

| 二次筛45-Main严攻 | 研究中 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 216--222 节。Reuse 异常在短差值下严格为零；Shared 互补商共享在 `L<Y_H` 下非退化严格为零。Good 主同步归约为互质商线性同余锁；剩余最小硬点为 Good-to-CRTDefect：若 good 同步达到模型密度，则推出小素投影 CRT 均衡缺陷。 |

| 二次筛Good-to-CRTDefect修正 | 研究中 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 223--229 节。一阶投影缺陷不足，正确对象是二阶差值转移矩阵缺陷。取 `r=q` 会循环，因为模型已包含主同步峰；需取辅助素 `r≈L, r≠q`，利用 `h=qt, |t|<L/q` 导致差值类支撑稀疏，从而推出二阶 CRTDefect。 |

| 二次筛辅助投影能量矛盾 | 研究中 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 230--234 节。主同步 `h=qt, |h|<L` 在辅助素 `r≈L` 上只占 `O(L/q)` 个差值类，给出二阶能量下界 `|G_q|^2/(1+2L/q)`；若近交叉能量上界为 `(1+eps)|G_q|^2/r+Err_r` 且误差足够小，则中大 `q` 主同步矛盾。剩余硬点为 Auxiliary Energy Upper Bound。 |

| 二次筛Auxiliary Energy严攻 | 研究中 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 235--240 节。辅助能量被四元组化；Reuse/Shared 后退化项归为端点度数，非退化项由 CRT 均衡给出 `1/r` 主项，镜像平滑处理边界。形成闭环：非零频大即 CRTDefect，非零频小则能量上界与主同步稀疏下界矛盾。剩余为 Endpoint Degree 与 Fourier CRTDefect 两个定量引理。 |

| 二次筛Endpoint Degree闭合 | 研究中 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 241--244 节。端点度数由 `y=x+qt, |t|<L/q` 点态给出 `d(x)<<1+L/q`，退化能量 `<<(1+L/q)|G_q|`；若不可吸收则 `G_q` 已小而削峰成功。剩余唯一硬点压缩为 Fourier CRTDefect Lemma。 |

| 二次筛Fourier CRTDefect硬攻 | 研究中 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 245--250 节。不转换命题，直接把大非零 Fourier 系数转成辅助模差值弧偏差；因 `r≈L, |h|<L`，进一步提升为真实短差值方向偏差；该偏差由 Directional Balance Lemma 排除。剩余唯一严写点为 Directional Balance 的小商误差与大商比例估计。 |

| 二次筛Fourier CRTDefect条件闭合 | 研究中 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 251--255 节。Directional Balance 分大商/小商严写：大商段给出 `|D|/(2L)+O(delta_L)` 比例，小商段因互补商 `Y_H`-rough 且 `Y_H>>L/delta_L` 只剩低阶端点。由此非零 Fourier 缺陷为 `o(|G_q|)`；45-Main 链条剩余转为统一参数核查。 |

| 二次筛统一参数核查 | 条件闭合/待常数核查 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 256--261 节。取 `Y_H=P^alpha0`, `L≈(log log P)^2`, `delta_L=(log L)^-1/10` 可满足 Reuse/Shared/小商吸收等尺度条件。45-Main 已回接 SC2-AVG-SS，再回接 SMC/TCA 顶尺度容量不足。诚实审查：尚未无条件闭合，剩余为小素常数包、TCA桥接损失、平滑回退损失、`q|w` 特例的最终余量核查。 |

| 二次筛最终常数余量核查 | 未闭合/剩 TCA 桥接 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 262--270 节。取 `alpha0=0.7` 总余量约 `0.28665`。Reuse/Shared 为 0，Endpoint/Directional/Smooth 可压到约 `0.06` 内；`q=2` 归一化为奇数骨架后不产生额外损失，奇素 `q|w` 更易处理（固定 w）。最大未闭合项为 TCA 桥接损失：需证明平均容量超标到 SMC 近交叉异常的线性桥接常数小于剩余约 `0.22665`。 |

| 二次筛TCA线性桥接严攻 | 研究中 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 271--277 节。TCA 从平方损失改写为块级线性正部：全局超容量给出 `sum_B(R_B-lambda_H X_B)_+`，该正部必须表现为 SMC/Directional/Endpoint/Block 损失。若块选择损失 `E_block<0.10`，则可取 `E_TCA<0.16<0.22665`。剩余最小硬点为 Block Positive-Part Lemma。 |

| 二次筛Block Positive-Part审查 | 研究中 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 278--282 节。取 `c0=1/2, alpha0=0.7` 时 Zero 块质量粗估给出正部约 `0.082`，接近但不足以支撑保守 `E_block<0.10`；提高 `alpha0` 到 `0.75` 可把总余量增至约 `0.425`。当前最小硬点压缩为 Zero Mass Lemma：证明 Zero 非空块承载足够质量，并优化 `c0,alpha0`。 |

| 二次筛Zero Mass严攻 | 条件可行 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 283--288 节。用 size-biased 公式得到 `rho0_model=(1-nu)e^{-c0 nu}`；取 `c0=1/2, nu=1/2` 模型值约 `0.389`。二阶 Bonferroni 保守目标 `rho0>=0.30` 可行。改取 `alpha0=0.75` 后余量 `1-2log(4/3)≈0.4246`，块正部约 `0.127>0.10`。剩余为补写二阶 Bonferroni Zero Mass 引理。 |

| 二次筛Zero Mass引理严写 | 条件闭合/待中尺度复核 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 289--296 节。用 `X=1,2` 块和二阶 Bonferroni 给出保守 `rho0>=0.30`：取 `M1>=0.58, M2>=0.28`，零概率分别 `>=0.48, >=0.10` 得 `0.3064`。最终参数 `alpha0=0.75,c0=1/2,nu=1/2` 下 Zero 正部约 `0.127`，TCA 损失可控到约 `0.16`。剩余全局义务：复核中尺度到 `P^0.75` 的 K=2 近交叉条件。 |

| 二次筛中尺度K2全局复核 | 参数通过/I1已定理化 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 297--303 节。最终 `alpha0=0.75` 时，若使用薄层递推、固定阶局部交叉与硬骨架截断 `R<=polylog(P)`，则最坏层 `Y=P^0.75` 的 K=2 误差为 `P^-0.5 polylog(P)=o(1)`，层数累积仍 `o(1)`。第 340--344 节已把 `Q_eff<=polylog` 内联证明；剩余是 SC2误差、Zero Mass块分布、平滑回退正式定理化。 |

| 二次筛剩余审稿义务A-D | I1/I2/I4已放电，剩 I3-Core | `docs/monograph/two-point-secondary-sieve-research.md` 第 340--344 节已内联证明 A/I1 固定阶局部交叉 `Q_eff,k<=polylog(P)`；第 345--349 节已把 I4 Zero Mass 与平滑回退放电为 I3 矩常数和端点 Directional Balance 的推论；第 350--353 节已把 I2 自适应分层放电为贪心分层/Single-Prime CRTDefect 二分；第 354--359 节把小素包压缩为 `q=2` 奇数骨架，并将唯一剩余核心定理化为 I3-Core：真实剩余 SC2/CRTDefect 相关定理。当前未完成无条件化。 |

| 二次筛Zero Mass义务修正 | 更稳路线 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 309--314 节。逐行审查发现用三阶矩直接证明 `M1>=0.58,M2>=0.28` 不够稳；改为 C'：加权 Bonferroni 直接证明 `sum X_B 1_{R=0}/sum X_B>=0.30`。模型值约 `0.604`，只需一阶命中、SC2二阶下界、三阶尾部三个矩估计，余量更大。 |

| 二次筛C'矩估计逐行 | 参数优化/待正式矩证明 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 315--319 节。将有效层均值从 `nu=1/2` 调整为 `nu=0.45`，C' 常数更宽松：一阶 `<=0.50`，二阶 `>=0.05`，三阶 `<0.03`，合并 `rho0>=0.52` 理论空间，远超所需 `0.30`。剩余为正式证明二阶下界和三阶上界的固定阶局部交叉矩估计。 |

| 二次筛C'矩闭合推进 | 常数闭合/剩三线形式化 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 320--323 节。对 `nu=0.45`，二阶主项 `nu^2/2=0.10125`，扣 `0.03` 仍 `>0.05`；三阶主项 `0.0152`，若退化三线 `<0.01` 则 `<0.03`。C' 给 `rho0>=0.52`。为更稳可最终取 `nu=0.4`，二阶仍够、三阶余量更大；剩余为三线退化估计形式化。 |

| 二次筛三线退化估计 | C'闭合 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 324--330 节。最终取 `nu=0.4`：重合退化通过互异线定义为 0；双同步退化由45-Main残余 `<0.02` 给 `<0.008`；三重共块由K=3局部交叉 polylog 复杂度给 `<0.005`。三阶总项 `<0.02567<0.03`，C' 得 `rho0>=0.57`，审稿义务 C' 闭合。 |

| 二次筛A/B最终缺口审查 | 不可无条件并入/缺口缩减 | `docs/archive/monograph-reviews/two-point-secondary-sieve-gap-audit-2026-05-01.md` 已新增。顶刊标准下原有 G1--G7 缺口；其中 `Q_eff<=polylog` 形式化已由第 340--344 节闭合。剩余重点为真实剩余/分层出口、SC2二阶相关与45-Main、小素有限包、Zero Mass/平滑回退以及固定 `w` 量词边界。 |

| G1补正工作台 | 未闭合/压缩为局部条件均衡 | `docs/monograph/two-point-gap-closure-workbench.md` 已新增。G1 真实剩余支撑不能用普通低阶权重绕过；最直接权重 `1_U` 真实支持但难计算。当前最小硬点压缩为“局部条件均衡引理”：真实二次筛剩余集 `U_Y` 对固定阶局部测试函数保持均衡，误差不依赖完整 CRT 周期。 |

| G1局部均衡强度审查 | 强下界不可直接闭合 | `docs/monograph/two-point-gap-closure-workbench.md` 已补充 G1.6--G1.9。局部条件均衡的下界方向接近强筛余项/parity barrier，不能直接无条件宣称。可行补正是 G1-Dichotomy：若真实剩余质量避开 Zero/低覆盖块，则产生 SC2/CRTDefect 异常。G1 需与 G2 合并处理。 |

| G1-G3合并补正 | 压缩为真实块协方差引理 | `docs/monograph/two-point-gap-closure-workbench.md` 已补充 G2.1--G2.4。G1真实支撑与G2真实块下界可合并：若真实剩余避开Zero/低覆盖块，则它与下一层覆盖函数产生异常正协方差；该协方差应由SC2/CRTDefect控制。因此G1--G3最小共同硬点为“真实块协方差引理”。 |

| 真实块协方差引理 | G1-G3实质闭合/需上界筛陈述 | `docs/monograph/two-point-gap-closure-workbench.md` 已补充 G3.1--G3.5。若真实剩余避开 Zero 块，则至少 70% 质量在 `R_B>=1` 块，给 `sum U_B R_B>0.70|U|`；而下一薄层上界筛给 `sum U_B R_B <=(nu+o(1))|U|`，取 `nu=0.4` 矛盾。因此 Zero 块真实质量 `>=0.30|U|`。G1-G3压缩为标准上界筛输入。 |

| 新模平均上界筛 | G1-G3闭合输入 | `docs/monograph/two-point-gap-closure-workbench.md` 已补充 G3.6--G3.10。点态新模均衡过强，但薄层平均上界足够：`sum_{x in U_Y}D_j(x)<=(nu+o(1))|U_Y|`。通过换元 `x=pm` 归为二禁类上界筛，属于 Selberg/Brun 上界方向，不触及下界筛/parity barrier。接受该输入后 G1--G3 闭合。 |

| G4三线退化补正 | 归约到45-Main与G5 | `docs/monograph/two-point-gap-closure-workbench.md` 已补充 G4.1--G4.5。三线退化分解为 `T_rep=0`、`T_pair<E_sync*nu<0.008`、`T_tri<0.005`。G4 无独立新缺口，依赖 45-Main 同步残余 `<0.02` 与 G5 固定阶三线 `Q_eff<=polylog`。 |

| G5固定阶Qeff补正 | 技术闭合 | `docs/monograph/two-point-gap-closure-workbench.md` 已补充 G5.1--G5.3。固定阶矩只展开截断权重 `d<=R<=polylog(P)` 和局部测试，故 `Q_eff,k<=R^k L^{O(k)}<=polylog(P)`。真实 `U_Y` 不展开完整CRT，只作支持集合；新模命中用上界筛处理。G5 闭合。 |

| I1固定阶局部交叉内联证明 | 已闭合 | `docs/monograph/two-point-secondary-sieve-research.md` 第 340--344 节新增正式对象、局部 CRT 计数引理、有效复杂度定理和窗口阈值接口。结论：任意固定阶 `k` 的 `Q_eff,k <= (log P)^{C_k}`；特别 `k=2,3` 可直接用于窗口压缩与 Zero Mass 三线尾部。 |

| I4 Zero-Mass 与平滑回退放电 | 已降级为 I3 常数接口 | `docs/monograph/two-point-secondary-sieve-research.md` 第 345--349 节新增加权 Bonferroni 放电与平滑夹逼证明。若 I3 给出 `M1<=0.45`, `M2>=0.05`, `M3<=0.03` 和端点 Directional Balance，则推出 `rho0>=0.57>0.30` 与 `E_smooth<0.03`。I4 不再作为独立结构输入。 |

| I2 自适应分层与单素数缺陷二分 | 已降级为 I3 CRTDefect 接口 | `docs/monograph/two-point-secondary-sieve-research.md` 第 350--353 节新增贪心分层引理。若所有单素数真实命中 `a_p<=0.05`，则可分层使 `nu_j^real<=0.4`；若某 `a_p>0.05`，则出现 Single-Prime CRTDefect，归入 I3 排除。 |

| G6-G7补正与G1-G7总表 | 缺口压缩完成 | `docs/monograph/two-point-gap-closure-workbench.md` 已补充 G6.1--G7.2 与总表。G6 由平滑夹逼端点层 `O(Delta)+o(1)` 闭合；G7 通过固定偶数 `w` 量词闭合，不声称均匀 `w` 版本。G1--G7 现压缩为两个正式输入：新模平均上界筛与 45-Main 同步残余 `<0.02` 的正式证明。 |

| H1新模平均上界筛逐行审查 | 修正为自适应分层 | `docs/monograph/two-point-gap-closure-workbench.md` 已补充 H1.1--H1.7。逐行审查发现预设薄层平均 `<=0.4` 不能仅由上界筛推出，否则隐含 `|U_Y|` 下界。修正为按真实命中量自适应切薄层，使每层真实平均 `<=0.4`；若单素数贡献过大，则作为大因子集中 CRTDefect 出口。H1 不再依赖下界筛。 |

| H2同步残余逐行审查 | 中大q闭合/小q有限包 | `docs/monograph/two-point-gap-closure-workbench.md` 已补充 H2.1--H3。对中大 `q>Q0`，主同步 `q|h` 在辅助素 `r≈L` 上支撑仅 `O(L/q)` 类，辅助能量下界与均匀上界差距约 `q` 倍；取 `Q0=100` 后 Directional/Endpoint 误差可压到 `<0.02`。小 `q<=Q0` 进入有限包。最终只剩自适应分层单素数集中出口与小q有限包明细。 |

| H4-H6最终补正 | 逻辑缺口压缩为文稿工程义务 | `docs/monograph/two-point-gap-closure-workbench.md` 已补充 H4--H6。自适应分层中的单素数大贡献定义为 Single-Prime CRTDefect，可由辅助投影能量处理；小 `q<=100` 作为有限包，`q=2` 归入奇数骨架，奇素 `q|w` 峰值更弱。G1--G7 当前不再有新的逻辑类型缺口，剩余为正式稿中添加该出口、有限包表和自适应分层表述。 |

| 正式稿工程义务完成 | 已并入正式研究稿/合著条件章节 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 331--334 节：Single-Prime CRTDefect 出口、自适应真实命中分层、小 `q<=100` 有限包表。`paper/contradiction-field-monograph/contradiction-field-monograph.tex` 已同步更新条件命题四输入和参数为 `nu_j^real<=0.4`。LaTeX 编译通过。 |

| 二次筛窗口压缩版 | 条件加强/剩余I3-Core | 新增 `docs/monograph/two-point-window-compression-and-unconditionality.md`，并在 `docs/monograph/two-point-secondary-sieve-research.md` 第 335--359 节写入窗口压缩审查、I1 内联证明、I4 放电证明、I2 分层二分和 I3-Core 定理化。当前方法在 I3-Core 成立时，可把后半窗口从约 `P/2` 行压缩到 `H_min^cond(P;eps)=ceil((C_Q/eps)P^{1/2}(log P)^C)` 行；渐近写法为 `ceil(P^{1/2}(log P)^{C_*})`, `C_*>C`。I3-Core 尚未逐行无条件证明。 |

| I3-Core 压力测试 | 未闭合/需 TRC 新定理 | `docs/monograph/two-point-secondary-sieve-research.md` 第 360--365 节新增局部 CRT 反例模型 `U^*`。该模型满足旧二禁类、短窗不可复用和局部 CRT 复杂度，却集中在新素数坏类上，说明现有刚性不能形式推出 I3-Core。剩余核心升级为 TRC（True Residual Correlation）：真实剩余集对新薄层的单素数坏类、二阶矩、三阶尾部和端点方向均衡。 |

| TRC-1 单素数均衡攻坚 | 低尺度可证/最终尺度未闭合 | `docs/monograph/two-point-secondary-sieve-research.md` 第 366--370 节新增筛余算术级数形式。若二维下界筛在尺度 `Y` 上可用，即 `Y<=N^{1/beta_2-o(1)}`，则 TRC-1 由分子上界筛与分母下界筛推出；但最终窗口 `N~P^{3/2}`、`Y=P^{3/4}` 给 `s=2+o(1)`，低于二维下界筛阈值，故最终仍需几何增强版 TRC-1G。 |

| TRC-1G-H 重原子攻坚 | 压缩为 LDB/NMFB | `docs/monograph/two-point-secondary-sieve-research.md` 第 371--381 节已把原 `0.05` 单素数阈值放宽为足够的 `0.4` 重原子排除，并严格证明：若某新素数坏类承载 `>40%` 的真实剩余质量，则必产生非零新模 Fourier 系数 `>1/5`，等价地产生 `0,\pm w mod p` 三差值长方向能量超标。旧方阵刚性已剥离短方向、45度锁、Reuse/Shared 与端点层；唯一剩余压缩为 LDB(p)/NMFB：真实二次筛剩余集在每个新模 `p>Y` 的长方向族上没有常数级能量集中。该输入尚未无条件证明。 |

| 二次筛总覆盖容量路线 | 最弱充分条件/未闭合 | `docs/monograph/two-point-secondary-sieve-research.md` 第 382--387 节新增 TLI（Total Large-Incidence bound）。不再要求逐点排除每个新素数重原子，只需证明 `sum_{P^alpha<p<=P} A_p < |U_{P^alpha}|`。模型主常数为 `2log(1/alpha)`；取 `alpha=3/4` 时为 `2log(4/3)=0.57536...`，余量 `1-2log(4/3)=0.42463...`。若 TLI 证明成立，则直接存在不被任何 `p<=P` 命中的 `x`，从而 `x,x-w` 为素数。当前 TLI 仍需真实剩余集的大素数命中总均衡，尚未由普通筛法或旧局部刚性无条件推出。 |

| TLI直接证明审查 | 压缩为 RB-TLI/未闭合 | `docs/monograph/two-point-secondary-sieve-research.md` 第 388--394 节已逐行展开 TLI 直接证明尝试。分子 `sum A_p` 可由换元 `x=pm` 与二维上界筛控制，主项为 `2C_+ log(1/alpha)|I|V_2(Y)`；真正卡点是分母 `|U_Y|` 的模型级下界。取 `alpha=3/4` 时需常数门槛 `C_+/c_-<1/(2log(4/3))=1.738...`。最终最小新增输入命名为 RB-TLI：真实剩余集的大素数总命中平均不超过 `2log(4/3)+eta_RB`，且 `eta_RB<0.42463...`。RB-TLI 尚未无条件证明；当前不能宣称二次筛命题无条件闭合。 |

| `q|w` 局部塌缩刚性 | 已纳入/不闭合RB-TLI | `docs/monograph/two-point-secondary-sieve-research.md` 第 395--400 节新增分析。若奇素 `q|w`，二禁类 `{0,w}` 合并为一禁类，局部密度由 `1-2/q` 改为 `1-1/q`，相对最硬情形增益 `(q-1)/(q-2)`；固定 `w` 后形成有限奇异因子。该刚性增大绝对候选密度、削弱小素同步峰、改善有限阈值。但对 TLI/RB-TLI 的相对主项，分子 `A_p` 与分母 `|U_Y|` 同乘正确的 `V_w(Y)`，故主常数仍为 `2log(1/alpha)`，取 `alpha=3/4` 仍是 `2log(4/3)`。最硬全称情形仍为 `w=2`，RB-TLI 尚未因此无条件闭合。 |

| `w=2` RB-TLI数值刚性 | 新框架BST/未闭合 | 新增 `experiments/rb_tli_w2_scan.py`，并生成 `docs/rb-tli-w2-scan.md`、`docs/rb-tli-w2-scan.json`、`docs/rb-tli-w2-scan-large.md`、`docs/rb-tli-w2-scan-large.json`。`docs/monograph/two-point-secondary-sieve-research.md` 第 401--407 节记录实验与新刚性：当 `alpha>2/3` 时，任意大因子命中 `p|x` 或 `p|(x-2)` 都强制互补商为素数，故命中等价于素商半素数转移。真实均值不服从 naive `2log(1/alpha)`，而服从 Buchstab 条件主常数 `K(alpha)=2log((2-alpha)/alpha)/(1+log((2-alpha)/alpha))`。实验：`alpha=3/4, P=10007` 得 `E_U D=0.691696`, `K=0.676220`, `D=0` 比例 `0.458678`；`alpha=0.80` 得 `E_U D=0.589679`, `K=0.576984`；`alpha=0.85` 得 `E_U D=0.477321`, `K=0.464233`。最终硬点升级为 BST（二点 Buchstab 半素数转移稳定性），尚未无条件证明。 |

| BST误差细分审查 | 压缩为BST-2/未闭合 | `experiments/rb_tli_w2_scan.py` 已增强壳层与两侧协方差指标，`docs/rb-tli-w2-scan-large.md` 更新结果。`docs/monograph/two-point-secondary-sieve-research.md` 第 408--413 节记录新刚性：`P=10007, alpha=3/4` 各壳层实际命中与 Buchstab 壳层期望接近；两侧协方差约 `-0.000093`；`D=0` 个数在 `alpha=0.75,0.80,0.85` 下均为 `201481`，说明最终幸存集与截断无关；端点类型在 `alpha>2/3` 下严格为“素数/单半素数/双半素数”三类。最后硬点进一步压缩为 BST-2：证明移位双素变量 `pm-2` 的 `Y`-rough 稳定性，即二点条件不造成 Buchstab 半素数主项常数级正放大。 |

| BST-2最终改写 | 压缩为BMD/未闭合 | `docs/monograph/two-point-secondary-sieve-research.md` 第 414--420 节新增直接攻坚。BST-2 被改写为双素变量 `(p,m)` 上的一维乘法筛：旧素数 `q<=Y` 的禁曲线为 `pm≡2 mod q`，在 `(F_q^*)^2` 中局部禁比例为 `1/(q-1)`。由此 Buchstab 主项来自乘法筛，而非 naive 独立模型。最后最小输入命名为 BMD（Biprime Multiplicative Dispersion）：双素变量在 `pm≡2 mod d` 乘法曲线上的 Rosser/Buchstab 加权分布误差为 `o(|U_Y|)`。若 BMD 成立，则 BST-2、BST、TLI 依次闭合；BMD 尚未无条件证明，属于双素 Type-II/dispersion 级估计。 |

| BMD行列输入审查 | 压缩为BMD-Char/条件辅助 | `docs/monograph/two-point-secondary-sieve-research.md` 第 421--425 节补充审稿边界：若把前文行列素数命题作为条件输入，它只能排除完整 CRT 局部块中的零行/零列/零截面退化，形成 BMD-Zero；它不能控制非主乘法角色的有符号谱偏差。BMD 被进一步分解为 `BMD-Zero + BMD-Char`，其中 `BMD-Char` 是双素变量角色和 `sum_{d<=D} |lambda_d|/phi(d) sum_{chi!=chi0} |sum_p chi(p) S_p(chi)| = o(|U_Y|)`。因此行列输入可作为辅助刚性，但不能直接证明 BMD；当前真正剩余硬点是 BMD-Char。 |

| BMD直接硬攻 | 归约到BV-E2/可标准引用闭合 | `docs/monograph/two-point-secondary-sieve-research.md` 第 426--431 节把 BMD 改写为受限二素数卷积 `a_n=#\{(p,m):Y<p<=P,m prime,n=pm\}` 在奇平方自由模算术级数中的 Bombieri--Vinogradov 平均分布；模 `2` 已确定剥离。若引用标准 BV-`E_2` 定理：`sum_{d<=P/log^B P} max_a |sum_{n≡a(d)}a_n - phi(d)^{-1}sum_{(n,d)=1}a_n| <<_A N/log^A N`，则对 Rosser/Buchstab 权重立即得 `sum lambda_d R_d=o(|U_Y|)`，因为 `|U_Y|~N/log^2 P`。参数窗口 `2/3<alpha<1` 同时保证商数素性刚性和 `Y<P/log^B P`。若不允许外部引用，则唯一剩余义务是内联证明 BV-`E_2` 附录。 |

| BV-E2自足化附录 | 最小硬点BE2-3 | 新增 `docs/monograph/bv-e2-appendix.md`，并在 `docs/monograph/two-point-secondary-sieve-research.md` 第 432--435 节接入。附录证明 BV-E2 推出 BMD，并明确普通乘法大筛在平衡块 `P_1≈M_1≈P`, `Q≈P/log^B P` 只给 `P^3/log^{2B}P`，目标却是 `P^2/log^A P`，差一个 `P` 量级。因此自足版唯一真正深点是 `BE2-3`：平衡 Type-II dispersion / Kloosterman cancellation。引用版可用 BFI/Motohashi 型外部定理闭合；完全自足版需逐行证明 BE2-3。 |

| BE2-3无黑箱化 | 压缩为BE2-3K | `docs/monograph/bv-e2-appendix.md` 第 7--9 节与 `docs/monograph/two-point-secondary-sieve-research.md` 第 436--439 节继续硬攻：BMD 不需完整 `max_a` BV-E2，只需固定剩余类 `2 mod d` 与 well-factorable Rosser/Buchstab 权重的 WBE2。对平衡 Type-II 块展开 dispersion，Cauchy 后归结为 `sum_r |T_r|^2` 方差界；非对角 CRT 条件 `rs1≡2(d1), rs2≡2(d2)` 产生双 Kloosterman 相位。最终最小无黑箱核命名为 `BE2-3K`：weighted bilinear Kloosterman dispersion。若 BE2-3K 成立，则 `BE2-3K=>BE2-3=>WBE2=>BMD`。 |

| 顶刊审稿最终状态 | 尚未完全无黑箱 | `docs/monograph/two-point-secondary-sieve-research.md` 第 440 节新增最终审稿结论：BMD 已严格归约到唯一深核 `BE2-3K`，但本文尚未在文内证明该 Kloosterman 双线性平均定理。若引用 BFI/Deshouillers--Iwaniec/Kuznetsov 型工具，则 BMD 可作为外部输入版闭合；若坚持完全无黑箱，则剩余唯一任务是证明 `BE2-3K`。不得把当前稿标为“完全无黑箱证明”。 |

| BE2-3K继续硬攻 | 压缩为KLS-window | `docs/monograph/bv-e2-appendix.md` 第 10--15 节与 `docs/monograph/two-point-secondary-sieve-research.md` 第 441--445 节继续细化。点态 Weil 界在平衡区间只给单模平方根抵消，不能提供任意 `log^{-A}`；`(d1,d2)>1` 的 gcd 层由 `s1≡s2 mod g` 带来 `1/g` 稀疏因子，只造成多对数损失；well-factorable 权重分解是必须结构。最终剩余核进一步定位为 `KLS-window`：窗口化 Kloosterman 谱大筛。逻辑链为 `KLS-window=>BE2-3K=>BE2-3=>WBE2=>BMD`。 |

| KLS外部引用闭合 | 外部深定理版闭合/非完全自足 | `docs/monograph/bv-e2-appendix.md` 第 16--19 节与 `docs/monograph/two-point-secondary-sieve-research.md` 第 446--447 节补充 KLS-source 定理包。KLS-window 精确关联到 Deshouillers--Iwaniec 的谱 Kloosterman 大筛与 Bombieri--Friedlander--Iwaniec 的 dispersion/well-factorable 权重框架。变量匹配为 `d,c` 对 Kloosterman 模数，`h` 对加法频率，`s` 对逆元变量，`lambda_d` 对 well-factorable 权重。链条为 `DI+BFI=>KLS-window=>BE2-3K=>BE2-3=>WBE2=>BMD`。因此二点筛 BMD 达到外部深定理版闭合；若要求完全自足，仍需重证 DI/BFI。 |

| 合著目录与理论系统总览 | 已整理/审稿辅助 | 新增 `docs/monograph/combined-monograph-directory-and-theory-system.md`，并在 `paper/contradiction-field-monograph/contradiction-field-monograph.tex` 增加 `Directory and Theory System` 章节。总览把合著稿分为五部：统一矛盾场方法、方阵行列程序、二点筛程序、RH 反例矛盾场、统一依赖图与优化方向；并明确二点筛最新链条、状态等级、优化方向和禁止过度声明边界。 |

| 外部定理引用索引 | 已建立/待主稿模板化 | 新增 `docs/monograph/external-theorem-index.md`，列出 DI、BFI、BV-E2、Vaughan/Heath-Brown、Kuznetsov、explicit formula、BG/Baker 等外部输入的用途、状态、适用条件和误用风险。最新补充 KLS-window 变量适配核查表：相位、模数、频率、逆元变量、well-factorable 权重、gcd 层、端点平滑和 `B(A)` 吸收账本。 |

| 关键证明链条优化审查 | 已新增/全稿状态清洗依据 | 新增 `docs/monograph/key-proof-chain-optimization-audit.md` 与归档 `docs/archive/monograph-reviews/monograph-key-chain-optimization-audit-2026-05-02.md`。该审查把主线压缩为 `PM-1..PM-8`、`TP-1..TP-9`、`RH-1..RH-5` 三条链，并明确：二点筛是外部深定理版闭合，完全自足版仍卡在 KLS-window；方阵链条需聚焦 Structured-EHPD；RH 链条不能宣称无条件证明。 |

| 广义斜率小素锁与粗数补洞 | 新增/结构层闭合，分布层未闭合 | 新增 `docs/monograph/generalized-slope-locks-and-rough-hole-limits.md`。将 `45°` 的 `P±1` 锁扩展为 `P±t`：若 `q|k` 且 `q|P±t`，非绕回算术段 `k+(P±t)l` 全由 `q` 标记；允许 `1<=t<=T` 可组织所有 `q<=T+1` 的小素因子层。最新补强圆柱螺旋公式：绕回轨道持续延续，但整数值为等差主项加绕回次数余项；每个绕回相位块是同余常数块，可用显式长度 `ell_u(a,t)` 计算锁定覆盖。最终硬点压缩为粗数带大因子总命中不等式 `B_Y(I)<|G_Y(I)|`，模型常数为一维 `log(1/alpha)`、二点筛 `2log(1/alpha)`。 |

| 三主线无条件化优化审查 | 新增/优化路线明确，未升级终局声明 | 新增 `docs/monograph/unconditionality-optimization-audit.md`。结论：方阵行列最优路线是 `GSL=>PM-R1/PM-R2=>RHI`，存在形式参数窗口 `e^{-1}<alpha<1/2`；二点筛必须严格审查 `BMD=>BST-2=>BST=>TLI` 是否隐藏筛余下界/parity barrier，不能把 BMD 子接口闭合等同于孪生素数型终局；RH 方向应把 controlled exits 写成四列表并尝试正性二次型化，仍保持 `Not claimed`。 |

| PM-RHI 工作台 | 新增/PM-R2B 成为最小硬点 | 新增 `docs/monograph/pm-rhi-workbench.md`。将方阵行列 RHI 路线拆成 `PM-R1` 短窗口粗数下界与 `PM-R2` 粗数带大因子补洞上界。审查结论：`PM-R1` 在 `alpha<1/2` 下是标准线性筛可攻部分；`PM-R2` 需利用互补商也 `Y`-rough 的结构，分为可筛段 `Y<p<=P/Y` 与尾段 `P/Y<p<=P`。普通筛法不能自动闭合尾段，最小硬点是 `PM-R2B` 尾段锚定上界。 |

| PM-R2B 尾段锚定 | 新增/压缩为 PTA 引理 | 新增 `docs/monograph/pm-r2b-tail-anchor-workbench.md`。尾段经除数切换写为粗互补商 `m` 上的短素数区间平均：`T(M)=sum_{m~M,P^-(m)>Y}(pi((X+H)/m)-pi(X/m))`。纯几何尾锚只给每个 `m` 至多 `O(1)` 命中，缺少 `1/log P` 素数密度因子；因此最小硬点压缩为 `PTA`：粗锚平均上的素数尾命中不超过 `H/(m log P)` 模型主项，异常需导入圆柱相位块、短窗不可复用、CRT 均衡或 Tail anchors。 |

| 最新刚性闭合优化 | 新增/压缩为 PTA-GSL 与奇异因子账本 | 新增 `docs/monograph/latest-rigidity-closure-optimization.md`。整合扩展斜线层锁与 `q|w` 二禁降一禁：GSL 可把 `p` 变量中 `q<=sqrt(P)` 的合数层也几何标记，故 `PM-R2B` 最小硬点强化为 `PTA-GSL`，即 GSL 删除小素层后 `p` 候选在粗锚平均上有 `1/log P` 上界；二点筛中 `q|w` 给奇异因子增益 `prod_{q|w}(q-1)/(q-2)`，改善常数但不改变最硬 `w=2` 的主障碍。当前仍不能宣称终局无条件闭合。 |

| PTA-GSL Selberg 硬攻 | 新增/压缩为 BSI | 新增 `docs/monograph/pta-gsl-hard-attack.md`。直接展开 `PTA-GSL` 的 Selberg 上界筛：`T(M)` 化为 `N_ell(M)=sum_{m~M,P^-(m)>Y}(floor((X+H)/(ell m))-floor(X/(ell m)))`。主项为 `H/ell sum 1/m`，平凡 `O(1)` 余项过大；因此最小硬点进一步压缩为 `BSI`：在 Selberg 二次权平均中控制粗锚双线性短区间地板函数余项。链条为 `BSI+GSL=>PTA-GSL=>PM-R2B=>RHI`。 |

| BSI sawtooth 硬攻 | 新增/压缩为 RSE 与筛水平张力 | `docs/monograph/pta-gsl-hard-attack.md` 已新增第 11--16 节。把 BSI 的地板函数余项用 sawtooth/Vaaler 展开，得到粗数倒数指数和 `S_{h,ell}(M)=sum_{m~M,P^-(m)>Y} e(hX/(ell m))(1-e(hH/(ell m)))`。相位总变化约 `hP_m/ell`，故振荡需要 `ell<<hP_m`；而 Selberg 筛水平给 `ell<=R^2`。新核心张力为 `R<=P^{(1-alpha)/2}` 有利于倒数相位抵消，但可能削弱 `1/log P` 主常数。最小接口进一步压缩为 `RSE`：Selberg 二次权平均下的粗数倒数指数和估计。 |

| 三命题闭合优化矩阵 | 新增/统一三链最小接口 | 新增 `docs/monograph/three-proposition-closure-optimization.md`。该矩阵把 PM、TP、RH 分别压缩为 `QLOW-MID-COMP(intervalized)+RRD+OSPC`、`BMD-to-TLI no-hidden-lower-bound`、`controlled exits four-column ledger`。结论：PM 的紧区间常数证书是当前最窄可攻点，且外向舍入预算已量化；TP 不能把 BMD 外部闭合直接等同于素数对终局；RH 仍保持 `Not claimed`。 |

| 外审前最硬剩余义务总表 | 已新增/主稿已接入 | 新增 `docs/monograph/pre-external-referee-remaining-obligations.md`，并在 `paper/contradiction-field-monograph/contradiction-field-monograph.tex` 增加 `Pre-External-Referee Hard Obligations` 小节。该表把当前所有最硬剩余逐项归入唯一审稿义务链：Prime Matrix 的 `Structured-EHPD/PDEC/SAE/Rankin/RRD/OSPC`，二点筛的 `I3-Core/DI-BFI适配/BMD=>TLI`，RH 的 controlled exits。结论保持诚实边界：作者侧已完成状态归档和阻塞接口压缩，但未把未证深命题伪装为无条件终局。 |

| 未闭合硬项攻坚路线图 | 已新增/逐项补充可行性方案 | 新增 `docs/monograph/unclosed-hard-obligations-attack-roadmap.md`。该路线图对 H1--H10 逐项给出精确证明目标、可用刚性、最小补正动作、可行性评级与失败时状态。优先级明确为：先做 `H7/H3/H10/H1` 的外审工程闭合，再攻 `H5/H4/H2` 的 PM 数学接口；`H6/H8/H9` 保持条件/verification 状态，除非新增真正深证明。 |

| BPN-LHB 证书复现账本 | H3已完成/外审复现包 | 新增 `docs/monograph/prime-matrix-bpn-lhb-certificate-reproduction-ledger.md`，列出低范围、窄带、尾段有限、显式尾段四组证书的脚本、JSON/Markdown 输出、验收标准和临时目录复现命令。本轮已修正窄带与显式尾段脚本的报告文字，使 8 个生成文件均可与仓库内对应文件字节级一致。该项闭合 BPN-LHB 子模块复现义务，但不升级 Prime Matrix 全局行列命题。 |

| KLS-window DI/BFI适配模板 | H7外部深定理版闭合 | 新增 `docs/monograph/kls-window-di-bfi-adaptation-template.md`，把 `DI+BFI=>KLS-window=>BE2-3K=>BE2-3=>WBE2=>BMD` 写成可审稿适配链。模板逐项核验 CRT 相位到标准 Kloosterman 逆元相位、模数族、频率族、逆元变量、well-factorable 权重、gcd strata、端点平滑和 `B(A)` 对数损失吸收。该项只闭合 BMD 的外部深定理输入，不闭合 `BMD=>TLI`，也不把二点筛终局或孪生素数命题升级为无条件证明。 |

| 命题状态纪律 | H10状态工程完成第一版 | 新增 `docs/monograph/claim-status-discipline.md`，固定 `Proved-in-text`、`Reduction-closed`、`External-theorem closed`、`Computational-certificate`、`Referee-block`、`Not claimed` 六类状态的允许结论、必须附件、禁止越界和升级条件。主稿同步新增六类状态专用 theorem-like 环境，并在 `Claim Status Legend` 中补入 `Computational-certificate`。该项不升级任何数学终局，只防止条件链被误写成无条件定理。 |

| Prime Matrix A/B入口定理清单 | H1入口归约闭合 | 新增 `docs/monograph/prime-matrix-ab-entrance-theorem-list.md`，把行/列反例入口整理为 `AB1--AB6`、`Theorem A`、`Theorem B`、`Corollary AB`，并固定小因子锁定、45度小因子锁定、Tail-log4尾部锚、主体双粗锚的剥离优先级。主稿中的 A/B reduction 已改用 `Reduction-closed Statement`。该项只完成反例到 `Structured-EHPD` 的入口归约，不证明 `Structured-EHPD` 不存在。 |

| H5 RRD/OSPC验收矩阵 | 六项硬义务已定式化 | 新增 `docs/monograph/h5-rrd-ospc-proof-obligation-matrix.md`，把 `RRD/OSPC/SelbergUniform/round` 常数接口拆成 `RRD-low<=0.006`、`RRD-perp<=0.012`、`RRD-conversion<=0.002`、`OSPC<=0.020`、`SelbergUniform<=0.008`、`round<=0.003` 六项。文件给出 `H5-Acceptance`：六项成立则总损失 `0.051<0.053369509758272926`。当前 H5.1 路由与 H5.4 出口吸收已完成；H5 仍未闭合，最小硬点转为 H4 的 `PDEC-Cert/SAE-Cert` 与 H5.2 的 `RRD-perp` 同权上界。 |

| H5.1 RRD-low出口定理 | 路由闭合/出口未排斥 | 新增 `docs/monograph/h5-1-rrd-low-exit-theorem.md`。该文件定义 `weighted CRTDefect` 阈值 `0.005366563145999495`，并用块级 Cauchy--Schwarz 证明：若无 `OSPC*` 且无 `weighted CRTDefect`，则 `|E_low|<=0.006`；等价地，`RRD-low` 超预算必进入 `OSPC*` 或 `weighted CRTDefect`。该项只闭合 H5.1 的出口路由，不排除这些出口；下游仍需 H5.4/H4 的 `PDEC-or-SAE` / Tail-anchor 排斥。 |

| H5.4 OSPC/weighted CRTDefect吸收 | 吸收到H4/出口未排斥 | 新增 `docs/monograph/h5-4-ospc-weighted-crtdefect-absorption.md`。该文件证明 `OSPC*` 与 `weighted CRTDefect` 都可写成零均值低模测试函数上的命名缺陷，并由统一 `PDEC-or-SAE` 二分进入 persistent Fourier/CRT 缺陷或 sparse 单窗逃逸义务。该项只完成出口吸收；仍未提交 `PDEC-Cert` 或 `SAE-Cert`，所以 Prime Matrix 终局不升级。 |

| H3-HLC GHLC-D闭合 | KZ-D分支闭合/剩KZ-B,KZ-E | 新增 `docs/monograph/prime-matrix-h3-dsb-hlc-ghlc-d-local-schur-closure.md`。该文件证明 generic hyperbolic 局部相关不能用点态格点数硬估，而应在预迹积分核层使用局部 `L^1` 核质量与 Schur 检验：`T^2∫_0^{T^{-1}log^B y}(1+Tr)^{-A}sinh r dr=O(1)`。因此 `GHLC-D=>LPC-D=>PTK-D=>KZ-D`。该条已被后续 KZ-B 闭合条目进一步推进；历史状态保留。 |

| H3-HLC KZ-B闭合 | 完全自足链剩KZ-E | 新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kz-b-kuznetsov-trace-specialization.md`。该文件把 Kuznetsov trace formula 的本文专门化从 automorphic kernel、Poincare 包 unfolding、双陪集 Kloosterman 几何侧、谱 Plancherel 侧和 Bessel 变换归一化逐项推出。KZ-B 只闭合公式转换；`log^{-A}` 节省仍完全落在 `KZ-E` BFI/well-factorable dispersion。 |

| H3-HLC KZ-E攻坚 | 压缩为WFD-core/未闭合 | 新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kz-e-well-factorable-dispersion-spine.md`。该文件内联 well-factorable 卷积分解、dispersion 方差恒等式、CRT 到标准 Kloosterman 相位的归一化、gcd 相容层和端点平滑账本，并证明 `WFD-core=>KZ-E`。当前完全自足链唯一剩余为 `WFD-core`：窗口化 well-factorable Kloosterman dispersion 平均估计；未证明前不得宣称 `SC-9/CORE-5/HLC` 完全自足闭合。 |

| H3-HLC WFD平方根平衡化 | 压缩为BWFD-core/后续再压缩 | 新增 `docs/monograph/prime-matrix-h3-dsb-hlc-wfd-core-balanced-factor-reduction.md`。该文件用平方根 well-factorable 分解把 `lambda_c` 写成 `c=uv` 且 `u,v≈c^{1/2}`，剥离 gcd 多对数层，并用 CRT 把 `e_{uv}(as+b\\bar s)` 因子化为双模数相位，证明 `BWFD-core=>WFD-core=>KZ-E`。该步当时剩余为 `BWFD-core`；后续谱完成攻击已进一步压缩为 `BSC-core`。 |

| H3-HLC BWFD谱完成攻击 | 压缩为BSC-core/后续再压缩 | 新增 `docs/monograph/prime-matrix-h3-dsb-hlc-bwfd-core-spectral-completion-attack.md`。该文件对 `s` 变量作精确有限 Fourier 完成，把不完整逆元相位化为完整 Kloosterman 和，并用 `S(A,B;uv)=S(A\\bar v,B\\bar v;u)S(A\\bar u,B\\bar u;v)` 显示平衡双模数完整核心。文中同时核定：普通 KZ-D 只能给 raw 二范数尺度，点态 Weil 也不给任意 `log^{-A}`；该步当时剩余为 `BSC-core`，后续分数相位攻击已进一步压缩为 `KFLS-core`。 |

| H3-HLC BSC分数相位硬攻 | 压缩为KFLS-core/后续再压缩 | 新增 `docs/monograph/prime-matrix-h3-dsb-hlc-bsc-core-kloosterman-fraction-attack.md`。该文件逐项展开完整 Kloosterman 和，把核心相位显形为 `e(\\bar vR/u+\\bar uT/v)`，并把单侧退化定位为二次同余 `(a_h+ell)x^2+b_h=0 mod u`，给出 CRT 根数包络。该步当时剩余为 `KFLS-core`：balanced Kloosterman-fraction large sieve logarithmic saving；后续平方核硬攻已进一步压缩为 `CFQK-core`。 |

| H3-HLC KFLS平方核硬攻 | 压缩为CFQK-core/后续再修正 | 新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kfls-core-square-kernel-attack.md`。该文件把 `KFLS-core` 的非退化和平方化，显式得到四模数相位差 `bar v R/u+bar u T/v-bar v' R'/u'-bar u' T'/v'`。文件指出全核绝对 Schur 被精确对角层阻断，只能恢复 raw 二范数尺度；该步当时剩余为中心化后的半对角 `(SQK-21)` 与真非对角 `(SQK-23)`。后续块中心化修正已进一步细化为 `BD-CEN + OSQK-core + TFQK-core`。 |

| H3-HLC CFQK块中心化修正 | 压缩为BD-CEN/OSQK/TFQK | 新增 `docs/monograph/prime-matrix-h3-dsb-hlc-cfqk-core-block-centering-attack.md`。该文件把平方核按 `(u,v)` 块拆分，证明同块半对角 `sum_b |S_b|^2` 不能被要求 `log^{-A}` 估小；它必须作为块对角/局部方差由 dispersion 中心化扣除。当前剩余修正为三项：`BD-CEN` 块中心化身份核查，`OSQK-core` 一侧共享模数三模数相关 `(BCF-14)`，以及 `TFQK-core` 真四模数相关 `(BCF-16)`。 |

| H3-HLC BD-CEN身份核查 | BD-CEN未闭合/第一阻断 | 新增 `docs/monograph/prime-matrix-h3-dsb-hlc-bd-cen-dispersion-centering-audit.md`。该文件逐行核查 KZ-E dispersion spine：现有 `(KE-5)` 只给出 `h=0` 主项抵消，即频率方向中心化；它没有给出同 `(u,v)` 块投影扣除 `(BDC-5)`。因此不能在平方核中事后删除 `sum_b |S_b|^2`。当前第一阻断点更新为 `BD-CEN identity (BDC-5)`；`OSQK/TFQK` 只能作为其后的条件义务。 |

| H3-HLC BD-CEN反证分叉 | BD-CEN当前对象下失败 | 新增 `docs/monograph/prime-matrix-h3-dsb-hlc-bd-cen-no-go-route-fork.md`。该文件用单块非零模型严格反证：在当前未块中心化的 WFD/KZ-E 对象和当前 admissible 系数范围内，`BD-CEN identity (BDC-5)` 不是未证引理而是错误身份；`h=0` 投影与块投影不同。该步当时把路线分叉为 `SOURCE-CEN`、`BLK-energy-core` 或外部 DI/BFI；后续两条内部裸出口已进一步核查并收窄为 `NC-BLK`。 |

| H3-HLC SOURCE-CEN反证 | SOURCE-CEN当前对象下失败 | 新增 `docs/monograph/prime-matrix-h3-dsb-hlc-source-cen-no-go.md`。该文件证明当前 `WFD-core (KE-13)` 是未块中心化的线性 Kloosterman 窗口；若在源头替换为同 `(u,v)` 块中心化对象，会改变原始目标并产生必须另估的块均值项。因此 `SOURCE-CEN` 不能作为恒等式闭合 `BD-CEN` 阻断。该步把剩余内部路线收窄为块能量/块非集中输入；后续 `BLK-energy` 核查进一步压缩为 `NC-BLK`。 |

| H3-HLC BLK-energy核查 | 裸BLK-energy数组版失败/剩NC-BLK | 新增 `docs/monograph/prime-matrix-h3-dsb-hlc-blk-energy-core-obstruction.md`。该文件证明裸 `BLK-energy-core` 不能作为平方核层任意系数数组定理成立：单块单原子测试使 `sum_b |S_b|^2` 与 raw 二范数同阶，不能再获得任意 `log^{-A}`。因此无黑箱内部版的真实最窄义务是 `NC-BLK`：从上游实际 Type-I/II、Fourier 与 well-factorable 结构证明块内非集中 `(BEC-12)`；否则 H3-HLC/KZ-E 只能标为外部 DI/BFI 定理版闭合。 |

| C13固定gap密度天花板 | 新增/压缩为LowQ-Layer-HDE | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-density-ceiling-audit.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_density_ceiling_audit.py`。该层证明固定 gap 上界给出端点带密度天花板 `N_g(J)/|J|<=C_FG*S_g/log(Q)^2`，从而若 `C_FG*S_g/log(Q)^2<=eta` 可直接排斥单层高密度。样本 `witness_C=1.2, ceiling_C=1.3, eta=1/25` 中 40/54 层被单层天花板排斥，但最紧低 q 层 `[1366,1498]` 仍需 `C_FG<=1.042465` 才能排斥。因此 C13 高密度出口被压缩为 `LowQ-Layer-HDE`：低 q 端点层需层唯一性/相位互斥、目标族 `C_FG<=1.04`，或 ColumnCRT/stitching 排斥；行命题未因此闭合。 |

| C13低q共享锚压缩 | 新增/压缩为LowQ-Reuse-Cap | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-lowq-overlap-certificate.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_lowq_overlap_audit.py`。在 `witness_C=1.2, ceiling_C=1.3, eta=1/25` 样本中，未被密度天花板排斥的 14 个低 q 层共有 26 个层 witness，但只落在 9 个 q 锚与 12 个固定 gap 素对上，最大共享锚为 `q=1427`、复用 6 次；精确有限计数给出 `actual_high=0`、最小 `eta` 余量 `1.32` 个槽。低 q 分支由此压缩为 `LowQ-Reuse-Cap`：证明同一 q 锚在固定 endpoint residue/side/u 下不能过度复用，或将其接入 ColumnCRT/stitching/有限证书。该步仍不是行命题闭合。 |

| C13低q有限阈值 | 新增/有限化接口闭合 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-lowq-finite-threshold.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_lowq_finite_threshold.py`。证明若 `P>=alpha^{-1} exp sqrt(C_FG*S_g*|M|/eta)`，则固定 gap 密度天花板加层投影鸽巢排斥低 q 高密度；否则只剩有限 `P<P0` 证书。样本 `witness_C=1.2, ceiling_C=1.3, eta=1/25` 输出 `groups=38, accepted=38, high=0, max_density=0.037594, min_eta_slack=0.32`，并给出 `max_pcrit_group=580109.58`。该项把 C13 低 q 分支有限化，但全局仍需目标族 gap 奇异因子上界与 `P<P0` 完整有限验证。 |

| C13 SparseSAE总量付款 | 新增/样本总量闭合 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-sparse-summability-ledger.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_sparse_summability.py`。证明对所有稀疏 envelope 有 `sum atoms(E)<=|M|*eta*sum Omega(E)`。当前压力样本输出 `moving=224, accepted=38, high=0, accepted_slots=215, accepted_env=24029, accepted_capacity=1922.32, moving_over_capacity=0.116526`，说明 SparseSAE 在样本总量层可同时付款。全局仍需 `sum Omega(E)` 的确定性上界与主链预算常数对接。 |

| C13确定性Omega上界 | 新增/减少观测黑箱 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-deterministic-envelope-bound.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_deterministic_envelope_bound.py`。证明每个 group 有确定槽数上界 `Omega(E)<=1+floor((beta max_m|I_m|-epsilon_E)/u_E)`，从而 SparseSAE 付款可完全由窗口长度、步长和残差求和控制。当前压力样本给出 `observed_env=24029, deterministic_env=24641, deterministic_capacity=1971.28, moving_over_capacity=0.113632`。全局剩余为目标族 group 数与 `u` 分布的确定性上界。 |

| C13 group/u分布上界 | 新增/纯几何外壳 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-group-u-distribution-bound.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_group_u_distribution.py`。证明真实 `C13Failure` group 嵌入纯几何候选外壳：`Delta*|r|=g*u`、`u|Delta*|r|`，并有 `sum Omega(E)<=sum_{m,Delta,u}(1+floor(beta Lmax/u))`。当前压力样本四层审计为 `geometric: 612 records/402 groups/env 68241/cap 5459.28`，`positive: 167/105/env 48380`，`narrow: 131/83/env 39750`，`failure: 57/38/env 24641`。该项把 group 数与 `u` 分布从实际 witness 中剥离；全局剩余为对目标窗口族求和并接入最终预算。 |

| C13除数和闭式外壳 | 新增/预算接口压缩 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-divisor-sum-envelope-bound.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_divisor_sum_envelope_bound.py`。将几何 envelope 求和进一步压成 `D_even=sum_{m,Delta,u|Delta|r|}(1+floor(beta L/u))` 与 `D_tau_sigma=sum_{m,Delta}(m-Delta)(tau(Delta|r|)+beta L sigma_{-1}(Delta|r|))`。当前样本 `dedup_env=68241, exact_even=108342, tau_sigma=122294.169, capacity_tau_sigma=9783.53352`，闭式外壳约为去重几何外壳的 `1.792` 倍。剩余硬点压缩为 `C13-DivisorBudget`：在目标窗口族上求和并小于主链预算。 |

| C13预算归一化 | 新增/压缩为Budget-Allocation | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-budget-normalization-ledger.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_budget_normalization.py`。将 `Cap_tau, Cap_even, Cap_fail` 与二阶账本 `D2=M2-B2` 和 `Equal` 对齐。当前样本总量为 `Cap_tau=9783.533520, Cap_even=8667.36, Cap_fail=1971.28, D2=11023.070597, Equal=22817`；比例为 `Cap_tau/D2=0.887551, Cap_even/D2=0.786293, Cap_fail/D2=0.178832`。逐窗口 `p=997` 有 `Cap_even/D2=1.124891`，说明不能逐窗口付款，必须证明全局 D2 池化、继续压低低 p 外壳，或有限证书化。 |

| C13混合预算证书 | 新增/修复低P逐窗口不足 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-hybrid-budget-certificate.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_hybrid_budget_certificate.py`。采用 `P<=1000` 有限几何外壳、`P>1000` 闭式 `D_even` 外壳。当前样本得到 `hybrid_capacity=8227.12, D2=11023.070597, hybrid/D2=0.746355, max_window_hybrid/D2=0.780430`，其中 `p=997` 降为 `0.709157`，`p=5003` 为最紧 `0.780430`。剩余为正式选择 `P_fin`、生成完整低 P 有限证书、证明高 P 统一预算比例并接入主链总预算。 |

| C13低P有限证书 | 新增/高P接口定式 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-lowp-finite-certificate.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_lowp_finite_certificate.py`。对 `P_fin=1000` 的低 P 样本窗口给出有限几何 group 证书：`p=997, records=123, groups=81, slots=9387, capacity=750.96, D2=1058.946880, cap/D2=0.709157`。高 P 义务定式为 `|M| eta D_even <= 0.781 D2`；当前样本 `p=5003` 为最紧 `0.780430`。剩余为证明低 P 窗口清单全覆盖和全局 HighP-D2-Lower。 |

| C13高P D2余量账本 | 新增/HighP-D2-Lower 代数化 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-highp-d2-margin.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_highp_d2_margin.py`。证明高 P 预算条件 `Cap_even<=D2` 等价于 `B2/M2<=1-Cap_even/M2`，即把剩余硬点改写为乘法基线占比必须留出足够二阶正偏差。当前高 P 样本总量 `Cap_even=7476.16, D2=9964.123717, margin=2487.963717, Cap/D2=0.750308`；最紧窗口 `p=5003` 仍有 `margin=677.727367, Cap/D2=0.780430`。该项完成样本余量证书与等价式，不闭合全局；剩余是证明所有 `P>1000` 目标窗口满足 `HighP-D2-Lower` 并接入主链预算。 |

| C13高P固定gap素对下界目标 | 新增/HighP-PLT 精确化 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-highp-pair-lower-target.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_highp_pair_lower_target.py`。证明若低筛后等乘数固定 gap 尾素对数满足 `sum G_m^L >= sum(B2_m+Cap_even_m)`，则 `HighP-D2-Lower` 成立。当前高 P 样本 `required_M2=15322.036283, M2=17810, margin=2487.963717, required/M2=0.860305, non_equal=0, low/geom=0.997200`；最紧层 `p=5003,m=4` 需要 `required/M2=0.907437`。该项把硬点压成 `PairLower + LowSievePreservation`，尚未提供全局固定 gap 素对下界。 |

| C13低筛保存AP出口 | 新增/LowSievePreservation-AP | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-lowsieve-preservation-audit.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_lowsieve_preservation_audit.py`。低筛删除满足刚性同余 `q≡-(j-j1)r u^{-1} mod ell`，给出纯整数删除天花板 `U_int`。当前高 P 总池 `geom=17860, required=15322.036283, slack=2537.963717, actual_deleted=50, U_int=2309` 总量通过；但逐窗口最紧点 `p=5003` 有 `slack=682.727367, actual_deleted=5, U_int=1245`，纯整数天花板失败。下一硬点变为 AP 素对删除上界：证明固定 gap 尾素对不会集中落入低筛删除同余类，或过密即触发 PDEC/SAE/ColumnCRT。 |

| C13低筛AP删除证书 | 新增/样本AP闭合 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-lowsieve-ap-deletion-audit.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_lowsieve_ap_deletion_audit.py`。定义 `U_AP=sum #{q,q+g in tail primes, q=a mod ell}`，证明 `D_low<=U_AP`，若 `U_AP<=G_geom-R` 则 `LowSievePreservation` 成立。当前高 P 样本 `U_int=2309` 但 `U_AP=50`，`slack=2537.963717`，逐窗口 `p=5003` 从 `U_int=1245>slack=682.727367` 修复为 `U_AP=5<slack`；所有活跃 AP 类 `max_class=1`。该项闭合当前压力样本 AP 删除，不闭合全局 AP 上界。 |

| C13低筛AP-Brun常数余量 | 新增/条件常数接口 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-lowsieve-ap-brun-margin.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_lowsieve_ap_brun_margin.py`。定义 AP 删除尺度 `B_AP=sum S(g)|J∩a mod ell|/log^2 J_-`；若目标删除类族整体满足 `U_AP<=C_AP B_AP` 且 `C_AP B_AP<=G_geom-R`，则低筛保存闭合。当前高 P 样本 `B_AP=51.228906, slack=2537.963717, allowable_C=49.541634`；逐窗口最紧 `p=5003` 允许 `27.803171`，逐层最紧 `p=5003,m=5` 允许 `27.077992`，所以聚合条件输入 `C_AP<=20` 在样本中通过。该项不证明 `C_AP<=20`，剩余是 AP-Brun 常数包或超标类 PDEC/SAE。 |

| C13 AP提升层刚性 | 新增/lift-1 邻接压缩 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-ap-lift-rigidity-audit.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_ap_lift_rigidity_audit.py`。修正前一层口径：`C_AP<=20` 只能作为聚合常数，不能逐 AP 类断言；样本中单点类逐类常数最高约 `35.50`。提升层分解 `q=a+t ell` 后，当前高 P 样本所有真实 AP 删除均为 `t=1`：`active=50, lift1=50, lift_ge2=0, max_possible_lift=3`。更强地，lift-1 纯整数候选总量已小于余量：`p=5003 possible_lift1=285<682.727367`、`p=10007 possible_lift1=256<1855.236350`。因此 AP 删除硬点进一步压成 lift-1 纯整数候选全局余量，以及 lift>=2 的空性或 PDEC/SAE 出口。 |

| C13 lift1纯整数余量 | 新增/lift1分支样本闭合 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-lift1-integer-margin.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_lift1_integer_margin.py`。证明 `lift=1` 时每个删除类最多给一个整数候选 `q=ell+a`，故真实删除 `D1<=N1`；若 `N1<=G_geom-R` 且 `D_ge2=0`，则低筛保存成立。当前高 P 样本 `slack=2537.963717, possible_lift1=541, margin=1996.963717, possible_lift1/slack=0.213163, active_lift_ge2=0`；逐层最紧 `p=5003,m=5` 为 `206/461.520978=0.446350`。剩余压缩为全局证明 `N1` 余量与 `lift>=2` 空性/PDEC。 |

| C13 lift1 offset/h-layer分解 | 新增/lift1结构压缩 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-lift1-offset-decomposition.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_lift1_offset_decomposition.py`。证明 `lift=1` 候选满足精确恒等式 `u a=n+h ell` 与 `q=((u+h)ell+n)/u`，从而 `N1` 可按 h-layer 门控求和。当前高 P 样本精确复现 `lift1=541`，实际低素块门控 `exact_hgate=541`，且所有候选均落在边缘整数层：`edge=541, mid=0, h0_head_integer=277, hu_tail_integer=264`；最紧层仍为 `p=5003,m=5`，`edge=206, mid=0, 206/461.520978=0.446350`。该项把全局义务压成 `LOD-MidVoid` 与 `LOD-EdgeBudget`，尚未闭合行命题。 |

| C13 lift1边缘层去重预算 | 新增/LOD-EdgeBudget压缩 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-lift1-edge-budget.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_lift1_edge_budget.py`。证明边缘层可写成 `h=0: q=ell+s` 与 `h=u: q=2ell-s` 的低素块短区间计数；并将多个低筛 witness 投影到 formal unit `(j1,j2,u,g,q)` 去重，得到 `D_1<=U_edge+N_mid`。进一步给出纯几何门数包络 `U_edge<=N_edge_raw<=K*G_edge` 与临界低素块条件 `K<=Kcrit=floor(slack/G_edge)`。当前高 P 样本 `raw_edge=541, unique_edge=527, gate_envelope=848, duplicate_saving=14, unique_edge/slack=0.207647, gate_envelope/slack=0.334126, Kcrit=23`；逐层最紧 `p=5003,m=5` 为 `raw=206, unique=194, gate_envelope=400, gate_envelope/slack=0.866699, Kcrit=9, Kmargin=1`。该项降低样本付款并给出更强全局接口；全局 `K<=Kcrit` 或 `U_edge<=slack` 与 `N_mid` 仍未闭合。 |

| C13 lift1中间层空性审计 | 新增/LOD-MidVoid与总池出口 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-lift1-midlayer-void-audit.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_lift1_midlayer_void_audit.py`。中间层定义为 `0<h<u`，候选仍由 `u a=n+h ell` 与 `q=((u+h)ell+n)/u` 门控。当前高 P 样本 `mid_exact=0, mid_gates=148, mid_gate_envelope=1184, mid_gate_envelope/slack=0.466516`，全部中间门满足 `h/u=1/2`。与边缘层合并后总池 `K(G_edge+G_mid)=848+1184=2032<2537.963717`，说明样本即使不用 mid 精确空性也可总池付款；但 `p=5003` 逐窗口门数包络超本窗口 slack，所以全局仍需证明总池付款合法，或证明 MidVoid/formal/PDEC。 |

| C13 lift1全局门数总池 | 新增/付款口径分离 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-lift1-global-gate-pool.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_lift1_global_gate_pool.py`。合并边缘与中间层，区分纯门数 `GatePool: D1<=K(G_edge+G_mid)` 与 `Formal+MidVoid: D1<=U_edge+N_mid`。当前高 P 总池 `slack=2537.963717, edge_gate=848, mid_gate=1184, gate_env=2032, gate_margin=505.963717, gate_env/slack=0.800642`，总池门数付款通过；同时 `formal=527, formal_margin=2010.963717, mid_void=True`。逐窗口 `p=5003` 的 LocalGatePool 失败，但 Formal+MidVoid 仍通过。剩余是证明 HighP-PLT 允许总池付款，或全局化逐窗口 `U_edge+N_mid<=S_local`。 |

| C13低筛保存总池桥接 | 新增/HighP-PLT接回接口 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-lowsieve-global-pool-bridge.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_lowsieve_global_pool_bridge.py`。证明若 `HighP-PLT` 对同一目标族 `F` 按总和要求 `sum G^L>=sum R`，则低筛删除可在 `F` 内总池付款：`sum D_low<=sum(G_geom-R)` 即可。当前高 P 样本 `slack=2537.963717, gate_lift1=2032, formal_lift1=527, ge2_both=0, gate_margin=505.963717, formal_margin=2010.963717, mid_void=True, ge2_void=True`，总池 GatePool 与逐窗口 Formal+MidVoid 均给出可用出口；但 LocalGatePool 在 `p=5003` 失败。剩余是全局证明完整目标族的 GatePool 总池不等式，或全局化每窗口 Formal+MidVoid，并全局化 lift>=2 Mod6Void。 |

| C13 HighP-PLT低筛闭合桥 | 新增/样本PLT接回闭合 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-highp-plt-closure-bridge.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_highp_plt_closure_bridge.py`。直接检查 `G_geom-D_low^upper>=R`。当前高 P 总池 `geom=17860, required=15322.036283, gate_deleted=2032, gate_low_lower=15828, gate_margin=505.963717, formal_low_lower=17333, formal_margin=2010.963717`，Gate 与 Formal 均通过；逐窗口 `p=5003` 的 Gate 口径失败但 Formal 口径通过。该项完成当前压力样本 `HighP-PLT` 接回闭合桥；全局仍需证明完整目标族的 Gate 总池不等式或 Formal 逐窗口不等式，并全局化 lift>=2 Mod6Void。 |

| C13高P主合同 | 新增/样本高P链条合成闭合 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-master-contract.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_master_contract.py`。合并 `lift>=2` 结构判据、Gate 总池 PLT、Formal 逐窗口 PLT，给出两条闭合路线：`TotalGateContract` 与 `LocalFormalContract`。当前高 P 样本 `structural=True, candidates=1368, good=0, min_block_margin=822, min_n_margin=4363, gate_plt=True, formal_plt=True, total_gate_contract=True, local_formal_contract=True, row_formal_contract=True`。该项说明当前压力样本内部高 P 链条已合成闭合；全局剩余转为明确完整目标窗口族生成规则，并证明该族满足同一合同或给例外出口。 |

| C13目标窗口族合同 | 新增/样本合同闭合且全局生成规则未闭合 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-target-family-contract.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_target_family_contract.py`。该项把 `C13` 高 `P` 主合同的最后全局化缺口单独物化为 `TFC-A/B/C/D`，并进一步把结构空性条件比例化：由 `L>alpha p`，`B<2alpha p` 与 `(m_max-1)|r|<alpha p` 即推出 `B<2L`、`(m-1)|r|<L` 与 `2B+(m-1)|r|<5L`；默认 `alpha=0.9,m_max=5` 时为 `B/p<1.8`、`|r|/p<0.225`。付款侧当前 `gate_total_margin=505.963717`，但 `min_gate_window_margin=-485.272633`，所以 Gate 只能走总池；逐窗口路线必须走 Formal，样本 `min_formal_window_margin=411.727367`。当前压力样本输出 `explicit_contract=True`、`ratio_structural=True`，但 `target_family_rule_closed=False`；不得据此宣称行命题全局无条件证明。 |

| C13 Formal局部付款合同 | 新增/样本逐窗口付款拆分闭合 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-formal-local-payment-contract.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_formal_local_payment_contract.py`。该项把逐窗口付款拆成 `D_formal=U_edge+N_mid+D_ge2`。当前高 P 样本 `slack=2537.963717, edge=527, mid=0, ge2=0, formal=527, margin=2010.963717, min_local_margin=411.727367, max_formal/slack=0.396937`，所以样本逐窗口 Formal 付款闭合。全局剩余更窄：证明完整目标族 `MidVoid` 恒成立并证明 `U_edge<=S`，或把失败窗口送入有限证书/PDEC/SAE。 |

| C13边缘Gate局部付款 | 新增/EdgeExact升级为EdgeGate | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-edge-gate-payment-contract.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_edge_gate_payment_contract.py`。该项证明边缘 exact 付款可由更粗的 `K*G_edge<=S` 替代，因为 `U_edge<=K*G_edge`。当前高 P 样本 `slack=2537.963717, gate_envelope=848, unique_edge=527, gate_margin=1689.963717, min_gate_margin=106.727367, max_gate/slack=0.843675`，逐窗口边缘 Gate 付款通过。全局剩余由 `MidVoid+EdgeExact` 缩窄为 `MidVoid+EdgeGatePayment`；仍不得宣称行命题全局闭合。 |

| C13中间层奇偶空性 | 新增/MidVoid压缩为MidHalfOnly | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-midlayer-parity-void-contract.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_midlayer_parity_void_contract.py`。中间层同余为 `n+h ell=0 mod u`；若非空中间门均为 `(h,u)=(1,2)`，则要求 `n+ell` 偶。目标族 `r` 偶使 `n` 偶，而低素 `ell>2` 为奇，故无解。当前高 P 样本 `layers=4, mid_gates=148, integer_ceiling=3922, mid_exact=0, half_only=True, shift_even=True, low_odd=True, parity_void=True`。全局剩余由 `MidVoid` 缩窄为证明完整目标族 `MidHalfOnly`，或把 `h/u!=1/2` 送入有限证书/PDEC/SAE。 |

| C13中间层结构空性 | 新增/MidVoid压缩为大小压缩+模2/3杀除 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-midlayer-structural-void-contract.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_midhalf_structural_contract.py`。若真实中间候选存在，则 `q=((u+h)ell+n)/u<=2B/u`，故 `(u+h)L-N<=2B`。条件 `2B+N<5L` 强制 `u+h<=4`，中间层只剩 `(u,h)=(2,1)` 或 `(3,1)`；再由 `6|r` 使 `n` 同时被 `2,3` 整除，而低素 `ell>3`，两种候选分别在模 `2/3` 下无解。当前高 P 样本 `structural_mid_void=True, min_compression_margin=6007, max_ratio=4.037748`。全局剩余从 `MidHalfOnly` 改进为证明完整目标族满足 `2B+(m-1)|r|<5L` 与 `6|r,L>3`。 |

| C13边缘门结构上界 | 新增/G_edge压缩为固定m公式 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-edge-structural-ceiling-contract.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_edge_structural_ceiling_contract.py`。在 `B<2L, U<B+1, T>U, 6|r` 下，非空边缘门只能来自 `u=1` 的 tail 与 `u=2,3` 的 head；因此 `G_edge(m)<=sum_{j1=1}^{m-1}j1^2+2*C(m,3)`。当前 `m={4,5}` 给逐窗口上界 `72`，默认 `K=8` 结构 envelope 为 `576`。样本 `actual_gates=106, structural_ceiling=144, structural_pay=True, min_structural_margin=106.727367`。全局剩余改进为证明每个目标窗口 `S>=K*72` 或给失败出口。 |

| C13结构边缘SlackFloor | 新增/付款余量拆解为共振余量+几何缓冲 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-slack-floor-contract.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_slack_floor_contract.py`。把 `S>=K*E_M` 拆成 `S=(M2-B2_model-Cap_even)+(G_geom-M2)`，并抽出更强充分条件 `ResonanceFloor: sum_m(M2-B2_model-Cap_even)>=K*E_M`。当前样本 `edge_envelope=1152, total_resonance_margin=2487.963717, total_slack=2537.963717, min_resonance_floor_margin=101.727367, min_slack_floor_margin=106.727367, res_pass=True, slack_pass=True`。全局剩余改进为证明完整目标族上的 ResonanceFloor/SlackFloor。 |

| C13低筛删除允许量 | 新增/SlackFloor等价为低筛删除密度界 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-low-deletion-allowance-contract.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_low_deletion_allowance_contract.py`。把 `SlackFloor` 等价改写为 `D_low=G_geom-M2 <= G_geom-B2_model-Cap_even-K E_M`。当前样本 `G=17860, survivor=17810, D_low=50, allowed=1385.963717, margin=1335.963717, deletion_density=0.002800, allowed_density=0.077602, allowance=True`；最紧窗口 `p=5003` 删除 `5`，允许删除 `106.727367`。全局剩余进一步定位为证明低大素块在几何候选集上的删除密度通用上界。 |

| C13低筛AP单点化归约 | 新增/D_low压成活跃AP类计数 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-ap-singleton-reduction-contract.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_ap_singleton_reduction_contract.py`。低筛删除类为 `(ell,j,residue,g,u,j1,j2)`，当前样本满足 `D_low=unique_ap=raw_ap=active_AP_classes=50` 且 `max_AP_pairs_per_class=1`。总 AP 类数 `3552`，活跃类密度 `0.014077`，允许几何删除密度 `0.077602`；逐窗口均有 `singleton=True,class_pay=True`。全局剩余进一步拆为 `APSingleton` 与 `ActiveClassBound`。 |

| C13 AP单点化结构条件 | 新增/APSingleton由q<2ell推出 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-ap-singleton-structural-contract.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_ap_singleton_structural_contract.py`。证明接口为：若活跃 AP 类满足 `q<2ell`，则同一残基类中只可能有 `q=ell+residue` 一个尾素候选。当前样本 `active=50, all_u23=True, all_q_lift1=True, all_q_lt_2ell=True, singleton=True, max_q/ell=1.099922, u_hist={2:25,3:25}`。全局剩余由 APSingleton 改进为证明活跃类不进入 `q>=2ell` 高提升残基，或给 PDEC/SAE 出口。 |

| C13活跃类模板上界 | 新增/ActiveClassBound压成模板骨架付款 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-active-class-template-bound-contract.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_active_class_template_bound_contract.py`。在 `q<2ell` 单点化后，同一模板骨架至多由 `K` 个低素激活，故充分条件为 `K*T_skeleton<=Allow`。当前样本 `active=50, skeleton=28, template_ceiling=224, allowed=1385.963717, min_template_margin=66.727367`。全局剩余改为证明目标族上的 `q<2ell` 与 `SkeletonCountBound`。 |

| C13前向源槽结构 | 新增/SkeletonCountBound压成前向源槽 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-source-slot-structural-contract.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_source_slot_structural_contract.py`。当前样本所有活跃骨架满足 `j>j1>j2`，并有 `q=ell+(j-j1)|r|/u`、`q+g=ell+(j-j2)|r|/u`。`p=10007` 由粗槽上界自动付款；`p=5003` 是唯一小余量窗口。全局剩余变为证明完整目标族的前向源槽结构，及小余量窗口的有限证书覆盖。 |

| C13小余量源槽证书 | 新增/唯一小余量样本有限闭合 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-small-slack-source-certificate.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_small_slack_source_certificate.py`。对 `p=5003` 枚举全部 `224` 个前向低素试验，只有 `5` 个激活，且与 `active_ap_classes()` 完全一致；允许源槽预算 `13.340921`，余量 `8.340921`。该项闭合当前样本小余量窗口，但全局仍需证明不会产生新的小余量窗口，或全部列入有限证书表。 |

| C13小余量有限化归约 | 新增/Allow<224进入有限表 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-small-slack-finite-reduction-contract.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_small_slack_finite_reduction_contract.py`。把源槽付款分为 `Allow>=224` 大余量自动付款与 `Allow<224` 有限证书出口。当前高 P 样本 `large_slack_windows=1, small_slack_windows=1, all_pass=True, F_small={(5003,8192,-36)}`；`p=997` 由 `finite-p-cut=1000` 路由到低 P 有限证书系统。全局剩余精确为证明完整高 P 目标族中所有 `Allow<224` 窗口均落入有限表。 |

| C13热门位移目标生成器 | 新增/selected来源去手填化 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-hotshift-target-generator-contract.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_hotshift_target_generator_contract.py`。生成规则为 `B=2^ceil(log2(p+1))`，再取固定符号低素 squarefree 光滑集合的最热门非零差值 `r`。当前高 P 样本自动生成 `5003:8192:-36,10007:16384:-900`，`matches_expected_highp=True, full_postlow_chain=True, small_slack=True`。该项只闭合 selected 样本来源；全局剩余仍是证明热门位移生成器覆盖所有 C13 高 P 目标窗口及并列 tie-break 不遗漏。 |

| C13热门位移tie-break | 新增/正负对称并列定向 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-hotshift-tiebreak-contract.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_hotshift_tiebreak_contract.py`。当前样本最大差值并列只来自正负对称：`p=5003` 为 `{-36,36}`，`p=10007` 为 `{-900,900}`；最大绝对差值唯一，取负向代表后 `all_oriented_unique=True`。全局剩余是证明所有高 P 目标窗口最大热门绝对差值唯一，或并列时全部输出并给出口。 |

| C13热门位移镜像合同 | 新增/正向窗口归一化到负向代表 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-hotshift-mirror-contract.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_hotshift_mirror_contract.py`。当前样本正向窗口 `5003:8192:36,10007:16384:900` 与负向代表在 `mid/formal/edge/res/active_template/source_exact/small_slack` 余量上完全一致；正向仅因源槽方向反转导致 `source_forward=False`，可由索引反射归一化。样本 `orientation_closed=True`。全局剩余是证明该镜像反射对所有正负热门对成立，及处理多个绝对热门差值并列。 |

| C13全最大热门集生成器 | 新增/多绝对热门并列全输出 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-hotshift-maxset-generator-contract.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_hotshift_maxset_generator_contract.py`。生成器输出所有达到最大热门计数的绝对差值，并只取负向代表；正向由镜像合同处理。当前样本 `max_abs_counts={997:1,5003:1,10007:1}`，高 P 输出仍为 `5003:8192:-36,10007:16384:-900`，并满足 `full_postlow=True, small_slack=True`。全局剩余改为证明行命题反例必须落入该全最大热门集，且所有输出窗口满足局部链或有出口。 |

| C13高P局部闭合链 | 新增/样本局部链合成闭合 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-local-chain-contract.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_local_chain_contract.py`。该项合成 `RatioStructuralVoid + MidStructuralVoid + EdgeStructuralPayment + SlackFloor => FormalLocalPayment`，并已接入 AP 单点化、前向源槽和小余量有限证书后段。当前样本输出 `local_chain=True, full_postlow_chain=True, mid_margin=6007, formal_margin=411.727367, edge_struct_margin=106.727367, res_margin=101.727367, active_template_margin=66.727367, small_slack_source_margin=8.340921, target_rule_closed=False`。全局剩余明确为目标窗口族生成器：证明不遗漏目标窗口，并证明完整目标族满足比例结构、MidStructuralVoid、EdgeStructuralPayment、LowDeletionAllowance、APSingletonStructural、ActiveClassTemplateBound 与 `Allow<224` 有限表覆盖，或给失败出口。 |

| C13 lift>=2空性审计 | 新增/高提升样本闭合 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-liftge2-void-audit.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_liftge2_void_audit.py`。当前高 P 样本所有 `lift>=2` 候选均不可能成为真实 AP 删除：`candidates=1368, q_tail=0, both_tail=0, q_not_tail=1368, q_spf={2:440,3:928}, lift_hist={2:888,3:480}`；逐窗口 `p=5003 candidates=704`、`p=10007 candidates=664` 也全部 `void_by_q=True`。这说明高提升层由 2/3 小素因子刚性杀掉。该项闭合当前样本 `lift>=2`，剩余是全局证明该小素因子空性或给未空候选 PDEC/SAE 出口。 |

| C13 lift>=2模6空性 | 新增/小素因子同余化 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-liftge2-mod6-audit.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_liftge2_mod6_audit.py`。将高提升空性改写为纯模 `6` 判据：若 `q=a+t ell mod 6` 不在 `{1,5}`，则 `q` 不是尾素。当前高 P 样本 `candidates=1368, bad_mod6=1368, good_mod6=0, q_mod6={2:250,3:928,4:190}, t_mod6={2:888,3:480}, residue_mod6={0:920,1:252,5:196}, ell_mod6={1:772,5:596}`；逐窗口全部 `all_bad=True`。剩余是全局证明 `LiftGE2-Mod6Void` 或将 `q mod 6 in {1,5}` 残余送入 PDEC/SAE。 |

| C13 lift>=2签名空性 | 新增/Mod6Void结构化 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-liftge2-signature-audit.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_liftge2_signature_audit.py`。由 `q=a+t ell` 与 `u a=n+h ell` 得 `u q=(tu+h)ell+n`；当前样本 `6|r`，故 `n=0 mod 6`，且所有 `lift>=2` 候选满足 `u=1, t in {2,3}, h in {0,1}`。因此 `q=(t+h)ell mod 6`，而 `t+h in {2,3,4}`、`ell mod 6 in {1,5}`，推出 `q mod 6 in {2,3,4}`。样本输出 `candidates=1368, bad=1368, good=0, q_mod6={2:250,3:928,4:190}, u_hist={1:1368}, t_hist={2:888,3:480}, h_hist={0:920,1:448}`。全局剩余压成证明目标族满足 `6|r`、`u=1`、`t in {2,3}`、`h in {0,1}`，否则送 PDEC/SAE。 |

| C13 lift>=2结构充分条件 | 新增/签名空性无枚举化 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-liftge2-structural-criterion.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_liftge2_structural_criterion.py`。证明若低素块最小素数 `L` 满足 `B<2L`、`(m-1)|r|<L`、`6||r|`，则所有 `lift>=2` 候选必有 `u=1`、`t in {2,3}`、`h in {0,1}`，进而 `q mod 6 in {2,3,4}`，所以 `D_ge2=0`。当前高 P 样本 `criterion=True, candidates=1368, good=0, min_block_margin=822, min_n_margin=4363`。全局剩余从逐候选 Mod6Void 压成证明完整目标窗口族满足这三条结构不等式，或对失败窗口给有限/PDEC/SAE 出口。 |

| C13低筛lift闭合证书 | 新增/低筛保存样本闭合 | 新增 `docs/monograph/prime-matrix-eda-alpha-tail-tailpair-c13-lowsieve-lift-closure.md` 与脚本 `experiments/prime_matrix_alpha_tail_tailpair_c13_lowsieve_lift_closure.py`。证明 `D_low<=N1+D_ge2`，若 `N1+D_ge2<=G_geom-R` 则低筛保存成立。当前高 P 样本 `slack=2537.963717, lift1=541, ge2_both=0, consumed=541, margin=1996.963717, consumed/slack=0.213163`；逐窗口 `p=5003 consumed/slack=0.417443`、`p=10007 consumed/slack=0.137988`；逐层最紧 `p=5003,m=5` 为 `0.446350`。该项闭合当前压力样本低筛保存分支；全局仍需证明 `N1+D_ge2<=S`。 |
| 提升轮强制重叠证书 | 新增/平方端点硬点升级 | 新增 `docs/monograph/prime-matrix-promoted-wheel-forced-overlap-certificate.md` 与脚本 `experiments/prime_matrix_promoted_wheel_forced_overlap_audit.py`。令 `T=sum_q|A_q|`、`I2=sum_k binom(m_k,2)`、`M` 为单点剩余 q 标签上界，则 `T-U>=2I2/M`；若 `T-ceil(2I2/M)<|S_W^\pm(P)|`，剩余高素斜线不能盖满轮骨架。样本 `W=9699690` 中 `P=99991, plus` 得 `S=17100,T=21271,I2=12968,M=6,forced_union_upper=16948`；提升到 `W=223092870` 后最大单线转到 `q=29` 且强制重叠余量增大。该项不是无条件行命题证明；剩余是证明 `T/I2/M` 的全局确定不等式，或把失败送入 `PDEC/SAE/ColumnCRT`。 |
| 动态提升轮粗骨架容量 | 新增/一阶容量主出口 | 新增 `docs/monograph/prime-matrix-dynamic-promoted-rough-capacity.md` 与脚本 `experiments/prime_matrix_dynamic_promoted_rough_capacity_audit.py`。取 `Y=P^alpha` 并把全部 `q<=Y` 提升进底座；若剩余高素总命中 `T_Y^\pm(P)<|S_Y^\pm(P)|`，则全覆盖不可能。选择 `alpha=0.43`，有 `e^{-1}<alpha<1/2` 且 `log(1/alpha)=0.843970<1`。连续审计 `13<=P<=100000` 的 `9587` 个素数、plus/minus 共 `19174` 条记录，`capacity_fail=0`、`forced_fail=0`、最小容量余量 `1`；高段 `P>=10007` 最小余量 `213`、最大 `T_Y/S_Y=0.871142`。该项把当前最优主线改为 `DPRC(alpha=0.43)`：证明同权相对筛不等式 `T_Y<S_Y`，若聚合筛估计超预算则路由到 `PDEC/SAE/ColumnCRT`。 |
| DPRC相对筛余量分解 | 新增/解析硬点压成平方根偏差 | 新增 `docs/monograph/prime-matrix-dprc-relative-sieve-margin.md` 与脚本 `experiments/prime_matrix_dprc_relative_sieve_margin.py`。用恒等式 `S-T=S(1-H)-(T-HS)` 分离模型余量与相对筛偏差，其中 `H=sum_{P^0.43<q<P}1/q`。审计 `13<=P<=100000` 显示 `P>=2003` 时 `min S(1-H)/sqrt(S)=3.579479`、`max max(0,T-HS)/sqrt(S)=2.468627`，所以 `C=3` 充分条件在 `P>=2003` 全部通过；`P<2003` 可保留有限证书。新的最小解析义务是证明动态粗骨架上的剩余高素同余类正偏差 `max(0,T-HS)<=3sqrt(S)`，或把失败送入 `PDEC/SAE/ColumnCRT`。 |
| DPRC beta桶能量同步性 | 新增/平方根偏差硬点再压缩 | 新增 `docs/monograph/prime-matrix-dprc-bucket-energy-synchronization.md`，并升级 `experiments/prime_matrix_dprc_block_envelope_scan.py` 输出正偏差桶向量的 `L1/L2/有效维数/Cauchy松弛`。设 `x_B=D_B^+/sqrt(S)`，目标由 `||x||_1<=3` 推出；若 `||x||_2<=3/sqrt(6)`，Cauchy 直接闭合。审计 `P<=100000` 高段显示 `max ||x||_2=1.233496`，粗 Cauchy 仅给 `3.021437`；但 `||x||_1>=2.4` 的记录只有 `2` 条，且 `max ||x||_2=1.177635<6/5`。反向看，`||x||_2>3/sqrt(6)` 的记录只有 `1` 条，最大 `||x||_1=2.078474<12/5`。新接口可取 `BES-A: ||x||_1>=12/5 => ||x||_2<=6/5`，或 `BES-B: ||x||_2>3/sqrt(6) => ||x||_1<12/5`。该项仍是归约和审计，不是无条件证明；若 BES 失败，应产生高能量高正和同步尖峰并进入 `PDEC/SAE/ColumnCRT`。 |
| DPRC-BES对偶大筛路线 | 新增/失败出口结构化 | 新增 `docs/monograph/prime-matrix-dprc-bes-dual-large-sieve-route.md`。将桶偏差写为中心化核 `D_B=<1_S,Psi_B>`，危险交集 `||x||_1>=12/5` 且 `||x||_2>6/5` 强制出现三类结构：`PointLoad`、`ShortWindow`、`LowPhase`，分别路由到 `ColumnCRT/tail-anchor`、`SAE`、`PDEC`。该文件是证明路线，不是证明；下一步需为三类出口分别给阈值定理或机器证书。 |
| DPRC-BES近危险结构审计 | 新增/出口优先级定位 | 新增 `docs/monograph/prime-matrix-dprc-bes-nearmiss-structure-audit.md` 与脚本 `experiments/prime_matrix_dprc_bes_nearmiss_structure_audit.py`。对最高 L1、最高 L2、高有效维数和各 beta 桶尖峰共 `10` 个代表样本做三出口解剖：最大单点负载全部为 `4`，暂未出现 PointLoad 爆炸；最强短 q 子窗约 `0.25~0.38sqrt(S)`，不足以形成危险交集；最稳定信号是 `mod30` 单位类内部偏斜，`all/mod30` 峰值最高 `0.902430sqrt(S)`，且所有顶峰的 `P^2±k mod 30` 均为单位类。下一最小硬点更新为 `WheelUnitPhaseBalance(W=30)`，再提升到 `210/2310`，或将同步峰物化为 `W-unit PDEC`。 |
| DPRC W=30单位相位平衡 | 新增/第一层轮偏斜不同步 | 新增 `docs/monograph/prime-matrix-dprc-wheel-unit-phase-balance.md` 与脚本 `experiments/prime_matrix_dprc_wheel_unit_phase_balance_scan.py`。全扫 `P<=100000`，`P>=2003` 共 `18578` 条记录中，`BES` 两类危险交集计数均为 `0`；最大 `unit30 peak=1.076781sqrt(S)` 出现在 `P=64853 minus`，但该记录 `BES L1=0.493686,L2=0.281040`。高 `L1>=12/5` 只有 `2` 条，最大 `unit30 peak=0.902430` 且 `L2<1.2`；唯一 `L2>3/sqrt(6)` 记录有 `L1=2.078474<12/5`。结论：`mod30` 单位类偏斜真实存在但不同步，下一硬点升级为 `Layered WheelUnitPhaseBalance(W=210/2310)` 或高模大筛吸收。 |
| DPRC层叠轮夹击场 | 新增/几何容量与轮相位合流 | 新增 `docs/monograph/prime-matrix-dprc-cylindrical-layered-wheel-clamp.md` 与脚本 `experiments/prime_matrix_dprc_layered_wheel_phase_scan.py`。全扫 `P<=100000` 同时检查 `W=30/210/2310`：`P>=10007` 时最大单单位峰从 `W=30` 的 `1.076781` 降到 `W=210` 的 `0.617936`、`W=2310` 的 `0.293727`；高 `BES L1` 样本对应单峰分别为 `0.902430/0.331095/0.175276`。这支持“层级轮筛把单位类偏斜逐层分散”的夹击模型：零行若存在，必须同时满足圆柱斜线容量、BES 能量同步和层叠轮相位同步；否则进入 `W-unit PDEC/SAE/ColumnCRT` 或高模大筛吸收。 |
| DPRC层叠轮Fourier路线 | 新增/未稀释峰转PDEC | 新增 `docs/monograph/prime-matrix-dprc-layered-wheel-fourier-energy-route.md`。将 `U_W` 上单位类偏差向量 `E_W(a)` 扣除平均项得到 `F_W(a)`；若单单位类峰未随 `phi(W)` 稀释，则把 `F_W` 延拓到 `Z/WZ` 后由 Parseval 强制存在非零低模加性 Fourier 频率偏大，即 `W-unit PDEC`。全扫显示 `max_peak*sqrt(phi(W))` 对 `30/210/2310` 约为 `3.0456/4.2812/6.4352`，说明不能用朴素均匀随机模型一刀切；正确接口是“稀释则高模大筛吸收，未稀释则低模 Fourier/PDEC 显化”。 |
| DPRC Fourier频率继承分类 | 新增/新素因子层PDEC接口 | 新增 `docs/monograph/prime-matrix-dprc-fourier-inheritance-classifier.md` 与脚本 `experiments/prime_matrix_dprc_fourier_inheritance_classifier.py`。读取 `docs/dprc_layered_wheel_fourier_audit_20260506.json` 后，对 `8` 条代表记录分类：`W=210` 的最强频率 `6/8` 为新增因子 `7` 的 `new-layer`，`W=2310` 的最强频率 `8/8` 为新增因子 `11` 的 `new-layer`；同时 `high L1=2`、`high L2(Cauchy)=1`、危险交集仍为 `0`。该项把层叠同余刚性写成 `Fourier Inheritance Clamp`：新增层频率若持续同步则给 `new-layer W-unit PDEC`，若不同步则低模相位不能支付 `BES` 危险交集，只能走高模分散大筛。 |
| DPRC新增层能量分散 | 新增/强能量高维分散接口 | 新增 `docs/monograph/prime-matrix-dprc-newlayer-energy-dispersion.md` 与脚本 `experiments/prime_matrix_dprc_newlayer_energy_scan.py`。对 `W=rW0`，用 Parseval 精确拆分 `r|h` 继承频率与 `r∤h` 新增层频率。全扫 `P<=100000`、`P>=10007` 的 `16726` 条记录显示：`30->210` 新增能量占比 `0.580510/0.897118/0.997260`，`210->2310` 为 `0.854837/0.926300/0.973218`；但 `2310` 层最大 centered peak 仅 `0.292146`，高 `BES L1/L2` 段分别仅 `0.170133/0.114485`。该项把硬点更新为 `NewLayer Dispersion Clamp`：新增层能量若低维集中则给 `new-layer PDEC`，若高维分散则由对偶大筛吸收。 |
| 第P列锚点轮筛矛盾场 | 新增/第一行平移骨架全局方程 | 新增 `docs/monograph/prime-matrix-pcolumn-anchor-wheel-field.md` 与脚本 `experiments/prime_matrix_pcolumn_anchor_wheel_field_audit.py`。令 `y=x+1,d=P-c`，则第 `x` 行为 `Py-d`，第 `P` 列点 `Py` 给出整行锚残基。对任意轮 `W`，骨架 `S_W(P,y)={d:Py-d mod W in U_W}` 是第一行骨架 `S_W(P,2)` 的圆柱平移 `P(y-2)`；样本 `P=101,499,997,2003,5003` 与 `W=30,210,2310,30030` 全部 `shift_identity_failures=0`。该项把 `P^2±k` 推广为任意行 `Py-d` 的全局覆盖-筛除方程；但第 `P` 列本身全为 `P` 的倍数，只提供锚相位，不直接闭合行命题，仍需证明高素完全覆盖平移骨架会触发容量超预算、`new-layer PDEC`、`SAE` 或 `ColumnCRT`。 |
| 第P列动态容量夹击 | 新增/全行动态轮主硬点 | 新增 `docs/monograph/prime-matrix-pcolumn-anchor-dynamic-capacity.md`，并升级脚本 `experiments/prime_matrix_pcolumn_anchor_dynamic_capacity_audit.py`。取 `Y=P^0.43`，定义 `S_Y(P,y)` 为 `Py-d` 避开全部 `q<=Y` 的动态骨架，`T_Y(P,y)` 为剩余 `Y<q<P` 高素斜线总命中。已严格证明 `T_Y<|S_Y|` 推出该行有素数洞；样本 `P=101,499,997,2003,5003,10007,20011` 全部 `capacity_failure=0`、`union_failure=0`。`P=20011` 最紧行 `y=71` 有 `T/S=0.956857` 但仍有 `1366` 个素数洞，暴露 `NearCutoff Anchor Spike`：cutoff 后第一批高素造成高命中但强重叠。剩余硬点为证明所有 `2<=y<=P+1` 的 `T_Y<S_Y`，或将失败送入近截止锚峰、`PDEC/SAE/ColumnCRT`。 |
| 第P列近截止-远尾反演 | 新增/正偏差主源结构化 | 新增 `docs/monograph/prime-matrix-pcolumn-nearcutoff-fartail-cofactor.md` 与脚本 `experiments/prime_matrix_pcolumn_nearcutoff_spike_audit.py`、`experiments/prime_matrix_pcolumn_far_tail_cofactor_audit.py`。专项审计显示最强 `T/S` 行的 top labels 是 `q≈Y`，但主要正偏差来自远尾 `q>10Y`；`P=100003,y=147` 中远尾承担 `62.4867%` 命中和 `12.725422 sqrt(S)` 正偏差。远尾命中严格反演为 `Y`-rough 互补因子 `m` 上的短素数区间计数：`ceil((Py-P+1)/m)<=q<=floor((Py-1)/m)`，样本全部 `identity_delta=0`。当前硬点升级为 `FarTail-Cofactor Bound`：证明这些互补因子短区间总计数不足以造成零行，或将超额送入 cofactor-anchor、`SAE/PDEC/ColumnCRT`。 |
| 第P列远尾模型付款 | 新增/常数付款接口 | 新增 `docs/monograph/prime-matrix-pcolumn-fartail-model-payment.md` 与脚本 `experiments/prime_matrix_pcolumn_far_tail_model_bound.py`、`experiments/prime_matrix_pcolumn_tail_payment_constant_scan.py`。定义 `Model_tail=sum_m |I_m|/log(q_m^-)`。样本 `P=5003,10007,20011,50021,100003,200003` 的最强近截止行中，远尾 `actual/model` 在 `0.993758..1.025423`，闭合允许常数 `C_allow=(S-non_tail)/Model_tail` 在 `1.107340..1.160000`。对每个 P 的 top-16 风险行取 `C_tail=1.05` 全部通过，失败数 `0`，最紧 `P=20011,y=71` 仍有付款余量 `78.398`。当前硬点为证明 `tail<=1.05*Model_tail`，或将超标层送入 cofactor-anchor、`SAE/PDEC/ColumnCRT`。 |
| 行命题全局结构闭合链 | 新增/非固定常数主路线 | 新增 `docs/monograph/prime-matrix-global-structural-closure-chain.md`、`docs/monograph/prime-matrix-self-normalized-tail-dichotomy.md` 与脚本 `experiments/prime_matrix_global_structural_chain_audit.py`。固定 `1.05` 降级为审计仪表；正式预算为 `C_allow(P,y)=(|S_Y|-N_{<=BY})/M_{>BY}`。已严格证明早期零行必满足 `A_{>BY}>=C_allow*M_{>BY}`，且 `R-E_tail=|S_Y|-T_Y` 把自归一化尾项缺口与斜线容量余量等同。当前审计 `P=5003,10007,20011,50021,100003,200003` 的 top-16 风险行共 `96` 行全部 `capacity_closed`；集中峰最大值为 `max_m_share=0.050898`、`max_band_share=0.333333`、`max_qmod30_share=0.150769`、`max_dmod30_share=0.160000`，到 `P=200003` 分别降至 `0.007967/0.164639/0.130234/0.130667`。新增 `SN-2 BandPositive` 判据：若二进 `m/y` 带满足 `sum_j E_j^+<R` 则零行不可能；样本 `max sum_jE_j^+/R=0.248700`、最小带级吸收余量 `40.980801`。该项是结构归约和路由账本，不是最终无条件证明；剩余硬点为证明带内 signed cancellation，或将失败带缺陷化为 `cofactor-anchor/SAE/PDEC/ColumnCRT` 并接入 `TotalDescent`。 |
| SN-2迭代缺陷下降 | 新增/结构性反证算法 | 新增 `docs/monograph/prime-matrix-sn2-iterative-defect-descent.md`、`experiments/prime_matrix_sn2_band_structure_audit.py` 与 `docs/sn2_band_structure_audit_20260506.md/json`。从最小反例出发，势函数 `Phi=(P,q-window length,-omega(W),unresolved_mass,descent_depth)` 强制每步缩短短窗、提升模数、固定位移、降低素数层或降低未解释质量；无限逃逸分别变成有限 `SAE`、非零 Fourier `PDEC`、固定非零 `ColumnCRT`、下降到 `p=2` 或分散大筛对偶出口。当前 SN-2 正带结构审计把 `163` 个正带分成 `131` 个 `SAE short q-window` 候选和 `32` 个 `DistributedBandLargeSieve` 候选，`mod30` 相位/列位移未触发阈值；分散候选最大单带责任占 `R` 不超过 `0.132524`。该项给出非统计的迭代闭合框架；剩余硬点是证明 `SN-3 DistributedBandLargeSieve` 或其对偶失败必返回 `SAE/PDEC/ColumnCRT`。 |
| SN-3分散正带大筛桥 | 新增/中心化投影再归约 | 新增 `docs/monograph/prime-matrix-sn3-distributed-band-large-sieve-bridge.md`、`experiments/prime_matrix_sn3_distributed_band_projection_audit.py` 与 `docs/sn3_distributed_band_projection_audit_20260506.md/json`。该项把 SN-2 的 `32` 个分散候选重新投影到 `q` 短窗、`q mod W`、`d=Py-qm mod W`，并修正低模模型为单位类条件主项 `W/phi(W)`，避免把非单位禁止类误读成 PDEC 峰。默认 `W=30,210` 审计给出 `distributed_candidate_count=32`，按诊断阈值 `0.75` 分为 `24` 个 `TrueDistributedDLS`、`6` 个 `ColumnCRT-return`、`2` 个 `PDEC-return`；`max E_J/R=0.132524`、`max E_J/sqrt(M_J)=1.310464`、`max centered projection peak share=1.018659`。当前结论是结构再归约：先把中心化 qmod/dmod 峰接近整带超额的部分回流 `PDEC/ColumnCRT`，再对所有低维中心化峰都小的剩余带证明真正的 `DLS/KLS` 高频吸收；仍不是最终无条件证明。 |
| SN3-A中心化低模回流证书 | 新增/低模峰确定性剥离 | 新增 `docs/monograph/prime-matrix-sn3a-centered-lowmod-return-certificate.md`、`experiments/prime_matrix_sn3a_centered_lowmod_return_certificate.py` 与 `docs/sn3a_centered_lowmod_return_certificate_20260506.md/json`。证明确定性剥离引理：若中心化低模桶 `E_beta*>=theta E_J`，则 `E_J-E_beta*<=(1-theta)E_J`；`q mod W` 峰路由 `PDEC`，`d mod W` 峰路由 `ColumnCRT`。当前 `theta=0.75` 的 `8` 个回流证书中，`6` 个 `ColumnCRT-return`、`2` 个 `PDEC-return`；总超额 `132.550671`，低模峰吸收 `121.448880`，比例 `0.916245`，剩余正质量比例 `0.087421`。该项闭合的是无名质量剥离，不是 PDEC/ColumnCRT 出口排斥。 |
| SN3-B真分散残余目标 | 新增/高频吸收接口定位 | 新增 `docs/monograph/prime-matrix-sn3b-true-distributed-residual-target.md`、`experiments/prime_matrix_sn3b_true_distributed_residual_audit.py` 与 `docs/sn3b_true_distributed_residual_audit_20260506.md/json`。该项把 SN3-A 剥离后的 `24` 个 `TrueDistributedDLS` 候选和 `8` 个低模回流正残余合并为高频残余账本：原分散正质量 `561.852711`，SN3-A 后有效未解释质量 `440.889774`，剥离比例 `0.215293`；最大行级剩余责任 `0.187188R`，最大单候选责任 `0.132524R`，真分散候选最大低维峰 `0.746970`。最紧行为 `P=10007,y=75`，由两个真分散带叠加且无低模残余。该项不是证明；剩余硬点是证明同一行多真分散带的高频同步不能持久，或把失败转成 `KLS/dispersion` 非零频率证书。 |
| SN3-C多带同步分裂 | 新增/多壳KLS硬点定位 | 新增 `docs/monograph/prime-matrix-sn3c-multiband-sync-split.md`、`experiments/prime_matrix_sn3c_multiband_sync_audit.py` 与 `docs/sn3c_multiband_sync_audit_20260506.md/json`。证明互反 q 壳分离接口：非邻二进 `m/y` 带的 q 壳严格分离，不能由同一短 q 窗解释。多真分散带叠加被分为 `ShellOverlap=>SAE`、`LowModSync=>PDEC/ColumnCRT`、`KLS-Multishell=>高频输入`。当前审计只有 `3` 个多真分散带行、`3` 对带，路由为 `2` 个 `KLS-Multishell` 与 `1` 个 `LowModSync`；最紧 `P=10007,y=75` 的 q 壳 `[1237,2444]` 与 `[4970,9500]` 相隔 `2525`，q-window 余弦 `0`，最大低模余弦 `0.432620`，确认为真正多壳高频候选。该项继续归约但未证明 KLS 输入。 |
| SN3-D多壳高频列相位桥 | 新增/KLS回流高频Column出口 | 新增 `docs/monograph/prime-matrix-sn3d-kls-multishell-frequency-bridge.md`、`experiments/prime_matrix_sn3d_kls_multishell_frequency_audit.py` 与 `docs/sn3d_kls_multishell_frequency_audit_20260506.md/json`。对 `KLS-Multishell` 残余按列位移 `d=Py-qm mod P` 做有限 Fourier 展开，由 Parseval 得到确定性二分：`HighFrequencyColumn/PDEC` 或 `L2Flat CleanMultishellKLS`。当前两个 KLS 候选均非平坦：`P=10007,y=75` 有 `flatness=0.014668`、`|Rhat(49)|/E=1.374721`；`P=50021,y=128` 有 `flatness=0.004695`、`|Rhat(119)|/E=2.056175`。该项把样本无名 KLS 残余回流高频列相位证书；全局仍需排斥高频 Column/PDEC 出口或证明 clean KLS 输入。 |
| SN3-E高频Bohr-cap无循环 | 新增/高频出口终端化 | 新增 `docs/monograph/prime-matrix-sn3e-highfreq-bohrcap-no-cycle.md`、`experiments/prime_matrix_sn3e_highfreq_bohrcap_certificate.py` 与 `docs/sn3e_highfreq_bohrcap_certificate_20260506.md/json`。证明 Jordan-Bohr 局部化引理：对 signed 残余 `r=r_+-r_-`，若非零频率大小为 `L`、总变差为 `V`，则 `r_+(Bohr_+)+r_-(Bohr_-)>=max(0,(L-alpha V)/(1-alpha))`。因此 `HighFrequencyColumn` 只有三归宿：持久 Bohr-cap 进入 `PDEC/ColumnCRT`，孤立 Bohr-cap 进入 `SAE/endpoint`，无帽则进入 `L2-flat CleanKLS`。当前两个样本在 `alpha=0` 时正帽分别捕获 `58.0008%` 与 `52.4712%` 的正残余质量。该项闭合的是高频无名循环；最终无条件证明仍需排斥命名出口或证明 CleanKLS/TotalDescent。 |
| 行命题无名逃逸闭合机 | 新增/统一势函数结构闭合 | 新增 `docs/monograph/prime-matrix-unnamed-escape-closure-machine.md`。该项把 SN-1 到 SN3-E 合并为势函数 `Phi=(P,active_shell_count,q_window_length,-lowmod_rank,-frequency_rank,unresolved_mass,descent_depth)`，证明最小早期零行反例不能在容量、远尾、正带、分散多壳或高频列相位层级中无限保持无名；每步要么容量闭合，要么进入 `SAE/PDEC/ColumnCRT/Bohr-cap` 命名出口，要么进入 `CleanMultishellKLS`，要么 `TotalDescent` 降到更小素数层。该项闭合的是“无名逃逸不可能”，不是最终无条件行命题；仍需排斥全部命名出口或证明 CleanKLS/TotalDescent。 |
| 行命题命名出口吸收合同 | 新增/出口接口统一 | 新增 `docs/monograph/prime-matrix-named-exit-absorption-contract.md`。该项把 `SAE/PDEC/ColumnCRT/Bohr-cap/CofactorAnchor/TailAnchor/CleanKLS/TotalDescent/EndpointSeam` 统一到吸收算子：`Bohr-cap=>PDEC/ColumnCRT/SAE or CleanKLS`，`EndpointSeam=>PDEC/ColumnCRT/SAE`，`CofactorAnchor=>TailAnchor-Cert or PDEC/ColumnCRT/SAE`，`TotalDescent=>p=2 contradiction or EndpointSeam`。同时补入统一缺陷向量引理：持久命名缺陷都可写成有限签名群上的零均值测试函数偏斜，从而进入 generalized `PDEC-Cert`；稀疏命名缺陷进入 `SAE-Cert`。因此 SN 无名闭合后的剩余不再包含第三类自由出口，只剩 `SAE-Cert/PDEC-Cert/ColumnCRT-Cert/CleanMultishellKLS/p=2下降矛盾` 五类终端接口。该项是结构合同和审稿路由闭合，不是最终无条件证明；仍需实际排斥终端证书或证明 CleanKLS/TotalDescent。 |
| PDEC对偶失败吸收合同 | 新增/PDEC失败形态结构化 | 新增 `docs/monograph/prime-matrix-pdec-dual-failure-absorption-contract.md`。证明 cap localization 引理：若同一坏窗计数 `g` 在某个非零频率方向满足 `sum g(a)c(a)>=U`，则 `g({c>=alpha})>=(U-alpha M)/(1-alpha)`。因此 `PDEC-Dual-Cert` 失败不能成为新自由出口，只能显化为短弧/Bohr-cap 聚簇：持久聚簇进入 refined `PDEC/ColumnCRT`，稀疏聚簇进入 `SAE`，口径不一致进入 `Multiplicity-Stitching` 义务。该项闭合的是 PDEC 失败回流规则，不是所有 `U_CRT<L_PDEC` 的最终证明。 |
| PDEC cap细化无循环 | 新增/refined PDEC递归受限 | 新增 `docs/monograph/prime-matrix-pdec-cap-refinement-no-cycle.md`。证明固定有限签名群内 cap 细化只会生成有限 Boolean algebra 分区；每次真细化严格增加原子数，最多 `|G|-1` 次。终止原子若 singleton 则进入 explicit `PDEC/ColumnCRT`，若仍有内部非零频率则继续细化，若内部平坦则进入 `CleanKLS/dual bound`，稀疏原子进入 `SAE`。若必须提升轮层，则分支已变成 `new-layer PDEC/ColumnCRT` 或高维分散 `CleanKLS`。该项闭合的是 refined PDEC 不会同层无限循环，不是终端证书排斥。 |
| New-layer PDEC塔熵合同 | 新增/无穷层叠结构化 | 新增 `docs/monograph/prime-matrix-newlayer-pdec-tower-entropy-contract.md`。把不断提升 `G_0<G_1<...` 的 new-layer PDEC 写成相对熵/二次能量账本：若每层新增 fiber/cap 偏斜持续存在，则 `sum H_n` 或 `sum E_n` 累积并形成 finite/profinite `PDEC/ColumnCRT`；若熵能量可求和，则新增层偏斜趋零，进入 `CleanKLS/DLS`；若层间口径不一致，则进入 `Multiplicity-Stitching`。该项把无穷轮筛层叠纳入同一结构二分，不是 profinite PDEC 或 CleanKLS 的最终排斥证明。 |
| Multiplicity-Stitching吸收合同 | 新增/口径出口删除 | 新增 `docs/monograph/prime-matrix-multiplicity-stitching-absorption-contract.md`。该项把证书口径不一致全局化为 formal unit 规范化：若重复项有独立约束权重，则进入 `weighted PDEC`；若没有，则坐标商掉并进入 `primitive/physical PDEC` 或 `CleanKLS`；若重复来自同一物理候选、列位移、端点或尾锚跨层复用，则进入 `ColumnCRT/SAE/TailAnchor/CofactorAnchor`。因此 `Multiplicity-Stitching` 不再是终端数学出口，只是证书规范化步骤；终端列表更新为 `explicit/profinite/weighted/primitive PDEC`、`ColumnCRT`、`SAE`、`CleanKLS/DLS`、`TailAnchor/CofactorAnchor`。 |
| TailAnchor/CofactorAnchor吸收合同 | 新增/尾锚出口并回主链 | 新增 `docs/monograph/prime-matrix-tailanchor-cofactor-absorption-contract.md`。利用远尾互补因子反演 `Py-d=qm`，把尾锚和互补因子锚写成 `m/y band`、`m mod Q`、`q mod Q`、`d mod Q/P` 签名。若某锚签名持久承担正超额，则进入 `cofactor/low-mod PDEC` 或 `ColumnCRT`；若稀疏孤立，则进入 `SAE-anchor`；若无锚同步，则进入 `CleanKLS/DLS` 或容量矛盾。因此 `TailAnchor/CofactorAnchor` 也不再是独立终端出口；终端列表压成 `PDEC family`、`ColumnCRT`、`SAE`、`CleanKLS/DLS`。 |
| ColumnCRT位移PDEC吸收合同 | 新增/列缺陷并入PDEC | 新增 `docs/monograph/prime-matrix-columncrt-displacement-pdec-absorption.md`。把列缺陷写成位移签名 `sigma_col=(ell,d_c mod ell)`，其中 `d_c=r_c-H`；CD0 已给出零位移余类禁止。若某非零位移余类持久过载，则进入 `displacement PDEC`；若孤立过载，则进入 `SAE-column`；若不过载，则成为 `PDEC-Dual-Cert` 的列约束行。因此 `ColumnCRT` 不再是独立终端；终端列表压成 `PDEC family`、`SAE family`、`CleanKLS/DLS`。 |
| SAE局部证书归约 | 新增/SAE终端改写为局部证书 | 新增 `docs/monograph/prime-matrix-sae-local-certificate-reduction.md`。把 sparse/single-window escape 改写为 `LocalSurvivorCert` 义务：对孤窗候选集 `C(I)` 和低因子、尾锚、列位移、端点 seam、核心重叠 blocker，必须给出未覆盖 witness 或严格覆盖不足；若局部证书失败，blocker 按签名回流到 `PDEC family`、`TotalDescent/RPZ` 或更小支撑 SAE。固定孤窗内下降有限，沿无限反例族复现则由鸽巢转为 PDEC。因此终端列表更新为 `PDEC family`、`LocalSurvivorCert family`、`CleanKLS/DLS`。 |
| CleanKLS/DLS证书合同 | 新增/clean分支证书化 | 新增 `docs/monograph/prime-matrix-cleankls-dls-certificate-contract.md`。将 `CleanKLS/DLS` 固定为 K1--K7 admission 后的证书对象：范围、低模正交、短窗 cap、列/Bohr cap、系数 L2-flat、gcd/unit 层、formal unit 均通过后，才可提交内部大筛证书或明确外部 `KLS/DI/BFI` 输入；任一 admission 或大筛失败项都必须回流到 `PDEC/SAE/Multiplicity`。因此 clean 分支不再是黑箱出口，最终剩余为 `PDEC family certificates`、`LocalSurvivorCert certificates`、`CleanKLS/DLS certificates or explicit ExternalKLS input`。 |
| 行命题终端三证书总收束 | 新增/无第四出口接口 | 新增 `docs/monograph/prime-matrix-terminal-certificate-triad.md`。该项把当前全部终端出口压成 `Persistent=>PDEC family`、`Sparse=>LocalSurvivorCert`、`Flat=>CleanKLS/DLS or ExternalKLS` 三类，并明确三类失败回流：PDEC 失败经 cap localization 回到 refined PDEC/LocalSurvivor/CleanKLS，LocalSurvivor 失败由 blocker 复现成 PDEC 或支撑缩小，CleanKLS admission/对偶失败回到 PDEC/LocalSurvivor/Multiplicity。该项闭合的是终端接口和无第四出口结构，不是最终无条件证明；剩余是提交三类证书全集，尤其 `Triad-A1 U_CRT<L_PDEC`、`Triad-B1 LocalSurvivor witness` 与 `Triad-C1 L2-flat 大筛界或外部输入`。 |
| Triad-A1 PDEC容量上界路线 | 新增/同一坏窗集合律 | 新增 `docs/monograph/prime-matrix-triad-a1-pdec-capacity-upper-route.md`。该项把 `U_CRT` 上界侧固定为同一坏窗推前计数 `g(t)` 上的 LP/对偶容量问题，禁止用背景全集、完整 CRT 周期均匀性或不同 formal unit 替代当前坏窗集合。可入证书行仅有 `Tautology`、`Attachment(S subset Z)`、`ConditionalRouting` 三类；失败必须输出 `AttachmentFail`、`PhaseCompatFail`、`CapacityInsufficient=>DualCap` 或 `RoutingGap`，并回流 refined PDEC/LocalSurvivor/命名出口。该项是 A1 的结构协议，不是全局 `U_CRT<L_PDEC` 证书。 |
| Triad-A1 LHB容量骨架 | 新增/首个分支骨架 | 新增 `docs/monograph/prime-matrix-triad-a1-lhb-branch-capacity-skeleton.md`。该项把 `Q=2310` 的 LHB-typed PDEC 分支合成为 A1 首个容量骨架：由坏窗分类和 LHB 接入得到 `S subset Z_LHB`，由多重度容量证书得到 `g(t)<=M(t)`，并在 `P in {13,17,19,23,29,31,37,43,47}` 上写入 `WHOLEDEF/BRIDGED bound=0` 零块行。当前闭合的是 attachment 与零块容量；仍未闭合完整 `U_CRT<L_PDEC` 对偶比较、有限 P 外扩展和非 LHB 出口排斥。 |
| Triad-A1 LHB LP骨架审计 | 新增/box-only阻断定位 | 新增 `experiments/prime_matrix_triad_a1_lhb_lp_skeleton.py` 与 `docs/monograph/prime-matrix-triad-a1-lhb-lp-skeleton.md/json`。脚本把 `Q=2310` LHB 分支的 `g(t)<=M(t)`、`WHOLEDEF/BRIDGED bound=0` 和质量范围生成机器可读 LP 骨架，并指出仅靠 box-only 容量无法证明全局 Fourier 抵消：任一 `M(t)>0` 相位都允许单相位支撑，非零频率 Fourier 模长等于质量。下一步必须补方向支撑、column/displacement 相位兼容行、tail/cofactor nonreuse 行或方向弧对偶证书。 |
| Triad-A1 LHB方向支撑合同 | 新增/PDEC支撑行固定 | 新增 `docs/monograph/prime-matrix-triad-a1-lhb-direction-support-contract.md`。该项把 PDEC 定义中的 `S={x:Re F(tau(x))>=kappa}` 转成正式 LP 行 `g(t)=0 outside C_F(kappa)`，并与 LHB 容量行合并为 `supp(g) subset C_F(kappa) cap {M(t)>0}`。若交集为空则 LHB 分支闭合，稀疏则进 LocalSurvivor/explicit PDEC，持久则进 refined PDEC/DualCap，平坦则进 CleanKLS。当前仍需为每个 theta 物化 `F,kappa,C_F`。 |
| Triad-A1 LHB方向支撑审计 | 新增/零块支撑子分支闭合 | 新增 `experiments/prime_matrix_triad_a1_lhb_direction_support_audit.py` 与 `docs/monograph/prime-matrix-triad-a1-lhb-direction-support-audit.md/json`。默认取 `C_F=WHOLEDEF union BRIDGED`，审计其与 `supp(M)` 的交集；当前 `Q=2310` 已列出全部 P 均为 `EmptyCap`。这闭合的是“PDEC 方向强制支撑落在零容量块”这一子分支，不是全部 PDEC；剩余方向必须提交真实 `F,kappa,C_F` 后继续审计。 |
| Triad-A1 LHB Fourier-cap扫描 | 新增/方向支撑压力测试 | 新增 `experiments/prime_matrix_triad_a1_lhb_fourier_cap_scan.py` 与 `docs/monograph/prime-matrix-triad-a1-lhb-fourier-cap-scan.md/json`。脚本扫描 `C_{h,alpha,dir}={t:cos(2*pi*h*t/Q+dir)>=alpha}` 与 `supp(M)` 的交集，并分类为 `EmptyCap/SparseCap/PersistentCap`。该项是方向支撑强弱的压力测试，不是连续方向最终证书；若高阈值 cap 仍 Persistent，则必须补 refined PDEC、column/tail 行或 CleanKLS。 |
| Triad-A1固定Q密度屏障 | 新增/固定层方向支撑路线排除 | 新增 `docs/monograph/prime-matrix-triad-a1-fixed-q-density-barrier.md`。证明有限相位群上的鸽巢下界 `|supp(M) cap C_F|>=|supp(M)|+|C_F|-Q`；因此当固定 `Q` 上 LHB 可完成相位支撑变稠时，任何正密度 Fourier cap 都必然 persistent。该项把 Fourier-cap 扫描中的高 P 持久现象结构化，排除“同一固定低模层普通方向支撑全局闭合”路线；下一步必须升层 refined PDEC、补 column/tail 行或进入 CleanKLS。 |
| Triad-A1新层提升试验 | 新增/Q=30030重新稀疏 | 新增 `docs/monograph/prime-matrix-triad-a1-newlayer-lift-pilot.md` 及 `prime-matrix-triad-a1-q30030-*` 有限产物。试验把 LHB 层从 `Q=2310` 提升到 `Q=30030`，在 `P=17,19,23,29` 上 `supp(M)` 密度分别下降约 `13.00,4.95,3.22,3.20` 倍，且 `WHOLEDEF/BRIDGED` 零块方向仍为 `EmptyCap`。该项验证了固定层密度屏障后的正确路线是 new-layer fiber 细化；仍需证明一般 fiber deletion inequality 或进入 new-layer entropy/CleanKLS 二分。 |
| Triad-A1 canonical-source 自足边界 | 新增/最终边界闭合 | 新增 `docs/monograph/prime-matrix-triad-a1-dibfi-self-contained-final-closure-router.md` 与 `docs/monograph/prime-matrix-triad-a1-self-contained-theorem-boundary-review.md`。最终评审裁定 `APPROVE_CANONICAL_SOURCE_SELF_CONTAINED_BOUNDARY`，闭合命题为 `Triad-A1 same-set capacity / full-S terminal on the canonical RIW/Buchstab source branch`，`open_review_gates=[]`，终端为 `NoFurtherTheoremBoundaryReviewGap`。该项确认 canonical-source 自足边界闭合。 |
| Triad-A1 unrestricted generic WFD 自足版 | 新增/反证且不声明 | 同一评审明确 `Unrestricted generic full-S well-factorable WFD self-contained theorem` 不作为闭合命题；`moving-delta no-go` 反证当前 generic anti-atom 输入，因此该宽口径不是待证缺口，而是已被隔离的错误强化。若接受 FullS-KLS-ext，可得到外部合同版；但外部合同不得混入 canonical-source 自足证明。 |
| 行命题最终边界合并审查 | 新增/合著吸收与剩余门控 | 新增 `docs/monograph/prime-matrix-row-theorem-final-boundary-plain-language.md` 与合并审查产物。合著主稿、理论总览、状态表均已并入 canonical-source 自足边界闭合。该项不升级完整 Prime Matrix 行/列命题为无条件定理；剩余仍为 `PDEC family certificates`、`LocalSurvivorCert family`、`CleanKLS/DLS certificates or explicit ExternalKLS input` 以及 D-structure/Tail-log4/Rankin/referee-block 接口。 |
| FO-PDEC嵌套重复支配审计 | 新增/单位权重复子门闭合 | 新增 `experiments/prime_matrix_wsh_fo_pdec_nested_duplicate_dominance_audit.py` 与 `docs/monograph/prime-matrix-wsh-fo-pdec-nested-duplicate-dominance-audit.md/json`。当前 `ell=199,h=95` 强阈值中的 7 个 exact nested duplicates 全部是同一正式坐标上的嵌套支撑重复，`all_exact_nested_duplicates_unit_weight_blocked=true`，`factor_199_nested_duplicate_unit_weight_blocked=true`。因此这些重复不能按单位权作为两个独立 PDEC 事件计数；若要保留权重，必须提交 fractional Weighted Hall dual，否则坐标商掉或回流 SAE/Endpoint。该项不闭合全局 PDEC，只关闭当前有限 FO-PDEC 的嵌套单位重复误计数路线。 |
| FO-PDEC加权Hall对偶支配 | 新增/fractional重复恢复路线阻断 | 新增 `experiments/prime_matrix_wsh_fo_pdec_weighted_hall_dual_audit.py`、`docs/monograph/prime-matrix-wsh-fo-pdec-weighted-hall-dual-audit.md/json` 与 `docs/monograph/prime-matrix-wsh-fo-pdec-weighted-hall-dual-dominance.md`。审计显示 7 个嵌套重复均为 laminar 支撑，差层 `Delta semiprime=1`、`Delta prime=1`、`Delta surplus=0`，没有新的 Hall 压力支付重复坐标第二单位质量，故 `FractionalWeightedHallCannotRecoverFullNestedDuplicateMass` 子门闭合。raw Fourier `3.959247567099438` 必须降到坐标 cap `2.9698366905785227`；若 cross-q persistence 不成立，则进一步降到 physical/primitive `1.9997507790353146` 或单分支 `1.0`。 |
| FO-PDEC cross-q坐标图重叠支配 | 新增/cross-q持久化当前样本阻断 | 新增 `experiments/prime_matrix_wsh_fo_pdec_cross_q_chart_overlap_audit.py`、`docs/monograph/prime-matrix-wsh-fo-pdec-cross-q-chart-overlap-audit.md/json` 与 `docs/monograph/prime-matrix-wsh-fo-pdec-cross-q-chart-overlap-dominance.md`。审计显示 9 个 cross-q reuses 全部是同一物理候选在重叠 `q` 行坐标图中的表示，统一满足 `base_gap=1,column_gap=-1,candidate_gap=0`，且候选、semiprime、offset、解释因子相同；`factor_199_cross_level_reuse_blocked=true`。因此当前 coordinate-cap `2.9698366905785227` 不能作为独立持久化 PDEC 下界，必须物理去重或转 SAE/Endpoint。 |
| FO-PDEC physical/primitive 二点退化 | 新增/二点阈值阻断 | 新增 `experiments/prime_matrix_wsh_fo_pdec_physical_primitive_tautology_audit.py`、`docs/monograph/prime-matrix-wsh-fo-pdec-physical-primitive-tautology-audit.md/json` 与 `docs/monograph/prime-matrix-wsh-fo-pdec-physical-primitive-tautology.md`。审计显示物理去重后当前 `factor=199` 只剩两个物理原子；任意二点残基在素模上都可由某个频率送成相邻对偶点，故 `2*cos(pi/199)=1.9997507790353146` 是 Fourier tautology，不是可攻 PDEC 缺陷阈值。子门 `PhysicalPrimitivePDECThresholdDegeneratesToTwoPointTautology` 闭合。 |
| FO-PDEC二点SAE/Endpoint吸收 | 新增/当前二点原子本地见证闭合 | 新增 `experiments/prime_matrix_wsh_fo_pdec_sae_endpoint_absorption_audit.py`、`docs/monograph/prime-matrix-wsh-fo-pdec-sae-endpoint-absorption-audit.md/json` 与 `docs/monograph/prime-matrix-wsh-fo-pdec-sae-endpoint-absorption.md`。审计把两个物理原子送入同固定偏移纤维检查：`250541` 的来源行均有 witness prime `250543`，`1664237` 的来源行均有 witness prime `1664227`，且 `factor=199` 在每个纤维内负载为 `1`。因此子门 `TwoPhysicalPrimitiveAtomsAbsorbedByLocalSurvivorWitnesses` 闭合；该项只关闭当前已审计二点样本，不关闭全局 `LocalSurvivorCert family`。 |
| LocalSurvivor已物化包总账 | 新增/当前物化孤窗义务清零 | 新增 `experiments/prime_matrix_local_survivor_materialized_packet_ledger.py`、`docs/monograph/prime-matrix-local-survivor-materialized-packet-ledger.md/json`。总账合并 Triad-A1 SparseCap、FO-PDEC 二点 SAE/Endpoint 和 RPZ Endpoint-SAE 有限账本：`materialized_packet_count=9`、`materialized_phase_atom_count=32`、`local_survivor_witness_count=5`、`finite_pdec_atom_count=25`、`open_materialized_obligation_count=0`。子门 `MaterializedLocalSurvivorPacketsExhausted` 闭合；这只清空当前已物化包，不证明未来所有 sparse escape。 |
| LocalSurvivor packet-generation合同 | 新增/无名孤窗出口删除 | 新增 `docs/monograph/prime-matrix-local-survivor-packet-generation-contract.md`。证明结构二分：任意 sparse/single-window escape 若不能给出有限 `LocalSurvivorCert` packet，则同签名无限复现会进入 `PDEC/ColumnCRT/TailAnchor/CofactorAnchor`，签名层级逃逸则进入 `CleanKLS/DLS`，下降/seam 路线回到命名包。因此剩余压成 `PacketExtractorCompleteness`、`NonTautologicalPDEC` 或 `CleanKLS/DLS`，不再允许无名 LocalSurvivor 终端。 |
| LocalSurvivor extractor覆盖审计 | 新增/已知入口覆盖闭合 | 新增 `experiments/prime_matrix_local_survivor_packet_extractor_coverage.py`、`docs/monograph/prime-matrix-local-survivor-packet-extractor-coverage.md/json`。审计覆盖 `8` 个入口，其中 `4` 个机器 extractor 分别处理 Triad-A1 SparseCap、FO-PDEC 二点 SAE/Endpoint、RPZ Endpoint-SAE 和聚合总账，`4` 个合同入口处理 generic SAE、持久签名、升层 clean 和 descent/seam；`missing_or_open_count=0`。子门 `KnownLocalSurvivorEntryExtractorsCovered` 闭合。 |
| NewSparseEntryAdmission审计 | 新增/未命名新孤窗入口排除 | 新增 `experiments/prime_matrix_new_sparse_entry_admission_audit.py`、`docs/monograph/prime-matrix-new-sparse-entry-admission-audit.md/json`。审计 `8` 类可能来源：短窗/endpoint、PDEC dual sparse cap、EndpointSeam、BohrCap、ColumnTail/Cofactor、DescentSeam、持久签名、升层 clean；全部准入到命名 `SAE/LocalSurvivor/PDEC/ColumnCRT/CleanKLS` 路线，`missing_admission_count=0`。子门 `NoAdditionalUnnamedLocalSurvivorEntryRoute` 闭合；未来若新增显式 sparse 路线，必须提交同类 extractor schema。 |
| 行列无条件自足前沿路由 | 新增/已物化前沿耗尽 | 新增 `experiments/prime_matrix_row_column_unconditional_frontier_router.py` 与 `docs/monograph/prime-matrix-row-column-unconditional-frontier-router.md/json`。路由裁定 `row_column_unconditional_closed=false`、`canonical_source_boundary_closed=true`、`generic_unrestricted_self_contained_refuted=true`、`terminal_triad_routed_no_fourth_exit=true`。当前已审计 FO-PDEC `ell=199` 强信号链已经依次通过嵌套重复、weighted Hall、cross-q 坐标图、physical 二点 tautology 和二点 SAE/Endpoint 本地 witness 吸收；已物化 LocalSurvivor/SAE 包全部闭合，已知 extractor 覆盖，且无未命名新 sparse 入口。CleanKLS/DLS 宽口径已由 K1--K9 admission 和 SC-9 展开压到 `NC-BLK`，且经边界核查确认 canonical-source 分支已吸收、generic 分支仍外部化；非二点 PDEC 准入审计确认当前已物化合法候选为 `0`。当前最窄硬点更新为 `CurrentMaterializedFrontierExhausted_GlobalTerminalFamiliesOpen`。 |
| NC-BLK边界核查 | 新增/canonical吸收但全局未闭合 | 新增 `experiments/prime_matrix_ncblk_boundary_reconciliation_router.py`、`docs/monograph/prime-matrix-ncblk-boundary-reconciliation-router.md/json`。核查 `all_reconciliation_gates_passed=true`：`NC-BLK` 在 canonical RIW/Buchstab source branch 中已被既有同集容量最终边界吸收；generic full-S non-AP 分支仍保持 `ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov` 外部/精确源熵路线，不能偷渡为自足闭合。该项删除“无名 CleanKLS 出口”的歧义，但明确 `row_column_unconditional_closed=false`，完整行/列无条件定理仍需 PDEC、LocalSurvivor、CleanKLS/ExternalKLS 与 D-structure/Rankin 终端证书。 |
| 非二点PDEC准入审计 | 新增/当前已物化候选为零 | 新增 `experiments/prime_matrix_nontautological_pdec_admission_audit.py`、`docs/monograph/prime-matrix-nontautological-pdec-admission-audit.md/json`。审计确认 `current_materialized_nontautological_pdec_candidate_count=0`：raw 三点信号缺同 formal unit 与独立性，嵌套重复、weighted Hall 恢复和 cross-q 坐标重叠均已阻断；物理 primitive 剩余只有二点 Fourier tautology，且二点原子被 LocalSurvivor/SAE witness 吸收。该项不关闭全局 `PDEC family`，但固定未来候选准入要求：同 formal unit、去重后三个以上物理 primitive 原子、非二点 tautology、非图重叠且未被 SAE/Endpoint 吸收。 |
| 全局终端家族边界路由 | 新增/唯一剩余重定位 | 新增 `experiments/prime_matrix_global_terminal_family_boundary_router.py` 与 `docs/monograph/prime-matrix-global-terminal-family-boundary-router.md/json`。审查确认 `materialized_frontier_exhausted=true`、`terminal_generation_contract_closed=true`、`current_terminal_instances_exhausted=true`，但 `global_terminal_family_exclusion_closed=false`、`row_column_unconditional_closed=false`。因此当前剩余不再是局部样本、固定常数或无名 NC-BLK/PDEC 出口，而是 `GlobalTerminalFamilyExclusionCertificates`：证明所有未来 `PDEC family`、`LocalSurvivorCert family`、`CleanKLS/DLS` 终端对象都有排斥证书，或明确接受外部/referee 输入。 |
| 全局终端家族排斥拆分路由 | 新增/最窄终局门重定位 | 新增 `experiments/prime_matrix_global_terminal_family_exclusion_split_router.py` 与 `docs/monograph/prime-matrix-global-terminal-family-exclusion-split-router.md/json`。审查确认 `closed_nonfinal_reductions=true`：无第四出口、当前 LocalSurvivor/NC-BLK 非独立阻塞、连续终端二分均已闭合到 PDEC-CAP 或 CleanKLS/DLS。完整命题仍未闭合；最窄剩余更新为 `PDEC_CAP_OR_KLS_EXT_OR_REFEREE`，完全自足路线则是 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve`。 |
| 完全自足终端瓶颈路由 | 新增/自足独立瓶颈继续收缩 | 新增 `experiments/prime_matrix_self_contained_terminal_bottleneck_router.py` 与 `docs/monograph/prime-matrix-self-contained-terminal-bottleneck-router.md/json`。审查确认 `closed_nonfinal_reductions=true`、`internal_clean_kls_independent_blocker_collapsed=true`、`self_contained_terminal_bottleneck_is_pdec_cap=true`。因此在当前 canonical-source 自足边界内，`InternalCleanKLS_LargeSieve` 不再是独立最窄瓶颈：CleanKLS 失败回流 PDEC/SAE，canonical NC-BLK/CleanKLS 分支已被同集容量边界吸收，unrestricted generic 自足版已反证隔离。当前唯一独立自足数学硬点压成 `PDEC_CAP_SameSetGlobalDualCertificate`；完整行/列无条件定理仍受 `DStructureRankinReferee` 晋级门阻塞。 |
| PDEC-CAP同集全局对偶前沿 | 新增/自足层转移门闭合，剩 external-only | 新增 `experiments/prime_matrix_pdec_cap_same_set_global_dual_router.py` 与 `docs/monograph/prime-matrix-pdec-cap-same-set-global-dual-router.md/json`。审查确认 `closed_current_materialized_pdec_gates=true`、`canonical_source_self_contained_pdec_cap_closed=true`：当前 DualCap 质量来源与早期出口、PersistentCap 晋升删除势、ForcedCap 多桶 APS 路由、LHB 升层投影单调、PDEC cap 无循环与有限塔证据均已接线。新增投影塔 APS、持久有限签名统一、SC-9 边界调和、持久终端准入、primitive 多原子秩边界、二秩 cap-stable 核逆否、统一帽稳定有限基、有限弧横向路由、横向 clean 归约、横向 clean 原子前沿、横向源支撑、横向来源嵌入和 canonical 层闭合路由后，canonical-source 自足分支的最新 PDEC-CAP 层转移门已闭合；剩余只属于 `DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY`。完整行/列无条件定理仍未闭合。 |
| PDEC-CAP diffuse终端分裂 | 新增/不持久分支继续压窄 | 新增 `experiments/prime_matrix_pdec_cap_diffuse_terminal_split_router.py` 与 `docs/monograph/prime-matrix-pdec-cap-diffuse-terminal-split-router.md/json`。审查确认 `diffuse_terminal_split_closed=true`、`external_deep_theorem_version_closed_if_accepted=true`、`self_contained_diffuse_terminal_closed=false`。该项把不持久 `Gamma` 分支的宽口径 `FiberDeletion/NoDeletion-KL/CleanKLS` 合成为严格二分：持续删除经支撑耗尽桥、HRO 下界路由、占位核路由与共同变量表只剩 `FixedShellLowModPersistencePDECOrColumnCRT`；删除停止且 KL/MI 偏斜回流 refined/new-layer PDEC；KL/MI 或多壳平坦才进入 CleanKLS/SC-9，且 K1--K9 失败回流命名出口。完全自足剩余还包括 `SelfContainedKuznetsovLSAtomSC9`，不能把外部 KLS 输入版误称为自足闭合。 |
| PDEC-CAP删除势-支撑耗尽桥 | 新增/发散后半段闭合 | 新增 `experiments/prime_matrix_pdec_cap_deletion_support_exhaustion_bridge.py` 与 `docs/monograph/prime-matrix-pdec-cap-deletion-support-exhaustion-bridge.md/json`。审查确认 `deletion_support_exhaustion_bridge_closed=true`、`global_deletion_divergence_closed=false`。该项把同源投影塔乘法公式、actual-payment 正需求责任、无名 sparse 入口排除和当前终端边界接合起来：一旦 `sum -log a_n=infinity`，活跃支撑密度趋零，不能继续作为 diffuse 正责任终端；剩余质量若集中或稀疏化则回流命名 `LocalSurvivor/SAE/PDEC/ColumnCRT/CleanKLS`。因此原 `GlobalDeletionDivergenceOrSupportExhaustion` 被压窄为 `GlobalDeletionPotentialDivergenceLowerBound`。 |
| PDEC-CAP删除发散下界路由 | 新增/压到占用饱和 | 新增 `experiments/prime_matrix_pdec_cap_deletion_divergence_lower_bound_router.py` 与 `docs/monograph/prime-matrix-pdec-cap-deletion-divergence-lower-bound-router.md/json`。审查确认 `deletion_divergence_lower_bound_reduced=true`、`global_deletion_divergence_closed=false`。HRO 引理给出 `S_t subset Occ_t union TI_t`；若删除势不发散，则正质量子列上 `Occ/r+TI/r->1`。`TI/r->1` 已是 NoDeletion-KL/CleanKLS 回流，所以删除侧唯一剩余为 `OccupancySaturationPDECOrColumnCRT`：证明旧洞 residue 近满占用触发低层容量矛盾、PDEC 或 ColumnCRT。 |
| PDEC-CAP占位饱和核路由 | 新增/压到稠密旧洞核 | 新增 `experiments/prime_matrix_pdec_cap_occupancy_saturation_kernel_router.py` 与 `docs/monograph/prime-matrix-pdec-cap-occupancy-saturation-kernel-router.md/json`。审查确认 `occupancy_saturation_reduced_to_dense_kernel=true`、`occupancy_saturation_closed=false`。HRO 注入界 `\|Occ_t\| <= min(\|H_Q(t)\|,r)` 排除旧洞稀疏或 residue 不满的占位饱和子情形；若占位仍近满，则必须存在近满旧洞选择核。删除侧新最窄硬点为 `DenseOldHoleKernelCapacityPDECOrColumnCRT`：证明该选择核触发低层容量过载、PDEC 相位偏斜或 ColumnCRT 列位移刚性。 |
| PDEC-CAP稠密旧洞共同变量表 | 新增/压到固定壳或SC9 | 新增 `experiments/prime_matrix_pdec_cap_dense_kernel_common_variable_router.py` 与 `docs/monograph/prime-matrix-pdec-cap-dense-kernel-common-variable-router.md/json`。审查确认 `dense_kernel_no_unnamed_escape_closed=true`、`dense_kernel_exclusion_closed=false`。把近满选择列写成 `c_b=rho_b+r k_b` 后，每个旧素数 `q\|Q` 都只是在同一个壳号变量 `k_b` 上禁止一个线性残基。于是无合法壳号是容量/Hall 删除；固定壳或有限壳包正密度是低模持久 `PDEC/ColumnCRT`；无固定壳持久就是多壳分散，非平坦频率回 `PDEC/ColumnCRT`，平坦频率进入自足 `SC-9`。新最窄不持久硬点为 `FixedShellLowModPersistencePDECOrColumnCRT_OR_SelfContainedKuznetsovLSAtomSC9`。 |
| PDEC-CAP持久有限签名统一 | 新增/平行持久硬点合并 | 新增 `experiments/prime_matrix_pdec_cap_persistent_signature_unification_router.py` 与 `docs/monograph/prime-matrix-pdec-cap-persistent-signature-unification-router.md/json`。审查确认 `persistent_signature_unification_closed=true`、`persistent_finite_signature_pdec_columncrt_closed=false`。持久 MFU 与固定壳低模持久都被改写为同一 formal unit 上的有限签名正密度；`ColumnCRT` 位移吸收到 displacement PDEC，PDEC 对偶失败吸收到 cap refinement，口径不一致吸收到 formal-unit normalization。因此当前最窄硬点不是两个平行分支，而是 `PersistentFiniteSignaturePDECColumnCRT_OR_SelfContainedKuznetsovLSAtomSC9`。 |
| PDEC-CAP/SC-9边界调和 | 新增/SC9非独立阻塞 | 新增 `experiments/prime_matrix_pdec_cap_sc9_boundary_reconciliation_router.py` 与 `docs/monograph/prime-matrix-pdec-cap-sc9-boundary-reconciliation-router.md/json`。审查确认 `pdec_cap_sc9_boundary_reconciled=true`、`canonical_sc9_independent_blocker_collapsed=true`。PDEC-CAP 终端中的 `SC-9` 只来自无持久有限签名后的 flat clean residual；clean 失败回流 PDEC/SAE，SC-9 已展开到 NC-BLK/外部 DI-BFI，canonical NC-BLK 已被同集容量边界吸收，generic WFD 分支不能纳入自足声明。因此当前 canonical-source 完全自足 PDEC-CAP 前沿只剩 `PersistentFiniteSignaturePDECColumnCRT`。 |
| PDEC-CAP持久终端准入 | 新增/压到primitive多原子门 | 新增 `experiments/prime_matrix_pdec_cap_persistent_terminal_admission_router.py` 与 `docs/monograph/prime-matrix-pdec-cap-persistent-terminal-admission-router.md/json`。审查确认 `persistent_terminal_admission_boundary_closed=true`、`current_materialized_persistent_terminal_instances_closed=true`、`primitive_multiatom_same_formal_unit_pdec_closed=false`。裸持久签名、裸 ColumnCRT、对偶失败、多重口径和二点 Fourier tautology 都不能直接作为终端；当前已物化 primitive 非二点候选为 `0`。未来唯一准入对象是同 formal unit、去重后三点以上、非二点 tautology、未被 LocalSurvivor/SAE/Endpoint 吸收的 `PrimitiveMultiAtomSameFormalUnitPDECCertificate`。 |
| PDEC-CAP primitive多原子秩边界 | 新增/压到二秩cap-stable核 | 新增 `experiments/prime_matrix_pdec_cap_primitive_multiatom_rank_router.py` 与 `docs/monograph/prime-matrix-pdec-cap-primitive-multiatom-rank-router.md/json`。审查确认 `primitive_multiatom_rank_boundary_closed=true`、`current_materialized_primitive_multiatom_instances_closed=true`。零秩/一秩 primitive 分支只能回到重复口径、二点 tautology、固定壳 PDEC/ColumnCRT 或 SAE；真正剩余压成 `RankTwoCapStablePrimitivePDECKernelInequality`。 |
| PDEC-CAP二秩cap-stable核 | 新增/核不等式逆否化 | 新增 `experiments/prime_matrix_pdec_cap_ranktwo_capstable_kernel_router.py` 与 `docs/monograph/prime-matrix-pdec-cap-ranktwo-capstable-kernel-router.md/json`。审查确认 `ranktwo_capstable_kernel_inequality_closed=true`。若某方向达到 `L_PDEC`，cap localization 给出方向帽质量下界并回流 SAE/refined PDEC/ColumnCRT/multiplicity；因此二秩核不等式转为 `UniformCapStabilityCertificateForRankTwoPrimitiveKernels`。 |
| PDEC-CAP统一帽稳定有限基 | 新增/连续方向帽离散化 | 新增 `experiments/prime_matrix_pdec_cap_uniform_cap_finite_basis_router.py` 与 `docs/monograph/prime-matrix-pdec-cap-uniform-cap-finite-basis-router.md/json`。审查确认 `uniform_cap_finite_basis_closed=true`。固定 finite formal unit 后，非平凡字符像是有限循环集，方向帽只是循环弧预像；连续 `zeta/alpha` 搜索压成 `FiniteCyclicArcCapMassBoundsForRankTwoPrimitiveKernels`。 |
| PDEC-CAP有限弧横向路由 | 新增/压到横向纤维扩张 | 新增 `experiments/prime_matrix_pdec_cap_finite_arc_transverse_router.py` 与 `docs/monograph/prime-matrix-pdec-cap-finite-arc-transverse-router.md/json`。审查确认 `finite_arc_no_unnamed_exit_closed=true`。高质量有限字符弧若低横向支撑则进 SAE/ColumnCRT/固定壳PDEC，若横向偏斜持久则进 refined PDEC，若横向平坦分散则进 CleanKLS/DLS 或外部大筛输入；最新最窄剩余为 `TransverseFiberExpansionForFiniteArcCaps`。 |
| PDEC-CAP横向clean归约 | 新增/压到横向商大筛原子 | 新增 `experiments/prime_matrix_pdec_cap_transverse_clean_reduction_router.py` 与 `docs/monograph/prime-matrix-pdec-cap-transverse-clean-reduction-router.md/json`。审查确认 `transverse_expansion_reduced_to_clean_atom=true`。有限弧只固定一个字符方向，二秩以上 primitive 核留下横向商；非平坦横向缺陷回流 SAE/refined PDEC/ColumnCRT，剩余为 `TransverseQuotientCleanLargeSieveAtom`。 |
| PDEC-CAP横向clean原子前沿 | 新增/大筛黑箱改写为证书边界 | 新增 `experiments/prime_matrix_pdec_cap_transverse_clean_atom_frontier_router.py` 与 `docs/monograph/prime-matrix-pdec-cap-transverse-clean-atom-frontier-router.md/json`。审查确认 `transverse_clean_atom_routed_to_named_frontier=true`：横向商 clean residual 接入 A1 `CleanKLS/SC-9`，K1--K9 失败回流 PDEC/SAE/ColumnCRT/Multiplicity，通过则进入实际系数 NC-BLK 或外部 DI/BFI。自足路线剩余为 `TransverseSourceSupportNonconcentrationCertificate`，即证明横向商系数继承 canonical RIW/Buchstab 源支撑下界或直接证明实际 transverse NC-BLK；外部原始 DI/BFI 路线剩余为 `DIBFIQuantifiedNoProjectionWindowCertificate`。 |
| PDEC-CAP横向源支撑路由 | 新增/来源链已压到 canonical 层 | 新增 `experiments/prime_matrix_pdec_cap_transverse_source_support_router.py` 与 `docs/monograph/prime-matrix-pdec-cap-transverse-source-support-router.md/json`。审查确认 `transverse_source_support_reduced=true`：A1/KZ-E actual-source provenance 已闭合到 canonical RIW/Buchstab pre-Cauchy 源，canonical RIW 支撑链压到 Buchstab 层，厚区间 squarefree 原始计数已闭合。该层先把自足路线压到 `TransverseFormalUnitA1SourceEmbedding`；嵌入成立后下游为 `CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn`，不走来源链则必须直接证明 `DirectTransverseNCBLKActualCoefficientNonConcentration`。 |
| PDEC-CAP横向来源嵌入路由 | 新增/有限测度函子性闭合 | 新增 `experiments/prime_matrix_pdec_cap_transverse_embedding_router.py` 与 `docs/monograph/prime-matrix-pdec-cap-transverse-embedding-router.md/json`。审查确认 `transverse_formal_unit_embedding_closed=true`：actual payment 是 canonical 源测度的确定性 first-cover 推前，有限签名塔是有限投影，方向弧是预像限制，横向商是有限因子/条件化，全链条没有重新加权或替换系数源。嵌入后剩余曾为 `CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn`。 |
| PDEC-CAP canonical层闭合路由 | 新增/最新自足硬点闭合 | 新增 `experiments/prime_matrix_pdec_cap_canonical_layer_closure_router.py` 与 `docs/monograph/prime-matrix-pdec-cap-canonical-layer-closure-router.md/json`。审查确认 `canonical_layer_transfer_closed=true`、`self_contained_canonical_branch_closed=true`：横向 formal unit 嵌入 canonical 源后，Buchstab 层准入/非零转移/薄块回流接入既有 A1 `selector retention -> finite signature -> decision tree -> actual source provenance -> branch boundary` 链，并由 canonical-source final boundary 吸收。`DIBFIQuantifiedNoProjectionWindowCertificate` 只保留为 generic/external 原始 DI/BFI 路线。 |
| PDEC-CAP自足边界提升路由 | 新增/canonical自足瓶颈解除 | 新增 `experiments/prime_matrix_self_contained_pdec_cap_boundary_lift_router.py` 与 `docs/monograph/prime-matrix-self-contained-pdec-cap-boundary-lift-router.md/json`。审查确认 `closed_nonfinal_lift_gates=true`、`canonical_source_self_contained_pdec_bottleneck_closed=true`：旧 `PDEC_CAP_SameSetGlobalDualCertificate` 不再是 canonical-source 自足分支的开放硬点；剩余 `DIBFIQuantifiedNoProjectionWindowCertificate` 只属于 generic/external 原始 DI/BFI 路线。完整行/列无条件定理仍未闭合，最终仍需全局终端家族晋级审查与 `DStructureRankinReferee`。 |
| canonical终端晋级闭合路由 | 新增/最新自足硬点闭合 | 新增 `experiments/prime_matrix_canonical_terminal_promotion_closure_router.py` 与 `docs/monograph/prime-matrix-canonical-terminal-promotion-closure-router.md/json`。审查确认 `latest_self_contained_hardpoint_closed=true`、`canonical_source_terminal_promotion_closed=true`、`open_self_contained_gates=[]`：当前已物化终端前沿耗尽、三终端无第四出口、PDEC-CAP 已由边界提升闭合、canonical `CleanKLS/NC-BLK` 被吸收或回流。因此 canonical-source 自足边界更新为 `NoFurtherCanonicalSourceTerminalPromotionGap`。完整行/列无条件定理仍未闭合；剩余为 generic/external `DIBFIQuantifiedNoProjectionWindowCertificate` 与 `DStructureRankinReferee` 最终晋级门。 |
| canonical-source自足命题最终闭合路由 | 新增/自足命题边界闭合 | 新增 `experiments/prime_matrix_canonical_source_self_contained_final_theorem_router.py` 与 `docs/monograph/prime-matrix-canonical-source-self-contained-final-theorem-router.md/json`。审查确认 `canonical_source_self_contained_theorem_closed=true`、`open_self_contained_gates=[]`、`terminal_boundary=NoFurtherCanonicalSourceSelfContainedTheoremBoundaryGap`。最终可声明的自足命题精确限于 canonical `RIW/Buchstab` 来源分支上的 Triad-A1 same-set/full-S terminal 与 canonical terminal promotion；不声明 unrestricted generic WFD 自足版，也不声明完整 Prime Matrix 行/列无条件定理。外部 `DIBFIQuantifiedNoProjectionWindowCertificate` 与 `DStructureRankinReferee` 保持在该自足边界之外。 |
| 完整全局无条件自足闭合阻断路由 | 新增/完整全局版需新增输入 | 新增 `experiments/prime_matrix_global_unconditional_self_contained_obstruction_router.py` 与 `docs/monograph/prime-matrix-global-unconditional-self-contained-obstruction-router.md/json`。审查确认 `current_corpus_global_unconditional_self_contained_closure_possible=false`、`row_column_unconditional_closed=false`。完整全局无条件自足闭合至少还需 `ActualA1FullSSourceLockTheorem_OR_FullSNonAPStrengthenedSourceAntiAtom`、`NoProjectionUncenteredDispersionIdentity`、`QuantifiedDIBFIWindowSubstitution` 与 `DStructureTailLog4FiniteRankinIndependentAcceptance`。因此当前只能声明 canonical-source 自足命题闭合，不能声明完整全局无条件行/列命题闭合。 |
| actual-source bridge全局调和 | 新增/canonical桥闭合，补集仍开 | 新增 `experiments/prime_matrix_actual_source_bridge_global_reconciliation_router.py` 与 `docs/monograph/prime-matrix-actual-source-bridge-global-reconciliation-router.md/json`。审查确认 `actual_source_bridge_closed_for_canonical_branch=true`、`actual_source_bridge_closes_global_unrestricted=false`：旧阻断门 `ActualFullSSourceBridge` 已在 canonical 分支内吸收，应替换为更精确的 `NoncanonicalFullSComplementAntiAtomOrExternalDIBFI`。完整全局版仍需处理 noncanonical full-S 补集、强化 source anti-atom 或外部 DI/BFI。 |
| noncanonical full-S补集输入合同 | 新增/必要输入边界闭合 | 新增 `experiments/prime_matrix_noncanonical_complement_input_contract_router.py` 与 `docs/monograph/prime-matrix-noncanonical-complement-input-contract-router.md/json`。审查确认 `contract_boundary_closed=true`、`canonical_branch_removed_from_remainder=true`、`generic_wfd_template_available=false`、`noncanonical_complement_closed_by_current_corpus=false`。该项闭合的是必要输入边界：扣除 canonical 分支后，generic WFD 模板已被 moving-delta 阻断，剩余只能走实际源恒等、实际源强化反原子、外部/量化 DI/BFI 与最终 DStructure/Rankin 晋级门；不能据此宣称完整行/列无条件定理闭合。 |
| 行命题闭合输入图谱 | 新增/最小输入基固定 | 新增 `experiments/prime_matrix_closure_input_atlas_router.py` 与 `docs/monograph/prime-matrix-closure-input-atlas-router.md/json`。图谱回顾 Full CRT/MinRep、方阵斜线/圆柱覆盖、第 P 列锚点、层叠轮筛、远尾互补因子、SN 递归剥离、命名出口吸收、PDEC cap 细化、canonical-source 分支和 noncanonical 补集。审查确认 `canonical_source_self_contained_closed=true`、`noncanonical_input_contract_closed=true`、`row_column_unconditional_closed=false`；最小闭合输入基固定为 `TerminalCertificatePackage`、`NoncanonicalFullSComplementPackage`、`DStructureRankinPromotionPackage`。 |
| 终端证书包压缩路由 | 新增/第一包独立输入缩为三证书族 | 新增 `experiments/prime_matrix_terminal_certificate_package_compression_router.py` 与 `docs/monograph/prime-matrix-terminal-certificate-package-compression-router.md/json`。审查确认 `terminal_package_compression_closed=true`、`terminal_package_fully_proved=false`：无名逃逸和命名出口吸收已是闭合合同，canonical 分支的 `CleanMultishellKLS` 已被最终边界吸收，`TotalDescent` 要么到 `p=2` 要么首阻断 seam 回流 `PDEC/ColumnCRT/SAE`。因此第一包真正独立剩余压成三类：全局 `SAE` 证书族、全部 persistent family 的 `PDEC` 显式/对偶证书、`ColumnCRT` 排斥或回流 `PDEC/SAE` 证书。 |
| ColumnCRT到PDEC/SAE吸收路由 | 新增/第一包独立输入缩为两证书族 | 新增 `experiments/prime_matrix_columncrt_to_pdec_sae_absorption_router.py` 与 `docs/monograph/prime-matrix-columncrt-to-pdec-sae-absorption-router.md/json`。审查确认 `columncrt_independent_terminal_removed=true`：`ColumnCRT` 固定非零位移入口是真实结构，但不是独立第三终端；持久过载改写为 displacement/endpoint/cofactor/primitive `PDEC`，孤立过载进入 `SAE`，平衡负载成为 PDEC 对偶约束行。第一包独立剩余进一步压成全局 `SAE` 证书族与广义 `PDEC` 证书族两类。 |
| SAE到LocalSurvivor/PDEC吸收路由 | 新增/第一包独立SAE终端删除 | 新增 `experiments/prime_matrix_sae_to_local_survivor_pdec_absorption_router.py` 与 `docs/monograph/prime-matrix-sae-to-local-survivor-pdec-absorption-router.md/json`。审查确认 `sae_independent_terminal_removed=true`：当前已物化 `LocalSurvivor/SAE` 包清零，已知入口 extractor 覆盖清零，无名 sparse 入口审计清零；孤窗若可抽取则必须给有限 packet 的 witness/deficit，若同签名持久复现则回流 `PDEC/ColumnCRT/TailAnchor/CofactorAnchor`，若层级逃逸则进入 `CleanKLS/DLS` 或外部输入。第一包当前结构剩余压成广义 `PDEC` 证书族，以及未来新增显式 sparse 路线必须附带的 extractor schema 义务；仍不得宣称完整行/列无条件闭合。 |
| Noncanonical补集三歧边界路由 | 新增/第二包边界闭合输入仍条件 | 新增 `experiments/prime_matrix_noncanonical_complement_trilemma_router.py` 与 `docs/monograph/prime-matrix-noncanonical-complement-trilemma-router.md/json`。审查确认 `trilemma_boundary_closed=true`、`self_contained_noncanonical_package_closed=false`、`external_contract_package_closed_if_fulls_kls_ext_accepted=true`：扣除 canonical `RIW/Buchstab` 分支后，generic full-S 自足反原子被 moving-delta capacity 反例排除；第二包只能走实际源恒等、强化实际源反原子，或接受/证明 `FullS-KLS-ext` / `FullSNonAPWFDKLSTheoremInput`。若坚持完全自足或逐页原文核验，仍需 `DIBFIPrimarySourceSpecializationProof`；完整行/列无条件定理仍未闭合。 |
| DStructure/Rankin晋级验收边界路由 | 新增/第三包边界闭合验收未完成 | 新增 `experiments/prime_matrix_dstructure_rankin_promotion_acceptance_router.py` 与 `docs/monograph/prime-matrix-dstructure-rankin-promotion-acceptance-router.md/json`。审查确认 `promotion_package_boundary_closed=true`、`promotion_package_independently_accepted=false`、`rankin_sample_pass=true`：第三包不再是模糊最终障碍，而是 D-structure/Structured-EHPD、Tail-log4 BG/RKS 适配、有限验证复现、全部正式着色走廊 Rankin 证书，以及独立审稿接受的验收清单。Rankin 样本 `core_count_exact=39`、`allowed_budget=40.0`，Rankin/exact 均通过，但正式全集和独立验收仍未完成，完整行/列无条件定理仍不能声明。 |
| PDEC family显式输入边界路由 | 新增/当前PDEC前沿清零未来需schema | 新增 `experiments/prime_matrix_pdec_family_explicit_input_boundary_router.py` 与 `docs/monograph/prime-matrix-pdec-family-explicit-input-boundary-router.md/json`。审查确认 `pdec_family_explicit_input_boundary_closed=true`、`current_materialized_pdec_frontier_closed=true`、`canonical_source_pdec_cap_closed=true`、`global_pdec_family_unconditional_closed=false`：当前已物化合法非二点 primitive `PDEC` 候选为零，canonical-source `PDEC-CAP` 已接回最终自足边界；未来若引入真正 `PDEC` 障碍，必须提交同 formal unit、三物理原子以上、非二点 tautology、二秩以上、cap-stable 且未被 sparse/ColumnCRT/CleanKLS 吸收的显式 schema。完整行/列无条件定理仍未闭合。 |
| Future sparse packet extractor schema边界路由 | 新增/当前sparse前沿清零未来需schema | 新增 `experiments/prime_matrix_future_sparse_packet_extractor_schema_boundary_router.py` 与 `docs/monograph/prime-matrix-future-sparse-packet-extractor-schema-boundary-router.md/json`。审查确认 `future_sparse_packet_schema_boundary_closed=true`、`current_materialized_sparse_frontier_closed=true`、`global_sparse_family_unconditional_closed=false`：当前 `LocalSurvivor/SAE` 物化包无开放义务，已知入口 extractor 全覆盖，当前合同体系无无名 sparse 入口；未来新增 sparse 路线必须提交有限窗口/候选集、blocker 投影、witness 或严格 deficit、有限签名持久性测试、层级逃逸测试和可复现账本。不给 schema 就回流 `PDEC/ColumnCRT/Tail/Cofactor` 或 `CleanKLS/DLS`；完整行/列无条件定理仍未闭合。 |
| 最终输入防火墙边界路由 | 新增/无隐藏终端但最终输入未接受 | 新增 `experiments/prime_matrix_final_input_firewall_boundary_router.py` 与 `docs/monograph/prime-matrix-final-input-firewall-boundary-router.md/json`。审查确认 `final_input_firewall_boundary_closed=true`、`current_materialized_terminal_frontier_closed=true`、`no_hidden_terminal_remaining=true`、`all_final_inputs_independently_accepted=false`、`row_column_unconditional_closed=false`：当前已物化 `PDEC` 与 sparse/LocalSurvivor 前沿均清零，noncanonical 分支和 `DStructure/Rankin` 晋级门均已命名；剩余只能作为四类显式输入进入：`FutureExplicitPrimitivePDECSchema`、`FutureExplicitSparsePacketExtractorSchema`、`NoncanonicalFullSComplementTrilemma`、`DStructureRankinPromotion`。该项闭合边界和命名性，不闭合完整无条件定理。 |
| 四开放输入攻坚路由 | 新增/条件链完整无条件仍开 | 新增 `experiments/prime_matrix_four_open_inputs_closure_attack_router.py` 与 `docs/monograph/prime-matrix-four-open-inputs-closure-attack-router.md/json`。审查确认 `current_materialized_frontier_zero=true`、`no_hidden_terminal_remaining=true`、`conditional_closure_chain_complete=true`、`all_current_obligations_closed=false`、`unconditional_closure_possible_from_current_corpus=false`：四类最终输入逐项硬攻后，`FutureExplicitPrimitivePDECSchema` 与 `FutureExplicitSparsePacketExtractorSchema` 在当前材料中无实际待证义务，只是未来新增路线准入防火墙；真正当前开放输入是 `NoncanonicalFullSComplementTrilemma` 与 `DStructureRankinPromotion`。形成条件闭合定理：若 noncanonical 三歧至少一支被证明/接受且 DStructure/Rankin 晋级包独立接受，则当前无隐藏终端链可升级为完整闭合；没有这些新输入时，当前材料不能诚实推出完整无条件定理。 |
| Noncanonical最终压窄路由 | 新增/noncanonical压成两真实输入 | 新增 `experiments/prime_matrix_noncanonical_final_narrowing_router.py` 与 `docs/monograph/prime-matrix-noncanonical-final-narrowing-router.md/json`。审查确认 `noncanonical_narrowing_boundary_closed=true`、`ap_source_lift_rejected=true`、`generic_self_contained_antiatom_refuted=true`、`exact_source_entropy_closed=false`、`external_full_s_contract_closed_if_accepted=true`、`self_contained_noncanonical_closed=false`：canonical 分支已移出，`APSourceLift` 被 AP/non-AP 分支定义和对象账本阻断，generic 自足反原子被 moving-delta 反证；noncanonical 最窄剩余只剩两项真实输入：内部新增 `ExactWFDSourceEntropy / FullSNonAPStrengthenedSourceAntiAtom`，或外部/新证 `FullSNonAPWFDKLSTheoremInput`。 |
| 最后剩余原子路由 | 新增/最终开放输入原子化 | 新增 `experiments/prime_matrix_last_remaining_atoms_router.py` 与 `docs/monograph/prime-matrix-last-remaining-atoms-router.md/json`。审查确认 `last_remaining_atom_boundaries_closed=true`、`conditional_logic_chain_complete=true`、`all_last_atoms_proved_or_accepted=false`、`row_column_unconditional_closed=false`：当前 PDEC/sparse 物化前沿清零且只保留未来 schema 防火墙，noncanonical 方向压成 `ActualFullSNonAPExactSupportAtom` 或 `ModulusDependentCompletedFullSKLSInput`，最终晋级压成 `DStructureRankinIndependentAcceptance`。因此最后条件闭合定理为：若前两者之一成立，并且 `DStructureRankinIndependentAcceptance` 独立成立，则无隐藏终端链可升级为完整行/列闭合；当前材料尚未证明或接受这些最后原子，不能声明完整全局无条件定理已证。 |
| 三个最终原子硬攻路由 | 新增/压成数学二选一+独立晋级 | 新增 `experiments/prime_matrix_three_final_atoms_hard_attack_router.py` 与 `docs/monograph/prime-matrix-three-final-atoms-hard-attack-router.md/json`。审查确认 `three_atom_attack_boundary_closed=true`、`conditional_logic_chain_complete=true`、`all_three_atoms_proved_or_accepted=false`、`row_column_unconditional_closed=false`：`ActualFullSNonAPExactSupportAtom` 继续压成 actual source 无 moving atom 反原子 `ActualFullSNonAPSourceCapacityAntiAtomForActualSource`；`ModulusDependentCompletedFullSKLSInput` 继续压成 `CDependentResidueWeightSpectralCancellationInput`；`DStructureRankinIndependentAcceptance` 继续压成正式全集 `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。最小无条件输入基更新为 `(ActualFullSNonAPSourceCapacityAntiAtomForActualSource OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`；当前材料仍未证明这些新增输入。 |
| 最终无条件闭合尝试路由 | 新增/不可再压缩输入基固定 | 新增 `experiments/prime_matrix_unconditional_closure_final_attempt_router.py` 与 `docs/monograph/prime-matrix-unconditional-closure-final-attempt-router.md/json`。审查确认 `final_attempt_boundary_closed=true`、`math_lanes_collapsed_to_common_core=true`、`internal_math_proof_found_in_current_corpus=false`、`external_math_match_found_in_current_corpus=false`、`independent_promotion_acceptance_completed=false`、`row_column_unconditional_closed=false`：二选一数学输入已经汇合到 `MovingBlockSpreadNCBLKForActualFullSNonAPWFDCoefficients` 或精确匹配外部 `DIBFI/Kuznetsov` dispersion；generic 反原子被 moving-delta 反证，fixed-projection 不能控制 moving label，外部定理尚未逐项匹配，独立晋级验收也未完成。最终不可再压缩输入基为 `(MovingBlockSpreadNCBLKForActualFullSNonAPWFDCoefficients OR PreciselyMatchedExternalDIBFIKuznetsovDispersionTheorem) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。当前材料完成终局输入边界闭合，但不能无条件闭合行/列命题。 |
| 不可约数学输入精化路由 | 新增/外部标签精化为 Full-S KLS 输入 | 新增 `experiments/prime_matrix_irreducible_math_input_refinement_router.py` 与 `docs/monograph/prime-matrix-irreducible-math-input-refinement-router.md/json`。审查确认 `refinement_boundary_closed=true`、`existing_primary_dibfi_match_rejected=true`、`ap_source_lift_rejected=true`、`new_full_s_kls_theorem_proved_or_cited_in_current_corpus=false`、`row_column_unconditional_closed=false`：现有 BFI AP 定理和 DI/Maynard J-scale 不能逐项推出当前 full-S、non-AP、未中心化、无投影 WFD 对象，`APSourceLift` 也被对象账本拒绝。因此上一轮的 `PreciselyMatchedExternalDIBFIKuznetsovDispersionTheorem` 需诚实精化为 `FullSNonAPWFDKLSTheoremInput`。最新输入基为 `(MovingBlockSpreadNCBLKForActualFullSNonAPWFDCoefficients OR FullSNonAPWFDKLSTheoremInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`；这仍是边界闭合，不是无条件定理证明。 |
| Full-S KLS / Moving-Block 联合硬攻路由 | 新增/内部路压成 exact support 包 | 新增 `experiments/prime_matrix_fulls_kls_movingblock_joint_attack_router.py` 与 `docs/monograph/prime-matrix-fulls-kls-movingblock-joint-attack-router.md/json`。审查确认 `joint_attack_boundary_closed=true`、`internal_lane_proved_in_current_corpus=false`、`external_lane_proved_or_cited_in_current_corpus=false`、`dstructure_rankin_independent_acceptance_completed=false`、`row_column_unconditional_closed=false`：canonical RIW/Buchstab 分支已闭合且不能偷渡到 noncanonical full-S 补集；内部 moving-block 路继续降到 `FullSNonAPExactFactorSupportPackageForActualNoncanonicalSource`，外部路仍是 `FullSNonAPWFDKLSTheoremInput`。最新输入基为 `(FullSNonAPExactFactorSupportPackageForActualNoncanonicalSource OR FullSNonAPWFDKLSTheoremInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。BFI/DI/Maynard 外部主来源提供谱与 dispersion 技术，但尚未逐项覆盖 c-dependent residue weights、未中心化、无投影、full-S、non-AP 和任意对数节省。 |
| 内外两线终端归约路由 | 新增/压成反原子或 c-dependent 谱输入 | 新增 `experiments/prime_matrix_dual_lane_terminal_reduction_router.py` 与 `docs/monograph/prime-matrix-dual-lane-terminal-reduction-router.md/json`。审查确认 `terminal_reduction_boundary_closed=true`、`internal_lane_closed=false`、`external_lane_closed=false`、`rankin_promotion_accepted=false`、`row_column_unconditional_closed=false`：内部线的 `FullSNonAPBalancedRangeThreshold` 已在 full-S regime 下闭合，exact factor support 与 Type/Fourier 容量兼容合并为 `FullSNonAPStrengthenedSourceAntiAtomContractForActualNoncanonicalSource`；外部线的 full-S 窗口已按模 `c` 完成，`FullSNonAPWFDKLSTheoremInput` 压成 `CDependentResidueWeightSpectralCancellationInput`。最新输入基为 `(FullSNonAPStrengthenedSourceAntiAtomContractForActualNoncanonicalSource OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。 |
| 内外两线共同核心调和路由 | 新增/外部线若自证则回到内部源核心 | 新增 `experiments/prime_matrix_dual_lane_common_core_reconciliation_router.py` 与 `docs/monograph/prime-matrix-dual-lane-common-core-reconciliation-router.md/json`。审查确认 `common_core_reconciliation_closed=true`、`self_contained_common_core_proved=false`、`external_contract_accepted_as_final_input=false`、`dstructure_rankin_independent_acceptance_completed=false`、`row_column_unconditional_closed=false`：`CDependentResidueWeightSpectralCancellationInput` 若作为外部 FullS-KLS/c-dependent 谱定理接受，则给出外部合同输入；若从当前材料内部证明，则有限 Fourier completion 会回到 BWFD/BSC/KFLS，再回到 actual same-(u,v) block non-concentration，与内部强化源反原子是同一个 moving-block 核心。调和后输入基为 `((ActualA1FullSSourceLockOrNewFullSNonAPSourceAntiAtomTheoremInput) OR AcceptedFullSKLSExtOrCDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`；完全自足版输入基为 `ActualA1FullSSourceLockOrNewFullSNonAPSourceAntiAtomTheoremInput AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。该项闭合两线独立性缺口，但仍未证明自足源核心，也未完成 DStructure/Rankin 独立验收。 |
| 完全自足最窄核心路由 | 新增/source-lock从全局剩余删除 | 新增 `experiments/prime_matrix_self_contained_narrowest_core_router.py` 与 `docs/monograph/prime-matrix-self-contained-narrowest-core-router.md/json`。审查确认 `narrowest_core_reduction_closed=true`、`canonical_source_lock_absorbed_for_canonical_branch=true`、`source_lock_option_removed_from_global_remainder=true`、`external_black_box_used=false`、`generic_self_contained_antiatom_available=false`、`noncanonical_actual_source_core_proved=false`、`dstructure_rankin_independent_acceptance_completed=false`、`row_column_unconditional_closed=false`：canonical source-lock 已被 canonical RIW/Buchstab 分支吸收，不能作为 unrestricted/global 剩余继续计入；generic full-S 自足反原子已被 moving-delta 反证。因此完全自足全局版最窄输入基更新为 `ActualNoncanonicalFullSSourceEntropyOrStrengthenedAntiAtomTheoremInput AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。该项闭合 source-lock/global-complement 歧义，但仍未证明 actual noncanonical source entropy，也未完成 DStructure/Rankin 独立验收。 |
| noncanonical源核心原子化路由 | 新增/entropy与anti-atom合并为支撑容量原子 | 新增 `experiments/prime_matrix_noncanonical_source_core_atomization_router.py` 与 `docs/monograph/prime-matrix-noncanonical-source-core-atomization-router.md/json`。审查确认 `source_core_atomization_closed=true`、`entropy_antiatom_duality_removed=true`、`balanced_range_threshold_closed=true`、`k4_k6_or_naive_incidence_suffices=false`、`canonical_import_allowed=false`、`actual_support_capacity_core_proved=false`、`dstructure_rankin_independent_acceptance_completed=false`、`row_column_unconditional_closed=false`：`source entropy` 与 `strengthened anti-atom` 不是两条独立自足路线，而是同一个 actual noncanonical full-S 源支撑/容量核心；balanced range 已闭合，K4/K6、朴素 incidence 与 canonical RIW/Buchstab 支撑偷渡均不能证明该核心。完全自足最新输入基更新为 `ActualNoncanonicalFullSFactorSupportCapacityTheoremInput AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。该项闭合命名二义性和伪捷径排除，但仍未证明 actual 支撑/容量核心。 |
| actual容量账本微原子路由 | 新增/支撑与容量口径分离 | 新增 `experiments/prime_matrix_actual_capacity_ledger_microatom_router.py` 与 `docs/monograph/prime-matrix-actual-capacity-ledger-microatom-router.md/json`。审查确认 `microatom_boundary_closed=true`、`support_only_suffices=false`、`registered_multiplier_discipline_would_suffice_with_support=true`、`exact_uv_support_proved=false`、`registered_multiplier_discipline_proved=false`、`actual_final_capacity_antiatom_proved=false`、`dstructure_rankin_independent_acceptance_completed=false`、`row_column_unconditional_closed=false`：raw `u/v` 支撑下界不能单独替代最终 source anti-atom，因为 Type/Fourier/fiber 阶段若有未登记容量乘子，单个 moving `(u,v)` 对仍可承载大容量。最新单原子表述为 `ActualFinalCapacityAntiAtomLedgerForNoncanonicalFullS`；可行证明包为 `ActualNoncanonicalExactUVSupportLowerBound AND ActualTypeFourierRegisteredCapacityMultiplierDiscipline`。该项闭合支撑-only 偷换与条件蕴含公式，不是 actual 容量反原子定理证明。 |
| 注册容量乘子纪律路由 | 新增/两个源微输入压成一个 | 新增 `experiments/prime_matrix_registered_capacity_multiplier_discipline_router.py` 与 `docs/monograph/prime-matrix-registered-capacity-multiplier-discipline-router.md/json`。审查确认 `registered_capacity_multiplier_discipline_closed=true`、`exact_uv_support_proved=false`、`actual_final_capacity_antiatom_proved=false`、`dstructure_rankin_independent_acceptance_completed=false`、`row_column_unconditional_closed=false`：Type 分解、dyadic、CRT、Fourier 尾项、gcd、平滑、full-S completion fiber 与 tail-label 成本都已登记为同一 actual formal unit 中的 log-power 乘子；本步没有调用外部 DI/BFI no-projection，也没有证明支撑下界。因此完全自足源核心从两个微输入压成单个 `ActualNoncanonicalExactUVSupportLowerBound`，另加 `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。 |
| ExactUVSupport终端攻击路由 | 新增/唯一源侧终端输入固定 | 新增 `experiments/prime_matrix_exact_uv_support_terminal_attack_router.py` 与 `docs/monograph/prime-matrix-exact-uv-support-terminal-attack-router.md/json`。审查确认 `exact_uv_support_terminal_boundary_closed=true`、`registered_capacity_multiplier_discipline_closed=true`、`exact_uv_support_proved=false`、`actual_final_capacity_antiatom_proved=false`、`dstructure_rankin_independent_acceptance_completed=false`、`row_column_unconditional_closed=false`：乘子纪律已闭合，canonical 分支支撑链已由 canonical-source 边界吸收，但 canonical 支撑不能导入 noncanonical full-S 补集；formal WFD、K4/K6、朴素 incidence 和 raw Buchstab 计数也不能推出 actual noncanonical exact `u/v` 支撑。当前唯一源侧终端输入固定为 `ActualNoncanonicalExactUVSupportLowerBound`，另加 DStructure/Rankin 独立验收。 |
| ExactUVSupport失败包化路由 | 新增/抽象源输入转成 packet 排斥 | 新增 `experiments/prime_matrix_exact_uv_support_failure_packetization_router.py` 与 `docs/monograph/prime-matrix-exact-uv-support-failure-packetization-router.md/json`。审查确认 `failure_packetization_closed=true`、`exact_uv_support_proved=false`、`actual_support_failure_packet_exclusion_proved=false`、`actual_final_capacity_antiatom_proved=false`、`dstructure_rankin_independent_acceptance_completed=false`、`row_column_unconditional_closed=false`：在 actual noncanonical clean block、exact `u/v` 支撑定义和 registered multiplier 阈值固定后，`ActualNoncanonicalExactUVSupportLowerBound` 等价改写为不存在正质量 `ActualNoncanonicalSupportFailurePacket`。支撑失败若发生，必须携带 source class、formal unit、block key、支撑集合、阈值、容量剖面、回流测试和可复现证书；当前材料尚未证明所有 packet 不存在或必回流。最新等价输入基为 `ActualNoncanonicalSupportFailurePacketExclusion AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。 |
| 支撑失败packet回流二分路由 | 新增/第五类隐藏终端删除 | 新增 `experiments/prime_matrix_support_failure_packet_return_dichotomy_router.py` 与 `docs/monograph/prime-matrix-support-failure-packet-return-dichotomy-router.md/json`。审查确认 `support_failure_packet_return_dichotomy_closed=true`、`clean_core_packet_exclusion_proved=false`、`actual_final_capacity_antiatom_proved=false`、`dstructure_rankin_independent_acceptance_completed=false`、`row_column_unconditional_closed=false`：支撑失败 packet 若不是 clean-core，必须回流到有限孤立 `LocalSurvivor/SAE` packet、持久 primitive `PDEC` schema、ColumnCRT/位移吸收、漂移 `CleanKLS/DLS` 或已阻断逃逸，不能成为第五类终端。源侧最新最窄微输入为 `ActualNoncanonicalCleanCoreSupportFailurePacketExclusion`，连同 `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`；当前材料尚未证明 clean-core packet 不存在。 |
| clean-core moving atom精确输入路由 | 新增/源侧sharp输入校准 | 新增 `experiments/prime_matrix_clean_core_moving_atom_sharp_input_router.py` 与 `docs/monograph/prime-matrix-clean-core-moving-atom-sharp-input-router.md/json`。审查确认 `clean_core_moving_atom_sharp_boundary_closed=true`、`clean_core_moving_atom_exclusion_proved=false`、`actual_final_capacity_antiatom_proved=false`、`dstructure_rankin_independent_acceptance_completed=false`、`row_column_unconditional_closed=false`：排斥所有 clean-core 低支撑 packet 足以闭合但过强；registered multiplier discipline 闭合后，最终容量大原子的逆否会给出支撑失败 packet，因此终局 sharp 输入是排斥 clean-core final capacity measure 的 moving same-`(u,v)` 大原子。最新输入基为 `ActualNoncanonicalCleanCoreMovingAtomExclusion AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`；当前材料尚未证明该 moving atom 排斥。 |
| clean-core终局输入标准形路由 | 新增/终局输入标准形闭合 | 新增 `experiments/prime_matrix_clean_core_terminal_normal_form_router.py` 与 `docs/monograph/prime-matrix-clean-core-terminal-normal-form-router.md/json`。审查确认 `clean_core_terminal_normal_form_closed=true`、`internal_exact_entropy_proved=false`、`external_completed_kls_accepted=false`、`dstructure_rankin_independent_acceptance_completed=false`、`row_column_unconditional_closed=false`：`ActualNoncanonicalCleanCoreMovingAtomExclusion` 的内部标准形是 `ExactCleanCoreFullSNonAPWFDSourceEntropy`，外部替代标准形是 completed、modulus-dependent 的 `ModulusDependentCompletedFullSKLSInput`，不能泛称 DI/BFI 或普通 KLS。最新条件输入基为 `(ExactCleanCoreFullSNonAPWFDSourceEntropy OR ModulusDependentCompletedFullSKLSInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`；完全自足输入基为 `ExactCleanCoreFullSNonAPWFDSourceEntropy AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。当前材料仅闭合命名和输入边界，仍未证明 exact entropy、接受 completed KLS，或完成 DStructure/Rankin 独立验收。 |
| clean-core exact entropy原子路由 | 新增/可行动证明包压到终端支撑原子 | 新增 `experiments/prime_matrix_clean_core_exact_entropy_atom_router.py` 与 `docs/monograph/prime-matrix-clean-core-exact-entropy-atom-router.md/json`。审查确认 `clean_core_exact_entropy_atom_boundary_closed=true`、`clean_core_terminal_support_incidence_proved=false`、`exact_clean_core_entropy_proved=false`、`dstructure_rankin_independent_acceptance_completed=false`、`row_column_unconditional_closed=false`：若 `ExactCleanCoreFullSNonAPWFDSourceEntropy` 失败，则存在 clean-core moving 大原子；registered multiplier 已关闭账外容量逃逸，packetization 与非 clean-core 回流已关闭隐藏出口，因此失败只能表现为通过全部回流测试的 clean-core terminal support atom。最新可行动自足证明包为 `CleanCoreTerminalSupportIncidenceTheorem AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`；当前材料尚未证明该支撑-关联定理。 |
| clean-core支撑关联终端攻击路由 | 新增/剩余压到exact层承认与非零转移 | 新增 `experiments/prime_matrix_clean_core_support_incidence_attack_router.py` 与 `docs/monograph/prime-matrix-clean-core-support-incidence-attack-router.md/json`。审查确认 `clean_core_support_incidence_attack_boundary_closed=true`、`clean_core_exact_layer_transfer_proved=false`、`clean_core_terminal_support_incidence_proved=false`、`external_completed_kls_accepted=false`、`dstructure_rankin_independent_acceptance_completed=false`、`row_column_unconditional_closed=false`：full-S range、registered capacity budget、厚区间 raw squarefree/Buchstab 计数与 support=>entropy 推出都已闭合；朴素 factor-residue incidence 被内部 fiber 阻断，canonical 支撑不能导入 noncanonical clean-core，普通计数不能替代 exact 层承认。最新条件输入基为 `(CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn OR ModulusDependentCompletedFullSKLSInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`；完全自足输入基为 `CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。当前材料尚未证明 clean-core exact 层承认、非零系数转移和 thin/rejected block 回流定理。 |
| clean-core层转移路径分割路由 | 新增/剩余压到actual系数路径账本 | 新增 `experiments/prime_matrix_clean_core_layer_transfer_path_router.py` 与 `docs/monograph/prime-matrix-clean-core-layer-transfer-path-router.md/json`。审查确认 `clean_core_layer_transfer_path_boundary_closed=true`、`clean_core_path_partition_proved=false`、`clean_core_exact_layer_transfer_proved=false`、`external_completed_kls_accepted=false`、`dstructure_rankin_independent_acceptance_completed=false`、`row_column_unconditional_closed=false`：selector retention 与有限路径签名 pigeonhole 模板可用，canonical RIW/Buchstab 决策树和来源账本已闭合但只覆盖 canonical-source 分支，不能导入 clean-core noncanonical 残余。最新条件输入基为 `(CleanCoreExactCoefficientPathPartitionNoCancellationAndThinReturn OR ModulusDependentCompletedFullSKLSInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`；完全自足输入基为 `CleanCoreExactCoefficientPathPartitionNoCancellationAndThinReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。当前材料尚未证明 actual clean-core 系数的 polylog 互斥路径分割、同路径非零/无抵消及薄块/失败回流。 |
| clean-core路径来源防火墙路由 | 新增/剩余压到pre-Cauchy系数来源律 | 新增 `experiments/prime_matrix_clean_core_path_source_firewall_router.py` 与 `docs/monograph/prime-matrix-clean-core-path-source-firewall-router.md/json`。审查确认 `clean_core_path_source_firewall_boundary_closed=true`、`clean_core_precauchy_source_law_proved=false`、`clean_core_path_partition_proved=false`、`external_spectral_atom_accepted=false`、`dstructure_rankin_independent_acceptance_completed=false`、`row_column_unconditional_closed=false`：路径分割、无抵消和路径数预算必须建立在 Cauchy/dispersion 前的 actual clean-core `alpha/delta` 来源公式上；canonical 决策树只限 canonical-source 分支，generic WFD 形式被 moving-delta 阻断。最新条件输入基为 `(CleanCorePreCauchyCoefficientSourceLawAndReturn OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`；完全自足输入基为 `CleanCorePreCauchyCoefficientSourceLawAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。当前材料尚未证明 clean-core pre-Cauchy 来源律，也未接受 c-dependent residue weight 谱输入。 |
| clean-core pre-Cauchy来源律原子化路由 | 新增/剩余压到原始生成账本 | 新增 `experiments/prime_matrix_clean_core_precauchy_source_law_atom_router.py` 与 `docs/monograph/prime-matrix-clean-core-precauchy-source-law-atom-router.md/json`。审查确认 `clean_core_precauchy_source_law_atom_boundary_closed=true`、`origin_generation_ledger_implication_closed=true`、`clean_core_original_coefficient_generation_ledger_proved=false`、`clean_core_precauchy_source_law_proved=false`、`external_spectral_atom_accepted=false`、`dstructure_rankin_independent_acceptance_completed=false`、`row_column_unconditional_closed=false`：pre-Cauchy 来源律不是新的统计估计，而是 actual clean-core `alpha/delta` 在 Cauchy/dispersion 前的同一 formal unit 原始生成账本问题。若该账本列出所有 summand、branch key、u/v map、符号和 local factor，则路径签名、polylog 路径预算、同路径非零/无抵消和失败回流由账本纪律推出；反过来任何来源律证明都必须至少给出这张表。最新条件输入基为 `(CleanCoreOriginalCoefficientGenerationLedgerAndReturn OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`；完全自足输入基为 `CleanCoreOriginalCoefficientGenerationLedgerAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。当前材料尚未证明 clean-core 原始生成账本。 |
| clean-core原始来源准入路由 | 新增/剩余压到primitive source constructor准入 | 新增 `experiments/prime_matrix_clean_core_origin_source_admission_router.py` 与 `docs/monograph/prime-matrix-clean-core-origin-source-admission-router.md/json`。审查确认 `clean_core_origin_source_admission_boundary_closed=true`、`constructor_admission_implies_origin_ledger=true`、`unregistered_source_return_absorbed=false`、`clean_core_primitive_source_constructor_admission_proved=false`、`clean_core_original_coefficient_generation_ledger_proved=false`、`external_spectral_atom_accepted=false`、`dstructure_rankin_independent_acceptance_completed=false`、`row_column_unconditional_closed=false`：原始生成账本的入口不是估计，而是来源准入；必须先证明 actual clean-core `alpha/delta` 由某个 pre-Cauchy primitive source constructor 生成。构造器准入后，emitted summand schema 可展开为原始生成账本；构造器缺失则必须作为未登记来源回流，不能继续当作 clean-core 终端。最新条件输入基为 `(CleanCorePrimitiveSourceConstructorAdmissionAndReturn OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`；完全自足输入基为 `CleanCorePrimitiveSourceConstructorAdmissionAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。当前材料尚未证明 noncanonical clean-core 的 primitive source constructor 准入，也未吸收未登记来源。 |
| clean-core构造器来源分类防火墙路由 | 新增/剩余压到actual noncanonical constructor公式 | 新增 `experiments/prime_matrix_clean_core_constructor_source_class_firewall_router.py` 与 `docs/monograph/prime-matrix-clean-core-constructor-source-class-firewall-router.md/json`。审查确认 `constructor_source_class_firewall_boundary_closed=true`、`source_class_partition_closed=true`、`unregistered_source_return_absorbed=true`、`actual_noncanonical_primitive_constructor_formula_proved=false`、`clean_core_primitive_source_constructor_admission_proved=false`、`external_spectral_atom_accepted=false`、`dstructure_rankin_independent_acceptance_completed=false`、`row_column_unconditional_closed=false`：primitive constructor 准入按来源类分裂，canonical constructor 只在 canonical-source 分支内闭合，generic WFD 不是 constructor，未登记或混合 formal unit 来源经 Multiplicity/Stitching 或 K7 formal-unit 失败回流，外部谱类仍是 `CDependentResidueWeightSpectralCancellationInput`。唯一完全自足源侧原子变为 `ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn`。最新条件输入基为 `(ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`；完全自足输入基为 `ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。当前材料尚未写出 actual noncanonical clean-core primitive constructor formula。 |
| clean-core外部引理参数匹配路由 | 新增/外部引理不能替代自足constructor公式 | 新增 `experiments/prime_matrix_clean_core_external_lemma_parameter_match_router.py` 与 `docs/monograph/prime-matrix-clean-core-external-lemma-parameter-match-router.md/json`。审查确认 `external_lemma_parameter_match_boundary_closed=true`、`external_lemmas_match_constructor_formula=false`、`external_lemmas_close_self_contained_remainder=false`、`external_spectral_atom_accepted=false`、`actual_noncanonical_primitive_constructor_formula_proved=false`、`row_column_unconditional_closed=false`：DI/BFI/Kuznetsov 外部引理处理 completion 后的 Kloosterman/AP/谱平均，要求系数或 residue 权重已经给定；当前完全自足原子要求在 Cauchy/dispersion 前写出 actual noncanonical `alpha/delta` 的 primitive constructor。因此外部引理不能生成 pre-Cauchy summand emitter，不能关闭自足剩余，只能作为 `CDependentResidueWeightSpectralCancellationInput` 外部谱分支的候选。最新条件输入基保持 `(ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`；完全自足输入基仍为 `ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。 |
| clean-core反向来源函子路由 | 新增/公式剩余改写为已登记纤维emitter | 新增 `experiments/prime_matrix_clean_core_reverse_provenance_functor_router.py` 与 `docs/monograph/prime-matrix-clean-core-reverse-provenance-functor-router.md/json`。审查确认 `reverse_provenance_functor_boundary_closed=true`、`payment_pushforward_functoriality_available=true`、`pushforward_reverse_uniqueness_rejected=true`、`finite_projection_recovers_gamma_not_source=true`、`constructor_formula_equivalent_to_registered_fiber_emitter=true`、`registered_primitive_prepushforward_fiber_emitter_proved=false`、`actual_noncanonical_primitive_constructor_formula_proved=false`、`row_column_unconditional_closed=false`：支付图、有限投影、弧限制和横向商只能正向保持来源兼容，不能从 `Gamma` 反推 pre-Cauchy primitive source；但在回流纪律已闭合后，当前公式剩余等价改写为 `RegisteredPrimitivePrePushforwardFiberEmitterAndReturn`。最新条件输入基为 `(RegisteredPrimitivePrePushforwardFiberEmitterAndReturn OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`；完全自足输入基为 `RegisteredPrimitivePrePushforwardFiberEmitterAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。当前材料仍未证明该 emitter，也未完成 DStructure/Rankin 独立验收。 |
| clean-core纤维emitter字段审计路由 | 新增/payment骨架闭合，alpha-delta提升开放 | 新增 `experiments/prime_matrix_clean_core_fiber_emitter_field_audit_router.py` 与 `docs/monograph/prime-matrix-clean-core-fiber-emitter-field-audit-router.md/json`。审查确认 `fiber_emitter_field_audit_boundary_closed=true`、`payment_fiber_skeleton_closed=true`、`first_cover_payment_map_closed=true`、`payment_count_identity_closed=true`、`alpha_delta_coefficient_lift_proved=false`、`polylog_branch_schema_proved=false`、`registered_primitive_prepushforward_fiber_emitter_proved=false`、`row_column_unconditional_closed=false`：`ActualPaymentSelection` 已给出 completion-hole 域、first-cover `pay(c,y)` 和 payment count identity，`ActualPaymentStitching` 已排除 payment 层第四出口；但这只是计数型 `Gamma` 骨架，不是 signed `alpha/delta` primitive source。最新自足输入压成 `ExactAlphaDeltaLiftForRegisteredPaymentFiberSkeletonAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`；条件输入基为 `(ExactAlphaDeltaLiftForRegisteredPaymentFiberSkeletonAndReturn OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。 |
| clean-core alpha-delta解积分字典路由 | 新增/alpha-delta提升压成signed解积分字典 | 新增 `experiments/prime_matrix_clean_core_alpha_delta_disintegration_router.py` 与 `docs/monograph/prime-matrix-clean-core-alpha-delta-disintegration-router.md/json`。审查确认 `alpha_delta_disintegration_boundary_closed=true`、`payment_base_map_closed=true`、`lift_equivalent_to_signed_disintegration_dictionary=true`、`canonical_decision_tree_template_scoped=true`、`generic_or_unregistered_dictionary_blocked=true`、`registered_alpha_delta_disintegration_dictionary_proved=false`、`exact_alpha_delta_lift_proved=false`、`row_column_unconditional_closed=false`：`ExactAlphaDeltaLiftForRegisteredPaymentFiberSkeletonAndReturn` 本质上等价于 signed `alpha/delta` primitive 源测度沿 first-cover payment map 的逐纤维解积分字典。payment skeleton、pre-Cauchy 字段纪律、路径预算用途和 canonical 模板都已可用，但 noncanonical clean-core 的 actual registered 字典尚未提交。最新自足输入基为 `RegisteredAlphaDeltaDisintegrationDictionaryAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`；条件输入基为 `(RegisteredAlphaDeltaDisintegrationDictionaryAndReturn OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。 |
| clean-core解积分自动性路由 | 新增/逐纤维分解形式闭合，源测度Phi预算开放 | 新增 `experiments/prime_matrix_clean_core_disintegration_automaticity_router.py` 与 `docs/monograph/prime-matrix-clean-core-disintegration-automaticity-router.md/json`。审查确认 `disintegration_automaticity_boundary_closed=true`、`discrete_payment_base_map_closed=true`、`signed_fiber_disintegration_formal=true`、`pushforward_identity_is_real_gate=true`、`actual_signed_source_measure_phi_compatibility_budget_proved=false`、`row_column_unconditional_closed=false`：在离散 first-cover payment map `Phi` 已闭合时，给定 actual signed 源测度 `nu` 后，逐纤维 signed disintegration 是形式恒等式；真正剩余是证明 `nu` 是同一 formal unit 内的 actual noncanonical `alpha/delta` 源测度，且 `Phi_*nu` 等于目标 payment-side 系数并满足总变差、绝对支撑和 branch key 预算。最新自足输入基为 `ActualSignedSourceMeasurePhiCompatibilityBudgetAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`；条件输入基为 `(ActualSignedSourceMeasurePhiCompatibilityBudgetAndReturn OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。 |
| clean-core几何Phi/预算桥路由 | 新增/几何基底闭合，signed源与预算分裂开放 | 新增 `experiments/prime_matrix_clean_core_geometric_phi_budget_bridge_router.py` 与 `docs/monograph/prime-matrix-clean-core-geometric-phi-budget-bridge-router.md/json`。审查确认 `geometric_phi_budget_bridge_boundary_closed=true`、`geometric_payment_base_available=true`、`geometry_defines_signed_source_measure=false`、`geometry_proves_phi_pushforward_identity=false`、`geometry_supplies_budget_return_shape=true`、`actual_signed_source_measure_phi_compatibility_budget_proved=false`、`row_column_unconditional_closed=false`：斜线覆盖、圆柱环绕、第P列锚、层叠轮筛和动态容量给出了统一 payment/Phi 几何基底、总变差/支撑/branch 预算候选形状及 `PDEC/SAE/ColumnCRT/CleanKLS` 命名回流场；但这些 unsigned 几何对象不生成 pre-Cauchy signed `alpha/delta` 源测度，也不自动证明 `Phi_*nu` 等于目标 payment-side 系数。因此最新自足输入基分裂为 `ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND GeometricVariationBranchBudgetCertificateOrNamedReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`；条件输入基为 `((ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND GeometricVariationBranchBudgetCertificateOrNamedReturn) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。 |
| clean-core几何变差/分支预算路由 | 新增/预算侧压成DPRC与signed提升两把锁 | 新增 `experiments/prime_matrix_clean_core_geometric_variation_branch_budget_router.py` 与 `docs/monograph/prime-matrix-clean-core-geometric-variation-branch-budget-router.md/json`。审查确认 `geometric_budget_attack_boundary_closed=true`、`geometry_ledger_alphabet_closed=true`、`dprc_analytic_capacity_bound_proved=false`、`signed_variation_branch_lift_proved=false`、`geometric_variation_branch_budget_certificate_proved=false`、`row_column_unconditional_closed=false`：CLB/PAW/DPRC/层叠轮/Atlas 已闭合 payment 支撑、容量、相位和命名回流字母表，但预算侧原子不能靠 unsigned 几何自动闭合。它被压成 `DPRCAlpha043CenteredDiscrepancyOrNamedLayerReturn` 与 `SignedGeometricLedgerVariationBranchLiftAndReturn` 两把锁：前者证明动态提升轮正偏差平方根界或层叠轮回流，后者证明 actual signed source 的总变差和 branch key 复杂度被几何账本支配且不能在 `Phi` 纤维内隐藏超预算质量。最新自足输入基为 `ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND DPRCAlpha043CenteredDiscrepancyOrNamedLayerReturn AND SignedGeometricLedgerVariationBranchLiftAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`；条件输入基为 `((ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND DPRCAlpha043CenteredDiscrepancyOrNamedLayerReturn AND SignedGeometricLedgerVariationBranchLiftAndReturn) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。 |
| clean-core DPRC中心化偏差路由 | 新增/DPRC解析锁压成ModelGap与BES-DLS | 新增 `experiments/prime_matrix_clean_core_dprc_centered_discrepancy_router.py` 与 `docs/monograph/prime-matrix-clean-core-dprc-centered-discrepancy-router.md/json`。审查确认 `dprc_centered_discrepancy_boundary_closed=true`、`rsm_identity_closed=true`、`bes_compression_closed=true`、`dprc_centered_discrepancy_input_proved=false`、`row_column_unconditional_closed=false`：DPRC 原始容量不等式已由 RSM 恒等式压成显式模型余量/有限账本与正偏差平方根界；正偏差界又由 BES 压成六个 beta 桶的高 `L1` 与高 `L2` 不能同步。若同步危险交集不能直接排斥，DLS 路线要求失败显化为 `PointLoad/ColumnCRT`、`ShortWindow/SAE` 或 `LowPhase/PDEC`。最新自足输入基为 `ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND BESDangerIntersectionExclusionOrDLSNamedReturn AND SignedGeometricLedgerVariationBranchLiftAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`；条件输入基为 `((ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND BESDangerIntersectionExclusionOrDLSNamedReturn AND SignedGeometricLedgerVariationBranchLiftAndReturn) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。 |
| clean-core BES-DLS命名回流路由 | 新增/BES-DLS压成三出口微输入 | 新增 `experiments/prime_matrix_clean_core_bes_dls_named_return_router.py` 与 `docs/monograph/prime-matrix-clean-core-bes-dls-named-return-router.md/json`。审查确认 `bes_dls_named_return_boundary_closed=true`、`dls_kernel_and_danger_algebra_closed=true`、`bes_dls_named_return_input_proved=false`、`row_column_unconditional_closed=false`：中心化核、危险交集、尖峰桶鸽巢和二次能量展开已形式化；若 BES 高 `L1`/高 `L2` 危险交集出现，不能作为无名同步失败保留，必须进入 `PointLoad`、`ShortWindow` 或 `LowPhase`。近危险摘要为 `max_point_load=4`、`max_short_window_positive=0.381667sqrt(S)`、`max_low_phase_positive=0.902430sqrt(S)` 且顶层 LowPhase 残基均为单位类。最新三微输入为 `DLSPointLoadColumnCRTBoundOrNamedReturn`、`DLSShortWindowSAEBoundOrNamedReturn`、`DLSLowPhasePDECNewLayerOrFlatDLSBound`；完全自足输入基相应更新为 `ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DLSPointLoadColumnCRTBoundOrNamedReturn AND DLSShortWindowSAEBoundOrNamedReturn AND DLSLowPhasePDECNewLayerOrFlatDLSBound AND SignedGeometricLedgerVariationBranchLiftAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。 |
| clean-core DLS LowPhase PDEC/flat DLS路由 | 新增/LowPhase压成固定轮、新增层、flat DLS三项 | 新增 `experiments/prime_matrix_clean_core_dls_lowphase_pdec_flat_router.py` 与 `docs/monograph/prime-matrix-clean-core-dls-lowphase-pdec-flat-router.md/json`。审查确认 `dls_lowphase_boundary_closed=true`、`lowphase_input_proved=false`、`row_column_unconditional_closed=false`：LowPhase 不能再作为单个固定模规律保留。固定轮单位类峰若持续同步，则必须给 `W-unit PDEC`；升层后若新增 Fourier 频率低维集中，则必须给 `new-layer PDEC`；若固定轮和新增层均被稀释，剩余只能是高模平坦分散能量，需由 `flat DLS/KLS` 大筛吸收。审计摘要：`W=30 max peak=1.076781`，`W=30 high-L1 max peak=0.902430`，层叠轮最大峰从 `30` 的 `1.076781` 降至 `210` 的 `0.617936`、`2310` 的 `0.293727`；Fourier 代表样本中 `W=2310` 强频率 `8/8` 为新增因子 `11` 层，但 centered peak 只有 `0.292146`。最新微输入为 `DLSFixedWheelUnitPeakDilutionOrPDECReturn`、`DLSNewLayerFourierConcentrationPDECReturn`、`DLSFlatHighModLargeSieveAbsorption`。 |
| LowMod PDEC容量失败定位路由 | 新增/抽象PDEC不等式失败材料化 | 新增 `experiments/prime_matrix_lowmod_pdec_capacity_failure_router.py` 与 `docs/monograph/prime-matrix-lowmod-pdec-capacity-failure-router.md/json`。审查确认 `lowmod_same_set_capacity_protocol_closed=true`、`lowmod_capacity_multiplier_discipline_closed=true`、`lowmod_pdec_inequality_closed=false`、`row_column_unconditional_closed=false`：`PersistentLowModPDECInequality_UCRT_LT_LPDEC` 若失败，必须在同一 LowMod formal unit `G_B=Z/Q_BZ` 上输出有限循环弧 `LowModDualCap(B,h,zeta,alpha)`，随后回流 `SAE/ColumnCRT/refined PDEC/new-layer PDEC/CleanKLS`。新的最窄原子输入为 `FiniteCyclicArcCapMassBoundsForFutureLowModPrimitiveSchemas`；本项闭合无名容量失败出口，不闭合完整行/列命题。 |
| LowMod有限弧cap归约路由 | 新增/独立LowMod弧输入并入LowPhase | 新增 `experiments/prime_matrix_lowmod_finite_arc_cap_reduction_router.py` 与 `docs/monograph/prime-matrix-lowmod-finite-arc-cap-reduction-router.md/json`。审查确认 `lowmod_finite_arc_independent_input_removed=true`、`lowmod_finite_arc_cap_mass_bounds_closed=false`、`lowphase_three_micro_inputs_proved=false`、`row_column_unconditional_closed=false`：未来 LowMod primitive schema 的有限循环弧 cap 不是第四终端，固定轮弧、新增层弧和高模平坦弧分别归入 `DLSFixedWheelUnitPeakDilutionOrPDECReturn`、`DLSNewLayerFourierConcentrationPDECReturn`、`DLSFlatHighModLargeSieveAbsorption`；稀疏或列位移弧帽回流 `SAE/ColumnCRT-as-PDEC`。真正剩余是 LowPhase 三微输入或具体 `LowModDualCap` 回流证书。 |
| LowMod-new-layer桥接路由 | 新增/新增层子口替换为schema+flat准入 | 新增 `experiments/prime_matrix_lowmod_newlayer_bridge_router.py` 与 `docs/monograph/prime-matrix-lowmod-newlayer-bridge-router.md/json`。审查确认 `lowmod_newlayer_bridge_closed=true`、`newlayer_schema_proved=false`、`newlayer_flat_admission_proved=false`、`row_column_unconditional_closed=false`：`DLSNewLayerFourierConcentrationPDECReturn` 已接入既有 new-layer 投影切片链，替换为 `RegisteredNewLayerPDECFormalUnitAndCapStableSchema AND NewLayerNoConcentrationImpliesFlatAdmission`。强新增层 Fourier 集中必须登记为同 formal unit 的 PDEC cap；无可登记低维集中时，剩余对象必须满足 flat-DLS/KLS 准入。下一步最窄优先目标为 `RegisteredNewLayerPDECFormalUnitAndCapStableSchema`。 |
| new-layer PDEC schema准入路由 | 新增/schema准入闭合预算账本开放 | 新增 `experiments/prime_matrix_newlayer_pdec_schema_admission_router.py` 与 `docs/monograph/prime-matrix-newlayer-pdec-schema-admission-router.md/json`。审查确认 `newlayer_schema_admission_closed=true`、`registered_same_formal_unit_omega_tau_weight=true`、`lowrank_column_sparse_return_closed=true`、`cap_unstable_return_closed=true`、`newlayer_ranktwo_budget_ledger_closed=false`、`row_column_unconditional_closed=false`：new-layer cap 的 formal unit 可登记为 `Omega'_A=A x F_r`、相位 `(old phase,b mod r)`、权重 `delta_A(b)`；跨层/重复/口径错配、低秩、二点、列位移、稀疏孤窗和 cap 不稳定全部回流命名出口。最新最窄目标为 `NewLayerRankTwoCapStablePDECBudgetLedger`。 |
| new-layer二秩预算账本路由 | 新增/预算账本独立输入移除 | 新增 `experiments/prime_matrix_newlayer_ranktwo_budget_ledger_router.py` 与 `docs/monograph/prime-matrix-newlayer-ranktwo-budget-ledger-router.md/json`。审查确认 `newlayer_ranktwo_budget_ledger_reduced=true`、`newlayer_ranktwo_budget_independent_input_removed=true`、`newlayer_pdec_budget_inequality_unconditionally_proved=false`、`newlayer_no_concentration_flat_admission_proved=false`、`row_column_unconditional_closed=false`：若 new-layer 二秩 cap-stable 预算失败，则同一 `Omega'_A=A x F_r` formal unit 内必产生有限字符弧 cap；旧轴回旧层 `PDEC/ColumnCRT/SAE`，新 fiber 与混合轴经有限弧横向分裂回流命名出口或进入 flat residual。因此 `NewLayerRankTwoCapStablePDECBudgetLedger` 不再作为独立最终输入，最新最窄目标更新为 `NewLayerNoConcentrationImpliesFlatAdmission`。 |
| new-layer无集中flat准入路由 | 新增/准入边界闭合转交flat DLS | 新增 `experiments/prime_matrix_newlayer_no_concentration_flat_admission_router.py` 与 `docs/monograph/prime-matrix-newlayer-no-concentration-flat-admission-router.md/json`。审查确认 `newlayer_no_concentration_flat_admission_boundary_closed=true`、`newlayer_no_concentration_independent_input_removed=true`、`dls_flat_highmod_large_sieve_absorption_proved=false`、`row_column_unconditional_closed=false`：无集中 residual 的含义被固定为所有低模、有限弧、互信息、短窗、列位移和晋升素数缺陷都已删除或命名回流；在既有 K1--K9 clean admission 合同下，它准入同一个 `DLSFlatHighModLargeSieveAbsorption` 证书口。最新最窄目标更新为 `DLSFlatHighModLargeSieveAbsorption`，仍未证明 flat high-mod 大筛吸收。 |
| 早期零行反例 flat-DLS 路由 | 新增/反例分支最后逃逸压窄 | 新增 `experiments/prime_matrix_early_zero_flatdls_counterexample_router.py` 与 `docs/monograph/prime-matrix-early-zero-flatdls-counterexample-router.md/json`。审查确认 `counterexample_assumption_only=true`、`empirical_absence_not_used=true`、`early_zero_flatdls_last_escape_boundary_closed=true`、`dls_flat_highmod_large_sieve_absorption_proved=false`、`direct_unconditional_contradiction_found=false`、`row_column_unconditional_closed=false`：本项只在“假设 P 行以内早期零行存在”的反例分支中工作，把 flat-DLS 高模残余解释为反例支付压力；任何短窗、低模、列频率或 Bohr-cap 集中都回流 `SAE/PDEC/ColumnCRT` 或外部谱输入，唯一自足剩余压成 `EarlyZeroL2FlatKLSCounterexampleSpectralExclusion`。 |
| 早期零行 L2-flat KLS 逃逸排除路由 | 新增/无名flat逃逸关闭到终端包 | 新增 `experiments/prime_matrix_early_zero_l2flat_kls_exclusion_router.py` 与 `docs/monograph/prime-matrix-early-zero-l2flat-kls-exclusion-router.md/json`。审查确认 `early_zero_l2flat_kls_counterexample_spectral_exclusion_closed=true`、`pure_l2flat_escape_as_unnamed_branch_removed=true`、`general_dls_flat_highmod_large_sieve_absorption_proved=false`、`direct_unconditional_contradiction_found=false`、`row_column_unconditional_closed=false`：在反例分支内，早期零行强制同 formal unit 的稳定复现或边界相位缺陷；flat/KLS 准入要求 registered 低维缺陷已经命名回流。因此 `EarlyZeroL2FlatKLSCounterexampleSpectralExclusion` 不再是无名最后逃逸，替换为 `EarlyZeroTerminalExclusionPackage`，但终端家族本身仍未排斥。 |
| 早期零行终端排斥包压缩路由 | 新增/抽象终端包压成三项几何硬核 | 新增 `experiments/prime_matrix_early_zero_terminal_package_reduction_router.py` 与 `docs/monograph/prime-matrix-early-zero-terminal-package-reduction-router.md/json`。审查确认 `early_zero_terminal_package_reduced=true`、`early_zero_terminal_package_fully_proved=false`、`direct_unconditional_contradiction_found=false`、`row_column_unconditional_closed=false`：抽象 `EarlyZeroTerminalExclusionPackage` 已被拆成 `AnchorCollarPrimeFiberCapacityBoundOrPDECReturn AND CompositeCofactorDepthDescentOrNamedReturn AND EarlyBandLocalSurvivorOrSAEExclusion`。大行段是真双素 canonical anchor-collar 短纤维容量，早期段是复合 cofactor 递归下降或 LocalSurvivor/SAE 排斥；下一步最窄目标为 `AnchorCollarPrimeFiberCapacityBoundOrPDECReturn`。 |
| anchor-collar容量端点缺陷桥路由 | 新增/容量硬点转为端点PDEC或纤维饱和 | 新增 `experiments/prime_matrix_anchor_collar_endpoint_bridge_router.py` 与 `docs/monograph/prime-matrix-anchor-collar-endpoint-bridge-router.md/json`。审查确认 `anchor_collar_endpoint_bridge_closed=true`、`anchor_collar_prime_fiber_capacity_fully_proved=false`、`direct_unconditional_contradiction_found=false`、`row_column_unconditional_closed=false`：对 `x>=sqrt(P)` 有精确恒等式 `H_x=Prime_x+A_x`；早期零行反例强制 `Prime_x=0`，故 `H_x=A_x`。再由包含排除 `H_x=(P-1)V_x+E_x`，若低骨架主项超过 anchor 容量，则反例推出强负端点 PDEC；若无主项间隙，则短纤维必须近饱和并回流 PDEC/SAE。最新最窄目标为 `AnchorCollarEndpointDefectPDECExclusion`。 |
| anchor端点PDEC低模/尾项二分路由 | 新增/端点缺陷黑箱拆分 | 新增 `experiments/prime_matrix_anchor_endpoint_lowmod_tail_router.py` 与 `docs/monograph/prime-matrix-anchor-endpoint-lowmod-tail-router.md/json`。审查确认 `anchor_endpoint_pdec_dichotomy_closed=true`、`anchor_endpoint_pdec_exclusion_fully_proved=false`、`direct_unconditional_contradiction_found=false`、`row_column_unconditional_closed=false`：若早期零行强制 `E_x<=-G_x`，则任意 `D,theta` 下必有低模有限 CRT 相位项 `E_{x,<=D}<=-theta G_x`，或高模尾项 `E_{x,>D}<=-(1-theta)G_x`。因此 `AnchorCollarEndpointDefectPDECExclusion` 被压成 `AnchorEndpointLowModPDECFinitePhaseExclusion AND AnchorEndpointTailCorePDECOrFiberSaturation`；下一步最窄目标为低模有限相位坏集排斥。 |
| anchor低模端点相位fixed-wheel准入路由 | 新增/anchor低模独立输入移除 | 新增 `experiments/prime_matrix_anchor_lowmod_fixedwheel_admission_router.py` 与 `docs/monograph/prime-matrix-anchor-lowmod-fixedwheel-admission-router.md/json`。审查确认 `anchor_lowmod_independent_input_removed=true`、`dls_fixedwheel_input_proved=false`、`direct_unconditional_contradiction_found=false`、`row_column_unconditional_closed=false`：固定 `D` 后 anchor 低模端点坏相位是有限 CRT 相位函数，按同 formal unit 准入既有 `DLSFixedWheelUnitPeakDilutionOrPDECReturn`，不再作为独立新剩余。anchor 专属下一步最窄目标更新为 `AnchorEndpointTailCorePDECOrFiberSaturation`，全局层面仍需证明 fixed-wheel 微输入。 |
| anchor tail-core到纤维饱和路由 | 新增/anchor tail-core独立输入移除 | 新增 `experiments/prime_matrix_anchor_tailcore_fiber_saturation_router.py` 与 `docs/monograph/prime-matrix-anchor-tailcore-fiber-saturation-router.md/json`。审查确认 `anchor_tailcore_independent_input_removed=true`、`anchor_fiber_saturation_proved=false`、`direct_unconditional_contradiction_found=false`、`row_column_unconditional_closed=false`：高模 tail 若非 fiber saturation，则已落入全局 DLS `PointLoad/ShortWindow/LowPhase` 或 Bohr-cap 命名出口；这些输入已在全局输入基中保留。因此 anchor 专属剩余只剩 `AnchorFiberSaturationPDECOrSAEReturn`。 |
| anchor fiber饱和命名回流schema路由 | 新增/anchor专属fiber gap删除 | 新增 `experiments/prime_matrix_anchor_fiber_saturation_return_schema_router.py` 与 `docs/monograph/prime-matrix-anchor-fiber-saturation-return-schema-router.md/json`。审查确认 `anchor_fiber_saturation_return_schema_closed=true`、`anchor_specific_fiber_gap_removed=true`、`pdec_or_sae_terminal_exclusion_proved=false`、`direct_unconditional_contradiction_found=false`、`row_column_unconditional_closed=false`：固定 `q` 的短素数窗口是有限 formal unit；持久近饱和必须提交 primitive PDEC schema，孤立近饱和必须提交 LocalSurvivor/SAE packet。因此 anchor 专属 fiber gap 已删除，但 PDEC/SAE 终端排斥仍未证明；下一步最窄目标回到 `CompositeCofactorDepthDescentOrNamedReturn`。 |
| 复合cofactor下降命名回流schema路由 | 新增/复合cofactor专属gap删除 | 新增 `experiments/prime_matrix_composite_cofactor_descent_schema_router.py` 与 `docs/monograph/prime-matrix-composite-cofactor-descent-schema-router.md/json`。审查确认 `composite_cofactor_descent_schema_closed=true`、`composite_cofactor_specific_gap_removed=true`、`pdec_or_sae_terminal_exclusion_proved=false`、`direct_unconditional_contradiction_found=false`、`row_column_unconditional_closed=false`：复合 cofactor 满足 `m<P` 且 x-rough 深度有限，递归不能无穷循环；持久复合签名必须进 PDEC，孤立复合签名必须进 SAE/LocalSurvivor。因此复合 cofactor 专属 gap 已删除，最新最窄目标回到 `EarlyBandLocalSurvivorOrSAEExclusion`。 |
| early-band LocalSurvivor/SAE命名回流schema路由 | 新增/early-band专属gap删除 | 新增 `experiments/prime_matrix_early_band_local_survivor_return_schema_router.py` 与 `docs/monograph/prime-matrix-early-band-local-survivor-return-schema-router.md/json`。审查确认 `early_band_local_survivor_return_schema_closed=true`、`early_band_specific_gap_removed=true`、`pdec_or_sae_terminal_exclusion_proved=false`、`dls_shortwindow_global_input_proved=false`、`row_column_unconditional_closed=false`：在早期零行反例分支中，孤立 early-band 窗口必须物化为有限 LocalSurvivor/SAE packet，持久同签名必须进入 PDEC，层级逃逸必须进入 CleanKLS/DLS。因此 early-band 专属无名出口已删除；全局最窄目标转到 `DLSShortWindowSAEBoundOrNamedReturn`。 |
| DLS short-window SAE命名回流schema路由 | 新增/short-window专属gap删除 | 新增 `experiments/prime_matrix_dls_shortwindow_sae_return_schema_router.py` 与 `docs/monograph/prime-matrix-dls-shortwindow-sae-return-schema-router.md/json`。审查确认 `dls_shortwindow_return_schema_closed=true`、`dls_shortwindow_specific_gap_removed=true`、`dls_shortwindow_numeric_bound_proved=false`、`pdec_or_sae_terminal_exclusion_proved=false`、`row_column_unconditional_closed=false`：固定短窗是有限局部覆盖对象；孤立时必须提交 LocalSurvivor/SAE packet，持久时必须提交 PDEC schema，层级逃逸时必须进入 CleanKLS/DLS 或下降回流。因此 short-window 专属无名出口已删除；最新最窄目标转到 `DLSPointLoadColumnCRTBoundOrNamedReturn`，`DLSFixedWheelUnitPeakDilutionOrPDECReturn` 仍开放。 |
| DLS point-load/ColumnCRT命名回流schema路由 | 新增/point-load专属gap删除 | 新增 `experiments/prime_matrix_dls_pointload_columncrt_return_schema_router.py` 与 `docs/monograph/prime-matrix-dls-pointload-columncrt-return-schema-router.md/json`。审查确认 `dls_pointload_return_schema_closed=true`、`dls_pointload_specific_gap_removed=true`、`columncrt_independent_terminal_removed=true`、`pdec_columncrt_sae_terminal_exclusion_proved=false`、`row_column_unconditional_closed=false`：单点高负载若平衡则不能支付缺陷预算；若持久则给出有限列位移或尾锚签名并进入 PDEC/ColumnCRT；若孤立则进入 SAE/LocalSurvivor packet。因此 point-load 专属无名出口已删除；最新最窄目标转到 `DLSFixedWheelUnitPeakDilutionOrPDECReturn`。 |
| DLS fixed-wheel单位峰命名回流schema路由 | 新增/fixed-wheel专属gap删除 | 新增 `experiments/prime_matrix_dls_fixedwheel_pdec_return_schema_router.py` 与 `docs/monograph/prime-matrix-dls-fixedwheel-pdec-return-schema-router.md/json`。审查确认 `dls_fixedwheel_return_schema_closed=true`、`dls_fixedwheel_specific_gap_removed=true`、`fixedwheel_numeric_dilution_proved=false`、`wunit_pdec_terminal_exclusion_proved=false`、`row_column_unconditional_closed=false`：固定轮峰若持久，必须登记为 W-unit PDEC；若升层后继续集中，进入 new-layer PDEC/flat admission；若固定轮和新增层缺陷都被剥离，则 flat/L2-flat 逃逸已在早期零行反例分支回到终端包。因此 fixed-wheel 专属无名出口已删除；最新最窄目标转到 `SignedGeometricLedgerVariationBranchLiftAndReturn`。 |
| signed几何变差锁兼容预算合并路由 | 新增/独立signed变差原子合并 | 新增 `experiments/prime_matrix_signed_geometric_variation_compatibility_merger.py` 与 `docs/monograph/prime-matrix-signed-geometric-variation-compatibility-merger.md/json`。审查确认 `signed_variation_independent_atom_removed=true`、`actual_signed_source_phi_compatibility_budget_proved=false`、`actual_noncanonical_constructor_formula_proved=false`、`row_column_unconditional_closed=false`：`SignedGeometricLedgerVariationBranchLiftAndReturn` 不是独立原子，而是 actual signed source、Phi 推前恒等式、总变差/支撑预算和 branch key 预算同一个兼容包的字段。因此 source identity 与 signed variation 合并为 `ActualSignedSourceMeasurePhiCompatibilityBudgetAndReturn`；最新最窄目标为提交该兼容预算或命名回流。 |
