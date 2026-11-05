# Context Graphs Explained - A Guide for Product Teams

**Source**: [Department of Product](https://departmentofproduct.substack.com/p/context-graphs-explained-a-guide)
**Author**: Rich Holmes | **Date**: Nov 05, 2026

---

## Summary

Context graphs are structured maps of the entities, relationships, and decision history that AI systems need to act well inside a business. The article argues product teams should build one deliberately, and it illustrates the approach with real examples from GitLab, Harvey, and Atlassian.

## Key Takeaways

- **Map the entities and relationships your AI features depend on.** List the core objects (customers, tickets, contracts, code, decisions) and how they connect before choosing any model or tool.
- **Capture decision traces, not just current state.** Record why actions were taken and what outcomes followed, so agents can learn from precedent instead of only reading static records.
- **Start with one high-value workflow.** Pick a single process where missing context causes visible errors, build the graph for that slice, and measure whether agent output improves before expanding.
- **Assign clear ownership for context quality.** Name a team responsible for data freshness, permissions, and schema changes, since a stale or inconsistent graph will quietly degrade every AI feature built on it.
- **Study the GitLab, Harvey, and Atlassian examples for patterns.** Compare how each company sourced context, governed access, and connected it to agent actions, and adapt the patterns that fit your product.

## Related

- [[2026-10-30 Product Intuition is Context Compounded]]
- [[2026-06-17 The AI Product Operating Model]]
- [[2026-09-24 Thinking in Systems, Shipping in Loops]]
