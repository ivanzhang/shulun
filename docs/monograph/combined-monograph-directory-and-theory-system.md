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
   - PTA/BSI/RSE 尾段粗锚短区间接口；
   - 当前状态：归约包完成，D 组仍需独立逐行审稿。

8. **有限验证与阈值账本**
   - 显式阈值；
   - 有限验证证书；
   - 参数余量与状态表。

8A. **BPN-BK 最终证书出口**
   - 可变阶 Bonferroni/Brun 只把边界零行导入缺陷出口；
   - 普通 Selberg/Brun 下界筛在 `H=P,z=P` 只有 `s<=1`，不能单独给正筛余；
   - 当前最终剩余为 `PDEC-Cert`、`SAE-Cert`、正式着色走廊 `Rankin certificates`；
   - `PDEC` 的硬核是证明同一坏窗指示函数满足 `U_CRT<L_PDEC`；
   - `PDEC-Cert` 进一步拆成显式坏窗计数证书与线性对偶主控证书；
   - 对偶约束账本拆成 mass、mirror、column、tail-anchor、core-overlap、Rankin routing；
   - 第一批真实约束行已由有限 CRT 枚举填入，`low-hole bucket` 已改写为高层 CRT 补洞容量；
   - 下一步最窄目标已校正为残基类 set-cover 的 Hall 亏损定理；
   - `Q=2310,P<61` 的全部 zero phases 已由低范围最终证书闭合，按整洞集亏损、桥洞临界、精确 DP 临界三类验收；
   - 一洞删除由桥洞机制认证：删去一个同时支撑两个高素数最大残基块的洞后，总容量下降 `2`；
   - `P=41` 的 `24` 个非桥洞临界相位由完整残基类 set-cover DP 有限证书闭合；
   - 列残基刚性把 `B_{\ell,a}` 化为 `c mod ell` 分块；临界桥洞在样本中均为 `13/19` 最大列残基块交点；
   - 扩展 `P=53,59,61` 显示转折后 zero bucket 消失或仅剩整洞集直接亏损；
   - 贪心构造证书显示 `P>=61,P<=109` 全相位可补完，转折后 zero bucket 可由构造性覆盖排除；
   - 固定升序碰撞梯审计显示 `P>=61,P<=149` 全相位可补完，动态选择自由不是必要条件；
   - 增益账本把转折后补洞压成 `LHB-7`：固定高素数 `13,17,19,23,...` 的重复增益不等式；
   - `LHB-7` 已进一步拆成列残基碰撞能量下界 `sum 2E_ell(H_j)/|H_j| >= |H_Q(t)|-|R|`；
   - 鸽巢尾段判据 `U_j=U_{j-1}-ceil(U_{j-1}/ell_j)` 在扫描到 `P<=100000` 时只失败十个素数，`P=107` 起闭合；
   - `P/5` 分割判据把尾段全局化分成 `107<=P<=229` 精确递推有限证书、`233<=P<=13207` 精确连续乘积有限证书、`P>=13208` 显式常数包；
   - 两段有限尾段证书已生成：`23` 行精确递推和 `1520` 行整数交叉乘法连续乘积均无失败；
   - `61<=P<=103` 十个窄带素数已由 `23100` 个低相位的碰撞能量证书闭合；
   - 最小符号化义务只剩 `P>=13208` 的 Mertens/prime-count 引用核验；
   - `SAE` 的硬核是逐孤立坏窗给出 survivor/lift/higher-defect 证书。

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
| 主要硬点 | Structured-EHPD 排斥；尾段 RSE-CRIT | KLS-window / 外部深定理 | controlled exits |
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

1. 方阵行列：A/B 归约清晰；Structured-EHPD 排斥与尾段 `RSE-CRIT` 是独立审稿核心。
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
- 方阵尾段应按 `RSE-OSC/RSE-AMP/RSE-CRIT` 三段定理化，优先攻临界带 `ell≈hP_m` 的合成权质量或 CRTDefect 排斥。
- 新增 `CWM/CRD` 二分后，模型权扫描显示绝对临界质量在尾部不稳；核剖面扫描进一步显示应保留真实 RSE 核；双出口扫描又显示普通 `SPC` 不足以推出缺陷；SKT 扫描把平滑部分拆为线性化与 Selberg 二次型变换；SQF 扫描显示主瓶颈在低频 `Q(it)`；最优权扫描把低频硬核压低；fixed-low 扫描显示裸 `Q` 在 `u>2` 会反弹；中频带权扫描把它压缩为固定紧区间常数界；紧区间网格证书进一步把单点硬核改写为 `2<u<=12` 的带权平均加导数余量。因此临界带最终应转为 `QLOW-MID-COMP(intervalized)/RRD/OSPC`：紧区间带权常数证书、粗数替换误差、有向小素支撑集中到 CRTDefect。
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
| Rosser--Schoenfeld explicit bounds | Rosser--Schoenfeld 1962, Cor. 1 `(3.5),(3.6)`, Thm. 7 `(3.26)` | BPN-LHB 尾段 `P>=13208` | Mertens 乘积常数 `1.03`、`pi` 上下界、`floor(P/5)` 取整 |
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

最新的广义斜率锁接口见 `docs/monograph/generalized-slope-locks-and-rough-hole-limits.md`。它把 `P±1` 的 45 度锁扩展为 `P±t`，并把圆柱绕回螺旋写成“等差主项 + 绕回次数余项”的显式公式。该接口的作用是闭合小素因子层，把反例压缩到粗数带大因子总命中不等式

```text
B_Y(I)<|G_Y(I)|.
```

因此它应并入第 1 层“小因子与 diagonal locks”，而不应作为新的终局命题单独膨胀。

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

## 11. 无条件化优化审查

最新的三主线无条件化审查见 `docs/monograph/unconditionality-optimization-audit.md`。其优化结论是：

- 方阵行列方向优先攻击 `PM-R1/PM-R2=>RHI`。这里有形式参数窗口 `e^{-1}<alpha<1/2`，是目前最有希望压缩 Structured-EHPD 的路线。
- 二点筛方向必须单独审查 `BMD=>BST-2=>BST=>TLI`，防止把 BMD 外部深定理版闭合误写成素数对终局证明。
- RH 方向应把 controlled exits 改写成“输入异常—输出吸收—使用定理—常数 convention”的四列表，并探索正性二次型化。

该审查不升级任何终局定理状态，只给出下一步最小攻坚接口。

## 12. 下一轮最优执行项

1. 在 TeX 主稿加入 `Claim Status Legend`。
2. 把 `external-theorem-index.md` 的 DI/BFI 条件转写为主稿外部定理模板。
3. 把二点筛链条重写成 `TP-1` 到 `TP-9` 的定理环境。
4. 给 `experiments/rb_tli_w2_scan.py` 和相关 JSON/MD 添加证据等级说明。
5. 对 KLS-window 完成逐项变量适配核查表并建立 `B(A)` 吸收账本。
6. 新增方阵行列 `PM-R1/PM-R2` 的 RHI 证明工作台。
7. 对二点筛 `BMD=>TLI` 做无隐藏下界审查。

## 13. PM-RHI 第一轮攻坚结果

`docs/monograph/pm-rhi-workbench.md` 已把方阵行列 RHI 路线拆成：

```text
PM-R1: 短窗口粗数下界
PM-R2A: 可筛段粗互补商上界
PM-R2B: 尾段锚定上界
```

审查结果是：`PM-R1` 是标准线性筛可攻部分；`PM-R2A` 需要同一筛权 convention 下的常数匹配；真正最小硬点是 `PM-R2B`，因为 `P/Y<p<=P` 时互补商窗口长度小于 `Y`，普通逐素数筛法失效，必须使用圆柱螺旋相位块、大因子短窗不可复用、Tail anchors 与 CRT 均衡刚性。

第一轮继续压缩见 `docs/monograph/pm-r2b-tail-anchor-workbench.md`。该文把 `PM-R2B` 写成尾锚平均素数命中引理 `PTA`：

```text
T(M) <= (1+eps) H/log(P) * sum_{m~M, P^-(m)>Y} 1/m + E_M.
```

当前最小实质缺口是获得这个 `1/log P` 素数密度节省。纯几何尾锚和大因子不可复用只能给 `O(1)` 命中，尚不足以闭合；必须使用外部解析平均定理，或证明异常命中会触发圆柱相位块/CRT 均衡/Tail-anchor 矛盾。

## 14. 最新刚性洞见的合成优化

`docs/monograph/latest-rigidity-closure-optimization.md` 进一步合成了两条新刚性：

- 扩展斜线层锁可作用到尾段 `p` 变量，把 `p<=P` 的合数小因子层通过 `q<=sqrt(P)` 的 GSL 相位块标记；
- 二点筛中 `q|w` 时 `{0,w}` 二禁降为一禁，产生奇异因子增益 `prod_{q|w}(q-1)/(q-2)`。

合成后的最小接口为：

```text
PM: PTA-GSL
Two-point: singular-factor ledger + BMD=>TLI no-hidden-lower-bound audit
RH: controlled exits four-column formalization
```

这里 `PTA-GSL` 仍需证明 GSL 删除小素层后的 `p` 候选平均密度具有 `1/log P` 上界。该点尚未无条件闭合。

`docs/monograph/pta-gsl-hard-attack.md` 已继续展开 `PTA-GSL`。Selberg 上界筛后，最小硬点变为 `BSI`：

```text
N_ell(M)=sum_{m~M,P^-(m)>Y}
  (floor((X+H)/(ell m))-floor(X/(ell m)))
```

需要在 Selberg 二次权平均中等于主项 `H/ell sum 1/m` 加可吸收误差。平凡地板函数余项太大；必须用圆柱相位块、`Y`-rough 互补商、短窗不可复用与 CRT 均衡把异常余项导入刚性出口。

继续硬攻后，`BSI` 又被 sawtooth/Vaaler 展开压缩为 `RSE`：

```text
S_{h,ell}(M)=sum_{m~M,P^-(m)>Y}
  e(hX/(ell m)) (1-e(hH/(ell m))).
```

关键相位总变化约为 `hP_m/ell`，其中 `P_m=X/M` 是尾段 `p` 尺度。若 Selberg level 为 `R`，则 `ell<=R^2`。因此出现新的核心张力：

```text
R small  -> 倒数相位可振荡；
R large  -> Selberg 主常数更好；
需兼容 R^2 <= P^{1-alpha} 与 1/log(P) 常数。
```

当前最细硬点是 `RSE`：在 Selberg 二次权平均中控制粗数权倒数指数和。

## 15. 三命题闭合优化矩阵

最新三命题统一优化见 `docs/monograph/three-proposition-closure-optimization.md`。该文件把三条主线压成同一五段模板：

```text
反例入口
=> 确定结构层
=> 粗剩余层
=> 总命中/总出口不等式
=> 反例排斥
```

当前最小接口为：

```text
PM: QLOW-MID-COMP(intervalized)+RRD+OSPC
TP: BMD-to-TLI no-hidden-lower-bound
RH: controlled exits four-column ledger
```

其中 PM 链经过 `PTA-GSL=>BSI=>RSE` 后，已进一步压缩到紧区间带权常数证书、粗数替换误差和有向小素集中三个窄接口。`QLOW-MID-COMP` 的浮点网格证书已有 `certified≈0.21--0.23<0.35` 的余量；新增 `docs/monograph/qlow-mid-comp-interval-budget.md` 进一步显示，预留 `0.065` 外向舍入误差后最紧样本仍有 `0.052304` 余量；新增 `docs/monograph/selberg-rational-weight-audit.md` 已把样本 Selberg 线性系统改为有理精确审计；新增 `docs/monograph/trig-log-interval-oracle-audit.md` 将 trig/log oracle 半径压到 `2.333e-67`；新增 `docs/monograph/qlow-mid-comp-hq-interval-audit.md` 进一步给出 H/Q 归一化乘积增量 `6.600e-67`；新增 `docs/monograph/qlow-mid-comp-supnorm-audit.md` 给出 `supBound=0.296630<0.35`，从而 QLOW-MID-COMP 紧区间不再依赖 `Phihat` 数值求积；新增 `docs/monograph/rse-rrd-ospc-margin-ledger.md` 将主链剩余写成 `C_RRD+C_OSPC+C_SelbergUniform+C_round<0.053369509758272926` 的同口径账本；新增 `docs/monograph/rse-rrd-same-weight-reduction.md` 进一步把 `RRD` 拆成 `low/perp/conversion` 三个子项；新增 `docs/monograph/rse-rrd-low-projection-dichotomy.md` 修正 `OSPC` 能量尺度并形式化 `Pi_{<=Z}` 低模投影；新增 `docs/monograph/rse-low-block-exit-criterion.md` 将 low-block 出口压成加权 CRT 缺陷界 `0.005366563145999495`。另新增 `docs/monograph/prime-matrix-recursive-lift-audit.md` 审查相邻素数递推路线，结论是该路线可剥离旧核心，但必须补充 `Seam(p,q)` 缝合窗口命题；新增 `docs/monograph/prime-matrix-seam-endpoint-audit.md` 又把 `Seam` 压缩为端点屏障 `SEB: max_t(sigma_t+pi_{t+1})<q`，`p<=10000` 样本中 seam 空窗和 `SEB` 证书失败均为 `0`；新增 `docs/monograph/prime-matrix-seb-unconditionality-audit.md` 指出 `SEB` 过强，应把无条件化目标改为只检查 `q` 行漂移残基的 `ASB`；新增 `docs/monograph/prime-matrix-asb-pressure-audit.md` 与 `docs/monograph/prime-matrix-asb-hard-attack.md` 又把 `ASB` 压缩为相对高素点覆盖不等式 `ASB-RHC`，关键参数窗口为 `e^{-1}<alpha<1/2`；新增 `docs/monograph/prime-matrix-asb-rhc-alpha-sweep.md` 进一步显示 `ASB-RHC` 等价于粗剩余素数比例下界 `RPD`；新增 `docs/monograph/prime-matrix-rpd-failure-structure.md` 将 `RPD` 压力定位到粗半素数投影；新增 `docs/monograph/prime-matrix-semiprime-anchor-projection.md` 又将半素数投影压缩到锚层效率接口；新增 `docs/monograph/prime-matrix-anchor-cofactor-interval-audit.md` 将锚层效率精确改写为互补素数短区间平均，并暴露单窗半素数/粗合数比例可达 `1.000000`；新增 `docs/monograph/prime-matrix-mge3-budget-audit.md` 将至少三粗因子预算改写为低锚复合互补因子恒等式，`M_{\ge3}=206`、占粗合数 `0.141678`、恒等式校验差 `0`；新增 `docs/monograph/prime-matrix-mge3-second-anchor-audit.md` 将其继续压缩为第二锚粗尾恒等式，第二锚容量效率 `0.203557`，尾因子为素数比例 `0.980583`；新增 `docs/monograph/prime-matrix-mge3-tail-envelope-audit.md` 将第二锚粗尾转为 Mertens 包络二分，所需全局放大常数 `1.242381`；新增 `docs/monograph/prime-matrix-tail-spike-localization-audit.md` 将高尖峰定位到 singleton-prime 双曲走廊；新增 `docs/monograph/prime-matrix-singleton-corridor-bound-audit.md` 给出 singleton 走廊的唯一分解、低筛 z-rough、走廊宽度三层上界，混合所需常数 `1.299083`；新增 `docs/monograph/prime-matrix-singleton-corridor-overlap-audit.md` 证明同窗口走廊不重叠，最大重叠度 `1`。PM 链仍需逐项证明统一 Selberg 矩常数、加权 CRT 缺陷界或其 Tail-anchor 出口、`RRD-perp` 同权上界、`OSPC` 和递推路线中的素互补因子短区间上界、聚合 Mertens 包络、不相交 singleton 走廊并集 z-rough 上筛或异常出口、Annulus 后才能作为正式证明输入。

新增 `docs/monograph/prime-matrix-disjoint-corridor-selberg-lemma.md` 后，PM 递推支线中的 singleton 走廊上筛已内联为有限 Selberg 二次型与加权端点缺陷出口。主文稿仍不能据此宣称 PM 全链闭合，因为素互补因子短区间、聚合 Mertens 包络、异常出口排斥和 `Annulus` 仍是独立义务。

新增 `docs/monograph/prime-matrix-asb-rpd-weighted-sieve-kernel.md` 后，素互补因子短区间和聚合 Mertens 包络被统一成同权加权区间筛预算。主文稿的递推支线剩余义务相应缩为：数值化 `RPD-Budget`、排斥加权低模端点缺陷出口、证明 `Annulus(p,q)`。这仍是未闭合义务，不得写成 ASB/RPD 无条件定理。

进一步新增 `docs/monograph/prime-matrix-rpd-first-anchor-identity.md` 后，`RPD-Budget` 的左侧可改为第一锚粗互补因子单预算，避免“半素数 rough 上界 + M_{\ge3}` 尾预算”的双计数。主文稿剩余义务相应改为：数值化第一锚同权预算、排斥第一锚低模端点缺陷出口、证明 `Annulus(p,q)`。

新增 `docs/monograph/prime-matrix-rpd-fac-budget-audit.md` 后，第一锚同权预算已有首轮数值化：同批压力窗口中全局所需常数 `1.352236`，但逐窗口最大所需常数 `1.695703` 超过 `eta=0.10` 的逐窗口最小允许常数 `1.570917`。因此主文稿不得把 FAC 全局平均写成闭合证明；剩余义务应更精确写为：分层/端点修正 FAC-Selberg 逐窗口预算，或超预算窗口导出加权低模端点缺陷并由 `CRTDefect/Tail-anchor/OSPC` 排除，另加 `Annulus(p,q)`。

新增 `docs/monograph/prime-matrix-rpd-fac-lowmod-defect-audit.md` 后，加权低模端点缺陷被具体写成 `D_T`。样本中最尖峰窗口在 `T=17` 已捕获 `90.9089%` 的最终 FAC 缺陷；`T=101` 对全部压力窗口的最小捕获率为 `80.4688%`。这把主文稿递推支线的未闭合接口进一步缩为：证明大的 `D_T` 必导向有向 CRTDefect/Tail-anchor/OSPC，或给出分层 FAC-Selberg 吸收该缺陷的逐窗口常数。

新增 `docs/monograph/prime-matrix-square-annulus-lift-lemma.md` 与 `docs/monograph/prime-matrix-square-annulus-sieve-lift-audit.md` 后，`Annulus(p,q)` 的结构也更清楚：在相邻素数平方壳层 `(p^2,q^2]` 中，旧 `p`-筛幸存者除 `q^2` 外自动为素数；加入 `q` 后真正非冗余删除的旧筛幸存点只有 `q^2`。`pq` 已由旧筛中的 `p` 删除。主文稿可把 Annulus 义务改写为旧筛幸存者非空命题：每个相关壳层 `q` 行段必须含有旧筛幸存者且不只含 `q^2`。样本中完整壳层行最小幸存者数只有 `1`，所以该义务必须逐行证明，不能由平均余量替代。

新增 `docs/monograph/prime-matrix-annulus-rough-nonempty-hard-attack.md` 后，递推支线的两个剩余异常统一为 signed low-mod bridge：ASB/RPD 失败给出正低模端点尖峰，Annulus-Rough 失败给出负低模端点亏损。若能证明足够大的有符号低模端点异常必触发 `CRTDefect/Tail-anchor/OSPC`，则相邻素数递推链会形成清晰闭合候选。

新增 `docs/monograph/prime-matrix-signed-lowmod-bridge-hard-attack.md` 后，signed low-mod bridge 已进一步端点场化：`D_T(I)` 精确等于 Möbius 加权端点 sawtooth 和。完整 `q` 行中，因 `(q,d)=1`，端点相位随行号作单位旋转。当前已闭合的是从大缺陷到低模端点投影；未闭合的是 `SESE-low`，即从大端点投影到 `CRTDefect/Tail-anchor/OSPC` 的排斥不等式。

新增 `docs/monograph/prime-matrix-directed-endpoint-crtdefect-bridge.md` 后，`SESE-low` 的桥接半段已经闭合为：

```text
large endpoint sawtooth projection
=> Directed Endpoint CRTDefect / OSPC*.
```

新增 `docs/monograph/prime-matrix-dec-ospc-exclusion-hardpoint.md` 后，最终剩余被进一步精确为 `PDEC-or-SAE`。单个端点 CRT 缺陷不能仅靠完整周期零均值排除；必须证明递推坏窗要么形成持续端点缺陷，从而产生坏行集合的非零 Fourier/CRT 缺陷，要么在孤立单窗情形下由旧核心锚点或壳层旧筛幸存者排除。主文稿应把该项标注为未闭合硬输入，而不是把 DEC/OSPC* 当作已经排除的矛盾。

新增 `docs/monograph/prime-matrix-zero-row-crt-audit.md` 与 `docs/monograph/prime-matrix-zero-row-delay-recursive-lemma.md` 后，递推路线多了一个可检查支撑事实：旧 `p`-筛的 `p` 对齐零行在样本中没有侵入下一素数 `q^2` 覆盖范围，且 `p<=2000` 的 `q×q` 旧筛行审计没有失败。严格证明链只能使用 `QSurv(p,q)=>Row(q)`；`p` 对齐零行延迟只是证据，因为 `q` 行跨越 `p` 行边界。若 `QSurv` 失败，它仍进入 `negative endpoint defect=>DEC/OSPC*=>PDEC-or-SAE` 的最终接口。

新增 `docs/monograph/prime-matrix-qsurv-gap-structure-audit.md` 与 `docs/monograph/prime-matrix-qsurv-grid-gap-hardpoint.md` 后，`QSurv` 的最小硬点被命名为 `GJE-SAE`：排除覆盖完整 `q` 网格行的素数荒漠。该命题弱于普通 `max prime gap<q`，但更有网格结构；实验中普通间隙可超过 `q` 而不产生空 `q` 行。合著稿应把这一点作为递推路线的最新硬接口。

新增 `docs/monograph/prime-matrix-gje-sae-terminal-band-decomposition.md` 后，递推路线的最新硬接口进一步更新为 `Terminal-SAE/PDEC`。普通短区间素数输入若指数 `theta>1/2`，只能覆盖低行段；靠近 `q^2` 的终端行必须使用镜像 CRT 覆盖结构。终端镜像把 `n` 改为 `m=q^2-n`，每个旧素数 `ell<=p` 的坏类统一为非零类 `q^2 mod ell`。这是下一步应专攻的最小结构命题。

新增 `docs/monograph/prime-matrix-terminal-sae-split-audit.md` 与 `docs/monograph/prime-matrix-terminal-sae-split-inequality.md` 后，该最小结构命题又压缩为 `TSI-or-PDEC`：先筛到 `y=max(2,floor(p/e))` 得低筛骨架 `G_y(h)`，再统计尾素数命中重数 `T_y(h)`。若 `G_y(h)>T_y(h)`，终端覆盖不可能；若失败，则失败必须解释为持续端点 CRT 缺陷。样本 `p<=1000` 全部终端镜像块均有正余量。

新增 `docs/monograph/prime-matrix-terminal-sae-y-sweep.md`、`docs/monograph/prime-matrix-terminal-tail-cofactor-audit.md` 与 `docs/monograph/prime-matrix-terminal-tail-cofactor-identity.md` 后，`TSI` 的证明义务进一步分解：参数 `y/p` 有稳定安全区间；尾项 `T_y(h)` 精确等于极短互补 `y`-rough 区间计数，且充分大后互补因子必须为素数。下一步应分别证明低筛骨架短块下界和极短互补素数窗口总和上界，或将失败送入 `PDEC/Tail-anchor`。

新增 `docs/monograph/prime-matrix-terminal-sae-cancellation-identity.md` 后，递推路线的最小接口再更新为 `RCI/PDEC`。在 `n=q^2-m` 变量中，`G_y(h)-T_y(h)=sum_{P^-(n)>y}(1-omega_tail(n))`，所以一尾因子项完全抵消；终端反例必须让多尾碰撞超额压倒无尾储备。审计 `docs/monograph/prime-matrix-terminal-sae-cancellation-audit.md` 到 `p<=1500` 显示正余量保持，且排除了 `n=1,q^2` 端点误算。合著稿应把 `TSI` 的下一步证明目标改写为 `RCI` 或 `RCI` 失败导出的端点/尾锚持续缺陷。

新增 `docs/monograph/prime-matrix-column-assisted-rci-bridge.md` 后，若列命题作为条件已证输入，行命题剩余可进一步表述为 `CDB/PDEC`。列命题只排除整列零截面，不能直接推出固定行非空；真正可用的是同列素数见证的位移刚性：若坏行点被标签 `ell` 覆盖，则同列素数见证的行位移不得为 `0 mod ell`。因此 `RCI` 失败必须表现为双尾碰撞集中、端点 CRT 缺陷或列见证半径异常。审计 `docs/monograph/prime-matrix-column-row-bridge-audit.md` 到 `q<=1000` 显示非平凡列失败为 `0`，最大列见证半径为 `107`。这给出了列输入辅助行递推的最小桥接链，但 `CDB` 本身仍需证明。

新增 `docs/monograph/prime-matrix-rci-cdb-parallel-hard-attack.md` 后，后续攻坚应把 `RCI/PDEC` 与 `CDB/PDEC` 并行推进。联合审计 `docs/monograph/prime-matrix-rci-cdb-joint-audit.md` 到 `p<=1000` 显示紧行 `RCI` 正余量仍为 `1`，且紧行最大尾标签负载、位移余类负载均为 `2`。因此最小硬点更新为 `Distributed-RCI`：在尾标签和位移余类均低集中度时，证明多尾碰撞超额严格小于无尾储备；集中分支则分别进入 Tail-anchor defect 或 Endpoint/Column CRT defect。

新增 `docs/monograph/prime-matrix-distributed-rci-semiprime-reduction.md` 后，`Distributed-RCI` 又缩成素数与平衡双尾半素数的短块比较。无尾项在 `n<q^2` 中必为素数；在 `y^3>q^2` 后，多尾负项只能是 `ell_1 ell_2`，其中 `y<ell_i<=p`。审计 `docs/monograph/prime-matrix-distributed-rci-semiprime-audit.md` 到 `p<=2000` 显示最大半素数/无尾比值为 `2/3`。下一步应证明低集中度下的 `balanced semiprimes < primes`，集中度高时送入尾锚或列位移缺陷。

新增 `docs/monograph/prime-matrix-distributed-rci-local-pairing-route.md` 后，`balanced semiprimes < primes` 可再攻为局部 Hall 匹配。若每个平衡双尾半素数都能在半径 `R` 内匹配到不同素数，则不等式成立；若 Hall 失败，则失败区间给出局部半素数过密与素数过疏，正好进入 `PDEC/Tail-anchor`。审计 `docs/monograph/prime-matrix-distributed-rci-pairing-audit.md` 到 `p<=2000` 显示配对失败为 `0`，最大匹配半径为 `132`。下一步最小硬点是 `LPH/PDEC`。

三命题共同闭合原则保持不变：TP 的 BMD 外部闭合不能直接替代 `BMD=>TLI` 的 Buchstab 转移审查；RH controlled exits 仍是 verification package，不得写成 RH 终局证明。

## 16. 轮筛阴影与固定偏移层锁更新

最新方阵行命题硬攻中，`Distributed-RCI` 已从“素数数压过平衡双尾半素数数”
进一步压缩为轮筛允许的局部 Hall 问题。核心新增结构是：

```text
双粗半素数 b 若要用附近素数 b+d 补洞，
则 d 必须同时避开所有小素数 r<=z 的禁类 -b mod r。
```

更细地，固定短偏移 `d` 的粗相位容量有精确公式：

```text
rho_z(d)=prod_{r<=z, r∤d} (r-2)/(r-1).
```

这解释了 `P±1`、`P±2`、`P±3`、`30` 轮筛等现象：奇偏移由模 `2`
完全锁死；`±2` 类偏移仍被 `3,5,7,...` 逐层削减；`±6,±12,±30`
因为含更多小素因子而较宽，但仍受更高小素数继续限制。审计
`docs/monograph/prime-matrix-semiprime-wheel-near-offset-audit.md` 显示
固定偏移实测比例与理论 `rho_z(d)` 对齐。

合著稿中方阵行命题最新最小接口应写为：

```text
RCI/PDEC
=> Distributed-RCI
=> WSH-Hall/PDEC
```

含义是：若轮筛允许 Hall 图可匹配全部平衡双尾半素数，则 `RCI` 成立；
若匹配失败，失败必须外显为固定偏移相位超载、尾标签集中或端点素数亏损。
该接口尚未无条件闭合，但比裸短区间素数下界更窄、更接近用户提出的
“半素数补洞能力受小素因子层锁限制”的刚性矛盾场。

新增 `experiments/prime_matrix_wsh_hall_phase_certificate.py` 与
`docs/monograph/prime-matrix-wsh-hall-phase-certificate.md/json` 后，
`WSH-Hall/PDEC` 的有限相位证书已经材料化。脚本在 `17<=p<=2000`、
`y=floor(p/e)`、轮筛素数 `2,3,5,7,11,13` 下扫描 `215074` 条含平衡双尾半素数的行：

```text
matching failure rows = 0
candidate radius failure rows for 3 log^2(q) = 0
max minimal matching radius = 132
max radius/log^2(q) = 2.3771082468335174
min(prime_count-semi_count) = 1
```

证书行逐项列出半素数、匹配素数、偏移、尾标签、固定偏移负载与轮筛相位负载，
并核验实际匹配偏移满足 `d != -b mod r`。这一步闭合的是有限审计格式和
失败出口格式，不是全局 `WSH-Hall` 定理。全局剩余仍是：

```text
prove WSH-Hall uniformly
or every Hall defect => PDEC / Tail-anchor / Endpoint deficit.
```

新增 `experiments/prime_matrix_wsh_hall_defect_anatomy.py`、
`docs/monograph/prime-matrix-wsh-hall-defect-anatomy.md/json` 与
`docs/monograph/prime-matrix-wsh-hall-defect-trichotomy.md` 后，上述第二分支的审稿模板被
进一步定式化。脚本读取 `WSH-Hall` 相位证书中的 `44` 条最紧行，故意把半径压到最小
Hall 半径以下，得到 `124` 个强制缺陷；每个缺陷都有连续半素数块 `B_0` 与
`|N_R(B_0)|<|B_0|` 的端点亏损，最大超额为 `5`。审计同时记录尾标签负载、轮筛相位负载、
固定偏移负载和 `q^2-n` 镜像区间。

这一步把下一个单点硬核命名为：

```text
WSH-Expansion-or-Defect:
if Tail-anchor and fixed-offset/PDEC thresholds do not fire,
then |N_R(B_0)| >= |B_0| for R=C log^2(q);
otherwise the failing block is absorbed by Endpoint/PDEC.
```

注意：该命题尚未证明。当前完成的是一维 Hall 缺陷正规形、五个刚性投影和三出口证书字段。

新增 `experiments/prime_matrix_wsh_expansion_margin_audit.py`、
`docs/monograph/prime-matrix-wsh-expansion-margin-audit.md/json` 与
`docs/monograph/prime-matrix-wsh-expansion-margin-ledger.md` 后，`WSH-Expansion-or-Defect`
的扩张项已被有限证书直接审计。脚本对 `17<=p<=2000`、`R=ceil(3 log^2 q)` 的全部含
平衡双尾半素数行逐个连续块计算

```text
Hall surplus = |N_R(B)| - |B|.
```

结果为：

```text
rows with balanced semiprimes = 215074
contiguous semiprime blocks = 8440419
global minimum Hall surplus = 1
zero-surplus blocks = 0
tight blocks with surplus <=1 = 7
```

这说明有限范围内不只是有匹配，而是每个连续半素数块都有正余量。全局证明仍缺
统一扩张下界；最新最小命题应写为：

```text
WSH Positive Expansion or Named Defect:
|N_R(B)| >= |B|
or Tail-anchor / fixed-offset-PDEC / Endpoint mirror deficit fires.
```

新增 `docs/monograph/prime-matrix-wsh-short-critical-block-audit.md/json` 与
`docs/monograph/prime-matrix-wsh-short-critical-block-reduction.md` 后，正扩张硬点又被压缩一层。
用同一扩张余量脚本取 `tight_surplus=2`，在 `8440419` 个连续块中只有 `45` 个小余量块，
且全部满足 `|B|<=3`：

```text
surplus=1, |B|=1: 4
surplus=1, |B|=2: 3
surplus=2, |B|=1: 24
surplus=2, |B|=2: 10
surplus=2, |B|=3: 4
```

因此下一最小硬点可拆为：

```text
SCB-1: |B|>=4 automatically expands or hits a named defect.
SCB-2: |B|<=3 local short blocks are excluded or hit a named defect.
```

这仍是有限审计支持的归约，不是全局证明。优先建议专攻 `SCB-2`，因为它只涉及单点、
双点、三点半素数簇，最适合把尾因子、固定偏移、小轮同余和端点镜像逐项写成不等式。

新增 `experiments/prime_matrix_wsh_scb2_local_certificate.py`、
`docs/monograph/prime-matrix-wsh-scb2-local-certificate.md/json` 与
`docs/monograph/prime-matrix-wsh-scb2-local-exclusion-template.md` 后，`SCB-2` 分支已有
路由闭合版定理。有限证书枚举所有 `|B|<=3` 短块：

```text
|B|=1 blocks = 1496400, min surplus = 1
|B|=2 blocks = 1281326, min surplus = 1
|B|=3 blocks = 1088870, min surplus = 2
negative blocks = 0
zero blocks = 0
tight blocks = 45
```

形式上，若短块 `B` 真的有 `|N_R(B)|<|B|`，这正是 `Endpoint/PDEC deficit`；若双点或三点
紧块还出现共享尾因子或共同固定偏移通道，则分别进入 `Tail-repeat` 或
`Fixed-offset-full-load`。因此当前可诚实写为：

```text
SCB-2 closed as routing modulo Endpoint/PDEC exclusion.
```

剩余硬点转为 `SCB-1` 长块正扩张，以及短块端点亏损出口的全局排斥。

新增 `experiments/prime_matrix_wsh_scb1_long_block_certificate.py`、
`docs/monograph/prime-matrix-wsh-scb1-long-block-certificate.md/json` 与
`docs/monograph/prime-matrix-wsh-scb1-long-block-expansion-template.md` 后，`SCB-1`
长块分支也已有有限证书和审稿模板。脚本枚举所有 `|B|>=4` 的连续平衡双尾半素数长块：

```text
long blocks = 4573823
global minimum long-block surplus = 3
negative long blocks = 0
zero long blocks = 0
tight long blocks = 4
```

最紧长块只出现在 `|B|=4,5`，且全部触发 `Endpoint-margin` 与
`Fixed-offset-full-load`。因此当前可诚实写为：

```text
SCB-1 has a finite long-block certificate with min surplus 3.
```

这一步没有证明全局长块扩张定理。它把下一最小硬点精确为：

```text
long-block positive expansion
or fixed-offset/PDEC absorption for long tight blocks.
```

合并后，`WSH-Hall/PDEC` 的当前主链为：

```text
SCB-2 routing closed modulo Endpoint/PDEC exclusion;
SCB-1 finite certificate supports long-block expansion;
remaining hard point = fixed-offset/PDEC absorption + Endpoint/PDEC exclusion.
```

新增 `experiments/prime_matrix_wsh_fixed_offset_pdec_ledger.py`、
`docs/monograph/prime-matrix-wsh-fixed-offset-pdec-ledger.md/json` 与
`docs/monograph/prime-matrix-wsh-fixed-offset-pdec-absorption.md` 后，
`Fixed-offset-full-load` 已被定理化为“无第三逃逸”的吸收接口。关键引理是：

```text
若 1<n<q^2 且 n 合成，则 n 有 <=p 的素因子；
若固定偏移 d 已避开 2,3,5,7,11,13，则缺失候选 b+d 必由 ell in (13,p] 解释。
```

有限吸收账本在 `SCB-1` 的 `4` 个最紧长块、`11` 条满载固定偏移行上核验：

```text
total candidates = 47
prime candidates = 15
missing candidates = 32
missing without factor <=p = 0
max factor load in one offset row = 1
```

这一步把固定偏移满载从未命名局部异常升级为正式路由：

```text
Fixed-offset-full-load
=> expansion or Tail-anchor or PDEC/low-mod CRTDefect or SAE/Endpoint.
```

它仍不排除 `PDEC/SAE/Endpoint`。因此全局闭合的下一真实缺口是
`FO-PDEC`：证明分散解释因子必产生 persistent low-mod 缺陷，或作为稀疏端点逃逸被
`SAE/Endpoint` 排除。

新增 `experiments/prime_matrix_wsh_fo_pdec_lowmod_audit.py`、
`docs/monograph/prime-matrix-wsh-fo-pdec-lowmod-audit.md/json` 与
`docs/monograph/prime-matrix-wsh-fo-pdec-hard-attack.md` 后，`FO-PDEC` 的方程层已经闭合。
每个缺失候选 `n=b+d=(r-1)q+c` 与解释因子 `ell` 给出：

```text
r == 1 - c*q^{-1} mod ell
uv + d == 0 mod ell
```

有限账本结果：

```text
lowmod equations = 43
CRT equation failures = 0
bilinear equation failures = 0
distinct explaining factors = 21
max same (q,row,factor) load = 2
```

这把 `FO-PDEC` 的剩余压成一个单一能量不等式：

```text
low-mod defect energy >= PDEC threshold
or non-persistent part is SAE/Endpoint.
```

该不等式尚未证明；因此不能宣称 `WSH-Hall/PDEC` 或方阵行列命题已全局无条件闭合。

新增 `experiments/prime_matrix_wsh_fo_pdec_energy_ledger.py`、
`docs/monograph/prime-matrix-wsh-fo-pdec-energy-ledger.md/json` 与
`docs/monograph/prime-matrix-wsh-fo-pdec-energy-lemma.md` 后，`FO-PDEC` 的能量产生部分已有
无条件组合下界。对任意解释方程多重集 `E` 和 `0<theta<1`：

```text
either exists ell with t_ell > theta*ell,
or low-mod defect energy E(E) >= (1-theta)|E|.
```

第一项是 `Tail/PDEC` 高负载出口；第二项给出低模正超额能量。默认 `theta=0.25` 的账本结果：

```text
global equation count = 43
global energy per equation = 0.9547817296210457
global high-load factor count = 0
```

因此当前主链最窄硬点已经更新为：

```text
FO-PDEC-to-PDEC threshold comparison:
prove U_CRT(E) < E(E)
or L_PDEC(E) <= (1-theta)|E|
for the same bad-window equation set.
```

这是定量阈值比较缺口，不是结构命名缺口。

新增 `experiments/prime_matrix_wsh_fo_pdec_threshold_ledger.py`、
`docs/monograph/prime-matrix-wsh-fo-pdec-threshold-ledger.md/json` 与
`docs/monograph/prime-matrix-wsh-fo-pdec-threshold-comparison.md` 后，阈值下界侧进一步显式化。
逐个解释因子投影计算非零 Fourier 最大值，当前最佳投影为：

```text
ell = 199
frequency h = 95
M_ell(E) = 3.959247567099438
```

因此下一步全局闭合目标已经具体到：

```text
prove U_CRT,199 < 3.959247567099438
for the same projected bad-window vector g_199.
```

这个 `U_CRT` 上界必须由合法 `PDEC-Dual-Cert` 约束或 `SAE/Endpoint` 排斥给出，不能用完整
CRT 周期均衡替代坏窗子集上界。

新增 `experiments/prime_matrix_wsh_fo_pdec_dual_cluster_audit.py`、
`docs/monograph/prime-matrix-wsh-fo-pdec-dual-cluster-audit.md/json` 与
`docs/monograph/prime-matrix-wsh-fo-pdec-dual-cluster-route.md` 后，`U_CRT,199`
的剩余障碍已被定位为对偶短弧聚簇：

```text
mass = 4
M_199 = 3.959247567099438
mass defect = 0.04075243290056196
dual arc length = 11
dual residues = 19(2), 30(1), 24(1)
```

纯质量上界只差约 `1.02%`，所以必须证明 `ell=199,h=95` 的长度 `11` 对偶短弧聚簇不能在
正式反例链中持久存在，或把非持久实例送入 `SAE/Endpoint`。

新增 `experiments/prime_matrix_wsh_fo_pdec_primitive_cluster_audit.py`、
`docs/monograph/prime-matrix-wsh-fo-pdec-primitive-cluster-audit.md/json` 与
`docs/monograph/prime-matrix-wsh-fo-pdec-multiplicity-legitimacy.md` 后，最后阈值的集合口径被
进一步审查。`ell=199,h=95` 投影在不同去重口径下为：

```text
equation/block-local: mass=4, Fourier=3.959247567099438
layer-local:          mass=3, Fourier=2.9698366905785227
physical:             mass=2, Fourier=1.9699193446802263
```

因此要使用强阈值 `3.959...`，必须证明正式 `PDEC` 坏窗集合允许 equation/block-local
多重计数，并且 `U_CRT` 上界也按同一多重集合计算。否则必须使用 primitive 口径或把重复项
送入 `SAE/Endpoint`。这是全局闭合前不可跳过的集合一致性义务。

新增 `experiments/prime_matrix_wsh_fo_pdec_formal_unit_audit.py`、
`docs/monograph/prime-matrix-wsh-fo-pdec-formal-unit-audit.md/json` 与
`docs/monograph/prime-matrix-wsh-fo-pdec-formal-unit-route.md` 后，集合一致性又被推进到
formal unit 层。审计显示：

```text
global_library_raw: mass=4, Fourier=3.959247567099438
global_layer_dedup: mass=3, Fourier=2.9698366905785227
global_physical:    mass=2, Fourier=1.9997507790353146
single formal unit after coordinate dedup: best Fourier=1.0
```

因此强阈值来自有限证书库聚合，不能直接代表单个正式反例分支。当前最小硬点更新为
`FormalUnit-Stitching / NestedBlock-Independence / SAE-Endpoint absorption`：必须证明跨 `q`
层事件属于同一个持久坏窗族，且嵌套块重复是独立约束；否则强阈值只能作为诊断信号，不能作为
全局无条件闭合的 `PDEC` 下界。

新增 `experiments/prime_matrix_wsh_fo_pdec_stitching_feasibility_audit.py`、
`docs/monograph/prime-matrix-wsh-fo-pdec-stitching-feasibility-audit.md/json` 与
`docs/monograph/prime-matrix-wsh-fo-pdec-branch-separation-theorem.md` 后，该硬点又被拆成两个
可审稿定理：`BS-1` 证明不同 `q` 层不能无拼接定理地合并；`BS-2` 证明同坐标嵌套重复必须
坐标商掉，除非有加权 Hall 对偶独立性。当前数据中 exact nested duplicates 为 `7`、
cross-level reuses 为 `9`；单个正式单元最佳 Fourier 仍为 `1.0`。下一步最小硬点因此是
`Weighted Hall Dual Independence` 或 exact duplicate 的 `SAE/Endpoint` 吸收。

## 17. CRT 行反射的可用与不可用部分

针对“第 `k` 行全覆盖是否迫使倒数第 `k` 行全覆盖并产生短周期”的新想法，
最新结论是：

```text
反射配对成立；
短平移周期和整除条件不成立。
```

令 `M=prod_{ell<=p}ell`，`N=M/p`。宽 `p` 行的非平凡列点
`n=(r-1)p+c, 1<=c<p` 在取负映射下变为

```text
M-n=(N-r)p+(p-c),
```

所以若行 `r` 全覆盖，则镜像行 `N-r+1` 全覆盖。这是证明级刚性。

但反射不是平移。行 `r` 与 `N-r+1` 同时全覆盖，不推出全覆盖行以
`r`、`2r` 或 `2r-1` 为现象周期，也不要求这些数整除 `N`。审计
`docs/monograph/prime-matrix-row-reflection-period-audit.md` 中
`p=23,r=59,N=9699690` 给出反例：`N mod 117=39`，且 `r+117=176`
不是零行。

更精确地，第二周期复现生成的是二面体轨道：

```text
r, N-r+1, N+r, 2N-r+1, ...
```

相邻间隔交替为 `N-2r+1` 与 `2r-1`，不是等差周期。行平移 `d`
保持所有旧素数覆盖相位的必要条件是 `ell|d` 对每个 `ell<p` 成立，
因此只能得到 CRT 行周期 `N`。斜线方向不变不等于截距相位不变。

若只研究“相位组合改变但全覆盖现象复现”，仍需额外证明零行集合对某个短平移
`d` 不变；反射本身不给出这个不变性。可用的条件稳定子引理是：

```text
若零行集合对平移 d 不变，且 r 是首个零行，则 gcd(N,d)>=r。
```

这给 `d=r,2r,2r-1` 带来强限制。已知样本中这些候选平移均不满足复现，
且 `gcd(N,d)<r`，所以不能作为当前闭合出口。

对 `P=23` 的完整周期扫描进一步说明了真实结构。第 `59` 行确是首个零行，
镜像行为 `9699632`；镜像前确有大量复现，共 `3454` 次，首次复现在第 `2612`
行。但第 `118=2*59` 行不是零行。零行总数为 `3456`，密度约 `0.0003563`，
间隔最小 `20`、最大 `21789`。这说明复现现象真实存在，但它是 CRT 相位空间中
多个覆盖证书点的稀疏集合，不是由 `k` 或 `2k` 生成的周期轨道。

最新分层审计还显示：第 `59` 行的 `2,3,5,7` 低素数骨架
`r≡59 (mod 210)` 在镜像前有 `324` 个零行复现，首个为 `6569`；
第 `59` 与第 `6569` 行在该骨架下都只剩列 `5,9,15`，但高素数补洞标签
从 `13,17,19` 变为 `19,13,17`。若固定到
`2,3,5,7,11,13,17`，镜像前只剩第 `59` 行。这说明零行复现应被建模为
“低骨架 + 高标签置换”的层级证书，而不是短等差周期。

因此，复现现象的可用方式是：若反例机制要求复现集合沿某短平移稳定，则使用
`gcd(N,d)>=r` 排斥；若不要求稳定，则只能把零行复现当成稀疏相位证书，继续由
`PDEC/SAE`、缝合零窗和端点缺陷账本处理。

合著稿中应保留的有效工具是“两端帽排斥”：若 `r0` 是首个 `p` 对齐零行，
则前 `r0-1` 行与末端 `r0-1` 行都没有零行。这能强化递推路线中的
端点异常账本；若 `q` 网格坏行产生的零窗无法同时兼容首端与尾端反射帽，
则进入 `PDEC-or-SAE`。但该工具仍不能直接替代 `QSurv`，因为 `q` 行边界
通常与 `p` 行边界漂移。

进一步的 `2P` 短复现审计见 `docs/monograph/prime-matrix-short-recurrence-gap-audit.md`。
它修正了一个自然但过强的猜想：全局上“任意两个零行循环距离都大于 `2P`”为假，
`P=19` 已有最小间隔 `5`，`P=23` 有最小间隔 `20`。这些短复现簇发生在周期内部，
由低素数骨架局部同步和高素数补洞标签置换产生。

真正可用的是边界版本。若首零行为 `r0`，反射给出末零行 `N-r0+1`，故首尾跨周期
距离恒为 `2r0-1`。所以

```text
首尾跨周期间隔 > 2P-1  ⇔  r0>P。
```

这只是目标的等价重写，不是独立闭合。下一步应把该等价式转化为首端帽/尾端帽的
边界相位非覆盖引理：在 `r<=P` 的边界帽中，低素数骨架必须留下洞，且高素数补洞
所需的 CRT 最小代表必须超过 `P`。

边界相位非覆盖的当前硬攻稿见
`docs/monograph/prime-matrix-boundary-phase-noncoverage-hard-attack.md`。其中已将目标压缩为

```text
BPN(P)
⇔ 每个 [xP+1,xP+P-1], 1<=x<P, 含素数
⇔ 每个完整覆盖证书的 CRT 最小代表 x_S>=P。
```

同时加入 Sylvester 大因子弱输入：每个边界行必有某数含 `>P` 大素因子；
但该数仍可能是“小因子 × 大因子”，所以剩余核心不是大因子存在，而是排除所有大因子点
都被小因子覆盖。当前单一接口命名为 `BPN-RM`：边界帽中补掉最后残洞必释放旧覆盖列。
该接口闭合前，边界相位非覆盖仍是严格归约，不是无条件定理。

`docs/monograph/prime-matrix-boundary-residual-migration-audit.md` 对 `BPN-RM` 作了必要校正：
局部补洞经常存在，正确现象是残洞迁移，而不是补洞能力不足。全局“补洞必产生新洞”
与 `BPN(P)` 几乎同强；若要变成证明，必须引入独立势函数

```text
Phi(R)>0
```

并证明所有补洞迁移保持 `Phi(R)>=1`。这成为边界帽路线的下一个真正硬点。

`docs/monograph/prime-matrix-crt-zero-solution-distribution-audit.md` 进一步把零行锁定为 CRT
覆盖方程组

```text
Z_P = cap_c union_{ell<P} {r : r = 1-cP^{-1} mod ell}.
```

该审计验证了零行镜像和边界帽样本非空性，但也排除了一个危险跳步：周期中区的粗合数/素数
密度画像不是 CRT 筛层的单调势能。论著中应将其作为“证书相位组合的经验画像”，不能作为
边界零行不存在的独立证明。正式证明仍需 `BPN-MCR` 或非循环 `Phi` 势函数。

`docs/monograph/prime-matrix-zero-row-spacing-gradient-audit.md` 又校正了一个更具体的间隔猜想：
首尾跨周期间隔确实由镜像严格给出

```text
Delta_edge = 2*r0 - 1,
```

其中 `r0` 是首个零行。样本中 `Delta_edge>2P` 成立；但这与 `r0>P`、即 `BPN(P)`
等价，仍不是独立证明。全局“中心零行复现更短、边界更宽”的十等分梯度不成立，不能进入
正式证明。可保留的新攻坚形式是 `BPN-Defect`：假设边界帽有零行，则它和镜像尾端零行形成
距离 `<=2P-1` 的双端覆盖证书；必须证明这种双端证书触发低模 CRT 缺陷、Tail-anchor
缺陷或残洞势函数矛盾。

`docs/monograph/prime-matrix-bpn-defect-bonferroni-audit.md` 将这个缺陷形式进一步压缩为
`BPN-B5`。在边界帽 `r<=P` 中，格点数 `<P^2`，故包含排斥中 `d>=P^2` 的交集项全部为
`0`。定义五阶 Bonferroni 下界

```text
S5(r)=(P-1)-I1(r)+I2(r)-I3(r)+I4(r)-I5(r).
```

若证明 `S5(r)>0` 对所有 `2<=r<=P` 成立，则 `BPN(P)` 直接闭合。有限审计到 `P<=199`
显示 `S3` 会失败而 `S5` 未失败，最坏样本仍有 `S5=12`。因此当前论著中边界帽最优攻坚点
应写为五阶交集和不等式，而不是更抽象的残洞势函数；但它仍需逐项证明，不能标为已闭合。

进一步的逐点恒等式说明：

```text
S5(row)=prime_like_count(row)-high_omega_penalty(row),
```

其中 `high_omega_penalty` 只来自含至少六个 `<P` 小素因子的整数，权重为
`binom(omega_P(n)-1,5)`。选点扫描到 `P=5003` 仍为正。故论著下一步应优先证明：
长度 `P` 的边界短窗内，高重小素因子合数的加权数量不能超过素数数量；若超过，则该短窗存在
小核心乘积过密，应导向 `Tail-anchor/CRTDefect`。

高重惩罚核心审计 `docs/monograph/prime-matrix-bpn-high-omega-core-audit.md` 进一步把该出口写成：

```text
Core6-Density-or-TailAnchor.
```

每个负贡献数有六小素核心 `core6<P^2`。若小/中 `core6` 桶过密，则固定核心倍数在短窗内异常集中；
若大 `core6≈n` 桶过密，则该数几乎被六小素核心锚定，形成尾锚/端点集中。这是目前从
`BPN-B5` 通向可吸收缺陷出口的最具体桥。

不过固定阶风险审计 `docs/monograph/prime-matrix-bpn-bonferroni-order-risk-audit.md`
显示：固定五阶不能作为全局终局。原因是小素因子个数的自然尺度
`lambda≈log log(P^2)` 无界增长，而任意固定奇阶截断的指数多项式模型最终会变号。
因此论著主线应写成：

```text
BPN-BK/Selberg:
K 随 log log P 增长，或使用 Selberg/Brun 非负筛权；
失败出口为 CoreK-Density-or-TailAnchor。
```

固定 `BPN-B5/Core6` 保留为低范围证据、结构探针和失败出口原型，不再写成全局证明终点。

新增 `docs/monograph/prime-matrix-bpn-bk-weight-model-audit.md` 与
`docs/monograph/prime-matrix-bpn-bk-selberg-route.md` 后，上述升级被进一步校正：
可变阶 BK 的严格恒等式为

```text
S_K(I)=prime_count(I)-sum_{omega>=K+1} binom(omega-1,K)。
```

因此它只是把固定 `Core6` 缺陷升级为 `CoreK` 高重尾部缺陷。普通
Selberg/Brun 下界筛在边界行 `H=P,z=P` 中只有 `s<=1`，不能单独证明非空；
若写成证明，必须补上

```text
BK-DEC(K,D,r) 或 CoreK-Density/TailAnchor
=> Directed CRTDefect / Tail-anchor / PDEC-or-SAE
```

的排斥链。当前行命题仍处于严格归约状态，不得标为无条件闭合。

新增 `docs/monograph/prime-matrix-bpn-bk-dec-bridge-proof.md` 后，上述排斥链的第一段
已闭合为定理：

```text
边界零行 + BK tail budget + positive BK main margin
=> BK-DEC
=> Directed Endpoint CRTDefect。
```

证明是有限代数：奇阶 Bonferroni 权在 `omega>=1` 上非正，低阶项精确分解为
`(P-1)V_{K,D}+E_{K,D}(r)`，再由分块鸽巢得到低模块投影异常。该定理把
合著稿中 BPN 主链的剩余义务更新为：

```text
BK tail budget / CoreK tail control
+ PDEC-or-SAE exclusion for the induced Directed Endpoint CRTDefect。
```

新增 `docs/monograph/prime-matrix-bpn-bk-tail-core-dichotomy.md`、
`docs/monograph/prime-matrix-bpn-tailcore-corridor-reduction.md` 与
`docs/monograph/prime-matrix-bpn-tailanchor-persistence-dichotomy.md` 后，`BK tail/CoreK`
侧进一步结构化：

```text
BK tail failure
=> TailCoreBucket/CoreK-Density
=> Tail-anchor concentration or Distributed corridor saturation
=> SAE/Directed CRTDefect or Distributed corridor saturation。
```

其中尾锚集中已并回 `PDEC-or-SAE`；剩余未并回的尾项出口是
`Distributed corridor saturation`，即许多互补锚走廊同时接近裸容量。该出口应接
不相交走廊 Selberg 包络或低模 CRTDefect。

新增 `docs/monograph/prime-matrix-bpn-distributed-corridor-saturation-reduction.md` 后，
`Distributed corridor saturation` 也被拆成可审查二分：

```text
sum_d sigma(d)m(d) saturated
=> high overlap fixed-core defect
   or colorable disjoint-corridor budget violation。
```

这里 `m(d)` 是核心 `d` 被多少互补锚走廊复用。高重叠分支并入
`PDEC-or-SAE`；低重叠分支由区间图着色拆成不相交走廊并集，再接
finite core-sieve/Selberg/Rankin 预算或 low-mod CRTDefect。

新增 `docs/monograph/prime-matrix-bpn-colored-corridor-core-sieve-budget.md` 后，
低重叠分支的预算口径被修正为 smooth-core Rankin，而不是 rough Selberg：

```text
N_K(C) <= (2D0)^s sum_{d in C} sigma_K(d)/d^s。
```

因此该出口的剩余义务是有限 Rankin 账本常数闭合；若按低模模型分配预算失败，
则进入 `low-mod core CRTDefect`。

脚本 `experiments/prime_matrix_bpn_rankin_ledger_certificate_audit.py` 已提供该账本的
证书实现。它使用逐走廊右端 `B_j` 的安全 Rankin 因子 `(B_j/d)^s`，并同时输出
低模相位尖峰。默认合成样本显示相位尖峰可很强，因此正式走廊证书若超预算，应优先
抽取 `low-mod core CRTDefect`，而不是继续放宽全局常数。

新增 `docs/monograph/prime-matrix-bpn-lowmod-core-crtdefect-bridge.md` 后，该
`low-mod core CRTDefect` 已并入统一最终出口：residue 尖峰经有限 Fourier 反演变成
非零低模角色异常；持续异常进入 `PDEC`，孤立异常进入 `SAE-core`。因此 BPN-BK
独立剩余只剩 `PDEC-or-SAE` 排斥与 Rankin 账本常数闭合。

新增 `docs/monograph/prime-matrix-bpn-unified-pdec-sae-dichotomy.md` 后，`PDEC-or-SAE`
本身也被统一化：endpoint 与 core 缺陷都只是零均值低模测试函数触发的坏窗。坏窗集合
密度大时，Parseval/Cauchy 给出非零 Fourier/CRT 缺陷；坏窗集合稀疏时，剩余为
单窗逃逸 `SAE`。因此合著稿最终应把 BPN-BK 剩余写成：

```text
PDEC exclusion + SAE local escape exclusion + finite Rankin ledger constants。
```

新增 `docs/monograph/prime-matrix-bpn-rankin-ledger-acceptance-theorem.md` 后，最后一项
变为证书验收制：正式反例诱导的每个着色走廊必须给出 `rankin_budget_pass=true`
的证书；否则失败者必须转入 `low-mod core CRTDefect`，再由统一 PDEC/SAE 接口处理。

## 18. q 零行反推 p 阶段的正确递推形态

新的反推想法可以严写为：

```text
q 零行
=> 旧 p 筛长度 q 零窗
=> 完整 p 对齐零行 或 p 缝合零窗。
```

第一步使用平方壳层事实：在 `q^2` 内，避开全部 `<=p` 素数的数除 `q^2`
外自动为素数。若 `2<=s<q` 的 `q` 行为零行，则非 `q` 倍数不可能旧筛幸存；
右端点 `sq` 中的 `s` 也必含不超过 `p` 的素因子。所以整条 `q` 行已经是旧
`p`-筛零窗。

第二步是纯几何。令 `q=p+g`，

```text
a_s=(s-1)q mod p.
```

若 `a_s=0` 或 `a_s>=p-g`，则该 `q` 零行包含完整 `p` 对齐零行，可在旧核心内
直接矛盾于 `Row(p)`；若 `0<a_s<p-g`，则只得到相邻两个 `p` 行的后缀/前缀缝合零窗。几何审计
`docs/monograph/prime-matrix-reverse-zero-row-dichotomy-audit.md` 显示，
在 `p<=2000` 的核心区假想 `q` 行中，直接支约 `0.00616`，缝合支约 `0.99384`。

因此递推链不能只写 `Row(p)=>Row(q)`；最小正确形态是：

```text
Row(p)
+ SeamSafe/ASB-or-PDEC
+ Annulus-Rough-or-negative-lowmod-defect
=> Row(q).
```

这把用户提出的“向前反推矛盾”变成了实际可攻的硬点：专攻缝合零窗排斥，而不是仅查完整旧行。

新增 `docs/monograph/prime-matrix-crt-lift-parity-audit.md` 后，另一个更直接的 CRT 奇偶路线也被
校正。对相邻素数 `p<q`，在 q 非平凡列 `1..q-1` 中，新增素数 `q` 本身不参与覆盖；所以 q 零行
确实降为旧 `p`-筛长度 q 零窗。但旧 `p`-筛在 q 行宽下的基本周期 `M_p=\prod_{\ell\le p}\ell`
中的零行集合已经由镜像成偶数；把周期人为放大为 `qM_p` 只会把零行数乘以奇数 `q`，仍为偶数。
样本 `5<=p<=19` 全部满足旧周期镜像、旧周期零行数偶、提升周期零行数偶，且 q 方阵内没有旧筛
零行。因此“有一个零行复制 q 次，与偶数性矛盾”的链条不能使用。可保留的增益是更精确的下降入口：

```text
q 方阵边界零行
=> 旧 p-筛第一周期内极早长度 q 零窗
=> 完整 p 对齐零行 或 p 缝合零窗
=> 早期端点 CRT 缺陷 / PDEC / SAE。
```

新增 `docs/monograph/prime-matrix-recursive-mirror-descent-audit.md` 后，继续递归反推的边界也被
明确。固定上层宽度 `q` 时，较低筛层的完整 CRT 周期可以有镜像偶数零行；但这不等于较低
宽度 `p'` 的实际 `p'×p'` 方阵内有零行。原因是：全周期零行通常远离早期方阵窗口；剥去最大
根基素数会产生复活洞；并且行宽从 `q` 改成 `p'` 后 CRT 相位方程改变。样本 `5<=p<=19`
中，旧周期零行已出现于 `(p,q)=(11,13),(13,17),(17,19),(19,23)`，但对应 `q^2` 早期行零行
均为空，实际更小方阵早期零行也均为空。最大样本 `(19,23)` 中，`<=19` 筛固定宽度 `23`
有 `3456` 个周期零行；剥去 `19` 后仅 `912` 个仍为 `<=17` 筛零行，`2544` 个由 `19`
这一层补齐，说明零行向下剥离不是单调传递。

新增 `docs/monograph/prime-matrix-annulus-mirror-localization-audit.md` 后，用户提出的“环带零行经
镜像落入更小方阵”被进一步拆开。第一，`Row(p)` 只排除包含完整 `p` 对齐行的 q 行；它不排除
`p^2` 内跨两条 p 行的 q 缝合零窗，所以 q 零行不必先落入 `(p^2,q^2)` 环带。第二，保持零同余
覆盖的 CRT 镜像是 `n -> -n mod M_p`，行坐标为 `r -> M_p-r+1`，落在周期尾部；落入早期小区间的
是终端反射 `n -> q^2-n`，但覆盖类变为 `q^2 mod ell` 的非零类，不是零行。样本 `5<=p<=31`
中，`p^2` 内未被 `Row(p)` 排除的 q 缝合行有 `97` 条，环带行有 `60` 条；虽然 CRT 镜像的行号
有 `45` 次落入某些更小方阵早期行号，但实际成为更小方阵零行的次数为 `0`。因此可保留路线是
`terminal nonzero-class block -> PDEC/SAE`，不是“小方阵零行递归矛盾”。

新增 `experiments/prime_matrix_adjacent_shell_descent_ledger.py`、
`docs/monograph/prime-matrix-adjacent-shell-descent-ledger.md/json` 与
`docs/monograph/prime-matrix-adjacent-shell-recursive-descent-route.md` 后，用户的相邻壳层直觉被
提炼为可用的正向递归路线。严格引理为：若 `p<q` 相邻，`n<q^2` 且旧 `p`-筛幸存，则 `n`
为素数；在闭端点 `n<=q^2` 内唯一合数旧筛幸存者为 `q^2`。因此非第一行 `q` 零行确实先降为
旧 `p`-筛零窗口，最后一行至多带 `q^2` 端点穿孔。随后写 `(s-1)q=mp+a,g=q-p`，得到无损二分：

```text
a=0 or a>=p-g  => 完整 p 对齐零行；
0<a<p-g        => seam zero window，guard 长度 a 与 p-g-a。
```

有限账本到 `p<=2000` 的 `302` 个相邻素数对中 `singleton failures=0`，但最大 seam 比例约
`0.9985`，说明主分支几乎总是 guard 缝合。当前递归路线的最小硬点更新为
`SeamGuard-Elimination`：证明 seam guards 不能无代价吸收 `Row(p)` 所需幸存者；若持续吸收，
则进入 `SAE/PDEC/ColumnCRT`。

新增 `docs/monograph/prime-matrix-seam-multilevel-descent-route.md` 与
`docs/monograph/prime-matrix-seam-multilevel-descent-audit.md/json` 后，guard 缝合又被转写成
多层下降问题。若 seam 区间 `I` 已是旧 `p`-筛零窗，则降到 `h<p` 后的条件复活点为
`Rev_{h,p}(I)={n∈I:P^-(n)>h,P^-(n)<=p}`，最后 `q` 行另加 `q^2` 穿孔。任何完整
`h` 对齐行只要避开 `Rev_{h,p}(I)`，就在该条件下成为强制 `h` 零行。全量 `p<=500`
的 `21339` 条 seam 和 `p<=2000,row_stride=25` 的 `11488` 条抽样 seam 均出现此类下层零行。
这支持用户“seam 继续降阶会在某层变零行”的机制，但仍需全局证明 `SMD-Global Inequality`
或把持久复活点阻断路由到 `SAE/PDEC/ColumnCRT`。

新增 `docs/monograph/prime-matrix-seam-tail-mirror-descent-route.md` 后，上述强制下层零行又被接入
CRT 周期镜像。对 `h` 层行周期 `N_h=M_h/h`，强制零行行号 `R` 的相位为
`rho=((R-1) mod N_h)+1`，镜像相位为 `N_h-rho+1`。若任一相位不超过 `h`，则条件零行落入
`h×h` 方阵头部。全量 `p<=500` 与 `p<=2000` 抽样账本均为 `100%` 命中，其中既有直接头部相位，
也有尾镜像相位。这把递归路线的最窄硬点更新为 `TailMirror-SMD`：证明真实 seam 反例必满足此
相位命中，或证明非命中持久阻断必触发 `SAE/PDEC/ColumnCRT`。

新增 `docs/monograph/prime-matrix-total-zero-row-recursive-descent-route.md` 后，递归路线不再只覆盖
seam 分支，而是统一覆盖任意非第一 `q` 行。总模型从相邻壳层单点性出发，把假想 `q` 零行转为
旧 `p`-筛零窗，末行允许 `q^2` 穿孔；再对所有 `h<=p` 检查复活集
`P^-(n)∈(h,p]`、完整 `h` 行和 CRT 头部/尾镜像命中。全量 `p<=500` 的 `21936`
条非第一 `q` 行与 `p<=2000` 抽样 `11583` 条均闭合，未闭合 `0`。合著稿当前应把该路线命名为
`TotalDescent-TM`：若它全局成立，则强归纳给出行命题；若不成立，非命中相位必须进入
`SAE/PDEC/ColumnCRT`。

新增 `docs/monograph/prime-matrix-total-descent-h3-margin-route.md` 后，这条路线获得更窄的固定
`h=3` 版本。每条完整 3 对齐行只有一个避开 `2,3` 的六轮候选 `c_R`。若
`5<=P^-(c_R)<=p`，它是从 `p` 层降到 `3` 层时的复活阻断；若 `P^-(c_R)>p`，它已经是旧
`p`-筛零窗的幸存点，直接矛盾。因此最小接口可写成

```text
H3-SixWheel-Roughness:
|完整 3 行| > |被 [5,p] 最小素因子打断的完整 3 行|。
```

脚本 `experiments/prime_matrix_total_descent_h3_margin_audit.py` 在 `p<=5000` 全量检查
`1552462` 条 `q` 行，失败数为 `0`、最小余量为 `1`。该结果把硬点从“找某个下降层”压成
“排除六轮候选全覆盖”；但它仍接近原行命题本身，不能用有限账本或一般短区间素数定理直接升级为
全局无条件证明。若全覆盖相位存在，必须进入 `SAE/PDEC/ColumnCRT`。

新增 `docs/monograph/prime-matrix-h3-sixwheel-hard-attack.md` 后，`H3` 全阻断被改写为 first-factor
Buchstab 下降方程：每个六轮候选 `n` 唯一写成 `n=ell m`，其中 `5<=ell<=p`、
`m` 落在长度 `q/ell` 的短 cofactor 窗口且 `P^-(m)>=ell`。这给出两个硬出口：少数 `ell` 高负载
进入 Tail/PDEC；所有 `ell` 低负载但全覆盖则产生分布式低模能量或端点/ColumnCRT 相位缺陷。
因此下一步不是再扩展有限模板，而是证明 `H3 Full-Blocking Defect Theorem`。

新增 `docs/monograph/prime-matrix-h3-full-blocking-defect-audit.md` 后，数据层也支持该二分：
`p<=5000` 中 `margin<=20` 的 `4015` 个近失败窗口最高只到 `p=317`，并且聚合 first-factor
负载由 `5,7,11,13,...` 小素数阶梯主导。若全局大 `p` 反例存在，它必须是持久结构相位，
不是普通近失败；这正是 Tail/PDEC/ColumnCRT/SAE 出口应捕获的对象。

新增 `docs/monograph/prime-matrix-h3-small-factor-envelope-route.md` 后，H3 第一出口进一步压成
确定性骨架包络：固定 cutoff `y`，小首因子不过载则全阻断至少需要
`K_y=ceil(R_y/(floor(q/ell_+(y))+1))` 个中尾标签。有限账本显示 `y=31,43` 时最大强制中尾
标签数为 `7,9`。因此 H3 当前最优分支是 `SmallSkeletonOverload=>Tail/PDEC` 与
`ManyLabel=>H3-PDEC` 并行，而不是继续寻找新下降层。

新增 `docs/monograph/prime-matrix-h3-global-scaling-law-route.md` 后，该并行分支获得全局尺度解释：
H3 自然幸存尺度为 `q/log q`；数据中 bucket 平均余量与此尺度同阶，从 `p=331` 后最小余量也
脱离近失败区。故全局反例必须压灭一个增长尺度，只能通过小骨架过载、多标签低模能量或端点相位
集中来实现。

新增 `docs/monograph/prime-matrix-h3-universal-scaling-inequality.md` 后，尺度规律被写成可审稿公式：
数据版为 `M_H3>=0.30*q/log q`（`p>=113`）和尾部 `0.40*q/log q`（`p>=2011`）；理论版为
`M_H3<c*q/log q` 必触发三类命名缺陷。

新增 `docs/monograph/prime-matrix-h3-global-tail-energy-lemma.md` 后，理论版进一步内联为确定性
二分：对任意 `B,L,y`，若 `M_H3(p,s)<B`，则
`C_y>#A_s-B-2L` 或尾标签低模能量 `E_y(d)>L`，其中
`d>=2(floor(q/ell_+(y))+1)`。取 `B=c*q/log q`、`L=lambda*q/log q` 即得到全局无限通用的
尺度缺陷公式。当前目录应把 H3 主链标为“组合缺陷二分已证，出口排斥未闭合”，剩余出口为
`SmallSkeletonOverload=>Tail/PDEC` 与 `TailEnergy=>H3-PDEC/ColumnCRT`。

新增 `docs/monograph/prime-matrix-h3-small-skeleton-pdec-bridge.md` 后，`SmallSkeletonOverload`
出口也已桥接到具体 PDEC 量：`D_y=V_y-R_y>V_y-B-2L`。若 `V_y` 具有
`(c+2lambda+eta)q/log q` 余量，则得到 `D_y>eta*q/log q`。因此 H3 目录状态应更新为：
低余量反例必触发 `PDEC defect D_y` 或 `TailEnergy`；剩余是这两个缺陷的最终排斥。

新增 `docs/monograph/prime-matrix-h3-tail-energy-fourier-bridge.md` 与
`docs/monograph/prime-matrix-h3-unified-defect-criterion.md` 后，`TailEnergy` 也被精确写成
`F_y(d)>dL` 的非零 Fourier/CRT 缺陷。当前 H3 主链的总公式为：
`D_y<=V_y-B-2L` 且 `F_y(d)<=dL` 推出 `M_H3(p,s)>=B`。该公式是全局通用条件闭合判据；
无条件 H3 仍等价于补齐统一缺陷排斥。

新增 `docs/monograph/prime-matrix-h3-first-row-scale-bridge.md` 后，H3 的尺度来源被接回方阵第一行：
`Pi_1(q)=pi(q)~q/log q`，而 H3 在 `q^2` 壳层的行平均为
`(pi(q^2)-pi(q))/q~q/(2log q)~Pi_1(q)/2`。该关系由素数定理和相邻壳层单点性给出，
说明 H3 的自然质量是第一行素数质量的平方壳层投影；逐行反例必须解释为低模质量迁移缺陷。

新增 `docs/monograph/prime-matrix-h3-pointwise-closure-boundary.md` 后，目录状态应区分：
第一行尺度桥是已证全局平均定理；逐行行命题仍等价于点态尺度转移
`M_H3(p,s)>=kappa*pi(q)` 或统一缺陷排斥，不能由平均式直接推出。

新增 `docs/monograph/prime-matrix-h3-square-root-short-interval-barrier.md` 后，该点态转移又被
识别为 `x≈q^2`、`h=sqrt x` 的对齐短区间素数下界。它是标准短区间/奇偶障碍强度的硬输入；
当前文稿只能给出缺陷判据，不能无条件闭合该输入。

新增 `docs/monograph/prime-matrix-h3-square-root-defect-exclusion-hard-attack.md` 后，目录状态更新为：
`D_y` 分支已归约到标准小筛层区间筛；最终未闭合对象是尾标签/双粗补洞排斥，即证明这些尾点
不能无缺陷地精确填满整行 H3 候选。

新增 `docs/monograph/prime-matrix-h3-tail-filler-rigidity-hardcore.md` 后，尾补洞排斥已有局部核心：
相邻/二步候选互质、尾标签复用间距 `>=y/4`、三连短差值方程。全局闭合仍需证明这些局部刚性
不能沿整行拼接。

新增 `docs/monograph/prime-matrix-h3-tail-filler-global-chain-capacity.md` 后，尾补洞全局拼接已
被容量化。任一连续尾补洞块 `B` 若被拼满，则必须有 `EdgeCap(B;y)=|B|-1` 与
`TriCap(B;y)=|B|-2`；若 `y>sqrt(q+6)`，同一有序标签对在一行内最多贡献一个相邻边或三连端点；
若 `y>q^(2/3)`，所有尾点都是双粗半素数。合著稿的 H3 目录状态应更新为：
必要容量判据已证，最终剩余是证明边/三连容量严格不足，或把满容量路由到
`PDEC/ColumnCRT/endpoint/cofactor` 缺陷。

新增 `docs/monograph/prime-matrix-h3-tail-edge-selberg-exclusion.md` 后，边/三连容量已有
宏观排斥：二维 Selberg 上筛给出满尾补洞块长度 `O(q/log^2 y)`，所以整行 `~q/3`
候选全由尾标签/双粗半素数连续补洞在无限尺度上不可能。合著稿的 H3 剩余接口应更新为：
`ShortBlock-PDEC Routing`。也就是说，若坏行仍存在，尾点只能被小骨架切成许多短块；
这种高频切割必须证明会触发 `D_y/PDEC`，或由短块端点、列位移和互补商相位触发
`ColumnCRT/endpoint/cofactor`。

新增 `docs/monograph/prime-matrix-h3-shortblock-singleton-barrier.md` 后，上述接口被精细化：
尾点数 `T`、尾块数 `J`、内部相邻尾边数 `E` 满足恒等式 `T=J+E`。二维上筛只控制 `E`，
因此尾质量在坏行中主要变为单点尾块，而不是直接变成 PDEC 缺陷。合著稿应把 H3 最新剩余
硬核改写为 `Singleton Tail Exclusion`：孤立尾点 `a_j=ell_j m_j` 被左右小骨架点夹住，
满足 `a_j≡0 mod ell_j` 与 `a_j≡±delta mod r_\pm`；需证明大量此类夹逼相位不能无缺陷存在。

新增 `docs/monograph/prime-matrix-h3-singleton-clamp-defect-criterion.md` 后，孤立尾点夹逼系统
被三分支化：尾标签集中、夹逼低模集中、分散单点容量。前两项可并入
`PDEC/ColumnCRT/endpoint/cofactor` 缺陷；第三项仍是最终硬核，因为分散容量在自然尺度上
能容纳与素数余量同阶的双粗半素数。合著稿最新状态应写为：单点夹逼 CRT 判据已证，
分散有符号半素数过剩排斥未证。

新增 `docs/monograph/prime-matrix-h3-distributed-singleton-bilinear-obstruction.md` 后，该最终硬核
被改写为尾标签--互补商双线性估计：`a=ell*m`，`m` 为素数，且
`m≡ell^{-1}rho(c) mod R(c)`。合著稿最新状态应写为：分散孤立尾点坏行等价于短互补商
区间族中的有符号素数偏差；仍需证明该偏差进入 `endpoint/PDEC/ColumnCRT/cofactor`，或给出
无条件双线性上界。

新增 `docs/monograph/prime-matrix-h3-bilinear-large-sieve-defect-bridge.md` 后，合著稿最新状态
应再更新为：大有符号双线性误差必产生非主角色频率缺陷。由于普通大筛不够，最终硬输入是
短窗口 `H3-DSB-LS/KLS` 型 dispersion/Kloosterman 估计，或证明该频率缺陷已是
`PDEC/ColumnCRT/cofactor`。

新增 `docs/monograph/prime-matrix-h3-dsb-kloosterman-window-reduction.md` 后，H3 最终频率缺陷
已转为加性 Kloosterman 窗口和。合著稿应把剩余义务写成四分支：
`KLS-window` 参数覆盖、`high-lcm clamp` 排斥、`high-frequency endpoint` 吸收、系数集中排斥。

新增 `docs/monograph/prime-matrix-h3-dsb-high-lcm-clamp-routing.md` 后，`high-lcm clamp`
分支已并入总出口体系：高 `R(c)` 一行容量强制稀疏化；跨坏行持久则给出
`PDEC/ColumnCRT` 非零 Fourier/CRT 缺陷，不持久则是 `SAE` 单窗逃逸。合著稿目录状态应
写为：高 `lcm` 路由已证，最终排斥仍需证明 `Persistent-HLC` 与 `Sparse-HLC` 两个出口。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-fourier-energy-clamp.md` 后，高 `lcm` 两出口的
共同能量机制已定理化：同模块非零 Fourier 能量为 `R sum mu(a)^2-U^2`，若 `U<=R/2`
则至少为 `RU/2`。合著稿应把高 `lcm` 章节标为“能量注入已证，PDEC/ColumnCRT 与
SAE/endpoint 出口排斥未证”。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-pdec-threshold-bridge.md` 后，合著稿的
高 `lcm` 持久出口可写成同口径 PDEC 证书条件：对每个 formal unit `B`，证明
`U_CRT(B)<L_HLC(B)`，其中
`L_HLC(B)=((R sum g_B(a)^2-U_B^2)/(R-1))^(1/2)`。稠密例外 `U_B>R/2` 已路由回
KLS/PDEC/SAE，不新增出口。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-pdec-failure-localization.md` 后，合著稿应
把高 `lcm` PDEC 失败记录为 Bohr-cap 相位集中：帽内质量至少
`(L-alpha U)/(1-alpha)`。该集中不是新命题，只能进入持久 PDEC 约束或孤立
SAE/endpoint 证书。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-bohr-cap-component-route.md` 后，合著稿应
继续把 Bohr-cap 写成组件路由：大 `d=(h,R)` 是低有效模集中，小 `d` 给出短弧组件集中。
两者都必须进入 PDEC/ColumnCRT 或 SAE/endpoint，不能回流到 KLS 主项。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-high-gcd-descent.md` 后，大 `d` 分支已无损下降
到低有效模数 `R/d`，不再作为独立目录项保留；合著稿剩余应标为低有效模出口和短弧组件出口。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-short-arc-density-pressure.md` 后，短弧组件出口
应改写为密度压力判据：压力超阈值进入 PDEC 局部密度行或 SAE/endpoint；压力低区间是
显式参数残余。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-short-arc-pressure-optimizer.md` 后，压力低区间
进一步变成 `t=L/U` 阈值与 L2 平坦残余；合著稿应把它列入 KLS-window 系数二范数核验，
而不是继续作为 short-arc 独立出口。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-l2-flat-kls-admission.md` 后，合著稿应把
L2-flat residual 写成 KLS admission 问题。K1--K6 全部通过才可引用 KLS；失败项必须回到
既有出口。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-clean-kls-reduction.md` 后，合著稿 HLC 目录
应标为：内部结构归约到 clean HLC Kloosterman window，剩余为 `HLC-KLS-ext` 外部输入或
自足证明。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kls-external-adaptation.md` 后，目录状态应进一步
细分：`HLC-KLS-ext` 的外部深定理版已经完成变量适配，clean HLC branch 可标为
`external-theorem closed`；完全自足无黑箱版仍标为 `self-contained spectral/dispersion proof open`。
该区分必须保留在合著稿中，避免把“可引用 DI/BFI/Kuznetsov”误写成“本文已重证 DI/BFI”。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kls-core-reduction.md` 后，目录中应增加
`HLC-KLS-core` 节点：

```text
clean HLC window
=> dyadic/Type standard kernel
=> HLC-KLS-core (CORE-5)
=> HLC-KLS-ext (CKR-5).
```

这把完全自足版的剩余从宽泛谱理论重证压缩为单一核心平均命题；但在 `(CORE-5)` 未证明或
未精确引用前，仍不得标为完全无黑箱闭合。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kls-core-self-contained-spine.md` 后，理论目录应在
`HLC-KLS-core` 下再挂一个自足证明脊柱：

```text
CORE-5
=> smooth completion + Kloosterman quadratic form
=> Kuznetsov-LS atom (SC-9)
=> CORE-5.
```

该节点把唯一未内联证明行精确标为 `(SC-9)`，并记录普通 Weil 界不足以替代谱平均。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kuznetsov-ls-atom-expansion.md` 后，目录应在
`SC-9` 下展开五个谱子原子：

```text
SC-9
=> KZ-A smoothing
 + KZ-B Kuznetsov trace formula
 + KZ-C Bessel transform decay
 + KZ-D spectral large sieve
 + KZ-E BFI/well-factorable logarithmic saving.
```

该文件证明 KZ-A--KZ-E 推出 `SC-9`；在该阶段 KZ-B--KZ-E 尚未内联证明。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kz-c-bessel-transform-decay.md` 后，KZ-C 已内联
证明，当时剩余子原子为 KZ-B、KZ-D、KZ-E。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kz-d-spectral-large-sieve-spine.md` 后，KZ-D
目录节点展开为：

```text
KZ-D
=> dual spectral kernel
=> PTK-D pretrace kernel bound
=> KZ-D.
```

oldform、Eisenstein、holomorphic 谱只保留为多对数账本；当时未闭合核心是 PTK-D。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-ptk-d-pretrace-kernel-bound.md` 后，PTK-D 目录节点
继续展开为：

```text
PTK-D
=> pretrace/Poincare coefficient kernel
=> diagonal T^2 volume
=> LPC-D spatial row-column correlation bound
=> PTK-D.
```

当时未闭合核心变为 LPC-D。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-lpc-d-spatial-correlation-split.md` 后，LPC-D
目录节点展开为：

```text
LPC-D
=> FAR tail closed
 + ID-near absorbed into PAR
 + PAR cusp divisor ledger closed
 + GHLC-D generic hyperbolic local correlation
=> LPC-D.
```

当时未闭合核心变为 GHLC-D。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-ghlc-d-local-schur-closure.md` 后，GHLC-D
被闭合为局部核质量问题：

```text
GHLC-D
=> local L1 mass of k_T on radius T^{-1}log^B y balls
=> Poincare-packet Schur row/column bound
=> LPC-D => PTK-D => KZ-D.
```

核心修正是不用点态 hyperbolic 格点计数控制 `k_T(0)≈T^2`，而在预迹积分核中使用局部面积
`T^{-2}` 抵消核高。KZ-D 因此不再是完全自足链的未闭合原子。剩余谱/dispersion 原子缩为：

```text
KZ-B specialized Kuznetsov trace formula
KZ-E BFI/well-factorable logarithmic saving.
```

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kz-b-kuznetsov-trace-specialization.md` 后，KZ-B
也已内联为等式推导：

```text
automorphic kernel
=> Poincare packet unfolding
=> double-coset Kloosterman geometric side
=> spectral Plancherel side
=> KZ-B.
```

这一步不提供对数节省，只闭合 trace formula 的公式和归一化。完全自足链的剩余单原子因此
更新为：

```text
KZ-E BFI/well-factorable dispersion logarithmic saving.
```

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kz-e-well-factorable-dispersion-spine.md` 后，
KZ-E 已进一步拆为：

```text
well-factorable convolution algebra
+ dispersion variance identity
+ CRT normalization to Kloosterman phase
+ gcd/endpoint/polylog ledger
+ WFD-core
=> KZ-E.
```

其中前四项是文内账本，已严写；剩余唯一深核是

```text
WFD-core windowed well-factorable Kloosterman dispersion mean estimate.
```

该核未证明前，合著稿仍不得宣称 HLC/SC-9/CORE-5 完全自足闭合。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-wfd-core-balanced-factor-reduction.md` 后，
`WFD-core` 进一步平方根平衡化：

```text
lambda_c well-factorable
=> c=uv, u,v≈c^{1/2}
=> gcd strata polylog ledger
=> CRT factorization of e_{uv}(as+b\bar s)
=> BWFD-core
=> WFD-core.
```

该步当时的唯一剩余核为：

```text
BWFD-core balanced two-modulus well-factorable Kloosterman dispersion mean estimate.
```

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-bwfd-core-spectral-completion-attack.md` 后，
`BWFD-core` 进一步完成化：

```text
s-variable finite Fourier completion
+ complete Kloosterman multiplicativity modulo uv
+ balanced u,v spectral bilinear correlation
=> BWFD-core
=> WFD-core
=> KZ-E.
```

普通 KZ-D 只恢复 raw 二范数尺度，点态 Weil 只给单点平方根抵消，均不能产生任意
`log^{-A}`。当前唯一剩余核因此更新为：

```text
BSC-core balanced complete Kloosterman bilinear correlation logarithmic saving.
```

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-bsc-core-kloosterman-fraction-attack.md` 后，
`BSC-core` 进一步显形化：

```text
complete Kloosterman expansion
+ phase e(bar v R/u + bar u T/v)
+ degenerate quadratic congruence ledger
+ non-degenerate two-modulus reciprocal-fraction average
=> BSC-core
=> BWFD-core
=> WFD-core
=> KZ-E.
```

当前唯一剩余核更新为：

```text
KFLS-core balanced Kloosterman-fraction large sieve logarithmic saving.
```

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-kfls-core-square-kernel-attack.md` 后，
`KFLS-core` 进一步平方化：

```text
square expansion of e(bar v R/u + bar u T/v)
+ exact diagonal/raw norm ledger
+ semi-diagonal layers
+ centered true off-diagonal four-modulus kernel
=> KFLS-core
=> BSC-core
=> BWFD-core
=> WFD-core
=> KZ-E.
```

该文件同时排除一条错误闭合路线：全核绝对 Schur 受对角质量阻断，只能恢复 raw 二范数尺度，
不能产生任意 `log^{-A}`。当前唯一剩余核更新为：

```text
CFQK-core centered four-modulus Kloosterman-fraction correlation saving.
```

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-cfqk-core-block-centering-attack.md` 后，`CFQK-core`
的半对角条款被修正：

```text
same (u,v) block diagonal = local variance, not a log-saving error
+ block-centering identity BD-CEN
+ one-shared-modulus core OSQK
+ true-four-modulus core TFQK
=> KFLS-core
=> BSC-core
=> BWFD-core
=> WFD-core
=> KZ-E.
```

当前剩余更新为：

```text
BD-CEN + OSQK-core + TFQK-core.
```

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-bd-cen-dispersion-centering-audit.md` 后，`BD-CEN`
被单独核查。结论是当前 KZ-E spine 只证明 `h=0` 主项抵消，没有证明同 `(u,v)` 块投影扣除

```text
|sum_b S_b|^2 - sum_b |S_b|^2.
```

该审计阶段的第一阻断点曾明确为：

```text
BD-CEN identity (BDC-5).
```

随后 no-go 文件进一步表明该身份在当前对象下失败；因此不能再把 `BD-CEN` 当作普通待证引理。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-bd-cen-no-go-route-fork.md` 后，`BD-CEN` 在当前对象
下被反证。单块非零模型显示 `h=0` 中心化不能推出块中心化，`(BDC-5)` 对当前未块中心化
WFD/KZ-E 对象失败。当前路线必须分叉为：

```text
SOURCE-CEN
or BLK-energy-core
or external DI/BFI.
```

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-source-cen-no-go.md` 后，`SOURCE-CEN` 也被核查并
反证。当前 `WFD-core (KE-13)` 是未块中心化的线性 Kloosterman 窗口；若在源头替换成同
`(u,v)` 块中心化对象，就改变了目标对象，并留下必须另估的块均值项。因此 `SOURCE-CEN`
不能作为当前无黑箱平方核路线的出口。

新增 `docs/monograph/prime-matrix-h3-dsb-hlc-blk-energy-core-obstruction.md` 后，裸
`BLK-energy-core` 也被进一步核查：若把它表述成平方核层任意系数数组定理，单块单原子测试使
`\sum_b |S_b|^2` 与 raw 二范数同阶，不能再额外获得任意 `\log^{-A}`。当前内部无黑箱路线
的真实最窄义务因此更新为：

```text
NC-BLK:
prove actual WFD coefficients are block-nonconcentrated strongly enough
to imply the block-energy estimate.
```

若不证明 `NC-BLK`，则只能走：

```text
external DI/BFI original dispersion theorem route.
```

## 19. RPZ first-grid-fail seam 的单余类证书化

新增增强版 `docs/monograph/prime-matrix-rpz-first-grid-fail-seam-certificate.md` 后，
首个 `grid_fail` seam 不再只是几何标准形，而被拆成可接入 PDEC/ColumnCRT 的精确账本。
对每个相邻下降 `p->r`，令 `Q=prod_{ell<=r}ell`、`g=p-r`、
`delta=-(a-1)g mod r`。若 `g<delta<r`，则对应相位行满足

```text
S_tau={a mod Q: a≡rho mod r}；
F_tau=1_{a≡rho mod r}-1/r；
nonzero Fourier support={Q/r,2Q/r,...,(r-1)Q/r}。
```

脚本 `experiments/prime_matrix_rpz_first_grid_fail_seam_certificate.py` 现在同时给出端点分裂：

```text
grid_fail phases in full Q: 1752
PDEC/Fourier support rows: 12
endpoint killed by lower labels: 1348
endpoint Q-unit branch: 404
```

这一步的意义是把 seam 的 PDEC 输入行、测试函数、Fourier 支持和端点 lower-label/unit
分支都固定下来。它仍不是排斥定理：`404` 个 unit endpoint 相位还需要 endpoint-PDEC 的
`U_CRT<L_PDEC` 上界，或 ColumnCRT 的列见证选择器 `Pi`、标签选择器 `lambda`、
位移余类与阈值 `L_D`。因此合著稿中的最新最小硬点应写为：

```text
unit endpoint seam branch
=> endpoint-PDEC upper bound
   or ColumnCRT displacement threshold certificate。
```

新增 `docs/monograph/prime-matrix-rpz-unit-endpoint-columncrt-gate.md` 后，该硬点又被压缩一层。
对每条 unit endpoint seam，端点在下层 `r` 网格中的列满足

```text
c=ap mod r=p*rho mod r=r+(p-r)-delta，
```

所以 `c` 是固定非平凡列；若同列素数见证为 `pi=h*r+c`，则端点下层行号满足

```text
H_endpoint ≡ -c*r^{-1} mod p，
d=h-H_endpoint mod p != 0。
```

当前有限账本中 `12/12` 门控行有显式同列素数见证，`12/12` 行给出非零位移，覆盖全部
`404` 个 unit endpoint 相位。故持久 unit endpoint seam 已被标准化为
`ColumnCRTDefect(p,d)` 候选。剩余真正硬点更新为：

```text
formal counterexample family -> unit endpoint gate rows
and ColumnCRTDefect(p,d) threshold L_D exclusion。
```

继续新增 `docs/monograph/prime-matrix-rpz-columncrt-threshold-obstruction.md` 后，`L_D` 路线本身被
审到底。固定 unit gate 中，所有 unit residues 已经具有同一个标签 `p` 和同一个非零位移
`d mod p`，所以

```text
R_{p,d} >= prod_{ell<r}(ell-1)。
```

当前账本最大内禀负载为 `48`；若使用既有有限样本中的位移负载阈值 `L_D=2`，则 `10`
条门控行、`400` 个相位都会超过阈值。该结果不是矛盾，而是表明这些相位进入
`ColumnCRTDefect`。因此最小硬点的严格状态应更新为：

```text
unit endpoint gate
=> fixed nonzero ColumnCRTDefect(p,d)
but threshold tuning alone cannot exclude it.
```

剩余合法闭合路线只剩三条：证明正式反例族避开 unit gate；证明 endpoint-PDEC 的
`U_CRT<L_PDEC`；或给出独立的 `ColumnCRTDefect` 排斥定理。

新增 `docs/monograph/prime-matrix-rpz-three-route-closure-audit.md` 后，这三条路线被同口径排序：

```text
rank 1: A_formal_family_avoidance
rank 2: B_endpoint_PDEC
rank 3: C_columnCRT_defect_exclusion
```

排序依据是：路线 A 与当前有限下降账本完全一致，`20` 个实际转换节点中 `grid_fail=0`；
路线 B 已完成支持行和测试函数，但没有 `U_CRT` 上界；路线 C 已完成固定非零位移入口，但
阈值调参被内禀负载障碍阻断。因此下一步主攻应从路线 A 的 formal-family 相位避开定理开始。

新增 `docs/monograph/prime-matrix-rpz-formal-phase-automaton.md` 后，路线 A 的目标被压成接受集准入。
定义 `A_p` 为模 `P(p)` 的相位集合：相位在 `A_p` 中当且仅当 canonical 下降路径逐步满足
`delta<=p-r` 并到达 `p=2`。当前自动机给出：

```text
max start prime = 13
current starts = 6
current starts accepted = 6
global formal-family closed = false
```

接受密度在当前层为：

```text
p=7: 126/210
p=11: 990/2310
p=13: 3510/30030
```

这说明当前账本的 A 路线已闭合，但全局 formal-family 仍需证明起始相位总落入 `A_p`，或把
`P(p)\setminus A_p` 的命中送入已物化的 seam/PDEC/ColumnCRT 链。

新增 `docs/monograph/prime-matrix-rpz-rejected-phase-absorption.md` 后，后一项在当前自动机范围内
已完全证书化。所有拒绝相位均有首个失败 seam，且全部属于已物化的 `12` 条 seam 行：

```text
total rejected phases = 27924
distinct first-fail seams = 12
uncovered rejected examples = 0
```

因此 RPZ formal-family 路线现在是一个完整的“接受/拒绝路由”：

```text
start phase in A_p      => canonical descent => p=2 contradiction；
start phase not in A_p  => materialized first-grid-fail seam => PDEC/ColumnCRT/SAE。
```

这不是最终无条件闭合，因为 seam/PDEC/ColumnCRT 出口本身仍未排除；但它已排除 rejected set
存在第三逃逸的可能。

新增 `docs/monograph/prime-matrix-rpz-seam-exit-pressure-ledger.md` 后，剩余出口进一步压缩：

```text
rejected phases absorbed = 27924
seam rows = 12
total seam support = 1752
killed endpoint phases = 1348
unit endpoint phases = 404
ColumnCRT displacement classes = 10
max aggregated displacement load = 96
```

因此当前真正硬点已经不是逐相位搜索，而是 `12` 条 seam 行、`12` 条单余类 PDEC 支持行、
以及聚合后的 `10` 个固定非零 ColumnCRT 位移类。若要继续推进，只能证明 formal-family 避开
这些 seam 行，或提交同口径 `U_CRT<L_PDEC` / `ColumnCRTDefect` 排斥证书。

新增 `docs/monograph/prime-matrix-rpz-symbolic-ladder-certificate.md` 后，首选 formal-family 避开
路线进一步改写为相邻素数阶梯数字约束。对 `p>r`、`g=p-r`：

```text
delta_p(a)=-(a-1)g mod r；
success iff delta_p(a)<=g；
first fail iff delta_p(a)>g。
```

该证书在 `P(19)=9699690` 以内逐相位枚举核验计数公式无不一致，并把符号阶梯延伸到
`p=97`。剩余证明义务不再是枚举 `A_p`，而是从正式反例构造本身推出每层
`delta_p(a)<=g`；若某层失败，则已回流到前述 seam/PDEC/ColumnCRT 出口。

新增 `docs/monograph/prime-matrix-rpz-bcb-start-digit-ledger.md` 后，当前 BCB-Core 起始行的实际
数字也已逐项抽取：

```text
start rows = 6
digit nodes = 20
safe digit nodes = 20
grid-fail digit nodes = 0
boundary margin=0 nodes = 10
minimum margin = 0
```

这说明当前样本确实全部避开 seam，但有一半节点贴在 `delta=gap` 边界上。下一步不能靠
粗余量估计，必须从起始行构造中证明精确同余余类落入 allowed residues。

新增 `docs/monograph/prime-matrix-rpz-bcb-accepted-row-selector.md` 后，正向目标再弱化为足够的
选择器命题。对 BCB 核心区间 `J=[u,v]` 与半宽素数 `h`，令

```text
C_h(J)={m: u <= (m-1)h+1 and mh <= v}。
```

只需证明 `C_h(J)∩A_h` 非空即可选择一条 accepted lower zero-row 下降。当前 `5/5` 个
BCB-Core 样本存在 selector，`6/6` 个候选完整下层行全部 accepted。剩余全局义务是证明正式
BCB-Core 的端点相位和长度强制该相交；若相交为空，则全体候选行回流到 seam/PDEC/ColumnCRT。

新增 `docs/monograph/prime-matrix-rpz-selector-gap-threshold.md` 后，selector 存在被拆成两支：

```text
长度分支：|C_h(J)| >= max_rejected_run(A_h)+1；
短候选相位分支：|C_h(J)| 较小时，端点相位必须精确避开 rejected gaps。
```

当前层的最大 rejected run 为：`h=5:0`、`h=7:1`、`h=11:5`、`h=13:15`。样本中 `2/5`
由长度单独强制 selector，`3/5` 仍依赖短候选端点相位。因此下一步必须直接攻短候选端点相位，
不能只强化核心长度估计。

新增 `docs/monograph/prime-matrix-rpz-short-candidate-phase-ledger.md` 后，短候选端点相位已从
`u mod h` 细化到 `u mod hP(h)`。当前 `3/3` 个短候选实际样本都有 accepted selector；
但完整相位族仍存在 all-rejected 相位：`(h,length)=(7,13)` 有 `588` 个、`(11,19)` 有
`11880` 个、`(13,25)` 有 `344760` 个。每个 all-rejected 相位都带有
`first_failure_key`，可回流到 seam/PDEC/ColumnCRT。剩余义务因此变成更精确的二选一：
证明正式 BCB 构造的端点相位避开这些 all-rejected 类，或逐项闭合对应出口证书。

新增 `docs/monograph/prime-matrix-rpz-short-phase-block-formula.md` 后，短候选端点禁区进一步
公式化。因当前短候选均满足 `length<2h`，一个端点最多包含一个完整 `h` 行；行号 `m`
对应端点块

```text
mh-length+1 <= u <= (m-1)h+1，
```

块宽为 `length-h+1`。于是 all-rejected 端点集合等于 rejected 行相位块的并集。三族公式均与
完整枚举一致；实际端点到 all-rejected 集合的距离分别为 `7,6,1`。剩余硬点被压成：
从正式 BCB 构造推出候选行相位属于 `A_h`，否则闭合其 first-failure 出口。

新增 `docs/monograph/prime-matrix-rpz-bcb-candidate-phase-identity.md` 后，候选行相位已从 BCB
参数中显式抽取。若上层零行号为 `R`、上层素数为 `P`、半宽素数为 `h`、平台端点为
`s_min,s_max`、尾锚阈值为 `T`，则

```text
L=(R-1)P+1+s_min+T，
U=RP+s_max-T，
m_min=floor((L+h-2)/h)+1，
m_max=floor(U/h)。
```

写 `P=Qh+d` 后，`m_min,m_max mod P(h)` 只依赖 `R mod hP(h)` 与平台参数。当前 `5/5`
条 BCB 样本公式匹配，`6/6` 个候选行相位 accepted。剩余全局义务进一步变为：
证明正式反例的 `R mod hP(h)` 必诱导 accepted 候选相位；失败则进入对应 first-failure 出口。

新增 `docs/monograph/prime-matrix-rpz-bcb-accepted-preimage-ledger.md` 后，accepted preimage 已对
当前 BCB 参数族逐项枚举。`P=13,h=5` 参数族没有 bad residue；其余四族仍有 bad residue，
类型为 `no_candidate` 或 `all_rejected`。当前实际 `R mod hP(h)` 全部落入 selector preimage；
到 bad residue 的距离为：`P=17` 为 `7`、`P=19` 为 `3`、`P=23` 为 `2`、`P=29` 为 `1`。
因此剩余义务不再是计算 preimage，而是证明 formal BCB 的顶层行 residue 必落入该 preimage；
否则按 `no_candidate` 回到 BCB endpoint，或按 `all_rejected` 回到 first-failure 出口。

新增 `docs/monograph/prime-matrix-rpz-bcb-core-run-obstruction.md` 后，BCB no-TailAnchor 分支有了
更上游的长度障碍。no-TailAnchor 强制 `J_T0` 是 `h`-筛零区间，因此 `|J_T0|` 不能超过
模 `P(h)` 中由 `<=h` 素数覆盖的最大连续长度。当前精确值为：

```text
h=5: 5，h=7: 9，h=11: 13，h=13: 21。
```

当前五个 BCB 核心长度为 `9,13,15,19,25`，全部严格超过对应上界，最小余量为 `4`。
因此当前有限 BCB no-TailAnchor 参数族已被核心低筛长度障碍排斥。全局剩余义务上移为
Jacobsthal 型低筛覆盖长度上界；若不能给出该上界，则仍按 endpoint/first-failure 出口路由。

新增 `docs/monograph/prime-matrix-rpz-bcb-jacobsthal-closure-interface.md` 后，这个全局义务被写成
精确闭合判据。记 `G(h)` 为所有点均被某个 `<=h` 素数整除的最长连续区间长度。正式 BCB
参数 `(P,h,m,T)` 的 no-TailAnchor 分支闭合当且仅当可证明

```text
G(h) < P+m-1-2T。
```

当前 finite 样本满足该不等式；全局证明仍需给出 formal 层的 Jacobsthal 型上界，或者继续保留
TailAnchor、endpoint、first-failure、PDEC、ColumnCRT 出口。

新增 `docs/monograph/prime-matrix-rpz-bcb-jacobsthal-risk-scan.md` 后，必须修正全局路线预期：
若只使用 `m=5,T=4,P>2h`，则 `G(h)<P-4` 不可能作为全局闭合输入。基于
Ziller--Morack primorial Jacobsthal 附属数据的风险扫描显示，首个非平凡失败在 `h=43`：
`G(h)=89`、最小 `P>2h` 为 `89`、核心长度为 `85`。因此下一步必须证明 formal BCB 平台长度
`m` 随层增长，或证明 bad 参数族进入 TailAnchor/endpoint/first-failure/PDEC/ColumnCRT。

新增 `docs/monograph/prime-matrix-rpz-bcb-platform-length-threshold.md` 后，平台增长目标已写成
精确整数阈值：

```text
m >= G(h)-P+2+2T。
```

当 `T=4` 时，首个 `h>=5` 实质不安全层为 `h=43`，所需平台长度为 `10`。因此下一硬点不再是
“是否存在 accepted selector”，而是证明 formal BCB 平台长度达到该阈值，或短平台触发已命名出口。

新增 `docs/monograph/prime-matrix-rpz-bcb-short-platform-embedding-route.md` 后，短平台出口也已命名：
若 `N=P+m-1-2T<=G(h)` 且 no-TailAnchor 成立，则 `J_T` 必须嵌入模 `P(h)` 的某个低筛极大覆盖块。
因此 `left(J_T) mod P(h)` 属于有限 Jacobsthal endpoint set `E_{h,N}`。该相位若低负载进入
`SAE`，若持续复现进入 `PDEC/ColumnCRT`。

新增 `docs/monograph/prime-matrix-rpz-bcb-short-platform-embedding-certificate.md` 后，最长块端点
子族 `Emax_{h,N}` 已材料化：脚本从 Ziller--Morack 的最长覆盖块模表示重建 CRT 左端相位，并
验证 `1197` 个最长块的覆盖性与边界非覆盖，验证失败数为 `0`。审稿边界保持不变：这不是完整
`E_{h,N}` 枚举；下一义务是证明任意长度 `>=N` 的覆盖块可归入最长块相位族，或生成完整覆盖块证书。

## 17. Triad-A1 自足边界最终评审并入

最新最终评审文件为：

```text
docs/monograph/prime-matrix-triad-a1-self-contained-theorem-boundary-review.md
docs/monograph/prime-matrix-row-theorem-final-boundary-plain-language.md
```

该评审把“已经闭合的命题”和“不能声明的更强命题”彻底分开。

### 17.1 通俗边界

已经闭合的是：

```text
Triad-A1 same-set capacity / full-S terminal
on the canonical RIW/Buchstab source branch.
```

直观解释是：只要 A1 链条的实际来源固定为 canonical RIW/Buchstab 决策树权重，那么同一坏窗集合上的容量上界、来源账本、分支覆盖、最终闭合证书和定理边界评审已经全部对齐。该分支不再需要借用外部 FullS-KLS-ext 作为自足证明的一部分。

不能声明的是：

```text
Unrestricted generic full-S well-factorable WFD self-contained theorem.
```

原因是 moving-delta no-go 已经反证当前 generic WFD 反原子输入。也就是说，generic WFD 宽口径不是“还剩一个普通证明缺口”，而是在当前形式假设下可被移动块容量模型击穿。

### 17.2 七门评审结论

最终评审裁定为：

```text
APPROVE_CANONICAL_SOURCE_SELF_CONTAINED_BOUNDARY
```

通过的七个门控为：

1. `TheoremStatementBoundaryExact`：闭合定理只限 canonical-source 分支；
2. `FinalClosureCertificateClosed`：final closure 证书无开放门；
3. `FrontierAbsorbsFinalBoundary`：same-set capacity frontier 已吸收最终边界；
4. `CanonicalSourceProvenanceClosed`：实际来源已闭合到 canonical RIW/Buchstab；
5. `BranchCoverageNoSilentUpgrade`：canonical 与 generic 分支没有静默混用；
6. `GenericUnrestrictedNoFalseClaim`：generic 自足版被反证，不写成闭合；
7. `ExternalContractSeparatedFromSelfContainedClaim`：外部 FullS-KLS-ext 合同与自足证明分离。

终端状态为：

```text
NoFurtherTheoremBoundaryReviewGap
```

### 17.3 对合著总状态的影响

合著稿中应新增如下状态规则：

```text
Triad-A1 canonical-source self-contained boundary: closed.
Triad-A1 unrestricted generic self-contained theorem: refuted and not claimed.
unrestricted generic WFD 自足版已反证，不能作为闭合命题声明。
Prime Matrix full row/column theorem: not promoted by this boundary alone.
```

因此，Triad-A1 的 canonical-source 边界已从“最窄剩余”升级为“已闭合边界”；但完整 Prime Matrix 行/列无条件定理仍必须单独完成终端证书排斥：

```text
PDEC family certificates；
LocalSurvivorCert family；
CleanKLS/DLS certificates or explicit ExternalKLS input；
D-structure/Tail-log4/Rankin/referee-block interfaces。
```

这与主稿 `paper/contradiction-field-monograph/contradiction-field-monograph.tex` 的新节
`Triad-A1 Self-Contained Theorem-Boundary Closure` 保持一致。

## 18. 行列无条件自足前沿路由与 FO-PDEC 嵌套重复子门

新增：

```text
experiments/prime_matrix_wsh_fo_pdec_nested_duplicate_dominance_audit.py
docs/monograph/prime-matrix-wsh-fo-pdec-nested-duplicate-dominance-audit.md/json
experiments/prime_matrix_wsh_fo_pdec_weighted_hall_dual_audit.py
docs/monograph/prime-matrix-wsh-fo-pdec-weighted-hall-dual-audit.md/json
docs/monograph/prime-matrix-wsh-fo-pdec-weighted-hall-dual-dominance.md
experiments/prime_matrix_wsh_fo_pdec_cross_q_chart_overlap_audit.py
docs/monograph/prime-matrix-wsh-fo-pdec-cross-q-chart-overlap-audit.md/json
docs/monograph/prime-matrix-wsh-fo-pdec-cross-q-chart-overlap-dominance.md
experiments/prime_matrix_wsh_fo_pdec_physical_primitive_tautology_audit.py
docs/monograph/prime-matrix-wsh-fo-pdec-physical-primitive-tautology-audit.md/json
docs/monograph/prime-matrix-wsh-fo-pdec-physical-primitive-tautology.md
experiments/prime_matrix_wsh_fo_pdec_sae_endpoint_absorption_audit.py
docs/monograph/prime-matrix-wsh-fo-pdec-sae-endpoint-absorption-audit.md/json
docs/monograph/prime-matrix-wsh-fo-pdec-sae-endpoint-absorption.md
experiments/prime_matrix_local_survivor_materialized_packet_ledger.py
docs/monograph/prime-matrix-local-survivor-materialized-packet-ledger.md/json
docs/monograph/prime-matrix-local-survivor-packet-generation-contract.md
experiments/prime_matrix_local_survivor_packet_extractor_coverage.py
docs/monograph/prime-matrix-local-survivor-packet-extractor-coverage.md/json
experiments/prime_matrix_new_sparse_entry_admission_audit.py
docs/monograph/prime-matrix-new-sparse-entry-admission-audit.md/json
experiments/prime_matrix_row_column_unconditional_frontier_router.py
docs/monograph/prime-matrix-row-column-unconditional-frontier-router.md/json
```

本轮没有把完整 Prime Matrix 行/列命题升级为无条件定理；相反，前沿路由器把边界进一步压清：

```text
canonical-source Triad-A1 自足边界：已闭合；
unrestricted generic WFD 自足版：已反证且不声明；
终端三证书接口：无第四出口，但三终端证书全集未提交；
当前最窄硬点：A1-FO-PDEC-SameFormalUnit。
```

其中 FO-PDEC 的 `ell=199,h=95` 强信号仍是库级诊断：

```text
raw Fourier = 3.959247567099438；
q-row coordinate dedup best = 1.0；
block-local best = 1.0。
```

新的嵌套重复支配审计闭合了一个子门：当前 7 个 exact nested duplicates 全部是同一正式坐标上的
嵌套支撑重复，且 `factor=199` 的关键重复也在其中。因此这些重复不能按单位权作为两个独立 PDEC
事件计数。若要保留权重，必须给出同一多重 formal unit 上的 fractional Weighted Hall dual；
否则应坐标商掉，转入 primitive PDEC 阈值或 SAE/Endpoint 吸收。

进一步的 weighted-Hall 审计显示，fractional Weighted Hall dual 也不能恢复完整第二单位质量：
每个嵌套对都是 laminar 支撑，差层只增加 `1` 个半素数与 `1` 个邻近素数，`Delta surplus=0`，
没有新的 Hall 压力可支付重复坐标。因此强阈值必须降口径：

```text
global_library_raw:      3.959247567099438
nested_coordinate_cap:   2.9698366905785227
physical_candidate_cap:  1.9997507790353146
single formal branch:    1.0
```

因此下一步不应回到泛化 generic WFD，也不应直接使用 raw `U_CRT,199<3.959...`。最窄可攻路线更新为：

```text
cross-q persistence theorem；
若成立，攻 coordinate-cap PDEC threshold U_CRT < 2.9698366905785227；
若失败，转 physical/primitive PDEC threshold 或 SAE/Endpoint absorption。
```

最新 cross-q 坐标图审计进一步关闭了当前样本的 cross-q persistence 路线。9 个跨 `q` 复用全部是
同一物理候选在 `q=773,row=325` 与 `q=967,row=260` 两张重叠坐标图中的表示，满足：

```text
base_gap = 1；
column_gap = -1；
candidate_gap = 0；
same candidate / semiprime / offset / factor = true。
```

关键 `factor=199` 复用 `250541=199*1259` 也在其中。因此 coordinate-cap `2.9698366905785227`
不能作为当前正式分支下界；前沿继续降到：

```text
physical/primitive PDEC threshold U_CRT < 1.9997507790353146；
或 SAE/Endpoint absorption for physical cross-chart reuses。
```

physical/primitive 子门继续审计后，发现 `1.9997507790353146` 不是新的结构缺陷阈值，而是
二点 Fourier 恒等式：

```text
2*cos(pi/199)=1.9997507790353146。
```

原因是模素数上任意两个不同残基都可由某个非零频率送成相邻对偶点。因此当前两个 physical
primitive 原子不能继续作为非退化 PDEC 下界。进一步送入 `SAE/Endpoint` 后，每个来源行在同一
固定偏移纤维里都有本地素数见证：

```text
250541  -> witness 250543；
1664237 -> witness 1664227。
```

且 `factor=199` 在这些纤维中的负载均为 `1`。所以当前已审计的 `ell=199` 强信号链已经完整降口径：

```text
raw library signal      -> nested duplicate / weighted Hall 阻断；
coordinate-cap signal   -> cross-q 坐标图重叠阻断；
physical two-point      -> Fourier tautology；
two physical atoms      -> LocalSurvivor witness 吸收。
```

新的最窄剩余不再是继续优化当前 `U_CRT` 常数，而是：

```text
global LocalSurvivorCert family；
or future primitive PDEC with >=3 non-tautological physical atoms or extra constraints；
plus CleanKLS/DLS and D-structure/Rankin referee inputs for final theorem promotion。
```

继续合并 LocalSurvivor 总账后，当前已经物化到机器账本的孤窗包也被清空：

```text
materialized packets: 9；
materialized phase atoms: 32；
local survivor witnesses: 5；
finite PDEC atoms: 25；
open materialized obligations: 0。
```

这合并了三类当前来源：Triad-A1 SparseCap、FO-PDEC 二点 SAE/Endpoint、RPZ Endpoint-SAE 有限
账本。于是 `LocalSurvivor` 的剩余从“逐个已知孤窗找 witness”改写为生成问题：

```text
PacketExtractorCompleteness:
  every future sparse escape emits a finite LocalSurvivor packet;

NonTautologicalPDEC:
  same formal unit has >=3 physical atoms
  or fixed-frequency constraints defeat two-point tautology;

CleanKLS/DLS:
  signature layers escape every finite packet.
```

`prime-matrix-local-survivor-packet-generation-contract.md` 同时证明无名孤窗不能作为第四终端停留：
同签名无限复现进入 `PDEC/ColumnCRT/TailAnchor/CofactorAnchor`，签名层级逃逸进入 `CleanKLS/DLS`，
下降或 seam 路线回到已命名包。因此新的最窄硬点更新为
`LocalSurvivorPacketGenerationOrNonTautologicalPDEC`。

进一步新增 extractor 覆盖审计与新入口准入审计后，LocalSurvivor 分支继续收缩：

```text
KnownLocalSurvivorEntryExtractorsCovered:
  entry_count=8；
  materialized_script_entry_count=4；
  contract_entry_count=4；
  missing_or_open_count=0。

NoAdditionalUnnamedLocalSurvivorEntryRoute:
  admission_source_count=8；
  missing_admission_count=0。
```

含义是：Triad-A1 SparseCap、FO-PDEC 二点 SAE/Endpoint、RPZ Endpoint-SAE 与聚合总账都有机器
extractor；generic SAE、持久签名、升层 clean 和 descent/seam 都有合同回流。短窗、endpoint、
Bohr-cap、tail/cofactor、descent/seam 等所有可能产生孤窗的来源都已命名到
`SAE/LocalSurvivor/PDEC/ColumnCRT/CleanKLS`。因此 LocalSurvivor 当前分支只剩条件性义务：
若未来提出新的显式 sparse 路线，必须同时提交 extractor schema 与有限账本。当前主硬点转为：

```text
NonTautologicalPDECOrCleanKLS。
```

再把已存在的 CleanKLS/DLS 路由接入总前沿后，这个宽口径继续收缩。`A1 CleanKLS` 只有在
K1--K9 准入全部通过时才可调用；失败项已经回流
`PDEC/SAE/Multiplicity/Promotion`。全部通过时进入 `SC-9`，而 `SC-9` 又由
`prime-matrix-triad-a1-kuznetsov-ls-atom-frontier-router.md` 展开为：

```text
KZ-A--KZ-D: 已由平滑、trace specialization、Bessel decay、
            spectral large-sieve/pretrace 链路由；
KZ-E:       剩 NC-BLK actual block non-concentration
            或外部 DI/BFI original dispersion。
```

所以总前沿中的 CleanKLS 不再是一个未定义黑箱。当前真实最窄硬点更新为：

```text
NonTautologicalPDECOrNCBLK。
```

新增 `prime-matrix-ncblk-boundary-reconciliation-router.md` 后，这个 `NC-BLK` 标签的边界读法被固定：

```text
canonical source branch:
  NC-BLK clean-KLS chain is absorbed by the existing same-set capacity boundary;

generic full-S non-AP branch:
  NC-BLK remains exact source entropy or external DI/BFI/Kuznetsov.
```

因此 `NC-BLK` 不再是无名 CleanKLS 出口，也不能被误读成全局行/列定理闭合。它的作用是把
canonical-source 边界闭合与 generic noncanonical 外部路线分开；完整行/列无条件定理仍需独立
终端证书，尤其是 PDEC family、LocalSurvivorCert family、CleanKLS/ExternalKLS 和
D-structure/Rankin/referee-block 接口。

新增 `prime-matrix-nontautological-pdec-admission-audit.md` 后，PDEC 侧当前已物化候选也被审计到
零：

```text
raw three-point signal:
  not admissible without same formal unit and independence;

nested / weighted / cross-q reductions:
  duplicate mass and chart overlap are blocked;

physical primitive remnant:
  two-point Fourier tautology;

two atoms:
  absorbed by LocalSurvivor/SAE witnesses.
```

因此当前没有已物化的非二点 primitive PDEC 候选。这个结论不关闭全局 `PDEC family`；它只固定
未来候选的准入门槛：同一 formal unit、去重后三个以上物理 primitive 原子、非二点 tautology、
非 cross-q 图重叠，并且未被 SAE/Endpoint witness 吸收。

继续接入总路由器后，`NonTautologicalPDECOrNCBLK` 已不再是最新终点。`NC-BLK` 被边界核查吸收或
外部化，当前已物化 PDEC 候选数为零，LocalSurvivor 已物化包也为零。因此最新前沿为：

```text
CurrentMaterializedFrontierExhausted_GlobalTerminalFamiliesOpen。
```

新增：

```text
experiments/prime_matrix_global_terminal_family_boundary_router.py
docs/monograph/prime-matrix-global-terminal-family-boundary-router.md/json
```

该路由器给出新的边界审查：

```text
materialized_frontier_exhausted=true；
terminal_generation_contract_closed=true；
current_terminal_instances_exhausted=true；
global_terminal_family_exclusion_closed=false；
row_column_unconditional_closed=false；
narrowest_next_hardpoint=GlobalTerminalFamilyExclusionCertificates。
```

这一步的结构意义是：当前机器总账能触及的局部终端样本已经耗尽；继续攻关不能再回到优化
`ell=199`、二点 Fourier 阈值、无名孤窗或旧 `NC-BLK` 标签。真正剩余是全局家族定理：

```text
每个未来最小反例产生的终端对象，
必须被 PDEC-family exclusion、
LocalSurvivor witness/deficit certificate、
CleanKLS/DLS internal large-sieve certificate，
或明确外部/referee 输入吸收。
```

该结论仍不是完整行/列无条件定理；它关闭的是“当前已物化前沿还有可局部消元对象”的可能，
并把唯一剩余固定为全局终端家族全集排斥。

进一步新增：

```text
experiments/prime_matrix_global_terminal_family_exclusion_split_router.py
docs/monograph/prime-matrix-global-terminal-family-exclusion-split-router.md/json
```

这个拆分路由器把 `GlobalTerminalFamilyExclusionCertificates` 再压成更小的终局门：

```text
closed_nonfinal_reductions=true；
open_final_gates=[
  PDEC_CAP,
  KLS_EXT_OR_INTERNAL_LARGE_SIEVE,
  DStructureRankinReferee
]；
narrowest_next_hardpoint=PDEC_CAP_OR_KLS_EXT_OR_REFEREE；
self_contained_next_hardpoint=PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve。
```

其中已经关闭的非终局门包括：

```text
当前已物化前沿耗尽；
终端三证书无第四出口；
LocalSurvivor 当前包与已知入口不再构成独立全局阻塞；
连续终端二分：正 limsup 有限签名 -> PDEC-CAP，
               有限签名消散 -> CleanKLS/DLS；
NC-BLK 不再构成独立内部终端。
```

再进一步新增：

```text
experiments/prime_matrix_self_contained_terminal_bottleneck_router.py
docs/monograph/prime-matrix-self-contained-terminal-bottleneck-router.md/json
```

该路由器把完全自足路线中的 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve` 再收缩一层：

```text
closed_nonfinal_reductions=true；
internal_clean_kls_independent_blocker_collapsed=true；
self_contained_terminal_bottleneck_is_pdec_cap=true；
open_final_gates=[
  PDEC_CAP_SameSetGlobalDualCertificate,
  DStructureRankinReferee
]；
narrowest_self_contained_hardpoint=PDEC_CAP_SameSetGlobalDualCertificate。
```

结构含义是：在当前 canonical-source 自足边界内，内部 `CleanKLS` 不再是平行独立黑箱。
若 clean large-sieve 失败，它输出对偶集中对象并回流 `PDEC/SAE`；
若处在 canonical NC-BLK/CleanKLS 分支，它已被 same-set capacity 边界吸收；
若要求 unrestricted generic full-S WFD，则该命题已被 moving-delta no-go 反证隔离。
所以完全自足路线的唯一独立数学硬点现在是同一坏窗集合上的全局 PDEC 容量对偶证书
`U_CRT<L_PDEC`；完整行/列无条件定理仍需单独通过 D-structure/Tail-log4/finite Rankin
referee 晋级门。

继续新增：

```text
experiments/prime_matrix_pdec_cap_same_set_global_dual_router.py
docs/monograph/prime-matrix-pdec-cap-same-set-global-dual-router.md/json
```

该路由器进入 `PDEC_CAP_SameSetGlobalDualCertificate` 内部，确认当前已物化 PDEC 中间门全部接线：

```text
closed_current_materialized_pdec_gates=true；
canonical_source_self_contained_pdec_cap_closed=true；
pdec_cap_same_set_global_dual_closed=false；
open_final_gates=[
  DIBFIQuantifiedNoProjectionWindowCertificate
]；
narrowest_next_hardpoint=
  DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY。
```

结构含义是：当前 PDEC-CAP 已不再是“寻找固定 `Q` Fourier 常数”的问题。现有 DualCap
都有同一 `M_Q` 质量来源并关闭早期 `P` 行出口；PersistentCap 已进入晋升删除势或
NoDeletion-KL/PDEC/CleanKLS；ForcedCap 已进入多桶 ActualPaymentStitching。新增
`prime-matrix-profinite-actual-payment-stitching-router.md/json` 后，真实支付图 `Gamma_n`
的投影塔二分也已闭合：若某有限候选签名正 limsup 持久，则进入多桶同集 `PDEC` 对偶比较；
若所有有限签名都不持久，则进入分散 `CleanKLS/DLS` 输入，或由 FiberDeletion /
NoDeletion-KL 回流剥离。

继续新增：

```text
experiments/prime_matrix_pdec_cap_diffuse_terminal_split_router.py
docs/monograph/prime-matrix-pdec-cap-diffuse-terminal-split-router.md/json
```

该路由器进一步压缩不持久 `Gamma` 分支：

```text
diffuse_terminal_split_closed=true；
self_contained_diffuse_terminal_closed=false；
open_final_gates=[
  FixedShellLowModPersistencePDECOrColumnCRT,
  SelfContainedKuznetsovLSAtomSC9
]；
narrowest_diffuse_hardpoint=
  FixedShellLowModPersistencePDECOrColumnCRT_OR_SelfContainedKuznetsovLSAtomSC9。
```

结构含义是：`FiberDeletion/NoDeletion-KL/CleanKLS` 不再是宽口径未命名剩余。持续删除必须支付全局删除势；
删除停止时 KL/互信息偏斜回流 refined/new-layer `PDEC`；只有 KL/互信息平坦才进入 `CleanKLS/DLS`，
而 `CleanKLS` 的 K1--K9 admission 失败项全部回流 `PDEC/SAE/Multiplicity/Promotion`。外部深定理版
可在明确引用窗口化 KLS/DI/BFI/Kuznetsov 输入时吸收 flat clean 分支；完全自足版仍剩命名原子 `SC-9`。

继续新增：

```text
experiments/prime_matrix_pdec_cap_deletion_support_exhaustion_bridge.py
docs/monograph/prime-matrix-pdec-cap-deletion-support-exhaustion-bridge.md/json
```

该桥接关闭了删除势发散后的后半段：

```text
deletion_support_exhaustion_bridge_closed=true；
global_deletion_divergence_closed=false；
narrowest_deletion_hardpoint=GlobalDeletionPotentialDivergenceLowerBound。
```

结构含义是：同源投影塔乘法公式给出 `sum -log a_n=infinity => density(A_QN)->0`；
actual-payment 账本给出正需求责任。二者不能继续作为 diffuse 正责任终端共存：若责任被耗尽，则删除侧闭合；
若剩余质量集中或稀疏化，则回流已命名 `LocalSurvivor/SAE/PDEC/ColumnCRT/CleanKLS` 入口。因此删除侧真正还要证明的只剩
全局删除势发散下界。

继续新增：

```text
experiments/prime_matrix_pdec_cap_deletion_divergence_lower_bound_router.py
docs/monograph/prime-matrix-pdec-cap-deletion-divergence-lower-bound-router.md/json
```

该路由器把全局删除势发散下界继续压缩：

```text
deletion_divergence_lower_bound_reduced=true；
global_deletion_divergence_closed=false；
narrowest_deletion_hardpoint=OccupancySaturationPDECOrColumnCRT。
```

结构含义是：HRO 引理给出 `S_t subset Occ_t union TI_t`。若删除势不发散，则在某个正质量子列上
`Occ/r+TI/r->1`；其中 `TI/r->1` 已是 promoted prime 非必要，并回流 NoDeletion-KL/CleanKLS。
所以删除侧唯一新剩余是 `OccupancySaturation`：旧洞 residue 在新增素数层近满占用必须触发容量/PDEC/ColumnCRT。

继续新增：

```text
experiments/prime_matrix_pdec_cap_occupancy_saturation_kernel_router.py
docs/monograph/prime-matrix-pdec-cap-occupancy-saturation-kernel-router.md/json
```

该路由器用 HRO 注入界继续压缩占位饱和：

```text
occupancy_saturation_reduced_to_dense_kernel=true；
occupancy_saturation_closed=false；
narrowest_occupancy_hardpoint=DenseOldHoleKernelCapacityPDECOrColumnCRT。
```

结构含义是：`|Occ_t| <= min(|H_Q(t)|,r)`，所以旧洞稀疏或 residue 不满时，占位饱和自动失败并给出删除缺口。
若占位仍近满，则必须存在近满旧洞选择核；也就是几乎每个 promoted residue 都能选到一个同时避开全部低层同余禁类的旧洞列。
因此删除侧硬点从宽口径 `OccupancySaturationPDECOrColumnCRT` 压成
`DenseOldHoleKernelCapacityPDECOrColumnCRT`。

继续新增：

```text
experiments/prime_matrix_pdec_cap_dense_kernel_common_variable_router.py
docs/monograph/prime-matrix-pdec-cap-dense-kernel-common-variable-router.md/json
```

该路由器把稠密旧洞核写成共同变量表：

```text
dense_kernel_no_unnamed_escape_closed=true；
dense_kernel_exclusion_closed=false；
narrowest_dense_kernel_hardpoint=
  FixedShellLowModPersistencePDECOrColumnCRT_OR_SelfContainedKuznetsovLSAtomSC9。
```

结构含义是：对近满 occupied residue 选择列 `c_b`，写成 `c_b=rho_b+r k_b`。
其中 `rho_b` 由 promoted prime 的仿射方程唯一决定；所有旧素数 `q|Q` 的禁类都变成
同一个壳号变量 `k_b` 上的一条线性禁止残基。于是无合法壳号是容量/Hall 删除；固定壳或有限壳包正密度
是低模持久 `PDEC/ColumnCRT`；无固定壳持久就是多壳分散，非平坦频率回 `PDEC/ColumnCRT`，
平坦频率进入自足 `SC-9`。这关闭的是稠密旧洞核的无名逃逸，不是终端排斥。

继续新增：

```text
experiments/prime_matrix_pdec_cap_persistent_signature_unification_router.py
docs/monograph/prime-matrix-pdec-cap-persistent-signature-unification-router.md/json
```

该路由器把持久 `Gamma` 的多桶 MFU 与固定壳低模持久统一为同一类对象：

```text
persistent_signature_unification_closed=true；
narrowest_next_hardpoint=
  PersistentFiniteSignaturePDECColumnCRT_OR_SelfContainedKuznetsovLSAtomSC9。
```

结构含义是：二者都只是同一个 formal unit 上的有限签名正密度。MFU 侧的有限签名是
phase-bucket/tail-column formal unit；固定壳侧的有限签名是 shell/displacement formal unit。
`ColumnCRT` 位移已吸收到 displacement PDEC，PDEC 对偶失败已吸收到 cap refinement，口径不一致
已由 Multiplicity-Stitching 吸收到 weighted/primitive PDEC 或复用缺陷。因此这两个持久类分支
不能再作为平行硬点保留。

此阶段的真实硬点不是“继续找一个未命名终端”，而是先压成更窄的二选一解析终端：

```text
PersistentFiniteSignaturePDECColumnCRT:
  证明所有持久有限签名 formal unit 的 PDEC/ColumnCRT 对偶容量排斥；

Referee promotion:
  D-structure/Tail-log4/finite Rankin 接口被独立接受。
```

继续新增：

```text
experiments/prime_matrix_pdec_cap_sc9_boundary_reconciliation_router.py
docs/monograph/prime-matrix-pdec-cap-sc9-boundary-reconciliation-router.md/json
```

该路由器把 PDEC-CAP 终端里重新出现的 flat clean `SC-9` 与 canonical-source 边界调和：

```text
pdec_cap_sc9_boundary_reconciled=true；
narrowest_next_hardpoint=PersistentFiniteSignaturePDECColumnCRT。
```

结构含义是：`SC-9` 在此处只来自无持久有限签名后的 flat clean residual。clean 估计失败会输出对偶集中并回流
`PDEC/SAE`；进入 `SC-9` 后又已展开到 `NC-BLK` 或外部 DI/BFI；而 canonical `NC-BLK` 已由同集容量边界吸收，
generic WFD 分支不能纳入自足声明。因此在当前 canonical-source 完全自足 PDEC-CAP 边界内，`SC-9` 不再是独立终端阻塞。

继续新增：

```text
experiments/prime_matrix_pdec_cap_persistent_terminal_admission_router.py
docs/monograph/prime-matrix-pdec-cap-persistent-terminal-admission-router.md/json
```

该路由器继续把 `PersistentFiniteSignaturePDECColumnCRT` 压到准入门：

```text
persistent_terminal_admission_boundary_closed=true；
narrowest_next_hardpoint=PrimitiveMultiAtomSameFormalUnitPDECCertificate。
```

结构含义是：裸持久签名、裸列位移、PDEC 对偶失败和多重口径都不能直接作为终端。列位移先吸收为
displacement/primitive PDEC 或 SAE；对偶失败先输出 cap refinement、ColumnCRT、SAE 或口径义务；
多重拼接先规范化到同一 formal unit；二点 Fourier tautology 与当前 SAE/Endpoint 已吸收。因此真正准入的剩余对象只剩：

```text
PrimitiveMultiAtomSameFormalUnitPDECCertificate:
  same formal unit；
  去重后三个以上 physical primitive atoms；
  非二点 tautology；
  未被 LocalSurvivor/SAE/Endpoint 吸收；
  需要证明 U_CRT<L_PDEC。
```

继续新增：

```text
experiments/prime_matrix_pdec_cap_primitive_multiatom_rank_router.py
docs/monograph/prime-matrix-pdec-cap-primitive-multiatom-rank-router.md/json
```

该路由器把 `PrimitiveMultiAtomSameFormalUnitPDECCertificate` 继续拆成秩边界：

```text
primitive_multiatom_rank_boundary_closed=true；
current_materialized_primitive_multiatom_instances_closed=true；
narrowest_next_hardpoint=RankTwoCapStablePrimitivePDECKernelInequality。
```

结构含义是：准入后的 primitive 多原子对象还不能直接当作最终黑箱。零秩/一秩分支只能是
重复口径、二点 Fourier tautology、固定壳 `PDEC/ColumnCRT` 或 `SAE`；若某方向的
`U_CRT<L_PDEC` 失败，则必须先输出 cap，并按 `SAE/refined PDEC/ColumnCRT/multiplicity`
回流；cap refinement 在固定签名群内无循环。因此当前真正剩余被进一步压成：

```text
RankTwoCapStablePrimitivePDECKernelInequality:
  对所有二秩以上、同 formal unit、且无可回流 cap 的 primitive PDEC 核，
  证明同一坏窗集合上的 U_CRT<L_PDEC。
```

继续新增：

```text
experiments/prime_matrix_pdec_cap_ranktwo_capstable_kernel_router.py
docs/monograph/prime-matrix-pdec-cap-ranktwo-capstable-kernel-router.md/json
```

该路由器把二秩 cap-stable 核不等式本身改写为 cap localization 的逆否命题：

```text
ranktwo_capstable_kernel_inequality_closed=true；
narrowest_next_hardpoint=UniformCapStabilityCertificateForRankTwoPrimitiveKernels。
```

结构含义是：若某方向的 `U_CRT` 达到 `L_PDEC`，帽定位给出质量至少
`(L_PDEC-alpha M)/(1-alpha)` 的方向帽；该帽若稀疏则进 `SAE`，若持久则进 refined
`PDEC/ColumnCRT`，若口径不一致则进 multiplicity 规范化。因此真正留在 cap-stable 核内的对象，
必须所有合法方向帽都低于阈值。

继续新增：

```text
experiments/prime_matrix_pdec_cap_uniform_cap_finite_basis_router.py
docs/monograph/prime-matrix-pdec-cap-uniform-cap-finite-basis-router.md/json
```

该路由器把统一帽稳定的连续方向族压成有限基：

```text
uniform_cap_finite_basis_closed=true；
narrowest_next_hardpoint=FiniteCyclicArcCapMassBoundsForRankTwoPrimitiveKernels。
```

结构含义是：固定 finite formal unit 后，非平凡字符像是有限循环集，任意方向帽都是该有限循环集上
某个弧的预像；`zeta/alpha` 的连续变化只会在有限端点处改变 cap 集合。因此统一帽稳定不再是连续参数
搜索，而是有限循环弧 cap 质量界全集。

继续新增：

```text
experiments/prime_matrix_pdec_cap_finite_arc_transverse_router.py
docs/monograph/prime-matrix-pdec-cap-finite-arc-transverse-router.md/json
```

该路由器把有限循环弧 cap 质量界继续拆成横向结构：

```text
finite_arc_no_unnamed_exit_closed=true；
narrowest_next_hardpoint=TransverseFiberExpansionForFiniteArcCaps。
```

结构含义是：有限字符弧是秩一薄片。若高质量弧只有低横向支撑，则进入
`SAE/ColumnCRT/固定壳PDEC/Hall deletion`；若横向偏斜持久，则把弧指标并入签名并进入
refined `PDEC`；若横向平坦分散，则进入 `CleanKLS/DLS` 或外部大筛输入。因此当前真正剩余是：

```text
TransverseFiberExpansionForFiniteArcCaps:
  对每个高质量有限字符弧，证明弧内横向纤维无法同时保持
  primitive 二秩、同 formal unit、cap-stable 和足够质量；
  若证明失败，必须输出 SAE / refined PDEC / ColumnCRT / CleanKLS 回流证书。
```

继续新增：

```text
experiments/prime_matrix_pdec_cap_transverse_clean_reduction_router.py
docs/monograph/prime-matrix-pdec-cap-transverse-clean-reduction-router.md/json
```

该路由器把横向纤维扩张进一步压成横向商 clean 大筛原子：

```text
transverse_expansion_reduced_to_clean_atom=true；
narrowest_next_hardpoint=TransverseQuotientCleanLargeSieveAtom。
```

结构含义是：有限字符弧只固定一个字符方向；二秩以上 primitive 核在弧内仍留下横向商变量。
横向低支撑、横向持久偏斜、横向列/壳集中已经分别回流 `SAE/refined PDEC/ColumnCRT`。
若这些非平坦横向缺陷都不存在，剩余就是横向商上的 `L2-flat clean residual`，必须进入
内部 `LargeSieve/DLS/KLS` 证明或明确外部 KLS/DI/BFI/Kuznetsov 输入。因此当前真正剩余是：

```text
TransverseQuotientCleanLargeSieveAtom:
  证明高质量有限弧的横向商在 K1--K9 clean admission 后满足内部大筛界；
  或明确登记外部输入；
  若任一 clean admission 失败，则回流 PDEC / SAE / ColumnCRT / Multiplicity。
```

继续新增：

```text
experiments/prime_matrix_pdec_cap_transverse_clean_atom_frontier_router.py
docs/monograph/prime-matrix-pdec-cap-transverse-clean-atom-frontier-router.md/json
```

该路由器把横向商 clean 大筛原子接入既有 A1 `CleanKLS/SC-9` 前沿：

```text
transverse_clean_atom_routed_to_named_frontier=true；
narrowest_next_hardpoint=
  TransverseSourceSupportNonconcentrationCertificate_OR_DIBFIQuantifiedNoProjectionWindowCertificate。
```

结构含义是：横向商 residual 通过 K1--K9 clean admission 后不是第四出口，而是进入已登记的
`SC-9` 前沿；`SC-9` 已展开为实际系数 `NC-BLK` 或外部 `DI/BFI`。自足路线不能直接调用
canonical-source 吸收，除非先证明横向商系数继承 canonical `RIW/Buchstab` 源支撑下界，或直接证明
实际 transverse `NC-BLK` 块非集中。朴素 factor-residue incidence 桥已被内部 fiber 阻断。外部原始
`DI/BFI` 路线则仍需闭合无投影对象恒等式和量化尺度代入。

因此当前真正剩余被进一步改写为：

```text
TransverseSourceSupportNonconcentrationCertificate:
  canonical RIW/Buchstab 源支撑下界或实际 transverse NC-BLK；

DIBFIQuantifiedNoProjectionWindowCertificate:
  外部原始 DI/BFI 的无投影对象恒等式 + 量化尺度代入。
```

继续新增：

```text
experiments/prime_matrix_pdec_cap_transverse_source_support_router.py
docs/monograph/prime-matrix-pdec-cap-transverse-source-support-router.md/json
```

该路由器把 `TransverseSourceSupportNonconcentrationCertificate` 继续拆成来源嵌入、canonical 层转移、
直接 NC-BLK 三个严格自足对象：

```text
transverse_source_support_reduced=true；
narrowest_next_hardpoint=TransverseFormalUnitA1SourceEmbedding；
downstream_source_route_hardpoint=
  CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn；
direct_fallback_hardpoint=
  DirectTransverseNCBLKActualCoefficientNonConcentration。
```

结构含义是：A1/KZ-E actual-source provenance 账本已经闭合到 canonical `RIW/Buchstab`
pre-Cauchy 源；canonical RIW 支撑链又已压到 Buchstab 层支撑，而厚区间 squarefree 原始计数也已闭合。
当前真正缺的第一步不是再估计大筛，而是证明横向商 formal unit 是该 canonical 源的合法限制、商或条件化。
若嵌入成立，下游再攻 canonical 层准入、非零转移和薄区间回流；若嵌入不成立，则必须走直接 actual
transverse `NC-BLK` 或外部 `DI/BFI`。

继续新增：

```text
experiments/prime_matrix_pdec_cap_transverse_embedding_router.py
docs/monograph/prime-matrix-pdec-cap-transverse-embedding-router.md/json
```

该路由器用有限测度函子性闭合横向来源嵌入：

```text
transverse_formal_unit_embedding_closed=true；
narrowest_next_hardpoint=CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn。
```

actual payment 是 canonical 源测度的确定性 first-cover 推前，有限签名塔是有限投影，
方向弧是预像限制，横向商是有限因子/条件化，所以没有重新加权或替换系数源。

继续新增：

```text
experiments/prime_matrix_pdec_cap_canonical_layer_closure_router.py
docs/monograph/prime-matrix-pdec-cap-canonical-layer-closure-router.md/json
```

该路由器把最新自足硬点接回既有 A1 链条并闭合：

```text
canonical_layer_transfer_closed=true；
self_contained_canonical_branch_closed=true；
open_self_contained_gates=[]；
open_external_gates=[DIBFIQuantifiedNoProjectionWindowCertificate]。
```

结构含义是：一旦横向 formal unit 已嵌入 canonical 源，`CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn`
不再是新的横向估计，而是既有
`selector retention -> finite signature -> decision tree -> actual source provenance -> branch boundary`
链条；该链条已经由 canonical-source final boundary 吸收。剩余 `DIBFIQuantifiedNoProjectionWindowCertificate`
只属于 generic/external 原始 DI/BFI 路线，不能当作 canonical-source 自足路线的剩余。

这一步继续保持诚实边界：它关闭的是全局终端家族剩余中的“未命名或局部样本硬点”，不是完整行/列
无条件证明。

继续新增：

```text
experiments/prime_matrix_self_contained_pdec_cap_boundary_lift_router.py
docs/monograph/prime-matrix-self-contained-pdec-cap-boundary-lift-router.md/json
```

该路由器把 PDEC-CAP 的 canonical-source 闭合结论向上提升到自足终端瓶颈层：

```text
closed_nonfinal_lift_gates=true；
canonical_source_self_contained_pdec_bottleneck_closed=true；
pdec_cap_same_set_global_dual_closed=false；
generic_external_dibfi_boundary_open=true；
row_column_unconditional_closed=false；
narrowest_self_contained_boundary=
  NoFurtherCanonicalSourceSelfContainedPDECCapGap；
narrowest_global_next_hardpoint=
  GlobalTerminalFamilyPromotionReview_OR_DStructureRankinReferee。
```

结构含义是：旧的 `PDEC_CAP_SameSetGlobalDualCertificate` 已不再是 canonical-source 自足分支的
开门；它已经由横向来源嵌入、canonical 层转移和既有 A1 来源边界闭合。剩余的
`DIBFIQuantifiedNoProjectionWindowCertificate` 只属于 generic/external 原始 `DI/BFI` 路线。
完整行/列无条件命题仍需全局终端家族晋级审查与 `DStructureRankinReferee`，不能由这次
PDEC-CAP 自足边界提升替代。

继续新增：

```text
experiments/prime_matrix_canonical_terminal_promotion_closure_router.py
docs/monograph/prime-matrix-canonical-terminal-promotion-closure-router.md/json
```

该路由器复核最新自足硬点，并把上层旧拆分中的 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve`
按最新边界重新分类：

```text
latest_self_contained_hardpoint_closed=true；
canonical_source_terminal_promotion_closed=true；
canonical_source_self_contained_boundary_closed=true；
open_self_contained_gates=[]；
open_external_gates=[
  DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY
]；
open_final_gates=[
  DStructureRankinRefereeStillOpen
]；
row_column_unconditional_closed=false；
narrowest_self_contained_boundary=
  NoFurtherCanonicalSourceTerminalPromotionGap；
narrowest_global_next_hardpoint=
  DStructureRankinReferee_FOR_FINAL_PROMOTION。
```

结构含义是：在 canonical `RIW/Buchstab` 来源分支内，终端晋级已经没有新的自足数学开门。
当前已物化终端前沿耗尽，三终端无第四出口，PDEC-CAP 由边界提升闭合，canonical
`CleanKLS/NC-BLK` 被吸收或回流 `PDEC/SAE`。这完成的是 canonical-source 自足终端晋级边界，
不是 unrestricted/global 终端家族排斥定理，也不是完整行/列无条件命题。外部/generic
`DI/BFI` 与最终 `DStructureRankinReferee` 仍在该闭合边界之外。

继续新增：

```text
experiments/prime_matrix_canonical_source_self_contained_final_theorem_router.py
docs/monograph/prime-matrix-canonical-source-self-contained-final-theorem-router.md/json
```

该路由器生成最终自足命题边界闭合证书：

```text
canonical_source_self_contained_theorem_closed=true；
open_self_contained_gates=[]；
terminal_boundary=
  NoFurtherCanonicalSourceSelfContainedTheoremBoundaryGap；
open_external_gates=[
  DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY
]；
open_final_promotion_gates=[
  DStructureRankinRefereeStillOpen
]；
row_column_unconditional_closed=false。
```

最终可声明的自足命题是：

```text
Prime Matrix canonical-source terminal theorem boundary:
  Triad-A1 same-set/full-S terminal plus canonical terminal promotion
  on the canonical RIW/Buchstab source branch.
```

不声明的命题仍是：

```text
Unrestricted generic full-S well-factorable WFD self-contained theorem；
Unrestricted/global Prime Matrix row-column unconditional theorem。
```

因此，当前“自足闭合”已经完成到精确命题边界：
`NoFurtherCanonicalSourceSelfContainedTheoremBoundaryGap`。完整无条件行/列命题的最终升级仍需外部/独立
审稿输入，不能由该自足边界证书替代。

继续新增：

```text
experiments/prime_matrix_global_unconditional_self_contained_obstruction_router.py
docs/monograph/prime-matrix-global-unconditional-self-contained-obstruction-router.md/json
```

该路由器专门回答“完整全局无条件行命题能否由当前材料自足闭合”：

```text
canonical_source_self_contained_theorem_closed=true；
current_corpus_global_unconditional_self_contained_closure_possible=false；
row_column_unconditional_closed=false。
```

阻断门为：

```text
UnrestrictedGenericWFD；
ActualFullSSourceBridge；
FullSNonAPStrengthenedSourceAntiAtom；
DIBFIQuantifiedNoProjectionWindowCertificate；
DStructureTailLog4FiniteRankinPromotion。
```

其中 `UnrestrictedGenericWFD` 不是普通缺口，而是已被 moving-delta no-go 反证的过强路线。
若要越过当前自足边界，必须新增下列输入之一组：

```text
ActualA1FullSSourceLockTheorem_OR_FullSNonAPStrengthenedSourceAntiAtom；
NoProjectionUncenteredDispersionIdentity；
QuantifiedDIBFIWindowSubstitution；
DStructureTailLog4FiniteRankinIndependentAcceptance。
```

因此，完整全局无条件自足版目前不能从当前材料直接闭合；当前可闭合且已闭合的是
canonical-source 精确自足命题。

继续新增：

```text
experiments/prime_matrix_actual_source_bridge_global_reconciliation_router.py
docs/monograph/prime-matrix-actual-source-bridge-global-reconciliation-router.md/json
```

该路由器把旧阻断门 `ActualFullSSourceBridge` 与已经闭合的 actual-source 来源账本重新调和：

```text
actual_source_bridge_closed_for_canonical_branch=true；
actual_source_bridge_closes_global_unrestricted=false；
old_blocker_superseded=ActualFullSSourceBridge；
updated_global_blocking_gates=[
  UnrestrictedGenericWFD,
  NoncanonicalFullSComplementAntiAtomOrExternalDIBFI,
  FullSNonAPStrengthenedSourceAntiAtom,
  DIBFIQuantifiedNoProjectionWindowCertificate,
  DStructureTailLog4FiniteRankinPromotion
]。
```

结构含义是：actual-source bridge 已经在 canonical `RIW/Buchstab` 来源分支内被来源账本、
source-lock 分支拆分和最终自足定理边界吸收；它不再是 canonical-source 自足命题的开门。
但该闭合只覆盖 canonical 分支，不能偷渡到 unrestricted/global 补集。旧的宽阻断名
`ActualFullSSourceBridge` 因此应替换为更精确的
`NoncanonicalFullSComplementAntiAtomOrExternalDIBFI`：若要闭合完整全局版，仍必须证明
noncanonical full-`S` 补集的强化反原子，或提交外部/量化 DI/BFI 无投影证书。完整行/列
无条件定理仍未由当前材料闭合。

继续新增：

```text
experiments/prime_matrix_noncanonical_complement_input_contract_router.py
docs/monograph/prime-matrix-noncanonical-complement-input-contract-router.md/json
```

该路由器把 noncanonical full-`S` 补集的“必要输入边界”固定为：

```text
contract_boundary_closed=true；
canonical_branch_removed_from_remainder=true；
generic_wfd_template_available=false；
noncanonical_complement_closed_by_current_corpus=false；
row_column_unconditional_closed=false。
```

因此当前已经闭合的是输入合同判定，而不是这些输入本身。可继续硬攻的输入族只剩：

```text
ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab；
FullSNonAPStrengthenedSourceAntiAtomForActualSource；
NoProjectionUncenteredDispersionIdentity；
QuantifiedDIBFIWindowSubstitution；
DStructureTailLog4FiniteRankinIndependentAcceptance。
```

结构含义是：在扣除 canonical 分支后，剩余 full-`S` 问题不能再被表述为 generic WFD
自足引理；该模板已被 moving-delta 模型反证。当前材料下没有第四条可自足偷渡路线：
要么证明实际源恒等，要么证明实际源强化反原子，要么提交外部/量化 `DI/BFI`，最终还要通过
`DStructure/Rankin` 晋级门。

继续新增：

```text
experiments/prime_matrix_noncanonical_complement_trilemma_router.py
docs/monograph/prime-matrix-noncanonical-complement-trilemma-router.md/json
```

该路由器把第二包进一步收束为三歧边界：

```text
trilemma_boundary_closed=true；
self_contained_noncanonical_package_closed=false；
external_contract_package_closed_if_fulls_kls_ext_accepted=true。
```

三种合法闭合模式为：

```text
实际源恒等；
强化实际源反原子；
接受或证明 FullS-KLS-ext / FullSNonAPWFDKLSTheoremInput。
```

其中 generic full-S 自足反原子已被 moving-delta capacity 反例排除，不能再由 formal WFD、
Type/Fourier、K4/K6 或朴素 incidence 修复。外部定理合同版在接受 `FullS-KLS-ext` 时闭合
scale/object/no-projection，但若坚持完全自足或逐页原文核验，仍需
`DIBFIPrimarySourceSpecializationProof`。因此第二包的边界闭合了，输入本身仍是条件性的。

继续新增：

```text
experiments/prime_matrix_closure_input_atlas_router.py
docs/monograph/prime-matrix-closure-input-atlas-router.md/json
```

该图谱把此前全部主要思路统一成输入基：

```text
canonical_source_self_contained_closed=true；
noncanonical_input_contract_closed=true；
row_column_unconditional_closed=false。
```

模型回顾结论是：

```text
Full CRT/MinRep、方阵斜线/圆柱覆盖、第 P 列锚点、层叠轮筛、
远尾互补因子、SN 递归剥离、命名出口吸收、PDEC cap 细化
=> 终端证书包；

Triad-A1 canonical-source 分支
=> 已闭合；

noncanonical full-S 补集
=> 必要输入边界已闭合，但输入本身仍开。
```

因此完整全局行/列无条件闭合的最小输入基固定为三包：

```text
TerminalCertificatePackage:
  SAE-Cert；
  PDEC-Cert with U_CRT<L_PDEC；
  ColumnCRT-Cert or return to PDEC/SAE；
  CleanMultishellKLS；
  TotalDescent to p=2 or first-seam absorption；

NoncanonicalFullSComplementPackage:
  actual full-S non-AP source equals canonical RIW/Buchstab；
  or strengthened anti-atom for actual noncanonical source；
  or quantified no-projection DI/BFI route；

DStructureRankinPromotionPackage:
  D-structure/Tail-log4/finite Rankin 晋级门通过。
```

这份图谱说明继续突破不应再寻找新无名分支或固定常数，而应逐项证明这三包。

继续新增：

```text
experiments/prime_matrix_dstructure_rankin_promotion_acceptance_router.py
docs/monograph/prime-matrix-dstructure-rankin-promotion-acceptance-router.md/json
```

该路由器把第三包固定为最终晋级验收包：

```text
promotion_package_boundary_closed=true；
promotion_package_independently_accepted=false；
row_column_unconditional_closed=false；
rankin_sample_pass=true。
```

边界含义是：D-structure/Tail-log4/finite Rankin 不再是无名终端，而是明确的 referee
promotion gate。Rankin 账本已经有可验收证书格式，样本 `core_count_exact=39`、
`allowed_budget=40.0` 且 Rankin/exact 均通过；但这只证明格式可复核，不等于正式全集已提交。
完整晋级仍需：

```text
D-structure / Structured-EHPD 入口与归约被独立接受；
Tail-log4 的 BG/RKS 定理号与适配审计被接受；
有限验证归档与脚本 hash 可复现；
全部正式着色走廊 Rankin 证书通过，或失败者回流 PDEC/SAE；
作者侧 BLOCK-REFEREE 只能由独立审稿接受后升级。
```

因此第三包的验收边界已经闭合，但第三包尚未被当前材料独立接受。

继续新增：

```text
experiments/prime_matrix_terminal_certificate_package_compression_router.py
docs/monograph/prime-matrix-terminal-certificate-package-compression-router.md/json
```

该路由器先补第一包的结构压缩：

```text
terminal_package_compression_closed=true；
terminal_package_fully_proved=false；
row_column_unconditional_closed=false。
```

压缩后的结论是：

```text
NoUnnamedEscape:
  已闭合为命名出口；

NamedExitAbsorption:
  已闭合为证书接口；

CleanMultishellKLS:
  canonical-source 分支已由最终边界吸收；
  noncanonical/generic 分支移入 NoncanonicalFullSComplementPackage 或外部 KLS；

TotalDescent:
  正式下降路径存在则到 p=2；
  不存在则首个 grid-fail seam 已材料化为 PDEC/ColumnCRT/SAE。
```

因此 `TerminalCertificatePackage` 不再有五个平行独立输入；真正剩余只有：

```text
Global SAE finite/window certificate family；
PDEC-Dual/Explicit certificates for all persistent families；
ColumnCRT exclusion or PDEC/SAE return certificates。
```

这一步补齐的是第一包的结构压缩，不是三类证书族本身的排斥。

继续新增：

```text
experiments/prime_matrix_columncrt_to_pdec_sae_absorption_router.py
docs/monograph/prime-matrix-columncrt-to-pdec-sae-absorption-router.md/json
```

该路由器把 `ColumnCRT` 从独立终端中删除：

```text
columncrt_independent_terminal_removed=true；
terminal_package_fully_proved=false；
row_column_unconditional_closed=false。
```

理由是：

```text
persistent nonzero displacement overload
  => displacement PDEC on enlarged finite signature；

sparse displacement overload
  => SAE/endpoint；

balanced displacement load
  => admissible PDEC-dual constraint row。
```

`RPZ` 的 unit endpoint gate 说明固定非零位移入口是真实结构，并且阈值调小不能直接排斥；
但这不使它成为第三类独立终端。它只说明必须走 endpoint/displacement `PDEC` 或 `SAE`。
因此第一包的独立剩余进一步压成：

```text
Global SAE finite/window/local-survivor certificate family；
PDEC family including displacement/endpoint/cofactor/primitive certificates。
```

继续新增：

```text
experiments/prime_matrix_sae_to_local_survivor_pdec_absorption_router.py
docs/monograph/prime-matrix-sae-to-local-survivor-pdec-absorption-router.md/json
```

该路由器把 `SAE` 从独立终端中删除：

```text
sae_independent_terminal_removed=true；
terminal_package_fully_proved=false；
row_column_unconditional_closed=false。
```

证明边界是：

```text
sparse/single-window escape
  => finite LocalSurvivor packet with witness or blocker-deficit；
  or persistent finite signature => PDEC/ColumnCRT/TailAnchor/CofactorAnchor；
  or layer escape => CleanKLS/DLS admission / external input。
```

当前已物化 `LocalSurvivor/SAE` 包清零，已知入口 extractor 覆盖清零，`NewSparseEntryAdmission`
审计也没有发现无名 sparse 入口。因此 `SAE` 不再是第一包的独立终端；第一包的核心剩余压成
广义 `PDEC` 证书族，以及未来若新增显式 sparse 路线时必须附带的 extractor schema 义务。
这仍不是第一包全证明，更不是完整行/列无条件闭合。

继续新增：

```text
experiments/prime_matrix_pdec_family_explicit_input_boundary_router.py
docs/monograph/prime-matrix-pdec-family-explicit-input-boundary-router.md/json
```

该路由器把广义 `PDEC family` 也从泛称终端压成显式输入边界：

```text
pdec_family_explicit_input_boundary_closed=true；
current_materialized_pdec_frontier_closed=true；
canonical_source_pdec_cap_closed=true；
global_pdec_family_unconditional_closed=false。
```

结构含义是：当前已物化合法非二点 primitive `PDEC` 候选为零；canonical-source `PDEC-CAP`
已经经横向来源嵌入和 canonical 层转移接回最终自足边界；每个低秩、重复、二点、
ColumnCRT、sparse、cap 失败或 clean 残差都有命名回流。未来若出现新的 `PDEC` 障碍，
必须显式提交：

```text
同一个 formal unit，且只有一个固定 phase map；
全部去重后至少三个物理 primitive 原子；
不是二点 Fourier tautology；
不是尚未吸收的 ColumnCRT/displacement；
商去 shell/column 退化后秩至少为 2；
对每个有限循环弧 localization 都 cap-stable；
横向支撑既非 sparse，也非持久偏斜，也未进入 clean 外部化。
```

因此第一包当前边界进一步写成：

```text
FutureExplicitPrimitivePDECSchema；
FutureExplicitSparsePacketExtractorSchema。
```

这仍不是全局 PDEC family 无条件排斥；它说明当前材料没有剩余已物化 PDEC 终端，未来 PDEC
必须作为显式新 schema 输入。

继续新增：

```text
experiments/prime_matrix_future_sparse_packet_extractor_schema_boundary_router.py
docs/monograph/prime-matrix-future-sparse-packet-extractor-schema-boundary-router.md/json
```

该路由器把 `FutureExplicitSparsePacketExtractorSchema` 也从提示性卫生规则固定成准入边界：

```text
future_sparse_packet_schema_boundary_closed=true；
current_materialized_sparse_frontier_closed=true；
global_sparse_family_unconditional_closed=false；
row_column_unconditional_closed=false。
```

结构含义是：当前机器物化的 `LocalSurvivor/SAE` 包没有开放局部义务；已知 sparse 入口都有脚本
extractor 或合同回流；当前合同体系内没有额外无名 sparse 入口；`SAE` 已不再是独立第三终端。
未来若新增 sparse 路线，必须显式提交：

```text
source class；
有限窗口或固定偏移纤维 I；
候选集合 C(I)；
blocker 家族及其命中投影；
witness 或严格 blocker-deficit；
phase_key/window_shape/formal_unit_id 与去重规则；
有限签名持久性测试；
层级逃逸测试；
可复现脚本、JSON 字段、范围、哈希和 open_obligation_count=0；
与既有 PDEC/ColumnCRT/LocalSurvivor/CleanKLS 路由的排他性或回流关系。
```

不给该 schema 的 sparse 说法不能作为终端；若同签名持久复现则进入 `PDEC/ColumnCRT/Tail/Cofactor`
schema，若有限包升层逃逸则进入 `CleanKLS/DLS` 或显式外部大筛输入。至此第一包的当前已物化前沿
清零，并且两个未来输入都被约束成显式 schema 边界；这仍不是完整行/列无条件闭合。

继续新增：

```text
experiments/prime_matrix_final_input_firewall_boundary_router.py
docs/monograph/prime-matrix-final-input-firewall-boundary-router.md/json
```

该路由器把当前全部剩余合成最终输入防火墙：

```text
final_input_firewall_boundary_closed=true；
current_materialized_terminal_frontier_closed=true；
no_hidden_terminal_remaining=true；
all_final_inputs_independently_accepted=false；
row_column_unconditional_closed=false。
```

防火墙的含义是：当前材料没有剩余已物化 `PDEC` 或 sparse/`LocalSurvivor` 终端，noncanonical 分支
和 `DStructure/Rankin` 晋级门也已命名；因此剩余不能再作为无名终端或口头硬点进入。最终开放输入
只剩：

```text
FutureExplicitPrimitivePDECSchema；
FutureExplicitSparsePacketExtractorSchema；
NoncanonicalFullSComplementTrilemma；
DStructureRankinPromotion。
```

这一步闭合的是边界和命名性，不是完整无条件定理。完整行/列命题要升级，还必须证明或独立接受这些
显式输入。

继续新增：

```text
experiments/prime_matrix_four_open_inputs_closure_attack_router.py
docs/monograph/prime-matrix-four-open-inputs-closure-attack-router.md/json
```

该路由器逐项硬攻四类最终输入：

```text
current_materialized_frontier_zero=true；
no_hidden_terminal_remaining=true；
conditional_closure_chain_complete=true；
all_current_obligations_closed=false；
unconditional_closure_possible_from_current_corpus=false。
```

细化结论是：

```text
FutureExplicitPrimitivePDECSchema      当前无已物化义务，只在未来新增 PDEC family 时触发；
FutureExplicitSparsePacketExtractorSchema 当前无已物化义务，只在未来新增 sparse route 时触发；
NoncanonicalFullSComplementTrilemma    当前真实开放，现有 DI/BFI 主来源不足以推出所需 full-S non-AP WFD KLS；
DStructureRankinPromotion              当前真实开放，需独立接受晋级包。
```

因此形成条件闭合定理：若未来 `PDEC/sparse` 新路线均按 schema 消解或没有新增，且 noncanonical 三歧
至少一支被证明/接受，且 `DStructureRankinPromotion` 被独立接受，则无隐藏终端链可升级为完整闭合。
同时形成当前材料不可能性定理：没有 `FullSNonAPWFDKLSTheoremInput/APSourceLift/强化实际源反原子`
和 `DStructureRankinPromotion` 独立接受时，当前材料不能诚实推出完整行/列无条件定理。

继续新增：

```text
experiments/prime_matrix_noncanonical_final_narrowing_router.py
docs/monograph/prime-matrix-noncanonical-final-narrowing-router.md/json
```

该路由器把 noncanonical 三歧继续压成两项真实输入：

```text
noncanonical_narrowing_boundary_closed=true；
ap_source_lift_rejected=true；
generic_self_contained_antiatom_refuted=true；
exact_source_entropy_closed=false；
external_full_s_contract_closed_if_accepted=true；
self_contained_noncanonical_closed=false。
```

结构含义是：canonical 分支已经由实际源头调和移出；`APSourceLift` 被 AP/non-AP 分支定义、
对象账本和 SOURCE-CEN/BD-CEN 阻断；generic 自足反原子被 moving-delta 容量模型反证；
支撑+容量兼容已精确压成 source capacity measure 无 moving atom。最终只剩：

```text
InternalNewTheorem:
  prove ExactWFDSourceEntropy / FullSNonAPStrengthenedSourceAntiAtom for the actual source；

ExternalDeepInput:
  accept or prove FullSNonAPWFDKLSTheoremInput。
```

这一步进一步删除了 `APSourceLift` 和 generic 反原子两个不可用方向，但仍没有自足证明
noncanonical 包。

继续新增：

```text
experiments/prime_matrix_last_remaining_atoms_router.py
docs/monograph/prime-matrix-last-remaining-atoms-router.md/json
```

该路由器把最后开放输入压成三个原子：

```text
last_remaining_atom_boundaries_closed=true；
conditional_logic_chain_complete=true；
all_last_atoms_proved_or_accepted=false；
row_column_unconditional_closed=false。
```

最后原子表为：

```text
ActualFullSNonAPExactSupportAtom；
ModulusDependentCompletedFullSKLSInput；
DStructureRankinIndependentAcceptance。
```

其中前两者是 noncanonical full-S 补集的二选一闭合方式：要么证明实际 full-S non-AP 源的精确
支撑/源熵自足定理，要么证明或接受模数依赖 completed full-S Kloosterman 大筛输入。第三者是
D-structure/Tail-log4/finite Rankin 晋级包的独立验收原子。因此逻辑链条已经条件闭合：前两者
至少一个成立，且第三者成立时，无隐藏终端链可晋级为完整行/列闭合。当前材料没有证明或独立接受
这些最后原子，所以完整全局无条件定理仍未成立。

继续新增：

```text
experiments/prime_matrix_three_final_atoms_hard_attack_router.py
docs/monograph/prime-matrix-three-final-atoms-hard-attack-router.md/json
```

该路由器继续硬攻三个最终原子，并把它们压成最小无条件输入基：

```text
three_atom_attack_boundary_closed=true；
conditional_logic_chain_complete=true；
all_three_atoms_proved_or_accepted=false；
row_column_unconditional_closed=false。
```

最终二选一数学输入为：

```text
ActualFullSNonAPSourceCapacityAntiAtomForActualSource；
CDependentResidueWeightSpectralCancellationInput。
```

第一个输入要求 actual full-S non-AP 源容量测度没有 moving same-(u,v) 大原子；generic 版本已经由
moving-delta 模型反证，K4/K6 和朴素 incidence 也不能推出。第二个输入要求处理
`B_{c,x}=sum_k beta_{x+kc}` 的 c-dependent completed residue weight 谱抵消；点态 Weil、L2、
普通大筛和平坦 residue 捷径都不足。最终晋级输入为：

```text
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

因此最小无条件输入基为：

```text
(ActualFullSNonAPSourceCapacityAntiAtomForActualSource
 OR CDependentResidueWeightSpectralCancellationInput)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

当前材料没有证明该二选一数学输入，也没有完成独立晋级验收，所以完整全局无条件定理仍未成立。

继续新增：

```text
experiments/prime_matrix_unconditional_closure_final_attempt_router.py
docs/monograph/prime-matrix-unconditional-closure-final-attempt-router.md/json
```

该路由器执行最终无条件闭合尝试：

```text
final_attempt_boundary_closed=true；
math_lanes_collapsed_to_common_core=true；
internal_math_proof_found_in_current_corpus=false；
external_math_match_found_in_current_corpus=false；
independent_promotion_acceptance_completed=false；
row_column_unconditional_closed=false。
```

关键合并是：`CDependentResidueWeightSpectralCancellationInput` 并不是新的独立终端；有限 Fourier
反演把 `B_{c,x}` 接入 `BWFD -> BSC -> KFLS`，而 KFLS 自足剩余又回到 actual same-`(u,v)`
block non-concentration 或外部 DI/BFI/Kuznetsov。另一方面，actual-source 反原子也正是
moving-block spread/source entropy。于是数学终局输入汇合为：

```text
MovingBlockSpreadNCBLKForActualFullSNonAPWFDCoefficients
OR PreciselyMatchedExternalDIBFIKuznetsovDispersionTheorem。
```

再加上不可自验收的晋级输入，最终不可再压缩输入基为：

```text
(MovingBlockSpreadNCBLKForActualFullSNonAPWFDCoefficients
 OR PreciselyMatchedExternalDIBFIKuznetsovDispersionTheorem)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

当前材料没有证明 moving-block spread，也没有给出 full-S/non-AP/未中心化/无投影对象的外部定理
逐项匹配；同时 DStructure/Rankin 独立验收未完成。因此本轮完成的是终局输入边界闭合，而不是
完整全局无条件定理闭合。

继续新增：

```text
experiments/prime_matrix_irreducible_math_input_refinement_router.py
docs/monograph/prime-matrix-irreducible-math-input-refinement-router.md/json
```

该路由器把上一轮的外部标签进一步精化：

```text
refinement_boundary_closed=true；
existing_primary_dibfi_match_rejected=true；
ap_source_lift_rejected=true；
internal_moving_block_proof_found_in_current_corpus=false；
new_full_s_kls_theorem_proved_or_cited_in_current_corpus=false；
row_column_unconditional_closed=false。
```

精化原因是：现有 BFI AP discrepancy、DI/Maynard J-scale 和 APSourceLift 均不能逐项覆盖当前
full-S、non-AP、未中心化、无投影 WFD 对象。因此 `PreciselyMatchedExternalDIBFIKuznetsovDispersionTheorem`
不能继续作为“已匹配现有主来源”的宽标签使用，必须改写成必须新增、证明或明确引用的：

```text
FullSNonAPWFDKLSTheoremInput。
```

最新不可约输入基为：

```text
(MovingBlockSpreadNCBLKForActualFullSNonAPWFDCoefficients
 OR FullSNonAPWFDKLSTheoremInput)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

这一步关闭的是输入命名精度缺口，不是证明缺口。当前材料仍没有内部 moving-block spread 证明，
没有 full-S non-AP WFD KLS 新定理证明或外部逐项引用，也没有完成 DStructure/Rankin 独立验收。

继续新增：

```text
experiments/prime_matrix_fulls_kls_movingblock_joint_attack_router.py
docs/monograph/prime-matrix-fulls-kls-movingblock-joint-attack-router.md/json
```

该路由器把内部 `MovingBlockSpreadNCBLK` 与外部 `FullSNonAPWFDKLS` 放在同一审查表中硬攻：

```text
joint_attack_boundary_closed=true；
internal_lane_proved_in_current_corpus=false；
external_lane_proved_or_cited_in_current_corpus=false；
dstructure_rankin_independent_acceptance_completed=false；
row_column_unconditional_closed=false。
```

关键收束是：canonical RIW/Buchstab 分支已经闭合并从 noncanonical full-S 补集中扣除，不能把
canonical 支撑结论偷渡到 noncanonical 反原子。内部路线继续降到：

```text
FullSNonAPExactFactorSupportPackageForActualNoncanonicalSource。
```

该包包含精确因子支撑下界、balanced range 阈值、Type/Fourier 容量兼容，以及小支撑触发
factor-residue incidence 或直接支撑定理。外部路线仍是：

```text
FullSNonAPWFDKLSTheoremInput。
```

BFI、DI、Maynard 主来源提供 AP/dispersion/Kuznetsov 技术，但现有审查没有发现直接覆盖本文
`c` 依赖完成 residue 权重、未中心化、无投影、full-S、non-AP 和任意对数节省的现成定理。
因此最新输入基为：

```text
(FullSNonAPExactFactorSupportPackageForActualNoncanonicalSource
 OR FullSNonAPWFDKLSTheoremInput)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

继续新增：

```text
experiments/prime_matrix_dual_lane_terminal_reduction_router.py
docs/monograph/prime-matrix-dual-lane-terminal-reduction-router.md/json
```

该路由器继续拆开两线终端：

```text
terminal_reduction_boundary_closed=true；
internal_lane_closed=false；
external_lane_closed=false；
rankin_promotion_accepted=false；
row_column_unconditional_closed=false。
```

内部线中 `FullSNonAPBalancedRangeThreshold` 已闭合，因为 full-S 下 `C≈P/log^O(P)`，
`c=uv` 的平衡因子大小超过任意固定对数阈值；剩下的 exact factor support 与
Type/Fourier capacity compatibility 等价于最终源容量测度无 moving same-`(u,v)` 原子：

```text
FullSNonAPStrengthenedSourceAntiAtomContractForActualNoncanonicalSource。
```

外部线中 full-S 窗口可按模 `c` 完成，真正剩余变成完成后权重
`B_{c,x}=sum_k beta_{x+k c}` 的谱/dispersion 抵消：

```text
CDependentResidueWeightSpectralCancellationInput。
```

因此最新输入基为：

```text
(FullSNonAPStrengthenedSourceAntiAtomContractForActualNoncanonicalSource
 OR CDependentResidueWeightSpectralCancellationInput)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

继续新增：

```text
experiments/prime_matrix_dual_lane_common_core_reconciliation_router.py
docs/monograph/prime-matrix-dual-lane-common-core-reconciliation-router.md/json
```

该路由器检查上一轮“内部反原子 / 外部 c-dependent 谱输入”是否真是两条独立自足剩余。结论为：

```text
common_core_reconciliation_closed=true；
self_contained_common_core_proved=false；
external_contract_accepted_as_final_input=false；
dstructure_rankin_independent_acceptance_completed=false；
row_column_unconditional_closed=false。
```

关键调和律是：`CDependentResidueWeightSpectralCancellationInput` 若作为外部 FullS-KLS/c-dependent
谱定理接受，就是外部合同输入；若不接受黑箱而在当前材料中自证，有限 Fourier completion 会把
它降回 `BWFD -> BSC -> KFLS`，随后回到 actual same-`(u,v)` block non-concentration。这与内部
`FullSNonAPStrengthenedSourceAntiAtomContractForActualNoncanonicalSource` 的 moving-block/source
entropy 核心是同一个数学义务。

因此两线调和后的输入基为：

```text
((ActualA1FullSSourceLockOrNewFullSNonAPSourceAntiAtomTheoremInput)
 OR AcceptedFullSKLSExtOrCDependentResidueWeightSpectralCancellationInput)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

若坚持完全自足且不接受外部黑箱，则输入基进一步固定为：

```text
ActualA1FullSSourceLockOrNewFullSNonAPSourceAntiAtomTheoremInput
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

这一步闭合的是外部/内部两线的独立性缺口，不是无条件定理证明。当前材料仍没有证明实际源恒等或
新 full-S 源反原子，也没有完成 DStructure/Rankin 独立验收。

继续新增：

```text
experiments/prime_matrix_self_contained_narrowest_core_router.py
docs/monograph/prime-matrix-self-contained-narrowest-core-router.md/json
```

该路由器专门处理完全自足版中的 `ActualA1FullSSourceLock OR NewFullSNonAPSourceAntiAtom` 是否仍
是全局剩余。结论为：

```text
narrowest_core_reduction_closed=true；
canonical_source_lock_absorbed_for_canonical_branch=true；
source_lock_option_removed_from_global_remainder=true；
external_black_box_used=false；
generic_self_contained_antiatom_available=false；
noncanonical_actual_source_core_proved=false；
dstructure_rankin_independent_acceptance_completed=false；
row_column_unconditional_closed=false。
```

结构律是：canonical source-lock 已经由 canonical RIW/Buchstab 分支和 actual-source provenance
账本吸收，不能再作为 unrestricted/global full-S noncanonical 补集的闭合输入；generic 自足反原子
又被 moving-delta 模型反证。因此外部黑箱被排除后，全局完全自足数学剩余不再是
`ActualA1FullSSourceLock OR generic anti-atom`，而是：

```text
ActualNoncanonicalFullSSourceEntropyOrStrengthenedAntiAtomTheoremInput
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

这里的源核心合同是：对 actual noncanonical full-S non-AP WFD 系数证明 exact source entropy，
或证明其 final source capacity measure 没有 moving same-`(u,v)` 大原子；该命题不能替换成
unrestricted generic WFD 模板。此步闭合 source-lock/global-complement 歧义，但没有证明
noncanonical actual source core，也没有完成 DStructure/Rankin 独立验收。

继续新增：

```text
experiments/prime_matrix_noncanonical_source_core_atomization_router.py
docs/monograph/prime-matrix-noncanonical-source-core-atomization-router.md/json
```

该路由器把上一轮的 `ActualNoncanonicalFullSSourceEntropyOrStrengthenedAntiAtomTheoremInput`
继续原子化。结论为：

```text
source_core_atomization_closed=true；
entropy_antiatom_duality_removed=true；
balanced_range_threshold_closed=true；
k4_k6_or_naive_incidence_suffices=false；
canonical_import_allowed=false；
actual_support_capacity_core_proved=false；
dstructure_rankin_independent_acceptance_completed=false；
row_column_unconditional_closed=false。
```

结构律是：actual noncanonical source entropy 与 strengthened anti-atom 不是两条独立路线，而是同一个
source-capacity 核心的两种命名。`ExactFullSNonAPWFDSourceEntropy` 已降为精确支撑包；full-S regime
中 balanced range 阈值已经由 `C≈P/log^O(P)` 与 `U,V≈C^{1/2}log^O(P)` 支付；强化反原子正是 final
source capacity measure 无 moving same-`(u,v)` 大原子。

同时，K4/K6、朴素 incidence 和 canonical 支撑偷渡都被阻断：K4/K6 控制固定 residue/phase 或
dyadic bookkeeping，不控制 moving factor-pair 支撑；一个 `(u,v)` 块可含增长的内部
`h,ell,x,z` fiber，使质量在内部原子上平坦但仍集中在同一 factor pair；canonical RIW/Buchstab 支撑只
属于 canonical 分支，不属于 noncanonical 补集。

因此完全自足最新输入基为：

```text
ActualNoncanonicalFullSFactorSupportCapacityTheoremInput
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

其中 `ActualNoncanonicalFullSFactorSupportCapacityTheoremInput` 要求：对每个幸存 actual noncanonical
full-S non-AP balanced block，证明精确 `u`、`v` 因子有对数幂级绝对支撑下界，并证明
Type/Fourier 容量兼容，使任何 moving `(u,v)` 对不能获得未登记的容量乘子。该步闭合命名二义性
和伪捷径排除，仍没有证明 actual 支撑/容量核心，也没有完成 DStructure/Rankin 独立验收。

继续新增：

```text
experiments/prime_matrix_actual_capacity_ledger_microatom_router.py
docs/monograph/prime-matrix-actual-capacity-ledger-microatom-router.md/json
```

该路由器把 actual 支撑/容量核心再向内校准为最终容量账本命题。结论为：

```text
microatom_boundary_closed=true；
support_only_suffices=false；
registered_multiplier_discipline_would_suffice_with_support=true；
exact_uv_support_proved=false；
registered_multiplier_discipline_proved=false；
actual_final_capacity_antiatom_proved=false；
dstructure_rankin_independent_acceptance_completed=false；
row_column_unconditional_closed=false。
```

关键结构律是：raw `u/v` 支撑宽不等于最终 source anti-atom。若 Type/Fourier/fiber 步骤允许某个
moving `(u,v)` 对获得未登记容量乘子，则最终容量测度 `M_{u,v}` 仍可集中。反过来，若
`|alpha_u|,|delta_v|<=L^C`，所有登记乘子 `W_{u,v}<=L^E`，并且
`S_u*S_v>=L^(2A+4C+E)`，则 `max M_{u,v}/sum M_{u,v}<=L^(-2A)`。

因此最新完全自足单原子表述为：

```text
ActualFinalCapacityAntiAtomLedgerForNoncanonicalFullS
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

可行证明包是：

```text
ActualNoncanonicalExactUVSupportLowerBound
AND ActualTypeFourierRegisteredCapacityMultiplierDiscipline。
```

这一步闭合支撑-only 偷换和条件蕴含公式；它仍没有证明 actual final capacity anti-atom ledger，
也没有完成 DStructure/Rankin 独立验收。

继续新增：

```text
experiments/prime_matrix_registered_capacity_multiplier_discipline_router.py
docs/monograph/prime-matrix-registered-capacity-multiplier-discipline-router.md/json
```

该路由器直接攻击 `ActualTypeFourierRegisteredCapacityMultiplierDiscipline`。结论为：

```text
registered_capacity_multiplier_discipline_closed=true；
exact_uv_support_proved=false；
actual_final_capacity_antiatom_proved=false；
dstructure_rankin_independent_acceptance_completed=false；
row_column_unconditional_closed=false。
```

结构律是：Type/Fourier/fiber 乘子纪律是账本门，不是新的谱相消输入。Type/Vaughan-Heath-Brown
分解、dyadic 求和、CRT 相位归一化、Fourier `h` 窗口和尾项、系数/gcd/端点/平滑、full-S
completion fiber 与 tail-label bookkeeping 都已有同一 actual formal unit 的登记行，且统一付出
`log^O` 成本。本步不调用外部 DI/BFI no-projection，不关闭 external theorem-match 分支，也不证明
`ExactUVSupport`。

因此完全自足源核心从：

```text
ActualNoncanonicalExactUVSupportLowerBound
AND ActualTypeFourierRegisteredCapacityMultiplierDiscipline
```

压成：

```text
ActualNoncanonicalExactUVSupportLowerBound。
```

最新输入基为：

```text
ActualNoncanonicalExactUVSupportLowerBound
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

这一步完成两个源微输入中的乘子纪律项；当前唯一源侧微输入是 `ActualNoncanonicalExactUVSupportLowerBound`，
但完整行/列无条件定理仍需 DStructure/Rankin 独立验收。

继续新增：

```text
experiments/prime_matrix_exact_uv_support_terminal_attack_router.py
docs/monograph/prime-matrix-exact-uv-support-terminal-attack-router.md/json
```

该路由器直接攻击剩余的 `ActualNoncanonicalExactUVSupportLowerBound`。结论为：

```text
exact_uv_support_terminal_boundary_closed=true；
registered_capacity_multiplier_discipline_closed=true；
exact_uv_support_proved=false；
actual_final_capacity_antiatom_proved=false；
dstructure_rankin_independent_acceptance_completed=false；
row_column_unconditional_closed=false。
```

结构律是：ExactUVSupport 已是当前材料的唯一源侧终端输入。它不能由 formal WFD 推出，因为 generic
WFD 允许点支撑因子；不能由 K4/K6 或朴素 incidence 推出，因为这些投影不控制 moving factor-pair
支撑；不能由 raw Buchstab 计数推出，因为厚区间数量只是 canonical 层支撑链的一部分；也不能由
canonical RIW/Buchstab 支撑链偷渡推出，因为那只关闭 canonical-source 分支，不关闭 noncanonical
full-S 补集。

因此最新输入基仍为：

```text
ActualNoncanonicalExactUVSupportLowerBound
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

若以后证明 `ActualNoncanonicalExactUVSupportLowerBound`，则结合已闭合的 registered multiplier
discipline 可推出 final capacity anti-atom ledger；再加 DStructure/Rankin 独立验收后，当前边界链
才可升级。当前材料完成的是终端边界审查，不是无条件证明。

继续新增：

```text
experiments/prime_matrix_exact_uv_support_failure_packetization_router.py
docs/monograph/prime-matrix-exact-uv-support-failure-packetization-router.md/json
```

该路由器把 `ActualNoncanonicalExactUVSupportLowerBound` 的失败完全包化。结论为：

```text
failure_packetization_closed=true；
exact_uv_support_proved=false；
actual_support_failure_packet_exclusion_proved=false；
actual_final_capacity_antiatom_proved=false；
dstructure_rankin_independent_acceptance_completed=false；
row_column_unconditional_closed=false。
```

结构律是：在 actual noncanonical clean block、exact `u/v` 支撑定义和 registered multiplier 阈值都已固定后，
`ActualNoncanonicalExactUVSupportLowerBound` 等价于不存在正质量
`ActualNoncanonicalSupportFailurePacket`。若支撑失败，它必须物化为 finite sparse packet，并携带
`source_class`、`formal_unit_id`、`block_key`、exact `u/v` 支撑、`L^(2A+4C+E)` 阈值、registered
capacity profile、回流测试和可复现证书；否则该失败命题无准入。

因此最新完全自足输入基可等价写成：

```text
ActualNoncanonicalSupportFailurePacketExclusion
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

这一步关闭“支撑失败还能无名停留”的边界，但没有证明所有 packet 不存在或必回流。下一步的源侧最窄硬点是
`ActualNoncanonicalSupportFailurePacketExclusion`，或直接证明 final capacity anti-atom；最终仍需
DStructure/Rankin 独立验收。

继续新增：

```text
experiments/prime_matrix_support_failure_packet_return_dichotomy_router.py
docs/monograph/prime-matrix-support-failure-packet-return-dichotomy-router.md/json
```

该路由器继续攻击 `ActualNoncanonicalSupportFailurePacketExclusion`。结论为：

```text
support_failure_packet_return_dichotomy_closed=true；
clean_core_packet_exclusion_proved=false；
actual_final_capacity_antiatom_proved=false；
dstructure_rankin_independent_acceptance_completed=false；
row_column_unconditional_closed=false。
```

结构律是：支撑失败 packet 不能成为第五类隐藏终端。若它不是 clean-core packet，就必须按有限孤立
packet、持久有限签名、ColumnCRT/位移、漂移 CleanKLS/DLS 或已阻断逃逸之一回流。孤立有限包进入
`LocalSurvivor/SAE` packet 证书；持久有限签名进入显式 primitive `PDEC` schema；列/位移/endpoint/cofactor
负载进入 `ColumnCRT` 吸收到的 `PDEC/SAE`；所有有限签名都不持久的 moving block 进入
`CleanKLS/DLS`、exact source entropy 或外部 KLS。

因此最新源侧最窄微输入压成：

```text
ActualNoncanonicalCleanCoreSupportFailurePacketExclusion。
```

连同独立晋级门，最新完全自足输入基为：

```text
ActualNoncanonicalCleanCoreSupportFailurePacketExclusion
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

clean-core packet 是通过所有回流测试后仍保留的正质量 actual noncanonical full-S non-AP balanced block：
同 formal unit、低于 exact `u/v` 支撑阈值、无 canonical 导入、无有限 sparse witness、无持久 PDEC 签名、
无列位移缺陷，也未进入外部或 generic CleanKLS。本步闭合回流完备性；当前材料仍未证明 clean-core
packet 不存在或必然矛盾。

继续新增：

```text
experiments/prime_matrix_clean_core_moving_atom_sharp_input_router.py
docs/monograph/prime-matrix-clean-core-moving-atom-sharp-input-router.md/json
```

该路由器继续校准 `ActualNoncanonicalCleanCoreSupportFailurePacketExclusion`。结论为：

```text
clean_core_moving_atom_sharp_boundary_closed=true；
clean_core_moving_atom_exclusion_proved=false；
actual_final_capacity_antiatom_proved=false；
dstructure_rankin_independent_acceptance_completed=false；
row_column_unconditional_closed=false。
```

结构律是：clean-core 支撑失败 packet 排斥是足够条件，但比最终目标更强。由于 registered multiplier
discipline 已闭合，final capacity 大原子的逆否会产生低于阈值的 exact `u/v` 支撑失败 packet；因此
终局真正需要排斥的是 clean-core final capacity measure 的 moving same-`(u,v)` 大原子，而不是所有
不会造成容量集中的低支撑 packet。

最新源侧 sharp 微输入为：

```text
ActualNoncanonicalCleanCoreMovingAtomExclusion。
```

连同独立晋级门，最新完全自足输入基为：

```text
ActualNoncanonicalCleanCoreMovingAtomExclusion
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

`ActualNoncanonicalCleanCoreMovingAtom` 是通过所有回流测试的正质量 actual noncanonical full-S non-AP
balanced block 中的 pair `(u,v)`，其最终登记容量 `M_{u,v}/sum M_{u,v}` 超过 `log^{-2A}` 阈值。本步只是
关闭输入口径，当前材料仍未证明该 moving atom exclusion；formal WFD、Type/Fourier 和固定投影路线仍被
moving-delta 阻断。

继续新增：

```text
experiments/prime_matrix_clean_core_terminal_normal_form_router.py
docs/monograph/prime-matrix-clean-core-terminal-normal-form-router.md/json
```

该路由器把 `ActualNoncanonicalCleanCoreMovingAtomExclusion` 归一化为终局输入标准形。结论为：

```text
clean_core_terminal_normal_form_closed=true；
internal_exact_entropy_proved=false；
external_completed_kls_accepted=false；
dstructure_rankin_independent_acceptance_completed=false；
row_column_unconditional_closed=false。
```

标准形律是：clean-core moving atom 排斥的内部等价表述是 exact clean-core source entropy，即对通过全部
回流测试后的 clean-core moving block `b=(u,v)`，

```text
max_b M_b / sum_b M_b <= log^{-2A}。
```

外部替代标准形也不能再泛称 DI/BFI 或普通 Kuznetsov，而必须是 full-S 完成分解后带 `c`-dependent residue
weights 的 `ModulusDependentCompletedFullSKLSInput`。因此最新条件终局输入基为：

```text
(ExactCleanCoreFullSNonAPWFDSourceEntropy
 OR ModulusDependentCompletedFullSKLSInput)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

若坚持完全自足路线，则最新输入基为：

```text
ExactCleanCoreFullSNonAPWFDSourceEntropy
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

本步闭合的是终局输入标准形和命名循环，不是 exact entropy 证明，也不是 completed KLS 接受，更不是
DStructure/Rankin 独立验收完成。

继续新增：

```text
experiments/prime_matrix_clean_core_exact_entropy_atom_router.py
docs/monograph/prime-matrix-clean-core-exact-entropy-atom-router.md/json
```

该路由器把 `ExactCleanCoreFullSNonAPWFDSourceEntropy` 的失败形态原子化。结论为：

```text
clean_core_exact_entropy_atom_boundary_closed=true；
clean_core_terminal_support_incidence_proved=false；
exact_clean_core_entropy_proved=false；
dstructure_rankin_independent_acceptance_completed=false；
row_column_unconditional_closed=false。
```

原子律是：若 exact clean-core entropy 失败，则存在 clean-core moving 大原子。registered multiplier
discipline 已闭合，所以失败不能归因于账外 Type/Fourier/fiber 乘子；支撑失败 packetization 已闭合，
所以支撑失败必须给出 packet；非 clean-core packet 的回流二分已闭合，所以剩余只能是通过全部回流测试的
clean-core terminal support atom。

因此完全自足路线的可行动证明包进一步写成：

```text
CleanCoreTerminalSupportIncidenceTheorem
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

`CleanCoreTerminalSupportIncidenceTheorem` 要求每个正质量 actual clean-core full-S non-AP WFD block
在同一 formal unit 内给出足够 exact `u/v` 支撑乘积，以抵消 divisor bound 与所有 registered capacity
multipliers。本步没有证明该支撑-关联定理；它只是把 exact entropy 的失败压成可复现的 clean-core
终端支撑原子。

继续新增：

```text
experiments/prime_matrix_clean_core_support_incidence_attack_router.py
docs/monograph/prime-matrix-clean-core-support-incidence-attack-router.md/json
```

该路由器直接攻击 `CleanCoreTerminalSupportIncidenceTheorem`。结论为：

```text
clean_core_support_incidence_attack_boundary_closed=true；
clean_core_exact_layer_transfer_proved=false；
clean_core_terminal_support_incidence_proved=false；
external_completed_kls_accepted=false；
dstructure_rankin_independent_acceptance_completed=false；
row_column_unconditional_closed=false。
```

攻击结果是：full-S range 阈值、registered capacity budget、厚区间 raw squarefree/Buchstab 计数都已闭合；
一旦 exact `u/v` 支撑成立，entropy/anti-atom 的初等推出也已闭合。剩余不是数量不足，而是 exact
clean-core 层是否承认这些 Buchstab products，且其 actual `alpha/delta` 系数非零。

同时三条路线被排除：朴素 factor-residue incidence 被内部 `h,ell,x,z` fiber 阻断；canonical 层支撑不能
导入 noncanonical clean-core；普通 squarefree 计数不能代替 exact 层承认和非零转移。因此最新条件输入基为：

```text
(CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn
 OR ModulusDependentCompletedFullSKLSInput)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

完全自足输入基为：

```text
CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

该内部子输入要求 exact clean-core 层承认厚 balanced block 中足够多 Buchstab products、系数非零，并把
thin 或 layer-rejected block 回流到命名出口。本步没有证明该定理；它关闭的是从 K4/K6、canonical 支撑或
普通计数偷渡到 clean-core 支撑关联的错误方向。

继续新增：

```text
experiments/prime_matrix_clean_core_layer_transfer_path_router.py
docs/monograph/prime-matrix-clean-core-layer-transfer-path-router.md/json
```

该路由器把 `CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn` 继续压成 actual clean-core
系数路径分割账本。结论为：

```text
clean_core_layer_transfer_path_boundary_closed=true；
clean_core_path_partition_proved=false；
clean_core_exact_layer_transfer_proved=false；
external_completed_kls_accepted=false；
dstructure_rankin_independent_acceptance_completed=false；
row_column_unconditional_closed=false。
```

结构律是：canonical RIW/Buchstab 决策树和来源账本已经闭合，但只在 canonical-source 分支内有效。
clean-core noncanonical 残余不能导入该来源；它必须给出自己的 actual coefficient path partition，或走
completed KLS/命名回流。若 actual clean-core 系数可被分割成 polylog 多个互斥 exact 路径签名，并且
同路径非零无抵消，则 pigeonhole 给出 selector retention；再结合 raw Buchstab support 与 thin/rejected
return，就推出 clean-core exact layer transfer。

最新条件输入基为：

```text
(CleanCoreExactCoefficientPathPartitionNoCancellationAndThinReturn
 OR ModulusDependentCompletedFullSKLSInput)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

完全自足输入基为：

```text
CleanCoreExactCoefficientPathPartitionNoCancellationAndThinReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

本步没有证明该路径分割账本；它关闭的是 canonical 决策树跨分支偷渡和 generic WFD 形式替代路径账本的错误方向。

继续新增：

```text
experiments/prime_matrix_clean_core_path_source_firewall_router.py
docs/monograph/prime-matrix-clean-core-path-source-firewall-router.md/json
```

该路由器把 `CleanCoreExactCoefficientPathPartitionNoCancellationAndThinReturn` 继续压到 pre-Cauchy
系数来源律。结论为：

```text
clean_core_path_source_firewall_boundary_closed=true；
clean_core_precauchy_source_law_proved=false；
clean_core_path_partition_proved=false；
external_spectral_atom_accepted=false；
dstructure_rankin_independent_acceptance_completed=false；
row_column_unconditional_closed=false。
```

来源律是：路径分割账本必须建立在 Cauchy/dispersion 前的 actual clean-core `alpha/delta` 系数公式上；
该公式要给出 exact 来源、polylog 路径签名、同路径非零/无抵消，以及路径超预算或薄块的命名回流。
防火墙律是：canonical 决策树只能作为模板，不能跨分支导入；generic WFD 形式已被 moving-delta 阻断。

最新条件输入基为：

```text
(CleanCorePreCauchyCoefficientSourceLawAndReturn
 OR CDependentResidueWeightSpectralCancellationInput)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

完全自足输入基为：

```text
CleanCorePreCauchyCoefficientSourceLawAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

本步没有证明 clean-core 来源律；它只是关闭 canonical 决策树偷渡和 generic WFD 形式替代 actual source law
这两个错误方向。

继续新增：

```text
experiments/prime_matrix_clean_core_precauchy_source_law_atom_router.py
docs/monograph/prime-matrix-clean-core-precauchy-source-law-atom-router.md/json
```

该路由器把 `CleanCorePreCauchyCoefficientSourceLawAndReturn` 再压缩到原始生成账本。结论为：

```text
clean_core_precauchy_source_law_atom_boundary_closed=true；
origin_generation_ledger_implication_closed=true；
clean_core_original_coefficient_generation_ledger_proved=false；
clean_core_precauchy_source_law_proved=false；
external_spectral_atom_accepted=false；
dstructure_rankin_independent_acceptance_completed=false；
row_column_unconditional_closed=false。
```

压缩定理是：pre-Cauchy 来源律的真正原子是
`CleanCoreOriginalCoefficientGenerationLedgerAndReturn`。若在 Cauchy/dispersion 前列出 actual clean-core
`alpha/delta` 的同一 formal unit 原始生成表，则 branch key 给出 exact path signature，K6/tail-label
给出 polylog 路径预算，同一完整 key 的 local factors 给出非零/无抵消；缺失来源、路径超预算、thin/rejected
block 或未消除抵消必须带 return tag 回流到 PDEC/SAE/ColumnCRT/CleanKLS 或外部谱输入。

最新条件输入基为：

```text
(CleanCoreOriginalCoefficientGenerationLedgerAndReturn
 OR CDependentResidueWeightSpectralCancellationInput)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

完全自足输入基为：

```text
CleanCoreOriginalCoefficientGenerationLedgerAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

本步没有证明 clean-core 原始生成账本。它闭合的是逻辑压缩：canonical 来源表不能跨分支导入，
generic WFD 形式不能替代 actual 来源；noncanonical clean-core 若要自足闭合，必须提交自己的原始生成账本。

继续新增：

```text
experiments/prime_matrix_clean_core_origin_source_admission_router.py
docs/monograph/prime-matrix-clean-core-origin-source-admission-router.md/json
```

该路由器把 `CleanCoreOriginalCoefficientGenerationLedgerAndReturn` 继续压成 primitive source constructor
准入。结论为：

```text
clean_core_origin_source_admission_boundary_closed=true；
constructor_admission_implies_origin_ledger=true；
unregistered_source_return_absorbed=false；
clean_core_primitive_source_constructor_admission_proved=false；
clean_core_original_coefficient_generation_ledger_proved=false；
external_spectral_atom_accepted=false；
dstructure_rankin_independent_acceptance_completed=false；
row_column_unconditional_closed=false。
```

压缩律是：原始生成账本的入口不是估计，而是来源准入。必须先证明 actual clean-core `alpha/delta`
由某个 pre-Cauchy primitive source constructor 生成；构造器准入后，emitted summand schema 可展开为原始生成账本。
构造器缺失、口径冲突、超预算或 thin block 必须带 return tag，落到 PDEC/SAE/ColumnCRT/CleanKLS
或外部谱输入；否则未登记来源会成为新的隐藏终端。

最新条件输入基为：

```text
(CleanCorePrimitiveSourceConstructorAdmissionAndReturn
 OR CDependentResidueWeightSpectralCancellationInput)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

完全自足输入基为：

```text
CleanCorePrimitiveSourceConstructorAdmissionAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

本步没有证明 primitive source constructor 准入，也没有吸收未登记来源。它只把原始生成账本的最小入口压成
来源构造器准入：没有构造器，就没有合法 clean-core 原始账本。

继续新增：

```text
experiments/prime_matrix_clean_core_constructor_source_class_firewall_router.py
docs/monograph/prime-matrix-clean-core-constructor-source-class-firewall-router.md/json
```

该路由器把 `CleanCorePrimitiveSourceConstructorAdmissionAndReturn` 按来源类别拆开。结论为：

```text
constructor_source_class_firewall_boundary_closed=true；
source_class_partition_closed=true；
unregistered_source_return_absorbed=true；
actual_noncanonical_primitive_constructor_formula_proved=false；
clean_core_primitive_source_constructor_admission_proved=false；
external_spectral_atom_accepted=false；
dstructure_rankin_independent_acceptance_completed=false；
row_column_unconditional_closed=false。
```

来源分类防火墙律是：primitive constructor admission 必须先分成 canonical、generic WFD、未登记/混合
formal unit、external spectral、actual noncanonical 五类。canonical constructor 已在 canonical-source 分支内闭合；
generic WFD 不是 constructor；未登记或混合 formal unit 来源经 Multiplicity/Stitching 或 K7 formal-unit 失败回流；
external spectral 类仍是外部谱输入。因此唯一完全自足源侧原子为：

```text
ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn。
```

最新条件输入基为：

```text
(ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn
 OR CDependentResidueWeightSpectralCancellationInput)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

完全自足输入基为：

```text
ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

本步没有证明 actual noncanonical primitive constructor formula。它闭合的是来源分类防火墙：canonical、generic、
unregistered 和 external 类都已按边界处理，唯一自足剩余是 actual noncanonical 显式公式。

继续新增：

```text
experiments/prime_matrix_clean_core_external_lemma_parameter_match_router.py
docs/monograph/prime-matrix-clean-core-external-lemma-parameter-match-router.md/json
```

该路由器把最新自足原子与 DI/BFI/Kuznetsov 外部引理逐项做结构和参数匹配。结论为：

```text
external_lemma_parameter_match_boundary_closed=true；
external_lemmas_match_constructor_formula=false；
external_lemmas_close_self_contained_remainder=false；
external_spectral_atom_accepted=false；
actual_noncanonical_primitive_constructor_formula_proved=false；
row_column_unconditional_closed=false。
```

对比律是：外部 DI/BFI/Kuznetsov 引理与当前自足原子处在不同层级。外部引理处理 completion 之后的
Kloosterman/AP/谱平均，要求系数或 residue 权重已经给定；当前自足原子要求在 Cauchy/dispersion 前写出
actual noncanonical `alpha/delta` 的 primitive constructor。故外部引理不能替代该公式，只能作为
`external_spectral` 分支候选。

参数匹配矩阵的核心结论如下：

| 引理族 | 匹配处 | 不匹配处 | 路由 |
| --- | --- | --- | --- |
| DI/Kuznetsov KLS | 完成后逆元相位、模数/频率平均 | 不生成 pre-Cauchy summand emitter | external KLS |
| BFI Theorem 10 | well-factorable AP discrepancy | 当前对象为 non-AP constructor | APSourceLift 或外部 |
| Maynard well-factorable AP | 更强 AP 分布背景 | 不处理 `B_{c,x}` 依赖或 source emitter | 背景，不闭合 |
| KLS-window template | CRT 相位、模数、频率已匹配 | 从已给定系数开始 | CleanKLS/external |
| C-dependent completed residue spectral | 最接近外部目标 | 尚无接受定理 | `CDependentResidueWeightSpectralCancellationInput` |

因此最新输入基保持：

```text
(ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn
 OR CDependentResidueWeightSpectralCancellationInput)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

完全自足输入基仍为：

```text
ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

继续新增：

```text
experiments/prime_matrix_clean_core_reverse_provenance_functor_router.py
docs/monograph/prime-matrix-clean-core-reverse-provenance-functor-router.md/json
```

该路由器把前面所有正向来源保持模型反向审查：actual payment graph、有限投影塔、方向弧限制、
横向商和来源分类防火墙都能保持同一 formal unit 的来源兼容，但它们都是正向推前或有限因子，
不能从 `Gamma` 反推出唯一 pre-Cauchy primitive summand。结论为：

```text
reverse_provenance_functor_boundary_closed=true；
payment_pushforward_functoriality_available=true；
pushforward_reverse_uniqueness_rejected=true；
finite_projection_recovers_gamma_not_source=true；
constructor_formula_equivalent_to_registered_fiber_emitter=true；
registered_primitive_prepushforward_fiber_emitter_proved=false；
actual_noncanonical_primitive_constructor_formula_proved=false；
row_column_unconditional_closed=false。
```

反向函子律是：`Gamma` 及其所有有限投影最多恢复下游 payment 质量，不恢复被推前前的 primitive
source；不同来源纤维分解可以给出同一个 payment graph。若要把当前 clean-core 残余变成自足证明，
必须提供同一 formal unit 内的已登记 pre-pushforward 纤维分解 emitter。该 emitter 对每个正质量
clean-core payment atom 输出有限/polylog 个 primitive preimage summand，并证明 `alpha/delta`、
branch key、`u/v` map、符号、local factor 和系数恒等式；无法登记、空纤维、超预算或 thin block
必须回流。

于是最新内部输入从“直接写公式”改写为更可审查的：

```text
RegisteredPrimitivePrePushforwardFiberEmitterAndReturn。
```

最新条件输入基为：

```text
(RegisteredPrimitivePrePushforwardFiberEmitterAndReturn
 OR CDependentResidueWeightSpectralCancellationInput)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

完全自足输入基为：

```text
RegisteredPrimitivePrePushforwardFiberEmitterAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

本步没有证明该 emitter；它关闭的是反向来源的边界误差：不能把下游 payment/profinite 几何结构误当作
上游 constructor 公式，但可以把最终自足硬点压成一个具体、可验收、可失败回流的纤维分解输入。

继续新增：

```text
experiments/prime_matrix_clean_core_fiber_emitter_field_audit_router.py
docs/monograph/prime-matrix-clean-core-fiber-emitter-field-audit-router.md/json
```

该路由器把 `RegisteredPrimitivePrePushforwardFiberEmitterAndReturn` 逐字段拆开。结论为：

```text
fiber_emitter_field_audit_boundary_closed=true；
payment_fiber_skeleton_closed=true；
first_cover_payment_map_closed=true；
payment_count_identity_closed=true；
alpha_delta_coefficient_lift_proved=false；
polylog_branch_schema_proved=false；
registered_primitive_prepushforward_fiber_emitter_proved=false；
row_column_unconditional_closed=false。
```

字段律是：`ActualPaymentSelection` 已经给出 completion-hole 域、first-cover `pay(c,y)` 和
`payment_count=sum_phase M(phase)*|H_low(phase)|` 的计数恒等式；`ActualPaymentStitching`
又排除 payment 层第四出口。因此 registered fiber emitter 的 payment 骨架已经闭合。可是该骨架只是
计数型 `Gamma`，它不等于 clean-core signed `alpha/delta` primitive summand。

在未登记来源回流、同一 formal unit 纪律和 canonical/noncanonical 分支隔离都闭合后，最新真正未闭合字段为：

```text
ExactAlphaDeltaLiftForRegisteredPaymentFiberSkeletonAndReturn。
```

该输入要求把 payment skeleton 提升为同一 formal unit 内的 actual noncanonical `alpha/delta` 预 Cauchy
primitive 系数，给出 polylog branch key、`u/v` map、phase/sign/local factor 和系数恒等式；无法提升者
必须命名回流。

最新条件输入基为：

```text
(ExactAlphaDeltaLiftForRegisteredPaymentFiberSkeletonAndReturn
 OR CDependentResidueWeightSpectralCancellationInput)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

完全自足输入基为：

```text
ExactAlphaDeltaLiftForRegisteredPaymentFiberSkeletonAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

本步没有证明 alpha/delta lift；它把最后自足硬点从“纤维 emitter 是否存在”进一步缩为“已闭合 payment 骨架
能否精确提升为 signed primitive 系数和 polylog 分支表”。

继续新增：

```text
experiments/prime_matrix_clean_core_alpha_delta_disintegration_router.py
docs/monograph/prime-matrix-clean-core-alpha-delta-disintegration-router.md/json
```

该路由器把 `ExactAlphaDeltaLiftForRegisteredPaymentFiberSkeletonAndReturn` 改写为 signed 源测度沿
first-cover payment map 的解积分问题。结论为：

```text
alpha_delta_disintegration_boundary_closed=true；
payment_base_map_closed=true；
lift_equivalent_to_signed_disintegration_dictionary=true；
canonical_decision_tree_template_scoped=true；
generic_or_unregistered_dictionary_blocked=true；
registered_alpha_delta_disintegration_dictionary_proved=false；
exact_alpha_delta_lift_proved=false；
row_column_unconditional_closed=false。
```

解积分律是：payment skeleton 提供基底映射 `Phi`；exact lift 等价于给出 actual noncanonical signed
`alpha/delta` 源测度 `nu` 在 `Phi` 上的已登记逐纤维字典。若 lift 已有，按 payment atom 分组 summand
即得字典；若字典已有，逐纤维求和和推前恒等式即得 lift。pre-Cauchy 来源账本给出必要字段，
路径分割给出 polylog branch key 的用途，canonical RIW/Buchstab 决策树只提供作用域内模板。

最新内部输入为：

```text
RegisteredAlphaDeltaDisintegrationDictionaryAndReturn。
```

该输入要求：

- pre-Cauchy actual noncanonical signed `alpha/delta` primitive 源测度；
- primitive summand 到 completion-hole/first-cover payment atom 的基底映射；
- 每个 payment atom 的 signed preimage summand 字典；
- branch key、`u/v` map、sign、local factor、总变差/支撑预算与推前恒等式；
- sign-refinement 和失败回流。

最新条件输入基为：

```text
(RegisteredAlphaDeltaDisintegrationDictionaryAndReturn
 OR CDependentResidueWeightSpectralCancellationInput)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

完全自足输入基为：

```text
RegisteredAlphaDeltaDisintegrationDictionaryAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

本步没有证明 noncanonical 字典；它把“系数提升”变成一个可检查的 signed 解积分证据对象，并明确 canonical
模板、generic WFD 与未登记来源都不能替代该对象。

继续新增：

```text
experiments/prime_matrix_clean_core_disintegration_automaticity_router.py
docs/monograph/prime-matrix-clean-core-disintegration-automaticity-router.md/json
```

该路由器继续审查 signed 解积分字典是否本身仍是数学硬点。结论为：

```text
disintegration_automaticity_boundary_closed=true；
discrete_payment_base_map_closed=true；
signed_fiber_disintegration_formal=true；
pushforward_identity_is_real_gate=true；
actual_signed_source_measure_phi_compatibility_budget_proved=false；
row_column_unconditional_closed=false。
```

自动性律是：在离散 first-cover payment map `Phi` 已闭合后，若 actual signed 源测度 `nu` 已给出，则
`nu=sum_a nu|_{Phi^{-1}(a)}` 形式给出逐纤维 signed 字典。故 disintegration 步骤不是新的解析估计。
真正剩余是证明 `nu` 是同一 formal unit 内的 actual noncanonical `alpha/delta` 源测度，证明 `Phi_*nu`
等于目标 payment-side 系数，并完成总变差、绝对支撑与 branch key 预算。

最新内部输入为：

```text
ActualSignedSourceMeasurePhiCompatibilityBudgetAndReturn。
```

该输入要求：

- pre-Cauchy actual noncanonical signed `alpha/delta` 源测度；
- `Phi` 兼容推前恒等式；
- 总变差与绝对支撑预算；
- branch key / sign refinement / local factor 的 polylog/K6 复杂度；
- 源测度缺失、`Phi` 不兼容、超预算、branch 爆炸或抵消回流。

最新条件输入基为：

```text
(ActualSignedSourceMeasurePhiCompatibilityBudgetAndReturn
 OR CDependentResidueWeightSpectralCancellationInput)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

完全自足输入基为：

```text
ActualSignedSourceMeasurePhiCompatibilityBudgetAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

本步没有证明源测度与预算；它只是关闭“字典分解技巧”这个伪硬点，把真正硬点定位到 actual signed source
与 `Phi` 兼容预算。

继续新增：

```text
experiments/prime_matrix_clean_core_geometric_phi_budget_bridge_router.py
docs/monograph/prime-matrix-clean-core-geometric-phi-budget-bridge-router.md/json
```

该路由器把斜线覆盖、圆柱环绕、第P列锚、层叠轮筛和动态容量统一回 clean-core 的 `Phi` 接口。
结论为：

```text
geometric_phi_budget_bridge_boundary_closed=true；
geometric_payment_base_available=true；
geometry_defines_signed_source_measure=false；
geometry_proves_phi_pushforward_identity=false；
geometry_supplies_budget_return_shape=true；
actual_signed_source_measure_phi_compatibility_budget_proved=false；
row_column_unconditional_closed=false。
```

几何模型现在可以诚实承担三件事：给出 payment/Phi 的覆盖-筛除基底，给出总变差/支撑/branch 预算的候选
证书形状，并把容量失败、相位同步或 branch 爆炸送入 `PDEC/SAE/ColumnCRT/CleanKLS`。它不能承担两件事：
生成 pre-Cauchy signed `alpha/delta` 源测度，或证明 `Phi_*nu` 等于目标 payment-side 系数。

因此最新自足输入基分裂为：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn
AND GeometricVariationBranchBudgetCertificateOrNamedReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

条件输入基为：

```text
((ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn
  AND GeometricVariationBranchBudgetCertificateOrNamedReturn)
 OR CDependentResidueWeightSpectralCancellationInput)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

该步没有闭合无条件行/列命题；它关闭的是几何模型与 signed-source 证明之间的接口边界，并把下一步内部
攻击点定位为几何变差/分支预算证书。

继续新增：

```text
experiments/prime_matrix_clean_core_geometric_variation_branch_budget_router.py
docs/monograph/prime-matrix-clean-core-geometric-variation-branch-budget-router.md/json
```

该路由器直接攻击 `GeometricVariationBranchBudgetCertificateOrNamedReturn`。结论为：

```text
geometric_budget_attack_boundary_closed=true；
geometry_ledger_alphabet_closed=true；
dprc_analytic_capacity_bound_proved=false；
signed_variation_branch_lift_proved=false；
geometric_variation_branch_budget_certificate_proved=false；
row_column_unconditional_closed=false。
```

新的压缩律是：

```text
GeometricVariationBranchBudgetCertificateOrNamedReturn
  => DPRCAlpha043CenteredDiscrepancyOrNamedLayerReturn
     AND SignedGeometricLedgerVariationBranchLiftAndReturn。
```

第一把锁是几何解析锁：动态提升轮必须证明 `T_Y<S_Y`，等价地证明正偏差平方根界；若失败，
层叠轮、短窗或列位移必须回流 `PDEC/SAE/ColumnCRT/CleanKLS`。第二把锁是 signed 提升锁：
actual signed `alpha/delta` 源的总变差和 branch key 复杂度必须被 payment 几何账本支配，不能在
`Phi` 纤维内通过正负抵消隐藏出超预算质量。

最新完全自足输入基为：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn
AND DPRCAlpha043CenteredDiscrepancyOrNamedLayerReturn
AND SignedGeometricLedgerVariationBranchLiftAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

继续新增：

```text
experiments/prime_matrix_early_zero_phase_defect_schema_router.py
docs/monograph/prime-matrix-early-zero-phase-defect-schema-router.md/json
```

该路由器接上“假设早期零行”的条件二分，直接处理开放项：

```text
EarlyZeroPhaseDefectSchemaAdmission
  = RegisteredSameFormalUnitRxFxLedger
    AND StableShortRecurrenceCertificateOrNoStableAutomorphism
    AND BoundaryPhaseNoncoverageDefectToPDECOrSAEOrColumnCRT。
```

结论为：

```text
early_zero_phase_defect_schema_admission_closed=true；
registered_same_formal_unit_rxf_ledger=true；
stable_short_recurrence_certificate_or_no_stable_automorphism_closed=true；
boundary_phase_defect_to_named_families_closed=true；
early_zero_branch_unconditional_contradiction=false；
row_column_unconditional_closed=false。
```

证明要点如下。若 `1<=x<P` 是早期零行，则 CLB 分解给出 `R_x=F_x`。把它正式登记为同一个
formal unit：

```text
Omega=R_x；
tau(c)=q(c), 其中 x<q(c)<P 且 q(c)|xP+c；
w(c)=1；
physical_atom(c)=(c,q(c),m(c)), xP+c=q(c)m(c), m(c)>x。
```

这里 `m(c)>x` 来自 `c in R_x`：否则 `m(c)` 会有不超过 `x` 的素因子，使 `xP+c` 已被低骨架删去。
同一 formal unit 的短移自同构由全部活动标签相位保持决定。因为 `gcd(P,ell)=1`，条件
`dP=0 mod ell` 等价于 `ell|d`，所以短移集合由活动标签的 `lcm` 判定：

```text
Aut_short(S_x)={0<|d|<P : lcm(active labels)|d}。
```

若该集合非空，输出稳定短复现证书，并按固定列位移/端点复用进入 `ColumnCRT/SAE/PDEC` 吸收路线；
若为空，则输出 no-stable-automorphism 证书，`R_x=F_x` 被登记为一次性边界相位锁定缺陷。持久、
多原子、同口径、非二点且二秩以上的缺陷进入 `PDEC family`；孤立短窗或端点逃逸进入
`SAE/LocalSurvivorCert`；固定列位移先进入 `ColumnCRT` 并由位移 PDEC/SAE 吸收。

因此早期零行相位缺陷没有第四类未命名出口；但准入不是排斥。完全排斥早期零行时，新的早期零行
分支剩余是三类终端都要关闭的义务包：

```text
EarlyZeroTerminalExclusionPackage
  = EarlyZeroPrimitivePDECBudgetInequality
    AND EarlyZeroLocalSurvivorPacketOrSAEExclusion
    AND StableRecurrenceDisplacementPDECBudgetOrColumnSAEExclusion。
```

该 overlay 不改变当前 new-layer/DLS/source/DStructure 完全自足输入基；它只是把“P 行以内零行”
反例分支压入已有终端排斥义务。

继续新增：

```text
experiments/prime_matrix_early_zero_carry_shell_router.py
docs/monograph/prime-matrix-early-zero-carry-shell-router.md/json
```

该路由器继续攻击早期零行终端包中的 primitive PDEC 容量项。核心是把未完成高素斜线补洞从
“任意高素覆盖”压成一个精确的双高因子带进位壳。

若 `1<=x<P`，`c in R_x`，且该残洞被未完成高素斜线补掉，则

```text
xP+c = q m,   x<q<P。
```

由于 `c in R_x`，`xP+c` 没有不超过 `x` 的素因子，所以 `m>x`；又 `q>=x+1`，故

```text
m < (x+1)P/(x+1)=P。
```

令

```text
h=P-x,  q=P-a,  m=P-b,  k=floor(ab/P)。
```

则 `1<=a,b<h`，且

```text
(P-a)(P-b)=P(P-a-b+k)+(ab mod P)。
```

与 `xP+c=(P-h)P+c` 比较得到精确恒等式：

```text
h = a+b-k；
c = ab mod P；
k = floor(ab/P)。
```

这说明早期零行的高补洞支撑不再是任意列集合，而只能落在由 `h,k` 索引的有限 carry shell 上。
当 `h<sqrt(P)` 时，`ab<h^2<P`，所以 `k=0`，立即恢复底部带二次缺口曲线：

```text
a+b=h；
c=ab=a(h-a)。
```

样本审计 `P=101,499,997` 的全行高补洞原子均满足：

```text
all_factor_windows_ok=true；
all_carry_identities_ok=true；
all_bottom_bands_have_zero_carry=true。
```

该样本只用于防止口径错误；恒等式本身由代数比较证明。于是
`EarlyZeroPrimitivePDECBudgetInequality` 被进一步改写为：

```text
CarryShellPrimitiveCapacityBoundOrPDECReturn
  = CarryShellPrimitiveCapacityBound
    OR CarryShellPersistentConcentrationPDECReturn
    OR CarryShellSparseLocalSurvivorOrSAEReturn
    OR CarryShellDisplacementColumnCRTReturn。
```

新的最窄未闭合点是 `CarryShellPrimitiveCapacityBound`：证明每个 `h` 壳的双高因子可用列容量
不能吃掉整个 `R_x`，或者一旦吃掉就强制产生可排斥的 PDEC/SAE/ColumnCRT 证书。

继续新增：

```text
experiments/prime_matrix_early_zero_cofactor_depth_router.py
docs/monograph/prime-matrix-early-zero-cofactor-depth-router.md/json
```

该路由器修正并强化 carry-shell 口径：在恒等式

```text
xP+c=q m,   x<q<P,   x<m<P
```

中，`m=P-b` 是 `x`-rough cofactor，不必总是素数。由于 `c in R_x`，`m` 的每个素因子也都
大于 `x`。若 `Omega(m)=d` 是带重数素因子深度，则

```text
m > x^d,   m<P,   因而 d < log(P)/log(x)。
```

特别地，当 `x>=sqrt(P)` 时，复合 `m` 至少含两个大于 `x` 的素因子，于是

```text
m > x^2 >= P
```

矛盾。所以：

```text
x>=sqrt(P)  =>  m is prime。
```

这把 carry-shell 剩余分成两块：

```text
1. x>=sqrt(P)：真双素 carry-shell 容量；
2. x<sqrt(P)：复合 cofactor 的有限深度递归壳。
```

复合 cofactor 壳不是新出口。若这种壳在反例族中持久集中，它就是同 formal unit 的 PDEC 支撑；
若只孤立出现，则进入 `SAE/LocalSurvivor`。样本审计 `P=101,499,997` 验证所有复合 cofactor
都只出现在 `x<sqrt(P)`：

```text
all_composite_only_before_sqrt_gate=true。
```

于是上一轮剩余进一步拆成：

```text
PrimePairCarryShellCapacityAndCompositeCofactorDepthDescent
  = PrimePairCarryShellCapacityBoundOrPDECReturn
    AND CompositeCofactorDepthDescentOrNamedReturn
    AND EarlyBandLocalSurvivorOrSAEExclusion。
```

第一项处理 `x>=sqrt(P)` 的真双素壳，第二项处理 `x<sqrt(P)` 的复合 cofactor 递归壳，第三项处理
递归不能持久化时的孤窗证书。该步骤仍是结构压缩，不是最终容量排斥。

继续新增：

```text
experiments/prime_matrix_early_zero_anchor_collar_router.py
docs/monograph/prime-matrix-early-zero-anchor-collar-router.md/json
```

该路由器继续攻击 `x>=sqrt(P)` 的真双素 carry-shell。关键新刚性是 canonical 最小高素锚：

```text
xP+c=q m,   x<q,m<P,   q,m prime。
```

取 `q` 为最小高素因子，则 `q<=m`，所以

```text
q^2 <= xP+c < (x+1)P。
```

因此

```text
x < q < sqrt((x+1)P)。
```

这把原本的高素选择区间 `(x,P)` 压成窄的 canonical anchor collar。用 carry-shell 坐标看，
它等价于只取 `q<=m` 的半边，去掉 `q,m` 互换重复，平方点只计一次。

固定 collar 中的 `q` 后，`m` 必须落在短素数纤维：

```text
ceil((xP+1)/q) <= m <= floor((xP+P-1)/q),
m prime, q<=m<P。
```

该窗口长度严格小于 `P/q`，而 `q>x>=sqrt(P)`，所以每条 q-fiber 长度 `<sqrt(P)`。于是全覆盖压力
不能再表述为“高素很多”，而必须表述为很多极短素数纤维同时满载。

样本审计 `P=101,499,997` 验证所有 canonical anchors 均落入 collar：

```text
all_anchor_hits_in_collar=true。
```

并给出量级信号：

```text
P=101: max_fiber_load=2, max_primepair_share=0.500000；
P=499: max_fiber_load=4, max_primepair_share≈0.420290；
P=997: max_fiber_load=5, max_primepair_share≈0.413333。
```

因此 `PrimePairCarryShellCapacityBoundOrPDECReturn` 进一步压成：

```text
AnchorCollarPrimeFiberCapacityBoundOrPDECReturn
  = AnchorCollarShortPrimeFiberUpperBound
    AND NoPersistentAnchorFiberConcentrationPDEC
    AND NoSparseAnchorFiberSAE
    AND NoColumnDisplacementReuseInAnchorFibers。
```

真正未闭合的是 `AnchorCollarShortPrimeFiberUpperBound`：证明 collar 中所有短素数纤维的容量总和
不能吃掉整个 `R_x`；若某些纤维承担异常大负载，则已经进入 PDEC/SAE/ColumnCRT 命名回流。

条件输入基为：

```text
((ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn
  AND DPRCAlpha043CenteredDiscrepancyOrNamedLayerReturn
  AND SignedGeometricLedgerVariationBranchLiftAndReturn)
 OR CDependentResidueWeightSpectralCancellationInput)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

该步的实质推进是把“几何预算证书”拆成几何解析与 signed-source 绝对变差两个不可混淆的输入，避免继续
在 unsigned 覆盖图上误判 signed 预算已经闭合。

继续新增：

```text
experiments/prime_matrix_clean_core_dprc_centered_discrepancy_router.py
docs/monograph/prime-matrix-clean-core-dprc-centered-discrepancy-router.md/json
```

该路由器直接攻击 `DPRCAlpha043CenteredDiscrepancyOrNamedLayerReturn`。结论为：

```text
dprc_centered_discrepancy_boundary_closed=true；
rsm_identity_closed=true；
bes_compression_closed=true；
dprc_centered_discrepancy_input_proved=false；
row_column_unconditional_closed=false。
```

新的压缩律是：

```text
DPRCAlpha043CenteredDiscrepancyOrNamedLayerReturn
  => ExplicitModelGapAndFiniteDPRCLedger
     AND BESDangerIntersectionExclusionOrDLSNamedReturn。
```

RSM 恒等式把 `T_Y<S_Y` 写成模型余量和正偏差比较；BES 把正偏差平方根界写成六个 beta 桶的高正和与高能量
不能同步；DLS 则规定同步失败必须显化为 `PointLoad/ColumnCRT`、`ShortWindow/SAE` 或
`LowPhase/PDEC`，尤其新增轮层 Fourier 同步必须成为 new-layer PDEC，而不是无名低模异常。

最新完全自足输入基为：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn
AND ExplicitModelGapAndFiniteDPRCLedger
AND BESDangerIntersectionExclusionOrDLSNamedReturn
AND SignedGeometricLedgerVariationBranchLiftAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

条件输入基为：

```text
((ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn
  AND ExplicitModelGapAndFiniteDPRCLedger
  AND BESDangerIntersectionExclusionOrDLSNamedReturn
  AND SignedGeometricLedgerVariationBranchLiftAndReturn)
 OR CDependentResidueWeightSpectralCancellationInput)
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

该步把 DPRC 解析锁从原始容量不等式压成一个可独立验收的有限/模型余量账本和一个 BES-DLS 三出口结构命题。

继续新增：

```text
experiments/prime_matrix_clean_core_bes_dls_named_return_router.py
docs/monograph/prime-matrix-clean-core-bes-dls-named-return-router.md/json
```

该路由器直接攻击 `BESDangerIntersectionExclusionOrDLSNamedReturn`。结论为：

```text
bes_dls_named_return_boundary_closed=true；
dls_kernel_and_danger_algebra_closed=true；
bes_dls_named_return_input_proved=false；
row_column_unconditional_closed=false。
```

新的压缩律是：

```text
BESDangerIntersectionExclusionOrDLSNamedReturn
  => DLSPointLoadColumnCRTBoundOrNamedReturn
     AND DLSShortWindowSAEBoundOrNamedReturn
     AND DLSLowPhasePDECNewLayerOrFlatDLSBound。
```

中心化核、危险交集、尖峰桶鸽巢和二次能量展开已登记；若危险交集出现，它必须通过 `PointLoad`、
`ShortWindow` 或 `LowPhase` 支付。ColumnCRT 已被位移 PDEC/SAE 吸收，SAE 已被 LocalSurvivor/PDEC
吸收，LowPhase 已接入 W-unit/new-layer PDEC 与 flat DLS 二分。近危险审计显示最稳定结构信号是单位类内部
LowPhase，因此下一步最窄自足攻点是 `DLSLowPhasePDECNewLayerOrFlatDLSBound`。

最新完全自足输入基为：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn
AND ExplicitModelGapAndFiniteDPRCLedger
AND DLSPointLoadColumnCRTBoundOrNamedReturn
AND DLSShortWindowSAEBoundOrNamedReturn
AND DLSLowPhasePDECNewLayerOrFlatDLSBound
AND SignedGeometricLedgerVariationBranchLiftAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

该步删除了 BES-DLS 无名同步失败口子，但尚未证明三类微输入。

继续新增：

```text
experiments/prime_matrix_clean_core_dls_lowphase_pdec_flat_router.py
docs/monograph/prime-matrix-clean-core-dls-lowphase-pdec-flat-router.md/json
```

该路由器直接攻击 `DLSLowPhasePDECNewLayerOrFlatDLSBound`。结论为：

```text
dls_lowphase_boundary_closed=true；
lowphase_input_proved=false；
row_column_unconditional_closed=false。
```

新的压缩律是：

```text
DLSLowPhasePDECNewLayerOrFlatDLSBound
  => DLSFixedWheelUnitPeakDilutionOrPDECReturn
     AND DLSNewLayerFourierConcentrationPDECReturn
     AND DLSFlatHighModLargeSieveAbsorption。
```

固定轮单位类峰持续同步时回流 `W-unit PDEC`；新增 Fourier 频率低维集中时回流 `new-layer PDEC`；
二者都稀释时，剩余只允许作为高模平坦分散能量进入 `flat DLS/KLS`。层叠轮审计显示单单位类峰从
`W=30` 的 `1.076781` 降到 `W=2310` 的 `0.293727`，而 Fourier 继承分类显示强频率转入新增因子
`11` 层。这不是证明，但明确了下一步最窄攻点为 `DLSNewLayerFourierConcentrationPDECReturn`。

最新完全自足输入基为：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn
AND ExplicitModelGapAndFiniteDPRCLedger
AND DLSPointLoadColumnCRTBoundOrNamedReturn
AND DLSShortWindowSAEBoundOrNamedReturn
AND DLSFixedWheelUnitPeakDilutionOrPDECReturn
AND DLSNewLayerFourierConcentrationPDECReturn
AND DLSFlatHighModLargeSieveAbsorption
AND SignedGeometricLedgerVariationBranchLiftAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

继续新增：

```text
experiments/prime_matrix_clean_core_newlayer_external_lemma_match_router.py
docs/monograph/prime-matrix-clean-core-newlayer-external-lemma-match-router.md/json
```

该路由器把当前最窄 `DLSNewLayerFourierConcentrationPDECReturn` 与已经登记的外部闭合引理
`FullS-KLS-ext`、`CleanKLS/DLS` 准入表和 DI/BFI 主来源 no-go 逐项匹配。结论为：

```text
direct_external_lemma_closes_newlayer=false；
self_contained_newlayer_closed=false；
row_column_unconditional_closed=false。
```

核心结构律是：外部 KLS/FullS 引理只闭合已经完成、已经给定系数、已经通过 clean admission 的
平坦谱块；当前新增轮层子口还处在更早一层，必须先证明新增素因子 fiber 上的低维 Fourier 集中
确实给出 `new-layer PDEC` 证书，或者证明删除全部这类集中后，剩余对象满足 flat-KLS/DLS 的准入条件。
因此该子口被压成两个更原子的输入：

```text
DLSNewLayerFourierConcentrationPDECReturn
  => ExactNewLayerFiberPDECProjectionMorphism
     AND NewLayerNoConcentrationImpliesFlatAdmission。
```

参数匹配表显示六个不能跳过的差异：证明阶段不同、`r∤h` 新增频率尚未投影到 KLS 逆元变量、
系数平坦性必须先删除 PDEC 尖峰、FullS 合同中的 no-projection 不是 new-layer 低模单位 fiber 的
formal-unit 等式、BES 危险阈值需要命名回流兼容、现有 DI/BFI 主来源仍不能给出完全自足 full-S
non-AP KLS-ext。由此，下一步最窄自足目标不是继续寻找普通外部引用，而是直接证明：

```text
ExactNewLayerFiberPDECProjectionMorphism；
NewLayerNoConcentrationImpliesFlatAdmission。
```

更新后的完全自足输入基为：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn
AND ExplicitModelGapAndFiniteDPRCLedger
AND DLSPointLoadColumnCRTBoundOrNamedReturn
AND DLSShortWindowSAEBoundOrNamedReturn
AND DLSFixedWheelUnitPeakDilutionOrPDECReturn
AND ExactNewLayerFiberPDECProjectionMorphism
AND NewLayerNoConcentrationImpliesFlatAdmission
AND DLSFlatHighModLargeSieveAbsorption
AND SignedGeometricLedgerVariationBranchLiftAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

继续新增：

```text
experiments/prime_matrix_near_zero_mirror_contradiction_router.py
docs/monograph/prime-matrix-near-zero-mirror-contradiction-router.md/json
```

该路由器专门回顾“P 行以内非平凡零行 -> 下一个零行很近 -> 与 CRT 周期镜像对称矛盾”这条思路。
结论为：

```text
direct_contradiction_from_near_next_zero_and_mirror=false；
row_column_unconditional_closed=false；
retained_route=BoundaryPhaseNoncoverageOrStableRecurrencePDEC。
```

可保留的严格事实是：完整 CRT 行周期内零行集合关于周期中心镜像对称；若首零行为 `r0`，则跨周期
首尾镜像间隔为 `2r0-1`，所以 `r0<=P` 等价于边界出现 `<=2P-1` 的短间隔。但这不是独立矛盾，
而是目标命题的等价改写。

不能直接使用的跳步有三项。第一，从一个零行自动推出“下一个零行很近”没有已证机制；`P=23` 的
首零行 `59` 后首次复现为 `2612`，平移 `2553`，且 `118=2*59` 不是零行。第二，全局 `2P` 短复现
禁止为假；`P=23` 周期内部有多对间隔不超过 `2P` 的零行。第三，镜像递归不会自动给出更小素数
方阵零行；剥层会复活洞，`q^2-n` 反射落到早期区间时变成非零类终端块，而不是小方阵零行。

因此这条思路的可攻形式应改写为：

```text
EarlyZeroRowWithinP
  => StableShortRecurrencePDEC/SAE/ColumnCRT
     OR BoundaryPhaseNoncoverageFailure。
```

换言之，若能额外证明“早期零行必然强制稳定短复现”，则稳定性会进入同一 formal unit 的
`PDEC/SAE/ColumnCRT` 缺陷；若不能证明稳定性，就必须回到首端帽边界相位非覆盖和高素数补洞
CRT 最小代表延迟。该回顾不改变当前 new-layer/DLS/source 输入基。

继续新增：

```text
experiments/prime_matrix_conditional_early_zero_stability_router.py
docs/monograph/prime-matrix-conditional-early-zero-stability-router.md/json
```

该路由器不再用真实零行统计反推，而是在假设反例分支内证明条件稳定性二分。结论为：

```text
conditional_lemma_proved=true；
stable_recurrence_forced_unconditionally=false；
phase_defect_forced_if_no_stable_recurrence=true；
row_column_unconditional_closed=false。
```

条件引理为：

```text
EarlyZeroRowWithinP
  => StableShortRecurrence
     OR BoundaryPhaseNoncoverageDefectSameFormalUnit。
```

证明骨架如下。假设 `1<=x<P` 且第 `x` 条边界行 `xP+c,1<=c<P` 是零行。由 CLB 分解，
低斜线留下 `R_x`，高斜线只在 `R_x` 内补洞；零行等价于 `U_x=R_x\F_x` 为空，即 `R_x=F_x`。
于是可用 `Omega=R_x`、补洞标签 `tau(c)=q(c)`、权重 `w(c)=1` 固定同一个 formal unit。
若存在非零短移 `d` 保持全部必要标签相位，则同一覆盖证书在 `x+d` 行稳定复现。若不存在这种短移，
则该早期零行不能由稳定轨道解释，只能是高素数补洞标签在 `R_x` 上一次性锁定全部残洞的边界相位缺陷。

因此你的思路在反例分支内可以闭合成一个严格二分；但要把它变成最终矛盾，还必须补：

```text
EarlyZeroPhaseDefectSchemaAdmission
  = RegisteredSameFormalUnitRxFxLedger
    AND StableShortRecurrenceCertificateOrNoStableAutomorphism
    AND BoundaryPhaseNoncoverageDefectToPDECOrSAEOrColumnCRT。
```

也就是说，下一步不再是证明“真实零行是否短复现”，而是把假设早期零行产生的
`BoundaryPhaseNoncoverageDefectSameFormalUnit` 完整登记为可验收的 `PDEC/SAE/ColumnCRT` 证书字段。

继续新增：

```text
experiments/prime_matrix_clean_core_newlayer_pdec_projection_router.py
docs/monograph/prime-matrix-clean-core-newlayer-pdec-projection-router.md/json
```

该路由器直接攻击 `ExactNewLayerFiberPDECProjectionMorphism`。结论为：

```text
newlayer_projection_slicer_closed_schema_admission_open；
exact_newlayer_projection_morphism_closed=false；
row_column_unconditional_closed=false。
```

本步真正压下了两个结构硬点：

```text
SameCPProjectionMonotonicity=true；
FourierToFiberCapSlicer=true。
```

第一，同一全周期完成集合 `C_P` 下，`Q -> rQ` 升层不会在旧投影支撑外产生新支撑；
第二，在新增 fiber 上若有强 `r∤h` Fourier 系数，旋转相位并用层蛋糕分解，必能切出一个循环弧/
半平面 cap，其质量偏差至少为该 Fourier 强度的绝对常数倍。这是有限群 Fourier 对偶，不是概率实验。

因此：

```text
ExactNewLayerFiberPDECProjectionMorphism
  => RegisteredNewLayerPDECFormalUnitAndCapStableSchema。
```

剩余已经不是“能否从 Fourier 看见 PDEC”这一几何问题，而是正式准入问题：必须固定同一个
`Omega,tau,w` 和相位图，证明该 new-layer cap 非二点 tautology、非 ColumnCRT/SAE 复用、二秩以上且
cap-stable，并且 PDEC 下界与 CRT 上界按同一 formal unit 计量。

更新后的完全自足输入基为：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn
AND ExplicitModelGapAndFiniteDPRCLedger
AND DLSPointLoadColumnCRTBoundOrNamedReturn
AND DLSShortWindowSAEBoundOrNamedReturn
AND DLSFixedWheelUnitPeakDilutionOrPDECReturn
AND RegisteredNewLayerPDECFormalUnitAndCapStableSchema
AND NewLayerNoConcentrationImpliesFlatAdmission
AND DLSFlatHighModLargeSieveAbsorption
AND SignedGeometricLedgerVariationBranchLiftAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

继续新增：

```text
experiments/prime_matrix_early_zero_contradiction_matrix_router.py
docs/monograph/prime-matrix-early-zero-contradiction-matrix-router.md/json
```

该路由器把“假设早期零行存在”与当前已有成果逐项对齐，形成早期零行矛盾矩阵。结论为：

```text
direct_unconditional_contradiction_found=false；
no_unnamed_exit_for_early_zero=true；
row_column_unconditional_closed=false；
strongest_current_frontier=AnchorCollarPrimeFiberCapacityBoundOrPDECReturn。
```

目前可确定的严格结构是：早期零行不再能作为自由斜线覆盖现象存在。它必须同时通过八个夹击面：

```text
CLB residual-filler front；
same-formal-unit front；
carry-shell front；
cofactor-depth front；
anchor-collar short-fiber front；
mirror-stability front；
P-column layered-wheel front；
terminal no-fourth-exit front。
```

这些夹击面的合成链为：

```text
EarlyZeroRowWithinP
  => CLB residual equality R_x=F_x
  => same-formal-unit phase ledger
  => ExactCarryShellIdentity
  => CofactorDepth split
  => CanonicalAnchorCollar short prime fibers for x>=sqrt(P)
  => AnchorCollar capacity deficit OR PDEC/SAE/ColumnCRT named return。
```

因此，若早期零行存在，它会与以下已登记成果发生条件性冲突。第一，CLB 要求剩余洞与补洞容量比较，
早期零行强制 `R_x=F_x`。第二，formal unit 准入禁止跨窗口、跨 q 层或跨重复口径随意拼接补洞。
第三，carry-shell 恒等式把每个高补洞限制到
`h=a+b-floor(ab/P), c=ab mod P`。第四，cofactor 深度门说明 `x>=sqrt(P)` 时 cofactor 必为素数，
复合 cofactor 只能留在浅层递归壳。第五，canonical anchor collar 把真双素分支压到
`x<q<sqrt((x+1)P)`，固定锚后的素数纤维长度 `<sqrt(P)`。第六，镜像对称不能直接给矛盾，
只能路由到稳定复现缺陷或边界相位缺陷。第七，P 列锚与层叠轮要求补洞支付进入同一
`Phi/payment` 字母表。第八，集中、孤立和固定列位移复用都已经进入 `PDEC/SAE/ColumnCRT`
命名终端。

不可再直接作为终局矛盾的路线也被明确登记：真实样本中未见早期零行不能替代反例分支证明；
完整 CRT 镜像对称只给等价边界短间隔；从一个零行自动推出下一个零行很近没有已证机制；
`P^2±k` 或层叠轮同余刚性只限制补洞通道，单独还不是容量排斥。

剩余闭合包保持为：

```text
AnchorCollarShortPrimeFiberUpperBound
AND CompositeCofactorDepthDescentOrNamedReturn
AND EarlyBandLocalSurvivorOrSAEExclusion
AND PrimitivePDECBudgetForPersistentConcentration
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

其中当前最窄优先级是 `AnchorCollarPrimeFiberCapacityBoundOrPDECReturn`：证明 anchor collar
中所有长度 `<sqrt(P)` 的短素数纤维总容量不能覆盖整个 `R_x`，或证明任何覆盖级过载都会进入
已命名且可排斥的 `PDEC/SAE/ColumnCRT`。

继续新增：

```text
experiments/prime_matrix_anchor_collar_survivor_identity_router.py
docs/monograph/prime-matrix-anchor-collar-survivor-identity-router.md/json
```

该路由器直接攻击 `AnchorCollarShortPrimeFiberUpperBound` 的本质。结论为：

```text
anchor_collar_survivor_identity_closed=true；
capacity_gap_equals_prime_survivors_closed=true；
anchor_collar_short_fiber_capacity_closed=false；
row_column_unconditional_closed=false；
terminal_gap_after_router=PrimeSurvivorLowerBoundOrPDECSAEColumnReturn。
```

核心恒等式如下。对 `sqrt(P)<=x<P`，令 `R_x` 为第 `x` 行中没有 `<=x` 素因子的列。由于
`xP+c<(x+1)P<=P^2`，任一 `c in R_x` 只有两种可能：

```text
xP+c is prime；
xP+c=q m,  x<q<=m<P,  q,m prime。
```

第二种正是 canonical anchor-collar 短纤维的精确支撑，因此：

```text
R_x = PrimeSurvivors_x disjoint_union SemiprimeFibers_x；
|R_x|-|SemiprimeFibers_x| = |PrimeSurvivors_x|。
```

这一步的意义是双重的。第一，短纤维容量硬点没有留下隐藏的计数松弛：

```text
AnchorCollarShortPrimeFiberUpperBound
  <=> PrimeSurvivors_x>0 on every sqrt(P)<=x<P row。
```

第二，继续直接数 q-fiber 总容量不能绕开短区间素数屏障；真正可继续硬攻的非循环方向变成变量行维数差：

```text
G_x(P)=#R_x                       一维粗骨架；
B_x(P)=#SemiprimeFibers_x          二维素对纤维；
PrimeSurvivors_x=G_x(P)-B_x(P)。
```

若能证明 `G_x(P)>B_x(P)`，则该行闭合；若失败，则失败必须表现为低模骨架亏损、素对纤维过密、
孤立幸存者逃逸或固定列位移复用，并分别回流 `PDEC/SAE/ColumnCRT`。

样本审计只验证实现口径；恒等式由唯一分解和 `x>=sqrt(P)` 直接证明。默认样本给出：

```text
all_identity_holds=true；
all_sqrt_gate_clean=true；
all_anchor_collar_clean=true；
P=101,499,997,1999 的最小素数幸存数分别为 7,29,54,110。
```

新的最窄剩余压成：

```text
PrimeSurvivorLowerBoundOrPDECSAEColumnReturn
  = VariableRowRoughSkeletonLowerBound
    AND VariableRowPrimePairFiberUpperBound
    AND PrimeFreeIntervalLowModPDECDefectReturn
    AND SparsePrimeSurvivorOrLocalSAEExclusion
    AND ColumnDisplacementReusePDECReturn。
```

这一步不是终局闭合；它把 anchor-collar 的容量语言压成了精确的素数幸存/维数差语言。

继续新增：

```text
experiments/prime_matrix_variable_row_dimension_gap_router.py
docs/monograph/prime-matrix-variable-row-dimension-gap-router.md/json
```

该路由器直接攻击变量行维数差 `G_x(P)>B_x(P)`。结论为：

```text
variable_row_dimension_gap_identity_closed=true；
endpoint_dimension_gap_uniform_lift_rejected=true；
uniform_dimension_gap_constants_proved=false；
row_column_unconditional_closed=false；
terminal_gap_after_router=AlignedPrimeMainBuchstabBranchLowerBoundOrDefectReturn。
```

对 `sqrt(P)<=x<P`，精确公式为：

```text
G_x(P)=#R_x；
B_x(P)=#SemiprimeFibers_x；
PrimeSurvivors_x=G_x(P)-B_x(P)。
```

双素纤维也有精确求和式：

```text
B_x(P)=sum_{q prime, x<q<=sqrt((x+1)P)}
  #{m prime: max(q,ceil((xP+1)/q))<=m<=floor((xP+P-1)/q)}。
```

本步排除了一个危险捷径：不能把对角端点 `x=P` 的维数差常数合同直接外推到全部变量行。
端点中双素覆盖被三条倒数地板曲线压到 `P/log^2 P` 型对象；但在变量行，尤其
`x≈sqrt(P)` 时，collar 中的 `m` 窗口长度可达 `sqrt(P)`，双素纤维仍有 `P/log P`
量级，与粗骨架同阶。因此端点维数差是 `alpha=1` 的退化口，不是 `alpha in [1/2,1]`
的统一证明。

已经闭合的结构门为：

```text
PrimeSurvivorIdentityImported；
ExactVariableFiberFormula；
EndpointDimensionGapDoesNotUniformlyLift；
TwoBranchSupportShape；
EndpointContractCompatibility；
EDADualCompatibility。
```

其中 `TwoBranchSupportShape` 是严格支撑事实：因 `x>=sqrt(P)` 且 `xP+c<P^2`，`R_x` 的合数
只能有两个 `>x` 素因子；支撑上只有一素分支与双素分支。尚未闭合的是：

```text
UniformBuchstabConstants；
UniformDimensionGapConstants。
```

样本只用于定位危险区间；默认审计给出：

```text
all_identity_holds=true；
global_min_prime=7；
global_max_semiprime_share=0.500000。
```

分桶读数显示危险最大处在 `alpha=log x/log P` 接近 `0.5` 的平方根带；随着 `alpha` 接近 `1`，
双素纤维占比下降，端点合同逐渐接管。这说明下一步不能继续攻击端点三曲线，而应直接攻击
统一的一素分支正性或缺陷回流。

新的最窄剩余为：

```text
AlignedPrimeMainBuchstabBranchLowerBoundOrDefectReturn
  = UniformBuchstabOnePrimeBranchLowerBound
    AND VariableRowRoughSkeletonLowerBound
    AND VariableRowPrimePairFiberUpperBound
    AND LowModSkeletonDeficitPDEC
    AND PrimePairFiberConcentrationTailPDEC
    AND SparsePrimeSurvivorSAE
    AND ColumnDisplacementReusePDEC。
```

含义是：若不能直接证明每行一素分支为正，就必须把失败转成同 formal unit 的低模亏损、
素对纤维集中、孤立幸存者逃逸或固定列位移复用。该路由仍未给出无条件闭合。

继续新增：

```text
experiments/prime_matrix_aligned_prime_main_defect_router.py
docs/monograph/prime-matrix-aligned-prime-main-defect-router.md/json
```

该路由器直接攻击 `UniformBuchstabOnePrimeBranchLowerBound`。结论为：

```text
prime_free_row_to_edabk_defect_closed=true；
buchstab_constants_standalone_rejected=true；
lowmod_tail_defect_exclusions_closed=false；
row_column_unconditional_closed=false；
terminal_gap_after_router=LowModTailCoreDefectExclusionPackage。
```

精确二分链为：

```text
PrimeSurvivors_x=0
=> EDA failure at the same aligned row x
=> positive-main endpoint defect by EDA-BK
=> LowMod endpoint CRTDefect OR Tail/Core concentration
=> named PDEC/SAE/ColumnCRT/Tail-anchor exits; no unnamed Buchstab exit。
```

这一步关闭了一个概念出口：`Buchstab` 常数本身不能作为终局证明。正主项为正只说明若行为空，
必须产生端点缺陷或尾项集中；它本身不排斥这些缺陷。已闭合的门为：

```text
VariableRowDimensionGapImported；
PrimeFreeRowImpliesEDAFailure；
PositiveMainEndpointDefectImported；
BuchstabConstantsNotStandalone；
BKDECBridgeCompatibility；
TailCoreBucketCompatibility；
DirectedEndpointDefectSchema。
```

其中 `PrimeFreeRowImpliesEDAFailure` 说明 `sqrt(P)<=x<P` 的一素分支为零就是同一对齐行的
`EDA` 失败；`PositiveMainEndpointDefectImported` 由 `EDA-BK` 给出正主项端点缺陷二分；
`BKDECBridgeCompatibility` 与 `TailCoreBucketCompatibility` 说明 LowMod 与 Tail 失败已经分别
接到 Directed Endpoint CRTDefect 与 TailCore/Tail-anchor 命名对象。

唯一开放门为：

```text
LowModAndTailExclusion。
```

新的最窄剩余是：

```text
LowModTailCoreDefectExclusionPackage
  = LowModEndpointCRTDefectExclusionOrPDEC
    AND TailCoreConcentrationAbsorptionOrTailAnchorPDEC
    AND SparseSingleWindowSAEExclusion
    AND ColumnDisplacementReusePDEC
    AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

这一步仍不是无条件闭合；它把“证明一素分支正性”的任务改写为两个命名出口的排斥任务。

继续新增：

```text
experiments/prime_matrix_lowmod_endpoint_formal_unit_router.py
docs/monograph/prime-matrix-lowmod-endpoint-formal-unit-router.md/json
```

该路由器直接攻击 `LowModEndpointCRTDefectExclusionOrPDEC` 的准入纪律。结论为：

```text
lowmod_formal_unit_admission_boundary_closed=true；
current_pdec_zero_not_future_exclusion=true；
lowmod_endpoint_exclusion_closed=false；
row_column_unconditional_closed=false；
terminal_gap_after_router=LowModFuturePDECSchemaExclusionOrSparseSAE。
```

LowMod endpoint formal unit 的形状被固定为：

```text
Omega        = bad aligned rows x triggering the same LowMod block B and sign；
phase_map    = x mod Q_B, where Q_B=lcm(d: d in B)；
test_function= f_B(x)=sum_{d in B} mu(d) epsilon_d(x)；
bad_set      = S={x: sign*f_B(x)>=kappa_B}。
```

关键纪律是：单点 LowMod 端点尖峰不是矛盾；完整 CRT 周期零均值不能排除一个短窗口尖峰。
只有同一低模块、同一符号、同一相位图上的坏行集合，才能形成可审查的 persistent PDEC 输入。
若坏行在同一低模块上持续出现：

```text
|S|>=beta Q_B
=> nonzero Fourier defect
=> future primitive PDEC schema。
```

若坏行只稀疏出现：

```text
|S| small
=> SAE/local survivor or endpoint escape exclusion。
```

本步同时排除一个错误跳步：

```text
错误：LowMod endpoint CRTDefect 出现
   => 当前 PDEC 候选为零
   => 矛盾。

正确：LowMod endpoint CRTDefect 出现
   => future explicit PDEC schema 或 sparse SAE。
```

当前 PDEC family 边界只清零现有已物化候选；反例假设若产生新的 LowMod formal unit，仍必须提交
同 formal unit、非二点、二秩以上、cap-stable 的完整字段，然后再证明 `U_CRT<L_PDEC`。

已经闭合的门为：

```text
LowModBranchImported；
FiniteLowModSawtoothUnit；
PersistentSparseDichotomyImported；
PersistentToFourierDefect；
ExplicitPDECSchemaDiscipline；
LowRankColumnSparseAbsorption；
CurrentMaterializedPDECCandidatesDoNotExcludeFutureLowMod。
```

唯一开放门为：

```text
LowModEndpointExclusion。
```

新的最窄剩余为：

```text
LowModFuturePDECSchemaExclusionOrSparseSAE
  = PersistentLowModPrimitivePDECSchemaAdmission
    AND PersistentLowModPDECInequality_UCRT_LT_LPDEC
    AND SparseLowModSAELocalSurvivorExclusion
    AND LowRankOrColumnDisplacementAbsorption
    AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

这一步仍不是无条件闭合；它把 LowMod 分支从泛称出口压成 future PDEC schema 与 sparse SAE 两个可验收输入。

## Prime Matrix LowMod PDEC 容量失败定位路由器

对应新增文件：

```text
experiments/prime_matrix_lowmod_pdec_capacity_failure_router.py
docs/monograph/prime-matrix-lowmod-pdec-capacity-failure-router.md/json
```

该路由器直接攻击 `PersistentLowModPDECInequality_UCRT_LT_LPDEC`。结论为：

```text
lowmod_same_set_capacity_protocol_closed=true；
lowmod_capacity_multiplier_discipline_closed=true；
lowmod_pdec_inequality_closed=false；
row_column_unconditional_closed=false；
terminal_gap_before_router=PersistentLowModPDECInequality_UCRT_LT_LPDEC；
terminal_gap_after_router=LowModFiniteArcDualCapStabilityOrSparseSAE；
new_atomic_input=FiniteCyclicArcCapMassBoundsForFutureLowModPrimitiveSchemas。
```

失败见证形状被固定为：

```text
formal_unit  = G_B=Z/Q_BZ with phase x mod Q_B；
bad_count    = g_B(t)=1_{sign*f_B(t)>=kappa_B} 或对应 multiplicity count；
lower_bound  = L_lowmod=kappa_B*beta/(sqrt(Q_B-1)*||f_B||_2)；
dual_success = U_CRT(G_B,g_B)<L_lowmod 排除 persistent LowMod PDEC；
dual_failure = 存在非平凡字符 h 与有限循环弧 A，
               使 g_B(A)>=(L-alpha M)/(1-alpha)；
named_returns= Sparse SAE / displacement ColumnCRT / refined PDEC /
               new-layer PDEC / CleanKLS。
```

本步的结构律是逆否定位：若同一 LowMod formal unit 上的 `U_CRT<L_PDEC` 不能成立，
失败不能停留为抽象容量缺口，必须显化为有限循环弧 `LowModDualCap(B,h,zeta,alpha)`。
固定 `Q_B` 后，方向帽只是有限字符循环弧预像，所以连续 `zeta/alpha` 搜索退路被消掉。

已经闭合的门为：

```text
LowModFuturePDECImported；
SameFormalUnitPinned；
PDECLowerBoundImported；
SameSetDualCertificateProtocolRegistered；
MultiplierDisciplineNoEscape；
CapLocalizationFailureOutput；
FiniteArcBasisForLowModCaps；
SparseLowRankColumnReturn；
PersistentCapNoSameLayerCycle。
```

唯一开放门为：

```text
PersistentLowModPDECInequality。
```

新的最窄剩余为：

```text
PersistentLowModPDECInequality_UCRT_LT_LPDEC
  <= same formal unit PDEC lower bound
     + same-set dual protocol
     + finite cyclic-arc DualCap localization
     + named return absorption
     + FiniteCyclicArcCapMassBoundsForFutureLowModPrimitiveSchemas。
```

其中前四项已经由现有材料和本路由器接线；最后一项仍未证明。
这一步仍不是无条件闭合；它排除了“PDEC 不等式失败但不给结构见证”的无名出口，
把下一步推进目标压到未来 LowMod primitive schema 的全局有限弧 cap 质量界。

## Prime Matrix LowMod 有限弧 cap 归约路由器

对应新增文件：

```text
experiments/prime_matrix_lowmod_finite_arc_cap_reduction_router.py
docs/monograph/prime-matrix-lowmod-finite-arc-cap-reduction-router.md/json
```

该路由器继续攻击 `FiniteCyclicArcCapMassBoundsForFutureLowModPrimitiveSchemas`。结论为：

```text
lowmod_finite_arc_independent_input_removed=true；
lowmod_finite_arc_cap_mass_bounds_closed=false；
lowphase_three_micro_inputs_proved=false；
row_column_unconditional_closed=false；
terminal_gap_before_router=FiniteCyclicArcCapMassBoundsForFutureLowModPrimitiveSchemas；
terminal_gap_after_router=LowPhaseThreeMicroInputsOrExplicitLowModDualCapReturn。
```

归约映射为：

```text
fixed_wheel_arc      -> DLSFixedWheelUnitPeakDilutionOrPDECReturn；
new_layer_arc        -> DLSNewLayerFourierConcentrationPDECReturn；
high_mod_flat_arc    -> DLSFlatHighModLargeSieveAbsorption；
sparse_or_displacement -> SAE finite packet or ColumnCRT-as-PDEC。
```

结构律是：LowMod 有限循环弧 cap 是有限签名空间中的非平凡字符秩一薄片，不是新的平行终端。
固定轮单位类峰、升层新增 Fourier 峰、剥离后的高模平坦残余，分别落入既有 LowPhase/DLS
三微输入；低支撑、孤窗和列位移弧帽则回流 SAE 或 ColumnCRT-as-PDEC。

已经闭合的门为：

```text
LowModFiniteArcInputPinned；
FiniteArcIsRankOneLowPhaseSlice；
LayeredWheelClampAvailable；
FourierInheritanceClassifiesNewLayer；
NewLayerEnergyDispersionAvailable；
NewLayerTowerNoUnnamedEscape；
SparseColumnNamedReturnsPreserved；
LowPhaseSharedMicroInputsImported。
```

唯一开放门为：

```text
LowModFiniteArcCapMassBoundsClosed。
```

新的最窄剩余不再是独立 LowMod 输入，而是：

```text
FiniteCyclicArcCapMassBoundsForFutureLowModPrimitiveSchemas
  -> DLSFixedWheelUnitPeakDilutionOrPDECReturn
     AND DLSNewLayerFourierConcentrationPDECReturn
     AND DLSFlatHighModLargeSieveAbsorption
  or explicit LowModDualCap return to SAE/ColumnCRT/refined PDEC。
```

这一步仍不是终端证明；它关闭的是输入分类边界，说明 LowMod 有限弧 cap 不再额外增加一个
独立开放原子。真正要继续硬攻的是 LowPhase 三微输入，或对具体 LowModDualCap 抽取回流证书。

## Prime Matrix LowMod-new-layer 桥接路由器

对应新增文件：

```text
experiments/prime_matrix_lowmod_newlayer_bridge_router.py
docs/monograph/prime-matrix-lowmod-newlayer-bridge-router.md/json
```

该路由器把 LowMod 有限弧路径中的新增层子口接入既有 new-layer 投影切片链。结论为：

```text
lowmod_newlayer_bridge_closed=true；
newlayer_schema_proved=false；
newlayer_flat_admission_proved=false；
row_column_unconditional_closed=false；
terminal_gap_before_router=DLSNewLayerFourierConcentrationPDECReturn；
terminal_gap_after_router=RegisteredNewLayerPDECFormalUnitAndCapStableSchema_AND_NewLayerNoConcentrationImpliesFlatAdmission。
```

替换律为：

```text
DLSNewLayerFourierConcentrationPDECReturn
  =>
RegisteredNewLayerPDECFormalUnitAndCapStableSchema
AND NewLayerNoConcentrationImpliesFlatAdmission。
```

结构含义是：强新增层 Fourier 集中若存在，必须通过确定性切片形成同 formal unit 的 PDEC cap；
若不存在可登记的低维集中，则剩余对象必须满足 flat-DLS/KLS 准入，而不能停在“无集中”这句话上。

已经闭合的门为：

```text
LowModFiniteArcReducedToLowPhase；
LowPhaseNewLayerAtomPinned；
ExternalLemmaDirectShortcutRejected；
ProjectionSlicerClosedToSchema；
NewLayerAtomBridgeClosed。
```

唯一开放门为：

```text
NewLayerSchemaAndFlatAdmissionStillOpen。
```

更新后的完全自足输入基为：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn
AND ExplicitModelGapAndFiniteDPRCLedger
AND DLSPointLoadColumnCRTBoundOrNamedReturn
AND DLSShortWindowSAEBoundOrNamedReturn
AND DLSFixedWheelUnitPeakDilutionOrPDECReturn
AND RegisteredNewLayerPDECFormalUnitAndCapStableSchema
AND NewLayerNoConcentrationImpliesFlatAdmission
AND DLSFlatHighModLargeSieveAbsorption
AND SignedGeometricLedgerVariationBranchLiftAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

下一步最窄优先目标为 `RegisteredNewLayerPDECFormalUnitAndCapStableSchema`。这一步仍不闭合行/列
无条件命题；它只关闭 LowMod 有限弧路径与 new-layer 子口之间的接线缺口。

## Prime Matrix new-layer PDEC schema 准入路由器

对应新增文件：

```text
experiments/prime_matrix_newlayer_pdec_schema_admission_router.py
docs/monograph/prime-matrix-newlayer-pdec-schema-admission-router.md/json
```

该路由器直接攻击 `RegisteredNewLayerPDECFormalUnitAndCapStableSchema`。结论为：

```text
newlayer_schema_admission_closed=true；
registered_same_formal_unit_omega_tau_weight=true；
lowrank_column_sparse_return_closed=true；
cap_unstable_return_closed=true；
newlayer_ranktwo_budget_ledger_closed=false；
row_column_unconditional_closed=false；
terminal_gap_before_router=RegisteredNewLayerPDECFormalUnitAndCapStableSchema；
terminal_gap_after_router=NewLayerRankTwoCapStablePDECBudgetLedger。
```

new-layer formal unit 字段被固定为：

```text
Omega     = Omega'_A=A x F_r inside the same C_P projection tower；
phase_map = (old phase on W0, new fiber residue b mod r)；
weight    = w_A(b)=centered signed fiber mass delta_A(b)，
            or count weight for positive cap；
cap       = B subset F_r or cyclic arc preimage selected by FourierToFiberCapSlicer；
invalid   = Multiplicity/Stitching, SAE, ColumnCRT, or refined PDEC。
```

替换律为：

```text
RegisteredNewLayerPDECFormalUnitAndCapStableSchema
  => NewLayerRankTwoCapStablePDECBudgetLedger。
```

准入层只负责把对象登记成合法证书，或把非法情形回流到命名出口；它不证明最终预算不等式。

已经闭合的门为：

```text
NewLayerSchemaInputImported；
SameCPProjectionFormalUnitAvailable；
RegisteredSameFormalUnitOmegaTauWeight；
FormalUnitMismatchNamedReturn；
PrimitiveAdmissionBoundaryInherited；
LowRankAndColumnCasesNamed；
CapUnstableCasesNamed；
NewLayerSchemaAdmissionClosed。
```

唯一开放门为：

```text
NewLayerRankTwoCapStablePDECBudgetLedger。
```

更新后的完全自足输入基为：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn
AND ExplicitModelGapAndFiniteDPRCLedger
AND DLSPointLoadColumnCRTBoundOrNamedReturn
AND DLSShortWindowSAEBoundOrNamedReturn
AND DLSFixedWheelUnitPeakDilutionOrPDECReturn
AND NewLayerRankTwoCapStablePDECBudgetLedger
AND NewLayerNoConcentrationImpliesFlatAdmission
AND DLSFlatHighModLargeSieveAbsorption
AND SignedGeometricLedgerVariationBranchLiftAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

下一步最窄目标更新为 `NewLayerRankTwoCapStablePDECBudgetLedger`。这一步仍不是行/列无条件闭合；
它把 new-layer 集中支的准入问题压成真正的同单位预算账本。

## Prime Matrix new-layer 二秩预算账本路由器

对应新增文件：

```text
experiments/prime_matrix_newlayer_ranktwo_budget_ledger_router.py
docs/monograph/prime-matrix-newlayer-ranktwo-budget-ledger-router.md/json
```

该路由器直接攻击 `NewLayerRankTwoCapStablePDECBudgetLedger`。结论为：

```text
newlayer_ranktwo_budget_ledger_reduced=true；
newlayer_ranktwo_budget_independent_input_removed=true；
newlayer_pdec_budget_inequality_unconditionally_proved=false；
newlayer_no_concentration_flat_admission_proved=false；
row_column_unconditional_closed=false；
terminal_gap_before_router=NewLayerRankTwoCapStablePDECBudgetLedger；
terminal_gap_after_router=NewLayerNoConcentrationImpliesFlatAdmission。
```

核心结构不是数值估计，而是同一 formal unit 上的逆否路由：

```text
NewLayerRankTwoCapStablePDECBudgetLedger
  same formal unit Omega'_A=A x F_r；
  if U_CRT >= L_PDEC:
    cap localization gives a finite cyclic arc cap；
    old-axis cap   => old PDEC / ColumnCRT / SAE return；
    new-fiber cap  => new-layer PDEC cap or flat residual；
    mixed-axis cap => transverse split, then named return or flat residual；
  therefore no independent budget-ledger terminal remains。
```

方向分裂为：

```text
old_axis       -> projection to old formal unit; old PDEC/ColumnCRT/SAE return；
new_fiber_axis -> fiber residue b mod r; new-layer cap or flat admission；
mixed_axis     -> finite character arc in A x F_r; transverse split then flat admission。
```

替换律为：

```text
NewLayerRankTwoCapStablePDECBudgetLedger
  => absorbed by named cap returns OR NewLayerNoConcentrationImpliesFlatAdmission。
```

注意：这一步删除的是独立预算账本原子，不是宣称 new-layer flat admission 已经完成。

已经闭合的门为：

```text
NewLayerRankTwoBudgetInputActive；
SameFormalUnitBudgetLedgerRegistered；
RankTwoCapLocalizationImported；
UniformFiniteArcBasisImported；
ProductCharacterDirectionSplit；
FiniteArcTransverseTrichotomyInherited；
TransverseFlatResidualUsesNewLayerFlatGate；
NoCycleAndNamedReturnPreserved；
NewLayerRankTwoBudgetIndependentGateRemoved。
```

唯一开放门为：

```text
NewLayerNoConcentrationImpliesFlatAdmission。
```

更新后的完全自足输入基为：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn
AND ExplicitModelGapAndFiniteDPRCLedger
AND DLSPointLoadColumnCRTBoundOrNamedReturn
AND DLSShortWindowSAEBoundOrNamedReturn
AND DLSFixedWheelUnitPeakDilutionOrPDECReturn
AND NewLayerNoConcentrationImpliesFlatAdmission
AND DLSFlatHighModLargeSieveAbsorption
AND SignedGeometricLedgerVariationBranchLiftAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

下一步最窄目标更新为 `NewLayerNoConcentrationImpliesFlatAdmission`。必须证明：删除/回流所有可登记
PDEC cap 后，剩余新增层对象确实满足 flat-DLS/KLS 准入；否则必须输出新的命名
PDEC/SAE/ColumnCRT/multiplicity 证书。

## Prime Matrix new-layer 无集中 flat 准入路由器

对应新增文件：

```text
experiments/prime_matrix_newlayer_no_concentration_flat_admission_router.py
docs/monograph/prime-matrix-newlayer-no-concentration-flat-admission-router.md/json
```

该路由器直接攻击 `NewLayerNoConcentrationImpliesFlatAdmission`。结论为：

```text
newlayer_no_concentration_flat_admission_boundary_closed=true；
newlayer_no_concentration_independent_input_removed=true；
dls_flat_highmod_large_sieve_absorption_proved=false；
row_column_unconditional_closed=false；
terminal_gap_before_router=NewLayerNoConcentrationImpliesFlatAdmission；
terminal_gap_after_router=DLSFlatHighModLargeSieveAbsorption。
```

Admission 逆否律为：

```text
NewLayerNoConcentrationImpliesFlatAdmission
  means all registered low-dimensional defects have been removed:
    finite arc PDEC cap, short-window SAE, column/Bohr cap,
    promotable top-prime residue, phase-residue mutual information；
  any failure of K1--K9 returns to a named gate；
  all K1--K9 passed residual enters DLSFlatHighModLargeSieveAbsorption。
```

替换律为：

```text
NewLayerNoConcentrationImpliesFlatAdmission
  => DLSFlatHighModLargeSieveAbsorption admission gate already present。
```

注意：本步只证明 flat admission 边界，不证明 flat 大筛吸收界。

已经闭合的门为：

```text
NewLayerNoConcentrationGateActive；
CleanKLSAdmissionContractRegistered；
LowPhasePointShortFlatContextInherited；
NoConcentrationDefinitionPinned；
K1ToK9RegisteredOrRouted；
LowModL2MIFlatnessFromNoConcentration；
NamedFailureReturnDisciplinePreserved；
FlatDLSInterfaceReady；
NewLayerNoConcentrationFlatAdmissionBoundaryClosed。
```

唯一开放门为：

```text
DLSFlatHighModLargeSieveAbsorption。
```

更新后的完全自足输入基为：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn
AND ExplicitModelGapAndFiniteDPRCLedger
AND DLSPointLoadColumnCRTBoundOrNamedReturn
AND DLSShortWindowSAEBoundOrNamedReturn
AND DLSFixedWheelUnitPeakDilutionOrPDECReturn
AND DLSFlatHighModLargeSieveAbsorption
AND SignedGeometricLedgerVariationBranchLiftAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

下一步最窄目标更新为 `DLSFlatHighModLargeSieveAbsorption`：证明经过 PointLoad/ShortWindow/LowPhase/new-layer
cap 删除后的高模平坦残余满足大筛吸收界；若失败，必须输出对偶高频缺陷并回流
PDEC/SAE/ColumnCRT/外部谱输入。

## Prime Matrix 早期零行反例 flat-DLS 最后逃逸路由器

对应新增文件：

```text
experiments/prime_matrix_early_zero_flatdls_counterexample_router.py
docs/monograph/prime-matrix-early-zero-flatdls-counterexample-router.md/json
```

该路由器把 `DLSFlatHighModLargeSieveAbsorption` 放回“假设 P 行以内早期零行存在”的反例分支中解释。结论为：

```text
counterexample_assumption_only=true；
empirical_absence_not_used=true；
early_zero_flatdls_last_escape_boundary_closed=true；
dls_flat_highmod_large_sieve_absorption_proved=false；
direct_unconditional_contradiction_found=false；
row_column_unconditional_closed=false；
terminal_gap_before_router=DLSFlatHighModLargeSieveAbsorption；
terminal_gap_after_router=EarlyZeroL2FlatKLSCounterexampleSpectralExclusion_OR_CDependentResidueWeightSpectralCancellationInput。
```

反例分支链条固定为：

```text
Assume EarlyZeroRowWithinP；
named low-dimensional exits removed；
flat-DLS residual must pay remaining zero-row budget；
SN3-A/B low projection peak => SAE/PDEC/ColumnCRT；
SN3-C multiband sync => ShellOverlap/LowModSync/KLS-Multishell；
SN3-D KLS-Multishell => HighFrequencyColumn or L2FlatKLS；
SN3-E HighFrequencyColumn => Bohr-cap PDEC/ColumnCRT/SAE or L2-flat CleanKLS；
only last escape: L2-flat KLS spectral/NC-BLK input。
```

注意：这一步不使用真实样本中未见早期零行作为证明，也不证明 flat high-mod 大筛吸收界。它只证明在反例支付压力下，短窗、低模、列频率或 Bohr-cap 集中都不能作为无名逃逸，必须回流 `SAE/PDEC/ColumnCRT`；真正剩余只有反例专属的 L2-flat KLS 谱逃逸。

替换律为：

```text
DLSFlatHighModLargeSieveAbsorption
  =>
EarlyZeroL2FlatKLSCounterexampleSpectralExclusion。
```

条件/外部版仍可由 `CDependentResidueWeightSpectralCancellationInput` 承担。

已经闭合的门为：

```text
EarlyZeroCounterexampleAssumptionPinned；
FlatDLSGateActiveInCounterexampleBasis；
EmpiricalShortcutExplicitlyBlocked；
SN3LowProjectionPeelingInherited；
SN3MultibandSyncSplitInherited；
SN3ColumnFrequencyDichotomyInherited；
HighFrequencyBohrCapNoCycleInherited；
CleanKLSAdmissionAndExternalInterfaceRegistered；
CDependentSpectralReductionKnownButOpen；
EarlyZeroFlatDLSLastEscapeBoundaryClosed。
```

唯一开放门为：

```text
EarlyZeroL2FlatKLSCounterexampleSpectralExclusion。
```

更新后的完全自足输入基为：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn
AND ExplicitModelGapAndFiniteDPRCLedger
AND DLSPointLoadColumnCRTBoundOrNamedReturn
AND DLSShortWindowSAEBoundOrNamedReturn
AND DLSFixedWheelUnitPeakDilutionOrPDECReturn
AND EarlyZeroL2FlatKLSCounterexampleSpectralExclusion
AND SignedGeometricLedgerVariationBranchLiftAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

下一步最窄目标更新为 `EarlyZeroL2FlatKLSCounterexampleSpectralExclusion`：在假设早期零行存在的反例分支中，证明 L2-flat 高频 KLS 残余不能继续支付零行余量；若证明失败，必须输出同 formal unit 的高频 Bohr/PDEC/SAE/ColumnCRT 证书，或明确接受/匹配 `CDependentResidueWeightSpectralCancellationInput`。

## Prime Matrix 早期零行 L2-flat KLS 逃逸排除路由器

对应新增文件：

```text
experiments/prime_matrix_early_zero_l2flat_kls_exclusion_router.py
docs/monograph/prime-matrix-early-zero-l2flat-kls-exclusion-router.md/json
```

该路由器直接攻击 `EarlyZeroL2FlatKLSCounterexampleSpectralExclusion`。结论为：

```text
counterexample_assumption_only=true；
empirical_absence_not_used=true；
early_zero_l2flat_kls_counterexample_spectral_exclusion_closed=true；
pure_l2flat_escape_as_unnamed_branch_removed=true；
general_dls_flat_highmod_large_sieve_absorption_proved=false；
direct_unconditional_contradiction_found=false；
row_column_unconditional_closed=false；
terminal_gap_before_router=EarlyZeroL2FlatKLSCounterexampleSpectralExclusion；
terminal_gap_after_router=EarlyZeroTerminalExclusionPackage_OR_CDependentResidueWeightSpectralCancellationInput。
```

核心结构碰撞为：

```text
Assume EarlyZeroRowWithinP；
CLB gives R_x=F_x in one formal unit；
Early-zero phase schema gives stable recurrence OR no-automorphism phase defect；
flat/KLS admission requires all registered low-dimensional defects routed away；
therefore pure L2-flat KLS cannot be the final unnamed counterexample branch；
remaining task is terminal exclusion for the registered early-zero defect。
```

这一步仍然只在反例分支内工作，不使用真实样本未见早期零行作为证明。它比较的是两个已登记合同：早期零行合同强制同 formal unit 的 registered defect；flat/KLS 准入合同要求这种 registered 低维缺陷已经删除或命名回流。因此 pure L2-flat KLS 不能作为最后无名逃逸。

替换律为：

```text
EarlyZeroL2FlatKLSCounterexampleSpectralExclusion
  =>
EarlyZeroTerminalExclusionPackage。
```

注意：本步不证明一般 `DLSFlatHighModLargeSieveAbsorption`，也不排斥早期零行终端家族本身。它只关闭无名 flat 谱逃逸口。

已经闭合的门为：

```text
CounterexampleBasisPinned；
L2FlatEscapeIsActiveLastGate；
FlatAdmissionNamedReturnDiscipline；
EarlyZeroPhaseDefectSchemaImported；
StableOrNoAutomorphismDichotomyImported；
PureL2FlatCounterexampleCollision；
EarlyZeroL2FlatKLSCounterexampleSpectralExclusion；
DStructureRankinStillIndependent。
```

唯一数学开放门为：

```text
EarlyZeroTerminalExclusionPackage。
```

更新后的完全自足输入基为：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn
AND ExplicitModelGapAndFiniteDPRCLedger
AND DLSPointLoadColumnCRTBoundOrNamedReturn
AND DLSShortWindowSAEBoundOrNamedReturn
AND DLSFixedWheelUnitPeakDilutionOrPDECReturn
AND EarlyZeroTerminalExclusionPackage
AND SignedGeometricLedgerVariationBranchLiftAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

下一步最窄目标更新为 `EarlyZeroTerminalExclusionPackage`：排斥准入后的早期零行终端家族，即 primitive PDEC 容量、SAE/LocalSurvivor packet，或稳定复现位移缺陷。完成该包后仍需 `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。

## Prime Matrix 早期零行终端排斥包压缩路由器

对应新增文件：

```text
experiments/prime_matrix_early_zero_terminal_package_reduction_router.py
docs/monograph/prime-matrix-early-zero-terminal-package-reduction-router.md/json
```

该路由器直接攻击抽象 `EarlyZeroTerminalExclusionPackage`。结论为：

```text
counterexample_assumption_only=true；
empirical_absence_not_used=true；
early_zero_terminal_package_reduced=true；
early_zero_terminal_package_fully_proved=false；
direct_unconditional_contradiction_found=false；
row_column_unconditional_closed=false；
terminal_gap_before_router=EarlyZeroTerminalExclusionPackage；
terminal_gap_after_router=AnchorCollarPrimeFiberCapacityBoundOrPDECReturn AND CompositeCofactorDepthDescentOrNamedReturn AND EarlyBandLocalSurvivorOrSAEExclusion。
```

结构链为：

```text
EarlyZeroTerminalExclusionPackage
=> registered stable recurrence or boundary phase defect
=> exact carry-shell primitive support
=> cofactor depth split
=> x>=sqrt(P): canonical anchor collar short prime fibers
=> x<sqrt(P): composite cofactor descent or SAE/PDEC return。
```

这一步删除的是“抽象终端包”的无名性，不是完成终端排斥。它把大行段压成真双素 canonical anchor-collar 短素数纤维容量，把早期段压成复合 cofactor 深度下降或 LocalSurvivor/SAE 排斥。

替换律为：

```text
EarlyZeroTerminalExclusionPackage
  =>
AnchorCollarPrimeFiberCapacityBoundOrPDECReturn
AND CompositeCofactorDepthDescentOrNamedReturn
AND EarlyBandLocalSurvivorOrSAEExclusion。
```

已经闭合的门为：

```text
EarlyZeroTerminalPackageActive；
PhaseDefectNoFourthExit；
StableRecurrenceDisplacementAbsorbed；
CarryShellPrimitiveSupportClosed；
CofactorDepthSplitClosed；
AnchorCollarPrimePairReductionClosed；
ContradictionMatrixFrontierCompatible；
EarlyZeroTerminalPackageReduced。
```

开放门为：

```text
AnchorCollarPrimeFiberCapacityBoundOrPDECReturn；
CompositeCofactorDepthDescentOrNamedReturn；
EarlyBandLocalSurvivorOrSAEExclusion。
```

更新后的完全自足输入基为：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn
AND ExplicitModelGapAndFiniteDPRCLedger
AND DLSPointLoadColumnCRTBoundOrNamedReturn
AND DLSShortWindowSAEBoundOrNamedReturn
AND DLSFixedWheelUnitPeakDilutionOrPDECReturn
AND AnchorCollarPrimeFiberCapacityBoundOrPDECReturn
AND CompositeCofactorDepthDescentOrNamedReturn
AND EarlyBandLocalSurvivorOrSAEExclusion
AND SignedGeometricLedgerVariationBranchLiftAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

下一步最窄目标更新为 `AnchorCollarPrimeFiberCapacityBoundOrPDECReturn`：证明 canonical anchor collar 中长度 `<sqrt(P)` 的短素数纤维总容量不能覆盖 `R_x`，或证明任何过载都会产生 PDEC/SAE/ColumnCRT 命名证书。

## Prime Matrix anchor-collar 容量端点缺陷桥路由器

对应新增文件：

```text
experiments/prime_matrix_anchor_collar_endpoint_bridge_router.py
docs/monograph/prime-matrix-anchor-collar-endpoint-bridge-router.md/json
```

该路由器直接攻击 `AnchorCollarPrimeFiberCapacityBoundOrPDECReturn`。结论为：

```text
counterexample_assumption_only=true；
empirical_absence_not_used=true；
anchor_collar_endpoint_bridge_closed=true；
anchor_collar_prime_fiber_capacity_fully_proved=false；
direct_unconditional_contradiction_found=false；
row_column_unconditional_closed=false；
terminal_gap_before_router=AnchorCollarPrimeFiberCapacityBoundOrPDECReturn；
terminal_gap_after_router=(AnchorCollarEndpointDefectPDECExclusion OR AnchorFiberSaturationPDECOrSAEReturn)。
```

精确桥为：

```text
H_x(P)=Prime_x(P)+A_x(P) for x>=sqrt(P)；
Assume EarlyZeroRowWithinP => Prime_x(P)=0 => H_x(P)=A_x(P)；
H_x(P)=(P-1)V_x(P)+E_x(P)；
if (P-1)V_x(P)-A_x(P)>=G_x>0 then E_x(P)<=-G_x。
```

其中 `H_x` 是低骨架粗洞数，`Prime_x` 是素数洞数，`A_x` 是 canonical anchor-collar 真双素容量，`E_x` 是固定相位包含排除端点误差。早期零行反例把 `Prime_x` 强制为零，所以容量不足会转成强负端点 PDEC；若主项间隙失败，则说明短素数纤维接近饱和，进入持久 PDEC 或孤立 SAE/LocalSurvivor 回流。

替换律为：

```text
AnchorCollarPrimeFiberCapacityBoundOrPDECReturn
  =>
(AnchorCollarEndpointDefectPDECExclusion OR AnchorFiberSaturationPDECOrSAEReturn)。
```

已经闭合的门为：

```text
AnchorCollarCapacityGateActive；
AnchorGeometryImported；
ExactRoughPrimeAnchorIdentity；
EarlyZeroForcesPrimeVoid；
EndpointDecompositionImported；
CapacityFailureBecomesEndpointDefect；
NoGapMeansFiberSaturation；
PDECSchemaAvailableForEndpointDefect；
SampleIdentityAudit；
AnchorCollarEndpointBridgeClosed。
```

开放门为：

```text
AnchorCollarEndpointDefectPDECExclusion；
AnchorFiberSaturationPDECOrSAEReturn。
```

更新后的完全自足输入基为：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn
AND ExplicitModelGapAndFiniteDPRCLedger
AND DLSPointLoadColumnCRTBoundOrNamedReturn
AND DLSShortWindowSAEBoundOrNamedReturn
AND DLSFixedWheelUnitPeakDilutionOrPDECReturn
AND (AnchorCollarEndpointDefectPDECExclusion OR AnchorFiberSaturationPDECOrSAEReturn)
AND CompositeCofactorDepthDescentOrNamedReturn
AND EarlyBandLocalSurvivorOrSAEExclusion
AND SignedGeometricLedgerVariationBranchLiftAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

下一步最窄目标更新为 `AnchorCollarEndpointDefectPDECExclusion`：排斥早期零行强制产生的 `E_x<=-G_x` 级同 formal unit 端点相位缺陷；若主项间隙失败，则进入 `AnchorFiberSaturationPDECOrSAEReturn`。

## Prime Matrix anchor 端点 PDEC 低模/尾项二分路由器

对应新增文件：

```text
experiments/prime_matrix_anchor_endpoint_lowmod_tail_router.py
docs/monograph/prime-matrix-anchor-endpoint-lowmod-tail-router.md/json
```

该路由器直接攻击 `AnchorCollarEndpointDefectPDECExclusion`。结论为：

```text
counterexample_assumption_only=true；
empirical_absence_not_used=true；
anchor_endpoint_pdec_dichotomy_closed=true；
anchor_endpoint_pdec_exclusion_fully_proved=false；
direct_unconditional_contradiction_found=false；
row_column_unconditional_closed=false；
terminal_gap_before_router=AnchorCollarEndpointDefectPDECExclusion；
terminal_gap_after_router=(AnchorEndpointLowModPDECFinitePhaseExclusion AND AnchorEndpointTailCorePDECOrFiberSaturation)。
```

二分公式为：

```text
If E_x<=-G_x, then for any D and theta either
E_{x,<=D}<=-theta G_x
or
E_{x,>D}<=-(1-theta)G_x。
```

其中低模项是有限 CRT 相位函数；若它承担强负缺陷，就必须形成 fixed-wheel/lowphase PDEC 坏相位。尾项若承担强负缺陷，则必须显化为 `PointLoad/ShortWindow/LowPhase` 或 anchor-fiber 饱和，回流 PDEC/SAE/LocalSurvivor。

替换律为：

```text
AnchorCollarEndpointDefectPDECExclusion
  =>
(AnchorEndpointLowModPDECFinitePhaseExclusion
 AND AnchorEndpointTailCorePDECOrFiberSaturation)。
```

已经闭合的门为：

```text
AnchorEndpointDefectGateActive；
EndpointBridgeImported；
DLS13LowTailTemplateImported；
AnchorEndpointLowTailDichotomy；
LowModFinitePhasePDECRoute；
TailCoreNamedReturnRoute；
AnchorEndpointPDECDichotomyClosed。
```

开放门为：

```text
AnchorEndpointLowModPDECFinitePhaseExclusion；
AnchorEndpointTailCorePDECOrFiberSaturation。
```

更新后的完全自足输入基为：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn
AND ExplicitModelGapAndFiniteDPRCLedger
AND DLSPointLoadColumnCRTBoundOrNamedReturn
AND DLSShortWindowSAEBoundOrNamedReturn
AND DLSFixedWheelUnitPeakDilutionOrPDECReturn
AND ((AnchorEndpointLowModPDECFinitePhaseExclusion
      AND AnchorEndpointTailCorePDECOrFiberSaturation)
     OR AnchorFiberSaturationPDECOrSAEReturn)
AND CompositeCofactorDepthDescentOrNamedReturn
AND EarlyBandLocalSurvivorOrSAEExclusion
AND SignedGeometricLedgerVariationBranchLiftAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

下一步最窄目标更新为 `AnchorEndpointLowModPDECFinitePhaseExclusion`：固定 `D` 后，低模项是有限 CRT 相位函数；若它能持续承担 `-theta G_x` 级负缺陷，就必须形成 fixed-wheel/lowphase PDEC 坏相位。下一步要排斥这个坏相位，或把它登记为可处理 PDEC 证书。

## Prime Matrix anchor 低模端点相位 fixed-wheel 准入路由器

对应新增文件：

```text
experiments/prime_matrix_anchor_lowmod_fixedwheel_admission_router.py
docs/monograph/prime-matrix-anchor-lowmod-fixedwheel-admission-router.md/json
```

该路由器直接攻击 `AnchorEndpointLowModPDECFinitePhaseExclusion`。结论为：

```text
counterexample_assumption_only=true；
empirical_absence_not_used=true；
anchor_lowmod_independent_input_removed=true；
dls_fixedwheel_input_proved=false；
direct_unconditional_contradiction_found=false；
row_column_unconditional_closed=false；
terminal_gap_before_router=AnchorEndpointLowModPDECFinitePhaseExclusion；
terminal_gap_after_router=DLSFixedWheelUnitPeakDilutionOrPDECReturn。
```

固定 `D` 后，`E_{x,<=D}` 是有限 CRT 相位函数，必须放入同一个 lowmod formal unit `G_B=Z/Q_BZ`。LowMod 有限弧 cap 已经归约到 fixed-wheel/new-layer/flat DLS 三类；本分支是固定轮切片，所以准入既有 fixed-wheel/LowPhase PDEC 输入，而不是新增 anchor 专属低模原子。

替换律为：

```text
AnchorEndpointLowModPDECFinitePhaseExclusion
  =>
DLSFixedWheelUnitPeakDilutionOrPDECReturn。
```

已经闭合的门为：

```text
AnchorLowModGateActive；
FiniteCRTPhasePinned；
SameFormalUnitLowModProtocolImported；
FiniteArcReductionImported；
FixedWheelLowPhaseTargetAvailable；
AnchorLowModIndependentInputRemoved。
```

开放门为：

```text
DLSFixedWheelUnitPeakDilutionOrPDECReturn；
AnchorEndpointTailCorePDECOrFiberSaturation。
```

更新后的完全自足输入基为：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn
AND ExplicitModelGapAndFiniteDPRCLedger
AND DLSPointLoadColumnCRTBoundOrNamedReturn
AND DLSShortWindowSAEBoundOrNamedReturn
AND DLSFixedWheelUnitPeakDilutionOrPDECReturn
AND (AnchorEndpointTailCorePDECOrFiberSaturation
     OR AnchorFiberSaturationPDECOrSAEReturn)
AND CompositeCofactorDepthDescentOrNamedReturn
AND EarlyBandLocalSurvivorOrSAEExclusion
AND SignedGeometricLedgerVariationBranchLiftAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

anchor 专属最窄目标更新为 `AnchorEndpointTailCorePDECOrFiberSaturation`。全局层面仍需证明既有 `DLSFixedWheelUnitPeakDilutionOrPDECReturn`。

## Prime Matrix anchor tail-core 到纤维饱和路由器

对应新增文件：

```text
experiments/prime_matrix_anchor_tailcore_fiber_saturation_router.py
docs/monograph/prime-matrix-anchor-tailcore-fiber-saturation-router.md/json
```

该路由器直接攻击 `AnchorEndpointTailCorePDECOrFiberSaturation`。结论为：

```text
counterexample_assumption_only=true；
empirical_absence_not_used=true；
anchor_tailcore_independent_input_removed=true；
anchor_fiber_saturation_proved=false；
direct_unconditional_contradiction_found=false；
row_column_unconditional_closed=false；
terminal_gap_before_router=AnchorEndpointTailCorePDECOrFiberSaturation；
terminal_gap_after_router=AnchorFiberSaturationPDECOrSAEReturn。
```

高模 tail 若承担强负缺陷但不是 anchor q-fiber 近饱和，则必须显化为全局 DLS 字母表中的 `PointLoad/ShortWindow/LowPhase`，或 SN3-E 的 Bohr-cap 命名出口。这些不是 anchor 专属新原子，已经在全局输入基中保留。因此 anchor 专属剩余只有 canonical q-fiber 近饱和是否必回流 PDEC/SAE。

替换律为：

```text
AnchorEndpointTailCorePDECOrFiberSaturation
  =>
AnchorFiberSaturationPDECOrSAEReturn。
```

已经闭合的门为：

```text
AnchorTailCoreGateActive；
BESDLSNamedAlphabetImported；
HighFrequencyNoCycleImported；
AnchorFiberGeometryPinned；
ExistingGlobalInputsCoverNonFiberTail；
AnchorTailCoreIndependentInputRemoved。
```

唯一开放门为：

```text
AnchorFiberSaturationPDECOrSAEReturn。
```

更新后的完全自足输入基为：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn
AND ExplicitModelGapAndFiniteDPRCLedger
AND DLSPointLoadColumnCRTBoundOrNamedReturn
AND DLSShortWindowSAEBoundOrNamedReturn
AND DLSFixedWheelUnitPeakDilutionOrPDECReturn
AND AnchorFiberSaturationPDECOrSAEReturn
AND CompositeCofactorDepthDescentOrNamedReturn
AND EarlyBandLocalSurvivorOrSAEExclusion
AND SignedGeometricLedgerVariationBranchLiftAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

下一步最窄目标更新为 `AnchorFiberSaturationPDECOrSAEReturn`：证明 canonical q-fiber 近饱和不能持续支付早期零行，或从近饱和中抽取同 formal unit 的 PDEC/SAE 证书。

## Prime Matrix anchor fiber 饱和命名回流 schema 路由器

对应新增文件：

```text
experiments/prime_matrix_anchor_fiber_saturation_return_schema_router.py
docs/monograph/prime-matrix-anchor-fiber-saturation-return-schema-router.md/json
```

该路由器直接攻击 `AnchorFiberSaturationPDECOrSAEReturn`。结论为：

```text
counterexample_assumption_only=true；
empirical_absence_not_used=true；
anchor_fiber_saturation_return_schema_closed=true；
anchor_specific_fiber_gap_removed=true；
pdec_or_sae_terminal_exclusion_proved=false；
direct_unconditional_contradiction_found=false；
row_column_unconditional_closed=false；
terminal_gap_before_router=AnchorFiberSaturationPDECOrSAEReturn；
terminal_gap_after_router=NoAnchorSpecificFiberSaturationGap_AfterNamedPDECOrSAEReturn。
```

固定 `q` 后，`m` 位于长度 `<sqrt(P)` 的有限素数窗口，物理原子为 `(x,q,m,c)`，因此 fiber 饱和可登记为有限 formal unit packet。若同一 fiber 签名沿反例族持久近饱和，则必须提交同 formal unit primitive PDEC schema；若只孤立出现，则必须提交有限 LocalSurvivor/SAE packet schema。没有 anchor 专属第四出口。

替换律为：

```text
AnchorFiberSaturationPDECOrSAEReturn
  =>
NoAnchorSpecificFiberSaturationGap_AfterNamedPDECOrSAEReturn。
```

已经闭合的门为：

```text
AnchorFiberSaturationGateActive；
FiniteShortFiberFormalUnit；
PersistentFiberSaturationAdmitsPDEC；
IsolatedFiberSaturationAdmitsSparseSAE；
NoUnnamedFiberSaturationExit；
AnchorFiberSaturationPDECOrSAEReturn。
```

仍开放的全局守门项为：

```text
GlobalPDECorSparseTerminalExclusion。
```

这不是新的 anchor 专属 gap：若未来实际物化新的 persistent PDEC 或 sparse packet，必须由
`FutureExplicitPrimitivePDECSchema` 或 `FutureExplicitSparsePacketExtractorSchema` 接管。

更新后的完全自足输入基为：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn
AND ExplicitModelGapAndFiniteDPRCLedger
AND DLSPointLoadColumnCRTBoundOrNamedReturn
AND DLSShortWindowSAEBoundOrNamedReturn
AND DLSFixedWheelUnitPeakDilutionOrPDECReturn
AND CompositeCofactorDepthDescentOrNamedReturn
AND EarlyBandLocalSurvivorOrSAEExclusion
AND SignedGeometricLedgerVariationBranchLiftAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

anchor 专属 fiber gap 已删除。下一步最窄目标回到 `CompositeCofactorDepthDescentOrNamedReturn`。

## Prime Matrix 复合 cofactor 下降命名回流 schema 路由器

对应新增文件：

```text
experiments/prime_matrix_composite_cofactor_descent_schema_router.py
docs/monograph/prime-matrix-composite-cofactor-descent-schema-router.md/json
```

该路由器直接攻击 `CompositeCofactorDepthDescentOrNamedReturn`。结论为：

```text
counterexample_assumption_only=true；
empirical_absence_not_used=true；
composite_cofactor_descent_schema_closed=true；
composite_cofactor_specific_gap_removed=true；
pdec_or_sae_terminal_exclusion_proved=false；
direct_unconditional_contradiction_found=false；
row_column_unconditional_closed=false；
terminal_gap_before_router=CompositeCofactorDepthDescentOrNamedReturn；
terminal_gap_after_router=NoCompositeCofactorUnnamedDescentGap_AfterWellFoundedNamedReturn。
```

若 `xP+c=q m` 且 `m` 复合，则 `m<P` 且所有素因子 `>x`，所以 x-rough 乘法深度满足
`d<log(P)/log(x)`。一旦 `x>=sqrt(P)`，复合 cofactor 不可能存在，只剩真双素/anchor 分支。每次真正递归都把顶层 `P` 换成更小的 cofactor `m<P`，或降低 cofactor 乘法深度，因此不存在无穷递归循环。

替换律为：

```text
CompositeCofactorDepthDescentOrNamedReturn
  =>
NoCompositeCofactorUnnamedDescentGap_AfterWellFoundedNamedReturn。
```

已经闭合的门为：

```text
CompositeCofactorGateActive；
XRoughDepthBoundImported；
SqrtGateTerminatesPrimePair；
CarryShellSupportInherited；
WellFoundedDescentMeasure；
PersistentCompositeCofactorAdmitsPDEC；
IsolatedCompositeCofactorAdmitsSparseSAE；
NoUnnamedCompositeCofactorDescent；
CompositeCofactorDepthDescentOrNamedReturn。
```

仍开放的全局守门项为：

```text
GlobalPDECorSparseTerminalExclusion。
```

这不是新的 cofactor 专属 gap：若未来实际物化新的 persistent PDEC 或 sparse packet，必须由
`FutureExplicitPrimitivePDECSchema` 或 `FutureExplicitSparsePacketExtractorSchema` 接管。

更新后的完全自足输入基为：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn
AND ExplicitModelGapAndFiniteDPRCLedger
AND DLSPointLoadColumnCRTBoundOrNamedReturn
AND DLSShortWindowSAEBoundOrNamedReturn
AND DLSFixedWheelUnitPeakDilutionOrPDECReturn
AND EarlyBandLocalSurvivorOrSAEExclusion
AND SignedGeometricLedgerVariationBranchLiftAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

复合 cofactor 专属 gap 已删除。下一步最窄目标回到 `EarlyBandLocalSurvivorOrSAEExclusion`。

## Prime Matrix early-band LocalSurvivor/SAE 命名回流 schema 路由器

对应新增文件：

```text
experiments/prime_matrix_early_band_local_survivor_return_schema_router.py
docs/monograph/prime-matrix-early-band-local-survivor-return-schema-router.md/json
```

该路由器直接攻击 `EarlyBandLocalSurvivorOrSAEExclusion`。结论为：

```text
counterexample_assumption_only=true；
empirical_absence_not_used=true；
early_band_local_survivor_return_schema_closed=true；
early_band_specific_gap_removed=true；
pdec_or_sae_terminal_exclusion_proved=false；
dls_shortwindow_global_input_proved=false；
direct_unconditional_contradiction_found=false；
row_column_unconditional_closed=false；
terminal_gap_before_router=EarlyBandLocalSurvivorOrSAEExclusion；
terminal_gap_after_router=NoEarlyBandSpecificLocalSurvivorSAEGap_AfterNamedReturn。
```

在早期零行反例分支中，early-band 的孤窗不能作为独立终端保留：若窗口可抽取，则必须物化为有限
`LocalSurvivor/SAE` packet；若同一局部签名沿 formal 反例族持久复现，则必须提交同 formal unit
`PDEC` schema；若签名层级逃逸，则进入 `CleanKLS/DLS` admission。由此没有 early-band 专属第四出口。

替换律为：

```text
EarlyBandLocalSurvivorOrSAEExclusion
  =>
NoEarlyBandSpecificLocalSurvivorSAEGap_AfterNamedReturn。
```

已经闭合的门为：

```text
EarlyBandLocalSurvivorGateActive；
EarlyZeroCounterexampleBranchGuard；
SAEIndependentTerminalAbsorbed；
LocalSurvivorPacketGenerationDichotomy；
FutureSparsePacketBoundaryImported；
PersistentEarlyBandSignatureAdmitsPDEC；
ShortWindowGlobalInputPreserved；
NoEarlyBandSpecificFourthExit；
EarlyBandLocalSurvivorOrSAEExclusion。
```

仍开放的全局守门项为：

```text
DLSShortWindowSAEBoundOrNamedReturn；
GlobalPDECorSparseTerminalExclusion。
```

这一步只删除 early-band 专属 gap，不证明全局 short-window/SAE 微输入。更新后的完全自足输入基为：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn
AND ExplicitModelGapAndFiniteDPRCLedger
AND DLSPointLoadColumnCRTBoundOrNamedReturn
AND DLSShortWindowSAEBoundOrNamedReturn
AND DLSFixedWheelUnitPeakDilutionOrPDECReturn
AND SignedGeometricLedgerVariationBranchLiftAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

下一步最窄目标转到 `DLSShortWindowSAEBoundOrNamedReturn`：证明 short-window SAE 不能持续支付
DLS/BES 危险交集，或把它物化为有限 packet / persistent PDEC schema。

## Prime Matrix DLS short-window SAE 命名回流 schema 路由器

对应新增文件：

```text
experiments/prime_matrix_dls_shortwindow_sae_return_schema_router.py
docs/monograph/prime-matrix-dls-shortwindow-sae-return-schema-router.md/json
```

该路由器直接攻击 `DLSShortWindowSAEBoundOrNamedReturn`。结论为：

```text
counterexample_assumption_only=true；
empirical_absence_not_used=true；
dls_shortwindow_return_schema_closed=true；
dls_shortwindow_specific_gap_removed=true；
dls_shortwindow_numeric_bound_proved=false；
pdec_or_sae_terminal_exclusion_proved=false；
direct_unconditional_contradiction_found=false；
row_column_unconditional_closed=false；
terminal_gap_before_router=DLSShortWindowSAEBoundOrNamedReturn；
terminal_gap_after_router=NoDLSShortWindowSpecificSAEGap_AfterLocalPacketOrPDECReturn。
```

DLS/BES 危险交集若落入 short-window 字母表，不能作为无名同步失败停留。固定短窗是有限局部覆盖对象，
有候选集 `C(I)` 与 blocker 投影；孤立时必须提交 `LocalSurvivor/SAE` packet，持久同签名复现时必须
提交同 formal unit 的 `PDEC` schema，层级逃逸时必须进入 `CleanKLS/DLS` 或下降回流。

替换律为：

```text
DLSShortWindowSAEBoundOrNamedReturn
  =>
NoDLSShortWindowSpecificSAEGap_AfterLocalPacketOrPDECReturn。
```

已经闭合的门为：

```text
DLSShortWindowGateActive；
ShortWindowAlphabetPinned；
FiniteLocalWindowObject；
SAELocalDescentWellFounded；
PacketGenerationDichotomy；
FutureSparsePacketBoundaryImported；
PersistentShortWindowAdmitsPDEC；
NoDLSShortWindowSpecificFourthExit；
DLSShortWindowSAEBoundOrNamedReturn。
```

仍开放的全局守门项为：

```text
DLSPointLoadColumnCRTBoundOrNamedReturn；
DLSFixedWheelUnitPeakDilutionOrPDECReturn；
GlobalPDECorSparseTerminalExclusion。
```

这一步只删除 short-window 专属 gap，不证明数值 short-window bound。更新后的完全自足输入基为：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn
AND ExplicitModelGapAndFiniteDPRCLedger
AND DLSPointLoadColumnCRTBoundOrNamedReturn
AND DLSFixedWheelUnitPeakDilutionOrPDECReturn
AND SignedGeometricLedgerVariationBranchLiftAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

下一步最窄目标转到 `DLSPointLoadColumnCRTBoundOrNamedReturn`：证明 point-load 不能持续支付
DLS/BES 危险交集，或把它物化为 `ColumnCRT/displacement PDEC` 或 sparse packet 回流。

## Prime Matrix DLS point-load/ColumnCRT 命名回流 schema 路由器

对应新增文件：

```text
experiments/prime_matrix_dls_pointload_columncrt_return_schema_router.py
docs/monograph/prime-matrix-dls-pointload-columncrt-return-schema-router.md/json
```

该路由器直接攻击 `DLSPointLoadColumnCRTBoundOrNamedReturn`。结论为：

```text
counterexample_assumption_only=true；
empirical_absence_not_used=true；
dls_pointload_return_schema_closed=true；
dls_pointload_specific_gap_removed=true；
columncrt_independent_terminal_removed=true；
pdec_columncrt_sae_terminal_exclusion_proved=false；
direct_unconditional_contradiction_found=false；
row_column_unconditional_closed=false；
terminal_gap_before_router=DLSPointLoadColumnCRTBoundOrNamedReturn；
terminal_gap_after_router=NoDLSPointLoadColumnCRTSpecificGap_AfterDisplacementPDECOrSAEReturn。
```

DLS/BES 危险交集若落入 point-load 字母表，也不能作为无名同步失败停留。单点高负载若平衡，
不能支付命名缺陷预算；若持久，必给出有限列位移签名或尾锚签名，进入 `displacement PDEC`、
`ColumnCRT` 或尾锚 `PDEC`；若孤立，则进入 `SAE/LocalSurvivor` packet。

替换律为：

```text
DLSPointLoadColumnCRTBoundOrNamedReturn
  =>
NoDLSPointLoadColumnCRTSpecificGap_AfterDisplacementPDECOrSAEReturn。
```

已经闭合的门为：

```text
DLSPointLoadGateActive；
PointLoadAlphabetPinned；
ColumnCRTIndependentExitAbsorbed；
FiniteDisplacementSignature；
BalancedPointLoadCannotPayDefectBudget；
TailAnchorPointLoadAbsorbed；
PersistentPointLoadAdmitsPDEC；
SparsePointLoadAdmitsSAE；
NoDLSPointLoadSpecificFourthExit；
DLSPointLoadColumnCRTBoundOrNamedReturn。
```

仍开放的全局守门项为：

```text
DLSFixedWheelUnitPeakDilutionOrPDECReturn；
GlobalPDECorSparseTerminalExclusion。
```

这一步只删除 point-load 专属 gap，不证明全局 `PDEC/ColumnCRT/SAE` 终端排斥。更新后的完全自足输入基为：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn
AND ExplicitModelGapAndFiniteDPRCLedger
AND DLSFixedWheelUnitPeakDilutionOrPDECReturn
AND SignedGeometricLedgerVariationBranchLiftAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

下一步最窄目标转到 `DLSFixedWheelUnitPeakDilutionOrPDECReturn`：证明固定轮单位类峰被层叠轮稀释，
或把持久单位峰登记为 `PDEC`。

## Prime Matrix DLS fixed-wheel 单位峰命名回流 schema 路由器

对应新增文件：

```text
experiments/prime_matrix_dls_fixedwheel_pdec_return_schema_router.py
docs/monograph/prime-matrix-dls-fixedwheel-pdec-return-schema-router.md/json
```

该路由器直接攻击 `DLSFixedWheelUnitPeakDilutionOrPDECReturn`。结论为：

```text
counterexample_assumption_only=true；
empirical_absence_not_used=true；
dls_fixedwheel_return_schema_closed=true；
dls_fixedwheel_specific_gap_removed=true；
fixedwheel_numeric_dilution_proved=false；
wunit_pdec_terminal_exclusion_proved=false；
direct_unconditional_contradiction_found=false；
row_column_unconditional_closed=false；
terminal_gap_before_router=DLSFixedWheelUnitPeakDilutionOrPDECReturn；
terminal_gap_after_router=NoDLSFixedWheelSpecificGap_AfterWUnitPDECOrLayeredDilutionReturn。
```

固定轮单位峰不能作为终局规律停留。固定 `W` 时，单位类 `U_W` 与中心化偏差 `E_a(W)` 是有限
formal unit 对象；若同一单位峰持久同步，则必须登记为 `W-unit PDEC`。若升层后峰继续集中，则进入
new-layer PDEC/flat admission；若固定轮和新增层缺陷都被剥离，则 flat/L2-flat 逃逸已在早期零行
反例分支回到终端包。

替换律为：

```text
DLSFixedWheelUnitPeakDilutionOrPDECReturn
  =>
NoDLSFixedWheelSpecificGap_AfterWUnitPDECOrLayeredDilutionReturn。
```

已经闭合的门为：

```text
DLSFixedWheelGateActive；
FixedWheelAtomPinned；
FiniteWheelFormalUnit；
FixedWheelNotTerminalLaw；
LayeredWheelDilutionOrPDEC；
PersistentWUnitPeakAdmitsPDEC；
LayerEscapeUsesNewLayerReturn；
FlatEscapeAlreadyCounterexampleRouted；
NoDLSFixedWheelSpecificFourthExit；
DLSFixedWheelUnitPeakDilutionOrPDECReturn。
```

仍开放的全局守门项为：

```text
SignedGeometricLedgerVariationBranchLiftAndReturn；
GlobalPDECorSparseTerminalExclusion。
```

这一步只删除 fixed-wheel 专属 gap，不证明数值稀释界，也不排斥 `W-unit PDEC` 或终端包。更新后的完全自足输入基为：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn
AND ExplicitModelGapAndFiniteDPRCLedger
AND SignedGeometricLedgerVariationBranchLiftAndReturn
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

下一步最窄目标转到 `SignedGeometricLedgerVariationBranchLiftAndReturn`：证明 actual signed source 的
总变差和 branch key 复杂度确由几何账本支配，或把超预算质量回流 `PDEC/SAE/ColumnCRT/CleanKLS`。

## Prime Matrix signed 几何变差锁兼容预算合并路由器

对应新增文件：

```text
experiments/prime_matrix_signed_geometric_variation_compatibility_merger.py
docs/monograph/prime-matrix-signed-geometric-variation-compatibility-merger.md/json
```

该路由器直接攻击 `SignedGeometricLedgerVariationBranchLiftAndReturn` 的独立性。结论为：

```text
counterexample_assumption_only=true；
empirical_absence_not_used=true；
signed_variation_independent_atom_removed=true；
actual_signed_source_phi_compatibility_budget_proved=false；
actual_noncanonical_constructor_formula_proved=false；
direct_unconditional_contradiction_found=false；
row_column_unconditional_closed=false；
terminal_gap_before_router=ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn AND SignedGeometricLedgerVariationBranchLiftAndReturn；
terminal_gap_after_router=ActualSignedSourceMeasurePhiCompatibilityBudgetAndReturn。
```

`SignedGeometricLedgerVariationBranchLiftAndReturn` 不是独立原子。几何层只给 unsigned payment 账本；
signed 总变差、绝对支撑、sign refinement 和 branch key 复杂度必须跟 actual signed source 与 `Phi`
推前恒等式一起审查。逐纤维解积分本身形式闭合，真实硬点是同一 formal unit 内的 actual signed source
兼容预算。

替换律为：

```text
ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn
AND SignedGeometricLedgerVariationBranchLiftAndReturn
  =>
ActualSignedSourceMeasurePhiCompatibilityBudgetAndReturn。
```

已经闭合的门为：

```text
SignedVariationGateActive；
SourceIdentityPairedInSameBasis；
GeometricBudgetSplitImported；
DisintegrationAutomaticityPinsCombinedGate；
AlphaDeltaDictionaryFieldsCoverVariation；
ConstructorSourceFieldsCoverBranchKeys；
NoIndependentSignedVariationAtom；
SignedGeometricLedgerVariationBranchLiftAndReturn。
```

仍开放的全局守门项为：

```text
ActualSignedSourceMeasurePhiCompatibilityBudgetAndReturn；
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

这一步只合并输入边界，不证明兼容预算。更新后的完全自足输入基为：

```text
ActualSignedSourceMeasurePhiCompatibilityBudgetAndReturn
AND ExplicitModelGapAndFiniteDPRCLedger
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

下一步最窄目标为 `ActualSignedSourceMeasurePhiCompatibilityBudgetAndReturn`：给出 actual noncanonical signed source、
`Phi` 推前恒等式、总变差/支撑预算和 branch key 预算，或把失败者命名回流。

## Prime Matrix actual signed/Phi 兼容预算到 pre-pushforward emitter 压缩路由器

对应新增文件：

```text
experiments/prime_matrix_actual_signed_phi_budget_emitter_reduction_router.py
docs/monograph/prime-matrix-actual-signed-phi-budget-emitter-reduction-router.md/json
```

该路由器直接攻击 `ActualSignedSourceMeasurePhiCompatibilityBudgetAndReturn` 的复合黑箱性。结论为：

```text
counterexample_assumption_only=true；
empirical_absence_not_used=true；
hypothetical_chain_only=true；
actual_signed_phi_budget_reduction_closed=true；
actual_signed_source_phi_compatibility_budget_proved=false；
registered_primitive_prepushforward_fiber_emitter_proved=false；
direct_unconditional_contradiction_found=false；
row_column_unconditional_closed=false；
terminal_gap_before_router=ActualSignedSourceMeasurePhiCompatibilityBudgetAndReturn；
terminal_gap_after_router=RegisteredPrimitivePrePushforwardFiberEmitterAndReturn。
```

这里必须分清两条链：假设链条中，早期零行反例若要保留 clean-core 支付链，就必须在
Cauchy/dispersion 前给出同 formal unit 的 primitive signed preimage summand、branch key、`u/v`、
sign/local factor 与推前系数恒等式；真实链条中，payment 图、有限投影塔或真实样本缺席都不能反向唯一恢复
这个 emitter。

替换律为：

```text
ActualSignedSourceMeasurePhiCompatibilityBudgetAndReturn
  =>
RegisteredPrimitivePrePushforwardFiberEmitterAndReturn。
```

已经闭合的门为：

```text
ActualSignedPhiBudgetGateActive；
HypotheticalCounterexampleChainGuard；
DisintegrationFormalPartClosed；
AlphaDeltaDictionaryFieldsPinned；
PaymentSkeletonAlreadyClosed；
ReversePushforwardNoGoImported；
PreCauchyLedgerFieldsImported；
CompatibilityBudgetReducedToFiberEmitter；
ActualSignedSourceMeasurePhiCompatibilityBudgetAndReturn。
```

仍开放的全局守门项为：

```text
RegisteredPrimitivePrePushforwardFiberEmitterAndReturn；
ExplicitModelGapAndFiniteDPRCLedger；
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

这一步只压缩兼容预算，不证明 emitter 存在。更新后的完全自足输入基为：

```text
RegisteredPrimitivePrePushforwardFiberEmitterAndReturn
AND ExplicitModelGapAndFiniteDPRCLedger
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

下一步最窄目标为 `RegisteredPrimitivePrePushforwardFiberEmitterAndReturn`：在推前前逐纤维列出 primitive
summand、系数恒等式、branch key、`u/v` map、符号和 local factor；无法登记或超预算者必须命名回流。

## Prime Matrix pre-pushforward emitter 到原始生成账本压缩路由器

对应新增文件：

```text
experiments/prime_matrix_prepushforward_emitter_origin_ledger_router.py
docs/monograph/prime-matrix-prepushforward-emitter-origin-ledger-router.md/json
```

该路由器继续攻击 `RegisteredPrimitivePrePushforwardFiberEmitterAndReturn` 的来源黑箱性。结论为：

```text
counterexample_assumption_only=true；
empirical_absence_not_used=true；
hypothetical_chain_only=true；
prepushforward_emitter_reduction_closed=true；
registered_primitive_prepushforward_fiber_emitter_proved=false；
clean_core_original_generation_ledger_proved=false；
direct_unconditional_contradiction_found=false；
row_column_unconditional_closed=false；
terminal_gap_before_router=RegisteredPrimitivePrePushforwardFiberEmitterAndReturn；
terminal_gap_after_router=CleanCoreOriginalCoefficientGenerationLedgerAndReturn。
```

这里的分界仍然是两条链：假设链条中，早期零行反例若要保留 clean-core 支付链，必须提交
Cauchy/dispersion 前的 actual clean-core `alpha/delta` 原始生成表；真实链条中，payment skeleton、
有限投影塔、斜线覆盖图或样本缺席都不能反向唯一恢复 primitive source。

替换律为：

```text
RegisteredPrimitivePrePushforwardFiberEmitterAndReturn
  =>
CleanCoreOriginalCoefficientGenerationLedgerAndReturn。
```

已经闭合的门为：

```text
PrePushforwardEmitterGateActive；
ReversePhiRouteBlocked；
PaymentSkeletonClosedButSignedLiftOpen；
PreCauchyOriginLedgerAtomPinned；
ConstructorAdmissionIsLedgerEntry；
SourceClassFirewallPreventsCanonicalLeak；
EmitterReducedToOriginGenerationLedger；
RegisteredPrimitivePrePushforwardFiberEmitterAndReturn。
```

仍开放的全局守门项为：

```text
CleanCoreOriginalCoefficientGenerationLedgerAndReturn；
ExplicitModelGapAndFiniteDPRCLedger；
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

这一步只压缩 pre-pushforward emitter，不证明原始账本存在。更新后的完全自足输入基为：

```text
CleanCoreOriginalCoefficientGenerationLedgerAndReturn
AND ExplicitModelGapAndFiniteDPRCLedger
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

下一步最窄目标为 `CleanCoreOriginalCoefficientGenerationLedgerAndReturn`：提交 actual clean-core
`alpha/delta` 的完整 pre-Cauchy 原始生成表；缺失来源、路径超预算、thin block 或抵消必须命名回流。

## Prime Matrix clean-core 来源环切断路由器

对应新增文件：

```text
experiments/prime_matrix_clean_core_source_loop_cut_router.py
docs/monograph/prime-matrix-clean-core-source-loop-cut-router.md/json
```

该路由器审查 `CleanCoreOriginalCoefficientGenerationLedgerAndReturn` 是否已经能被既有材料自我闭合。结论为：

```text
counterexample_assumption_only=true；
empirical_absence_not_used=true；
hypothetical_chain_only=true；
source_loop_detected=true；
circular_reverse_derivation_rejected=true；
source_loop_cut_closed=true；
acyclic_pre_cauchy_source_seed_proved=false；
clean_core_original_generation_ledger_proved=false；
direct_unconditional_contradiction_found=false；
row_column_unconditional_closed=false；
terminal_gap_before_router=CleanCoreOriginalCoefficientGenerationLedgerAndReturn；
terminal_gap_after_router=AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn。
```

检测到的来源环为：

```text
CleanCoreOriginalCoefficientGenerationLedgerAndReturn
  -> CleanCorePrimitiveSourceConstructorAdmissionAndReturn
  -> ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn
  -> RegisteredPrimitivePrePushforwardFiberEmitterAndReturn
  -> CleanCoreOriginalCoefficientGenerationLedgerAndReturn。
```

这给出一个真正有用的切断：假设早期零行反例不能把自身 payment skeleton、有限投影塔、斜线覆盖图或样本缺席
当作 primitive source 的生成证明。若 clean-core 分支仍要保留，必须给出无环的 pre-Cauchy actual
noncanonical primitive source seed；否则它不是合法 clean-core 终端，只能命名回流。

替换律为：

```text
CleanCoreOriginalCoefficientGenerationLedgerAndReturn
  =>
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn。
```

已经闭合的门为：

```text
OriginLedgerToConstructorAdmission；
ConstructorAdmissionToActualNoncanonicalFormula；
ActualFormulaToRegisteredEmitter；
RegisteredEmitterBackToOriginLedger；
CleanCoreSourceLoopDetected；
CircularReverseDerivationRejected。
```

仍开放的全局守门项为：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn；
ExplicitModelGapAndFiniteDPRCLedger；
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

这一步仍不是行/列命题无条件证明；它只删除“循环来源证明”这个伪闭合路径。更新后的完全自足输入基为：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn
AND ExplicitModelGapAndFiniteDPRCLedger
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

下一步最窄目标为 `AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn`：给出不依赖 downstream payment 图的
pre-Cauchy 源种子，或证明任何此类种子都会触发 PDEC/SAE/ColumnCRT/CleanKLS/external spectral 回流。

## Prime Matrix 假设早期零行源种子 no-go 路由器

对应新增文件：

```text
experiments/prime_matrix_hypothetical_zero_row_seed_no_go_router.py
docs/monograph/prime-matrix-hypothetical-zero-row-seed-no-go-router.md/json
```

该路由器直接审查一个最容易混淆的方向：能否从“假设早期零行存在”本身抽取无环 pre-Cauchy 源种子。结论为：

```text
counterexample_assumption_only=true；
empirical_absence_not_used=true；
hypothetical_chain_only=true；
zero_row_crt_equivalence_used=true；
zero_row_seed_extraction_blocked=true；
geometry_source_extraction_blocked=true；
downstream_reverse_source_blocked=true；
independent_precauchy_arithmetic_source_identity_proved=false；
direct_unconditional_contradiction_found=false；
row_column_unconditional_closed=false；
terminal_gap_before_router=AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn；
terminal_gap_after_router=IndependentPreCauchyArithmeticSourceIdentityForNoncanonicalCleanCoreAndReturn。
```

核心 no-go 为：

```text
early zero row assumption
  => complete covering CRT certificate tau
  => unsigned payment / cylindrical / wheel geometry
  != pre-Cauchy signed alpha/delta source seed。
```

这一步严格分清假设链条和真实链条：假设早期零行提供的是覆盖事实、CRT 相容性和几何 payment 基底；
pre-Cauchy 源种子要求 signed `alpha/delta` 系数生成恒等式。几何模型可以提供 Phi 基底、容量形状和命名回流场，
但不定义 signed source；来源环切断又禁止从 downstream payment skeleton 反推 primitive source。

替换律为：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn
  =>
IndependentPreCauchyArithmeticSourceIdentityForNoncanonicalCleanCoreAndReturn。
```

已经闭合的门为：

```text
ZeroRowCRTEquivalenceClosed；
HypotheticalZeroRowDataUnsigned；
GeometryPaymentBaseNoSourceMeasure；
DownstreamReverseSourceBlocked；
HypotheticalZeroRowCannotSupplyAcyclicSeed。
```

仍开放的全局守门项为：

```text
IndependentPreCauchyArithmeticSourceIdentityForNoncanonicalCleanCoreAndReturn；
ExplicitModelGapAndFiniteDPRCLedger；
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

这一步仍不是行/列命题无条件证明；它删除的是“由反例覆盖图自己制造 signed 源”的伪路径。更新后的完全自足输入基为：

```text
IndependentPreCauchyArithmeticSourceIdentityForNoncanonicalCleanCoreAndReturn
AND ExplicitModelGapAndFiniteDPRCLedger
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

下一步最窄目标为 `IndependentPreCauchyArithmeticSourceIdentityForNoncanonicalCleanCoreAndReturn`：提交独立的
pre-Cauchy 算术来源恒等式，或证明任何候选恒等式都必回流到 PDEC/SAE/ColumnCRT/CleanKLS/external spectral。

## Prime Matrix 独立 pre-Cauchy 来源恒等式分类路由器

对应新增文件：

```text
experiments/prime_matrix_independent_precauchy_identity_taxonomy_router.py
docs/monograph/prime-matrix-independent-precauchy-identity-taxonomy-router.md/json
```

该路由器穷尽 `IndependentPreCauchyArithmeticSourceIdentityForNoncanonicalCleanCoreAndReturn` 的合法来源类。结论为：

```text
counterexample_assumption_only=true；
empirical_absence_not_used=true；
hypothetical_chain_only=true；
identity_taxonomy_closed=true；
canonical_source_identity_blocked=true；
generic_wfd_identity_rejected=true；
ap_source_lift_rejected=true；
external_spectral_self_contained_identity_proved=false；
actual_moving_block_spread_proved=false；
precisely_matched_external_spectral_accepted=false；
direct_unconditional_contradiction_found=false；
row_column_unconditional_closed=false；
terminal_gap_before_router=IndependentPreCauchyArithmeticSourceIdentityForNoncanonicalCleanCoreAndReturn；
terminal_gap_after_router=ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn。
```

分类律为：

```text
independent pre-Cauchy source identity
  in {canonical, generic_wfd, AP/external, actual_noncanonical}
canonical       -> scoped out of noncanonical clean-core
generic_wfd     -> rejected
AP/external     -> not self-contained source identity
actual_noncanonical -> moving-block spread / NC-BLK core。
```

这一步继续分清假设链条与真实链条：假设早期零行不能自己制造 signed source；即使要求一个独立
pre-Cauchy 来源恒等式，它也不能走 canonical 偷渡、generic WFD、APSourceLift 或外部谱自足化。自足内部剩余必须落到
actual noncanonical same-`(u,v)` moving block spread/NC-BLK 核心；外部谱匹配只在条件分支保留。

替换律为：

```text
IndependentPreCauchyArithmeticSourceIdentityForNoncanonicalCleanCoreAndReturn
  =>
ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn。
```

已经闭合的门为：

```text
NoHiddenFourthRouteImported；
CanonicalSourceIdentityBlockedForNoncanonical；
GenericWFDIdentityRejected；
APSourceLiftRejected；
ExternalSpectralNotSelfContainedSourceIdentity；
RemainingActualSourceCoreIdentified；
IndependentPreCauchyIdentityTaxonomyClosed。
```

仍开放的全局守门项为：

```text
ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn；
ExplicitModelGapAndFiniteDPRCLedger；
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

这一步仍不是行/列命题无条件证明；它删除的是“独立来源恒等式”作为新黑箱的可能。更新后的完全自足输入基为：

```text
ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn
AND ExplicitModelGapAndFiniteDPRCLedger
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

下一步最窄目标为 `ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn`：在假设早期零行反例分支中，
证明 actual same-`(u,v)` moving block 不能集中到足以支付零行；若改走外部条件分支，则必须精确匹配并接受
`CDependentResidueWeightSpectralCancellationInput`；否则给出命名 PDEC/SAE/ColumnCRT/CleanKLS 回流证书。

## Prime Matrix 反例分支 moving-block 到早期零行终端包路由器

对应新增文件：

```text
experiments/prime_matrix_counterexample_moving_block_terminal_router.py
docs/monograph/prime-matrix-counterexample-moving-block-terminal-router.md/json
```

该路由器只在假设早期零行反例分支内工作。结论为：

```text
counterexample_assumption_only=true；
empirical_absence_not_used=true；
hypothetical_chain_only=true；
moving_block_to_terminal_reduction_closed=true；
actual_moving_block_spread_proved=false；
early_zero_terminal_package_fully_proved=false；
exact_model_gap_dprc_compatibility_proved=false；
direct_unconditional_contradiction_found=false；
row_column_unconditional_closed=false；
terminal_gap_before_router=ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn；
terminal_gap_after_router=EarlyZeroTerminalExclusionPackage AND ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock。
```

反例二分为：

```text
Assume EarlyZeroRowWithinP
actual moving same-(u,v) atom
  -> registered finite/low-dimensional signature
       -> PDEC / SAE / ColumnCRT / EarlyZeroTerminalExclusionPackage
  -> no registered signature
       -> pure L2-flat / NC-BLK escape
       -> EarlyZeroTerminalExclusionPackage。
```

这一步把用户强调的“假设链条 vs 真实链条”继续落到形式账本上：如果 moving block 有登记低维签名，
它不是 clean-core 无名源，而是终端缺陷；如果它没有任何登记签名，它就是 pure L2-flat/NC-BLK 逃逸，
而早期零行反例分支已经证明 pure L2-flat 逃逸与早期零行强制的稳定/相位缺陷合同冲突，必须回到
`EarlyZeroTerminalExclusionPackage`。

替换律为：

```text
ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn
  =>
EarlyZeroTerminalExclusionPackage AND ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock。
```

已经闭合的门为：

```text
SourceEntropyImplicationImported；
SharpMovingAtomPinned；
RegisteredOrPureFlatDichotomy；
PureL2FlatEscapeAlreadyRemovedInEarlyZeroBranch；
EarlyZeroTerminalPackageAlreadyReduced；
CounterexampleMovingBlockReducedToTerminalPackage。
```

仍开放的全局守门项为：

```text
EarlyZeroTerminalExclusionPackage；
ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock；
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

这一步仍不是行/列命题无条件证明；它删除的是 moving-block 作为独立无名 clean-core 出口的可能。更新后的完全自足输入基为：

```text
EarlyZeroTerminalExclusionPackage
AND ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock
AND ExplicitModelGapAndFiniteDPRCLedger
AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。
```

下一步最窄目标回到 `EarlyZeroTerminalExclusionPackage`：排斥 primitive PDEC 容量、SAE/LocalSurvivor packet
或稳定复现位移缺陷；同时核对模型余量/DPRC 账本是否与该替换口径兼容。
