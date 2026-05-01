# LSMP/FCT/CapacityFail 最终闭合强度审稿

本文接续 `docs/rh-dso-capacity-final-audit.md`。目标是核查最后三类高频出现的“剩余出口”——`LSMP`、`FCT` 与 `CapacityFail`——是否都已被压成可审查定理族或命名容量义务，而不是新的自由逃逸通道。

## 1. 总矩阵

| 出口 | 核心文档 | 成功/吸收 | 失败/后继 |
| --- | --- | --- | --- |
| `LSMP` | `docs/omr-cgtp-lsmp-theoremization.md`, `docs/rh-pc4-lsmp-frequency-corollary.md` | coarea/DPI 吸收小质量原子 | 输出 PI/FCT 或 NRC 失败 |
| `FCT` | `docs/fct-tree-wfe-theoremization.md`, `docs/rh-pc4-fct-noether-descent-ledger.md` | 短深度 span 计数 + Noether 终止 | 输出 PI/SC/LV/LSMP/CE |
| `CapacityFail` | 具体容量文档绑定 | 已证容量则矛盾 | 未证则列入对应容量文档，不得自由回流 |

## 2. LSMP 闭合强度

LSMP 的两个核心步骤是：

1. **离散 coarea**：小质量块族经 dyadic 厚度层选择，抽出有限重叠薄层族；
2. **DPI**：若薄层族同向偏移不可吸收，则产生允许窗口上的高投影增量，或 NRC 失败进入 FCT。

`docs/rh-pc4-lsmp-frequency-corollary.md` 已给频率原子版：大局部复杂度若无重 span、无重可控子集，则质量分散到小原子，进入 LSMP。故 LSMP 的合法出口只有：吸收、PI、FCT、NRC，不存在独立非终端。

## 3. FCT 闭合强度

FCT 分两层：

1. `docs/fct-tree-wfe-theoremization.md`：NRC 失败给短深度 span 证书，Tree-WFE 把无限生成树路径转成短簇、高投影增量或频率闭包终端；
2. `docs/rh-pc4-fct-noether-descent-ledger.md`：频率闭包终端若继续跨尺度逃逸，则离散 Noether 势函数下降；若不下降，固定低维 Bohr 模板重复并转 PI/SC/LV/LSMP/CE。

因此 FCT 不再是“共振失败”的黑洞，而是一个有 span 计数、树状账本和跨尺度 Noether 终止的结构终端。

## 4. CapacityFail 绑定清单

任何 `CapacityFail` 必须绑定以下具体文档之一：

- `DSO`：`docs/rh-dso-capacity-final-audit.md`；
- `PI`：`docs/rh-pc4-pi-lacunary-capacity.md`、`docs/rh-pc4-pi-cap-carleson.md`；
- `SC`：`docs/rh-pc4-short-cluster-local-density.md`；
- `OV2/MLC`：`docs/rh-ov2-mlc-unconditional-core.md`、`docs/rh-ov2-mlc-uniform-absorption.md`；
- `DGap`：`docs/rh-pc4-dual-box-overlap.md`、`docs/rh-pc4-dual-projection-orthogonalization.md`；
- `AAI/主层`：`docs/rh-ov2-main-layer-capacity-interface.md` 及其无条件核心。

若未指明具体容量文档，审稿时应视为未闭合引用；若已指明且容量定理成立，则 `CapacityFail` 是矛盾或转入该容量文档定义的命名事件。

## 5. 最终闭合定理

**Theorem LSMP-FCT-Capacity-Final-Audit。** 当前总攻链条中，`LSMP`、`FCT` 与 `CapacityFail` 均不提供未命名最终逃逸通道：LSMP 只能吸收或输出 PI/FCT/NRC；FCT 只能通过 Tree-WFE/Noether 账本终止或输出 PI/SC/LV/LSMP/CE；CapacityFail 必须绑定具体容量定理，不能自由回流。

**证明。** LSMP 由 coarea 与 DPI 二分，失败即 PI 或 FCT/NRC。FCT 由短深度 span 计数和 Tree-WFE 处理单尺度递推，再由 Noether 下降账本处理跨尺度闭包。CapacityFail 按第 4 节绑定到具体容量文档；若无绑定则不允许作为事件图边，若有绑定则由对应文档处理。证毕。

## 6. 剩余工作定位

到此，PC1/PC2/PC3 上游、NRC/EXT、DSO/容量、LSMP/FCT/CapacityFail 均已有审稿矩阵。下一步最优任务是做全文最终一致性总审查：检查清单、索引、提交包、未跟踪文件说明与“不能宣称 RH 已证明”的口径是否一致。
