# 交接给新 codex 会话

> 旧 codex 会话因模型限流卡死。Claude 接手完成它最后一句任务后，写下此交接文档。
> **接手时间**: 2026-05-05
> **覆盖范围**: 仅完成 codex 最后一句明确任务 (运行 95% 热门带分类器并取回结果)，
> 其它工作 (论文主线、§242/§243/§244 行命题分析等) 留给新 codex 会话继续。

---

## 1. 旧 codex 会话最后状态

**最后一条 codex 自述**:
> "热门带暴露了真实分流：部分强热门位移不满足 C13 付款，需要出口而不是硬塞入局部链。
>  我会把这做成分类合同：闭合窗口与 PDEC/SAE 出口窗口分开。"
> "分类器已实现。现在运行 95% 热门带，看哪些窗口闭合、哪些进入出口。"
> "还在跑；这个分类器会逐个热门窗口调用完整 C13 链，耗时略长。我现在取回结果。"

**卡死原因**: 模型限流 (rate limit)，并非分类器逻辑问题。

**实现文件** (codex 已写好但未提交):
- `experiments/prime_matrix_alpha_tail_tailpair_c13_hotband_exit_classifier.py` (9431 字节)
  - 入口: `hotband_exit_package(...)`
  - 默认参数: `--p-list 5003,10007 --beta 0.95 --finite-p-cut 1000 --eta 0.04`
  - 出口分类: `C13Closed / TargetSyntaxOrRatioExit / SlackFloorExit / ActiveTemplateExit / FiniteSourceExit / ResidualPDECOrSAEExit`

---

## 2. 接手执行的最后一步

Claude 用 codex 预设的命令行参数运行了分类器：

```bash
cd experiments && \
python3 prime_matrix_alpha_tail_tailpair_c13_hotband_exit_classifier.py \
  --p-list 5003,10007 --beta 0.95 --finite-p-cut 1000 --eta 0.04 --format table
```

完整输出已保存到 `docs/c13_hotband_exit_classifier_run_20260505.txt`。

---

## 3. 关键结果摘要 (codex 等待的分流答案)

| 维度 | 数值 |
|------|------|
| 窗口总数 (P∈{5003,10007}, β=0.95) | 18 |
| C13 闭合窗口 | **11** |
| 出口窗口 | **7** |
| 出口类型分布 | `{'SlackFloorExit': 7}` |
| 其它出口 (TargetSyntax/Ratio/ActiveTemplate/FiniteSource/Residual) | **0** |
| min_closed_source_margin | 8.340921 |
| min_exit_res_margin | -858.879113 |

**强分流事实**:
1. **所有出口窗口的 syntax/ratio 均通过** — 即出口不是来自语法或比率结构破坏。
2. **所有出口都集中在 SlackFloorExit** — 即 `slack_floor_pass` 与 `resonance_floor_pass`
   失败导致 `local_chain` 与 `full_postlow` 双假。
3. **没有窗口落入 ResidualPDECOrSAEExit** — 即 codex 预想的"PDEC/SAE 残余出口"在此采样下空集。

**闭合 / 出口窗口具体清单**:

闭合 (11):
```
5003:8192:-36, 5003:8192:-180, 5003:8192:-360,
10007:16384:-900, 10007:16384:-180, 10007:16384:-360,
10007:16384:-252, 10007:16384:-540, 10007:16384:-504,
10007:16384:-396, 10007:16384:-720
```

出口 (7, 全为 SlackFloorExit):
```
5003:8192:-144, 5003:8192:-288, 5003:8192:-216,
10007:16384:-72, 10007:16384:-1800, 10007:16384:-144, 10007:16384:-108
```

---

## 4. 给新 codex 会话的下一步建议

新会话恢复后，建议直接处理以下三个最小硬点 (按优先级)：

### 4.1 SlackFloorExit 的统一处理合同 (最紧急)

当前观察到 7/18 = 39% 的强热门窗口在 SlackFloorExit 出口。codex 之前的语义里
"出口不是硬塞入局部链"——但出口比例如此之高时，必须给出**统一的出口处理证书**：

- 写一个 `c13_hotband_slack_floor_exit_handler` 包，证明：
  当某热门窗口落入 SlackFloorExit 时，行命题在该窗口仍可由 **endpoint persistence** 或
  **alpha-tail additive energy** 的另一条独立链承担。
- 否则 39% 的"硬塞失败"会成为整体闭合的真空洞。

### 4.2 提高 β 与 P 范围验证类型分布是否稳定

当前只测了 β=0.95 与 P∈{5003,10007}。建议补 β∈{0.90, 0.85} 与 P∈{20011, 50021}，
验证：
- 是否仍只有 SlackFloorExit 出口
- 出口比例是否会上升超过临界 (例如 50%)

如果出口比例超过 50%，4.1 的出口处理证书就必须前置成"主链"。

### 4.3 闭合窗口的 source_margin 下限是否可解析下界化

当前 `min_closed_source_margin = 8.340921` (来自 5003:8192:-36)。
若要无条件证明，需把这个数值下界升级为 P 的解析下界 (例如 ≥ c·log P)。
这是把数值证据升级为定理的关键瓶颈。

---

## 5. 与论文主线的衔接

旧会话的论文主线 (`docs/generalized_framework.md`) 已写到 §244 行命题分析。
**主线与本任务的关系**:

- 主线 (§198-§244) 是论文骨架: H_P 的行/列命题、零行 i_min > P 的论证。
- 本任务是支线工具链: C13 局部链在 alpha-tail-tailpair 框架下的热门带分类，
  支线为主线某一节 (具体节号 codex 未明确指定) 提供数值/结构证书。

新 codex 会话**不要**把这两条线混淆：
- 主线的下一步是 §245 (零行行号 i_min > P 的递归剥离构造)。
- 支线的下一步是 §4.1 (SlackFloorExit 处理合同)。

---

## 6. 未提交的工作清单

`git status` 此刻应显示:
```
?? AGENTS.md
?? HANDOFF_CODEX.md                                                       (本文)
?? docs/c13_hotband_exit_classifier_run_20260505.txt                      (运行结果)
?? experiments/prime_matrix_alpha_tail_tailpair_c13_hotband_exit_classifier.py  (codex 写好但未提交)
```

Claude 准备把这四份一起提交，提交信息：
```
Add C13 hotband exit classifier and run results
```

新 codex 会话可以从此提交开始接手。

---

## 7. 不要重做的事

- 不要重跑 `--p-list 5003,10007 --beta 0.95 --finite-p-cut 1000 --eta 0.04`
  这个组合 — 结果已在 `docs/c13_hotband_exit_classifier_run_20260505.txt`。
- 不要重写 `prime_matrix_alpha_tail_tailpair_c13_hotband_exit_classifier.py` —
  它已经是 codex 最新版本，只是当时没来得及提交。
- 不要回头改 §242/§243/§244 — 那是 Claude 在 codex 卡死前写的行命题分析章节，
  与本任务无直接关系；如果新 codex 觉得需要改，请明确征求用户同意。

---

**交接完成**。 — Claude
