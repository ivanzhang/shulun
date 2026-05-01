# C8 CapacityFail 升级审查与闭合判据

本文继续补 `docs/rh-merge-unconditional-checklist.md` 的 C8。已有 `docs/rh-capacityfail-binding-table.md` 证明：所有 `CapacityFail` 均已绑定到具体容量文档。本文进一步区分“绑定”与“无条件闭合”：绑定只排除了自由黑箱；无条件闭合还要求对应容量定理已经逐行证明，且失败出口不能回到自身或制造新接口。

## 1. C8 的精确定义

`CapacityFail` 在最终主稿中允许出现的唯一含义是：某个容量定理的适用条件被违反，或某个容量上界若不成立则推出已命名结构事件。它不能作为终端结论，也不能作为“反例还能逃逸”的占位符。

因此 C8 闭合需要三步：

1. **绑定**：每个 `CapacityFail` 指向唯一容量定理或有限组容量定理；
2. **判别**：容量定理成功时给出 `log^C X` 或 `X^{o(1)}` 上界；
3. **出口**：容量定理失败时进入已编号事件 `A/PI/FCT/SC/LV/LSMP/CE/DSO/NRC`，且事件图无回流。

## 2. 升级核验表

| 容量接口 | 绑定状态 | 成功时闭合 | 失败出口闭合 | C8 状态 |
|---|---|---|---|---|
| PC2 基线容量 | 已绑定 | 初等 CRT/Mertens，理论上可内联 | 失败即 C2 失败 | 可闭合，待内联 |
| DSO martingale | 已绑定 | Hilbert/Parseval 平方函数可内联 | TC/CE/LSMP/FCT/LV | 可闭合，待编号 |
| NRC 非共振容量 | 已绑定到 `EXT-KL` | 依赖 Weil/Kloosterman 正式引用 | 失败转 FCT | 依赖 C10 |
| Fourier/Vaaler 尾项 | 已绑定到 `EXT-Vaaler` | 依赖 Vaaler 截断 | 失败转 CE/LSMP/LV | 依赖 C10/C9 |
| PI lacunary/dense | 已绑定 | lacunary 较稳；dense 经 DSO | 失败转 DSO/SC/LV/CE | 待 C6 定理化 |
| SC 局部乘积容量 | 已绑定 | 需主稿逐层 dyadic 证明 | 失败转 PI/A/FCT/LV/LSMP | 待 C6 定理化 |
| OV2/MLC Uniform | 已绑定 | 需主层容量与零频容量常数化 | 失败转 PPI/FCT/SC/LV/DSO/PI | 待 C4 定理化 |
| DGap 盒重叠与投影 | 已绑定 | frame/投影/低维抽取需内联 | 失败转 PI/FCT/SC/LV/CE | 待 C5 定理化 |
| AAI 允许锚容量 | 已绑定 | 整除上包络可初等化 | 失败转 MLC 或代数矛盾 | 可闭合，待内联 |
| FCT/LSMP 容量 | 已绑定 | Noether 下降与 coarea 需编号 | 失败转 PI/SC/LV/CE | 待 C6/C7 定理化 |

## 3. 最小剩余容量割集

C8 不能单独从清单中完全勾销，因为它依赖下列接口的逐行证明：

`C4(OV2/MLC) + C5(DGap) + C6(A/PI/FCT/SC) + C9(Tail) + C10(EXT)`。

但 C8 的“自由黑箱”问题已解决：当前没有无绑定的 `CapacityFail`。剩余问题是绑定目标本身是否已达到顶刊逐行证明标准。

## 4. 主稿替换规则

最终主稿中每次出现 `CapacityFail`，必须替换为以下形式之一：

- “由 Lemma Cap-PC2 得矛盾”；
- “由 Lemma Cap-DSO 得上界，故不能承载 `Δ`”；
- “若 Cap-SC 适用条件失败，则由 Proposition SC-Exit 进入 `PI/A/FCT/LV/LSMP`”；
- “若 EXT-KL 所需非退化条件失败，则相位退化给 `FCT_seed`”。

禁止保留“进入 CapacityFail”作为最终出口。

## 5. C8 当前结论

**Proposition C8-CapacityFail-Bound-But-Not-Fully-Discharged.** 当前文档包已经排除自由 `CapacityFail`：每个容量失败均绑定到具体容量接口和命名失败出口。因此 C8 的自由黑箱部分闭合。可是 C8 仍不能完全勾销；其最终闭合等价于 C4、C5、C6、C9、C10 中相关容量定理全部逐行内联或正式引用。

**证明。** 第 2 节逐项核查当前容量表，所有语境均有绑定对象和失败出口，故不存在无绑定自由事件。第 3 节列出仍依赖的容量定理化接口；这些接口尚未全部内联到合并稿，所以 C8 只能标记为“已绑定，待随 C4/C5/C6/C9/C10 放电”。证毕。

## 6. 对无条件化清单的影响

C8 应从“未知黑箱”降级为“依赖型闭合义务”。下一步最优攻坚不再是继续列 CapacityFail 表，而是选择 C5 或 C6，把其中一个容量定理写成可直接并入合并稿的完整编号证明。
