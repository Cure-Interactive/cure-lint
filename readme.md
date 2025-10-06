# Cure Lint

This Python script helps identify non-alternating quotes inside f-strings in Python files. It scans each line of a selected Python file, looking for occurrences of quotes that are the same type as the outer f-string delimiter within expressions. This is useful for catching quote usage that might confuse the code parser or lead to unexpected results.

## Features

- **Drag-and-Drop File Selection**: Uses a basic GUI file dialog to select the Python file to scan.
- **Quote Matching Detection**: Identifies non-alternating quotes within f-string expressions, ignoring escaped quotes.
- **Visual Caret Indicator**: For each detected issue, prints the line with caret symbols (`^`) to indicate the exact positions of non-alternating quotes.

## Prerequisites

- Python 3.x
- `tkinter` module (pre-installed with Python)

## Usage

1. Run the script from the command line:
   ```bash
   python python_lint_quote.py
   ```
2. A file dialog will open, allowing you to select a Python file to analyze.
3. The script will print any lines containing non-alternating quotes with visual indicators of the positions in the console.

## Example Output

If non-alternating quotes are found, the output might look like this:

```bash
Scanning file: /path/to/your_script.py
Lines containing non-alternating quotes inside formatted strings:
Line 9, Columns [47, 73]:
`print(f"Text with function call {function_call("string with double quotes")} here.")  # Bad`
                                                ^                         ^
Line 10, Columns [47, 73]:
`print(f'Text with function call {function_call('string with single quotes')} here.')  # Bad`
                                                ^                         ^
```

If no issues are found, the script will output:

```bash
No lines found with non-alternating quotes inside formatted strings.
```

## Color Key

The script uses ANSI color codes for better readability in terminals that support it:

- **Red**: Indicates lines with issues and positions of non-alternating quotes.
- **Green**: Confirms no issues were found.
- **Cyan**: Displays the path of the selected file.

## License

This project is open source and available under the MIT License.
