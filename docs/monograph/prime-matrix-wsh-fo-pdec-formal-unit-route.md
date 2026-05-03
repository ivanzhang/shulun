# FO-PDEC Formal Unit 拼接路线

**状态：** `formal_unit_stitching_required_before_global_closure`

本文继续硬攻 `FO-PDEC` 的最后缺口。新的审计表明，当前 `ell=199` 的强阈值不是普通
`U_CRT` 上界差一点的问题，而是更上游的 formal unit 一致性问题：`PDEC` 证书必须作用于
同一个正式坏窗集合或多重集合。

## 1. Formal unit 一致性引理

**引理 FU-1（同一坏窗集合原则）。**  
在 `PDEC-Cert` 中，相位向量

\[
  g(t)=\#\{x\in S:\tau(x)=t\}
\]

只能由一个已经从正式反例链抽取出的坏窗集合或多重集合 `S` 生成。若两批事件没有共同的
索引域 `S` 与同一个相位映射 `tau`，则它们的 Fourier 质量不能相加作为同一个
`PDEC` 下界。

**证明。**  
`PDEC` 下界与上界都以同一函数 `g` 为对象。下界使用

\[
  \widehat g(h)=\sum_t g(t)e^{2\pi iht/Q},
\]

上界约束则写成 `Ag<=b, Eg=e`。若把来自不同 `S` 或不同 `tau` 的事件相加，就没有单个
`g` 同时满足两侧定义；此时下界与上界作用于不同对象，证书非法。证毕。

## 2. 当前最佳投影的真实结构

新增审计：

```text
experiments/prime_matrix_wsh_fo_pdec_formal_unit_audit.py
docs/monograph/prime-matrix-wsh-fo-pdec-formal-unit-audit.md/json
```

结果显示：

```text
global_library_raw:  mass=4, Fourier=3.959247567099438
global_layer_dedup:  mass=3, Fourier=2.9698366905785227
global_physical:     mass=2, Fourier=1.9997507790353146
q_row_raw:           best mass=2, Fourier=2.0, support=1
q_row_coordinate:    best mass=1, Fourier=1.0
block_local:         best mass=1, Fourier=1.0
offset_row:          best mass=1, Fourier=1.0
```

因此强阈值 `3.959...` 的来源不是单个固定偏移行、单个 Hall 块、或去重后的单个矩阵行；
它来自有限证书库中的跨层聚合。

## 3. 两类重复的证明义务

最佳因子 `ell=199` 的四个事件分成两类：

1. **嵌套同坐标重复。**  
   `candidate=1664237` 在 `q=1993,row=836,column=82,offset=30` 处由 block `1`
   与 block `4` 重复出现，目标残基同为 `40`。这是同一正式坐标重复。若要计两次，
   必须证明两个嵌套 Hall 块在对偶证书中给出两条独立约束行；否则只能计一次。

2. **跨层同整数重复。**  
   `candidate=250541` 同时出现在 `q=773,row=325` 与 `q=967,row=260`，目标残基分别为
   `126` 与 `61`。这是同一整数在不同方阵宽度下的两种表示。若要合并，必须证明二者属于
   同一个持久坏窗族，并给出统一相位映射；否则不能放入同一个 `PDEC` 向量。

## 4. 可闭合路线二分

现在 `FO-PDEC` 的真实剩余被压成以下二分：

```text
Route A: FormalUnit-Stitching + NestedBlock-Independence
         => 强阈值 3.959... 可进入 PDEC-Dual-Cert；

Route B: 无法拼接或独立化
         => 重复项进入 SAE/Endpoint，强阈值降为单元级或 primitive 级，
            必须另给 U_CRT 上界或改攻 SAE 排斥。
```

这不是转换命题，而是修正 `PDEC` 的对象口径。若跳过这一步，后续即使写出
`U_CRT<3.959...`，也可能不是同一坏窗集合上的不等式。

## 5. 下一步最小硬点

优先攻 `NestedBlock-Independence`，因为它只涉及同一 `q`、同一行、同一正式坐标的嵌套
Hall 块。可证目标应写成：

```text
若同一正式坐标在两个嵌套 Hall 块中重复出现，
则要么两个块在对偶 Hall 证书中有不同独立约束权重，
要么该重复属于 endpoint/SAE 非持久逃逸。
```

若该目标失败，则 `q_row_raw` 的 `mass=2,support=1` 不能提供严格节省，必须退回
`SAE/Endpoint` 或寻找新的正式坏窗族。

## 6. 诚实结论

当前没有达到全局无条件闭合。已完成的是把 `FO-PDEC` 最后缺口从模糊的
`U_CRT` 上界问题进一步压缩为：

```text
FormalUnit-Stitching / NestedBlock-Independence / SAE-Endpoint absorption
```

三者之一必须严格闭合，才能继续使用强阈值并推进全局证明。
