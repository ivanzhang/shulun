# 未闭合硬项逐项攻坚路线图

本文承接 `docs/monograph/pre-external-referee-remaining-obligations.md` 的 H1--H10 清单。目标不是把尚未证明的深命题改写成已证，而是为每个未闭合接口给出：

1. 精确证明目标；
2. 可用刚性与外部工具；
3. 最小补正动作；
4. 可行性评级；
5. 若失败时必须采用的诚实状态。

可行性评级：

| 等级 | 含义 |
|---|---|
| A | 文稿/证书工程，可直接完成 |
| B | 现有框架内可攻，需补常数或形式化 |
| C | 需要新的非平凡定理，但目标已精确 |
| D | 等价或接近重大开放问题，不应承诺短期闭合 |

## 0. 总体优先级

| 优先级 | 项目 | 理由 |
|---|---|---|
| P0 | H1/H3/H7/H10 | 主要是定理化、引用适配、证书复现、状态工程；可立即提升外审可读性 |
| P1 | H4/H5 | Prime Matrix 最有希望继续推进；接口已压缩为 PDEC/SAE/Rankin 与 RRD/OSPC 常数账本 |
| P2 | H2 | Structured-EHPD/RHI 是行列终局核心，需要新的统一不等式或完整 D 组排斥 |
| P3 | H6/H8 | 二点筛终局会触及固定差素数对强后果，必须严防隐藏下界 |
| P4 | H9 | RH controlled exits 属于 RH 终局验证，不可由类比或实验完成 |

## 1. H1：Prime Matrix A/B 入口归约

### 1.1 精确目标

把“全合数行/列反例”无损导入 Structured-EHPD：

\[
\text{full-composite row/column}
\Rightarrow
\text{small-factor locks}+\text{tail anchors}+\text{Structured-EHPD}.
\]

### 1.2 当前可用材料

- `docs/row-column-reduction-formal-appendix.md`
- `docs/monograph/key-proof-chain-optimization-audit.md`
- `docs/monograph/pre-external-referee-remaining-obligations.md`

### 1.3 补正动作

1. 把 A/B 入口拆为 4 个正文附录引理：
   - Matrix coordinate and excluded column;
   - small-factor lock peeling;
   - large-factor non-reuse;
   - tail-anchor/source-deleting reduction.
2. 对每个剥离步骤给出集合分解式，避免“解释层重叠”。
3. 明确 Tail-log4 是输入还是已证引理。

### 1.3A 本轮进展

新增 `docs/monograph/prime-matrix-ab-entrance-theorem-list.md`。该清单把 A/B 入口整理为 `AB1--AB6`、`Theorem A`、`Theorem B` 与 `Corollary AB`，并固定剥离优先级、小因子/45度锁定/尾部锚/主体双粗层的不重不漏规则，以及 `ab-to-d-interface-match.md` 的五项 D 标准形式匹配。主稿中的 A/B reduction 已改为 `Reduction-closed Statement`。

### 1.4 可行性

评级：A/B，作者侧入口定理化已完成。
这只得到入口闭合，不能推出行列命题；终局仍转入 H2/H4/H5。

## 2. H2：Structured-EHPD / D 组终局排斥

### 2.1 精确目标

证明 Structured-EHPD 不存在，或用更短的 RHI 不等式替代：

\[
G_Y(I)=\{n\in I:(n,\prod_{q\le Y}q)=1\},
\]
\[
B_Y(I):=\sum_{Y<p\le P}\#\{n\in G_Y(I):p\mid n\}<|G_Y(I)|.
\tag{RHI}
\]

若 RHI 对反例窗口成立，则大素数补洞能力不足，行/列反例被排除。

### 2.2 关键数学分解

RHI 可拆成：

| 子目标 | 形式 | 风险 |
|---|---|---|
| PM-R1 | `|G_Y(I)|` 的短窗口粗数下界 | 普通短区间筛余下界不自动成立 |
| PM-R2A | `Y<p<=P/Y` 可筛段大素命中上界 | 需同一筛权 convention |
| PM-R2B | `P/Y<p<=P` 尾段锚定上界 | 真正硬点，需 PTA/RSE/RRD/OSPC |

模型余量要求取 `Y=P^alpha` 且

\[
e^{-1}<\alpha<1/2.
\]

### 2.3 可用刚性

1. 广义斜率锁：`docs/monograph/generalized-slope-locks-and-rough-hole-limits.md`
2. PTA/RSE 链：`docs/monograph/pta-gsl-hard-attack.md`
3. RRD/OSPC 账本：`docs/monograph/rse-rrd-ospc-margin-ledger.md`
4. 低模投影二分：`docs/monograph/rse-rrd-low-projection-dichotomy.md`

### 2.4 攻坚路线

路线 A：直接 D 组排斥。

```text
D-OMR + D-CGTP + D-LSMP + D-FCT/NRC
=> Structured-EHPD impossible
```

需要把每个 D 子接口的常数、量词和出口写成可审查定理。

路线 B：RHI 替代。

```text
GSL deletes q<=Y
=> PM-R1 lower rough mass
=> PM-R2 large-prime incidence upper bound
=> RHI
=> no full row/column cover
```

当前更建议路线 B，因为它把大量局部刚性统一成一个总命中不等式。

### 2.5 可行性

评级：C。
目标已经清楚，但 `PM-R2B/RSE/RRD/OSPC` 仍需新的定量证明。不能用 CRT 完整周期均衡或实验扫描替代短窗口大因子命中上界。

## 3. H3：BPN-LHB 子模块

### 3.1 精确目标

证明 low-hole bucket 接口在五段范围内闭合：

```text
13<=P<61
61<=P<=103
107<=P<=229
233<=P<=13207
P>=13208
```

### 3.2 当前状态

该子模块已达到有限证书/显式外部定理版闭合。剩余主要是外审复现工程。

### 3.3 补正动作

1. 为每个证书写一行复现命令、输入文件、输出判定。
2. 给 `RS1962` 写独立定理模板：
   - `pi(x)>x/log x`;
   - `pi(x)<1.25506x/log x`;
   - Mertens product upper bound。
3. 统一 `floor(P/5)`，避免 `P/5` 取整歧义。
4. 在主稿明确：BPN-LHB 是子模块，不是整条 PM 终局。

### 3.3A 本轮进展

新增 `docs/monograph/prime-matrix-bpn-lhb-certificate-reproduction-ledger.md`。该账本列出四个生成脚本、八个输出文件、五段范围、验收标准和临时目录字节级复现命令。本轮已执行复现核查，低范围、窄带、尾段有限、显式尾段四组 JSON/Markdown 均与仓库内文件一致。

### 3.4 可行性

评级：A，复现账本已完成。
剩余只是在最终主稿中把 RS1962 模板作为正式外部定理环境排版；BPN-LHB 子模块本身仍保持“外部定理版闭合”。

## 4. H4：PDEC / SAE / Rankin 最终出口

### 4.1 精确目标

闭合 BPN-BK 的最终出口三分：

\[
\text{BPN-BK bad window}
\Rightarrow
\text{PDEC}\ \vee\ \text{SAE}\ \vee\ \text{Rankin-budget failure}.
\]

并逐项排除。

### 4.2 PDEC exclusion

目标：

\[
U_{\mathrm{CRT}}<L_{\mathrm{PDEC}}
\]

其中 `U_CRT` 是同一坏窗指示函数的非零 Fourier/CRT 上界。

补正动作：

1. 完成结构约束矩阵 `A,b,E,e` 的来源证明；
2. 对每条约束标注来自 mirror、column、tail-anchor、core-overlap 或 Rankin routing；
3. 给出对偶证书 `lambda,mu`，证明所有非零频率被主控；
4. 若出现大非零频，严格导入 persistent endpoint CRTDefect。

可行性：B/C。
证书格式已经清楚，难点是无限族约束的结构来源证明。

### 4.2A 本轮进展

新增 `docs/monograph/h4-pdec-certificate-template.md`。该模板把 `PDEC exclusion`
固定为可提交证书包：

```text
输入：Q, X, tau, S, g, F, kappa, ||F||_2；
下界：L_PDEC=kappa |S|/(sqrt(Q-1)||F||_2)；
上界：由 A g<=b, E g=e 的结构约束推出 U_CRT；
验收：U_CRT<L_PDEC。
```

模板同时规定了两种合法提交形式：

```text
PDEC-Explicit-Cert：有限坏窗相位计数向量的精确 Fourier 审计；
PDEC-Dual-Cert：覆盖无限族的线性对偶主控证书。
```

该进展不排除 `PDEC`；它把 H4 persistent 分支的最终义务压缩为“逐条证明约束来源、
覆盖全部频率方向、核验严格余量”的三项可审稿任务。

### 4.2B 本轮进展：约束来源引理

新增 `docs/monograph/h4-pdec-constraint-source-lemmas.md`。该文件把 `A g<=b, E g=e`
中第一批可合法进入对偶证书的约束行逐条定理化：

```text
H4-PDEC-S1：mass 与非负性；
H4-PDEC-S2：S subset Z 时的 phase/block capacity；
H4-PDEC-S3：mirror equality 与 mirror-pair capacity 的区分；
H4-PDEC-S4：low-hole bucket capacity 的继承规则；
H4-PDEC-S5：出口路由后的 conditional row。
```

该进展闭合的是“约束行合法性规则”，不是 `U_CRT<L_PDEC` 本身。下一步需要把
`prime-matrix-bpn-pdec-constraint-ledger.md` 的每一类原子标成
`tautology / finite certificate / symbolic capacity theorem / conditional routing / not yet admissible`，
再生成正式 `A,b,E,e` 表。

### 4.2C 本轮进展：约束准入表

新增 `docs/monograph/h4-pdec-admissible-constraint-table.md`。该表把 PDEC 候选约束行
逐项分为：

```text
Tautology；
FiniteCert；
SymbolicReady；
ConditionalRouting；
NeedsProof；
Rejected。
```

当前可无争议进入证书的是非负性、质量行、已证明 `S subset Z` 后的 phase/block cap、
有限范围证书行，以及带出口元数据的 conditional routing 行。当前明确不能进入的是：

```text
完整 CRT 周期均衡直接推出坏窗子集均衡；
有限样本相位表直接推广到全体 P；
未证明 m(S)=S 时使用 mirror equality。
```

因此 H4-PDEC 下一步从“准入规则”推进到“正式系数源”：column cap、low-hole bucket
符号化、tail/core/Rankin/H5 条件路由元数据。

### 4.2D 本轮进展：column cap 来源

新增 `docs/monograph/h4-pdec-column-cap-source-lemma.md`。该文件把 column cap 的合法来源
固定为三类：

```text
有限列投影容量；
符号化列容量定理；
违反列预算即进入 ColumnRadius/ColumnCRT/Tail-anchor 的条件路由行。
```

它严写了列见证位移非零刚性：若坏行点 `Hq+c` 被旧标签 `ell` 覆盖，而同列素数见证
`r_c q+c` 不等于 `ell`，则 `r_c-H` 不能为 `0 mod ell`。这给出列见证能进入
PDEC 约束场的真实通道。当前仍未完成的是 `B_col(j)` 系数账本和完整 ColumnDefect
路由证书。

### 4.2E 本轮进展：column cap 系数账本 V1

新增 `docs/monograph/h4-pdec-column-cap-coefficient-ledger.md`。该账本登记三类 column cap
系数源：

```text
CC-FIN-*：q<=1000 或 p<=1000 的有限列见证/RCI-CDB 摘要界值；
CC-LHB-*：Q=2310 的 LHB 列残基刚性有限界值；
CC-COND-*：ColumnRadius/ColumnCRT/Tail-anchor 条件路由模板。
```

账本明确当前还不是最终 `A,b,E,e`：有限审计多数只给摘要常数，尚未输出相位块
`C_j=[t_1,...,t_k]`。下一步最小工程任务是优先把 `Q=2310` 的 LHB column rows
物化为机器可读 `phase_block + bound + source_hash`。

### 4.2F 本轮进展：Q=2310 相位块物化

新增脚本 `experiments/prime_matrix_bpn_lhb_column_phase_blocks.py`，并生成：

```text
docs/monograph/h4-pdec-lhb-column-phase-blocks.json；
docs/monograph/h4-pdec-lhb-column-phase-blocks.md。
```

结果覆盖 `Q=2310` 与 `p=13,17,19,23,29,31,37,43,47`，共 `45` 条机器行。
其中 `AFFINE`、`NEGDELTA`、`UNBRIDGED` 三类空异常块均满足 `phase_block=[]`、
`bound=0`，可作为有限空异常块 `A` 行。`WHOLEDEF` 与 `BRIDGED` 行已输出支撑相位，
但仍需证明正式坏窗集合投影关系，暂不升级为最终容量行。

### 4.2G 本轮进展：支撑到容量转移条件

新增 `docs/monograph/h4-pdec-lhb-support-to-capacity-transfer.md`。该文件严写：

```text
phase_block support != capacity bound for g(t)。
```

`WHOLEDEF/BRIDGED` 的 `bound=phase_block_size` 只有在相位指示型证书中才可直接使用；
对 persistent 计数向量，必须补充 `g(t)<=M(t)` 的多重度界，或证明 `S subset Z_LHB`
并计算 `Z_LHB` 在相位块上的投影容量。下一步最小硬点因此变为 `T3-multiplicity`
或 `T4-allowed-set`，其中优先推荐 `T3` 与既有 `phase_cap_t` 合并。

### 4.2H 本轮进展：T3 多重度容量路线

新增 `docs/monograph/h4-pdec-lhb-multiplicity-cap-route.md`。该文件把
`T3-multiplicity` 从一句“补多重度界”严写为可审计合同：

```text
输入同一 (p,Q,S,tau) 下的 M(t)；
证明 g(t)<=M(t)；
对每个相位块 C 输出 bound=sum_{t in C}M(t)。
```

合法来源被限定为有限全集投影、资源不可复用单射、以及排除命名出口后的条件路由上界。
因此当时 `WHOLEDEF/BRIDGED` 的剩余硬点进一步收窄为：生成并证明 `Q=2310` 的 `M(t)`，
而不是继续争论 `phase_block_size` 是否可作容量。

### 4.2I 本轮进展：Q=2310 `M(t)` 有限证书

新增脚本 `experiments/prime_matrix_bpn_lhb_multiplicity_cap_certificate.py`，并生成：

```text
docs/monograph/h4-pdec-lhb-multiplicity-cap-certificate.json；
docs/monograph/h4-pdec-lhb-multiplicity-cap-certificate.md。
```

证书取 `M(t)` 为高层 CRT 补洞完成数 `C_P(t;Q)`。对
`P=13,17,19,23,29,31,37,43,47`，`WHOLEDEF/BRIDGED` 支撑相位块全部满足
`sum_{t in C}M(t)=0`。这把 LHB allowed-set 分支中的诊断支撑行升级为 `bound=0`
容量行。

审稿边界：该升级依赖 `S subset Z_LHB(p,Q)`。当前全局 PDEC 的最小硬点已从
“生成 `M(t)`”变为“证明当前正式坏窗集合接入 LHB allowed-set，或失败回流到命名出口”。

### 4.2J 本轮进展：LHB 型坏窗接入

新增 `docs/monograph/h4-pdec-lhb-attachment-lemma.md`。该文件定义
`Z_LHB(p,Q)` 为高层 CRT 补洞完成集合，并证明：

```text
若 PDEC 坏窗是同一 (p,Q) 下的一整行 LHB 型全覆盖窗口，
则 S subset Z_LHB(p,Q)。
```

于是 `WHOLEDEF/BRIDGED` 的 `bound=0` 行已经可用于 LHB 型分支。当前全局最小硬点
进一步变为坏窗分类：证明正式 PDEC 抽取出的坏窗要么满足 LHB 型三条件，要么因坐标、
低骨架、高标签或混合口径失败而进入 `SAE / ColumnCRT / ColumnRadius / TailAnchor / Rankin`
等命名出口。

### 4.2K 本轮进展：PDEC 坏窗分类

新增 `docs/monograph/h4-pdec-bad-window-classification-lemma.md`。该文件使用已有
`UPS-1`、`H4-PDEC-S5`、`H4-PDEC-COL3`、尾锚二分和 Rankin 接入规则，证明非空命名
低模坏窗满足三分支：

```text
SAE；
LHB-PDEC；
Routed-PDEC。
```

在执行同口径拆分并排除 `SAE/ColumnCRT/ColumnRadius/TailAnchor/Rankin` 出口的剩余分支中，
所有 persistent 坏窗都是 LHB 型，因此可以接入 `Z_LHB` 与 `M(t)` 的 `bound=0` 容量行。
审稿边界保持不变：这些出口尚未被排除，PDEC 最终对偶主控也尚未提交。

### 4.2L 本轮进展：同口径拆分

新增 `docs/monograph/h4-pdec-homogeneous-splitting-lemma.md`。该文件证明口径混合
不是新的数学出口：任何混合坏窗集合必须按

```text
theta=(Q,tau,F,kappa,p,window-shape)
```

无损拆成同口径子族，然后对每个非空子族单独应用 `UPS-1` 与坏窗分类。若要从全局混合
密度推出同口径 persistent 子族，还需额外阈值账本；否则逐子族进入 `PDEC/SAE` 即可。
当前剩余数学出口因此更新为 `SAE/ColumnCRT/ColumnRadius/TailAnchor/Rankin`，不再包含
口径混合作为独立出口。

### 4.2M 本轮进展：ColumnDefect 路由合同

新增 `docs/monograph/h4-pdec-column-defect-routing-contract.md`。该文件把
`ColumnRadiusDefect` 与 `ColumnCRTDefect` 从口头出口改成可审稿的条件证书对象：

```text
ColumnRadiusDefect：
  半径阈值 D_0、列见证选择器、相位兼容权重 W_D(t)，违反 R_D(g)<=0 即回流出口；

ColumnCRTDefect：
  标签 ell、非零位移余类 a、阈值 L_D、相位兼容权重 W_{ell,a}(t)，
  违反 R_{ell,a}(g)<=L_D 即回流出口。
```

该文件还严写 CD0 零类禁止：若坏行点由 `ell` 覆盖且同列素数见证不是 `ell`，
则列位移 `d_c` 不能为 `0 mod ell`。因此 `ColumnCRT` 的入口不再依赖启发式均匀性，
而是来自同列素数见证的不可零同余刚性。

审稿边界：这一步只闭合 `CC-COND-RADIUS/CC-COND-DISPLOAD` 的路由元数据；
它没有排除 `ColumnRadius/ColumnCRT`。当前最小硬点更新为物化
相位兼容的 `W_D(t),W_{\ell,a}(t)`，并证明全局阈值 `D_0,L_D` 或把违反者继续送入
`PDEC/TailAnchor/SAE`。

### 4.2N 本轮进展：ColumnDefect 有限权重物化

新增脚本 `experiments/prime_matrix_h4_pdec_column_defect_weight_certificate.py`，并生成：

```text
docs/monograph/h4-pdec-column-defect-weight-certificate.json；
docs/monograph/h4-pdec-column-defect-weight-certificate.md。
```

证书使用有限细化相位

```text
tau_fin=(p,q,row)
```

覆盖 `p<=1000`、每个 `p` 的 `5` 条最紧 RCI 行，共 `835` 个有限相位。两条权重行通过：

```text
CC-FIN-TIGHT-RADIUS-WEIGHT：D_col>81 的异常块为空；
CC-FIN-DISPLOAD-WEIGHT：displacement residue load>2 的异常块为空。
```

观测最大列见证半径为 `81`，最大位移余类负载为 `2`。这把上一节中的两个有限紧行
权重从“摘要常数”升级为机器可读空相位块。

审稿边界：该证书只在 `tau_fin` 有限域中相位兼容，不是全局
`ColumnRadius/ColumnCRT` 排斥。当前最小硬点进一步收窄为：

```text
证明正式坏窗抽取过程落入 tau_fin 有限域；
或给出全局 D_0,L_D 解析阈值；
并补 CC-FIN-RADIUS-1000 的全行半径权重。
```

### 4.2O 本轮进展：递归剥离新硬点

新增 `docs/monograph/prime-matrix-recursive-peeling-zero-row-hardpoint.md` 与审计
`docs/monograph/prime-matrix-recursive-peeling-zero-row-audit.md`。它把“上层零行向下递归”
写成精确层剥离恒等式：

```text
p-筛零窗剥到前一素数 r 后，
r-筛幸存者只能来自 p 的倍数，且商避开更小素数。
```

因此第一层剥离给出的是低复杂度复活点集合，而不是自动下层对齐零行。已知 `5` 个首零行样本中，
连续下层零行对为 `0`。该路线可保留为新的全局阈值攻坚目标：

```text
RPZ-Absorption => ColumnCRT/TailAnchor/ColumnRadius。
```

也就是证明若这些复活点被缝合窗口稳定吸收，则位移余类负载、尾标签负载或列见证半径必超阈值。
这比直接证明固定小 `D_0,L_D` 更接近当前 H4-PDEC 出口账本。

新增 `docs/monograph/prime-matrix-scaled-peeling-halfwidth-audit.md` 后，缩放行号与半宽素数版本也已审计：
同批样本中 `nP/p` 缩放后实际含完整下层零行的只有 `1/5`；半宽层连续零行段最大长度为 `0`。
这说明 `q^2` 落入半宽 CRT 周期只是建模条件，不能替代复活点吸收缺陷定理。

新增 `docs/monograph/prime-matrix-rpz-absorption-defect-route.md`、
`docs/monograph/prime-matrix-rpz-absorption-defect-audit.md` 与脚本
`experiments/prime_matrix_rpz_absorption_defect_audit.py` 后，复活点吸收缺陷已被路由为：

```text
survivor / TailAnchor / ColumnCRT / ColumnRadius / Distributed-RPZ。
```

有限样本中半宽层共有 `15` 个复活点，缺失吸收标签为 `0`，单窗最大吸收标签负载与
最大顶层列负载均为 `1`。因此 `RPZ-Absorption=>TailAnchor` 不能靠单窗集中闭合；
当前最小硬点进一步压缩为 `RPZ-Distributed Barrier`：若漂移窗口族中
`L_T<=T_0`、`L_D<=D_1` 且 `L_R=0`，则低负载吸收容量不足以覆盖所有 RPZ 复活点，
否则必须回流到命名出口。

新增 `docs/monograph/prime-matrix-rpz-sliding-plateau-barrier.md`、
`docs/monograph/prime-matrix-rpz-sliding-plateau-audit.md` 与脚本
`experiments/prime_matrix_rpz_sliding_plateau_audit.py` 后，`Distributed-RPZ` 又被压缩：
在同批样本中包含原零行的最大连续滑动零窗平台长度均为 `5`，唯一复活源 `16` 个，
滑动吸收事件 `73` 个；阈值 `T_0=4` 时 `5/5` 样本都触发持久源 `TailAnchor`。
因此剩余硬点不再是一般分散吸收，而是源删除后的边界压缩分支 `RPZ-BCB`：
若未触发 TailAnchor，则所有复活源必须落入滑动平台两端边界层；下一步要排除该边界层逃逸，
或把它送入 `SAE/PDEC/ColumnCRT`。

新增 `docs/monograph/prime-matrix-rpz-boundary-compressed-core-route.md`、
`docs/monograph/prime-matrix-rpz-bcb-core-audit.md` 与脚本
`experiments/prime_matrix_rpz_bcb_core_audit.py` 后，`RPZ-BCB` 已被进一步路由为
`BCB-Core`：无 TailAnchor 时，强制中心区间 `J_{T0}=[L+A+T0,R+B-T0]`
是半宽 `h`-筛零区间。同批样本中中心区间实际 `11` 个半宽幸存者全是尾锚核心源；
删除这些尾锚源后 `5/5` 中心区间干净，且 `5/5` 中心区间含完整半宽行。当前最小硬点更新为
`BCB-Grid/Endpoint exclusion`：证明正式平台中心区间必含完整下层行，或端点 seam
失败进入 `SAE/PDEC/ColumnCRT`。

新增 `docs/monograph/prime-matrix-rpz-bcb-grid-endpoint-criterion.md`、
`docs/monograph/prime-matrix-rpz-bcb-grid-endpoint-audit.md` 与脚本
`experiments/prime_matrix_rpz_bcb_grid_endpoint_audit.py` 后，网格包含部分已精确化：
`J=[u,v]` 含完整 `h` 对齐行当且仅当 `N>=delta_h(u)+h`。样本中 `5/5` 满足该判据，
端点缺陷为 `0`，判据与枚举不一致为 `0`，`4/5` 由纯长度 `N>=2h-1` 自动闭合。
当前最小硬点更新为 `BCB-Endpoint persistence exclusion`，即排除 `(Grid)` 失败相位的持续存在，
或路由到 `SAE/PDEC/ColumnCRT`。

新增 `docs/monograph/prime-matrix-rpz-bcb-endpoint-persistence-route.md`、
`docs/monograph/prime-matrix-rpz-bcb-endpoint-phase-ledger.md` 与脚本
`experiments/prime_matrix_rpz_bcb_endpoint_phase_ledger.py` 后，端点失败分支已完成稀疏/持久二分：
低相位负载进入 `SAE`，高相位负载进入 `PersistentEndpointDefect`，再进入 `PDEC/ColumnCRT`。
有限样本实际端点失败 `0/5`，可能失败相位总数 `2`，不同可能失败相位键数 `2`。
RPZ 链条下一步应转为二选一：闭合 `SAE/PDEC/ColumnCRT` 证书，或继续沿下层 `h`-筛零行做递归下降。

新增 `docs/monograph/prime-matrix-rpz-dual-track-closure-route.md`、
`docs/monograph/prime-matrix-rpz-lower-zero-descent-audit.md` 与脚本
`experiments/prime_matrix_rpz_lower_zero_descent_audit.py` 后，上述二选一已同步推进：
Track A 固定 `RPZ-SAE/RPZ-PDEC/RPZ-ColumnCRT` 三类证书接口；Track B 证明下层零行下降引理，
并在样本中把 `6` 条 BCB 条件下层零行全部下降到 `p=2` 直接矛盾，阻断节点数为 `0`。
当前最小硬点更新为 `LowerDescent-Grid persistence + certificate materialization`。

新增 `docs/monograph/prime-matrix-rpz-lower-descent-obstruction-ledger.md`、对应 JSON 与脚本
`experiments/prime_matrix_rpz_lower_descent_obstruction_ledger.py` 后，`LowerDescent` 阻断不再是
未命名异常。对每个相邻转换 `p -> r`，阻断由行号模 `P(r)` 的有限相位决定，并分为
`grid_fail` 与 `puncture_block`。本批实际转换节点 `20` 个全部为 `success`，实际阻断为 `0`。
新增 `docs/monograph/prime-matrix-rpz-certificate-materialization-interface.md` 把这些阻断相位并入
`RPZ-SAE-FIN`、`RPZ-PDEC endpoint phase row` 与 `RPZ-ColumnCRT endpoint displacement row`。
当前最小硬点进一步拆成：证明正式下降路径总在 `success` 相位，或提交上述三类证书。

新增 `docs/monograph/prime-matrix-rpz-certificate-skeleton-package.md`、对应 JSON 与脚本
`experiments/prime_matrix_rpz_certificate_skeleton_builder.py` 后，证书义务已变成具体行：
endpoint 低负载 `RPZ-SAE-FIN` 候选 `2` 个；endpoint `PDEC/ColumnCRT` 行各 `2` 条；
lower-descent `grid_fail` 的 `PDEC/ColumnCRT` 行各 `3` 条。`puncture_block` 暂无相位。
下一步最小硬点是先闭合两个 endpoint SAE 候选，再证明三条 lower-descent `grid_fail`
相位行不会被正式下降路径命中，或为其提交 `U_CRT<L_PDEC` / `ColumnCRT` 证书。

新增 `docs/monograph/prime-matrix-rpz-endpoint-sae-finite-certificate.md`、对应 JSON 与脚本
`experiments/prime_matrix_rpz_endpoint_sae_finite_certificate.py` 后，两个 endpoint SAE 候选在
当前账本中 possible load 为 `2`、actual load 为 `0`，因此当前有限账本层面的
`RPZ-SAE-FIN` 真空闭合。该项不排除全局 SAE；当前最小硬点转为三条 lower-descent
`grid_fail` 相位行的路径避开证明，或其 `PDEC/ColumnCRT` 证书。

新增 `docs/monograph/prime-matrix-rpz-lower-grid-fail-avoidance-certificate.md`、对应 JSON 与脚本
`experiments/prime_matrix_rpz_lower_grid_fail_avoidance_certificate.py` 后，三条 `grid_fail`
相位行已化为闭式判据 `delta=-(a-1)(p-r) mod r`、`grid_success iff delta<=p-r`。当前下降树
`20` 个实际转换节点全部避开，实际 `grid_fail` 为 `0`，闭式计数与枚举不一致为 `0`。
剩余硬点因此变为全局相位控制：证明正式下降路径始终满足该不等式，或把违反族送入
`PDEC/ColumnCRT`。

新增 `docs/monograph/prime-matrix-rpz-formal-descent-phase-inequality.md` 后，上述表述进一步校正：
已存在的正式下降路径自动满足 `delta<=p-r`；真正未闭合的是“每个正式反例分支都存在这样的
下降路径”。若路径不存在，第一处失败必是 `grid_fail/puncture_block` 有限相位，进入
`SAE/PDEC/ColumnCRT`。当前最小硬点更新为：证明路径存在，或排除首阻断相位证书。

新增 `docs/monograph/prime-matrix-rpz-first-obstruction-dichotomy.md` 后，端点穿孔阻断被全局排除：
完整下层行若含端点 `ap`，则必有 `r|a`，与端点复活所需的 `r∤a` 矛盾。因此首阻断唯一可能是
`grid_fail` seam 相位。当前最小硬点收窄为 first-grid-fail seam 的 `PDEC/ColumnCRT` 排斥证书。

新增 `docs/monograph/prime-matrix-rpz-first-grid-fail-seam-certificate.md`、对应 JSON 与脚本
`experiments/prime_matrix_rpz_first_grid_fail_seam_certificate.py` 后，first-grid-fail 已压成双帽
seam 标准形：`12` 个 seam 相位行覆盖完整 `Q` 中 `1752` 个 grid_fail 相位，计数不一致为 `0`。
增强账本进一步给出：`1348` 个端点相位已由下层标签杀死，`404` 个 unit endpoint 相位需要
endpoint-PDEC 或 ColumnCRT。

新增 `docs/monograph/prime-matrix-rpz-unit-endpoint-columncrt-gate.md` 与脚本
`experiments/prime_matrix_rpz_unit_endpoint_columncrt_gate.py` 后，unit endpoint 分支被压到固定非零
ColumnCRT 位移：

```text
c=ap mod r=r+(p-r)-delta；
H_endpoint ≡ -c*r^{-1} mod p；
d=h_witness-H_endpoint mod p != 0。
```

当前 `12/12` 门控行都有显式同列素数见证，覆盖全部 `404` 个 unit endpoint 相位。当前最小硬点更新为：
证明正式反例族映入这些门控行并排除 `ColumnCRTDefect(p,d)` 阈值 `L_D`，或证明正式反例族避开
unit endpoint seam。

新增 `docs/monograph/prime-matrix-rpz-columncrt-threshold-obstruction.md` 后，直接阈值排斥被证伪为
无效路线：同一 unit gate 内全部 unit residues 具有同一个 `(label=p, displacement=d)`，故
`R_{p,d}` 的内禀负载等于 `prod_{ell<r}(ell-1)`。当前最大内禀负载 `48`，测试 `L_D=2`
时 `10` 条门控行、`400` 个相位超过阈值；这只表示进入 `ColumnCRTDefect`，不是排除。
因此当前最小硬点不应再写成“调低 L_D”，而应写成三选一：formal-family 避开 unit gate、
endpoint-PDEC 上界、或独立 `ColumnCRTDefect` 排斥定理。

新增 `docs/monograph/prime-matrix-rpz-three-route-closure-audit.md` 后，三选一已排序：
路线 A `formal-family avoidance` 优先；路线 B `endpoint-PDEC` 保留；路线 C
`ColumnCRTDefect` 只作为深定理备选。下一步应把攻坚火力转到 formal-family 相位不等式
`delta<=p-r` 或 unit gate 避开定理。

新增 `docs/monograph/prime-matrix-rpz-formal-phase-automaton.md` 后，路线 A 进一步压缩为
`A_p` 接受集准入定理。当前 BCB-Core 账本中 `6/6` 起始行被接受，且自动机给出每个
`p<=13` 的接受/拒绝相位计数。当前最小硬点更新为：证明 formal-family 起始相位必在
`A_p`，或把拒绝相位命中送入 seam/PDEC/ColumnCRT。

新增 `docs/monograph/prime-matrix-rpz-rejected-phase-absorption.md` 后，拒绝相位命中已经全量送入
seam/PDEC/ColumnCRT：`27924` 个 rejected phase、`12` 个 distinct first-fail seams、未覆盖样例
`0`。因此路线 A 的未命名逃逸已清零；剩余硬点重新集中到 seam/PDEC/ColumnCRT 出口排斥。

新增 `docs/monograph/prime-matrix-rpz-seam-exit-pressure-ledger.md` 后，seam/PDEC/ColumnCRT 出口
本身被压成更小的审稿对象：`12` 条 seam 行覆盖 `1752` 个 seam 支持相位，其中 `1348` 个端点
已由下层标签杀死；剩余 `404` 个 unit endpoint 相位全部进入固定非零 ColumnCRT 位移类，聚合后
为 `10` 类，最大聚合负载 `96`。当前最小硬点因此更新为三选一：formal-family 避开这 `12`
条 seam；为 `12` 条单余类 PDEC 支持提交 `U_CRT<L_PDEC`；或证明 `10` 个固定非零
`ColumnCRTDefect` 类不可能出现。

### 4.3 SAE local escape exclusion

目标：孤立坏窗不能逃过 PDEC。

补正动作：

1. 定义 isolated window 的最小局部状态；
2. 给出 survivor/lift/higher-defect 三出口；
3. 对每个出口建立有限局部证书或递推提升；
4. 证明 SAE 不与 PDEC 分支重复计数。

可行性：B/C。
局部证书可攻，但需要避免把孤立逃逸重新定义成原命题。

### 4.4 Rankin certificates

目标：正式着色走廊全部满足 smooth-core Rankin 预算，或失败者转入 low-mod CRTDefect/PDEC/SAE。

补正动作：

1. 固定正式走廊列表；
2. 对每个颜色类计算 exact core count 与 Rankin ledger；
3. 对失败颜色抽取 low-mod residue spike；
4. 证明 spike 必进入 PDEC/SAE。

可行性：B。
这是证书驱动项，最适合继续推进。

## 5. H5：RRD / OSPC / Selberg-uniform 常数账本

### 5.1 精确目标

在同一 convention 下证明：

\[
C_{\mathrm{RRD}}+C_{\mathrm{OSPC}}+
C_{\mathrm{SelbergUniform}}+C_{\mathrm{round}}
<0.053369509758272926.
\]

当前预算拆分：

| 子项 | 目标 |
|---|---|
| RRD-low | `<=0.006` |
| RRD-perp | `<=0.012` |
| RRD-conversion | `<=0.002` |
| OSPC | `<=0.020` |
| SelbergUniform | `<=0.008` |
| round | `<=0.003` |

### 5.2 攻坚路线

1. **RRD-low**：使用低模字典投影 `Pi_{<=Z}`；证明无 `OSPC*` 时加权 CRT 缺陷界
   `0.005366563145999495` 足以吸收。
2. **RRD-perp**：写成正交补能量上界，避免与 low 分支重复。
3. **OSPC**：把 `E_dir>=1+delta_dir` 的有向集中转成 CRTDefect 或 Tail-anchor。
4. **SelbergUniform**：把样本有理审计升级为 `P>=P0` 的统一矩常数。
5. **round**：保持外向舍入，所有 trig/log/sup-rho oracle 使用有理包络。

### 5.2A 本轮进展

新增 `docs/monograph/h5-rrd-ospc-proof-obligation-matrix.md`。该矩阵给出 `H5-Acceptance`：若 `RRD-low<=0.006`、`RRD-perp<=0.012`、`RRD-conversion<=0.002`、`OSPC<=0.020`、`SelbergUniform<=0.008`、`round<=0.003` 六项成立，则总损失为 `0.051`，严格小于 `0.053369509758272926`。

新增 `docs/monograph/h5-1-rrd-low-exit-theorem.md`。该文件用块级 Cauchy--Schwarz 证明 H5.1 出口路由：

```text
|E_low|>0.006 => OSPC* or weighted CRTDefect.
```

因此 H5.1 的路由义务已闭合；当前 H5 最小硬点转为排除 `OSPC* / weighted CRTDefect` 出口，或把它们并入 H4 的 `PDEC-or-SAE` / Tail-anchor 排斥。

新增 `docs/monograph/h5-4-ospc-weighted-crtdefect-absorption.md`。该文件证明 `OSPC*` 与 `weighted CRTDefect` 都产生零均值低模测试函数与坏窗集合，因此由统一 `UPS-1` 二分进入：

```text
PDEC or SAE.
```

由此，H5.4 的出口吸收已闭合；未闭合的是 H4 的 `PDEC exclusion` 与 `SAE local escape exclusion` 证书。

### 5.3 可行性

评级：B。
这是 PM 方向当前最可操作的硬项。当前并未闭合 H5；H5.1 与 H5.4 的路由/吸收已完成，下一步应先攻 H4 的 `PDEC-Cert/SAE-Cert`，再攻 H5.2。

## 6. H6：二点筛 I3-Core

### 6.1 精确目标

把 I3-Core 拆成可审查定理链：

```text
TRC / true residual balance
=> TCA linear bridge
=> SC2 near-crossing control
=> 45-Main synchronization peak control
=> Directional Balance / Fourier CRTDefect
=> Zero Mass
=> endpoint smoothing
=> fixed-w singular ledger
```

### 6.2 最大风险

该接口不能靠普通上界筛闭合。原因是二点筛终局含固定差素数对强后果；任何使用 `|U_Y|` 下界的步骤都可能隐藏 parity barrier。

### 6.3 攻坚路线

路线 A：真实残余新模均衡。

证明对所有新素数 `p>Y`：

\[
\#\{x\in U_Y:x\equiv0,w\pmod p\}
\le (2/p+o(1))|U_Y|+E_p
\]

并使总误差可求和。

路线 B：总命中不等式绕开逐点均衡。

\[
\sum_{P^\alpha<p\le P}\#\{x\in U_{P^\alpha}:p\mid x(x-w)\}
<|U_{P^\alpha}|.
\]

路线 C：若 A/B 失败，明确命名为 `true-residual correlation gap`。

### 6.4 可行性

评级：D（终局版），B/C（条件/局部版）。
局部结构、有限包、小 `q`、endpoint smoothing 可继续完善；但全局 I3-Core 若完全闭合，会推进固定差素数对，必须按重大新定理标准处理。

## 7. H7：DI/BFI 外部定理到 KLS-window 适配

### 7.1 精确目标

建立外部定理版链条：

\[
\text{DI}+\text{BFI}
\Rightarrow
\text{KLS-window}
\Rightarrow
\text{BE2--3K}
\Rightarrow
\text{WBE2}
\Rightarrow
\text{BMD}.
\]

### 7.2 补正动作

1. 写 `Theorem KLS-ext (DI/BFI)`，逐项列外部假设；
2. 建立变量表：
   - Kloosterman 相位；
   - 模数族；
   - 频率 `h`;
   - 逆元变量；
   - well-factorable 权重；
   - gcd strata；
   - 端点平滑；
   - `B(A)` 对数损失。
3. 证明本文 KLS-window 完全满足该模板；
4. 把完全自足版明确降级为“需重证 DI/BFI”。

### 7.2A 本轮进展

新增 `docs/monograph/kls-window-di-bfi-adaptation-template.md`。该文件已给出 `H7-KLS-ext` 与 `H7-BMD-ext` 两个外部定理版命题，并逐项填入 CRT 相位归一化、非互素 gcd 层、多对数损失、well-factorable 权重和 `B(A)` 吸收账本。由此，H7 从“适配表未完成”升级为“外部深定理版闭合；完全自足版仍需重证 DI/BFI”。

### 7.3 可行性

评级：A/B，外部引用工程已完成第一版。
该项不等于证明孪生素数，也不闭合 `BMD=>TLI`；下一硬项应转入 H8 或返回 Prime Matrix 的 H5/H4/H2。

## 8. H8：BMD 到 TLI 无隐藏下界审查

### 8.1 精确目标

证明：

\[
\text{BMD}\Rightarrow\text{BST--2}\Rightarrow\text{BST}\Rightarrow\text{TLI}
\]

且没有使用未证明的素数对筛余下界。

### 8.2 必须逐项检查

| 检查项 | 必须排除的隐藏假设 |
|---|---|
| BMD-Zero vs BMD-Char | 非空性不能替代有符号分布 |
| BST-2 | `pm-2` 的 `Y`-rough 稳定性不能偷用目标结论 |
| BST | Buchstab 半素数转移常数必须有上下界 |
| TLI denominator | `|U_Y|` 不能来自未证二点筛下界 |
| singular convention | `q|w` 的局部因子在分子分母中同口径 |

### 8.3 攻坚路线

路线 A：分母消除法。
把 TLI 改写为不需要单独下界 `|U_Y|` 的加权恒等式，直接比较命中权与残余权。

路线 B：Buchstab 稳定性定理。
证明 `pm-2` 的旧筛粗性在 BMD 分布下满足 Buchstab 主项，误差小于余量。

路线 C：若不能闭合，明确命名为 `Buchstab-transfer parity gap`，并保持条件状态。

### 8.4 可行性

评级：D（终局版），B（审查版）。
审查和定位可完成；真正无条件闭合会触及固定差素数对，不能承诺由现有材料完成。

## 9. H9：RH controlled exits

### 9.1 精确目标

把 RH verification package 改写为每个出口的同口径不等式：

\[
\text{exit load lower bound}
\le
\text{exit capacity upper bound}.
\]

并在全局 GEE 中得到矛盾。

### 9.2 必须定理化的出口

| 出口 | 需要证明 |
|---|---|
| PC1 | 显式公式入口，离线零点给出平滑素数异常 |
| PC2 | CRT baseline transfer，无 convention 换算误差 |
| sparse | ACC/Hole/OV 吸收 |
| dense | DGap/PI/FCT/DSO 吸收 |
| tail | Vaaler/Fourier 高尾吸收 |
| internal | Lyapunov/no-cycle 有限下降 |
| GEE | 所有出口总上界与入口下界矛盾 |

### 9.3 攻坚路线

路线 A：controlled exits 四列表。

```text
输入异常 | 输出吸收 | 使用定理 | 常数 convention
```

路线 B：正性二次型压缩。

尝试构造一个二次型 `Q`：

\[
\text{off-critical zero}\Rightarrow Q<0,
\qquad
\text{CRT/prime ledger}\Rightarrow Q\ge0.
\]

若成功，RH 链可从多出口工程压缩为正性定理。

### 9.4 可行性

评级：D。
该方向不能通过方阵或二点筛刚性类比完成；必须保持 verification package，直到 controlled exits 被独立证明。

## 10. H10：合著稿状态工程

### 10.1 已完成

1. 主稿已接入 `Pre-External-Referee Hard Obligations`。
2. `pre-external-referee-remaining-obligations.md` 已列出 H1--H10。
3. `claim-status-table.md` 已记录该审查项。
4. 主稿保留不可过度声明边界。
5. 新增 `docs/monograph/claim-status-discipline.md`，固定六类状态、升级条件、禁止越界声明和机械检查命令。
6. 主稿新增状态专用 theorem-like 环境：`Proved-in-text`、`Reduction-closed`、`External-theorem-closed`、`Computational-certificate`、`Referee-block`、`Not-claimed`。

### 10.2 仍可优化

1. 把历史章节中的普通 theorem 环境逐步替换为状态专用环境；
2. 给每个实验脚本建立用途索引；
3. 将历史探索文档移入 archive，主线只保留当前最短链条。

### 10.3 可行性

评级：A，作者侧状态分级工程已完成第一版。
剩余为编辑性替换和索引清理，不改变当前数学闭合状态。

## 11. 建议下一轮执行顺序

### 11.1 可立即完成的工程闭合

1. 给每个实验脚本建立用途索引；
2. 把历史章节中的普通 theorem 环境逐步替换为状态专用环境。

### 11.2 最值得继续硬攻的数学接口

1. `H5`：RRD/OSPC 六项常数账本；
2. `H4`：Rankin certificate 全列表与失败路由；
3. `H2`：RHI 路线中的 PM-R2B/RSE。

### 11.3 必须保持条件状态的深接口

1. `H6`：I3-Core 终局；
2. `H8`：BMD=>TLI 终局；
3. `H9`：RH controlled exits。

这些接口可以继续研究，但在新增真正证明前，不应写成“已补齐全部缺口”。
