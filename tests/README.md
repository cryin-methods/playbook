# tests/ — 自测

> 每个沉淀物的 smoke test。目的：保证骨架没坏 / 没退化。
> 风格：极简 Python 标准库（避免引入 pytest 等依赖）。

## 怎么用

```bash
python tests/run_all.py
```

预期输出：

```
[OK]   skill-template/SKILL.md has frontmatter
[OK]   NAMING.md exists
[OK]   README.md exists
[OK]   methods/*/README.md all present
[FAIL] <some-check>
```

## 设计原则

- **每个沉淀物一个 smoke 文件** — `tests/<thing>.py` 测 `methods/<thing>/`
- **不引第三方库** — stdlib only，避免污染
- **不测逻辑** — 测**结构**：文件在不在 / frontmatter 齐不齐 / 必填段有没有
- **CI 友好** — 退出码 0 = pass，1 = fail

## 当前覆盖

| 沉淀物 | 测试 | 状态 |
|---|---|---|
| skill-template | `tests/skill-template.py`（待写）| ⚠ 待 |
| methods/* README 齐 | `tests/methods-structure.py`（待写）| ⚠ 待 |
| run_all | `tests/run_all.py`（待写）| ⚠ 待 |

## 何时新增

- 新增一个 `<dim>/` 目录 → 加 `tests/<dim>-structure.py` 验证 README
- 新增一个 skill → 加 `tests/<skill>.py` 验证 frontmatter 必填字段
- 文档说"必填 X" → 加 test 强制（约定 + 自动化 = 不会被忘）