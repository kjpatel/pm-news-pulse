# How Stripe built “minions”—AI coding agents that ship 1,300 PRs weekly from Slack reactions | Steve Kaliski (Stripe engineer)

**Source**: [Lenny's Newsletter](https://www.lennysnewsletter.com/p/how-stripe-built-minionsai-coding)
**Author**: Lenny Rachitsky (featuring Steve Kaliski) | **Date**: Mar 25, 2026

---

## Summary

Stripe has built "minions," AI coding agents that autonomously ship 1,300 pull requests weekly from Slack reactions, demonstrating how excellent developer experience and cloud environments unlock massive engineering velocity at scale. The system shows how AI agents can be integrated into existing workflows while handling code review and even autonomous spending through machine payments.

## Key Takeaways

- **Prioritize activation energy over execution**: Stripe's approach of allowing engineers to trigger development work with a single Slack emoji reaction removes friction and is more important than optimizing the underlying execution speed.
- **Invest in developer experience for AI agents**: Building tools with great DX for humans (cloud environments, clear abstractions, good system prompts) directly translates to better AI agent performance and productivity.
- **Scale code review through stratification**: Instead of reviewing all 1,300+ weekly agent PRs with equal rigor, implement tiered review strategies based on risk level and change scope to handle AI-generated code at scale.
- **Enable cloud-based development environments**: Stripe's use of cloud development environments allows multiple AI agents to work in parallel safely, avoiding local machine conflicts and enabling true multi-threaded AI engineering.
- **Extend agent capabilities beyond engineering teams**: Non-engineers across Stripe are starting to use minions to ship code, suggesting AI agents should be designed as accessible tools for entire organizations, not just technical teams.

## Related

- [[2026-03-10 The Org Chart Math Behind AI-Native Speed]]
- [[2026-03-16 What I Learned Building a Self-Improving Agentic System with Claude]]
- [[2026-03-07 The PM's Guide to Agent Distribution MCP Servers, CLIs, and AGENTS.md]]
