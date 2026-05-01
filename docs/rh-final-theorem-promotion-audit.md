# RH 主定理升级审查：最终 warning 是否可删除

本文对 `paper/rh-proof/rh-contradiction-field.tex` 中主定理口径与 `Submission warning` 做最终升级审查。结论先行：主定理 `review form` 标签已由 U1/U4 删除，但当前仍不能诚实删除 warning；普通 proof 级审稿标记已经清零，且 `EXT-KL`、`EXT-PC1-LI` 的主稿实际使用形式均已精确适配。

## 1. 已完成的可审稿补正

- `Proof sketch for review` 与 `Review proof` 已从 LaTeX 主稿中全部消除。
- `PC1` 有主稿证明；有限边界零点情形文内闭合，无限边界/上确界情形由 `docs/rh-ext-pc1-li-precision-final.md` 固定为 `EXT-PC1-LI`。
- `PC2` 有主稿 CRT 零频基线证明。
- `EXT-KL` 单变量 NRC 入口已由 `docs/rh-ext-kl-precision-final.md` 固定为素数模非退化 `ax+b/x` 完成和。
- GEE 下界/上界已经同尺度化：下界为 `Δ log^{-C_route}X`，上界通过阈值层级压到 `Δ log^{-B_final}X`，并要求 `B_final>C_route+C_total+10`。

## 2. 仍不能删除 warning 的原因

主定理现在以如下形式成立：由 PC1、C4、C5、C6、C9、GEE upper、PC2、C3、GEE0 以及 restricted external inputs 合成，离线零点无自由逃逸通道。

这还不是“RH 无条件证明”的最终期刊表述，原因是：

1. 主稿已改称 `Consolidated Verification Manuscript`，但其结构仍要求独立逐行核验每个 controlled exit。
2. C4/C5/C6/C9 已在主稿编号化，但 routing、capacity、tail、terminal 结论仍需最终 referee verification。
3. 外部输入虽已精确适配为 restricted packages，但专著页码仍是排版核验义务。
4. 若删除 warning，会把“验证稿”误标为“RH 已无条件证明定稿”，这超过当前文档可审查状态。

## 3. 最小剩余审稿义务

要删除最终 `Submission warning`，至少需要完成以下一张验收表：

| 项 | 需要动作 | 当前状态 |
|---|---|---|
| C4 sparse branch | 将 consolidated proof 展开为逐引理链，或列出精确定理号 | 已完成主稿编号化；见 `docs/rh-c4-sparse-maintext-final.md` |
| C5 DGap branch | 将三接口链与投影/尾项归约逐条编号 | 已完成主稿编号化；见 `docs/rh-c5-dgap-maintext-final.md` |
| C6 no-cycle | 将事件图势函数下降写成形式化图论引理 | 已完成主稿编号化；见 `docs/rh-c6-no-cycle-maintext-final.md` |
| C9 tail closure | 将 Vaaler/Fourier 尾项链逐项定理化 | 已完成主稿编号化；见 `docs/rh-c9-tail-maintext-final.md` |
| EXT packages | 给 Titchmarsh/Ingham/IK/Katz/Vaaler/BG/Baker/Selberg/Vaughan 具体章节/定理号 | 章节/论文级定位已完成，专著页码待排版核验 |
| Main theorem | 删除 review form 并改题名/摘要口径 | 已完成 U1/U4；仍保留 submission warning |
| U5 compile | 编译 LaTeX/BibTeX 并核查 undefined refs/cites | 未完成 |

## 4. 审稿结论

本轮可以标记完成的是：`EXT-PC1-LI` 精确适配、`EXT-KL` 精确适配、GEE 同尺度矛盾修补、普通 proof 标记清零。

本轮不能完成的是：把主定理升级为最终无条件 RH 定理。C4、C5、C6、C9 均已完成主稿编号化。下一步应进行主定理升级前的全文交叉引用、外部定理号和 warning 删除条件总审查。


## 最终全文升级审查评审更新

新增 `docs/rh-final-upgrade-review-2026-05-01.md`。自动扫描确认 `Consolidated proof`、`Proof sketch for review`、`Review proof` 均为 0，且 LaTeX `\ref` 未发现缺失标签。但审查结论是不应删除主定理 `review form` 与 `Submission warning`：主稿仍有条件合成口径、AEX 输入接受性和 EXT 页码/定理号核验义务。下一步最优为逐项处理 U1--U3：主定理前提改写、AEX 条件化措辞消除、EXT 精确定理号表。


## U2 AEX 接受性核验更新

新增 `docs/rh-u2-aex-acceptance-review.md`。审查确认 AEX-1 已由 Baseline-Subtraction、PI-Lac、PI-Dense 支撑，PI-Dense 已归约到 DSO-SF/EXT-KL；AEX-2 由 DSO-SF 支撑；AEX-3 的单变量入口由 EXT-KL 支撑，Tail/RKS、双变量 PPI 与 DSO-E 均转入已命名出口或 DSO-SF。LaTeX 主稿已删除 “conditional exactly on AEX-1, AEX-2, AEX-3” 措辞，改为由前文 AEX propositions 与已记录输入支撑。主定理 warning 仍保留；下一步最优为 U3 EXT 页码/定理号表。


## U3 EXT 精确引用表更新

新增 `docs/rh-u3-ext-reference-table.md`。U3 已完成章节/论文级定位：Vaaler、Baker、Vaughan 给出卷期页码；Bourgain--Garaev 给出 arXiv/DOI；Iwaniec--Kowalski、Katz、Titchmarsh--Heath-Brown、Ingham、Halberstam--Richert 给出章节/定理定位与受限使用边界。专著具体页码仍可在最终排版时核对，但不再作为数学逻辑缺口。下一步最优转向 U1/U4：主定理前提和 review-draft 口径统一。


## U1/U4 主定理与文体口径更新

LaTeX 主稿已完成 U1/U4：标题、摘要和 GEE 说明从旧审查稿文体改为 verification manuscript / final synthesis 口径；主定理标题删除 `review form`，定理陈述由 `Assume Theorems...` 改为 `By Theorems...` 的前文合成口径。`Submission warning` 仍保留，用于诚实标记 U5 最终编译审查、专著页码核验和独立逐行 referee verification 尚未完成。下一步最优为 U5 编译与引用一致性审查。


## U5 最终编译与引用一致性审查更新

新增 `docs/rh-u5-final-compile-audit.md`。已安装 TeX Live 工具链并真实运行 `latexmk -pdf -interaction=nonstopmode -halt-on-error rh-contradiction-field.tex`，生成 `paper/rh-proof/rh-contradiction-field.pdf`。40 个 label、57 个 ref 全匹配，11 个 cite 均有 BibTeX 条目，日志无 undefined refs/cites；`review form/review draft/Assume Theorems/conditional synthesis/exttt` 主稿残留为 0。本轮还把 EXT 外部来源表接入正式 `\cite{...}`，并修正 section/table 引用措辞。剩余为专著页码核验和独立逐行 referee verification；版式日志已清零，`Submission warning` 仍需保留。


## 最终审稿义务闭合账本更新

新增 `docs/rh-final-referee-obligations-closure.md`。作者侧可执行义务已经完成：U1/U4 文体与主定理口径、U2 AEX、U3 EXT 定位、U5 latexmk/PDF/BibTeX、undefined refs/cites 与版式 warning 均已处理。剩余项被精确界定为外部审稿/排版义务：专著页码级核验与独立逐行 referee verification。由于这两项不能由作者自称完成，`Submission warning` 仍应保留，不能宣称 RH 无条件证明定稿。
