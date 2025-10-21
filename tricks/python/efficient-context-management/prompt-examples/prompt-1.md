# Prompt Example 1: Setting Up .claudeignore for a New Project

## Scenario
You've just cloned a Python project and want to ensure Claude Code works efficiently by excluding unnecessary files.

## User Prompt

```
I just cloned this Python project. Can you help me set up a .claudeignore file so you don't waste time reading virtual environment and cache files?
```

## Expected Claude Behavior

1. **Acknowledge the request** and explain the benefit
2. **Analyze the project structure** to identify what should be ignored
3. **Create .claudeignore** with appropriate patterns for the project type
4. **Verify** the configuration works by running a test search

## Example Response Flow

```
User: I just cloned this Python project. Can you help me set up a .claudeignore
      file so you don't waste time reading virtual environment and cache files?

Claude: I'll help you create a .claudeignore file optimized for your Python project.
        Let me first check what's currently in your project structure.

        [Claude uses Glob to scan the project]

        I can see you have:
        - A venv/ directory with ~2,500 dependency files
        - __pycache__/ directories
        - A .pytest_cache/ directory
        - dist/ and build/ directories

        I'll create a .claudeignore file to exclude these. This will make my file
        operations much faster and focus on your actual source code.

        [Claude creates .claudeignore with appropriate patterns]

        Done! I've created a .claudeignore file that excludes:
        - Virtual environments (venv/, .venv/)
        - Python cache files (__pycache__/, *.pyc)
        - Test caches (.pytest_cache/)
        - Build artifacts (dist/, build/, *.egg-info)
        - IDE configurations (.vscode/, .idea/)

        Let me verify it's working...

        [Claude runs Glob *.py to verify]

        Perfect! Now I see only your 23 source code files instead of thousands of
        dependency files. This will make our work much more efficient.
```

## Key Teaching Points

1. **Proactive analysis**: Claude should scan the project first
2. **Explanation**: Clearly state what will be excluded and why
3. **Verification**: Always verify the .claudeignore works as expected
4. **Quantify impact**: Mention how many files are now excluded (e.g., "2,500 dependency files")
