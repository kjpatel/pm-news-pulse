# Sonnet 5 review: I ran 64 generations to find out if it's worth it

**Source**: [Lenny's Newsletter](https://www.lennysnewsletter.com/p/sonnet-5-review-i-ran-64-generations)
**Author**: Lenny Rachitsky (featuring Claire Vo) | **Date**: Jun 30, 2026

---

## Summary

Lenny Rachitsky built a repeatable evaluation framework (the How I AI Bench) using Claude Code to rigorously test Sonnet 5 against four other frontier models across multiple tasks, revealing surprising results that differ from vendor claims and one-off vibe checks.

## Key Takeaways

- **Build repeatable evals instead of one-off tests** — Create a systematized scoring framework combining human judgment (70%) with LLM-as-judge (30%) to get reliable, comparable results across model releases over time.
- **Use local HTML scoring pages with JSON exports** — Set up a simple interface to rate AI outputs on gut feel and export structured data, making it easy to iterate on evaluation criteria and aggregate scores.
- **Match models to specific tasks rather than declaring winners** — Different models excel at different tasks (PRDs, prototypes, agents, personality), so make model-by-task recommendations instead of using a single leaderboard rank.
- **Run blind comparisons with 64+ generations** — Test enough samples across multiple dimensions to surface patterns that individual tests would miss and validate vendor claims against real-world performance.

## Related

- [[2026-05-28 Claude Opus 4.8 is here. Is it as good as they say]]
- [[2026-06-09 Claude Fable 5 review what the new Mythos model gets right (and very wrong)]]
- [[2026-05-15 I faced off the AI prototyping tools, and added the winner to my bundle]]
