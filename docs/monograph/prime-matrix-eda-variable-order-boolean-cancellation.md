# EDA 变量阶布尔消尾：Tail/Core 的点态吸收

**状态：** `variable_order_tail_penalty_eliminated_endpoint_positive_open`

本文综合 `EDA-Dual`、`EDA-TailCore`、`EDA-SignedTail` 的历史经验，攻击当前最窄尾项硬点。
结论是：固定五阶的 `Tail/Core` 惩罚不是本质障碍；若选择随 `p` 增长的奇数阶 `K`，使其
超过早期区段内任意整数可能拥有的 `<p` 不同素因子数，则 Bonferroni 权逐点等于精确幸存指示。

这一步不证明 `U_p(x)>0`，但它严格消除了“高重合尾项吞掉余量”的固定阶假障碍，把剩余重新压回
精确 CRT 端点和 MinRep 正性。

## 1. 最大小素因子数

对早期区段

\[
1\le x\le p,\qquad n\in I_{p,x}=\{px+1,\ldots,px+p-1\},
\tag{VBC-1}
\]

有

\[
n\le p^2+p-1.
\tag{VBC-2}
\]

若 `n` 有 `t` 个不同素因子，则 `n>=2^t`。因此

\[
\omega_p(n)\le
\Omega_p:=
\left\lfloor \log_2(p^2+p-1)\right\rfloor.
\tag{VBC-3}
\]

取

\[
K_p=
\begin{cases}
\Omega_p,&\Omega_p\ {\rm odd},\\
\Omega_p+1,&\Omega_p\ {\rm even}.
\end{cases}
\tag{VBC-4}
\]

则 `K_p` 为奇数，且对所有早期 `n` 都有 `\omega_p(n)\le K_p`。

## 2. 点态布尔消尾

定义奇数阶 Bonferroni 权

\[
b_K(t)=\sum_{j=0}^{\min(K,t)}(-1)^j{t\choose j}.
\tag{VBC-5}
\]

**定理 VBC-1（变量阶点态精确性）。**  
对上述 `K_p`，任意早期 `n` 满足

\[
b_{K_p}(\omega_p(n))=
\begin{cases}
1,&\omega_p(n)=0,\\
0,&\omega_p(n)\ge1.
\end{cases}
\tag{VBC-6}
\]

**证明。**  
若 `\omega_p(n)=0`，显然 `b_{K_p}(0)=1`。若 `t=\omega_p(n)\ge1`，由 `(VBC-3)` 有
`t<=K_p`，故

\[
b_{K_p}(t)=\sum_{j=0}^{t}(-1)^j{t\choose j}=(1-1)^t=0.
\tag{VBC-7}
\]

证毕。

于是变量阶 Bonferroni 和满足

\[
S_{K_p}(p,x)=U_p(x)
\tag{VBC-8}
\]

对所有 `1<=x<=p` 精确成立。

## 3. 对 Tail/Core 路线的影响

固定五阶身份

\[
S_5=U_p-\sum_{\omega_p(n)\ge6}{\omega_p(n)-1\choose5}
\tag{VBC-9}
\]

显示高重合点会形成负惩罚。`EDA-TailCore` 与 `EDA-SignedTail` 已把该惩罚压成
`SignedTail-Balance`、孤立奇核心和影子拥塞。

变量阶 `K_p` 给出更强的处理：在每个点 `n` 的小素因子布尔格上，所有非空子集贡献完全相消。
因此：

```text
Tail/Core penalty is a fixed-order truncation artifact.
```

它不是 `EDA` 的最终本质障碍。真正障碍变成：如何把精确包含排除和

\[
U_p(x)=
\sum_{d\mid M_{<p}}\mu(d)
\#\{1\le k<p:d\mid px+k\}
\tag{VBC-10}
\]

证明为正。

## 4. 与 LowMod / FactorDescent 的衔接

变量阶消尾后，剩余不能再写成“尾惩罚太大”，而应写成：

```text
exact endpoint cancellation too perfect.
```

若 `U_p(x)=0`，则完整布尔格消和在每个点上都为 `0`，整行没有任何 `t=0` 点。这时可用的结构输入是：

1. **LowMod:** 低模端点函数必须与高模端点函数精确抵消；
2. **MinRep:** 完整覆盖 CRT 证书的最小代表命中 `x<=p`；
3. **FactorDescent:** 每个 `pi|x` 必须发生中高标签泄漏或代表逃逸；
4. **SignedTail:** 若回到低阶截断，负尾项必须来自孤立奇核心或影子拥塞。

因此下一步最小硬点不再是固定阶 Tail/Core，而是：

```text
ExactEndpoint-MinRep Defect:
prove exact Boolean cancellation cannot cover every column in 1<=x<=p
without producing LowMod/FactorDescent/PDEC contradiction.
```

## 5. 审稿边界

本步已无条件证明：

```text
for K_p odd and >= Omega_p, S_{K_p}(p,x)=U_p(x) exactly.
```

尚未证明：

```text
U_p(x)>0 for every 1<=x<=p.
```

也就是说，本步消掉的是“固定阶尾项惩罚”这一技术障碍；剩余仍是首零行 MinRep/EDA 的核心正性。

