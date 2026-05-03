# D4/R5 精确符号模板状态

## 已完成

- `experiments/d4_r5_symbolic_template_extractor.py` 提取了完整危险窗口 400 行的精确符号模板。
- 结果：400 个精确模板、0 个碰撞。
- 这说明保留绝对 floor 数据时模板过细。

## 见证骨架库

`experiments/d4_r5_symbolic_skeleton_library.py` 删除绝对 floor 数据后，对窗口极值见证得到 3 个骨架：

| 接口 | 示例 x | groups | a-total |
|---|---:|---:|---:|
| R5global1 | 1088588 | 104 | 201 |
| R5global2 | 1088475 | 106 | 230 |
| R5global3 | 1088373 | 87 | 218 |

证书：`docs/d4-r5-symbolic-witness-skeleton-library.json`

## 真正剩余解析点

需要证明：任何满足 R5global1--R5global4 约束的极值相位单元，在删除绝对 floor 数据后，必须落入有限 offset/a 骨架族。

当前文档只给出窗口证据与骨架候选，不给出全局覆盖证明。
