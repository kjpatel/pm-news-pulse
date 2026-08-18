# When Models Learn

**Source**: [Tomasz Tunguz](https://www.tomtunguz.com/test-time-training-impact/)
**Author**: Tomasz Tunguz | **Date**: Aug 17, 2026

---

## Summary

Test-time training allows AI models to learn and update their weights as users interact with them, fundamentally changing the economics of AI by trading off memory efficiency for increased compute requirements and enabling personalization.

## Key Takeaways

- **Understand the memory tradeoff**: Test-time training replaces growing KV-caches with fixed-size weight updates, keeping memory flat regardless of context length, but requires separate model instances per user instead of shared frozen models.
- **Evaluate personalization ROI**: Only deploy test-time training where persistent learning justifies per-user compute costs—coding agents that build codebase knowledge are viable, but one-off queries should use cheaper shared models.
- **Plan for infrastructure scaling**: Providers must allocate more GPU capacity to serve test-time trained models since each user gets a personalized copy, fundamentally shifting from memory constraints to compute constraints.

## Related

- [[2026-07-14 The Harness Is the New Battleground]]
- [[2026-06-29 When AI Costs More Than the Engineer]]
- [[2026-08-04 Racing to Sustain Jevons' Paradox]]
