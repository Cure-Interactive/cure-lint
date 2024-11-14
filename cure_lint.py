import tkinter as tk
from tkinter import filedialog

# Import the whole module with an alias
import cure_terminal as ct

# Set up a basic GUI to enable drag-and-drop file selection
root = tk.Tk()
root.withdraw()  # Hide the main window

# Open a file dialog to allow the user to select a Python script (.py or .pyw)
file_path = filedialog.askopenfilename(
    title="Select a Python file",
    filetypes=[("Python files", "*.py *.pyw")]
)

if not file_path:
    ct.Print.status("Error", "No file selected.")
else:
    ct.Print.status("Info", f"Scanning file: `[[COLOR_OFF]]{file_path}[[COLOR_ON]]`...")

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

    # Analyze each line in the selected file
    lines_with_mismatched_quotes = []
    with open(file_path, 'r') as file:
        for line_num, line in enumerate(file, 1):
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

    # Print results
    if lines_with_mismatched_quotes:
        ct.Print.status("Error", "Lines containing non-alternating quotes inside formatted strings:")
        for line_num, line, positions, first_col in lines_with_mismatched_quotes:
            # Print line and all column positions
            ct.Print.status("Error", f"Line `[[COLOR_OFF]]{line_num}[[COLOR_ON]]`, Columns `[[COLOR_OFF]]{positions}[[COLOR_ON]]`:")
            
            # Print the line with exact indentation
            ct.Print.color("red", f"`{line.rstrip()}`")

            CARET_ADJUSTMENT = 2

            # Adjust caret position for prefix and indentation
            adjusted_positions = [pos + CARET_ADJUSTMENT for pos in positions]  # Account for 1-based indexing in display

            # Generate the caret line with adjustments for prefix and indentation
            caret_line = ''.join('^' if i in adjusted_positions else ' ' for i in range(1, len(line.rstrip()) + CARET_ADJUSTMENT))
            print(caret_line.rstrip())
    else:
        ct.Print.status("Success", "No lines found with non-alternating quotes inside formatted strings.")
