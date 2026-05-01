# 容量定理常数与适用条件统一核验表

本文补强 `docs/rh-capacityfail-binding-table.md`：不仅要求每个 `CapacityFail` 绑定到具体容量文档，还要求每个容量定理的适用条件、损失类型、常数余量和失败出口可审查。本文不宣称 RH 已证明；它把容量黑箱压缩为可逐项核验的接口矩阵。

全局 `log^C X` 常数层级排序见 `docs/rh-global-log-constant-hierarchy-audit.md`。

## 1. 统一核验字段

每个容量定理必须给出六个字段：

1. **对象**：被计数或被控的窗口/锚/频率/盒族；
2. **适用条件**：固定复杂度、有限重叠、自然细化、非低体积等；
3. **容量界**：平方能量、体积、Carleson、局部乘积或 dyadic 上包络；
4. **允许损失**：`log^C X` 或 `X^{o(1)}`；
5. **常数余量来源**：主异常 `X^{β-o(1)}` 与 `β>1/2`、或 dyadic/CRT 对数余量；
6. **失败出口**：失败不能裸回流，必须进入命名事件。

## 2. 容量核验总表

| 容量接口 | 对象 | 适用条件 | 容量界 | 允许损失 | 失败出口 |
| --- | --- | --- | --- | --- | --- |
| DSO-C | CRT martingale 差分 | 同一固定模板自然细化 | `Σ||D_kF||_2^2<=||F||_2^2` | 常数/有限重叠 | TC/CE/LSMP/FCT/LV |
| DSO/PI bridge | 新增独立频率包 | 包是允许投影有限交；无回流审查见 `docs/rh-pi-dense-dso-bridge-no-return-audit.md` | square-function 反馈 PI | `log^C X` | PI 或 DSO 容量终端 |
| PI-lacunary | lacunary 尺度投影包 | Mellin 支撑强分离 | 有限重叠/Carleson | `log^C X` | dense DSO/SC/LV/CE |
| PI-dense/Carleson | dense 投影包 | 固定模板、可拉回 DSO；无回流审查见 `docs/rh-pi-dense-dso-bridge-no-return-audit.md` | Carleson/平方函数 | `log^C X` | DSO/CE/LSMP/FCT |
| SC 局部乘积 | 短窗 `q_1q_2r` 锚复用 | dyadic 层固定、非低体积；逐层核验见 `docs/rh-sc-local-product-capacity-dyadic-audit.md` | `Vol_eff(I;Q,R)` | `log^C X` | PI/A/FCT/LV/LSMP |
| OV2/MLC | 主层双锚能量 | AAI 正规形、主层分离；Uniform 常数化见 `docs/rh-ov2-mlc-uniform-capacity-constants-audit.md` | 主层容量/Uniform 零频 | `X^{o(1)}` | PPI/FCT/SC/LV/DSO/PI |
| AAI | 允许锚上包络 | 整除正规形、dyadic 分层 | divisor/dyadic 上包络 | `log^C X` | MLC 或代数矛盾 |
| DGap 盒重叠 | 物理窗×层×相位盒 | dyadic 网格、固定相位模板 | 点态重叠 `log^C X` | `log^C X` | LV/CE/LSMP/FCT |
| DGap 投影 | 盒空间 frame | 有限重叠、常数方向剥离 | frame 上界转投影能量 | `log^C X` | PI/FCT/SC/LV/CE |
| FCT/LSMP 容量 | 低维闭包/小质量原子 | span 计数、Noether 下降 | 终止或小质量吸收 | `log^C X` | PI/SC/LV/LSMP/CE |
| PC2 基线 | CRT 零频基线 | Mertens/CRT 初等估计 | `C_z-C_z^0=o(Δ)` | `X^{o(1)}` | PC2 接口失败 |

## 3. 常数余量统一口径

所有容量估计只允许以下两类损失：

1. 多对数损失 `log^C X`；
2. 可写作 `X^{o(1)}` 的固定复杂度损失。

PC1 给出的离线零点异常为 `X^{β-o(1)}`，`β>1/2`。PC2/PC3/PC4 的容量损失若保持在 `X^{o(1)}`，不会改变主指数。若某接口需要固定正幂损失 `X^ε` 且无法吸收，则必须登记为未闭合容量硬点；当前正式入口未允许这种损失作为已闭合容量。

## 4. 适用条件失败的规范出口

容量定理不适用时，不能写成 `CapacityFail` 直接回流；必须按失败原因分流：

- 固定复杂度失败：`CE/LSMP/FCT`；
- 有限重叠失败：`LV/SC/CE`；
- 自然细化失败：`CE/FCT/DSO-PI`；
- 非低体积失败：`LV/LSMP/SC`；
- 非共振失败：`FCT`；
- dense/lacunary 分解失败：转另一尺度包或 `DSO`。

这使 `CapacityFail` 只是审稿标签，不是数学终端。

## 5. 核验定理

**Theorem Capacity-Constants-Applicability-Audit（条件化）。** 当前正式 RH 反例矛盾场文档中的容量使用均可登记到第 2 节表格。每个容量接口的损失均被要求为 `log^C X` 或 `X^{o(1)}`；若适用条件失败，则失败出口按第 4 节进入已命名事件，不形成自由回流。

**证明。** 第 2 节逐项列出当前 `CapacityFail` 绑定表中的容量接口，并补齐对象、适用条件、容量界、损失和失败出口。第 3 节统一常数余量，排除正幂损失被误写成闭合。第 4 节规定适用条件失败只能按结构转入命名事件。故容量接口在当前文档包中是可审查的条件化输入。证毕。

## 6. 剩余真正硬点

本文不是逐个容量定理的完整外部证明。继续无条件化时，真正剩余是：

1. 对 SC 局部乘积容量与 AAI/LV 常数层级做最终排序；
2. 对 OV2/MLC Uniform 与 PPI 阈值常数层级做最终排序；
3. 对 PI dense/Carleson 与 DSO bridge 的适用条件同全局事件图做最终交叉引用；
4. 在最终论文中按 `docs/rh-global-log-constant-hierarchy-audit.md` 改写匿名常数。
