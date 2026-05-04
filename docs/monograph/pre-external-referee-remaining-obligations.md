# 合著稿外部专家审查前剩余义务总表

本文档审查 `paper/contradiction-field-monograph/contradiction-field-monograph.tex` 及 `docs/monograph/` 中的状态表、依赖图、逐行复核矩阵和优化审查。目标是明确外部专家正式审查前，作者还必须完成哪些证明链条闭合义务，尤其是实际论证细节的严格性。

## 0. 总判定

当前合著稿可以作为“矛盾场理论体系、依赖边界和审稿包整理稿”进入内部继续完善，但还不应作为宣称终局无条件定理的外审稿提交。

必须保持的总状态：

| 主线 | 当前可诚实宣称 | 不能宣称 |
|---|---|---|
| Prime Matrix 行列命题 | A/B 入口归约、BPN-LHB 子模块有限证书/显式外部定理版闭合、多个刚性接口已压缩 | 方阵行列素数存在性已完整无条件证明 |
| 二点筛 A/B 命题 | 等价性与强度已证明；二次筛链条有条件/外部深定理版框架 | 孪生素数、Goldbach 型结论或二点筛非空已无条件证明 |
| RH 方向 | RH contradiction-field verification package；controlled exits 已编号组织 | RH 已无条件证明 |
| 合著理论系统 | 统一方法论、依赖图、证据等级和未闭合接口已显式化 | 所有核心猜想/主命题已被合著稿完全闭合 |

外审前最关键任务不是继续增加新命名，而是把每个 `Reduction-closed`、`External-theorem closed`、`Referee-block` 的接口变成可逐行核验的定理、引用模板、常数账本或有限证书。

## 1. 主稿命题逐项审查

| 主稿位置 | 声明 | 当前状态 | 外审前必须补正 |
|---|---|---|---|
| `contradiction-field-monograph.tex:58` | A/B reduction | 归约命题；未排除 Structured-EHPD | 把 `docs/row-column-reduction-formal-appendix.md` 的入口、剥离、不重不漏、Tail-anchor 假设转为正文或附录定理；明确哪些为已证，哪些依赖 D 组 |
| `contradiction-field-monograph.tex:70` | 二点命题等价与强度 | 文内可证明 | 保留“会推出孪生素数/固定差素数对”的强度说明；禁止把后续条件链写成无条件证明 |
| `contradiction-field-monograph.tex:184` | 二点二次筛条件闭合链 | 条件命题；依赖 I3-Core | 把 I3-Core 拆成定理清单：TRC/TCA/SC2/45-Main/Directional Balance/Zero Mass/Endpoint；逐项给证明或外部输入 |
| `contradiction-field-monograph.tex:202` | 窗口压缩条件版 | 条件命题；依赖同一 I3-Core | 补全 `C_Q,C,C_*` 的来源、固定 `w` 量词、有限小 `P` 处理；不得作为无条件窗口非空定理 |
| `contradiction-field-monograph.tex:390` | RH contradiction-field synthesis | verification package | 将每个 controlled exit 写成“输入异常—输出吸收—常数 convention—使用定理”；独立核验前保留 warning |
| `contradiction-field-monograph.tex:530` | 当前合著闭合 | 可作为审稿边界定理 | 保持“闭合的是审稿结构和依赖边界，不是终局定理”的措辞 |
| `contradiction-field-monograph.tex:542` | 内部逐行审查 | 作者侧审查完成 | 不能把 `BLOCK-REFEREE` 改写为 `PASS-AUTHOR`；需外部专家逐行接受 |

## 2. Prime Matrix 行列命题剩余义务

### PM-A. 入口与结构归约

必须完成：

1. **A/B 入口附录内联或定理化**：逐行证明行/列反例如何进入 Structured-EHPD，不能只引用探索文档。
2. **三层剥离不重不漏**：小因子锁、双粗主体、尾锚剥离必须给出集合分解等式或 disjoint/source-deleting 规则。
3. **Tail-log4 接口核验**：若仍使用 BG/RKS/Baker 类外部输入，必须在 `external-theorem-index.md` 中给精确定理号、变量替换和常数吸收。

当前风险：A/B 入口是归约，不是终局排斥；主稿已正确说明这一点，但外审稿需要把“归约链条”写得足够可复核。

### PM-B. Structured-EHPD / D 组排斥

这是 Prime Matrix 终局的第一硬缺口。外审前必须至少选择一种方式：

1. **直接闭合 D 组**：给出 Structured-EHPD 不可能的完整证明，包含 D-OMR、D-CGTP、D-LSMP、D-FCT/NRC 的常数与量词。
2. **压缩到 RHI 路线**：把局部刚性统一为 `PM-R1/PM-R2 => RHI`，并证明
   \[
   |G_Y(I)|\ge c_-(\alpha)|I|\prod_{q\le Y}(1-1/q),
   \quad
   B_Y(I)\le(\log(1/\alpha)+\eta)|G_Y(I)|
   \]
   且 `eta < 1-log(1/alpha)`。
3. **保持归约状态**：若不能完成 1 或 2，则 Prime Matrix 终局必须继续标为 `Conditional on PM-5/PM-7`。

当前风险：扩展斜线锁、CRT 镜像、零行复现、实验扫描都能提供刚性，但不能单独替代大因子命中上界或有符号分布估计。

新增 `docs/monograph/prime-matrix-wsh-hall-phase-certificate.md` 后，RHI/Structured-EHPD
路线中最窄的半素数补洞接口已有有限相位证书：`17<=p<=2000` 的 `215074` 条含平衡双尾半素数行
没有局部 Hall 匹配失败，且全部通过 `3 log^2(q)` 候选半径；证书逐项核验匹配偏移满足
小素数轮筛允许条件。该文件只能作为 `WSH-Hall/PDEC` 的材料化审计，不能替代全局定理。
外审前若使用此路线，必须补以下二择一证明：

```text
WSH-Hall uniformly true;
or any Hall defect forces PDEC / Tail-anchor / Endpoint deficit.
```

新增 `docs/monograph/prime-matrix-wsh-hall-defect-trichotomy.md` 后，第二项被拆成可审查的
三出口模板。任意 Hall 失败先化为连续半素数块 `B_0` 的正规形
`|N_R(B_0)|<|B_0|`，再同时投影到端点亏损、尾因子负载、小轮相位、固定偏移容量和
`q^2-n` 镜像非零类块。外审前仍缺的是统一不等式：

```text
WSH-Expansion-or-Defect:
if Tail-anchor and fixed-offset/PDEC thresholds do not fire,
then |N_R(B_0)| >= |B_0| for R=C log^2(q);
else the named exit absorbs the block.
```

新增 `docs/monograph/prime-matrix-wsh-expansion-margin-ledger.md` 后，作者侧有限证书显示
`17<=p<=2000` 中 `8440419` 个连续半素数块的最小 Hall 余量为 `1`，零余量块为 `0`。
外审前仍不能把该有限事实推广为全局证明；必须补 `WSH Positive Expansion or Named Defect`
的统一证明，或把它明确标为条件输入。

新增 `docs/monograph/prime-matrix-wsh-short-critical-block-reduction.md` 后，该统一证明进一步拆为
`SCB-1/SCB-2`：长块 `|B|>=4` 自动扩张或触发命名缺陷；短块 `|B|<=3` 逐型排斥或触发命名缺陷。
有限审计中所有 `surplus<=2` 的小余量块都满足 `|B|<=3`。外审前仍需给出这两个命题的逐行证明。

新增 `docs/monograph/prime-matrix-wsh-scb2-local-exclusion-template.md` 后，`SCB-2` 已达到
“路由闭合 modulo Endpoint/PDEC exclusion”：短块若 Hall 失败，按定义进入端点亏损出口；
双点/三点紧块还检查 Tail-repeat 与 Fixed-offset-full-load。外审前剩余不再是短块失败是否
可命名，而是 Endpoint/PDEC 出口是否能被全局排除。

新增 `docs/monograph/prime-matrix-wsh-scb1-long-block-expansion-template.md` 与
`docs/monograph/prime-matrix-wsh-scb1-long-block-certificate.md/json` 后，`SCB-1` 长块分支
也有了有限证书：`17<=p<=2000` 中 `4573823` 个 `|B|>=4` 连续长块的最小 Hall 余量为
`3`，负余量和零余量均为 `0`；全部 `4` 个最紧长块同时触发 `Endpoint-margin` 与
`Fixed-offset-full-load`。外审前仍不能把该有限证书写成全局定理；必须补以下二择一证明：

```text
long-block positive expansion uniformly;
or every long tight block is absorbed by fixed-offset/PDEC, Tail-anchor, or Endpoint/PDEC.
```

因此 `WSH-Hall/PDEC` 的真实剩余已收窄为固定偏移/PDEC 吸收与 Endpoint/PDEC 排斥，
而不是继续枚举长短块样本。

新增 `docs/monograph/prime-matrix-wsh-fixed-offset-pdec-absorption.md` 后，固定偏移满载已有
一条逐行可核验的“无第三逃逸”引理：若 `1<n<q^2` 合成，则 `n` 有 `<=p` 的素因子；
满载偏移避开 `2,3,5,7,11,13` 后，所有缺失候选都必须由 `(13,p]` 中的解释因子吸收。
有限账本 `docs/monograph/prime-matrix-wsh-fixed-offset-pdec-ledger.md/json` 在 `11` 条满载偏移行、
`47` 个候选上核验 `missing_without_factor<=p=0`。外审前剩余随之更新为：

```text
FO-PDEC:
distributed explanation factors
=> persistent low-mod CRTDefect/PDEC
or sparse SAE/Endpoint escape.
```

该项仍未排除最终出口；它只证明固定偏移满载不再是未命名逃逸。

新增 `docs/monograph/prime-matrix-wsh-fo-pdec-hard-attack.md` 与
`docs/monograph/prime-matrix-wsh-fo-pdec-lowmod-audit.md/json` 后，`FO-PDEC` 进一步被压成
低模能量不等式。方程层已经逐项核验：`43` 条低模方程、`0` 个 CRT 方程失败、`0` 个双线性
方程失败。外审前剩余的精确义务是：

```text
FO-PDEC-E:
low-mod defect energy >= explicit PDEC threshold,
unless SAE/Endpoint absorbs the non-persistent part.
```

这仍是定量不等式缺口，不是文本工程缺口。

新增 `docs/monograph/prime-matrix-wsh-fo-pdec-energy-lemma.md` 后，`FO-PDEC-E` 的能量产生
半边已经证明：若解释因子不高负载，则低模能量至少为 `(1-theta)|E|`；若高负载，则进入
`Tail/PDEC` 出口。外审前剩余进一步收窄为阈值比较：

```text
PDEC-threshold:
same bad-window equation set E
must satisfy U_CRT(E) < E(E)
or L_PDEC(E) <= (1-theta)|E|.
```

该项需要正式常数、测试函数和同一集合上界；不能由有限能量账本替代。

新增 `docs/monograph/prime-matrix-wsh-fo-pdec-threshold-comparison.md` 后，`PDEC-threshold`
下界侧已变成显式投影：

```text
ell=199, h=95, M_ell(E)=3.959247567099438.
```

外审前剩余义务已经具体为：对同一投影坏窗向量 `g_199`，提交合法约束来源并证明
`U_CRT,199<3.959247567099438`，或证明该投影不持久而进入 `SAE/Endpoint`。

新增 `docs/monograph/prime-matrix-wsh-fo-pdec-dual-cluster-route.md` 后，上述 `U_CRT`
上界缺口进一步定位为 `ell=199,h=95` 的长度 `11` 对偶短弧聚簇。外审前必须证明：

```text
DualCluster-Exclusion:
dual arc length 11 cannot persist in the formal counterexample chain,
or the non-persistent instance is SAE/Endpoint.
```

新增 `docs/monograph/prime-matrix-wsh-fo-pdec-multiplicity-legitimacy.md` 后，外审前还必须核验
同一集合口径：`ell=199,h=95` 的强阈值 `3.959...` 依赖 equation/block-local 多重计数；
physical 去重后阈值为 `1.9699193446802263`。正式稿必须证明 `PDEC` 下界和 `U_CRT` 上界使用
同一个多重集合，或降级到 primitive 阈值。

新增 `docs/monograph/prime-matrix-wsh-fo-pdec-formal-unit-route.md` 后，该义务进一步前置：
`3.959...` 来自有限证书库中的跨 `q` 层聚合和嵌套块重复，不自动对应单个正式反例分支。
外审前必须补齐：

```text
FormalUnit-Stitching:
跨 q 层事件属于同一个持久坏窗族；

NestedBlock-Independence:
嵌套块重复是独立 Hall/PDEC 约束；

否则：
重复项回流 SAE/Endpoint，不能计入强阈值。
```

新增 `docs/monograph/prime-matrix-wsh-fo-pdec-branch-separation-theorem.md` 后，外审前义务进一步
精确：`BS-1/BS-2` 已排除无证明拼接和无证明重复计数。剩余不是泛泛的 formal unit 口径，
而是：

```text
Weighted Hall Dual Independence:
为 exact nested duplicates 提交加权 Hall 对偶独立行；

or

SAE/Endpoint absorption:
证明这些 exact duplicates 是非持久端点逃逸或必须坐标商掉。
```

### PM-C. BPN-BK / BPN-LHB 子模块

已较强闭合的部分：

1. `13<=P<61` 低范围最终证书。
2. `61<=P<=103` 窄带碰撞能量证书。
3. `107<=P<=229` 精确 `P/5` 分割递推。
4. `233<=P<=13207` 整数交叉乘法连续乘积证书。
5. `P>=13208` Rosser--Schoenfeld 显式常数包。

外审前仍需完成：

1. **证书复现说明**：每个 JSON/脚本需说明输入、输出、随机性为零、验收不等式和复现命令。
2. **RS1962 引用模板**：把 Corollary 1 `(3.5),(3.6)` 与 Theorem 7 `(3.26)` 写成正文可引用引理，并统一 `floor(P/5)`。
3. **全局接口边界**：明确 BPN-LHB 只是低洞桶接口闭合，不自动推出整个 PM 行列命题。

### PM-D. PDEC/SAE/Rankin 最终出口

这是 BPN-BK 全局链的最终硬缺口。必须完成三项之一的闭合：

| 出口 | 必须证明 | 失败时处理 |
|---|---|---|
| `PDEC exclusion` | 同一坏窗集合的非零 Fourier/CRT 缺陷上界 `U_CRT<L_PDEC` | 若无法证明，保持 referee-block |
| `SAE local escape exclusion` | 孤立坏窗的 survivor/lift/higher-defect 证书排斥 | 给出有限证书或降级为条件输入 |
| `Rankin certificates` | 全部颜色类 `rankin_budget_pass=true`，或失败者转入 low-mod CRTDefect/PDEC/SAE | 必须有正式走廊列表和可复现证书 |

外审稿不能把 `PDEC-or-SAE` 当作已经排除的矛盾；必须写成最终待验收接口。

新增 `docs/monograph/h4-pdec-certificate-template.md` 后，`PDEC exclusion` 的验收格式已固定为
`PDEC-Explicit-Cert` 或 `PDEC-Dual-Cert`。该模板证明了 persistent 分支给出的
`L_PDEC` 下界如何与同一坏窗集合的 `U_CRT` 上界相矛盾，并要求每条 `A,b,E,e`
约束都回指到 mirror、column、tail-anchor、core-overlap、Rankin routing 或
RRD/OSPC 吸收来源。当前仍未提交的是正式坏窗族的完整约束来源证明、全频率方向证书和
严格余量核验。

新增 `docs/monograph/h4-pdec-constraint-source-lemmas.md` 后，首批约束来源规则已逐行证明：
mass/非负性、相位容量继承、镜像等式与成对容量的适用边界、low-hole bucket 容量继承、
以及“违反即进入命名出口”的条件路由行。该项仍不排除 PDEC；它防止把完整周期均衡、
有限样本容量或条件镜像误用为任意坏窗子集的无条件约束。

新增 `docs/monograph/h4-pdec-admissible-constraint-table.md` 后，候选约束行已有第一版准入
矩阵：`Tautology / FiniteCert / SymbolicReady / ConditionalRouting / NeedsProof / Rejected`。
该表明确 full-cycle balance 与 sample-to-global cap 被拒绝进入正式证书；column cap、
low-hole bucket 符号化和条件路由元数据仍是下一步系数源硬点。

新增 `docs/monograph/h4-pdec-column-cap-source-lemma.md` 后，column cap 来源规则已固定：
有限列投影容量、符号化列容量定理、或违反列预算即进入 ColumnRadius/ColumnCRT/Tail-anchor
出口的条件路由行。该文件证明列见证位移非零刚性，但尚未给出 `B_col(j)` 系数账本。

新增 `docs/monograph/h4-pdec-column-cap-coefficient-ledger.md` 后，column cap 的 V1 系数源
已登记：有限列见证半径、RCI/CDB 联合审计、LHB 列残基刚性和条件 ColumnDefect 路由。
当前仍缺机器可读相位块 `C_j`，所以这些行尚不能直接进入最终 `A,b,E,e`。

新增 `docs/monograph/h4-pdec-lhb-column-phase-blocks.json` 与同名 Markdown 摘要后，
`Q=2310` LHB column rows 的第一批相位块已物化。`AFFINE/NEGDELTA/UNBRIDGED`
空异常块可作为有限 `A` 行；`WHOLEDEF/BRIDGED` 仍需投影容量证明。

新增 `docs/monograph/h4-pdec-lhb-support-to-capacity-transfer.md` 后，投影容量证明的缺口已精确化：
支撑相位大小不能自动界定 persistent 计数 `g(t)`；必须补相位指示、多重度界 `M(t)` 或允许全集
`Z_LHB` 投影容量。

新增 `docs/monograph/h4-pdec-lhb-multiplicity-cap-route.md` 后，`T3` 多重度路线已经有正式验收合同：
同一 `(p,Q,S,tau)` 下证明 `g(t)<=M(t)`，再把 `WHOLEDEF/BRIDGED` 的容量界写成
`sum_{t in C}M(t)`。这一步把外审义务压缩为可物化的 `M(t)` 与接入证明。

新增 `docs/monograph/h4-pdec-lhb-multiplicity-cap-certificate.json/md` 后，`Q=2310` 的
`M(t)` 已由高层 CRT 补洞完成数物化；`WHOLEDEF/BRIDGED` 在 LHB allowed-set 分支给出
`bound=0` 容量行。外审硬义务随之改为接入 LHB 分支或把不满足者路由到
`ColumnRadius/ColumnCRT/TailAnchor/SAE` 等命名出口。

新增 `docs/monograph/h4-pdec-lhb-attachment-lemma.md` 后，`S subset Z_LHB` 在 LHB 型坏窗
分支中已经逐行证明。外审硬义务继续收窄为：证明正式 PDEC 抽取过程只产生 LHB 型坏窗，
或把非 LHB 型失败逐类送入命名出口。

新增 `docs/monograph/h4-pdec-bad-window-classification-lemma.md` 后，非 LHB 型失败已经
逐类送入 `SAE/ColumnCRT/ColumnRadius/TailAnchor/Rankin/拆分证书`。其中拆分是工程义务；
其余出口仍需排除或提交各自证书，而不是继续补 LHB 接入口。

新增 `docs/monograph/h4-pdec-homogeneous-splitting-lemma.md` 后，`拆分证书` 义务已闭合：
口径混合必须无损拆成同口径子族，不能作为单个 `PDEC-Dual-Cert`。剩余硬义务只保留
拆分后的 `SAE/ColumnCRT/ColumnRadius/TailAnchor/Rankin` 出口。

新增 `docs/monograph/prime-matrix-recursive-peeling-zero-row-hardpoint.md` 与
`docs/monograph/prime-matrix-recursive-peeling-zero-row-audit.md` 后，递归剥离路线已进入审稿边界：
它严格给出上层零窗剥离后的复活点结构，但不能自动推出连续下层零行。外审前若使用该路线，
必须补 `RPZ-Absorption=>ColumnCRT/TailAnchor/ColumnRadius`，即复活点被吸收时必触发命名出口。

新增 `docs/monograph/prime-matrix-adjacent-shell-recursive-descent-route.md` 后，递归剥离支线得到
更强的相邻壳层入口：在 `q^2` 内从旧 `p`-筛升级到 `q`-筛，非第一行唯一新增旧筛幸存穿孔为
`q^2`。因此外审前可把 `q` 零行无损降为：

```text
旧 p-筛 q 零窗
=> 完整 p 对齐零行 or seam zero window with two guards。
```

新的剩余义务是 `SeamGuard-Elimination`：证明两个 guard 不能长期吸收 `Row(p)` 所需幸存者；
若吸收持续，必须触发 `SAE/PDEC/ColumnCRT`。

新增 `docs/monograph/prime-matrix-scaled-peeling-halfwidth-audit.md` 后，缩放到前一素数和约半宽素数的版本
也不能直接闭合：缩放行号需要完整包含判据，半宽层会复活粗互补因子点。该路线仍需复活点吸收缺陷定理。

新增 `docs/monograph/prime-matrix-seam-multilevel-descent-route.md` 与对应审计后，外审前可使用更精确
的 seam 多层下降接口：`h` 层复活点为 `P^-(n)∈(h,p]` 的点，完整下层行避开该集合即强制零行。
有限账本中 `p<=500` 全量与 `p<=2000` 确定性抽样均无 seam 阻断。剩余义务因此改写为：
证明全局 `SMD-Global Inequality`，或证明所有持久阻断必触发 `SAE/PDEC/ColumnCRT`；不能仅凭有限账本
宣称 seam guard 已无条件排除。

新增 `docs/monograph/prime-matrix-seam-tail-mirror-descent-route.md` 与对应审计后，外审前还可使用
尾镜像接口：强制 `h` 零行的行相位 `rho` 或镜像相位 `N_h-rho+1` 若落入 `1..h`，就给出
`h×h` 方阵内条件零行，从而可与归纳输入 `Row(h)` 冲突。有限账本中 `p<=500` 全量和
`p<=2000` 抽样均为 `100%` 命中。剩余义务进一步收窄为证明全局 `TailMirror-SMD`，
或把非命中相位集合接入 `SAE/PDEC/ColumnCRT`。

新增 `docs/monograph/prime-matrix-total-zero-row-recursive-descent-route.md` 与对应总审计后，外审前
应把 aligned、seam、末行穿孔统一放入 `TotalDescent-TM`。有限账本中 `p<=500` 全量
`21936/21936` 条非第一 `q` 行闭合，`p<=2000,row_stride=25` 抽样 `11583/11583`
条闭合。正式稿剩余义务：逐行证明 `TotalDescent-TM`，或证明任意非命中相位集合必触发
`SAE/PDEC/ColumnCRT`。不能把“与实证矛盾”写成最终逻辑；应写为“与有限基底验证和强归纳输入
`Row(h)` 矛盾”。

新增 `docs/monograph/prime-matrix-total-descent-h3-margin-route.md` 与固定 `h=3` 审计后，外审前可把
上述义务再压缩为 `H3-SixWheel-Roughness`。具体义务是：对任意相邻 `p<q`、任意 `2<=s<=q`，
证明 `I=[(s-1)q+1,sq]` 内完整 3 行的六轮候选不可能全部满足 `5<=P^-(c_R)<=p`。有限账本中
`p<=5000` 的 `1552462` 条 `q` 行全部有正余量，最小余量为 `1`；但这仍是计算证据，不是全局
证明。若正式稿不能直接证明该六轮余量不等式，就必须证明全阻断相位产生
`SAE/PDEC/ColumnCRT` 缺陷；不得把普通素数间隙定理或有限样本写成替代证明。

新增 `docs/monograph/prime-matrix-h3-sixwheel-hard-attack.md` 后，外审前的新增精确义务是：
把 `H3 Full-Blocking Defect Theorem` 逐行证明或标为条件输入。该定理必须在同一集合口径下证明
四分支覆盖：first-factor 高负载、分布式低模 PDEC 能量、稀疏端点 SAE、持久 ColumnCRT 位移。
若该四分支只被命名而未给阈值比较，则 Prime Matrix 行命题仍只能保持归约状态。

新增 `docs/monograph/prime-matrix-h3-full-blocking-defect-audit.md` 后，外审前还需把数据中出现的
小首因子骨架过载转为正式阈值：`5,7,11,13,...` 的聚合负载不能只作为经验表，应写成
`Tail/PDEC envelope` 的可验证上界；若不使用该上界，则必须证明多标签低模能量达到
`H3-PDEC` 阈值。

新增 `docs/monograph/prime-matrix-h3-small-factor-envelope-route.md` 后，外审前的最小义务进一步
具体化：必须证明 `SmallSkeletonOverload(y,K)=>Tail/PDEC`，或证明由
`K_y=ceil(R_y/(floor(q/ell_+(y))+1))` 强制出的多中尾标签给出 `H3-PDEC` 下界。该二分本身是
确定性组合账本；未闭合的是两个出口的阈值。

新增 `docs/monograph/prime-matrix-h3-global-scaling-law-route.md` 后，外审前还必须把尺度论证严证化：
Mertens 粗剩余尺度只能作为自然尺度和阈值设计依据，不能直接替代逐窗下界。正式稿需证明
“压灭 `q/log q` 尺度”必触发 Tail/PDEC、H3-PDEC 或 SAE/ColumnCRT 三出口之一。

新增 `docs/monograph/prime-matrix-h3-universal-scaling-inequality.md` 后，外审前必须避免把
`0.30*q/log q` 有限公式写成已证全局下界。可接受写法是缺陷版不等式：低于该尺度时，给出
SmallSkeletonOverload、ManyLabel-PDEC、Endpoint-SAE/ColumnCRT 的逐项证明。

新增 `docs/monograph/prime-matrix-h3-global-tail-energy-lemma.md` 后，上述“低于尺度时进入缺陷”的
组合部分已可逐行证明：`M_H3<B` 必推出小骨架过载 `C_y>#A_s-B-2L` 或尾标签低模能量
`E_y(d)>L`。外审前剩余义务应相应改写为两个出口证明，而不是继续要求证明三分支组合账本：
1. 证明 `SmallSkeletonOverload(y,B,L)=>Tail/PDEC` 的同口径阈值上界；
2. 证明 `TailEnergy(d,L)=>H3-PDEC/ColumnCRT` 的低模能量排斥。
这两个出口未闭合前，正文只能宣称全局确定性缺陷二分，不能宣称 H3/行命题无条件闭合。

新增 `docs/monograph/prime-matrix-h3-small-skeleton-pdec-bridge.md` 后，第 1 项已从“阈值上界”改写为
精确 PDEC 入口：`SmallSkeletonOverload` 推出 `D_y>V_y-B-2L`。外审前剩余不再是证明
`SmallSkeletonOverload` 会产生缺陷，而是证明该大小的 `D_y` 缺陷不能在坏窗集合中持续，或必须
进入既有 `PDEC/SAE/ColumnCRT` 排斥证书。

新增 `docs/monograph/prime-matrix-h3-tail-energy-fourier-bridge.md` 与
`docs/monograph/prime-matrix-h3-unified-defect-criterion.md` 后，外审前 H3 义务应最终改写为：
证明统一缺陷排斥 `D_y<=V_y-B-2L` 与 `F_y(d)<=dL`，或明确声明 H3 只达到条件闭合判据。
当前文稿不能把该判据误升格为无条件 H3/行命题，因为 `(D_y,F_y)` 的排斥正是最后深输入。

新增 `docs/monograph/prime-matrix-h3-first-row-scale-bridge.md` 后，外审表述可说明 `q/log q` 尺度已由
PNT 与相邻壳层单点性理论解释：H3 行平均为第一行素数数目的 `1/2+o(1)`。但这仍是平均尺度桥，
不是逐行下界；外审前仍需统一缺陷排斥才能宣称行命题闭合。

新增 `docs/monograph/prime-matrix-h3-pointwise-closure-boundary.md` 后，外审义务应精确写为：
证明点态第一行尺度转移 `M_H3(p,s)>=kappa*pi(q)`，或证明统一缺陷判据中的 `D_y/F_y` 排斥。
若两者都未证明，行命题必须保持未闭合。

新增 `docs/monograph/prime-matrix-h3-square-root-short-interval-barrier.md` 后，外审前必须承认：
上述点态转移是平方根长度短区间素数下界问题。除非提交新的 `Square-root Defect Exclusion`
证明，否则不得写成已完成无条件 H3/行命题。

新增 `docs/monograph/prime-matrix-h3-square-root-defect-exclusion-hard-attack.md` 后，外审义务应再细化：
`D_y` 分支可用标准区间筛处理；剩余必须证明尾标签/双粗补洞不可能精确填满整行，或必进入
ColumnCRT、端点相位、互补因子矛盾证书。

新增 `docs/monograph/prime-matrix-h3-tail-filler-rigidity-hardcore.md` 后，外审义务进一步收窄为：
把已证的相邻互质、二步互质、复用间距和三连短差值刚性拼成全局不相容性证明。当前尚未完成
该全局拼接排斥。

新增 `docs/monograph/prime-matrix-h3-tail-filler-global-chain-capacity.md` 后，该义务进一步定式化：
尾补洞连续块若被拼满，必须满足相邻边容量 `EdgeCap(B;y)=|B|-1` 与三连容量
`TriCap(B;y)=|B|-2`。外审前需补上的最后一层证明是：

```text
EdgeCap(B;y)<|B|-1 或 TriCap(B;y)<|B|-2，
除非满容量本身强制 PDEC/ColumnCRT/endpoint/cofactor 缺陷。
```

该容量判据是必要条件已证，不是无条件排斥已证；未补完前不能宣称 H3/行命题无条件闭合。

新增 `docs/monograph/prime-matrix-h3-tail-edge-selberg-exclusion.md` 后，容量排斥已有第一条
审稿级闭合分支：二维 Selberg 上筛给出

```text
满尾补洞连续块长度 <= 2 + A_*(theta)(q+6)/(log y)^2。
```

故宏观整行尾补洞分支已排除。外审前剩余义务相应收窄为：

```text
Short-block extraction / PDEC routing:
尾点若只能出现在许多短块中，则小骨架切割频率必须产生 D_y/PDEC 缺陷；
若不产生 D_y/PDEC，则短块端点、列位移或互补商必须产生 ColumnCRT/endpoint/cofactor 缺陷。
```

此外还需把二维上筛常数 `A_delta(theta)` 显式引用或内联 Selberg 二次型证明，才能升级为
完全显式阈值版。

新增 `docs/monograph/prime-matrix-h3-shortblock-singleton-barrier.md` 后，需修正外审义务表述：
短块化并不自动产生 PDEC。精确恒等式 `T=J+E` 显示，二维上筛控制内部相邻尾边 `E` 后，
尾质量主要转移到单点尾块。由于小骨架自然为 `q` 级，不能把 `J~q/log y` 个切割点直接宣称为
异常。外审前真正剩余义务是：

```text
Singleton Tail Exclusion:
大量孤立 y-rough 尾点若全部为合数，则尾标签 ell>y 与左右小骨架标签 r_-,r_+<=y
形成的夹逼相位系统必须触发 PDEC/ColumnCRT/endpoint/cofactor 缺陷。
```

若该单点尾块排斥未证明，H3/行命题仍不能宣称无条件闭合。

新增 `docs/monograph/prime-matrix-h3-singleton-clamp-defect-criterion.md` 后，外审义务进一步精确：
孤立尾点的左右夹逼相位已可逐行审查。固定夹逼单元 `c=(delta_-,delta_+,r_-,r_+)` 后，
所有点落入 `rho(c) mod lcm(r_-,r_+)`；再加尾标签 `ell>y` 后落入模
`ell*lcm(r_-,r_+)` 的唯一类。因此大量孤立尾点必须满足三分支：

```text
Tail-label concentration / Clamp low-mod concentration / Distributed singleton capacity.
```

前两项是命名缺陷入口；外审前剩余是第三项，即分散容量中素数与双粗半素数的有符号分离。
该项未证明前，不能把夹逼 CRT 容量误写成 Singleton Tail Exclusion 的无条件证明。

新增 `docs/monograph/prime-matrix-h3-distributed-singleton-bilinear-obstruction.md` 后，第三项被
精确双线性化。外审前剩余义务应改写为：

```text
H3 Distributed Singleton Bilinear Exclusion:
对 y>q^(2/3) 的分散孤立尾点，证明
sum Delta(c)=O(q/log^2 y)，
或证明 q/log y 级正异常必触发 endpoint/PDEC/ColumnCRT/cofactor。
```

这里 `Delta(c)` 是夹逼单元中半素数通道减素数幸存通道；半素数通道等价于互补商短区间中
`m≡ell^{-1}rho(c) mod R(c)` 的素数计数。该有符号短互补商估计未证明前，H3/行命题仍保持
条件闭合。

新增 `docs/monograph/prime-matrix-h3-bilinear-large-sieve-defect-bridge.md` 后，上述估计被
进一步压缩为非主角色频率缺陷。外审前最后义务应写为：

```text
H3-DSB-LS/KLS:
对夹逼模 R(c) 与短互补商窗口 I/ell，
证明非主角色双线性和满足 O(q/log^2 y)，
或证明任意 q/log y 级频率异常触发 PDEC/ColumnCRT/cofactor。
```

普通大筛不足以直接给出该界；若引用外部 dispersion/Kloosterman 型定理，必须逐项核验
模数范围、短窗口长度、素数权、平滑截断和角色相位 `conj(chi(ell))*chi(m)`。

新增 `docs/monograph/prime-matrix-h3-dsb-kloosterman-window-reduction.md` 后，最后义务变为
Kloosterman 窗口适配核查：

```text
m≡rho*bar(ell) mod R
=> e(-h*rho*bar(ell)/R) Kloosterman kernel.
```

外审前必须逐项处理四个分支：

1. `KLS-window` 是否覆盖 `R(c)`、`h`、短窗口 `I/ell` 与素数权；
2. `high-lcm clamp` 是否能并入夹逼低模/端点/cofactor 缺陷；
3. `high-frequency endpoint` 是否能由 sawtooth 尾项预算吸收；
4. 系数二范数过大是否等价于 tail-label 或 clamp concentration。

这些分支未逐项证明前，不能把 DI/BFI 的名字直接写成 H3 行命题闭合。

新增 `docs/monograph/prime-matrix-h3-dsb-high-lcm-clamp-routing.md` 后，第 2 项已被进一步
路由而不是闭合：高 `R(c)` 单元一行容量为 `1+floor((q+O(1))/R_0)`，所以若承载
`q/log y` 级质量，必有大量稀疏高 `lcm` 单元。该分支只有两个合法出口：

```text
Persistent-HLC => PDEC/ColumnCRT 非零 Fourier/CRT 缺陷；
Sparse-HLC     => SAE 单窗逃逸。
```

外审前剩余因此改写为：排除 `Persistent-HLC` 与 `Sparse-HLC` 两个出口，或明确保留为
条件输入；不能再把 high-lcm 质量混入低模 `KLS-window` 主估计。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-fourier-energy-clamp.md` 后，`Persistent-HLC`
与 `Sparse-HLC` 又合并到同一个能量注入公式：同模相位块有

```text
sum_{h!=0}|muhat(h)|^2 = R*sum_a mu(a)^2 - U^2 >= R*U/2    若 U<=R/2。
```

因此外审前不再需要接受“高 lcm 无结构逃逸”作为独立缺口。剩余审稿义务更窄：
证明上述能量在持久情形必被 `PDEC/ColumnCRT` 排斥，在单窗情形必被 `SAE/endpoint`
排斥；未证明前只能称为出口压缩，不能称 H3 无条件闭合。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-pdec-threshold-bridge.md` 后，持久情形的下界
已经变成可审稿阈值：

```text
L_HLC(B)=sqrt((R*sum_a g_B(a)^2-U_B^2)/(R-1)).
```

稀疏区 `U_B<=R/2` 自动给 `L_HLC>=sqrt(R U_B/(2(R-1)))`；稠密区 `U_B>R/2`
不再作为 high-lcm 分散逃逸，而必须回到 KLS、PDEC/ColumnCRT 或 SAE/endpoint。
外审前真正剩余是：逐个 HLC formal unit 证明同口径上界 `U_CRT(B)<L_HLC(B)`，
或输出失败频率、相位主贡献与回流出口。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-pdec-failure-localization.md` 后，失败输出有了
定量下界：若 `sum g(a)Re(zeta e(ha/R))>=L`，则 Bohr-cap
`C_alpha={a:Re(zeta e(ha/R))>=alpha}` 的质量满足
`G_alpha>=(L-alpha U)/(1-alpha)`。外审前剩余因此更具体：对这些帽集中逐项证明
持久帽可加入 PDEC 约束并通过，或孤立帽由 SAE/endpoint 排除。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-bohr-cap-component-route.md` 后，帽集中还需按
`d=(h,R)` 拆成 high-gcd 与 short-arc 两类。外审前应要求：大 `d` 被证明为低有效模
PDEC/ColumnCRT 集中，小 `d` 的短弧组件被物化为通过的 PDEC 行或 SAE/endpoint 证书。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-high-gcd-descent.md` 后，大 `d` 已有严格下降：
外审前不应再把 high-gcd 作为独立缺口；只需审查下降后的低有效模 PDEC/KLS 出口和
short-arc 组件出口。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-short-arc-density-pressure.md` 后，short-arc
出口应按密度压力审查：若压力 `>1+epsilon`，必须给出 PDEC 局部密度行或 SAE/endpoint
证书；若压力 `<=1+epsilon`，必须列出参数残余区并说明由 KLS/PDEC/SAE 哪一项覆盖。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-short-arc-pressure-optimizer.md` 后，参数残余区
已有精确格式：`Psi_{D0,R}(L/U)<=1+epsilon`，并推出 L2 平坦性。外审前剩余应改为：
给出有限 `lambda` 压力证书，或逐项核验 L2-flat residual 满足 KLS-window 的系数范数条件。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-l2-flat-kls-admission.md` 后，外审前应按 K1--K6
核查 HLC L2-flat residual。不能只说“平坦所以 KLS 可用”；必须逐项确认模数、频率、端点、
二范数、gcd/unit 和分块条件，或把失败项路由到对应出口。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-clean-kls-reduction.md` 后，K1--K6 核验已可
压缩为 clean-unit 判定：若 E1--E6 均无，则 K1--K6 通过。外审前剩余变为逐项引用或证明
`HLC-KLS-ext` 覆盖 clean HLC 的 `(CKR-4)` 窗口和。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kls-external-adaptation.md` 后，外部深定理版
的逐项引用适配已完成：`(CKR-4)` 的逆元相位、低有效模 dyadic level、有效频率、短窗口
平滑、`Lambda(m)` 分解、L2-flat 系数、gcd/unit 层和分块损失都已列入同一核查表。
因此外审义务应区分为两类：

```text
external-theorem version:
  核对 DI/BFI/Kuznetsov 原文定理号和窗口化版本，即可审查 HLC-KLS-ext 调用；
self-contained version:
  仍需在本文内重证相应窗口化谱/dispersion 定理。
```

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kls-core-reduction.md` 后，上述 self-contained
义务进一步改写为：

```text
prove HLC-KLS-core (CORE-5):
  for every clean dyadic/Type block D,
  |S(D)| <= N(D)/log^A y.
```

该文件已经证明 `HLC-KLS-core => HLC-KLS-ext`，所以外审前不应再把 HLC clean 分支写成
多个模糊解析缺口；它只有一个精确缺口 `(CORE-5)`，以及一个书目动作：找出可直接推出
`(CORE-5)` 的外部定理并核对变量。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kls-core-self-contained-spine.md` 后，外审前义务
继续收窄：

```text
prove Kuznetsov-LS atom (SC-9)
or cite an external theorem that implies it.
```

该文已完成 `SC-9=>CORE-5` 和点态 Weil 不足审查。若作者要宣称完全自足闭合，必须继续
补 Kuznetsov trace formula、Bessel transform bounds、spectral large sieve 与本文窗口的
参数专门化，不能只写“由谱理论可得”。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kuznetsov-ls-atom-expansion.md` 后，外审义务
被拆成以下精确清单：

```text
KZ-B: Kuznetsov trace formula specialization;
KZ-C: Bessel transform decay;
KZ-D: spectral large sieve with oldform/Eisenstein;
KZ-E: BFI/well-factorable dispersion logarithmic saving.
```

该文件已证明 KZ-A--KZ-E 合起来推出 `SC-9`。作者若继续无黑箱化，必须逐项补这四个子原子。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kz-c-bessel-transform-decay.md` 后，KZ-C 已补齐。
外审前剩余清单缩为：

```text
KZ-B: Kuznetsov trace formula specialization;
KZ-D: spectral large sieve with oldform/Eisenstein;
KZ-E: BFI/well-factorable dispersion logarithmic saving.
```

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kz-d-spectral-large-sieve-spine.md` 后，KZ-D
继续收窄为：

```text
PTK-D: pretrace kernel bound (diagonal T^2 plus off-diagonal N0 Schur rows/columns).
```

oldform、Eisenstein、holomorphic 谱已经进入多对数账本；外审前剩余不应再笼统写
“spectral large sieve”，而应写 PTK-D。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-ptk-d-pretrace-kernel-bound.md` 后，PTK-D 继续
收窄为：

```text
LPC-D: spatial lattice-point/correlation Schur row-column bound.
```

该文已证明 `LPC-D=>PTK-D`。外审前若继续无黑箱化，应直接补空间侧格点/相关计数。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-lpc-d-spatial-correlation-split.md` 后，LPC-D
继续收窄为：

```text
GHLC-D: generic hyperbolic local correlation row-column bound.
```

FAR、ID-near、PAR 三个空间分支已经处理；外审前应直接补 generic hyperbolic 近距离格点
相关计数。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-ghlc-d-local-schur-closure.md` 后，上述
GHLC-D 已闭合。关键是不用点态格点计数，而在预迹积分核层使用局部 `L^1` 质量
`T^2∫_0^{T^{-1}log^B y}(1+Tr)^{-A}sinh r dr=O(1)` 与 Poincare 包 Schur 归一化。
因此外审前 HLC 无黑箱剩余清单更新为：

```text
KZ-B: Kuznetsov trace formula specialization;
KZ-E: BFI/well-factorable dispersion logarithmic saving.
```

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kz-b-kuznetsov-trace-specialization.md` 后，KZ-B
已内联推导。几何侧由 Poincare 包 unfolding 和双陪集分解给出 Kloosterman 模数和；谱侧由
automorphic kernel 的 Plancherel 展开给出 Maass/holomorphic/Eisenstein 项；Bessel 变换
归一化与 KZ-C 相接。因此当前 HLC 完全自足剩余清单进一步缩为：

```text
KZ-E: BFI/well-factorable dispersion logarithmic saving.
```

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kz-e-well-factorable-dispersion-spine.md` 后，KZ-E
的非深账本已内联：well-factorable 分解、dispersion 方差恒等式、CRT 相位、gcd 相容层、
端点和平滑损失。外审前 HLC 完全自足剩余清单进一步缩为：

```text
WFD-core: windowed well-factorable Kloosterman dispersion mean estimate.
```

该项是当前唯一不得省略的深平均估计。若只引用 BFI/DI，则可作为外部深定理版；若要求完全
自足，必须继续逐行证明 WFD-core。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-wfd-core-balanced-factor-reduction.md` 后，WFD-core
已平方根平衡化。外审前 HLC 完全自足剩余清单进一步缩为：

```text
BWFD-core: balanced two-modulus well-factorable Kloosterman dispersion mean estimate.
```

该项要求直接处理 `u,v≈C^{1/2}` 的双模数 Kloosterman 相位平均；筛权分解、gcd 剥离和 CRT
归一化已经不再是剩余义务。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-bwfd-core-spectral-completion-attack.md` 后，BWFD-core
已完成化为完整 Kloosterman 双线性相关。外审前 HLC 完全自足剩余清单进一步缩为：

```text
BSC-core: balanced complete Kloosterman bilinear correlation logarithmic saving.
```

该项当时要求证明 `(BSA-13)` 的任意对数节省；普通谱大筛 KZ-D 和点态 Weil 已在该文件中核定为
只能给 raw 尺度或单点平方根抵消，不能替代 BSC-core。后续分数相位攻击已进一步压缩该点。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-bsc-core-kloosterman-fraction-attack.md` 后，BSC-core
已展开为互逆 Kloosterman 分数相位。外审前 HLC 完全自足剩余清单进一步缩为：

```text
KFLS-core: balanced Kloosterman-fraction large sieve logarithmic saving.
```

该项要求直接证明 `(KFA-17a)`--`(KFA-17b)`；也就是在 `u,v≈C^{1/2}` 的双模数族上控制
`e(\bar vR/u+\bar uT/v)` 的非退化平均抵消。

新增 `docs/monograph/prime-matrix-rpz-absorption-defect-route.md`、
`docs/monograph/prime-matrix-rpz-absorption-defect-audit.md` 与
`experiments/prime_matrix_rpz_absorption_defect_audit.py` 后，复活点吸收定理已被改写为
`survivor/TailAnchor/ColumnCRT/ColumnRadius/Distributed-RPZ` 五分支路由。有限样本显示
单窗吸收是分散型，最大标签负载和最大顶层列负载均为 `1`。因此外审前剩余不是简单
`RPZ-Absorption=>TailAnchor`，而是必须证明 `Distributed-RPZ` 低负载分散吸收不能持续，
或提交它进入 `ColumnCRT/ColumnRadius/TailAnchor` 的容量不等式。

新增 `docs/monograph/prime-matrix-rpz-sliding-plateau-barrier.md`、
`docs/monograph/prime-matrix-rpz-sliding-plateau-audit.md` 与
`experiments/prime_matrix_rpz_sliding_plateau_audit.py` 后，连续滑动平台中的非边界复活源
会以平台长度重复出现，形成持久源 TailAnchor；同批样本在 `T_0=4` 下 `5/5` 触发。
因此外审前剩余进一步收窄为 `RPZ-BCB`：排除源删除后的边界压缩逃逸，或证明它进入
`SAE/PDEC/ColumnCRT`。

新增 `docs/monograph/prime-matrix-rpz-boundary-compressed-core-route.md`、
`docs/monograph/prime-matrix-rpz-bcb-core-audit.md` 与
`experiments/prime_matrix_rpz_bcb_core_audit.py` 后，边界压缩分支已转化为强制中心零区间：
若无 TailAnchor，则 `J_{T0}` 是半宽 `h`-筛零区间。有限审计显示中心幸存者全为尾锚核心源；
条件删除后 `5/5` 中心区间含完整半宽行。外审前剩余进一步收窄为
`BCB-Grid/Endpoint exclusion`，即下层对齐零行或端点 seam 缺陷的最终处理。

新增 `docs/monograph/prime-matrix-rpz-bcb-grid-endpoint-criterion.md`、
`docs/monograph/prime-matrix-rpz-bcb-grid-endpoint-audit.md` 与
`experiments/prime_matrix_rpz_bcb_grid_endpoint_audit.py` 后，`BCB-Grid` 的几何判据已逐行证明：
`J=[u,v]` 含完整 `h` 行当且仅当 `N>=delta_h(u)+h`。同批样本 `5/5` 满足，端点缺陷为 `0`。
外审前剩余进一步收窄为 `BCB-Endpoint persistence exclusion`：若该判据失败，端点相位必须进入
`SAE/PDEC/ColumnCRT`，不能作为未命名逃逸。

新增 `docs/monograph/prime-matrix-rpz-bcb-endpoint-persistence-route.md`、
`docs/monograph/prime-matrix-rpz-bcb-endpoint-phase-ledger.md` 与
`experiments/prime_matrix_rpz_bcb_endpoint_phase_ledger.py` 后，端点失败已经完成命名路由：
稀疏端点失败进入 `SAE`，持久同相失败进入 `PDEC/ColumnCRT`。该项仍不排除这些出口；
但外审义务已从“端点失败是否还有第三逃逸”收窄为 `SAE/PDEC/ColumnCRT` 证书闭合或下层递归下降。

新增 `docs/monograph/prime-matrix-rpz-dual-track-closure-route.md`、
`docs/monograph/prime-matrix-rpz-lower-zero-descent-audit.md` 与
`experiments/prime_matrix_rpz_lower_zero_descent_audit.py` 后，双轨义务已明确：
一边物化 `RPZ-SAE/RPZ-PDEC/RPZ-ColumnCRT` 证书，一边证明下层零行下降网格条件。
有限审计显示样本 `6/6` 条件下层零行下降到 `p=2` 矛盾；全局外审前仍需证明该下降不被
端点穿孔/网格缺口阻断，或把阻断送入上述证书接口。

新增 `docs/monograph/prime-matrix-rpz-lower-descent-obstruction-ledger.md`、对应 JSON 与
`experiments/prime_matrix_rpz_lower_descent_obstruction_ledger.py` 后，端点穿孔/网格缺口已被改写为
有限相位账本：`grid_fail` 与 `puncture_block`。本批实际下降转换 `20` 个全部为 `success`，
实际阻断为 `0`。新增 `docs/monograph/prime-matrix-rpz-certificate-materialization-interface.md`
把所有阻断相位接入 `RPZ-SAE-FIN/PDEC/ColumnCRT` 三类证书。外审前剩余不再是“阻断是否可命名”，
而是必须证明正式反例下降避开阻断相位，或填写并核验这些证书。

新增 `docs/monograph/prime-matrix-rpz-certificate-skeleton-package.md`、对应 JSON 与
`experiments/prime_matrix_rpz_certificate_skeleton_builder.py` 后，证书行已经材料化：`2` 个
endpoint `RPZ-SAE-FIN` 候选、`2` 条 endpoint `PDEC/ColumnCRT` 行、`3` 条 lower-descent
`grid_fail` 的 `PDEC/ColumnCRT` 行。外审前作者仍需填写这些证书；当前文件只固定义务，
不宣称排除。

新增 `docs/monograph/prime-matrix-rpz-endpoint-sae-finite-certificate.md`、对应 JSON 与
`experiments/prime_matrix_rpz_endpoint_sae_finite_certificate.py` 后，当前有限 BCB 账本中两个
endpoint SAE 候选均无实际窗口：possible load 为 `2`，actual load 为 `0`。因此当前账本的
endpoint SAE-FIN 行已真空闭合；全局 SAE 排斥仍未完成，下一硬点转为 lower-descent
`grid_fail` 三条相位行。

新增 `docs/monograph/prime-matrix-rpz-lower-grid-fail-avoidance-certificate.md`、对应 JSON 与
`experiments/prime_matrix_rpz_lower_grid_fail_avoidance_certificate.py` 后，`grid_fail` 三条相位行
具有闭式判据 `delta=-(a-1)(p-r) mod r` 且 `grid_success iff delta<=p-r`。当前实际下降节点
`20` 个全部避开该失败相位；这闭合当前账本，不闭合全局正式路径。外审前剩余是证明正式路径
全局满足该相位不等式，或提交 `PDEC/ColumnCRT` 排斥证书。

新增 `docs/monograph/prime-matrix-rpz-formal-descent-phase-inequality.md` 后，外审表述需更精确：
若正式下降路径已经存在，则 `delta<=p-r` 是定义和网格判据的推论；未闭合的是路径存在性。
如果路径不存在，第一处失败必为有限相位首阻断，并进入 `SAE/PDEC/ColumnCRT`。因此外审前
剩余应写为“证明路径存在或排除首阻断相位证书”，而不是重复证明已存在路径的相位不等式。

新增 `docs/monograph/prime-matrix-rpz-first-obstruction-dichotomy.md` 后，首阻断类型进一步唯一化：
端点穿孔不可能阻断完整下层行，所以不存在 `puncture_block` 第三逃逸。外审前剩余压缩为：
排除 first-grid-fail seam 相位的 `SAE/PDEC/ColumnCRT` 证书。

新增 `docs/monograph/prime-matrix-rpz-first-grid-fail-seam-certificate.md`、对应 JSON 与脚本
`experiments/prime_matrix_rpz_first_grid_fail_seam_certificate.py` 后，first-grid-fail seam 已有
双帽标准形和机器账本：`12` 个 seam 相位行、完整 `Q` 中 `1752` 个相位、源计数不一致为 `0`。
其中 `1348` 个端点相位已由下层标签杀死，`404` 个 unit endpoint 相位仍需处理。
新增 `docs/monograph/prime-matrix-rpz-unit-endpoint-columncrt-gate.md` 后，`404` 个 unit endpoint
相位被压缩为 `12` 条固定非零位移 `ColumnCRT` 门控行，且当前账本 `12/12` 有显式同列素数见证。
外审前剩余进一步变为：证明正式反例族映入这些门控行并排除对应 `ColumnCRTDefect(p,d)` 阈值，
或证明正式反例族避开 unit endpoint seam。

新增 `docs/monograph/prime-matrix-rpz-columncrt-threshold-obstruction.md` 后，阈值路线的限制已明确：
固定 unit gate 的全部 unit residues 自身已经落入同一个 `(p,d)` 类，内禀负载为
`prod_{ell<r}(ell-1)`；当前最大为 `48`。因此 `L_D=2` 只会触发 `ColumnCRTDefect`，不是排除。
外审前若要闭合该项，必须给出独立 `ColumnCRTDefect` 排斥、endpoint-PDEC 上界，或 formal-family
避开定理。

新增 `docs/monograph/prime-matrix-rpz-three-route-closure-audit.md` 后，三条路线的外审优先级固定为：
formal-family 避开优先，其次 endpoint-PDEC，上述两者都失败时才转独立 `ColumnCRTDefect`
排斥定理。当前没有路线已全局闭合。

新增 `docs/monograph/prime-matrix-rpz-formal-phase-automaton.md` 后，formal-family 避开路线的外审义务
具体化为起始相位准入：证明任意 formal-family 起始相位属于自动机接受集 `A_p`。当前账本
`6/6` 起始行被接受，但这仍不是全局证明。

新增 `docs/monograph/prime-matrix-rpz-rejected-phase-absorption.md` 后，自动机拒绝集的外审义务也被
材料化：`27924` 个 rejected phase 全部追踪到 `12` 条已物化 first-grid-fail seam，未覆盖样例为
`0`。外审前剩余不再是 rejected set 未命名，而是 seam/PDEC/ColumnCRT 出口排斥。

新增 `docs/monograph/prime-matrix-rpz-seam-exit-pressure-ledger.md` 后，该出口排斥义务已被压成
可逐行审查的窄接口：`12` 条 seam 行、`1348` 个下层标签已杀死端点、`404` 个 unit endpoint
相位、`10` 个固定非零 ColumnCRT 位移类，最大聚合位移负载为 `96`。外审前不能再把该项写成
“继续查 rejected phase”；必须提交 formal-family 避开定理、endpoint-PDEC 上界，或独立
`ColumnCRTDefect` 排斥定理。

新增 `docs/monograph/prime-matrix-rpz-symbolic-ladder-certificate.md` 后，formal-family 避开定理的
外审表述变成逐层数字不等式：对相邻素数 `p>r` 与 `g=p-r`，必须证明正式起始相位沿 canonical
下降链满足 `delta_p(a)=-(a-1)g mod r <= g`。该证书已在 `P(19)=9699690` 内枚举核验计数公式，
但仍未证明正式反例族必满足这些数字约束。

新增 `docs/monograph/prime-matrix-rpz-bcb-start-digit-ledger.md` 后，当前 BCB 样本的 `20` 个
digit 节点全部安全，但 `10` 个节点正好位于 `margin=0`。外审前应明确：formal-family
避开不能用粗余量替代，必须给出 `start_row mod r` 的精确同余推导。

新增 `docs/monograph/prime-matrix-rpz-bcb-accepted-row-selector.md` 后，外审义务可改写为更弱的
selector 存在定理：对正式 BCB 核心区间 `J`，证明完整下层候选行集合 `C_h(J)` 与 accepted set
`A_h` 相交。当前样本 `5/5` 有 selector、`6/6` 候选行 accepted；但全局 selector 存在仍未证明。

新增 `docs/monograph/prime-matrix-rpz-selector-gap-threshold.md` 后，selector 存在义务拆成长度分支
与短候选端点相位分支。当前样本只有 `2/5` 可由长度自动保证，`3/5` 必须证明端点相位避开
`A_h` 的 rejected gaps。

新增 `docs/monograph/prime-matrix-rpz-short-candidate-phase-ledger.md` 后，短候选分支已被精确化：
实际 `3/3` 个短候选样本均命中 selector，但完整 `u mod hP(h)` 相位族中仍有 all-rejected
相位。外审前不能把“当前样本安全”写成“任意短相位安全”；必须证明正式 BCB 端点相位不落入
all-rejected 类，或把这些类逐项送入 seam/PDEC/ColumnCRT 证书闭合。

新增 `docs/monograph/prime-matrix-rpz-short-phase-block-formula.md` 后，all-rejected 类已由块公式
替代枚举：当 `length<2h` 时，rejected 行相位 `m mod P(h)` 给出端点禁区
`mh-length+1 <= u <= (m-1)h+1`。当前三族公式全部匹配枚举，实际端点到禁区集合距离为正。
外审剩余不再是端点集合计算，而是证明正式 BCB 构造诱导的候选行相位属于 `A_h`，或闭合其
first-failure 出口。

新增 `docs/monograph/prime-matrix-rpz-bcb-candidate-phase-identity.md` 后，候选行相位不再是
程序扫描黑箱，而是由 BCB 参数的 floor 身份给出。当前 `5/5` 条样本匹配核心区间与候选行，
`6/6` 个候选行相位 accepted。外审前最后剩余输入是全局 residue implication：
正式 BCB 反例的 `R mod hP(h)` 必须推出候选行相位属于 `A_h`；否则该 rejected 相位必须
接入 first-failure seam/PDEC/ColumnCRT 证书。

新增 `docs/monograph/prime-matrix-rpz-bcb-accepted-preimage-ledger.md` 后，该 residue implication
的当前参数族 preimage 已显式化：实际样本全部在 selector preimage 中，但四个参数族仍存在
bad residue。因此外审前仍需证明正式反例不能取这些 bad residue；若能取，则必须分别闭合
`no_candidate` 的 BCB endpoint 出口或 `all_rejected` 的 first-failure 出口证书。

新增 `docs/monograph/prime-matrix-rpz-bcb-core-run-obstruction.md` 后，当前 BCB no-TailAnchor
样本可由低筛最大连续覆盖长度直接排斥：`|J_T0|` 分别为 `9,13,15,19,25`，对应 `h=5,7,7,11,13`
的最大低筛覆盖长度为 `5,9,9,13,21`。外审前需要把这一有限账本升级为 formal 层的
Jacobsthal 型上界，或保留 endpoint/first-failure/PDEC/ColumnCRT 出口闭合义务。

新增 `docs/monograph/prime-matrix-rpz-bcb-jacobsthal-closure-interface.md` 后，外审义务可表述为：
对正式 BCB 参数 `(P,h,m,T)`，证明 `G(h)<P+m-1-2T`，其中 `G(h)` 是 `h` 层低筛最大连续
覆盖长度。该条件闭合 no-TailAnchor BCB 分支；未证明前，不得把当前 finite 样本闭合推广为
全局闭合。

新增 `docs/monograph/prime-matrix-rpz-bcb-jacobsthal-risk-scan.md` 后，外审义务更严格：
不能把 `G(h)<P-4` 作为全局证书，因为风险扫描在 `h=43` 已出现失败。作者必须补充
formal BCB 平台长度增长定理，或把这些失败层路由到 TailAnchor/endpoint/first-failure 出口。

新增 `docs/monograph/prime-matrix-rpz-bcb-platform-length-threshold.md` 后，平台长度增长定理的精确
形式是 `m>=G(h)-P+2+2T`。外审前若不能证明该不等式覆盖 formal BCB 参数，则必须保留短平台
出口闭合义务。

新增 `docs/monograph/prime-matrix-rpz-bcb-short-platform-embedding-route.md` 后，短平台出口已被压成
有限 Jacobsthal endpoint set `E_{h,N}`。外审前仍需生成 `E_{h,N}` 的显式证书，或证明这些相位
进入并闭合 `SAE/PDEC/ColumnCRT`。

新增 `docs/monograph/prime-matrix-rpz-bcb-short-platform-embedding-certificate.md` 后，最长块端点
子族 `Emax_{h,N}` 已有可重算证书：`1197` 个最长块通过 CRT 重建与边界验证。剩余义务更精确：
完整 `E_{h,N}` 尚未枚举；必须证明所有长度 `>=N` 的覆盖块归入最长块相位族，或补一个完整覆盖块
枚举/证明，再进入 `SAE/PDEC/ColumnCRT`。

新增 `docs/monograph/prime-matrix-crt-lift-parity-audit.md` 后，q 阶零行向 p 阶 CRT 周期提升的
奇偶矛盾路线不能作为闭合证明：旧周期零行数本身已由镜像成偶数，乘以奇数 `q` 后仍为偶数。
外审前可使用的版本只能是早期旧筛 q 零窗下降，并继续排斥完整 p 行支与缝合零窗支。

新增 `docs/monograph/prime-matrix-recursive-mirror-descent-audit.md` 后，递归镜像下降也不能作为
闭合证明：全周期零行、剥层后零行、实际小方阵早期零行是三种不同对象。外审前若使用该路线，
必须把目标明确写成“早期缝合零窗排斥/端点 CRT 缺陷”，不能写成“镜像偶性递归推出小方阵零行”。

新增 `docs/monograph/prime-matrix-annulus-mirror-localization-audit.md` 后，环带镜像路线还需避免
混用两种镜像：`-n mod M_p` 保持零同余但落在 CRT 周期尾部；`q^2-n` 落到早期但变成非零类
终端镜像块。外审前不能把后者写成更小素数方阵零行。

新增 `docs/monograph/h4-pdec-column-defect-routing-contract.md` 后，
`ColumnRadius/ColumnCRT` 的条件路由元数据已定式化：半径缺陷使用
`D_0`、列见证选择器和相位兼容权重 `W_D(t)`；位移余类缺陷使用标签 `ell`、非零余类 `a`、
阈值 `L_D` 和相位兼容权重 `W_{ell,a}(t)`。该项允许在剥离这些出口后的分支中加入
`R_D(g)<=0` 与 `R_{ell,a}(g)<=L_D`。它仍不排除这些出口；外审前还需物化权重并证明
阈值或提交排斥证书。

新增 `experiments/prime_matrix_h4_pdec_column_defect_weight_certificate.py` 与
`docs/monograph/h4-pdec-column-defect-weight-certificate.json/md` 后，`p<=1000` 紧行域的
两条有限权重已物化：`tau_fin=(p,q,row)` 上共有 `835` 个相位，`D_col>81` 与
位移余类负载 `>2` 的异常块均为空。该项解决的是有限相位兼容权重物化，不是全局
`D_0,L_D` 解析阈值或出口排斥。

### PM-E. RSE/RRD/OSPC 常数链

当前最窄常数账本为：

\[
C_{\mathrm{RRD}}+C_{\mathrm{OSPC}}+C_{\mathrm{SelbergUniform}}+C_{\mathrm{round}}
<0.053369509758272926.
\]

外审前必须逐项完成：

1. `RRD-low<=0.006` 或失败触发加权 CRT 缺陷。
2. `RRD-perp<=0.012` 的同权正交上界。
3. `RRD-conversion<=0.002` 的 convention 换算。
4. `OSPC<=0.020` 的有向出口排斥。
5. `SelbergUniform<=0.008` 的 `P>=P0` 统一矩常数。
6. `C_round<=0.003` 的外向舍入/区间化误差。

当前风险：多个文档给出了样本余量和有理审计，但顶刊外审需要无限范围统一常数，而不只是样本证书。

## 3. 二点筛 A/B 命题剩余义务

### TP-A. 状态边界

已经闭合：

1. `p∤x(x-w)` 与 `p∤x(w-x)` 等价。
2. 若二点断言对充分大 `P` 成立，则固定差素数对成立；`w=2` 推出孪生素数。

未闭合：

1. 二点断言本身。
2. I3-Core 真残余相关定理。
3. `BMD=>BST-2=>BST=>TLI` 是否无隐藏下界。

### TP-B. I3-Core 必须拆成可审查定理

当前主稿把二点筛条件链压到 I3-Core。外审前应把 I3-Core 分解为以下定理环境：

| 编号 | 定理义务 | 关键检查 |
|---|---|---|
| I3-1 | True-residual new-modulus balance | 排除真实剩余集中在某个新素数 `0,w` 类 |
| I3-2 | TCA linear bridge | 总覆盖超标如何转成块级正部；常数损失必须小于余量 |
| I3-3 | SC2 near-crossing bound | 固定阶近交叉误差；不能依赖完整 primorial 周期 |
| I3-4 | 45-Main synchronization削峰 | Reuse/Shared/Good 三分；Good 必须推出 Fourier CRTDefect |
| I3-5 | Directional Balance | 非零 Fourier 缺陷到短差值方向偏差，再排除 |
| I3-6 | Zero Mass | Bonferroni 零块质量与 `M1,M2,M3` 来源 |
| I3-7 | Endpoint/Smoothing | 平滑到 sharp 的端点层损失 |
| I3-8 | `q|w` collapse ledger | 固定 `w` 下局部一禁类/二禁类常数统一 |

当前风险：普通上界筛不能替代真实剩余下界；若某步需要 `|U_Y|` 的强下界，必须显式标为 parity-barrier 型缺口。

### TP-C. DI/BFI 外部深定理适配

若主稿声称二点筛某个子链为 `External-theorem closed`，必须完成：

1. 把 DI 谱 Kloosterman 大筛写成可引用定理模板。
2. 把 BFI dispersion/well-factorable 权重写成可引用定理模板。
3. 把 KLS-window 变量逐项填入模板：相位、模数、频率、逆元变量、权重、gcd 层、端点平滑、目标强度。
4. 建立 `B(A)` 对数损失吸收账本。
5. 区分“引用 DI/BFI 后闭合”和“完全自足重证 KLS-window”。

当前风险：外部定理适配若只写“由 DI/BFI 得到”，不足以通过顶刊审稿。

### TP-D. BMD 到 TLI 无隐藏下界审查

这是二点筛最重要的实质审查。必须证明：

1. `BMD` 控制的是有符号/加权乘法曲线分布，而不仅是零截面非空。
2. `BST-2/BST` 的 Buchstab 半素数转移没有偷偷使用素数对下界。
3. `TLI` 的分母 `|U_Y|` 来自已证的真实剩余质量或可避免除以未知下界。
4. 所有主项常数在同一奇异级数 convention 下比较。
5. hardest case `w=2` 中 `K(alpha)` 半素数常数与误差项有严格上下界，而非实验拟合。

若上述任一项不能闭合，二点筛终局必须标为 `Buchstab-transfer parity gap` 或 `conditional`.

## 4. RH 方向剩余义务

RH 章节必须保持 verification package 状态。外审前应完成：

1. **PC1 显式公式入口**：平滑核、零点贡献、素数幂剥离、误差项逐项写入。
2. **PC2 CRT baseline transfer**：候选账本与素数账本转换使用同一 baseline convention。
3. **C3/C4/C5 分解不重不漏**：sparse/dense/tail/internal/global exits 的覆盖关系必须形式化。
4. **C6 no-cycle**：Lyapunov 或势函数下降必须给出良基性和源删除规则。
5. **C9 tail**：Vaaler/Fourier 高尾截断、KL/BG/Baker 输入必须精确引用。
6. **AEX/GEE**：每个 controlled exit 必须给出 load lower bound 与 capacity upper bound。
7. **全局矛盾**：所有上下界必须在同一 normalization 下相矛盾。

当前风险：RH 链条不应通过方阵或二点筛局部刚性“类比升级”；唯一可审稿路径是 controlled exits 的定理化或转成明确正性二次型。

## 5. 合著稿工程与证据等级义务

外审前必须完成的文稿工程：

1. **定理环境分级**：将 `Proved-in-text`、`Reduction-closed`、`External-theorem closed`、`Referee-block`、`Not claimed` 分成不同声明格式。
2. **依赖唯一性**：每个主命题只允许一条主依赖链；历史探索移入注记或 archive。
3. **引用索引完备**：所有外部定理有来源、页码/定理号、变量替换、适用条件。
4. **证书复现包**：每个计算证书有脚本、输入、输出、验收命令、hash 或版本说明。
5. **实验降级**：所有实验结果标为结构证据或常数猜测，不能作为无限定理证明。
6. **符号统一**：`P,p,q,Y,H,I,U_Y,G_Y,B_Y` 等在 PM/TP/RH 中不能重名冲突。
7. **无过度声明检查**：全稿扫描删除或限定“unconditional proof of RH/prime-pair/row-column theorem”等表述。

## 6. 外审前优先级清单

### P0：必须先完成，否则不宜外审

1. 建立主稿命题状态总表，并在每个 theorem/proposition 后标注状态。
2. 把 Prime Matrix 终局改写为 `A/B reduction + remaining Structured-EHPD/PDEC/SAE/Rankin obligations`。
3. 把二点筛终局改写为 `conditional on I3-Core` 或 `external DI/BFI subchain only`。
4. RH 保留 verification package 和 warning，不写最终 RH 证明。
5. 完成外部定理引用模板：RS1962、DI、BFI、explicit formula、KL/Vaaler/BG/Baker。

### P1：决定是否可升级为强证明稿

1. Prime Matrix：闭合 `PDEC exclusion`、`SAE local escape exclusion`、Rankin certificates。
2. Prime Matrix：闭合 `RRD/OSPC/SelbergUniform/round` 常数账本。
3. 二点筛：完成 `BMD=>TLI` 无隐藏下界审查。
4. 二点筛：完成 I3-Core 的 true-residual balance 或明确标为未闭合。
5. RH：把 controlled exits 写成四列表并逐项证明。

### P2：提升可读性和审稿效率

1. 二点筛链条编号为 `TP-1` 到 `TP-9`。
2. Prime Matrix 链条编号为 `PM-1` 到 `PM-8`。
3. RH 链条编号为 `RH-1` 到 `RH-5`。
4. 为每个实验脚本写用途说明。
5. 将历史探索稿合并、降级或移入 archive，避免主线混乱。

## 7. 作者当前应采用的外审前结论措辞

建议在合著稿摘要或导论保留如下边界：

> 本稿给出统一矛盾场方法、Prime Matrix、二点筛与 RH 方向的依赖图、局部刚性、证书接口和未闭合义务。本文已经闭合若干子模块，尤其是 BPN-LHB 的有限证书/显式外部定理版接口；但 Prime Matrix 行列命题、二点筛素数对命题与 RH 终局仍需相应的结构排斥、外部深定理适配或 controlled exits 逐行验证后，才可升级为最终无条件定理。

这个措辞是当前最符合顶级期刊审稿标准的诚实边界。

## 8. 本轮逐项处理结果

本轮对“当前所有最硬剩余”的处理采用顶刊审稿标准：能用现有材料闭合的，标为闭合子模块；只能归约但未证明的，标为最小硬输入；涉及 RH、孪生素数或 Prime Matrix 终局提升的，不以作者自审替代证明。

| 编号 | 最硬剩余 | 本轮完成的实际动作 | 当前诚实状态 |
|---|---|---|---|
| H1 | Prime Matrix A/B 入口 | 已新增 `prime-matrix-ab-entrance-theorem-list.md`，并将主稿 A/B reduction 改为 `Reduction-closed Statement` | 归约闭合；非终局排斥 |
| H2 | Structured-EHPD / D 组 | 明确列为 Prime Matrix 终局第一硬门；要求直接证明或由 RHI 替代 | 未闭合定理级接口 |
| H3 | BPN-LHB | 已确认五段证书/RS1962 外部定理版闭合边界，并新增可字节级复现的证书账本 | 子模块闭合；不推出全局行列命题 |
| H4 | PDEC/SAE/Rankin | 拆成 `PDEC exclusion`、`SAE local escape exclusion`、Rankin certificates 三项；新增 H4-PDEC 证书模板、首批约束来源引理、约束准入表、column cap 来源规则和 V1 系数账本，固定 `PDEC-Explicit-Cert/PDEC-Dual-Cert` 的输入、下界、约束合法性、准入等级和失败回流规则 | 最终硬输入；PDEC 格式/来源/准入规则闭合但证书未填 |
| H5 | RRD/OSPC 常数账本 | 新增 `h5-4-ospc-weighted-crtdefect-absorption.md`，把 `OSPC* / weighted CRTDefect` 吸收到 `PDEC-or-SAE` | H5.1/H5.4 路由完成；最小硬点转为 H4 证书排斥 |
| H6 | 二点筛 I3-Core | 拆成八个必须逐项证明的定理义务 | 条件核心；未闭合 |
| H7 | DI/BFI 外部适配 | 已新增 `kls-window-di-bfi-adaptation-template.md`，完成 KLS-window 的相位、模数、频率、权重、gcd、平滑、`B(A)` 全表核验 | 外部深定理版闭合；完全自足版仍需重证 DI/BFI |
| H8 | BMD 到 TLI | 明确为二点筛最重要的无隐藏下界审查 | 未闭合；若失败即 parity-transfer gap |
| H9 | RH controlled exits | 改写为七项 controlled-exit 证明义务 | verification package；非 RH 证明 |
| H10 | 合著稿状态工程 | 已新增 `claim-status-discipline.md`，并在主稿加入六类状态专用 theorem-like 环境 | 作者侧状态分级完成；剩余为编辑性替换 |

因此，“逐项完成”的当前可交付结果是：所有最硬剩余已被归入唯一审稿义务链，且每项都标明了可闭合条件和不能过度声明的边界。真正的数学定理级缺口仍需新增证明，不能由文稿整理或实验扫描替代。

## 9. 后续逐项攻坚路线图

新增 `docs/monograph/unclosed-hard-obligations-attack-roadmap.md`，对 H1--H10 逐项给出：

1. 精确证明目标；
2. 可用刚性与外部工具；
3. 最小补正动作；
4. 可行性评级；
5. 失败时必须采用的诚实状态。

该路线图把下一步执行顺序明确为：

```text
可立即完成：实验脚本用途索引、历史 theorem 环境状态化替换；H1入口定理化、H3证书复现账本、H7 DI/BFI适配模板、H10状态分级已完成；
最值得硬攻：H5 RRD/OSPC、H4 Rankin/PDEC/SAE、H2 RHI/PM-R2B；
必须保持条件：H6 I3-Core、H8 BMD=>TLI、H9 RH controlled exits。
```
