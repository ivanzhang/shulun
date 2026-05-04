# ThreeEdge-Parity-PDEC：共振三点链的合并奇偶证书

**状态：** `alpha_tail_threeedge_parity_pdec_reduction_open`

本文补上 `resonant chain parity gate` 后的最小硬点：三组相关
`K01,K12,K02` 不能当作三条独立二点相关处理。三点链上每个未锁素数只命中一个点，却同时翻转两条边，
因此所有奇偶压力必须落在一个四状态低模 CRT 证书或一个二边尾锚证书中。

## 1. 三边符号向量

在共振链

\[
d,\qquad d+r,\qquad d+2r
\tag{TEP-1}
\]

都 squarefree 的支撑 `T_r` 上，记

\[
\epsilon_{01}(d)=\mu(d)\mu(d+r),\quad
\epsilon_{12}(d)=\mu(d+r)\mu(d+2r),\quad
\epsilon_{02}(d)=\mu(d)\mu(d+2r).
\tag{TEP-2}
\]

逐点有恒等式

\[
\epsilon_{01}(d)\epsilon_{12}(d)\epsilon_{02}(d)=1.
\tag{TEP-3}
\]

因此三边符号只可能落在四个状态

\[
A=(+,+,+),\quad B=(-,+,-),\quad C=(-,-,+),\quad D=(+,-,-).
\tag{TEP-4}
\]

这条四状态约束是三点链相对二点链的新增刚性。

## 2. 局部素数状态表

对素数 `q`：

1. 若 `q|r`，则三点同余。`q` 要么不影响三点，要么共同进入三点支撑；无论哪种情形都不改变三边符号。
2. 若 `q∤r` 且 `q>2`，则 `0,-r,-2r mod q` 互异，`q` 最多命中一个点，并产生下表：

| 局部情形 | 条件 | 三边状态 |
|---|---|---|
| 无命中 | `d` 不在 `0,-r,-2r` | `A=(+,+,+)` |
| 命中点 0 | `d≡0` | `B=(-,+,-)` |
| 命中点 1 | `d≡-r` | `C=(-,-,+)` |
| 命中点 2 | `d≡-2r` | `D=(+,-,-)` |

3. `q=2` 是退化低模因子：若 `2|r`，按第 1 类；若 `2∤r`，局部符号为固定状态，可并入低模主项。

**证明。**  
当 `q∤r,q>2` 时三个剩余类互异，所以 squarefree 三点链中 `q` 不能同时整除两个不同点。若命中点
`i`，则 `q` 只进入含点 `i` 的两条边的对称差，正好翻转这两条边。若 `q|r`，三个点同余，`q`
进入三点支撑的次数相同，不进入任何对称差。证毕。

## 3. 四状态计数与三边相关

令 `N_A,N_B,N_C,N_D` 为 `T_r` 上四状态计数，`N=|T_r|`。则

\[
\begin{aligned}
K_{01}&=N_A+N_D-N_B-N_C,\\
K_{12}&=N_A+N_B-N_C-N_D,\\
K_{02}&=N_A+N_C-N_B-N_D.
\end{aligned}
\tag{TEP-5}
\]

反过来

\[
\begin{aligned}
N_A&={N+K_{01}+K_{12}+K_{02}\over4},\\
N_B&={N-K_{01}+K_{12}-K_{02}\over4},\\
N_C&={N-K_{01}-K_{12}+K_{02}\over4},\\
N_D&={N+K_{01}-K_{12}-K_{02}\over4}.
\end{aligned}
\tag{TEP-6}
\]

所以“三条边同时偏大”不是三个自由异常，而是四状态分布偏离局部 CRT 主项。正式证书应检验
`(N_A,N_B,N_C,N_D)`，而不是逐条边重复使用二点 `Parity-PDEC`。

## 4. 低模合并证书

取 cutoff `R<=y`，令

\[
Q_R=\prod_{q\le R}q.
\tag{TEP-7}
\]

由第 2 节，把每个 `d mod Q_R` 映到低模四状态

\[
\Gamma_R(d)\in\{A,B,C,D\}.
\tag{TEP-8}
\]

令 `P_R(A),P_R(B),P_R(C),P_R(D)` 为完整 CRT residue 系上的局部主项概率；它由第 2 节的局部表
逐素卷积给出，是完全显式的有理数。定义中心化四状态函数

\[
F_{R,v}(d)=1_{\Gamma_R(d)=v}-P_R(v),\qquad v\in\{A,B,C,D\}.
\tag{TEP-9}
\]

令三边相关向量

\[
K=(K_{01},K_{12},K_{02})
\tag{TEP-10}
\]

在反例链中达到阈值 `Xi`，则对任意 `0<beta<1` 至少发生一项：

1. **ThreeEdge-Parity-PDEC。**

\[
\max_v\left|\sum_{d\in T_r}F_{R,v}(d)\right|
\ge c_1\beta\Xi;
\tag{TEP-11}
\]

2. **三边高尾奇偶锚。**

大于 `R` 的未锁素数对四状态的剩余翻转贡献达到

\[
\ge c_2(1-\beta)\Xi;
\tag{TEP-12}
\]

3. **无符号三点链包络失败。**

`|T_r|` 超过前文三禁/一禁 Selberg 包络预算。

这里 `c_1,c_2` 只依赖正式反例抽取时对三组边相关的线性组合归一化；若反例直接给出某一条边
`Kij` 大，则可取相应坐标投影并退化回二点版本。

**证明。**  
把完整三边状态分解为低模状态与高尾状态的坐标乘积：

\[
\epsilon_{ab}(d)=\epsilon^{\le R}_{ab}(d)\epsilon^{>R}_{ab}(d),
\qquad ab\in\{01,12,02\}.
\tag{TEP-13}
\]

于是

\[
K_{ab}=\sum_{d\in T_r}\epsilon^{\le R}_{ab}(d)
+
\sum_{d\in T_r}\epsilon^{\le R}_{ab}(d)\bigl(\epsilon^{>R}_{ab}(d)-1\bigr).
\tag{TEP-14}
\]

若第二项在三个坐标中都小于 `(1-beta)Xi` 的正式归一化阈值，则第一项必须承担至少
`beta Xi` 的压力。第一项只由 `d mod Q_R` 决定。再用 `(TEP-5)--(TEP-6)` 的可逆线性变换，
边坐标压力等价于四状态低模计数相对局部主项 `P_R(v)|T_r|` 的偏离；因此至少有一个
`F_{R,v}` 的和达到 `(TEP-11)`。若低模与高尾都不承担，则只能是 `|T_r|` 本身超过无符号三点链预算。
证毕。

## 5. Fourier/CRT 证书出口

`F_{R,v}` 只依赖 `d mod Q_R`，且在完整 residue 系上均值为零。若 `(TEP-11)` 成立，则在
`Z/Q_R Z` 上 Fourier 展开给出非零频率 `h` 满足

\[
\left|\sum_{a\bmod Q_R}A_r(a)e(ha/Q_R)\right|
\ge
{\Delta_v\over \sum_{h\ne0}|\widehat F_{R,v}(h)|},
\tag{TEP-15}
\]

其中 `A_r(a)=#{d in T_r:d≡a mod Q_R}`，`\Delta_v=|\sum_{d\in T_r}F_{R,v}(d)|`。
这就是合并三边版 `Parity-PDEC` 证书。

## 6. 高尾二边锚出口

若 `(TEP-12)` 成立，按高素数从小到大 telescoping。对 `q∤r,q>R`：

```text
d≡0      翻转 01 与 02；
d≡-r     翻转 01 与 12；
d≡-2r    翻转 12 与 02。
```

因此尾部异常不是单边锚点，而是二边同源锚点。一个高素锚点若被用来增加某条边压力，必同时改变另一条
边的状态；这给 `ColumnCRT/PDEC/SAE` 证书额外一行一致性约束。

## 7. 审计样本

审计脚本：

```text
experiments/prime_matrix_alpha_tail_threeedge_parity_audit.py
```

样本：

| p | block | shift | chains | A | B | C | D | K01 | K12 | K02 | max centered |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 997 | 4096 | -36 | 362 | 172 | 60 | 65 | 65 | 112 | 102 | 112 | 35.660899 |
| 5003 | 8192 | -36 | 1686 | 657 | 348 | 331 | 350 | 328 | 324 | 290 | -34.539849 |
| 10007 | 16384 | -900 | 3720 | 1254 | 829 | 811 | 826 | 440 | 446 | 410 | -156.257655 |

样本核验 `(TEP-5)`：旧脚本给出的 `corr01,corr12,corr02` 正是四状态计数的线性投影。
低模中心化偏置没有单调同号，说明正式闭合必须同时保留低模 PDEC 与高尾二边锚两个出口。

## 8. 审稿边界

已证明：

```text
共振三点链有符号压力
=> ThreeEdge-Parity-PDEC
   or three-edge tail-anchor pressure
   or unsigned three-point sieve envelope failure.
```

尚未证明：

```text
ThreeEdge-Parity-PDEC 与 three-edge tail-anchor 两个出口不可能。
```

下一步最小硬点是给 `(TEP-11)` 的四状态低模函数提交正式 `PDEC-Cert`，并把 `(TEP-12)` 的
二边同源高素锚接入现有 `ColumnCRT/SAE` 约束矩阵。
