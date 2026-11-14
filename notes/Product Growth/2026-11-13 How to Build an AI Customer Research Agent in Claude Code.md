# How to Build an AI Customer Research Agent in Claude Code

**Source**: [Product Growth](https://www.news.aakashg.com/p/ai-customer-research)
**Author**: Aakash Gupta (featuring Greg Greiner) | **Date**: Nov 13, 2026

---

## Summary

Greg Greiner, former CPO of Bolt and now CEO of Woven, shows how product teams can use AI to run research conversations with every customer who drops out of the funnel, rather than the handful they can interview by hand. He also provides a Claude Code blueprint for building that outreach agent, with evals to keep its replies grounded in documentation.

## Key Takeaways

- **Send one plain-text question by email at key churn moments.** Target six moments: unfinished sign-up, mid-trial, trial ended without purchase, failed upsell conversion, usage drop, and cancellation. Ask a single open question so the customer leads rather than filling out a survey.
- **Correlate open-ended answers with later behavior.** Group replies into themes and measure each group's conversion against a baseline, as Ancestry did. This shows which issues actually move revenue, such as shipping timing (41% conversion) versus promotion-waiting (28%).
- **Build the agent with four inputs in Claude Code.** Provide a CSV of dropped-off users, a CLAUDE.md describing tone and email format, a policy file defining what the agent may and may not do, and a skill for sending. Start with Gmail MCP at low volume and move to a sender like Postmark at scale.
- **Add a groundedness eval before auto-sending replies.** Use an LLM judge to check that claims match your documentation and style. If a reply fails, regenerate it and save it as a draft for review, and feed the failure back as an input rather than as exact instructions to avoid overfitting.
- **Use email's latency to make evals practical.** Customers don't expect instant replies over email, so the eval-and-regenerate loop can run invisibly. In a live chat, the same loop would leave the user waiting for minutes.

## Related

- [[2026-11-05 The end of feature discovery as we know it.]]
- [[2026-05-22 How to Run Evals in Claude Code with Aparna Dhinakaran, Founder and CPO of Arize]]
- [[2026-09-22 Advanced evals How to find (and fix) hidden AI failures in your product]]
