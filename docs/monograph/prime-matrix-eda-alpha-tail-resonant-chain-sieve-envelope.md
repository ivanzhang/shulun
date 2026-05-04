# 共振三点链的三禁/一禁筛包络

**状态：** `alpha_tail_resonant_chain_sieve_envelope_reduction_open`

本文把共振差值 `s=±r` 的三点光滑链写成上筛包络。相比二点 `ShiftSmooth(r)`，未锁素数从
“二禁”升级为“三禁”，因此该分支有额外刚性。

## 1. 三点链对象

定义

\[
T_r=\{d:d,\ d+r,\ d+2r\ {\rm all\ }y{\rm -smooth/squarefree}\}.
\tag{RSE-1}
\]

这里只先给无符号上筛；Möbius 符号过滤只会减少数量或进入奇偶 PDEC。

## 2. 局部禁零类数

对素数 `q`，三点非光滑排除对应剩余类

\[
d\equiv0,\ -r,\ -2r\pmod q.
\tag{RSE-2}
\]

令 `b_q(r)` 为这些剩余类的 distinct 数，则

\[
b_q(r)=
\#\{0,-r,-2r\pmod q\}.
\tag{RSE-3}
\]

特别地：

```text
b_q(r)=1, 若 q|r；
b_q(r)=3, 若 q∤r 且 q>2；
b_2(r)<=2。
```

这就是三点链的三禁/一禁结构。

## 3. Selberg 上筛接口

令

\[
P(z)=\prod_{y<q\le z}q,\qquad z=3B.
\tag{RSE-4}
\]

对任意 Selberg 上筛权 `lambda_a`，有

\[
|T_r|
\le
\sum_{d\in I_3}
\left(
\sum_{\substack{a|P(z)\\ d\bmod a\in\Omega_{3,r}(a)}}\lambda_a
\right)^2,
\tag{RSE-5}
\]

其中 `I_3` 是 `d,d+r,d+2r` 同在高块中的区间，`\Omega_{3,r}(a)` 由 `(RSE-2)` 通过 CRT 生成。
主筛因子为

\[
\mathcal V_{3,r}(z)
\asymp
\prod_{y<q\le z}\left(1-{b_q(r)\over q}\right).
\tag{RSE-6}
\]

若 `q|r`，局部因子从 `1-3/q` 提升为 `1-1/q`，这正是共振奇异因子。

## 4. 出口

若三点链超过 `(RSE-5)` 可接受包络，则只能发生：

1. **三点奇异因子过大**：`r` 的中高素因子太多，进入 `ColumnCRT`；
2. **三点端点缺陷**：Selberg 端点锯齿同号累积，进入 `PDEC/SAE`；
3. **三点 Möbius 奇偶偏置**：平方自由同符号过滤异常，回到 `Parity-PDEC`。

## 5. 审稿边界

审计脚本：

```text
experiments/prime_matrix_alpha_tail_resonant_chain_audit.py
```

样本：

| p | block | shift | domain | chains | all same | alternating | corr01 | corr12 | corr02 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 997 | 4096 | -36 | 4024 | 362 | 172 | 65 | 112 | 102 | 112 |
| 5003 | 8192 | -36 | 8120 | 1686 | 657 | 331 | 328 | 324 | 290 |
| 10007 | 16384 | -900 | 14584 | 3720 | 1254 | 811 | 440 | 446 | 410 |

样本显示：三点链数量与 `s=±r` 共振差值完全对应；但三组相邻/跨端 Möbius 相关远小于链总量。
因此共振压力的无符号部分强，符号同向部分仍需通过三点奇偶/PDEC 继续压制。

已证明：

```text
resonant branch
=> three-point sieve envelope with b_q(r)=#{0,-r,-2r mod q}.
```

尚未证明：

```text
该包络常数足以压住正式反例所需共振压力。
```

下一步最小硬点是核验三点链上筛主项与端点误差；失败时输出 `ColumnCRT/PDEC/SAE` 证书。
