# Example Project: Testing .claudeignore

This is a sample Python ML project designed to demonstrate the effectiveness of `.claudeignore` for optimizing Claude Code performance.

## Project Structure

```
example-project/
├── src/                    # Source code (4 Python files)
│   ├── main.py
│   ├── data_processor.py
│   ├── model.py
│   ├── utils.py
│   └── __pycache__/        # Python cache (should be ignored)
├── tests/                  # Test files
│   ├── test_data_processor.py
│   └── __pycache__/        # Test cache (should be ignored)
├── venv/                   # Virtual environment (should be ignored)
│   └── lib/python3.11/site-packages/
│       ├── requests/       # 3rd party package
│       ├── numpy/          # 3rd party package
│       └── pandas/         # 3rd party package
├── data/                   # Data directory (should be ignored)
│   ├── raw/
│   │   ├── input.csv
│   │   └── large_dataset.csv
│   └── processed/
│       └── model_weights.pkl
├── dist/                   # Distribution files (should be ignored)
│   └── ml_pipeline-0.1.0-py3-none-any.whl
├── .pytest_cache/          # Pytest cache (should be ignored)
├── .mypy_cache/            # Mypy cache (should be ignored)
├── setup.py                # Package setup
├── requirements.txt        # Dependencies
├── pytest.ini              # Pytest configuration
└── .claudeignore          # Claude ignore patterns
```

## How to Test

### Step 1: Test WITHOUT .claudeignore

First, temporarily disable the `.claudeignore` file to see how Claude behaves without it:

```bash
# Navigate to the example project
cd example-project

# Rename .claudeignore to disable it
mv .claudeignore .claudeignore.disabled
```

Now ask Claude Code:

```
What Python files do you see in this project?
```

**Expected Result:** Claude will return ALL files including:
- Source files in `src/`
- Virtual environment files in `venv/lib/python3.11/site-packages/`
- Cache files in `__pycache__/` directories
- Build artifacts in `dist/`
- Data files in `data/`

**Total files:** ~20+ files including unnecessary ones

### Step 2: Test WITH .claudeignore

Re-enable the `.claudeignore` file:

```bash
# Restore .claudeignore
mv .claudeignore.disabled .claudeignore
```

Ask Claude Code the same question:

```
What Python files do you see in this project?
```

**Expected Result:** Claude will ONLY return:
- Source files in `src/` (4 files)
- Test files in `tests/` (1 file)
- Configuration files (`setup.py`)

**Total files:** ~5-6 relevant source files

### Step 3: Verify Specific Exclusions

Test that specific patterns are working:

**Test virtual environment exclusion:**
```
Search for files in the venv directory
```
Expected: No results or indication that it's being ignored

**Test cache exclusion:**
```
Search for .pyc files
```
Expected: No cache files found

**Test data file exclusion:**
```
Search for .csv files
```
Expected: No CSV files found (data is ignored)

**Test that important files are still accessible:**
```
Can you read setup.py?
```
Expected: Yes, configuration files are still readable

```
Can you read src/main.py?
```
Expected: Yes, source code is still readable

## Performance Comparison

### Without .claudeignore:
- **Total files visible:** ~20+ files
- **Includes:** venv packages, cache files, data files, build artifacts
- **Context usage:** High (lots of irrelevant content)
- **Search speed:** Slower (searches through all files)

### With .claudeignore:
- **Total files visible:** ~6 files
- **Includes:** Only source code and essential configs
- **Context usage:** Low (focused on relevant code)
- **Search speed:** Faster (searches only source files)

## Key Takeaways

1. **Performance:** `.claudeignore` dramatically reduces the number of files Claude processes
2. **Focus:** Results are cleaner and more relevant to actual development
3. **Context Efficiency:** Saves context tokens for actual code analysis
4. **Still Accessible:** Ignored files can still be read with direct paths if needed

## Customizing .claudeignore

You can modify the `.claudeignore` file to suit your needs:

**To exclude additional patterns:**
```bash
# Add to .claudeignore
*.tmp
temp/
scratch/
```

**To include specific files from ignored directories:**
```bash
# Add to .claudeignore
data/           # Ignore all data
!data/schema.py # But include the schema file
```

## Test Commands to Try

Here are some useful commands to test with Claude Code:

1. **File discovery:**
   - "What Python files are in this project?"
   - "Show me the project structure"
   - "List all files in the src directory"

2. **Code search:**
   - "Find all functions that use pandas"
   - "Search for imports of numpy"
   - "Find all test functions"

3. **Verification:**
   - "Can you see files in the venv directory?"
   - "Are there any .pyc files visible?"
   - "Can you read the data files?"

4. **Direct access test:**
   - "Read the file at data/raw/input.csv"
   - (This should work even though data/ is in .claudeignore)

## Notes

- This is a **simulated** project - the venv and data files are minimal representations
- In a real project, the performance difference would be even more dramatic
- Real virtual environments can have 10,000+ files
- Real ML projects can have GBs of data files

The `.claudeignore` file prevents Claude from wasting time and context on these unnecessary files.
