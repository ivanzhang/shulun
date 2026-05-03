# H4-PDEC Column Cap 系数账本 V1

**状态：** `h4_pdec_column_cap_coefficients_v1_registered_not_a_ready`

本文承接 `h4-pdec-column-cap-source-lemma.md`，登记当前已有 column cap 数值界值与条件路由阈值。结论是：已有审计能给出若干有限或条件界值，但还没有完整物化为 `PDEC-Dual-Cert` 可直接读取的 `A,b,E,e` 输入；缺口主要是相位块 `C_j` 与正式坏窗集合 `S` 的投影关系。

## 1. 账本字段

每一行使用以下字段：

```text
row_id；
q_range / p_range；
Q；
phase block C_j；
B_col(j)；
source type；
source file；
excluded exit if conditional；
A-ready status；
remaining materialization task。
```

`A-ready` 的含义是：该行已经有明确相位块、明确界值、明确来源定理或证书，并作用于同一个 `g(t)`。若只登记了数值摘要但没有 `C_j`，则不是 `A-ready`。

## 2. 有限列见证界值

来源：`prime-matrix-column-row-bridge-audit.json`，扫描 `q<=1000` 的 `167` 个奇素数。

| row_id | q_range | Q | phase block `C_j` | `B_col(j)` | source type | source file | A-ready | 剩余任务 |
|---|---|---:|---|---:|---|---|---|---|
| `CC-FIN-EMPTYCOL-1000` | `q<=1000` | variable | empty nontrivial column defect set | `0` | `FiniteCert` | `prime-matrix-column-row-bridge-audit.json` | 否 | 把“空非平凡列”事件映射到 `tau` 相位块 |
| `CC-FIN-RADIUS-1000` | `q<=1000` | variable | `D_col(r)>107` | `0` | `FiniteCert` | `prime-matrix-column-row-bridge-audit.json` | 否 | 输出所有 `D_col(r)>107` 相位块为空的证书 |
| `CC-FIN-RADIUS-WORST` | `q=929` | variable | worst radius row | `D_col=107` | `FiniteCert` | `prime-matrix-column-row-bridge-audit.json` | 否 | 仅作常数定位，不能作为上界行 |

审稿解释：`CC-FIN-RADIUS-1000` 可在有限范围内写成

\[
\sum_{t\in C_{D>107}}g(t)\le0,
\]

但当前 JSON 只给出摘要，没有列出 `C_{D>107}` 的相位块。因此它是“数值界值已知、相位块未物化”的账本行。

## 3. RCI/CDB 联合有限界值

来源：`prime-matrix-rci-cdb-joint-audit.json`，扫描 `p<=1000`。

| row_id | p_range | Q | phase block `C_j` | `B_col(j)` | source type | source file | A-ready | 剩余任务 |
|---|---|---:|---|---:|---|---|---|---|
| `CC-FIN-TIGHT-RCI-MARGIN` | `p<=1000` | variable | tight rows with `RCI margin<1` | `0` | `FiniteCert` | `prime-matrix-rci-cdb-joint-audit.json` | 否 | 输出 tight-row 相位块 |
| `CC-FIN-TIGHT-RADIUS` | `p<=1000` | variable | tight rows with `D_col>81` | `0` | `FiniteCert` | `prime-matrix-rci-cdb-joint-audit.json` | 否 | 物化 `D_col>81` 的相位块 |
| `CC-FIN-TAILLOAD` | `p<=1000` | variable | tight rows with tail-label load `>2` | `0` | `FiniteCert` | `prime-matrix-rci-cdb-joint-audit.json` | 否 | 物化尾标签负载相位块 |
| `CC-FIN-DISPLOAD` | `p<=1000` | variable | tight rows with displacement residue load `>2` | `0` | `FiniteCert` | `prime-matrix-rci-cdb-joint-audit.json` | 否 | 物化位移余类负载相位块 |

这里 `B_col=0` 的含义是：有限扫描中没有超过该阈值的记录。它不能直接推广到全局，也不能代替 CDB 证明。

## 4. LHB 列残基刚性有限界值

来源：`prime-matrix-bpn-lhb-column-residue-rigidity-audit.json` 与
`prime-matrix-bpn-lhb-column-residue-rigidity-extended.json`。

| row_id | p_range | Q | phase block `C_j` | `B_col(j)` | source type | source file | A-ready | 剩余任务 |
|---|---|---:|---|---:|---|---|---|---|
| `CC-LHB-AFFINE-Q2310` | `13<=p<=61` sampled | `2310` | affine rigidity failure phases | `0` | `FiniteCert` | LHB column residue audits | 部分 | 将失败相位块空集写入机器输入 |
| `CC-LHB-NEGDELTA-Q2310` | `13<=p<=61` sampled | `2310` | zero bucket with `Delta(H)<0` | `0` | `FiniteCert` | LHB column residue audits | 部分 | 将 `Delta(H)<0` 相位块空集写入机器输入 |
| `CC-LHB-UNBRIDGED-Q2310` | `13<=p<=61` sampled | `2310` | critical zero bucket not bridged | `0` | `FiniteCert` | LHB column residue audits | 部分 | 输出未桥接临界相位块为空的证书 |
| `CC-LHB-BRIDGE-SUPPORT` | `p=43,47` sampled | `2310` | bridged critical phases | `40` for `p=43`, `12` for `p=47` | `FiniteCert` | LHB column residue audits | 否 | 若要入 `A`，需按 `p` 拆行并列出相位块 |

这些行比一般 column cap 更接近 `A-ready`，因为 `Q=2310` 固定且列残基刚性已给出明确相位结构。但当前仓库只保存审计摘要和例子；正式审计输入仍需输出完整相位块列表。

## 5. 条件 ColumnDefect 路由系数

以下行不是有限事实，而是下一步要证明的条件路由模板。

| row_id | range | Q | phase block `C_j` | `B_col(j)` | source type | excluded exit | A-ready | 剩余任务 |
|---|---|---:|---|---:|---|---|---|---|
| `CC-COND-RADIUS` | asymptotic | variable | `D_col>D_0(q)` | `0` after routing | `ConditionalRouting` | `ColumnRadiusDefect` | 否 | 证明大半径坏窗进入端点/列 CRT 缺陷 |
| `CC-COND-DISPLOAD` | asymptotic | variable | displacement residue load `>L_D(q)` | `0` after routing | `ConditionalRouting` | `ColumnCRTDefect` | 否 | 给出 `L_D(q)` 与路由定理 |
| `CC-COND-TAILLOAD` | asymptotic | variable | tail-label load `>L_T(q)` | `0` after routing | `ConditionalRouting` | `TailAnchorDefect` | 否 | 给出 `L_T(q)` 与尾锚路由 |
| `CC-COND-DISTRIBUTED` | asymptotic | variable | low radius/load complement | RCI positive margin | `ConditionalRouting` | none; direct `Distributed-RCI` | 否 | 证明低集中度时 RCI 正余量 |

条件行进入 `A` 的规则是：先在证明树中剥离对应出口，再把剩余分支限制写成线性约束。没有出口排斥时，这些行不能作为无条件证书行。

新增 `h4-pdec-column-defect-routing-contract.md` 后，`CC-COND-RADIUS` 与
`CC-COND-DISPLOAD` 的合同对象已经定式化：

```text
ColumnRadiusDefect:
  输入 D_0、列见证选择器 Pi、高半径相位兼容权重 W_D(t)；
  违反 R_D(g)<=0 即回流 ColumnRadiusDefect。

ColumnCRTDefect:
  输入标签 ell、非零位移余类 a、阈值 L_D、相位兼容权重 W_{ell,a}(t)；
  违反 R_{ell,a}(g)<=L_D 即回流 ColumnCRTDefect。
```

因此条件路由行的“出口元数据”已闭合；仍未闭合的是 `D_0,L_D` 的全局解析阈值和
有限摘要到机器可读相位兼容权重 `W_D,W_{ell,a}` 的物化。

## 6. 第一版已生成的机器输入

新增 `h4-pdec-lhb-column-phase-blocks.json` 与 `h4-pdec-lhb-column-phase-blocks.md` 后，
`Q=2310`、`13<=p<=47` 的 LHB column rows 已经物化为机器可读行：

```text
rows = 45；
p_values = 13,17,19,23,29,31,37,43,47；
all_empty_anomaly_rows_pass = true。
```

其中三类空异常块已经有 `phase_block=[]` 与 `bound=0`：

```text
CC-LHB-AFFINE；
CC-LHB-NEGDELTA；
CC-LHB-UNBRIDGED。
```

这些行在有限 `Q=2310` 范围内可以作为空异常块 `A` 行。`CC-LHB-WHOLEDEF` 与
`CC-LHB-BRIDGED` 已输出支撑相位块，但当前仍标为 `diagnostic-phase-support`：
它们需要额外证明正式坏窗集合 `S` 的投影关系和容量含义，才能进入最终对偶证书。
补充文档 `h4-pdec-lhb-support-to-capacity-transfer.md` 已证明转移规则：若没有相位指示假设、
多重度界 `M(t)` 或允许全集 `Z_LHB` 投影容量，不能把 `bound=phase_block_size` 当作
`sum_{t in C}g(t)` 的上界。
进一步新增 `h4-pdec-lhb-multiplicity-cap-route.md` 后，多重度路线已固定为正式合同：
只要同一 `(p,Q,S,tau)` 下给出 `M(t)` 并证明 `g(t)<=M(t)`，`WHOLEDEF/BRIDGED`
即可用 `bound=sum_{t in C}M(t)` 升级为容量行。
新增 `h4-pdec-lhb-multiplicity-cap-certificate.json/md` 后，`Q=2310` 的第一版 `M(t)`
已经物化为高层 CRT 补洞完成数，且 `WHOLEDEF/BRIDGED` 块全部给出 `bound=0`。
这些行当前的使用范围是 LHB allowed-set 分支；进入全局 PDEC 还需证明当前 `S subset Z_LHB`。
新增 `h4-pdec-lhb-attachment-lemma.md` 后，该包含关系在 LHB 型坏窗分支中已经证明；
全局剩余改为证明正式 PDEC 坏窗的分类：LHB 型接入，非 LHB 型进入命名出口。
新增 `h4-pdec-bad-window-classification-lemma.md` 后，该分类已定式化为 `SAE` 或
`LHB-PDEC` 或 `Routed-PDEC` 三分支；它仍不排除非 LHB 出口。
新增 `h4-pdec-homogeneous-splitting-lemma.md` 后，口径混合不再是数学出口，而是
无损拆分预处理；拆分后的子族再分别进入上述三分支。

因此 V1 账本已经从“系数来源登记”推进到“部分相位块物化”。它仍不是最终
`A,b,E,e`，因为有限列见证半径、RCI/CDB 摘要界值和条件路由行尚未物化相位块。

## 7. 下一步最小工程任务

下一步应继续扩展审计脚本，为剩余 column rows 输出以下机器可读对象：

```text
row_id；
Q；
phase_block: [t_1,...,t_k]；
bound；
source_hash；
normalization；
admissibility: finite / conditional；
excluded_exit。
```

优先级更新为：

1. 将 `diagnostic-phase-support` 行升级为有正式 `S subset Z` 证明的容量行；
2. 为 `CC-FIN-RADIUS-1000` 与 `CC-FIN-TIGHT-*` 输出相位块；
3. 为 `CC-COND-*` 写出实际出口路由定理编号与阈值函数。
