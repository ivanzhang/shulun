# Global-Exit-Exclusion：最终核心矛盾不等式目标

本文集中攻当前 RH 反例矛盾场的最小真正硬点：把“所有异常都进入已命名出口”升级为“所有已命名出口的总容量为 `o(Δ)`，因此与 PC1--PC2 给出的 `≥cΔ` 异常矛盾”。本文是顶刊审稿口径的核心目标定理；它不假装已经证明 RH，而是把最后需要证明的定量不等式完整显式化。

## 1. 为什么需要本定理

当前链条已经把离线零点异常送入有限出口集合

`𝓔={A,PI,FCT,SC,LV,LSMP,CE,DSO,NRC}`。

但是“进入已命名出口”不等于矛盾。真正需要证明的是：每个出口可承载的离线零点同向异常量都有上界，并且这些上界总和小于主异常。

因此最终闭合必须具有如下形式：

`c_0Δ <= Σ_{E∈𝓔} Load(E;X) + Err(X) <= o(Δ)`，

从而矛盾。

## 2. 出口负担量定义

对每个成功尺度 `X_j`，定义 `Load(E;X_j)` 为被路由到事件 `E` 的 Chebyshev 加权同向异常绝对负担。要求满足：

1. **分配完备性**：PC1--PC2--C3--C4/C5 后的异常被 `𝓔` 与可吸收误差完全覆盖；
2. **有限重叠**：每个原始异常原子进入至多 `log^C X` 个出口负担；
3. **同权口径**：所有负担使用同一 Chebyshev 权与同一平滑窗口；
4. **误差可吸收**：尾项、边界、dyadic pigeonhole 损失合计为 `X^{o(1)}` 或 `o(Δ)`。

于是需要先证明负担分配不等式：

**(GEE-0)** `c_0Δ <= Σ_E Load(E;X)+o(Δ)`。

GEE-0 是纯 bookkeeping 定理，依赖 PC1、PC2、C3、C4、C5。

## 3. 九个出口上界目标

### 3.1 A/ACC 同步出口

目标上界：

**(GEE-A)** `Load(A;X) <= o(Δ)`，除非触发 `PI/FCT/SC/LV/LSMP/CE/DSO` 中某个已计入出口。

所需证明：固定 ACC 模板重复同向过剩不能超过 square-function/投影/低体积容量预算。当前 C6 只给无循环结构，还需要定量上界。

### 3.2 PI 投影出口

目标上界：

**(GEE-PI)** `Load(PI;X) <= o(Δ)`。

所需证明：lacunary 容量与 dense martingale/Carleson 容量之和，在固定模板和有限重叠下小于离线零点异常。必须显式比较 PI energy `e_j=δ_j^2 μ_j^0(A_j)` 与线性负担 `Load(PI)`。

### 3.3 FCT 频率闭包出口

目标上界：

**(GEE-FCT)** `Load(FCT;X) <= o(Δ)`。

所需证明：Noether 下降只能排除无限递归；还需证明有限闭包状态承载同向异常时，会被 PI/SC/DSO/NRC 的定量上界吸收，而不是停在 FCT 中。

### 3.4 SC 短簇出口

目标上界：

**(GEE-SC)** `Load(SC;X) <= o(Δ)`。

所需证明：短窗内 `q_1q_2r` 锚复用局部乘积容量 `Vol_eff(I;Q,R)` 的 dyadic 总和小于 `Δ`，或者强制进入 A/PI/FCT/LV/LSMP/CE 并由对应上界吸收。

### 3.5 LV 低体积出口

目标上界：

**(GEE-LV)** `Load(LV;X) <= Vol_eff(X) log^C X = o(Δ)`。

这是最容易的出口，但需要把每个 LV 入口的 `Vol_eff` 明确写出，并统一证明 `Vol_eff log^C X=o(Δ)`。

### 3.6 LSMP 小质量/薄层出口

目标上界：

**(GEE-LSMP)** `Load(LSMP;X) <= o(Δ)`。

所需证明：薄层 coarea、小质量原子和频率原子分散的总质量在全 dyadic 层上可求和；若方向筛选输出 PI/FCT seed，则负担转入 PI/FCT，不重复计数。

### 3.7 CE 复杂度逃逸出口

目标上界：

**(GEE-CE)** `Load(CE;X) <= o(Δ)`。

所需证明：复杂度逃逸不能作为大量独立原子出现。要证明每一次复杂度增加要么消耗全局复杂度预算，要么输出到 FCT/LSMP/LV/PI；全局复杂度预算总贡献为 `o(Δ)`。

### 3.8 DSO 正交出口

目标上界：

**(GEE-DSO)** `Load(DSO;X) <= o(Δ)`。

所需证明：新增独立频率包的 square-function 能量由 Parseval/martingale 控制；从平方能量上界推出线性同向负担上界时，必须处理 Cauchy 损失和包数量，保证仍为 `o(Δ)`。

### 3.9 NRC 非共振出口

目标上界：

**(GEE-NRC)** `Load(NRC;X) <= o(Δ)`。

所需证明：非共振倒数和经 `EXT-KL` 完成法得到 `p^{1/2}log^C p` 型上界；经过主层体量、dyadic 求和、Vaaler 截断后，仍严格小于 `Δ`。这是外部引用与参数匹配共同硬点。

## 4. 全局出口排斥定理（目标版）

**Theorem GEE-Target（Global-Exit-Exclusion，目标版）。** 假设 GEE-0 与九个出口上界 GEE-A、GEE-PI、GEE-FCT、GEE-SC、GEE-LV、GEE-LSMP、GEE-CE、GEE-DSO、GEE-NRC 全部成立，则 ζ 函数不存在离线零点 `β>1/2`。

**证明。** 反设存在离线零点。PC1 给 `Δ=X^{β-o(1)}` 级同向异常；PC2/C3/C4/C5 把异常分配到出口集合并给 GEE-0：

`c_0Δ <= Σ_E Load(E;X)+o(Δ)`。

九个出口上界给

`Σ_E Load(E;X) <= o(Δ)`。

于是 `c_0Δ <= o(Δ)`，矛盾。证毕。

## 5. 当前已知进度与缺口

| 项 | 当前状态 | 是否顶刊闭合 |
|---|---|---|
| GEE-0 | `docs/rh-gee0-load-distribution.md` + `docs/rh-gee0-pc2-boundary-and-route-overlap.md` | bookkeeping 闭合 |
| GEE-LV | `docs/rh-gee-lv-low-volume-exit-bound.md` | 闭合：相对 `Δ` 低体积阈值下为 `o(Δ)`，失败转其它出口 |
| GEE-NRC | `docs/rh-gee-nrc-nonresonant-exit-bound.md` + `docs/rh-gee-nrc-entry-parameter-table.md` | 单变量与 Tail/RKS 分流闭合；剩 `NRC-2D` 与 `DSO-SF` |
| GEE-DSO | 有 square-function 思路；缺线性负担转换 | 未闭合 |
| GEE-PI | 有 lacunary/dense 分类；缺总容量到 `o(Δ)` | 未闭合 |
| GEE-FCT | 有 no-cycle；缺有限状态负担上界 | 未闭合 |
| GEE-SC | 有局部乘积容量框架；缺全 dyadic 求和 | 未闭合 |
| GEE-LSMP | 有 coarea/薄层路线；缺全局可求和 | 未闭合 |
| GEE-CE | 有分类器；缺复杂度预算总上界 | 未闭合 |
| GEE-A | 有同步压力；缺定量负担上界 | 未闭合 |

## 6. 下一步最优攻坚顺序

1. **专攻 `NRC-2D`**：双变量倒数包必须给无幂损失压缩，避免 `Q·P^{1/2}` 逃逸。
2. **专攻 `DSO-SF`**：square-function 到线性负担转换必须无幂损失。
3. **再攻 GEE-A/FCT/SC/LSMP/CE/PI**：这些依赖全局势函数和复杂度预算。

## 7. 审稿口径

在 GEE-0 和九个 GEE-* 上界全部证明前，当前 RH 文档包不能称为无条件证明。正确表述是：结构分支已经压缩为有限出口集合；最终证明等价于 Global-Exit-Exclusion 的十个定量不等式。

## GEE-NRC 入口参数核验补充

详见 `docs/rh-gee-nrc-entry-parameter-table.md`。当前审查结论为：单变量 PPI 与 Tail/RKS 分流已可闭合；双变量 PPI 仍需 `NRC-2D` 无幂损失完成和；DSO-E 仍需 `DSO-SF` 无幂损失 square-function 总量。因此 `GEE-NRC` 不得标记为完全无条件闭合。

## NRC-2D 专项状态

新增 `docs/rh-gee-nrc-2d-bilinear-hardpoint.md`。当前最小硬点已从“二维 NRC 泛泛未闭合”压缩为：证明加性分离相位的 `PPI-Rank` 有限秩窗口引理与 `Capacity-Match` 主层容量门槛；若出现乘积倒数相位，再单独调用 `EXT-BG` 支路。

## PPI-Rank 状态更新

新增 `docs/rh-ppi-rank-finite-separation-lemma.md`。`NRC-2D` 的有限秩义务已转为可审查引理；当前剩余为 `Capacity-Match` 容量门槛。

## Capacity-Match 状态更新

新增 `docs/rh-nrc-2d-capacity-match-audit.md`。`NRC-2D` 当前不再是解析估计问题，而是中间容量层结构问题：需证明 `MidCap-Structure`，把 `Δ/log^A X<V_Q<Plog^D X` 的偏差层送入 `LSMP/SC/PI/CE`。

## NRC-2D 分流闭合状态

新增 `docs/rh-nrc-2d-midcap-structure-route.md`。`GEE-NRC` 的二维加性分离入口已分流：高容量相对小、低体积转 LV、中间容量转 `LSMP/SC/PI/CE/DSO`。因此 `GEE-NRC` 的剩余压力主要回到 `GEE-PI/GEE-DSO/GEE-SC/GEE-LSMP/GEE-CE`，而非 NRC 解析估计。

## GEE-PI/DSO 负担目标

新增 `docs/rh-gee-pi-dso-load-bound-target.md`。PI/DSO 当前从“桥接无回流”升级为明确负担目标：需证明 `Lac-Baseline`、`Dense-Carleson` 与 `Anomaly-L2-Control` 三项，才能推出 `Load(PI)+Load(DSO)=o(Δ)`。最硬点为 `Dense-Carleson`。

## Dense-Carleson 状态更新

新增 `docs/rh-gee-dense-carleson-load-bridge.md`。`GEE-PI/DSO` 最硬点已从 dense 正交转为基线账本：需证明 `Baseline-Subtraction`，即 PI/DSO 的零频容量只作基线扣除，进入 `Load` 的仅为超额偏差。

## GEE-PI/DSO 基线扣除更新

新增 `docs/rh-gee-baseline-subtraction-lemma.md`。PI/DSO 的 lacunary/dense 零频容量不再重复计入异常负担；`Load(PI)+Load(DSO)` 只登记超额偏差。因此 `GEE-PI/DSO` 当前可作为条件闭合出口，依赖接收出口 `SC/LV/LSMP/CE/FCT/NRC` 的全局上界。

## GEE-CE/LSMP 负担审查

新增 `docs/rh-gee-ce-lsmp-load-bound-audit.md`。CE/LSMP 被拆成可吸收项与 seed 转出项；可吸收项给 `o(Δ)`，seed 必须转入对应出口并从 CE/LSMP 删除。剩余硬点为 `Seed-Transfer Consistency`。

## GEE-CE/LSMP Seed-Transfer 更新

新增 `docs/rh-gee-seed-transfer-consistency.md`。CE/LSMP 的 seed 转出账本已闭合：seed 不再计入 CE/LSMP，而有限重叠转入 `A/PI/FCT/SC/LV/DSO/NRC`。`GEE-CE/LSMP` 当前可标记为吸收项闭合、seed 转出一致。

## GEE-FCT 内部转移更新

新增 `docs/rh-gee-fct-load-bound-audit.md`。FCT 被重新定义为内部 Noether 化简器：真下降步不登记最终负担，重复状态和独立频率转入目标出口；因此最终 `Load(FCT)=0`。剩余压力转入 `GEE-SC/GEE-A` 及已接收出口。

## GEE-SC 内部转移更新

新增 `docs/rh-gee-sc-load-bound-audit.md`。SC 被改写为容量吸收与内部递归转移：低容量短簇给 `o(Δ)`，真 shorter_SC 步不作最终负担，重复模板转入 `A/PI/FCT/LV/LSMP/CE`。因此 `GEE-SC` 可标记为内部转移闭合。
