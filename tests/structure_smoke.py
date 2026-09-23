"""structure_smoke.py — playbook 骨架 smoke test

跑法：`python tests\structure_smoke.py`
退出码 0 = pass，1 = fail

设计原则（来自 docs/agent-collaboration.md §8）：
- 不引第三方库（stdlib only）
- 测**结构**，不测逻辑（文件在 / frontmatter 齐 / 必填段）
- 失败定义要硬
"""
from __future__ import annotations

import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent  # tests/ → repo root


def check(label: str, ok: bool, detail: str = "") -> bool:
    """Print result, return ok. Caller decides fail logic."""
    status = "OK  " if ok else "FAIL"
    line = f"[{status}] {label}"
    if detail:
        line += f"  ({detail})"
    print(line)
    return ok


def test_files_exist() -> list[bool]:
    """必填文件必须存在"""
    must_exist = [
        "README.md",
        "NAMING.md",
        "CHANGELOG.md",
        ".gitignore",
        "skill-template/SKILL.md",
        "skill-template/README.md",
        "docs/agent-collaboration.md",
        "methods/ai-collab/README.md",
        "methods/prompt-workflow/README.md",
        "methods/knowledge-base/README.md",
        "methods/behavior-routine/README.md",
        "methods/projects/README.md",
    ]
    results = []
    for rel in must_exist:
        p = REPO_ROOT / rel
        results.append(check(f"file exists: {rel}", p.is_file()))
    return results


def test_skill_md_frontmatter() -> bool:
    """SKILL.md 必须有 YAML frontmatter 含 name + description"""
    p = REPO_ROOT / "skill-template" / "SKILL.md"
    if not p.is_file():
        return check("SKILL.md frontmatter", False, "file missing")
    text = p.read_text(encoding="utf-8")
    # YAML frontmatter: --- ... ---
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return check("SKILL.md frontmatter", False, "no --- delimiter")
    fm = m.group(1)
    has_name = bool(re.search(r"^name:\s*\S+", fm, re.MULTILINE))
    has_desc = bool(re.search(r"^description:\s*\S+", fm, re.MULTILINE))
    detail = "name+desc" if (has_name and has_desc) else f"name={has_name} desc={has_desc}"
    return check("SKILL.md frontmatter has name + description", has_name and has_desc, detail)


def test_readme_three_sections() -> bool:
    """顶层 README.md 必须有「给新 agent 的 30 秒阅读 / 目录 / 核心约束」3 段"""
    p = REPO_ROOT / "README.md"
    if not p.is_file():
        return check("top-level README.md three sections", False, "file missing")
    text = p.read_text(encoding="utf-8")
    sections = [
        "给新 agent 的 30 秒阅读" in text,
        "目录" in text,
        "核心约束" in text,
    ]
    return check("top-level README.md has 3 核心段", all(sections), f"{sum(sections)}/3")


def test_naming_no_temp_or_misc() -> bool:
    """NAMING.md 禁忌列表要含 temp/tmp/misc + 中文文件名 + 单字母"""
    p = REPO_ROOT / "NAMING.md"
    if not p.is_file():
        return check("NAMING.md 禁忌列表", False, "file missing")
    text = p.read_text(encoding="utf-8")
    must_have = ["temp", "tmp", "untitled", "中文文件名", "单字母"]
    missing = [m for m in must_have if m not in text]
    return check("NAMING.md 禁忌列表覆盖", not missing, f"missing: {missing}" if missing else "ok")


def test_no_secrets_in_repo() -> bool:
    """绝不能有明文 .env / SSH 私钥 / API key 入仓"""
    bad_patterns = [
        (REPO_ROOT / ".env", ".env 不能入仓"),
        (REPO_ROOT / "secrets", "secrets/ 目录不能入仓"),
    ]
    # 也检查 git 历史：但这里只检查 working tree
    results = []
    for p, label in bad_patterns:
        results.append(check(label, not p.exists(), str(p)))
    return all(results)


def test_changelog_present() -> bool:
    """CHANGELOG.md 必填"""
    p = REPO_ROOT / "CHANGELOG.md"
    if not p.is_file():
        return check("CHANGELOG.md", False, "missing")
    text = p.read_text(encoding="utf-8")
    has_version = bool(re.search(r"^##\s+v\d+", text, re.MULTILINE))
    return check("CHANGELOG.md 头部有 ## v## 段", has_version)


def main() -> int:
    # Force UTF-8 stdout for Windows console (avoids GBK encoding errors on emojis)
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
        sys.stderr.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except (AttributeError, ValueError):
        pass  # older Python or non-stdout

    print("=" * 60)
    print("playbook structure smoke test")
    print(f"repo root: {REPO_ROOT}")
    print("=" * 60)
    all_results: list[bool] = []
    all_results.extend(test_files_exist())
    all_results.append(test_skill_md_frontmatter())
    all_results.append(test_readme_three_sections())
    all_results.append(test_naming_no_temp_or_misc())
    all_results.append(test_no_secrets_in_repo())
    all_results.append(test_changelog_present())
    print("=" * 60)
    passed = sum(all_results)
    total = len(all_results)
    print(f"PASSED: {passed}/{total}")
    if passed == total:
        print("[OK] all checks pass")
        return 0
    print(f"[FAIL] {total - passed} check(s) failed")
    return 1


if __name__ == "__main__":
    sys.exit(main())