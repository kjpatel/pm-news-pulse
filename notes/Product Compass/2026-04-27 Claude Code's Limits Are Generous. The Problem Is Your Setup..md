# Claude Code's Limits Are Generous. The Problem Is Your Setup.

**Source**: [Product Compass](https://www.productcompass.pm/p/stop-hitting-claude-code-limits)
**Author**: Pawel Huryn | **Date**: Apr 27, 2026

---

## Summary

Claude Code's generous limits are often wasted due to inefficient setup; this article identifies four root causes of token waste—cache misses, context bloat, wrong model selection, and poor input formats—and provides specific optimization techniques to reduce costs by 60-90%.

## Key Takeaways

- **Protect the prompt cache** by locking tools and models at session start; never add/remove MCP servers or switch models mid-session, as this invalidates the cache and forces expensive full re-reads.
- **Disable 1M context and use 200K default** with auto-compact set to 80%; compact early before auto-triggers fire, and use subagents to isolate context and parallelize cheaper models for mechanical tasks.
- **Route model selection strategically** by starting with Sonnet sessions for scoped work or Opus sessions with delegation; set effort levels per-prompt (not session-wide) and route to cheaper providers like GLM-5.1 when hitting subscription limits.
- **Replace expensive inputs** by swapping screenshots for agent-browser (90% token savings), using file paths instead of grep, and compressing tool output with CLI proxies like rtk-ai/rtk.
- **Implement session management discipline** through /compact at 50%, /clear between unrelated work, /rewind for mistakes, and spec-based prompts with exact file paths and constraints to eliminate vague requests.

## Related

- [[2026-04-23 Claude Cowork Now Runs Any LLM. Test It Free.]]
- [[2026-03-31 How to Turn Claude Code into an Operating System with Carl Vellotti]]
- [[2026-02-19 Head of Claude Code What happens after coding is solved Boris Cherny]]
