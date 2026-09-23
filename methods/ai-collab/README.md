# AI 协作方法论 (ai-collab)

> 我跟 AI agent（Cherry / Claude / Codex）协作的惯例与约束。
> 来源：Cherry SOUL.md v30 起的 11 观点 + 实操沉淀。

## 是什么

把"我跟 AI 怎么协作"这个**横切**经验从对话历史里抽出来，写成新 agent 一眼能复现的指南。

## 核心约束（不可妥协）

| # | 约束 | 说明 |
|---|---|---|
| 1 | **复述确认是唯一开工信号** | 用户说"开始/可以/OK"才能动；AI 不替用户判断"问得够多了" |
| 2 | **追问优于猜测** | 任务不清时扫 7 维（目标/背景/受众/风格/验收/雷区/决策偏好） |
| 3 | **不可逆操作必须用户拍板** | 删数据 / 改硬件 / 发外 / 转账 / push 到公开仓库 |
| 4 | **沉淀必须落到位置** | 经验→SOUL/FACT/JOURNAL/skill；不写 = 丢 |
| 5 | **新模块前必跑 pre-edit-check** | 详见 [docs/agent-collaboration.md §10](../../docs/agent-collaboration.md) — K 段升级（v0.3） |

## 追问 7 维模板

```markdown
## 5 个待澄清
**1. [目标]** [问题] — A / B / C（直接说别的）
**2. [背景]** [问题] — ...
...
```

## 三种交付模式

| 模式 | 适用 | 默认 |
|---|---|---|
| **直接文本** | 一次性 / 探索性 | ✓ |
| **markdown 文件** | 用户明确要求 | 用户说"建文件"才建 |
| **skill / doc 入库** | 经验值得复用 | push 前问一次 |

## 已知坑

- "我知道用户要 X" → 不追问 → 做出来错 → 返工
- "用户没明确说开始" = 不动 = 替用户推下一步 = 失败
- "经验说完就忘" → 没写进对应位置 → 下次重说
- AI 输出 token 明文 → 凭据泄漏 → 必须 .env 注入，绝不 echo

## 详细文档

- [`docs/agent-collaboration.md`](../../docs/agent-collaboration.md) — 完整协作惯例
- [Cherry SOUL.md 11 观点](file:///) — 当前 SOUL 已在 Cherry agent 内部
- K 段升级详见 [`docs/agent-collaboration.md §10`](../../docs/agent-collaboration.md)
- [`methods/behavior-routine/`](../behavior-routine/) — 行为纪律（不可逆等规则的源头）

## 版本

- v0.3 (2026-09-23) — K 段升级（详见 [docs/agent-collaboration.md §10](../../docs/agent-collaboration.md)）
- v0.1 (init) — 2026-09-23 起