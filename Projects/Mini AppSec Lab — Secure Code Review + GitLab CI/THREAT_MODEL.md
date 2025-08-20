
# Threat Model — Mini AppSec Lab (STRIDE)

**System**: Tiny TypeScript/Express app exposing two routes.  
**Trust boundaries**: Internet client → Express app; app → filesystem (read-only).  
**Assets**: Response HTML, filesystem contents under `./public`, secrets (dummy in code).

## Routes

### 1) `GET /search?q=`
- **Spoofing**: N/A (no auth)  
- **Tampering**: N/A  
- **Repudiation**: Add request logging with timestamp, IP, UA  
- **Information Disclosure**: N/A  
- **Denial of Service**: Large `q` values; mitigate with length cap  
- **Elevation of Privilege**: **Reflected XSS** enables DOM execution

**Abuse case**: Attacker crafts a link with `<img src=x onerror=alert(1)>` causing script execution in the victim’s browser.  
**Mitigations**: HTML-escape user input, output encode, CSP headers, input length limits.  
**Validation**: Unit tests around encoding; manual payload checks.  

### 2) `GET /download?file=`
- **Spoofing**: N/A  
- **Tampering**: Path traversal to read unexpected files  
- **Repudiation**: Log file paths requested and normalized result  
- **Information Disclosure**: **High** risk if `../../` resolves outside the intended dir  
- **Denial of Service**: Large files; limit size, implement timeouts  
- **Elevation of Privilege**: N/A

**Abuse case**: `../../package.json` returns unintended file.  
**Mitigations**: Normalize path, enforce allowlist or jail to `./public`, reject `..`, permission checks.  
**Validation**: Unit tests for traversal attempts; negative tests for blocked inputs.

## Secrets
- **Risk**: Hardcoded key in code may leak via repo or logs.  
- **Mitigations**: Move to environment variable, add `.env.example`, add secret scanning in CI, avoid commits with real secrets.  
- **Validation**: Gitleaks report clean on MR.

## Controls summary
- Input validation and output encoding  
- CSP headers (recommended)  
- Strict path normalization and allowlist  
- Comprehensive logging for requests and errors  
- CI security gates: SAST, SCA, secret scanning
