# RPZ 双轨攻坚闭合路线

**状态：** `rpz_dual_track_routes_to_named_exits_or_p2_descent`

本文承接 `prime-matrix-rpz-bcb-endpoint-persistence-route.md`。当前 RPZ 主链已经把单窗分散、
滑动平台、边界压缩、网格端点失败逐层压缩。现在同步推进两个目标：

```text
Track A：SAE/PDEC/ColumnCRT 证书闭合；
Track B：下层 h-筛零行递归下降。
```

二者不是重复路线。Track A 处理所有端点/持久相位出口；Track B 处理 BCB-Core 已经给出的
完整下层零行。

## 1. Track A：出口证书接口

端点失败相位

\[
\tau=(h,\ N\bmod h,\ u\bmod h,\ \Delta)
\]

已经由 `prime-matrix-rpz-bcb-endpoint-persistence-route.md` 路由为：

| 分支 | 输入 | 验收义务 |
|---|---|---|
| `SAE` | 每个端点相位负载 `<=B_SAE` | 给出有限孤立窗口证书，或证明 survivor/lift/higher-defect |
| `PDEC` | 某端点相位负载 `>B_SAE` 且跨平台持久 | 接入 `h4-pdec-certificate-template.md`，证明同一坏窗集合的 `U_CRT<L_PDEC` |
| `ColumnCRT` | 持久端点相位同时携带列位移/标签余类 | 接入 `h4-pdec-column-defect-routing-contract.md`，给出非零位移余类负载证书 |

因此 Track A 的下一步不是再定义端点失败，而是物化三类证书：

```text
RPZ-SAE finite package；
RPZ-PDEC endpoint phase row；
RPZ-ColumnCRT endpoint displacement row。
```

## 2. Track B：下层零行递归下降定理

设 `p>2`，`r` 是 `p` 的前一素数。若 `p` 对齐行

\[
I=[(a-1)p+1,\ ap]
\]

是 `p`-筛零行，则剥到 `r` 层后，`r`-筛幸存者只能来自端点

\[
ap=p\cdot a,
\]

且该端点实际复活当且仅当 `(a,P(r))=1`。

**Lemma RPZ-LowerDescent（下层零行下降）。**
在上述条件下，若 `I` 完整包含一条 `r` 对齐行 `J`，且 `J` 不含端点穿孔 `ap`，
则 `J` 是 `r`-筛零行。

**证明。**
若 `n∈J` 是 `r`-筛幸存者，则因为 `I` 是 `p`-筛零行，`n` 必须被某个素数 `ell`、
`r<ell<=p` 整除。由于 `r,p` 相邻，唯一可能是 `ell=p`。而 `I` 的长度为 `p`，其中
`p` 的倍数只有端点 `ap`。若 `J` 不含该端点，则这样的 `n` 不存在。证毕。

当递归到 `p=2` 时，任意 `2` 对齐行 `[2m-1,2m]` 且 `m>1` 都含奇数 `2m-1`，不可能是
`2`-筛零行。因此若下降路径到达 `p=2`，反例分支直接矛盾。

## 3. 有限下降审计

新增审计：

```text
experiments/prime_matrix_rpz_lower_zero_descent_audit.py；
docs/monograph/prime-matrix-rpz-lower-zero-descent-audit.json；
docs/monograph/prime-matrix-rpz-lower-zero-descent-audit.md。
```

审计输入为 `prime-matrix-rpz-bcb-core-audit.json` 中的
`would_be_zero_rows_after_tail_deletion`。结果：

| 指标 | 数值 |
|---|---:|
| 起始条件下层零行数 | `6` |
| 到达 `p=2` 直接矛盾的起始支数 | `6` |
| 被端点穿孔或网格缺口阻断的节点数 | `0` |
| 含端点穿孔的节点数 | `7` |
| 最大下降深度 | `5` |

这说明样本中 Track B 不需要调用出口证书：每条 BCB 下层零行都可递归下降到 `p=2`。

## 4. 下降阻断相位账本与证书材料化

新增审计与接口：

```text
experiments/prime_matrix_rpz_lower_descent_obstruction_ledger.py；
docs/monograph/prime-matrix-rpz-lower-descent-obstruction-ledger.json；
docs/monograph/prime-matrix-rpz-lower-descent-obstruction-ledger.md；
docs/monograph/prime-matrix-rpz-certificate-materialization-interface.md。
```

对每个相邻素数转换 `p -> r`，下降是否被阻断只依赖行号模

\[
P(r)=\prod_{\ell\le r}\ell.
\]

阻断被分成两类：

```text
grid_fail：p 行不完整包含任何 r 对齐行；
puncture_block：完整 r 行全部被端点 p*a 穿孔。
```

有限下降树中的实际转换节点数为 `20`，实际状态全部为 `success`，实际阻断节点为 `0`。
枚举相位表同时显示，可能的 `grid_fail` 相位是有限账本对象，`puncture_block` 在本批相位中密度为
`0`。因此全局证明若遇到下降阻断，不再产生新逃逸，而是进入：

```text
RPZ-SAE-FIN；
RPZ-PDEC endpoint phase row；
RPZ-ColumnCRT endpoint displacement row。
```

这一步只完成“阻断相位可命名、可证书化”的接口，不排除 `SAE/PDEC/ColumnCRT`。

进一步新增：

```text
experiments/prime_matrix_rpz_certificate_skeleton_builder.py；
docs/monograph/prime-matrix-rpz-certificate-skeleton-package.json；
docs/monograph/prime-matrix-rpz-certificate-skeleton-package.md。
```

骨架包抽取出 `2` 个 endpoint `RPZ-SAE-FIN` 候选，`2` 条 endpoint `PDEC/ColumnCRT` 行，
以及 `3` 条 lower-descent `grid_fail` 的 `PDEC/ColumnCRT` 行。LowerDescent 的可能阻断相位
共 `1752` 个，全部属于 `grid_fail`；`puncture_block` 行为 `0`。

新增：

```text
experiments/prime_matrix_rpz_endpoint_sae_finite_certificate.py；
docs/monograph/prime-matrix-rpz-endpoint-sae-finite-certificate.json；
docs/monograph/prime-matrix-rpz-endpoint-sae-finite-certificate.md。
```

该证书核验两个 endpoint 候选在当前 BCB 账本中的 `possible load=2`、`actual load=0`，
所以当前有限账本的 `candidate_windows` 为空，endpoint `RPZ-SAE-FIN` 真空闭合。它不是全局
`SAE` 排斥；若正式反例族实际命中这些相位，仍需逐窗证书或进入 `PDEC/ColumnCRT`。

继续新增：

```text
experiments/prime_matrix_rpz_lower_grid_fail_avoidance_certificate.py；
docs/monograph/prime-matrix-rpz-lower-grid-fail-avoidance-certificate.json；
docs/monograph/prime-matrix-rpz-lower-grid-fail-avoidance-certificate.md。
```

该证书把三条 lower-descent `grid_fail` 行化为闭式判据。若 `g=p-r`、`a` 是 `p` 行号，则

```text
delta = -(a-1)g mod r；
grid_success iff delta<=g。
```

当前下降树 `20` 个实际转换节点全部满足该不等式，实际 `grid_fail` 节点为 `0`；闭式计数与
相位枚举不一致数为 `0`。这仍是当前账本避开证书，不是全局正式下降路径避开证明。

新增 `prime-matrix-rpz-formal-descent-phase-inequality.md` 后，逻辑边界进一步澄清：
一旦一条正式下降路径已经存在，即每步有完整下层行包含且不被端点穿孔阻断，则
`delta<=p-r` 由网格判据自动成立。真正未闭合的是正式下降路径的全局存在性；若不存在，
第一处失败必为 `grid_fail` 或 `puncture_block` 有限相位，并回到 `SAE/PDEC/ColumnCRT`。

新增 `prime-matrix-rpz-first-obstruction-dichotomy.md` 后，首阻断进一步收窄：端点穿孔不能阻断
完整下层行。若完整 `r` 行包含端点 `ap`，则其右端点必须等于 `ap`，从而 `r|a`；但端点实际复活
要求 `a` 避开所有 `<=r` 素数，矛盾。因此不下降分支的唯一首阻断是 `grid_fail` seam 相位。

新增 `prime-matrix-rpz-first-grid-fail-seam-certificate.md` 与脚本
`experiments/prime_matrix_rpz_first_grid_fail_seam_certificate.py` 后，该 seam 被材料化为双帽标准形：
`g<delta<r`，左右帽长为 `delta` 与 `r+g-delta`，缺口总量恒为 `r-g`，且 `r`-筛幸存者至多为右端点
`ap`。证书抽取 `12` 个 seam 相位行，覆盖完整 `Q` 中 `1752` 个 grid_fail 相位，源账本计数不一致为 `0`。

该证书现在进一步输出每条 seam 的 `PDEC/ColumnCRT` 增强包：

```text
PDEC support:
  S_tau={a mod Q: a≡rho mod r}
  F_tau=1_{rho}-1/r
  Fourier support={jQ/r: 1<=j<r}

Endpoint split:
  endpoint killed by lower labels: 1348 phases
  endpoint Q-unit branch: 404 phases
```

因此 lower-descent grid_fail 不再是三条粗粒度 PDEC 行，而是 `12` 条可逐行检查的
单余类 PDEC/Fourier 行。端点已由下层标签杀死的分支可回到下层标签账本；真正剩余的窄口是
`404` 个 unit endpoint 相位：它们需要 endpoint-PDEC 的 `U_CRT<L_PDEC`，或需要
ColumnCRT 的 `Pi,lambda,L_D` 位移阈值证书。

进一步新增

```text
experiments/prime_matrix_rpz_unit_endpoint_columncrt_gate.py；
docs/monograph/prime-matrix-rpz-unit-endpoint-columncrt-gate.json；
docs/monograph/prime-matrix-rpz-unit-endpoint-columncrt-gate.md。
```

该门控证书证明 unit endpoint 的下层列不是自由变量。若 `a≡rho mod r`，则

```text
c = ap mod r = p*rho mod r = r+g-delta；
H_endpoint ≡ -c*r^{-1} mod p。
```

对每个显式同列素数见证 `pi=h*r+c`，位移 `d=h-H_endpoint mod p` 与 `a` 无关且非零。
当前账本 `12/12` 门控行通过，覆盖全部 `404` 个 unit endpoint 相位。因此持久 unit seam
已经被路由到固定非零 `ColumnCRTDefect(p,d)` 候选；剩余不再是构造位移入口，而是排除
该 `ColumnCRT` 阈值或证明正式反例族避开这些门控行。

再新增

```text
experiments/prime_matrix_rpz_columncrt_threshold_obstruction.py；
docs/monograph/prime-matrix-rpz-columncrt-threshold-obstruction.json；
docs/monograph/prime-matrix-rpz-columncrt-threshold-obstruction.md。
```

该审计说明固定非零位移入口仍不是排斥。对每条 unit gate，全部 unit residues 已在同一
`(label=p, displacement=d)` 类中，因此

```text
R_{p,d} >= prod_{ell<r}(ell-1)。
```

当前最大内禀负载为 `48`；测试 `L_D=2` 时有 `10` 条门控行、`400` 个相位超过阈值。
这只说明它们进入 `ColumnCRTDefect`，不是被排除。故单靠阈值调参不能闭合 RPZ；
下一步必须证明正式反例族避开 unit gate、走 endpoint-PDEC，或给出独立的
`ColumnCRTDefect` 排斥定理。

三路线并进审计

```text
experiments/prime_matrix_rpz_formal_phase_automaton.py；
docs/monograph/prime-matrix-rpz-formal-phase-automaton.json；
docs/monograph/prime-matrix-rpz-formal-phase-automaton.md；
experiments/prime_matrix_rpz_three_route_closure_audit.py；
docs/monograph/prime-matrix-rpz-three-route-closure-audit.json；
docs/monograph/prime-matrix-rpz-three-route-closure-audit.md
```

先由相位自动机定义接受集 `A_p`：起始相位属于 `A_p` 当且仅当 canonical 下降逐步满足
`delta<=p-r` 并到达 `p=2`。当前 BCB-Core 的 `6` 个起始行全部属于 `A_p`。随后三路线审计
给出当前排序：`A_formal_family_avoidance` 第一，`B_endpoint_PDEC` 第二，
`C_columnCRT_defect_exclusion` 第三。理由是当前有限下降账本 `20` 个实际转换节点全部避开
`grid_fail`，而 PDEC 仍缺 `U_CRT`，ColumnCRT 则已被证明不能靠阈值调参闭合。

## 5. 双轨合成

当前 RPZ 链条可写成：

```text
RPZ absorption
=> TailAnchor/ColumnCRT/ColumnRadius/PDEC/SAE named exits
   or BCB lower h-zero-row
=> recursive lower descent
=> p=2 contradiction
   or descent endpoint/grid obstruction
=> SAE/PDEC/ColumnCRT named exits。
```

因此下一硬点不再是“找新出口”，而是两个明确义务：

1. 证明正式反例平台满足下层下降网格条件直到 `p=2`，或每个阻断都进入端点相位账本；
2. 对所有进入账本的 `SAE/PDEC/ColumnCRT` 分支提交证书。

## 6. 审稿边界

本文完成：

```text
Track A 的证书接口表；
Track B 的下层零行下降引理；
样本级下降到 p=2 的可复现审计；
下降阻断相位有限账本；
RPZ-SAE/PDEC/ColumnCRT 证书材料化接口；
RPZ 出口证书骨架包；
当前 endpoint SAE 有限证书；
当前 lower_descent_grid_fail 避开证书。
正式下降路径相位不等式定理。
首阻断 grid_fail 二分定理。
first-grid-fail seam 标准形证书。
first-grid-fail seam 的单余类 PDEC/Fourier 支持包与端点分裂账本。
unit endpoint seam 的固定非零 ColumnCRT 位移门控证书。
ColumnCRT 阈值调参不可闭合障碍证书。
三路线闭合审计与优先级排序。
formal-family 下降相位自动机证书。
formal-family rejected set 全量 seam 吸收证书。
seam/PDEC/ColumnCRT 出口压力账本。
accepted-set 符号阶梯证书。
BCB 起始数字账本。
BCB accepted lower-row 选择器账本。
```

再新增

```text
experiments/prime_matrix_rpz_rejected_phase_absorption.py；
docs/monograph/prime-matrix-rpz-rejected-phase-absorption.json；
docs/monograph/prime-matrix-rpz-rejected-phase-absorption.md。
experiments/prime_matrix_rpz_seam_exit_pressure_ledger.py；
docs/monograph/prime-matrix-rpz-seam-exit-pressure-ledger.json；
docs/monograph/prime-matrix-rpz-seam-exit-pressure-ledger.md。
experiments/prime_matrix_rpz_symbolic_ladder_certificate.py；
docs/monograph/prime-matrix-rpz-symbolic-ladder-certificate.json；
docs/monograph/prime-matrix-rpz-symbolic-ladder-certificate.md。
experiments/prime_matrix_rpz_bcb_start_digit_ledger.py；
docs/monograph/prime-matrix-rpz-bcb-start-digit-ledger.json；
docs/monograph/prime-matrix-rpz-bcb-start-digit-ledger.md。
experiments/prime_matrix_rpz_bcb_accepted_row_selector.py；
docs/monograph/prime-matrix-rpz-bcb-accepted-row-selector.json；
docs/monograph/prime-matrix-rpz-bcb-accepted-row-selector.md。
```

该证书把自动机拒绝集逐相位追踪到首个 `grid_fail` seam。当前范围内：

```text
rejected phases = 27924；
distinct first-fail seams = 12；
materialized seam rows = 12；
uncovered rejected examples = 0。
```

所以路线 A 已变成严格二分：`A_p` 内部相位下降到 `p=2`；`A_p` 外部相位全部回到已物化
seam/PDEC/ColumnCRT 出口。它仍不排除这些出口，但关闭了“rejected set 是否还有未命名逃逸”的缺口。

出口压力账本进一步显示：

```text
seam rows = 12；
total seam support = 1752；
killed endpoint phases = 1348；
unit endpoint phases = 404；
ColumnCRT displacement classes = 10；
max aggregated displacement load = 96。
```

因此剩余出口不再是相位搜索，而是有限窄接口：`12` 条 seam、`12` 条单余类 PDEC 支持、
`10` 个固定非零 ColumnCRT 位移类。

accepted-set 符号阶梯证书把路线 A 的正面目标写成：

```text
for every adjacent p->r, g=p-r:
  delta_p(a)=-(a-1)g mod r <= g。
```

若该不等式首次失败，即进入已材料化 first-grid-fail seam。证书在 `P(19)=9699690` 内逐相位
枚举核验计数公式无不一致，并把符号阶梯记录到 `p=97`。因此 Track B 的下一步不是再扩展
有限相位表，而是证明 formal-family 起始行构造本身强制这些 `delta` 数字落入允许盒。

BCB 起始数字账本显示当前样本的 `20` 个 digit 节点全部安全，但 `10` 个节点位于
`margin=0` 边界。因此不能期待一个统一正余量；路线 A 必须走精确同余证明。

BCB accepted lower-row 选择器账本把正向目标弱化为：

```text
C_h(J)∩A_h != empty。
```

当前 `5/5` 个 BCB-Core 样本都有 selector，`6/6` 个完整下层候选行都 accepted。因此路线 A
的最小闭合目标不必证明每个候选行安全，只需证明正式核心区间中至少存在一个 accepted 候选行。

本文没有完成：

```text
全局下降网格条件；
first-grid-fail seam 标准形的 PDEC/ColumnCRT 证书排斥；
最终 Prime Matrix 行命题无条件闭合。
```

下一步最小硬点更新为：

```text
formal-family 避开 12 条 seam；
或 12 条 endpoint-PDEC 上界 U_CRT<L_PDEC；
或 10 个固定非零 ColumnCRTDefect 排斥证书。
其中 formal-family 避开已等价压缩为逐层 delta 数字约束。
当前样本还显示该数字约束是贴边成立，不能用粗余量替代。
更弱的 selector 存在定理 `C_h(J)∩A_h != empty` 仍未全局证明。
```
