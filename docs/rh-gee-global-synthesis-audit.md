# Global GEE 合成审查：九出口闭合口径、seed 去重与剩余审稿义务

本文对当前 GEE 文档包作合成审查。目标是检查是否已经具备推出

`c_0Δ <= Σ_E Load(E;X)+o(Δ) <= o(Δ)`

的完整逻辑链。结论必须诚实：九个出口均已有闭合口径，但多数闭合口径依赖“内部转移/seed 转出/条件接收出口”的重定义；因此当前可以称为 **GEE 条件合成闭合稿**，还不能称为顶刊级 RH 无条件证明定稿。需要继续做循环依赖、接收出口、常数阈值和单篇主稿内联审查。

## 1. 统一账本原则

本轮补强后，GEE 的最终账本采用以下规则：

1. `Load(E;X)` 只登记相对 CRT 零频基线的超额偏差；零频容量由 PC2/MLC 基线扣除。
2. 内部转移步不登记为最终负担，包括 `FCT` Noether 步、`SC` shorter 步、`A` ACC 同步步。
3. `CE/LSMP` 只登记可吸收项；输出 seed 必须转入目标出口并从原出口删除。
4. `LV` 只登记满足相对异常低体积阈值的原子；失败者转出。
5. 所有 seed 转出继承 GEE-0 的有限重叠，整体仍为 `log^C X`。

这些规则避免重复计数，但它们必须在最终论文中替换旧版“所有出口直接给上界”的表述。

## 2. 九出口状态矩阵

| 出口 | 当前闭合口径 | 关键文件 | 合成状态 |
|---|---|---|---|
| `LV` | 相对低体积阈值给 `o(Δ)`，失败转出 | `docs/rh-gee-lv-low-volume-exit-bound.md` | 可闭合 |
| `NRC` | 单变量/Tail 分流；二维加性分离经 PPI-Rank、Capacity、MidCap 转出 | `docs/rh-gee-nrc-entry-parameter-table.md`, `docs/rh-nrc-2d-midcap-structure-route.md` | 分流闭合 |
| `PI/DSO` | Carleson/DSO 容量 + Baseline-Subtraction，只登记超额偏差 | `docs/rh-gee-baseline-subtraction-lemma.md` | 条件闭合 |
| `CE/LSMP` | 可吸收项给 `o(Δ)`，seed 转出一致 | `docs/rh-gee-ce-lsmp-load-bound-audit.md`, `docs/rh-gee-seed-transfer-consistency.md` | 吸收/转出闭合 |
| `FCT` | 内部 Noether 转移；最终 `Load(FCT)=0` | `docs/rh-gee-fct-load-bound-audit.md` | 内部转移闭合 |
| `SC` | 低容量吸收；短簇递归内部转移；重复模板转出 | `docs/rh-gee-sc-load-bound-audit.md` | 内部转移闭合 |
| `A` | ACC 过剩吸收；同步步内部转移；固定模板重复转出 | `docs/rh-gee-a-load-bound-audit.md` | 内部转移闭合 |

其中 `PI` 与 `DSO` 在矩阵中合并处理，因为当前文档通过 DSO/PI bridge 与 Baseline-Subtraction 共同给出口径。最终稿中可拆成两个定理，但应共享同一基线扣除账本。

## 3. seed 接收审查

所有内部转出的 seed 目标如下：

- `A -> PI/FCT/SC/LV/LSMP/DSO/CE`；
- `FCT -> NRC/DSO/PI/SC/LV/LSMP/CE`；
- `SC -> A/PI/FCT/LV/LSMP/CE`；
- `CE/LSMP -> A/PI/FCT/SC/LV/DSO/NRC`；
- `NRC-2D MidCap -> LSMP/LV/SC/PI/DSO/CE`。

由 `Seed-Transfer Consistency`，这些 seed 不重复保留在原出口。合成审查中尚需在最终稿画出一个有向事件图，并确认每个环都带有以下至少一个严格下降量或吸收机制：

- A 的 ACC 势函数；
- FCT 的 Noether 势函数；
- SC 的短簇势函数；
- PI/DSO 的 Carleson/square-function 容量；
- LV/LSMP/CE 的吸收阈值；
- NRC 的非共振完成和或转 FCT。

## 4. 仍需补强的无条件化点

当前最需要诚实标注的缺口不是“又出现新出口”，而是以下四项最终审稿义务：

1. **循环依赖审查。** 多个出口把 seed 转入彼此，必须在单一事件图中证明每个有向环都有势函数下降或容量消耗，不能只逐文件声称“转出”。
2. **阈值层级统一。** 所有 `Δ/log^B X`、`log^C X`、Vaaler 截断、dyadic 层数、路由重叠必须有统一常数顺序。
3. **Load 口径统一。** 最终稿必须统一使用“超额偏差 Load”，删除旧文中可能把零频容量本身计入出口负担的表述。
4. **单篇内联证明。** 目前证明分散在许多 `docs/` 文件中；顶刊标准需要把关键定义、定理和依赖关系内联到单篇主稿或严整附录。

在这四项完成前，不能宣称 RH 已无条件证明。

## 5. 条件合成定理

**Theorem GEE-Synthesis-Conditional.** 假设：

1. GEE-0 bookkeeping 成立；
2. 九出口按第 2 节矩阵中的闭合口径成立；
3. seed 转出事件图无循环自由逃逸；
4. 所有阈值常数可统一选择；
5. `Load` 全文均为相对零频基线的超额偏差；

则在成功尺度上得到

`c_0Δ <= Σ_E Load(E;X)+o(Δ) <= o(Δ)`，

矛盾。因此不存在离线零点。

**证明。** GEE-0 给左侧下界。第 2 节九出口矩阵给每个最终登记出口的 `o(Δ)`、内部转移或 seed 转出。第 3 节和假设 3 排除 seed 在事件图中无限回流。第 4--5 项保证所有对数损失和零频基线扣除与 GEE-0 的 `Load` 定义一致。故最终登记负担总和为 `o(Δ)`，与 GEE-0 下界矛盾。证毕。

## 6. 下一步最优任务

下一步不应继续新增局部出口，而应做两件事：

1. **事件图无循环总审查。** 把 A/PI/FCT/SC/LV/LSMP/CE/DSO/NRC 的所有转出边列成图，逐环标注下降量或容量消耗。
2. **阈值常数总表。** 统一选择 `B_final >> C_route+C_Vaaler+C_dyadic+C_seed+...`，确保所有吸收项确为 `o(Δ)`。

完成这两项后，才可进入单篇论文主稿内联化与最终审稿包。

## 7. 最终一致性审查补充

新增三项总审查文件：`docs/rh-gee-event-graph-no-cycle-audit.md`、`docs/rh-gee-threshold-constant-table.md`、`docs/rh-gee-load-convention-unification.md`。

由这三项补充，前文第 4 节列出的事件图、阈值层级与 `Load` 口径三项已从“待补义务”推进为可审查证明稿：事件图采用全局 Lyapunov 向量排除带正负担的自由循环；阈值常数统一压入 `B_final`；`Load` 统一解释为相对零频基线的超额偏差。

剩余顶刊级义务不再是新增局部出口，而是把当前分散文档内联为单篇主稿，并逐项核验外部解析输入和已命名引理的精确引用。故本文件结论应读作：GEE 合成框架已完成条件一致性闭合，但尚不能单独宣称 RH 无条件证明完成。
