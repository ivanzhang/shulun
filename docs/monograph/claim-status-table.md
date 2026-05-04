# 合著论著命题状态总表

本文给出合著论著 `paper/contradiction-field-monograph/contradiction-field-monograph.tex` 的命题状态。状态必须诚实区分：已在文稿中证明、已归约、外部输入、计算证书、仍需独立审稿。

| 模块 | 命题/输入 | 当前状态 | 主要证据 | 是否可称无条件终稿 |
|---|---|---|---|---|
| Prime Matrix A/B | 行/列反例归约到 Structured-EHPD | 已归约/入口定理化完成 | `docs/row-column-reduction-formal-appendix.md`; `docs/monograph/prime-matrix-ab-entrance-theorem-list.md` | 否，仍依赖 D 组排斥 |
| Prime Matrix recursive lift | 相邻素数方阵递推升级路线 | 新增路线审查/粗合数投影已压缩到第一锚粗互补因子同权预算；恒等式审计差为 `0`；FAC 模型审计暴露逐窗口单一常数负余量；低模审计显示尖峰主要由 `D_T` 端点缺陷捕获；Annulus 已压缩为旧筛幸存者非空；正负异常统一为 signed endpoint sawtooth bridge；终端带最新压缩到 `RCI/PDEC`，分散分支进一步压缩到 `WSH-Hall/PDEC`：单尾因子完全抵消，只剩无尾储备与多尾碰撞超额，双粗半素数补洞受固定偏移轮筛容量约束 | `docs/monograph/prime-matrix-recursive-lift-audit.md`, `docs/monograph/prime-matrix-seam-endpoint-audit.md`, `docs/monograph/prime-matrix-seb-unconditionality-audit.md`, `docs/monograph/prime-matrix-asb-pressure-audit.md`, `docs/monograph/prime-matrix-asb-hard-attack.md`, `docs/monograph/prime-matrix-asb-rhc-alpha-sweep.md`, `docs/monograph/prime-matrix-rpd-failure-structure.md`, `docs/monograph/prime-matrix-semiprime-anchor-projection.md`, `docs/monograph/prime-matrix-anchor-cofactor-interval-audit.md`, `docs/monograph/prime-matrix-mge3-budget-audit.md`, `docs/monograph/prime-matrix-mge3-second-anchor-audit.md`, `docs/monograph/prime-matrix-mge3-tail-envelope-audit.md`, `docs/monograph/prime-matrix-tail-spike-localization-audit.md`, `docs/monograph/prime-matrix-singleton-corridor-bound-audit.md`, `docs/monograph/prime-matrix-singleton-corridor-overlap-audit.md`, `docs/monograph/prime-matrix-singleton-corridor-closure-lemma.md`, `docs/monograph/prime-matrix-disjoint-corridor-selberg-lemma.md`, `docs/monograph/prime-matrix-rpd-first-anchor-identity.md`, `docs/monograph/prime-matrix-rpd-first-anchor-identity-audit.md`, `docs/monograph/prime-matrix-rpd-fac-budget-audit.md`, `docs/monograph/prime-matrix-rpd-fac-lowmod-defect-audit.md`, `docs/monograph/prime-matrix-square-annulus-lift-lemma.md`, `docs/monograph/prime-matrix-square-annulus-sieve-lift-audit.md`, `docs/monograph/prime-matrix-annulus-rough-nonempty-hard-attack.md`, `docs/monograph/prime-matrix-signed-lowmod-bridge-hard-attack.md`, `docs/monograph/prime-matrix-directed-endpoint-crtdefect-bridge.md`, `docs/monograph/prime-matrix-dec-ospc-exclusion-hardpoint.md`, `docs/monograph/prime-matrix-terminal-sae-cancellation-identity.md`, `docs/monograph/prime-matrix-terminal-sae-cancellation-audit.md`, `docs/monograph/prime-matrix-asb-rpd-weighted-sieve-kernel.md`, `docs/monograph/prime-matrix-semiprime-wheel-shadow-rigidity.md`, `docs/monograph/prime-matrix-semiprime-wheel-near-offset-audit.md` | 否，最终剩余已精确为 `RCI/PDEC` 的分散出口 `WSH-Hall/PDEC`: 证明轮筛允许 Hall 匹配，或证明失败形成固定偏移 CRTDefect、Tail-anchor、Endpoint/PDEC；否则递推链仍为严格归约 |
| Prime Matrix EDA-Dual | 早期对角避让 `X0(p)>p` 的 Bonferroni/Selberg 对偶路线 | 新增低阶硬攻：`U_p(x)` 已写成小素因子覆盖余量，奇数阶 Bonferroni 下界 `S_K(p,x)` 已严格化为纯 CRT 整除计数；五阶恒等式 `S_5=U_p-\sum_{\omega_p(n)\ge6}{\omega_p(n)-1\choose5}` 精确暴露唯一尾项。实验样本显示 `S_5>0`，但固定阶存在渐近变号风险，不能作为全局证明 | `docs/monograph/prime-matrix-early-diagonal-avoidance-hardpoint.md`, `docs/monograph/prime-matrix-first-zero-equivalence-and-diagonal-barrier.md`, `docs/monograph/prime-matrix-eda-gap-barrier-and-dual-route.md`, `docs/monograph/prime-matrix-eda-dual-bonferroni-hard-attack.md`, `experiments/prime_matrix_eda_bonferroni_audit.py` | 否，剩余为 `EDA-BK/Selberg`：构造可变阶 Bonferroni/Brun/Selberg 正下界，或证明高重合尾项过大必触发 `PDEC/SAE` |
| Prime Matrix EDA-BK bridge | Bonferroni 下界失败到端点 CRT 缺陷 | 桥接定理已逐行证明：写 `S_K=H G_K+E_K`，其中 `G_K` 是截断 Euler 主项，`E_K` 是端点分数部分锯齿和；若奇数阶 `K` 满足 `G_K>0` 且 `S_K<=0`，则必有 `E_K<=-H G_K`。因此任何 EDA 反例都会产生显式负端点缺陷 | `docs/monograph/prime-matrix-eda-bk-endpoint-defect-bridge.md`, `experiments/prime_matrix_eda_endpoint_defect_audit.py` | 否，桥接已证；正主项阶数由下一行闭合，仍需排斥端点缺陷或将其并入 `PDEC/SAE` 证书 |
| Prime Matrix EDA-BK dichotomy | 正主项阶数与低模/尾项二分 | 已证明存在奇数阶 `K_*(p)` 使 `G_{K_*}(p)>0`；若 EDA 失败，则反例行给出 `E_{K_*}<=-(p-1)G_{K_*}`，并对任意 cutoff `D` 二分为 `LowMod endpoint CRTDefect` 或 `Tail/Core concentration` | `docs/monograph/prime-matrix-eda-bk-lowmod-tail-dichotomy.md` | 否，二分已证；剩余是排斥 LowMod 出口并吸收 Tail/Core 出口 |
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
