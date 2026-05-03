# BPN-LHB 证书复现账本

本文档完成外审前 H3 义务：把 BPN low-hole bucket 子模块的有限证书与显式常数包整理成可复现审稿表。

## 0. 结论

`BPN-LHB` 子模块在以下五段中闭合：

| 范围 | 证书类型 | 当前状态 |
|---|---|---|
| `13<=P<61` | low-range final certificate | 可复现，全部通过 |
| `61<=P<=103` | narrow-band collision-energy certificate | 可复现，全部通过 |
| `107<=P<=229` | exact `P/5` splitting recursion | 可复现，全部通过 |
| `233<=P<=13207` | integer cross-multiplied product certificate | 可复现，全部通过 |
| `P>=13208` | Rosser--Schoenfeld explicit constants | 外部定理版闭合，引用接口已定位 |

该结论只闭合 `BPN-LHB` 子模块，不推出整个 Prime Matrix 行列命题。全局行列命题仍依赖 `Structured-EHPD/PDEC/SAE/Rankin/RRD/OSPC` 等未闭合接口。

## 1. 复现环境

默认工作目录：

```bash
/opt/code/shulun
```

所有命令使用仓库内 Python 脚本，无随机种子、无网络依赖。生成输出应与仓库内对应 JSON/Markdown 字节级一致。

## 2. 证书清单

| 项 | 脚本 | JSON 输出 | Markdown 输出 | 验收标准 |
|---|---|---|---|---|
| 低范围 | `experiments/prime_matrix_bpn_lhb_low_range_final_certificate.py` | `docs/monograph/prime-matrix-bpn-lhb-low-range-final-certificate.json` | `docs/monograph/prime-matrix-bpn-lhb-low-range-final-certificate.md` | `all_pass=True`, `total_zero=15414`, `summary_sha256=74c6277349f9ef14a9578598f3250bb67ffb98257f0af34a923d74ddf073efb1` |
| 窄带 | `experiments/prime_matrix_bpn_lhb_narrow_band_collision_certificate.py` | `docs/monograph/prime-matrix-bpn-lhb-narrow-band-collision-certificate.json` | `docs/monograph/prime-matrix-bpn-lhb-narrow-band-collision-certificate.md` | `all_pass=True`, 10 个素数各 `failure_count=0` |
| 尾段有限 | `experiments/prime_matrix_bpn_lhb_tail_finite_certificate.py` | `docs/monograph/prime-matrix-bpn-lhb-tail-finite-certificate.json` | `docs/monograph/prime-matrix-bpn-lhb-tail-finite-certificate.md` | `split_failures=[]`, `product_failures=[]`, `product_min_float_margin=0.5347204008758055` |
| 显式尾段 | `experiments/prime_matrix_bpn_lhb_explicit_tail_constant_audit.py` | `docs/monograph/prime-matrix-bpn-lhb-explicit-tail-constant-audit.json` | `docs/monograph/prime-matrix-bpn-lhb-explicit-tail-constant-audit.md` | `last_bad=13207`, `stable_from_in_scan=13208`, `mertens_eps=0.03` |

## 3. 单项复现命令

### 3.1 低范围

```bash
python3 experiments/prime_matrix_bpn_lhb_low_range_final_certificate.py
```

默认覆盖 `13,17,19,23,29,31,37,41,43,47,53,59`，输出低范围 JSON 与 Markdown。

### 3.2 窄带

```bash
python3 experiments/prime_matrix_bpn_lhb_narrow_band_collision_certificate.py
```

默认覆盖 `61,67,71,73,79,83,89,97,101,103`，输出窄带 JSON 与 Markdown。

### 3.3 尾段有限证书

```bash
python3 experiments/prime_matrix_bpn_lhb_tail_finite_certificate.py
```

默认使用 `Q=2310`、`max_p=13207`、`split_denominator=5`，输出两段有限证书。

### 3.4 显式尾段常数审计

```bash
python3 experiments/prime_matrix_bpn_lhb_explicit_tail_constant_audit.py
```

默认使用 `Q=2310`、`max_p=300000`、`mertens_eps=0.03`、`pi_upper_constant=1.25506`。

## 4. 字节级复现核查命令

推荐审稿复现时不要直接覆盖仓库文件，而是输出到临时目录并比较：

```bash
tmp=$(mktemp -d)
export BPN_LHB_TMP="$tmp"
python3 experiments/prime_matrix_bpn_lhb_low_range_final_certificate.py \
  --json-output "$tmp/low.json" --md-output "$tmp/low.md"
python3 experiments/prime_matrix_bpn_lhb_narrow_band_collision_certificate.py \
  --json-output "$tmp/narrow.json" --md-output "$tmp/narrow.md"
python3 experiments/prime_matrix_bpn_lhb_tail_finite_certificate.py \
  --json-output "$tmp/tail.json" --md-output "$tmp/tail.md"
python3 experiments/prime_matrix_bpn_lhb_explicit_tail_constant_audit.py \
  --json-output "$tmp/explicit.json" --md-output "$tmp/explicit.md"

python3 - <<'PY'
import filecmp
import os
from pathlib import Path

pairs = [
    ("low.json", "docs/monograph/prime-matrix-bpn-lhb-low-range-final-certificate.json"),
    ("narrow.json", "docs/monograph/prime-matrix-bpn-lhb-narrow-band-collision-certificate.json"),
    ("tail.json", "docs/monograph/prime-matrix-bpn-lhb-tail-finite-certificate.json"),
    ("explicit.json", "docs/monograph/prime-matrix-bpn-lhb-explicit-tail-constant-audit.json"),
    ("low.md", "docs/monograph/prime-matrix-bpn-lhb-low-range-final-certificate.md"),
    ("narrow.md", "docs/monograph/prime-matrix-bpn-lhb-narrow-band-collision-certificate.md"),
    ("tail.md", "docs/monograph/prime-matrix-bpn-lhb-tail-finite-certificate.md"),
    ("explicit.md", "docs/monograph/prime-matrix-bpn-lhb-explicit-tail-constant-audit.md"),
]

base = Path(os.environ["BPN_LHB_TMP"])
for generated, tracked in pairs:
    if not filecmp.cmp(base / generated, tracked, shallow=False):
        raise SystemExit(f"mismatch: {generated} vs {tracked}")
    print(f"ok: {generated} == {tracked}")
PY
rm -rf "$tmp"
```

本轮已执行该核查，8 个生成文件全部与仓库内文件一致。

## 5. 外部定理接口

显式尾段使用 Rosser--Schoenfeld 1962：

1. Corollary 1, formula `(3.5)`: `pi(x)>x/log x`；
2. Corollary 1, formula `(3.6)`: `pi(x)<1.25506 x/log x`；
3. Theorem 7, formula `(3.26)`: Mertens 乘积上界。

在 `P>=13208` 时，`floor(P/5)>=2641`，故 Mertens 因子

\[
1+\frac{1}{2\log^2\lfloor P/5\rfloor}<1.009<1.03.
\]

因此当前 `mertens_eps=0.03` 是保守可接受常数。若替换为 Dusart 或其他显式常数，必须重新运行显式尾段常数审计与尾段有限证书边界核查。

## 6. 审稿边界

`BPN-LHB` 证书闭合的是 low-hole bucket 接口：

```text
low-hole bucket
=> finite certificates + RS1962 explicit tail
=> BPN-LHB closed as a submodule
```

它不闭合以下全局接口：

```text
Structured-EHPD
PDEC / SAE
Rankin global exits
RRD / OSPC / SelbergUniform
```

这些仍按 `docs/monograph/unclosed-hard-obligations-attack-roadmap.md` 的 H2/H4/H5 路线继续推进。
