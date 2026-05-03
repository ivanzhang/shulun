# D4/R5 RPL 局部闭合草案

## RPL-stable-capacity

恒等式：

```text
D(S∪A)-D(S) = d(A) - L(S)L(A)/10
```

其中 `d(A)=E(A)-L(A)^2/20`。

局部证据显示 stable 步中所有 `d(A)>=0`，所有负的 `D` 下降均由容量支付项 `L(S)L(A)/10` 覆盖。

证书：`docs/d4-r5-capacity-payment-audit.json`

## RPL-jump-absorb

唯一 jump 步 `1088588:160->200` 的所有坏度指标均为 0，故跳变不传递坏结构。

证书：`docs/d4-r5-jump-absorption-audit.json`

## RPL-backflow

在当前局部探针中，没有出现“无容量支付、无 jump、仍有坏度”的步，因此 backflow 分支为空触发。

全局证明中仍需证明：若该分支出现，则去掉新壳层后坏度损失可控。

## 局部结论

对当前 R5 危险窗口的递归壳层探针，三择传递闭合：

```text
stable => capacity payment
jump => no badness propagation
backflow => not triggered
```

这不是全局 RPL 证明，但给出正确的局部传递模型。
