# Changelog

按 [NAMING.md](../NAMING.md) 规范：v0.1 init 起记。

## v0.3 (2026-09-23) — K 段升级 + Cherry 自动钩子

**核心变更**：观点 K 从「同库新模块先抄旧修复」（v0.1 软规则）升级为「同库新模块前必跑 pre-edit-check」（v0.3 硬触发）

**新增：**
- `docs/agent-collaboration.md` §10 — 观点 K 升级详解（v0.1 原措辞 / 升级原因 / 升级版 / Cherry 软钩子 / 配套资产）
- `docs/agent-collaboration.md` §9 表格 K 行升级
- `.gitignore` 加 `methods/ai-collab/SOUL-snapshots/`（私有备份，不能公开）

**升级原因：**
K 自 2026-09-14 写以来 8 天，触发率仅 ~1/3（实测：anchor 引号 3+ 次、edit_safety 误报 3 次、bytes literal 中文 4 次都没拦住）。**靠 AI 自觉不可靠 → 必须升级为硬触发 + 工程化钩子**。

**Cherry 侧配套（不在公开范围）：**
- SOUL.md 观点 K v2（私有）
- Cherry SKILL `auto-pre-edit-check`

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