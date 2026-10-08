# Creating Aha! Builder: Concept to Code, No Engineers Required

**Source**: [Product Talk](https://www.producttalk.org/creating-aha-builder-concept-to-code-no-engineers-required/)
**Author**: Teresa Torres (featuring Brian De Haaff, Chris Waters, and Sarah Moisan-Thomas) | **Date**: Sep 17, 2026

---

## Summary

Aha! built Aha! Builder, an AI app builder for product managers rather than engineers, by moving from a wasteful containerized architecture to a single-instance, multi-tenant design with deterministic components. The team argues that as building gets easier, knowing what to build becomes the PM's main differentiator.

## Key Takeaways

- **Keep deterministic where reliability matters.** Use pre-built, non-AI components for authentication, SSO, databases, and email. This cuts token costs and guarantees reliability that AI-generated code cannot.
- **Break app generation into phases.** Run a multi-agent pipeline that builds the design system first, then the prototype, then the backend, rather than relying on one open-ended chat prompt.
- **Measure infrastructure cost before scaling AI features.** Aha! found that containerized Ruby on Rails infrastructure was too slow and expensive for AI app building, so they moved to a single-instance, multi-tenant architecture with V8 isolates.
- **Aim AI builders at prototypes and internal tools first.** Aha! optimizes Builder for prototypes, proofs of concept, and internal "meta applications" rather than primary line-of-business apps, which keeps enterprise governance and PII risk manageable.
- **Invest your PM time in deciding what to build.** As building gets cheaper, the valuable skill is defining the right problem and outcome, not implementing the solution, so practice this judgment deliberately.

## Related

- [[2026-10-01 Harness Engineering Your Complete Guide]]
- [[2026-03-13 There's a New PM Skill. It's Called Taste at Speed]]
- [[2026-04-15 Product Design Questions Are Dead. Here's What Replaced Them.]]
