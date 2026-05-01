# PC4 正交输入最终合并审查

DSO/容量定理的最终审稿矩阵见 `docs/rh-dso-capacity-final-audit.md`。


本文合并 `DSO-C`、`TC`、`CE` 与 `DSO-E` 的审查结果，确认 RH 总攻框架第 4 项“正交输入”已经从单一黑箱降解为标准 Hilbert 正交、模板组合定理、复杂度逃逸三分和 DSO-E/NRC/LSMP/FCT 匹配。本文不证明 PC4 终端 closure；它只说明“分散正交能量”不再是独立逃逸通道。

## 1. 已闭合模块

1. **DSO-C**：`docs/rh-pc4-dso-crt-martingale.md` 给出逆极限 CRT martingale square-function，属于无条件 Hilbert 空间定理。
2. **TC**：`docs/rh-pc4-dso-template-consistency.md` 将固定复杂度窗口接入 DSO-C；失败时不留在 TC，而进入 CE。
3. **CE**：`docs/rh-pc4-complexity-escape-interface.md` 将复杂度、尾项、旧坐标重写、边界体积逃逸转入 FCT、LSMP、LV 或 PI-Seed；CE-1 的正交输入由 DSO-E 接收。
4. **DSO-E**：`docs/rh-pc4-dso-e-unconditionalization-audit.md` 已把 E1--E4 与 NRC/EXT-KL、FCT、LSMP-Freq、PI-Seed 匹配。

## 2. 合并后的分散能量四分

任一 PC4 中出现的分散正交能量，必处于以下一类：

1. 固定模板、平方可和误差：由 DSO-C+TC 控制；
2. 频率复杂度逃逸：由 DSO-E 转入正交控制、FCT、LSMP 或 PI-Seed；
3. 尾项/边界/旧坐标逃逸：由 CE 转入 LSMP、LV、FCT 或 PI-Seed；
4. 非共振解析失败：由 NRC/EXT 标记为 NRC 异常终端。

没有第五类“正交能量自行吸收 RH 反例波动”。

## 3. 无循环依赖口径

正交输入的最终使用顺序必须写为：

`DSO failure => PI-Seed / FCT / LSMP / LV / NRC`

而不是

`DSO failure => PC4-PI-Closure`。

这样 PC4-PI-Closure 可以在后续统一处理 PI-Seed 与其他终端，避免正交输入反向依赖 PC4 终端 closure。

## 4. 正交输入最终命题

**Theorem Orthogonality-Input-Final（PC4 正交输入最终归约）。** 在标准 Hilbert 正交、固定模板一致性、NRC/EXT-KL、FCT、LSMP/LV 与 PI-Seed 接口可用的前提下，PC4 中任意分散正交能量分支不能作为独立 RH 反例逃逸通道；它必被吸收为 DSO-C 容量上界，或转入 PI-Seed、FCT、LSMP、LV、NRC 之一。

**证明。** 固定模板由 DSO-C+TC 控制。若固定模板条件失败，CE 四分给 FCT/LSMP/LV/PI-Seed，唯一的频率复杂度逃逸由 DSO-E 处理。DSO-E 的失败分支由 DSO-E-Match 转入 FCT/LSMP/NRC/PI-Seed；成功分支回到 DSO-C 平方函数容量上界。证毕。

## 5. 对总攻的影响

第 4 项“正交输入”现在可以标记为内部合并完成；最终 DSO/容量出口矩阵见 `docs/rh-dso-capacity-final-audit.md`。
