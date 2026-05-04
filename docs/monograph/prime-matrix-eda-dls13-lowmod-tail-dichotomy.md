# DLS13-PDEC 的低模/尾项二分

**状态：** `dls13_lowmod_tail_dichotomy_proved_exits_open`

本文继续压缩 `DLS13-PDEC`。从端点缺陷桥已经知道，若对角分割容量失败，则

\[
E_y(p)\le T_y(p):=C_y(p)-(p-1)V_y<0.
\tag{DLT-1}
\]

本文把该失败进一步分解成低模极负或尾项极负两个出口。

## 1. 低模/尾项分解

取 cutoff `D>=1`。定义

\[
E_{\le D}(p)=
\sum_{\substack{d\mid M_y\\d\le D}}\mu(d)
\left(
N_d(p)-{p-1\over d}
\right),
\tag{DLT-2}
\]

其中

\[
N_d(p)=\#\{1\le k<p:k\equiv -p^2\pmod d\}.
\tag{DLT-3}
\]

并令

\[
E_{>D}(p)=E_y(p)-E_{\le D}(p).
\tag{DLT-4}
\]

这是精确恒等式。

## 2. 二分定理

**定理 DLT-1（低模/尾项二分）。**  
固定 `0<theta<1`。若对角分割容量失败，即 `E_y(p)<=T_y(p)`，则至少发生一项：

\[
E_{\le D}(p)\le \theta T_y(p),
\tag{DLT-5}
\]

或

\[
E_{>D}(p)\le (1-\theta)T_y(p).
\tag{DLT-6}
\]

**证明。**  
若两项都不发生，则

\[
E_y(p)=E_{\le D}(p)+E_{>D}(p)>
\theta T_y(p)+(1-\theta)T_y(p)=T_y(p),
\]

矛盾。证毕。

因此 `DLS13-PDEC` 被严格压成：

```text
排斥 LowMod-Bad(D,theta)
和 Tail-Bad(D,theta)。
```

## 3. 低模坏相位的有限函数

低模项只依赖 `p` 在模

\[
Q_D=\operatorname{lcm}\{d:d\le D,\ d\mid M_y\}
\tag{DLT-7}
\]

下的残基，且每个 `N_d(p)` 可由 `-p^2 mod d` 精确计算。故

\[
E_{\le D}(p)
\tag{DLT-8}
\]

是一个有限 CRT 相位函数。这正是 `PDEC` 可处理的对象：若 `(DLT-5)` 发生，
则 `p mod Q_D` 落入显式低模坏相位集合。

## 4. 尾项出口的含义

尾项

\[
E_{>D}(p)
\tag{DLT-9}
\]

包含高模 squarefree 交叠。若 `(DLT-6)` 发生，说明高模交叠造成异常负贡献。
结合 `DLS` 的 Buchstab 分解，该异常只能通过两类结构显化：

1. 近对称半素数壳层过密；
2. 高模固定相位交叠形成集中 core，并回流到 PDEC/SAE。

因此尾项不是自由误差，而是结构出口。

## 5. 样本审计

脚本：

```text
experiments/prime_matrix_dls13_lowmod_tail_audit.py
```

对 `theta=1/2` 的失败阈值，样本中低模和尾项均远未达到坏阈值。例如：

| p | D | E_total | T_y | E_low | E_tail |
|---:|---:|---:|---:|---:|---:|
| 499 | 1000 | -2.77 | -15.77 | 7.39 | -10.16 |
| 997 | 1000 | -1.38 | -30.38 | 0.78 | -2.16 |
| 5003 | 1000 | -38.58 | -99.58 | -8.07 | -30.51 |

这些不是证明，但说明失败需要比真实样本强得多的负缺陷。

## 6. 下一步最小硬点

当前剩余进一步变为两项：

```text
DLT-LowMod:
prove E_{<=D}(p) > theta T_y(p), unless explicit PDEC bad phase occurs.

DLT-Tail:
prove E_{>D}(p) > (1-theta)T_y(p), unless semiprime-shell/core SAE occurs.
```

最优下一步是先攻 `DLT-LowMod`，因为它是有限 CRT 相位函数，可被完全枚举、Fourier 化或证书化；
尾项则需要继续接 `DLS` 半素数壳层和高模 core。
