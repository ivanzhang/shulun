# 常数吸收编号不等式证明

本文件把 `docs/constants-absorption-final-audit.md` 改写为与抽取器相对应的编号不等式。

## I1. 尾界强于主缺口

`tail_error_power=4 > A_star=2`。

故 Tail-log4 的尾部误差 `P/log^4P` 可吸收主链 `P/log^2P` 级覆盖缺口中的尾部项。

## I2. RKS 对数节省余量

RKS 参数账本给总损失

`L_RKS=74`。

常数包给

`K_sieve_log_saving=128`。

因此

`K_sieve_log_saving-L_RKS=54>0`。

## I3. D 组结构对数损失

D 组四个主结构指数为

`A_OMR_log=A_CGTP_log=A_LSMP_log=A_collision_span_log=8`。

总结构损失

`L_D=8+8+8+8=32`。

于是

`L_D < K_sieve_log_saving=128`。

## I4. Weil 完成法损失

`A_weil_completion_log=4`，故

`A_weil_completion_log + L_D = 36 < 128`。

Weil/NRC 完成法损失可与 D 组结构损失同时吸收。

## I5. OMR 安全幂余量

`epsilon_OMR_power=64`。

CGTP 二次能量最坏产生 `Λ^4` 型损失，D 组将其计入至多 `log^16K` 与偏差幂损失。`64` 远大于所需的二次能量安全幂，故抽取器中 OMR 包不会反向消耗 Tail-log4 主余量。

## I6. 小区间直接验证重叠

理论抽取给

`log_P0_upper=3.5`。

有限验证覆盖

`logP<=5`。

因 `3.5<5`，理论段 `P>exp(3.5)` 与有限段 `P<=exp(5)` 重叠，覆盖所有奇素数。

## I7. 抽取器一致性

`experiments/extract_p0.py` 检查 I1--I6 对应的布尔条件和常数正性条件，并输出 `log_P0_upper=3.5`。因此常数包与证明账本一致。
