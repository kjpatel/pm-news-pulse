# 🎙️ How I AI: OpenClaw for executives: Automate every 1% annoyance

**Source**: [Lenny's Newsletter](https://www.lennysnewsletter.com/p/how-i-ai-openclaw-for-executives)
**Author**: Lenny Rachitsky (featuring Ankit Maheshwari) | **Date**: Nov 23, 2026

---

## Summary

Ankit Maheshwari, CTO of Innovaccer, shows how he built a personal AI chief of staff called Jarvis on OpenClaw that handles approvals, lunch orders, coworker follow-ups, restaurant bookings, and smart home controls. His core argument is that small, frustrating tasks are the best entry points for agents, and that control, specialized agents, and strict guardrails make such a system trustworthy.

## Key Takeaways

- **Automate the bottleneck before the grand vision.** Start with one recurring, painful task, like a cron job that briefs you every four hours on items awaiting approval, and expand only after it works.
- **Apply the '1% annoyance' rule.** If a task is slightly frustrating and repeats a few times, automate it. This is how you find candidates for agents such as lunch ordering, unanswered Slack follow-ups, and home automation.
- **Split work across specialized agents once tasks get complex.** Move distinct workflows, such as voice calls, into dedicated agents with narrow scopes so persona and behavior stay consistent and orchestration stays separate from execution.
- **Invest more in agent instructions than in integrations.** Define each agent's personality, boundaries, permissions, and routing in files like soul.md, and expect more iteration on these instructions than on connecting the tools.
- **Set explicit limits for worst-case actions and optimize model costs early.** Define hard limits for high-impact approvals, such as job-role changes, before an incident occurs, and test cheaper local models for summaries, email, and cron checks while reserving frontier models for complex browser work.

## Related

- [[2026-02-25 5 OpenClaw agents run my home, finances, and code Jesse Genet]]
- [[2026-03-31 OpenClaw The complete guide to building, training, and living with your]]
- [[2026-09-02 Grok Bot vs. OpenClaw How I replaced my entire agent stack]]
