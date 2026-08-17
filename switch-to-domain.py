#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OLD = "https://erezoren.github.io/A-T-SOLUTIONS/"
NEW = "https://attacticalsolutions.com/"

for name in ["index.html", "who-we-are.html", "programs.html", "robots.txt", "sitemap.xml"]:
    path = ROOT / name
    text = path.read_text(encoding="utf-8")
    path.write_text(text.replace(OLD, NEW), encoding="utf-8")

ready = ROOT / "CNAME.ready"
cname = ROOT / "CNAME"
if ready.exists():
    cname.write_text(ready.read_text(encoding="utf-8"), encoding="utf-8")
    ready.unlink()

print("Switched canonical, Open Graph, structured-data, robots and sitemap URLs to", NEW)
print("Activated CNAME for attacticalsolutions.com")
