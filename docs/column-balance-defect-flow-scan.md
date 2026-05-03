# CRT 列均衡亏损-补偿流扫描

**状态：** `complete_CRT_smallP_confirms_column_balance_and_zero_row_pattern`

小 P 完整 CRT 周期扫描确认除第 P 列外列类素数计数相等。零行若存在，其在周期内的位置呈刚性分布；下一步应研究零行间距与根基模数的关系，判断是否可推广为全行覆盖的周期矛盾。

## 摘要
- P=5 M=6 equal=True zero_rows=[] hist={'1': 4, '2': 2}
- P=7 M=30 equal=True zero_rows=[] hist={'1': 12, '2': 18}
- P=11 M=210 equal=True zero_rows=[] hist={'1': 24, '2': 108, '3': 72, '4': 6}
- P=13 M=2310 equal=True zero_rows=[169, 702, 1609, 2142] hist={'0': 4, '1': 180, '2': 966, '3': 992, '4': 168}

## 下一证明义务
- 分析 zero_rows 的间距 gcd 与 M 的关系。
- 若 P x P 内出现零行，比较其在完整 CRT 周期中的重复位置。
- 将零行亏损视为列均衡缺陷，研究补偿行的相位分布。
