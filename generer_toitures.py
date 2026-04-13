#!/usr/bin/env python3
"""
Script de génération d'images de toitures pour MTech WebSite
Mode 1 (défaut) : Pollinations.ai  — 100% gratuit, aucune clé API, modèle Flux
Mode 2           : Google Gemini    — nécessite un compte avec facturation activée

Usage :
    python generer_toitures.py              # Pollinations.ai (gratuit)
    python generer_toitures.py --gemini     # Google Gemini (facturation requise)
"""

import os
import sys
import time
import urllib.request
import urllib.parse
from pathlib import Path

# Force UTF-8 sur la console Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

OUTPUT_DIR = Path("images_toitures")

# ─── Prompts – 6 styles de toitures québécoises ───────────────────────────────
IMAGES = [
    {
        "slug": "01_bardeaux_asphalte_gris",
        "label": "Bardeaux d'asphalte gris charbon",
        "prompt": (
            "photorealistic professional roofing photography, Quebec residential home, "
            "modern architectural charcoal grey asphalt shingles, brand new roof installation, "
            "bright sunny day, clear blue sky, well-maintained two-story suburban house, "
            "lush green lawn, wide-angle view showing full roof slope, "
            "high-end real estate photography, sharp focus, cinematic lighting"
        ),
    },
    {
        "slug": "02_toit_metal_debout_sur_joint",
        "label": "Toiture métal debout-sur-joint (Standing Seam)",
        "prompt": (
            "photorealistic professional roofing photography, Quebec residential home, "
            "modern standing seam metal roof, dark charcoal steel panels, "
            "vertical seam lines, contemporary architectural design, "
            "autumn Quebec landscape, colorful red and orange maple trees in background, "
            "overcast sky with soft diffused light, luxury home exterior, "
            "sharp metal panel texture detail, commercial photography quality"
        ),
    },
    {
        "slug": "03_bardeau_cedre_traditionnel",
        "label": "Bardeau de cèdre traditionnel",
        "prompt": (
            "photorealistic professional roofing photography, traditional Quebec cottage home, "
            "natural cedar wood shingles roof, weathered silver-grey cedar texture, "
            "rustic country house style, Quebec Laurentians mountains setting, "
            "golden autumn afternoon light, warm tones, dense forest in background, "
            "heritage architecture, artisanal craftsmanship, documentary photography"
        ),
    },
    {
        "slug": "04_toit_plat_membrane_TPO",
        "label": "Toiture plate membrane TPO/EPDM",
        "prompt": (
            "photorealistic professional aerial roofing photography, modern flat roof building Quebec, "
            "white TPO membrane flat roof, rooftop HVAC units, drainage system, "
            "urban Montreal neighborhood, blue sky with scattered clouds, "
            "drone bird eye view perspective looking down at flat commercial roof, "
            "clean modern lines, professional installation, architectural photography"
        ),
    },
    {
        "slug": "05_lucarne_pignon_quebecois",
        "label": "Lucarne et pignon typique québécois",
        "prompt": (
            "photorealistic professional roofing photography, classic Quebec Victorian heritage house, "
            "steep pitched roof with traditional dormers lucarnes, "
            "dark grey asphalt shingles, ornate gable trim details, decorative fascia, "
            "Quebec City old residential neighborhood, early autumn morning golden light, "
            "heritage home restoration, traditional French Canadian architecture, "
            "dramatic sky with light clouds, wide perspective showing full house facade"
        ),
    },
    {
        "slug": "06_renovation_toiture_terminee",
        "label": "Rénovation toiture complétée – résultat professionnel",
        "prompt": (
            "photorealistic professional roofing photography, Quebec suburban home, "
            "brand new roof renovation just completed, fresh charcoal architectural asphalt shingles, "
            "clean ridge cap newly installed, new flashings around brick chimney, "
            "late afternoon golden hour sunlight, immaculate professional roofing company workmanship, "
            "pristine clean gutters, beautiful curb appeal, proud homeowner, vibrant colors"
        ),
    },
]


# ═══════════════════════════════════════════════════════════════════════════════
#  MODE 1 : Pollinations.ai (gratuit, sans clé API)
# ═══════════════════════════════════════════════════════════════════════════════

def generate_pollinations(prompt: str, slug: str, width=1344, height=768) -> Path | None:
    """
    Génère une image via Pollinations.ai (modèle Flux – gratuit, sans clé).
    Retourne le Path du fichier sauvegardé ou None en cas d'erreur.
    """
    seed = abs(hash(slug)) % 99999          # seed déterministe par image
    encoded = urllib.parse.quote(prompt, safe='')
    url = (
        f"https://image.pollinations.ai/prompt/{encoded}"
        f"?width={width}&height={height}&model=flux&seed={seed}&nologo=true"
    )

    filepath = OUTPUT_DIR / f"{slug}.jpg"
    headers  = {"User-Agent": "MTech-RoofGen/1.0"}

    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            if resp.status == 200:
                data = resp.read()
                with open(filepath, "wb") as f:
                    f.write(data)
                return filepath
    except Exception as e:
        raise RuntimeError(f"Pollinations error: {e}")
    return None


def run_pollinations():
    print("Mode : Pollinations.ai (Flux) — 100 % gratuit, sans clé API")
    print(f"Dossier : {OUTPUT_DIR.resolve()}\n")

    generated, errors = [], []

    for idx, item in enumerate(IMAGES, 1):
        print(f"[{idx}/{len(IMAGES)}] {item['label']}")
        print(f"         prompt : {item['prompt'][:75]}...")
        try:
            filepath = generate_pollinations(item["prompt"], item["slug"])
            if filepath:
                size_kb = filepath.stat().st_size // 1024
                print(f"  ✓ Sauvegardé : {filepath.name}  ({size_kb} Ko)\n")
                generated.append({"slug": item["slug"], "label": item["label"],
                                   "filepath": filepath})
            else:
                raise RuntimeError("Aucune image retournée")
        except Exception as e:
            print(f"  ✗ Erreur : {e}\n")
            errors.append(item["slug"])

        if idx < len(IMAGES):
            time.sleep(2)   # politesse envers le serveur gratuit

    return generated, errors


# ═══════════════════════════════════════════════════════════════════════════════
#  MODE 2 : Google Gemini (nécessite facturation activée)
# ═══════════════════════════════════════════════════════════════════════════════

GEMINI_API_KEY = "AIzaSyCRB8DwA9mNZZzcA0Z8d95Am-qDeqyHuKA"
GEMINI_MODEL   = "gemini-3.1-flash-image-preview"   # ou gemini-2.5-flash-image


def run_gemini():
    try:
        from google import genai
        from google.genai import types
    except ImportError:
        print("ERREUR: pip install google-genai")
        sys.exit(1)

    print(f"Mode : Google Gemini ({GEMINI_MODEL})")
    print("AVERTISSEMENT : Ce mode nécessite la facturation activée sur AI Studio.\n")
    print(f"Dossier : {OUTPUT_DIR.resolve()}\n")

    client     = genai.Client(api_key=GEMINI_API_KEY)
    generated, errors = [], []

    for idx, item in enumerate(IMAGES, 1):
        print(f"[{idx}/{len(IMAGES)}] {item['label']}")
        try:
            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=item["prompt"],
                config=types.GenerateContentConfig(
                    response_modalities=["IMAGE", "TEXT"]
                ),
            )
            saved = False
            for part in response.candidates[0].content.parts:
                if part.inline_data is not None:
                    ext = "png" if "png" in part.inline_data.mime_type else "jpg"
                    filepath = OUTPUT_DIR / f"{item['slug']}.{ext}"
                    with open(filepath, "wb") as f:
                        f.write(part.inline_data.data)
                    size_kb = filepath.stat().st_size // 1024
                    print(f"  ✓ {filepath.name}  ({size_kb} Ko)\n")
                    generated.append({"slug": item["slug"], "label": item["label"],
                                      "filepath": filepath})
                    saved = True
                    break
            if not saved:
                raise RuntimeError("Aucune image dans la réponse")
        except Exception as e:
            print(f"  ✗ Erreur : {e}\n")
            errors.append(item["slug"])

        if idx < len(IMAGES):
            print("     (pause 5s — limites API Gemini)...")
            time.sleep(5)

    return generated, errors


# ═══════════════════════════════════════════════════════════════════════════════
#  Génération du fichier galerie.html
# ═══════════════════════════════════════════════════════════════════════════════

def generate_html_gallery(generated: list[dict], mode: str) -> Path:
    cards_html = ""
    for item in generated:
        rel_path = item["filepath"].as_posix()
        cards_html += f"""
        <div class="card">
            <img src="{rel_path}" alt="{item['label']}" loading="lazy">
            <div class="caption">{item['label']}</div>
        </div>"""

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Galerie Toitures – MTech</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            background: #0f1117;
            color: #e8e8e8;
            min-height: 100vh;
        }}
        header {{
            background: linear-gradient(135deg, #1a1f2e 0%, #2d3a4a 100%);
            padding: 40px 20px;
            text-align: center;
            border-bottom: 3px solid #e8a020;
        }}
        header h1 {{
            font-size: 2.2rem;
            font-weight: 700;
            color: #fff;
        }}
        header h1 span {{ color: #e8a020; }}
        header p {{
            margin-top: 10px;
            color: #9aa5b4;
            font-size: 0.95rem;
        }}
        .gallery {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
            gap: 24px;
            padding: 40px;
            max-width: 1400px;
            margin: 0 auto;
        }}
        .card {{
            background: #1a1f2e;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 20px rgba(0,0,0,0.4);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            cursor: pointer;
        }}
        .card:hover {{
            transform: translateY(-6px);
            box-shadow: 0 12px 32px rgba(232,160,32,0.25);
        }}
        .card img {{
            width: 100%;
            height: 240px;
            object-fit: cover;
            display: block;
        }}
        .caption {{
            padding: 14px 16px;
            font-size: 0.9rem;
            font-weight: 500;
            color: #c8d6e5;
            border-top: 2px solid #e8a020;
        }}
        footer {{
            text-align: center;
            padding: 30px;
            color: #4a5568;
            font-size: 0.82rem;
        }}
        #lightbox {{
            display: none;
            position: fixed; inset: 0;
            background: rgba(0,0,0,0.93);
            z-index: 1000;
            align-items: center;
            justify-content: center;
        }}
        #lightbox.active {{ display: flex; }}
        #lightbox img {{ max-width: 92vw; max-height: 90vh; border-radius: 8px; box-shadow: 0 0 60px rgba(232,160,32,0.2); }}
        #lightbox-close {{
            position: fixed; top: 18px; right: 28px;
            font-size: 2.4rem; color: #fff; cursor: pointer;
            line-height: 1; user-select: none; opacity: 0.8;
        }}
        #lightbox-close:hover {{ opacity: 1; color: #e8a020; }}
    </style>
</head>
<body>
<header>
    <h1>Galerie <span>Toitures Québec</span></h1>
    <p>Images générées par IA ({mode}) • {len(generated)} images • {time.strftime('%Y-%m-%d %H:%M')}</p>
</header>

<div class="gallery">{cards_html}
</div>

<footer>MTech WebSite — Images IA de toitures québécoises</footer>

<div id="lightbox">
    <span id="lightbox-close" onclick="closeLightbox()">&#x2715;</span>
    <img id="lightbox-img" src="" alt="">
</div>
<script>
    document.querySelectorAll('.card img').forEach(img => {{
        img.addEventListener('click', () => {{
            document.getElementById('lightbox-img').src = img.src;
            document.getElementById('lightbox').classList.add('active');
        }});
    }});
    function closeLightbox() {{
        document.getElementById('lightbox').classList.remove('active');
    }}
    document.getElementById('lightbox').addEventListener('click', e => {{
        if (e.target === e.currentTarget) closeLightbox();
    }});
    document.addEventListener('keydown', e => {{
        if (e.key === 'Escape') closeLightbox();
    }});
</script>
</body>
</html>
"""
    html_path = Path("galerie.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    return html_path


# ═══════════════════════════════════════════════════════════════════════════════
#  Main
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    use_gemini = "--gemini" in sys.argv

    print("=" * 62)
    print("  Générateur d'images de toitures — MTech WebSite")
    print("=" * 62)
    print()

    OUTPUT_DIR.mkdir(exist_ok=True)

    if use_gemini:
        generated, errors = run_gemini()
        mode_label = f"Google Gemini · {GEMINI_MODEL}"
    else:
        generated, errors = run_pollinations()
        mode_label = "Pollinations.ai · Flux"

    # ─── Rapport ──────────────────────────────────────────────────────────────
    print("=" * 62)
    print(f"  {len(generated)}/{len(IMAGES)} images générées avec succès.")

    if generated:
        html_path = generate_html_gallery(generated, mode_label)
        print(f"  Galerie HTML   : {html_path.resolve()}")
        print(f"  Dossier images : {OUTPUT_DIR.resolve()}")

    if errors:
        print(f"\n  Erreurs ({len(errors)}) : {', '.join(errors)}")

    print("=" * 62)
    if generated:
        print("\n  Ouvrez galerie.html dans votre navigateur pour voir le résultat !")
        print()


if __name__ == "__main__":
    main()
