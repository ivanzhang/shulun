# 多点主筛 `C=1` 候选与端点缺陷桥

**状态：** `alpha_tail_multipoint_c1_endpoint_bridge_reduction_open`

主因子账本显示样本中

\[
C_m^{\rm req}={|T_{m,r}|\over |I_m|V_{m,r}}<1.
\tag{C1B-1}
\]

因此最优下一步不是继续扩展对象，而是攻击候选不等式

\[
|T_{m,r}|\le |I_m|V_{m,r},\qquad m=4,5.
\tag{C1B-2}
\]

本文把该候选变成正式二分：若 `C=1` 不成立，则必产生一个可提交的多点端点 `PDEC` 证书。

## 1. 完整主项与端点缺陷

记

\[
H_m=|I_m|,\qquad
V_m=V_{m,r}(y,z_m).
\tag{C1B-3}
\]

定义端点缺陷

\[
E_m=|T_{m,r}|-H_mV_m.
\tag{C1B-4}
\]

则候选 `C=1` 等价于

\[
E_m\le0.
\tag{C1B-5}
\]

若 `(C1B-2)` 失败，则

\[
E_m>0.
\tag{C1B-6}
\]

这就是端点主项错配：实际多点链数量超过完整 CRT 主项预算。

## 2. 低模/尾项二分

取 cutoff `D`，把 `V_m` 的局部因子拆成

\[
V_m=V_{m,\le D}V_{m,>D}.
\tag{C1B-7}
\]

对应地，把端点缺陷写成

\[
E_m=E_{m,\le D}+E_{m,>D}.
\tag{C1B-8}
\]

若 `E_m>0`，则对任意 `0<theta<1` 至少发生一项：

\[
E_{m,\le D}\ge \theta E_m,
\tag{C1B-9}
\]

或

\[
E_{m,>D}\ge (1-\theta)E_m.
\tag{C1B-10}
\]

第一项是有限低模相位偏置，进入 `PDEC`；第二项是高尾/奇异因子错配，进入 `ColumnCRT/Rankin/SAE`。

## 3. `C=1` 失败证书

一个 `Multipoint-C1-Fail-Cert` 必须给出：

```text
p, B, r, m;
I_m and H_m;
y, z_m;
V_m;
actual |T_m|;
positive defect E_m=|T_m|-H_m V_m;
cutoff D and split E_{<=D}, E_{>D};
PDEC/ColumnCRT/SAE route key.
```

因此，若不能证明 `C=1`，失败本身就是结构化异常，不会回到无结构共振。

## 4. 接入共振预算

若 `C=1` 对 `m=4,5` 成立，则多点共振压力满足

\[
|\mathcal P_{\rm res}(u;r)|
\le
2C_u(H_4V_4+H_5V_5),
\tag{C1B-11}
\]

再与正式反例阈值比较即可。若 `(C1B-11)` 仍不足以压住反例，则剩余硬点不是多点链计数，而是
投影常数 `C_u` 或反例压力抽取阈值的归一化。

## 5. 审计样本

审计脚本：

```text
experiments/prime_matrix_alpha_tail_multipoint_c1_bridge_audit.py
```

样本：

| p | block | shift | m | count | HV | defect | C_req | C1 ok |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 997 | 4096 | -36 | 4 | 189 | 1312.796894 | -1123.796894 | 0.143967 | True |
| 997 | 4096 | -36 | 5 | 101 | 985.094774 | -884.094774 | 0.102528 | True |
| 5003 | 8192 | -36 | 4 | 1209 | 4576.405896 | -3367.405896 | 0.264181 | True |
| 5003 | 8192 | -36 | 5 | 916 | 3951.765916 | -3035.765916 | 0.231795 | True |
| 10007 | 16384 | -900 | 4 | 2860 | 8068.084595 | -5208.084595 | 0.354483 | True |
| 10007 | 16384 | -900 | 5 | 2302 | 6604.719933 | -4302.719933 | 0.348539 | True |

样本中 `defect<0`，说明 `C=1` 有明显余量；正式证明仍需逐行证明或将正缺陷路由到证书出口。

## 6. 审稿边界

已证明：

```text
C=1 failure
=> positive multipoint endpoint defect
=> low-mod PDEC or high-tail/ColumnCRT/SAE split.
```

尚未证明：

```text
E_m<=0 对所有正式参数成立；
或 E_m>0 的两个出口全部可排斥。
```

下一步最小硬点是为 `E_m<=0` 构造正式低模/高尾不等式，或生成可机器核验的 `PDEC` 证书模板。
