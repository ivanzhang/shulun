# 列命题辅助的 RCI/PDEC 桥接攻坚

**状态：** `conditional_column_input_reduces_row_hardpoint_to_displacement_defect`

本文回答一个精确问题：

```text
若列命题已经作为已证定理使用，它能否更快闭合当前行命题硬点？
```

结论是：可以显著缩小硬点，但不能直接替代当前 `RCI/PDEC`。列命题排除的是
“整列无素数”的零截面退化；当前终端行硬点是“固定长度 `q` 的横截面无素数”。
二者之间还需要一个行列桥接：把横向空行产生的覆盖标签，传递成纵向列见证的
位移缺陷。

## 1. 当前链条位置

相邻奇素数 `p<q` 的递推路线已压缩为：

```text
QSurv(p,q) => Row(q).
```

而 `QSurv` 的终端带又压缩为：

```text
RCI/PDEC:
无尾储备数 > 多尾碰撞超额，
或失败触发持续端点/尾锚缺陷。
```

精确恒等式见 `docs/monograph/prime-matrix-terminal-sae-cancellation-identity.md`：

\[
G_y(h)-T_y(h)
=
\sum_{P^-(n)>y}(1-\omega_T(n)).
\]

因此当前真正剩余不是一般列非空，而是：

\[
|R_0(h)|>
\sum_{j\ge2}(j-1)|R_j(h)|.
\tag{RCI}
\]

## 2. 列命题能直接提供什么

设 `Col(q)` 表示每个非平凡列 `1<=c<q` 在 `q×q` 方阵中含素数。

若 `Col(q)` 作为已证输入，则对每个列 `c<q`，存在某个行号 `r_c`
使

\[
\pi_c=r_cq+c
\]

为素数。若某个目标行 `H` 是空行，则 `r_c\ne H`。

这排除了以下退化：

1. 某个非平凡列完全没有素数；
2. 反例把所有亏损隐藏为完整列空洞；
3. `PDEC` 中的零截面分支。

但它没有直接排除单个空行。一个抽象配置可以每列有一个素数，同时某一行全空。
所以 `Col(q)` 必须和行内覆盖标签一起使用。

## 3. 行列位移刚性

假设目标行 `H` 的列点

\[
n_c=Hq+c,\qquad 1\le c<q
\]

被某个旧素数标签 `\ell<=p` 覆盖，即 `\ell|n_c`。令 `\pi_c=r_cq+c`
为同列素数见证，并设位移

\[
d_c=r_c-H.
\]

若 `\pi_c\ne \ell`，则

\[
d_c\not\equiv0\pmod\ell.
\tag{D}
\]

**证明。**
若 `d_c≡0 (mod ell)`，由于 `q` 与 `ell` 互素，

\[
\pi_c-n_c=d_cq\equiv0\pmod\ell.
\]

又 `ell|n_c`，故 `ell|\pi_c`。但 `\pi_c` 是素数且 `\pi_c\ne ell`，矛盾。证毕。

这就是列命题能真正接入行命题的地方：行内每个覆盖标签都会对同列素数见证的
纵向位移施加非零同余约束。

## 4. 双尾碰撞的位移压力

在 `RCI` 的双尾化区间内，负项来自

\[
n_c=\ell_1\ell_2 t,\qquad y<\ell_1,\ell_2\le p.
\]

对这样的列 `c`，列见证位移同时满足

\[
d_c\not\equiv0\pmod{\ell_1},
\qquad
d_c\not\equiv0\pmod{\ell_2},
\]

除非同列见证就是某个极小例外素数 `\ell_i`。终端带中这些例外可以单独列入
小 `p` 或顶端见证误差。

因此若 `RCI` 失败，即双尾碰撞超额压倒无尾储备，则不是一个纯横向现象；
它强迫大量列见证位移同时避开大量尾标签的零类。

这给出新的桥接命题。

## 5. CDB 桥接命题

**CDB（Column Displacement Budget）。**
固定相邻奇素数 `p<q`、终端行 `H` 与 `y=floor(p/e)`。若 `Col(q)` 成立，
且行 `H` 的 `RCI` 失败，则下面至少发生一项：

1. **Tail-anchor defect：** 大量双尾标签的列见证位移集中在少数非零余类；
2. **Endpoint CRT defect：** 坏行集合在某些低模/尾模上形成持续端点偏差；
3. **Column radius defect：** 存在大量列，其最近素数见证必须离开 `H` 一个异常大的纵向距离。

若三项均不发生，则 `RCI` 必须成立。

这不是新黑箱，而是当前最小可攻接口：它把

```text
横向无尾储备 vs 双尾碰撞
```

转成

```text
纵向列见证位移的 CRT 预算
```

从而真正把已证列命题接入行命题。

## 6. 条件闭合定理

**Theorem C-Row（列输入下的行递推闭合）。**
假设对所有奇素数 `q`，`Col(q)` 成立。再假设 `CDB` 成立，并且
`PDEC/Tail-anchor` 出口排斥已经闭合。则 `Row(q)` 对所有奇素数 `q`
成立。

**证明。**
反设存在最小相邻递推失败 `Row(q)`。由平方壳层引理和
`QSurv(p,q)=>Row(q)`，失败给出某个 `q` 行旧 `p`-筛幸存者为空。
低行段按既有短区间/递推分解处理，剩余进入终端镜像带。

终端带由 `TSI` 和单尾抵消恒等式化为 `RCI/PDEC`。若 `RCI` 成立，则
该行存在旧筛幸存者，矛盾。若 `RCI` 失败，则由 `Col(q)+CDB`，失败
必触发 Tail-anchor、Endpoint CRT 或 Column radius 缺陷；这些缺陷由
`PDEC/Tail-anchor` 出口排斥，仍矛盾。故 `QSurv(p,q)` 成立，进而
`Row(q)` 成立。证毕。

## 7. 实验支撑与实际含义

新增审计：

```text
experiments/prime_matrix_column_row_bridge_audit.py
docs/monograph/prime-matrix-column-row-bridge-audit.md
```

`q<=1000` 的结果：

- 数据中非平凡列命题失败数为 `0`；
- 全局最小行素数数为 `1`；
- 排除第 `q` 平凡列后，最大列见证半径为 `107`，出现在 `q=929` 的末行；
- 说明列输入确实提供纵向支撑，但这个支撑半径不是平凡常数，必须进入
  `Column radius defect` 或位移预算分析。

这验证了逻辑判断：列命题不是无用输入，但它本身不是行命题；它需要通过
列见证位移刚性才能转化为行命题压力。

## 8. 下一步最小硬攻

当前最优攻坚顺序：

1. **严证 CDB-1：** 双尾碰撞若不集中，则其总超额被无尾储备吸收；
2. **严证 CDB-2：** 双尾碰撞若集中，则给出 Tail-anchor defect；
3. **严证 CDB-3：** 列见证半径若异常大，则给出 Endpoint/Column CRT defect；
4. **出口闭合：** 将上述 defect 接入既有 `PDEC/Tail-anchor` 排斥。

这样使用列命题后，行命题的剩余硬点不再是泛泛的短区间素数存在性，而是一个
具体的行列双向闭锁不等式：

```text
RCI-Fail + Col(q) => CDB defect => PDEC/Tail-anchor contradiction.
```

这就是下一步应集中硬攻的最小闭合链条。
