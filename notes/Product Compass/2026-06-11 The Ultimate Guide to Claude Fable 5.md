# The Ultimate Guide to Claude Fable 5

**Source**: [Product Compass](https://www.productcompass.pm/p/claude-fable-5-guide)
**Author**: Pawel Huryn | **Date**: Jun 11, 2026

---

## Summary

Fable 5 is Anthropic's new general-access model with frontier-level capabilities that introduces mandatory thinking, safeguard routing, and demonstrated 'agentic judgment' that audits its own behavior—requiring teams to rethink their prompting, effort tuning, and workflow architecture.

## Key Takeaways

- **Default effort to 'high'** rather than max: experiments show max effort triples response time without improving correctness on most tasks, making high the practical baseline for balancing speed and quality.
- **Budget 3 seconds for startup latency** when migrating from Opus: Fable takes 3+ seconds longer to start responding but delivers denser, more token-efficient outputs that often finish faster overall despite the pause.
- **Prepare for invisible safeguard routing** on ~5% of queries: requests touching security, healthcare, or biotech will silently route to Opus 4.8; use the `/security-review` command for supported security work instead of fighting the classifier.
- **Audit your CLAUDE.md and prompt rules before migration**: Fable's self-auditing behavior means it will flag contradictions in your own quality gates that weaker models missed—run the provided audit prompt to catch these conflicts.
- **Plan team testing during the June 22 API window**: Subscription surfaces (Claude Code, Cowork) have early access, but API-only teams cannot access Fable until June 22, and temperature/thinking-off configs will break existing pipelines.

## Related

- [[2026-06-09 Claude Fable 5 review what the new Mythos model gets right (and very wrong)]]
- [[2026-04-23 How Anthropic's product team moves faster than anyone else Cat Wu (Head of]]
- [[2026-05-28 Claude Opus 4.8 is here. Is it as good as they say]]
