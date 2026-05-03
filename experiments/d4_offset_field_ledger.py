#!/usr/bin/env python3
"""D4 R5 偏移能量场账本。

把普通层线性项、过渡层、短链/轻边界项合并成统一上界。
用法：
  python3 experiments/d4_offset_field_ledger.py \
    --json docs/d4-r5-offset-field-ledger.json
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ordinary-k", type=float, default=5e-4)
    parser.add_argument("--tail-trans", type=float, default=0.14)
    parser.add_argument("--low-trans", type=float, default=0.12)
    parser.add_argument("--short-light", type=float, default=0.13)
    parser.add_argument("--ordinary-weight", type=float, default=700.0)
    parser.add_argument("--target-lowblock", type=float, default=0.3477286482061424)
    parser.add_argument("--envelope", type=float, default=0.35698733112203435)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    ordinary_bound = args.ordinary_k * args.ordinary_weight
    exceptional_l1_bound = args.tail_trans + args.low_trans + args.short_light
    exceptional_l2_bound = math.sqrt(
        args.tail_trans**2 + args.low_trans**2 + args.short_light**2
    )
    total_l1_bound = ordinary_bound + exceptional_l1_bound
    total_energy_bound = ordinary_bound + exceptional_l2_bound
    payload = {
        "ordinary_k": args.ordinary_k,
        "ordinary_weight": args.ordinary_weight,
        "ordinary_bound": ordinary_bound,
        "tail_transition_bound": args.tail_trans,
        "low_transition_bound": args.low_trans,
        "short_light_bound": args.short_light,
        "exceptional_l1_bound": exceptional_l1_bound,
        "exceptional_l2_bound": exceptional_l2_bound,
        "total_l1_field_bound": total_l1_bound,
        "total_energy_field_bound": total_energy_bound,
        "target_lowblock_observed": args.target_lowblock,
        "envelope_k082_at_worst": args.envelope,
        "l1_margin_to_observed": total_l1_bound - args.target_lowblock,
        "l1_margin_to_envelope": args.envelope - total_l1_bound,
        "energy_margin_to_observed": total_energy_bound - args.target_lowblock,
        "energy_margin_to_envelope": args.envelope - total_energy_bound,
        "closes_envelope_l1": total_l1_bound <= args.envelope,
        "closes_envelope_energy": total_energy_bound <= args.envelope,
    }
    print(json.dumps(payload, indent=2))
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
