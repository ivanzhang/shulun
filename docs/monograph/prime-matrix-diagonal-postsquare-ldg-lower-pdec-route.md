# 对角平方后端点 LDG-Lower 的 PDEC 路线

**状态：** `ldg_lower_reduced_to_lowmod_skeleton_discrepancy_or_pdec`

本文专攻维数差合同中的第一个输入：

```text
LDG-Lower: G(P) >= 0.48 P/log P。
```

这里

\[
G(P)=\#\{1\le k<P:\ P^-(P^2+k)>y\},
\qquad y=\max(2,\lfloor P/e\rfloor).
\tag{LDG-1}
\]

## 1. 完整周期主项

低模筛的完整 CRT 密度为

\[
V(y)=\prod_{r\le y}\left(1-{1\over r}\right).
\tag{LDG-2}
\]

Mertens 主项给出

\[
V(y)\sim {e^{-\gamma}\over\log y},
\]

所以自然尺度是

\[
P V(y)\approx e^{-\gamma}{P\over\log P}.
\tag{LDG-3}
\]

候选常数 `0.48` 低于 `e^{-gamma}=0.561...`，允许大约 `14%` 的短区间相位亏损。

## 2. 审计读数

数据来自：

```text
docs/diagonal_postsquare_primepair_excess_audit_p100000_20260505.json
```

并用 `(LDG-2)` 计算完整周期主项。关键读数：

```text
min G(P) log(P)/P = 0.4879618800870573 at P=37。
```

阈值后的最坏 `G/(P V(y))`：

```text
P>=23:    0.7045326576576575 at P=37；
P>=101:   0.7756446711556736 at P=337；
P>=501:   0.8155743623940284 at P=523；
P>=1009:  0.8722793046172782 at P=1913；
P>=2003:  0.8837565403641735 at P=4637；
P>=5003:  0.8947256727592108 at P=5939；
P>=10007: 0.9007876726186265 at P=10657；
P>=50021: 0.9216214236089851 at P=83561。
```

这说明低筛骨架亏损随 `P` 增大快速变薄；`0.48P/logP` 的真正压力来自小范围有限带。

该小范围已由有限证书剥离：

```text
docs/diagonal_postsquare_lowband_finite_certificate_p2003_20260505.md
```

其中 `P<=2003` 的所有奇素数直接通过端点素数检查；`P>=23` 的维数差检查也全部通过。
因此 `LDG-Lower` 的解析义务可以集中在 `P>=2003`。

## 3. PDEC 化的亏损形式

令

\[
S_P(k)=\prod_{r\le y}1_{k\not\equiv -P^2\pmod r}.
\tag{LDG-4}
\]

则

\[
G(P)=\sum_{1\le k<P}S_P(k).
\tag{LDG-5}
\]

若 `LDG-Lower` 失败，则

\[
\sum_{1\le k<P}(S_P(k)-V(y))
\le
-\left(PV(y)-0.48{P\over\log P}\right).
\tag{LDG-6}
\]

右侧是固定端点相位 `-P^2 mod r` 的低模骨架负偏差。它不是尾素数问题，而是低模 CRT 覆盖过量问题。因此应路由为：

```text
LowSkeletonDeficit:
低模禁类在长度 P 的固定端点窗口中过度覆盖。

Persistent LowSkeletonDeficit:
若同类亏损在无限坏族中持续，抽取非零 Fourier/PDEC 证书。

Sparse LowSkeletonDeficit:
若只在孤立小范围出现，进入有限 SAE/直接证书。
```

## 4. 当前验收接口

`LDG-Lower` 的闭合可以走两条路：

```text
LDG-Uniform:
直接证明所有 P>=23 满足 G(P)>=0.48P/logP。

LDG-PDEC:
证明任何违反该下界的相位亏损都会给出 PDEC/SAE 证书，并由既有出口排斥。
```

本文没有给出无条件证明；它把低筛骨架下界从“希望有足够剩余点”改写为一个固定低模相位亏损命题。与 `RFP-Upper` 配合后，平方后端点只剩这两个显式常数接口。
