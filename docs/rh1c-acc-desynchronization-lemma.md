# RH-1C 下一关键：ACC 不同步引理

本文件继续推进 `docs/rh1c-buchstab-weight-construction.md` 的结论。我们已经找到最有希望的统一权重

`ω_z^B(n)=log P^-(n)`，

它对素数保留 Chebyshev 权，对合数给出最小大因子锚分配。下一关键是证明允许合数覆盖容量 `ACC_z^B` 不能同步模拟离线零点带来的 `X^β` 级波动。

## 1. ACC 的定义

令 `P^-(n)` 为最小素因子，`z=X^α`。定义总 Buchstab 权

`T_z^B(X)=Σ_{P^-(n)>z} log P^-(n) W(n/X)`。

定义允许覆盖容量

`ACC_z^B(X)=Tail_z^B(X)+Body_z^B(X)+Overlap_z^B(X)`，

其中：

1. `Tail_z^B`：最小大因子或解释锚落在尾部区间的合数覆盖；
2. `Body_z^B`：主体双粗锚覆盖；
3. `Overlap_z^B`：多重解释、窗口边界与分裂权重修正。

定义缺口

`Defect_z^B(X)=T_z^B(X)-ACC_z^B(X)`。

若 `ACC` 完全等于全部合数 Buchstab 权，则 `Defect` 只是素数 Chebyshev 权，显式公式直接进入。但这不是局部机器允许的覆盖容量。真正的 `ACC` 必须受短窗互斥、Tail-log4、D 组能量与 FCT 约束。

## 2. ACC 不同步引理

**命题 ACC-Desync。** 对任意 `β>1/2`，合法允许覆盖容量满足

`ACC_z^B(X)-ExpectedACC_z^B(X) = O(X^{1/2}log^A X) + O(X/log^4X)`

或至少不能在无穷多 `X_j` 上产生与某个离线零点相同相位的 `X_j^β/log^A X_j` 级波动。

若该命题成立，则离线零点造成的 Chebyshev 波动无法被允许合数覆盖同步吸收，必然转化为 `Defect_z^B` 的大偏差，进入 M5/D 组矛盾场。

## 3. 三层容量分解

### 3.1 Tail 层

Tail 层对应大锚接近尺度上界。本文已有 Tail-log4 型估计：尾部锚平均贡献具有 `log^{-4}` 削薄。

目标子引理：

`Tail_z^B(X)-ExpectedTail_z^B(X) = O(X/log^4X)`。

这是当前框架中最稳的一层。

### 3.2 Body 层

Body 层是主体双粗锚覆盖。若它试图产生 `X^β` 级相干波动，则按 M5/D 组逻辑会迫出一阶偏差，进而触发短簇、高投影增量或 FCT。

目标子引理：

若 `Body_z^B` 在无穷多尺度上有 `X^β` 级同步波动，则存在跨尺度 D 组终端序列。

这把问题推向 RH-3，但已是可结构化对象。

### 3.3 Overlap 层

Overlap 是最危险的“调节器”。多重解释、边界窗口和权重分裂可能在局部抵消偏差。

目标子引理：

`Overlap_z^B` 的总变差受局部 multiplicity energy 控制，不能与固定离线零点相位在无穷多尺度相干。

这需要新的 overlap-energy 账本。

## 4. 为什么 ACC 不应能同步零点波动

离线零点波动是 Mellin 频率 `γ` 上的全局振荡，形如

`X^β cos(γ log X+θ)`。

而 ACC 的三层来源是局部因子覆盖：

- Tail 由接近 `X` 的锚平均决定；
- Body 由有限 CRT 相位和倒数锚决定；
- Overlap 由多个大因子组合决定。

要同步模拟零点波动，ACC 必须在无穷多尺度上生成同一个 Mellin 频率 `γ` 的相干项。但局部覆盖锚的自然频率是 CRT/additive/dedekind-like finite phase，不是连续 Mellin 频率。除非存在跨尺度频率锁定，否则同步不应发生。

这提示一个更强命题：

**Mellin-CRT 非共振引理。** 有限 CRT 覆盖频率族在跨尺度 Mellin 变量 `log X` 上与固定离线零点频率 `γ` 非共振；若共振无穷发生，则进入低维 frequency-closure，进而违反 Euler product 局部因子相容性。

## 5. 可攻的弱版：平均不同步

直接证明点态不同步很难。先攻平均版。

**ACC-Desync-Mean。** 对任意固定 `γ≠0`，有

`∫_{T}^{2T} (ACC_z^B(e^u)-ExpectedACC_z^B(e^u)) e^{-iγu} du = O(e^{T/2}T^A)`。

如果成立，则 ACC 没有 `e^{βu}e^{iγu}` 的 Mellin 频率成分，不能吸收离线零点。

这看起来更像可证明的指数和/振荡积分命题，可尝试用：

1. dyadic 锚分解；
2. Mellin transform of smooth weights；
3. Euler product 局部因子解析性；
4. D 组 FCT 处理低维共振。

## 6. 与经典 RH 等价命题的关系

需要警惕：若 ACC-Desync-Mean 强到直接给 `ψ(X)-X=O(X^{1/2+ε})`，它就等价于 RH 级别，不能指望轻易证明。可行策略是让 ACC-Desync 只处理“允许覆盖容量”这部分，而不是全部 prime error。

换言之，我们不证明所有 Chebyshev 波动小；我们证明合数覆盖容量无法模拟 Chebyshev 的离线零点波动。剩余波动就必须出现在 `Defect`，再由 M5/D 组排斥。

## 7. 下一步最优子目标

最小可攻子目标是 Tail+Overlap 的同步排除：

1. Tail 已有 Tail-log4，可视为完成；
2. Overlap 构造 multiplicity energy，证明其 Mellin-Fourier 变换平方平均受 `X^{1/2}` 控制；
3. Body 同步交给 D 组终端。

因此下一文档应专攻：

**Overlap-energy 引理。** 多重解释 overlap 不能在 Mellin 频率 `γ` 上产生 `X^β` 级相干波动。

## 8. 当前结论

ACC 不同步引理把 RH-1C 的难点进一步压缩为：允许合数覆盖容量是否能伪造离线零点波动？

Tail 层基本可控，Body 层可接 D 组，真正的新硬点是 Overlap 层的跨尺度相干控制。若 overlap-energy 能建立，RH-1C 将明显接近可证明形式。
