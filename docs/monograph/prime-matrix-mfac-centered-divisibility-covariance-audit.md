# MFAC 中心化整除协方差有限谱审计

对 `2 <= d,e <= D`，本审计使用精确核

\[C_X(d,e)=\lfloor X/[d,e]\rfloor-\lfloor X/d\rfloor\lfloor X/e\rfloor/X.\]

其二次型等于中心化整除总负载的有限平方和。

- 参数：`X=4096`，`D=8`，`theta=0.25`
- 有限加权最小强制比读数：`0.1437035256654433`
- 最大特征残差：`5.933404809144172e-14`
- 近退化支持：`[{'index': 6, 'coefficient_estimate': -0.02061015088535316}, {'index': 2, 'coefficient_estimate': 0.014069916504568519}, {'index': 3, 'coefficient_estimate': 0.013137454580204372}]`

```text
uniform_weighted_coercivity_proved=false
actual_chebyshev_energy_bridge_proved=false
actual_mellin_contraction_present=false
rh_proved=false
```

有限谱读数不构成跨尺度统一强制性。即使未来得到该强制性，仍须独立建立非循环的 Chebyshev 能量桥接和 dyadic 到 Mellin 的可和性；本证书**不构成 RH 证明**。
