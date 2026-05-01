# 合著论著审稿级闭合审查

本文对 `paper/contradiction-field-monograph/contradiction-field-monograph.tex` 做审稿级逻辑链检查。目标不是把尚未外部验证的命题强行改成已证，而是把每条逻辑链的闭合状态严格标明。

## 1. 闭合判据

一条 contradiction-field 证明链只有在以下四项全部满足时才可称为闭合：

1. **入口闭合**：反例能无损进入结构化场；无未命名例外。
2. **分解闭合**：所有局部解释被不重不漏地分到命名层。
3. **出口闭合**：每个命名出口要么吸收、要么严格下降、要么源删除转移、要么被外部定理排斥。
4. **全局闭合**：下界与上界在同一 load convention 下相矛盾，且没有循环或容量重复计数。

## 2. Prime Matrix 链条审查

| 环节 | 当前状态 | 缺口性质 | 闭合结论 |
|---|---|---|---|
| 行/列反例入口 | A/B 附录已给三层剥离 | 符号与分层需 referee 核验 | 条件闭合 |
| 小因子锁定 | CRT 非零类均衡已写入 A/B | 无明显工程缺口 | 可审查闭合 |
| 尾部锚剥离 | Tail-log4 作为输入 | 外部 BG/RKS 与常数需核对 | 条件闭合 |
| Structured-EHPD | D 组附录与审查包存在 | D 组排斥仍需逐行复核 | 未最终闭合 |
| 有限验证 | 证书存在 | 只覆盖阈值以下 | 条件闭合 |
| 行/列最终定理 | 依赖 D + finite | D 未独立接受前不能升级 | 未最终闭合 |

结论：Prime Matrix 部分当前是“归约链 + 条件排斥包”，不是无条件终稿。

## 3. RH 链条审查

| 环节 | 当前状态 | 缺口性质 | 闭合结论 |
|---|---|---|---|
| PC1 离线零点到素数异常 | 主稿编号化，外部 LI 固定 | 需 referee 核验引用适配 | 条件闭合 |
| PC2 CRT baseline | 主稿编号化 | 需 referee 核验误差项 | 条件闭合 |
| C3/C4/C5 分解 | 主稿编号化 | 需逐行核验路由不重不漏 | 条件闭合 |
| C6/C9 no-cycle/tail | 主稿编号化，latexmk 通过 | 需逐行核验势函数与尾项吸收 | 条件闭合 |
| AEX/GEE | U1--U5 作者侧完成 | controlled exits 需独立接受 | 条件闭合 |
| EXT | 章节/论文级定位完成 | 专著页码 copyediting | 工程剩余 |
| RH 终局定理 | 保留 Submission warning | 不能由作者自称 referee verification | 未最终闭合 |

结论：RH 部分是“verification manuscript with warning”，不是最终无条件证明稿。

## 4. 合著论著闭合状态

合著论著可以严格闭合为如下命题：

> Prime Matrix 与 RH 两个研究程序共享同一个 contradiction-field 骨架；所有当前已完成的归约、分解、出口、编译、引用和状态边界均已被集中记录；尚未外部接受的命题被显式标记为条件输入或 referee obligation。

合著论著不能诚实闭合为如下命题：

> 本书已经无条件证明 RH 与方阵行列素数命题。

## 5. 下一步真正闭合路径

1. 对 Prime Matrix：逐行审查 D-structure exclusion、Tail-log4、M5 gap、常数吸收与有限验证阈值接口。
2. 对 RH：组织外部 referee package，逐条审查 PC1/PC2/C3/C4/C5/C6/C9/AEX/GEE/EXT。
3. 对合著书稿：把每个条件输入变成独立 appendix theorem 或明确外部 theorem；所有未接受项继续保留 warning。
