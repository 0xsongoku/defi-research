"""Bewaakt de woord-caps op alles wat elke sessie automatisch laadt, en dat er geen secrets
in git staan. Draai: python3 tests/test_context_budget.py (exit 0 = ok).

Een cap verhogen is een bewuste wijziging met Erics akkoord (CLAUDE.md § Geheugen-discipline).
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CAPS = {
    "CLAUDE.md": 1100,
    "lessen.md": 600,
    "MEMORY.md": 800,
    "profiel.md": 500,
}

FORBIDDEN_TRACKED = (".env", ".pem", ".key")


def main() -> int:
    failures = []
    for name, cap in CAPS.items():
        words = len((ROOT / name).read_text(encoding="utf-8").split())
        status = "ok" if words <= cap else "TE LANG"
        print(f"{name:12} {words:5} / {cap} woorden  {status}")
        if words > cap:
            failures.append(f"{name}: {words} > {cap}")

    tracked = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout.split()
    leaked = [f for f in tracked if f.endswith(FORBIDDEN_TRACKED) or "/.env" in f]
    if leaked:
        failures.append(f"secrets in git: {leaked}")

    if failures:
        print("FAIL: " + "; ".join(failures))
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
