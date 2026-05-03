# H4-PDEC 第一版约束准入表

**状态：** `h4_pdec_admissible_constraint_table_v1`

本文承接 `h4-pdec-certificate-template.md` 与 `h4-pdec-constraint-source-lemmas.md`，把
`PDEC-Dual-Cert` 中候选约束行逐项标注为可进入、条件可进入或暂不可进入正式
`A g<=b, E g=e` 系统。本文仍不排除 `PDEC`；它只完成第一版证书输入边界。

## 1. 准入等级

| 等级 | 含义 | 可否进入正式证书 |
|---|---|---|
| `Tautology` | 对任意 `S` 恒真 | 可进入 |
| `FiniteCert` | 指定有限范围、指定 `Z`、指定输出文件可复核 | 可进入有限证书 |
| `SymbolicReady` | 已有符号化定理给出容量或路由 | 可进入对应范围 |
| `PartialFiniteAReady` | 部分有限行已有机器相位块与界值 | 仅对应有限行可进入 |
| `ConditionalRouting` | 在排除某个命名出口后的剩余分支中成立 | 只能作为分支证书行 |
| `NeedsCoefficients` | 来源规则已证明，但 `C_j,B_j` 或分支元数据未填 | 暂不可进入实际审计输入 |
| `NeedsPhaseBlock` | 数值界值已登记，但缺机器可读相位块 `C_j` | 暂不可进入实际审计输入 |
| `NeedsProof` | 形式正确但缺来源证明、系数或界值 | 不可进入 |
| `NeedsMultiplicityCap` | 支撑相位块已物化，但缺 `g(t)<=M(t)` 多重度界 | 暂不可进入实际审计输入 |
| `Rejected` | 逻辑上不能从现有假设推出 | 不可进入 |

正式 `PDEC-Dual-Cert` 只能使用前三类及注明分支的 `ConditionalRouting`。`NeedsProof`
可以保留为下一步攻坚目标；`Rejected` 必须从证书输入中删除。

## 2. 原子约束准入表

| 原子行 | 形式 | 准入等级 | 来源 | 当前可用范围 | 备注 |
|---|---|---|---|---|---|
| 非负性 | `g(t)>=0` | `Tautology` | `H4-PDEC-S1` | 全部 `S` | 进入变量域，不进入 `A` 行也可 |
| 质量等式 | `sum_t g(t)=|S|` | `Tautology` | `H4-PDEC-S1` | 已知精确 `|S|` 时 | 若只知范围，改成上下界 |
| 质量下界 | `sum_t g(t)>=S_min` | `Tautology` | persistent 定义 + `H4-PDEC-S1` | 只知 `|S|` 下界时 | 用 `-sum_t g(t)<=-S_min` 写入 `A` |
| 质量上界 | `sum_t g(t)<=S_max` | `Tautology` | 索引域容量 + `H4-PDEC-S1` | 只知 `|S|` 上界时 | 通常 `S_max=|X|` |
| phase cap | `g(t)<=C_Z(t)` | `FiniteCert` / `SymbolicReady` | `H4-PDEC-S2` | 有 `S subset Z` 证明时 | 有限 `P=23,Q=210` 表只用于有限样本 |
| block cap | `sum_{t in T}g(t)<=C_Z(T)` | `FiniteCert` / `SymbolicReady` | `H4-PDEC-S2` | 有相位块容量定理时 | column、bucket、mirror-pair 都是特例 |
| mirror equality | `g(t)=g(rho(t))` | `NeedsProof` | `H4-PDEC-S3` | 仅当证明 `m(S)=S` | 不能由完整周期镜像自动推出 |
| mirror-pair cap | `g(t)+g(rho(t))<=B_mir(t)` | `FiniteCert` / `SymbolicReady` | `H4-PDEC-S3` | 有 `S subset Z` 与成对容量时 | 当前比强镜像等式更安全 |
| column cap | `sum_{t in C_j}g(t)<=B_col(j)` | `PartialFiniteAReady` / `NeedsPhaseBlock` / `NeedsMultiplicityCap` / `ConditionalRouting` | `h4-pdec-column-cap-source-lemma.md`; `h4-pdec-column-cap-coefficient-ledger.md`; `h4-pdec-lhb-column-phase-blocks.json`; `h4-pdec-lhb-multiplicity-cap-route.md`; `h4-pdec-lhb-multiplicity-cap-certificate.json`; `h4-pdec-lhb-attachment-lemma.md`; `h4-pdec-bad-window-classification-lemma.md`; `h4-pdec-homogeneous-splitting-lemma.md` | `Q=2310` LHB 空异常块已物化；`WHOLEDEF/BRIDGED` 在 LHB 型分支已有接入证明、`M(t)` 与 `bound=0`；分类引理给出非 LHB 型失败出口，口径混合已降为拆分 | 不能由期望均匀性或支撑大小替代 |
| low-hole bucket | `sum_{h_Q(t)>=m}g(t)<=B_m` | `FiniteCert` / `NeedsProof` | `H4-PDEC-S4` | 有限样本可用；全局需 Hall/CRT 定理 | `P=23,Q=210,m>=5` 是有限证书行 |
| tail-anchor cap | `sum_{t in A_a}g(t)<=B_tail(a)` | `ConditionalRouting` | `H4-PDEC-S5` | 排除 Tail-anchor 出口后的剩余分支 | 必须列出路由定理 |
| core-overlap cap | `sum_{t in H_c}g(t)<=B_core(c)` | `ConditionalRouting` | `H4-PDEC-S5` | 排除 core/high-overlap 出口后的剩余分支 | 违反时回流 higher-defect |
| Rankin spike cap | `sum_{t in R_m}g(t)<=B_rankin(m)` | `ConditionalRouting` | `H4-PDEC-S5` | 处理 Rankin 失败剩余分支 | 必须绑定正式走廊证书 |
| H5 exit cap | `R_{H5}(g)<=B_{H5}` | `ConditionalRouting` | `h5-1` 与 `h5-4` | 非 OSPC*/非 weighted CRTDefect 剩余分支 | 不能当作全局约束 |
| full-cycle balance | `sum_{t in C}g(t)≈expected` | `Rejected` | 无 | 不可用 | 完整周期均衡不传给任意子集 |
| sample-to-global cap | 有限表直接用于全体 `P` | `Rejected` | 无 | 不可用 | 必须有符号化容量定理 |

## 3. 第一版 `A,b,E,e` 骨架

给定一个具体证书范围 `R` 与允许坏窗全集 `Z_R`，第一版线性系统应按如下顺序生成：

```text
变量：
  g_0,...,g_{Q-1} >= 0

等式 E g=e：
  若 |S| 精确已知：sum_t g_t = |S|
  若已证明 m(S)=S：g_t-g_{rho(t)}=0

不等式 A g<=b：
  若只知质量范围：sum_t g_t<=S_max, -sum_t g_t<=-S_min
  对每个准入相位 t：g_t<=C_Z(t)
  对每个准入相位块 T：sum_{t in T}g_t<=C_Z(T)
  对每个有限或符号化 bucket：sum_{h_Q(t)>=m}g_t<=B_m
  对每个分支路由行：R_i(g)<=B_i
```

其中，`mirror equality` 只在 `m(S)=S` 已证明时进入 `E`；否则仅可使用
`mirror-pair cap`。`ConditionalRouting` 行必须在证书元数据中写明“当前分支排除了哪个出口”。

## 4. 有限样本 `P=23,Q=210` 的准入状态

由 `prime-matrix-bpn-pdec-real-constraint-rows.md` 已知：

```text
P=23, Q=210；
真实零行数 3456；
非零 phase cap 数 44/210；
max phase cap = 324；
low-hole >=5 的 bucket bound = 0。
```

在仅讨论该有限样本、且 `Z` 取完整真实零行全集时：

| 行 | 准入状态 | 说明 |
|---|---|---|
| `g(t)>=0` | 可用 | 恒真 |
| `sum_t g(t)=3456` | 只对完整零行族可用 | 任意子族只能用范围 |
| `phase_cap_t` | 可用 | `S subset Z` 时安全 |
| `mirror_pair_cap` | 可用 | 成对容量安全 |
| `conditional mirror` | 条件可用 | 需证明当前 `S` 镜像闭合 |
| `low-hole>=5 => 0` | 有限样本可用 | 全局需 Hall/CRT 容量定理 |

该有限样本可用于测试 `PDEC-Dual-Cert` 审计管线，但不能作为无限族闭合。

## 5. 下一步必须补的系数源

第一版准入表暴露出三个真正数学硬点：

1. **Column cap 相位块物化与多重度界。** `Q=2310` LHB 空异常块已由 `h4-pdec-lhb-column-phase-blocks.json` 物化；`WHOLEDEF/BRIDGED` 在 LHB 型分支已由 `h4-pdec-lhb-attachment-lemma.md` 与 `h4-pdec-lhb-multiplicity-cap-certificate.json` 给出接入证明、`M(t)` 与 `bound=0`；`h4-pdec-bad-window-classification-lemma.md` 已把非 LHB 型失败归入命名出口；`h4-pdec-homogeneous-splitting-lemma.md` 已闭合口径混合拆分；仍需物化列见证半径/RCI-CDB/条件路由相位块并排除出口。
2. **Low-hole bucket 符号化。** 需要把有限 `B_m=0` 现象提升为 Hall/CRT 容量定理或给出可计算的分范围证书。
3. **Conditional routing 元数据。** tail/core/Rankin/H5 行必须逐条绑定“违反即进入哪个出口”的定理编号，否则不能进入正式 `A`。

完成这三项后，才能导出可供 `prime_matrix_bpn_pdec_dual_certificate_audit.py` 审计的第一版正式
`A,b,E,e` 输入文件。
