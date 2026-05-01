# CapacityFail 全局绑定表

本文执行 `docs/rh-unconditional-proof-roadmap.md` 的第一硬点 `R2-CapacityBinding`：把当前正式审稿入口中的 `CapacityFail`、容量失败、容量界失败逐项绑定到具体容量文档。

## 1. 绑定总表

| 出现语境 | 绑定容量 | 文档 | 状态 |
| --- | --- | --- | --- |
| DSO/正交能量失败 | DSO martingale square-function / DSO-E 局部平方控制 | `docs/rh-dso-capacity-final-audit.md`, `docs/rh-pc4-dso-crt-martingale.md` | 已绑定；失败转 PI/FCT/LSMP/NRC/CE |
| PI lacunary 包超容量 | Mellin 有限重叠/Carleson 容量 | `docs/rh-pc4-pi-lacunary-capacity.md`, `docs/rh-pc4-pi-cap-carleson.md` | 已绑定；失败转 SC/LV/CE/PI 极端 |
| SC 短窗锚复用过密 | 局部乘积容量 `Vol_eff(I;Q,R)` | `docs/rh-pc4-short-cluster-local-density.md` | 已绑定；失败转 PI/A/FCT/LV/LSMP 或容量矛盾 |
| OV2/MLC 主层能量 | 双锚主层容量、低尾层容量、Uniform 零频容量 | `docs/rh-ov2-mlc-unconditional-core.md`, `docs/rh-ov2-mlc-uniform-absorption.md` | 已绑定；失败转主层/PPI/FCT/SC/LV/DSO/PI |
| DGap 盒有限重叠 | 物理窗/dyadic/相位盒有限重叠 | `docs/rh-pc4-dual-box-overlap.md` | 已绑定；失败转 LV/CE/LSMP/FCT |
| DGap 投影正交化 | 盒空间 Gram 上界与投影分解 | `docs/rh-pc4-dual-projection-orthogonalization.md` | 已绑定；失败转 PI/FCT/SC/LV/CE |
| AAI 允许锚容量 | 整除上包络与双锚正规形 | `docs/rh-ov2-aai-unconditional-theorem.md`, `docs/rh-ov2-main-layer-capacity-interface.md` | 已绑定；AAI 代数无条件，主层转 MLC |
| DGap/PC2 基线接口失败 | CRT 基线误差容量 | `docs/rh-pc2-baseline-unconditional-audit.md` | 已绑定；PC2 初等无条件 |

## 2. 未绑定项扫描结论

在当前正式入口中，`CapacityFail` 不再作为自由事件出现；它总是指向某个容量文档或接口失败文档。真正待攻的不是“找不到绑定”，而是各绑定文档的证明强度排序。

## 3. 强度排序

从最需要继续逐行化的角度排序：

1. **DGap 投影正交化**：frame 上界与逐步正交投影补强见 `docs/rh-dgap-projection-line-by-line-audit.md`；剩余为低维抽取、误差逃逸和盒模板统一；
2. **SC 局部乘积容量**：短窗内 `q_1q_2r` 自由度估计需保持对所有 dyadic 层一致；
3. **PI lacunary/Carleson 容量**：当前主要解决 lacunary，dense 依赖 DSO；
4. **OV2/MLC Uniform 容量**：已转多出口，但 Uniform 零频容量需最终常数化；
5. **DSO martingale 容量**：Hilbert 部分最稳，主要剩模板一致性细节。

## 4. R2 结论

**Proposition R2-CapacityBinding。** 当前正式审稿入口中的所有 `CapacityFail` 均已绑定到具体容量文档；未发现无绑定自由容量事件。下一步应按第 3 节强度排序，优先攻 `DGap 投影正交化` 的逐行证明强度。

**证明。** 逐项核查第 1 节表格。每个容量失败语境都有唯一或主导绑定文档，且对应文档规定了失败出口。证毕。
