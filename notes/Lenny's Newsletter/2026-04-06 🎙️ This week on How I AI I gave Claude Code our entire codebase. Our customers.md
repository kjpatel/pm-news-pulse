# 🎙️ This week on How I AI: I gave Claude Code our entire codebase. Our customers noticed.

**Source**: [Lenny's Newsletter](https://www.lennysnewsletter.com/p/this-week-on-how-i-ai-i-gave-claude)
**Author**: Lenny Rachitsky (featuring Al Chen) | **Date**: Apr 06, 2026

---

## Summary

Al Chen, a field engineer at Galileo, demonstrates how to leverage Claude Code to query an entire codebase across 15 repositories, combined with Confluence and Slack data, to provide enterprise customers with accurate technical answers without relying on outdated documentation or constant engineering interruptions.

## Key Takeaways

- **Automate repository syncing** by writing a daily script (using Claude Code itself) that pulls the latest main branch from all repositories each morning, ensuring you're always querying current code rather than stale information.
- **Maintain a customer-specific context page** documenting each enterprise customer's unique deployment requirements, security configurations, and infrastructure constraints, then reference it in Claude Code commands to generate tailored answers instead of generic responses.
- **Use code as your source of truth** by querying actual repositories directly instead of relying on official documentation, which often can't answer detailed technical questions about how services interact, feature implementations, and deployment specifics.
- **Convert support conversations into knowledge articles** automatically using tools like Pylon to transform Slack threads into help articles that are more current and in-depth than formal docs without requiring PR reviews.
- **Add human judgment to AI outputs** by proofreading responses, removing AI-specific phrases, condensing verbose answers, and validating complex technical solutions with engineering when needed to ensure accuracy and customer-appropriate tone.

## Related

- [[2026-04-06 I gave Claude Code our entire codebase. Our customers noticed. Al Chen (Galileo)]]
- [[2026-03-30 How to turn Claude Code into your personal life operating system Hilary Gridley]]
- [[2026-03-25 How Stripe built "minions"—AI coding agents that ship 1,300 PRs weekly from]]
