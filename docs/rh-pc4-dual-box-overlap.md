# PC4-Dual：DGap 盒分解有限重叠定理

本文补强 `docs/rh-pc4-dual-dgap-decomposition.md` 的第一个基础接口：DGap 场的盒分解为何可取有限重叠，且重叠损失只为 `log^C X`。该结论使后续 Cauchy 能量下界、短簇识别与投影正交化有共同的离散支架。

## 1. 盒的三重标签

固定尺度 `X`、筛层 `z=(log X)^A` 与平滑支撑 `[X/2,2X]`。DGap 盒 `B` 由三类标签组成：

1. **物理窗标签** `I`：长度取 dyadic 网格 `L=2^ell`，端点在 `L` 的整数倍网格上；
2. **锚层标签** `(Q,R)`：`Q` 与 `R` 取 dyadic 值，并满足 AAI 正规形的主层关系 `Q^2R≈X` 或跨层同型关系；
3. **CRT/Bohr 相位标签** `Ω`：由固定数量的新增 CRT 坐标、倒数环带、短弧或有限 Bohr 切片构成。

盒定义为

`B=I ∩ Layer(Q,R) ∩ Ω`。

这里 `Layer(Q,R)` 只记录 dyadic 类型，不改变 CRT 坐标；`Ω` 属于固定复杂度 cylinder/Bohr 模板族。

## 2. 物理窗有限重叠

采用标准 dyadic Whitney 网格：每个点 `n∈[X/2,2X]` 在每个长度层 `L` 至多属于 `O(1)` 个物理窗。长度层数为 `O(log X)`，故

`Σ_I 1_I(n) <= C log X`。

若只使用短窗候选层 `L<=L_max`，重叠更小；若使用平滑 partition of unity，则点态重叠换成权重重叠，同样为 `O(log X)`。

## 3. dyadic 锚层有限重叠

对固定 `n≈X`，满足 `q|n` 的 dyadic 锚层 `Q<q<=2Q` 至多有 `O(log X)` 个可能 `Q`。若要求双锚正规形 `n=q_1q_2r` 且 `q_i≈Q`，则 `R≈X/Q^2` 被 `Q` 决定到 `O(1)` 个 dyadic 层。因此

`Σ_{Q,R} 1_{Layer(Q,R)}(n) <= C log X`。

跨层正规形 `n=q_0q_1r` 只增加一个 dyadic 标签，重叠仍为 `O(log^2 X)`，可吸收到 `log^C X`。

## 4. CRT/Bohr 相位有限复杂度

相位盒 `Ω` 来自固定复杂度模板族：有限个倒数环带、短弧、Bohr 切片及其有限并交差。按 `docs/rh-pc4-dso-template-consistency.md`，固定模板在 CRT 逆极限中是 cylinder 型或同型新增坐标 cylinder 型。

对每个固定模板层，选取有限重叠的短弧/Bohr cover，使

`Σ_Ω 1_Ω(n) <= C_T`

其中 `C_T` 只依赖模板复杂度。若模板复杂度随尺度增长，则不纳入本文有限重叠盒分解，而转入 `docs/rh-pc4-complexity-escape-interface.md`。

## 5. 总有限重叠定理

**Theorem DGap-Box-Overlap（DGap 盒分解有限重叠，条件化）。** 对固定复杂度 DGap 盒族 `𝓑`，若物理窗采用 dyadic 有限重叠网格，锚层采用 dyadic `Q,R` 标签，相位原子属于固定复杂度 CRT/Bohr cylinder 模板，则对每个 `n≈X` 有

`Σ_{B∈𝓑} 1_B(n) <= log^C X`。

若该界失败，则失败原因只能是：物理窗层数非 dyadic 可控、锚层复杂度无界、相位模板复杂度无界，或边界平滑尾项不可平方求和；这些均进入 LV/LSMP、FCT 或 Complexity-Escape。

**证明。** 盒指标是三类标签指标的乘积。第 2 节给物理窗重叠 `O(log X)`；第 3 节给 dyadic 锚层重叠 `O(log^2 X)`；第 4 节给相位原子重叠 `O(1)`，常数依赖固定模板复杂度。相乘得 `log^C X`。若任一因子不满足有限重叠，按对应定义正是低体积/复杂度/尾项逃逸，转入既有接口。证毕。

## 6. 对 DGap-Decomposition 的输入

有了 DGap-Box-Overlap，对 `h=g_z^0-g_z` 的正质量盒分解满足：

`Σ_B μ^0(B) <= log^C X · μ^0([X/2,2X])`。

因此 Cauchy 下界

`Σ_B H(B)_+^2/μ^0(B) >= (Σ_B H(B)_+)^2 / Σ_B μ^0(B)`

只损失 `log^C X`，可写入 `X^{o(1)}`。这正是 `DGap-Decomposition` 从分散正质量推出投影能量压力的基础。
