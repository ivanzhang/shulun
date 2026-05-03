# RSE 临界带硬攻：从相位抵消转为合成权质量

## 0. 结论

`RSE` 压力测试显示，真正硬点不是全部倒数指数和，而是临界带

\[
\ell\asymp hP_m,\qquad P_m=\frac XM.
\]

在该带中，倒数相位没有足够振荡；但振幅因子自动给出 `1/P` 级小量。因此剩余硬点进一步压缩为：

```text
临界带 Selberg 合成权是否有足够小的调和质量；
若没有，权重质量集中是否强迫 CRTDefect 出口。
```

这比原 `RSE` 更具体，也更适合审稿。

## 1. 临界带的精确归一化

写

\[
\Theta=\frac{hP_m}{\ell}.
\]

临界带为

\[
L^{-1}<\Theta<L,\qquad L=(\log P)^A.
\]

令 `m=Mt`，`1<=t<2`。因为 `P_m=X/M`，有

\[
\frac{hX}{\ell m}
=
\frac{hP_m}{\ell}\frac{M}{m}
=
\Theta t^{-1}.
\]

同时

\[
\frac{hH}{\ell m}
=
\Theta\frac{HM}{Xm}
=
\Theta\frac HX t^{-1}.
\]

在方阵窗口中 `H≈P`、`X≈P^2`，所以

\[
\left|1-e\left(\frac{hH}{\ell m}\right)\right|
\ll
\Theta\frac HP
\asymp
\frac{\Theta}{P}.
\]

更准确地说，

\[
1-e\left(\frac{hH}{\ell m}\right)
=
-2\pi i\Theta\frac HX t^{-1}
+
O\left(\Theta^2\frac{H^2}{X^2}\right).
\]

因此临界带中

\[
S_{h,\ell}(M)
=
-2\pi i\Theta\frac HX
\sum_{\substack{m\sim M\\P^-(m)>Y}}
\frac Mm
e\left(\Theta\frac Mm\right)
+
O\left(\frac{L^2}{P^2}N_M\right),
\]

其中

\[
N_M=\#\{m\sim M:P^-(m)>Y\}.
\]

于是点态有

\[
|S_{h,\ell}(M)|\ll \frac{L}{P}N_M.
\tag{1}
\]

这解释了压力测试中临界带 `|S|/N` 大约按 `1/P` 衰减的现象。

## 2. 为什么点态小量仍未闭合

Vaaler 系数满足 `|c_h|<<1/h`。由振幅界直接估计：

\[
\frac1h |S_{h,\ell}(M)|
\ll
\frac H{\ell}
\sum_{\substack{m\sim M\\P^-(m)>Y}}\frac1m.
\tag{2}
\]

注意 `(2)` 中的 `h` 已经抵消。将 `(2)` 放入 Selberg 合成权平均，临界带贡献受

\[
H
\sum_{\substack{m\sim M\\P^-(m)>Y}}\frac1m
\sum_{\substack{1\le h\le K\\L^{-1}<hP_m/\ell<L}}
\frac{|\omega_\ell|}{\ell}
\tag{3}
\]

控制。

而

\[
H
\sum_{\substack{m\sim M\\P^-(m)>Y}}\frac1m
\asymp
H V(Y)
\]

正是粗候选主尺度。因此临界带闭合不再是指数和点态问题，而是下面的调和质量问题：

\[
\sum_{\substack{1\le h\le K\\L^{-1}<hP_m/\ell<L}}
\frac{|\omega_\ell|}{\ell}
=o(1)
\quad\text{或至少小于可用余量。}
\tag{CWM}
\]

这里 `omega_ell` 是 Selberg 二次权

\[
\omega_\ell
=
\sum_{\substack{d_1,d_2\le R\\[d_1,d_2]=\ell}}
\lambda_{d_1}\lambda_{d_2}.
\]

## 3. 新的最小接口：CWM/CRD 二分

### 3.1 CWM：临界合成权稀薄

**CWM（Critical Weight Mass）。** 对每个 dyadic `M`，

\[
\sum_{1\le h\le K}
\sum_{\ell:\ L^{-1}<hP_m/\ell<L}
\frac{|\omega_\ell|}{\ell}
\le \eta_{\mathrm{crit}}(P),
\qquad
\eta_{\mathrm{crit}}(P)=o(1).
\]

若 `CWM` 成立，则由 `(3)` 可直接吸收临界带，`RSE-CRIT` 闭合。

### 3.2 CRD：若 CWM 失败则产生 CRTDefect

若 `CWM` 失败，则存在很多 Selberg lcm 层 `ell` 与 Vaaler 频率 `h` 满足

\[
\ell\asymp hP_m.
\]

这意味着大量小素数组合的 lcm 被压到同一个移动尺度 `P_m=X/M` 附近。回到原双曲线条带：

\[
X\le \ell a m<X+H,
\]

此时

\[
a\asymp \frac X{\ell M}\asymp \frac1h.
\]

所以临界质量集中对应“低 `a` 层 + 高 lcm 层”同步穿过同一个 dyadic 粗锚块。若这种同步在多个 `h` 上持续，圆柱相位块会在小素 CRT 投影上产生非模型集中：

```text
小素 lcm 层集中
=> 临界双曲线条带同步
=> m 的非零类投影偏离均衡
=> CRTDefect / 短窗不可复用出口。
```

因此可设第二接口：

**CRD（Critical Resonance Defect）。** 若 `CWM` 失败，则必存在辅助小素模 `r<=Y` 或短差值窗口 `|u|<L`，使临界条带诱导的 `m` 投影满足

\[
\left|
\#\{m\sim M:P^-(m)>Y,\ m\bmod r\in A\}
-
\frac{|A|}{r-1}N_M
\right|
\ge c_{\mathrm{crit}}N_M
\]

或产生同等强度的短窗不可复用能量超标。

若 `CRD` 成立，而既有 CRT 均衡/短窗不可复用账本排除该缺陷，则 `RSE-CRIT` 也闭合。

## 4. 当前最强闭合链

三段化后的链条为：

```text
RSE-OSC: 由倒数相位振荡处理；
RSE-AMP: 由振幅小量处理；
RSE-CRIT:
    CWM 成立 => 直接吸收；
    CWM 失败 => CRD => CRTDefect/短窗不可复用矛盾。
```

因此当前真正剩余不再是泛泛的 `RSE`，而是：

```text
CWM/CRD 二分。
```

## 5. 下一步可执行目标

下一步应优先做两件事。

1. **计算 Selberg 合成权临界质量。** 给定标准 Selberg 上界权，数值扫描

\[
\sum_{h,\ell:\ L^{-1}<hP_m/\ell<L}\frac{|\omega_\ell|}{\ell}
\]

随 `M,R,K,L` 的变化，判断 `CWM` 是否现实。

2. **若 CWM 不现实，转攻 CRD。** 把临界集中层按小素支撑拆成 `ell` 的 prime-support profile，证明高临界质量必然在某个小模或短差值方向产生可检测的 CRTDefect。

审稿级状态：

```text
RSE-CRIT 尚未闭合；
但最小剩余已压缩为 CWM/CRD 二分，
比原 PTA-GSL 更具体、更可测试、更可定理化。
```

## 6. CWM 模型权扫描后的修正

新增脚本：

```text
experiments/cwm_selberg_critical_mass_scan.py
```

对应输出：

```text
docs/monograph/cwm-selberg-critical-mass-scan.md
docs/monograph/cwm-selberg-critical-mass-scan.json
```

该扫描使用模型权

\[
\lambda_d=\mu(d)\frac{\log(R/d)}{\log R}
\]

合成 `omega_ell`。结论是：

- 当 `M` 接近 `P` 时，临界绝对质量很小，`CWM` 可能直接成立；
- 当 `M` 进入尾部较大 dyadic 桶，例如 `M≈P^{1.4}`，临界绝对质量不再自动趋零；
- signed mass 明显小于 absolute mass，说明 Selberg 符号相消可能是可用资源；
- 因此不能把 `CWM` 的绝对值版本作为主证明路线。

修正后的最小二分应写成：

```text
signed-CWM 成立
=> 临界带由 Selberg 符号相消吸收；

signed-CWM 失败
=> 临界 lcm 层存在同号共振质量
=> CRD
=> CRTDefect / 短窗不可复用矛盾。
```

也就是说，真正剩余硬点进一步变为：

```text
signed-CWM / CRD 二分。
```

这比绝对 `CWM` 更符合扫描结果，也避免用过强的绝对质量稀薄假设。

## 7. signed-CWM/CRD 剖面扫描

新增脚本：

```text
experiments/scwm_crd_profile_scan.py
```

对应输出：

```text
docs/monograph/scwm-crd-profile-scan.md
docs/monograph/scwm-crd-profile-scan.json
```

该扫描不再只看

\[
\sum |\omega_\ell|/\ell,
\]

而是直接计算临界带中的真实加权核

\[
\mathcal E_{\mathrm{crit}}(M)
=
\sum_{\substack{1\le h\le K\\ L^{-1}<hP_m/\ell<L}}
\frac{\omega_\ell}{h}
S_{h,\ell}(M).
\tag{4}
\]

并与绝对包络

\[
\mathcal A_{\mathrm{crit}}(M)
=
\sum_{\substack{1\le h\le K\\ L^{-1}<hP_m/\ell<L}}
\frac{|\omega_\ell|}{h}
|S_{h,\ell}(M)|
\tag{5}
\]

比较。样本结论稳定分成两类：

1. `M≈P^{1.4}` 的尾部 dyadic 桶中，

\[
\frac{|\mathcal E_{\mathrm{crit}}|}{\mathcal A_{\mathrm{crit}}}
\]

通常低于 `0.1`，说明保留 Selberg 符号与真实 RSE 核后有显著相消；

2. `M≈P` 或 `M≈P^{1.2}` 的桶中，若核相消不够，则临界质量高度集中在少数小素支撑上，例如 top prime share 常超过 `0.5`，这正是 `CRD` 的入口。

因此当前最优硬攻不应再估计绝对质量，而应证明下面的核版本二分。

## 8. 核版本最小二分

### 8.1 kernel-signed-CWM

**KSCWM（Kernel signed critical weight mass）。** 对每个 dyadic `M`，临界带贡献满足

\[
\left|
\sum_{\substack{1\le h\le K\\ L^{-1}<hP_m/\ell<L}}
\frac{\omega_\ell}{h}
S_{h,\ell}(M)
\right|
\le
\eta_{\mathrm{ks}}(P)
H
\sum_{\substack{m\sim M\\P^-(m)>Y}}\frac1m,
\tag{KSCWM}
\]

其中 `eta_ks(P)=o(1)`，或至少小于尾段余量。

若 `KSCWM` 成立，则 `RSE-CRIT` 直接闭合。注意这是有符号核估计，不是绝对值估计；它保留了 Selberg 权的交错符号和倒数相位核的实际方向。

### 8.2 KSCWM 失败的反向结构

设

\[
z_{h,\ell}
=
\frac{\omega_\ell}{h}S_{h,\ell}(M).
\]

若

\[
\left|\sum z_{h,\ell}\right|
\ge \rho\sum |z_{h,\ell}|,
\tag{6}
\]

则由初等反三角不等式，存在单位复数 `u`，使

\[
\sum |z_{h,\ell}|
\left(1-\Re(u z_{h,\ell}/|z_{h,\ell}|)\right)
\le 1-\rho.
\tag{7}
\]

特别地，至少 `1-O((1-\rho)/\delta)` 的绝对质量落在角宽 `O(\sqrt\delta)` 的同一扇区内。这说明 `KSCWM` 失败不是随机失败，而是强同向共振：

```text
Selberg 符号 + Vaaler 频率 + RSE 倒数相位
在临界带内同向排列。
```

这种同向排列是 `CRD` 的入口。

## 9. CRD 的更窄形式：小素支撑集中或短差值集中

剖面扫描显示，KSCWM 不明显时，临界质量通常集中在少数小素支撑上。正式化为：

**SPC（small-prime support concentration）。** 若 `(6)` 成立且 `KSCWM` 失败，则存在小素数 `q<=R`，使

\[
\sum_{\substack{h,\ell\ \mathrm{crit}\\ q|\ell}}
\frac{|z_{h,\ell}|}{\sum |z_{h,\ell}|}
\ge c_q.
\tag{SPC}
\]

若 `SPC` 成立，则临界条带主要来自包含 `q` 的 lcm 层。由于 `m` 是 `Y`-rough，`m` 在 `q` 的零类被硬剔除；若包含 `q` 的临界条带仍与 RSE 核同向，则其命中必须偏向某些非零类或短差值方向。由此得到更窄 `CRD`：

**CRD-SPC。** 存在 `q<=R` 和非零类集合 `A_q`，使

\[
\left|
\#\{m\sim M:P^-(m)>Y,\ m\bmod q\in A_q\}
-
\frac{|A_q|}{q-1}N_M
\right|
\ge c_{\mathrm{spc}}N_M,
\tag{CRD-SPC}
\]

或存在短差值 `|u|<L` 的同向能量超过模型上界。

这一步正好接入已有方阵/CRT 刚性账本：

- `Y`-rough 排除零类；
- 非零类在完整 CRT 周期中均衡；
- 大因子短窗不可复用排除短差值高重数；
- 圆柱斜线锁把小素支撑集中转化为相位块集中。

## 10. 当前最窄闭合链

现在 `RSE-CRIT` 的最小链条应写为：

```text
临界带
=> KSCWM 或 KSCWM 失败

KSCWM 成立
=> RSE-CRIT 吸收；

KSCWM 失败
=> 反三角同向共振
=> SPC 或短差值集中
=> CRD-SPC
=> CRTDefect / 短窗不可复用矛盾。
```

因此当前真正剩余已经从

```text
RSE-CRIT
```

压缩为两个更窄、可分别攻克的输入：

```text
(A) KSCWM：临界带有符号核相消；
(B) CRD-SPC：若无相消，则小素支撑集中推出 CRTDefect。
```

审稿状态保持诚实：

```text
KSCWM 与 CRD-SPC 均尚未逐行证明；
但它们是当前最小可审查硬点，
且已由实验明确支持为正确分叉。
```

## 11. 双出口压力扫描后的严格修正

新增脚本：

```text
experiments/kscwm_crd_dual_obstruction_scan.py
```

对应输出：

```text
docs/monograph/kscwm-crd-dual-obstruction-scan.md
docs/monograph/kscwm-crd-dual-obstruction-scan.json
```

该实验做了两个必要检查。

第一，把真实临界核分解为平滑 dyadic 模型与粗数分布误差：

\[
\mathcal E_{\mathrm{crit}}
=
\mathcal E_{\mathrm{smooth}}
+
\mathcal E_{\mathrm{rough-discrep}}.
\tag{8}
\]

第二，在 top support prime `q` 固定后，检查辅助模 `r` 上的有向残基能量：

\[
C_a(q,r)
=
\sum_{\substack{h,\ell,m\\ q|\ell,\ m\equiv a\pmod r}}
\frac{\omega_\ell}{h}
e\left(\frac{hX}{\ell m}\right)
\left(1-e\left(\frac{hH}{\ell m}\right)\right).
\tag{9}
\]

实验结论有两个关键修正：

1. 多数尾部样本中 `smooth/env` 与 `roughDiff/env` 都小，支持先证明平滑 Selberg 变换相消，再用 Buchstab/CRT 控制粗数分布误差；
2. top prime support share 偏大时，辅助模有向能量并不一定大，说明普通 `SPC` 不能单独推出 `CRD-SPC`。

因此第 9 节的 `CRD-SPC` 必须强化为“有向 SPC”。

## 12. KSCWM 的两段化

令 `U_M` 为 `m~M, P^-(m)>Y` 的粗数集合。用平滑密度模型替代 `U_M` 得

\[
\mathcal E_{\mathrm{smooth}}
=
\rho_Y
\sum_{\substack{1\le h\le K\\ \ell\ \mathrm{crit}}}
\frac{\omega_\ell}{h}
\sum_{M\le n<2M}
e\left(\frac{hX}{\ell n}\right)
\left(1-e\left(\frac{hH}{\ell n}\right)\right),
\tag{10}
\]

其中

\[
\rho_Y\approx \prod_{q\le Y}\left(1-\frac1q\right).
\]

粗数误差为

\[
\mathcal E_{\mathrm{rough-discrep}}
=
\sum_{\substack{1\le h\le K\\ \ell\ \mathrm{crit}}}
\frac{\omega_\ell}{h}
\sum_{M\le m<2M}
\left(1_{P^-(m)>Y}-\rho_Y\right)
K_{h,\ell}(m),
\tag{11}
\]

其中

\[
K_{h,\ell}(m)
=
e\left(\frac{hX}{\ell m}\right)
\left(1-e\left(\frac{hH}{\ell m}\right)\right).
\]

于是 `KSCWM` 可拆成两个更标准的输入：

**SKT（Smooth Selberg transform）。**

\[
|\mathcal E_{\mathrm{smooth}}|
\le
\eta_{\mathrm{smooth}}
H\sum_{\substack{m\sim M\\P^-(m)>Y}}\frac1m.
\tag{SKT}
\]

这只涉及平滑函数

\[
F(\theta)
=
\int_1^2 e(\theta/t)
\left(1-e(\theta H/Xt)\right)\,dt
\]

与 Selberg 合成权变换

\[
\sum_{h,\ell\ \mathrm{crit}}
\frac{\omega_\ell}{h}
F(hP_m/\ell).
\]

**RRD（Rough replacement discrepancy）。**

\[
|\mathcal E_{\mathrm{rough-discrep}}|
\le
\eta_{\mathrm{rough}}
H\sum_{\substack{m\sim M\\P^-(m)>Y}}\frac1m.
\tag{RRD}
\]

这部分才需要 Buchstab 分解、CRT 非零类均衡和短窗不可复用。实验显示 `RRD` 在代表性样本中比绝对包络小很多，因而比原始 `KSCWM` 更可攻。

因此：

```text
SKT + RRD => KSCWM。
```

## 13. CRD-SPC 的有向强化

普通 `SPC` 只说明临界 lcm 权重常含某个小素 `q`。这可能只是 Selberg 权结构本身，不必然导致真实 `m` 分布偏差。必须加入有向相位条件。

**OSPC（oriented small-prime concentration）。** 存在小素 `q`、辅助素 `r` 或短差值方向，使得 `(9)` 的有向能量满足

\[
(r-1)
\sum_{a\in(\mathbb Z/r\mathbb Z)^\times}
|C_a(q,r)|^2
\ge
(1+\delta_{\mathrm{dir}})
\mathcal A(q,r)^2.
\tag{OSPC}
\]

等价地，令

\[
E_{\rm dir}(q,r)=
\frac{
(r-1)\sum_a |C_a(q,r)|^2
}{
\mathcal A(q,r)^2
},
\]

其中 `A(q,r)` 是参与该 `q,r` 块的总绝对质量。则 `OSPC` 是 `E_dir(q,r)>=1+delta_dir`。这个归一化与实验脚本中的 `complex_energy` 一致：均匀同相分布给 `E_dir=1`，单个残基类集中给 `E_dir=r-1`。

若 `OSPC` 成立，则确实得到辅助模方向上的非模型集中。此时可以进入已有刚性：

```text
OSPC
=> 辅助模 Fourier 系数偏大
=> 非零类 CRTDefect 或短差值能量超标
=> 由 CRT 均衡 / 大因子短窗不可复用排除。
```

若只有 `SPC` 而无 `OSPC`，则不能推出 `CRD`。该点是本轮实验给出的必要修正。

## 14. 当前最终二硬点

经过修正，当前最窄硬点不是旧的 `KSCWM/CRD-SPC`，而是：

```text
(A) SKT + RRD：证明 KSCWM；
(B) OSPC => CRTDefect：证明有向小素支撑集中会触发刚性出口。
```

更精确的二分链为：

```text
临界带
=> 平滑变换相消 SKT
   + 粗数替换误差 RRD
=> KSCWM
=> RSE-CRIT 吸收；

若 KSCWM 失败
=> 反三角同向共振
=> OSPC 或平滑变换大异常
=> CRTDefect / RRD 失败出口
=> 由既有刚性排除。
```

审稿结论：

```text
普通 SPC 已被降级，不再作为充分条件；
KSCWM 需证明 SKT 与 RRD；
CRD 需证明 OSPC 到 CRTDefect。
```

## 15. SKT 平滑变换扫描与线性化

新增脚本：

```text
experiments/skt_smooth_transform_scan.py
```

对应输出：

```text
docs/monograph/skt-smooth-transform-scan.md
docs/monograph/skt-smooth-transform-scan.json
```

该实验验证 `SKT` 的主结构。令

\[
\varepsilon=\frac HX,\qquad
\theta=\frac{hP_m}{\ell}.
\]

平滑核为

\[
F(\theta,\varepsilon)
=
\int_1^2 e(\theta/t)
\left(1-e(\theta\varepsilon/t)\right)\,dt.
\]

一阶展开给

\[
F(\theta,\varepsilon)
=
-2\pi i\,\theta\varepsilon
G(\theta)
+
O(\theta^2\varepsilon^2),
\tag{12}
\]

其中

\[
G(\theta)=\int_1^2 e(\theta/t)\frac{dt}{t}.
\]

代回 `SKT` 的平滑和：

\[
M\sum_{h,\ell\ \mathrm{crit}}
\frac{\omega_\ell}{h}
F\left(\frac{hP_m}{\ell},\frac HX\right)
=
-2\pi i H
\sum_{h,\ell\ \mathrm{crit}}
\frac{\omega_\ell}{\ell}
G\left(\frac{hP_m}{\ell}\right)
+
E_{\mathrm{lin}}.
\tag{13}
\]

注意这里 `h` 在主项中完全抵消。这是关键结构：`SKT` 不是普通双变量指数和，而是 `omega_ell/ell` 对一维核 `G(hP_m/ell)` 的合成变换。

实验中 `linear_error_ratio` 通常为 `10^{-2}` 到 `10^{-4}` 量级，支持把 `SKT` 分成两段。

## 16. SKT-LIN：线性化误差

**SKT-LIN。** 对临界带 `L^{-1}<theta<L`，

\[
|E_{\mathrm{lin}}|
\le
\eta_{\mathrm{lin}}(P)
H\sum_{\substack{m\sim M\\P^-(m)>Y}}\frac1m.
\tag{SKT-LIN}
\]

由 `(12)`，有粗界

\[
|E_{\mathrm{lin}}|
\ll
M\varepsilon^2L^2
\sum_{h,\ell\ \mathrm{crit}}\frac{|\omega_\ell|}{h}.
\tag{14}
\]

在方阵尺度 `H≈P, X≈P^2` 下，

\[
M\varepsilon^2
\asymp
\frac{M}{P^2}.
\]

尾段 `M<=P^{1+\alpha}` 且 `alpha<1/2`，因此

\[
M\varepsilon^2\le P^{-1/2+o(1)}.
\]

只要 Selberg 权满足多项对数级总变差

\[
\sum_{h,\ell\ \mathrm{crit}}\frac{|\omega_\ell|}{h}
\ll (\log P)^C,
\tag{15}
\]

则 `(14)` 可吸收。`(15)` 对模型 Selberg 权是标准 divisor-bound 级估计；正式稿中应把它作为 Selberg 权账本引理逐行列出。

所以 `SKT-LIN` 是可闭合的技术项，不是主要硬点。

## 17. SKT-TRANS：真正的平滑变换相消

线性化后剩余为

\[
\mathcal T(M)
=
\sum_{h,\ell\ \mathrm{crit}}
\frac{\omega_\ell}{\ell}
G\left(\frac{hP_m}{\ell}\right).
\tag{16}
\]

**SKT-TRANS。** 证明

\[
H|\mathcal T(M)|
\le
\eta_{\mathrm{trans}}(P)
H\sum_{\substack{m\sim M\\P^-(m)>Y}}\frac1m.
\tag{SKT-TRANS}
\]

这是当前 `SKT` 的真正核心。

最直接的严写方式是 Mellin 变换。令 `Phi` 为临界带截断后的 `G`：

\[
\Phi(u)=G(u)\chi(L^{-1}<u<L).
\]

在平滑截断后，

\[
\Phi(u)
=
\frac1{2\pi i}
\int_{(\sigma)}
\widehat\Phi(s)u^{-s}\,ds.
\]

于是

\[
\mathcal T(M)
=
\frac1{2\pi i}
\int_{(\sigma)}
\widehat\Phi(s)
P_m^{-s}
\left(\sum_{1\le h\le K}h^{-s}\right)
Q(s)\,ds,
\tag{17}
\]

其中 Selberg 合成权 Dirichlet 型因子为

\[
Q(s)
=
\sum_{\ell}
\omega_\ell \ell^{s-1}
=
\sum_{d_1,d_2\le R}
\lambda_{d_1}\lambda_{d_2}
[d_1,d_2]^{s-1}.
\tag{18}
\]

因此 `SKT-TRANS` 不再是几何问题，而是下列解析账本：

```text
Mellin decay of Phi
+ Selberg quadratic form bound for Q(s)
+ short h-sum bound
=> T(M) small.
```

这给出一个可审稿的最小输入：

**SQF（Selberg quadratic form transform bound）。**

\[
\int_{|\Im s|\le T}
|\widehat\Phi(s)|
|P_m^{-s}|
\left|\sum_{h\le K}h^{-s}\right|
|Q(s)|\,|ds|
\le
\eta_{\mathrm{trans}}(P)
\sum_{\substack{m\sim M\\P^-(m)>Y}}\frac1m.
\tag{SQF}
\]

若 `SQF` 成立，则 `SKT-TRANS` 成立。

当前状态：

```text
SKT-LIN: 可由 Taylor 余项 + Selberg 总变差账本闭合；
SKT-TRANS: 已压缩为 SQF；
SQF: 尚需逐行证明或精确引用外部 Selberg 二次型估计。
```

## 18. SQF Mellin 预算扫描

新增脚本：

```text
experiments/sqf_quadratic_form_scan.py
```

对应输出：

```text
docs/monograph/sqf-quadratic-form-scan.md
docs/monograph/sqf-quadratic-form-scan.json
```

该扫描数值近似

\[
\int |\widehat\Phi(it)|\,|H(it)|\,|Q(it)|\,dt,
\qquad
H(it)=\sum_{h\le K}h^{-it},
\]

并与平凡预算

\[
\int |\widehat\Phi(it)|\,K
\sum_\ell\frac{|\omega_\ell|}{\ell}\,dt
\]

比较。样本稳定显示：

- `budget/trivial` 约为 `0.15--0.20`，已有固定节省；
- `Q(0)/sum|omega|/ell` 约为 `0.10--0.18`，低频 Selberg 二次型相消很强；
- 最大 integrand 出现在 `|t|≈1` 的低频区，说明主要硬点不是高频；
- `H(it)` 在最坏点的节省有限，核心应优先攻 `Q(it)` 的低频二次型界。

因此 `SQF` 不应先走高频大筛式路线，而应拆为：

```text
SQF-QLOW: 低频 Q(it) / sum|omega|/ell 有固定节省；
SQF-PHI: 平滑截断给 Phihat 快速衰减，截断高频；
SQF-H: h-sum 在中高频给平均节省。
```

## 19. Q(s) 的精确二次型分解

对

\[
Q(s)=
\sum_{d_1,d_2\le R}
\lambda_{d_1}\lambda_{d_2}
[d_1,d_2]^{s-1},
\]

令 `s=it`。因为

\[
[d_1,d_2]^{it-1}
=
(d_1d_2)^{it-1}
(d_1,d_2)^{1-it},
\]

并且对任意 `z` 有 Jordan 卷积恒等式

\[
n^z=\sum_{r|n}J_z(r),
\qquad
J_z=\mu * \mathrm{id}_z,
\]

得到精确展开

\[
Q(it)
=
\sum_{r\le R}
J_{1-it}(r)
\left(
\sum_{\substack{d\le R\\r|d}}
\lambda_d d^{it-1}
\right)^2.
\tag{19}
\]

特别地，当 `t=0` 时，

\[
Q(0)
=
\sum_{r\le R}\varphi(r)
\left(
\sum_{\substack{d\le R\\r|d}}
\frac{\lambda_d}{d}
\right)^2
\ge 0.
\tag{20}
\]

这解释了低频相消不是偶然符号抵消，而是 Selberg 权通过最小化正二次型实现的结构性节省。

## 20. SQF-QLOW：低频二次型界

由扫描结果，最关键的可审稿命题是：

**SQF-QLOW。** 对 `|t|<=T_0`，例如 `T_0=(log P)^B` 的低频主区，有

\[
|Q(it)|
\le
\eta_Q(P)
\sum_\ell\frac{|\omega_\ell|}{\ell},
\tag{SQF-QLOW}
\]

其中 `eta_Q(P)` 至少有固定小于 `1` 的节省；若要渐近闭合，则需 `eta_Q(P)` 与 `RRD/OSPC` 余量共同小于尾段余量。

可行证明路线：

1. 用 `(19)` 把 `Q(it)` 化为 `r` 上的 Selberg 二次型；
2. 对低频 `|t|<=T_0`，展开

\[
d^{it}=1+O(|t|\log d)
\]

或使用平滑 Lipschitz 控制，把 `Q(it)` 约化到 `Q(0)` 加可控扰动；
3. 用 Selberg 权的极小性质给

\[
Q(0)\ll \frac1{\log R}
\quad\text{相对于}\quad
\sum_\ell |\omega_\ell|/\ell;
\]

4. 将扰动限制到 `T_0` 主区，由 `\widehat\Phi` 权重吸收。

这一命题是当前 SQF 的核心。

## 21. SQF-PHI：高频衰减

若把临界截断 `chi(L^{-1}<u<L)` 换成 `C^\infty` 截断，则对任意 `A`，

\[
|\widehat\Phi(it)|
\ll_A
(1+|t|)^{-A}(\log L)^{C_A}
\sup_{0\le j\le A}
\left\|(u\partial_u)^jG(u)\right\|_\infty.
\tag{SQF-PHI}
\]

由于

\[
G(u)=\int_1^2 e(u/t)\frac{dt}{t},
\]

在 `u∈[L^{-1},L]` 上的对数导数至多给出 `L^{O(A)}`，而 `L=(log P)^B`，故高频段可由取 `A` 足够大吸收。该项是标准平滑 Mellin 衰减，不是核心硬点。

## 22. SQF-H：短 h-sum 中高频节省

对

\[
H(it)=\sum_{h\le K}h^{-it},
\]

低频 `|t|<=1` 没有明显节省；扫描中最坏点也在该区附近。因此 `SQF-H` 只应作为中高频辅助：

\[
\int_{|t|>T_1}
|\widehat\Phi(it)|\,|H(it)|\,|Q(it)|\,dt
\]

用二阶均值或 van der Corput 型界处理。正式证明中不应依赖 `H(it)` 解决低频主项。

## 23. SQF 的当前最窄接口

当前 `SQF` 已压缩为：

```text
SQF-QLOW: 低频 Q(it) 二次型节省；
SQF-PHI: 平滑 Mellin 高频衰减；
SQF-H: h-sum 中高频平均节省。
```

其中：

```text
SQF-PHI 与 SQF-H 是标准解析账本；
SQF-QLOW 是当前最后硬核。
```

换言之，整个尾段临界带当前最窄剩余链条为：

```text
SQF-QLOW
+ SQF-PHI
+ SQF-H
=> SQF
=> SKT-TRANS
=> SKT
=> KSCWM
=> RSE-CRIT。
```

审稿状态：

```text
SQF-QLOW 尚未逐行证明；
但它已是当前最具体、最可审查的单一硬点。
```

## 24. QLOW 最优 Selberg 权扫描

新增脚本：

```text
experiments/sqf_qlow_optimal_weight_scan.py
```

对应输出：

```text
docs/monograph/sqf-qlow-optimal-weight-scan.md
docs/monograph/sqf-qlow-optimal-weight-scan.json
```

该实验比较两类权：

1. 标准对数模型权

\[
\lambda_d^{std}=\mu(d)\frac{\log(R/d)}{\log R};
\]

2. 精确最小化

\[
Q(0)=\sum_{d,e\le R}\frac{\lambda_d\lambda_e}{[d,e]},
\qquad \lambda_1=1
\tag{21}
\]

的 Selberg 极小权。

写

\[
A_{d,e}=\frac1{[d,e]},\qquad e_1=(1,0,\ldots,0).
\]

则最优权为

\[
\lambda^{opt}
=
\frac{A^{-1}e_1}{e_1^TA^{-1}e_1},
\tag{22}
\]

且

\[
Q_{opt}(0)=\frac1{e_1^TA^{-1}e_1}.
\tag{23}
\]

扫描结果稳定显示：

- `Q0/abs` 从标准权的约 `0.10--0.18` 降到约 `0.07--0.12`；
- Mellin 预算比 `budget/trivial` 同步下降；
- `lambda_l1` 只增加约 `1.6--1.9` 倍，没有出现爆炸。

这说明当前最优路线不是继续使用标准对数权，而是把 `PTA-GSL` 中的 Selberg 上界筛权改为低频优化权。

## 25. SQF-QLOW 的三段化

`SQF-QLOW` 现在应拆成三个可审稿输入。

### 25.1 QLOW-OPT：零频极小化

**QLOW-OPT。** 取 `(22)` 的 Selberg 极小权，则

\[
Q(0)
\le
\frac{C}{\log R}
\tag{QLOW-OPT}
\]

并且相对于总变差

\[
\mathcal V_\omega
=
\sum_\ell\frac{|\omega_\ell|}{\ell}
\]

有固定节省

\[
\frac{Q(0)}{\mathcal V_\omega}
\le \eta_0<1.
\tag{24}
\]

其中 `(QLOW-OPT)` 是标准 Selberg 筛二次型极小性质；正式稿中应以矩阵公式 `(22)` 或传统 Selberg `G` 函数公式证明。

### 25.2 QLOW-STAB：低频稳定

**QLOW-STAB。** 对低频主区 `|t|<=T_0`，

\[
|Q(it)-Q(0)|
\le
\eta_{\mathrm{stab}}(T_0,R)\,\mathcal V_\omega.
\tag{QLOW-STAB}
\]

若只用粗 Lipschitz，

\[
|Q(it)-Q(0)|
\le
|t|\sum_\ell\frac{|\omega_\ell|\log\ell}{\ell},
\]

则只能处理 `|t|<<1/log R`。因此低频应再细分为：

```text
ultra-low: |t| <= c/log R，用 Lipschitz 稳定；
fixed-low: c/log R < |t| <= T0，用 Euler-product/oscillatory local factor 控制。
```

这一步是 `SQF-QLOW` 中最敏感的部分：不能把 `d^{it}=1+O(t log d)` 用到 `t≈1` 而不付出过大损失。

### 25.3 QLOW-VAR：变差账本不爆炸

**QLOW-VAR。** 低频优化权仍满足

\[
\sum_{d\le R}|\lambda_d|
\le
(\log R)^C,
\qquad
\sum_\ell\frac{|\omega_\ell|}{\ell}
\le
(\log R)^C,
\tag{QLOW-VAR}
\]

并且不会破坏 `RRD` 和 `OSPC` 中对 Selberg 权总变差的吸收。实验中 `lambda_l1` 只增加常数倍，支持该账本。

## 26. 当前最后硬核的再定位

经过最优权扫描，当前最后硬核已从泛泛的 `SQF-QLOW` 变为：

```text
QLOW-STAB fixed-low 段：
c/log R < |t| <= T0 时，
优化 Selberg 二次型 Q(it) 仍相对 V_omega 有足够节省。
```

`QLOW-OPT` 处理 `t=0`，`QLOW-VAR` 是账本项；真正要硬攻的是 `fixed-low` 频带。

最有希望的证明路线是 Euler-product 局部因子：

```text
Q(it)
≈ smoothed truncated product of (1-p^{-1+it})
with optimized Selberg cutoff
```

当 `|t|>>1/log R` 时，局部相位 `t log p` 开始产生欧拉乘积振荡；这应给出相对总变差的固定节省。正式证明需要把 `(22)` 的有限维极小权与传统 Selberg `G` 函数/欧拉乘积渐近连接起来。

当前最窄接口因此更新为：

```text
QLOW-OPT + QLOW-STAB + QLOW-VAR
=> SQF-QLOW。
```

其中：

```text
QLOW-STAB fixed-low 是当前最后单点硬核。
```

## 27. fixed-low 归一化频率扫描后的修正

新增脚本：

```text
experiments/sqf_qlow_fixed_low_stability_scan.py
```

对应输出：

```text
docs/monograph/sqf-qlow-fixed-low-stability-scan.md
docs/monograph/sqf-qlow-fixed-low-stability-scan.json
```

扫描归一化频率

\[
u=t\log R.
\]

结论比上一节预期更精确：

- `0<=u<=1/2` 中，`Q(iu/log R)/V_omega` 与 `Q(0)/V_omega` 接近；
- `1/2<u<=2` 中，比例仍很低，样本约 `0.13--0.24`；
- `u>2` 后未加权的 `Q` 会反弹，样本峰值可到 `0.5--0.7`；
- 因此不能把 `u>2` 的区间仅靠 `Q` 自身振荡处理，必须保留 `Phihat` 衰减与 `h`-sum 共同预算。

这修正了“`u>2` 单靠 Euler 局部振荡下降”的过强说法。

## 28. 最后硬核的正确三段

`QLOW-STAB` 应拆成：

### 28.1 QLOW-ULTRA

\[
0\le u\le\frac12.
\]

用矩阵扰动或 Lipschitz：

\[
|Q(iu/\log R)-Q(0)|
\ll u\,\mathcal V_\omega.
\]

因 `u<=1/2` 且 `Q(0)` 已由极小化压低，此段可闭合。

### 28.2 QLOW-TRANS

\[
\frac12<u\le2.
\]

这是有限宽过渡带。实验显示此带仍有强节省；证明上可采用紧区间最大值策略：

1. 将 `Q(iu/log R)` 视为由有限 Euler/Selberg 局部因子给出的解析函数；
2. 用 Bernstein/Markov 型导数界把连续区间化为网格；
3. 在网格上用 Selberg 极小权的二次型表示给出统一界。

该段是可以有限参数化证明的，不再是主要硬核。

### 28.3 QLOW-MID：带权中频峰

\[
u>2.
\]

未加权 `Q` 可能反弹，因此真正需要证明的是带权版本：

\[
\int_{u>2}
|\widehat\Phi(iu/\log R)|
|H(iu/\log R)|
|Q(iu/\log R)|
\frac{du}{\log R}
\]

可被

\[
\eta_{\mathrm{mid}}\mathcal V_\omega
\]

吸收。这里节省来自三者共同作用：

```text
Q 的固定节省
+ Phihat 的 Mellin 衰减
+ H 的中频平均节省。
```

因此最后单点硬核不再是裸 `QLOW-STAB fixed-low`，而是：

```text
QLOW-MID weighted absorption:
u>2 的中频峰必须被 Phihat/H 加权吸收。
```

## 29. 当前最终单点硬核

最终链条更新为：

```text
QLOW-OPT
+ QLOW-ULTRA
+ QLOW-TRANS
+ QLOW-MID
+ QLOW-VAR
=> SQF-QLOW。
```

其中：

```text
QLOW-OPT: 标准 Selberg 极小化；
QLOW-ULTRA: Lipschitz 矩阵扰动；
QLOW-TRANS: 有限宽稳定；
QLOW-VAR: 变差账本；
QLOW-MID: 当前最后硬核。
```

审稿级诚实结论：

```text
最后硬核已从 fixed-low 全段缩为带权中频峰 QLOW-MID；
不能再声称裸 Q(it) 在 u>2 单调下降；
必须证明 Phihat/H/Q 的联合带权吸收。
```

## 30. QLOW-MID 带权吸收扫描

新增脚本：

```text
experiments/sqf_qlow_mid_weighted_absorption_scan.py
```

对应输出：

```text
docs/monograph/sqf-qlow-mid-weighted-absorption-scan.md
docs/monograph/sqf-qlow-mid-weighted-absorption-scan.json
```

该实验直接扫描

\[
\int_{u>2}
|\widehat\Phi(iu/\log R)|
|H(iu/\log R)|
|Q(iu/\log R)|
\frac{du}{\log R}.
\tag{25}
\]

关键发现：

- 虽然裸 `Q` 在 `u>2` 可反弹，但带权总比值 `midRatio` 稳定在约 `0.135--0.151`；
- 主要中频段 `2<u<=6` 的局部比值最高，样本约 `0.21--0.26`；
- `6<u<=12` 已明显下降，样本约 `0.17--0.19`；
- `u>12` 的尾部由 `Phihat` 与 `H` 共同压低，局部比值多在 `0.07--0.10`；
- 因此 `QLOW-MID` 不应再作为无限频带硬点，而应压缩成有限紧区间常数不等式。

## 31. QLOW-MID 的最终压缩

取一个固定常数 `U0`，例如 `U0=12`。把中频峰拆成：

### 31.1 QLOW-MID-COMP

\[
2<u\le U_0.
\]

证明显式常数界

\[
\int_{2<u\le U_0}
|\widehat\Phi(iu/\log R)|
|H(iu/\log R)|
|Q(iu/\log R)|
\frac{du}{\log R}
\le
C_{\mathrm{comp}}
\mathcal V_\omega
\int_{2<u\le U_0}
|\widehat\Phi(iu/\log R)|K\frac{du}{\log R},
\tag{QLOW-MID-COMP}
\]

其中目标是 `C_comp<0.30`，更保守可先取 `C_comp<0.35`。实验样本最大约 `0.257`，有常数余量。

这是一个紧区间问题，可以用审稿级有限覆盖证明：

1. 将 `u∈[2,U0]` 分成小区间；
2. 对 `Q(iu/logR)` 使用导数界

\[
\left|\frac{d}{du}Q(iu/\log R)\right|
\le
\frac1{\log R}
\sum_\ell \frac{|\omega_\ell|\log\ell}{\ell}
\ll \mathcal V_\omega;
\]

3. 对 `H` 和 `Phihat` 同样给出导数界；
4. 网格点用 Selberg 二次型公式和显式常数计算/证明；
5. 区间间隙由导数界补齐。

这不是“有限模板控制无限 P”：`u` 是归一化连续频率，区间固定；`P` 的影响进入可显式控制的导数常数和 Selberg 权账本。

### 31.2 QLOW-MID-TAIL

\[
u>U_0.
\]

若 `Phi` 使用 `C^\infty` 平滑截断，则对任意 `A`，

\[
|\widehat\Phi(iu/\log R)|
\ll_A
(1+u/\log R)^{-A}(\log L)^{C_A}.
\]

配合

\[
|H(it)|\le K,\qquad |Q(it)|\le \mathcal V_\omega
\]

得到

\[
\int_{u>U_0}
|\widehat\Phi(iu/\log R)|
|H(iu/\log R)|
|Q(iu/\log R)|
\frac{du}{\log R}
\le
C_A U_0^{1-A}K\mathcal V_\omega.
\tag{QLOW-MID-TAIL}
\]

取 `A` 与 `U0` 固定足够大即可吸收。实验中即使 sharp-ish 截断，`u>12` 也已明显小；平滑截断只会更稳。

## 32. 当前最后单点硬核

`QLOW-MID` 现已压缩为：

```text
QLOW-MID-COMP + QLOW-MID-TAIL。
```

其中：

```text
QLOW-MID-TAIL: 标准平滑 Mellin 衰减；
QLOW-MID-COMP: 当前最后单点硬核。
```

最终剩余单点变成：

```text
在固定紧区间 2<u<=U0 上，
证明 Phihat/H/Q 的显式带权常数界 C_comp<可用余量。
```

这已经是一个有限维、可审稿、可常数化的解析不等式，而不是原来的全局短区间筛余难题。

## 33. QLOW-MID-COMP 的紧区间证书化

新增证书脚本：

```text
experiments/qlow_mid_comp_grid_certificate.py
```

对应输出：

```text
docs/monograph/qlow-mid-comp-grid-certificate.md
docs/monograph/qlow-mid-comp-grid-certificate.json
```

### 33.1 归一化硬核函数

在固定紧区间 `2<u<=12` 上定义

\[
\rho_R(u)
=
\frac{|H(iu/\log R)|}{K}
\frac{|Q(iu/\log R)|}{\mathcal V_\omega}.
\tag{33.1}
\]

则 `QLOW-MID-COMP` 等价于证明

\[
\frac{
\int_2^{12}|\widehat\Phi(iu/\log R)|\,|H(iu/\log R)|\,|Q(iu/\log R)|\,du/\log R
}{
K\mathcal V_\omega
\int_2^{12}|\widehat\Phi(iu/\log R)|\,du/\log R
}
\le C_{\rm comp}.
\tag{33.2}
\]

这里必须保留 `|\widehat\Phi|` 的真实权重；若改用
`sup rho`，会丢失中频峰附近的主要余量。

### 33.2 导数余量

对任一小区间 `I`，设中点为 `m_I`。由

\[
\left|\frac{d}{du}\frac{|H(iu/\log R)|}{K}\right|
\le
\frac{\log(K!)}{K\log R},
\tag{33.3}
\]

以及

\[
\left|\frac{d}{du}\frac{|Q(iu/\log R)|}{\mathcal V_\omega}\right|
\le
\frac{
\sum_\ell |\omega_\ell|\log\ell/\ell
}{
\mathcal V_\omega\log R
},
\tag{33.4}
\]

得到

\[
\rho_R(u)
\le
\rho_R(m_I)
\;+\;
\frac{|I|}{2}
\left(
\frac{\log(K!)}{K\log R}
+
\frac{
\sum_\ell |\omega_\ell|\log\ell/\ell
}{
\mathcal V_\omega\log R
}
\right).
\tag{33.5}
\]

把 (33.5) 乘以非负权 `|\widehat\Phi(iu/\log R)|` 并在各小区间求和，得

\[
\operatorname{Avg}_{|\widehat\Phi|}(\rho_R)
\le
\operatorname{GridAvg}_{|\widehat\Phi|}(\rho_R)
+
\operatorname{LipMargin}.
\tag{33.6}
\]

因此只需在固定紧区间上给出外向舍入网格表，即可把连续积分界化为有限个显式常数检查。

### 33.3 当前证书读数

默认参数 `U0=12, K=8, step=0.02, target=0.35` 下，证书读数为：

```text
P=2003, R=P^0.30: certified=0.232696
P=2003, R=P^0.35: certified=0.221604
P=5003, R=P^0.30: certified=0.226291
P=5003, R=P^0.35: certified=0.216654
P=10007, R=P^0.30: certified=0.220040
P=10007, R=P^0.35: certified=0.208588
```

这说明最后单点硬核的真实规模约为 `0.21--0.23`，而不是接近 `0.35` 的临界状态；主要贡献来自 `u≈2--3` 的低中频入口，最大逐点峰反而不是带权积分瓶颈。

### 33.4 审稿级闭合义务

当前进展可以严格表述为：

```text
RSE 临界带已压缩到一个固定紧区间带权常数证书。
```

但它还不是完整无条件闭合。剩余义务只有两项：

1. 将 `Phihat/H/Q` 的浮点网格值替换为有理区间外向舍入；
2. 将 Selberg 最优权的 `V_omega` 与对数矩常数在 `P>=P0` 上统一显式化。

完成这两项后，`QLOW-MID-COMP` 可作为常数引理接入
`QLOW-MID-COMP + RRD + OSPC` 主链。

关键点是：这里不再用有限模板控制无限素数情形。频率区间固定，`P` 的全部影响只进入
`logR`、Selberg 权矩和导数账本；这些量可以由显式解析估计或区间证书统一控制。

## 34. QLOW-MID-COMP 外向舍入预算

新增预算脚本：

```text
experiments/qlow_mid_comp_interval_budget.py
```

对应输出：

```text
docs/monograph/qlow-mid-comp-interval-budget.md
docs/monograph/qlow-mid-comp-interval-budget.json
```

该预算表把上一节的浮点网格证书转化为区间化证明的误差容许量。目标形式是

\[
C_{\rm grid}+C_{\rm Lip}+C_{\rm interval}<C_{\rm target},
\qquad C_{\rm target}=0.35.
\tag{34.1}
\]

当前最紧样本仍是 `P=2003, R=9`。其读数为

```text
certified=0.232696,
rawSlack=0.117304.
```

若预留总外向舍入误差

\[
C_{\rm interval}\le 0.065,
\tag{34.2}
\]

则所有样本仍满足目标界；最紧样本扣除预算后仍有

```text
postBudgetSlack=0.052304.
```

预算拆分为：

| 误差来源 | 预算 |
| --- | ---: |
| `Phihat` Mellin/求积外向误差 | `0.022750` |
| `sin/cos/log` 有理区间包络 | `0.016250` |
| Selberg 权线性系统与 `V_omega` | `0.013000` |
| 网格端点与加权平均替换 | `0.007800` |
| 十进制导出与表格抄录 | `0.005200` |

因此 `QLOW-MID-COMP` 的下一步严格化不再需要寻找新的结构刚性，而是需要构造三个可审稿 oracle：

1. `Phihat` 的 Mellin/求积外向区间；
2. `H/Q` 中 `sin/cos/log` 的有理区间包络；
3. Selberg 最优权、合成权 `omega` 与 `V_omega` 的区间线性代数。

本地环境当前没有区间三角函数库，因此本节仍是预算证书，不是形式区间证明。它的价值在于：正式区间证明只要把总外向误差控制在 `0.065` 内，现有 `C_comp<0.35` 余量仍然成立。

## 35. Selberg 权线性代数的有理审计

新增审计脚本：

```text
experiments/selberg_rational_weight_audit.py
```

对应输出：

```text
docs/monograph/selberg-rational-weight-audit.md
docs/monograph/selberg-rational-weight-audit.json
```

该审计把 `QLOW-MID-COMP` 中的 Selberg 最优权求解从浮点线性代数改为有理精确消元。对矩阵

\[
A_{d,e}=\frac1{[d,e]},\qquad d,e\le R,\quad d,e\ {\rm squarefree},
\tag{35.1}
\]

精确求解约束 `\lambda_1=1` 下的最小二次型，并验证

\[
A\lambda=q_0e_1,\qquad \lambda_1=1,\qquad
q_0=\sum_\ell\frac{\omega_\ell}{\ell}.
\tag{35.2}
\]

当前样本全部满足有理残差为零：

```text
P=2003, R=9,  size=6,  exact normal eq=Y
P=2003, R=14, size=10, exact normal eq=Y
P=5003, R=12, size=8,  exact normal eq=Y
P=5003, R=19, size=13, exact normal eq=Y
P=10007,R=15, size=11, exact normal eq=Y
P=10007,R=25, size=16, exact normal eq=Y
```

因此预算项

```text
selberg_weight_solver = 0.013
```

在这些样本上不再表示浮点消元风险，而应改解释为：

1. 从有限样本到 `P>=P0` 的统一 `\mathcal V_\omega` 与对数矩常数；
2. `\sum_\ell |\omega_\ell|\log\ell/\ell` 中 `log` 的区间 oracle；
3. 正式稿表格抄录和外向输出误差。

这一步移除了 `QLOW-MID-COMP` 中最容易被审稿质疑的数值线性代数黑箱。剩余真正区间化硬点现在集中到 `Phihat` 的 Mellin/求积外向误差与 `sin/cos/log` 的有理区间包络。

## 36. sin/cos/log 有理区间 oracle

新增审计脚本：

```text
experiments/trig_log_interval_oracle_audit.py
```

对应输出：

```text
docs/monograph/trig-log-interval-oracle-audit.md
docs/monograph/trig-log-interval-oracle-audit.json
```

该审计不依赖外部区间库，完全使用有理级数：

1. 对 `log n`，将 `n=2^k y`, `1<=y<2`，用

\[
\log y
=
2\sum_{j<N}\frac{z^{2j+1}}{2j+1}
+
O\!\left(
\frac{2z^{2N+1}}{(2N+1)(1-z^2)}
\right),
\qquad
z=\frac{y-1}{y+1}.
\tag{36.1}
\]

2. 对 `pi`，用 Machin 公式

\[
\pi=16\arctan(1/5)-4\arctan(1/239)
\tag{36.2}
\]

及交错级数余项。

3. 对 `sin/cos`，先用 `2pi` 区间做范围归约，再在 `|x|<=pi` 上用 Taylor 尾项给统一半径。

默认参数

```text
log_terms=80, pi_terms=80, taylor_degree=70
```

给出当前全部样本三角/对数调用的最大半径

```text
oracle_half_radius <= 2.333e-67.
```

该半径远小于预算表中的

```text
trig_log_interval_oracle = 0.016250.
```

因此 `sin/cos/log` 外向包络本身已不是常数余量瓶颈。剩余工作是把该 oracle 逐点接入复数区间版 `H(iu/logR)` 与 `Q(iu/logR)`，并重算 `C_comp` 表。

至此，`QLOW-MID-COMP` 的区间化义务已进一步缩小为：

```text
Phihat Mellin/求积外向区间
+ 复数区间版 H/Q 重算
+ P>=P0 统一 Selberg 矩常数。
```

## 37. H/Q 复数区间增量审计

新增审计脚本：

```text
experiments/qlow_mid_comp_hq_interval_audit.py
```

对应输出：

```text
docs/monograph/qlow-mid-comp-hq-interval-audit.md
docs/monograph/qlow-mid-comp-hq-interval-audit.json
```

该审计把上一节的 trig/log oracle 半径接入

\[
\rho_R(u)=\frac{|H(iu/\log R)|}{K}
\frac{|Q(iu/\log R)|}{\mathcal V_\omega}.
\tag{37.1}
\]

若每个 `sin/cos` 坐标外向半径为 `\varepsilon`，则单位复指数项的复平面误差至多

\[
\delta=\sqrt2\,\varepsilon.
\tag{37.2}
\]

由于

\[
\frac{|H|}{K}\le 1,\qquad
\frac{|Q|}{\mathcal V_\omega}\le 1,
\tag{37.3}
\]

归一化乘积的增量满足

\[
\Delta_{HQ}\le 2\delta+\delta^2.
\tag{37.4}
\]

使用 `oracle_half_radius<=2.333e-67` 得到

```text
complex term radius <= 3.300e-67,
H/Q rho margin <= 6.600e-67.
```

该增量对 `C_comp` 的影响远低于预算，样本最小余量仍为 `0.117304`。因此 H/Q 的三角与对数外向误差已在样本证书层面闭合。

更新后的最小剩余为：

```text
Phihat Mellin/求积外向区间
+ P>=P0 统一 Selberg 矩常数
+ RRD/OSPC 主链接口。
```

## 38. Phihat-free 的 sup-rho 旁路

继续审查发现，`QLOW-MID-COMP` 的紧区间证明可以完全绕开 `Phihat` 数值求积。

新增审计脚本：

```text
experiments/qlow_mid_comp_supnorm_audit.py
```

对应输出：

```text
docs/monograph/qlow-mid-comp-supnorm-audit.md
docs/monograph/qlow-mid-comp-supnorm-audit.json
```

核心观察是：在 `2<u<=12` 上，若能直接证明

\[
\rho_R(u)=
\frac{|H(iu/\log R)|}{K}
\frac{|Q(iu/\log R)|}{\mathcal V_\omega}
<0.35,
\tag{38.1}
\]

则对任意非负权 `|\widehat\Phi|` 都有

\[
\frac{
\int_2^{12}|\widehat\Phi|\,|H|\,|Q|\,du/\log R
}{
K\mathcal V_\omega
\int_2^{12}|\widehat\Phi|\,du/\log R
}
\le
\sup_{2<u\le12}\rho_R(u)
<0.35.
\tag{38.2}
\]

因此 `QLOW-MID-COMP` 不必证明 `Phihat` 的 Mellin/求积外向区间。

审计把四项相加：

```text
maxRhoGrid + LipschitzMargin + HQIntervalMargin + DecimalMargin.
```

当前最紧样本为：

```text
P=2003, R=9:
maxRho=0.281688,
Lip=0.009742,
H/Q=6.600e-67,
Decimal=0.005200,
supBound=0.296630,
slack=0.053370.
```

全部样本均满足 `supBound<0.35`。这比带权平均证书更粗，但审稿上更稳：它消除了紧区间常数界对 `Phihat` 数值外向舍入的依赖。

于是 `QLOW-MID-COMP` 的剩余数值义务进一步压缩为：

```text
H/Q 网格值的正式区间重算
+ P>=P0 统一 Selberg 矩常数。
```

其中 H/Q 的 trig/log oracle、Lipschitz 和十进制预算已经给出足够余量；真正全局化剩余是 `P>=P0` 统一 Selberg 矩常数。主链层面仍有 `RRD/OSPC`。

## 39. RRD/OSPC 主链余量账本

上一节给出 `QLOW-MID-COMP` 的 Phihat-free `sup-rho` 旁路后，最紧样本为

```text
P=2003, R=9:
supBound=0.29663049024172705,
target=0.35,
available_margin=0.053369509758272926.
```

新增账本脚本：

```text
experiments/rse_rrd_ospc_margin_ledger.py
```

对应输出：

```text
docs/monograph/rse-rrd-ospc-margin-ledger.md
docs/monograph/rse-rrd-ospc-margin-ledger.json
```

该账本的作用不是证明 `RRD/OSPC`，而是把主链剩余项放进同一归一化 convention。所有误差必须先换算到 `QLOW-MID-COMP` 的 `target=0.35` 损失尺度，才能使用下表余量：

| 接口 | 预算目标 | 当前证明义务 |
| --- | ---: | --- |
| `RRD` | `C_RRD<=0.020` | 证明粗数替换误差在同权 `K V_omega` 尺度下不超过该值。 |
| `OSPC` | `C_OSPC<=0.020` | 证明有向小素集中必触发 `CRTDefect/Tail-anchor`，且 Fourier 到缺陷出口的损失不超过该值。 |
| `SelbergUniform` | `C_SelbergUniform<=0.008` | 把样本 Selberg 有理矩阵审计升级为 `P>=P0` 的统一矩常数。 |
| `LedgerRounding` | `C_round<=0.003` | 统一 H/Q、Selberg 变差、RSE 核与 RRD/OSPC 的换算误差。 |

因此当前可审查闭合判据被明确压缩为

\[
C_{\rm RRD}+C_{\rm OSPC}+C_{\rm SelbergUniform}+C_{\rm round}
<0.053369509758272926.
\tag{39.1}
\]

按账本目标，四项预算和为 `0.051`，保留约 `0.0023695` 的余量。审稿边界必须保持清楚：`QLOW-MID-COMP` 的样本余量已经量化；但 `RRD`、`OSPC` 与 `P>=P0` 统一 Selberg 矩常数仍是主链剩余证明义务。下一步最小硬点应先攻 `RRD` 的同权归一化，因为它是标量替换误差；随后攻 `OSPC` 的有向 Fourier 到 `CRTDefect` 定量出口。

## 40. RRD 同权归一化与两段式拆解

继续审查 `RRD` 后，新增脚本：

```text
experiments/rse_rrd_same_weight_reduction.py
```

对应输出：

```text
docs/monograph/rse-rrd-same-weight-reduction.md
docs/monograph/rse-rrd-same-weight-reduction.json
```

该审查首先确认一个负面但关键的事实：旧的“一步常数密度替换”不能直接证明 `C_RRD<=0.020`。在 `kscwm-crd-dual-obstruction-scan` 的旧压力样本中，

```text
max roughDiff/env = 0.2000018136297129,
median roughDiff/env = 0.033779147536475755.
```

其中最坏样本为 `P=5003, M=P^1.2, R=P^0.3`。按 `M` 层分组，旧样本显示 `M=P^1.4` 层已接近或低于 `0.020`，真正困难集中在较短粗锚层 `M=P^1.2`。因此后续不能继续把 `RRD` 当作单密度随机误差处理。

本轮正向推进是同权归一化恒等式。对

\[
K_{h,\ell}(m)
=e\left({hX\over \ell m}\right)
\left(1-e\left({hH\over \ell m}\right)\right),
\]

在 `m~M` 且 `hH/(\ell M)` 小的区间，有

\[
|K_{h,\ell}(m)|
\le
2\pi {hH\over \ell M}
+O\left(\left({hH\over \ell M}\right)^2\right).
\]

代入 RRD 系数并用 `H/M` 归一化后，

\[
{|\omega_\ell|\over h}\cdot {hH\over \ell M}
\bigg/ {H\over M}
=
{|\omega_\ell|\over \ell}.
\tag{40.1}
\]

所以 `RRD` 天然落入与 `QLOW` 相同的 Selberg 变差范数

\[
\mathcal V_\omega=\sum_\ell {|\omega_\ell|\over \ell}.
\tag{40.2}
\]

这一步把 `RRD` 的归一化问题闭合：不需要引入新尺度，真正剩余是证明粗数指示函数在该同权测试范数下足够小。

由旧压力样本可知，必须做两段式拆解。令

\[
a_m=1_{P^-(m)>Y}-\rho_M,
\qquad
a_m=\Pi_{\le Z}a_m+(1-\Pi_{\le Z})a_m.
\tag{40.3}
\]

其中 `Pi_{<=Z}` 是待正式化的低模周期/Buchstab 低层投影。于是

\[
\mathcal E_{\rm RRD}
=
\mathcal E_{\rm low}
+
\mathcal E_{\rm perp}.
\tag{40.4}
\]

低模项不是随机误差；它若偏大，应触发 `OSPC/CRTDefect` 或消耗很小独立预算。正交项才适合用 Buchstab 分解、CRT 非零类均衡和短窗不可复用证明小范数。

因此 `C_RRD<=0.020` 被进一步拆成三个可审查目标：

| 子项 | 预算 | 证明义务 |
| --- | ---: | --- |
| `RRD-low` | `0.006` | 低模项若超过该预算，必须定量推出 `OSPC/CRTDefect`；否则由 RRD 账本吸收。 |
| `RRD-perp` | `0.012` | 去掉低模投影后的正交粗数余项满足同权测试范数上界。 |
| `RRD-conversion` | `0.002` | 振幅线性化二阶项、dyadic 端点和归一化换算误差。 |

当前主链剩余从

```text
证明 RRD 很小
```

精确化为

\[
C_{\rm RRD-low}+C_{\rm RRD-perp}+C_{\rm RRD-conv}\le 0.020.
\tag{40.5}
\]

下一步最小硬点是形式化 `Pi_{<=Z}` 并证明低模项的二分出口：

```text
RRD-low small
或
RRD-low large => OSPC/CRTDefect.
```

完成该出口后，`RRD-perp` 才成为一个干净的同权大筛/均衡估计。

## 41. RRD-low 的低模投影与 OSPC 二分

继续推进 `RRD-low` 后，新增脚本：

```text
experiments/rse_rrd_low_projection_dichotomy.py
```

对应输出：

```text
docs/monograph/rse-rrd-low-projection-dichotomy.md
docs/monograph/rse-rrd-low-projection-dichotomy.json
```

本轮首先修正一个规范点：早期 `OSPC` 写法若在右侧额外除以 `r-1`，则均匀分布也会自动满足，不能作为“有向集中”判据。正确尺度应为

\[
E_{\rm dir}(q,r)
=
\frac{(r-1)\sum_{a\in(\mathbb Z/r\mathbb Z)^\times}|C_a(q,r)|^2}
{\mathcal A(q,r)^2},
\qquad
E_{\rm dir}(q,r)\ge 1+\delta_{\rm dir}.
\tag{41.1}
\]

旧辅助模扫描在该尺度下的最大 `complex_energy` 仅为 `0.004424`，说明旧样本没有显示强有向集中；也说明 ordinary support concentration 仍不能替代 `OSPC`。

现在正式定义低模投影。固定 dyadic 层 `m~M`，取 Hilbert 空间

\[
\mathcal H_M=L^2([M,2M),\mu_M),
\]

其中 `mu_M` 是归一化计数测度。令

\[
a(m)=1_{P^-(m)>Y}-\rho_M.
\]

选择低模字典 `D_Z`，由三类原子张成：

1. `q<=Z` 的小模周期原子；
2. Buchstab 分解的低层因子原子；
3. 辅助模 `r` 上的有向残基块原子，对应 `C_a(q,r)`。

定义

\[
\Pi_{\le Z}:\mathcal H_M\to {\rm span}(D_Z)
\tag{41.2}
\]

为正交投影；若字典非正交，则必须用 Gram 矩阵的外向区间逆来定义可审查投影。于是

\[
a=a_{\rm low}+a_{\rm perp},
\qquad
a_{\rm low}=\Pi_{\le Z}a.
\tag{41.3}
\]

令 `W` 为上一节已经同权归一化后的 RSE 临界测试函数，则

\[
\mathcal E_{\rm low}
=
\langle \Pi_{\le Z}a,W\rangle
=
\langle a,\Pi_{\le Z}W\rangle.
\tag{41.4}
\]

由正交投影和 Cauchy--Bessel，得到严格二分：

```text
若 |E_low| <= 0.006，
    则 RRD-low 被账本吸收；
若 |E_low| > 0.006，
    则某个低模块 B(q,r) 的投影贡献超过块预算，
    从而进入 OSPC*/CRTDefect 出口。
```

这里 `OSPC*` 指修正后的 `E_dir(q,r)>=1+delta_dir`。因此 `RRD-low` 的当前最小剩余已不是定义问题，而是证明低模块预算违例确实推出 `OSPC*` 或直接 `CRTDefect`。完成该出口后，主链可转入 `RRD-perp<=0.012` 的正交均衡估计。

## 42. 低模块出口的代数准则

继续攻 `low-block=>exit` 后，新增脚本：

```text
experiments/rse_low_block_exit_criterion.py
```

对应输出：

```text
docs/monograph/rse-low-block-exit-criterion.md
docs/monograph/rse-low-block-exit-criterion.json
```

该准则把低模块预算违例化为一个纯代数二分。取

```text
epsilon_low = 0.006,
delta_dir = 1/4.
```

则

\[
{ \epsilon_{\rm low}\over \sqrt{1+\delta_{\rm dir}}}
=0.005366563145999495.
\tag{42.1}
\]

把低模投影后的测试函数分解成有限低模块

\[
\Pi_{\le Z}W=\sum_B W_B,
\]

其中 `B=(q,r,s)` 表示小模、辅助模与 Buchstab 低层类型。对每个块定义

\[
C_{B,a}=\sum_{m\equiv a\pmod r}W_B(m),
\qquad
\mathcal A_B=\sum_m |W_B(m)|,
\tag{42.2}
\]

以及

\[
E_{\rm dir}(B)
=
\frac{(r-1)\sum_a |C_{B,a}|^2}{\mathcal A_B^2}.
\tag{42.3}
\]

再令 `kappa_B` 表示真实粗数残差在该块上的归一化 CRT 缺陷强度，使

\[
\left|\sum_a d_{B,a}C_{B,a}\right|
\le
\kappa_B
\left(\sum_a |C_{B,a}|^2\right)^{1/2}.
\tag{42.4}
\]

若所有低模块都没有 `OSPC*`，即

\[
E_{\rm dir}(B)\le 1+\delta_{\rm dir},
\]

则由 Cauchy--Schwarz 得

\[
|\mathcal E_{\rm low}|
\le
\sqrt{1+\delta_{\rm dir}}
\sum_B \kappa_B m_B,
\tag{42.5}
\]

其中 `m_B` 是吸收 `A_B/sqrt(r-1)` 后的同权块质量。因此若同时有

\[
\sum_B \kappa_B m_B
\le
0.005366563145999495,
\tag{42.6}
\]

便推出

\[
|\mathcal E_{\rm low}|\le 0.006.
\]

逆否命题给出当前所需出口：

```text
|E_low| > 0.006
=> 存在低模块 OSPC*
   或 加权 CRTDefect 超过 0.005366563145999495。
```

这一步把 `RRD-low` 的剩余从“证明低模块出口”压缩为一个具体加权 CRT 缺陷不等式。下一步最优硬点是证明

\[
\sum_B \kappa_B m_B\le 0.005366563145999495
\]

或证明该不等式失败时必触发已有 `Tail-anchor/CRTDefect` 刚性出口。完成后，`RRD-low` 将从主链剩余中移除，转入 `RRD-perp<=0.012`。
