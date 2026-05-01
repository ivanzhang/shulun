# RH/GEE 单篇主稿内联审查稿

本文把当前 `docs/` 中分散的 Global-Exit-Exclusion（GEE）证明包内联为一篇可审稿的主稿草案。本文目标是完成“单篇主稿内联化”义务：统一定义、账本、事件图、阈值常数、九出口定理与合成定理。必须诚实说明：本文仍是 RH/GEE 条件合成闭合稿；只有当所有命名输入被外部精确引用或文内逐行证明后，才能升级为 RH 无条件证明定稿。

## 1. 反例输入与成功尺度

反设存在 ζ 函数离线零点 `ρ=β+iγ`，其中 `β>1/2`。PC1 给出无穷尺度 `X`、平滑权 `w_X`、基线权 `w_X^0`、符号 `σ∈{±1}` 与主异常尺度

`Δ=X^{β-o(1)}`，

使得某个平滑素数或 von Mangoldt 账本存在同向异常。PC2 把该异常转化为相对 CRT 零频基线的候选偏差。GEE 的任务是证明所有可能承载该偏差的最终出口总量为 `o(Δ)`，从而与 PC1/PC2 给出的 `≥c_0Δ` 下界矛盾。

本文不重新证明 PC1/PC2 的解析输入；它们在当前仓库中由以下文件承担：

- `docs/rh-pc1-landau-ingham-maintext-chain.md`；
- `docs/rh-pc1-external-input-standardization-audit.md`；
- `docs/rh-pc2-crt-baseline-maintext-appendix.md`；
- `docs/rh-pc2-baseline-unconditional-audit.md`；
- `docs/rh-gee0-load-distribution.md`；
- `docs/rh-gee0-pc2-boundary-and-route-overlap.md`。

## 2. 统一 Load 定义

令

`𝓔={A,PI,FCT,SC,LV,LSMP,CE,DSO,NRC}`

为九个 GEE 出口。对路由原子 `a` 定义超额偏差

`Excess(a)=max(0, σΣ_{n∈a}(w_X(n)-w_X^0(n)))`。

对任意出口 `E∈𝓔`，最终负担定义为

`Load(E;X)=Σ_{a routed finally to E} θ_{a,E} Excess(a)`，

其中 `θ_{a,E}` 是有限重叠路由权重，并满足全局有限重叠常数约束。

若某出口使用平方能量语言，则统一改写为

`ExcessEnergy=max(0, Energy-C_0·ZeroFrequencyCapacity)`。

因此以下对象不进入最终 `Load`：CRT/MLC/PI/DSO 零频容量本身；`A/FCT/SC` 的内部势函数下降步；`CE/LSMP` 已转出的 seed；`LV` 阈值失败并已转出的对象；`NRC` 非共振失败后转入其它出口的对象。

## 3. GEE-0 负担分配定理

**Theorem 3.1（GEE-0 bookkeeping）.** 在 PC1/PC2 与路由有限重叠成立时，存在常数 `c_0>0`，使得无穷成功尺度上

`Σ_{E∈𝓔} Load(E;X) ≥ c_0Δ+o(Δ)`。

**证明。** PC1 给出同向主异常，PC2 扣除 CRT 零频基线并把异常转为候选账本偏差。GEE-0 路由把每个异常原子分配到九类出口之一，且路由重叠由 `C_route` 控制。由于 `Load` 只登记 `w_X-w_X^0` 的同向超额，零频基线不重复计入，故路由后仍保留固定比例主异常。边界、素数幂、平滑端点与有限重叠误差由 `docs/rh-gee0-pc2-boundary-and-route-overlap.md` 吸收为 `o(Δ)`。证毕。

## 4. 九出口闭合矩阵

九出口在最终账本中的闭合口径如下。

| 出口 | 内联闭合机制 | 最终状态 |
|---|---|---|
| `LV` | 相对低体积阈值内直接给 `o(Δ)`，失败者转入其它出口 | 吸收闭合 |
| `NRC` | 单变量/Tail 非共振估计闭合；二维中容量经 PPI-Rank、Capacity、MidCap 分流 | 分流闭合 |
| `PI` | 投影容量扣除零频基线后只登记超额偏差 | 条件闭合 |
| `DSO` | square-function/Carleson 容量扣除基线后只登记超额偏差 | 条件闭合 |
| `CE` | coarea、薄层、平方可和项满足阈值即吸收，seed 转出 | 吸收/转出闭合 |
| `LSMP` | 低质量与结构小包满足阈值即吸收，seed 转出 | 吸收/转出闭合 |
| `FCT` | Noether 势函数内部下降；无下降则转出到接收出口 | 内部转移闭合 |
| `SC` | 短簇势函数内部下降；低容量吸收；重复模板转出 | 内部转移闭合 |
| `A` | ACC 同步势函数内部下降；容量吸收；固定模板重复转出 | 内部转移闭合 |

该矩阵内联自：

- `docs/rh-gee-lv-low-volume-exit-bound.md`；
- `docs/rh-gee-nrc-entry-parameter-table.md`；
- `docs/rh-nrc-2d-midcap-structure-route.md`；
- `docs/rh-gee-baseline-subtraction-lemma.md`；
- `docs/rh-gee-ce-lsmp-load-bound-audit.md`；
- `docs/rh-gee-seed-transfer-consistency.md`；
- `docs/rh-gee-fct-load-bound-audit.md`；
- `docs/rh-gee-sc-load-bound-audit.md`；
- `docs/rh-gee-a-load-bound-audit.md`。

## 5. 事件图与无循环定理

GEE 事件图的转出边为：

| 来源 | 目标 | 控制量 |
|---|---|---|
| `A` | `PI/FCT/SC/LV/LSMP/DSO/CE` | ACC 势函数下降或固定模板转出 |
| `FCT` | `NRC/DSO/PI/SC/LV/LSMP/CE` | Noether 势函数下降或闭包失败转出 |
| `SC` | `A/PI/FCT/LV/LSMP/CE` | 短簇势函数下降或重复短簇转出 |
| `CE/LSMP` | `A/PI/FCT/SC/LV/DSO/NRC` | Seed-Transfer 去重 |
| `NRC-2D` | `LSMP/LV/SC/PI/DSO/CE` | PPI-Rank/Capacity/MidCap 分流 |
| `PI/DSO` | `SC/LV/LSMP/CE/FCT/NRC` | Baseline-Subtraction 与 NoReturn |

定义 Lyapunov 向量

`𝓛=(𝓐pot,𝓝,𝓥,ExcessCap,ComplexityRank)`，

其中 `𝓐pot` 是 ACC 同步势，`𝓝` 是 FCT Noether 势，`𝓥` 是 SC 短簇势，`ExcessCap` 是扣除零频后的容量超额，`ComplexityRank` 是固定模板复杂度秩。

**Theorem 5.1（GEE Event No-Cycle）.** 在 Seed-Transfer、Baseline-Subtraction、A/FCT/SC 势函数账本、PI/DSO 容量账本、LV/LSMP/CE 吸收阈值与 NRC 分流定理成立时，GEE 事件图不存在承载正 `Load` 的无限有向循环。

**证明。** 自环方面，`A`、`FCT`、`SC` 每次内部保留都分别使 `𝓐pot`、`𝓝`、`𝓥` 严格下降；若不下降，则按定义转出，不再作为同一内部状态保留。`PI/DSO` 自环只可能来自重复投影容量，但零频容量已扣除，超额部分由 Carleson/square-function 容量消耗。`CE/LSMP` 不保留 seed；`LV/NRC` 是吸收或分流节点。

混合环方面，若环经过 `A/FCT/SC`，则对应势函数在每次返回时下降，有限次后终止；若环避开这些节点，则只包含吸收、基线扣除、seed 分类或非共振分流节点，它们不能保持同一正 `Load` 回流。故沿任何非吸收路径，`𝓛` 按字典序下降或容量超额被扣除。由于各分量有下界且复杂度有限，不存在无限正负担循环。证毕。

## 6. 阈值常数层级

设总对数损失常数

`C_total=C_route+C_seed+C_dyadic+C_Vaaler+C_Fourier+C_smooth+C_frame+C_template+C_capacity+C_NRC+C_coarea+C_boundary+100`。

选择

`B_final=10C_total+100`，

并要求各出口阈值满足

`B_E ≥ B_final+C_total`。

**Theorem 6.1（Threshold Compatibility）.** 若所有局部对数损失均由 `C_total` 支配，并按上式选择阈值，则所有可吸收项贡献总和为 `o(Δ)`；内部转移和 seed 转出不改变该估计。

**证明。** 任一可吸收入口给出

`Contribution ≤ Δ/log^{B_E-C_entry}X`, `C_entry≤C_total`。

所有路由重叠、dyadic 分解、Vaaler/Fourier 截断、平滑边界、容量 frame 与 seed 重标记再损失至多 `log^{C_total}X`。由 `B_E≥B_final+C_total` 得总贡献 `≤Δ/log^{B_final}X=o(Δ)`。内部转移不登记最终负担；seed 转出只改变标签并由 `C_seed` 计入 `C_total`。证毕。

## 7. 九出口上界定理

**Theorem 7.1（GEE Exit Upper Bound）.** 假设第 4 节矩阵中每个出口的局部闭合机制成立，且第 5、6 节事件图与阈值层级成立，则

`Σ_{E∈𝓔} Load(E;X)=o(Δ)`。

**证明。** `LV/CE/LSMP/NRC_abs` 等吸收项由 Theorem 6.1 给 `o(Δ)`。`PI/DSO` 的零频容量不计入 `Load`，超额偏差由容量账本吸收或转出，因此最终登记量为 `o(Δ)`。`A/FCT/SC` 的内部保留步由对应势函数有限终止；不能终止的对象按事件图转入其它出口，且由 Theorem 5.1 不可能形成正负担自由循环。每个转出 seed 由 Seed-Transfer 从源出口删除并进入唯一接收账本，有限重叠损失已包含在 `C_total`。因此所有最终登记出口只剩可吸收项，总和为 `o(Δ)`。证毕。

## 8. GEE 合成矛盾定理

**Theorem 8.1（GEE Conditional Synthesis）.** 假设 PC1/PC2/GEE-0、九出口局部闭合机制、事件图无循环、阈值常数层级与统一 `Load` 口径均成立，则不存在离线零点 `β>1/2`。

**证明。** 反设离线零点存在。Theorem 3.1 给出

`Σ_E Load(E;X) ≥ c_0Δ+o(Δ)`。

另一方面 Theorem 7.1 给出

`Σ_E Load(E;X)=o(Δ)`。

当 `X` 沿成功尺度趋于无穷时，二者矛盾。因此在上述全部输入成立时，不存在离线零点。证毕。

## 9. 顶刊审稿义务清单

本文完成的是单篇主稿内联化的第一版：定义、出口矩阵、事件图、阈值表和合成定理已在同一文档中闭合。但顶级数学期刊标准仍要求以下逐项完成：

1. **外部输入精确引用。** PC1 的 Landau--Ingham/显式公式输入、NRC 使用的完成和或大筛输入、PI/DSO 的 Carleson/square-function 输入，必须给出正式定理编号、适用范围和常数依赖。
2. **命名引理逐条证明。** `Seed-Transfer`、`Baseline-Subtraction`、`PPI-Rank`、`MidCap-Structure`、`A/FCT/SC` 势函数下降等，需从当前引用文档迁入正式附录或主文证明。
3. **符号一致性。** `X,z,M,Δ,B_E,C_total,Load,Excess` 必须在最终 LaTeX 主稿中唯一命名，避免旧稿中 `Σ|bias|` 与超额偏差混用。
4. **常数可追踪性。** 若要求显式有限验证阈值，则必须把 `C_total` 的每一项替换为具体整数；当前稿只给出渐近对数余量方案。
5. **不可过度宣称。** 在以上义务完成前，本文只能称为 RH/GEE 条件合成审稿稿，不能称为 RH 无条件证明定稿。

## 10. 归档结论

本稿把 GEE 合成层面的最后四项义务压缩为一篇内联证明框架：九出口矩阵、事件图无循环、阈值常数与 `Load` 口径已经统一。剩余工作已明确定位为外部定理精确引用和命名引理逐条内联证明。故当前最优下一步不是新增出口，而是把第 9 节清单逐项转写进正式 LaTeX 主稿。
