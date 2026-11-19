# Agent Sandboxes Explained - A Guide for Product Teams

**Source**: [Department of Product](https://departmentofproduct.substack.com/p/agent-sandboxes-explained-a-guide)
**Author**: Rich Holmes | **Date**: Nov 19, 2026

---

## Summary

Agent sandboxes are isolated execution environments that let AI agents run code and take actions safely, and this guide explains how they work and what product teams need to know. It draws on real-world examples from OpenAI, Dropbox, Replit, Figma and others.

## Key Takeaways

- **Treat the sandbox as a product requirement:** Define what an agent may read, write, execute, and reach over the network before building features, and document those boundaries for your team.
- **Scope permissions per task:** Give each agent session only the credentials and file access it needs, and expire them when the task ends.
- **Make agent actions observable:** Log commands, file changes, and external calls so product and support teams can audit and debug what an agent did.
- **Plan for failure inside the sandbox:** Design clear recovery paths for crashed runs, runaway processes, and partial writes so users can resume or roll back safely.
- **Study how peers run sandboxes:** Review the OpenAI, Dropbox, Replit, and Figma examples to compare isolation approaches and choose the simplest one that meets your risk level.

## Related

- [[2026-07-14 The Harness Is the New Battleground]]
- [[2026-11-05 Agent Harness How I Built My Own Claude Code, Step by Step]]
- [[2026-05-08 Securing the Agentic Enterprise]]
