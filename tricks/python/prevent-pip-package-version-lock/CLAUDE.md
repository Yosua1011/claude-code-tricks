================== existing CLAUDE.md ================== 

## Using Context7 for Latest Documentation

**ALWAYS use Context7 when working with external libraries.**

Add `use context7` to your prompts when:
- Installing or configuring any library
- Writing code that uses external packages
- Checking API syntax or available methods
- Unsure about current best practices

Example prompts:
- "Set up FastAPI with SQLAlchemy. use context7"
- "Create a data pipeline with Polars. use context7"
- "Build an async web scraper with httpx. use context7"

This ensures you get current documentation instead of relying on outdated training data.

## Package Versions & Dependencies

**IMPORTANT**: Your knowledge cutoff is January 2025, but the current date is October 2025.

### Version Management Rules:
1. **DO NOT assume package versions** based on your knowledge cutoff
2. **Always use latest available versions** unless specified otherwise
3. Use `pip index versions <package-name>` to check latest versions
4. Install packages WITHOUT version pinning: `pip install package-name`
5. Only pin versions if there's a compatibility issue or specific requirement

### Dependency Management:
- Keep `requirements.txt` up to date after installing new packages
- Use `pip freeze > requirements.txt` or manually curate it
- Document why any version is pinned in comments

================== existing CLAUDE.md ==================
