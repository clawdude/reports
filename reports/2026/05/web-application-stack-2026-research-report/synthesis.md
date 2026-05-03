# Synthesis

## Bottom line
The best default 2026 stack is a lean TypeScript product stack, not a microservice zoo: SvelteKit or TanStack Start; Hono for APIs; Postgres with Drizzle; Neon/Supabase for managed Postgres; Better Auth for owned auth or Clerk/Zitadel when auth risk outweighs control; Trigger.dev/Inngest for durable work; Cloudflare Workers for edge/web workloads; Railway/Render/Fly for containers and stateful workers; OpenTelemetry plus Sentry/PostHog for observability.

## What changed versus a generic answer
A generic answer would over-rank popularity and produce Next.js + Prisma + Vercel + Redis + Kubernetes. The evidence shifted the recommendation toward simpler boundaries: keep Postgres central, use edge only where it fits, avoid Kubernetes early, prefer durable workflow tools over raw queues, and split frontend/API/workers only when operationally useful.

## High-confidence findings
- Postgres remains the coordination point. Newer serverless Postgres providers add branching/scale-to-zero, but the data model should not be scattered across platform-specific stores.
- Hono is the best default API layer when edge portability and simplicity matter; Fastify is still better for conventional Node services with plugins and long-running process assumptions.
- SvelteKit is the simplest coherent full-stack choice if React is not mandatory. TanStack Start is the highest-upside React choice, but its newer/RC status raises maturity risk. Next.js remains strongest when Vercel/RSC ecosystem fit matters, but DX complexity is a real cost.
- Durable workflow platforms are better than assembling queues, cron, retry state, idempotency, and dashboards manually for most product teams.
- Observability should start with Sentry + PostHog and an OpenTelemetry shape, not a bespoke ELK/Grafana stack.

## Contradictions and negative evidence
- Newer tools have better DX but higher churn. Old tools have maturity but often drag hidden complexity. The practical answer is not “new” or “old”; it is reversible choices at the edges and boring choices at the core.
- Serverless/edge is cheap and fast for request/response, but weak for long CPU, large dependencies, raw sockets, and some database patterns.
- Hosted auth saves time but creates pricing and lock-in risk. Self-hosted/owned auth saves money but creates security liability.
- “Microservices” are requested, but premature microservices would damage simplicity. Use modular services/deployables; split only around scaling, isolation, team ownership, or compliance.

## Recommendation
Default to the Lean TypeScript Product Stack. Use SvelteKit when React is optional; TanStack Start when React and type-safe routing/client-first DX matter; Next.js only for teams that explicitly want the Vercel/RSC ecosystem. Keep the first production architecture to 4 deployables: web app, API/BFF, worker/workflow service, and observability/release pipeline.
