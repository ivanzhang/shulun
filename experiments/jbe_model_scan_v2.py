#!/usr/bin/env python3
"""JBE 理论分桶账本模型 v2：单次层与多次层同时计账。"""
from __future__ import annotations

import argparse
from math import isqrt, log


def phi(m: int, tau: float) -> float:
    """单锚联合能量贡献。"""
    return 1.0 - tau * m * (m - 1) / 2.0


def positive_multi_phi(mmax: int, tau: float) -> float:
    """多次层的保守正贡献上界：允许 m=2..mmax 中最坏正贡献。"""
    if mmax < 2:
        return 0.0
    return max(0.0, max(phi(m, tau) for m in range(2, min(mmax, 50) + 1)))


def bucket_rows(P: int, tau: float, cs: float, theta: float, multi_eff: float) -> list[dict]:
    D = isqrt(P)
    N_model = 2 * P / log(P)
    rows = []
    Y = D
    j = 0
    while Y < P:
        hi = min(2 * Y, P)
        width = hi - Y
        mid = (Y + hi) / 2
        possible = max(0.0, width / log(max(3.0, mid)))
        mmax = max(1, int(P // max(1, Y)))

        # 单次层：只在可用 LSH 的桶段启用，代表 n_q=1 的筛后锚数。
        single = 0.0
        if Y >= P ** theta:
            single = cs * (P / Y) * possible / log(P)

        # 多次层：同一桶里仍可能存在 n_q>=2 的有效锚，不能因 single 启用而忽略。
        # multi_eff 表示粗骨架穿透/有效率折扣；=1 是极保守，<1 体现小筛损耗。
        multi = multi_eff * possible * positive_multi_phi(mmax, tau)

        rows.append({
            "j": j,
            "Y/P": round(Y / P, 6),
            "possible/N": round(possible / N_model, 6),
            "mmax": mmax,
            "single/N": round(single / N_model, 6),
            "multi/N": round(multi / N_model, 6),
            "total/N": round((single + multi) / N_model, 6),
        })
        Y *= 2
        j += 1
    return rows


def scan(P: int, tau_values: list[float], cs_values: list[float], theta_values: list[float], multi_eff_values: list[float]) -> dict:
    out = []
    for tau in tau_values:
        for cs in cs_values:
            for theta in theta_values:
                for multi_eff in multi_eff_values:
                    rows = bucket_rows(P, tau, cs, theta, multi_eff)
                    total = sum(r["total/N"] for r in rows)
                    out.append({
                        "tau": tau,
                        "C_s": cs,
                        "theta": theta,
                        "multi_eff": multi_eff,
                        "model_total/N": round(total, 4),
                        "closed": total < 1.0,
                    })
    return {"P": P, "cases": out}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--P", type=int, default=1000003)
    parser.add_argument("--tau", nargs="+", type=float, default=[0.05, 0.1, 0.2])
    parser.add_argument("--cs", nargs="+", type=float, default=[0.5, 1.0, 1.5, 2.0])
    parser.add_argument("--theta", nargs="+", type=float, default=[0.5, 0.6, 0.7])
    parser.add_argument("--multi-eff", nargs="+", type=float, default=[0.25, 0.5, 1.0])
    parser.add_argument("--detail", action="store_true")
    args = parser.parse_args()
    print(scan(args.P, args.tau, args.cs, args.theta, args.multi_eff))
    if args.detail:
        print(bucket_rows(args.P, args.tau[0], args.cs[0], args.theta[0], args.multi_eff[0]))


if __name__ == "__main__":
    main()
