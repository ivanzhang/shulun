# 合著稿关键证明链条优化审查归档

日期：2026-05-02

## 1. 审查结论

本轮新增 `docs/monograph/key-proof-chain-optimization-audit.md`，把合著稿主线压缩为三条可审稿链：

- 方阵行列链条：`PM-1` 到 `PM-8`；
- 二点筛链条：`TP-1` 到 `TP-9`；
- RH 反例矛盾场链条：`RH-1` 到 `RH-5`。

## 2. 核心状态

- 二点筛 BMD 链条在引用 DI/BFI 外部深定理时可标注为 `External-theorem closed`。
- 二点筛完全自足无黑箱版仍需文内证明 `KLS-window`。
- 方阵行列链条应继续聚焦 `Structured-EHPD` 和 Tail anchors。
- RH 链条仍是 verification/referee package，不能宣称无条件证明。

## 3. 本轮补正重点

本轮补正的关键不是新证明，而是防止逻辑状态混淆：

```text
existence/non-empty rigidity
≠ signed spectral distribution
≠ Kloosterman large-sieve cancellation
```

因此 `RC-Prime` 可支持 `BMD-Zero`，但不能替代 `BMD-Char`；实验扫描可支持结构洞察，但不能替代定理证明。

## 4. 后续义务

下一步最优工程义务：

1. 将 `TP-1` 到 `TP-9` 写成正式定理链；
2. 将 DI/BFI 的引用形式做成主稿中的外部定理模板；
3. 完成 `KLS-window` 变量适配核查表；
4. 清洗旧章节中过强的“无条件闭合”措辞。
