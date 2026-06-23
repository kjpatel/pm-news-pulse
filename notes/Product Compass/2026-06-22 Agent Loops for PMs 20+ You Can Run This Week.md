# Agent Loops for PMs: 20+ You Can Run This Week

**Source**: [Product Compass](https://www.productcompass.pm/p/loop-engineering-for-pms)
**Author**: Pawel Huryn | **Date**: Jun 22, 2026

---

## Summary

Agent loops are feedback cycles that repeat until a defined stop condition is met, and their effectiveness depends entirely on clearly defining what 'done' means—which is a PM job of writing acceptance criteria, success metrics, and sign-off procedures, not a coding task.

## Key Takeaways

- **Define stop conditions explicitly** - Write your loop's goal as a measurable, checkable condition rather than leaving it vague; without a clear definition of 'done,' loops will run indefinitely producing plausible-looking garbage.
- **Separate the maker from the checker** - For subjective evaluations, use an independent grader (a second model, rubric, or human review) rather than letting the same agent judge its own work, since models pass themselves on subjective criteria.
- **Use /goal syntax for human-initiated loops** - In Claude Code or Codex, /goal automatically stops when conditions are met, while /loop just reruns on a timer; choose the right primitive based on whether you need deterministic stopping versus fixed scheduling.
- **Write acceptance criteria as Intent Engineering** - Defining loop stop conditions is the same PM work you already do for features—name objectives, desired outcomes, and health metrics upfront so agents can act autonomously without waiting for your next prompt.
- **Build in escape hatches for impossible goals** - Add a line allowing the agent to quit by saying 'STOP' three times if a goal can't be achieved or measured, preventing infinite loops on unreachable targets.

## Related

- [[2026-06-17 How to design AI agent loops schedules, goals, and subagents in Claude Code and]]
- [[2026-05-08 I've spent the last week building you a Team OS in Claude Code]]
- [[2026-03-07 The PM's Guide to Agent Distribution MCP Servers, CLIs, and AGENTS.md]]
