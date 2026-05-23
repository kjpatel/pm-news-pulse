# How to Run Evals in Claude Code with Aparna Dhinakaran, Founder and CPO of Arize

**Source**: [Product Growth](https://www.news.aakashg.com/p/aparna-dhinakaran-podcast)
**Author**: Aakash Gupta (featuring Aparna Dhinakaran) | **Date**: May 22, 2026

---

## Summary

Claude Code can now run evals directly through the Arize skills integration, allowing PMs to move from manual error analysis to automated eval suggestion and self-improving agent loops. This fundamentally changes how product teams test and iterate on AI systems, compressing what used to take weeks into hours.

## Key Takeaways

- **Install Arize skills in Claude Code** with a single command (npx skills add Arize-ai/arize-skills) to get instant access to instrumentation, eval suggestion, and improvement capabilities without writing eval code yourself.
- **Let Claude suggest your first eval** by asking it to analyze your agent traces and propose evaluation categories—these Claude-generated v0 evals are trustworthy starting points that get you data in minutes, not weeks of manual analysis.
- **Build a self-improving loop** that automatically fetches eval failures, categorizes them, and proposes fixes on a schedule, with you always approving changes before they ship to maintain control while gaining speed.
- **Move from output-level to behavior-level evals** by asking specific questions about what you actually care about (e.g., priority scoring accuracy) so Claude surfaces concrete failure categories you can systematically improve.
- **Replace manual PM workflows** where you spend hours reading issues and calls trying to find patterns—instead, let Claude run continuous loops that surface patterns at scale and propose targeted improvements.

## Related

- [[2026-03-20 Evals are the new PRD. Here is the playbook with the CEO of the leader in the]]
- [[2026-02-19 AI Evals Explained Simply by Ankit Shukla]]
- [[2026-05-08 I've spent the last week building you a Team OS in Claude Code]]
