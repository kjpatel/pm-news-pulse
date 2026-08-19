# Birds Don't Fly Like Planes. Neither Does AI.

**Source**: [Tomasz Tunguz](https://www.tomtunguz.com/birds-dont-fly-like-planes-neither-does-ai/)
**Author**: Tomasz Tunguz | **Date**: Aug 18, 2026

---

## Summary

Smaller local AI models can match cloud-based models in quality by using more reasoning tokens, but they take different computational paths—like how bumblebees and planes achieve flight differently. The key metric is time-to-answer, not token generation speed.

## Key Takeaways

- **Measure end-to-end latency**: Stop optimizing for token-per-second speeds and instead focus on total time-to-answer, as smaller models achieve equal quality through longer reasoning chains.
- **Local models are now production-ready**: A 27B-parameter local model (Qwen3.8-27B) ranks #1 across 135 models on capability benchmarks, matching or exceeding 753B frontier models while running on standard hardware.
- **Reasoning efficiency varies by architecture**: Dense models memorize answers directly while sparse models reason from first principles; understand which approach fits your task before choosing between cloud and local deployment.
- **Benchmark quality independently from speed**: Intelligence rankings and verbosity rankings move independently—a model's intelligence score doesn't predict how many tokens it needs, so establish your own trade-off acceptance criteria.

## Related

- [[2026-05-15 The First Derivative of Inference]]
- [[2026-06-29 When AI Costs More Than the Engineer]]
- [[2026-07-20 Open Models Tack Toward the Frontier]]
