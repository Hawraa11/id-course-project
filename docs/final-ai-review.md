# Final AI Review and Ownership Evidence

## AGENTS.md guardrails
- Repo-specific stack and commands included: yes
- Docs-first/read-first guardrail included: yes
- Unexpected app/frontend edits rule included: yes

## AI code review mini-log
| AI comment | Grade: Useful / Noise / Wrong | Reason | Verification or decision |
|---|---|---|---|
| Dockerfile uses multi-stage build for smaller image size | Useful | Multi-stage builds separate build dependencies from runtime, reducing final image size and attack surface | Verified in Dockerfile lines 1-10 and 11-29 - builder stage installs dependencies, runtime stage only copies needed files |
| Dockerfile creates non-root user 'app' for security | Useful | Running as non-root reduces risk if container is compromised | Verified in Dockerfile lines 20-21 - adduser command and USER app directive |
| Dockerfile should pin Python version to match CI | Useful | Version consistency between local dev, CI, and Docker prevents environment mismatches | Corrected Dockerfile from Python 3.11 to 3.10 to match .github/workflows/ci.yml |
| Dockerfile includes tests directory in runtime image | Noise | Tests are not needed in production runtime but included for completeness | Acceptable for this learning project - tests add minimal overhead |
| Dockerfile uses --no-cache-dir for pip installs | Useful | Reduces image size by not caching pip metadata | Verified in Dockerfile lines 8-9 - both pip commands use --no-cache-dir |

## AI security mini-review
| Finding | File evidence | Grade: Valid / False Positive / Noise | Reason | Next action |
|---|---|---|---|---|
| CORS allows all origins (allow_origins=["*"]) | app/main.py line 24 | Valid | Wide-open CORS is appropriate for development but not production | Documented as learning project limitation in AGENTS.md |
| No authentication or authorization on endpoints | app/main.py lines 50-91 | Valid | All endpoints are publicly accessible without auth | Documented as learning project scope - not a bug to fix |
| No secrets in .env.example | .env.example lines 1-2 | Valid | Only contains PORT and APP_ENV, no sensitive data | Already secure - no action needed |
| Pydantic models use extra="forbid" to reject unknown fields | app/models.py lines 21, 42, 65 | Valid | Prevents injection of unexpected fields in requests | Good security practice - no action needed |
| Title validation prevents blank titles and length > 200 | app/models.py lines 30-38, 51-61 | Valid | Input validation prevents malformed data | Good security practice - no action needed |
| Dockerfile runs as non-root user | Dockerfile lines 20-21, 25 | Valid | Reduces container security risk | Already implemented - no action needed |
| .dockerignore excludes .env and .env.example | .dockerignore lines 1-2 | Valid | Prevents secrets from being copied into Docker image | Already implemented - no action needed |

## Manual security check
I manually reviewed the CORS configuration in app/main.py and confirmed that while allow_origins=["*"] is a security concern for production, it is explicitly documented as appropriate for this learning project in AGENTS.md. I also verified that .env.example contains no sensitive data (only PORT and APP_ENV), and that the .dockerignore properly excludes environment files to prevent accidental secret inclusion in Docker images. These checks align with the documented scope boundaries of a learning project, not a production deployment.

## One AI output I rejected or corrected
AI initially suggested using Python 3.11 in the Dockerfile. I corrected this to Python 3.10 to match the CI workflow configuration (.github/workflows/ci.yml specifies Python 3.10). Version consistency between development, CI, and Docker environments is important to prevent "works on my machine" issues. I also added httpx and pytest to the Docker build since the CI workflow runs tests, and having test dependencies available in the container supports the same testing capability across environments.

## Three AI usage rules
1. **Never paste secrets**: I will never paste API keys, passwords, tokens, or real customer data into AI tools. I always use .env.example as reference and sanitize any logs or data before sharing with AI.

2. **Always verify before committing**: I will run commands, check files, and test all AI suggestions before accepting them. If I can't explain why a change was made, I don't commit it. This includes reviewing Docker configurations, CI workflows, and any code changes.

3. **Protect scope boundaries**: I will respect the project scope boundaries. For this learning project, I won't add authentication, production databases, or deployment infrastructure without explicit approval. I focus on documentation, CI, Docker, and verification evidence rather than new product features.

## Ownership statement
I am comfortable submitting this repository as my own work because: (1) I ran and verified all baseline tests myself (40 tests passed including new null title validation test), (2) I started the API server and confirmed the /health endpoint returns HTTP 200 with the expected response, (3) I reviewed every configuration file I created or modified (CI workflow, Dockerfile, .dockerignore, documentation), (4) I can explain the purpose of each change - e.g., Python 3.10 for version consistency, non-root user for container security, and .dockerignore exclusions to prevent secret leakage, (5) I fixed the null title validation issue by updating the TaskUpdate model validator and adding corresponding tests, and (6) All documentation reflects actual testing and verification I performed, not assumed or AI-generated claims.