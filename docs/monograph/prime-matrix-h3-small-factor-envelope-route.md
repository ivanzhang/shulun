# H3 小首因子骨架包络路线

**状态：** `deterministic_envelope_reduction_not_global_proof`

本文推进 `H3 Full-Blocking Defect` 的第一分支：

```text
small-first-factor skeleton overload => Tail/PDEC envelope.
```

核心结论是一个确定性二分：固定 cutoff `y` 后，若小首因子骨架没有承担足够覆盖，则任何 H3 全阻断都必须使用许多 `>y` 的中尾 first-factor 标签；后者正是低模 PDEC 能量的入口。

## 1. 符号

设 `p<q` 为相邻素数，`I_s=[(s-1)q+1,sq]`，`A_s` 为固定 `h=3` 的六轮候选集合。对 cutoff `y<p`，定义

\[
C_y=\#\{n\in A_s:5\le P^-(n)\le y\},
\qquad
R_y=\#A_s-C_y.
\]

令 `ell_+(y)` 为大于 `y` 的下一素数。若 `H3-SWR` 失败，则所有 `R_y` 个剩余候选必须由 first factor `ell>y` 覆盖。

## 2. 单标签容量

对固定 `ell>y`，同余条件 `ell|n` 在长度 `q` 的整数区间中命中至多

\[
\left\lfloor {q\over \ell}\right\rfloor+1
\le
\left\lfloor {q\over \ell_+(y)}\right\rfloor+1
=U_y.
\]

该上界不使用随机性，也不使用候选集合的 `6` 轮稀疏性；因此是保守但无条件的。

## 3. 骨架二分

若 `H3-SWR` 失败，则：

\[
\text{active labels above }y
\ge
K_y
:=
\left\lceil {R_y\over U_y}\right\rceil .
\tag{H3-SE}
\]

等价地，对任意整数 `K`，若活跃中尾标签数至多 `K`，则必须有

\[
C_y\ge \#A_s-KU_y.
\tag{H3-SO}
\]

这就是小首因子骨架过载的精确定义：在没有许多中尾标签的情况下，`<=y` 的小首因子必须覆盖到 `#A_s-KU_y` 以上。

## 4. 数据账本

对应审计：

```text
experiments/prime_matrix_h3_small_factor_envelope_audit.py
docs/monograph/prime-matrix-h3-small-factor-envelope-audit.md/json
```

在 `p<=5000`、`margin<=20` 的 `4015` 个近失败窗口中：

```text
cutoff 7:  max residual 76, max forced tail labels 3
cutoff 13: max residual 65, max forced tail labels 4
cutoff 31: max residual 49, max forced tail labels 7
cutoff 43: max residual 45, max forced tail labels 9
```

解释：

1. 小 cutoff 时，单个中尾标签容量大，因此只需少数标签就能理论补齐。
2. cutoff 增到 `31` 或 `43` 后，若小骨架不过载，任何全阻断都至少需要 `7` 或 `9` 个中尾标签。
3. 多中尾标签同时活跃会带来 first-factor 标签低模方差，是 `H3-PDEC` 的自然入口。

## 5. 接入 Tail/PDEC

正式证明可按以下二分推进。

### 5.1 小骨架过载

若对某个 cutoff `y` 和小整数 `K` 有

\[
C_y\ge \#A_s-KU_y,
\]

则小首因子集合 `ell<=y` 在同一 `q` 行窗口内承担接近全覆盖的固定相位负载。这应被写入 `Tail/PDEC envelope`：

```text
SmallSkeletonOverload(y,K):
  C_y >= #A_s-KU_y
  => Tail/PDEC.
```

这里的 `Tail/PDEC` 不是口号；正式稿还需给出同一集合口径下的负载阈值、低模投影和上界比较。

### 5.2 多标签低模能量

若小骨架不过载，则 `(H3-SE)` 强制至少 `K_y` 个中尾标签。每个标签只在短 cofactor 窗口中贡献少量点。多个标签在同一行窗口内同步覆盖，会产生

\[
\sum_{d\le D}\sum_{b\bmod d}\sum_{\ell>y}
\left|\mu_{s,\ell}(b;d)-{1\over d}\#A_{s,\ell}\right|^2
\]

型低模能量。这是 `H3-PDEC` 的第二分支。

## 6. 剩余证明义务

本路线已经完成确定性组合二分，但尚未闭合全局证明。剩余义务是：

1. 给 `SmallSkeletonOverload(y,K)=>Tail/PDEC` 填入可审查阈值；
2. 给 `many labels=>H3-PDEC` 填入低模能量下界；
3. 把端点取整损失独立路由到 `SAE/ColumnCRT`；
4. 统一三者的负载口径，避免同一阻断点重复计数。

因此当前硬点已从“六轮候选全覆盖”进一步压缩为：

```text
SmallSkeletonOverload threshold
or
ManyLabel low-mod energy
or
Endpoint SAE/ColumnCRT.
```
