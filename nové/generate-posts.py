import asyncio
import base64
import os
from pathlib import Path
from playwright.async_api import async_playwright

BASE = Path("/Users/cinconko/Desktop/Bez názvu 2")
POSTS = BASE / "posts"
PHOTOS = BASE / "branding" / "Branding" / "AI Visuals - Website _ Landing Page"

W, H = 1080, 1350

def photo_b64(filename):
    p = PHOTOS / filename
    with open(p, "rb") as f:
        return base64.b64encode(f.read()).decode()

def wrap_html(inner_html):
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ width:{W}px; height:{H}px; overflow:hidden; font-family:system-ui,-apple-system,'Segoe UI',Roboto,sans-serif; }}
</style>
</head><body>{inner_html}</body></html>"""


# === SINGLE IMAGE POSTS ===

def single_post_html(photo_file, headline_html, subtitle, watermark_pos="bl"):
    b64 = photo_b64(photo_file)
    return wrap_html(f"""
<div style="width:{W}px;height:{H}px;position:relative;overflow:hidden;background:#0a0a0a">
  <div style="position:absolute;inset:0;background:url(data:image/png;base64,{b64}) center/cover"></div>
  <div style="position:absolute;inset:0;background:linear-gradient(to top,#0a0a0a 18%,rgba(10,10,10,0.4) 45%,transparent 65%)"></div>
  <div style="position:absolute;bottom:72px;left:56px;right:56px">
    <div style="font-size:17px;color:#999;font-weight:900;letter-spacing:-0.05em;margin-bottom:14px">spndr<span style="color:#f97316">.</span></div>
    <h1 style="font-size:58px;font-weight:900;line-height:1.08;letter-spacing:-0.03em;color:#fff;margin:0">{headline_html}</h1>
    <p style="font-size:21px;color:#ccc;margin-top:14px;line-height:1.4">{subtitle}</p>
  </div>
</div>""")


def stat_post_html(big_number, big_label, body_text, bottom_line=None):
    bottom_html = ""
    if bottom_line:
        bottom_html = f'<p style="font-size:22px;font-weight:700;color:#fff;margin-top:48px;max-width:500px;line-height:1.4">{bottom_line}</p>'
    return wrap_html(f"""
<div style="width:{W}px;height:{H}px;background:#0a0a0a;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;position:relative;padding:80px 60px">
  <div style="width:48px;height:3px;background:#f97316;margin-bottom:56px"></div>
  <div style="font-size:96px;font-weight:900;color:#f97316;font-style:italic;line-height:1">{big_number}</div>
  <div style="font-size:20px;color:#999;margin-top:8px;letter-spacing:0.5px">{big_label}</div>
  <p style="font-size:26px;color:#f0f0f0;margin-top:40px;line-height:1.5;max-width:680px">{body_text}</p>
  {bottom_html}
  <div style="position:absolute;bottom:48px;left:50%;transform:translateX(-50%);font-size:17px;color:#666;font-weight:900;letter-spacing:-0.05em">spndr<span style="color:#f97316">.</span></div>
</div>""")


# === CAROUSEL TEMPLATES ===

def carousel_hook_html(photo_file, headline_html, subtitle, slide_num, total_slides):
    b64 = photo_b64(photo_file)
    return wrap_html(f"""
<div style="width:{W}px;height:{H}px;position:relative;overflow:hidden;background:#0a0a0a">
  <div style="position:absolute;inset:0;background:url(data:image/png;base64,{b64}) center/cover"></div>
  <div style="position:absolute;inset:0;background:linear-gradient(to top,#0a0a0a 18%,rgba(10,10,10,0.4) 45%,transparent 65%)"></div>
  <div style="position:absolute;top:36px;right:44px;font-size:16px;color:rgba(255,255,255,0.45);font-weight:500">{slide_num} / {total_slides}</div>
  <div style="position:absolute;bottom:72px;left:56px;right:56px">
    <div style="font-size:17px;color:#999;font-weight:900;letter-spacing:-0.05em;margin-bottom:14px">spndr<span style="color:#f97316">.</span></div>
    <h1 style="font-size:56px;font-weight:900;line-height:1.08;letter-spacing:-0.03em;color:#fff;margin:0">{headline_html}</h1>
    <p style="font-size:20px;color:#ccc;margin-top:14px">{subtitle}</p>
  </div>
  <div style="position:absolute;bottom:36px;right:44px;font-size:15px;color:#999">Swipe →</div>
</div>""")


def carousel_content_html(number, heading_html, body_text, slide_num, total_slides):
    return wrap_html(f"""
<div style="width:{W}px;height:{H}px;background:#0a0a0a;padding:80px 56px;display:flex;flex-direction:column;justify-content:center;position:relative">
  <div style="position:absolute;top:36px;right:44px;font-size:16px;color:rgba(255,255,255,0.45);font-weight:500">{slide_num} / {total_slides}</div>
  <div style="font-size:110px;font-weight:900;color:#f97316;line-height:1;font-style:italic;margin-bottom:12px">{number}</div>
  <h2 style="font-size:44px;font-weight:800;line-height:1.12;color:#fff;margin:0 0 20px;letter-spacing:-0.02em">{heading_html}</h2>
  <p style="font-size:23px;color:#e0e0e0;line-height:1.55;max-width:85%">{body_text}</p>
  <div style="position:absolute;bottom:48px;left:56px;font-size:17px;color:#666;font-weight:900;letter-spacing:-0.05em">spndr<span style="color:#f97316">.</span></div>
</div>""")


def carousel_cta_html(photo_file, headline_html, cta_text, handle, slide_num, total_slides):
    b64 = photo_b64(photo_file)
    return wrap_html(f"""
<div style="width:{W}px;height:{H}px;position:relative;overflow:hidden;background:#0a0a0a">
  <div style="position:absolute;inset:0;background:url(data:image/png;base64,{b64}) center/cover"></div>
  <div style="position:absolute;inset:0;background:linear-gradient(to top,#0a0a0a 30%,rgba(10,10,10,0.5) 55%,transparent 70%)"></div>
  <div style="position:absolute;top:36px;left:44px;font-size:17px;color:rgba(255,255,255,0.7);font-weight:900;letter-spacing:-0.05em">spndr<span style="color:#f97316">.</span></div>
  <div style="position:absolute;top:36px;right:44px;font-size:16px;color:rgba(255,255,255,0.45);font-weight:500">{slide_num} / {total_slides}</div>
  <div style="position:absolute;bottom:72px;left:0;right:0;text-align:center">
    <h2 style="font-size:50px;font-weight:900;color:#fff;line-height:1.15;letter-spacing:-0.02em;margin:0">{headline_html}</h2>
    <div style="display:inline-block;margin-top:28px;padding:16px 44px;background:#f97316;border-radius:8px;font-size:22px;font-weight:700;color:#fff">{cta_text}</div>
    <p style="font-size:16px;color:#999;margin-top:20px">{handle}</p>
  </div>
</div>""")


def carousel_steps_html(steps, slide_num, total_slides):
    steps_html = ""
    for i, (num, title) in enumerate(steps):
        mb = "margin-bottom:48px;" if i < len(steps)-1 else ""
        steps_html += f"""
        <div style="{mb}">
          <div style="font-size:72px;font-weight:900;color:#f97316;font-style:italic;line-height:1">{num}</div>
          <div style="font-size:20px;color:#ccc;margin-top:4px">{title}</div>
        </div>"""
    return wrap_html(f"""
<div style="width:{W}px;height:{H}px;background:#0a0a0a;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;position:relative;padding:80px 60px">
  <div style="position:absolute;top:36px;right:44px;font-size:16px;color:rgba(255,255,255,0.45);font-weight:500">{slide_num} / {total_slides}</div>
  <div style="width:48px;height:3px;background:#f97316;margin-bottom:56px"></div>
  {steps_html}
  <div style="position:absolute;bottom:48px;left:50%;transform:translateX(-50%);font-size:17px;color:#666;font-weight:900;letter-spacing:-0.05em">spndr<span style="color:#f97316">.</span></div>
</div>""")


def carousel_features_html(heading_html, features, tagline, slide_num, total_slides):
    feat_html = ""
    for icon, title, desc in features:
        feat_html += f"""
        <div style="margin-bottom:36px">
          <div style="font-size:28px;font-weight:800;color:#fff;margin-bottom:6px">{icon} {title}</div>
          <div style="font-size:20px;color:#ccc;line-height:1.4">{desc}</div>
        </div>"""
    return wrap_html(f"""
<div style="width:{W}px;height:{H}px;background:#0a0a0a;padding:80px 56px;display:flex;flex-direction:column;justify-content:center;position:relative">
  <div style="position:absolute;top:36px;right:44px;font-size:16px;color:rgba(255,255,255,0.45);font-weight:500">{slide_num} / {total_slides}</div>
  <div style="width:48px;height:3px;background:#f97316;margin-bottom:32px"></div>
  <h2 style="font-size:40px;font-weight:900;color:#fff;line-height:1.12;margin:0 0 40px;letter-spacing:-0.02em">{heading_html}</h2>
  {feat_html}
  <p style="font-size:22px;color:#999;margin-top:16px;font-style:italic">{tagline}</p>
  <div style="position:absolute;bottom:48px;left:56px;font-size:17px;color:#666;font-weight:900;letter-spacing:-0.05em">spndr<span style="color:#f97316">.</span></div>
</div>""")


# ===== ALL POSTS DEFINITION =====

POSTS_TO_CREATE = {
    # Post 02: Single - Meet spndr
    "02-single-meet-spndr/slide-1.png": lambda: single_post_html(
        "Reference_usage_Use_202603182320.png",
        'Meet <span style="color:#f97316">spndr.</span>',
        "Your AI finance agent. Track everything. Optimize automatically.",
    ),
    # Post 04: Stat - Bank accounts
    "04-stat-bank-accounts/slide-1.png": lambda: stat_post_html(
        "5.3",
        "bank accounts per American",
        "That's checking, savings, credit cards, investments, HSAs — scattered across different apps.",
        "One dashboard to see them all. That's spndr.",
    ),
    # Post 06: Single - Built for earners
    "06-single-built-for-earners/slide-1.png": lambda: single_post_html(
        "Reference_usage_Use_202603182343.png",
        'Built for people who <span style="color:#f97316">earn more</span> than they have time to track.',
        "Multi-income. Multi-account. One AI agent.",
    ),
    # Post 08: Carousel 5 - "3 Things Your Bank App Won't Tell You"
    "08-carousel-bank-app/slide-1.png": lambda: carousel_hook_html(
        "Reference_usage_Use_202603182321.png",
        '3 things your bank app <span style="color:#f97316">won\'t</span> tell you',
        "And they're costing you thousands.",
        1, 3
    ),
    "08-carousel-bank-app/slide-2.png": lambda: carousel_features_html(
        'What your bank <span style="color:#f97316">hides</span> in plain sight',
        [
            ("01", "Hidden fee patterns", "Small charges that add up to hundreds per year — your bank won't flag them"),
            ("02", "Subscription drift", "Services you signed up for and forgot. The average American wastes $238/month"),
            ("03", "Tax-deductible expenses", "Your bank sees transactions. spndr sees tax write-offs hiding in them"),
        ],
        "spndr catches what your bank misses.",
        2, 3
    ),
    "08-carousel-bank-app/slide-3.png": lambda: carousel_cta_html(
        "Reference_usage_Use_202603182335.png",
        'spndr catches what<br>your bank <span style="color:#f97316">misses.</span>',
        "Try spndr free", "@spndr.app",
        3, 3
    ),
    # Post 09: Single - Accountant
    "09-single-accountant/slide-1.png": lambda: single_post_html(
        "Reference_usage_Use_202603182335 (1).png",
        'Your accountant sees your finances <span style="color:#f97316">once a year.</span>',
        "spndr sees them in real time.",
    ),
    # Post 10: Carousel 6 - "How spndr Works"
    "10-carousel-how-it-works/slide-1.png": lambda: carousel_hook_html(
        "Reference_usage_Use_202603182335 (1).png",
        '<span style="color:#f97316">Connect.</span> Track. Optimize.',
        "How spndr works — in 30 seconds.",
        1, 3
    ),
    "10-carousel-how-it-works/slide-2.png": lambda: carousel_steps_html(
        [
            ("5,000+", "Connect your banks in seconds"),
            ("24/7", "AI categorizes every transaction"),
            ("$0", "Tax optimization insights — free forever"),
        ],
        2, 3
    ),
    "10-carousel-how-it-works/slide-3.png": lambda: carousel_cta_html(
        "Reference_usage_Use_202603182343.png",
        'Set it up in <span style="color:#f97316">30 seconds.</span><br>Free forever.',
        "Get started free", "@spndr.app",
        3, 3
    ),
    # Post 11: Stat - Subscriptions
    "11-stat-subscriptions/slide-1.png": lambda: stat_post_html(
        "$2,400",
        "per year",
        "That's what the average American loses to forgotten subscriptions they don't even use.",
        "spndr finds them. Automatically.",
    ),
    # Post 12: Carousel 7 - "The Spreadsheet Era Is Over"
    "12-carousel-spreadsheet/slide-1.png": lambda: carousel_hook_html(
        "Reference_usage_Use_202603182332.png",
        'The spreadsheet era is <span style="color:#f97316">over.</span>',
        "There's a smarter way to manage your money.",
        1, 2
    ),
    "12-carousel-spreadsheet/slide-2.png": lambda: carousel_cta_html(
        "Reference_usage_Use_202603182320.png",
        'Your AI finance agent<br>is <span style="color:#f97316">ready.</span>',
        "Try spndr free", "@spndr.app",
        2, 2
    ),
}


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": W, "height": H})

        for rel_path, html_fn in POSTS_TO_CREATE.items():
            out_path = POSTS / rel_path
            out_path.parent.mkdir(parents=True, exist_ok=True)
            
            html = html_fn()
            tmp = BASE / "_tmp_post.html"
            tmp.write_text(html, encoding="utf-8")
            
            await page.goto(f"file://{tmp}")
            await page.wait_for_timeout(300)
            await page.screenshot(path=str(out_path), clip={"x": 0, "y": 0, "width": W, "height": H})
            print(f"  OK  {rel_path}")

        tmp.unlink(missing_ok=True)
        await browser.close()
    print(f"\nDone — {len(POSTS_TO_CREATE)} images generated.")

asyncio.run(main())
