#!/usr/bin/env python3
"""JBE 理论分桶账本模型扫描。"""
from __future__ import annotations

import argparse
from math import isqrt, log


def phi(m: int, tau: float) -> float:
    """单锚联合能量贡献。"""
    return 1.0 - tau * m * (m - 1) / 2.0


def bucket_rows(P: int, tau: float, cs: float, theta: float) -> list[dict]:
    D = isqrt(P)
    N_model = 2 * P / log(P)
    rows = []
    Y = D
    j = 0
    while Y < P:
        hi = min(2 * Y, P)
        mid = (Y + hi) / 2
        possible = max(0.0, (hi - Y) / log(max(3.0, mid)))
        mmax = max(1, int(P // max(1, Y)))
        single = 0.0
        if Y >= P ** theta:
            single = cs * (P / Y) * possible / log(P)
        # 多次层极保守：按桶典型最大层数给正贡献。
        multi_phi = max(0.0, phi(max(2, min(mmax, 20)), tau)) if mmax >= 2 else 0.0
        multi = possible * multi_phi if Y < P ** theta else 0.0
        rows.append({
            "j": j,
            "Y/P": round(Y / P, 5),
            "possible/N": round(possible / N_model, 5),
            "mmax": mmax,
            "single/N": round(single / N_model, 5),
            "multi/N": round(multi / N_model, 5),
            "total/N": round((single + multi) / N_model, 5),
        })
        Y *= 2
        j += 1
    return rows


def scan(P: int, tau_values: list[float], cs_values: list[float], theta_values: list[float]) -> dict:
    out = []
    for tau in tau_values:
        for cs in cs_values:
            for theta in theta_values:
                rows = bucket_rows(P, tau, cs, theta)
                total = sum(r["total/N"] for r in rows)
                out.append({"tau": tau, "C_s": cs, "theta": theta, "model_total/N": round(total, 4), "closed": total < 1.0})
    return {"P": P, "cases": out}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--P", type=int, default=1000003)
    parser.add_argument("--tau", nargs="+", type=float, default=[0.05, 0.1, 0.2])
    parser.add_argument("--cs", nargs="+", type=float, default=[0.5, 1.0, 1.5, 2.0])
    parser.add_argument("--theta", nargs="+", type=float, default=[0.5, 0.6, 0.7])
    parser.add_argument("--detail", action="store_true")
    args = parser.parse_args()
    print(scan(args.P, args.tau, args.cs, args.theta))
    if args.detail:
        print(bucket_rows(args.P, args.tau[0], args.cs[0], args.theta[0]))


if __name__ == "__main__":
    main()
