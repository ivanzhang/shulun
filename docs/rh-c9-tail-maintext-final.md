# C9 Fourier--Vaaler tail 主稿编号化完成记录

本文记录 `paper/rh-proof/rh-contradiction-field.tex` 中 C9 tail closure 的审稿升级。

## 已完成事项

- 新增 `Definition C9 fixed-complexity template`：限定允许的平滑窗、硬区间平滑替代、dyadic 标签、CRT 字符、倒数环带与 Bohr 弧原子。
- 新增 `Lemma C9.1 atomic tails`：逐原子证明尾项平方可和，失败进入命名出口。
- 新增 `Lemma C9.2 Boolean stability`：固定深度布尔组合保持尾项平方可和。
- 新增 `Lemma C9.3 box summation`：有限重叠盒族只造成多对数损失。
- 新增 `Lemma C9.4 no free high-frequency tail`：高频尾项若承载固定比例异常，必须进入 `CE/LSMP/LV/SC/FCT/DSO/PI`。
- 将原 C9 consolidated proof 改为由四个编号引理推出的正式证明链。

## 审稿口径

C9 现在不再是摘要式 Fourier/Vaaler 尾项说明，而是单篇主稿中的编号化证明链。它仍依赖 `EXT-Vaaler` 的标准一维区间逼近；该外部输入已在 `docs/rh-ext-precision-final.md` 中限定为受限引用。

## 下一步

在主定理升级阻断表中，C9 可标记为“主稿编号化完成”。剩余 consolidated proof 只剩 C4 sparse branch 与 C5 DGap branch；下一步最优应先处理 C4，因为它是分支路由骨架，能减少 C5 的依赖歧义。
