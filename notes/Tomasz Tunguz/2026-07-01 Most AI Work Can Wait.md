# Most AI Work Can Wait

**Source**: [Tomasz Tunguz](https://www.tomtunguz.com/ai-execution-routing/)
**Author**: Tomasz Tunguz | **Date**: Jul 01, 2026

---

## Summary

Most AI work doesn't require expensive frontier models—prioritize building a smart routing system that classifies tasks and intelligently directs 70-80% of traffic to cheap local models or async batch processing instead of choosing models first.

## Key Takeaways

- **Design the router first.** Build a three-layer routing system (skill classifier, router, model selector) that decides which tier of model handles each request before selecting any specific model.
- **Queue async work aggressively.** Most tasks like drafting replies, summarizing repos, and running evaluations don't need real-time responses—batch async inference costs two orders of magnitude less than real-time inference.
- **Implement dual feedback loops.** Use synchronous predictors to catch known-hard tasks before failure and nightly batch evaluators to discover new failure modes and update router weights without expensive real-time inference.
- **Separate classification from routing decisions.** Keep intent recognition (skill classifier) distinct from scheduling logic (router) to enable A/B testing different models against the same operation.

## Related

- [[2026-06-25 Full Sail on Asynchronous Inference]]
- [[2026-05-29 Skill Distillation]]
- [[2026-06-05 The Minimill of AI]]
