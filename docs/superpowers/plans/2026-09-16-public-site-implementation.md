# ClimbClip Public Site Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** GitHub Pages で公開できる ClimbClip の日本語ホームページ、プライバシーポリシー、利用規約を静的 HTML/CSS で提供する。

**Architecture:** JavaScript やビルド工程を持たない静的サイトとし、3 ページで共通のヘッダー、ナビゲーション、フッターを持たせる。Google Drive 連携については `drive.file` + Google Picker API を前提とし、実機解析・診断ログの保存目的と、ユーザーが明示的に許可した範囲のみを利用する旨を記載する。

**Tech Stack:** HTML5, CSS3, GitHub Pages

**Spec:** `docs/superpowers/specs/2026-09-16-public-site-design.md`

## Global Constraints

- 日本語のみ。
- JavaScript を使用しない。
- 外部 CDN / Web フォントを使用しない。
- OS 標準フォントを使用する。
- Cookie / アクセス解析を導入しない。
- 問い合わせ先は `kaynos.gm@gmail.com`。
- Google Drive OAuth scope は `https://www.googleapis.com/auth/drive.file` を前提とする。
- Google Picker API によりユーザーが許可する対象を選択する前提とする。
- 公開 URL は GitHub Pages Project Site の相対パスで壊れないよう、内部リンクと CSS 参照は相対 URL を使用する。
- 独自ドメイン、GitHub Actions デプロイ、多言語化は実装しない。

---

### Task 1: 静的サイトの共通スタイルと公開設定

**Files:**
- Create: `style.css`
- Create: `.nojekyll`

**Interfaces:**
- Produces: 3 ページが共通利用する CSS クラスと GitHub Pages の静的配信設定。

- [ ] **Step 1: 共通スタイルを実装する**

`style.css` に、OS 標準フォント、最大幅 880px、レスポンシブ余白、共通ヘッダー、ナビゲーション、本文、注意書き、フッター、モバイル対応を定義する。色は高コントラストの白背景・濃色文字を基調とし、リンクとフォーカス状態を視認できるようにする。

- [ ] **Step 2: GitHub Pages 用 `.nojekyll` を追加する**

空ファイル `.nojekyll` を作成し、Jekyll 処理を介さず静的ファイルを配信できるようにする。

- [ ] **Step 3: 構文を確認する**

CSS の括弧対応と不正な絶対 `/` パスがないことを目視確認する。

- [ ] **Step 4: コミットする**

```bash
git add style.css .nojekyll
git commit -m "feat: add static site foundation"
```

### Task 2: ホームページを実装する

**Files:**
- Create: `index.html`

**Interfaces:**
- Consumes: `style.css`
- Produces: Google OAuth のホームページ URL として利用できる ClimbClip の公開説明ページ。

- [ ] **Step 1: 必須内容を満たす HTML を作成する**

`index.html` に以下を含める。

- `<html lang="ja">`
- `ClimbClip` の名称と概要
- Android 向けボルダリング動画撮影・解析アプリである説明
- Google Drive 連携は実機解析・診断ログの保存目的である説明
- Google Drive 連携はユーザー操作により許可された範囲で行う旨
- `privacy.html` と `terms.html` への明示的なリンク
- `mailto:kaynos.gm@gmail.com` の問い合わせ先

- [ ] **Step 2: Project Site の相対 URL を確認する**

CSS は `style.css`、内部リンクは `privacy.html` / `terms.html` のように相対 URL とする。

- [ ] **Step 3: HTML 構造を確認する**

`header`, `nav`, `main`, `section`, `footer` を使用し、見出し階層が `h1` → `h2` の順に破綻していないことを確認する。

- [ ] **Step 4: コミットする**

```bash
git add index.html
git commit -m "feat: add ClimbClip home page"
```

### Task 3: プライバシーポリシーを実装する

**Files:**
- Create: `privacy.html`

**Interfaces:**
- Consumes: `style.css`
- Produces: Google OAuth / Drive 連携のデータ利用を説明する公開プライバシーポリシー。

- [ ] **Step 1: ポリシー本文を作成する**

以下のセクションを含める。

1. 適用範囲
2. 取得・利用する情報
3. Google Drive 連携
4. 利用目的
5. 第三者提供
6. 情報の保存・管理
7. Google Drive へのアクセス権の撤回
8. 外部サービス
9. ポリシーの変更
10. 問い合わせ先

Google Drive については、ClimbClip が `drive.file` 相当の限定権限を用いて、ユーザーが明示的に許可した範囲に実機解析・診断ログを保存する目的で利用し、広告、販売、プロファイリング等には利用しない旨を記載する。未確定のアクセストークン保存方式などは断定しない。

- [ ] **Step 2: ナビゲーションを追加する**

`index.html`、`privacy.html`、`terms.html` の3ページ間を相対 URL で移動できるようにする。

- [ ] **Step 3: HTML 構造を確認する**

見出し階層、問い合わせ先、改定日の表示、内部リンクを確認する。

- [ ] **Step 4: コミットする**

```bash
git add privacy.html
git commit -m "feat: add privacy policy"
```

### Task 4: 利用規約を実装する

**Files:**
- Create: `terms.html`

**Interfaces:**
- Consumes: `style.css`
- Produces: ClimbClip の公開利用規約。

- [ ] **Step 1: 規約本文を作成する**

以下のセクションを含める。

1. 適用
2. 利用条件
3. 禁止事項
4. Google Drive 連携
5. 本アプリの変更・停止
6. 知的財産権
7. 免責・責任制限
8. 規約の変更
9. 準拠法
10. 問い合わせ先

利用者自身の責任、法令・第三者権利の尊重、サービス変更・停止の可能性、完全性・継続性・特定目的適合性を保証しないこと、適用法令上許される範囲での責任制限、日本法準拠を簡潔に記載する。特定の専属的合意管轄は設けない。

- [ ] **Step 2: ナビゲーションを追加する**

3ページ間の相対リンクを揃える。

- [ ] **Step 3: HTML 構造を確認する**

見出し階層、問い合わせ先、制定日の表示、内部リンクを確認する。

- [ ] **Step 4: コミットする**

```bash
git add terms.html
git commit -m "feat: add terms of service"
```

### Task 5: README と静的検証を仕上げる

**Files:**
- Modify: `README.md`
- Create: `tests/validate_site.py`

**Interfaces:**
- Consumes: `index.html`, `privacy.html`, `terms.html`, `style.css`
- Produces: 公開手順の説明と、依存なしで実行できるサイト構造検証スクリプト。

- [ ] **Step 1: 失敗する検証スクリプトを先に用意する**

Python 標準ライブラリだけで、次を検証する `tests/validate_site.py` を作成する。

- `index.html`, `privacy.html`, `terms.html`, `style.css`, `.nojekyll` が存在する
- 3ページに `<html lang="ja">` がある
- 3ページから `style.css` が参照される
- 3ページすべてから `index.html` / `privacy.html` / `terms.html` に到達可能なリンクがある
- `index.html` に `ClimbClip`, `Google Drive`, `プライバシーポリシー`, `利用規約` がある
- `privacy.html` に `Google Drive`, `drive.file`, `kaynos.gm@gmail.com` がある
- `terms.html` に `禁止事項`, `免責`, `日本法`, `kaynos.gm@gmail.com` がある
- `href="/` や `src="/` のような Project Site を壊すルート絶対 URL を使用していない

- [ ] **Step 2: 検証を実行する**

Run:

```bash
python3 tests/validate_site.py
```

Expected: 実装漏れがあれば非0で終了し、対象ファイルと条件を表示する。

- [ ] **Step 3: README を更新する**

`README.md` にサイト目的、公開予定URL、GitHub Pagesを `main` / `/(root)` から公開する手順、ローカル検証コマンドを記載する。

- [ ] **Step 4: 検証を再実行する**

Run:

```bash
python3 tests/validate_site.py
```

Expected: `All site validation checks passed.` と表示して終了コード0。

- [ ] **Step 5: コミットする**

```bash
git add README.md tests/validate_site.py
git commit -m "test: add static site validation"
```

### Task 6: PR 前検証と提出

**Files:**
- Verify only

**Interfaces:**
- Consumes: 全実装ファイル
- Produces: レビュー可能なPR。

- [ ] **Step 1: 最終検証を実行する**

```bash
python3 tests/validate_site.py
```

Expected: PASS。

- [ ] **Step 2: main との差分を確認する**

設計書・計画書以外に、意図しないファイルや秘密情報が含まれていないことを確認する。

- [ ] **Step 3: PR を作成する**

タイトル:

```text
ClimbClip 公開サイトのホーム・プライバシーポリシー・利用規約を追加
```

本文には、3ページ追加、Google Drive連携の説明、静的検証、マージ後にGitHub Pages設定が必要であることを記載する。
