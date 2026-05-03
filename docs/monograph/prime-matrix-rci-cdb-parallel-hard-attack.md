# RCI/PDEC 与 CDB/PDEC 并行攻坚路线

**状态：** `parallel_hard_attack_reduces_to_distributed_collision_or_defect_exit`

本文把前一阶段的 `RCI/PDEC` 与最新的列输入桥接 `CDB/PDEC` 合并分析。结论：

```text
两条路线可以并行推进，并且相互支撑；
但它们不是两个独立证明，而是共享同一个 PDEC/Tail-anchor 出口。
```

最优策略不是在二者中二选一，而是分支：

```text
分散双尾碰撞 => 直接 RCI 赢；
集中双尾碰撞 => CDB/Tail-anchor 缺陷；
列见证半径异常 + RCI 变紧 => Endpoint/Column CRT 缺陷。
```

## 1. 两条路线的逻辑角色

### 1.1 RCI/PDEC

`RCI` 是横向行内账本：

\[
|R_0(h)|>
\sum_{j\ge2}(j-1)|R_j(h)|.
\tag{RCI}
\]

其中：

- `R_0` 是无尾储备；
- `R_1` 完全抵消；
- `R_j,j>=2` 是多尾碰撞超额。

因此 `RCI` 的优势是极窄、直接、可数值化；弱点是它只看行内横截面。

### 1.2 CDB/PDEC

`CDB` 是纵向列见证位移账本。若列命题 `Col(q)` 作为输入，则每个非平凡列
有素数见证。行内覆盖标签 `ell|n_c` 强制同列见证位移

\[
d_c\not\equiv0\pmod\ell.
\tag{D}
\]

因此 `CDB` 的优势是把行内双尾碰撞投影到列方向，暴露端点/尾锚缺陷；弱点是它
仍需证明“位移预算不足”。

## 2. 为什么两线可并行

两线攻击的是同一个反例的两个投影：

| 投影 | 看到的对象 | 失败时暴露 |
|---|---|---|
| `RCI` 横向 | 无尾储备 vs 多尾碰撞 | 碰撞超额压倒储备 |
| `CDB` 纵向 | 列素数见证位移 | 位移余类避零压力 |
| `PDEC` 全局 | 端点/尾锚相位 | 持续 CRT 缺陷 |

所以可以并行证明两个互补命题：

1. **分散碰撞命题：** 若多尾碰撞没有尾锚集中，也没有位移余类集中，则
   `RCI` 直接成立。
2. **集中碰撞命题：** 若多尾碰撞足够集中以威胁 `RCI`，则触发
   `CDB` 缺陷，进入 `PDEC/Tail-anchor`。

这避免了单一路线的最难点：不必对所有行强行证明统一筛余下界；只需证明
反例不能同时“分散到躲开尾锚”又“集中到打败无尾储备”。

## 3. 联合审计事实

新增联合审计：

```text
experiments/prime_matrix_rci_cdb_joint_audit.py
docs/monograph/prime-matrix-rci-cdb-joint-audit.md
```

参数 `max_p=1000`、`y=floor(p/e)`、每个 `p` 保留最紧 `5` 行：

- 紧行全局最小 `RCI margin` 为 `1`；
- 紧行最大列见证半径为 `81`；
- 紧行最大尾标签负载为 `2`；
- 紧行最大位移余类负载为 `2`。

这些数据支持三个判断：

1. 最紧 `RCI` 行没有出现强尾锚集中；
2. 位移余类集中度很低，说明 `CDB` 压力是分散型；
3. 列见证半径大的样本多数不是双尾碰撞紧行，因此“半径大”本身不是反例核心。

因此下一步证明应避免误攻“所有列见证半径都小”这种过强命题，而应证明：

```text
只有当列见证半径异常与 RCI 失败同场出现时，才需要进入 PDEC。
```

## 4. 并行证明的三分支

### 分支 A：低集中度直接 RCI

设

\[
L_T(h)=\max_{\ell}\#\{n\in R_{\ge2}(h):\ell|n\}
\]

为尾标签最大负载。若 `L_T(h)` 小，则双尾碰撞分散。目标证明：

\[
\sum_{j\ge2}(j-1)|R_j(h)|
\le
|R_0(h)|-1.
\tag{A}
\]

这就是 `CDB-1` 的精确形式。它不需要列命题；它是直接 `RCI` 分支。

### 分支 B：尾标签集中进入 Tail-anchor

若 `(A)` 失败，则双尾超额必须接近或超过无尾储备。若同时 `L_T(h)` 大，则大量
碰撞共享同一尾标签 `ell`，形成尾锚集中：

\[
\#\{n\in I_h:\ell|n,\ P^-(n/\ell)>y\}
\text{ 异常大}.
\]

目标证明：

```text
large L_T(h) => Tail-anchor defect.
```

这是 `CDB-2/PDEC` 分支。

### 分支 C：位移余类集中进入 Endpoint/Column defect

若尾标签本身不集中，但 `RCI` 仍失败，则由列命题给出的同列素数见证位移
必须在许多尾标签上同时避开零类。设

\[
L_D(h)=\max_{\ell,a\ne0}
\#\{c:\ell|n_c,\ d_c\equiv a\pmod\ell\}.
\]

若 `L_D(h)` 大，则得到列位移余类集中；若 `L_D(h)` 小，则分散压力回到分支 A。

目标证明：

```text
RCI-Fail + small L_T(h) + large L_D(h)
=> Endpoint/Column CRT defect.
```

这是 `CDB-3/PDEC` 分支。

## 5. 合成定理

**Theorem RCI-CDB-Parallel（条件合成）。**
假设列命题 `Col(q)` 可作为输入。若分支 A、B、C 均成立，且
`PDEC/Tail-anchor` 出口排斥成立，则终端 `QSurv` 硬点闭合，从而相邻素数递推的
行命题闭合。

**证明。**
反设某终端行失败。由单尾抵消恒等式，失败等价于 `RCI` 失败或其边界等号。
若尾标签和位移余类均不集中，则分支 A 给出 `RCI` 正余量，矛盾。
若尾标签集中，则分支 B 触发 Tail-anchor defect，由出口排斥矛盾。
若尾标签不集中但位移余类集中，则分支 C 触发 Endpoint/Column CRT defect，
由出口排斥矛盾。三种情况穷尽，故失败不存在。证毕。

## 6. 当前最小硬点

并行路线把剩余义务压缩为三个可审查不等式：

1. **CDB-1 / Distributed RCI：**
   分散双尾碰撞不能超过无尾储备。
2. **CDB-2 / Tail-anchor Exit：**
   大尾标签负载强制尾锚缺陷。
3. **CDB-3 / Displacement Exit：**
   大位移余类负载强制端点/列 CRT 缺陷。

其中最值得先攻的是 **CDB-1**，因为联合审计显示最紧行通常处在低集中度区域：

```text
max_tail_label_load <= 2,
max_displacement_residue_load <= 2.
```

若 `CDB-1` 被证明，剩余只需处理集中异常，而集中异常天然更适合 `PDEC/Tail-anchor`
出口。

新增 `docs/monograph/prime-matrix-distributed-rci-semiprime-reduction.md` 后，
`CDB-1` 可再具体化：在 `y^3>q^2` 后，`RCI` 的正项就是终端块中的素数数，
负项就是因子都在 `(y,p]` 的平衡双尾半素数数。因此 `Distributed-RCI`
的核心不等式是

```text
balanced semiprimes in I_h < primes in I_h.
```

审计 `docs/monograph/prime-matrix-distributed-rci-semiprime-audit.md` 到
`p<=2000` 显示：最后双尾残因子例外为 `p=13`，最后三尾例外为 `p=7`，
最大半素数/无尾比值为 `2/3`。

新增 `docs/monograph/prime-matrix-distributed-rci-local-pairing-route.md` 后，
该比较又可转化为局部 Hall 配对：把每个平衡双尾半素数注入匹配到同一行附近
的不同素数。审计 `docs/monograph/prime-matrix-distributed-rci-pairing-audit.md`
在 `17<=p<=2000` 中没有配对失败，最大最小匹配半径为 `132`。若未来证明
`Hall-R`，则 `Distributed-RCI` 直接闭合；若 `Hall-R` 失败，失败区间就是
可定位的 `PDEC/Tail-anchor` 异常。

## 7. 下一步硬攻目标

下一步不应再泛化为“证明所有短区间都有素数”。具体目标应写为：

```text
Distributed-RCI:
在尾标签负载和位移余类负载均小的终端行中，
多尾碰撞超额严格小于无尾储备。
```

这是目前最小、最可操作、最能同时利用 `RCI` 与列命题的硬点。
