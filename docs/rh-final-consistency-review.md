# RH 反例矛盾场全文最终一致性总审查

本文对当前 RH 反例矛盾场文档包做最终一致性审查。审查目标不是宣称 RH 已证明，而是确认：主链、审稿矩阵、索引、归档清单、验证证书和未跟踪文件说明保持一致；所有结论均使用“条件化闭合/审稿矩阵闭合/待无条件化”的诚实口径。

## 1. 主链状态

当前主链为：

`PC1 解析异常 -> PC2 CRT 基线 -> PC3-OV2 过疏桥接 -> PC4 终端无循环 -> PC4-Dual/DGap 过密匹配 -> 外部事件吸收`。

对应最终审查入口：

1. PC1：`docs/rh-pc1-analytic-input-citation-audit.md`，并由 `docs/rh-pc1-external-input-standardization-audit.md` 标准化外部解析输入；
2. PC2：`docs/rh-pc2-baseline-unconditional-audit.md`；
3. PC3：`docs/rh-pc3-ov2-upstream-unconditional-audit.md`；
4. PC4 内部终端：`docs/rh-pc4-terminal-final-no-cycle-audit.md`；
5. PC4 外部事件：`docs/rh-pc4-external-event-absorption-audit.md`；
6. PC4-Dual/DGap：`docs/rh-pc4-dual-dgap-event-match-audit.md`，并由 `docs/rh-dgap-projection-line-by-line-audit.md`、`docs/rh-dgap-lowdim-extraction-line-by-line-audit.md`、`docs/rh-dso-pi-squarefunction-bridge-audit.md`、`docs/rh-fct-seed-isomorphism-audit.md`、`docs/rh-fourier-vaaler-tail-uniform-audit.md` 与 `docs/rh-fct-closure-no-cycle-final-audit.md` 补强投影、低维抽取、DSO/PI 桥接、FCT_seed 同型、尾项和 FCT 无循环接口；
7. 全局接口：`docs/rh-global-interface-consistency-audit.md`；
8. NRC/EXT：`docs/rh-nrc-ext-final-citation-audit.md`；
9. DSO/容量：`docs/rh-dso-capacity-final-audit.md`；
10. LSMP/FCT/CapacityFail：`docs/rh-lsmp-fct-capacity-final-audit.md`。

## 2. 口径审查

允许表述：

- “条件化反例矛盾场骨架”；
- “审稿矩阵闭合”；
- “接口已拆解为无条件核心与已命名事件输出”；
- “剩余义务为外部定理页码、容量定理细节和最终论文整合”。

禁止表述：

- “RH 已证明”；
- “无条件证明已完成”；
- “顶刊已通过”；
- “所有外部输入已完全逐页引用”。

当前总攻文档 `docs/rh-contradiction-field-final-assault.md` 已保留“不能写成 RH 已证明”的明确口径。

## 3. 索引与归档一致性

正式入口文件为：

- `docs/final-submission-manifest.md`；
- `docs/final-archive-report.md`；
- `docs/references-and-appendices.md`；
- `docs/rh-contradiction-field-final-assault.md`。

本轮新增的审稿矩阵均已加入索引/归档清单。历史未跟踪实验文件、扫描输出和草稿不纳入正式审稿入口，避免与当前主链口径冲突。

## 4. 验证状态

本轮所有归档提交均使用同一组验证：

- `python3 experiments/extract_p0.py --constants docs/explicit-p0-constants.structured-conservative.json --max-log 100 --step 0.1`；
- `python3 experiments/verify_small_prime_square.py --max-log 5 --out docs/finite-verify-exp5.json`；
- `python3 -m py_compile experiments/extract_p0.py experiments/verify_small_prime_square.py`；
- 针对本次文件的 `git diff --check`。

当前证书状态保持：

- 理论阈值抽取：`log_P0_upper=3.5`；
- 有限验证：`P<=floor(exp(5))=148`，`ok=true`。

这些验证属于行列命题/阈值证书链，不等价于 RH 证明验证。

## 5. 发现的问题与修正口径

本次总审查发现旧文件中仍存在若干历史“下一步”表述，例如“下一步继续审查 FCT/SC/A”或“上游 PC3 尚待核查”。这些已被后续矩阵覆盖。正式口径以本文件第 1 节列出的最终审查入口为准。

对于旧历史文件，不需要逐字重写所有探索记录；只需在主入口与最终清单中明确最新状态，避免审稿入口引用过时路线图。

## 6. 最终审查结论

**Theorem Final-Consistency-Review（全文一致性审查结论）。** 当前文档包在主链入口层面是一致的：PC1/PC2/PC3 上游输入、PC4 内部终端、PC4 外部事件、Dual/DGap、NRC/EXT、DSO/容量、LSMP/FCT/CapacityFail 均有对应审稿矩阵；正式结论保持条件化和待无条件化口径；未跟踪实验文件未纳入正式审稿包。

**证明。** 逐项核查第 1 节入口与最终索引清单；核查总攻文档口径；核查验证证书；核查未跟踪文件说明。所有正式入口均指向当前最新矩阵，且没有把 RH 称为已证明。证毕。

## 无条件化攻坚续篇

继续向 RH 无条件证明推进的剩余条件割集与优先顺序见 `docs/rh-unconditional-proof-roadmap.md`；CapacityFail 全局绑定表见 `docs/rh-capacityfail-binding-table.md`。

## 7. 下一步建议

若继续推进，最优不是再新增分支，而是进入“论文定稿编辑模式”：

1. 把上述审稿矩阵合并进一篇连贯论文；
2. 给 `EXT-*` 外部定理补精确页码/定理号；
3. 选择 Chebyshev 权或无权口径并全文统一；
4. 将未跟踪实验文件分类归档或保持排除；
5. 对最终 PDF/LaTeX 做交叉引用检查。
