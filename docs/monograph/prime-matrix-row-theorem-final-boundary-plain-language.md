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
