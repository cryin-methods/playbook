# 外脑索引 (knowledge-base)

> 指向 `D:\knowledge-base\`（31 条结构化条目：思维模型 14 + 量化交易 17）的索引层。
> 目的：让外脑"能被找到"——满足 playbook 硬约束 5。

## 是什么

`D:\knowledge-base\` 是我多年积累的笔记库，但它只是本机文件。本目录把"哪些条目现在有用、什么时候用"沉淀出来，让新 agent / 未来的我不用遍历整个 knowledge-base。

## 现状

| 类别 | 条目数 | 来源 |
|---|---|---|
| 思维模型 | 14 | `D:\knowledge-base\思维模型\` |
| 量化交易 | 17 | `D:\knowledge-base\量化交易\` |

## 索引格式

每条外脑条目在本目录里建一个 `<date>_<slug>.md` 引用文件：

```markdown
# <条目名>

> 来源：`D:\knowledge-base\<category>\<file>.md`
> 录入日期：YYYY-MM-DD

## 一句话
[条目核心]

## 什么时候用
- 场景 1
- 场景 2

## 跟 playbook 其他维度的关系
- [ai-collab](../ai-collab/)：...
- [behavior-routine](../behavior-routine/)：...
```

## 何时新增索引

- **用得上 3 次以上**的外脑条目 → 入索引
- 用过 1-2 次的 → 留 local 即可
- 刚发现但还没用 → 留 local，1 月后再决定

## 已知坑

- 不要**全量搬运**外脑到 git —— 31 条 × 多 KB 进去会污染 playbook（且很多是过时/不成熟的）
- 索引是"指针"不是"复制"——保持单源（[单一来源原则](https://en.wikipedia.org/wiki/Single_source_of_truth)）
- 索引写"什么时候用"比"是什么"重要——后者在外脑里

## 关联

- [`methods/behavior-routine/`](../behavior-routine/) — 行为纪律（健身 / 饮食 / 交易）会引用这里的具体条目
- [`methods/projects/`](../projects/) — 项目级方法论会引用这里