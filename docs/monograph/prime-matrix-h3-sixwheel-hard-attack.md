# H3-SixWheel 最窄硬点攻坚稿

**状态：** `hard_attack_reduction_not_global_proof`

本文集中处理当前最窄接口：

```text
H3-SixWheel-Roughness
or
H3 full blocking => SAE/PDEC/ColumnCRT.
```

目标不是把有限账本误写成证明，而是把真正剩余硬点拆到最小可攻方程：若固定 `h=3` 的六轮候选被 `[5,p]` 最小素因子全部阻断，则这种全阻断必须表现为低模能量、端点持久相位或 ColumnCRT 位移缺陷。

## 1. 精确强度

设 `p<q` 为相邻奇素数，`2<=s<=q`，并令

\[
I_s=[(s-1)q+1,sq].
\]

对完整 3 对齐行 `J_R=[3R-2,3R]⊂I_s`，唯一避开 `2,3` 的候选数为

\[
c_R=
\begin{cases}
3R-2,&R\text{ odd},\\
3R-1,&R\text{ even}.
\end{cases}
\]

`H3-SWR` 断言存在完整 3 行使 `P^-(c_R)>p`。这立即推出 `I_s` 含素数：若 `s<q`，则 `c_R<q^2`；若 `s=q`，因 `q^2≡1 (mod 3)`，包含 `q^2` 的 3 行不是完整包含行，所以仍有 `c_R<q^2`。若 `c_R` 合成，则其最小素因子大于 `p`，而下一素数为 `q`，故 `c_R>=q^2`，矛盾。

因此 `H3-SWR` 是行命题的强入口。它略强于“本行含素数”，因为它舍弃至多两个边界不完整 3 行；但在递归下降中这正是获得 `h=3` 头部/尾镜像自动闭合的代价。

## 2. 为什么普通筛法不够

在 `x≈q^2` 附近，要求的窗口长度为 `q≈x^{1/2}`，筛除上界为 `z=p≈q`，于是 Buchstab/线性筛参数

\[
u={\log x\over\log z}=2+o(1).
\]

线性筛下界在 `u=2` 边界没有正余量；这正是奇偶性/半素数障碍的临界位置。换言之，直接证明每个 `q` 宽窗口含 `p`-rough 六轮候选，本质上是 Legendre 级的平方根长度素数存在问题，不能由普通无条件短区间素数定理、有限模板或单纯平均密度推出。

所以当前硬攻方向必须使用方阵/CRT 额外刚性：`q` 网格对齐、相邻壳层单点性、最小素因子分层、端点相位、列位移和 PDEC 低模能量。

## 3. 全阻断的精确方程

令

\[
\mathcal A_s=\{c_R:J_R\subset I_s\}.
\]

`H3` 失败等价于 disjoint first-factor partition：

\[
\mathcal A_s=
\bigsqcup_{5\le \ell\le p}
\mathcal A_{s,\ell},
\qquad
\mathcal A_{s,\ell}=\{n\in\mathcal A_s:P^-(n)=\ell\}.
\tag{H3-FP}
\]

对每个 `n∈A_{s,ell}`，写 `n=ell m`。则

\[
{(s-1)q\over \ell}<m\le {sq\over \ell},
\qquad
P^-(m)\ge \ell,
\qquad
m\equiv \pm \ell^{-1}\pmod 6.
\tag{H3-BD}
\]

这就是六轮全阻断的 Buchstab 下降方程。它把每个阻断点变成一个短 cofactor 窗口中的 `ell`-rough 点。

直接后果：

1. **大因子短窗不可复用。** 对固定 `ell`，命中数至多 `floor(q/ell)+1`；若 `ell>q/2`，至多 `2` 个。
2. **小因子必须承担高频覆盖。** 若大 `ell` 不足以填满 `A_s`，则小 `ell` 的同余类必须在同一 `q` 行窗口内持续高负载。
3. **全阻断不是自由覆盖。** 每个阻断同时满足 `n≡±1 (mod 6)`、`ell|n`、`P^-(n)=ell`、`n` 落在 `q` 网格行内四类约束。

## 4. 三个可攻缺陷出口

### 4.1 First-factor load

若存在素数 `ell` 使

\[
\#\mathcal A_{s,\ell}
\]

显著超过短 cofactor 窗口的 rough 上筛包络，则该 `ell` 是尾锚/固定偏移高负载。它应进入 `TailAnchor` 或 `PDEC`，而不是作为自由补洞。

### 4.2 Distributed low-mod energy

若所有 `ell` 都低负载，却仍满足 `(H3-FP)`，则必须使用大量不同 `ell`。这些 `ell` 在同一 `q` 行窗口中给出大量不同同余斜线，同时每条斜线只贡献短 cofactor 命中。把

\[
\mu_{s,\ell}(b;d)=
\#\{n\in\mathcal A_{s,\ell}:n\equiv b\pmod d\}
\]

投影到小模数 `d`。全阻断只说明 `sum_ell 1_{A_{s,ell}}=1_{A_s}`；它不说明各 first-factor 标签在所有小模数中均衡。可攻目标是证明：若全覆盖且无高负载，则标签测度的低模方差满足

\[
\sum_{d\le D}\sum_{b\bmod d}
\sum_{5\le\ell\le p}
\left|
\mu_{s,\ell}(b;d)-{1\over d}\#\mathcal A_{s,\ell}
\right|^2
\ge L_{\rm PDEC},
\tag{H3-PDEC}
\]

从而触发 PDEC/ColumnCRT。这里的能量来自 first-factor 标签分布的相位负担，而不是来自未覆盖点；物理覆盖等式本身仍为零差。

### 4.3 Endpoint / ColumnCRT

如果低模能量被端点取整抵消，则失败只能集中在有限边界相位：`I_s` 的左右端点相对于 `3`、`ell`、`q` 的相位反复相同。稀疏出现是 `SAE`；持久出现则形成固定 `q` 网格位移类，应进入 `ColumnCRT`。

## 5. 当前可证明部分

本稿内已可逐行证明：

1. `H3-SWR` 推出对应 `q` 行含素数。
2. 末行 `q^2` 不破坏固定 `h=3` 的完整行判据。
3. `H3` 失败等价于 first-factor partition `(H3-FP)`。
4. 每个 first factor `ell` 满足短窗容量上界 `floor(q/ell)+1`。
5. 因此全阻断只能是两类：少数 first factor 高负载，或大量 first factor 分布式低模同步。

第 5 项正是下一步的真实数学缺口：高负载与分布式同步必须分别接入已经建立的 `TailAnchor/PDEC/ColumnCRT/SAE` 出口，并在同一负载口径下给出阈值比较。

## 6. 下一步最小定理

当前最小可攻定理应写成：

```text
H3 Full-Blocking Defect Theorem.
Assume H3-SWR fails for a formal q-row counterexample.
Then either
  (i) a first-factor load exceeds the Tail/PDEC envelope;
  (ii) distributed first-factor coverage gives H3-PDEC low-mod energy;
  (iii) the remaining endpoint phase is sparse SAE;
  (iv) the endpoint phase is persistent ColumnCRT.
```

若此定理闭合，再结合已有 `SAE/PDEC/ColumnCRT` 排斥或证书，行命题主链才能继续升级。若这些出口尚未排除，则本链仍应诚实标记为 `Reduction-closed`，不能宣称全局无条件证明。

## 7. 近失败数据给出的结构信号

新增审计：

```text
experiments/prime_matrix_h3_full_blocking_defect_audit.py
docs/monograph/prime-matrix-h3-full-blocking-defect-audit.md/json
```

该审计在 `p<=5000` 的 `1552462` 条非第一 `q` 行中抽取 `margin<=20` 的近失败窗口，得到：

```text
near windows = 4015
near p range = 5..317
near max q = 331
near max candidate count = 110
near max blocked count = 91
near branch counts = {'aligned_p_row_contained': 255, 'seam_window': 3760}
aggregate first factors =
  5:36548, 7:20953, 11:11564, 13:8858,
  17:6153, 19:5052, 23:3738, 29:2673, ...
```

这给出三条可用洞察。

1. **真正最紧余量是低层现象。** `margin<=3` 的 `70` 个窗口全部已包含在低素数层；扩大到 `margin<=20` 后，近失败也只到 `p=317`。这说明全局大 `p` 反例若存在，不会表现为普通随机近失败，而必须维持一个异常稳定的结构相位。
2. **阻断主负载来自小首因子阶梯。** 聚合 first-factor 负载近似按 `5,7,11,13,...` 递减，小素数承担骨架覆盖，中尾素数只是补洞。若要全阻断，必须把这种小首因子骨架推到更强的固定相位负载，正适合进入 Tail/PDEC。
3. **低负载全覆盖必有相位能量。** 若禁止任何首因子高负载，则全覆盖只能使用更多中尾 first-factor。每个中尾标签在短 cofactor 窗口中贡献很少，标签数量增加会提高小模投影方差；这正是 `H3-PDEC` 的数据来源。

因此下一步不应继续枚举更大有限模板，而应尝试证明如下数据驱动二分：

```text
H3 full blocking
=> small-first-factor skeleton overload
   or many-label low-mod energy
   or endpoint persistence.
```

其中第一项进入 `Tail/PDEC`，第二项进入 `PDEC/ColumnCRT`，第三项进入 `SAE/ColumnCRT`。

## 8. 小首因子骨架包络

新增路线：

```text
docs/monograph/prime-matrix-h3-small-factor-envelope-route.md
experiments/prime_matrix_h3_small_factor_envelope_audit.py
docs/monograph/prime-matrix-h3-small-factor-envelope-audit.md/json
```

该路线给出确定性二分。对 cutoff `y`，记 `C_y` 为 `<=y` 的小首因子骨架覆盖，`R_y=A-C_y`，
`ell_+(y)` 为下一素数，`U_y=floor(q/ell_+(y))+1`。若 H3 全阻断成立，则至少需要

\[
K_y=\left\lceil {R_y\over U_y}\right\rceil
\]

个 `>y` 的中尾 first-factor 标签，除非 `C_y` 已经接近全覆盖并进入 `Tail/PDEC` 过载。
在 `p<=5000, margin<=20` 的近失败账本中，cutoff `31` 与 `43` 分别给出最大强制中尾标签数
`7` 与 `9`。因此下一步可专攻：

```text
SmallSkeletonOverload(y,K) => Tail/PDEC
or
ManyLabel(y,K_y) => H3-PDEC.
```

## 9. 全局尺度规律

新增全局尺度路线：

```text
docs/monograph/prime-matrix-h3-global-scaling-law-route.md
experiments/prime_matrix_h3_margin_growth_audit.py
docs/monograph/prime-matrix-h3-margin-growth-audit.md/json
```

增长审计显示：`p<=5000` 中，从 `p=331` 起每个素数层的最小 H3 余量都至少为 `21`；bucket
平均余量与六轮 Mertens 尺度 `#A_s prod_{5<=ell<=p}(1-1/ell)` 同阶。由此得到全局本质：
H3 全阻断不是普通局部波动，而是必须把自然增长的 `q/log q` 粗剩余尺度压为 `0`。若选择
`y=p^theta`，小骨架不过载时，包络公式强制至少约 `y/log y` 个中尾标签同步活跃；这正是
`H3-PDEC` 能量的全局来源。
