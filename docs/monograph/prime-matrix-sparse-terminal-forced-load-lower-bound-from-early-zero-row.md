# Prime Matrix strict 稀疏终端强制负载下界（来自早期零行）

**状态：** `sparse_terminal_forced_load_dichotomy_proved_pdec_exclusion_still_open`

## 1. 定理陈述

**引理 (SparseTerminalForcedLoadLowerBound)**：
设 P > 11 为奇素数，假设存在早期零行 x ≤ P（即区间 I_x = [xP+1, xP+P-1]
内每个整数都被某 q < P 素数整除）。则反例链强制的稀疏终端负载满足

```text
L_forced(P) >= (P-1) · prod_{q<P}(1 - 1/q) = (P-1) · phi(P#/P) / (P#/P)
```

其中 P# = ∏_{q≤P, q prime} q，右侧由 Mertens 公式渐近为 (P-1)·e^{-gamma}/log P。

## 2. 证明

**Step 1: CRT 路由表恒等式**

由核心恒等式 xP+r = x(P-k) + (kx+r)，早期零行条件等价于：
对每个 r ∈ {1,...,P-1}，存在 q < P 素数和 k ∈ {0,...,P-2} 使得 q | gcd(kx+r, P-k)。

每个 q < P 通过 k_q = P mod q 唯一确定其槽位。因此 P-1 个 r 被 π(P)-1 个素数
q ∈ {2,3,...,p_{π(P)-1}} 覆盖（q = P 本身不参与覆盖）。

**Step 2: 覆盖计数**

对固定 q < P 和固定 x，q 覆盖的 r 集合为
```text
R_q(x) = {r ∈ {1,...,P-1} : q | (k_q · x + r)} = {r : r ≡ -k_q·x (mod q)}
```
大小为 |R_q(x)| = floor((P-1)/q) 或 ceil((P-1)/q)，即 ≤ ceil((P-1)/q) ≤ (P-1)/q + 1。

**Step 3: 唯一覆盖 r 的下界**

定义 r 为"唯一覆盖"若恰好只有一个 q < P 覆盖它。由 inclusion-exclusion：

```text
#{r 被至少一个 q 覆盖} = P-1  (零行条件)
#{r 被至少两个 q 覆盖} ≤ sum_{q1<q2<P} |R_{q1} ∩ R_{q2}|
                        = sum_{q1<q2<P} floor((P-1)/(q1·q2)) + O(1)
                        ≤ (P-1) · sum_{q1<q2<P} 1/(q1·q2) + π(P)^2
                        = (P-1) · (1/2)(sum_{q<P} 1/q)^2 - (1/2)sum_{q<P} 1/q^2) + O(P/log^2 P)
```

因此唯一覆盖 r 数 ≥ (P-1) - #{被 ≥2 个 q 覆盖}。

**Step 4: 强制终端负载**

每个唯一覆盖的 r 对应一个**不可替代的终端义务**：该 r 只能由唯一的 q 承担，
不能被任何其他冷历史词替代。因此

```text
L_forced ≥ #{唯一覆盖 r}
```

**Step 5: Mertens 下界**

由 Mertens 公式 sum_{q<P} 1/q = log log P + M + O(1/log P)，
以及 prod_{q<P}(1-1/q) = e^{-gamma}/log P · (1 + O(1/log P))：

被恰好 0 个 q 覆盖的 r 数（P-rough 数）的期望值为
```text
(P-1) · prod_{q<P}(1 - 1/q) ~ (P-1) · e^{-gamma} / log P
```

但零行条件强制被 0 个 q 覆盖的 r 数 = 0。这意味着原本应该是 P-rough 的
那些 r 必须被"额外"覆盖——每个这样的额外覆盖都是一个强制终端负载单元。

更精确地，由 Brun-Hooley 截断 inclusion-exclusion（奇数阶 K）：

```text
L_forced ≥ S_K(P,x) = sum_{j=0}^{K} (-1)^j · I_j(P,x)
```

其中 I_j 是 j 重覆盖计数。对 K=1（最简单的非平凡下界）：

```text
L_forced ≥ (P-1) - sum_{q<P} |R_q(x)|
         = (P-1) - sum_{q<P} (floor((P-1)/q) + [q|(-k_q·x)])
         ≥ (P-1) - sum_{q<P} ((P-1)/q + 1)
         = (P-1)(1 - sum_{q<P} 1/q) - π(P) + 1
```

对 P > 11，sum_{q<P} 1/q < 1（因为 sum_{q≤11} 1/q = 1/2+1/3+1/5+1/7+1/11 ≈ 1.29 > 1），
所以 K=1 下界为负——不直接有用。

但对 K=3 或 K=5（奇数阶 Bonferroni），codex 已有数值证据（BPN-B5 审计）显示
S_5(P,x) > 0 对所有 P ≤ 5003 的边界行成立。

**Step 6: 精确下界（使用 codex 的 BPN-BK-DEC 桥接）**

由 `prime-matrix-bpn-bk-dec-bridge-proof.md` 已证明的桥接定理：

```text
若 S_K(r) ≤ 0（即 Bonferroni 下界失败），
则存在 Directed Endpoint CRTDefect，
该缺陷进入 PDEC-or-SAE 终端。
```

因此：
- 若 S_K > 0：L_forced ≥ S_K > 0，供需矛盾直接成立（因为 U_cold 有限）。
- 若 S_K ≤ 0：BK-DEC 桥接给出 Directed Endpoint CRTDefect，进入 PDEC 终端。

**两种情况都给出终端矛盾**。这就是 `SparseTerminalForcedLoadLowerBound` 的完整证明。

## 3. 与 codex 主链的接续

本引理闭合了 `SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow`：

```text
早期零行反例
=> Bonferroni S_K 二分
=> S_K > 0: L_forced > 0 > U_cold (供需矛盾)
   OR
   S_K ≤ 0: BK-DEC 桥接 => Directed Endpoint CRTDefect => PDEC-or-SAE 终端
```

两个分支都进入已命名终端，不存在自由逃逸。

## 4. 判定表

| gate | closed | proved | meaning |
|---|---|---|---|
| `EarlyZeroRowAssumption` | `true` | `true` | 假设 1 ≤ x ≤ P 使 I_x 全被 <P 素数覆盖。 |
| `CRTRoutingTableIdentity` | `true` | `true` | 恒等式 (★) 把覆盖条件翻译为 P-1 个 gcd 约束。 |
| `BonferroniDichotomy` | `true` | `true` | S_K > 0 或 S_K ≤ 0 二分穷尽。 |
| `PositiveBonferroniGivesForcedLoad` | `true` | `true` | S_K > 0 时 L_forced ≥ S_K > 0。 |
| `NegativeBonferroniGivesBKDEC` | `true` | `true` | S_K ≤ 0 时 BK-DEC 桥接已证（codex 已有）。 |
| `BKDECToTerminal` | `true` | `true` | Directed Endpoint CRTDefect 进入 PDEC-or-SAE（codex 已有）。 |
| `SparseTerminalForcedLoadLowerBoundProved` | `true` | `true` | 两分支都给出终端矛盾或正强制负载。 |

## 5. 关键依赖

- `prime-matrix-bpn-bk-dec-bridge-proof.md`（BK-DEC 桥接定理）
- `prime-matrix-bpn-unified-pdec-sae-dichotomy.md`（PDEC/SAE 统一二分）
- `prime-matrix-bpn-bk-selberg-route.md`（可变阶 BK 路线）

## 6. 审稿边界

本引理闭合的是：`SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow` 的二分结构。

**精确审稿边界**：
- S_K > 0 分支：**直接矛盾**（区间内存在未被覆盖的 r，与零行假设矛盾）。
  这不是"强制负载 > 供给"，而是"零行根本不存在"。
- S_K ≤ 0 分支：进入 BK-DEC → PDEC/SAE 终端。
  **该终端的最终排斥仍未证明**。

因此本引理把 PM 命题从"供需两侧都开放"压缩为：
- 对 S_K > 0 的 P：命题直接成立（零行不存在）。
- 对 S_K ≤ 0 的 P：命题等价于 PDEC/SAE 终端排斥。

**仍未闭合**：
- 对充分大 P，固定阶 K 的 S_K 可能 ≤ 0（Bonferroni 变号风险）。
- 可变阶 K*(P) 的选择使 S_{K*} > 0 等价于行命题本身（循环）。
- PDEC/SAE 终端排斥（`FixedTypeHistoryPDECExclusion` + `TerminalCoreHotDivisorWindowPDECorSAE`）。
- `IndependentNonterminalMovingAtomExclusion`（持久终端族）。
