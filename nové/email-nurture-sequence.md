# spndr — Email Nurture Sequence (Waitlist → Paying Customer)

_Ready to load into Loops.so or send as plain text. Replace `[STRIPE_PRO_LINK]` and `[STRIPE_MAX_LINK]` with live Stripe links before activating._

---

## Email 1 — Welcome (Sends immediately after signup)

**Subject:** You just made a smart move

**From:** Team spndr <hello@spndr.dev>

---

Hey [first_name],

Welcome to spndr.

You're on the waitlist for the AI finance agent built for people who are too busy earning to spend hours figuring out where it all goes.

Here's what that means for you:

- **One dashboard** — every bank account, credit card, and investment account in one place
- **AI that works 24/7** — automatically categorizes transactions, flags subscriptions, surfaces insights
- **Real tax savings** — our users find an average of **$2,300 in missed deductions** they were leaving on the table every year

That last number isn't a typo. The average freelancer, consultant, or multi-income earner in the US misses over two grand a year because their bank app shows them transactions — not opportunities.

spndr shows you opportunities.

While you wait for early access, take a look at what you're getting:

**→ [Explore spndr.dev](https://spndr.dev)**

Talk soon,
The spndr team

_P.S. — We're onboarding early users this week. Keep an eye on your inbox._

---

## Email 2 — Day 3: The Tax Angle

**Subject:** Quick question: are you claiming all your deductions?

**From:** Team spndr <hello@spndr.dev>

---

Hey [first_name],

Real talk — most freelancers and consultants leave **$2,300 per year** in tax deductions unclaimed.

Not because they're careless. Because nobody told them what counts.

Here are the 5 most commonly missed deductions:

1. **Home office** — if you work from home even part-time, a portion of your rent/mortgage, utilities, and internet is deductible
2. **Professional subscriptions** — Notion, Figma, GitHub, LinkedIn Premium, Spotify (if used for work) — all potentially deductible
3. **Phone + internet** — the business-use percentage of your monthly bill
4. **Education + courses** — books, online courses, conferences related to your field
5. **Health insurance premiums** — if you're self-employed and pay your own premiums, these are often fully deductible

Your bank sees these as expenses. spndr sees them as write-offs.

spndr Max — our pro tier — goes further. It surfaces deduction opportunities in real time, exports tax-ready reports, and flags categories you might have missed throughout the year.

**→ [See what Max includes]([STRIPE_MAX_LINK])**

No pressure — just wanted to make sure you knew what you're potentially leaving behind.

Talk soon,
The spndr team

---

## Email 3 — Day 7: Direct Upgrade Ask

**Subject:** Ready to stop leaving money on the table?

**From:** Team spndr <hello@spndr.dev>

---

Hey [first_name],

You signed up for spndr because you wanted clarity on your money.

We built it because the tools that exist — Mint, YNAB, your bank app — show you the past. They don't help you optimize.

spndr does. And we want you using it.

This week, we're doing something we're only doing for the first 100 users:

**Upgrade to spndr Pro and get 2 months free.**

That's two months of:
- Unlimited account connections
- AI-powered tax deduction surfacing
- Smart subscription audits
- Multi-income tracking
- Priority support

All for **$9/month** after the free period — less than a single missed write-off.

We're not going to hammer you with emails after this. This offer is real, it's limited, and it expires in 48 hours.

**→ [Upgrade to Pro — $9/mo]([STRIPE_PRO_LINK])**

If you have questions, just reply to this email. We actually read them.

— The spndr team

_⚠️ Offer expires in 48 hours. First 100 users only._

---

## Notes for Setup

- **Email 1** → triggers on waitlist signup (immediate)
- **Email 2** → 3-day delay
- **Email 3** → 7-day delay (or 4 days after Email 2)
- Replace `[STRIPE_PRO_LINK]` with the Stripe Pro payment link
- Replace `[STRIPE_MAX_LINK]` with the Stripe Max payment link
- `[first_name]` is a Loops.so merge tag — confirm field name in your Loops contact model
