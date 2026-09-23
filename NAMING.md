# Naming Conventions — playbook

> 命名是沉淀的一半。命名前请读完。

## 总原则

1. **含义优先** — 看到名字就知道它是什么、什么时候用
2. **kebab-case** — 全小写、短横线分隔（GitHub URL 友好）
3. **稳定胜过漂亮** — 名字一旦 push 出去，就改不动（redirect 成本极高）
4. **单数 vs 复数** — 看语境：方法论 / skill 用单数（`prompt-workflow`），具体条目用复数（`decision-logs/`）

## 目录命名

| 场景 | 模式 | 示例 |
|---|---|---|
| 维度根目录 | `<dim-name>/`（单数，含义明确） | `methods/ai-collab/` |
| 子分类 | `<category>/` | `methods/knowledge-base/decision-logs/` |
| skill 仓库（独立版本化） | `<skill-name>/` + 版本子目录 | `skills/pm-k12/v3/`、`skills/pm-k12/v4/` |
| skill 模板 | `skill-template/`（固定名） | — |
| 自测 | `tests/<unit-of-test>/` | `tests/skill-template/` |
| 横切文档 | `docs/<doc-name>.md` | `docs/agent-collaboration.md` |

## 文件命名

| 场景 | 模式 | 示例 |
|---|---|---|
| skill 定义（Cherry Studio 识别） | `SKILL.md`（固定名，必须在 skill 根目录） | `skill-template/SKILL.md` |
| 仓库 / 维度 README | `README.md`（固定名） | `methods/ai-collab/README.md` |
| 单条记录 / 决策 | `<YYYY-MM-DD>_<slug>.md` | `2026-09-20_高频行为反制_轻量日志与分层节奏.md` |
| 横切文档 | `<doc-name>.md` | `docs/decision-template.md` |
| 配置示例 | `<tool>.example.json` | `skill-template/assets/config/mcp.json.example` |

## 命名禁忌

| 禁忌 | 为什么 |
|---|---|
| `temp/` / `tmp/` / `misc/` | 用户 8 月重起步就是因为"丢了 v3 在 temp" |
| `untitled-*.md` | 没有含义 |
| 中文文件名 | 跨平台兼容 + grep 友好 |
| 大写 + 下划线混用 | `My_Doc.md` 这种 |
| 单字母 | `a.md` / `x.js` |
| v1 / v2 后缀 | 用 `versions/v1/` 子目录而不是文件名后缀（避免 grep 时被分割） |

## 版本化策略

沉淀物演进时：

- **小改**（typo / 段落调整） → 直接改原文，commit message 标注
- **中等改**（结构调整、新增段落） → 在 `CHANGELOG.md` 记录，原文保留
- **大改**（范式变了） → 复制到 `v2/` 子目录，v1 标 "deprecated"
- **彻底重写** → 写到新目录，旧的写 "superseded by <new-name>"

参考范本：`D:\skills\pm-k12\` 用 `v3.0` 在 README 顶部标注。

## 例：完整命名路径

```
playbook/
├── methods/
│   └── prompt-workflow/                  # 维度根（单数）
│       ├── README.md                    # 维度 README
│       └── v4/                          # 版本子目录（如果结构变了）
│           ├── README.md
│           ├── prompt-v4-pure.txt
│           └── prompt-v4.md
└── skills/
    └── pm-k12/                          # 独立 skill（submodule）
        ├── README.md
        └── SKILL.md
```

---

## 命名校验 checklist（提交前自查）

- [ ] 看一眼就知道是什么
- [ ] 全小写 + 短横线
- [ ] 不在禁忌列表
- [ ] 文件路径总和指向**单一**位置（不重复）
- [ ] 新目录已加进顶层 `playbook/README.md` 的"目录"段
- [ ] cross-reference 没断（其他文件里 grep 新名字能命中）