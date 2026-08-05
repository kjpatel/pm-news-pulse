# Build an AI code review bot in 30 minutes with Vercel Eve

**Source**: [Lenny's Newsletter](https://www.lennysnewsletter.com/p/build-an-ai-code-review-bot-in-30)
**Author**: Lenny Rachitsky (featuring Claire Vo) | **Date**: Aug 05, 2026

---

## Summary

Learn how to build an AI-powered PR review bot (Merge Mommy) using Vercel Eve that automatically scores pull requests across six risk dimensions, auto-approves low-risk changes, and escalates to humans for review—solving the PR bottleneck created by AI-generated code.

## Key Takeaways

- **Implement risk scoring** Use a six-component model (blast radius, reversibility, data security, ops impact, verification gap, change surface) to automatically categorize PRs and reduce manual review burden.
- **Leverage AI agents for bottlenecks** Deploy Vercel Eve agents in Slack and GitHub to handle repetitive review tasks, enabling faster approval cycles while maintaining audit trails for SOC 2 compliance.
- **Use browser automation** Employ Chrome browser use within Codex to automate setup processes like GitHub app configuration, reducing manual configuration work to zero.
- **Maintain compliance with automation** Auto-approved PRs can be SOC 2 compliant by ensuring the process is auditable, queryable, and aligned with your risk policy—no manual review required for low-risk changes.
- **Build faster with guided iterations** Use a single Codex prompt with steering turns to develop full agent functionality in one session, proving that complex automation doesn't require extensive engineering.

## Related

- [[2026-04-20 How Intercom 2x'd their engineering velocity in 9 months with Claude Code Brian]]
- [[2026-06-17 How to design AI agent loops schedules, goals, and subagents in Claude Code and]]
- [[2026-07-08 What a harness is and how to build one with Claude Agent SDK]]
