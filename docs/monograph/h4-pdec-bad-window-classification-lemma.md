# H4-PDEC 坏窗分类引理

**状态：** `typed_bad_window_classification_proved_exit_exclusion_open`

本文承接 `h4-pdec-lhb-attachment-lemma.md`。目标是把全局 PDEC 接入义务再压缩一层：
正式反例链抽取出的坏窗要么是 LHB 型坏窗，可使用 `Z_LHB` 与 `M(t)`；要么在第一个
失败条件处进入已有命名出口。本文不排除这些出口；它只证明分类是穷尽且可审查的。

## 1. 已有输入

本文使用以下已登记输入。

| 输入 | 文件 | 用途 |
|---|---|---|
| `UPS-1` | `prime-matrix-bpn-unified-pdec-sae-dichotomy.md` | 任意非空命名低模坏窗集二分为 `PDEC` 或 `SAE` |
| `H4-PDEC-S5` | `h4-pdec-constraint-source-lemmas.md` | 违反即出口的条件路由行合法 |
| `H4-PDEC-COL3` | `h4-pdec-column-cap-source-lemma.md` | 列冲突违反进入 `ColumnRadius/ColumnCRT/TailAnchor` |
| `Tail-anchor dichotomy` | `prime-matrix-bpn-tailanchor-persistence-dichotomy.md` | 尾锚集中进入 `SAE-anchor` 或 persistent tail-anchor defect |
| `Rankin access rule` | `prime-matrix-bpn-final-residual-hard-attack.md` | Rankin 失败若有 low-mod spike 则进入 `PDEC/SAE`，否则保留为常数账本缺口 |
| `H4-LHB-Attach` | `h4-pdec-lhb-attachment-lemma.md` | LHB 型坏窗满足 `S subset Z_LHB(p,Q)` |

这些输入均是路由或接入定理，不是最终排斥定理。

## 2. LHB 型判定合同

对 persistent 分支中的坏窗集合 `S`，每个坏窗 `x` 必须按以下顺序检查。

```text
C0: 同一低模测试函数与同一 phase map tau；
C1: 同一素数 p、同一低模 Q，并且窗口是一整行非平凡列窗口；
C2: 低素数 L={ell<p: ell|Q} 剥离后，剩余列正是 H_Q(tau(x))；
C3: 每个低洞 c in H_Q(tau(x)) 都由某个高根基素数 ell in R={ell<p:ell∤Q} 覆盖；
C4: 坏窗集合不混合不同的 (p,Q,tau) 口径。
```

满足 `C1--C3` 的坏窗称为 `LHB-typed`。`C0` 与 `C4` 是证书一致性条件；失败时不能
继续使用同一个 `g(t)`。

## 3. 失败出口表

| 首个失败条件 | 失败含义 | 强制路由 |
|---|---|---|
| `C0` | 低模测试函数或 `tau` 不同一 | 拆成同一口径子证书；若不可拆则该行拒绝进入 `PDEC-Cert` |
| `C1` | 不是同一 `p,Q` 下的一整行非平凡列窗口 | `SAE` 或重新抽取正式 PDEC 块 |
| `C2` | 低骨架与 `H_Q(t)` 不一致 | `ColumnCRTDefect` 或 `ColumnRadiusDefect` |
| `C3` | 某低洞不能由 `R` 中高根基素数覆盖 | `TailAnchorDefect`、`Rankin low-mod spike` 或 `SAE-survivor` |
| `C4` | 集合 `S` 混合多个口径 | 分块后分别提交证书；不能作为单个 `PDEC-Dual-Cert` 行 |

该表是分类表，不是出口排斥表。若出口尚未排除，只能作为分支条件使用。

## 4. 分类定理

**Theorem H4-PDEC-BWC（坏窗分类）。**
设 `D` 是一个已经由反例链抽取出的命名低模缺陷，并给出窗口索引域 `X`、低模周期
`Q`、相位映射 `tau` 与坏窗集合

\[
S=\{x\in X:\Re F(\tau(x))\ge \kappa\}.
\]

若 `S` 非空，则恰有以下三类之一：

1. `SAE`：`0<|S|<\beta |X|`；
2. `LHB-PDEC`：`|S|\ge\beta |X|`，且 `S` 可分解为同一 `(p,Q,tau)` 下的 LHB 型子族；
3. `Routed-PDEC`：`|S|\ge\beta |X|`，但某个首个失败条件 `C0--C4` 触发上表中的命名出口或拆分义务。

特别地，在排除了 `SAE/ColumnCRT/ColumnRadius/TailAnchor/Rankin/口径混合` 出口的剩余
分支中，所有 persistent 坏窗都是 LHB 型，因而满足

\[
S\subset Z_{\rm LHB}(p,Q).
\]

**证明。**
由 `UPS-1`，非空 `S` 首先二分为 sparse 与 persistent。Sparse 分支即第 1 类 `SAE`。
在 persistent 分支中，按 `C0,C1,C2,C3,C4` 顺序检查。若全部通过，则每个同口径子族
满足 `H4-LHB-Attach` 的三个 LHB 型条件，因此是第 2 类。若某项首次失败，则根据第 3
节失败出口表进入对应命名出口或拆分义务，得到第 3 类。三类由构造穷尽，且在排除所有
第 1、3 类出口后的剩余分支中只剩第 2 类，故 `S subset Z_LHB(p,Q)`。证毕。

## 5. 接入 `M(t)` 容量行

在第 2 类 `LHB-PDEC` 中，可直接引用：

```text
h4-pdec-lhb-attachment-lemma.md；
h4-pdec-lhb-multiplicity-cap-certificate.json。
```

得到

\[
g(t)\le M(t),\qquad
\sum_{t\in C_{\rm WHOLEDEF}}g(t)=0,\qquad
\sum_{t\in C_{\rm BRIDGED}}g(t)=0
\]

对 `Q=2310`、`P=13,17,19,23,29,31,37,43,47` 的有限 LHB 型分支成立。

## 6. 审稿边界

已经闭合：

```text
非空命名低模坏窗 => SAE 或 persistent；
persistent => LHB 型接入 或 命名出口/拆分义务；
排除非 LHB 出口后的剩余分支可使用 LHB bound=0 容量行。
```

仍未闭合：

```text
SAE 出口排斥；
ColumnCRT/ColumnRadius/TailAnchor/Rankin 出口排斥或完整吸收；
混合口径拆分后的所有子证书；
Q=2310 有限 P 列表之外的符号化或分段扩展；
最终 PDEC 对偶主控 U_CRT<L_PDEC。
```

因此下一步最小硬点不再是“LHB 型能否接入”，而是：

\[
\boxed{\text{逐个排除或证书化非 LHB 型出口。}}
\]
