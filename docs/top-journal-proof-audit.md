# 顶级数学期刊审稿级复核清单

统一最终接口索引见 `docs/final-interface-index.md`。

本文档记录对行命题与列命题归档稿的审稿级复核。目标不是重复历史探索，而是明确最终主链、可接受证据、以及仍需顶刊级补强的接口。

## 1. 当前可确认的闭合结构

- **有限验证闭合**：`docs/finite-verify-exp5.json` 证明 `P<=floor(exp(5))=148` 的 33 个奇素数全部通过，最差行/列素数数均为 1。
- **机械阈值抽取**：`docs/explicit-p0-structured-conservative-result.json` 给出保守常数包下 `log_P0_upper=3.5`。
- **两段覆盖关系**：`exp(3.5)<exp(5)`，因此理论段与有限验证段重叠。
- **证书可复现性**：`experiments/extract_p0.py` 与 `experiments/verify_small_prime_square.py` 可复现上述两个 JSON 证书。

## 2. 顶刊审稿首先会质疑的点

### R1：历史探索段与最终主链混杂

主文档前 1200 多节保留大量“候选”“仍需”“硬点”表述。若不加入口说明，审稿人会误以为主证明仍未闭合。

**修复**：已在 `docs/critical-bucket-single-hit-sieve-attack.md` 文首加入审稿入口，声明最终主链以第 1273--1275 节和状态文档第 90--97 节为准，早期段落作为探索记录。

### R2：常数包自洽不等于深层结构输入已证

`extract_p0.py` 只能验证常数之间的不等式关系；它不能替代 OMR/CGTP/LSMP、Tail-log4、Bilinear-prime-sieve-average 等结构引理的数学证明。

**修复**：在第 1275 节把“机械抽取义务”和“数学证明义务”分离。最终定理只能在这些结构输入被证明后无条件成立。

### R3：行命题与列命题的接口需统一命名

早期文本中行命题、列命题、坏窗口、单次锚筛、Structured-EHPD 等术语多次变化。顶刊审稿需要固定最终命题名称和依赖方向。

**修复方案**：第 1275 节采用统一接口：`Column-Closure`、`Row-Closure`、`Structured-EHPD`、`Tail-log4`、`OMR/CGTP/LSMP`、`Finite-Verification`。

### R4：有限验证只验证小素数，不证明大素数

有限验证证书本身可靠，但必须明确它只覆盖 `P<=exp(5)`，大素数完全依赖理论段。

**修复**：最终口径固定为“两段覆盖”，不再尝试宣称理论从 `P=5` 开始。

### R5：顶刊级“完整无条件证明”仍需逐项补强

当前归档稿已形成完整的证明框架和常数抽取闭环，但顶刊级无条件版本还需要把所有结构输入写成可逐行审查的定理证明，尤其是 OMR/CGTP/LSMP 与 Tail-log4 的标准解析输入。

**修复方向**：不伪造证明；将这些输入列为第 1275 节的审稿义务，并给出每项需要的精确输出形式。

## 3. 当前结论的严格表述

在当前文档状态下，最严谨的结论应表述为：

> 若第 1275 节列出的结构输入均按所给常数包无条件证明，则由机械阈值抽取与有限验证证书可推出方阵行列命题对全部奇素数成立。

不能表述为：

> 本文已经达到无需额外结构输入的顶级期刊最终无条件证明。

除非后续逐项补全第 1275 节所有输入的完整证明。

## 4. 下一轮真正补强优先级

1. `Tail-log4` 三项已在 `docs/tail-log4-theoremization.md` 拆成 TL4-L/TL4-S/TL4-M；RKS 分区与参数账本见 `docs/rks-bridge-partition.md`、`docs/rks-parameter-audit.md`。下一步主要是最终引用文字与附录化。
2. `OMR/CGTP/LSMP` 已在 `docs/omr-cgtp-lsmp-theoremization.md` 拆成形式化组合定理；NRC 与 FCT/Tree-WFE 已分别在 `docs/nrc-theoremization.md`、`docs/fct-tree-wfe-theoremization.md` 定理化，下一步主要统一符号并审查行/列归约 A、B。
3. 行命题与列命题的最终归约已在 `docs/row-column-reduction-theoremization.md` 写成 Theorem A/B；下一步核对三层分解与符号统一。
4. 保留有限验证作为附录证书，不让数值验证承担大素数理论义务。
