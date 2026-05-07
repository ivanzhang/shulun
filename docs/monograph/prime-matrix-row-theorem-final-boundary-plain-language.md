# 行命题最终边界闭合的通俗说明

## 1. 一句话结论

当前真正闭合的是一个精确边界命题：

```text
Triad-A1 same-set capacity / full-S terminal
在 canonical RIW/Buchstab source branch 上已经自足闭合。
```

更通俗地说：如果 A1 链条使用的是已经锁定来源的 canonical RIW/Buchstab 决策树权重，那么同一坏窗集合上的容量上界、来源账本、分支覆盖和最终评审已经全部对齐，没有剩余内部门。

## 2. 不能扩大成什么

它不能被改写成下面这个更强命题：

```text
Unrestricted generic full-S well-factorable WFD self-contained theorem
```

原因不是还差一点证明，而是 moving-delta no-go 已经给出反证模型：在当前形式假设下，generic WFD 源可以把容量集中到一个移动块上，从而破坏所需的反原子输入。因此这个宽口径 generic 自足版不是“待闭合缺口”，而是“不能声明的命题”。

## 3. 几何直觉

可以把当前边界理解成三层：

1. **canonical 源头层**：斜线、圆柱绕回、同余覆盖和容量账本都来自同一套 RIW/Buchstab 决策树来源。这里的来源账本已经闭合。
2. **generic WFD 宽口径层**：允许任意 well-factorable 源头。这个层太宽，moving-delta 模型显示它能产生当前证书无法排除的移动原子，所以不能说自足闭合。
3. **外部深定理层**：如果接受 FullS-KLS-ext 外部合同，generic 外部版可走外部定理路由，但这不是 canonical-source 自足证明的一部分。

所以最终边界不是“所有可能源头都被内部证明”，而是“精确限定源头后，内部链条完全闭合；未限定源头的强版本被反证并隔离”。

## 4. 证明链条的核心检查

最终评审文件：

```text
docs/monograph/prime-matrix-triad-a1-self-contained-theorem-boundary-review.md
```

给出的评审裁定是：

```text
APPROVE_CANONICAL_SOURCE_SELF_CONTAINED_BOUNDARY
```

七个门控全部通过：

- 定理陈述边界精确；
- final closure certificate 无开放门；
- same-set capacity frontier 已吸收最终边界；
- actual source provenance 已闭合到 canonical RIW/Buchstab；
- canonical/generic 分支没有静默混用；
- unrestricted generic 自足版被记录为反证，不被误称为闭合；
- 外部 FullS-KLS-ext 合同与自足声明保持分离。

终端状态为：

```text
NoFurtherTheoremBoundaryReviewGap
```

## 5. 与完整行命题的关系

这一步闭合的是行命题攻关中的一个终端边界：`Triad-A1` 的 canonical-source self-contained boundary。

它不自动等于整个 Prime Matrix 行/列命题已经无条件闭合。合著主线中仍需单独处理的全局终端证书包括：

- `PDEC family certificates`
- `LocalSurvivorCert family`
- `CleanKLS/DLS certificates or explicit ExternalKLS input`
- 以及主稿中仍标注的 D-structure/Tail-log4/Rankin/referee-block 接口。

因此当前最诚实的说法是：

```text
canonical-source 自足边界已完全闭合；
unrestricted generic 自足版已反证；
整条 Prime Matrix 行/列无条件定理仍需剩余终端证书排斥。
```

## 6. 最新前沿边界

继续接入 `NC-BLK` 边界核查、非二点 `PDEC` 准入审计和全局终端家族边界路由器后，当前前沿进一步压成：

```text
CurrentMaterializedFrontierExhausted_GlobalTerminalFamiliesOpen
```

通俗地说：现在已经没有一个“当前已物化的局部样本”可继续消元。`PDEC` 侧当前合法非二点候选为 `0`，`LocalSurvivor` 侧开放包为 `0`，已知 sparse 入口全部有准入路线，`NC-BLK` 也不再是无名出口。

剩下的唯一大门是：

```text
GlobalTerminalFamilyExclusionCertificates
```

也就是必须证明所有未来可能出现的 `PDEC family`、`LocalSurvivorCert family`、`CleanKLS/DLS` 终端对象都能被证书排除，或明确引用外部/referee 输入。这仍不是最终行/列无条件定理闭合，但它把“最后剩余是什么”压到了当前最窄、最清晰的形式。

继续拆分后，这个唯一大门又被压成更具体的三项：

```text
PDEC_CAP:
  证明同一坏窗集合上的容量上界 U_CRT<L_PDEC；

KLS_EXT_OR_INTERNAL_LARGE_SIEVE:
  证明 L2-flat clean residual 的内部大筛吸收，
  或明确外部 KLS/DI/BFI 输入；

DStructureRankinReferee:
  D-structure/Tail-log4/finite Rankin 接口通过独立审稿。
```

其中 LocalSurvivor 当前包、已知 sparse 入口、NC-BLK 旧出口和连续终端二分都不再是独立剩余。完全自足路线的最窄目标现在是：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve
```

最新自足瓶颈路由又把这一项压窄：

```text
experiments/prime_matrix_self_contained_terminal_bottleneck_router.py
docs/monograph/prime-matrix-self-contained-terminal-bottleneck-router.md/json

closed_nonfinal_reductions=true；
internal_clean_kls_independent_blocker_collapsed=true；
self_contained_terminal_bottleneck_is_pdec_cap=true；
narrowest_self_contained_hardpoint=PDEC_CAP_SameSetGlobalDualCertificate。
```

通俗说，`CleanKLS` 现在不再作为完全自足路线里的平行独立终端硬点：它失败时会给出对偶集中并回到 `PDEC/SAE`，在 canonical-source 分支中已经被同集容量边界吸收，而 unrestricted generic 版本已经被反证隔离。剩下的自足核心就是同一批坏窗上的全局容量不等式：

```text
U_CRT < L_PDEC
```

这仍不是完整行/列无条件定理闭合，因为还必须通过 `DStructureRankinReferee` 晋级门。

继续进入这个 `PDEC-CAP` 内部后，最新路由给出：

```text
experiments/prime_matrix_pdec_cap_same_set_global_dual_router.py
docs/monograph/prime-matrix-pdec-cap-same-set-global-dual-router.md/json

closed_current_materialized_pdec_gates=true；
pdec_cap_same_set_global_dual_closed=false；
narrowest_next_hardpoint=SameSetPDECDualComparisonForPersistentMFU_OR_DiffuseGlobalDeletionOrSC9。
```

通俗地说，当前已经不是继续调一个固定低模层上的 Fourier 常数。已知的 PDEC 失败帽都能追到同一质量来源，早期行出口已经接线；持久帽进入升层删除势或 NoDeletion-KL；强制持久帽进入多桶实际支付缝合。继续新增的 APS 投影塔二分路由器又把“真实支付图会不会持久缝合”的逻辑二分闭合了：

```text
真实支付图 Gamma 在无穷投影塔中，
要么持久命中某个有限候选签名 -> 多桶 PDEC；
要么对所有有限候选签名都不持久 -> 分散 CleanKLS/DLS；
若升层持续删除，则递推剥离；
若删除停止但 KL/互信息偏斜，则回流 new-layer/refined PDEC。
```

继续攻入不持久 `Gamma` 分支后，新增 diffuse 终端分裂路由器：

```text
experiments/prime_matrix_pdec_cap_diffuse_terminal_split_router.py
docs/monograph/prime-matrix-pdec-cap-diffuse-terminal-split-router.md/json

diffuse_terminal_split_closed=true；
self_contained_diffuse_terminal_closed=false；
narrowest_diffuse_hardpoint=
  GlobalDeletionDivergenceOrSupportExhaustion_OR_SelfContainedKuznetsovLSAtomSC9。
```

通俗说，不持久分支不再只是“删除势 / NoDeletion / CleanKLS”这个宽口径描述。现在链条已经拆成：

```text
持续删除 -> 需要证明全局删除势发散会耗尽可覆盖支撑；
删除停止 + KL/互信息偏斜 -> 回流 refined/new-layer PDEC；
删除停止 + KL/互信息平坦 -> CleanKLS/DLS；
CleanKLS 的 K1--K9 任一失败 -> 回流 PDEC/SAE/Multiplicity/Promotion；
K1--K9 全过 -> 外部 KLS 版可引用深定理，自足版剩 SC-9。
```

所以当前真正剩余是更窄的二选一终端估计：

```text
持久 Gamma：证明 U_CRT^multi < L_PDEC^multi；
不持久 Gamma：证明 GlobalDeletionDivergenceOrSupportExhaustion，
              或证明 SelfContainedKuznetsovLSAtomSC9。
```

## 7. 已并入合著的文件

主稿已并入：

```text
paper/contradiction-field-monograph/contradiction-field-monograph.tex
```

合著理论总览已并入：

```text
docs/monograph/combined-monograph-directory-and-theory-system.md
```

状态总表已并入：

```text
docs/monograph/claim-status-table.md
```
