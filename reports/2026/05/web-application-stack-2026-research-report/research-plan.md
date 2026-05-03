# Research plan — 2026 web application stack from scratch

## Objective
Recommend a coherent, modern 2026 stack for a serious web application: not just frontend/backend/database, but auth, queues/workflows, cache, search, storage, payments/email, observability, CI/CD, infrastructure as code, and deployment. Optimize for performance, developer experience, documentation quality, simplicity, deployment complexity/price, and how well the pieces fit together — not popularity.

## Inclusion criteria
- Actively maintained in 2025–2026 or backed by a durable company/community.
- Production-suitable for a team that wants to ship quickly without hiding all operational details.
- Strong TypeScript or first-class web-standard ergonomics unless a non-TS option is clearly better.
- Clear docs/pricing/operational model.
- Works as part of a coherent system rather than a bag of trendy tools.

## Exclusion criteria
- Outdated defaults chosen mainly because they are old or popular.
- Tools with unclear maintenance, vague pricing, or no credible production path.
- Heavy microservice/Kubernetes-first designs for a product that has not earned that complexity.
- Frameworks that require platform lock-in without a clear benefit.

## Source categories
- Official docs/pricing for direct capabilities and limits.
- GitHub/activity checks for maturity and churn risk.
- Practitioner/community reports for DX and hidden pain.
- Adversarial search for cost, lock-in, serverless, auth, and observability failure modes.

## Subagent tracks launched
1. Primary/official sources.
2. GitHub/code-hosting activity.
3. Practitioner/community reports.
4. Deployment/platform economics and operations.
5. Adversarial risk/negative evidence.

## Verification strategy
Directly verify pricing, platform limits, official capability claims, and repository activity where practical. Treat vendor performance claims as claims unless independently benchmarked for the target workload.
