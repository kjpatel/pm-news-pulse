# WebMCP in Practice

**Source**: [Department of Product](https://departmentofproduct.substack.com/p/webmcp-in-practice)
**Author**: Rich Holmes | **Date**: Oct 19, 2026

---

## Summary

WebMCP is a emerging standard that lets websites expose their functionality directly to AI agents, and this article examines how companies such as Shopify, Stripe, Lovable, and Vercel are using it in production, what results they are seeing, and how to decide whether your product needs it.

## Key Takeaways

- **Audit your product's core actions before adopting WebMCP.** List the tasks users most often complete on your site, then identify which ones an AI agent would need to perform on a user's behalf.
- **Start with a single high-value workflow in production.** Pick one action, such as checkout, search, or account lookup, expose it through WebMCP, and measure completion rates before expanding.
- **Measure agent-driven outcomes separately from human traffic.** Track conversion, error rates, and task completion for agent sessions so you can judge whether the investment pays off.
- **Decide based on whether agents are already reaching your product.** If agents are already scraping or automating your UI, WebMCP can make those interactions more reliable; if not, the case for it is weaker.
- **Treat your site's tool definitions as a product surface.** Write clear names, descriptions, and permissions for each exposed capability, since agents rely on them the way users rely on interface labels.

## Related

- [[2026-09-15 How to develop a Headless Product Strategy]]
- [[2026-10-06 The new UX of AI Agents]]
- [[2026-05-22 Plastic User Interfaces]]
