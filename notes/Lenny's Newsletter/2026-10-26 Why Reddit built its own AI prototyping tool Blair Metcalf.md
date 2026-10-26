# Why Reddit built its own AI prototyping tool | Blair Metcalf

**Source**: [Lenny's Newsletter](https://www.lennysnewsletter.com/p/why-reddit-built-its-own-ai-prototyping)
**Author**: Lenny Rachitsky (featuring Blair Metcalf) | **Date**: Oct 26, 2026

---

## Summary

Blair Metcalf, principal UX engineer at Reddit, explains how Reddit built Reddit Proto, an in-house vibe-coding harness that uses a custom design system MCP to turn Reddit's product language into production-ready prototypes. The episode argues that a company-specific prototyping harness, grounded in real data and design-system mappings, can drive near-universal adoption across product and design.

## Key Takeaways

- **Build prototyping on your own design system.** Create an MCP server that maps your product's components and language to production code so AI-generated prototypes match what engineers will ship.
- **Prototype with real production data, not mock data.** Real Reddit data surfaces edge cases and realistic behavior that mock data hides, making prototype feedback more trustworthy.
- **Make targeted edits by annotating the prototype.** Mark up a specific element and send that annotation to Cursor as a scoped code change instead of re-prompting the whole prototype.
- **Hand off work as a feature capsule.** Package each prototype's scope, components, and behavior into a self-contained unit so engineers can pick up implementation without reverse-engineering the prototype.
- **Create a 'Rosetta stone' to translate between design and code.** Map terminology and components across tools so designers, PMs, and engineers share one vocabulary when working with AI.

## Related

- [[2026-04-22 What Claude Design is actually good for (and why Figma isn’t dead yet)]]
- [[2026-03-11 From Figma to Claude Code and back Gui Seiz & Alex Kern (Figma)]]
- [[2026-05-04 From Weeks to Hours How Claude Design Compresses Product Discovery]]
