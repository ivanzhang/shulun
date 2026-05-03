# RRD 同权归一化与两段式拆解

**状态：** `same_weight_reduction_and_two_stage_rrd_obligation`

本报告专攻 `RRD`：把粗数替换误差从原始振荡和式中剥离出来，检查它能否进入上一轮建立的 `C_RRD<=0.020` 账本。

## 1. 直接单密度替换的压力结论

- RRD 账本目标：`C_RRD<=0.020`。
- 旧扫描样本数：`8`。
- 旧 `roughDiff/env` 最大值：`0.200002`。
- 旧 `roughDiff/env` 中位数：`0.033779`。
- 最坏样本：`P=5003, M=P^1.2, R=P^0.3`。

结论：旧的一步常数密度替换不能直接当作 `C_RRD<=0.020` 的证明。它是定位工具，不是终局 RRD 估计。

按 `M` 层分组：

| M_exp | 样本数 | max roughDiff/env | median | 是否直接低于 0.020 |
| ---: | ---: | ---: | ---: | :---: |
| 1.200 | 4 | 0.200002 | 0.092177 | N |
| 1.400 | 4 | 0.016077 | 0.009683 | Y |

这给出一个有用定位：较长 `M=P^1.4` 层已经接近或低于预算，真正硬点集中在较短粗锚层，例如旧样本中的 `M=P^1.2`。

## 2. 同权归一化的核心恒等式

对

\[
K_{h,\ell}(m)=e\left({hX\over \ell m}\right)
\left(1-e\left({hH\over \ell m}\right)\right)
\]

在 `m~M` 且 `hH/(ell M)` 小的区间，有一阶振幅界

\[
|K_{h,\ell}(m)|\le 2\pi {hH\over \ell M}+O\left(({hH\over \ell M})^2\right).
\]

代回 RRD 系数后，主因子发生精确降阶：

\[
{|\omega_\ell|\over h}\cdot {hH\over \ell M}
\bigg/ {H\over M}
={|\omega_\ell|\over \ell}.
\]

因此 RRD 天然落入与 QLOW 相同的 Selberg 变差范数

\[
\mathcal V_\omega=\sum_\ell {|\omega_\ell|\over \ell}.
\]

这一步是本轮真正的结构推进：`RRD` 不需要新归一化，只需证明粗数误差在上述同权测试范数中足够小。

## 3. 必要两段式拆解

令

\[
a_m=1_{P^-(m)>Y}-\rho_M.
\]

不能直接要求 `a_m` 对所有临界核都小，因为小模周期和 Buchstab 低层会产生可见结构。应取一个低模投影 `\Pi_{\le Z}`，写成

\[
a_m=\Pi_{\le Z}a_m+(1-\Pi_{\le Z})a_m.
\]

于是

\[
\mathcal E_{\rm RRD}=\mathcal E_{\rm low}+\mathcal E_{\rm perp}.
\]

低模项不是随机误差，应进入 `OSPC/CRTDefect` 或单独预算；正交项才用 Buchstab+CRT 均衡+短窗不可复用证明小范数。

## 4. 新的 RRD 子预算

| 子项 | 预算 | 证明义务 |
| --- | ---: | --- |
| `RRD-low` | 0.006 | 证明该低模项或者被并入 OSPC/CRTDefect 出口，或者在 RRD 账本中消耗不超过 0.006。 |
| `RRD-perp` | 0.012 | 用 Buchstab 分解、CRT 非零类均衡和短窗不可复用证明同权测试范数不超过 0.012。 |
| `RRD-conversion` | 0.002 | 把 |1-e(t)| 的二阶余项、端点层和有限截断误差全部外向舍入进 0.002。 |

三项合计仍为 `0.020`。因此 `RRD` 的下一步最小硬点已从“证明单密度替换很小”改为：

\[
C_{\rm RRD-low}+C_{\rm RRD-perp}+C_{\rm RRD-conv}\le 0.020.
\]

## 5. 审稿结论

旧的一步常数密度替换在压力样本中最坏 roughDiff/env 约为 0.200002，不能直接作为 C_RRD<=0.020 的证明。可行路线是先剥离低模/Buchstab 可见结构，再只对正交余项证明同权小范数。

下一步应先形式化 `\Pi_{\le Z}`：它必须是有限小模周期投影或 Buchstab 低层投影，并证明低模部分若超过 `0.006` 就自动触发 OSPC/CRTDefect；否则剩余正交项进入 `0.012` 的同权大筛/均衡估计。

## 6. 低模投影接口更新

后续 `docs/monograph/rse-rrd-low-projection-dichotomy.md` 已把 `Pi_{<=Z}` 正式改写为低模字典 `D_Z` 的正交投影，并修正 OSPC 归一化为

\[
E_{\rm dir}(q,r)=
\frac{(r-1)\sum_a |C_a(q,r)|^2}{\mathcal A(q,r)^2}
\ge 1+\delta_{\rm dir}.
\]

因此本报告中的 `RRD-low` 大情形应理解为：某个低模块的投影贡献超过块预算，并触发修正后的 `OSPC*` 或直接 `CRTDefect`。
