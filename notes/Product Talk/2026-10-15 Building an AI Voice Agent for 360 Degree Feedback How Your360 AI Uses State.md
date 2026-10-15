# Building an AI Voice Agent for 360 Degree Feedback: How Your360 AI Uses State Machines, Evals, and Layered Synthesis

**Source**: [Product Talk](https://www.producttalk.org/building-an-ai-voice-agent-for-360-degree-feedback-how-your360-ai-uses-state-machines-evals-and-layered-synthesis/)
**Author**: Teresa Torres (featuring Jared Goralnick, Eda Goksel Jackson, and Alex Krasun) | **Date**: Oct 15, 2026

---

## Summary

Your360 AI shows how to build a reliable AI voice agent for interview-based 360-degree feedback by replacing a single prompt with state machines, controlling the full voice stack, and testing with evals built from failed calls. The article argues that accurate, corroborated, and anonymous synthesis requires layered, two-pass evaluation.

## Key Takeaways

- **Ship in stages, starting with the riskiest interaction.** Your360 validated the self-discovery agent a month before feedback collection existed, and built synthesis after that, so each layer was proven one call at a time.
- **Use state machines instead of a single prompt for structured conversations.** State machines keep the voice agent on track through strengths, growth areas, and requested topics while still letting it go deep when a user wants to.
- **Build evals from personas based on calls that failed.** Use these regression tests to check model and provider upgrades before rolling them out.
- **Replace routine transcript review with automated flags.** Flag sentiment, customer value, and product quality issues so humans only step in when something goes wrong, and find design partners willing to let you see conversations early.
- **Run two kinds of evals on synthesis.** Use structural passes to catch errors like misattributed feedback, and substantive passes that re-run analysis with few rules to surface patterns the first pass missed.

## Related

- [[2026-09-22 Advanced evals How to find (and fix) hidden AI failures in your product]]
- [[2026-03-20 Evals are the new PRD. Here is the playbook with the CEO of the leader in the]]
- [[2026-09-21 Ch. 10 Testing Assumptions]]
