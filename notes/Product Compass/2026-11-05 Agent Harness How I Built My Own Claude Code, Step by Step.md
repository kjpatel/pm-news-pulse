# Agent Harness: How I Built My Own Claude Code, Step by Step

**Source**: [Product Compass](https://www.productcompass.pm/p/build-your-own-agent-harness)
**Author**: Pawel Huryn | **Date**: Nov 05, 2026

---

## Summary

The article argues that an agent harness (the tools, memory, and safety layer around a model) can be understood by building one, and the author shares a 1,200-line Python 'Mini Harness' that ranked near the top on Claude Haiku in tests against seven other harnesses. It walks readers through 15 prompt-driven steps to build their own harness in about 1-2 hours.

## Key Takeaways

- **Build a minimal agent loop first.** Start with a loop that sends the task to the model, runs the tools it requests, returns results, and repeats until the model stops asking for actions.
- **Give every tool call an answer and write errors as instructions.** Even denied or failed actions need a response, and error messages should tell the model what to try next, such as 'that text appears 3 times, add more context.'
- **Never edit context that has already been sent.** Append new information to the end of the conversation so the provider's cache keeps working and costs stay down, since cached tokens are far cheaper.
- **Keep a design doc and test each step.** Record every decision and how to run the project, then verify each feature with simple tests like a headless 'say hi' run or a missing API key check.
- **Use AGENTS.md to control behavior across sessions.** Put project-level instructions in this file, then confirm they apply by changing it and starting a new session to see the difference.

## Related

- [[2026-05-12 Claude Code for PMs The Beginner's Guide]]
- [[2026-04-27 Claude Code's Limits Are Generous. The Problem Is Your Setup.]]
- [[2026-10-20 Claude Desktop v2.0 You Don't Need VS Code Anymore!]]
