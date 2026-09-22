# Advanced evals: How to find (and fix) hidden AI failures in your product

**Source**: [Lenny's Newsletter](https://www.lennysnewsletter.com/p/advanced-evals-how-to-find-and-fix)
**Author**: Lenny Rachitsky (featuring Hamel Husain and Shreya Shankar) | **Date**: Sep 22, 2026

---

## Summary

Error discovery—identifying which AI failures are worth measuring—is the critical first step in building effective evals that most teams skip, and this post shows how to use a three-step process with coding agents to find the failures that actually matter to your product.

## Key Takeaways

- **Prioritize error discovery over metrics**: Review real user traces first to understand what "good" looks like in your specific context before writing automated metrics, otherwise you'll measure the wrong things or measure them poorly.
- **Use human judgment with agent assistance**: Have a person review a diverse sample of 20-50 traces first to define success criteria and spot context-dependent failures, then dispatch a coding agent to find similar issues at scale—not the other way around.
- **Watch for criteria drift**: Your definition of product success often only becomes clear after reviewing actual failure examples, so validate your assumptions with real data before automating error detection across your entire system.
- **Make error discovery scalable**: Use a free coding agent plugin to automate the labor-intensive parts of reviewing traces (pattern matching, contradiction detection), which keeps this critical step from feeling too slow to actually do in practice.

## Related

- [[2026-05-22 How to Run Evals in Claude Code with Aparna Dhinakaran, Founder and CPO of Arize]]
- [[2026-07-28 How to Build Frontier-Lab Quality Evals with Daniel McKinnon, ex-PM at Meta]]
- [[2026-03-20 Evals are the new PRD. Here is the playbook with the CEO of the leader in the]]
