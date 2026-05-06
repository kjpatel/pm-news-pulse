# Optimizing Software Factories

**Source**: [Tomasz Tunguz](https://www.tomtunguz.com/optimizing-software-factories/)
**Author**: Tomasz Tunguz | **Date**: May 05, 2026

---

## Summary

As startups increasingly replace engineers with AI agents, the critical trade-off is not throughput but resiliency—concentrating orchestration knowledge in too few people creates fragile systems that fail catastrophically when those people leave.

## Key Takeaways

- **Apply manufacturing principles**: Run engineering teams at 70-90% utilization, not 100%, to maintain system robustness and avoid cascading failures when key people depart.
- **Map your AI/labor ratio intentionally**: Decide between 10/90 (traditional hierarchy), 50/50 (hybrid with architect roles), or 90/10 (minimal humans) based on your resiliency requirements, not just cost optimization.
- **Prioritize institutional memory distribution**: In agent-heavy setups, the loss of one person means losing a third of the knowledge that trains and validates your agent fleet—design redundancy into prompt engineering and agent oversight.
- **Rethink org structure around agent orchestration**: As manager span of control widens due to autonomous agents, focus on identifying and distributing the orchestration knowledge that currently lives in a few heads to prevent single points of failure.

## Related

- [[2026-03-25 How Stripe built "minions"—AI coding agents that ship 1,300 PRs weekly from]]
- [[2026-04-30 How to Build a Full AI Dev Team in Claude Code Guide from Google PM Gabor Meyer]]
- [[2026-03-10 The Org Chart Math Behind AI-Native Speed]]
