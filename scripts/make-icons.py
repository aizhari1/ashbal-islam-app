#!/usr/bin/env python3
import base64, io, subprocess, sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow", "-q"])
    from PIL import Image

LOGO_B64 = open(Path(__file__).with_name("logo.b64")).read().strip() if Path(__file__).with_name("logo.b64").exists() else ""

def load_logo():
    # Prefer clean logo.b64; else embedded minimal green icon
    candidates = []
    p = Path(__file__).with_name("logo.b64")
    if p.exists():
        candidates.append(p.read_text().strip())
    if LOGO_B64:
        candidates.append(LOGO_B64)
    for b64 in candidates:
        try:
            # fix padding
            b64 = b64.strip().replace("\n", "").replace(" ", "")
            while len(b64) % 4:
                b64 += "="
            data = base64.b64decode(b64)
            img = Image.open(io.BytesIO(data)).convert("RGB")
            print("loaded logo", img.size)
            return img
        except Exception as e:
            print("try failed", e)
    print("using green fallback")
    return Image.new("RGB", (512, 512), (11, 107, 58))

img = load_logo()
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
print("icons ready", img.size)
