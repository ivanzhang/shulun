# 《方阵与 CRT 数论矛盾场研究》合著目录与理论系统总览

## 0. 审稿边界

本合著稿当前定位为：

- **方法论与依赖图闭合稿**：统一整理方阵、CRT、二点筛与 RH 反例矛盾场的结构、入口、出口、依赖和审稿边界。
- **外部深定理版闭合局部结果**：二点筛 BMD 链条在接受 DI/ BFI 外部深定理后闭合。
- **非完全自足终局证明稿**：方阵行列终局、RH 终局、二点筛完全无黑箱版仍有各自独立审稿义务。

不得把当前稿表述为“RH、孪生素数或全部方阵行列命题的完全无条件自足证明”。

## 1. 合著目录建议

### 第 I 部：统一矛盾场方法

1. **导论：从反例到矛盾场**
   - 反例不是单点异常，而是结构化覆盖场；
   - 入口、分解、出口、容量、无环势能；
   - 证明闭合的四件套：入口定理、出口分类、出口排除、全局矛盾。

2. **CRT 骨架与非零同余类均衡**
   - 非零同余类基线；
   - CRT 周期骨架；
   - 局部相位均衡与全局短窗口失衡的区别。

3. **大因子短窗不可复用**
   - 同一大因子在短窗口内不可重复解释；
   - 行、列、斜线截面上的复用间隔；
   - 双粗锚与尾部锚分层。

4. **矛盾场账本语言**
   - source deletion；
   - baseline subtraction；
   - capacity upper/lower comparison；
   - no-cycle potential。

### 第 II 部：方阵行列素数存在性程序

5. **Prime Matrix 模型**
   - `n(r,c)=(r-1)P+c`；
   - 第 `P` 列平凡因子排除；
   - 行/列/圆柱斜线语言。

6. **A/B 入口归约**
   - 行反例到 Structured-EHPD；
   - 列反例到 Structured-EHPD；
   - 小因子锁定、45 度锁、Tail-log4 尾部锚。

7. **D 组结构排斥接口**
   - Structured-EHPD 定义；
   - 大锚容量；
   - 短窗互斥；
   - 当前状态：归约包完成，D 组仍需独立逐行审稿。

8. **有限验证与阈值账本**
   - 显式阈值；
   - 有限验证证书；
   - 参数余量与状态表。

### 第 III 部：二点筛与素数对方向

9. **二点粗候选命题**
   - `p∤x(x-w)`；
   - A/B 二点命题与 prime-pair 后果；
   - 为什么它不是原行列命题的简单推论。

10. **二次筛矛盾场**
    - 小素数双禁类；
    - TRC、I3-Core、SC2；
    - 自适应真实命中分层；
    - Zero-mass 与 smoothing discharge。

11. **从 TLI 到 BST**
    - Total Large Incidence；
    - `w=2` 的 Buchstab 半素数转移；
    - `K(alpha)` 常数；
    - 实验扫描证据与协方差审查。

12. **BMD：双素乘法分布**
    - `pm≡2 mod d` 乘法曲线；
    - 模 `2` 的确定剥离；
    - BMD-Zero 与 BMD-Char；
    - 行列输入只能排除零截面，不能替代有符号分布。

13. **BV-E2 / WBE2 / BE2-3K / KLS-window**
    - BMD 改写为受限 `E_2` 序列 AP 分布；
    - BV-E2 强版本与 WBE2 精确版本；
    - 普通大筛差一个 `P` 量级；
    - BE2-3 dispersion 方差；
    - BE2-3K 双 Kloosterman 核；
    - KLS-window 与 DI/ BFI 外部深定理版闭合。

### 第 IV 部：RH 反例矛盾场

14. **离线零点到素数异常**
    - 显式公式；
    - 平滑素数计数异常；
    - 反例场入口。

15. **RH controlled exits**
    - sparse/dense/tail/internal/global exits；
    - GEE/NRC/DSO 等出口；
    - controlled exits 的依赖边界。

16. **RH 审稿状态**
    - 当前为 verification package；
    - 不是最终无条件 RH 证明；
    - 需独立逐行 referee verification。

### 第 V 部：统一依赖图与优化方向

17. **统一依赖矩阵**
   - 方阵行列；
   - 二点筛；
   - RH；
   - 外部输入、计算证书、条件接口。

18. **顶刊审稿审查清单**
   - 不可过度声明；
   - 每个深输入的来源；
   - 每个条件命题的状态；
   - 每个实验结果的证据等级。

19. **未来优化与无黑箱化路线**
   - D 组排斥；
   - BE2-3K/KLS 内联；
   - RH controlled exits 独立化；
   - 统一术语和符号重构。

## 2. 理论系统图

### 2.1 总体模式

`反例 -> 结构化覆盖场 -> 局部刚性分层 -> 出口排除 -> 全局容量矛盾`

该模式在三个方向中的投影：

| 模块 | 方阵行列 | 二点筛 | RH |
| --- | --- | --- | --- |
| 反例入口 | 全合数行/列 | 无二点粗候选窗口 | 离线零点 |
| 骨架 | CRT 非零类 | 二禁类 CRT 骨架 | 平滑 CRT 候选基线 |
| 局部刚性 | 大因子短窗不可复用 | 双素/半素数转移 | sparse/dense/tail routing |
| 主要硬点 | Structured-EHPD 排斥 | KLS-window / 外部深定理 | controlled exits |
| 当前状态 | 归约包完成 | BMD 外部深定理版闭合 | verification package |

### 2.2 二点筛最新闭合链

外部深定理版：

`DI + BFI => KLS-window => BE2-3K => BE2-3 => WBE2 => BMD => BST-2 => BST => TLI`

其中：

- `DI`：Deshouillers--Iwaniec 谱 Kloosterman 大筛；
- `BFI`：Bombieri--Friedlander--Iwaniec dispersion 与 well-factorable 权重；
- `KLS-window`：窗口化 Kloosterman 谱大筛；
- `BE2-3K`：weighted bilinear Kloosterman dispersion；
- `WBE2`：固定类 `2 mod d` 的 weighted BV-E2；
- `BMD`：双素乘法曲线分布；
- `BST`：Buchstab 半素数转移稳定性；
- `TLI`：总大因子命中容量不等式。

完全自足版：

`KLS-window` 仍需文内重证 DI/ BFI 级谱理论，因此未闭合。

### 2.3 状态等级

| 等级 | 含义 |
| --- | --- |
| Proved-in-text | 文内逐行证明 |
| Reduction-closed | 归约链条闭合，但终点仍是命名输入 |
| External-theorem closed | 接受经典外部定理后闭合 |
| Computational-certificate | 有有限验证或实验脚本证书 |
| Referee-block | 作者侧完成组织，但需独立审稿确认 |
| Open / not self-contained | 完全自足版本尚未闭合 |

## 3. 当前最新结论

1. 方阵行列：A/B 归约清晰，但 Structured-EHPD 排斥仍是独立审稿核心。
2. 二点筛：BMD 链条在 DI/ BFI 外部深定理下已闭合到外部定理版；完全自足版剩 KLS-window。
3. RH：仍是 verification package，不得宣称最终 RH 证明。
4. 合著理论系统已经形成统一语言：CRT 骨架、局部刚性、容量账本、谱/外部输入。

## 4. 可优化方向

### 4.1 结构优化

- 把“条件命题”“外部定理版命题”“完全自足命题”分成三个不同环境，避免同一段内状态混杂。
- 给每条链统一编号，例如 `TP-1` 到 `TP-9` 表示二点筛链条，`PM-1` 到 `PM-8` 表示方阵链条。
- 将实验、启发式、正式证明分栏呈现。

### 4.2 数学优化

- 二点筛方向应优先正式化 `WBE2`，不再使用过强 `max_a BV-E2` 作为主陈述。
- KLS-window 应直接以 DI/ BFI 的标准定理格式重写，减少自定义相位和外部定理之间的翻译成本。
- 方阵行列方向应继续压缩 Structured-EHPD 到一个最小可审查不等式，而不是扩展更多命名接口。
- RH 方向应把 controlled exits 改写为“入口—出口—吸收”三列表。

### 4.3 文稿工程优化

- 合并重复的二点筛历史章节，保留“审稿路径版”主线，历史探索移入 archive。
- 在 TeX 主稿中加入“Claim Status Legend”。
- 所有外部定理引用加入 bib 文件或固定参考列表。
- 为每个实验 JSON/脚本写一行“用途、输入、输出、是否证明”说明。

### 4.4 审稿风险控制

- 明确禁止把二点筛外部深定理版闭合表述为孪生素数完全自足证明。
- 明确 DI/ BFI 的适用条件需在最终稿中逐项核对：平滑性、well-factorable level、模数范围、系数范数、端点截断。
- 对 RH 章节保留 submission warning。
- 对方阵行列章节保留 Structured-EHPD referee-block 标签。

## 5. 下一步建议

最优下一步不是继续增加新命题，而是做三件文稿工程：

1. **定理编号化**：把二点筛链条全部编号并写成 `Theorem/Proposition/Lemma`。
2. **外部定理引用表**：为 DI、BFI、BV、Vaughan、explicit formula 等建立统一表；当前已新增 `docs/monograph/external-theorem-index.md`。
3. **状态清洗**：把已经被新链条替代的旧“未闭合”描述移入历史注记，主线只保留最新状态。

## 6. 主链编号体系草案

### 6.1 Prime Matrix 链条

| 编号 | 名称 | 内容 | 状态 |
| --- | --- | --- | --- |
| PM-1 | Matrix Model | `n(r,c)=(r-1)P+c` 与第 `P` 列排除 | Proved-in-text |
| PM-2 | Small-Factor Locks | 小因子覆盖线与 CRT 非零骨架 | Proved-in-text / archived |
| PM-3 | Large-Factor Non-Reuse | 大因子短窗不可复用 | Proved-in-text |
| PM-4 | Diagonal Locks | `P±1` 斜线锁定归属 | Proved-in-text |
| PM-5 | Tail Anchors | Tail-log4 尾部锚削尾 | Referee-block |
| PM-6 | A/B Reduction | 行/列反例到 Structured-EHPD | Reduction-closed |
| PM-7 | Structured-EHPD Exclusion | D 组排斥 | Referee-block |
| PM-8 | Prime Matrix Closure | 行列命题终局 | Conditional on PM-5/PM-7 |

### 6.2 Two-Point Sieve 链条

| 编号 | 名称 | 内容 | 状态 |
| --- | --- | --- | --- |
| TP-1 | Two-Point Rough Pair | `p∤x(x-w)` 的二点候选 | Proved equivalence |
| TP-2 | TLI | 总大因子命中容量不等式 | Reduction target |
| TP-3 | BST | Buchstab 半素数转移稳定性 | Reduction target |
| TP-4 | BST-2 | `pm-2` 的 `Y`-rough 稳定性 | Reduction target |
| TP-5 | BMD | `pm≡2 mod d` 加权分布 | External-theorem closed |
| TP-6 | WBE2 | 固定类 `2 mod d` weighted BV-E2 | External-theorem closed |
| TP-7 | BE2-3 | 平衡 Type-II dispersion | External-theorem closed |
| TP-8 | BE2-3K | 双 Kloosterman 核 | External-theorem closed |
| TP-9 | KLS-window | 窗口化 Kloosterman 谱大筛 | External input DI/BFI |

### 6.3 RH 链条

| 编号 | 名称 | 内容 | 状态 |
| --- | --- | --- | --- |
| RH-1 | Off-Critical Entrance | 离线零点产生素数异常 | External explicit formula |
| RH-2 | CRT Field Transfer | 异常转入 CRT rough ledger | Verification package |
| RH-3 | Controlled Exits | sparse/dense/tail/internal/global exits | Referee-block |
| RH-4 | No-Cycle Ledger | 出口无环与容量闭合 | Referee-block |
| RH-5 | RH Final Promotion | RH 终局证明 | Not claimed |

## 7. 外部定理引用条件表

| 输入 | 来源 | 用途 | 必须核对的适用条件 |
| --- | --- | --- | --- |
| DI spectral Kloosterman large sieve | Deshouillers--Iwaniec 1982 | KLS-window 的谱平均抵消 | 模数范围、频率范围、平滑权、系数二范数、Kloosterman 相位符号 |
| BFI dispersion / well-factorable weights | Bombieri--Friedlander--Iwaniec 1987 | WBE2/BE2-3 的大模数分布 | well-factorable level、Dirichlet 多项式长度、卷积类型、端点平滑 |
| Bombieri--Vinogradov / E2 variant | 标准筛论输入 | 强版本 BV-E2 备选入口 | level `N^{1/2}/log^B N`、`E_2` 序列限制、奇模剥离 |
| Vaughan / Heath-Brown identity | 标准解析数论 | 素数权替换为 Type-I/II | 截断参数、系数范数、dyadic 分解损失 |
| Explicit formula | 标准 ζ 函数理论 | RH 反例入口 | 平滑核、零点贡献、误差项、阈值 |
| Bourgain--Garaev/Baker 类输入 | 方阵/RH 局部估计 | 旧章节外部输入 | 精确版本、常数、变量范围 |

## 8. 旧链条降级规则

为了避免主线混乱，采用以下降级规则。

1. **被新链条替代的硬点进入历史注记。** 例如 RB-TLI 原始形式被 BST/BMD/WBE2 链条替代后，不再作为当前主缺口。
2. **启发式和实验只保留证据等级。** 实验 JSON 只能支持“数值现象/常数猜测”，不得作为证明。
3. **强于必要的命题降为备选。** `max_a BV-E2` 强于 WBE2，主线使用 WBE2，BV-E2 作为充分但非最小输入。
4. **条件输入必须显式标注。** RC-Prime、Structured-EHPD、RH controlled exits 不得在无条件链条中隐式使用。
5. **外部深定理版与完全自足版分开陈述。** DI/BFI 接受时可说外部定理版闭合；不接受时必须说 KLS-window 未自证。

## 9. 当前理论体系的可优化点深评

### 9.1 二点筛链条

最有价值的优化是把主线从历史探索式叙述改写为：

`TP-1 -> TP-2 -> ... -> TP-9`

每一步只保留一个命题、一个证明或一个外部引用。这样可以明显降低审稿人寻找缺口的成本。

`WBE2` 应作为主命题，`BV-E2` 只作为强充分条件。原因是 `WBE2` 精确匹配 Rosser/Buchstab well-factorable 权重，也避免引入不必要的 `max_a`。

### 9.2 KLS-window 链条

当前最大风险不是数学方向，而是“外部定理适配”的细节。最终稿必须逐项核对：

- 第 438 节相位是否完全落入 DI/ BFI 的 Kloosterman 相位类；
- `h` 的截断长度是否在谱大筛允许范围；
- `beta_s` 的 divisor-bounded 条件是否足以替代光滑系数；
- well-factorable 分解后的 level 是否仍满足 BFI 条件；
- gcd 层的多对数损失是否能被 `B(A)` 吸收。

### 9.3 方阵行列链条

方阵部分的命名接口太多，最优整理是把所有中间探索统一归入三层：

1. 小因子与 diagonal locks；
2. 大因子不可复用与尾部锚；
3. Structured-EHPD 排斥。

审稿主线只应追踪这三层，不再引入新的局部命名，除非它直接缩小 Structured-EHPD。

### 9.4 RH 链条

RH 章节需要与二点筛章节采用同样的状态等级。每个 controlled exit 应标注：

- 入口假设；
- 输出结论；
- 使用的外部定理；
- 是否需要独立 referee verification。

目前 RH 章节最应避免的是把 verification package 写成 final proof。

## 10. 关键证明链条优化审查

本轮新增 `docs/monograph/key-proof-chain-optimization-audit.md`，用于把全稿主线压缩为三条可审稿链：

```text
PM-1 -> ... -> PM-8
TP-1 -> ... -> TP-9
RH-1 -> ... -> RH-5
```

该审查文件的主要结论是：

- 方阵行列链条应继续聚焦 `Structured-EHPD` 与 Tail anchors，不再扩散为大量局部命名；
- 二点筛链条在 `DI+BFI` 外部深定理允许时达到 `External-theorem closed`，完全自足版仍卡在 `KLS-window`；
- RH 链条保持 `Verification package / Not claimed`，不得写成无条件 RH 证明；
- 存在性刚性、完整 CRT 均衡、实验扫描均不能替代有符号谱分布估计。

## 11. 下一轮最优执行项

1. 在 TeX 主稿加入 `Claim Status Legend`。
2. 把 `external-theorem-index.md` 的 DI/BFI 条件转写为主稿外部定理模板。
3. 把二点筛链条重写成 `TP-1` 到 `TP-9` 的定理环境。
4. 给 `experiments/rb_tli_w2_scan.py` 和相关 JSON/MD 添加证据等级说明。
5. 对 KLS-window 完成逐项变量适配核查表并建立 `B(A)` 吸收账本。
