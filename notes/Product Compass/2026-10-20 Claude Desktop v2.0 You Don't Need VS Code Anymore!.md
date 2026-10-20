# Claude Desktop v2.0: You Don't Need VS Code Anymore!

**Source**: [Product Compass](https://www.productcompass.pm/p/claude-desktop-code-tab)
**Author**: Pawel Huryn | **Date**: Oct 20, 2026

---

## Summary

Pawel Huryn argues that the rebuilt Claude Desktop's Code tab now replaces VS Code for Product Managers, offering the same agentic building capabilities behind a friendlier interface. He explains why Cowork falls short for this work and walks through setup, permissions, model choice, and connectors.

## Key Takeaways

- **Move agentic PM work to the Code tab instead of VS Code:** It provides Claude Code's capabilities (prototyping, agentic systems, automation) in a user-friendly interface, without terminal-only setup friction.
- **Use Cowork for chat-style tasks, not project building:** Cowork can't run and preview apps, define project-specific skills, add project-scoped MCP connections, or guardrails, and it doesn't support AGENTS.md, so it isn't interoperable with other agents like Codex.
- **Organize every project in a dedicated folder with an AGENTS.md:** Folders hold project-specific instructions, knowledge, skills, and settings, and an AGENTS.md file lets other agents work on the same project.
- **Default to Auto permission mode and High effort:** Auto mode evaluates each action with an independent agent, and Anthropic's study showed manual approval prompts are often rubber-stamped. Use Haiku 5.5 for most work, Sonnet 5.5 for simple subagent tasks, and Opus 5.5 at xhigh effort for the hardest strategic work.
- **Keep the skill and connector footprint lean:** Each installed skill's description loads into the context window, so install only what you need. Restrict connector permissions per tool, and scope custom MCP servers to individual projects when they shouldn't be global.

## Related

- [[2026-02-21 Claude Cowork The Ultimate Guide for PMs]]
- [[2026-05-12 Claude Code for PMs The Beginner's Guide]]
- [[2026-05-26 How to Set Up Codex as a PM and Run It Next to Claude]]
