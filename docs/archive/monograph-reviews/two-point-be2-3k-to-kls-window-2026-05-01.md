# BE2-3K 细化硬攻：压缩到 KLS-window（2026-05-01）

## 本轮结论

`BE2-3K` 继续缩小为 `KLS-window`。

逻辑链：

`KLS-window => BE2-3K => BE2-3 => WBE2 => BMD`。

## 已排除路线

点态 Weil 界不足。

对单个不完整倒数和

`B_d(A)=sum_{s~S} beta_s e(A s^{-1}/d)`

完成后只有

`B_d(A) << tau(d)(S/d+1)d^{1/2}log d`。

在 `S~P`, `d~P/log^B P` 时只是单模平方根抵消，不能在 `d1,d2,h` 总平均中给任意 `log^{-A}`。

## 已控制部分

`(d1,d2)>1` 的 gcd 层不是真正硬点。公共因子 `g` 强制 `s1=s2 mod g`，给出约 `1/g` 稀疏因子；总和只产生多对数损失。

## 必须使用的结构

Rosser/Buchstab 权重的 well-factorable 分解是关键。它允许把模数拆为 Kloosterman 模数部分与外层平滑平均部分，是普通大筛无法替代的结构。

## 最后核心

`KLS-window`：窗口化 Kloosterman 谱大筛。

若引用 Kuznetsov/Deshouillers--Iwaniec 型谱大筛，该输入可作为外部深定理闭合；若坚持完全自足，则下一步必须证明 `KLS-window`。
