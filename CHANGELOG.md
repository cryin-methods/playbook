# Changelog

按 [NAMING.md](../NAMING.md) 规范：v0.1 init 起记。

## v0.2 (2026-09-23) — gap 补 + 真实 smoke test

**新增：**
- README "📐 playbook 的范围"段（明说 playbook vs Cherry 私有 vs 用户本机 的边界）
- README 核心约束表 + 1 行「改 submodule 或 git history 算不可逆」（v0.1 漏了）
- `tests/structure_smoke.py` — 真实 smoke test（90+ 行，stdlib only），覆盖：
  - 12 个必填文件存在
  - SKILL.md frontmatter 有 name + description
  - README 三大核心段（30 秒 / 目录 / 约束）
  - NAMING.md 禁忌列表覆盖
  - 无明文 .env / secrets 目录入仓
  - CHANGELOG 头部有 ## v## 段

**响应 D2 评估**：自解释从 ~70% → 预期 ~85%

## v0.1 (2026-09-23) — init

第一次 push。

**新增：**
- 顶层 README.md（30 秒上手 + 目录 + 核心约束）
- NAMING.md（kebab-case + 含义 + 版本化策略）
- .gitignore（标准 + 凭据 / OS / IDE）
- skill-template/（SKILL.md + README.md，蒸馏自 pm-k12）
- methods/ai-collab/README.md
- methods/prompt-workflow/README.md
- methods/knowledge-base/README.md
- methods/behavior-routine/README.md
- methods/projects/README.md
- docs/agent-collaboration.md（11 观点详解）
- tests/README.md（占位，v0.2 实装 .py）
- .github/ISSUE_TEMPLATE/add-method.md

**已知留白（v0.3 候选）：**
- 各 methods 子目录的详细文档（diet-baseline / fitness-3-tiers / trading-rules / commitment-24h）
- prompt-v4 入库
- GridPilot / only-one / OneTable 项目方法论入库
- tests/ runner script（tests/run_all.py）