# QueryMind

A natural-language-to-SQL analytics copilot. Connect a database, ask a question in plain English, and get back safe, schema-aware SQL plus an auto-generated chart.

**Status: In Development** 🚧

## Plan

- **Schema-aware RAG** — embed table/column metadata (and sample values) into a vector store so the LLM grounds generated SQL in the real schema instead of hallucinating columns.
- **Read-only guardrails** — every generated query runs through a SQL parser that rejects anything but `SELECT`, plus a sandboxed, rate-limited DB connection.
- **Auto-charting** — infer a sensible chart type (line/bar/table) from the result shape and render it immediately.
- **Eval suite** — a small fixed set of question/answer pairs per connected schema to track SQL accuracy across model/prompt changes.

## Planned stack

- **Backend**: Python, FastAPI
- **LLM / RAG**: OpenAI or Gemini API, pgvector for schema embeddings
- **Database**: PostgreSQL
- **Frontend**: React, TypeScript
- **Infra**: Docker, deployed on Render/Fly.io + Vercel

## Roadmap

- [ ] Schema introspection + embedding pipeline
- [ ] NL → SQL generation with guardrails
- [ ] Auto-chart rendering
- [ ] Eval suite + accuracy tracking
- [ ] Deployed demo with a sample dataset
