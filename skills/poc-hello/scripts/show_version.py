"""references/version_info.md のバージョン情報を表示する検証用スクリプト。"""
from pathlib import Path


def main() -> None:
    info = Path(__file__).resolve().parent.parent / "references" / "version_info.md"
    print(info.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
