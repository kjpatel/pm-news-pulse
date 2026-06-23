# 🎙️ How I AI: How to write AI agent loops in Claude Code and Codex + How Claude Mythos found a 15-year-old bug in Mozilla Firefox

**Source**: [Lenny's Newsletter](https://www.lennysnewsletter.com/p/how-i-ai-how-to-write-ai-agent-loops)
**Author**: Lenny Rachitsky (featuring Claire Vo and Brian Grinstead) | **Date**: Jun 22, 2026

---

## Summary

This episode features two practical deep dives into AI agent loops: Claire demonstrates how to design and build automated loops in Claude Code and Codex (from simple scheduled tasks to complex self-spawning subagents), while Brian Grinstead explains how Mozilla used custom AI agent harnesses to find and fix 423 Firefox security bugs in one month.

## Key Takeaways

- **Define loops as job descriptions.** Treat agent loops like onboarding an employee—specify what to check, how often, what output you want, and who to contact when something's wrong. A clear job description becomes a clear loop prompt.
- **Use goal loops with explicit success criteria.** Goal loops are most powerful but most misused; vague success criteria cause agents to loop forever burning tokens. Let Codex write goals using vendor guides, and validate outcomes precisely.
- **Build verification loops to eliminate false positives.** Mozilla's two-stage verification (trigger actual crash + verifier subagent) makes agent output ship-ready. Apply this pattern to security, performance, and tech debt work.
- **Spawn subagents to handle parallel work.** The ceiling on loop automation is how well you define the job, not engineering complexity. Use subagents to parallelize verification and specialized tasks like skills validation.
- **Score and prioritize your codebase before pointing agents at it.** Use a simple LLM judge to score files on likelihood and accessibility; this prevents wasted agent cycles and makes outputs more targeted and valuable.

## Related

- [[2026-06-17 How to design AI agent loops schedules, goals, and subagents in Claude Code and]]
- [[2026-06-22 How Claude Mythos found a 15-year-old bug in Mozilla Firefox]]
- [[2026-04-30 How to Build a Full AI Dev Team in Claude Code Guide from Google PM Gabor Meyer]]
