# PC4-A：ACC 不同步分支闭合命题

本文合并 `ACC-Seed` 与 `ACC-Sync-Pressure`，形成 RH 总攻框架中 ACC 过剩分支的条件化闭合命题。本文不宣称证明 RH；它说明在 PC4-PI、PC4-FCT、LSMP/LV 与短簇等终端均按既有接口处理时，允许覆盖容量 `ACC` 不能作为 RH 反例链条的最终同步吸收通道。

## 1. 输入与目标

由 `docs/rh-pc3-ov2-bridge-theorem.md`，若离线零点造成平滑素数过疏，且不进入 D 组终端，则出现允许覆盖容量过剩：

`ACC_z(X)>=ACC_z^0(X)+cX^{β-o(1)}`, `β>1/2`。

PC4-A 的目标是排除这种过剩在无穷多尺度上同相位模拟同一个离线零点波动。

## 2. Seed：固定 ACC 模板同步种子

由 `docs/rh-pc4-acc-seed.md`，若 ACC 过剩可作为最终吸收通道，并排除 D 组终端、PC4-PI、PC4-FCT、LSMP/LV、短簇与复杂度逃逸，则可抽取：

1. 固定 ACC 组件类型 `𝓒_*`；
2. 固定有限复杂度覆盖模板 `𝓐_*`；
3. 固定离线相位短弧 `I_*`；
4. 无穷尺度子列；

使 `𝓐_*` 在该子列上产生同向 `X^{β-o(1)}` 级过剩。

## 3. Sync-Pressure：同步过剩转终端

由 `docs/rh-pc4-acc-sync-pressure.md`，固定 ACC 模板同向过剩必触发以下至少一项：

1. `PC4-PI` 高投影增量；
2. `PC4-FCT` 频率闭包；
3. 短簇；
4. `LSMP/LV` 低质量或低体积逃逸；
5. DSO/CE 容量矛盾。

该命题来自固定模板偏差分解 `low/osc/tail`：低体积或尾项转 LSMP/LV/短簇，振荡主项转 PI/FCT 或容量矛盾。无循环账本见 `docs/rh-pc4-acc-sync-ledger.md`，其中真模板变化导致离散势函数下降，固定模板重复则强制转入这些终端边。

## 4. PC4-A 主闭合命题

**Theorem PC4-A-Closure（ACC 不同步分支闭合，条件化）。** 假设：

1. PC3-OV2 在无穷多尺度输出 ACC 过剩；
2. PC4-PI 与 PC4-FCT 按对应闭合文档条件化成立；
3. LSMP/LV、DSO/CE 容量输入与短簇终端按现有接口处理；
4. 复杂度逃逸按 CE/FCT/LSMP 接口处理。

则 ACC 过剩不能作为 RH 反例链条的最终逃逸通道。

**证明。** 反设 ACC 过剩作为最终通道。由 ACC-Seed，排除复杂度逃逸和其它终端后，抽取固定 ACC 模板与同相位子列，得到固定模板同步过剩。由 ACC-Sync-Pressure，该同步过剩必须转入 PC4-PI、PC4-FCT、短簇、LSMP/LV 或 DSO/CE 容量矛盾。前两者由对应闭合文档排除；其余由本定理假设中的终端接口处理。矛盾。证毕。

## 5. 对 RH 总攻的影响

PC4-A 现在与 PC4-PI、PC4-FCT 一样，进入条件化闭合状态。PC-4 总框架剩余主分支进一步缩小为：

1. `PC4-SC`：短簇跨尺度排斥；
2. `PC4-Dual`：过密对偶或多零点相干补充。

PC4-A 的失败分支进入短簇时，由 `docs/rh-pc4-short-cluster-descent-ledger.md` 的 `SC-Descent-Termination` 处理；进入 PI/FCT 时分别由对应终端归约和 Noether 下降账本处理。因此 A 分支已可作为总事件图中的无循环输出边。
