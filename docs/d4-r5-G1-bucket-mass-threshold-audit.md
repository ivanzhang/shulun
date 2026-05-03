# D4/R5 G1 桶质量阈值反解审计

**状态：** `tau_9_59_or_tau_ge17_mass_thresholds_are_plausible_but_need_structural_proof`

对近危险支撑向量反解可见，单独 tau_17_32 质量下界通常过强；tau>=17 或 tau=9..59 的合并质量阈值更自然。但二块反解只是充分条件，正式证明仍应回到六桶二次型；最有希望的定理化约束是：低 tau 支撑接近饱和时，中高 tau 总质量存在强制下界。

## 组质量阈值摘要
- `tau_17_32`：{'min_margin_top20_vectors': -0.06145711953324606, 'max_required_top20_vectors': 0.3912528965708799, 'min_actual_top20_vectors': 0.2587141445639177}
- `tau_17_59`：{'min_margin_top20_vectors': -0.04691012503302178, 'max_required_top20_vectors': 0.3926901965402043, 'min_actual_top20_vectors': 0.3362712279682688}
- `tau_ge_17`：{'min_margin_top20_vectors': -0.008299564461815567, 'max_required_top20_vectors': 0.4088722811775605, 'min_actual_top20_vectors': 0.37753014657582357}
- `tau_9_32`：{'min_margin_top20_vectors': -0.12408418497644902, 'max_required_top20_vectors': 0.6657789471999946, 'min_actual_top20_vectors': 0.5161685800767233}
- `tau_9_59`：{'min_margin_top20_vectors': -0.04960814419568016, 'max_required_top20_vectors': 0.6915297572908078, 'min_actual_top20_vectors': 0.5704781306196008}

## 证明义务
- 证明低三桶支撑数大时，tau>=17 或 tau=9..59 的质量不能低于反解门槛。
- 把该质量下界代入六桶二次型，而非二块粗并，以保留额外余量。
- 若统一质量下界太强，则按近危险 n 向量分族证明局部阈值。
