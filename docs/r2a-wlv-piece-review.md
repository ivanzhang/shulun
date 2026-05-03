# R2a WLV-piece 三步复核

**状态：** `WLV_piece_review_passed_modulo_existing_atlas_and_parameter_ledger`

WLV-piece 的 signed/complex 旋转、总变差到二维盒片、LV-KS 权重吸收三步均已拆成确定性审稿点；剩余不再是新数学接口，而是确认引用的低体积 atlas 与 C_poly 参数账本被最终接受。

## 复核项
### W1_complex_phase_rotation
- 命题：signed/complex Stieltjes 测度经极分解和四象限旋转后，只损失固定常数。
- 状态：`closed_deterministic`
- 审查说明：不使用随机符号或正相关假设。
- 证据：docs/final-proof-draft.md:WLV-rot, docs/final-proof-draft.md:6.18.1d-WLV

### W2_variation_to_box_piece
- 命题：Hardy--Krause 分部后，端点/角点承载大值则入低体积坏层；否则存在二维正常盒片承载大值。
- 状态：`closed_modulo_existing_low_volume_atlas`
- 审查说明：避免把总变差集中在低维端点误判为二维密度。
- 证据：docs/final-proof-draft.md:WLV-piece, docs/final-proof-draft.md:6.14.2c-FS8

### W3_LV_weight_absorption
- 命题：抽取的正权盒片在 vdC 平移后仍满足 KS-W 型变差界，新增端点由 C_WLV/C_poly 支付。
- 状态：`closed_modulo_parameter_ledger`
- 审查说明：若平移端点超账本，则归入 dyadic 端点/低体积坏层。
- 证据：docs/final-proof-draft.md:KS-W, docs/final-proof-draft.md:KS-W-poly, docs/r2-Cpoly-absorption-scan.md
