# AlphaTail：坏高标签上界与素数下界边界

**状态：** `alpha_tail_bad_upper_prime_lower_boundary`

前文已证明

\[
H_\alpha(p)-C_\alpha(p)=P_\alpha(p)-B_\alpha^{bad}(p)
\tag{BPL-1}
\]

对 `alpha=0.9` 成立。本文继续压缩 `BadHigh`，并明确剩余边界。

## 1. 坏高标签的粗上界

对 `alpha>1/\sqrt2`，高标签唯一，因此

\[
B_\alpha^{bad}(p)\le C_\alpha(p).
\tag{BPL-2}
\]

又每个高标签 `q in (alpha p,p)` 最多命中两列，所以

\[
B_\alpha^{bad}(p)
\le
2\bigl(\pi(p-1)-\pi(\lfloor\alpha p\rfloor)\bigr).
\tag{BPL-3}
\]

若有显式素数计数上界

\[
\pi(p-1)-\pi(\lfloor\alpha p\rfloor)
\le C_\pi(1-\alpha){p\over\log p},
\tag{BPL-4}
\]

则

\[
B_\alpha^{bad}(p)
\le
2C_\pi(1-\alpha){p\over\log p}.
\tag{BPL-5}
\]

## 2. 条件闭合常数

若同时有对角短区间素数下界

\[
P_\alpha(p)=\pi(p^2+p-1)-\pi(p^2)
\ge c_P {p\over\log p},
\tag{BPL-6}
\]

且

\[
c_P>2C_\pi(1-\alpha),
\tag{BPL-7}
\]

则由 `(BPL-1)` 得

\[
H_\alpha(p)>C_\alpha(p),
\tag{BPL-8}
\]

从而对角分支闭合。

例如 `alpha=0.9` 时，只需

\[
c_P>0.2C_\pi.
\tag{BPL-9}
\]

若 `C_pi=1.30`，则要求 `c_P>0.26`。

## 3. alpha 趋近 1 的意义

令 `alpha=1-\varepsilon`。坏高标签上界变为

\[
B_\alpha^{bad}(p)
\le 2C_\pi\varepsilon {p\over\log p}.
\tag{BPL-10}
\]

所以只要能证明任意固定正比例短区间素数下界 `(BPL-6)`，就可选足够小的 `epsilon`
闭合 AlphaTail。

但若把 `epsilon` 取得随 `p` 太小，使坏命中数低于 `1`，则剩余条件退化为：

```text
(p^2,p^2+p) 中至少有一个素数。
```

这正是对角端点原命题，不能视为独立证明。

## 4. 审稿边界

`BadHigh` 已不是主要障碍：它可由高标签区间长度任意压小。真正不可绕开的输入是某种形式的
对角短区间素数下界：

```text
P_alpha(p)>0 或 P_alpha(p)>=c p/log p。
```

若不引用外部平方根长度短区间素数定理，则必须用 PDEC/SAE 直接证明“没有素数”会造成
固定相位缺陷矛盾。

因此当前路线分叉为：

1. **外部输入版：** 假设或引用 `(BPL-6)`，AlphaTail 由 `(BPL-7)` 闭合；
2. **内部矛盾场版：** 证明 `P_alpha(p)=0` 会触发 PDEC/SAE，而不是通过普通筛下界。

## 5. 下一步最优

继续无条件化时，应直接攻：

```text
PrimeVoid=>PDEC:
若 (p^2,p^2+p) 无素数，
则固定相位族 k≡-p^2 mod q 形成不可允许的端点 CRT 缺陷。
```

这才是对角分支的最终内部硬点。
