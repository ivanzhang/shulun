# 三命题临界密度反馈桥与当前最窄证明义务

## 0. 结论边界

本文记录一个新的统一桥梁：素数密度 `1/log x` 可视为自筛反馈系统的唯一临界固定点。
该桥梁能把三个命题的剩余硬点重新组织成同一类问题：

```text
反例导致局部幸存密度低于临界固定点
=> 必须由额外覆盖槽补洞
=> 额外覆盖槽若固定则形成 CRT/PDEC
=> 额外覆盖槽若移动则支付 Rankin/SAE 质量
=> 若二者都不能发生，则反例不存在
```

这不是最终无条件证明。它是把启发式洞察转换为可审查证明义务的桥梁。
任何后续论文表述都必须保持以下边界：

- Prime Matrix 行/列命题尚未无条件闭合；
- 二点筛尚未无条件闭合，其 `w=2` 情形仍是孪生素数级强度；
- RH 矛盾场仍是 verification package，独立逐行审稿前不能宣称 RH 终局证明。

## 1. 临界密度固定点

设一个自筛集合在尺度 `x` 的局部密度被模型化为

```text
rho(x) ~ C / (log x)^alpha.
```

它此前元素产生的一禁类筛强度为

```text
S(x) = sum_{a <= x, a in A} 1/a
     ~ integral_2^x rho(t) dt/t.
```

于是：

```text
alpha > 1: S(x) 收敛，筛强度太弱，幸存密度不应趋零；
alpha = 1: S(x) ~ C log log x，幸存密度约为 (log x)^(-C)；
alpha < 1: S(x) ~ C/(1-alpha) (log x)^(1-alpha)，筛强度太强，幸存密度低于任意 log 幂。
```

若要求筛后幸存密度与自身密度同阶，唯一指数固定点是

```text
alpha = 1.
```

在 `alpha=1` 层，若 `rho(x) ~ C/log x`，则筛乘积给出 `(log x)^(-C)`。
指数自一致要求 `C=1`。因此一阶固定点为

```text
rho(x) ~ 1/log x.
```

这个推导的严格含义是：`1/log x` 是自筛平均密度的临界固定点。
它本身还不是短区间非空、二点相关或 RH 的点态证明；要进入定理，需要把平均固定点升级为局部反集中、误差控制和短窗幸存者下界。

## 2. 对 Prime Matrix 行/列命题的作用

Prime Matrix 反例链的核心形态是：某个行/列窗口中，所有候选都被小于锚素数的素因子覆盖。
这等价于局部幸存密度被压到 `0`。按临界反馈原理，若平均临界密度应为 `1/log x`，那么这种局部压空只能由三类结构解释：

| 解释 | 证明出口 |
| --- | --- |
| 固定低/中模残基反复命中 | `PDEC/ColumnCRT` |
| 高因子补洞槽持续移动 | `SAE/Rankin` |
| 局部模型已经低于临界固定点 | 形成端点缺陷或低模/尾项异常 |

因此当前最窄自足目标应写成：

```text
CriticalFeedback-PM:
任何 Prime Matrix 反例若压空一个合法行/列窗口，
则它必须触发 PDEC/ColumnCRT，或触发可求和 SAE/Rankin 质量，
或违反临界幸存密度下界。
```

这条桥梁与当前最新前沿的精确连接点是：

```text
AffineTwinFillResidueArrivalBoundOrFillCatchUpMassPDECExclusion
```

已有账本说明：

- 最小阈值穿越没有 generator-only 路线；
- 每条最小穿越路线都必须新增 fill residue；
- 若不是新 residue，则触发 repeated-residue/reset/ColumnCRT PDEC；
- 若持续新增，则要支付 fill-side Rankin/SAE 质量；
- 当前有限前沿中同时穿越候选的最小新增 fill Rankin 质量为 `23339/137299`。

所以最直接的下一步不是另起命题，而是证明：

```text
FillArrivalBound:
在同一临界密度 convention 下，fill-side residue arrival 的总质量
不能长期超过阈值；一旦超过，必产生可命名的
FillCatchUpMass-PDEC、reset-PDEC 或 ColumnCRT。
```

如果 `FillArrivalBound` 闭合，AffineTwin 分支就会回流到当前已有的 SAE/PDEC/ColumnCRT 框架。
若它失败，失败形态本身就是新的显式反例证书，必须登记为 MovingSlot-PDEC/ColumnCRT，而不是无名逃逸。

## 3. 对二点筛命题的作用

二点筛不是单点 `1/log x` 的直接推论。它的临界密度是二禁类乘积：

```text
V_w(y) = product_{q <= y} (1 - nu_q(w)/q)
       ~ S(w) / (log y)^2,
```

其中 `nu_q(w)=1` 当 `q|w`，否则 `nu_q(w)=2`。
因此二点固定点的证明义务不是“有单点幸存者”，而是：

```text
真实二点剩余集 U_y 不能在新素数 p 的坏类 0,w mod p 上重度集中。
```

当前主稿已经把这一步压成 I3-Core/TRC：

```text
TrueResidualCorrelation:
对新模数 p>Y，真实剩余集 U_Y 在 0,w mod p 的总命中
不能超过二点临界模型允许的主量加可吸收误差。
```

最弱足够形态是总大关联不等式：

```text
sum_{P^alpha < p <= P} #{x in U_{P^alpha}(I): p | x(x-w)}
  < |U_{P^alpha}(I)|.
```

临界密度反馈在这里给出的不是终局证明，而是正确目标：

- 若真实剩余集比 `S(w)/(log y)^2` 更稀，二禁类约束会变弱，应产生更多幸存者；
- 若真实剩余集更密，后续新模数命中会变强，应产生更大覆盖压力；
- 平衡态必须围绕二点奇异级数临界密度。

缺口是把该平均平衡升级为新模数反集中定理。这仍是 prime-pair 级强度，不能由 Prime Matrix 单点行/列刚性自动代替。

## 4. 对 RH 矛盾场的作用

RH 分支中，离线零点会通过显式公式制造平滑素数异常。
临界密度反馈视角把该异常解释为：

```text
若素数密度偏离 1/log x 的自筛固定点，
则 CRT rough-composite ledger 中必须出现额外覆盖负载或缺口负载。
```

该负载随后进入 sparse、dense、tail、internal、global exits。
因此 RH 线的真正审稿义务是逐项确认：

- 显式公式入口没有丢失正幂；
- prime anomaly 到 CRT ledger 的转移同一权重 convention；
- 每个 controlled exit 都有上界、吸收或无循环证明；
- sparse/dense/tail 之间没有重复计数或未命名逃逸；
- final no-cycle ledger 不依赖未证明的 Prime Matrix 或二点筛结论。

换言之，临界密度反馈可作为 RH 矛盾场的解释框架，但不能跳过 controlled exits 的逐行验证。

## 5. 当前主攻顺序

最合理的作者侧攻坚顺序是：

```text
1. Prime Matrix:
   FillArrivalBound
   => FillCatchUpMass-PDEC/reset-PDEC/ColumnCRT 排斥
   => AffineTwin 分支回流
   => 接入现有全局 PDEC/SAE/Rankin 守门项。

2. 二点筛:
   TrueResidualCorrelation / TotalLargeIncidence
   => I3-Core 无条件化
   => 二点 secondary sieve 才能升级。

3. RH:
   逐项 referee verification controlled exits
   => 只在所有 exits 无条件闭合后才可升级终局表述。
```

这条顺序保持了目标强度的真实层级：先攻单点行/列局部反馈，再攻二点相关，最后攻 RH 矛盾场的全局解析闭合。

## 6. 下一条可写成定理的精确输入

后续最值得尝试证明的输入可以命名为：

```text
Critical Fill-Arrival Anti-Overfilling Theorem
```

一个可审查版本如下。

```text
定理输入 CF-PM-Fill:
固定 Prime Matrix 的 square-phase/off-band selector H-lower formal unit。
若 AffineTwin 阈值穿越在无限多个 P 上发生，且没有 repeated-residue/reset/ColumnCRT PDEC，
则新增 fill residue 的 Rankin 质量在对应 dyadic epoch 上形成不可求和下界。
该下界与单原子 SAE 尾和和已登记的 sparse/moving family 账本矛盾。
```

证明路线必须包含四个独立账本：

| 账本 | 需要证明 |
| --- | --- |
| arrival ledger | 每次阈值穿越至少新增一个未复用 fill residue |
| non-reuse ledger | 复用 residue 自动变成 reset/ColumnCRT PDEC |
| mass ledger | 新 residue 贡献的 Rankin/SAE 质量下界可累加 |
| critical ceiling | 临界密度反馈给出同一 epoch 内可承载的上界 |

前三项已有大量局部材料，第四项是本轮洞察带来的真正新增硬点。
若第四项能用现有 PDEC/SAE/Rankin 语言闭合，Prime Matrix 行/列证明链才可能推进到作者侧无条件候选。

## 7. 状态

本文完成的是“临界密度反馈桥”的形式化和三命题最窄义务重排。
它没有宣称完成 Prime Matrix、二点筛或 RH 的无条件证明。
当前最窄主攻点仍是：

```text
AffineTwinFillResidueArrivalBoundOrFillCatchUpMassPDECExclusion
```

下一轮若继续推进，应直接围绕 `CF-PM-Fill` 的第四项 `critical ceiling` 建立可计算/可证明不等式，而不是重新转换命题。
