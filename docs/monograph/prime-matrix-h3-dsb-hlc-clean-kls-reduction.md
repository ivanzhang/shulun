# H3-DSB 高 lcm clean formal unit 到 KLS-window 的归约

**状态：** `hlc_clean_kls_reduction_proved_external_kls_adapted_self_contained_open`

本文继续只攻击当前唯一闭合目标：

```text
H3 Distributed Singleton Bilinear Exclusion.
```

上一层把 `L2-flat residual` 接入 KLS admission 表。本文继续完成“逐项核验所有
HLC formal unit”的形式化：定义 clean formal unit，并证明 clean 时 K1--K6 全部通过。
剩余只是不在本文内重证的外部 `HLC-KLS-window` 估计。

## 1. Clean HLC formal unit

称一个 HLC formal unit `B` 为 clean，若以下命名出口均未发生：

```text
E1: low-effective-modulus PDEC/ColumnCRT；
E2: high-frequency/sawtooth endpoint；
E3: endpoint/SAE smoothing failure；
E4: coefficient concentration；
E5: clamp low-mod / unit conflict / gcd overrun；
E6: tail-label concentration / excessive dyadic splitting。
```

这些出口正是 admission 表 K1--K6 的失败项。

## 2. Clean unit 的 K1--K6 核验

**命题。** 若 HLC L2-flat formal unit `B` 是 clean，则 `B` 满足 KLS admission 的 K1--K6。

**证明。**

1. **K1 模数。** 若有效模数不在 KLS 可控范围，则由 high-gcd descent 与低有效模路由，
   `E1` 发生；clean 排除 `E1`，故 K1 成立。
2. **K2 频率。** 若有效频率超过截断范围，则该项正是 sawtooth 高频尾，`E2` 发生；
   clean 排除 `E2`，故 K2 成立。
3. **K3 端点。** 若互补商窗口 `J_\ell=I/\ell` 不能平滑或端点误差未入账，则 `E3` 发生；
   clean 排除 `E3`，故 K3 成立。
4. **K4 二范数。** L2-flat residual 给出
   \[
   \sum_a |b_a|^2\le\mathfrak C_{\rm flat}(R,\tau)/R.
   \tag{CKR-1}
   \]
   若仍有大原子或二范数超标，则 `E4` 发生；clean 排除 `E4`，故 K4 成立。
5. **K5 gcd/unit。** 若 gcd 或非单位层超出多对数账本，则 `E5` 发生；clean 排除 `E5`，
   故 K5 成立。
6. **K6 分块。** 若 dyadic 或尾标签分块数量不是多对数级，则为尾标签集中或过度分裂，
   `E6` 发生；clean 排除 `E6`，故 K6 成立。

六项全部成立。证毕。

## 3. HLC-KLS 窗口对象

对 clean unit，Kloosterman 核保持为

\[
e\!\left(-\frac{h\rho(c)\bar\ell}{R(c)}\right),
\tag{CKR-2}
\]

互补商窗口为

\[
J_\ell=\{m:\ell m\in I\},
\qquad |J_\ell|\le \frac{q+O(1)}{\ell}.
\tag{CKR-3}
\]

clean admission 后，HLC 需要控制的对象正是

\[
\mathcal K_{\rm HLC}(B)
=
\sum_{c\in B}\sum_{0<|h|\le H_0}
\beta_{c,h}
\sum_{y<\ell\le p}\alpha_\ell
e\!\left(-\frac{h\rho(c)\bar\ell}{R(c)}\right)
\sum_m \Lambda(m)W_{\ell,c}(m)e\!\left(\frac{hm}{R(c)}\right).
\tag{CKR-4}
\]

其中 `(CKR-1)` 给出系数二范数，K1--K6 给出模数、频率、平滑、gcd 与分块条件。

## 4. 外部输入版闭合命题

**HLC-KLS-ext 输入。** 对所有 clean HLC formal unit `B`，`(CKR-4)` 满足

\[
\mathcal K_{\rm HLC}(B)=O\!\left(\frac{q}{\log^2 y}\right),
\tag{CKR-5}
\]

或满足更强的任意对数节省版本。

**条件闭合命题。** 若 HLC-KLS-ext 成立，则 clean L2-flat residual 不可能承载
`q/log y` 级的 HLC 反例质量。

**证明。**
HLC 反例质量若在 clean unit 内保持 `q/log y` 级，则前面非零频率归约强制
`\mathcal K_{\rm HLC}(B)` 至少为同阶的大量项；但 `(CKR-5)` 给出 `q/log^2 y` 级上界，
与 `log y` 因子差距矛盾。证毕。

## 5. 当前实际闭合度

本文完成：

1. clean formal unit 的定义；
2. clean `=>` K1--K6 admission 的逐项证明；
3. HLC clean unit 的 Kloosterman 窗口对象 `(CKR-4)`；
4. 外部 HLC-KLS 输入下的 clean residual 条件排斥。

本文仍未完成：

```text
在文内自足证明 HLC-KLS-ext。
```

外部深定理版适配已补入
`docs/monograph/prime-matrix-h3-dsb-hlc-kls-external-adaptation.md`。该文件逐项核验
`(CKR-4)` 的模数、频率、逆元变量、短窗口、素数权、二范数、gcd/unit 与分块条件，
并说明在接受 DI/BFI/Kuznetsov 型窗口化 Kloosterman 输入时，clean HLC 分支得到
`O(q/log^2 y)` 上界而闭合。

这就是当前剩余障碍的最窄形式：不再是 high-lcm / short-arc / L2-flat 的内部结构问题，
而是 clean HLC Kloosterman window 的完全自足谱/dispersion 重证问题；外部深定理版已完成
变量适配与审稿边界标注。
