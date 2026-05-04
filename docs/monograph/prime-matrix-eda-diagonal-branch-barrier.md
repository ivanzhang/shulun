# EDA 对角分支屏障：`x=p` 的不可降阶端点

**状态：** `diagonal_branch_exactendpoint_barrier_open`

PinnedDivisor-Leakage 压力强化了 `x` 有内部素因子 `pi<p` 的分支。但早期对角段还包含端点
`x=p`。这一行没有任何可用的内部因子，因而不能由因子降阶路线处理。

本文把该端点独立出来，避免把内部因子分支的进展误用为全局闭合。

## 1. 对角行的精确等价

对 `x=p`，

\[
I_{p,p}=\{p^2+1,\ldots,p^2+p-1\}.
\tag{DBB-1}
\]

**定理 DBB-1（对角筛余等价素数）。**  

\[
U_p(p)>0
\tag{DBB-2}
\]

当且仅当区间

\[
(p^2,p^2+p)
\tag{DBB-3}
\]

中存在素数。

**证明。**  
若 `(p^2,p^2+p)` 中有素数 `r`，则 `r=p^2+k`，其中 `1<=k<p`。它不被任何 `<p`
素数整除，故贡献一个筛余点。

反过来，若 `p^2+k` 贡献筛余点，则它没有 `<p` 素因子。又

\[
p^2<p^2+k<p^2+p<(p+1)^2,
\tag{DBB-4}
\]

所以任何合数因子分解都必须有一个素因子 `<=p`。但 `p\nmid p^2+k`，故若它合成，就会有
某个 `<p` 素因子，矛盾。因此 `p^2+k` 为素数。证毕。

## 2. 为什么因子降阶不能触及 `x=p`

因子降阶需要 `x=pi y` 且 `pi<p`。但 `x=p` 的唯一素因子是 `p` 本身，不属于 `<p`
筛标签集合，也不能形成更小 `pi` 层窗口。因此：

```text
FactorDescent / PinnedDivisor-Leakage 只覆盖 x<p 的内部因子分支；
x=p 必须由 ExactEndpoint-MinRep / LowMod-PDEC / 对角素数屏障处理。
```

这一点是审稿边界：若证明稿声称 `X_0(p)>p`，必须显式覆盖 `x=p`。

## 3. 对角行的 CRT 形态

在对角行中，覆盖条件为

\[
q\mid p^2+k,\qquad q<p.
\tag{DBB-5}
\]

由于 `p` 对每个 `q<p` 可逆，每个 `q` 覆盖 `[1,p-1]` 中的单个模 `q` 等差类：

\[
k\equiv -p^2\pmod q.
\tag{DBB-6}
\]

因此 `U_p(p)=0` 等价于这些固定相位等差类完全覆盖 `1,\ldots,p-1`。这里没有 `x` 的相位自由；
全部相位由 `p mod q` 决定。

这比一般 `x` 行更刚性，但也更集中：要排斥对角零行，必须证明固定相位族

```text
{k ≡ -p^2 mod q : q<p}
```

不能覆盖全部列。

## 4. 当前可用约束

对角分支可继承以下已证工具：

1. **变量阶布尔精确性：**
   \[
   S_{K_p}(p,p)=U_p(p).
   \tag{DBB-7}
   \]
2. **LowMod/PDEC：** 任何负端点缺陷必须来自固定相位低模函数；
3. **HighLabel-MinRep：** 高标签 `q` 在 `[1,p-1]` 中的覆盖仍是单等差类，复用间距至少 `q`；
4. **PinnedDivisor 的反面：** 此处分支没有 `x` 内部因子可提供相位钉扎，也没有可下降出口；
5. **Prime-square endpoint：** 任一幸存点自动是素数。

## 5. 对全局证明链的影响

现在 EDA 全局闭合必须分为两条：

```text
Internal branch: 1<=x<p
  用 PDL / FactorDefect / Low-or-High / PDEC 排斥；

Diagonal branch: x=p
  证明固定相位族 k≡-p^2 mod q 不能全覆盖，
  等价于证明 (p^2,p^2+p) 中存在素数。
```

这说明当前“唯一硬点”实际有一个不可再忽略的端点核：

```text
Diagonal ExactEndpoint-MinRep Defect:
exclude U_p(p)=0 directly.
```

内部因子分支再强，也不能替代这一端点证明。

## 6. 下一步可攻方向

最自然的下一步不是继续降阶，而是针对固定相位 `(DBB-6)` 建立一个专用不等式：

\[
\#\left(
[1,p-1]\setminus
\bigcup_{q<p}\{k:k\equiv -p^2\pmod q\}
\right)>0.
\tag{DBB-8}
\]

若能证明 `(DBB-8)`，则对角分支闭合；再与 PDL 内部分支合并，才可能得到完整
`X_0(p)>p`。
