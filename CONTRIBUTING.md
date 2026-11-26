# Contributing

Thanks for helping improve Awesome Coding Agent Sessions. This is a curated list, not an exhaustive directory.

## Inclusion criteria

A project must meet every requirement:

1. Directly read, write, index, transform, render, resume, manage, or analyze coding-agent session, history, or transcript data.
2. Have a public repository, substantive documentation, and a verified open-source license.
3. Provide a distinct, usable session workflow rather than a placeholder, abandoned fork, or promotional landing page.
4. Document the supported coding agents or session formats clearly enough to verify the entry.
5. Fit one primary category in this list. Secondary capabilities belong in the comparison metadata, not duplicate entries.

There is no minimum Stars requirement. Stars are displayed as an adoption signal and do not substitute for scope fit, documentation, maintenance, or licensing.

## Out of scope

Do not submit:

- General-purpose coding agents, agent directories, prompt libraries, or model comparisons.
- Generic orchestration, observability, memory, context-engineering, or MCP tools that do not process coding-agent session data directly.
- Closed-source products or source-available projects with restrictions incompatible with an open-source license.
- Multiple forks with no material session-specific difference.
- Blog posts, tutorials, or repositories that only document a manual workflow.

## Adding a project

1. Add one object to `catalog.json` under the correct category.
2. Keep projects alphabetized by `name` within each category.
3. Use factual, non-promotional English. `summary` and `best_for` must end with a period.
4. Verify supported agents, interfaces, capabilities, and license against the project's current README and repository metadata.
5. Record the current Stars count in `stars_snapshot` and today's date in `verified_at`; the README itself uses a live badge.
6. Update the top-level `metadata_checked` date.
7. Run `make render` and `make check`.

Submit one project per pull request unless a repository rename or category-wide correction requires a grouped change.

## Updating an existing entry

Prefer factual corrections over promotional expansion. When a repository is archived, loses its license, stops processing session data, or becomes a duplicate, propose removal and include evidence in the pull request.

## Local validation

The repository uses only Python's standard library:

```sh
make render  # regenerate README.md from catalog.json
make check   # validate catalog invariants and detect README drift
```

Reviewers still decide whether a project is genuinely useful and accurately described. Automated checks cannot make that curation judgment.
