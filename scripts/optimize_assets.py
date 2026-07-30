"""One-shot asset optimizer. Idempotent — safe to re-run.
Compresses oversized images and generates the OG social card + apple-touch-icon.
"""
from __future__ import annotations
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
IMG_DIR = os.path.join(ROOT, "Assets", "Images")
ICON_DIR = os.path.join(ROOT, "Assets", "Icons")


def _save_jpeg(im: Image.Image, path: str, quality: int = 82):
    im = im.convert("RGB")
    im.save(path, "JPEG", quality=quality, optimize=True, progressive=True)


def _save_png(im: Image.Image, path: str):
    im.save(path, "PNG", optimize=True)


def resize_and_save(src: str, dst: str, max_w: int, jpeg: bool = True, quality: int = 82):
    if not os.path.exists(src):
        print(f"skip (missing): {src}")
        return
    im = Image.open(src)
    if im.width > max_w:
        h = int(im.height * max_w / im.width)
        im = im.resize((max_w, h), Image.LANCZOS)
    if jpeg:
        _save_jpeg(im, dst, quality=quality)
    else:
        _save_png(im, dst)
    before = os.path.getsize(src)
    after = os.path.getsize(dst)
    print(f"{os.path.basename(dst):48s}  {before//1024:>5} KB  ->  {after//1024:>5} KB")


def optimize_azure_icon():
    src = os.path.join(ICON_DIR, "Introduction_to_Azure_Data_Core_Icon.png")
    dst = src  # overwrite
    if not os.path.exists(src):
        return
    im = Image.open(src).convert("RGBA")
    max_side = 128
    if max(im.size) > max_side:
        im.thumbnail((max_side, max_side), Image.LANCZOS)
    im.save(dst, "PNG", optimize=True)
    after = os.path.getsize(dst)
    print(f"Azure icon optimized: now {after//1024} KB @ {im.size}")


def _load_font(size: int, bold: bool = True):
    for cand in [
        os.path.join(os.environ.get("WINDIR", ""), "Fonts", "arialbd.ttf" if bold else "arial.ttf"),
        os.path.join(os.environ.get("WINDIR", ""), "Fonts", "segoeuib.ttf" if bold else "segoeui.ttf"),
    ]:
        if cand and os.path.exists(cand):
            try:
                return ImageFont.truetype(cand, size)
            except Exception:
                pass
    return ImageFont.load_default()


def _draw_bracket_mark(d, cx, cy, letter_size, letters="ZR", letter_color=(255, 255, 255), bracket_color=(96, 165, 250)):
    """Draw the 8d bracketed monogram [ ZR ] centered at (cx, cy).
       Returns total width for layout callers."""
    letter_font = _load_font(letter_size, bold=True)
    bracket_font = _load_font(int(letter_size * 1.32), bold=True)
    gap = int(letter_size * 0.14)
    lb = d.textbbox((0, 0), letters, font=letter_font)
    lb_w = lb[2] - lb[0]
    lb_h = lb[3] - lb[1]
    l_bb = d.textbbox((0, 0), "[", font=bracket_font)
    r_bb = d.textbbox((0, 0), "]", font=bracket_font)
    lb_bw = l_bb[2] - l_bb[0]
    rb_bw = r_bb[2] - r_bb[0]
    total_w = lb_bw + gap + lb_w + gap + rb_bw
    x = cx - total_w / 2
    top = cy - lb_h / 2 - lb[1]
    # Baseline-align brackets with letters
    br_top = cy - (l_bb[3] - l_bb[1]) / 2 - l_bb[1]
    d.text((x - l_bb[0], br_top), "[", fill=bracket_color, font=bracket_font)
    x += lb_bw + gap
    d.text((x - lb[0], top), letters, fill=letter_color, font=letter_font)
    x += lb_w + gap
    d.text((x - r_bb[0], br_top), "]", fill=bracket_color, font=bracket_font)
    return total_w


def make_apple_touch_icon():
    dst = os.path.join(ICON_DIR, "apple-touch-icon.png")
    size = 180
    # Dark tile so blue brackets pop
    im = Image.new("RGBA", (size, size), (11, 18, 32, 255))
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, size, size), radius=34, fill=255)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(im, (0, 0), mask)
    d = ImageDraw.Draw(out)
    _draw_bracket_mark(d, size / 2, size / 2, letter_size=72,
                       letter_color=(255, 255, 255),
                       bracket_color=(96, 165, 250))
    out.save(dst, "PNG", optimize=True)
    print(f"apple-touch-icon.png written ({os.path.getsize(dst)//1024} KB)")


def make_og_card():
    dst = os.path.join(IMG_DIR, "og-card.png")
    W, H = 1200, 630
    # Gradient background: deep blue -> navy
    im = Image.new("RGB", (W, H), (11, 18, 32))
    px = im.load()
    for y in range(H):
        t = y / H
        r = int(11 + (23 - 11) * t)
        g = int(18 + (36 - 18) * t)
        b = int(32 + (88 - 32) * t)
        for x in range(W):
            px[x, y] = (r, g, b)
    d = ImageDraw.Draw(im)

    # Accent blue bar left
    d.rectangle((0, 0, 12, H), fill=(37, 99, 235))
    # Dot grid overlay
    for y in range(24, H, 32):
        for x in range(24, W, 32):
            d.ellipse((x - 1, y - 1, x + 1, y + 1), fill=(60, 80, 130))

    _f = _load_font

    # Bracketed [ ZR ] monogram, left-aligned
    _draw_bracket_mark(d, cx=72 + 48, cy=100, letter_size=48,
                       letter_color=(255, 255, 255),
                       bracket_color=(96, 165, 250))

    # Kicker
    kicker = "FINAL-YEAR COMPUTER SCIENCE CO-OP"
    d.text((72, 200), kicker, fill=(96, 165, 250), font=_f(24))

    # Name
    d.text((72, 244), "Zohaib Rahim", fill=(243, 246, 250), font=_f(96))

    # Tagline
    d.text((72, 360), "Practical technology for real operational needs.", fill=(200, 210, 225), font=_f(34, bold=False))

    # Pill row
    pills = ["Data & Analytics", "Digital Transformation", "Full-Stack Engineering"]
    pill_font = _f(20)
    px_start = 72
    py = 470
    for label in pills:
        b = d.textbbox((0, 0), label, font=pill_font)
        w = b[2] - b[0]
        h = b[3] - b[1]
        pad_x = 20
        pad_y = 10
        d.rounded_rectangle((px_start, py, px_start + w + pad_x * 2, py + h + pad_y * 2), radius=999, outline=(96, 165, 250), width=2, fill=(20, 30, 55))
        d.text((px_start + pad_x - b[0], py + pad_y - b[1]), label, fill=(147, 197, 253), font=pill_font)
        px_start += w + pad_x * 2 + 12

    # URL/handle bottom right
    d.text((W - 380, H - 60), "zohaibrahim.vercel.app", fill=(140, 160, 190), font=_f(22))

    im.save(dst, "PNG", optimize=True)
    print(f"og-card.png written ({os.path.getsize(dst)//1024} KB @ {W}x{H})")


def main():
    # Compress big project screenshots (keep source PNG when it matters for crispness)
    tasks = [
        # (src, dst, max_w, jpeg, quality)
        (os.path.join(IMG_DIR, "Zohaib_Rahim_Headshot.jpg"), os.path.join(IMG_DIR, "Zohaib_Rahim_Headshot.jpg"), 960, True, 82),
        (os.path.join(IMG_DIR, "JDC_West_1st_Team_Photo.png"), os.path.join(IMG_DIR, "JDC_West_1st_Team_Photo.jpg"), 1200, True, 82),
        (os.path.join(IMG_DIR, "Jobtrackr", "Jobtrackr.png"), os.path.join(IMG_DIR, "Jobtrackr", "Jobtrackr.jpg"), 1200, True, 82),
        (os.path.join(IMG_DIR, "Jobtrackr", "Dashboard.png"), os.path.join(IMG_DIR, "Jobtrackr", "Dashboard.jpg"), 1600, True, 85),
        (os.path.join(IMG_DIR, "Jobtrackr", "AI Analysis.png"), os.path.join(IMG_DIR, "Jobtrackr", "AI_Analysis.jpg"), 1600, True, 85),
        (os.path.join(IMG_DIR, "Roshtay_Website.png"), os.path.join(IMG_DIR, "Roshtay_Website.jpg"), 1400, True, 85),
        (os.path.join(IMG_DIR, "PHSA_Stock_Dashboard.png"), os.path.join(IMG_DIR, "PHSA_Stock_Dashboard.jpg"), 1400, True, 85),
        (os.path.join(IMG_DIR, "Canadian_Crime_Dashboard.png"), os.path.join(IMG_DIR, "Canadian_Crime_Dashboard.jpg"), 1400, True, 85),
        (os.path.join(IMG_DIR, "PHSA_Staff_Scheduling_Automation_System.png"), os.path.join(IMG_DIR, "PHSA_Staff_Scheduling_Automation_System.jpg"), 1600, True, 85),
        (os.path.join(IMG_DIR, "Parallel_Sorting_Algorithm", "Comparision Graph.png"), os.path.join(IMG_DIR, "Parallel_Sorting_Algorithm", "Comparision_Graph.jpg"), 1400, True, 85),
        (os.path.join(IMG_DIR, "Parallel_Sorting_Algorithm", "Step_by_Stey_Process.png"), os.path.join(IMG_DIR, "Parallel_Sorting_Algorithm", "Step_by_Step_Process.jpg"), 1400, True, 85),
        (os.path.join(IMG_DIR, "Stock_dashboard", "5.jpg"), os.path.join(IMG_DIR, "Stock_dashboard", "5.jpg"), 1400, True, 85),
        (os.path.join(IMG_DIR, "Stock_dashboard", "6.jpg"), os.path.join(IMG_DIR, "Stock_dashboard", "6.jpg"), 1400, True, 85),
        (os.path.join(IMG_DIR, "Jailbreak", "Screenshot 2026-04-16 032847.png"), os.path.join(IMG_DIR, "Jailbreak", "Jailbreak_Layer_Accuracy.jpg"), 1400, True, 85),
        (os.path.join(IMG_DIR, "Jailbreak", "Screenshot 2026-04-16 032657.png"), os.path.join(IMG_DIR, "Jailbreak", "Jailbreak_Training_Results.jpg"), 1200, True, 85),
    ]
    for src, dst, maxw, jpeg, q in tasks:
        resize_and_save(src, dst, maxw, jpeg=jpeg, quality=q)

    optimize_azure_icon()
    make_apple_touch_icon()
    make_og_card()


if __name__ == "__main__":
    main()
