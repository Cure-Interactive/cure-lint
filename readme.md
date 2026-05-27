# Cure Lint

Small Python lint helper for finding quote conflicts inside f-string expressions.

## What It Checks

`cure_lint.py` opens a file picker, scans the selected Python file, and reports f-string expressions that appear to reuse the same quote style as the outer f-string. Findings are printed with line numbers and caret markers.

## Requirements

- Python 3.10+
- Tkinter, usually included with standard Python installers

This standalone repository vendors the small `cure_utility/` helper package used by the script.

## Run

```bash
python cure_lint.py
```

Then select a Python file when the file dialog opens.

## Files

- `cure_lint.py`: main scanner
- `cure_lint_testfile.py`: small sample file for trying the scanner
- `cure_utility/`: vendored helper package
