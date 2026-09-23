---
name: skill-template
description: "Distilled template for new Cherry Studio / agent skills. Use when creating any new skill that the agent should pick up automatically — provides the minimum structure (frontmatter + README + assets dir) that meets Cherry's SKILL.md scan + an honest README so a new agent can self-onboard."
---

# Skill Template — minimum viable skill

This is the **distilled** template. Reference: `D:\skills\pm-k12\` is the live, full-featured example — but **do not copy it wholesale**. Use this template, then grow.

## Start and route

1. **Read this template fully** before customizing.
2. Copy this `skill-template/` directory to `skills/<your-skill-name>/` (kebab-case, see [`NAMING.md`](../NAMING.md)).
3. Replace `name:` and `description:` in the SKILL.md frontmatter.
4. Fill in the three sections below.
5. Cherry Studio picks up any directory containing a `SKILL.md` under its scan path — no registration needed.

## When to use this template

- You're starting a new method / workflow that the agent should recognize by name.
- You want to share the method with future agents (or across machines).
- The method has **stable rules** that don't change every conversation.

## When NOT to use this template

- The method is conversation-specific or one-off → put it in `methods/<dim>/<date>_<slug>.md` instead.
- The method changes weekly → a skill is too rigid; use a `methods/` entry.
- You want to test a half-formed idea → start in `methods/<dim>/`, promote to skill later.

## Three sections every skill must have

### 1. What it is
- One paragraph: the purpose, the boundary (what's in / what's out).
- If it has a versioning story, say it here (see pm-k12 README "重点 v3.0").

### 2. How to use (start and route)
- Numbered steps or a short table — what does the agent do first?
- Include the failure modes / known issues here so the agent self-corrects.

### 3. Known pitfalls
- Bullet list, observable failure patterns.
- Distilled from real failure logs, not speculation.

## Optional sections (only if needed)

- **Customization** — how a project can override defaults without editing the skill itself (see pm-k12's `local-overrides.md` pattern).
- **Self-test** — `tests/` directory with smoke tests.

## Anti-patterns (do NOT do)

- **Don't copy pm-k12 wholesale** — its 80+ files are overkill for most skills. Use this template.
- **Don't put secrets in SKILL.md** — frontmatter is loaded by the agent.
- **Don't link to absolute Windows paths** — use repo-relative paths.
- **Don't write "see also" sections without confirming the targets exist** — broken links rot fast.
- **Don't add a CHANGELOG unless you're past v1** — premature structure.

## Customization workflow

After copying:

1. **Edit the frontmatter** (`name`, `description`) — these are how the agent finds the skill.
2. **Rewrite the "What it is"** section.
3. **List 3-5 concrete steps** in "How to use".
4. **Document 2-3 real pitfalls** you or the agent have actually hit.
5. Test: open a fresh agent session and ask it to use the skill by name.

## What "done" looks like

- [ ] frontmatter `name` is kebab-case, unique, no spaces
- [ ] frontmatter `description` includes 2-3 trigger phrases the user would naturally say
- [ ] "What it is" section is one paragraph
- [ ] "How to use" is 3-7 numbered steps
- [ ] "Known pitfalls" has at least one bullet from real experience
- [ ] No secrets, no absolute Windows paths, no broken cross-links
- [ ] Cherry Studio reloads and shows the skill in its list