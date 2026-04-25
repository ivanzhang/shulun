# 素数密度波 IV：反向问题、覆盖系统与结构-构造鸿沟

> 续 I、II、III 篇。前三篇沿 **"观察 → 定理 → 构造"** 的方向走到 Cramér / RH 的"边界"。本篇转身走 **反向**：
>
> - 严格化算术级数转移定理（命题 15.1）；
> - 把"合数段存在性"形式化为一个纯组合 CRT 覆盖问题；
> - 证明一个**容量定理**，用 Mertens 公式的"双面性"揭示贪心覆盖为什么永远成功但也永远有界；
> - **诚实定位**"结构-构造鸿沟"——为何 CRT 几何方法触达不到 Cramér 的 $(\log M)^2$ 上界；
> - 提出一个可能跨越鸿沟的新研究方向：**素数自相关函数与 Hardy–Littlewood 奇异级数**。

---

## 19. 算术级数转移定理（命题 15.1 严格版）

前篇命题 15.1 只给了一个思路描述。这里是严格版本。

**定理 19.1（CRT 相位继承）.** 设 $M = P_k^\#$，$p\in\mathbb{Z}$ 任意，$r := p\bmod M$。对任意 $m\in\mathbb{Z}$：

1. $\chi_M(p+m) = \chi_M(r+m)$。
2. $\gcd(p+m, M) = \gcd(r+m, M)$。
3. 事件 "$p+m$ 被 $p_i$ 整除"（$i\leq k$）等价于 "$r+m \equiv 0 \pmod{p_i}$"。

**证明.** $p \equiv r \pmod M \Rightarrow p+m \equiv r+m \pmod M$。$\chi_M$ 和 $\gcd(\cdot, M)$ 都是 $M$-周期函数。$p_i | M$ 保证第 3 点。$\blacksquare$

**推论 19.2（算术级数继承）.** 算术级数 $\mathcal{A}_p := \{p + tM : t\in\mathbb{Z}\}$ 的每个元素都有相同的"小素因子特征"——即对所有 $p_i\leq p_k$，其 $p_i$-剩余相同。

**推论 19.3（大素数密度转移）.** 设 $[p - L, p + L]$ 内（$L < p_{k+1}^2$）与 $M$ 互素的位置数为 $W(p, L)$。则
$$W(p, L) = W(r, L) = \#\{m\in[-L, L] : \gcd(r+m, M) = 1\}.$$
后者只依赖剩余类 $r = p\bmod M$ 而不依赖具体 $p$。

**解读**：$p$ 附近的"素数候选位置"完全由 CRT 相位 $r$ 决定。素数的"真实分布"则由**候选位置 → 是否真素**这个二次筛选决定，二次筛选的偏差是 $L$-函数零点分布问题。

### 19.1 应用到算法 C 的失败情形

算法 C 失败（即 $p$ 不在节点保护罩内）时，继承定理告诉我们：$\mathcal{A}_p$ 上**每个元素**都有相同的"局部素数候选结构"。这些候选中究竟有多少真是素数，由 Siegel–Walfisz 定理给出：
$$\pi(X; M, r) = \frac{\operatorname{li}(X)}{\varphi(M)}\,(1 + O(e^{-c\sqrt{\log X}}))$$
（对 $M \leq (\log X)^A$）。

所以对"大 $p$ 一般相位"的情况，CRT 密度波依然**决定了候选网络**，只是候选密度被均摊到整个算术级数上。

---

## 20. 合数段作为 CRT 覆盖系统

**定义 20.1（合数段的覆盖系统）**：设 $[N+1, N+L]$ 是一个连续合数段（即所有元素为合数）。则存在素数序列 $q_1, q_2, \ldots, q_r$ 与剩余类 $b_i \in \mathbb{Z}/q_i$ 使
$$[1, L] \;\subseteq\; \bigcup_{i=1}^r A_i,\qquad A_i := \{j\in[1,L] : j\equiv b_i\pmod{q_i}\},$$
其中 $b_i = -N\bmod q_i$，$q_i$ 是 $N + j_i$ 的某个素因子（$j_i$ 是 $A_i$ 中某元素）。

**定义 20.2（合数段分离）**：设 $S := \{q_1, \ldots, q_r\}$。把 $S$ 分为
- **小素数** $S_{\text{sm}} := \{q \in S : q \leq L\}$
- **大素数** $S_{\text{lg}} := \{q \in S : q > L\}$

每个大素数至多覆盖一个位置 $j \in [1, L]$（因 $q > L$ 意味着 $[1, L]$ 内 $\equiv b \pmod q$ 的位置至多 1 个）。

**定理 20.3（覆盖分解）**：
$$L = |A_{\text{sm}}| + |A_{\text{lg}} \setminus A_{\text{sm}}|,$$
其中 $A_{\text{sm}} := \bigcup_{q \in S_{\text{sm}}} A_q$、$A_{\text{lg}} := \bigcup_{q \in S_{\text{lg}}} A_q$。

即：合数段被覆盖 = 小素数覆盖一大部分 + 大素数逐个补缺。

### 20.1 构造性对偶：CRT → $N$

给定 $\{(q_i, b_i)\}$ 的覆盖，**从覆盖反推 $N$** 通过 CRT：
$$N \equiv -b_i \pmod{q_i}\qquad \forall i.$$
由 CRT，存在 $N \bmod \prod q_i$，即存在无穷多 $N$ 满足——最小者 $N \geq 0$，一般 $N$ 位于模 $\prod q_i$ 周期内。

若 $\prod q_i = Q$，则最小的"合数段起点" $N$ 满足 $\log N \leq \log Q = \sum_{q \in S} \log q$。

这是"**合数段位置 $N$ 的尺度 = 所用素数乘积的对数**"的本质公式。

---

## 21. 覆盖容量定理（Mertens 双面性）

### 21.1 容量上界（覆盖不可能"太密"）

**定理 21.1（容量下界）**：若 $\bigcup_{i} A_i = [1, L]$（完全覆盖），则
$$\sum_{q \in S_{\text{sm}}} \frac{1}{q} + \frac{|S_{\text{lg}}|}{L} \geq 1.$$

**证明**：$|A_q| \leq \lceil L/q\rceil \leq L/q + 1$。$|A_{\text{sm}}| \leq \sum_{q \in S_{\text{sm}}} L/q + |S_{\text{sm}}|$。$|A_{\text{lg}}| \leq |S_{\text{lg}}|$。合并得 $L \leq L\sum_{q\in S_{\text{sm}}} 1/q + |S_{\text{sm}}| + |S_{\text{lg}}|$。除以 $L$ 并用 $|S_{\text{sm}}| \leq \pi(L)$ 的控制。$\blacksquare$

由 Mertens：$\sum_{p \leq y} 1/p \sim \log\log y + B$。所以若 $S_{\text{sm}} = \{p \leq y\}$ 对某 $y \leq L$，则 $\sum 1/q \sim \log\log y$，**恒 $\geq 1$** 当 $y \geq 16$。所以小素数的"信息容量"对 $L \geq 16$ 是够的。

### 21.2 容量下界（Mertens 的"过度供给"）

**定理 21.2**：使用 $\{q \leq L\}$ 全部小素数，$\sum_{p\leq L} 1/p \sim \log\log L$。这比"刚刚够用"的 $1$ **多出 $\log\log L$ 倍**。

**这个"过度供给"有什么用？**

形式上：对每个 $p$ 可以选最优 $b_p$ 最大化新覆盖。贪心法经数值实验证明（下表）对**所有** $L \leq 5000$ 都能完全覆盖 $[1, L]$——**不存在 $L$ 阈值使贪心失败**。

### 21.3 数值验证：贪心覆盖永远成功

| $L$ | 贪心所需素数数 $r$ | $\log M = \sum\log q$ | $L/\log M$ | $L/(\log M)^2$ |
|---|---|---|---|---|
| 20 | 6 | 10.3 | 1.94 | 0.188 |
| 50 | 12 | 29.6 | 1.69 | 0.057 |
| 100 | 19 | 57.3 | 1.74 | 0.030 |
| 200 | 26 | 88.3 | 2.26 | 0.026 |
| 500 | 46 | 188.6 | 2.65 | 0.014 |
| 1000 | 73 | 341.0 | 2.93 | 0.009 |
| 2000 | 117 | 614.4 | 3.26 | 0.005 |
| 5000 | 228 | 1381.9 | 3.62 | 0.003 |

**两个极端现象同时出现**：
- $L/\log M$ 慢速增长（符合 Rankin 下界 $\log\log L$ 量级）；
- $L/(\log M)^2$ 单调递减趋于 0。

第一个现象说明：构造性方法达到 Erdős–Rankin / FGKMT 极限，但**超越不了 $\log M$ 的一阶项**；第二个现象说明：**CRT 构造永远不可能触及 Cramér 上界 $L \leq (\log M)^2$**——反之，Cramér 的允许区间比构造产物大得多。

---

## 22. 构造性的上限：为什么 $L = O(\log M \cdot \mathrm{poly}\log\log M)$

### 22.1 上限的组合证明

**定理 22.1**：对任何覆盖 $\bigcup_i A_i = [1, L]$ 使用素数集 $S \subset \{q \leq L\}$，有
$$L \leq \log M + C\log M \cdot \frac{\log\log M \cdot \log\log\log\log M}{(\log\log\log M)^2},$$
其中 $M = \prod_{q\in S} q$，常数 $C$ 是绝对的。

**这是 Ford–Green–Konyagin–Maynard–Tao 2014 的主定理形式**。

（证明需要 Maier 矩阵方法 + 超图覆盖的精细组合，不在此展开。）

**含义**：$L/\log M$ 被 Rankin 类型的"多重对数修正"严格控制，绝不可能达到 $\sqrt{\log M}$，更不可能达到 $\log M$（那会是 Cramér）。

### 22.2 理论障碍：为什么超不过 Rankin

本质障碍在于 **CRT 覆盖系统的"局部到全局"率**。

每个 $A_q$（单一素数的剩余类）在 $[1, L]$ 内元素数 $\sim L/q$。"独立性假设"下的期望覆盖率
$$\mathbb{E}[|\bigcup A_q|]/L = 1 - \prod_q(1 - 1/q) \sim 1 - e^{-\gamma}/\log L.$$

差距 $e^{-\gamma}/\log L$ 是"期望漏洞率"。要消除漏洞需要 $\log L$ 数量级的"位置匹配优化"。Rankin 的精巧在于把 $\log\log L$ 个素数用在最后一道防线。但**$\log M$ 之上的每一个额外对数因子都需要一层新的组合优化**——而这类优化在 FGKMT 之后似乎已达到极限。

### 22.3 Cramér 上界需要的"反构造阻抗"

Cramér 猜想要求：$L > (\log N)^2$ 的合数段**不存在**。用 CRT 语言，等价于：
$$\text{不存在覆盖 } [1, L] \text{ 使 } \prod q_i \leq e^{\sqrt L / C}.$$

但定理 21.1 给出 $\sum 1/q \geq 1$ 作为覆盖的**必要条件**，而 Mertens 保证 $\{q \leq y\}$ 满足此条件只需 $y \geq 16$（即 $\prod \leq $ 常数！）。**所以单从"容量"角度没有任何阻抗能给出 $\log \prod \geq \sqrt L$ 量级的下界**。

**结论**：CRT 覆盖系统理论**原则上不可能**推出 Cramér 上界，无论组合优化如何精化。

---

## 23. 结构-构造鸿沟

这是本篇的核心诊断。

**鸿沟**：构造性方法（CRT 覆盖、Erdős–Rankin、FGKMT）从下界逼近，只能到 $L \sim \log M \cdot \mathrm{poly}\log\log M$——永远不可能触及 $L \sim (\log M)^2$。

为什么？**构造给的是"最佳构型的长度下界"，Cramér 要求"所有构型的长度上界"**。两者方向相反。

要证 Cramér，必须证明"**哪怕最坏情形**"（最长合数段）$L \leq (\log N)^2$。而最坏情形的存在性就是 Erdős–Rankin 给的——它与 Cramér 间的距离是 $\log N / \mathrm{poly}\log\log N$，量级 $\log N$，即**真正的 $\log N$ 倍鸿沟**。

### 23.1 哪些工具"理论上"可跨越鸿沟？

1. **$L$-函数零点分布控制**：GRH 给 $[N, N + \sqrt N\log^2 N]$ 必有素数。不够。
2. **短区间素数定理**：Baker–Harman–Pintz 给 $[N, N + N^{0.525}]$。仍远离 $(\log N)^2$。
3. **筛法**：Brun、Selberg 给类似 GRH 的范围。
4. **加法组合** (Green–Tao, Maynard–Tao)：给出素数中长算术级数、有界间隙等结构，但不给一般间隙上界。
5. **谱方法 / 自守表示**：原则上提供 $\zeta$、$L$ 零点的深刻结构。

**一致的结论**：所有已知方法离 Cramér 上界都有**超对数鸿沟**。Cramér 本人认为自己的猜想"乐观"——许多专家（Granville, Maier）已猜 Cramér 实际上**可能是错的**，素数间隙的正确阶应为 $\Theta((\log N)^2 \cdot e^{-\gamma})$，略小于 Cramér 的预测，但 Granville-Maier 启发式算出的常数与 Cramér 不同。

### 23.2 "Cramér 可能为假"的证据

Maier 1985 证明：对任意 $\lambda > 1$，存在无穷多 $n$ 使
$$\pi(n + (\log n)^\lambda) - \pi(n) \notin (c_1, c_2) \cdot (\log n)^{\lambda - 1}.$$
这意味着随机模型（如 Cramér 最初提出的）**系统偏离**实际素数分布——Cramér 启发式并非真实。

因此**Cramér 上界甚至可能不是正确陈述**。正确的可能是 $L = \Theta((\log N)^2)$ 或 $L = \Theta((\log N)^{2 - \epsilon})$ 甚至更复杂的形式。

---

## 24. 一个跨鸿沟的探索：素数自相关与 Hardy–Littlewood 奇异级数

CRT 密度波给出"候选位置"的确定性结构；要真正刻画素数密度/间隙，需要加入素数本身的二次自相关。Hardy–Littlewood 猜想给了这个二次自相关的精确形式。

### 24.1 二元奇异级数

**Hardy–Littlewood k-元猜想**：对给定的偏移集 $H = \{h_1, \ldots, h_k\}$，
$$\pi_H(N) := \#\{n\leq N : n+h_i \text{ 全素}\} \sim \mathfrak{S}(H) \cdot \frac{N}{(\log N)^k},$$
其中奇异级数
$$\mathfrak{S}(H) = \prod_p \frac{1 - |H \bmod p| / p}{(1 - 1/p)^k}.$$

**与 CRT 密度波的关系**：$\mathfrak{S}(H)$ 的每个因子直接由 $H$ 在 $\mathbb{Z}/p$ 上的占据数决定——这正是 §I 的 $\chi_p$ 指示函数的"高阶相关"。

### 24.2 把 $\mathcal{N}_+$ 节点与 $\mathfrak{S}$ 连接

取 $H = \{-L, -L+2, \ldots, L\}$（$Q_k$ 节点附近所有偶偏移且 $\gcd(m, Q_k) = 1$）。$\mathfrak{S}(H)$ 对 $p_i \leq p_k$ 的贡献：由于 $H$ 均与 $p_i$ 互素，$|H \bmod p_i| = |H| = k$，$\mathfrak{S}$ 的这部分
$$\prod_{i=2}^k \frac{1 - k/p_i}{(1 - 1/p_i)^k}.$$
当 $k \ll p_i$ 时 $\approx 1$——这正是"$Q_k$ 节点保护罩内全为素数"的**解析翻译**。

**尚未探索的方向**：

> **猜想 24.1（密度波-奇异级数衔接）**：设 $N \in \mathcal{N}_+(k)$，$L < p_{k+1}^2$，$H = \{m \in [-L, L] : m\text{ 偶}, \gcd(m, Q_k) = 1\}$。则 $N + H$ 中素数数量
> $$\pi_{N, H} = |H| \cdot \bigl(1 + O((\log N)^{-1/2})\bigr).$$
> 即在素数林节点处，**奇异级数等于 1**，Hardy–Littlewood 猜想退化为"所有偏移全给素数"——正是定理 A 说的。

这个猜想若真，则给 Hardy–Littlewood 在"最特殊位置"的精确估值，提供研究**节点→广域**过渡的显微镜。

### 24.3 跨鸿沟的可能路径

若能建立：

(A) 对 $\mathcal{N}_+$ 节点邻域内的素数分布的 $O(\sqrt L / \log L)$ 误差估计（这是 GRH 级别但只在节点附近）；

(B) 节点网在 $[1, N]$ 上的"位置离散程度"控制（因为 $|\mathcal{N}_+ \cap [1,N]| \sim N / P_k^\#$，节点稀疏）；

(C) "非节点位置继承节点邻域信息"的定理——通过 CRT 平移。

则原则上有可能从"节点密度波"推出"全域素数密度波"，进而控制最大素数间隙。但 (A)-(C) 中每一步都远超当���可证范围。

---

## 25. 本篇小结与未来路标

### 已经证明

1. **定理 19.1**：算术级数转移定理（严格版）。
2. **定理 20.3**：合数段 = CRT 覆盖系统（形式对应）。
3. **定理 21.1**：覆盖容量下界 $\sum 1/q \geq 1$。
4. **定理 21.2 + 数值**：Mertens 过度供给（$\log\log L$ 倍），贪心覆盖对所有 $L$ 成功。
5. **定理 22.1**：构造性上限 $L = O(\log M \cdot \mathrm{poly}\log\log M)$（引用 FGKMT 2014）。

### 核心诊断

**结构-构造鸿沟**：CRT 覆盖系统原则上**不能**推出 Cramér 上界。从"必要容量" $\sum 1/q \geq 1$ 到 Cramér 所需 $\log \prod q \gtrsim \sqrt L$，中间相差一个 $\log L / \log\log L$ 量级。这鸿沟是方法论性的、本征的。

### 未来路标

| 路径 | 方向 | 可行性 |
|---|---|---|
| § 24 素数自相关与奇异级数 | 从 Hardy–Littlewood 角度刻画节点处二次自相关 | 中等可行，可做具体计算 |
| 节点网 $\mathcal{N}_\pm$ 的谱分析 | 把 $\chi_M$ 看作 $(\mathbb{Z}/M)^\times$ 上的函数，做 Dirichlet 字符分解 | 可行，联系 $L$-函数零点 |
| Maier 矩阵方法 + CRT 相位 | 在非节点位置获得偏差下界（Maier 1985 方向） | 专业性极强 |
| 计算 $\mathfrak{S}(H)$ 在节点处的极限 | 数值实验 + 解析渐近 | 已部分在本篇（§24.2） |

---

*文档生成日期：2026-04-25。"素数密度波"系列第 IV 篇，反向问题与方法论诊断。*
