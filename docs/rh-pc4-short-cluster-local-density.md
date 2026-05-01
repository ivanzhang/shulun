# PC4-SC：短窗锚复用局部密度命题

本文接续 `docs/rh-pc4-short-cluster-mass-balance.md`。SC-Mass-Balance 后，短簇剩余硬点是：固定物理短窗内是否可能长期承载离线零点级锚复用过密。本文把该情形压回乘积容量 `q_1q_2r`、CRT 非零类均衡、LV 体积账本，或已闭合的 PC4-PI/PC4-A/PC4-FCT 分支。

## 1. 局部短窗模型

设短窗 `I_X` 长度为 `L_X=o(X)`，其中存在允许锚复用过密。按 AAI 接口，任意双锚复用点有正规形

`n=q_1q_2r`, `q_i~Q`, `Q^2R~X`。

限制到短窗 `I_X` 后，固定 `r` 与 `q_1` 时，`q_2` 被薄壳与短窗同时限制；因此局部自由度小于全局 `R·Q` 体积。

## 2. 局部乘积容量界

**Lemma SC-LD1（短窗双锚容量）。** 在短窗 `I_X` 内，同层双锚复用点的有效体积满足

`Vol_eff(I_X;Q,R) << (L_X/X) RQ log^C X + R log^C X`。

特别地，若 `L_X <= X/log^B X` 或 `R<log^A X`，则该层由 LV 吸收，除非质量集中到更短窗口。

**证明。** 全局同层双锚体积由 AAI 正规形与 LV 账本给 `RQ log^C X` 量级。短窗只占平滑尺度比例 `L_X/X`，给第一项。端点与薄壳边界对每个 `r` 至多贡献 `log^C X` 个异常选择，给第二项。若短窗或 `R` 足够小，代入 `docs/rh-lv-low-volume-principle.md` 的 LV 条件即可吸收；若平凡比例失败，只能是更短窗口集中。证毕。

## 3. 局部过密到结构分支

**Lemma SC-LD2（局部过密三分）。** 若固定短窗内锚复用超过 SC-LD1 的零频容量一个离线零点级量，则至少发生一项：

1. 过密在允许投影窗口中可检测，转入 PC4-PI；
2. 过密表现为 ACC 覆盖容量同步过剩，转入 PC4-A；
3. 过密由低维相位锁定造成，转入 PC4-FCT；
4. 过密集中到更短窗口或低体积尾层，转入 LV/LSMP。

**证明。** 超过局部乘积容量的部分不能由零频体积解释。若它在 D 组可检测 σ-代数中出现，则相位推送给投影增量，转入 PC4-PI。若它主要改变允许覆盖容量账本，则转入 PC4-A。若它只在低维 Bohr 相位中可见且非共振失败，则转入 PC4-FCT。若都不可检测，则只能是更短尺度或低体积原子集中，由 LV/LSMP 吸收。证毕。

## 4. SC-Local-Density 主命题

**Proposition SC-Local-Density（短簇局部密度，条件化）。** 固定物理短窗若在无穷多尺度上反复承载离线零点级锚复用过密，则至少触发以下一项：

1. LV/LSMP 低体积或更短簇吸收；
2. PC4-PI 高投影增量；
3. PC4-A ACC 同步过剩；
4. PC4-FCT 频率闭包；
5. 局部乘积容量界 SC-LD1 被违反。

在接受 AAI 正规形与 LV 体积账本时，第 5 项不可能作为独立终端。

**证明。** 对短窗内复用点按 dyadic `Q,R` 分层。若每层满足 SC-LD1，则总零频容量不足以支撑离线零点级超额，除非进入 LV/LSMP。若某层超过 SC-LD1 的容量，由 SC-LD2 转入 PC4-PI、PC4-A、PC4-FCT 或更短簇。迭代更短簇时，窗口长度严格下降或体积预算下降，不能无限；否则由 LV 吸收。证毕。

## 5. 对 PC4-SC 的影响

结合 `docs/rh-pc4-short-cluster-seed.md` 与 `docs/rh-pc4-short-cluster-mass-balance.md`，SC-Local-Density 排除了最后的物理短窗锚复用过密独立通道。`docs/rh-pc4-short-cluster-descent-ledger.md` 进一步把更短簇递归写成离散下降账本，可合并为 `PC4-SC-Closure`，把短簇分支推进为条件化闭合分支。
