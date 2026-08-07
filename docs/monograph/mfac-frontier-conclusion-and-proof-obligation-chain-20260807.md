# MFAC 最前沿结论与证明义务链（2026-08-07）

**状态：** `global_arithmetic_transport_closed_actual_noncanonical_precauchy_source_open`

## 0. 一句话结论

截至 2026 年 8 月 7 日，MFAC 线已严格闭合**全局 Möbius 算术 payload 的可追溯分解与有限审计**，并精确排除了把无符号支撑、全局零和、hash、parity 或 synthetic record 误称为 actual signed source 的循环捷径；但尚未构造独立、pre-Cauchy 的 noncanonical primitive emitter。

因此它目前是 signed-source 缺口的高分辨率中间定理计划与否证框架，**不是** `ψ` 平滑误差、零点排除或 RH 的证明。

当前唯一应被攻击的正向数学门为：

```text
SemiprimeTriadDeclarationLineFromIndependentArithmeticIdentity
```

它必须给出不能从既有 divisor/LPF/word/parity/canonical 数据恢复的 primitive arithmetic functional，并把该泛函直接绑定到 actual row、取向、局部因子、exact `(u,v)` 与 prepushforward identity。

## 1. 证据等级与阅读规则

| 等级 | 含义 | 本轮例子 | 不允许推出 |
| --- | --- | --- |
| E1 | 初等精确恒等式 | `Lambda(n) = -sum_{d|n} mu(d) log(d)` | actual primitive row |
| E2 | 有限审计或精确重构 | D/E divisor-history、最小 `(2,3)` triad | 无穷范围 signed family |
| E3 | schema/路由/条件分类 | hash、record、orientation、局部自然性二分 | 新的算术恒等式 |
| E4 | 真正正向数学构造 | 尚未获得 | `ψ` 平方根误差、零点排除、RH |

“closed”在本文件中只表示某个指定等级内的断言已核验；它绝不自动提升到更高等级。

## 2. 已闭合的算术骨架

### 2.1 全局 Möbius--von Mangoldt 源对恒等式（E1）

对每个 `n`，有精确恒等式：

```text
Lambda(n) = -sum_{d|n} mu(d) log(d)
```

审计把每个非零项写作 source pair `(d,m)`，其中 `n=d*m`。这给出全局 payload 的正确来源坐标；它不指定该项属于哪个 actual primitive row，更不指定 orientation 或 local factor。

粗辅因子审计的关键负结果同样精确：仅以 LPF owner、当前 rough cofactor 与 cofactor 保存的局部状态不充分。最小碰撞为：

```text
(n,d,m)=(6,3,2) 与 (12,6,2)
LPF-local state=(2,3,2)
```

两条来源具有不同 Möbius 符号与 `log(d)` 因子分解。因此任何试图从这种局部状态直接推出 MFAC-1A signed transport 的论证都在此失败；完整 divisor-history 或等价可追溯信息是必要的。

### 2.2 D/E 双色 divisor word 的全局传输（E2）

完整 divisor-history 可编码为 D/E 双色词。已有审计逐项验证：

```text
record_reconstruction_verified=true
one_step_transport_verified=true
global_payload_conservation_verified=true
```

这说明在有限审计范围内，追加粗辅因子的精确 D、E 或零 Möbius 分支可以逐项追踪，按 `n` 汇总可恢复全局 `Lambda(n)` payload。

但边界同样是硬的：

```text
actual_primitive_unit_binding_constructed=false
mfac_1a_general_transport_constructed=false
```

“全局算术项被正确传输”不等于“每个项已经成为可进入 Cauchy 的 signed row”。这是整个推理链最重要的类型差异。

## 3. 已排除的循环捷径

### 3.1 hash 不能产生 registration

formal-unit/source-tuple/source-record hash 未含 `emitter_id`、`primitive_slot` 与 `same_formal_unit_certificate`。因此 hash 可以命名或校验一个已给定对象，却不能反向生成 actual emitter registration。首缺字段是 `emitter_id`。

### 3.2 schema 不能产生原子记录

当前语料没有从假设 witness 到 actual noncanonical atomic source record 的前向构造器；最早缺失字段是 `origin_selector`。没有该字段，branch alphabet 连定义域也没有，因而不能进行“同 row、异 orientation/local factor”的实际 collision 搜索。

### 3.3 factor-word parity 不能产生取向

`mu`、Liouville、squarefree 与 depth parity 可以从因子词后验计算，但没有提供：

```text
origin_selector
orientation 的前向来源
local-factor product
actual-emitter registration
prepushforward signed-sum identity
```

这排除把“可计算 parity”当作“已构造 orientation law”的混淆。parity 单独没有同一 formal unit 的 signed-source 语义。

### 3.4 全局三项零和不能产生 row dispatch

最小 offdiagonal triad 为：

```text
(2,3,+log 2), (3,2,+log 3), (6,1,-log 6)
log 2 + log 3 - log 6 = 0
```

对应证书读数为：

```text
global_triad_reconstructed=true
global_payload_zero_sum=true
actual_dispatch_present=false
canonical_zero_sum_collapse=false
```

该恒等式只说明全局 payload 零和。若没有 `row_key`，就无法判定三项是同一 canonical row 内的消去，还是不同 actual row 的带符号发射；更不能把它直接送入 trace、Kloosterman、Type-II 或 Cauchy 步骤。当前语料没有该 triad 的 actual dispatch。

## 4. 局部自然性二分：本轮最精确的前沿定位（E3）

| 候选族 | 分类 | 它确实提供的内容 | 它不提供的内容 |
| --- | --- | --- | --- |
| global Möbius/Lambda | `global_only_zero_sum` | 全局三项恒等式 | row declaration |
| D/E colored divisor word | `global_only_transport` | 可追溯全局 payload | actual primitive-unit binding |
| LPF/Phi factor word | `unsigned_or_canonical_support` | 支撑、owner、顺序词 | signed emitter |
| square-base/parity | `posterior_state_only` | 后验状态 | orientation 来源 |
| canonical RIW/Buchstab T1 | `canonical_factorization` | canonical branch 系数 | noncanonical complement |

此审计的条件模型要求候选只读取 `(p,q,d)` 的 divisor、cofactor、ordered factor word、LPF owner、parity 与局部对数权，且满足素因子重命名自然性、局部系数律与下游独立性。在这个明确范围内，候选只能落入 canonical factorization、rowwise cancellation 或上述非 source 分类。

“条件”不可省略：审计没有证明世界上所有可能的 arithmetic identity 都必须如此分解。它证明的是，把当前五族材料重新命名为 noncanonical source 行不通。完整 synthetic 独立记录会被识别为 collision certificate，故判据不是恒为负。

## 5. 共同 source packet 与真正断点

所有下游 signed-payload 与 ExactUV 目标在当前项目中收敛为同一必须前向支付的对象：

```text
PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket
```

它至少需要：

```text
declaration_line
source_tuple_domain_entropy
primitive_summand_rows
basis_word_signed_coefficient_identity
alpha_delta_prepushforward_identity
fixed_exact_uv_fiber_bound
no_downstream_recovery
named_return_partition
```

其中 `primitive_summand_rows` 必须逐行携带 branch key、basis word、sign、local factor、exact `(u,v)` 与 return tag。`declaration_line` 是最早生产字段：若它在 Cauchy/Phi/payment 之后才被识别，那不是 source declaration，而是下游恢复，必须进入 named return。

当前真正的矛盾场因此是严格二分：

```text
若 declaration 仅由既有局部乘法资料决定
  => canonical factorization 或 rowwise cancellation。

若 declaration 确实给出 noncanonical row
  => 必须提交不可由既有资料恢复的独立算术泛函。
```

第二支所需泛函不能只是 `Lambda(p*q)=0`、global D/E history、Möbius parity 或 LPF support 的别名；它必须从一个独立的 pre-Cauchy 算术恒等式产生 actual `origin_selector` 并给出原始行系数。

## 6. 唯一正向攻击目标的精确定式

对每个 `p<q` 和 `d in {p,q,p*q}`，需要独立构造：

```text
D(p,q,d)=(s,r,kappa,epsilon,L,(u,v),return)
```

并在不调用 Cauchy、Phi pushforward、payment、terminal table 或 canonical 后验表的条件下，独立定义 primitive row coefficient `c_W(r)`，使：

```text
c_W(r) = sum_{D(p,q,d)=r} -mu(d) log(d)
```

构造必须完成严格分支：

1. 三项若送入同一 canonical row，必须直接给出该行零系数，不能伪装成 signed seed；
2. 若存在非同-row dispatch，必须同时给 actual registration、origin selector、orientation、local factor、exact `(u,v)` 和 prepushforward identity；
3. 若任一字段只能从下游获得，则该分支不得进入 source packet，必须登记 named return；
4. 若两个 branch symbol 对同一输入给出同一 row 而 orientation/local factor 不同，必须输出最小 collision certificate，不能通过选择器消隐冲突。

这就是 `SemiprimeTriadDeclarationLineFromIndependentArithmeticIdentity` 的实际数学内容。

## 7. 它距 RH 还差什么

即使上节 declaration line 被构造出来，也只获得进入真正分析链的资格，而非 RH 本身。至少仍需：

```text
source-domain entropy
fixed exact-(u,v) polylog fiber bound
alpha/delta prepushforward identity
same-unit multiplicity control
nonzero signed-row survival
可求和的 signed family / Type-II 或等价平方根尺度输入
从该输入到 psi 平滑误差、显式公式和零点排除的独立论证
```

当前证书一致报告：

```text
mathematical_nonexistence_proved=false
rh_proved=false
row_column_unconditional_closed=false
```

本轮绝不能表述为“RH 已证”或“已获得 `ψ` 的平方根误差”。最强诚实表述是：已把当前全局乘法资料与 RH 级 signed analytic input 之间的第一个不可替代的前向缺口，压缩到最小半素数 triad 的独立 declaration line；并已验证现有五类候选都不能填补它。

## 8. 可重复验证与审稿清单

本结论由下列七份证书交叉约束：

```text
prime-matrix-mfac-rough-cofactor-mobius-signed-transport-audit.json
prime-matrix-mfac-colored-divisor-word-transport-audit.json
prime-matrix-mfac-actual-record-constructor-audit.json
prime-matrix-mfac-registration-hash-audit.json
prime-matrix-mfac-orientation-provenance-no-go-audit.json
prime-matrix-mfac-semiprime-triad-dispatch-audit.json
prime-matrix-mfac-semiprime-local-naturality-factorization-audit.json
```

审稿时应逐项确认：

1. 没有把 `global_payload_conservation_verified=true` 改写为 actual primitive binding；
2. 没有把 finite/synthetic positive fixture 改写为当前语料的 actual record；
3. 没有从 hash、LPF owner、parity 或 canonical row 反向恢复 `origin_selector`；
4. 没有把 triad 的 global 零和改写为 noncanonical dispatch；
5. 没有把局部自然性模型内的分类改写为一般数学 no-go；
6. 所有 `rh_proved=false` 与 `row_column_unconditional_closed=false` 边界仍保持显式。

推荐复核命令：

```bash
python3 -m unittest discover -s experiments -p 'prime_matrix_mfac_*_test.py' -v
python3 experiments/prime_matrix_mfac_semiprime_local_naturality_factorization_audit.py
git diff --check
```

## 9. 下一轮唯一可接受的“突破”标准

下一轮只有在提交一个可独立审稿的 `SemiprimeTriadDeclarationLineFromIndependentArithmeticIdentity` 实例时，才可称为正向数学突破。最小验收包必须同时包含：

```text
对所有 p<q 的明确定义域
非 downstream 的 declaration line
逐项 primitive row coefficient identity
actual origin/registration/orientation/local-factor/exact-(u,v) 字段
同-row 零和与非同-row dispatch 的严格分支
最小 collision 或完整性证明
prepushforward alpha/delta identity
```

在此之前，最有价值的工作是继续寻找或否证这样的独立泛函；继续增加无符号覆盖、hash、router、support 枚举或全局零和的重述，不会跨越当前硬门。
