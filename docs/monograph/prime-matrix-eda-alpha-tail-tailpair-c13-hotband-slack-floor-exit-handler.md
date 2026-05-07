# AlphaTail `C13` 热门带 `SlackFloorExit` 处理合同

**状态：** `slack_floor_exits_routed_with_pdec_or_sae_obligation`

本文接续 `prime_matrix_alpha_tail_tailpair_c13_hotband_exit_classifier.py`。目标不是把
`SlackFloorExit` 硬塞回局部 `C13` 闭合链，而是把这类出口拆成两个可审稿对象：

```text
AlphaTailHotband carrier；
Endpoint true-failure no-loss route to SAE or DirectedEndpointCRTDefect/PDEC。
```

## 1. 合同命题

设 `Hotband(beta)` 是热门带分类器输出的窗口族，`W_slack` 是其中
`exit_type=SlackFloorExit` 的子族。对每个窗口 `W=(p,B,r)` 记录同一 alpha-tail 低素平方自由块
的差值计数

\[
C_W=\max(N(r),N(-r)),\qquad C_{\max}=\max_{d\ne0}N(d).
\tag{HSF-1}
\]

若

\[
C_W\ge \beta C_{\max},
\tag{HSF-2}
\]

则该 `SlackFloorExit` 仍由热门差值能量承载，不能解释为目标生成器噪声。

同时，对 `W_slack` 内全部端点整数门槛原子使用 `C13` endpoint persistence 合同。真实失败质量

\[
\mu_{13}(J)=\max(0,1-\sigma_{13}(J))
\tag{HSF-3}
\]

按相位键无损分解：

```text
persistent true-failure key -> DirectedEndpointCRTDefect/PDEC；
nonpersistent true-failure key -> SAE；
mu_13=0 key -> NearThresholdWatchOnly。
```

因此本处理合同只声明：

```text
SlackFloorExit
=> AlphaTailHotband carrier
   and (EndpointNoFailure or DirectedEndpointCRTDefect/PDEC or SAE)。
```

若 `PDEC/SAE` 质量非零，整体行命题仍未闭合；剩余债务必须在 `PDEC exclusion` 或
`SAE local escape exclusion` 中排除。

## 2. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_hotband_slack_floor_exit_handler.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_hotband_slack_floor_exit_handler.py \
  --p-list 5003,10007 --beta 0.95 --finite-p-cut 1000 --eta 0.04 --format table
```

完整输出保存于：

```text
docs/c13_hotband_slack_floor_exit_handler_run_20260505.txt
```

## 3. 当前样本结果

`beta=0.95, P in {5003,10007}` 下：

```text
classifier_windows=18；
SlackFloorExit=7；
alpha_tail_carrier_windows=7；
endpoint_records=189；
endpoint_keys=104；
failure_records=1；
failure_keys=1；
failure_mass=3；
handler_routes={'AlphaTailHotband/EndpointNoFailure': 6,
                'DirectedEndpointCRTDefect/PDEC': 1}；
endpoint_routes={'DirectedEndpointCRTDefect/PDEC': 1,
                 'NearThresholdWatchOnly': 103}；
handler_contract_pass=True；
global_closed=False。
```

逐窗口结论：

```text
5003:8192:-144   -> AlphaTailHotband/EndpointNoFailure
5003:8192:-288   -> AlphaTailHotband/EndpointNoFailure
5003:8192:-216   -> AlphaTailHotband/EndpointNoFailure
10007:16384:-72  -> AlphaTailHotband/EndpointNoFailure
10007:16384:-1800 -> DirectedEndpointCRTDefect/PDEC
10007:16384:-144 -> AlphaTailHotband/EndpointNoFailure
10007:16384:-108 -> AlphaTailHotband/EndpointNoFailure
```

唯一真实失败键为：

```text
g900:j1-0:u2:right
```

它在 `10007:16384:-1800` 的 `m=5` 层贡献失败质量 `3`，因此不能被写成端点空失败。
它已经被命名路由到 `DirectedEndpointCRTDefect/PDEC`，但尚未被排斥。

## 4. 当前结论边界

已完成：

```text
7 个 SlackFloorExit 全部确认为 beta 热门能量承载；
端点真实失败质量无遗漏；
6 个出口无真实端点失败；
1 个出口进入 PDEC 债务。
```

未完成：

```text
排斥 DirectedEndpointCRTDefect/PDEC 键 g900:j1-0:u2:right；
扩大 beta 与 P 范围以检查 SlackFloorExit 类型分布；
把热门带样本合同升级为完整目标族生成器合同。
```

因此本更新关闭的是 `SlackFloorExit` 的无损路由接口，不是 Prime Matrix 行命题的最终无条件闭合。
