# RPZ 出口证书材料化接口

**状态：** `rpz_certificate_materialization_interface_defined`

本文承接 `prime-matrix-rpz-dual-track-closure-route.md`。双轨路线已经把 RPZ 剩余义务压成：

```text
LowerDescent-Grid persistence
and RPZ-SAE/PDEC/ColumnCRT certificate materialization。
```

本文把第二项证书义务材料化为可填写的审稿接口，同时说明下降阻断相位如何回流到同一接口。

## 1. 下降阻断相位账本

新增审计：

```text
experiments/prime_matrix_rpz_lower_descent_obstruction_ledger.py；
docs/monograph/prime-matrix-rpz-lower-descent-obstruction-ledger.json；
docs/monograph/prime-matrix-rpz-lower-descent-obstruction-ledger.md。
```

对每个相邻素数转换 `p -> r`，行号相位取模

\[
P(r)=\prod_{\ell\le r}\ell.
\]

下降失败只有两类：

1. `grid_fail`：`p` 行不完整包含任何 `r` 对齐行；
2. `puncture_block`：完整 `r` 行全部含端点穿孔 `p\cdot row`。

有限审计中，实际下降转换节点全部为 `success`，实际阻断节点为 `0`。但枚举相位账本给出了
所有可能阻断相位，因此全局阻断可直接进入 `SAE/PDEC/ColumnCRT`。

新增证书骨架：

```text
experiments/prime_matrix_rpz_certificate_skeleton_builder.py；
docs/monograph/prime-matrix-rpz-certificate-skeleton-package.json；
docs/monograph/prime-matrix-rpz-certificate-skeleton-package.md。
```

该骨架把已命名出口转成待填证书行：

```text
Endpoint SAE 候选：2；
Endpoint PDEC/ColumnCRT 行：各 2；
LowerDescent grid_fail PDEC/ColumnCRT 行：各 3；
LowerDescent 可能阻断相位：1752，全部为 grid_fail。
```

这一步只完成证书行抽取，不排除任何出口。

## 2. RPZ-SAE finite package

**输入对象。**

```text
phase_type = endpoint_grid_failure | lower_descent_grid_fail | lower_descent_puncture_block
phase_key  = finite tuple recorded in the corresponding ledger
load       = number of formal bad windows carrying this phase
B_SAE      = sparse escape threshold
```

**验收义务。**

若每个 `phase_key` 的负载 `<=B_SAE`，需要提交：

```text
RPZ-SAE-FIN:
  candidate_windows: explicit finite list or bounded local family；
  local_state: survivor / lift / higher-defect status for each window；
  verdict: each window either contains a survivor or routes to named higher defect。
```

该接口不要求证明全局 Fourier 矛盾；它只处理低负载孤立逃逸。

## 3. RPZ-PDEC endpoint phase row

**输入对象。**

```text
S_tau = {formal bad windows with the same persistent RPZ phase tau}
F_tau = 1_{S_tau} - |S_tau|/Q
```

其中 `tau` 可以来自：

```text
BCB endpoint phase；
LowerDescent grid_fail phase；
LowerDescent puncture_block phase。
```

**验收义务。**

接入 `h4-pdec-certificate-template.md`：

```text
PDEC-Explicit-Cert if S_tau is finite；
PDEC-Dual-Cert if S_tau is an infinite same-phase family。
```

需要填写：

```text
Q, S_tau, F_tau；
Fourier lower bound L_PDEC；
CRT upper bound U_CRT；
verification U_CRT < L_PDEC。
```

该接口只说明如何接入 PDEC；它不宣称 PDEC 已排除。

## 4. RPZ-ColumnCRT endpoint displacement row

当同一持久 RPZ 相位同时携带吸收标签 `ell` 与列见证位移余类 `a` 时，接入
`h4-pdec-column-defect-routing-contract.md`：

```text
ColumnCRTDefect(ell, a, L_D, theta, S, Pi, lambda)。
```

需要填写：

```text
label selector lambda；
same-column prime witness selector Pi；
nonzero displacement residue a mod ell；
load threshold L_D；
finite certificate or source theorem proving load > L_D impossible。
```

若负载超过阈值，则进入 `ColumnCRTDefect`；若未超过阈值，则该相位可回到 PDEC/SAE
账本继续处理。

## 5. 当前审稿边界

本文完成：

```text
下降阻断相位 finite ledger；
RPZ-SAE / RPZ-PDEC / RPZ-ColumnCRT 三类证书材料化接口；
当前 endpoint RPZ-SAE-FIN 有限账本证书；
当前 lower_descent_grid_fail 闭式判据与避开证书；
正式下降路径相位不等式定理；
首阻断 grid_fail 二分定理；
first-grid-fail seam 标准形证书。
first-grid-fail seam 的 PDEC/Fourier 支持包与端点 unit/killed 分裂。
unit endpoint seam 的 ColumnCRT 固定非零位移门控证书。
ColumnCRT 阈值调参不可闭合障碍证书。
```

本文没有完成：

```text
全局 RPZ-SAE-FIN 的窗口列表；
RPZ-PDEC 的 U_CRT<L_PDEC 证书；
RPZ-ColumnCRT 的 L_D 阈值证书；
LowerDescent-Grid persistence 的全局证明。
```

新增 seam 增强包把 `12` 个 first-grid-fail 相位逐行写成：

```text
S_tau={a mod Q: a≡rho mod r}；
F_tau=1_{a≡rho mod r}-1/r；
nonzero Fourier support={Q/r,2Q/r,...,(r-1)Q/r}；
endpoint split = Q-unit endpoint branch + lower-label-killed endpoint branch。
```

完整 `Q` 中共有 `1752` 个 grid_fail 相位，其中端点 `ap` 已被下层小素数杀死的相位为
`1348`，端点是 `Q`-unit、必须继续进入 endpoint-PDEC 或 ColumnCRT 的相位为 `404`。
这一步填实了 PDEC 输入行和端点分裂账本；它仍不提供 `U_CRT` 上界或 ColumnCRT 阈值。

新增 `prime-matrix-rpz-unit-endpoint-columncrt-gate.md` 后，`404` 个 unit endpoint 相位又被压成
`12` 条固定列位移门控行。若下层列为 `c`，则

```text
c = p*rho mod r = r+(p-r)-delta；
H_endpoint ≡ -c*r^{-1} mod p；
d = h_witness-H_endpoint mod p != 0。
```

当前有限门控账本中 `12/12` 行有显式同列素数见证，且 `12/12` 行的位移均为非零 `mod p`
余类。因此持久 unit endpoint seam 不再是未结构化坏窗，而是标准
`ColumnCRTDefect(p,d)` 候选。

新增 `prime-matrix-rpz-columncrt-threshold-obstruction.md` 后，下一层障碍也已明确：
在同一 unit gate 内，所有 unit residues 已经落到同一个 `(label=p, displacement=d mod p)` 类，
所以该类的内禀负载为

```text
R_{p,d} >= prod_{ell<r}(ell-1)。
```

当前账本最大内禀负载为 `48`；若测试阈值 `L_D=2`，则 `10` 条门控行、`400` 个相位只会触发
`ColumnCRTDefect`，不能被排除。若把 `L_D` 提高到内禀负载以上，又失去排斥力。因此
`ColumnCRT` 路线的剩余必须是独立 `ColumnCRTDefect` 排斥定理，不能靠阈值调参完成。

下一步最小硬点：

```text
1. 把正式反例族到 unit endpoint gate rows 的映射写成定理；
2. 提交独立 ColumnCRTDefect(p,d) 排斥定理，不能仅调小 L_D；
3. 或证明正式反例族无法命中 unit endpoint seam；
4. 或改走 endpoint-PDEC 的 U_CRT<L_PDEC 上界。
```
