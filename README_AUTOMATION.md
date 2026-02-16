# ORCID / Google Scholar auto-update (best-effort)

## ORCID (recommended)
This repo includes a GitHub Action + script that can fetch public data from ORCID and generate publication stubs
into `_publications_orcid/`.

### Setup
1. In your GitHub repo settings → Secrets and variables → Actions → **Secrets**, add:
   - `ORCID_ID` (e.g., `0000-0000-0000-0000`)

2. (Optional) Add `ORCID_TOKEN` if you want authenticated requests.
   ORCID public API may require credentials depending on your configuration. See ORCID docs:
   https://info.orcid.org/documentation/api-tutorials/api-tutorial-read-data-on-a-record/

3. Run the workflow manually (Actions → Auto-update ORCID/Scholar) or wait for Monday schedule.

## Google Scholar (optional, fragile)
Google Scholar has no stable public API; automated fetching may be blocked.
We include a best-effort step using the `scholarly` Python package.
If it fails, the workflow continues without breaking the build.

Add secret `SCHOLAR_USER_ID` (the `user=...` value from your Scholar profile URL).

## DOI badges
DOI badges are rendered using shields.io:
`https://img.shields.io/badge/DOI-<doi>-blue`
and link to `https://doi.org/<doi>`.
