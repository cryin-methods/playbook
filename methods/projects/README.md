# 项目方法论 (projects)

> 已完成 / 在做的项目的"踩坑+设计决策"沉淀。
> 一个项目=一个 `<project-name>/` 子目录。

## 是什么

项目做完容易"忘了为什么这么做"。这个维度沉淀"决策 + 坑 + 范式"——下次新项目开始时能**翻一遍找相似**。

## 现状

| 项目 | 状态 | 来源 |
|---|---|---|
| **only-one** | v0.5.2 上线 (https://cryin.online) | `D:\AI\`（also GitHub: Cryin-20/only-one）|
| **GridPilot** | testnet 跑通 (https://cryin.online/gp/) | `D:\projects\` (待梳理) |
| **OneTable** | v3 抖音视频抓取分析 | `D:\home\`（命名致敬"一只桌子"）|
| **pm-k12** | 公开 skill v3 | `D:\skills\pm-k12\` |

## 每个项目子目录结构

```
<project-name>/
├── README.md           # 是什么 / 什么时候用 / 已知坑
├── decisions.md        # 关键决策时间线（为什么做 / 放弃什么 / 选了什么）
├── pitfalls.md         # 实际踩过的坑（按现象分类，不按时间）
└── versions/           # 重大版本切换留档（v1 → v2 → v3）
    ├── v1.md
    └── v2.md
```

## 何时新增

- 项目**做完**或**做满 1 个月** → 至少写 `decisions.md` 和 `pitfalls.md`
- 命名纪念日 / 重大重写 → 写 `versions/v<N>.md`

## 已知坑

- 项目做完不写 decisions → 下次做类似项目又从头摸索
- 写"流水账"而不是"决策点" → 没用——只记**为什么**不记"做了什么"
- 链接到外部但外部失效 → broken links = 不存在

## 关联

- [`methods/ai-collab/`](../ai-collab/) — 项目里"AI 怎么参与"的惯例
- [`methods/knowledge-base/`](../knowledge-base/) — 项目里"用了哪些外脑"