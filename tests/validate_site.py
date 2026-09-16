from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    ROOT / "index.html",
    ROOT / "privacy.html",
    ROOT / "terms.html",
    ROOT / "style.css",
    ROOT / ".nojekyll",
]
HTML_FILES = [ROOT / "index.html", ROOT / "privacy.html", ROOT / "terms.html"]
NAV_TARGETS = ["index.html", "privacy.html", "terms.html"]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def require_text(path: Path, *needles: str) -> str:
    text = path.read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text:
            fail(f"{path.name} is missing required text: {needle}")
    return text


def validate() -> None:
    for path in REQUIRED_FILES:
        if not path.exists():
            fail(f"missing required file: {path.relative_to(ROOT)}")

    for path in HTML_FILES:
        text = require_text(path, '<html lang="ja">', 'href="style.css"')
        for target in NAV_TARGETS:
            if f'href="{target}"' not in text:
                fail(f"{path.name} is missing navigation link to {target}")
        if re.search(r'(?:href|src)="/', text):
            fail(f"{path.name} contains a root-absolute URL that can break GitHub Pages project paths")

    require_text(
        ROOT / "index.html",
        "ClimbClip",
        "Google Drive",
        "プライバシーポリシー",
        "利用規約",
        "kaynos.gm@gmail.com",
    )
    require_text(
        ROOT / "privacy.html",
        "Google Drive",
        "drive.file",
        "kaynos.gm@gmail.com",
        "アクセス権の撤回",
    )
    require_text(
        ROOT / "terms.html",
        "禁止事項",
        "免責",
        "日本法",
        "kaynos.gm@gmail.com",
    )

    print("All site validation checks passed.")


if __name__ == "__main__":
    try:
        validate()
    except (OSError, UnicodeError) as exc:
        print(f"FAIL: {exc}")
        sys.exit(1)
