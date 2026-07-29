# Aftermarket Harnesses

**Source**: [Tomasz Tunguz](https://www.tomtunguz.com/aftermarket-harnesses/)
**Author**: Tomasz Tunguz | **Date**: Jul 28, 2026

---

## Summary

AI harnesses—the infrastructure layer that wraps models—now have greater impact on performance and cost than the underlying models themselves, with cache discipline and intelligent context management being the primary value drivers. Third-party harnesses like Cursor can match or exceed the performance of first-party solutions through superior engineering techniques.

## Key Takeaways

- **Prioritize harness architecture over model selection**: Endor Labs found GPT-5.5 scored 25.7 points higher in Cursor's harness (87.2%) than its native Codex harness (61.5%), proving the runtime environment matters more than the model for functional correctness.
- **Implement aggressive prompt caching strategies**: Since input tokens represent 86-98% of LLM costs, deploy cache-first design patterns with stable prefixes before dynamic content to achieve 40-80% cost savings and 13-31% faster time-to-first-token.
- **Engineer precise information retrieval pipelines**: Design harnesses to fetch only concise, relevant context (code snippets, style guides, document sections) rather than broad context, directly reducing token costs without sacrificing quality.
- **Adopt dynamic tool-fetching and prefix assembly**: Third-party harnesses match first-party performance by implementing multi-tier caching, dynamic tool selection, and priority-based prompt construction—techniques that are harness-level, not model-level capabilities.
- **Treat harness co-design as a competitive advantage**: While bundled solutions like Claude Code achieve 96% cache hit rates through system integration, the discipline itself is portable—invest in harness engineering to match first-party advantages independently.

## Related

- [[2026-07-14 The Harness Is the New Battleground]]
- [[2026-05-20 PM Brain OS The Second Brain for Product Managers, Made of Markdown]]
- [[2026-06-07 Claude Dynamic Workflows for PMs The Ultimate Guide]]
