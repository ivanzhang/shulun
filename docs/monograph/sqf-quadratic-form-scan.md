# SQF Selberg 二次型 Mellin 预算扫描

**状态：** `mellin_budget_scan_not_a_proof`

本实验近似扫描

\[
\int |\widehat\Phi(it)|\,|H(it)|\,|Q(it)|\,dt
\]

并与平凡预算 `int |Phihat| K sum|omega_l|/l dt` 比较。

## 摘要
- P=2003 M=P^1.2 R=P^0.3 omega=13 budget/trivial=0.196 Q0/Qabs=0.176 avgQ/Qabs=0.538 avgH/K=0.299 top t=-1.0 Q/Qabs=0.339 H/K=0.803
- P=2003 M=P^1.2 R=P^0.35 omega=31 budget/trivial=0.175 Q0/Qabs=0.136 avgQ/Qabs=0.487 avgH/K=0.299 top t=-1.0 Q/Qabs=0.309 H/K=0.803
- P=2003 M=P^1.4 R=P^0.3 omega=13 budget/trivial=0.196 Q0/Qabs=0.176 avgQ/Qabs=0.538 avgH/K=0.299 top t=-1.0 Q/Qabs=0.339 H/K=0.803
- P=2003 M=P^1.4 R=P^0.35 omega=31 budget/trivial=0.175 Q0/Qabs=0.136 avgQ/Qabs=0.487 avgH/K=0.299 top t=-1.0 Q/Qabs=0.309 H/K=0.803
- P=5003 M=P^1.2 R=P^0.3 omega=21 budget/trivial=0.184 Q0/Qabs=0.149 avgQ/Qabs=0.504 avgH/K=0.299 top t=-1.0 Q/Qabs=0.317 H/K=0.803
- P=5003 M=P^1.2 R=P^0.35 omega=58 budget/trivial=0.165 Q0/Qabs=0.115 avgQ/Qabs=0.455 avgH/K=0.299 top t=-1.0 Q/Qabs=0.297 H/K=0.803
- P=5003 M=P^1.4 R=P^0.3 omega=21 budget/trivial=0.184 Q0/Qabs=0.149 avgQ/Qabs=0.504 avgH/K=0.299 top t=-1.0 Q/Qabs=0.317 H/K=0.803
- P=5003 M=P^1.4 R=P^0.35 omega=58 budget/trivial=0.165 Q0/Qabs=0.115 avgQ/Qabs=0.455 avgH/K=0.299 top t=-1.0 Q/Qabs=0.297 H/K=0.803
- P=10007 M=P^1.2 R=P^0.3 omega=35 budget/trivial=0.173 Q0/Qabs=0.131 avgQ/Qabs=0.479 avgH/K=0.299 top t=-1.0 Q/Qabs=0.306 H/K=0.803
- P=10007 M=P^1.2 R=P^0.35 omega=82 budget/trivial=0.155 Q0/Qabs=0.100 avgQ/Qabs=0.430 avgH/K=0.299 top t=-1.0 Q/Qabs=0.289 H/K=0.803
- P=10007 M=P^1.4 R=P^0.3 omega=35 budget/trivial=0.173 Q0/Qabs=0.131 avgQ/Qabs=0.479 avgH/K=0.299 top t=-1.0 Q/Qabs=0.306 H/K=0.803
- P=10007 M=P^1.4 R=P^0.35 omega=82 budget/trivial=0.155 Q0/Qabs=0.100 avgQ/Qabs=0.430 avgH/K=0.299 top t=-1.0 Q/Qabs=0.289 H/K=0.803

## 证明判读

- `Q0/Qabs` 小：Selberg 二次型在低频已有强符号相消。
- `budget/trivial` 小：`SQF` 主要来自 `Q(it)` 与短 `h` 和的共同相消。
- 若 `top integrand` 集中在小 `t`，应优先证明低频 `Q(it)` 零阶抵消。
- 若大 `t` 主导，则需要依赖 `Phihat` 衰减或平滑截断提升。

## 下一步接口

将 `SQF` 拆为：

```text
SQF-Q0: Q(it) 在低频相对 sum|omega|/ell 有固定节省；
SQF-PHI: 平滑截断使 |Phihat(it)| 快速衰减；
SQF-H: 短 h-sum 在中高频提供平均节省。
```
