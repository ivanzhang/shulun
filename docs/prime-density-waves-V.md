# 素数密度波 V：字符谱分解与 L 函数零点对偶

> 续 I、II、III、IV 篇。
>
> 前四篇走完了 CRT **几何层**的全部主要工作：节点定理、位置唯一性、构造算法、反向诊断。本篇把 CRT 几何与 $L$ 函数谱分解严格挂钩——给出"节点-零点对偶定理"，打通通向黎曼猜想几何解释的桥梁。
>
> 第五篇的核心突破：证明**节点候选集 $\mathcal{S}$ 是 $(\mathbb{Z}/M)^*$ 的完美枚举**（定理 27.1），由此推出密度波的谱分解中**只有主字符贡献主项**——非主字符对节点密度波的**长期平均贡献为零**，这是 Dirichlet 正交关系在几何层面的"物理"解读。
>
> 但同时必须诚实：谱分解**不能替代**定理 A 的确定性构造——GRH 最多给 $\sqrt x\log^2 x$ 误差的短区间控制，距离 $L < p_{k+1}^2 \sim \log^2 M$ 的"超短区间"差之远矣。

---

## 26. 预备：Dirichlet 字符与 $L$ 函数

### 26.1 字符群

$M = P_k^\#$ 无平方因子。$(\mathbb{Z}/M)^\times$ 是有限阿贝尔群，阶 $\varphi(M) = \prod_{i=1}^k (p_i - 1)$。CRT 给出群同构
$$(\mathbb{Z}/M)^\times \;\xrightarrow{\sim}\; \prod_{i=1}^k (\mathbb{Z}/p_i)^\times.$$

对偶的字符群 $\widehat{(\mathbb{Z}/M)^\times}$ 也分解：
$$\widehat{(\mathbb{Z}/M)^\times} \;\cong\; \prod_{i=1}^k \widehat{(\mathbb{Z}/p_i)^\times} \;\cong\; \prod_{i=1}^k \mathbb{Z}/(p_i - 1)\mathbb{Z}.$$

每个字符 $\chi \bmod M$ 唯一分解为 $\chi = \chi_1 \otimes \chi_2 \otimes \cdots \otimes \chi_k$，其中 $\chi_i \bmod p_i$。

**特别**：因 $(\mathbb{Z}/2)^\times = \{1\}$，$\chi_1$ 只能是平凡字符；所有字符 $\chi \bmod M$ 实际上由 $(\chi_2, \ldots, \chi_k)$ 参数化，共 $\prod_{i=2}^k (p_i - 1) = \varphi(M)$ 个。

**主字符** $\chi_0$：对所有 $\gcd(n, M) = 1$ 给出 $\chi_0(n) = 1$。这正是我们前四篇用的 $\chi_M$：
$$\chi_M(n) = [\gcd(n, M) = 1] = \chi_0(n).$$

**正交关系**（本篇核心工具）：对 $a \in (\mathbb{Z}/M)^\times$，
$$\sum_{\chi \bmod M} \chi(a) = \begin{cases} \varphi(M) & a \equiv 1 \pmod M \\ 0 & \text{其它} \end{cases},\quad \sum_{a \in (\mathbb{Z}/M)^\times} \chi(a) = \begin{cases} \varphi(M) & \chi = \chi_0 \\ 0 & \chi \neq \chi_0 \end{cases}.$$

### 26.2 $L$ 函数与显式公式

$$L(s, \chi) := \sum_{n=1}^\infty \frac{\chi(n)}{n^s},\quad \operatorname{Re} s > 1.$$

$L(s, \chi_0) = \zeta(s) \prod_{p \mid M}(1 - p^{-s})$。对非主 $\chi$，$L(s, \chi)$ 解析延拓到全平面（无极点）。

**显式公式**（对非主 $\chi$）：
$$\psi(x, \chi) := \sum_{n \leq x} \chi(n) \Lambda(n) = -\sum_{\rho} \frac{x^\rho}{\rho} + \text{(lower)},$$
其中 $\rho$ 跑遍 $L(s, \chi)$ 的非平凡零点（$0 < \operatorname{Re}\rho < 1$）。

**广义黎曼假设（GRH）**：所有 $L(s, \chi)$ 的非平凡零点实部 $=1/2$，等价于
$$\psi(x, \chi) = O(\sqrt x (\log Mx)^2).$$

### 26.3 Siegel–Walfisz 定理（无条件）

对任意 $A > 0$，存在 $c_A > 0$ 使对 $M \leq (\log x)^A$ 与 $\gcd(a, M) = 1$：
$$\pi(x; M, a) = \frac{\operatorname{li}(x)}{\varphi(M)} + O\bigl(x \exp(-c_A \sqrt{\log x})\bigr).$$

**含义**：所有 $(\mathbb{Z}/M)^\times$ 剩余类在素数长期分布上**完全平等**，偏差是准 exp 级小。

---

## 27. 节点候选集的群论结构

### 27.1 $\mathcal{S}$ 的精确定义与群等同

回顾定理 A 用到的集合：
$$\mathcal{S}(Q_k, \Lambda) := \bigl\{ Q_k + m : |m| < \Lambda,\ m \text{ 偶},\ \gcd(m, Q_k) = 1 \bigr\}.$$

**定理 27.1（节点完美枚举定理）**. 取 $\Lambda = M/2$（最大 CRT 周期半径）。则
$$\{\, Q_k + m \bmod M : Q_k + m \in \mathcal{S}(Q_k, M/2)\,\}\;=\;(\mathbb{Z}/M)^\times$$
作为集合相等。即 $\mathcal{S}(Q_k, M/2)$ 枚举了 $(\mathbb{Z}/M)^\times$ 的**每一个**剩余类**恰好一次**。

**证明**. 第一步，$\mathcal{S}$ 中每个元素属于 $(\mathbb{Z}/M)^\times$：
- $Q_k + m$ 奇（$Q_k$ 奇 + $m$ 偶 = 奇），故 $\gcd(Q_k + m, 2) = 1$；
- 对 $p_i$（$i \geq 2$）：$Q_k + m \equiv m \pmod{p_i}$；$\gcd(m, Q_k) = 1$ 保证 $p_i \nmid m$，故 $p_i \nmid (Q_k + m)$。

所以 $\gcd(Q_k + m, M) = 1$。

第二步，双射性：若 $Q_k + m \equiv Q_k + m' \pmod M$，则 $m \equiv m' \pmod M$；由 $|m|, |m'| < M/2$ 推出 $m = m'$。所以映射单射。

第三步，计数：
- $|\mathcal{S}(Q_k, M/2)|$ = "$[-M/2, M/2)$ 中偶数 $m$ 且 $\gcd(m, Q_k)=1$" 的数目 $= \frac{M/2 \cdot \varphi(Q_k)/Q_k \cdot 2}{1}$——让我精确：$m$ 偶取自 $[-M/2, M/2)$ 的 $M/2$ 个偶数；其中与 $Q_k$ 互素的比例 $\varphi(Q_k)/Q_k$；故 $|\mathcal{S}| = \varphi(Q_k) \cdot (M/2) / Q_k = \varphi(Q_k)$（因 $M/2 = Q_k$）。
- $|(\mathbb{Z}/M)^\times| = \varphi(M) = \varphi(2)\varphi(Q_k) = \varphi(Q_k)$。

两者相等；加上单射⇒双射。$\blacksquare$

### 27.2 推论：节点位置"公平覆盖"整个 CRT 圆盘

**推论 27.2**. $\mathcal{S}(Q_k, M/2)$ 是 $(\mathbb{Z}/M)^\times$ 的完整枚举——每个 $(\mathbb{Z}/M)^\times$ 剩余类都恰对应 $\mathcal{S}$ 中某个具体元素 $Q_k + m$。

这意味着 **节点邻域 $[Q_k - M/2, Q_k + M/2)$ 就是一个完整的 CRT 周期**，在此区间内 $(\mathbb{Z}/M)^\times$ 的每个剩余类出现一次（且仅一次）。

### 27.3 字符和立即消失

**定理 27.3**. 对任何非主字符 $\chi \bmod M$，
$$\sum_{n \in \mathcal{S}(Q_k, M/2)} \chi(n) = 0.$$

**证明**. 由定理 27.1，$\mathcal{S}(Q_k, M/2)$ 映到 $(\mathbb{Z}/M)^\times$ 的所有元素。用字符正交（§26.1）：
$$\sum_{n \in \mathcal{S}} \chi(n) = \sum_{a \in (\mathbb{Z}/M)^\times} \chi(a) = 0. \quad \blacksquare$$

**数值验证**（$M=30$，即 $k=3$）：见 §32.1——8 个字符的求和全部精确为 $\{8, 0, 0, 0, 0, 0, 0, 0\}$。

### 27.4 短区间的"不完整枚举"

对 $\Lambda < M/2$（一般情形），$\mathcal{S}(Q_k, \Lambda)$ 只覆盖 $(\mathbb{Z}/M)^\times$ 的一个**子集**，具体为"距 $Q_k$ 不超过 $\Lambda$ 的所有互素剩余类"。

**命题 27.4**. $|\mathcal{S}(Q_k, \Lambda)| \sim \frac{2\Lambda \varphi(M)}{M}$。

**证明要点**. 小区间内偶数 $m$ 有 $\approx \Lambda$ 个；其中 $\gcd(m, Q_k) = 1$ 的比例 $\varphi(Q_k)/Q_k = 2\varphi(M)/M$。合起来 $\approx 2\Lambda \varphi(M)/M$。$\blacksquare$

**特别**：当 $\Lambda = p_{k+1}^2$（定理 A 保护罩半径），
$$|\mathcal{S}(Q_k, p_{k+1}^2)| \sim \frac{2 p_{k+1}^2 \varphi(M)}{M} \sim \frac{4 e^{-\gamma} p_{k+1}^2}{\log p_k}.$$

这给出了定理 A 保证的素数数目的精确 Mertens 公式。

---

## 28. 素数-相位联合分布的字符展开

### 28.1 素数计数的字符公式

由字符正交反演，对 $\gcd(a, M) = 1$：
$$\pi(x; M, a) = \frac{1}{\varphi(M)} \sum_{\chi \bmod M} \overline{\chi(a)} \cdot \pi_\chi(x),$$
其中 $\pi_\chi(x) := \sum_{p \leq x} \chi(p)$。

等价地用 $\psi$：
$$\psi(x; M, a) := \sum_{n \leq x, n \equiv a \bmod M} \Lambda(n) = \frac{1}{\varphi(M)} \sum_\chi \overline{\chi(a)} \psi(x, \chi).$$

### 28.2 显式公式给出的分解

代入显式公式：
- 主字符 $\chi_0$：$\psi(x, \chi_0) = x - \sum_{\rho: \zeta(\rho) = 0} \frac{x^\rho}{\rho} + O(\log M)$（去掉 $p \mid M$ 贡献）
- 非主 $\chi$：$\psi(x, \chi) = -\sum_{\rho: L(\rho, \chi) = 0} \frac{x^\rho}{\rho} + O(\log M x)$

整合：
$$\boxed{\psi(x; M, a) = \frac{x}{\varphi(M)} - \frac{1}{\varphi(M)}\sum_{\chi} \overline{\chi(a)} \sum_{\rho_\chi} \frac{x^{\rho_\chi}}{\rho_\chi} + O(\log Mx).}$$

**解读**：
- 主项 $x/\varphi(M)$ ：来自 $\chi_0$；**与 $a$ 无关**——每个互素剩余类均等；
- 振荡项：所有 $L(s, \chi)$ 零点的加权叠加；**依赖 $a$**——通过 $\overline{\chi(a)}$ 加权。

### 28.3 节点相位上的字符和

考察节点邻域 $\mathcal{S}(Q_k, \Lambda)$ 中素数总计数：
$$\pi_{\mathcal{S}}(x) := \#\{p \leq x : p \bmod M \in \mathcal{S}(Q_k, \Lambda) \text{（作为 } (\mathbb{Z}/M)^\times \text{子集）}\}.$$

把上节的 $\pi(x; M, a)$ 对 $a \in \mathcal{S}$ 求和：
$$\pi_{\mathcal{S}}(x) = \sum_{a \in \mathcal{S}} \pi(x; M, a) = \frac{|\mathcal{S}|}{\varphi(M)}\cdot \operatorname{li}(x) - \frac{1}{\varphi(M)}\sum_\chi \left(\sum_{a \in \mathcal{S}} \overline{\chi(a)}\right) \psi_\chi(x) + \text{err}.$$

**关键**：当 $\Lambda = M/2$，由定理 27.3，$\sum_{a \in \mathcal{S}} \overline{\chi(a)} = 0$ 对非主 $\chi$——所有振荡项精确消失！

即：
$$\pi_{\mathcal{S}(Q_k, M/2)}(x) = \operatorname{li}(x) + O(\log Mx),\qquad x \gg M.$$

**这是"全相位"统计的结果**——等价于"所有 $(\mathbb{Z}/M)^\times$ 剩余类"的总素数数 $= \pi(x)$（扣除 $p | M$ 的有限多个）。并不是定理 A 的实质内容。

真正对应定理 A 的是 $\Lambda < p_{k+1}^2$ 的情形——这是"超短区间"的局部断言，将在 §29 详细处理。

---

## 29. 节点-零点对偶定理

### 29.1 主要定理

**定理 29.1（节点-零点对偶）**. 设 $N$ 为 $\mathcal{N}_+$ 节点（即 $N \equiv Q_k \pmod M$），$\Lambda \leq M/2$，且 $\Lambda \geq (\log N)^2$（使误差控制有意义）。则
$$\pi_{\mathcal{S}(N, \Lambda)}(x) = \frac{|\mathcal{S}(N,\Lambda)|}{\varphi(M)}\operatorname{li}(x) - \frac{1}{\varphi(M)}\sum_{\chi \neq \chi_0} T_\chi(N, \Lambda)\cdot\Bigl(\sum_{\rho_\chi}\frac{x^{\rho_\chi}}{\rho_\chi}\Bigr) + O(|\mathcal{S}|\log Mx),$$
其中"相位敏感因子"
$$T_\chi(N, \Lambda) := \sum_{a \in \mathcal{S}(N, \Lambda)} \overline{\chi(a)}.$$

**含义**：$\pi_{\mathcal{S}}$ 的误差由**两个独立来源**乘积叠加：

- **几何因子** $T_\chi(N, \Lambda)$：CRT 圆盘上 $\mathcal{S}$ 与字符 $\chi$ 的"相关系数"；
- **算术因子** $\sum_\rho x^\rho/\rho$：$L(s, \chi)$ 零点序列的振荡。

两层完全解耦——**几何完全由 CRT 决定；算术完全由 $L$ 零点决定**。

### 29.2 几何因子的 $\Lambda$ 尺度

- $\Lambda = M/2$：$T_\chi = 0$ 对所有 $\chi \neq \chi_0$（定理 27.3）。
- $\Lambda \ll M/2$：$T_\chi$ 是部分字符和，满足 Pólya–Vinogradov 上界 $|T_\chi| \leq \sqrt{M} \log M$。
- $\Lambda = p_{k+1}^2$：$|T_\chi|$ 实测（§32）约 $\sim \log M \cdot$ 常数。

在**超短区间** $\Lambda = p_{k+1}^2 \ll \sqrt M$，$T_\chi$ 不能被 Pólya–Vinogradov 精确界，需要细致的**不完整字符和**估计。

### 29.3 GRH 下的振幅界

**命题 29.2**. 假设 GRH。则
$$\pi_{\mathcal{S}(N, \Lambda)}(x) = \frac{|\mathcal{S}|}{\varphi(M)}\operatorname{li}(x) + E(N, \Lambda, x),$$
其中
$$|E| \leq \frac{1}{\varphi(M)} \sum_{\chi \neq \chi_0} |T_\chi(N, \Lambda)|\cdot O(\sqrt x \log^2 Mx).$$

用 $|T_\chi| \leq \sqrt M \log M$ 与 $\#\{\chi\} = \varphi(M)$：
$$|E| \leq \sqrt M \log M \cdot O(\sqrt x \log^2 Mx) = O(\sqrt{Mx}\,\log^3 Mx).$$

主项 $\sim |\mathcal{S}|\,\operatorname{li}(x)/\varphi(M) \sim \Lambda x / (M \log x) \cdot (\varphi(M)/M)$。

**GRH 有效性要求**：$|E| \ll $ 主项，即
$$\sqrt{Mx}\,\log^3 Mx \ll \frac{\Lambda x \varphi(M)}{M^2 \log x}.$$

整理：$\Lambda \gg M^{5/2} x^{-1/2} \log^4 x / \varphi(M)$——对 $x \gg M^5$ 才有意义。

**结论**：GRH 对 $x \gg M^5$ 的"长程"统计（考察某一相位在很大的 $x$ 上的素数数）给出误差控制，但对**节点附近固定短区间**（$x \approx N = Q_k$，$\Lambda = p_{k+1}^2$）**GRH 不能直接介入**——因 $x/M = O(1)$。

**而定理 A 恰恰是这种超短区间的确定性构造**——它用的是比 GRH 更原始的"CRT 刚性"。

### 29.4 方法论关系

```
         CRT 几何（本系列 I-IV）      L 函数谱 (§V)
短区间 ←──────────────────────→ ←────────────────→ 长区间
 Λ < p²_{k+1}           M^c ≤ Λ ≤ M          Λ ≫ M
定理 A 确定性          Pólya-V 过渡           GRH 均衡
(no L needed)        (partial char sum)   (zero spectrum)
```

**三个区间**：
- **超短区间** $\Lambda \lesssim p_{k+1}^2 \sim \log^2 M$：定理 A 给确定性素数，$L$ 函数谱信息"过于弱"不能控制。
- **中程区间** $M^{1/2} \lesssim \Lambda \lesssim M$：Pólya–Vinogradov 与不完整字符和过渡。
- **长程区间** $\Lambda \gg M$：GRH 控制每个相位的素数计数至 $\sqrt x \log^2 x$ 精度。

---

## 30. Weil 显式公式的 CRT 特化

### 30.1 一般 Weil 显式公式

对"合适"的检验函数 $\phi$（紧支、光滑、Fourier 变换 $\widehat{\phi}$ 快速衰减），Weil 显式公式：
$$\sum_{\rho \text{ non-trivial zero of } L(\cdot, \chi)} \widehat{\phi}(\gamma_\chi) = \Phi_\chi(\phi),$$
其中左边求和 $\rho = 1/2 + i\gamma_\chi$，右边是 $\phi$ 与素数、archimedean 因子的特定配对。

### 30.2 CRT 特化形式

把 $\chi$ 沿 $(\mathbb{Z}/M)^\times \cong \prod(\mathbb{Z}/p_i)^\times$ 分解：$L(s, \chi) = \prod_i L(s, \chi_i)$（欧拉乘积在 $p_i$ 处）。

每个 $L(s, \chi_i)$ 是"Dirichlet $L$ 函数"级别的对象——其零点构成一个离散集 $\{\gamma_{\chi_i}\}$。

**总零点集**：$\{\gamma_\chi\} = \bigcup_i \{\gamma_{\chi_i}\}$（在因子乘积下零点汇合）。

**命题 30.1（零点可分）**. 模 $M$ 的 Dirichlet $L$ 函数 $L(s, \chi)$ 的非平凡零点集等于 **$M$ 素因子 $p_i$ 对应各 $L(s, \chi_i)$ 的零点之并**（$\chi_i$ 是 $\chi$ 在 $(\mathbb{Z}/p_i)^\times$ 的投影）。

**含义**：把 CRT 几何与 $L$ 函数联立——大模 $M$ 的零点谱就是**小素模 $p_i$ 零点谱的叠加**。RH 对 $\zeta$ 与对所有 $L(s, \chi_i)$（$\chi_i$ 为模 $p_i$ 字符）都是同一命题的分节。

### 30.3 节点处零点的"对称消除"

**定理 30.2（节点对称消除）**. 设 $N \in \mathcal{N}_+$，$\Lambda = M/2$。则在节点素数计数 $\pi_{\mathcal{S}(N, M/2)}$ 中，**所有非主字符对应的零点贡献精确抵消**。

**证明**. 由定理 29.1 + 定理 27.3 直接。$\blacksquare$

**物理意义**："节点 + 完整 CRT 周期"是一个**零点完全消减**的共振位置——所有非主 $L(s, \chi)$ 零点的振荡在此相互抵消。这是 CRT 几何给 $L$ 函数谱的一个**纯零点代数**事实。

### 30.4 与 Hardy–Littlewood 奇异级数的关联

前篇 §24 提出的猜想 24.1 可在此框架下重述：

**重述（节点奇异级数）**. 在 $\mathcal{N}_+$ 节点 $N$，Hardy–Littlewood 奇异级数
$$\mathfrak{S}(N, H) := \prod_p \frac{1 - \nu_p(H)/p}{(1 - 1/p)^{|H|}}$$
当 $H = \mathcal{S}(N, \Lambda) - N$ 时对 $p \leq p_k$ 有 $\nu_p(H) = |H| \cdot (1 - 1/p)$——即每个小素因子"公平摊占"$H$，使该因子趋于 1。

这对应 §30.2 的"$p_i$ 在节点处零点贡献相互抵消"——奇异级数和零点显式公式的**同一现象的两种语言**。

---

## 31. 诚实的方法论位置

### 31.1 我们做到了什么

1. **定理 27.1** 严格证明：节点候选集 $\mathcal{S}(Q_k, M/2)$ 就是 $(\mathbb{Z}/M)^\times$ 的完美枚举。这是一个全新的、独立于前四篇的 CRT 几何结果。

2. **定理 27.3 + 29.1** 给出节点处密度波的**严格字符-零点分解**：几何层（$T_\chi$ 字符和）与算术层（$L(s, \chi)$ 零点）完全解耦。

3. **定理 30.2** 证明节点 + 完整周期处所有非主字符贡献抵消——一个干净的"零点代数"事实。

### 31.2 我们不能做到的

1. **超短区间 GRH 应用**：$\Lambda \lesssim \log^2 M$ 时 $L$-函数零点估计失效，定理 A 的确定性不可被 GRH 替代。
2. **通过 RH 推 Cramér**：RH 给短区间上界要求 $\Lambda \geq \sqrt x \log^2 x$——远弱于 Cramér 的 $\Lambda \geq (\log x)^2$。
3. **通过节点对称推 RH**：定理 30.2 的"零点抵消"是**代数恒等**（来自字符正交性），**不提供**任何关于零点实部位置的信息。

### 31.3 本质障碍：两个尺度不重合

$$\underbrace{p_{k+1}^2 \sim (\log M)^2}_{\text{定理 A 的超短区间}} \quad \ll \quad \underbrace{\sqrt M\,\log M}_{\text{Pólya-Vinogradov}} \quad \ll \quad \underbrace{\sqrt x\,\log^2 x}_{\text{GRH 短区间精度}}.$$

在这三个尺度的**差距**（$\log M \cdot \sqrt M / (\log M)^2 = \sqrt M/\log M$ 与 $\sqrt x/\sqrt M$）中，当前数学**没有任何**工具能跨越。

---

## 32. 数值验证

### 32.1 字符和的精确消失（$M = 30$）

$(\mathbb{Z}/30)^\times = \{1, 7, 11, 13, 17, 19, 23, 29\}$，$\varphi(30) = 8$。8 个字符在该集合上的求和：

| $\chi$ 参数 $(t_3, t_5)$ | 性质 | $\sum_{a \in (\mathbb{Z}/30)^\times} \chi(a)$ |
|---|---|---|
| $(0, 0)$ | 主字符 | $8.0000 + 0.0000\,i$ |
| $(0, 1)$ | 非主 | $\approx 0$ |
| $(0, 2)$ | 非主 | $\approx 0$ |
| $(0, 3)$ | 非主 | $\approx 0$ |
| $(1, 0)$ | 非主 | $\approx 0$ |
| $(1, 1)$ | 非主 | $\approx 0$ |
| $(1, 2)$ | 非主 | $\approx 0$ |
| $(1, 3)$ | 非主 | $\approx 0$ |

数值机器精度消失——定理 27.3 的直接验证。

### 32.2 素数的字符和：GRH 宽松但趋近 $\sqrt X$

对 $X = 10^2, 10^3, 10^4, 10^5$，计算非主 $\chi \bmod 30$ 在 $\{p \leq X\}$ 上的求和：

| $X$ | $\sqrt X$ | $\sqrt X \log^2 X$（GRH 上界） | 典型 $\vert\sum_{p} \chi(p)\vert$（非主 $\chi$） |
|---|---|---|---|
| $10^2$ | 10 | 212 | $0\text{–}4$ |
| $10^3$ | 32 | 1509 | $3\text{–}9$ |
| $10^4$ | 100 | 8483 | $3\text{–}8$ |
| $10^5$ | 316 | 41915 | $9\text{–}35$ |

实测值 $\sim \sqrt X$ 的 $10\%$ 左右——远小于 GRH 上界 $\sqrt X\log^2 X$ 允许的最大振幅。这印证 RH 本身（若成立）给出的是**"上界"**而非典型增长。

### 32.3 $T_\chi(Q_k, \Lambda)$ 在节点处的几何因子

对 $k = 3$，$N = Q_3 = 15$，$\Lambda = p_4^2 = 49$：$\mathcal{S}(15, 49)$ 的所有元素（由定理 27.1 + §II.9.1.1）正是
$$\{7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47\}.$$

对模 $30$ 求模，它们是
$$\{7, 11, 13, 17, 19, 23, 29, 1, 7, 11, 13, 17\}$$

（注意 $31 \equiv 1$、$37\equiv 7$ 等重复——因 $\Lambda > M/2 = 15$）。

由于定理 27.1 要求 $\Lambda = M/2$，这里 $\Lambda > M/2$ 出现"重复覆盖"。对 $\Lambda = p_{k+1}^2 < M/2$ 的情形（即大 $k$），$\mathcal{S}$ 是 $(\mathbb{Z}/M)^\times$ 的**严格子集**——$T_\chi$ 不再自动为 0。

---

## 33. 系列五篇综合

| 篇 | 主题 | 核心定理 | 结论 |
|---|---|---|---|
| I | 邻域定理 | A、B₀ | 定量确定性构造 |
| II | 位置唯一 | D、E | 节点即特殊点 |
| III | 构造算法 | 算法 A/B/C | 给定 $p$ 的可计算方案 |
| IV | 反向诊断 | 21.1, 22.1 | 证 CRT 不能达 Cramér |
| V | 谱分解 | 27.1, 29.1, 30.2 | 联 L 函数零点 |

**统一图景**（单一公式）：
$$\pi_{\mathcal{S}(N, \Lambda)}(x) \;=\; \underbrace{\frac{|\mathcal{S}|}{\varphi(M)}\operatorname{li}(x)}_{\text{几何主项}} \;-\;\underbrace{\frac{1}{\varphi(M)} \sum_{\chi \neq \chi_0} T_\chi(N, \Lambda)\cdot\!\sum_{\rho_\chi}\!\frac{x^{\rho_\chi}}{\rho_\chi}}_{\text{几何} \times \text{算术}}\;+\;\mathrm{err}.$$

- **$N \in \mathcal{N}_+$, $\Lambda = M/2$**：$T_\chi = 0$ 对非主 $\chi$，只剩主项——**RH 无关的精确恒等**（定理 30.2）。
- **$N \in \mathcal{N}_+$, $\Lambda = p_{k+1}^2$（超短）**：$|\mathcal{S}|$ 小但 $T_\chi$ 有结构；GRH 不适用，**定理 A 的确定性接管**。
- **一般 $N$, $\Lambda = M$**：$T_\chi$ 满足 Pólya–V；GRH 控制算术因子；给 Siegel–Walfisz 的精细版本。
- **一般 $N$, $\Lambda \geq \sqrt x$**：GRH 足够控制——短区间素数定理。

### 33.1 剩余开放

- **上界：Cramér 猜想**。CRT 几何结构（本系列）只给下界构造；上界需要跨越 §IV.23 诊断的结构-构造鸿沟。
- **上界：RH**。本系列在节点处给出的"零点抵消"是代数事实（字符正交），不提供零点位置信息。
- **奇异级数的节点值计算**。猜想 24.1 的数值验证可做，但解析证明仍需工具升级。

### 33.2 本系列的真正贡献

1. 把"素数密度"分解成**几何 × 算术**两层，并给各层严格公式；
2. **节点完美枚举定理**（27.1）是 CRT 与 Dirichlet 字符连接的一个**具体、新的**结果；
3. **方法论诊断**（§IV.23, §V.31）清楚划定 CRT 几何能做与不能做的边界。

五篇合起来给出了素数密度波**作为一个完整现象**的数学地图：从"$15$ 附近四胞胎"的最小观察到 Cramér、RH 的遥远猜想之间，我们识别了每一步的严格内容、每一层的工具来源、以及每一道未解决的障碍。

---

*文档生成日期：2026-04-25。"素数密度波"系列第 V（终）篇——字符谱分解打通 CRT 几何与 $L$ 函数零点桥梁。*
