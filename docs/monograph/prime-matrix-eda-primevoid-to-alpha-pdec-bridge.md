# PrimeVoid 到 Alpha-PDEC 的桥

**状态：** `primevoid_to_alpha_pdec_bridge_proved_exits_open`

本文把对角最终反例

```text
(p^2,p^2+p) 中无素数
```

直接接入 `alpha=0.9` 的端点缺陷系统。

## 1. PrimeVoid 推出分割容量失败

设 `alpha>1/sqrt2`，`y=floor(alpha p)`。若

\[
\pi(p^2+p-1)-\pi(p^2)=0,
\tag{PAB-1}
\]

则 `P_alpha(p)=0`。由 AlphaTail 精确分解

\[
H_\alpha(p)-C_\alpha(p)
=P_\alpha(p)-B_\alpha^{bad}(p),
\tag{PAB-2}
\]

得到

\[
H_\alpha(p)-C_\alpha(p)=-B_\alpha^{bad}(p)\le0.
\tag{PAB-3}
\]

因此

\[
H_\alpha(p)\le C_\alpha(p).
\tag{PAB-4}
\]

也就是说，对角无素数自动触发分割容量失败。

## 2. PrimeVoid 推出强负端点缺陷

令

\[
V_\alpha(p)=\prod_{q\le y}\left(1-\frac1q\right),
\qquad
E_\alpha(p)=H_\alpha(p)-(p-1)V_\alpha(p).
\tag{PAB-5}
\]

由端点缺陷桥，

\[
E_\alpha(p)\le C_\alpha(p)-(p-1)V_\alpha(p).
\tag{PAB-6}
\]

若 Alpha-MainGap 常数包给出

\[
(p-1)V_\alpha(p)-C_\alpha(p)
\ge c_\alpha {p\over\log p},
\tag{PAB-7}
\]

则

\[
E_\alpha(p)\le -c_\alpha {p\over\log p}.
\tag{PAB-8}
\]

这就是 `PrimeVoid=>PDEC` 的精确形式：无素数不是普通失败，而是强负端点 CRT 缺陷。

## 3. LowMod/Tail 二分

对任意固定 `D` 与 `0<theta<1`，写

\[
E_\alpha(p)=E_{\alpha,\le D}(p)+E_{\alpha,>D}(p).
\tag{PAB-9}
\]

若 `(PAB-8)` 成立，则至少发生一项：

\[
E_{\alpha,\le D}(p)\le -\theta c_\alpha {p\over\log p},
\tag{PAB-10}
\]

或

\[
E_{\alpha,>D}(p)\le -(1-\theta)c_\alpha {p\over\log p}.
\tag{PAB-11}
\]

固定 `D` 时，`E_{\alpha,\le D}=O_D(1)`，所以 `(PAB-10)` 对充分大 `p` 自动不可能。
因此大尺度 PrimeVoid 必须进入尾项强负出口 `(PAB-11)`。

## 4. 当前最小剩余

至此，对角无素数反例被严格压成：

```text
AlphaTailStrong:
E_{alpha,>D}(p) <= -c p/log p
```

其中 `alpha=0.9` 可由显式常数包保证 `c>0`。

尾项强负必须来自：

1. 高模交叠 core；
2. 坏高标签命中过密；
3. 固定相位 PDEC/SAE。

## 5. 审稿边界

本文证明了：

```text
PrimeVoid => strong Alpha-PDEC endpoint defect.
```

尚未证明：

```text
strong AlphaTail endpoint defect impossible.
```

下一步最优硬点已经非常窄：

```text
AlphaTailStrong exclusion:
排斥 E_{alpha,>D} 的 -c p/log p 级负尾项，
或证明其必产生 SAE/PDEC 证书矛盾。
```
