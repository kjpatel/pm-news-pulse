# The AI Preflight Check

**Source**: [Tomasz Tunguz](https://www.tomtunguz.com/the-ai-preflight-check/)
**Author**: Tomasz Tunguz | **Date**: Jul 08, 2026

---

## Summary

Tomasz describes a memory architecture for AI agents that uses preflight retrieval to load relevant skills before execution, with a watchdog system that continuously improves the skill library through overnight asynchronous inference.

## Key Takeaways

- **Implement preflight retrieval** - Have your agent inspect a skills library and load only relevant skills into the context window before executing tasks, rather than relying solely on context size.
- **Route tasks intelligently** - Direct routine tasks to local models (which handles ~80% of work) and only route genuinely hard tasks to frontier models to optimize cost and latency.
- **Build a self-improving system** - Use a watchdog to monitor skill usage, decisions, and success rates overnight, then automatically refactor skills and convert repetitive LLM work into deterministic code.
- **Convert skills to versioned artifacts** - Consolidate memory by creating named, versioned workflow files that serve as reusable tools, enabling the agent to learn which skills work best over time.

## Related

- [[2026-05-29 Skill Distillation]]
- [[2026-06-25 Full Sail on Asynchronous Inference]]
- [[2026-03-07 The PM's Guide to Agent Distribution MCP Servers, CLIs, and AGENTS.md]]
