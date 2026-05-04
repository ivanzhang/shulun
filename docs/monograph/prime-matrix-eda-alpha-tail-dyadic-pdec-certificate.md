# AlphaTail 强负尾项到 dyadic PDEC 证书

**状态：** `alpha_tail_dyadic_pdec_certificate_reduction_open`

本文继续压缩 `AlphaTailStrong`。结论不是排斥强负尾项，而是证明：一旦强负尾项出现，它不能作为
“整体模糊误差”存在，必定显化为某个 dyadic 模数块上的有向端点 CRT 缺陷，除非远尾 core 已经
单独异常。

## 1. 端点函数

固定

\[
\alpha=0.9,\qquad y=\lfloor \alpha p\rfloor,\qquad H=p-1.
\tag{DYP-1}
\]

令 `M_y` 为所有素数 `q<=y` 的乘积。对 squarefree `d|M_y` 定义

\[
N_d(p)=\#\{1\le k\le H:d\mid p^2+k\},
\qquad
\varepsilon_d(p)=N_d(p)-{H\over d}.
\tag{DYP-2}
\]

若 `rho_d(p)` 是 `-p^2 mod d` 在 `{1,...,d}` 中的正代表，则

\[
N_d(p)=
\begin{cases}
1+\left\lfloor {H-\rho_d(p)\over d}\right\rfloor,& \rho_d(p)\le H,\\
0,& \rho_d(p)>H.
\end{cases}
\tag{DYP-3}
\]

因此

\[
|\varepsilon_d(p)|\le 1.
\tag{DYP-4}
\]

这是纯 CRT 端点锯齿函数；它只依赖 `p mod d` 与短端点 `H=p-1`。

## 2. Dyadic 块分解

对任意有限模数区间 `I` 写

\[
E_I(p)=
\sum_{\substack{d\in I\\ d\mid M_y\\ d\ {\rm squarefree}}}
\mu(d)\varepsilon_d(p).
\tag{DYP-5}
\]

特别地，对 dyadic 块 `I_B=(B,2B]` 写

\[
E_B(p)=
E_{(B,2B]}(p).
\tag{DYP-6}
\]

并令

\[
E_{(D_0,D_1]}(p)=
\sum_{D_0<d\le D_1}\mu(d)\varepsilon_d(p),
\qquad
E_{>D}(p)=
\sum_{d>D}\mu(d)\varepsilon_d(p),
\tag{DYP-7}
\]

其中求和条件仍为 `d|M_y` 且 `d` squarefree。

## 3. 强负尾项的 dyadic 显化

**定理 DYP.**  
设存在 `eta>0` 使

\[
E_{>D_0}(p)\le -\eta {p\over\log p}.
\tag{DYP-8}
\]

取 `D_1>D_0` 与 `0<=beta<1`。若远尾没有承担至少 `beta` 比例的负缺陷，即

\[
E_{>D_1}(p)>-\beta\eta {p\over\log p},
\tag{DYP-9}
\]

则存在一个参与覆盖 `(D_0,D_1]` 的截断 dyadic 块

\[
I_j=(D_0,D_1]\cap (2^jD_0,2^{j+1}D_0],
\]

使

\[
E_{I_j}(p)\le
-{(1-\beta)\eta\over L}{p\over\log p},
\qquad
L=\left\lceil \log_2 {D_1\over D_0}\right\rceil+1.
\tag{DYP-10}
\]

**证明。**  
由 `(DYP-8)` 与 `(DYP-9)`，

\[
E_{(D_0,D_1]}(p)
=E_{>D_0}(p)-E_{>D_1}(p)
<-(1-\beta)\eta {p\over\log p}.
\tag{DYP-11}
\]

区间 `(D_0,D_1]` 至多被 `L` 个 dyadic 块覆盖。若每个块都大于
右端平均阈值，则总和大于 `(DYP-11)` 右端，矛盾。证毕。

## 4. 证书含义

`(DYP-10)` 是有向端点 PDEC 证书：

```text
固定 dyadic 模数层内，CRT 端点函数 mu(d)(N_d-H/d)
出现 -p/log p 级别的同向偏斜。
```

这一步利用了前面已经建立的刚性：

1. `PrimeVoid=>AlphaPDEC`：对角无素数会给出 `E_{>D_0}<=-eta p/log p`；
2. 固定低模项 `O_{D_0}(1)`：低模不能承载大尺度负缺陷；
3. `AlphaTail` 精确分解：好半素数壳层已抵消，剩余必须表现为端点或坏高标签异常；
4. dyadic 分块：强负尾项不能分散到无形，必须落入某个有限模数尺度，或进入远尾 core。

因此下一步硬点被压成二选一：

```text
Dyadic-PDEC：排斥某个块上的强有向端点偏斜；
FarTail-Core：证明远尾 core 负缺陷必进入 Tail-anchor / SAE / ColumnCRT。
```

本文只证明出口显化，不证明两个出口不可能。

## 5. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_dyadic_audit.py
```

用法：

```text
python3 experiments/prime_matrix_alpha_tail_dyadic_audit.py --selected 997,5003 --alpha 0.9 --maxD 20000 --format table
```

样本摘要：

| p | alpha | maxD | partial endpoint | worst block | worst endpoint |
|---:|---:|---:|---:|---:|---:|
| 499 | 0.9 | 20000 | -0.752135 | 4096 | -9.537456 |
| 997 | 0.9 | 20000 | 10.978184 | 4096 | -18.263347 |
| 5003 | 0.9 | 20000 | -20.894845 | 8192 | -13.341102 |
| 10007 | 0.9 | 20000 | 1.257294 | 4096 | -33.957000 |

这些数据只说明端点缺陷在有限审计中确实会集中到少数 dyadic 层；它们不是全局证明输入。

## 6. 审稿边界

已证明：

```text
AlphaTailStrong + far-tail 非主导
=> Dyadic endpoint PDEC certificate.
```

尚未证明：

```text
Dyadic endpoint PDEC certificate impossible,
或 FarTail-Core impossible.
```

所以 Prime Matrix 对角分支仍保持归约状态，不能升级为无条件闭合。
