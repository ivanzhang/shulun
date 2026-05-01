# C4 sparse branch 主稿编号化完成记录

本文记录 `paper/rh-proof/rh-contradiction-field.tex` 中 C4 sparse branch / PC3-OV2 的审稿升级。

## 已完成事项

- 新增 `Lemma C4.1 sparse trichotomy`：由 C3 分解把稀疏异常分配到 `ACC/Hole/OV` 三类账本。
- 新增 `Lemma C4.2 coverage and hole exits`：`ACC` 进入 A 分支，`Hole` 进入 `LV/LSMP/CE` 或 baseline-completeness failure。
- 新增 `Lemma C4.3 overlap normal form`：由 AAI 语义把正 overlap 归约为双锚正规形 `n=q_1q_2r`。
- 新增 `Lemma C4.4 main-layer routing`：由 MLC 主层定位、PPI 相位推送和不可检测均匀吸收，把主层 overlap 路由到 `FCT/SC/PI/LV/LSMP/CE/DSO/NRC` 或零频吸收。
- 将原 C4 consolidated proof 改为由四个编号引理推出的正式证明链。

## 审稿口径

C4 现在不再是摘要式 PC3/OV2 说明，而是单篇主稿中的编号化路由链。它仍依赖 AAI/PPI/MLC 既有接口文档的接受性；这些接口已经分别在 `docs/rh-ov2-aai-unconditional-theorem.md`、`docs/rh-ov2-ppi-unconditional-theorem.md`、`docs/rh-ov2-mlc-unconditional-core.md` 与 `docs/rh-ov2-mlc-uniform-absorption.md` 中拆解。

## 下一步

在主定理升级阻断表中，C4 可标记为“主稿编号化完成”。剩余 consolidated proof 只剩 C5 DGap branch；下一步最优应专攻 C5。
