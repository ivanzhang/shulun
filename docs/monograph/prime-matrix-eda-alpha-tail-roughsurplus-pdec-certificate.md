# RoughSurplus-PDEC：粗筛端点盈余证书

**状态：** `alpha_tail_roughsurplus_pdec_certificate_reduction_open`

本文处理 `square mass bridge` 的第二个出口：粗筛端点盈余

\[
\Delta^{\rm rough}=|R|-HV.
\tag{RSP-1}
\]

若大素粗筛幸存数明显超过完整 CRT 主项，则该盈余必须来自有限大素模的端点偏置，或来自高素尾的孤窗异常。

## 1. 大素粗筛函数

令

\[
\mathcal P=(y,z]\cap\{\text{primes}\}.
\tag{RSP-2}
\]

对 `q in P` 定义局部允许函数

\[
\phi_q(d)=1_{\{d\not\equiv -jr\pmod q,\ 0\le j<m\}}.
\tag{RSP-3}
\]

完整粗筛函数为

\[
\Phi(d)=\prod_{q\in\mathcal P}\phi_q(d),
\tag{RSP-4}
\]

于是

\[
|R|=\sum_{d\in I_m}\Phi(d),
\qquad
V=\prod_{q\in\mathcal P}\left(1-{b_{m,q}(r)\over q}\right).
\tag{RSP-5}
\]

## 2. 低大素/高大素二分

取 `D`，令

\[
\mathcal P_{\le D}=\{q:y<q\le D\},\qquad
\mathcal P_{>D}=\{q:D<q\le z\}.
\tag{RSP-6}
\]

定义

\[
\Phi_{\le D}(d)=\prod_{q\in\mathcal P_{\le D}}\phi_q(d),
\qquad
V_{\le D}=\prod_{q\in\mathcal P_{\le D}}\left(1-{b_q\over q}\right).
\tag{RSP-7}
\]

低模粗筛盈余为

\[
\Delta_{\le D}=
\sum_{d\in I_m}\Phi_{\le D}(d)-H V_{\le D}.
\tag{RSP-8}
\]

若完整盈余 `Delta^{rough}` 达到 `Delta_0`，则对任意 `0<beta<1` 至少发生一项：

1. **低大素 RoughSurplus-PDEC。**

\[
\Delta_{\le D}\ge \beta\Delta_0;
\tag{RSP-9}
\]

2. **高大素尾盈余。**

高素尾条件化后贡献至少 `(1-beta)Delta_0`，进入 `Rankin/SAE/ColumnCRT`。

这是普通加减分解；第一项是有限模

\[
Q_D=\prod_{y<q\le D}q
\tag{RSP-10}
\]

上的低模端点偏置。

## 3. Fourier 证书

定义零均值测试函数

\[
F_D(d)=\Phi_{\le D}(d)-V_{\le D}.
\tag{RSP-11}
\]

若 `(RSP-9)` 成立，则

\[
\sum_{d\in I_m}F_D(d)\ge \beta\Delta_0.
\tag{RSP-12}
\]

由于 `F_D` 在完整 `Q_D` residue 系上均值为零，H4-PDEC 模板给出非零频率 `h` 使

\[
|\widehat g(h)|
\ge
{\beta\Delta_0\over\sum_{h\ne0}|\widehat F_D(h)|},
\tag{RSP-13}
\]

其中 `g(t)=#{d in I_m:d≡t mod Q_D}` 或正式坏窗子集的相位计数。若当前分支只处理粗筛幸存子集，
则必须把 `S` 改为同一集合的推前计数，不能混用背景 `I_m`。

## 4. 审计样本

审计脚本：

```text
experiments/prime_matrix_alpha_tail_roughsurplus_pdec_audit.py
```

样本：

| p | block | shift | m | D primes | full surplus | low surplus | tail gap |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 997 | 4096 | -36 | 4 | 8 | -126.796894 | 18.140517 | -144.937410 |
| 997 | 4096 | -36 | 5 | 8 | 9.905226 | 26.773639 | -16.868413 |
| 5003 | 8192 | -36 | 4 | 8 | 0.594104 | 4.936565 | -4.342461 |
| 5003 | 8192 | -36 | 5 | 8 | 309.234084 | 8.799064 | 300.435020 |
| 10007 | 16384 | -900 | 4 | 8 | 449.915405 | 0.409632 | 449.505772 |
| 10007 | 16384 | -900 | 5 | 8 | 1024.280067 | 0.510250 | 1023.769817 |

## 5. 审稿边界

已证明：

```text
rough surplus
=> finite low-large-prime PDEC
   or high-large-prime tail surplus.
```

尚未证明：

```text
低大素 PDEC 不可能；
高大素尾盈余不可能或可由 Rankin/SAE/ColumnCRT 吸收。
```

下一步最小硬点是把低大素 `RoughSurplus-PDEC` 接入 H4 对偶证书，并给高大素尾一个 Rankin/SAE 上界。
