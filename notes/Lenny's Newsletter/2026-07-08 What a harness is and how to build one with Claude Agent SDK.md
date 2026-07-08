# What a harness is and how to build one with Claude Agent SDK

**Source**: [Lenny's Newsletter](https://www.lennysnewsletter.com/p/what-a-harness-is-and-how-to-build)
**Author**: Lenny Rachitsky (featuring Claire Vo) | **Date**: Jul 08, 2026

---

## Summary

A harness is a specialized AI system built for specific, repetitive workflows that goes beyond general-purpose tools—this episode demonstrates how to build one for bug triage using Claude Agent SDK, with live code examples and architectural guidance.

## Key Takeaways

- **Define your use case precisely**: Build a harness only for highly structured, repetitive workflows where you need consistent input/output formats and specific permissions—general tools like Claude Code are better for exploratory work.
- **Structure with three core components**: Every effective harness needs a clear architecture of runs (orchestration), tasks (specific actions), tools (integrations with your stack), and artifacts (standardized outputs your team can consume).
- **Encode permissions and guardrails**: Use custom adapters and harness design to limit what agents can do—don't just give them broad access to your tools; control inputs, outputs, and which systems they can interact with.

## Related

- [[2026-04-30 How to Build a Full AI Dev Team in Claude Code Guide from Google PM Gabor Meyer]]
- [[2026-06-17 How to design AI agent loops schedules, goals, and subagents in Claude Code and]]
- [[2026-04-07 How to build a Team OS in Claude Code with Hannah Stulberg, PM @ DoorDash]]
