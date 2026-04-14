# spndr Community Outreach Posts

> Ready to copy-paste. Post at 8–9 AM EST for maximum visibility.

---

## 1. Reddit r/personalfinance

**Title:** I built an AI that analyzes your bank transactions and found $4,800 in savings I was leaving on the table

**Body:**

Last year I sat down one Sunday to do my taxes and realized I had no idea where half my money was going. I'm a freelancer with income from three sources — client work, a side SaaS, and some consulting. I had accounts at two banks, a brokerage, and PayPal. None of them talked to each other.

I spent an entire weekend in spreadsheets. Manually categorizing hundreds of transactions. Trying to figure out which expenses were deductible. I found a $47/month subscription I forgot about (some analytics tool I used once). A recurring charge from a gym I canceled. And a pattern: I was spending almost $900/month on food delivery without realizing it.

Total money I was either wasting or not claiming? About $4,800 a year.

That experience bothered me so much that when I went to a hackathon in Slovakia earlier this month, I built a tool to do what I did manually — but with AI. It connects to your bank accounts (read-only, via Plaid), auto-categorizes every transaction, detects subscriptions, and flags tax deductions you're probably missing.

A few things I learned building it:

- **Most people with multiple income sources have no single view of their money.** Bank apps are designed for single-account holders with a salary.
- **Subscription creep is real.** The average person in our early testing had 2–3 subscriptions they forgot about.
- **Tax deductions are the big one.** If you freelance or have side income, you're almost certainly leaving money on the table. The average user we've seen so far is missing about $2,300 in deductions.

I'm not trying to replace your accountant. This is more like having a financial co-pilot that actually pays attention to your accounts every day — something your bank app should do but doesn't.

If you're curious, it's at [spndr.dev](https://spndr.dev). There's a free tier if you just want to connect one account and see what it finds. Happy to answer any questions about the tech or the approach.

---

## 2. Reddit r/SideProject

**Title:** I built an AI finance agent at a hackathon in 48 hours — here's what I shipped and what I learned

**Body:**

Two weeks ago I went to a hackathon in Slovakia (Pronea Hackathon 2026) with one idea: build a personal finance tool that actually works for people with messy, multi-source income.

I'm a freelancer. I have income from three places, accounts at two banks, and a PayPal. Every finance app I tried was built for someone with a single paycheck going into a single checking account. That's not my life, and it's probably not yours either if you're building side projects.

**What I built in 48 hours:**

An AI agent that connects to your bank accounts via Plaid (12,000+ banks, read-only), pulls all your transactions, and does the analysis you'd never bother doing yourself — categorization, subscription detection, spending pattern analysis, and tax deduction flagging.

**Stack:**

- Next.js frontend
- Plaid for bank connectivity
- LLM layer for natural language queries ("how much did I spend on food this month?" → real answer)
- Telegram bot as the primary interface (no app download needed)

**The non-obvious decisions:**

1. **Telegram-first, not app-first.** Building a native app at a hackathon is suicide. But more importantly, I realized people don't want *another* app to open. They want their finances to come to them. Morning briefing in Telegram. Alerts when something looks weird. That's it.

2. **Personality modes.** This sounds gimmicky but it's the feature people latched onto. You can switch between a calm advisor, a motivating hype mode, and a brutal roast mode that shames your spending. The roast mode gets people to actually look at their spending data. Behavioral design > feature checklists.

3. **Proactive > reactive.** Every finance app waits for you to open it. I built spndr to message you first. "Hey, you spent $340 on food delivery this week — that's 2x your average." You never have to remember to check.

**What I learned:**

- Plaid integration is genuinely excellent. Took about 3 hours to get working.
- The AI categorization accuracy got good fast — merchant names are surprisingly parseable.
- People care way more about "what should I do?" than "what did I spend?" The insight layer matters more than the data layer.

It's live at [spndr.dev](https://spndr.dev) if you want to check it out. Free tier, no credit card. Would love feedback from other builders.

---

## 3. Hacker News — Show HN

**Title:** Show HN: spndr – AI finance agent for people with complex income

**Body:**

I freelance with income from multiple sources and got tired of manually reconciling transactions across bank accounts every month. Built spndr at a hackathon to scratch that itch.

**What it does:** Connects to 12,000+ banks via Plaid (read-only). AI auto-categorizes transactions, detects subscriptions, flags tax deductions, and sends proactive alerts. You interact via natural language — ask "how much did I spend on SaaS tools this quarter?" and get a real answer.

**Key design decision:** Telegram-first, not app-first. Your financial data comes to you via morning briefings and spending alerts. No app to remember to open.

**Who it's for:** People with 2+ income sources — freelancers, consultants, founders with side projects. The existing tools (Mint is dead, YNAB is manual, Cleo targets Gen Z) don't serve this segment well.

**Pricing:** Free tier (1 account, 3 AI queries/day). Pro $9/mo. Max $19/mo with tax optimization.

Stack: Next.js, Plaid, LLM-powered categorization and chat.

Live at https://spndr.dev

---

## 4. Reddit r/startups

**Title:** How we're taking on Cleo ($350M ARR) by building for the customers they ignore

**Body:**

Cleo does $350M in annual revenue. They've nailed their market: Gen Z users who need help not overdrafting. Sarcastic AI, cash advances, credit building. Great product for that audience.

But here's the gap we spotted: Cleo doesn't serve anyone who actually earns well.

If you make $100k+ from multiple sources — freelancing, consulting, a side business, creator income — Cleo isn't built for you. Neither is YNAB (too manual), Monarch (no AI), or Copilot (no proactive intelligence). And Mint is dead.

We built spndr at a hackathon in Slovakia two weeks ago. The thesis was simple: **what if your finances managed themselves?**

The product connects to your banks via Plaid, auto-categorizes everything, and proactively reaches out to you with insights. Not "open the app and look at charts." More like "hey, your DoorDash spending is up 40% this month — want me to set a limit?"

**Our unfair advantages with a $0 marketing budget:**

1. **Telegram-first distribution.** No app store approval. No downloads. Users are live in 2 minutes. Telegram has 900M+ users and zero cost to distribute through.

2. **The product saves real money.** Average user in early testing found ~$2,300 in missed tax deductions. When a product pays for itself 100x over, word of mouth does the marketing.

3. **We're building for an underserved segment.** Every finance app goes after the mass market. We're going after the 73 million Americans with non-traditional income who are currently using spreadsheets or nothing at all.

4. **Hackathon-to-product speed.** We went from idea to live product in 48 hours, and from live product to first paying customer in under 12 hours after that. When your iteration cycle is measured in hours, you can afford to have no marketing budget.

We're not trying to out-Cleo Cleo. We're going after the segment above them — people whose hour is worth $100+ and who need a financial co-pilot, not a budgeting toy.

Early days, but we're seeing strong pull from the exact persona we built for. The site is [spndr.dev](https://spndr.dev) if you want to look at how we're positioning it.

Curious if anyone else is building in fintech against an entrenched competitor — how do you think about market segmentation when the incumbent has massive distribution?

---

## 5. IndieHackers

**Title:** From hackathon to first paying customer in 10 hours — our playbook

**Body:**

I want to share the timeline because I think it's useful for anyone trying to validate an idea fast.

**Hour 0–6: Hackathon starts (Slovakia, Pronea Hackathon 2026)**

We had one hypothesis: people with complex income (freelancers, consultants, multi-source earners) are underserved by every finance app on the market. Mint is dead. YNAB requires manual entry. Cleo is for Gen Z. There's a gap.

We scoped aggressively. No mobile app. No dashboard. Just: connect your bank, AI analyzes everything, and you get a Telegram bot that proactively sends you insights.

**Hour 6–24: Core product**

Plaid integration for bank connectivity (12,000+ banks). LLM-powered transaction categorization. Natural language query interface ("how much did I spend on Uber this month?"). Morning briefing system. Subscription detection.

The Telegram-first decision was the single best call we made. Zero friction to start using the product. No app store. No onboarding flow. Connect bank → get first insight in under 3 minutes.

**Hour 24–48: Polish + go live**

Landing page (Next.js). Pricing page. Three tiers: Free (1 account), Pro $9/mo (unlimited), Max $19/mo (tax tools). We launched at spndr.dev.

**Hour 48–58: First paying customer**

This is the part I didn't expect. We posted in a few communities. One user connected their account, asked "how much am I spending on subscriptions I don't use?" — the AI found three forgotten subscriptions totaling $127/month. They upgraded to Pro immediately.

**What actually worked:**

- **Solving a hair-on-fire problem.** Everyone with multiple income sources knows the pain. You don't need to explain it.
- **Telegram as distribution.** People already have it. No download. Feels like texting a smart friend, not using a finance app.
- **Personality modes.** We added a "roast mode" where the AI roasts your spending. People share screenshots of their roasts. Free marketing.
- **The product pays for itself.** $9/month when it finds $2,300 in missed deductions? The ROI sells itself.

**What I'd do differently:**

- Should have had analytics from day one. We were flying blind on what features people actually used.
- The free tier is maybe too generous. Still figuring out the right conversion trigger.

We're now at the point where the product is live, people are using it, and we need to figure out growth beyond communities. But the validation loop — hackathon → working product → paying customer in under 60 hours — taught me that you can test an idea way faster than most people think.

If you're sitting on an idea, go to a hackathon. The time constraint forces you to cut everything that doesn't matter.

Check it out at [spndr.dev](https://spndr.dev) if you're curious. Happy to answer questions about the build, the stack, or the go-to-market.
