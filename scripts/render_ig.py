#!/usr/bin/env python3
"""Render IG carousel images (1:1, 1080x1080) from the chirpy-blog-seo-aeo skill.

Slide 1 is a cover; slides 2..N each carry one highlight ("pt" layout).

Usage:
  render_ig.py --slug tds-das \
      --title "東京迪士尼海洋 __DAS 無障礙實測__" \
      --series "親子旅遊" --subtitle "迪士尼海洋25週年" \
      --bg /path/to/bg.jpg \
      --slide "DAS 註冊只要 5 步|身障手冊＋官方 APP 就能預約快速通關" \
      --slide "一天玩 5 個設施|夢幻奇航、冰雪之旅、樂佩、小飛俠、玩具總動員" \
      --out-dir ~/Desktop/agent/ig-posts/

Automated H2 mode: 先讀文章，把它轉成輪播圖重點（第 1 張為封面）。
"""
import argparse
import pathlib
import re
import sys
import tempfile

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("缺少 playwright: pip install playwright && playwright install chromium")

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
TEMPLATE = SCRIPT_DIR.parent / "templates" / "ig-carousel-template.html"


def render_html(base_html: str, replaces: dict, hide_cover: bool, out: pathlib.Path):
    html = base_html
    for k, v in replaces.items():
        html = html.replace(k, v)
    if hide_cover:
        # 遮住封面版面、露出重點版面
        html = html.replace(
            "<div class=\"content-cover\">",
            "<div class=\"content-cover\" style=\"display:none\">",
            1,
        )
        html = html.replace(
            "<div style=\"display:none\">",
            "<div>",
            1,
        )
    with tempfile.NamedTemporaryFile("w", suffix=".html", encoding="utf-8", delete=False) as f:
        f.write(html)
        tmp_path = f.name
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={"width": 1080, "height": 1080})
        page.goto(f"file://{tmp_path}")
        page.wait_for_timeout(150)
        page.screenshot(path=str(out))
        browser.close()
    pathlib.Path(tmp_path).unlink(missing_ok=True)
    print(f"OK {out.name}")


def resolve_bg(bg: str) -> str:
    p = pathlib.Path(bg).expanduser().resolve()
    if not p.exists():
        sys.exit(f"背景圖不存在: {p}")
    return f"file://{p}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True, help="檔案前綴，例如 tds-das")
    ap.add_argument("--title", required=True, help="封面主標題，__文字__ 會被強調成橘色")
    ap.add_argument("--series", default="親子旅遊", help="封面系列徽章")
    ap.add_argument("--subtitle", default="", help="封面次要標籤")
    ap.add_argument("--bg", default="", help="封面背景圖（無則純色底）")
    ap.add_argument("--slide", action="append", default=[], help='重點標題，格式 "標題|說明"')
    ap.add_argument("--out-dir", required=True, help="輸出資料夾，例如 ~/Desktop/agent/ig-posts/")
    args = ap.parse_args()

    if not args.slide:
        sys.exit("至少要一個 --slide（第 2 張以後的重點）")

    base = TEMPLATE.read_text(encoding="utf-8")
    bg_url = resolve_bg(args.bg) if args.bg else ""
    title_html = re.sub(r"__(.+?)__", r'<span class="hl">\1</span>', args.title)
    series_html = " ".join(args.series)  # 逐字間隔，避免壓版

    # 第 1 張：封面
    cover = {
        "__TITLE__": title_html,
        "__SERIES__": series_html,
        "__SUBTITLE__": args.subtitle,
        "__PT_TAG__": "", "__PT_TITLE__": "", "__PT_NOTE__": "", "__PT_COUNT__": "",
    }
    html = base.replace("__BG__", bg_url)
    out_dir = pathlib.Path(args.out_dir).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    render_html(html, cover, hide_cover=False, out=out_dir / f"{args.slug}-01-cover.png")

    # 第 2~N 張：重點
    total = len(args.slide) + 1
    for i, s in enumerate(args.slide, start=2):
        if "|" in s:
            pt_title, pt_note = s.split("|", 1)
        else:
            pt_title, pt_note = s, ""
        pt_title = re.sub(r"__(.+?)__", r'<span class="hl">\1</span>', pt_title.strip())
        pt = {
            "__BG__": "",
            "__TITLE__": "",
            "__SERIES__": "",
            "__SUBTITLE__": "",
            "__PT_TAG__": f"重點 {i-1}/{total-1}",
            "__PT_TITLE__": pt_title,
            "__PT_NOTE__": pt_note,
            "__PT_COUNT__": f"{i:02d}",
        }
        render_html(base, pt, hide_cover=True, out=out_dir / f"{args.slug}-{i:02d}.png")

    print(f"完成：共 {total} 張，輸出在 {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())