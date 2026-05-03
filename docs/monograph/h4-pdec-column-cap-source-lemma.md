# H4-PDEC Column Cap 来源引理

**状态：** `h4_pdec_column_cap_source_rule_completed_coefficients_open`

本文专攻 `PDEC-Dual-Cert` 中的 `column cap` 来源。结论是：列信息可以进入 `A g<=b`
系统，但只能通过明确的列投影容量、列见证位移预算或条件路由行进入；不能由“完整 CRT
列均衡”直接推出任意坏窗子集的均衡。

## 1. 坐标与对象

固定奇素数 `q`。矩阵点写为

\[
n_{r,c}=rq+c,\qquad 1\le c<q,
\]

第 `q` 列作为平凡列单独剥离。设 `H` 是待排除的坏行，坏行点为

\[
n_c=Hq+c.
\]

若列命题或列见证输入可用，则每个非平凡列 `c` 有某个素数见证

\[
\pi_c=r_cq+c.
\]

定义列见证位移

\[
d_c=r_c-H.
\]

在 H4-PDEC 中，仍以同一个 persistent 坏窗集合 `S` 与相位计数

\[
g(t)=\#\{x\in S:\tau(x)=t\}
\]

为对象。任何 column cap 必须是这个 `g` 的线性约束。

## 2. 列投影容量行

设 `C_j\subset \mathbb Z/Q\mathbb Z` 是一个列投影相位块，`Z` 是已经由独立证明、有限证书或外部定理给出的允许坏窗全集，且 `S\subset Z`。

**Lemma H4-PDEC-COL1（列投影容量继承）。**
若

\[
B_{\rm col}(j)
=
\#\{x\in Z:\tau(x)\in C_j\},
\]

则

\[
\sum_{t\in C_j}g(t)\le B_{\rm col}(j).
\]

**证明。**
这是 `H4-PDEC-S2` 对相位块 `C_j` 的直接应用。左侧只计数 `S` 中投影到 `C_j`
的元素；由 `S\subset Z`，它不超过 `Z` 中同一投影块的元素数。证毕。

**审稿边界。**
该引理说明 column cap 的合法形式，但不自动给出 `B_col(j)`。`B_col(j)` 必须来自列见证预算、有限枚举容量或符号化列容量定理。

## 3. 列见证位移刚性

设坏行点 `n_c` 被旧标签 `\ell` 覆盖，即

\[
\ell\mid Hq+c,\qquad \ell<q.
\]

**Lemma H4-PDEC-COL2（同列素数见证非零位移）。**
若同列见证 `\pi_c=r_cq+c` 是素数且 `\pi_c\ne \ell`，则

\[
d_c=r_c-H\not\equiv0\pmod\ell.
\]

**证明。**
若 `d_c≡0 (mod ell)`，则
\[
\pi_c-n_c=(r_c-H)q\equiv0\pmod\ell.
\]
又 `\ell|n_c`，故 `\ell|\pi_c`。由于 `\pi_c` 是素数且 `\pi_c\ne\ell`，矛盾。证毕。

该引理是列见证真正能进入行反例矛盾场的地方：坏行覆盖标签不能与同列素数见证位移的零类兼容。

## 4. 位移预算到 column cap

给定一组列标签约束 `\lambda(c)`，其中 `\lambda(c)` 是解释坏行点 `Hq+c` 的旧素数标签。定义列冲突集合

\[
Z_{\rm bad}(\ell)
=
\{c:\lambda(c)=\ell,\ d_c\equiv0\pmod\ell,\ \pi_c\ne\ell\}.
\]

由 Lemma H4-PDEC-COL2，真实坏行必须满足

\[
|Z_{\rm bad}(\ell)|=0
\]

除非这些列被登记为以下例外之一：

```text
见证等于标签 ell 的小例外；
列见证半径异常，进入 ColumnRadiusDefect；
位移非零类高度集中，进入 Column CRTDefect；
尾标签集中，进入 Tail-anchor defect。
```

因此 column cap 的可审稿形式不是“列均匀性”，而是以下条件路由行。

**Lemma H4-PDEC-COL3（列冲突路由行）。**
设 `R_col(g)` 是由列冲突集合推得的非负线性函数。若已经证明

\[
R_{\rm col}(g)>B_{\rm col}
\Longrightarrow
\text{ColumnRadiusDefect}\vee\text{ColumnCRTDefect}\vee\text{TailAnchorDefect},
\]

则在排除这些出口后的剩余分支中，可以加入

\[
R_{\rm col}(g)\le B_{\rm col}.
\]

**证明。**
这是 `H4-PDEC-S5` 的列版本。若剩余分支中违反该行，则路由定理强制进入已剥离出口，矛盾。证毕。

## 5. 三种可准入 column cap

正式 `PDEC-Dual-Cert` 中，column cap 只接受以下三种来源。

### 5.1 有限列证书

对有限范围，给出：

```text
q, Q, X, Z；
每个相位块 C_j；
B_col(j)=# {x in Z: tau(x) in C_j}；
S subset Z 的证明或证书。
```

验收后可由 Lemma H4-PDEC-COL1 写入 `A g<=b`。该类型只覆盖明示有限范围。

### 5.2 符号化列容量定理

若证明了对全体或某个无限范围的 `q`：

\[
\#\{x\in Z_q:\tau(x)\in C_j\}\le B_{\rm col}(j,q),
\]

且正式反例诱导的 `S_q\subset Z_q`，则同样由 COL1 写入 `A`。这才是全局 column cap 的无条件形式。

### 5.3 条件列路由行

若无法直接给出容量上界，但能证明违反上界会进入 `ColumnRadiusDefect`、`ColumnCRTDefect`
或 `TailAnchorDefect`，则由 COL3 写入当前剩余分支。该行必须在元数据中记录被剥离出口，不能作为全局无条件行。

## 6. 与现有列材料的关系

现有文档 `prime-matrix-column-assisted-rci-bridge.md` 已证明列见证位移非零刚性，即本文
COL2 的核心。审计 `prime-matrix-column-row-bridge-audit.md` 显示样本中非平凡列见证存在，
但最大列见证半径达到 `107`，所以不能把“列见证在固定小半径内存在”当成无条件事实。

`prime-matrix-bpn-lhb-column-residue-rigidity-audit.md` 证明高层补洞残基块由列残基
`c mod ell` 决定。这可为 low-hole bucket 的 Hall 容量提供列残基结构，但它本身仍不是
任意 PDEC 坏窗集合的 column cap；必须通过 COL1 或 COL3 接入。

## 7. 当前准入状态更新

本文件完成后，`column cap` 从“来源未定义”升级为：

```text
source rule proved；
coefficients and branch metadata still open。
```

即：

- COL1 给出列投影容量行的合法继承规则；
- COL2 给出列见证位移非零刚性；
- COL3 给出违反列预算时回流到命名出口的条件行；
- 仍未提交正式 `B_col(j)` 表、全局列容量定理或完整 ColumnDefect 路由证书。

## 8. 下一步系数任务

补充文档 `h4-pdec-column-cap-coefficient-ledger.md` 已生成第一版 `column-cap coefficient
ledger`，每一行登记：

```text
row_id；
q 或 q-range；
Q；
phase block C_j；
B_col(j)；
source type: finite / symbolic / conditional-routing；
source theorem or certificate；
excluded exit if conditional；
normalization used by PDEC-Dual-Cert。
```

该 V1 账本登记了有限列见证半径、RCI/CDB 联合审计界值、LHB 列残基刚性有限界值和
ColumnDefect 条件路由模板。新增 `h4-pdec-column-defect-routing-contract.md` 后，
`ColumnRadius/ColumnCRT` 模板的路由合同已定式化为相位兼容权重
`W_D(t),W_{\ell,a}(t)` 与阈值 `D_0,L_D`。它仍未把所有相位块或权重物化为机器可读数组；
因此下一步是扩展审计脚本输出 `phase_block`、`weight`、`bound` 与 `source_hash`。
