# 合著论著命题状态总表

本文给出合著论著 `paper/contradiction-field-monograph/contradiction-field-monograph.tex` 的命题状态。状态必须诚实区分：已在文稿中证明、已归约、外部输入、计算证书、仍需独立审稿。

| 模块 | 命题/输入 | 当前状态 | 主要证据 | 是否可称无条件终稿 |
|---|---|---|---|---|
| Prime Matrix A/B | 行/列反例归约到 Structured-EHPD | 已归约 | `docs/row-column-reduction-formal-appendix.md` | 否，仍依赖 D 组排斥 |
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


## 内部逐行复核更新

新增 `docs/monograph/line-by-line-internal-referee-matrix.md`。作者侧逐行复核未发现新的 `BLOCK-MATH`，但 Prime Matrix 终局与 RH 终局仍为 `BLOCK-REFEREE`：必须由独立审稿接受 D-structure/Tail-log4/finite 接口与 RH controlled exits 后，才可升级为最终无条件定理。

## 两点 P-rough 命题 A/B 状态

新增 `docs/monograph/two-point-rough-pair-propositions.md`。审查结论：A 与 B 在同余条件上等价；由于 `P×P` 方阵内任意大于 1 的 `P`-rough 数必为素数，A/B 对固定偶数 `w` 的全体充分大 `P` 成立将推出固定偶差素数对无穷多，特别 `w=2` 推出孪生素数猜想。因此 A/B 不能作为当前论著的无条件定理，只能列为二点 rough Jacobsthal / prime-pair 级未来突破方向。

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

| 二次筛中尺度K2全局复核 | 参数通过/待定理化 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 297--303 节。最终 `alpha0=0.75` 时，若使用薄层递推、固定阶局部交叉与硬骨架截断 `R<=polylog(P)`，则最坏层 `Y=P^0.75` 的 K=2 误差为 `P^-0.5 polylog(P)=o(1)`，层数累积仍 `o(1)`。全局参数义务通过；剩余是把 `Q_eff<=polylog`、SC2误差、Zero Mass块分布、平滑回退正式定理化。 |

| 二次筛剩余审稿义务A-D | 骨架完成/待逐行展开 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 304--308 节。四项义务定理化为：A 固定阶局部交叉 `Q_eff<=polylog(P)`；B `SC2` 二阶相关误差 `<=0.15`；C Zero块分布 `M1>=0.58,M2>=0.28`；D 平滑回退损失 `<0.03`。A/D 技术性可闭合，B 依赖45-Main链条，C 依赖硬骨架低阶矩。下一步优先逐行补 C。 |

| 二次筛Zero Mass义务修正 | 更稳路线 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 309--314 节。逐行审查发现用三阶矩直接证明 `M1>=0.58,M2>=0.28` 不够稳；改为 C'：加权 Bonferroni 直接证明 `sum X_B 1_{R=0}/sum X_B>=0.30`。模型值约 `0.604`，只需一阶命中、SC2二阶下界、三阶尾部三个矩估计，余量更大。 |

| 二次筛C'矩估计逐行 | 参数优化/待正式矩证明 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 315--319 节。将有效层均值从 `nu=1/2` 调整为 `nu=0.45`，C' 常数更宽松：一阶 `<=0.50`，二阶 `>=0.05`，三阶 `<0.03`，合并 `rho0>=0.52` 理论空间，远超所需 `0.30`。剩余为正式证明二阶下界和三阶上界的固定阶局部交叉矩估计。 |

| 二次筛C'矩闭合推进 | 常数闭合/剩三线形式化 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 320--323 节。对 `nu=0.45`，二阶主项 `nu^2/2=0.10125`，扣 `0.03` 仍 `>0.05`；三阶主项 `0.0152`，若退化三线 `<0.01` 则 `<0.03`。C' 给 `rho0>=0.52`。为更稳可最终取 `nu=0.4`，二阶仍够、三阶余量更大；剩余为三线退化估计形式化。 |

| 二次筛三线退化估计 | C'闭合 | `docs/monograph/two-point-secondary-sieve-research.md` 已补充第 324--330 节。最终取 `nu=0.4`：重合退化通过互异线定义为 0；双同步退化由45-Main残余 `<0.02` 给 `<0.008`；三重共块由K=3局部交叉 polylog 复杂度给 `<0.005`。三阶总项 `<0.02567<0.03`，C' 得 `rho0>=0.57`，审稿义务 C' 闭合。 |

| 二次筛A/B最终缺口审查 | 不可无条件并入 | `docs/archive/monograph-reviews/two-point-secondary-sieve-gap-audit-2026-05-01.md` 已新增。顶刊标准下仍有 G1--G7 缺口：真实剩余集支撑/下界筛、TCA线性桥接真实块下界、SC2二阶相关下界、三线退化常数、`Q_eff<=polylog`形式化、平滑回退、任意偶数w均匀性。可作为条件研究命题章节并入，不能作为无条件证明。 |

| G1补正工作台 | 未闭合/压缩为局部条件均衡 | `docs/monograph/two-point-gap-closure-workbench.md` 已新增。G1 真实剩余支撑不能用普通低阶权重绕过；最直接权重 `1_U` 真实支持但难计算。当前最小硬点压缩为“局部条件均衡引理”：真实二次筛剩余集 `U_Y` 对固定阶局部测试函数保持均衡，误差不依赖完整 CRT 周期。 |

| G1局部均衡强度审查 | 强下界不可直接闭合 | `docs/monograph/two-point-gap-closure-workbench.md` 已补充 G1.6--G1.9。局部条件均衡的下界方向接近强筛余项/parity barrier，不能直接无条件宣称。可行补正是 G1-Dichotomy：若真实剩余质量避开 Zero/低覆盖块，则产生 SC2/CRTDefect 异常。G1 需与 G2 合并处理。 |

| G1-G3合并补正 | 压缩为真实块协方差引理 | `docs/monograph/two-point-gap-closure-workbench.md` 已补充 G2.1--G2.4。G1真实支撑与G2真实块下界可合并：若真实剩余避开Zero/低覆盖块，则它与下一层覆盖函数产生异常正协方差；该协方差应由SC2/CRTDefect控制。因此G1--G3最小共同硬点为“真实块协方差引理”。 |
