# Personal AI Playbook

## When I reach for AI first
- **Documentation generation**: Creating README sections, release evidence, and structured documentation where format matters more than creative content
- **Configuration templates**: CI/CD workflows, Dockerfiles, and other infrastructure files where I know the pattern but want to ensure best practices
- **Code review assistance**: Getting a second pair of eyes on security issues, potential bugs, or improvement opportunities in existing code
- **Debugging**: When stuck on an error or unexpected behavior, using AI to suggest debugging approaches or common causes
- **Test coverage**: Identifying edge cases or test scenarios I might have missed in my test suite

## When I do not reach for AI first
- **Core business logic**: The actual problem-solving code that defines what my application does
- **Security-sensitive operations**: Anything involving authentication, authorization, cryptography, or secrets handling
- **Production deployments**: Database migrations, infrastructure changes, or anything that affects live systems
- **Learning new concepts**: When the goal is to understand something deeply, I work through it manually first
- **Emergency fixes**: Time-sensitive production issues where I need full control and understanding

## My non-negotiables
- **Never paste secrets**: No API keys, passwords, tokens, or real customer data in AI tools
- **Always verify AI output**: I run commands, check files, and test suggestions before accepting them
- **Own every line**: If I can't explain why a change was made, I don't submit it
- **Version consistency**: Ensure Python versions, dependencies, and environments match across local, CI, and Docker
- **Security first**: Any AI suggestion involving security gets extra scrutiny and manual verification
- **Documentation alignment**: If AI generates docs, I verify the claims against actual code behavior

## My review rules
- **Diff inspection**: I read every line of code changes AI suggests, checking for logic errors, security issues, and style consistency
- **Command verification**: I run commands locally when possible to ensure they work as expected
- **Evidence-based grading**: When AI provides code review findings, I verify each one against actual files before accepting or rejecting
- **Context matters**: I consider whether AI suggestions make sense for the specific project scope (learning vs. production)
- **Incremental acceptance**: I apply AI suggestions piece by piece, testing each change rather than accepting large diffs blindly

## What I am still figuring out
- **Tool selection for different tasks**: When to use specialized AI tools vs. general-purpose assistants
- **Team norms**: How to establish AI usage guidelines in a team setting with different experience levels
- **Balancing speed vs. understanding**: When AI acceleration helps learning vs. when it shortcuts the learning process
- **AI model limitations**: Understanding where different AI models excel or struggle based on their training

## Decision Card

### New feature
- Use AI for: Initial brainstorming, documentation drafts, test case suggestions
- Don't use AI for: Core implementation without understanding, security-critical components
- Rule: I must be able to explain the feature's implementation before committing

### Code review
- Use AI for: Security patterns, best practices, edge case identification
- Don't use AI for: Judgments about business logic appropriateness without context
- Rule: Verify all AI findings against actual code before accepting

### Debugging
- Use AI for: Suggesting debugging approaches, common error explanations
- Don't use AI for: Running destructive commands or making changes without testing
- Rule: Test AI suggestions in isolation before applying to the main codebase

### Infrastructure
- Use AI for: Configuration templates, CI/CD patterns, Docker best practices
- Don't use AI for: Production secrets, database schema changes, networking config
- Rule: All infrastructure changes must be manually reviewed and tested

### Never-paste
- Never paste: API keys, passwords, tokens, customer data, production logs, .env files
- Always use: Example data, mock credentials, sanitized logs, .env.example files
- Rule: If I'm unsure whether data is sensitive, I don't paste it

### One rule
- **Verification before submission**: Every AI-assisted change must be manually verified, tested, and understood before being committed. If I can't explain it, I don't submit it.