# A FAANG PM's Guide to Practical AI Evals

**Source**: [Product Growth](https://www.news.aakashg.com/p/practical-ai-evals)
**Author**: Aakash Gupta (featuring Mahesh Yadav) | **Date**: Nov 24, 2026

---

## Summary

AI evals have become a core PM skill, and this guide lays out a four-step process (define good, set the bar, scale with LLM judges, keep humans grading) for building evals that actually work. It also explains how the PM and engineering roles split ownership of evals and what that skill could mean for compensation.

## Key Takeaways

- **Define 'good' as yes/no tests.** Break helpful, honest, and harmless into specific, binary checks (e.g., 'did it redact only the needed words?'), and use code-based checks wherever code can verify the output.
- **Set a bar between competitor performance and the realistic ceiling.** Start with a floor at your competitor's level, aim for a bar in the middle, and cap the ceiling near 70-80%. If you land below the bar, narrow the product to the slices it handles correctly about 80% of the time.
- **Train an LLM judge against human experts.** Use human experts first, then build a judge that agrees with them 70-80% of the time, and avoid chasing near-perfect agreement, which can hide problems.
- **Keep sampling human grading after launch.** Have humans review a regular sample of judge outputs (for large systems, perhaps 200-1,000 per week) to catch drift.
- **Own the metrics and the eval questions, and let engineering build the pipeline.** As the PM, define what good means for users, set the launch bar and stage gates, check the judge, and own weekly cost reviews, while engineers build judges and hill-climb quality and cost.

## Related

- [[2026-09-22 Advanced evals How to find (and fix) hidden AI failures in your product]]
- [[2026-03-20 Evals are the new PRD. Here is the playbook with the CEO of the leader in the]]
- [[2026-02-19 AI Evals Explained Simply by Ankit Shukla]]
