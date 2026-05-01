# PC4-PI 终端最终归约：seed--dense--lacunary 三分闭合

本文把 `docs/rh-pc4-pi-terminal-audit.md` 中的审查结论定理化。它不是 RH 的独立证明，而是 PC4 过密分支中 `PI` 事件的局部终端归约：一旦接受 PI-Seed、dense 正交闭合和 lacunary 容量账本，`PI` 不能再作为事件图中的最终逃逸通道。

## 1. 事件与非终端假设

固定模板记为 `𝓦_*`，尺度序列为 `X_j`，PI 窗口为 `A_j`，相对偏差为 `δ_j`，能量为

`e_j=δ_j^2 μ_j^0(A_j)`。

在 PC4 事件图中，本文始终处于以下非终端假设下：

1. 不发生 CE/复杂度逃逸；
2. 不发生 LSMP/低支撑质量逃逸；
3. 不发生 LV/低体积逃逸；
4. 不发生 SC/短簇逃逸；
5. 不发生 FCT/频率闭包链逃逸；
6. 不发生 NRC/非共振完成和逃逸。

这些假设的作用只是排除已经由其他终端分支处理的异常，使 PI 分支只剩固定模板、固定容量账本与固定尺度分解。

## 2. 尺度三分

给定任意无限 PI 子列，按相邻尺度的 Mellin 距离分解为两类：

- **lacunary 包**：存在固定 `B>1`，满足 `X_{j_{m+1}}>=X_{j_m}^B` 的强分离子列；
- **dense 包**：不能继续抽取强分离承载能量的剩余尺度包；
- **边界坏包**：由 dyadic 边界、模板支撑改变或归一化失效导致的有限复杂度异常。

边界坏包若无限承载正能量，则模板复杂度或窗口支撑不再固定，转入 CE/LSMP/LV/SC；若只有限承载，则可并入误差。因此在非终端假设下，PI 能量只能由 lacunary 包或 dense 包承载。

## 3. Lacunary 归约

由 `docs/rh-pc4-pi-lacunary-capacity.md`，对任意有限 lacunary 截断 `𝓛_N` 有

`Σ_{j∈𝓛_N} e_j <= C(𝓦_*) Cap(𝓛_N)`。

该界的含义是：lacunary 包只能按自身 disjoint Mellin 容量支付能量，不能产生跨尺度同相位压缩。若 PI-Seed 需要的是固定总容量内的无限能量，则 lacunary 包立即给矛盾；若容量随尺度线性增长，则它不是逃逸，而只是容量账本的正常支出，不能解释 RH 反例所需的同相位压缩。

因此，lacunary 包在事件图中只有两种出口：

1. 满足容量账本，剩余相干能量必须进入 dense 包；
2. 违反容量账本，触发 SC/LV/CE 或单尺度 PI 极端终端。

## 4. Dense 归约

由 `docs/rh-pc4-pi-dense-closure-theorem.md` 与 `docs/rh-pc4-orthogonality-final-closure-audit.md`，dense 包若承载固定模板的发散 PI 能量，则必须出现以下之一：

- Mellin/CRT martingale 正交容量上界被违反；
- Euler 局部因子去相关失败；
- 新增 CRT 坐标中相位长期锁定；
- 投影能量被压缩到低维频率闭包。

这些出口分别转入 DSO-C/DSO-E、NRC、LSMP/LV 或 FCT。故在非终端假设下，dense 包也不能作为最终逃逸通道。

## 5. PI 终端最终归约定理

**Theorem PC4-PI-Terminal-Final-Reduction。** 假设：

1. `docs/rh-pc4-pi-seed.md` 的 PI-Seed 能量下界成立；
2. `docs/rh-pc4-pi-dense-closure-theorem.md` 的 dense 正交闭合已由正交输入最终审查支撑；
3. `docs/rh-pc4-pi-lacunary-capacity.md` 的 lacunary 容量上界成立；
4. CE/LSMP/LV/SC/FCT/NRC 均作为 PC4 事件图终端处理。

则 `PI` 不能是 PC4 事件图中的最终逃逸通道。

**证明。** 反设 `PI` 是最终逃逸。由 PI-Seed，存在固定模板 `𝓦_*` 与无限尺度子列，使有限截断能量和无界增长：

`Σ_{j<=N} e_j -> ∞`。

按第 2 节把该子列分成 lacunary、dense 与边界坏包。边界坏包若承载无界能量，则由定义触发 CE/LSMP/LV/SC，违背最终逃逸假设；否则删去后能量仍无界。

若 lacunary 部分在固定总容量中承载无界能量，则违反 PI-Lacunary-Capacity；若它只按自身 disjoint 容量增长，则它不产生同相位压缩，删去其容量账本贡献后，RH 反例所需的剩余相干能量必须由 dense 部分承载。若 dense 部分承载无界相干能量，则由 dense 正交闭合转入 DSO/NRC/LSMP/LV/FCT 终端，仍违背最终逃逸假设。

于是所有可能承载 PI-Seed 发散能量的分支均被容量账本或终端事件吸收，与 `PI` 为最终逃逸矛盾。证毕。

## 6. 审稿口径

本定理闭合的是 PC4-PI 的事件图接口，不声称单独证明 RH。其审稿义务是逐项核验三类输入：PI-Seed、dense 正交闭合、lacunary 容量上界，以及 CE/LSMP/LV/SC/FCT/NRC 终端分支的无循环处理。
