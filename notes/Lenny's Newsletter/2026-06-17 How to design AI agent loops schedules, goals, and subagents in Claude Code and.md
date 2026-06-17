# How to design AI agent loops: schedules, goals, and subagents in Claude Code and Codex

**Source**: [Lenny's Newsletter](https://www.lennysnewsletter.com/p/how-to-design-ai-agent-loops-schedules)
**Author**: Lenny Rachitsky (featuring Claire Vo) | **Date**: Jun 17, 2026

---

## Summary

This episode provides a comprehensive guide to designing AI agent loops in Claude Code and Codex, covering the four loop types (heartbeat, cron, hook, goal), their use cases, and the five essential components every effective loop needs before production.

## Key Takeaways

- **Understand loop types**: Master the four automation patterns—heartbeat (continuous), cron (scheduled), hook (event-triggered), and goal-based (outcome-driven)—to pick the right one for your workflow rather than defaulting to complexity.
- **Build loops with five foundations**: Every production loop requires work trees (task breakdown), skills (agent capabilities), plugins/connectors (external integrations), subagents (delegation), and state tracking (memory between runs).
- **Use the employee onboarding framework**: Design loops by asking what instructions you'd give a new employee—this mental model clarifies scope, prevents over-engineering, and identifies where subagents should spawn.
- **Watch for cost signals early**: Goal-based loops are token-intensive; watch for loops that validate their own output or spawn excessive subagents, as these are early warnings of runaway costs before production deployment.
- **Implement scheduled loops strategically**: Cron loops like the PR reviewer example (running at 10:15 a.m.) show how to build self-aware agents that know when to run and when to delegate to subagents for specific tasks.

## Related

- [[2026-03-07 The PM's Guide to Agent Distribution MCP Servers, CLIs, and AGENTS.md]]
- [[2026-04-30 How to Build a Full AI Dev Team in Claude Code Guide from Google PM Gabor Meyer]]
- [[2026-05-08 Securing the Agentic Enterprise]]
