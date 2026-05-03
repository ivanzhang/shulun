#!/usr/bin/env python3
"""从精确符号模板中抽取可参数化骨架。"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


def skeleton_from_template(template: dict) -> dict:
    """去掉绝对 floor，只保留偏移团与 a 形状。"""
    groups = []
    for group in template["groups"]:
        adata = group["a_data"]
        groups.append(
            {
                "offset": group["offset"],
                "layer": group["layer"],
                "prefix_tail": group["prefix_tail"],
                "count": group["count"],
                "tau_sum": group["tau_sum"],
                "a_values": tuple(item["a"] for item in adata),
                "tau_values": tuple(item["tau"] for item in adata),
                "h_mod_values": tuple(item["h_mod_a"] for item in adata),
            }
        )
    return {"branch": template["branch"], "groups": groups}


def main() -> int:
    data = json.loads(Path("docs/d4-r5-symbolic-templates-1088200-1088600.json").read_text())
    skeletons = {}
    for name, witness in data["witnesses"].items():
        if witness is None:
            continue
        skel = skeleton_from_template(witness["template"])
        canonical = json.dumps(skel, sort_keys=True, separators=(",", ":"))
        digest = hashlib.sha256(canonical.encode()).hexdigest()[:20]
        skeletons[name] = {
            "skeleton_digest": digest,
            "example_x": witness["x"],
            "branch": witness["branch"],
            "group_count": len(skel["groups"]),
            "a_total": sum(len(group["a_values"]) for group in skel["groups"]),
            "skeleton": skel,
            "query_values": witness["query_values"],
        }
    payload = {
        "certificate_type": "D4-R5-symbolic-witness-skeleton-library",
        "source": "docs/d4-r5-symbolic-templates-1088200-1088600.json",
        "status": "exact witness skeletons for finite window; parameter coverage proof remains",
        "skeletons": skeletons,
        "skeleton_count": len({item["skeleton_digest"] for item in skeletons.values()}),
    }
    Path("docs/d4-r5-symbolic-witness-skeleton-library.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    print(json.dumps({k: v for k, v in payload.items() if k != "skeletons"}, ensure_ascii=False, indent=2))
    for name, item in skeletons.items():
        print(name, item["skeleton_digest"], item["example_x"], item["group_count"], item["a_total"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
