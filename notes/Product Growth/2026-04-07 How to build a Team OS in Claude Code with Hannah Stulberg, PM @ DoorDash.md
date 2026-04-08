# How to build a Team OS in Claude Code with Hannah Stulberg, PM @ DoorDash

**Source**: [Product Growth](https://www.news.aakashg.com/p/claude-code-team-os)
**Author**: Aakash Gupta (featuring Hannah Stulberg) | **Date**: Apr 07, 2026

---

## Summary

Hannah Stulberg from DoorDash shares how to build a Team Operating System in Claude Code that allows product teams to scale impact by centralizing knowledge in a structured GitHub repo with nested indexes and optimized context management.

## Key Takeaways

- **Create a root Claude MD file** that contains only three elements: a doc index map, team roster with handles, and key Slack channels—keeping it to one page to avoid wasting context on unnecessary information.
- **Implement nested Claude MD indexes** for every major folder to enable Claude to navigate directly to relevant files, reducing token consumption from explore agents and leaving more context for reasoning.
- **Organize your repo in three tiers** of context efficiency: Tier 1 (always-loaded root info under 500 tokens), Tier 2 (folder-level indexes loaded on query), and Tier 3 (content files loaded on demand) to maximize thinking room.
- **Structure folders by function and product area** with clear ownership models so team members can self-serve answers without going through the PM, transforming the PM from a bottleneck to a knowledge architect.
- **Use shared agents, commands, and skills** in a .claude/ folder that the entire team leverages consistently, enabling non-technical team members to work productively in the repo without coding experience.

## Related

- [[2026-03-30 How to Turn Claude Code into an Operating System with Carl Vellotti]]
- [[2026-02-21 Claude Cowork The Ultimate Guide for PMs]]
- [[2026-03-08 A Guide to Claude Code for PMs From Cowork to Code]]
