"""Build the GitHub Pages copy of the game.

Wraps baloot.html (the claude.ai page) in a full HTML document, adds the
Firebase settings from firebase-config.json so playing with friends works
outside claude.ai, and writes index.html (the file uploaded to GitHub).

    python3 build_site.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
page = (ROOT / "baloot.html").read_text(encoding="utf-8")
config = json.loads((ROOT / "firebase-config.json").read_text(encoding="utf-8"))

head = (
    "<!doctype html>\n"
    '<html lang="ar">\n<head>\n'
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
    '<meta name="theme-color" content="#0c1412">\n'
    "<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}"
    "body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>\n"
    f"<script>window.FIREBASE_CONFIG={json.dumps(config, ensure_ascii=False)};</script>\n"
    "</head>\n<body>\n"
)
out = ROOT / "index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(head + page + "\n</body>\n</html>\n", encoding="utf-8")
print(f"wrote {out.relative_to(ROOT)} ({out.stat().st_size // 1024} KB)")
