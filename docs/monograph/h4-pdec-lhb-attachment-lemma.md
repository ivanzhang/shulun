# H4-PDEC LHB 接入引理

**状态：** `lhb_typed_attachment_proved_global_classification_open`

本文闭合 `h4-pdec-lhb-multiplicity-cap-certificate.json` 的使用前提中最窄的一段：
若当前 PDEC 坏窗已经被证明属于 LHB 型全覆盖行分支，则它必然落入
`Z_LHB(p,Q)`，从而可以使用已经物化的 `M(t)` 容量行。本文不证明任意 PDEC 坏窗都
属于 LHB 型分支；非 LHB 型对象仍必须路由到命名出口。

## 1. 坐标与低洞集

固定素数 `p` 与低模

\[
Q\mid \prod_{\ell<p}\ell.
\]

设

\[
L=\{\ell<p:\ell\mid Q\},\qquad
R=\{\ell<p:\ell\nmid Q\},\qquad
M_R=\prod_{\ell\in R}\ell.
\]

低相位 `t mod Q` 与高层变量 `y mod M_R` 给出行

\[
r=t+Qy.
\]

列 `1<=c<p` 的格点值是

\[
n_{r,c}=(r-1)p+c.
\]

低骨架洞集定义为

\[
H_Q(t)=\{1\le c<p:\ n_{t,c}\not\equiv0\pmod\ell
\text{ for every }\ell\in L\}.
\]

因为 `Q` 被所有 `ell in L` 整除，`n_{t+Qy,c}\equiv n_{t,c}\pmod\ell`，所以
`H_Q(t)` 不依赖 `y`。

## 2. LHB 允许全集

定义

\[
Z_{\rm LHB}(p,Q)=
\left\{(t,y):\forall c\in H_Q(t),\ \exists \ell\in R
\text{ with }(t+Qy-1)p+c\equiv0\pmod\ell
\right\}.
\]

相位映射为

\[
\tau(t,y)=t.
\]

于是

\[
M(t)=\#\{y\bmod M_R:(t,y)\in Z_{\rm LHB}(p,Q)\}
\]

正是 `prime_matrix_bpn_low_hole_bucket_capacity.py` 中的 `completion_count(t)`。

## 3. 接入定理

**Theorem H4-LHB-Attach（LHB 型坏窗接入）。**
设 `S` 是当前 PDEC 分支抽取出的坏窗集合。若每个 `x in S` 都带有坐标

\[
x=(t_x,y_x)
\]

并满足以下 LHB 型条件：

1. `x` 的窗口是同一个 `p,Q` 下的一整行非平凡列窗口；
2. 低素数 `L` 覆盖的列已经按 `H_Q(t_x)` 剥离；
3. 对每个低洞 `c in H_Q(t_x)`，该列由某个高根基素数 `ell in R` 覆盖，即
   \[
   (t_x+Qy_x-1)p+c\equiv0\pmod\ell;
   \]

则

\[
S\subset Z_{\rm LHB}(p,Q).
\]

因此对 `g(t)=#{x in S:tau(x)=t}` 有

\[
g(t)\le M(t),
\]

且对任意相位块 `C` 有

\[
\sum_{t\in C}g(t)\le \sum_{t\in C}M(t).
\]

**证明。**
取任意 `x=(t_x,y_x) in S`。由条件 1 与条件 2，低素数集合 `L` 已经覆盖
`H_Q(t_x)` 之外的列；剩余待覆盖列正是 `H_Q(t_x)`。由条件 3，对每个
`c in H_Q(t_x)` 都存在 `ell in R` 使
`(t_x+Qy_x-1)p+c≡0 mod ell`。这正是 `Z_LHB(p,Q)` 的定义。因此
`x in Z_LHB(p,Q)`。任意性给出 `S subset Z_LHB(p,Q)`。随后逐相位容量继承由
`H4-PDEC-S2` 或 `H4-LHB-M1` 直接推出。证毕。

## 4. 与高层 CRT 补洞公式一致

对 `ell in R` 与 `c in H_Q(t)`，由于 `ell` 不整除 `Qp`，有

\[
(t+Qy-1)p+c\equiv0\pmod\ell
\]

等价于

\[
y\equiv (1-cp^{-1}-t)Q^{-1}\pmod\ell.
\]

所以 `Z_LHB(p,Q)` 与 `prime-matrix-bpn-low-hole-bucket-capacity-theorem.md`
的 `C_P(t;Q)` 完全同一对象。`h4-pdec-lhb-multiplicity-cap-certificate.json`
物化的 `M(t)` 正是该集合在 `tau` 下的相位投影计数。

## 5. 非 LHB 型失败路由

若当前 PDEC 坏窗不能满足 Theorem H4-LHB-Attach 的三个条件，不能使用 LHB 容量行。
它必须按失败位置进入下表的命名出口或新证书行。

| 失败点 | 含义 | 允许回流 |
|---|---|---|
| 坐标失败 | 不是同一 `p,Q` 下的一整行非平凡列窗口 | `SAE` 或重新抽取 PDEC 块 |
| 低骨架失败 | 低素数剥离后剩余列不是 `H_Q(t)` | `ColumnCRTDefect` / `ColumnRadiusDefect` |
| 高标签失败 | 某个低洞不是由 `R={ell<p:ell∤Q}` 中的高根基素数覆盖 | `TailAnchorDefect` / `Rankin low-mod spike` |
| 多窗口混合 | 一个 `S` 混合了不同 `p,Q,tau` 口径 | 拆分成同口径子证书，或拒绝进入该行 |

这些回流不是证明出口已经矛盾；它只说明 LHB 容量行的使用边界是可审查的。

## 6. 当前结论

已经闭合：

```text
LHB 型 PDEC 坏窗 => S subset Z_LHB(p,Q)；
Z_LHB 的 M(t) 已由 Q=2310 有限证书物化；
WHOLEDEF/BRIDGED 在该分支中给出 bound=0 容量行。
```

仍未闭合：

```text
任意全局 PDEC 坏窗都属于 LHB 型分支；
或非 LHB 型坏窗全部被 ColumnCRT/ColumnRadius/TailAnchor/SAE/Rankin 出口排除；
或把该接入推广到 Q=2310 有限 P 列表之外的符号化范围。
```

因此下一步最小硬点从 `S subset Z_LHB` 进一步压缩为：

\[
\boxed{\text{PDEC 坏窗分类：LHB 型接入，非 LHB 型命名出口。}}
\]

补充文件 `h4-pdec-bad-window-classification-lemma.md` 已完成该分类的第一版合同：
非空命名低模坏窗先由 `UPS-1` 二分为 `SAE` 或 persistent；persistent 分支再按同一
`(p,Q,tau)`、低骨架、高标签和口径混合四类失败路由。该分类仍不排除出口，但把
LHB 容量行的全局使用边界精确化为“排除非 LHB 型出口后的剩余分支”。
