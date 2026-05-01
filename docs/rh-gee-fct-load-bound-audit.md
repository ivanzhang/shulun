# GEE-FCT 负担上界审查：Noether 下降、重复转出与剩余接口

本文专攻 `GEE-FCT`。现有 FCT 文档已经证明 FCT 内部不存在无限回流：频率碰撞链要么 Noether 势函数下降，要么重复状态转入 `PI/SC/LV/LSMP/DSO/CE`。但 GEE 需要定量上界：

`Load(FCT;X)=o(Δ)`。

因此本文把 FCT 负担拆成三类：下降步、重复状态、独立频率误归入。

## 1. FCT 的正确 GEE 口径

FCT 只应登记真正的短深度频率碰撞证书：当前频率落入祖先 span，且该证书导致规范低维状态发生真闭包变化。若新频率在旧 span 外，按定义不是 FCT，应转 `NRC/DSO/PI`。

因此定义：

- `Load_desc(FCT;X)`：Noether 势函数严格下降的真 FCT 步；
- `Seed_rep(FCT;X)`：重复状态产生的 `PI/SC/LV/LSMP/DSO/CE` seed；
- `Seed_ind(FCT;X)`：旧 span 外的新频率，转入 `NRC/DSO/PI`。

GEE-FCT 只需证明 `Load_desc(FCT;X)=o(Δ)`；两类 seed 必须转出并删除。

## 2. 下降步的容量预算

设 FCT 状态势函数为

`𝓝(S)=A_1r_free+A_2q+A_3L-A_4τ`。

每个真 FCT 步使 `𝓝` 至少下降 `1`。在排除 `LV/LSMP/SC/CE` 后，`𝓝` 有下界，且初始复杂度由固定模板给

`𝓝(S_0)<=log^{C_FCT}X`。

因此任一路由路径上真 FCT 步数至多 `log^{C_FCT}X`。这本身只给多对数个 FCT 证书，并不自动给 `o(Δ)`；还需每个真下降步满足相对体积阈值，或者下降步只作为路由中间节点而不登记最终负担。

本文采用后一种更安全口径：真下降步是**内部转移**，不作为最终出口负担；只有当下降导致低体积/短簇/投影等结构出现时，转入对应出口。

## 3. FCT 内部转移原则

FCT 真下降步不消耗异常本身，而是改写其结构证书：把同一个异常原子从一个低维状态送到更低势函数状态。最终必发生三种结果之一：

1. 降到低体积或短簇阈值，转 `LV/SC/LSMP`；
2. 出现重复规范状态，转 `PI/SC/LV/LSMP/DSO/CE`；
3. 新频率离开旧 span，转 `NRC/DSO/PI`。

若把每个内部下降步都记为 `Load(FCT)`，会重复记录同一异常原子。因此 GEE-FCT 的正确负担定义应只登记“未转出的最终 FCT 停止态”；而 FCT-Noether 说明这种停止态不存在。

## 4. Theorem GEE-FCT-Transfer

**Theorem GEE-FCT-Transfer.** 假设 FCT-Noether 下降账本、重复状态能量出口和 Seed-Transfer 去重账本成立。则可以重定义 GEE 路由，使：

1. FCT 真下降步作为内部路由，不计入最终 `Load(FCT)`；
2. 旧 span 外新频率转入 `NRC/DSO/PI`；
3. 重复状态转入 `PI/SC/LV/LSMP/DSO/CE`；
4. 低体积/短簇/小质量细化转入 `LV/SC/LSMP`；
5. 最终留在 FCT 的负担为零，故

   `Load(FCT;X)=0`，在该路由定义下当然为 `o(Δ)`。

**证明。** 对任一进入 FCT 的异常原子，沿规范 FCT 状态递推。若遇到旧 span 外频率，按定义改路由到 `NRC/DSO/PI`。若处于真 FCT 闭包步，势函数下降；由于势函数有下界，真下降步有限。下降终止后若没有转出，则只能是重复规范状态；由重复状态能量出口转入 `PI/SC/LV/LSMP/DSO/CE`。若下降过程中体积低于阈值或出现短簇/小质量，则转入对应出口。所有转出由 Seed-Transfer 保证有限重叠且从 FCT 删除。因此没有异常原子最终停留在 FCT。证毕。

## 5. 审稿注意

这个结论不是说频率碰撞“不存在”，而是说 FCT 不是最终负担出口。FCT 是内部 Noether 化简器：它把频率碰撞异常转化为更低势函数状态，最终转入 `NRC/DSO/PI/SC/LV/LSMP/CE` 等出口。

因此 `GEE-FCT` 可标记为“内部转移闭合”；剩余压力转移到接收出口的上界，尤其是 `GEE-SC` 与 `GEE-A`，以及已条件闭合的 `PI/DSO/NRC/LV/CE/LSMP`。
