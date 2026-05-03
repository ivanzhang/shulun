# WSH-Hall 缺陷三出口模板

**状态：** `reduction_template_with_forced_defect_audit_not_global_proof`

本文把 `WSH-Hall/PDEC` 的下一硬点从“继续找匹配”改成“若匹配失败，失败必须在哪里显形”。
核心目标是把所有可用刚性投影统一到同一个 Hall 缺陷块上：

```text
行坐标投影 + 尾因子双曲投影 + 小轮同余投影 + 固定偏移投影 + q²-n 镜像投影
=> Tail-anchor / PDEC / Endpoint 三出口之一。
```

这一步不是全局证明；它固定下一步必须证明的精确三出口不等式。

## 1. 局部 Hall 图

固定相邻素数层 `p<q`，取

```text
y=floor(p/e),  W_z=prod_{r<=z} r。
```

在某个 `q` 宽行 `I_h` 内，令

```text
P_h = {n in I_h : P^-(n)>p}
B_h = {b=ell_1 ell_2 in I_h : y<ell_1,ell_2<=p}
```

这里 `P_h` 是无尾项，在 `n<q^2` 内实际为素数；`B_h` 是平衡双尾半素数。

给定半径 `R`，定义二部图

```text
G_R(h):  b in B_h 连接 pi in P_h iff |pi-b|<=R。
```

`WSH-Hall` 断言存在从 `B_h` 到 `P_h` 的注入匹配。若失败，则由一维区间图的 Hall
正规形，存在连续半素数块 `B_0={b_i,...,b_j}` 使

\[
  |N_R(B_0)|<|B_0|.
\tag{HDef}
\]

**证明要点。** 每个半素数的邻域是实线上的区间 `[b-R,b+R]` 与有序素数集的交。
若 Hall 失败，取最小失败子集；把它按半素数顺序分成连续分量。不同分量的邻域互不相交，
否则可合并成更短失败块；至少一个连续分量仍违反 Hall。证毕。

因此失败不是模糊事件，而是一个可定位的端点素数亏损块。

## 2. 五个刚性投影

### 2.1 端点亏损投影

对缺陷块定义

\[
  \Delta_E(B_0,R)=|B_0|-|N_R(B_0)|>0.
\]

这是 `Endpoint/PDEC` 可吸收的原始亏损量。若这种亏损在相邻行、镜像块或递推壳层中持续，
它应进入 persistent endpoint CRT defect。

### 2.2 尾因子双曲投影

每个 `b in B_0` 有唯一尾标签对

\[
  b=\ell_1\ell_2,\qquad y<\ell_1,\ell_2\le p。
\]

定义尾标签负载

\[
  L_{\rm tail}(B_0)=
  \max_{\ell\in(y,p]}\#\{b\in B_0:\ell\mid b\}.
\]

若 `L_tail` 大，则 `B_0` 落在少数双曲锚线 `ell*m` 上，进入 `Tail-anchor`。
这正是大因子不可复用刚性在 Hall 缺陷块上的投影。

### 2.3 小轮同余投影

由于 `b` 和可匹配素数 `pi=b+d` 都必须避开小素数 `r<=z`，任何真实边都满足

\[
  d\not\equiv -b\pmod r,\qquad r\le z。
\tag{WS}
\]

这给出允许偏移集合

\[
  \mathcal A_z(b,R)=
  \{d:0<|d|\le R,\ d\not\equiv -b\pmod r\ \forall r\le z\}.
\]

若缺陷块中的 `b mod W_z` 集中在少数相位，或所有允许偏移集中在少数 `d`，
则它进入 `PDEC/fixed-offset CRT defect`。

### 2.4 固定偏移容量投影

对固定偏移 `d`，粗相位保留比例有精确公式

\[
  \rho_z(d)=
  \prod_{\substack{r\le z\\r\nmid d}}
  {r-2\over r-1}.
\tag{FOS}
\]

因此若大量半素数只能通过同一个短偏移 `d` 补洞，它们必须落入比例 `rho_z(d)` 的相位通道。
当实际负载超过该通道容量时，失败不是随机稀疏，而是固定偏移 CRT 缺陷。

### 2.5 终端镜像投影

终端变量的可用镜像是

\[
  n\mapsto q^2-n。
\]

它把终端缺陷转成早期非零类块：对每个旧素数 `ell<=p`，禁类变为

\[
  q^2\pmod \ell。
\]

注意这不是 `-n mod M_p` 的完整周期镜像，也不推出更小方阵零行或短周期复现。
可用结论只有：终端端点亏损可转写为早期非零类块亏损，从而接入 `PDEC/Endpoint`。

## 3. 三出口模板

令 `tau_tail,tau_phase,tau_offset` 为待定阈值。任意 Hall 缺陷块必须满足下列三者之一：

```text
(T) Tail-anchor:
    L_tail(B_0) >= tau_tail(B_0,p,z).

(C) PDEC/fixed-offset CRT defect:
    max_a #{b in B_0: b=a mod W_z} >= tau_phase(B_0,p,z)
    or
    max_d #{b in B_0: d in A_z(b,R)} >= tau_offset(B_0,p,z).

(E) Endpoint deficit:
    Delta_E(B_0,R)>0 persists after removing (T) and (C),
    hence induces a directed endpoint CRT/PDEC deficit.
```

这个模板是当前最小严格目标。要把它变成证明，必须补三个显式不等式：

1. `Tail absorption`：`(T)` 触发已有 Tail-anchor 出口；
2. `Phase absorption`：`(C)` 触发 PDEC 或固定偏移 CRT defect；
3. `Distributed endpoint expansion`：若 `(T),(C)` 都不发生，则
   \[
     |N_R(B_0)|\ge |B_0|
   \]
   对 `R=C log^2 q` 成立，或其失败触发 Endpoint/PDEC。

## 4. 有限缺陷审计

新增脚本：

```text
experiments/prime_matrix_wsh_hall_defect_anatomy.py
```

输入：

```text
docs/monograph/prime-matrix-wsh-hall-phase-certificate.json
```

输出：

```text
docs/monograph/prime-matrix-wsh-hall-defect-anatomy.md
docs/monograph/prime-matrix-wsh-hall-defect-anatomy.json
```

该脚本故意把已知可匹配行的半径压到最小 Hall 半径以下，强制制造缺陷。结果：

```text
input certificate rows = 44
forced radius scenarios = 124
Hall defect records = 124
max excess = 5
max tail label load = 2
max wheel phase load = 1
max allowed offset load = 5
```

解释：

- 所有强制失败都有明确连续 `B_0`，即端点亏损；
- 小样本尾标签不高度集中，说明 Tail-anchor 不是唯一出口；
- 多个最大缺陷依赖少数固定偏移通道，例如 `d=18`，这正是固定偏移相位压力；
- `q^2-n` 镜像区间已记录，但只作为终端到早期非零类块的转写，不作为零行递归证明。

## 5. 下一步最小硬点

当前真正剩余不是扩大数值范围，而是证明下列命题：

**WSH-Expansion-or-Defect.**
对正式反例诱导的任意 Hall 缺陷块 `B_0`，若 Tail-anchor 与固定偏移/PDEC 阈值均未触发，
则 `B_0` 的小轮允许邻域在同一行素数集上满足 Hall 扩张：

\[
  |N_R(B_0)|\ge |B_0|,\qquad R=C\log^2 q。
\]

若该扩张失败，则失败块的 `q^2-n` 镜像非零类在端点层产生可计量 `PDEC/Endpoint` 亏损。

这就是下一轮应专攻的单点硬核。
