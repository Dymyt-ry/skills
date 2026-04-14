import os
import glob
from playwright.sync_api import sync_playwright

SRC = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(SRC)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(
        viewport={"width": 1080, "height": 1350},
        device_scale_factor=2,
    )

    for html_file in sorted(glob.glob(os.path.join(SRC, "*.html"))):
        if html_file.endswith("render.py"):
            continue
        base = os.path.splitext(os.path.basename(html_file))[0]
        png_file = os.path.join(OUT, f"{base}.png")

        page.goto(f"file://{html_file}")
        page.wait_for_load_state("networkidle")

        page.screenshot(
            path=png_file,
            clip={"x": 0, "y": 0, "width": 1080, "height": 1350},
        )

        from PIL import Image
        img = Image.open(png_file)
        print(f"OK: {base}.png ({img.size[0]}x{img.size[1]})")

    browser.close()

print("DONE")
