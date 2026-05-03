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
