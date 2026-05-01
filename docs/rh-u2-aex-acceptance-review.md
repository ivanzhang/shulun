# U2 AEX-1/2/3 接受性核验与条件化措辞消除

本文处理最终升级清单中的 U2：主稿中 AEX-1/2/3 是否仍是条件输入，能否把 analytic exit reduction 从“conditional exactly on AEX-1/2/3”升级为由前文已登记 proposition/input 支撑的定理链。

## 1. 结论

U2 可标记为“主稿措辞补正完成，但最终主定理 warning 仍不删除”。理由：

- AEX-1 已拆成 Baseline-Subtraction、PI-Lac、PI-Dense；
- PI-Lac 已由 `docs/rh-pi-lac-input-final.md` 完成；
- PI-Dense 已由 `docs/rh-pi-dense-input-final.md` 归约到 `DSO-SF/EXT-KL`；
- AEX-2 的唯一核心输入 `DSO-SF` 已由 `docs/rh-dso-sf-input-final.md` 完成；
- AEX-3 的单变量外部输入 `EXT-KL` 已由 `docs/rh-ext-kl-precision-final.md` 完成，DSO-E 对 `DSO-SF` 的依赖已解除；
- Tail/RKS 与双变量 PPI 在 AEX-3 中不是 NRC 终态，而是 Transfer 到已命名出口。

因此，主稿不应再写“conditional exactly on AEX-1, AEX-2, AEX-3”。更准确的表述是：analytic exits are controlled by the AEX-1/2/3 propositions together with the already recorded PI-Lac, PI-Dense, DSO-SF, EXT-KL, and transfer-accounting inputs.

## 2. AEX-1 接受性链

AEX-1 目标是：

`Excess_PI <= Δ/log^{B_PI}X`。

证明链：

1. Baseline-Subtraction 删除零频容量，不把 `Cap^0` 计入异常负担；
2. lacunary pack 由 PI-Lac 有限重叠/Bessel 容量处理；
3. dense pack 由 PI-Dense 归约到 DSO-C/TC/DSO-E；
4. DSO-C/TC 接入 martingale square-function；
5. DSO-E 的非共振由 EXT-KL/NRC，resonant 由 FCT，小质量由 LSMP，剩余由 DSO-SF；
6. Transfer-Accounting 删除源出口重复负担。

所以 AEX-1 不再是独立未证输入；其剩余依赖已归入 DSO-SF/EXT-KL 与命名出口体系。

## 3. AEX-2 接受性链

AEX-2 目标是：

`Excess_DSO <= Δ/log^{B_DSO}X`。

证明链：

1. 固定复杂度频率包是 CRT/Bohr 有限交；
2. Parseval/frame 把包平方和控制到 martingale difference；
3. 非 square-summable、非允许包、高重叠包均转命名出口；
4. DSO-SF 给 Hilbert martingale identity：`Σ||D_kF||_2^2 <= ||F-E_0F||_2^2`，扣除零频容量后只剩阈值超额；
5. 阈值层级压到 `o(Δ log^{-C_route}X)`。

故 AEX-2 可视为由 DSO-SF proposition 支撑。

## 4. AEX-3 接受性链

AEX-3 处理 NRC 四入口：

1. 单变量 PPI：`EXT-KL` 给 `X^{1/2}log^C X=o(Δ)`；
2. Tail/RKS：低体积进 LV，否则回主层 PPI；
3. 双变量 PPI：通过 PPI-Rank/Capacity/MidCap 转 `LSMP/SC/PI/DSO/CE`，不作为 NRC 终态；
4. DSO-E：由 DSO-SF 给 square-function 基线，失败转 `PI/FCT/CE/LSMP`。

因此 NRC 不保留独立自由终端。

## 5. 对主稿的修改要求

主稿 analytic exit reduction 证明末句应从：

`conditional exactly on AEX-1, AEX-2, AEX-3 and accepted external estimates`

改为：

`by the preceding AEX propositions and the recorded PI-Lac/PI-Dense/DSO-SF/EXT-KL inputs`。

同时 AEX-2 proposition 前的“remaining capacity input DSO-SF”应改成“recorded capacity input DSO-SF”，PI-Dense 中的“remaining DSO-SF”也应改成“recorded DSO-SF”。

## 6. 仍不删除主定理 warning 的原因

U2 只消除 AEX 条件化措辞。主定理 warning 还受 U1、U3、U4、U5 约束：主定理前提仍是 conditional theorem，EXT 页码/定理号未核验，摘要/标题仍是 review draft，且尚未做 TeX 编译审查。
