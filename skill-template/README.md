# skill-template

> 蒸馏自 `D:\skills\pm-k12\` 的最少必要 skill 结构。
> 用途：创建新 skill 时的起点（不要直接复制 pm-k12）。

## 是什么

Cherry Studio 的 `SKILL.md` frontmatter（`name` + `description`）会被自动扫描并加载。把方法论沉淀成 skill 的最小可行结构 = 一个 `SKILL.md` + 一个 `README.md` + 可选的 `scripts/`。

## 什么时候用

- 沉淀一个**稳定可复用**的工作流 / 方法论
- 未来 agent（或不同机器上的 agent）需要能识别这个名字

## 什么时候不用

- 一次性 / 实验性 idea → 写到 `methods/<dim>/`，成熟后再升级成 skill
- 跨对话频繁变的内容 → 用 `methods/` 替代

## 怎么用

1. 复制 `skill-template/` 整个目录到 `skills/<your-skill-name>/`（kebab-case，见 [`../NAMING.md`](../NAMING.md)）
2. 编辑 `SKILL.md` 的 frontmatter：`name` 和 `description`（这两个字段决定 agent 能不能识别）
3. 改写三段：是什么 / 怎么用 / 已知坑
4. Cherry Studio 重启 / 重扫自动加载
5. 跑 `tests/skill-template/` 里的 smoke test

## 已知坑

- **frontmatter `description` 写得像 API 文档** — 应写成"用户会怎么自然说"，包含 2-3 个触发短语
- **smoke test 永远不跑** — 写完 skill 不验证 = 不写
- **CHANGELOG 在 v1 之前就建** — 过早结构化
- **复制 pm-k12 全部 80+ 文件** — 90% 用不到，先用这个 5 文件的版本

## 范本对照

| 场景 | 用 |
|---|---|
| 蒸馏骨架 | 本 `skill-template/`（5 文件） |
| 完整活样板 | `D:\skills\pm-k12\`（80+ 文件，本地参考 / 不进 playbook） |
| 已 GitHub 公开 | https://github.com/<user>/<skill>（submodule 接入） |