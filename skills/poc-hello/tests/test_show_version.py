"""version_info.md が存在し、バージョン表記を含むことを確認する。"""
from pathlib import Path


def test_version_info_exists() -> None:
    info = Path(__file__).resolve().parent.parent / "references" / "version_info.md"
    assert info.exists()
    assert "バージョン" in info.read_text(encoding="utf-8")
