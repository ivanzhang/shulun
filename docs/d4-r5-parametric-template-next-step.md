# D4/R5 参数化相位模板枚举：下一步严格任务

## 已完成

- 完整危险窗口 `[1088200,1088600)` 的逐行枚举已完成。
- 当前有限证书候选全集已完成左右半单元外向舍入闭合。
- 多窗口压缩模板探针已完成：五个代表窗口、每个 400 行，共得到 11 个压缩见证模板。

## 新证书

- `docs/d4-r5-multwindow-template-probe-w400.json`
- `docs/d4-r5-compressed-witness-template-library.json`

## 真正剩余任务

必须把经验压缩模板升级为精确符号模板：

```text
T = (floor data, offset groups, layer labels, constraint branch)
```

并证明：任何满足 R5global1--R5global4 约束的相位单元都属于有限模板族 `T_R5`。

随后对 `T_R5` 的每个模板运行已经完成的外向舍入固定成员管线。

## 当前不能声称

多窗口模板探针不是覆盖证明。它只说明最坏见证形态高度集中，帮助设计有限模板族。
