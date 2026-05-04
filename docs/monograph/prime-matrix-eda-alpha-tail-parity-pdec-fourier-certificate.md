# Parity-PDEC 的中心化 Fourier 证书

**状态：** `alpha_tail_parity_pdec_fourier_certificate_reduction_open`

本文补强 `Parity-PDEC bridge`：低模奇偶和必须先扣除局部均值。扣除后，任何剩余偏置都会给出
有限 CRT 模数上的非零 Fourier 系数。

## 1. 低模符号函数与均值

固定 `R`，令

\[
Q_R=\prod_{q\le R}q.
\tag{PFC-1}
\]

低模奇偶函数为

\[
\Psi_{R,r}(d)=\prod_{q\le R}\psi_{q,r}(d).
\tag{PFC-2}
\]

它只依赖 `d mod Q_R`。在完整 residue 系上的均值为

\[
m_R(r)=
\prod_{\substack{q\le R\\ q\nmid r}}{q-4\over q},
\tag{PFC-3}
\]

因为 `q\nmid r` 时有两个剩余类取 `-1`，其余 `q-2` 个剩余类取 `+1`；`q|r` 时该局部因子恒为
`+1`。

定义中心化函数

\[
\Psi^0_{R,r}(d)=\Psi_{R,r}(d)-m_R(r).
\tag{PFC-4}
\]

## 2. 中心化低模偏置

令 `A_r` 为删除后 squarefree 支撑。若

\[
\left|\sum_{d\in A_r}\Psi^0_{R,r}(d)\right|\ge \Delta,
\tag{PFC-5}
\]

则发生真正的低模奇偶偏置。未中心化的

\[
\sum_{d\in A_r}\Psi_{R,r}(d)
\tag{PFC-6}
\]

可以很大，但其中 `m_R(r)|A_r|` 是局部奇异因子主项，不能误标为 PDEC。

## 3. Fourier 证书

在群 `Z/Q_RZ` 上展开

\[
\Psi^0_{R,r}(a)=
\sum_{h\bmod Q_R}\widehat\Psi(h)e(ha/Q_R),
\qquad \widehat\Psi(0)=0.
\tag{PFC-7}
\]

设

\[
A(a)=\#\{d\in A_r:d\equiv a\pmod{Q_R}\}.
\tag{PFC-8}
\]

则

\[
\sum_{d\in A_r}\Psi^0_{R,r}(d)
=
\sum_{h\ne0}\widehat\Psi(h)
\sum_{a\bmod Q_R}A(a)e(ha/Q_R).
\tag{PFC-9}
\]

因此由三角不等式，若 `(PFC-5)` 成立，则存在 `h!=0` 使

\[
\left|
\sum_{a\bmod Q_R}A(a)e(ha/Q_R)
\right|
\ge
{\Delta\over \sum_{h\ne0}|\widehat\Psi(h)|}.
\tag{PFC-10}
\]

这就是有限低模 `Parity-PDEC` Fourier 证书。

## 4. 审稿边界

审计脚本：

```text
experiments/prime_matrix_alpha_tail_parity_pdec_audit.py
```

样本摘要：

| p | block | shift | pairs | K | R | low sum | modeled | centered | tail gap |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 997 | 4096 | -36 | 710 | 202 | 31 | 120 | 10.039637 | 109.960363 | 82 |
| 5003 | 8192 | -36 | 2416 | 486 | 31 | 84 | 34.163046 | 49.836954 | 402 |
| 10007 | 16384 | -900 | 5107 | 819 | 31 | 139 | 361.073420 | -222.073420 | 680 |

样本显示：低模中心化项并不总为正；较大正相关经常由 `tail gap` 承担。因此下一步必须严写
`TailParity`，不能只攻低模 PDEC。

## 5. 审稿边界

已证明：

```text
中心化低模奇偶偏置
=> 非零 Fourier/CRT 系数。
```

尚未证明：

```text
该非零系数不可能。
```

下一步最小硬点是为正式反例链抽出的 `A_r` 提交 `PDEC-Cert` 上界，或证明偏置只能孤立发生并进入
`SAE`。
