# 合著稿命题状态纪律

本文档完成外审前 H10 义务：把合著稿中每类命题的状态、可允许结论、必须附件和禁止越界用法固定为可审稿规则。

## 0. 结论

当前合著稿可以作为统一矛盾场理论、依赖图、证书包和条件链审稿稿件推进；不得把尚未闭合的 Prime Matrix 终局、二点筛终局或 RH 终局写成无条件定理。

状态工程的目标不是降低数学标准，而是防止以下错误：

1. 把 `Reduction-closed` 写成 `Proved-in-text`；
2. 把 `External-theorem closed` 写成完全自足证明；
3. 把 `Computational-certificate` 写成无限尾段证明；
4. 把 `Referee-block` 写成外审已接受定理；
5. 把 `Not claimed` 的 RH 终局写成已证结论。

## 1. 状态等级

| 状态 | 含义 | 可使用结论 | 禁止越界 |
|---|---|---|---|
| `Proved-in-text` | 文内逐行证明已完成 | 可作为本文内部定理引用 | 不得隐藏外部深输入 |
| `Reduction-closed` | 已归约到更小命名接口 | 可引用归约命题 | 不得引用为终局排斥 |
| `External-theorem closed` | 接受明确外部定理后闭合 | 可在“引用外部定理”条件下使用 | 不得宣称完全自足 |
| `Computational-certificate` | 有有限证书或脚本复现 | 可闭合有限范围或证书子模块 | 不得替代无限尾段证明 |
| `Referee-block` | 作者侧组织完成但需逐行复核 | 可作为审稿包提交 | 不得作为已验定理使用 |
| `Not claimed` | 本稿不主张该终局 | 只能作为研究方向或条件目标 | 不得进入主定理结论 |

## 2. 必须附件

| 状态 | 必须具备 |
|---|---|
| `Proved-in-text` | 定义、引理、证明、依赖列表、无外部未命名输入 |
| `Reduction-closed` | 起点命题、终点接口、双向/单向方向、失败时状态 |
| `External-theorem closed` | 外部来源、变量替换、适用范围、损失吸收账本 |
| `Computational-certificate` | 脚本、输入参数、输出文件、复现命令、字节级或哈希核查 |
| `Referee-block` | 审稿矩阵、逐项义务、未决接口、风险说明 |
| `Not claimed` | 明确禁止作为当前定理引用的声明 |

## 3. 当前主线状态

| 主线 | 当前最高诚实状态 | 原因 |
|---|---|---|
| Prime Matrix 行列命题 | `Reduction-closed / Referee-block` | BPN-LHB 子模块已闭合，但 Structured-EHPD、PDEC/SAE/Rankin、RRD/OSPC 仍是终局硬接口 |
| 二点筛 BMD 子链 | `External-theorem closed` | H7 已完成 DI/BFI 到 KLS-window 的外部深定理适配 |
| 二点筛素数对终局 | `Reduction-closed / Referee-block` | H8 仍需证明 `BMD=>TLI` 无隐藏下界和无 parity gap |
| RH 反例矛盾场 | `Verification package / Not claimed` | controlled exits 尚未逐行无条件闭合 |
| BPN-LHB 子模块 | `Computational-certificate + External-theorem closed` | H3 已完成五段证书与 RS1962 尾段常数账本 |

## 4. 主稿写法规则

1. 每个定理标题或前后段落必须出现状态标签，除非该定理明显是基础定义或形式恒等式。
2. 凡出现 `External-theorem closed`，必须同时给外部定理名称或索引路径。
3. 凡出现 `Computational-certificate`，必须给脚本路径、输出路径和复现命令位置。
4. 凡出现 `Referee-block`，不得使用 “therefore the main theorem is proved” 类型结论。
5. 凡涉及 RH，必须保留 `Not claimed` 或 `verification package` 口径，直到 controlled exits 全部独立闭合。

## 5. 升级条件

### 5.1 Prime Matrix 终局升级

必须至少完成以下之一：

```text
Structured-EHPD exclusion
```

或

```text
RHI / PM-R2B / RSE
=> Structured-EHPD exclusion
```

并同时闭合 PDEC/SAE/Rankin/RRD/OSPC 常数账本。

### 5.2 二点筛终局升级

必须证明：

```text
BMD => BST-2 => BST => TLI
```

且逐项排除隐藏素数对下界、Buchstab transfer parity gap 和筛余非空性偷用。

### 5.3 RH 终局升级

必须把所有 controlled exits 写成同一负载约定下的逐行定理，并证明：

```text
off-critical zero anomaly
=> one controlled exit fires
=> each exit contradicts the global nonnegative ledger.
```

在完成前，RH 主结论保持 `Not claimed`。

## 6. 审稿前机械检查

建议每次归档前执行：

```bash
rg -n "unconditional proof|RH is proved|twin prime.*proved|Goldbach.*proved" docs paper
rg -n "External-theorem closed|Referee-block|Not claimed|Reduction-closed" docs/monograph paper/contradiction-field-monograph
git diff --check
```

第一条用于检查是否出现越界声明；第二条用于确认状态标签仍可追踪。

## 7. H10 当前状态

H10 已完成作者侧状态分级工程：

1. 主稿已有 `Claim Status Legend`；
2. 主稿已加入状态专用 theorem-like 环境；
3. 本文档给出状态纪律、升级条件和机械检查；
4. `pre-external-referee-remaining-obligations.md` 与 `claim-status-table.md` 已同步。

剩余属于编辑优化：把历史章节中的所有普通 theorem 环境逐步替换为状态专用环境。这不改变数学闭合状态。
