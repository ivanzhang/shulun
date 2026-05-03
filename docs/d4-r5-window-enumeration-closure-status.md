# D4/R5 完整危险窗口枚举闭合状态

## 完成范围

对完整危险窗口 `[1088200,1088600)` 的 400 个整数行完成逐行成员签名与层泛函枚举。

证书：`docs/d4-r5-window-phasecell-enumeration-1088200-1088600.json`

结果：

- `row_count=400`
- `unique_member_signature_count=400`
- `all_window_checks_ok=true`
- R5global1 窗口极值：`x=1088588`
- R5global2 窗口极值：`x=1088475`
- R5global3 窗口极值：`x=1088373`

对这 3 个极值见证的 6 个左右半单元运行固定成员根证书和外向舍入审计：

- `docs/d4-r5-window-query-witnesses-one-sided-batch.json`
- `docs/d4-r5-window-query-witnesses-outward-audit.json`

结果：

- `root_boxes=0`
- `unresolved=0`
- `all_certified=true`

## 严格边界

这证明完整危险窗口内没有遗漏整数行候选，并且极值见证的连续左右邻域没有内部导数极值。

这仍不是所有尺度窗口的 R5global 解析证明。下一步必须把窗口枚举器提升为解析相位模板枚举器：用参数化相位单元替代固定窗口逐行枚举，并证明所有尺度窗口都由有限模板族覆盖。
