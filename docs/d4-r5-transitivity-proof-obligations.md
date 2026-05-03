# D4/R5 层叠剥离递归：待证核心不等式

## 已验证方向

`docs/d4-r5-recursive-transitivity-classification.json` 显示：

- stable steps: 23
- jump steps: 1
- stable bad: 0

所有 stable 步的新壳层缺陷 `ΔE²-(ΔL)²/20` 非负。

## 待证不等式 1：stable 交叉项控制

对旧层 `S` 与新壳层 `A`：

```text
D(S∪A)-D(S)
= [E(A)-L(A)^2/20] + Cross(S,A)
```

其中

```text
Cross(S,A) = - L(S)L(A)/10
```

若直接使用总质量会为负，因此必须利用层正交/偏移互斥/同余独立性，证明有效交叉项被削弱：

```text
Cross_eff(S,A) >= -theta_j [E(A)-L(A)^2/20] - err_j
```

目标：`theta_j<1` 且 `sum err_j` 可控。

## 待证不等式 2：jump 吸收

若层分类跳变，必须跨越阈值边界：

- `tau_sum=60`
- `count=20` 或 `25`
- `U=0.16`
- `L=0.35`

目标证明：跳变集合要么低维且稀疏，要么坏度下降：

```text
B_after <= B_before - kappa_j
```

或落入有限危险窗口证书族。

## 待证不等式 3：回传可传递性

若没有 stable 耗散也没有 jump 吸收，则坏结构必须投影回旧尺度：

```text
Bad(X_j) => Bad(X_{j-1}) with loss <= eps_j
```

目标：`sum eps_j` 被初始局部证书余量吸收。

## 结论

真正全局闭合现在压缩为三个递归不等式，而不是无限模板枚举。
