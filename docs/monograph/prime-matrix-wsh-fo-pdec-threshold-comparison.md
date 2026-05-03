# FO-PDEC 显式阈值比较攻坚稿

**状态：** `explicit_pdec_lower_threshold_computed_ucrt_open`

本文继续硬攻 `FO-PDEC` 的最后阈值层。本轮完成的是同一坏窗方程集合上的显式
Fourier 下界；尚未完成的是同一投影的 `U_CRT` 上界。

## 1. 显式投影下界

对解释因子 `ell`，令

\[
  g_\ell(\rho)=\#\{n=b+d:\ell\mid n,\ r(n)\equiv\rho\pmod\ell\}.
\]

定义非零 Fourier 阈值

\[
  M_\ell(E)=
  \max_{1\le h<\ell}
  \left|
  \sum_{\rho\bmod\ell}g_\ell(\rho)e^{2\pi i h\rho/\ell}
  \right|.
\]

这是 `PDEC` 证书模板中的显式下界对象：若能证明同一 `g_ell` 满足

\[
  U_{\rm CRT,\ell}<M_\ell(E),
\]

则该 `ell` 投影排斥当前 persistent 分支。

## 2. 有限阈值账本

新增脚本：

```text
experiments/prime_matrix_wsh_fo_pdec_threshold_ledger.py
```

输出：

```text
docs/monograph/prime-matrix-wsh-fo-pdec-threshold-ledger.md
docs/monograph/prime-matrix-wsh-fo-pdec-threshold-ledger.json
```

当前低模方程账本给出：

```text
global equation count = 43
global best factor = 199
best frequency = 95
max Fourier threshold = 3.959247567099438
support PDEC lower bound = 0.16288018964317724
top residue loads = [(40,2),(126,1),(61,1)]
```

这说明全局最佳 `ell=199` 投影已经产生接近 `4` 的非零 Fourier 信号。若能在同一坏窗集合上
证明

\[
  U_{\rm CRT,199}<3.959247567099438,
\]

则该有限投影闭合。

## 3. 证明级下界与数值阈值的关系

支撑型 Cauchy 下界只给出

\[
  L_{\rm support}
  =
  t_\ell
  \sqrt{\frac{\ell-s_\ell}{\ell(\ell-1)s_\ell}},
\]

在 `ell=199,t=4,s=3` 时为 `0.162880...`，远弱于实际 Fourier 下界 `3.959...`。
因此后续闭合不应只依赖支撑型软界，而应使用显式投影或解析同余结构给出强下界。

## 4. 剩余上界义务

当前唯一剩余为：

```text
FO-PDEC-UCRT:
For the same projected bad-window vector g_199,
prove max_{h!=0} |hat g_199(h)| <= U_CRT,199
from independent CRT constraints,
with U_CRT,199 < 3.959247567099438.
```

可用约束来源只能来自已有审稿合法行：

1. `mass/nonnegative`；
2. `mirror pair cap`，若同一坏窗集合有镜像闭合或成对容量；
3. `column cap`，若列见证在同一投影上有效；
4. `tail non-reuse`，若同一解释因子重复会触发 Tail-anchor；
5. `SAE/Endpoint`，若非持久相位被稀疏端点吸收。

不能使用完整 CRT 周期均衡替代坏窗子集均衡。

## 5. 当前结论

本轮把 `FO-PDEC` 的最后缺口压缩为一个具体数值目标：

```text
prove U_CRT,199 < 3.959247567099438
for the same projected bad-window set.
```

在该上界完成前，不能宣称全局无条件闭合。下一步应直接为 `ell=199,h=95` 构造
`PDEC-Dual-Cert` 或证明该投影进入 `SAE/Endpoint`。
