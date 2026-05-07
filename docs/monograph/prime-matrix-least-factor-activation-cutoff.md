# 最小因子激活截止

**状态：** `least_factor_cutoff_exact_reduction_to_prime_residual`

本文把“斜线到 `q^2` 后才真正连线”的几何图像进一步逐行化。

## 1. 截止引理

固定素数 `P` 与行参数 `1<=x<=P`，行窗口为

\[
n=xP+c,\qquad 1\le c<P.
\]

令

\[
Q_x=\left\lfloor \sqrt{xP+P-1}\right\rfloor.
\]

若 `n` 是合数，则它有最小素因子 `q<=sqrt(n)<=Q_x`。因此：

```text
只需画 q<=Q_x 的独立斜线；
q>Q_x 的命中必有更小素因子先命中，是 shadow hit。
```

于是只用 `q<=Q_x` 筛出的残洞，精确等于该行中的素数列。

## 2. 审计

脚本：

```text
experiments/prime_matrix_least_factor_activation_cutoff_audit.py
```

输出：

```text
docs/least_factor_activation_cutoff_audit_run_20260505.txt
docs/least_factor_activation_cutoff_audit_run_20260505.json
```

读数：

| P | `<P` 素数数 | 独立激活素数数范围 | 最小残洞 | 残洞=素数数 | 最弱行 |
|---:|---:|---|---:|---|---|
| 23 | 8 | 3..8 | 2 | True | x=14,23 |
| 101 | 25 | 6..25 | 7 | True | x=73 |
| 499 | 94 | 11..94 | 29 | True | x=362 |
| 997 | 167 | 14..167 | 54 | True | x=916 |
| 1999 | 302 | 18..302 | 110 | True | x=1881 |
| 5003 | 669 | 25..669 | 260 | True | x=4980 |

这验证了逐行精确等价：超过最小因子截止的斜线对“是否还有素数洞”没有独立贡献。

## 3. 对证明链的影响

圆柱斜线模型现在有三层严格含义：

```text
q^2 前：q 命中是 shadow hit；
q^2 后但 q>Q_x：在当前行仍不是最小因子标签；
q<=Q_x：才是当前行可独立覆盖的最小因子斜线。
```

所以行命题可写为：

```text
对每个 1<=x<=P，
当前已激活最小因子斜线 q<=floor(sqrt(xP+P-1))
不能覆盖全部列。
```

这不是新证明；它与早期短区间素数存在等价。但它是目前最忠实于几何模型的闭合接口，
能把所有“大素因子斜线未连线”的直觉转化为可审稿的最小因子截止。
