# 最终审稿包一致性总审查报告

## 1. 检查范围

本轮检查最终审稿入口、附录、证书和脚本：

- `docs/final-submission-manifest.md`
- `docs/references-and-appendices.md`
- `docs/final-interface-index.md`
- `docs/formal-theoremization-review.md`
- `docs/top-journal-proof-audit.md`
- A/B/C/D 各定理化附录
- RKS、NRC、FCT 子附录
- 显式常数包与有限验证证书

## 2. 互链检查

最终入口文件中的文档与脚本路径引用均已检查，未发现缺失文件。

## 3. 证书复现

以下命令已重新运行并通过：

- `python3 experiments/extract_p0.py --constants docs/explicit-p0-constants.structured-conservative.json --max-log 100 --step 0.1`
- `python3 experiments/verify_small_prime_square.py --max-log 5 --out docs/finite-verify-exp5.json`
- `python3 -m py_compile experiments/extract_p0.py experiments/verify_small_prime_square.py`
- `git diff --check` 针对最终审稿包文件通过。

复现结果：

- 理论抽取：`log_P0_upper=3.5`；
- 有限验证：`P<=148` 的 33 个奇素数全部通过；
- 最差行/列素数数均为 1。

## 4. 口径修正

本轮发现并修正了 `docs/rks-bridge-partition.md` 中旧的 `RKS-bridge-minor` 风险表述：第 4--6 节现标为历史风险定位，第 7--9 节为最终口径。当前 RKS 剩余为 `RKS-parameter-audit` 与最终引用文字附录化，不再要求新增 `RKS-bridge-minor` 数论估计。

## 5. 当前最终剩余义务

当前审稿包的剩余义务均为可核对接口，而非新的大黑箱：

1. A/B：核对小因子锁定、双粗主体、尾部锚三层不重不漏；
2. C：将 BG/Weil/Selberg/Vaaler/Vaughan 引用文字正式 bibliography 化；
3. D：统一 OMR/CGTP/LSMP、NRC、FCT 的符号和常数；
4. 证书：保持理论 `P>exp(3.5)` 与有限验证 `P<=exp(5)` 的两段覆盖口径。

## 6. 总结

最终审稿包已经具备统一入口、附录索引、bibliography 草稿、显式常数证书和有限验证证书。主文档历史探索段仍保留，但最终接口索引已明确规定：若历史段与最终接口文件冲突，以最终接口文件为准。
