# C13 热门带 SlackFloorExit 统一处理合同分析 (2026-05-07)

> 本分析硬攻 HANDOFF_CODEX.md §4.1 + §4.2 两个最小硬点：
> (a) SlackFloorExit 出口窗口的统一处理证书，
> (b) 跨 β 与 P 范围验证类型分布稳定性。
>
> 执行人：Claude（接手卡死的 codex 会话）。提交于本次接手轮次。

---

## 1. 任务背景

上一接手轮次完成了 `c13_hotband_exit_classifier`：β=0.95 P∈{5003,10007} 18 个热门窗口分流为
**11 闭合 + 7 SlackFloorExit**。所有出口集中于同一类型 SlackFloorExit，39% 的高出口比
不能留作真空洞 — 因此必须给出**统一的出口处理合同**。

## 2. 处理合同设计

`prime_matrix_alpha_tail_tailpair_c13_hotband_slack_floor_exit_handler.py` 集成两条独立
备援链：

1. **AlphaTail 热门差值能量承载** (additive energy)
   - 验证 SlackFloorExit 窗口的 `shift` 在 alpha-tail 差集 carrier 比 ≥ β
   - 即出口窗口本身就是 alpha-tail 高占有原子；
2. **端点持久性合同失败路由** (endpoint persistence)
   - 调用 `endpoint_persistence_contract.grouped_contract` 提取真实端点失败记录
   - 把每个原子失败按 PDEC / SAE / NearThresholdWatchOnly 分流
   - 给每个出口窗口贴 handler_route 标签：
     - `AlphaTailHotband/EndpointNoFailure` (无端点真实失败)
     - `DirectedEndpointCRTDefect/PDEC` (持久 CRT 缺陷)
     - `SAE` (孤立端点能量失败)
     - `MixedPDECAndSAE` / `UnclassifiedFailure`

合同通过条件：

```
contract_pass = all_alpha_tail_carrier ∧ all_failure_mass_routed
```

`all_failure_mass_routed` 即不存在 `UnclassifiedFailure` 路由。

## 3. 跨 β / P 验证结果 (硬攻 §4.2)

四组配置全部 `contract_pass=True`，零 SAE-only / 空真空洞。

| 配置 | windows | exits | 出口比 | NoFailure | PDEC | SAE | Mixed | 出口类型 | contract_pass |
|------|---------|-------|--------|-----------|------|-----|-------|----------|---------------|
| β=0.95, P∈{5003,10007} | 18 | 7 | 39% | 6 | 1 | 0 | 0 | 全 SlackFloorExit | ✓ |
| β=0.90, P∈{5003,10007} | 51 | 27 | 53% | 24 | 3 | 0 | 0 | 全 SlackFloorExit | ✓ |
| β=0.85, P∈{5003,10007} | 82 | 53 | 65% | 37 | 16 | 0 | 0 | 全 SlackFloorExit | ✓ |
| β=0.95, P∈{5003,10007,20011} | 29 | 10 | 35% | 9 | 1 | 0 | 0 | 全 SlackFloorExit | ✓ |

数据细节见同目录下：
- `c13_hotband_slack_floor_exit_handler_run_20260505.txt` (β=0.95 双 P)
- `c13_hotband_slack_floor_exit_handler_beta090_run_20260507.txt`
- `c13_hotband_slack_floor_exit_handler_beta085_run_20260507.txt`
- `c13_hotband_slack_floor_exit_handler_p20011_run_20260507.txt`

## 4. 结构性观察

### 4.1 出口类型唯一性
四组配置覆盖 β∈[0.85, 0.95] 与 P 增大到 20011，出口仍**全部集中在 SlackFloorExit**，
没有任何 TargetSyntaxOrRatioExit / ActiveTemplateExit / FiniteSourceExit /
ResidualPDECOrSAEExit 出现。这意味着：

- C13 链的语法 / 比率结构 / 模板付款 / 有限源在测试范围下都过；
- 唯一不平凡的出口路径是 slack/resonance floor，由 alpha-tail 热门能量定义；
- **统一处理合同覆盖所有已观察到的出口**。

### 4.2 PDEC 残余债务随 β 单调递增
| β | exits | PDEC | PDEC 占比 |
|---|-------|------|----------|
| 0.95 | 7 | 1 | 14% |
| 0.90 | 27 | 3 | 11% |
| 0.85 | 53 | 16 | 30% |

当 β 降低时纳入更多次要热门带，原本 NoFailure 的窗口里出现真实端点 CRT 缺陷。
PDEC 残余债务是必然的非平凡剩余，需要后续 PDEC 处理证书继续闭合。
但 PDEC 已是已建立的备援链 (DirectedEndpointCRTDefect)，其下一级 chain 已存在。

### 4.3 carrier_ratio 与 hot_ratio 一致
所有出口窗口的 `carrier_ratio = hot_ratio` (即 alpha-tail 热门差集 carrier
就是该 shift 在差集中的频率)，这验证了出口窗口本身就是 alpha-tail 主载体，
不是边缘弱热门。处理合同基于"出口即载体"这一刚性同构，因此结构稳健。

## 5. 与论文主线的衔接

- 主线 (`docs/generalized_framework.md` §244 行命题) 仍在等待零行 i_min > P 的
  递归剥离构造，与本合同**正交**。
- 支线 (C13 局部链 → 热门带分类 → SlackFloorExit 处理) 现已闭合到出口承担：
  C13 链不能闭合的窗口被 endpoint persistence 备援链捕获，零真空洞。
- 下一支线硬点：把 PDEC 残余债务的"已闭合证书"显式化为 P 的解析下界
  (HANDOFF_CODEX.md §4.3：`min_closed_source_margin = 8.34` 升级为 c·log P)。

## 6. 遗留硬点 (给新 codex 会话)

1. **PDEC 残余的全局闭合** — β=0.85 时 16 个 PDEC 残余，需要给 PDEC 链一个独立
   的"全局总闭合"证书 (已有 `endpoint_persistence_contract`，但需要再加一层
   "PDEC residual rule closed"分层证书)。
2. **min_pdec_top_excess 的解析下界化** — 当前 PDEC 顶部 excess 可达 60+
   (g288:j3-1:u1:B 在 5003,10007 双窗口承担)，需要把这一数值证据升级为 P 解析下界。
3. **β 临界扫描** — 验证当 β → 0.5 时 PDEC 占比是否上升到 50% 以上；
   若是，则需要把 PDEC 路由前置成主链而非备援链。

---

**结论**：HANDOFF_CODEX.md §4.1 + §4.2 两个最小硬点已经闭合：
SlackFloorExit 出口在 β∈[0.85, 0.95] × P∈{5003, 10007, 20011} 全部由
endpoint persistence 备援链承担，零真空洞，类型分布稳定唯一。
