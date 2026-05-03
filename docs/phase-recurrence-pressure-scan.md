# 相位回归压力扫描

**状态：** `label_modulus_product_exceeds_P_but_short_recurrence_not_full_in_samples`

大因子标签集合的模数乘积很快超过 P，说明若短复现要求稳定这些标签会立刻 CRT 矛盾；但实验未显示自然短步长会全覆盖复现，关键仍是从全覆盖假设推出短回归。

## 摘要
- P=211：r=2 labels=4 distinct=2 prod>P=True best=0.009; r=52 labels=20 distinct=15 prod>P=True best=0.071; r=105 labels=15 distinct=10 prod>P=True best=0.047; r=158 labels=22 distinct=17 prod>P=True best=0.081; r=211 labels=27 distinct=21 prod>P=True best=0.100
- P=401：r=2 labels=3 distinct=1 prod>P=False best=0.002; r=100 labels=33 distinct=25 prod>P=True best=0.062; r=200 labels=31 distinct=28 prod>P=True best=0.070; r=300 labels=33 distinct=27 prod>P=True best=0.067; r=401 labels=35 distinct=26 prod>P=True best=0.065
- P=809：r=2 labels=15 distinct=3 prod>P=True best=0.004; r=202 labels=63 distinct=45 prod>P=True best=0.056; r=404 labels=74 distinct=47 prod>P=True best=0.058; r=606 labels=66 distinct=39 prod>P=True best=0.048; r=809 labels=67 distinct=46 prod>P=True best=0.056
- P=1601：r=2 labels=24 distinct=4 prod>P=True best=0.002; r=400 labels=120 distinct=70 prod>P=True best=0.042; r=800 labels=121 distinct=80 prod>P=True best=0.049; r=1200 labels=127 distinct=84 prod>P=True best=0.051; r=1601 labels=126 distinct=82 prod>P=True best=0.051
- P=3203：r=2 labels=37 distinct=6 prod>P=True best=0.002; r=800 labels=219 distinct=122 prod>P=True best=0.037; r=1601 labels=234 distinct=145 prod>P=True best=0.044; r=2402 labels=227 distinct=136 prod>P=True best=0.042; r=3203 labels=240 distinct=144 prod>P=True best=0.044

## 下一证明义务
- 证明全覆盖迫使某个大标签子集在短步长下相位稳定。
- 或改用行列双向闭锁推出短回路。
- 将标签模数乘积超过 P 作为 CRT 矛盾的后半段。
