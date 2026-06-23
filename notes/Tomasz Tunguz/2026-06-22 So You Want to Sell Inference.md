# So You Want to Sell Inference

**Source**: [Tomasz Tunguz](https://www.tomtunguz.com/so-you-want-to-sell-inference/)
**Author**: Tomasz Tunguz | **Date**: Jun 22, 2026

---

## Summary

Reselling inference at cost is a zero-margin business; companies must choose between cost-plus pricing (markup on raw API costs), value-based pricing (charging for outcomes), or optimization (reducing delivery costs) to maintain sustainable margins. The model chosen fundamentally determines whether you're building a payment processor or a software company.

## Key Takeaways

- **Choose your pricing model intentionally**: Decide between cost-plus pricing (risky as inference commoditizes), value-based pricing (charge per outcome, not tokens), or optimization (reduce costs through distillation and routing) based on your defensibility strategy.
- **Build a superior product harness**: If pursuing cost-plus pricing, your UX, workflow, and product must justify a 30%+ premium over raw API costs, or customers will route directly to cheaper inference providers.
- **Defend with proprietary distillation**: Run production traffic through frontier models to distill into small proprietary models deployable on cheap hardware—this creates a defensible competitive advantage that pure routing and caching cannot replicate.
- **Understand BYOK (bring your own key) implications**: If customers bring their own inference keys, cost-plus pricing breaks immediately (visible tax), so shift to value-based pricing (charge for outcomes) or optimization (platform fee for efficiency gains).
- **Decouple from the inference line**: Use outcome-based abstractions like credits (Databricks/Snowflake), resolved tickets (Sierra), or Agent Compute Units (Devin) instead of token pricing to maintain margin durability as inference costs fall.

## Related

- [[2026-05-11 The Inference Shift]]
- [[2026-02-23 How to Price AI Products The Complete Guide for PMs]]
- [[2026-04-23 Intelligence About Business]]
