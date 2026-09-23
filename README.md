# BotBuilders AI Sales Engines

Three guided builds for selling what you know. Ask in plain English and the right Engine picks
itself up. There are no commands to learn.

- **Offer Generator** — six short phases from a rough idea to a tested Offer Blueprint and product visuals.
- **Webinar Creator** — ten phases to a sales webinar, every slide, and a to-do list.
- **Course Builder** — ten phases to a finished course and a practical build plan.

## Install

```bash
claude plugin marketplace add BotBuilders/ai-sales-engine
claude plugin install ai-sales-engine@ai-sales-engine
```

That is it. The shared **AI Skills** connection installs automatically alongside it — you do not
add a second marketplace for it. Restart Claude Code, and the first time the connection is used
you will be asked to sign in in your browser and approve access.

## Use it

Just ask:

- "I want to sell something. Where do I start?"
- "Help me make an offer for my coaching business."
- "I need a sales webinar for my course."
- "I want to turn what I know into an online course."

Or type **/ai-sales-engine** to point it at the library explicitly.

## Good to know

- **One Engine per chat.** Each build keeps one Blueprint up to date. Start a new chat for a
  different Engine.
- **It will not invent a fact.** No made-up results, testimonials, credentials, deadlines, or
  scarcity. Where something is missing it names the gap.
- **If the library looks empty,** your account is not switched on for AI Sales Engines yet. That
  is a billing question — support@botbuilders.com.

## Buying another product later

One more `claude plugin install`. The skills connection is shared, so you do not sign in again.

## Uninstall

```bash
claude plugin uninstall ai-sales-engine@ai-sales-engine
claude plugin prune -y          # removes the shared connection once nothing needs it
claude plugin marketplace remove ai-sales-engine
```

`prune` is a separate step on purpose — uninstalling a product never rips the shared connection
out from under another product you still have.

## Requirements

Claude Code 2.1.247 or newer.
