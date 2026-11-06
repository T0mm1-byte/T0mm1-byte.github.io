#!/usr/bin/env python3
"""Build the site: content/ + templates/ + static/ -> dist/.

Usage: python3 build.py && python3 -m http.server -d dist
"""
import shutil
from collections import Counter
from datetime import date
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from markdown_it import MarkdownIt
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import TextLexer, get_lexer_by_name
from pygments.util import ClassNotFound

ROOT = Path(__file__).parent
DIST = ROOT / "dist"
SITE = yaml.safe_load((ROOT / "site.yml").read_text(encoding="utf-8"))
DIFFICULTIES = ["Very Easy", "Easy", "Medium", "Hard", "Nightmare"]
FORMATTER = HtmlFormatter(nowrap=True)


def highlight_code(code, lang, _attrs):
    try:
        lexer = get_lexer_by_name(lang) if lang else TextLexer()
    except ClassNotFound:
        lexer = TextLexer()
    return highlight(code, lexer, FORMATTER)


MD = MarkdownIt("commonmark", {"html": True, "highlight": highlight_code}).enable(["table", "strikethrough"])


def load_section(section):
    """Read content/<section>/*.md, newest first."""
    pages = []
    for path in (ROOT / "content" / section).glob("*.md"):
        _, head, body = path.read_text(encoding="utf-8").split("---\n", 2)
        page = yaml.safe_load(head)
        page.update(slug=path.stem, section=section, url=f"/{section}/{path.stem}/",
                    html=MD.render(body), date=date.fromisoformat(str(page["date"])))
        pages.append(page)
    return sorted(pages, key=lambda p: (p["date"], p["title"]), reverse=True)


def uart_trace(text, bit=12, high=8, low=38):
    """Draw `text` as its real UART 8N1 waveform (idle high, LSB first) for the home page."""
    x, y, points, labels = 0, high, [(0, high)], []
    x += bit * 2
    points.append((x, high))
    for char in text:
        start = x
        bits = [0] + [(ord(char) >> i) & 1 for i in range(8)] + [1]
        for b in bits:
            level = high if b else low
            if level != y:
                points.append((x, level))
                y = level
            x += bit
            points.append((x, y))
        labels.append((start + bit * 5, char))
        x += bit
        points.append((x, y))
    path = " ".join(f"{px},{py}" for px, py in points)
    return {"width": x + bit * 2, "path": path, "labels": labels}


def code_css():
    """Syntax colors for both color schemes."""
    light = HtmlFormatter(style="xcode").get_style_defs(".prose pre code")
    dark = HtmlFormatter(style="github-dark").get_style_defs(".prose pre code")
    return f"@media (prefers-color-scheme: light) {{\n{light}\n}}\n@media (prefers-color-scheme: dark) {{\n{dark}\n}}\n"


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(ROOT / "static", DIST)
    (DIST / "css" / "code.css").write_text(code_css(), encoding="utf-8")

    env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=True,
                      undefined=StrictUndefined, trim_blocks=True, lstrip_blocks=True)
    env.globals.update(site=SITE)

    def render(template, out, **ctx):
        target = DIST / out
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(env.get_template(template).render(**ctx), encoding="utf-8")

    projects, challenges, writeups = map(load_section, ("projects", "challenges", "writeups"))

    types = [t for t, _ in Counter(p["type"] for p in writeups).most_common()]
    used = {p["difficulty"] for p in writeups}
    about = MD.render((ROOT / "content" / "about.md").read_text(encoding="utf-8"))
    render("home.html", "index.html", nav="home", about=about, trace=uart_trace(SITE["handle"]))
    render("projects.html", "projects/index.html", nav="projects", title="Projects", pages=projects)
    render("challenges.html", "challenges/index.html", nav="challenges", title="Challenges", pages=challenges)
    render("writeups.html", "writeups/index.html", nav="writeups", title="Writeups", pages=writeups,
           types=types, difficulties=[d for d in DIFFICULTIES if d in used])
    for page in projects + challenges + writeups:
        render("page.html", f"{page['section']}/{page['slug']}/index.html",
               nav=page["section"], title=page["title"], page=page)
    render("404.html", "404.html", nav="", title="Not found")
    print(f"Built {len(projects)} projects, {len(challenges)} challenges, {len(writeups)} writeups in {DIST}")


if __name__ == "__main__":
    main()
