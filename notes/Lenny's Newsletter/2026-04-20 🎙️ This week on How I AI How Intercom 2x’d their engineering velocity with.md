# 🎙️ This week on How I AI: How Intercom 2x’d their engineering velocity with Claude Code

**Source**: [Lenny's Newsletter](https://www.lennysnewsletter.com/p/this-week-on-how-i-ai-how-intercom)
**Author**: Lenny Rachitsky (featuring Brian Scanlan) | **Date**: Apr 20, 2026

---

## Summary

Intercom doubled their engineering velocity in 9 months by treating their engineering org like a product, implementing deep telemetry, building custom Claude Code skills with guardrails, and fostering a culture of permission. The key insight is that AI magnifies existing strengths and weaknesses—strong fundamentals like CI/CD and test coverage are prerequisites for meaningful velocity gains.

## Key Takeaways

- **Instrument everything like a product.** Track skill invocations, store anonymized sessions, and build dashboards showing engineer performance. You can't improve what you don't measure, and visibility into AI adoption is essential for scaling.
- **Fix fundamentals before adding velocity.** Ensure mature CI/CD, comprehensive test coverage, and high-trust culture exist first. AI magnifies both strengths and weaknesses—a broken deployment pipeline will just ship broken code faster.
- **Use custom skills to enforce quality at creation.** Build guardrails like PR description requirements that make the golden path the only path, preventing low-quality shortcuts at the point of code generation.
- **Give permission and take accountability as a leader.** Remove activation energy for experimentation by telling engineers they can connect AI to any tool. Technical leadership means enabling risk-taking while owning the consequences.
- **Design products to be agent-friendly or customers will build workarounds.** Build CLIs and APIs that agents can autonomously use; otherwise, customers' agents will brute-force your UI, burn tokens, and eventually abandon your product entirely.

## Related

- [[2026-04-06 I gave Claude Code our entire codebase. Our customers noticed. Al Chen (Galileo)]]
- [[2026-03-25 How Stripe built "minions"—AI coding agents that ship 1,300 PRs weekly from]]
- [[2026-04-13 Claude Cowork 101 How to automate your workday without touching code JJ Englert]]
