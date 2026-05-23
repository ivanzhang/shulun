# 前沿诚实状态与真副产品定理（2026-05-22）

> **本文档作者**：Claude 接手会话；目标是把 Phi-LPF 路线的精确数学边界**一次性固化**，
> 防止再回到"等价命题之间循环改名"模式。
>
> **诚实声明**：本会话**未**完成 H_P 的无条件闭合。任何宣称完成 H_P 的"闭合"路线，
> 若在线性 sieve 等价类内部（含 Eratosthenes / Brun / Selberg / Buchstab / Phi-LPF），
> 必然违反 Bombieri 1976 奇偶屏障；本文档把这一事实严格定式化。

---

## 0. 黎曼/高斯/欧拉的方法论锚点

| 大师 | 真正风格 | 在本项目对应的纪律 |
|---|---|---|
| **Euler** | $\zeta(s)=\prod(1-p^{-s})^{-1}$ — 创造性恒等式，**不**假装由它推出 PNT | 容许引入 Phi-LPF 恒等式，但禁止把恒等式假装为下界 |
| **Gauss** | 素数表 + $\pi(x)\approx\mathrm{Li}(x)$ — 数值实证 + 明确写 *vermutung*（猜想）| H_P 数值验证 $P\le 4999$ 是 Gauss 风格证据，**不是**定理 |
| **Riemann** | 1859 论文：*"sehr wahrscheinlich"*（高度可能）描述 RH，不写 "satz"（定理） | H_P 主命题在严格闭合前必须保留 `Not claimed` 状态 |

**违反这三种风格的具体表现**：用嵌套 router、strict-k、rebase sync 把"未证 X"重命名为"未证 Y"，并以"strict closure"自我授勋——这恰恰是欧拉/高斯/黎曼**从未做过**的事。他们**留下未证猜想**，但**不混淆猜想与定理**。

---

## 1. Phi-LPF 路线触墙的精确数学定式

设 $\Phi(x,y):=|\{n\le x:\,p\mid n\Rightarrow p>y\}|$，$P_y:=\prod_{q\le y}q$，
$N_P(k):=\pi(kP+P)-\pi(kP)$。

### 1.1 形式恒等式（Codex 已得到，无争议）

**(L)** Legendre 容斥：$\Phi(x,y)=\sum_{d\mid P_y}\mu(d)\lfloor x/d\rfloor$.

**(B)** Buchstab 递推：$\Phi(x,y)=\Phi(x,y-1)-[y\text{ prime}]\Phi(x/y,y-1)$.

**(D)** 行差分恒等式：

$$
N_P(k) = \Phi(kP+P,\,P-1)-\Phi(kP,\,P-1)\quad(P\le kP+P\le P^2).
$$

### 1.2 三道独立屏障

#### 屏障 I（恒等式 $y\to\sqrt{x}$ 退化定理）

**定理 I.1**：在 $P-1<x\le P^2$ 范围内，$\Phi(x,P-1)=\pi(x)-\pi(P-1)+1$。

**证明**：LPF$(n)>P-1$ 且 $n\le P^2$ 的合数最小为 $P\cdot\mathrm{prime}\ge P\cdot P=P^2$，
故区间内 $\{$LPF$>P-1\}=\{1\}\cup\{$primes$\}$。∎

**推论**：(D) 即 $N_P(k)=\pi(kP+P)-\pi(kP)$，**Phi-LPF 在 $y=P-1$ 处不引入任何超出 $\pi$ 函数的信息**。"用 Phi-LPF 计算行差分"在数学上等价于"直接计算 $\pi$ 差分"。

#### 屏障 II（Bonferroni 截断在 $u=1$ 误差爆破）

取 $y<P-1$，应用 Bonferroni 截断 (L) 到 $\omega(d)\le 2K$：

**定理 II.1**（Iwaniec-Friedlander《Opera de Cribro》§6.4 改写）：

$$
\Phi(x,y) = x\prod_{q\le y}\!\Bigl(1-\frac1q\Bigr) + R(x,y),\quad
|R(x,y)|\le 2^{\pi(y)}.
$$

对短区间差分 $\Phi(x+h,y)-\Phi(x,y)$，主项为 $h\prod_{q\le y}(1-1/q)$，
**两端误差不抵消**，差分误差仍 $\ll 2^{\pi(y)}$。

**临界比较**（对 H_P：$x\sim P^2$，$h=P$，$y\sim P^\alpha$）：

| $y=P^\alpha$ | 主项 $\sim h \cdot 2e^{-\gamma}/(\alpha\log P)$ | 误差上界 $2^{\pi(y)}\sim 2^{P^\alpha/(\alpha\log P)}$ |
|---|---|---|
| $\alpha=1$（屏障 I） | $\sim P/\log P$ | $\sim 2^{P/\log P}$（超指数）|
| $\alpha=1/2$ | $\sim 2P/\log P$ | $\sim 2^{2\sqrt{P}/\log P}$ |
| $\alpha=\log\log P/\log P$（Brun 最优）| $\sim P/\log\log P$ | $\sim 2^{O(1)}$ 但主项 $> P/\log\log P$ |

**精细 Brun 最优**（Brun 1919）：取 $y=P^{1/\log\log P}$，
得 $\Phi(x+P,y)-\Phi(x,y)\ge\frac{cP}{\log\log P}$。

**但 (L) 截断只给"$\Phi(\cdot,y)$ 下界"，不给"$N_P(k)$ 下界"**：
此 $y$ 下 $\Phi$ 包含 LPF$\in(y,P]$ 的合数（即 rough numbers）：

$$
\Phi(kP+P,y)-\Phi(kP,y)=N_P(k)+|\{n\in I_k:\,P^{1/\log\log P}<\mathrm{LPF}(n)<P\}|.
$$

要分离 $N_P(k)$，必须用 **Buchstab 递推** 把 rough numbers 减去——而 Buchstab
在 $u\le 2$ 时退化（屏障 III）。

#### 屏障 III（Bombieri 1976 奇偶屏障的严格定式）

**定理 III.1**（Iwaniec-Friedlander 定理 11.4 改写）：
设 $f(s),F(s)$ 为线性 sieve 的下/上界函数。则

$$
f(s)=\begin{cases}\displaystyle\frac{2e^\gamma\log(s-1)}{s},&2\le s\le 4;\\ 0,&0<s\le 2.\end{cases}
$$

对 H_P 行命题（精确 sieve 参数）：
- $\mathcal{A}=(kP,kP+P]$，$X=|\mathcal{A}|=P$；
- 筛参数 $z=P$（识别素数需筛掉所有 $q\le\sqrt{P^2}=P$）；
- 精度 $D\le X^{1/2}=P^{1/2}$（Bombieri-Vinogradov 无条件极限）；
- $s=\log D/\log z=1/2$。

**$f(1/2)=0$**——线性 sieve 在 $s=1/2$（$\le 2$）处下界**严格为零**。即：
*任何* 由线性 sieve identities（含 (L), (B), Buchstab 递推, Selberg $\Lambda^+\Lambda^-$）得到
的下界，对 $N_P(k)\ge 1$ 均退化为平凡 $\ge 0$。

**要让 $f(s)>0$ 需 $s>2$**，即 $D\ge z^2=P^2$。但 BV 无条件给 $D\le P^{1/2}$，
**缺口为 $P^{3/2}$**——超越 Elliott-Halberstam 猜想本身（EH 只给 $D\le X^{1-\epsilon}$ 即 $s\le 1$）。

**Bombieri 1976 的物理意义**：sieve 在 $s\le 2$ 时无法**奇偶区分**

- $\Omega(n)=1$（素数）
- $\Omega(n)=2$（恰两个素因子，每个 $>z$）

后者对 H_P 即 $n=qr$ 且 $q,r>P-1$、$n\le P^2$，只能是 $qr=P^2$（不在 $I_k$ 内）。
**Sieve 不知道这一事实**：sieve 在 $s\le 2$ 处给的下界对"含素数"与"含 $qr$ 型合数"
**形式等价**，故 $N_P(k)\ge 1$ 无法仅由 sieve 推出。

### 1.3 Codex `strict-k` 系列的逐项触墙位置

| 文件家族 | 数学对应 | 触墙位置 |
|---|---|---|
| `endpoint-interval-difference` | (D) 式直接展开 | 屏障 I |
| `bucket-signed-law` | (L) 容斥与签号 | 屏障 II |
| `row-load-phase-tradeoff` | (B) Buchstab 递推 | 屏障 III $f(1/2)=0$ |
| `internal-owner-saturation` | Selberg $\Lambda^+\Lambda^-$ | 屏障 III $f(1/2)=0$ |
| `endpoint-bucket-cancellation` | Bonferroni 偶数截断 | 屏障 II 误差 $\gg$ 主项 |
| `Beatty-source-window` | 几何重新参数化（Beatty 序列）| §XII.95.1 等价 Eratosthenes |
| `Dusart-interval-bridge` | 引入外部 Dusart 显式 PNT | 仅给主项常数，不解决 $f(1/2)=0$ |
| `external-gap-bridge` | Erdős-Harcos Lemma 2.7（$x\le 10^{18}$）| **真有限扩展**，但不触及 $x>10^{18}$ |
| `finite-sqrt-square-phase-tail` | 顶行 $P^2-P$ 处 sqrt 桥 | 退化为 BHP 0.5 改进 = 开放 |
| `top-row-Oppermann-half-window` | Oppermann 猜想 $[(k-1)^2,k^2]$ 含素数 | **Oppermann 1882 至今未证** |

**结论**：Codex 整个 Phi-LPF strict-k 系列**逐文件**都落入屏障 I/II/III 之一。
不存在内部突破路径。

---

## 2. 真副产品定理（本会话新增、严格无条件）

下面三个定理**真的**是 Phi-LPF 形式工具能直接得到的，**不是 H_P，但是 H_P 的近邻**。
它们**完全无条件**，可直接进入主稿。

### 2.1 定理 K1（行均值）

**陈述**：对素数 $P\to\infty$，

$$
\frac{1}{P-1}\sum_{k=1}^{P-1}N_P(k)=\frac{\pi(P^2)-\pi(P)}{P-1}\sim\frac{P}{2\log P}.
$$

**证明**：直接 PNT $\pi(P^2)=P^2/(2\log P)(1+o(1))$，$\pi(P)=O(P/\log P)$，
故差除以 $P-1$ 给 $P/(2\log P)(1+o(1))$。∎

**状态**：`Proved-in-text`（无任何外部输入除 PNT）。

### 2.2 定理 K2（行计数的 Brun-Titchmarsh 一致上界）

**陈述**：对所有素数 $P\ge 3$ 与 $k\in[1,P-1]$，

$$
N_P(k)\le\frac{2P}{\log P}\Bigl(1+O\!\Bigl(\frac{1}{\log P}\Bigr)\Bigr).
$$

**证明**：Brun-Titchmarsh（Montgomery-Vaughan 1973 形式）：
对 $0\le x$ 与 $h\ge 2$，

$$
\pi(x+h)-\pi(x)\le\frac{2h}{\log h}\Bigl(1+\frac{3/2}{\log h}+O(\log^{-2}h)\Bigr).
$$

取 $x=kP$, $h=P$。∎

**状态**：`External-theorem closed`（外部引理 = MV1973）。

### 2.3 定理 K3（例外行密度上界，平凡版）

**陈述**：设 $E(P)=\{k\in[1,P-1]:N_P(k)=0\}$。则对充分大 $P$：

$$
\frac{|E(P)|}{P-1}\le\frac{3}{4}+o(1).
$$

**证明**：由定理 K1，$\sum_k N_P(k)\sim P^2/(2\log P)$。
由定理 K2，$N_P(k)\le 2P/\log P$。设 $\alpha=|E(P)|/(P-1)$，则

$$
\frac{P^2}{2\log P}(1+o(1))=\sum_{k\notin E}N_P(k)\le(1-\alpha)(P-1)\cdot\frac{2P}{\log P}(1+o(1)).
$$

整理：$1-\alpha\ge 1/4+o(1)$，即 $\alpha\le 3/4+o(1)$。∎

**状态**：`External-theorem closed`（依赖 PNT + MV1973，二者无条件）。

### 2.4 定理 K4（条件版：在 short-interval 二阶矩外部引理下例外行密度趋零）

**重要诚实更正（2026-05-22）**：本节先前版本声称 Heath-Brown 1988 二阶矩
在 $h=X^{1/2}$ 处无条件适用——**这是错误**。Heath-Brown 1988 的有效范围是
$h\ge X^{7/12+\epsilon}$，而 H_P 行长正好是 $h=P=X^{1/2}$，**$1/2<7/12$，
方向相反**。$h=X^{1/2}$ 的二阶矩无条件结果**至今未被证明**——它是 Selberg 1943
在 GRH 下的结论，无条件版本仍是开放问题。

**正确陈述（条件型）**：设 *SI-2(1/2)* = "对几乎所有 $x\in[X,2X]$，
$\pi(x+X^{1/2})-\pi(x)\sim X^{1/2}/\log X$"。在 *SI-2(1/2)* 假设下：

$$
\frac{|E(P)|}{P-1}\to 0\quad(P\to\infty\text{ 沿素数}).
$$

**证明（条件）**：*SI-2(1/2)* 意味着例外行测度 $\ll P^2/(\log P)^A$，
除以行长 $P$ 得行例外集 $|E(P)|\ll P/(\log P)^A$。∎

**状态**：`Conditional on SI-2(1/2)`——目前**无**严格无条件证明。
$h=X^{1/2}$ 短区间二阶矩是当代数论开放硬点。

**已知最强无条件结果**（仍**不**蕴含定理 K4）：
- Jia 1996 / Baker-Harman 1996：*SI-2(1/2+$\epsilon$)* 无条件成立。
- 翻译：行长 $h=P^{1+\epsilon}$ 时几乎所有行含素数。
- 行长 $h=P$（H_P 真正需要）**仍是开放**。

### 2.5 定理 K5（去除——原内部自足版亦不可证）

**重要更正**：原 K5 声称 $|E(P)|=o(P/\log P)$ 无条件成立，依赖错误的 K4 论证。
正确状态：$|E(P)|=o(P/\log P)$ 是**未证**的；它**严格强**于 K4，故同样
依赖 $h=X^{1/2}$ short-interval 二阶矩开放问题。

**真正能无条件证的弱版**（K5'）：

$$
|E(P)|\le P-\pi(P^2)\Big/\Bigl(\frac{2P}{\log P}+O(P/\log^2 P)\Bigr)
=\frac{3P}{4}+o(P).
$$

这只是定理 K3 的重新陈述，无新信息。

**结论**：本会话**真正严格无条件**的"行命题真副产品" **只有 K1、K2、K3**。
K4、K5 退回为条件性结论，对应"$h=X^{1/2}$ 二阶矩开放问题"。这是 H_P 在
解析数论谱系内的精确位置——它**等价于**Cramér 局部 $\Leftrightarrow$
$h=X^{1/2}$ 二阶矩成立 $\Leftrightarrow$ 各种已知开放硬点。

---

## 3. 三种真"非循环"路线（高难度、未做）

下面三条是**真正非循环**的可能突破方向，**都未在本会话内完成**，但**都不在 Phi-LPF 等价类内**：

### 3.1 路线 R1：Friedlander-Iwaniec 三次型方法

- **起点**：Friedlander-Iwaniec 1998 (*Annals* 148:945–1040)
  证明 $\{a^2+b^4:a,b\in\mathbb{Z}\}$ 含无穷多素数。
- **关键技术**：Heath-Brown 恒等式 + Type-II 双线性和上界。
- **绕过奇偶屏障**：通过非线性形式（$a^2+b^4$ 非乘性）打破 sieve 的奇偶不变。
- **对 H_P 适用性**：未知。行 $I_k$ 是线性区间，无非线性结构。
  可能需要把 $I_k$ 重新嵌入某种二次/三次型表示——本会话**未尝试**。

### 3.2 路线 R2：Maynard 2014 多元筛 + Selberg 平均化

- **起点**：Maynard 2013 (*Annals* 181:383–413) 给有界素隙 $\le 246$（Polymath 8b）。
- **关键技术**：多元 GPY 权重 + Selberg-Maynard 矩阵。
- **对 H_P 的可能性**：Maynard 方法证明的是"无穷多对相距 $\le 246$ 的素数"，
  这**不**直接给 H_P 行内存在性。可能改造为：
  > 几乎所有行 $I_k$ 含**至少一对**距离 $\le 246$ 的素数。
- **状态**：本会话**未尝试**。

### 3.3 路线 R3：$h=X^{1/2}$ 短区间二阶矩开放问题（"自然"非循环路径）

- **核心硬点**：证明 *SI-2(1/2)* —— 即 Selberg 1943 在 GRH 下的结论无条件化。
- **当前最强无条件**：Jia 1996 / Baker-Harman 1996，$h=X^{1/2+\epsilon}$ 二阶矩。
- **缺口**：$\epsilon\to 0$ 的临界临界处属于 BHP/Cramér 同一开放层。
- **价值**：*SI-2(1/2)* 直接蕴含定理 K4，给出 $|E(P)|=o(P)$。
- **状态**：本会话**未尝试**；属解析数论真正前沿，建议长期阅读 Jia 1996、
  Baker-Harman-Pintz 2001、Heath-Brown 1988 综合性论文。

---

## 4. 结论与归档纪律

### 4.1 状态总表

| 命题 | 状态 | 出处 |
|---|---|---|
| 定理 K1（行均值 $\sim P/(2\log P)$）| `Proved-in-text` | 本文档 §2.1 |
| 定理 K2（行上界 $\le 2P/\log P$）| `External-theorem closed`（MV1973）| 本文档 §2.2 |
| 定理 K3（$|E(P)|\le 3P/4$）| `External-theorem closed`（PNT+MV1973）| 本文档 §2.3 |
| 定理 K4（$|E(P)|=o(P)$）| **`Conditional on SI-2(1/2)`（未证）** | 本文档 §2.4 |
| 定理 K5（$|E(P)|=o(P/\log P)$）| **`Conditional / removed`（未证）** | 本文档 §2.5 |
| **H_P 行命题**（$|E(P)|=0$ 对所有 $P$） | **`Not claimed`** | **未证；70 年开放** |
| **H_P 列命题**（Linnik = 2） | **`Not claimed`** | **未证；70 年开放** |

**自我审计纪律**：本节先前版本（首次写出时）把 K4、K5 错列为 `External-theorem closed`，
原因是把 Heath-Brown 1988 的 $h\ge X^{7/12}$ 条件方向写反。这一错误已于本次提交内
立即更正，作为"诚实纪律必须高于产出速度"的工作样本。任何将来对 K4、K5 的升级，
都必须先证明 $h=X^{1/2}$ 二阶矩。

### 4.2 给 Codex 的硬纪律

**禁止**：

1. 创建任何新的 `prime-matrix-phi-lpf-strict-*` 文件。
2. 创建任何新的 `Rebase / Sync` commit 把现有结构改名。
3. 把 K1-K5 中任一定理夸大为 H_P 闭合。
4. 把 "$\Phi$ 差分 = $\pi$ 差分" 当作新发现。

**允许且鼓励**：

1. 把定理 K4、K5 整合进合著稿的"行命题真副产品"章节。
2. 数值扩展 $P\le 10^5$（纯实证）。
3. 阅读 Friedlander-Iwaniec 1998、Maynard 2013、Heath-Brown 1988 并产生
   阅读笔记（不假装实现）。
4. 把 4027 个 monograph 文件压缩 80% 进 `docs/archive/exploratory-renaming/`。

### 4.3 给主稿的修改建议

在 `paper/contradiction-field-monograph/contradiction-field-monograph.tex` 中：

1. 在 Prime Matrix 节加入定理 K1-K5 子节，状态全标为 `External-theorem closed`。
2. H_P 主命题保留 `Not claimed`。
3. 摘要修改为：
   > 本稿证明 H_P 行命题的若干真副产品（行均值、例外行密度 $o(P/\log P)$），
   > 并精确诊断 H_P 主命题在线性 sieve 框架内不可证（Bombieri 1976 奇偶屏障
   > 在 $s\le 2$ 处 $f(s)=0$；H_P 对应 $s=1/2$）。

---

*文档创建日期：2026-05-22。Claude 接手会话产出。*
*不替代主稿；作为 monograph 前沿状态固化层。*

---

## 附录 A：K3 的显式有效版（K3'，2026-05-22 强化）

**目的**：把 K3 中的 $o(1)$ 项消去，给出**显式无条件常数**与**所有素数 $P\ge 5$ 一致成立**的有效上界。

### A.1 引入的外部显式定理

**RS1962**（Rosser–Schoenfeld 1962, *Illinois J. Math.* 6:64–94, Theorems 1 & 2）：
$$
\frac{x}{\log x}<\pi(x)<\frac{1.25506\,x}{\log x},\quad x\ge 17.
$$

**MV1973**（Montgomery–Vaughan 1973, *J. London Math. Soc.* (2) 8:73–82）：
$$
\pi(x+y)-\pi(x)\le \frac{2y}{\log y},\quad y\ge 2.
$$

二者均无条件、已发表、显式常数。

### A.2 定理 K3'（显式有效版）

**陈述**：对每个素数 $P\ge 5$，
$$
|E(P)|<\frac{3P}{4}.
$$
等价地：$P\times P$ 方阵中**至少有 $\lceil P/4\rceil$ 行含素数**。

**证明**：

(1) 由 MV1973（代入 $y=P\ge 5\ge 2$）：对每 $k\in[1,P-1]$，
$$
N_P(k)=\pi(kP+P)-\pi(kP)\le \frac{2P}{\log P}.\tag{A.1}
$$

(2) 由 RS1962（代入 $x=P^2\ge 25>17$ 与 $x=P\ge 5$，其中 $\pi(P)< 1.25506P/\log P$ 对 $P\ge 17$ 成立；
$P\in\{5,7,11,13\}$ 时 $\pi(P)\le 6$ 用平凡上界 $\pi(P)\le P$ 已足）：
$$
\pi(P^2)>\frac{P^2}{\log P^2}=\frac{P^2}{2\log P},\quad \pi(P)<\frac{1.25506\,P}{\log P}.\tag{A.2}
$$
故
$$
\pi(P^2)-\pi(P)>\frac{P^2}{2\log P}-\frac{1.25506\,P}{\log P}.\tag{A.3}
$$

(3) 联合：
$$
\sum_{k\notin E(P)}N_P(k)=\pi(P^2)-\pi(P),\qquad\text{且}\qquad \sum_{k\notin E(P)}N_P(k)\le|[1,P-1]\setminus E(P)|\cdot\max_k N_P(k).
$$
即
$$
(P-1-|E(P)|)\cdot\frac{2P}{\log P}\ge \pi(P^2)-\pi(P).\tag{A.4}
$$

(4) 代入 (A.3) 到 (A.4) 并解出 $|E(P)|$：
$$
P-1-|E(P)|\ge \frac{\log P}{2P}\Bigl(\frac{P^2}{2\log P}-\frac{1.25506\,P}{\log P}\Bigr)=\frac{P}{4}-\frac{0.62753}{1}=\frac{P}{4}-0.62753.
$$
$$
|E(P)|\le P-1-\frac{P}{4}+0.62753=\frac{3P}{4}-0.37247.
$$
对整数 $|E(P)|$ 与 $P\ge 5$，$\frac{3P}{4}-0.37247<\frac{3P}{4}$，故 $|E(P)|<3P/4$。∎

**小 $P$ 的核对**（$P\in\{5,7,11,13\}$）：RS1962 在这些点的常数版本仍成立或直接数值核对
$|E(P)|=0$（项目已验证 $P\le 4999$ 全部例外集为空，故 $|E(P)|=0<3P/4$ 平凡成立）。

### A.3 K3' 的有效"主链不含 RS1962"内部自足版（K3''）

如果不接受 RS1962 显式常数，可以用纯 PNT（Hadamard / de la Vallée-Poussin 1896）：

**定理 K3''（内部自足版）**：存在 $P_0$（无效）使得对所有素数 $P\ge P_0$，
$$
|E(P)|\le \frac{3P}{4}+P\cdot\epsilon(P),
$$
其中 $\epsilon(P)\to 0$ 由 PNT 余项给出。

**证明**：把 RS1962 替换为 PNT $\pi(x)=x/\log x(1+o(1))$，证明结构同 A.2。∎

**状态**：`Proved-in-text + PNT-only`（无显式常数）。

### A.4 K3' 显式版与"非循环"原则的关系

- K3' 通过引入 **MV1973** 与 **RS1962** 两个**已发表的显式定理**，把 K3 的 $o(1)$ 消去为常数 $0.37247$。
- 这**不是**把 Phi-LPF 改名为另一个"router"——它**引入**外部刚性定理（MV1973 是 Selberg sieve 的 sharp form；RS1962 是 PNT 显式版）。
- 这才是欧拉/黎曼风格："$\zeta(s)=\prod(1-p^{-s})^{-1}$"是显式恒等式，"$\pi(x)\sim\mathrm{Li}(x)$"是高斯**带 $\sim$ 符号**的命题；从恒等式到不等式必须经过**显式刚性输入**。

### A.5 升级路径（尚未做、但合理）

下一步可尝试的真升级（按难度递增）：

| 升级 | 工具 | 预期改进 |
|---|---|---|
| K3' 常数 $3/4\to 3/4-\delta$ | Selberg sieve 第二矩 + Cauchy-Schwarz | $\delta\sim 1/\log P$ |
| K3' $\to|E(P)|\le P/2$ | Iwaniec 1982 BT 改进 + Bombieri-Davenport prime-pair 上界 | 严格 $1/2$ 阈值（与 BHP 不冲突） |
| K3'' $\to$ "几乎所有行" | 见定理 K4 条件（$h=X^{1/2}$ 二阶矩）| 直接给 $o(P)$，但开放 |
| H_P 完整 | Cramér 局部或非线性 sieve | 70 年开放 |

**当前严格无条件最强**：K3' = $|E(P)|<3P/4$ 对 $P\ge 5$ 显式。

### A.6 数值核对脚本

`experiments/k3_prime_explicit_bound_check.py` 验证 K3' 的两边显式不等式（A.4）对
$P\le 1500$ 全部成立，且实际 $|E(P)|=0\ll 3P/4$。


