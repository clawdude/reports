---
name: research
description: Conduct deep, source-backed research reports that go beyond generic ChatGPT answers by using explicit scoping, targeted source discovery, parallel adversarial subagents, evidence extraction, verification, synthesis, and an HTML report saved to ~/reports or the existing reports server. Use when the user asks for research, a research report, source comparison, landscape scan, forum/GitHub/message-board investigation, due diligence, or says "research <topic>" with an objective.
---

# Research

Turn a topic + objective into a decision-useful, source-backed report. The point of this skill is **not** to answer from general model knowledge. The point is to discover, verify, compare, and synthesize evidence that the chat interface would usually miss.

## Inputs

Require:
- **Topic**: what to investigate.
- **Objective**: what decision/question the research should answer.

If either is missing, ask one concise clarifying question. If the objective is vague, convert it into a decision frame: “choose X”, “understand risks”, “find best options”, “validate claim”, or “map landscape”.

## Non-negotiable quality bar

A research run is incomplete unless it has:
- A source-discovery pass before planning.
- Explicit inclusion/exclusion criteria.
- Multiple independent source categories attempted or marked blocked.
- A source ledger with URLs, dates, source type, credibility, and relevance.
- Evidence-backed claims; uncited claims must be labeled as inference.
- At least one contradiction/risk/negative-evidence pass.
- Verification of important metadata with direct source checks where practical.
- A synthesized conclusion that explains what changed because of the research.

Avoid generic “overview” reports. Prefer decision-useful findings, tradeoffs, caveats, and next actions.

## Workflow

### 1. Orient and discover sources before planning

Do a light discovery pass first. Use web search, direct URLs, GitHub/API/CLI, package registries, docs, forums, papers, or targeted site searches as appropriate.

Produce enough orientation to know:
- The topic vocabulary and likely primary sources.
- Where real practitioner discussion happens.
- Which source categories are likely high-signal vs noisy.
- Whether the topic is fast-moving and needs recency constraints.

Do not start full research yet.

### 2. Plan first, then wait for confirmation

Present a concise plan and wait for explicit confirmation.

The plan must include:
- Decision/objective restatement.
- Key questions to answer.
- Inclusion/exclusion criteria.
- Source categories and why each matters.
- Proposed subagent tracks and expected outputs.
- Verification strategy for important claims.
- Deliverable: HTML report saved under the reports location.

If time/depth is unclear, offer 2–3 modes:
- **Fast scan**: fewer sources, directional answer.
- **Normal**: several source categories, evidence matrix.
- **Deep**: broader search, adversarial pass, stronger verification.

Recommend one mode instead of dumping choices.

### 3. Search like an investigator, not a chatbot

Use targeted queries and source-specific searches. Vary query shape:
- Official terms + synonyms.
- “problems”, “limitations”, “migration”, “postmortem”, “benchmark”, “comparison”, “pricing”, “security”, “production”, “alternatives”.
- Site-specific searches: `site:github.com`, `site:news.ycombinator.com`, `site:reddit.com`, docs domains, package registries, issue trackers.
- Time-bounded searches for fast-moving topics.

Prefer primary/near-primary sources:
1. Official docs/specs/releases/pricing/security pages.
2. Maintainer posts, GitHub issues/discussions/PRs.
3. User reports from forums/message boards with dates and context.
4. Independent benchmarks/reviews with methodology.
5. Blogs/tutorials only when they add concrete evidence.

Actively look for negative evidence and disconfirming sources. Do not just collect sources that agree with the emerging answer.

### 4. Deploy parallel subagents after confirmation

Spawn isolated subagents with `sessions_spawn` for independent tracks. Use narrow prompts so each subagent returns evidence, not prose filler.

Recommended tracks:
- **Primary sources**: official docs, specs, announcements, changelogs, pricing, security pages.
- **GitHub/code-hosting**: repos, README, stars/activity, releases, issues, discussions, PRs. Avoid deep code reading unless needed.
- **Community/practitioner reports**: Reddit, HN, StackOverflow, forums, Discord mirrors, blogs with concrete implementation experience.
- **Ecosystem/alternatives**: package registries, starter templates, awesome lists, competing tools, commercial alternatives.
- **Adversarial/risks**: failure cases, complaints, lock-in, hidden costs, abandoned projects, security/privacy/licensing concerns.

Each subagent must return structured notes:
- URLs with title/source/date/access date.
- Key findings in bullets.
- Evidence snippets or precise paraphrases.
- Credibility/relevance rating: high/medium/low.
- Recency/activity signals.
- Contradictions, caveats, and unanswered questions.
- What this track suggests for the final decision.

If web search is unavailable or rate-limited, switch methods: direct URLs, GitHub CLI/API, `web_fetch`, package registry pages, local docs, or targeted source searches. State hard blockers clearly.

### 5. Consolidate into an evidence ledger

Before writing, consolidate all findings into a working source ledger. Include:
- Source URL/title.
- Source category.
- Date published/updated when available.
- Access date.
- Main claim(s) supported.
- Credibility/relevance notes.
- Whether it is primary, practitioner, benchmark, opinion, or weak/noisy.

Then:
- Deduplicate sources and claims.
- Resolve contradictions by comparing source quality, dates, methods, and incentives.
- Separate high-confidence findings from weak/noisy ones.
- Track rejected/low-confidence items when useful.
- Identify “unknowns that matter” instead of pretending certainty.

### 6. Verify important claims

Directly verify claims that materially affect the conclusion, such as:
- Current pricing, version support, license, availability, or API limits.
- Repo activity/release freshness.
- Benchmarks or performance claims.
- Security/privacy/compliance claims.
- “Best”, “most popular”, “dead”, “production-ready”, or “recommended” claims.

Use direct source checks where practical. Label anything not verified.

### 7. Build the HTML report

Create a polished standalone HTML file in the reports location.

Default location:
- Use `/Users/macmini/reports/`. This is the GitHub Pages repo.
- Only fall back to `~/reports/` if `/Users/macmini/reports/` is unavailable.

Static-site saving convention:
- Save new reports as `/Users/macmini/reports/reports/YYYY/MM/<slug>/index.html`.
- Use a lowercase slug of the topic/objective.
- Example: `/Users/macmini/reports/reports/2026/05/sveltekit-remote-functions/index.html`.
- Keep report-local assets, evidence JSON, screenshots, or downloads inside the same report folder if needed.
- Do not add every new report directly to the site root.
- After saving under `/Users/macmini/reports/`, run `python3 /Users/macmini/reports/reports/build_index.py` to regenerate the static GitHub Pages index.

The report must include:
- Title, date, topic, objective.
- Executive summary with bottom-line answer.
- “What changed after research” / why this is better than a generic answer.
- Methodology and source scope.
- Inclusion/exclusion criteria.
- Evidence ledger/source table.
- Main findings, ranked or grouped by decision relevance.
- Contradictions, caveats, and negative evidence.
- Recommended next steps.
- Appendix of rejected/low-confidence sources if useful.

Style requirements:
- Self-contained CSS.
- Readable on mobile and desktop.
- Clickable links.
- Use real HTML tables/cards, not markdown tables inside HTML.

### 8. Build the static index and report completion

GitHub Pages is static: Python server code will not run there. Treat `server.py` only as an optional local preview helper.

After saving in `/Users/macmini/reports/`:
- Run `python3 /Users/macmini/reports/reports/build_index.py`.
- Confirm `index.html` includes the new report path.
- If a Git repository is present, check `git status` and commit/push when the user asked to publish.
- For local preview, use the existing server on port `8765` if already running, or `python3 -m http.server` for a temporary static preview. Do not start long-lived new servers unless explicitly needed.
- Verify any local URL with `curl -I` before reporting it works.

In webchat, reply with the report path and static index/link. Do not send Discord messages unless explicitly requested or the current conversation is Discord and a response is needed.

## Report writing rules

- Lead with the answer, not background.
- Make tradeoffs explicit.
- Prefer fewer, stronger claims over broad shallow coverage.
- Say “I could not verify X” instead of implying certainty.
- Distinguish facts, source claims, and synthesis.
- Include dates for fast-moving topics.
- Avoid SEO-blog filler and generic LLM prose.
- If the final report feels like something ChatGPT could have produced without browsing, the research failed.
