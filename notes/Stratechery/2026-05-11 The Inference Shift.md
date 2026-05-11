# The Inference Shift

**Source**: [Stratechery](https://stratechery.com/2026/the-inference-shift/)
**Author**: Ben Thompson | **Date**: May 11, 2026

---

## Summary

As AI workloads shift from training-dominated to inference-heavy, the semiconductor industry is moving from GPU monopoly to specialized architectures, with Cerebras and other inference-optimized chips gaining traction for specific use cases like low-latency applications and wearables.

## Key Takeaways

- **Understand the inference bottleneck**: Inference is fundamentally different from training—it's memory-bandwidth bound rather than compute bound, which makes GPUs suboptimal for many inference scenarios and creates opportunities for specialized chips like Cerebras.
- **Optimize for latency in product design**: As AI moves into wearables and real-time interactions, token generation speed becomes a core product differentiator; companies should measure and optimize for end-user latency rather than throughput metrics.
- **Expect heterogeneous chip architectures**: The future of AI compute won't be dominated by a single chip type; different workloads (prefill, decode, KV cache management) require different optimization strategies, creating multiple viable market opportunities.
- **Evaluate memory-bandwidth tradeoffs**: When choosing between chips for inference, memory bandwidth per unit of memory becomes critical; Cerebras' 6,000x bandwidth advantage over H100 matters only when the entire model fits on-chip, so calculate your actual requirements before committing.

## Related

- [[2026-04-13 The Beginning of Scarcity in AI]]
- [[2026-04-28 The Three Questions in AI Sales]]
- [[2026-04-20 TSMC Earnings, New N3 Fabs, The Nvidia Ramp]]
