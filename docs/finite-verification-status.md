# 有限验证状态

**状态：** 有限范围计算验证；不替代无条件证明。

## 1. 本轮验证

运行命令：

`python3 experiments/verify_finite_p_grid.py --max-p 5000 --quiet`

结果：

`SUMMARY: all passed for 668 odd primes P<= 5000`

含义：对所有 `P<=5000` 的奇素数，脚本验证：

- `P×P` 方阵每一行含至少一个素数；
- 除第 `P` 列外，每一列含至少一个素数。

## 2. 验证方法

脚本对每个奇素数 `P`：

- 构造 `0..P^2` 的素性筛；
- 逐行检查区间 `[(r-1)P+1,rP]`；
- 逐列检查 `{c+kP:0<=k<P}`，其中 `1<=c<P`。

这是直接验证目标命题本身。

## 3. 诚实边界

该有限验证只覆盖 `P<=5000`。剩余无限范围仍需全局证明。根据 `docs/final-closure-hard-obstruction-review.md`，列命题强接近最小等差素数 `p(a,P)<P^2` 问题，不能由有限验证或局部参数优化自动闭合。

## 4. 新增验证器与上探计划（2026-04-30）

新增三个实验性验证器：

- `experiments/verify_finite_p_grid_segmented.py`：分段筛流式验证，内存低但当前实现较慢；
- `experiments/verify_finite_p_grid_fast.py`：逐 P bytearray 筛，适合中等上界；
- `experiments/verify_finite_p_grid_byte.py`、`experiments/verify_finite_p_grid_witness_fast.py`：全局 bytearray/见证式尝试，仍需性能优化。

复核通过的稳定证书仍为：

`python3 experiments/verify_finite_p_grid.py --max-p 5000 --quiet`

输出：

`SUMMARY: all passed for 668 odd primes P<= 5000`

下一步若要上探 `P<=50000`，应进一步优化为 C/Rust 实现或 Python+bitarray/segmented prime witness 证书生成，避免 Python 层嵌套遍历。
