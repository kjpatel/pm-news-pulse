# Skill Distillation

**Source**: [Tomasz Tunguz](https://www.tomtunguz.com/the-pi-agent-skill-distillation/)
**Author**: Tomasz Tunguz | **Date**: May 29, 2026

---

## Summary

Skill distillation is a novel technique where frontier AI models teach smaller, locally-run models how to execute specific procedures through inspectable markdown skill files, enabling efficient personal agents that retrieve and execute procedures rather than relying on model weights or retrieval-augmented generation.

## Key Takeaways

- **Use markdown skill files as the bridge** between frontier and local models—write procedures as SKILL.md files that frontier models author and refine, allowing smaller models to execute without needing to understand the underlying logic
- **Build a three-layer agent architecture** with QMD knowledge base (procedural playbooks), Skills (atomic SKILL.md files with frontier-written evaluations), and Agent Loop (local execution via APIs and MCPs) to create an inspectable, versionable operating system
- **Automate skill generation nightly** by analyzing historical logs to identify which new skills should be created, letting the system continuously learn and adapt to emerging work patterns
- **Switch between student models quarterly** based on cost-efficiency since procedures are decoupled from model weights—skill distillation makes your agent resilient to model changes and price fluctuations

## Related

- [[2026-03-30 How to turn Claude Code into your personal life operating system Hilary Gridley]]
- [[2026-05-02 🧠 Community Wisdom Claude Code tips for ADHD users, resources for managing up,]]
- [[2026-04-01 OpenAI's Codex is the Best Way to Use ChatGPT A PM's Guide]]
