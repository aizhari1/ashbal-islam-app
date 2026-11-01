#!/usr/bin/env python3
import base64, io, subprocess, sys
from pathlib import Path
try:
    from PIL import Image
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pillow', '-q'])
    from PIL import Image

# Minimal white icon with green accent if logo decode fails — real logo embedded below when available
# Prefer regenerating from embedded JPEG of academy logo
B64 = None
try:
    B64 = open(Path(__file__).with_name('logo.b64')).read().strip()
except Exception:
    pass

if not B64:
    # 1x1 white fallback will be replaced — generate simple solid
    img = Image.new('RGB', (512, 512), (255, 255, 255))
else:
    img = Image.open(io.BytesIO(base64.b64decode(B64))).convert('RGB')

base = Path('app/src/main/res')
sizes = {
    'mipmap-mdpi': 48,
    'mipmap-hdpi': 72,
    'mipmap-xhdpi': 96,
    'mipmap-xxhdpi': 144,
    'mipmap-xxxhdpi': 192,
}
for folder, size in sizes.items():
    d = base / folder
    d.mkdir(parents=True, exist_ok=True)
    icon = img.resize((size, size), Image.Resampling.LANCZOS)
    icon.save(d / 'ic_launcher.png', 'PNG')
    icon.save(d / 'ic_launcher_round.png', 'PNG')
drawable = base / 'drawable'
drawable.mkdir(parents=True, exist_ok=True)
img.resize((256, 256), Image.Resampling.LANCZOS).save(drawable / 'splash_logo.png', 'PNG')
print('icons ready')
