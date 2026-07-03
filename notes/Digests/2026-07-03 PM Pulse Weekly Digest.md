# PM Pulse: Weekly Digest — Jul 03, 2026

15 articles from 8 feeds | Jun 26 – Jul 03, 2026

---

## This Week

**AI isn't a feature category anymore—it's collapsing your org design, your cost structure, and your hiring playbook.**

This week reveals a fundamental shift: AI adoption isn't about bolting agents onto existing products. It's about reorganizing how teams build, how you price, and who you hire. Three themes emerge: (1) frontier models are becoming a cost liability, not an asset—routing logic and cheap local models are the real lever; (2) small, empowered teams shipping with Claude Code are outpacing traditional org structures, making 'taste' more valuable than process; (3) enterprise buyers are systematically defunding seat-priced SaaS, shifting budget to AI infrastructure and developer tools. For a Series C PM leader, this means your roadmap and org design are out of sync. You need to rethink unit economics before scaling headcount, and fast.

- Model routing, not model selection — most AI work is cheaper and faster with local/async processing; frontier models should be exceptions, not defaults
- Org structure is collapsing — small, autonomous teams with direct access to coding tools are outshippiing traditional PM/Eng/Design silos; 'taste' matters more than process
- Enterprise SaaS is stratifying — seat-priced software is defunding; winners are infrastructure, security, and developer tools; category now outweighs growth rate
- Cost structure is becoming competitive advantage — frontier model compute is 2.3x payroll at scale; unit economics of AI workflows will separate winners from losers by 2029

---

## Must-Read

### 1. [Most AI Work Can Wait](https://www.tomtunguz.com/ai-execution-routing/)
*Tomasz Tunguz* — Tomasz Tunguz — Jul 01, 2026  `#AI Strategy`  `#Roadmapping`

Tomasz Tunguz argues most AI workloads don't need expensive frontier models. The real optimization is building a smart routing layer that classifies tasks and directs 70–80% of traffic to cheap local models or async batch processing. This flips the typical PM instinct (pick the best model first) and has immediate implications for your unit economics, feature prioritization, and competitive positioning. If your roadmap assumes Sonnet or GPT-4, you're likely leaving money on the table.

**Why it matters**: Directly impacts your product cost model and roadmap prioritization—routing cheap models correctly is more valuable than model selection.

- **Design the router first.** Build a three-layer routing system (skill classifier, router, model selector) that decides which tier of model handles each request before selecting any specific model.
- **Queue async work aggressively.** Most tasks like drafting replies, summarizing repos, and running evaluations don't need real-time responses—batch async inference costs two orders of magnitude less than real-time inference.
- **Implement dual feedback loops.** Use synchronous predictors to catch known-hard tasks before failure and nightly batch evaluators to discover new failure modes and update router weights without expensive real-time inference.
- **Separate classification from routing decisions.** Keep intent recognition (skill classifier) distinct from scheduling logic (router) to enable A/B testing different models against the same operation.

[Read article →](https://www.tomtunguz.com/ai-execution-routing/)

---

### 2. [No Figma. No Jira. No docs. How Gusto built a new product line with Claude Code | Eddie Kim (CTO)](https://www.lennysnewsletter.com/p/no-figma-no-jira-no-docs-how-gusto)
*Lenny's Newsletter* — Lenny Rachitsky (featuring Eddie Kim) — Jun 29, 2026  `#AI Tools`  `#Org Design`

Gusto's five-person team shipped a production AI product (Gusto Cofounder) in 10 weeks using Claude Code, eliminating traditional Jira, design docs, and standups. Eddie Kim's case study shows the org design implications: fewer handoffs, direct shipping authority, and rapid iteration beat process rigor at this stage. This challenges conventional Series C scaling (hiring managers, adding process layers) and suggests a different org structure may be competitive. The model is reproducible and shows what happens when you give small teams the right AI tools.

**Why it matters**: Demonstrates how to ship complex products faster with smaller teams; directly relevant to scaling org and managing costs as Series C.

- **Use the trash-can method** for product decisions: write full PRs, review them thoroughly, then delete them as a planning artifact instead of creating separate design docs—this compresses decision cycles and keeps decisions tied to actual code.
- **Build with minimal tooling**: Gusto's stack (Claude Code + Cloudflare Workers + Vercel AI SDK) eliminated the need for Figma, Jira, and documentation tools, reducing context switching and accelerating shipping velocity.
- **Hire for learning velocity over credentials**: The team included a designer with no engineering background who hit the 94th percentile for code shipping—focus on adaptability and willingness to learn new tools over traditional qualifications.
- **Run eval-first workflows in Claude Code** to catch real customer bugs: use evaluations to validate fixes before shipping, turning bug reports into test cases that ensure production quality.
- **Give small teams permission to experiment**: Five people with autonomy, a clear 10-week deadline, and daily synchronous communication (perma-Zoom) shipped a tier-one product faster than traditional org structures allow.

[Read article →](https://www.lennysnewsletter.com/p/no-figma-no-jira-no-docs-how-gusto)

---

### 3. [How top PMs increase their leverage with AI](https://www.lennysnewsletter.com/p/how-top-pms-increase-their-leverage)
*Lenny's Newsletter* — Lenny Rachitsky (featuring Colin Matthews) — Jun 30, 2026  `#AI Tools`  `#Org Design`

Lenny and Colin Matthews describe how top PMs are shifting from coordination to active building by using Claude Code, agents, and MCPs to complete entire tasks end-to-end. This isn't about PMs learning to code—it's about PMs becoming force multipliers by doing work directly (wireframes, analysis, prototyping) rather than delegating. This has hiring implications (what skills do you prioritize?) and org implications (flatter teams, fewer specialists). It's a fundamental reshaping of the PM value proposition and directly affects how you staff for growth.

**Why it matters**: Redefines the PM role in AI-native companies; critical for deciding how to hire, promote, and structure your product team.

- **Understand your leverage rung**: Assess whether you're at assistance level (AI helps you write), artifact level (AI creates outputs), or delegation level (AI completes full tasks) for personal leverage, and intentionally move up rungs based on task complexity.
- **Connect AI to external tools**: Use MCPs to connect Claude to analytics platforms like PostHog or Amplitude to complete multi-step analysis tasks automatically, freeing yourself from manual data review and enabling faster insights.
- **Build AI-powered systems**: Create repeatable workflows with AI agents that can handle multi-step tasks, validate their own work, and integrate with your actual codebase and production tools for genuine systems leverage.
- **Master prototyping with real code**: Move beyond static mockups by using Claude Code and similar tools to prototype directly in your company's codebase, enabling faster validation and easier handoff to engineering.
- **Invest in AI skills progression**: Enroll in structured training (like the "Become an AI-Native Builder" course) to systematically develop skills with tools like Codex, Claude Code, and Cursor rather than learning ad-hoc.

[Read article →](https://www.lennysnewsletter.com/p/how-top-pms-increase-their-leverage)

---

## All Articles

**4.** [The CIO's Choices are Clear in 2026](https://www.tomtunguz.com/cio-choices-clear-2026/) — *Tomasz Tunguz* · Jun 30, 2026  `#Market Trends`  `#Enterprise`

CIOs are systematically defunding traditional seat-priced SaaS applications and investing heavily in AI infrastructure, security, and developer tools, creating a clear market divergence where category matters far more than growth rates.

- **Prioritize infrastructure and security investments**: Infrastructure & Dev Tools (+68.5% 1Y) and Security (+17.6% 1Y) are the only positive SaaS sectors; allocate budget toward AI compute, data stacks, and defense tools rather than horizontal applications.
- **Recognize seat-based model vulnerability**: Business applications (-36.2% 1Y) are being decimated as AI agents substitute for human workers; if your product relies on per-seat pricing, expect margin compression and plan alternative monetization strategies.
- **Position products on the AI token path**: Companies that facilitate AI workflows (messaging, compute, routing, data querying) command premium multiples; evaluate whether your product is a payment processor for AI agents or a traditional software business.
- **Track category trends over growth metrics**: The market separates winners from losers by sector, not growth rate; two 21% growth companies are valued at 10.8x and 3.4x multiples depending on whether they serve AI infrastructure or traditional applications.
- **Monitor agent substitution threats**: Salesforce's reduction from 9,000 to 5,000 employees with Agentforce handling 50% of interactions signals that any role performing routine interactions faces replacement risk within 12-18 months.

**5.** [When AI Costs More Than the Engineer](https://www.tomtunguz.com/ai-spend-breakeven-2029/) — *Tomasz Tunguz* · Jun 29, 2026  `#AI Strategy`  `#Metrics`

Anthropic spends 2.3x its payroll on compute costs, creating a structural cost gap with the rest of the software market; three scenarios show how this gap may or may not close by 2029 depending on token pricing, model competition, and agentic workflow adoption.

- **Model your AI cost scenarios**: Map three trajectories for 2027-2029 (Bear: token deflation, Base: top-1% growth tapers, Bull: rest of market reaches Anthropic's 2.3x ratio) to stress-test whether your financial model treats AI as optional or structural.
- **Plan for agentic workflows**: Goldman Sachs projects 24x token consumption growth by 2030 as agentic AI replaces chat interfaces; if competitors ship features faster with high-compute workflows, rationing by role or workload becomes a competitive necessity.
- **Track the top-1% spending baseline**: Top-tier SaaS companies already spend $89k/engineer/year on AI (40% of senior engineer salary); the median spends $137/year, creating a 680x gap that will compress—prepare for your AI bill to rise from 0.06% to 2.3x of payroll over three years in the Bull case.
- **Hedge with open-weight models**: DeepSeek-V3 and similar models deliver frontier-comparable performance at 1/10th to 1/30th the cost of proprietary APIs; mixing frontier and open-source SKUs can bend the cost curve even if token prices stabilize.

**6.** [Sonnet 5 review: I ran 64 generations to find out if it's worth it](https://www.lennysnewsletter.com/p/sonnet-5-review-i-ran-64-generations) — *Lenny's Newsletter* · Jun 30, 2026  `#AI Strategy`  `#Metrics`

Lenny Rachitsky built a repeatable evaluation framework (the How I AI Bench) using Claude Code to rigorously test Sonnet 5 against four other frontier models across multiple tasks, revealing surprising results that differ from vendor claims and one-off vibe checks.

- **Build repeatable evals instead of one-off tests** — Create a systematized scoring framework combining human judgment (70%) with LLM-as-judge (30%) to get reliable, comparable results across model releases over time.
- **Use local HTML scoring pages with JSON exports** — Set up a simple interface to rate AI outputs on gut feel and export structured data, making it easy to iterate on evaluation criteria and aggregate scores.
- **Match models to specific tasks rather than declaring winners** — Different models excel at different tasks (PRDs, prototypes, agents, personality), so make model-by-task recommendations instead of using a single leaderboard rank.
- **Run blind comparisons with 64+ generations** — Test enough samples across multiple dimensions to surface patterns that individual tests would miss and validate vendor claims against real-world performance.

**7.** [OpenAI Codex lead on the new shape of product work | Andrew Ambrosino](https://www.lennysnewsletter.com/p/openai-codex-lead-on-the-new-shape) — *Lenny's Newsletter* · Jun 28, 2026  `#AI Tools`  `#Leadership`

Andrew Ambrosino, lead of OpenAI's Codex desktop app, discusses how AI has fundamentally transformed product development by collapsing traditional roles and elevating 'taste' as the most critical skill for product leaders in an AI-first workplace.

- **Develop taste as your core competency**: In an AI-first world where everyone can build, taste—the ability to make nuanced judgment calls on what's right—has become the most valuable and irreplaceable professional skill for product leaders.
- **Adopt zone defense product management**: Instead of role-based ownership, organize teams where PMs operate like zone defenders who can move fluidly across areas, enabling faster decision-making when everyone has building capabilities.
- **Time your product launches strategically**: The Codex app would have failed if launched in November but succeeded in February because the market maturity and user capability level had fundamentally shifted, illustrating the importance of product-market timing in AI.
- **Use AI tools to run your own workflows**: Leaders should personally use the tools they're building (Andrew uses Codex for his workflows) to develop authentic intuition about user needs rather than relying solely on feedback loops.
- **Build toward integrated coordination hubs**: Design products as home bases that coordinate work across multiple platforms (ChatGPT, Codex, existing tools) rather than isolated point solutions to maximize utility and adoption.

**8.** [🎙️ How I AI: GLM-5.2 review & How Gusto built a new product line with Claude Code](https://www.lennysnewsletter.com/p/how-i-ai-glm-52-review-and-how-gusto) — *Lenny's Newsletter* · Jun 29, 2026  `#AI Strategy`  `#Dev Tools`

Open-weight models like GLM-5.2 are now production-grade alternatives to frontier models, and small teams can ship tier-one products in weeks using Claude Code with minimal process overhead.

- **Test open-weight models in rotation**: GLM-5.2 delivers Opus-level performance at 72% lower cost for long-running agentic tasks—worth piloting alongside closed models rather than as a full replacement, especially for frontend and design work.
- **Strip process to its essentials when AI is your builder**: A five-person team shipped a tier-one product in 10 weeks with no PM, Jira, Figma, or specs by letting Claude Code handle engineering coordination and replacing text threads with shared AI context.
- **Self-host when scale matters**: Open-weight models eliminate vendor lock-in and API pricing pressure—running GLM-5.2 through Open Router took 30 minutes to configure and cost $3.36 for 6 million tokens versus frontier model rates.
- **Persistent AI context replaces human standups**: A permanent Zoom room with Claude Code running continuously gives you the equivalent of a senior engineer always available and always current on codebase state, eliminating async coordination friction for small teams.
- **Watch the React consistency boundary**: GLM-5.2 handles HTML/CSS reliably but struggled with TypeScript and React under multi-step agentic pressure—test your specific tech stack before committing open-weight models to critical paths.

**9.** [GitHub for PMs: Version Control for Everything You Build With AI](https://www.news.aakashg.com/p/github-for-pms) — *Product Growth* · Jun 27, 2026  `#AI Tools`  `#Roadmapping`

This article provides a comprehensive guide for product managers to use GitHub as version control for AI artifacts, personal workspaces, and project files, addressing the problem of AI workspace drift and lost prompt versions by implementing systematic tracking and collaboration workflows.

- **Implement three-tier repo structure**: Create separate GitHub repositories for your private PM workspace (Repo 1), shared team tools and skills (Repo 2), and active project work (Repo 3) to organize and version control all AI artifacts.
- **Establish daily commit discipline**: Follow a consistent seven-step workflow (pull, branch, commit, push, review, merge) using natural language commands in Claude Code to track changes to CLAUDE.md files, skills, and eval criteria without memorizing git syntax.
- **Secure your GitHub setup before launch**: Use the provided .gitignore template and run secret scans to remove API keys, sensitive customer data, internal strategy documents, and personal context before pushing any PM workspace to GitHub.
- **Enable cross-device access and recovery**: Store your PM OS infrastructure on GitHub to enable instant setup on new machines, access via iOS Claude Code app, and ability to restore previous skill or prompt versions when performance degrades.
- **Strip personal context from shared tools**: When building Repo 2 for team collaboration, completely remove company-specific and personal context so other PMs can fork and adapt your skills, templates, and configurations to their own workspaces.

**10.** [Please stop the AI Confidence Theater](https://www.elenaverna.com/p/please-stop-the-ai-confidence-theater) — *Elena's Growth Scoop* · Jul 02, 2026  `#Positioning`

Elena Verna critiques the pervasive 'AI Confidence Theater' where people exaggerate their AI capabilities and use cases, creating false baselines that demoralize others and obscure genuine, valuable applications of AI tools.

- **Demand proof over claims**: When someone shares an AI success story, ask them to demonstrate it and show you a critical workflow that would actually break without it—most won't have one.
- **Reframe your AI wins as incremental**: Stop waiting to celebrate 'life-changing' AI moments; instead appreciate and build on small time-saves like meeting summaries or email drafting that genuinely improve your day.
- **Revamp your hiring process for AI roles**: Move beyond verbal interviews and AI jargon fluency; require case studies and work trials to distinguish between people who sound competent versus those who can actually build and deploy working AI systems.
- **Resist the false baseline comparison**: Recognize that social media-amplified AI use cases aren't representative; stop feeling behind because others claim radical transformations, and focus on your actual workflow improvements.
- **Build authentic messaging for AI products**: Move away from marketing certainty for inherently uncertain tools; instead communicate the specific contexts where AI works, the limitations, and the real outcomes users should expect.

**11.** [The AI-Native PM Roadmap: A Live Session Every Week, First 3 Free](https://www.productcompass.pm/p/ai-native-pm-roadmap) — *Product Compass* · Jul 01, 2026  `#AI Tools`

Pawel Huryn is launching a weekly live training series to help PMs move from theoretical understanding of AI agents to practical hands-on implementation, with the first three sessions free and covering progression from Cowork to Claude Code.

- **Start with hands-on practice** – Moving from theory to actually using VS Code and agents requires doing the work, breaking things, and fixing them rather than just reading or listening to content.
- **Commit to weekly 90-minute sessions** – The live sessions run every Thursday at 6:00 PM CET with recordings available, allowing you to apply each skill directly to your own product as homework.
- **Leverage the free trial period** – Take advantage of the first three free sessions covering Cowork, Codex, and Claude Code to determine if the premium roadmap suits your learning pace before committing.
- **Build toward production readiness** – The full roadmap progresses from foundational agent work toward Agentic Engineering and Production Hardening, with a certificate available upon completion of knowledge tests and practical exercises.
- **Close the two-speed PM gap** – Recognize that product management is splitting between PMs who work with agents daily and those who haven't started; this series helps bridge that growing divide within weeks rather than months.

**12.** [Great Products, Bad Companies](https://www.svpg.com/great-products-bad-companies/) — *SVPG* · Jun 30, 2026  `#Leadership`  `#Startups`

Great products alone are insufficient for building great companies; successful product companies often become targets for opportunistic leaders who prioritize short-term financial gains over long-term value, a problem that alternative corporate governance structures can help prevent.

- **Recognize that great products attract predators** - Companies known for producing excellent products become attractive targets for board members and investors motivated by quick financial wins rather than sustainable value creation.
- **Understand corporate governance's impact on product work** - Corporate governance structures directly affect your ability to succeed as a product person; traditional governance approaches often fail to protect companies from destructive leadership changes.
- **Adopt mission-locked governance structures** - Explore alternative governance models designed to protect companies from threats and preserve founder vision, as some leading companies have already implemented these protective structures.
- **Vote with your feet as a product creator** - When evaluating companies to join or lead, prioritize those with governance structures that protect long-term mission and culture over those vulnerable to predatory takeovers.

**13.** [🧠 Community Wisdom: Beating a career slump, adding more structure to an established team, questions for new-team 1:1s, the evolving shape of the growth role, and more](https://www.lennysnewsletter.com/p/community-wisdom-beating-a-career) — *Lenny's Newsletter* · Jun 27, 2026  `#Org Design`

This Community Wisdom edition curates the most valuable discussions from Lenny's subscriber Slack community, covering practical advice on career development, team management, and evolving professional roles.

- **Address career slumps proactively** by seeking structured feedback from mentors and peers in your community to identify root causes and develop actionable recovery plans.
- **Implement layered structure gradually** when scaling established teams by documenting processes and creating clear frameworks without disrupting existing culture.
- **Prepare targeted 1:1 questions** for new team members that focus on understanding their strengths, motivations, and how they prefer to work rather than just surface-level information.
- **Stay current with role evolution** by recognizing how growth roles are changing and adapting your skill set to include cross-functional collaboration and strategic thinking beyond traditional metrics.

**14.** [Celebrate People like Om Malik and Susan Wojcicki When They’re Alive. That’s the Best Chance We Have To Make Tech Good Again.](https://hunterwalk.com/2026/06/29/celebrate-people-like-om-malik-and-susan-wojcicki-when-theyre-alive-thats-the-best-chance-we-have-to-make-tech-good-again/) — *Hunter Walk* · Jun 29, 2026  `#Leadership`

Hunter Walk reflects on the deaths of Susan Wojcicki and Om Malik, calling for the tech industry to celebrate and acknowledge role models for their kindness and character while they're alive, rather than only after they pass.

- **Celebrate people now**: Recognize and honor people in your industry for their character, kindness, and contributions to others while they're still alive to experience that appreciation.
- **Identify role models**: Look for the next generation of leaders like Wojcicki and Malik who combine professional success with genuine humanity and approachability.
- **Set moral examples**: Use the example of how well-liked these leaders were as a benchmark for what tech's moral compass should look like and aspire to build that culture.
- **Build community around values**: Create environments where being successful doesn't require sacrificing kindness, and where generosity and approachability are celebrated traits.

**15.** [Summer Break: Week of June 29](https://stratechery.com/2026/summer-break-week-of-june-29/) — *Stratechery* · Jun 29, 2026

Stratechery is taking a summer break the week of June 29 with no weekly article or updates, resuming regular publication on July 6.

- **Plan your content calendar** around summer breaks to maintain reader expectations and communication about publication schedules
- **Maintain some content flow** by continuing select podcasts like Greatest of All Talk and Asianometry during the break period
- **Communicate clearly** about when services resume to keep subscribers informed and engaged


## Trending on GitHub

**[Krishnagangwal/CS-Fundamentals](https://github.com/Krishnagangwal/CS-Fundamentals)** (⭐ 1,483 · N/A)
Curated CS fundamentals for placement prep: DSA,Computer Networks, DBMS & SQL, OOPs, Operating Systems, System Design & Software Engineering
*Comprehensive CS fundamentals resource signals growing demand for structured technical hiring standards and skill validation frameworks in competitive talent markets.*

**[yynxxxxx/Codex-5.5-codex-instruct-5.5](https://github.com/yynxxxxx/Codex-5.5-codex-instruct-5.5)** (⭐ 1,269 · Python)
No description
*Undescribed Codex model release suggests continued democratization of AI coding capabilities, potentially impacting your engineering velocity and hiring competitive advantage.*

**[mekos2772/ios-location-spoofer](https://github.com/mekos2772/ios-location-spoofer)** (⭐ 1,233 · JavaScript)
Standalone iOS app to spoof GPS location without jailbreak. Includes Shadowrocket/Surge/Loon/QX/Stash module.
*iOS location spoofing tool highlights persistent security gaps in mobile verification—relevant for product teams handling location-based services or compliance requirements.*

**[Kulaxyz/self-learning-skills](https://github.com/Kulaxyz/self-learning-skills)** (⭐ 994 · N/A)
A self-improving skill for AI coding agents (Claude Code, Cursor, AGENTS.md): recognize a hard-won golden path in a session and harvest it into a reusable skill/rule for next time.
*Self-improving AI coding agents reveal emerging workflow patterns where tools autonomously capture and reuse domain knowledge, reshaping how engineering teams operate.*

**[TianhangZhuzth/Fundamental-Ava](https://github.com/TianhangZhuzth/Fundamental-Ava)** (⭐ 761 · Python)
Build digital human beings — autonomous, collaborative, and socially intelligent agents. FNzgGxU31RWiDgLr3GvxxSa42nRntvZNSG6aBMQ1pump
*Digital human agent framework indicates accelerating shift toward autonomous, multi-agent systems—signal to monitor for B2B SaaS opportunities in agent orchestration platforms.*


## Trending on Hacker News

**[Claude Code is steganographically marking requests](https://thereallo.dev/blog/claude-code-prompt-steganography)** (▲ 2,425 · 💬 740) — [discussion](https://news.ycombinator.com/item?id=48734373)
*Claude's steganographic marking raises critical questions about AI tool transparency and trust—essential consideration for teams integrating LLMs into production workflows.*

**[Android Developer Verification: Threat masquerading as protection](https://f-droid.org/2026/07/01/adv-malware.html)** (▲ 1,645 · 💬 711) — [discussion](https://news.ycombinator.com/item?id=48755965)
*Android verification drama exposes how platform gatekeeping can backfire; reminder that developer trust is fragile and directly impacts tool adoption.*

**[Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5)** (▲ 1,256 · 💬 780) — [discussion](https://news.ycombinator.com/item?id=48736605)
*Claude Sonnet 5 release signals rapid model iteration commoditizing capabilities—pressure to differentiate beyond raw LLM performance in your AI-powered features.*

**[Qwen 3.6 27B is the sweet spot for local development](https://quesma.com/blog/qwen-36-is-awesome/)** (▲ 1,184 · 💬 753) — [discussion](https://news.ycombinator.com/item?id=48721903)
*Local 27B models reaching production viability indicates AI infrastructure democratization, reducing vendor lock-in and reshaping competitive dynamics in AI-dependent products.*

**[U.S. government will decide who gets to use GPT-5.6](https://www.washingtonpost.com/technology/2026/06/26/openai-says-us-government-will-vet-users-its-latest-ai-model/)** (▲ 1,183 · 💬 1,241) — [discussion](https://news.ycombinator.com/item?id=48690101)
*Government GPT-5.6 access restrictions preview coming regulatory fragmentation—critical for planning international GTM strategy and compliance posture around AI features.*

