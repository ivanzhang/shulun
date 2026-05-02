# 关键证明链条优化审查

## 0. 审查目的

本文档只做一件事：把合著稿中仍在主线上的关键逻辑链条压缩为可审稿对象，并明确每一条链的闭合等级、剩余输入和优化优先级。

状态标签如下：

- `Proved-in-text`：正文已有逐步证明；
- `Reduction-closed`：已严格归约到更小接口；
- `External-theorem closed`：引用明确外部深定理后闭合；
- `Referee-block`：已有证明框架，但仍需逐行审稿核查；
- `Not claimed`：不能作为无条件结论使用。

## 1. 方阵行列链条

当前最清晰的审稿链条应写为：

```text
PM-1 Matrix model
=> PM-2 CRT nonzero skeleton
=> PM-3 large-factor non-reuse
=> PM-4 diagonal/slope locks
=> PM-5 tail anchors
=> PM-6 A/B structured reduction
=> PM-7 Structured-EHPD exclusion
=> PM-8 row/column closure
```

### 1.1 已稳定部分

- `PM-1` 到 `PM-4` 是结构性定义、CRT 骨架和局部刚性，适合作为正文基础引理。
- 大因子不可复用、相邻互质、45 度锁、`P±1` 斜线锁定应统一归入“局部刚性层”，避免在主线中反复新增命名。

### 1.2 仍需保守标注部分

- `PM-5` Tail anchors 与 `PM-7` Structured-EHPD 是方阵链条的审稿核心。
- 在它们完全逐行核查前，`PM-8` 只能标注为 `Reduction package` 或 `Conditional on PM-5/PM-7`。
- 方阵行列结论可以辅助二点筛中的 `BMD-Zero`，但不能替代 `BMD-Char` 的有符号谱分布估计。

### 1.3 优化重点

最优整理不是增加新的局部刚性名称，而是把所有局部刚性统一服务于 `Structured-EHPD`：

```text
local rigidity ledger + capacity ledger + no-reuse ledger
=> Structured-EHPD impossible
```

这会把方阵部分的审稿焦点压缩到一个最终接口。

## 2. 二点筛链条

当前二点筛主线应写为：

```text
TP-1 two-point rough pair
=> TP-2 TLI
=> TP-3 BST
=> TP-4 BST-2
=> TP-5 BMD
=> TP-6 WBE2
=> TP-7 BE2-3
=> TP-8 BE2-3K
=> TP-9 KLS-window
```

外部定理版闭合链为：

```text
DI + BFI
=> KLS-window
=> BE2-3K
=> BE2-3
=> WBE2
=> BMD
=> BST-2
=> BST
=> TLI
```

### 2.1 已完成的关键压缩

- `BMD` 已不是模糊猜想，而是受限二素数卷积 `a_n=#\{p m=n\}` 在固定类 `2 mod d` 上的加权 AP 分布。
- `BMD` 不需要完整 `max_a BV-E2`，只需要 well-factorable 权重下的 `WBE2`。
- `BE2-3` 的普通大筛路线已被排除，真正硬核是 Kloosterman 平均。
- `BE2-3K` 已进一步压缩为 `KLS-window`。

### 2.2 当前准确状态

- 引用 DI 谱 Kloosterman 大筛与 BFI dispersion/well-factorable 权重时，二点筛 BMD 链条达到 `External-theorem closed`。
- 若要求完全自足无黑箱，则 `KLS-window` 仍未在文内重证，不能宣称完全无黑箱闭合。

### 2.3 适配核查义务

主稿必须逐项核对：

| 项目 | 需核查内容 | 风险 |
| --- | --- | --- |
| 相位匹配 | 第 8 节双逆元相位是否完全落入 DI/BFI Kloosterman 相位类 | 相位符号或归一化偏差 |
| 模数范围 | `C≈P/log^{O(1)}P` 是否在外部定理 level 内 | level 超界 |
| 频率范围 | `H<=P/log^{O(1)}P` 是否被谱大筛覆盖 | Fourier tail 过长 |
| 系数范数 | `beta_s` divisor-bounded 与二范数是否满足假设 | 系数过粗 |
| 权重结构 | `lambda_d` 是否保持 well-factorable level | 权重不能接入 BFI |
| 损失账本 | dyadic、gcd、sawtooth、平滑损失是否均可由 `B(A)` 吸收 | 对数节省不足 |

## 3. RH 链条

RH 方向必须保持更严格的状态语言：

```text
RH-1 explicit-formula entrance
=> RH-2 CRT field transfer
=> RH-3 controlled exits
=> RH-4 no-cycle ledger
=> RH-5 final RH promotion
```

当前只能标注为 `Verification package` 或 `Referee-block`，不能标注为无条件 RH 证明。原因是 controlled exits 与 no-cycle ledger 尚未形成外部定理级或逐行自足级证明。

## 4. 合著稿统一闭合规则

全稿采用以下规则防止逻辑跳跃。

1. 存在性结论不能替代有符号平均分布估计。
2. 完整 CRT 周期均衡不能直接替代短窗口真实剩余分布。
3. 实验、扫描和数值证书只能作为证据等级，不作为证明。
4. 外部深定理版与完全自足版必须分开定理化。
5. 每个主结论必须有唯一依赖链，避免同一命题在不同章节中使用不同条件。

## 5. 下一步优化优先级

1. 把二点筛链条正式编号为 `TP-1` 至 `TP-9` 的定理/引理环境。
2. 把 `external-theorem-index.md` 中 DI/BFI 条件转写为主稿可引用的定理模板。
3. 为 `KLS-window` 建立变量适配核查表，并在主稿中标明“已核对/待核对”。
4. 将方阵行列章节压缩到 `Structured-EHPD` 单一最终接口。
5. 对 RH 章节继续使用 `Not claimed` 警示，直到 controlled exits 全部逐行闭合。
