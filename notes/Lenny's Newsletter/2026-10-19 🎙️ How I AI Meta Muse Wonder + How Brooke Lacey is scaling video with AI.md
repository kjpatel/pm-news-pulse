# 🎙️ How I AI: Meta Muse Wonder + How Brooke Lacey is scaling video with AI

**Source**: [Lenny's Newsletter](https://www.lennysnewsletter.com/p/how-i-ai-meta-muse-wonder-how-brooke)
**Author**: Lenny Rachitsky (featuring Claire Vo and Brooke Lacey) | **Date**: Oct 19, 2026

---

## Summary

This How I AI episode pairs two workflow reviews: Claire Vo finds Meta's Muse Wonder strong for agentic tasks and email writing but weak at frontend design, and Brooke Lacey shows how Claude Code, FFmpeg, and Whisper can turn a raw phone recording into a finished TikTok short in about 15 seconds. Both argue that AI is most useful when paired with a person's existing judgment and a well-structured system.

## Key Takeaways

- **Test agent models on your own real workflows before adopting them.** Claire ran Muse Wonder through nearly 20 tasks and found it ranked first on billing-ticket resolution, inbox triage, and computer use, but fell short on visual work. Build a small benchmark from your own tasks to see where a model actually performs.
- **Keep AI out of the final 20% of polished design work.** Muse produced convincing scaffolds but broke buttons, themes, and image rendering during interaction testing. Use AI for first drafts and scaffolding, then have a human own the finishing and QA pass.
- **Encode your style with explicit examples and iteration.** Brooke taught Claude her jump-cut cadence through deliberate instruction and repeated refinement, not a single prompt. Start with a few concrete examples of what good looks like and refine the rules over several rounds.
- **Store editing decisions in a plain text file so they can be regenerated.** Brooke's edit lives in a TSV of start time, end time, shot size, and label, so one command produces 15-, 30-, and 60-second versions plus a landscape crop. Keeping edits in structured text makes them reusable and easy to revise.
- **Build a personal operating system with separate memory and permissions per project.** Brooke's "lane OS" gives each product its own memory, permissions, and status files, and when Claude makes a mistake she records the correction globally. Logging fixes this way prevents the same error from recurring.

## Related

- [[2026-10-14 Meta’s new ‘Muse Wonder’ model good for AI agents, bad for design]]
- [[2026-09-16 Muse review The personal AI agent that gets consumer UX right]]
- [[2026-03-30 How to turn Claude Code into your personal life operating system Hilary Gridley]]
