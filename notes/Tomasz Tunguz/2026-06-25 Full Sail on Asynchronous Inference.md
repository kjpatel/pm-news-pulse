# Full Sail on Asynchronous Inference

**Source**: [Tomasz Tunguz](https://www.tomtunguz.com/sail-inference-queue/)
**Author**: Tomasz Tunguz | **Date**: Jun 25, 2026

---

## Summary

Asynchronous inference represents a massive cost opportunity as AI workloads shift from real-time chat to multi-turn agents running in the background, with Sail Research building fleet-aware orchestration to maximize throughput per dollar of inference spend.

## Key Takeaways

- **Segment inference markets by latency tolerance**: Real-time, near-real-time, and batch/async inference have fundamentally different economics—async workloads can achieve 6x cost savings by sacrificing milliseconds of latency for dramatically higher throughput.
- **Optimize for queue-based architectures**: Build systems that pack requests into idle capacity rather than reserving capacity per request, using spot instances when available and failing over to reliable compute to keep utilization and cost efficiency high.
- **Route requests to cheapest capable models**: Implement dynamic model routing across open-source alternatives like DeepSeek, Qwen, and GLM to reduce token costs without sacrificing quality for most agent tasks.
- **Design agent infrastructure for background workers**: Structure compute resources as stateful containers that pause during inference waits and resume in seconds, billing only for active time to eliminate idle waste in long-running agent tasks.

## Related

- [[2026-05-15 The First Derivative of Inference]]
- [[2026-04-29 Darwinian Specialization in AI]]
- [[2026-06-03 Intelligence Per Dollar]]
