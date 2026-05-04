# AlphaTail 双线性证书的频率分割合同

**状态：** `alpha_tail_frequency_split_contract_reduction_open`

本文修正并压实 `BFC=>BBC` 的使用口径：非零频率并不自动等于缺陷。低频可能只是短区间核的
平滑边界项；只有扣除低频模型后仍残留的大值，才进入 Bohr-cap/PDEC。

## 1. 频率分割

沿用大模 `Q>4p^2` 与短区间核 Fourier 展开。取频率 cutoff `H_0`，写

\[
\mathcal F_{\le H_0}
=
{1\over Q}
\sum_{1\le h\le H_0}
\widehat K_H(h)e(-hp^2/Q)B_h(M,D)
+{\rm conjugate},
\tag{FSC-1}
\]

\[
\mathcal F_{>H_0}
=
{1\over Q}
\sum_{H_0<h<Q-H_0}
\widehat K_H(h)e(-hp^2/Q)B_h(M,D).
\tag{FSC-2}
\]

则双曲线带偏差满足恒等式

\[
\Delta(M,D)=\mathcal F_{\le H_0}+\mathcal F_{>H_0}.
\tag{FSC-3}
\]

这里 `Delta` 是已经扣除 `h=0` 主项后的偏差。

## 2. 合同式二分

若

\[
|\Delta(M,D)|\ge \Xi,
\tag{FSC-4}
\]

则对任意 `0<beta<1`，至少发生一项：

\[
|\mathcal F_{\le H_0}|\ge \beta\Xi,
\tag{FSC-5}
\]

或

\[
|\mathcal F_{>H_0}|\ge (1-\beta)\Xi.
\tag{FSC-6}
\]

第一项定义为 `LowFreq-ModelMismatch`；第二项才进入高频证书。

## 3. 高频证书抽取

若 `(FSC-6)` 成立，则由三角不等式存在某个 `h`、`H_0<h<Q-H_0`，使

\[
|B_h(M,D)|
\ge
{(1-\beta)\Xi Q\over
\sum_{H_0<h<Q-H_0}|\widehat K_H(h)|}.
\tag{FSC-7}
\]

随后才能应用 Bohr-cap 归约 `(BBC-11)`。这保证我们不会把低频平滑项误标为 PDEC。

## 4. 低频分支的意义

`LowFreq-ModelMismatch` 不是丢弃项。它表示局部短区间模型

\[
\sum_{d\in I\cap(p^2/m,(p^2+H)/m]\cap D}{m\over d}
\]

与全局 harmonic 模型 `H R_I` 的差异承担了反例所需余量。该分支应回到 `CIN` 的模型错配出口，
并进一步做端点 Euler--Maclaurin 或 sawtooth 账本，而不是进入 Bohr-cap。

## 5. 审稿边界

已证明：

```text
WSS excess
=> LowFreq-ModelMismatch 或 HighFreq-BohrCap。
```

尚未证明：

```text
LowFreq-ModelMismatch 不可能；
HighFreq-BohrCap 不可能。
```

当前最小硬点被明确拆成两项：低频模型错配吸收、高频 Bohr-cap 差集排斥。
