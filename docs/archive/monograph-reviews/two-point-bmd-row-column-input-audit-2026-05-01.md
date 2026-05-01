# BMD 行列输入审查记录（2026-05-01）

## 结论

本轮审查确认：前文方阵行列素数命题即使作为条件输入，也不能直接推出 BMD。

它能提供的有效刚性是：

- 排除完整 CRT 局部块中的整行空洞；
- 排除完整 CRT 局部块中的非零列空洞；
- 排除由小因子同步造成的零截面退化；
- 将这些退化统一并入 BMD-Zero。

但 BMD 要求的是双素变量在乘法曲线 `pm≡2 mod d` 上的 Rosser/Buchstab 加权分布。该分布等价于控制非主乘法角色的 bilinear dispersion。

## 精确分解

令 `J_p={m>Y:pm in I}`。则

在剥离确定的模 `2` 后，对奇平方自由 `d` 有

`R_d=sum_{Y<p<=P, p prime} Delta_d(2p^{-1};J_p)`,

其中

`Delta_d(a;J)=pi(J;d,a)-phi(d)^{-1}pi(J;d,*)`。

角色展开给出剩余核心：

`sum_{d<=D} |lambda_d|/phi(d) sum_{chi!=chi0} |sum_p chi(p) S_p(chi)| = o(|U_Y|)`,

其中

`S_p(chi)=sum_{m in J_p, m prime} chi(m)`。

## 审稿状态

- `RC-Prime`：在当前合著稿中仍应作为条件输入或待独立审稿输入。
- `BMD-Zero`：可由 `RC-Prime` 条件支持，负责排除极端几何孔洞。
- `BMD-Char`：仍未证明，是当前最小真实硬点。

## 下一步

下一轮应直接专攻 `BMD-Char`：用大筛、Vaughan/Type-II 或双素变量 dispersion 方法证明上述角色和相对 `|U_Y|` 为小量。行列输入只作为剥离零截面的辅助刚性，不再作为替代分布估计使用。
