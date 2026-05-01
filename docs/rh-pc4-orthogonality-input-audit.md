# PC4 正交输入审查：DSO-C/DSO-E/TC/CE

本文进入 RH 总攻框架第 4 项“正交输入”。目标是审查 `DSO-C`、模板一致性 `TC`、复杂度逃逸 `CE` 与 Euler 局部因子去相关 `DSO-E` 的闭合状态，明确哪些部分已是 Hilbert/组合定理，哪些仍是下一步硬点。

## 1. 正交输入在总攻中的位置

PC4-PI、DGap 投影正交化、MLC 不可检测吸收都需要同一类输入：若异常质量分散在许多新增 CRT 坐标或频率上，则平方能量不能无限累加；否则必须形成低维频率闭包、短簇、LSMP/LV 或高投影增量。

这一输入由四个模块组成：

1. `DSO-C`：逆极限 CRT martingale square-function；
2. `TC`：固定模板接入 martingale 的一致性；
3. `CE`：模板复杂度或尾项逃逸时转入终端；
4. `DSO-E`：新增 Euler 局部因子/独立新频率的去相关。

## 2. DSO-C 状态

入口：`docs/rh-pc4-dso-crt-martingale.md`。

状态：无条件 Hilbert 空间核心已闭合。

已证明内容：

- 构造 `G_∞=∏_p (Z/pZ)^*`；
- 条件期望 martingale 差 `D_k` 两两正交；
- `Σ_k||D_kF||_2^2<=||F||_2^2`；
- 字符版本等价于新增坐标 Fourier Parseval。

剩余不在 DSO-C 本身，而在“具体窗口是否来自同一固定模板”。

## 3. TC 状态

入口：`docs/rh-pc4-dso-template-consistency.md`。

状态：固定复杂度、自然细化、平方可和误差方案已条件化闭合，接近无条件组合定理。

已证明内容：

- cylinder 模板一致性；
- 有限布尔闭包；
- 倒数环带的固定 Vaaler 截断；
- 截断误差平方可和；
- dyadic 标签不重写旧坐标。

剩余风险：若实际应用需要随尺度增长的截断高度、无界频率集合或旧坐标重写，则 TC 不适用，必须进入 CE。

## 4. CE 状态

入口：`docs/rh-pc4-complexity-escape-interface.md`。

状态：除 CE-1 依赖 DSO-E 外，其余逃逸已明确转入终端。

四类逃逸：

1. 频率复杂度逃逸：依赖 DSO-E，转 FCT 或 PI；
2. 尾项能量逃逸：转 LSMP 或高投影增量；
3. 旧坐标重写逃逸：转 LV 或 FCT；
4. 边界体积逃逸：转 LV。

因此 CE 的真正硬点是 CE-1 中“独立新频率近正交”的 DSO-E 输入。

## 5. DSO-E 状态

入口：`docs/rh-pc4-dso-euler-decorrelation.md` 与 `docs/rh-pc4-dso-euler-match-audit.md`。

作用：当频率复杂度增长但没有落入短深度 span 时，新增 Euler 局部因子应表现为近正交；否则频率必须闭合为 FCT 或集中为 LSMP。

当前审查结论：DSO-E 是第 4 项正交输入的主硬点。它需要把三件事严密拼接：

1. 新增局部字符与旧 CRT 坐标正交；
2. 倒数/混合相位非共振由 NRC/Weil/Kloosterman 控制；
3. 高复杂度或低支撑失败转入 LSMP/FCT，而不是作为新终端。

## 6. 正交输入合并命题

**Proposition Orthogonality-Input-Reduction（正交输入归约）。** 若 DSO-C、TC、CE 与 DSO-E 均成立，则 PC4 中所有“分散正交能量”情形只能进入以下分支之一：

1. 固定模板平方函数受 DSO-C 控制；
2. 复杂度逃逸转入 FCT、LSMP、LV 或 PI；
3. 新增独立频率由 DSO-E 去相关控制；
4. DSO-E 失败时转入 NRC 异常、FCT 或 LSMP。

因此正交输入不再产生新的 RH 反例吸收通道。

**证明。** 固定模板由 DSO-C+TC 控制。若模板条件失败，CE 四分处理。CE 中唯一非终端风险是频率复杂度逃逸；由 DSO-E，要么新增频率近正交并受平方函数控制，要么共振为 FCT，要么低支撑为 LSMP/LV，要么非共振估计失败为 NRC/EXT 异常。证毕。

## 7. 下一步硬点

下一步应专攻 `DSO-E` 的无条件化审查，优先顺序：

1. 对 `docs/rh-pc4-dso-euler-decorrelation.md` 逐条抽取 DSO-E1/E2/E3/E4；
2. 将 DSO-E2 的非共振倒数/混合相位估计与 `docs/nrc-theoremization.md`、`docs/bibliography.md` 的 EXT-KL/Weil 引用精确匹配；
3. 将 DSO-E4 的低支撑/大复杂度失败与 `docs/rh-pc4-lsmp-frequency-corollary.md`、LSMP/LV 接口匹配；
4. 检查 DSO-E 是否循环依赖 PC4-PI closure；若有，改写为“DSO-E 失败触发 PI-Seed”，避免闭合循环。


## 8. DSO-E 匹配审查入口

DSO-E1--E4 与 NRC/EXT-KL、FCT、LSMP-Freq、PI-Seed 的逐项匹配见 `docs/rh-pc4-dso-e-unconditionalization-audit.md`。


## 9. 最终合并审查入口

DSO-C、TC、CE 与 DSO-E 的最终合并审查见 `docs/rh-pc4-orthogonality-final-closure-audit.md`。该文档确认分散正交能量不再作为独立逃逸通道，而是转入 DSO 容量上界或 PI-Seed/FCT/LSMP/LV/NRC。
