# Prompt 工作流 (prompt-workflow)

> prompt 的版本化沉淀。背景：2026-08-28 创建了 `prompt-v4.md`（约 13KB），但只有两个散文件、没结构、没 README，导致 4 月的工作 v3 已不可考。
> 这个目录的目的：让 prompt **版本可考 + 易检索 + 易复盘**。

## 是什么

把"我跟 LLM 协作用的 prompt"按版本归档，每版留 4 件套：
1. `prompt-v<N>.md` — 完整 prompt（人读）
2. `prompt-v<N>-pure.txt` — 纯文本版（程序读）
3. `CHANGELOG.md` — 跟上一版的 diff 摘要
4. `USAGE.md` — 怎么用、什么时候用、已知坑

## 现状

| 版本 | 路径 | 状态 |
|---|---|---|
| v4 | [`D:\prompt-v4\`](file:///D:/prompt-v4/) | 2026-08-28 创建，2 文件，**待入库** |

v3 / v2 / v1 已散失——这是 playbook 存在的根因。

## 入库计划（待办）

- [ ] 把 `D:\prompt-v4\` 复制到 `methods/prompt-workflow/v4/`
- [ ] 写 `CHANGELOG.md`（v3 → v4 的推测 diff——凭印象 + SOUL 早期版本推断）
- [ ] 写 `USAGE.md`
- [ ] 链接到 [skill-template](../../skill-template/) 里作为"如何写 prompt 文档"的范本

## 命名

- 版本子目录 = `v<N>/`（不带前导零）
- 文件名 `prompt-v<N>.md` / `prompt-v<N>-pure.txt`
- CHANGELOG 单文件累积，不分版本

## 已知坑

- v3 之前的东西**已经找不回**——不要假装"v3 是这样"来伪造历史
- 散文件 vs 入库——**先入库再说**，不要在散文件状态超过 1 周
- prompt 里如果含 token / 私有信息——`git add` 前必须 review（SOUL H 凭据边界）