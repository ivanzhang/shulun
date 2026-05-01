# C6 no-cycle 主稿编号化完成记录

本文记录 `paper/rh-proof/rh-contradiction-field.tex` 中 C6 internal terminal no-cycle 的审稿升级。

## 已完成事项

- 新增 `Definition C6 internal state graph`：明确内部节点 `A,PI,FCT,SC` 与内部边的含义。
- 新增 Lyapunov 向量 `𝓛=(𝓐pot,𝓝,𝓥,𝓒_PI,𝓡)`，统一 ACC、FCT、SC、PI 的下降/容量账本。
- 新增 `Lemma C6 self-loop exclusion`：分别排除 `A`、`FCT`、`SC`、`PI` 的无限自环。
- 新增 `Lemma C6 mixed-cycle exclusion`：用字典序 Lyapunov 下降或转出排除混合环。
- 将原 C6 consolidated proof 改为由两个编号引理推出的正式证明。

## 审稿口径

C6 现在不再只是摘要式 no-cycle 说明，而是有定义、两个中间引理和最终定理的主稿证明链。它仍依赖 A/FCT/SC/PI 各自的“重复模板转出或势函数下降”支撑命题；这些支撑已由既有 GEE/PC4 审查文档记录。

## 下一步

在主定理升级阻断表中，C6 可标记为“主稿编号化完成”。下一步最优应转向 C9 Fourier--Vaaler tail closure，因为它仍是 consolidated proof 形式且长度相对可控。
