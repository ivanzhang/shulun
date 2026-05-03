# D4/R5 H80 资源锁候选闭合：审稿级状态报告

## 已闭合范围

本轮证书链条闭合的是 R5 异常层中 H80 资源锁候选单元的固定成员层泛函极值排除。

已验证：

1. H80 四个资源锁单元的整数层泛函查询全部通过。
2. H80 单元内 17 个整数候选行的成员签名逐行分解完成。
3. 17 个候选行的 34 个左右半单元固定成员证书全部通过。
4. 六类目标泛函 `U,V,L_light,L,E2,E2-L2/20` 的最坏区间均通过外向舍入区间审计。
5. 最小外向舍入下界为 `3.76564855398413484253367188062E-10`，对应 `V` 泛函。

## 证书文件

- `docs/d4-r5-light-H80-layer-functional-certificate.json`
- `docs/d4-r5-H80-unified-candidate-boxes.json`
- `docs/d4-r5-H80-membership-cell-decomposition.json`
- `docs/d4-r5-H80-one-sided-fixed-membership-all17-batch.json`
- `docs/d4-r5-decimal-audit-by-functional-worst.json`
- `docs/d4-r5-budget-interval-audit-by-functional-worst.json`
- `docs/d4-r5-outward-interval-audit-by-functional-worst.json`
- `docs/d4-r5-review-grade-consistency-audit.json`

## 不能声称的范围

当前还不能声称全文目标命题已经证明。剩余工作是：

1. 将同一证书管线推广到 R5global1--R5global4 的全部候选单元。
2. 将 R5global 闭合重新接回 USC、DBA、JND、列命题等全局依赖。
3. 抽取最终阈值并完成阈值以下有限验证。

## 审稿级结论

当前 H80 资源锁候选闭合链条已经达到可审查证书状态；它是 R5global 全局闭合的局部样板，而不是全文主定理的完成证明。
