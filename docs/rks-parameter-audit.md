# RKS-parameter-audit 对数损失账本

统一参考文献标签见 `docs/bibliography.md`。
本文件完成 `RKS-bridge` 降级后的参数核对：确认 TL4-L 中 Type I/II、端点块、`r,h` 求和、dyadic 分块与 Vaughan 系数的总对数损失可由保守常数 `K_sieve_log_saving=128` 吸收。

## 1. 覆盖分区核对

TL4-L 的 Vaughan 块 `S(M,N)` 满足 `MN≈P`。按短侧 `S=min(M,N)` 分区：

1. `S<=P^{1/18}`：逐短变量 Weil 完成和，贡献 `<=S P^{1/2}log^C P<=P^{5/9}log^C P`，强于 `P/log^44P`。
2. `P^{1/18}<S<P^{7/12-ε}`：长侧 `P/S>P^{5/12+ε}`，落入 BG 双线性覆盖区。
3. `S>=P^{7/12-ε}` 不可能与 `MN≈P` 同时两侧均为短侧定义；此时两变量较平衡或可由多线性分裂进入 BG `Kloost 1/2`。
4. 端点低体积块：总长度 `<=P/log^A P`，平凡吸收。

因此不存在未覆盖的 Type I/II 长度区域；剩余只是不等式和对数损失核算。

## 2. 对数损失账本

保守记录如下：

| 来源 | 损失指数 |
| --- | ---: |
| `r<=log^8P` 求和 | 8 |
| `h<=log^16P` Fourier 模 | 16 |
| dyadic `M,N` 分块 | 4 |
| Vaughan 恒等式分块 | 10 |
| bounded variation/Abel 平滑 | 10 |
| divisor-bounded 系数分层 | 10 |
| Vaaler 截断非主误差缓冲 | 8 |
| BG/Weil 覆盖区切换安全余量 | 8 |
| **合计** | **74** |

合计 `74<128=K_sieve_log_saving`。因此即使 TL4-L 目标需要 `log^{-44}P`，预先要求 BG/Weil 覆盖区提供 `log^{-(44+74)}P` 级余量即可；BG 幂节省和短侧 Weil 的幂节省均强于任意固定对数余量。

## 3. 与保守常数包的关系

当前保守常数包中：

- `K_sieve_log_saving=128`；
- 内部机械损失 `C_vaughan_blocks+C_rect_variation+C_divisor_coeff=30`；
- TL4-L 本账本给出 RKS 侧损失 `74`。

两者服务不同接口：`30` 是全局抽取器中的通用内部损失，`74` 是 TL4-L 内部要求输入定理预留的对数节省。由于 TL4-L 最终只向抽取器报告 `tail_error_power=4`，本账本不需要新增 JSON 字段；它只是证明 `tail_error_power=4` 的内部余量。

## 4. 审稿结论

RKS-parameter-audit 通过：长度分区无缺口，总对数损失保守小于 `128`。Tail-log4 的 TL4-L 剩余义务从“新桥接估计”降为“在最终论文中逐项引用 BG/Weil 并保留本账本”。
