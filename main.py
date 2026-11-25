from pathlib import Path

ENTRY = "Have you tried turning it off and on again — and by 'it', I mean your hopes, your dreams, and this call?"


def main():
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
