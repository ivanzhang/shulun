# MFAC 半素数局部自然性分解二分设计

## 目标

固定任意两个不同素数 `p < q` 及最小 Möbius 三项：

```text
(p, q, +log p)
(q, p, +log q)
(p*q, 1, -log(p*q))
```

研究一个条件性、可反驳的二分：若候选三项 declaration 完全由既有的局部乘法资料决定，
且不使用下游对象，则它只能因子化到 canonical RIW/Buchstab 行，或在每个同-row
纤维内精确零和。该二分不否定数学上可能存在新的 noncanonical emitter；它反而精确
规定该 emitter 必须额外提供何种独立算术信息。

## 备选路径与选择

- **A：局部自然性分解二分（采用）**：以最小 `p < q` triad 为对象，先排除从已有
  divisor/LPF/word/parity 资料重命名得到 actual dispatch 的可能性。
- B：直接寻找新的 alpha/delta 行锚定公式：若存在会更强，但目前没有独立的 declaration
  line，容易把下游表值误写为来源恒等式。
- C：扩展 rough-cofactor 递推：只能传播已有 signed seed，不能生成 first seed。

## 非目标

- 不证明 RH、零点排除、`ψ` 平滑误差或任意平方根级估计。
- 不证明所有 noncanonical pre-Cauchy arithmetic identity 在数学上不存在。
- 不把本二分中的有限枚举、schema、synthetic fixture 或现有 global Möbius payload 称为
  actual signed source。
- 不从 payment、Phi pushforward、Cauchy/dispersion、零行覆盖、terminal 表或
  canonical 后验表恢复候选 declaration。

## 条件性模型

候选 declaration 为一个在 Cauchy 前定义的映射：

\[
\mathscr D(p,q,d)=(r,\varepsilon,L,\iota),\qquad d\in\{p,q,pq\},
\]

其中 `r` 是 row key，`ε` 是 orientation，`L` 是 local factor，`ι` 是候选的
origin selector。候选必须满足以下审计公理：

1. **局部可决定性**：所有字段只读取 `(p,q,d)` 的 divisor、cofactor、ordered factor
   word、LPF owner、squarefree/depth parity 与显式局部对数权；不读取下游对象。
2. **素因子重命名自然性**：交换 `p,q` 时，候选仅按预先声明的 branch permutation
   变换；不得由 terminal 选择临时决定 branch。
3. **局部系数律**：row coefficient 由对应纤维中 `-μ(d) log d` 乘以声明的局部因子
   相加得到；不得从 row-level coefficient table 回填。
4. **无新增原子资料**：`ι` 亦由第 1 项资料确定，且不额外绑定 actual primitive unit、
   exact `(u,v)` 或独立 alpha/delta identity。
5. **canonical 可识别性**：若 row key 只编码 RIW/Buchstab 的已存在 canonical decision
   tree 行，则显式标为 canonical，不能改名为 noncanonical。

这些是被审计的假设，不是已经证明的数学公理。任何候选若不满足其中一项，必须明确报告
它实际引入的新字段和来源恒等式。

## 待检验二分

对满足上述公理的候选，审计器只允许以下两类结果：

1. **Canonical factorization**：三项的 row key 经局部资料投影后落入 canonical
   RIW/Buchstab row；该候选不产生 actual noncanonical emitter。
2. **Rowwise cancellation**：若三项落入同一 row，则该 row 的局部系数必须被直接计算为
   \(\log p+\log q-\log(pq)=0\)，而不是把 global 零和误称为 source。

任何同时满足局部可决定性、自然性和局部系数律，却既非 canonical factorization 又不
发生 rowwise cancellation 的最小实例，都是对本二分的 collision certificate。该反例必须
完整列出三个输入、branch symbol、row key、orientation、local factor、origin selector、
exact `(u,v)`（若声称 actual primitive unit）及不依赖下游的系数恒等式。

## 真正正向出口

若二分在既有候选族中成立，唯一保留的正向门是：

```text
SemiprimeTriadDeclarationLineFromIndependentArithmeticIdentity
```

它必须提供不能由 divisor/LPF/word/parity 资料恢复的 primitive arithmetic functional，
并同时给出：

```text
origin_selector
actual_emitter_registered
orientation
local_factor
exact (u,v)
prepushforward alpha/delta identity
```

这才可进入 `PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket`；缺任何一项均只
登记为 source-missing 或 named return，不能进入 RH 链条。

## 最小验证矩阵

首个样本固定 `(p,q)=(2,3)`：

| candidate family | 预期结果 | 允许的结论 |
| --- | --- | --- |
| global Möbius/Lambda | global 零和 | 不是 row declaration |
| D/E colored divisor word | global transport | 无 actual primitive binding |
| LPF/Phi factor word | canonical/support | 无 signed emitter |
| square-base/parity | 后验 state | 无 orientation source |
| canonical RIW/Buchstab T1 | canonical factorization | 仅 scoped canonical promotion |

审计输出必须含：

```text
current_corpus_has_independent_semiprime_declaration_line=false
conditional_factorization_dichotomy_proved=<仅在明确公理范围内>
minimal_collision_certificate_present=false
mathematical_nonexistence_proved=false
rh_proved=false
row_column_unconditional_closed=false
```

## 计划产物与验证

在用户审阅本规格后新增：

- `experiments/prime_matrix_mfac_semiprime_local_naturality_factorization_audit.py`
- `experiments/prime_matrix_mfac_semiprime_local_naturality_factorization_audit_test.py`
- `docs/monograph/prime-matrix-mfac-semiprime-local-naturality-factorization-audit.md`
- `docs/monograph/prime-matrix-mfac-semiprime-local-naturality-factorization-audit.json`

测试至少覆盖：五个现有候选族的分类、`(2,3)` canonical 例、synthetic collision 的捕获、
downstream 依赖拒绝、以及 non-RH 边界字段。实现前先用红色测试固定：任何没有独立来源
恒等式的 noncanonical row 都必须被拒绝。

用法示例：

```bash
python3 experiments/prime_matrix_mfac_semiprime_local_naturality_factorization_audit.py
python3 -m unittest experiments/prime_matrix_mfac_semiprime_local_naturality_factorization_audit_test.py -v
```
