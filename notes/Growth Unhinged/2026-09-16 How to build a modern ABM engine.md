# How to build a modern ABM engine

**Source**: [Growth Unhinged](https://www.growthunhinged.com/p/how-to-build-a-modern-abm-engine)
**Author**: Kyle Poyar (featuring Dan Rosenthal) | **Date**: Sep 16, 2026

---

## Summary

Account-based marketing is becoming practical for B2B companies with high ACVs and small addressable markets, because AI agents and data enrichment make it cheaper to build. The article lays out a step-by-step, agent-compatible ABM system using HubSpot, Clay, and Claude, starting with TAM and stakeholder mapping.

## Key Takeaways

- **Recommend ABM only when the fit is right:** Use it for B2B companies with an ACV of $50k+ and a constrained addressable market (under 20,000 qualified companies), since other GTM channels convert too poorly to rely on alone.
- **Write down your ICP before building lists:** Create a data-supported ICP document with agreed-upon qualification and tiering parameters, using a simple tiering model for clearer sales execution.
- **Combine 3+ data sources to reach 90%+ TAM coverage:** Blend general prospecting databases, lookalike databases, specialized databases, and web scraping to build the Target Account List, balancing coverage against credit and AI qualification costs.
- **Qualify companies with a structured AI research prompt:** Use a template that checks exclusions first, looks for explicit qualifying evidence, and applies a clear threshold for hybrid companies, returning a standardized verdict for each domain.
- **Move list merging and deduping out of Clay:** Handle merging and deduplication in Claude Code, then use Clay for back-testing and optimizing the qualification prompts and research agents.

## Related

- [[2026-10-06 How to Automate Inbound]]
- [[2026-09-15 When Inbound Sells Itself]]
- [[2026-04-28 The Three Questions in AI Sales]]
