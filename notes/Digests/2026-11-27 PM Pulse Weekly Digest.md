# PM Pulse: Weekly Digest — Nov 27, 2026

19 articles from 10 feeds | Nov 20 – Nov 27, 2026

---

## This Week

**This week's PM newsletters focus on making AI product quality measurable through evals, running agents at team scale, and how AI changes PM roles, hiring, and pricing.**

Gupta and Mahesh Yadav, along with Torres and Wille, argue that AI output must be judged against an agreed standard, with evals as the mechanism. Tunguz and Shiebler describe agent-driven engineering at high volume, while Thompson argues AI lets individuals do work that once needed teams. Rachitsky's Lenny's Newsletter pieces emphasize personal agents and PM craft.

- **Evals and quality standards for AI** — Gupta and Mahesh Yadav argue evals are now a core PM skill; Torres and Wille argue AI outputs are better or worse rather than right or wrong, so teams must agree on 'good enough.' Vo's benchmark reports blind scoring across frontier models. Sources: [Product Growth](https://www.news.aakashg.com/p/practical-ai-evals) · [Product Talk](https://www.producttalk.org/bugs-all-things-product-podcast-with-teresa-torres-petra-wille/) · [Lenny's Newsletter](https://www.lennysnewsletter.com/p/gemini-4-neon-beat-gpt-62-and-claude)
- **Agents running team-scale work** — Shiebler describes parallel coding agents merging over 31,000 PRs a quarter, with evals catching regressions. Holmes reports Uber's 5,000-skill internal marketplace, while Maheshwari describes a personal agent that starts with small approval tasks. *Continuing thread: Extends prior agent-harness threads from personal setups toward team-level marketplaces and parallel agent work.* Sources: [Tomasz Tunguz](https://tomtunguz.com/engineering-at-machine-speed-office-hours/) · [Department of Product: How Uber built an Internal Marketplace of…](https://departmentofproduct.substack.com/p/how-uber-built-an-internal-marketplace) · [Lenny's Newsletter: 🎙️ How I AI: OpenClaw for executives…](https://www.lennysnewsletter.com/p/how-i-ai-openclaw-for-executives) · [Lenny's Newsletter: OpenClaw for executives: Automate every 1%…](https://www.lennysnewsletter.com/p/openclaw-for-executives-automate) · [Department of Product: 🔵 Replit, Google and Vercel are betting on…](https://departmentofproduct.substack.com/p/replit-google-and-vercel-are-betting) · [Lenny's Newsletter: 🧠 Community Wisdom: Handling context…](https://www.lennysnewsletter.com/p/community-wisdom-handling-context)
- **AI-era PM roles and hiring** — Mansour argues the PM's core job is building a shared brain for the team, and Singhal's The Skip piece examines what AI hiring managers now seek. Gupta's guide notes how eval ownership may split between PMs and engineers. *Continuing thread: Hiring thread continues, now focused on specific skills and ownership boundaries rather than PM demand alone.* Sources: [Lenny's Newsletter](https://www.lennysnewsletter.com/p/first-principles-what-it-takes-to) · [The Skip](https://theskip.substack.com/p/what-ai-hiring-managers-want-right) · [Product Growth](https://www.news.aakashg.com/p/practical-ai-evals)
- **AI pricing and token economics** — Growth Unhinged argues pass-through pricing suits falling token prices, while Tunguz argues demand elasticity could make AI spend behave like copper. Thompson's Stratechery pieces and Amazon's compute posture add a compute-cost angle. *Continuing thread: Usage-pricing and compute-economics threads continue, now framed around pass-through models and demand elasticity.* Sources: [Growth Unhinged](https://www.growthunhinged.com/p/pass-through-pricing-for-ai) · [Tomasz Tunguz](https://tomtunguz.com/jevons-works-on-tokens-not-on-dollars/) · [Stratechery: The Individual Exception](https://stratechery.com/2026/the-individual-exception/) · [Stratechery: Amazon Earnings, The Chip Question, About…](https://stratechery.com/2026/amazon-earnings-the-chip-question-about-agents/)

---

## Must-Read

### 1. [A FAANG PM's Guide to Practical AI Evals](https://www.news.aakashg.com/p/practical-ai-evals)
*Product Growth* — Aakash Gupta (featuring Mahesh Yadav) — Nov 24, 2026  `#AI Strategy`  `#Metrics`

Gupta, with Mahesh Yadav, lays out a four-step process for practical AI evals: define what good means, set the quality bar, scale grading with LLM judges, and keep humans grading. The guide frames evals as a core PM competency rather than an engineering-only task. It also explores how ownership splits between PMs and engineers and what the skill could mean for compensation.

**Why it matters**: Gives a concrete four-step process for building AI evals and clarifies PM versus engineering ownership, directly useful for setting team roles.

- **Define 'good' as yes/no tests.** Break helpful, honest, and harmless into specific, binary checks (e.g., 'did it redact only the needed words?'), and use code-based checks wherever code can verify the output.
- **Set a bar between competitor performance and the realistic ceiling.** Start with a floor at your competitor's level, aim for a bar in the middle, and cap the ceiling near 70-80%. If you land below the bar, narrow the product to the slices it handles correctly about 80% of the time.
- **Train an LLM judge against human experts.** Use human experts first, then build a judge that agrees with them 70-80% of the time, and avoid chasing near-perfect agreement, which can hide problems.
- **Keep sampling human grading after launch.** Have humans review a regular sample of judge outputs (for large systems, perhaps 200-1,000 per week) to catch drift.
- **Own the metrics and the eval questions, and let engineering build the pipeline.** As the PM, define what good means for users, set the launch bar and stage gates, check the judge, and own weekly cost reviews, while engineers build judges and hill-climb quality and cost.

[Read article →](https://www.news.aakashg.com/p/practical-ai-evals)

---

### 2. [Bugs - All Things Product Podcast with Teresa Torres & Petra Wille](https://www.producttalk.org/bugs-all-things-product-podcast-with-teresa-torres-petra-wille/)
*Product Talk* — Teresa Torres (featuring Petra Wille) — Nov 24, 2026  `#AI Strategy`  `#Discovery`

Torres, with Petra Wille, argues that AI products do not have bugs in the deterministic sense, because outputs are better or worse rather than right or wrong. They suggest teams define 'good enough' and reduce categories of errors through error analysis and evals rather than patching individual complaints. Because errors cannot be eliminated entirely, they argue quality must be steered, which requires cross-functional agreement on the standard.

**Why it matters**: Offers a framework for steering AI quality through cross-functional agreement on standards, which is central to shipping AI features at a Series C company.

- **Define 'good' across multiple dimensions:** Break quality into specific criteria, such as tone, length, and fit for the recipient in an email, before deciding whether an output is acceptable.
- **Avoid overfitting to individual complaints:** Don't edit the prompt for every reported error (e.g., adding 'never use em dashes'), since this makes the agent brittle and worse on unseen cases.
- **Fix categories of errors, not single instances:** Collect enough examples, run error analysis to find patterns, and track reductions in error rates over time, accepting that this takes patience.
- **Set a shared 'good enough' bar across the org:** Align product, sales, support, and other teams on an acceptable quality threshold and reset the expectation that every reported bug will be fixed.
- **Treat quality as steerable, not perfect:** Aim to keep the agent on the intended path while leaving it room to maneuver, rather than trying to eliminate every error.

[Read article →](https://www.producttalk.org/bugs-all-things-product-podcast-with-teresa-torres-petra-wille/)

---

### 3. [Engineering at Machine Speed](https://tomtunguz.com/engineering-at-machine-speed-office-hours/)
*Tomasz Tunguz* — Tomasz Tunguz (featuring Dan Shiebler) — Nov 24, 2026  `#Agentic`  `#Org Design`

Tunguz interviews Dan Shiebler, CTO of Artemis Security, who describes merging over 31,000 pull requests in a quarter and shipping most feature requests within 24 hours. He attributes this pace to running several coding agents in parallel. Shiebler argues quality holds only because evaluation pipelines and row-level inspection of failures catch problems continuously.

**Why it matters**: Shows one engineering leader's claimed operating model for running many agents in parallel with continuous evaluation, relevant to scaling delivery speed.

- **Run multiple coding agents in parallel:** Assign each engineer several agents (Artemis reports 4 to 8) working on separate tasks so throughput scales beyond what one person coding by hand can produce.
- **Set a 24-hour target for feature delivery:** Measure how quickly feature requests reach customers and push the team to ship most of them within a day, which forces smaller scopes and faster feedback.
- **Build evaluation pipelines before scaling output:** Automated evals should run on every change so that quality checks keep pace with the volume of pull requests rather than becoming a bottleneck.
- **Inspect failures row by row:** When evals flag problems, look at individual failing cases instead of only aggregate scores to find the specific root causes and fix them quickly.
- **Rethink design, code review, and ownership for agent-driven work:** Expect that high parallelism changes how designs are written, how reviews are done, and who owns each change, so define those processes explicitly for agent output.

[Read article →](https://tomtunguz.com/engineering-at-machine-speed-office-hours/)

---

## All Articles

**4.** [A transparent pricing model for AI](https://www.growthunhinged.com/p/pass-through-pricing-for-ai) — *Growth Unhinged* · Nov 22, 2026  `#AI Strategy`  `#PLG`

AI price-per-token keeps falling and customers are shifting to cheaper models, so software companies struggle to keep pricing current. Pass-through pricing, which charges customers at cost plus a transparent fee, offers trust, control, and automatic adaptation to price changes, as shown by Gumloop's 8% orchestration-fee model.

- **Consider cost-plus pricing for AI-heavy features.** Passing model costs through at list price and charging a separate platform or orchestration fee avoids repricing every time a new model launches or token prices fall.
- **Split your pricing into a pass-through axis and a value axis.** As Clay did, separate low-margin data or compute costs from high-margin platform actions so customers see what they pay for and value is not tied to raw usage.
- **Pick your fee by benchmarking against comparable take rates.** Marketplace and platform take rates typically run about 10% to 20%, and OpenRouter charges 5.5% to 8%. Gumloop chose 8%, high enough to capture value but low enough not to hurt platform usage.
- **Plan for the operational cost of a pricing change.** Gumloop decided in under a month but needed about eight weeks to operationalize, and existing quotes had to be reissued. Budget time for billing, sales collateral, and re-quoting pipeline deals.
- **Make the bill transparent to earn trust.** Opaque credit systems, where customers can't tell what a credit buys, create openings for competitors. Showing exactly what each request costs helps customers control spend and reduces price objections.

**5.** [First principles: What it takes to be a great product manager in the AI era | Sherif Mansour](https://www.lennysnewsletter.com/p/first-principles-what-it-takes-to) — *Lenny's Newsletter* · Nov 22, 2026  `#Org Design`  `#Hiring`

Sherif Mansour, Atlassian's Head of AI and Product Craft, argues that a PM's core job in the AI era is to build a "shared brain" for their team, and that PM roles are growing fastest even as the job changes. The conversation also covers three PM archetypes (artist, scientist, and GM), Atlassian's hiring of junior PMs, and common mistakes new PM managers make.

- **Make the shared brain your primary job:** Centralize the context, decisions, and reasoning your team needs in a place everyone can access, so people stop relying on you as the single source of truth.
- **Identify your PM archetype:** Decide whether you lean toward the artist (craft and user intuition), the scientist (experimentation and evidence), or the GM (ownership and execution), then deliberately build the skills of the other two where you're weakest.
- **Hire and develop junior talent deliberately:** Treat AI as a reason to bring in early-career people who can work fast with new tools, and pair them with clear coaching on product judgment.
- **Avoid the most common new-manager trap:** When you start managing PMs, resist doing their work yourself; set outcomes and standards, then let your reports make and own decisions.
- **Position yourself for growing PM demand:** Focus on the judgment-heavy parts of product work that AI doesn't replace, such as deciding what to build and why, since those are where PM roles are expanding.

**6.** [How Uber built an Internal Marketplace of 5,000 Agent Skills](https://departmentofproduct.substack.com/p/how-uber-built-an-internal-marketplace) — *Department of Product* · Nov 24, 2026  `#Platform Strategy`  `#Dev Tools`

Uber built an internal marketplace of roughly 5,000 agent skills, and the article shares what it learned along the way. It also surveys how other companies, including Perplexity, Figma, and PayPal, have built their own Agent Skills libraries.

- **Treat reusable agent skills as shared internal infrastructure.** Package common agent capabilities as discoverable, versioned skills that teams can find and reuse instead of rebuilding them per product.
- **Study how peer companies structure their skill libraries.** Compare the Perplexity, Figma, and PayPal examples to pick a library structure, naming convention, and ownership model before building your own.
- **Plan for discovery and curation from the start.** A marketplace of thousands of skills only works if people can find the right one, so invest early in search, metadata, and clear ownership.
- **Apply Uber's lessons to your own agent rollout.** Start with a small set of high-demand skills, measure how often teams reuse them, and expand the catalog based on actual usage.

**7.** [Inside Clay’s GTM machine](https://www.growthunhinged.com/p/inside-clay-s-gtm-machine) — *Growth Unhinged* · Nov 23, 2026  `#Product Growth`  `#PLG`

Clay succeeds by pairing heavy GTM automation (account scoring, routing, meeting prep, follow-ups) with human-led relationship building, rather than treating the two as opposites. Its 17 automated workflows prioritize where reps invest their time, while people still review and approve outreach.

- **Replace static scoring with a fit score and propensity model:** Combine firmographic data, AI research fields, and intent signals into a 0-100 fit score written to your CRM, then weight it with engagement and predicted contract value to surface each rep's top 5 accounts weekly.
- **Route leads by fit score and contact seniority:** Send qualified accounts with decision makers straight to AEs, qualified accounts without decision makers to SDRs, and unqualified leads to a self-serve path.
- **Keep humans in the loop on automated outreach:** Have the system draft emails for signals like new executive hires or job changes, but require reps to edit and approve them before sending.
- **Define territories by account size and clear criteria:** Assign accounts to territories only when they cross a fit threshold, have no open opportunity, and lack an owner, and size rep books by segment (e.g., 60 accounts for sales-assist, 45 for the largest enterprise accounts).
- **Automate pre-call preparation to protect rep time:** Send tailored pre-demo emails three days before calls based on lead form responses, and surface account context like product usage, past deal history, and prior loss reasons in a single rep view.

**8.** [Will AI Deflate Like Lightbulbs or Compound Like Copper?](https://tomtunguz.com/jevons-works-on-tokens-not-on-dollars/) — *Tomasz Tunguz* · Nov 24, 2026  `#Market Trends`  `#Metrics`

AI token prices have fallen 43% while usage grew 11.1x, but whether total spending rises like copper or falls like lightbulbs depends on price elasticity of demand. Early evidence from Ramp, OpenRouter, and Anthropic's S-1 suggests demand is elastic enough that GPU and token economics may behave more like copper than lightbulbs.

- **Track spend against volume, not just price per token.** Ramp data shows 11.1x volume against only 4.7x spending, so a falling unit price can still mean a widening gap, and the 2.4x wedge is the number to watch in 2027.
- **Measure your own price elasticity before setting pricing.** Ramp and OpenRouter show a 1% price drop driving 4.3% to 6.8% more tokens, which signals that cutting prices can grow total spend if your customers are similarly price-sensitive.
- **Watch GPU rents as a leading indicator of margin pressure.** Neocloud GPU rents rose 48% and CoreWeave repriced 30% to 50% on lease renewals, so compute costs may not fall as fast as token prices, squeezing lab margins.
- **Lower your inference bill with routing, caching, and smaller models.** Sending easy questions to smaller models, reusing past answers, and using cached tokens (up to 90% cheaper) cut cost per token faster than GPU rents rise.
- **Discount panel data for its biases before drawing conclusions.** Corporate card data misses direct enterprise deals and cloud marketplaces where nearly half of Anthropic's revenue lands, and blended prices mix list cuts with routing to cheaper models.

**9.** [Gemini 4 Neon beat GPT-6.2 and Claude in my 25-task AI benchmark](https://www.lennysnewsletter.com/p/gemini-4-neon-beat-gpt-62-and-claude) — *Lenny's Newsletter* · Nov 25, 2026  `#AI Tools`  `#Metrics`

Claire Vo's 25-task How I AI benchmark, scored blind across six frontier models, names Gemini 4 Neon the surprise winner over GPT-6.2 and Claude. She argues that coding no longer separates the frontier models and introduces a new 'Annoyance Bench' built from her own agent sessions.

- **Run your own blind benchmark on real work:** Build a task set spanning your actual workflows (coding, writing, prototyping, personal assistant), score outputs without knowing which model produced them, and blend in LLM-as-judge ratings to reduce bias.
- **Build an Annoyance Bench from your agent sessions:** Mine your local agent session logs for moments of friction, such as repeated corrections, rework, or ignored instructions, and turn them into scored eval tasks that measure how a model feels to work with.
- **Don't assume coding quality decides the model:** Frontier models now perform similarly on coding, so evaluate on the other dimensions that affect your day-to-day work, like creative output, prototyping, and instruction-following.
- **Factor in speed and cost, not just quality:** A slow model can erode productivity even when its output is excellent, so compare latency and price per task alongside quality scores before committing to a default model.
- **Match models to tasks instead of picking one favorite:** Use the benchmark results to decide where each model earns its place and where you should avoid it, rather than relying on a single preferred model for everything.

**10.** [🎙️ How I AI: OpenClaw for executives: Automate every 1% annoyance](https://www.lennysnewsletter.com/p/how-i-ai-openclaw-for-executives) — *Lenny's Newsletter* · Nov 23, 2026  `#Agentic`  `#Leadership`

Ankit Maheshwari, CTO of Innovaccer, shows how he built a personal AI chief of staff called Jarvis on OpenClaw that handles approvals, lunch orders, coworker follow-ups, restaurant bookings, and smart home controls. His core argument is that small, frustrating tasks are the best entry points for agents, and that control, specialized agents, and strict guardrails make such a system trustworthy.

- **Automate the bottleneck before the grand vision.** Start with one recurring, painful task, like a cron job that briefs you every four hours on items awaiting approval, and expand only after it works.
- **Apply the '1% annoyance' rule.** If a task is slightly frustrating and repeats a few times, automate it. This is how you find candidates for agents such as lunch ordering, unanswered Slack follow-ups, and home automation.
- **Split work across specialized agents once tasks get complex.** Move distinct workflows, such as voice calls, into dedicated agents with narrow scopes so persona and behavior stay consistent and orchestration stays separate from execution.
- **Invest more in agent instructions than in integrations.** Define each agent's personality, boundaries, permissions, and routing in files like soul.md, and expect more iteration on these instructions than on connecting the tools.
- **Set explicit limits for worst-case actions and optimize model costs early.** Define hard limits for high-impact approvals, such as job-role changes, before an incident occurs, and test cheaper local models for summaries, email, and cron checks while reserving frontier models for complex browser work.

**11.** [OpenClaw for executives: Automate every 1% annoyance | Ankit Maheshwari (Innovaccer)](https://www.lennysnewsletter.com/p/openclaw-for-executives-automate) — *Lenny's Newsletter* · Nov 23, 2026  `#Agentic`  `#AI Tools`

CTO Ankit Maheshwari shows how he built an OpenClaw-based assistant, "Jarvis", on a Mac Mini that began by clearing his work approvals and expanded into personal tasks like ordering lunch, booking reservations, and controlling his smart home. He argues that well-scoped subagents, clear guardrails, and automating small daily annoyances make personal AI agents trustworthy, and he is testing whether a cheaper local model can replace his $500-to-$600-a-month Anthropic bill.

- **Start automation with the bottleneck you feel most.** Maheshwari began by automating the approvals that were slowing him down at work, then expanded the system to other tasks once it proved reliable.
- **Split agents into well-scoped subagents instead of one global agent.** A single agent hallucinated across personas, so he used separate subagents (such as a health coach, email triage, and a master soul file) for clearer behavior.
- **Apply the 1% annoyance rule to pick what to automate next.** Look for small, recurring frictions like ordering food, booking restaurants, or adjusting the AC, since each one saves time and builds trust in the system.
- **Build guardrails before giving an agent real-world actions.** Define what the agent can do on its own and what needs confirmation, and test those limits mid-task, since trustworthiness depends on these boundaries.
- **Benchmark a local model against your current API bill before switching.** Maheshwari is pressure-testing GLM 5.3 Flash to see which tasks it can handle and whether it can meaningfully cut recurring model costs.

**12.** [I made my entire podcast available to your AI](https://www.news.aakashg.com/p/pod-transcripts-github) — *Product Growth* · Nov 26, 2026  `#AI Tools`  `#Creator Economy`

Aakash Gupta has released transcripts of all 166 episodes of his podcast on GitHub and, for annual subscribers, an MCP server that lets AI assistants search the podcast's guest knowledge with timestamps and context files. He argues this gives PMs more accurate, cheaper, and faster answers than general-purpose AI, and he runs a $1,200 contest to encourage builders to create products with it.

- **Pull guest advice into your AI workflows:** Add the Growth Podcast MCP to your Claude Code projects (or your PM OS, Job Search OS, or Content OS) and add a CLAUDE.md line telling it to search the podcast whenever a task touches a company, person, or topic a guest covered.
- **Upgrade PRDs with practitioner evals:** When drafting a PRD, ask the assistant to pull eval practices from guests, including a held-out test set, evals that are expected to fail, and a golden set that grows from production logs, rather than settling for a generic checklist.
- **Prepare for AI PM interviews with real guest insight:** Ask your assistant to role-play an interviewer at a target company using specific guests' views on how that company builds and hires, then compare your answers against what a strong response should cover.
- **Resolve team debates with sourced quotes:** When experts disagree, such as on prototyping before writing a spec, ask the MCP for opposing guest advice with exact quotes and timestamps from each side before deciding.
- **Research technical choices before building:** For a side project, ask what architectures and stacks guests who built similar products chose, with timestamps, to ground your decisions in real builder experience.

**13.** [What AI Hiring Managers Want Right Now](https://theskip.substack.com/p/what-ai-hiring-managers-want-right) — *The Skip* · Nov 24, 2026  `#Hiring`  `#Leadership`

The article examines how hiring for AI-era PM roles has shifted, what has stayed the same, and how candidates can position themselves to land a PM role now. Only the title and subtitle were provided, so this summary is based on those alone.

- **Map your AI experience to real product outcomes.** Describe what you built or shipped with AI tools and the measurable result, rather than listing tools you have used.
- **Prepare for AI-specific interview formats.** Expect questions on evals, prototyping, and how you would judge AI feature quality, and practice answering them out loud.
- **Keep the fundamentals that still get hired.** Strong product sense, prioritization, and clear communication with stakeholders remain central, so don't swap them out for AI buzzwords.
- **Build a small, demonstrable portfolio.** Create a working prototype or case study that shows your judgment on an AI problem, and be ready to walk through your decisions.
- **Treat your job search as an ongoing process.** Revisit your positioning and interview prep regularly, because hiring expectations are changing quickly.

**14.** [🧠 Community Wisdom: Handling context switching with multiple agents, giving feedback on AI-generated designs, getting AI to write less like AI, why PMs don’t share what they’re really working on](https://www.lennysnewsletter.com/p/community-wisdom-handling-context) — *Lenny's Newsletter* · Nov 21, 2026  `#Leadership`  `#Agentic`

This weekly Community Wisdom edition, a subscriber-only roundup from Lenny's member Slack, shares peer advice on managing context switching across multiple AI agents, giving feedback on AI-generated designs, making AI writing sound less like AI, and why PMs often don't share what they're really working on. The article text provided is only the introduction, so the takeaways below are drawn from the headline topics.

- **Batch your agent check-ins.** Rather than jumping between several running agents, group reviews into set windows so each context switch costs less focus.
- **Give feedback on AI designs against the goal, not the output.** State the user problem and success criteria first, so critiques target the intent instead of the polish of generated mockups.
- **Edit AI drafts for voice before publishing.** Strip stock phrasing and hedges, and add specific examples and your own opinions so the text reads as yours.
- **Share works-in-progress early and briefly.** Post short updates on what you're exploring and why, so stakeholders see your priorities and can help before work is finished.
- **Track where your attention actually goes.** Note your interruptions and agent handoffs for a week to find the bottlenecks you can reduce or delegate.

**15.** [🔵 Replit, Google and Vercel are betting on Agent Swarms](https://departmentofproduct.substack.com/p/replit-google-and-vercel-are-betting) — *Department of Product* · Nov 22, 2026  `#Agentic`  `#Platform Strategy`

The newsletter covers Replit, Google, and Vercel betting on agent swarms, alongside Anthropic's record-breaking IPO, Google making its Gemini agent free, and Gusto's CTO arguing that teams don't need a PRD. The full article text was not provided, so this summary is based only on the title and teaser.

- **Test multi-agent workflows on a narrow task first:** Platforms like Replit, Google, and Vercel are investing in agent swarms, so pick one repeatable product workflow and pilot coordinated agents on it before scaling.
- **Re-evaluate whether your PRD is still the right artifact:** Gusto's CTO argues teams can ship without a PRD, so try a lightweight alternative such as a one-page problem statement with success metrics on your next feature.
- **Watch falling agent access costs when planning roadmaps:** Google making its Gemini agent free lowers the barrier to adoption, so reassess which AI-assisted features are now affordable to build and offer to users.
- **Track how frontier AI company IPOs shape vendor risk:** Anthropic's record IPO signals heavier investment in the platforms your product may depend on, so review vendor dependencies and build fallback options into your architecture.

**16.** [The Individual Exception](https://stratechery.com/2026/the-individual-exception/) — *Stratechery* · Nov 24, 2026  `#Org Design`  `#Market Trends`

Ben Thompson argues that AI is letting individuals do work that once required teams for weeks or months, while the most valuable companies keep shrinking their headcount relative to revenue and market cap. He uses Jensen Huang's reinstatement at Nvidia as evidence that tech is turning business back toward individual vision and away from managerial bureaucracy.

- **Build small, end-to-end tools yourself:** Use AI to create the internal apps, dashboards, and device controls your workflow needs, instead of waiting for a team to build them. The article's author built a studio control service, a screen-sharing client, and a status board this way.
- **Route agent work to the right machines:** Give your agent a harness that splits tasks across your own hardware based on load and platform, such as a Mac for iOS builds, a GPU PC for heavy compute, and a Linux server for general work.
- **Measure output per person, not headcount:** Track revenue or market cap per employee as a benchmark for how much leverage your team gets from AI. Compare it against past peers to see whether your org is actually getting more productive.
- **Plan for founder-driven organizations:** When a company's value depends on one person's vision, document the reasoning behind key decisions so it survives leadership changes. Thompson's Nvidia analysis suggests that over-reliance on a single leader is a concentrated risk.
- **Expect scrutiny of concentrated power:** Recognize that a singular, high-leverage operator can attract intense regulatory and political attention, so plan governance, compliance, and reputational safeguards early.

**17.** [Amazon Earnings, The Chip Question, About Agents](https://stratechery.com/2026/amazon-earnings-the-chip-question-about-agents/) — *Stratechery* · Nov 23, 2026  `#Market Trends`  `#Competitive Strategy`

Amazon argues that it is not a typical compute provider, even as it signals a willingness to accept lower margins to serve frontier AI labs. The full article is paywalled, so this summary relies only on the public teaser.

- **Separate commodity compute from frontier-serving capacity** when comparing cloud providers, since Amazon is positioning itself as different from other compute vendors.
- **Track margin trade-offs in AI infrastructure earnings** by watching whether cloud providers accept thinner margins to win frontier model customers.
- **Re-check your AI infrastructure assumptions against the Amazon earnings details** in the full Stratechery piece before making vendor or capacity decisions.
- **Compare Amazon's pitch with the existing Amazon notes in your vault** to see whether its positioning on compute has changed over the year.

**18.** [TBM 453: How to Get Unstuck Without Losing Yourself (or Pretending Everything Is Fine)](https://cutlefish.substack.com/p/tbm-453-how-to-get-unstuck-without) — *The Beautiful Mess* · Nov 26, 2026  `#Leadership`

The article argues that being stuck is not always a failure: staying in a difficult problem can be productive as long as it is worth wrestling with. It asks how to move forward without abandoning yourself or pretending everything is fine.

- **Name the thing you're stuck on.** Write one sentence describing the unresolved problem so you can tell whether you're circling a real tension or just avoiding it.
- **Separate productive struggle from avoidance.** Ask whether each week brings new understanding or only repeats the same frustration, and change your approach if it's the latter.
- **Stay honest about your current state.** Acknowledge to yourself and one trusted colleague what isn't working, instead of performing confidence you don't feel.
- **Protect your identity while changing course.** Before you change direction, list the values and skills you want to keep, so the shift doesn't require discarding who you are.
- **Set a check-in date for the stuckness.** Choose a point to reassess whether the difficulty is still worth the effort, and decide in advance what you'll do if the answer is no.

**19.** [Partnering with Isomorphic Labs: Drug Discovery Is an AI Problem](https://www.sequoiacap.com/article/partnering-with-isomorphic-labs-drug-discovery-is-an-ai-problem) — *Sequoia Capital* · Nov 23, 2026  `#Market Trends`  `#Startups`

Sequoia Capital's partnership announcement introduces Isomorphic Labs, whose stated mission is to improve human health by solving disease with AI. The article frames drug discovery as fundamentally an AI problem, though the provided text is only a one-line description.

- **Treat drug discovery as a data and modeling problem:** Evaluate biotech and health bets by asking whether the company's advantage comes from proprietary data, models, and computation rather than only from lab work.
- **Look for mission-driven AI teams with deep technical leadership:** Isomorphic is led by Demis Hassabis and Max Jaderberg, so assess founder and research-team depth when judging whether an AI-for-science company can execute on a long-horizon goal.
- **Track the bottleneck, not the headline:** Before backing or building in AI-driven health, identify which stage (target identification, molecule design, clinical validation) AI actually shortens, and measure progress there.
- **Read the full article before acting:** The provided text is a single sentence, so verify the specifics of the partnership, its terms, and any milestones in the original Sequoia post before drawing conclusions.


## Trending on GitHub

**[Marvisak/VIctory](https://github.com/Marvisak/VIctory)** (⭐ 13,784 · Rust)
An attempt at running GTA VI on PC
*Hype-driven GTA VI-on-PC compatibility project; a reminder that viral repos draw traffic fast, and unverified binaries are a security risk.*

**[4lwayz/portwatch-vi](https://github.com/4lwayz/portwatch-vi)** (⭐ 6,682 · JavaScript)
Does GTA VI run on PC yet? A live tracker of community recompilation and emulation efforts, updated daily.
*Daily tracker of GTA VI PC recompilation and emulation efforts; a clear gauge of community demand, though it verifies no working playable build.*

**[EL4CTEO/fast-anything](https://github.com/EL4CTEO/fast-anything)** (⭐ 4,445 · Rust)
Don't rewrite it in Rust. Rewrite the 5% that's slow: profile your app, port the hot functions with your coding agent, prove they behave the same. Python, JS/TS, Ruby, Java, Kotlin, Go, PHP, C/C++, C#, R.
*Profile-driven porting of hot functions to Rust across ten languages, using coding agents, offers a low-risk path to performance gains without costly full rewrites.*

**[fxceless/victory-fork](https://github.com/fxceless/victory-fork)** (⭐ 3,357 · Rust)
Work-in-progress fork of VIctory: getting an Xbox Series title to render and run on a Windows PC. No game files.
*Work-in-progress fork pursuing Xbox Series rendering on Windows PC, a reminder that platform lock-in is being actively probed and that IP exposure is real.*

**[trustno1-coder/VIctory-NVIDIA](https://github.com/trustno1-coder/VIctory-NVIDIA)** (⭐ 2,834 · Rust)
VIctory (Xbox Series compatibility layer) tuned for NVIDIA RTX cards: Series X at 2560x1440 with DLSS, about 26-30 fps on an RTX 5070, DLSS frame generation 2x-6x, an F1 settings menu and F3 stats panel, open water without dark blocks. Built on many repos combined into one. No game files or NVIDIA files included.
*Community fork tuned for NVIDIA RTX with DLSS frame generation, showing how quickly rendering tech spreads through open source; its performance claims remain unverified.*


## Trending on Hacker News

**[Nvidia Reinstates Jensen Huang as CEO](https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html)** (▲ 2,858 · 💬 3,830) — [discussion](https://news.ycombinator.com/item?id=50611576)
*Nvidia's CEO reinstatement signals strategic continuity at the dominant AI-infrastructure supplier, so plan GPU costs and roadmap dependencies accordingly.*

**[Ladybird is now in alpha](https://ladybird.org/posts/alpha/)** (▲ 2,467 · 💬 741) — [discussion](https://news.ycombinator.com/item?id=50614249)
*Ladybird's alpha signals an independent browser engine nearing real use, a reminder that Chromium's dominance is contestable for web-platform bets.*

**[Holy shit holy shit holy shit holy shit: The magnitude of what’s now happening](https://scottaaronson.blog/?p=10379)** (▲ 2,033 · 💬 1,879) — [discussion](https://news.ycombinator.com/item?id=50646108)
*Viral AI-acceleration post reflects widespread urgency about AI; treat it as a signal of competitive pressure, not evidence to drive roadmap decisions.*

**["Dario is hyping the dangers so OSS models are illegal and he stays in control"](https://twitter.com/ylecun/status/2124550037912920090)** (▲ 2,024 · 💬 1,207) — [discussion](https://news.ycombinator.com/item?id=50615308)
*Debate over restricting open models shows regulatory risk to self-hosted AI options, so keep vendor-agnostic model strategies and monitor policy closely.*

**[Jensen Huang Reinstated as Nvidia CEO](https://nvidianews.nvidia.com/news/nvidia-board-reinstates-jensen-huang-as-president-ceo-and-board-director)** (▲ 1,714 · 💬 4) — [discussion](https://news.ycombinator.com/item?id=50611588)
*Duplicate of the Nvidia CEO story with minimal discussion; treat the higher-engagement thread above as the substantive read on Nvidia's leadership direction.*

