"""
Generate OG images (1200x630, <150KB, Sumi & Shu theme) and favicons.
"""

import os
from PIL import Image, ImageDraw, ImageFont

IMG_DIR = "img"
os.makedirs(IMG_DIR, exist_ok=True)

# List of pages and their H1 titles
OG_PAGES = [
    ("og-anime-name-generator.png", "Anime Name Generator", "名", "Random Japanese Character Names & Authentic Kanji"),
    ("og-anime-username-generator.png", "Anime Username Generator", "号", "Cool & Aesthetic Handles for Gamers & Creators"),
    ("og-anime-usernames-for-tiktok.png", "Anime Usernames for TikTok", "瞬", "Viral Aesthetic Handles Under 24 Characters"),
    ("og-anime-usernames-for-discord.png", "Anime Usernames for Discord", "響", "Server Tags & Aesthetic Nicknames Under 32 Chars"),
    ("og-anime-names-with-meaning.png", "Anime Names With Meaning", "意", "Kanji, Romaji & Philosophical Japanese Origins"),
    ("og-anime-last-name-generator.png", "Anime Last Name Generator", "姓", "Noble Clan Surnames, Origins & Kanji Meanings"),
    ("og-anime-villain-name-generator.png", "Anime Villain Name Generator", "魔", "Dark, Sinister & Antagonist Japanese Names"),
    ("og-anime-boy-names.png", "Anime Boy Names", "雄", "Heroic Male Japanese Names with Traditional Kanji"),
    ("og-anime-girl-names.png", "Anime Girl Names", "華", "Cute & Elegant Japanese Female Names with Kanji")
]

def get_font(font_name, size):
    font_path = os.path.join(os.environ.get("WINDIR", "C:\\Windows"), "Fonts", font_name)
    if os.path.exists(font_path):
        try:
            return ImageFont.truetype(font_path, size)
        except Exception:
            pass
    return ImageFont.load_default()

def create_og_image(filename, h1_text, kanji_seal, subtitle_text):
    width, height = 1200, 630
    img = Image.new("RGB", (width, height), color=(17, 18, 21)) # Ink 900
    draw = ImageDraw.Draw(img)

    # Decorative border in subtle ink
    draw.rectangle([(24, 24), (width - 25, height - 25)], outline=(41, 43, 51), width=2)
    # Inner border accent
    draw.rectangle([(32, 32), (width - 33, height - 33)], outline=(30, 32, 38), width=1)

    # Top accent line in Shu Vermilion
    draw.line([(60, 48), (width - 60, 48)], fill=(200, 57, 43), width=4)

    # Hanko seal (Vermilion stamp)
    seal_x, seal_y = 80, 100
    seal_size = 96
    draw.rectangle([(seal_x, seal_y), (seal_x + seal_size, seal_y + seal_size)], fill=(200, 57, 43))
    draw.rectangle([(seal_x + 3, seal_y + 3), (seal_x + seal_size - 4, seal_y + seal_size - 4)], outline=(245, 230, 228), width=2)

    # Kanji inside seal
    kanji_font = get_font("YuGothB.ttc", 60)
    # Fallback to msgothic
    if kanji_font == ImageFont.load_default():
        kanji_font = get_font("msgothic.ttc", 60)
    draw.text((seal_x + 18, seal_y + 14), kanji_seal, font=kanji_font, fill=(255, 255, 255))

    # Brand label
    brand_font = get_font("georgia.ttf", 24)
    draw.text((seal_x + seal_size + 24, seal_y + 20), "SUMI & SHU  |  ANIME NAME GENERATOR", font=brand_font, fill=(166, 172, 190))
    cat_font = get_font("arial.ttf", 16)
    draw.text((seal_x + seal_size + 24, seal_y + 56), "AUTHENTIC JAPANESE ONOMASTICS & SEO TOOLS", font=cat_font, fill=(200, 57, 43))

    # Main H1 Title
    title_font = get_font("georgia.ttf", 56)
    # Wrap if title is long
    draw.text((80, 260), h1_text, font=title_font, fill=(250, 250, 247))

    # Subtitle / Intent
    sub_font = get_font("arial.ttf", 26)
    draw.text((80, 360), subtitle_text, font=sub_font, fill=(180, 185, 200))

    # Bottom badge elements
    draw.line([(80, 460), (width - 80, 460)], fill=(41, 43, 51), width=1)
    badge_font = get_font("arial.ttf", 18)
    draw.text((80, 490), "✓ Zero Cross-Page Repeats", font=badge_font, fill=(147, 152, 168))
    draw.text((380, 490), "✓ Accurate Kanji & Meanings", font=badge_font, fill=(147, 152, 168))
    draw.text((700, 490), "✓ One-Click Instant Copy", font=badge_font, fill=(147, 152, 168))
    draw.text((1000, 490), "✓ 100% Free", font=badge_font, fill=(200, 57, 43))

    # Save optimized PNG
    out_path = os.path.join(IMG_DIR, filename)
    img.save(out_path, format="PNG", optimize=True)
    size_kb = os.path.getsize(out_path) / 1024
    print(f"Created {filename}: {size_kb:.1f} KB (must be <150 KB)")
    assert size_kb < 150, f"{filename} is {size_kb} KB, exceeds 150 KB limit!"

def create_favicons():
    # Base favicon image 512x512
    base = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(base)
    # Vermilion rounded rectangle
    draw.rounded_rectangle([(32, 32), (480, 480)], radius=64, fill=(200, 57, 43, 255))
    draw.rounded_rectangle([(44, 44), (468, 468)], radius=56, outline=(255, 255, 255, 180), width=8)

    kanji_font = get_font("YuGothB.ttc", 300)
    if kanji_font == ImageFont.load_default():
        kanji_font = get_font("msgothic.ttc", 300)
    draw.text((106, 85), "名", font=kanji_font, fill=(255, 255, 255, 255))

    # 512x512
    base.save(os.path.join(IMG_DIR, "icon-512.png"), format="PNG", optimize=True)
    # 192x192
    icon_192 = base.resize((192, 192), Image.Resampling.LANCZOS)
    icon_192.save(os.path.join(IMG_DIR, "icon-192.png"), format="PNG", optimize=True)
    # 180x180 (apple touch icon)
    icon_180 = base.resize((180, 180), Image.Resampling.LANCZOS)
    icon_180.save(os.path.join(IMG_DIR, "apple-touch-icon.png"), format="PNG", optimize=True)
    # 32x32
    icon_32 = base.resize((32, 32), Image.Resampling.LANCZOS)
    icon_32.save(os.path.join(IMG_DIR, "favicon-32.png"), format="PNG", optimize=True)
    # .ico
    base.resize((32, 32), Image.Resampling.LANCZOS).save(os.path.join(IMG_DIR, "favicon.ico"), format="ICO")

    # favicon.svg
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="10" fill="#C8392B"/>
  <rect x="3" y="3" width="58" height="58" rx="8" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-opacity="0.7"/>
  <text x="32" y="47" font-family="'Yu Mincho', 'MS Mincho', Georgia, serif" font-size="38" font-weight="900" fill="#FFFFFF" text-anchor="middle">名</text>
</svg>'''
    with open(os.path.join(IMG_DIR, "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(svg_content)

    # Decorative hanko SVG
    hanko_content = '''<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48" role="img" aria-label="Authentic Japanese Hanko Seal">
  <rect x="2" y="2" width="44" height="44" rx="6" fill="#C8392B"/>
  <rect x="5" y="5" width="38" height="38" rx="4" fill="none" stroke="#FFFFFF" stroke-width="1.5" stroke-opacity="0.8"/>
  <text x="24" y="34" font-family="'Yu Mincho', 'MS Mincho', Georgia, serif" font-size="28" font-weight="bold" fill="#FFFFFF" text-anchor="middle">名</text>
</svg>'''
    with open(os.path.join(IMG_DIR, "hanko-stamp.svg"), "w", encoding="utf-8") as f:
        f.write(hanko_content)

    # site.webmanifest
    manifest = {
        "name": "Anime Name Generator",
        "short_name": "AnimeNames",
        "icons": [
            {"src": "/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "/img/icon-512.png", "sizes": "512x512", "type": "image/png"}
        ],
        "theme_color": "#C8392B",
        "background_color": "#FAFAF7",
        "display": "standalone"
    }
    with open("site.webmanifest", "w", encoding="utf-8") as f:
        import json
        json.dump(manifest, f, indent=2)

    print("Created all favicons and site.webmanifest successfully.")

if __name__ == "__main__":
    for filename, h1_text, kanji_seal, sub_text in OG_PAGES:
        create_og_image(filename, h1_text, kanji_seal, sub_text)
    create_favicons()
