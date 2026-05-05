# AlphaTail `C13` 目标窗口族合同审计

**状态：** `explicit_selected_contract_closed_target_generation_open`

本文把 `C13` 高 `P` 主链的最后全局化缺口单独抽出：当前脚本能验证给定
`selected` 窗口清单上的合同闭合，但仓库中尚未形式化“完整高 `P` 目标窗口族如何由
`P` 生成 `B,r,m`”的规则。因此本层闭合的是显式样本合同，不是行命题全局闭合。

## 1. 合同对象

对每个高 `P` 窗口 `(p,B,r)`，令低大素块最小素数为 `L`，并取
`m in {4,5}`。目标族生成器必须至少给出以下可审查条件：

```text
TFC-A: B 是 dyadic block，且在当前候选样式中 B=2^ceil(log2(p+1)), p<B<2p；
TFC-B: 6 divides |r|；
TFC-C: B<2L、(m-1)|r|<L、2B+(m-1)|r|<5L；
TFC-D: Gate 总池闭合，或 Formal+MidVoid+EdgeStructural 逐窗口闭合。
```

其中 `TFC-C` 同时接回 `lift>=2` 结构空性与 `lift=1` 中间层结构空性，
`TFC-D` 接回 `HighP-PLT` 低筛闭合桥。
若完整目标族生成器只输出满足 `TFC-A/B/C/D` 的窗口，则 `C13` 高 `P` 链条可在该
目标族上闭合。

## 2. 比例化结构充分条件

`TFC-C` 仍含低素块最小素数 `L`。但在当前 `alpha=0.9` 的低大素块定义下，
`L` 是第一个大于 `floor(alpha p)` 的素数，故

\[
L>\alpha p.
\tag{TFC-1}
\]

因此有一个不再依赖低素枚举的充分条件：

```text
TFC-R1: B < 2 alpha p；
TFC-R2: (m_max-1)|r| < alpha p；
TFC-R3: 6 divides |r|。
```

由 `TFC-R1` 与 `(TFC-1)` 得 `B<2L`；由 `TFC-R2` 与 `(TFC-1)` 得
`(m-1)|r|<L`。并且

\[
2B+(m-1)|r|<4\alpha p+\alpha p=5\alpha p<5L.
\tag{TFC-2}
\]

所以 `TFC-R1/R2/R3` 推出 `TFC-B/C`。

在本文默认 `alpha=0.9,m_max=5` 下，该比例条件为：

```text
B/p < 1.8；
|r|/p < 0.225；
6 divides |r|。
```

这给目标窗口族生成器一个更硬的审稿接口：无需逐窗口先算 `L`，只要生成器保证上述
两个比例不等式，`lift>=2` 结构空性即自动接回。

等价地，对固定 dyadic block `B` 和默认 `alpha=0.9`，生成器必须输出

```text
p > B/1.8；
|r| < 0.225 p。
```

这两个量可作为窗口生成阶段的余量账本：`p-B/1.8` 控制 `B<2L`，而
`0.225p-|r|` 控制所有 `m<=5` 的 `(m-1)|r|<L`。

## 3. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_target_family_contract.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_target_family_contract.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --format table
```

## 4. 当前样本结果

高 `P` 样本只包含 `p=5003,10007`，输出为：

```text
highP_windows=2；
syntax=True；
ratio_structural=True；
structural=True；
total_gate=True；
local_formal=True；
row_formal=True；
explicit_contract=True；
target_rule_closed=False。
```

付款余量：

```text
gate_total_margin=505.963717；
formal_total_margin=2010.963717；
min_gate_window_margin=-485.272633；
min_formal_window_margin=411.727367。
```

逐窗口：

```text
p=5003:
  B=8192=2^ceil(log2(p+1))；
  p<B<2p；
  B/p=1.637418<1.8；
  |r|/p=0.007196<0.225；
  p-B/1.8=451.888889；
  0.225p-|r|=1089.675000；
  mid_compression_margin=6007；
  6 divides |r|；
  min_block_margin=822；
  min_n_margin=4363；
  gate_pass=False；
  formal_pass=True。

p=10007:
  B=16384=2^ceil(log2(p+1))；
  p<B<2p；
  B/p=1.637254<1.8；
  |r|/p=0.089937<0.225；
  p-B/1.8=904.777778；
  0.225p-|r|=1351.575000；
  mid_compression_margin=8667；
  6 divides |r|；
  min_block_margin=1630；
  min_n_margin=5407；
  gate_pass=True；
  formal_pass=True。
```

因此当前显式高 `P` 压力样本满足：

```text
lift>=2 structural void；
Gate total pool closure；
Formal local closure。
```

这也暴露下一窄口：`Gate` 不能逐窗口使用，因为 `p=5003` 的局部余量为负；
若目标族不能证明总池付款合法，则必须使用 `Formal+MidVoid` 的逐窗口付款路线。

新增 `prime-matrix-eda-alpha-tail-tailpair-c13-formal-local-payment-contract.md` 后，
`Formal+MidVoid` 进一步拆成：

```text
FLP-A: lift>=2 void；
FLP-B: MidVoid；
FLP-C: EdgeExact U_edge<=S。
```

当前样本 `mid=0, ge2=0, edge=527, slack=2537.963717`，最紧局部余量为
`411.727367`。进一步由 `prime-matrix-eda-alpha-tail-tailpair-c13-edge-gate-payment-contract.md`，
`EdgeExact` 可替换为更粗的 `K*G_edge<=S`：当前 `gate_envelope=848`，
`min_gate_margin=106.727367`。因此下一硬点已经压成完整目标族上的
`MidVoid + EdgeGatePayment`。新增
`prime-matrix-eda-alpha-tail-tailpair-c13-midlayer-structural-void-contract.md` 后，
`MidVoid` 又进一步压成 `2B+(m-1)|r|<5L` 与 `6|r,L>3` 的结构同余判据。
当前样本 `structural_mid_void=True`，最小压缩余量为 `6007`。
新增 `prime-matrix-eda-alpha-tail-tailpair-c13-edge-structural-ceiling-contract.md` 后，
`EdgeGatePayment` 又被压成固定门数公式：当前 `m in {4,5}` 时
`G_edge<=72`，默认 `K=8` 只需 `S>=576`。样本最小结构付款余量仍为
`106.727367`。
新增 `prime-matrix-eda-alpha-tail-tailpair-c13-slack-floor-contract.md` 后，
`S>=576` 被拆成 `ResonanceFloor + geometric_buffer`；当前样本最紧窗口仅用
`ResonanceFloor` 仍有 `101.727367` 正余量。
新增 `prime-matrix-eda-alpha-tail-tailpair-c13-low-deletion-allowance-contract.md` 后，
该条件等价为 `D_low<=G-B2-Cap-K E_M`。样本总删除量 `50`，允许删除量
`1385.963717`；最紧窗口删除 `5`，允许删除 `106.727367`。
新增 `prime-matrix-eda-alpha-tail-tailpair-c13-ap-singleton-reduction-contract.md` 后，
样本满足 `D_low=active_AP_classes` 且每个活跃 AP 类只含一个尾素对。
新增 `prime-matrix-eda-alpha-tail-tailpair-c13-ap-singleton-structural-contract.md`
后，单点化由 `q<2ell` 推出；样本所有活跃类均满足 `u in {2,3}` 与
`q=ell+residue`。

## 5. 精确剩余

当前真正剩余不是样本内部预算，而是：

```text
TargetFamilyGenerator:
  给出完整高 P 目标窗口族 W(P)；
  证明 W(P) 不遗漏任何 C13 目标窗口；
  证明每个输出窗口满足 TFC-A 与 TFC-R1/R2/R3；
  在生成器账本中显式给出 p-B/1.8 与 0.225p-|r| 的正余量；
  证明 Gate 总池付款合法，或证明每个输出窗口满足 Formal+MidVoid+EdgeStructural+LowDeletionAllowance+APSingleton 局部付款；
  若有例外，则列入有限证书或 PDEC/SAE 出口。
```

在该生成器未形式化前，本文只能支持：

```text
当前 explicit-selected 样本合同闭合；
完整行命题全局闭合仍未完成。
```

新增 `HotShiftTargetGenerator` 后，当前高 `P` selected 样本已可由
`B=2^ceil(log2(p+1))` 与固定符号 squarefree 光滑集合的热门非零位移生成：

```text
5003 -> 8192, r=-36；
10007 -> 16384, r=-900。
```

该生成器目前只闭合“样本来源”，尚未证明它覆盖完整行命题目标族。
