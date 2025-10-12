# Prevent Pip Package Version Lock

Stop Claude Code from getting stuck with outdated Python package versions by using Context7 and dynamic version management.

## The Problem

Claude Code often defaults to package versions from its knowledge cutoff, causing issues with:
* Outdated API syntax and methods
* Deprecated package features
* Compatibility conflicts with newer dependencies
* Incorrect requirements.txt files

## The Solution

Create a CLAUDE.md file in your project root with guidelines that instruct Claude Code to:
* Always use Context7 for external library documentation
* Install latest package versions without pinning
* Generate requirements.txt from actual installed versions

## Setup

1. Add the Context7 MCP server to Claude Code with:
```
claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY: YOUR_API_KEY"
```
Reference: [https://github.com/upstash/context7](https://github.com/upstash/context7)

2. Add the sections from `CLAUDE.md` to your existing CLAUDE.md file in your project root. Don't forget to state current date.
3. Include "use context7" in prompts when working with external libraries
4. Let Claude Code install packages first, then generate requirements.txt using `pip freeze`

## How It Works

The CLAUDE.md file contains specific instructions that override Claude Code's default behavior:
* Forces Claude Code to check latest package versions using `pip index versions`
* Directs Claude Code to Context7 for current documentation
* Prevents assumption-based version pinning

## Example Usage

Instead of:
```
Set up FastAPI with SQLAlchemy
```

Use:
```
Set up FastAPI with SQLAlchemy. use context7
```

This ensures Claude Code accesses current documentation and installs compatible versions.

## Results

* Eliminates "method not found" errors from outdated package knowledge
* Ensures requirements.txt reflects working environment
* Reduces debugging time from version conflicts
* Keeps projects compatible with latest package features
