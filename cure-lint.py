import tkinter as tk
from tkinter import filedialog

# Import the whole module with an alias
import cure_utility as cu

cu.Option.set('duration_style', 'symbol')
cu.Option.set('step_count', 2)

cu.Print.title("Cure Python Lint Begin")

# Set up a basic GUI to enable drag-and-drop file selection
root = tk.Tk()
root.withdraw()  # Hide the main window

cu.Print.step("Select a Python file")

# Open a file dialog to allow the user to select a Python script (.py or .pyw)
file_path = filedialog.askopenfilename(
    title="Select a Python file",
    filetypes=[("Python files", "*.py *.pyw")]
)

if not file_path:
    cu.Print.status("Error", "No file selected.")

else:
    cu.Print.status("Info", f"Selected file: `[[COLOR_OFF]]{file_path}[[COLOR_ON]]`...\n")

    cu.Print.step()

    cu.Print.step("Scan file")

    cu.Print.status("Info", f"Scanning file: `[[COLOR_OFF]]{file_path}[[COLOR_ON]]`...\n")

    def find_non_alternating_quotes(line):
        """
        Identifies lines with non-alternating quotes inside formatted strings.
        Ignores escaped quotes within expressions.
        """
        i = 0
        length = len(line)
        in_fstring = False
        outer_quote = None
        brace_depth = 0
        quote_positions = []

        while i < length:
            char = line[i]

            # Check for the start of an f-string
            if char == 'f' and i + 1 < length and line[i + 1] in ['"', "'"]:
                in_fstring = True
                outer_quote = line[i + 1]  # Set the outer quote (either " or ')
                i += 1  # Skip the outer quote
            elif in_fstring:
                # Check for the end of the f-string
                if char == outer_quote and brace_depth == 0:
                    in_fstring = False
                    outer_quote = None
                # Check for the start of an expression
                elif char == '{':
                    brace_depth += 1
                # Check for the end of an expression
                elif char == '}':
                    if brace_depth > 0:
                        brace_depth -= 1
                # Check inside an expression for non-alternating quotes
                elif brace_depth > 0:
                    # Ignore escaped quotes by checking if the previous character is a backslash
                    if ((outer_quote == '"' and char == '"' and (i == 0 or line[i - 1] != '\\')) or
                        (outer_quote == "'" and char == "'" and (i == 0 or line[i - 1] != '\\'))):
                        # Flag only the position where inner quote matches the outer f-string quote type
                        quote_positions.append(i)
            i += 1

        return quote_positions if quote_positions else None

    def find_trailing_whitespace(line):
        """
        Identifies lines with trailing whitespace (spaces or tabs).
        """
        stripped_line = line.rstrip("\r\n")  # Remove only newline characters
        return stripped_line.endswith(" ") or stripped_line.endswith("\t")

    # Read all lines to get the file length for progress tracking
    with open(file_path, 'r') as file:
        lines = file.readlines()
        total_lines = len(lines)

    # Initialize progress bar
    cu.Progress.print_single(0, total_lines, custom_suffix=f"({{i}} of {{total}} lines)")

    # Analyze each line in the selected file
    lines_with_mismatched_quotes = []
    lines_with_trailing_whitespace = []
    for line_num, line in enumerate(lines, 1):
        # Update progress
        cu.Progress.print_single(line_num, total_lines, custom_suffix=f"({{i}} of {{total}} lines)")

        quote_positions = find_non_alternating_quotes(line)
        if quote_positions:
            # Capture the first column where a non-alternating quote appears
            first_col = quote_positions[0] + 1  # Column number starts at 1

            # Print the line with offending characters wrapped in color tags
            highlighted_line = ""
            for i, char in enumerate(line.rstrip()):
                if i in quote_positions:
                    highlighted_line += f"[[COLOR_OFF]]{char}[[COLOR_ON]]"
                else:
                    highlighted_line += char

            lines_with_mismatched_quotes.append((line_num, highlighted_line, quote_positions, first_col))

        # Check for trailing whitespace
        if find_trailing_whitespace(line):
            lines_with_trailing_whitespace.append(line_num)

    cu.Print.status('Info', "Results:\n")

    # Print results
    if lines_with_mismatched_quotes:
        cu.Print.status("Error", "Lines containing non-alternating quotes inside formatted strings:\n")
        for line_num, line, positions, first_col in lines_with_mismatched_quotes:
            # Print line and all column positions
            cu.Print.status("Error", f"Line `[[COLOR_OFF]]{line_num}[[COLOR_ON]]`, Columns `[[COLOR_OFF]]{positions}[[COLOR_ON]]`:")

            # Print the line with exact indentation
            cu.Print.color("red", f"`{line.rstrip()}`")

            CARET_ADJUSTMENT = 2

            # Adjust caret position for prefix and indentation
            adjusted_positions = [pos + CARET_ADJUSTMENT for pos in positions]  # Account for 1-based indexing in display

            # Generate the caret line with adjustments for prefix and indentation
            caret_line = ''.join('^' if i in adjusted_positions else ' ' for i in range(1, len(line.rstrip()) + CARET_ADJUSTMENT))
            print(caret_line.rstrip())
    else:
        cu.Print.status("Success", "No lines found with non-alternating quotes inside formatted strings.")

    print()

    if lines_with_trailing_whitespace:
        cu.Print.status("Warning", "Lines with trailing whitespace (spaces or tabs):\n")
        for line_num in lines_with_trailing_whitespace:
            cu.Print.color("yellow", f"Line `[[COLOR_OFF]]{line_num}[[COLOR_ON]]` has trailing whitespace.")
    else:
        cu.Print.status("Success", "No lines found with trailing whitespace.")

print()
cu.Print.step()

cu.Print.title("Cure Python Lint End")
