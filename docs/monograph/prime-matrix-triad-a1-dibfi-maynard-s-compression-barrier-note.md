# Triad-A1 Maynard S-compression barrier 记录

**状态：** `maynard_s_compression_barrier_identified`

本记录指出一个必须避开的错误翻译：共同变量表中的逆元窗口 `S` 不能直接等同于 Maynard-W4
指数锥中的 `S_May`。这不是数值实验，而是由指数锥本身推出的结构性阻断。

## 1. 已知尺度

当前非 AP-source scale ledger 已固定：

```text
X≈P^2；
Q<=P log^O P，因此 x_Q=1/2+o(1)；
共同变量表/KE-13 的逆元窗口 S_common≈P，因此 x_S_common=1/2+o(1)。
```

Maynard 指数锥为：

```text
n+m=1；
2n+2r+s <= 1-eta；
n+2r+5s+q <= 2-eta；
2n+3r+4s+q <= 2-eta。
```

其中 `q` 是 `Q_May=x^q` 的指数，`s` 是 `S_May=x^s` 的指数。

## 2. 锥内强制 S 上界

由于 `n,r>=0`，第二条非对角条件立即给出：

```text
5s+q <= 2-eta。
```

所以

```text
s <= (2-q)/5 - eta/5。
```

若沿用当前 level `Q≈P=X^(1/2)`，即 `q=1/2+o(1)`，则：

```text
s <= 3/10 - eta/5 + o(1)。
```

## 3. 直接同一化矛盾

若把共同变量表的逆元窗口直接设为 Maynard 的 `S_May`，则：

```text
S_May = S_common≈P=X^(1/2)，即 s=1/2+o(1)。
```

这与 `s<=3/10-o(1)` 矛盾。更强地说，即使取 `q>=0`，也有 `s<=2/5-o(1)`，
仍然不能容纳 `s=1/2`。

因此：

```text
S_common != S_May
```

在当前证明链中不是记号偏好，而是指数锥的强制结论。

## 4. 当前剩余被进一步定位

`CurrentWFDMaynardTranslationMatrixFeasibleWithSlack` 不能通过朴素变量同名关闭。必须证明下列二选一：

```text
MaynardSCompressionMap:
  从当前 WFD 的 s1,s2/h/completion 结构中抽出一个真实 S_May，
  满足 S_May <= X^(3/10-o(1))；

或

AlternateW4ObjectRerouting:
  证明当前 WFD 非对角对象并不走这个 Maynard-W4 指数锥接口，
  而是进入另一个已登记且可闭合的外部 dispersion 原子。
```

这一步把最窄剩余从“找变量表”推进到“证明压缩的 Maynard-S 不是共同逆元窗口 S”。
