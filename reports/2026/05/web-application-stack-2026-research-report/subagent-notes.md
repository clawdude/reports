# Subagent notes — consolidated

Five parallel evidence-track subagents were launched for this redo: primary sources, GitHub/activity, practitioner/community, platforms/economics, and adversarial risks. Several child sessions were still running or compacted when parent consolidation began; the parent therefore used their visible trail plus direct source verification rather than relying on unstored prose summaries.

## Platform/economics track
- Official pricing pages verified Cloudflare Workers, Railway, Fly.io, Neon, Vercel, Sentry, PostHog, Resend and related services.
- Strong signal: Cloudflare Workers and Neon have unusually low entry costs for spiky/web workloads, while Railway is simpler for ordinary containers and background workers.
- Risk: Vercel/Railway/Fly all have different cost traps: bandwidth/function add-ons, usage-based compute/egress, or machine/storage cleanup.

## Community/practitioner track
- Visible searches targeted Reddit, HN, migration posts, Vercel pricing complaints, Cloudflare/Fly/Railway latency comparisons, and HTMX/server-rendered alternatives.
- Signal: practitioners value boring Postgres, simple deployment, and fewer moving parts; complaints cluster around framework churn, Vercel cost surprises, and opaque serverless behavior.
- Risk: community posts are noisy and often anecdotal, so they were used mainly as negative-evidence prompts, not final authority.

## Adversarial/risk track
- Looked for reasons not to choose trendy stacks: React Server Component complexity, edge runtime restrictions, serverless cold starts, auth liability, queue/workflow lock-in, and observability cost blowups.
- Result incorporated as guardrails: choose TanStack/SvelteKit only if team accepts ecosystem risk, keep critical state in Postgres, instrument early, set spend caps, and avoid Kubernetes until needed.

## GitHub/activity track
- Parent directly verified examples where GitHub CLI/API was responsive: TanStack Router, SvelteKit, Hono showed same-day activity on 2026-05-03; network timeouts prevented complete repo matrix during this run.
- Recommendation treats high activity as useful but not sufficient: activity can also mean churn.

## Primary-source track
- Parent directly fetched official docs for TanStack Start, SvelteKit, Hono, Drizzle, Better Auth, Inngest, Trigger.dev, OpenTelemetry, platform pricing, UI, email, payments, and search.
