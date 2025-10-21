# Claude Code Configuration: Efficient Context Management

**Current Date: 2025-10-21**

## Purpose

This configuration ensures you help users optimize their Claude Code context usage by properly configuring `.claudeignore` files for Python projects.

## Core Principles

1. **Proactive Guidance**: When you notice inefficient context usage (e.g., reading virtual environments, cache directories), suggest creating or updating `.claudeignore`

2. **Context Awareness**: Before performing broad file searches, check if a `.claudeignore` file exists. If not, recommend creating one for Python projects.

3. **Pattern Recognition**: Recognize these anti-patterns and suggest `.claudeignore`:
   - Glob results showing `site-packages/` or `venv/` files
   - Grep searching through `__pycache__/` directories
   - File listings dominated by cache or build artifacts
   - Slow response times due to large context

## .claudeignore Best Practices

### When to Recommend .claudeignore

Suggest creating `.claudeignore` when:
- User has a Python project without one
- You notice virtual environment files in search results
- Context is being wasted on non-source files
- User asks about project structure and you see clutter

### Standard Python .claudeignore Template

Always recommend this baseline template for Python projects:

```
# Virtual Environments
venv/
.venv/
env/
ENV/

# Python Cache
__pycache__/
*.pyc
*.pyo
*.pyd

# Testing Cache
.pytest_cache/
.coverage
.tox/
.nox/

# Type Checking
.mypy_cache/
.pytype/

# Distribution
build/
dist/
*.egg-info/

# Documentation builds
docs/_build/
site/

# Notebooks
.ipynb_checkpoints/

# IDEs
.vscode/
.idea/
```

### Customization by Project Type

**Data Science / ML Projects:**
```
# Add to standard template:
data/raw/
data/processed/
*.csv
*.parquet
*.h5
*.pkl
*.pt
*.pth
models/weights/
```

**Web Development (Django/Flask):**
```
# Add to standard template:
staticfiles/
media/
*.sqlite3
db.sqlite3
migrations/
```

**Package Development:**
```
# Add to standard template:
.eggs/
.tox/
htmlcov/
```

## Workflow Instructions

### When User Starts New Project

1. Check for `.claudeignore` file
2. If missing and it's a Python project, suggest:
   ```
   I notice you don't have a .claudeignore file. This can help me work more efficiently by excluding virtual environments and cache files. Would you like me to create one?
   ```

### When Performing File Operations

1. **Before Glob/Grep**: If you anticipate hitting ignored directories, that's good - the ignore is working
2. **After large results**: If Glob returns thousands of files including venv/cache, suggest `.claudeignore`
3. **Performance issues**: If operations are slow, check if context reduction would help

### When User Asks About Files

If user asks "what files are in this project?" or similar:
1. List source files clearly
2. If you see clutter, mention: "I also see [venv/cache/build] directories that could be excluded with .claudeignore for better performance"

## Communication Guidelines

### Do Say:
- "I can help you create a .claudeignore file to exclude virtual environments and cache directories"
- "Adding .claudeignore will speed up my file searches and focus on your source code"
- "I notice files from your virtual environment. Should we add a .claudeignore?"

### Don't Say:
- "I cannot read files" (you can, just suggest ignoring irrelevant ones)
- "You must create .claudeignore" (it's a suggestion, not requirement)
- Technical jargon without explanation

## Pattern Syntax Reference

For helping users write custom patterns:

- `file.txt` - Exact filename in any directory
- `*.py` - All Python files
- `dir/` - Entire directory and contents
- `**/temp/` - Directory named 'temp' anywhere in tree
- `!important.py` - Exception (don't ignore this file)

## Verification Steps

After creating/updating `.claudeignore`, verify:

1. Run a Glob search for Python files - should show only source code
2. Check that important files are still accessible
3. Confirm cache/venv directories are excluded

Example verification:
```
Let me verify the .claudeignore is working correctly...
[Use Glob to search for *.py files]
Great! Now I only see your source code files, not the virtual environment.
```

## Edge Cases

**User wants to analyze dependency code:**
- Suggest temporarily commenting out venv/ in `.claudeignore`
- Or use `!venv/specific_package/` to include just that package

**User's important files match ignore patterns:**
- Use `!` negation patterns
- Or use more specific directory paths in ignore patterns

**Project has nested virtual environments:**
- Use `**/.venv/` to match at any level
- Verify with user which ones to exclude

## Integration with Other Workflows

This trick works well with:
- **Version management tricks**: Clean context helps you suggest correct versions
- **Slash commands**: Custom commands can ensure `.claudeignore` exists
- **MCP servers**: Less noise means better context for MCP tool results

## Success Metrics

You've successfully implemented this trick when:
- File searches return only relevant source code
- Users notice faster response times
- Context is focused on actual code, not dependencies
- Users understand and maintain their `.claudeignore` file

## Remember

`.claudeignore` is about **focusing your attention** on what matters - the user's actual code. It's not about limiting capability, but about working smarter with the context window available.
