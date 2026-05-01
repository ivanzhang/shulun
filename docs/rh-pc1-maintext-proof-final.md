# RH PC1 主稿证明最终化记录

本文记录 `paper/rh-proof/rh-contradiction-field.tex` 中 PC1 段落的审稿状态更新。

## 已完成事项

- 将 `PC1 Landau--Ingham input` 的 `Proof sketch for review` 升级为普通 `proof`。
- 在主稿内展开平滑显式公式的 Mellin 反演、轮廓移动和零点残数来源。
- 在有限边界零点情形中写出非零有限三角多项式与均方正性论证。
- 在一般无限边界或上确界情形中精确保留 `EXT-PC1-LI` 作为经典 Landau--Ingham 振荡输入。
- 补入固定符号子列选择与素数幂项 `O_W(X^{1/2}\log^C X)` 的吸收。

## 审稿口径

PC1 现在不再是主稿中的“证明草图”。其剩余外部义务仅为 `EXT-PC1-LI` 的标准文献核验；该义务已经被 `docs/rh-ext-precision-final.md` 纳入外部输入精确化表。

## 后续最优先项

PC2 已在 `docs/rh-pc2-maintext-proof-final.md` 中完成主稿化。下一步应处理主定理 `review form` 与外部输入精确引用核验，特别是 `EXT-PC1-LI`、`EXT-KL`、`EXT-Vaaler`、`EXT-Selberg/BT/BG` 的逐项匹配。
