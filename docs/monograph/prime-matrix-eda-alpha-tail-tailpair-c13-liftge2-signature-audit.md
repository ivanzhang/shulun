# AlphaTail `C13` 的 `lift>=2` h/t 签名空性

**状态：** `c13_liftge2_signature_mod6_sample_closed_global_open`

本文接续 `lift>=2` 的模 `6` 空性审计，把“`q mod 6` 不在 `{1,5}`”进一步解释为
`u,t,h` 签名刚性。

## 1. h/t 公式

低筛 AP 类写成

\[
q=a+t\ell,\qquad t\ge2.
\tag{LGS-1}
\]

同时

\[
u a=n+h\ell,\qquad n=-(j-j_1)r.
\tag{LGS-2}
\]

因此

\[
u q=(tu+h)\ell+n.
\tag{LGS-3}
\]

当前目标窗口的 `r` 都满足 `6|r`，故

\[
n\equiv0\pmod6.
\tag{LGS-4}
\]

若进一步有

```text
u=1；
t in {2,3}；
h in {0,1}；
ell mod 6 in {1,5}，
```

则

\[
q\equiv(t+h)\ell\pmod6.
\tag{LGS-5}
\]

此时 `t+h` 只能为 `2,3,4`，所以

\[
q\bmod6\in\{2,3,4\},
\tag{LGS-6}
\]

不可能是大于 `3` 的素数。

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_liftge2_signature_audit.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_liftge2_signature_audit.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --format table
```

输出摘要：

```text
highP-total:
  candidates=1368；
  bad_mod6=1368；
  good_mod6=0；
  algebra_fail=0；
  q_mod6={2:250, 3:928, 4:190}；
  t_hist={2:888, 3:480}；
  u_hist={1:1368}；
  h_hist={0:920, 1:448}；
  h_over_u={'0/1':920, '1/1':448}。
```

逐窗口：

```text
p=5003:
  candidates=704；
  bad_mod6=704；
  good_mod6=0。

p=10007:
  candidates=664；
  bad_mod6=664；
  good_mod6=0。
```

## 3. 结构结论

当前压力样本的 `lift>=2` 空性不再只是经验模 `6` 统计，而是由以下签名链推出：

```text
6|r
=> n=-(j-j1)r == 0 mod 6；

候选签名被压缩到:
  u=1, t in {2,3}, h in {0,1}；

于是:
  q == (t+h)ell mod 6；

由于 ell 是尾素:
  ell mod 6 in {1,5}；

而 t+h in {2,3,4}：
  q mod 6 in {2,3,4}。
```

所以所有 `lift>=2` 候选的 `q` 都不是尾素，进而

\[
D_{\ge2}=0.
\tag{LGS-7}
\]

## 4. 全局接口

样本结构提示，全局化 `LiftGE2-Mod6Void` 可以压成三个确定条件：

```text
LGS-A:
  目标窗口族满足 6|r。

LGS-B:
  lift>=2 候选必有 u=1。

LGS-C:
  lift>=2 候选必有 t in {2,3} 且 h in {0,1}。
```

若 `LGS-A/B/C` 全局成立，则 `lift>=2` 分支无条件空。

## 5. 审稿边界

已完成：

```text
当前压力样本的 lift>=2 h/t/u 签名完全提取；
证明样本候选满足 u=1, t in {2,3}, h in {0,1}；
由 6|r 推出 q mod 6 in {2,3,4}；
因此样本 D_ge2=0。
```

仍未完成：

```text
全局证明 LGS-A/B/C；
若某目标窗口出现 u>1 或 t>=4 或 h 不在 {0,1}，需送入 PDEC/SAE；
把该结构性 Mod6Void 接回完整目标窗口族。
```
