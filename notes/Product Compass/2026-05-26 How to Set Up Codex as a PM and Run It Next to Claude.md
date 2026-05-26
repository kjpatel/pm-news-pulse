# How to Set Up Codex as a PM and Run It Next to Claude

**Source**: [Product Compass](https://www.productcompass.pm/p/codex-setup-for-pms)
**Author**: Pawel Huryn | **Date**: May 26, 2026

---

## Summary

This guide teaches product managers how to set up and run OpenAI's Codex alongside Claude Code on the same repository, leveraging Codex's growing user base (4M weekly active users) and unique features like manual session compaction and visual diffs to create a complementary dual-runtime workflow.

## Key Takeaways

- **Install both Codex surfaces** — Set up the Codex desktop app for long chat sessions and manual compaction, plus the Codex VS Code extension to access hidden dot folders (.agents, .codex) that the app's file picker hides.
- **Create a single source of truth** — Bridge AGENTS.md and CLAUDE.md by making AGENTS.md a pointer to CLAUDE.md, ensuring both Codex and Claude Code follow one canonical document that serves as the agent's memory of how you work.
- **Use progressive disclosure in CLAUDE.md** — Keep the core file lean with only essential sections (Communication, Strategy, Project Structure, Workflow), then link to deeper files (strategy.md, knowledge/INDEX.md) that load on-demand to avoid context bloat.
- **Leverage different perspectives** — Hand code or prompts to whichever runtime didn't write it first, since different models catch different mistakes and provide complementary feedback for higher-quality outputs.
- **Install Plugins for instant integrations** — Use Codex's one-click Plugins panel to connect Gmail, Linear, Jira, and Slack, giving both runtimes access to shared app connections and project skills without manual configuration.

## Related

- [[2026-03-31 The Claude Code Job Search Operating System]]
- [[2026-03-30 How to Turn Claude Code into an Operating System with Carl Vellotti]]
- [[2026-05-20 PM Brain OS The Second Brain for Product Managers, Made of Markdown]]
