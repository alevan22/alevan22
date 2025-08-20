
# Security Release Checklist — Mini AppSec Lab

**Release tag**: v0.1

## Before merge
- [ ] All Issues linked in MR (`Closes #…`)
- [ ] Unit tests: at least **6** pass (3 vuln repro pre-fix, 3 post-fix)
- [ ] **Semgrep** report attached, no high-severity matches in changed code
- [ ] **npm audit** report attached, no critical direct vulnerabilities
- [ ] **Gitleaks** report attached, no findings in repo history
- [ ] Manual repros confirm: XSS blocked, traversal blocked
- [ ] README updated with steps and expected outputs
- [ ] Threat model updated to reflect current design

## After merge
- [ ] MR merged with squash and signed commit (if enforced)
- [ ] Release tag created (v0.1)
- [ ] Screenshots captured: Issues, MR, CI pipeline summary
- [ ] Close-out note posted with links to artifacts

## Optional (stretch)
- [ ] Add ZAP baseline stage
- [ ] Add pre-commit hooks for local SAST/secret checks
- [ ] Add CSP headers and test
