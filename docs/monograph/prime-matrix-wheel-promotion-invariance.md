# 轮提升不变性

**状态：** `proved_structural_identity`

本文记录平方前后端点的一个结构性恒等式：把某个小素数从“高素斜线覆盖层”提升进轮底座，不改变最终幸存偏移集合，只改变证明账本的分层。

## 1. 设置

固定平方端点窗口

```text
plus:  n=P^2+k, 1<=k<P；
minus: n=P^2-k, 1<=k<P。
```

令 `W` 为不含 `P` 的平方自由轮模数，定义轮骨架

\[
S_W^\pm(P)=\{k: P^2\pm k\text{ 与 }W\text{ 互素}\}.
\]

令高素覆盖层为

\[
C_q^\pm(P)=\{k: q\mid P^2\pm k\},
\qquad q<P,\ q\nmid W.
\]

相对于轮 `W` 的最终幸存集合是

\[
R_W^\pm(P)
=
S_W^\pm(P)\setminus\bigcup_{\substack{q<P\\q\nmid W}}C_q^\pm(P).
\tag{WPI-1}
\]

## 2. 轮提升引理

若 `s<P` 是素数且 `s∤W`，令 `W'=Ws`。则

\[
R_W^\pm(P)=R_{W'}^\pm(P).
\tag{WPI-2}
\]

证明很短：

\[
S_{W'}^\pm(P)=S_W^\pm(P)\setminus C_s^\pm(P).
\tag{WPI-3}
\]

而 `W'` 的高素覆盖层正好是 `W` 的高素覆盖层去掉 `q=s`：

\[
\{q<P:q\nmid W'\}=\{q<P:q\nmid W\}\setminus\{s\}.
\tag{WPI-4}
\]

代入 `(WPI-1)` 即得

\[
S_W^\pm\setminus
\left(C_s^\pm\cup\bigcup_{q\nmid W'}C_q^\pm\right)
=
(S_W^\pm\setminus C_s^\pm)\setminus
\bigcup_{q\nmid W'}C_q^\pm
=R_{W'}^\pm.
\]

这就是轮提升不变性。

## 3. 结构意义

该恒等式说明：

```text
轮筛不是概率近似；
它是把若干小素斜线从覆盖层移入底座层的严格重分层。
```

因此可以自由选择 `W=6,30,210,2310,...` 来暴露不同层面的刚性，而不用担心改变最终端点幸存集合。

它也说明单纯扩大轮模数不能自动证明行命题：最终幸存集合不变。真正需要证明的是：

```text
在任意提升后的轮骨架上，剩余高素斜线不能完成全覆盖；
若能完成，则覆盖证书必须产生 PDEC/SAE/ColumnCRT 缺陷。
```

## 4. 审计确认

审计脚本：

```text
experiments/prime_matrix_square_row_wheel_setcover_capacity_audit.py
```

报告：

```text
docs/square_row_wheel_setcover_capacity_audit_w6_2310_20260506.md
```

在 `P=10007,36739,95093,99991` 与 `W=6,30,210,2310` 上，`plus/minus` 两侧最终未覆盖数完全不随 `W` 改变。

示例：

| P | side | W=6 | W=30 | W=210 | W=2310 |
|---:|---|---:|---:|---:|---:|
| 10007 | minus | 566 | 566 | 566 | 566 |
| 10007 | plus | 530 | 530 | 530 | 530 |
| 36739 | minus | 1755 | 1755 | 1755 | 1755 |
| 36739 | plus | 1696 | 1696 | 1696 | 1696 |
| 95093 | minus | 4146 | 4146 | 4146 | 4146 |
| 95093 | plus | 4142 | 4142 | 4142 | 4142 |
| 99991 | minus | 4338 | 4338 | 4338 | 4338 |
| 99991 | plus | 4368 | 4368 | 4368 | 4368 |

同时，底座骨架随 `W` 增大而变小。例如 `P=36739, plus`：

```text
W=6:    skeleton=12246, covered=10550, uncovered=1696；
W=30:   skeleton=9797,  covered=8101,  uncovered=1696；
W=210:  skeleton=8398,  covered=6702,  uncovered=1696；
W=2310: skeleton=7636,  covered=5940,  uncovered=1696。
```

这正是 `(WPI-2)` 的机器复核。

## 5. 当前证明策略影响

轮提升不变性把“选择哪个小模连乘”从猜测变成了策略选择：

- 小 `W`：底座大，高素覆盖层多；
- 大 `W`：底座小，高素覆盖层少；
- 最终幸存集合不变。

因此最优证明路线是选择能最大化结构刚性的 `W`，例如 `210` 或 `2310`，再证明剩余高素斜线在
`U_W±P^2` 平移骨架上不能全覆盖。

当前最小接口应写为：

```text
Promoted Wheel Set Cover:
  对一个方便的 W，证明 R_W^\pm(P) 非空；
  若 R_W^\pm(P)=empty，则覆盖证书在该 W 的 CRT 骨架中产生
  PDEC/SAE/ColumnCRT 缺陷。
```

这一步把小模连乘同余的作用精确化了：它不是最终证明本身，而是通向缺陷证书的结构坐标系。

后续容量分解见：

```text
docs/monograph/prime-matrix-promoted-wheel-setcover-capacity.md
```
