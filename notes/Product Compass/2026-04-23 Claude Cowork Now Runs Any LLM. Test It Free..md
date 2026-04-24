# Claude Cowork Now Runs Any LLM. Test It Free.

**Source**: [Product Compass](https://www.productcompass.pm/p/cowork-on-3p-any-llm)
**Author**: Pawel Huryn | **Date**: Apr 23, 2026

---

## Summary

Anthropic has quietly shipped third-party inference support for Claude Cowork and Code, allowing users to run these tools against any LLM (GPT-5, Grok, Gemini, local models, or enterprise gateways) with full admin controls. This signals a strategic shift toward enterprise compliance and positions Claude as an infrastructure layer rather than just a consumer product.

## Key Takeaways

- **Set up third-party inference immediately** if you're hitting Claude's usage limits or need to run local models—configure it via Menu → Developer → Configure Third-Party Inference and point to OpenRouter or your preferred gateway in under 5 minutes.
- **Import Anthropic skills and plugins manually** when using third-party inference, as they don't auto-populate like they do with native Claude—download from the official repos and upload via Customize → Skills/Plugins to maintain full functionality.
- **Replace native web search with Brave MCP** when using OpenRouter, since third-party inference doesn't support Anthropic's native search—add the Brave server to your MCP configuration to preserve agent capabilities.
- **Recognize this as an enterprise play**, not a consumer feature—the research preview ships with team-wide admin controls (token caps, MCP allowlists, OpenTelemetry) designed for regulated industries and organizations with strict data residency requirements.
- **Test non-Claude models carefully** for agentic workflows, as tool calling and multi-step flows vary significantly by model—start with recommended models like Tencent's HY3 before scaling to production use cases.

## Related

- [[2026-02-16 You Should Be Using Claude Cowork Complete Guide]]
- [[2026-02-21 Claude Cowork The Ultimate Guide for PMs]]
- [[2026-03-08 A Guide to Claude Code for PMs From Cowork to Code]]
