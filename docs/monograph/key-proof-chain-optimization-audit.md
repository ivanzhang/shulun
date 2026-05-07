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

新增 `docs/monograph/prime-matrix-h3-square-root-short-interval-barrier.md` 后，最小硬点被识别为
平方根长度短区间障碍与筛法奇偶障碍的交点。后续若继续攻坚，应直接攻
`Square-root Defect Exclusion`，而不是再包装平均尺度。

新增 `docs/monograph/prime-matrix-h3-square-root-defect-exclusion-hard-attack.md` 后，攻坚顺序明确：
先接受 `D_y` 小筛层可控，把全部火力集中到尾标签/双粗精确补洞排斥。

新增 `docs/monograph/prime-matrix-h3-tail-filler-rigidity-hardcore.md` 后，下一步最窄攻坚应是
`Tail-Filler Global Incompatibility`：局部 `2/4/6` 短差值互质单元不能整行拼接。

新增 `docs/monograph/prime-matrix-h3-tail-filler-global-chain-capacity.md` 后，上述攻坚面已改写为
`H3 Tail Edge/Triple Capacity`：尾补洞连续块 `B` 若拼满，则相邻边证书数为 `|B|-1`，
三连端点证书数为 `|B|-2`。在高 cutoff 下，有序标签对一行内不可复用，尾点半素数化。
下一步最优攻坚不再是寻找新平均尺度，而是证明边/三连容量严格小于满链需求，或证明满容量强制
`PDEC/ColumnCRT/endpoint/cofactor` 缺陷。

新增 `docs/monograph/prime-matrix-h3-tail-edge-selberg-exclusion.md` 后，最优攻坚推进一层：
宏观满尾链由二维 Selberg 上筛排除，长度上界为 `O(q/log^2 y)`。因此 H3 尾分支不再需要
证明“整行双粗尾链不可能”；它已经被 rough 对上界压掉。新的最窄硬点是
`ShortBlock-PDEC Routing`：若全阻断仍成立，尾块只能短而多，小骨架切割必须转化为
`D_y/PDEC` 缺陷，或短块端点/列位移/互补商集中转化为 `ColumnCRT/endpoint/cofactor`。

新增 `docs/monograph/prime-matrix-h3-shortblock-singleton-barrier.md` 后，最优攻坚面再次收窄并
修正：`ShortBlock-PDEC Routing` 中“切割频率本身给 PDEC”并不成立。尾块恒等式 `T=J+E`
与二维上筛 `E=O(q/log^2 y)` 说明，主要剩余是 `J_1=T+O(q/log^2 y)` 个孤立尾点。
下一步必须专攻 `Singleton Tail Exclusion`：用孤立尾点的
`ell>y` 尾标签和左右 `r_-,r_+<=y` 小骨架夹逼同余，逼出
`PDEC/ColumnCRT/endpoint/cofactor` 缺陷。

新增 `docs/monograph/prime-matrix-h3-singleton-clamp-defect-criterion.md` 后，`Singleton Tail`
已被 CRT 单元化。每个孤立尾点落入一个夹逼低模类；加尾标签后落入模
`ell*lcm(r_-,r_+)` 的唯一类。最优攻坚面现在是 `Distributed Singleton Signed Excess`：
尾标签集中与夹逼低模集中都可路由为命名缺陷；剩余分散容量仍可能自然容纳 `q/log y`
个双粗点，必须证明该分散半素数过剩强制 `PDEC/ColumnCRT/endpoint/cofactor`。

新增 `docs/monograph/prime-matrix-h3-distributed-singleton-bilinear-obstruction.md` 后，最优攻坚面
进一步精确为 `Distributed Singleton Bilinear Exclusion`。分散孤立尾点在 `y>q^(2/3)` 下是
`ell*m` 双素乘积；夹逼相位给互补商移动同余 `m≡ell^{-1}rho(c) mod R(c)`。下一步不应再
重复容量抽屉，而应直接证明该短互补商双线性有符号误差小，或把大误差送入
`endpoint/PDEC/ColumnCRT/cofactor`。

新增 `docs/monograph/prime-matrix-h3-bilinear-large-sieve-defect-bridge.md` 后，下一步最优攻坚
更窄：大有符号误差已经通过角色展开变成非主角色双线性频率缺陷。普通大筛仍差短窗口
dispersion；因此后续应直接攻 `H3-DSB-LS/KLS`，核验是否能由已有 DI/BFI/KLS-window
外部输入覆盖，或把该非零频率并入 `PDEC/ColumnCRT/cofactor`。

新增 `docs/monograph/prime-matrix-h3-dsb-kloosterman-window-reduction.md` 后，`H3-DSB-LS/KLS`
已具备标准逆元相位：`e(-h*rho*bar(ell)/R)`。下一步最优攻坚不再是泛称“引用大筛”，而是
逐项闭合四分支：KLS 覆盖活跃参数、高 lcm 夹逼、 高频端点尾、系数集中。

新增 `docs/monograph/prime-matrix-h3-dsb-high-lcm-clamp-routing.md` 后，高 lcm 夹逼分支已
被压成可审稿二分：`R(c)>R_0` 的大质量必须是大量单点级高 `lcm` 激活；若跨行持久，
进入 `PDEC/ColumnCRT` 非零频率缺陷，若不持久，进入 `SAE` 单窗逃逸。下一步最小硬点
相应变为排除 `Persistent-HLC/Sparse-HLC` 出口，或转攻另外两个 KWR 分支：
高频端点尾与系数集中。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-fourier-energy-clamp.md` 后，这个最小硬点
继续收窄：同模高 `lcm` 块的非零 Fourier 能量精确等于
`R sum mu(a)^2-U^2`，在 `U<=R/2` 时至少为 `RU/2`。因此高 `lcm` 分支已变成
能量注入后的出口排斥问题：持久能量排斥归入 `PDEC/ColumnCRT`，单窗能量排斥归入
`SAE/endpoint`。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-pdec-threshold-bridge.md` 后，persistent
分支的最小审查点已经是单个不等式：
`U_CRT(B)<L_HLC(B)`，其中
`L_HLC(B)=((R sum g_B(a)^2-U_B^2)/(R-1))^(1/2)`。若 `U_B>R/2`，则作为稠密有效模
集中回流到 KLS/PDEC/SAE，不再是分散高 `lcm` 自由出口。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-pdec-failure-localization.md` 后，若上述
不等式失败，失败相位被定量局部化为 Bohr-cap 质量下界
`G_alpha>=(L-alpha U)/(1-alpha)`。下一步最小硬点不是再找新分支，而是排除这些
Bohr-cap 集中，或把持久帽变成可通过的 PDEC 约束、把孤立帽变成 SAE/endpoint 证书。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-bohr-cap-component-route.md` 后，Bohr-cap
又被拆成 high-gcd cap 与 short-arc cap。当前最小硬点变为：证明大 `d=(h,R)` 是低有效
模集中并可由 PDEC/ColumnCRT 处理；小 `d` 时短弧组件必须由 PDEC 约束或 SAE/endpoint 排除。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-high-gcd-descent.md` 后，大 `d` 分支已严格下降：
`R'=R/d`、`\hat g_R(h)=\hat g_{R'}(h/d)`，帽质量无损保留，迭代有限终止。当前最小硬点
只剩低有效模出口和 short-arc cap。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-short-arc-density-pressure.md` 后，short-arc cap
进一步变为密度压力不等式。下一步最小硬点是优化 `alpha,D0,epsilon`，证明压力超阈值
触发 PDEC/SAE，或把压力低残余接回低有效模 KLS/PDEC。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-short-arc-pressure-optimizer.md` 后，压力低残余
已经接回 `t=L/U` 的一维阈值与 L2 平坦性。当前最小硬点变为：提交有限参数压力证书，
或证明 L2-flat HLC residual 满足 KLS-window 系数二范数核验。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-l2-flat-kls-admission.md` 后，最小硬点从
“是否能进 KLS”改为 K1--K6 admission 核查。K4 已由 L2-flat 给出；剩余是模数、频率、
端点、gcd/unit 和分块条件，或对应出口排斥。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-clean-kls-reduction.md` 后，K1--K6 核查又被
压成 clean-unit 定理。当前最小硬点就是 `HLC-KLS-ext`：对 clean HLC 窗口和 `(CKR-4)`
给出 `O(q/log^2 y)` 上界，或文内重证相应 KLS-window。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kls-external-adaptation.md` 后，`HLC-KLS-ext`
在外部深定理版中已完成适配。优化结论相应更新：H3-HLC 的内部结构缺口已压到 clean
Kloosterman 窗口；若接受 DI/BFI/Kuznetsov 窗口化 Kloosterman 输入，该分支闭合。若坚持
完全自足无黑箱稿，真正最小硬点就是内联重证该窗口化谱/dispersion 定理，而不是继续拆分
high-lcm、short-arc 或 L2-flat 子情形。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kls-core-reduction.md` 后，上述最小硬点再被
压缩为 `HLC-KLS-core`：对单个 clean dyadic/Type block 的标准核 `(CORE-2)` 证明
`|\mathfrak S(\mathscr D)|<=\mathcal N(\mathscr D)/log^A y`。该文已证明从 `(CORE-5)`
到 `(CKR-5)` 的所有账本步骤；下一步若继续硬攻，必须直接证明或精确引用 `(CORE-5)`。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kls-core-self-contained-spine.md` 后，下一步硬点
再次收窄为 `Kuznetsov-LS atom (SC-9)`。该文件完成了 completion、单位群归一化、二范数
账本和 `SC-9=>CORE-5`；同时证明点态 Weil 只给临界平方根级，不能提供所需任意对数节省。
因此继续攻坚时必须进入 Kuznetsov trace formula / spectral large sieve 的内联证明。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kuznetsov-ls-atom-expansion.md` 后，`SC-9`
已经分解为 KZ-A--KZ-E 五个子原子。下一步最优顺序是先攻 KZ-C（Bessel transform
衰减，最短），再攻 KZ-D（谱大筛），再攻 KZ-B（trace formula 正规化），最后攻 KZ-E
（BFI/well-factorable 对数节省）。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kz-c-bessel-transform-decay.md` 后，KZ-C 已闭合。
当时下一步最优硬点更新为 KZ-D：spectral large sieve with oldform/Eisenstein。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kz-d-spectral-large-sieve-spine.md` 后，KZ-D
已压缩为 `PTK-D` 预迹核上界；oldform/Eisenstein/holomorphic 账本不再是独立黑箱。
当时下一步最优硬点更新为 PTK-D。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-ptk-d-pretrace-kernel-bound.md` 后，PTK-D
已压缩为空间侧 `LPC-D` 格点/相关行列和上界。当时下一步最优硬点更新为 LPC-D。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-lpc-d-spatial-correlation-split.md` 后，LPC-D
已压缩为 `GHLC-D`：generic hyperbolic local correlation。当时下一步最优硬点更新为 GHLC-D。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-ghlc-d-local-schur-closure.md` 后，GHLC-D 的
正确闭合方式已明确：在积分核层用局部 `L^1` 质量
`T^2∫_0^{T^{-1}log^B y}(1+Tr)^{-A}sinh(r)dr=O(1)`，再用 Poincare 包 Schur 归一化给出
行列和 `O(N_0log^C y)`。这避免了点态近邻计数保留 `T^2` 的错误。于是
`GHLC-D=>LPC-D=>PTK-D=>KZ-D`，KZ-D 不再是当前未闭合原子；完全自足链剩余更新为
KZ-B 与 KZ-E。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kz-b-kuznetsov-trace-specialization.md` 后，KZ-B
由 automorphic kernel、Poincare unfolding、双陪集 Kloosterman 几何侧和谱 Plancherel 侧的
比较闭合。它只负责公式专门化，不产生 `log^{-A}`。当前完全自足链的唯一剩余原子更新为
KZ-E：BFI/well-factorable dispersion logarithmic saving。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kz-e-well-factorable-dispersion-spine.md` 后，
KZ-E 的筛权分解、dispersion 恒等式、CRT 相位归一化、gcd/端点账本均已内联；最小硬点
进一步压缩为 `WFD-core`。该核心是窗口化 well-factorable Kloosterman dispersion 平均估计，
不能由点态 Weil 或普通大筛替代。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-wfd-core-balanced-factor-reduction.md` 后，
`WFD-core` 经平方根 well-factorable 分解压缩为 `BWFD-core`。现在不应再攻筛权分解或 gcd
层；唯一硬点是 `u,v≈C^{1/2}` 的 balanced two-modulus Kloosterman 平均 `(WB-11)`。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-bwfd-core-spectral-completion-attack.md` 后，
`BWFD-core` 经 `s` 变量精确完成和完整 Kloosterman 乘法公式压缩为 `BSC-core`。现在不应再攻
completion 或单模谱大筛；该步当时的硬点是 `(BSA-13)` 的 balanced complete Kloosterman
bilinear correlation 任意对数节省。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-bsc-core-kloosterman-fraction-attack.md` 后，
`BSC-core` 被逐项展开为 `e(\bar vR/u+\bar uT/v)` 的互逆分数相位。现在不应再停留在
Kloosterman 和符号层；该步当时的硬点是 `(KFA-17a)`--`(KFA-17b)` 的 `KFLS-core`，即 balanced
Kloosterman-fraction large sieve 任意对数节省。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kfls-core-square-kernel-attack.md` 后，`KFLS-core`
被平方化为中心化四模数核。现在不应再尝试全核绝对 Schur；该路线被对角层阻断。唯一硬点
更新为 `(SQK-21)`--`(SQK-23)` 的 `CFQK-core`，即 centered four-modulus Kloosterman-fraction
correlation saving。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-cfqk-core-block-centering-attack.md` 后，`CFQK-core`
的半对角被修正：同 `(u,v)` 块半对角不能估小，必须作为局部方差中心化扣除。当前硬点更新为
`BD-CEN + OSQK-core + TFQK-core`；在尚未核查 BD-CEN 前，暂不能直接跳到三模数的
`OSQK-core`。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-bd-cen-dispersion-centering-audit.md` 后，最窄目标
顺序一度修正为：`BD-CEN` 尚未闭合。当前 KZ-E spine 只证明 `h=0` 主项抵消，没有证明同
`(u,v)` 块投影扣除 `(BDC-5)`，因此当时不能直接跳到 `OSQK-core`。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-bd-cen-no-go-route-fork.md` 后，`BD-CEN identity`
在当前对象下被反证。此时不应继续试图从现有 KZ-E 推出 `(BDC-5)`；路线曾分叉为
`SOURCE-CEN` 源头块中心化、`BLK-energy-core` 块能量节省，或明确使用外部 DI/BFI。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-source-cen-no-go.md` 后，`SOURCE-CEN` 也被反证：
源头块中心化会把当前未块中心化的 `WFD-core (KE-13)` 换成另一个对象，不能作为恒等式加入。
新增 `docs/monograph/prime-matrix-h3-dsb-hlc-blk-energy-core-obstruction.md` 后，裸
`BLK-energy-core` 也被证明不能作为平方核层任意系数数组定理成立。当前最窄
无黑箱义务不再是 `SOURCE-CEN` 或裸块能量估计，而是：

```text
NC-BLK actual coefficient block non-concentration,
or external DI/BFI original dispersion theorem.
```

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

新增 `docs/monograph/prime-matrix-cylindrical-completion-line-barrier.md` 与
`experiments/prime_matrix_cylindrical_completion_audit.py` 后，用户的圆柱斜线直觉被严写为
`Completed-Line Skeleton`：第 `x<P` 行先由已绕完整圆柱的 `q<=x` 斜线形成低素数骨架
`R_x`，再由未完成的 `x<q<P` 斜线补洞 `F_x`；若 `R_x\F_x` 非空，则其中每一点自动为素数。
样本 `P=23,101,499,997,1999,5003` 的最薄行均满足正余量，`P=5003` 仍有 `260` 个最终洞。
这说明“还有斜线未画完”本身不是证明，不变量应改为 `|F_x|<|R_x|`。当前最小硬点更新为
`Incomplete-FillerBound`：证明未完成高素斜线不能吃掉全部已完成骨架残洞；若失败，则失败必须
表现为低模 CRT 缺陷、Tail-anchor 集中或 SAE 单窗逃逸。

新增 `experiments/prime_matrix_incomplete_filler_deficit_audit.py` 后，`Incomplete-FillerBound`
在底部 `h=P-x<sqrt(P)` 带进一步变成缺口二次曲线问题：若未完成线命中骨架残洞，则
`xP+c=(P-a)(P-b)`，从而 `a+b=h` 且 `c=ab`。样本 `P=997,1999,5003` 的底部带所有命中均满足
该 clean pair identity，且每行最多 `2` 个补洞。下一硬点可改写为
`BottomDeficitPairBound`：证明低骨架残洞 `R_{P-h}` 不可能全部落在 `c=a(h-a)` 的短二次乘积列上；
若全部落入，则应抽取低模二次 CRT/PDEC 缺陷。

新增 `docs/monograph/prime-matrix-bottom-deficit-pair-bound-hard-attack.md` 与
`experiments/prime_matrix_bottom_deficit_pair_bound_segmented_audit.py` 后，底部带容量界被修正：
平方型补洞 `(P-h/2)^2` 真实存在，所以上界应为 `|F_{P-h}|<=floor(h/2)`，不是
`floor((h-1)/2)`。分段审计把样本扩展到 `P=100003`，全部底部行有素数，修正后最小余量从
`51,93,245` 增长到 `4100` 量级。底部几何部分已闭合为精确分解，剩余接口应写成
`BottomPrimeWindow`：证明近平方长度 `P` 行窗口中的素数洞加高素对洞超过 `floor(h/2)`，
或失败进入 `SAE/PDEC/ColumnCRT`。

新增 `docs/monograph/prime-matrix-terminal-row-square-gap-hardpoint.md` 与
`experiments/prime_matrix_terminal_row_gap_audit.py` 后，圆柱路线的终端边界被单独物化：
第 `x=P-1` 行中所有 `q<P` 斜线都已完成，未完成补洞集为空；该行命题等价于
`p_-(P^2)>P^2-P`，即 `P^2` 前长度 `P` 的窗口含素数。样本 `P<=5000` 的 `668` 个奇素数无失败，
最坏 `P=3929` 的平方前间隙为 `98`。这说明完整闭合必须并行攻两个硬点：
`Incomplete-FillerBound` 处理 `x<P-1`，`TerminalSquareGap` 处理终端行；不能只靠“斜线未画完”
解释最后一行。

新增 `docs/terminal_sae_split_audit_p2000_20260505.md` 与
`docs/terminal_sae_cancellation_audit_p2000_20260505.md` 后，终端 SAE 支线的证据扩展到
`p<=2000`：302 个奇素数全部满足 `G_y(h)>T_y(h)`，`p>=7` 最小 margin 仍为 `1`；
抵消审计同样无未认证记录，最大 `omega_tail=3`，从 `p=11` 起实际双尾化，简单条件
`y^3>q^2` 的最后例外是 `p=31`。终端最小硬点因此保持为 `RCI/PDEC`：
证明无尾储备严格大于多尾碰撞超额，或把失败路由到持续端点/尾锚缺陷。

新增 `docs/monograph/prime-matrix-terminal-rci-boundary-split.md` 与
`experiments/prime_matrix_terminal_rci_boundary_split_audit.py` 后，终端 `RCI` 又剥离出一个可证明边界块：
当 `h=q` 时镜像区间为 `[1,q]`，若 `y^2>q`，低筛骨架只剩尾素数与新素数 `q`；尾素数单尾抵消，
`q` 给出唯一无尾储备，所以余量恒为 `1`。`p<=2000` 中 302 条记录有 295 条全局最小余量来自该
边界块。剥离后非底块最小余量随阈值增厚：`p>=101` 为 `4`、`p>=501` 为 `22`、`p>=1009`
为 `44`。当前终端硬点应更准确写成 `Nonbottom-RCI/PDEC`。

新增 `docs/monograph/prime-matrix-line-activation-cover-threshold.md` 与
`experiments/prime_matrix_line_activation_cover_audit.py` 后，用户的“斜线到 `q^2` 才真正连线”
被证明为平方激活引理：若 `q|n<q^2`，则该命中已有更小素因子，是 shadow hit，不是独立覆盖。
但审计也给出关键校正：`P=13` 时所有 `<P` 斜线第 `10` 行已激活，任意相位覆盖能力也第 `10`
行已经具备，而实际 `1..P` 行仍无零行，首零行为第 `169=P^2` 行。因此“未全激活”只能作为
必要结构，不能单独闭合行命题；当前最小接口应写为 `Early Phase-Lock`：早期小代表元相位
`(-(r-1)P mod q)_{q<P}` 不能同步实现任何完整覆盖证书。`P<=11` 全周期无零行的原因则是更低层的
任意相位覆盖能力本身不存在；`P=13` 是覆盖能力首次出现的阈值。

新增 `docs/monograph/prime-matrix-early-phase-lock-minrep-audit.md` 与
`experiments/prime_matrix_early_phase_lock_minrep_audit.py` 后，首零行行号因子结构也被校正：
`P=13` 为 `13^2`，但 `P=17` 为 `7*173`，`P=19,23` 为素数，`P=29` 为 `2*5*521`；
乘数 `x=row-1` 也没有稳定粗数律。可用不变量不是“行号必为大粗数”，而是
`MinRep Phase-Lock`：任意完整覆盖证书的 CRT 最小正代表必须大于 `P`。这与
`Early-Diagonal-Avoidance` 等价，但更贴近圆柱斜线相位同步模型。

新增 `docs/monograph/prime-matrix-diagonal-postsquare-rci-hardpoint.md` 与
`experiments/prime_matrix_diagonal_postsquare_rci_audit.py` 后，`x=P` 对角端点不再只是裸
`(P^2,P^2+P)` 短区间硬点；它也具有与 Terminal-SAE 同型的 RCI 抵消结构：
`G_y-T_y=no_tail_reserve-multi_tail_excess`。审计扩展到 `p<=10000`，1228 个奇素数全部正余量，
最大 `omega_tail=2`，`y^3<=p^2+p` 的最后例外为 `p=23`。当前端点硬点更新为
`PostSquare-RCI/PDEC`：证明无尾储备大于双尾碰撞，或把失败路由到固定端点相位 CRT 缺陷。

新增 `docs/monograph/prime-matrix-least-factor-activation-cutoff.md` 与
`experiments/prime_matrix_least_factor_activation_cutoff_audit.py` 后，平方激活被逐行精确化：
第 `x` 行只需独立考虑 `q<=floor(sqrt(xP+P-1))` 的最小因子斜线；所有更大 `q` 的命中都是
shadow hit。样本 `P=23,101,499,997,1999,5003` 中，用该截止筛出的残洞数与真实素数数逐行完全一致。
这给出目前最贴合圆柱几何的等价接口：当前已激活最小因子斜线不能覆盖全部列。

新增 `docs/monograph/prime-matrix-diagonal-postsquare-tail-collision-vanishing.md` 后，
`PostSquare-RCI` 的端点负项被消掉：`P>=23` 时 `y^3>P^2+P`，任一低筛骨架点至多含两个尾素因子；
但两个 `<P` 尾素数的乘积小于 `P^2`，不能落入 `(P^2,P^2+P)`。因此多尾碰撞超额为 `0`。
平方后端点剩余硬点更新为 `Tail-Perfect-Cover Exclusion`：排斥一尾项 `y<ell<P` 完美吃掉全部低筛骨架。

新增 `docs/monograph/prime-matrix-diagonal-postsquare-tail-cofactor-identity.md` 与
`experiments/prime_matrix_diagonal_postsquare_tail_cofactor_audit.py` 后，端点一尾项进一步被剥离：
若 `P>=23`，则 `P^2+k=ell*m` 中的互补因子必为素数，且 `P<m`，每条 `ell` 的候选区间长度至多
`3`。审计扩展到 `P<=100000`，复合 `y`-rough 互补因子只出现 `4` 次，最后在 `P=13`；
互补因子素性阈值最后失败在 `P=19`，offset 三曲线分布为
`{1:2382774,2:1224068,3:163279}`。因此当前端点最窄硬点应改写为
`Short Prime-Cofactor Perfect-Cover Exclusion`：长度至多 `3` 的互补素数窗口不能完美吃掉平方后
端点低筛骨架；等价地，三条倒数地板曲线
`floor(P^2/ell)+s (s=1,2,3)` 上的素-素命中不能覆盖全部低筛骨架。若失败，必须路由到
`PDEC/Tail-anchor` 短窗素数异常集中。

新增 `docs/monograph/prime-matrix-diagonal-postsquare-primepair-dimension-gap.md` 与
`experiments/prime_matrix_diagonal_postsquare_primepair_excess_audit.py` 后，端点硬点被压成两个显式
常数输入：`G(P)>=0.48 P/log P` 与 `B(P)<=1.50 P/log^2 P`。因为 `1.50/0.48=3.125<log(23)`，
这组常数若成立即可从 `P>=23` 直接闭合平方后端点。审计到 `P<=100000` 显示
`min G log P/P=0.4879618800870573`、`max B log^2 P/P=1.4688379348569027`，候选全在低骨架内且无重复覆盖。
当前最窄硬点因此更新为 `LDG-Lower + RFP-Upper`，或证明任一失败路由到 `PDEC/Tail-anchor`。

新增 `docs/monograph/prime-matrix-diagonal-postsquare-rfp-selberg-route.md` 后，`RFP-Upper` 被拆成
双曲窄带二维上筛常数包：`B(P)` 是
`R_P={(a,b): y<a<P, P<b, P^2<ab<P^2+P}` 中两个坐标同为素数的点数，原始体量
`X(P)≈P`，二维筛应给 `X(P)/log^2P`。面积审计 `p<=10000` 显示低范围最大
`X/P=1.053097` 在 `P=113`，但 `P>=2003` 后最大降为 `1.019811`；高点抽样到
`P=200003` 仍约 `1.001`。剩余工程义务为 `RFP-Area`、`RFP-Selberg` 和 `RFP-Defect`：
`23<=P<2003` 走有限证书、`P>=2003` 证明 `X(P)<=1.02P`，再证明主常数加误差 `<=1.50`，
或把超预算相位路由到 `PDEC/Tail-anchor`。

新增 `docs/monograph/prime-matrix-diagonal-postsquare-ldg-lower-pdec-route.md` 后，`LDG-Lower`
也被固定成常数/PDEC 接口：完整周期主项为
`P V(y)=P prod_{r<=y}(1-1/r)≈e^{-gamma}P/logP`，候选下界 `0.48P/logP` 允许约 `14%`
短窗亏损。审计到 `P<=100000` 显示 `min G logP/P=0.4879618800870573`，且
`G/(PV)` 从 `P>=23` 的 `0.7045` 提升到 `P>=50021` 的 `0.9216`。若该下界失败，失败必须是
固定端点相位低模骨架亏损 `LowSkeletonDeficit`，进入 `PDEC/SAE`。

新增 `experiments/prime_matrix_diagonal_postsquare_lowband_finite_certificate.py` 与
`docs/diagonal_postsquare_lowband_finite_certificate_p2003_20260505.md` 后，平方后端点低段已剥离：
`P<=2003` 的 `303` 个奇素数直接端点素数失败数为 `0`；`P>=23` 的 `296` 条维数差记录失败数为
`0`，最小 margin 为 `2`。因此后续 `LDG/RFP` 解析常数账本可从 `P>=2003` 起攻。

新增 `experiments/prime_matrix_diagonal_postsquare_area_carry_audit.py` 后，`RFP-Area` 被进一步
精确化为基线-进位分解：
`X(P)=P+floor(P/2)-1-2floor(P/e)+C(P)`。`P<=10000` 审计中
`X<=1.02P` 的最后失败是 `P=1873`；`P>=2003` 全部通过，最紧样本为
`P=2221`，`carry=569`、允许 `569.42`、余量 `0.42`。当前面积硬点更新为
`AreaCarryBound`：证明尾段二次剩余进位计数不过密，或把过密路由到
`HyperbolicDiscFailure/PDEC`。

新增 `experiments/prime_matrix_diagonal_postsquare_carry_phase_discrepancy_audit.py` 后，
`AreaCarryBound` 进一步拆成连续主量和二次相位偏差：进位条件为
`{h^2/a}>1-h/a`，故 `C(P)=W(P)+D(P)`，`W=sum h/a`。`P<=10000` 审计显示
最大正偏差 `D/sqrt(P)=1.109666`，最大绝对偏差 `1.256024`；最紧点 `P=2221`
满足 `allowance-W=46.115249`、`D=45.695249`、最终余量 `0.42`。因此面积硬点
可更新为 `CarryMain + CarryDiscrepancy`，后者失败即为 `HyperbolicDisc/PDEC`。

新增 `experiments/prime_matrix_diagonal_postsquare_carry_main_identity_audit.py` 后，`CarryMain`
已基本初等化：`allowance-W=P(1.02-(H_{P-1}-H_y))`，且
`H_{P-1}-H_y<=log((P-1)/y)<=log((P-1)/(P/e-1))`。审计到 `P<=100000` 显示
`P>=10007` 时去 floor 显式下界已有 `1.98352 sqrt(P)` 余量。因此面积尾段可再切成
`2003<=P<10007` 有限 carry 证书，以及 `P>=10007` 的 `CarryDiscrepancy` 目标：
证明 `D(P)<=1.98sqrt(P)`，或把更大正偏差路由到 `HyperbolicDisc/PDEC`。

新增 `docs/monograph/prime-matrix-diagonal-postsquare-carry-discrepancy-pdec-route.md` 后，
`CarryDiscrepancy` 先被形式化为纯双曲地板相位问题：若
`D(P)>1.98sqrt(P)`，Erdos-Turan 频率展开强制某个低频端点相位和异常。

新增 `docs/monograph/prime-matrix-diagonal-postsquare-carry-reciprocal-frequency.md` 与
`experiments/prime_matrix_diagonal_postsquare_carry_reciprocal_frequency_audit.py` 后，这一步又被压窄：
因为 `{P/a}=h/a` 且 `{P^2/a}={h^2/a}`，真正频率对象是
`sum_{y<a<P} e(rP^2/a)(1-e(rP/a))`，即 `RSE` 的 `ell=1, X=P^2, H=P, m~P`
端点倒数相位核。`10007<=P<=50000` 审计中最大 `D/sqrt(P)=1.285713`，64 频余误差在最大样本
为 `-0.082190sqrt(P)`。当前最小硬点因此更新为 `EndpointReciprocal-OSC` 或
`EndpointReciprocal-PDEC`：用 RSE-OSC / B-process 控制该端点倒数和，或把任何异常低频集中
抽取为 `HyperbolicDisc/PDEC` 证书。

新增 `docs/monograph/prime-matrix-diagonal-postsquare-endpoint-reciprocal-osc-hard-attack.md` 后，
该接口拆成 `ERO-Low + ERO-Tail + ERO-Edge`：低频必须保留有符号结构，因样本中绝对谐和预算
可到 `2.266653sqrt(P)`，而实际低频有符号量最大样本约 `1.367904sqrt(P)`。下一步应优先证明
端点有符号振荡界，不能退回粗绝对值估计。

新增 `experiments/prime_matrix_diagonal_postsquare_endpoint_bprocess_skeleton.py` 与
`docs/diagonal_postsquare_endpoint_bprocess_skeleton_r64_20260505.md` 后，`ERO-Low` 的 B-process
驻相骨架进一步明确：驻相相位为 `e(2P sqrt(rn))`，所有 `rn=s^2` 的平方共振项由端点因子
`1-e(sqrt(rn))` 精确消去。`R<=64` 中 `171` 个平方驻相项的原始预算为 `0.283225`，加权后为
`1.743e-15`。因此低频剩余是非平方根频率的有符号有限账本，若其仍异常，只能表现为
endpoint reciprocal PDEC。

新增 `experiments/prime_matrix_diagonal_postsquare_bprocess_model_audit.py`、
`experiments/prime_matrix_diagonal_postsquare_bprocess_envelope_scan.py` 与
`docs/monograph/prime-matrix-diagonal-postsquare-ero-low-bprocess-envelope.md` 后，`ERO-Low`
进一步压缩为有限非平方三角包络：20 个最大样本中 B-process 主项最优常数 `kappa=1/8`，
最大模型误差 `0.004077`；`10007<=P<=100000` 的 `8363` 个素数上，64 频包络无一超过
`1.55`，最大 `1.369773` at `P=36739`。尾核正贡献全局可达 `0.523830`，但此时核心仅
`0.362995`；当核心 `>=1.10` 时尾核正贡献最多 `0.198029`。最新最窄硬点因此修正为
`CoreKernel-Lock + CoreTail-AntiLock + Edge-Remainder`：不是分别证明核心和尾核都小，而是证明
核心小核高峰与尾核正堆积不能同步；任何同步失败都应抽取 endpoint PDEC/SAE 证书。

新增 `experiments/prime_matrix_square_row_wheel_rigidity_audit.py` 与
`docs/monograph/prime-matrix-square-row-wheel-rigidity.md` 后，用户提出的 `6/30/210` 轮结构已接入
平方前后端点主线：对任意平方自由轮 `W`，`P^2+k` 的轮幸存偏移为 `U_W-P^2`，`P^2-k`
的轮幸存偏移为 `P^2-U_W`，两者严格镜像；双侧同时幸存偏移数为
`prod_{\ell|W,\ell>2}(\ell-2)`，例如 `W=210` 为 `15`、`W=2310` 为 `135`。`P>=10007`
尾段中 `W=210` 单侧骨架至少约 `0.228P`，`W=2310` 至少约 `0.207P`。这把端点覆盖硬点改写为
`Wheel-Rigid Set Cover`：高素斜线必须在 `U_W±P^2` 的确定平移骨架上做 CRT 集合覆盖；
若核心轮骨架高峰与尾核正堆积同步，则应抽取 endpoint `PDEC/SAE/ColumnCRT` 缺陷。

新增 `docs/monograph/prime-matrix-wheel-promotion-invariance.md` 后，轮结构又获得一个严格不变量：
若把素数 `s<P` 从高素斜线层提升进轮底座 `W'=Ws`，最终幸存集合不变
`R_W^\pm(P)=R_{W'}^\pm(P)`。审计 `W=6,30,210,2310` 在多个端点样本上未覆盖偏移完全一致。
因此小模连乘的证明价值不是改变幸存集合，而是选择更刚性的 CRT 坐标系；当前接口应写为
`Promoted Wheel Set Cover -> PDEC/SAE/ColumnCRT`。

新增 `docs/monograph/prime-matrix-promoted-wheel-setcover-capacity.md` 后，高素斜线容量也被结构化：
`P^2±k=q m` 命中提升轮骨架当且仅当互补因子 `m mod W` 是单位类。把 `13` 从高素层提升进
`W=30030` 后，最终未覆盖集合不变，但最大单线由 `q=13` 转移到 `q=17`，如 `P=36739`
的 plus 侧从 `587` 降到 `416`。下一步硬点是
`Promoted-Wheel Capacity Dichotomy`：若提升后仍全覆盖，则中等 `q` 桶容量、重叠或单位类短窗
必有异常，并路由到 `PDEC/SAE/ColumnCRT`。

新增 `experiments/prime_matrix_promoted_wheel_unit_interval_envelope.py` 后，单条 `q` 线容量有了
审稿级确定上界：若互补因子区间长度为 `L_q`，则容量至多
`B_W(L_q)`；并由莫比乌斯反演有 `B_W(L)<=L*phi(W)/W+2^omega(W)`。审计显示
`W=510510,L=5000` 时真实 `B_W(L)=910`，密度期望 `902.63`。因此 q 线容量已经从概率估计
改成有限 CRT 包络；剩余硬点转为桶间协同和重叠异常的 `PDEC/SAE/ColumnCRT` 排斥。

新增 `docs/monograph/prime-matrix-promoted-wheel-forced-overlap-certificate.md` 与
`experiments/prime_matrix_promoted_wheel_forced_overlap_audit.py` 后，桶间重叠异常被进一步压成
强制二重交叉证书。令 `T=sum_q |A_q|`，`I2=sum_k binom(m_k,2)`，`M` 为单点剩余 q 标签上界，
则 `T-U>=2I2/M`；若 `T-ceil(2I2/M)<|S_W^\pm(P)|`，剩余高素斜线不可能盖满轮骨架。
`M` 由最小剩余素数连乘给出。样本 `W=9699690` 中
`P=36739, plus` 有 `S=6286,T=7363,I2=4151,M=6,forced_union_upper=5979`；
`P=99991, plus` 有 `S=17100,T=21271,I2=12968,M=6,forced_union_upper=16948`。
继续提升到 `W=223092870` 后最大单线转移到 `q=29`，强制重叠余量反而增大。
当前平方端点硬点升级为 `Promoted-Wheel Forced-Overlap Certificate`：证明 `T/I2/M`
三项确定不等式，或将失败路由到 `PDEC/SAE/ColumnCRT`。

进一步新增 `docs/monograph/prime-matrix-dynamic-promoted-rough-capacity.md` 与
`experiments/prime_matrix_dynamic_promoted_rough_capacity_audit.py` 后，固定提升轮路线升级为动态提升轮：
取 `Y=P^alpha`，把全部 `q<=Y` 提升进底座。若剩余高素总命中
`T_Y^\pm(P)<|S_Y^\pm(P)|`，则无需二重重叠即可排除全覆盖。选择
`alpha=0.43` 位于 `e^{-1}<alpha<1/2`，模型常数 `log(1/alpha)=0.843970<1`。
连续审计 `13<=P<=100000` 的 `9587` 个素数、plus/minus 共 `19174` 条记录中
`capacity_fail=0`，最小容量余量 `1`；高段 `P>=10007` 最小余量 `213`，最大
`T_Y/S_Y=0.871142`。当前最优主线应改写为 `DPRC(alpha=0.43)`：证明同权相对筛不等式
`T_Y<S_Y`，若聚合筛估计超预算则送入 `PDEC/SAE/ColumnCRT`。强制重叠证书降为等号/近等号备出口。

新增 `docs/monograph/prime-matrix-dprc-relative-sieve-margin.md` 与
`experiments/prime_matrix_dprc_relative_sieve_margin.py` 后，`DPRC` 又被拆成模型余量与相对筛偏差：
`S-T=S(1-H)-(T-HS)`，其中 `H=sum_{P^0.43<q<P}1/q`。审计到 `P<=100000` 显示
`P>=2003` 时 `min S(1-H)/sqrt(S)=3.579479`，而 `max max(0,T-HS)/sqrt(S)=2.468627`。
因此当前最小解析接口可写为：`P<2003` 有限证书；`P>=2003` 证明
`S(1-H)>3sqrt(S)` 与 `max(0,T-HS)<=3sqrt(S)`。后一项是新的最窄硬点：
动态粗骨架上的剩余高素同余类正偏差只有平方根级，失败路由到 `PDEC/SAE/ColumnCRT`。

新增 `docs/monograph/prime-matrix-dprc-bucket-energy-synchronization.md` 并升级
`experiments/prime_matrix_dprc_block_envelope_scan.py` 后，平方根偏差硬点进一步压成六个 beta 桶
正偏差向量的能量-同步性命题。设 `x_B=D_B^+/sqrt(S)`。目标
`D_+<=3sqrt(S)` 由 `||x||_1<=3` 推出；Cauchy 给出
`||x||_1<=sqrt(6)||x||_2`，因此 `||x||_2<=3/sqrt(6)=1.224744...` 即可闭合。
审计显示 `max ||x||_2=1.233496`，粗 Cauchy 只超 `0.008752`；但高正和段
`||x||_1>=2.4` 只有 2 条记录，且 `max ||x||_2=1.177635<6/5`。所以新的最窄硬点可写为：

```text
BES:
  若 ||x||_1 >= 12/5，则证明 ||x||_2 <= 6/5；
  否则 ||x||_1 < 12/5 已经远小于 3。
```

若 `BES` 失败，则同时存在多尺度正偏差同步与单桶尖峰，应强制产生
`PDEC/SAE/ColumnCRT` 缺陷。这比直接证明 `max(0,T-HS)<=3sqrt(S)` 更接近小模连乘同余刚性本身。
进一步的能量阈值审计显示，`||x||_2>3/sqrt(6)` 的记录只有 1 条，且
`||x||_1=2.078474<12/5`。因此也可用对偶接口攻：

```text
若 ||x||_2 > 3/sqrt(6)，则证明 ||x||_1 < 12/5；
否则 Cauchy 已给 ||x||_1<=3。
```

这个接口把危险交集精确成“高能量且高正和”的同步尖峰；样本中该交集为空。

新增 `docs/monograph/prime-matrix-dprc-bes-dual-large-sieve-route.md` 后，`BES` 失败形态进一步被
写成中心化核的对偶大筛问题：`D_B=<1_S,Psi_B>`，危险交集强制出现
`PointLoad / ShortWindow / LowPhase` 三类结构之一，分别路由到
`ColumnCRT / SAE / PDEC`。下一步不应再扩大统计表，而应分别证明这三类出口的阈值定理或提交证书。

新增 `docs/monograph/prime-matrix-dprc-bes-nearmiss-structure-audit.md` 与脚本
`experiments/prime_matrix_dprc_bes_nearmiss_structure_audit.py` 后，近危险样本的结构优先级更清楚：
10 个代表样本最大单点负载均为 `4`，短 q 子窗峰值仅约 `0.25~0.38sqrt(S)`；最稳定信号是
`mod30` 单位类内部偏斜，`all/mod30` 峰值最高 `0.902430sqrt(S)`，且所有顶峰对应的
`P^2±k mod 30` 都是单位类。因此下一最小硬点应写成 `WheelUnitPhaseBalance(W=30)`：
证明单位类内部偏斜不能与 BES 高能量高正和同步，或把同步峰物化为 `W-unit PDEC` 证书。

新增 `docs/monograph/prime-matrix-dprc-wheel-unit-phase-balance.md` 与脚本
`experiments/prime_matrix_dprc_wheel_unit_phase_balance_scan.py` 后，`W=30` 已做全范围扫描：
`P>=2003` 的 `18578` 条记录中，`BES` 两类危险交集计数均为 `0`；最大 `unit30 peak`
为 `1.076781sqrt(S)`，但该记录的 `BES L1=0.493686,L2=0.281040`。高 `BES L1` 段只有
2 条，最大 `unit30 peak=0.902430` 且 `L2<1.2`；唯一高 `BES L2` 记录有
`L1=2.078474<12/5`。因此 `mod30` 是真实第一层偏斜，但不同步；下一硬点升级为
`Layered WheelUnitPhaseBalance`：继续检查 `W=210/2310`，或证明所有有限提升层不同步后由高模大筛吸收。

新增 `experiments/prime_matrix_dprc_layered_wheel_phase_scan.py` 与
`docs/dprc_layered_wheel_phase_scan_p100000_20260506.md` 后，三层轮 `30/210/2310` 的全范围扫描显示：
`P>=10007` 时 `W=30` 最大单峰 `1.076781`，`W=210` 降为 `0.617936`，`W=2310` 降为
`0.293727`；高 `BES L1` 样本在三层中的最大单位峰分别为 `0.902430,0.331095,0.175276`。
这说明轮层提升会把单单位类偏斜分散到更多单位类；若某层不分散，则正好给出 `W-unit PDEC`。
新增 `prime-matrix-dprc-cylindrical-layered-wheel-clamp.md` 将其与圆柱斜线容量合并为
`LayeredClamp`：零行必须同时穿过几何容量、BES 能量同步和层叠轮相位同步三道门。

新增 `docs/monograph/prime-matrix-dprc-layered-wheel-fourier-energy-route.md` 后，层叠轮分支进一步
Fourier 化：对 `U_W` 上的单位类偏差向量 `E_W(a)`，若单类峰未稀释，则扣除平均项后由
Parseval 强制存在非平凡低模字符偏大，即 `W-unit PDEC`。注意全扫中
`max_peak*sqrt(phi(W))` 对 `30/210/2310` 约为 `3.0456,4.2812,6.4352`，不支持朴素均匀随机一刀切；
正确二分是“稀释则高模大筛吸收，未稀释则低模 Fourier/PDEC 显化”。

新增 `docs/monograph/prime-matrix-dprc-fourier-inheritance-classifier.md` 与
`experiments/prime_matrix_dprc_fourier_inheritance_classifier.py` 后，低模 Fourier 分支又被拆成
“旧层继承”和“新层显化”。对 `8` 条代表记录，`W=210` 的最强频率有 `6/8` 条需要新增因子
`7`，`W=2310` 的最强频率 `8/8` 都需要新增因子 `11`；同时 `danger intersection=0`。
这把用户提出的层叠同余刚性压成新的接口：

```text
Fourier Inheritance Clamp:
  若新增素因子层频率持续同步，则给出 new-layer W-unit PDEC；
  若每层新增频率都不持续同步，则低模相位不能支撑 BES 危险交集，
  剩余偏差只能走高模分散大筛。
```

该项仍是 `Reduction-closed + audit`，不是最终证明；下一步要么物化 `new-layer PDEC`
证书阈值，要么证明新增频率非同步时的高模分散大筛界。

新增 `docs/monograph/prime-matrix-dprc-newlayer-energy-dispersion.md` 与
`experiments/prime_matrix_dprc_newlayer_energy_scan.py` 后，继承分类被提升成整层能量恒等式。
对 `W=rW0`，`r|h` 的 Fourier 频率是旧层继承，`r∤h` 是新增素因子层。Parseval 给出
继承能量等于按 `mod W0` 折叠后的平方和，因此新增层能量可精确计算。全扫 `P<=100000`
且 `P>=10007` 的 `16726` 条记录显示：

```text
30 -> 210:
  new share min/avg/max = 0.580510 / 0.897118 / 0.997260
  max centered peak = 0.611625
  high L1/L2 max peak = 0.280206 / 0.271803

210 -> 2310:
  new share min/avg/max = 0.854837 / 0.926300 / 0.973218
  max centered peak = 0.292146
  high L1/L2 max peak = 0.170133 / 0.114485
```

因此新结论不是“新增层能量小”，而是“新增层能量大但高维分散”。`BES` 高压样本在
`W=2310` 的相位有效维数约 `27` 到 `55`，不像低维同步峰。下一最小硬点更新为
`NewLayer Dispersion Clamp`：证明 `BES` 危险交集若存在，则某个新增层必须低维集中；
低维集中给 `new-layer PDEC`，否则新增层高维分散由对偶大筛吸收。

新增 `docs/monograph/prime-matrix-pcolumn-anchor-wheel-field.md` 与
`experiments/prime_matrix_pcolumn_anchor_wheel_field_audit.py` 后，用户提出的“第 `P` 列也做层叠轮筛”
被严写为全行锚点场。令 `y=x+1,d=P-c`，则

```text
xP+c = Py-d，
第 P 列锚点 = Py。
```

对任意轮 `W`，

```text
S_W(P,y)={1<=d<P: Py-d mod W in U_W}
        = S_W(P,2)+P(y-2)  (mod W)。
```

审计 `P=101,499,997,2003,5003` 与 `W=30,210,2310,30030` 得全部
`shift_identity_failures=0`。这证明层面把“第一行斜线覆盖”和“第 `P` 列锚点筛”放进同一个
圆柱平移方程。需要注意：第 `P` 列本身全是 `P` 的倍数，不能直接给素数洞；它给的是锚残基
`Py mod W`。最薄样本如 `P=5003,W=30030` 仍有 `260` 个素数洞，说明当前主攻接口应写为

```text
PColumn Anchor-Wheel Field:
  若某个第一行轮骨架平移块被高素斜线完全覆盖，
  则触发高素容量超预算、new-layer PDEC、SAE 或 ColumnCRT。
```

这把平方端点 `P^2±k` 推广到任意行 `Py-d`，但仍是结构归约与审计，不是最终无条件证明。

新增 `docs/monograph/prime-matrix-pcolumn-anchor-dynamic-capacity.md` 后，第 `P` 列锚点场被提升到
动态轮 `Y=P^0.43`。定义

```text
S_Y(P,y)={1<=d<P:(Py-d,prod_{ell<=Y}ell)=1}
T_Y(P,y)=sum_{Y<q<P} #{d in S_Y(P,y): d≡Py mod q}。
```

严格蕴含已经闭合：若 `T_Y(P,y)<|S_Y(P,y)|`，则该行存在素数洞。原因是未命中的
`Py-d` 无 `<P` 素因子且不被 `P` 整除，而 `P<Py-d<P^2+P`，合成数必有最小素因子
`<P+1`。新增审计脚本升级为相对筛余量输出：

```text
S-T = S(1-H) - (T-HS),    H=sum_{Y<q<P}1/q。
```

样本 `P=101,499,997,2003,5003,10007,20011` 全部 `capacity_failure=0`、
`union_failure=0`。其中 `P=20011` 最紧行 `y=71` 有
`S=2596,T=2484,margin=112,max T/S=0.956857`，但仍有 `1366` 个素数洞；
相对筛窗口为 `max D+/sqrt=6.659539 < min model/sqrt=8.802969`。这暴露了新的硬点
`NearCutoff Anchor Spike`：全行版本的最紧容量行常由 cutoff 后第一批高素
`q≈P^0.43` 支撑，但这些高命中同时产生强重叠。当前最优目标更新为
`PColumn Dynamic Capacity`：证明所有 `2<=y<=P+1` 满足 `T_Y<S_Y`；若失败，则必须抽取
近截止锚峰低重叠同步、低模 `PDEC`、单窗 `SAE` 或第 `P` 列位移 `ColumnCRT`。

新增 `docs/monograph/prime-matrix-pcolumn-nearcutoff-fartail-cofactor.md` 与两个专项脚本后，
近截止硬点进一步分裂。`experiments/prime_matrix_pcolumn_nearcutoff_spike_audit.py`
显示最强 `T/S` 行的 top labels 虽然是 cutoff 后第一批高素，但相对正偏差主来源是远尾
`q>10Y`：`P=100003,y=147` 中 `q>10Y` 承担 `62.4867%` 命中和
`12.725422 sqrt(S)` 的正偏差。随后
`experiments/prime_matrix_pcolumn_far_tail_cofactor_audit.py` 证明并审计远尾恒等式：

```text
Py-d=qm, q>10Y, 1<=d<P
<=>
ceil((Py-P+1)/m)<=q<=floor((Py-1)/m),
q prime, q<P, m is Y-rough。
```

样本 `P=5003,10007,20011,50021,100003` 全部 `identity_delta=0`。top `m` 也位于 cutoff
后第一批 `Y`-rough 数，如 `P=100003` 的 `m=167,163,157,181`。因此当前硬点再压缩为
`NearCutoff-FarTail Split + FarTail-Cofactor Bound`：近截止 `q≈Y` 给最大单线，远尾
`q>10Y` 给主要正偏差；远尾偏差等价于 `Y`-rough 互补因子短素数区间总计数。若该计数超预算，
它必须进入 cofactor-anchor、`SAE`、`ColumnCRT` 或 `PDEC`，不能再视为无结构统计波动。

新增 `docs/monograph/prime-matrix-pcolumn-fartail-model-payment.md` 与
`experiments/prime_matrix_pcolumn_far_tail_model_bound.py`、
`experiments/prime_matrix_pcolumn_tail_payment_constant_scan.py` 后，远尾分支被进一步常数化。
设 `Model_tail=sum_m |I_m|/log(q_m^-)`。对
`P=5003,10007,20011,50021,100003,200003`，最强近截止行的
`actual/model` 介于 `0.993758` 与 `1.025423`，而闭合允许常数
`C_allow=(S-non_tail)/Model_tail` 介于 `1.107340` 与 `1.160000`。进一步对每个 `P`
扫描 top-16 风险行，取 `C_tail=1.05` 全部通过，失败数为 `0`；最紧样本
`P=20011,y=71` 仍有付款余量 `78.398`。当前最小硬点升级为
`FarTail-Model Bound(C_tail=1.05)`：证明远尾互补因子短素数区间总计数
`<=1.05 Model_tail`，或将任何超标 `m/y` 层送入 cofactor-anchor、`SAE/PDEC/ColumnCRT`。

用户进一步指出不应把全局闭合寄托在固定常数上。新增
`docs/monograph/prime-matrix-global-structural-closure-chain.md` 后，当前路线被重写为非固定常数版。
固定 `1.05` 只保留为审计仪表；正式对象改成自归一化允许量

```text
C_allow(P,y) = (|S_Y(P,y)| - T_{<=BY}(P,y)) / Model_{>BY}(P,y)。
```

若 `tail < C_allow*Model_tail`，容量直接闭合；若失败，则失败等价于互补因子短素数区间总超额
超过本行真实可付款余量。此时必须产生 `cofactor-anchor / SAE / PDEC / ColumnCRT`
之一，或进入 `TotalDescent-TM` 递归下降；若下降成功到 `p=2` 矛盾，若下降阻断则首阻断是
grid-fail seam 并回到 `SAE/PDEC/ColumnCRT`。当前全局硬点因此更新为
`Self-Normalized Tail Dichotomy + NonHit-Phase Descent + No-Cycle Defect Ledger`，而不是证明某个
固定常数永远有效。

新增 `docs/monograph/prime-matrix-self-normalized-tail-dichotomy.md` 与
`experiments/prime_matrix_global_structural_chain_audit.py` 后，上述路线进一步严格化。核心预算引理为：
若早期行是零行，则高标签对低素骨架的近端命中 `N_{<=BY}` 与远尾命中 `A_{>BY}` 必满足
`N_{<=BY}+A_{>BY}>=|S_Y|`，所以 `A_{>BY}>=C_allow(P,y)M_{>BY}`。这把“远尾付款常数”
改成行内自归一化必要条件。当前审计 `P=5003,10007,20011,50021,100003,200003` 的 top-16
风险行共 `96` 行全部 `capacity_closed`；`P=5003` 全行版本也确认最强风险行为
`y=41,S=741,T=695,margin=46`。集中峰诊断显示全样本 `max_m_share=0.050898`、
`max_band_share=0.333333`、`max_qmod30_share=0.150769`、`max_dmod30_share=0.160000`，
且到 `P=200003` 分别降至 `0.007967/0.164639/0.130234/0.130667`。下一硬点由固定常数界更新为：
证明任何自归一化远尾超额若不能被分散大筛吸收，就必须物化为
`cofactor-anchor/SAE/PDEC/ColumnCRT` 或进入 `TotalDescent-TM`。

进一步新增的精确身份为 `R-E_tail=|S_Y|-T_Y`，其中
`R=(C_allow-1)M_{>BY}`、`E_tail=A_{>BY}-M_{>BY}`。因此自归一化尾项缺口与斜线容量余量是同一量。
当前账本中最紧 `P=20011,y=71` 给出 `E_tail=34.759866,R=146.759866,R-E=112`。同时
`sum_m E_m^+/R` 最大可到 `1.110155`，说明单个 `m` 层过细；但
`sum_{dyadic m/y band}E_band^+/R` 最大只有 `0.248700`，提示下一条主攻应是带级 signed
cancellation：证明 `sum_band E_band^+<R`，或将失败带作为 `cofactor-anchor` 命名出口。
该判据已写成 `SN-2 BandPositive`：`A_{>BY}=M_{>BY}+sum_jE_j<=M_{>BY}+sum_jE_j^+`，
所以 `sum_jE_j^+<R` 直接排除零行；当前最小带级吸收余量为 `40.980801`。

新增 `docs/monograph/prime-matrix-sn2-iterative-defect-descent.md` 与
`experiments/prime_matrix_sn2_band_structure_audit.py` 后，`SN-2` 后续不再表述为数值逼近，而是势函数下降：
`Phi=(P,q-window length,-omega(W),unresolved_mass,descent_depth)`。从最小反例出发，每一步只能缩短
`q` 窗、提升模数、固定位移、下降素数层或减少未解释质量；无限重复分别变成 `SAE/PDEC/ColumnCRT/p=2`
或大筛对偶出口。当前正带结构审计中 `163` 个正带分成 `131` 个短窗候选和 `32` 个分散大筛候选，
分散候选最大单带责任占 `R` 不超过 `0.132524`。下一硬点明确为 `SN-3 DistributedBandLargeSieve`
及其对偶失败出口。

新增 `docs/monograph/prime-matrix-sn3-distributed-band-large-sieve-bridge.md` 与
`experiments/prime_matrix_sn3_distributed_band_projection_audit.py` 后，`SN-3` 又被压窄一层。
低模投影模型已修正为单位类条件主项：

```text
q mod W: W/phi(W) * #{q in I_m: q=a mod W}/log(q_m^-), a in U_W。
```

默认审计 `W=30,210` 仍有 `32` 个候选，按诊断阈值 `0.75` 分为
`24` 个 `TrueDistributedDLS`、`6` 个 `ColumnCRT-return`、`2` 个 `PDEC-return`；
`max E_J/R=0.132524`、`max E_J/sqrt(M_J)=1.310464`，中心化投影峰最大为 `1.018659`。因此原来的
`DistributedBandLargeSieve` 应拆成两步：先把中心化 `qmod/dmod` 峰接近整带超额的部分回流
`PDEC/ColumnCRT`，再对所有低维中心化峰都小的剩余带证明真正的 `DLS/KLS` 高频吸收。

新增 `docs/monograph/prime-matrix-sn3a-centered-lowmod-return-certificate.md` 与
`experiments/prime_matrix_sn3a_centered_lowmod_return_certificate.py` 后，第一步已经证书化：
若 `E_beta*>=theta E_J`，则 `E_J-E_beta*<=(1-theta)E_J`。当前 `theta=0.75` 的 `8`
个回流候选中，`6` 个为 `ColumnCRT-return`、`2` 个为 `PDEC-return`；总超额
`132.550671` 中低模峰吸收 `121.448880`，比例 `0.916245`，剩余正质量比例仅
`0.087421`。下一硬点因此变成排斥这些命名出口，和证明剩余 `TrueDistributedDLS` 高频吸收。

新增 `docs/monograph/prime-matrix-sn3b-true-distributed-residual-target.md` 与
`experiments/prime_matrix_sn3b_true_distributed_residual_audit.py` 后，SN3-B 的高频残余账本也已物化。
原分散正质量 `561.852711`，SN3-A 后有效未解释质量为 `440.889774`，剥离比例
`0.215293`。最紧行级责任为 `0.187188R`，发生在 `P=10007,y=75`，由两个真分散带叠加且无低模残余。
因此下一步最窄硬点是排斥同一行多真分散带的高频同步，或把它转成 `KLS/dispersion` 非零频率证书。

新增 `docs/monograph/prime-matrix-sn3c-multiband-sync-split.md` 与
`experiments/prime_matrix_sn3c_multiband_sync_audit.py` 后，多带同步被进一步三分：
`ShellOverlap=>SAE`、`LowModSync=>PDEC/ColumnCRT`、`KLS-Multishell=>高频输入`。当前只有
`3` 个多真分散带行、`3` 对带；其中 `2` 对为 `KLS-Multishell`，`1` 对为低模同步。最紧
`P=10007,y=75` 的两带 q 壳 `[1237,2444]` 与 `[4970,9500]` 相隔 `2525`，q-window 余弦为
`0`，最大低模余弦 `0.432620`，因此确认为真正多壳高频候选。

新增 `docs/monograph/prime-matrix-sn3d-kls-multishell-frequency-bridge.md` 与
`experiments/prime_matrix_sn3d_kls_multishell_frequency_audit.py` 后，KLS-Multishell 又通过
`d=Py-qm mod P` 的有限 Fourier 分裂为 `HighFrequencyColumn/PDEC` 或
`L2Flat CleanMultishellKLS`。当前两个 KLS 候选均非 L2-flat：`P=10007,y=75` 有
`|Rhat(49)|/E=1.374721`，`P=50021,y=128` 有 `|Rhat(119)|/E=2.056175`。因此样本剩余回流到高频
Column/PDEC 证书；全局剩余是排斥该高频出口或证明 clean KLS 输入。

新增 `docs/monograph/prime-matrix-sn3e-highfreq-bohrcap-no-cycle.md` 与
`experiments/prime_matrix_sn3e_highfreq_bohrcap_certificate.py` 后，高频出口进一步统一为
Bohr-cap 无循环：若非零频率大小为 `L`、变差为 `V`，则
`r_+(Bohr_+)+r_-(Bohr_-)>=max(0,(L-alpha V)/(1-alpha))`。持久帽进入
`PDEC/ColumnCRT`，孤立帽进入 `SAE/endpoint`，无帽则进入 `L2-flat CleanKLS`。当前两个样本在
`alpha=0` 时正帽分别捕获 `58.0008%` 与 `52.4712%` 的正残余质量。由此主链完成“无名逃逸闭合”，剩余是命名出口排斥或 clean KLS 输入。

新增 `docs/monograph/prime-matrix-unnamed-escape-closure-machine.md` 后，当前 SN 链条被合并为统一势函数
`Phi=(P,active_shell_count,q_window_length,-lowmod_rank,-frequency_rank,unresolved_mass,descent_depth)`。
每一步必须容量闭合、窗口缩短、低模/频率 rank 增加并形成命名缺陷、未解释质量下降、进入
CleanKLS，或由 TotalDescent 降低 `P`。因此最小反例不能无限无名逃逸；剩余审稿义务是排斥
`SAE/PDEC/ColumnCRT/Bohr-cap` 出口或证明 `CleanMultishellKLS/TotalDescent`。

新增 `docs/monograph/prime-matrix-named-exit-absorption-contract.md` 后，命名出口层也被规范为统一证书接口。
`Bohr-cap` 只允许吸收到 `PDEC/ColumnCRT/SAE/CleanKLS`，`EndpointSeam` 只允许吸收到
`PDEC/ColumnCRT/SAE`，`CofactorAnchor/TailAnchor` 只允许给尾锚证书或回流
`PDEC/ColumnCRT/SAE`，`TotalDescent` 只允许下降到 `p=2` 或产生首阻断 seam。审稿主线因此改写为：

```text
SN unnamed closure
=> NamedExit absorption
=> SAE-Cert / PDEC-Cert / ColumnCRT-Cert / CleanKLS / p=2 descent contradiction。
```

该更新完成的是“无第三类自由出口”的合同，不是终端证书排斥。下一优化优先级应固定为：

```text
优先级 A：PDEC 同一坏窗集合的 U_CRT<L_PDEC；
优先级 B：ColumnCRT 非零位移负载排斥或回流 PDEC/SAE；
优先级 C：SAE 孤窗 survivor/lift/higher-defect；
优先级 D：CleanMultishellKLS 或无缺陷 TotalDescent。
```

同一合同还补入统一缺陷向量引理：`ColumnCRT/Bohr-cap/EndpointSeam/W-unit/CofactorAnchor`
的持久分支都可写成有限签名群 `G` 上的零均值测试函数偏斜，因而给出 generalized PDEC
Fourier 下界；稀疏分支则是 SAE。于是终端主线可进一步压成：

```text
PersistentNamedDefect => generalized PDEC-Cert；
SparseNamedDefect     => SAE-Cert；
NoNamedDefect         => CleanKLS or TotalDescent。
```

新增 `docs/monograph/prime-matrix-pdec-dual-failure-absorption-contract.md` 后，`PDEC-Cert` 的失败
也不再是黑箱。若某个 `(h,zeta)` 方向无法证明 `U_CRT<L_PDEC`，则坏窗计数在 cap
`C_alpha={a:Re(zeta chi_h(a))>=alpha}` 中满足
`g(C_alpha)>=(U-alpha M)/(1-alpha)`。因此 PDEC 失败只能进入：

```text
persistent cap => refined PDEC / ColumnCRT；
sparse cap     => SAE；
口径不一致     => Multiplicity-Stitching；
no cap         => 该方向上界成立。
```

这把下一轮最小硬点从“证明所有 PDEC 上界”细化为：

```text
PDEC-Dual-Cert 或 DualCap-Absorption；
若出现 cap，则证明 cap 不能持久递归，或把它物化为更细 PDEC/ColumnCRT/SAE 证书。
```

新增 `docs/monograph/prime-matrix-pdec-cap-refinement-no-cycle.md` 后，cap 持久递归也被限定在有限层。
固定签名群内，cap 集合生成的 Boolean algebra 原子数每次真细化都会增加，最多 `|G|-1` 次；
终止后只能是 singleton `explicit PDEC/ColumnCRT`、局部平坦 `CleanKLS/dual bound`，或稀疏 `SAE`。
若必须提升签名群，则分支已经变成 `new-layer PDEC/ColumnCRT` 或高维分散 `CleanKLS`。
因此下一硬点不应再拆结构树，而应选择终端证书：

```text
explicit/refined PDEC；
ColumnCRT；
SAE；
CleanKLS；
new-layer PDEC。
```

新增 `docs/monograph/prime-matrix-newlayer-pdec-tower-entropy-contract.md` 后，`new-layer PDEC`
也被改写为塔熵二分。若无穷提升层持续给出新增相位偏斜，则相对熵/二次能量成本累积，
形成 finite/profinite `PDEC/ColumnCRT`；若熵成本可求和，则新增层偏斜趋零，进入
`CleanKLS/DLS`；若层间口径不一致，则进入 `Multiplicity/Stitching`。因此终端列表进一步收窄为：

```text
explicit/profinite PDEC；
ColumnCRT；
SAE；
CleanKLS/DLS；
Multiplicity-Stitching。
```

新增 `docs/monograph/prime-matrix-multiplicity-stitching-absorption-contract.md` 后，
`Multiplicity-Stitching` 从终端列表中删除。若重复项有加权对偶独立性，则进入 `weighted PDEC`；
若没有，则按正式坐标商掉，进入 `primitive/physical PDEC` 或 `CleanKLS`；若重复来自同一物理候选、
列位移、端点或尾锚跨层复用，则进入 `ColumnCRT/SAE/TailAnchor/CofactorAnchor`。新的终端列表为：

```text
explicit/profinite/weighted/primitive PDEC；
ColumnCRT；
SAE；
CleanKLS/DLS；
TailAnchor/CofactorAnchor。
```

新增 `docs/monograph/prime-matrix-tailanchor-cofactor-absorption-contract.md` 后，
`TailAnchor/CofactorAnchor` 也并回主出口。远尾互补因子反演 `Py-d=qm` 使锚签名成为
`m/y band, m mod Q, q mod Q, d mod Q/P`。持久锚进入 `cofactor/low-mod PDEC` 或
`ColumnCRT`，稀疏锚进入 `SAE-anchor`，无锚同步则进入 `CleanKLS/DLS` 或容量矛盾。
因此终端列表更新为：

```text
PDEC family: explicit/profinite/weighted/primitive/cofactor；
ColumnCRT；
SAE；
CleanKLS/DLS。
```

新增 `docs/monograph/prime-matrix-columncrt-displacement-pdec-absorption.md` 后，`ColumnCRT`
也被吸收到 `displacement PDEC/SAE-column`。列位移签名
`sigma_col=(ell,d_c mod ell)` 是有限签名；非零位移余类持久过载就是 displacement PDEC，
孤立过载是 SAE-column，不过载则成为 PDEC 对偶列约束行。终端列表变为：

```text
PDEC family: explicit/profinite/weighted/primitive/cofactor/displacement；
SAE family；
CleanKLS/DLS。
```

新增 `docs/monograph/prime-matrix-sae-local-certificate-reduction.md` 后，`SAE family`
被改写为 `LocalSurvivorCert` 族。每个孤窗必须给出候选集合、blocker 集合和未覆盖 witness，
或证明 blocker 覆盖失败会产生 low-mod/cofactor/displacement/endpoint PDEC、TotalDescent，
或更小支撑的 SAE。固定孤窗内下降有限；无限复现则变成 PDEC。终端列表变为：

```text
PDEC family；
LocalSurvivorCert family；
CleanKLS/DLS。
```

新增 `docs/monograph/prime-matrix-cleankls-dls-certificate-contract.md` 后，`CleanKLS/DLS`
也被证书化。clean 分支必须通过 K1--K7 admission，并提交内部大筛证书或明确外部
`KLS/DI/BFI` 输入；任一失败项回流 `PDEC/SAE/Multiplicity`。最终剩余不再是出口树，而是三类
验收对象：

```text
PDEC family certificates；
LocalSurvivorCert certificates；
CleanKLS/DLS certificates or explicit ExternalKLS input。
```
