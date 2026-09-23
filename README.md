# playbook — Cryin's personal methods

> 知识库 / AI 协作方法论 / 决策日志 / 项目沉淀的统一入口。
> 目的：让我（和未来的 agent）中断几个月后，回来仍能一眼接上。

---

## 给新 agent 的 30 秒阅读

如果你是新启动的 Cherry / Claude / Codex agent，看到这段时按以下顺序读：

1. **[`NAMING.md`](./NAMING.md)** — 命名规范（kebab-case + 含义 + 版本）
2. **[`docs/agent-collaboration.md`](./docs/agent-collaboration.md)** — 我跟 AI agent 的协作惯例（追问式 / 不可逆操作 / 沉淀触发）
3. **[`methods/`](./methods/)** — 各维度方法论入口
4. **本 README 的"目录"段** — 知道哪个维度放哪里

读完后应能回答：
- "我想沉淀一个 X 类经验，应该写到哪个目录、起什么名？"
- "用户给了一个看似简单的任务，但我想先问哪些问题？"
- "什么操作必须让用户亲自拍板、什么 AI 自主跑就行？"

---

## 目录

```
playbook/
├── README.md                  ← 你正在看
├── NAMING.md                  ← 命名规范
├── CHANGELOG.md               ← 版本变更
├── skill-template/            ← 创建新 skill 的最少必要结构（蒸馏自 pm-k12）
│   ├── SKILL.md
│   └── README.md
├── methods/                   ← 各维度方法论
│   ├── ai-collab/             ← AI 协作方法论（追问 / 角色互换 / 不可逆 / 沉淀触发）
│   ├── prompt-workflow/       ← prompt 工作流（v4 沉淀 + 后续版本）
│   ├── knowledge-base/        ← 外脑索引（思维模型 + 量化交易 + 决策日志）
│   ├── behavior-routine/      ← 行为纪律（健身 / 饮食 / 交易 / 承诺）
│   └── projects/              ← 项目级方法论（GridPilot / only-one / OneTable 等）
├── tests/                     ← 自测（各沉淀物的 smoke test）
└── docs/                      ← 横切文档（agent 协作 / 决策模板 / 复盘模板）
```

---

## 核心约束（不能违反）

| 约束 | 说明 |
|---|---|
| **每个沉淀物必须有名字** | kebab-case，含义明确，单数或复数看语境 |
| **每个沉淀物必须有 README** | 第一段说明"是什么"，第二段说明"什么时候用"，第三段"已知坑" |
| **每个沉淀物必须在互联网可被找到** | 这是 playbook 存在的意义。如果只能在本机看，等于没沉淀 |
| **不可逆操作必须用户拍板** | 删数据 / 改硬件 / 发外 / 转账 / push 到公开仓库 / **改 submodule 或 git history（`--force-with-lease` 算）** — 必须先问 |
| **追问优于猜测** | 任务不清先问 7 维，不替用户拍板"开始"信号 |

---

## 📐 playbook 的范围（v0.2 新增 — 避免混淆）

playbook **只管公开沉淀**。其他东西各自有归属，新 agent 别来 playbook 找：

| 类目 | 在哪 | playbook 管吗 |
|---|---|---|
| **AI 协作方法论 / 命名规范 / skill 模板 / 各维度沉淀 / agent-collaboration 详解** | 本 playbook（公开）| ✅ 管 |
| **Cherry Studio 的 SOUL.md / JOURNAL.jsonl / FACT.md / skills/** | Cherry agent 私有（不同机器可能不一样）| ❌ 不管 |
| **用户本机的 `D:\knowledge-base\` / `D:\methods\` / `D:\skills\pm-k12\`** | 用户本机私有 | ❌ 不管（但 playbook `methods/knowledge-base/` 会建索引指针） |
| **GitHub 账号 / SSH key / mihomo 配置 / 域名 / 服务器地址** | `memory/secrets-index.md`（Cherry 私有） | ❌ 不管 |

如果你是新 agent：playbook **只给你协作惯例的骨架**。具体 Cherry 行为 / 用户私人状态 / 网络配置，分别去对应的文件读。

---

## 状态

| 维度 | 内容 |
|---|---|
| 当前版本 | v0.3 (K 升级 + Cherry 自动钩子) |
| 仓库地址 | https://github.com/cryin-methods/playbook |
| 本地路径 | `D:\methods\playbook` |
| 首次 push | 2026-09-23 |
| 命名致敬 | pm-k12 是这套范式的活样板 |

---

## 如何贡献（给未来的我）

加新沉淀物时：

1. 决定它属于哪个维度（`methods/<dim>/`）
2. 读 [`NAMING.md`](./NAMING.md) 取名
3. 复制 [`skill-template/`](./skill-template/) 或该维度的 sibling 目录作为起点
4. 写完三段：是什么 / 什么时候用 / 已知坑
5. 在本 README 的"目录"段更新路径
6. 跑 `tests/` 里的 smoke test
7. commit + push（公开 push 前最后看一眼）