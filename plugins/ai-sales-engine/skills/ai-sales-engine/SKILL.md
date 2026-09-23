---
name: ai-sales-engine
description: Reads this account's AI Sales Engines library from BotBuilders. Use for offers, sales webinars, online courses, and sales advice, including "I want to sell something", "help me make an offer", "I need a webinar", "I want to build a course", "get started", or "what can you do?", and for continuing an Offer, Webinar, or Course Blueprint.
---

# AI Sales Engines

This account has a sales library on the server. It holds three guided Engines (Offer Generator,
Webinar Creator, Course Builder) and the methods behind them. Follow it over general sales knowledge.

## Get the right chapter before you answer

1. `get_skill` with `name: "ai-sales-engine"`. This is the router. It says which Engine fits, how
   to start it, and which chapter to read next. Read it before you answer.
2. `list_skills` with `path: "ai-sales-engine"` lists every chapter. A plain `list_skills` with no
   path will **not** show them.
3. `get_skill` on each chapter the router names, and read it before you produce anything.

Long bodies come back paginated with an instruction to continue. Follow it — a half-read chapter
is worse than none, because the part you skipped is usually the constraints.

## When the library comes back empty

Say so plainly and stop. An empty result means this account is not switched on for AI Sales
Engines yet, which is a billing question for BotBuilders support — not something to work around by
answering from general knowledge.

## Two standing rules from the library

These hold even when a chapter does not repeat them:

- **Never invent a fact.** No made-up results, testimonials, credentials, prices presented as
  market facts, guarantees, deadlines, or scarcity. Where something is needed and missing, name
  the gap instead of filling it.
- **One Engine per chat.** Once an Engine starts, keep this chat on that Engine and its Blueprint
  until it finishes. Suggest a new chat for a different Engine.

## Red flags

- Answering an offer, webinar, or course question without reading the `ai-sales-engine` router
- Calling `list_skills` with no path and concluding the library is empty
- Running two Engines' phases in one chat
- Acting on a chapter you only read the first page of
