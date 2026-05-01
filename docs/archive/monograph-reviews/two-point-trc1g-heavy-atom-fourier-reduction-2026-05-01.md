# 二次筛 TRC-1G-H 重原子攻坚归档

日期：2026-05-01

## 审查结论

本轮没有把 TRC-1G-H 宣称为无条件闭合，而是把它压缩成一个更精确、可审查的剩余命题。

## 已严格完成的链条

设 `U_Y(I)` 为真实二次筛剩余集，新素数 `p>Y` 的坏类质量为

\[
\lambda_p=\frac{\#\{x\in U_Y(I):x\equiv0,w\pmod p\}}{|U_Y(I)|}.
\]

已在主文档第 376--381 节补入如下严格链：

1. 若 `\lambda_p>0.4`，则 `U_Y(I)` 在 `mod p` 上存在非零 Fourier 系数 `>1/5`。
2. 该 Fourier 缺陷等价于 `0,\pm w mod p` 三差值族的常数级能量超标。
3. 方阵旧刚性可剥离短方向、45度锁、Reuse/Shared 与端点层。
4. 剥离后唯一剩余为长方向新模均衡 LDB(p)/NMFB。

## 当前最小剩余

需要证明：

\[
\sum_{\delta\in\{0,w,-w\}}
\sum_k C_U(kp+\delta)
\le \varepsilon_p |U_Y(I)|^2,\qquad \varepsilon_p<0.16,
\]

其中短方向、45度锁、Reuse/Shared 和端点异常已经从求和中剥离。

等价 Fourier 形式为：

\[
\max_{a\ne0}
\left|
\frac1{|U_Y(I)|}
\sum_{x\in U_Y(I)}e^{2\pi iax/p}
\right|
\le \frac15-o(1).
\]

## 审稿边界

LDB(p)/NMFB 尚未无条件证明。此前压力模型 `U^*` 说明，旧局部 CRT 条件、短窗不可复用和固定阶局部复杂度不能单独推出新模长方向均衡。因此当前二次筛命题仍保持条件状态。
