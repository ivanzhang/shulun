# shulun 项目操作守则（Codex / Claude 通用）

本文件下面有 `<claude-mem-context>
# Memory Context

# [shulun] recent context, 2026-08-07 11:37am PDT

Legend: 🎯session 🔴bugfix 🟣feature 🔄refactor ✅change 🔵discovery ⚖️decision
Format: ID TIME TYPE TITLE
Fetch details: get_observations([IDs]) | Search: mem-search skill

Stats: 50 obs (11,347t read) | 1,093,219t work | 99% savings

### Aug 6, 2026
8207 11:38p 🟣 MFAC 实际 LCM Gram 能量审计模块实现完成——TDD 绿灯阶段
8210 11:39p 🔵 素数密度补偿波动思想——RH论证新视角
8211 11:40p 🔴 新增两个输入验证红灯测试——lcm_gram_quadratic_form 和 audit_centering_contract 缺少防御性校验
8212 11:42p 🟣 MFAC 实际 LCM Gram 能量审计模块实现完成——Task 2 绿灯通过
8213 " 🔴 MFAC LCM Gram 审计模块输入验证修正——commit 4818e2bd
8214 " 🔵 MFAC 全局自由 Mellin 增长反模型审计结论登记——external-theorem-index 更新
8215 " 🔴 MFAC LCM Gram 能量输入验证修正——非有限系数与非 Mapping 合同防御性校验落地
8216 11:44p 🔵 lcm_gram_quadratic_form 浮点溢出漏洞——有限系数相乘可产生 inf 而未被拒绝
8217 " 🔵 素数密度补偿波动机制——RH论证新视角
8218 11:46p 🔴 lcm_gram_quadratic_form 双重数值安全修正——乘积溢出检测与非内建类型拒绝
8219 " 🔵 audit_centering_contract 裸字符串与非字符串元素红灯——uses 字段迭代验证缺失
### Aug 7, 2026
8221 12:05a 🔵 素数密度自调节补偿机制——RH论证新视角
8223 12:07a 🔵 audit_centering_contract uses 字段验证缺口——裸字符串与非字符串元素均未被拒绝
8224 " 🟣 lcm_gram_quadratic_form 双重数值安全修正落地——溢出检测与非内建类型拒绝
8225 " ✅ shulun 项目新增 worktree codex/mfac-actual-lcm-gram-energy-quality
8229 12:09a 🔴 MFAC LCM Gram 数值合同全面完善——15项测试全绿，commit 276e5650
8233 12:10a 🔵 素数密度自补偿波动机制——RH论证新视角
8234 12:12a 🟣 MFAC LCM Gram 审计模块全部 15 项测试通过
8235 12:13a 🔵 素数密度自补偿机制——RH论证新视角（乘法补集理论）
8236 12:15a 🟣 MFAC LCM Gram 穷举正定性审计测试——Task 2 质量加固提交
8237 " 🔵 素数密度自补偿机制——RH论证新视角
8238 12:16a 🔵 素数密度自补偿波动机制——RH论证新视角
8239 12:18a 🔵 素数密度自补偿机制——乘法集补集视角下的RH论证新思路
8242 12:20a 🔵 素数密度自补偿波动机制——RH论证新视角（用户提案）
8243 12:21a 🟣 MFAC 实际 LCM Gram 能量审计全量验证通过并归档提交
8244 " 🔵 素数补集密度自补偿波动机制——RH论证新视角（续篇深化）
8246 12:24a 🔵 shulun 项目 worktree 布局与 MFAC LCM Gram 能量证书归档状态确认
8248 12:57a 🔵 素数密度自补偿波动机制——RH论证补集动力学新视角
8250 12:58a 🟣 MFAC 实际 LCM Gram 能量审计模块归档——commit dabf639a 完整验证
8252 12:59a 🔵 素数密度自补偿机制——RH论证的补集动力学新视角（深化请求）
8254 1:01a 🔵 素数密度自补偿波动机制——补集动力学对RH论证的核心作用
8253 " 🔵 MFAC 实际 LCM Gram 能量审计——commit dabf639a 完整验证确认
8256 1:03a 🔵 素数密度自补偿波动机制——RH论证的补集动力学新视角（续）
8257 1:04a 🔵 MFAC 实际 LCM Gram 能量审计模块架构与已归档证书状态确认
8258 " 🔴 验证脚本字段断言失败——`row_column_unconditional_closed` 不在证书 JSON 中
8259 1:05a ✅ MFAC LCM Gram 能量审计计划全部归档——状态更新为 implemented_and_archived
8260 1:06a ✅ MFAC LCM Gram 计划所有步骤标记完成并归档
8384 8:41a 🔵 素数密度自补偿波动机制——乘法补集视角论证RH新思路
8385 8:42a 🟣 shulun 项目新建 red-tests worktree——MFAC LCM 去常数投影循环审计 TDD 阶段
8386 " 🔵 MFAC LCM 去常数投影循环计划——write_certificate / direct_projection_data 接口规格确认
8389 8:43a 🟣 shulun MFAC LCM 去常数投影循环 TDD 红灯测试文件写入并提交
8391 8:44a 🔵 素数密度自补偿波动机制——乘法补集视角论证黎曼假设新思路
8392 8:45a ✅ MFAC 投影循环测试文件小幅修正并提交——TDD 红灯阶段全部完成
8393 8:46a 🔵 shulun mfac-lcm-offconstant-projection 红灯状态确认——实现模块缺失导致 ModuleNotFoundError
8394 8:47a 🔵 素数密度自补偿波动机制——乘法补集视角论证RH新思路
8395 8:48a 🔵 素数密度自补偿波动机制——乘法补集视角论证RH新思路（第三轮深化）
8396 8:50a 🔵 shulun MFAC LCM 去常数投影循环审计模块现状确认与全测试绿灯验证
8397 8:52a 🔵 素数密度自补偿波动机制——乘法补集视角论证RH新思路提出
8398 8:53a 🔵 素数密度自补偿波动机制——乘法补集视角论证RH新思路
8399 8:55a 🔵 素数密度自补偿波动机制——乘法补集视角论证RH新思路

Access 1093k tokens of past work via get_observations([IDs]) or mem-search skill.
</claude-mem-context>