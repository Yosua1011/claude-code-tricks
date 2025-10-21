# Prompt Example 2: Optimizing Context for ML Projects

## Scenario
You're working on a machine learning project with large datasets and model files. Claude is slow because it's trying to process data files.

## User Prompt

```
Claude seems slow when searching through my ML project. I have a lot of data files
and model checkpoints. How can I speed things up?
```

## Expected Claude Behavior

1. **Diagnose the issue** by checking current file structure
2. **Identify large/unnecessary files** being processed
3. **Suggest .claudeignore** if it doesn't exist, or update existing one
4. **Customize patterns** for ML-specific files (datasets, models, checkpoints)
5. **Show before/after** comparison

## Example Response Flow

```
User: Claude seems slow when searching through my ML project. I have a lot of
      data files and model checkpoints. How can I speed things up?

Claude: Let me check what files I'm currently processing in your project.

        [Claude uses Glob to scan]

        I found the issue! I'm reading:
        - 150 CSV files in data/raw/ (~2.5GB total)
        - 45 .pt model checkpoint files (~8GB)
        - Parquet files in data/processed/
        - .h5 dataset files

        These data and model files are slowing down my search operations. I can
        fix this by creating (or updating) a .claudeignore file to exclude them.

        You'll still have your data and models - I just won't try to read them
        during code searches, which makes sense since they're binary/data files
        anyway.

        [Claude checks if .claudeignore exists]

        I see you already have a .claudeignore file. I'll add ML-specific patterns
        to it:

        [Claude updates .claudeignore with:]
        # Data files
        data/raw/
        data/processed/
        *.csv
        *.parquet
        *.h5
        *.hdf5

        # Model files
        *.pt
        *.pth
        *.ckpt
        *.pkl
        *.joblib
        models/weights/
        models/checkpoints/

        # But keep your data processing scripts
        !data/schema.py
        !data/README.md

        [Claude verifies]

        Perfect! Before: 1,245 files (10.5GB)
               After:   89 Python files (2.3MB)

        Now my searches will be much faster since I'm only looking at your code,
        not your datasets and models. Try your search again!
```

## Key Teaching Points

1. **Performance diagnosis**: Identify what's causing slowness
2. **Data awareness**: Recognize ML projects have different needs
3. **Selective inclusion**: Use `!` patterns to keep important files like schemas
4. **Metrics**: Show concrete before/after numbers
5. **User reassurance**: Clarify files still exist, just excluded from context

## Advanced Variation

If user wants to analyze specific data files:

```
User: But I need you to look at one specific dataset sometimes.

Claude: No problem! There are two approaches:

        1. Use the Read tool with the specific file path:
           "Read data/raw/sample.csv"
           Even though it's in .claudeignore, direct reads still work.

        2. Temporarily include a specific file:
           Add to .claudeignore: !data/raw/important_sample.csv

        Which approach would you prefer?
```
