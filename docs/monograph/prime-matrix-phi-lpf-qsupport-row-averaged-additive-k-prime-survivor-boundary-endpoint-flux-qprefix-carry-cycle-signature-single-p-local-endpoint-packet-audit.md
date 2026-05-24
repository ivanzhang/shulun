# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local endpoint packet 审计

**状态：** `single_p_local_endpoint_structure_ledger_closed_bound_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=single-P local packets inside pure endpoint missing-mirror support
operation=local template, P-slice, route, and endpoint-shell decomposition
dominant_shape=many small width-one local templates, with edge mass split almost evenly between wing and right-tail superclasses
remaining=uniform local template multiplicity and P-slice summation or a named PDEC/SAE return route
```

## 2. single-P local endpoint packet 审计

```text
max_prime=1009
single_P_local_endpoint_structure_ledger_closed=true
single_P_local_endpoint_edge_mass=26753
single_P_local_endpoint_template_count=4915
single_P_support_prime_count=128
single_P_support_P_min/max=97/1009
single_P_edge_mass_per_P_min/median/max=2/167.5/827
single_P_template_edge_mass_min/median/max=1/5/16
observed_local_template_edge_mass_le_16=true
observed_width_one_route_superclass_balance_gap=327
row_column_unconditional_closed=false
```

route superclass edge mass：

| route_superclass | edge_mass | edge_ratio |
| --- | --- | --- |
| wing_single_P_local | 13540 | 0.5061114641348634 |
| right_tail_single_P_local | 13213 | 0.49388853586513665 |

route edge mass：

| route_class | edge_mass | edge_ratio |
| --- | --- | --- |
| pure_right_tail_two_sided_collar | 9056 | 0.338504092998916 |
| pure_upper_wing_single_shell | 9053 | 0.33839195604231304 |
| pure_lower_wing_single_shell | 4487 | 0.16771950809255037 |
| pure_right_tail_right_collar | 2026 | 0.07572982469255785 |
| pure_right_tail_left_collar | 1511 | 0.056479647142376556 |
| pure_right_tail_terminal_full_interval | 620 | 0.023174971031286212 |

A-class edge mass：

| A_class | edge_mass | edge_ratio |
| --- | --- | --- |
| mixed_positive_negative | 26052 | 0.9737973311404329 |
| mixed_with_zero | 388 | 0.014503046387321049 |
| all_positive | 185 | 0.006915112323851531 |
| all_negative | 128 | 0.004784510148394572 |

P bucket edge mass：

| P_bucket | edge_mass | edge_ratio |
| --- | --- | --- |
| P_800_to_1009 | 13897 | 0.5194557619706202 |
| P_500_to_799 | 10114 | 0.3780510596942399 |
| P_200_to_499 | 2687 | 0.10043733413075169 |
| P_le_199 | 55 | 0.002055844204388293 |

template edge-mass distribution：

| template_edge_mass | template_count | template_ratio |
| --- | --- | --- |
| 5 | 1172 | 0.23845371312309258 |
| 4 | 1155 | 0.23499491353001017 |
| 6 | 955 | 0.1943031536113937 |
| 7 | 650 | 0.13224821973550355 |
| 3 | 399 | 0.08118006103763988 |
| 8 | 273 | 0.055544252288911494 |
| 9 | 118 | 0.02400813835198372 |
| 10 | 85 | 0.017293997965412006 |
| 2 | 57 | 0.011597151576805697 |
| 11 | 19 | 0.0038657171922685655 |
| 12 | 19 | 0.0038657171922685655 |
| 14 | 5 | 0.001017293997965412 |
| 1 | 3 | 0.0006103763987792472 |
| 16 | 3 | 0.0006103763987792472 |
| 13 | 1 | 0.0002034587995930824 |
| 15 | 1 | 0.0002034587995930824 |

cycle length edge mass：

| cycle_length | edge_mass | edge_ratio |
| --- | --- | --- |
| 5 | 6135 | 0.2293200762531305 |
| 6 | 5730 | 0.21418158711172577 |
| 4 | 4824 | 0.18031622621762045 |
| 7 | 4606 | 0.17216760737113596 |
| 8 | 2016 | 0.07535603483721452 |
| 3 | 1326 | 0.049564534818525026 |
| 9 | 1053 | 0.03936007176765222 |
| 10 | 590 | 0.022053601465256232 |
| 11 | 209 | 0.007812207976675513 |
| 2 | 138 | 0.005158300003737898 |
| 12 | 96 | 0.0035883826112959294 |
| 14 | 14 | 0.0005233057974806563 |
| 13 | 13 | 0.0004859268119463238 |
| 1 | 3 | 0.0001121369566029978 |

q-prefix bucket edge mass：

| q_prefix_bucket | edge_mass | edge_ratio |
| --- | --- | --- |
| qprefix_17_to_32 | 17252 | 0.644862258438306 |
| qprefix_9_to_16 | 7851 | 0.29346241543004525 |
| qprefix_ge_33 | 847 | 0.031660000747579714 |
| qprefix_5_to_8 | 790 | 0.029529398572122754 |
| qprefix_1_to_4 | 13 | 0.0004859268119463238 |

m-shell bucket edge mass：

| m_shell_bucket | edge_mass | edge_ratio |
| --- | --- | --- |
| m_shell_3_to_4 | 10883 | 0.40679549957014166 |
| m_shell_1_to_2 | 7981 | 0.29832168354950844 |
| m_shell_5_to_8 | 6768 | 0.252980974096363 |
| m_shell_ge_9 | 1121 | 0.04190184278398684 |

最高 P-slices：

| P | edge_mass | template_count | route_profile |
| --- | --- | --- | --- |
| 1009 | 827 | 166 | pure_upper_wing_single_shell:328,pure_right_tail_two_sided_collar:230,pure_lower_wing_single_shell:223,pure_right_tail_left_collar:29,pure_right_tail_right_collar:9,pure_right_tail_terminal_full_interval:8 |
| 991 | 625 | 112 | pure_right_tail_two_sided_collar:269,pure_upper_wing_single_shell:205,pure_lower_wing_single_shell:116,pure_right_tail_right_collar:14,pure_right_tail_terminal_full_interval:11,pure_right_tail_left_collar:10 |
| 997 | 625 | 119 | pure_upper_wing_single_shell:251,pure_lower_wing_single_shell:132,pure_right_tail_two_sided_collar:126,pure_right_tail_right_collar:68,pure_right_tail_left_collar:44,pure_right_tail_terminal_full_interval:4 |
| 919 | 588 | 102 | pure_upper_wing_single_shell:320,pure_right_tail_two_sided_collar:125,pure_lower_wing_single_shell:117,pure_right_tail_right_collar:22,pure_right_tail_terminal_full_interval:4 |
| 971 | 552 | 93 | pure_right_tail_two_sided_collar:224,pure_upper_wing_single_shell:158,pure_right_tail_right_collar:64,pure_right_tail_left_collar:51,pure_lower_wing_single_shell:45,pure_right_tail_terminal_full_interval:10 |
| 881 | 535 | 87 | pure_right_tail_two_sided_collar:275,pure_upper_wing_single_shell:109,pure_lower_wing_single_shell:71,pure_right_tail_right_collar:50,pure_right_tail_left_collar:30 |
| 883 | 517 | 85 | pure_right_tail_two_sided_collar:270,pure_upper_wing_single_shell:126,pure_right_tail_right_collar:55,pure_lower_wing_single_shell:49,pure_right_tail_left_collar:17 |
| 983 | 495 | 94 | pure_upper_wing_single_shell:183,pure_right_tail_two_sided_collar:144,pure_lower_wing_single_shell:109,pure_right_tail_right_collar:50,pure_right_tail_left_collar:9 |
| 929 | 480 | 91 | pure_right_tail_two_sided_collar:240,pure_upper_wing_single_shell:134,pure_right_tail_right_collar:50,pure_lower_wing_single_shell:39,pure_right_tail_terminal_full_interval:17 |
| 853 | 476 | 77 | pure_right_tail_two_sided_collar:189,pure_upper_wing_single_shell:156,pure_lower_wing_single_shell:80,pure_right_tail_terminal_full_interval:24,pure_right_tail_right_collar:15,pure_right_tail_left_collar:12 |
| 827 | 466 | 88 | pure_upper_wing_single_shell:243,pure_lower_wing_single_shell:112,pure_right_tail_two_sided_collar:42,pure_right_tail_left_collar:39,pure_right_tail_right_collar:24,pure_right_tail_terminal_full_interval:6 |
| 821 | 462 | 77 | pure_upper_wing_single_shell:147,pure_right_tail_two_sided_collar:113,pure_lower_wing_single_shell:104,pure_right_tail_right_collar:50,pure_right_tail_left_collar:48 |
| 977 | 458 | 84 | pure_right_tail_two_sided_collar:202,pure_upper_wing_single_shell:150,pure_lower_wing_single_shell:71,pure_right_tail_terminal_full_interval:24,pure_right_tail_right_collar:11 |
| 839 | 455 | 82 | pure_upper_wing_single_shell:165,pure_lower_wing_single_shell:99,pure_right_tail_two_sided_collar:98,pure_right_tail_right_collar:46,pure_right_tail_terminal_full_interval:31,pure_right_tail_left_collar:16 |
| 947 | 449 | 76 | pure_right_tail_two_sided_collar:279,pure_upper_wing_single_shell:108,pure_lower_wing_single_shell:44,pure_right_tail_terminal_full_interval:11,pure_right_tail_right_collar:7 |
| 863 | 446 | 77 | pure_right_tail_two_sided_collar:203,pure_upper_wing_single_shell:133,pure_lower_wing_single_shell:86,pure_right_tail_right_collar:13,pure_right_tail_left_collar:6,pure_right_tail_terminal_full_interval:5 |
| 877 | 442 | 73 | pure_right_tail_two_sided_collar:281,pure_upper_wing_single_shell:85,pure_lower_wing_single_shell:42,pure_right_tail_right_collar:21,pure_right_tail_terminal_full_interval:7,pure_right_tail_left_collar:6 |
| 823 | 435 | 77 | pure_upper_wing_single_shell:168,pure_right_tail_two_sided_collar:155,pure_lower_wing_single_shell:67,pure_right_tail_right_collar:25,pure_right_tail_left_collar:20 |
| 787 | 429 | 71 | pure_upper_wing_single_shell:189,pure_right_tail_two_sided_collar:97,pure_lower_wing_single_shell:85,pure_right_tail_left_collar:33,pure_right_tail_right_collar:25 |
| 859 | 428 | 73 | pure_right_tail_two_sided_collar:172,pure_upper_wing_single_shell:127,pure_lower_wing_single_shell:80,pure_right_tail_left_collar:43,pure_right_tail_right_collar:6 |

最高 single-P templates：

| signed_child | raw_base_template | P | edge_mass | route_class | route_superclass | A_class |
| --- | --- | --- | --- | --- | --- | --- |
| g=10,c=16,A=negative -> g=2,c=3,A=positive -> g=6,c=10,A=positive -> g=4,c=6,A=negative -> g=6,c=9,A=positive -> g=8,c=13,A=negative -> g=4,c=6,A=positive -> g=2,c=3,A=negative | g=10,c=16 -> g=2,c=3 -> g=6,c=10 -> g=4,c=6 -> g=6,c=9 -> g=8,c=13 -> g=4,c=6 -> g=2,c=3 | 829 | 16 | pure_upper_wing_single_shell | wing_single_P_local | mixed_positive_negative |
| g=10,c=9,A=negative -> g=8,c=8,A=positive -> g=6,c=5,A=negative -> g=6,c=6,A=positive -> g=4,c=3,A=positive -> g=8,c=8,A=negative -> g=4,c=4,A=positive -> g=14,c=13,A=negative | g=10,c=9 -> g=8,c=8 -> g=6,c=5 -> g=6,c=6 -> g=4,c=3 -> g=8,c=8 -> g=4,c=4 -> g=14,c=13 | 971 | 16 | pure_right_tail_two_sided_collar | right_tail_single_P_local | mixed_positive_negative |
| g=2,c=1,A=negative -> g=6,c=6,A=negative -> g=6,c=5,A=positive -> g=4,c=4,A=negative -> g=2,c=2,A=positive -> g=4,c=4,A=positive -> g=6,c=5,A=negative -> g=6,c=6,A=positive | g=2,c=1 -> g=6,c=6 -> g=6,c=5 -> g=4,c=4 -> g=2,c=2 -> g=4,c=4 -> g=6,c=5 -> g=6,c=6 | 809 | 16 | pure_right_tail_two_sided_collar | right_tail_single_P_local | mixed_positive_negative |
| g=2,c=2,A=negative -> g=4,c=3,A=negative -> g=6,c=5,A=positive -> g=8,c=6,A=negative -> g=4,c=3,A=positive | g=2,c=2 -> g=4,c=3 -> g=6,c=5 -> g=8,c=6 -> g=4,c=3 | 607 | 15 | pure_right_tail_two_sided_collar | right_tail_single_P_local | mixed_positive_negative |
| g=10,c=10,A=negative -> g=8,c=8,A=positive -> g=10,c=9,A=positive -> g=8,c=8,A=negative -> g=6,c=6,A=positive -> g=4,c=4,A=positive -> g=8,c=7,A=positive | g=10,c=10 -> g=8,c=8 -> g=10,c=9 -> g=8,c=8 -> g=6,c=6 -> g=4,c=4 -> g=8,c=7 | 919 | 14 | pure_right_tail_two_sided_collar | right_tail_single_P_local | mixed_positive_negative |
| g=10,c=10,A=positive -> g=12,c=11,A=negative -> g=2,c=2,A=positive -> g=10,c=9,A=negative -> g=8,c=7,A=positive -> g=6,c=6,A=negative -> g=6,c=6,A=positive -> g=4,c=3,A=positive -> g=8,c=8,A=negative -> g=6,c=5,A=positive -> g=4,c=4,A=negative -> g=8,c=8,A=positive -> g=4,c=3,A=negative -> g=14,c=13,A=negative | g=10,c=10 -> g=12,c=11 -> g=2,c=2 -> g=10,c=9 -> g=8,c=7 -> g=6,c=6 -> g=6,c=6 -> g=4,c=3 -> g=8,c=8 -> g=6,c=5 -> g=4,c=4 -> g=8,c=8 -> g=4,c=3 -> g=14,c=13 | 947 | 14 | pure_right_tail_two_sided_collar | right_tail_single_P_local | mixed_positive_negative |
| g=10,c=17,A=negative -> g=2,c=4,A=positive -> g=4,c=7,A=positive -> g=2,c=3,A=positive -> g=4,c=7,A=negative -> g=14,c=24,A=positive -> g=6,c=10,A=positive | g=10,c=17 -> g=2,c=4 -> g=4,c=7 -> g=2,c=3 -> g=4,c=7 -> g=14,c=24 -> g=6,c=10 | 613 | 14 | pure_upper_wing_single_shell | wing_single_P_local | mixed_positive_negative |
| g=10,c=9,A=negative -> g=2,c=2,A=positive -> g=4,c=3,A=negative -> g=6,c=5,A=negative -> g=4,c=3,A=positive -> g=2,c=2,A=negative -> g=12,c=10,A=positive | g=10,c=9 -> g=2,c=2 -> g=4,c=3 -> g=6,c=5 -> g=4,c=3 -> g=2,c=2 -> g=12,c=10 | 821 | 14 | pure_right_tail_two_sided_collar | right_tail_single_P_local | mixed_positive_negative |
| g=4,c=3,A=positive -> g=8,c=8,A=positive -> g=6,c=5,A=negative -> g=4,c=4,A=positive -> g=8,c=7,A=negative -> g=6,c=5,A=positive -> g=6,c=6,A=negative | g=4,c=3 -> g=8,c=8 -> g=6,c=5 -> g=4,c=4 -> g=8,c=7 -> g=6,c=5 -> g=6,c=6 | 977 | 14 | pure_right_tail_two_sided_collar | right_tail_single_P_local | mixed_positive_negative |
| g=12,c=12,A=negative -> g=8,c=7,A=positive -> g=4,c=4,A=negative -> g=8,c=8,A=positive -> g=4,c=3,A=positive -> g=6,c=6,A=negative -> g=12,c=12,A=positive -> g=2,c=1,A=negative -> g=18,c=18,A=positive -> g=6,c=5,A=negative -> g=6,c=6,A=positive -> g=2,c=2,A=positive -> g=4,c=3,A=negative | g=12,c=12 -> g=2,c=1 -> g=18,c=18 -> g=6,c=5 -> g=6,c=6 -> g=2,c=2 -> g=4,c=3 -> g=12,c=12 -> g=8,c=7 -> g=4,c=4 -> g=8,c=8 -> g=4,c=3 -> g=6,c=6 | 619 | 13 | pure_right_tail_left_collar | right_tail_single_P_local | mixed_positive_negative |
| g=10,c=10,A=positive -> g=8,c=7,A=negative -> g=10,c=9,A=negative -> g=2,c=2,A=positive -> g=4,c=3,A=positive -> g=6,c=6,A=negative -> g=6,c=5,A=positive -> g=2,c=2,A=negative -> g=12,c=11,A=positive -> g=4,c=4,A=positive -> g=6,c=5,A=negative -> g=8,c=7,A=positive | g=10,c=10 -> g=8,c=7 -> g=10,c=9 -> g=2,c=2 -> g=4,c=3 -> g=6,c=6 -> g=6,c=5 -> g=2,c=2 -> g=12,c=11 -> g=4,c=4 -> g=6,c=5 -> g=8,c=7 | 877 | 12 | pure_right_tail_two_sided_collar | right_tail_single_P_local | mixed_positive_negative |
| g=10,c=11,A=positive -> g=2,c=3,A=negative -> g=4,c=4,A=negative -> g=6,c=7,A=positive -> g=2,c=2,A=negative -> g=12,c=14,A=positive | g=10,c=11 -> g=2,c=3 -> g=4,c=4 -> g=6,c=7 -> g=2,c=2 -> g=12,c=14 | 823 | 12 | pure_right_tail_two_sided_collar | right_tail_single_P_local | mixed_positive_negative |
| g=10,c=11,A=positive -> g=6,c=6,A=negative -> g=6,c=7,A=positive -> g=4,c=4,A=negative -> g=2,c=2,A=negative -> g=12,c=13,A=positive | g=10,c=11 -> g=6,c=6 -> g=6,c=7 -> g=4,c=4 -> g=2,c=2 -> g=12,c=13 | 769 | 12 | pure_right_tail_two_sided_collar | right_tail_single_P_local | mixed_positive_negative |
| g=10,c=12,A=negative -> g=2,c=2,A=positive -> g=4,c=5,A=negative -> g=6,c=7,A=positive -> g=6,c=8,A=positive -> g=2,c=2,A=negative -> g=12,c=15,A=positive -> g=4,c=4,A=negative -> g=6,c=8,A=negative -> g=8,c=9,A=negative -> g=10,c=12,A=positive -> g=8,c=10,A=negative | g=10,c=12 -> g=2,c=2 -> g=4,c=5 -> g=6,c=7 -> g=6,c=8 -> g=2,c=2 -> g=12,c=15 -> g=4,c=4 -> g=6,c=8 -> g=8,c=9 -> g=10,c=12 -> g=8,c=10 | 881 | 12 | pure_right_tail_two_sided_collar | right_tail_single_P_local | mixed_positive_negative |
| g=10,c=12,A=negative -> g=2,c=3,A=positive -> g=4,c=4,A=negative -> g=6,c=8,A=positive -> g=6,c=7,A=negative -> g=2,c=2,A=negative -> g=12,c=14,A=positive -> g=4,c=5,A=negative -> g=6,c=7,A=positive -> g=8,c=10,A=negative -> g=10,c=12,A=positive -> g=8,c=9,A=positive | g=10,c=12 -> g=2,c=3 -> g=4,c=4 -> g=6,c=8 -> g=6,c=7 -> g=2,c=2 -> g=12,c=14 -> g=4,c=5 -> g=6,c=7 -> g=8,c=10 -> g=10,c=12 -> g=8,c=9 | 881 | 12 | pure_right_tail_two_sided_collar | right_tail_single_P_local | mixed_positive_negative |
| g=10,c=15,A=positive -> g=6,c=9,A=negative -> g=6,c=9,A=positive -> g=2,c=3,A=positive -> g=18,c=27,A=positive -> g=6,c=8,A=negative | g=10,c=15 -> g=6,c=9 -> g=6,c=9 -> g=2,c=3 -> g=18,c=27 -> g=6,c=8 | 1009 | 12 | pure_upper_wing_single_shell | wing_single_P_local | mixed_positive_negative |
| g=10,c=16,A=negative -> g=2,c=3,A=positive -> g=6,c=10,A=negative -> g=8,c=13,A=positive -> g=4,c=6,A=positive -> g=2,c=3,A=negative | g=10,c=16 -> g=2,c=3 -> g=6,c=10 -> g=8,c=13 -> g=4,c=6 -> g=2,c=3 | 821 | 12 | pure_upper_wing_single_shell | wing_single_P_local | mixed_positive_negative |
| g=10,c=7,A=positive -> g=14,c=9,A=negative -> g=4,c=3,A=negative -> g=2,c=1,A=positive -> g=4,c=3,A=positive -> g=14,c=10,A=negative -> g=6,c=4,A=negative -> g=6,c=4,A=positive -> g=2,c=1,A=negative -> g=6,c=5,A=positive -> g=4,c=2,A=negative -> g=2,c=2,A=positive | g=10,c=7 -> g=14,c=9 -> g=4,c=3 -> g=2,c=1 -> g=4,c=3 -> g=14,c=10 -> g=6,c=4 -> g=6,c=4 -> g=2,c=1 -> g=6,c=5 -> g=4,c=2 -> g=2,c=2 | 503 | 12 | pure_lower_wing_single_shell | wing_single_P_local | mixed_positive_negative |
| g=10,c=8,A=negative -> g=12,c=10,A=positive -> g=2,c=2,A=negative -> g=10,c=9,A=positive -> g=2,c=1,A=negative -> g=4,c=4,A=positive -> g=8,c=6,A=negative -> g=6,c=5,A=negative -> g=4,c=4,A=negative -> g=8,c=7,A=positive -> g=4,c=3,A=negative -> g=14,c=12,A=positive | g=10,c=8 -> g=12,c=10 -> g=2,c=2 -> g=10,c=9 -> g=2,c=1 -> g=4,c=4 -> g=8,c=6 -> g=6,c=5 -> g=4,c=4 -> g=8,c=7 -> g=4,c=3 -> g=14,c=12 | 991 | 12 | pure_right_tail_two_sided_collar | right_tail_single_P_local | mixed_positive_negative |
| g=10,c=8,A=negative -> g=8,c=6,A=positive -> g=10,c=9,A=positive -> g=8,c=6,A=negative -> g=6,c=5,A=positive -> g=8,c=7,A=positive | g=10,c=8 -> g=8,c=6 -> g=10,c=9 -> g=8,c=6 -> g=6,c=5 -> g=8,c=7 | 937 | 12 | pure_right_tail_left_collar | right_tail_single_P_local | mixed_positive_negative |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PureEndpointPhaseInterfaceImported | True | True | The previous pure endpoint phase-interface ledger is imported. | none for import |
| SinglePLocalEndpointStructureLedger | True | True | The single-P local mass is decomposed by route, A-class, P-slice, q-prefix, and shell-prime load. | none for the finite structure ledger |
| LocalTemplateMultiplicityUniformBound | False | False | Promote the observed bounded local template masses to a uniform proof. | requires an analytic or structural multiplicity argument, not just the finite ledger |
| SinglePSliceEndpointPacketSummationOrPDEC | False | False | Sum the width-one local packets over P-slices without parity loss, or return failures to a named PDEC/SAE route. | requires global P-slice summation or a formal defect route |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear_v3 | https://arxiv.org/abs/2511.09459 | not directly applicable to single-P local packets without a long completed trace family |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | not directly applicable until a bilinear Kloosterman variable pair is extracted |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | not directly applicable to width-one P-support packets |
| Xu_Zhang_2026_generalized_kloosterman_arbitrary_sets | https://doi.org/10.1016/j.jnt.2025.09.027 | published Kloosterman-set input; still needs explicit finite-field set variables and does not bound width-one packets by itself |
| Li_2023_short_interval_primes_x_052_v8 | https://arxiv.org/abs/2308.04458 | does not estimate signed single-P local endpoint packets |

```text
FKMS_trace_bilinear=does not enter before width-one local packets are lifted to a genuine trace family
Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman=does not bound single-P local packets without extracted bilinear Kloosterman variables
Wright_unbalanced_Kloosterman=does not address P-support width one
Xu_Zhang_generalized_Kloosterman_arbitrary_sets=published external check; still requires explicit finite-field set variables and is not a direct local packet bound
Li_short_interval_x_052=irrelevant to signed carrier phase saving
```

结论：single-P local endpoint 支路已被压成局部模板重数与 P-slice
求和两个实际门。平均型 trace/Kloosterman theorem 仍不能直接吃掉该支路。

## 5. 最新最窄口

```text
LocalTemplateMultiplicityUniformBound
AND SinglePSliceEndpointPacketSummationOrPDEC
AND MultiPPureEndpointTraceKloostermanCompletion
AND PureEndpointCarrierPhaseSaving
AND MixedRightTailEndpointRouterNoLoss
AND UnequalMirrorPairResidualPhaseSaving
AND ThinPSupportCarrierSummationWithoutLoss
AND ResidualEndpointPathSummationWithoutBoundaryLoss
AND NoLossAggregationAcross15439QPrefixFlowAtoms
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
single_P_local_endpoint_structure_ledger_closed=true
local_template_multiplicity_uniform_bound_proved=false
single_P_slice_endpoint_packet_summation_closed=false
single_P_local_endpoint_packet_bound_closed=false
multi_P_trace_completion_closed=false
pure_endpoint_carrier_phase_saving_closed=false
mixed_right_tail_endpoint_router_no_loss_closed=false
unequal_mirror_pair_residual_phase_saving_closed=false
thin_P_support_carrier_summation_closed=false
residual_endpoint_path_summation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
