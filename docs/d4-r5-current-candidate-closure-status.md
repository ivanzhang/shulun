# D4/R5 当前有限证书候选全集闭合状态

## 已完成

从当前有限窗口/模板证书中提取所有候选/见证行，得到 41 个候选整数行：

- 来源：light H80、highmass、tail-absent frontier、four-point valley 等现有证书。
- 证书：`docs/d4-r5-current-candidate-x-set.json`。

对 41 行的 82 个左右半单元运行固定成员层泛函根证书：

- 证书：`docs/d4-r5-current-candidates-one-sided-batch.json`。
- 结果：`root_boxes=0`，`unresolved=0`。

对六类泛函最坏区间做外向舍入审计：

- 证书：`docs/d4-r5-current-candidates-outward-audit-by-functional-worst.json`。
- 结果：`all_certified=true`。
- 最小外向下界：`3.7656485368520207187E-10`，对应 `V` 泛函。

## 严格边界

这闭合的是“当前有限证书体系已枚举候选全集”，不是完整 R5global 相位模板全集。

要宣称 R5global1--R5global4 无条件闭合，还需要：

1. 一个相位模板枚举器，生成所有可能满足 R5global 约束的固定成员单元；
2. 一个覆盖证明，说明枚举器输出没有遗漏；
3. 将当前外向舍入固定成员管线作用于枚举器输出的全部单元；
4. 汇总生成全局最小余量证书。
