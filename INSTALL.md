# Installing AI Sales Engines

About two minutes, most of it waiting.

## Before you start

You need Claude Code on your computer. If you don't have it yet, get it at
[claude.com/code](https://claude.com/code) and sign in. If you already have it, make sure it's
up to date — run `claude update`.

## Step 1 — Run two commands

Open your terminal and paste these one at a time:

```
claude plugin marketplace add BotBuilders/ai-sales-engine
```

```
claude plugin install ai-sales-engine@ai-sales-engine
```

The first tells Claude where to find AI Sales Engines. The second installs it.

You should see a line ending in **`(+ 1 dependency: ai-skills)`**. That second piece is the
connection to your skills library — it's supposed to come along automatically, so nothing to do
there.

## Step 2 — Restart Claude Code

Quit it and start it again. Plugins only load at startup.

## Step 3 — Sign in once

The first time AI Sales Engines reaches for your library, a browser window opens asking you to
sign in to BotBuilders and approve access. Do that once per computer and you're done.

## Using it

Just ask, in plain English:

- "I want to sell something. Where do I start?"
- "Help me make an offer for my coaching business."
- "I need a sales webinar for my course."
- "I want to turn what I know into an online course."

There are no commands to memorize. If you'd rather point it at the library directly, type
**`/ai-sales-engine`**.

## Two things it will never do

- **It won't invent a fact.** No made-up results, testimonials, credentials, deadlines, or
  scarcity. If something's missing, it tells you what's missing instead of filling it in.
- **It won't mix builds.** Each chat runs one Engine. It will suggest a new chat for another one.

## If something looks wrong

**"It says my library is empty."** Your account isn't switched on for AI Sales Engines yet. That's
a billing thing, not a broken install — email support@botbuilders.com.

**"It's asking me to sign in again."** Normal on a new computer. Also happens if you were signed
out.

**"The install didn't mention `ai-skills`."** Something went sideways. Run
`claude plugin install ai-skills@ai-sales-engine` and restart.

## Removing it

```
claude plugin uninstall ai-sales-engine@ai-sales-engine
claude plugin prune -y
claude plugin marketplace remove ai-sales-engine
```

The middle command cleans up the shared connection. It's separate on purpose, so removing one
BotBuilders product never breaks another one you're still using.

---

Questions: support@botbuilders.com
