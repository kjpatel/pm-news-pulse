# What an AI-Native Product Team Actually Looks Like at Salesforce

**Source**: [Product Growth](https://www.news.aakashg.com/p/salesforce-ai-native-product-team)
**Author**: Aakash Gupta (featuring Jayesh Govindarajan) | **Date**: Nov 03, 2026

---

## Summary

Salesforce's head of AI engineering, Jayesh Govindarajan, argues that AI features need a continuous lifecycle (ADLC) instead of the linear SDLC because models and data drift, so agents must be constantly re-evaluated and rebuilt. He also shows how a large org can become AI-native through tool choice, eval-first practices, feedback loops, and hiring for agency and skepticism.

## Key Takeaways

- **Budget for evals and observability before the build:** AI features need continual rebuilding as models and context change, so plan maintenance costs and evaluation infrastructure up front.
- **Grade the agent before you trust it:** Define how each eval scores the agent's behavior, and bring in domain subject-matter experts to write evals instead of relying on generic ones.
- **Decide where determinism is required:** Use tools like Agent Script to lock down outputs that must be consistent (such as pipeline figures), and reserve LLM reasoning for places where variability is acceptable.
- **Let teams choose their AI tools:** Avoid mandating one tool; let teams pick options like Codex, Claude Code, or Cursor, and spread the practices of the best performers.
- **Route field feedback into the roadmap:** Have forward deployed engineers post tagged paper cuts and feature requests to one channel, and ask whether any customer-specific build should become a platform feature.
- **Prove value with one win, then go wide:** Pick a single area where the agent clearly delivers results, then expand the ADLC across the organization.

## Related

- [[2026-10-15 How PM Work Is Changing in the AI Era]]
- [[2026-09-22 Advanced evals How to find (and fix) hidden AI failures in your product]]
- [[2026-04-29 The AI Product Sense Interview Guide]]
