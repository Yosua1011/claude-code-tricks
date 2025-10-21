# Efficient Context Management with .claudeignore

## The Problem

When working with Python projects, Claude Code may read unnecessary files that waste context tokens and slow down responses:

- **Virtual environments** (`venv/`, `.venv/`, `env/`) containing thousands of dependency files
- **Cache directories** (`__pycache__/`, `.pytest_cache/`, `.mypy_cache/`)
- **Build artifacts** (`dist/`, `build/`, `*.egg-info/`)
- **Large data files** (datasets, models, media files)
- **Generated documentation** (`docs/_build/`, `site/`)
- **IDE configurations** (`.vscode/`, `.idea/`)

Without proper configuration, Claude Code might analyze these files, leading to:
- Slower response times
- Wasted context window on irrelevant content
- Higher costs for API usage
- Difficulty focusing on actual source code

## The Solution

Use `.claudeignore` to explicitly exclude unnecessary directories and files from Claude Code's context. This works similarly to `.gitignore` but specifically for Claude Code's file reading operations.

## Setup

### Step 1: Create .claudeignore File

In your project root, create a `.claudeignore` file:

```bash
touch .claudeignore
```

### Step 2: Add Python-Specific Ignore Patterns

Add these common patterns to your `.claudeignore`:

```
# Virtual Environments
venv/
.venv/
env/
ENV/
virtualenv/

# Python Cache
__pycache__/
*.pyc
*.pyo
*.pyd
.Python

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/
.nox/

# Type Checking
.mypy_cache/
.dmypy.json
dmypy.json
.pytype/

# Distribution / Packaging
build/
dist/
*.egg-info/
.eggs/

# Documentation
docs/_build/
site/
_build/

# Jupyter Notebooks checkpoints
.ipynb_checkpoints/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# Data files (adjust based on your needs)
*.csv
*.parquet
*.h5
*.hdf5
data/raw/
data/processed/

# Models and weights
*.pkl
*.joblib
*.pt
*.pth
*.ckpt
models/weights/

# Environment files (if they contain secrets)
.env
.env.local
credentials.json
secrets.yaml
```

### Step 3: Verify Configuration

You can verify what files Claude Code will read by asking:

```
What Python files do you see in this project?
```

Claude should only list your source code files, not virtual environment or cache files.

## How It Works

1. **Pattern Matching**: `.claudeignore` uses glob patterns similar to `.gitignore`
   - `*` matches any characters except `/`
   - `**` matches any characters including `/` (recursive)
   - `!` negates a pattern (includes files that would otherwise be ignored)

2. **Scope**: The ignore patterns apply to all Claude Code file operations:
   - Glob tool searches
   - Grep content searches
   - Automatic context gathering
   - Task agent file exploration

3. **Performance Impact**:
   - Reduces context size by 70-90% in typical Python projects
   - Faster tool operations (Glob, Grep)
   - More focused code analysis

## Example Usage

### Before .claudeignore

```
User: Find all Python files
Claude: [Returns 5,000+ files including site-packages, cache files, etc.]
```

### After .claudeignore

```
User: Find all Python files
Claude: [Returns only your 50 source code files]
```

### Advanced: Selectively Include Files

Sometimes you want to exclude a directory but include specific files:

```
# Exclude entire data directory
data/

# But include the schema definition
!data/schema.py
!data/README.md
```

## Best Practices

1. **Start Broad, Refine Later**: Begin with common patterns, then adjust based on your needs

2. **Don't Ignore Everything**: Keep these files accessible:
   - Source code (`.py` files)
   - Tests (`test_*.py`, `*_test.py`)
   - Configuration (`setup.py`, `pyproject.toml`)
   - Documentation (`README.md`, `docs/*.md`)

3. **Project-Specific Adjustments**: Customize for your project:
   - ML projects: May want to ignore model files but keep training scripts
   - Web projects: Ignore static assets but keep templates
   - Data projects: Ignore raw data but keep processing scripts

4. **Combine with .gitignore**: Most patterns in `.gitignore` should also be in `.claudeignore`

5. **Test Your Patterns**: Use Claude Code to verify what's visible:
   ```
   Show me what directories you can see in this project
   ```

## Results

With proper `.claudeignore` configuration:

- **Faster responses**: Claude processes only relevant files
- **Better focus**: Analysis concentrated on actual source code
- **Cost efficiency**: Reduced token usage
- **Clearer communication**: File listings show only what matters

## Troubleshooting

**Claude still reading ignored files?**
- Ensure `.claudeignore` is in the project root
- Check pattern syntax (test with simple patterns first)
- Verify file paths are relative to project root

**Accidentally ignored important files?**
- Use `!` prefix to negate patterns
- Be specific with directory names to avoid over-matching

**Not sure what to ignore?**
- Start with the template above
- Ask Claude: "What files should I add to .claudeignore for a Python project?"
- Check your `.gitignore` for additional patterns

## Related Tricks

- Use with "Prevent Pip Package Version Lock" for complete dependency management
- Combine with custom slash commands for project-specific workflows
- Pair with MCP servers for enhanced capabilities
