# PC-3 + OV-2 桥接定理：素数过疏到覆盖过剩或 D 组终端

本文把 `docs/rh-pc3-formal-theoremization.md` 与 OV-2 三接口闭合文档合并为一个 RH 反例矛盾场路线中的正式桥接定理。它不是 RH 证明；它只完成 PC-3 这一桥接环节：若离线零点造成平滑窗口内素数过疏，则局部覆盖动力系统必须出现覆盖容量过剩或 D 组结构终端。

## 1. 依赖文档

- `docs/rh-pc3-formal-theoremization.md`：PC-3 无权核心与 Buchstab 加权提升；
- `docs/rh-ov2-admissible-anchor-interface.md`：AAI，允许锚语义接口；
- `docs/rh-ov2-phase-pushforward-interface.md`：PPI，相位推送接口；
- `docs/rh-ov2-main-layer-capacity-interface.md`：MLC，主层容量接口；
- `docs/rh-lv-low-volume-principle.md`：LV，低体积原则；
- D 组附录：OMR/CGTP/LSMP/NRC/FCT 终端机制。

## 2. 桥接定理

**Theorem PC3-OV2（素数过疏桥接）。** 设 `z=(log X)^A`, `0<A<1`，固定平滑窗口 `W`。设在该窗口内存在素数过疏

`P_z(X)<=P_z^0(X)-Δ`, `Δ=X^{β-o(1)}`, `β>1/2`，

且边界误差 `Err_bd=o(Δ)`。假设 LV、NRC、FCT 与 D 组 OMR/CGTP/LSMP 接口均按现有附录成立。则二者必居其一：

1. 无权允许覆盖容量出现过剩：

   `ACC_z(X)>=ACC_z^0(X)+cΔ`；

2. 触发 D 组终端：短簇、高投影增量、FCT 或 NRC 异常。

若额外满足 PC3-B 的 dyadic 加权提升条件，则第一分支提升为 Buchstab 权覆盖容量过剩：

`ACC_z^B(X)>=ACC_z^{B,0}(X)+c(log z)Δ`，

除非加权 overlap-energy 触发同型 D 组终端。

## 3. 证明

由 PC3-U，素数过疏给出粗合数过剩：

`B_z(X)>=B_z^0(X)+Δ-o(Δ)`。

写允许覆盖容量为

`ACC_z=B_z-O_z`。

若 overlap 小，即

`|O_z|<=X^{1/2+ε}log^C X=o(Δ)`，

则立刻得到第一分支。

若 overlap 大，则 `E_ov>X^{1+ε}`。AAI 把 overlap 解释为允许覆盖锚相对真实最小锚账本的扣重，并给出双锚正规形 `n=q_1q_2r`。PPI 把主层中 D 组可检测的双锚偏差推送到倒数环带/斜线相位窗口。MLC 与 LV 排除低容量尾层和不可检测正交质量。于是大 overlap 必进入 D 组 OMR/NRC/FCT 三分支，触发短簇、高投影增量、FCT 或 NRC 异常。故第二分支成立。

Buchstab 加权版本由 PC3-B 对 dyadic 层过剩乘以 `log Q>=log z` 得到，overlap 部分重复上述 OV-2 论证。证毕。

## 4. 逻辑地位

PC3-OV2 完成的是 RH 路线中的一段局部-全局桥接：

`离线零点导致素数过疏`  
`=> CRT 候选总量刚性保持`  
`=> 粗合数/覆盖容量必须补偿`  
`=> 补偿若被 overlap 吸收，则 overlap 本身触发 D 组终端`。

它尚不包含 PC-1、PC-2、PC-4：

- PC-1：离线零点到足够强的平滑素数过疏窗口；
- PC-2：Li/显式公式零频基线与 CRT 候选基线完全匹配；
- PC-4：覆盖容量过剩或 D 组终端最终反推出 RH 反例矛盾。

因此本文应作为 RH 探索论文的桥接定理，而不是最终 RH 证明。
