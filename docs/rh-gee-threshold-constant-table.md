# GEE 阈值常数总表

本文补 `docs/rh-gee-global-synthesis-audit.md` 的第二项剩余义务：统一所有 `Δ/log^B X` 与 `log^C X` 损失。目标是给出可审查的常数选择顺序，确保所有吸收项确为 `o(Δ)`。

## 1. 损失来源

定义总损失常数：

`C_total=C_route+C_seed+C_dyadic+C_Vaaler+C_Fourier+C_smooth+C_frame+C_template+C_capacity+C_NRC+C_coarea+C_boundary+100`。

各项含义：

| 常数 | 来源 |
|---|---|
| `C_route` | GEE-0 路由有限重叠 |
| `C_seed` | seed 转出细分与重标记 |
| `C_dyadic` | dyadic 层、短窗网格、频率层 |
| `C_Vaaler+C_Fourier` | Vaaler/Fourier 截断频率与系数和 |
| `C_smooth+C_boundary` | 平滑边界、端点、素数幂误差 |
| `C_frame` | 投影 frame、有限重叠盒族 |
| `C_template` | 固定模板布尔组合复杂度 |
| `C_capacity` | PI/DSO/SC/A 容量账本常数 |
| `C_NRC` | Kloosterman 完成和与 NRC 包求和 |
| `C_coarea` | LSMP coarea、薄层选择、方向筛选 |

所有文档中出现的 `log^C X` 损失均要求由 `C_total` 支配。

## 2. 阈值选择

选择最终吸收余量

`B_final=10C_total+100`。

各出口使用：

- `B_LV>=B_final+C_total`；
- `B_LSMP>=B_final+C_total`；
- `B_SC>=B_final+C_total`；
- `B_A>=B_final+C_total`；
- `B_PI/DSO>=B_final+C_total`；
- `B_NRC>=B_final+C_total`。

这样任一入口若满足相对阈值

`Mass_eff log^{C_entry}X <= Δ/log^{B_entry}X`, `C_entry<=C_total`,

则总求和后仍有

`Contribution <= Δ/log^{B_final}X=o(Δ)`。

## 3. 内部转移不消耗阈值

`A/FCT/SC` 的内部势函数下降步不登记最终 `Load`，因此不需要单独 `o(Δ)` 阈值；只需保证其 seed 转出重叠被 `C_seed` 吸收。

`PI/DSO` 的零频容量由 Baseline-Subtraction 扣除，不进入 `Load`；只需对超额偏差使用 `B_PI/DSO`。

`CE/LSMP` 的 seed 转出不进入自身负担；只需对可吸收项使用 `B_LSMP`。

## 4. Theorem Threshold-Compatibility

**Theorem.** 若所有局部文档中的对数损失均被 `C_total` 支配，并按第 2 节选择各出口阈值，则所有可吸收项贡献总和为 `o(Δ)`；内部转移和 seed 转出不改变该估计。

**证明。** 对每个可吸收入口，局部阈值给 `<=Δ/log^{B_entry-C_entry}X`。所有入口类型和路由重复至多再损失 `log^{C_total}X`，故总贡献 `<=Δ/log^{B_final}X`。内部转移不登记最终负担；seed 转出只重标记同一超额偏差并由 `C_seed` 计入 `C_total`。证毕。

## 5. 审稿备注

本文给出的是常数层级方案，不抽取数值 `P_0`。若最终论文要求显式 `P_0`，需把 `C_total` 中每一项替换为具体整数并运行有限验证；当前 GEE 合成只需要固定对数余量。
