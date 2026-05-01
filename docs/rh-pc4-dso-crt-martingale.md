# DSO-C：逆极限 CRT 概率空间与 martingale square-function

本文专攻 `docs/rh-pc4-dense-scale-orthogonality.md` 中最可操作的 DSO-C 接口。目标是构造 inverse-limit CRT 概率空间，并证明固定函数的 martingale square-function 上界。随后说明固定投影模板如何接入该空间，以及剩余的模板拉回一致性义务。

## 1. 逆极限 CRT 空间

令 `p_1<p_2<...` 为素数序列，取

`G_k=∏_{i<=k} (Z/p_iZ)^*`。

由 CRT，`G_k ≅ (Z/M_kZ)^*`, `M_k=∏_{i<=k}p_i`。投影映射

`π_{k+1,k}:G_{k+1}->G_k`

忘掉最后一个素数坐标。定义逆极限

`G_∞=lim← G_k = ∏_p (Z/pZ)^*`。

赋予乘积概率测度

`μ=⊗_p μ_p`，其中 `μ_p` 是 `(Z/pZ)^*` 上的均匀测度。

令 `𝔽_k` 为前 `k` 个素数坐标生成的 σ-代数。

## 2. CRT martingale

对 `f∈L^2(G_∞,μ)`，定义

`E_k f = E[f | 𝔽_k]`,

`D_k f = E_k f - E_{k-1} f`。

**Lemma DSO-C1（CRT martingale orthogonality）。** 对任意 `f∈L^2(G_∞)`，有

`Σ_{k>=1} ||D_k f||_2^2 <= ||f-E_0f||_2^2 <= ||f||_2^2`。

**证明。** `E_k f` 是 Hilbert 空间 `L^2` 中到闭子空间 `L^2(𝔽_k)` 的正交投影。差分 `D_k f` 两两正交，因为 martingale differences 对嵌套 σ-代数正交。故

`||E_N f-E_0f||_2^2=Σ_{k<=N}||D_k f||_2^2`。

令 `N→∞` 并用 `L^2` martingale 收敛定理得结论。证毕。

这是 DSO-C 的严格核心：新增 CRT 素数层的独立坐标给出 Parseval/Doob 平方函数上界。

## 3. 字符正交版本

`G_k` 的字符群为

`Ĝ_k=∏_{i<=k} \widehat{(Z/p_iZ)^*}`。

`D_k f` 正好由那些首次依赖第 `k` 个素数坐标的 Fourier 字符组成。

**Lemma DSO-C2（新增字符层 Parseval）。** 若

`f=Σ_χ \hat f(χ)χ`

为 `G_∞` 上的 Fourier 展开，则

`||D_k f||_2^2 = Σ_{χ: max supp(χ)=k} |\hat f(χ)|^2`。

因此

`Σ_k||D_k f||_2^2=Σ_{χ≠1}|\hat f(χ)|^2`。

**证明。** 条件期望 `E_k` 保留只依赖前 `k` 个坐标的字符，杀掉依赖后续坐标的字符。差分 `E_k-E_{k-1}` 正好保留最大支持坐标为 `k` 的字符。Parseval 给平方和。证毕。

## 4. 固定投影模板的拉回

固定投影模板 `𝓦_*` 在有限模 `M_k` 上给出窗口函数

`f_k:G_k->[0,1]`。

把它拉回到 `G_∞`：

`F_k=f_k∘π_{∞,k}`。

重要严审点：并非任意随尺度变化的窗口 `f_k` 都来自同一个极限函数 `F`。若不能证明这一点，martingale 正交不能直接使用。只有当 `f_k` 是同一模板的自然细化时，才可期待存在 `F∈L^2(G_∞)`，使

`F_k=E_kF+err_k`, `Σ_k||err_k||_2^2<∞`。

这就是模板一致性条件。

**Definition DSO-C-TC（模板一致性）。** 称固定投影模板 `𝓦_*` 满足 CRT martingale 一致性，若存在 `F∈L^2(G_∞)` 与误差 `err_k`，使上述关系成立，且误差平方可和。

## 5. DSO-C 主命题

**Proposition DSO-C（模板一致性推出密集尺度正交）。** 若固定投影模板 `𝓦_*` 满足 DSO-C-TC，则在任意密集尺度包中，新增 CRT 层造成的投影偏差满足

`Σ_k ||D_k F||_2^2 <= ||F||_2^2`，

并且对应高投影增量能量满足

`Σ_{X_j in pack} δ_j^2 μ_j^0(A_j) <= C(𝓦_*) Cap(pack)+O(Σ||err_k||_2^2)`。

**证明。** 模板窗口拉回后，每个密集尺度中的新增投影偏差由某些 martingale difference `D_kF` 控制。由 Lemma DSO-C1，所有新增层平方贡献总和受 `||F||_2^2` 控制。固定模板复杂度只造成有限重叠常数 `C(𝓦_*)`；误差项按平方可和吸收。证毕。

## 6. 剩余义务：模板一致性

DSO-C 的 Hilbert 空间核心已经严格闭合；剩余不是 martingale 定理，而是几何接入：证明 PPI/OMR 的固定投影模板确实满足 DSO-C-TC。若模板在尺度变化时重写旧坐标或引入无界新复杂度，则本定理不适用，该情况必须转入 Complexity-Escape/FCT/LSMP 分支。

该义务可拆成三项：

1. **自然细化**：从 `G_k` 到 `G_{k+1}` 时，窗口只新增一个局部坐标条件，不重写旧坐标；
2. **复杂度稳定**：有限并差、倒数环带和 dyadic 标签在新增素数层下复杂度不爆炸；
3. **误差平方可和**：边界、Vaaler 截断、dyadic 端点误差在 `k` 上平方可和或由 LV/LSMP 吸收。

## 7. 与 Dense-scale orthogonality 的关系

本文证明了 DSO-C 的核心 square-function：

`固定 L^2 函数在 inverse-limit CRT 空间上的新增层偏差平方和有界`。

因此密集尺度正交的剩余硬点从“证明某种跨尺度正交”缩小为具体的“模板一致性 DSO-C-TC”。下一步最优专攻就是逐项证明 PPI/OMR 固定模板满足自然细化、复杂度稳定与误差平方可和。
