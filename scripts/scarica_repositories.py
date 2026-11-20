#!/usr/bin/env python3
"""Elenca o clona, su richiesta esplicita, i repository linkati nel catalogo.

Non esegue codice dei repository scaricati. Necessita di Python 3 e Git.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "docs" / "CATALOGO_COMPLETO.md"
TARGET = ROOT / "repository_esterni"
PATTERN = re.compile(r"https://github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")


def available():
    source = CATALOG.read_text(encoding="utf-8")
    # Usa l'ordine della tabella e rimuove duplicati senza perdere l'ordine.
    return list(dict.fromkeys(PATTERN.findall(source)))


def main():
    parser = argparse.ArgumentParser(description="Scarica i sorgenti GitHub elencati nel catalogo.")
    parser.add_argument("--list", action="store_true", help="Elenca tutti i repository.")
    parser.add_argument("--repo", action="append", default=[], help="Seleziona owner/nome; ripetibile.")
    parser.add_argument("--all", action="store_true", help="Scarica TUTTI i progetti (puo' richiedere molto spazio).")
    args = parser.parse_args()
    entries = available()
    if not args.all and not args.repo:
        for entry in entries:
            print(entry)
        print(f"\nTotale: {len(entries)} repository. Usa --repo o --all per scaricarli.")
        return 0
    chosen = entries if args.all else list(dict.fromkeys(args.repo))
    unknown = [entry for entry in chosen if entry not in entries]
    if unknown:
        parser.error("Repository non presenti nel catalogo: " + ", ".join(unknown))
    TARGET.mkdir(parents=True, exist_ok=True)
    errors = 0
    for name in chosen:
        owner, project = name.split("/", 1)
        dest = TARGET / owner / project
        if dest.exists():
            print(f"Gia' presente: {dest}; nessuna sovrascrittura.")
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        print("Clono:", name, flush=True)
        try:
            subprocess.run(["git", "clone", "--", "https://github.com/" + name + ".git", str(dest)], check=True)
        except (OSError, subprocess.CalledProcessError) as exc:
            print("Errore per " + name + ": " + str(exc), file=sys.stderr)
            errors += 1
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
