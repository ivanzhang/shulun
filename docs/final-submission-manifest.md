# 最终归档提交清单

本次归档固定当前定稿主链：列命题闭合、行命题当前闭合稿、显式阈值抽取与小素数有限验证证书。

## 纳入提交的文件

- `docs/final-archive-report.md`：最终归档报告。
- `docs/references-and-appendices.md`：审稿版引用与附录入口。
- `docs/final-interface-index.md`：最终接口索引与一致性口径。
- `docs/final-cross-reference-matrix.md`：最终符号交叉编号矩阵。
- `docs/final-top-journal-unconditional-review.md`：顶刊无条件证明标准最终复核判定。
- `docs/concluding-perspective.md`：论文结语式总结评述。
- `docs/rh-rigidity-exploration.md`：从局部刚性到 RH 全局波动控制的探索框架。
- `docs/rh-double-contradiction-field.md`：RH 双重矛盾场严格路线草案。
- `docs/rh1-weak-attack-plan.md`：RH-1 weak 到筛余空洞投影的专攻计划。
- `docs/rh1c-sifted-hole-explicit-formula.md`：RH-1C 筛余空洞函数与显式公式桥接。
- `docs/rh1c-buchstab-weight-construction.md`：RH-1C Buchstab 覆盖权构造。
- `docs/rh1c-acc-desynchronization-lemma.md`：RH-1C ACC 不同步引理攻坚。
- `docs/rh-offline-zero-prime-count-contradiction.md`：离线零点素数计数超界与方阵/CRT 矛盾场。
- `docs/rh-pc3-prime-sparse-to-cover-excess.md`：PC-3 素数过疏到允许覆盖过剩。
- `docs/rh-pc3-candidate-overlap-two-tasks.md`：PC-3 候选基线与 overlap-energy 两任务。
- `docs/rh-pc3-formal-theoremization.md`：PC-3 正式定理化证明稿。
- `docs/rh-ov2-overlap-terminal-proof.md`：OV-2 overlap 大能量到 D 组终端接口。
- `docs/rh-ov2-admissible-anchor-interface.md`：OV-2 允许锚语义接口。
- `docs/rh-ov2-phase-pushforward-interface.md`：OV-2 相位推送接口。
- `docs/rh-ov2-main-layer-capacity-interface.md`：OV-2 主层容量接口与条件化闭合。
- `docs/rh-lv-low-volume-principle.md`：LV 低体积原则编号引理。
- `docs/rh-pc3-ov2-bridge-theorem.md`：PC-3+OV-2 素数过疏桥接定理。
- `docs/rh-pc1-offline-zero-smooth-window.md`：PC-1 离线零点到平滑素数异常窗口。
- `docs/rh-pc2-li-crt-baseline-match.md`：PC-2 连续零频与 CRT 零频基线匹配。
- `docs/rh-pc4-final-exclusion-framework.md`：PC-4 最终排斥框架与 RH 总攻地图。
- `docs/rh-pc4-pi-seed.md`：PC4-PI 跨尺度投影能量种子命题。
- `docs/rh-pc4-pi-cap-carleson.md`：PC4-PI 跨尺度 Carleson 容量上界路线。
- `docs/rh-pc4-dense-scale-orthogonality.md`：PC4-PI 密集尺度正交接口。
- `docs/row-column-reduction-formal-appendix.md`：A/B 行列归约正式附录证明稿。
- `docs/ab-to-d-interface-match.md`：A/B 到 D 定义逐项匹配附录。
- `docs/d-structure-formal-appendix.md`：D 组 Structured-EHPD 正式附录证明稿。
- `docs/d-structure-line-by-line-expansion.md`：D 组压缩证明逐行展开附录。
- `docs/external-theorem-package.md`：外部定理包与精确引用模板。
- `docs/ext-citation-final-audit.md`：EXT 外部定理精确引用最终审查表。
- `docs/constants-absorption-final-audit.md`：常数吸收最终核对表。
- `docs/constants-numbered-inequalities.md`：常数吸收编号不等式证明。
- `docs/bg-rks-block-match.md`：BG/RKS 分区逐块匹配附录。
- `docs/m5-explicit-gap-lemma.md`：Lemma M5 覆盖缺口显式化附录。
- `docs/critical-bucket-single-hit-sieve-attack.md`：主论文/主证明文档。
- `docs/explicit-p0-constants.status.md`：显式常数与阈值抽取状态记录。
- `docs/explicit-p0-constants.structured-conservative.json`：最终保守结构常数包。
- `docs/explicit-p0-structured-conservative-result.json`：理论阈值抽取证书，给出 `log_P0_upper=3.5`。
- `docs/finite-verify-exp5.json`：`P<=floor(exp(5))=148` 的有限验证证书。
- `experiments/extract_p0.py`：显式阈值抽取脚本。
- `experiments/verify_small_prime_square.py`：小奇素数有限验证脚本。

## 未纳入提交的文件

当前工作树中仍有大量未跟踪探索性实验脚本、扫描输出和历史审查草稿。这些文件用于研究过程，不作为本次定稿主链证据提交，避免审稿入口被历史候选路线和临时数据干扰。

## 最终覆盖口径

- 理论证明覆盖：`P>exp(3.5)`。
- 有限验证覆盖：`P<=exp(5)`。
- 两段重叠，因此覆盖全部奇素数。

## 提交前校验

- `python3 experiments/extract_p0.py --constants docs/explicit-p0-constants.structured-conservative.json --max-log 100 --step 0.1`
- `python3 experiments/verify_small_prime_square.py --max-log 5 --out docs/finite-verify-exp5.json`
- `python3 -m py_compile experiments/extract_p0.py experiments/verify_small_prime_square.py`
- `git diff --check` 针对本次归档文件通过。
