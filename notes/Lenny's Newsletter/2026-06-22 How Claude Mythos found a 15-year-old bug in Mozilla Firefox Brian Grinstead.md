# How Claude Mythos found a 15-year-old bug in Mozilla Firefox | Brian Grinstead

**Source**: [Lenny's Newsletter](https://www.lennysnewsletter.com/p/how-claude-mythos-found-a-15-year)
**Author**: Lenny Rachitsky (featuring Brian Grinstead) | **Date**: Jun 22, 2026

---

## Summary

Mozilla engineer Brian Grinstead demonstrates how a custom agentic bug-finding pipeline using Claude Mythos discovered a record number of security vulnerabilities in Firefox, including a 15-year-old bug, by combining intelligent file prioritization, goal-loop patterns, and human verification rather than relying solely on model capability.

## Key Takeaways

- **Build a basic harness first**: Create a bug-finding pipeline using Claude Code or Codex with a single prompt and the -p flag—no SDK required—before investing in complex infrastructure.
- **Prioritize files with an LLM judge**: Use a verifier subagent to score and rank files before spending compute, preventing wasteful analysis of the entire codebase at once.
- **Implement goal loops with clear signals**: Give agents tightly scoped problems with explicit pass/fail criteria and let them retry far beyond where humans would quit to maximize bug discovery.
- **Split credit between model and harness**: Recognize that the harness and pipeline logic deserve ~50% of the credit alongside the LLM—optimize both systematically rather than expecting the model alone to solve problems.
- **Keep humans in the verification loop**: Have humans review all AI-generated patches before shipping; use verifier subagents to catch false positives and ensure patches actually fix the stated problem.

## Related

- [[2026-06-15 Anthropic's Safety Superpower]]
- [[2026-04-14 Your .claude Folder Is a Production Agent]]
- [[2026-05-22 How to Run Evals in Claude Code with Aparna Dhinakaran, Founder and CPO of Arize]]
