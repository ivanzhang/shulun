# 分层阈值增长缺口实验

**状态：** `threshold_choice_changes_patch_gap_sqrt_layer_is_natural_but_not_enough_alone`

扫描不同阈值 Y=P^alpha 后，sqrt(P) 层最自然：Y 以下筛掉小因子，Y 以上每个剩余合数只能有少数大因子。但仅凭粗计数仍接近 Legendre/短区间素数问题，必须叠加 CRT 周期刚性或大因子互斥的短块版本。

## 摘要
- P=211：Y=5 alpha=0.30 max_patch=0.719 min_unpatched=16; Y=8 alpha=0.39 max_patch=0.673 min_unpatched=16; Y=14 alpha=0.49 max_patch=0.628 min_unpatched=16; Y=24 alpha=0.59 max_patch=0.543 min_unpatched=16; Y=35 alpha=0.66 max_patch=0.515 min_unpatched=16
- P=401：Y=7 alpha=0.32 max_patch=0.641 min_unpatched=33; Y=10 alpha=0.38 max_patch=0.641 min_unpatched=33; Y=20 alpha=0.50 max_patch=0.522 min_unpatched=33; Y=36 alpha=0.60 max_patch=0.441 min_unpatched=33; Y=54 alpha=0.67 max_patch=0.340 min_unpatched=33
- P=809：Y=9 alpha=0.33 max_patch=0.697 min_unpatched=56; Y=14 alpha=0.39 max_patch=0.639 min_unpatched=56; Y=28 alpha=0.50 max_patch=0.566 min_unpatched=56; Y=55 alpha=0.60 max_patch=0.477 min_unpatched=56; Y=86 alpha=0.67 max_patch=0.411 min_unpatched=56
- P=1601：Y=11 alpha=0.32 max_patch=0.672 min_unpatched=109; Y=19 alpha=0.40 max_patch=0.608 min_unpatched=109; Y=40 alpha=0.50 max_patch=0.551 min_unpatched=109; Y=83 alpha=0.60 max_patch=0.460 min_unpatched=109; Y=136 alpha=0.67 max_patch=0.411 min_unpatched=109
- P=3203：Y=14 alpha=0.33 max_patch=0.678 min_unpatched=197; Y=25 alpha=0.40 max_patch=0.623 min_unpatched=197; Y=56 alpha=0.50 max_patch=0.550 min_unpatched=197; Y=126 alpha=0.60 max_patch=0.476 min_unpatched=197; Y=217 alpha=0.67 max_patch=0.424 min_unpatched=197
- P=6421：Y=18 alpha=0.33 max_patch=0.692 min_unpatched=357; Y=33 alpha=0.40 max_patch=0.636 min_unpatched=357; Y=80 alpha=0.50 max_patch=0.549 min_unpatched=357; Y=192 alpha=0.60 max_patch=0.472 min_unpatched=357; Y=345 alpha=0.67 max_patch=0.424 min_unpatched=357

## 下一证明义务
- 证明 sqrt(P) 筛后洞数的显式下界。
- 证明大因子补洞在长度 sqrt(P) 块中的局部上界。
- 用块级缺口避免直接诉诸完整短区间素数定理。
