# DSO-E 接口匹配审查：NRC/EXT 与 LSMP 对齐

本文对 `docs/rh-pc4-dso-euler-decorrelation.md` 做投稿级接口核查。目标是把 DSO-E2 的解析输入精确落到 NRC/EXT-KL，把 DSO-E4 的组合剥离精确落到 LSMP/FCT，而不是留下“去相关黑箱”。

## 1. DSO-E2 与 EXT-KL/NRC 的匹配

### 1.1 纯倒数相位

DSO-E2 的纯倒数交叉项为

`p^{-1}Σ_{x∈F_p^*} e_p((h-h')x^{-1})`。

令 `y=x^{-1}`，它等于

`p^{-1}Σ_{y∈F_p^*} e_p((h-h')y)`。

若 `h≠h' mod p`，则完整非主加法字符和为 `-1`，归一化后大小 `p^{-1}`。此处不需要外部 Weil 输入。

### 1.2 混合相位

DSO-E2 的混合交叉项为

`p^{-1}Σ_{x∈F_p^*} e_p(ax+b/x)`。

若 `(a,b)≠(0,0)`，这正是 `docs/external-theorem-package.md` 中 `EXT-KL` 的完整 Kloosterman 特例，给

`|Σ_{x∈F_p^*} e_p(ax+b/x)| <= 2p^{1/2}`，

即归一化界 `2p^{-1/2}`。

### 1.3 非共振失败与 FCT

若 DSO-E 中的混合相位退化，不是指 `(a,b)=(0,0)` 这一个代数事件本身，而是指当前频率被祖先频率组合抵消，使有效相位落入低维短深度 span。该条件与 `docs/nrc-theoremization.md` 第 2 节的

`ξ notin Span_H(Ξ(g))`

完全对应。失败时不调用 Weil，而记录为 `docs/fct-tree-wfe-theoremization.md` 的 frequency-collision terminal。

**结论 E2-Match。** DSO-E2 的解析部分已经由初等字符正交与 `EXT-KL` 覆盖；唯一非解析分支是非共振失败，它按 NRC 口径转入 FCT。

## 2. DSO-E3 的常数账本

DSO-E3 展开 `L^2` 后有

`||b_p||_2^2 <= Σ|a_ν|^2 + 2p^{-1/2}Σ_{ν<ν'} |a_νa_{ν'}|`。

由 `2|ab|<=|a|^2+|b|^2` 得

`2p^{-1/2}Σ_{ν<ν'} |a_νa_{ν'}| <= 2m_p p^{-1/2}Σ|a_ν|^2`。

因此若 `m_p<=1/4 p^{1/2}`，已经有常数 `<=3/2`；文档中保守采用 `m_p<=c p^{1/4}` 时 `<=2`，更强且留出截断与有限并差余量。

纯倒数差情形可用 `p^{-1}`，条件可放宽到 `m_p<=c p^{1/2}`；但主链保守统一使用混合相位阈值，避免分情形账本膨胀。

## 3. DSO-E4 与 LSMP/FCT 的匹配

DSO-E4 处理 `m_p` 过大。它不是解析定理，而是组合剥离接口。需要核验三步。

### 3.1 祖先 span 重质量到 FCT

把 `Ω_p` 按 `Span_H(Ξ)` 的短深度祖先 span 分桶。若某桶承载固定比例 `l^2` 质量，则这些频率由有限深度祖先关系生成，正是 `docs/fct-tree-wfe-theoremization.md` 的 FCT 输入。

### 3.2 无重桶到小质量分散

若没有 span 桶承载固定比例质量，而所有可控大小子集也不承载固定比例质量，则 `l^2` 质量被迫分散到许多小原子。按系数 dyadic 大小层蛋糕分解，得到大量小质量薄层。这与 `docs/omr-cgtp-lsmp-theoremization.md` 中：

- `LSMP-1` 离散 coarea；
- `LSMP-2` DPI；
- `Theorem LSMP` 小质量原子吸收，

的输入形式一致。

### 3.3 可控子集抽取返回 DSO-E3

若既无重 span，也非完全小质量分散，则存在某个可控大小子集 `Ω'_p` 承载固定比例 `l^2` 质量。选择阈值 `|Ω'_p|<=c p^{1/4}`，对该子集调用 DSO-E3。剩余质量重复剥离。有限次结束则全由 DSO-E3 控制；无限次只可能意味着小质量分散，回到 LSMP。

**结论 E4-Match。** DSO-E4 的严格性依赖 LSMP 的离散 coarea/有限重叠薄层选择；它不再是新黑箱，而是 LSMP 的一次局部频率版本调用。后续若要进一步减少黑箱，应在 LSMP 文档中增加“频率原子版 coarea corollary”。

## 4. 当前闭合状态

DSO-E 现在可分成三类状态：

1. **已证明**：纯倒数相位正交、加法/乘法字符正交；
2. **外部定理支撑**：混合 Kloosterman 完整和，由 `EXT-KL` 与 NRC 完成法支撑；
3. **组合接口支撑**：大复杂度剥离，由 FCT 与 LSMP 支撑。

因此 DSO-E 对 PC4-PI 的作用可以诚实表述为：在接受 `EXT-KL`、NRC 非共振口径、FCT/LSMP 组合接口的条件下，新增 Euler 局部因子的非主偏差若不进入 FCT/LSMP，则平方可控。

## 5. 下一步最小补强

为继续向 RH 总攻推进，下一步最优不是再重写 DSO-E，而是补一个窄 corollary：

**LSMP-Freq Corollary。** 已在 `docs/rh-pc4-lsmp-frequency-corollary.md` 中写出：对频率原子集合 `Ω_p`，若无短深度 span 重桶且无可控大小重子集，则 dyadic 层蛋糕产生 LSMP 小质量原子输入。

因此 DSO-E4 最后一处“组合剥离接口”已经降为可逐行引用的 LSMP 推论。
