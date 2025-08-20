
# Mini AppSec Lab — Secure Code Review + GitLab CI (TypeScript/Express)

**Purpose**  
A tiny, intentionally vulnerable TypeScript/Express app to practice AppSec workflows in **GitLab**: Issues, Merge Requests, CI jobs for **SAST/SCA/secret scanning**, and documentation. Scope fits a **4–6 hour** build.

**What you’ll show**  
- Ability to triage issues with **repro steps**, **STRIDE** notes, and **CVSS** estimates.  
- Ability to fix issues via **MR** with linked **CI artifacts**.  
- Ability to document and ship a **security release** with a checklist.

---

## Scope

Two endpoints with deliberate flaws:
1. `GET /search?q=` → **Reflected XSS** via unsanitized user input.  
2. `GET /download?file=` → **Path traversal** risk due to naive file read.

A dummy hardcoded secret is present to trigger secret scanning.

**Quantifiable artifacts**  
- 2 vulnerable routes  
- 3 GitLab Issues (XSS, path traversal, hardcoded secret)  
- 1 Merge Request that closes all 3 Issues  
- 3 CI jobs (Semgrep SAST, npm audit SCA, Gitleaks secrets)  
- 6 supertest cases (3 failing before fix, 3 passing after fix)  
- 1 security release checklist, 1 threat model

---

## Quick start

```bash
# Requirements: Node 20+, npm
npm ci || npm i
npm run build || npx tsc
npm start
# in another shell
curl "http://localhost:3000/search?q=<img src=x onerror=alert(1)>"
curl "http://localhost:3000/download?file=../../package.json"
```

## Tests

```bash
npm test
# Expected: 3 tests fail on vulnerable branch; all pass after MR fixes
```

---

## GitLab CI

`.gitlab-ci.yml` defines three fast jobs:
- **SAST:** `semgrep --config p/owasp-top-ten --config auto`  
- **SCA:** `npm audit --json`  
- **Secrets:** `gitleaks detect --report-format sarif`

Artifacts (`semgrep.json`, `npm-audit.json`, `gitleaks.sarif`) attach to the pipeline and the MR.

**Pipeline goals**  
- Runtime under **3 minutes** on Node:20 image  
- Clear pass/fail signals for review

---

## Issues and MR

Create three Issues:  
- **Reflected XSS in `/search`** — repro with `<img onerror>` payload; CVSS AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N  
- **Path traversal in `/download`** — repro with `../../` payload; CVSS AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N  
- **Hardcoded secret** — detected by Gitleaks; move to env var

Open one MR `fix/xss-path-secrets` that:
- Escapes user input for `/search` using `escape-html`
- Normalizes and allowlists paths for `/download`
- Removes hardcoded secret, uses `process.env`, adds `.env.example`
- Updates tests to pass

Link Issues with `Closes #1 #2 #3`. Attach CI artifacts.

---

## Security release checklist

See `docs/SECURITY_RELEASE_CHECKLIST.md`.

---

## Threat model (STRIDE)

See `docs/THREAT_MODEL.md` for route-by-route analysis and mitigations.

---

## Next steps (optional, time permitting)
- Add **OWASP ZAP baseline** scan stage.  
- Add pre-commit hooks with `lefthook` or `pre-commit`.  
- Add SAST rule tuning and custom Semgrep policies.  
- Containerize with minimal Node base image.

---

## License
This lab is for educational purposes.

