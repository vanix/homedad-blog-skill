---
name: chirpy-blog-seo-aeo
description: 為 宅爸 的 Chirpy GitHub Pages 部落格（vanix.github.io / 充滿意外的宅爸人生）撰寫具 SEO 與 AEO（Answer Engine Optimization）優化的繁體中文文章。當使用者說「寫一篇部落格文章、幫我寫 blog post、寫 SEO 文章、寫 AEO 文章、新增 _posts 文章、宅爸部落格文章、把 YouTube 影片寫成文章、YT 影片轉文章、製作/產生部落格封面、封面圖、IG 貼文、IG 輪播、IG 卡圖、社群貼文」時使用。產出文章會放入 `~/Desktop/agent/blog/YYYY-MM-slug.md`（草稿區），並遵循 Chirpy front matter、既有分類/標籤與台灣繁體中文風格。支援四種增強功能：(1) 使用者給主題/PDF/截圖；(2) 使用者給 YouTube 網址，自動抓說明欄與中文字幕當素材，並把至少 6 個精彩片段轉成 GIF 當圖片；(3) 用 skill 目錄內的 Playwright 封面模板/腳本自動產生 1200x630 文章封面圖並更新 front matter 的 image 欄位；(4) 用 skill 目錄內的 IG 模板/腳本產生 1080x1080 多張輪播圖與 IG 貼文文案到 ~/Desktop/agent/ig-posts/。
---

# Chirpy Blog SEO/AEO 文章寫作技能

為「充滿意外的宅爸人生」（https://vanix.github.io）撰寫繁體中文技術部落格文章，同時最佳化**傳統搜尋引擎 SEO** 與 **AI 答案引擎 AEO**（ChatGPT Search / Perplexity / Google AI Overviews / Claude 引用）。

## 部落格背景（已確認）

- **主題/模板**：Jekyll + `jekyll-theme-chirpy`，標題「充滿意外的宅爸人生」，tagline「宅爸的程式教學、資訊分享與生活筆記」
- **作者**：宅爸（`social.name: homedad`），高職資訊科老師，內容包含：程式教學（計概、Python、APCS、證照丙級）、AI Agent 實作（OpenClaw、opencode、Palmier、RAG、n8n）、樹莓派、旅遊親子、生活紀錄
- **SEO 基礎設施已就緒**（不要動）：`robots.txt` 已放行 AI 搜尋爬蟲並封鎖訓練爬蟲、`_includes/ai-seo-meta.html` 已輸出 BlogPosting JSON-LD、GA4 + AdSense + Google 驗證已設定
- **已知可改進但非本次任務**：`_config.yml` 的 `lang: en`（內容為繁中，建議改 `zh-TW`）；若使用者要求才處理，不動為原則

## 前置工作（動手寫之前一定要做）

1. **確認工作目錄**：文章一律寫入草稿區 `~/Desktop/agent/blog/`（該目錄已存在，文章放根目錄、檔名 `YYYY-MM-slug.md`，使用者之後會自行上傳到部落格）。**不需要 clone repo，也不要對任何 git repo 做操作。**
2. **確認封面工具**：封面圖靠 skill 內的 Playwright 腳本，若使用報錯（缺 chromium），先安裝：`python3 -m playwright install chromium`
3. **讀取必要的既有資料**（保持一致性）：
   - 直接讀取 `~/Desktop/agent/blog/` 中 3～5 篇既有草稿（學習語氣、結構、front matter 寫法）
   - 若要更貼近部落格現況，可（唯讀）查看 https://github.com/vanix/vanix.github.io 的 `_config.yml` 與 `_posts/`；不 clone、不修改遠端
   - 沿用既有分類與標籤（taxonomies），不要隨意發明
3. **研究目標關鍵字**：若要，可用 websearch 確認熱門提問角度與長尾關鍵字（繁體中文為主）。

## 檔案命名與位置

- 檔案：`~/Desktop/agent/blog/YYYY-MM-slug.md`（放在目錄**根層**，不是 `_posts/`，與既有草稿一致；若無法確定月份，用目前年月）
- slug：英文 kebab-case（如 `2026-09-rag-guide.md`），與既有草稿一致；盡量含主要關鍵字
- **date（front matter 內的發布日期）**：填你預期發布的完整日期，台灣時間（`+0800`）
- **permalink**：沿用部落格主流格式 `/<year>/<month>/<slug>.html`，年月與 `date` 一致（注意：實際部落格 _config.yml 預設是 `/posts/:title/`，但 139 篇中有 136 篇使用 `/YYYY/MM/slug.html`，以多數慣例為準）

## Chirpy Front Matter 範本

```yaml
---
author: 宅爸
date: YYYY-MM-DD HH:MM:SS +0800
layout: post
permalink: /YYYY/MM/slug.html
title: 主要關鍵字放在前面｜補充說明讓標題完整（約 55～70 字）
description: 這個欄位很重要：150～300 字的摘要，包含關鍵字，同時作為 meta description 與 JSON-LD 描述
categories: [教學, AI應用]          # 沿用既有：教學 / AI應用 / n8n / openclaw / APCS升學 / 證照 / 軟體工具 / 電玩 / 旅遊 / 親子…
tags: [標籤1, 標籤2, ...]          # 與既有文章一致的標籤，中英混用可，避免過度堆疊（控制在 5～10 個）
---
```

說明：
- `layout: post` 是 Chirpy 預設，可不寫，但部落格慣例有寫，保留一致
- 有封面圖才加 `image: /assets/images/...`（1200x630，建議放 `assets/images/cover/` 或 `assets/images/blog/`；front matter 內請用 `image:` + alt 描述）
- **每篇都必須有 `description`**（這是目前部落格最大的 SEO 缺口，139 篇只有 2 篇有）

## SEO 規範（傳統搜尋引擎）

1. **Title（標題）**：主要關鍵字放最前面；完整、含誘因（ex：教／步驟／比較／懶人包／心得）；繁中標題 55～70 字元以內；不要與 H1 重複（Chirpy 中 title 就是 H1）
2. **Meta description**：150～300 字（因 JSON-LD 會 truncate 160 但保留自訂），含關鍵字、給出「看了能得到什麼」
3. **URL/slug**：短、有意義、含關鍵字、用連字號（`-`），不加日期（日期已在檔案名）
4. **關鍵字佈局**：
   - 標題、第一個自然段（前 100 字內）、至少一個 H2、圖片 alt、檔案名中各出現一次主要關鍵字
   - 每段只講一件事，段落短（3～5 行以內）
5. **標題階層**：只有一個 H1（= title）；H2 為主要章節；H3 為小節；層級不要跳階
6. **內容結構**：多使用表格、編號步驟、條列、程式碼塊（這些都容易被擷取為精選摘要）
7. **內部連結**：自然連結到部落格既有相關文章（用 `https://vanix.github.io/posts/<slug>/` 或既有 permalink；先確認連結真的存在）
8. **圖片**：alt 描述性文字（含關鍵字）、自訂檔名具描述性
9. **不要**：關鍵字堆疊、無意義長句、未確認的連結、重複內容

## AEO 規範（AI 答案引擎）

AI 答案引擎（ChatGPT Search、Perplexity、Google AI Overviews）會直接從文章抽取答案並標註來源，重點：

1. **開頭就先給答案**：第一段（100～150 字內）用一句話直接回答核心問題，再解釋。不要鋪陳、不要講古
2. **問題式小標**：H2/H3 用使用者真的會問的問法。「什麼是 X？」「X 和 Y 差在哪？」「怎麼安裝 X？」「X 要多少錢／多久？」
3. **可以直接被引用的句子**：每個小節最好有一句完整的、可獨立理解的總結句（通常用 **粗體** 標示），這樣 AI 引用時可以直接抽出
4. **句型為 Q&A**：先問後答、直接、肯定語氣
5. **多用清單與表格**：步驟清單、比較表格、FAQ 區塊（AEO 與精選摘要最愛）
6. **定義名詞**：出現專有名詞時用一兩句定義（AI 引用時常需要完整定義）
7. **FAQ 區塊**：文末可加「常見問題（FAQ）」H2 區塊，收 3～5 個長尾問題
8. **可被驗證**：提到的數據、版本、日期要具體，不要模糊

## 語氣與風格（宅爸 persona）

- 繁體中文（台灣用語），友善、像老師跟學生聊天、偶爾詼諧自嘲（「學校馴獸師」）
- 用生活化比喻講技術（既有文章用「圖書館通才管理員」解釋 RAG）
- 可用 **粗體** 強調重點；可適度用 emoji（參考既有文章：👉、📊、📦 等），但不濫用
- 少用贅詞，直接、具體
- 結尾給下一步、相關文章連結或 GitHub repo 連結

## 寫作工作流程

1. 確認素材來源：使用者給主題／PDF／截圖，或是 YouTube 網址（用下方「YouTube 轉文章工作流程」）
2. 做前置工作（讀 `~/Desktop/agent/blog/` 既有草稿、看 taxonomies）
3. 規劃並回報：標題、description、slug/permalink、categories、tags、文章大綱（H2 結構）
4. 寫成完整 Markdown，放入 `~/Desktop/agent/blog/YYYY-MM-slug.md`（front matter 依範本，**不做任何 git 操作**）
5. 產生封面圖（見「封面圖片製作」章節），更新 front matter 的 `image` 欄位
6. 若使用者要 IG 曝光，自動產出 IG 貼文文案與輪播圖（見「IG 貼文 + 輪播圖製作」章節）
7. 逐項檢查下方清單，並回報通過結果
8. 完成後告知使用者文章路徑；**由使用者自行上傳到部落格，不要 commit/push**

## 封面圖片製作（所有文章通用）

每一篇文章都應該有封面圖（1200x630），提升 SEO/OG 分享與列表點擊率。使用在 skill 資料夾內的封面上模板與 Playwright 渲染腳本。

### 產出位置與 front matter 寫法

- 封面圖統一放 `~/Desktop/agent/blog/assets/images/cover/<slug>.png`
- front matter 加入（Chirpy 格式，`path` 必填、`alt` 建議）：
  ```yaml
  image:
    path: /assets/images/cover/<slug>.png
    alt: <描述性文字，含主要關鍵字>
  ```

### 渲染腳本

```bash
python3 ~/.config/opencode/skills/chirpy-blog-seo-aeo/scripts/render_cover.py \
  --title "文章標題（支援 __要強調__ 包住想用橘色強調的文字）" \
  --bg <背景圖路徑> \
  --series "系列徽章，預設 親子旅遊" \
  --subtitle "次要標籤" \
  --date "2026.09" \
  --out ~/Desktop/agent/blog/assets/images/cover/<slug>.png
```

### 背景圖來源（依優先順序）

1. **YouTube 文章**：挑一支高解析度影片畫面（`yt-dlp --download-sections '*MM:SS-MM:SS'` 抓片段，ffmpeg 抽幀，來源 1920x1080 為佳），裁成 1200x630。夜間燈光秀、熱鬧場景、值得留念的畫面最適合當封面
2. **有截圖/照片**：直接用使用者提供的清晰圖片
3. **純色/漸層**：省略 `--bg`，模板自動用深藍色底

### 注意事項

- 背景圖若要裁切 1200x630，用 ffmpeg：`scale=1200:630:force_original_aspect_ratio=increase,crop=1200:630`，避免變形
- 標題當中的 `__文字__` 會被渲染成橘色強調（瀏覽網頁時無法驗證，可請使用者開圖確認版面）
- 封面檔名與 slug 一致，上傳時連同 `assets/images/cover/` 一起放進 repo
- 此功能我（模型）無法直接看渲染結果，**產出後請提醒使用者開圖確認**才不會有版面問題

## IG 貼文 + 輪播圖製作（YouTube 與一般文章皆適用）

文章完成後，可同時產出 **IG 貼文文案** 與 **多張正方形輪播圖**（1:1，1080x1080），第 1 張是封面、接下來每張放一個重點，把整篇文章拆成「滑得完」的精華。輸出統一放 `~/Desktop/agent/ig-posts/`。

### 產出檔案

- `~/Desktop/agent/ig-posts/<slug>-ig.md`：IG 貼文文案（參考既有 `ig-post-*` 草稿風格：開頭掛鉤→故事→重點條列→限動/連結→hashtag）
- `~/Desktop/agent/ig-posts/<slug>-01-cover.png`：封面（1080x1080）
- `~/Desktop/agent/ig-posts/<slug>-02.png`、`-03.png`…：逐張重點，共 N 張

### 渲染腳本（輪播圖）

```bash
python3 ~/.config/opencode/skills/chirpy-blog-seo-aeo/scripts/render_ig.py \
  --slug tds-das \
  --title "東京迪士尼海洋 __DAS 無障礙實測__｜身障手冊、輪椅專屬區一次看懂" \
  --series "親子旅遊" \
  --subtitle "迪士尼海洋25週年" \
  --bg <方形背景圖路徑> \
  --slide "DAS 是什麼？|身障手冊遊客專用免費快速通關，最高帶 5 位親友" \
  --slide "註冊只要 5 步|入園找工作人員＋官方APP集中門票" \
  ... \
  --out-dir ~/Desktop/agent/ig-posts/
```

- `--slide "標題|說明"`：標題會顯示成大標，說明顯示成副標；每多一個 `--slide` 就多一張圖（不支援省略說明，可只給 `--slide "標題"`）
- `--title` 內用 `__文字__` 包住要橘色強調的詞
- 背景圖來源同「封面圖片製作」原則；**方形 1080x1080** 用 ffmpeg：`scale=1080:1080:force_original_aspect_ratio=increase,crop=1080:1080`

### 自動流程（寫完文章後照做）

1. 從文章挑 **3~6 個 H2 重點**，每個改寫成短標題＋一句說明（IG 使用者不看長文）
2. 產生輪播圖（上列指令）
3. 同時寫 `~/Desktop/agent/ig-posts/<slug>-ig.md` 文案，模仿 `ig-post-robot-arm-tutorial.md` 的語氣與結構
4. **回報時明確列出**：輪播圖張數、各張重點、IG 文案檔案路徑

### 注意事項

- IG 圖上的文字要**短而有力**（標題 ≤ 20 字、說明 ≤ 30 字），不要把部落格段落整段貼上去
- 封面張用有吸引力的背景；重點張建議純色底（腳本預設深藍），字才讀得清楚
- 金句型重點（如「里程當飲料點數」「DAS 註冊只要 5 步」）特別適合 IG，優先選
- 我（模型）無法驗證渲染版面，產出後提醒使用者開圖確認
- IG 文案 hashtag 用 台灣繁體搜得到的（#東京迪士尼 #DAS #親子旅遊 #無障礙 等），10~20 個

## YouTube 轉文章工作流程

當使用者提供 YouTube 網址時，流程如下：

1. **前置確認**：確認 `yt-dlp` 與 `ffmpeg` 已安裝（本機已裝：`/Users/vanix/miniconda3/bin/yt-dlp`、`/opt/homebrew/opt/ffmpeg@6/bin/ffmpeg`）
2. **抓說明欄全文**：
   ```bash
   mkdir -p ~/Desktop/agent/yt_tmp && cd ~/Desktop/agent/yt_tmp
   yt-dlp --skip-download --write-description --write-info-json -o '%(id)s' '<YT_URL>'
   ```
   讀取 `*.description` 檔（含章節時間軸、相關連結、完整介紹）。
3. **抓中文字幕**（優先找 CC 字幕，找不到再找自動字幕）：
   ```bash
   yt-dlp --skip-download --sub-langs 'zh.*,zh-Hans,zh-Hant,zh-TW,zh-CN' --write-subs --write-auto-subs --sub-format vtt -o '%(id)s' '<YT_URL>'
   ```
   先跑 `yt-dlp --list-subs '<YT_URL>'` 看有哪些字幕語言可選。字幕（`.vtt`）需轉成純文字：`ffmpeg -i '<id>.zh*.vtt' '<id>.srt'` 或直接抽取文字行（忽略時間碼與 webvtt 標記）。
   - **若影片沒有中文字幕**：改用本機語音轉文字（whisper 需另行確認是否安裝），或請使用者提供逐字稿／改用說明欄撰寫，並明確告知使用者。
4. **挑 6 個以上精彩片段，畫面轉成 GIF**：
   - 下載低解析度影片供截圖用（不留高畫質省空間）：
     ```bash
     yt-dlp -f 'best[height<=720]/best' -o 'video.mp4' '<YT_URL>'
     ```
   - 依據字幕／說明欄選出 6 個以上「精彩片段」（笑點、重點講解、示範畫面、結論金句），用 ffmpeg 截取約 2～4 秒轉 GIF（palette 法避免色塊、fps 10、寬 480）：
     ```bash
     ffmpeg -ss <START> -t <DURATION> -i video.mp4 -vf "fps=10,scale=480:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 'assets/images/blog/<主題>/<kebab-case>-clip.gif'
     ```
   - GIF 檔名用描述性 kebab-case（如 `step-solve-phone-around-miles.png` 風格）；gif 本身具描述性即可，不用 `.png`
   - GIF 張數至少 6 張；張數不足就補到精彩片段為主，不要為湊數塞重複畫面
5. **撰寫文章**：以上下結構 ==正文==（說明欄＋字幕整理）為素材，套用「Chirpy Front Matter 範本」與 SEO/AEO 規範（大綱讓使用者確認後再寫）
6. **插入 GIF**：文章中對應小節插入 `![描述性 alt（含關鍵字）](/assets/images/blog/主題/xxx.gif)`，alt 用該片段場景描述；可在 GIF 後加 Chirpy caption（`_說明_` 斜體行）。**此步驟不改動文章既有文字內容**
7. **清理暫存**：完成後把 `~/Desktop/agent/yt_tmp/` 的影片檔案刪除，只保留 GIF（已複製進文章 assets 資料夾）與草稿

### 注意事項（YouTube 流程）

- 字幕若為簡中（zh-Hans），寫文章時轉成台灣繁中使用語與用詞
- GIF 檔案不要太大：每張控制在 1～3MB 內（縮小 fps／解析度／秒數），避免拖慢部落格
- 若使用者指定要幾張 GIF、每秒幾畫格、或只要特定片段，以使用者指示為準
- 不直接下載整支高畫質影片：以 `best[height<=720]` 為上限，省空間與時間
- 協助話術：明確告知使用者 GIF 已產生、放哪、可自行調整秒數/解析度

## 完成前驗證檢查清單

- [ ] 檔案存在於 `~/Desktop/agent/blog/YYYY-MM-slug.md`（根目錄），front matter 完整且 YAML 語法正確
- [ ] 有 `description`（150～300 字，含主要關鍵字）
- [ ] 標題含主要關鍵字且置前、不超過 70 字元
- [ ] 開頭段落直接給出答案（不超過 150 字）
- [ ] 主要關鍵字出現在：title、開頭段、至少一個 H2
- [ ] H2/H3 有用問題式問句（AEO），且階層正確
- [ ] 至少含一個表格或編號清單
- [ ] 有 FAQ 或比較性區塊（若適合主題）
- [ ] categories/tags 沿用既有 taxonomies
- [ ] 有內部連結連到既有相關文章（並確認連結有效）
- [ ] 文長適中：教學／指南類約 1500～4000 字，心得類 800～2000 字
- [ ] 語氣符合宅爸 persona（繁體中文、友善、具體）
- [ ] （YouTube 來源）有抓說明欄全文與中文字幕，並在回報中標示素材來源
- [ ] （YouTube 來源）至少插入 6 個 GIF，每個 GIF 檔案存在且 < 3MB，alt 具描述性
- [ ] 有封面圖 `assets/images/cover/<slug>.png`（1200x630），且 front matter 有 `image.path`（+ `image.alt`）
- [ ] （IG 需要）`ig-posts/<slug>-ig.md` 文案存在、輪播圖 3~6 張皆 1080x1080、每張重點文字簡短

## 注意事項

- 不要改動 `_config.yml`、`_includes/`、`robots.txt`、既有文章，除非使用者明確要求
- 寫入路徑一律是 `~/Desktop/agent/blog/`，**不執行任何 git 操作**（不 clone、不 commit、不 push），使用者會自行上傳部落格
- YouTube 流程的暫存影片與檔案放在 `~/Desktop/agent/yt_tmp/`（用完即刪），GIF 輸出到 `~/Desktop/agent/blog/assets/images/blog/<主題>/`