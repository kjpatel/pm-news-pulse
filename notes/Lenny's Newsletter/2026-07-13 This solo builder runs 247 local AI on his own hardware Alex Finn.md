# This solo builder runs 24/7 local AI on his own hardware | Alex Finn

**Source**: [Lenny's Newsletter](https://www.lennysnewsletter.com/p/this-solo-builder-runs-247-local)
**Author**: Lenny Rachitsky | **Date**: Jul 13, 2026

---

## Summary

Alex Finn, an AI builder and YouTuber, discusses his ambitious local AI setup running 24/7 across multiple machines (Mac Studios, DGX Spark, RTX 5090) coordinated through a custom fleet dashboard, demonstrating how local inference changes the economics and possibilities of AI development.

## Key Takeaways

- **Choose hardware by workload**: Mac Studio excels at unified memory tasks, DGX Spark handles distributed inference, and RTX 5090 specializes in throughput—match your machine to your model's requirements rather than buying one universal solution.
- **Use Tailscale for fleet management**: Installing Tailscale even on a single machine enables seamless agent coordination across your entire hardware fleet without manual intervention or constant babysitting.
- **Build redundancy into agent loops**: Run multiple agents with failover mechanisms (Alex runs 5 agents total) to ensure 24/7 operation and graceful degradation when individual models or machines encounter issues.
- **Rethink task allocation by cost**: Unlimited local inference eliminates the per-token economics of cloud services—assign compute-intensive, low-value tasks to local models and reserve cloud APIs for high-leverage work that benefits from latest model capabilities.
- **Leverage local models as security layers**: Use local inference as a first-pass security scanner or content filter feeding into Claude Code loops, reducing exposure to sensitive data in cloud APIs while improving latency.

## Related

- [[2026-03-17 How to design AI agent loops schedules, goals, and subagents in Claude Code and Codex]]
- [[2026-06-30 How top PMs increase their leverage with AI]]
- [[2026-04-14 How to Ship Your First Pull Request as a PM]]
