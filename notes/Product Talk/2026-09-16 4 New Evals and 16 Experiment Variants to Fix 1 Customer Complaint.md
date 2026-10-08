# 4 New Evals and 16 Experiment Variants to Fix 1 Customer Complaint

**Source**: [Product Talk](https://www.producttalk.org/4-new-evals-and-16-experiment-variants/)
**Author**: Teresa Torres | **Date**: Sep 16, 2026

---

## Summary

Teresa Torres shows how fixing one customer complaint about flat, unstructured opportunities in an AI-generated opportunity solution tree required building measurement first. She used code-assertion and LLM-as-a-judge evals, calibrated against her own labels, to find and fix the root cause rather than adding a shortcut 'clean up' feature.

## Key Takeaways

- **Measure the error before you fix it.** Build an eval that counts how often the failure occurs (for example, parents with too many children) so you can judge whether a fix actually reduces the error rate.
- **Combine code-based and judgment-based evals.** Use simple code assertions for structural properties like tree shape and an LLM-as-a-judge for semantic problems like missed sub-groupings.
- **Calibrate your LLM judge against your own labels.** Hand-label a calibration set with a mix of error and non-error cases, then compare the judge's output to yours, checking both specificity and recall.
- **Fix the root cause, not the symptom.** Ask why the agent failed to add structure (the prompt, the logic, or the input) instead of giving users a manual 'clean up' button that hides the defect.
- **Expect experimentation to take several rounds.** Plan for multiple evals and many prompt variants, since the team in this story needed 4 new evals and 16 experiment variants to resolve one customer complaint.

## Related

- [[Generating Opportunity Solution Trees with AI How Vistaly Rebuilt Its Product]]
- [[2026-09-22 Advanced evals How to find (and fix) hidden AI failures in your product]]
- [[2026-03-20 Evals are the new PRD. Here is the playbook with the CEO of the leader in the]]
