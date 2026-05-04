# WFD-core：平方根 well-factorable 平衡化与双模数核心

**状态：** `wfd_core_reduced_to_bsc_complete_kloosterman_bilinear_core`

本文继续只攻击同一个剩余：

```text
WFD-core: windowed well-factorable Kloosterman dispersion mean estimate.
```

本步目标是把 `WFD-core` 中的单一 well-factorable 模数权，严格拆成平方根双模数平均。这样
剩余不再是笼统的 BFI/DI，而是一个明确的 balanced two-modulus Kloosterman 核 `BWFD-core`。
后续 `prime-matrix-h3-dsb-hlc-bwfd-core-spectral-completion-attack.md` 已进一步把 `BWFD-core`
经 `s` 变量精确完成和完整 Kloosterman 乘法公式压缩为 `BSC-core`。

## 1. 起点：WFD-core

上一层的剩余为

\[
\mathcal W(C,S,H)
=
\sum_{c\sim C}\lambda_c
\sum_{0<|h|\le H}\omega_h
\sum_{\substack{s\sim S\\(s,c)=1}}
\beta_s e_c(a_hs+b_h\bar s),
\tag{WB-1}
\]

目标是

\[
|\mathcal W(C,S,H)|
\ll_A
\frac{\mathcal B(C,S,H)}{\log^A y},
\tag{WB-2}
\]

其中 `\mathcal B(C,S,H)` 是 KZ-D 谱大筛给出的自然二范数尺度，且 `\lambda_c` 为
well-factorable 权。

## 2. 平方根 well-factorable 分解

设 dyadic 支持为 `C\le c< C_+`，其中 `C_+\asymp C`。取

\[
U=V=C_+^{1/2}.
\tag{WB-3}
\]

由 well-factorable 性质，存在

\[
\lambda_c=\sum_{c=uv}\alpha_u\delta_v,
\qquad
u\le U,\quad v\le V,\quad
|\alpha_u|,|\delta_v|\le\tau(uv)^C.
\tag{WB-4}
\]

把 `c~C` 的 dyadic 条件插入 `(WB-4)`。若 `uv\in[C,C_+)` 且 `u,v<=C_+^{1/2}`，则
必有

\[
u\asymp C^{1/2},\qquad v\asymp C^{1/2}
\tag{WB-5}
\]

除了 dyadic 边界的 `\log^{O(1)}y` 个平滑过渡块。原因是若 `u<C^{1/2}/L`，则
`v\gg LC^{1/2}` 才能使 `uv\ge C`，这与 `v<=C_+^{1/2}\asymp C^{1/2}` 矛盾；`v` 同理。

因此 WFD-core 可拆成多对数多个平衡块

\[
\mathcal W_{U,V}
=
\sum_{u\sim U}\alpha_u
\sum_{v\sim V}\delta_v
\sum_{0<|h|\le H}\omega_h
\sum_{\substack{s\sim S\\(s,uv)=1}}
\beta_s e_{uv}(a_hs+b_h\bar s),
\tag{WB-6}
\]

其中

\[
U,V=C^{1/2}\log^{O(1)}y,\qquad UV\asymp C.
\tag{WB-7}
\]

## 3. gcd 层剥离

令 `g=(u,v)`，写 `u=gu_1`, `v=gv_1`, `(u_1,v_1)=1`。单位条件 `(s,uv)=1` 已强迫
`(s,g)=1`。公共因子层的总权重由

\[
\sum_g\frac{\tau(g)^C}{g}\ll\log^{C'}y
\tag{WB-8}
\]

吸收：在 dispersion 来源中，相容层还额外要求同一公共模上的剩余类一致；不相容层为零。
故只需证明互素主层 `(u,v)=1`。

## 4. CRT 相位因子化

在 `(u,v)=1` 的主层中，

\[
\frac{1}{uv}\equiv \frac{\bar v}{u}+\frac{\bar u}{v}\pmod1,
\tag{WB-9}
\]

且 `\bar s mod uv` 同时投影为 `\bar s mod u` 和 `\bar s mod v`。所以

\[
e_{uv}(a_hs+b_h\bar s)
=
e_u(\bar v(a_hs+b_h\bar s))\,
e_v(\bar u(a_hs+b_h\bar s)).
\tag{WB-10}
\]

这一步把单模数 Kloosterman 相位变成两个平方根模数上的耦合相位。注意：这不是估计，
只是 CRT 恒等式；它不会产生对数节省。

## 5. 剩余核心：BWFD-core

**BWFD-core（balanced well-factorable dispersion core）。** 对所有满足 `(WB-7)` 的平衡块，
互素主层满足

\[
\left|
\sum_{\substack{u\sim U,\,v\sim V\\(u,v)=1}}
\alpha_u\delta_v
\sum_{0<|h|\le H}\omega_h
\sum_{\substack{s\sim S\\(s,uv)=1}}
\beta_s
e_u(\bar v(a_hs+b_h\bar s))
e_v(\bar u(a_hs+b_h\bar s))
\right|
\ll_A
\frac{\mathcal B(UV,S,H)}{\log^A y}.
\tag{WB-11}
\]

这是当前真正的 balanced Type-II 双模数 Kloosterman 平均。它比 `(WB-1)` 更窄，因为：

1. 模数已强制分裂为两个平方根因子；
2. 非互素层已变成多对数账本；
3. 相位已完全 CRT 因子化；
4. 端点、频率、dyadic 与 unit 损失仍由 K1--K6 吸收。

## 6. `BWFD-core => WFD-core`

**命题。** 若 BWFD-core 成立，则 WFD-core 成立。

**证明。**

1. 用 `(WB-4)` 在平方根处分解 `\lambda_c`。
2. 用 dyadic 平滑拆分 `u,v`。由 `(WB-5)`，只有 `U,V=C^{1/2}\log^{O(1)}y` 的平衡块可贡献。
3. gcd 层由 `(WB-8)` 吸收；剩余互素主层由 `(WB-10)` 化为 `(WB-11)`。
4. 对全部平衡块调用 BWFD-core，调用指数取 `A+C_{\rm dyad}+C_{\rm gcd}+10`，吸收所有
   多对数损失。

得到 `(WB-2)`。证毕。

## 7. 当前边界

本文严格完成：

```text
BSC-core => BWFD-core => WFD-core => KZ-E.
```

本文本身证明 `BWFD-core=>WFD-core`；后续谱完成攻击文件进一步证明 `BSC-core=>BWFD-core`。
因此当前唯一剩余进一步压缩为：

```text
BSC-core: balanced complete Kloosterman bilinear correlation logarithmic saving.
```

下一步不能再重复筛权分解、gcd 剥离、CRT 归一化或 `s`-completion；这些已经完成。必须直接攻
`(BSA-13)`：在 `u,v≈C^{1/2}` 的完整 Kloosterman 双线性族上证明任意对数节省。
