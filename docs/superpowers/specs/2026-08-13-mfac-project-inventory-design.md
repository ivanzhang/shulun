# MFAC 全项目模块清单与保守状态归类设计

**日期：** 2026-08-13

**状态：** 已确认设计，待用户审阅书面规格

## 1. 目的

本阶段不尝试证明任何新的解析不等式，也不将有限数值、条件链或已有审计证书
升级为 RH 证明。目标是可复现地扫描全项目的 MFAC 审计模块及其默认 JSON 证书，
为后续 RH 主链依赖图提供唯一、可机检的模块清单与保守状态归类。

扫描范围仅限下列命名约定：

- 模块：`experiments/prime_matrix_mfac_*_audit.py`；
- 默认机器证书：`docs/monograph/prime-matrix-mfac-*-audit.json`。

其中模块 stem 从 `prime_matrix_mfac_` 转成 `prime-matrix-mfac-`，再追加
`-audit.json`。缺失、不可读或非 JSON 证书都必须显式记录，不能用 Markdown、
测试名称或有限实验输出补推状态。

## 2. 输入、输出与可复现性

新增扫描器接收仓库根目录或显式的 `experiments`、`docs/monograph` 路径；按文件名
字典序枚举模块，以保证相同文件树得到相同的 JSON 和 Markdown 排序。

默认 CLI 写出：

- `docs/monograph/prime-matrix-mfac-project-inventory-audit.json`；
- `docs/monograph/prime-matrix-mfac-project-inventory-audit.md`。

JSON 每行模块记录至少包含：模块相对路径、预期证书相对路径、证书可用状态、
抽取出的 `rh_proved`、`status` 与所有名称含 `status` 的顶层字段、分类、以及
阻断 RH 闭合的明确理由。Markdown 提供模块总数、各分类计数、按模块排序的表格、
缺失/不可读证书列表，并逐项陈述扫描的非证明边界。

扫描器只读取文件，不导入或执行 MFAC 模块，也不生成或覆盖任何已有模块证书。

## 3. 保守归类规则

对每个模块记录，分类使用以下固定优先级：

1. `missing_or_unreadable_certificate`：预期 JSON 不存在、不能 UTF-8 读取、不能
   解析为 JSON，或顶层 JSON 不是 object；
2. `conditional_or_external_dependency`：任一抽取字段名或字符串值含
   `conditional`、`external`、`assumed`，或 `rh_proved` 缺失/不是内建布尔值以外
   且显示依赖外部输入；
3. `open_or_unresolved`：任一 `status` 字段或字符串值含 `open`、`unproved`、
   `unresolved`、`not_closed`，或 `rh_proved` 明确为 `false`；
4. `finite_verified_only`：证书可读、未命中上述关键词、有明确有限证据字段，
   但仍不提供可机检 RH 闭合证明；
5. `requires_manual_rh_review`：仅当 `rh_proved` 明确为内建 `true` 时允许，且
   绝不归类为 `rh_closed`。

关键字匹配使用小写化后的字段名和字符串序列化值；对未知值宁可归为
`open_or_unresolved`，不作乐观推断。任何 `rh_proved=false` 都是 RH 阻断理由，
即使同时存在有限恒等式、数值扫描或局部闭合字段。

## 4. RH 边界

阶段 1 的顶层输出固定包含：

```text
rh_proved=false
rh_closed_module_count=0
inventory_status=conservative_index_only
```

即使发现某个未来证书声称 `rh_proved=true`，扫描器也只报告
`requires_manual_rh_review`，并将顶层 `rh_proved` 保持为 `false`。扫描器不检查
数学证明的正确性，因此不能凭字段文本认证 RH。

## 5. 测试与验收

单元测试必须在临时目录构造最小文件树，覆盖：

1. 模块到证书的确定性路径匹配与字典序输出；
2. 缺失证书、坏 JSON、非 object JSON 的显式登记；
3. `conditional`/`externally_assumed` 归类为条件或外部依赖；
4. `unproved`、`unresolved`、`open` 和 `rh_proved=false` 归类为开放或未闭合；
5. 没有开放关键字的有限证书仍只归为 `finite_verified_only`；
6. `rh_proved=true` 只能进入人工复核，不得输出 `rh_closed`；
7. JSON/Markdown 证书保持固定 RH 边界；
8. CLI 从脚本路径运行并写出两种默认/指定输出。

阶段 1 完整实现后，运行新模块测试、全量 MFAC 测试和 `git diff --check`；通过后
只暂存本阶段新增的扫描器、测试、规格、计划及库存证书并创建独立 Git 提交。

## 6. 非目标

- 不证明 RH、Mertens、PNT、零自由区、Mellin 收缩、L²--Upper 或 Mass--Lower；
- 不以测试通过、文件存在或数值读数推断全局解析结论；
- 不修改已有 MFAC 审计器的接口或已有默认证书；
- 不将全文 Markdown、源代码注释或 Git 历史作为状态推断来源；
- 不在本阶段绘制 RH 主链；该工作属于阶段 2，并以本库存 JSON 为输入。

## 使用示例

```bash
python3 experiments/prime_matrix_mfac_project_inventory_audit.py \
  --repo-root . \
  --json-out /tmp/mfac-project-inventory.json \
  --markdown-out /tmp/mfac-project-inventory.md
```

该命令只生成保守模块索引；它不执行被索引模块，也不会证明任何 RH 相关命题。
