# 行命题终端三证书总收束合同

**状态：** `terminal_triad_reduction_not_closed`

本文承接 `prime-matrix-cleankls-dls-certificate-contract.md`。截至当前结构链，早期零行反例已经不能再
作为无名容量失败、无名斜线逃逸、无名轮筛层叠或无名高频同步继续游走。所有剩余责任必须落入三类
可审稿终端证书：

```text
A. PDEC family certificates；
B. LocalSurvivorCert family；
C. CleanKLS/DLS certificates or explicit ExternalKLS input。
```

本文的目标是固定这三类证书的总接口、互相回流规则和“无第四出口”原则。本文仍不是最终无条件证明；
最终证明还需要提交三类证书的全集，或给出明确外部输入。

## 1. 统一反例账本

设 `(P,y)` 是最小早期零行反例。取任意动态底座 `Y(P)` 和高标签分块账本。低骨架为

\[
S_Y(P,y)=\{d: 1\le d<P,\ Py-d\ {\rm 避开所有}\ q\le Y\}.
\]

高标签覆盖用 formal unit 记录：

```text
Omega(P,y) = {(d,q,m): Py-d=qm, Y<q<P, q prime, m rough/admissible}；
pi(d,q,m)=d。
```

若该行为零行，则

\[
S_Y(P,y)\subseteq \pi(\Omega(P,y)).
\tag{TCT-1}
\]

把模型主项、已剥离低模/短窗/列位移/尾锚责任扣除后，得到剩余支付义务：

\[
R(P,y)\le \sum_{\mathcal B} E_{\mathcal B}^{+}.
\tag{TCT-2}
\]

这里每个 `E_B` 是一个分块、签名层或频率层的中心化正超额。行命题闭合的结构任务就是证明
`(TCT-2)` 不可能成立；若成立，则它必须输出一个可命名缺陷证书。

## 2. 三分准则

对任一剩余正超额族 `E_B^+`，按下列优先级分类：

```text
Persistent:
  同一有限/可升层签名在反例族中承担正比例责任。
  => PDEC family。

Sparse:
  责任只集中在有限孤窗、端点、短弧或有限列块，不能形成稳定密度。
  => LocalSurvivorCert family。

Flat:
  已无低模峰、短窗峰、列/Bohr cap、尾锚、gcd/unit 异常和口径混合。
  => CleanKLS/DLS。
```

这个三分不依赖固定常数。阈值可以随证明阶段自归一化选择；一旦某阈值分类失败，失败对象必须成为更
尖锐的 `Persistent` 或 `Sparse` 证书，而不是生成新类型。

## 3. A 类：PDEC family certificate

PDEC 证书统一登记：

```text
formal unit Omega；
signature group G；
bad-window/count function g:G->R_{\ge0}；
zero-mean test F:G->C；
lower bias L_PDEC；
admissible capacity upper U_CRT；
route source: low-mod / cofactor / displacement / Bohr-cap / endpoint / weighted / primitive / profinite。
```

验收目标是：

\[
U_{\rm CRT}<L_{\rm PDEC}.
\tag{TCT-3}
\]

若 `(TCT-3)` 失败，则由 `PDEC-Dual-Failure` 合同给出 cap localization：

```text
persistent cap => refined PDEC / displacement PDEC / ColumnCRT-absorbed PDEC；
sparse cap     => LocalSurvivorCert；
口径不一致     => Multiplicity-Stitching，再回到 weighted/primitive PDEC 或 CleanKLS；
no cap         => 原方向上界成立。
```

固定签名群内 refined cap 不能无限循环；不断升层时进入 `new-layer tower entropy` 二分：

```text
熵/能量发散   => finite/profinite PDEC or ColumnCRT-absorbed PDEC；
熵/能量可求和 => CleanKLS/DLS；
层间口径不一 => Multiplicity/Stitching，再回流。
```

所以 PDEC 失败只会产生更窄 PDEC、LocalSurvivor 或 CleanKLS，不产生第四出口。

## 4. B 类：LocalSurvivorCert family

局部证书统一登记：

```text
isolated window I；
candidate set C(I)；
blockers B_j(I): low-factor / tail-cofactor / displacement / endpoint-seam / core-overlap；
projection map from blockers to physical candidates；
optional descent target。
```

验收目标是二选一：

```text
给出 witness n0 in C(I) 未被任何 blocker 覆盖；
或证明 |union_j B_j(I)|<|C(I)|。
```

若局部证书失败，则覆盖者必须承担解释责任：

```text
同类 blocker 在无限反例族中复现 => PDEC family；
支撑真缩小                      => 更小 LocalSurvivorCert；
下降阻断                        => TotalDescent/RPZ seam，再进 PDEC/LocalSurvivor；
formal unit 不一致              => Multiplicity/Stitching，再回流。
```

固定孤窗内候选集有限，因此支撑真缩小不能无限发生。若孤窗类型无限复现，按鸽巢原理变成 persistent
签名，回到 PDEC。

## 5. C 类：CleanKLS/DLS certificate

Clean 分支只有在下列 admission 全部通过后才可调用：

```text
K1 ranges；
K2 lowmod orthogonality；
K3 no short-window cap；
K4 no column/Bohr cap；
K5 coefficient L2-flat；
K6 gcd/unit strata；
K7 formal unit consistency。
```

通过后必须提交：

```text
内部 LargeSieve/DLS/KLS 不等式，证明 |E|<R；
或明确外部 KLS/DI/BFI 输入及变量适配表。
```

若 admission 失败：

```text
K2/K4/K5/K6 fail => PDEC family；
K3 fail          => LocalSurvivorCert or refined PDEC；
K7 fail          => Multiplicity/Stitching，再回流。
```

若 admission 通过但大筛界失败，则大筛对偶输出系数集中、频率相关、短窗端点主导或 gcd 层异常，
分别回流到 PDEC 或 LocalSurvivor。因此 CleanKLS/DLS 也不是黑箱出口。

## 6. 无第四出口定理

**Terminal Triad Reduction.** 假设所有上游合同成立：

```text
SN unnamed closure；
NamedExit absorption；
PDEC dual-failure absorption；
PDEC cap no-cycle；
new-layer entropy dichotomy；
Multiplicity/Stitching absorption；
TailAnchor/Cofactor absorption；
ColumnCRT displacement absorption；
SAE LocalSurvivor reduction；
CleanKLS/DLS certificate contract。
```

则任意最小早期零行反例必须给出 A、B、C 三类对象之一；且任一对象验收失败，只能回流到 A、B、C
中的另一个或更细同类对象。

证明要点是：所有上游命名缺陷已经被写成有限签名、孤立支撑或 clean 平坦残余三种形态。有限签名的
持久偏斜是 PDEC；孤立支撑是 LocalSurvivor；无签名无孤立支撑的剩余满足 Clean admission，进入
KLS/DLS。固定层递归由有限原子数终止；无限升层由熵二分终止；口径混合由 formal unit 规范化吸收。
因此不存在第四类可持续逃逸。

## 7. 当前未闭合义务

终局证明仍需提交以下全集之一：

```text
PDEC family certificates:
  explicit/profinite/weighted/primitive/cofactor/displacement/gcd-stratum 全部 U_CRT<L_PDEC；

LocalSurvivorCert family:
  所有孤窗候选集的 witness 或 blocker 覆盖不足证书；

CleanKLS/DLS:
  所有 clean residual 的内部大筛证书，或明确 ExternalKLS 输入。
```

如果继续走完全自足路线，下一最小硬点应优先攻：

```text
Triad-A1: 对同一坏窗集合建立 PDEC capacity upper U_CRT；
Triad-B1: 对所有稀疏孤窗建立 LocalSurvivor witness；
Triad-C1: 对 clean residual 建立统一 L2-flat 大筛界。
```

其中 A1 是当前最可直接连接前序 `H4-PDEC` 与 `Column displacement` 文档的硬点。

新增 `prime-matrix-triad-a1-pdec-capacity-upper-route.md` 后，A1 被进一步固定为同一坏窗集合上的
容量上界协议：

```text
Same-Set Law；
Attachment / PhaseCompat / ConditionalRouting；
LP/dual upper U_CRT；
U_CRT<L_PDEC 或输出 AttachmentFail/PhaseCompatFail/DualCap/RoutingGap。
```

这把 PDEC 上界侧从“找一个常数”改写为“证明集合嵌入、相位兼容和对偶容量”的结构任务。

新增 `prime-matrix-triad-a1-terminal-reduction-after-liftd.md` 后，A1 的 new-layer 子分支已进一步
接入本终端三分。其机器路由当前为：

```text
route_counts={'LiftFiberDeletion': 6}；
triad_counts={'ContinueLiftOrSparse': 6}。
```

这说明当前物化层仍由删除势支付；若删除势发散，进入 Sparse/LocalSurvivor 或容量矛盾。若删除势
可求和，则 Lift-D 的 `NoDeletion-KL` 门控强制转入：

```text
KL 发散  => PDEC family；
KL 可求和 => CleanKLS/DLS admission。
```

因此 A1 的当前最窄硬点可重写为：

```text
DeletionPotential divergence
or PDEC/CleanKLS terminal certificate。
```

## 8. 结论

当前主链可诚实表述为：

```text
早期零行反例
=> 统一反例账本 (TCT-1)(TCT-2)
=> Persistent / Sparse / Flat 三分
=> PDEC / LocalSurvivor / CleanKLS 三终端证书
=> 证书失败仍回流三终端，无第四出口。
```

这完成的是终端接口总收束和递归无逃逸结构，不是最终无条件闭合。最终闭合必须继续把三类证书逐项物化。
