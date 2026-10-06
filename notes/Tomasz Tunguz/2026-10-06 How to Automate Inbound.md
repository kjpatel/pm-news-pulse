# How to Automate Inbound

**Source**: [Tomasz Tunguz](https://tomtunguz.com/how-to-automate-inbound/)
**Author**: Tomasz Tunguz | **Date**: Oct 06, 2026

---

## Summary

Vercel's COO Jeanne DeWitt Grosser explains how to build production inbound sales agents by starting with deterministic rules, human-in-the-loop validation, and gradually shifting from complex prompts to explicit rule-based logic with AI handling only judgment calls.

## Key Takeaways

- **Start with a single engineer** spending 20% time on a well-scoped, deterministic problem (research, qualification, drafting) rather than attempting to automate the entire sales process at once.
- **Implement human-in-the-loop validation early** by having your best SDR review 100% of the agent's first outputs for ~6 weeks, then transition to random sampling once competency is demonstrated.
- **Separate rules from judgment** by encoding explicit deterministic rules (14 in Vercel's case) in code and reserving the model only for nuanced decisions that require human-like reasoning.
- **Build a monitoring agent** that watches for rule violations and either fixes exceptions or escalates them, ensuring consistent agent behavior within your company's constraints.
- **Redeploy freed-up humans to higher-value work** by moving SDRs away from email management into outbound conversations, where human judgment and relationship-building create more value.

## Related

- [[2026-02-26 Is AI Doing Less & Less]]
- [[2026-09-15 When Inbound Sells Itself]]
- [[2026-05-26 Agent Gravity Who's Running Your Agents]]
