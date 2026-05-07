# Triad-A1 DI/BFI full-S dispersion atom 说明

本文固定最新最窄尺度硬点：

```text
FullSOriginalDIBFIAtom:
  prove/cite an original DI/BFI dispersion atom in the current full-S window.
```

## 1. 对象窗口

当前 non-AP generic WFD 路线的共同变量表给出：

```text
X≈P^2;
S_common≈P=X^(1/2+o(1));
z=s1*s2≈X.
```

因此该硬点不是短区间宽度问题，而是 full-S dyadic 块本身的问题。若保持当前块，
Maynard-W4 的 `S_May` 必被 `z=s1*s2` 推到 `X^(1/2+o(1))`。

## 2. 已排除退路

Maynard-W4 指数锥在 `q=1/2+o(1)` 时强制：

```text
S_May <= X^(3/10-o(1));
Z <= X^(3/5-o(1)).
```

所以 full-S 对象不能由 Maynard-W4 直接承接。短 S 子窗口也不能解决：在
`s≈X^(1/2)` 内切小宽度区间不会改变 `s` 的实际量级；真正选择
`s<=X^(3/10)` 又离开了当前 full-S dyadic 块。

## 3. 可接受闭合输入

可接受输入只能是以下两类之一：

```text
ExternalFullSDIBFIAtomMatch:
  BFI/DI 原始 dispersion 定理或等价外部 deep theorem；
  明确覆盖 S_common≈X^(1/2)、z≈X；
  明确不会向当前对象插入隐藏中心化、投影或 dyadic 主块遗漏。

UncenteredWFDToKE13NoProjectionIdentity:
  从当前 non-AP WFD 原始对象逐项推出 KE-13/WFD-core；
  不借助 AP-source 身份；
  不删同块对角，不插块中心化，不投影到更弱对象。
```

## 4. 当前结论

`NewFullSDispersionAtom` 现在应改写为：

```text
ExternalFullSDIBFIAtomMatch
```

它仍未闭合。当前推进意义是：full-S 缺口不再是笼统“新原子”，而是一个可逐项审计的
外部原始 DI/BFI 定理合同。
