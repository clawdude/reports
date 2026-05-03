# Reports

Public research reports served with GitHub Pages:

https://clawdude.github.io/reports/

## Structure

- `index.html` is generated. Do not edit it by hand.
- `OPENCLAW_RESEARCH_SKILL.md` is the repo-local instruction file used by the hourly report automation.
- New reports live at `reports/YYYY/MM/<slug>/index.html`.
- Report-local assets/evidence can live beside that report's `index.html`.
- Regenerate the static index after adding or moving reports:

```sh
python3 reports/build_index.py
```

## Request a new report

Open a GitHub issue in this repo with:

- The topic to research
- The question or decision the report should help answer
- Any constraints, preferred sources, or output notes

An hourly automation checks open issues. If the request is clear and allowed, it generates an HTML report, commits it to this repo, updates `index.html`, and comments on the issue with the public link.

## Request changes

Reply on the same issue with the changes you want. The automation will update the report, commit/push the changes, and comment back with what changed.

## Review/close

Issues are left open after a report is ready. Close the issue yourself when the report looks good.
