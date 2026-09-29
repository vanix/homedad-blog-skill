#!/usr/bin/env python3
"""Render a 1200x630 blog cover PNG from the chirpy-blog-seo-aeo cover template.

Usage:
  render_cover.py --title "文章標題" --bg /path/to/background.jpg \
      [--series "旅遊親子系列"] [--subtitle "東京迪士尼 DAS"] \
      [--date "2026-09"] [--out /path/to/cover.png]

Requirements: playwright (pip), chromium installed. Fonts fall back to
PingFang TC / Hiragino Sans GB available on macOS.
"""
import argparse
import pathlib
import sys
import tempfile

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("缺少 playwright: pip install playwright && playwright install chromium")

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
TEMPLATE = SCRIPT_DIR.parent / "templates" / "cover-template.html"


def resolve_bg(bg: str) -> str:
    """Return a value usable inside CSS url(...)."""
    p = pathlib.Path(bg).expanduser().resolve()
    if not p.exists():
        sys.exit(f"背景圖不存在: {p}")
    return f"file://{p}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", required=True, help="封面主標題（可用 _ 分隔要強調的詞）")
    ap.add_argument("--bg", default="", help="背景圖路徑（影片關鍵幀）；省略則純色底")
    ap.add_argument("--series", default="親子旅遊", help="左上系列徽章字樣")
    ap.add_argument("--subtitle", default="", help="系列徽章旁的次要標籤")
    ap.add_argument("--date", default="", help="底部日期文字，如 2026.09")
    ap.add_argument("--out", required=True, help="輸出 PNG 路徑")
    args = ap.parse_args()

    # 支援語法：__要強調__ 包住想用橘色強調的文字
    import re
    title_html = re.sub(r"__(.+?)__", r'<span class="hl">\1</span>', args.title)

    html = TEMPLATE.read_text(encoding="utf-8")
    html = html.replace("__TITLE__", title_html)
    html = html.replace("__SERIES__", args.series)
    html = html.replace("__SUBTITLE__", args.subtitle)
    html = html.replace("__DATE__", args.date)
    html = html.replace("__BG__", resolve_bg(args.bg) if args.bg else "")

    with tempfile.NamedTemporaryFile("w", suffix=".html", encoding="utf-8", delete=False) as f:
        f.write(html)
        tmp_path = f.name

    out = pathlib.Path(args.out).expanduser().resolve()
    out.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={"width": 1200, "height": 630})
        page.goto(f"file://{tmp_path}")
        page.wait_for_timeout(150)
        page.screenshot(path=str(out))
        browser.close()

    pathlib.Path(tmp_path).unlink(missing_ok=True)
    print(f"OK 封面已產生: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())