# PM Pulse: Weekly Digest — Jul 31, 2026

15 articles from 7 feeds | Jul 24 – Jul 31, 2026

---

## This Week

**The infrastructure layer—not the model—is becoming the competitive moat in AI; PMs must shift from chasing model capabilities to engineering harnesses and evals.**

This week reveals a fundamental inversion in AI product strategy: raw model capability is commoditizing fast, but the orchestration layer—evals, caching, context management, and agentic access control—is where differentiation lives. Three distinct threads emerge: (1) hyperscalers are pivoting spending from models to infrastructure (AWS acceleration, Microsoft's reseller model), (2) frontier labs are shipping eval-driven development as core methodology, and (3) third-party harnesses like Cursor are outperforming first-party solutions through superior engineering. For VPs at Series C companies, the implication is stark: your moat isn't the AI model you're wrapping; it's how well you've instrumented the layer around it. Spending on evals and harness architecture now matters more than choosing between Claude and GPT.

- Evals are becoming the product development primitive—cold-start eval construction without production data is now table stakes for AI shipping
- Harnesses, not models, are the real value driver—cache discipline, context management, and third-party wrapper engineering outweigh underlying model choice
- Enterprise AI security is consolidating—data security + agentic access control is merging into a single category, suggesting ecosystem winners are platform-shaped, not point-solution shaped
- Hyperscaler strategies are diverging by architectural choice—AWS and Microsoft's opposing bets on owned vs. merchant silicon will reshape cloud vendor margins and customer lock-in

---

## Must-Read

### 1. [Anthropic’s first technical PM on token maxing, the jagged edge, and living in the future | Dianne Penn](https://www.lennysnewsletter.com/p/anthropics-first-technical-pm-on)
*Lenny's Newsletter* — Lenny Rachitsky (featuring Dianne Penn) — Jul 26, 2026  `#AI Strategy`  `#Discovery`

Anthropic's first technical PM reveals that Claude's rapid iteration and market leadership stem from an eval-driven feedback loop—not larger models. Penn articulates how human judgment (not pure data-driven optimization) remains critical in deciding which evals to optimize for, emphasizing that the fastest path to production-grade AI is structured evaluation before user data exists. This directly counters the narrative that bigger models solve everything and provides a repeatable methodology for startups to ship competitive AI features without waiting for massive training runs.

**Why it matters**: Dianne Penn's framework on eval-driven development and the irreplaceable role of human judgment in AI product scaling is the primary playbook for Series C companies building frontier-grade evals at speed.

- **Embrace eval-driven development**: Build systematic evaluation frameworks that allow your team to measure incremental improvements and validate product decisions at scale, rather than relying solely on intuition.
- **Hire for technical depth in product**: Recruit PMs with engineering backgrounds or deep technical understanding early—they can communicate better with researchers and help translate complex AI capabilities into user-facing features.
- **Maintain human judgment as a moat**: Don't automate away decision-making; recognize that human judgment about which problems matter and how to prioritize remains irreplaceable even as AI capabilities accelerate.
- **Build feedback loops into your culture**: Create systems where teams can rapidly iterate and learn from real-world usage patterns, turning each release into a learning opportunity rather than a final endpoint.
- **Stay grounded during hypergrowth**: Find ways to maintain perspective and joy when operating at extreme velocity; establish practices that help teams reflect and celebrate progress rather than only chasing the next milestone.

[Read article →](https://www.lennysnewsletter.com/p/anthropics-first-technical-pm-on)

---

### 2. [Aftermarket Harnesses](https://www.tomtunguz.com/aftermarket-harnesses/)
*Tomasz Tunguz* — Tomasz Tunguz — Jul 28, 2026  `#AI Strategy`  `#Platform Strategy`

Tomasz Tunguz argues that the orchestration layer (caching, context management, prompt engineering) now has greater impact on user-facing performance than the underlying model itself. Third-party harnesses like Cursor demonstrate that superior engineering can match or exceed first-party solutions, meaning vendor lock-in is weaker than assumed. For Series C companies, this means engineering discipline on latency and cost efficiency in the harness layer is now a primary competitive lever—arguably more important than which foundation model you license.

**Why it matters**: Harnesses—not models—determine product performance and cost efficiency; this insight should reshape infrastructure and R&D investment decisions for any VP scaling an AI product suite.

- **Prioritize harness architecture over model selection**: Endor Labs found GPT-5.5 scored 25.7 points higher in Cursor's harness (87.2%) than its native Codex harness (61.5%), proving the runtime environment matters more than the model for functional correctness.
- **Implement aggressive prompt caching strategies**: Since input tokens represent 86-98% of LLM costs, deploy cache-first design patterns with stable prefixes before dynamic content to achieve 40-80% cost savings and 13-31% faster time-to-first-token.
- **Engineer precise information retrieval pipelines**: Design harnesses to fetch only concise, relevant context (code snippets, style guides, document sections) rather than broad context, directly reducing token costs without sacrificing quality.
- **Adopt dynamic tool-fetching and prefix assembly**: Third-party harnesses match first-party performance by implementing multi-tier caching, dynamic tool selection, and priority-based prompt construction—techniques that are harness-level, not model-level capabilities.
- **Treat harness co-design as a competitive advantage**: While bundled solutions like Claude Code achieve 96% cache hit rates through system integration, the discipline itself is portable—invest in harness engineering to match first-party advantages independently.

[Read article →](https://www.tomtunguz.com/aftermarket-harnesses/)

---

### 3. [How to Build Frontier-Lab Quality Evals with Daniel McKinnon, ex-PM at Meta, Google](https://www.news.aakashg.com/p/how-to-build-your-first-eval)
*Product Growth* — Aakash Gupta (featuring Daniel McKinnon) — Jul 28, 2026  `#AI Strategy`  `#Discovery`

McKinnon, an ex-PM at Meta and Google, describes a structured approach to building evals for AI features when you have no user data yet: combine domain expertise with systematic testing of edge cases rather than waiting for production errors. This bridges the gap between raw capability (what a model can do) and product-grade reliability (what it should do). For a Series C VP launching new AI features, this methodology collapses time-to-launch and reduces the risk of shipping half-baked AI experiences.

**Why it matters**: Daniel McKinnon's cold-start eval methodology provides a concrete, repeatable framework for building frontier-lab-quality AI feature validation without production data—critical for shipping differentiated AI features before competitors.

- **Build evals before launch** by using domain expertise to create test cases through a systematic floor-to-ceiling approach, rather than waiting for production data to analyze failures.
- **Structure your eval workspace** by uploading relevant context into Claude or ChatGPT projects with clear instructions about what correct and incorrect answers look like, enabling the model to generate realistic test cases at scale.
- **Use binary pass/fail scoring** with specific criteria (substantive correctness, format usability, and scope alignment) rather than subjective grading, making evals reliable handoff documents for other teams.
- **Invest 90% of your development time in eval quality** because well-designed evals become your specification, reducing ambiguity and enabling faster iteration than traditional PRDs.
- **Share evals directly instead of specs** when requesting features from partner teams—send the eval artifact itself rather than descriptions, cutting middleman work and improving clarity across teams.

[Read article →](https://www.news.aakashg.com/p/how-to-build-your-first-eval)

---

## All Articles

**4.** [AWS's Road to a Trillion](https://www.tomtunguz.com/aws-answers-the-cloud-race/) — *Tomasz Tunguz* · Jul 30, 2026  `#Competitive Strategy`  `#Market Trends`

AWS accelerated to 36.7% growth in Q2 2026, narrowing Azure's lead and positioning itself toward a potential $1 trillion revenue business, though the company's aggressive capital spending has pushed free cash flow negative while betting on enterprise AI adoption to materialize.

- **AWS is closing the gap**: AWS grew 36.7% YoY and narrowed Azure's lead from 16 points to 6 points, signaling a major competitive shift in cloud infrastructure as frontier AI labs drive demand for compute capacity.
- **Capital spending is unsustainable without enterprise adoption**: Amazon raised 2026 capex to $220B and turned free cash flow negative (-$7.6B) — the company must achieve rapid enterprise AI workload adoption in the 'middle of the barbell' to justify this spending.
- **Backlog growth masks competitive disadvantage**: AWS's $496B backlog trails Microsoft's $678B partly because Microsoft locked in OpenAI capacity early; Amazon's deals with Anthropic and OpenAI came later, requiring it to overbuild infrastructure ahead of confirmed demand.
- **The trillion-dollar thesis depends on timing**: Jassy explicitly conceded uncertainty about whether enterprise production workload adoption will accelerate at the same pace as frontier lab demand—this timing risk is the core variable determining AWS's trillion-dollar potential.
- **Microsoft's hedging strategy outperforms Amazon's all-in bet**: Microsoft kept free cash flow positive at $19.6B by spending more cautiously on capex ($41B including leases), while Amazon borrowed heavily to fund its $220B spending plan, creating divergent risk profiles.

**5.** [Microsoft Resells the Frontier](https://www.tomtunguz.com/microsoft-resells-the-frontier/) — *Tomasz Tunguz* · Jul 29, 2026  `#Competitive Strategy`  `#Platform Strategy`

Microsoft's cloud strategy differs fundamentally from Google's because it resells AI models and relies on merchant silicon rather than owning its stack, forcing it to adopt a more cautious spending approach despite massive contracted backlog concentrated heavily in OpenAI.

- **Understand the economics gap**: Google's ownership of models and custom chips (TPUs) allows 35.6% cloud operating margins while Microsoft's reliance on Nvidia silicon and resold models creates thinner margins that limit capacity spending per revenue dollar.
- **Monitor concentration risk**: Nearly half of Microsoft's $678B contracted backlog ($220B of $310B growth) comes from a single customer (OpenAI) that funds commitments through capital markets rather than profits—a structural vulnerability absent in Google's diversified base.
- **Track financing circularity**: The same borrowed capital appears on multiple balance sheets (Nvidia guaranteeing OpenAI leases, OpenAI's commitments to Microsoft), creating systemic risk reflected in rising credit default swaps and S&P downgrades of dependent vendors like Oracle.
- **Evaluate capex flexibility as risk management**: Microsoft's focus on short-lived assets (GPUs/CPUs) over infrastructure enables demand-responsive spending that can be reduced if the capital-market-dependent customer base falters, whereas Google's aggressive spending reflects confidence in owned-stack ROI.
- **Watch growth rate divergence**: Google Cloud grew 82% YoY while Azure grew 43%, with Google spending $44.9B capex against $24.8B revenue—the margin economics and ownership model are now driving nearly 2x growth acceleration for the smaller competitor.

**6.** [Cyera and Oasis: Stronger Together](https://sequoiacap.com/article/cyera-and-oasis-stronger-together/) — *Sequoia Capital* · Jul 28, 2026  `#Enterprise`  `#Agentic`

Cyera and Oasis Security are merging to create a comprehensive AI security platform that combines data security with agentic access management, positioning themselves as the default security layer for enterprises deploying AI agents.

- **Combine complementary capabilities**: Data security (Cyera) and identity/access management (Oasis) work together to secure the entire path an AI agent takes through an enterprise—from data access to credential verification.
- **Leverage GTM scale for rapid expansion**: Oasis gains access to Cyera's established enterprise sales engine, potentially compressing years of go-to-market development into months and accelerating time-to-market.
- **Define the security category before competitors**: The window to establish the first complete AI security standard is narrow—speed and product completeness are both critical to becoming the default platform enterprises adopt.
- **Watch for founder pattern matching**: Technical founders from elite programs (Talpiot, Unit 8200) are disproportionately successful in cybersecurity—this signals strong founding team quality and market insight.

**7.** [11 products I love, free for a year—the biggest Product Pass expansion in 2 years](https://www.lennysnewsletter.com/p/productpass-summer2026launch) — *Lenny's Newsletter* · Jul 28, 2026  `#Product Growth`  `#Market Trends`

Lenny announces a major expansion of Lenny's Product Pass, adding 11 new products (bringing the total to 34) including Runway, Brain.fm, Waking Up, and others, offering over $40,000 in value for annual subscribers to help close the access gap for AI tools and personal productivity software.

- **Curate ruthlessly**: Only include tools you genuinely love and use personally—Lenny's Product Pass succeeds because every product is hand-selected and battle-tested, not just trending.
- **Extend trial periods strategically**: A full year of free access (vs. typical 2-week trials) allows users to build real workflows, form habits, and make informed decisions about tool adoption.
- **Bundle complementary categories**: Mix work tools (Cursor, Linear, Resend) with wellness products (Waking Up, Brain.fm, Readwise) to address the full spectrum of what creators need to thrive.
- **Focus on accessibility barriers**: The Product Pass exists because expensive tools create a success gap—solve this by partnering with companies to offer unprecedented discounts and free years.
- **Leverage community feedback**: Use your audience to validate product quality (e.g., asking readers which tools they use most), then double down on partnerships with the winners.

**8.** [🎙️ How I AI: Claude Opus 5 Review + Browser use in Codex + How Cursor and a Raspberry Pi makes AI fun](https://www.lennysnewsletter.com/p/how-i-ai-claude-opus-5-review-browser) — *Lenny's Newsletter* · Jul 27, 2026  `#AI Tools`  `#Agentic`

This episode covers three major AI developments: Claude Opus 5's capabilities and limitations compared to other models, practical browser automation workflows with Codex, and how non-technical builders can create hardware projects using AI coding tools.

- **Match compute levels to task complexity** — Use frontier models for reasoning-heavy work like code review, but drop to medium-effort models for simpler tasks like LinkedIn triage to reduce costs while maintaining quality.
- **Let frontier models think freely** — Give AI room to approach problems without prescriptive lists; saying 'QA the onboarding flow' yields better coverage than listing 25 specific tests because the model avoids human blind spots.
- **Build physical projects without deep coding knowledge** — You only need enough literacy to spot wire mistakes and verify direction; AI handles implementation, so complex hardware becomes accessible through plain-language descriptions.
- **Use persona-based testing to expose real friction** — Have AI interact with products as specific users (PM in a meeting, engineer reading PRD) to uncover UX problems that abstract evaluation misses.
- **Prototype with intention, not perfection** — Building 'fun' projects that route tweets through multiple services is valid because AI removes implementation burden; focus on finishing ideas rather than elegant architecture.

**9.** [🧠 Community Wisdom: Staying on a client’s radar during pilot purgatory, pairing Linear with a discovery tool, the limits of what AI can automate, whether Techstars is worth it, and more](https://www.lennysnewsletter.com/p/community-wisdom-staying-on-a-clients) — *Lenny's Newsletter* · Jul 25, 2026  `#Enterprise`  `#Metrics`

This Community Wisdom column aggregates practical advice from Lenny's subscriber Slack community on topics including maintaining client relationships during pilot phases, integrating Linear with discovery tools, AI automation limitations, and evaluating accelerator programs like Techstars.

- **Stay visible during pilots** by establishing regular check-in cadences and demonstrating incremental value to clients in extended evaluation periods to prevent deals from stalling.
- **Combine Linear with dedicated discovery tools** rather than relying solely on Linear for product discovery, as project management and discovery require different workflows and capabilities.
- **Recognize AI automation boundaries** by identifying which processes benefit from automation versus those requiring human judgment, context, and decision-making that AI cannot fully replace.
- **Evaluate accelerator ROI carefully** by considering whether Techstars' network, mentorship, and resources align with your specific stage and needs rather than pursuing the brand name alone.

**10.** [From zero coding background to hardware hacker: How Cursor + a Raspberry Pi makes AI fun](https://www.lennysnewsletter.com/p/from-zero-coding-background-to-hardware) — *Lenny's Newsletter* · Jul 27, 2026  `#AI Tools`  `#Creator Economy`

Maddie Reese demonstrates how non-coders can build creative hardware projects by leveraging AI tools like Cursor and Lovable, using a vibe-coding approach to rapidly prototype physical products from thermal receipt printers to Raspberry Pi-based Twitter pagers.

- **Use Cursor's agent view** to brainstorm hardware projects by dumping your idea and letting the AI interview you to generate shopping lists and implementation plans before buying any parts.
- **Build for fun first** rather than practicality—this motivation unlocks faster shipping of physical projects and removes the pressure that blocks hardware beginners from starting.
- **Create personal APIs** that expose your preferences (coffee order, pets, favorite snacks) so both humans and AI agents can integrate with your data without repeated requests.
- **Read just enough code** to understand your project without needing deep technical knowledge—focus on the concepts and functionality rather than mastering every line.
- **Combine AI tools with hardware platforms** like Raspberry Pi, Bluetooth, and cloud services (Resend, Cloudflare Workers, Supabase) to build end-to-end systems without traditional coding experience.

**11.** [Vibe Coding Interviews for PMs: Complete Guide](https://www.news.aakashg.com/p/vibe-coding-interviews-for-pms-complete) — *Product Growth* · Jul 29, 2026  `#Hiring`  `#Org Design`

This guide provides PMs with strategies to excel at vibe coding interviews, a rapidly expanding assessment format at AI-native companies that combines product design with live AI coding demonstrations.

- **Identify target companies**: Vibe coding rounds are concentrated at AI-native/AI-pivoted companies (Figma, Meta, Microsoft, Adobe, Google) and are more common in US and India markets for AI PM roles.
- **Balance ideation with execution**: Avoid jumping immediately into coding—hiring managers prioritize thoughtful product thinking and strategic decision-making before execution, not just rushing to build with AI tools.
- **Demonstrate AI coaching skills**: Show that you can guide and critique AI outputs rather than passively accepting the first suggestion, proving you think critically about edge cases and alternatives during the live coding portion.
- **Prepare a reusable framework**: Develop a systematic approach to handle both product sense and vibe coding components simultaneously, including a PM harness toolkit that covers ideation, evaluation, and implementation steps.

**12.** [Ultimate Guide: ChatGPT Work For PMs](https://www.news.aakashg.com/p/chatgpt-work-pm) — *Product Growth* · Jul 27, 2026  `#AI Tools`

This guide explores how ChatGPT Work can be leveraged by product managers to streamline workflows, automate tasks, and enhance decision-making in their day-to-day operations.

- **Integrate ChatGPT Work into your PM toolkit** to automate routine tasks like stakeholder communication, meeting notes analysis, and roadmap documentation
- **Use ChatGPT Work for rapid prototyping and user research** by generating interview guides, analyzing feedback patterns, and identifying user pain points at scale
- **Set up ChatGPT Work workflows for decision-making** to synthesize complex data, compare strategic options, and pressure-test assumptions before leadership reviews
- **Build team muscle around prompt engineering** to maximize ChatGPT Work's effectiveness—treat it as a collaborative tool that amplifies rather than replaces PM judgment

**13.** [So, you want to be a content creator?](https://www.elenaverna.com/p/so-you-want-to-be-a-content-creator) — *Elena's Growth Scoop* · Jul 28, 2026  `#Leadership`  `#Creator Economy`

Elena Verna shares her personal journey into content creation, revealing how she built an audience by sharing authentic product and career insights rather than chasing viral metrics, and explains the often-hidden realities of being a creator.

- **Start with a clear purpose, not clout**: Share knowledge because you've solved real problems others face repeatedly, not because you want to become an influencer—your authentic motivation will show and resonate with audiences.
- **Apply simple content rules consistently**: Post about patterns and contrarian takes that you've already explained 3+ times in conversations; this ensures you're sharing tested ideas rather than untested theories.
- **Build on your 'superpower' niche**: Identify what comes naturally to you (e.g., product-led growth) and deepen your expertise there rather than trying to cover everything—audiences will engage more with specialized, authentic knowledge.
- **Own your distribution channel**: Create long-form content on your own platform (newsletter, blog) rather than relying only on social media algorithms, so you maintain control when platforms change their rules.
- **Monetize thoughtfully and selectively**: Only sponsor products you genuinely use, gate career content for free access, and use tiered monetization (free + paid archive) to align revenue with audience value rather than maximizing impressions.

**14.** [Startup Kool-Aid; Why You’re Making Enough Money but Still Anxious; $100 Million in Odyssey Popcorn Buckets; the World’s Best Fake $50 Bill, +++ [link post]](https://hunterwalk.com/2026/07/25/startup-kool-aid-why-youre-making-enough-money-but-still-anxious-100-million-in-odyssey-popcorn-buckets-the-worlds-best-fake-50-bill-link-post/) — *Hunter Walk* · Jul 25, 2026  `#Startups`

A curated collection of interesting links covering topics ranging from popcorn bucket economics to startup culture and financial anxiety, reflecting on contemporary consumer trends and workplace dynamics.

- **Explore niche markets**: The $100M popcorn bucket market demonstrates how seemingly trivial consumer products can generate massive revenue when they tap into collectibility and nostalgia.
- **Examine financial anxiety patterns**: Understanding why people with sufficient income still experience anxiety reveals psychological and cultural factors beyond pure economics.
- **Question startup narratives**: Be skeptical of romanticized startup culture and its underlying assumptions about success, risk, and fulfillment.

**15.** [Vacation: Week of July 27](https://stratechery.com/2026/vacation-week-of-july-27/) — *Stratechery* · Jul 27, 2026  `#Meta`

Stratechery is taking a vacation week beginning July 27, 2026, with no new weekly articles or updates scheduled until August 3.

- **Plan subscriber communications** around vacation schedules to set expectations for content pause periods
- **Maintain auxiliary content streams** like Sharp China and Asianometry during main publication breaks to keep audience engaged
- **Publish a clear posting schedule** so subscribers know exactly when content will resume and what remains active


## Trending on GitHub

**[MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3)** (⭐ 7,673 · N/A)
Open Frontier Intelligence
*Open-source frontier AI model gaining traction; signals market demand for accessible alternatives to closed proprietary LLMs.*

**[mshumer/Claude-of-Duty](https://github.com/mshumer/Claude-of-Duty)** (⭐ 2,478 · JavaScript)
A Call of Duty-quality FPS in Three.js, built from a single prompt.
*Single-prompt game generation demonstrates AI's creative capability; indicates feasibility of AI-driven content creation as product feature.*

**[bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer)** (⭐ 1,208 · TypeScript)
No description
*Optical transfer optimization tool suggests emerging infrastructure layer for AI applications; worth monitoring for performance gains.*

**[VictorTaelin/OptMem](https://github.com/VictorTaelin/OptMem)** (⭐ 997 · Python)
Permanent memory for AI agents. A 426-token prompt, a script, plug and play.
*Persistent AI agent memory solves critical limitation in agent reliability; enables stateful interactions essential for enterprise use cases.*

**[xikhar/persona](https://github.com/xikhar/persona)** (⭐ 705 · JavaScript)
Bringing real-time voice to life.
*Real-time voice synthesis reaching production quality; signals convergence of conversational AI features becoming table-stakes for SaaS platforms.*


## Trending on Hacker News

**[Claude Opus 5](https://www.anthropic.com/news/claude-opus-5)** (▲ 1,778 · 💬 1,331) — [discussion](https://news.ycombinator.com/item?id=49038433)
*Claude Opus 5 release indicates continued LLM capability improvements; evaluate implications for your AI feature roadmap and competitive positioning.*

**[Kimi-K3 on HuggingFace](https://huggingface.co/moonshotai/Kimi-K3)** (▲ 1,376 · 💬 544) — [discussion](https://news.ycombinator.com/item?id=49065752)
*Open-source model momentum growing; assess whether proprietary or open-weight models better align with your platform strategy and cost structure.*

**[US citizen charged after GrapheneOS phone wipes during airport search](https://www.techspot.com/news/113236-us-prosecutors-charge-atlanta-man-after-grapheneos-phone.html)** (▲ 1,334 · 💬 1,112) — [discussion](https://news.ycombinator.com/item?id=49063022)
*Security/privacy incident highlights device-level AI risks; consider implications if your product processes sensitive data on user hardware.*

**[Our position on open-weights models](https://www.anthropic.com/news/position-open-weights-models)** (▲ 1,175 · 💬 1,743) — [discussion](https://news.ycombinator.com/item?id=49076057)
*Industry stance on open-weights models reflects shifting market philosophy; monitor for competitive advantages through different AI accessibility strategies.*

**[UEFA and its national associations will not participate in FIFA competitions](https://www.uefa.com/news-media/news/02a7-213a92896eb0-54dfbf454e3b-1000--statement-on-behalf-of-uefa-and-its-55-national-associations/)** (▲ 1,171 · 💬 627) — [discussion](https://news.ycombinator.com/item?id=49113929)

