# RH PC2 主稿证明最终化记录

本文记录 `paper/rh-proof/rh-contradiction-field.tex` 中 PC2 段落的审稿状态更新。

## 已完成事项

- 将 `CRT zero-frequency baseline` 的 `Review proof` 升级为普通 `proof`。
- 在主稿内展开 `M_z=\prod_{p\le z}p=X^{o(1)}` 的初等 Chebyshev 估计。
- 对每个 reduced residue class 写出平滑 Riemann 和估计，并求和得到 `C_z-C_z^0=O_W(M_z)=o(\Delta)`。
- 明确说明窗口内素数均大于 `z`，因此全部落在 CRT 非零类候选账本中。
- 补入候选账本恒等式 `C_z=P_z+B_z+Err_z` 与素数幂误差 `O_W(X^{1/2}\log^C X)=o(\Delta)`。

## 审稿口径

PC2 现在是初等 CRT 周期计数引理，不再依赖未展开附录。剩余审稿重点转向主链后段的 GEE 负担汇总与 AEX-3 附近残留证明标记。
