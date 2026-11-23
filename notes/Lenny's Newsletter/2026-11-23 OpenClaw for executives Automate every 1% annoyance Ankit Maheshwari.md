# OpenClaw for executives: Automate every 1% annoyance | Ankit Maheshwari (Innovaccer)

**Source**: [Lenny's Newsletter](https://www.lennysnewsletter.com/p/openclaw-for-executives-automate)
**Author**: Lenny Rachitsky (featuring Ankit Maheshwari) | **Date**: Nov 23, 2026

---

## Summary

CTO Ankit Maheshwari shows how he built an OpenClaw-based assistant, "Jarvis", on a Mac Mini that began by clearing his work approvals and expanded into personal tasks like ordering lunch, booking reservations, and controlling his smart home. He argues that well-scoped subagents, clear guardrails, and automating small daily annoyances make personal AI agents trustworthy, and he is testing whether a cheaper local model can replace his $500-to-$600-a-month Anthropic bill.

## Key Takeaways

- **Start automation with the bottleneck you feel most.** Maheshwari began by automating the approvals that were slowing him down at work, then expanded the system to other tasks once it proved reliable.
- **Split agents into well-scoped subagents instead of one global agent.** A single agent hallucinated across personas, so he used separate subagents (such as a health coach, email triage, and a master soul file) for clearer behavior.
- **Apply the 1% annoyance rule to pick what to automate next.** Look for small, recurring frictions like ordering food, booking restaurants, or adjusting the AC, since each one saves time and builds trust in the system.
- **Build guardrails before giving an agent real-world actions.** Define what the agent can do on its own and what needs confirmation, and test those limits mid-task, since trustworthiness depends on these boundaries.
- **Benchmark a local model against your current API bill before switching.** Maheshwari is pressure-testing GLM 5.3 Flash to see which tasks it can handle and whether it can meaningfully cut recurring model costs.

## Related

- [[2026-03-17 The Complete Guide to OpenClaw for PMs [EXCLUSIVE]]]
- [[2026-04-01 Listen OpenClaw A power-user's guide to the most powerful personal AI tool]]
- [[2026-02-25 5 OpenClaw agents run my home, finances, and code Jesse Genet]]
