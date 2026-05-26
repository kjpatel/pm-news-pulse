# How PMs Ship 100K Lines of Code at OpenAI with Ryan Lopopolo, Member of Technical Staff

**Source**: [Product Growth](https://www.news.aakashg.com/p/ryan-lapopolo-podcast)
**Author**: Aakash Gupta (featuring Ryan Lopopolo) | **Date**: May 25, 2026

---

## Summary

OpenAI PMs ship 100K lines of production code by building a 'harness'—a system of docs, tests, and rules that teaches AI agents how to code—rather than writing code themselves. This shifts PM work from writing PRDs to creating executable artifacts (markdown specs, tests, evals) that guide agent behavior and dramatically compress feature development from weeks to days.

## Key Takeaways

- **Build an agents.md harness**: Create a repo-level file documenting your team's operating loop, design patterns, and decision history so AI agents understand how you build software before they start coding.
- **Encode taste into tests and lints**: Instead of arguing style in Slack, embed non-functional requirements directly into your test suite—use lint failures as instructions so agents learn your standards automatically.
- **Shift PM artifacts from PRDs to executable specs**: Write markdown PRDs paired with tests and evals that agents can run independently; your leverage comes from artifacts the harness understands, not from typing code.
- **Use review agents with persona docs**: Spin up specialized AI reviewers (frontend architect, reliability engineer, security) with documented perspectives so feedback loops stay tight and patterns don't repeat.
- **Prove features work through user paths**: Give agents observability into metrics, logs, and UI so they can validate that features work end-to-end through the same flows your users take, not just pass tests.

## Related

- [[2026-04-30 How to Build a Full AI Dev Team in Claude Code Guide from Google PM Gabor Meyer]]
- [[2026-04-14 How to Ship Your First Pull Request as a PM]]
- [[2026-03-30 How to turn Claude Code into an Operating System with Carl Vellotti]]
