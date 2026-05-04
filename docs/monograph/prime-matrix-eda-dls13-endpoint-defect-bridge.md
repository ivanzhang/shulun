# DLS13 端点缺陷桥：低洞失败必给出负 CRT 缺陷

**状态：** `dls13_endpoint_defect_bridge_reduction_open`

本文把 `DLS-13` 继续压缩为一个显式端点缺陷命题。设

\[
y=\lfloor2p/3\rfloor,\qquad
V_y=\prod_{q\le y}\left(1-\frac1q\right).
\tag{DEB-1}
\]

对角低洞数为

\[
H_y(p)=\#\{1\le k<p:\forall q\le y,\ q\nmid p^2+k\}.
\tag{DEB-2}
\]

高标签精确容量仍记为 `C_y(p)`。

## 1. 精确端点分解

由完整包含排除，

\[
H_y(p)=
\sum_{d\mid M_y}\mu(d)
\#\{1\le k<p:k\equiv -p^2\pmod d\},
\quad
M_y=\prod_{q\le y}q.
\tag{DEB-3}
\]

写

\[
H_y(p)=(p-1)V_y+E_y(p),
\tag{DEB-4}
\]

其中

\[
E_y(p)=
\sum_{d\mid M_y}\mu(d)
\left(
\#\{1\le k<p:k\equiv -p^2\pmod d\}
-{p-1\over d}
\right).
\tag{DEB-5}
\]

这是精确恒等式；没有估计。

## 2. 失败推出负端点缺陷

**定理 DEB-1（DSC 失败的端点缺陷桥）。**  
若对角分割容量判据失败，即

\[
H_y(p)\le C_y(p),
\tag{DEB-6}
\]

则

\[
E_y(p)\le C_y(p)-(p-1)V_y.
\tag{DEB-7}
\]

**证明。**  
由 `(DEB-4)`，`E_y(p)=H_y(p)-(p-1)V_y`。代入 `(DEB-6)` 即得。证毕。

因此，只要证明

\[
E_y(p)> C_y(p)-(p-1)V_y,
\tag{DEB-8}
\]

就能推出 `H_y(p)>C_y(p)`，从而由 `DSC-1` 得对角行存在素数。

## 3. 样本余量

脚本：

```text
experiments/prime_matrix_dls13_endpoint_bridge_audit.py
```

样本显示 `E_y(p)` 通常为负，但离失败阈值还有明显余量：

| p | main `(p-1)V_y` | low holes | high capacity | endpoint | failure threshold | margin |
|---:|---:|---:|---:|---:|---:|---:|
| 101 | 12.96 | 11 | 9 | -1.96 | -3.96 | 2.00 |
| 499 | 47.77 | 45 | 32 | -2.77 | -15.77 | 13.00 |
| 997 | 85.38 | 84 | 55 | -1.38 | -30.38 | 29.00 |
| 5003 | 345.58 | 307 | 246 | -38.58 | -99.58 | 61.00 |
| 10007 | 637.28 | 585 | 455 | -52.28 | -182.28 | 130.00 |

这里 `margin = H_y(p)-C_y(p)`，正好是分割容量判据的余量。

## 4. 真正剩余

`DEB` 把 `DLS-13` 的低洞下界改写为更精准的端点缺陷排斥：

```text
DLS13-PDEC:
E_y(p) cannot be as negative as C_y(p)-(p-1)V_y.
```

这比直接证明 `H_y(p)\gg p/log p` 更贴近 CRT 结构，因为：

1. 主项 `(p-1)V_y` 已显式；
2. 高标签容量 `C_y(p)` 已显式；
3. 只需排斥过强负端点缺陷；
4. 失败正是固定相位 `-p^2 mod d` 的 PDEC 型异常。

## 5. 下一步最优接口

将 `(DEB-5)` 按模数大小分解：

\[
E_y(p)=E_{\le D}(p)+E_{>D}(p).
\tag{DEB-9}
\]

下一步应证明：

1. `LowMod`: `E_{\le D}` 不能达到大负阈值，除非出现显式 Fourier/PDEC 坏相位；
2. `Tail`: `E_{>D}` 若过大，则由高模核心或近对称半素数壳层吸收；
3. 两个出口均回流到现有 PDEC/SAE 证书系统。

本文完成的是严格桥接；尚未证明 `(DEB-8)`。当前最小硬点已经从粗 `DLS-13` 降为
`DLS13-PDEC`。
