# DSO-E 无条件化匹配审查

本文专攻 `docs/rh-pc4-orthogonality-input-audit.md` 指出的第 4 项正交输入主硬点：`DSO-E`。目标是把 `docs/rh-pc4-dso-euler-decorrelation.md` 的 DSO-E1--E4 与 `NRC/EXT-KL`、`FCT`、`LSMP-Freq` 精确匹配，确认 CE-1 中“独立新频率近正交”不再作为悬空黑箱。

## 1. DSO-E1：单层字符正交

入口：`docs/rh-pc4-dso-euler-decorrelation.md` 第 2 节。

状态：无条件。

理由：新增局部空间 `G_p=(Z/pZ)^*` 是有限阿贝尔群。不同乘法字符正交；纯加法字符在完整剩余类上也按标准有限 Fourier 正交。该部分只依赖有限群 Parseval。

## 2. DSO-E2：倒数/混合相位非共振界

入口：`docs/rh-pc4-dso-euler-decorrelation.md` 第 3 节。

状态：可由 NRC/EXT-KL 精确引用。

匹配：

1. 纯倒数差 `e_p((h-h')x^{-1})` 经变量替换 `y=x^{-1}` 化为非主加法字符和，归一化大小 `<=p^{-1}`；
2. 混合相位 `e_p(ax+bx^{-1})` 是 Kloosterman 型完整和；若 `(a,b)` 非退化，由 Weil/Kloosterman 界给 `O(p^{1/2})`，归一化为 `O(p^{-1/2})`；
3. 非退化失败正是频率落入祖先 span 或相位常数化，进入 FCT。

引用位置：`docs/nrc-theoremization.md` 与 `docs/bibliography.md` 的 `EXT-KL` / `[Weil-Kloosterman]`。

## 3. DSO-E3：局部多频平方控制

入口：`docs/rh-pc4-dso-euler-decorrelation.md` 第 4 节。

状态：由 E2 + Schur/Gershgorin 型矩阵界给出。

匹配：若局部频率数 `m_p<=c p^{1/4}`，非对角相关总量最多为 `O(m_p p^{-1/2})`，故 Gram 矩阵是恒等矩阵的小扰动。于是

`||b_p||_2^2 <= 2Σ|a_{p,ν}|^2`。

若非对角项不是非共振，则转 FCT；因此 E3 不新增黑箱。

## 4. DSO-E4：大局部复杂度二次剥离

入口：`docs/rh-pc4-dso-euler-decorrelation.md` 第 5 节。

状态：由 `docs/rh-pc4-lsmp-frequency-corollary.md` 补齐。

三分匹配：

1. 频率集中在短深度 span：触发 FCT；
2. 存在大小 `<=c p^{1/4}` 的重可控子集：返回 DSO-E3；
3. 无重 span、无重可控子集：由 `LSMP-Freq` 的 dyadic 层蛋糕与 coarea 进入 LSMP 小质量逃逸。

因此大复杂度不是独立终端；它只触发 FCT、LSMP 或返回 E3。

## 5. CE-1 闭合匹配

`docs/rh-pc4-complexity-escape-interface.md` 中 CE-1 需要的输入是：无界频率复杂度若不落入短深度 span，则新增独立频率不能长期同向累积。

由 E1--E4：

- 可控局部复杂度由 E3 控制；
- 大局部复杂度由 E4 剥离；
- 非共振估计由 E2/NRC 提供；
- 共振失败转 FCT；
- 小质量分散转 LSMP。

故 CE-1 的“独立新频率近正交”已被替换为 `DSO-E + NRC + LSMP-Freq + FCT` 的可审查组合。

## 6. DSO-E 匹配定理

**Theorem DSO-E-Match（DSO-E 与 NRC/LSMP/FCT 匹配闭合）。** 假设标准 Weil/Kloosterman 完成和界、NRC 非共振接口、FCT 频率碰撞终端与 LSMP-Freq 小质量逃逸均可用。则 DSO-E 中任何新增 Euler 局部因子非主偏差满足以下二分：

1. 局部平方能量由 `Σ|a_{p,ν}|^2` 控制，并可输入 DSO-C/PI 正交账本；
2. 或触发 FCT、LSMP、NRC 异常、PI-Seed/CE 失败分支之一。

因此 DSO-E 不再提供独立 RH 反例逃逸通道。

**证明。** 对每个新增素数层应用 E1--E4。E1 处理正交字符；E2 处理纯倒数与混合非共振；E3 控制可控多频层；E4 处理大复杂度层。所有失败分支分别由 FCT、LSMP-Freq、NRC 或 PI-Seed 接收。对层求和即得。证毕。

## 7. 循环依赖检查

DSO-E 的正确用法是：失败触发 `PI-Seed` 或 D 组终端，而不是引用 `PC4-PI-Closure` 后再证明 `PC4-PI-Closure`。因此在最终总攻中应写：

`DSO-E failure => FCT / LSMP / NRC / PI-Seed`

再由 PC4 总框架处理这些终端。这样避免 DSO-E 与 PC4-PI 闭合之间的循环。
