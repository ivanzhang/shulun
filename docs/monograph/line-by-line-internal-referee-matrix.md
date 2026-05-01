# 合著论著逐行内部复核矩阵

本文执行作者侧逐行复核。结论必须区分：

- `PASS-AUTHOR`：作者侧逐行复核未发现内部逻辑断裂；
- `PASS-CONDITIONAL`：若指定外部输入/附录定理被接受，则该步闭合；
- `BLOCK-REFEREE`：不能由作者自证，必须外部独立审稿；
- `BLOCK-MATH`：发现明确数学缺口，需要新增证明。

本轮没有把任何 `BLOCK-REFEREE` 改写为 `PASS-AUTHOR`，以避免把“自审”伪装为独立审稿。

## 1. Prime Matrix 逐行复核

| 编号 | 环节 | 复核内容 | 判定 | 理由 |
|---|---|---|---|---|
| PM-1 | 方阵记号 | `n(r,c)=(r-1)P+c` 与非第 `P` 列排除 | PASS-AUTHOR | `docs/row-column-reduction-formal-appendix.md` AB4 直接证明 |
| PM-2 | 三层分解 | 小因子锁定 / 双粗主体 / 尾部锚不重不漏 | PASS-AUTHOR | AB1 给出优先规则；未发现集合遗漏 |
| PM-3 | 大因子互斥 | 同行/同列同大素因子复用周期 | PASS-AUTHOR | AB2/AB3 为整除差值的直接论证 |
| PM-4 | CRT 均衡 | 非第 `P` 列非零同余类数量与列无关 | PASS-AUTHOR | AB5 为逐素数双射 + CRT 乘法计数 |
| PM-5 | 列归约 | 列全合数反例剥离后进入 Structured-EHPD | PASS-CONDITIONAL | 归约成立依赖 Tail-log4 剥离与 D 组坏配置定义接受 |
| PM-6 | 行归约 | 行全合数反例剥离后进入 Structured-EHPD | PASS-CONDITIONAL | 同 PM-5，另需确认 45 度小因子锁定只归入小因子层 |
| PM-7 | Tail-log4 | 尾部锚误差 `P/log^4P` 级吸收 | PASS-CONDITIONAL | `docs/tail-log4-formal-appendix.md` 已定理化；BG/RKS 外部定理号仍需核验 |
| PM-8 | BG/RKS 分区 | RKS-1--RKS-4 覆盖所有块 | PASS-CONDITIONAL | `docs/bg-rks-block-match.md` 与 `docs/final-cross-reference-matrix.md` 已逐块匹配；需原文定理号 |
| PM-9 | M5 缺口 | `Gap=r-B_0` 与 `γr/log^2P` 一阶偏差桥接 | PASS-CONDITIONAL | `docs/m5-explicit-gap-lemma.md` 已显式化；需与 D 一阶偏差入口逐行外审 |
| PM-10 | D-OMR | 一阶偏差产生高投影或 FCT | PASS-CONDITIONAL | D1--D3 有证明框架；NRC 与 `Λ^2r` 吸收条件需外审 |
| PM-11 | D-CGTP | 高投影增量有限步矛盾 | PASS-AUTHOR | D4/D5 为 martingale 方差账本，逻辑清楚 |
| PM-12 | D-LSMP | 小质量 packing 不产生自由终端 | PASS-CONDITIONAL | D6/D7 依赖 coarea/Vitali 与终端定义一致性；需外审 |
| PM-13 | D-FCT/NRC | frequency closure 与 non-resonance 背景 | PASS-CONDITIONAL | 外部 KL 与祖先 span 定义需外审 |
| PM-14 | 常数吸收 | I1--I7 编号不等式 | PASS-AUTHOR | `docs/constants-numbered-inequalities.md` 与交叉矩阵给出余量；未发现方向错误 |
| PM-15 | 有限验证 | 阈值以下奇素数 | PASS-CONDITIONAL | 证书存在；需复现环境和脚本 hash 才可顶刊化 |
| PM-16 | Prime Matrix 终局 | 行/列素数存在性 | BLOCK-REFEREE | D 组 + Tail-log4 + finite 需独立审稿后才能升级 |

## 2. RH 逐行复核

| 编号 | 环节 | 复核内容 | 判定 | 理由 |
|---|---|---|---|---|
| RH-1 | PC1 显式公式 | 离线零点推出平滑 Chebyshev 异常 | PASS-CONDITIONAL | 主稿编号化；Landau--Ingham 外部输入需页码/定理号核验 |
| RH-2 | PC1 素数幂去除 | Chebyshev 权到素数权 | PASS-AUTHOR | 素数幂 `O(X^{1/2}log^C X)` 对 `β>1/2` 可吸收 |
| RH-3 | PC2 CRT baseline | 候选账本与素数账本转换 | PASS-CONDITIONAL | 主稿有证明；平滑边界与 baseline convention 需外审 |
| RH-4 | C3 分解 | sparse/dense/terminal 三分 | PASS-CONDITIONAL | 结构定义完整，但“不重不漏”需外部逐行核验 |
| RH-5 | C4 sparse | ACC/Hole/OV 路由 | PASS-CONDITIONAL | 主稿编号化；路由接口需外审 |
| RH-6 | C5 dense | DGap/PI/FCT/DSO 分配 | PASS-CONDITIONAL | 正交投影账本存在；capacity failure 不可隐藏需外审 |
| RH-7 | C6 no-cycle | internal terminal finite descent | PASS-AUTHOR | Lyapunov 向量下降/转移源删除逻辑明确 |
| RH-8 | C9 tail | Fourier--Vaaler 高尾项无自由终端 | PASS-CONDITIONAL | 模板固定复杂度是关键假设；需外审确认适用范围 |
| RH-9 | AEX-1/2/3 | analytic exit reductions | PASS-CONDITIONAL | U2 已验收接受性链；仍需外审 controlled exits |
| RH-10 | DSO-SF | martingale square-function capacity | PASS-AUTHOR | Hilbert projection正交性本身无缺口；frame overlap 需保持固定复杂度 |
| RH-11 | EXT | KL/Vaaler/BG/Selberg/Vaughan | PASS-CONDITIONAL | U3 完成章节/论文定位；专著页码/定理号仍需 copyediting |
| RH-12 | GEE lower | final load lower bound convention | PASS-CONDITIONAL | 与 PC2/C3/C4/C5/C9 依赖一致性需外审 |
| RH-13 | GEE upper | absorbing/descent/transfer upper bound | PASS-CONDITIONAL | 阈值层级明确；所有 exits 无隐藏 positive-power loss 需外审 |
| RH-14 | GEE contradiction | lower/upper 同 convention 相矛盾 | PASS-AUTHOR | 若 RH-12/RH-13 前提成立，则矛盾推理形式正确 |
| RH-15 | LaTeX/PDF/BibTeX | 编译、引用、版式 | PASS-AUTHOR | U5 已完成，日志清零 |
| RH-16 | RH 终局 | 删除 `Submission warning` 并宣称 RH | BLOCK-REFEREE | 必须外部独立逐行接受 RH-1--RH-13 后才可升级 |

## 3. 复核结论

作者侧逐行复核完成后，合著论著可以升级为：

> Internal line-by-line audit completed; all remaining theorem-level promotions are explicitly isolated as referee obligations.

但不能升级为：

> RH 与 Prime Matrix 行列命题已经被本文无条件证明。

当前没有发现新的 `BLOCK-MATH`，但存在多个 `BLOCK-REFEREE`。这些不是文本整理问题，而是顶刊标准下必须由独立审稿接受的证明义务。
