"""Check the written entry against the bounty gate.

Asserts /output/entry.txt exists, is UTF-8, 1-199 characters, a single line,
carries no emoji and no quotation marks, and has no trailing newline.
Run: python3 tests/check_entry.py
"""

import sys
from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> int:
    assert OUTPUT_PATH.exists(), "entry file is missing"
    data = OUTPUT_PATH.read_bytes()
    text = data.decode("utf-8")  # raises on invalid UTF-8
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 199, f"entry must be 1-199 chars, got {len(text)}"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert '"' not in text, "entry must carry no quotation marks"
    assert not any(_is_emoji(ch) for ch in text), "entry must carry no emoji"
    assert not data.endswith(b"\n"), "entry must have no trailing newline"
    print(f"OK: {len(text)} chars, {len(data)} bytes, single line, no newline")
    return 0


def _is_emoji(ch: str) -> bool:
    """True for characters in the common emoji blocks (beyond > U+1F000)."""
    code = ord(ch)
    return (
        code > 0x1F000
        or 0x2600 <= code <= 0x27BF  # misc symbols, dingbats, emoticon text
        or code in (0xFE0F, 0x200D)  # variation selector, zero-width joiner
    )


if __name__ == "__main__":
    sys.exit(main())
