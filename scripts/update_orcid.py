#!/usr/bin/env python3
"""Update local YAML (sidebar) and publications from ORCID public record.

This script is designed to run in GitHub Actions.
It tries unauthenticated public reads first. If ORCID_TOKEN is set, it will use it.

You must set ORCID_ID in the environment (e.g., 0000-0000-0000-0000).
"""

import os, sys, json, re
from datetime import date
import requests
import yaml

ORCID_ID = os.environ.get("ORCID_ID", "").strip()
TOKEN = os.environ.get("ORCID_TOKEN", "").strip()

if not ORCID_ID:
    print("ORCID_ID is not set; skipping.")
    sys.exit(0)

BASE = f"https://pub.orcid.org/v3.0/{ORCID_ID}"
HEADERS = {
    "Accept": "application/json",
}
if TOKEN:
    HEADERS["Authorization"] = f"Bearer {TOKEN}"

def get_json(endpoint: str):
    r = requests.get(f"{BASE}/{endpoint}", headers=HEADERS, timeout=30)
    if r.status_code >= 400:
        raise RuntimeError(f"ORCID request failed {r.status_code}: {r.text[:200]}")
    return r.json()

def safe_slug(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:80] or "item"

# 1) Update sidebar bio basics (optional): person endpoint
try:
    person = get_json("person")
except Exception as e:
    print(f"Could not read person data: {e}")
    person = None

if person:
    name = person.get("name", {})
    given = (name.get("given-names") or {}).get("value") or ""
    family = (name.get("family-name") or {}).get("value") or ""
    display_name = (given + " " + family).strip()

    bio = ((person.get("biography") or {}).get("content") or "").strip()

    out = {
        "orcid_id": ORCID_ID,
        "name": display_name,
        "bio": bio,
    }
    os.makedirs("_data", exist_ok=True)
    with open("_data/orcid_profile.yml", "w", encoding="utf-8") as f:
        yaml.safe_dump(out, f, sort_keys=False, allow_unicode=True)

# 2) Update publications from works summary (public)
# Endpoint: /activities works summary is embedded in /activities? We'll use /works
try:
    works = get_json("works")
except Exception as e:
    print(f"Could not read works: {e}")
    sys.exit(0)

groups = works.get("group", []) or []
os.makedirs("_publications_orcid", exist_ok=True)

def pick_year(work_summary):
    pub_date = (work_summary.get("publication-date") or {})
    y = (pub_date.get("year") or {}).get("value")
    if y and y.isdigit():
        return int(y)
    return None

for g in groups:
    ws = (g.get("work-summary") or [])
    if not ws:
        continue
    w = ws[0]  # primary
    title = ((w.get("title") or {}).get("title") or {}).get("value") or "Untitled"
    year = pick_year(w) or date.today().year
    month = (w.get("publication-date") or {}).get("month", {}).get("value") or "01"
    day = (w.get("publication-date") or {}).get("day", {}).get("value") or "01"
    dt = f"{year}-{month.zfill(2)}-{day.zfill(2)}"

    # DOI if present
    doi = None
    for ext in (w.get("external-ids") or {}).get("external-id", []) or []:
        if (ext.get("external-id-type") or "").lower() == "doi":
            doi = ext.get("external-id-value")
            break

    slug = f"{year}-{safe_slug(title)}"
    path = os.path.join("_publications_orcid", f"{slug}.md")

    front = {
        "title": title,
        "collection": "publications",
        "date": dt,
        "pub_type": "orcid",
        "venue": "ORCID record",
    }
    if doi:
        front["doi"] = doi

    with open(path, "w", encoding="utf-8") as f:
        f.write("---\n")
        yaml.safe_dump(front, f, sort_keys=False, allow_unicode=True)
        f.write("---\n\n")
        f.write("Imported from ORCID.\n")

print(f"Generated {len(os.listdir('_publications_orcid'))} ORCID items in _publications_orcid/.")
print("You can choose to merge these into _publications/ or keep separate and display both.")
