# Engineering at Machine Speed

**Source**: [Tomasz Tunguz](https://tomtunguz.com/engineering-at-machine-speed-office-hours/)
**Author**: Tomasz Tunguz (featuring Dan Shiebler) | **Date**: Nov 24, 2026

---

## Summary

Artemis Security's CTO Dan Shiebler argues that engineering teams can run at machine speed, merging over 31,000 pull requests in a quarter and shipping most feature requests within 24 hours, by running several coding agents in parallel. Quality holds at that pace only because evaluation pipelines and row-level inspection of failures catch problems continuously.

## Key Takeaways

- **Run multiple coding agents in parallel:** Assign each engineer several agents (Artemis reports 4 to 8) working on separate tasks so throughput scales beyond what one person coding by hand can produce.
- **Set a 24-hour target for feature delivery:** Measure how quickly feature requests reach customers and push the team to ship most of them within a day, which forces smaller scopes and faster feedback.
- **Build evaluation pipelines before scaling output:** Automated evals should run on every change so that quality checks keep pace with the volume of pull requests rather than becoming a bottleneck.
- **Inspect failures row by row:** When evals flag problems, look at individual failing cases instead of only aggregate scores to find the specific root causes and fix them quickly.
- **Rethink design, code review, and ownership for agent-driven work:** Expect that high parallelism changes how designs are written, how reviews are done, and who owns each change, so define those processes explicitly for agent output.

## Related

- [[2026-05-31 I Don't Review the Code. I Review the Artifacts.]]
- [[2026-06-22 Agent Loops for PMs 20+ You Can Run This Week]]
- [[2026-07-14 The Harness Is the New Battleground]]
