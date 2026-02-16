#!/usr/bin/env python3
"""OPTIONAL Google Scholar updater.

Google Scholar has no stable public API and may block automated requests.
This script is best-effort: it tries to use the 'scholarly' package if installed.

If it fails, it exits 0 so the workflow continues.
"""
import os, sys
try:
    from scholarly import scholarly  # type: ignore
except Exception:
    print("scholarly not installed; skipping.")
    sys.exit(0)

USER_ID = os.environ.get("SCHOLAR_USER_ID", "").strip()
if not USER_ID:
    print("SCHOLAR_USER_ID not set; skipping.")
    sys.exit(0)

try:
    author = scholarly.search_author_id(USER_ID)
    author = scholarly.fill(author, sections=["publications"])
except Exception as e:
    print(f"Scholar fetch failed (likely blocked): {e}")
    sys.exit(0)

os.makedirs("_data", exist_ok=True)
with open("_data/google_scholar.json", "w", encoding="utf-8") as f:
    import json
    json.dump(author, f, ensure_ascii=False, indent=2)

print("Saved _data/google_scholar.json (best-effort).")
