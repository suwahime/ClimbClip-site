# ClimbClip-site

ClimbClip の公開情報サイトです。

Google OAuth の外部向け運用に必要な公開ページとして、以下を提供します。

- ホーム: `index.html`
- プライバシーポリシー: `privacy.html`
- 利用規約: `terms.html`

## GitHub Pages

PR マージ後、GitHub リポジトリの **Settings → Pages** で公開元を `main` ブランチの `/ (root)` に設定します。

公開予定 URL:

- `https://suwahime.github.io/ClimbClip-site/`
- `https://suwahime.github.io/ClimbClip-site/privacy.html`
- `https://suwahime.github.io/ClimbClip-site/terms.html`

## ローカル検証

追加依存はありません。Python 3 の標準ライブラリのみで、必要ファイル・内部リンク・主要文言・GitHub Pages の相対パスを検証できます。

```bash
python3 tests/validate_site.py
```

期待結果:

```text
All site validation checks passed.
```
