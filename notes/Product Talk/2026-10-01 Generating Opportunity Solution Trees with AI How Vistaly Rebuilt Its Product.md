# Generating Opportunity Solution Trees with AI: How Vistaly Rebuilt Its Product Around Interview Synthesis, Evals, and Repair Loops

**Source**: [Product Talk](https://www.producttalk.org/generating-opportunity-solution-trees-with-ai-how-vistaly-rebuilt-its-product-around-interview-synthesis-evals-and-repair-loops/)
**Author**: Teresa Torres (featuring Matt O'Connell, CP Dehli, and Steve Klein) | **Date**: Oct 01, 2026

---

## Summary

Vistaly rebuilt its opportunity solution tree software around AI-driven interview synthesis, arguing that the real competition is shallow synthesis that never happened, not faster manual synthesis. The hard problems turned out to be layered analysis errors, evals, orchestration-based repair loops, and helping users understand what changed rather than output quality alone.

## Key Takeaways

- **Build evals and a cheap pre-filter before an LLM judge.** Use simple code assertions, such as a node having too many children, to catch obvious failures before spending money on an LLM-as-a-judge, and expect to iterate on judges that are hard to calibrate.
- **Fix recurring errors in orchestration, not just the prompt.** When a prompt cannot balance two opposing error modes, add an agentic repair loop that checks and corrects the output, then promote the eval that exposed the problem into a production guardrail.
- **Validate inputs at the bottom layer of your analysis.** Screen uploaded interviews for sales demos, stakeholder meetings, and synthetic transcripts, because bad snapshots at the base corrupt every layer built on top of them.
- **Have the AI log semantic moves instead of diffing outputs at the end.** Teach the agent the rules of the game (merge, move, reframe) so it records meaningful change sets, since multiple valid change sets can exist for the same input and output pair.
- **Design for generate-then-correct rather than step-by-step collaboration.** Give users a complete first draft and an easy way to correct it, because users want the answer first and then the ability to fix it, not a guided chat through every insight.

## Related

- [[2026-09-22 Advanced evals How to find (and fix) hidden AI failures in your product]]
- [[2026-03-20 Evals are the new PRD. Here is the playbook with the CEO of the leader in the]]
- [[2026-02-13 How to Do AI-Powered Discovery (Step-by-Step with Live Demo) Caitlin Sullivan]]
