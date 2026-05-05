# AlphaTail `C13` 边缘门结构上界合同

**状态：** `edge_structural_ceiling_sample_closed_global_open`

本文把 `EdgeGatePayment` 的剩余门数 `G_edge` 进一步压成只依赖 `m` 的有限公式。
这比逐窗口枚举非空边缘门更适合目标族全局化。

## 1. 结构门型压缩

边缘层只有两类：

```text
head: h=0, q=ell+s；
tail: h=u, q=2ell-s。
```

设低大素块为 `[L,U]`，尾素块首素为 `T`。在目标族条件

```text
B<2L；
U<B+1；
T>U；
6 divides r
```

下，非空边缘门只能来自：

```text
u=1 的 tail 门；
u=2 或 u=3 的 head 门。
```

证明要点如下。

1. 任意边缘候选满足 `q>=L` 且 `q<=2B/u`，所以 `u>=4` 与 `B<2L` 矛盾。
2. `u=1` 的 head 门若非空，则由窗口左端给出 `B+1<=U`，与 `U<B+1` 矛盾。
3. `u=2,3` 的 tail 门若非空，则 `2uL<=2B-jr_abs<=2B`，从而 `B>=2L`，矛盾。
4. `u=2,3` 的 head 门中 `s=0` 会给 `q=ell<=U<T`，不能进入尾素块；因此只剩 `s>0`。

## 2. 有限计数公式

对固定 `m`，`u=1` tail 门数至多为

\[
T_m=\sum_{j_1=1}^{m-1}j_1^2
=\frac{m(m-1)(2m-1)}6.
\tag{ESC-1}
\]

`u=2,3` head 门中必须有 `j_2<j_1<j`，每个 `u` 至多贡献

\[
H_m=\binom m3.
\tag{ESC-2}
\]

故

\[
G_{\rm edge}(m)\le T_m+2H_m.
\tag{ESC-3}
\]

在当前 `m in {4,5}` 下：

```text
m=4: 14+8=22；
m=5: 30+20=50；
window ceiling = 72。
```

所以默认 `K=8` 时，逐窗口只需

\[
S\ge 8\cdot72=576
\tag{ESC-4}
\]

即可得到结构化 `EdgeGatePayment`。

## 3. 审计脚本

脚本：

```text
experiments/prime_matrix_alpha_tail_tailpair_c13_edge_structural_ceiling_contract.py
```

样本命令：

```text
python3 experiments/prime_matrix_alpha_tail_tailpair_c13_edge_structural_ceiling_contract.py \
  --selected '997:4096:-36,5003:8192:-36,10007:16384:-900' \
  --finite-p-cut 1000 --eta 0.04 --format table
```

输出摘要：

```text
guard=True；
actual_under_ceiling=True；
structural_pay=True；
total_actual_gates=106；
total_structural_gate_ceiling=144；
total_structural_gate_envelope=1152；
total_structural_margin=1385.963717；
min_structural_margin=106.727367。
```

逐窗口：

```text
p=5003:
  actual_gates=72；
  structural_ceiling=72；
  structural_envelope=576；
  margin=106.727367。

p=10007:
  actual_gates=34；
  structural_ceiling=72；
  structural_envelope=576；
  margin=1279.236350。
```

新增 `prime-matrix-eda-alpha-tail-tailpair-c13-slack-floor-contract.md` 后，
该余量被拆成：

```text
S = (M2 - B2_model - Cap_even) + (G_geom - M2)。
```

当前样本甚至满足更强的 `ResonanceFloor`：最紧窗口仅用第一项仍有
`101.727367` 正余量。

## 4. 审稿边界

该合同已把边缘门数从窗口枚举压成固定公式，但完整行命题仍需目标族生成器证明：

```text
所有 C13 高 P 目标窗口满足 B<2L、U<B+1、T>U、6|r；
每个目标窗口的低筛保存余量 S 至少为 K*sum_m(T_m+2H_m)；
若 S<该结构 envelope，则进入有限证书、formal 去重或 PDEC/SAE 出口。
```
