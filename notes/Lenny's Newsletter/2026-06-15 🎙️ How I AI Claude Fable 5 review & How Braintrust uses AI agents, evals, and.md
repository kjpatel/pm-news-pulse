# 🎙️ How I AI: Claude Fable 5 review & How Braintrust uses AI agents, evals, and CI to ship better software

**Source**: [Lenny's Newsletter](https://www.lennysnewsletter.com/p/how-i-ai-claude-fable-5-review-and)
**Author**: Lenny Rachitsky | **Date**: Jun 15, 2026

---

## Summary

This episode reviews Claude Fable 5's strengths and weaknesses across real-world tasks, and explores how Braintrust uses AI agents, evals, and CI/CD practices to ship higher-quality software faster.

## Key Takeaways

- **Match model intelligence to task complexity** — Use Fable 5 for hard technical problems, vision tasks, and long-horizon work, but deploy cheaper models like Sonnet or Opus for specs, design, and front-end work to save on tokens and get better outputs.
- **Define success with evals, not implementation** — Treat evals as the modern PRD by specifying concrete test cases and scoring functions that quantify what success looks like, allowing AI agents to autonomously improve toward measurable outcomes.
- **Push the agent line higher by building smart integrations** — Identify tasks that feel like they need human judgment but can actually run below the agent line; expand what agents handle autonomously through better skills and integrations.
- **Run practical quality checks continuously** — AI agents maintain consistent focus and run every benchmark without skipping tedious tests, achieving higher practical quality than human engineers who lose context and skip rigorous validation over time.
- **Use four to six foreground agents simultaneously** — Match your agent concurrency to human context-switching limits by running isolated agents on separate problems, with each agent having its own environment and production-scale data access.

## Related

- [[2026-06-15 Anthropic's Safety Superpower]]
- [[2026-06-11 The Ultimate Guide to Claude Fable 5]]
- [[2026-04-23 How Anthropic's product team moves faster than anyone else]]
