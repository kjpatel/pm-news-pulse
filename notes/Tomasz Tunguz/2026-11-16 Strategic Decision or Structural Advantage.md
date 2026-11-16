# Strategic Decision or Structural Advantage?

**Source**: [Tomasz Tunguz](https://tomtunguz.com/two-pricing-strategies-in-enterprise-ai/)
**Author**: Tomasz Tunguz | **Date**: Nov 16, 2026

---

## Summary

Databricks enterprise telemetry shows Anthropic and OpenAI splitting the AI token market by tier: Anthropic dominates premium frontier usage, while OpenAI dominates low-end usage after steep price cuts. The article asks whether OpenAI's Luna pricing is a temporary market-share subsidy or a durable cost advantage in its model architecture.

## Key Takeaways

- **Segment your model spend by tier.** Route frontier tasks to premium models and high-volume, low-complexity work to economy models, since the two labs are winning different segments.
- **Track the mid tier closely.** OpenAI went from 0% to 47% of mid-tier volume in a few months, so re-benchmark Sonnet-class and Sol-class models against your own workloads before committing to a provider.
- **Test whether price cuts are durable before rebuilding around them.** Luna's 90% cut may be a subsidy, so model costs over a 6 to 12 month horizon rather than assuming today's prices will hold.
- **Monitor open-weight adoption as a pricing hedge.** Open-weight share stalled at 31% when OpenAI cut prices, so keep an open-weight option tested to use as leverage and a fallback.
- **Calculate blended costs using your real input-to-output ratio.** The article's 200:1 blend shows that per-token list prices can mislead, so compute effective cost per task from your own traffic mix.

## Related

- [[2026-10-05 Inference Is the Most Important Market in Software]]
- [[2026-11-11 Who Captures the Most Margin in AI]]
- [[2026-10-13 Price War in the Chip Aisle]]
