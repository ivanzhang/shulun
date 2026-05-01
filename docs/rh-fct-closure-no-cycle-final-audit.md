# FCT closure 无无限递归最终审查

本文对 `docs/rh-pc4-fct-closure-theorem.md` 作最终无循环审查：确认 `FCT_seed -> FCT_drift -> FCT_Noether` 不会形成未命名回流，并且每条失败边都进入已命名终端。本文仍属于 RH 反例矛盾场的条件化无条件化推进，不宣称 RH 已证明。

## 1. FCT 分支事件图

FCT 分支只允许以下事件节点：

1. `Seed`：固定低维编码种子；
2. `ZeroFreq`：新增坐标命中只有零频期望；
3. `SquarePressure`：非主局部偏差平方压力；
4. `NewClosure`：新的低维同步闭包证书；
5. `NoetherDescent`：规范状态势函数严格下降；
6. `RepeatState`：同一规范 Bohr 状态重复承载偏差；
7. 终端：`PI/SC/LV/LSMP/DSO/CE/Err`。

不允许出现“FCT 自由回流”或“未命名容量失败”。

## 2. 边的逐项审查

| 边 | 来源文档 | 结论 | 非闭合出口 |
| --- | --- | --- | --- |
| `Seed -> Drift` | `docs/rh-pc4-fct-seed.md`, `docs/rh-fct-seed-isomorphism-audit.md` | 固定低维相位证书进入漂移压力分析 | 类型不固定则 `CE/LSMP/DSO-PI` |
| `Drift -> ZeroFreq` | `docs/rh-pc4-fct-phase-drift.md` | 只给零频背景，不能承载离线异常 | 直接矛盾当前成功尺度假设 |
| `Drift -> SquarePressure` | `docs/rh-pc4-fct-phase-drift.md` | 命中超额给非主平方能量 | 转 `PI/SC/LV/LSMP/DSO` |
| `Drift -> NewClosure` | `docs/rh-pc4-fct-phase-drift.md` | 非共振失败给新 FCT 证书 | 进入 Noether 账本 |
| `NewClosure -> NoetherDescent` | `docs/rh-pc4-fct-noether-descent-ledger.md` | 非重复真闭包使离散势函数下降 | 若新增独立则不是 FCT，转 `DSO/PI` |
| `NewClosure -> RepeatState` | `docs/rh-pc4-fct-noether-descent-ledger.md` | 规范代表不变即重复状态 | 转重复能量出口 |
| `RepeatState -> terminal` | `docs/rh-pc4-fct-noether-descent-ledger.md` | 同一 Bohr 模板反复承载偏差 | `PI/SC/LV/LSMP/CE/DSO` |

每一条边都被既有文档接收；没有边返回到未标记的 FCT 状态。

## 3. 离散势函数防循环

FCT 状态规范化为

`S=(Λ,R,𝓑,τ)`，

势函数为

`𝓝(S)=A_1r_free(S)+A_2q(S)+A_3L(S)-A_4τ(S)`。

在排除 `LV/LSMP/SC/CE` 后，`r_free,q,L,τ` 均处于固定复杂度账本内，且 `L>=0`，故 `𝓝` 有下界。每个非重复真闭包步至少使 `𝓝` 下降 `1`。因此无限链若存在，只能在有限多次下降后进入重复状态；重复状态由 `FCT-ND2` 转终端。故 FCT 内部无循环。

## 4. 与 PC4 终端无循环的兼容

`FCT` 输出到 `PI` 或 `SC` 时，必须由 `docs/rh-pc4-terminal-final-no-cycle-audit.md` 接收；输出到 `LV/LSMP/DSO/CE` 时，必须由 `docs/rh-pc4-external-event-absorption-audit.md` 与 `docs/rh-lsmp-fct-capacity-final-audit.md` 接收。本文检查到的出口均属于这些已登记节点。

若某个出口不能被这些文档接收，则不是 FCT 内部问题，而是全局事件图登记缺口；当前正式入口未发现该缺口。

## 5. 最终审查命题

**Theorem FCT-Closure-NoCycle-Final（条件化）。** 在接受 `FCT-Seed`、`FCT-Drift`、`FCT-Noether-Descent` 及已登记终端吸收文档的前提下，FCT closure 分支不存在无限递归或未命名回流。任何试图长期由 FCT 吸收离线零点异常的链条，必在有限步内转入 `PI/SC/LV/LSMP/DSO/CE/Err` 或与零频不足矛盾。

**证明。** 由第 2 节事件图，FCT 成功尺度从 Seed 进入 Drift。Drift 的三分中，零频分支不能承载离线异常，平方压力分支转已命名终端，新闭包分支进入 Noether 账本。Noether 账本中，非重复闭包使离散势函数严格下降且势函数有下界；重复闭包转固定 Bohr 模板能量出口。故无限 FCT 内部链不存在。所有出口由第 4 节登记到 PC4 终端或外部吸收文档。证毕。

## 6. 对总攻割集的影响

本文把当前最小剩余硬点 `FCT phase drift/closure 无无限递归` 压缩为已登记的条件化闭合分支。下一阶段若继续向 RH 无条件证明推进，主任务不再是 DGap/FCT 内部分类，而是：

1. 上游解析输入 `PC1` 的标准外部定理精确化；
2. 容量定理常数与适用条件的最终逐项核验；
3. 全局事件图中 `PC4-A/SC/Dual` 与外部吸收的无回流总审查。
