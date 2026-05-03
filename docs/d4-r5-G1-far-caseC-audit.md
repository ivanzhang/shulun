# D4/R5 G1 far tail Case C 审计

**状态：** `case_C_balanced_scan_safe_not_current_bottleneck`

Case C balanced 的 far/head 扫描最坏约 0.3648，显著低于 0.435；因此它不是当前闭合瓶颈。Case C 可用较粗的联合预算闭合，真正瓶颈回到 Case A low4>=0.20 的极端低 tau 点。

## Case C 定义
- `low4<0.20 and hi9<0.08`
- 样本数：`971`

## 最坏记录
- far 最坏：{'x': 1001500, 'low4': 0.16434991022887022, 'mid8': 0.16548701889262674, 'hi9': 0.03496130104128009, 'far': 0.36479823016277707}
- mid8 最坏：{'x': 1001500, 'low4': 0.16434991022887022, 'mid8': 0.16548701889262674, 'hi9': 0.03496130104128009, 'far': 0.36479823016277707}

## 下一焦点
- Prove Case A low4>=0.20 implies far/head<=0.435, likely by classifying low tau<=4 saturation and showing mid8+hi9 cannot exceed about 0.21 there.
