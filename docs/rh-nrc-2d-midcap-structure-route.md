# NRC-2D MidCap-Structure 中间容量层分流路线

本文专攻 `docs/rh-nrc-2d-capacity-match-audit.md` 留下的唯一硬点：

`Δ/log^A X < V_Q < P log^D X`

的中间容量层若承载固定比例 PPI 可检测偏差，为什么必须触发 `LSMP/SC/PI/CE`。本文给出审稿安全的四触发判据，把“中间容量”从模糊硬点压缩为四个具体接口；但不伪称四个接口已经全部无条件闭合。

## 1. 中间容量层的含义

在 PPI 双锚层 `q_1,q_2~Q`, `r~R`, `Q^2R~X` 中，`V_Q` 表示当前相位/窗口包的有效零频容量。中间层同时满足：

1. `V_Q` 大于全局低体积阈值，故不能直接由 `GEE-LV` 吸收；
2. `V_Q` 小于 `Plog^D X`，故二维低秩 NRC 的 `Plog^C X` 背景不能相对压小；
3. 窗口偏差达到固定比例，即 `|Bias(A)| >= cV_Q/log^C X`。

这意味着偏差存在，但自由度不足。唯一可能性是质量在某个结构方向上被压缩。

## 2. 四种压缩方向

把有效容量按三个坐标投影：尾因子 `r`、物理短窗 `n=q_1q_2r`、相位盒 `A(Θ)`，以及窗口描述复杂度。若不存在任何结构压缩，则容量应以零频方式铺开，回到高容量相对小或 Uniform 容量界。因此中间层必须落入以下之一。

### 2.1 尾因子薄层：LSMP/LV

若有效质量由少数 `r` 层承载，即存在 `R_*` 个尾层使

`Σ_{r∈R_*}V(r) >= cV_Q`, `R_* <= log^C X` 或每层质量低于 coarea 阈值，

则这是薄层/小质量结构。按 `LV/LSMP/CE` 主文吸收链，低总量进入 `LV`，不可吸收的同向偏差进入 `LSMP` 并输出 `PI_seed/FCT_seed`。

### 2.2 物理短簇集中：SC

若质量集中在少数物理短窗 `I`，使某个短窗族承载

`Σ_I V(I;Q,R) >= cV_Q`,

且其局部容量超过 `SC-Local-Product-Capacity-Dyadic` 的

`Vol_eff(I;Q,R) << (|I|/X)RQlog^C X + Rlog^C X`,

则触发短簇 `SC` 或其失败出口 `PI/A/FCT/LV/LSMP/SC`。若局部容量界未超，则这些短窗总贡献不足以承载固定比例偏差。

### 2.3 相位盒/投影集中：PI

若同一有限模板相位盒在多层或多相邻窗口中重复承载固定比例偏差，即存在允许投影模板 `𝓦_*` 使

`Σ_j |Bias(A_j)| >= cΣ_j V(A_j)/log^C X`,

则这是高投影增量种子。按 PI 主链，它进入 lacunary Carleson 或 dense-scale orthogonality 分支；若 PI 容量失败，则由 DSO/PI 容量终端接收。

### 2.4 模板复杂度集中：CE

若以上三类均不发生，但仍需超过固定模板深度、超过 Vaaler 截断高度或使用超多相位盒才能描述偏差，则它不属于 PPI 主层固定模板。按 CE 分类器，分别转入频率复杂度、尾项能量、旧坐标重写或边界体积逃逸。

## 3. 非压缩反面：Uniform 容量排斥

若尾因子不薄、物理短窗不集中、相位盒不重复集中、模板复杂度固定，则质量对 PPI partition 的每个原子都处于零频均匀背景。由 `OV2/MLC Uniform` 容量界，非终端分支满足

`E_unif(Q,R) <= W_Q log^C X`。

若它仍承载固定比例 PPI 偏差，则 PPI-U2 会抽出一个允许窗口；该窗口又与“不发生相位盒/投影集中”矛盾。因此非压缩中间层不能存在。

这里的逻辑是反面判别：中间容量层要么被某个坐标投影压缩，要么均匀；均匀则不产生固定比例可检测偏差。

## 4. Theorem MidCap-Structure（分流版）

**Theorem MidCap-Structure-Reduction.** 假设 `PPI-Rank`、`Capacity-Match-Safe`、SC 局部容量界、LV/LSMP/CE 吸收链与 PI 容量主链接收规则均可引用。若中间容量层

`Δ/log^A X < V_Q < P log^D X`

承载固定比例 PPI 可检测偏差，则以下至少一项发生：

1. 尾因子薄层或小质量原子，进入 `LSMP/LV`；
2. 物理短窗局部乘积容量异常，进入 `SC` 或其命名失败出口；
3. 允许投影模板重复承载偏差，进入 `PI/DSO`；
4. 固定模板复杂度、Vaaler 尾项或边界描述失败，进入 `CE/LSMP/LV`。

**证明。** 对有效质量按尾因子、物理短窗、相位盒和模板复杂度四个投影作层蛋糕分解。若某一投影有固定比例集中，则分别落入 1--4。若四者均无固定比例集中，则质量在固定复杂度 partition 上均匀铺开；由 Uniform 容量界和 PPI-U2 的逆否命题，不能承载固定比例窗口偏差，矛盾。因此至少一项发生。证毕。

## 5. 审稿义务矩阵

| 接口 | 当前已有文档 | 状态 |
|---|---|---|
| 尾因子薄层 -> LSMP/LV | `docs/rh-lv-lsmp-ce-maintext-absorption-chain.md` | 可引用，但需最终常数排序 |
| 短窗集中 -> SC | `docs/rh-sc-local-product-capacity-dyadic-audit.md` | 条件化可审查 |
| 相位盒重复 -> PI/DSO | `docs/rh-pc4-pi-cap-carleson.md`, `docs/rh-pi-dso-maintext-bridge-chain.md` | 仍依赖 PI dense/lacunary 闭合 |
| 复杂度逃逸 -> CE | `docs/rh-lv-lsmp-ce-maintext-absorption-chain.md` | 可引用，若分类失败则是接口缺口 |
| 非压缩均匀排斥 | `docs/rh-ov2-mlc-uniform-capacity-constants-audit.md` | 条件化可审查 |

因此 `MidCap-Structure` 已压缩为 PI/DSO 容量主链与常数排序问题；它不是新的解析 NRC 难题。

## 6. 对 NRC-2D 的影响

结合：

- `PPI-Rank` 有限分离秩；
- `Capacity-Match-Safe` 三分；
- 本文 `MidCap-Structure-Reduction`；

二维加性分离 NRC 入口可以改写为：高容量相对小，低体积进 LV，中间容量必转 `LSMP/SC/PI/CE/DSO`。因此 `NRC-2D` 本身不再是独立解析出口；剩余压力转移到全局 `PI/DSO/SC/LSMP/CE` 出口上界。
