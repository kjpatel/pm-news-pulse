# Inside the black box of AI: How AI models actually think | Emmanuel Ameisen (Anthropic)

**Source**: [Lenny's Newsletter](https://www.lennysnewsletter.com/p/a-mind-expanding-conversation-on)
**Author**: Lenny Rachitsky (featuring Emmanuel Ameisen) | **Date**: Oct 18, 2026

---

## Summary

Anthropic interpretability researcher Emmanuel Ameisen argues that the common 'next-token predictor' framing understates how LLMs actually plan and think, since models form general concept representations and plan many tokens ahead. He contends that models are 'grown' rather than built, which makes interpretability research central to understanding and aligning them.

## Key Takeaways

- **Retire the 'just a next-token predictor' framing when reasoning about model behavior.** Research shows models plan several tokens ahead and represent concepts generally, so judge them by what they can internally do, not only by their surface output.
- **Use anthropomorphic language deliberately as a working tool.** Ameisen argues that comparing model behavior to human cognition can be a productive way to form hypotheses, as long as you test those hypotheses rather than assume them.
- **Treat AI models as grown systems that need empirical probing.** Because training shapes models in ways no one fully specifies, test for unexpected behaviors and capabilities directly instead of assuming the design intent holds.
- **Don't read sudden capability jumps as discontinuities.** Ameisen points to a smooth underlying scaling curve, so anticipate gradual improvement in capabilities and plan product roadmaps around trend lines rather than surprise breakthroughs.
- **Invest in interpretability as part of safety and alignment work.** Understanding internal model mechanisms is how you verify what a model is doing and why, which supports safer deployment decisions.

## Related

- [[2026-02-19 Head of Claude Code What happens after coding is solved Boris Cherny]]
- [[2026-09-22 Advanced evals How to find (and fix) hidden AI failures in your product]]
- [[2026-02-19 AI Evals Explained Simply by Ankit Shukla]]
