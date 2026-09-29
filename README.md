# homedad-blog-skill

「充滿意外的宅爸人生」（[vanix.github.io](https://vanix.github.io)）部落格內容自動化 skill：用一個工作流，同時產出 **SEO/AEO 部落格文章、YouTube 精華 GIF、文章封面圖、IG 貼文文案與 1080x1080 輪播圖**。

> 用於 [opencode](https://opencode.ai)（OpenAI Code 的開源 CLI），作為 skill 載入使用。

## 功能

- 📝 **部落格文章**：繁體中文 SEO + AEO（AI 答案引擎）優化，依 Chirpy front matter 規範輸出到 `~/Desktop/agent/blog/`
- 🎬 **YouTube 轉文章**：自動抓說明欄＋中文字幕當素材，選 6+ 個精彩片段用 ffmpeg 轉成 GIF 插入文章
- 🖼️ **文章封面**：Playwright 渲染品牌風 1200x630 封面，自動更新 front matter `image` 欄位
- 📱 **IG 貼文**：從文章 H2 重點自動產出 IG 文案 + 多張 1080x1080 輪播圖

## 目錄結構

```
homedad-blog-skill/
├── SKILL.md              # opencode skill 主文件（工作流程與規範）
├── templates/
│   ├── cover-template.html      # 部落格封面模板（1200x630）
│   └── ig-carousel-template.html# IG 輪播模板（1080x1080）
└── scripts/
    ├── render_cover.py          # Playwright 封面渲染腳本
    └── render_ig.py             # Playwright IG 輪播渲染腳本
```

## 使用方式

### 1. 安裝 skill（opencode）

將整個 repo 複製到 opencode skills 目錄：

```bash
git clone https://github.com/vanix/homedad-blog-skill.git
cp -R homedad-blog-skill ~/.config/opencode/skills/chirpy-blog-seo-aeo
```

或直接在 `opencode.json` 宣告為外部 skill 來源。

### 2. 前置工具

```bash
# Playwright（封面/IG 圖片渲染）
pip install playwright
python3 -m playwright install chromium

# YouTube 素材（字幕抓取、影片下載）
pip install -U yt-dlp

# GIF/抽幀
brew install ffmpeg
```

### 3. 說一句話就開工

對 opencode 說例如「把這支 YouTube 影片寫成文章」或「寫一篇部落格文章＋IG 貼文」，skill 就會自動完成整條產出流程。

## 產出位置

| 產物 | 路徑 |
|:---|:---|
| 部落格文章草稿 | `~/Desktop/agent/blog/YYYY-MM-slug.md` |
| 文章封面圖 | `~/Desktop/agent/blog/assets/images/cover/<slug>.png` |
| 文章內圖片/GIF | `~/Desktop/agent/blog/assets/images/blog/<主題>/` |
| IG 文案＋輪播圖 | `~/Desktop/agent/ig-posts/<slug>-ig.md`、`<slug>-NN.png` |

## License

MIT