# Prime Matrix 行命题闭合输入图谱

**状态：** `closure_input_atlas_complete_global_inputs_still_open`

闭合输入图谱已固定：继续突破不应再寻找无名新分支，而应集中证明终端证书包、noncanonical full-S 补集输入包和 D-structure/Rankin 晋级包。

## 1. 图谱律

All explored structures now fall into two classes: closed reductions/contracts, or named inputs. The current corpus closes the canonical-source theorem boundary and the no-unnamed-escape logic, but full global unconditional closure still requires the terminal certificate package, the noncanonical full-S complement package, and final D-structure/Rankin promotion.

```text
canonical_source_self_contained_closed=true
noncanonical_input_contract_closed=true
row_column_unconditional_closed=false
```

## 2. 已探索模型回顾

| model | proved / reduced | output | closure input | status |
| --- | --- | --- | --- | --- |
| Full CRT / MinRep 零行等价 | 零行等价于完整覆盖 CRT 证书与最小代表缺陷。 | 把反例固定为具体 tau 与 r_tau^+<=P。 | 后续必须排斥 MinRep 缺陷，或把它送入容量/端点/PDEC 出口。 | `reduction_closed` |
| 方阵斜线 / 圆柱覆盖 | 高素斜线补洞可以写成圆柱面残基命中；覆盖需要容量大于剩余洞。 | T_Y>=\|S_Y\| 是零行必要条件。 | 动态容量不等式，或失败进入 SAE/PDEC/ColumnCRT/尾锚。 | `reduction_closed` |
| 第 P 列锚点动态轮容量 | T_Y(P,y)<\|S_Y(P,y)\| 严格推出该行有素数洞。 | 全行全列夹击方程 S_Y(P,y)=圆柱平移骨架。 | 证明所有行容量不足；若容量失败，证明近截止/远尾超额必进命名缺陷。 | `input_needed` |
| P^2±k 与层叠轮筛 | 30/210/2310/... 单位类偏斜若不稀释则给 W-unit PDEC；若稀释则进 CleanKLS/DLS。 | 圆柱容量压力与小模相位同步形成夹击。 | W-unit PDEC/ColumnCRT 排斥，或高维分散 CleanKLS/DLS。 | `input_needed` |
| 远尾互补因子反演 | 远尾 q 命中等价为 Y-rough 互补因子 m 上的短素数区间计数。 | 正超额不再无结构，落在 m-band/cofactor-anchor。 | Self-normalized tail dichotomy：超额必进 cofactor-anchor/SAE/PDEC/ColumnCRT。 | `input_needed` |
| SN-1/SN-2/SN-3 递归剥离 | 最小反例不能无限保持无名；低模峰、高频峰、多壳同步都必须命名。 | 反例有限步进入 SAE/PDEC/ColumnCRT/Bohr-cap/CleanKLS/TotalDescent。 | 排斥这些命名出口，或证明 CleanMultishellKLS / TotalDescent。 | `unnamed_closed_named_open` |
| 命名出口吸收合同 | Bohr-cap、EndpointSeam、CofactorAnchor 不再是自由出口，吸收到统一接口。 | 最终出口缩为 SAE-Cert / PDEC-Cert / ColumnCRT-Cert / CleanKLS / p=2 descent。 | 提交这些证书或证明无缺陷下降到底。 | `contract_closed_certificates_open` |
| PDEC 对偶失败与 cap 细化 | PDEC 上界失败只能变成帽集中；持久帽进 refined PDEC，稀疏帽进 SAE。 | PDEC 失败不能生成新无名分支。 | 完成 U_CRT<L_PDEC，或完成 refined PDEC / SAE / ColumnCRT / stitching。 | `no_cycle_closed_certificate_open` |
| Triad-A1 canonical-source 自足分支 | canonical RIW/Buchstab 来源分支的 same-set/full-S terminal 与 terminal promotion 已闭合。 | NoFurtherCanonicalSourceSelfContainedTheoremBoundaryGap。 | 无 canonical 内部输入；只需防止误升级。 | `closed` |
| Noncanonical full-S 补集 | 必要输入边界已闭合；generic WFD 模板不可用。 | 补集只能走实际源恒等、实际源强化反原子或外部/量化 DI/BFI。 | ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab 或 FullSNonAPStrengthenedSourceAntiAtomForActualSource 或 DIBFI no-projection。 | `input_contract_closed_input_open` |
| D-structure / Tail-log4 / Rankin 晋级门 | 作者侧组织与边界已固定；仍是独立审稿门。 | PM final promotion remains referee-block。 | DStructureTailLog4FiniteRankinIndependentAcceptance。 | `referee_block` |

## 3. 最小闭合输入基

### TerminalCertificatePackage

- SAE-Cert
- PDEC-Cert with U_CRT<L_PDEC
- ColumnCRT-Cert or return to PDEC/SAE
- CleanMultishellKLS
- TotalDescent to p=2 or first-seam absorption

需要原因：无名逃逸和命名出口已被压到这些接口；排斥它们即可关闭结构反例出口。

### NoncanonicalFullSComplementPackage

- Actual full-S non-AP source equals canonical RIW/Buchstab source
- or strengthened anti-atom for the actual noncanonical source
- or quantified no-projection DI/BFI route

需要原因：canonical 分支已扣除，generic WFD 模板已反证；补集不能偷渡闭合。

### DStructureRankinPromotionPackage

- D-structure/Tail-log4 interface accepted
- finite Rankin and threshold interfaces accepted
- PM final promotion referee block removed

需要原因：完整行/列无条件定理晋级仍依赖该独立门。

## 4. 可选捷径

- 外部平方根长度短区间素数输入可直接关闭对角端点，但不是当前自足主路线。
- 外部 FullS-KLS / DI / BFI 可关闭 generic 外部合同版，但不能冒充 canonical 自足证明。

## 5. 最终判定

当前材料已经把全部主要思路压成有限输入图谱：

```text
方阵斜线/圆柱覆盖/第P列锚点/层叠轮筛/远尾反演/SN递归剥离
=> 无名逃逸不可能
=> 命名出口吸收
=> 终端证书包或 CleanKLS/TotalDescent。

canonical-source 分支
=> 已闭合。

noncanonical full-S 补集
=> 必要输入边界已闭合，但输入本身仍开。
```

因此继续突破的正确目标不是寻找新的固定常数，也不是回到 generic WFD 模板，而是逐项证明最小输入基中的三包。只有三包全部闭合，完整行/列无条件定理才可升级。
