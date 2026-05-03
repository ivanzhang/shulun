# LD-2 小壳迁移二择一释放定理

**状态：** 修正版候选引理；实验支持。

## 1. 原始 LD-2 的修正

原始设想是：若小壳签名改变并补掉旧核，则新壳差集

`S_B(y)\S_B(x)`

中必有一点逃过剩余层覆盖。

扫描显示这条命题太强：有些样本中 `S_B(y)\S_B(x)` 全部被剩余层覆盖，但完整洞集仍出现新洞。

因此正确形式应是二择一：

> 小壳迁移补洞时，要么新壳差集有逃逸点，要么原壳内部因中大层重排释放新洞。

## 2. 精确定义

固定小素数集合 `B`。令

`S_x=S_B(x)`，`S_y=S_B(y)`，`K=H_P(x)`。

若 `K` 中至少一个点被 `y` 补掉，且小壳签名改变，即

`S_x != S_y`，

定义：

`OuterEscape = (S_y\S_x) \ U_{>B}(y)`，

其中 `U_{>B}(y)` 是剩余素数层在 `S_y` 上的覆盖并集。

再定义原壳重排释放：

`InnerRelease = H_P(y) \ (S_y\S_x)`。

完整新洞为

`H_P(y)=OuterEscape union InnerRelease`。

## 3. LD-2 二择一命题

**LD-2。** 若 `1<=x,y<P`，小壳签名改变，且 `y` 补掉 `H_P(x)` 的至少一个点，则

`OuterEscape nonempty` 或 `InnerRelease nonempty`。

等价地：

`H_P(y) nonempty`。

但这里的价值在于拆分新洞来源：

- `OuterEscape` 是小壳迁移直接释放；
- `InnerRelease` 是剩余层覆盖重排释放。

## 4. 实验依据

`ld2-shell-release-escape-scan` 显示：

- 对 `B={2,3}`，扫描样本中 `OuterEscape` 已经总是非空；
- 对 `B={2,3,5}` 或 `{2,3,5,7}`，存在 `OuterEscape=empty` 的情形；
- 但这些情形中 `born_full=H_P(y)\H_P(x)` 仍非空，即 `InnerRelease` 非空。

典型样本：

- `P=37, B={2,3,5}, x=36, y=18`：壳差逃逸为空，但新洞 `[7,11,17,25]` 出现；
- `P=47, B={2,3,5,7}, x=46, y=16`：壳差逃逸为空，但新洞 `[5,9,21,35]` 出现。

## 5. 证明思路

若 `OuterEscape=empty`，说明新壳差集全部被剩余层覆盖。这会消耗剩余层容量并增加重叠压力。

同时，`y` 还要补掉旧核的一部分。剩余层必须同时完成：

1. 覆盖新壳差集；
2. 覆盖旧核中未被小素数吞掉的点；
3. 保持原壳中原本已覆盖点不释放。

这三个要求共同导致重叠能量或标签同步压力上升。若没有 `OuterEscape`，压力只能以内壳释放形式出现，即 `InnerRelease nonempty`。

## 6. 接入列缺陷流

LD-2 的释放列集合是

`H_P(y)\H_P(x)=OuterEscape union InnerRelease minus old_remaining`。

该集合给列缺陷流 `D_c` 提供正回流位置。由于释放位置由小模数壳迁移和剩余层重排共同决定，它不是任意可调的。

下一步要证明：若前窗口零行试图通过连续小壳迁移消灭洞，则这些受限释放列无法满足 CRT 周期列均衡与镜像配对的全局要求。

## 7. 下一步最小证明目标

先证明弱版：

**LD-2w。** 若小壳签名改变且补掉全部旧极小核 `K`，则 `H_P(y) nonempty`。

这已经足以说明小壳迁移不能把极小核净消为零。

再证明强版：

**LD-2s。** 新洞来源满足二择一分解，并可给出列缺陷流的受限支撑。

## 8. 相关文件

- `experiments/ld2_shell_release_escape_scan.py`
- `docs/ld2-shell-release-escape-scan.md`
- `docs/extended-field-next-obligations.md`
