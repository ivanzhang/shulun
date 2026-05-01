# RH 反例矛盾场：PC1-PC4 接口闭合审查

本文审查当前 RH 反例矛盾场路线从 PC1 到 PC4 的逻辑拼接。目标不是宣称 RH 已证明，而是把现有文档的输入、输出、符号、尺度、误差和剩余条件化接口逐项对齐，为后续无条件化攻坚提供清晰地图。

## 1. 总链条

当前路线为：

`离线零点`
`=> PC1 平滑素数异常`
`=> PC2 Li/CRT 零频基线匹配`
`=> PC3-OV2 覆盖过剩或 D 组终端`
`=> PC4-A/SC/PI/FCT/Dual 排斥`
`=> 反例矛盾场闭合（条件化）`。

其中 PC1 与 PC2 负责把解析零点波动转成 CRT 筛余候选中的离散异常；PC3 把素数异常转成覆盖动力系统异常；PC4 排斥所有可持续异常通道。

## 2. PC1 输出核查

`docs/rh-pc1-offline-zero-smooth-window.md` 输出：若存在离线零点 `β>1/2`，则存在平滑权、无穷尺度与符号 `σ`，使 Chebyshev 或无权素数窗口异常满足

`σ(P-P^0) >= X^{β-o(1)}`。

接口核查：

1. **幅度**：固定对数损失吸收到 `X^{o(1)}`，仍保持 `β>1/2`；
2. **符号**：可能过疏或过密；过疏走 PC3-OV2，过密走 PC4-Dual 或反相位子列；
3. **权重**：Chebyshev 权可经 Buchstab 加权接口保留，也可细分成无权窗口；
4. **剩余硬点**：Landau--Ingham 振荡原则与权函数非湮灭选择属于解析外部输入，需要最终精确引用或逐行展开。

## 3. PC2 输出核查

`docs/rh-pc2-li-crt-baseline-match.md` 输出：取 `z=(log X)^A`, `A<1`，CRT 周期 `M=exp((log X)^A)=X^{o(1)}`，候选总量满足

`C_z=C_z^0+o(Δ)`。

因此：

- 过疏 `P_z<=P_z^0-Δ` 推出 `B_z>=B_z^0+Δ-o(Δ)`；
- 过密 `P_z>=P_z^0+Δ` 推出 `B_z<=B_z^0-Δ+o(Δ)`。

接口核查：

1. **尺度匹配**：`M=X^{o(1)}`，CRT 边界误差低于 `X^{β-o(1)}`；
2. **基线一致**：不是要求 `P_z^0=C_z^0`，而是 `B_z^0=C_z^0-P_z^0`；
3. **符号保留**：PC2 不改变异常符号，只把它转成粗合数候选的相反符号；
4. **剩余硬点**：候选总量的平滑边界误差与权重正规化需在最终稿中保持统一符号和常数。

## 4. PC3-OV2 输出核查

`docs/rh-pc3-ov2-bridge-theorem.md` 处理过疏：

`P_z<=P_z^0-Δ`
`=> ACC_z>=ACC_z^0+cΔ 或 D组终端`。

依赖 AAI/PPI/MLC/LV 与 D 组附录，将 overlap 异常解释为双锚正规形、相位推送、主层容量或终端机制。

接口核查：

1. **过疏闭合方向**：已进入 PC4-A 或 D 组分支；
2. **加权版本**：Buchstab 加权只放大主层容量，不改变终端类型；
3. **overlap 语义**：需要 AAI 正规形保证“覆盖容量过剩”不是纯记账幻象；
4. **剩余硬点**：OV2 三接口仍是条件化结构输入，后续无条件化时必须逐项定理化。

## 5. PC4 输出核查

当前 PC4 显性分支状态如下：

1. `docs/rh-pc4-acc-closure-theorem.md`：PC4-A，ACC 同步过剩/不足的条件化闭合；
2. `docs/rh-pc4-short-cluster-closure-theorem.md`：PC4-SC，短簇分支条件化闭合；
3. `docs/rh-pc4-pi-closure-theorem.md`：PC4-PI，高投影增量条件化闭合；
4. `docs/rh-pc4-fct-closure-theorem.md`：PC4-FCT，频率闭包条件化闭合；
5. `docs/rh-pc4-dual-overdense-closure.md`：PC4-Dual，过密对偶分支条件化闭合框架。

接口核查：

- 过疏分支：PC3-OV2 输出由 PC4-A/SC/PI/FCT/NRC 吸收并排斥；
- 过密分支：PC4-Dual 经 `Dual-Gap-Ledger` 转成 ACC 负向同步、overlap 过剩、`DGap` 压缩异常、对偶短簇、对偶 PI 或对偶 FCT；
- 复杂度逃逸：由 CE/FCT/LSMP/LV 接口接收；
- 非共振异常：由 NRC/EXT 外部包接收。

## 6. 统一矛盾场方程

把过疏与过密统一写成绝对异常场：

`E_z(X)=P_z(X)-P_z^0(X)`，`|E_z(X)|>=Δ`。

CRT 候选刚性给

`B_z-B_z^0=-E_z+o(Δ)`。

覆盖分解给

`B_z-B_z^0=(ACC_z-ACC_z^0)-(O_z-O_z^0)+(Gap_z-Gap_z^0)+Err_z`。

因此

`-E_z=(ACC_z-ACC_z^0)-(O_z-O_z^0)+(Gap_z-Gap_z^0)+o(Δ)`。

若 `E_z<0`，主压力是 ACC 正向过剩或 D 组终端；若 `E_z>0`，主压力是 ACC 负向不足、overlap 过剩、`DGap=Gap_z^0-Gap_z` 压缩异常或对偶 D 组终端。无论符号如何，`X^{β-o(1)}` 级异常必须进入以下有限类型：

`ACC / SC / PI / FCT / NRC / LV-LSMP / 接口失败`。

PC4 各 closure 文档的共同作用是排除前六类作为最终逃逸通道；剩余就是把“接口失败”逐项无条件化。

## 7. 当前闭合等级

当前可以严谨表述为：

**Conditional RH-Contradiction-Field Closure.** 若 PC1 的解析振荡输入、PC2 的 CRT 基线匹配、PC3-OV2 的 AAI/PPI/MLC/LV 桥接、PC4 的 A/SC/PI/FCT/Dual closure，以及 NRC/EXT 外部包均成立，则离线零点不能被该覆盖动力系统吸收。

不能表述为：RH 已无条件证明。

## 8. 下一步无条件化义务

按优先级排序：

1. 精确引用或逐行证明 PC1 的 Landau--Ingham 平滑振荡命题；
2. 将 PC2 的 CRT 候选边界误差写成统一显式引理；
3. 把 PC3-OV2 的 AAI/PPI/MLC 三接口从条件化接口降为定理；
4. 把 PC4-Dual 中 `DGap` 的 SC/PI/FCT 分解完全无条件化；
5. 对 PC4-A/SC/PI/FCT 的 closure 假设逐项回溯，消除循环依赖。

完成以上五项后，RH 反例矛盾场才可能从“条件化闭合框架”升级为可审稿的无条件证明候选。
