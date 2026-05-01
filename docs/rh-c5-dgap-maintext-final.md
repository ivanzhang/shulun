# C5 DGap branch 主稿编号化完成记录

本文记录 `paper/rh-proof/rh-contradiction-field.tex` 中 C5 DGap branch 的审稿升级。

## 已完成事项

- 新增 `Lemma C5.1 DGap box localization`：把 DGap 正质量局部化到固定复杂度、有限重叠盒族，失败进入 `LV/SC/LSMP/CE`。
- 新增 `Lemma C5.2 frame lower bound after baseline removal`：用盒函数 frame/Bessel 下界，把非基线 DGap 负担转为非恒定投影能量。
- 新增 `Lemma C5.3 orthogonal projection allocation`：用逐步正交投影分配到 `PI`、低维/短簇/低体积出口或注册容量失败。
- 新增 `Lemma C5.4 low-dimensional residual extraction`：借助 C9 尾项闭合，把低维残余路由到 `FCT` 或 `DSO/PI`。
- 将原 C5 consolidated proof 改为由四个编号引理推出的正式证明链。

## 审稿口径

C5 现在不再是摘要式 DGap 说明，而是单篇主稿中的编号化三接口链：盒局部化、frame 下界、正交分配、低维抽取。它仍引用已登记的 C9 tail closure、PC2 baseline、PI/DSO/FCT/SC/LV/LSMP/CE 接口；这些在当前主稿或归档文档中已有对应入口。

## 当前全稿状态

C4、C5、C6、C9 的 `Consolidated proof` 已全部消除。主稿仅保留主定理 `review form` 与 submission warning，原因是最终 RH 定理升级仍需整篇引用链的顶层接受性审查和排版级外部定理号核验。
