"""验证 MFAC RH 主链依赖图。"""

import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

from experiments.prime_matrix_mfac_rh_main_chain_graph_audit import (
    MODULE_ROLE_REGISTRY,
    build_main_chain_graph,
)


class MFACRHMainChainGraphAuditTest(unittest.TestCase):
    """验证 MFAC RH 主链图谱的严格覆盖和保守边界。"""

    def test_registry_covers_inventory_and_preserves_multiple_roles(self) -> None:
        """每个库存模块必须预注册，且一个模块可以保留多个角色。"""
        inventory = {
            "modules": [
                {
                    "module_name": name,
                    "classification": (
                        "conditional_or_external_dependency"
                        if name == "mertens_conditional_l2_upper"
                        else "open_or_unresolved"
                    ),
                    "rh_blockers": [],
                }
                for name in MODULE_ROLE_REGISTRY
            ]
        }

        graph = build_main_chain_graph(inventory)

        by_name = {item["module_name"]: item for item in graph["module_roles"]}
        self.assertEqual(graph["unmapped_modules"], [])
        self.assertEqual(graph["stale_registry_modules"], [])
        self.assertEqual(len(by_name["actual_lcm_gram_energy"]["roles"]), 2)
        self.assertEqual(
            {
                role["node"]
                for role in by_name["mertens_conditional_l2_upper"]["roles"]
            },
            {"W1", "C7"},
        )
        self.assertFalse(graph["rh_proved"])

    def test_unknown_module_blocks_and_conditional_w1_never_closes_chain(self) -> None:
        """未映射模块必须阻断；条件 W1 不能跳过 W2 或关闭 RH 链。"""
        with self.assertRaisesRegex(ValueError, "unmapped"):
            build_main_chain_graph(
                {
                    "modules": [
                        {
                            "module_name": "unknown",
                            "classification": "open_or_unresolved",
                        }
                    ]
                }
            )

        inventory = {
            "modules": [
                {
                    "module_name": name,
                    "classification": (
                        "conditional_or_external_dependency"
                        if name == "mertens_conditional_l2_upper"
                        else "open_or_unresolved"
                    ),
                    "rh_blockers": [],
                }
                for name in MODULE_ROLE_REGISTRY
            ]
        }

        graph = build_main_chain_graph(inventory)

        self.assertEqual(graph["nodes"]["W1"]["status"], "conditional")
        self.assertEqual(graph["nodes"]["W2"]["status"], "not_started")
        self.assertEqual(graph["shortest_blocking_path"], ["W1", "W2"])
        self.assertFalse(graph["rh_chain_closed"])
        self.assertFalse(graph["rh_proved"])

    def test_missing_registered_module_blocks_generation(self) -> None:
        """库存漏掉已预注册模块时不得生成看似完整的图谱。"""
        inventory = {
            "modules": [
                {
                    "module_name": name,
                    "classification": "open_or_unresolved",
                    "rh_blockers": [],
                }
                for name in MODULE_ROLE_REGISTRY
                if name != "uniform_offconstant_coercivity"
            ]
        }

        with self.assertRaisesRegex(ValueError, "stale"):
            build_main_chain_graph(inventory)

    def test_cli_never_promotes_inventory_rh_claim_to_graph_proof(self) -> None:
        """即使库存模块声称 RH，图谱也只按预注册义务输出未闭合状态。"""
        with TemporaryDirectory() as directory:
            root = Path(directory)
            inventory_path = root / "inventory.json"
            json_path = root / "graph.json"
            markdown_path = root / "graph.md"
            inventory_path.write_text(
                json.dumps(
                    {
                        "modules": [
                            {
                                "module_name": name,
                                "classification": "open_or_unresolved",
                                "rh_blockers": [],
                                "rh_proved_field": name == "actual_lcm_gram_energy",
                            }
                            for name in MODULE_ROLE_REGISTRY
                        ]
                    }
                ),
                encoding="utf-8",
            )
            result = subprocess.run(
                [
                    sys.executable,
                    "experiments/prime_matrix_mfac_rh_main_chain_graph_audit.py",
                    "--inventory",
                    str(inventory_path),
                    "--json-out",
                    str(json_path),
                    "--markdown-out",
                    str(markdown_path),
                ],
                cwd=Path.cwd(),
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, msg=result.stderr)
            payload = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertFalse(payload["rh_proved"])
            self.assertFalse(payload["rh_chain_closed"])
            self.assertIn("不构成 RH 证明", markdown_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
