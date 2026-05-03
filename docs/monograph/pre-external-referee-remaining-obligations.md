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
新增 `docs/monograph/prime-matrix-scaled-peeling-halfwidth-audit.md` 后，缩放到前一素数和约半宽素数的版本
也不能直接闭合：缩放行号需要完整包含判据，半宽层会复活粗互补因子点。该路线仍需复活点吸收缺陷定理。

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
