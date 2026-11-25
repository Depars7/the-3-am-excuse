"""The 3 AM Excuse — hardware-wallet refusal writer.

Writes the winning one-line excuse to /output/entry.txt as exact UTF-8
bytes with no trailing newline. The line is the wallet itself speaking:
it refuses to sign at 3 AM because the owner who actually reads the
address went to bed hours ago, while the owner holding it now just tried
to send rent money to a frog. The punchline is withheld until the end.

Gate asserted before writing: 1-199 characters, a single line, not only
whitespace, no emoji, no quotation marks, valid UTF-8 when encoded.
The written file is verified by read-back: exact bytes, mode 0644,
no trailing newline.
"""

import os
import stat

ENTRY_TEXT = (
    "I'm not signing at 3 AM. The you who actually reads the address "
    "went to bed hours ago \u2014 the you holding me just tried to send "
    "rent money to a frog."
)
OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> bytes:
    """Check the entry against the gate and return its exact UTF-8 bytes."""
    assert isinstance(text, str) and text.strip(), "entry must be non-blank text"
    assert 1 <= len(text) <= 199, f"entry must be 1-199 chars, got {len(text)}"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert '"' not in text, "entry must carry no quotation marks"
    assert not any(_is_emoji(ch) for ch in text), "entry must carry no emoji"
    data = text.encode("utf-8")
    assert data.decode("utf-8") == text, "entry must round-trip as UTF-8"
    return data


def _is_emoji(ch: str) -> bool:
    """True for characters in the common emoji blocks (beyond > U+1F000)."""
    code = ord(ch)
    return (
        code > 0x1F000
        or 0x2600 <= code <= 0x27BF  # misc symbols, dingbats, emoticon text
        or code in (0xFE0F, 0x200D)  # variation selector, zero-width joiner
    )


def verify_written(data: bytes) -> None:
    """Re-read the output file and assert it is exactly the intended bytes."""
    with open(OUTPUT_PATH, "rb") as fh:
        written = fh.read()
    assert written == data, "written bytes must match the entry exactly"
    assert not written.endswith(b"\n"), "entry must have no trailing newline"


def main() -> None:
    data = validate(ENTRY_TEXT)
    os.umask(0o022)
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(data)
        fh.flush()
        os.fsync(fh.fileno())
    os.chmod(OUTPUT_PATH, 0o644)
    mode = stat.S_IMODE(os.stat(OUTPUT_PATH).st_mode)
    assert mode == 0o644, f"unexpected file mode {oct(mode)}"
    verify_written(data)


if __name__ == "__main__":
    main()
