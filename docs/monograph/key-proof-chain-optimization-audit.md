# 关键证明链条优化审查

## 0. 审查目的

本文档只做一件事：把合著稿中仍在主线上的关键逻辑链条压缩为可审稿对象，并明确每一条链的闭合等级、剩余输入和优化优先级。

状态标签如下：

- `Proved-in-text`：正文已有逐步证明；
- `Reduction-closed`：已严格归约到更小接口；
- `External-theorem closed`：引用明确外部深定理后闭合；
- `Referee-block`：已有证明框架，但仍需逐行审稿核查；
- `Not claimed`：不能作为无条件结论使用。

## 1. 方阵行列链条

当前最清晰的审稿链条应写为：

```text
PM-1 Matrix model
=> PM-2 CRT nonzero skeleton
=> PM-3 large-factor non-reuse
=> PM-4 diagonal/slope locks
=> PM-5 tail anchors
=> PM-6 A/B structured reduction
=> PM-7 Structured-EHPD exclusion
=> PM-8 row/column closure
```

### 1.1 已稳定部分

- `PM-1` 到 `PM-4` 是结构性定义、CRT 骨架和局部刚性，适合作为正文基础引理。
- 大因子不可复用、相邻互质、45 度锁、`P±1` 斜线锁定及其广义版本 `P±t` 应统一归入“局部刚性层”，避免在主线中反复新增命名。
- 新增的广义斜率锁只闭合小素因子层：`q|k` 且 `q|P±t` 时非绕回算术段全由 `q` 标记；圆柱绕回螺旋持续延续，但实际整数值带有绕回次数余项，故应按绕回相位块计算锁定覆盖。

### 1.2 仍需保守标注部分

- `PM-5` Tail anchors 与 `PM-7` Structured-EHPD 是方阵链条的审稿核心。
- 在它们完全逐行核查前，`PM-8` 只能标注为 `Reduction package` 或 `Conditional on PM-5/PM-7`。
- 方阵行列结论可以辅助二点筛中的 `BMD-Zero`，但不能替代 `BMD-Char` 的有符号谱分布估计。

### 1.3 优化重点

最优整理不是增加新的局部刚性名称，而是把所有局部刚性统一服务于 `Structured-EHPD`：

```text
local rigidity ledger + capacity ledger + no-reuse ledger
=> Structured-EHPD impossible
```

这会把方阵部分的审稿焦点压缩到一个最终接口。

新增的粗数补洞接口可写为：

```text
generalized slope locks remove q<=Y
=> rough band G_Y remains
=> large-prime incidence B_Y(G_Y) must be < |G_Y|
```

其模型常数为 `log(1/alpha)`，其中 `Y=P^alpha`。这给出更简单的目标不等式，但证明该不等式仍需要短窗口粗数分布和大因子命中上界，不能由斜率锁本身推出。

### 1.3A BPN-BK 最终证书层

新增 `docs/monograph/prime-matrix-bpn-final-exit-acceptance-contract.md` 与
`docs/monograph/prime-matrix-bpn-final-residual-hard-attack.md` 后，边界相位非覆盖主链
应按最终证书层书写：

```text
BPN-BK reductions
=> PDEC-Cert
   or SAE-Cert
   or formal Rankin certificates。
```

优化重点不再是新增等价分支，而是提交三类证书：

- `PDEC-Cert`：证明同一坏窗集合的非零 Fourier 上界 `U_CRT<L_PDEC`；
- `SAE-Cert`：对孤立坏窗给出 survivor/lift/higher-defect；
- `Rankin certificates`：全部颜色类通过预算，或失败者转入 low-mod core CRTDefect。

该层当前是 `Reduction-closed`，不是 `Proved-in-text`。在证书全集通过前，方阵行命题仍不能升级为无条件终局定理。

新增 `docs/monograph/prime-matrix-bpn-pdec-dual-certificate-framework.md` 后，`PDEC-Cert`
进一步拆成两类可验收对象：

```text
PDEC-Explicit-Cert:
  直接给出坏窗相位计数向量并核验 max |g_hat(h)|<L_PDEC；

PDEC-Dual-Cert:
  把镜像、列均衡、尾锚不可复用、核心重叠回流写成线性约束，
  再用对偶主控证书统一证明 U_CRT<L_PDEC。
```

脚本 `experiments/prime_matrix_bpn_pdec_certificate_audit.py` 已覆盖显式证书审计。无限族闭合仍需
对偶证书或解析主控；这是当前最窄硬点。

新增 `docs/monograph/prime-matrix-bpn-pdec-constraint-ledger.md` 与
`experiments/prime_matrix_bpn_pdec_dual_certificate_audit.py` 后，对偶证书层进一步机器化：

```text
结构约束原子 -> A,b,E,e；
对偶权重 -> lambda,mu；
逐相位主控 -> c_{h,zeta}(t)<=A^T lambda+E^T mu；
总界 -> U_dual=lambda*b+mu*e<L_PDEC。
```

当前真正剩余不是证书格式，而是证明这些 `A,b,E,e` 的每一行确实来自边界零行刚性，
并覆盖所有非零频率与连续方向。

新增 `experiments/prime_matrix_bpn_pdec_real_constraint_rows.py` 与报告
`docs/monograph/prime-matrix-bpn-pdec-real-constraint-rows.md` 后，第一批真实系数行已填入。
默认 `P=23,Q=210` 完整 CRT 枚举给出：

```text
zero rows = 3456；
nonzero phase caps = 44/210；
max phase cap = 324；
low-hole >=5 bucket bound = 0。
```

这把下一步攻坚压成一个具体符号化目标：证明“低骨架剩余洞数过高”时尾锚/核心补洞容量
不足，形成 `low-hole bucket` 上界定理。

新增 `docs/monograph/prime-matrix-bpn-low-hole-bucket-capacity-theorem.md` 与
`experiments/prime_matrix_bpn_low_hole_bucket_capacity.py` 后，`low-hole bucket` 已不再依赖
整周期枚举，而是精确改写为高层 CRT 补洞容量。低范围 `P=13,17,19,23,Q=210` 的读数显示：

```text
max holes with completion = number of high primes；
max single-prime cover on completion = 1。
```

但 `P>=29` 时单洞匹配会失效。正确的下一步最窄硬点是 Hall 型 set-cover 亏损：

```text
存在 W subset H_Q(t):
|W| > sum_ell max_a |W cap B_{ell,a}(t)|
=> completion_count(t)=0。
```

最新 `Q=2310` 扫描中，`P=13..47` 的全部 zero phases 均已由 Hall 亏损证书覆盖。
进一步按最小删洞数 `d=|H_Q(t)|-|W|` 统计，证书实际只有两类：
`P<=37` 全部为整洞集见证，`P=43,47` 只需整洞集或一洞删除。
先前的二洞删除是最大亏损搜索的见证选择假象，不是结构例外。因此下一步不应再搜索任意
`W⊆H_Q(t)`，而应严攻两类显式不等式：

```text
Delta(H_Q(t))>0；
若 Delta(H_Q(t))=0，则存在桥洞 c0 使 Delta(H_Q(t)\{c0})>0。
```

新增 `prime-matrix-bpn-lhb-bridge-deletion-audit.md` 显示全部一洞删除相位满足桥洞机制：
被删洞同时支撑两个高素数最大残基块，删去它使总容量下降 `2`、洞数只下降 `1`。
这把 `low-hole bucket` 的当前最窄硬点压成“整洞集亏损或桥洞删一亏损”定理。

新增 `prime-matrix-bpn-lhb-column-residue-rigidity-audit.md` 后，这个硬点又被代数化：
由

```text
a_{ell,c,t}=a_{ell,c',t} <=> c=c' mod ell
```

可知高层覆盖容量只取决于低洞集 `H_Q(t)` 的列残基分布。`Q=2310,P<=47`
的全部 zero bucket 均满足：

```text
Delta(H_Q(t))>0；
或 Delta(H_Q(t))=0 且存在两个高素数最大列残基块的公共桥洞 c_*。
```

临界态只出现在 `P=43,47`，桥洞支撑素数均为 `(13,19)`。下一步最窄硬点因此是：
证明实际 PDEC 低骨架中，整洞集若不亏损，则小高素数最大块必发生桥洞交叉。
扩展审计 `P=53,59,61` 显示，桥洞临界带之后 zero bucket 基本消失；唯一例外
`P=59` 的 8 个相位已经由 `Delta(H)>0` 直接覆盖。因此更准确的下一步二分是：

```text
低范围临界带：整洞集亏损、桥洞临界或精确 DP 临界；
转折后范围：zero bucket 消失，或仅剩整洞集直接亏损。
```

新增 `prime-matrix-bpn-lhb-greedy-cover-transition-audit.md` 后，转折后范围进一步有构造性证书：

```text
Q=2310:
P=53 greedy fail = 26；
P=59 greedy fail = 22；
P>=61, P<=109 greedy fail = 0。
```

因此下一步真正最窄硬点变为证明 `P>=61` 的贪心补洞定理：低洞集在高素数列残基块中
总能被逐步覆盖。后续低范围最终证书已把 `P<61` 的有限临界带闭合为三类证书：
整洞集亏损、桥洞临界和 `P=41` 的精确 DP 临界。
增益账本进一步显示，该贪心定理可压成一个显式不等式。若 `s(t)` 是构造覆盖所需块数，
`D(t)=|H_Q(t)|-s(t)` 是重复增益，则只需证明

```text
D(t) >= |H_Q(t)|-|R|。
```

样本中重复增益主要由 `13,17,19,23` 的列残基碰撞提供；`P` 增大后，`29,31,37`
继续补强。所以下一层最窄硬点是“小高素数碰撞梯重复增益下界”。

最新固定升序碰撞梯审计把该硬点再压窄一层：不需要动态选择高素数顺序。固定按
`13,17,19,23,...` 使用高素数，每步只取当前未覆盖洞中的最大列残基块，得到：

```text
Q=2310:
P=53 fixed-ladder fail = 44；
P=59 fixed-ladder fail = 36；
P>=61, P<=149 fixed-ladder fail = 0。
```

因此转折后最小符号目标应写成 `LHB-7`：证明 `P>=61` 时固定升序碰撞梯的累计重复增益
满足 `sum_j(|H_{j-1}∩(b_j mod ell_j)|-1) >= |H_Q(t)|-|R|`。该形式只涉及
固定低洞集的列残基块计数，比“存在某个贪心路径”更适合进入顶刊审稿。

主定理稿已补入碰撞能量分解：令
`E_ell(S)=sum_a binom(|S∩(a mod ell)|,2)`，则固定梯单步增益满足
`g_j-1 >= 2E_ell_j(H_{j-1})/|H_{j-1}|`。所以 `LHB-7` 可进一步由
固定残集上的能量和不等式推出。当前最小硬点不是搜索证书，而是证明
`13,17,19,23,...` 在低洞残集上的累计碰撞能量下界。

新增 `prime-matrix-bpn-lhb-pigeonhole-tail-audit.md` 后，尾段又出现一个更强的纯鸽巢出口。
令 `Hmax(P)` 为 `Q=2310` 周期中长度 `P-1` 的最大互素残基数，并递推
`U_j=U_{j-1}-ceil(U_{j-1}/ell_j)`。若 `U_j` 归零，则任意洞集都被固定升序梯覆盖。
扫描到 `P<=100000` 显示鸽巢递推只在
`61,67,71,73,79,83,89,97,101,103` 失败，`P=107` 起全部闭合。
进一步的 `P/5` 分割判据更适合解析证明：先用 `ell<=P/5` 做鸽巢递推，若剩余洞数
不超过 `(P/5,P)` 中的高素数个数，则后半段逐个删洞闭合。扫描中该判据在
`P>=107` 无失败。若再用连续乘积上界替代精确取整递推，则最后失败为 `P=229`，
从 `P=233` 起扫描无失败。
因此下一步最优严攻被拆成两个更小任务：

```text
Tail-A: 对 107<=P<=229 做精确 P/5 分割递推有限证书；
Tail-B: 用显式 prime-count/Mertens 界证明连续乘积不等式对所有 P>=233 闭合；
Band: 对 61<=P<=103 的十个素数，用真实碰撞能量补足鸽巢残量 1 或 2。
```

新增 `prime-matrix-bpn-lhb-explicit-tail-constant-audit.md` 后，`Tail-B` 被进一步拆成
有限乘积证书与解析常数包：`Hmax(P)<=16(P-1)/77+5`，再用候选标准输入
`prod_{p<=x}(1-1/p)<=e^{-gamma}(1.03)/log x`、`pi(x)>=x/log x`、
`pi(x)<=1.25506x/log x`，得到解析余量从 `P>=13208` 起为正。因此尾段当前最窄
工程义务是：

```text
107<=P<=229：精确分割递推表；
233<=P<=13207：精确连续乘积有限表；
P>=13208：显式 Mertens/prime-count 引用核验。
```

新增 `prime-matrix-bpn-lhb-tail-finite-certificate.md` 后，两段有限尾段证书已经生成：
`107<=P<=229` 共 `23` 行精确分割递推无失败，最小余量 `0`；`233<=P<=13207`
共 `1520` 行连续乘积证书无失败，使用整数交叉乘法
`R(P)B_y-Hmax(P)A_y>0` 验收，最小浮点余量约 `0.5347204`。因此尾段有限义务
已从“待生成”变为“证书可复核”，无限尾段只剩显式常数引用核验。

新增 `prime-matrix-bpn-lhb-narrow-band-collision-certificate.md` 后，`61<=P<=103`
的十个窄带素数也已闭合为有限碰撞能量证书。全 `23100` 个低相位固定升序梯均通过，
最小碰撞余量分别为 `0,0,0,1,1,2,2,2,2,3`。因此 `LHB-7` 剩余不再包含窄带；
新增 `prime-matrix-bpn-lhb-low-range-final-certificate.md` 后，`P<61` 也不再是剩余缺口：
`15414` 个 zero bucket 全部通过，分解为 `15282` 个整洞集亏损、`108` 个桥洞临界和
`24` 个 `P=41` 精确 DP 临界。当前 `LHB` 主线只剩 `P>=13208` 的显式常数引用核验。

### 1.4 尾段接口的最新压缩

新增 `docs/monograph/pta-gsl-hard-attack.md` 与 `docs/monograph/rse-reciprocal-sum-scan.md` 后，方阵尾段链条应改写为：

```text
GSL
=> Selberg upper sieve
=> BSI
=> RSE-OSC + RSE-AMP + RSE-CRIT
=> PTA-GSL
=> PM-R2B
```

其中：

- `RSE-OSC`：`hP_m/ell` 足够大，目标是粗数倒数相位抵消；
- `RSE-AMP`：`hP_m/ell` 足够小，目标是振幅因子账本吸收；
- `RSE-CRIT`：`ell≈hP_m` 的临界带，是当前唯一实质新硬点。

压力测试只能作为证据等级，但它明确排除了“继续泛化斜率锁即可闭合尾段”的路线。斜率锁负责删除小素合数层；剩余需要解析型短区间双线性分布或等价的临界带 CRTDefect 排斥。

`docs/monograph/rse-critical-band-hard-attack.md` 进一步把 `RSE-CRIT` 改写为 `CWM/CRD` 二分。随后 `docs/monograph/cwm-selberg-critical-mass-scan.md` 显示绝对 `CWM` 在尾部 dyadic 桶并不稳；`docs/monograph/scwm-crd-profile-scan.md` 显示必须保留真实 RSE 核；`docs/monograph/kscwm-crd-dual-obstruction-scan.md` 又修正了一个关键点：普通小素支撑集中 `SPC` 不足以推出 CRTDefect。`docs/monograph/skt-smooth-transform-scan.md` 把 `SKT` 拆成 `SKT-LIN` 与 `SKT-TRANS/SQF`；`docs/monograph/sqf-quadratic-form-scan.md` 显示 SQF 主瓶颈在低频 `Q(it)`；`docs/monograph/sqf-qlow-optimal-weight-scan.md` 显示精确最优 Selberg 权能降低零频和预算；`docs/monograph/sqf-qlow-fixed-low-stability-scan.md` 修正为 `QLOW-MID` 带权吸收；`docs/monograph/sqf-qlow-mid-weighted-absorption-scan.md` 将其进一步压缩为固定紧区间 `QLOW-MID-COMP` 加平滑尾部；`docs/monograph/qlow-mid-comp-grid-certificate.md` 则给出 `2<u<=12` 的导数余量网格证书，当前读数 `certified≈0.21--0.23<0.35`。因此最终窄接口应写为 `QLOW-MID-COMP(intervalized) + RRD + OSPC`。

## 2. 二点筛链条

当前二点筛主线应写为：

```text
TP-1 two-point rough pair
=> TP-2 TLI
=> TP-3 BST
=> TP-4 BST-2
=> TP-5 BMD
=> TP-6 WBE2
=> TP-7 BE2-3
=> TP-8 BE2-3K
=> TP-9 KLS-window
```

外部定理版闭合链为：

```text
DI + BFI
=> KLS-window
=> BE2-3K
=> BE2-3
=> WBE2
=> BMD
=> BST-2
=> BST
=> TLI
```

### 2.1 已完成的关键压缩

- `BMD` 已不是模糊猜想，而是受限二素数卷积 `a_n=#\{p m=n\}` 在固定类 `2 mod d` 上的加权 AP 分布。
- `BMD` 不需要完整 `max_a BV-E2`，只需要 well-factorable 权重下的 `WBE2`。
- `BE2-3` 的普通大筛路线已被排除，真正硬核是 Kloosterman 平均。
- `BE2-3K` 已进一步压缩为 `KLS-window`。

### 2.2 当前准确状态

- 引用 DI 谱 Kloosterman 大筛与 BFI dispersion/well-factorable 权重时，二点筛 BMD 链条达到 `External-theorem closed`。
- 若要求完全自足无黑箱，则 `KLS-window` 仍未在文内重证，不能宣称完全无黑箱闭合。

### 2.3 适配核查义务

主稿必须逐项核对：

| 项目 | 需核查内容 | 风险 |
| --- | --- | --- |
| 相位匹配 | 第 8 节双逆元相位是否完全落入 DI/BFI Kloosterman 相位类 | 相位符号或归一化偏差 |
| 模数范围 | `C≈P/log^{O(1)}P` 是否在外部定理 level 内 | level 超界 |
| 频率范围 | `H<=P/log^{O(1)}P` 是否被谱大筛覆盖 | Fourier tail 过长 |
| 系数范数 | `beta_s` divisor-bounded 与二范数是否满足假设 | 系数过粗 |
| 权重结构 | `lambda_d` 是否保持 well-factorable level | 权重不能接入 BFI |
| 损失账本 | dyadic、gcd、sawtooth、平滑损失是否均可由 `B(A)` 吸收 | 对数节省不足 |

## 3. RH 链条

RH 方向必须保持更严格的状态语言：

```text
RH-1 explicit-formula entrance
=> RH-2 CRT field transfer
=> RH-3 controlled exits
=> RH-4 no-cycle ledger
=> RH-5 final RH promotion
```

当前只能标注为 `Verification package` 或 `Referee-block`，不能标注为无条件 RH 证明。原因是 controlled exits 与 no-cycle ledger 尚未形成外部定理级或逐行自足级证明。

## 4. 合著稿统一闭合规则

全稿采用以下规则防止逻辑跳跃。

1. 存在性结论不能替代有符号平均分布估计。
2. 完整 CRT 周期均衡不能直接替代短窗口真实剩余分布。
3. 实验、扫描和数值证书只能作为证据等级，不作为证明。
4. 外部深定理版与完全自足版必须分开定理化。
5. 每个主结论必须有唯一依赖链，避免同一命题在不同章节中使用不同条件。

## 5. 下一步优化优先级

1. 把二点筛链条正式编号为 `TP-1` 至 `TP-9` 的定理/引理环境。
2. 把 `external-theorem-index.md` 中 DI/BFI 条件转写为主稿可引用的定理模板。
3. 为 `KLS-window` 建立变量适配核查表，并在主稿中标明“已核对/待核对”。
4. 将方阵行列章节压缩到 `Structured-EHPD` 单一最终接口。
5. 对 RH 章节继续使用 `Not claimed` 警示，直到 controlled exits 全部逐行闭合。

最新三命题统一优化矩阵见 `docs/monograph/three-proposition-closure-optimization.md`。在 `RSE` 被压缩后，方阵链条的第 4 项已细化为 `QLOW-MID-COMP(intervalized)+RRD+OSPC` 常数账本；其中 `QLOW-MID-COMP` 已有 `0.065` 外向舍入预算、正余量记录、Selberg 样本有理线性代数审计、trig/log 有理 oracle、H/Q 增量审计和 Phihat-free 的 sup-rho 旁路。新增 `docs/monograph/rse-rrd-ospc-margin-ledger.md` 给出 `0.053369509758272926` 可用余量，并把剩余拆为 `C_RRD<=0.020`、`C_OSPC<=0.020`、`C_SelbergUniform<=0.008`、`C_round<=0.003` 四个可审查目标。新增 `docs/monograph/rse-rrd-same-weight-reduction.md` 进一步证明 `RRD` 使用同一 `sum |omega_l|/l` 变差范数，并把 `C_RRD` 拆为 `RRD-low<=0.006`、`RRD-perp<=0.012`、`RRD-conversion<=0.002`。新增 `docs/monograph/rse-rrd-low-projection-dichotomy.md` 修正 `OSPC` 为 `E_dir>=1+delta_dir`，并把 `Pi_{<=Z}` 形式化为低模字典正交投影。新增 `docs/monograph/rse-low-block-exit-criterion.md` 给出 low-block 出口代数准则：无 `OSPC*` 时只需加权 CRT 缺陷界 `0.005366563145999495` 即可吸收 `RRD-low`。二点筛保持 `BMD-to-TLI` 审查；RH 保持 controlled exits 四列表。

相邻素数递推路线见 `docs/monograph/prime-matrix-recursive-lift-audit.md`。它保留了“旧核心素数不会被升级筛消去”的正确直觉，但指出 `Row(p)` 不能直接传递到 `Row(q)`：多数 `q` 行不包含完整 `p` 行，必须增加 `Seam(p,q)` 缝合窗口引理。新增 `docs/monograph/prime-matrix-seam-endpoint-audit.md` 将该引理压缩为 `SEB(p,q)` 端点屏障：相邻旧 `p` 行跨边界的末端无素数段与首端无素数段之和必须小于 `q`。新增 `docs/monograph/prime-matrix-seb-unconditionality-audit.md` 进一步审查后，结论是全局 `SEB` 过强，接近 `G(p^2)<=q` 的素数间隙输入；真正应攻的是只检查新 `q` 行漂移残基的 `ASB(p,q)`。新增 `docs/monograph/prime-matrix-asb-hard-attack.md` 又把 `ASB-Fail` 转化为低筛粗剩余与高素补洞的相对点覆盖矛盾 `ASB-RHC`；新增 `docs/monograph/prime-matrix-asb-rhc-alpha-sweep.md` 再把它等价改写为粗剩余素数比例下界 `RPD`；新增 `docs/monograph/prime-matrix-rpd-failure-structure.md` 将压力进一步定位到粗半素数投影；新增 `docs/monograph/prime-matrix-semiprime-anchor-projection.md` 又将半素数投影压缩到锚层效率接口；新增 `docs/monograph/prime-matrix-anchor-cofactor-interval-audit.md` 进一步把锚层效率改写为互补素数短区间平均；新增 `docs/monograph/prime-matrix-mge3-budget-audit.md` 将至少三粗因子项改写为低锚复合互补因子恒等式；新增 `docs/monograph/prime-matrix-mge3-second-anchor-audit.md` 继续压缩为第二锚粗尾恒等式；新增 `docs/monograph/prime-matrix-mge3-tail-envelope-audit.md` 将第二锚粗尾压成聚合 Mertens 包络或局部密度尖峰出口；新增 `docs/monograph/prime-matrix-tail-spike-localization-audit.md` 将尖峰进一步定位为 singleton-prime 双曲走廊；新增 `docs/monograph/prime-matrix-singleton-corridor-bound-audit.md` 给出唯一分解、低筛 z-rough 与走廊宽度三层上界；新增 `docs/monograph/prime-matrix-singleton-corridor-overlap-audit.md` 证明样本中同窗口走廊不重叠。该路线可作为 PM 的替代结构框架，但当前不能替代 RSE/RRD/OSPC 主链；其最小硬点已从泛化窗口存在性变为“素互补因子短区间上界 + 聚合 Mertens 包络 + 不相交 singleton 走廊并集 z-rough 上筛，或异常出口”，并仍需 annulus 壳层命题。

新增 `docs/monograph/prime-matrix-adjacent-shell-recursive-descent-route.md` 后，递归零行路线得到更精确的入口：相邻 `p<q` 时，`q^2` 内旧 `p`-筛唯一合数幸存者是 `q^2`；所以 `q` 零行可无损降为旧 `p`-筛 q 零窗，再二分为完整 `p` 行或 seam guard。该支线当前最小硬点是 `SeamGuard-Elimination`，即证明端点 guards 无法长期吸收幸存者，或其持续吸收进入 `SAE/PDEC/ColumnCRT`。

新增 `docs/monograph/prime-matrix-seam-multilevel-descent-route.md` 后，`SeamGuard-Elimination`
被进一步压成 `SMD-Global Inequality`：从 seam 零窗降到 `h<p` 时，复活点精确为
`P^-(n)∈(h,p]` 的点；若某条完整 `h` 行避开该集合，则 seam 强制下降为 `h` 零行。
实验账本 `p<=500` 全量与 `p<=2000` 抽样均无阻断。证明链优化的下一步应专攻全局复活点
非全覆盖不等式；若失败，则把持久阻断路由到 `SAE/PDEC/ColumnCRT`，而不是退回泛化模板覆盖。

新增 `docs/monograph/prime-matrix-seam-tail-mirror-descent-route.md` 后，SMD 的证明出口进一步加强：
强制 `h` 零行不必以绝对行号落入 `h×h`，只需其 CRT 行相位或尾镜像相位落入 `1..h`。
全量 `p<=500` 和 `p<=2000` 抽样均 `100%` 命中。当前最优专攻因此改为
`TailMirror-SMD` 的全局相位命中不等式；这是比单纯复活点非全覆盖更窄的接口。

新增 `docs/monograph/prime-matrix-total-zero-row-recursive-descent-route.md` 后，证明链最窄接口再升级：
不再分别处理 aligned/seam/末行端点，而是统一证明 `TotalDescent-TM`。有限账本显示所有非第一
`q` 行假想零行均能强制小阶方阵零行。下一步最优专攻应是把该有限相位事实转为全局不等式：
任意非命中相位若存在，则其复活点/端点/镜像结构必须产生 `SAE/PDEC/ColumnCRT` 缺陷。

新增 `docs/monograph/prime-matrix-total-descent-h3-margin-route.md` 后，最窄接口进一步变为固定
`h=3` 的六轮余量：完整 3 行只有一个六轮候选，阻断只来自 `5<=P^-(c_R)<=p`。若存在未阻断候选，
它就是旧 `p`-筛零窗的幸存点，直接排除假想 `q` 零行。有限账本到 `p<=5000` 全量无失败，最小
余量 `1`。优化结论是：后续不应再扩展任意 `h` 模板，而应专攻
`H3-SixWheel-Roughness` 或证明六轮全阻断相位进入 `SAE/PDEC/ColumnCRT`。

新增 `docs/monograph/prime-matrix-h3-sixwheel-hard-attack.md` 后，专攻对象进一步明确为
`H3 Full-Blocking Defect`。直接 `H3-SWR` 处在 `u=2` 筛法临界，风险等同平方根长度素数存在；
可推进方向是 first-factor partition 的缺陷化：高负载进 Tail/PDEC，低负载全覆盖进低模能量，
端点残余进 SAE/ColumnCRT。

新增 `docs/monograph/prime-matrix-h3-full-blocking-defect-audit.md` 后，数据优先级也清楚：
近失败窗口最高只到 `p=317`，且 first-factor 负载由小素数阶梯主导。下一步最优专攻应是
`small-first-factor skeleton overload => Tail/PDEC`，同时保留 `many-label low-mod energy => PDEC`
作为低负载备选出口。

新增 `docs/monograph/prime-matrix-h3-small-factor-envelope-route.md` 后，`small-first-factor` 分支
已不是纯经验判断，而是确定性包络二分：小骨架不过载就强制多中尾标签。下一步最小硬点应直接
攻 `SmallSkeletonOverload(y,K)=>Tail/PDEC` 的阈值定义与同口径上界。

新增 `docs/monograph/prime-matrix-h3-global-scaling-law-route.md` 后，H3 主链的高层策略固定为
“增长尺度压灭”证明：自然粗剩余约 `q/log q`，反例将其变成 `0`，必须产生命名缺陷。下一步仍
优先攻小骨架 Tail/PDEC 阈值，因为它是二分的第一出口。

新增 `docs/monograph/prime-matrix-h3-universal-scaling-inequality.md` 后，优化目标常数固定为
缺陷版 `c*q/log q` 下界，优先使用 `c=0.30`。下一步不是调参，而是证明低于该阈值必进入三出口。

新增 `docs/monograph/prime-matrix-h3-global-tail-energy-lemma.md` 后，这一步的组合证明已经完成到
全局尺度：`M_H3<B` 强制 `C_y>#A_s-B-2L` 或 `E_y(d)>L`，且证明只用 first-factor 分解、短窗
容量与整数二次能量恒等式。后续最优专攻应从“证明低余量进入缺陷”转为“排斥两个出口”：先攻
`SmallSkeletonOverload=>Tail/PDEC`，并行保留 `TailEnergy=>H3-PDEC/ColumnCRT`。

新增 `docs/monograph/prime-matrix-h3-small-skeleton-pdec-bridge.md` 后，第一出口已经完成桥接：
`C_y>#A_s-B-2L` 直接推出 `D_y>V_y-B-2L`，即低模 rough 计数亏损。下一步优先级应更新为
`PDEC defect exclusion for D_y` 与 `TailEnergy=>H3-PDEC/ColumnCRT`，而不是继续重证小骨架二分。

新增 `docs/monograph/prime-matrix-h3-tail-energy-fourier-bridge.md` 与
`docs/monograph/prime-matrix-h3-unified-defect-criterion.md` 后，尾能量出口也已变成
`F_y(d)>dL` 的非零 Fourier 缺陷。最优攻坚对象只剩一个统一命题：
`D_y` rough-count 缺陷与 `F_y` tail-Fourier 缺陷不能在正式坏窗族中同时逃逸。

新增 `docs/monograph/prime-matrix-h3-first-row-scale-bridge.md` 后，`q/log q` 量级的来源应改写为
第一行尺度守恒：H3 行平均为 `Pi_1(q)/2`，其中 `Pi_1(q)=pi(q)`。后续优化不应再寻找新的经验
常数，而应证明单行把这份平均质量压到零时必触发 `D_y/F_y` 缺陷。

新增 `docs/monograph/prime-matrix-h3-pointwise-closure-boundary.md` 后，下一步攻坚目标更窄：
不是再证明平均式，而是证明点态尺度转移或缺陷排斥。平均到点态的跳跃已明确标为无效推理。

新增 `docs/monograph/prime-matrix-disjoint-corridor-selberg-lemma.md` 后，上述 singleton 走廊并集上筛已不再停留在黑箱层，而是内联为有限 Selberg 二次型 `XΛ_z(ξ)` 与加权低模端点缺陷出口。递推路线的剩余硬点相应更新为“素互补因子短区间上界 + 聚合 Mertens 包络 + singleton Selberg 预算或端点缺陷排斥 + Annulus”。

新增 `docs/monograph/prime-matrix-asb-rpd-weighted-sieve-kernel.md` 后，素互补因子短区间和聚合 Mertens 包络又被统一为同一个加权区间 Selberg 二次型：半素数互补因子使用锚层 `P_{<A_\nu}`-rough 上筛，`M_{\ge3}` 第二锚尾使用 `P_{<B_\mu}`-rough 上筛，singleton 走廊使用不相交二次型。ASB/RPD 当前最小硬点因此变为“同权加权区间筛预算小于低筛粗剩余下界，或低模端点缺陷触发 CRTDefect/Tail-anchor/OSPC”，外加 `Annulus(p,q)`。

进一步新增 `docs/monograph/prime-matrix-rpd-first-anchor-identity.md` 后，上一句可再压缩：半素数与 `M_{\ge3}` 不应分开加预算；全部粗合数精确等于第一锚粗互补因子计数。因此当前最小硬点更新为“第一锚加权 rough-cofactor Selberg 预算小于低筛粗剩余下界，或低模端点缺陷触发 CRTDefect/Tail-anchor/OSPC”，外加 `Annulus(p,q)`。

新增 `docs/monograph/prime-matrix-rpd-fac-budget-audit.md` 后，该硬点有了首轮常数账本：全局模型量 `1075.256057`、真实 FAC 粗互补 `1454`、全局所需常数 `1.352236`；但逐窗口最大所需常数 `1.695703` 高于 `eta=0.10` 的逐窗口最小允许常数 `1.570917`。因此递推支线的下一步不能是裸全局 Mertens 常数，而必须是“分层/端点修正 FAC-Selberg 预算”与“低模端点缺陷出口”二分。

新增 `docs/monograph/prime-matrix-rpd-fac-lowmod-defect-audit.md` 后，低模端点缺陷出口已有明确数值形态：最尖峰窗口 `p=53,q_row=43` 在 `T=17` 已捕获 `90.9089%` 的 FAC 缺陷；同批窗口在 `T=101` 的最小捕获率为 `80.4688%`。下一步最小证明义务是把大的 `D_T` 变成有向 CRTDefect/Tail-anchor/OSPC，而不是继续放宽全局常数。

新增 `docs/monograph/prime-matrix-square-annulus-lift-lemma.md` 后，递推支线的 `Annulus` 接口也被结构化：平方壳层 `(p^2,q^2]` 中旧 `p`-筛幸存者除 `q^2` 外自动为素数；`pq` 是 `q` 倍数但已被旧筛删除。审计 `docs/monograph/prime-matrix-square-annulus-sieve-lift-audit.md` 给出 `max_p=2000` 下例外失败数 `0`，完整壳层行空段数 `0`，但最稀疏完整壳层行旧筛幸存者数只有 `1`。因此后续不再需要在壳层重新处理合数结构，只需证明相关 `q` 行壳层段的旧筛幸存者非空；该步骤不能用粗平均闭合。

新增 `docs/monograph/prime-matrix-annulus-rough-nonempty-hard-attack.md` 后，相关 `q` 行壳层段非空失败被写成负低模亏损 `D_{p^+}^{ann}(I)=-|I|V(p^+)`。它与 ASB/RPD 中正 FAC 尖峰共用同一个最终桥接：`large signed low-mod endpoint defect => directed CRTDefect/Tail-anchor/OSPC`。

新增 `docs/monograph/prime-matrix-signed-lowmod-bridge-hard-attack.md` 后，该最终桥接已拆成精确 Möbius 端点恒等式和 `SESE-low` 两步。第一步已严格证明：`D_T(I)=sum_{d|P_T} mu(d)({(L-1)/d}-{R/d})`，完整 `q` 行上是单位旋转 sawtooth 场；第二步仍待证：大 sawtooth 投影必须触发 `CRTDefect/Tail-anchor/OSPC`。

新增 `docs/monograph/prime-matrix-directed-endpoint-crtdefect-bridge.md` 与 `docs/monograph/prime-matrix-dec-ospc-exclusion-hardpoint.md` 后，第二步应再拆开：大端点投影已经能严格推出 `Directed Endpoint CRTDefect/OSPC*`；但单个 DEC 不是矛盾，因为完整 CRT 零均值不排除单个短窗端点尖峰。最终剩余应标为 `PDEC-or-SAE`：要么坏窗在同一低模块上形成持续端点缺陷并推出坏行指示函数的 Fourier/CRT 缺陷，要么孤立坏窗由单窗锚逃逸排斥。该接口闭合前，递推链仍是严格归约，不是无条件行命题证明。

新增 `docs/monograph/prime-matrix-semiprime-wheel-shadow-rigidity.md` 与 `docs/monograph/prime-matrix-semiprime-wheel-near-offset-audit.md` 后，`RCI/PDEC` 的分散分支又被压缩为 `WSH-Hall/PDEC`。固定偏移 `d` 的粗相位容量精确为 `rho_z(d)=prod_{r<=z,r∤d}(r-2)/(r-1)`：奇偏移由模 `2` 归零，`±2` 类偏移继续被 `3,5,7,...` 逐层削弱，`±6,±12,±30` 因含小素因子而更宽但仍非自由。下一步应证明轮筛允许 Hall 匹配，或把匹配失败导入固定偏移 CRTDefect、Tail-anchor 或 Endpoint/PDEC。

新增 `docs/monograph/prime-matrix-row-reflection-period-audit.md` 后，CRT 行反射被校正为可用但有限的工具。若 `p` 对齐全覆盖行为 `r`，则镜像行 `N-r+1` 必全覆盖；第二周期复现给出的轨道为 `r,N-r+1,N+r,2N-r+1,...`，相邻间隔交替为 `N-2r+1` 与 `2r-1`，不是短平移周期。即使只要求全覆盖现象复现，`r,2r,2r-1` 也不是自动现象周期；样本 `p=23,r=59` 中 `r+59=118`、`r+117=176`、`r+118=177` 都不是零行。可保留的证明增益是“两端帽排斥”和条件稳定子引理 `period d => gcd(N,d)>=r`，可作为 `PDEC-or-SAE` 的端点刚性输入。

新增 `docs/monograph/prime-matrix-p23-zero-recurrence-audit.md` 后，`P=23` 的真实复现结构被完整确认：周期内零行 `3456` 个，镜像前复现 `3454` 次，首次复现在第 `2612` 行而不是第 `118` 行。复现的本质是不同 CRT 相位向量重新组成覆盖证书；间隔不规则，不能写成短周期。最新分层读数进一步显示，同一 `2,3,5,7` 骨架 `r≡59 (mod 210)` 在镜像前有 `324` 个零行，第 `59` 与 `6569` 行共享三洞 `5,9,15`，由 `13,17,19` 与 `19,13,17` 两套高标签置换补齐。该事实支持下一步把“复现稳定性”作为条件出口：若短平移稳定则触发 gcd 限制，否则进入层级稀疏相位证书的 `PDEC/SAE` 账本。

新增 `docs/monograph/prime-matrix-short-recurrence-gap-audit.md` 后，`2P` 短复现路线被校正：全局短间隔禁止为假，`P=19`、`P=23` 均有周期内部的 `<=2P` 短复现簇；边界短间隔版本则与 `first_zero>P` 等价，因为跨周期首尾间隔恒为 `2r0-1`。优化方向因此不是证明全局零行稀疏，而是证明首端帽/尾端帽的边界相位非覆盖：前 `P` 行低素数骨架必留洞，且高素数补洞标签的 CRT 最小代表越过 `P`。

新增 `docs/monograph/prime-matrix-boundary-phase-noncoverage-hard-attack.md` 后，边界帽路线压缩为单一核心接口 `BPN-RM`：低素数骨架在 `x<P` 内留下残洞；任何高素数标签补洞若保持 `x<P`，必须释放一个旧覆盖列，因此完整覆盖证书的 CRT 最小代表 `x_S` 不可能小于 `P`。该路线吸收了前缀势垒、完整覆盖最小相位、短复现反例和 Sylvester 大因子弱输入。诚实状态：`BPN-RM` 尚未逐行证明；在闭合前，边界相位非覆盖只能标为严格归约，不能标为无条件定理。

新增 `docs/monograph/prime-matrix-boundary-residual-migration-audit.md` 后，`BPN-RM` 的正确非循环版本更清楚：局部补洞可发生，不能声称高素数补洞能力不足；可攻对象是残洞势函数。全局陈述“补洞必有新洞”与 `BPN(P)` 几乎等价，因此下一步必须证明一个独立势函数不等式 `Phi(R(y))>=1`，而不是把等价命题换名。

新增 `docs/monograph/prime-matrix-crt-solution-set-geometry-audit.md` 后，CRT 解集路线被校正：`R(N-r+1)=P-R(r)` 给出精确镜像和两端帽，但中区素数/粗合数密度是数值层，不是 CRT 筛幸存数的单调势能。该路线可提供势函数候选，但目前不能单独证明边界零行不存在。主链仍回到 `BPN` 残洞势函数或 `GridPrimeGap` 条件输入。

新增 `docs/monograph/prime-matrix-crt-zero-solution-distribution-audit.md` 与脚本 `experiments/prime_matrix_crt_zero_solution_distribution_audit.py` 后，零行被写成精确 CRT 覆盖方程组
`Z_P=cap_c union_{ell<P}{r: r=1-cP^{-1} mod ell}`。完整扫描 `P=13,17,19,23` 显示边界帽零行数均为 `0`，镜像严格成立；但十等分平均幸存列数基本相同，说明“中区粗合数密集”不能作为单调势能推出边界帽无零行。新的可审查硬点更精确：证明所有完整覆盖证书的 CRT 最小正代表 `>=P`，或构造非循环残洞势函数 `Phi_P(R)`。

新增 `docs/monograph/prime-matrix-zero-row-spacing-gradient-audit.md` 与脚本 `experiments/prime_matrix_zero_row_spacing_gradient_audit.py` 后，零行间隔梯度猜想被校正：首尾跨周期边界间隔 `Delta_edge=2r0-1` 在样本中均大于 `2P`，但这等价于 `r0>P`，即等价于 `BPN(P)`；同时全局“中心更密、边界更稀”的十等分梯度为假，`P=23` 边缘十等分零行数 `361` 反而高于中心十等分 `342`。因此主链不能使用全局密度梯度，只能把边界间隔作为 `BPN-Defect` 目标形式：若边界帽有零行，则双端镜像证书距离 `<=2P-1`，需推出低模 CRT 缺陷、Tail-anchor 缺陷或残洞势函数矛盾。

新增 `docs/monograph/prime-matrix-bpn-defect-bonferroni-audit.md` 与脚本 `experiments/prime_matrix_bpn_defect_bonferroni_audit.py` 后，边界帽最优硬点进一步从抽象 `Phi` 势函数压缩为 `BPN-B5`：证明五阶 Bonferroni 下界
`S5(r)=(P-1)-I1+I2-I3+I4-I5>0` 对所有 `2<=r<=P` 成立。边界事实 `r<=P` 使所有 `d>=P^2` 的交集项为 `0`，所以该不等式是有限且可逐项审查的。审计显示三阶 `S3` 会失败，但 `P<=199` 的全部边界帽行中 `S5` 未失败，最坏 `P=199` 仍有最小 `S5=12`。下一步最优攻坚应是证明 `I1-I2+I3-I4+I5<P-1`，失败时再转带权 Selberg/Brun 或 CRTDefect/Tail-anchor 出口。

同一审计进一步给出 `BPN-B5` 的逐点恒等式：`S5(r)=prime_like_count-high_omega_penalty`，其中高重惩罚只来自同一行内含至少六个 `<P` 小素因子的数，权重为 `binom(omega_P(n)-1,5)`。选点扫描到 `P=5003` 仍为正，最坏样本 `P=5003` 的最薄行有 `272` 个素数型点、惩罚 `95`、余量 `177`。这把下一步硬点再压成：证明长度 `P` 边界短窗中，至少六小素因子整数的加权数量严格小于素数数量；若失败，则失败应表现为小核心乘积过密或 Tail-anchor/CRTDefect。

新增 `docs/monograph/prime-matrix-bpn-high-omega-core-audit.md` 与脚本 `experiments/prime_matrix_bpn_high_omega_core_audit.py` 后，高重惩罚进一步按六小素核心 `core6` 分桶。样本最薄行显示惩罚项有明显 core 结构：小/中 `core6` 桶对应固定小核心倍数在长度 `P` 短窗中过密，大 `core6≈n` 桶对应尾锚或端点集中。由此 `BPN-B5` 的下一步最小出口可写成 `Core6-Density-or-TailAnchor`：若高重惩罚压过素数数目，则某个 core6 桶产生可命名的 CRT/Tail-anchor 缺陷；否则五阶下界保持正。

新增 `docs/monograph/prime-matrix-bpn-bonferroni-order-risk-audit.md` 与脚本 `experiments/prime_matrix_bpn_bonferroni_order_risk_audit.py` 后，固定阶路线被校正：任意固定奇阶 Bonferroni 截断在 `lambda≈log log(P^2)` 的独立模型下都会在有限 `lambda` 后变号。`P=10007` 样本仍有 `S5=236>0`，但高重惩罚/素数型点比例已达 `0.532673`，显示固定五阶不能作为全局终局。主线最优硬点应升级为 `BPN-BK/Selberg`：取 `K≈c log log P` 的可变阶 Bonferroni/Brun 截断，或构造 Selberg/Brun 非负筛权；`Core6` 相应升级为低阶失败时的 `CoreK-Density-or-TailAnchor` 出口。

新增 `docs/monograph/prime-matrix-bpn-bk-weight-model-audit.md` 与 `docs/monograph/prime-matrix-bpn-bk-selberg-route.md` 后，`BPN-BK/Selberg` 的可审查表述进一步收紧：普通 Selberg/Brun 下界筛在边界行 `H=P,z=P` 下只有 `s<=1`，不能单独给正筛余。下一步真正硬点不是“再换一个筛权”，而是严证 `S_K(r)<=0` 必推出 `BK-DEC` 端点 sawtooth 缺陷或 `CoreK` 高重桶过密，并由 `Directed CRTDefect/Tail-anchor/PDEC-or-SAE` 排斥。

新增 `docs/monograph/prime-matrix-bpn-bk-dec-bridge-proof.md` 后，`BK-DEC=>Directed Endpoint CRTDefect` 已严格闭合。证明依赖三个确定事实：零行使奇阶 BK 总和非正；低阶 BK 截断精确等于 `(P-1)V_{K,D}+E_{K,D}(r)`；大端点项经低模分块鸽巢给出某个块投影异常。当前最小硬点因此继续前移到 `BK tail budget/CoreK tail control` 与 `PDEC-or-SAE` 排斥。

新增 `docs/monograph/prime-matrix-bpn-bk-tail-core-dichotomy.md`、`docs/monograph/prime-matrix-bpn-tailcore-corridor-reduction.md` 与 `docs/monograph/prime-matrix-bpn-tailanchor-persistence-dichotomy.md` 后，`BK tail/CoreK` 已不再是黑箱：尾项失败推出尾核心桶过密；尾核心桶过密推出尾锚集中或分布式走廊饱和；尾锚集中再推出 `SAE-anchor` 或持续尾锚低模缺陷。因此当前最小硬点压为 `PDEC-or-SAE` 与 `Distributed corridor saturation` 的 Selberg/CRTDefect 排斥。

新增 `docs/monograph/prime-matrix-bpn-distributed-corridor-saturation-reduction.md` 后，分布式走廊饱和又被压成高重叠固定核心缺陷或着色不相交走廊预算违例。高重叠分支归入 `PDEC-or-SAE`；低重叠分支归入 `Colored disjoint-corridor core-sieve budget/low-mod CRTDefect`。因此下一步最小硬攻应在两个最终出口中选择：要么攻 `PDEC-or-SAE`，要么攻不相交着色走廊的核心筛预算。

新增 `docs/monograph/prime-matrix-bpn-colored-corridor-core-sieve-budget.md` 后，着色走廊的核心筛预算已改成有限 Rankin smooth-core 账本，避免误用 rough Selberg 下界。当前最小硬点更新为：`PDEC-or-SAE`、finite Rankin smooth-core ledger 常数闭合、low-mod core CRTDefect 排斥。

新增 `experiments/prime_matrix_bpn_rankin_ledger_certificate_audit.py` 后，finite Rankin 账本已有证书工具。它对正式走廊列表给出 exact core count、Rankin ledger 与 low-mod residue spike；若常数闭合失败，应直接抽取 `low-mod core CRTDefect`，而不是继续使用粗全局 smooth-core 包络。

新增 `docs/monograph/prime-matrix-bpn-lowmod-core-crtdefect-bridge.md` 后，low-mod core CRTDefect 已由 Fourier 反演并入 `PDEC-or-SAE`。当前 BPN-BK 只剩两个独立任务：`PDEC-or-SAE` 排斥，以及正式走廊证书上的 finite Rankin smooth-core ledger 常数闭合。

新增 `docs/monograph/prime-matrix-bpn-unified-pdec-sae-dichotomy.md` 后，`PDEC-or-SAE` 被统一为 endpoint/core 共用的低模测试函数二分。Persistent 分支已经严格 Fourier 化；Sparse 分支就是 SAE local escape。当前最终剩余为 `PDEC exclusion`、`SAE local escape exclusion` 和 finite Rankin ledger constants。

新增 `docs/monograph/prime-matrix-bpn-rankin-ledger-acceptance-theorem.md` 后，finite Rankin ledger constants 已变成可验收证书：`rankin_budget_pass=true` 即闭合该颜色类；失败者必须低模化或细分。当前最终剩余进一步精确为 `PDEC exclusion`、`SAE local escape exclusion`、正式着色走廊 Rankin certificates 全部通过或失败者进入 PDEC/SAE。

新增 `docs/monograph/prime-matrix-reverse-zero-row-dichotomy.md` 后，用户提出的“q 零行反推 p 零行”被严写为二分：`q` 零行先变成旧 `p`-筛长度 `q` 零窗；若起点相位 `a_s>=p-(q-p)`，则包含完整 `p` 对齐零行并直接矛盾；若 `a_s<p-(q-p)`，则只形成相邻 `p` 行的缝合零窗。审计显示核心区直接支仅约 `0.00616`，主支是缝合零窗。因此下一步最小硬点应攻 `SeamSafe/ASB-or-PDEC`，而不是继续尝试从所有 `q` 零行直接推出 `p` 对齐零行。

新增 `docs/monograph/prime-matrix-wsh-scb1-long-block-expansion-template.md` 与
`experiments/prime_matrix_wsh_scb1_long_block_certificate.py` 后，`WSH-Hall/PDEC` 的长块分支也被
材料化：`17<=p<=2000` 中 `4573823` 个 `|B|>=4` 连续长块最小余量为 `3`，最紧长块均触发
`Fixed-offset-full-load` 与 `Endpoint-margin`。当前最优攻坚点因此不再是扩大 SCB 枚举，
而是证明固定偏移满载必进入 persistent `PDEC` 或稀疏 `Endpoint/SAE` 出口；完成后可把
`SCB-1` 与 `SCB-2` 合并为单一 `Endpoint/PDEC` 最终排斥接口。

新增 `docs/monograph/prime-matrix-wsh-fixed-offset-pdec-absorption.md` 与
`experiments/prime_matrix_wsh_fixed_offset_pdec_ledger.py` 后，固定偏移满载的第一层已闭合：
`1<n<q^2` 的合数必有 `<=p` 因子，满载偏移排除小轮素数后，缺失候选必由 `(13,p]`
解释。有限账本在 `11` 条满载偏移行上核验无未解释候选。当前最小硬点更新为
`FO-PDEC`：分散解释因子必须产生 persistent low-mod CRTDefect/PDEC，或进入稀疏
`SAE/Endpoint`。这是真正出口排斥，不应被写作已经完成的无条件闭合。

新增 `docs/monograph/prime-matrix-wsh-fo-pdec-hard-attack.md` 与
`experiments/prime_matrix_wsh_fo_pdec_lowmod_audit.py` 后，`FO-PDEC` 继续压缩：
每条缺失候选都严格给出 `r=1-cq^{-1} mod ell` 与 `uv+d=0 mod ell` 两个方程，
有限账本 `43` 条方程无失败。当前最窄硬点已不是结构发现，而是定量能量：
证明这些低模方程的正超额达到 `PDEC` 阈值，或把非持久部分送入 `SAE/Endpoint`。

新增 `docs/monograph/prime-matrix-wsh-fo-pdec-energy-lemma.md` 与
`experiments/prime_matrix_wsh_fo_pdec_energy_ledger.py` 后，定量能量产生本身也已闭合为组合引理：
若 `t_ell<=theta ell` 对所有解释因子成立，则低模能量 `>= (1-theta)|E|`；否则同一解释因子
高负载已经触发 `Tail/PDEC`。当前唯一硬点收窄为同一坏窗集合上的 `PDEC` 阈值比较
`U_CRT(E)<E(E)` 或 `L_PDEC(E)<=(1-theta)|E|`。

新增 `docs/monograph/prime-matrix-wsh-fo-pdec-threshold-comparison.md` 与
`experiments/prime_matrix_wsh_fo_pdec_threshold_ledger.py` 后，该阈值比较下界侧已具体化为
`ell=199,h=95` 的 Fourier 投影，阈值 `3.959247567099438`。下一步如果继续硬攻，就必须直接给出
同一投影的 `U_CRT,199` 合法上界或 `SAE/Endpoint` 非持久吸收。

新增 `docs/monograph/prime-matrix-wsh-fo-pdec-dual-cluster-route.md` 与
`experiments/prime_matrix_wsh_fo_pdec_dual_cluster_audit.py` 后，`U_CRT,199` 上界的实际障碍已
显现：最佳频率把支撑压到长度 `11` 的对偶短弧，Fourier 距离质量上界只差
`0.04075243290056196`。下一步必须攻对偶短弧聚簇排斥，而不是继续泛泛提高能量下界。

新增 `docs/monograph/prime-matrix-wsh-fo-pdec-multiplicity-legitimacy.md` 与
`experiments/prime_matrix_wsh_fo_pdec_primitive_cluster_audit.py` 后，最后一步的集合口径风险被暴露：
强阈值 `3.959...` 依赖 equation/block-local 多重计数；physical 去重后为 `1.9699...`。
因此下一步必须先证明多重计数合法，或在 primitive 口径下重做 `U_CRT`/SAE 排斥。

新增 `experiments/prime_matrix_wsh_fo_pdec_formal_unit_audit.py` 后，风险进一步定位为 formal unit
一致性：`3.959...` 来自跨 `q` 层与嵌套块的有限库聚合；单个正式单元坐标去重后最佳值为
`1.0`。因此下一步最优不再是直接优化 `U_CRT,199`，而是证明
`FormalUnit-Stitching` 或 `NestedBlock-Independence`；若失败，重复项必须回流到
`SAE/Endpoint`。

新增 `prime_matrix_wsh_fo_pdec_stitching_feasibility_audit.py` 与
`prime-matrix-wsh-fo-pdec-branch-separation-theorem.md` 后，前述目标进一步细化：
不同 `q` 层已证明不能无条件拼接，同坐标嵌套重复已证明必须坐标商掉，除非补上
`Weighted Hall Dual Independence`。因此当前最小硬点是加权 Hall 对偶独立性或 exact duplicate
的 SAE/Endpoint 吸收。
