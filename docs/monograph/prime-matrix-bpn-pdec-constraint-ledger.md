# BPN-PDEC 结构约束账本

**状态：** `constraint_atoms_formalized_for_dual_certificate`

本文把 `PDEC-Dual-Cert` 中的抽象约束

\[
Ag\le b,\qquad Eg=e,\qquad g(t)\ge0
\]

拆成可审稿的结构约束原子。目标不是直接证明 `BPN(P)`，而是明确下一层最窄硬点：

```text
边界零行诱导的坏窗相位计数 g
必须满足哪些线性约束；
这些约束是否足以推出 U_CRT<L_PDEC。
```

## 1. 变量

固定低模周期 `Q`。令

\[
g(t)=\#\{x\in S:\tau(x)=t\},\qquad t\bmod Q,
\]

其中 `S` 是同一低模缺陷块的 persistent 坏窗集合。

审稿时必须同时登记：

```text
Q；
|S|；
kappa；
||F||_2；
每个结构约束的来源、系数、界值。
```

## 2. 约束原子

### 2.1 Mass 约束

Persistent 分支给出

\[
\sum_t g(t)=|S|,\qquad |S|\ge \beta |X|.
\]

在具体证书中应把 `|S|` 作为等式；若只知道范围，则必须拆成上、下两个不等式。

### 2.2 Mirror 约束

CRT 镜像把行相位 `t` 送到某个显式 involution `\rho(t)`。若坏窗族继承两端帽镜像，
则可用等式或上界：

\[
g(t)-g(\rho(t))=0,
\]

或更弱的成对容量约束

\[
g(t)+g(\rho(t))\le B_{\rm mir}(t).
\]

第一种强约束只能在坏窗定义本身镜像不变时使用；否则只能使用第二种成对容量约束。

### 2.3 Column-balance 约束

列非零同余类均衡不能直接推出 `g` 均衡，但可给出列投影容量。若相位块 `C_j`
对应同一列投影，则可写成

\[
\sum_{t\in C_j}g(t)\le B_{\rm col}(j).
\]

界值 `B_col(j)` 必须来自列见证、非零同余类计数或已证列命题；不能由期望均匀性代替。

### 2.4 Tail-anchor 不可复用约束

若相位块 `A_a` 共享同一尾锚或大因子复用资源，则短窗不可复用给出

\[
\sum_{t\in A_a}g(t)\le B_{\rm tail}(a).
\]

该约束是 `PDEC` 中最有价值的非均匀约束：它不是全周期平均，而是来自大因子在短窗口内
不能重复解释多个洞的刚性。

### 2.5 Core-overlap 回流约束

固定核心高重叠若超过阈值，应回流到 `SAE` 或 low-mod core CRTDefect。因此留在
`PDEC-Dual-Cert` 的相位计数必须满足

\[
\sum_{t\in H_c}g(t)\le B_{\rm core}(c).
\]

若该约束失败，不能放宽；应输出 `higher-defect` 证书并送回最终出口。

### 2.6 Rankin low-mod spike 路由约束

正式走廊 Rankin 证书失败时，若有低模尖峰，则该颜色类不应继续留在 smooth-core 预算中，
而要登记为 low-mod core CRTDefect。留在 `PDEC` 对偶系统中的部分必须满足

\[
\sum_{t\in R_m}g(t)\le B_{\rm rankin}(m).
\]

这里 `R_m` 是低模尖峰相位块，`B_rankin(m)` 来自证书报告的允许尖峰阈值。

## 3. 对偶证书验收格式

对每个非零频率 `h` 和方向 `zeta`，目标向量为

\[
c_{h,\zeta}(t)=\Re\{\zeta e^{2\pi iht/Q}\}.
\]

一个对偶证书必须给出：

```text
非负不等式权重 lambda_i；
自由等式权重 mu_j；
逐相位余量 slack(t)>=0；
总上界 U_CRT。
```

并逐相位核验

\[
c_{h,\zeta}(t)\le
\sum_i\lambda_i A_i(t)+\sum_j\mu_j E_j(t).
\]

总上界为

\[
U_{\rm dual}=\sum_i\lambda_i b_i+\sum_j\mu_j e_j.
\]

若 `U_dual<=U_CRT<L_PDEC`，则该 `h,zeta` 方向被排除。

## 4. 现在真正要补的内容

当前下一层硬点已经非常窄：

```text
不是再发明新的刚性名称；
而是为 mirror / column / tail / core / Rankin 五类约束给出实际系数和界值，
再提交覆盖所有 h,zeta 的 PDEC-Dual-Cert。
```

若某个频率方向无法被对偶证书压住，则应输出该方向的 slack 失败相位；这些相位就是
下一轮 `SAE-Window` 或 `Rankin low-mod spike` 的具体攻击目标。

## 4A. 约束来源合法性规则

补充文档 `h4-pdec-constraint-source-lemmas.md` 已把第一批约束来源逐行定理化。正式
`PDEC-Dual-Cert` 中的每一行必须先通过以下分类：

```text
tautology: mass / nonnegativity；
capacity inheritance: S subset Z 后的 phase cap 或 block cap；
mirror closed: 坏窗族自身镜像闭合时的 equality；
mirror pair capacity: 未证明镜像闭合时的弱成对容量；
bucket capacity: 已有 Hall/CRT 容量定理或有限证书时的 low-hole bucket；
conditional routing: 违反该行会进入 SAE/Rankin/tail/H5 出口的剩余分支约束。
```

因此，全周期 CRT 均衡、有限样本相位表、或完整零行族镜像等式不能自动成为任意
persistent 坏窗子集的无条件约束。

补充文档 `h4-pdec-admissible-constraint-table.md` 已把上述规则落实成第一版准入矩阵。
准入等级为 `Tautology / FiniteCert / SymbolicReady / ConditionalRouting / NeedsProof /
Rejected`。下一步生成正式 `A,b,E,e` 时必须只取已准入行；`NeedsProof` 行只能作为
待攻目标，`Rejected` 行必须从证书输入中删除。

补充文档 `h4-pdec-column-cap-source-lemma.md` 已进一步处理 column cap 来源。列约束
只能通过三种方式进入 `A`：有限列投影容量、符号化列容量定理、或违反列预算即进入
ColumnRadius/ColumnCRT/Tail-anchor 出口的条件路由行。该文件证明了列见证位移非零刚性，
但尚未提交 `B_col(j)` 系数表。

补充文档 `h4-pdec-column-cap-coefficient-ledger.md` 已提交 V1 系数账本，登记了
`CC-FIN-*`、`CC-LHB-*` 与 `CC-COND-*` 三类行。当前状态是数值界值和条件出口已登记，
但多数行仍缺机器可读 `phase_block`，所以尚不能直接作为 `A,b,E,e` 输入。

补充证书 `h4-pdec-lhb-column-phase-blocks.json` 已把 `Q=2310`、`13<=p<=47` 的
LHB column rows 物化为 `45` 条机器行。三类空异常块 `AFFINE/NEGDELTA/UNBRIDGED`
均通过 `bound=0`；整洞集亏损与桥洞临界块保留为诊断支撑，尚需正式投影容量证明。

## 5. 第一批真实系数行

脚本 `experiments/prime_matrix_bpn_pdec_real_constraint_rows.py` 已开始从完整 CRT 周期枚举中
填入真实结构约束行。默认样本为 `P=23,Q=210`，输出：

```text
phase_cap_t:          g(t)<=C_t；
mirror_pair_cap:      g(t)+g(rho(t))<=C_t+C_rho(t)；
low_hole_bucket_m:    sum_{h_Q(t)>=m}g(t)<=B_m；
mass equality:        sum_t g(t)=Z_P；
conditional mirror:   g(t)-g(rho(t))=0。
```

这些行的性质不同：

- `phase_cap_t` 对任意真实零行子族安全；
- `mass equality` 只对完整零行族安全；
- `conditional mirror` 只对已证明镜像闭合的坏窗族安全；
- `low_hole_bucket_m` 目前是有限枚举压力账本，需进一步提升为 tail/core 容量定理。

因此第一批真实行已经填入系数与界值，但还没有完成无条件推广。

默认样本的关键读数是：

```text
P=23, Q=210；
真实零行数 3456；
非零 phase cap 数 44/210；
max phase cap = 324；
low-hole >=5 的 bucket bound = 0。
```

这说明低骨架剩余洞数达到 5 个以上时，样本中高层补洞完全失败。下一步应把该现象提升为
符号化容量不等式：

\[
\sum_{h_Q(t)\ge5}g(t)=0
\]

或更弱但可推广的上界，并把它接入 `PDEC-Dual-Cert`。

## 6. 高层补洞容量恒等式

补充文档 `prime-matrix-bpn-low-hole-bucket-capacity-theorem.md` 已证明精确恒等式：

```text
固定低相位 t mod Q；
低骨架洞集 H_Q(t)；
高层行变量 r=t+Qy；
每个洞 c 与高素数 ell 给出 y mod ell 的一个补洞残基；
completion_count(t) 等于该低相位下真实零行数。
```

脚本 `experiments/prime_matrix_bpn_low_hole_bucket_capacity.py` 已用该恒等式扫描
`P=13,17,19,23`。这一步把整周期枚举改写成高层 CRT 补洞容量问题；下一步唯一硬点是
把 `completion_count(t)=0` 证明为 Hall/CRT 不相容定理。

低范围扫描曾显示更窄的结构：

```text
max holes with completion = high prime count；
max single-prime cover on completion = 1。
```

但扩大到更大 `P` 后，单洞匹配不再是一般事实。当前正确硬点已校正为 Hall 型 set-cover
亏损：对某个洞子集 `W`，若

\[
|W|>\sum_{\ell\in R}\max_a |W\cap B_{\ell,a}(t)|,
\]

则该低相位不能被高层补完。最新扫描中，`Q=2310` 对 `P=13,17,19,23,29,31,37,43,47`
的全部 `completion_count=0` 相位都能找到 Hall 亏损证书。

更细地，按最小删洞数 `d=|H_Q(t)|-|W|` 分类后，当前证书只剩两类：
`P<=37` 全部为 `d=0`，`P=43,47` 只需 `d=0,1`。一洞删除相位由
桥洞机制认证：删去一个同时支撑两个高素数最大残基块的洞后，总容量下降 `2`。
因此 `PDEC-Dual-Cert` 的下一批真实约束行应优先写成两类：

```text
Delta(H_Q(t))>0；
若 Delta(H_Q(t))=0，则存在桥洞 c0 使 Delta(H_Q(t)\{c0})>0。
```

这比“存在某个 Hall 子集”更接近可符号化的结构定理。

进一步地，补洞残基满足列残基刚性：

```text
a_{ell,c,t}=a_{ell,c',t} <=> c=c' mod ell。
```

所以 `Delta(H_Q(t))` 只需要统计低洞列集合在高素数模数下的最大残基块。最新
`Q=2310` 审计中，所有临界 `Delta(H_Q(t))=0` 的 zero bucket 都有桥洞；
桥洞是 `13` 与 `19` 的唯一最大列残基块交点。下一批 `PDEC-Dual-Cert`
真实约束行应把该事实写成“低骨架列残基最大块交叉”定理，而不是保留为
高层 CRT 枚举现象。

扩展 `P=53,59,61` 审计显示：`P=53,61` 已无 `Q=2310` low-hole zero bucket；
`P=59` 仅剩 8 个，且全部为 `Delta(H_Q(t))>0`。因此真实约束行还应加入
“转折后 zero bucket 消失或整洞集直接亏损”的二分出口。

贪心补洞审计进一步把“消失”改写为构造性覆盖：从 `P=61` 到 `P=109`，
每个低相位的 `H_Q(t)` 都能由互异高素数的列残基块逐步覆盖。该证书一旦符号化，
即可直接给出 `completion_count(t)>0`，无需完整 DP 计数。

最新增益账本给出更适合接入对偶证书的形式。若覆盖使用 `s(t)` 个高素数列残基块，
重复增益为 `D(t)=|H_Q(t)|-s(t)`，则

```text
D(t) >= |H_Q(t)|-|R|
```

就是高层可补完的充分条件。真实约束行可把 `13,17,19,23,...` 的列残基碰撞写成
该重复增益下界，而不是保留为贪心算法日志。

固定升序碰撞梯审计进一步去掉了动态贪心的选择自由。对 `Q=2310`，固定按
`13,17,19,23,...` 使用高素数，并在每一步只取当前未覆盖洞中最大的列残基块，得到：

```text
P=53 fixed-ladder fail = 44；
P=59 fixed-ladder fail = 36；
P>=61, P<=149 fixed-ladder fail = 0。
```

因此 `PDEC-Dual-Cert` 中的 low-hole 真实约束行可升级为：

```text
低范围 P<61：整洞集亏损、桥洞临界、精确 DP 临界三类证书闭合；
转折后 P>=61：固定升序高素数碰撞梯满足重复增益下界。
```

这不是终局证明；它把剩余符号化义务精确化为 `LHB-7`：
证明固定梯的累计重复增益始终不小于 `|H_Q(t)|-|R|`。

为了避免把“最大块选择”继续当算法黑箱，主定理稿还给出碰撞能量下界。对残集 `S`
定义 `E_ell(S)=sum_a binom(|S∩(a mod ell)|,2)`，固定梯在 `ell` 下的单步增益满足

```text
g_ell(S)-1 >= 2 E_ell(S)/|S|。
```

所以 `LHB-7` 的下一步真实约束行可写成累计能量不等式，而不是写成程序运行成功：

```text
sum_j 2 E_{ell_j}(H_{j-1})/|H_{j-1}| >= |H_Q(t)|-|R|。
```

另一个更保守但更通用的真实约束行是鸽巢尾段判据。令 `Hmax(P)` 为长度 `P-1`
的任意 `Q=2310` 连续残基段内最多的 `Q`-互素残基数，并令

```text
U_0=Hmax(P),  U_j=U_{j-1}-ceil(U_{j-1}/ell_j)。
```

若 `U_j=0`，则不需要任何低洞结构，固定梯也覆盖任意同大小洞集。审计到
`P<=100000` 显示该纯鸽巢出口从 `P=107` 起稳定闭合，失败只剩
`61,67,71,73,79,83,89,97,101,103`。因此 `PDEC` 的 low-hole 行可进一步拆成
尾段鸽巢闭合与十个素数的窄带碰撞能量闭合。

更适合写入正式证明的版本是 `P/5` 分割：先用 `ell<=floor(P/5)` 的高素数把残量降为
`V(P)`，再用区间 `(P/5,P)` 中的高素数逐个删除剩余洞。充分条件是

```text
V(P) <= pi(P-1)-pi(floor(P/5))。
```

审计显示该判据在 `P>=107, P<=100000` 内无失败。正式稿中只需把 `V(P)` 用
`Hmax(P) * product_{13<=ell<=P/5}(1-1/ell)` 上界，再接显式 Mertens 乘积和
素数计数区间下界。但该连续乘积上界在小尾段偏保守；最新审计显示最后失败为
`P=229`，从 `P=233` 起扫描无失败。因此正式账本应拆成：

```text
107<=P<=229：精确 P/5 分割递推有限证书；
P>=233：连续乘积 + 显式 Mertens/prime-count 常数证明。
```

常数审计进一步给出保守切分：`Hmax(P)<=16(P-1)/77+5`，配合
`prod_{p<=x}(1-1/p)<=e^{-gamma}(1.03)/log x`、`pi(x)>=x/log x`、
`pi(x)<=1.25506x/log x` 后，连续乘积不等式从 `P>=13208` 起自动闭合。
这些常数已在 `external-theorem-index.md` 中固定到 Rosser--Schoenfeld 1962：
Corollary 1 的 `(3.5),(3.6)` 给出 `pi` 上下界，Theorem 7 的 `(3.26)` 给出
Mertens 乘积上界；`P>=13208` 给出 `floor(P/5)>=2641`，足以覆盖 Mertens
放宽常数 `1.03` 的适用范围。
所以正式 `PDEC` 账本可登记为：

```text
107<=P<=229：精确分割递推有限证书；
233<=P<=13207：精确连续乘积有限证书；
P>=13208：显式常数包解析闭合。
```

有限证书已经落地为 `prime-matrix-bpn-lhb-tail-finite-certificate.md`：

```text
107<=P<=229：23 个素数行，失败 0，最小余量 0；
233<=P<=13207：1520 个素数行，失败 0，最小浮点余量约 0.5347204。
```

第二段验收使用整数交叉乘法 `R(P)B_y-Hmax(P)A_y>0`，不依赖浮点判定。
因此 `PDEC` 的 low-hole 尾段有限部分已经具备可复核证书；剩余无限段只需引用
显式 Mertens/prime-count 常数包。

窄带证书也已落地为 `prime-matrix-bpn-lhb-narrow-band-collision-certificate.md`：

```text
P=61,67,71,73,79,83,89,97,101,103；
总相位数 23100；
失败 0；
最小碰撞余量序列 0,0,0,1,1,2,2,2,2,3。
```

低范围最终证书 `prime-matrix-bpn-lhb-low-range-final-certificate.md` 又补齐
`13<=P<61`：`15414` 个 zero bucket 全部闭合，其中 `15282` 个整洞集亏损、
`108` 个桥洞临界、`24` 个 `P=41` 精确 DP 临界。该证书修正了旧的“全为整洞集
亏损或桥洞交叉”表述，并把低范围义务从主线移除。

因此 `PDEC` 的 low-hole 真实约束行可把 `P<61`、`61<=P<=103` 和尾段有限部分
全部标为证书已通过。剩余 low-hole 义务只保留 `P>=13208` 显式常数包的引用核验。
