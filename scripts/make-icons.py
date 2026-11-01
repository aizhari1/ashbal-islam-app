#!/usr/bin/env python3
"""Generate Android launcher + splash icons from the academy logo."""
import io
import subprocess
import sys
import urllib.request
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow", "-q"])
    from PIL import Image

LOGO_URLS = [
    "https://ashbal-islam.vercel.app/icons/icon-512.png",
    "https://ashbal-islam.vercel.app/apple-touch-icon.png",
    "https://ashbal-islam.vercel.app/logo.svg",
]

def fetch_logo() -> Image.Image:
    for url in LOGO_URLS:
        try:
            print("fetch", url)
            with urllib.request.urlopen(url, timeout=30) as r:
                data = r.read()
            img = Image.open(io.BytesIO(data)).convert("RGBA")
            # white background for transparent
            bg = Image.new("RGB", img.size, (255, 255, 255))
            bg.paste(img, mask=img.split()[-1] if img.mode == "RGBA" else None)
            # square crop/pad
            w, h = bg.size
            side = max(w, h)
            canvas = Image.new("RGB", (side, side), (255, 255, 255))
            canvas.paste(bg, ((side - w) // 2, (side - h) // 2))
            print("logo ok", canvas.size)
            return canvas
        except Exception as e:
            print("fail", url, e)
    print("fallback green")
    return Image.new("RGB", (512, 512), (11, 107, 58))

img = fetch_logo()
base = Path("app/src/main/res")
sizes = {
    "mipmap-mdpi": 48,
    "mipmap-hdpi": 72,
    "mipmap-xhdpi": 96,
    "mipmap-xxhdpi": 144,
    "mipmap-xxxhdpi": 192,
}
for folder, size in sizes.items():
    d = base / folder
    d.mkdir(parents=True, exist_ok=True)
    icon = img.resize((size, size), Image.Resampling.LANCZOS)
    icon.save(d / "ic_launcher.png", "PNG")
    icon.save(d / "ic_launcher_round.png", "PNG")

drawable = base / "drawable"
drawable.mkdir(parents=True, exist_ok=True)
img.resize((256, 256), Image.Resampling.LANCZOS).save(drawable / "splash_logo.png", "PNG")
print("icons ready from academy logo")
